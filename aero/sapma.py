# -*- coding: utf-8 -*-
"""SAPMA EKSENI -- atalet, otorite, yon kararliligi ve sonumleme.

NEDEN VAR. Yatis denetimi (yatis.py) bakilmamis bir eksende tasiyici bir
sayinin cokmesiyle sonuclandi. Uc dis degerlendirmenin UCU birden ayni
seyi soyledi: dondurmadan once SAPMA eksenine de bakin, cunku o da hic
incelenmedi.

Bu modul yatis.py ile ayni disiplini uygular: hesaplanabilen hesaplanir,
hesaplanamayan GEREKSINIM olarak yazilir, ve hicbir yerde "otorite
gosterildi" denmez.

EKSENLER. x veter, y aciklik, z kalinlik. Uc cerceveleri z boyunca
±0,71 m uzaniyor; uc pervane ciftleri bu cercevelerin uclarinda.

  YUNUSLAMA (y ekseni): ust/alt cift farki -> kol = cerceve boyu 0,71 m
  SAPMA    (z ekseni): sag/sol cift farki  -> kol = YARI ACIKLIK 1,726 m

Yani sapmanin kolu yunuslamanin 2,43 KATI. Bu, uc pervane duzeninin
kendiliginden gelen bir ozelligi ve makalede hic soylenmemis.
"""
import sys, os, math
import numpy as np
import aerosandbox as asb

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from planform import istasyonlar, olcuier, P
from vlm import kanat_kur, SPAN_COZ, VETER_COZ
import donme

RHO = 1.225
V_SEYIR = 30.0
CD0_KESIT = 0.010          # kesit profil surukleme katsayisi, sonumleme icin
T_CIFT, T_CIFT_TEMKINLI = 16.2, 12.4

# Yon kararliligi hedefleri. Ilk ikisi bu calismanin kendi sectigi
# degerlerdi; son ikisi OLCUTTUR -- NACA ACR L4H19 (1944) s. 18.
D2R_ = math.pi / 180.0
HEDEFLER = (
    (0.03, "bu calismanin sectigi alt deger"),
    (0.05, "bu calismanin sectigi ust deger"),
    (0.001 / D2R_ / 3, "L4H19: serbest-ucus tunelinde ucurulan en dusuk"),
    (0.001 / D2R_, "L4H19: geleneksel ucaklar icin ONERILEN"),
)


def atalet_z():
    kal = donme.dagilim()
    M = sum(k[0] for k in kal)
    xg = sum(k[0] * k[1] for k in kal) / M
    Izz = sum(m * ((x - xg) ** 2 + y * y) for m, x, y, z, I0 in kal)
    return M, xg, Izz


def mevcut_sapma(T=T_CIFT):
    """Itki TERS DONEMEZ: en buyuk fark bir yandaki iki cift tam,
    otekiler sifir -> M = 2 T (yari aciklik)."""
    o = olcuier()
    return 2 * T * o["yari"], o["yari"]


def yon_kararliligi(betalar=(0.0, 2.0, 5.0), alfa=4.0, hiz=30.0, x_cg=0.7777):
    """C_n_beta ve C_l_beta. UYARI: yalniz planform; uc cerceveleri
    modelde YOK, ve seyirde onlar DUSEY YUZEYLERDIR."""
    o = olcuier()
    cik = []
    for be in betalar:
        ac = asb.Airplane(wings=[kanat_kur()], s_ref=o["alan"],
                          b_ref=o["aciklik"], c_ref=0.6514,
                          xyz_ref=[x_cg, 0.0, 0.0])
        r = asb.VortexLatticeMethod(
            airplane=ac,
            op_point=asb.OperatingPoint(velocity=hiz, alpha=alfa, beta=be),
            spanwise_resolution=SPAN_COZ, chordwise_resolution=VETER_COZ).run()
        cik.append((be, float(r["Cn"]), float(r["Cl"]), float(r["CY"])))
    return o, cik


