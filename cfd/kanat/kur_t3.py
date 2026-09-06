# -*- coding: utf-8 -*-
"""T3 serisinin bir vakasini OpenFOAM T3A egitim vakasindan turetir.

Degerler Langtry (2006) doktora tezi, Tablo (Bolum 4) -- HUCUM KENARI
degerleridir. Ayni ag, ayni akiskan (nu = 1.5e-5), yalnizca U, k, omega
ve ReThetat degisir.
"""
import math, os, re, shutil, sys

KAYNAK = "/tmp/ofsrc/openfoam-1912.200626/tutorials/incompressible/simpleFoam/T3A"
NU = 1.5e-5

VAKALAR = {           # ad: (U, Tu%, nut/nu)
    "T3A":  (5.4,  3.3,   12.0),
    "T3B":  (9.4,  6.5,  100.0),
    "T3Am": (19.8, 0.874,  8.72),   # T3A-
    "SK":   (50.1, 0.3,    1.0),    # Schubauer & Klebanoff
}


def re_theta_t(tu):
    """Langtry korelasyonu, lambda_theta = 0."""
    if tu <= 1.3:
        return 1173.51 - 589.428 * tu + 0.2196 / tu ** 2
    return 331.50 * (tu - 0.5658) ** -0.671


def kur(ad, dizin):
    U, tu, nut_orani = VAKALAR[ad]
    k = 1.5 * (tu / 100.0 * U) ** 2
    omega = k / (nut_orani * NU)
    rtt = re_theta_t(tu)

    if os.path.exists(dizin):
        shutil.rmtree(dizin)
    shutil.copytree(KAYNAK, dizin)

    def degistir(dosya, desen, yeni, beklenen=1):
        p = os.path.join(dizin, dosya)
        s = open(p).read()
        n = len(re.findall(desen, s))
        if n != beklenen:
            raise RuntimeError("%s: '%s' %d kez gecti, %d bekleniyordu"
                               % (dosya, desen, n, beklenen))
        open(p, "w").write(re.sub(desen, yeni, s))

    degistir("0/U", r"uniform \(5\.4 0 0\)", "uniform (%.6g 0 0)" % U)
    degistir("0/k", r"uniform 0\.047633", "uniform %.6g" % k)
    degistir("0/omega", r"uniform 264\.63", "uniform %.6g" % omega)
    degistir("0/ReThetat", r"uniform 160\.99", "uniform %.6g" % rtt)
    # functionObject'ler bu kurulumda kirik (OSHA1stream). Cikarilir.
    p = os.path.join(dizin, "system/controlDict")
    s = open(p).read()
    s2 = re.sub(r"functions\n\{.*?\n\}\n", "functions { }\n", s, flags=re.S)
    if s2 == s:
        raise RuntimeError("controlDict icinde functions blogu bulunamadi")
    open(p, "w").write(s2)

    return dict(vaka=ad, U=U, Tu=tu, nut_orani=nut_orani, k=k,
                omega=omega, ReThetat=rtt, Re_x_max=U * 1.5 / NU)


if __name__ == "__main__":
    ad = sys.argv[1]
    b = kur(ad, sys.argv[2] if len(sys.argv) > 2 else "/tmp/t3_" + ad)
    for anahtar in ("vaka", "U", "Tu", "nut_orani", "k", "omega",
                    "ReThetat", "Re_x_max"):
        print("  %-10s %.6g" % (anahtar, b[anahtar])
              if anahtar != "vaka" else "  %-10s %s" % (anahtar, b[anahtar]))
