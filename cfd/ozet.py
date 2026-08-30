# -*- coding: utf-8 -*-
"""Butun CFD calismalarinin sonuc tablolarini TEK kaynaktan uretir.

Neden: bu depoda daha once, makalenin 7.4'undeki iki tablo bayat kaldi ve
ayni vaka iki yerde farkli sayilarla gorundu. `dogrula.py` onu yakaladi ve
o gunden beri kural su: bir sayi iki yerde duruyorsa, ikincisi elle
yazilmaz.

`cfd/README.md`'deki tablolar bu betigin ciktisidir. Kosular yenilenince
tablo da yenilenir; elle guncellenmesi gereken hicbir sayi kalmaz.

    python3 cfd/ozet.py            ekrana
    python3 cfd/ozet.py --md       README'ye yapistirilacak markdown
"""
import json, os, sys

KAYNAK = {
    "A": "/tmp/tarama-A/sonuc.json",
    "B": "/tmp/tarama-B/sonuc.json",
    "alan": "/tmp/alan2/sonuc.json",
    "model": "/tmp/model/sonuc.json",
    "kalinlik": "/tmp/kalinlik/sonuc.json",
}


def yukle(ad):
    y = KAYNAK[ad]
    return json.load(open(y)) if os.path.exists(y) else None


def tablo(basliklar, satirlar, md=False):
    if md:
        out = ["| " + " | ".join(basliklar) + " |",
               "|" + "|".join(["---:"] * len(basliklar)) + "|"]
        out += ["| " + " | ".join(str(v) for v in s) + " |" for s in satirlar]
        return "\n".join(out)
    g = [max(len(str(b)), max((len(str(s[i])) for s in satirlar), default=0))
         for i, b in enumerate(basliklar)]
    out = ["  " + "  ".join(str(b).rjust(g[i]) for i, b in enumerate(basliklar))]
    out.append("  " + "  ".join("-" * g[i] for i in range(len(basliklar))))
    out += ["  " + "  ".join(str(v).rjust(g[i]) for i, v in enumerate(s))
            for s in satirlar]
    return "\n".join(out)


def ag_ailesi(harf, md=False):
    d = yukle(harf)
    if not d:
        return None
    d = sorted(d, key=lambda x: x["hucre"])
    s = []
    for v in d:
        g = v["gecmis"][-1]
        s.append([v["ad"], v["hucre"], "%.3f" % v.get("yplus_hedef", 1.0),
                  "%.2f" % g["yp_ort"], "%.6f" % g["CD"],
                  "%.6f" % g["CD_b"], "%.6f" % g["CD_v"]])
    return tablo(["ag", "hücre", "y+ hedef", "y+ ölç.", "C_D",
                  "basınç", "viskoz"], s, md)


def alan_tablo(md=False):
    d = yukle("alan")
    if not d:
        return None
    d = sorted(d, key=lambda x: x["R"])
    s = [["%g" % v["R"], v.get("n_normal", "-"), v["hucre"],
          "%.6f" % v["CD"], "%.6f" % v["CD_b"], "%.6f" % v["CD_v"],
          "%+.2f" % ((v["CD"] / d[0]["CD"] - 1) * 100)] for v in d]
    return tablo(["R (veter)", "n_normal", "hücre", "C_D", "basınç",
                  "viskoz", "R=20'ye göre %"], s, md)


def model_tablo(md=False):
    d = yukle("model")
    if not d:
        return None
    s = [[v["model"], "%.6f" % v["CD"], "%.6f" % v["CD_b"],
          "%.6f" % v["CD_v"], "%.2f" % v["yp"]] for v in d]
    if len(d) == 2:
        s.append(["fark %", "%+.2f" % ((d[1]["CD"] / d[0]["CD"] - 1) * 100),
                  "%+.2f" % ((d[1]["CD_b"] / d[0]["CD_b"] - 1) * 100),
                  "%+.2f" % ((d[1]["CD_v"] / d[0]["CD_v"] - 1) * 100), ""])
    return tablo(["model", "C_D", "basınç", "viskoz", "y+"], s, md)


def kalinlik_tablo(md=False):
    d = yukle("kalinlik")
    if not d:
        return None
    d = sorted(d, key=lambda x: x["kalinlik"])
    s = [["%d%%" % v["kalinlik"], "%.6f" % v["CD"], "%.6f" % v["nf_xtr0"],
          "%.3f" % (v["CD"] / v["nf_xtr0"]), "%.6f" % v["nf_xtr5"],
          "%.3f" % (v["CD"] / v["nf_xtr5"])] for v in d]
    return tablo(["t/c", "RANS C_D", "NF (xtr→0)", "oran",
                  "NF (xtr=0,05)", "oran"], s, md)


BOLUM = [("A ailesi — sabit duvar aralığı (y+ = 1), yalnızca hücre sayısı ölçekleniyor",
          lambda m: ag_ailesi("A", m)),
         ("B ailesi — düzgün inceltme, bütün aralıklar birlikte",
          lambda m: ag_ailesi("B", m)),
         ("Alan boyutu — büyüme oranı sabit tutularak", alan_tablo),
         ("Türbülans modeli", model_tablo),
         ("Kalınlık — RANS ile NeuralFoil (2. basamak)", kalinlik_tablo)]


if __name__ == "__main__":
    md = "--md" in sys.argv
    for baslik, f in BOLUM:
        t = f(md)
        if t is None:
            print(("### " if md else "") + baslik)
            print("_(henüz koşulmadı)_" if md else "  (henüz koşulmadı)")
            print()
            continue
        print(("### " if md else "") + baslik)
        print()
        print(t)
        print()
