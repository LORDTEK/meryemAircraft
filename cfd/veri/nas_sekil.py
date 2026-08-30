# -*- coding: utf-8 -*-
"""NAS-2016-01'in Sekil 4.1 ve 4.2'sindeki egrileri BIRINCI ELDEN okur.

Kaynak: NASA Advanced Supercomputing Division, Technical Report
NAS-2016-01, Bolum 4 "2D Zero Pressure Gradient Flat Plate".
Dosya: cfd/kaynak/NAS_Technical_Report_NAS-2016-01.pdf (kullanici indirdi).

Vaka: M = 0,2 , Re = 5.000.000 (birim uzunluk uzerinden). Ilgilenilen
buyuklukler: C_f'in Re_theta'ya karsi degisimi (4000 < Re_theta < 13000)
ve Re_theta = 10000'de u+'in y+'a karsi degisimi. Bolum 4 ayrica
Re_theta'nin tanimini veriyor: momentum kalinligi integralinin ust siniri
u = %99,5 U_inf noktasidir.

OKUMA YONTEMI. Sekillerde sayisal tablo yok. Ama PDF'teki sekiller
VEKTOR grafik; yani egrilerin dugum noktalari dosyanin icinde sayi olarak
duruyor. Sayfa pdftocairo ile SVG'ye cevriliyor ve egri yollari dogrudan
okunuyor. Bu, sekli goz ile okumaktan (raster sayisallastirma) niteliksel
olarak farklidir: okunan sey cizimin kendi verisidir.

KALIBRASYON DENETIMI -- IKI KATMANLI. Sayfa koordinatindan eksen
degerine gecis VARSAYILMAZ, sinanir.

1. Eksen denetimi (eksen_denetimi). Eksen etiketlerinin sayfa uzerindeki
   konumlari okunur ve varsayilan eksen araligiyla DOGRUSAL olup
   olmadigina bakilir. Dogruysa artiklar sabit cikar (glif sol kenari
   yanliligi); yanlissa yelpaze gibi acilir.

   BU DENETIM BIR HATA YAKALADI. Sekil 4.1'in x eksenini once cerceve
   kenarlarindan 4000-12000 diye almistim; etiketler ise 4000-13000
   diyor (artiklar 12000'de +1,13'ten +19,50'ye aciliyor, 13000'de
   +1,12'de sabit, sacilim 0,009). Cerceve kenari her sekilde eksen
   ucuna denk DUSMUYOR: 4.1 ve 4.2'de dusuyor, 7.4'te dusmuyor
   (orada cercevenin sol kenari x/c = -0,040).

2. Fizik denetimi. Sekil 4.2'de ucuncu egri Coles'in ortalama hiz
   profilidir ve logaritmik tabakada u+ = (1/kappa) ln y+ + B'ye
   oturmak zorundadir; cikarilan egri buna y+ = 100-300 arasinda
   0,05'ten iyi uyuyor. Sekil 7.4'te Cp egrisinin azami degeri M = 0,15
   icin durma basincidir; cikarilan egri 1,0058 veriyor, kuramsal
   1 + M^2/4 = 1,0056.

SINIR. Bizim vakamiz sikistirilamaz, referansinki M = 0,2. Bu fark
kaldirilmadi; C_f karsilastirmasinda akilda tutulmalidir.
"""
import math, os, re, subprocess, sys

BURA = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(BURA, "..", "kaynak", "NAS_Technical_Report_NAS-2016-01.pdf")

