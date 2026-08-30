# -*- coding: utf-8 -*-
"""Sifir basinc gradyanli duz levha -- kurulumun MODEL sinamasi.

NEDEN BU VAKA. NACA 0012 profilinde olculdu ki bizim k-omega SST
kurulumumuzun logaritmik tabakasinda

    nu_t / (kappa u_tau y) = 0.88     (SA ayni akista 0.98)

ve bu oran ag inceltmesiyle DEGISMIYOR (B2 0.880, B3 0.880, B4 0.882),
yani sayisal degil. Ama bu tek basina bir kusur KANITI DEGILDIR: x/c=0,5
noktasinda basinc gradyani ters yonludur ve SST tam da ters gradyanda
nu_t'yi bilerek kisar (a1 sinirlayicisi). Yani 0,88 modelin dogru
davranisi da olabilir.

Iki olasiligi ayirmanin yolu, basinc gradyaninin SIFIR oldugu bir akista
ayni olcumu yapmaktir. Denge halindeki logaritmik tabakada SST'nin kendi
sabitleri su ucunu ZORUNLU kilar -- disaridan olcum gerekmez, model
kapanisinin kendi tanimidir:

    nu_t   = kappa u_tau y
    k      = u_tau^2 / sqrt(beta*)          beta* = 0.09  ->  k+ = 3.333
    omega  = u_tau / (sqrt(beta*) kappa y)

BEKLENTI ONCEDEN:
  (a) Duz levhada oran ~1,00 cikarsa, kurulumumuz dogrudur ve profildeki
      0,88 ters gradyanin fizigidir. O zaman referans kodlarla aramizdaki
      %5, sinir tabakasi yapisinda DEGIL, baska bir yerde aranmalidir.
  (b) Duz levhada da ~0,88 cikarsa, kusur kurulumun kendisindedir --
      basinc gradyanindan bagimsizdir -- ve sinir kosullarinda ya da
      OpenFOAM'in kOmegaSST uygulamasindadir.

Ag duz oldugu icin burada blockMesh yeterlidir: dik acililik tamdir.
(Profilde blockMesh'ten kacinmanin nedeni egri duvarda dikligin
bozulmasiydi; duz levhada boyle bir sorun yok.)

Ayni vaka SA ile de kosulur. SA'nin karisim uzunlugu dogrudan kappa u_tau y
uzerine kuruludur, yani SA'nin ~1,00 vermesi olcumun kendisinin dogru
oldugunu gosteren ic denetimdir.
"""
import math, os, subprocess, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kilit import Kilit                                  # noqa: E402

KOK = "/tmp/levha"
U0, NU = 1.0, 2e-7            # Re_x = 5e6  (x = 1 m)
X0, X1, H = -0.33, 2.0, 1.0   # simetri girisi, levha sonu, alan yuksekligi
NY, NX0, NX1 = 128, 32, 240
Y1 = 4e-6                     # ilk hucre yuksekligi  ->  y+ ~ 0.7

BAS = ("FoamFile\n{\n    version 2.0;\n    format ascii;\n"
       "    class %s;\n    object %s;\n}\n\n")


def _y(yol, sinif, nesne, govde):
    open(yol, "w").write(BAS % (sinif, nesne) + govde)


def _oran(y1, H, n):
    """y1 ilk hucre, H toplam, n hucre iken hucreler arasi buyume orani.

    y1 (r^n - 1)/(r - 1) = H  denklemi ikiye bolerek cozulur.
    """
    alt, ust = 1.0 + 1e-9, 2.0
    for _ in range(200):
        r = 0.5 * (alt + ust)
        if y1 * (r ** n - 1.0) / (r - 1.0) < H:
            alt = r
        else:
            ust = r
    return 0.5 * (alt + ust)


