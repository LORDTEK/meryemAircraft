# -*- coding: utf-8 -*-
"""Gonderim paketi ureteci (Journal of Aircraft, LaTeX).

Kaynak: paper/v8/ASSEMBLED.md (v8_assemble.py ciktisi). Adim kaynaklarina DOKUNMAZ.
Cikti:  paper/submission/latex/meryemaircraft.tex  (+ derlenirse .pdf)
Rapor:  paper/submission/build-report.md  -- her mekanik degisiklik tek tek; insan okur.

Mekanik donusumler (joa-requirements.md §4-§7, yazar kararlari E25-E31):
  bolumler Roma rakamiyla, alt bolumler harfle; "Section 6.1" -> "Sec. VI.A";
  koseli parantezli atif (references-draft.md yerlesim tablosu); E1 arac adlari;
  kalin vurgu kaldirilir; listeler 1) 2); Amerikan yazimi; sayi bicimi (1200, 12,000);
  tablolar numarali + baslikli; uc denklem numarali; Tesekkur (E31 b).
Uslup gecisi (tireler, above/below) BURADA YAPILMAZ: rapora liste olarak yazilir, okuyucu turuna gider.

Kullanim: python3 paper/build/submission_build.py [--pdf]
"""
import re, os, sys, difflib, subprocess, collections

KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(KOK, 'paper/v8/ASSEMBLED.md')
REFS = os.path.join(KOK, 'paper/submission/references-draft.md')
OUTDIR = os.path.join(KOK, 'paper/submission/latex')
OUT = os.path.join(OUTDIR, 'meryemaircraft.tex')
REPORT = os.path.join(KOK, 'paper/submission/build-report.md')

RAPOR = collections.OrderedDict((k, []) for k in [
    'citations', 'e1', 'table_refs', 'pointers', 'spelling', 'numbers', 'percent', 'headings',
    'warnings', 'dashes', 'above_below', 'italics'])

# ---------------------------------------------------------------- 1. on madde ve sabit metinler
TITLE = "meryemAircraft: Tail-Sitting Blended-Wing Body for Vertical Takeoff Without Propulsor Reorientation"
AUTHORS = [("Meryem G\\\"ulmen", True), ("Berke G\\\"ulmen", False), ("\\\"Omer G\\\"ulmen", False)]
AFFIL = "Independent Researcher, Ankara, T\\\"urkiye"
EMAIL = "meryemgulmen@outlook.com"
ABSTRACT = ("Hybrid aircraft for vertical takeoff and landing reach wing-borne cruise by carrying separate lift rotors or by "
 "reorienting their propulsors. This analytical study presents a tail-sitting blended-wing body arranged to change regime by "
 "rotating the airframe instead, and so carrying no mechanism that reorients a propulsor; every propulsor is a coaxial, "
 "torque-balanced pair, and a buffered series hybrid supplies the hover peak. An accounting of carried hover mass, exposed "
 "cruise drag, and hover-sized continuous power is stated first; one of its predictions holds on an independent sizing study, "
 "though not as a controlled experiment. Only the nose pair meets the accounting's escape condition; the exposed tip frames and "
 "rotors account for 57 to 69 percent of zero-lift drag. The effective lift-to-drag ratio, 5.56 to 7.39 before sizing closure, "
 "exceeds a published turboshaft quadrotor's throughout and ranges from 4 percent below to 27 percent above an all-electric one; "
 "against helicopters the result is mixed. The sizing loop closes at 52.3 to 57.5 kilograms, establishing arithmetic "
 "consistency, not that the package exists. Against lift-plus-cruise layouts the range ranking depends on the sizing contract. "
 "The buffer's required specific power is not demonstrated by the sources consulted, and the transition is not settled.")
# E31 (b), yazar onayi 2026-09-30
ACK = ("The authors used artificial-intelligence tools, under their direction, to draft and revise the English text, to search "
 "the literature, to review the manuscript, and as a tool in carrying out the calculations; the concept, architecture, design, "
 "and solution approach are the authors' own, and all three authors read and approved the manuscript and take full "
 "responsibility for its content.")

