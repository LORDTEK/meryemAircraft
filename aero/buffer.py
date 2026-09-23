# -*- coding: utf-8 -*-
"""ADIM 14 -- TAMPON: ADIM 10'UN KAPANISLARI HANGI OZGUL GUCU VARSAYIYOR,
VE OLCULMUS OZGUL GUCTE DONGU NEREDE KAPANIYOR?

ISTASYON KURALI (thrust.py'den, v7'de bir kez duzeltilmisti):
    rotor MILI -> elektrik makinesi (0,92) -> guc elektronigi (0,95) -> [BARA]
    motor MILI -> jenerator (0,90) -> [BARA]
Tampon BARADADIR. Talep = P_mil / (0,92 x 0,95) - P_motor x 0,90.
Rotor milinden motor milini cikarmak uc istasyonu karistirir.

TUR 56 BULGUSU: Adim 11'in "acik 0,128-0,150 kW/kg" ve Adim 12'nin
"0,166 -> 0,162" sayilari MIL - MIL cikarmasiydi, yani v7'nin kendi
duzelttigi karisiklik v8'e geri gelmisti. Bu betik bara tabaninda verir.

TALEP DURUMLARI (uc cifti gucu askinin %12,3'u -- 4 x 335 W / 10,9 kW):
    askı      T/W 1,000   yalniz burun
    kalkis    T/W 1,132   burun + dort uc cifti tam (v7 Tablo 22'nin durumu)

OLCULMUS OZGUL GUCLER (Yu ve ark. 2026, Batteries 12:317, Tablo 3 ve
10,68C testi -- references/Yu-2025_24S-NCM-battery-eVTOL-IN-FLIGHT_Batteries.pdf):
    0,724 kW/kg  24S1P test paketi, surekli (110 A)
    0,892 kW/kg  24S4P ucan sistem, surekli (440 A, 4 x 110 A'dan hesaplanmis)
    1,49  kW/kg  24S1P, 10,68C: 1394,3 Wh / 249 s / 13,5 kg -- ısıl pay 4,9 C
    4,0   kW/kg  Barrett ve ark. 2023 NIAC: "about twice that of existing batteries"

Sonuc: aero/buffer-result.txt
"""
import math
import os
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)

import baseline as BL                                     # noqa: E402
import drag_sweep as DS                                   # noqa: E402
from chain_resolve import gorev_ile                       # noqa: E402
from closure import CD0, ETA_P, kapat                     # noqa: E402

ETA_MAKINE, ETA_GE, ETA_JEN = 0.92, 0.95, 0.90
UC_PAYI = 4 * 335.0 / 10900.0                  # 0,1229 -- kalkista uc ciftleri
TALEP = {"aski": 1.0, "kalkis": 1.0 + UC_PAYI}
KAPANISLAR = (("A", "olumsuz", "alt"), ("B", "olumsuz", "ust"),
              ("C", "elverisli", "alt"), ("D", "elverisli", "ust"))
OLCULMUS = ((0.724, "24S1P surekli"), (0.892, "24S4P surekli"),
            (1.49, "24S1P 10,68C, isil pay 4,9 C"), (4.0, "NIAC tasarim varsayimi"))


def tampon_gucu(P_hover_kW, P_motor_kW, talep):
    """Barada tamponun vermesi gereken guc, kW."""
    return P_hover_kW * TALEP[talep] / (ETA_MAKINE * ETA_GE) - P_motor_kW * ETA_JEN


def kur(cd0, eta_p):
    pay = 1.1 if abs(cd0 - 0.0381) < 1e-9 else 1.0
    ld_temiz, a_carpan = DS.zincir(cd0, rotorlu=True, pay=pay)
    g = gorev_ile(eta_p)
    m = BL.mimariler(f_tampon=0.036)[0]
    m.LD_carpan = a_carpan
    return m, ld_temiz, g


