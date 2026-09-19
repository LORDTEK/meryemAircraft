# -*- coding: utf-8 -*-
"""BURUN CIFTI, IKI NOKTADA -- 0,599 ve 0,80 ayni palette cikiyor mu?

NEDEN VAR. Makale ayni sabit hatveli burun ciftine iki ayri rejimden iki
ayri verim atfediyor:

    askida  figure of merit  FM   = 0,599   (3.3, 3.8, 3.17)
    seyirde pervane verimi   eta  = 0,80    (2.12 zinciri)

Ikisinin de AYNI palet geometrisinden ciktigi hicbir yerde gosterilmiyor.
Daha kotusu: makale burun ciftinin devrini, pala sayisini, veterini ya da
burulmasini hicbir rejimde vermiyor. Tasarim tablolarinda yalniz CAP ve
DISK YUKLEMESI var. Uc ciftleri ayni makalede yedi pala tasarimi, devir,
uc Mach sayisi ve sayisal bir ceza aliyor (3.4); ucagin her iki rejimde
BUTUN itkisini ureten parca hicbiri almiyor.

Bu betik o bosluğu kapatiyor.

YONTEM. Dort kose, cunku makale iki sayiyi birden iddia ediyor:

    palet H: ASKI icin tasarla  -> askida FM     -> seyirde eta
    palet C: SEYIR icin tasarla -> seyirde eta   -> askida FM

Tek yonlu bir hesap yalniz bir sayiyi sinar. Iki yon gerekiyor.

Denklemler tip_propeller.py'nin denklemleridir; degisen yalniz geometri
ve calisma noktalaridir. Bunu iddia etmek yetmez, bu yuzden __main__
once UC CIFTININ kendi durumunu bu genel motorla kosturup tip_propeller
ile ayni sonucu verdigini gosteriyor. Vermezse hesap durur.

SINIR. Pala sayisi, kesit, veter ve burulma dagilimi SECILDI, olculmedi
-- cunku makalede yok. Bu yuzden sonuc tek sayi degil, makul secimler
uzerinde bir ARALIK. Isaretini tahmin etmiyoruz.
"""
import math
import os
import sys

import numpy as np

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)

from tip_propeller import kesit_kuvvet, RHO, MU, D2R          # noqa: E402


