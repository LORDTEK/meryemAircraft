# -*- coding: utf-8 -*-
"""BILESEN DUZEYINDE KUTLE BUTCESI.

NEDEN VAR. Makale 6.2'de su kesirleri veriyor: %30 yapi, %16 tahrik,
%4 pil, %8 aviyonik, %16 yakit, kalan %26 faydali yuk. Makale bunun
"bir hedef, bulgu degil" oldugunu ACIKCA soyluyor (8.2). Uc bagimsiz
dis denetim de ayni yere isaret etti: faydali yuk kesri iddiasinin
ayakta durabilmesi icin bu kesirlerin BILESENDEN kurulmasi gerekir.

ILKE (temel.py ile ayni). Uydurulan kesir yok. Her kalem ya
  (i) geometriden ve bir mukavemet/gerilme hesabindan gelir, ya da
  (ii) acikca etiketlenmis bir OZGUL DEGERDEN gelir ve taranir.
Hicbir kalem hedef kesirden geri cozulmez -- yoksa sinama degil,
kendini dogrulama olur.

SORU. 13 kg faydali yuk (%26) ayakta kaliyor mu?
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from planform import istasyonlar, P                       # noqa: E402

G, RHO_HAVA = 9.81, 1.225

# --- OZGUL DEGERLER -- hepsi VARSAYIM, hepsi taranabilir --------------
#
# Bunlar makaleden gelmiyor; kucuk insansiz hava araci pratiginin
# yaygin araliklarindan alindi ve her birinin araligi tara() icinde
# suruluyor. Tek bir sayiya guvenmiyoruz; sonucun hangi sayiya
# duyarli oldugunu ARIYORUZ.
V = dict(
    kabuk=1.5,        # kg/m2  karbon/epoksi sandvic kabuk, alan yogunlugu
    ic_yapi=0.45,     # kabuk kutlesinin kati: kaburga, boluc, yapistirma
    rho_karbon=1600., # kg/m3
    sigma_karbon=400e6,  # Pa  tasarim izin gerilmesi (knock-down dahil)
    n_ult=5.25,       # nihai yuk katsayisi (limit 3,5 x 1,5)
    n_inis=3.0,       # dikey inis yuk katsayisi
    motor=4.0,        # kW/kg  fircasiz DA motor, surekli
    guc_elektronik=20.0,  # kW/kg  ESC + dogrultucu
    ice_jen=1.0,      # kW/kg  ice tepmeli motor + jenerator (6.2'nin varsayimi)
    pil_ozgul=180.0,  # Wh/kg  Li-ion (tampon; guc yogun hucre daha dusuk)
    pervane_k=0.139,  # kg/m2  pervane kutlesi = k * D^2 (1,2 m -> 0,20 kg)
    kablo=0.010,      # kg/m/kW  guc kablosu (bakir + yalitim)
    aviyonik_sabit=0.35,  # kg  ucus bilgisayari, alicilar, sensorler
    aviyonik_olcek=0.030, # kg/kg^(2/3)   olcekle buyuyen kismi
    # --- ILK TURDA UNUTULAN KALEMLER --------------------------------
    # Ilk kosu %42,8 faydali yuk verdi; hedef %26. Asagidan yukari bir
    # butce kendi hedefini %60 asiyorsa once KALEM ARANIR. Asagidakiler
    # o aramanin sonucudur; hicbiri kesirle uydurulmadi, hepsi ya
    # standart pratik ya da bu konfigurasyonun kendi zorunlulugu.
    baglanti=0.10,    # yapi kutlesinin kati: baglanti elemani, yapistirici,
                      #   dolgu, boya, conta -- kompozit yapida %8-12 tipik
    kapak_luk=0.06,   # yapi kutlesinin kati: erisim kapaklari, mentese, kilit
    motor_yatak=0.25, # ICE kutlesinin kati: yatak, yangin duvari, sogutma,
                      #   egzoz, hava girisi
    gobek=0.35,       # ana pervane kutlesinin kati: es eksenli gobek, mil,
                      #   yatak, spinner -- es eksenli cift TEK pervane degil
    sinyal_kablo=0.008,  # kg/m  sinyal/sensor demeti (guc kablosundan AYRI)
    yuk_arayuz=0.06,  # faydali yuk kutlesinin kati: yuva, titresim yalitimi
    temas_pedi=0.15,  # kg per uc  inis temas pedi/ayagi
    # Belirsizlik payi: on tasarimda standart pratik. Bir sayi degil,
    # butun kalemlerin toplu eksikligine karsi ayrilan yer.
    pay=0.12,         # KURU kutlenin kati (on tasarim %10-15)
)


# ---------------------------------------------------------------------
# GEOMETRI
# ---------------------------------------------------------------------
def naca_cevre(tc, n=400):
    """NACA 00xx kesitinin veter basina cevresi (ust + alt)."""
    def yt(x):
        return 5 * tc * (0.2969 * math.sqrt(x) - 0.1260 * x - 0.3516 * x * x
                         + 0.2843 * x ** 3 - 0.1015 * x ** 4)
    u = 0.0
    xs = [i / n for i in range(n + 1)]
    for a, b in zip(xs[:-1], xs[1:]):
        u += math.hypot(b - a, yt(b) - yt(a))
    return 2 * u          # ust + alt


_GEO = {}


def geometri(olcek=1.0, n=200):
    """Islak alan, planform alani, aciklik -- planform.py'nin kendisinden.

    Onbellekli: kirilma degeri aramasi yuzlerce kez cagiriyor ve
    NACA cevresi integrali her seferinde yeniden hesaplanmamali."""
    if (olcek, n) in _GEO:
        return _GEO[(olcek, n)]
    ist, yari, _ = istasyonlar(n=n)
    S = Swet = 0.0
    for a, b in zip(ist[:-1], ist[1:]):
        dy = (b[0] - a[0]) * olcek
        c = 0.5 * (a[2] + b[2]) * olcek
        tc = 0.5 * (a[3] + b[3])
        S += c * dy
        Swet += naca_cevre(tc) * c * dy
    _GEO[(olcek, n)] = dict(S=2 * S, Swet=2 * Swet, yari=yari * olcek,
                            kok_veter=P["kokVeter"] * olcek,
                            tc_kok=P["tcKok"] / 100.0)
    return _GEO[(olcek, n)]


# ---------------------------------------------------------------------
# YAPI
# ---------------------------------------------------------------------
def kiris(MTOW, g, v=V):
    """Ana kiris baslik kutlesi -- egilmeden.

    Yari kanadin tasidigi kaldirma n_ult W/2; eliptik dagilimda etki
    merkezi 0,42 (b/2). Kok egilme momenti buradan; baslik alani
    A = M/(sigma h), h yapisal derinlik. Basliklar aciklik boyunca
    momentle birlikte incelir; ucgen yaklasimla etkin carpan ~0,35."""
    W = MTOW * G
    y_etki = 0.42 * g["yari"]
    M_kok = v["n_ult"] * (W / 2.0) * y_etki
    h = 0.90 * g["tc_kok"] * g["kok_veter"]        # yapisal derinlik
    A = M_kok / (v["sigma_karbon"] * h)
    m = 2 * 2 * v["rho_karbon"] * A * g["yari"] * 0.35   # 2 yari, 2 baslik
    return m, M_kok, A


def uc_cerceve(MTOW, post_uzunluk, v=V, cap=None, olcek=1.0):
    """Uc cercevesi -- kuyruk ustu bunlarin uzerine INER.

    Her uc cercevesi inis yukunun yarisini tasir; en kotu hal, yukun
    tek postun ucuna gelmesi (yana yatik inis). Konsol kirisi:
        sigma = 4 M / (pi d^2 t)   ince cidarli boru
    Postun CAPI ucakla birlikte buyumelidir; sabit birakmak agir hatta
    50 mm capli boruya 44 mm et kalinligi isteyen sacma bir sonuc verir
    (ilk surumdeki hata buydu). Cap kok veterinin ~%5'ine baglanir."""
    d = cap or 0.05 * olcek
    F = v["n_inis"] * MTOW * G / 2.0
    M = F * post_uzunluk
    t = 4 * M / (math.pi * d * d * v["sigma_karbon"])
    t = max(t, 0.0005)                      # uretim alt siniri 0,5 mm
    m_uzunluk = v["rho_karbon"] * math.pi * d * t
    # her ucta iki yone uzanan post + karsi yon: 2 x post_uzunluk
    m = 2 * (2 * post_uzunluk) * m_uzunluk
    return m * 2.0, t                        # x2: baglanti, fitting, mafsal


