# -*- coding: utf-8 -*-
"""Kucuk bir OpenFOAM ASCII okuyucu: polyMesh ve alan dosyalari.

Neden var: bu makinedeki OpenFOAM 1912 paketinde HICBIR fonksiyon nesnesi
calismiyor -- forceCoeffs, forces, yPlus, hatta writeObjects, hepsi
OSHA1stream uzerinde "error in IOstream sha1" verip cikiyor. Kusur vakada
degil kurulumda: stok bir vakada da ayni sonuc aliniyor. Daha yeni bir
OpenFOAM kurmak da mumkun degil, dl.openfoam.com/org kapali.

Bu yuzden kuvvetler ve y+ cozumden SONRA, yazilmis alanlardan hesaplaniyor
(kuvvet.py). Ara adim olarak agi ve alanlari okumak gerekiyor; yaptigi is
bu.

Kapsam bilerek dar: yalnizca ASCII, sikistirilmamis, tek bolgeli ag ve
volScalarField / volVectorField. Genel bir okuyucu degildir.
"""
import os, re


def _govde(yol):
    """FoamFile basligini atlar, geri kalan metni doner."""
    with open(yol) as fh:
        m = fh.read()
    i = m.find("FoamFile")
    if i >= 0:
        d = m.index("{", i)
        derinlik, k = 0, d
        while k < len(m):
            if m[k] == "{":
                derinlik += 1
            elif m[k] == "}":
                derinlik -= 1
                if derinlik == 0:
                    break
            k += 1
        m = m[k + 1:]
    return re.sub(r"/\*.*?\*/|//[^\n]*", "", m, flags=re.S)


_SAYI = re.compile(r"[-+0-9.eE]+")


def _liste(metin, bas=0):
    """'N ( ... )' bicimindeki listeyi ayristirir; (deger_listesi, bitis)."""
    m = re.compile(r"(\d+)\s*\(").search(metin, bas)
    if not m:
        return None, bas
    n, i = int(m.group(1)), m.end()
    derinlik, j = 1, i
    while j < len(metin) and derinlik:
        if metin[j] == "(":
            derinlik += 1
        elif metin[j] == ")":
            derinlik -= 1
        j += 1
    return metin[i:j - 1], j, n


