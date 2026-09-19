# -*- coding: utf-8 -*-
"""AGIR TASARIMIN burun cifti, ayni iki nokta.

Hafif tasarimda makalenin FM'ini tutturan palet 0,80 yerine 0,63-0,68
veriyor. Agir tasarim yirmi kat kutlede, 5,40 m capla ve 40 m/s'de; ayni
sorunun orada da ayni cevabi verip vermedigi bir OLCEK sorusudur ve
makalenin 3.9'u tam olarak olcek uzerine kurulu. Varsaymak yerine kosuyoruz.
"""
import math
import os
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)

import nose_propeller as NP                                   # noqa: E402
from nose_propeller import Rotor, fm_makale_yontemi           # noqa: E402

# --- 3.8 agir referans tasarim ---------------------------------------
D_AGIR = 5.40
MTOW_AGIR = 1000.0
W_AGIR = MTOW_AGIR * 9.81
V_AGIR = 40.0
LD_AGIR = 13.6
T_SEYIR_AGIR = W_AGIR / LD_AGIR
P_HOVER_AGIR = 216.2e3
MENZIL_AGIR = 1814.0
ZINCIR_PERVANESIZ = 0.28 * 0.90 * 0.95 * 0.92


def iki_nokta_agir(rot, c, th):
    om_h = rot.devir_icin(1e-3, c, th, W_AGIR, alt=5.0, ust=400.0)
    T_h, Q_h, _ = rot.coz(1e-3, om_h, c, th)
    FM, _ = fm_makale_yontemi(T_h, Q_h * om_h, rot.A)
    om_c = rot.devir_icin(V_AGIR, c, th, T_SEYIR_AGIR, alt=2.0, ust=400.0)
    T_c, Q_c, _ = rot.coz(V_AGIR, om_c, c, th)
    P_c = Q_c * om_c
    eta = T_c * V_AGIR / P_c if P_c > 0 else float("nan")
    n_c = om_c / (2 * math.pi)
    return dict(om_h=om_h, P_h=Q_h * om_h, FM=FM, om_c=om_c, eta=eta,
                J=V_AGIR / (n_c * 2 * rot.R), M_h=om_h * rot.R / 340.3)


def aile_agir(rot, cl_h, dth):
    c, th = rot.tasarla(1e-3, 55.0, W_AGIR, cl_h)
    return c, th + dth * NP.D2R


def fm_icin_hatve(rot, cl_h, hedef, alt=0.0, ust=20.0, tur=7):
    for _ in range(tur):
        orta = 0.5 * (alt + ust)
        k = iki_nokta_agir(rot, *aile_agir(rot, cl_h, orta))
        if k["FM"] > hedef:
            alt = orta
        else:
            ust = orta
    orta = 0.5 * (alt + ust)
    return orta, iki_nokta_agir(rot, *aile_agir(rot, cl_h, orta))


if __name__ == "__main__":
    A = math.pi * (D_AGIR / 2) ** 2
    fm_k, P_ideal = fm_makale_yontemi(W_AGIR, P_HOVER_AGIR, A)
    print("AGIR TASARIM, BURUN CIFTI")
    print("D = %.2f m, W = %.0f N, V = %.0f m/s, T_seyir = %.0f N (L/D %.1f)"
          % (D_AGIR, W_AGIR, V_AGIR, T_SEYIR_AGIR, LD_AGIR))
    print("Makalenin kendi aritmetigi: ideal %.0f W / %.0f W = FM %.4f"
          % (P_ideal, P_HOVER_AGIR, fm_k))
    print("3.8 ayrica FM'in agir hatta 0,599'a ULASAMADIGINI soyluyor;")
    print("bu yuzden hedef, makalenin kendi agir FM'i: %.4f" % fm_k)
    print()
    print("%-6s %-7s %8s %8s %8s %8s %9s %9s"
          % ("pala", "c_l", "d_th", "FM", "eta", "J", "zincir", "menzil km"))
    print("-" * 74)
    etalar = []
    for B_PALA in (2, 3):
        rot = Rotor(D_AGIR, 2 * B_PALA)
        for cl_h in (0.55, 0.70):
            dth, k = fm_icin_hatve(rot, cl_h, fm_k)
            etalar.append(k["eta"])
            print("%-6d %-7.2f %8.1f %8.3f %8.3f %8.2f %9.4f %9.0f"
                  % (B_PALA, cl_h, dth, k["FM"], k["eta"], k["J"],
                     ZINCIR_PERVANESIZ * k["eta"],
                     MENZIL_AGIR * k["eta"] / 0.80))
    print("-" * 74)
    lo, hi = min(etalar), max(etalar)
    print("eta araligi     %.3f - %.3f   (makale: 0,80)" % (lo, hi))
    print("menzil araligi  %.0f - %.0f km  (makale: %.0f km)"
          % (MENZIL_AGIR * lo / 0.80, MENZIL_AGIR * hi / 0.80, MENZIL_AGIR))
    print("dusus           %.1f - %.1f %%"
          % (100 * (1 - hi / 0.80), 100 * (1 - lo / 0.80)))