# ---------------------------------------------------------------------
# TAHRIK
# ---------------------------------------------------------------------
def tahrik(P_hover_kW, P_motor_kW, D_ana, D_uc, n_uc_pervane, yari, v=V):
    """Seri hibrit tahrik zinciri, kalem kalem.

    Burun motoru HOVER'a boyutlanir (tepe guc), ice tepmeli motor ise
    SEYIRE (tampon farki kapatir) -- makalenin merkezi iddiasi budur ve
    butcede de boyle gorunmelidir."""
    P_uc_kW = 0.12 * P_hover_kW            # 5.1: uc pervaneler burnun %12'si
    k = {}
    k["burun motoru (hover tepe)"] = P_hover_kW / v["motor"]
    k["uc motorlari (%d ad.)" % n_uc_pervane] = P_uc_kW / v["motor"]
    k["ana pervane cifti"] = 2 * v["pervane_k"] * D_ana ** 2
    k["uc pervaneleri"] = n_uc_pervane * v["pervane_k"] * D_uc ** 2
    k["ice tepmeli motor + jenerator"] = P_motor_kW / v["ice_jen"]
    k["guc elektronigi"] = (P_hover_kW + P_uc_kW) / v["guc_elektronik"]
    k["guc kablosu"] = v["kablo"] * (2 * yari) * P_uc_kW + \
                       v["kablo"] * 0.5 * P_hover_kW
    return k


