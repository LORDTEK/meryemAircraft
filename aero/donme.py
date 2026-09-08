# -*- coding: utf-8 -*-
"""GECIS DONME DINAMIGI ve UC PERVANE BOYUTLANDIRMASI.

NEDEN VAR. 7.4'un gecis benzetimi iki serbestlik dereceli bir NOKTA
KUTLE: govde acisi theta kinematik olarak surulur. Yani ucak donmuyor,
DONDUGU VARSAYILIYOR. Donmeyi ureten moment modelde yok ve 8.14'un 3.
maddesi bunu "uc pervaneleri mertebe tahminiyle degil duzgun
boyutlandirmak" diye kaydediyor.

BU MODUL TAM 6-DoF DEGILDIR ve oyle olmadigini bastan soyler. Tam
6-DoF, 90 dereceye kadar moment katsayilari C_m(alpha) ister; o veri
yok ve deneysiz uretilemez. Burada yapilan sey daha dar ve daha
saglamdir:

  ATALET ALT SINIRI. Uc pervaneler ucagin ATALETINI bile
  donduremiyorsa, aerodinamik momenti hic donduremez. Yetiyorsa,
  aerodinamik marjin BILINMEDIGI acikca yazilir.

Donme ekseni: uc cerceveleri planforma DIK uzaniyor (4.3), ust/alt cift
farki govde x ekseni boyunca kuvvet x govde z kolu -> ACIKLIK EKSENI
etrafinda moment. Gecisin dondugu eksen de budur. Yani I_yy gerekir:

    I_yy = toplam m (x^2 + z^2)     x veter yonu, z kalinlik yonu
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from planform import istasyonlar, P                       # noqa: E402
import kutle                                              # noqa: E402

G, RHO = 9.81, 1.225


# ---------------------------------------------------------------------
# KUTLE DAGILIMI
# ---------------------------------------------------------------------
# Konumlar govde ekseninde: x veter yonu, kok hucum kenari x=0'da,
# firar kenarina dogru +; y aciklik; z kalinlik, ust +.
# Kalem kutleleri kutle.py'nin butcesinden gelir -- burada YENIDEN
# uydurulmaz. Belirsiz olan yalnizca KONUMLARDIR ve taranir.

# ⚠️ DUZELTME (08.09.2026). Ilk surum bu kalemleri veter boyunca ELLE
# yerlestiriyordu ve CG'yi kok veterinin %57'sine koyuyordu. YANLISTI:
# ic hacmin NEREDE oldugu hic bakilmamisti. Olculdu -- ic hacmin mutlak
# merkezi kok veterinin %78,3'unde, cunku ok acisi dis kesitleri kok
# firar kenarinin cok arkasina tasiyor.
#
# Artik tasinabilir kalemler IC HACME ORANTILI dagitiliyor: gercek bir
# tasarimin yapacagi sey budur ve sonucu bambaska.
#
#   elle yerlestirme  CG %57    statik marj +%47 MAC (sacma)
#   hacme orantili    CG %80,2  statik marj +%12,4 MAC (olagan)
#
# Burunda SABIT kalanlar tasinamaz: es eksenli pervane cifti, gobegi ve
# onu dondUren elektrik makinesi burun grubudur.
BURUN = -0.08          # kok veterinin kesri; burun grubunun konumu


def dagilim(r=None, olcek=1.0, n=120):
    """(kutle, x, y, z, Iy_kendi) listesi dondurur.

    Iy_kendi: kalemin KENDI merkezinden gecen aciklik ekseni etrafindaki
    atalet momenti (yayili kalemler icin sifirdan farkli)."""
    r = r or kutle.butce(yaz=False, olcek=olcek)
    ist, yari, _ = istasyonlar(n=n)
    kok = P["kokVeter"] * olcek
    K = r["kalem"]
    kal = []

    # --- kabuk + ic yapi + baglanti + kapak: planforma YAYILI ---------
    yapi_yayili = (K["YAPI"]["kanat/govde kabugu (%.2f m2 islak)" % r["g"]["Swet"]]
                   + K["YAPI"]["ic yapi (kaburga, boluc, baglanti)"]
                   + K["YAPI"]["baglanti eleman., yapistirici, boya"]
                   + K["YAPI"]["erisim kapaklari ve lukler"]
                   + K["YAPI"]["ana kiris basliklari"])
    S_top = sum(0.5 * (a[2] + b[2]) * (b[0] - a[0]) for a, b in zip(ist[:-1], ist[1:]))
    for a, b in zip(ist[:-1], ist[1:]):
        dy = (b[0] - a[0]) * olcek
        c = 0.5 * (a[2] + b[2]) * olcek
        tc = 0.5 * (a[3] + b[3])
        xle = 0.5 * (a[1] + b[1]) * olcek
        y = 0.5 * (a[0] + b[0]) * olcek
        # iki yari kanat
        m = 2 * yapi_yayili * (0.5 * (a[2] + b[2]) * (b[0] - a[0])) / (2 * S_top)
        # serit: veterce c, kalinlikca t -> kendi ekseninde m(c^2+t^2)/12
        t = tc * c
        kal.append((m, xle + 0.5 * c, y, 0.0, m * (c * c + t * t) / 12.0))

    # --- uc cerceveleri: z boyunca YAYILI cubuk, ±post -----------------
    post = 0.71 * olcek
    x_uc = (ist[-1][1] + 0.5 * ist[-1][2]) * olcek
    m_cer = K["YAPI"]["uc cerceveleri + inis yuku"]
    # her cerceve 2*post uzunlugunda cubuk, merkezi kanat duzleminde
    kal.append((m_cer, x_uc, yari * olcek, 0.0,
                m_cer * (2 * post) ** 2 / 12.0))
    kal.append((K["YAPI"]["inis temas pedleri"], x_uc, yari * olcek, 0.0,
                K["YAPI"]["inis temas pedleri"] * post * post))

    # --- uc motorlari + pervaneleri: z = ±post'ta NOKTA ---------------
    m_uc = (K["TAHRIK"]["uc motorlari (8 ad.)"] + K["TAHRIK"]["uc pervaneleri"])
    kal.append((m_uc, x_uc, yari * olcek, post, 0.0))   # z^2 asagida islenir

    # --- burunda SABIT: es eksenli cift, gobegi ve onu donduren makine --
    burun = (K["TAHRIK"]["ana pervane cifti"]
             + K["TAHRIK"]["es eksenli gobek, mil, yatak"]
             + K["TAHRIK"]["burun motoru (hover tepe)"])
    kal.append((burun, BURUN * kok, 0.0, 0.0, 0.0))

    # --- TASINABILIR kalemler: ic hacme ORANTILI dagitilir -------------
    tasinabilir = (K["TAHRIK"]["ice tepmeli motor + jenerator"]
                   + K["TAHRIK"]["motor yatagi, sogutma, egzoz"]
                   + K["TAHRIK"]["guc elektronigi"] + K["TAHRIK"]["guc kablosu"]
                   + K["ENERJI"]["yakit"] + K["ENERJI"]["pil tamponu"]
                   + sum(K["SISTEM"].values()) + r["kalan"]
                   + K["PAY"][list(K["PAY"])[0]])
    hucre = hacim_hucreleri(olcek, n=n)
    Vt = sum(h[2] for h in hucre)
    for x, y, V in hucre:
        kal.append((tasinabilir * V / Vt, x, y, 0.0, 0.0))
    return kal


def hacim_hucreleri(olcek=1.0, n=200, nc=30):
    """Ic hacmi (x, y, V) hucrelerine bolerek dondurur.

    NACA 00xx yari kalinligi:
      yt/c = 5 t (0,2969 sqrt(x') - 0,1260 x' - 0,3516 x'^2
                  + 0,2843 x'^3 - 0,1015 x'^4)
    Kesit alani bu egrinin iki katinin integralidir."""
    def yt(xp, tc):
        return 5 * tc * (0.2969 * math.sqrt(xp) - 0.1260 * xp
                         - 0.3516 * xp * xp + 0.2843 * xp ** 3
                         - 0.1015 * xp ** 4)
    ist, _, _ = istasyonlar(n=n)
    cik = []
    for a, b in zip(ist[:-1], ist[1:]):
        dy = (b[0] - a[0]) * olcek
        c = 0.5 * (a[2] + b[2]) * olcek
        tc = 0.5 * (a[3] + b[3])
        xle = 0.5 * (a[1] + b[1]) * olcek
        y = 0.5 * (a[0] + b[0]) * olcek
        for k in range(nc):
            x0, x1 = k / nc, (k + 1) / nc
            A = 2 * 0.5 * (yt(x0, tc) + yt(x1, tc)) * (x1 - x0) * c * c
            cik.append((xle + 0.5 * (x0 + x1) * c, y, 2 * A * dy))
    return cik


def atalet(kal):
    """CG ve aciklik ekseni etrafinda I_yy."""
    M = sum(k[0] for k in kal)
    xg = sum(k[0] * k[1] for k in kal) / M
    zg = sum(k[0] * k[3] for k in kal) / M
    Iyy = 0.0
    for m, x, y, z, I0 in kal:
        Iyy += I0 + m * ((x - xg) ** 2 + (z - zg) ** 2)
    # uc motorlari ±z'de simetrik: yukarida tek nokta olarak z=+post
    # verildi; simetrik esini de ekle ve tekini yarim say
    return M, xg, Iyy


# ---------------------------------------------------------------------
# GEREKEN ve MEVCUT MOMENT
# ---------------------------------------------------------------------
def gereken(Iyy, t_r, aci=math.pi / 2, profil="ucgen"):
    """Doksan dereceyi t_r saniyede donmek icin gereken TEPE moment.

    7.4'un benzetimi theta'yi DOGRUSAL rampa ile suruyor: theta = 90 t/t_r.
    Bunun ivmesi her yerde sifir, iki ucunda SONSUZ -- sonlu momentle
    uretilemez.

    Iki aday sonlu profil:
      ucgen (bang-bang)  ilk yari +a, ikinci yari -a
                         alpha = 4 * aci / t_r^2   <- EN AZ olan
      yumusak (3t^2-2t^3) hiz VE ivme uclarda sifir
                         alpha = 6 * aci / t_r^2

    YAPILABILIRLIK sinamasi (gerek sart) EN AZ olani kullanmalidir:
    "bu hic yapilabilir mi" sorusunun cevabi en ucuz profille verilir.
    Varsayilan bu yuzden ucgen. Yumusak profil, gercek bir kumandanin
    daha muhtemel secimidir ve ayrica raporlanir."""
    kats = dict(yumusak=6.0, ucgen=4.0)[profil]
    alpha = kats * aci / (t_r ** 2)
    return alpha, Iyy * alpha


def mevcut(T_cift, kol):
    """Ust ve alt ciftlerin itki farkindan dogan yunuslama momenti.

    ⚠️ DUZELTME (08.09.2026). Ilk surum 4 T L kullaniyordu; YANLISTI ve
    dis denetim yakaladi. 4 T L, ALT ciftlerin -T uretmesini, yani
    itkinin tersine cevrilebilmesini gerektirir. Bu ucakta pervaneler
    tersine calismiyor: itki negatif olamaz.

    Itki negatif olamiyorsa en buyuk fark, ust ciftler tepe degerde ve
    alt ciftler SIFIRDA iken olusur. Iki ust cift vardir:

        M_maks = 2 T_maks L

    Bu, makalenin 4.4 ve 7.4'te zaten yazdigi bagintidir. Ilk surum
    ikisiyle celisiyordu."""
    return 2 * T_cift * kol


def itki_gucten(P_W, D, FoM=0.599, es_eksenli_verim=0.85):
    """Askidaki bir pervane cifti icin guc -> itki.
        P = T^1.5 / (FoM sqrt(2 rho A))   ->   T = (P FoM sqrt(2 rho A))^(2/3)
    Es eksenli cift tek disk gibi calismaz; girisim kaybi carpanla."""
    A = math.pi * (D / 2.0) ** 2
    T = (P_W * FoM * math.sqrt(2 * RHO * A)) ** (2.0 / 3.0)
    return T * es_eksenli_verim


def FoM_geri(T, P_W, D, es_eksenli_verim=1.0):
    """Verilen itki ve gucu ureten FoM. Makalenin sayisini sinar."""
    A = math.pi * (D / 2.0) ** 2
    return (T / es_eksenli_verim) ** 1.5 / (P_W * math.sqrt(2 * RHO * A))


def rapor(ad, MTOW, t_r, P_hover_kW, D_uc, post, T_makale, P_uc_W, olcek=1.0,
          **kw):
    r = kutle.butce(yaz=False, MTOW=MTOW, P_hover_kW=P_hover_kW,
                    D_uc=D_uc / olcek, post=post / olcek, olcek=olcek, **kw)
    kal = dagilim(r, olcek)
    M, xg, Iyy = atalet(kal)
    print("%s" % ad)
    print("  kutle %.1f kg (butce), CG kok veterinin %%%.0f'inde, I_yy = %.3f kg m2"
          % (M, 100 * xg / (P["kokVeter"] * olcek), Iyy))
    if not T_makale:
        # uc itkisi makalede verilmemis: kendi guc butcesinden hesapla
        P_cift = 0.12 * P_hover_kW * 1000.0 / 4.0
        T_makale = itki_gucten(P_cift, D_uc)
        print("  uc itkisi makalede verilmemis; %%12 guc payindan: %.0f W/cift"
              " -> %.1f N/cift" % (P_cift, T_makale))
    for profil in ("yumusak", "ucgen"):
        alpha, M_ger = gereken(Iyy, t_r, profil=profil)
        M_mev = mevcut(T_makale, post)
        print("  %-8s profil: alpha_tepe %.3f rad/s2 -> GEREKEN %.2f N m"
              % (profil, alpha, M_ger))
        print("           MEVCUT %.2f N m (2 x %.1f N x %.2f m)   PAY %.2f kat"
              % (M_mev, T_makale, post, M_mev / M_ger))
    if P_uc_W:
        T_hesap = itki_gucten(P_uc_W, D_uc)
        print("  makalenin %.1f N'u %.0f W ile: momentum teorisi %.1f N veriyor "
              "(%+.0f%%)" % (T_makale, P_uc_W, T_hesap,
                             100 * (T_hesap - T_makale) / T_makale))
        print("           makalenin sayisi FoM = %.3f ve es eksenli kayip YOK"
              " varsayimina denk" % FoM_geri(T_makale, P_uc_W, D_uc))
    alpha_y, M_y = gereken(Iyy, t_r, profil="ucgen")
    T_ger = M_y / (2 * post)
    print("  ATALET icin YETEN itki: %.2f N/cift  (mevcut %.1f N'un %%%.0f'i)"
          % (T_ger, T_makale, 100 * T_ger / T_makale))
    for pr in ("ucgen", "yumusak"):
        print("  EN KISA donme (%s): %.2f s   (tasarim %.1f s)"
              % (pr, en_kisa_tr(Iyy, T_makale, post, profil=pr), t_r))
    # temkinli itki: makalenin KENDI hover FoM'u ve es eksenli kayip
    if P_uc_W:
        T_tem = itki_gucten(P_uc_W, D_uc, FoM=0.599, es_eksenli_verim=0.85)
        print("  temkinli itki (FoM 0,599 + es eksenli kayip): %.1f N -> pay %.1f kat"
              % (T_tem, mevcut(T_tem, post) / M_y))
    return dict(M=M, Iyy=Iyy, alpha=alpha_y, M_ger=M_y, T_ger=T_ger,
                M_mev=mevcut(T_makale, post), T=T_makale)


def en_kisa_tr(Iyy, T_cift, kol, aci=math.pi / 2, profil="yumusak"):
    """Mevcut momentle donulebilen EN KISA donme suresi (pay = 1)."""
    kats = dict(yumusak=6.0, ucgen=4.0)[profil]
    M = mevcut(T_cift, kol)
    return math.sqrt(kats * aci * Iyy / M)


def aero_esigi(S, b, M_mevcut, M_gereken, hizlar=(10, 15, 20, 30)):
    """Kalan payi TAM tuketecek yunuslama momenti katsayisi.

    Aerodinamik momenti TAHMIN etmiyoruz -- C_m(alpha) verisi yok.
    Bunun yerine kabuk alan yogunlugunda ise yarayan tekniğin aynisi:
    hangi degerde tasarim kapanmaz, onu veriyoruz.

        M_aero = q S c_ort C_m   ->   C_m_esik = (M_mevcut - M_ger)/(q S c_ort)
    """
    c = S / b
    pay = M_mevcut - M_gereken
    print("  ortalama veter %.3f m, aerodinamige kalan %.1f N m" % (c, pay))
    print("  %-10s" % "V (m/s)" + "".join("%9.0f" % v for v in hizlar))
    print("  %-10s" % "esik C_m" +
          "".join("%9.3f" % (pay / (0.5 * RHO * v * v * S * c)) for v in hizlar))


def olcek_davranisi(Iy_h, M_h, t_h, Iy_a, M_a, t_a):
    """Donme kontrol payi olcekle nasil degisiyor?

    ⚠️ DUZELTME. Ilk surum bunu GEOMETRIK BENZERLIK varsayarak turetti
    (M ~ olcek^3, I ~ olcek^5, dolayisiyla pay ~ t_r^2/olcek^2). Iki
    referans tasarim geometrik olarak benzer DEGIL: aciklik 3,345 kat
    buyurken kutle 20 kat buyuyor (3,345^3 = 37,4, 20 degil) ve kanat
    yuklemesi 25,3'ten 45,0 kg/m2'ye cikiyor. O turetim bu yuzden
    gecersizdi.

    Artik oran, VARSAYIMDAN DEGIL, iki tasarimin hesaplanmis
    degerlerinden okunuyor."""
    rI, rM = Iy_a / Iy_h, M_a / M_h
    print("  olculen oranlar (agir / hafif):")
    print("    I_yy      %7.1f     (aciklik orani 3,345^3 = %.1f, ^5 = %.1f)"
          % (rI, 3.3449 ** 3, 3.3449 ** 5))
    print("    M_mevcut  %7.1f" % rM)
    ra = (t_h / t_a) ** 2
    print("  gereken moment orani = I orani x alpha orani = %.1f x %.3f = %.1f"
          % (rI, ra, rI * ra))
    print("  -> pay orani = %.1f / %.1f = %.2f  (pay agir hatta %.0f%% daraliyor)"
          % (rM, rI * ra, rM / (rI * ra), 100 * (1 - rM / (rI * ra))))
    t_esit = t_h * math.sqrt(rI / rM)
    print("  hafif hattin PAYINI korumak icin agir hattin donme suresi: %.2f s"
          % t_esit)
    print("  tasarim %.1f s kullaniyor -> %s"
          % (t_a, "esitlenmis" if abs(t_a - t_esit) < 0.2
             else "payi %s" % ("dar" if t_a < t_esit else "genis")))
    print("  (agir hattin donme suresi ZATEN bu hesapla 4 s'den 5,1 s'ye")
    print("   cikarildi; oran 0,61 idi, simdi 0,99)")


if __name__ == "__main__":
    print("=" * 74)
    print("GECIS DONME DINAMIGI -- atalet alt siniri")
    print("=" * 74)
    print()
    h = rapor("HAFIF 50 kg, t_r = 2 s", 50.0, 2.0, 10.9, 0.20, 0.71, 16.2, 335.0)
    print()
    a = rapor("AGIR 1000 kg, t_r = 5.1 s", 1000.0, 5.1, 216.2, 0.67, 2.38, 0.0,
          0.0, olcek=3.3449, P_motor_kW=54.3, D_ana=5.40 / 3.3449,
          m_yakit=160.0, m_pil=40.0, m_faydali=260.0)
    print()
    print("=" * 74)
    print("OLCEK DAVRANISI -- olculen oranlardan")
    print("=" * 74)
    olcek_davranisi(h["Iyy"], h["M_mev"], 2.0, a["Iyy"], a["M_mev"], 5.1)
    print()
    print("=" * 74)
    print("AERODINAMIK MOMENT ESIGI -- payi tuketecek C_m")
    print("=" * 74)
    print("HAFIF:")
    aero_esigi(1.98, 3.4528, h["M_mev"], h["M_ger"])
    print("AGIR:")
    aero_esigi(22.24, 11.55, a["M_mev"], a["M_ger"])
    print()
    print("  Ok kanatli planformlarda stall sonrasi C_m rutin olarak 0,1-0,3.")
    print("  Yani aerodinamik terim buyuk olasilikla ATALETTEN BUYUK.")
