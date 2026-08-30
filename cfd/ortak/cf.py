# -*- coding: utf-8 -*-
"""Yuzey surtunme katsayisi dagilimi, C_f(x/c).

Toplam C_D tek bir sayidir ve iki cozum arasindaki farkin NEREDE
oldugunu soylemez. C_f dagilimi soyler: fark veterin her yerine yayilmis
mi, yoksa belli bir bolgede mi?

Ilk kullanimi: SA ile SST kurulumlarimiz arasindaki %9,5'lik farkin yeri.
Olculdu -- oran (SST/SA) x = 0,02'de 0,963, x = 0,10'da 0,890 (en dusuk),
x = 0,98'de 0,957. Yani acik on bolgede yogunlasiyor ama LAMINER bir bolge
degil: laminer olsaydi C_f bes kat dusukolurdu, burada en fazla %11.

    tau_w = (nu + nu_t,duvar) * |U_t| / d        (ikinci mertebe secenegi
    C_f   = tau_w / (0.5 U_inf^2)                 kuvvet.py'de)
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from foamoku import Ag, Alan, son_zaman        # noqa: E402
from kuvvet import nu_oku                      # noqa: E402


def dagilim(vaka, yama="duvar", Uinf=1.0, zaman=None):
    """[(x, y, C_f)] -- duvar yuzlerinin her biri icin."""
    ag = Ag(vaka)
    z = zaman or son_zaman(vaka)
    nu = nu_oku(vaka)
    U = Alan(vaka, z, "U", vektor=True)
    nut = Alan(vaka, z, "nut") if os.path.exists(
        os.path.join(vaka, z, "nut")) else None
    merkez = ag.hucre_merkez()
    y = ag.yama[yama]
    out = []
    for k in range(y["n"]):
        fi = y["bas"] + k
        S, C = ag.yuz_alan(fi)
        A = math.sqrt(sum(v * v for v in S))
        if A <= 0:
            continue
        n = [S[a] / A for a in range(3)]
        h = ag.sahip[fi]
        cm = merkez[h]
        d = abs(sum((cm[a] - C[a]) * n[a] for a in range(3)))
        if d <= 0:
            continue
        u = U.ic[h]
        un = sum(u[a] * n[a] for a in range(3))
        t = [u[a] - un * n[a] for a in range(3)]
        ut = math.sqrt(sum(v * v for v in t))
        nw = 0.0
        if nut is not None:
            v = nut.yama_degeri(yama, k)
            nw = v if v is not None else 0.0
        out.append((C[0], C[1], (nu + nw) * ut / d / (0.5 * Uinf ** 2)))
    return out


def ust_yuzey(d):
    return sorted([v for v in d if v[1] > 0], key=lambda v: v[0])


def karsilastir(vaka_a, vaka_b, ad_a="A", ad_b="B",
                noktalar=(0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 0.98)):
    a, b = ust_yuzey(dagilim(vaka_a)), ust_yuzey(dagilim(vaka_b))
    print("   x/c    C_f(%s)   C_f(%s)   %s/%s" % (ad_a, ad_b, ad_b, ad_a))
    for h in noktalar:
        va = min(a, key=lambda v: abs(v[0] - h))
        vb = min(b, key=lambda v: abs(v[0] - h))
        print("  %.3f  %.6f  %.6f    %.3f"
              % (va[0], va[2], vb[2], vb[2] / va[2] if va[2] else float("nan")))
    ta = sum(v[2] for v in a) / len(a)
    tb = sum(v[2] for v in b) / len(b)
    print("\n  ortalama: %s %.6f   %s %.6f   oran %.3f"
          % (ad_a, ta, ad_b, tb, tb / ta))


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        karsilastir(sys.argv[1], sys.argv[2],
                    os.path.basename(sys.argv[1]), os.path.basename(sys.argv[2]))
    else:
        for v in ust_yuzey(dagilim(sys.argv[1])):
            print("%.6f %.8f" % (v[0], v[2]))
