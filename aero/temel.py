# -*- coding: utf-8 -*-
"""KARSILASTIRMALI TEMEL: ayni gorev, ayni denklemler, uc mimari.

NEDEN VAR. Makale "mimari vergi odenmiyor" diyor ama odenmedigini
gosterecek bir KARSILASTIRMA tasimiyor. Uc bagimsiz degerlendirme de
merkezi zayifligin bu oldugunu soyledi. Bu modul ayni gorevi uc mimariyle
boyutlandirir:

  A  kuyruk ustu, tamponlu seri hibrit   (makalenin konfigurasyonu)
  B  lift + cruise                        (iki tahrik grubu)
  C  tilt                                 (tek grup, egme mekanizmasi)

ILKE. Uydurulan kesir yok. Mimariler arasindaki her fark ya
  (i) makalenin alintiladigi bir OLCUMDEN gelir, ya da
  (ii) parametre olarak acikta birakilir ve sonucun ona duyarliligi
       gosterilir.
Ortak olan her sey (govde, aviyonik, gorev, enerji zinciri, kanat
yuklemesi) UC MIMARIDE DE AYNIDIR; yoksa karsilastirma anlamsiz olur.

DENKLEMLER (hepsi makalede zaten var)
  kapali cevrim kutle   MTOW = m_faydali / (1 - f_bos - f_enerji)      3.2
  hover gucu            P_hover = W^1.5 / (eta sqrt(2 rho A))          3.2
  menzil                R = f_yakit E* eta_zincir (L/D) / g            6.1

OLCULMUS CIPALAR (makale 3.3, ruzgar tuneli)
  temiz govde                            L/D ~ 17
  hover donanimi takili, pervane hizali  L/D ~ 13   -> ceyrek kayip
  hover donanimi takili, pervane dik     L/D ~  9
  ikinci govde: 11 (toplanmis) / 8 (acik)
  geri cekme mekanizmasi = arac kutlesinin %5'i                        3.5
"""
import math

G, RHO = 9.81, 1.225

# --- gorev ve ortak varsayimlar (UC MIMARIDE DE AYNI) --------------------
GOREV = dict(
    m_faydali=13.0,        # kg -- 6.2'nin hafif hattinin faydali yuku
    V=30.0,                # m/s seyir
    kanat_yuklemesi=25.3,  # kg/m2  (6.2)
    disk_yuklemesi=44.2,   # kg/m2  (6.2)
    Estar=12.9 * 3.6e6,    # J/kg yakit
    eta_zincir=0.176,      # yakittan itkiye (6.1)
    # Hover ve seyir verimleri AYNI DEGILDIR ve ikisi de 6.2'den geri
    # cozulmustur; model once makalenin kendi tasarimini yeniden
    # uretmeli, ancak ondan sonra baskasini karsilastirabilir.
    #   hover:  P = W^1.5/(FoM sqrt(2 rho A)) = 10,9 kW  ->  FoM = 0,599
    #   seyir:  P_el = W V/(L/D)/eta          =  1,7 kW  ->  eta  = 0,721
    #   motor derecelendirmesi = 2,6/1,7 = 1,53 x seyir elektrik gucu
    #     (jenerator, guc elektronigi ve pay dahil)
    eta_hover=0.599,
    eta_seyir=0.721,
    motor_pay=1.53,
)

# --- ortak kutle kesirleri (mimariden BAGIMSIZ olanlar) -----------------
ORTAK = dict(f_govde=0.30, f_aviyonik=0.08, f_yakit=0.16)

# Tahrik zinciri kutlesi SABIT DEGILDIR; kurulu guce baglidir. Bunu
# ayirmamak Bill 3'u gorunmez yapar: A'nin motoru 1,6 kW, C'ninki 10,8 kW
# olurken ikisine de ayni kesri vermek, makalenin merkezi iddiasini
# olcememek demektir.
#
#   m_tahrik = f_tahrik_sabit * MTOW  +  P_kurulu / OZGUL_GUC
#
# f_tahrik_sabit: pervane, mil, montaj, kablolama -- guce zayif bagli.
# OZGUL_GUC: bu sinifta ice tepmeli motor + jeneratorun ozgul gucu.
# 6.2'nin butcesinden geri cozuldu: A'nin toplam tahrik kesri 0,16 ve
# motoru 2,6 kW; ozgul guc 1,0 kW/kg alinirsa sabit kismi 0,108 kalir.
OZGUL_GUC = 1.0        # kW/kg -- kucuk ice tepmeli motor + jenerator
#
# F_TAHRIK_SABIT, 6.2'nin butcesinden GERI COZULDU ve modelin dogrulamasi
# budur: A mimarisi bu degerle makalenin 50,0 kg'ini yeniden uretmelidir.
# 6.2: toplam tahrik kesri 0,16, motor 2,6 kW, MTOW 50 kg.
#   0,16 - (2,6 kW / 1,0 kW/kg) / 50 kg = 0,108
F_TAHRIK_SABIT = 0.108


