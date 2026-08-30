# -*- coding: utf-8 -*-
"""Ag ve cozum yakinsamasini olcer; Richardson ve GCI.

Iki ayri yakinsama sorulur ve karistirilmaz:

  COZUM yakinsamasi  -- yineleme ilerledikce C_D duruyor mu?
  AG yakinsamasi     -- hucre kucultuldukce C_D bir degere gidiyor mu?

Ikincisi icin Roache'un ag yakinsama indeksi (GCI) kullaniliyor. Gozlenen
mertebe p, ardisik uc seviyeden cozuluyor:

    eps32 = f3 - f2 ,  eps21 = f2 - f1 ,  s = sign(eps32/eps21)
    p = |ln|eps32/eps21| + ln((r21^p - s)/(r32^p - s))| / ln(r21)

Oran r sabit olmadigi icin (hucre sayilari 9216 -> 20736 -> 36864 -> 82944)
p yinelemeli cozulur. h olcusu iki boyutta h ~ 1/sqrt(N) alinir.

GCI, "bu sayinin ag yuzunden belirsizligi" icin bir bant verir; guvenlik
carpani ardisik uc ag kullanildiginda 1.25'tir.
"""
import json, math, os, sys


def mertebe(f1, f2, f3, r21, r32, tur=200):
    """Gozlenen yakinsama mertebesi. f1 en INCE ag."""
    e21, e32 = f2 - f1, f3 - f2
    if e21 == 0 or e32 == 0:
        return None
    o = e32 / e21
    if o <= 0:                      # salinimli yakinsama: mertebe tanimsiz
        return None
    s = 1.0 if o > 0 else -1.0
    p = 2.0
    for _ in range(tur):
        q = math.log((r21 ** p - s) / (r32 ** p - s))
        yeni = abs(math.log(abs(o)) + q) / math.log(r21)
        if abs(yeni - p) < 1e-12:
            p = yeni
            break
        p = 0.5 * (p + yeni)        # gevsetilmis, salinimi keser
    return p


def gci(f1, f2, r21, p, fs=1.25):
    """En ince agin ag yakinsama indeksi, yuzde."""
    if f1 == 0:
        return None
    return fs * abs((f2 - f1) / f1) / (r21 ** p - 1) * 100


def coz(sonuc, alan="CD"):
    """sonuc: tarama.py'nin json'u. En ince uc seviyeyi kullanir."""
    s = sorted(sonuc, key=lambda d: d["hucre"])
    if len(s) < 3:
        return None
    ucu = s[-3:]                            # kaba -> ince
    f3, f2, f1 = [d["gecmis"][-1][alan] for d in ucu]
    N3, N2, N1 = [d["hucre"] for d in ucu]
    h = lambda N: 1.0 / math.sqrt(N)
    r21, r32 = h(N2) / h(N1), h(N3) / h(N2)
    p = mertebe(f1, f2, f3, r21, r32)
    if p is None:
        return dict(p=None, f1=f1, f2=f2, f3=f3, r21=r21, r32=r32,
                    fext=None, gci=None,
                    adlar=[d["ad"] for d in ucu])
    fext = (r21 ** p * f1 - f2) / (r21 ** p - 1)
    return dict(p=p, f1=f1, f2=f2, f3=f3, r21=r21, r32=r32,
                fext=fext, gci=gci(f1, f2, r21, p),
                adlar=[d["ad"] for d in ucu])


def yaz(sonuc):
    print("COZUM YAKINSAMASI -- her seviyede C_D'nin yineleme gecmisi")
    for s in sorted(sonuc, key=lambda d: d["hucre"]):
        g = s["gecmis"]
        print("  %-3s %6d hucre" % (s["ad"], s["hucre"]))
        for k, v in enumerate(g):
            d = ""
            if k:
                d = "   degisim %+.2e" % (v["CD"] - g[k - 1]["CD"])
            print("     t=%-6s C_D=%.6f%s" % (v["zaman"], v["CD"], d))
        print("     y+ ortalama %.2f  en fazla %.2f  |  C_L = %+.2e"
              % (g[-1]["yp_ort"], g[-1]["yp_max"], g[-1]["CL"]))

    print()
    print("AG YAKINSAMASI")
    print("  %-4s %8s %10s %10s %10s %8s" %
          ("ag", "hucre", "C_D", "basinc", "viskoz", "y+ ort"))
    for s in sorted(sonuc, key=lambda d: d["hucre"]):
        g = s["gecmis"][-1]
        print("  %-4s %8d %10.6f %10.6f %10.6f %8.2f"
              % (s["ad"], s["hucre"], g["CD"], g["CD_b"], g["CD_v"], g["yp_ort"]))

    r = coz(sonuc, "CD")
    if not r:
        return
    print()
    print("  Richardson (%s, %s, %s):" % tuple(r["adlar"]))
    print("    inceltme orani  r21 = %.4f   r32 = %.4f" % (r["r21"], r["r32"]))
    if r["p"] is None:
        print("    gozlenen mertebe: TANIMSIZ -- yakinsama salinimli.")
        print("    Ardisik farklarin isareti degisiyor; Richardson bu halde")
        print("    uygulanmaz. Daha ince bir seviye ya da daha siki cozum")
        print("    yakinsamasi gerekir.")
    else:
        print("    gozlenen mertebe p = %.2f" % r["p"])
        print("    h -> 0 kestirimi   C_D = %.6f" % r["fext"])
        print("    en ince agin GCI'si  %.2f %%" % r["gci"])


if __name__ == "__main__":
    yol = sys.argv[1] if len(sys.argv) > 1 else "/tmp/tarama/sonuc.json"
    if not os.path.exists(yol):
        raise SystemExit("sonuc dosyasi yok: " + yol)
    yaz(json.load(open(yol)))
