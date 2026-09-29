# Tur 167: Tur 166'da besimizin evet dedigi uc madde uygulanir:
#  - DeepSeek'in 6.4 isaretcisi; C3' (6.2 listesi kalir, yalniz isaretci); 2.3 gozden gecirilmis taslak (v8_round166_23.py)
import re, sys, os, glob, subprocess
root = sys.argv[1] if len(sys.argv) > 1 else "."
def rd(n):
    f = glob.glob(os.path.join(root, 'paper/v8/%02d-*.md' % n))[0]; s = open(f).read()
    m = re.search(r"^## (?!Yazar)", s, re.M); e = re.search(r"^## Yazarın denetimi", s, re.M)
    return f, s, m.start(), e.start()
def rep(n, a, b):
    f, s, st, en = rd(n); body = s[st:en]
    rx = r'\s+'.join(re.escape(w) for w in a.split())
    m = list(re.finditer(rx, body)); assert len(m) == 1, (n, a[:50], len(m))
    body = body[:m[0].start()] + b + body[m[0].end():]
    open(f, 'w').write(s[:st] + body + s[en:])
def paras(n):
    f, s, st, en = rd(n)
    return [p.strip() for p in re.split(r"\n\s*\n", s[st:en]) if p.strip()]
# 1. DeepSeek'in isaretcisi
rep(13, "at the declared lift-group fraction, and always toward the lighter aircraft.",
        "at the declared lift-group fraction, and always toward the lighter aircraft. The per-closure numbers are in Supplement S13.")
# 2. C3'
rep(11, "none of these is a ledger entry, and Section 14 lists them.", "none of these is a ledger entry, and Supplement S14 lists them.")
# 3. 2.3
once = paras(4)
subprocess.check_call([sys.executable, os.path.join(root, 'paper/build/v8_round166_23.py'), root])
f, s, st, en = rd(4); body = s[st:en]
body = re.sub(r"(?<=[^\s])  +(?=[^\s])", " ", body)          # silmenin biraktigi cift bosluk
open(f, 'w').write(s[:st] + body + s[en:])
sonra = paras(4)
def duz(x): return re.sub(r"\s+", " ", x).strip()
S = set(duz(p) for p in sonra)
degisen = [p for p in once if duz(p) not in S and not p.startswith('#')]
blok = ("### Section 4's paragraphs as they stood before the Round 167 recomposition\n\n"
        "Each paragraph below lost a sentence or a clause when Section 4 was recomposed in Round 167; it is given here in full, verbatim.\n\n"
        + "\n\n".join(degisen) + "\n\n---\n\n")
sp = os.path.join(root, 'paper/v8/supplement.md'); T = open(sp).read()
s5 = "## S5. Section 5 (from Section 5)"; assert T.count(s5) == 1
T = T.replace(s5, blok + s5); open(sp, 'w').write(T)
print('ok; S4e giden paragraf:', len(degisen))
