# -*- coding: utf-8 -*-
"""UC PERVANESI SEYIRDE -- sifir saft torkunda ne kadar suruklüyor?

NEDEN VAR. 3.3 su tabloyu veriyor ve makalenin "Fatura 2 azaltildi,
kaldirilmadi" iddiasi tamamen ona dayaniyor:

    sifir saft yukunde donen   ->  dC_D0 = 0,0003 - 0,0008
    kenarindan durdurulmus     ->  0,0008
    genis yuzeyle durdurulmus  ->  0,015 - 0,018

Ucuncu satirla birincinin arasi otuz kat ve ORTA satirlar yok; yani
sonucun saglamligi "hangi durumda oldugu" sorusuna baglaniyor, sayinin
kendisine degil. Ama birinci satirin kendisi VARSAYIM. Bu betik onu
hesapliyor.

YONTEM. Once palet hover'da TASARLANIR: 16,2 N'u 335 W ile veren burulma
ve veter dagilimi aranir -- yani karsilastirilan sey gercekten bu ucagin
pervanesidir, genel bir pervane degil. Sonra ayni palet seyir hizinda
kosturulur ve NET SAFT TORKUNUN SIFIR oldugu devir aranir. O devirde
eksenel kuvvet okunur; isareti negatifse suruklemedir.

Kesit verisi NeuralFoil'den, her serit kendi yerel Reynolds'unda ve kendi
yerel hucum acisinda cagrilir. Palet kesitleri ince ve dusuk Re'de; bu
bolgede lineer teori kullanilmaz.

NE ALEYHIMIZE SAYILIR. Sekiz diskin toplam dC_D0'i 0,004'e ULASIRSA --
ki bu zaten uc cerceveleri icin odedigimiz sayi -- "Fatura 2 yok"
iddiasi coker: seyir L/D duser, B'ye karsi menzil ustunlugu erir.

SINIR. Palet kesiti, veter ve burulma dagilimi SECILDI, olculmedi.
Gercek bir pervane baska cikabilir. Bu yuzden sonuc tek sayi degil,
makul tasarimlar uzerinde bir ARALIK olarak veriliyor.
"""
import math, os, sys

import numpy as np

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)

import neuralfoil as nf                                     # noqa: E402

RHO = 1.225
D2R = math.pi / 180.0

# --- 3.7 / 2.10'dan uc cifti -----------------------------------------
D = 0.20                 # m
R = D / 2.0
B = 2                    # palet sayisi, rotor basina
N_DISK = 8               # dort cift x iki rotor
T_HOVER_CIFT = 16.2      # N, cift basina
P_HOVER_CIFT = 335.0     # W, cift basina
V_SEYIR = 30.0           # m/s
S_REF = 1.979            # m2, referans kanat alani
MU = 1.81e-5

KESIT = "naca0012"       # ince simetrik; palet kesiti secilmis, olculmemis
N_SERIT = 24
r_h = 0.15 * R           # gobek


def serit():
    kenar = np.linspace(r_h, R, N_SERIT + 1)
    r = 0.5 * (kenar[:-1] + kenar[1:])
    dr = np.diff(kenar)
    return r, dr


def veter(r, c_kok):
    """Basit sivrilme: kokte c_kok, ucta yarisi."""
    x = (r - r_h) / (R - r_h)
    return c_kok * (1.0 - 0.5 * x)


def burulma(r, theta_uc, adim):
    """Ideal burulma: tan(theta) = adim / (2 pi r). theta_uc kalibre eder."""
    return np.arctan2(adim, 2 * math.pi * r) + theta_uc


def kesit_kuvvet(alfa_deg, Re):
    """NeuralFoil, dizi halinde."""
    o = nf.get_aero_from_airfoil(
        airfoil=__import__("aerosandbox").Airfoil(KESIT),
        alpha=alfa_deg, Re=Re, model_size="medium")
    return o["CL"], o["CD"]


