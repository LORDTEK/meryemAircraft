# -*- coding: utf-8 -*-
"""SST'nin serbest akis turbulans degerlerine duyarliligi.

NEDEN: NAS-2016-01 (Jespersen, Pulliam, Childs) sekiz yerlesik kodun ayni
vakadaki degerlerini veriyor. Alfa = 0, Re = 6e6, M = 0.15'te SA ile SST
arasindaki fark yalnizca %0,9 (0,00819 ve 0,00812). Bizde %9,4 cikmisti.
Bizim SA'miz referanslarin ust ucunda ama SST'miz her yerlesik kodun %5
altinda -- yani sorun modelde degil, bizim SST kurulumumuzda.

Ayni raporun 13. sayfasi referans uygulamayi yaziyor: SST icin serbest
akista MUTINF = (mu_t/mu)_inf = 0,001 ve XKINF = 1,5 (FSTI/100)^2. Biz
mu_t/mu = 1,0 kullanmisiz -- BIN KAT buyuk. k dogruydu (%0,1 siddet), ama
omega_inf = k / nu_t oldugu icin bizimki 9, referansinki 9000.

Bu betik o tek degiskeni tarar. Digerleri sabit: ayni ag, ayni semalar,
ayni k, ayni duvar islemi.

BEKLENTI ONCEDEN YAZILIYOR: hipotez dogruysa mu_t/mu kucultuldukce C_D
referans bandina (0,00808 - 0,00821) dogru YUKSELMELIDIR. Yukselmezse
hipotez yanlistir ve sorun baska yerdedir -- o zaman duvar islemine
bakilacaktir.
"""
import json, os, subprocess, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kur import kur                                    # noqa: E402
from kuvvet import hesapla                             # noqa: E402
from kilit import Kilit                                # noqa: E402

ORAN = [1.0, 0.1, 0.01, 0.001]
KOK = "/tmp/serbest"
REFERANS = dict(SST_min=0.00808, SST_max=0.00821, SST_ort=0.00812)

if __name__ == "__main__":
    with Kilit(KOK):
        yol = os.path.join(KOK, "sonuc.json")
        cikti = json.load(open(yol)) if os.path.exists(yol) else []
        yapilan = {d["nut_orani"] for d in cikti}
        for o in ORAN:
            if o in yapilan:
                continue
            vaka = os.path.join(KOK, "n%s" % str(o).replace(".", "_"))
            bilgi = kur(vaka, kod="0012", Re=6e6, alfa=0.0, yplus=1.0,
                        n_profil=256, n_normal=96, n_iz=64, R=20.0, Xiz=20.0,
                        nut_orani=o, adim=3000, yaz_araligi=1500)
            print("[mu_t/mu = %g]  omega_inf = %.4g  -- cozuluyor"
                  % (o, bilgi["omega"]), flush=True)
            subprocess.run([os.path.join(BURA, "kos.sh"), vaka, "4"],
                           check=True, stdout=subprocess.DEVNULL)
            r = hesapla(vaka, alfa=0.0, mertebe=2)
            print("   C_D=%.6f  basinc=%.6f  viskoz=%.6f  y+ %.2f  C_L=%+.1e"
                  % (r["CD"], r["CD_basinc"], r["CD_viskoz"], r["yplus_ort"],
                     r["CL"]), flush=True)
            cikti.append(dict(nut_orani=o, omega=bilgi["omega"], CD=r["CD"],
                              CD_b=r["CD_basinc"], CD_v=r["CD_viskoz"],
                              yp=r["yplus_ort"], CL=r["CL"]))
            json.dump(cikti, open(yol, "w"), indent=1)
        print()
        print("  mu_t/mu   omega_inf      C_D    referansa gore")
        for d in sorted(cikti, key=lambda x: -x["nut_orani"]):
            print("   %7g  %9.4g  %.6f   %+.1f%%"
                  % (d["nut_orani"], d["omega"], d["CD"],
                     (d["CD"] / REFERANS["SST_ort"] - 1) * 100))
        print("  referans SST bandi: %.5f - %.5f (NAS-2016-01, Tablo 7.2)"
              % (REFERANS["SST_min"], REFERANS["SST_max"]))
