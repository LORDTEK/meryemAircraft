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

UYARI -- %25 SATIRI GECERSIZDIR (olculdu, varsayilmadi):

Kararli RANS %25 kesitinde YAKINSAMIYOR. Uc ayri belirti ayni seyi
soyluyor. Asagidaki sayilar ILK kosudan (kOmegaSST); ayni teshis SA ile
de yapildi ve ayni cikti -- yani bu, modele degil AKISA ait:

  SA ile olculen (makaleye giden kosu):
    C_L = +2,6e-2   (%12'de +6,4e-7, %18'de +1,1e-3)
    Ux kalintisi  1,28e-4 -> 1,59e-4  YUKSELIYOR
    Uy kalintisi  9,62e-3 -> 1,19e-2  YUKSELIYOR
    Ayrilma TARAF DEGISTIRIYOR: t=2000'de 23 yuz, HEPSI ustte;
    t=4000'de 28 yuz, 8 ust / 20 alt.
    Karsilastirma: %12'de hic ayrilma yok; %18'de yalnizca firar kenari
    noktasinda 1 ust + 1 alt, yani simetrik ve durgun.

  kOmegaSST ile olculen (ilk kosu):
  - C_L = +0,048. Simetrik profil, sifir hucum acisi: C_L sifir olmak
    zorunda. %12'de -4e-6, %18'de +5e-6, %25'te +5e-2.
  - Ux kalintisi dusmuyor, YUKSELIYOR: 1,4e-5 -> 1,6e-4.
  - Firar kenarindaki ayrilma bolgesi iki yuzey arasinda TARAF
    DEGISTIRIYOR: t = 2000'de 18 ust / 7 alt, t = 4000'de 0 ust / 21 alt.
    (ortak/ayrilma.py)

Yani %25'te akis kararli degil; firar kenari ayrilmasi salintili ve
kararli cozucu onu kovaliyor. Kararli C_D (SST'de 0,012408, SA'da
0,013920) kararli bir cozum DEGILDIR ve oran olarak kullanilamaz.

