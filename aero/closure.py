# -*- coding: utf-8 -*-
"""KAPANMA DONGUSU -- olculmus bir pakette hafif tasarim var mi?

NEDEN VAR. 4.4 su an sunu yapiyor: 1,5 kW/kg'da tampon 6,8 kg olur,
elde 2,2 kg var, demek kapanmiyor. Bu bir CIKARMA, dongu degil. Disaridan
bir okuma bunu dogru teshis etti: agir tampon MTOW'u buyutur, MTOW hover
gucunu buyutur, hover gucu tamponu buyutur. Sabit disk yuklemesinde bu
geri besleme DOGRUSALDIR (P_hover/W sabit), yani patlamaz ama yigilir --
ve yigildigi yer tek adimlik cikarmanin gosterdigi yer degildir.

BU BETIK dongu kapatiyor. Iki ucu da veriyor:
  (a) faydali yuk 13 kg'da SABIT tutulur, MTOW nereye oturur;
  (b) MTOW 50 kg'da SABIT tutulur, faydali yuke ne kalir.

NE ALEYHIMIZE SAYILIR. Ikisi de dusunulmus:
  - (a) yakinsar ve menzil B'nin 1 370 km'sinin UZERINDE kalirsa,
    "hicbir olculmus ozgul gucte kapanmiyor" cumlesi fazla sert demektir.
    Ucak agirlasti, yok olmadi.
  - (b) faydali yuk sifira duserse ya da (a) kacarsa, 6.2'nin 50 kg /
    1 598 km satiri kosullu bir referans tasarim degil, ULASILAMAZ bir
    noktadir ve o satirla acilan her tablo bundan etkilenir.

OLCEKLEME. Kanat yuklemesi ve disk yuklemesi sabit tutulur (makalenin
kendi kurali, 3.9). Ikisi de sabitse S ~ m ve A ~ m, yani dogrusal olcek
sqrt(m/50). Hover gucu W ile DOGRUSAL buyur -- makalenin klasik L^3.5
yerine elde ettigi sonuc budur ve burada da kullanilir.

SINIR. Kutle kurulusu mass.py'nin kendisidir; bu betik onu yeni bir
tampon kutlesiyle ve yeni bir olcekle tekrar cagirir. mass.py'nin butun
sinirlari (yerel yuk girisi modellenmiyor, burkulma yok, ...) burada da
gecerlidir. Dongu kutle butcesini DUZELTMIYOR, sadece tutarli cozuyor.
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from mass import butce                                    # noqa: E402

G, RHO = 9.81, 1.225

# --- 3.7 hafif referans tasarim, dongunun capasi ---------------------
M0 = 50.0            # kg
P_HOVER0 = 10.9e3    # W, burun mil gucu, T/W = 1,00
P_MOTOR0 = 2.6e3     # W, motor mili
P_UC0 = 4 * 335.0    # W, dort uc cifti
F_YAKIT = 0.16       # menzili korumak icin yakit KESRI sabit
LD = 12.0
E_YAKIT = 12.9       # kWh/kg
ETA_ZINCIR = 0.176   # 0.28 x 0.90 x 0.95 x 0.92 x 0.80

ETA_JEN, ETA_GE, ETA_MAK = 0.90, 0.95, 0.92


def tampon_gucu(m, uclar_dahil):
    """Verilen MTOW'da barada tampondan cekilen guc (W).

    Disk yuklemesi sabit -> P_hover/W sabit -> hover gucu m ile dogrusal.
    Ayni sekilde seyir gucu ve dolayisiyla motor derecesi de.
    """
    k = m / M0
    p_saft = P_HOVER0 * k + (P_UC0 * k if uclar_dahil else 0.0)
    bara = p_saft / ETA_MAK / ETA_GE
    jen = P_MOTOR0 * k * ETA_JEN
    return bara - jen


def menzil(m_yakit, m):
    """Breguet, 3.1'in denklemi. R = f_yakit E* eta (L/D) / g."""
    return (m_yakit / m) * E_YAKIT * 3.6e6 * ETA_ZINCIR * LD / G / 1000.0


def artik(m, sigma, uclar_dahil, m_faydali=13.0):
    """Verilen MTOW'da faydali yuke kalan eksi istenen. Kok = kapanma."""
    m_pil = tampon_gucu(m, uclar_dahil) / (sigma * 1e3)
    k = m / M0
    r = butce(MTOW=m, P_hover_kW=P_HOVER0 * k / 1e3,
              P_motor_kW=P_MOTOR0 * k / 1e3, m_yakit=F_YAKIT * m,
              m_pil=m_pil, m_faydali=m_faydali, olcek=math.sqrt(m / M0),
              yaz=False)
    return r["kalan"] - m_faydali, m_pil


