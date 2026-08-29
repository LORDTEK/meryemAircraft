# -*- coding: utf-8 -*-
"""meryemAircraft planformunu, makaledeki ok acisi yasalarindan yeniden kurar.

Yasalar mkfig06.py ve mkfig08.py ile AYNIDIR — sayilar tek yerden gelsin diye
burada da bagimsiz olarak yeniden turetiliyor ve kunye degerleriyle sinaniyor.
"""
import math

D2R = math.pi / 180.0

P = dict(kokVeter=0.97, okKok=45.0, okUc=35.0, okTE=25.0, kirpma=67.0,
         tcKok=25.0, tcUc=12.0)


def birlesme_acikligi(p=P, n=4000):
    """Hucum ve firar kenarinin bulusacagi yari-aciklik (ikiye bolerek)."""
    lo, hi = 0.1, 60 * p["kokVeter"]
    for _ in range(200):
        mid = (lo + hi) / 2
        adim = mid / n
        x = y = 0.0
        carpti = False
        for _ in range(n):
            s = (p["okKok"] + (p["okUc"] - p["okKok"]) * min((y + adim / 2) / mid, 1)) * D2R
            x += math.tan(s) * adim
            y += adim
            if p["kokVeter"] + y * math.tan(p["okTE"] * D2R) - x <= 0:
                carpti = True
                break
        if carpti:
            hi = mid
        else:
            lo = mid
        if abs(hi - lo) < 1e-7:
            break
    return (lo + hi) / 2


def istasyonlar(n=60, p=P):
    """n adet yari-aciklik istasyonu: (y, x_hucum, veter, t/c, ok_acisi)."""
    birlesme = birlesme_acikligi(p)
    yari = birlesme * p["kirpma"] / 100.0
    adim = yari / n
    y = x = 0.0
    cikti = [(0.0, 0.0, p["kokVeter"], p["tcKok"] / 100.0, p["okKok"])]
    for i in range(n):
        t = (y + adim / 2) / birlesme
        s = p["okKok"] + (p["okUc"] - p["okKok"]) * min(t, 1)
        x += math.tan(s * D2R) * adim
        y += adim
        veter = p["kokVeter"] + y * math.tan(p["okTE"] * D2R) - x
        f = y / yari
        tc = (p["tcKok"] + (p["tcUc"] - p["tcKok"]) * f) / 100.0
        ok = p["okKok"] + (p["okUc"] - p["okKok"]) * min(y / birlesme, 1)
        cikti.append((y, x, veter, tc, ok))
    return cikti, yari, birlesme


def olcuier(p=P):
    ist, yari, birlesme = istasyonlar(p=p)
    alan = 0.0
    for a, b in zip(ist[:-1], ist[1:]):
        alan += 0.5 * (a[2] + b[2]) * (b[0] - a[0])
    alan *= 2                      # iki yari
    aciklik = 2 * yari
    return dict(aciklik=aciklik, alan=alan, AR=aciklik ** 2 / alan,
                kokVeter=ist[0][2], ucVeter=ist[-1][2],
                sivrilme=ist[-1][2] / ist[0][2], ucOk=ist[-1][4],
                birlesme=birlesme, yari=yari)


if __name__ == "__main__":
    o = olcuier()
    kunye = dict(aciklik=3.453, alan=1.9785, AR=6.026, ucVeter=0.236, ucOk=38.30)
    print(f"{'buyukluk':<12}{'hesap':>10}{'kunye':>10}{'fark %':>9}")
    for k, v in kunye.items():
        print(f"{k:<12}{o[k]:10.4f}{v:10.4f}{100*abs(o[k]-v)/v:9.2f}")
    print(f"\nkok veter {o['kokVeter']:.3f} m · sivrilme {o['sivrilme']:.3f} · "
          f"yari-aciklik {o['yari']:.4f} m")