class Mimari:
    """Bir mimarinin ortaktan FARKLARI. Her alan bir gerekce tasir."""

    def __init__(self, ad, f_tahrik, f_tampon, LD_carpan, motor_hover,
                 f_ek=0.0, ek_ad="", gerekce=""):
        self.ad = ad
        self.f_tahrik = f_tahrik      # tahrik zinciri kutle kesri
        self.f_tampon = f_tampon      # batarya/tampon kesri
        self.f_ek = f_ek              # mimariye ozgu ek kutle
        self.ek_ad = ek_ad
        self.LD_carpan = LD_carpan    # temiz L/D'ye gore carpan
        self.motor_hover = motor_hover  # motor hover'a mi boyutlaniyor
        self.gerekce = gerekce

    def f_bos(self):
        """Yalnizca guce BAGLI OLMAYAN kalemler. Tahrik kutlesi
        boyutlandir() icinde kurulu guce gore hesaplanir."""
        return (ORTAK["f_govde"] + ORTAK["f_aviyonik"]
                + F_TAHRIK_SABIT + self.f_tampon + self.f_ek)


def boyutlandir(m, LD_temiz, g=GOREV, tur=60):
    """Kapali cevrim, YINELEMELI.

    Motor kutlesi kurulu guce, kurulu guc MTOW'a, MTOW da motor
    kutlesine bagli oldugu icin cozum yinelemelidir. Sabit nokta
    aranir; yakinsamazsa mimari kapanmiyor demektir."""
    LD = LD_temiz * m.LD_carpan
    MTOW = g["m_faydali"] / 0.26          # baslangic tahmini
    for _ in range(tur):
        S = MTOW / g["kanat_yuklemesi"]
        A = MTOW / g["disk_yuklemesi"]
        W = MTOW * G
        P_hover = W ** 1.5 / (g["eta_hover"] * math.sqrt(2 * RHO * A))
        P_seyir = W * g["V"] / LD / g["eta_seyir"]
        P_kurulu = P_hover if m.motor_hover else P_seyir * g["motor_pay"]
        f_tahrik = F_TAHRIK_SABIT + (P_kurulu / 1000.0) / OZGUL_GUC / MTOW
        f_bos = (ORTAK["f_govde"] + ORTAK["f_aviyonik"] + f_tahrik
                 + m.f_tampon + m.f_ek)
        payda = 1.0 - f_bos - ORTAK["f_yakit"]
        if payda <= 0:
            return dict(mimari=m.ad, kapanmadi=True, f_bos=f_bos)
        yeni = g["m_faydali"] / payda
        if abs(yeni - MTOW) < 1e-9:
            MTOW = yeni
            break
        MTOW = 0.5 * MTOW + 0.5 * yeni     # gevsetilmis yineleme
    else:
        return dict(mimari=m.ad, kapanmadi=True, f_bos=f_bos)
    R = (ORTAK["f_yakit"] * g["Estar"] * g["eta_zincir"] * LD / G) / 1000.0
    return dict(mimari=m.ad, MTOW=MTOW, S=S, A=A, LD=LD,
                P_hover=P_hover / 1000.0, P_seyir=P_seyir / 1000.0,
                motor_kW=P_kurulu / 1000.0, m_motor=(P_kurulu / 1000.0) / OZGUL_GUC,
                menzil=R, faydali_pay=g["m_faydali"] / MTOW,
                f_bos=f_bos, f_tahrik=f_tahrik, kapanmadi=False)


# --- MIMARILER ----------------------------------------------------------
#
# Ortak olan her sey ortaktir. Asagida YALNIZCA mimarinin zorladigi
# farklar var ve her birinin gerekcesi yaninda yazili.
#
# L/D carpanlari, makale 3.3'un OLCULMUS merdiveninden:
#     temiz govde 17  ->  hover donanimi takili, pervane hizali 13
#     yani  13/17 = 0,765 -- "ceyrek kayip"
# A'nin carpani, 5.2'nin kendi olcumunden: uc cerceveleri seyir
# suruklemesinin ~%12'si, yani L/D  x  1/1,12 = 0,893.
# C icin 1,0 alindi (egilen grup seyirde akisa hizali). Bu, TILT'IN
# LEHINE ve makalenin aleyhine bir secim; kasitlidir.

