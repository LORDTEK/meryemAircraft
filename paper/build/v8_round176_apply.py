# -*- coding: utf-8 -*-
"""Tur 176: Bolum 1'in son gecisi -- yazar (Tur 175 sonrasi): "Bolum 1 icin tamamina bak ... son kez yapiyoruz gibi dusunerek ne
oluyorsa artik yap gec." Yalniz korunmayan tekrar; iki kesim yazarca onaylandi.

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

# ---------------- Katman 1
# 1.1 -- "both capabilities are wanted at once" cumlenin basinda soylendi
rep(1, " — and both want to leave from an unprepared site and then cover distance", "")
# 1.2 -- NASA calismasinin tek evi 2.3; rotalar burada adlandirilir (R10)
rep(1, "The NASA sizing study used in Section 4 describes the two routes they take between the regimes:",
       "They take two routes between the regimes:")
# 1.3 -- yazar onayi
rep(1, " It is neither new nor untried nor abandoned.", "")
# 1.5 -- 1.4'un tepki torku paragrafinin tekrari; R11
rep(1, " A quadrotor tail-sitter produces a rolling moment from the reaction torque of four independently driven rotors; a coaxial pair "
       "can produce one the same way, by running its two rotors at different speeds. **Operating every pair torque-balanced spends that "
       "channel to buy",
       " **Operating every pair torque-balanced spends the reaction-torque channel to buy")
# 1.5 -- yazar onayi; 2.1'in korunan acilisi ayni seyi soyluyor
del_para(1, "Section 2 states the cost that any architecture in this corner pays")

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
    blok = ("### Section %d's paragraphs as they stood before the Round 176 shortening\n\n"
            "Each paragraph below was shortened or moved in Round 176 (Section 1, the last pass; the author's decision); it is given here "
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
