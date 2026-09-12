# -*- coding: utf-8 -*-
"""YATIS EKSENI -- sonumleme, otorite ve ac-kapa davranisi.

NEDEN VAR. Bir dis degerlendirme (YZ3, 9. tur) sunu soyledi ve haklidir:
makalenin EN ZAYIF TASIYICI iddiasi denge degil, YATIS. Cunku

  - yunuslama ve sapma uc pervanelerden geliyor,
  - yatis YALNIZCA alt yuzeydeki seritten geliyor,
  - "hic kumanda yuzeyi olmadan tam kontrol" iddiasinin tamami buna
    dayaniyor,

ve §4.4'un sayilari (46 N m, 20-25 derece/s) su ana kadar "mertebe
tahmini" etiketiyle duruyordu: sonumleme ve kumanda etkinligi
katsayilari LITERATURDEN aliniyordu, bu geometri icin HESAPLANMIYORDU.

BU MODUL uc seyi yapar ve dorduncusunu yapmaz:

  1. I_xx'i kutle butcesinden hesaplar (yunuslama icin I_yy zaten
     hesaplanmisti; yatis ekseni hic bakilmamisti).
  2. YATIS SONUMLEMESINI bu planform icin girdap-kafesle hesaplar --
     literaturden almaz. Yontem: kanada helis acisi kadar burulma
     verilir, theta(y) = -atan(p y / V), ve dogan yatis momenti
     olculur. Sonuc p'de dogrusaldir ve yakinsamistir.
  3. Ac-kapa (bang-bang) serit icin kapali cevrim davranisini benzetir:
     birinci mertebe yatis dinamigi + olu bant -> sinir cevrimi.

  4. YAPMADIGI: seridin kendi kuvvet katsayisini hesaplamak. O, ayrilmis
     akista bir cihaz katsayisidir; girdap kafes veremez, ve RANS ile de
     ancak guclukle verilir. Bunun yerine SORU TERSINE CEVRILIR: 20-25
     derece/s icin GEREKEN kuvvet hesaplanir ve makul cihaz katsayisi
     araligiyla KARSILASTIRILIR. Denge icin yapilan sey neyse (gereksinim
     nicelenir, kapanis iddia edilmez) burada da odur.

EKSEN. Kanat duzleminde x veter, y aciklik, z kalinlik. Seyirde govde x
ekseni ucus dogrultusundadir; yatis o eksen etrafindadir, yani I_xx =
toplam m (y^2 + z^2) gerekir.
"""
import sys, os, math
import numpy as np
import aerosandbox as asb

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from planform import istasyonlar, olcuier, P
import donme

RHO, G = 1.225, 9.81

# --- hafif referans tasarim, 6.3 -------------------------------------
MTOW, S_REF, V_SEYIR = 50.0, 1.9785, 30.0
T_ITKI_HOVER = MTOW * G          # asili durumda itki = agirlik
D_PERVANE = 1.20                 # ana pervane capi, 6.3

# --- serit geometrisi, 4.4 -------------------------------------------
SERIT_UZUNLUK = 1.20 * P["kokVeter"]      # kok veterinin %120'si
SERIT_H_IC, SERIT_H_DIS = 0.02, 0.06      # ic ve dis uctaki yukseklik
SERIT_ACI = 45.0                          # PLANFORMDA ok acisi (mkfig08)
# ⚠️ Ilk surumde bu aci "yuzeye gore egim" saniliyordu ve sin(45) ile
# carpiliyordu. Sekil 8'in uretimi (gorsel/uretim/mkfig08.py) seridi
# sx = u L, sz = zA0 + u L diye kuruyor: yani serit planformda 45
# derecelik bir KOSEGEN, alt yuzeye dik duran bir citten ibaret.
# Akisa gore oklu bir cit icin normal kuvvet cos^2(ok) ile olceklenir.
SERIT_IC_ORAN = 0.46                      # boyunun %46'si slipstream icinde
M_PAPER = 46.0                            # 4.4'un verdigi yatis momenti


