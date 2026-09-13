# -*- coding: utf-8 -*-
"""RANS'in yeniden dagilimi KAC DERECEYE denk? Zinciri kapatan hesap.

RANS-VLM karsilastirmasi sunu verdi: K(y) = c_l c (y)_RANS / (ayni)_VLM,
ve K/K_L acikligin buyuk bolumunde 1'in %5'i icinde. Yani hata BUYUK
OLCUDE CARPANSAL. Ama "buyuk olcude" bir sayi degil.

3.10'un duyarliligi burulmayi sekil . sin(pi eta) ile bozup denge
burulmasinin ne kadar oynadigini olcmustu: derece basina 0,38 derece,
esik 2,6 derece. O esik "derece" cinsinden; RANS artigi ise "K/K_L
sacilmasi" cinsinden. Ikisi ayni birimde degil ve karsilastirilamaz.

BU BETIK KOPRUYU KURAR: ayni sin(pi eta) bozulmasinin aciklik
yuklemesini NE KADAR degistirdigini olcer, RANS ile ayni normalize
edilmis biçimde. Boylece RANS artigi derece cinsine cevrilir ve 2,6
derecelik esige karsi okunabilir.
"""
import json, os, sys
import numpy as np
import aerosandbox as asb

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
import kararlilik as K                                  # noqa: E402
import yukleme_duyarlilik as Y                          # noqa: E402
from vlm_yukleme import aciklik_yuklemesi               # noqa: E402

V, CL_HEDEF = 30.0, 0.45


def coz(sekil, alfa, burulma=0.0):
    o = K.olcuier()
    ac = asb.Airplane(wings=[Y.kanat_sekilli(burulma, sekil)],
                      s_ref=o["alan"], b_ref=o["aciklik"],
                      c_ref=K.mac()[0], xyz_ref=[0, 0, 0])
    v = asb.VortexLatticeMethod(
        airplane=ac, op_point=asb.OperatingPoint(velocity=V, alpha=alfa),
        spanwise_resolution=K.SPAN_COZ, chordwise_resolution=K.VETER_COZ)
    return v, v.run()


def alfa_icin(sekil, hedef=CL_HEDEF):
    alt, ust = -4.0, 16.0
    for _ in range(16):
        o = 0.5 * (alt + ust)
        if coz(sekil, o)[1]["CL"] < hedef:
            alt = o
        else:
            ust = o
    return 0.5 * (alt + ust)


if __name__ == "__main__":
    rj = json.load(open(os.path.join(BURA, "..", "cfd", "kanat",
                                     "rans_vlm.json")))
    kk = np.array(rj["K"]) / rj["KL"]
    # Uc kutusundaki tek sicrama disarida: orada VLM yuklemesi kucuk ve
    # oran iki kucuk sayinin bolumu. Hem dahil hem haric raporlanir.
    rans_tam = float(kk.max() - kk.min())
    ic = np.sort(kk)[:-1]
    rans_ic = float(ic.max() - ic.min())
    print("RANS artigi (K/K_L sacilmasi)")
    print("  tum kutular        %.3f" % rans_tam)
    print("  en buyuk sapan haric %.3f" % rans_ic)
    print()

    # --- ayni olcuyu sin(pi eta) bozulmasi icin uret -------------------
    print("%-10s %10s %12s" % ("sekil (der)", "alfa", "K/K_L sacilmasi"))
    taban = None
    kayit = []
    for sekil in (0.0, 0.5, 1.0, 2.0):
        a = alfa_icin(sekil)
        v, r = coz(sekil, a)
        yy, clc, gen, yari = aciklik_yuklemesi(v, a)
        if taban is None:
            taban_y, taban_clc = yy, clc
            taban = True
            print("%-10.1f %10.3f %12s" % (sekil, a, "-- taban --"))
            continue
        # Ayni normalizasyon: yerel oran / toplam oran
        oran = np.interp(taban_y, yy, clc) / taban_clc
        oran = oran / (r["CL"] / CL_HEDEF)
        s = float(oran.max() - oran.min())
        kayit.append((sekil, s))
        print("%-10.1f %10.3f %12.3f" % (sekil, a, s))

    # Derece basina sacilma -> RANS artigini dereceye cevir
    egim = np.mean([s / d for d, s in kayit])
    print()
    print("derece basina K/K_L sacilmasi: %.4f" % egim)
    print()
    print("RANS'IN YENIDEN DAGILIMI, DERECE CINSINDEN")
    print("  tum kutular          %.2f derece" % (rans_tam / egim))
    print("  en buyuk sapan haric %.2f derece" % (rans_ic / egim))
    print()
    print("3.10'un esigi: 2,6 derece (1 derecelik denge burulmasi hareketi)")
