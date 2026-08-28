# -*- coding: utf-8 -*-
"""Dokuz bolumu, on bilgiyi, kaynakcayi ve 12 sekli tek belgede birlestirir.

Sekiller metinde ilk atif aldiklari paragrafin hemen ardina yerlestirilir.
Turkce calisma notlari (*Taslak...*, [koseli parantez icindekiler]) ayiklanir.
Cikti: makale/makale.md  ve  makale/pdf/meryemAircraft-makale.pdf
"""
import os, re, sys, base64, glob, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kapaklar import FIGS

ROOT = "/home/user/meryemAircraft"
BOL  = os.path.join(ROOT, "makale", "bolumler")
GOR  = os.path.join(ROOT, "gorsel", "cikti")
OUT  = os.path.join(ROOT, "makale")

CAP = {n: (f if isinstance(f, list) else [f], c) for n, f, c in FIGS}

# ---------------------------------------------------------------- temizlik
NOT = re.compile(r"^\s*\*?\[.*", re.S)

def temizle(s):
    """Turkce calisma notlarini ve taslak damgasini ayiklar."""
    s = re.sub(r"^\*Taslak v1.*?\n", "", s, flags=re.M)
    ciktilar = []
    for par in s.split("\n\n"):
        p = par.strip()
        if not p:
            continue
        if p == "---":
            continue
        # koseli parantezle baslayan not paragraflari
        if NOT.match(p):
            continue
        # italik Turkce not paragraflari (ASCII disi Turkce harf tasiyanlar)
        govde = p.strip("*_ ")
        if p.startswith("*") and p.rstrip().endswith("*") and \
           any(ch in govde for ch in "şığçöüŞİĞÇÖÜ") and not p.startswith("**"):
            continue
        if any(ch in p for ch in "şığŞİĞ") and re.match(r"^(Durum|Bölüm|Not|Kaynak)\b", p):
            continue
        ciktilar.append(par.rstrip())
    return "\n\n".join(ciktilar).strip()

def blok(metin, baslik):
    """00-on-bilgi.md icinden '## baslik' ya da '### baslik' bolumunu ceker."""
    m = re.search(r"^#{2,3}\s+%s\s*$(.*?)(?=^#{2,3}\s|\Z)" % re.escape(baslik),
                  metin, flags=re.M | re.S)
    return temizle(m.group(1)) if m else ""

# ------------------------------------------------------- sekil yerlesimi
def sekilleri_yerlestir(metin):
    """Her sekli, ilk atif aldigi paragrafin ardina koyar."""
    paras = metin.split("\n\n")
    yerlesen = []
    for n, _, _ in FIGS:
        pat = re.compile(r"Figure %s(?![0-9])" % re.escape(n))
        for i, p in enumerate(paras):
            if pat.search(p):
                yerlesen.append((i, n))
                break
    cikti = []
    for i, p in enumerate(paras):
        cikti.append(p)
        for j, n in yerlesen:
            if j == i:
                cikti.append("@@FIG:%s@@" % n)
    return "\n\n".join(cikti), [n for _, n in yerlesen]

# ---------------------------------------------------------------- montaj
ON = open(os.path.join(OUT, "00-on-bilgi.md")).read()

baslik   = blok(ON, "Title").replace("**", "").replace("\n", " ").strip()
yazarlar = blok(ON, "Authors").replace("\n", " ").strip()
ozet     = blok(ON, "Abstract")
anahtar  = blok(ON, "Keywords")
tesekkur = blok(ON, "Acknowledgements")
cikar    = blok(ON, "Conflicts of Interest")
veri     = blok(ON, "Data Availability")
fon      = blok(ON, "Funding") or "This research received no external funding."

def alintiyi_duzlestir(t):
    return re.sub(r"^>\s?", "", t, flags=re.M).strip()

ON_HTML = "\n\n".join([
    "# " + baslik,
    yazarlar,
    "**Abstract.** " + " ".join(ozet.split()),
    "**Keywords:** " + " ".join(anahtar.split()),
])

bolumler = sorted(glob.glob(os.path.join(BOL, "*.md")))
govde = "\n\n".join(temizle(open(f).read()) for f in bolumler)
govde, sirali = sekilleri_yerlestir(govde)

ARKA = "\n\n".join([
    "# Declarations",
    "**Funding.** " + alintiyi_duzlestir(fon),
    "**Conflicts of interest.** " + alintiyi_duzlestir(cikar),
    "**Data availability.** " + alintiyi_duzlestir(veri),
    "**Acknowledgements.** " + alintiyi_duzlestir(tesekkur),
    temizle(open(os.path.join(OUT, "kaynakca-en.md")).read()),
])

eksik = [n for n, _, _ in FIGS if n not in sirali]
if eksik:
    print("UYARI — metinde atif bulunamayan sekiller:", eksik)

MD = ON_HTML + "\n\n" + govde + "\n\n" + ARKA
open(os.path.join(OUT, "makale.md"), "w").write(
    re.sub(r"@@FIG:([0-9]+)@@", r"[Figure \1 about here]", MD))

# ------------------------------------------------------------------ HTML
import markdown as md

