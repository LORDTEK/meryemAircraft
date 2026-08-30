# -*- coding: utf-8 -*-
"""B3 ve B4'u tam yakinsamaya kadar kos.

Iki ayri soruyu birlikte kapatir:

1. Momentum dengesindeki fark, cozum yakinsamasinin bir olcusu cikti
   (kuvvet_sina.py). 3000 yinelemede B3 icin %2,2, B4 icin %6,5 ve ikisi
   de hala dusuyordu. Tam yakinsamada sifira gitmeli. Gitmezse geriye
   gercek bir yontem hatasi kalir.

2. B ailesindeki salinim (B3 -> B4 arasi +%0,8) gercek mi, yoksa B4'un
   daha az yakinsamis olmasindan mi? B4 daha cok hucreli oldugu icin ayni
   yineleme sayisinda daha geride kaliyor; salinim bundan geliyor olabilir.

Iki soru da yalnizca DAHA COK YINELEME ile ayrilabilir.
"""
import os, sys, subprocess, json

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kur import kur                                    # noqa: E402
from kuvvet import hesapla                             # noqa: E402
from kilit import Kilit                                # noqa: E402

SEVIYE = [("B3u", 256, 96, 64, 1.000), ("B4u", 384, 144, 96, 0.667)]
ADIM, YAZ = 20000, 2500
KOK = "/tmp/uzun"

if __name__ == "__main__":
    with Kilit(KOK):
        os.makedirs(KOK, exist_ok=True)
        yol = os.path.join(KOK, "sonuc.json")
        cikti = json.load(open(yol)) if os.path.exists(yol) else []
        yapilan = {d["ad"] for d in cikti}
        for ad, nf, nn, nw, yp in SEVIYE:
            if ad in yapilan:
                continue
            vaka = os.path.join(KOK, ad)
            bilgi = kur(vaka, kod="0012", Re=6e6, alfa=0.0, yplus=yp,
                        n_profil=nf, n_normal=nn, n_iz=nw,
                        adim=ADIM, yaz_araligi=YAZ)
            print("[%s] %d hucre -- %d yinelemeye kadar" % (ad, bilgi["hucre"], ADIM),
                  flush=True)
            subprocess.run([os.path.join(BURA, "kos.sh"), vaka, "4"],
                           check=True, stdout=subprocess.DEVNULL)
            z = sorted((float(a), a) for a in os.listdir(vaka)
                       if a.replace(".", "").isdigit() and float(a) > 0
                       and os.path.isdir(os.path.join(vaka, a)))
            g = []
            for _, t in z:
                r = hesapla(vaka, alfa=0.0, zaman=t, mertebe=2)
                g.append(dict(zaman=t, CD=r["CD"], CL=r["CL"],
                              CD_b=r["CD_basinc"], CD_v=r["CD_viskoz"],
                              yp_ort=r["yplus_ort"]))
                print("   t=%-6s C_D=%.6f" % (t, r["CD"]), flush=True)
            cikti.append(dict(ad=ad, hucre=bilgi["hucre"], yplus_hedef=yp,
                              gecmis=g))
            json.dump(cikti, open(yol, "w"), indent=1)
        print("bitti")
