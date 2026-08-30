# -*- coding: utf-8 -*-
"""2. BASAMAK -- serit kurami kalin kesitte nerede ayrisiyor?

Makalenin `aero/` kurulumunun kendi kaydettigi en zayif halkasi:

    "Govde bir profil degildir. Serit yontemi kok kesitini %25
     kalinliginda iki boyutlu bir NACA profili gibi ele aliyor."

Bu halkada IKI ayri supheli var ve karistirilmamalari gerekir:

    (a) KALINLIK  -- iki boyutlu bir cozucu (XFOIL uzerine egitilmis
        NeuralFoil) %25 kalinlikta hala dogru mu?
    (b) UC BOYUTLULUK -- kanat-govde merkez govdesinde akis zaten iki
        boyutlu degil.

Bu betik yalnizca (a)'yi olcer. Cozum de karsilastirma da IKI BOYUTLUDUR;
aradaki fark ne cikarsa yalnizca kalinliktan gelir. (b) ucuncu basamaga
kalir. Ikisini tek bir kosuda olcup farki "govde etkisi" diye
adlandirmak, iki hatayi tek isme yazmak olurdu.

ESLESTIRME -- burasi onemli ve duz degil:

`cd0.py` NeuralFoil'i xtr = 0,05 ile cagirir (gecis %5 veterde
tetiklenmis). Buradaki RANS ise TAMAMEN TURBULANSLI, yani gecis hucum
kenarinda. Bunlar ayni sey degildir.

Akla ilk gelen cozum -- NeuralFoil'i xtr = 0 ile cagirmak -- CALISMAZ.
Olculdu: NeuralFoil'in verdigi C_D, xtr kucultuldukce once BUYUYOR,
xtr ~ 0,02'de tepe yapiyor, sonra DUSUYOR. Gecis one alindikca surtunme
monoton artmali; bu davranis fiziksel degil. Nedeni acik: NeuralFoil
XFOIL uzerine egitilmistir ve hucum kenarina cok yakin zorlanmis gecis
egitim kumesinde yok denecek kadar azdir, yani orada disdegerleme
yapiyor. Olculen tepe (Re = 2e6, alfa = 0):

    xtr     %12       %18       %25
    0,000  0,009502  0,010960  0,013055     <- guvenilmez
    0,010  0,009939  0,011511  0,013701     <- guvenilmez
    0,020  0,009992  0,011600  0,013804     <- tepe, guvenilmez
    0,030  0,009881  0,011479  0,013663     <- buradan sonra monoton
    0,050  0,009656  0,011221  0,013368     <- cd0.py bunu kullaniyor
    0,100  0,009203  0,010667  0,012709
    0,200  0,008366  0,009512  0,011084

Bu, cd0.py'nin dayandigi aracin sinirlarina dair kendi basina bir
bulgudur ve kayda geciyor: kullanilan xtr = 0,05, guvenilmez bolgenin
hemen ustunde ama ona yakin.

Bu yuzden karsilastirma iki referansla yapiliyor:
  - xtr = 0,05           cd0.py'nin gercekte kullandigi deger
  - xtr -> 0 disdegerlemesi   yalnizca GUVENILIR bolgeden (xtr >= 0,03)
                              dogrusal geri atim; tamamen turbulansliya
                              en yakin savunulabilir NeuralFoil degeri

ASIL OLCU: ORANLARIN ORANI.
Gecis islemindeki uyusmazlik her kalinlikta AYNI yonde ve yaklasik ayni
buyuklukte oldugu icin, RANS/NF oraninin KALINLIKLA nasil degistigi bu
uyusmazliga karsi dayaniklidir. Oran %12 ile %25 arasinda sabit kaliyorsa
kalinlik serit kurami icin bir sorun DEGILDIR; buyuyorsa sorundur. Tek
bir kalinliktaki mutlak oran ise gecis uyusmazligini de icerir ve tek
basina yorumlanmamalidir.
"""
import os, sys, subprocess, json

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kur import kur                                    # noqa: E402
from kuvvet import hesapla                             # noqa: E402

KALINLIK = [12, 18, 25]
RE = 2.0e6            # aracin KOK veterindeki Reynolds sayisi
KOK = "/tmp/kalinlik"