# ---------------------------------------------------------------------
# BUTCE
# ---------------------------------------------------------------------
def butce(MTOW=50.0, P_hover_kW=10.9, P_motor_kW=2.6, D_ana=1.20, D_uc=0.20,
          n_uc=8, post=0.71, m_yakit=8.0, m_pil=1.8, m_faydali=13.0,
          olcek=1.0, v=V, yaz=True):
    g = geometri(olcek)
    kalem = {}

    m_kabuk = v["kabuk"] * g["Swet"]
    m_kiris, M_kok, A_kiris = kiris(MTOW, g, v)
    m_cerceve, t_post = uc_cerceve(MTOW, post * olcek, v, olcek=olcek)
    m_birincil = (m_kabuk + v["ic_yapi"] * m_kabuk + m_kiris + m_cerceve)
    kalem["YAPI"] = {
        "kanat/govde kabugu (%.2f m2 islak)" % g["Swet"]: m_kabuk,
        "ic yapi (kaburga, boluc, baglanti)": v["ic_yapi"] * m_kabuk,
        "ana kiris basliklari": m_kiris,
        "uc cerceveleri + inis yuku": m_cerceve,
        "baglanti eleman., yapistirici, boya": v["baglanti"] * m_birincil,
        "erisim kapaklari ve lukler": v["kapak_luk"] * m_birincil,
        "inis temas pedleri": 2 * v["temas_pedi"] * olcek ** 2,
    }
    kalem["TAHRIK"] = tahrik(P_hover_kW, P_motor_kW, D_ana * olcek,
                             D_uc * olcek, n_uc, g["yari"], v)
    kalem["TAHRIK"]["es eksenli gobek, mil, yatak"] = \
        v["gobek"] * kalem["TAHRIK"]["ana pervane cifti"]
    kalem["TAHRIK"]["motor yatagi, sogutma, egzoz"] = \
        v["motor_yatak"] * kalem["TAHRIK"]["ice tepmeli motor + jenerator"]
    kalem["SISTEM"] = {
        "aviyonik ve kumanda": v["aviyonik_sabit"] + v["aviyonik_olcek"] * MTOW ** (2/3.),
        "yakit sistemi (depo, pompa, hat)": 0.12 * m_yakit,
        "serit tahriki (tek hareketli parca)": 0.02 * MTOW ** (2/3.),
        "sinyal/sensor demeti": v["sinyal_kablo"] * (4 * g["yari"] + 2 * g["kok_veter"]),
        "faydali yuk arayuzu": v["yuk_arayuz"] * m_faydali,
    }
    kalem["ENERJI"] = {"yakit": m_yakit, "pil tamponu": m_pil}

    toplam = {b: sum(d.values()) for b, d in kalem.items()}
    kuru = toplam["YAPI"] + toplam["TAHRIK"] + toplam["SISTEM"]
    m_pay = v["pay"] * kuru
    kalem["PAY"] = {"belirsizlik payi (kurunun %%%.0f'i)" % (100 * v["pay"]): m_pay}
    toplam["PAY"] = m_pay
    bos = kuru + m_pay + toplam["ENERJI"]
    kalan = MTOW - bos

    if yaz:
        print("MTOW %.1f kg   islak alan %.2f m2   planform %.3f m2"
              % (MTOW, g["Swet"], g["S"]))
        print("kok egilme momenti %.0f N.m -> baslik alani %.1f mm2 "
              "(post et kalinligi %.2f mm)" % (M_kok, A_kiris * 1e6, t_post * 1000))
        print()
        for b in ("YAPI", "TAHRIK", "SISTEM", "PAY", "ENERJI"):
            print("%s" % b)
            for ad, m in sorted(kalem[b].items(), key=lambda x: -x[1]):
                print("    %-42s %7.3f kg  %5.1f%%" % (ad, m, 100 * m / MTOW))
            print("    %-42s %7.3f kg  %5.1f%%"
                  % ("-- ara toplam", toplam[b], 100 * toplam[b] / MTOW))
            print()
        print("  %-44s %7.3f kg  %5.1f%%" % ("BOS (yakit ve pil dahil)", bos,
                                             100 * bos / MTOW))
        print("  %-44s %7.3f kg  %5.1f%%" % ("FAYDALI YUKE KALAN", kalan,
                                             100 * kalan / MTOW))
        print("  %-44s %7.3f kg  %5.1f%%" % ("makalenin hedefi", m_faydali,
                                             100 * m_faydali / MTOW))
        print("  %-44s %+7.3f kg" % ("FARK", kalan - m_faydali))
        print()
        print("  makalenin kesirleriyle karsilastirma:")
        for ad, olc, hedef in (("yapi", toplam["YAPI"], 0.30),
                               ("tahrik", toplam["TAHRIK"], 0.16),
                               ("pil", m_pil, 0.04),
                               ("aviyonik+sistem+pay", toplam["SISTEM"] + m_pay, 0.08),
                               ("yakit", m_yakit, 0.16)):
            print("    %-18s olculen %5.1f%%   hedef %4.1f%%   %+6.1f puan"
                  % (ad, 100 * olc / MTOW, 100 * hedef,
                     100 * olc / MTOW - 100 * hedef))
    return dict(kalem=kalem, toplam=toplam, bos=bos, kalan=kalan, g=g)


