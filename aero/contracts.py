# -*- coding: utf-8 -*-
"""ADIM 13 -- SIRALAMALAR SOZLESMEYE AITTIR, ADIM 10'UN DORT KAPANISI UZERINDE.

Adim 10 yalniz bu yapilandirmayi (A) kapatti. Bu betik ayni dort kapanisin
her birinde uc mimariyi (A kuyruk ustu, B lift+cruise, C tilt) uc sozlesme
altinda boyutlandirir:

  1) sabit yakit KESRI     R ~ (L/D) eta_p               -- MTOW sadelesir
  2) sabit yakit KUTLESI   R ~ (L/D) eta_p / MTOW        -- yakit = A'nin yakiti
  3) sabit MTOW + faydali  R ~ (L/D) eta_p f_yakit       -- yakit artan yer

TABAN (her biri ilan edilir, hicbiri olculmedi):
  * surukleme: A'nin carpani drag_sweep.zincir'den (olumsuz uca x1,1 pay),
    closure.py ile AYNI. B ve C ayni temiz govdeye kendi carpanlarini uygular:
    B 13/17 (Bacchini'nin olcumu, baska bir govde), C 1,00 (ideallestirilmis).
  * pervane: A Adim 10'un hesaplanmis 0,632 / 0,683'u. B 0,80 (yalniz seyir
    yapan pervane), C 0,80 (degisken hatve gobegi). Ikisi de VARSAYIM.
    chain_resolve.gorev_ile() her mimariye kendi eta_p'siyle uygulanir
    (eta_zincir ve eta_seyir birlikte).
  * tampon: ucunde de %3,6 ve ucunde de motor seyre boyutlu -- Fatura 3
    ORTAK tutulur; karsilastirma Fatura 1 ve Fatura 2'yi olcer.
  * B'nin ek tahrik grubu %10, C'nin egme mekanizmasi %5: parametre.

DUYARLILIK: (a) hepsi A'nin eta_p'si (karsi-olgusal), (b) B'nin ek grubu
%5 / %15, (c) B'nin cezasi carpan yerine SABIT C_D artisi olarak.

Sonuc: aero/contracts-result.txt
"""
import os
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)

import baseline as BL                                     # noqa: E402
import drag_sweep as DS                                   # noqa: E402
from chain_resolve import gorev_ile                       # noqa: E402
from closure import CD0, ETA_P, kapat                     # noqa: E402

AD = ("kuyruk ustu", "lift+cruise", "tilt")
KAPANISLAR = (("A", "olumsuz", "alt"), ("B", "olumsuz", "ust"),
              ("C", "elverisli", "alt"), ("D", "elverisli", "ust"))
B_CARPAN = 13.0 / 17.0


def b_artis_carpani(ld_temiz):
    """(c) B'nin cezasi sabit C_D artisi: 13/17'nin temiz L/D 17'deki degeri."""
    dcd = DS.CL * (1.0 / 13.0 - 1.0 / 17.0)
    cd_temiz = DS.CL / ld_temiz
    return cd_temiz / (cd_temiz + dcd)


def kos(cd0, eta_A, eta_BC=0.80, f_grup=0.10, b_artis=False):
    pay = 1.1 if abs(cd0 - 0.0381) < 1e-9 else 1.0
    ld_temiz, a_carpan = DS.zincir(cd0, rotorlu=True, pay=pay)
    ms = BL.mimariler(f_kaldirma_grubu=f_grup, f_tampon=0.036)
    ms[0].LD_carpan = a_carpan
    ms[1].LD_carpan = b_artis_carpani(ld_temiz) if b_artis else B_CARPAN
    ms[2].LD_carpan = 1.00
    gs = (gorev_ile(eta_A), gorev_ile(eta_BC), gorev_ile(eta_BC))
    ref = BL.boyutlandir(ms[0], ld_temiz, g=gs[0])
    m_yakit = BL.ORTAK["f_yakit"] * ref["MTOW"]
    out = {}
    for i, (m, g) in enumerate(zip(ms, gs)):
        out[(1, i)] = BL.boyutlandir(m, ld_temiz, g=g)
        out[(2, i)] = BL.sabit_yakit(m, ld_temiz, m_yakit, g=g)
        out[(3, i)] = BL.sabit_MTOW(m, ld_temiz, ref["MTOW"], g=g)
    return ld_temiz, ref, out


