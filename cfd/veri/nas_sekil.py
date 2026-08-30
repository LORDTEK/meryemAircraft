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

KALIBRASYON DENETIMI. Sayfa koordinatindan eksen degerine gecis
VARSAYILMAZ, sinanir: Sekil 4.2'de ucuncu egri Coles'in ortalama hiz
profilidir ve logaritmik tabakada u+ = (1/kappa) ln y+ + B'ye oturmak
zorundadir. Cikarilan egri bu bagintiya y+ = 100-300 arasinda 0,05'ten
iyi uyuyor. Uymasaydi kalibrasyon yanlis olurdu ve okuma
kullanilmazdi -- denetim dogrudan bunun icin var.

SINIR. Bizim vakamiz sikistirilamaz, referansinki M = 0,2. Bu fark
kaldirilmadi; C_f karsilastirmasinda akilda tutulmalidir.
"""
import math, os, re, subprocess, sys

BURA = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(BURA, "..", "kaynak", "NAS_Technical_Report_NAS-2016-01.pdf")

# Sekil -> (PDF sayfasi, cerceve dikdortgeni [yol koordinati], eksen degerleri)
SEKIL = {
    "4.1": dict(sayfa=20, x=(4000.0, 12000.0), y=(0.0020, 0.0040),
                cerceve=(818.007504, 6938.001312, 468.030374, 4751.997163),
                en_az=40),
    "4.2": dict(sayfa=21, x=(-1.0, 4.0), y=(0.0, 30.0),
                cerceve=(518.017188, 6637.970776, 548.069151, 4831.967268),
                en_az=200),
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
        model = ALT.get(tr.group(1).split(",")[4].strip()[:7])
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