# ---------------------------------------------------------------------
# 1. I_xx
# ---------------------------------------------------------------------
def atalet_x(olcek=1.0):
    """Yatis ekseni atalet momenti, kutle butcesinin dagilimindan.

    donme.dagilim() iki yari kanadi tek girdi olarak +y'de topluyor;
    I_xx'e y^2 girdiginden bu dogrudur (±y ayni y^2). Uc motorlari da
    ±z'de simetriktir, z^2 ayni.
    """
    kal = donme.dagilim(olcek=olcek)
    M = sum(k[0] for k in kal)
    Ixx = sum(m * (y * y + z * z) for m, x, y, z, I0 in kal)
    return M, Ixx


# ---------------------------------------------------------------------
# 2. YATIS SONUMLEMESI -- bu geometri icin hesaplanir
# ---------------------------------------------------------------------
def _tam_kanat(p, V, kesit=10, n=200):
    """Helis acisi kadar burulmus TAM kanat (simetrik bayragi kapali).

    Yatan bir kanatta y istasyonu p*y kadar dusey hiz gorur; yerel hucum
    acisi atan(p y / V) kadar degisir. Kalici yatis, bu burulmanin
    dogurdugu momenttir.
    """
    ist, yari, _ = istasyonlar(n=n)
    idx = np.linspace(0, len(ist) - 1, kesit).astype(int)
    xs = []
    for i in list(reversed(idx[1:])) + list(idx):
        y, x, c, tc, _ = ist[i]
        yy = -y if i in idx[1:] and len(xs) < kesit - 1 else y
        xs.append((yy, x, c, tc))
    # yukaridaki kosul kirilgan; acikca kur:
    xs = []
    for i in reversed(idx[1:]):
        y, x, c, tc, _ = ist[i]
        xs.append((-y, x, c, tc))
    for i in idx:
        y, x, c, tc, _ = ist[i]
        xs.append((y, x, c, tc))
    kesitler = []
    for y, x, c, tc in xs:
        tw = -math.degrees(math.atan(p * y / V))
        kesitler.append(asb.WingXSec(
            xyz_le=[x, y, 0.0], chord=c, twist=tw,
            airfoil=asb.Airfoil("naca00%02d" % int(round(tc * 100)))))
    return asb.Wing(name="govde", symmetric=False, xsecs=kesitler)


def sonumleme(p=0.20, V=30.0, alfa=4.0, kesit=10, sr=6, cr=8):
    """|C_l_p| -- yatis sonumleme katsayisinin buyuklugu."""
    o = olcuier()
    ac = asb.Airplane(wings=[_tam_kanat(p, V, kesit)], s_ref=o["alan"],
                      b_ref=o["aciklik"], c_ref=o["alan"] / o["aciklik"])
    r = asb.VortexLatticeMethod(
        airplane=ac, op_point=asb.OperatingPoint(velocity=V, alpha=alfa),
        spanwise_resolution=sr, chordwise_resolution=cr).run()
    phat = p * o["aciklik"] / (2 * V)
    return abs(float(r["Cl"])) / phat, o


# ---------------------------------------------------------------------
# 3. DENGE YATIS HIZI ve ZAMAN SABITI
# ---------------------------------------------------------------------
def sonum_egimi(Clp, V, o, rho=RHO):
    """dL/dp  [N m / (rad/s)] -- sonumleme momentinin hiza gore egimi."""
    q = 0.5 * rho * V * V
    b = o["aciklik"]
    return Clp * q * o["alan"] * b * b / (2 * V)


def denge_hizi(M_kumanda, V, o, Clp):
    return M_kumanda / sonum_egimi(Clp, V, o)


# ---------------------------------------------------------------------
# 4. SERIT: GEREKEN kuvvet (kapanis degil, gereksinim)
# ---------------------------------------------------------------------
def serit_kolu(n=400):
    """Seridin agirlikli moment kolu ve alani.

    Serit kokten disa dogru uzanir; yuksekligi ic uctan dis uca dogrusal
    artar. Etkin kol = integral(y h dy) / integral(h dy).
    """
    ys = np.linspace(0.0, SERIT_UZUNLUK, n)
    h = SERIT_H_IC + (SERIT_H_DIS - SERIT_H_IC) * ys / SERIT_UZUNLUK
    A = np.trapezoid(h, ys) if hasattr(np, "trapezoid") else np.trapz(h, ys)
    My = (np.trapezoid(ys * h, ys) if hasattr(np, "trapezoid")
          else np.trapz(ys * h, ys))
    return My / A, A, ys, h


