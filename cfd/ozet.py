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
    "B-SA": "/tmp/tarama-B-SA/sonuc.json",
    "tmrgeo": "/tmp/tmrgeo/sonuc.json",
    "levha_model": "/tmp/levha_model/sonuc.json",
    "levha_omega": "/tmp/levha_omega/sonuc.json",
    "levha_sema": "/tmp/levha_sema/sonuc.json",
    "A-SA": "/tmp/tarama-A-SA/sonuc.json",
    "alan-SA": "/tmp/alan2-SpalartAllmaras/sonuc.json",
    "kalinlik-SA": "/tmp/kalinlik-SpalartAllmaras/sonuc.json",
    "yplus": "/tmp/yplus/sonuc.json",
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


def alan_tablo(md=False, ad="alan"):
    d = yukle(ad)
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


def kalinlik_tablo(md=False, ad="kalinlik"):
    d = yukle(ad)
    if not d:
        return None
    d = sorted(d, key=lambda x: x["kalinlik"])
    s = [["%d%%" % v["kalinlik"], "%.6f" % v["CD"], "%.6f" % v["nf_xtr0"],
          "%.3f" % (v["CD"] / v["nf_xtr0"]), "%.6f" % v["nf_xtr5"],
          "%.3f" % (v["CD"] / v["nf_xtr5"])] for v in d]
    return tablo(["t/c", "RANS C_D", "NF (xtr→0)", "oran",
                  "NF (xtr=0,05)", "oran"], s, md)


def tmrgeo_tablo(md=False):
    d = yukle("tmrgeo")
    if not d:
        return None
    s = [[v["model"], "%.6f" % v["onceki"], "%.6f" % v["CD"],
          "%+.2f" % ((v["CD"] / v["onceki"] - 1) * 100)] for v in d]
    return tablo(["model", "%12 kapalı", "TMR %11,894", "değişim %"], s, md)


def _levha(ad, anahtar, basliklar, md=False):
    d = yukle(ad)
    if not d:
        return None
    s = []
    for v in d:
        if "oran" not in v:
            s.append([v.get(anahtar, "?"), "(koşulamadı)", "", "", ""])
            continue
        s.append([v[anahtar], "%.6f" % v["Cf"], "%.3f" % v["oran"],
                  "%.3f" % v["kp"] if v.get("kp") else "-",
                  "%.3f" % v["om"] if v.get("om") else "-"])
    return tablo(basliklar, s, md)


def levha_model_tablo(md=False):
    return _levha("levha_model", "model",
                  ["model", "C_f", "ν_t/(κu_τy)", "k+/3,333", "ω/ω_denge"], md)


def levha_omega_tablo(md=False):
    return _levha("levha_omega", "ad",
                  ["varyant", "C_f", "ν_t/(κu_τy)", "k+/3,333", "ω/ω_denge"], md)


def levha_sema_tablo(md=False):
    return _levha("levha_sema", "ad",
                  ["varyant", "C_f", "ν_t/(κu_τy)", "k+/3,333", "ω/ω_denge"], md)


BOLUM = [("A ailesi — sabit duvar aralığı (y+ = 1), yalnızca hücre sayısı ölçekleniyor",
          lambda m: ag_ailesi("A", m)),
         ("B ailesi — düzgün inceltme, bütün aralıklar birlikte",
          lambda m: ag_ailesi("B", m)),
         ("Alan boyutu — büyüme oranı sabit tutularak", alan_tablo),
         ("Türbülans modeli", model_tablo),
         ("Kalınlık — RANS ile NeuralFoil (2. basamak)", kalinlik_tablo),
         # --- makalenin birincil modeli SA; ag yakinsamasi onun icin de
         #     olculmeliydi ve olculdu (bkz. dogrulama.md)
         ("B ailesi, **Spalart–Allmaras** ile — makalenin birincil modeli",
          lambda m: ag_ailesi("B-SA", m)),
         ("Geometri — TMR'ın %11,894 profiliyle", tmrgeo_tablo),
         # --- duz levha: SST acigini yalitma calismalari.
         #     Oran hedefi 1,000 ama DENGE halindeki log tabakasi icin
         #     kesindir; gelisen sinir tabakasinda mutlak sapma bir kusur
         #     olcusu DEGIL, isarettir (bkz. dogrulama.md "DUZELTME").
         #     Anlamli olan varyantlar arasindaki karsilastirmadir.
         ("Düz levha — model ayırt edici", levha_model_tablo),
         ("Düz levha — duvar ω koşulu, serbest akış ve ağ", levha_omega_tablo),
         ("Düz levha — ayrışım şemaları", levha_sema_tablo),
         # --- makaleye gidecek sayilar: SA ile
         ("A ailesi, **Spalart–Allmaras** ile", lambda m: ag_ailesi("A-SA", m)),
         ("Alan boyutu, **Spalart–Allmaras** ile",
          lambda m: alan_tablo(m, "alan-SA")),
         ("Kalınlık, **Spalart–Allmaras** ile — 2. basamağın çıktısı",
          lambda m: kalinlik_tablo(m, "kalinlik-SA"))]


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
