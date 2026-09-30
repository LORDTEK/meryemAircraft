# -*- coding: utf-8 -*-
"""Tur 191: son okumanin onarimlari -- D1 (4.1 R-2, besimiz), D2 (1.3 korunan, yazar E24: "the only ones"), satir 0 (2.2 "priced" -> "analyses ... without pricing it", besimiz).
Kullanim: python3 v8_round191_apply.py KOK"""
import re, sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
root = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else "."
SEC = set()
if '--s' in sys.argv:
    v = sys.argv[sys.argv.index('--s') + 1]
    SEC = set('abcdefghijk') if v == 'all' else set(v.split(','))
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




rep(6, "On this axis the alternative is the rotorcraft, multirotor and helicopter alike, and as in the previous section",
       "On this axis the alternative is the rotorcraft — multirotor and helicopter alike — and as in the previous section")      # D1
rep(1, "they are the only one of those documented obstacles an uncrewed aircraft removes",
       "they are the only ones of those documented obstacles an uncrewed aircraft removes")                                        # D2 (E24)
rep(3, "that is not one of the three charges, and it is priced where the transition is analysed.",
       "that is not one of the three charges, and Section 10 analyses the transition without pricing it.")                         # satir 0

cp = os.path.join(root, 'paper/v8-caveats.md'); C = open(cp, encoding='utf-8').read()
a = "| 1 | they are the only one of those documented obstacles an uncrewed aircraft removes | Q |"
assert C.count(a) == 1
C = C.replace(a, "| 1 | they are the only ones of those documented obstacles an uncrewed aircraft removes | Q (E24) |")
open(cp, 'w', encoding='utf-8').write(C)

sp = os.path.join(root, 'paper/v8/supplement.md'); S = open(sp, encoding='utf-8').read()
def norm(x): return re.sub(r"\s+", " ", x).strip()
toplam = 0
for n in sorted(ESKI):
    yeni = set(norm(p) for p in paras(split(n)[3]))
    gid = [p for p in ESKI[n] if norm(p) not in yeni and not p.startswith('#')]
    if not gid: continue
    toplam += len(gid)
    blok = ("### Section %d's paragraphs as they stood before the Round 191 repairs\n\n"
            "Each paragraph below was repaired in Round 191 (the last part–whole–part reading: defects only, not length); it is given here "
            "in full, verbatim.\n\n" % n + "\n\n".join(gid) + "\n\n---\n\n")
    m = re.search(r"^## S%d\. .*$" % n, S, re.M); assert m, n
    nx = re.search(r"^## S\d+\. ", S[m.end():], re.M)
    at = m.end() + nx.start() if nx else len(S)
    S = S[:at] + blok + S[at:]
open(sp, 'w', encoding='utf-8').write(S)
print("ok; eke giden paragraf:", toplam)
