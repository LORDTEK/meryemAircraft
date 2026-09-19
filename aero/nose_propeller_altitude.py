# -*- coding: utf-8 -*-
"""IRTIFA cift gorev cezasini degistiriyor mu?

YAZARIN SORUSU. "Bu calismalari deniz seviyesinde mi yapiyoruz? Galiba
irtifa da bu hesaplari etkileyecek bir etmen."

MAKALE NE DIYOR. 2.12 deniz seviyesini acikca ilan ediyor ve savunuyor:
menzil R = f_yakit E* eta_zincir (L/D)/g formulunde YOGUNLUK YOK; sabit
C_L'de ince hava daha hizli ucularak ayni L/D veriliyor, menzil
degismiyor. Irtifa menzili ancak L/D'yi oynatarak etkiler.

AMA O PARAGRAF PERVANE ICIN YAZILMADI. eta_zincir'in icinde eta_p var ve
eta_p, askı ile seyir arasindaki ILERLEME ORANI ACIKLIGINA bagli:

    aski   J = 0            irtifadan BAGIMSIZ
    seyir  V ~ 1/sqrt(rho)  irtifayla BUYUR  ->  J buyur

Yani iki gorev arasindaki aciklik irtifayla ACILIYOR ve cift gorev
uzlasmasinin kotulesmesi BEKLENIR. Beklemek yetmez; olcuyoruz.

Ayni FM hedefi, ayni palet ailesi, uc yogunluk.
"""
import math
import os
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)

import numpy as np                                            # noqa: E402
import tip_propeller as TP                                    # noqa: E402
import nose_propeller as NP                                   # noqa: E402

# ISA
KATMANLAR = ((0.0, 1.2250), (1000.0, 1.1117), (2000.0, 1.0066), (3000.0, 0.9093))

W_N = NP.W_N
LD = NP.LD_SEYIR
T_SEYIR = NP.T_SEYIR          # agirlik/LD -- irtifadan bagimsiz
CL_SEYIR = W_N / (0.5 * 1.2250 * 30.0 ** 2 * 1.979)
FM_HEDEF = 0.599


def V_irtifa(rho):
    """Sabit C_L -> V = sqrt(2W/(rho S C_L)). 2.12'nin kendi argumani."""
    return math.sqrt(2 * W_N / (rho * 1.979 * CL_SEYIR))


def kos(rho, cl_h=0.70, B_PALA=2, tur=7):
    TP.RHO = rho
    NP.RHO = rho
    rot = NP.Rotor(NP.D_BURUN, 2 * B_PALA)
    V = V_irtifa(rho)

    def nokta(dth):
        c, th = rot.tasarla(1e-3, 250.0, W_N, cl_h)
        th = th + dth * NP.D2R
        om_h = rot.devir_icin(1e-3, c, th, W_N, alt=30.0, ust=2000.0)
        T_h, Q_h, _ = rot.coz(1e-3, om_h, c, th)
        P_i = T_h ** 1.5 / math.sqrt(2 * rho * rot.A)
        FM = P_i / (Q_h * om_h)
        om_c = rot.devir_icin(V, c, th, T_SEYIR, alt=10.0, ust=2000.0)
        T_c, Q_c, _ = rot.coz(V, om_c, c, th)
        P_c = Q_c * om_c
        eta = T_c * V / P_c if P_c > 0 else float("nan")
        n_c = om_c / (2 * math.pi)
        return FM, eta, V / (n_c * 2 * rot.R), Q_h * om_h

    alt, ust = 0.0, 20.0
    for _ in range(tur):
        orta = 0.5 * (alt + ust)
        if nokta(orta)[0] > FM_HEDEF:
            alt = orta
        else:
            ust = orta
    orta = 0.5 * (alt + ust)
    FM, eta, J, P_h = nokta(orta)
    return dict(dth=orta, FM=FM, eta=eta, J=J, V=V, P_h=P_h)


if __name__ == "__main__":
    print("IRTIFA VE CIFT GOREV CEZASI")
    print("Sabit C_L = %.3f; 2.12'nin kendi argumani: V = sqrt(2W/(rho S C_L))"
          % CL_SEYIR)
    print("Aski itkisi = agirlik (irtifadan bagimsiz); seyir itkisi = W/(L/D)")
    print("Palet ailesi ayni, FM hedefi ayni (%.3f). 2 pala, c_l 0,70." % FM_HEDEF)
    print()
    print("%-8s %8s %8s %8s %8s %8s %9s"
          % ("irtifa m", "rho", "V m/s", "FM", "eta", "J", "aski kW"))
    print("-" * 64)
    ilk = None
    for h, rho in KATMANLAR:
        r = kos(rho)
        if ilk is None:
            ilk = r
        print("%-8.0f %8.4f %8.1f %8.3f %8.3f %8.2f %9.2f"
              % (h, rho, r["V"], r["FM"], r["eta"], r["J"], r["P_h"] / 1000.0))
    print("-" * 64)
    print()
    print("OKUMA. eta deniz seviyesinden uzaklastikca DUSUYORSA, 2.12'nin")
    print("'irtifa menzili yalniz L/D uzerinden etkiler' cumlesi eksiktir:")
    print("eta_zincir'in icindeki eta_p ikinci bir kanaldir ve o paragraf")
    print("pervane hesabindan ONCE yazildi.")
