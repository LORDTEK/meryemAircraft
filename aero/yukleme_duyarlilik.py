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
import kararlilik as K                                      # noqa: E402

CL_SEYIR = 0.4497


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
    o = K.olcuier()
    ac = asb.Airplane(wings=[kanat_sekilli(burulma_uc, sekil)],
                      s_ref=o["alan"], b_ref=o["aciklik"], c_ref=K.mac()[0],
                      xyz_ref=[x_ref, 0.0, 0.0])
    r = asb.VortexLatticeMethod(
        airplane=ac, op_point=asb.OperatingPoint(velocity=hiz, alpha=alfa),
        spanwise_resolution=K.SPAN_COZ,
        chordwise_resolution=K.VETER_COZ).run()
    return float(r["CL"]), float(r["Cm"])


def alfa_icin_CL(burulma_uc, sekil, x_ref, hedef=CL_SEYIR):
    alt, ust = -8.0, 16.0
    for _ in range(14):
        mid = 0.5 * (alt + ust)
        if kos(burulma_uc, sekil, mid, x_ref)[0] < hedef:
            alt = mid
        else:
            ust = mid
    return 0.5 * (alt + ust)


def tarafsiz(burulma_uc, sekil, dx=0.02):
    """dC_m/dC_L = 0 olan x_ref."""
    a1, a2 = 2.0, 6.0
    CL1, Cm1 = kos(burulma_uc, sekil, a1, 0.0)
    CL2, Cm2 = kos(burulma_uc, sekil, a2, 0.0)
    s0 = (Cm2 - Cm1) / (CL2 - CL1)
    CL1b, Cm1b = kos(burulma_uc, sekil, a1, dx)
    CL2b, Cm2b = kos(burulma_uc, sekil, a2, dx)
    s1 = (Cm2b - Cm1b) / (CL2b - CL1b)
    return -s0 / ((s1 - s0) / dx)


def denge_burulmasi(sekil, x_cg=0.0):
    """Seyir C_L'inde C_m = 0 veren burulma (derece)."""
    alt, ust = -18.0, 2.0
    for _ in range(12):
        tw = 0.5 * (alt + ust)
        a = alfa_icin_CL(tw, sekil, x_cg)
        if kos(tw, sekil, a, x_cg)[1] < 0.0:
            ust = tw
        else:
            alt = tw
    return 0.5 * (alt + ust)


if __name__ == "__main__":
    mac_uz = K.mac()[0]
    print("YUKLEME SEKLI DUYARLILIGI -- RANS DEGIL, RANS'IN SONUCUNU SINIRLAMA")
    print("MAC = %.4f m" % mac_uz)
    print()
    print("Yukleme sekli, acikligin ortasindan kontrollu bicimde")
    print("bozuluyor; kok ve uc burulmasi degismiyor. Her sekilde")
    print("tarafsiz nokta ve denge burulmasi yeniden cozuluyor.")
    print()
    print("%-14s %13s %13s %14s %13s"
          % ("sekil (derece)", "x_np (m)", "Dx_np (%MAC)", "denge burul.", "D burul (der)"))
    taban_np = tarafsiz(-9.0, 0.0)
    taban_tw = denge_burulmasi(0.0)
    for sekil in (0.0, +1.0, -1.0, +2.0, -2.0):
        xnp = tarafsiz(-9.0, sekil)
        tw = denge_burulmasi(sekil)
        print("%-14.1f %13.4f %13.2f %14.2f %13.2f"
              % (sekil, xnp, 100 * (xnp - taban_np) / mac_uz, tw, tw - taban_tw))
    print()
    print("Esikler (disaridan onerilen): tarafsiz nokta %5 MAC, burulma 1 derece.")
