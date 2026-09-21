# -*- coding: utf-8 -*-
"""ADIM 10 -- BOYUTLANDIRMA DONGUSUNUN ANALITIK KAPANISI.

Dort kapanis. Her biri IKI bagimsiz model girdisiyle beslenir:

    surukleme belirsizligi   C_D0 in {0,0285 (elverisli), 0,0381 (olumsuz)}
    palet ailesi SECIMI      eta_p in {0,632 (alt), 0,683 (ust)}

Yayimlanan 0,0248 KULLANILMAZ: drag_sweep.py onu tutarli braketin IKI
UCUNUN DA ALTINA koydu. Dort dis okuyucu da braket uzerinde kapanmayi
soyledi.

GIRDI YUVASI -- Tur 51'de ChatGPT ve Grok bir cift sayim yakaladi, ve
kod denetlendi, haklilardi. Ayrintisi aero/closure_inputs.py'de:
  * L/D yuvasina AERODINAMIK oran girer, L/De DEGIL.
  * eta_p IKI terimi birden olcekler: eta_zincir (menzil) ve eta_seyir
    (seyir gucu -> motor boyutu). Yalniz birini olceklemek motoru eski
    pervaneye, menzili yeni pervaneye gore hesaplamak olur.
gorev_ile() bunu zaten dogru yapiyor; burada yeniden kullaniliyor.

KURULUS SINAMASI: yayimlanan varsayimda (C_D0 = 0,0248 rotorsuz,
eta_p = 0,80) kurulus makalenin 50,1 kg / L/D 11,88 / 1583 km'sini
yeniden uretmelidir. Uretmezse betik DURUR ve hicbir sayi yayimlanmaz.
"""
import os
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)

import baseline as BL                                     # noqa: E402
import drag_sweep as DS                                   # noqa: E402
from chain_resolve import gorev_ile                       # noqa: E402

CD0 = {"elverisli": 0.0285, "olumsuz": 0.0381}
ETA_P = {"ust": 0.683, "alt": 0.632}
YAYIMLANAN_CD0 = 0.0248


def kapat(cd0, eta_p, rotorlu=True):
    """Tek kapanis: (C_D0, eta_p) -> tam kapali cevrim sonucu."""
    ld_temiz, a_carpan = DS.zincir(cd0, rotorlu=rotorlu)
    g = gorev_ile(eta_p)
    m = BL.mimariler(f_tampon=0.036)[0]          # A, kuyruk ustu
    m.LD_carpan = a_carpan
    r = BL.boyutlandir(m, ld_temiz, g=g)
    r["cd0"], r["eta_p"], r["LD_temiz"] = cd0, eta_p, ld_temiz
    return r


def main():
    print("ADIM 10 -- BOYUTLANDIRMA DONGUSUNUN ANALITIK KAPANISI")
    print("=" * 78)
    print()

    print("KURULUS SINAMASI -- yayimlanan varsayim yayimlanan ucagi vermeli")
    ref = kapat(YAYIMLANAN_CD0, 0.80, rotorlu=False)
    hedef = dict(MTOW=50.1, LD=11.88, menzil=1583.0)
    tamam = True
    for k, h in hedef.items():
        sap = abs(ref[k] - h) / h
        bayrak = "ok" if sap < 0.02 else "SAPMA"
        if sap >= 0.02:
            tamam = False
        print("  %-8s hesaplanan %8.2f   yayimlanan %8.2f   %+5.1f %%  %s"
              % (k, ref[k], h, 100 * (ref[k] / h - 1), bayrak))
    if not tamam:
        print()
        print("  >>> DUR -- kurulus yayimlanan ucagi uretmiyor. Sayi yayimlanmaz.")
        raise SystemExit(1)
    print("  kurulus dogrulandi.")
    print()

    print("DORT KAPANIS -- braket uzerinde, yayimlanan 0,0248 DISARIDA")
    print()
    print("%-3s %-8s %-7s %7s %8s %8s %8s %8s %9s"
          % ("", "C_D0", "eta_p", "L/D", "MTOW", "f_bos", "P_askı", "motor", "menzil"))
    print("%-3s %-8s %-7s %7s %8s %8s %8s %8s %9s"
          % ("", "", "", "", "kg", "", "kW", "kW", "km"))
    print("-" * 78)
    sonuc = {}
    ad = "ABCD"
    i = 0
    for dk in ("olumsuz", "elverisli"):
        for ek in ("alt", "ust"):
            r = kapat(CD0[dk], ETA_P[ek])
            sonuc[ad[i]] = r
            if r.get("kapanmadi"):
                print("%-3s %-8.4f %-7.3f   KAPANMADI  f_bos %.3f"
                      % (ad[i], CD0[dk], ETA_P[ek], r["f_bos"]))
            else:
                print("%-3s %-8.4f %-7.3f %7.2f %8.1f %8.3f %8.2f %8.2f %9.0f"
                      % (ad[i], CD0[dk], ETA_P[ek], r["LD"], r["MTOW"],
                         r["f_bos"], r["P_hover"], r["motor_kW"], r["menzil"]))
            i += 1
    print("-" * 78)
    print()

    iyi = [r for r in sonuc.values() if not r.get("kapanmadi")]
    if len(iyi) < 4:
        print("!! Dort kapanistan %d tanesi KAPANMADI." % (4 - len(iyi)))
        print()

    def yay(anahtar):
        v = [r[anahtar] for r in iyi]
        return min(v), max(v), 100 * (max(v) / min(v) - 1)

    print("YAYILIMLAR (dort kapanis boyunca)")
    for k, ad2, bir in (("MTOW", "kalkis kutlesi", "kg"),
                        ("menzil", "menzil", "km"),
                        ("motor_kW", "motor derecesi", "kW"),
                        ("P_hover", "askı gucu", "kW"),
                        ("faydali_pay", "faydali yuk payi", "")):
        lo, hi, pct = yay(k)
        print("  %-18s %8.2f - %8.2f %-3s   yayilim %5.1f %%" % (ad2, lo, hi, bir, pct))
    print()

    print("HANGI GIRDI DAHA BASKIN?")
    for etiket, cift in (("surukleme braketi (ayni palet)", ("A", "C")),
                         ("palet ailesi (ayni surukleme)", ("A", "B"))):
        a, b = sonuc[cift[0]], sonuc[cift[1]]
        print("  %-32s MTOW %+5.1f %%   menzil %+6.1f %%"
              % (etiket, 100 * (b["MTOW"] / a["MTOW"] - 1),
                 100 * (b["menzil"] / a["menzil"] - 1)))
    print()
    print("En iyi palet ailesi (eta_p 0,683) kapanistan SONRA da en iyi mi?")
    for dk, p in (("olumsuz", ("A", "B")), ("elverisli", ("C", "D"))):
        alt, ust = sonuc[p[0]], sonuc[p[1]]
        print("  %-11s  alt eta_p menzil %6.0f km / ust %6.0f km  ->  %s"
              % (dk, alt["menzil"], ust["menzil"],
                 "EVET" if ust["menzil"] > alt["menzil"] else "HAYIR"))


if __name__ == "__main__":
    main()
