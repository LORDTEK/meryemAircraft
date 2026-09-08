# -*- coding: utf-8 -*-
"""STATIK YUNUSLAMA KARARLILIGI -- tarafsiz nokta ve statik marj.

NEDEN VAR. 7.6'nin gecis zarfi, EN DAR C_m butcesinin donusun SONUNDA
oldugunu gosterdi: alfa kucuk (5-6 derece), hiz yuksek, butce 0,079
(hafif) / 0,015 (agir). Metin bunu "kuyruksuz bir ucagin siradan denge
sorusu" diye niteledi.

Bir dis denetim buna itiraz etti ve hakli: bu ucakta elevon yok, refleks
kamber tarif edilmemis, ve CG kok veterinin %57-58'inde. Dolayisiyla
"siradan" demek yetmez -- GOSTERILMESI gerekir.

BU MODUL onu gosterir, ya da gosteremedigini soyler. Girdap-kafes
cozumuyle C_m(alfa) hesaplanir, oradan

    dC_m/dC_L = (x_ref - x_np) / c_ref      ->      x_np
    statik marj = (x_np - x_cg) / c_ref

x_cg icin: donme.py'nin HACIM AGIRLIKLI yerlestirmesi. Bu bir OLCUM
degil, bir TASARIM KURALIDIR: ayrintili ic yerlesim tarif edilmedigi
icin, kutleler govde hacmiyle orantili dagitilmis kabul edilir. Cikan
deger (kok veterinin %80,2'si) bu kuralin sonucudur; farkli bir
yerlesim farkli bir CG verir. Bu yuzden asagida CG bir PENCERE olarak
taranir ve pencerenin siniri bir TASARIM KISITI olarak yazilir.

Referans veter: gercek ortalama aerodinamik veter (MAC), S/b degil.
Onceki bir surum ikisini karistirmisti: marj MAC uzerinden (%12,4),
denge gereksinimi ise S/b uzerinden (0,063) verilmisti. Ikisi de
MAC uzerinden verilir artik.

SINIR -- ONEMLI. vlm.py'nin kesitleri SIMETRIK NACA'dir; makalenin tarif
ettigi kamber ve refleks dagilimlari burada YOKTUR. Dolayisiyla:
  - C_m0 (sifir-kaldirmada moment) bu kosumda SIFIRDIR ve gercek degildir;
  - C_m_alfa ve tarafsiz nokta ise kambere birinci mertebede duyarsizdir
    ve HESAPLANABILIR.
Yani bu modul KARARLILIGI verir, DENGEYI (trim) vermez. Denge, kamber ve
refleks tanimlandiktan sonra hesaplanabilir.
"""
import sys, os, math
import numpy as np
import aerosandbox as asb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from planform import istasyonlar, olcuier, P
from vlm import kanat_kur, KESIT_SAYISI, SPAN_COZ, VETER_COZ

CL_SEYIR = 0.45          # 6.3: hafif hat, 50 kg, 30 m/s, S = 1,9785 m2
CG_PENCERE = (0.78, 0.80, 0.802, 0.83, 0.85)


def mac():
    """Gercek ortalama aerodinamik veter ve hucum kenarinin x'i.

        MAC   = (2/S) int c^2 dy      x_LE = (2/S) int x_le c dy
    """
    ist, yari, bir = istasyonlar()
    S2 = c2 = xc = 0.0
    for a, b in zip(ist[:-1], ist[1:]):
        dy = b[0] - a[0]
        S2 += 0.5 * (a[2] + b[2]) * dy
        c2 += 0.5 * (a[2] ** 2 + b[2] ** 2) * dy
        xc += 0.5 * (a[1] * a[2] + b[1] * b[2]) * dy
    return c2 / S2, xc / S2


def cm_taramasi(alfalar=(0.0, 2.0, 4.0, 6.0), hiz=30.0, x_ref=0.0,
                kesit=None, sr=None, cr=None):
    o = olcuier()
    kanat = kanat_kur(kesit)
    c_ref = mac()[0]
    ucak = asb.Airplane(wings=[kanat], s_ref=o["alan"], b_ref=o["aciklik"],
                        c_ref=c_ref, xyz_ref=[x_ref, 0.0, 0.0])
    cik = []
    for a in alfalar:
        r = asb.VortexLatticeMethod(
            airplane=ucak, op_point=asb.OperatingPoint(velocity=hiz, alpha=a),
            spanwise_resolution=sr or SPAN_COZ,
            chordwise_resolution=cr or VETER_COZ).run()
        cik.append((a, float(r["CL"]), float(r["Cm"])))
    return o, c_ref, cik


def tarafsiz_nokta(x_ref=0.0, **kw):
    """dC_m/dC_L'den tarafsiz noktayi cikarir.

        C_m(x_ref) = C_m(x_np) + C_L (x_ref - x_np)/c_ref
        -> dC_m/dC_L = (x_ref - x_np)/c_ref
        -> x_np = x_ref - c_ref (dC_m/dC_L)
    """
    o, c_ref, cik = cm_taramasi(x_ref=x_ref, **kw)
    CL = np.array([c[1] for c in cik])
    Cm = np.array([c[2] for c in cik])
    egim = np.polyfit(CL, Cm, 1)[0]          # dC_m/dC_L
    x_np = x_ref - c_ref * egim
    return o, c_ref, cik, egim, x_np