# ---------------------------------------------------------------- 2. atiflar (references-draft.md yerlesim tablosu)
# (isaretten hemen once gelen metin, kaynak numaralari). Metin ham markdown'da tam bir kez eslesmeli.
CITES = [
    ('before testing was curtailed because of engine and gear-box reliability problems"*', [1]),
    ('has been exploiting exactly those three for over a decade', [2]),
    ('have been built and flown for more than a decade', [2, 3]),
    ('A tail-sitter study reported in 2007', [4]),
    ('Attitude without aerodynamic control surfaces is established', [3]),
    ('at a cost its proposers name as added mechanical complexity', [5]),
    ('a tail-sitting micro air vehicle reported in 2014', [6]),
    ('for three-axis control in hover', [6]),
    ('a flying-wing tail-sitter reported in 2018', [7]),
    ('A coaxial contra-rotating tail-sitter reported in 2012', [8]),
    ('aimed at disaster response, is established, reported in 2025', [9]),
    ('a 2026 study of 100 kg winged biplane tail-sitters', [10]),
    ('a long-endurance concept reported in 2025', [11]),
    ('theoretically impossible to be very efficient in both hovering and forward flight."*', [2]),
    ('A long-range tail-sitter reported in 2018', [2]),
    ('Tail-sitting aircraft are seventy years old', [1]),
    ('a standing subject of transport research for more than three decades', [12]),
    ('series-hybrid propulsion has been designed for small uncrewed aircraft', [13]),
    ('the drag produced by the motors is significant."*', [14]),
    ('always predicts higher lift and lower drag than were experimentally observed."*', [15]),
    ('One of these transfers has direct experimental support', [14]),
    ('The check uses a NASA study', [16]),
    ('Reviewing the tail-sitters of the 1950s, NASA recorded', [17]),
    ('The landing difficulty of the 1950s tail-sitters was attributed', [17]),
    ('surveying the field, one study concludes', [18]),
    ('The sizing set of Section 2.3 reports', [16]),
    ('The source writes hover power', [16]),
    ('5,000-ft altitude and ISA + 20°C"*', [16]),
    ('three methods of three fidelities depart at the same place, the highest of them against wind-tunnel measurement', [21, 22]),
    ('studies of a winged tail-sitter (Section 1)', [10]),
    ('a single-aisle airliner reported in 2016', [23]),
    ('sized against the criterion the tailless literature recommends', [24]),
    ('on section polars computed rather than measured', [19]),
    ("transferred from a different airframe's wind-tunnel campaign", [14]),
    ('A pack flown in a 210 kg-class electric VTOL aircraft', [25]),
    ('A NASA-funded design study adopts 4 kW per kilogram', [26]),
]
# E1 (Tur 195, dort okuyucu + Claude): arac adlari ve surumleri 4.7'de, yalniz uretecte
E1 = [
    ('blade-element momentum theory at two operating points',
     'blade-element momentum theory, with section polars from NeuralFoil 0.3.3⟦CITE:19⟧, at two operating points'),
    ('from a vortex-lattice solution of the trimmed planform',
     'from a vortex-lattice solution (AeroSandbox 4.2.10⟦CITE:20⟧) of the trimmed planform'),
]
# Tablo numaralari: metin atiflari (okuyucu teyidine gider) ve basliklar (oneri; okuyucu teyidine gider)
TABLE_REFS = [
    ('The table is not a census of the field', 'Table 1 is not a census of the field'),
    ('and the table above is where one would appear', 'and Table 1 is where one would appear'),
    ('derived by inverting the table,', 'derived by inverting Table 1,'),
    ('a design variable this study has not fixed.', 'a design variable this study has not fixed (Table 2).'),
    ('The sizing set contains two quadrotors for the same mission,', 'The sizing set contains two quadrotors for the same mission (Table 3),'),
    ('this table alone does not establish', 'Table 3 alone does not establish'),
    ('The table counts the mechanism classes', 'Table 4 counts the mechanism classes'),
    ('On these assumptions all four converge', 'On these assumptions all four converge (Table 5)'),
    ("this paper's alternatives differ from axis to axis.", "this paper's alternatives differ from axis to axis (Table 6)."),
]
CAPTIONS = [
    "Known partial remedies and the charges they move",
    "Effective lift-to-drag ratio at the corners of the drag and propeller-efficiency brackets",
    "Effective lift-to-drag ratio against the two published quadrotors",
    "Mechanism classes that change regime or remove a rotor from one regime's flow",
    "The four closures of the sizing loop, 50 kg design",
    "The four claim axes and their opponents",
]
EQUATIONS = {  # ham kaynak -> LaTeX (numarali)
    'P_hover / P_cruise = √(DL / 2ρ) · (L/D) / V · (η_p / η_h)':
        r'\frac{P_\mathrm{hover}}{P_\mathrm{cruise}} = \sqrt{\frac{DL}{2\rho}}\,\frac{L/D}{V}\,\frac{\eta_p}{\eta_h}',
    '**L/De = WV/P = (L/D) · η_p**': r'(L/D)_e = \frac{WV}{P} = (L/D)\,\eta_p',
}
INLINE_MATH = {
    '`C_D = C_D0 + C_L²/(πARe)`': r'$C_D = C_{D0} + C_L^2/(\pi A\!R\,e)$',
    '`C_L = W/(qS)`': r'$C_L = W/(qS)$',
    '`L/De = WV/P`': r'$(L/D)_e = WV/P$',
    '`P = DV/η_p`': r'$P = DV/\eta_p$',
    '`P`': r'$P$',
    'MTOW = m_payload / (1 − f_empty − f_energy)': r'$\mathrm{MTOW} = m_\mathrm{payload}/(1 - f_\mathrm{empty} - f_\mathrm{energy})$',
}
SYMBOLS = [  # metin ici semboller (sira onemli: uzun once)
    ('ΔC_D0', r'$\Delta C_{D0}$'), ('C_D0', r'$C_{D0}$'), ('η_p', r'$\eta_p$'), ('η_h', r'$\eta_h$'),
    ('L/De', r'$(L/D)_e$'), ('√(DL)', r'$\sqrt{DL}$'), ('10⁵', r'$10^5$'), ('m s⁻¹', r'm\,s$^{-1}$'), ('m²', r'm$^2$'),
]
SPELLING = [  # (Ingiliz, Amerikan) -- sozcuk sinirli, buyuk-kucuk harf korunur
    ('favourable', 'favorable'), ('unfavourable', 'unfavorable'), ('favours', 'favors'), ('favoured', 'favored'),
    ('favour', 'favor'), ('modelled', 'modeled'), ('modelling', 'modeling'), ('optimised', 'optimized'),
    ('optimise', 'optimize'), ('centreline', 'centerline'), ('centre', 'center'), ('centres', 'centers'),
    ('idealised', 'idealized'), ('idealisation', 'idealization'), ('characterisation', 'characterization'),
    ('characterised', 'characterized'), ('characterise', 'characterize'), ('analysed', 'analyzed'), ('analyse', 'analyze'),
    ('aeroplane', 'airplane'), ('aeroplanes', 'airplanes'), ('behaviour', 'behavior'), ('manoeuvre', 'maneuver'),
    ('manoeuvres', 'maneuvers'), ('metre', 'meter'), ('metres', 'meters'), ('towards', 'toward'), ('whilst', 'while'),
    ('minimise', 'minimize'), ('minimised', 'minimized'), ('maximise', 'maximize'), ('recognised', 'recognized'),
    ('realised', 'realized'), ('stabilised', 'stabilized'), ('summarised', 'summarized'), ('organised', 'organized'),
    ('utilised', 'utilized'), ('emphasised', 'emphasized'), ('catalogue', 'catalog'), ('defence', 'defense'),
    ('grey', 'gray'), ('travelled', 'traveled'), ('fuelled', 'fueled'), ('labelled', 'labeled'), ('levelled', 'leveled'),
    ('programme', 'program'), ('take-off', 'takeoff'),
]
# 'analyses' fiil mi isim mi baglama bagli: elle
ANALYSES_VERB = ['Section 10 analyses', 'analyses the transition', 'which analyses']