def bemt(V, omega, c_kok, theta_uc, adim, tur=200):
    """Palet-eleman + momentum, MUTLAK indukleme hiziyla.

    NEDEN BOYLE. Ilk surum indukleme carpanlarini SERBEST AKISA gore
    tanimliyordu (Va = V(1+a)). O formulasyon hover'da yapisal olarak
    cokuyor: V -> 0 iken eksenel indukleme hic gelismiyor, ve palet
    hover'da 16,2 N yerine 1,5 N veriyordu -- yani kalibrasyon on kat
    sasiyordu ve bunu fark etmeden seyir sonucunu raporlayacaktim.
    Mutlak hizla yazilinca ayni denklem hem V = 0'da hem V = 30'da
    gecerli olur:

        dT = 4 pi rho r (V + v) v F dr
        dQ = 4 pi rho r^2 (V + v) w F dr
    """
    r, dr = serit()
    c = veter(r, c_kok)
    th = burulma(r, theta_uc, adim)
    v = np.full_like(r, 5.0)          # eksenel indukleme, m/s
    w = np.zeros_like(r)              # tegetsel indukleme, m/s
    for _ in range(tur):
        Va = V + v
        Vt = omega * r - w
        W = np.hypot(Va, Vt)
        phi = np.arctan2(Va, np.maximum(Vt, 1e-6))
        alfa = (th - phi) / D2R
        Re = np.clip(RHO * W * c / MU, 2e4, 2e6)
        cl, cd = kesit_kuvvet(alfa, Re)
        f = B / 2.0 * (R - r) / np.maximum(r * np.sin(phi), 1e-6)
        F = np.clip(2 / math.pi * np.arccos(np.clip(np.exp(-np.abs(f)), 0, 1)),
                    1e-3, 1.0)
        q = 0.5 * RHO * W ** 2 * c
        dT = B * q * (cl * np.cos(phi) - cd * np.sin(phi))      # birim uzunluk
        dQt = B * q * (cl * np.sin(phi) + cd * np.cos(phi))     # tegetsel kuvvet
        # momentum dengesi -> yeni indukleme
        with np.errstate(divide="ignore", invalid="ignore"):
            disk = 4 * math.pi * RHO * r * F
            kok = (V / 2.0) ** 2 + np.maximum(dT, 0.0) / disk
            v_yeni = -V / 2.0 + np.sqrt(np.maximum(kok, 0.0))
            w_yeni = dQt / np.maximum(2 * disk * (V + v), 1e-6)
        v_yeni = np.clip(np.nan_to_num(v_yeni), 0.0, 60.0)
        w_yeni = np.clip(np.nan_to_num(w_yeni), 0.0, 0.5 * omega * r + 1e-6)
        v += 0.25 * (v_yeni - v)
        w += 0.25 * (w_yeni - w)
    Va = V + v
    Vt = omega * r - w
    W = np.hypot(Va, Vt)
    phi = np.arctan2(Va, np.maximum(Vt, 1e-6))
    alfa = (th - phi) / D2R
    Re = np.clip(RHO * W * c / MU, 2e4, 2e6)
    cl, cd = kesit_kuvvet(alfa, Re)
    q = 0.5 * RHO * W ** 2 * c
    dT = B * q * (cl * np.cos(phi) - cd * np.sin(phi)) * dr
    dQ = B * q * (cl * np.sin(phi) + cd * np.cos(phi)) * r * dr
    return dT.sum(), dQ.sum(), alfa, Re


