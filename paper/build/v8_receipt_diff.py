# -*- coding: utf-8 -*-
"""Alindi denetimi farki (Tur 150, asama kapanis kapisi): bugunku gövdedeki isaretci cumlelerini Tur 130 denetim
tablosuyla karsilastirir; eslesmeyen (yeni ya da degisen) cumleler INSAN OKUSUN diye listelenir."""
import re, glob, os

KOK = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def govde(n):
    f = glob.glob(os.path.join(KOK, "paper", "v8", "%02d-*.md" % n))[0]
    s = open(f, encoding="utf-8").read()
    m = re.search(r"^## (?!Yazar)", s, re.M)
    t = re.search(r"^## Yazarın denetimi", s, re.M)
    return s[m.start():t.start() if t else len(s)]


def norm(x):
    return re.sub(r"\s+", " ", re.sub(r"[*_]", "", x)).strip()


aud = open(os.path.join(KOK, "paper/v8/drafts/receipt-audit.md"), encoding="utf-8").read()
starts = [norm(m.group(1)).rstrip("…")[:45] for m in re.finditer(r"^\| \d+ \| \d+ \| (.+?) \|", aud, re.M)]
PAT = re.compile(r"Sections? \d|Supplement S\d|next section|previous section|last section")
new, tot = [], 0
for n in range(1, 16):
    b = norm(govde(n))
    for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(\"])", b):
        if PAT.search(s):
            tot += 1
            if not any(s.startswith(st) or st in s for st in starts):
                new.append((n, s))
print("pointer sentences now:", tot, " audited rows:", len(starts), " not matched:", len(new))
for n, s in new:
    print(n, "|", s[:260])
