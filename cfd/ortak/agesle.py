# -*- coding: utf-8 -*-
"""Bir agin alanini BASKA bir aga tasir (en yakin komsu).

NEDEN VAR. `mapFields` bu OpenFOAM kurulumunda kirik (segfault, ayni
OSHA1stream ailesinden). Ihtiyac su: k-omega SST'nin y+~1 cozumu
yalnizca SA cozumunden isinmis baslangicla elde edilebildi ve bu,
"SST cozumu SA'nin nut topografyasini miras almis olabilir mi" sorusunu
aciyor. Soruyu kapatmanin yolu, AYNI cozume MADDI OLARAK FARKLI bir
baslangictan varmak: y+~20 agindaki SST cozumunu y+=1 agina tasiyip
oradan koşmak.

Iki ag farkli (820 323 ve 2 263 560 hucre), o yuzden tasima gerekiyor.

YONTEM. En yakin komsu ataması (cKDTree). Bu bir ENTERPOLASYON DEGILDIR
ve oyle sunulmamalidir: hedef agdaki her hucre, kaynak agdaki merkezi
kendisine en yakin hucrenin degerini alir. Sicak baslangic icin yeterli,
cunku amac dogru cozum havzasina girmektir; nihai cozumu belirleyen sey
baslangic degil, yakinsamis denklemlerdir.

SINIR. Duvara cok yakin hucrelerde iki agin cozunurlugu 20 kat farkli
oldugu icin atama kaba kalir. Bu yuzden tasinan alan dogrudan
kullanilmaz; k ve omega, tasinan nut'tan isinmis.py'nin log-tabaka
bagintilariyla HEDEF agin kendi duvar mesafesiyle yeniden kurulur.
Boylece duvar yakini yapinin hedef aga ait olmasi saglanir.
"""
import os
import sys

import numpy as np

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
import isinmis as I                                    # noqa: E402


def esle(kaynak_vaka, kaynak_zaman, hedef_vaka, alanlar=("nut",)):
    """{alan_adi: hedef_agdaki_dizi} dondurur."""
    from scipy.spatial import cKDTree
    km, _ = I.ag_oku(kaynak_vaka)
    hm, _ = I.ag_oku(hedef_vaka)
    agac = cKDTree(km)
    _, idx = agac.query(hm, k=1)
    cik = {}
    for ad in alanlar:
        v = I.skaler_oku(kaynak_vaka, kaynak_zaman, ad)
        if v.size == 1:
            v = np.full(km.shape[0], v[0])
        cik[ad] = v[idx]
    return cik, hm


if __name__ == "__main__":
    kv, kz, hv = sys.argv[1], sys.argv[2], sys.argv[3]
    d, hm = esle(kv, kz, hv)
    for ad, v in d.items():
        print("%s: %d -> %d hucre, [%.4g, %.4g]"
              % (ad, I.skaler_oku(kv, kz, ad).size, v.size, v.min(), v.max()))
        np.save("/tmp/esle_%s.npy" % ad, v)
