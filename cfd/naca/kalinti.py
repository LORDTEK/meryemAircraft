# -*- coding: utf-8 -*-
"""Ag seviyelerini AYNI KALINTI DUZEYINDE karsilastirir.

Neden gerekli: farkli cozunurlukteki aglar ayni yineleme sayisinda ayni
olcude yakinsamaz. Daha cok hucreli ag ayni adimda daha geride kalir.
Bu yuzden "3000 yinelemede hepsi" diye karsilastirmak, AG farkinin
uzerine YAKINSAMA farkini bindirir ve ikisi ayirt edilemez.

Olculdu: B ailesinde 3000 yinelemede B3'un Ux kalintisi 6,2e-7, B4'unki
8,3e-7. Ayni yineleme sayisinda B3 -> B4 farki +%0,77; ayni KALINTI
duzeyinde +%0,35 - %0,40. Yani gorunen salinimın yaklasik yarisi
yakinsama farkindan geliyordu, yarisi gercek.

Yontem: her seviyenin log'undan Ux ilk kalintisi cikarilir, yazim
zamanlariyla eslesitirilir, verilen hedef kalinti duzeyinde C_D logaritmik
ara degerle bulunur.
"""
import json, math, os, re, sys


def kalinti_gecmisi(vaka, alan="Ux"):
    """{yineleme: ilk kalinti} -- log.simpleFoam'dan."""
    d, n = {}, 0
    yol = os.path.join(vaka, "log.simpleFoam")
    if not os.path.exists(yol):
        return d
    for satir in open(yol):
        if satir.startswith("Time = "):
            try:
                n = int(satir.split("=")[1])
            except ValueError:
                n = 0
        elif n and ("Solving for " + alan) in satir:
            m = re.search(r"Initial residual = ([0-9.eE+-]+)", satir)
            if m:
                d[n] = float(m.group(1))
    return d


def cd_kalintida(vaka, gecmis, hedef, alan="Ux"):
    """Verilen kalinti duzeyinde C_D; yoksa None.

    C_D kalintiya gore logaritmik ara degerle bulunur -- kalinti ustel
    azaldigi icin dogrusal ara deger yaniltir.
    """
    kal = kalinti_gecmisi(vaka, alan)
    cd = {int(g["zaman"]): g["CD"] for g in gecmis}
    ts = sorted(t for t in cd if t in kal)
    alt = [t for t in ts if kal[t] >= hedef]
    ust = [t for t in ts if kal[t] < hedef]
    if not alt or not ust:
        return None
    t1, t2 = max(alt), min(ust)
    r1, r2 = kal[t1], kal[t2]
    if r1 <= 0 or r2 <= 0 or r1 == r2:
        return None
    w = (math.log(hedef) - math.log(r1)) / (math.log(r2) - math.log(r1))
    return cd[t1] + w * (cd[t2] - cd[t1])


if __name__ == "__main__":
    yol = sys.argv[1] if len(sys.argv) > 1 else "/tmp/tarama-B/sonuc.json"
    kok = os.path.dirname(yol)
    d = sorted(json.load(open(yol)), key=lambda x: x["hucre"])

    print("  ag    hucre   son yineleme  Ux kalintisi     C_D")
    for s in d:
        kal = kalinti_gecmisi(os.path.join(kok, s["ad"]))
        g = s["gecmis"][-1]
        t = int(g["zaman"])
        print("  %-4s %7d  %8d      %.3e   %.6f"
              % (s["ad"], s["hucre"], t, kal.get(t, float("nan")), g["CD"]))

    print()
    print("  AYNI KALINTI DUZEYINDE")
    basliklar = "  hedef    " + "".join("%-11s" % s["ad"] for s in d)
    print(basliklar)
    for hedef in (3e-6, 2e-6, 1.5e-6, 1.2e-6, 1e-6, 8e-7):
        satir = "  %.1e" % hedef
        deger = []
        for s in d:
            v = cd_kalintida(os.path.join(kok, s["ad"]), s["gecmis"], hedef)
            deger.append(v)
            satir += "  %-9s" % ("%.6f" % v if v else "-")
        print(satir)
    print()
    print("  Ayni yineleme sayisindaki fark, AG farkinin uzerine YAKINSAMA")
    print("  farkini bindirir. Ustteki tablo ikisini ayirir.")