def hover_tasarla(cl_hedef=0.55, om=2100.0, T_hedef=8.1, tur=40):
    """Paleti ARAMAK yerine TASARLAR -- minimum induklenmis kayip mantigi.

    NEDEN BOYLE. Ilk surum 20 tasarimlik bir izgarayi her birinde 40 kez
    ikiye bolerek tariyordu: dort milyon kesit degerlendirmesi, saatlerce.
    Daha kotusu, izgara aramasi paleti bu gorev icin TASARLAMIYOR, yalnizca
    en az kotu adayi seciyor.

    Burada klasik yol: sabit devirde her serit, hedeflenen kesit c_l'sini
    verecek hucum acisina getirilir (burulma boyle cikar) ve veteri o
    seritin itki payini tasiyacak sekilde secilir. Cikan palet bu gorevin
    paletidir, bir aday degil.
    """
    r, dr = serit()
    v = np.full_like(r, 10.0)
    c = np.full_like(r, 0.015)
    th = np.zeros_like(r)
    for _ in range(tur):
        Vt = om * r
        W = np.hypot(v, Vt)
        phi = np.arctan2(v, Vt)
        Re = np.clip(RHO * W * c / MU, 2e4, 1e6)
        a_alt = np.full_like(r, -2.0)
        a_ust = np.full_like(r, 14.0)
        for _ in range(20):                 # hedef c_l -> alfa, ikiye bolme
            a_orta = 0.5 * (a_alt + a_ust)
            cl_o, _ = kesit_kuvvet(a_orta, Re)
            dusuk = cl_o < cl_hedef
            a_alt = np.where(dusuk, a_orta, a_alt)
            a_ust = np.where(dusuk, a_ust, a_orta)
        alfa = 0.5 * (a_alt + a_ust)
        th = phi + alfa * D2R
        cl, cd = kesit_kuvvet(alfa, Re)
        dTdr_hedef = T_hedef / (R - r_h)    # her serit esit disk yuklemesi
        pay = B * 0.5 * RHO * W ** 2 * (cl * np.cos(phi) - cd * np.sin(phi))
        # VETER SINIRLARI YARICAPA GORELI, MUTLAK DEGIL.
        #
        # Ilk surum bunu 0,004 - 0,040 m olarak MUTLAK yaziyordu. O
        # araliK 0,20 m'lik hafif rotor icin secilmisti (veter/R = 0,04
        # ile 0,40) ve orada dogru calisiyor. Ama ayni betik 0,67 m'lik
        # AGIR rotora uygulaninca ayni mutlak arali_ 335 mm yaricapta
        # 12 mm veter demek oluyor -- veter/R = 0,035, yani fiziksel
        # olarak sacma bir palet. Kirpma her iki ucta da BAGLIYORDU.
        #
        # Bunun sonucu masum degildi: agir rotorun dusuk dolgunlugu hem
        # serbest donme suruklemesini yapay olarak kucultuyor hem de
        # hover verim sayisini dusuruyordu. 3.8'in "agir hat FM 0,599'a
        # ulasamiyor" bulgusu ve 3.9'un "Fatura 2 olcekle kuculuyor"
        # sonucu ikisi de bu kirpmadan geliyordu.
        c_yeni = np.clip(dTdr_hedef / np.maximum(pay, 1e-6),
                         0.04 * R, 0.40 * R)
        c += 0.4 * (c_yeni - c)
        dT = pay * c
        v_yeni = np.clip(np.sqrt(np.maximum(dT / (4 * math.pi * RHO * r), 0.0)),
                         1.0, 40.0)
        v += 0.4 * (v_yeni - v)
    return c, th


