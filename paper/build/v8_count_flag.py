# -*- coding: utf-8 -*-
"""Sayim isareti (Tur 157; ChatGPT'nin onerisi, dort okuyucu + Claude; Tur 95 kuralinin mekanik hali).

Bir commit'e gore kisalan her paragrafta, KALAN metindeki sayma/sira sozcuklerini (first, second, third,
the former, the latter, both, two, three, four, these ...) ve silinen parcayi listeler. Yalniz ISARETTIR:
hicbir seyi durdurmaz; sayimin hala dogru olup olmadigini insan okur.

  python3 paper/build/v8_count_flag.py BASE      (BASE: kesimden onceki commit)
  --sina: K-9 hatasini (Bolum 4'un sabit hatve cumlesinin silinmesi) bellekte geri koyar, isaretin ciktigini sinar.
"""
import difflib, glob, os, re, subprocess, sys
KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SAYIM = re.compile(r"\b(first|second|third|fourth|fifth|former|latter|both|two|three|four|five|six|these|the others?|last of these)\b", re.I)


def govde(s):
    m = re.search(r"^## (?!Yazar)", s, re.M); e = re.search(r"^## Yazarın denetimi", s, re.M)
    return s[m.start() if m else 0:e.start() if e else len(s)]


def paragraflar(s):
    return [" ".join(p.split()) for p in re.split(r"\n\s*\n", govde(s)) if p.strip()]


def isaretler(eski, yeni):
    out = []
    ye = paragraflar(yeni)
    for p in paragraflar(eski):
        if p in ye:
            continue
        aday = max(ye, key=lambda q: difflib.SequenceMatcher(None, p, q).ratio(), default="")
        if difflib.SequenceMatcher(None, p, aday).ratio() < 0.5:
            continue                                      # paragraf tasindi ya da tamamen cikti; baska denetimin isi
        pw, aw = p.split(), aday.split()
        silinen = [" ".join(pw[a:b]) for op, a, b, _, _ in difflib.SequenceMatcher(None, pw, aw, autojunk=False).get_opcodes() if op in ("delete", "replace")]
        kalan = sorted(set(m.group(0).lower() for m in SAYIM.finditer(aday)))
        if kalan:
            out.append((aday[:90], kalan, [x.strip() for x in silinen if len(x.strip()) > 3]))
    return out


if __name__ == "__main__":
    base = [a for a in sys.argv[1:] if not a.startswith("--")][0]
    toplam = 0
    for f in sorted(glob.glob(os.path.join(KOK, "paper", "v8", "[0-9][0-9]-*.md"))):
        yol = os.path.relpath(f, KOK)
        eski = subprocess.run(["git", "-C", KOK, "show", "%s:%s" % (base, yol)], capture_output=True, text=True).stdout
        yeni = open(f, encoding="utf-8").read()
        if "--sina" in sys.argv:                          # yalniz K-9 silmesi: tabandaki metinden tek cumle cikar
            if not yol.startswith("paper/v8/06-"):
                continue
            yeni = re.sub(r"And the\s+fixed-pitch propeller that serves both regimes is the reason the margin above sits where it does\s+rather than higher\. ", "", eski)
        for bas, kalan, silinen in isaretler(eski, yeni):
            toplam += 1
            print("  ?? %s | kalan sayim sozcukleri: %s\n     paragraf: %s ...\n     silinen: %s" % (yol[9:11], ", ".join(kalan), bas, " / ".join(s[:80] for s in silinen)))
    if "--sina" in sys.argv:
        print("SINAMA: K-9 silmesi %s" % ("isaretlendi" if toplam else "ISARETLENMEDI -- denetim kor"))
    else:
        print("  %d paragraf insan okumasina isaretlendi (durdurmaz)." % toplam)
