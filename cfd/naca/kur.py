# -*- coding: utf-8 -*-
"""Iki boyutlu profil icin eksiksiz bir simpleFoam vakasi kurar.

Olcekleme: veter = 1 m, U = 1 m/s, rho = 1 alinir; nu = 1/Re. Boylece
forceCoeffs dogrudan C_L ve C_D verir, ayrica bir boyutsuzlastirma adimi
kalmaz.

Hucum acisi AGI DONDURMEZ, serbest akis vektorunu dondurur: boylece butun
acilar TEK bir agda cozulur ve aci taramasindaki farklar agdan degil
akistan gelir.

Turbulans: k-omega SST. Sinir tabakasi cozumlenir (y+ ~ 1), duvar
fonksiyonu kullanilmaz -- surukleme duvar kayma gerilmesinin integrali
oldugu icin bu tercih dogrudan sonucu etkiler ve 'kur' bunu 8.12'nin
istedigi bicimde acik birakir.
"""
import os, math, shutil, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from cagi import CAgi                                   # noqa: E402

BAS = ("FoamFile\n{\n    version 2.0;\n    format ascii;\n"
       "    class %s;\n    object %s;\n}\n\n")


def _y(yol, sinif, nesne, govde):
    with open(yol, "w") as fh:
        fh.write(BAS % (sinif, nesne) + govde)


# ------------------------------------------------------------------ alanlar

def _alan(yol, nesne, boyut, ic, disalan, duvar, cikis):
    _y(yol, "volScalarField" if nesne != "U" else "volVectorField", nesne,
       "dimensions      %s;\n\ninternalField   uniform %s;\n\n"
       "boundaryField\n{\n"
       "    duvar\n    {\n%s    }\n"
       "    disalan\n    {\n%s    }\n"
       "    cikis\n    {\n%s    }\n"
       "    \"(on|arka)\"\n    {\n        type            empty;\n    }\n}\n"
       % (boyut, ic, duvar, disalan, cikis))


