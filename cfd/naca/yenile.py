# -*- coding: utf-8 -*-
"""Saklanmis vakalarin katsayilarini yeniden hesaplar.

Gerekcesi: A ve B aileleri, duvar gradyani ikinci mertebeye gecirilmeden
once kosuldu ve JSON'lari birinci mertebe degerleri tasiyor. Alan, model
ve kalinlik calismalari ise ikinci mertebe. Ayni tabloda iki farkli
yontemin durmasi kabul edilemez; bu betik hepsini ayni olcute getirir.

Cozum dosyalari duruyor, yeniden cozmeye gerek yok -- yalnizca kuvvet
integrali yeniden aliniyor. Iki mertebe de saklaniyor ki fark gorulebilsin.
"""
import json, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kuvvet import hesapla                             # noqa: E402

HEDEF = [("/tmp/tarama-A", "sonuc.json"), ("/tmp/tarama-B", "sonuc.json")]

if __name__ == "__main__":
    for kok, ad in HEDEF:
        yol = os.path.join(kok, ad)
        if not os.path.exists(yol):
            print("atlandi (yok):", yol)
            continue
        d = json.load(open(yol))
        for s in d:
            vaka = os.path.join(kok, s["ad"])
            for g in s["gecmis"]:
                r1 = hesapla(vaka, alfa=0.0, zaman=g["zaman"], mertebe=1)
                r2 = hesapla(vaka, alfa=0.0, zaman=g["zaman"], mertebe=2)
                g["CD_m1"] = r1["CD"]
                g.update(CD=r2["CD"], CL=r2["CL"], CD_b=r2["CD_basinc"],
                         CD_v=r2["CD_viskoz"], yp_ort=r2["yplus_ort"],
                         yp_max=r2["yplus_max"])
            g = s["gecmis"][-1]
            print("  %-3s  C_D(1)=%.6f  C_D(2)=%.6f  fark %+.2f%%"
                  % (s["ad"], g["CD_m1"], g["CD"],
                     (g["CD"] / g["CD_m1"] - 1) * 100), flush=True)
        json.dump(d, open(yol, "w"), indent=1)
        print("yazildi:", yol)
