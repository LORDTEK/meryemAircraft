# -*- coding: utf-8 -*-
"""Tur 170: yazarin alt bolum notlari uzerine hemfikir olunan islemler + yazarin S kararlari (E13).
Eski paragraflar ekin kendi bolumune aynen gider. Kullanim: python3 v8_round170_apply.py KOK"""
import re, sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v8_round170_texts as T
root = sys.argv[1] if len(sys.argv) > 1 else "."
YAZ = "## Yazarın denetimi"

def path(n): return glob.glob(os.path.join(root, 'paper/v8/%02d-*.md' % n))[0]
def split(n):
    s = open(path(n), encoding='utf-8').read()
    m = re.search(r"^## (?!Yazar)", s, re.M); e = s.index(YAZ)
    body = s[m.start():e]
    tail = re.search(r"\n---\s*\n\s*$", body)
    core = body[:tail.start()] if tail else body.rstrip()
    rest = body[len(core):]
    return s, m.start(), e, core, rest
def write(n, s, st, en, core, rest):
    open(path(n), 'w', encoding='utf-8').write(s[:st] + core + rest + s[en:])

def paras(txt): return [p.strip() for p in re.split(r"\n\s*\n", txt) if p.strip()]
ESKI = {}
def remember(n):
    if n not in ESKI:
        ESKI[n] = paras(split(n)[3])

def sub_bounds(core, heading):
    m = re.search(r"^### " + re.escape(heading) + r".*$", core, re.M)
    assert m, heading
    a = m.end()
    nx = re.search(r"^### ", core[a:], re.M)
    b = a + nx.start() if nx else len(core)
    return a, b
def tables_of(block):
    lines = block.split('\n'); out = []; i = 0
    grab = []
    while i < len(lines):
        if lines[i].lstrip().startswith('|'):
            t = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                t.append(lines[i]); i += 1
            # tablonun hemen ardindaki italik not
            j = i
            while j < len(lines) and not lines[j].strip(): j += 1
            if j < len(lines) and lines[j].lstrip().startswith('*') and not lines[j].lstrip().startswith('**'):   # yalniz italik not (Tur 170: kalin paragraf not sanilmisti)
                k = j; note = []
                while k < len(lines) and lines[k].strip():
                    note.append(lines[k]); k += 1
                t += [''] + note; i = k
            grab.append('\n'.join(t))
        else:
            i += 1
    return grab
def rep_sub(n, heading, new):
    remember(n)
    s, st, en, core, rest = split(n)
    a, b = sub_bounds(core, heading)
    old = core[a:b]
    if '{TABLE}' in new:
        tb = tables_of(old); assert len(tb) == 1, (n, heading, len(tb))
        new = new.replace('{TABLE}', tb[0])
    core = core[:a] + '\n\n' + new.strip() + '\n\n' + core[b:].lstrip('\n')
    write(n, s, st, en, core, rest)
def rep_intro(n, new, whole=False):
    remember(n)
    s, st, en, core, rest = split(n)
    h = re.match(r"## .*\n", core); a = h.end()
    nx = re.search(r"^### ", core[a:], re.M)
    b = len(core) if (whole or not nx) else a + nx.start()
    old = core[a:b]
    if '{TABLE}' in new:
        tb = tables_of(old); assert len(tb) == 1, (n, len(tb))
        new = new.replace('{TABLE}', tb[0])
    core = core[:a] + '\n' + new.strip() + '\n\n' + core[b:].lstrip('\n')
    write(n, s, st, en, core.rstrip() + '\n', rest)
def rep_para(n, start, new):
    remember(n)
    s, st, en, core, rest = split(n)
    ps = re.split(r"(\n\s*\n)", core)
    hit = [i for i, p in enumerate(ps) if p.strip().startswith(start)]
    assert len(hit) == 1, (n, start, len(hit))
    ps[hit[0]] = new.strip()
    write(n, s, st, en, ''.join(ps), rest)
def rep_exact(n, a, b):
    remember(n)
    s, st, en, core, rest = split(n)
    rx = r'\s+'.join(re.escape(w) for w in a.split())
    m = list(re.finditer(rx, core)); assert len(m) == 1, (n, a[:50], len(m))
    core = core[:m[0].start()] + b + core[m[0].end():]
    write(n, s, st, en, core, rest)

