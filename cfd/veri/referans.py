# -*- coding: utf-8 -*-
"""Deneysel referans degerler -- BIRINCI ELDEN okunmus kaynaklardan.

Bu dosyadaki her sayinin yaninda nereden ve NASIL okundugu yazilidir.
Projenin kurali: sayisal iddialar yalnizca birinci elden okunan kaynaklara
baglanir. Ikinci elden aktarim, ozet ya da yapay zeka ciktisi KULLANILMAZ.

Kaynaklar `cfd/kaynak/` altinda durur ve depoya girmistir.

OKUMA YONTEMI
Kaynak PDF'lerin metin katmani yoktur (taranmis). Degerler, sayfalar 300
dpi'da goruntuye cevrilip grafiklerin IZGARA CIZGILERI tespit edilerek ve
isaretcilerin piksel agirlik merkezi olculerek okunmustur. Kalibrasyon her
seferinde bilinen izgara degerleriyle capraz dogrulanmistir; asagida her
degerin yaninda o dogrulama da yazilidir.
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
