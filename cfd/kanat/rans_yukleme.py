# -*- coding: utf-8 -*-
"""RANS'in aciklik yuklemesi -- VLM ile K(y) karsilastirmasi.

Duvar yuzlerinin BASINC kuvvetleri aciklik seritlerine toplanir. Viskoz
terim BILEREK disarida: bu kosu duvar fonksiyonlu ve viskoz suruklemeyi
raporlamak icin kurulmadi. Yuklemenin SEKLI basinc dagiliminin isidir.

Toplam, ayni yuzlerden hesaplanan C_L'ye karsi sinaniyor.
"""
import json, math, os, sys
import numpy as np

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kuvvet import ag_oku, son_zaman, Alan              # noqa: E402


def aciklik(vaka, alfa_deg, S_ref, yama="duvar"):
    ag, nu = ag_oku(vaka)
    z = son_zaman(vaka)
    p = Alan(vaka, z, "p")
    y = ag.yama[yama]
    span, kuv = [], []
    for k in range(y["n"]):
        fi = y["bas"] + k
        S, C = ag.yuz_alan(fi)
        A = math.sqrt(sum(s * s for s in S))
        if A <= 0:
            continue
        pf = p.yama_degeri(yama, k)
        if pf is None:
            pf = p.ic[ag.sahip[fi]]
        span.append(C[2])                       # ag z'yi aciklik sayar
        kuv.append((pf * S[0], pf * S[1]))      # (Fx, Fy), basinc
    span = np.array(span)
    Fx = np.array([a for a, _ in kuv])
    Fy = np.array([b for _, b in kuv])
    ar = math.radians(alfa_deg)
    # Kaldirma ruzgar ekseninde. Isaret: S akistan GOVDEYE bakiyor, yani
    # govdeye etkiyen kuvvet -pS. hesapla() ile ayni evre korunuyor.
    L = -(Fy * math.cos(ar) - Fx * math.sin(ar))
    return span, L


if __name__ == "__main__":
    vaka = sys.argv[1]
    alfa = float(sys.argv[2])
    vj = json.load(open(os.path.join(BURA, "..", "..", "aero",
                                     "vlm_yukleme.json")))
    S_ref, yari = vj["S"], vj["yari"]
    span, L = aciklik(vaka, alfa, S_ref)
    print("duvar yuzu %d, aciklik araligi %.4f .. %.4f m"
          % (len(span), span.min(), span.max()))

    # VLM'in KENDI serit kenarlarina topla -- ayni kutulara dusmeleri sart,
    # yoksa K(y) iki farkli bolmenin orani olur.
    yv = np.array(vj["y"])
    kenar = np.empty(len(yv) + 1)
    kenar[1:-1] = 0.5 * (yv[:-1] + yv[1:])
    kenar[0] = max(0.0, yv[0] - (kenar[1] - yv[0]))
    kenar[-1] = yari
    idx = np.clip(np.digitize(np.abs(span), kenar) - 1, 0, len(yv) - 1)
    Ls = np.zeros(len(yv))
    for i, f in zip(idx, L):
        Ls[i] += f
    gen = np.diff(kenar)
    q = 0.5                                   # U = 1, rho = 1 (boyutsuz)
    clc_r = Ls / (q * gen)

    CL_r = np.sum(clc_r * gen) / S_ref * 2.0
    print("RANS C_L (basinc, aciklik toplamindan) = %.4f" % CL_r)
    print("VLM  C_L                               = %.4f" % vj["CL"])
    print("K_L = %.3f" % (CL_r / vj["CL"]))

    clc_v = np.array(vj["clc"])
    ok = clc_v > 0.05 * clc_v.max()
    K = clc_r[ok] / clc_v[ok]
    KL = CL_r / vj["CL"]
    print()
    print("%-8s %10s %10s %8s %9s" % ("eta", "VLM c_l*c", "RANS c_l*c",
                                      "K", "K/K_L"))
    et = yv[ok] / yari
    for i in range(0, len(et), max(1, len(et) // 12)):
        print("%-8.3f %10.4f %10.4f %8.3f %9.3f"
              % (et[i], clc_v[ok][i], clc_r[ok][i], K[i], K[i] / KL))
    print()
    print("K/K_L sacilmasi: %.3f .. %.3f  (sabit ise hata saf carpansal)"
          % ((K / KL).min(), (K / KL).max()))
    json.dump(dict(eta=list(map(float, et)), K=list(map(float, K)),
                   KL=float(KL), CL_rans=float(CL_r), CL_vlm=vj["CL"]),
              open(os.path.join(BURA, "rans_vlm.json"), "w"), indent=1)
