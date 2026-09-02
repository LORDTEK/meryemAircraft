# -*- coding: utf-8 -*-
"""SINAMA: uc boyutlu ag, iki boyutlu sonucu YENIDEN URETMELI.

NEDEN BU SINAMA. Uc boyutlu ag ureteci yeni koddur; dogrulanmamistir.
Uzerine kanat kurup "iste uc boyutlu suruklenme" demek, dogrulanmamis bir
araci sonuc uretmekte kullanmak olur. Once aracin kendisi sinanmali.

Sinamanin gucu su: sabit kesitli, ok acisiz, sivrilmesiz bir kanat iki
ucunda da symmetryPlane ile kosuldugunda, akis aciklik boyunca degismez --
yani problem FIZIKSEL OLARAK iki boyutludur. Sonuc, dogrulanmis iki boyutlu
kurulumun sonucuyla ayni cikmalidir. Cikmazsa hata yeni kodda demektir ve
nerede oldugu aranabilir.

Vakalar arasindaki TEK fark agdir: alan dosyalari, semalar, cozucu ayarlari
ve turbulans kurulumu naca/kur.py'den, ikisine de ayni sekilde geliyor
(bkz. kur3b.py).

BEKLENTI (kosmadan once yaziliyor):

  (a) C_D, iki boyutlu degerden binde birkacten fazla sapmamali. Ayni
      izgara, ayni semalar, ayni model; kalan tek fark aciklik yonundeki
      ayriklastirmanin varligi ve o yonde turev sifir olmali.

  (b) Aciklik dilim sayisi (NK) 2'den 5'e cikarildiginda sonuc DEGISMEMELI.
      Degisirse, aciklik yonu cozume sizmis demektir -- ki fiziksel olarak
      sizmamali. Bu, (a)'dan bagimsiz ikinci bir denetimdir: (a) tek basina
      tesadufen tutabilir, (b) tutmaz.

  (c) C_L, iki boyutlu gibi sifir olmali (alfa=0, simetrik kesit).

  Sapma binde birkacin uzerindeyse: uc boyutlu ureteci HATALIDIR ve
  kanat hesabina gecilmez. Boyle cikarsa oyle yazilir.

Referans: NACA 0012, Re=6e6, alfa=0, SA, ayni izgara (256x113x64, R=100).
"""
import json
import os
import subprocess
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "naca"))
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kanatagi import duz_kanat                        # noqa: E402
from kur3b import kur3b                               # noqa: E402
from kur import kur as kur2b                          # noqa: E402
from kuvvet import hesapla                            # noqa: E402
from kilit import Kilit                               # noqa: E402

KOK = "/tmp/kanat_sonsuz"
AG = dict(n_profil=256, n_normal=113, n_iz=64, R=100.0, Xiz=100.0)
ORTAK = dict(kod="0012", Re=6e6, alfa=0.0, yplus=1.0,
             adim=3000, yaz_araligi=1500, model="SpalartAllmaras", **AG)
ACIKLIK = 0.1                 # veter cinsinden; symmetryPlane oldugu icin
                              # deger onemsiz -- akis aciklikta degismiyor
NK = [2, 3, 5]                # dilim sayisi taramasi


def kos(vaka, cek=4):
    subprocess.run([os.path.join(BURA, "kos3b.sh"), vaka, str(cek)],
                   check=True)


if __name__ == "__main__":
    with Kilit(KOK):
        os.makedirs(KOK, exist_ok=True)
        yol = os.path.join(KOK, "sonuc.json")
        cikti = json.load(open(yol)) if os.path.exists(yol) else []
        yapilan = {d["ad"] for d in cikti}

        # --- iki boyutlu referans, AYNI kod yolundan yeniden uretiliyor
        if "2b" not in yapilan:
            v = os.path.join(KOK, "2b")
            kur2b(v, **ORTAK)
            subprocess.run([os.path.join(BURA, "..", "naca", "kos.sh"), v, "4"],
                           check=True)
            r = hesapla(v, alfa=0.0, mertebe=2)
            cikti.append(dict(ad="2b", nk=0, **{k: r[k] for k in
                              ("CD", "CL", "CD_viskoz", "CD_basinc")}))
            json.dump(cikti, open(yol, "w"), indent=1)
            print("  2B  C_D=%.6f  C_L=%.3e" % (r["CD"], r["CL"]), flush=True)

        # --- uc boyutlu, dilim sayisi taramasi
        for nk in NK:
            ad = "3b-nk%d" % nk
            if ad in yapilan:
                continue
            v = os.path.join(KOK, ad)
            ag = duz_kanat(ACIKLIK, nk, kod="0012", Re=6e6, yplus=1.0, **AG)
            b = kur3b(v, ag, **ORTAK)
            print("  %s: %d hucre (%dx%dx%d)"
                  % (ad, b["hucre"], b["NI"], b["NJ"], b["NK"]), flush=True)
            kos(v)
            r = hesapla(v, alfa=0.0, mertebe=2)
            # Uc boyutta kuvvet, aciklik boyunca butun duvar yuzlerinden
            # toplanir; iki boyutluyla karsilastirmak icin acikliga bolunur.
            cikti.append(dict(ad=ad, nk=nk, aciklik=ACIKLIK,
                              CD=r["CD"] / ACIKLIK, CL=r["CL"] / ACIKLIK,
                              CD_viskoz=r["CD_viskoz"] / ACIKLIK,
                              CD_basinc=r["CD_basinc"] / ACIKLIK))
            json.dump(cikti, open(yol, "w"), indent=1)
            print("     C_D=%.6f  C_L=%.3e"
                  % (cikti[-1]["CD"], cikti[-1]["CL"]), flush=True)

        print()
        ref = [d for d in cikti if d["ad"] == "2b"][0]
        print("  vaka        C_D         2B'ye gore     C_L")
        for d in cikti:
            print("  %-9s  %.6f   %+8.3f%%     %+.2e"
                  % (d["ad"], d["CD"], (d["CD"] / ref["CD"] - 1) * 100, d["CL"]))
