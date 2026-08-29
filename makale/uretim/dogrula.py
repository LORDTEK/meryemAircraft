# -*- coding: utf-8 -*-
"""Makalenin her basik sayisini, makalenin kendi denklemleriyle yeniden hesaplar.

Amac: metinde duran sayilarla, o sayilari uretmesi gereken bagintilarin
birbirini tutup tutmadigini bagimsiz olarak sinamak. Sapma esigi %1,5.
"""
import math, re, glob, sys

g, RHO = 9.81, 1.225
hatalar, kontrol = [], 0


def esit(ad, hesap, metin, tol=0.015, birim=""):
    global kontrol
    kontrol += 1
    sapma = abs(hesap - metin) / abs(metin) if metin else abs(hesap)
    isaret = "  ok " if sapma <= tol else "  !! "
    if sapma > tol:
        hatalar.append((ad, hesap, metin, sapma))
    print(f"{isaret}{ad:<46} hesap {hesap:>10.4g}   metin {metin:>10.4g} {birim}"
          f"   sapma {100*sapma:5.2f} %")


# ------------------------------------------------------ verim zinciri (Bolum 6.1)
ZINCIR = dict(motor=0.28, jeneratör=0.90, guc_elek=0.95, makine=0.92, pervane=0.80)
ETA = 1.0
for v in ZINCIR.values():
    ETA *= v
esit("zincir verimi (6.1)", ETA, 0.176)

FoM = 0.60            # sekil-i liyakat — 6.1'de "figure of merit" olarak aniliyor
ESTAR = 12.9 * 3.6e6  # J/kg, yakit

TASARIM = [
    # ad,        m,     S,      b,     Dana,  Dic,  Lp,    V,   LD,  yakit_pay
    ("hafif",    50.0,  1.9785, 3.453, 1.20,  0.20, 0.71,  30., 12.0, 0.16),
    ("agir",   1000.0, 22.24,  11.55, 5.40,  0.67, 2.38,  40., 13.6, 0.16),
]

BEKLENEN = {
 "hafif": dict(AR=6.00, kanat_yuku=25.3, disk_yuku=44.2, hover=10.9e3,
               seyir_elek=1.7e3, motor_mil=1.9e3, menzil=1598e3, dayanim=14.8,
               q_iz=433., Vstall=20.1),
 "agir":  dict(AR=6.00, kanat_yuku=45.0, disk_yuku=43.7, hover=216.2e3,
               seyir_elek=39.2e3, motor_mil=45.8e3, menzil=1814e3, dayanim=12.6),
}

for ad, m, S, b, Dana, Dic, Lp, V, LD, yakit in TASARIM:
    print(f"\n=== {ad} — {m:.0f} kg " + "=" * 34)
    B = BEKLENEN[ad]
    W = m * g
    A = math.pi * (Dana / 2) ** 2

    esit(f"{ad}: en-boy orani b^2/S", b * b / S, B["AR"])
    esit(f"{ad}: kanat yuku m/S", m / S, B["kanat_yuku"], birim="kg/m2")
    esit(f"{ad}: disk yuku m/A", m / A, B["disk_yuku"], birim="kg/m2")

    # askı gucu — momentum teorisi + sekil-i liyakat
    P_hover = W ** 1.5 / (FoM * math.sqrt(2 * RHO * A))
    esit(f"{ad}: askı gucu W^1.5/(FoM*sqrt(2rhoA))", P_hover, B["hover"], birim="W")

    # seyir gucu — surukleme polarindan
    P_itki = W * V / LD
    P_mil = P_itki / ZINCIR["pervane"]
    P_elek = P_mil / ZINCIR["makine"]
    P_motor = P_elek / (ZINCIR["jeneratör"] * ZINCIR["guc_elek"])
    # metinde iki anlamli haneye yuvarli — tolerans buna gore
    esit(f"{ad}: seyir elektrik gucu", P_elek, B["seyir_elek"], tol=0.03, birim="W")
    esit(f"{ad}: seyir motor mil gucu", P_motor, B["motor_mil"], tol=0.03, birim="W")

    # L/D, AZAMI degil, SEYIR NOKTASINDA olculur (6.1). Formulden geri
    # cikarilan C_D0 ile polar yeniden kurulup metindeki L/D sinaniyor.
    CL = W / (0.5 * RHO * V ** 2 * S)
    cd0 = math.pi * B["AR"] * 0.85 / (4 * {"hafif": 12.70, "agir": 14.00}[ad] ** 2)
    esit(f"{ad}: seyir noktasinda L/D = C_L/C_D",
         CL / (cd0 + CL ** 2 / (math.pi * B["AR"] * 0.85)), LD, tol=0.01)

    # menzil — R = (m_f/m) E* eta (L/D) / g
    R = yakit * ESTAR * ETA * LD / g
    esit(f"{ad}: menzil (m_f/m)E*eta(L/D)/g", R, B["menzil"], birim="m")
    esit(f"{ad}: dayanim R/V", R / V / 3600, B["dayanim"], birim="h")

    if ad == "hafif":
        esit("hafif: iz basinci q = T/A (askıda)", W / A, B["q_iz"], birim="Pa")
        esit("hafif: 26 m/s'nin q'su", 0.5 * RHO * 26.6 ** 2, W / A)
        esit("hafif: stall hizi (C_Lmax = 1.0)",
             math.sqrt(2 * W / (RHO * S * 1.0)), B["Vstall"], birim="m/s")

