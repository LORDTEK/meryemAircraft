# -*- coding: utf-8 -*-
"""MEKANIZMA SINAMASI: alan etkisi, profile ULASAN nuTilda'dan mi geliyor?

sa_serbest.py serbest akis nuTilda'sinin C_D'yi etkiledigini ve yonun
hipotezle uyustugunu olctu. Ama bu, R=100 ile R=200 arasindaki %0,31'lik
farkin SEBEBINI kurmuyor -- yalnizca boyle bir sebebin mumkun oldugunu
gosteriyor. Aradaki fark onemlidir: duyarlilik varligi, o duyarliligin
gozlenen farki URETTIGI anlamina gelmez.

Dogrudan sinama sudur. Hipotez, alan buyudukce girişten gelen nuTilda'nin
daha az bozunarak profile ulastigini soyler. Oyleyse profilin HEMEN
ONUNDEKI nuTilda, R=200'de R=100'dekinden BUYUK olmalidir -- ve fark,
sa_serbest'te olculen duyarlilikla birlikte %0,31'i aciklayacak buyuklukte
olmalidir.

BEKLENTI (kosmadan once yaziliyor):

  (a) nuTilda(profil onu, R=200) > nuTilda(profil onu, R=100) ise hipotez
      DOGRUDAN desteklenir.

  (b) Ikisi esitse hipotez YANLISTIR: C_D farki serbest akis tasinimindan
      degil, baska bir seyden (uzak alan cozunurlugu, dis sinir kosulunun
      kendisi) geliyordur. O zaman oyle yazilir.

  (c) Nicel denetim: sa_serbest'te bir onluk nuTilda degisimi C_D'yi
      %0,43 oynatti. Gozlenen %0,31 icin gereken nuTilda orani yaklasik
      10^(0,31/0,43) ~ 5'tir. Olculen oran bundan cok farkliysa (diyelim
      1,1 ya da 100), mekanizma tek basina yeterli DEGILDIR ve oyle yazilir.

Olcum noktalari: profilin onunde, durma cizgisi uzerinde (y=0), hucum
kenarindan geriye dogru birkac uzaklikta. Sinir tabakasi disinda kalmalari
icin yeterince uzak, uzak alandan etkilenmemeleri icin yeterince yakin.
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
from foamoku import Ag, Alan, son_zaman                # noqa: E402
from kilit import Kilit                                # noqa: E402

KOK = "/tmp/nutilda_ulasan"
# R=200 vakasi sa_serbest'ten hazir: /tmp/sa_serbest/c3 (3nu, R=200)
HAZIR_200 = "/tmp/sa_serbest/c3"
X = [-0.5, -0.2, -0.1, -0.05, -0.02]      # hucum kenari x=0'da


def ornekle(vaka, xler, y=0.0):
    """Verilen (x, y) noktalarina en yakin hucre merkezlerindeki nuTilda."""
    z = son_zaman(vaka)
    ag = Ag(vaka)
    M = ag.hucre_merkez()
    nt = Alan(vaka, z, "nuTilda").ic
    cikti = []
    for x in xler:
        en, ei = None, None
        for i, c in enumerate(M):
            d = (c[0] - x) ** 2 + (c[1] - y) ** 2
            if en is None or d < en:
                en, ei = d, i
        cikti.append(dict(x=x, x_ger=M[ei][0], y_ger=M[ei][1],
                          nuTilda=nt[ei] if isinstance(nt, list) else nt))
    return cikti


if __name__ == "__main__":
    with Kilit(KOK):
        os.makedirs(KOK, exist_ok=True)
        yol = os.path.join(KOK, "sonuc.json")
        cikti = json.load(open(yol)) if os.path.exists(yol) else {}

        # R=100, digerlerinin tipatip aynisi
        if "r100" not in cikti:
            v = os.path.join(KOK, "r100")
            if not os.path.isdir(os.path.join(v, "processor0")):
                kur(v, kod="0012", Re=6e6, alfa=0.0, yplus=1.0,
                    n_profil=256, n_normal=113, n_iz=64, R=100.0, Xiz=100.0,
                    adim=3000, yaz_araligi=250, model="SpalartAllmaras")
                subprocess.run([os.path.join(BURA, "kos.sh"), v, "4"],
                               check=True)
            else:
                subprocess.run([os.path.join(BURA, "devam.sh"), v, "3000", "4"],
                               check=True)
            r = hesapla(v, alfa=0.0, mertebe=2)
            cikti["r100"] = dict(CD=r["CD"], nokta=ornekle(v, X))
            json.dump(cikti, open(yol, "w"), indent=1)
            print("  R=100  C_D=%.6f" % r["CD"], flush=True)

        if "r200" not in cikti:
            r = hesapla(HAZIR_200, alfa=0.0, mertebe=2)
            cikti["r200"] = dict(CD=r["CD"], nokta=ornekle(HAZIR_200, X))
            json.dump(cikti, open(yol, "w"), indent=1)
            print("  R=200  C_D=%.6f" % r["CD"], flush=True)

        print()
        print("      x       nuTilda(R=100)   nuTilda(R=200)    oran")
        for a, b in zip(cikti["r100"]["nokta"], cikti["r200"]["nokta"]):
            print("  %6.2f     %.6e     %.6e     %.4f"
                  % (a["x"], a["nuTilda"], b["nuTilda"],
                     b["nuTilda"] / a["nuTilda"]))
        print()
        print("  C_D: R=100 %.6f, R=200 %.6f  (%+.2f%%)"
              % (cikti["r100"]["CD"], cikti["r200"]["CD"],
                 (cikti["r200"]["CD"] / cikti["r100"]["CD"] - 1) * 100))
