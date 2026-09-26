# -*- coding: utf-8 -*-
"""Bir adim taslagini kaynagina karsi denetler (Tur 68 plani, madde 3).

  python3 paper/build/v8_draft_check.py 12

1. YENI YUKLEM YOK: taslaktaki her cumle, kaynaktaki bir cumlenin (ya da kisa bir ardisik
   bolumun) SILMEYLE kisaltilmis hali olmali -- kelimeleri kaynakta ayni sirayla, dar bir
   pencere icinde bulunmali. ⟦ ⟧ icindeki baglantilar bundan muaf; ayrica listelenir.
2. Korunan cumleler (paper/v8-caveats.md, o adimin satirlari) taslakta duruyor mu.
3. Kaynaktaki her cumle: KALDI / KISALDI (silinen kisim) / CIKTI -> paper/v8/drafts/NN-removed.md
--sina: taslaga kaynakta olmayan bir yuklem ekleyip yakalandigini sinar.
"""
import glob, os, re, sys
KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v8_caveats import duz, liste  # noqa

n = int(sys.argv[1])
# Tur 110: --taslak YOL ile baska bir taslak dosyasi (ornek: drafts/02-draft2.md); cikti yanina -removed yazilir.
TASLAK = sys.argv[sys.argv.index("--taslak") + 1] if "--taslak" in sys.argv else None
src_f = glob.glob(os.path.join(KOK, "paper", "v8", "%02d-*.md" % n))[0]
s = open(src_f, encoding="utf-8").read()
m = re.search(r"^## (?!Yazar)", s, re.M); e = re.search(r"^## Yazarın denetimi", s, re.M)
kaynak = re.sub(r"\n---\s*$", "", s[m.start():e.start()].rstrip())
taslak = open(TASLAK or os.path.join(KOK, "paper", "v8", "drafts", "%02d-draft.md" % n), encoding="utf-8").read()
if "--sina" in sys.argv:
    taslak = taslak.replace("**Coupling is not identity.**", "**Coupling is identity.**")

TOK = re.compile(r"[\w×⁻¹²³⁴⁵⁶⁷⁸⁹⁰.,'’%–−²³^]+", re.U)


def toks(x):
    x = x.replace("*", "")
    return [w.strip(".,").lower() for w in TOK.findall(x) if w.strip(".,")]


def cumleler(x):
    x = re.sub(r"(?m)^#+ .*$", "", x)
    x = re.sub(r"\s+", " ", x.replace("*", ""))
    # Tur 110: tirnakla biten cumle de bolunur (."); yoksa alinti ile biten cumle sonrakine yapisiyordu
    return [c.strip() for c in re.split(r"(?:(?<=[.!?])|(?<=[.!?]\"))\s+(?=[A-Z(])", x) if c.strip()]


kc = cumleler(kaynak)
kt = [toks(c) for c in kc]
flat = [(i, w) for i, ws in enumerate(kt) for w in ws]
kullanildi = [set() for _ in kc]
baglanti = re.findall(r"⟦(.*?)⟧", taslak)
temiz = re.sub(r"⟦.*?⟧", "", taslak)
KORUYUCU = {"not", "no", "never", "nothing", "none", "nor", "cannot", "neither", "without", "only",
            "unless", "except", "approximately", "about", "roughly", "nearly", "within", "less", "more",
            "not,", "rather", "but", "if", "either", "may", "might", "would", "could"}


def altdizi(dt, ws):
    k, idx = 0, []
    for j, w in enumerate(ws):
        if k < len(dt) and w == dt[k]:
            idx.append(j); k += 1
    return idx if k == len(dt) else None


hata, bekci = [], []
for c in cumleler(temiz):
    dt = toks(c)
    if not dt:
        continue
    eslesme = None
    for i, ws in enumerate(kt):                      # once tek bir kaynak cumlede
        idx = altdizi(dt, ws)
        if idx is not None:
            eslesme = [(i, j) for j in idx]
            break
    if eslesme is None:                              # sonra ardisik iki-uc cumlede
        for i in range(len(kt)):
            ws = [(a, j) for a in range(i, min(i + 3, len(kt))) for j in range(len(kt[a]))]
            idx = altdizi(dt, [kt[a][j] for a, j in ws])
            if idx is not None:
                eslesme = [ws[q] for q in idx]
                break
    if eslesme is None:
        hata.append(c)
        continue
    for i, j in eslesme:
        kullanildi[i].add(j)
    # silinen koruyucu kelime: eslesen aralikta atlanan olumsuzluk/niteleyici
    for i in sorted({i for i, _ in eslesme}):
        js = [j for a, j in eslesme if a == i]
        for j in range(min(js), max(js) + 1):
            if j not in js and kt[i][j] in KORUYUCU:
                bekci.append((c[:90], kt[i][j]))
if bekci:
    print("SILINMIS OLUMSUZLUK/NITELEYICI (anlam donebilir):")
    for c, w in bekci:
        print("   - '%s' silinmis: %s" % (w, c))
if hata:
    print("YENI YUKLEM ADAYI (kaynakta silmeyle turetilemeyen cumle):")
    for c in hata:
        print("   -", c[:160])

d = duz(taslak)
eksik = [q for a, q, _ in liste() if a == n
         for p in [duz(x).strip(" .,") for x in q.split("…") if duz(x).strip(" .,")] if p not in d]

satirlar = ["# Adım %d taslağı — kaynaktan çıkan ve kısalan her cümle (üretildi: v8_draft_check.py)\n" % n,
            "Çıkan cümleler taslak uygulanırsa Ek S%d'ye **aynen** gider.\n" % n]
cikti = kisaldi = 0
for i, c in enumerate(kc):
    u = kullanildi[i]
    if len(u) == len(kt[i]):
        continue
    if not u:
        cikti += 1
        satirlar.append("- **ÇIKTI:** %s" % c)
    else:
        kisaldi += 1
        silinen = [w for j, w in enumerate(kt[i]) if j not in u]
        satirlar.append("- **KISALDI:** %s\n  - *silinen:* %s" % (c, " ".join(silinen)))
open(re.sub(r"\.md$", "-removed.md", TASLAK) if TASLAK else os.path.join(KOK, "paper", "v8", "drafts", "%02d-removed.md" % n), "w", encoding="utf-8").write("\n".join(satirlar) + "\n")

print("kaynak %d kelime, %d cumle | taslak %d kelime" % (len(kaynak.split()), len(kc), len(re.sub(r"[⟦⟧]", "", taslak).split())))
print("cikan cumle %d, kisalan %d, aynen kalan %d" % (cikti, kisaldi, len(kc) - cikti - kisaldi))
print("baglantilar (olgu soylememeli, gosterilir):", baglanti)
print("eksik korunan:", eksik or "yok")
sys.exit(1 if (hata or eksik or bekci) else 0)