def coz_yuk_sabit(sigma, uclar_dahil, m_faydali=13.0, ust=5000.0):
    """(a) Faydali yuk 13 kg'da sabit; MTOW nereye oturur?

    Sabit nokta yinelemesi yerine IKIYE BOLME. Gevsetmeli yineleme
    salinabilir ve o salinim 'kacti' gibi okunur -- yani cozucunun
    kusuru fizige yazilir. Kok bulma bu ayrimi kaldiriyor: aralikta
    isaret degisimi yoksa cozum YOKTUR, cozucu yorgunlugu degil.
    """
    f0, _ = artik(M0, sigma, uclar_dahil, m_faydali)
    if f0 >= 0:                      # 50 kg'da zaten kapaniyor
        return M0, tampon_gucu(M0, uclar_dahil) / (sigma * 1e3), \
               F_YAKIT * M0, "50 kg'da zaten kapaniyor"
    alt, yuk = M0, M0
    while yuk < ust:
        yuk *= 1.25
        f, _ = artik(yuk, sigma, uclar_dahil, m_faydali)
        if f >= 0:
            break
        alt = yuk
    else:
        return None, None, None, "COZUM YOK (%.0f kg'a kadar)" % ust
    for _ in range(80):
        orta = 0.5 * (alt + yuk)
        f, _ = artik(orta, sigma, uclar_dahil, m_faydali)
        if f < 0:
            alt = orta
        else:
            yuk = orta
    m = 0.5 * (alt + yuk)
    _, m_pil = artik(m, sigma, uclar_dahil, m_faydali)
    return m, m_pil, F_YAKIT * m, "kok bulundu"


def coz_mtow_sabit(sigma, uclar_dahil, m=M0):
    """(b) MTOW 50 kg'da sabit; faydali yuke ne kalir?"""
    m_pil = tampon_gucu(m, uclar_dahil) / (sigma * 1e3)
    m_yakit = F_YAKIT * m
    r = butce(MTOW=m, P_hover_kW=P_HOVER0 / 1e3, P_motor_kW=P_MOTOR0 / 1e3,
              m_yakit=m_yakit, m_pil=m_pil, m_faydali=13.0, olcek=1.0, yaz=False)
    return r["kalan"], m_pil


def basli(s):
    print("\n" + s)
    print("-" * len(s))


HATLAR = ((0.724, "Yu vd., birim paket, surekli"),
          (0.892, "Yu vd., ucus sistemi, surekli"),
          (1.50, "Yu vd., olculmus termal tavan"),
          (2.50, "ara deger, olculmemis"),
          (5.63, "makalenin ortuk varsayimi, hover"),
          (6.48, "makalenin ortuk varsayimi, kalkis"))

if __name__ == "__main__":
    print("KAPANMA DONGUSU -- hafif tasarim, olculmus paketlerde")
    print("Yakit KESRI %.2f sabit (menzil korunsun); kanat ve disk"
          % F_YAKIT)
    print("yuklemesi sabit; hover gucu MTOW ile dogrusal.")

    for uclar, ad in ((False, "HOVER talebi (yalniz burun, T/W = 1,00)"),
                      (True, "KALKIS talebi (burun + uc ciftleri)")):
        basli("(a) faydali yuk 13 kg SABIT -- %s" % ad)
        print("%-34s %9s %9s %9s %9s  %s"
              % ("tampon kW/kg", "MTOW kg", "pil kg", "pil %", "menzil km", "durum"))
        for sigma, etiket in HATLAR:
            m, m_pil, m_yakit, durum = coz_yuk_sabit(sigma, uclar)
            if m is None:
                print("%-34s %9s %9s %9s %9s  %s"
                      % ("%.3f  %s" % (sigma, etiket), "-", "-", "-", "-", durum))
                continue
            print("%-34s %9.1f %9.2f %8.1f%% %9.0f  %s"
                  % ("%.3f  %s" % (sigma, etiket), m, m_pil,
                     100 * m_pil / m, menzil(m_yakit, m), durum))

        basli("(b) MTOW 50 kg SABIT -- %s" % ad)
        print("%-34s %12s %9s" % ("tampon kW/kg", "faydali yuk kg", "pil kg"))
        for sigma, etiket in HATLAR:
            kalan, m_pil = coz_mtow_sabit(sigma, uclar)
            print("%-34s %12.2f %9.2f" % ("%.3f  %s" % (sigma, etiket),
                                          kalan, m_pil))

    basli("Karsilastirma: 4.4'un tek adimlik cikarmasi")
    p = tampon_gucu(M0, False)
    print("50 kg'da hover tamponu %.2f kW; 1,5 kW/kg'da %.2f kg."
          % (p / 1e3, p / 1.5e3))
    print("4.4 bunu 1,8 kg ile karsilastirip farki 2,2 kg paya soruyor.")
    print("Yukaridaki (a) satiri, o payin yetmemesinin MTOW'u nereye")
    print("goturdugunu gosteriyor -- cikarmanin gostermedigi sey bu.")
