# -*- coding: utf-8 -*-
"""ISKOZ ACIKLIK VERIMI -- burulmus kanadin Oswald verimi.

NEDEN VAR. Makale iki ayri buyuklugu kullaniyordu ve ikisi ayni sey degil:

  inviscid e   : VLM'in verdigi sey. INDUKLENEN surtunmenin eliptik
                 idealden sapmasi. Burulmasizda 0,993; -9 derece
                 washout'ta 0,865.
  Oswald e     : surtunme kurulusunun ihtiyaci olan sey. Yukaridakine
                 EK OLARAK, profil surtunmesinin C_L ile artan kismini
                 da tasir. Makalede 0,85 VARSAYILMISTI.

Ikisi arasindaki orani makale VARSAYIYORDU (S1). Bu modul varsaymiyor,
hesapliyor.

YONTEM (Sugar Gabor & Botez'in dogrusal-olmayan VLM'i ile ayni sinif):

  1. VLM burulmus kanadi cozer; her aciklik seridinin YEREL c_l'i
     panel kuvvetlerinden cikarilir.
  2. Her seritte 2-B agdali cozum (NeuralFoil, XFOIL uzerine egitilmis)
     o seridin KENDI c_l'inde yapilir -- sifir kaldirmada DEGIL.
     Bu, cd0.py'den tek farkimiz; cd0.py C_D0 tanimi geregi sifirda okur.
  3. C_Dp = (2/S) integral c_d(y) c(y) dy
  4. C_D = C_Di + C_Dp bir dizi C_L'de kurulur, parabol uydurulur,
     e_Oswald = 1/(pi AR B).

SURUKLEME AYRISTIRMASI -- ve neden cift sayim YOK:
  cd0.py'nin verdigi C_D0, profil surtunmesinin SIFIR KALDIRMADAKI
  degeridir. Buradaki C_Dp(C_L) ise ayni integralin C_L'e bagli hali.
  Oswald verimi, C_Dp'nin C_L ile ARTAN kismini induklenene ekler;
  sabit kismi C_D0'dir ve orada kalir. Parabol uydurmasi bu ayrimi
  kendiliginden yapar: A sabiti C_D0'a, B C_L^2 katsayisi Oswald'a.

OK ACISI. Serit kuramı ok acisini ihmal eder; kok ok acimiz 45 derece.
Iki secenek var ve ikisi de hesaplanip ARALIK olarak veriliyor:
  "akim yonlu"  : yerel veter, serbest akim hizi. cd0.py ile AYNI
                  konvansiyon -- bu yuzden ana sonuc budur, aksi halde
                  C_D0 ile bu modulun sayilari toplanamaz.
  "normal kesit": basit-ok kurami. V_n = V cos L, c_n = c cos L,
                  c_l_n = c_l / cos^2 L. Duyarlilik olarak veriliyor.
Hangisinin dogru oldugunu bu modul SECMIYOR; ikisini de yaziyor.

SINIR -- ve bu sinir cd0.py'nin de sinirIDIR: VLM kesitleri simetrik
NACA00xx. Makalenin tarif ettigi kamber/refleks dagilimi modelde YOK.
Yani buradaki c_d(c_l), o c_l'i SIMETRIK bir kesitle ureten bir kanadin
profil surtunmesidir. Kamberli bir kesit ayni c_l'i daha kucuk alfada
ve genellikle daha kucuk c_d ile uretir. Dolayisiyla buradaki Oswald
verimi bir ALT SINIR sayilmalidir.
"""
import sys, os, math
import numpy as np
import aerosandbox as asb

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from planform import istasyonlar, olcuier, P
from vlm import SPAN_COZ, VETER_COZ, KESIT_SAYISI

RHO, NU = 1.225, 1.46e-5
V_SEYIR = 30.0
CL_SEYIR = 0.45
BURULMA_TRIM = -9.0          # 7.6'nin denge cozumu


def skaler(x):
    return float(np.asarray(x).ravel()[0])


