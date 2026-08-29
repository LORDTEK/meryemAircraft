# -*- coding: utf-8 -*-
"""C_D0 kurulumunun sonuclarini iki referans tasarim icin toplar.

cd0.py bilesenleri verir; burasi onlari L/D ve menzile cevirip makalenin
varsaydigi degerlerle karsilastirir.
"""
import sys, os, math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cd0 as C
from planform import olcuier

G, RHO, E_OSWALD = 9.81, 1.225, 0.85
ESTAR, ETA, YAKIT_PAY = 12.9 * 3.6e6, 0.176, 0.16   # 6.1'deki zincir


def menzil(LD):
    return YAKIT_PAY * ESTAR * ETA * LD / G / 1000.0   # km


def hat(ad, olcek, hiz, kutle, LD_makale, menzil_makale):
    ks, _, o = C.kanat_cd0(False, olcek=olcek, hiz=hiz)
    kt, _, _ = C.kanat_cd0(True, olcek=olcek, hiz=hiz)
    S = o["alan"] * olcek ** 2
    cer = C.CERCEVE_CD * (C.CERCEVE_UZUNLUK * olcek) * (C.CERCEVE_KALINLIK * olcek) / S
    gobek = [C.UC_GOBEK_CD * C.UC_GOBEK_SAYISI * math.pi * ((d * olcek) / 2) ** 2 / S
             for d in C.UC_GOBEK_CAP]

    hal = [("iyimser  (temiz yuzey, 28 mm gobek)", ks + cer + gobek[0]),
           ("orta     (tetikli, 28 mm gobek)",     kt + cer + gobek[0]),
           ("kotumser (tetikli, 32 mm gobek, +%10)", (kt + cer + gobek[1]) * 1.10)]

    W = kutle * G
    q = 0.5 * RHO * hiz ** 2
    CL = W / (q * S)
    AR = o["AR"]

    print(f"\n{'='*66}\n{ad} — {kutle:.0f} kg, {hiz:.0f} m/s, S = {S:.3f} m2, C_L = {CL:.3f}")
    print(f"{'-'*66}")
    print(f"  kanat/govde   serbest gecis {ks:.5f}   tetikli gecis {kt:.5f}")
    print(f"  uc iskeleti   {cer:.5f}        gobekler {gobek[0]:.5f}–{gobek[1]:.5f}")
    print(f"{'-'*66}")
    print(f"{'hal':<38}{'C_D0':>8}{'L/D':>7}{'menzil':>10}")
    for etiket, cdv in hal:
        LD = CL / (cdv + CL ** 2 / (math.pi * AR * E_OSWALD))
        print(f"{etiket:<38}{cdv:8.4f}{LD:7.2f}{menzil(LD):9.0f} km")
    cd_makale = f"{0.0248:8.4f}" if olcek == 1 else f"{'—':>8}"   # 6.1 yalniz hafif hat icin veriyor
    print(f"{'MAKALE (varsayim)':<38}{cd_makale}{LD_makale:7.2f}{menzil_makale:9.0f} km")


if __name__ == "__main__":
    hat("HAFIF HAT", 1.0, 30.0, 50, 12.0, 1598)
    hat("AGIR HAT", C.AGIR_OLCEK, C.AGIR_V, 1000, 13.6, 1814)
    print(f"\n{'='*66}")
    print("MAKALE satiri, duzeltilmis yontemle (seyir noktasi polari) hesaplanmis")
    print("degerleri gosterir. Varsayilan C_D0 = 0.0248, hesaplanan araligin")
    print("TAMAMININ ustunde; yani varsayim her senaryoda kotumser.")
