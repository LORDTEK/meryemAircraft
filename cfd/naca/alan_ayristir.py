# -*- coding: utf-8 -*-
"""R=200 anomalisini AYRISTIRIR: alan boyutu mu, uzak alan cozunurlugu mu?

BULGU. Yerlesik alan taramasi (alan.py) n_normal'i her R icin YENIDEN
seciyordu; amac j yonundeki buyume oranini sabit tutup "yakin alan
degismesin, disariya yalnizca katman eklensin" demekti. Secilen degerler:

    R = 20 -> 96 katman,  R = 50 -> 103,  R = 100 -> 108,  R = 200 -> 113

Yani R = 100'den R = 200'e gecerken IKI SEY birden degisti: alan boyutu
ve katman sayisi. Tarama bunlari ayirmiyordu.

OLCUM. Uc vaka, hepsi SA, Re = 6e6, alfa = 0, ayni profil ve iz izgarasi:

    R = 100, n = 108   C_D = 0,008406     yerlesik taramanin R=100'u
    R = 100, n = 113   C_D = 0,008388     yalnizca katman eklendi
    R = 200, n = 113   C_D = 0,008432     yerlesik taramanin R=200'u

Buradan iki etki ayri ayri okunuyor:

    saf alan etkisi (n = 113 sabit, R 100 -> 200)   +%0,52
    uzak alan cozunurlugu (R = 100, n 108 -> 113)   -%0,21
    ------------------------------------------------------
    toplam                                          +%0,31

Taramanin R=100 -> R=200 icin olctugu deger de +%0,31'dir. Aritmetik
kapaniyor: gozlenen "anomali", zit isaretli iki etkinin toplamidir.

SONUC (yontem). Bu ag ailesinde alan boyutu ile uzak alan cozunurlugu
BAGIMSIZ degistirilemez. R'yi buyutup hem n_normal'i hem buyume oranini
sabit tutmak mumkun degildir; biri sabitlenirse oteki kayar. Dolayisiyla
"saf alan taramasi" diye bir sey yoktur ve alan.py'nin buyume oranini
sabitleme onlemi bir karistiriciyi digeriyle degistirmistir. Bu, sonucu
gecersiz kilmaz ama ne olculdugunu degistirir ve boyle raporlanmalidir.

Buyukluk baglami: olculen sicramanin tamami (%0,31) ve saf alan etkisi
(%0,52), ag belirsizligi olarak olculen GCI %1,29'un altindadir.

TEKRARLANABILIRLIK. Iki yerlesik deger sifirdan yeniden kurulup yeniden
cozuldu ve birebir cikti: R=200/n=113 -> 0,008432; R=100/n=108 ->
0,008406. Yani yukaridaki farklar kurulum gurultusu degildir.
"""
import json
import os
import subprocess
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kur import kur                                    # noqa: E402
from kuvvet import hesapla                             # noqa: E402
from kilit import Kilit                                # noqa: E402

KOK = "/tmp/alan_ayristir"
VAKA = [("r100-n108", 100.0, 108), ("r100-n113", 100.0, 113),
        ("r200-n113", 200.0, 113)]


if __name__ == "__main__":
    with Kilit(KOK):
        os.makedirs(KOK, exist_ok=True)
        yol = os.path.join(KOK, "sonuc.json")
        cikti = json.load(open(yol)) if os.path.exists(yol) else {}
        for ad, R, nn in VAKA:
            if ad in cikti:
                continue
            v = os.path.join(KOK, ad)
            if not os.path.isdir(os.path.join(v, "processor0")):
                kur(v, kod="0012", Re=6e6, alfa=0.0, yplus=1.0,
                    n_profil=256, n_normal=nn, n_iz=64, R=R, Xiz=R,
                    adim=3000, yaz_araligi=250, model="SpalartAllmaras")
                subprocess.run([os.path.join(BURA, "kos.sh"), v, "4"], check=True)
            else:
                subprocess.run([os.path.join(BURA, "devam.sh"), v, "3000", "4"],
                               check=True)
            r = hesapla(v, alfa=0.0, mertebe=2)
            cikti[ad] = dict(R=R, n_normal=nn, CD=r["CD"], CL=r["CL"])
            json.dump(cikti, open(yol, "w"), indent=1)
            print("  %s  C_D=%.6f" % (ad, r["CD"]), flush=True)

        a = cikti["r100-n108"]["CD"]
        b = cikti["r100-n113"]["CD"]
        c = cikti["r200-n113"]["CD"]
        print()
        print("  R=100 n=108   %.6f" % a)
        print("  R=100 n=113   %.6f" % b)
        print("  R=200 n=113   %.6f" % c)
        print()
        print("  saf alan etkisi (n=113 sabit)      %+.2f%%" % ((c / b - 1) * 100))
        print("  uzak alan cozunurlugu (R=100)      %+.2f%%" % ((b / a - 1) * 100))
        print("  toplam (taramanin olctugu)         %+.2f%%" % ((c / a - 1) * 100))
