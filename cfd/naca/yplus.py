# -*- coding: utf-8 -*-
"""y+ duyarliligi -- ag topolojisi SABIT, yalnizca duvar araligi degisir.

Nereden cikti: en-boy sinirini profil yuzeyinden kaldirdiktan sonra A
ailesi (duvar araligi sabit) TEKDUZE yakinsadi, B ailesi (her sey birlikte
incelir) salinimli kaldi. Fark tam olarak yalitilabiliyor: A4 ile B4 ayni
hucre sayisinda (82 944) ve ayni topolojide; tek fark duvar araligi.

    A4   y+ = 0,96   C_D = 0,007649
    B4   y+ = 0,64   C_D = 0,007750     -> %1,3, YALNIZCA y+'tan

Demek ki B'deki salinim bir ag yakinsama kusuru degil, duvar
cozunurlugune duyarlilik. Bu betik o duyarliligi haritalar: ayni
384 x 144 x 96 topolojide birkac y+ hedefi.

Beklenti dogru kurulmali: cozumlenmis sinir tabakasinda (y+ < 1) sonucun
y+'a duyarsiz olmasi beklenir. Duyarli cikiyorsa bu, duvar isleminin
kendisinin bir ozelligidir -- omegaWallFunction'in harmanlamasi ve
viskoz alt tabakada omega ~ 6 nu / (beta1 y^2) bagintisi y -> 0'da
iraksar. Olculen sey budur, aginin 'yakinsamamis' olmasi degil.
"""
import json, os, subprocess, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kur import kur                                    # noqa: E402
from kuvvet import hesapla                             # noqa: E402
from kilit import Kilit                                # noqa: E402

HEDEF = [1.50, 1.00, 0.667, 0.40]
NF, NN, NW = 384, 144, 96
KOK = "/tmp/yplus"

# MODEL SECIMI -- sonradan eklendi, ve burada ozel bir anlami var.
#
# Yukaridaki gerekce SST'ye OZGU bir mekanizmaya dayaniyor:
# omegaWallFunction'in harmanlamasi ve omega ~ 6 nu/(beta1 y^2)'nin
# y -> 0'da iraksamasi. SA'da omega denklemi YOKTUR. Dolayisiyla ongoru
# su: SA ile y+ duyarliligi cok daha kucuk olmali.
#
# Bu ongoru bos degil, elimizde destegi var: B ailesi SST ile SALINIMLI
# yakinsamisti (0,008494 / 0,007804 / 0,007691 / 0,007750), SA ile ise
# TEKDUZE (0,009848 / 0,008983 / 0,008416 / 0,008234). Yani betigin
# cikis noktasi olan salinim, SST'ye ozgu gorunuyor.
#
# Makaleye giden belirsizlik butcesi SA'nin duyarliligidir; SST kosusu
# ise kusurun karakterizasyonuna aittir. Ikisi de kosulur.
#     python3 cfd/naca/yplus.py [model]
MODEL = sys.argv[1] if len(sys.argv) > 1 else "kOmegaSST"
if MODEL != "kOmegaSST":
    KOK = KOK + "-" + MODEL

if __name__ == "__main__":
    with Kilit(KOK):
        yol = os.path.join(KOK, "sonuc.json")
        cikti = json.load(open(yol)) if os.path.exists(yol) else []
        yapilan = {d["hedef"] for d in cikti}
        for yp in HEDEF:
            if yp in yapilan:
                continue
            vaka = os.path.join(KOK, "y%03d" % round(yp * 100))
            bilgi = kur(vaka, kod="0012", Re=6e6, alfa=0.0, yplus=yp,
                        n_profil=NF, n_normal=NN, n_iz=NW,
                        adim=3000, yaz_araligi=1500, model=MODEL)
            print("[y+ %.3f] %d hucre -- cozuluyor" % (yp, bilgi["hucre"]),
                  flush=True)
            subprocess.run([os.path.join(BURA, "kos.sh"), vaka, "4"],
                           check=True, stdout=subprocess.DEVNULL)
            r = hesapla(vaka, alfa=0.0, mertebe=2)
            print("   C_D=%.6f  basinc=%.6f  viskoz=%.6f  y+ olculen %.2f"
                  % (r["CD"], r["CD_basinc"], r["CD_viskoz"], r["yplus_ort"]),
                  flush=True)
            cikti.append(dict(hedef=yp, hucre=bilgi["hucre"], CD=r["CD"],
                              CD_b=r["CD_basinc"], CD_v=r["CD_viskoz"],
                              yp=r["yplus_ort"], CL=r["CL"]))
            json.dump(cikti, open(yol, "w"), indent=1)
        d = sorted(cikti, key=lambda x: -x["hedef"])
        print("\n  y+ hedef  y+ olcum      C_D    basinc    viskoz   en dusuge gore")
        taban = min(v["CD"] for v in d)
        for v in d:
            print("    %.3f     %.2f    %.6f  %.6f  %.6f    %+.2f%%"
                  % (v["hedef"], v["yp"], v["CD"], v["CD_b"], v["CD_v"],
                     (v["CD"] / taban - 1) * 100))
        print("bitti")