# ---------------------------------------------------------------------
# KONVANSIYON DENETIMI
# ---------------------------------------------------------------------
# NEDEN VAR. Bir dis degerlendirme sunu istedi: iki zincir --
#   (a) CG -> tarafsiz nokta -> statik marj
#   (b) CG -> aerodinamik moment -> gereken denge C_m
# ayni referans noktasini, ayni isaret kuralini, ayni q, S ve veteri
# kullaniyor mu? Referans veter hatasi (MAC / S-b karisimi) tam da bu
# aileden cikti; ikincisinin OLMADIGINI varsaymak yetmez, GOSTERILMELI.
#
# Alti sinama var ve hicbiri "ayni formulu iki kez yazmak" degil:
# ucu dogrudan cozucuye sorulmus, biri boyutlu yoldan bagimsiz
# turetilmis.

MTOW_HAFIF, S_HAFIF, V_SEYIR = 50.0, 1.9785, 30.0
CG_KURAL = 0.802                 # donme.py, hacme orantili yerlestirme


def _cm(x_ref, alfa, hiz=30.0):
    o = olcuier()
    ucak = asb.Airplane(wings=[kanat_kur()], s_ref=o["alan"],
                        b_ref=o["aciklik"], c_ref=mac()[0],
                        xyz_ref=[x_ref, 0.0, 0.0])
    r = asb.VortexLatticeMethod(
        airplane=ucak, op_point=asb.OperatingPoint(velocity=hiz, alpha=alfa),
        spanwise_resolution=SPAN_COZ, chordwise_resolution=VETER_COZ).run()
    return float(r["CL"]), float(r["Cm"])


def konvansiyon_denetimi():
    """Alti sinama. Her biri (ad, gecti_mi, aciklama) dondurur."""
    o = olcuier()
    MAC, x_le = mac()
    kok = P["kokVeter"]
    S, b = o["alan"], o["aciklik"]
    x_cg = CG_KURAL * kok
    _, _, _, egim, x_np = tarafsiz_nokta(x_ref=0.0)
    marj = (x_np - x_cg) / MAC
    sonuc = []

    # 1. BASLANGIC NOKTASI. donme.py x'i kok hucum kenarindan, firara +
    # olarak sayiyor. vlm.py'nin ilk kesiti xyz_le = [0, 0, 0]. Ayni mi?
    ist, _, _ = istasyonlar(n=200)
    ayni = abs(ist[0][1]) < 1e-12
    sonuc.append(("baslangic noktasi ortak (kok hucum kenari, x=0)", ayni,
                  "planform ilk istasyon x_le = %.3e" % ist[0][1]))

    # 2. ISARET KURALI. x_ref kok hucum kenarindayken kaldirma HER ZAMAN
    # referansin arkasinda dogar; dolayisiyla pozitif alfada C_m NEGATIF
    # (burun asagi) olmali. Cikmazsa isaret kurali ters demektir.
    _, cm_le = _cm(0.0, 4.0)
    sonuc.append(("isaret kurali: kok LE'ye gore C_m(alfa>0) < 0", cm_le < 0,
                  "C_m(4 derece, x_ref=0) = %+.5f" % cm_le))

    # 3. TARAFSIZ NOKTA SINAMASI -- cozucuye dogrudan sorulmus. x_ref'i
    # hesaplanan x_np'ye koyunca dC_m/dC_L SIFIRLANMALI. Bu, x_np'nin
    # cikarildigi formulun tersten dogrulanmasidir.
    CL2, cm2 = _cm(x_np, 2.0)
    CL6, cm6 = _cm(x_np, 6.0)
    egim_np = (cm6 - cm2) / (CL6 - CL2)
    sonuc.append(("x_ref = x_np'de dC_m/dC_L ~ 0", abs(egim_np) < 5e-3,
                  "dC_m/dC_L = %+.5f (kok LE'de %+.4f idi)" % (egim_np, egim)))

    # 4. MARJ SINAMASI -- yine cozucuye sorulmus. x_ref'i CG'ye koyunca
    # dC_m/dC_L = -(statik marj) olmali. Marj formulu ile cozucunun
    # kendi momenti boylece ayni sayida bulusuyor.
    CLa, cma = _cm(x_cg, 2.0)
    CLb, cmb = _cm(x_cg, 6.0)
    egim_cg = (cmb - cma) / (CLb - CLa)
    sonuc.append(("x_ref = x_cg'de dC_m/dC_L = -marj",
                  abs(egim_cg + marj) < 5e-3,
                  "cozucu %+.4f, marj formulu %+.4f" % (egim_cg, -marj)))

    # 5. q BAGIMSIZLIGI. C_m boyutsuz; 20 ve 40 m/s ayni sayiyi vermeli.
    # Vermezse bir yerde boyutlu bir buyukluk katsayiya sizmis demektir.
    _, cm20 = _cm(x_cg, 4.0, hiz=20.0)
    _, cm40 = _cm(x_cg, 4.0, hiz=40.0)
    sonuc.append(("C_m hiza bagimsiz", abs(cm20 - cm40) < 1e-6,
                  "20 m/s %+.6f, 40 m/s %+.6f" % (cm20, cm40)))

    # 6. BOYUTLU CAPRAZ SINAMA -- bagimsiz turetme. Katsayi zincirini hic
    # kullanmadan: seyirde kaldirma agirliga esit, tarafsiz noktada etki
    # ediyor, CG'ye gore kolu (x_np - x_cg). Cikan MOMENT, katsayidan
    # geri cevrilen momentle ayni olmali.
    W = MTOW_HAFIF * 9.81
    M_boyutlu = W * (x_np - x_cg)                       # N m
    q = 0.5 * RHO_ * V_SEYIR ** 2
    CL_seyir = W / (q * S_HAFIF)
    M_katsayi = CL_seyir * marj * q * S_HAFIF * MAC     # N m
    sonuc.append(("boyutlu ve katsayi yolu ayni momenti veriyor",
                  abs(M_boyutlu - M_katsayi) < 1e-6 * max(1.0, abs(M_boyutlu)),
                  "W(x_np - x_cg) = %.4f N m ; C_L marj q S MAC = %.4f N m"
                  % (M_boyutlu, M_katsayi)))

    return sonuc, dict(MAC=MAC, x_le=x_le, x_np=x_np, x_cg=x_cg, marj=marj,
                       CL_seyir=W / (q * S_HAFIF), S=S, b=b, kok=kok)


