# -*- coding: utf-8 -*-
"""Govde ic hacmi yuke yetiyor mu?

Kanat-govde yuku govdenin ICINDE tasir. Hacim, kalinlik dagilimindan gelir ve
sabittir; gorev ise yukun YOGUNLUGUNU belirler. Bu yuzden "hangi gorev" sorusu
yapiyi etkiler ama once sunun sorulmasi gerekir: yuk zaten siğiyor mu?

NACA 00xx kesit alani ~ 0.6853 * t * c.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from planform import istasyonlar, olcuier

KULLANILABILIR = 0.55        # brut ic hacmin yapi/kaplama disinda kalan payi

KALEMLER = [("yakit (benzin)", 8.0, 0.74),
            ("pil tamponu (Li-ion)", 1.8, 2.0),
            ("motor + jenerator", 8.0, 1.3),
            ("aviyonik ve kumanda", 4.0, 1.5)]
YUK_KG = 13.0


def brut_hacim(olcek=1.0):
    ist, _, _ = istasyonlar(n=400)
    h = 0.0
    for a, b in zip(ist[:-1], ist[1:]):
        dy = (b[0] - a[0]) * olcek
        c = 0.5 * (a[2] + b[2]) * olcek
        tc = 0.5 * (a[3] + b[3])
        h += 0.6853 * tc * c * c * dy
    return 2 * h


if __name__ == "__main__":
    for ad, olcek, yuk in (("HAFIF 50 kg", 1.0, YUK_KG),
                           ("AGIR 1000 kg", 3.3449, YUK_KG * 20)):
        V = brut_hacim(olcek) * 1000
        kul = V * KULLANILABILIR
        dolu = sum(kg * olcek ** 3 / yog for _, kg, yog in KALEMLER)
        kalan = kul - dolu
        print(f"\n{ad}: brut {V:.0f} L · kullanilabilir {kul:.0f} L · "
              f"yuksuz dolum {dolu:.0f} L · yuke kalan {kalan:.0f} L")
        print(f"  {yuk:.0f} kg yuk icin gereken yogunluk >= {yuk/kalan:.2f} kg/L")
        print("  su 1.0 · elektronik 0.8 · kopuk kargo 0.3 kg/L  ->  "
              f"{'hepsi sigar' if yuk/kalan < 0.3 else 'kontrol gerekir'}")
    print("\nSonuc: konfigurasyon hacim degil KUTLE sinirli. Gorev secimi ic hacmi"
          "\nzorlamiyor; yapiyi ve yuk yollarini etkiliyor, ki o da kutle butcesidir.")
