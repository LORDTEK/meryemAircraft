# -*- coding: utf-8 -*-
"""Turbulans modeli duyarliligi.

Ayni ag, ayni akis, ayni semalar; yalnizca model degisir. Sorusu: sonucun
ne kadari fizikten, ne kadari model seciminden geliyor?

Iki model, NASA turbulans modelleme kaynagi da bu ikisini karsilastirdigi
icin secildi:
  kOmegaSST         menter'in iki denklemli modeli
  SpalartAllmaras   tek denklemli, havacilikta yerlesik

Bu, ikinci makale icin belirleyici bir sayidir: merkez govde %25
kalinliginda ve orada ters basinc gradyani daha siddetli olacak, yani
model duyarliligi burada gorunenden BUYUK olmasi beklenir. Buradaki deger
bir alt sinirdir.
"""
import os, sys, subprocess, json

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kur import kur                                    # noqa: E402
from kuvvet import hesapla                             # noqa: E402

MODEL = ["kOmegaSST", "SpalartAllmaras"]
KOK = "/tmp/model"

if __name__ == "__main__":
    os.makedirs(KOK, exist_ok=True)
    yol = os.path.join(KOK, "sonuc.json")
    cikti = json.load(open(yol)) if os.path.exists(yol) else []
    yapilan = {d["model"] for d in cikti}
    for m in MODEL:
        if m in yapilan:
            continue
        vaka = os.path.join(KOK, m)
        bilgi = kur(vaka, kod="0012", Re=6e6, alfa=0.0, yplus=1.0,
                    n_profil=256, n_normal=96, n_iz=64, R=20.0, Xiz=20.0,
                    adim=3000, yaz_araligi=1500, model=m)
        print("[%s] %d hucre -- cozuluyor" % (m, bilgi["hucre"]), flush=True)
        subprocess.run([os.path.join(BURA, "kos.sh"), vaka, "4"],
                       check=True, stdout=subprocess.DEVNULL)
        r = hesapla(vaka, alfa=0.0, mertebe=2)
        print("   C_D=%.6f  basinc=%.6f  viskoz=%.6f  C_L=%+.2e  y+ %.2f"
              % (r["CD"], r["CD_basinc"], r["CD_viskoz"], r["CL"],
                 r["yplus_ort"]), flush=True)
        cikti.append(dict(model=m, CD=r["CD"], CD_b=r["CD_basinc"],
                          CD_v=r["CD_viskoz"], CL=r["CL"], yp=r["yplus_ort"]))
        json.dump(cikti, open(yol, "w"), indent=1)
    if len(cikti) == 2:
        a, b = cikti
        print("\nfark: C_D %+.2f %%  (basinc %+.2f %%, viskoz %+.2f %%)"
              % ((b["CD"] / a["CD"] - 1) * 100,
                 (b["CD_b"] / a["CD_b"] - 1) * 100,
                 (b["CD_v"] / a["CD_v"] - 1) * 100))
    print("bitti")