# ---------------------------------------------------------------- yardimcilar
def roman(n): return ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'][n]
def letter(m): return 'ABCDEFGHIJ'[m - 1]

def loose(phrase):
    """ham markdown'da kalin isaretlerini ve satir sonlarini tolere eden desen"""
    out = []
    for ch in phrase:
        if ch == ' ': out.append(r'(?:\*\*)?\s+(?:\*\*)?')
        else: out.append(re.escape(ch) + r'(?:\*\*)?')
    return ''.join(out)

def insert_after(raw, phrase, token, kind):
    m = list(re.finditer(loose(phrase), raw))
    assert len(m) == 1, (kind, phrase, len(m))
    e = m[0].end()
    RAPOR[kind].append('`%s` + %s' % (phrase[-70:], token))
    return raw[:e] + token + raw[e:]

def replace_once(raw, a, b, kind):
    m = list(re.finditer(loose(a), raw))
    assert len(m) == 1, (kind, a, len(m))
    RAPOR[kind].append('`%s` → `%s`' % (a, b))
    return raw[:m[0].start()] + b + raw[m[0].end():]

# ---------------------------------------------------------------- 3. ham metin: atif, E1, tablo atiflari
raw = open(SRC, encoding='utf-8').read()
raw = raw.split('\n', 1)[1]                       # ilk satir: gorunum basligi
for phrase, nums in CITES:
    raw = insert_after(raw, phrase, '⟦CITE:%s⟧' % ','.join(map(str, nums)), 'citations')