# --- Adim 1 (Bolum 1)
rep_sub(1, "What the contemporary answers do", T.S1_ANSWERS)
rep_para(1, "There is a third way", T.S1_THIRD_P1)
rep_para(1, "Three things are available now", T.S1_THIRD_P3)
rep_sub(1, "What is already occupied", T.S1_OCCUPIED)
# --- Adim 2 (2.1.6): geri cekme ornegi + korunan +5 m/s -> S2 (E13)
rep_para(2, "**One of these transfers has direct experimental support.**", T.S2_RETRACTION_NEW)
# --- Adim 3 (2.2.4)
rep_sub(3, "What the condition does not say", T.S3_DOESNOT)
# --- Adim 4 (2.3): quadrotor ve olcek cumlesi -> S4 (E13)
rep_exact(4, "Three of the nine designs matter here. The turboshaft quadrotor reaches an effective lift-to-drag ratio of 4.9 at a design gross weight of 3 678 lb, with no dedicated lift group: its rotors serve both regimes.", "Two of the nine designs matter here.")
rep_exact(4, " **The quadrotor is reported for scale, and the isolation test above is what carries the prediction**: against it the lift-plus-cruise design changes three things at once, and the contrast is in Supplement S4.", "")
rep_exact(4, "compared with the quadrotor,", "compared with a quadrotor,")
# --- Adim 5 (3.4)
rep_sub(5, "What is sized, and what is not demonstrated", T.S5_SIZED)
# --- Adim 6 (4.4-4.8); "Whether 0.683 ..." ve "1 660 to 3 275 kg" -> S6 (E13)
rep_sub(6, "What the margin actually is", T.S6_MARGIN)
rep_sub(6, "What the comparison gives", T.S6_COMPARISON)
rep_sub(6, "Five qualifications", T.S6_FIVE)
rep_sub(6, "What is sized, and what is not demonstrated", T.S6_SIZED)
rep_sub(6, "What this half costs", T.S6_COSTS)
# --- Adim 7 (5.1)
rep_intro(7, T.S7_BODY, whole=True)
# --- Adim 8 (5.2)
rep_sub(8, "The airframe", T.S8_AIRFRAME)
rep_sub(8, "The propulsion", T.S8_PROPULSION)
rep_sub(8, "What produces each moment", T.S8_MOMENTS)
rep_sub(8, "What meets the ground", T.S8_GROUND)
rep_sub(8, "What moves", T.S8_MOVES)
rep_sub(8, "What this inventory does not settle", T.S8_NOTSETTLE)
# --- Adim 10 (6.1)
rep_sub(10, "The inputs, and why", T.S10_INPUTS)
rep_sub(10, "The four closures", T.S10_CLOSURES)
rep_sub(10, "The transition", T.S10_TRANSITION)
# --- Adim 11 (6.2)
rep_intro(11, T.S11_INTRO)
rep_sub(11, "Bill 2 — the drag of hover hardware", T.S11_BILL2)
# --- Adim 12 (6.3)
rep_intro(12, T.S12_BODY, whole=True)
# --- Adim 13 (6.4)
rep_intro(13, T.S13_INTRO)
rep_sub(13, "Three contracts, and what each holds equal", T.S13_CONTRACTS)
rep_sub(13, "What is compared, and on what basis", T.S13_BASIS)
rep_sub(13, "Section 2's prediction, tested", T.S13_PREDICTION)
# --- Adim 14 (7.2)
rep_sub(14, "First, the known obstacle: the energy store", T.S14_STORE)

# --- Ek: degisen eski paragraflar, adimin ek bolumune, aynen
sp = os.path.join(root, 'paper/v8/supplement.md'); S = open(sp, encoding='utf-8').read()
def norm(x): return re.sub(r"\s+", " ", x).strip()
toplam = 0
for n in sorted(ESKI):
    yeni = set(norm(p) for p in paras(split(n)[3]))
    gid = [p for p in ESKI[n] if norm(p) not in yeni and not p.startswith('#')]
    if not gid: continue
    toplam += len(gid)
    blok = ("### Section %d's paragraphs as they stood before the Round 170 shortening\n\n"
            "Each paragraph below was shortened, rewritten or moved in Round 170, on the author's subsection notes (Round 168) and the readers' "
            "agreed operations (Rounds 168–169); it is given here in full, verbatim. The protected sentences moved here by the author's decision "
            "(E13) are among them.\n\n" % n + "\n\n".join(gid) + "\n\n---\n\n")
    m = re.search(r"^## S%d\. .*$" % n, S, re.M); assert m, n
    nx = re.search(r"^## S\d+\. ", S[m.end():], re.M)
    at = m.end() + nx.start() if nx else len(S)
    S = S[:at] + blok + S[at:]
open(sp, 'w', encoding='utf-8').write(S)

# --- Korunan cumle kaydi: E13 tasimalari
cp = os.path.join(root, 'paper/v8-caveats.md'); C = open(cp, encoding='utf-8').read()
TAS = [(2, "The same work finds the retraction's advantage elsewhere"), (6, "Whether 0.683 is the blade"),
       (4, "The quadrotor is reported for scale"), (6, "The compared vehicles are 1 660 to 3 275 kg")]
ek = []
for n, bas in TAS:
    m = re.search(r"^\| %d \| (%s[^|]*) \| [GDCQK+]+ \|\n" % (n, re.escape(bas)), C, re.M); assert m, bas
    C = C[:m.start()] + C[m.end():]
    ek.append("| S%d | %s | E13 |" % (n, m.group(1)))
last = list(re.finditer(r"^\| S\d+ \| .* \| E\d+ \|$", C, re.M))[-1]
C = C[:last.end()] + "\n" + "\n".join(ek) + C[last.end():]
open(cp, 'w', encoding='utf-8').write(C)
print("ok; eke giden paragraf:", toplam)
