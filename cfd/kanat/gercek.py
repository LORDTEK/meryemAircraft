# -*- coding: utf-8 -*-
"""Gercek meryemAircraft planformunun uc boyutlu agi.

Geometri UYDURULMUYOR: aero/planform.py'nin istasyonlari kullaniliyor.
O dosya ok acisi yasalarindan kokten uca (y, x_hucum, veter, t/c, ok)
uretiyor ve kunye degerleriyle sinanmis durumda.

Kesit kalinligi kokte %25, ucta %12; CAgi dort haneli simetrik NACA
uretecine bu yerel t/c ile cagriliyor.

UC KAPANISI -- COZULMEMIS. C-agi yigininda uc duzlemi, profilin
ETRAFINI saran bir izgaradir; profilin KESITI aga dahil degildir, yani
o duzlemde kanadin ucunu kapatacak yuz yoktur. Uc yamasi
  - symmetryPlane yapilirsa kanat aynalanir: gercek uc yok, uc girdabi yok
  - patch yapilirsa uc acik kalir
Ikisi de gercek bir sonlu kanat vermez. Bu yuzden bu dosya SIMDILIK
yalnizca agi uretiyor ve olcuyor; uc kapanisi ayri bir adim.
"""
import math
import os
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "..", "aero"))
from kanatagi import KanatAgi, naca_kodu                # noqa: E402
from planform import istasyonlar                        # noqa: E402


def gercek_istasyonlar(n=24):
    """planform.py'den (z, x_hucum, veter, t/c) dizisi.

    planform y'yi aciklik yonu sayar; ag z'yi aciklik yonu kullanir.
    """
    ist, yari, birlesme = istasyonlar(n=n)
    return [(y, x, c, tc) for (y, x, c, tc, _ok) in ist], yari


if __name__ == "__main__":
    ist, yari = gercek_istasyonlar(n=int(sys.argv[1]) if len(sys.argv) > 1 else 24)
    print("  istasyon: %d, yari aciklik %.4f" % (len(ist), yari))
    print("  kok: veter %.4f, t/c %.4f -> %s"
          % (ist[0][2], ist[0][3], naca_kodu(ist[0][3])))
    print("  uc : veter %.4f, t/c %.4f -> %s"
          % (ist[-1][2], ist[-1][3], naca_kodu(ist[-1][3])))
    print("  kesitler KESIRLI t/c ile uretiliyor (yuvarlama yok)")


    ag = KanatAgi(ist, Re=6e6, yplus=1.0, R=100.0, Xiz=100.0,
                  n_profil=256, n_normal=113, n_iz=64)
    yol = sys.argv[2] if len(sys.argv) > 2 else "/tmp/gercek/ag.msh"
    os.makedirs(os.path.dirname(yol), exist_ok=True)
    b = ag.yaz(yol)
    print()
    print("  ag: %d dugum, %d hucre (%dx%dx%d), %d duvar yuzu"
          % (b["dugum"], b["hucre"], b["NI"], b["NJ"], b["NK"], b["duvar"]))