def kanat_kur(burulma_uc=0.0, kesit=None):
    """vlm.kanat_kur ile ayni, ama DOGRUSAL burulma ekliyor."""
    ist, yari, _ = istasyonlar(n=200)
    idx = np.linspace(0, len(ist) - 1, kesit or KESIT_SAYISI).astype(int)
    xsecs = []
    for i in idx:
        y, x, veter, tc, _ = ist[i]
        kal = int(round(tc * 100))
        xsecs.append(asb.WingXSec(
            xyz_le=[x, y, 0.0], chord=veter,
            twist=burulma_uc * (y / yari),
            airfoil=asb.Airfoil(f"naca00{kal:02d}")))
    return asb.Wing(name="govde", symmetric=True, xsecs=xsecs)


def _ok_acisi(y, n=200):
    ist, _, _ = istasyonlar(n=n)
    ys = np.array([a[0] for a in ist])
    ok = np.array([a[4] for a in ist])
    return np.interp(np.abs(y), ys, ok)


def _veter(y, n=200):
    ist, _, _ = istasyonlar(n=n)
    ys = np.array([a[0] for a in ist])
    cs = np.array([a[2] for a in ist])
    return np.interp(np.abs(y), ys, cs)


def _tc(y, n=200):
    ist, _, _ = istasyonlar(n=n)
    ys = np.array([a[0] for a in ist])
    t = np.array([a[3] for a in ist])
    return np.interp(np.abs(y), ys, t)


def serit_yukleri(alfa, burulma_uc=0.0, hiz=V_SEYIR, sr=None, cr=None):
    """VLM cozup her aciklik seridinin yerel c_l'ini dondurur.

    Doner: (seritler, CL_cozucu, CDi_cozucu, o)
    seritler: her biri (y, veter, t/c, ok, dy, c_l_yerel)
    """
    o = olcuier()
    ucak = asb.Airplane(wings=[kanat_kur(burulma_uc)], s_ref=o["alan"],
                        b_ref=o["aciklik"], c_ref=0.6514)
    cozucu = asb.VortexLatticeMethod(
        airplane=ucak, op_point=asb.OperatingPoint(velocity=hiz, alpha=alfa),
        spanwise_resolution=sr or SPAN_COZ,
        chordwise_resolution=cr or VETER_COZ)
    r = cozucu.run()

    F = np.asarray(cozucu.forces_geometry, dtype=float)      # (n,3)
    merkez = np.asarray(cozucu.vortex_centers, dtype=float)  # (n,3)
    a = math.radians(alfa)
    # Geometri eksenlerinde serbest akim ~ (cos a, 0, sin a);
    # kaldirma yonu ona dik, x-z duzleminde.
    e_L = np.array([-math.sin(a), 0.0, math.cos(a)])
    e_D = np.array([math.cos(a), 0.0, math.sin(a)])
    L_panel = F @ e_L
    D_panel = F @ e_D

    q = 0.5 * RHO * hiz ** 2
    # Serit genisligi PANEL GEOMETRISINDEN alinir, komsu merkezlerden
    # DEGIL: merkezlerden turetince en distaki serit yarim genislik
    # kadar disari tasiyor ve toplam aciklikk %0,14 asiyordu. Boyle
    # kucuk bir tasma bile integrali dogrudan sisirir.
    sol = np.asarray(cozucu.left_vortex_vertices, dtype=float)[:, 1]
    sag = np.asarray(cozucu.right_vortex_vertices, dtype=float)[:, 1]
    dy_panel = np.abs(sag - sol)
    ys = merkez[:, 1]
    anahtar = np.round(ys, 6)
    seritler = []
    for yv in np.unique(anahtar):
        m = anahtar == yv
        c = float(_veter(yv))
        seritler.append(dict(y=float(yv), veter=c, tc=float(_tc(yv)),
                             ok=float(_ok_acisi(yv)), L=float(L_panel[m].sum()),
                             dy=float(dy_panel[m].mean())))
    for s in seritler:
        s["cl"] = s["L"] / (q * s["veter"] * s["dy"])
    return (seritler, skaler(r["CL"]), skaler(r["CD"]), o,
            float(L_panel.sum()), float(D_panel.sum()), q)