def mimariler(f_kaldirma_grubu=0.10, f_egme=0.05, tamponlu_hepsi=True):
    """f_kaldirma_grubu: B'nin ikinci tahrik grubunun MTOW kesri.
       f_egme:           C'nin egme mekanizmasinin MTOW kesri.
    Ikisi de OLCULMUS DEGIL -- parametredir ve taranir. f_egme'nin
    varsayilani, 3.5'te alintilanan geri cekme mekanizmasinin %5'inden
    alinmistir (mertebe capasi, esdegerlik iddiasi degil)."""
    return [
        Mimari("A  kuyruk ustu (makale)",
               f_tahrik=0.16, f_tampon=0.04, LD_carpan=1.0 / 1.12,
               motor_hover=False,
               gerekce="6.2'nin butcesi; uc cerceveleri seyir suruklemesinin %12'si"),
        Mimari("B  lift + cruise",
               f_tahrik=0.16, f_tampon=0.04, f_ek=f_kaldirma_grubu,
               ek_ad="ikinci tahrik grubu", LD_carpan=13.0 / 17.0,
               motor_hover=not tamponlu_hepsi,
               gerekce="3.3 olcumu: L/D 17 -> 13; ek grup parametre"),
        Mimari("C  tilt",
               f_tahrik=0.16, f_tampon=0.04, f_ek=f_egme,
               ek_ad="egme mekanizmasi", LD_carpan=1.0,
               motor_hover=not tamponlu_hepsi,
               gerekce="seyirde acik hover donanimi yok; mekanizma parametre"),
    ]


def tablo(f_kaldirma_grubu=0.10, f_egme=0.05, tamponlu_hepsi=True,
          LD_temiz=13.44):
    """LD_temiz varsayilani: 6.2'nin L/D 12,0'i, A'nin cerceve cezasi
    geri alinarak temiz govdeye cevrilmis (12,0 x 1,12)."""
    print("gorev: %.0f kg faydali, %.0f m/s, kanat yuklemesi %.1f kg/m2"
          % (GOREV["m_faydali"], GOREV["V"], GOREV["kanat_yuklemesi"]))
    print("guc sistemi: %s"
          % ("UCUNDE DE tamponlu seri hibrit (Bill 3 notrlendi)"
             if tamponlu_hepsi else "mimariye ozgu (Bill 3 acik)"))
    print("temiz govde L/D = %.2f" % LD_temiz)
    print()
    print("  %-24s %7s %7s %8s %8s %9s %7s %8s"
          % ("mimari", "f_bos", "MTOW", "L/D", "P_hov", "motor", "m_mot", "menzil"))
    print("  %-24s %7s %7s %8s %8s %9s %7s %8s"
          % ("", "", "kg", "", "kW", "kW", "kg", "km"))
    cik = []
    for m in mimariler(f_kaldirma_grubu, f_egme, tamponlu_hepsi):
        r = boyutlandir(m, LD_temiz)
        cik.append(r)
        if r["kapanmadi"]:
            print("  %-24s %7.3f  KAPANMADI (f_bos + f_yakit >= 1)"
                  % (m.ad, r["f_bos"]))
            continue
        print("  %-24s %7.3f %7.1f %8.2f %8.1f %9.1f %7.1f %8.0f"
              % (r["mimari"], r["f_bos"], r["MTOW"], r["LD"],
                 r["P_hover"], r["motor_kW"], r["m_motor"], r["menzil"]))
    return cik


def basabas(LD_temiz=13.44, tamponlu_hepsi=True):
    """B'nin ikinci tahrik grubu NE KADAR HAFIF olsaydi A'yi yakalardi?

    Menzil L/D ile dogru orantili ve L/D mimariden geliyor; kutle ise
    faydali yuk payini belirliyor. Iki olcut ayri ayri aranir."""
    A = boyutlandir(mimariler(0, 0, tamponlu_hepsi)[0], LD_temiz)
    print("A: menzil %.0f km, faydali pay %.3f, MTOW %.1f kg"
          % (A["menzil"], A["faydali_pay"], A["MTOW"]))
    print()
    print("  B'nin ek grup kesri -> MTOW, faydali pay, menzil")
    print("  %8s %8s %9s %9s %10s" % ("f_ek", "MTOW", "faydali", "menzil", "A'ya gore"))
    for f in (0.0, 0.02, 0.05, 0.08, 0.10, 0.15, 0.20):
        r = boyutlandir(mimariler(f, 0, tamponlu_hepsi)[1], LD_temiz)
        if r["kapanmadi"]:
            print("  %8.3f  KAPANMADI" % f); continue
        print("  %8.3f %8.1f %9.3f %9.0f %9.1f%%"
              % (f, r["MTOW"], r["faydali_pay"], r["menzil"],
                 100 * (r["menzil"] - A["menzil"]) / A["menzil"]))
    print()
    print("  NOT: B'nin menzili f_ek'ten BAGIMSIZ -- menzil yalnizca L/D'ye")
    print("  ve yakit kesrine bagli. Ek kutle MTOW'u ve faydali yuk PAYINI")
    print("  degistirir, menzili degil. Iki olcut ayri okunmalidir.")


if __name__ == "__main__":
    print("=" * 78)
    print("DUZEY 1 -- ayni guc sistemi (Bill 3 notrlendi, A'nin aleyhine)")
    print("=" * 78)
    tablo(tamponlu_hepsi=True)
    print()
    print("=" * 78)
    print("DUZEY 2 -- mimariye ozgu guc sistemi (Bill 3 acik)")
    print("=" * 78)
    tablo(tamponlu_hepsi=False)
    print()
    print("=" * 78)
    print("BASABAS")
    print("=" * 78)
    basabas()
