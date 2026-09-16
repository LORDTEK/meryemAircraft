# -*- coding: utf-8 -*-
"""Ucagin KENDI hover verim sayisinda (FM = 0,599) serbest donme direnci.

NEDEN. tip_propeller.py dort tasarim tarayip mansete EN IYISINI koydu:
dC_D0 = 0.0085. Ama o tasarimin hover verim sayisi 0,27 ve makale hover
gucunu her yerde FM = 0,599 uzerinden kuruyor. Yani manset, ucagin
kullanamayacagini kendi soyledigi pervaneden aliniyor. Bu betik FM'yi
0,599'a KILITLEYIP karsilik gelen serbest donme direncini hesaplar.

FM tasarim c_l'sinde tek yonlu DEGIL: 0,40'ta 0,617, 0,55'te 0,646,
sonra dusuyor. 0,599'un iki koku var; ilgili olan INEN dal, cunku
yuksek tasarim c_l'si daha dusuk serbest donme direnci verir ve
makalenin lehine olan kok odur. Inen dalda ikiye bolunuyor.
"""
import math, sys
sys.path.insert(0, "/home/user/meryemAircraft/aero")
import tip_propeller as U

A = math.pi * U.R ** 2
HEDEF_FM = 0.599


def fm(cl_h):
    c, th = U.hover_tasarla(cl_hedef=cl_h)
    om = U.devir_itki_icin(c, th)
    T, Q, _ = U.bemt_sabit(1e-3, om, c, th)
    P = 2 * Q * om
    return (2 * (T ** 1.5 / math.sqrt(2 * U.RHO * A)) / P if P > 0 else 0.0,
            c, th, P)


print("FM = %.3f'e KILITLI tasarim -- inen dalda ikiye bolme" % HEDEF_FM)
print("%-10s %8s" % ("tasarim c_l", "FM"))
alt, ust = 0.55, 0.70                      # 0.646 -> 0.350, hedefi kapsiyor
for _ in range(12):
    orta = 0.5 * (alt + ust)
    f = fm(orta)[0]
    print("%-10.4f %8.3f" % (orta, f))
    if f > HEDEF_FM:
        alt = orta
    else:
        ust = orta
cl_son = 0.5 * (alt + ust)
f, c, th, P = fm(cl_son)
print("\nSecilen tasarim c_l = %.4f, FM = %.3f, cift gucu %.0f W" % (cl_son, f, P))

om, T = U.sifir_tork(c, th)
d = U.dcd0(T)
print("\nSEYIR, NET SAFT TORKU SIFIR")
print("  devir        %.0f rpm" % (om * 60 / 2 / math.pi))
print("  uc Mach      %.2f" % (om * U.R / 340.0))
print("  eksenel      %.3f N / rotor" % T)
print("  dC_D0 (8)    %.5f" % d)
print("\nKARSILASTIRMA")
print("  manset (FM 0,27)        0.00850")
print("  UCAGIN FM'si (0,599)    %.5f   -> %.1f kat" % (d, d / 0.0085))
print("  uc cerceveleri          0.00430")
print("  varsayilan C_D0         0.02480")