for a, b in E1:
    raw = replace_once(raw, a, b, 'e1')
for a, b in TABLE_REFS:
    raw = replace_once(raw, a, b, 'table_refs')

# ---------------------------------------------------------------- 4. bolum haritasi
HEAD = {}          # "2" -> "II", "2.1" -> "II.A"
sec = sub = 0
for line in raw.split('\n'):
    m = re.match(r'^(#{2,4}) (.*)$', line)
    if not m: continue
    lvl = len(m.group(1))
    if lvl == 2:
        sec = int(re.match(r'(\d+)\.', m.group(2)).group(1)); sub = 0; HEAD[str(sec)] = roman(sec)
    elif lvl == 3:
        sub += 1
        mm = re.match(r'(\d+)\.(\d+) ', m.group(2))
        if mm: assert (int(mm.group(1)), int(mm.group(2))) == (sec, sub), line
        HEAD['%d.%d' % (sec, sub)] = '%s.%s' % (roman(sec), letter(sub))

# ---------------------------------------------------------------- 5. satir ici donusum
PH = {}
def protect(s):
    k = '⟦P%d⟧' % len(PH); PH[k] = s; return k

def conv_pointers(t):
    def one(n):
        assert n in HEAD, ('cozulmeyen atif', n)
        return HEAD[n]
    def rep(m):
        start = m.start()
        pre = t[max(0, start - 3):start]
        sentence_start = start == 0 or re.search(r'(^|[.!?:]\s|[.!?]\*\*\s|\n)$', t[max(0, start - 4):start]) is not None
        plural = m.group(1) == 'Sections'
        a, b = m.group(2), m.group(3)
        tgt = one(a) + ((' and ' + one(b)) if b else '')
        word = ('Sections' if plural else 'Section') if sentence_start else ('Secs.' if plural else 'Sec.')
        new = '%s %s' % (word, tgt)
        RAPOR['pointers'].append('`%s` → `%s`' % (m.group(0), new))
        return new
    return re.sub(r'\b(Sections?) (\d+(?:\.\d+)?)(?:,? and (\d+(?:\.\d+)?))?(?!\.\d)', rep, t)

def conv_spelling(t):
    for gb, us in SPELLING:
        def rep(m, us=us):
            w = m.group(0); new = us[0].upper() + us[1:] if w[0].isupper() else us
            RAPOR['spelling'].append('%s → %s' % (w, new)); return new
        t = re.sub(r'\b%s\b' % gb, rep, t, flags=re.I)
    for ph in ANALYSES_VERB:
        if ph in t:
            t = t.replace(ph, ph.replace('analyses', 'analyzes')); RAPOR['spelling'].append('analyses (verb) → analyzes')
    return t

def conv_numbers(t):
    def rep(m):
        a, b = m.group(1), m.group(2)
        new = a + b if len(a) == 1 else a + ',' + b
        RAPOR['numbers'].append('%s %s → %s' % (a, b, new)); return new
    t = re.sub(r'(?<![\d.,])(\d{1,3}) (\d{3})(?![\d])', rep, t)
    def pct(m):
        RAPOR['percent'].append('`%s` → `%s%%`' % (m.group(0), m.group(1))); return m.group(1) + '%'
    return re.sub(r'(\d) %', pct, t)

