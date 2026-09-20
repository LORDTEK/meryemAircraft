# -*- coding: utf-8 -*-
"""Etkin kaldirma-surukleme orani -- NASA'nin para biriminde.

NEDEN: makale cok rotorlu karsilastirmasini iki FARKLI turden sayiyla yapiyor.
Johnson & Silva 2022, Tablo 3, turbosaft quadrotor icin L/De = 4,9 veriyor ve
belgenin adlandirma listesi bunu acikca tanimliyor:

    L/De   aircraft effective lift-to-drag ratio, WV/P      (s. 94, gosterim listesi)

Bizim 8,80--10,82 sayimiz ise AERODINAMIK L/D = L/D, yani bir kuvvet orani.
Ikisi ayni sey degil. Bu betik bizimkini NASA'nin birimine cevirir.

TUREV (elde, iki satir):
    Seyirde T = D ve L = W.
    Pervane mili gucu   P_mil = T V / eta_p = D V / eta_p
    L/De = W V / P_mil = W V eta_p / (D V) = (L/D) * eta_p

BU AYNI DUZLEM MI? Evet, ve bu VARSAYILMADI -- kaynaktan kanitlandi.

Johnson & Silva enerjiyi soyle yaziyor (denklem 2, s. 645):
    E_cruise = (Pc/eta_c) * t,   Pc = W V / (L/De)
ve eta_c'yi "the propulsion system efficiency in cruise" diye tanimliyor.
Bu tek basina belirsiz: eta_c elektrik zinciri mi, yoksa pervaneyi de kapsiyor mu?
Kapsiyorsa bizim carpanimiz eta_p'yi IKI KEZ saymis olurdu.

KANIT askidaki esdegerinden geliyor (denklem 3, s. 658):
    I = (Ph/nu)/eta_h    ve    Ph = W sqrt(W/2rhoA) / FM
Burada Ph, FM ZATEN UYGULANMIS askı gucudur -- yani MIL gucu. eta_h ise onun
DISINDA duruyor. Demek ki eta_h rotorun aerodinamik verimi degil, elektrik
zinciri verimidir; rotorun isini FM yapiyor.

Bicimsel simetriyle eta_c de seyirdeki elektrik zinciri verimidir, ve
Pc = WV/(L/De) MIL gucudur. Dolayisiyla L/De propulsor verimini ICERIR.
Bizim eta_p de pervane milinde tanimli. Ayni duzlem. Cift sayim yok.

CAPRAZ DENETIM: ters cevirip NASA araclarinin aerodinamik L/D'sini bulalim.
eta_p ~ 0,80 ile tiltwing 8,6 -> L/D ~ 10,8; lift+cruise 8,5 -> L/D ~ 10,6.
Ikisi de bu sinif icin makul. Cevrim sacma sayi uretmiyor.

GIRDILER -- hepsi depodaki dosyalardan, hicbiri uydurma:
  L/D  : paper-v7.md Tablo 9, satir 1511. Suruklemesi faturalanmis hal.
  eta_p: paper/chain-resolve-finding.md -- iki noktali BEMT sonucu.
"""

# --- Girdiler ---------------------------------------------------------------

LD = {                      # paper-v7.md satir 1511, Tablo 9
    "temiz govde":        13.40,   # satir 1502
    "yayimlanmis varsayim": 11.88,
    "bracket elverisli":  10.82,
    "bracket olumsuz":     8.80,
}

ETA_P = {                   # paper/chain-resolve-finding.md
    "makalenin varsayimi": 0.800,
    "hesaplanan ust":      0.683,
    "hesaplanan alt":      0.632,
}

NASA = {                    # cfd/1521_Johnson & Silva_122721.pdf, Tablo 3, s. 70
    "Quadrotor, turbosaft":   4.9,
    "Quadrotor, elektrik":    5.8,
    "QSMR, turbosaft":        5.4,
    "Side-by-side, turbosaft":5.9,
    "Lift+Cruise, TE":        8.5,
    "Tiltwing, TE":           8.6,
}


