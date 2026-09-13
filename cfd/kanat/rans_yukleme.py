# -*- coding: utf-8 -*-
"""RANS'in aciklik yuklemesi ve K(y) = c_l,RANS / c_l,VLM.

Dort dis okumanin dordu de ayni seyi istedi: tarafsiz noktayi DEGIL,
aciklik boyunca yukleme ORANINI karsilastir. Sebep, tarafsiz noktanin
savunulabilir cozucu secimleri arasinda %1,34 MAC sacilmasi -- agin
hareketinin bes kati. RANS-VLM tarafsiz nokta farki o sacilmanin icinde
okunamaz kalir.

    K(y) = c_l c (y)_RANS / c_l c (y)_VLM      K_L = C_L,RANS / C_L,VLM

K(y)/K_L sabitse hata saf CARPANSALDIR ve makalenin iptal savunmasi
ayakta. Degilse yukleme yeniden dagilmistir; 3.10'un katsayilari
(derece basina 0,38 derece burulma) onu denge burulmasi hareketine
cevirir ve esik 2,6 derecedir.

NORMALLESTIRME. simpleFoam boyutsuz kosuyor: U = 1, p kinematik.
ortak/kuvvet.py Aref = 1 kullaniyor, kanat alanini DEGIL; ustelik kok
simetri duzlemi oldugu icin cozulen YARIM kanat. Ikisi de burada
duzeltiliyor ve sonuc hesapla()'nin kendi C_L'sine karsi sinaniyor.
Ilk surum ayrica isareti ters yazmisti (p S artidir, eksi degil) ve
C_L'yi -0,354 veriyordu.

KUTULAMA. Iki cozucu de AYNI tekduze kutulara toplanir. Ilk surum RANS'i
VLM'in kendi serit kenarlarina dolduruyordu ve neredeyse her sey tek
kutuya dusuyordu; K(y) iki farkli bolmenin orani olmamali.
"""
import json, math, os, sys
import numpy as np

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kuvvet import ag_oku, son_zaman, Alan, hesapla      # noqa: E402

N_KUTU = 16


def rans_serit(vaka, alfa_deg, yama="duvar"):
    """Duvar yuzlerinin BASINC kaldirmasi, aciklik konumuyla birlikte.

    Viskoz terim disarida: kosu duvar fonksiyonlu ve viskoz surukleme
    bundan RAPORLANMIYOR. Yuklemenin sekli basincin isidir; hesapla()
    zaten C_L'nin tamaminin basinctan geldigini gosteriyor.
    """
    ag, nu = ag_oku(vaka)
    z = son_zaman(vaka)
    p = Alan(vaka, z, "p")
    y = ag.yama[yama]
    a = math.radians(alfa_deg)
    kal = (-math.sin(a), math.cos(a), 0.0)
    span, L = [], []
    for k in range(y["n"]):
        fi = y["bas"] + k
        S, C = ag.yuz_alan(fi)
        if S[0] == S[1] == S[2] == 0.0:
            continue
        pf = p.yama_degeri(yama, k)
        if pf is None:
            pf = p.ic[ag.sahip[fi]]
        span.append(C[2])
        L.append(pf * (S[0] * kal[0] + S[1] * kal[1]))
    return np.array(span), np.array(L)


def kutula(y, agir, kenar):
    idx = np.clip(np.digitize(y, kenar) - 1, 0, len(kenar) - 2)
    cik = np.zeros(len(kenar) - 1)
    for i, w in zip(idx, agir):
        cik[i] += w
    return cik


