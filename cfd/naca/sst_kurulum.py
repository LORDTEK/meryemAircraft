# -*- coding: utf-8 -*-
"""SST kurulumundaki kusuru yalitmak icin ayar taramasi.

DURUM: Referans veriye gore (NAS-2016-01, Tablo 7.1-7.5) bizim
Spalart-Allmaras kurulumumuz dogru, k-omega SST kurulumumuz degil.

  Overflow SA  (897x257)   0,00838      bizim SA   0,00842   (+%0,5)
  Overflow SST (897x257)   0,00821      bizim SST  0,00769   (-%6,3)

SA ile SST arasinda bizde %9,5 fark var, Overflow'da %2,1. Ikisi ayni agi,
ayni semalari, ayni kuvvet integralini ve ayni duvar mesafesini
kullaniyor; ayrilan tek sey turbulans modeli ve ONUN sinir kosullaridir.

Bu betik SST'ye ozgu ayarlari tek tek degistirir. serbest.py serbest akis
degerlerini zaten tariyor; burada DUVAR islemi ve alan sinir kosullari
var.

Denenen degiskenler:
  taban        simdiki kurulum -- omegaWallFunction blended true,
               nut duvarda nutLowReWallFunction, k duvarda fixedValue 0
  omega_ham    omegaWallFunction blended false
  nut_hesap    nut duvarda 'calculated' (modele birakilir, sifirlanmaz)
  k_dusukRe    k duvarda kLowReWallFunction

BEKLENTI ONCEDEN: bir degisken C_D'yi 0,0081 bandina tasiyorsa kusur
odur. Hicbiri tasimazsa kusur bu dordusunde degildir ve siradaki supheli,
OpenFOAM'in kOmegaSST uretim terimi ile TMR'nin tanimi arasindaki fark
olur -- o da modelin kendi kaynagindan okunarak sinanmalidir.
"""
import json, os, re, subprocess, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kur import kur                                    # noqa: E402
from kuvvet import hesapla                             # noqa: E402
from kilit import Kilit                                # noqa: E402

KOK = "/tmp/sstkurulum"
REF = 0.00821          # Overflow SST, 897x257 (NAS-2016-01 Tablo 7.5)


def duzenle(vaka, hangi):
    """0/ alanlarindaki duvar kosullarini degistirir."""
    if hangi == "omega_ham":
        p = os.path.join(vaka, "0", "omega")
        s = open(p).read().replace("blended         true;", "blended         false;")
        open(p, "w").write(s)
    elif hangi == "nut_hesap":
        p = os.path.join(vaka, "0", "nut")
        s = open(p).read()
        s = s.replace("        type            nutLowReWallFunction;\n"
                      "        value           uniform 0;\n",
                      "        type            calculated;\n"
                      "        value           uniform 0;\n", 1)
        open(p, "w").write(s)
    elif hangi == "k_dusukRe":
        p = os.path.join(vaka, "0", "k")
        s = open(p).read()
        s = s.replace("        type            fixedValue;\n"
                      "        value           uniform 1e-14;\n",
                      "        type            kLowReWallFunction;\n"
                      "        value           uniform 1e-14;\n", 1)
        open(p, "w").write(s)


VARYANT = ["taban", "omega_ham", "nut_hesap", "k_dusukRe"]

if __name__ == "__main__":
    with Kilit(KOK):
        yol = os.path.join(KOK, "sonuc.json")
        cikti = json.load(open(yol)) if os.path.exists(yol) else []
        yapilan = {d["varyant"] for d in cikti}
        for v in VARYANT:
            if v in yapilan:
                continue
            vaka = os.path.join(KOK, v)
            kur(vaka, kod="0012", Re=6e6, alfa=0.0, yplus=1.0,
                n_profil=256, n_normal=96, n_iz=64, R=20.0, Xiz=20.0,
                adim=3000, yaz_araligi=1500)
            duzenle(vaka, v)
            print("[%s] cozuluyor" % v, flush=True)
            r = subprocess.run([os.path.join(BURA, "kos.sh"), vaka, "4"],
                               stdout=subprocess.DEVNULL)
            if r.returncode != 0:
                print("   COZULEMEDI (cikis %d) -- muhtemelen bu sinir kosulu"
                      " bu surumde yok" % r.returncode, flush=True)
                cikti.append(dict(varyant=v, CD=None, hata=r.returncode))
                json.dump(cikti, open(yol, "w"), indent=1)
                continue
            k = hesapla(vaka, alfa=0.0, mertebe=2)
            print("   C_D=%.6f  viskoz=%.6f  y+ %.2f   referansa gore %+.1f%%"
                  % (k["CD"], k["CD_viskoz"], k["yplus_ort"],
                     (k["CD"] / REF - 1) * 100), flush=True)
            cikti.append(dict(varyant=v, CD=k["CD"], CD_v=k["CD_viskoz"],
                              CD_b=k["CD_basinc"], yp=k["yplus_ort"]))
            json.dump(cikti, open(yol, "w"), indent=1)
        print()
        print("  varyant        C_D      referansa gore")
        for d in cikti:
            if d.get("CD") is None:
                print("  %-12s  (cozulemedi)" % d["varyant"])
            else:
                print("  %-12s %.6f   %+.1f%%"
                      % (d["varyant"], d["CD"], (d["CD"] / REF - 1) * 100))
        print("  referans: Overflow SST 897x257 = %.5f" % REF)