def ag(dizin):
    r = _oran(Y1, H, NY)
    yg = r ** (NY - 1)                       # son hucre / ilk hucre
    v = []
    for z in (-0.05, 0.05):
        for x, yy in ((X0, 0), (0, 0), (X1, 0), (X1, H), (0, H), (X0, H)):
            v.append((x, yy, z))
    _y(os.path.join(dizin, "system", "blockMeshDict"), "dictionary",
       "blockMeshDict",
       "scale 1;\n\nvertices\n(\n" +
       "".join("    (%g %g %g)\n" % p for p in v) +
       ");\n\nblocks\n(\n"
       "    hex (0 1 4 5 6 7 10 11) (%d %d 1) simpleGrading (0.1 %g 1)\n"
       "    hex (1 2 3 4 7 8 9 10) (%d %d 1) simpleGrading (400 %g 1)\n"
       ");\n\nedges ();\n\n"
       "boundary\n(\n"
       "    girisi   { type patch; faces ( (0 6 11 5) ); }\n"
       "    cikis    { type patch; faces ( (2 3 9 8) ); }\n"
       "    simetri  { type symmetryPlane; faces ( (0 1 7 6) ); }\n"
       "    duvar    { type wall; faces ( (1 2 8 7) ); }\n"
       "    ust      { type patch; faces ( (5 11 10 4) (4 10 9 3) ); }\n"
       "    on       { type empty; faces ( (0 5 4 1) (1 4 3 2) ); }\n"
       "    arka     { type empty; faces ( (6 7 10 11) (7 8 9 10) ); }\n"
       ");\n\nmergePatchPairs ();\n" % (NX0, NY, yg, NX1, NY, yg))
    return r


def alanlar(dizin, model):
    # Serbest akis: mu_t/mu = 1. serbest.py'de bu degerin 1000 kat
    # araliginda sonucu %0,003 degistirdigi olculdu.
    om = U0 / (0.1 * H) * 10.0
    k0 = NU * om
    sst = model == "kOmegaSST"

    def yaz(ad, sinif, boyut, ic, duvar, giris_tip="fixedValue"):
        _y(os.path.join(dizin, "0", ad), sinif, ad,
           "dimensions      %s;\n\ninternalField   uniform %s;\n\n"
           "boundaryField\n{\n"
           "    girisi   { type %s; value uniform %s; }\n"
           "    cikis    { type zeroGradient; }\n"
           "    ust      { type slip; }\n"
           "    simetri  { type symmetryPlane; }\n"
           "    duvar\n    {\n%s    }\n"
           "    \"(on|arka)\" { type empty; }\n}\n"
           % (boyut, ic, giris_tip, ic, duvar))

    yaz("U", "volVectorField", "[0 1 -1 0 0 0 0]", "(%g 0 0)" % U0,
        "        type            noSlip;\n")
    _y(os.path.join(dizin, "0", "p"), "volScalarField", "p",
       "dimensions      [0 2 -2 0 0 0 0];\n\ninternalField   uniform 0;\n\n"
       "boundaryField\n{\n"
       "    girisi   { type zeroGradient; }\n"
       "    cikis    { type fixedValue; value uniform 0; }\n"
       "    ust      { type slip; }\n"
       "    simetri  { type symmetryPlane; }\n"
       "    duvar    { type zeroGradient; }\n"
       "    \"(on|arka)\" { type empty; }\n}\n")
    if sst:
        yaz("k", "volScalarField", "[0 2 -2 0 0 0 0]", "%g" % k0,
            "        type            fixedValue;\n"
            "        value           uniform 1e-14;\n")
        yaz("omega", "volScalarField", "[0 0 -1 0 0 0 0]", "%g" % om,
            "        type            omegaWallFunction;\n"
            "        blended         true;\n"
            "        value           uniform %g;\n" % om)
    else:
        yaz("nuTilda", "volScalarField", "[0 2 -1 0 0 0 0]", "%g" % (3 * NU),
            "        type            fixedValue;\n"
            "        value           uniform 0;\n")
    yaz("nut", "volScalarField", "[0 2 -1 0 0 0 0]", "%g" % NU,
        "        type            nutLowReWallFunction;\n"
        "        value           uniform 0;\n", giris_tip="calculated")