def denetim(alfa=4.0, burulma_uc=0.0):
    """SERIT TOPLAMI COZUCUNUN C_L'INE ESIT MI?

    Bu modulun butun sonuclari serit ayristirmasina dayaniyor. Once o
    ayristirmanin dogru oldugu gosterilmeli, sonra uzerine hesap kurulmali.
    """
    ser, CL, CD, o, Ltop, Dtop, q = serit_yukleri(alfa, burulma_uc)
    CL_serit = sum(s["L"] for s in ser) / (q * o["alan"])
    CL_kuvvet = Ltop / (q * o["alan"])
    testler = [
        ("serit toplami = cozucu C_L", abs(CL_serit - CL) < 1e-6,
         "serit %.6f, cozucu %.6f" % (CL_serit, CL)),
        ("panel kuvvet toplami = cozucu C_L", abs(CL_kuvvet - CL) < 1e-6,
         "kuvvet %.6f, cozucu %.6f" % (CL_kuvvet, CL)),
        ("serit genislikleri toplami = yari aciklik x 2",
         abs(sum(s["dy"] for s in ser) - o["aciklik"]) < 1e-4,
         "toplam %.4f, aciklik %.4f" % (sum(s["dy"] for s in ser),
                                        o["aciklik"])),
        ("yerel c_l hicbir seritte saticma degil",
         all(-2.0 < s["cl"] < 2.5 for s in ser),
         "c_l araligi %.3f .. %.3f" % (min(s["cl"] for s in ser),
                                       max(s["cl"] for s in ser))),
    ]
    return testler, ser, CL, CD, o


# ---------------------------------------------------------------------
# 2-B AGDALI COZUM: seridin KENDI c_l'inde
# ---------------------------------------------------------------------
_NF = {}


def _nf(kal, alfa, Re, tetikli):
    k = (kal, round(alfa, 4), round(math.log10(max(Re, 1.0)), 4), tetikli)
    if k not in _NF:
        kw = dict(alpha=alfa, Re=Re, model_size="xlarge")
        if tetikli:
            kw.update(xtr_upper=0.05, xtr_lower=0.05)
        r = asb.Airfoil(f"naca00{kal:02d}").get_aero_from_neuralfoil(**kw)
        _NF[k] = (skaler(r["CL"]), skaler(r["CD"]))
    return _NF[k]


def cd_hedef_cl(kal, cl_hedef, Re, tetikli, tur=40):
    """Kesit c_l = cl_hedef verecek alfayi ARAR, c_d'yi ORADA okur.

    Dogrusal ara deger YOK. Daha once C_Di'yi dogrusal ara degerle
    bulmaya calisip e > 1 (fiziksel olmayan) sonuc almistim; ayni
    hatayi burada tekrarlamiyoruz -- alfa ikiye bolerek aranir.
    """
    lo, hi = -14.0, 18.0
    cl_lo, _ = _nf(kal, lo, Re, tetikli)
    cl_hi, _ = _nf(kal, hi, Re, tetikli)
    if not (cl_lo <= cl_hedef <= cl_hi):
        # kesit bu c_l'i uretemiyor (perdovites disinda); ucu dondur
        a = lo if cl_hedef < cl_lo else hi
        cl, cd = _nf(kal, a, Re, tetikli)
        return cd, a, cl, False
    for _ in range(tur):
        mid = 0.5 * (lo + hi)
        cl, cd = _nf(kal, mid, Re, tetikli)
        if cl < cl_hedef:
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-4:
            break
    a = 0.5 * (lo + hi)
    cl, cd = _nf(kal, a, Re, tetikli)
    return cd, a, cl, True


