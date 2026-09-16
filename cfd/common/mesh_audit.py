# -*- coding: utf-8 -*-
"""Hucre hacmini OpenFOAM'IN HESAPLADIGI GIBI hesaplar.

NEDEN AYRI BIR DOSYA. Uretec tarafinda hucrelerin ters donup donmedigini
denetlemek icin once bes-dortyuzlu (5-tet) ayristirma kullanilmisti. O
denetim YANILTICI: kaba bir ag icin "0 negatif hucre" dedi, ayni ag
checkMesh'te 497 negatif hucre ve 1681 yanlis yonlu yuz verdi.

Fark, altigen yuzlerin DUZLEMSEL OLMAMASINDAN geliyor. 5-tet ayristirma
her yuzu bir kosegenden ikiye boler; OpenFOAM ise her yuzu KENDI
MERKEZINE gore ucgen yelpazesine acar ve hacmi o yuzlerden piramitlerle
toplar. Yuz cok carpiksa iki olcu ayri isaret verebilir -- ve ag gecerli
sayilan yerde aslinda bozuktur.

Burada OpenFOAM'in primitiveMesh::makeCellCentresAndVols yordami birebir
izleniyor:

  1. Her yuzun merkezi ve alan vektoru, yuzun nokta ortalamasi etrafinda
     ucgen yelpazesiyle, ucgen alanlariyla AGIRLIKLANDIRILARAK bulunur.
  2. Hucre merkezi once yuz merkezlerinin ortalamasiyla kestirilir.
  3. Hacim, her yuzden o kestirime kurulan piramitlerin toplamidir.

Boylece denetim, checkMesh ne diyorsa onu der.
"""


def yuz_merkez_alan(P):
    """Cokgenin (x,y,z) noktalarindan merkezini ve alan vektorunu dondurur."""
    n = len(P)
    if n == 3:
        c = tuple(sum(q[i] for q in P) / 3.0 for i in range(3))
        u = [P[1][i] - P[0][i] for i in range(3)]
        v = [P[2][i] - P[0][i] for i in range(3)]
        s = (u[1] * v[2] - u[2] * v[1],
             u[2] * v[0] - u[0] * v[2],
             u[0] * v[1] - u[1] * v[0])
        return c, tuple(0.5 * x for x in s)

    # nokta ortalamasi -- yelpazenin tepesi
    pAvg = [sum(q[i] for q in P) / float(n) for i in range(3)]
    sumA = 0.0
    sumAc = [0.0, 0.0, 0.0]
    sumN = [0.0, 0.0, 0.0]
    for i in range(n):
        a = P[i]
        b = P[(i + 1) % n]
        c3 = [(a[k] + b[k] + pAvg[k]) / 3.0 for k in range(3)]
        u = [b[k] - a[k] for k in range(3)]
        v = [pAvg[k] - a[k] for k in range(3)]
        nrm = (u[1] * v[2] - u[2] * v[1],
               u[2] * v[0] - u[0] * v[2],
               u[0] * v[1] - u[1] * v[0])
        a3 = (nrm[0] ** 2 + nrm[1] ** 2 + nrm[2] ** 2) ** 0.5
        sumA += a3
        for k in range(3):
            sumAc[k] += a3 * c3[k]
            sumN[k] += nrm[k]
    if sumA < 1e-300:                      # cokmus yuz
        return tuple(pAvg), (0.0, 0.0, 0.0)
    return (tuple(sumAc[k] / sumA for k in range(3)),
            tuple(0.5 * sumN[k] for k in range(3)))


# Altigenin alti yuzu, gmsh/OpenFOAM dugum sirasina gore (a b c d taban,
# e f g h ust). Yuzler DISARI bakacak sekilde sarilidir.
HEX_YUZ = ((0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4),
           (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7))


def hucre_hacmi(dugumler):
    """dugumler: altigenin 8 kosesi (a..h). OpenFOAM'in hacmini dondurur."""
    merkezler = []
    alanlar = []
    for yz in HEX_YUZ:
        c, s = yuz_merkez_alan([dugumler[i] for i in yz])
        merkezler.append(c)
        alanlar.append(s)
    cEst = [sum(c[i] for c in merkezler) / 6.0 for i in range(3)]
    V = 0.0
    for c, s in zip(merkezler, alanlar):
        V += sum(s[i] * (c[i] - cEst[i]) for i in range(3))
    return V / 3.0