%18 AYRI BIR DURUMDUR ve karistirilmamalidir. Orada ayrilma yalnizca
firar kenari noktasindadir, simetriktir ve iki yazim arasinda
degismiyor; kalintilar da hala DUSUYOR (son %10'da oran 0,63). Yani
akis kararli, sadece 4000 adim yetmemis. Bu yuzden %18 icin dogru islem
URANS degil, DAHA UZUN kosudur (ADIM parametresi).

Bunun projeye bakan yuzu daha onemli: kok kesitimiz %25'tir. Demek ki
orada hem kararli RANS hem de XFOIL/NeuralFoil (ki o da kararli, yapisik
ya da ilimli ayrilmis akis varsayar) rahat bolgelerinin disinda
calisiyor. Dogru islem zamana bagli cozum (URANS) ve zaman ortalamasidir.

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
from kilit import Kilit                                # noqa: E402

KALINLIK = [12, 18, 25]
RE = 2.0e6            # aracin KOK veterindeki Reynolds sayisi
KOK = "/tmp/kalinlik"

# MODEL SECIMI -- sonradan eklendi. Bu calisma kur()'un varsayilaniyla,
# yani kOmegaSST ile kosulmustu. Sonradan olculdu ki SST kurulumumuz
# yuzey surtunmesini referans kodlarin 5-7 yuzde altinda veriyor, SA ise
# iki bagimsiz kodla profil duzeyinde cakisiyor (bkz. dogrulama.md).
# Yani makaleye gidecek sayilar SA ile uretilmelidir. Kullanim:
#     python3 <betik> [model]
MODEL = sys.argv[1] if len(sys.argv) > 1 else "kOmegaSST"
if MODEL != "kOmegaSST":
    KOK = KOK + "-" + MODEL

# ADIM -- sonradan eklendi. 4000 adimda %18 kesiti YAKINSAMIYORDU ve bu
# olculdu, varsayilmadi: Uy kalintisi 2,98e-3'te (%12'de 2,31e-5) ve C_L
# +1,1e-3 (%12'de +6,4e-7; simetrik profilde sifir olmali). Kalintilar
# hala DUSUYORDU (son %10'da oran 0,63), yani akis kararsiz degil,
# yalnizca adim yetmemis. Ikisi ayri seydir ve karistirilmamalidir:
# %25'te kalinti YUKSELIYOR, orasi gercekten kararsiz (bkz. gecici.py).
#     python3 cfd/naca/kalinlik.py [model] [adim]
ADIM = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
if ADIM != 4000:
    KOK = KOK + "-%d" % ADIM


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


def son_kalintilar(vaka, pay=0.1):
    """log.simpleFoam'dan son kalintilar ve son %10'daki egilim.

    Neden kayda geciyor: bir satirin guvenilir olup olmadigi C_D'ye
    bakarak anlasilmaz. Simetrik profilde C_L'nin sifirdan uzaklasmasi
    ve Uy kalintisinin buyuk kalmasi, o satirin YAKINSAMADIGINI soyler.
    Bu kanit tabloyla birlikte saklanir ki okuyan kendi karar verebilsin.
    """
    import re
    p = os.path.join(vaka, "log.simpleFoam")
    if not os.path.exists(p):
        return None
    m = open(p).read()
    out = dict(yakinsadi="SIMPLE solution converged" in m)
    for ad in ("Ux", "Uy", "p", "nuTilda", "k", "omega"):
        v = [float(x) for x in re.findall(
            r"Solving for %s, Initial residual = ([0-9.e+-]+)" % ad, m)]
        if not v:
            continue
        n = len(v)
        out[ad] = dict(son=v[-1], oran=v[-1] / v[int(n * (1 - pay))])
    return out


def neuralfoil(kal, Re, xtr):
    import aerosandbox as asb
    import numpy as np
    kw = dict(alpha=0.0, Re=Re, model_size="xlarge")
    if xtr is not None:
        kw.update(xtr_upper=xtr, xtr_lower=xtr)
    r = asb.Airfoil("naca00%02d" % kal).get_aero_from_neuralfoil(**kw)
    return float(np.asarray(r["CD"]).ravel()[0])


if __name__ == "__main__":
    with Kilit(KOK):
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
                        adim=ADIM, yaz_araligi=ADIM // 2, model=MODEL)
            print("[%s] %d hucre -- cozuluyor" % (kod, bilgi["hucre"]), flush=True)
            subprocess.run([os.path.join(BURA, "kos.sh"), vaka, "4"],
                           check=True, stdout=subprocess.DEVNULL)
            r = hesapla(vaka, alfa=0.0, mertebe=2)
            kal_son = son_kalintilar(vaka)
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
                              kalinti=kal_son,
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
        # ORANLARIN ORANI yalnizca GECERLI satirlardan hesaplanir.
        #
        # Neden: bu sayi calismanin manseti ve dogrudan makaleye gider.
        # Once mekanik olarak en kalin ve en ince satirdan hesaplaniyordu;
        # %25 satiri kararsizlik yuzunden GECERSIZ oldugu halde sayiya
        # giriyordu (olculdu: 4000 adimda C_L = +2,6e-2, 16000 adimda
        # -2,7e-2 -- isaret degistiriyor, C_D %2,7 oynuyor). Yani sayi,
        # salinimin rastgele iki anindan uretilmis olurdu.
        #
        # Olcut C_L'dir: simetrik profil, sifir hucum acisi, C_L sifir
        # OLMAK ZORUNDA. Esik surukemenin %1'i alindi; gecerli satirlar
        # bunun cok altinda kaliyor (%12: 7e-7, %18: 2e-8), gecersiz
        # olan cok ustunde (%25: 3e-2).
        gecerli = [v for v in d if abs(v["CL"]) < 0.01 * v["CD"]]
        atilan = [v for v in d if v not in gecerli]
        if atilan:
            print()
            for v in atilan:
                print("  UYARI: %d%% satiri GECERSIZ -- C_L = %+.1e "
                      "(simetrik profilde sifir olmali, esik %.1e). "
                      "Kararli cozum degil; URANS gerekir (gecici.py)."
                      % (v["kalinlik"], v["CL"], 0.01 * v["CD"]))
        if len(gecerli) >= 2:
            print()
            print("  ORANLARIN ORANI -- gecis uyusmazligina dayanikli olcu")
            print("  (yalnizca gecerli satirlardan: %s)"
                  % ", ".join("%d%%" % v["kalinlik"] for v in gecerli))
            for ref, ad in (("nf_xtr0", "xtr->0"), ("nf_xtr5", "xtr=0,05")):
                t = ((gecerli[-1]["CD"] / gecerli[-1][ref])
                     / (gecerli[0]["CD"] / gecerli[0][ref]))
                print("    %-9s  (%d%% orani) / (%d%% orani) = %.3f"
                      % (ad, gecerli[-1]["kalinlik"], gecerli[0]["kalinlik"], t))
            print("    1'e yakin  -> kalinlik serit kurami icin sorun degil")
            print("    1'den buyuk -> kalinlik arttikca serit kurami sapiyor")
        else:
            print()
            print("  ORANLARIN ORANI hesaplanmadi: gecerli satir sayisi %d "
                  "(en az 2 gerekir)." % len(gecerli))
        print("bitti")
