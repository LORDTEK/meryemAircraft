# -*- coding: utf-8 -*-
"""meryemAircraft planformunda girdap-kafes cozumu.

Amac: makalede VARSAYILAN iki sayiyi hesaplanmisla degistirmek —
  - aciklik verimi  e   (varsayim 0.85)
  - kaldirma egrisi egimi CL_alpha

Cozucu: AeroSandbox VortexLatticeMethod.

YAKINSAMA -- DUZELTILDI (02.09.2026). Onceki surumde cozunurluk DIKDORTGEN
AR=6 kanatta sinanmis ve bu planforma tasindigi VARSAYILMISTI. Tasinmiyor.
Gercek planformda olculdu (veter cozunurlugu 12 sabit, alfa = 4 derece):

    52 serit (eski varsayilan)   e = 1.0067   <- FIZIKSEL SINIRIN USTUNDE
   104 serit                     e = 0.9890
   216 serit                     e = 0.9845
   Richardson h->0 (p = 1.98)    e = 0.9830

Duzlemsel bir kanatta e, 1'i asamaz; eski varsayilan cozunurluk 1.0067
veriyordu, yani sonuc yakinsamamisti ve bunu asmasindan anlasildi.
Veter yonu de etkiliyor: 104 seritte veter 12 -> 24 ile e 0.9890 -> 0.9936.
Iki yon birlikte dusunuldugunde e yaklasik 0.98-0.99 bandindadir.

CL_alpha ise yakinsamis: 52 seritte 3.874 /rad, 216 seritte 3.842 /rad --
alti kat cozunurlukte %0.8 degisim. Gozlenen mertebe dusuk (p = 0.42), o
yuzden CL_alpha icin Richardson degeri degil OLCULEN aralik verilmelidir.

Varsayilan cozunurluk 104 serite cikarildi; yakinsama sinamasi icin
yakinsama() cagrilabilir.

SINIR: profil kesitleri simetrik NACA olarak alindi (yerel t/c ile). Makalenin
tarif ettigi kamber ve refleks dagilimlari BURADA YOK; dolayisiyla bu kosum
kaldirmanin sifir-alfa degerini degil, EGIMI ve INDUKLENEN SURUKLEMEYI verir.
Bu ikisi kambere birinci mertebede duyarsizdir.
"""
import sys, os, math
import numpy as np
import aerosandbox as asb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from planform import istasyonlar, olcuier

# AeroSandbox'ta spanwise_resolution KESIT CIFTI BASINADIR. Toplam serit
# sayisi = (KESIT_SAYISI - 1) * SPAN_COZ. Dikdortgen kanattaki yakinsama
# sinamasi ~40 serit gerektirdigini gosterdi.
KESIT_SAYISI, SPAN_COZ, VETER_COZ = 14, 8, 12   # 104 serit


def kanat_kur(kesit=None):
    ist, yari, _ = istasyonlar(n=200)
    idx = np.linspace(0, len(ist) - 1, kesit or KESIT_SAYISI).astype(int)
    xsecs = []
    for i in idx:
        y, x, veter, tc, _ = ist[i]
        kalinlik = int(round(tc * 100))
        xsecs.append(asb.WingXSec(
            xyz_le=[x, y, 0.0], chord=veter,
            airfoil=asb.Airfoil(f"naca00{kalinlik:02d}")))
    return asb.Wing(name="govde", symmetric=True, xsecs=xsecs)


def kos(alfalar=(0.0, 2.0, 4.0, 6.0), hiz=30.0, kesit=None, sr=None, cr=None):
    o = olcuier()
    kanat = kanat_kur(kesit)
    ucak = asb.Airplane(wings=[kanat], s_ref=o["alan"],
                        b_ref=o["aciklik"], c_ref=o["alan"] / o["aciklik"])
    sonuc = []
    for a in alfalar:
        r = asb.VortexLatticeMethod(
            airplane=ucak, op_point=asb.OperatingPoint(velocity=hiz, alpha=a),
            spanwise_resolution=sr or SPAN_COZ,
            chordwise_resolution=cr or VETER_COZ).run()
        sonuc.append((a, float(r["CL"]), float(r["CD"])))
    return o, sonuc


if __name__ == "__main__":
    o, s = kos()
    print(f"planform: aciklik {o['aciklik']:.3f} m · alan {o['alan']:.4f} m2 · AR {o['AR']:.3f}\n")
    print(f"{'alfa':>6}{'CL':>10}{'CDi':>12}{'e':>9}")
    es = []
    for a, CL, CDi in s:
        e = CL ** 2 / (math.pi * o["AR"] * CDi) if CDi > 1e-9 else float("nan")
        if a > 0:
            es.append(e)
        print(f"{a:6.1f}{CL:10.4f}{CDi:12.6f}{e:9.3f}")
    A = np.array([a for a, _, _ in s]); C = np.array([c for _, c, _ in s])
    egim = np.polyfit(np.deg2rad(A), C, 1)[0]
    print(f"\nCL_alpha = {egim:.3f} /rad = {egim*math.pi/180:.4f} /deg")
    print(f"aciklik verimi e = {np.mean(es):.3f}   (makalede VARSAYILAN: 0.85)")


def yakinsama(alfa=4.0, kafes=((14, 4, 12), (14, 8, 12), (28, 8, 12))):
    """Cozunurluk taramasi. Bu planformda YAPILMALIDIR -- dikdortgen
    kanattaki sinama buraya tasinmiyor (bkz. modul basi)."""
    global KESIT_SAYISI
    o = olcuier()
    eski = KESIT_SAYISI
    cik = []
    try:
        for ks, sr, cr in kafes:
            KESIT_SAYISI = ks
            _o, s = kos(alfalar=(0.0, alfa), sr=sr, cr=cr)
            CL, CDi = s[1][1], s[1][2]
            cik.append(dict(serit=(ks - 1) * sr, veter=cr, CL=CL, CDi=CDi,
                            e=CL ** 2 / (math.pi * o["AR"] * CDi)))
    finally:
        KESIT_SAYISI = eski
    return cik
