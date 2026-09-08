# -*- coding: utf-8 -*-
"""Iki cozumun DUVAR BASINCINI karsilastirir.

NEDEN VAR. bl_C ve bl_E ayni agda, ayni modelle, ayni sinir kosullariyla
kosuldu ve ikisi de yakinsadi; ama C_D'leri %4,3 farkli ve farkin tamami
BASINCTA (viskoz bilesen binde uc icinde ayni). Dis denetim hakli olarak
sordu: fark NEREDE?

Bu betik yeni bir kosu yapmaz. Elde duran iki yakinsamis alani okur ve
farkin duvarda nereye dustugunu gosterir:
  1. Acikliga gore basinc suruklemesi dagilimi -- fark hangi istasyonda?
  2. Ters akis (ayrilma) alan kesri -- topoloji farkli mi?
  3. Sectigi istasyonlarda vec boyunca Cp -- fark hucum kenarinda mi,
     firar kenarinda mi?

Cp = 2 p / Uinf^2 ; p kinematik, Uinf = 1  ->  Cp = 2 p.
Basinc kuvveti = toplam(p Sf) (bkz. kuvvet.py'deki isaret gerekcesi).
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from foamoku import Ag, Alan, son_zaman        # noqa: E402


def duvar_kayitlari(vaka, zaman=None, yama="duvar"):
    """Her duvar yuzu icin (merkez, Sf, p, tegetsel hiz) dondurur."""
    ag = Ag(vaka)
    z = zaman or son_zaman(vaka)
    P = Alan(vaka, z, "p")
    U = Alan(vaka, z, "U", vektor=True)
    y = ag.yama[yama]
    kayit = []
    for k in range(y["n"]):
        fi = y["bas"] + k
        S, C = ag.yuz_alan(fi)
        A = math.sqrt(sum(v * v for v in S))
        if A <= 0:
            continue
        h = ag.sahip[fi]
        p = P.yama_degeri(yama, k, P.ic[h])
        n = [S[a] / A for a in range(3)]
        u = U.ic[h]
        un = sum(u[a] * n[a] for a in range(3))
        t = [u[a] - un * n[a] for a in range(3)]
        kayit.append(dict(C=C, S=S, A=A, p=p, ux_t=t[0], n=n))
    return kayit, z


def _acik_ekseni(kayit):
    """Aciklik ekseni: kok simetri duzlemi hangi eksende ise o.
    En genis yayilimli eksen aciklik, akis x."""
    en = None
    for a in (1, 2):
        v = [k["C"][a] for k in kayit]
        d = max(v) - min(v)
        if en is None or d > en[1]:
            en = (a, d)
    return en[0]


def karsilastir(vaka1, vaka2, ad1="1", ad2="2", zaman=None, n_bant=12,
                Aref=0.989612):
    K1, z1 = duvar_kayitlari(vaka1, zaman)
    K2, z2 = duvar_kayitlari(vaka2, zaman)
    ek = _acik_ekseni(K1)
    print("aciklik ekseni: %s   zamanlar: %s / %s" % ("xyz"[ek], z1, z2))
    print("duvar yuzu sayisi: %d / %d" % (len(K1), len(K2)))
    if len(K1) != len(K2):
        print("UYARI: yuz sayilari farkli, ayni ag degil!")
    print()

    # --- 1. acikliga gore basinc suruklemesi ---
    s = [k["C"][ek] for k in K1]
    s0, s1 = min(s), max(s)
    print("1. BASINC SURUKLEMESININ ACIKLIK DAGILIMI  (C_Dp katkisi)")
    print("  %-14s %11s %11s %10s %9s" % ("s/yari", ad1, ad2, "fark", "% pay"))
    top1 = top2 = 0.0
    satir = []
    for b in range(n_bant):
        a0 = s0 + (s1 - s0) * b / n_bant
        a1 = s0 + (s1 - s0) * (b + 1) / n_bant
        f1 = sum(k["p"] * k["S"][0] for k in K1 if a0 <= k["C"][ek] < a1)
        f2 = sum(k["p"] * k["S"][0] for k in K2 if a0 <= k["C"][ek] < a1)
        c1, c2 = f1 / (0.5 * Aref), f2 / (0.5 * Aref)
        top1 += c1; top2 += c2
        satir.append(((a0 - s0) / (s1 - s0), (a1 - s0) / (s1 - s0), c1, c2))
    fark_top = top1 - top2
    for a0, a1, c1, c2 in satir:
        pay = 100 * (c1 - c2) / fark_top if fark_top else 0.0
        print("  %.2f - %.2f   %11.6f %11.6f %10.6f %8.1f%%"
              % (a0, a1, c1, c2, c1 - c2, pay))
    print("  %-14s %11.6f %11.6f %10.6f" % ("TOPLAM", top1, top2, fark_top))
    print()

    # --- 2. ayrilma ---
    print("2. TERS AKIS (ayrilma) -- tegetsel hizin akis yonu bileseni < 0")
    for ad, K in ((ad1, K1), (ad2, K2)):
        Atop = sum(k["A"] for k in K)
        Ater = sum(k["A"] for k in K if k["ux_t"] < 0.0)
        x = [k["C"][0] for k in K if k["ux_t"] < 0.0]
        print("  %-6s ters akis alani %%%.2f" % (ad, 100 * Ater / Atop), end="")
        if x:
            print("   x araligi %.3f .. %.3f m" % (min(x), max(x)))
        else:
            print("   (yok)")
    print()

    # --- 3. istasyonlarda Cp ---
    print("3. SECILI ISTASYONLARDA Cp = 2p  (ust/alt ayri, vec boyunca)")
    for frak in (0.25, 0.46, 0.75):
        sm = s0 + (s1 - s0) * frak
        gen = (s1 - s0) / (2.0 * n_bant)
        d1 = [k for k in K1 if abs(k["C"][ek] - sm) < gen]
        d2 = [k for k in K2 if abs(k["C"][ek] - sm) < gen]
        if not d1:
            continue
        xs = [k["C"][0] for k in d1]
        x0, x1 = min(xs), max(xs)
        print("  s/yari = %.2f   vec %.3f .. %.3f m" % (frak, x0, x1))
        print("    %-8s %10s %10s %10s %10s" %
              ("x/c", ad1 + " ust", ad2 + " ust", ad1 + " alt", ad2 + " alt"))
        for b in range(8):
            a0 = x0 + (x1 - x0) * b / 8.0
            a1 = x0 + (x1 - x0) * (b + 1) / 8.0
            hu = []
            for K in (d1, d2):
                u = [2 * k["p"] for k in K if a0 <= k["C"][0] < a1 and k["n"][1] > 0]
                a = [2 * k["p"] for k in K if a0 <= k["C"][0] < a1 and k["n"][1] < 0]
                hu.append((sum(u) / len(u) if u else float("nan"),
                           sum(a) / len(a) if a else float("nan")))
            print("    %-8.3f %10.4f %10.4f %10.4f %10.4f"
                  % ((a0 - x0) / (x1 - x0), hu[0][0], hu[1][0],
                     hu[0][1], hu[1][1]))
        print()


if __name__ == "__main__":
    karsilastir(sys.argv[1], sys.argv[2],
                ad1=os.path.basename(sys.argv[1].rstrip("/")),
                ad2=os.path.basename(sys.argv[2].rstrip("/")),
                zaman=sys.argv[3] if len(sys.argv) > 3 else None)
