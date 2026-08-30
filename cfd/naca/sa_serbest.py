# -*- coding: utf-8 -*-
"""SA'nin serbest akis nuTilda degerine duyarliligi -- alan boyutuyla bagi.

DURUM. Alan taramasi SA ile kosuldugunda dizi TEKDUZE CIKMADI:

    R = 20c   C_D = 0,008416
    R = 50c         0,008407
    R = 100c        0,008406
    R = 200c        0,008432     <- yukseldi, R=100'e gore +%0,31

Yakinsama artigi DEGIL: dortunun de iki yazim arasindaki surukleniyi
ayni (+%0,14 / +%0,145 / +%0,140 / +%0,136), yani hepsi esdeger
yakinsama durumunda. Karsilastirma: SST ile dizi tekduzeydi
(0,007691 / 0,007685 / 0,007683 / 0,007680).

HIPOTEZ (once yaziliyor, sonra sinaniyor). SA'nin tasidigi nuTilda'nin
yok olma terimi ~ (nuTilda/d)^2 bicimindedir; d duvar uzakligidir.
Serbest akista uretim yoktur (Stilda ~ 0), yalnizca yok olma vardir.
Alan buyudukce d buyur, yok olma ZAYIFLAR, dolayisiyla giristen gelen
nuTilda daha az bozunarak sinir tabakasina ulasir -- ve daha buyuk bir
girdap viskozitesi daha yuksek surukleme demektir. Isaret uyuyor.

Bu, SST'de bulunan omega bozunma sorununun SA'daki karsiligidir; orada
serbest akis degerinin degil ALAN BOYUTUNUN belirleyici oldugu
olculmustu (omega(x) = omega0/(1+beta omega0 x) doyuma gidiyordu).

BEKLENTI ONCEDEN:
  (a) Serbest akis nuTilda'si kucultuldugunde R=200'un C_D'si R=100'e
      DOGRU inerse hipotez dogrulanir; o zaman alan boyutu etkisi diye
      olculen sey aslinda serbest akis tasinimi etkisidir ve ikisi
      ayrilmalidir.
  (b) Degismezse hipotez YANLISTIR ve yukselisin nedeni baska yerdedir
      (uzak alan cozunurlugu, dis sinir kosulu, ...). O zaman oyle
      yazilir.

Kosulan: R = 200c, uc serbest akis degeri. Yerlesik secim 3*nu'dur.
"""
import json, os, subprocess, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kur import kur                                    # noqa: E402
from kuvvet import hesapla                             # noqa: E402
from kilit import Kilit                                # noqa: E402

KOK = "/tmp/sa_serbest"
NU = 1.0 / 6e6
CARPAN = [3.0, 0.3, 0.03]        # nuTilda_inf = carpan * nu
# Olculen degerler (SA, ayni ag ailesi, yerlesik 3*nu ile)
REF = {20: 0.008416, 100: 0.008406, 200: 0.008432}

if __name__ == "__main__":
    with Kilit(KOK):
        os.makedirs(KOK, exist_ok=True)
        yol = os.path.join(KOK, "sonuc.json")
        cikti = json.load(open(yol)) if os.path.exists(yol) else []
        yapilan = {d["carpan"] for d in cikti}
        for c in CARPAN:
            if c in yapilan:
                continue
            vaka = os.path.join(KOK, "c%g" % c)
            kur(vaka, kod="0012", Re=6e6, alfa=0.0, yplus=1.0,
                n_profil=256, n_normal=113, n_iz=64, R=200.0, Xiz=200.0,
                adim=3000, yaz_araligi=1500, model="SpalartAllmaras")
            # nuTilda serbest akis degerini degistir.
            #
            # Metin degistirme kirilgandir: aranan dizge ("5e-07") cok
            # genel ve dosya bicimi degisirse sessizce yanlis yere ya da
            # hic yazmayabilir. Bu yuzden ADET DOGRULANIYOR: dosyada tam
            # iki yerde gecmeli (internalField ve freestreamValue; duvar
            # degeri 0, boyutlar ayri). Iki degilse durulur.
            p = os.path.join(vaka, "0", "nuTilda")
            metin = open(p).read()
            hedef = "%.10g" % (3 * NU)
            adet = metin.count(hedef)
            if adet != 2:
                raise RuntimeError(
                    "0/nuTilda icinde %r %d kez gecti, 2 bekleniyordu -- "
                    "dosya bicimi degismis olabilir, degistirme guvenli "
                    "degil" % (hedef, adet))
            open(p, "w").write(metin.replace(hedef, "%.10g" % (c * NU)))
            print("[nuTilda_inf = %g nu] cozuluyor" % c, flush=True)
            subprocess.run([os.path.join(BURA, "kos.sh"), vaka, "4"],
                           check=True, stdout=subprocess.DEVNULL)
            r = hesapla(vaka, alfa=0.0, mertebe=2)
            print("   C_D=%.6f  (R=200'un yerlesik degeri %.6f, R=100 %.6f)"
                  % (r["CD"], REF[200], REF[100]), flush=True)
            cikti.append(dict(carpan=c, CD=r["CD"], CD_v=r["CD_viskoz"],
                              CD_b=r["CD_basinc"], CL=r["CL"]))
            json.dump(cikti, open(yol, "w"), indent=1)
        print()
        print("  nuTilda_inf     C_D        R=200 yerlesike gore")
        for d in sorted(cikti, key=lambda x: -x["carpan"]):
            print("  %5g nu     %.6f     %+.2f%%"
                  % (d["carpan"], d["CD"], (d["CD"] / REF[200] - 1) * 100))
        print("  Karsilastirma: R=100 (yerlesik) %.6f" % REF[100])
