# -*- coding: utf-8 -*-
"""Alan boyutu duyarliligi: dis sinir ne kadar uzakta olmali?

B ailesinde ag yakinsamasi salinimli cikti ve salinim viskoz kisimda.
Duvar gradyani kestiriminin bundan sorumlu OLMADIGI gosterildi (ikinci
mertebeye gecince en ince iki agda degisim %0,1'in altinda). Geriye, ag
inceldikce KUCULMEYEN bir hata kaynagi kaliyor: dis sinir sabit 20
veterde tutuldu.

Bu betik ayni cozunurlukte alani buyutuyor. Hucre sayisi degismez,
yalnizca hucreler disariya dogru daha cok gerilir; boylece olculen sey
yalnizca alan boyutudur.
"""
import os, sys, subprocess, json, math

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kur import kur                                    # noqa: E402
from kuvvet import hesapla                             # noqa: E402
from kilit import Kilit                                # noqa: E402

BOYUT = [20.0, 50.0, 100.0, 200.0]
KOK = "/tmp/alan2"

# MODEL SECIMI -- sonradan eklendi. Bu calisma kur()'un varsayilaniyla,
# yani kOmegaSST ile kosulmustu. Sonradan olculdu ki SST kurulumumuz
# yuzey surtunmesini referans kodlarin 5-7 yuzde altinda veriyor, SA ise
# iki bagimsiz kodla profil duzeyinde cakisiyor (bkz. dogrulama.md).
# Yani makaleye gidecek sayilar SA ile uretilmelidir. Kullanim:
#     python3 <betik> [model]
MODEL = sys.argv[1] if len(sys.argv) > 1 else "kOmegaSST"
if MODEL != "kOmegaSST":
    KOK = KOK + "-" + MODEL

# Alan buyurken n_normal SABIT tutulursa dis hucreler de gerilir ve olculen
# sey saf alan boyutu olmaz -- alan boyutu ARTI bozulan uzak alan
# cozunurlugu olur. Ilk kosuda bu yapildi ve fark her katlamada ~1e-5 ile
# azalmadi; oysa uzak alan hatasinin azalmasi gerekir. Burada n_normal, j
# yonundeki BUYUME ORANI sabit kalacak sekilde her R icin yeniden
# secilir: yakin alan degismez, yalnizca disariya katman EKLENIR.


def n_normal_sec(R, dy, r_hedef):
    """Buyume orani r_hedef'te kalacak sekilde gereken katman sayisi."""
    return int(round(math.log(1 + R * (r_hedef - 1) / dy) / math.log(r_hedef)))


def buyume_orani(R, dy, n):
    lo, hi = 1.0 + 1e-12, 2.0
    for _ in range(200):
        r = (lo + hi) / 2
        if dy * (r ** n - 1) / (r - 1) < R:
            lo = r
        else:
            hi = r
    return (lo + hi) / 2

if __name__ == "__main__":
    with Kilit(KOK):
        os.makedirs(KOK, exist_ok=True)
        yol = os.path.join(KOK, "sonuc.json")
        cikti = json.load(open(yol)) if os.path.exists(yol) else []
        yapilan = {d["R"] for d in cikti}
        from cagi import ilk_hucre_yuksekligi
        dy = ilk_hucre_yuksekligi(6e6, 1.0)
        r0 = buyume_orani(20.0, dy, 96)            # olcut: R = 20, 96 katman
        for R in BOYUT:
            if R in yapilan:
                continue
            nn = n_normal_sec(R, dy, r0)
            vaka = os.path.join(KOK, "R%d" % R)
            bilgi = kur(vaka, kod="0012", Re=6e6, alfa=0.0, yplus=1.0,
                        n_profil=256, n_normal=nn, n_iz=64, R=R, Xiz=R,
                        adim=3000, yaz_araligi=1500, model=MODEL)
            print("[R=%g] n_normal=%d  %d hucre  (buyume orani %.4f) -- cozuluyor"
                  % (R, nn, bilgi["hucre"], buyume_orani(R, dy, nn)), flush=True)
            subprocess.run([os.path.join(BURA, "kos.sh"), vaka, "4"],
                           check=True, stdout=subprocess.DEVNULL)
            r = hesapla(vaka, alfa=0.0, mertebe=2)
            print("   C_D=%.6f  basinc=%.6f  viskoz=%.6f  C_L=%+.2e  y+ %.2f"
                  % (r["CD"], r["CD_basinc"], r["CD_viskoz"], r["CL"],
                     r["yplus_ort"]), flush=True)
            cikti.append(dict(R=R, n_normal=nn, hucre=bilgi["hucre"], CD=r["CD"],
                              CD_b=r["CD_basinc"], CD_v=r["CD_viskoz"],
                              CL=r["CL"], yp=r["yplus_ort"]))
            json.dump(cikti, open(yol, "w"), indent=1)
        print("bitti")