def conv_inline(t, in_table=False):
    # sabit matematik ve semboller once korunur
    for k, v in INLINE_MATH.items():
        if k in t: t = t.replace(k, protect(v))
    for k, v in SYMBOLS:
        t = t.replace(k, protect(v))
    # atif isaretleri
    t = re.sub(r'⟦CITE:([\d,]+)⟧', lambda m: protect('~\\cite{%s}' % ','.join('r' + x for x in m.group(1).split(','))), t)
    # vurgu
    t = t.replace('**', '')
    def ital(m):
        inner = m.group(1)
        if inner.startswith('"') and inner.endswith('"'):
            return inner                                   # alinti: italik degil, tirnak kalir
        RAPOR['italics'].append(inner[:80]); return '⟦I⟧' + inner + '⟦/I⟧'
    t = re.sub(r'(?<![*\w])\*([^*\n]+?)\*(?![*\w])', ital, t)
    t = conv_pointers(t)
    t = conv_spelling(t)
    t = conv_numbers(t)
    # kacis
    t = t.replace('\\', r'\textbackslash{}')
    for a, b in [('&', r'\&'), ('%', r'\%'), ('#', r'\#'), ('_', r'\_'), ('$', r'\$'), ('~', r'\textasciitilde{}'), ('^', r'\^{}')]:
        t = t.replace(a, b)
    # tirnaklar
    t = re.sub(r'(^|[\s(\[—–/])"', r'\1``', t)
    t = t.replace('"', "''")
    # unicode
    for a, b in [('—', '---'), ('–', '--'), ('…', r'\ldots{}'), ('°', r'$^\circ$'), ('−', r'$-$'), ('±', r'$\pm$'),
                 ('×', r'$\times$'), ('·', r'$\cdot$'), ('η', r'$\eta$'), ('ρ', r'$\rho$'), ('π', r'$\pi$'), ('Δ', r'$\Delta$'),
                 ('√', r'$\surd$'), ('²', r'$^2$')]:
        t = t.replace(a, b)
    t = t.replace('⟦I⟧', r'\textit{').replace('⟦/I⟧', '}')
    for _ in range(3):
        for k, v in list(PH.items()):
            t = t.replace(k, v)
    assert '⟦' not in t, t[:200]
    return t

def title_case(s):
    small = {'a', 'an', 'the', 'and', 'but', 'or', 'nor', 'for', 'so', 'yet', 'as', 'at', 'by', 'in', 'of', 'on', 'to', 'up',
             'per', 'via', 'vs', 'with', 'from', 'into', 'than'}
    words = s.split(' '); out = []
    for i, w in enumerate(words):
        def cap(x):
            return x[:1].upper() + x[1:] if x and x[:1].isalpha() else x
        prev = words[i - 1] if i else ''
        if i == 0 or i == len(words) - 1 or prev.endswith(':') or prev in ('—', '–') or w.lower() not in small:
            w = '-'.join(cap(p) for p in w.split('-'))
        out.append(w)
    return ' '.join(out)

# ---------------------------------------------------------------- 6. blok ayristirma
lines = raw.split('\n')
body = []
i = 0; tabno = 0; eqno = 0
counts = collections.Counter()
child = collections.defaultdict(int)
cur2 = cur3 = None
def para_text(buf): return ' '.join(x.strip() for x in buf)

def table_tex(rows, note):
    global tabno
    tabno += 1
    hdr = [c.strip() for c in rows[0].strip('|').split('|')]
    align = [c.strip() for c in rows[1].strip('|').split('|')]
    data = [[c.strip() for c in r.strip('|').split('|')] for r in rows[2:]]
    ncol = len(hdr)
    num = all(a.endswith(':') for a in align[1:]) if ncol > 1 else False
    if ncol >= 8:
        spec = 'l' + 'r' * (ncol - 1)
    else:
        spec = ''.join('r' if a.endswith(':') else ('X' if j else ('l' if num else 'X')) for j, a in enumerate(align))
    env = 'tabular' if ncol >= 8 else 'tabularx'
    out = [r'\begin{table}[htbp]', r'\centering', r'\caption{%s}' % conv_inline(CAPTIONS[tabno - 1]), r'\label{tab:%d}' % tabno]
    out.append(r'\footnotesize' if ncol >= 8 else r'\small')
    out.append(r'\begin{%s}%s{%s}' % (env, '{\\linewidth}' if env == 'tabularx' else '', spec))
    out.append(r'\hline')
    out.append(' & '.join(conv_inline(h, True) for h in hdr) + r' \\ \hline')
    for r in data:
        out.append(' & '.join(conv_inline(c, True) for c in r) + r' \\')
    out.append(r'\hline')
    out.append(r'\end{%s}' % env)
    if note:
        out.append(r'\par\smallskip\parbox{\linewidth}{\footnotesize %s}' % conv_inline(note))
    out.append(r'\end{table}')
    return '\n'.join(out)

