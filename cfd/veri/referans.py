# -*- coding: utf-8 -*-
"""Deneysel referans degerler -- BIRINCI ELDEN okunmus kaynaklardan.

Bu dosyadaki her sayinin yaninda nereden ve NASIL okundugu yazilidir.
Projenin kurali: sayisal iddialar yalnizca birinci elden okunan kaynaklara
baglanir. Ikinci elden aktarim, ozet ya da yapay zeka ciktisi KULLANILMAZ.

Kaynaklar `cfd/kaynak/` altinda durur ve depoya girmistir.

OKUMA YONTEMLERI -- her degerin yaninda hangisi kullanildigi yazilidir.

1. Metin katmani. En iyisi; olcum yok, okuma var. (NAS-2016-01'in
   tablolari boyle okundu.)

2. Vektor cikarimi. PDF'teki sekil vektor grafikse egrinin dugum
   noktalari dosyanin icinde SAYI olarak durur; sayfa SVG'ye cevrilip
   yollar dogrudan okunur (veri/nas_sekil.py). Okunan sey cizimin kendi
   verisidir, goz olcusu degil. (NAS-2016-01 Sekil 4.1 ve 4.2 boyle
   okundu.)

3. Raster sayisallastirma. Kaynak taranmis goruntuyse baska yol yok:
   sayfa 300 dpi'da goruntuye cevrilir, grafigin IZGARA CIZGILERI tespit
   edilir, isaretcilerin piksel agirlik merkezi olculur. Kalibrasyon her
   seferinde bilinen izgara degerleriyle CAPRAZ DOGRULANIR ve dogrulama
   asagida degerin yaninda yazilidir. (Ladson ve McCroskey boyle okundu.)
"""

LADSON_CD0 = dict(
    deger=0.00807,
    belirsizlik=0.0002,
    kosul="M = 0.15, Re = 6.0e6, gecis 0.05c'de tetiklenmis",
    kaynak="Ladson, C. L., NASA TM 4074, Ekim 1988, Sekil 28(b)",
    dosya="cfd/kaynak/19880019495.pdf, PDF sayfa 90 (basili sayfa 88)",
    yontem=(
        "Sekil 28(b) 300 dpi'da tarandi. Yatay izgara cizgileri satir "
        "1685/1928/2173/2417/2660'ta bulundu ve sirasiyla c_d,o = "
        "0.012/0.010/0.008/0.006/0.004'e karsilik geliyor (244 piksel = "
        "0.002). Dusey cizgiler sutun 610/1050/1488/1928'de, R = "
        "0/5/10/15 x 1e6 (439 piksel = 5e6). R = 6e6 sutununda (1137) "
        "#80, #120 ve #180 isaretcileri ust uste biniyor; kumenin agirlik "
        "merkezi satir 2164 -> c_d,o = 0.00807. Kalibrasyonun capraz "
        "dogrulamasi: ayni taramada 0.010 ve 0.006 izgara cizgileri "
        "0.01000 ve 0.00600 olarak geri okundu."),
    not_=(
        "#60-W (sarmali gecis seridi) ayni noktada 0.00897 veriyor ve "
        "KULLANILMAMALIDIR: raporun kendi metni (basili sayfa 4) sarmali "
        "yontemin zimpara tanelerinden dolayi surukemeyi yaklasik 0.001 "
        "artirdigini soyluyor."),
)

MCCROSKEY_CD0 = dict(
    deger=0.00826,
    belirsizlik=0.0001,
    kosul="Re = 6.0e6, tetiklenmis deneylere en iyi uyum, C_L = 0",
    kaynak=("NASA Turbulence Modeling Resource, '2DN00: 2D NACA 0012 "
            "Airfoil Validation Case', C_D - C_L grafigi"),
    dosya="cfd/kaynak/2D NACA 0012 Airfoil Validation Case.pdf, sayfa 5",
    yontem=(
        "Grafik 300 dpi'da tarandi. Yatay izgara: satir 1913 = C_D 0, "
        "258 piksel = 0.005 (dogrulama: 0.005 -> 1655, 0.010 -> 1397, "
        "ikisi de tespit edilen cizgilerle birebir). Dusey izgara: sutun "
        "1334 = C_L 0, 206 piksel = 0.5. Siyah dolu daire (McCroskey en "
        "iyi uyum) agirlik merkezi satir 1487, sutun 1334 -> C_L = "
        "+0.001, C_D = 0.00826."),
    not_=(
        "Ayni sayfanin metni sunu soyluyor: 'For comparing with fully "
        "turbulent CFD drag results, tripped experimental data are more "
        "appropriate than untripped.' Bizim cozumumuz tamamen turbulansli "
        "oldugu icin karsilastirma tetiklenmis veriyledir."),
)

# ---------------------------------------------------------------- kosullar

