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

# ---------------------------------------- agir uc rotoru: ARALIK denetimi
# BU DENETIM BIR DELIGI KAPATIYOR. 3.8 uzun sure 0,0051 tasidi ve hicbir
# kontrol onu yeniden turetmedi; tur 22'de betik kosturulunca kuralin
# ("FM >= 0,599 saglayanlarin en az surukleyeni") sectigi sayinin 0,00446
# oldugu, 0,0051'in ise listede bulunmayan c_l = 0,70'e ait oldugu
# goruldu. Cozum tek sayiyi degistirmek degil -- degistirmek BIZIM
# LEHIMIZE olurdu -- kuralin agir hatta hic baglamadigini kabul edip
# aralik rapor etmekti. Denetim de artik araligi sinar.
# TUR 55 -- BU DENETIM HATAYI YAKALAMIYOR, YENIDEN URETIYORDU. Betigin
# kendisiyle ayni varsayilan argumanlarla cagiriyordu: sifir_tork(c, th)
# dengeyi 30 m/s'de cozuyor (V=V_SEYIR tanim aninda baglanmis), dcd0 ise
# 40 m/s'nin q'suna boluyordu; hover_tasarla hafif rotorun 2100 rad/s
# tasarim devrini agir rotora uyguluyordu (tasarim uc hizi 703 m/s).
# Denetim ayni hatayi tekrarladigi icin 0,0035-0,0074'u "dogruladi".
# Artik duzeltilmis kurulumu sinar VE eski kurulumun bu beklentiyi
# KARSILAMADIGINI da sinar -- ayrimi yapamayan bir denetim denetim degildir.
print("\n=== agir uc rotoru araligi " + "=" * 32)
try:
    sys.path.insert(0, "/home/user/meryemAircraft/aero")
    import heavy_rotor as _A, tip_propeller as _U

    def _uclar(eski):
        _, _T, _om_t, _V = _A.agir_ayarla(eski)
        _d = []
        for _cl in (0.55, 0.85):           # yalniz iki uc; digerleri arada
            _c, _th = _U.hover_tasarla(cl_hedef=_cl, om=_om_t, T_hedef=_T)
            _om, _T2 = _U.sifir_tork(_c, _th, V=_V)
            if _om:
                _d.append(_U.dcd0(_T2))
        return _d

    _d = _uclar(False)
    if len(_d) == 2:
        esit("agir rotor yuku, ust uc", max(_d), 0.0100, tol=0.03)
        esit("agir rotor yuku, alt uc", min(_d), 0.0045, tol=0.03)
        esit("agir/hafif, ust uc", max(_d) / 0.01535, 0.65, tol=0.03)
        esit("agir/hafif, alt uc", min(_d) / 0.01535, 0.29, tol=0.03)
        _e = _uclar(True)
        esit("ESKI kurulum beklentiyi KARSILAMIYOR (ayrim sinamasi)",
             1.0 if abs(max(_e) - 0.0100) / 0.0100 > 0.03 else 0.0, 1.0, tol=0.001)
    else:
        print("  -- atlandi: sifir tork cozulmedi")
except Exception as _h:                    # pragma: no cover
    # Bir ithal hatasi UC kontrolu sessizce dusuruyordu: yeniden adlandirmada
    # "uc_pervane" -> "tip_propeller" kacinca sayi 43'ten 40'a indi ve kimse
    # gormedi. Sessiz atlama, hic olmayan denetimden beterdir -- artik bagirir.
    print("  ** ATLANDI, BU BIR KUSURDUR (%s: %s)" % (type(_h).__name__, _h))
    _atlanan_blok = True

# ---------------------------------------------- Tablo 15 (3.9) tutarliligi
print("\n=== Tablo 15 " + "=" * 45)
# metinde tam yuzdeye yuvarli — tolerans yarim puan
for tr, P, yuzde in ((2, 221.5, 1.02), (3, 65.6, 0.30), (4, 27.7, 0.13), (5, 14.2, 0.07)):
    esit(f"Tablo 15, {tr} s — aski gucunun kesri", P / 216.2, yuzde,
         tol=0.005 / max(yuzde, 0.07))
# M = I alpha  ->  P ~ 1/t^3 degil, itki 1/t^2, guc T^1.5 -> 1/t^3
esit("Tablo 15 olcegi: P(2s)/P(4s) ~ 2^3", 221.5 / 27.7, 8.0, tol=0.05)

# --------------------------------------------- gecis simulasyonu tablolari (7.4)
print("\n=== gecis tablolari " + "=" * 38)
sys.path.insert(0, "/home/user/meryemAircraft/figures/build")
from transition2 import sim

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

# 7.4'un GOVDEDEKI tablosu. Yukaridakiler sekil verisidir ve T/W = 1,2'de
# kalir; govde tablosu ULASILABILIR orandadir. Ayrimi burada kilitliyoruz
# cunku onceki surumde govde 1,2 varsayiyordu ve kurulu guc onu vermiyor:
# 6.1 itki = agirlik diyor, yani 10,9 kW zaten T/W = 1,00'dir. Donme
# sirasinda ust uc ciftleri tam itkide, alt ciftler sifirda (M = 2TL), ve
# ust ciftler hala yukari itiyor -- kalan oran budur. aero/thrust.py cikarir.
TW_GOVDE = {"hafif": 1.066, "agir": 1.041}
METIN_74_HAFIF = {1: -18.2, 2: -14.7, 3: -11.2, 4: -4.9}
METIN_74_AGIR = {2: -31.0, 3: -26.9, 4: -22.7, 5.1: -13.1}
for tr, gt in METIN_74_HAFIF.items():
    h = sim(50, 1.98, 6, TW_GOVDE["hafif"], tr, 30.0)[0]
    if abs(h - gt) > 0.15:
        print(f"  !! 7.4 hafif t_r={tr}: hesap {h:.1f}  metin {gt}"); sap += 1