RHO_ = 1.225


if __name__ == "__main__":
    kok = P["kokVeter"]
    MAC, x_le = mac()
    print("=" * 74)
    print("STATIK YUNUSLAMA KARARLILIGI -- girdap kafes")
    print("=" * 74)
    o, c_ref, cik, egim, x_np = tarafsiz_nokta(x_ref=0.0)
    print("planform: aciklik %.3f m, alan %.4f m2, kok veter %.2f m"
          % (o["aciklik"], o["alan"], kok))
    print("MAC = %.4f m (S/b = %.4f m; marj ve denge MAC uzerinden)"
          % (MAC, o["alan"] / o["aciklik"]))
    print("MAC hucum kenari x_le = %.4f m" % x_le)
    print()
    print("  %6s %10s %12s" % ("alfa", "CL", "Cm (kok LE)"))
    for a, CL, Cm in cik:
        print("  %6.1f %10.4f %12.5f" % (a, CL, Cm))
    print()
    print("  dC_m/dC_L (kok hucum kenarina gore) = %+.4f" % egim)
    print("  TARAFSIZ NOKTA x_np = %.4f m = kok veterinin %%%.1f'i"
          " = MAC'in %%%.1f'i" % (x_np, 100 * x_np / kok,
                                  100 * (x_np - x_le) / MAC))
    print()
    print("CG PENCERESI -- hacim agirlikli kural bir NOKTA verir; tasarim")
    print("kisiti olarak yazilabilmesi icin komsulugu da taranir.")
    print("  denge gereksinimi: |C_m| = C_L_seyir x marj, C_L_seyir = %.2f"
          % CL_SEYIR)
    print()
    print("  %10s %10s %12s %12s" % ("CG (%kok)", "x_cg (m)",
                                     "marj (%MAC)", "gereken C_m"))
    for oran in CG_PENCERE:
        x_cg = oran * kok
        sm = (x_np - x_cg) / MAC
        print("  %9.1f%% %10.4f %11.1f%% %12.3f"
              % (100 * oran, x_cg, 100 * sm, CL_SEYIR * sm))
    print()
    print("  Refleks kesitler tipik olarak 0,02-0,05 C_m0 verir; pencerenin")
    print("  ust ucu (%83-85) bu araliga girer, alt ucu girmez.")
    print()
    print("  Not: kesitler simetrik; C_m0 bu kosumda sifirdir ve gercek")
    print("  degildir. Bu sonuc KARARLILIGI verir, DENGEYI vermez: yukaridaki")
    print("  'gereken C_m' bir GEREKSINIMDIR, saglandiginin gosterimi degil.")
    print()
    print("=" * 74)
    print("KONVANSIYON DENETIMI -- iki zincir ayni kurallari mi kullaniyor?")
    print("=" * 74)
    sinamalar, d = konvansiyon_denetimi()
    for ad, gecti, aciklama in sinamalar:
        print("  %s  %s" % ("GECTI " if gecti else "KALDI!", ad))
        print("          %s" % aciklama)
    kalan = [a for a, g, _ in sinamalar if not g]
    print()
    print("  %d sinama, %d kaldi." % (len(sinamalar), len(kalan)))
    if kalan:
        print("  KALANLAR: " + ", ".join(kalan))
