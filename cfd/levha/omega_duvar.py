# -*- coding: utf-8 -*-
"""Duz levhada omega duvar isleminin taranmasi -- KESIN HEDEFLI DOGRULAMA.

DURUM. duzlevha.py sifir basinc gradyaninda olctu:

    nu_t / (kappa u_tau y)     SA 0,969      SST 0,859

SA olcumun kendisini dogruluyor (karisim uzunlugu dogrudan kappa u_tau y
uzerine kurulu). SST ise kendi kapanis sabitlerinin ZORUNLU kildigi
degerin %14 altinda. Bu, profildeki 0,880 ile ayni. Yani kusur ters
basinc gradyaninin fizigi degil; basinc gradyanindan bagimsiz.

Ayrisim da degil: profil aginin uc kademesinde oran 0,880 / 0,880 / 0,882.

Ayrica NACA vakasinda olculdu ki duvar omega kosulu C_D uzerinde en
buyuk kaldirac: duvar fonksiyonu yerine yuze fixedValue 6nu/(beta1 d1^2)
konunca C_D 0,00769'dan 0,00870'e cikti (+%13). Bu, referans bandini bu
sefer YUKARIDAN asiyor. Demek ki dogru ayar ikisinin ARASINDA bir yerde.

BU TARAMA. Duz levha bu isin dogru tezgahi, cunku hedef KESIN ve
disaridan hicbir olcum gerektirmiyor: denge halindeki log tabakasinda
modelin kendi sabitleri nu_t = kappa u_tau y'yi zorunlu kilar.

Duvar omega kosulu iki onlu bir aralikta taranir; yaninda serbest akis
ve ag da bu vakada ayrica elenir.

BEKLENTI ONCEDEN:
  (a) Oran, taranan aralikta 1,00'i KESIYORSA duvar omega islemi bu
      acigi yonetiyor demektir. O zaman 1,00'i veren ayar bulunur ve
      NACA vakasina uygulanir. Bu bir ayar UYDURMA degildir: hedef,
      modelin kendi kapanis sartidir, olculmus bir surukleme degil.
      Elde edilen C_D yine de bagimsiz kalir, cunku dogrulamada
      kullanilan buyukluk (log tabakasi dengesi) ile karsilastirilan
      buyukluk (surukleme) ayni sey degildir.
  (b) Alti varyantin hepsi 0,86 civarinda kaliyorsa duvar islemi bu
      acigi yonetmiyordur; o zaman kusur OpenFOAM'in kOmegaSST
      uygulamasinin kendisindedir ve bu, kaynagindan okunmadan
      duzeltilemez -- rapor edilir, duzeltilmez.
"""
import json, math, os, subprocess, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
import duzlevha                                          # noqa: E402
from duzlevha import KOS                                 # noqa: E402
from duvaryasasi import profil, KAPPA, BETA_YILDIZ       # noqa: E402
from kilit import Kilit                                  # noqa: E402

KOK = "/tmp/levha_omega"

#  ad              model         ek kur() argumanlari
VARYANT = [
    ("taban",        "kOmegaSST", {}),
    ("serbest_100x_az", "kOmegaSST", dict(om_carpan=0.01)),
    ("ag_ince",      "kOmegaSST", dict(ny=192, y1=2e-6)),
    ("duvar_1x",     "kOmegaSST", dict(duvar_omega=1.0)),
    ("duvar_10x",    "kOmegaSST", dict(duvar_omega=10.0)),
    ("duvar_100x",   "kOmegaSST", dict(duvar_omega=100.0)),
]


def olc(vaka, x=1.0):
    """Log tabakasindaki azami nu_t/(kappa u_tau y) ve orada k, omega."""
    u_tau, nu, p = profil(vaka, x, ust=None)
    en, nokta = -1.0, None
    for d in p:
        yp = d["y"] * u_tau / nu
        if not 30 <= yp <= 600:
            continue
        r = d["nut"] / (KAPPA * u_tau * d["y"])
        if r > en:
            en, nokta = r, d
    kp = (nokta["k"] / u_tau ** 2) * math.sqrt(BETA_YILDIZ) \
        if "k" in nokta else None
    om = nokta["omega"] / (u_tau / (math.sqrt(BETA_YILDIZ) * KAPPA * nokta["y"])) \
        if "omega" in nokta else None
    return dict(u_tau=u_tau, Cf=2 * u_tau ** 2, oran=en,
                yp=nokta["y"] * u_tau / nu, kp=kp, om=om)


if __name__ == "__main__":
    with Kilit(KOK):
        yol = os.path.join(KOK, "sonuc.json")
        cikti = json.load(open(yol)) if os.path.exists(yol) else []
        yapilan = {d["ad"] for d in cikti}
        for ad, model, ek in VARYANT:
            if ad in yapilan:
                continue
            vaka = os.path.join(KOK, ad)
            duzlevha.kur(vaka, model, **ek)
            print("[%s] cozuluyor" % ad, flush=True)
            r = subprocess.run(["bash", "-c", KOS % vaka])
            if r.returncode != 0:
                print("   KOSULAMADI (%d)" % r.returncode, flush=True)
                cikti.append(dict(ad=ad, hata=r.returncode))
            else:
                m = olc(vaka)
                print("   C_f=%.6f  nu_t/(k.u.y)=%.3f @y+%.0f  k+/3,333=%.3f"
                      "  omega/denge=%.3f"
                      % (m["Cf"], m["oran"], m["yp"], m["kp"], m["om"]),
                      flush=True)
                cikti.append(dict(ad=ad, **m))
            json.dump(cikti, open(yol, "w"), indent=1)

        print()
        print("  varyant            C_f     nu_t/(k.u.y)   k+/3,333  omega/denge")
        for d in cikti:
            if "oran" not in d:
                print("  %-16s (kosulamadi)" % d["ad"])
            else:
                print("  %-16s %.6f    %.3f        %.3f      %.3f"
                      % (d["ad"], d["Cf"], d["oran"], d["kp"], d["om"]))
        print("  HEDEF: nu_t/(kappa u_tau y) = 1,000  (modelin kendi kapanis sarti)")
        print("""  NOT -- 1,000 hedefi DENGE halindeki log tabakasi icin kesindir.
  Duz levhanin sinir tabakasi akis yonunde gelistigi icin dogru
  kurulmus bir iki denklemli model de bunu tam tutturmak zorunda
  degildir; bkz. dogrulama.md, 'DUZELTME' bolumu. Bu yuzden mutlak
  sapma bir kusur olcusu DEGIL, isarettir. Anlamli olan varyantlar
  arasindaki KARSILASTIRMADIR.""")
        print("  SA ayni vakada 0,969 veriyor -- olcumun ic denetimi.")