def kanat_serit_alani(y0=0.0, y1=None, n=400):
    """Seridin acikligindaki YARI kanat alani ve alan merkezi.

    Ikinci mekanizma icin gerekir: serit kendi surtunmesiyle degil,
    bulundugu yari kanadin DOLASIMINI degistirerek de moment uretebilir
    (Gurney / spoiler etkisi). O durumda etkiyen alan seridin kendi
    alani degil, KANADIN alanidir -- iki mertebe buyuk.
    """
    y1 = SERIT_UZUNLUK if y1 is None else y1
    ist, yari, _ = istasyonlar(n=n)
    A = My = 0.0
    for a, b in zip(ist[:-1], ist[1:]):
        y = 0.5 * (a[0] + b[0])
        if y0 <= y <= y1:
            dA = 0.5 * (a[2] + b[2]) * (b[0] - a[0])
            A += dA
            My += dA * y
    return A, (My / A if A else 0.0)


_VETER_TABLO = {}


def _veter_tablo(n=400):
    """Planform bir kez kurulur; yerel_veter cagri basina kurmaz."""
    if n not in _VETER_TABLO:
        ist, _, _ = istasyonlar(n=n)
        _VETER_TABLO[n] = (np.array([a[0] for a in ist]),
                           np.array([a[2] for a in ist]))
    return _VETER_TABLO[n]


def yerel_veter(y, n=400):
    """Aciklik istasyonu y'deki yerel veter (dogrusal ara deger)."""
    ys, cs = _veter_tablo(n)
    return float(np.interp(y, ys, cs))


# ---------------------------------------------------------------------
# 4b. OLU BANT: NACA ACR L4H19'un olctugu h/c esigi
# ---------------------------------------------------------------------
# "spoiler projections of less than 0.01c produce negligible changes in
# lift" -- NACA ACR No. L4H19 (1944), iki ayri model uzerinde.
#
# Bizim serit surekli degiskendir (kullanicinin duzeltmesi: ac-kapa
# DEGIL). O halde bu esik, kumanda kursunun ALTINDAN bir olu bant
# keser. Ve serit konik oldugu icin esik her istasyonda ayni f'te
# asilmaz: dista yukseklik buyuk, veter kucuk, yani DIS UC ONCE calisir.
ESIK_HC = 0.01


def esik_istasyonu(f, n=400):
    """Kumanda kesri f'te seridin hangi noktasindan itibaren etkin oldugu.

    f = 0 tam kapali, f = 1 tam acik (yukseklikler 4.4'teki degerler).
    Doner: (y_esik, etkin_uzunluk_orani). y_esik = 0 ise serit tumuyle
    etkin; y_esik > SERIT_UZUNLUK ise hicbir yeri etkin degil.
    """
    ys = np.linspace(0.0, SERIT_UZUNLUK, n)
    h = f * (SERIT_H_IC + (SERIT_H_DIS - SERIT_H_IC) * ys / SERIT_UZUNLUK)
    c = np.interp(ys, *_veter_tablo())
    etkin = h / c >= ESIK_HC
    if not etkin.any():
        return float("inf"), 0.0
    i = int(np.argmax(etkin))          # ilk etkin istasyon
    return float(ys[i]), float(etkin.sum()) / n


def esik_kolu(f, n=400):
    """Yalnizca esigi asan kismin agirlikli kolu ve alani."""
    ys = np.linspace(0.0, SERIT_UZUNLUK, n)
    h = f * (SERIT_H_IC + (SERIT_H_DIS - SERIT_H_IC) * ys / SERIT_UZUNLUK)
    c = np.interp(ys, *_veter_tablo())
    m = (h / c) >= ESIK_HC
    if not m.any():
        return 0.0, 0.0
    tr = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    A = tr(h[m], ys[m])
    if A <= 0:
        return 0.0, 0.0
    return tr(ys[m] * h[m], ys[m]) / A, A


def gereken_katsayi(M_hedef, q, kol, A):
    """Hedef momenti veren normal kuvvet katsayisi.

    M = C_N q A_dik kol,  A_dik = A sin(45 derece)
    """
    A_dik = A * math.cos(math.radians(SERIT_ACI)) ** 2
    return M_hedef / (q * A_dik * kol)


