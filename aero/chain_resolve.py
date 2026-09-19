# -*- coding: utf-8 -*-
"""ZINCIR VE MENZILLER, HESAPLANMIS PERVANE VERIMIYLE YENIDEN COZULUYOR.

NEDEN VAR. nose_propeller.py, makalenin kendi aski FM'i 0,599'u tutturan
paletin seyirde 0,632 - 0,683 verdigini hesapladi; makale ayni palet icin
0,80 diyor. 2.12'nin zinciri o 0,80'i tasiyor ve her menzil o zincirden
turuyor. Bu betik butun zinciri ve butun menzilleri yeniden cozuyor.

EN ONEMLI MODELLEME KARARI, VE ACIKCA SOYLENIYOR.

baseline.py'de eta_zincir GOREV sozlugunde, yani UC MIMARIDE DE AYNI. Bu,
her ucune 0,80 vermek demektir. Hesap A icin bunun yanlis oldugunu
gosterdi. Peki B ve C icin de yanlis mi?

  A (kuyruk ustu)  tek SABIT HATVELI propulsor, iki gorev
                   -> 0,80'i hak etmiyor. Hesaplanan: 0,632 - 0,683.
  B (lift+cruise)  seyir pervanesi YALNIZCA seyir yapar; askiyi ayri
                   rotorlar yapar -> palet seyir icin tasarlanabilir
                   -> 0,80 mesru.
  C (tilt)         tek propulsor iki gorev, AMA DEGISKEN HATVE GOBEGI
                   VAR -> palet her rejimde ayarlanir -> 0,80 mesru.

Bu ucuncu satir sonucun kendisidir: **degisken hatve gobegini reddetmenin
bedeli, simdi bir sayidir.** Makale o gobegi elediğini soyluyordu ama
neye mal oldugunu hic yazmamisti.

TARAFLI OLMAMAK ICIN ikinci bir senaryo da basiliyor: hepsi ayni cezayi
oderse ne olur. Okuyucu ikisini de gorsun.

BULUNAN IKINCI SEY. baseline.py'nin duyarlilik_C() islevi, TILT'in paleti
askiya boyutlanmissa seyirde ceza odemesi gerektigini zaten soyluyor ve
eta'yi 0,85'e kadar tariyor. Gerekcesi de yazili: "pal hover'a
boyutlanmis -> seyirde A'nin pervanesinden IYI olmasi beklenmez." Yani
A'nin pervanesi RAKIBIN cezalandirildigi OLCUT olarak kullanilmis, ama
kendisi hic olculmemisti.
"""
import math
import os
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)

import baseline as BL                                        # noqa: E402

ETA_P_MAKALE = 0.80
ETA_P_ALT, ETA_P_UST = 0.632, 0.683     # nose_propeller_crossing.py
ZINCIR_PERVANESIZ = 0.28 * 0.90 * 0.95 * 0.92                # 0,2202
MENZIL_HAFIF = 1598.0
MENZIL_AGIR = 1814.0


def gorev_ile(eta_p):
    """GOREV'in eta_p'ye bagli olan her terimi yeniden cozulmus kopyasi."""
    g = dict(BL.GOREV)
    g["eta_zincir"] = ZINCIR_PERVANESIZ * eta_p
    # 2.12'nin kendi eta_seyir'i 0,721; 1,7 kW'tan geri cozulmus ve
    # ortuk pervane verimi 0,784, zincirdeki 0,80 DEGIL. Makalenin kendi
    # iki sayisi arasinda zaten %2 tutarsizlik var. Oraniyla oluyoruz.
    g["eta_seyir"] = BL.GOREV["eta_seyir"] * eta_p / ETA_P_MAKALE
    return g


def satir(ad, eta_p):
    z = ZINCIR_PERVANESIZ * eta_p
    return (ad, eta_p, z, MENZIL_HAFIF * eta_p / ETA_P_MAKALE,
            MENZIL_AGIR * eta_p / ETA_P_MAKALE)