# ---------------------------------------------------------------------
# Genel motor. tip_propeller.py ile ayni denklemler, geometri disaridan.
# ---------------------------------------------------------------------
class Rotor(object):
    def __init__(self, D, B, n_serit=24, hub=0.15):
        self.R = D / 2.0
        self.B = B
        self.r_h = hub * self.R
        kenar = np.linspace(self.r_h, self.R, n_serit + 1)
        self.r = 0.5 * (kenar[:-1] + kenar[1:])
        self.dr = np.diff(kenar)

    # --- palet TASARIMI: her serit hedef kesit c_l'sinde calisir -----
    def tasarla(self, V, om, T_hedef, cl_hedef, tur=40):
        r = self.r
        v = np.full_like(r, max(10.0, 0.5 * V))
        c = np.full_like(r, 0.05 * self.R)
        th = np.zeros_like(r)
        for _ in range(tur):
            Va = V + v
            Vt = om * r
            W = np.hypot(Va, Vt)
            phi = np.arctan2(Va, Vt)
            Re = np.clip(RHO * W * c / MU, 2e4, 2e6)
            a_alt = np.full_like(r, -2.0)
            a_ust = np.full_like(r, 14.0)
            for _ in range(20):
                a_orta = 0.5 * (a_alt + a_ust)
                cl_o, _ = kesit_kuvvet(a_orta, Re)
                dusuk = cl_o < cl_hedef
                a_alt = np.where(dusuk, a_orta, a_alt)
                a_ust = np.where(dusuk, a_ust, a_orta)
            alfa = 0.5 * (a_alt + a_ust)
            th = phi + alfa * D2R
            cl, cd = kesit_kuvvet(alfa, Re)
            dTdr_hedef = T_hedef / (self.R - self.r_h)
            pay = self.B * 0.5 * RHO * W ** 2 * (cl * np.cos(phi)
                                                 - cd * np.sin(phi))
            c_yeni = np.clip(dTdr_hedef / np.maximum(pay, 1e-6),
                             0.04 * self.R, 0.40 * self.R)
            c += 0.4 * (c_yeni - c)
            dT = pay * c
            v_yeni = np.clip(
                -V / 2.0 + np.sqrt(np.maximum(
                    (V / 2.0) ** 2
                    + np.maximum(dT, 0.0) / (4 * math.pi * RHO * r), 0.0)),
                0.5, 60.0)
            v += 0.4 * (v_yeni - v)
        return c, th

    # --- verilen palette BEMT ---------------------------------------
    def coz(self, V, om, c, th, tur=150):
        r, dr = self.r, self.dr
        v = np.full_like(r, 5.0)
        w = np.zeros_like(r)
        for _ in range(tur):
            Va, Vt = V + v, om * r - w
            W = np.hypot(Va, Vt)
            phi = np.arctan2(Va, np.maximum(Vt, 1e-6))
            alfa = (th - phi) / D2R
            Re = np.clip(RHO * W * c / MU, 2e4, 2e6)
            cl, cd = kesit_kuvvet(alfa, Re)
            f = self.B / 2.0 * (self.R - r) / np.maximum(r * np.sin(phi), 1e-6)
            F = np.clip(2 / math.pi * np.arccos(
                np.clip(np.exp(-np.abs(f)), 0, 1)), 1e-3, 1.0)
            q = 0.5 * RHO * W ** 2 * c
            dT = self.B * q * (cl * np.cos(phi) - cd * np.sin(phi))
            dQt = self.B * q * (cl * np.sin(phi) + cd * np.cos(phi))
            disk = 4 * math.pi * RHO * r * F
            with np.errstate(divide="ignore", invalid="ignore"):
                v_yeni = -V / 2.0 + np.sqrt(np.maximum(
                    (V / 2.0) ** 2 + np.maximum(dT, 0.0) / disk, 0.0))
                w_yeni = dQt / np.maximum(2 * disk * (V + v), 1e-6)
            v += 0.3 * (np.clip(np.nan_to_num(v_yeni), 0.0, 80.0) - v)
            w += 0.3 * (np.clip(np.nan_to_num(w_yeni), 0.0,
                                0.5 * om * r) - w)
        Va, Vt = V + v, om * r - w
        W = np.hypot(Va, Vt)
        phi = np.arctan2(Va, np.maximum(Vt, 1e-6))
        alfa = (th - phi) / D2R
        Re = np.clip(RHO * W * c / MU, 2e4, 2e6)
        cl, cd = kesit_kuvvet(alfa, Re)
        q = 0.5 * RHO * W ** 2 * c
        T = (self.B * q * (cl * np.cos(phi) - cd * np.sin(phi)) * dr).sum()
        Q = (self.B * q * (cl * np.sin(phi) + cd * np.cos(phi)) * r * dr).sum()
        return T, Q, alfa

    def devir_icin(self, V, c, th, T_hedef, alt=50.0, ust=6000.0, tur=26):
        """T_hedef'i veren omega. Elektrik tahrikin serbestlik derecesi."""
        for _ in range(tur):
            om = 0.5 * (alt + ust)
            if self.coz(V, om, c, th)[0] < T_hedef:
                alt = om
            else:
                ust = om
        return 0.5 * (alt + ust)

    @property
    def A(self):
        return math.pi * self.R ** 2


# ---------------------------------------------------------------------
# Hafif tasarim, 3.7 tablosu
# ---------------------------------------------------------------------
D_BURUN = 1.20            # m, 3.7
MTOW = 50.1               # kg  (kanat yuku 25,3 x alan 1,979)
W_N = MTOW * 9.81         # N
V_SEYIR = 30.0            # m/s, 3.7
LD_SEYIR = 12.0           # 3.7
T_SEYIR = W_N / LD_SEYIR  # N
P_HOVER_MAKALE = 10900.0  # W, 3.7
FM_MAKALE = 0.599
ETA_MAKALE = 0.80


