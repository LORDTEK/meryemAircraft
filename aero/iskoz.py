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
    onbellek = {}
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
        # Kanat simetrik: +y ve -y seritleri ayni cozumu verir. Ayni
        # 2-B aramayi iki kez yapmanin anlami yok.
        ank = (kal, round(cl_e, 6), round(Re, 1))
        if ank not in onbellek:
            onbellek[ank] = cd_hedef_cl(kal, cl_e, Re, tetikli)
        cd, alfa_e, cl_ger, ok = onbellek[ank]
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


# ⚠️ BURADA BIR KATEGORI HATASI VAR VE ILK KOSUMDA ICINE DUSTUM.
#
# e = C_L^2 / (pi AR C_Di) formulu YALNIZCA burulmasiz (simetrik yuklu)
# bir kanatta gecerlidir; orada C_Di ~ C_L^2'dir. BURULMUS bir kanatta
# induklenen surukleme C_L = 0'da SIFIR DEGILDIR ve en kucuk degerini
# sifirdan farkli bir C_L'de alir. O yuzden bu formul burulmus kanatta
# dusuk C_L'de sacmalar (ilk kosumda C_L = 0,03'te e = 0,024 verdi).
#
# Ayni sebeple, parabol uydurmasindan gelen e (polarin EGRILIGI) ile
# seyir noktasindaki e (oradaki MUTLAK surukleme) FARKLI BUYUKLUKLERDIR.
# Ilk kosumda ikisini boldum ve 1,08 -- yani "Oswald > inviscid" --
# gibi fiziksel olmayan bir oran cikti. Oran anlamsizdi, sonuc degil.
#
# Makale e'yi su denklemde kullaniyor:  C_D = C_D0 + C_L^2/(pi AR e)
# yani e, C_L ile DEGISEN her seyi tasimak zorunda. Dolayisiyla
# makaleyle tutarli tek tanim NOKTA tanimidir:
#
#   e(C_L) = C_L^2 / (pi AR [ C_Di(C_L) + C_Dp(C_L) - C_Dp(0) ])
#
# C_Dp(0) sifir kaldirmadaki profil surtunmesidir ve zaten C_D0'in
# icindedir; cift sayilmasin diye cikariliyor.


def _cdp_sifirda(pol):
    """C_Dp'yi C_L'e karsi parabol uydurup C_L = 0'da oku."""
    CL = np.array([p["CL"] for p in pol])
    CDp = np.array([p["CDp"] for p in pol])
    k = np.polyfit(CL, CDp, 2)
    return float(np.polyval(k, 0.0)), k


def nokta_e(pol, o, CL_hedef=CL_SEYIR):
    """Makaleyle TUTARLI e: seyir C_L'inde, kaldirmaya bagli her sey dahil.

    Doner: (e_oswald, e_inviscid, ayrinti)
    """
    CL = np.array([p["CL"] for p in pol])
    CDi = np.array([p["CDi"] for p in pol])
    CDp = np.array([p["CDp"] for p in pol])
    kD = np.polyfit(CL, CDi, 2)
    kP = np.polyfit(CL, CDp, 2)
    CDi_h = float(np.polyval(kD, CL_hedef))
    CDp_h = float(np.polyval(kP, CL_hedef))
    CDp_0 = float(np.polyval(kP, 0.0))
    kaldirmaya_bagli = CDi_h + (CDp_h - CDp_0)
    e_osw = CL_hedef ** 2 / (math.pi * o["AR"] * kaldirmaya_bagli)
    e_inv = CL_hedef ** 2 / (math.pi * o["AR"] * CDi_h)
    return e_osw, e_inv, dict(CDi=CDi_h, CDp=CDp_h, CDp0=CDp_0,
                              dCDp=CDp_h - CDp_0, toplam=kaldirmaya_bagli)


