# -*- coding: utf-8 -*-
"""DIKEY ITKI BUTCESI -- kurulu guc gercekten hangi T/W'yi satin aliyor?

NEDEN VAR. Makale iki yerde birbiriyle bagdasmayan sey soyluyordu:

  6.1  "Thrust equals weight and induced power follows from momentum
        theory" -- yani hover gucu T/W = 1,00 icin.
  6.2  "Hover power | 10,9 kW"
  S2   10,9 kW satirina "T/W 1,20" yaziyordu.
  7.4  "T/W = 1,2'de dikey ivme 0,2 g" -- ve 5 m/s tirmanis girisi
        makalenin "irtifa kaybi sifir" sonucunun dayanagi.

Ucu birden ayni anda dogru olamaz. Momentum kurami FM = 0,599 ve tek
1,20 m disk ile 490,5 N icin 10,9 kW veriyor; bu T/W = 1,00'dir. T/W =
1,2 icin 14,3 kW gerekir, ki kurulu degil.

BU BETIK bunu disaridan bir varsayimla kapatmiyor. Ucagin elinde olan
tek ek dikey itki kaynagini -- moment icin boyutlanmis UC CIFTLERINI --
sayiya dokuyor ve su takasi cikariyor: uc pervanelerinden ne kadar
dikey itki alirsan, yunuslama otoritesinden o kadar vazgeciyorsun.

Ayrica batarya tamponunu DUZELTIYOR. Onceki 4,61 kW/kg su cikarmayla
bulunmustu:

    (10,9 kW - 2,6 kW) / 1,8 kg

10,9 kW rotor MILINDE, 2,6 kW motor MILINDE, batarya ise ELEKTRIK
BARASINDA. Uc ayri istasyondaki uc sayi cikarilamaz. Asagisi zinciri
tek tek yurutuyor.

SINIR. Uc pervane itkisi (cift basina 16,2 N, 335 W) 6.2'den aliniyor
ve bu calismada olculmedi; S4 bunun FM = 0,702 ima ettigini ve hover
icin kullanilan 0,599'dan yuksek oldugunu zaten kaydediyor. Muhafazakar
hat da hesaplaniyor.
"""
import math

RHO, G = 1.225, 9.81

# --- 6.2 hafif referans tasarim -------------------------------------
M = 50.0                     # kg
W = M * G                    # N
D_BURUN = 1.20               # m, burun es eksenli cift
FM = 0.599                   # 6.1 / S6.2 kalibrasyonu
P_HOVER = 10.9e3             # W, 6.2 tablosu

# uc ciftleri (6.2 / 5.1)
T_UC = 16.2                  # N, cift basina
P_UC = 335.0                 # W, cift basina
N_CIFT = 4
KOL = 0.71                   # m, cerceve direk uzunlugu

# zincir (6.1)
ETA_MOTOR_YAKIT = 0.28
ETA_JENERATOR = 0.90
ETA_GE = 0.95                # guc elektronigi
ETA_MAKINE = 0.92
P_MOTOR_SAFT = 2.6e3         # W, 6.2 motor derecesi
M_TAMPON = 1.8               # kg


def disk(d):
    return math.pi * (d / 2.0) ** 2


def guc_iten(T, A, fm):
    """Momentum kurami + figure of merit -> mil gucu."""
    return T ** 1.5 / (fm * math.sqrt(2 * RHO * A))


def itki_gucten(P, A, fm):
    """Ters cozum: verilen mil gucu hangi itkiyi verir."""
    return (P * fm * math.sqrt(2 * RHO * A)) ** (2.0 / 3.0)


def basli(s):
    print("\n" + s)
    print("-" * len(s))


# ====================================================================
basli("1. Hover gucu gercekten hangi T/W'de?")

A = disk(D_BURUN)
print("burun disk alani            %.4f m2   (D = %.2f m)" % (A, D_BURUN))
print("disk yuklemesi              %.1f kg/m2  (6.2: 44,2)" % (M / A))
P1 = guc_iten(W, A, FM)
print("T/W = 1,00 icin mil gucu    %.0f W" % P1)
print("6.2'nin yazdigi hover gucu  %.0f W" % P_HOVER)
print("  -> fark %.1f %%" % (100 * (P_HOVER / P1 - 1)))
print()
print("10,9 kW hangi T/W'yi verir  %.3f" % (itki_gucten(P_HOVER, A, FM) / W))
print("T/W = 1,20 kac kW ister     %.2f kW" % (guc_iten(1.2 * W, A, FM) / 1e3))
print("10,9 kW ile T/W=1,2 icin FM %.3f  (hover icin kullanilan %.3f)"
      % (1.2 * W / (P_HOVER * math.sqrt(2 * RHO * A)) ** 0 * 0 +
         ((1.2 * W) ** 1.5 / (P_HOVER * math.sqrt(2 * RHO * A))), FM))
