# -*- coding: utf-8 -*-
"""Dergi eki ureteci (Journal of Aircraft, LaTeX).

Kaynak: paper/submission/supplement-src.md (Tur 204-213, her parca kaynak notuyla). Kaynak notlari (<!-- -->) ciktiya GIRMEZ.
Cikti:  paper/submission/latex/meryemaircraft-supplement.tex (+ --pdf ile .pdf)

Mekanik donusumler, govde ureteciyle AYNI islevlerle (submission_build.py bolum 1-5 burada calistirilir):
  ek bolumleri S2-S14 -> S1-S11 (Tur 204, dort okuyucu + Claude); "Section 6.1" -> "Sec. VI.A"; Amerikan yazimi;
  sayi bicimi; kalin vurgu kaldirilir; tablolar "Table S1", "Table S2" ...
Denetim: (1) her korunan ek satiri (paper/v8-caveats.md alt tablosu; Section 10 -> Section 6.1 gibi yeniden numaralama
dahil) ciktida sozcuk sozcuk var mi; (2) govdenin her "Supplement S#" isaretcisinin karsiligi olan bolum ciktida var mi.

Kullanim: python3 paper/build/supplement_build.py [--pdf] [--sina]
"""
import os, re, sys, subprocess

KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
GEN = os.path.join(KOK, 'paper/build/submission_build.py')
SRC = os.path.join(KOK, 'paper/submission/supplement-src.md')
OUTDIR = os.path.join(KOK, 'paper/submission/latex')
OUT = os.path.join(OUTDIR, 'meryemaircraft-supplement.tex')

kod = open(GEN, encoding='utf-8').read()
kod = kod.split('# ---------------------------------------------------------------- 6. blok ayristirma')[0]
ns = {'__file__': GEN}
exec(compile(kod, GEN, 'exec'), ns)
conv_inline, title_case, SUPP_MAP, TITLE = ns['conv_inline'], ns['title_case'], ns['SUPP_MAP'], ns['TITLE']
_tam = open(GEN, encoding='utf-8').read()
PRE = re.search(r'^PRE = r"""(.*?)"""', _tam, flags=re.S | re.M).group(1)

src = open(SRC, encoding='utf-8').read()
src = re.sub(r'<!--.*?-->', '', src, flags=re.S)
src = src.split('\n', 1)[1]                       # ilk satir: kaynak basligi
SINA = '--sina' in sys.argv                         # denetimin kendisi: korunan bir ek satiri silinir, denetim yakalamali
if SINA:
    assert 'This paragraph compares the reference pair only.' in src
    src = src.replace('This paragraph compares the reference pair only.', '')
# ust simge birimleri: govde ureteci yalniz kendi gectigi bicimleri tasir (SYMBOLS); ekte digerleri de var
UST = {'⁻¹': '^{-1}', '⁻²': '^{-2}', '⁴': '^4', '⁵': '^5', 'β': r'\beta', '∝': r'\propto'}
src = re.sub('|'.join(UST), lambda m: ns['protect']('$%s$' % UST[m.group(0)]), src)

tabno = 0
def table_tex(rows):
    global tabno
    tabno += 1
    hdr = [c.strip() for c in rows[0].strip('|').split('|')]
    align = [c.strip() for c in rows[1].strip('|').split('|')]
    data = [[c.strip() for c in r.strip('|').split('|')] for r in rows[2:]]
    spec = ''.join('r' if a.endswith(':') else 'X' for a in align)
    out = [r'\begin{table}[htbp]', r'\centering', r'\caption*{Table S%d}' % tabno, r'\small',
           r'\begin{tabularx}{\linewidth}{%s}' % spec, r'\hline',
           ' & '.join(conv_inline(h, True) for h in hdr) + r' \\ \hline']
    for r in data:
        out.append(' & '.join(conv_inline(c, True) for c in r) + r' \\')
    out += [r'\hline', r'\end{tabularx}', r'\end{table}']
    return '\n'.join(out)

