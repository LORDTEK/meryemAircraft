# -*- coding: utf-8 -*-
"""ADIM 11 -- DEFTER. ATIF, EKLEME DEGIL.

Grok ve DeepSeek ayni sarti koydu ve kabul edildi:

    Adim 10'un sayilari zaten iceriyor:
      * uc cerceveleri ve serbest donen rotorlar  -> C_D0 braketinin icinde
      * sabit hatve uzlasmasi                     -> eta_p araliginin icinde
      * burulma bedeli                            -> aciklik veriminin icinde
      * hepsinin kutle ve guc sonuclari           -> MTOW ve motor derecesinde
    Defter bunlari TEKRAR eklerse, closure_inputs.py'de yakalanan cift
    sayimin duz yazi halidir.

Bu betik hicbir sey EKLEMEZ. Kapanisin kendi sayilarini bilesenlerine
AYIRIR, ve ayrilamayan terimleri ADLANDIRIR.

DeepSeek'in ayrimi korunuyor:
    AYRISTIRILABILIR  -- C_D0 kalemleri, kutle kesirleri (hesaplandilar)
    AYRISTIRILAMAZ    -- eta_p acigi (0,80 -> 0,632-0,683) kaynak basina
                         bolunmedi; C_D0'daki girisim terimi modellenmedi
"""
import os
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)

import baseline as BL                                  # noqa: E402
import drag_sweep as DS                                # noqa: E402
from closure import kapat, CD0, ETA_P                  # noqa: E402

# drag_sweep.py'nin kendi kalemleri (satir 41-48)
TEMIZ_YUZEY = {"elverisli": 0.0073, "olumsuz": 0.0129}
GOBEK       = {"elverisli": 0.0015, "olumsuz": 0.0020}
CERCEVE, ROTOR = DS.CERCEVE, DS.ROTOR
PAY         = {"elverisli": 1.00, "olumsuz": 1.10}   # olumsuz uca %10 pay

ETA_P_YAYIMLANAN = 0.80


def cd0_dokumu(uc):
    p = PAY[uc]
    k = dict(temiz_yuzey=TEMIZ_YUZEY[uc] * p, gobek=GOBEK[uc] * p,
             cerceveler=CERCEVE * p, rotorlar=ROTOR * p)
    k["toplam"] = sum(k.values())
    return k


def main():
    print("ADIM 11 -- DEFTER: KAPANISIN ICINDE NE VAR")
    print("=" * 74)
    print()

    # ---- FATURA 2: acikta seyir suruklemesi -------------------------------
    print("FATURA 2 -- C_D0 braketinin dokumu (hicbiri eklenmiyor, ayrilyor)")
    print()
    print("%-16s %12s %12s" % ("", "elverisli", "olumsuz"))
    print("-" * 42)
    d = {u: cd0_dokumu(u) for u in ("elverisli", "olumsuz")}
    for k, ad in (("temiz_yuzey", "temiz yuzey"), ("gobek", "gobek"),
                  ("cerceveler", "UC CERCEVELERI"), ("rotorlar", "ROTORLAR"),
                  ("toplam", "toplam")):
        print("%-16s %12.4f %12.4f" % (ad, d["elverisli"][k], d["olumsuz"][k]))
    print()
    for u in ("elverisli", "olumsuz"):
        aski = d[u]["cerceveler"] + d[u]["rotorlar"]
        print("  %-10s askı donanimi = %.4f  ->  C_D0'in %%%.0f'i"
              % (u, aski, 100 * aski / d[u]["toplam"]))
    print()

    # L/D karsiligi
    print("  Ayni sey L/D olarak (drag_sweep.zincir):")
    for u, c in (("elverisli", CD0["elverisli"]), ("olumsuz", CD0["olumsuz"])):
        temiz, carpan = DS.zincir(c)
        print("    %-10s temiz govde %6.2f -> ucak %6.2f   (korunan %%%.0f, "
              "Fatura 2 = %%%.0f)" % (u, temiz, temiz * carpan,
                                      100 * carpan, 100 * (1 - carpan)))
    print()
    print("  DIKKAT: Fatura 2 ELVERISLI ucta DAHA AGIR. Temiz govde temizlendikce")
    print("  sabit rotor terimi toplamin daha buyuk bir kesri oluyor.")
    print()

    # ---- FATURA 2'nin ayrilamayan terimi ---------------------------------
    print("AYRISTIRILAMAYAN: girisim. Kalemler ayri ayri hesaplandi; rotor-yapi")
    print("ve rotor-kanat girisimi MODELLENMEDI ve bir kaleme yazilmadi.")
    print()

    # ---- SABIT HATVE: eta_p acigi ----------------------------------------
    print("SABIT HATVE UZLASMASI -- eta_p acigi (ayristirilamaz)")
    for ek, ep in ETA_P.items():
        print("  yayimlanan %.3f -> hesaplanan %.3f   acik %%%.1f"
              % (ETA_P_YAYIMLANAN, ep, 100 * (1 - ep / ETA_P_YAYIMLANAN)))
    print("  Bu acik burulma / kesit suruklemesi / akis acisi diye BOLUNMEDI.")
    print()

    # ---- FATURA 1 ve 3: kutle ve guc -------------------------------------
    print("FATURA 1 ve 3 -- kapanisin bos kutle kesrinin dokumu")
    print()
    print("%-3s %7s %8s %8s %8s %8s %8s %8s"
          % ("", "MTOW", "govde", "aviyonik", "tahrik", "TAMPON", "f_bos", "motor kW"))
    print("-" * 66)
    ad = "ABCD"
    i = 0
    satir = {}
    for dk in ("olumsuz", "elverisli"):
        for ek in ("alt", "ust"):
            r = kapat(CD0[dk], ETA_P[ek])
            satir[ad[i]] = r
            print("%-3s %7.1f %8.3f %8.3f %8.3f %8.3f %8.3f %8.2f"
                  % (ad[i], r["MTOW"], BL.ORTAK["f_govde"], BL.ORTAK["f_aviyonik"],
                     r["f_tahrik"], 0.036, r["f_bos"], r["motor_kW"]))
            i += 1
    print("-" * 66)
    print()
    print("FATURA 1 bu mimaride ayri bir kaldirma grubu DEGIL -- tampondur:")
    print("  tampon kesri 0,036 sabit; %.1f - %.1f kg arasi"
          % (0.036 * min(r["MTOW"] for r in satir.values()),
             0.036 * max(r["MTOW"] for r in satir.values())))
    print()
    print("FATURA 3 motordan kaldirildi ama ELEKTRIK YOLUNDAN kaldirilmadi:")
    for k in ("A", "D"):
        r = satir[k]
        print("  %s: motor %.2f kW (seyirle boyutlandi) ama askı %.2f kW"
              " elektrik yolundan geciyor -> orani %.1fx"
              % (k, r["motor_kW"], r["P_hover"], r["P_hover"] / r["motor_kW"]))
    print()
    print("  Tahrik kesri iki parcali: sabit %.3f + kurulu guc / %.1f kW/kg / MTOW"
          % (BL.F_TAHRIK_SABIT, BL.OZGUL_GUC))
    for k in ("A", "D"):
        r = satir[k]
        guc_payi = (r["motor_kW"] / BL.OZGUL_GUC) / r["MTOW"]
        print("    %s: sabit %.3f + guce bagli %.3f = %.3f"
              % (k, BL.F_TAHRIK_SABIT, guc_payi, r["f_tahrik"]))


if __name__ == "__main__":
    main()
