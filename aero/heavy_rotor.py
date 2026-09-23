# -*- coding: utf-8 -*-
"""AGIR HATTIN uc rotorlari da serbest donme faturasi odar mi?

3.8 de tam 3.6'nin tasidigi kusuru tasiyor: LD_temiz = 13,6 x 1,12, yani
YALNIZCA uc cerceveleri faturalanmis, serbest donen rotorlar degil.
Hafif hatta o terim 0,0154 cikti; agir hatta OLCEKLEME ile tahmin etmek
yerine ayni BEMT ayni kosullarda kosturuluyor.

AGIR HATTIN KENDI SAYILARI (3.8 ve rotation.py'den, uydurulmuyor):
    D = 0,67 m, 8 disk, V = 40 m/s, S_ref = 22,24 m2
    uc cifti gucu = hover gucunun %12'si / 4 = 0,12 x 216,2 kW / 4
    hover itkisi momentum kuraminden, FM = 0,599 ile

tip_propeller.py modul duzeyi sabitlerle yazilmis; burada o sabitler AGIR
hattin degerleriyle degistiriliyor ve ayni fonksiyonlar cagriliyor.
Kendi kopyasini yazmak, cikan farkin "olcek mi, yoksa ikinci bir
kurulus mu?" sorusunu acik birakirdi.

=====================================================================
TUR 55 DUZELTMESI -- BU BETIK UC AYRI YERDE HAFIF HATTA KALMISTI.
=====================================================================
Modul sabitlerini degistirmek yetmiyordu, cunku uc deger modul
sabitinden DEGIL, baska yerden geliyordu:

1. SEYIR HIZI. tip_propeller.sifir_tork(c, th, V=V_SEYIR) -- varsayilan
   arguman Python'da TANIM ANINDA baglanir. U.V_SEYIR = 40 yapmak onu
   degistirmez; sifir_tork serbest donme dengesini 30 m/s'de cozuyordu.
   Ama dcd0() q'yu modul sabitinden, yani 40 m/s'den aliyordu. Sonuc:
   30 m/s'lik kuvvet 40 m/s'lik dinamik basinca bolundu, terim kabaca
   (30/40)^2 = 0,56 carpanla KUCUK cikti. Makalenin "q artiyor, fatura
   duser" mekanizmasi TAM OLARAK bu hatanin imzasiydi: sifir torkta
   serbest donen rotorun kuvveti q ile olceklenir, q birinci mertebede
   SADELESIR.

2. TASARIM DEVRI. hover_tasarla(cl_hedef, om=2100.0, ...) -- 2100 rad/s
   hafif rotorun (R = 0,10 m) tasarim devri, uc hizi 210 m/s. Agir
   rotorda (R = 0,335 m) ayni devir 703 m/s tasarim uc hizi demek; palet
   o hiz icin tasarlaninca veter kucuk cikiyor ve rotor askida uc Mach
   ~1,0'da donuyor. Makalenin "dolgunluk 0,075 -> 0,044 duser" terimi
   BU hatanin imzasiydi. Duzeltme: ayni tasarim uc hizi, 210 m/s.

3. GOBEK. r_h = 0,15 R ithal aninda hesaplaniyor (0,015 m) ve R
   degisince guncellenmiyordu; agir rotorda gobek %4,5 R'de kaliyordu.
   Duzeltme: r_h = 0,15 R, hafif hattaki oranla ayni.

--eski bayragi eski kurulumu AYNEN yeniden uretir (0,0051 ve 0,0035 -
0,0074) -- hatanin geri konup yakalandigini gormek icin. Varsayilan
kosu duzeltilmis kurulumdur. Sonuc: aero/heavy-rotor-result.txt.
"""
import math, os, sys

import numpy as np

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
import tip_propeller as U                                  # noqa: E402

