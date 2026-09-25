# -*- coding: utf-8 -*-
"""Tablo / satir atiflari denetimi (Tur 86; DeepSeek'in onerisi, S-7'den).

Adim govdelerinde "table", "tables", "table's", "row", "rows" geçen her cumle listelenir ve
paper/v8-refs-reviewed.md'deki GOZDEN GECIRILMIS listeyle karsilastirilir. Listede olmayan
(yeni ya da degismis) her atif basilir ve cikis kodu 1 olur: bir insan / okuyucu onun hangi
tabloya isaret ettigine bakmadan gecilmez. Bir tablo eke tasindiginda bu betik kosulur.
Geniş ilişkisel adlar (the inversion, the condition, the fourth ...) bu betigin DISINDA,
kor okumada elle denetlenir (Tur 86 karari: iki katman).
--sina: Adim 3 govdesine bellekte bayat bir atif ekleyip yakalandigini sinar.
"""
import glob, os, re, sys
KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V8 = os.path.join(KOK, "paper", "v8")
ATIF = re.compile(r"\b(tables?|table's|rows?)\b", re.I)


def duz(x):
    return re.sub(r"\s+", " ", x.replace("*", "")).strip()


def govde(n):
    s = open(glob.glob(os.path.join(V8, "%02d-*.md" % n))[0], encoding="utf-8").read()
    m = re.search(r"^## (?!Yazar)", s, re.M); e = re.search(r"^## Yazarın denetimi", s, re.M)
    return s[m.start():e.start() if e else len(s)]


def atiflar(b):
    out = []
    for p in re.split(r"\n\s*\n", b):
        if p.lstrip().startswith("|"):
            continue
        for c in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", duz(p)):
            if ATIF.search(c):
                out.append(c)
    return out


gozden = []
for L in open(os.path.join(KOK, "paper", "v8-refs-reviewed.md"), encoding="utf-8"):
    m = re.match(r"^\| (\d+) \| (.+?) \| (.+?) \| (.+?) \|$", L.strip())
    if m and m.group(1).isdigit():
        gozden.append((int(m.group(1)), duz(m.group(2))))

yeni = []
for n in range(1, 16):
    b = govde(n)
    if "--sina" in sys.argv and n == 3:
        b += "\n\nThe table's last row permits nothing.\n"
    for c in atiflar(b):
        if not any(n == a and c.startswith(p) for a, p in gozden):
            yeni.append((n, c))
print("=== TABLO / SATIR ATIF DENETIMI ===")
for n, c in yeni:
    print("  !! Adim %d, gozden gecirilmemis atif: %s" % (n, c[:120]))
if yeni:
    print("  %d atif gozden gecirilmeli (paper/v8-refs-reviewed.md)." % len(yeni))
    sys.exit(1)
print("  ok  butun tablo/satir atiflari gozden gecirilmis (%d kayit)." % len(gozden))