def fm_makale_yontemi(T_toplam, P_saft_toplam, A):
    """3.7/2.12'nin kendi tanimi: tek disk ideal gucu, cift saft gucu."""
    P_ideal = T_toplam ** 1.5 / math.sqrt(2 * RHO * A)
    return P_ideal / P_saft_toplam, P_ideal


def cift_coz(rot, V, c, th, T_hedef, alt=30.0, ust=3000.0):
    """Esseksenli cift = TEK disk, 2B palet, TAM itki.

    ILK SURUM BUNU YANLIS YAPTI ve sonuc FM = 1,08 idi -- fiziksel olarak
    imkansiz, cunku figure of merit birden buyuk olamaz. Hata suydu: cift,
    her biri TAM A alanina sahip iki ayrik disk olarak modellenmis, her biri
    T/2 uretiyordu; sonra saft gucu makalenin TEK diskli ideal gucune karsi
    okunuyordu. Yani cifte fiziksel olarak sahip olmadigi iki kat eyleyici
    disk alani verilmisti. Bir sayinin imkansiz olmasi, onu yakalayan sey oldu.

    Dogrusu makalenin kendi boyutlandirmasidir: DL = T/A ve P_i =
    T^1,5/sqrt(2 rho A), yani TEK disk. Cift, ayni disk uzerinde 2B paletle
    modelleniyor. Bu, karsit donusun girdap geri kazanimini SAYMAZ; yani
    muhafazakar taraftadir ve boyle isaretlenir.
    """
    om = rot.devir_icin(V, c, th, T_hedef, alt=alt, ust=ust)
    T, Q, alfa = rot.coz(V, om, c, th)
    return om, T, Q * om, alfa


def capraz_denetim():
    """Genel motor, UC CIFTININ kendi durumunda tip_propeller'i tutturuyor mu?

    Tutturmazsa burun sonucu yayimlanmaz. Sessizce gecen bir denetim hic
    olmayandan beterdir; bu projede bir kez oldu.
    """
    import tip_propeller as tp
    rot = Rotor(tp.D, tp.B)
    c, th = rot.tasarla(1e-3, 2100.0, 8.1, 0.55)
    om = rot.devir_icin(1e-3, c, th, 8.1, alt=300.0, ust=6000.0)
    T, Q, _ = rot.coz(1e-3, om, c, th)
    P_cift = 2 * Q * om

    c2, th2 = tp.hover_tasarla(cl_hedef=0.55)
    om2 = tp.devir_itki_icin(c2, th2)
    T2, Q2, _ = tp.bemt_sabit(1e-3, om2, c2, th2)
    P2 = 2 * Q2 * om2
    return (om, T, P_cift), (om2, T2, P2)


def aile(rot, cl_h, om_tasarim, d_theta_deg):
    """Tek parametreli palet ailesi: askı paleti + duzgun hatve kaymasi.

    NEDEN BOYLE. Dort kose yetmedi ve bunu hesabin kendisi gosterdi. Askı
    icin tasarlanan palet bir HELIKOPTER ROTORU cikiyor -- hatve kokte 19,
    ucta 7 derece -- ve 30 m/s'de o palet ancak uc Mach 0,96'da net itki
    veriyor. Seyir icin tasarlanan palet ise tersi. Yani soru "H mi C mi"
    degil; soru, ikisinin ARASINDA makalenin iki sayisini birden veren bir
    palet olup olmadigi. Qwen bunu onceden soyledi.

    Aile: veter askı itkisinden sabitlenir, burulmaya duzgun bir kayma
    eklenir. Kayma sifirda helikopter rotoru, buyukte pervane. Tek parametre,
    ve o parametre tam olarak takasin kendisi.
    """
    c, th = rot.tasarla(1e-3, om_tasarim, W_N, cl_h)
    return c, th + d_theta_deg * D2R