def sozlesmeler_mimariye_ozgu(eta_A, eta_B=0.80, eta_C=0.80,
                              LD_temiz=13.44, f_egme=0.05,
                              f_kaldirma_grubu=0.10, f_tampon=0.04,
                              A_LD_carpan=None):
    """sozlesmeler() ile ayni uc sozlesme, ama her mimari KENDI zinciriyle."""
    ms = BL.mimariler(f_kaldirma_grubu, f_egme, True, 1.00, 1.00,
                      A_LD_carpan=A_LD_carpan, f_tampon=f_tampon)
    gs = [gorev_ile(eta_A), gorev_ile(eta_B), gorev_ile(eta_C)]

    ref = BL.boyutlandir(ms[0], LD_temiz, g=gs[0])
    m_yakit_A = BL.ORTAK["f_yakit"] * ref["MTOW"]
    MTOW_A = ref["MTOW"]
    print("  Referans A: MTOW %.1f kg, yakit %.2f kg, L/D %.2f, menzil %.0f km"
          % (MTOW_A, m_yakit_A, ref["LD"], ref["menzil"]))
    print("  eta_p:  A %.3f   B %.3f   C %.3f" % (eta_A, eta_B, eta_C))
    print()
    baslik = ("  1) sabit yakit KESRI (%0,16)",
              "  2) sabit yakit KUTLESI (%.2f kg)" % m_yakit_A,
              "  3) sabit MTOW (%.1f kg) + sabit faydali yuk" % MTOW_A)
    hesap = (lambda m, g: BL.boyutlandir(m, LD_temiz, g=g),
             lambda m, g: BL.sabit_yakit(m, LD_temiz, m_yakit_A, g=g),
             lambda m, g: BL.sabit_MTOW(m, LD_temiz, MTOW_A, g=g))
    ozet = []
    for ad, f in zip(baslik, hesap):
        print(ad)
        print("    %-24s %8s %8s %9s %10s"
              % ("", "MTOW", "f_yakit", "menzil", "A'ya gore"))
        taban = None
        farklar = []
        for m, g in zip(ms, gs):
            r = f(m, g)
            if r.get("kapanmadi"):
                print("    %-24s  KAPANMADI (f_bos %.3f)" % (m.ad, r["f_bos"]))
                farklar.append(float("nan"))
                continue
            if taban is None:
                taban = r["menzil"]
            d = 100 * (r["menzil"] - taban) / taban
            farklar.append(d)
            print("    %-24s %8.1f %8.3f %9.0f %+9.1f%%"
                  % (m.ad, r["MTOW"], r.get("f_yakit", BL.ORTAK["f_yakit"]),
                     r["menzil"], d))
        ozet.append((ad.strip(), farklar))
        print()
    return ozet


