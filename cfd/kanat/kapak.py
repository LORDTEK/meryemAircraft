# -*- coding: utf-8 -*-
"""Uc kapagini dolduran IC AG -- coken kenar BIRAKMADAN.

SORUN. Kesiti dolduran duz bir H-agi, hucum kenarinda cokerdi: orada
kesit kalinligi sifira gittigi icin butun kalinlik cizgileri tek noktada
bulusur. Olculdu: kapagin duzlem ici en-boy orani her yerde <= 8, ama o
tek coken kenar yuzunden agin azami en-boy orani 1,33e9 cikiyordu
(192 prizma hucre).

COZUM: halka + kelebek cekirdek (O-H).
  - HALKA: sinirdan iceri NR katman. Sinirin sivri hucum kenarini bu
    katmanlar sogurur; hucreler ince ama duzgun (annulus'un duvar
    yakinindaki hucreleri gibi).
  - CEKIRDEK: halkanin ic ilmeginde tek bir Coons yamasi. Ic ilmek,
    sinirin YUMUSATILMIS hali oldugu icin kut; dort kosesi esit yay
    uzunlugunda secildiginden karsilikli kenarlar ayni nokta sayisina
    sahip ve hicbir yerde cokme YOK.

Ic ilmek, sinir ilmeginin Laplace yumusatmasiyla elde edilir: yumusatma
kose yuvarlar ve ilmegi agirlik merkezine dogru buzer -- tam gereken sey.
"""
import math


def _yumusat(P, gecis):
    """Kapali ilmekte Laplace yumusatmasi (kosleri yuvarlar, buzer)."""
    n = len(P)
    Q = list(P)
    for _ in range(gecis):
        Q = [((Q[i - 1][0] + 2 * Q[i][0] + Q[(i + 1) % n][0]) / 4.0,
              (Q[i - 1][1] + 2 * Q[i][1] + Q[(i + 1) % n][1]) / 4.0)
             for i in range(n)]
    return Q


def ic_ilmek(sinir, gecis=400, buzme=0.55):
    """Halkanin ic ilmegi: yumusatilmis ve agirlik merkezine dogru buzulmus."""
    S = _yumusat(sinir, gecis)
    cx = sum(q[0] for q in S) / len(S)
    cy = sum(q[1] for q in S) / len(S)
    return [(cx + buzme * (q[0] - cx), cy + buzme * (q[1] - cy)) for q in S]


def _coons(alt, sag, ust, sol):
    """Dort kenardan Coons yamasi. alt/ust n1+1, sag/sol n2+1 nokta.

    alt: (0,0)->(1,0)   sag: (1,0)->(1,1)   ust: (0,1)->(1,1)   sol: (0,0)->(0,1)
    """
    n1, n2 = len(alt) - 1, len(sag) - 1
    G = [[None] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(n1 + 1):
        u = i / float(n1)
        for j in range(n2 + 1):
            v = j / float(n2)
            p = []
            for c in range(2):
                a = (1 - v) * alt[i][c] + v * ust[i][c]
                b = (1 - u) * sol[j][c] + u * sag[j][c]
                d = ((1 - u) * (1 - v) * alt[0][c] + u * (1 - v) * alt[n1][c]
                     + (1 - u) * v * ust[0][c] + u * v * ust[n1][c])
                p.append(a + b - d)
            G[i][j] = tuple(p)
    return G


def kapak_agi(sinir, n_halka=6, gecis=400, buzme=0.55):
    """sinir: kesit sinirinin KAPALI ilmegi (NP nokta, son != ilk).

    Doner: (dugum_izgarasi, hucreler) -- hucreler dortgen kose dizisi
    olarak, hepsi (a,b,c,d) ve HICBIRI cokmus degil.

    NP dorde bolunebilmelidir; kelebek cekirdegin karsilikli kenarlari
    esit nokta sayisi ister.
    """
    NP = len(sinir)
    if NP % 4:
        raise ValueError("sinir ilmegi 4'e bolunebilmeli, NP=%d" % NP)
    ic = ic_ilmek(sinir, gecis, buzme)

    # --- halka katmanlari: sinirdan ic ilmege
    kat = []
    for r in range(n_halka + 1):
        f = r / float(n_halka)
        kat.append([(sinir[p][0] + f * (ic[p][0] - sinir[p][0]),
                     sinir[p][1] + f * (ic[p][1] - sinir[p][1]))
                    for p in range(NP)])

    # --- cekirdek: ic ilmegin dortte birlerinden Coons yamasi
    q = NP // 4
    L = kat[-1]
    alt = [L[(0 + i) % NP] for i in range(q + 1)]
    sag = [L[(q + i) % NP] for i in range(q + 1)]
    ust = [L[(3 * q - i) % NP] for i in range(q + 1)]      # ters yon
    sol = [L[(4 * q - i) % NP] for i in range(q + 1)]      # ters yon
    G = _coons(alt, sag, ust, sol)

    return kat, G, q
