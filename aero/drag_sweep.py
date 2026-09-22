# -*- coding: utf-8 -*-
"""SURUKLEME BRAKETINI BUTUN ZINCIRE SUPUR.

NEDEN. Makale 3.6'yi rotor terimiyle elden yeniden boyutlandirdi ama
3.7, 3.8 ve agir tasarim hala varsayilan C_D0 = 0,0248 uzerinde duruyor.
Dort dis okumanin dordu de ayni seyi soyledi: bu CFD degil, aritmetik;
gonderilmeden once yapilmali ve gunler surer, aylar degil.

UC AYRI SURUKLEME DEGERI DOLASIYORDU -- burada TEKE indiriliyor:
    0,0248   3.7, 3.8 ve asagisi (varsayilan)
    0,0401   3.6'nin fiilen kullandigi (varsayilan + rotor)
    0,0216 - 0,0380   S1'in brakети

VE S1'IN BRAKETI KENDI ICINDE TUTARSIZDI. Alt ucu 0,0085'lik rotoru
kullaniyordu -- yani 3.3'un "ucagin hover butcesi bu pervaneyi
kullanamaz" diye elediği tasarimi. DeepSeek'in yakaladigi hatanin
aynisini oteki sutunda yapmisim. Rotor terimi iki ucta da ayni olmali
ve hover sartini saglayan degerdir: 0,0154.

    tutarli braket = 0,0285 - 0,0381
    ve varsayilan 0,0248 IKI UCUN DA ALTINDA -- "braketin icinde" degil.

ZINCIR. Surukleme, boyutlandirmaya iki sayiyla giriyor: temiz govde L/D
ve mimari carpani. Ikisi de burada TEK kuruluştan turetiliyor:
    L/D(C_D0) = C_L / (C_D0 + C_Di)
    temiz govde = toplam - cerceveler - rotorlar
    A'nin carpani = L/D(toplam) / L/D(temiz)
B ve C kendi olculmus carpanlarini korur ve ayni temiz govdeye uygulanir.

SINAMA. Yayinlanan varsayimda kuruluş, yayinlanan 13,44'u yeniden
uretmelidir. Uretmezse supurme gecersizdir ve betik DURUR.
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
import baseline as T                                       # noqa: E402
import planform as P                                    # noqa: E402

CL, E_SPAN = 0.45, 0.817
CERCEVE, ROTOR = 0.0043, 0.0154
C_DI = CL * CL / (math.pi * P.olcuier()["AR"] * E_SPAN)

VARSAYILAN = 0.0248                       # 3.7/3.8'in hala kullandigi
ALT = 0.0073 + CERCEVE + 0.0015 + ROTOR   # temiz yuzey, kucuk gobek, pay yok
UST = (0.0129 + CERCEVE + 0.0020 + ROTOR) * 1.1


def ld(cd0):
    return CL / (cd0 + C_DI)


def zincir(cd0_toplam, rotorlu=True, pay=1.0):
    """Verilen toplam C_D0 -> (temiz govde L/D, A'nin carpani).

    DUZELTME, Tur 53. Grok ve DeepSeek bagimsiz olarak ayni hatayi buldu:
    olumsuz uctaki toplam ZATEN x1,1 marj tasiyor, ama bu fonksiyon cerceve
    ve rotoru MARJSIZ degerleriyle cikariyordu. Az cikarinca temiz govde
    fazla kirli goruluyor ve clean L/D dusuk cikiyordu (14,29; dogrusu 15,26).

    KAPANISA ETKISI YOKTU: carpan = ld(toplam)/ld(temiz) ve boyutlandir()
    LD = LD_temiz * carpan yapiyor, yani carpim ld(toplam)'a sadelesiyor.
    Hatali olan YALNIZ raporlanan temiz govde orani ve ondan turetilen
    "korunan yuzde" idi -- ikisi de Adim 11'de.

    pay: o uca uygulanan marj (olumsuz uc 1,1; oteki uclar 1,0).
    """
    cikar = (CERCEVE + (ROTOR if rotorlu else 0.0)) * pay
    return ld(cd0_toplam - cikar), ld(cd0_toplam) / ld(cd0_toplam - cikar)


if __name__ == "__main__":
    print("SURUKLEME BRAKETI, BUTUN ZINCIRE SUPURULUYOR")
    print("C_Di = %.4f (C_L %.2f, e %.3f, AR %.3f)"
          % (C_DI, CL, E_SPAN, P.olcuier()["AR"]))
    print()

    # --- SINAMA: yayinlanan varsayim yayinlanan temiz govdeyi uretmeli
    # Yayinlanan surumde rotor IHMAL EDILMIS sayiliyordu.
    ldt, _ = zincir(VARSAYILAN, rotorlu=False)
    print("KURULUS SINAMASI")
    print("  varsayim %.4f -> temiz govde L/D %.2f (yayinlanan 13,44)"
          % (VARSAYILAN, ldt))
    if abs(ldt - 13.44) > 0.15:
        sys.exit("!! DUR -- kurulus yayinlanan 13,44'u uretmiyor.")
    print("  fark %.2f %%, kurulus dogrulandi." % (100 * (ldt / 13.44 - 1)))
    print()

    print("TUTARLI BRAKET (rotor terimi iki ucta da 0,0154)")
    print("  alt        %.4f   L/D %.2f" % (ALT, ld(ALT)))
    print("  varsayilan %.4f   L/D %.2f   <- IKI UCUN DA ALTINDA"
          % (VARSAYILAN, ld(VARSAYILAN)))
    print("  ust        %.4f   L/D %.2f" % (UST, ld(UST)))
    print()

    noktalar = (("yayinlanan varsayim (rotor ihmal)", VARSAYILAN, False),
                ("braket ALT", ALT, True),
                ("braket UST", UST, True))
    for ad, cd0, rot in noktalar:
        ldt, carp = zincir(cd0, rotorlu=rot)
        print("=" * 72)
        print("%s   C_D0 %.4f   temiz L/D %.2f   A carpani 1/%.3f   A L/D %.2f"
              % (ad, cd0, ldt, 1 / carp, ldt * carp))
        print("=" * 72)
        T.sozlesmeler(LD_temiz=ldt, A_LD_carpan=carp)