while i < len(lines):
    L = lines[i]
    if not L.strip(): i += 1; continue
    m = re.match(r'^(#{2,4}) (.*)$', L)
    if m:
        lvl = len(m.group(1)); txt = m.group(2)
        txt = re.sub(r'^\d+(\.\d+)?\.? ', '', txt)
        tc = title_case(txt)
        RAPOR['headings'].append('%s %s → %s' % ('#' * lvl, m.group(2), tc))
        cmd = {2: 'section', 3: 'subsection', 4: 'subsubsection'}[lvl]
        if lvl == 2: cur2 = tc; cur3 = None
        elif lvl == 3: child[('s', cur2)] += 1; cur3 = tc
        else: child[('ss', cur2, cur3)] += 1
        body.append('\\%s{%s}' % (cmd, conv_inline(tc)))
        i += 1; continue
    if L.startswith('|'):
        rows = []
        while i < len(lines) and lines[i].startswith('|'): rows.append(lines[i]); i += 1
        note = None
        j = i
        while j < len(lines) and not lines[j].strip(): j += 1
        if j < len(lines) and lines[j].startswith('*L/De = L/D'):
            buf = []
            while j < len(lines) and lines[j].strip(): buf.append(lines[j]); j += 1
            note = para_text(buf).strip('*'); i = j
        body.append(table_tex(rows, note)); counts['table'] += 1
        continue
    if L.startswith('    ') and L.strip() in EQUATIONS or (L.startswith('> ') and L[2:].strip() in EQUATIONS):
        key = L.strip() if not L.startswith('> ') else L[2:].strip()
        eqno += 1
        body.append('\\begin{equation}\n%s\n\\end{equation}' % EQUATIONS[key]); i += 1; continue
    if L.startswith('> '):
        buf = []
        while i < len(lines) and lines[i].startswith('>'):
            buf.append(lines[i][1:].strip()); i += 1
        body.append('\\begin{quote}\n%s\n\\end{quote}' % conv_inline(' '.join(buf))); counts['quote'] += 1
        continue
    if re.match(r'^(- |\d+\. )', L):
        items = []
        while i < len(lines) and (re.match(r'^(- |\d+\. )', lines[i]) or (lines[i].startswith('  ') and lines[i].strip())):
            if re.match(r'^(- |\d+\. )', lines[i]): items.append(re.sub(r'^(- |\d+\. )', '', lines[i]))
            else: items[-1] += ' ' + lines[i].strip()
            i += 1
        body.append('\\begin{enumerate}[label=\\arabic*)]\n' + '\n'.join('\\item ' + conv_inline(x) for x in items) + '\n\\end{enumerate}')
        counts['list'] += 1
        continue
    buf = []
    while i < len(lines) and lines[i].strip() and not re.match(r'^(#{2,4} |\||- |\d+\. |    \S|> )', lines[i]):
        buf.append(lines[i]); i += 1
    if not buf:
        raise SystemExit('ayristirilamayan satir: %r' % L)
    body.append(conv_inline(para_text(buf)))

# ---------------------------------------------------------------- 7. uyarilar ve uslup listeleri
for k, v in child.items():
    if v == 1: RAPOR['warnings'].append('tek alt baslik (AIAA: en az 2): %s' % (k,))
plain = raw
for m in re.finditer(r'[^.\n]*—[^.\n]*', plain):
    RAPOR['dashes'].append(m.group(0).strip().replace('**', '')[:160])
for m in re.finditer(r'[^.\n]*\b(above|below)\b[^.\n]*', plain):
    RAPOR['above_below'].append(m.group(0).strip().replace('**', '')[:160])
assert tabno == len(CAPTIONS), (tabno, len(CAPTIONS))
assert eqno == len(EQUATIONS), eqno

