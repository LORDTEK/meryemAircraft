# -*- coding: utf-8 -*-
"""%25 kesitinde kararli cozucunun basarisizligi LINEER COZUCU kaynakli mi?

DURUM. Kararli (SIMPLE) cozucu %25 kesitinde yakinsamiyor: C_L simetrik
profilde 4000 adimda +2,6e-2, 16000 adimda -2,7e-2 (isaret degistiriyor),
hiz kalintilari dusmek yerine yukseliyor. Bunu "akis kararsiz" diye
yorumlamistim.

URANS BUNU CURUTTU. Zamana bagli cozumde:
    C_L ustel olarak sifira sonumleniyor, lambda = -36,4 1/s
        (negatif -> simetrik durum KARARLI)
    C_D ustel gevsemeyle ~0,01357'ye gidiyor, zaman sabiti ~0,138 s
Yani akis kararli ve simetrik. Kararli cozucunun savrulmasi FIZIKSEL
degil, SAYISAL.

HIPOTEZ (once yaziliyor). Ayni agda PIMPLE kosusunda olculdu ki GAMG
basinc denkleminde tikaniyor: azami en-boy orani 5000, azami
dik-olmayanlik 61 derece. pFinal 1000 yinelemeye carpip pes ediyordu ve
PCG+DIC'e gecince 6,9 kat hizlandi, cozum degismedi. Kararli kosularda
da basinc GAMG ile ve relTol 0,01 ile cozuluyor. Eger GAMG bu agda her
yinelemede basinci yeterince cozemiyorsa, SIMPLE her adimda kucuk ama
tutarsiz bir basinc alaniyla ilerler; simetriyi bozan ve buyuyen sey bu
olabilir.

BEKLENTI ONCEDEN:
  (a) PCG+DIC ile C_L sifira gider ve kalintilar duserse, kararli
      cozucunun basarisizligi LINEER COZUCU kaynakliydi. O zaman %25
      satiri kararli cozumle alinabilir ve pahali URANS'a gerek kalmaz.
      Elde edilen C_D, URANS'in gittigi degere (~0,01357) yakin
      olmalidir -- bu, iki bagimsiz yoldan ayni cevaba varmak demektir.
  (b) Yine savrulursa hipotez YANLIS; basarisizlik baska yerdedir
      (gevsetme carpanlari, ya da denklemlerin kendi katiligi) ve URANS
      tek yol olarak kalir.

Bu betik AYNI vakayi iki lineer cozucuyle kosar. Baska hicbir sey
degismez.
"""
import json, os, re, subprocess, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kur import kur                                    # noqa: E402
from kuvvet import hesapla                             # noqa: E402
from kilit import Kilit                                # noqa: E402

KOK = "/tmp/kararli_cozucu"
# ADIM ve varyantlar -- ortam kisiti yuzunden daraltildi.
#
# Bu ortamda konteyner, oturum bosa dustugunde yeniden basliyor ve kosan
# her sey oluyor (bu oturumda UC kez oldu). Yani hesap, tek bir etkin
# adimin icinde bitmeli. 36864 hucrede yineleme maliyeti 0,1345 s
# olculdu, yani 3000 yineleme ~400 s: bir adima sigar.
#
# GAMG varyanti YENIDEN KOSULMUYOR cunku ayni vaka kalinlik
# calismasinda zaten GAMG ile kosuldu ve degerleri kayitli (asagida).
ADIM = 3000
# Ayni vakanin GAMG ile verdigi degerler (olculdu)
GAMG_4000 = dict(CD=0.013920, CL=+2.6e-2)
URANS_GIDIS = 0.01357          # URANS'in gevsedigi deger (ustel disdegerleme)


def kalintilar(vaka):
    p = os.path.join(vaka, "log.simpleFoam")
    if not os.path.exists(p):
        return {}
    m = open(p).read()
    out = {}
    for ad in ("Ux", "Uy", "p", "nuTilda"):
        v = [float(x) for x in re.findall(
            r"Solving for %s, Initial residual = ([0-9.e+-]+)" % ad, m)]
        if v:
            n = len(v)
            out[ad] = dict(son=v[-1], oran=v[-1] / v[int(n * 0.9)])
    return out


VARYANT = [("pcg_dic", ("        solver          GAMG;\n"
                        "        smoother        GaussSeidel;\n",
                        "        solver          PCG;\n"
                        "        preconditioner  DIC;\n"))]

if __name__ == "__main__":
    with Kilit(KOK):
        os.makedirs(KOK, exist_ok=True)
        yol = os.path.join(KOK, "sonuc.json")
        cikti = json.load(open(yol)) if os.path.exists(yol) else []
        yapilan = {d["ad"] for d in cikti}
        for ad, degis in VARYANT:
            if ad in yapilan:
                continue
            vaka = os.path.join(KOK, ad)
            kur(vaka, kod="0025", Re=2e6, alfa=0.0, yplus=1.0,
                n_profil=256, n_normal=96, n_iz=64, R=50.0, Xiz=50.0,
                adim=ADIM, yaz_araligi=ADIM // 2, model="SpalartAllmaras")
            if degis:
                p = os.path.join(vaka, "system", "fvSolution")
                s = open(p).read()
                if s.count(degis[0]) != 1:
                    raise RuntimeError("fvSolution'da basinc cozucu blogu "
                                       "%d kez bulundu, 1 bekleniyordu"
                                       % s.count(degis[0]))
                open(p, "w").write(s.replace(degis[0], degis[1]))
            print("[%s] cozuluyor (%d adim)" % (ad, ADIM), flush=True)
            subprocess.run([os.path.join(BURA, "kos.sh"), vaka, "4"],
                           check=True, stdout=subprocess.DEVNULL)
            r = hesapla(vaka, alfa=0.0, mertebe=2)
            k = kalintilar(vaka)
            print("   C_D=%.6f  C_L=%+.2e   (GAMG 4000 adimda C_L=%+.1e idi)"
                  % (r["CD"], r["CL"], GAMG_4000["CL"]), flush=True)
            for x in ("Ux", "Uy"):
                if x in k:
                    print("   %s kalintisi son=%.2e  son %%10 orani %.3f  %s"
                          % (x, k[x]["son"], k[x]["oran"],
                             "YUKSELIYOR" if k[x]["oran"] > 1 else "dusuyor"),
                          flush=True)
            cikti.append(dict(ad=ad, CD=r["CD"], CL=r["CL"],
                              CD_v=r["CD_viskoz"], CD_b=r["CD_basinc"],
                              kalinti=k))
            json.dump(cikti, open(yol, "w"), indent=1)
        print()
        print("  cozucu     C_D        C_L         URANS gidisine gore")
        for d in cikti:
            print("  %-9s %.6f  %+.2e   %+.2f%%"
                  % (d["ad"], d["CD"], d["CL"],
                     (d["CD"] / URANS_GIDIS - 1) * 100))
        print("  URANS'in gevsedigi deger: %.5f" % URANS_GIDIS)