if __name__ == "__main__":
    import json
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
    print("  Denetim gecti: ayristirma cozucunun C_L'ini ALTI HANEDE")
    print("  yeniden uretiyor. Yani asagidaki serit yukleri cozumun")
    print("  kendisidir, ona benzeyen bir sey degil.")
    print()

    ALFA = {"burulmasiz": (0.0, (1.0, 2.5, 4.0, 5.5, 7.0, 8.5)),
            "trim (-9 washout)": (BURULMA_TRIM,
                                  (4.0, 5.5, 7.0, 8.5, 10.0, 11.5))}
    kayit = {}
    for etiket, (bur, alf) in ALFA.items():
        print("-" * 74)
        print("POLAR -- %s" % etiket)
        print("-" * 74)
        pol, o = polar(bur, alf)
        print("  %6s %9s %10s %10s %10s" % ("alfa", "C_L", "C_Di", "C_Dp", "C_D"))
        for p in pol:
            print("  %6.2f %9.4f %10.5f %10.5f %10.5f"
                  % (p["alfa"], p["CL"], p["CDi"], p["CDp"], p["CD"]))
        e_osw, e_inv, d = nokta_e(pol, o, CL_SEYIR)
        print()
        print("  SEYIR NOKTASINDA (C_L = %.2f):" % CL_SEYIR)
        print("    C_Di                       %.5f" % d["CDi"])
        print("    C_Dp                       %.5f" % d["CDp"])
        print("    C_Dp(C_L=0), C_D0'in icinde %.5f" % d["CDp0"])
        print("    kaldirmaya bagli profil     %.5f" % d["dCDp"])
        print("    kaldirmaya bagli TOPLAM     %.5f" % d["toplam"])
        print("    inviscid e                 %.4f" % e_inv)
        print("    OSWALD e                   %.4f" % e_osw)
        print("    oran (Oswald/inviscid)     %.4f" % (e_osw / e_inv))
        print()
        kayit[etiket] = dict(e_osw=e_osw, e_inv=e_inv, d=d,
                             pol=[{k: v for k, v in p.items()
                                   if k not in ("ser", "ayr")} for p in pol])

    ei = kayit["trim (-9 washout)"]
    ed = kayit["burulmasiz"]
    print("=" * 74)
    print("S1'IN CEVABI")
    print("=" * 74)
    print("  %-22s %10s %10s %8s" % ("", "inviscid e", "Oswald e", "oran"))
    for ad, k in (("burulmasiz", ed), ("TRIM (-9 washout)", ei)):
        print("  %-22s %10.4f %10.4f %8.4f"
              % (ad, k["e_inv"], k["e_osw"], k["e_osw"] / k["e_inv"]))
    print()
    print("  Makale ORANI 0,85-0,90 varsayiyordu. Hesaplanan: %.3f ve %.3f."
          % (ed["e_osw"] / ed["e_inv"], ei["e_osw"] / ei["e_inv"]))
    print("  Yani iskoz cezasi varsayilandan KUCUK.")
    print()
    print("  Ama sonuc yine de varsayimin ALTINDA, cunku baslangic noktasi")
    print("  dusuk: makale e = 0,850 kullaniyor, hesaplanan %.4f." % ei["e_osw"])
    fark = 100 * (ei["e_osw"] - 0.850) / 0.850
    print("  Fark %+.1f%%  ->  varsayim %s" %
          (fark, "IYIMSER" if fark < 0 else "TEMKINLI"))
    CD0A, AR = 0.0248, o["AR"]
    for ad, e in (("makalenin varsayimi", 0.850), ("hesaplanan", ei["e_osw"])):
        LD = CL_SEYIR / (CD0A + CL_SEYIR ** 2 / (math.pi * AR * e))
        print("    e = %.4f (%-20s) -> seyir L/D = %.2f" % (e, ad, LD))
    print()

    print("-" * 74)
    print("OK ACISI -- ve neden basit-ok kurami BURADA kullanilamaz")
    print("-" * 74)
    ser, CL, CDi, o, _, _, _ = serit_yukleri(10.0, BURULMA_TRIM)
    for ad, duz in (("akim yonlu (cd0.py ile ayni)", False),
                    ("normal kesit (basit-ok)", True)):
        CDp, _, kap = profil_direnci(ser, o, V_SEYIR, True, duz)
        print("  %-32s C_Dp = %.5f" % (ad, CDp))
    print()
    print("  Iki sayi ARASINDA IKI KAT fark var, ve bu bir belirsizlik")
    print("  degil, bir GECERSIZLIK isareti. Basit-ok kurami basinc")
    print("  alanini ok cizgisine dik bilesenle kurar; ama SURTUNME")
    print("  yuzeyin uzerinden V ile akar, V cos L ile degil. Surtunmeyi")
    print("  cos^3 ile kucultmek fiziksel degil. Bu yuzden ana sonuc")
    print("  AKIM YONLU serittir -- hem dogru olan o, hem de cd0.py'nin")
    print("  C_D0'i oyle kuruldu, aksi halde iki sayi toplanamaz.")
    print()

    yol = os.path.join(BURA, "iskoz-sonuc.json")
    with open(yol, "w") as f:
        json.dump(kayit, f, indent=1)
    print("  Polar verisi %s dosyasina yazildi." % os.path.basename(yol))