def kapat_ozgul(cd0, eta_p, sp, talep="kalkis", tur=400):
    """Tampon kesri DONGUNUN ICINDE: m_tampon = tampon_gucu / sp."""
    m, ld_temiz, g = kur(cd0, eta_p)
    LD = ld_temiz * m.LD_carpan
    eta_s = g["eta_seyir"] * m.eta_carpan
    MTOW = 60.0
    for _ in range(tur):
        A = MTOW / g["disk_yuklemesi"]
        W = MTOW * BL.G
        P_h = W ** 1.5 / (g["eta_hover"] * math.sqrt(2 * BL.RHO * A)) / 1000.0
        P_s = W * g["V"] / LD / eta_s / 1000.0
        P_m = P_s * g["motor_pay"]
        f_tahrik = BL.F_TAHRIK_SABIT + P_m / BL.OZGUL_GUC / MTOW
        m_t = max(tampon_gucu(P_h, P_m, talep), 0.0) / sp
        f_t = m_t / MTOW
        f_bos = BL.ORTAK["f_govde"] + BL.ORTAK["f_aviyonik"] + f_tahrik + f_t + m.f_ek
        payda = 1.0 - f_bos - BL.ORTAK["f_yakit"]
        if payda <= 0.0:
            return None
        yeni = g["m_faydali"] / payda
        if abs(yeni - MTOW) < 1e-10:
            break
        MTOW = 0.5 * MTOW + 0.5 * yeni
    else:
        return None
    if MTOW > 2000.0:
        return None
    return dict(MTOW=MTOW, m_t=m_t, f_t=f_t, P_h=P_h, P_m=P_m)


def faydali_sabit_MTOW(cd0, eta_p, sp, MTOW, talep="kalkis"):
    """MTOW Adim 10'un kapanisinda tutulur; tampon sp'den; faydali yuk artan yer."""
    m, ld_temiz, g = kur(cd0, eta_p)
    LD = ld_temiz * m.LD_carpan
    eta_s = g["eta_seyir"] * m.eta_carpan
    A = MTOW / g["disk_yuklemesi"]
    W = MTOW * BL.G
    P_h = W ** 1.5 / (g["eta_hover"] * math.sqrt(2 * BL.RHO * A)) / 1000.0
    P_s = W * g["V"] / LD / eta_s / 1000.0
    P_m = P_s * g["motor_pay"]
    f_tahrik = BL.F_TAHRIK_SABIT + P_m / BL.OZGUL_GUC / MTOW
    m_t = tampon_gucu(P_h, P_m, talep) / sp
    f_bos_tamponsuz = BL.ORTAK["f_govde"] + BL.ORTAK["f_aviyonik"] + f_tahrik + m.f_ek
    return MTOW * (1.0 - f_bos_tamponsuz - BL.ORTAK["f_yakit"]) - m_t, m_t