def tara(taban=None):
    """Sonuc hangi varsayima dayaniyor? Tek tek gevsetilir.

    Aranan sey "en iyi tahmin" degil, KIRILMA NOKTASI: hangi kalem ne
    kadar kotulesirse 13 kg faydali yuk kapanmaz olur."""
    taban = taban or dict()
    ana = butce(yaz=False, **taban)["kalan"]
    print("taban: faydali yuke kalan %.2f kg (hedef 13,0 kg)" % ana)
    print()
    print("  %-26s %10s %10s %10s" % ("varsayim", "deger", "kalan kg", "hedefe"))
    denemeler = [
        ("kabuk kg/m2", "kabuk", (1.0, 1.5, 2.0, 2.5, 3.0)),
        ("ic yapi / kabuk", "ic_yapi", (0.30, 0.45, 0.70, 1.00)),
        ("motor kW/kg", "motor", (6.0, 4.0, 3.0, 2.0)),
        ("ICE+jen kW/kg", "ice_jen", (1.5, 1.0, 0.7, 0.5)),
        ("belirsizlik payi", "pay", (0.10, 0.12, 0.20, 0.30)),
        ("baglanti/yapistirici", "baglanti", (0.05, 0.10, 0.20)),
    ]
    for ad, anahtar, degerler in denemeler:
        for d in degerler:
            v = dict(V); v[anahtar] = d
            r = butce(yaz=False, v=v, **taban)["kalan"]
            im = "  <-- taban" if d == V[anahtar] else ("  KAPANMAZ" if r < 13.0 else "")
            print("  %-26s %10.2f %10.2f %+10.2f%s"
                  % (ad if d == degerler[0] else "", d, r, r - 13.0, im))
        print()