# ---------------------------------------------------------------------
# 5. AC-KAPA (bang-bang) SINIR CEVRIMI
# ---------------------------------------------------------------------
def acKapa(M_kumanda, Ixx, egim, olu_bant=2.0, gecikme=0.05,
           t_son=6.0, dt=0.001, phi0=10.0):
    """Olu bantli ac-kapa yatis kontrolu; birinci mertebe dinamik.

        Ixx * pdot = ±M_kumanda - egim * p

    Serit ac-kapa oldugundan kumanda momenti UC DEGERLIDIR: sol, sifir,
    sag. Olu bant icinde kapali. Gecikme, eyleyicinin acilma suresidir.
    """
    phi, p, t = math.radians(phi0), 0.0, 0.0
    u, u_hedef, t_gec = 0.0, 0.0, -1.0
    iz = []
    ob = math.radians(olu_bant)
    while t < t_son:
        if phi > ob:
            yeni = -1.0
        elif phi < -ob:
            yeni = +1.0
        else:
            yeni = 0.0
        if yeni != u_hedef:
            u_hedef, t_gec = yeni, t + gecikme
        if t_gec >= 0 and t >= t_gec:
            u = u_hedef
        pdot = (u * M_kumanda - egim * p) / Ixx
        p += pdot * dt
        phi += p * dt
        t += dt
        iz.append((t, math.degrees(phi), math.degrees(p), u))
    return iz


