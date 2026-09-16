# -*- coding: utf-8 -*-
"""AG INCELTME KIYASI -- eta ~ 0,94 sapmasi fizik mi, ayriklastirma mi?

Iki (sonra uc) cozunurlukte ayni nicelik: K(y)/K_L. Soru, uctaki
sapmanin ag inceldikce KUCULUP kuculmedigi. Kuculuyorsa ayriklastirma,
kalmiyorsa fizik.

Iki olcu ayri ayri veriliyor:
  - IC BOLGE (eta <= 0,90): iptal savunmasinin dayandigi bolge
  - UC BOLGESI (eta > 0,90): sapmanin oturdugu yer
Ikisini ayirmak sart, cunku tek bir sacilma sayisi ikisini karistirir ve
"uc kotulesti ama ic duzeldi" durumunu gizler.
"""
import json, os, subprocess, sys
import numpy as np

BURA = os.path.dirname(os.path.abspath(__file__))
SEVIYE = (("alfa6.7", 20, 192320), ("orta", 28, 444416), ("ince", 36, 681984))
SINIR = 0.90


def oku(vaka, n):
    y = os.path.join(BURA, "data", "real3d", vaka)
    if not os.path.exists(os.path.join(y, "3000")):
        return None
    subprocess.run([sys.executable, os.path.join(BURA, "rans_loading.py"),
                    y, "6.69", str(n)], capture_output=True, text=True)
    return json.load(open(os.path.join(BURA, "rans_vlm.json")))


if __name__ == "__main__":
    # OLCU, KUTU SAYISINDAN BAGIMSIZ OLMALI. Azami-asgari degil:
    # 20 kutulu ag ile 28 kutulu agi azami-asgari ile kiyaslamak, daha
    # cok kutuya daha cok uc deger sansi vermek demektir ve "inceltince
    # kotulesti" gibi sahte bir sonuc uretir. Iki olcu veriliyor:
    #   - standart sapma (kutu sayisina duyarsiz)
    #   - ORTAK eta izgarasina ara degerlenmis azami-asgari
    ORTAK = np.linspace(0.05, SINIR, 15)
    print("%-8s %8s %7s %9s %9s %9s %9s"
          % ("ag", "hucre", "K_L", "C_L", "ic std", "ic mak-min", "uc std"))
    for ad, n, hucre in SEVIYE:
        d = oku(ad, n)
        if d is None:
            print("%-8s %8d  -- henuz kosmadi --" % (ad, hucre))
            continue
        eta = np.array(d["eta"]); kk = np.array(d["K"]) / d["KL"]
        ic, uc = kk[eta <= SINIR], kk[eta > SINIR]
        ortak = np.interp(ORTAK, eta, kk)
        print("%-8s %8d %7.3f %9.4f %9.3f %9.3f %9.3f"
              % (ad, hucre, d["KL"], d["CL_rans"], ic.std(),
                 ortak.max() - ortak.min(),
                 uc.std() if len(uc) > 1 else float("nan")))
    print()
    print("ic bolge eta <= %.2f, uc bolgesi eta > %.2f" % (SINIR, SINIR))
    print("ortak izgara: %d nokta, eta 0,05 - %.2f" % (15, SINIR))
    print("Sacilma ag inceldikce KUCULUYORSA ayriklastirma; KALIYORSA fizik.")
