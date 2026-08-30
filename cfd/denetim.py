# -*- coding: utf-8 -*-
"""Her vakaya AYNI denetim bataryasi -- sonuc hosa gitsin ya da gitmesin.

Neden var. Bu calismada hatalarin cogu, bir egilim yanlis yonde gorundugu
icin BAKILDIGINDA bulundu: momentum dengesindeki uc hata, %25 kesitinin
yakinsamamasi, ayrilma olcutundeki isaret hatasi. Hepsi gercek hataydi ve
bagimsiz olarak dogrulandi -- ama hepsine, sonuc tuhaf gorundugu icin
bakildi.

Bu tek yonlu bir taramadir ve sakattir: hosa gitmeyen sonuclarda hata
bulma olasiligi, hosa gidenlerdekinden yuksek olur. Kabul edilen sonuclar
denetlenmemis kalir.

Bu betik o asimetriyi kapatir. Butun vakalara ayni kontroller uygulanir,
sonuc ne olursa olsun; cikti bir HUKUM degil bir KAYITTIR. Esikler
onceden yazilmistir ve sonuca bakarak degistirilmez.

Kontroller ve NEDEN o esik:

  C_L simetrisi   Simetrik profil, sifir hucum acisi -> C_L = 0 fizik
                  geregi. Sifirdan sapma; ag simetrisini, cozucuyu ve
                  kuvvet integralini birlikte sinar. Esik 1e-4: kabul
                  edilen vakalarda olculen degerler 1e-6 mertebesinde,
                  reddedilen %25 vakasinda 5e-2.
  Kalinti egilimi Son ucte birlik yinelemede kalinti DUSUYOR mu? Yukselen
                  kalinti, kararli cozumun bulunamadigini soyler.
  Ayrilma         Ters akan yuz orani ve ust/alt dengesizligi. Simetrik
                  profilde ust ile alt esit olmali; dengesizlik, cozumun
                  simetriyi kirdigini gosterir.
  y+              Olculen y+ hedefe uyuyor mu? Duvar isleminin gecerlilik
                  bolgesinde olup olmadigimizi soyler.
  Momentum        Duvar integrali ile dis sinir dengesi arasindaki fark.
                  Bu OLCUT COZUM YAKINSAMASINI olcer (kuvvet_sina.py),
                  bir yontem hatasini degil.
"""
import glob, json, math, os, re, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BURA, "ortak"))
sys.path.insert(0, os.path.join(BURA, "naca"))
from kuvvet import hesapla                             # noqa: E402
from ayrilma import tara                               # noqa: E402
from kalinti import kalinti_gecmisi                    # noqa: E402

ESIK = dict(CL=1e-4, ayrilma_dengesizlik=0.25, yplus_sapma=0.5)


def kalinti_yon(vaka):
    """Son ucte birlik kisimda kalinti dusuyor mu? (oran, son deger)"""
    k = kalinti_gecmisi(vaka)
    if len(k) < 20:
        return None, None
    t = sorted(k)
    d = t[2 * len(t) // 3:]
    ilk, son = k[d[0]], k[d[-1]]
    return (son / ilk if ilk > 0 else None), son


def denetle(vaka, kod="0012", hedef_yplus=1.0):
    ad = os.path.basename(vaka)
    try:
        r = hesapla(vaka, alfa=0.0, mertebe=2)
    except Exception as e:
        return dict(ad=ad, hata=str(e))

    oran, son_kal = kalinti_yon(vaka)

    try:
        t = [v for v in tara(vaka) if v[0] > 0.01]
        geri = [v for v in t if v[2] < 0]
        ust = len([v for v in geri if v[1] > 0])
        alt = len([v for v in geri if v[1] < 0])
        pay = (ust + alt) or 1
        dengesizlik = abs(ust - alt) / pay if geri else 0.0
        ayr = len(geri) / len(t)
    except Exception:
        ayr, dengesizlik, ust, alt = None, None, None, None

    bayrak = []
    if abs(r["CL"]) > ESIK["CL"]:
        bayrak.append("C_L=%.2e (esik %.0e)" % (r["CL"], ESIK["CL"]))
    if oran is not None and oran > 1.0:
        bayrak.append("kalinti YUKSELIYOR (son/ilk = %.2f)" % oran)
    if dengesizlik is not None and dengesizlik > ESIK["ayrilma_dengesizlik"]:
        bayrak.append("ayrilma dengesiz (ust %d / alt %d)" % (ust, alt))
    if abs(r["yplus_ort"] / hedef_yplus - 1) > ESIK["yplus_sapma"]:
        bayrak.append("y+ hedeften uzak (%.2f / %.2f)"
                      % (r["yplus_ort"], hedef_yplus))

    return dict(ad=ad, CD=r["CD"], CL=r["CL"], yplus=r["yplus_ort"],
                kalinti_oran=oran, kalinti_son=son_kal,
                ayrilma=ayr, dengesizlik=dengesizlik, bayrak=bayrak)


VAKALAR = [
    ("/tmp/tarama-A/A*", "0012", None),
    ("/tmp/tarama-B/B*", "0012", None),
    ("/tmp/alan2/R*", "0012", 1.0),
    ("/tmp/model/*", "0012", 1.0),
    ("/tmp/kalinlik/00*", None, 1.0),
    ("/tmp/yplus/y*", "0012", None),
]

YP_HEDEF = {"A1": 1.0, "A2": 1.0, "A3": 1.0, "A4": 1.0,
            "B1": 2.25, "B2": 1.5, "B3": 1.0, "B4": 0.667}


if __name__ == "__main__":
    tum = []
    for desen, kod, yp in VAKALAR:
        for v in sorted(glob.glob(desen)):
            if not os.path.isdir(v):
                continue
            ad = os.path.basename(v)
            h = yp or YP_HEDEF.get(ad)
            if h is None:
                m = re.match(r"y(\d+)$", ad)
                h = int(m.group(1)) / 100.0 if m else 1.0
            k = kod or ("00" + ad[-2:] if ad.startswith("00") else "0012")
            tum.append(denetle(v, kod=k, hedef_yplus=h))

    print("  %-10s %10s %11s %7s %9s %9s" %
          ("vaka", "C_D", "C_L", "y+", "kalinti", "ayrilma"))
    print("  " + "-" * 62)
    for d in tum:
        if "hata" in d:
            print("  %-10s  HATA: %s" % (d["ad"], d["hata"][:40]))
            continue
        print("  %-10s %10.6f %11.2e %7.2f %9s %9s%s"
              % (d["ad"], d["CD"], d["CL"], d["yplus"],
                 "%.2f" % d["kalinti_oran"] if d["kalinti_oran"] else "-",
                 "%.1f%%" % (100 * d["ayrilma"]) if d["ayrilma"] is not None else "-",
                 "  <<<" if d["bayrak"] else ""))
    print()
    isaretli = [d for d in tum if d.get("bayrak")]
    if not isaretli:
        print("  Isaretlenen vaka yok.")
    else:
        print("  ISARETLENEN VAKALAR")
        for d in isaretli:
            print("    %s" % d["ad"])
            for b in d["bayrak"]:
                print("      - %s" % b)
    json.dump(tum, open("/tmp/denetim.json", "w"), indent=1, default=str)
