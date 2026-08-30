# -*- coding: utf-8 -*-
"""Kusur ayrisim semalarindan mi geliyor? -- duz levhada sema taramasi.

DURUM. Duz levhada, denge halindeki log tabakasinda modelin kendi
sabitlerinin zorunlu kildigi oran nu_t/(kappa u_tau y) = 1,000. Olculen:

    SpalartAllmaras  0,969      (yani olcum dogru)
    kOmega           0,881
    kOmegaSST        0,859

Eleme durumu: serbest akis, ag, duvar omega kosulu (iki onlu) ve a1
sinirlayicisi elendi. Duz kOmega'da F1 harmanlamasi ve capraz yayilim
YOKTUR, yine de 0,88 veriyor -- yani kusur SST'ye ozgu makinede degil,
omega ailesinde ortak.

Omega ailesi ile SA arasinda kurulumumuzda GERCEK bir asimetri var ve bu
bizim kendi secimimiz:

    grad(U)        cellLimited Gauss linear 1
    grad(k)        cellLimited Gauss linear 1
    grad(omega)    cellLimited Gauss linear 1
    grad(nuTilda)  -- listede YOK, default'a dusuyor: Gauss linear

Yani SA'nin turbulans degiskeninin gradyani SINIRLANDIRILMAMIS, iki
omega modelininki sinirlandirilmis. omega duvar yakininda y^-2 gibi
davranir; gerilmis agda hucre sinirlayicisi orada isirabilir.

BEKLENTI ONCEDEN:
  (a) Bir varyant orani ~1,00'e tasirsa kusur BIZIM sema secimimizdir.
      Bu durumda duzeltilir ve duzeltilmesi mesrudur: sema bir ayrisim
      secimidir, uydurulmus bir model sabiti degil. Butun NACA
      sonuclari duzeltilmis semayla YENIDEN kosulur.
  (b) Hicbiri tasimazsa sema da elenir. O zaman geriye OpenFOAM'in omega
      denklemi uygulamasi kalir; kaynagindan okunmadan duzeltilemez,
      RAPOR EDILIR.
"""
import json, os, subprocess, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
import duzlevha                                          # noqa: E402
from duzlevha import KOS                                 # noqa: E402
from omega_duvar import olc                              # noqa: E402
from kilit import Kilit                                  # noqa: E402

KOK = "/tmp/levha_sema"

SINIRLI = "cellLimited Gauss linear 1"

VARYANT = [
    ("taban", []),
    # turbulans degiskenlerinin gradyani sinirsiz (SA ile ayni muamele)
    ("turb_grad_serbest", [("    grad(k)         $limited;\n"
                            "    grad(omega)     $limited;\n", "")]),
    # hiz gradyani sinirsiz (uretim terimi buradan besleniyor)
    ("U_grad_serbest", [("    grad(U)         $limited;\n", "")]),
    # butun gradyanlar sinirsiz
    ("grad_serbest", [("    limited         %s;\n" % SINIRLI, ""),
                      ("    grad(U)         $limited;\n", ""),
                      ("    grad(k)         $limited;\n", ""),
                      ("    grad(omega)     $limited;\n", "")]),
    # k ve omega tasinimi sinirsiz merkezi
    ("tas_merkezi", [("    div(phi,k)      bounded Gauss limitedLinear 1;\n",
                      "    div(phi,k)      bounded Gauss linear;\n"),
                     ("    div(phi,omega)  bounded Gauss limitedLinear 1;\n",
                      "    div(phi,omega)  bounded Gauss linear;\n")]),
]


def duzenle(vaka, degisim):
    p = os.path.join(vaka, "system", "fvSchemes")
    s = open(p).read()
    for eski, yeni in degisim:
        if eski not in s:
            raise RuntimeError("fvSchemes'te bulunamadi: %r" % eski)
        s = s.replace(eski, yeni, 1)
    open(p, "w").write(s)


if __name__ == "__main__":
    with Kilit(KOK):
        yol = os.path.join(KOK, "sonuc.json")
        cikti = json.load(open(yol)) if os.path.exists(yol) else []
        yapilan = {d["ad"] for d in cikti}
        for ad, deg in VARYANT:
            if ad in yapilan:
                continue
            vaka = os.path.join(KOK, ad)
            duzlevha.kur(vaka, "kOmegaSST")
            duzenle(vaka, deg)
            print("[%s] cozuluyor" % ad, flush=True)
            r = subprocess.run(["bash", "-c", KOS % vaka])
            if r.returncode != 0:
                print("   KOSULAMADI (%d)" % r.returncode, flush=True)
                cikti.append(dict(ad=ad, hata=r.returncode))
            else:
                d = olc(vaka)
                print("   C_f=%.6f  nu_t/(k.u.y)=%.3f @y+%.0f  k+/3,333=%.3f"
                      "  omega/denge=%.3f"
                      % (d["Cf"], d["oran"], d["yp"], d["kp"], d["om"]),
                      flush=True)
                cikti.append(dict(ad=ad, **d))
            json.dump(cikti, open(yol, "w"), indent=1)

        print()
        print("  varyant              C_f     nu_t/(k.u.y)  k+/3,333  omega/denge")
        for d in cikti:
            if "oran" not in d:
                print("  %-18s (kosulamadi)" % d["ad"])
            else:
                print("  %-18s %.6f    %.3f       %.3f     %.3f"
                      % (d["ad"], d["Cf"], d["oran"], d["kp"], d["om"]))
        print("  HEDEF 1,000 -- modelin kendi kapanis sarti.")
        print("  Ayni vakada SA 0,969, kOmega 0,881 veriyor.")
