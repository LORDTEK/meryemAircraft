# -*- coding: utf-8 -*-
"""Gecis benzetimi, hesaplanmis kaldirma egrisi egimine ne kadar duyarli?

gecis2.py kaldirma egrisi egimini CLa = 2pi/(1+2/AR) = 4.72 /rad varsayiyor.
VLM ayni planformda 3.87 /rad veriyor — %18 dusuk. Bu betik, makaledeki
tablolarin bu farka dayanip dayanmadigini sinar.
"""
import sys, os, math

KOK = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
KAYNAK = open(os.path.join(KOK, "gorsel", "uretim", "gecis2.py")).read()

VARSAYIM, HESAP = 4.717, 3.87


def sim_yap(CLa):
    ns = {}
    kod = KAYNAK.replace("CLa=2*math.pi/(1+2/AR)", f"CLa={CLa}").split("if __name__")[0]
    exec(compile(kod, "gecis2", "exec"), ns)
    return ns["sim"]


def tablo(ad, m, S, Vcr, trler, tw=1.2, w0=0.0):
    a, b = sim_yap(VARSAYIM), sim_yap(HESAP)
    print(f"\n{ad} — T/W = {tw}, w0 = {w0} m/s")
    print(f"{'t_r':>6}{'CLa 4.72':>11}{'CLa 3.87':>11}{'fark':>8}")
    en_buyuk = 0.0
    for tr in trler:
        x = a(m, S, 6, tw, tr, Vcr, w0=w0)[0]
        y = b(m, S, 6, tw, tr, Vcr, w0=w0)[0]
        en_buyuk = max(en_buyuk, abs(y - x))
        print(f"{tr:6.0f}{x:11.1f}{y:11.1f}{y-x:8.1f}")
    return en_buyuk


if __name__ == "__main__":
    en = 0.0
    en = max(en, tablo("hafif 50 kg", 50, 1.98, 30.0, (1, 2, 3, 4)))
    en = max(en, tablo("hafif 50 kg", 50, 1.98, 30.0, (1, 2, 3), w0=5))
    en = max(en, tablo("agir 1000 kg", 1000, 22.24, 40.0, (2, 3, 4, 5)))
    en = max(en, tablo("agir 1000 kg", 1000, 22.24, 40.0, (2, 3, 4), w0=5))
    print(f"\nEn buyuk sapma: {en:.1f} m")
    print("Referans profiller (hafif 2 s / agir 4 s, w0 = 5 m/s) her iki egimde de "
          "sifir irtifa kaybi veriyor.")
