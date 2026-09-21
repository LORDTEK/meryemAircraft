# -*- coding: utf-8 -*-
"""ADIM 10'UN GIRDI YUVASI -- ve icine dusulmesi kolay iki tuzak.

NEDEN BU DOSYA VAR. Tur 54 metninde Adim 10'un planini soyle yazdim:
    "L/De matrisinin dort kosesi, L/D'yi girdi alan baseline.py'ye
     dort girdi olarak tasinir."
ChatGPT ve Grok bagimsiz olarak bunun CIFT SAYIM olacagini soyledi.
Kod denetlendi; HAKLILAR. Bu betik dogru girdiyi sabitler.

TUZAK 1 -- L/De'yi L/D yuvasina koymak.
    baseline.py:126   R = f_yakit E* eta_zincir (L/D) / g
    baseline.py:43    eta_zincir = 0.176 = 0.2202 x 0.80
Yani eta_zincir ZATEN pervaneyi iceriyor. L/De = (L/D) eta_p'yi L/D
yuvasina koymak eta_p ile IKI KEZ carpmak demektir.

TUZAK 2 -- yalniz eta_zincir'i olceklemek. Dongude IKI verim var:
    baseline.py:111   P_seyir = W V / LD / eta_seyir      <- MOTORU BOYUTLANDIRIR
    baseline.py:126   R       = ... eta_zincir (LD) ...   <- MENZILI VERIR
eta_seyir = 0,721 de pervaneyi iceriyor (2.12'nin 1,7 kW'indan geri
cozulmus). Yalniz eta_zincir olceklenirse motor ESKI pervaneye gore
boyutlanir, menzil YENI pervaneye gore hesaplanir. Kapanis kendi icinde
tutarsiz olur -- ve bu, bu projenin tekrar tekrar dustugu hata sinifidir.

DOGRUSU ZATEN DEPODA. chain_resolve.gorev_ile(eta_p) iki terimi de
olcekliyor. Adim 10 onu yeniden kullanir; yeni bir mekanizma yazilmaz.
"""
import os
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)

import baseline as BL                                        # noqa: E402
from chain_resolve import gorev_ile, ZINCIR_PERVANESIZ       # noqa: E402

LD = {"olumsuz": 8.80, "elverisli": 10.82}     # §3.6 Tablo 9, e = 0,817
ETA_P = {"alt": 0.632, "ust": 0.683}           # dort palet ailesinin ucu ve alti
CD0 = {"olumsuz": 0.0381, "elverisli": 0.0285}  # tutarli braket; 0,0248 DISARIDA


def kurulus_sinamasi():
    """gorev_ile(0,80) makalenin yayimlanmis GOREV'ini yeniden uretmeli."""
    g = gorev_ile(0.80)
    ref = BL.GOREV
    sapmalar = {}
    for k in ("eta_zincir", "eta_seyir"):
        sapmalar[k] = abs(g[k] - ref[k]) / ref[k]
    return g, ref, sapmalar


def main():
    print("ADIM 10'UN GIRDI YUVASI")
    print("=" * 70)
    print()
    print("KURULUS SINAMASI -- gorev_ile(0,80) yayimlanan GOREV'i verir mi?")
    g, ref, sap = kurulus_sinamasi()
    for k in ("eta_zincir", "eta_seyir"):
        print("  %-12s hesaplanan %.5f   yayimlanan %.5f   sapma %.2f %%"
              % (k, g[k], ref[k], 100 * sap[k]))
    if max(sap.values()) > 0.01:
        print("  >>> DUR: kurulus yayimlanan degerleri uretmiyor.")
        raise SystemExit(1)
    print("  ok -- kurulus dogrulandi, her iki terim de %1'in icinde.")
    print()

    print("DORT KAPANIS -- her biri IKI fiziksel nicelikle beslenir:")
    print()
    print("%-4s %-11s %-7s %9s %11s %11s"
          % ("", "C_D0", "eta_p", "L/D", "eta_zincir", "eta_seyir"))
    print("-" * 60)
    ad = "ABCD"
    i = 0
    for dk, ld in (("olumsuz", LD["olumsuz"]), ("elverisli", LD["elverisli"])):
        for ek, ep in (("alt", ETA_P["alt"]), ("ust", ETA_P["ust"])):
            gg = gorev_ile(ep)
            print("%-4s %-11.4f %-7.3f %9.2f %11.5f %11.5f"
                  % (ad[i], CD0[dk], ep, ld, gg["eta_zincir"], gg["eta_seyir"]))
            i += 1
    print("-" * 60)
    print()
    print("DIKKAT: L/D sutununa AERODINAMIK oran girer (8,80 / 10,82),")
    print("        L/De (5,56 / 6,01 / 6,84 / 7,39) DEGIL. L/De yalniz")
    print("        Adim 6'nin cok rotorlu karsilastirmasinin birimidir;")
    print("        boyutlandirma dongusunun girdisi degildir.")
    print()
    print("DeepSeek'in iki sorusunun yaniti:")
    print("  1) eta_p bir GIRDI, dongu degiskeni degil -- baseline.py pervane")
    print("     boyutlandirmiyor, verimi GOREV sozlugunden aliyor.")
    print("  2) Motor boyutu dort kapanista DEGISIR, cunku P_seyir eta_seyir'e")
    print("     bagli ve eta_seyir eta_p ile olcekleniyor. Adim 10 motor")
    print("     buyuklugunun yayilimini da raporlayacak.")


if __name__ == "__main__":
    main()