def kirilma(anahtar, hedef=13.0, alt=0.1, ust=20.0, taban=None, **kw):
    """Bir varsayimin KIRILMA DEGERI: hangi degerde faydali yuk hedefe
    tam esitleniyor? Ikiye bolerek aranir."""
    taban = dict(taban or {}); taban.update(kw)
    def f(x):
        v = dict(V); v[anahtar] = x
        return butce(yaz=False, v=v, **taban)["kalan"] - hedef
    if f(alt) * f(ust) > 0:
        return None
    for _ in range(60):
        orta = 0.5 * (alt + ust)
        if f(alt) * f(orta) <= 0:
            ust = orta
        else:
            alt = orta
    return 0.5 * (alt + ust)


def pil_sinami(P_hover=10.9, P_motor=2.6, m_pil=1.8, Wh_kg=180.0):
    """Pil tamponu GUC mu ENERJI mi sinirli?

    Dis denetim sordu: 1,8 kg pil, hover ile motor derecelendirmesi
    arasindaki farki gercekten besleyebilir mi? Bu bir kutle kalemi
    degil, bir HUCRE SARTNAMESI sorusudur ve makalede hic yazmiyor."""
    fark = P_hover - P_motor
    ozgul = fark / m_pil
    C = ozgul / (Wh_kg / 1000.0)
    t_esik = m_pil * Wh_kg * 3600.0 / (fark * 1000.0)
    print("hover %.1f kW - motor %.1f kW = %.1f kW pilden" % (P_hover, P_motor, fark))
    print("  %.1f kg pil -> GEREKEN OZGUL GUC %.2f kW/kg  (%.0fC, %.0f Wh/kg'da)"
          % (m_pil, ozgul, C, Wh_kg))
    print("  enerji sinirina gecis: %.0f s hover" % t_esik)
    print("  Yani %.0f s'nin ALTINDA tampon GUC sinirli, ustunde ENERJI sinirli."
          % t_esik)
    print("  Not: %.0fC verebilen hucreler tipik olarak %.0f Wh/kg'in altinda kalir;"
          % (C, Wh_kg))
    print("  o durumda enerji esigi de asagi iner. Bu bir hucre secimi kisitidir.")
    return ozgul, t_esik


