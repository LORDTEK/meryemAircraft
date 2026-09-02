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


def gercek_istasyonlar(n=24, sikistir=False):
    """planform.py'den (z, x_hucum, veter, t/c) dizisi.

    planform y'yi aciklik yonu sayar; ag z'yi aciklik yonu kullanir.

    sikistir=True ise istasyonlar UCA DOGRU SIKLASTIRILIR. Neden: veter
    kokte 0,97, ucta 0,236. Aciklik adimi sabit tutulursa Dz/c orani
    0,15'ten 0,61'e cikar ve son iki istasyon arasinda veter %26 degisir --
    ag orada tasiyamaz.

    Olculdu (checkMesh, y+=60, dy sabit): tekduze istasyonla kalan butun
    kusurlar aciklığın DIS %25'inde toplaniyordu; z araligi [1,22 - 1,65],
    yari aciklik 1,73. Sikistirma bunu hedefler.

    Yontem: istasyonlar, Dz/c orani sabit kalacak sekilde yerlestirilir --
    yani s(z) = INTEGRAL dz/c(z) degiskeninde esit araliklarla.

    SONUC: ISE YARAMADI. Dz/c gercekten sabitlendi (0,272-0,280; oncesi
    0,071-0,492) ama checkMesh kotulesti: negatif hucre 29 -> 211 (n=12),
    53 (n=20). Sebebi muhtemelen sudur: Dz/c'yi sabitlemek KOK tarafinda
    Dz'yi buyutuyor (0,142 -> 0,264) ve kusuru oraya tasiyor. Varsayilan
    False; secenek olculmus bir kayit olarak duruyor.
    """
    ince, yari, birlesme = istasyonlar(n=max(400, 20 * n))
    if not sikistir:
        # TEKDUZE aralikli istasyonlar, ARA DEGERLEME ile.
        #
        # Onceki surum ince listeyi dilimliyor (ince[::adim]) ve son
        # istasyonu ayrica ekliyordu. Bolme tam gelmediginde bu, en sonda
        # KIYMIK bir aralik biraktiriyordu: olculdu, son adim 0,0173 iken
        # otekiler 0,142 -- sekiz kat ince, ve tam UCTA. Kusurlarin hepsinin
        # uc bolgesinde toplanmasi buna baglı olabilir.
        y = [q[0] for q in ince]
        cik = []
        for i in range(n + 1):
            h = y[-1] * i / n
            j = min(range(len(y) - 1), key=lambda k: abs(y[k] - h)) \
                if False else 0
            # ikili arama yerine dogrusal tarama yeterli (ince ~400 nokta)
            j = 0
            while j < len(y) - 2 and y[j + 1] < h:
                j += 1
            t = 0.0 if y[j + 1] == y[j] else (h - y[j]) / (y[j + 1] - y[j])
            cik.append(tuple(ince[j][m] + t * (ince[j + 1][m] - ince[j][m])
                             for m in range(4)))
        cik[0] = tuple(ince[0][:4])
        cik[-1] = tuple(ince[-1][:4])
        return cik, yari

    # s(z) = toplam dz/c
    y = [q[0] for q in ince]
    c = [q[2] for q in ince]
    s = [0.0]
    for k in range(1, len(y)):
        s.append(s[-1] + (y[k] - y[k - 1]) * 2.0 / (c[k] + c[k - 1]))
    hedef = [s[-1] * i / n for i in range(n + 1)]
    cik, j = [], 0
    for h in hedef:
        while j < len(s) - 2 and s[j + 1] < h:
            j += 1
        t = 0.0 if s[j + 1] == s[j] else (h - s[j]) / (s[j + 1] - s[j])
        q = [ince[j][m] + t * (ince[j + 1][m] - ince[j][m]) for m in range(4)]
        cik.append(tuple(q))
    cik[0] = tuple(ince[0][:4])
    cik[-1] = tuple(ince[-1][:4])
    return cik, yari


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
