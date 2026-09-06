# -*- coding: utf-8 -*-
"""SA cozumunden k-omega SST icin ISINMIS BASLANGIC alani uretir.

NEDEN. k-omega SST'yi y+~1 agida TEK BICIMLI alandan baslatmak yerel bir
k adasi uretiyor: olculdu, 61. adimda k_max = 10 391, 2000 adimda uc
mertebe soniyor ama fiziksel degere (k/U^2 ~ 0,005) inemiyor, 7,3'te
takilip 2150 civarinda patliyor (bkz. dogrulama.md). Ayni agda SA
sorunsuz kosuyor. Bu betik SA'nin yakinsamis nut alanindan SST icin
tutarli bir (k, omega) cifti turetir.

YONTEM. Logaritmik tabaka dengesinden (nut = kappa u_tau y,
k = u_tau^2/sqrt(beta*)):

    omega_turb = nut / (sqrt(beta*) * kappa^2 * y^2)
    k          = nut * omega_turb = nut^2 / (sqrt(beta*) kappa^2 y^2)

Bu, S (gerinim hizi) hesaplamayi gerektirmez -- yalnizca nut ve duvar
mesafesi yeter. Denetim: nut = kappa u_tau y konunca k = u_tau^2/sqrt(b*)
cikiyor, yani dogru log-tabaka degeri.

Viskoz alt tabakada log-tabaka bagintisi gecersizdir; orada Menter'in
viskoz omega'si alinir:

    omega_visc = 6 nu / (beta1 y^2),   beta1 = 0,075

ve omega = max(omega_turb, omega_visc, omega_sonsuz).

Serbest akimda nut kucuk ve y buyuk oldugu icin k ve omega tabanlariyla
sinirlanir.

DIKKAT. Bu bir FIZIKSEL donusum degil, sayisal bir sicak baslangictir.
SA cozumu SST cozumune cevrilmis olmaz; yalnizca SST'nin kotu gecici
rejimi atlanir.
"""
import io
import os
import re

import numpy as np

BETA_YILDIZ = 0.09
BETA1 = 0.075
KAPPA = 0.41


def _govde(yol):
    return io.open(yol, encoding="utf-8", errors="replace").read()


def skaler_oku(vaka, zaman, ad):
    """internalField'i numpy dizisi olarak dondurur (tek biciml ise yayar)."""
    s = _govde(os.path.join(vaka, zaman, ad))
    i, j = s.index("internalField"), s.index("boundaryField")
    blok = s[i:j]
    m = re.search(r"nonuniform List<scalar>\s*\n(\d+)\s*\n\(", blok)
    if m:
        g = blok.index("(", m.end() - 1) + 1
        return np.fromstring(blok[g:blok.index(")", g)], sep="\n")
    m = re.search(r"uniform\s+([-\d.eE+]+)", blok)
    return np.full(1, float(m.group(1)))


def ag_oku(vaka):
    """(hucre_merkez, duvar_yuz_merkez). Merkezler YAKLASIKTIR (yuz
    noktalarinin ortalamasi, hucre yuzlerinin ortalamasi) -- duvar
    mesafesi ve sicak baslangic icin yeterli, kuvvet hesabi icin degil."""
    yol = os.path.join(vaka, "constant", "polyMesh")

    def liste(ad):
        s = _govde(os.path.join(yol, ad))
        m = re.search(r"\n(\d+)\s*\n\(", s)
        g = m.end() - 1
        return s, int(m.group(1)), g

    s, npt, g = liste("points")
    son = s.rindex(")")
    ham = s[g + 1:son].replace("(", " ").replace(")", " ")
    P = np.fromstring(ham, sep=" ").reshape(-1, 3)

    s, nf, g = liste("faces")
    son = s.rindex(")")
    # "n(i1 i2 ... in)" bicimi
    parcalar = re.findall(r"(\d+)\(([^)]*)\)", s[g:son])
    yuz_merkez = np.empty((len(parcalar), 3))
    for i, (n, ic) in enumerate(parcalar):
        idx = np.fromstring(ic, sep=" ", dtype=float).astype(np.int64)
        yuz_merkez[i] = P[idx].mean(axis=0)

    s, no, g = liste("owner")
    son = s.rindex(")")
    ow = np.fromstring(s[g + 1:son], sep="\n", dtype=float).astype(np.int64)
    s, nn, g = liste("neighbour")
    son = s.rindex(")")
    nb = np.fromstring(s[g + 1:son], sep="\n", dtype=float).astype(np.int64)

    nh = int(max(ow.max(), nb.max())) + 1
    top = np.zeros((nh, 3))
    say = np.zeros(nh)
    for a in range(3):
        top[:, a] = np.bincount(ow, weights=yuz_merkez[:len(ow), a], minlength=nh)
        top[:, a] += np.bincount(nb, weights=yuz_merkez[:len(nb), a], minlength=nh)
    say = (np.bincount(ow, minlength=nh) + np.bincount(nb, minlength=nh))
    merkez = top / say[:, None]

    s = _govde(os.path.join(yol, "boundary"))
    m = re.search(r"\n    duvar\n    \{(.*?)\n    \}", s, re.S)
    nfd = int(re.search(r"nFaces\s+(\d+);", m.group(1)).group(1))
    sfd = int(re.search(r"startFace\s+(\d+);", m.group(1)).group(1))
    return merkez, yuz_merkez[sfd:sfd + nfd]


def duvar_mesafesi(merkez, duvar_yuz):
    from scipy.spatial import cKDTree
    return cKDTree(duvar_yuz).query(merkez, k=1)[0]


def uret(sa_vaka, sa_zaman, nu, k_sonsuz, omega_sonsuz):
    merkez, duvar = ag_oku(sa_vaka)
    y = duvar_mesafesi(merkez, duvar)
    y = np.maximum(y, 1e-12)
    nut = skaler_oku(sa_vaka, sa_zaman, "nut")
    if nut.size == 1:
        nut = np.full(merkez.shape[0], nut[0])
    c = np.sqrt(BETA_YILDIZ) * KAPPA ** 2
    om_turb = nut / (c * y ** 2)
    om_visc = 6.0 * nu / (BETA1 * y ** 2)
    omega = np.maximum(np.maximum(om_turb, om_visc), omega_sonsuz)
    k = np.maximum(nut * om_turb, k_sonsuz)
    return k, omega, y, nut


def yaz(kaynak_dosya, hedef_dosya, deger):
    """kaynak_dosya'nin basligini ve boundaryField'ini koruyup
    internalField'i deger dizisiyle degistirir."""
    s = _govde(kaynak_dosya)
    i, j = s.index("internalField"), s.index("boundaryField")
    yeni = ("internalField   nonuniform List<scalar>\n%d\n(\n%s\n)\n;\n\n"
            % (deger.size, "\n".join("%.10g" % v for v in deger)))
    io.open(hedef_dosya, "w", encoding="utf-8").write(s[:i] + yeni + s[j:])