if __name__ == "__main__":
    print("ADIM 14 -- TAMPON, BARA TABANINDA, ADIM 10'UN DORT KAPANISI")
    print("=" * 88)

    print("\n1. ADIM 10'UN KAPANISLARI HANGI OZGUL GUCU VARSAYIYOR? (tampon %3,6)")
    print("%-3s %8s %8s %8s %9s | %9s %9s | %9s %9s | %10s"
          % ("", "MTOW", "P_aski", "motor", "tampon", "bara aski", "sp aski",
             "bara kalk", "sp kalk", "acik/kg"))
    print("%-3s %8s %8s %8s %9s | %9s %9s | %9s %9s | %10s"
          % ("", "kg", "kW mil", "kW mil", "kg", "kW", "kW/kg", "kW", "kW/kg", "bara kW/kg"))
    gerek = {}
    for k, dk, ek in KAPANISLAR:
        r = kapat(CD0[dk], ETA_P[ek])
        mt = 0.036 * r["MTOW"]
        ba = tampon_gucu(r["P_hover"], r["motor_kW"], "aski")
        bk = tampon_gucu(r["P_hover"], r["motor_kW"], "kalkis")
        gerek[k] = (ba / mt, bk / mt, r)
        print("%-3s %8.2f %8.2f %8.2f %9.3f | %9.2f %9.2f | %9.2f %9.2f | %10.4f"
              % (k, r["MTOW"], r["P_hover"], r["motor_kW"], mt, ba, ba / mt, bk, bk / mt,
                 ba / r["MTOW"]))
    sa = [v[0] for v in gerek.values()]
    sk = [v[1] for v in gerek.values()]
    print("  gereken ozgul guc: aski %.2f-%.2f, kalkis %.2f-%.2f kW/kg" % (min(sa), max(sa), min(sk), max(sk)))
    for sp, ad in OLCULMUS:
        print("  %-34s %5.3f kW/kg -> kalkis talebi bunun %.1f-%.1f kati"
              % (ad, sp, min(sk) / sp, max(sk) / sp))
    ac = [gerek[k][0] / 1 for k in gerek]
    acik = [tampon_gucu(v[2]["P_hover"], v[2]["motor_kW"], "aski") / v[2]["MTOW"] for v in gerek.values()]
    print("  bara acigi / kg (aski): %.4f-%.4f kW/kg, yayilim %.1f %%"
          % (min(acik), max(acik), 100 * (max(acik) / min(acik) - 1)))
    mil = [(v[2]["P_hover"] - v[2]["motor_kW"]) / v[2]["MTOW"] for v in gerek.values()]
    print("  (KARSILASTIRMA: mil - mil cikarmasi %.4f-%.4f, yayilim %.1f %% -- Adim 11'in eski sayisi)"
          % (min(mil), max(mil), 100 * (max(mil) / min(mil) - 1)))

    print("\n2. SINAMA -- dongu, tamponu ozgul guctan turetince Adim 10'u uretmeli")
    for k, dk, ek in KAPANISLAR:
        r = kapat_ozgul(CD0[dk], ETA_P[ek], gerek[k][1], "kalkis")
        print("  %s  sp %.3f -> MTOW %.3f kg (Adim 10: %.3f), tampon %%%.2f"
              % (k, gerek[k][1], r["MTOW"], gerek[k][2]["MTOW"], 100 * r["f_t"]))
        if abs(r["MTOW"] - gerek[k][2]["MTOW"]) > 0.01:
            sys.exit("!! DUR -- dongu Adim 10'u uretmiyor.")
    print("  ayni.")

    print("\n3. OLCULMUS OZGUL GUCTE DONGU (kalkis talebi, yakit kesri sabit -> menzil degismez)")
    print("%-3s | %-40s %9s %9s %9s %9s" % ("", "ozgul guc", "MTOW kg", "tampon kg", "tampon %", "vs Adim10"))
    for k, dk, ek in KAPANISLAR:
        for sp, ad in OLCULMUS:
            r = kapat_ozgul(CD0[dk], ETA_P[ek], sp, "kalkis")
            if r is None:
                print("%-3s | %-40s %9s" % (k, "%.3f %s" % (sp, ad), "KAPANMADI"))
            else:
                print("%-3s | %-40s %9.1f %9.2f %9.1f %+8.1f%%"
                      % (k, "%.3f %s" % (sp, ad), r["MTOW"], r["m_t"], 100 * r["f_t"],
                         100 * (r["MTOW"] / gerek[k][2]["MTOW"] - 1)))
    print("\n   ayni, YALNIZ ASKI talebiyle (uc ciftleri tampondan beslenmezse):")
    for k, dk, ek in KAPANISLAR:
        for sp, ad in OLCULMUS[:3]:
            r = kapat_ozgul(CD0[dk], ETA_P[ek], sp, "aski")
            print("%-3s | %-40s %s" % (k, "%.3f %s" % (sp, ad),
                  "KAPANMADI" if r is None else "%.1f kg, tampon %%%.1f" % (r["MTOW"], 100 * r["f_t"])))

    print("\n4. MTOW ADIM 10'DA TUTULURSA FAYDALI YUK (13 kg idi), kalkis talebi")
    for k, dk, ek in KAPANISLAR:
        M = gerek[k][2]["MTOW"]
        s = []
        for sp, ad in OLCULMUS[:3]:
            fy, mt = faydali_sabit_MTOW(CD0[dk], ETA_P[ek], sp, M)
            s.append("%.3f: %5.1f kg (tampon %.1f)" % (sp, fy, mt))
        print("  %s  MTOW %.1f  |  %s" % (k, M, "  |  ".join(s)))

    print("\n5. ADIM 12'NIN YAYIMLANMIS CIFTI, BARA TABANINDA (aski)")
    for ad, m, ph, pm in (("hafif", 50.1, 10.9, 2.6), ("agir", 1000.0, 216.2, 54.3)):
        b = tampon_gucu(ph, pm, "aski")
        print("  %-6s bara talebi %7.2f kW, kg basina %.4f kW/kg   (mil-mil: %.4f)"
              % (ad, b, b / m, (ph - pm) / m))
    h = tampon_gucu(10.9, 2.6, "aski") / 50.1
    a = tampon_gucu(216.2, 54.3, "aski") / 1000.0
    print("  degisim %.1f %%" % (100 * (a / h - 1)))
