# -*- coding: utf-8 -*-
"""v8 SEKIL SAYISI DENETIMI (Tur 141; P-e: DeepSeek P3 + Qwen P1, dort okuyucu + Claude).

Her v8 sekil betiginin etiket, aciklama ve altyazi dizgilerindeki her sayi, govdede ya da
ekte AYNI KIMLIKLE (deger + birim) gecmeli. Gorsel oncul kurali (Tur 103): sekil, govdenin
tanimlamadigi ya da eke gondermedigi bir sayi getiremez.

  YOK       -> sayi govdede ve ekte hic yok: HATA (cikis 1)
  YALNIZ-DEGER -> sayi var ama sekildeki birimiyle yok: insan okur (0.47 vakasi, F1/S-62)
  ok        -> deger + birim govdede ya da ekte

--sina : F1'i (Tur 139) geri koyar ve denetimin onu YAKALADIGINI sinar.
"""
import ast, os, re, sys

KOK = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.dirname(__file__))
from v8_stale import SEKILLER

BIRIM = r"(m|cm|mm|kg|kW|W|Pa|%|°|s|km|N·m|N\.m|W/kg|kW/kg|m²|m/s)"
SAYI = re.compile(r"(?<![\w.#/-])(\d+(?:\.\d+)?)\s*" + BIRIM + r"?(?![\w])")


def duz(x):
    return re.sub(r"\s+", " ", x.replace("*", "").replace("$", "").replace("\\,", " "))


def dizgiler(kaynak):
    agac = ast.parse(kaynak)
    belge = ast.get_docstring(agac, clean=False)
    out = []
    for d in ast.walk(agac):
        if isinstance(d, ast.Constant) and isinstance(d.value, str) and d.value != belge:
            s = d.value
            if s.startswith("#") or s.endswith((".png", ".svg", ".ttf")) or "/" in s and " " not in s:
                continue                                    # renk, dosya yolu
            out.append(s)
    return duz(" ".join(out))


def metin():
    govde = open(os.path.join(KOK, "paper", "v8", "ALL-STEPS.md"), encoding="utf-8").read()
    ek = open(os.path.join(KOK, "paper", "v8", "supplement.md"), encoding="utf-8").read()
    return duz(govde + " " + ek)


def denetle(etiketler, hedef):
    yok, yalniz = [], []
    for ad, lab in etiketler:
        for m in SAYI.finditer(lab):
            v, b = m.group(1), m.group(2)
            if not b:                                       # birimsiz: deger yoksa insan okusun (0, indeks, 2.43 x)
                if not re.search(r"(?<![\d.])" + re.escape(v) + r"(?![\d])", hedef):
                    yalniz.append((ad, v + " (birimsiz, degeri de yok)"))
                continue
            ifade = re.compile(r"(?<![\d.])" + re.escape(v) + r"\s*" + re.escape(b) + r"(?![\w])")
            if ifade.search(hedef):
                continue
            if re.search(r"(?<![\d.])" + re.escape(v) + r"(?![\d])", hedef):
                yalniz.append((ad, v + " " + b))
            else:
                yok.append((ad, v + " " + b))
    return yok, yalniz


if __name__ == "__main__":
    etiketler = [(os.path.basename(f), dizgiler(open(os.path.join(KOK, f), encoding="utf-8").read())) for f in SEKILLER]
    hedef = metin()
    if "--sina" in sys.argv:
        etiketler.append(("SINA-F1", "slipstream boundary 0.67 m → 0.47 m tip b/2 = 1.73 m"))
    yok, yalniz = denetle(etiketler, hedef)
    print("=== v8 SEKIL SAYISI DENETIMI (%d betik) ===" % len(SEKILLER))
    for ad, s in yalniz:
        print("  ?? %s: '%s' -- deger var, bu birimle yok; insan okusun" % (ad, s))
    for ad, s in yok:
        print("  !! %s: '%s' -- govdede ve ekte yok" % (ad, s))
    if "--sina" in sys.argv:
        yakaladi = any(a == "SINA-F1" for a, _ in yok + yalniz)
        print("  %s  --sina: F1 geri kondu, denetim %s" % ("ok" if yakaladi else "!!", "yakaladi" if yakaladi else "YAKALAMADI"))
        sys.exit(0 if yakaladi else 1)
    print("  %s  %s" % ("ok" if not yok else "!!", "her birimli sekil sayisi govdede ya da ekte" if not yok else "%d sayi yok" % len(yok)))
    sys.exit(1 if yok else 0)
