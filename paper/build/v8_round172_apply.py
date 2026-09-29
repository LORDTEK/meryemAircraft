# -*- coding: utf-8 -*-
"""Tur 172 taslagi: Bolum 6 hesap calismasi eke (katman 1, okuyucu teyidi) + korunan cumle S/C listesi (katman 2,
yazarin karari) + 2.2.5 ve 2.3 sadelestirme (yazarin notu, Tur 171 sonrasi).

Kullanim: python3 v8_round172_apply.py KOK [--s a,b,c ...]   (--s verilmezse yalniz katman 1 uygulanir; --s all hepsi)
Degisen eski paragraflar ekin adim bolumune aynen gider; S/C ile kalkan korunan satirlar v8-caveats.md alt tablosuna E15 ile."""
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

# ---------------- Katman 1: korunmayan calisma (okuyucu teyidi)
# 2.2.5 (Adim 3) -- yazar: "Kosuldan ne cikmaz kismini kisaltalim"
rep(3, " Three questions follow from it, and they are answered separately: whether the accounting behind the condition survives contact "
       "with an independent sizing study is tested in the next section, against data this work did not produce; whether any configuration "
       "satisfies the condition is the subject of Sections 5 to 7; and what such a configuration pays instead is the subject of Section 11, "
       "the answer most likely to be wrong.", "")
rep(3, "A tilting architecture accepts the third departure and buys its way out of the first with a mechanism. ", "")
# 2.3 (Adim 4) -- yazar: "bizimle ilgili olan kisimlar olacak sekilde sadelestirsek"
rep(4, "and the payment is amplified: additional empty mass enters through a multiplier that grows as the empty-mass fraction rises, and "
       "the same increment is counted again in hover.", "and the payment is amplified.")
rep(4, "inside a breakdown this work did not produce**: its three reported categories account for 580 lb of the 679 lb empty-weight "
       "difference, and the remaining 99 lb lies in categories it does not break out (Supplement S4).",
       "inside a breakdown this work did not produce** (Supplement S4).")
rep(4, "The tilting family avoids it too — it carries no dedicated lift group, it is the lighter of the two matched designs, and an "
       "independent set says so.", "The tilting family avoids it too.")
# 6.1 (Adim 10)
rep(10, "Wing loading, disc loading and aspect ratio are held fixed, so **the cruise lift coefficient is 0.450 in every closure** "
        "(Supplement S10). ", "")
rep(10, "; the loop holds both factors fixed within each closure, so the closure changes neither.",
        "; the loop holds both factors fixed within each closure.")
rep(10, "**The blade that is best before the loop is still best after it**, though a loop can reverse a local ranking: at both ends of "
        "the drag bracket the higher-efficiency family closes to the longer range — **a result of the closure rather than an assumption "
        "carried into it.**",
        "**The blade that is best before the loop is still best after it** — **a result of the closure rather than an assumption "
        "carried into it.**")
rep(10, ", at the reference rotation times of 2 s for the 50 kg design and 5.1 s for the 1 000 kg one", "")
# 6.2 (Adim 11)
del_para(11, "**Every one of the charges above belongs to one scale**")
# 6.3 (Adim 12)
rep(12, " Either answer leaves the mechanism claim where it was.", "")
rep(12, "**: no closure was run at 1 000 kg, the heavy design has no drag bracket and no structural closure, and no heavy-design range "
        "is quoted (Supplement S12).", "** (Supplement S12).")

# ---------------- Katman 2: korunan cumleler (yazarin karari; C = kopya diye kes, S = sonucuyla eke)
TAS = []   # (adim, kayittaki cumlenin basi, ek bolumu)
if 'a' in SEC:   # C -- 6.4.4 ve 6.4.7 ayni kurali soyluyor
    del_para(10, "Because the comparative result depends on the sizing contract")
    TAS.append((10, "no comparison in this paper should be quoted without the contract", 10))
if 'b' in SEC:   # S -> S10
    rep(10, " **If no fixed point exists, the declared sizing package does not close.**", "")
    TAS.append((10, "If no fixed point exists", 10))
if 'c' in SEC:   # S -> S10
    rep(10, " **The reference design's assumed zero-lift value of 0.0248 is not used**: it lies below both ends of the bracket.", "")
    TAS.append((10, "The reference design's assumed zero-lift value of 0.0248", 10))
