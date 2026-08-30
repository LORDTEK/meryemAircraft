# -*- coding: utf-8 -*-
"""Referans karsilastirmasindaki GEOMETRI farkini kaldir.

Referans veri (NAS-2016-01, Tablo 7.1 ve 7.2) sekiz kodun ayni vakada
verdigi degerleri tasiyor. Bizim iki kurulumumuz da o bandin DISINDA,
ters yonlerde:

    SA   bizim 0,00842   referans 0,00812 - 0,00838   (sekizinin de ustunde)
    SST  bizim 0,00769   referans 0,00808 - 0,00821   (dordunun de altinda)

Ters yonlerde olmalari, tek bir ortak yanliligin ikisini birden
aciklayamayacagini soyler; ama ortak bir yanlilik VARSA once o
kaldirilmalidir, cunku o kaldirilmadan modele ozgu kusur dogru
olculemez.

Belirlenen uc kosul farkindan biri tam da boyle ortak bir yanlilik
uretir: GEOMETRI. Biz kapali firar kenarli NACA 0012 kullaniyoruz (azami
kalinlik veterin %12'si); TMR'nin aglari ise acik formulden turetilip
1.008930411365 ile olceklenmis, azami kalinligi %11.894 olan bir kopya.
Bizimki yaklasik %0,9 daha KALIN, yani C_D'yi yukari itmesi beklenir --
SA'nin bandin ustunde cikmasinin yonuyle uyumlu.

Bu betik ayni iki modeli TMR'nin kendi profiliyle kosar. Profilin
katsayilari kaynaktan birinci elden okunmustur (cagi.naca4, kapali="tmr").

BEKLENTI ONCEDEN: TMR profiliyle iki modelin de C_D'si DUSMELIDIR.
Dususun buyuklugu geometrinin payini verir. Dusus %1 mertebesindeyse
geometri ortak yanliligin bir parcasidir ama SST'deki %5'lik acigi
aciklamaz; o zaman aciklama duvar isleminde ya da modelin kendisinde
aranir.
"""
import json, os, subprocess, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kur import kur                                    # noqa: E402
from kuvvet import hesapla                             # noqa: E402
from kilit import Kilit                                # noqa: E402

KOK = "/tmp/tmrgeo"
# NAS-2016-01, Tablo 7.1 ve 7.2, alfa = 0
REF = {"kOmegaSST": dict(ort=0.00812, alt=0.00808, ust=0.00821),
       "SpalartAllmaras": dict(ort=0.00819, alt=0.00812, ust=0.00838)}
# Ayni kurulumun %12 kapali profille verdigi degerler (olculdu)
ONCEKI = {"kOmegaSST": 0.00769, "SpalartAllmaras": 0.00842}

if __name__ == "__main__":
    with Kilit(KOK):
        yol = os.path.join(KOK, "sonuc.json")
        cikti = json.load(open(yol)) if os.path.exists(yol) else []
        yapilan = {d["model"] for d in cikti}
        for m in ("kOmegaSST", "SpalartAllmaras"):
            if m in yapilan:
                continue
            vaka = os.path.join(KOK, m)
            bilgi = kur(vaka, kod="0012", Re=6e6, alfa=0.0, yplus=1.0,
                        n_profil=256, n_normal=96, n_iz=64,
                        R=20.0, Xiz=20.0, kapali="tmr",
                        adim=3000, yaz_araligi=1500, model=m)
            print("[%s + TMR profili] %d hucre -- cozuluyor"
                  % (m, bilgi["hucre"]), flush=True)
            subprocess.run([os.path.join(BURA, "kos.sh"), vaka, "4"],
                           check=True, stdout=subprocess.DEVNULL)
            r = hesapla(vaka, alfa=0.0, mertebe=2)
            d = (r["CD"] / ONCEKI[m] - 1) * 100
            print("   C_D=%.6f   (%%12 profille %.5f idi, degisim %+.2f%%)"
                  % (r["CD"], ONCEKI[m], d), flush=True)
            print("   referans bandi %.5f - %.5f  ->  %s"
                  % (REF[m]["alt"], REF[m]["ust"],
                     "ICINDE" if REF[m]["alt"] <= r["CD"] <= REF[m]["ust"]
                     else "DISINDA"), flush=True)
            cikti.append(dict(model=m, CD=r["CD"], CD_b=r["CD_basinc"],
                              CD_v=r["CD_viskoz"], yp=r["yplus_ort"],
                              CL=r["CL"], onceki=ONCEKI[m]))
            json.dump(cikti, open(yol, "w"), indent=1)

        print()
        print("  model              %12       TMR      degisim   referans      durum")
        for d in cikti:
            R = REF[d["model"]]
            print("  %-16s %.5f  %.5f   %+.2f%%   %.5f-%.5f  %s"
                  % (d["model"], d["onceki"], d["CD"],
                     (d["CD"] / d["onceki"] - 1) * 100, R["alt"], R["ust"],
                     "icinde" if R["alt"] <= d["CD"] <= R["ust"] else "DISINDA"))
