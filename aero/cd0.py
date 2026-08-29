# -*- coding: utf-8 -*-
"""C_D0'i bilesen bilesen kurar. Makalede VARSAYIM: 0.0248.

Yontem
------
Kanat/govde: serit yontemi. Planform istasyonlara bolunur; her istasyonda
yerel veter, yerel t/c ve yerel Reynolds sayisi bulunur; kesit surukleme
katsayisi NeuralFoil'den (XFOIL uzerine egitilmis) SIFIR KALDIRMADA alinir ve
veterle agirliklandirilarak kanat alanina indirgenir:

    C_D0_kanat = (2/S) * integral( Cd(y) * c(y) dy )      0..yari-aciklik

Sifir kaldirmada aliniyor, cunku C_D0 tanimi budur; kaldirmaya bagli agdali
sürükleme ayri hesaplanip Oswald verimine yaziliyor (bkz. asagida).

IKI SENARYO
  serbest : XFOIL'in kendi gecis tahmini. Temiz, cilali yuzey. IYIMSER.
  tetikli : gecis %5 veterde zorlanir, yani neredeyse tam turbulent.
            Uretilmis, boyali, antenli bir yuzey icin GERCEKCI.

Cerceveler: makalenin 5.2'sindeki ayni hesap burada yeniden kuruluyor.
Uc pervaneleri: govde/gobek on alani uzerinden SINIRLANDIRILMIS kestirim;
olculeri secilmedigi icin bir aralik olarak veriliyor.
"""
import sys, os, math
import numpy as np
import aerosandbox as asb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from planform import istasyonlar, olcuier

RHO, NU = 1.225, 1.46e-5
V = 30.0                      # hafif hattin seyir hizi
Q = 0.5 * RHO * V ** 2

# agir hat: ayni bicim, 3.35 kat uzunluk olcegi, 40 m/s
AGIR_OLCEK, AGIR_V = 3.3449, 40.0

# --- cerceveler (5.2 ile ayni) ---
CERCEVE_UZUNLUK = 4 * 0.71    # dort dikme, her biri 0.71 m
CERCEVE_KALINLIK = 0.020
CERCEVE_CD = 0.15             # kaportali kesit

# --- uc pervaneleri: gobek + baglanti ---
# Piyasa taramasi (2026-08): her uc rotoru 8 inc pervanede ~0,83 kgf ve ~168 W
# vermeli. Bu, standart 22 mm statorlu sinifin tam ortasi. T-Motor MT2216'nin
# dis kovan capi 27,8 mm, agirligi 75 g; ayni sinifin 2212 surumu 28 mm.
# Alt sinir bu olcu, ust sinir montaj/kaporta payiyla 32 mm.
UC_GOBEK_CAP = (0.028, 0.032)
UC_GOBEK_SAYISI = 8            # dort cift, her ciftte iki gobek
UC_GOBEK_CD = 0.6              # kisa donel cisim, on alan uzerinden


def skaler(x):
    return float(np.asarray(x).ravel()[0])


def kanat_cd0(tetikli, n=40, olcek=1.0, hiz=None):
    hiz = hiz or V
    ist, yari, _ = istasyonlar(n=n)
    o = olcuier()
    toplam = 0.0
    satir = []
    for a, b in zip(ist[:-1], ist[1:]):
        dy = b[0] - a[0]
        c = 0.5 * (a[2] + b[2]) * olcek
        tc = 0.5 * (a[3] + b[3])
        Re = hiz * c / NU
        kal = int(round(tc * 100))
        kal = min(max(kal, 6), 30)
        kwargs = dict(alpha=0.0, Re=Re, model_size="xlarge")
        if tetikli:
            kwargs.update(xtr_upper=0.05, xtr_lower=0.05)
        r = asb.Airfoil(f"naca00{kal:02d}").get_aero_from_neuralfoil(**kwargs)
        cd = skaler(r["CD"])
        toplam += cd * c * (dy * olcek)
        satir.append((0.5 * (a[0] + b[0]), c, tc, Re, cd))
    return 2 * toplam / (o["alan"] * olcek ** 2), satir, o


def cerceve_cd0(S):
    alan = CERCEVE_UZUNLUK * CERCEVE_KALINLIK
    return CERCEVE_CD * alan / S


def uc_pervane_cd0(S):
    out = []
    for d in UC_GOBEK_CAP:
        alan = UC_GOBEK_SAYISI * math.pi * (d / 2) ** 2
        out.append(UC_GOBEK_CD * alan / S)
    return out


if __name__ == "__main__":
    print(f"seyir: V = {V} m/s · q = {Q:.1f} Pa · nu = {NU:.2e} m2/s\n")
    sonuc = {}
    for tetikli, ad in ((False, "serbest gecis (temiz, iyimser)"),
                        (True, "tetikli gecis (uretilmis yuzey, gercekci)")):
        cd_kanat, satir, o = kanat_cd0(tetikli)
        sonuc[ad] = (cd_kanat, satir, o)
        print(f"--- {ad} ---")
        print(f"{'y/(b/2)':>9}{'veter':>8}{'t/c':>7}{'Re':>11}{'Cd':>9}")
        for y, c, tc, Re, cd in satir[::8]:
            print(f"{y/o['yari']:9.2f}{c:8.3f}{tc*100:6.1f}%{Re:11.3e}{cd:9.5f}")
        print(f"kanat/govde C_D0 = {cd_kanat:.5f}\n")

    o = sonuc[list(sonuc)[0]][2]
    S = o["alan"]
    cd_cer = cerceve_cd0(S)
    cd_uc_alt, cd_uc_ust = uc_pervane_cd0(S)

    print("=" * 62)
    print(f"{'bilesen':<34}{'serbest':>10}{'tetikli':>10}")
    print("-" * 62)
    k_s = sonuc["serbest gecis (temiz, iyimser)"][0]
    k_t = sonuc["tetikli gecis (uretilmis yuzey, gercekci)"][0]
    print(f"{'kanat / govde':<34}{k_s:10.5f}{k_t:10.5f}")
    print(f"{'uc iskeletleri (kaportali)':<34}{cd_cer:10.5f}{cd_cer:10.5f}")
    print(f"{'uc pervane gobekleri (30 mm)':<34}{cd_uc_alt:10.5f}{cd_uc_alt:10.5f}")
    print(f"{'uc pervane gobekleri (50 mm)':<34}{cd_uc_ust:10.5f}{cd_uc_ust:10.5f}")
    print("-" * 62)
    alt_s = k_s + cd_cer + cd_uc_alt
    alt_t = k_t + cd_cer + cd_uc_alt
    ust_s = (k_s + cd_cer + cd_uc_ust) * 1.10
    ust_t = (k_t + cd_cer + cd_uc_ust) * 1.10
    print(f"{'ARA TOPLAM (alt sinir)':<34}{alt_s:10.5f}{alt_t:10.5f}")
    print(f"{'+ buyuk gobek + %10 artik payi':<34}{ust_s:10.5f}{ust_t:10.5f}")
    print("=" * 62)
    print(f"\nmakalede VARSAYILAN C_D0 = 0.0248")
    print(f"hesaplanan aralik: {min(alt_s,alt_t):.4f} – {max(ust_s,ust_t):.4f}")