def nf_sifira(kal, Re, ornek=(0.03, 0.05, 0.10, 0.20)):
    """NeuralFoil'in xtr -> 0 degerini, YALNIZCA guvenilir bolgeden
    (xtr >= 0,03) dogrusal en kucuk kareler ile geri atar.

    Agin xtr < 0,03'te verdigi degerler kullanilmaz: orada C_D, gecis one
    alindikca dusuyor, ki bu fiziksel degildir (bkz. dosya basi).
    """
    x = list(ornek)
    y = [neuralfoil(kal, Re, v) for v in x]
    n = len(x)
    mx = sum(x) / n
    my = sum(y) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    egim = sxy / sxx
    return my - egim * mx


def neuralfoil(kal, Re, xtr):
    import aerosandbox as asb
    import numpy as np
    kw = dict(alpha=0.0, Re=Re, model_size="xlarge")
    if xtr is not None:
        kw.update(xtr_upper=xtr, xtr_lower=xtr)
    r = asb.Airfoil("naca00%02d" % kal).get_aero_from_neuralfoil(**kw)
    return float(np.asarray(r["CD"]).ravel()[0])


if __name__ == "__main__":
    os.makedirs(KOK, exist_ok=True)
    yol = os.path.join(KOK, "sonuc.json")
    cikti = json.load(open(yol)) if os.path.exists(yol) else []
    yapilan = {d["kalinlik"] for d in cikti}

    for kal in KALINLIK:
        if kal in yapilan:
            continue
        kod = "00%02d" % kal
        vaka = os.path.join(KOK, kod)
        bilgi = kur(vaka, kod=kod, Re=RE, alfa=0.0, yplus=1.0,
                    n_profil=256, n_normal=96, n_iz=64, R=50.0, Xiz=50.0,
                    adim=4000, yaz_araligi=2000)
        print("[%s] %d hucre -- cozuluyor" % (kod, bilgi["hucre"]), flush=True)
        subprocess.run([os.path.join(BURA, "kos.sh"), vaka, "4"],
                       check=True, stdout=subprocess.DEVNULL)
        r = hesapla(vaka, alfa=0.0, mertebe=2)
        nf0 = nf_sifira(kal, RE)
        nf5 = neuralfoil(kal, RE, 0.05)
        nfs = neuralfoil(kal, RE, None)
        print("   RANS C_D=%.6f (basinc %.6f  viskoz %.6f)  y+ %.2f  C_L=%+.1e"
              % (r["CD"], r["CD_basinc"], r["CD_viskoz"], r["yplus_ort"],
                 r["CL"]), flush=True)
        print("   NF xtr->0 disdeger. %.6f   -> RANS/NF = %.3f"
              % (nf0, r["CD"] / nf0), flush=True)
        print("   NF xtr=0,05         %.6f   -> RANS/NF = %.3f  (cd0.py)"
              % (nf5, r["CD"] / nf5), flush=True)
        print("   NeuralFoil serbest  %.6f" % nfs, flush=True)
        cikti.append(dict(kalinlik=kal, hucre=bilgi["hucre"], CD=r["CD"],
                          CD_b=r["CD_basinc"], CD_v=r["CD_viskoz"],
                          CL=r["CL"], yp=r["yplus_ort"],
                          nf_xtr0=nf0, nf_xtr5=nf5, nf_serbest=nfs))
        json.dump(cikti, open(yol, "w"), indent=1)

    print()
    print("  t/c    RANS      NF(xtr->0)  oran    NF(xtr=,05)  oran")
    d = sorted(cikti, key=lambda x: x["kalinlik"])
    for v in d:
        print("  %2d%%   %.6f  %.6f   %.3f   %.6f   %.3f"
              % (v["kalinlik"], v["CD"], v["nf_xtr0"],
                 v["CD"] / v["nf_xtr0"], v["nf_xtr5"],
                 v["CD"] / v["nf_xtr5"]))
    if len(d) >= 2:
        print()
        print("  ORANLARIN ORANI -- gecis uyusmazligina dayanikli olcu")
        for ref, ad in (("nf_xtr0", "xtr->0"), ("nf_xtr5", "xtr=0,05")):
            t = (d[-1]["CD"] / d[-1][ref]) / (d[0]["CD"] / d[0][ref])
            print("    %-9s  (%d%% orani) / (%d%% orani) = %.3f"
                  % (ad, d[-1]["kalinlik"], d[0]["kalinlik"], t))
        print("    1'e yakin  -> kalinlik serit kurami icin sorun degil")
        print("    1'den buyuk -> kalinlik arttikca serit kurami sapiyor")
    print("bitti")