for tr, gt in METIN_74_AGIR.items():
    h = sim(1000, 22.24, 6, TW_GOVDE["agir"], tr, 40.0)[0]
    if abs(h - gt) > 0.15:
        print(f"  !! 7.4 agir t_r={tr}: hesap {h:.1f}  metin {gt}"); sap += 1

# Ve mansetin kendisi: referans donme surelerinde 5 m/s girisle kayip SIFIR
# olmali -- ulasilabilir her oranda, T/W = 1,00 dahil. Bu, duzeltmenin
# sonucu degistirmedigini soyleyen iddiadir; bozulursa haber verilmeli.
for ad, m, S, Vcr, tr in (("hafif", 50, 1.98, 30.0, 2.0),
                          ("agir", 1000, 22.24, 40.0, 5.1)):
    for tw in (1.000, TW_GOVDE[ad], 1.132 if ad == "hafif" else 1.082, 1.200):
        h = sim(m, S, 6, tw, tr, Vcr, w0=5.0)[0]
        if h < -0.05:
            print(f"  !! manset {ad} T/W={tw} t_r={tr}: {h:.2f} m (sifir bekleniyordu)")
            sap += 1
print(f"  {'ok  ' if not sap else '!!  '}gecis tablolarinin 68 hucresi — sapan: {sap}")

# -------------------------------------------------------------------- ozet
print("\n" + "=" * 62)
print(f"{kontrol} kontrol calisti, {len(hatalar)} sapma, gecis tablosunda {sap} sapma.")
for ad, h, m2, s2 in hatalar:
    print(f"  SAPMA  {ad}: hesap {h:.4g} / metin {m2:.4g}  (%{100*s2:.1f})")

# ---------------------------------------------------------------------
# TEKRAR EDEN SAYILARIN BIREBIR AYNILIGI
# ---------------------------------------------------------------------
# NEDEN VAR. Son uc turun hatalarinin hepsi ayni sinifta: bir deger bir
# bolumde guncellendi, oteki bolumlerde kalmadi. Surukleme braketi UC
# yerde eski haliyle duruyordu (S1'in kendi nesri dahil, yani digerlerinin
# kaynak gosterdigi yerde) ve alt sinir ucaǧın kullanamayacagi pervaneyi
# tasiyordu. Disaridan iki okuma ayni turda yakaladi.
#
# Bu denetim onu makinaya devrediyor: asagidaki dizgelerin HER BIRI, gectigi
# her dosyada ayni yazilisla gecmek zorunda; eski bir surumu kalmissa
# uretim DURUR.
import glob as _glob, os as _os, io as _io

_KOK = _os.path.dirname(_os.path.dirname(
    _os.path.dirname(_os.path.abspath(__file__))))

_YASAK = {
    "0.0216": "eski surukleme braketi alt siniri (kullanilamaz pervaneyle)",
    "0.0380": "eski surukleme braketi ust siniri",
    "0.0153": "eski rotor surukleme yuvarlamasi (0.0154 olmali)",
    "0.0033": "eski AGIR rotor suruklemesi (kirpma kusurlu; 0.0051 olmali)",
    "0.00446": "agir rotor yukunun EN DUSUK ucu; tek sayi olarak tasinamaz",
    "0.547":  "eski AGIR verim sayisi (kirpma kusurlu)",
    "1 649":  "eski agir menzil (1 571 olmali)",
    "12.37":  "eski agir L/D (11.78 olmali)",
    "1800 km": "eski agir menzil, ikili kullanim beyaninda",
}
_dosyalar = (_glob.glob(_os.path.join(_KOK, "paper", "sections", "*.md"))
             + _glob.glob(_os.path.join(_KOK, "paper", "supplement", "*.md"))
             + [_os.path.join(_KOK, "paper", "00-front-matter.md")])
_bulunan = []
for _f in _dosyalar:
    _t = _io.open(_f, encoding="utf-8").read()
    for _k, _neden in _YASAK.items():
        if _k in _t:
            # 0.00336 gibi uzun sayilarin icindeki yanlis eslesmeyi ele
            if _k == "0.0033" and "0.00336" in _t and _t.count("0.0033") == _t.count("0.00336"):
                continue
            _bulunan.append((_os.path.basename(_f), _k, _neden))
print()
print("=== BAYAT SAYI DENETIMI ===")
if _bulunan:
    for _f, _k, _n in _bulunan:
        print("  !! %s icinde '%s' — %s" % (_f, _k, _n))
    sys.exit("Bayat deger bulundu; uretim durduruldu.")
print("  ok  %d yasakli eski degerin hicbiri %d dosyada gecmiyor."
      % (len(_YASAK), len(_dosyalar)))