def profil_direnci(seritler, o, hiz=V_SEYIR, tetikli=True, ok_duzeltme=False):
    """C_Dp = (1/S) integral c_d(y) c(y) dy, iki yari dahil.

    ok_duzeltme=False : akim yonlu serit (cd0.py ile AYNI konvansiyon)
    ok_duzeltme=True  : basit-ok kurami (duyarlilik)
    """
    toplam = 0.0
    ayrinti = []
    kapsandi = True
    for s in seritler:
        c, cl, L = s["veter"], s["cl"], math.radians(s["ok"])
        kal = min(max(int(round(s["tc"] * 100)), 6), 30)
        if ok_duzeltme:
            cosL = math.cos(L)
            c_e = c * cosL
            V_e = hiz * cosL
            cl_e = cl / (cosL ** 2)
        else:
            c_e, V_e, cl_e = c, hiz, cl
        Re = V_e * c_e / NU
        cd, alfa_e, cl_ger, ok = cd_hedef_cl(kal, cl_e, Re, tetikli)
        kapsandi = kapsandi and ok
        if ok_duzeltme:
            # normal duzlemdeki surtunmeyi kanat eksenine tasi
            katki = cd * (math.cos(L) ** 3) * c * s["dy"]
        else:
            katki = cd * c * s["dy"]
        toplam += katki
        ayrinti.append((s["y"], c, Re, cl_e, alfa_e, cd))
    return toplam / o["alan"], ayrinti, kapsandi


# ---------------------------------------------------------------------
# SURUKLEME POLARI VE OSWALD VERIMI
# ---------------------------------------------------------------------
def polar(burulma_uc, alfalar, hiz=V_SEYIR, tetikli=True, ok_duzeltme=False):
    """Her alfada C_L, C_Di (VLM) ve C_Dp (serit, yerel c_l'de)."""
    cik = []
    for a in alfalar:
        ser, CL, CDi, o, _, _, _ = serit_yukleri(a, burulma_uc, hiz)
        CDp, ayr, kapsandi = profil_direnci(ser, o, hiz, tetikli, ok_duzeltme)
        cik.append(dict(alfa=a, CL=CL, CDi=CDi, CDp=CDp, CD=CDi + CDp,
                        kapsandi=kapsandi, ser=ser, ayr=ayr))
    return cik, o


def oswald(pol, o):
    """C_D = A + B (C_L - C_L0)^2 uydur; e = 1/(pi AR B).

    Genel parabol kullaniliyor cunku burulmus/kamberli bir kanatta en
    kucuk surukleme C_L = 0'da DEGILDIR; C_L0'i sifira zorlamak e'yi
    yapay olarak dusurur.
    """
    CL = np.array([p["CL"] for p in pol])
    CD = np.array([p["CD"] for p in pol])
    k = np.polyfit(CL, CD, 2)                 # k0 CL^2 + k1 CL + k2
    B = k[0]
    CL0 = -k[1] / (2 * k[0])
    A = k[2] - k[0] * CL0 ** 2
    art = CD - np.polyval(k, CL)
    e = 1.0 / (math.pi * o["AR"] * B)
    return dict(B=B, CL0=CL0, A=A, e=e, artik=float(np.max(np.abs(art))))


def inviscid_e(pol, o):
    """Yalniz C_Di'den: e_inv = C_L^2 / (pi AR C_Di). VLM'in verdigi sey."""
    out = []
    for p in pol:
        if abs(p["CDi"]) > 1e-9:
            out.append((p["CL"], p["CL"] ** 2 / (math.pi * o["AR"] * p["CDi"])))
    return out


