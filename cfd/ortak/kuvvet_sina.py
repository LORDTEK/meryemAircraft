# -*- coding: utf-8 -*-
"""kuvvet.py'yi BAGIMSIZ yollardan sinar.

Gerekcesi: OpenFOAM'in kendi forceCoeffs'i bu kurulumda calismadigi icin
katsayilar kuvvet.py ile hesaplaniyor. O kod artik yuk tasiyor, dolayisiyla
kendisi de sinanmali. Uc sinama, uc ayri seyi yakalar:

1. YUZEY ALANI  -- duvar yuzlerinin alan toplami, profil cevresi x acikliga
   esit mi? Alan hesabindaki bir hata butun kuvvetleri ayni oranda kaydirir
   ve baska hicbir sinama bunu yakalamaz.

2. KAPALI YUZEY  -- duvar yuzlerinin alan VEKTORU toplami sifir olmali
   (kapali bir yuzeyin net normali sifirdir). Yuz yonelimlerindeki bir
   tutarsizligi yakalar.

3. MOMENTUM DENGESI -- govdeye etkiyen kuvvet, dis sinirlardan gecen
   momentum akisi ve basinc integralinden de hesaplanabilir:

       F_govde = -kapali_integral_dis( U (U.n) + p n ) dA

   Bu, TAMAMEN BASKA yuzler ve baska bir fiziksel ilke kullanir. Duvarda
   yapilan integralle karsilastirilir.

   Beklenti olcusuz iyimser olmamali: uzak alan 20 veterde ve orada ag
   kabadir, dolayisiyla momentum dengesinden gelen surukleme birkac yuzde
   sapar. Sinamanin isi mertebeyi ve isareti dogrulamaktir -- iki katlik
   ya da ters isaretli bir hatayi yakalar, binde birlik bir farki degil.
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from foamoku import Ag, Alan, son_zaman        # noqa: E402
from kuvvet import hesapla, nu_oku             # noqa: E402
from cagi import naca4                         # noqa: E402


def cevre(kod="0012", n=20000, kapali=True):
    """Profilin yay uzunlugu (iki yuzey toplami)."""
    xs = [(1 - math.cos(math.pi * i / n)) / 2 for i in range(n + 1)]
    L = 0.0
    for i in range(n):
        dx = xs[i + 1] - xs[i]
        dy = naca4(kod, xs[i + 1], kapali) - naca4(kod, xs[i], kapali)
        L += math.hypot(dx, dy)
    return 2 * L


def sina(vaka, kod="0012", aciklik=1.0, alfa=0.0, zaman=None):
    ag = Ag(vaka)
    z = zaman or son_zaman(vaka)
    y = ag.yama["duvar"]

    A_top, S_top = 0.0, [0.0, 0.0, 0.0]
    for k in range(y["n"]):
        S, _ = ag.yuz_alan(y["bas"] + k)
        A_top += math.sqrt(S[0] ** 2 + S[1] ** 2 + S[2] ** 2)
        for a in range(3):
            S_top[a] += S[a]
    A_bek = cevre(kod) * aciklik

    print("1. YUZEY ALANI")
    print("   agdan       %.6f m2" % A_top)
    print("   profilden   %.6f m2   (cevre %.6f x aciklik %.1f)"
          % (A_bek, cevre(kod), aciklik))
    print("   fark        %+.3f %%   <- ag, egri yuzeyi kirikli cizgiyle"
          % ((A_top / A_bek - 1) * 100))
    print("                          temsil ettigi icin HEP biraz kucuk cikar")

    print("2. KAPALI YUZEY")
    print("   alan vektoru toplami (%.2e %.2e %.2e)" % tuple(S_top))
    print("   |toplam| / alan = %.2e   <- sifir olmali" %
          (math.sqrt(sum(v * v for v in S_top)) / A_top))

    # --- 3. momentum dengesi
    p = Alan(vaka, z, "p")
    U = Alan(vaka, z, "U", vektor=True)
    F = [0.0, 0.0, 0.0]
    for ad in ("disalan", "cikis"):
        if ad not in ag.yama:
            continue
        ym = ag.yama[ad]
        for k in range(ym["n"]):
            fi = ym["bas"] + k
            S, _ = ag.yuz_alan(fi)
            uv = U.yama_degeri(ad, k)
            if uv is None:
                uv = U.ic[ag.sahip[fi]]
            pf = p.yama_degeri(ad, k)
            if pf is None:
                pf = p.ic[ag.sahip[fi]]
            akis = uv[0] * S[0] + uv[1] * S[1] + uv[2] * S[2]   # U.n dA
            for a in range(3):
                F[a] -= uv[a] * akis + pf * S[a]

    a = math.radians(alfa)
    q = 0.5
    CD_m = (F[0] * math.cos(a) + F[1] * math.sin(a)) / q
    CL_m = (-F[0] * math.sin(a) + F[1] * math.cos(a)) / q
    r = hesapla(vaka, alfa=alfa, zaman=z)

    print("3. MOMENTUM DENGESI")
    print("   duvarda integral   C_D = %.6f   C_L = %+.6f" % (r["CD"], r["CL"]))
    print("   dis sinirlardan    C_D = %.6f   C_L = %+.6f" % (CD_m, CL_m))
    print("   fark               %+.2f %%" % ((CD_m / r["CD"] - 1) * 100
                                              if r["CD"] else 0.0))
    return dict(A_ag=A_top, A_bek=A_bek, CD_duvar=r["CD"], CD_momentum=CD_m)


if __name__ == "__main__":
    sina(sys.argv[1], alfa=float(sys.argv[2]) if len(sys.argv) > 2 else 0.0)