def sonumleme_n(cd=CD0_KESIT, n=400):
    """C_n_r'nin profil-surukleme payi -- serit kuramiyla.

        N = -rho V r cd integral(y^2 c dy)  ->  C_n_r = -4 cd Ic/(S b^2)

    SINIR: yalnizca profil suruklemesi. Induklenen surukleme ve dusey
    yuzeylerin payi yok; ikisi de daha cok sonumler -> ALT SINIR."""
    ist, yari, _ = istasyonlar(n=n)
    o = olcuier()
    Ic = 0.0
    for a, b in zip(ist[:-1], ist[1:]):
        y = 0.5 * (a[0] + b[0])
        c = 0.5 * (a[2] + b[2])
        Ic += 2 * y * y * c * (b[0] - a[0])
    S, bb = o["alan"], o["aciklik"]
    return -4 * cd * Ic / (S * bb * bb), Ic, o


def gereken_yanal_alan(Cnb_hedef, kol, a_f, o):
    """C_n_beta = a_f S_f l_f / (S b)  ->  S_f"""
    return Cnb_hedef * o["alan"] * o["aciklik"] / (a_f * kol)


if __name__ == "__main__":
    print("=" * 74)
    print("SAPMA EKSENI")
    print("=" * 74)
    M, xg, Izz = atalet_z()
    o = olcuier()
    print("kutle %.1f kg, CG x = %.4f m" % (M, xg))
    print("I_zz = %.3f kg m2  (I_xx 25,010 + I_yy 9,813 = %.3f; ucak"
          % (Izz, 25.010 + 9.813))
    print("  neredeyse duzlemsel oldugu icin ikisi birbirine yakin)")
    print()

    print("-" * 74)
    print("MEVCUT SAPMA MOMENTI -- kolu yunuslamanınkinin 2,43 kati")
    print("-" * 74)
    for T, ad in ((T_CIFT, "makalenin 16,2 N'u"),
                  (T_CIFT_TEMKINLI, "temkinli 12,4 N")):
        Mz, kol = mevcut_sapma(T)
        print("  %-20s -> M_z = 2 T x %.3f m = %5.1f N m  (yunuslama %.1f N m)"
              % (ad, kol, Mz, 2 * T * 0.71))
    print("  Sapma, uc pervane duzeninin EN GUCLU eksenidir -- duzenin")
    print("  kendiliginden gelen bir ozelligi, makalede hic soylenmemis.")
    print()

    print("-" * 74)
    print("YON KARARLILIGI -- girdap kafes, YALNIZ PLANFORM")
    print("-" * 74)
    o, cik = yon_kararliligi()
    print("  %6s %12s %12s %12s" % ("beta", "C_n", "C_l", "C_Y"))
    for be, Cn, Cl, CY in cik:
        print("  %6.1f %12.6f %12.6f %12.6f" % (be, Cn, Cl, CY))
    be, Cn, Cl, CY = cik[-1]
    print()
    print("  C_n_beta = %+.5f /rad    C_l_beta = %+.5f /rad"
          % (Cn / math.radians(be), Cl / math.radians(be)))
    print()
    print("  BULGU. Planform yon kararliligini SIFIR veriyor. Hata degil,")
    print("  beklenen sonuc: kanat duzlemsel, yanal kuvvet uretecek yuzeyi")
    print("  yok. C_l_beta ise saglikli negatif -- ok acisi YALPA")
    print("  kararliligini veriyor, SAPMA kararliligini vermiyor.")
    print()
    print("  Dolayisiyla yon kararliligi UC CERCEVELERINDEN gelmek zorunda:")
    print("  seyirde onlar kanat duzlemine DIK duran yuzeylerdir. Modelde yok.")
    print()
    ist, _, _ = istasyonlar(n=200)
    x_uc = ist[-1][1] + 0.5 * ist[-1][2]
    kol_f = x_uc - xg
    print("  cerceve orta-veteri x = %.3f m, CG'ye kol = %.3f m" % (x_uc, kol_f))
    print("  GEREKEN yanal alan (iki cerceve toplami):")
    print("  %10s %14s %14s   %s" % ("C_n_beta", "a_f = 3,0", "a_f = 5,0",
                                     "nereden"))
    for hedef, etiket in HEDEFLER:
        print("  %10.4f %11.4f m2 %11.4f m2   %s"
              % (hedef, gereken_yanal_alan(hedef, kol_f, 3.0, o),
                 gereken_yanal_alan(hedef, kol_f, 5.0, o), etiket))
    boy = 2 * 0.71
    print()
    print("  Cerceve boyu 2 x 0,71 = %.2f m; iki cerceve -> %.2f m toplam."
          % (boy, 2 * boy))
    for hedef, etiket in HEDEFLER:
        s = gereken_yanal_alan(hedef, kol_f, 4.0, o)
        print("     C_n_beta = %.4f /rad -> fairing veteri %3.0f mm   (%s)"
              % (hedef, 1000 * s / (2 * boy), etiket))
    print("  20 mm kalinlikli bir fairing'in veteri tipik olarak 50-70 mm.")
    print()
    print("  OLCUT NEREDEN GELIYOR (NACA ACR L4H19, 1944, s. 18):")
    print("  Langley serbest-ucus tuneli, kuyruksuz modeller. Geleneksel")
    print("  ucaklar icin onerilen deger 'usually greater than 0.001 per")
    print("  degree'; modeller bunun UCTE BIRIYLE de ucurulmus, ama 'the")
    print("  best flying qualities ... were obtained with values of C_n_beta")
    print("  in excess of 0.001'. Ayni rapor kuyruksuz ucaklarin bu")
    print("  gereksinimden MUAF OLMADIGINI acikca soyluyor.")
    print("  Yani 0,03 ve 0,05 /rad bizim SECTIGIMIZ sayilardi; alanin")
    print("  yerlesik olcutu 0,0573 /rad ve ikisi de onun ALTINDA.")
    print()

    print("-" * 74)
    print("SAPMA SONUMLEMESI -- alt sinir (yalniz profil suruklemesi)")
    print("-" * 74)
    Cnr, Ic, _ = sonumleme_n()
    q = 0.5 * RHO * V_SEYIR ** 2
    S, bb = o["alan"], o["aciklik"]
    egim = abs(Cnr) * q * S * bb * bb / (2 * V_SEYIR)
    print("  C_n_r = %+.5f  (kesit c_d = %.3f varsayimi)" % (Cnr, CD0_KESIT))
    print("  dN/dr = %.2f N m / (rad/s),  tau = I_zz/(dN/dr) = %.1f s"
          % (egim, Izz / egim))
    print("  Bu sayilar SONUMLEMENIN ZAYIFLIGINI gosteriyor, otoritenin")
    print("  gucunu degil: duzlemsel kanadin sapma sonumlemesi neredeyse")
    print("  yoktur. Gercek sonumleme, yon kararliligini saglayacak AYNI")
    print("  dusey yuzeylerden gelecek -- yani ikisi ayni acik kalemdir.")
    print()
    print("  ATALET SINIRI ise anlamli ve saglaniyor:")
    for T, ad in ((T_CIFT, "16,2 N"), (T_CIFT_TEMKINLI, "12,4 N")):
        Mz, _ = mevcut_sapma(T)
        al = Mz / Izz
        print("     %s -> M_z %5.1f N m -> %.2f rad/s2 = %.0f derece/s2;"
              " 15 derece sapmaya %.2f s"
              % (ad, Mz, al, math.degrees(al),
                 math.sqrt(2 * math.radians(15) / al)))
    print()
    print("-" * 74)
    print("SONUC")
    print("-" * 74)
    print("  1. Sapma OTORITESI yunuslamanınkinden 2,4 kat guclu (kol yari")
    print("     aciklik). Atalet siniri rahat saglaniyor.")
    print("  2. Sapma KARARLILIGI planformdan GELMIYOR (C_n_beta = 0);")
    print("     uc cercevesi fairing'inden gelmek zorunda. Gereken yanal")
    print("     alan makul, ama HESAPLANMIS DEGIL.")
    print("  3. Fairing artik yalnizca bir SURUKLEME onlemi degil, ayni")
    print("     zamanda YON KARARLILIGI YUZEYIDIR. Makale bunu hicbir yerde")
    print("     soylemiyor; bu turun en onemli yeni tasarim gereksinimi budur.")
    print("  4. Yatista oldugu gibi: otorite GOSTERILMIYOR, BOYUTLANDIRILIYOR.")
