# -*- coding: utf-8 -*-
"""YUKLEME SEKLI DUYARLILIGI -- VLM'in 'iptal olur' savunmasi ne kadar saglam?

NE OLMADIGI, ONCE. Bu betik RANS DEGILDIR. Istenen hesap, ayni trimli
planformun RANS cozumunu VLM'e karsi koymak ve

    K_L(y) = c_l,RANS(y) / c_l,VLM(y)

oraninin acikligi boyunca SABIT olup olmadigina bakmakti. O kosu bu
depoda kurulu: 1,67 M hucreli ag, 4 cekirdekte 12,3 s/adim. Yakinsamis
bir KALDIRMALI cozum icin yaklasik 4 000 adim gerekir, yani ~14 saat --
ve trimli (burulmali) geometri icin ag yeniden uretilmeli. Bu oturumda
yapilmadi ve yapilmis gibi RAPOR EDILMIYOR.

BU BETIK NE YAPIYOR. Savunmanin SONUCUNU sinirliyor. Makale su an diyor
ki: buyukluk hatasi ortak bir carpansa oranlarda iptal olur. Ortak carpan
varsayimi dogruysa iptal TANIM GEREGI olur -- sinanacak bir sey yok.
Sinanabilir olan sorunun tersi: **yukleme SEKLI belli bir miktar
degisirse, tarafsiz nokta ve denge burulmasi ne kadar oynar?**

Yani RANS'in bulacagi yeniden dagilimi bilmiyoruz, ama "su kadar yeniden
dagilim su kadar oynatir" diyebiliyoruz. Boylece "hic siniri yok" olan
maruziyet, "sinirli, ve siniri sudur" haline geliyor.

YONTEM. Burulma dagilimi araciligiyla yukleme sekli kontrollu bicimde
ice/disa kaydiriliyor -- ayni toplam C_L'de. Her sekilde VLM'den
tarafsiz nokta ve denge burulmasi yeniden cozuluyor.

NE ALEYHIMIZE SAYILIR (disaridan onerilen esikler)
  - tarafsiz nokta > %5 MAC oynarsa,
  - ya da denge burulmasi > 1 derece oynarsa,
  VLM turevli denge zinciri yeniden hesaplanmali demektir.
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)

import numpy as np                                          # noqa: E402
import aerosandbox as asb                                   # noqa: E402
import stability as K                                      # noqa: E402

CL_SEYIR = K.CL_SEYIR
X_CG = K.CG_KURAL * K.P["kokVeter"]          # stability.py ile AYNI

# Denge, kok hucum kenarina gore DEGIL agirlik merkezine gore kuruluyor.
# Betigin ilk surumu x_ref = 0 aliyordu: tarafsiz nokta 0,87 m oradayken
# bu devasa bir burun-asagi moment demek ve cozum -81 dereceye kaciyordu.
# Ikiye bolme parantezi [-18, +2] oldugundan eski surum bunu GORMEZ,
# sessizce uca yapisir ve makul gorunen bir tablo basardi.


def kanat_sekilli(burulma_uc, sekil, n=200, kesit=K.BURULMA_KESIT):
    """kararlilik.burulmali_kanat ile AYNI geometri, tek farkla.

    Ayni istasyon listesi, ayni kesitler, ayni cozunurluk kullaniliyor --
    kendi planformumu kurmuyorum. Karsilastirilan seyin tek degiskeni
    yukleme sekli olmali; geometri kurulusu ikinci bir fark getirseydi
    cikan sayi "sekil mi, kurulus mu?" sorusunu acik birakirdi.

    sekil > 0 yuku DISA, < 0 ICE tasir. Bozulma sin(pi eta) ile carpildigi
    icin kokte ve ucta SIFIRDIR: uc burulmasi ve dolayisiyla uc yuklemesi
    degismez, yalnizca aradaki dagilim degisir.
    """
    ist, yari, _ = K.istasyonlar(n=n)
    idx = np.linspace(0, len(ist) - 1, kesit).astype(int)
    xs = []
    for i in idx:
        y, x, c, tc, _ = ist[i]
        eta = y / yari
        tw = burulma_uc * eta + sekil * math.sin(math.pi * eta)
        xs.append(asb.WingXSec(
            xyz_le=[x, y, 0.0], chord=c, twist=tw,
            airfoil=asb.Airfoil("naca00%02d" % int(round(tc * 100)))))
    return asb.Wing(name="govde", symmetric=True, xsecs=xs)


def kos(burulma_uc, sekil, alfa, x_ref, hiz=30.0):
    global SAYAC
    SAYAC += 1
    o = K.olcuier()
    ac = asb.Airplane(wings=[kanat_sekilli(burulma_uc, sekil)],
                      s_ref=o["alan"], b_ref=o["aciklik"], c_ref=K.mac()[0],
                      xyz_ref=[x_ref, 0.0, 0.0])
    r = asb.VortexLatticeMethod(
        airplane=ac, op_point=asb.OperatingPoint(velocity=hiz, alpha=alfa),
        spanwise_resolution=K.SPAN_COZ,
        chordwise_resolution=K.VETER_COZ).run()
    return float(r["CL"]), float(r["Cm"]), float(r["CD"])


SAYAC = 0

# --- Neden ikiye bolme DEGIL --------------------------------------------
# Bu depoda kural: dogrusal aradegerleme yerine ikiye bolme. O kural
# DOGRUSAL OLMAYAN seyler icin kondu (NeuralFoil kesit verisi gibi).
# Burada cozulen sey vorteks kafesidir ve vorteks kafesi hucum acisinda
# da burulmada da TAM OLARAK dogrusaldir: ikisi de sinir kosuluna dogrusal
# girer, cozulen dogrusal denklem takimidir. Dogrusal bir fonksiyonu
# ikiye bolerek aramak bilineni aramaktir -- sekil basina 168 kosu, alti
# sekil icin 1,5 saat, ve sonunda ayni sayi.
#
# Bunun yerine afin harita UC kosuyla kuruluyor ve takim TAM cozuluyor.
# Ama dogrusallik VARSAYILMIYOR: cozum noktasi ayrica KOSULUYOR ve
# artiklari basiliyor. Artik sifira yakin degilse dogrusallik varsayimi
# yanlistir ve tablo gecersizdir -- asagida durduruluyor.


def afin(sekil, x_ref=0.0, a0=2.0, da=4.0, t0=-9.0, dt=-3.0):
    """(alfa, burulma) -> (C_L, C_m) afin haritasi, uc kosuda.

    Donen: taban degerler ve dort kismi turev.
    """
    CL1, Cm1, _ = kos(t0, sekil, a0, x_ref)
    CL2, Cm2, _ = kos(t0, sekil, a0 + da, x_ref)
    CL3, Cm3, _ = kos(t0 + dt, sekil, a0, x_ref)
    return dict(a0=a0, t0=t0, x_ref=x_ref, CL0=CL1, Cm0=Cm1,
                CLa=(CL2 - CL1) / da, Cma=(Cm2 - Cm1) / da,
                CLt=(CL3 - CL1) / dt, Cmt=(Cm3 - Cm1) / dt)


def tarafsiz_afin(h, c_ref):
    """x_np = x_ref - c_ref (dC_m/dC_L) -- stability.py'nin konvansiyonu.

    Sonlu farkla x_ref'i taramaya gerek yok: iliski tam. Yine de ana
    blokta taban sekil icin eski dort kosuluk sonlu fark ile
    karsilastiriliyor. (Betigin ilk surumu bu isareti TERS yazmisti ve
    tarafsiz noktayi 0,865 m ONDE degil ARKADA veriyordu; karsilastirma
    onu yakaladi.)
    """
    return h["x_ref"] - c_ref * (h["Cma"] / h["CLa"])


def _adim(h, b1, b2):
    """Olculmus Jacobian ile 2x2 cozum: (dalfa, dburulma)."""
    det = h["CLa"] * h["Cmt"] - h["CLt"] * h["Cma"]
    return ((b1 * h["Cmt"] - h["CLt"] * b2) / det,
            (h["CLa"] * b2 - b1 * h["Cma"]) / det)


def denge_newton(sekil, h, hedef=CL_SEYIR, tol=1e-6, azami=6):
    """C_L = hedef ve C_m = 0 veren (alfa, burulma).

    Harita TAM afin degil: hem hucum acisi hem burulma VLM'e sinus ve
    kosinusleriyle girer, yani egimler nokta nokta azicik kayar. Tek
    atimlik afin cozum 2e-3 mertebesinde artik birakiyordu. Burada
    Jacobian OLCULMUS degerinde sabit tutulup taban nokta her adimda
    gercek kosuyla yenileniyor -- yani gercek fonksiyon uzerinde Newton,
    durma olcutu de OLCULEN artik. Dogrusallik hicbir yerde varsayilmiyor.
    """
    alfa, tw = h["a0"], h["t0"]
    dA, dT = _adim(h, hedef - h["CL0"], -h["Cm0"])
    alfa, tw = alfa + dA, tw + dT
    for it in range(1, azami + 1):
        CL, Cm, CD = kos(tw, sekil, alfa, h["x_ref"])
        art = max(abs(CL - hedef), abs(Cm))
        if art < tol:
            return alfa, tw, art, CD
        dA, dT = _adim(h, hedef - CL, -Cm)
        alfa, tw = alfa + dA, tw + dT
    return alfa, tw, art, CD


if __name__ == "__main__":
    mac_uz = K.mac()[0]
    print("YUKLEME SEKLI DUYARLILIGI -- RANS DEGIL, RANS'IN SONUCUNU SINIRLAMA")
    print("MAC = %.4f m,  hedef C_L = %.4f,  x_cg = %.4f m"
          % (mac_uz, CL_SEYIR, X_CG))
    print()
    print("Yukleme sekli, acikligin ortasindan kontrollu bicimde")
    print("bozuluyor; kok ve uc burulmasi degismiyor. Her sekilde")
    print("tarafsiz nokta ve denge burulmasi yeniden cozuluyor.")
    print()

    # --- Once cozucunun kendisi sinaniyor --------------------------------
    h0 = afin(0.0, x_ref=X_CG)
    xnp_afin = tarafsiz_afin(h0, mac_uz)

    # Eski sonlu-fark tarafsiz nokta, ayni taban sekil icin (4 kosu).
    dx = 0.02
    CL1, Cm1, _ = kos(-9.0, 0.0, 2.0, X_CG)
    CL2, Cm2, _ = kos(-9.0, 0.0, 6.0, X_CG)
    s0 = (Cm2 - Cm1) / (CL2 - CL1)
    CL1b, Cm1b, _ = kos(-9.0, 0.0, 2.0, X_CG + dx)
    CL2b, Cm2b, _ = kos(-9.0, 0.0, 6.0, X_CG + dx)
    s1 = (Cm2b - Cm1b) / (CL2b - CL1b)
    xnp_fark = X_CG - s0 / ((s1 - s0) / dx)

    # Tarafsiz nokta burulmadan bagimsiz olmali (egimler burulmaya
    # bakmaz); bu da sinaniyor, varsayilmiyor.
    h0b = afin(0.0, t0=-14.0, dt=-3.0, x_ref=X_CG)
    xnp_burulma = tarafsiz_afin(h0b, mac_uz)

    print("COZUCU SINAMASI")
    print("  x_np, afin (2 kosu)            %.5f m" % xnp_afin)
    print("  x_np, sonlu fark (4 kosu)      %.5f m   fark %.3f %%MAC"
          % (xnp_fark, 100 * (xnp_fark - xnp_afin) / mac_uz))
    print("  x_np, burulma -14 der taban    %.5f m   fark %.3f %%MAC"
          % (xnp_burulma, 100 * (xnp_burulma - xnp_afin) / mac_uz))
    print()

    taban_np = xnp_afin
    _t0a, taban_tw, _t0r, taban_cd = denge_newton(0.0, h0)
    AR = K.olcuier()["AR"]
    taban_e = CL_SEYIR ** 2 / (math.pi * AR * taban_cd)

    print("Yukleme sekli GERCEKTEN degisiyor mu? Olcusu aciklik verimi e:")
    print("bozulma yalnizca kucuk bir yeniden dagilimsa e kipirdamaz ve")
    print("tablo hicbir sey siniramaz. Tabanda e = %.4f (3.10: 0,817)."
          % taban_e)
    print()
    print("%-14s %10s %12s %9s %11s %10s %8s %8s %6s"
          % ("sekil (derece)", "x_np (m)", "Dx_np (%MAC)", "alfa",
             "denge bur.", "D bur (der)", "e", "De (%)", "artik"))
    kotu = []
    kayit = []
    for sekil in (0.0, +1.0, -1.0, +2.0, -2.0):
        h = afin(sekil, x_ref=X_CG)
        xnp = tarafsiz_afin(h, mac_uz)
        alfa, tw, art, cd = denge_newton(sekil, h)
        e = CL_SEYIR ** 2 / (math.pi * AR * cd)
        if art > 1e-5:
            kotu.append((sekil, art))
        print("%-14.1f %10.4f %12.2f %9.2f %11.2f %10.2f %8.4f %8.2f %6.0e"
              % (sekil, xnp, 100 * (xnp - taban_np) / mac_uz,
                 alfa, tw, tw - taban_tw, e, 100 * (e - taban_e) / taban_e,
                 art))
        kayit.append((sekil, 100 * (xnp - taban_np) / mac_uz, tw - taban_tw))

    # --- KARAR: bu bir SINIR degil, bir AKTARIM KATSAYISI --------------
    # RANS'in bulacagi yeniden dagilimin ne kadar oldugunu BILMIYORUZ.
    # Bilinen sey artik su: bir derecelik orta-aciklik yeniden dagilimi
    # tarafsiz noktayi ve denge burulmasini su kadar oynatir. Okuyucu
    # kendi yeniden dagilim tahminini bu katsayilarla carpabilir.
    d_np = sum(abs(k[1]) / abs(k[0]) for k in kayit if k[0]) / 4.0
    d_tw = sum(abs(k[2]) / abs(k[0]) for k in kayit if k[0]) / 4.0
    print()
    print("AKTARIM KATSAYILARI (derece basina, ortalama)")
    print("  tarafsiz nokta   %.3f %%MAC / derece  -> %%5 esigi %.0f derecede"
          % (d_np, 5.0 / d_np))
    print("  denge burulmasi  %.3f derece / derece -> 1 der esigi %.1f derecede"
          % (d_tw, 1.0 / d_tw))
    print()
    print("  BAGLAYICI KISIT denge burulmasi, tarafsiz nokta DEGIL --")
    print("  arada %.0f kat var. Yeniden dagilim once dengeyi bozar." % ((5.0 / d_np) / (1.0 / d_tw)))
    print()
    print("Toplam VLM kosusu: %d" % SAYAC)
    print("Esikler (disaridan onerilen): tarafsiz nokta %5 MAC, burulma 1 derece.")
    if kotu:
        print()
        print("!! DUR -- denge cozumu yakinsamadi, tablo gecersiz: %r" % kotu)
        raise SystemExit(1)