GEOMETRI_NOTU = """
Bu karsilastirmada uc kosul farki vardir ve hicbiri gizlenmemelidir:

1. GECIS. Bizim cozumumuz TAMAMEN TURBULANSLI (gecis hucum kenarinda),
   Ladson'in verisi %5 veterde TETIKLENMIS. Tamamen turbulansli akis, %5'e
   kadar laminer kalan akistan daha cok surukleme uretir. Yani bizim
   degerlerimiz deneyin biraz USTUNDE cikmalidir. TMR sayfasi yine de
   tetiklenmis veriyi tamamen turbulansli CFD icin uygun referans sayiyor.

2. GEOMETRI. Biz kapali firar kenarli NACA 0012 kullaniyoruz (dorduncu
   katsayi -0.1036, azami kalinlik veterin %12'si, firar kenari x = 1'de
   sifir kalinlikta kapaniyor). TMR'nin CFD agları bunun yerine acik firar
   kenarli formulden turetilip 1.008930411365 ile olceklenmis bir kopya
   kullanir; azami kalinligi veterin %11.894'u. Ladson'in RUZGAR TUNELI
   MODELI ise gercek NACA 0012'dir (veter 60.10 cm, olculer tasarim
   ordinatlarindan 0.0002c'den az sapiyor) ve gercek NACA 0012'nin firar
   kenari kordur, sivri degil. Yani bizim geometrimiz TMR'nin CFD
   geometrisinden cok deneyin modeline yakindir; ama kor firar kenarinin
   taban suruklemesi bizde yoktur.

3. SIKISTIRILABILIRLIK ve ALAN. Bizim cozumumuz sikistirilamaz, deney
   M = 0.15. Ladson Sekil 27(a) c_d,o'nun M = 0.15 ile 0.36 arasinda
   neredeyse duz oldugunu gosteriyor, yani M = 0.15'te Mach etkisi
   kucuktur. Dis sinirimiz 20 veter, TMR'ninki 500 veter; 20'den 200
   vetere gecmenin olculen etkisi -%0.14.
"""

if __name__ == "__main__":
    for ad, d in (("Ladson TM 4074", LADSON_CD0),
                  ("McCroskey (TMR)", MCCROSKEY_CD0)):
        print("%s" % ad)
        print("  c_d,o = %.5f  +- %.4f" % (d["deger"], d["belirsizlik"]))
        print("  kosul : %s" % d["kosul"])
        print("  kaynak: %s" % d["kaynak"])
        print("  dosya : %s" % d["dosya"])
        print()
    print(GEOMETRI_NOTU)


# ------------------------------------------------- kod-kod referans degerleri

KOD_KOD = dict(
    kaynak=("Jespersen, D. C., Pulliam, T. H., Childs, M. L., "
            "'Turbulence Modeling Resource Validation Results', "
            "NAS Technical Report NAS-2016-01, NASA Ames"),
    dosya="cfd/kaynak/NAS_Technical_Report_NAS-2016-01.pdf, Tablo 7.1 ve 7.2",
    kosul="M = 0.15, Re = 6.0e6, alfa = 0, 897 x 257 ag",
    yontem="PDF'in metin katmanindan dogrudan okundu (tarama/olcum yok).",
    SA={"Cfl3d": 0.00819, "Fun3d": 0.00812, "Nts": 0.00813, "Joe": 0.00812,
        "Sumb": 0.00813, "Turns": 0.00830, "Ggns": 0.00817,
        "Overflow": 0.00838},
    SST={"Cfl3d": 0.00809, "Fun3d": 0.00808, "Nts": 0.00809,
         "Overflow": 0.00821},
    # Overflow'un kendi ag yakinsamasi, SST, alfa = 0 (Tablo 7.5)
    SST_ag={3729: 0.00951145, 14625: 0.00846612, 57921: 0.00826384,
            230529: 0.00820820, 919809: 0.00816992},
    SA_ag={3729: 0.00978291, 14625: 0.00878727, 57921: 0.00841582,
           230529: 0.00838221, 919809: 0.00820996},
    not_=(
        "BU TABLO BIR ONCEKI SONUCUMUZU CURUTTU. Yerlesik kodlarda SA ile "
        "SST arasindaki fark alfa = 0'da yalnizca %0,9 (ortalama 0,00819 ve "
        "0,00812). Bizde %9,4 cikmisti ve bunu 'baskin belirsizlik turbulans "
        "modelidir' diye yazmistik. Yanlisti: bizim SA'miz referans bandinin "
        "ust ucunda, ama SST'miz her yerlesik kodun %5 altinda. Sorun model "
        "duyarliligi degil, bizim SST kurulumumuz."),
)