body, bolumler = [], []
lines = src.split('\n')
i = 0
while i < len(lines):
    L = lines[i]
    if not L.strip(): i += 1; continue
    m = re.match(r'^## S(\d+)\. (.*)$', L)
    if m:
        yeni = SUPP_MAP[m.group(1)]
        bolumler.append(yeni)
        body.append(r'\section*{S%s. %s}' % (yeni, conv_inline(title_case(m.group(2)))))
        i += 1; continue
    m = re.match(r'^### (.*)$', L)
    if m:
        body.append(r'\subsection*{%s}' % conv_inline(title_case(m.group(1)))); i += 1; continue
    if L.startswith('|'):
        rows = []
        while i < len(lines) and lines[i].startswith('|'): rows.append(lines[i]); i += 1
        body.append(table_tex(rows)); continue
    if L.startswith('    '):
        buf = []
        while i < len(lines) and lines[i].startswith('    '):
            buf.append(r'\texttt{%s}' % conv_inline(lines[i].strip())); i += 1
        body.append('\\begin{center}\n%s\n\\end{center}' % ' \\\\\n'.join(buf)); continue
    if re.match(r'^\d+\) ', L):
        items = []
        while i < len(lines) and re.match(r'^\d+\) ', lines[i]):
            items.append(re.sub(r'^\d+\) ', '', lines[i])); i += 1
        body.append('\\begin{enumerate}[label=\\arabic*)]\n' + '\n'.join('\\item ' + conv_inline(x) for x in items) + '\n\\end{enumerate}')
        continue
    buf = []
    while i < len(lines) and lines[i].strip() and not re.match(r'^(#{2,3} |\||    \S|\d+\) )', lines[i]):
        buf.append(lines[i].strip()); i += 1
    if not buf:
        raise SystemExit('ayristirilamayan satir: %r' % L)
    body.append(conv_inline(' '.join(buf)))

doc = [PRE.replace('paper/build/submission_build.py', 'paper/build/supplement_build.py'),
       r'\title{Supplemental Material for ``%s''}' % TITLE, r'\author{}', r'\date{}', r'\begin{document}', r'\maketitle',
       "The sections below hold the working behind the pointers of the paper (``Supplement S1'' to ``Supplement S11''); "
       "section and reference numbers are those of the paper.", ''] + body + ['', r'\end{document}', '']
tex = '\n\n'.join(doc)
tex = tex.replace(r'\usepackage{graphicx}', '\\usepackage{graphicx}\n\\usepackage{caption}')
os.makedirs(OUTDIR, exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(tex)

# ---------------------------------------------------------------- denetim
def sozler(t):
    t = re.sub(r'\\[a-zA-Z]+\*?', ' ', t).replace('``', '"').replace("''", '"')
    return ' '.join(w.lower() for w in re.findall(r"[A-Za-z]+|\d+", t))
cikti = sozler(tex)
cav = open(os.path.join(KOK, 'paper/v8-caveats.md'), encoding='utf-8').read()
alt = cav.split('Yazar kararıyla eke taşınan korunan cümleler')[1]
eksik, n = [], 0
for m in re.finditer(r'^\| S(\d+) \| (.+?) \| E\d+ \|$', alt, flags=re.M):
    if m.group(1) not in SUPP_MAP: continue          # S9 vb.: dergi ekinde olmayan arsiv bolumleri
    n += 1
    cumle = m.group(2)
    cumle = re.sub(r'\bSection 10\b', 'Section 6.1', cumle)
    cumle = re.sub(r'\bSection 8\b', 'Section 5.2', cumle)
    cumle = cumle.replace('the isolation test above', 'the isolation test of Section 2.3')
    parcalar = [sozler(conv_inline(x)) for x in cumle.split('…') if x.strip()]   # '…' kayitta kisaltma isareti
    if not all(h in cikti for h in parcalar): eksik.append((m.group(1), cumle))
govde = open(os.path.join(KOK, 'paper/v8/ASSEMBLED.md'), encoding='utf-8').read()
isaret = sorted(set(re.findall(r'Supplement S(\d+)', govde)), key=int)
yok = [s for s in isaret if SUPP_MAP.get(s) not in bolumler]
print('tex:', OUT)
print('bolumler:', ', '.join('S' + b for b in bolumler), '| tablolar:', tabno)
print('korunan ek satiri: %d denetlendi, %d eksik' % (n, len(eksik)))
for e in eksik: print('  EKSIK', e)
print('govde isaretcileri:', ', '.join('S%s->S%s' % (s, SUPP_MAP.get(s, '?')) for s in isaret), '| karsiliksiz:', yok or 'yok')
if SINA:
    print('SINA:', 'yakaladi' if eksik else 'YAKALAMADI'); sys.exit(0 if eksik else 1)
if eksik or yok: sys.exit(1)

if '--pdf' in sys.argv:
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', os.path.basename(OUT)], cwd=OUTDIR,
                           capture_output=True, text=True)
    print('pdflatex:', r.returncode)
    if r.returncode: print(r.stdout[-3000:])