# ---------------------------------------------------------------- 8. kaynakca
def bib():
    rows = [l for l in open(REFS, encoding='utf-8').read().split('\n') if re.match(r'^\| \d+ \| ', l)]
    items = []
    for r in rows:
        c = [x.strip() for x in r.strip('|').split('|')]
        n, e = int(c[0]), c[1]
        e = re.sub(r' \[DOI and version history[^\]]*\]', '', e)
        url = re.search(r'(https://doi\.org/\S+)$', e)
        if url: e = e[:url.start()].rstrip()
        t = e
        t = re.sub(r'\*([^*]+)\*', lambda m: '⟦I⟧' + m.group(1) + '⟦/I⟧', t)
        t = t.replace('&', r'\&').replace('%', r'\%').replace('_', r'\_')
        t = re.sub(r'(^|[\s(])"', r'\1``', t).replace('"', "''")
        t = t.replace('–', '--').replace('ö', r'\"o').replace('ü', r'\"u').replace('ñ', r'\~n').replace('é', r"\'e")
        t = t.replace('⟦I⟧', r'\textit{').replace('⟦/I⟧', '}')
        if url: t += ' \\url{%s}' % url.group(1).rstrip('.')
        items.append((n, t))
    assert [n for n, _ in items] == list(range(1, len(items) + 1))
    return items

# ---------------------------------------------------------------- 9. belge
PRE = r"""%% Uretildi: paper/build/submission_build.py -- elle duzenlemeyin; kaynak paper/v8/ adim dosyalaridir.
\IfFileExists{new-aiaa.cls}{%
  \documentclass[journal]{new-aiaa}
  \def\USINGAIAA{1}
}{%
  \documentclass[10pt]{article}
  \usepackage[margin=1in]{geometry}
  \usepackage{newtxtext,newtxmath}
  \usepackage{setspace}\doublespacing
  \usepackage{authblk}
  \usepackage[font=small,labelfont=bf,labelsep=space]{caption}
  \usepackage{titlesec}
  \renewcommand\thesection{\Roman{section}}
  \renewcommand\thesubsection{\Alph{subsection}}
  \renewcommand\thesubsubsection{\arabic{subsubsection}}
  \titleformat{\section}[block]{\centering\bfseries\large}{\thesection.}{0.5em}{}
  \titleformat{\subsection}[block]{\bfseries}{\thesubsection.}{0.5em}{}
  \titleformat{\subsubsection}[block]{\itshape}{\thesubsubsection.}{0.5em}{}
  \renewcommand\Authfont{\normalsize}
  \renewcommand\Affilfont{\itshape\small}
}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath}
\usepackage{tabularx}
\usepackage[shortlabels]{enumitem}
\usepackage{cite}
\usepackage{url}
\usepackage{textcomp}
"""

def build():
    auth = []
    for n, c in AUTHORS:
        fn = ('Independent Researcher; corresponding author, \\protect\\url{%s}.' % EMAIL) if c else 'Independent Researcher.'
        auth.append(r'\author{%s\thanks{%s}}' % (n, fn))
    doc = [PRE, r'\title{%s}' % TITLE] + auth + [r'\affil{%s}' % AFFIL, r'\date{}', r'\begin{document}', r'\maketitle',
           r'\begin{abstract}', ABSTRACT.replace('%', r'\%'), r'\end{abstract}', '']
    doc += body
    doc += ['', r'\section*{Acknowledgments}', ACK, '', r'\begin{thebibliography}{99}']
    for n, t in bib():
        doc.append(r'\bibitem{r%d} %s' % (n, t))
    doc += [r'\end{thebibliography}', r'\end{document}', '']
    return '\n\n'.join(x for x in doc if x is not None)

os.makedirs(OUTDIR, exist_ok=True)
tex = build()
open(OUT, 'w', encoding='utf-8').write(tex)

# ---------------------------------------------------------------- 10. cikti denetimi: sozcuk dizisi mekanik donusum disinda ayni mi
def norm_md(t):
    t = re.sub(r'⟦CITE:[\d,]+⟧', '', t)
    t = t.replace('**', '')
    t = re.sub(r'(?<![*\w])\*([^*\n]+?)\*(?![*\w])', r'\1', t)
    t = re.sub(r'^#+ (\d+(\.\d+)?\.? )?', '', t, flags=re.M)
    t = re.sub(r'^\|?[-:| ]+\|$', '', t, flags=re.M)
    t = re.sub(r'\bSections? \d+(?:\.\d+)?(?:,? and \d+(?:\.\d+)?)?(?!\.\d)', ' SECREF ', t)
    t = re.sub(r'(?<![\d.,])(\d{1,3}) (\d{3})(?!\d)', r'\1\2', t)
    for gb, us in SPELLING:
        t = re.sub(r'\b%s\b' % gb, us, t, flags=re.I)
    for ph in ANALYSES_VERB:
        t = t.replace(ph, ph.replace('analyses', 'analyzes'))
    return t