# Sekil -> (PDF sayfasi, cerceve dikdortgeni [yol koordinati], eksen degerleri)
SEKIL = {
    # DIKKAT: x ust ucu 13000, 12000 DEGIL -- eksen etiketlerinden
    # dogrulandi (bkz. eksen_denetimi ve modul basligi).
    "4.1": dict(sayfa=20, x=(4000.0, 13000.0), y=(0.0020, 0.0040),
                cerceve=(818.007504, 6938.001312, 468.030374, 4751.997163),
                en_az=40,
                # (deger, sayfa_x) ciftleri, SST alt grafigi
                etiket=dict(eksen="x", tx=(311.103, 0.027054),
                            nokta=[(4000, 332.1), (6000, 368.9), (8000, 405.7),
                                   (10000, 442.5), (12000, 479.3)])),
    "4.2": dict(sayfa=21, x=(-1.0, 4.0), y=(0.0, 30.0),
                cerceve=(518.017188, 6637.970776, 548.069151, 4831.967268),
                en_az=200),
    # NACA0012, alfa = 0, SA modeli. Ust satirin SAG grafigi: ust yuzeyde
    # C_f. Bu sekilde cerceve kenari eksen ucuna denk DUSMEZ; kalibrasyon
    # tik isaretlerinden yapildi (x/c=0 -> 863.7, x/c=1 -> 6748.0 iken
    # cerceve 627.96 - 6748.03, yani sol kenar x/c = -0.0401).
    "7.4cf": dict(sayfa=44, x=(-0.040075, 1.0), y=(0.0, 0.008),
                  cerceve=(718.066890, 6838.019847, 387.952902, 4672.048055),
                  en_az=100, tx_kod=("311.103", "291.629"), model="SA"),
    "7.4cp": dict(sayfa=44, x=(-0.040075, 1.0), y=(1.2, -0.6),
                  cerceve=(627.959101, 6748.032909, 387.948041, 4671.985599),
                  en_az=100, tx_kod=("110.854", "291.629"), model="SA"),
    # Sekil 7.6: ayni duzen, ayni cerceveler ve ayni tik yapisi, SST modeli
    "7.6cf": dict(sayfa=46, x=(-0.040075, 1.0), y=(0.0, 0.008),
                  cerceve=(718.066890, 6838.019847, 387.952902, 4672.048055),
                  en_az=100, tx_kod=("311.103", "291.629"), model="SST"),
    "7.6cp": dict(sayfa=46, x=(-0.040075, 1.0), y=(1.2, -0.6),
                  cerceve=(627.959101, 6748.032909, 387.948041, 4671.985599),
                  en_az=100, tx_kod=("110.854", "291.629"), model="SST"),
}
# Alt grafikleri ayiran, yolun kendi transform matrisindeki oteleme
ALT = {"110.854": "SA", "311.103": "SST", "210.979": "SST-V"}
KAPPA, B = 0.41, 5.0


def _svg(sekil, gecici="/tmp"):
    yol = os.path.join(gecici, "nas_%s.svg" % sekil.replace(".", "_"))
    if not os.path.exists(yol):
        s = SEKIL[sekil]["sayfa"]
        subprocess.run(["pdftocairo", "-svg", "-f", str(s), "-l", str(s),
                        PDF, yol], check=True)
    return yol


def egriler(sekil):
    """{(model, kod): [(x, y), ...]} -- eksen degerlerinde."""
    t = SEKIL[sekil]
    s = open(_svg(sekil)).read()
    cx0, cx1, cy0, cy1 = t["cerceve"]
    out = {}
    for m in re.finditer(r"<path\b([^>]*?)/>", s):
        a = m.group(1)
        d = re.search(r'd="([^"]*)"', a)
        tr = re.search(r'transform="matrix\(([^)]*)\)"', a)
        if not d or not tr or d.group(1).count("L") < t["en_az"]:
            continue
        p = tr.group(1).split(",")
        tx, ty = p[4].strip()[:7], p[5].strip()[:7]
        if "tx_kod" in t:
            # Bazi sayfalarda (orn. 44) UC alt grafik satiri ayni
            # x-otelemesini paylasir; alt grafigi ayirt etmek icin
            # y-otelemesi de gerekir. Bunu atlamak yanlis alt grafigi
            # okumaya yol acar -- fizik denetimi bunu yakaladi
            # (azami Cp 1,0722 cikti, 1,0056 olmaliydi).
            if (tx, ty) != tuple(x[:7] for x in t["tx_kod"]):
                continue
            model = t.get("model", "SA")
        else:
            model = ALT.get(tx)
            if model is None:
                continue
        # Renk kodu: yesil = kuram (Coles / Karman-Schoenherr),
        # kirmizi kesikli = Cfl3d, siyah duz = Overflow.
        kod = ("kuram" if "0%, 100%, 0%" in a else
               "Cfl3d" if "100%, 0%, 0%" in a else "Overflow")
        out[(model, kod)] = [
            (t["x"][0] + (float(px) - cx0) / (cx1 - cx0) * (t["x"][1] - t["x"][0]),
             t["y"][0] + (float(py) - cy0) / (cy1 - cy0) * (t["y"][1] - t["y"][0]))
            for px, py in re.findall(r"(-?\d+\.?\d*)[ ,](-?\d+\.?\d*)", d.group(1))]
    return out


