# -*- coding: utf-8 -*-
"""AG INCELTME -- eta = 0,936 istasyonu fizik mi, ayriklastirma mi?

NEDEN. RANS-VLM karsilastirmasinda tek bir istasyon (eta = 0,936) butun
farki tasiyor: onunla esdeger yeniden dagilim 5,3 derece (3.10'un 2,6
derecelik esigini GECIYOR), onsuz 1,6 derece (geciyor). O istasyon agin
en kaba ve uc kapanisina en yakin oldugu yerde, yani ayriklastirma
kalintisi MAKUL -- ama makul gosterilmis degildir.

Istasyonu "sapan" diye dusurmedim, cunku dusurmek makalenin TERCIH
ETTIGI cevabi veriyor. Karari ag inceltmesi versin.

UC SEVIYE, ayni ayarlarla, yalnizca cozunurluk degisiyor:
  192 320   n=20  nf=128 nn=48 ni=32   (taban, kosuldu)
  444 416   n=28  nf=160 nn=64 ni=40
  681 984   n=36  nf=192 nn=64 ni=48

Ucunde de: normal="ortak", firar_taban=4, y+ = 60, alfa = 6,69.
Ucu de negatif hucresiz ve dikey olmayanlik ~80'de dogrulandi.
"""
import os, subprocess, sys, time

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from gercek import gercek_istasyonlar                   # noqa: E402
from kanatagi import KanatAgi                           # noqa: E402
from kur3b import kur3b                                 # noqa: E402

SEVIYE = (("orta", 28, 160, 64, 40), ("ince", 36, 192, 64, 48))
KOK = os.path.join(BURA, "veri", "gercek3b")
ALFA = 6.69

if __name__ == "__main__":
    for ad, n, nf, nn, ni in SEVIYE:
        v = os.path.join(KOK, ad)
        if os.path.exists(os.path.join(v, "3000")):
            print("%s zaten kosmus, atlaniyor" % ad, flush=True)
            continue
        ist, yari = gercek_istasyonlar(n=n, sikistir=True)
        ag = KanatAgi(ist, Re=1.3e6, yplus=60.0, normal="ortak",
                      firar_taban=4, n_profil=nf, n_normal=nn, n_iz=ni)
        b = kur3b(v, ag, kok="symmetryPlane", uc="serbest",
                  alfa=ALFA, Re=1.3e6, kod="0012")
        print("%s: %d hucre kuruldu" % (ad, b["hucre"]), flush=True)
        t = time.time()
        subprocess.run(["bash", os.path.join(BURA, "kos3b.sh"), v, "4"],
                       check=False)
        print("%s: cozuldu %.0f dk" % (ad, (time.time() - t) / 60), flush=True)
        subprocess.run(["bash", "-lc",
                        ". /usr/share/openfoam/etc/bashrc >/dev/null 2>&1; "
                        "cd %s && reconstructPar -latestTime > "
                        "log.reconstructPar 2>&1" % v], check=False)
        # Cozulen vaka buyuk; islemci dizinleri sonucu birlestirdikten
        # sonra silinir, yoksa uc seviye diski doldurur.
        subprocess.run(["bash", "-lc", "rm -rf %s/processor*" % v],
                       check=False)
        print("%s: hazir" % ad, flush=True)
