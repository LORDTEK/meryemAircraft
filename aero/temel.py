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

    def __init__(self, ad, f_tampon, LD_carpan, motor_hover,
                 f_ek=0.0, ek_ad="", eta_carpan=1.0, f_govde_ek=0.0,
                 gerekce=""):
        self.ad = ad
        self.f_tampon = f_tampon      # batarya/tampon kesri
        self.f_ek = f_ek              # mimariye ozgu ek kutle
        self.ek_ad = ek_ad
        self.LD_carpan = LD_carpan    # temiz L/D'ye gore carpan
        self.eta_carpan = eta_carpan  # seyir itki veriminin carpani
        self.f_govde_ek = f_govde_ek  # mimariye ozgu YAPISAL ek kesir
        self.motor_hover = motor_hover  # motor hover'a mi boyutlaniyor
        self.gerekce = gerekce


def boyutlandir(m, LD_temiz, g=GOREV, tur=60):
    """Kapali cevrim, YINELEMELI.

    Motor kutlesi kurulu guce, kurulu guc MTOW'a, MTOW da motor
    kutlesine bagli oldugu icin cozum yinelemelidir. Sabit nokta
    aranir; yakinsamazsa mimari kapanmiyor demektir."""
    LD = LD_temiz * m.LD_carpan
    eta_s = g["eta_seyir"] * m.eta_carpan
    f_govde = ORTAK["f_govde"] + m.f_govde_ek
    MTOW = g["m_faydali"] / 0.26          # baslangic tahmini
    for _ in range(tur):
        S = MTOW / g["kanat_yuklemesi"]
        A = MTOW / g["disk_yuklemesi"]
        W = MTOW * G
        P_hover = W ** 1.5 / (g["eta_hover"] * math.sqrt(2 * RHO * A))
        P_seyir = W * g["V"] / LD / eta_s
        P_kurulu = P_hover if m.motor_hover else P_seyir * g["motor_pay"]
        f_tahrik = F_TAHRIK_SABIT + (P_kurulu / 1000.0) / OZGUL_GUC / MTOW
        f_bos = (f_govde + ORTAK["f_aviyonik"] + f_tahrik
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
                menzil=R, faydali_pay=g["m_faydali"] / MTOW, eta_seyir=eta_s,
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

def mimariler(f_kaldirma_grubu=0.10, f_egme=0.05, tamponlu_hepsi=True,
              C_LD=1.00, C_eta=1.00, B_govde_ek=0.00):
    """f_kaldirma_grubu: B'nin ikinci tahrik grubunun MTOW kesri.
       f_egme:           C'nin egme mekanizmasinin MTOW kesri.
       C_LD, C_eta:      C'nin seyir L/D ve itki verimi carpanlari.
       B_govde_ek:       B'nin ek YAPISAL kesri.
    Hicbiri OLCULMUS DEGIL -- hepsi parametredir ve taranir. f_egme'nin
    varsayilani, 3.5'te alintilanan geri cekme mekanizmasinin %5'inden
    alinmistir (mertebe capasi, esdegerlik iddiasi degil).

    C_LD = C_eta = 1,00 varsayilani, tilt'in seyirde HICBIR aerodinamik
    veya itki cezasi odemedigi IDEALLESTIRILMIS UST SINIRDIR. Sonuc
    olarak degil, sinir olarak okunmalidir; duyarlilik icin
    duyarlilik_C()."""
    return [
        Mimari("A  kuyruk ustu (makale)",
               f_tampon=0.04, LD_carpan=1.0 / 1.12,
               motor_hover=False,
               gerekce="6.2'nin butcesi; uc cerceveleri seyir suruklemesinin %12'si"),
        Mimari("B  lift + cruise",
               f_tampon=0.04, f_ek=f_kaldirma_grubu,
               ek_ad="ikinci tahrik grubu", LD_carpan=13.0 / 17.0,
               f_govde_ek=B_govde_ek,
               motor_hover=not tamponlu_hepsi,
               gerekce="3.3 olcumu: L/D 17 -> 13; ek grup ve yapisal ek parametre"),
        Mimari("C  tilt",
               f_tampon=0.04, f_ek=f_egme,
               ek_ad="egme mekanizmasi", LD_carpan=C_LD, eta_carpan=C_eta,
               motor_hover=not tamponlu_hepsi,
               gerekce="IDEALLESTIRILMIS: seyirde sifir tilt cezasi varsayimi"),
    ]


def tablo(f_kaldirma_grubu=0.10, f_egme=0.05, tamponlu_hepsi=True,
          LD_temiz=13.44, C_LD=1.00, C_eta=1.00, B_govde_ek=0.00):
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
    for m in mimariler(f_kaldirma_grubu, f_egme, tamponlu_hepsi,
                       C_LD, C_eta, B_govde_ek):
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


# --- KARSILASTIRMA SOZLESMELERI --------------------------------------
#
# Ucuncu bir bagimsiz denetim (YZ3) ilk ikisinin kacirdigi bir seyi
# gordu ve haklı: menzil formulu
#     R = f_yakit E* eta_zincir (L/D) / g
# sabit f_yakit altinda MTOW'dan BAGIMSIZ. Formul dogru (Breguet'nin
# kesir bicimi), ama MIMARI KARSILASTIRMASI icin tehlikeli bir
# sozlesmedir: daha agir mimari, ayni kesri korudugu icin orantili
# olarak DAHA FAZLA YAKIT tasir. Kutle faturasi menzilden silinir.
#
# Genel bicim:  R = (E* eta_zincir / g) (L/D) (m_yakit / MTOW)
#   sabit kesir   -> m_yakit/MTOW sabit -> R MTOW'dan bagimsiz
#   sabit kutle   -> R  ~  (L/D) / MTOW      <- kutle cezasi geri gelir
#   sabit MTOW    -> f_yakit = 1 - f_bos - m_faydali/MTOW
#
# Uc sozlesme de raporlanmadan "C daha iyi menzil veriyor" denemez.

def menzil_ver(LD, f_yakit, g=GOREV):
    return (f_yakit * g["Estar"] * g["eta_zincir"] * LD / G) / 1000.0


def sabit_MTOW(m, LD_temiz, MTOW, g=GOREV):
    """Sabit MTOW ve sabit faydali yuk: yakit ARTAN yerdir.

    Yineleme yok -- MTOW verili. f_yakit negatif cikarsa mimari o
    MTOW'da bu gorevi kapatamaz."""
    LD = LD_temiz * m.LD_carpan
    eta_s = g["eta_seyir"] * m.eta_carpan
    A = MTOW / g["disk_yuklemesi"]
    W = MTOW * G
    P_hover = W ** 1.5 / (g["eta_hover"] * math.sqrt(2 * RHO * A))
    P_seyir = W * g["V"] / LD / eta_s
    P_kurulu = P_hover if m.motor_hover else P_seyir * g["motor_pay"]
    f_tahrik = F_TAHRIK_SABIT + (P_kurulu / 1000.0) / OZGUL_GUC / MTOW
    f_bos = (ORTAK["f_govde"] + m.f_govde_ek + ORTAK["f_aviyonik"]
             + f_tahrik + m.f_tampon + m.f_ek)
    f_yakit = 1.0 - f_bos - g["m_faydali"] / MTOW
    return dict(mimari=m.ad, MTOW=MTOW, LD=LD, f_bos=f_bos, f_yakit=f_yakit,
                menzil=menzil_ver(LD, f_yakit, g) if f_yakit > 0 else float("nan"),
                kapanmadi=f_yakit <= 0)


def sabit_yakit(m, LD_temiz, m_yakit, g=GOREV, tur=200):
    """Sabit YAKIT KUTLESI: f_yakit mimariye gore degisir, MTOW kapanir."""
    LD = LD_temiz * m.LD_carpan
    eta_s = g["eta_seyir"] * m.eta_carpan
    MTOW = g["m_faydali"] / 0.26
    for _ in range(tur):
        A = MTOW / g["disk_yuklemesi"]
        W = MTOW * G
        P_hover = W ** 1.5 / (g["eta_hover"] * math.sqrt(2 * RHO * A))
        P_seyir = W * g["V"] / LD / eta_s
        P_kurulu = P_hover if m.motor_hover else P_seyir * g["motor_pay"]
        f_tahrik = F_TAHRIK_SABIT + (P_kurulu / 1000.0) / OZGUL_GUC / MTOW
        f_bos = (ORTAK["f_govde"] + m.f_govde_ek + ORTAK["f_aviyonik"]
                 + f_tahrik + m.f_tampon + m.f_ek)
        yeni_MTOW = (g["m_faydali"] + m_yakit) / (1.0 - f_bos)
        if abs(yeni_MTOW - MTOW) < 1e-9:
            MTOW = yeni_MTOW
            break
        MTOW = 0.5 * MTOW + 0.5 * yeni_MTOW
    else:
        return dict(mimari=m.ad, kapanmadi=True, f_bos=f_bos)
    f_yakit = m_yakit / MTOW
    return dict(mimari=m.ad, MTOW=MTOW, LD=LD, f_bos=f_bos, f_yakit=f_yakit,
                m_yakit=m_yakit, menzil=menzil_ver(LD, f_yakit, g),
                kapanmadi=False)


def sozlesmeler(LD_temiz=13.44, C_LD=1.00, C_eta=1.00, f_egme=0.05,
                f_kaldirma_grubu=0.10):
    """Uc sozlesme yan yana. A her zaman payda."""
    ms = mimariler(f_kaldirma_grubu, f_egme, True, C_LD, C_eta)
    ref = boyutlandir(ms[0], LD_temiz)
    m_yakit_A = ORTAK["f_yakit"] * ref["MTOW"]
    MTOW_A = ref["MTOW"]
    print("Referans A: MTOW %.1f kg, yakit %.2f kg, L/D %.2f, menzil %.0f km"
          % (MTOW_A, m_yakit_A, ref["LD"], ref["menzil"]))
    print("C'nin carpanlari: L/D x%.2f, eta x%.2f" % (C_LD, C_eta))
    print()
    baslik = ("1) sabit yakit KESRI (%0,16)",
              "2) sabit yakit KUTLESI (%.2f kg)" % m_yakit_A,
              "3) sabit MTOW (%.1f kg) + sabit faydali yuk" % MTOW_A)
    hesap = (lambda m: boyutlandir(m, LD_temiz),
             lambda m: sabit_yakit(m, LD_temiz, m_yakit_A),
             lambda m: sabit_MTOW(m, LD_temiz, MTOW_A))
    for ad, f in zip(baslik, hesap):
        print(ad)
        print("  %-24s %8s %8s %9s %10s" % ("", "MTOW", "f_yakit", "menzil", "A'ya gore"))
        taban = None
        for m in ms:
            r = f(m)
            if r.get("kapanmadi"):
                print("  %-24s  KAPANMADI (f_bos %.3f)" % (m.ad, r["f_bos"]))
                continue
            if taban is None:
                taban = r["menzil"]
            print("  %-24s %8.1f %8.3f %9.0f %+9.1f%%"
                  % (m.ad, r["MTOW"], r.get("f_yakit", ORTAK["f_yakit"]),
                     r["menzil"], 100 * (r["menzil"] - taban) / taban))
        print()


def duyarlilik_C(LD_temiz=13.44, f_egme=0.05):
    """C'nin menzil ustunlugu HANGI VARSAYIMDAN geliyor?

    Iki bagimsiz denetim de ayni yere isaret etti: C'ye hem temiz L/D
    (carpan 1,00) hem A'nin seyir itki verimi veriliyor. Ikisi de
    P_seyir'de CARPILIYOR ve menzil L/D ile dogru orantili; ikisini
    birden bagislamak tilt'in seyir faturasini tamamen kapatir.

    Fiziksel gerekce (olculmedi, bu yuzden taraniyor):
      L/D  -- nasel/poyra/boslugu, aktuator cikintisi, girisim
      eta  -- pal hover'a boyutlanmis (yuksek disk yuku, yanlis burulma)
              -> seyirde A'nin pervanesinden IYI olmasi beklenmez

    Tablo A'nin menziline gore yuzde farki verir. Isaret degistigi yer,
    iddianin dayandigi esiktir."""
    A = boyutlandir(mimariler()[0], LD_temiz)
    print("A (kuyruk ustu): menzil %.0f km, MTOW %.1f kg, L/D %.2f"
          % (A["menzil"], A["MTOW"], A["LD"]))
    print("C'nin A'ya gore menzili (yuzde), egme kesri %.2f" % f_egme)
    print()
    etalar = (1.00, 0.95, 0.90, 0.85)
    print("  %-10s" % "L/D carp." + "".join("  eta x%.2f" % e for e in etalar))
    for cld in (1.00, 0.96, 0.92, 0.88, 0.85):
        satir = "  %-10.2f" % cld
        for ce in etalar:
            r = boyutlandir(mimariler(f_egme=f_egme, C_LD=cld, C_eta=ce)[2],
                            LD_temiz)
            if r["kapanmadi"]:
                satir += "     KAPAN"; continue
            satir += "   %+7.1f" % (100 * (r["menzil"] - A["menzil"]) / A["menzil"])
        print(satir)
    print()
    print("  NOT: menzil eta'dan BAGIMSIZ (R = f_yakit E* eta_zincir (L/D)/g).")
    print("  eta yalnizca kurulu gucu ve dolayisiyla MTOW'u degistirir.")
    print("  C'nin menzil ustunlugu bu yuzden TEK BASINA L/D carpanindan")
    print("  gelir; esik carpan ~0,89'dur (A'nin kendi 1/1,12 cezasi).")
    print()
    print("  Ayni tarama MTOW icin (kg) -- eta burada etkili:")
    print("  %-10s" % "L/D carp." + "".join("  eta x%.2f" % e for e in etalar))
    for cld in (1.00, 0.92, 0.88):
        satir = "  %-10.2f" % cld
        for ce in etalar:
            r = boyutlandir(mimariler(f_egme=f_egme, C_LD=cld, C_eta=ce)[2],
                            LD_temiz)
            satir += "   %7.1f" % (r["MTOW"] if not r["kapanmadi"] else float("nan"))
        print(satir)
    print("  (A: %.1f kg)" % A["MTOW"])


def duyarlilik_B(LD_temiz=13.44, f_kaldirma_grubu=0.10):
    """B'ye A ile ayni yapisal kesri (%30) vermek B'yi kayiriyor mu?

    Iki denetim de haklı olarak isaret etti: dagitilmis kaldirma
    kanadi, motor yataklarini ve kablolamayi da agirlastirir; B'nin
    yapisal kesri A'ninkiyle ayni olmamaliydi. Tarama, bunun sonucun
    YONUNU degistirip degistirmedigini gosterir."""
    A = boyutlandir(mimariler()[0], LD_temiz)
    print("B'nin ek YAPISAL kesri -- A: f_bos %.3f, MTOW %.1f kg, menzil %.0f km"
          % (A["f_bos"], A["MTOW"], A["menzil"]))
    print("  %10s %8s %8s %9s %10s" % ("f_govde_ek", "f_bos", "MTOW", "menzil", "faydali"))
    for fg in (0.00, 0.02, 0.04, 0.06, 0.08):
        r = boyutlandir(mimariler(f_kaldirma_grubu, B_govde_ek=fg)[1], LD_temiz)
        if r["kapanmadi"]:
            print("  %10.2f %8.3f  KAPANMADI" % (fg, r["f_bos"])); continue
        print("  %10.2f %8.3f %8.1f %9.0f %10.3f"
              % (fg, r["f_bos"], r["MTOW"], r["menzil"], r["faydali_pay"]))
    print()
    print("  Menzil f_govde_ek'ten BAGIMSIZ; ek yapisal kutle yalnizca MTOW'u")
    print("  ve faydali yuk PAYINI kotulestirir. Yani bu eksiklik gercektir")
    print("  ama A > B sonucunun YONUNU degistirmez, guclendirir.")


def agir_ayarsiz():
    """Agir hat, HICBIR yeniden ayar olmadan -- motor payi da 1,529.

    agir_dogrula() motor payini 6.3'un kendi sayilarindan (1,385)
    aliyor; bu, 'tek bir sayi bile degistirilmedi' iddiasiyla celisir.
    Bu fonksiyon o istisnayi da kaldirir: hafif hattin 1,529'u kullanilir.
    Ikisinin farki, makalenin belirtilmemis olcek etkisinin buyuklugudur."""
    g = agir_gorev()
    g["motor_pay"] = GOREV["motor_pay"]          # 1,53 -- hafif hattin payi
    r = boyutlandir(mimariler()[0], AGIR["LD_temiz"], g=g)
    print("AGIR HAT -- TEK BIR SAYI BILE DEGISTIRILMEDI (motor payi 1,53)")
    print("  %-12s %10s %10s %8s" % ("", "model", "makale", "fark"))
    for ad, h, mk in (("MTOW kg", r["MTOW"], 1000.0), ("L/D", r["LD"], 13.6),
                      ("P_hover kW", r["P_hover"], 216.2),
                      ("motor kW", r["motor_kW"], 54.3),
                      ("menzil km", r["menzil"], 1814.0),
                      ("f_tahrik", r["f_tahrik"], 0.16)):
        print("  %-12s %10.3f %10.3f %+7.1f%%" % (ad, h, mk, 100 * (h - mk) / mk))
    print()
    print("  Motor %+.1f%% sapiyor. Sebep makalenin kendi icinde:" %
          (100 * (r["motor_kW"] - 54.3) / 54.3))
    print("  hafif hatta 2,6/1,7 = 1,529, agir hatta 54,3/39,2 = 1,385")
    print("  (yuzde 10,4 fark). Makale bunu HICBIR YERDE gerekcelendirmiyor.")
    print("  Menzil ve L/D bu istisnadan etkilenmiyor: %+.1f%% ve %+.1f%%."
          % (100 * (r["menzil"] - 1814.0) / 1814.0,
             100 * (r["LD"] - 13.6) / 13.6))


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


# --- AGIR HAT (1000 kg) -- modelin BAGIMSIZ sinamasi -------------------
#
# Model hafif hatta (50 kg) kalibre edildi. Ayni katsayilarla, HICBIR
# yeniden ayar yapmadan agir hat bilinebiliyor mu? Bilebiliyorsa model
# 20 kat kutle araliginda dogrulanmis olur.
#
# BULGU: bilebiliyor, ama makalenin motor derecelendirme payi iki
# tasarimda AYNI DEGIL:
#     hafif hat  2,6 / 1,7  = 1,529
#     agir hat  54,3 / 39,2 = 1,385      -> %10,4 fark
# Hafif hattin payiyla motor %16,9 sapiyor; agir hattin kendi payiyla
# her sey %3,5 icinde kapaniyor. Yani model dogru, makalede
# BELIRTILMEMIS bir olcek etkisi (ya da tutarsizlik) var. Buyuk
# jenerator ve guc elektroniginin daha verimli olmasi fiziksel olarak
# savunulabilir, ama makale bunu hicbir yerde soylemiyor.

AGIR = dict(V=40.0, kanat_yuklemesi=45.0, disk_yuklemesi=43.7,
            m_faydali=260.0, motor_pay=54.3 / 39.2, LD_temiz=13.6 * 1.12)


def agir_gorev():
    g = dict(GOREV)
    g.update({k: v for k, v in AGIR.items() if k != "LD_temiz"})
    return g


def agir_dogrula():
    g = agir_gorev()
    r = boyutlandir(mimariler()[0], AGIR["LD_temiz"], g=g)
    print("AGIR HAT -- hafif hatta kalibre edilmis model, yeniden ayar yok")
    print("  (tek istisna: motor payi 6.3'un kendi sayilarindan, 1,385)")
    print("  %-12s %10s %10s %8s" % ("", "model", "makale", "fark"))
    for ad, h, mk in (("MTOW kg", r["MTOW"], 1000.0), ("L/D", r["LD"], 13.6),
                      ("P_hover kW", r["P_hover"], 216.2),
                      ("motor kW", r["motor_kW"], 54.3),
                      ("menzil km", r["menzil"], 1814.0),
                      ("f_tahrik", r["f_tahrik"], 0.16)):
        print("  %-12s %10.3f %10.3f %+7.1f%%" % (ad, h, mk, 100 * (h - mk) / mk))


def agir_tablo():
    g = agir_gorev()
    print("  %-24s %7s %8s %8s %8s %9s"
          % ("mimari", "f_bos", "MTOW", "L/D", "P_hov", "menzil"))
    for m in mimariler():
        r = boyutlandir(m, AGIR["LD_temiz"], g=g)
        if r["kapanmadi"]:
            print("  %-24s %7.3f  KAPANMADI" % (m.ad, r["f_bos"])); continue
        print("  %-24s %7.3f %8.1f %8.2f %8.1f %9.0f"
              % (r["mimari"], r["f_bos"], r["MTOW"], r["LD"],
                 r["P_hover"], r["menzil"]))


if __name__ == "__main__":
    print("=" * 78)
    print("DUZEY 1 -- ayni guc sistemi (Bill 3 notrlendi, A'nin aleyhine)")
    print("=" * 78)
    tablo(tamponlu_hepsi=True)
    print()
    print("=" * 78)
    print("DUZEY 2 -- KORKULUK, adil karsilastirma DEGIL")
    print("  (ucunde de motor hover'a boyutlaniyor, tampon yok. Gercek bir")
    print("   lift+cruise kaldirmayi bataryayla yapar; bu tablo o mimariyi")
    print("   temsil etmez, yalnizca tamponsuz bir seri hibritin ne")
    print("   olacagini gosterir.)")
    print("=" * 78)
    tablo(tamponlu_hepsi=False)
    print()
    print("=" * 78)
    print("C'NIN USTUNLUGU HANGI VARSAYIMDAN GELIYOR")
    print("=" * 78)
    duyarlilik_C()
    print()
    print("=" * 78)
    print("B'YE ORTAK YAPISAL KESIR VERMEK")
    print("=" * 78)
    duyarlilik_B()
    print()
    print("=" * 78)
    print("BASABAS")
    print("=" * 78)
    basabas()
    print()
    print("=" * 78)
    print("AGIR HAT (1000 kg) -- modelin bagimsiz sinamasi")
    print("=" * 78)
    agir_ayarsiz()
    print()
    agir_dogrula()
    print()
    print("  uc mimari, agir hat:")
    agir_tablo()