if __name__ == "__main__":
    print("=" * 74)
    print("1. ZINCIR")
    print("=" * 74)
    print("motor 0,28 x jeneratör 0,90 x güç elektroniği 0,95 x makine 0,92")
    print("  = %.4f, pervane HARIC" % ZINCIR_PERVANESIZ)
    print()
    print("  %-26s %8s %9s %11s %11s"
          % ("", "eta_p", "zincir", "hafif km", "agir km"))
    print("  " + "-" * 68)
    for ad, e in (("makalenin varsayimi", ETA_P_MAKALE),
                  ("hesaplanan, alt uc", ETA_P_ALT),
                  ("hesaplanan, ust uc", ETA_P_UST)):
        a, ep, z, mh, ma = satir(ad, e)
        print("  %-26s %8.3f %9.4f %11.0f %11.0f" % (a, ep, z, mh, ma))
    print("  " + "-" * 68)
    print("  %-26s %8s %9s %10.1f%% %10.1f%%"
          % ("dusus, ust uc", "", "",
             -100 * (1 - ETA_P_UST / ETA_P_MAKALE),
             -100 * (1 - ETA_P_UST / ETA_P_MAKALE)))
    print("  %-26s %8s %9s %10.1f%% %10.1f%%"
          % ("dusus, alt uc", "", "",
             -100 * (1 - ETA_P_ALT / ETA_P_MAKALE),
             -100 * (1 - ETA_P_ALT / ETA_P_MAKALE)))
    print()
    print("  NOT: agir hattin kendi iki noktali hesabi ayri kosuyor")
    print("  (nose_propeller_heavy.py). Yukaridaki agir sutun, hafif")
    print("  hattin oranini tasiyan bir ON DEGERDIR, sonuc degildir.")

    print()
    print("=" * 74)
    print("2. SOZLESMELER -- A cezayi oder, B ve C odemez")
    print("=" * 74)
    print("Gerekce: B'nin seyir pervanesi yalnizca seyir yapar; C'nin")
    print("degisken hatve gobegi vardir. Ikisi de 0,80'i hak eder.")
    print()
    print("-- A'nin UST ucu (lehimize) --")
    ust = sozlesmeler_mimariye_ozgu(ETA_P_UST)
    print("-- A'nin ALT ucu (aleyhimize) --")
    alt = sozlesmeler_mimariye_ozgu(ETA_P_ALT)

    print("=" * 74)
    print("3. KARSI SENARYO -- hepsi ayni cezayi oderse")
    print("=" * 74)
    print("Bu, 0,80'i hepsinden almak demek. A'nin lehine olan okuma budur")
    print("ve tam da bu yuzden basiliyor: okuyucu ikisini de gorsun.")
    print()
    hepsi = sozlesmeler_mimariye_ozgu(ETA_P_ALT, ETA_P_ALT, ETA_P_ALT)

    print("=" * 74)
    print("4. NE DEGISTI")
    print("=" * 74)
    print("%-34s %10s %10s %10s" % ("sozlesme", "A ust", "A alt", "hepsi ayni"))
    print("-" * 68)
    for i, (ad, _) in enumerate(ust):
        print("%-34s %9.1f%% %9.1f%% %9.1f%%"
              % (ad[:34], ust[i][1][1], alt[i][1][1], hepsi[i][1][1]))
    print("(sutunlar: B'nin A'ya gore menzil farki, yuzde)")
    print()
    print("%-34s %10s %10s %10s" % ("", "A ust", "A alt", "hepsi ayni"))
    for i, (ad, _) in enumerate(ust):
        print("%-34s %9.1f%% %9.1f%% %9.1f%%"
              % (ad[:34], ust[i][1][2], alt[i][1][2], hepsi[i][1][2]))
    print("(sutunlar: C'nin A'ya gore menzil farki, yuzde)")


    # --- 5. YAYIMLANMIS TABLO, yeniden cozulmus -----------------------
    import resize as RS
    carp = RS.carpan(0.0153)
    print()
    print("=" * 74)
    print("5. 3.6'NIN YAYIMLANMIS TABLOSU -- 'rotorlar faturalanmis'")
    print("=" * 74)
    print("Makalenin BASILI sonucu bu satirdir; yukaridaki 2. bolum")
    print("rotor terimi ONCESI durumdur. A'nin L/D carpani 1/%.3f." % (1 / carp))
    print()
    print("-- makalenin kendi hali (eta_p = 0,80, hepsine) --")
    taban = sozlesmeler_mimariye_ozgu(0.80, 0.80, 0.80, A_LD_carpan=carp)
    print("-- A'nin UST ucu (0,683), B ve C 0,80 --")
    y_ust = sozlesmeler_mimariye_ozgu(ETA_P_UST, A_LD_carpan=carp)
    print("-- A'nin ALT ucu (0,632), B ve C 0,80 --")
    y_alt = sozlesmeler_mimariye_ozgu(ETA_P_ALT, A_LD_carpan=carp)

    print("=" * 74)
    print("6. YAYIMLANMIS TABLO: ONCE / SONRA")
    print("=" * 74)
    print("%-30s %10s %10s %10s" % ("sozlesme", "basili", "A ust", "A alt"))
    print("-" * 64)
    for i in range(3):
        print("B  %-27s %+9.1f%% %+9.1f%% %+9.1f%%"
              % (taban[i][0][:27], taban[i][1][1], y_ust[i][1][1],
                 y_alt[i][1][1]))
    print("-" * 64)
    for i in range(3):
        print("C  %-27s %+9.1f%% %+9.1f%% %+9.1f%%"
              % (taban[i][0][:27], taban[i][1][2], y_ust[i][1][2],
                 y_alt[i][1][2]))
    print()
    print("Makalenin basili satirlari: B +21,1 / -5,4 / -44,9")
    print("                            C +58,3 / +49,2 / +35,7")
    print("Ustteki 'basili' sutunu bunlari yeniden uretmiyorsa DUR.")

    # --- 7. KARSI SENARYO, YAYIMLANMIS AYARDA ------------------------
    print()
    print("=" * 74)
    print("7. KARSI SENARYO -- rotorlar faturalanmis halde, hepsi 0,632")
    print("=" * 74)
    print("BUNU KACIRMISTIM. 3. bolumdeki karsi senaryo rotor terimi ONCESI")
    print("ayarda kosuyordu; yayimlanmis tablo ise rotorlar faturalanmis")
    print("halde. Karsilastirilmasi gereken sey bu.")
    print()
    hepsi_y = sozlesmeler_mimariye_ozgu(ETA_P_ALT, ETA_P_ALT, ETA_P_ALT,
                                        A_LD_carpan=carp)
    print("%-30s %10s %10s" % ("sozlesme", "basili", "hepsi 0,632"))
    print("-" * 54)
    for i in range(3):
        print("B  %-27s %+9.1f%% %+9.1f%%"
              % (taban[i][0][:27], taban[i][1][1], hepsi_y[i][1][1]))
    for i in range(3):
        print("C  %-27s %+9.1f%% %+9.1f%%"
              % (taban[i][0][:27], taban[i][1][2], hepsi_y[i][1][2]))
    print()
    print("SORU: ceza simetrik olsa bile B satirinda ISARET DONUYOR mu?")
