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
    #
    # RANS'ta bir yuzeyden gecen momentum akisi yalnizca U(U.n) + p n
    # DEGILDIR. Uc terim daha var ve ucu de burada hesaba katiliyor:
    #
    #   (2/3) k n   Reynolds gerilmesinin izotropik parcasi. Izde k
    #               ihmal edilebilir degildir; atlanirsa surukleme
    #               sistematik olarak kayar.
    #   nu_eff dU/dn  yuzeydeki kayma. Uzak alanda kucuk, cikista degil.
    #   U_inf * mdot  sahte kutle kaynagi duzeltmesi. Cozucu korunumlu yuz
    #               akisini (phi) korur, bizim kullandigimiz U.S'yi degil;
    #               ikisi arasindaki fark kapali yuzeyde sifir olmayan bir
    #               net kutle akisi birakir ve o da sahte momentum uretir.
    p = Alan(vaka, z, "p")
    U = Alan(vaka, z, "U", vektor=True)
    kk = Alan(vaka, z, "k") if os.path.exists(os.path.join(vaka, z, "k")) else None
    nut = Alan(vaka, z, "nut") if os.path.exists(
        os.path.join(vaka, z, "nut")) else None
    nu = nu_oku(vaka)
    merkez = ag.hucre_merkez()

    F = [0.0, 0.0, 0.0]
    mdot = 0.0
    for ad in ("disalan", "cikis"):
        if ad not in ag.yama:
            continue
        ym = ag.yama[ad]
        for k in range(ym["n"]):
            fi = ym["bas"] + k
            S, C = ag.yuz_alan(fi)
            A = math.sqrt(S[0] ** 2 + S[1] ** 2 + S[2] ** 2)
            if A <= 0:
                continue
            nrm = [S[a] / A for a in range(3)]
            h = ag.sahip[fi]
            uv = U.yama_degeri(ad, k)
            if uv is None:
                uv = U.ic[h]
            pf = p.yama_degeri(ad, k)
            if pf is None:
                pf = p.ic[h]
            kf = 0.0
            if kk is not None:
                v = kk.yama_degeri(ad, k)
                kf = v if v is not None else kk.ic[h]
            nutf = 0.0
            if nut is not None:
                v = nut.yama_degeri(ad, k)
                nutf = v if v is not None else nut.ic[h]

            akis = sum(uv[a] * S[a] for a in range(3))
            mdot += akis
            # normal gerilme: p + (2/3)k
            for a in range(3):
                F[a] -= uv[a] * akis + (pf + 2.0 / 3.0 * kf) * S[a]
            # kayma: nu_eff * dU/dn, komsu hucreden tek yanli
            cm = merkez[h]
            d = abs(sum((cm[a] - C[a]) * nrm[a] for a in range(3)))
            if d > 0:
                uc = U.ic[h]
                for a in range(3):
                    F[a] += (nu + nutf) * (uv[a] - uc[a]) / d * A

    # sahte kutle kaynaginin tasidigi momentumu geri al
    for a in range(3):
        F[a] += mdot * (math.cos(math.radians(alfa)) if a == 0 else
                        math.sin(math.radians(alfa)) if a == 1 else 0.0)

    a = math.radians(alfa)
    q = 0.5
    CD_m = (F[0] * math.cos(a) + F[1] * math.sin(a)) / q
    CL_m = (-F[0] * math.sin(a) + F[1] * math.cos(a)) / q
    r = hesapla(vaka, alfa=alfa, zaman=z)

    print("3. MOMENTUM DENGESI")
    print("   net kutle akisi    %+.3e  (duzeltildi)" % mdot)
    print("   duvarda integral   C_D = %.6f   C_L = %+.6f" % (r["CD"], r["CL"]))
    print("   dis sinirlardan    C_D = %.6f   C_L = %+.6f" % (CD_m, CL_m))
    print("   fark               %+.2f %%" % ((CD_m / r["CD"] - 1) * 100
                                              if r["CD"] else 0.0))
    print("   NOT: bu sinama kaba. Dis sinir 20 veterde ve orada ag seyrek;")
    print("        sapmanin buyuklugu degil, MERTEBESI ve AG INCELDIKCE")
    print("        KUCULMESI anlamlidir.")
    return dict(A_ag=A_top, A_bek=A_bek, CD_duvar=r["CD"], CD_momentum=CD_m,
                mdot=mdot)


if __name__ == "__main__":
    sina(sys.argv[1], alfa=float(sys.argv[2]) if len(sys.argv) > 2 else 0.0)
