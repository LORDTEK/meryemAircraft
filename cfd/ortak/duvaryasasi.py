# -*- coding: utf-8 -*-
"""Sinir tabakasi profilini duvar degiskenlerinde cikarir: u+ , y+.

Neden: SST kurulumumuzun C_D'si referans kodlarin %5 altinda. Sebep
arayisinda serbest akis elendi. Bu sinama DISARIDAN HICBIR VERI
GEREKTIRMEZ, cunku referansi fizigin kendisidir:

    viskoz alt tabaka   u+ = y+
    logaritmik tabaka   u+ = (1/kappa) ln y+ + B ,  kappa ~ 0.41 , B ~ 5.0

Log tabakasi YUKARI kaymissa (ayni y+'ta u+ daha buyukse) bu, u_tau'nun
kucuk oldugu anlamina gelir -- ve C_f = 2 (u_tau/U)^2 oldugu icin dogrudan
dusuk surtunme demektir. Yani kayma varsa, dusuk C_D'nin nedeni sinir
tabakasinin yapisindadir, kuvvet integralinde ya da agda degil.

Profil, duvardan disariya hucre hucre yurunerek cikarilir (Ag.karsi_hucre).
Yapisal C-agi oldugu icin bu yurume duvara dik dogrultuyu izler.
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from foamoku import Ag, Alan, son_zaman        # noqa: E402
from kuvvet import nu_oku                      # noqa: E402

KAPPA, B = 0.41, 5.0


def profil(vaka, x_hedef=0.5, ust=True, n=60, zaman=None):
    """Verilen x/c'ye en yakin duvar yuzunden disariya profil.

    Doner: (u_tau, nu, [(y, u_t), ...])
    """
    ag = Ag(vaka)
    z = zaman or son_zaman(vaka)
    nu = nu_oku(vaka)
    U = Alan(vaka, z, "U", vektor=True)
    nut = Alan(vaka, z, "nut") if os.path.exists(
        os.path.join(vaka, z, "nut")) else None
    merkez = ag.hucre_merkez()
    y = ag.yama["duvar"]

    # hedefe en yakin duvar yuzu
    en, ed = None, 1e18
    for k in range(y["n"]):
        fi = y["bas"] + k
        S, C = ag.yuz_alan(fi)
        if (C[1] > 0) != ust:
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
        ut = sum(uu[a] * teget[a] for a in range(3))
        nokta.append((yy, ut))
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
    for yy, ut in p:
        yp = yy * u_tau / nu
        up = ut / u_tau
        if yp < 0.3 or yp > 3000:
            continue
        log = (1 / KAPPA) * math.log(yp) + B
        if 30 <= yp <= 1000:
            print("  %9.2f %9.3f %9.3f    %+.3f" % (yp, up, log, up - log))
    return u_tau, nu, p


if __name__ == "__main__":
    x = float(sys.argv[-1]) if len(sys.argv) > 2 and \
        sys.argv[-1].replace(".", "").isdigit() else 0.5
    for v in sys.argv[1:]:
        if v.replace(".", "").isdigit():
            continue
        yaz(v, os.path.basename(v), x)
        print()