SST_SERBEST_AKIS = dict(
    kaynak="NAS-2016-01, basili sayfa 13",
    dosya="cfd/kaynak/NAS_Technical_Report_NAS-2016-01.pdf",
    mutinf=0.001,
    xkinf_formul="XKINF = 1.5 * (FSTI/100)^2",
    not_=(
        "Referans uygulama SST icin serbest akista (mu_t/mu)_inf = 0,001 "
        "aliyor. Biz 1,0 kullanmisiz -- bin kat buyuk. k dogruydu (%0,1 "
        "siddet, referansin %0,088 - %0,104'uyle uyumlu) ama omega_inf = "
        "k / nu_t oldugu icin bizimki 9, referansinki 9000. Bu degisken "
        "SA'da YOKTUR; SA'nin oturup SST'nin oturmamasinin nedeni olabilir. "
        "cfd/naca/serbest.py bunu tariyor."),
)


DUZ_LEVHA = dict(
    kaynak=("Jespersen, D. C., Pulliam, T. H., Childs, M. L., "
            "NAS Technical Report NAS-2016-01, Bolum 4, "
            "'2D Zero Pressure Gradient Flat Plate'"),
    dosya="cfd/kaynak/NAS_Technical_Report_NAS-2016-01.pdf, Sekil 4.1 ve 4.2",
    kosul="M = 0.2, Re = 5.0e6 (birim uzunluk uzerinden)",
    yontem=(
        "Vektor cikarimi (yontem 2). Sekiller vektor grafik; sayfa "
        "pdftocairo ile SVG'ye cevrilip egri yollari okundu. Kod: "
        "veri/nas_sekil.py, karsilastirma: levha/karsilastir.py.\n"
        "KALIBRASYON DENETIMI -- varsayilmadi, sinandi: Sekil 4.2'nin "
        "ucuncu egrisi Coles'in ortalama hiz profilidir ve log tabakasinda "
        "u+ = (1/kappa) ln y+ + B'ye oturmak zorundadir. Cikarilan egri "
        "buna y+ = 100-300 arasinda 0,05'ten iyi uyuyor (y+ 100'de +0,006, "
        "200'de +0,021, 300'de +0,048). Denetim basarisizsa "
        "levha/karsilastir.py calismayi durdurur."),
    # Re_theta tanimi kaynagin kendi metninden: integralin ust siniri
    # u = %99,5 U_inf noktasidir (basili sayfa 17).
    re_theta_tanimi="momentum kalinligi, ust sinir u = %99,5 U_inf",
    # Sekil 4.1'den okunan C_f degerleri
    # DUZELTILDI: x ekseni 4000-13000, 4000-12000 degil. Ilk okumada
    # cerceve kenarindan 12000 varsaymistim; eksen etiketlerinin konumu
    # 13000 diyor (artik sacilimi 0,009'a karsi 6,495). Bkz.
    # nas_sekil.eksen_denetimi ve dogrulama.md "DUZELTME 2".
    Cf_Overflow={"SA": {5000: 0.002920, 7000: 0.002754, 9000: 0.002641,
                        11000: 0.002554},
                 "SST": {5000: 0.002914, 7000: 0.002747, 9000: 0.002630,
                         11000: 0.002543}},
    Cf_Cfl3d={"SA": {5000: 0.002916, 7000: 0.002753, 9000: 0.002638,
                     11000: 0.002555},
              "SST": {5000: 0.002905, 7000: 0.002739, 9000: 0.002623,
                      11000: 0.002535}},
    # Sekil 4.2'den okunan u+ degerleri, Re_theta = 10000
    up_Overflow={"SA": {30: 13.289, 100: 16.371, 300: 19.054, 800: 22.080},
                 "SST": {30: 12.643, 100: 16.213, 300: 19.024, 800: 21.912}},
    not_=(
        "BU, CALISMADAKI EN GUCLU DOGRULAMA ADIMI, cunku karsilastirilan "
        "sey toplam bir katsayi degil PROFILIN KENDISI ve iki bagimsiz kod "
        "var.\n"
        "Sonuc: bizim SA'miz iki kodla da +-0,06 u+ icinde cakisiyor -- "
        "ag, semalar, u_tau cikarimi ve kuvvet makinesi dogrulandi (hepsi "
        "SST ile ORTAK). Bizim SST'miz her y+'ta duzgun +0,53 u+ kaymis.\n"
        "C_f'te modeller ARASI fark: referansta -%0,2 ... -%0,8, bizde "
        "-%4,1 ... -%4,8.\n"
        "SINIR -- kaldirilmadi: referans M = 0,2, bizimki sikistirilamaz; "
        "ayrica bizim ust sinirimiz H = 1 m'de kayma kosullu ve levha "
        "boyunca dCp/dx = -0,0034 olculdu. Bu iki fark IKI MODELI DE ayni "
        "yonde etkiler (olculdu: SA +%1,03->+%1,30, SST -%3,33->-%2,65, "
        "ikisi de Re_theta ile artiyor). Bu yuzden MUTLAK C_f farklari "
        "modelin dogrulamasi olarak okunmamalidir; anlamli olan modeller "
        "arasindaki farktir."),
)