def bemt_sabit(V, omega, c, th, tur=150):
    """Verilen veter/burulma dagilimiyla BEMT -- tasarlanmis palet icin."""
    r, dr = serit()
    v = np.full_like(r, 5.0)
    w = np.zeros_like(r)
    for _ in range(tur):
        Va, Vt = V + v, omega * r - w
        W = np.hypot(Va, Vt)
        phi = np.arctan2(Va, np.maximum(Vt, 1e-6))
        alfa = (th - phi) / D2R
        Re = np.clip(RHO * W * c / MU, 2e4, 2e6)
        cl, cd = kesit_kuvvet(alfa, Re)
        f = B / 2.0 * (R - r) / np.maximum(r * np.sin(phi), 1e-6)
        F = np.clip(2 / math.pi * np.arccos(np.clip(np.exp(-np.abs(f)), 0, 1)),
                    1e-3, 1.0)
        q = 0.5 * RHO * W ** 2 * c
        dT = B * q * (cl * np.cos(phi) - cd * np.sin(phi))
        dQt = B * q * (cl * np.sin(phi) + cd * np.cos(phi))
        disk = 4 * math.pi * RHO * r * F
        with np.errstate(divide="ignore", invalid="ignore"):
            v_yeni = -V / 2.0 + np.sqrt(np.maximum(
                (V / 2.0) ** 2 + np.maximum(dT, 0.0) / disk, 0.0))
            w_yeni = dQt / np.maximum(2 * disk * (V + v), 1e-6)
        v += 0.3 * (np.clip(np.nan_to_num(v_yeni), 0.0, 60.0) - v)
        w += 0.3 * (np.clip(np.nan_to_num(w_yeni), 0.0, 0.5 * omega * r) - w)
    Va, Vt = V + v, omega * r - w
    W = np.hypot(Va, Vt)
    phi = np.arctan2(Va, np.maximum(Vt, 1e-6))
    alfa = (th - phi) / D2R
    Re = np.clip(RHO * W * c / MU, 2e4, 2e6)
    cl, cd = kesit_kuvvet(alfa, Re)
    q = 0.5 * RHO * W ** 2 * c
    T = (B * q * (cl * np.cos(phi) - cd * np.sin(phi)) * dr).sum()
    Q = (B * q * (cl * np.sin(phi) + cd * np.cos(phi)) * r * dr).sum()
    return T, Q, alfa


def devir_itki_icin(c, th, T_hedef=8.1, V=1e-3):
    """Verilen palette T_hedef'i veren omega."""
    alt, ust = 300.0, 6000.0
    for _ in range(26):
        om = 0.5 * (alt + ust)
        if bemt_sabit(V, om, c, th)[0] < T_hedef:
            alt = om
        else:
            ust = om
    return 0.5 * (alt + ust)


def sifir_tork(c, th, V=V_SEYIR):
    """Net saft torkunun sifir oldugu omega ve oradaki eksenel kuvvet."""
    def Q(om):
        return bemt_sabit(V, om, c, th)[1]
    alt, ust = 100.0, 8000.0
    if Q(alt) * Q(ust) > 0:
        return None, None
    for _ in range(34):
        om = 0.5 * (alt + ust)
        if Q(alt) * Q(om) <= 0:
            ust = om
        else:
            alt = om
    om = 0.5 * (alt + ust)
    T, _, _ = bemt_sabit(V, om, c, th)
    return om, T


def sifir_tork_devri(c_kok, adim, V=V_SEYIR):
    """Net saft torkunun sifir oldugu omega; orada eksenel kuvvet."""
    alt, ust = 50.0, 6000.0
    Qa, _, _, _ = bemt(V, alt, c_kok, 0.0, adim)[1], 0, 0, 0
    def Q(om):
        return bemt(V, om, c_kok, 0.0, adim)[1]
    if Q(alt) * Q(ust) > 0:
        return None, None, None
    for _ in range(50):
        om = 0.5 * (alt + ust)
        if Q(alt) * Q(om) <= 0:
            ust = om
        else:
            alt = om
    om = 0.5 * (alt + ust)
    T, Qn, alfa, Re = bemt(V, om, c_kok, 0.0, adim)
    return om, T, (alfa, Re)


def dcd0(T_rotor):
    """Bir rotorun eksenel kuvveti -> sekiz diskin toplam dC_D0'i."""
    q = 0.5 * RHO * V_SEYIR ** 2
    return N_DISK * (-T_rotor) / (q * S_REF)


