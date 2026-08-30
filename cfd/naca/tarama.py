# -*- coding: utf-8 -*-
"""Ag taramasi -- IKI AYRI AILE, ayri sorular.

A ailesi -- SABIT DUVAR ARALIGI
    Hucre sayilari 1.5 oraniyla buyur, ilk hucre yuksekligi y+ = 1'de
    SABIT kalir. Olctugu sey: yuzey ve iz cozunurlugune duyarlilik,
    sinir tabakasi cozunurlugu sabitken.

    Bu aileye Richardson UYGULANMAZ. Richardson tek bir h olcusunun
    varligini varsayar; burada duvara dik aralik olceklenmedigi icin
    boyle bir h yoktur ve "gozlenen mertebe" anlamsiz cikar.

B ailesi -- DUZGUN INCELTME
    Butun araliklar birlikte olceklenir: hucre sayilari r ile carpilir,
    ilk hucre yuksekligi r'ye BOLUNUR. Dolayisiyla y+ seviyeyle degisir
    (2.25 / 1.5 / 1.0 / 0.67). Richardson'un istedigi budur ve gozlenen
    mertebe ancak bu ailede anlam tasir.

Iki aile ayri ayri kaydedilir; karistirilmaz.
"""
import os, sys, subprocess, json

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
sys.path.insert(0, os.path.join(BURA, "..", "ortak"))
from kur import kur                                    # noqa: E402
from kuvvet import hesapla                             # noqa: E402

ADIM, YAZ = 3000, 500

# (ad, n_profil, n_normal, n_iz, yplus)
AILE = {
    "A": [("A1", 128, 48, 32, 1.0),
          ("A2", 192, 72, 48, 1.0),
          ("A3", 256, 96, 64, 1.0),
          ("A4", 384, 144, 96, 1.0)],
    "B": [("B1", 114, 43, 28, 2.25),
          ("B2", 171, 64, 43, 1.50),
          ("B3", 256, 96, 64, 1.00),
          ("B4", 384, 144, 96, 0.667)],
}


def zamanlar(vaka):
    z = []
    for a in os.listdir(vaka):
        try:
            v = float(a)
        except ValueError:
            continue
        if v > 0 and os.path.isdir(os.path.join(vaka, a)):
            z.append((v, a))
    return [a for _, a in sorted(z)]


def yurut(harf, kok):
    os.makedirs(kok, exist_ok=True)
    yol = os.path.join(kok, "sonuc.json")
    cikti = json.load(open(yol)) if os.path.exists(yol) else []
    yapilan = {d["ad"] for d in cikti}
    for ad, nf, nn, nw, yp in AILE[harf]:
        if ad in yapilan:
            continue
        vaka = os.path.join(kok, ad)
        bilgi = kur(vaka, kod="0012", Re=6e6, alfa=0.0, yplus=yp,
                    n_profil=nf, n_normal=nn, n_iz=nw,
                    adim=ADIM, yaz_araligi=YAZ)
        print("[%s] %d hucre  y+hedef %.3f -- cozuluyor"
              % (ad, bilgi["hucre"], yp), flush=True)
        subprocess.run([os.path.join(BURA, "kos.sh"), vaka, "4"],
                       check=True, stdout=subprocess.DEVNULL)
        gecmis = []
        for z in zamanlar(vaka):
            r = hesapla(vaka, alfa=0.0, zaman=z, mertebe=2)
            gecmis.append(dict(zaman=z, CD=r["CD"], CL=r["CL"],
                               CD_b=r["CD_basinc"], CD_v=r["CD_viskoz"],
                               yp_ort=r["yplus_ort"], yp_max=r["yplus_max"]))
        g = gecmis[-1]
        print("   CD=%.6f  CL=%+.2e  y+ %.2f/%.2f  (son iki yazim farki %+.2e)"
              % (g["CD"], g["CL"], g["yp_ort"], g["yp_max"],
                 g["CD"] - gecmis[-2]["CD"] if len(gecmis) > 1 else 0.0),
              flush=True)
        cikti.append(dict(ad=ad, hucre=bilgi["hucre"], NI=bilgi["NI"],
                          NJ=bilgi["NJ"], yplus_hedef=yp, gecmis=gecmis))
        json.dump(cikti, open(yol, "w"), indent=1)
    print("%s ailesi bitti" % harf)


if __name__ == "__main__":
    harf = sys.argv[1] if len(sys.argv) > 1 else "A"
    yurut(harf, sys.argv[2] if len(sys.argv) > 2 else "/tmp/tarama-" + harf)
