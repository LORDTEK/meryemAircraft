# -*- coding: utf-8 -*-
"""paper/v8/ALL-STEPS.md'yi adim dosyalarinin Ingilizce govdelerinden kurar.

Her NN-*.md dosyasindan ilk "## " (Yazar olmayan) baslik ile "## Yazarın denetimi"
arasi alinir; sondaki "---" atilir; govdeler "---" ile birlestirilir. Turkce
basliklar ve denetim tablolari ALL-STEPS'e girmez.
"""
import glob
import os
import re

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V8 = os.path.join(KOK, "paper", "v8")

parcalar = []
for f in sorted(glob.glob(os.path.join(V8, "[0-9][0-9]-*.md"))):
    s = open(f, encoding="utf-8").read()
    m = re.search(r"^## (?!Yazar)", s, re.M)
    t = re.search(r"^## Yazarın denetimi", s, re.M)
    b = s[m.start():t.start() if t else len(s)].rstrip()
    parcalar.append(re.sub(r"\n---\s*$", "", b).rstrip())
metin = "\n\n---\n\n".join(parcalar) + "\n"
open(os.path.join(V8, "ALL-STEPS.md"), "w", encoding="utf-8").write(metin)
print("ALL-STEPS.md: %d adim, %d kelime" % (len(parcalar), len(metin.split())))