def sistem(dizin, model, adim):
    _y(os.path.join(dizin, "constant", "transportProperties"), "dictionary",
       "transportProperties",
       "transportModel  Newtonian;\nnu              [0 2 -1 0 0 0 0] %g;\n" % NU)
    _y(os.path.join(dizin, "constant", "turbulenceProperties"), "dictionary",
       "turbulenceProperties",
       "simulationType  RAS;\n\nRAS\n{\n    RASModel        %s;\n"
       "    turbulence      on;\n    printCoeffs     on;\n}\n" % model)
    _y(os.path.join(dizin, "system", "controlDict"), "dictionary", "controlDict",
       "application     simpleFoam;\nstartFrom       startTime;\n"
       "startTime       0;\nstopAt          endTime;\nendTime         %d;\n"
       "deltaT          1;\nwriteControl    timeStep;\nwriteInterval   %d;\n"
       "purgeWrite      2;\nwriteFormat     ascii;\nwritePrecision  10;\n"
       "writeCompression off;\ntimeFormat      general;\ntimePrecision   6;\n"
       "runTimeModifiable false;\n" % (adim, adim))
    _y(os.path.join(dizin, "system", "fvSchemes"), "dictionary", "fvSchemes",
       "ddtSchemes      { default steadyState; }\n\n"
       "gradSchemes\n{\n    default         Gauss linear;\n"
       "    limited         cellLimited Gauss linear 1;\n"
       "    grad(U)         $limited;\n    grad(k)         $limited;\n"
       "    grad(omega)     $limited;\n}\n\n"
       "divSchemes\n{\n    default         none;\n"
       "    div(phi,U)      bounded Gauss linearUpwind limited;\n"
       "    div(phi,k)      bounded Gauss limitedLinear 1;\n"
       "    div(phi,omega)  bounded Gauss limitedLinear 1;\n"
       "    div(phi,nuTilda) bounded Gauss limitedLinear 1;\n"
       "    div((nuEff*dev2(T(grad(U))))) Gauss linear;\n}\n\n"
       "laplacianSchemes { default Gauss linear corrected; }\n"
       "interpolationSchemes { default linear; }\n"
       "snGradSchemes   { default corrected; }\n"
       "wallDist        { method meshWave; }\n")
    _y(os.path.join(dizin, "system", "fvSolution"), "dictionary", "fvSolution",
       "solvers\n{\n"
       "    p\n    {\n        solver GAMG;\n        smoother GaussSeidel;\n"
       "        tolerance 1e-9;\n        relTol 0.01;\n    }\n"
       "    \"(U|k|omega|nuTilda)\"\n    {\n        solver smoothSolver;\n"
       "        smoother symGaussSeidel;\n        tolerance 1e-10;\n"
       "        nSweeps 2;\n        relTol 0.01;\n    }\n}\n\n"
       "SIMPLE\n{\n    nNonOrthogonalCorrectors 0;\n    consistent yes;\n"
       "    residualControl\n    {\n        p 1e-7;\n        U 1e-8;\n"
       "        \"(k|omega|nuTilda)\" 1e-8;\n    }\n}\n\n"
       "relaxationFactors\n{\n    equations\n    {\n        U 0.9;\n"
       "        \"(k|omega|nuTilda)\" 0.7;\n    }\n}\n")
    _y(os.path.join(dizin, "system", "decomposeParDict"), "dictionary",
       "decomposeParDict",
       "numberOfSubdomains 4;\nmethod hierarchical;\n\n"
       "coeffs\n{\n    n (4 1 1);\n    order xyz;\n}\n")


def kur(dizin, model, adim=4000):
    for d in ("0", "system", "constant"):
        os.makedirs(os.path.join(dizin, d), exist_ok=True)
    r = ag(dizin)
    alanlar(dizin, model)
    sistem(dizin, model, adim)
    return r


KOS = (". /usr/share/openfoam/etc/bashrc >/dev/null 2>&1; cd %s && "
       "blockMesh > blockMesh.log 2>&1 && "
       "decomposePar -force > decompose.log 2>&1 && "
       "mpirun --allow-run-as-root -np 4 simpleFoam -parallel > coz.log 2>&1 && "
       "reconstructPar -latestTime > recon.log 2>&1")

if __name__ == "__main__":
    with Kilit(KOK):
        for model in ("SpalartAllmaras", "kOmegaSST"):
            vaka = os.path.join(KOK, model)
            r = kur(vaka, model)
            print("[%s] ag %dx%d, buyume orani %.4f -- cozuluyor"
                  % (model, NX0 + NX1, NY, r), flush=True)
            s = subprocess.run(["bash", "-c", KOS % vaka])
            if s.returncode != 0:
                print("   KOSULAMADI (%d); coz.log sonu:" % s.returncode)
                print(subprocess.run(["tail", "-15",
                                      os.path.join(vaka, "coz.log")],
                                     capture_output=True, text=True).stdout)
                continue
            print("   cozuldu", flush=True)