P_HOVER_KW, D_AGIR, V_AGIR, S_AGIR = 216.2, 0.67, 40.0, 22.24
FM = 0.599
OM_HAFIF, R_HAFIF, V_HAFIF = 2100.0, 0.10, 30.0     # hafif hattin tasarim devri
UC_HIZI_TASARIM = OM_HAFIF * R_HAFIF                # 210 m/s, iki hatta ayni
HAFIF_DCD0 = 0.01535                                # tip_propeller, c_l 0,68
LISTE = (0.55, 0.62, 0.68, 0.70, 0.72, 0.75, 0.78, 0.85)
KK = U.kesit_kuvvet


def agir_ayarla(eski=False):
    """Agir hattin kurulumu. eski=True: Tur 55 oncesi kurulum, aynen."""
    U.D, U.R = D_AGIR, D_AGIR / 2.0
    U.V_SEYIR, U.S_REF = V_AGIR, S_AGIR
    U.r_h = 0.015 if eski else 0.15 * U.R
    om_tasarim = OM_HAFIF if eski else UC_HIZI_TASARIM / U.R
    V_denge = V_HAFIF if eski else V_AGIR
    p_cift = 0.12 * P_HOVER_KW * 1000.0 / 4.0
    A = math.pi * U.R ** 2
    # momentum: P = T^1.5 / (FM sqrt(2 rho A))  ->  T
    T = (p_cift / 2.0 * FM * math.sqrt(2 * U.RHO * A)) ** (2.0 / 3.0)
    return p_cift, T, om_tasarim, V_denge


def dolgunluk(c):
    r, dr = U.serit()
    return U.B * (c * dr).sum() / (math.pi * U.R ** 2)


def medyan_Re(V, om, c):
    r, _ = U.serit()
    return float(np.median(U.RHO * np.hypot(V, om * r) * c / U.MU))


def serbest(c, th, V, re_bolen=1.0):
    """Sifir tork dengesi; re_bolen > 1 kesit Re'sini yapay olarak dusurur."""
    if re_bolen != 1.0:
        U.kesit_kuvvet = lambda a, Re: KK(a, np.clip(Re / re_bolen, 2e4, 2e6))
    try:
        return U.sifir_tork(c, th, V=V)
    finally:
        U.kesit_kuvvet = KK


def tara(T, om_tasarim, V_denge):
    satirlar = []
    for cl_h in LISTE:
        c, th = U.hover_tasarla(cl_hedef=cl_h, om=om_tasarim, T_hedef=T)
        om = U.devir_itki_icin(c, th, T_hedef=T)
        Th, Q, _ = U.bemt_sabit(1e-3, om, c, th)
        P = 2 * Q * om
        A = math.pi * U.R ** 2
        fm = 2 * (Th ** 1.5 / math.sqrt(2 * U.RHO * A)) / P if P > 0 else 0.0
        om2, T2 = serbest(c, th, V_denge)
        d = U.dcd0(T2) if om2 else float("nan")
        satirlar.append(dict(cl=cl_h, fm=fm, M_h=om * U.R / 340.0,
                             sigma=dolgunluk(c), om0=om2 or 0.0, d=d, c=c, th=th))
    return satirlar