def iki_nokta(rot, c, th):
    """Bir palet, iki rejim. Makalenin kendi tanimlariyla FM ve eta."""
    try:
        om_h, T_h, P_h, _ = cift_coz(rot, 1e-3, c, th, W_N,
                                     alt=30.0, ust=2000.0)
        FM, _ = fm_makale_yontemi(T_h, P_h, rot.A)
    except Exception:
        om_h, T_h, P_h, FM = float("nan"), float("nan"), float("nan"), float("nan")
    try:
        om_c, T_c, P_c, _ = cift_coz(rot, V_SEYIR, c, th, T_SEYIR,
                                     alt=10.0, ust=2000.0)
        eta = T_c * V_SEYIR / P_c if P_c > 0 else float("nan")
        n_c = om_c / (2 * math.pi)
        J = V_SEYIR / (n_c * 2 * rot.R)
    except Exception:
        om_c, P_c, eta, J = float("nan"), float("nan"), float("nan"), float("nan")
    return dict(om_h=om_h, P_h=P_h, FM=FM, om_c=om_c, P_c=P_c, eta=eta, J=J,
                M_h=om_h * rot.R / 340.3, M_c=om_c * rot.R / 340.3)


if __name__ == "__main__":
    print("BURUN CIFTI, IKI NOKTADA")
    print("D = %.2f m, W = %.1f N, V = %.0f m/s, T_seyir = %.1f N (L/D %.1f)"
          % (D_BURUN, W_N, V_SEYIR, T_SEYIR, LD_SEYIR))
    A = math.pi * (D_BURUN / 2) ** 2
    fm_k, P_ideal = fm_makale_yontemi(W_N, P_HOVER_MAKALE, A)
    print("Makalenin kendi aritmetigi: ideal %.0f W / %.0f W = FM %.4f"
          % (P_ideal, P_HOVER_MAKALE, fm_k))
    print("MAKALENIN IDDIASI: FM = %.3f VE eta = %.2f, AYNI PALETTE."
          % (FM_MAKALE, ETA_MAKALE))
    print("Seyirde gereken saft gucu, eta = 0,80 olsaydi: %.0f W"
          % (T_SEYIR * V_SEYIR / ETA_MAKALE))

    print("\n0. CAPRAZ DENETIM -- genel motor, uc ciftinin kendi durumunda")
    print("-" * 74)
    a, b = capraz_denetim()
    print("%-24s %9s %9s %9s" % ("", "om r/s", "T (N)", "cift W"))
    print("%-24s %9.0f %9.2f %9.0f" % ("nose_propeller motoru", a[0], a[1], a[2]))
    print("%-24s %9.0f %9.2f %9.0f" % ("tip_propeller.py", b[0], b[1], b[2]))
    sapma = abs(a[2] - b[2]) / max(b[2], 1e-9)
    print("guc sapmasi %.2f %%" % (100 * sapma))
    if sapma > 0.02:
        print("\n!! DENETIM DUSTU -- motorlar ayni degil. Burun sonucu YAYIMLANMAZ.")
        sys.exit(1)
    print("gecti.")

    for B_PALA in (2, 3):
        rot = Rotor(D_BURUN, 2 * B_PALA)      # esseksenli cift, tek disk
        print("\n%s" % ("=" * 74))
        print("%d PALA / ROTOR  (tek diskte %d palet)" % (B_PALA, 2 * B_PALA))
        print("=" * 74)
        for cl_h in (0.55, 0.70):
            print("\nhedef kesit c_l = %.2f, tasarim devri 250 r/s" % cl_h)
            print("%-8s %8s %8s %8s %8s %8s %8s %8s"
                  % ("d_theta", "om_h", "M_uc", "askı kW", "FM",
                     "om_c", "J", "eta"))
            for dth in (0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0):
                c, th = aile(rot, cl_h, 250.0, dth)
                k = iki_nokta(rot, c, th)
                print("%-8.0f %8.0f %8.2f %8.2f %8.3f %8.0f %8.2f %8.3f"
                      % (dth, k["om_h"], k["M_h"], k["P_h"] / 1000.0, k["FM"],
                         k["om_c"], k["J"], k["eta"]))
