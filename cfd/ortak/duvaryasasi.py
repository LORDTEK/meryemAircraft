# -*- coding: utf-8 -*-
"""Sinir tabakasi profilini duvar degiskenlerinde cikarir: u+ , y+ ve
logaritmik tabakanin turbulans dengesi.

Neden: SST kurulumumuzun C_D'si referans kodlarin %5 altinda. Sebep
arayisinda serbest akis elendi. Bu sinama DISARIDAN HICBIR VERI
GEREKTIRMEZ, cunku referansi fizigin kendisidir:

    viskoz alt tabaka   u+ = y+
    logaritmik tabaka   u+ = (1/kappa) ln y+ + B ,  kappa ~ 0.41 , B ~ 5.0

Log tabakasi YUKARI kaymissa (ayni y+'ta u+ daha buyukse) bu, u_tau'nun
kucuk oldugu anlamina gelir -- ve C_f = 2 (u_tau/U)^2 oldugu icin dogrudan
dusuk surtunme demektir. Yani kayma varsa, dusuk C_D'nin nedeni sinir
tabakasinin yapisindadir, kuvvet integralinde ya da agda degil.

Ikinci sinama (log_denge) kaymanin HANGI denklemden geldigini sorar.
Denge halindeki logaritmik tabakada k-omega ailesinin uc bagintisi
kesindir -- model sabitlerinden cikar, olcume dayanmaz:

    nu_t   = kappa u_tau y            (uretim = yitim, karisim uzunlugu)
    k      = u_tau^2 / sqrt(beta*)    beta* = 0.09  ->  k+ = 3.333
    omega  = u_tau / (sqrt(beta*) kappa y)

Ucu birbirine bagli (nu_t = k/omega ozdesligi), yani ikisi saglanip biri
saglanmiyorsa okuma hatasi vardir. Ucu de sapiyorsa model o bolgede
denge halinde degildir. Hangisinin saptigi, kusurun k denkleminde mi
omega denkleminde mi oldugunu soyler.

Profil, duvardan disariya hucre hucre yurunerek cikarilir (Ag.karsi_hucre).
Yapisal C-agi oldugu icin bu yurume duvara dik dogrultuyu izler.
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from foamoku import Ag, Alan, son_zaman        # noqa: E402
from kuvvet import nu_oku                      # noqa: E402

KAPPA, B, BETA_YILDIZ = 0.41, 5.0, 0.09


def _alan(vaka, z, ad, vektor=False):
    """Varsa alani okur, yoksa None doner (SA'da k ve omega yoktur)."""
    if not os.path.exists(os.path.join(vaka, z, ad)):
        return None
    return Alan(vaka, z, ad, vektor=vektor)


def profil(vaka, x_hedef=0.5, ust=True, n=60, zaman=None):
    """ust=None: yuzey ayrimi yapilmaz (duz levha gibi tek yuzeyli vaka)."""
    """Verilen x/c'ye en yakin duvar yuzunden disariya profil.

    Doner: (u_tau, nu, [nokta, ...]) -- her nokta bir sozluk:
        y, u_t  ve varsa  k, omega, nut
    """
    ag = Ag(vaka)
    z = zaman or son_zaman(vaka)
    nu = nu_oku(vaka)
    U = Alan(vaka, z, "U", vektor=True)
    nut = _alan(vaka, z, "nut")
    k_a = _alan(vaka, z, "k")
    om_a = _alan(vaka, z, "omega")
    merkez = ag.hucre_merkez()
    y = ag.yama["duvar"]

    # hedefe en yakin duvar yuzu
    en, ed = None, 1e18
    for k in range(y["n"]):
        fi = y["bas"] + k
        S, C = ag.yuz_alan(fi)
        if ust is not None and (C[1] > 0) != ust:
            continue
        d = abs(C[0] - x_hedef)
        if d < ed:
            ed, en = d, (fi, k, S, C)
    if en is None:
        raise RuntimeError("duvar yuzu bulunamadi")
    fi, k, S, C = en
    A = math.sqrt(sum(v * v for v in S))
    nrm = [S[a] / A for a in range(3)]

    # duvar kayma gerilmesi (birinci mertebe; u_tau icin yeterli)
    h = ag.sahip[fi]
    cm = merkez[h]
    d1 = abs(sum((cm[a] - C[a]) * nrm[a] for a in range(3)))
    u1 = U.ic[h]
    un = sum(u1[a] * nrm[a] for a in range(3))
    t1 = [u1[a] - un * nrm[a] for a in range(3)]
    ut1 = math.sqrt(sum(v * v for v in t1))
    nw = 0.0
    if nut is not None:
        v = nut.yama_degeri("duvar", k)
        nw = v if v is not None else 0.0
    tau = (nu + nw) * ut1 / d1
    u_tau = math.sqrt(abs(tau))
    teget = [v / ut1 for v in t1] if ut1 else [1.0, 0.0, 0.0]

    # disariya yuru
    nokta, hucre, onceki = [], h, fi
    for _ in range(n):
        cm = merkez[hucre]
        yy = abs(sum((cm[a] - C[a]) * nrm[a] for a in range(3)))
        uu = U.ic[hucre]
        d = dict(y=yy, u_t=sum(uu[a] * teget[a] for a in range(3)))
        for ad, alan in (("nut", nut), ("k", k_a), ("omega", om_a)):
            if alan is not None:
                d[ad] = alan.ic[hucre]
        nokta.append(d)
        h2 = ag.karsi_hucre(onceki, hucre)
        if h2 is None:
            break
        # bir sonraki adim icin: hucreler arasi yuzu bul
        yeni = None
        for g in ag.hucre_yuzleri()[hucre]:
            if g < len(ag.komsu) and (
                    (ag.sahip[g] == hucre and ag.komsu[g] == h2) or
                    (ag.komsu[g] == hucre and ag.sahip[g] == h2)):
                yeni = g
                break
        if yeni is None:
            break
        onceki, hucre = yeni, h2
    return u_tau, nu, nokta


def yaz(vaka, ad, x_hedef=0.5):
    u_tau, nu, p = profil(vaka, x_hedef)
    print("  %s   x/c = %.2f   u_tau/U = %.5f   C_f = %.6f"
          % (ad, x_hedef, u_tau, 2 * u_tau ** 2))
    print("      y+        u+      log yasasi   fark")
    for d in p:
        yp = d["y"] * u_tau / nu
        up = d["u_t"] / u_tau
        if 30 <= yp <= 1000:
            log = (1 / KAPPA) * math.log(yp) + B
            print("  %9.2f %9.3f %9.3f    %+.3f" % (yp, up, log, up - log))
    return u_tau, nu, p


def log_denge(vaka, ad, x_hedef=0.5):
    """Log tabakasinda k-omega denge bagintilarindan sapma.

    Oran 1'e ne kadar yakinsa o denklem o kadar dengededir. Sapan
    baginti, kusurun hangi denklemde oldugunu gosterir.
    """
    u_tau, nu, p = profil(vaka, x_hedef)
    if "k" not in p[0]:
        print("  %s: k/omega alani yok (SA) -- yalnizca nu_t sinanir" % ad)
    print("  %s   u_tau/U = %.5f" % (ad, u_tau))
    print("      y+     nu_t/(k.u.y)   k+/3.333   omega/omega_denge")
    kd = 1.0 / math.sqrt(BETA_YILDIZ)              # k+ denge degeri = 3.3333
    for d in p:
        yp = d["y"] * u_tau / nu
        if not 30 <= yp <= 1000:
            continue
        s = ["%9.2f" % yp]
        s.append("%12.3f" % (d["nut"] / (KAPPA * u_tau * d["y"]))
                 if "nut" in d else "%12s" % "-")
        s.append("%11.3f" % ((d["k"] / u_tau ** 2) / kd)
                 if "k" in d else "%11s" % "-")
        if "omega" in d:
            od = u_tau / (math.sqrt(BETA_YILDIZ) * KAPPA * d["y"])
            s.append("%17.3f" % (d["omega"] / od))
        else:
            s.append("%17s" % "-")
        print("  " + "".join(s))
    return u_tau, p


if __name__ == "__main__":
    arg = sys.argv[1:]
    denge = "-denge" in arg
    arg = [a for a in arg if a != "-denge"]
    x = 0.5
    if arg and arg[-1].replace(".", "").isdigit():
        x = float(arg[-1])
        arg = arg[:-1]
    for v in arg:
        (log_denge if denge else yaz)(v, os.path.basename(v), x)
        print()
