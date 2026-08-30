# -*- coding: utf-8 -*-
"""%25 kesiti icin zamana bagli cozum (URANS) ve zaman ortalamasi.

Neden gerekli: kalinlik calismasi %25'te kararli RANS'in YAKINSAMADIGINI
gosterdi -- C_L simetrik profilde +0,048, Ux kalintisi dusmek yerine
yukseliyor, firar kenari ayrilmasi iki yuzey arasinda taraf degistiriyor.
Akis kararli degil. Kararli bir cozucuyle kararsiz bir akisi cozmeye
calismak, salinimin ortasinda rastgele bir ana bakmak demektir.

Iki asama, bilerek:

  KESIF   Kisa bir kosu; amaci C_L'nin salinim periyodunu OLCMEK. Periyot
          bilinmeden ne zaman adimi ne de ortalama penceresi secilebilir;
          tahminle secmek, sonucu tahmine baglamak olurdu.
  URETIM  Olculen periyoda gore ayarlanmis uzun kosu; ortalama tam sayida
          cevrim uzerinden alinir. Yarim cevrim artigi, ortalamaya
          dogrudan yanlilik olarak girer.

Not: zaman ortalamali bir C_D ile NeuralFoil'in kararli C_D'sini
karsilastirmak da kendi basina sorunludur -- XFOIL kararli, yapisik ya da
ilimli ayrilmis akis varsayar. Bu karsilastirma bir esdegerlik degil, bir
BUYUKLUK KIYASIDIR ve oyle sunulmalidir.
"""
import json, math, os, subprocess, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kur import kur                                    # noqa: E402
from kuvvet import hesapla                             # noqa: E402
from kilit import Kilit                                # noqa: E402

KOD, RE = "0025", 2.0e6
KOK = "/tmp/gecici"

# MODEL SECIMI -- sonradan eklendi. Makaleye gidecek sayilar SA ile
# uretilir: SST kurulumumuz yuzey surtunmesini referans kodlarin 5-7
# yuzde altinda veriyor, SA ise iki bagimsiz kodla profil duzeyinde
# cakisiyor (bkz. dogrulama.md). Kullanim:
#     python3 cfd/naca/gecici.py [kesif|uretim] [model]
MODEL = sys.argv[2] if len(sys.argv) > 2 else "kOmegaSST"
if MODEL != "kOmegaSST":
    KOK = KOK + "-" + MODEL


def zamanlar(vaka):
    z = []
    for a in os.listdir(vaka):
        try:
            v = float(a)
        except ValueError:
            continue
        if v > 0 and os.path.isdir(os.path.join(vaka, a)):
            z.append((v, a))
    return sorted(z)


def gecmis(vaka):
    """Her yazilmis zamanda C_D ve C_L."""
    out = []
    for v, a in zamanlar(vaka):
        r = hesapla(vaka, alfa=0.0, zaman=a, mertebe=2)
        out.append((v, r["CD"], r["CL"]))
    return out


def periyot(g, alan=2):
    """C_L'nin (ya da C_D'nin) sifir gecislerinden periyot kestirimi.

    Ortalamadan sapmanin isaret degistirdigi yerler bulunur; ardisik iki
    gecis yarim periyottur. Ilk ucte birlik gecis suresi atilir.
    """
    if len(g) < 8:
        return None
    n0 = len(g) // 3
    d = g[n0:]
    ort = sum(v[alan] for v in d) / len(d)
    gecis = []
    for i in range(1, len(d)):
        a, b = d[i - 1][alan] - ort, d[i][alan] - ort
        if a == 0 or (a < 0) != (b < 0):
            w = 0.0 if b == a else a / (a - b)
            gecis.append(d[i - 1][0] + w * (d[i][0] - d[i - 1][0]))
    if len(gecis) < 3:
        return None
    yari = [gecis[i] - gecis[i - 1] for i in range(1, len(gecis))]
    return 2.0 * sum(yari) / len(yari)


def kos(ad, T, dt0, dyaz):
    vaka = os.path.join(KOK, ad)
    bilgi = kur(vaka, kod=KOD, Re=RE, alfa=0.0, yplus=1.0,
                n_profil=256, n_normal=96, n_iz=64, R=50.0, Xiz=50.0,
                gecici=(T, dt0, dyaz), model=MODEL)
    print("[%s] %d hucre  T=%g s  dt0=%g  yazim %g s"
          % (ad, bilgi["hucre"], T, dt0, dyaz), flush=True)
    subprocess.run([os.path.join(BURA, "kos.sh"), vaka, "4"],
                   check=True, stdout=subprocess.DEVNULL)
    return vaka


def ortala(g, T_per):
    """TAM SAYIDA cevrim uzerinden ortalama. Yarim cevrim artigi
    ortalamaya dogrudan yanlilik olarak girer, o yuzden kirpilir."""
    if not g:
        return None
    son = g[-1][0]
    if T_per:
        n = int((son - g[len(g) // 3][0]) / T_per)
        if n >= 1:
            bas = son - n * T_per
            d = [v for v in g if v[0] >= bas]
        else:
            d = g[len(g) // 3:]
    else:
        d = g[len(g) // 3:]
    cd = [v[1] for v in d]
    cl = [v[2] for v in d]
    return dict(n=len(d), t0=d[0][0], t1=d[-1][0],
                CD=sum(cd) / len(cd), CD_min=min(cd), CD_max=max(cd),
                CL=sum(cl) / len(cl), CL_genlik=(max(cl) - min(cl)) / 2)


if __name__ == "__main__":
    with Kilit(KOK):
        asama = sys.argv[1] if len(sys.argv) > 1 else "kesif"
        yol = os.path.join(KOK, "sonuc.json")
        d = json.load(open(yol)) if os.path.exists(yol) else {}

        if asama == "kesif":
            vaka = kos("kesif", T=0.2, dt0=1e-4, dyaz=0.002)
            g = gecmis(vaka)
            for v in g[::max(1, len(g) // 25)]:
                print("   t=%.4f  C_D=%.6f  C_L=%+.5f" % v, flush=True)
            T = periyot(g)
            print("\n  olculen periyot: %s" % ("%.5f s" % T if T else "BULUNAMADI"))
            d["kesif"] = dict(periyot=T, gecmis=g)
            json.dump(d, open(yol, "w"), indent=1)
            if T:
                print("  uretim kosusu icin oneri: T = %.2f s (20 cevrim), "
                      "dt0 = %.1e, yazim = %.4f s"
                      % (20 * T, T / 400, T / 20))
        else:
            T = d.get("kesif", {}).get("periyot")
            if not T:
                raise SystemExit("once kesif asamasi kosulmali")
            vaka = kos("uretim", T=20 * T, dt0=T / 400, dyaz=T / 20)
            g = gecmis(vaka)
            o = ortala(g, T)
            print("\n  ZAMAN ORTALAMASI (%d ornek, t = %.3f .. %.3f)"
                  % (o["n"], o["t0"], o["t1"]))
            print("    C_D = %.6f   (en az %.6f, en cok %.6f)"
                  % (o["CD"], o["CD_min"], o["CD_max"]))
            print("    C_L = %+.6f  genlik %.5f" % (o["CL"], o["CL_genlik"]))
            d["uretim"] = dict(periyot=T, ortalama=o, gecmis=g)
            json.dump(d, open(yol, "w"), indent=1)
        print("bitti")
