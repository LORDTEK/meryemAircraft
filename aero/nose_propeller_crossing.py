# -*- coding: utf-8 -*-
"""Makalenin FM'ini TUTTURAN palet, seyirde ne veriyor?

Supurme takasi gosterdi: hatve artinca eta yukseliyor, FM dusuyor. Soru
artik "hangi palet" degil: MAKALENIN KENDI FM'i olan 0,599'u veren palet
hangi eta'yi veriyor? Makale 0,80 diyor. Bu betik o tek sayiyi ariyor.

Hatve kaymasi uzerinde ikiye bolme: FM(d_theta) = 0,599. O noktada eta
okunur. Dort palet ailesinde tekrarlanir, cunku pala sayisi ve kesit c_l
secildi, olculmedi -- sonuc tek sayi degil, aralik.
"""
import math
import os
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)

from nose_propeller import (Rotor, aile, iki_nokta, D_BURUN, FM_MAKALE,   # noqa
                            ETA_MAKALE, V_SEYIR, T_SEYIR, W_N)

# 2.12 zinciri, pervane haric
ZINCIR_PERVANESIZ = 0.28 * 0.90 * 0.95 * 0.92
MENZIL_MAKALE = 1598.0            # km, 3.7 hafif tasarim


def fm_icin_hatve(rot, cl_h, hedef=FM_MAKALE, alt=0.0, ust=20.0, tur=7):
    """FM = hedef veren hatve kaymasi. FM hatveyle AZALIYOR."""
    for _ in range(tur):
        orta = 0.5 * (alt + ust)
        c, th = aile(rot, cl_h, 250.0, orta)
        k = iki_nokta(rot, c, th)
        if k["FM"] > hedef:
            alt = orta
        else:
            ust = orta
    orta = 0.5 * (alt + ust)
    c, th = aile(rot, cl_h, 250.0, orta)
    return orta, iki_nokta(rot, c, th)


if __name__ == "__main__":
    print("MAKALENIN FM'INI TUTTURAN PALET, SEYIRDE NE VERIYOR?")
    print("Aranan: FM = %.3f. Makalenin ayni palet icin iddiasi: eta = %.2f"
          % (FM_MAKALE, ETA_MAKALE))
    print("Zincir, pervane haric: %.4f. Makalenin toplami: %.4f"
          % (ZINCIR_PERVANESIZ, ZINCIR_PERVANESIZ * ETA_MAKALE))
    print()
    print("%-6s %-7s %8s %8s %8s %8s %9s %9s"
          % ("pala", "c_l", "d_th", "FM", "eta", "J", "zincir", "menzil km"))
    print("-" * 74)
    etalar = []
    for B_PALA in (2, 3):
        rot = Rotor(D_BURUN, 2 * B_PALA)
        for cl_h in (0.55, 0.70):
            dth, k = fm_icin_hatve(rot, cl_h)
            zincir = ZINCIR_PERVANESIZ * k["eta"]
            menzil = MENZIL_MAKALE * k["eta"] / ETA_MAKALE
            etalar.append(k["eta"])
            print("%-6d %-7.2f %8.1f %8.3f %8.3f %8.2f %9.4f %9.0f"
                  % (B_PALA, cl_h, dth, k["FM"], k["eta"], k["J"],
                     zincir, menzil))
    print("-" * 74)
    lo, hi = min(etalar), max(etalar)
    print("eta araligi          %.3f - %.3f   (makale: %.2f)" % (lo, hi, ETA_MAKALE))
    print("zincir araligi       %.4f - %.4f  (makale: %.4f)"
          % (ZINCIR_PERVANESIZ * lo, ZINCIR_PERVANESIZ * hi,
             ZINCIR_PERVANESIZ * ETA_MAKALE))
    print("menzil araligi       %.0f - %.0f km  (makale: %.0f km)"
          % (MENZIL_MAKALE * lo / ETA_MAKALE, MENZIL_MAKALE * hi / ETA_MAKALE,
             MENZIL_MAKALE))
    print("dusus                %.1f - %.1f %%"
          % (100 * (1 - hi / ETA_MAKALE), 100 * (1 - lo / ETA_MAKALE)))
    print()
    print("KARSILASTIRMA OLCEGI: cok rotorlu bir ucak icin menzil 10-100 km")
    print("mertebesindedir. Bu aralik iddiayi degistirmiyor; degistirdigi sey")
    print("makalenin 0,80'i hak edip etmedigidir.")