def b64(p):
    with open(p, "rb") as fh:
        return "data:image/png;base64," + base64.b64encode(fh.read()).decode()

GENIS = {"2", "9"}   # en/boy > 2 — dik sayfaya sigmaz, yatay tam sayfa basilir

YATAY_DIZIN = os.path.join(ROOT, "gorsel", "cikti", "yatay")
os.makedirs(YATAY_DIZIN, exist_ok=True)

# Tam sayfa yatay sekil: 250 mm x 166 mm tuval, 300 dpi karsiligi
YW, YH = 2953, 1961          # piksel — 250 mm x 166 mm, 300 dpi
YKENAR = 40
YFONT = 36                   # 8.7 pt @ 300 dpi  (8.7/72*300 = 36 px)


def yatay_sekil_uret(n, yollar, cap):
    """Sekli ve altyazisini tek tuvale dizip 90 derece dondurur.

    CSS transform'una guvenmiyoruz: ekranda saran altyazi baskida sarmadi ve
    sonraki sayfaya tasti. Burada sarma islemi piksel olarak yapiliyor, sonuc
    dosyaya yaziliyor ve basilmadan once gozle dogrulanabiliyor.
    """
    from PIL import Image as _I, ImageDraw as _D, ImageFont as _F
    import matplotlib
    fd = os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")
    fn = _F.truetype(os.path.join(fd, "DejaVuSans.ttf"), YFONT)
    fb = _F.truetype(os.path.join(fd, "DejaVuSans-Bold.ttf"), YFONT)

    tuval = _I.new("RGB", (YW, YH), "white")
    d = _D.Draw(tuval)

    # --- altyaziyi sar ---
    genislik = YW - 2 * YKENAR
    bas = "Figure %s. " % n
    kelimeler = cap.split()
    satirlar, gecerli = [], bas
    ilk = True
    for k in kelimeler:
        deneme = (gecerli + k) if gecerli.endswith(" ") else (gecerli + " " + k)
        w = d.textlength(deneme, font=fn) + (d.textlength(bas, font=fb) -
                                             d.textlength(bas, font=fn) if ilk else 0)
        if w > genislik and gecerli.strip() not in ("", bas.strip()):
            satirlar.append(gecerli.rstrip()); gecerli = k; ilk = False
        else:
            gecerli = deneme
    satirlar.append(gecerli.rstrip())

    satir_h = int(YFONT * 1.42)
    alt_h = len(satirlar) * satir_h + 24

    # --- gorselleri yerlestir ---
    resimler = [_I.open(y).convert("RGB") for y in yollar]
    enb = max(r.width for r in resimler)
    ust_alan = YH - alt_h - 2 * YKENAR
    olcek = min(genislik / enb,
                ust_alan / sum(r.height * (enb / r.width) for r in resimler) if resimler else 1)
    y = YKENAR
    for r in resimler:
        w = int(r.width * (enb / r.width) * olcek)
        h = int(r.height * (enb / r.width) * olcek)
        tuval.paste(r.resize((w, h), _I.LANCZOS), ((YW - w) // 2, y))
        y += h

    # --- altyaziyi yaz ---
    ty = YH - alt_h - YKENAR + 24
    for i, sat in enumerate(satirlar):
        x = YKENAR
        if i == 0:
            d.text((x, ty), bas, font=fb, fill=(28, 32, 36))
            x += d.textlength(bas, font=fb)
            sat = sat[len(bas):] if sat.startswith(bas) else sat
        d.text((x, ty), sat, font=fn, fill=(51, 57, 63))
        ty += satir_h

    cikti = os.path.join(YATAY_DIZIN, "sekil%s-yatay.png" % n)
    tuval.rotate(90, expand=True).save(cikti)      # saat yonunun tersine
    return cikti


def figblok(n):
    dosyalar, cap = CAP[n]
    yollar = [os.path.join(GOR, d) for d in dosyalar]
    from PIL import Image as _I

    if n in GENIS:
        return ('<figure class="figtam"><img src="%s"></figure>'
                % b64(yatay_sekil_uret(n, yollar, cap)))

    boyut = [_I.open(y).size for y in yollar]
    genis = [b[0] for b in boyut]
    enb = max(genis)
    # boyu enine yakin sekiller tam sutun genisliginde bir sayfayi tek basina
    # doldurur; %82'ye cekilince metinle ayni sayfayi paylasabiliyorlar
    oran = enb / max(b[1] for b in boyut)
    olcek = 82.0 if oran < 1.5 else 100.0
    imgs = "".join('<img src="%s" style="width:%.1f%%">' % (b64(y), olcek * g / enb)
                   for y, g in zip(yollar, genis))
    return ('<figure class="fig">%s<figcaption><b>Figure %s.</b> %s</figcaption>'
            '</figure>' % (imgs, n, cap))

parts = re.split(r"@@FIG:([0-9]+)@@", MD)
html_parcalari = []
for i, seg in enumerate(parts):
    if i % 2 == 0:
        html_parcalari.append(md.markdown(seg, extensions=["tables", "sane_lists"]))
    else:
        html_parcalari.append(figblok(seg))
GOVDE_HTML = "\n".join(html_parcalari)

# "**Table N.** ..." paragrafi ile hemen ardindaki tabloyu birlikte tut
GOVDE_HTML = re.sub(
    r"(<p><strong>Table [0-9]+\..*?</p>)\s*(<table>.*?</table>)",
    r'<div class="tblok">\1\2</div>', GOVDE_HTML, flags=re.S)

CSS = """
@page { size: A4; margin: 22mm 20mm 20mm 20mm; }
html { -webkit-print-color-adjust: exact; }
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 10.4pt;
       line-height: 1.52; color: #16191c; margin: 0; text-align: justify;
       hyphens: auto; }
h1 { font-family: "DejaVu Sans", Helvetica, sans-serif; font-size: 17pt;
     line-height: 1.28; margin: 0 0 14pt 0; text-align: left; }
h2 { font-family: "DejaVu Sans", Helvetica, sans-serif; font-size: 12.4pt;
     margin: 20pt 0 7pt 0; text-align: left; page-break-after: avoid; }
h3 { font-family: "DejaVu Sans", Helvetica, sans-serif; font-size: 10.8pt;
     margin: 14pt 0 5pt 0; text-align: left; page-break-after: avoid; }
h4 { font-family: "DejaVu Sans", Helvetica, sans-serif; font-size: 10.2pt;
     margin: 12pt 0 4pt 0; text-align: left; page-break-after: avoid; }
p { margin: 0 0 7pt 0; }
blockquote { margin: 8pt 0 8pt 14pt; padding-left: 10pt;
             border-left: 2px solid #b9c2c9; color: #33393f; font-style: italic; }
code, pre { font-family: "DejaVu Sans Mono", monospace; font-size: 9.2pt; }
pre { background: #f4f6f7; padding: 7pt 9pt; margin: 8pt 0; white-space: pre-wrap;
      border-radius: 3px; page-break-inside: avoid; }
table { border-collapse: collapse; width: 100%; margin: 9pt 0 11pt 0;
        font-family: "DejaVu Sans", Helvetica, sans-serif; font-size: 8.9pt;
        page-break-inside: avoid; }
th, td { border-bottom: 0.6pt solid #ccd2d7; padding: 3.4pt 5pt;
         text-align: left; vertical-align: top; }
th { border-bottom: 1pt solid #6e7c87; font-weight: bold; }
figure.fig { margin: 13pt 0 15pt 0; page-break-inside: avoid; text-align: center; }
figure.fig img { max-width: 100%; height: auto; }
/* genis sekiller: altyazisiyla birlikte tek gorsele derlenip dondurulmus hali.
   CSS transform kullanilmiyor — ekranda saran altyazi baskida sarmiyor,
   dondurulmus blok sonraki sayfaya tasiyordu. */
.figtam { page-break-after: always; page-break-inside: avoid;
          margin: 0; text-align: center; }
.figtam img { width: 100%; height: auto; }
figcaption { font-family: "DejaVu Sans", Helvetica, sans-serif; font-size: 8.7pt;
             line-height: 1.42; color: #33393f; text-align: left;
             margin-top: 5pt; }
hr { border: 0; border-top: 0.6pt solid #d3d9dd; margin: 14pt 0; }
.tblok { page-break-inside: avoid; }
.tblok > p { margin-bottom: 3pt; }
strong { font-weight: bold; }
h1 + p { font-size: 11pt; margin-bottom: 12pt; text-align: left; }
ol { padding-left: 16pt; margin: 6pt 0 0 0; }
ol li { margin-bottom: 4.5pt; font-size: 9.6pt; line-height: 1.42;
        text-align: left; }
"""

HTML = ("<!doctype html><html lang='en'><head><meta charset='utf-8'>"
        "<title>meryemAircraft</title><style>%s</style></head><body>%s</body></html>"
        % (CSS, GOVDE_HTML))

tmp = os.path.join(tempfile.gettempdir(), "meryemAircraft-makale.html")
os.makedirs(os.path.dirname(tmp), exist_ok=True)
open(tmp, "w").write(HTML)

# ------------------------------------------------------------------- PDF
import asyncio
from playwright.async_api import async_playwright
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
PDF = os.path.join(OUT, "pdf", "meryemAircraft-makale.pdf")
os.makedirs(os.path.dirname(PDF), exist_ok=True)

async def yaz():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path=CHROME,
                                     args=["--no-sandbox", "--font-render-hinting=none"])
        pg = await b.new_page()
        await pg.goto("file://" + tmp, wait_until="networkidle")
        await pg.pdf(path=PDF, format="A4", print_background=True,
                     margin={"top": "22mm", "bottom": "20mm",
                             "left": "20mm", "right": "20mm"},
                     display_header_footer=True,
                     header_template="<div></div>",
                     footer_template="<div style='width:100%;text-align:center;"
                                     "font:8pt DejaVu Sans,sans-serif;color:#6e7c87'>"
                                     "<span class='pageNumber'></span></div>")
        await b.close()

asyncio.run(yaz())
print("makale.md  ve  %s yazildi" % PDF)
print("yerlesen sekiller:", sirali)