if __name__ == "__main__":
    o = olcuier()
    b, S = o["aciklik"], o["alan"]
    print("=" * 74)
    print("YATIS EKSENI -- sonumleme, otorite, ac-kapa")
    print("=" * 74)

    M, Ixx = atalet_x()
    print("kutle %.1f kg, I_xx = %.3f kg m2 (jirasyon %.3f m, yari-aciklik %.3f m)"
          % (M, Ixx, math.sqrt(Ixx / M), o["yari"]))
    print("karsilastirma: I_yy = 9.813 kg m2 -- yatis ataleti 2.5 kat buyuk,")
    print("cunku kutle veterce degil ACIKLIKCA yayili.")
    print()

    print("-" * 74)
    print("YATIS SONUMLEMESI -- literaturden degil, bu planformdan")
    print("-" * 74)
    Clp, _ = sonumleme()
    print("  |C_l_p| = %.4f" % Clp)
    print("  dogrusallik ve yakinsama:")
    for pp in (0.10, 0.20, 0.40):
        c, _ = sonumleme(p=pp)
        print("     p = %.2f rad/s  ->  |C_l_p| = %.4f" % (pp, c))
    for kesit, sr, cr in ((8, 4, 6), (10, 6, 8), (14, 8, 10)):
        c, _ = sonumleme(kesit=kesit, sr=sr, cr=cr)
        print("     %2d kesit / sr %d / cr %2d  ->  |C_l_p| = %.4f"
              % (kesit, sr, cr, c))
    print()

    egim = sonum_egimi(Clp, V_SEYIR, o)
    print("-" * 74)
    print("SEYIRDE (%g m/s) OTORITE" % V_SEYIR)
    print("-" * 74)
    print("  sonumleme egimi dL/dp = %.2f N m / (rad/s)" % egim)
    p_ss = denge_hizi(M_PAPER, V_SEYIR, o, Clp)
    print("  4.4'un 46 N m'si -> denge yatis hizi %.1f derece/s"
          % math.degrees(p_ss))
    print("  4.4 metinde 20-25 derece/s diyor: HESAPLANAN SONUMLEME ILE")
    print("  metnin sayisi TEMKINLI tarafta kaliyor (%.0f%% pay)."
          % (100 * (math.degrees(p_ss) / 22.5 - 1)))
    tau = Ixx / egim
    print("  zaman sabiti tau = I_xx/(dL/dp) = %.3f s" % tau)
    t30 = 30.0 / math.degrees(p_ss) + tau
    print("  30 derece yatisa yaklasik %.2f s (4.4: 1,2-1,5 s)" % t30)
    print()
    for hedef in (20.0, 25.0):
        M_ger = math.radians(hedef) * egim
        print("  %g derece/s icin GEREKEN moment: %.1f N m  (4.4'un 46'si %.2f kat)"
              % (hedef, M_ger, M_PAPER / M_ger))
    print()

    print("-" * 74)
    print("SERIT: GEREKEN KATSAYI (kapanis degil, gereksinim)")
    print("-" * 74)
    kol, A, _, _ = serit_kolu()
    q = 0.5 * RHO * V_SEYIR ** 2
    print("  serit boyu %.3f m, alan %.4f m2, etkin kol %.3f m (yari-acikligin %%%.0f'i)"
          % (SERIT_UZUNLUK, A, kol, 100 * kol / o["yari"]))
    for hedef, ad in ((math.degrees(p_ss), "4.4'un 46 N m'si"),
                      (25.0, "25 derece/s"), (20.0, "20 derece/s")):
        M_ger = math.radians(hedef) * egim
        CN = gereken_katsayi(M_ger, q, kol, A)
        print("  %-18s -> M %5.1f N m -> GEREKEN C_N = %.2f" % (ad, M_ger, CN))
    print()
    print()
    print("  Akisa dik duz levha C_D ~ 1,1-1,3. GEREKEN deger 3-5 bandinda,")
    print("  yani SERIDIN KENDI SURUKLEMESI BU MOMENTI VEREMEZ -- dort kat")
    print("  eksik kaliyor. Demek ki moment baska bir mekanizmadan gelmeli.")
    print()
    print("  MEKANIZMA 1 -- seridin kendi kuvveti (ust sinir, C_N = 1,3):")
    M1 = 1.3 * q * A * math.cos(math.radians(SERIT_ACI)) ** 2 * kol
    print("     M = %.1f N m  ->  denge yatis hizi %.1f derece/s"
          % (M1, math.degrees(denge_hizi(M1, V_SEYIR, o, Clp))))
    print()
    print("  MEKANIZMA 2 -- yari kanadin DOLASIMINI degistirmesi")
    print("  (Gurney/spoiler etkisi; etkiyen alan seridin degil KANADIN alani):")
    A_k, kol_k = kanat_serit_alani()
    print("     serit acikligindaki yari kanat alani %.4f m2, alan merkezi y = %.3f m"
          % (A_k, kol_k))
    for dCL in (0.10, 0.15, 0.20, 0.30):
        M2 = dCL * q * A_k * kol_k
        print("     dC_L = %.2f -> M = %5.1f N m -> %.1f derece/s"
              % (dCL, M2, math.degrees(denge_hizi(M2, V_SEYIR, o, Clp))))
    print()
    print("  BULGU. Iki mekanizma momenti yaklasik DORT KAT ayri yerlere")
    print("  koyuyor. 4.4'un 46 N m'si birincisiyle ulasilamaz, ikincisiyle")
    print("  dC_L ~ 0,20 demektir. Metin hangi mekanizmayi kastettigini")
    print("  SOYLEMIYOR, ve sayi buradan geliyor gibi duruyor ama")
    print("  TURETILMIS degil. 20 derece/s icin gereken dC_L ~ %.2f'dir;"
          % (math.radians(20.0) * egim / (q * A_k * kol_k)))
    print("  %1-2 veter Gurney seritleri tipik olarak dC_L 0,1-0,3 verir,")
    print("  yani gereksinim MAKUL ama GOSTERILMIS DEGILDIR.")
    print()

    print("-" * 74)
    print("ASILI DURUMDA (V = 0) -- slipstream")
    print("-" * 74)
    A_disk = math.pi * (D_PERVANE / 2) ** 2
    q_slip = T_ITKI_HOVER / A_disk
    print("  q_slipstream = T/A = %.1f N/m2 (%.1f m/s serbest akisin esdegeri)"
          % (q_slip, math.sqrt(2 * q_slip / RHO)))
    ys = np.linspace(0.0, SERIT_UZUNLUK * SERIT_IC_ORAN, 200)
    h = SERIT_H_IC + (SERIT_H_DIS - SERIT_H_IC) * ys / SERIT_UZUNLUK
    tr = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    A_ic, My_ic = tr(h, ys), tr(ys * h, ys)
    kol_ic = My_ic / A_ic
    print("  MEKANIZMA 1 -- seridin kendi kuvveti:")
    for CN in (0.6, 1.0, 1.4):
        M_ic = CN * q_slip * A_ic * math.cos(math.radians(SERIT_ACI)) ** 2 * kol_ic
        alpha_x = M_ic / Ixx
        print("     C_N = %.1f -> M = %5.2f N m -> %5.1f derece/s2,"
              " 30 dereceye %.2f s"
              % (CN, M_ic, math.degrees(alpha_x),
                 math.sqrt(2 * math.radians(30) / alpha_x)))
    A_ks, kol_ks = kanat_serit_alani(0.0, 0.60)
    print("  MEKANIZMA 2 -- iz icindeki yari kanadin dolasimi")
    print("     iz icindeki yari kanat alani %.4f m2, alan merkezi y = %.3f m"
          % (A_ks, kol_ks))
    for dCL in (0.10, 0.15, 0.20):
        M_ic = dCL * q_slip * A_ks * kol_ks
        alpha_x = M_ic / Ixx
        print("     dC_L = %.2f -> M = %5.2f N m -> %5.1f derece/s2,"
              " 30 dereceye %.2f s"
              % (dCL, M_ic, math.degrees(alpha_x),
                 math.sqrt(2 * math.radians(30) / alpha_x)))
    print("  V = 0'da AERODINAMIK SONUMLEME YOK: hareket saf ataletsel,")
    print("  yani asili durumda serit kapatilmazsa yatis hizi SURESIZ artar.")
    print("  Bu, ac-kapa kontrolunu seyirdekinden daha kritik yapar.")
    print()

    print("-" * 74)
    print("OLU BANT -- NACA ACR L4H19'un h/c = %0.2f esigi" % ESIK_HC)
    print("-" * 74)
    kol0, A0 = esik_kolu(1.0)
    print("  1944 Langley olcumu: 0,01 veterden alcak spoiler cikintilari")
    print("  tasimada 'negligible' degisiklik veriyor (iki ayri model).")
    print("  Serit SUREKLI degisken oldugu icin bu esik kumanda kursunun")
    print("  ALTINDAN bir olu bant keser. Serit konik: dis uc once calisir.")
    print()
    print("  %6s %9s %8s %8s %9s %9s" %
          ("f", "y_esik", "etkin%", "kol(m)", "M/M_tam", "dogrusal"))
    for f in (0.05, 0.075, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 1.0):
        ye, orn = esik_istasyonu(f)
        kol, A = esik_kolu(f)
        print("  %6.3f %9s %8.1f %8.3f %9.3f %9.3f"
              % (f, ("%.3f" % ye) if ye != float("inf") else "yok",
                 100 * orn, kol, (A * kol) / (A0 * kol0), f))
    print()
    print("  Okunusu: esik gorundugunden UCUZA geliyor. Esigi asan kisim")
    print("  seridin EN UZUN KOLLU kismi oldugu icin, kaybedilen alanin")
    print("  buyuk bolumu buyuyen kolla geri geliyor. Kursun dortte birinin")
    print("  ustunde tepki %5 icinde DOGRUSAL; %15'in altinda momentin")
    print("  dortte birinden fazlasi kayip; %7'nin altinda serit HICBIR SEY")
    print("  yapmiyor. Yani surekli kumanda sifirdan baslamiyor.")
    print()

    print("-" * 74)
    print("AC-KAPA SINIR CEVRIMI -- seyir")
    print("-" * 74)
    for ob, gec in ((2.0, 0.05), (2.0, 0.15), (5.0, 0.05)):
        iz = acKapa(M_PAPER, Ixx, egim, olu_bant=ob, gecikme=gec)
        son = [k for k in iz if k[0] > 3.0]
        phi = [k[1] for k in son]
        print("  olu bant %.0f derece, eyleyici gecikmesi %.0f ms:"
              "  sinir cevrimi %+.2f / %+.2f derece (genlik %.2f)"
              % (ob, 1000 * gec, min(phi), max(phi), (max(phi) - min(phi)) / 2))
    print()
    print("  Bu bir KONTROL TASARIMI DEGILDIR: olu bant ve gecikme secilmis")
    print("  degerlerdir, olculmus degil. Gosterdigi sey su: birinci mertebe")
    print("  yatis dinamiginde ac-kapa bir serit, makul olu bant ve gecikmeyle")
    print("  SINIRLI genlikte bir sinir cevrimi verir -- yani ac-kapa olmasi")
    print("  tek basina kontrolu imkansiz kilmaz. Kapali cevrim kararliligi")
    print("  ayri bir calismadir.")
