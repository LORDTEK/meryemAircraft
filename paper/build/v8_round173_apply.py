# -*- coding: utf-8 -*-
"""Tur 173 taslagi: Bolum 2 (cerceve) -- yazarin karari (Tur 172 sonrasi: "Bolum 2 olsun"). Katman 1 korunmayan tekrar/calisma
(okuyucu teyidi); katman 2 korunan cumleler (yazarin karari, E16).

Kullanim: python3 v8_round172_apply.py KOK [--s a,b,c ...]   (--s verilmezse yalniz katman 1 uygulanir; --s all hepsi)
Degisen eski paragraflar ekin adim bolumune aynen gider; S/C ile kalkan korunan satirlar v8-caveats.md alt tablosuna E16 ile."""
import re, sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
root = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else "."
SEC = set()
if '--s' in sys.argv:
    v = sys.argv[sys.argv.index('--s') + 1]
    SEC = set('ab') if v == 'all' else set(v.split(','))
YAZ = "## Yazarın denetimi"

def path(n): return glob.glob(os.path.join(root, 'paper/v8/%02d-*.md' % n))[0]
def split(n):
    s = open(path(n), encoding='utf-8').read()
    m = re.search(r"^## (?!Yazar)", s, re.M); e = s.index(YAZ)
    body = s[m.start():e]
    tail = re.search(r"\n---\s*\n\s*$", body)
    core = body[:tail.start()] if tail else body.rstrip()
    return s, m.start(), e, core, body[len(core):]
def write(n, s, st, en, core, rest):
    core = re.sub(r"\n{3,}", "\n\n", core)
    core = re.sub(r"[ \t]+\n", "\n", core)          # silmeden kalan satir sonu bosluklari
    core = re.sub(r"(\n\n)[ \t]{1,3}(?=\S)", r"\1", core)  # 4+ bosluk kod blogudur, dokunulmaz  # silmeden kalan paragraf basi bosluklari
    core = re.sub(r"(?<=\S)  +(?=\S)", " ", core)     # silmeden kalan cift bosluk
    open(path(n), 'w', encoding='utf-8').write(s[:st] + core + rest + s[en:])
def paras(txt): return [p.strip() for p in re.split(r"\n\s*\n", txt) if p.strip()]
ESKI = {}
def remember(n):
    if n not in ESKI: ESKI[n] = paras(split(n)[3])
def rep(n, a, b):
    remember(n)
    s, st, en, core, rest = split(n)
    rx = r'\s+'.join(re.escape(w) for w in a.split())
    m = list(re.finditer(rx, core)); assert len(m) == 1, (n, a[:60], len(m))
    core = core[:m[0].start()] + b + core[m[0].end():]
    write(n, s, st, en, core, rest)
def del_para(n, start):
    remember(n)
    s, st, en, core, rest = split(n)
    ps = re.split(r"(\n\s*\n)", core)
    hit = [i for i, p in enumerate(ps) if p.strip().startswith(start)]
    assert len(hit) == 1, (n, start, len(hit))
    ps[hit[0]] = ''
    write(n, s, st, en, ''.join(ps), rest)

# ---------------- Katman 1: korunmayan tekrar ve calisma (okuyucu teyidi)
# 2.1.2 -- yol haritasi; 2.1'in son paragrafi ayni soruyu bir sonraki bolume yollar
rep(2, " Whether any architecture avoids the mismatch — and what it pays instead — is the subject of the next section, and it is not "
       "settled here.", "")
# 2.1.3 -- ussun olcek kuralina bagli oldugu notu eke (S2)
rep(2, " *(The exponent is a property of the scaling rule chosen: holding disc loading constant instead makes hover power grow linearly "
       "with weight, and Section 12 uses that.)*", "")
# 2.1.6 -- korunan "is the origin of all three charges below" (2.1.2) ve tablo basliginin tekrari
rep(2, "The mismatch of the root is the origin of all three charges; each charge is one specific payment",
       "Each charge is one specific payment")
rep(2, " A remedy's own cost can fall in kilograms, drag counts or installed kilowatts without being one of the three charges, and the "
       "table names such a cost in words rather than by a bill's number.", "")