def fark(out, s, i):
    a, x = out[(s, 0)], out[(s, i)]
    if x.get("kapanmadi") or a.get("kapanmadi"):
        return float("nan")
    return 100.0 * (x["menzil"] / a["menzil"] - 1.0)


def kapanis_tablosu(etiket, **kw):
    print(etiket)
    print("%-3s %-7s %-6s | %8s %8s %8s | %8s %8s %8s | %8s %8s"
          % ("", "C_D0", "eta_A", "B/A s1", "B/A s2", "B/A s3",
             "C/A s1", "C/A s2", "C/A s3", "mB/mA", "mC/mA"))
    satirlar = []
    for k, dk, ek in KAPANISLAR:
        cd0, eA = CD0[dk], ETA_P[ek]
        _, ref, out = kos(cd0, eA, **kw)
        fb = [fark(out, s, 1) for s in (1, 2, 3)]
        fc = [fark(out, s, 2) for s in (1, 2, 3)]
        mb = out[(1, 1)]["MTOW"] / out[(1, 0)]["MTOW"]
        mc = out[(1, 2)]["MTOW"] / out[(1, 0)]["MTOW"]
        satirlar.append((k, fb, fc, mb, mc))
        print("%-3s %-7.4f %-6.3f | %+7.1f%% %+7.1f%% %+7.1f%% | %+7.1f%% %+7.1f%% %+7.1f%% | %8.3f %8.3f"
              % (k, cd0, eA, *fb, *fc, mb, mc))
    return satirlar


def isaret_ozeti(satirlar, ad):
    for j, isim in ((1, "B"), (2, "C")):
        for s in range(3):
            v = [r[j][s] for r in satirlar]
            ok = "B onde" if all(x > 0 for x in v) else (
                "A onde" if all(x < 0 for x in v) else "ISARET DEGISIYOR")
            print("   %s, sozlesme %d: %+6.1f .. %+6.1f %%  -> %s"
                  % (isim if isim == "B" else "C", s + 1, min(v), max(v),
                     ok.replace("B onde", "%s onde" % isim)))
    print()


