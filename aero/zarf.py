# -*- coding: utf-8 -*-
"""GECIS TASARIM ZARFI -- aerodinamik moment butcesi zaman icinde.

NEDEN VAR. 7.6 "payi tuketecek C_m" esigini veriyordu ama esigi TEK bir
temsili hizda hesapliyordu. Bu yanlis bir soru sordurtuyordu:

    "90 dereceye kadar C_m ne kadar?"

Oysa gecis boyunca ucak 90 derece HUCUM ACISINA cikmiyor. GOVDE acisi
90 derece donuyor, ama bagil ruzgar da onunla birlikte donuyor -- cunku
ucak ayni anda hizlaniyor ve tirmaniyor. Gercek hucum acisi cok daha
kucuk kaliyor.

BU MODUL 7.4'un kendi yorungesini kullanir (yeni fizik yok) ve her anda
sunu sorar: o andaki q, S ve c ile, elde kalan moment hangi C_m'yi
karsilar?

    C_m_butce(t) = (M_mevcut - I alpha) / (q(t) S c_ort)
    C_m_tavan(t) =  M_mevcut          / (q(t) S c_ort)

Butce, ataletin de dondurulmesi gerektigini varsayar; tavan, sonsuz
yavas donmede bile asilamayacak sinirdir.

SINIR. alpha(t) NOKTA KUTLE yorungesinden gelir: govde ekseni ile hiz
vektoru arasindaki aci. Yorunge yanlissa aci da yanlistir. Ayrica donme
hizinin kendisi, govde boyunca YEREL hucum acisini degistirir; bu ayrica
hesaplanir ve raporlanir.
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)

RHO, G = 1.225, 9.81


def yorunge(m, S, AR, Tw, tr, Vcr, w0=5.0, dt=0.0005, e=0.85, CD0=0.0248,
            astall=math.radians(12), profil="ucgen"):
    """7.4'un benzetimi, ama aci ve hiz gecmisini de dondurur."""
    W = m * G
    Tmax = Tw * W
    vx, vh, t = 0.0, w0, 0.0
    CLa = 2 * math.pi / (1 + 2 / AR)
    iz = []
    while t <= tr:
        tau = min(t / tr, 1.0)
        if profil == "ucgen":
            f = 2 * tau ** 2 if tau <= 0.5 else 1 - 2 * (1 - tau) ** 2
            om = (4 * (math.pi / 2) / tr ** 2) * (tau * tr if tau <= 0.5
                                                  else (1 - tau) * tr)
        else:                                  # yumusak
            f = 3 * tau ** 2 - 2 * tau ** 3
            om = (math.pi / 2) * 6 * (tau - tau ** 2) / tr
        th = math.radians(90) * f
        bx, bh = math.sin(th), math.cos(th)
        V = math.hypot(vx, vh)
        if V > 1e-6:
            ux, uh = vx / V, vh / V
            al = -math.atan2(bx * uh - bh * ux, bx * ux + bh * uh)
        else:
            ux, uh, al = bx, bh, 0.0
        a = abs(al)
        CL = CLa * al if a <= astall else math.copysign(
            2 * math.sin(a) * math.cos(a), al)
        CD = CD0 + CL * CL / (math.pi * AR * e) + 2 * math.sin(a) ** 3
        q = 0.5 * RHO * V * V
        L, D = q * S * CL, q * S * CD
        iz.append(dict(t=t, theta=math.degrees(th), alfa=math.degrees(al),
                       V=V, q=q, omega=om))
        T = Tmax if V < Vcr or vx < Vcr * 0.95 else min(Tmax, D)
        vx += ((T * bx - L * uh - D * ux) / m) * dt
        vh += ((T * bh + L * ux - D * uh) / m - g_) * dt if False else \
              ((T * bh + L * ux - D * uh) / m - G) * dt
        t += dt
    return iz


def zarf(ad, m, S, b, AR, Tw, tr, Vcr, Iyy, M_mevcut, w0=5.0, profil="ucgen"):
    c = S / b
    alpha = (4.0 if profil == "ucgen" else 6.0) * (math.pi / 2) / tr ** 2
    M_at = Iyy * alpha
    iz = yorunge(m, S, AR, Tw, tr, Vcr, w0=w0, profil=profil)

    def but(r):
        d = r["q"] * S * c
        return (M_mevcut - M_at) / d if d > 1e-9 else float("inf")

    en_alfa = max(iz, key=lambda r: abs(r["alfa"]))
    en_dar = min(iz, key=but)
    print("%s   (giris tirmanisi %.0f m/s, %s profil)" % (ad, w0, profil))
    print("  atalet %.1f N m | mevcut %.1f N m | aeroya kalan %.1f N m"
          % (M_at, M_mevcut, M_mevcut - M_at))
    for etiket, r in (("EN BUYUK hucum acisi", en_alfa),
                      ("EN DAR C_m butcesi  ", en_dar)):
        # donme hizinin yerel aciya katkisi: omega * (c/2) / V
        dyerel = math.degrees(math.atan(r["omega"] * 0.5 * c / max(r["V"], 1e-6)))
        print("  %s: t=%.2f s  govde %4.0f°  alfa %5.1f°  V %5.1f m/s  "
              "-> C_m butce %6.3f (yerel aci ±%.1f°)"
              % (etiket, r["t"], r["theta"], abs(r["alfa"]), r["V"],
                 but(r), dyerel))
    print()


if __name__ == "__main__":
    print("=" * 78)
    print("GECIS TASARIM ZARFI -- hucum acisi 90 dereceye CIKMIYOR")
    print("=" * 78)
    print()
    for w0 in (5.0, 0.0):
        zarf("HAFIF 50 kg, t_r = 2 s", 50, 1.98, 3.4528, 6.03, 1.2, 2.0, 30.0,
             7.039, 23.00, w0=w0)
    for w0 in (5.0, 0.0):
        zarf("AGIR 1000 kg, t_r = 5,1 s", 1000, 22.24, 11.55, 6.0, 1.2, 5.1,
             40.0, 1918.294, 952.28, w0=w0)
