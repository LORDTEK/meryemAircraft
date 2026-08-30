# -*- coding: utf-8 -*-
"""Kusur SST'ye mi ozgu, yoksa butun omega ailesinde mi? -- ayirt edici.

DURUM. Duz levhada, sifir basinc gradyaninda, denge halindeki log
tabakasinda modelin kendi sabitlerinin zorunlu kildigi oran:

    nu_t / (kappa u_tau y) = 1,000

Olculen: SA 0,969 (yani olcum dogru), kOmegaSST 0,859. Ve bu 0,86;
serbest akis 100 kat azaltilinca, ag inceltilince ve duvar omega kosulu
iki onlu aralikta degistirilince DEGISMIYOR (omega_duvar.py). Duvar
kosulu C_f'i %3,5 oynatiyor ama log tabakasi dengesizligini
duzeltmiyor.

Ayrica a1 sinirlayicisi da elenmis durumda: olculen k ve omega'dan
k/omega = 0,957/1,113 = 0,860 cikiyor ve bu, olculen nu_t oraniyla ayni.
Yani nu_t gercekten k/omega'ya esit; sinirlayici devrede degil.

Geriye SST'ye ozgu makine kaliyor: F1 harmanlamasi (ic k-omega dali ile
dis k-epsilon dali arasinda) ve capraz yayilim terimi.

BU SINAMA. Ayni ag, ayni semalar, ayni sinir kosullari, tek fark model:
duz kOmega (Wilcox). Duz k-omega'nin log tabakasi da ayni ucu zorunlu
kilar; harmanlama ve capraz yayilim ise YOKTUR.

BEKLENTI ONCEDEN:
  (a) kOmega ~1,00 verirse kusur SST'ye ozgu makinededir (F1 / capraz
      yayilim). Bu, kaynagindan okunmadan duzeltilemez; RAPOR EDILIR,
      duzeltilmez.
  (b) kOmega da ~0,86 verirse kusur butun omega ailesinde ortaktir --
      yani omega denkleminin bizdeki ayrisimi ya da duvar yakini
      isleyisidir, SST'ye ozgu degildir.
"""
import json, os, subprocess, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
import duzlevha                                          # noqa: E402
from duzlevha import KOS                                 # noqa: E402
from omega_duvar import olc                              # noqa: E402
from kilit import Kilit                                  # noqa: E402

KOK = "/tmp/levha_model"
MODEL = ["kOmega", "kOmegaSST", "SpalartAllmaras"]

if __name__ == "__main__":
    with Kilit(KOK):
        yol = os.path.join(KOK, "sonuc.json")
        cikti = json.load(open(yol)) if os.path.exists(yol) else []
        yapilan = {d["model"] for d in cikti}
        for m in MODEL:
            if m in yapilan:
                continue
            vaka = os.path.join(KOK, m)
            duzlevha.kur(vaka, m)
            print("[%s] cozuluyor" % m, flush=True)
            r = subprocess.run(["bash", "-c", KOS % vaka])
            if r.returncode != 0:
                print("   KOSULAMADI (%d)" % r.returncode, flush=True)
                cikti.append(dict(model=m, hata=r.returncode))
            else:
                d = olc(vaka)
                print("   C_f=%.6f  nu_t/(k.u.y)=%.3f @y+%.0f  k+/3,333=%s"
                      "  omega/denge=%s"
                      % (d["Cf"], d["oran"], d["yp"],
                         "%.3f" % d["kp"] if d["kp"] else "-",
                         "%.3f" % d["om"] if d["om"] else "-"), flush=True)
                cikti.append(dict(model=m, **d))
            json.dump(cikti, open(yol, "w"), indent=1)

        print()
        print("  model              C_f     nu_t/(k.u.y)  k+/3,333  omega/denge")
        for d in cikti:
            if "oran" not in d:
                print("  %-16s (kosulamadi)" % d["model"])
            else:
                print("  %-16s %.6f    %.3f       %s     %s"
                      % (d["model"], d["Cf"], d["oran"],
                         "%.3f" % d["kp"] if d["kp"] else "  -  ",
                         "%.3f" % d["om"] if d["om"] else "  -  "))
        print("  HEDEF 1,000 -- modelin kendi kapanis sarti, disaridan olcum yok.")