if __name__ == "__main__":
    print("ADIM 13 -- UC MIMARI, UC SOZLESME, ADIM 10'UN DORT KAPANISI")
    print("=" * 96)
    print("Taban: A eta_p hesaplanmis (0,632/0,683); B ve C 0,80 varsayim; tampon %3,6")
    print("hepsinde; B ek grup %10; C egme %5, L/D carpani 1,00 (ideallestirilmis).")
    print("Sozlesme 2 ve 3'te yakit kutlesi / MTOW, A'nin o kapanistaki degeri.")
    print()

    # --- A'nin kendi kapanisi Adim 10'u yeniden uretmeli ---------------
    print("SINAMA: A'nin kapanislari Adim 10'un tablosunu uretmeli")
    for k, dk, ek in KAPANISLAR:
        r1 = kapat(CD0[dk], ETA_P[ek])
        _, ref, _ = kos(CD0[dk], ETA_P[ek])
        print("  %s  closure.py %.2f kg %.0f km   bu betik %.2f kg %.0f km"
              % (k, r1["MTOW"], r1["menzil"], ref["MTOW"], ref["menzil"]))
        if abs(r1["MTOW"] - ref["MTOW"]) > 1e-6:
            sys.exit("!! DUR -- A'nin kapanisi Adim 10'dan farkli.")
    print("  ayni.")
    print()

    # --- ayrintili tablo -----------------------------------------------
    print("AYRINTI -- her kapanista MTOW (kg), L/D, menzil (km)")
    for k, dk, ek in KAPANISLAR:
        ldt, ref, out = kos(CD0[dk], ETA_P[ek])
        print("  kapanis %s (C_D0 %.4f, eta_A %.3f, temiz L/D %.2f; yakit %.2f kg; MTOW_A %.1f kg)"
              % (k, CD0[dk], ETA_P[ek], ldt, 0.16 * ref["MTOW"], ref["MTOW"]))
        for s, sad in ((1, "s1 sabit kesir"), (2, "s2 sabit yakit"), (3, "s3 sabit MTOW")):
            parca = []
            for i in range(3):
                r = out[(s, i)]
                if r.get("kapanmadi"):
                    parca.append("%-11s KAPANMADI" % AD[i])
                else:
                    parca.append("%-11s %5.1f kg L/D %5.2f %5.0f km"
                                 % (AD[i], r["MTOW"], r["LD"], r["menzil"]))
            print("    %-15s %s" % (sad, " | ".join(parca)))
    print()

    print("=" * 96)
    t0 = kapanis_tablosu("TABAN -- menzil farki A'ya gore; mB/mA sozlesme 1'de kutle orani")
    isaret_ozeti(t0, "taban")

    print("SALINIM -- sozlesme 1'den 3'e, A'ya dogru (yuzde puan)")
    for k, fb, fc, mb, mc in t0:
        print("  %s  B/A %+6.1f -> %+6.1f  (%5.1f puan)   C/A %+6.1f -> %+6.1f  (%5.1f puan)"
              "   A, B'den %%%.1f, C'den %%%.1f hafif (s1)"
              % (k, fb[0], fb[2], fb[0] - fb[2], fc[0], fc[2], fc[0] - fc[2],
                 100 * (1 - 1 / mb), 100 * (1 - 1 / mc)))
    print()
    print("KUTLE BILESENLERI, sozlesme 1 (bos kutle kesri)")
    for k, dk, ek in KAPANISLAR:
        _, _, out = kos(CD0[dk], ETA_P[ek])
        print("  %s  " % k + "   ".join(
            "%s f_bos %.3f f_tahrik %.3f motor %.2f kW"
            % (AD[i], out[(1, i)]["f_bos"], out[(1, i)]["f_tahrik"], out[(1, i)]["motor_kW"])
            for i in range(3)))
    print()

    print("=" * 96)
    print("(a) KARSI-OLGUSAL -- B ve C de A'nin eta_p'sini oder")
    print("%-3s | %8s %8s %8s | %8s %8s %8s" % ("", "B/A s1", "B/A s2", "B/A s3",
                                               "C/A s1", "C/A s2", "C/A s3"))
    ta = []
    for k, dk, ek in KAPANISLAR:
        _, _, out = kos(CD0[dk], ETA_P[ek], eta_BC=ETA_P[ek])
        fb = [fark(out, s, 1) for s in (1, 2, 3)]
        fc = [fark(out, s, 2) for s in (1, 2, 3)]
        ta.append((k, fb, fc, 0, 0))
        print("%-3s | %+7.1f%% %+7.1f%% %+7.1f%% | %+7.1f%% %+7.1f%% %+7.1f%%" % (k, *fb, *fc))
    isaret_ozeti(ta, "a")

    for fg in (0.05, 0.15):
        print("=" * 96)
        t = kapanis_tablosu("(b) B'nin ek tahrik grubu %%%d" % round(100 * fg), f_grup=fg)
        isaret_ozeti(t, "b")

    print("=" * 96)
    t = kapanis_tablosu("(c) B'nin cezasi SABIT C_D artisi (13/17'nin temiz L/D 17'deki degeri)",
                        b_artis=True)
    isaret_ozeti(t, "c")