if __name__ == "__main__":
    eski = "--eski" in sys.argv
    p_cift, T, om_t, V_d = agir_ayarla(eski)
    print("AGIR HAT, UC ROTORU  --  %s KURULUM"
          % ("ESKI (Tur 55 oncesi, HATALI)" if eski else "DUZELTILMIS"))
    print("  D %.2f m, gobek %.4f m (%.1f %% R), 8 disk, S_ref %.2f m2"
          % (U.D, U.r_h, 100 * U.r_h / U.R, U.S_REF))
    print("  tasarim devri %.0f rad/s -> tasarim uc hizi %.0f m/s"
          % (om_t, om_t * U.R))
    print("  serbest donme dengesi %.0f m/s'de; dC_D0 q'su %.0f m/s'de"
          % (V_d, U.V_SEYIR))
    print("  cift gucu %.0f W, rotor basina hover itkisi %.1f N" % (p_cift, T))
    print("  (hafif hat: 335 W, 8,1 N; tasarim uc hizi 210 m/s; gobek %15 R)")
    print()
    print("%-7s %7s %9s %9s %9s %12s %8s"
          % ("c_l", "FM", "askiMach", "dolgunluk", "om0 r/s", "dC_D0 8disk", "/hafif"))
    s = tara(T, om_t, V_d)
    for k in s:
        print("%-7.2f %7.3f %9.2f %9.4f %9.0f %12.5f %8.2f"
              % (k["cl"], k["fm"], k["M_h"], k["sigma"], k["om0"], k["d"],
                 k["d"] / HAFIF_DCD0))
    uygun = [k for k in s if k["fm"] >= FM]
    print()
    print("FM >= %.3f saglayan: %d / %d tasarim" % (FM, len(uygun), len(s)))
    if uygun:
        lo = min(k["d"] for k in uygun)
        hi = max(k["d"] for k in uygun)
        print("  dC_D0 araligi %.5f - %.5f ; hafif hattin %.5f'ine oran %.2f - %.2f"
              % (lo, hi, HAFIF_DCD0, lo / HAFIF_DCD0, hi / HAFIF_DCD0))
        print("  KURAL BAGLAMIYOR: hepsi hover sartini sagliyor; aralik taranan")
        print("  listenin ucuyla (c_l %.2f - %.2f) sinirli, fizikle degil."
              % (LISTE[0], LISTE[-1]))
    if eski:
        sys.exit(0)

    # --- MEKANIZMA DENEYI -------------------------------------------------
    # Ayni-c_l karsilastirmasi: hafif hattin secilen tasarimi c_l 0,68.
    k68 = [k for k in s if abs(k["cl"] - 0.68) < 1e-9][0]
    print()
    print("MEKANIZMA -- hangi terim hareket ediyor? (c_l 0,68, hafif hattin secimi)")
    hafif_sigma = 0.0754                      # tip_propeller, c_l 0,68
    print("  dolgunluk: hafif %.4f, agir %.4f  -> agir DAHA DOLGUN (x%.2f)"
          % (hafif_sigma, k68["sigma"], k68["sigma"] / hafif_sigma))
    # 1) q: ayni palet 30 ve 40 m/s'de
    om30, T30 = serbest(k68["c"], k68["th"], 30.0)
    U.V_SEYIR = 30.0
    d30 = U.dcd0(T30)
    U.V_SEYIR = V_AGIR
    print("  q deneyi, ayni agir palet: 30 m/s'de %.5f, 40 m/s'de %.5f (oran %.3f;"
          % (d30, k68["d"], k68["d"] / d30))
    print("    q oranina (%.3f) bakilsaydi 1/%.3f = %.3f olmaliydi -- q SADELESIYOR,"
          % ((40 / 30) ** 2, (40 / 30) ** 2, (30 / 40) ** 2))
    print("    kalan kucuk dusus Reynolds'tan)")
    # 2) Re: agir paleti hafif hattin Reynolds'una indir
    ReH = medyan_Re(V_AGIR, k68["om0"], k68["c"])
    U.D, U.R = 0.20, 0.10
    U.r_h = 0.15 * U.R
    cL, thL = U.hover_tasarla(cl_hedef=0.68)
    omL, _ = U.sifir_tork(cL, thL, V=V_HAFIF)
    ReL = medyan_Re(V_HAFIF, omL, cL)
    agir_ayarla(False)
    omx, Tx = serbest(k68["c"], k68["th"], V_AGIR, re_bolen=ReH / ReL)
    dx = U.dcd0(Tx)
    print("  Re deneyi: medyan kesit Re hafif %.0f, agir %.0f (x%.2f)" % (ReL, ReH, ReH / ReL))
    print("    agir palet hafif hattin Re'sine indirilince dC_D0 = %.5f,"
          % dx)
    print("    hafif hattin %.5f'inin %.2f kati -- DUSUSUN TAMAMI REYNOLDS'TAN"
          % (HAFIF_DCD0, dx / HAFIF_DCD0))