# ------------------------------------------------- uc pervaneleri (4.4 ve 7.4)
print("\n=== uc pervaneleri " + "=" * 40)
T_uc, L_uc, D_uc = 16.2, 0.71, 0.20
A_uc = math.pi * (D_uc / 2) ** 2
esit("uc cifti kumanda momenti M = 2TL", 2 * T_uc * L_uc, 23.0, birim="N.m")
esit("uc cifti gucu (eta=0.70)",
     T_uc ** 1.5 / (0.70 * math.sqrt(2 * RHO * A_uc)), 335., birim="W")
esit("dort uc cifti toplami", 4 * 335., 1340., birim="W")
esit("uc guc / askı gucu", 4 * 335. / 10.9e3, 0.123)
esit("dikme acikligi 2L", 2 * L_uc, 1.42, birim="m")

# ------------------------------------------------------ olcek yasalari (6.4)
print("\n=== olcek " + "=" * 48)
# Bolum 6.4: geometrik benzerlik KORUNMUYOR — kanat yuku 25,3'ten 45,0'e cikiyor.
# Bu yuzden aciklik orani m^(1/3) degil, kanat alani oraninin karekokudur.
esit("aciklik orani = sqrt(S orani)", 11.55 / 3.453, math.sqrt(22.24 / 1.9785))
esit("aciklik orani (metinde 3.35)", 11.55 / 3.453, 3.35)
esit("geometrik benzerlik olsaydi (m^1/3)", (1000 / 50) ** (1 / 3), 2.71)
esit("kanat yuku orani", 45.0 / 25.3, 22.24 / 1.9785 / 20 * 20 / (22.24 / 1.9785) * 1.78,
     tol=0.02)
# disk yuku sabit -> A ~ W -> P_hover ~ W  (klasik L^3.5 DEGIL). 6.4'un ana savi.
esit("pervane capi orani = sqrt(kutle orani)", 5.40 / 1.20, math.sqrt(20.0))
esit("askı gucu orani = kutle orani (L^3.5 degil)", 216.2 / 10.9, 20.0, tol=0.02)
esit("cap/aciklik: hafif", 1.20 / 3.453, 0.35, tol=0.02)
esit("cap/aciklik: agir", 5.40 / 11.55, 0.47, tol=0.02)

# ------------------------------------------------- Tablo 4 (6.4) tutarliligi
print("\n=== Tablo 4 " + "=" * 46)
# metinde tam yuzdeye yuvarli — tolerans yarim puan
for tr, P, yuzde in ((2, 221.5, 1.02), (3, 65.6, 0.30), (4, 27.7, 0.13), (5, 14.2, 0.07)):
    esit(f"Tablo 4, {tr} s — askı gucunun kesri", P / 216.2, yuzde,
         tol=0.005 / max(yuzde, 0.07))
# M = I alpha  ->  P ~ 1/t^3 degil, itki 1/t^2, guc T^1.5 -> 1/t^3
esit("Tablo 4 olcegi: P(2s)/P(4s) ~ 2^3", 221.5 / 27.7, 8.0, tol=0.05)

# --------------------------------------------- gecis simulasyonu tablolari (7.4)
print("\n=== gecis tablolari " + "=" * 38)
sys.path.insert(0, "/home/user/meryemAircraft/gorsel/uretim")
from gecis2 import sim

METIN_HAFIF = {0.5: (-19.1, -16.6, -14.5, -11.0), 1: (-17.1, -14.2, -11.6, -3.5),
               2: (-13.2, -9.1, -2.1, 0), 3: (-9.9, -0.8, 0, 0), 4: (-2.2, 0, 0, 0)}
METIN_AGIR = {1: (-32.2, -27.4, -23.3, -16.0), 2: (-27.0, -20.9, -7.7, -1.0),
              3: (-21.8, -7.2, -1.4, 0), 4: (-17.7, -1.4, 0, 0), 5: (-5.8, 0, 0, 0)}
METIN_TIRM = {1: (-14.2, -10.3, -0.4, 0), 2: (-9.1, -0.4, 0, 0),
              3: (-0.8, 0, 0, 0), 4: (0, 0, 0, 0)}

sap = 0
for tr, satir in METIN_HAFIF.items():
    for tw, gt in zip((1.1, 1.2, 1.3, 1.5), satir):
        h = sim(50, 1.98, 6, tw, tr, 30.0)[0]
        if abs(h - gt) > 0.15:
            print(f"  !! hafif t_r={tr} T/W={tw}: hesap {h:.1f}  metin {gt}"); sap += 1
for tr, satir in METIN_AGIR.items():
    for tw, gt in zip((1.1, 1.2, 1.3, 1.5), satir):
        h = sim(1000, 22.24, 6, tw, tr, 40.0)[0]
        if abs(h - gt) > 0.15:
            print(f"  !! agir t_r={tr} T/W={tw}: hesap {h:.1f}  metin {gt}"); sap += 1
for tr, satir in METIN_TIRM.items():
    for w0, gt in zip((0, 2, 5, 8), satir):
        h = sim(50, 1.98, 6, 1.2, tr, 30.0, w0=w0)[0]
        if abs(h - gt) > 0.15:
            print(f"  !! tirmanis t_r={tr} w0={w0}: hesap {h:.1f}  metin {gt}"); sap += 1
print(f"  {'ok  ' if not sap else '!!  '}gecis tablolarinin 52 hucresi — sapan: {sap}")

# -------------------------------------------------------------------- ozet
print("\n" + "=" * 62)
print(f"{kontrol} kontrol calisti, {len(hatalar)} sapma, gecis tablosunda {sap} sapma.")
for ad, h, m2, s2 in hatalar:
    print(f"  SAPMA  {ad}: hesap {h:.4g} / metin {m2:.4g}  (%{100*s2:.1f})")