print()
print("SONUC: 10,9 kW = T/W 1,00. S2 tablosunun T/W sutunu ve 7.4'un")
print("T/W = 1,2 varsayimi kurulu gucle karsilanmiyor.")

# S2 tablosunun sutunu
basli("2. S2 tamponlu guc tablosu -- yazilan ve dogru")
print("%-12s %10s %10s %10s" % ("tampon kW/kg", "toplam kW", "yazilan", "dogru"))
for skg, Ptop, yazilan in ((0.735, 3.9, 0.61), (1.30, 4.9, 0.71),
                           (2.50, 7.1, 0.90), (4.61, 10.9, 1.20)):
    dogru = itki_gucten(Ptop * 1e3, A, FM) / W
    print("%-12.3f %10.1f %10.2f %10.3f" % (skg, Ptop, yazilan, dogru))
print("Yazilan sutun her satirda tam 1,2 kat sisik: T/W = 1,2 varsayilip")
print("gucle olceklenmis, oysa 10,9 kW zaten T/W = 1,00'in gucu.")

# ====================================================================
basli("3. Uc ciftleri: dikey itki ile yunuslama otoritesi arasindaki takas")

M_TAM = 2 * T_UC * KOL       # S4 / 4.3: M = 2TL
print("cift basina itki             %.1f N   @ %.0f W" % (T_UC, P_UC))
print("tam diferansiyel momenti     %.1f N.m  (S4: 23,0)" % M_TAM)
print()
print("Ust ciftler T_u, alt ciftler T_l; M = 2(T_u - T_l)L,")
print("dikey katki = 2T_u + 2T_l.  T_u = T_max tutulur.")
print()
print("%-18s %10s %10s %10s %10s" %
      ("korunan moment", "T_u (N)", "T_l (N)", "dikey (N)", "T/W"))
satirlar = []
for pay in (1.00, 0.75, 0.50, 0.25, 0.00):
    Mk = pay * M_TAM
    Tu = T_UC
    Tl = Tu - Mk / (2 * KOL)
    dik = 2 * Tu + 2 * Tl
    tw = (W + dik) / W
    satirlar.append((pay, Mk, dik, tw))
    print("%-18s %10.1f %10.1f %10.1f %10.3f"
          % ("%.0f %% (%.1f N.m)" % (100 * pay, Mk), Tu, Tl, dik, tw))
print()
print("ULASILABILIR ARALIK: T/W = %.3f (tam otorite) ... %.3f (otorite yok)"
      % (satirlar[0][3], satirlar[-1][3]))
print("7.4'un varsaydigi 1,200 hicbir ayarda ulasilmiyor.")

tw_tam = satirlar[0][3]
tw_sifir = satirlar[-1][3]

basli("4. Tirmanis: ulasilabilir T/W ne veriyor?")
print("%-10s %8s %10s %12s %10s" % ("T/W", "a (m/s2)", "a/g", "5 m/s'ye s", "irtifa m"))
for tw in (1.200, tw_sifir, tw_tam, 1.000):
    a = (tw - 1.0) * G
    if a <= 1e-9:
        print("%-10.3f %8.2f %10.3f %12s %10s" % (tw, a, 0.0, "hic", "-"))
        continue
    t5 = 5.0 / a
    print("%-10.3f %8.2f %10.3f %12.1f %10.1f"
          % (tw, a, a / G, t5, 0.5 * a * t5 ** 2))
print()
print("7.4 'T/W = 1,2'de 0,2 g, 5 m/s'ye 2,6 s'de, 6,4 m' diyor.")
print("Ulasilabilir en iyi hat: %.3f g, %.1f s, %.1f m."
      % ((tw_sifir - 1), 5.0 / ((tw_sifir - 1) * G),
         0.5 * (tw_sifir - 1) * G * (5.0 / ((tw_sifir - 1) * G)) ** 2))

# ====================================================================
basli("5. Batarya tamponu -- bara uzerinden, istasyonlar karistirilmadan")