# 2.1.6 -- tilt satirinin tekrari; R4
rep(2, "**One row pays part of its cost in none of the three currencies, and that is not an oversight.** What a tilting architecture buys "
       "its unified propulsion group with is a mechanism — a pivot, an actuator, the gyroscopic coupling of a reorienting mass, and a "
       "control problem through the turn. The pivot and the actuator are paid in kilograms, although they are not lift-subsystem mass; "
       "the coupling and the control problem are paid in none of the three. That part is a cost, but it is not one of the three charges "
       "this accounting tracks.",
       "**One row pays part of its cost in none of the three currencies, and that is not an oversight**: the tilting row's gyroscopic "
       "coupling and transition control problem are costs, but not charges this accounting tracks.")
# 2.1.7 -- ongorudeki basabas noktasinin aciklamasi
rep(2, " break even, where the mass difference as the contract counts it and the cruise-efficiency difference cancel in the range.**",
       " break even.**")
# 2.1.7 -- "It" ile baslayan ongoru cumlesi, tilt paragrafi eke giderse oznesiz kalir; R5 (a'dan bagimsiz, acik ozne)
rep(2, "It also makes a prediction that can be checked", "The accounting also makes a prediction that can be checked")
# 2.2.3 -- sayim tekrari
rep(3, " The first three come from the first three departures; the fourth comes from the fourth.", "")

# ---------------- Katman 2: korunan cumleler (yazarin karari)
TAS = []
if 'a' in SEC:   # S -> S2: tilt satirinin testi (D4'u yeniden acar) + onculu "no worse" ayrintilari (P71)
    rep(2, " A charge that architecture already paid, left no larger, is no worse. A charge it did not pay, imposed by the move, is "
           "worse; so is one it paid, enlarged by it.", "")
    del_para(2, "**The tilting row needs both clarifications.**")
    TAS.append((2, "If that architecture already sizes its continuous plant by the hover peak", 2))
if 'b' in SEC:   # C -- ayni paragrafta "but it is not thereby exempt from being counted"
    rep(2, " **A framework that could absorb any cost by declaring it out-of-scope would be unfalsifiable**, so the costs outside the "
           "three are listed, not waved away.", "")
    TAS.append((2, "A framework that could absorb any cost", 2))

# ---------------- Ek: degisen eski paragraflar, aynen
sp = os.path.join(root, 'paper/v8/supplement.md'); S = open(sp, encoding='utf-8').read()
def norm(x): return re.sub(r"\s+", " ", x).strip()
toplam = 0
for n in sorted(ESKI):
    yeni = set(norm(p) for p in paras(split(n)[3]))
    gid = [p for p in ESKI[n] if norm(p) not in yeni and not p.startswith('#')]
    if not gid: continue
    toplam += len(gid)
    blok = ("### Section %d's paragraphs as they stood before the Round 173 shortening\n\n"
            "Each paragraph below was shortened or moved in Round 173 (Section 2, the framework; the author's decision); it is given here "
            "in full, verbatim. Protected sentences moved here by the author's decision (E16) are among them.\n\n" % n + "\n\n".join(gid) + "\n\n---\n\n")
    m = re.search(r"^## S%d\. .*$" % n, S, re.M); assert m, n
    nx = re.search(r"^## S\d+\. ", S[m.end():], re.M)
    at = m.end() + nx.start() if nx else len(S)
    S = S[:at] + blok + S[at:]
open(sp, 'w', encoding='utf-8').write(S)

# ---------------- Korunan cumle kaydi
cp = os.path.join(root, 'paper/v8-caveats.md'); C = open(cp, encoding='utf-8').read()
ek = []
for n, bas, sn in TAS:
    m = re.search(r"^\| %d \| (%s[^|]*) \| [GDCQK+]+ \|\n" % (n, re.escape(bas)), C, re.M | re.I); assert m, bas
    C = C[:m.start()] + C[m.end():]
    ek.append("| S%d | %s | E16 |" % (sn, m.group(1)))
if ek:
    last = list(re.finditer(r"^\| S\d+ \| .* \| E\d+ \|$", C, re.M))[-1]
    C = C[:last.end()] + "\n" + "\n".join(ek) + C[last.end():]
    open(cp, 'w', encoding='utf-8').write(C)
print("ok; eke giden paragraf:", toplam, "; kayittan eke:", len(ek))