def kur(dizin, kod="0012", Re=6e6, alfa=0.0, yplus=1.0,
        n_profil=256, n_normal=96, n_iz=64, R=20.0, Xiz=20.0,
        siddet=0.001, nut_orani=1.0, adim=3000, kapali=True,
        yaz_araligi=None, model="kOmegaSST", gecici=None):
    """Vakayi kurar; ag .msh olarak birakilir, cevrimi kos.sh yapar.

    gecici=None            kararli cozum, simpleFoam
    gecici=(T, dt0, dyaz)  zamana bagli cozum, pimpleFoam: T saniyeye kadar,
                           dt0 baslangic adimi, dyaz saniyede bir yazim.
                           Kalin kesitte akis kararli olmadigi icin (bkz.
                           kalinlik.py) kararli cozucu yakinsamaz; dogru
                           islem budur.
    """
    if os.path.isdir(dizin):
        shutil.rmtree(dizin)
    for a in ("0", "system", "constant"):
        os.makedirs(os.path.join(dizin, a))

    ag = CAgi(kod=kod, Re=Re, yplus=yplus, R=R, Xiz=Xiz,
              n_profil=n_profil, n_normal=n_normal, n_iz=n_iz, kapali=kapali)
    bilgi = ag.yaz(os.path.join(dizin, "ag.msh"))

    U, c, nu = 1.0, 1.0, 1.0 / Re
    a = math.radians(alfa)
    ux, uy = math.cos(a), math.sin(a)
    # serbest akista turbulans: dusuk turbulanslli basincli tunel varsayimi
    k = 1.5 * (siddet * U) ** 2
    omega = k / (nut_orani * nu)

    # --- 0/
    _alan(os.path.join(dizin, "0", "U"), "U", "[0 1 -1 0 0 0 0]",
          "(%.10g %.10g 0)" % (ux, uy),
          "        type            freestreamVelocity;\n"
          "        freestreamValue uniform (%.10g %.10g 0);\n" % (ux, uy),
          "        type            noSlip;\n",
          "        type            zeroGradient;\n")
    _alan(os.path.join(dizin, "0", "p"), "p", "[0 2 -2 0 0 0 0]", "0",
          "        type            freestreamPressure;\n"
          "        freestreamValue uniform 0;\n",
          "        type            zeroGradient;\n",
          "        type            fixedValue;\n        value           uniform 0;\n")
    _alan(os.path.join(dizin, "0", "k"), "k", "[0 2 -2 0 0 0 0]", "%.10g" % k,
          "        type            freestream;\n"
          "        freestreamValue uniform %.10g;\n" % k,
          "        type            fixedValue;\n        value           uniform 1e-14;\n",
          "        type            zeroGradient;\n")
    _alan(os.path.join(dizin, "0", "omega"), "omega", "[0 0 -1 0 0 0 0]",
          "%.10g" % omega,
          "        type            freestream;\n"
          "        freestreamValue uniform %.10g;\n" % omega,
          "        type            omegaWallFunction;\n"
          "        blended         true;\n"
          "        value           uniform %.10g;\n" % omega,
          "        type            zeroGradient;\n")
    if model == "SpalartAllmaras":
        # SA'nin tasidigi degisken nuTilda'dir. Serbest akis degeri, yerlesik
        # secim olan 3*nu: sinir tabakasi disinda nut'u ihmal edilebilir
        # birakir ama modelin uyanmasina yetecek kadar buyuktur.
        _alan(os.path.join(dizin, "0", "nuTilda"), "nuTilda",
              "[0 2 -1 0 0 0 0]", "%.10g" % (3 * nu),
              "        type            freestream;\n"
              "        freestreamValue uniform %.10g;\n" % (3 * nu),
              "        type            fixedValue;\n"
              "        value           uniform 0;\n",
              "        type            zeroGradient;\n")

    _alan(os.path.join(dizin, "0", "nut"), "nut", "[0 2 -1 0 0 0 0]", "0",
          "        type            freestream;\n"
          "        freestreamValue uniform 0;\n",
          "        type            nutLowReWallFunction;\n"
          "        value           uniform 0;\n",
          "        type            calculated;\n        value           uniform 0;\n")

    # --- constant/
    _y(os.path.join(dizin, "constant", "transportProperties"),
       "dictionary", "transportProperties",
       "transportModel  Newtonian;\nnu              %.12g;\n" % nu)
    _y(os.path.join(dizin, "constant", "turbulenceProperties"),
       "dictionary", "turbulenceProperties",
       "simulationType  RAS;\n\nRAS\n{\n    RASModel        %s;\n"
       "    turbulence      on;\n    printCoeffs     on;\n}\n" % model)

    # --- system/
    if gecici:
        T, dt0, dyaz = gecici
        _y(os.path.join(dizin, "system", "controlDict"), "dictionary",
           "controlDict",
           "application     pimpleFoam;\nstartFrom       startTime;\n"
           "startTime       0;\nstopAt          endTime;\n"
           "endTime         %.10g;\ndeltaT          %.10g;\n"
           "writeControl    adjustableRunTime;\nwriteInterval   %.10g;\n"
           "purgeWrite      0;\nwriteFormat     ascii;\nwritePrecision  10;\n"
           "runTimeModifiable false;\n"
           # ZAMAN ADIMI SABIT. Courant tabanli uyarlama duvar cozumlu
           # bir agda kullanissizdir: olculdu, uyarlanan adim 4,6e-7'ye
           # cokuyor (ortalama Courant 1,2e-6, en fazla 3,69 -- yani sinir
           # tek bir minik hucrenin elinde) ve 0,5 saniyeye ulasmak bir
           # milyon adim alirdi. PIMPLE ortuk oldugu icin buyuk yerel
           # Courant sayilari kararliligi bozmaz; sinir dogruluktur ve o da
           # SALINIM PERIYODUNU cozmekle ilgilidir, tek bir sinir tabakasi
           # hucresini degil. Adim periyoda gore secilir.
           "adjustTimeStep  no;\n"
           % (T, dt0, dyaz))
    else:
        _y(os.path.join(dizin, "system", "controlDict"), "dictionary", "controlDict",
       "application     simpleFoam;\nstartFrom       startTime;\n"
       "startTime       0;\nstopAt          endTime;\nendTime         %d;\n"
       "deltaT          1;\nwriteControl    timeStep;\nwriteInterval   %d;\n"
       "purgeWrite      0;\n"
       "writeFormat     ascii;\nwritePrecision  10;\n"
       "runTimeModifiable false;\n"
       # Fonksiyon nesnesi YOK. Bu makinedeki OpenFOAM 1912
       # paketinde hicbiri calismiyor: forceCoeffs, forces, yPlus,
       # hatta writeObjects, hepsi OSHA1stream uzerinde "error in
       # IOstream sha1" verip cikiyor. Kusur vakada degil kurulumda
       # -- stok bir vakada da ayni. Daha yeni bir surum kurmak da
       # mumkun degil, openfoam depolari kapali. Katsayilar ve y+,
       # cozumden sonra yazilmis alanlardan ortak/kuvvet.py ile
       # hesaplaniyor.
       % (adim, yaz_araligi or adim))


    _y(os.path.join(dizin, "system", "fvSchemes"), "dictionary", "fvSchemes",
       ("ddtSchemes      { default backward; }\n\n" if gecici else
        "ddtSchemes      { default steadyState; }\n\n") +
       
       "gradSchemes\n{\n    default         Gauss linear;\n"
       "    limited         cellLimited Gauss linear 1;\n"
       "    grad(U)         $limited;\n    grad(k)         $limited;\n"
       "    grad(omega)     $limited;\n}\n\n"
       # Momentum ikinci mertebeden olmak ZORUNDA: birinci mertebe upwind'in
       # sayisal yayilimi, olculmek istenen sinir tabakasi suruklemesiyle
       # ayni buyukluk mertebesindedir.
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

    P_COZ = ("        solver          GAMG;\n"
             "        smoother        GaussSeidel;\n"
             "        tolerance       1e-9;\n")
    U_COZ = ("        solver          smoothSolver;\n"
             "        smoother        symGaussSeidel;\n"
             "        tolerance       1e-10;\n"
             "        nSweeps         2;\n")

    cozucu = ("solvers\n{\n"
              "    p\n    {\n" + P_COZ + "        relTol          0.01;\n    }\n"
              "    \"(U|k|omega|nuTilda)\"\n    {\n" + U_COZ +
              "        relTol          0.01;\n    }\n")

    if gecici:
        # Zamana bagli dalda ANA p de PCG+DIC (yukaridaki gerekce).
        cozucu = cozucu.replace(
            "    p\n    {\n" + P_COZ,
            "    p\n    {\n"
            "        solver          PCG;\n"
            "        preconditioner  DIC;\n"
            "        tolerance       1e-9;\n", 1)

        # PIMPLE son dis duzeltmede "Final" cozucu girdilerini arar ve
        # onlarsiz calismaz. Final adimda relTol = 0 verilir: o adim zaman
        # adiminin sonucunu belirledigi icin bagil degil MUTLAK toleransa
        # kadar cozulur.
        # pFinal COZUCUSU DEGISTIRILDI -- olculdu, varsayilmadi.
        #
        # Once GAMG + tolerance 1e-9 + relTol 0 idi. O deger bu agda
        # ERISILEMIYOR: GAMG her cagrisinda 1000 yinelemeye (varsayilan
        # ust sinira) carpip ~3e-8'de birakiyordu. "Mutlak toleransa
        # kadar cozuldu" degil, "1000 yinelemede pes etti" -- ve bu
        # sessizdi, cunku cozucu hata vermez.
        #
        # Nedeni ag: azami en-boy orani 5000 (y+ ~ 1 duvar hucreleri),
        # azami dik-olmayanlik 61 derece. GAMG bu bilesimde tikaniyor.
        # Ilk basinc cozumu (relTol 0,01) 6-36 yinelemede bitiyor;
        # tikanan, dik-olmayanlik duzeltmesindeki pFinal.
        #
        # Uc varyant AYNI baslangictan 80 zaman adimi kosuldu:
        #
        #   GAMG   tol 1e-7   1,765 s/adim   ort 329 yineleme (azami 1000)
        #   GAMG   tol 1e-6   0,368 s/adim   ort  68
        #   PCG+DIC tol 1e-7  0,257 s/adim   ort 183
        #
        # Ucu de AYNI COZUMU verdi: C_D farklari 2e-9 ve 5e-9, yani
        # %0,00001 ve %0,00003. Yedi anlamli basamaga kadar ayni.
        # Dolayisiyla secim maliyetle ilgili, dogrulukla degil.
        #
        # PCG+DIC secildi: en hizlisi VE sikı toleransi koruyor, yani
        # gevsetmeye gerek birakmiyor. Tolerans 1e-7'de tutuldu; 1e-9'a
        # inmek olculebilir bir sey kazandirmiyor (cozum zaten ayni) ama
        # maliyet ekliyor.
        # ... VE ANA p COZUCUSU DE. Ilk duzeltmede yalnizca pFinal
        # degistirilmisti; kiyas t ~ 0,03'te yapilmisti ve ORASI TEMSILI
        # DEGILDI. O anda kalintilar buyuk (ilk kalinti ~2,6e-4) ve
        # GAMG'nin p cozumu 6-36 yinelemede bitiyordu. Akis oturdukca ilk
        # kalinti 9e-6'ya dustu; relTol 0,01 yine iki mertebe indirme
        # istiyor ve GAMG bunu bu agda yapamiyor -- olculdu: 662, 471,
        # 1000 yineleme. Sonuc: adim maliyeti 2,3 s'e cikti, yani
        # duzeltmeden onceki 2,9 s'e geri donmustu.
        #
        # Ders: bir hiz kiyasi, kosunun TEMSILI bir aninda alinmali.
        # Gecici rejimin basi, yakinsamis rejimi temsil etmiyor.
        #
        # Bu degisiklik YALNIZCA zamana bagli dala uygulaniyor. Kararli
        # dal dokunulmadan birakildi: butun dogrulanmis 2-B sonuclari
        # onunla uretildi ve lineer cozucunun yakinsamis cozumu
        # degistirmedigi olculmus olsa da (yedi anlamli basamak),
        # gereksiz yere degistirmiyorum.
        P_SON = ("        solver          PCG;\n"
                 "        preconditioner  DIC;\n"
                 "        tolerance       1e-7;\n")
        cozucu += ("    pFinal\n    {\n" + P_SON +
                   "        relTol          0;\n    }\n"
                   "    \"(U|k|omega|nuTilda)Final\"\n    {\n" + U_COZ +
                   "        relTol          0;\n    }\n")
    cozucu += "}\n\n"

    if gecici:
        # Zamana bagli cozumde denklemler GEVSETILMEZ. Gevsetme, kararli
        # cozumde yakinsamayi hizlandirmak icindir; burada o isi zaman
        # adiminin kendisi gorur ve gevsetme zaman dogrulugunu bozar.
        cozucu += ("PIMPLE\n{\n    nOuterCorrectors 3;\n"
                   "    nCorrectors     1;\n"
                   "    nNonOrthogonalCorrectors 1;\n"
                   "    turbOnFinalIterOnly false;\n}\n\n"
                   "relaxationFactors\n{\n    equations\n    {\n"
                   "        \".*\"            1;\n    }\n}\n")
    else:
        cozucu += ("SIMPLE\n{\n    nNonOrthogonalCorrectors 2;\n"
                   "    consistent      yes;\n"
                   "    residualControl\n    {\n        p               1e-7;\n"
                   "        U               1e-8;\n"
                   "        \"(k|omega|nuTilda)\" 1e-8;\n    }\n}\n\n"
                   "relaxationFactors\n{\n    equations\n    {\n"
                   "        U               0.9;\n"
                   "        \"(k|omega|nuTilda)\" 0.7;\n    }\n}\n")

    _y(os.path.join(dizin, "system", "fvSolution"), "dictionary", "fvSolution",
       cozucu)

    _y(os.path.join(dizin, "system", "decomposeParDict"), "dictionary",
       "decomposeParDict",
       # Ubuntu paketi scotch'u sahte kutuphaneyle geliyor; geometrik
       # ayristirma kullaniliyor. C-agi tek yapisal blok oldugu icin
       # hiyerarsik bolme dengeli cikar.
       "numberOfSubdomains 4;\nmethod          hierarchical;\n\n"
       "coeffs\n{\n    n               (2 2 1);\n    order           xyz;\n}\n")

    bilgi.update(Re=Re, alfa=alfa, nu=nu, k=k, omega=omega, model=model)
    return bilgi
