# Tur 166: Tur 165'te besimizin evet dedigi C1, C2, R-a, R-b uygulanir (C3 ChatGPT'de bekliyor).
import re, sys, os, glob
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
    return m[0].group(0)
# C1: 6.4 tablosu S13'e
f, s, st, en = rd(13); body = s[st:en]
m = re.search(r"Range of the lift-plus-cruise layout relative to this configuration:\s*\n\s*\n(\|.*\|\s*\n)+", body); assert m
tablo = m.group(0).rstrip('\n') + '\n'
body = body[:m.start()] + body[m.end():].lstrip('\n')
open(f, 'w').write(s[:st] + body + s[en:])
# C2
f, s, st, en = rd(14); body = s[st:en]
m = re.search(r"^Section 10 closed the sizing loop.*$", body, re.M); eski14 = m.group(0)
rep(14, " Section 15 calls this section a debt: questions the paper does not answer and that better evidence would.", "")
# R-a, R-b
rep(5, "is an open question in Section 14 rather than an answered one here.", "is an open question in Supplement S14 rather than an answered one here.")
rep(15, "Section 14 lists what the paper leaves open.", "Section 14 and Supplement S14 list what the paper leaves open.")
# Ek
sp = os.path.join(root, 'paper/v8/supplement.md'); S = open(sp).read()
bas = "## S13. Sensitivity of the lift-plus-cruise comparison (from Section 13)\n\n"
assert S.count(bas) == 1
S = S.replace(bas, bas + tablo + "\n*(Moved here from Section 13's body in Round 166; the body keeps every range, the shift and the sign change. The table below varies the inputs of this one.)*\n\n")
s15 = "## S15. Section 15 (from Section 15)"
blok = ("### Section 14's opening paragraph as it stood before the Round 165 cut\n\n"
        "The debt sentence was deleted in Round 166; Section 15 states the debt and the scope. The paragraph is given here in full, verbatim.\n\n"
        + eski14 + "\n\n---\n\n")
assert S.count(s15) == 1
S = S.replace(s15, blok + s15)
open(sp, 'w').write(S)
print('ok')
