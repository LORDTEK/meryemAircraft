# -*- coding: utf-8 -*-
"""Duvarda ters akis (ayrilma) var mi, nerede basliyor?

Gerekcesi: kalinlik calismasinda %25 kesiti sifir hucum acisinda C_L =
+0,048 verdi. Simetrik profil, sifir aci: C_L sifir OLMAK ZORUNDA. Ayni
kosuda Ux kalintisi dusmek yerine yukseldi ve C_L iki yazim arasinda
-0,0067'den +0,0481'e savruldu. Bunlarin hepsi tek bir seye isaret eder:
akis kararli degil, kararli cozucu bir yere oturamiyor.

Bu betik o teshisi FIZIKSEL olarak dogrular. Duvara komsu hucredeki
tegetsel hizin, yuzey boyunca hucum kenarindan firar kenarina bakan
yonle isaretini karsilastirir. Isaret negatifse orada akis geri
akiyordur -- ayrilma.

Ayrilmanin varligi tek basina kotu degildir; kararli RANS ilimli ve
DURAGAN bir ayrilmayi cozebilir. Kotu olan, ayrilmanin salinmasi ve
cozumun yakinsamamasidir. Bu yuzden cikti, ayrilma yerini kalinti
gecmisiyle BIRLIKTE okunmak icindir.
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from foamoku import Ag, Alan, son_zaman        # noqa: E402


def tara(vaka, yama="duvar", zaman=None):
    ag = Ag(vaka)
    z = zaman or son_zaman(vaka)
    U = Alan(vaka, z, "U", vektor=True)
    merkez = ag.hucre_merkez()
    y = ag.yama[yama]

    # yuz merkezleri ve komsu hucre hizlari
    kayit = []
    for k in range(y["n"]):
        fi = y["bas"] + k
        S, C = ag.yuz_alan(fi)
        A = math.sqrt(sum(v * v for v in S))
        if A <= 0:
            continue
        n = [S[a] / A for a in range(3)]
        u = U.ic[ag.sahip[fi]]
        un = sum(u[a] * n[a] for a in range(3))
        t = [u[a] - un * n[a] for a in range(3)]
        kayit.append((C, t))

    # Olcut: tegetsel hizin SERBEST AKIS yonundeki bileseni.
    #
    # Ilk bicim teget yonunu komsu yuz merkezlerinden aliyordu; YANLISTI.
    # C-agindaki i indeksi alt yuzeyde firardan hucuma dogru ilerler, yani
    # o yon akisin tersidir ve alt yuzeyin TAMAMI "ters akiyor" cikiyordu.
    # Belirti acikti: NACA 0012 icin %50 ayrilma, hepsi alt yuzeyde.
    #
    # Serbest akis yonu her iki yuzeyde ayni oldugu icin olcut simetriktir
    # ve bu, aranan seyin ta kendisidir: simetrik profilde ust ve alt
    # yuzeydeki ayrilma esit olmali.
    ters = []
    for C, t in kayit:
        ters.append((C[0], C[1], t[0] * math.cos(0.0) + t[1] * math.sin(0.0)))
    return ters


def ozet(vaka, zaman=None):
    t = tara(vaka, zaman=zaman)
    # Hucum kenarinin hemen onunde akis durma noktasi cevresinde gercekten
    # one doner; bu ayrilma degildir. Ilk %1 veter disarida birakilir.
    t = [v for v in t if v[0] > 0.01]
    n = len(t)
    geri = [v for v in t if v[2] < 0]
    print("  %s  (t = %s)" % (os.path.basename(vaka), zaman or son_zaman(vaka)))
    print("    duvar yuzu           %d" % n)
    print("    ters akan yuz        %d  (%%%.1f)" % (len(geri), 100.0 * len(geri) / n))
    if geri:
        ust = [v for v in geri if v[1] > 0]
        alt = [v for v in geri if v[1] < 0]
        print("      ust yuzeyde %d,  alt yuzeyde %d   <- SIMETRIK OLMALI"
              % (len(ust), len(alt)))
        for ad, dizi in (("ust", ust), ("alt", alt)):
            if dizi:
                print("      %s: x = %.3f .. %.3f" % (ad, min(v[0] for v in dizi),
                                                      max(v[0] for v in dizi)))
    return len(geri) / n


if __name__ == "__main__":
    for v in sys.argv[1:]:
        ozet(v)
