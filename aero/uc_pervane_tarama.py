# -*- coding: utf-8 -*-
"""FM gercekten ucurumdan mi atliyor, yoksa cozucu mu kararsiz?

Her tasarim IKI KEZ kuruluyor. Ayni girdi iki farkli FM veriyorsa sorun
fizikte degil cozucudedir ve o tasarimdan sayi ALINMAZ.
"""
import math, sys
sys.path.insert(0, "/home/user/meryemAircraft/aero")
import uc_pervane as U

A = math.pi * U.R ** 2


def bir(cl_h):
    c, th = U.hover_tasarla(cl_hedef=cl_h)
    om = U.devir_itki_icin(c, th)
    T, Q, _ = U.bemt_sabit(1e-3, om, c, th)
    P = 2 * Q * om
    FM = 2 * (T ** 1.5 / math.sqrt(2 * U.RHO * A)) / P if P > 0 else 0.0
    om2, T2 = U.sifir_tork(c, th)
    return FM, (U.dcd0(T2) if om2 else float("nan")), T

print("%-8s %8s %8s %7s %10s %10s" % ("c_l", "FM (1)", "FM (2)", "ayni?",
                                      "dC_D0", "hover T N"))
for cl_h in (0.55, 0.60, 0.64, 0.68, 0.70, 0.85):
    f1, d1, T1 = bir(cl_h)
    f2, d2, T2 = bir(cl_h)
    ayni = "EVET" if abs(f1 - f2) < 1e-6 else "HAYIR"
    print("%-8.2f %8.3f %8.3f %7s %10.5f %10.2f" % (cl_h, f1, f2, ayni, d1, T1))