def lde(ld, eta_p):
    return ld * eta_p


def main():
    print("ETKIN KALDIRMA-SURUKLEME ORANI  L/De = (L/D) x eta_p")
    print("=" * 66)
    print()
    print("NASA Tablo 3 (birinci elden okundu), L/De = WV/P:")
    for k, v in NASA.items():
        print("  %-26s %5.1f" % (k, v))
    print()

    print("Bu yapilandirma -- her L/D, her eta_p:")
    print()
    print("  %-22s" % "" + "".join("%12s" % k for k in ETA_P))
    print("  %-22s" % "" + "".join("%12.3f" % v for v in ETA_P.values()))
    print("  " + "-" * 60)
    for kl, vl in LD.items():
        print("  %-22s" % ("L/D %5.2f  %s" % (vl, ""))[:22]
              + "".join("%12.2f" % lde(vl, ve) for ve in ETA_P.values())
              + "   <- " + kl)
    print()

    # Savunulabilir aralik: suruklemesi faturalanmis L/D braketi x hesaplanan eta_p
    alt = lde(LD["bracket olumsuz"], ETA_P["hesaplanan alt"])
    ust = lde(LD["bracket elverisli"], ETA_P["hesaplanan ust"])
    q = NASA["Quadrotor, turbosaft"]
    qe = NASA["Quadrotor, elektrik"]

    print("SAVUNULABILIR ARALIK (rotorlari faturalanmis L/D x hesaplanan eta_p):")
    print("  L/De = %.2f ... %.2f" % (alt, ust))
    print()
    print("  turbosaft quadrotor'a karsi (%.1f): +%.0f %% ... +%.0f %%"
          % (q, 100 * (alt / q - 1), 100 * (ust / q - 1)))
    print("  elektrik quadrotor'a karsi  (%.1f): +%.0f %% ... +%.0f %%"
          % (qe, 100 * (alt / qe - 1), 100 * (ust / qe - 1)))
    print()
    print("KARSILASTIRMA -- makalenin simdiye kadar kullandigi cift:")
    print("  aerodinamik  8,80--10,82  vs  L/De 4,9  ->  +%.0f %% ... +%.0f %%"
          % (100 * (8.80 / q - 1), 100 * (10.82 / q - 1)))
    print("  AYNI BIRIMDE 5,56-- 7,39  vs  L/De 4,9  ->  +%.0f %% ... +%.0f %%"
          % (100 * (alt / q - 1), 100 * (ust / q - 1)))
    print()
    print("Yani ayni birime cevrilince pay ciddi bicimde DARALIYOR:")
    print("  ~iki kat -> +%.0f..+%.0f %% (turbosaft quadrotor)."
          % (100 * (alt / q - 1), 100 * (ust / q - 1)))
    print()
    print("VE BIR KOSEDE ISARET DEGISIYOR. Bunu yumusatma:")
    print("  olumsuz kosemiz   L/De = %.2f" % alt)
    print("  elektrik quadrotor L/De = %.1f  -> bizden YUKSEK" % qe)
    print("  Yani 'her rotorlu araci geceriz' YANLIS. Gectigimiz, bizimle ayni")
    print("  enerji kaynagini kullanan turbosaft quadrotor'dur (4,9), her kosede.")
    print("  Elektrik quadrotor verimini 1.742 lb batarya ve ayni gorev icin")
    print("  iki kat agirlikla satin aliyor (7.221 lb / 3.678 lb) -- Fatura 1.")
    print("  Ama VERIM EKSENINDE, tek basina, bizi geciyor.")
    print()
    print("EN KOTU KOSE DENETIMI -- pay hangi noktada kapanir?")
    print("  gereken eta_p, olumsuz uctaki L/D = 8,80 ile: %.3f" % (q / 8.80))
    print("  hesaplanan en dusuk eta_p                   : %.3f" % ETA_P["hesaplanan alt"])
    print("  marj                                        : %.3f" % (ETA_P["hesaplanan alt"] - q / 8.80))


if __name__ == "__main__":
    main()