print("Zincir: motor mili -> jenerator -> [BARA] -> guc elektronigi")
print("        -> elektrik makinesi -> pervane mili")
print()
jen = P_MOTOR_SAFT * ETA_JENERATOR
print("motor mili                  %6.2f kW" % (P_MOTOR_SAFT / 1e3))
print("jeneratorden baraya         %6.2f kW  (x%.2f)" % (jen / 1e3, ETA_JENERATOR))
print()

def bara_talebi(P_saft):
    """Pervane milinde P_saft icin barada gereken guc."""
    return P_saft / ETA_MAKINE / ETA_GE

for ad, P_saft in (("yalniz burun (T/W = 1,00)", P_HOVER),
                   ("burun + uclar tam (T/W = %.3f)" % tw_sifir,
                    P_HOVER + N_CIFT * P_UC),
                   ("burun + uclar, tam otorite korunur (T/W = %.3f)" % tw_tam,
                    P_HOVER + 2 * P_UC)):
    bara = bara_talebi(P_saft)
    tampon = bara - jen
    print("%-42s" % ad)
    print("   pervane mili %6.2f kW -> bara %6.2f kW -> tampon %6.2f kW"
          % (P_saft / 1e3, bara / 1e3, tampon / 1e3))
    print("   1,8 kg'da            %6.2f kW/kg" % (tampon / 1e3 / M_TAMPON))
    print()

print("Makalenin yazdigi           4,61 kW/kg  =  (10,9 - 2,6)/1,8")
print("  -> rotor mili ile motor mili cikarilip elektrik barasina bolunmus.")
print()

# olculmus ozgul guclere karsi gereken tampon kutlesi
basli("6. Olculmus ozgul guclerde gereken tampon kutlesi")
bara_hover = bara_talebi(P_HOVER)
tampon_hover = bara_hover - jen
bara_kalkis = bara_talebi(P_HOVER + N_CIFT * P_UC)
tampon_kalkis = bara_kalkis - jen
print("%-34s %14s %14s" % ("ozgul guc (kW/kg)", "hover 1,00", "kalkis %.3f" % tw_sifir))
for skg, etiket in ((0.724, "Yu vd. surekli, alt"),
                    (0.892, "Yu vd. surekli, ust"),
                    (1.50, "Yu vd. termal sinir"),
                    (4.61, "eski varsayim")):
    print("%-34s %11.2f kg %11.2f kg"
          % ("%.3f  %s" % (skg, etiket),
             tampon_hover / 1e3 / skg, tampon_kalkis / 1e3 / skg))
print()
print("6.2 butcesi 1,8 kg ayiriyor; S2 kurulusunda 2,2 kg pay var.")


# ====================================================================
basli("7. Agir referans tasarim -- ayni sorular")

M_A, D_A = 1000.0, 5.40
W_A = M_A * G
A_A = disk(D_A)
P_HOVER_A = 216.2e3
T_UC_A, KOL_A = 200.0, 2.37      # S4: 200 N/cift; kol 6.3 planformundan
D_UC_A = 0.67

print("disk alani                  %.3f m2, yukleme %.1f kg/m2" % (A_A, M_A / A_A))
P1A = guc_iten(W_A, A_A, FM)
print("T/W = 1,00 icin             %.1f kW   (6.3 yaziyor %.1f kW)"
      % (P1A / 1e3, P_HOVER_A / 1e3))
print("216,2 kW hangi T/W'yi verir %.3f" % (itki_gucten(P_HOVER_A, A_A, FM) / W_A))
print()
A_UC_A = disk(D_UC_A)
P_UC_A = guc_iten(T_UC_A, A_UC_A, FM)
print("uc cift %.0f N -> %.2f kW/cift (FM %.3f), dort cift %.1f kW = hover'in %% %.1f"
      % (T_UC_A, P_UC_A / 1e3, FM, 4 * P_UC_A / 1e3, 100 * 4 * P_UC_A / P_HOVER_A))
print()
print("%-22s %12s %10s" % ("korunan moment", "dikey (N)", "T/W"))
for pay in (1.00, 0.00):
    Tl = T_UC_A - pay * (2 * T_UC_A * KOL_A) / (2 * KOL_A)
    dik = 2 * T_UC_A + 2 * Tl
    print("%-22s %12.0f %10.3f" % ("%.0f %%" % (100 * pay), dik, (W_A + dik) / W_A))
