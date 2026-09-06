# -*- coding: utf-8 -*-
"""Yazilmis OpenFOAM alanlarinin en kucuk/en buyuk degerleri.

Neden gerekli: bu kurulumda forceCoeffs, yPlus ve postProcess kirik
(OSHA1stream / segfault). Alan istatistikleri de bu yuzden ELDEN
okunuyor. Duvara komsu hucreler ayrica raporlanir -- omega'nin patlamasi
once orada gorunur.

Kullanim: python3 alanistat.py <vaka> [alan1 alan2 ...]
"""
import os
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from foamoku import Alan, son_zaman                    # noqa: E402


def zamanlar(vaka):
    z = []
    for ad in os.listdir(vaka):
        try:
            float(ad)
        except ValueError:
            continue
        if os.path.isdir(os.path.join(vaka, ad)):
            z.append(ad)
    return sorted(z, key=float)


def duvar_hucreleri(vaka):
    """duvar yamasina komsu hucrelerin indisleri (owner listesinden)."""
    import re
    p = os.path.join(vaka, "constant", "polyMesh", "boundary")
    s = open(p).read()
    m = re.search(r"\n    duvar\n    \{(.*?)\n    \}", s, re.S)
    if not m:
        return None
    blok = m.group(1)
    nf = int(re.search(r"nFaces\s+(\d+);", blok).group(1))
    sf = int(re.search(r"startFace\s+(\d+);", blok).group(1))
    ow = os.path.join(vaka, "constant", "polyMesh", "owner")
    veri = open(ow).read()
    g = veri.index("(", veri.index("FoamFile"))
    son = veri.rindex(")")
    sayilar = veri[g + 1:son].split()
    return [int(sayilar[i]) for i in range(sf, sf + nf)]


def istat(vaka, alanlar=("k", "omega", "nut", "nuTilda", "p")):
    dv = duvar_hucreleri(vaka)
    cik = []
    for z in zamanlar(vaka):
        if z == "0":
            continue
        satir = {"zaman": z}
        for ad in alanlar:
            yol = os.path.join(vaka, z, ad)
            if not os.path.exists(yol):
                continue
            try:
                v = Alan(vaka, z, ad).ic
            except Exception as e:                       # noqa: BLE001
                satir[ad] = "okunamadi(%s)" % e
                continue
            satir[ad] = (min(v), max(v))
            if dv:
                dd = [v[i] for i in dv if i < len(v)]
                if dd:
                    satir[ad + "_duvar"] = (min(dd), max(dd))
        cik.append(satir)
    return cik


if __name__ == "__main__":
    vaka = sys.argv[1]
    alanlar = sys.argv[2:] or ["k", "omega", "nut", "nuTilda", "p"]
    for s in istat(vaka, alanlar):
        print("t = %s" % s["zaman"])
        for ad in alanlar:
            if ad in s:
                v = s[ad]
                d = s.get(ad + "_duvar")
                if isinstance(v, str):
                    print("   %-8s %s" % (ad, v))
                elif d:
                    print("   %-8s tum ag [%.4g, %.4g]   duvar hucreleri "
                          "[%.4g, %.4g]" % (ad, v[0], v[1], d[0], d[1]))
                else:
                    print("   %-8s [%.4g, %.4g]" % (ad, v[0], v[1]))
