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

KONUM = dict(
    # x, kok veterinin kesri olarak (kok veter 0,97 m)
    burun_grubu=-0.08,   # es eksenli cift + gobek: kok hucum kenarinin ONUNDE
    motor=0.30,          # elektrik makinesi, merkez govde icinde
    ice=0.45,            # ice tepmeli motor + jenerator
    yakit=0.50,          # yakit deposu
    pil=0.35,
    aviyonik=0.20,
    faydali=0.40,
)


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

    # --- burun grubu, motor, ICE, sistemler: merkez govdede -----------
    burun = (K["TAHRIK"]["ana pervane cifti"]
             + K["TAHRIK"]["es eksenli gobek, mil, yatak"])
    nokta = [
        (burun, KONUM["burun_grubu"] * kok),
        (K["TAHRIK"]["burun motoru (hover tepe)"], KONUM["motor"] * kok),
        (K["TAHRIK"]["ice tepmeli motor + jenerator"]
         + K["TAHRIK"]["motor yatagi, sogutma, egzoz"]
         + K["TAHRIK"]["guc elektronigi"] + K["TAHRIK"]["guc kablosu"],
         KONUM["ice"] * kok),
        (K["ENERJI"]["yakit"] + K["SISTEM"]["yakit sistemi (depo, pompa, hat)"],
         KONUM["yakit"] * kok),
        (K["ENERJI"]["pil tamponu"], KONUM["pil"] * kok),
        (sum(K["SISTEM"][k] for k in K["SISTEM"]
             if k != "yakit sistemi (depo, pompa, hat)"), KONUM["aviyonik"] * kok),
        (r["kalan"], KONUM["faydali"] * kok),
        (K["PAY"][list(K["PAY"])[0]], 0.45 * kok),
    ]
    for m, x in nokta:
        kal.append((m, x, 0.0, 0.0, 0.0))
    return kal


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
def gereken(Iyy, t_r, aci=math.pi / 2, profil="yumusak"):
    """Doksan dereceyi t_r saniyede donmek icin gereken TEPE moment.

    7.4'un benzetimi theta'yi DOGRUSAL rampa ile suruyor: theta = 90 t/t_r.
    Bunun ivmesi her yerde sifir, iki ucunda SONSUZ -- sonlu momentle
    uretilemez. Sonlu momentle uretilebilen en yakin profil, hiz ve
    ivmesi uclarda sifirlanan yumusak (3tau^2-2tau^3) profildir:
        alpha_tepe = 6 * aci / t_r^2
    Ucgen (bang-bang) profil daha ucuzdur: alpha = 4 * aci / t_r^2."""
    kats = dict(yumusak=6.0, ucgen=4.0)[profil]
    alpha = kats * aci / (t_r ** 2)
    return alpha, Iyy * alpha


def mevcut(T_cift, kol, n_cift_ust=2):
    """Ust ve alt ciftlerin itki farkindan dogan yunuslama momenti.

    4.3: dort cift, ikisi ust ikisi alt, kol = post uzunlugu. Ust
    ciftler +T, alt ciftler -T verirse cift kuvvet:
        M = 2 * n_cift_ust * T * kol
    Makalenin kendi bagintisi M = 2 T L, T'yi taraf basina toplam alarak."""
    return 2 * n_cift_ust * T_cift * kol


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
        print("           MEVCUT %.2f N m (%.1f N x %.2f m x 4)   PAY %.1f kat"
              % (M_mev, T_makale, post, M_mev / M_ger))
    if P_uc_W:
        T_hesap = itki_gucten(P_uc_W, D_uc)
        print("  makalenin %.1f N'u %.0f W ile: momentum teorisi %.1f N veriyor "
              "(%+.0f%%)" % (T_makale, P_uc_W, T_hesap,
                             100 * (T_hesap - T_makale) / T_makale))
        print("           makalenin sayisi FoM = %.3f ve es eksenli kayip YOK"
              " varsayimina denk" % FoM_geri(T_makale, P_uc_W, D_uc))
    alpha_y, M_y = gereken(Iyy, t_r, profil="yumusak")
    T_ger = M_y / (2 * 2 * post)
    print("  ATALET icin YETEN itki: %.2f N/cift  (mevcut %.1f N'un %%%.0f'i)"
          % (T_ger, T_makale, 100 * T_ger / T_makale))
    print("  mevcut momentle EN KISA donme: %.2f s  (tasarim %.1f s)"
          % (en_kisa_tr(Iyy, T_makale, post), t_r))
    # temkinli itki: makalenin KENDI hover FoM'u ve es eksenli kayip
    if P_uc_W:
        T_tem = itki_gucten(P_uc_W, D_uc, FoM=0.599, es_eksenli_verim=0.85)
        print("  temkinli itki (FoM 0,599 + es eksenli kayip): %.1f N -> pay %.1f kat"
              % (T_tem, mevcut(T_tem, post) / M_y))
    return dict(M=M, Iyy=Iyy, alpha=alpha_y, M_ger=M_y, T_ger=T_ger)


def en_kisa_tr(Iyy, T_cift, kol, aci=math.pi / 2, profil="yumusak"):
    """Mevcut momentle donulebilen EN KISA donme suresi (pay = 1)."""
    kats = dict(yumusak=6.0, ucgen=4.0)[profil]
    M = mevcut(T_cift, kol)
    return math.sqrt(kats * aci * Iyy / M)


def olcek_davranisi():
    """Donme kontrol payi olcekle nasil degisiyor?

    M_mevcut ~ T kol ~ olcek^2 * olcek = olcek^3   (T guc payindan, ~ olcek^3)
    I_yy     ~ m L^2                   ~ olcek^5
    alpha    ~ 1/t_r^2
    Pay = M/(I alpha) ~ olcek^3 / (olcek^5 / t_r^2) = t_r^2 / olcek^2
    Yani ayni pay icin t_r OLCEKLE DOGRUSAL buyumeli. 7.4 zaten agir
    ucagin daha yavas donmesi gerektigini soyluyor; bu, o ifadenin
    sayisal karsiligidir."""
    print("Donme kontrol payi ~ t_r^2 / olcek^2  ->  ayni pay icin t_r ~ olcek")
    print("  olcek 3,345 kat -> ayni pay icin t_r 2 s'den %.2f s'ye cikmali"
          % (2.0 * 3.3449))


if __name__ == "__main__":
    print("=" * 74)
    print("GECIS DONME DINAMIGI -- atalet alt siniri")
    print("=" * 74)
    print()
    rapor("HAFIF 50 kg, t_r = 2 s", 50.0, 2.0, 10.9, 0.20, 0.71, 16.2, 335.0)
    print()
    rapor("AGIR 1000 kg, t_r = 4 s", 1000.0, 4.0, 216.2, 0.67, 2.38, 0.0,
          0.0, olcek=3.3449, P_motor_kW=54.3, D_ana=5.40 / 3.3449,
          m_yakit=160.0, m_pil=40.0, m_faydali=260.0)
    print()
    print("=" * 74)
    print("OLCEK DAVRANISI")
    print("=" * 74)
    olcek_davranisi()