if __name__ == "__main__":
    vaka, alfa = sys.argv[1], float(sys.argv[2])
    vj = json.load(open(os.path.join(BURA, "..", "..", "aero",
                                     "vlm_yukleme.json")))
    S_ref, yari = vj["S"], vj["yari"]

    ref = hesapla(vaka, alfa=alfa, mertebe=2)
    span, L = rans_serit(vaka, alfa)
    print("duvar yuzu %d, aciklik %.4f .. %.4f m (yari aciklik %.4f)"
          % (len(span), span.min(), span.max(), yari))

    # SINAMA: yuz toplami hesapla()'nin kendi C_L'sini uretmeli.
    CL_ref_1 = ref["CL"]                    # Aref = 1, yarim kanat
    CL_bizim = L.sum() / 0.5                # ayni normalizasyon
    print("SINAMA  hesapla() C_L(Aref=1) = %.4f, yuz toplamimiz = %.4f"
          % (CL_ref_1, CL_bizim))
    if abs(CL_bizim - CL_ref_1) > 0.02 * abs(CL_ref_1):
        sys.exit("!! DUR -- yuz toplami hesapla()'yi uretmiyor.")

    # Kanat alanina ve TAM kanada cevir: yarim kanat x 2 / S_ref
    CL_rans = 2.0 * (L.sum() / 0.5) / S_ref
    KL = CL_rans / vj["CL"]
    print()
    print("TOPLAM")
    print("  RANS C_L = %.4f   VLM C_L = %.4f   K_L = %.3f"
          % (CL_rans, vj["CL"], KL))

    # --- AGI KURAN ISTASYON LISTESI kenar olarak ----------------------
    # Iki yanlis deneme oldu ve ikisi de kutulama kusuruydu:
    #   1. tekduze kutu -> kimi kutu bos kaldi, K(y) tirtiklandi
    #   2. yuz merkezlerinin farkli z'leri -> 621 "istasyon" cikti;
    #      duvar yuzleri sabit-z duzlemlerinde DEGIL.
    # Dogrusu, agi kuran istasyon listesini dogrudan kullanmak: o liste
    # geometrinin tanimi ve iki cozucu de ayni kenarlara toplanabilir.
    from gercek import gercek_istasyonlar
    # ISTASYON SAYISI VAKAYA AITTIR, sabit DEGIL. Ilk surum n=20'yi
    # gomuyordu; 28 istasyonlu orta agda kenarlar agin istasyonlariyla
    # hizalanmiyor ve yuzler kutular arasinda SIRAYLA dusuyor. Cikan
    # duzenli alternatif desen (0,56 / 1,15 / 0,56 / 1,11 ...) fizik
    # degil, hizalanmama kusuruydu.
    n_ist = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    gist, _ = gercek_istasyonlar(n=n_ist, sikistir=True)
    kenar = np.array([g[0] for g in gist], dtype=float)
    kenar[0] = 0.0
    kenar[-1] = max(kenar[-1], float(np.abs(span).max()), yari)
    print("\nkenar: agi kuran %d istasyon" % len(kenar))
    if len(kenar) - 1 < 8:
        sys.exit("!! DUR -- kutu sayisi cok az.")
    Lr = kutula(np.abs(span), L, kenar)
    clc_r = 2.0 * (Lr / 0.5) / np.diff(kenar)          # c_l*c, tam kanat

    # VLM tarafi KUTULANMAZ, INTEGRALI ALINIR. Sebep: VLM'in 104 ince
    # seridi 20 kaba kutuya doldurulunca kutu sinirlari seritleri kesiyor
    # ve pürüzsüz dagilim tirtiklaniyor -- tirtik fizik degil, bolme
    # kusuru. c_l c (y) duzgun bir egri; her kutuda ince orneklemeyle
    # ortalamasi aliniyor.
    yv = np.array(vj["y"]); clcv = np.array(vj["clc"])
    clc_v = np.empty(len(kenar) - 1)
    for i in range(len(kenar) - 1):
        ince = np.linspace(kenar[i], kenar[i + 1], 200)
        clc_v[i] = np.interp(ince, yv, clcv).mean() * 2.0

    # Uc kutusu disarida: orada VLM yuklemesi sifira gider ve RANS'ta uc
    # kapagi var; oran iki kucuk sayinin bolumu olur ve anlamsizdir.
    ok = (clc_v > 0.05 * clc_v.max())
    ok[-1] = False
    K = clc_r[ok] / clc_v[ok]
    orta = 0.5 * (kenar[:-1] + kenar[1:])[ok]
    print()
    print("%-8s %12s %12s %8s %9s" % ("eta", "VLM c_l*c", "RANS c_l*c",
                                      "K", "K/K_L"))
    for e, a, b, k in zip(orta / yari, clc_v[ok], clc_r[ok], K):
        print("%-8.3f %12.4f %12.4f %8.3f %9.3f" % (e, a, b, k, k / KL))
    kk = K / KL
    print()
    print("K/K_L  ortalama %.3f, aralik %.3f .. %.3f, sacilma %.1f %%"
          % (kk.mean(), kk.min(), kk.max(),
             100 * (kk.max() - kk.min()) / kk.mean()))
    json.dump(dict(eta=list(map(float, orta / yari)),
                   K=list(map(float, K)), KL=float(KL),
                   CL_rans=float(CL_rans), CL_vlm=vj["CL"],
                   clc_rans=list(map(float, clc_r[ok])),
                   clc_vlm=list(map(float, clc_v[ok]))),
              open(os.path.join(BURA, "rans_vlm.json"), "w"), indent=1)
