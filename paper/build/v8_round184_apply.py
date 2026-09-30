# -*- coding: utf-8 -*-
"""Tur 184: 4. asama, 2.3 -- yazarin karari E20 (B + cumle 11).
A (besimiz): 10 C (-> 5, 8-9), 38 C (-> 2.1 tilt satiri / 2.1.6 govde cumlesi), 41 ses.
Yazar: 11 S (ChatGPT vetosu yazarca gecildi), 16-17 S (karsi-kume + korunan "None is known"), 31-32 S (korunan kaynak cumlesi + alinti).
Kullanim: python3 v8_round184_apply.py KOK
Degisen eski paragraflar ekin S4 bolumune aynen gider; kalkan korunan satirlar v8-caveats.md alt tablosuna E20 ile."""
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


# ---------------- 2.3 (Adim 4)
rep(4, " Section 2 predicts the charge and the amplification; **it does not prove that the credit must lose.** A dedicated lift system "
       "raises the empty-mass fraction and may lower the energy fraction at the same time, and which wins is a closure result rather than a "
       "consequence of the accounting.", "")                                   # 10 C, 11 S (yazar)
rep(4, " **The counter-set is therefore a common-mission sizing study at longer range in which a dedicated-lift configuration is both more "
       "efficient and no heavier than one without.** None is known to the authors.", "")   # 16-17 S (yazar)
rep(4, " **And the source states the second half of the prediction in its own words, on a comparison the check does not use as its test.** "
       "Discussing why the all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high cruise efficiency "
       "of the lift-plus-cruise type reduces battery weight compared with a quadrotor, *\"but not enough to counter the increase in structure "
       "and propulsion weight.\"*", "")                                          # 31-32 S (yazar)
rep(4, " The tilt-wing does not escape the accounting by avoiding the mass charge; it *moves* the cost — to the mechanism that reorients its "
       "propulsors (Section 2).", "")                                          # 38 C
rep(4, " That is the whole of it.", "")                                        # 41 ses
TAS = [(4, "None is known to the authors", 4), (4, "And the source states the second half", 4), (4, "but not enough to counter", 4)]

# ---------------- Ek: degisen eski paragraflar, aynen
sp = os.path.join(root, 'paper/v8/supplement.md'); S = open(sp, encoding='utf-8').read()
def norm(x): return re.sub(r"\s+", " ", x).strip()
toplam = 0
for n in sorted(ESKI):
    yeni = set(norm(p) for p in paras(split(n)[3]))
    gid = [p for p in ESKI[n] if norm(p) not in yeni and not p.startswith('#')]
    if not gid: continue
    toplam += len(gid)
    blok = ("### Section %d's paragraphs as they stood before the Round 184 shortening\n\n"
            "Each paragraph below was shortened in Round 184 (stage 4, the author's decision E20 on Section 2.3); it is given here in full, "
            "verbatim. The protected sentences moved here by that decision are among them: the counter-set and *\"None is known to the "
            "authors\"*, and the source's own statement with its quotation.\n\n" % n + "\n\n".join(gid) + "\n\n---\n\n")
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
    ek.append("| S%d | %s | E20 |" % (sn, m.group(1)))
last = list(re.finditer(r"^\| S\d+ \| .* \| E\d+ \|$", C, re.M))[-1]
C = C[:last.end()] + "\n" + "\n".join(ek) + C[last.end():]
open(cp, 'w', encoding='utf-8').write(C)
print("ok; eke giden paragraf:", toplam, "; kayittan eke:", len(ek))
