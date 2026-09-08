# -*- coding: utf-8 -*-
"""STATIK YUNUSLAMA KARARLILIGI -- tarafsiz nokta ve statik marj.

NEDEN VAR. 7.6'nin gecis zarfi, EN DAR C_m butcesinin donusun SONUNDA
oldugunu gosterdi: alfa kucuk (5-6 derece), hiz yuksek, butce 0,079
(hafif) / 0,015 (agir). Metin bunu "kuyruksuz bir ucagin siradan denge
sorusu" diye niteledi.

Bir dis denetim buna itiraz etti ve hakli: bu ucakta elevon yok, refleks
kamber tarif edilmemis, ve CG kok veterinin %57-58'inde. Dolayisiyla
"siradan" demek yetmez -- GOSTERILMESI gerekir.

BU MODUL onu gosterir, ya da gosteremedigini soyler. Girdap-kafes
cozumuyle C_m(alfa) hesaplanir, oradan

    dC_m/dC_L = (x_ref - x_np) / c_ref      ->      x_np
    statik marj = (x_np - x_cg) / c_ref

x_cg, kutle butcesinden (kutle.py) gelir: kok veterinin %57'si.

SINIR -- ONEMLI. vlm.py'nin kesitleri SIMETRIK NACA'dir; makalenin tarif
ettigi kamber ve refleks dagilimlari burada YOKTUR. Dolayisiyla:
  - C_m0 (sifir-kaldirmada moment) bu kosumda SIFIRDIR ve gercek degildir;
  - C_m_alfa ve tarafsiz nokta ise kambere birinci mertebede duyarsizdir
    ve HESAPLANABILIR.
Yani bu modul KARARLILIGI verir, DENGEYI (trim) vermez. Denge, kamber ve
refleks tanimlandiktan sonra hesaplanabilir.
"""
import sys, os, math
import numpy as np
import aerosandbox as asb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from planform import istasyonlar, olcuier, P
from vlm import kanat_kur, KESIT_SAYISI, SPAN_COZ, VETER_COZ


def cm_taramasi(alfalar=(0.0, 2.0, 4.0, 6.0), hiz=30.0, x_ref=0.0,
                kesit=None, sr=None, cr=None):
    o = olcuier()
    kanat = kanat_kur(kesit)
    c_ref = o["alan"] / o["aciklik"]
    ucak = asb.Airplane(wings=[kanat], s_ref=o["alan"], b_ref=o["aciklik"],
                        c_ref=c_ref, xyz_ref=[x_ref, 0.0, 0.0])
    cik = []
    for a in alfalar:
        r = asb.VortexLatticeMethod(
            airplane=ucak, op_point=asb.OperatingPoint(velocity=hiz, alpha=a),
            spanwise_resolution=sr or SPAN_COZ,
            chordwise_resolution=cr or VETER_COZ).run()
        cik.append((a, float(r["CL"]), float(r["Cm"])))
    return o, c_ref, cik


def tarafsiz_nokta(x_ref=0.0, **kw):
    """dC_m/dC_L'den tarafsiz noktayi cikarir.

        C_m(x_ref) = C_m(x_np) + C_L (x_ref - x_np)/c_ref
        -> dC_m/dC_L = (x_ref - x_np)/c_ref
        -> x_np = x_ref - c_ref (dC_m/dC_L)
    """
    o, c_ref, cik = cm_taramasi(x_ref=x_ref, **kw)
    CL = np.array([c[1] for c in cik])
    Cm = np.array([c[2] for c in cik])
    egim = np.polyfit(CL, Cm, 1)[0]          # dC_m/dC_L
    x_np = x_ref - c_ref * egim
    return o, c_ref, cik, egim, x_np


if __name__ == "__main__":
    kok = P["kokVeter"]
    print("=" * 74)
    print("STATIK YUNUSLAMA KARARLILIGI -- girdap kafes")
    print("=" * 74)
    o, c_ref, cik, egim, x_np = tarafsiz_nokta(x_ref=0.0)
    print("planform: aciklik %.3f m, alan %.4f m2, c_ref %.4f m, kok veter %.2f m"
          % (o["aciklik"], o["alan"], c_ref, kok))
    print()
    print("  %6s %10s %12s" % ("alfa", "CL", "Cm (kok LE)"))
    for a, CL, Cm in cik:
        print("  %6.1f %10.4f %12.5f" % (a, CL, Cm))
    print()
    print("  dC_m/dC_L (kok hucum kenarina gore) = %+.4f" % egim)
    print("  TARAFSIZ NOKTA x_np = %.4f m = kok veterinin %%%.1f'i"
          % (x_np, 100 * x_np / kok))
    print()
    for ad, oran in (("kutle butcesinden (6.7)", 0.57),):
        x_cg = oran * kok
        sm = (x_np - x_cg) / c_ref
        print("  CG %s: x_cg = %.4f m (kok veterinin %%%.0f'i)"
              % (ad, x_cg, 100 * oran))
        print("  STATIK MARJ = (x_np - x_cg)/c_ref = %+.3f  ->  %s"
              % (sm, "KARARLI" if sm > 0 else "KARARSIZ"))
    print()
    print("  Not: kesitler simetrik; C_m0 bu kosumda sifirdir ve gercek")
    print("  degildir. Bu sonuc KARARLILIGI verir, DENGEYI vermez.")