if __name__ == "__main__":
    print("UC PERVANESI, SEYIRDE SIFIR SAFT TORKU")
    print("D = %.2f m, %d palet, %d disk, V = %.0f m/s, S_ref = %.3f m2"
          % (D, B, N_DISK, V_SEYIR, S_REF))

    print("\n1. Paleti HOVER gorevi icin TASARLA (rotor basina 8,1 N)")
    print("-" * 66)
    print("%-12s %9s %9s %9s %9s %11s %9s"
          % ("hedef c_l", "om r/s", "rpm", "uc m/s", "T (N)", "cift W", "FM"))
    tasarimlar = []
    A_disk = math.pi * R ** 2
    for cl_h in (0.40, 0.55, 0.70, 0.85):
        c, th = hover_tasarla(cl_hedef=cl_h)
        om = devir_itki_icin(c, th)
        T, Q, _ = bemt_sabit(1e-3, om, c, th)
        P_cift = 2 * Q * om
        P_ideal = T ** 1.5 / math.sqrt(2 * RHO * A_disk)
        FM = 2 * P_ideal / P_cift if P_cift > 0 else 0.0
        print("%-12.2f %9.0f %9.0f %9.0f %9.2f %11.0f %9.3f"
              % (cl_h, om, om * 60 / 2 / math.pi, om * R, T, P_cift, FM))
        tasarimlar.append((cl_h, c, th, P_cift, FM))

    print("\nHedef: cift basina 16,2 N ve 335 W (3.7). Ideal guc 2 x %.0f W;"
          % (8.1 ** 1.5 / math.sqrt(2 * RHO * A_disk)))
    print("335 W bir FM = %.2f demek -- kucuk, dusuk Re'li bir pervane icin"
          % (2 * 8.1 ** 1.5 / math.sqrt(2 * RHO * A_disk) / 335.0))
    print("makul. Asagida 335 W'a en yakin tasarim kullaniliyor.")

    en = min(tasarimlar, key=lambda t: abs(t[3] - P_HOVER_CIFT))
    print("\nSecilen: hedef c_l = %.2f, cift gucu %.0f W (hedef 335), FM %.3f"
          % (en[0], en[3], en[4]))

    print("\n2. AYNI paleti seyirde kostur, net saft torku sifir olsun")
    print("-" * 66)
    print("%-14s %10s %10s %11s %13s" %
          ("hedef c_l", "om r/s", "rpm", "eksenel N", "dC_D0 (8 disk)"))
    sonuc = []
    for cl_h, c, th, P_cift, FM in tasarimlar:
        om, T = sifir_tork(c, th)
        if om is None:
            print("%-14.2f %10s %10s %11s %13s" % (cl_h, "-", "-", "kok yok", "-"))
            continue
        d = dcd0(T)
        sonuc.append((cl_h, d))
        print("%-14.2f %10.0f %10.0f %11.3f %13.5f"
              % (cl_h, om, om * 60 / 2 / math.pi, T, d))

    if sonuc:
        d = [x[1] for x in sonuc]
        print("\n3. Karar")
        print("-" * 66)
        print("hesaplanan aralik   dC_D0 = %.5f - %.5f" % (min(d), max(d)))
        print("3.3'un varsaydigi   dC_D0 = 0.00030 - 0.00080")
        print("uc cerceveleri      dC_D0 = 0.00430   <- kirilma esigi")
        print("varsayilan C_D0            0.02480")
        if max(d) >= 0.004:
            print("\n!! ESIK ASILDI -- 'Fatura 2 yok' iddiasi bu haliyle durmuyor.")
        elif max(d) > 0.0008:
            print("\nEsik asilmadi ama 3.3'un araligi ASILDI: varsayim iyimser.")
            print("Kirilma esigine %.1f kat pay var." % (0.004 / max(d)))
        else:
            print("\n3.3'un araligi dogrulandi.")
