# -*- coding: utf-8 -*-
"""Cozulmus bir vakadan kaldirma/surukleme katsayilarini ve y+ dagilimini
hesaplar.

Neden OpenFOAM'in forceCoeffs'i kullanilmiyor: bu makinedeki 1912 paketinde
hicbir fonksiyon nesnesi calismiyor (bkz. foamoku.py). Hesap burada, acikca
yapiliyor.

Basinc kuvveti
    OpenFOAM'da bir duvar yamasinin Sf alan vektoru akis alanindan DISARI,
    yani govdenin icine bakar: Sf = -n A, n govdeden akisa bakan normal.
    Govdeye etkiyen basinc kuvveti  integral(-p n) dA = integral(p Sf).
    Sikistirilamaz cozucude p kinematiktir (p/rho); rho = 1 alindigi icin
    donen deger dogrudan kuvvettir.

Viskoz kuvvet
    Sinir tabakasi cozumlendigi (y+ ~ 1) ve ag duvarda dik oldugu icin
    duvar kayma gerilmesi, cozucunun kendi kullandigi yaklasimla ayni:
        tau_w = rho * nu_eff * |U_t| / d
    U_t duvara komsu hucre merkezindeki tegetsel hiz, d o merkezin duvara
    dik uzakligi. Kuvvetin yonu U_t yonudur: akiskan govdeyi kendi akis
    yonunde suruklar.

y+
    y+ = d * u_tau / nu ,  u_tau = sqrt(tau_w / rho)
    Cozumun y+ ~ 1 varsayimini gercekten sagladigini SONRADAN denetler --
    varsayim degil olcum olur.
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from foamoku import Ag, Alan, son_zaman, _govde   # noqa: E402
import re                                          # noqa: E402


def nu_oku(vaka):
    m = _govde(os.path.join(vaka, "constant", "transportProperties"))
    return float(re.search(r"nu\s+([-+0-9.eE]+)", m).group(1))


def hesapla(vaka, yama="duvar", alfa=0.0, Uinf=1.0, Aref=1.0, zaman=None,
            mertebe=1):
    """mertebe=1  duvar gradyani tek hucreden: dU/dn = U_t1 / d1
       mertebe=2  ilk IKI hucreden, duvarda sifir sartiyla parabol:
                  U_t(d) = a d + b d^2  ->  dU/dn = a

    Neden onemli: birinci mertebe kestirim, viskoz alt tabakadaki hafif
    bukumu gormez ve gradyani EKSIK verir; hata d ile orantilidir. Ag
    inceldikce bu hata kuculdugu icin, viskoz suruklemede ag yakinsamasi
    gibi gorunen bir egilim aslinda KESTIRIMIN yakinsamasi olabilir.
    Ikinci mertebe bunu ayirt eder.
    """
    ag = Ag(vaka)
    z = zaman or son_zaman(vaka)
    nu = nu_oku(vaka)
    p = Alan(vaka, z, "p")
    U = Alan(vaka, z, "U", vektor=True)
    nut = Alan(vaka, z, "nut") if os.path.exists(
        os.path.join(vaka, z, "nut")) else None
    merkez = ag.hucre_merkez()

    y = ag.yama[yama]
    Fp = [0.0, 0.0, 0.0]
    Fv = [0.0, 0.0, 0.0]
    yp = []

    for k in range(y["n"]):
        fi = y["bas"] + k
        S, C = ag.yuz_alan(fi)
        A = math.sqrt(S[0] ** 2 + S[1] ** 2 + S[2] ** 2)
        if A <= 0:
            continue
        nx, ny, nz = S[0] / A, S[1] / A, S[2] / A     # akistan govdeye

        pf = p.yama_degeri(yama, k)
        if pf is None:
            pf = p.ic[ag.sahip[fi]]
        for a in range(3):
            Fp[a] += pf * S[a]

        # duvara komsu hucre
        h = ag.sahip[fi]
        cm = merkez[h]
        dx, dy, dz = cm[0] - C[0], cm[1] - C[1], cm[2] - C[2]
        d = abs(dx * nx + dy * ny + dz * nz)          # dik uzaklik
        if d <= 0:
            continue
        u = U.ic[h]
        un = u[0] * nx + u[1] * ny + u[2] * nz
        tx, ty, tz = u[0] - un * nx, u[1] - un * ny, u[2] - un * nz
        ut = math.sqrt(tx * tx + ty * ty + tz * tz)

        nut_w = 0.0
        if nut is not None:
            v = nut.yama_degeri(yama, k)
            if v is not None:
                nut_w = v
        nueff = nu + nut_w

        egim = ut / d                                  # birinci mertebe
        if mertebe >= 2 and ut > 0:
            h2 = ag.karsi_hucre(fi, h)
            if h2 is not None:
                cm2 = merkez[h2]
                d2 = abs((cm2[0] - C[0]) * nx + (cm2[1] - C[1]) * ny
                         + (cm2[2] - C[2]) * nz)
                u2 = U.ic[h2]
                # AYNI teget yonune izdusum; yoksa isaret kayar
                ut2 = (u2[0] * tx + u2[1] * ty + u2[2] * tz) / ut
                payda = d * d2 * (d2 - d)
                if abs(payda) > 0:
                    e2 = (ut * d2 ** 2 - ut2 * d ** 2) / payda
                    # Ayrilmis ya da ters akista ut2 negatif olabilir ve
                    # parabol uydurmasi anlamsiz bir egim verir. Ikinci
                    # mertebe yalnizca birinci mertebeden MAKUL bir bantta
                    # kaldiginda kullanilir; disina cikarsa birinci mertebe
                    # korunur. Bu, duzgun akista hicbir sey degistirmez
                    # (fark y+ < 1'de binde birler mertebesinde) ama
                    # ayrilma bolgesinde sacma deger uretilmesini onler.
                    if 0.5 * egim <= e2 <= 2.0 * egim:
                        egim = e2
        tau = nueff * egim
        if ut > 0:
            for a, t in zip(range(3), (tx, ty, tz)):
                Fv[a] += tau * A * t / ut
        # y+ icin MUTLAK deger: ayrilma bolgesinde tau isaret
        # degistirir, u_tau ise buyukluktur.
        yp.append(d * math.sqrt(abs(tau)) / nu)

    a = math.radians(alfa)
    sur = (math.cos(a), math.sin(a), 0.0)
    kal = (-math.sin(a), math.cos(a), 0.0)
    F = [Fp[i] + Fv[i] for i in range(3)]
    q = 0.5 * Uinf ** 2 * Aref

    def bilesen(V, yon):
        return sum(V[i] * yon[i] for i in range(3)) / q

    return dict(
        zaman=z,
        CL=bilesen(F, kal), CD=bilesen(F, sur),
        CD_basinc=bilesen(Fp, sur), CD_viskoz=bilesen(Fv, sur),
        CL_basinc=bilesen(Fp, kal), CL_viskoz=bilesen(Fv, kal),
        yplus_ort=sum(yp) / len(yp) if yp else 0.0,
        yplus_max=max(yp) if yp else 0.0,
        yuz=len(yp))


if __name__ == "__main__":
    vaka = sys.argv[1]
    alfa = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
    r = hesapla(vaka, alfa=alfa)
    print("zaman %s   yuz %d" % (r["zaman"], r["yuz"]))
    print("  C_L = %+.5f   (basinc %+.5f  viskoz %+.5f)"
          % (r["CL"], r["CL_basinc"], r["CL_viskoz"]))
    print("  C_D = %+.6f   (basinc %+.6f  viskoz %+.6f)"
          % (r["CD"], r["CD_basinc"], r["CD_viskoz"]))
    print("  y+  : ortalama %.2f   en fazla %.2f"
          % (r["yplus_ort"], r["yplus_max"]))