class Ag:
    """polyMesh: noktalar, yuzler, sahip/komsu, sinir yamalari."""

    def __init__(self, vaka):
        d = os.path.join(vaka, "constant", "polyMesh")
        for a in ("points", "faces", "owner", "neighbour", "boundary"):
            if not os.path.exists(os.path.join(d, a)):
                raise RuntimeError("polyMesh eksik: " + a)

        g, _, _ = _liste(_govde(os.path.join(d, "points")))
        self.nokta = [tuple(float(v) for v in _SAYI.findall(s))
                      for s in re.findall(r"\(([^()]*)\)", g)]

        g, _, _ = _liste(_govde(os.path.join(d, "faces")))
        self.yuz = [[int(v) for v in s.split()]
                    for s in re.findall(r"\(([^()]*)\)", g)]

        g, _, _ = _liste(_govde(os.path.join(d, "owner")))
        self.sahip = [int(v) for v in g.split()]
        g, _, _ = _liste(_govde(os.path.join(d, "neighbour")))
        self.komsu = [int(v) for v in g.split()]

        self.yama = {}
        b = _govde(os.path.join(d, "boundary"))
        g, _, _ = _liste(b)
        for ad, govde in re.findall(r"(\w+)\s*\{([^}]*)\}", g):
            nf = re.search(r"nFaces\s+(\d+)", govde)
            sf = re.search(r"startFace\s+(\d+)", govde)
            tp = re.search(r"type\s+(\w+)", govde)
            if nf and sf:
                self.yama[ad] = dict(bas=int(sf.group(1)), n=int(nf.group(1)),
                                     tur=tp.group(1) if tp else "patch")
        self.n_hucre = max(self.sahip) + 1
        self._yuz_ob = {}          # yuz alan/merkez onbellegi
        self._merkez = None        # hucre merkezleri onbellegi
        self._hucre_yuz = None     # hucre -> yuzler haritasi

    def hucre_yuzleri(self):
        """Her hucrenin yuz listesi. Duvardan ikinci hucreye yurumek icin
        gerekiyor (ikinci mertebeden duvar gradyani)."""
        if self._hucre_yuz is not None:
            return self._hucre_yuz
        h = [[] for _ in range(self.n_hucre)]
        for fi, c in enumerate(self.sahip):
            h[c].append(fi)
        for fi, c in enumerate(self.komsu):
            h[c].append(fi)
        self._hucre_yuz = h
        return h

    def karsi_hucre(self, fi, h):
        """h hucresinde, fi yuzunun KARSISINDAKI ic yuzun obur hucresi.

        Yapisal bir hucrede karsi yuz, normali fi'nin normaline en yakin
        olarak TERS olan yuzdur. Yapisal olmayan agda bu tanim gevser; bu
        yuzden yalnizca duvara komsu tabakada, ki orada ag yapisaldir.
        """
        S0, _ = self.yuz_alan(fi)
        A0 = (S0[0]**2 + S0[1]**2 + S0[2]**2) ** 0.5
        if A0 <= 0:
            return None
        n0 = [S0[a] / A0 for a in range(3)]
        en_iyi, en_hucre = 0.0, None
        for g in self.hucre_yuzleri()[h]:
            if g == fi or g >= len(self.komsu):
                continue                      # sinir yuzu ya da kendisi
            S, _ = self.yuz_alan(g)
            A = (S[0]**2 + S[1]**2 + S[2]**2) ** 0.5
            if A <= 0:
                continue
            # g yuzunun DISA bakan normali, h acisindan
            isaret = 1.0 if self.sahip[g] == h else -1.0
            nk = sum(isaret * S[a] / A * n0[a] for a in range(3))
            if -nk > en_iyi:
                en_iyi = -nk
                en_hucre = self.komsu[g] if self.sahip[g] == h else self.sahip[g]
        return en_hucre if en_iyi > 0.7 else None

    def yuz_alan(self, fi):
        """Yuzun alan vektoru ve merkezi. Ucgen yelpazesiyle; duzlemsel
        olmayan yuzlerde de dogru sonuc verir.

        Sonuc onbellege alinir: hem kuvvet hesabi hem hucre merkezleri ayni
        yuzleri defalarca ister. Iki boyutta onemsiz, uc boyutlu vakada
        belirleyici olur.
        """
        h = self._yuz_ob.get(fi)
        if h is not None:
            return h
        p = [self.nokta[k] for k in self.yuz[fi]]
        n = len(p)
        ox = sum(q[0] for q in p) / n
        oy = sum(q[1] for q in p) / n
        oz = sum(q[2] for q in p) / n
        Sx = Sy = Sz = 0.0
        Cx = Cy = Cz = 0.0
        A = 0.0
        for i in range(n):
            a, b = p[i], p[(i + 1) % n]
            ux, uy, uz = a[0] - ox, a[1] - oy, a[2] - oz
            vx, vy, vz = b[0] - ox, b[1] - oy, b[2] - oz
            sx = 0.5 * (uy * vz - uz * vy)
            sy = 0.5 * (uz * vx - ux * vz)
            sz = 0.5 * (ux * vy - uy * vx)
            m = (sx * sx + sy * sy + sz * sz) ** 0.5
            Sx += sx; Sy += sy; Sz += sz
            cx = (ox + a[0] + b[0]) / 3
            cy = (oy + a[1] + b[1]) / 3
            cz = (oz + a[2] + b[2]) / 3
            Cx += m * cx; Cy += m * cy; Cz += m * cz
            A += m
        if A > 0:
            Cx, Cy, Cz = Cx / A, Cy / A, Cz / A
        else:
            Cx, Cy, Cz = ox, oy, oz
        h = ((Sx, Sy, Sz), (Cx, Cy, Cz))
        self._yuz_ob[fi] = h
        return h

    def hucre_merkez(self):
        """Hucre merkezleri: yuz merkezlerinin alanla agirlikli ortalamasi.

        Dikdortgen hucrede bu TAM sonucu verir (duvardan uzaklik h/2);
        bizim duvara komsu hucrelerimiz dik ve dikdortgene cok yakin
        oldugu icin yaklasim orada keskindir. Bir kez hesaplanip
        onbellege alinir.
        """
        if self._merkez is not None:
            return self._merkez
        top = [[0.0, 0.0, 0.0, 0.0] for _ in range(self.n_hucre)]
        for fi in range(len(self.yuz)):
            S, C = self.yuz_alan(fi)
            m = (S[0] ** 2 + S[1] ** 2 + S[2] ** 2) ** 0.5
            for h in (self.sahip[fi],
                      self.komsu[fi] if fi < len(self.komsu) else -1):
                if h < 0:
                    continue
                t = top[h]
                t[0] += m * C[0]; t[1] += m * C[1]; t[2] += m * C[2]; t[3] += m
        self._merkez = [(t[0] / t[3], t[1] / t[3], t[2] / t[3]) if t[3]
                        else (0.0, 0.0, 0.0) for t in top]
        return self._merkez


def son_zaman(vaka):
    """En buyuk sayisal zaman dizini (0 haric)."""
    z = []
    for a in os.listdir(vaka):
        try:
            v = float(a)
        except ValueError:
            continue
        if os.path.isdir(os.path.join(vaka, a)) and v > 0:
            z.append((v, a))
    if not z:
        raise RuntimeError("yazilmis zaman dizini yok: " + vaka)
    return max(z)[1]


class Alan:
    """Bir volScalarField / volVectorField: ic degerler + yama degerleri."""

    def __init__(self, vaka, zaman, ad, vektor=False):
        self.vektor = vektor
        m = _govde(os.path.join(vaka, zaman, ad))
        i = m.index("internalField")
        j = m.index("boundaryField")
        self.ic = self._coz(m[i:j])
        self.yama = {}
        g, _, _ = _liste(m[j:], 0) if False else (m[j:], 0, 0)
        for ym, govde in re.findall(r"(\w+)\s*\n?\s*\{((?:[^{}]|\{[^{}]*\})*)\}",
                                    m[j:]):
            self.yama[ym] = self._coz(govde)

    def _coz(self, metin):
        """uniform tek deger ya da nonuniform liste."""
        if "nonuniform" in metin:
            g, _, _ = _liste(metin)
            if self.vektor:
                return [tuple(float(v) for v in s.split())
                        for s in re.findall(r"\(([^()]*)\)", g)]
            return [float(v) for v in g.split()]
        m = re.search(r"uniform\s+(\([^)]*\)|[-+0-9.eE]+)", metin)
        if not m:
            return None
        t = m.group(1)
        if t.startswith("("):
            return ("U", tuple(float(v) for v in t[1:-1].split()))
        return ("U", float(t))

    def yama_degeri(self, ym, k, varsayilan=None):
        v = self.yama.get(ym)
        if v is None:
            return varsayilan
        if isinstance(v, tuple) and v and v[0] == "U":
            return v[1]
        return v[k]