def deger(egri, x):
    """Egrinin x'teki degeri (en yakin dugum)."""
    return min(egri, key=lambda t: abs(t[0] - x))[1]


def eksen_denetimi(sekil="4.1"):
    """Eksen etiketlerinin konumlari varsayilan aralikla dogrusal mi?

    Dogruysa artiklar SABIT cikar (glif sol kenari yanliligi). Yanlissa
    yelpaze gibi acilir. Doner: (sacilim, artiklar).
    """
    t = SEKIL[sekil]
    e = t.get("etiket")
    if e is None:
        return None, None
    tx0, olcek = e["tx"]
    cx0, cx1 = t["cerceve"][0], t["cerceve"][1]
    xa, xb = t["x"]
    artik = []
    for deger, sayfa_x in e["nokta"]:
        px = cx0 + (deger - xa) / (xb - xa) * (cx1 - cx0)
        artik.append(tx0 + olcek * px - sayfa_x)
    ort = sum(artik) / len(artik)
    sac = (sum((a - ort) ** 2 for a in artik) / len(artik)) ** 0.5
    return sac, artik


def kalibrasyon_denetimi():
    """Coles egrisi log yasasina oturuyor mu? Oturmuyorsa okuma gecersiz."""
    c = egriler("4.2")[("SST", "kuram")]
    kotu = []
    for yp in (100, 150, 200, 300):
        fark = deger(c, math.log10(yp)) - ((1 / KAPPA) * math.log(yp) + B)
        if abs(fark) > 0.10:
            kotu.append((yp, fark))
    return kotu


if __name__ == "__main__":
    sac, artik = eksen_denetimi("4.1")
    print("EKSEN DENETIMI  (Sekil 4.1, x ekseni etiket konumlari)")
    print("   artiklar: %s" % " ".join("%+.2f" % a for a in artik))
    print("   sacilim %.4f -> %s" % (sac, "gecerli" if sac < 0.05 else "GECERSIZ"))
    print()
    kotu = kalibrasyon_denetimi()
    print("KALIBRASYON DENETIMI  (Coles egrisi ile log yasasi)")
    c = egriler("4.2")[("SST", "kuram")]
    for yp in (30, 50, 100, 200, 300, 500):
        log = (1 / KAPPA) * math.log(yp) + B
        print("   y+=%4d   sekil %7.3f   log yasasi %7.3f   fark %+6.3f"
              % (yp, deger(c, math.log10(yp)), log, deger(c, math.log10(yp)) - log))
    print("   -> %s" % ("GECERSIZ: " + str(kotu) if kotu else
                        "gecerli (y+ 100-300 arasi sapma < 0,10)"))
    for s in ("4.1", "4.2"):
        e = egriler(s)
        print("\nSekil %s: %d egri" % (s, len(e)))
        for k in sorted(e):
            print("   %-6s %-9s %5d dugum" % (k[0], k[1], len(e[k])))
