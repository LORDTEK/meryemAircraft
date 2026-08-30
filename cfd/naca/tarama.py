# -*- coding: utf-8 -*-
"""Ag bagimsizligi taramasi: ayni akis, dort cozunurlukte.

Her seviyede alanlar araliklarla yazilir, katsayilar her yazilmis zamanda
yeniden hesaplanir. Boylece hem AG yakinsamasi hem de COZUM yakinsamasi
ayni kosudan okunur -- fonksiyon nesneleri calismadigi icin katsayi
gecmisini baska turlu almanin yolu yok.
"""
import os, sys, subprocess, json

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kur import kur                                    # noqa: E402
from kuvvet import hesapla                             # noqa: E402
from foamoku import Ag                                 # noqa: E402

SEVIYE = [("S1", 128, 48, 32), ("S2", 192, 72, 48),
          ("S3", 256, 96, 64), ("S4", 384, 144, 96)]
ADIM, YAZ = 3000, 500
KOK = "/tmp/tarama"


def zamanlar(vaka):
    z = []
    for a in os.listdir(vaka):
        try:
            v = float(a)
        except ValueError:
            continue
        if v > 0 and os.path.isdir(os.path.join(vaka, a)):
            z.append((v, a))
    return [a for _, a in sorted(z)]


if __name__ == "__main__":
    os.makedirs(KOK, exist_ok=True)
    cikti = []
    for ad, nf, nn, nw in SEVIYE:
        vaka = os.path.join(KOK, ad)
        bilgi = kur(vaka, kod="0012", Re=6e6, alfa=0.0,
                    n_profil=nf, n_normal=nn, n_iz=nw,
                    adim=ADIM, yaz_araligi=YAZ)
        print("[%s] %d hucre -- cozuluyor" % (ad, bilgi["hucre"]), flush=True)
        subprocess.run([os.path.join(BURA, "kos.sh"), vaka, "4"],
                       check=True, stdout=subprocess.DEVNULL)
        gecmis = []
        for z in zamanlar(vaka):
            r = hesapla(vaka, alfa=0.0, zaman=z)
            gecmis.append(dict(zaman=z, CD=r["CD"], CL=r["CL"],
                               CD_b=r["CD_basinc"], CD_v=r["CD_viskoz"],
                               yp_ort=r["yplus_ort"], yp_max=r["yplus_max"]))
            print("   t=%-6s CD=%.6f  CL=%+.2e  y+ %.2f/%.2f"
                  % (z, r["CD"], r["CL"], r["yplus_ort"], r["yplus_max"]),
                  flush=True)
        cikti.append(dict(ad=ad, hucre=bilgi["hucre"], NI=bilgi["NI"],
                          NJ=bilgi["NJ"], gecmis=gecmis))
        json.dump(cikti, open(os.path.join(KOK, "sonuc.json"), "w"), indent=1)
    print("bitti")