if 'd' in SEC:   # S -> S10; anlami bir sonraki cumlenin yan cumlesinde kalir
    rep(10, "The tip frames, tip discs and strip were set on the 50 kg reference design of Section 8, and **the control moment arms of "
            "Section 8 are therefore reference values that this closure does not re-derive.** ", "")
    rep(10, "with anything that depends on the arms carried at the reference geometry.",
            "with anything that depends on the control moment arms carried at the reference geometry of Section 8.")
    TAS.append((10, "the control moment arms of Section 8 are therefore reference values", 10))
if 'e' in SEC:   # C -- ayni paragrafta 5.4-6.6 m cumlesi
    rep(10, " **Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude.**", "")
    TAS.append((10, "Within the finite-moment dynamic model", 10))
if 'f' in SEC:   # C -- "It attributes. It does not add."
    rep(11, " Every cost named below is already inside the closure of Section 10. **No new physical cost term is introduced here.**", "")
    TAS.append((11, "Every cost named below is already inside", 11)); TAS.append((11, "No new physical cost term", 11))
if 'g' in SEC:   # S -> S11 (P71: onculu olan temiz govde sayilariyla birlikte)
    del_para(11, "Without the hub and small items")
    TAS.append((11, "Bill 2 therefore occupies a larger share", 11))
if 'h' in SEC:   # S -> S12
    rep(12, "and both figures are inputs: **a change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it "
            "cannot be offered as evidence that Bill 1 moves with size in either direction.**",
            "and both figures are inputs (Supplement S12).")
    TAS.append((12, "A change from 3.6 to 4.0 percent", 12))
if 'i' in SEC:   # S -> S13; sonucu (duyarlilik) ekte, "Where it falls ... (Supplement S13)" govdede
    rep(13, "With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every closure; with a heavier one "
            "this configuration leads under a fixed take-off mass at every closure; with a common propeller efficiency a reversal appears "
            "at every closure. ", "")
    TAS.append((13, "With a lighter lift group", 13))

if 'j' in SEC:   # B -- 6.3: olcek sinirlari sonuclariyla S12'ye (calismasi zaten orada)
    rep(12, " Bill 2 moved by more than the Bill 3 ratio at every point in the heavy interval and under either engine margin.", "")
    rep(12, " Disc loading is held nearly constant, so specific hover power is held with it: **that near-constancy is a property of the "
            "constant-disc-loading rule, not a finding about Bill 3.** The rule is paid in geometry, and **much above 1 000 kg a single "
            "nose pair can no longer hold the disc loading.**", "")
    rep(12, "Only the rotor term of Bill 2 is computed at both sizes; the frame term enters both designs as the same multiplier. ", "")
    TAS.append((12, "That near-constancy is a property", 12)); TAS.append((12, "Much above 1 000 kg", 12))
if 'k' in SEC:   # B -- 6.3: gecis olcegi sonucuyla S12'ye
    rep(12, " **The transition is where the square–cube relation is paid in full**, and **a larger aircraft of this type turns more "
            "slowly, and must** (Supplement S12).", "")
    TAS.append((12, "A larger aircraft of this type turns more slowly", 12))

# ---------------- Ek: degisen eski paragraflar, aynen
sp = os.path.join(root, 'paper/v8/supplement.md'); S = open(sp, encoding='utf-8').read()
def norm(x): return re.sub(r"\s+", " ", x).strip()
toplam = 0
for n in sorted(ESKI):
    yeni = set(norm(p) for p in paras(split(n)[3]))
    gid = [p for p in ESKI[n] if norm(p) not in yeni and not p.startswith('#')]
    if not gid: continue
    toplam += len(gid)
    blok = ("### Section %d's paragraphs as they stood before the Round 172 shortening\n\n"
            "Each paragraph below was shortened or moved in Round 172 (calculation working to the supplement; the author's notes on "
            "Sections 3 and 4); it is given here in full, verbatim. Protected sentences moved here by the author's decision (E15) are "
            "among them.\n\n" % n + "\n\n".join(gid) + "\n\n---\n\n")
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
    ek.append("| S%d | %s | E15 |" % (sn, m.group(1)))
if ek:
    last = list(re.finditer(r"^\| S\d+ \| .* \| E\d+ \|$", C, re.M))[-1]
    C = C[:last.end()] + "\n" + "\n".join(ek) + C[last.end():]
    open(cp, 'w', encoding='utf-8').write(C)
print("ok; eke giden paragraf:", toplam, "; kayittan eke:", len(ek))