def norm_tex(t):
    t = t.split(r'\maketitle', 1)[1].split(r'\section*{Acknowledgments}', 1)[0]
    t = t.split(r'\end{abstract}', 1)[1]
    t = re.sub(r'\\caption\{[^}]*\}', '', t)
    t = re.sub(r'\\label\{[^}]*\}', '', t)
    t = re.sub(r'~?\\cite\{[^}]*\}', '', t)
    t = re.sub(r'\\(begin|end)\{[^}]*\}(\{[^}]*\})*(\[[^\]]*\])?(\{[^}]*\})*', ' ', t)
    t = re.sub(r'\b(Secs?\.|Sections?) [IVX]+(?:\.[A-H])?(?: and [IVX]+(?:\.[A-H])?)?', ' SECREF ', t)
    t = re.sub(r'(\d),(\d{3})', r'\1\2', t)
    t = re.sub(r'\\[a-zA-Z]+', ' ', t)
    return t
def words(t):
    t = t.replace('``', '"').replace("''", '"').replace('---', '—').replace('--', '–')
    t = re.sub(r'[{}$\\]', ' ', t)
    return [w.lower() for w in re.findall(r"[A-Za-z]+(?:'[a-z]+)?|\d+", t)]
wa, wb = words(norm_md(raw)), words(norm_tex(tex))
sm = difflib.SequenceMatcher(None, wa, wb, autojunk=False)
fark = [(op, ' '.join(wa[a1:a2]), ' '.join(wb[b1:b2])) for op, a1, a2, b1, b2 in sm.get_opcodes() if op != 'equal']

# ---------------------------------------------------------------- 11. rapor
bodywords = len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", re.sub(r'\\[a-zA-Z]+\*?', ' ', norm_tex(tex))))
with open(REPORT, 'w', encoding='utf-8') as f:
    f.write('# Build report: `paper/build/submission_build.py`\n\n')
    f.write('Source `paper/v8/ASSEMBLED.md`; output `paper/submission/latex/meryemaircraft.tex`. **The step sources are not changed.**\n\n')
    f.write('- Body words (text and table cells, excluding abstract, references and acknowledgments): **%d**\n' % bodywords)
    f.write('- Tables: %d · numbered equations: %d · lists: %d\n\n' % (tabno, eqno, counts['list']))
    f.write('## Output check: word-sequence differences other than the listed mechanical changes\n\n')
    f.write('Each row is a place where the output\'s words differ from the source. Every row should be one of the changes listed below; anything else is a generator defect.\n\n')
    f.write('| op | source | output |\n|---|---|---|\n')
    for op, a, b in fark:
        f.write('| %s | %s | %s |\n' % (op, a[:120], b[:120]))
    titles = {'citations': 'Citation markers inserted', 'e1': 'E1 tool names (Round 195)', 'table_refs': 'Table references (for reader check)',
              'pointers': 'Section pointers', 'spelling': 'American spelling', 'numbers': 'Number format', 'percent': 'Percent spacing',
              'headings': 'Headings (title case)', 'warnings': 'Warnings', 'dashes': 'Dashes left in the text (style pass: reader round)',
              'above_below': '"above" / "below" left in the text (style pass: reader round)', 'italics': 'Italic (non-quotation) kept'}
    for k, v in RAPOR.items():
        f.write('\n## %s (%d)\n\n' % (titles[k], len(v)))
        for x in v: f.write('- %s\n' % x)
print('tex:', OUT)
print('govde sozcuk:', bodywords, '| tablo', tabno, '| denklem', eqno, '| fark satiri', len(fark))
for k, v in RAPOR.items(): print('  %-12s %d' % (k, len(v)))

if '--pdf' in sys.argv:
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'meryemaircraft.tex'], cwd=OUTDIR,
                           capture_output=True, text=True)
    print('pdflatex:', r.returncode)
    if r.returncode: print(r.stdout[-3000:])
