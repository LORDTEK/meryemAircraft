# -*- coding: utf-8 -*-
"""Duz levha cozumumuzu NAS-2016-01 Bolum 4 ile karsilastirir.

Bu, calismadaki EN GUCLU dogrulama adimi, cunku ayni vakada iki bagimsiz
referans kod (Overflow ve Cfl3d) ve bir kuram egrisi var, ve
karsilastirilan buyukluk toplam bir katsayi degil PROFILIN KENDISI.

Esleme Re_theta uzerinden yapilir: referans u+ profili Re_theta = 10000'de
verilmis. Bizim istasyonumuz, kendi cozumumuzden hesaplanan Re_theta o
degere esit olacak sekilde ARANIR (ikiye bolme). Momentum kalinligi
integralinin ust siniri, kaynagin kendi tarifiyle u = %99,5 U_inf.

Sikistirilabilirlik farki KALDIRILMAMISTIR: referans M = 0,2, bizimki
sikistirilamaz. C_f karsilastirmasinda bu akilda tutulmali; u+ profilinde
etkisi cok daha kucuktur.
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
sys.path.insert(0, os.path.join(BURA, "..", "veri"))
from duvaryasasi import profil                           # noqa: E402
from nas_sekil import egriler, deger, kalibrasyon_denetimi  # noqa: E402

KOK = "/tmp/levha"
MODEL = (("SpalartAllmaras", "SA"), ("kOmegaSST", "SST"))


def re_teta(vaka, x):
    """(Re_theta, C_f, u_tau, nu, profil) -- kaynagin kendi tanimiyla."""
    u_tau, nu, p = profil(vaka, x, ust=None, n=128)
    Ue = max(d["u_t"] for d in p)
    y, u = [0.0], [0.0]
    for d in p:
        y.append(d["y"])
        u.append(d["u_t"])
        if d["u_t"] >= 0.995 * Ue:
            break
    t = sum(0.5 * ((u[i-1]/Ue)*(1-u[i-1]/Ue) + (u[i]/Ue)*(1-u[i]/Ue))
            * (y[i] - y[i-1]) for i in range(1, len(y)))
    return t / nu, 2 * u_tau ** 2, u_tau, nu, p


def istasyon(vaka, hedef, a=0.15, b=1.95):
    """Re_theta = hedef olan x'i ikiye bolerek bulur."""
    for _ in range(40):
        m = 0.5 * (a + b)
        if re_teta(vaka, m)[0] < hedef:
            a = m
        else:
            b = m
    return 0.5 * (a + b)


if __name__ == "__main__":
    kotu = kalibrasyon_denetimi()
    if kotu:
        sys.exit("sekil kalibrasyonu gecersiz: %s" % kotu)
    print("Sekil kalibrasyonu gecerli (Coles egrisi log yasasina oturuyor).")

    s41, s42 = egriler("4.1"), egriler("4.2")

    print("\n=== C_f , Re_theta'ya karsi   (NAS-2016-01 Sekil 4.1)")
    print("  model  Re_theta    bizim    Overflow     Cfl3d   bizim/Overflow")
    for m, et in MODEL:
        for h in (5000, 7000, 9000, 11000):
            x = istasyon(os.path.join(KOK, m), h)
            R, cf, _, _, _ = re_teta(os.path.join(KOK, m), x)
            o = deger(s41[(et, "Overflow")], R)
            c = deger(s41[(et, "Cfl3d")], R)
            print("  %-5s %8.0f  %.6f  %.6f  %.6f    %+6.2f%%"
                  % (et, R, cf, o, c, (cf / o - 1) * 100))

    print("\n=== u+ , y+'a karsi , Re_theta = 10000   (NAS-2016-01 Sekil 4.2)")
    for m, et in MODEL:
        vaka = os.path.join(KOK, m)
        x = istasyon(vaka, 10000)
        R, cf, u_tau, nu, p = re_teta(vaka, x)
        print("\n  %s   x = %.3f m   Re_theta = %.0f   C_f = %.6f"
              % (et, x, R, cf))
        print("       y+    bizim    Overflow     Cfl3d     Coles"
              "   bizim-Overflow")
        for yp in (30, 50, 100, 200, 300, 500, 800):
            d = min(p, key=lambda q: abs(q["y"] * u_tau / nu - yp))
            g = d["y"] * u_tau / nu
            up = d["u_t"] / u_tau
            o = deger(s42[(et, "Overflow")], math.log10(g))
            c = deger(s42[(et, "Cfl3d")], math.log10(g))
            k = deger(s42[(et, "kuram")], math.log10(g))
            print("   %7.1f %8.3f %10.3f %9.3f %9.3f        %+7.3f"
                  % (g, up, o, c, k, up - o))
