# -*- coding: utf-8 -*-
"""Tur 175 taslagi: 5.1 -- Grok, ChatGPT, Qwen (Tur 174); yazarin Tur 168 notu ("daralir bu 5.1", "cok sorun edilmis bu govdeyi
dondurmek"). Yalniz korunmayan tekrar; korunan cumleye dokunulmaz, mimarinin sinirlari yerinde kalir.

Kullanim: python3 v8_round172_apply.py KOK [--s a,b,c ...]   (--s verilmezse yalniz katman 1 uygulanir; --s all hepsi)
Degisen eski paragraflar ekin adim bolumune aynen gider; S/C ile kalkan korunan satirlar v8-caveats.md alt tablosuna E17 ile."""
import re, sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
root = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else "."
SEC = set()
if '--s' in sys.argv:
    v = sys.argv[sys.argv.index('--s') + 1]
    SEC = set('a') if v == 'all' else set(v.split(','))
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

# ---------------- Katman 1 (okuyucu teyidi)
# 5.1 -- rota cumlesi: tilt-wing'in bedel listesi hemen asagidaki mekanizma tablosunun ve 1.2'nin tekrari
rep(7, ", which takes a pivot and actuators and brings a gyroscopic moment and a control problem through the turn.", ".")
# 5.1 -- tutum: 5.2.5'in tekrari; ayni paragrafin ikinci cumlesi (kalkis payi, "dedicated lift system" siniri) tablonun yaninda kalir
rep(7, "Attitude comes from differential thrust between the fixed-pitch pairs: the moment arms of the four tip pairs give pitch and yaw. ", "")
# 5.1 -- sabit hatve bedeli: 2.2.4'un altinci maddesi ve 6.2.3 soyluyor
rep(7, " A fixed-pitch blade that serves both regimes is at its best in neither; that is a price of refusing the variable-pitch hub, "
       "charged in Section 11.", "")
# 5.1 -- gecis: nedenin ayrintisi 4.7 ve 6.1.4'te; R9
rep(7, "**: whether the moment available suffices, and whether the aircraft trims through the rotation, depend on aerodynamics that the "
       "methods used here do not predict reliably in the band the rotation passes through (Section 6).",
       "**: the aerodynamics of the rotation are not predicted reliably here (Sections 6 and 10).")

TAS = []

# ---------------- Ek: degisen eski paragraflar, aynen
sp = os.path.join(root, 'paper/v8/supplement.md'); S = open(sp, encoding='utf-8').read()
def norm(x): return re.sub(r"\s+", " ", x).strip()
toplam = 0
for n in sorted(ESKI):
    yeni = set(norm(p) for p in paras(split(n)[3]))
    gid = [p for p in ESKI[n] if norm(p) not in yeni and not p.startswith('#')]
    if not gid: continue
    toplam += len(gid)
    blok = ("### Section %d's paragraphs as they stood before the Round 175 shortening\n\n"
            "Each paragraph below was shortened or moved in Round 175 (Section 5.1; the readers' proposal and the author's Round 168 note); it is given here "
            "in full, verbatim. Protected sentences moved here by the author's decision (none this round) are among them.\n\n" % n + "\n\n".join(gid) + "\n\n---\n\n")
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
    ek.append("| S%d | %s | E18 |" % (sn, m.group(1)))
if ek:
    last = list(re.finditer(r"^\| S\d+ \| .* \| E\d+ \|$", C, re.M))[-1]
    C = C[:last.end()] + "\n" + "\n".join(ek) + C[last.end():]
    open(cp, 'w', encoding='utf-8').write(C)
print("ok; eke giden paragraf:", toplam, "; kayittan eke:", len(ek))