if __name__ == "__main__":
    print("=" * 74)
    print("ISKOZ ACIKLIK VERIMI -- burulmus kanadin Oswald verimi")
    print("=" * 74)
    print()
    print("-" * 74)
    print("0. DENETIM -- serit ayristirmasi cozucuyle tutuyor mu?")
    print("-" * 74)
    testler, ser0, CL0, CD0, o = denetim(alfa=4.0, burulma_uc=0.0)
    hepsi = True
    for ad, gecti, aciklama in testler:
        hepsi = hepsi and gecti
        print("  %s  %-48s %s" % ("GECTI" if gecti else "KALDI", ad, aciklama))
    print()
    if not hepsi:
        print("  DENETIM KALDI -- asagidaki hicbir sayi kullanilmamalidir.")
        sys.exit(1)
    print("  Denetim gecti. Ayristirma cozucunun C_L'ini alti hanede")
    print("  yeniden uretiyor, yani asagidaki serit yukleri cozumun")
    print("  kendisidir, ona benzeyen bir sey degil.")
    print()

    ALFA_DUZ = (1.0, 2.5, 4.0, 5.5, 7.0)
    ALFA_BUR = (4.0, 5.5, 7.0, 8.5, 10.0)

    sonuc = {}
    for etiket, bur, alf in (("burulmasiz", 0.0, ALFA_DUZ),
                             ("trim (-9 derece washout)", BURULMA_TRIM,
                              ALFA_BUR)):
        print("-" * 74)
        print("POLAR -- %s" % etiket)
        print("-" * 74)
        pol, o = polar(bur, alf)
        print("  %6s %8s %10s %10s %10s" %
              ("alfa", "C_L", "C_Di", "C_Dp", "C_D"))
        for p in pol:
            print("  %6.2f %8.4f %10.5f %10.5f %10.5f"
                  % (p["alfa"], p["CL"], p["CDi"], p["CDp"], p["CD"]))
        f = oswald(pol, o)
        inv = inviscid_e(pol, o)
        print()
        print("  parabol: C_D = %.5f + %.5f (C_L %+.4f)^2   (en buyuk artik %.2e)"
              % (f["A"], f["B"], -f["CL0"], f["artik"]))
        print("  OSWALD e = %.4f" % f["e"])
        print("  inviscid e (C_Di'den): " +
              "  ".join("%.3f@CL%.2f" % (v, c) for c, v in inv))
        print()
        sonuc[etiket] = (f, inv, pol, o)

    print("=" * 74)
    print("S1'IN CEVABI")
    print("=" * 74)
    fd = sonuc["burulmasiz"][0]
    fb = sonuc["trim (-9 derece washout)"][0]
    invb = sonuc["trim (-9 derece washout)"][1]
    e_inv_seyir = None
    for c, v in invb:
        if e_inv_seyir is None or abs(c - CL_SEYIR) < abs(e_inv_seyir[0] - CL_SEYIR):
            e_inv_seyir = (c, v)
    print("  burulmasiz Oswald e = %.4f" % fd["e"])
    print("  TRIM   Oswald e     = %.4f" % fb["e"])
    print("  trim inviscid e     = %.4f  (C_L = %.2f'de)"
          % (e_inv_seyir[1], e_inv_seyir[0]))
    print()
    print("  ORAN (Oswald / inviscid) = %.4f" % (fb["e"] / e_inv_seyir[1]))
    print("  Makale bu orani 0,85-0,90 VARSAYIYORDU. Yukaridaki hesaplanmis.")
    print()
    print("  Makalenin kullandigi deger: e = 0,85 (varsayim)")
    print("  Hesaplanan          : e = %.4f" % fb["e"])
    fark = 100 * (fb["e"] - 0.85) / 0.85
    print("  Fark: %+.1f%%  -> varsayim %s" %
          (fark, "IYIMSER" if fark < 0 else "TEMKINLI"))
    print()

    print("-" * 74)
    print("OK ACISI DUYARLILIGI -- seyir noktasinda")
    print("-" * 74)
    ser, CL, CDi, o, _, _, _ = serit_yukleri(7.0, BURULMA_TRIM)
    for ad, duz in (("akim yonlu (cd0.py ile ayni)", False),
                    ("normal kesit (basit-ok)", True)):
        CDp, _, kap = profil_direnci(ser, o, V_SEYIR, True, duz)
        print("  %-32s C_Dp = %.5f%s" % (ad, CDp, "" if kap else "  (bazi seritler kapsam disi)"))
    print()
    print("  Bu iki sayi arasindaki fark, ok acisi konvansiyonunun")
    print("  getirdigi belirsizliktir. Ana sonuc AKIM YONLU olanla")
    print("  kuruldu, cunku cd0.py'nin C_D0'i da oyle kuruldu; aksi")
    print("  halde iki sayi toplanamaz.")
