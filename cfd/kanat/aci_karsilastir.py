# -*- coding: utf-8 -*-
"""Uc boyutlu CFD aci taramasini VLM ile karsilastirir.

CL_alfa, EN KUCUK KARELERLE uydurulur; iki uc noktadan egim almak,
noktalardan birinde ufak bir yakinsama hatasi varsa egimi oransiz
bozar. Ayrica uydurmanin SABIT TERIMI de raporlanir: kesitler simetrik
(NACA 00xx) ve planformda burulma yok, dolayisiyla sabit terim sifira
yakin OLMALIDIR. Degilse kurulumda bir yanlislik var demektir -- bu,
ayrica yazilmasi gerekmeyen, bedava bir denetimdir.
"""
import math
import os
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BURA, "..", "..", "aero"))


def dogru_uydur(x, y):
    """En kucuk kareler: y = a*x + b. (a, b, en buyuk artik) dondurur."""
    n = len(x)
    sx = sum(x); sy = sum(y)
    sxx = sum(v * v for v in x); sxy = sum(u * v for u, v in zip(x, y))
    payda = n * sxx - sx * sx
    a = (n * sxy - sx * sy) / payda
    b = (sy - a * sx) / n
    kalan = max(abs(v - (a * u + b)) for u, v in zip(x, y))
    return a, b, kalan


def oku(yol):
    """tarama ciktisini okur: 'alfa=A ... CL_CD_yplus=CL CD yplus'."""
    veri = []
    for satir in open(yol):
        if not satir.startswith("alfa="):
            continue
        p = satir.split()
        a = float(p[0].split("=")[1])
        i = satir.index("CL_CD_yplus=")
        q = satir[i + len("CL_CD_yplus="):].split()
        veri.append((a, float(q[0]), float(q[1]), float(q[2])))
    return sorted(veri)


def karsilastir(yol, alfa4=None):
    veri = oku(yol)
    if alfa4:
        veri = sorted(veri + [alfa4])
    from vlm import kos
    o, vs = kos(alfalar=tuple(a for a, _, _, _ in veri))
    vlm = {a: CL for a, CL, _ in vs}

    print("  planform: aciklik %.3f m · alan %.4f m2 · AR %.3f"
          % (o["aciklik"], o["alan"], o["AR"]))
    print()
    print("   alfa      CFD C_L      VLM C_L    oran    CFD C_D    y+")
    for a, CL, CD, yp in veri:
        # alfa=0'da iki deger de sifir; oran anlamsiz, basilmaz.
        o_s = "  --  " if abs(vlm[a]) < 1e-6 else "%6.3f" % (CL / vlm[a])
        print("   %4.1f    %9.5f    %9.5f  %s   %8.5f  %5.1f"
              % (a, CL, vlm[a], o_s, CD, yp))

    ar = [math.radians(a) for a, _, _, _ in veri]
    ac, bc, kc = dogru_uydur(ar, [CL for _, CL, _, _ in veri])
    av, bv, kv = dogru_uydur(ar, [vlm[a] for a, _, _, _ in veri])
    print()
    print("  CL_alfa (en kucuk kareler):")
    print("    CFD  %.4f /rad  = %.5f /derece   (sabit %+.5f, en buyuk artik %.5f)"
          % (ac, ac * math.pi / 180, bc, kc))
    print("    VLM  %.4f /rad  = %.5f /derece   (sabit %+.5f, en buyuk artik %.5f)"
          % (av, av * math.pi / 180, bv, kv))
    print("    CFD / VLM = %.4f   (fark %%%.1f)" % (ac / av, 100 * (ac / av - 1)))
    print()
    print("  Sabit terim denetimi: kesitler simetrik ve burulma yok,")
    print("  sifira yakin olmali.  CFD sabit = %+.5f" % bc)

    # INDIRGENMIS SURUKLEME -- ayri ve BAGIMSIZ bir karsilastirma.
    #
    # CFD'nin toplam C_D'si sürtünme + basinc + indirgenmis suruklemeyi
    # birlikte tasir; VLM ise yalnizca indirgenmis suruklemeyi (CDi)
    # hesaplar, dogrudan karsilastirilamazlar. Ama alfa=0'daki C_D
    # tasimasiz suruklemedir (kesitler simetrik oldugu icin orada
    # indirgenmis surukleme sifir), dolayisiyla FARK alinirsa geriye
    # tasimaya bagli kisim kalir ve VLM'in CDi'siyle karsilastirilabilir.
    cd0 = dict((a, CD) for a, _, CD, _ in veri).get(0.0)
    if cd0 is not None:
        vcdi = dict((a, CDi) for a, _, CDi in vs)
        print()
        print("  Indirgenmis surukleme (C_D - C_D0, tasimasiz surukleme cikarilmis):")
        print("   alfa    CFD artis    VLM CDi     oran")
        for a, CL, CD, _ in veri:
            if a == 0.0:
                continue
            d = CD - cd0
            print("   %4.1f   %9.6f  %9.6f   %6.3f"
                  % (a, d, vcdi[a], d / vcdi[a] if vcdi[a] else float("nan")))
    return dict(CFD_CL_alfa=ac, VLM_CL_alfa=av, CFD_sabit=bc, veri=veri)


if __name__ == "__main__":
    karsilastir(sys.argv[1] if len(sys.argv) > 1 else "/tmp/aci_sonuc.txt")