def agir(kabuk_us=0.5):
    """Agir hat (1000 kg). TEK ACIK SORU: kabuk alan yogunlugu olcekle
    nasil buyur?

      kabuk kutlesi ~ sigma_alan * S_islak ~ sigma_alan * olcek^2
      MTOW          ~ olcek^3
    sigma_alan SABIT kalirsa kabuk KESRI olcekle 1/olcek gibi duser --
    bu acikca yanlistir, buyuk ucakta kaplama incelmez. Sabit KESIR
    icin sigma_alan ~ olcek^1 gerekir. Gercek us ikisinin arasindadir;
    burada acikca taranir, tek bir deger secilmez."""
    OLCEK = 3.3449
    print("agir hat, kabuk alan yogunlugu us'u taraniyor "
          "(0 = sabit kg/m2, 1 = sabit kesir)")
    print("  %-8s %12s %12s %12s %10s" % ("us", "kabuk kg/m2", "yapi kg",
                                          "faydali kg", "hedef 260"))
    for us in (0.0, 0.25, 0.50, 0.75, 1.00):
        v = dict(V); v["kabuk"] = V["kabuk"] * OLCEK ** us
        r = butce(MTOW=1000.0, P_hover_kW=216.2, P_motor_kW=54.3,
                  D_ana=5.40 / OLCEK, D_uc=0.67 / OLCEK, post=2.38 / OLCEK,
                  m_yakit=160.0, m_pil=40.0, m_faydali=260.0,
                  olcek=OLCEK, v=v, yaz=False)
        print("  %-8.2f %12.2f %12.1f %12.1f %10s"
              % (us, v["kabuk"], r["toplam"]["YAPI"], r["kalan"],
                 "OK" if r["kalan"] >= 260 else "KAPANMAZ"))
    print()
    OLCEK2 = 3.3449
    lo, hi = 0.0, 1.0
    for _ in range(60):
        orta = 0.5 * (lo + hi)
        v = dict(V); v["kabuk"] = V["kabuk"] * OLCEK2 ** orta
        r = butce(MTOW=1000.0, P_hover_kW=216.2, P_motor_kW=54.3,
                  D_ana=5.40 / OLCEK2, D_uc=0.67 / OLCEK2, post=2.38 / OLCEK2,
                  m_yakit=160.0, m_pil=40.0, m_faydali=260.0,
                  olcek=OLCEK2, v=v, yaz=False)
        if r["kalan"] >= 260.0:
            lo = orta
        else:
            hi = orta
    print()
    print("  KIRILMA USSU: %.3f  (kabuk %.2f kg/m2). Bu ussun uzerinde"
          % (lo, V["kabuk"] * OLCEK2 ** lo))
    print("  agir hat 260 kg faydali yuku KAPATMIYOR.")
    print()
    print("  Not: kiris basliklari her iki olcekte de ihmal edilebilir")
    print("  (hafifte %0,1, agirda ~%0,3). Bu boyutlarda yapiyi belirleyen")
    print("  MUKAVEMET DEGIL, asgari kaplama kalinligi ve montajdir.")


if __name__ == "__main__":
    print("=" * 74)
    print("HAFIF HAT -- 50 kg")
    print("=" * 74)
    butce()
    print()
    print("=" * 74)
    print("DUYARLILIK -- sonuc hangi varsayima dayaniyor")
    print("=" * 74)
    tara()
    print("KIRILMA DEGERLERI -- hafif hat, hangi degerde 13 kg kapanmaz")
    for ad, anahtar in (("kabuk kg/m2", "kabuk"), ("ic yapi / kabuk", "ic_yapi"),
                        ("belirsizlik payi", "pay"), ("baglanti orani", "baglanti")):
        x = kirilma(anahtar)
        print("  %-22s taban %6.2f  ->  kirilma %s"
              % (ad, V[anahtar], ("%.3f" % x) if x else "bulunamadi"))
    for ad, anahtar in (("motor kW/kg", "motor"), ("ICE+jen kW/kg", "ice_jen")):
        x = kirilma(anahtar, alt=0.2, ust=20.0)
        print("  %-22s taban %6.2f  ->  kirilma %s (ALTINDA kapanmaz)"
              % (ad, V[anahtar], ("%.3f" % x) if x else "bulunamadi"))
    print()
    print("=" * 74)
    print("PIL TAMPONU -- guc mu enerji mi sinirli")
    print("=" * 74)
    pil_sinami()
    print()
    print("  agir hat:")
    pil_sinami(216.2, 54.3, 40.0)
    print()
    print("=" * 74)
    print("AGIR HAT -- 1000 kg")
    print("=" * 74)
    agir()
