# -*- coding: utf-8 -*-
"""KAPAK MEKTUBUNU PDF'E BASAR -- paper/pdf/meryemAircraft-kapak-mektubu.pdf

NEDEN VAR. Drones kapak mektubunu PDF olarak istiyor. Metin duz metin
olarak drones-cover-letter.txt'te duruyor ve TEK KAYNAK odur; bu betik
onu okur, bicimlendirir, basar. Metni burada yeniden yazmak iki kopya
uretirdi ve bu depoda ayni adla iki icerik sorunu zaten yasandi.

Buyuk harfli tek satirlar bolum basligi sayilir; gerisi paragraf.
Imza bloku son bos satirdan sonrasidir ve girintisiz, sikisik basilir.
"""
import os, re, sys, tempfile, asyncio, html as _html

BURA = os.path.dirname(os.path.abspath(__file__))
MAKALE = os.path.abspath(os.path.join(BURA, ".."))
KAYNAK = os.path.join(MAKALE, "drones-cover-letter.txt")
PDF = os.path.join(MAKALE, "pdf", "meryemAircraft-kapak-mektubu.pdf")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CSS = """
@page { size: A4; }
body { font: 10.5pt/1.55 "DejaVu Serif", Georgia, serif; color: #1c2024;
       margin: 0; }
p { margin: 0 0 10pt 0; text-align: justify; }
h2 { font: bold 9pt/1.3 "DejaVu Sans", Arial, sans-serif; color: #2f6f8f;
     letter-spacing: .06em; margin: 16pt 0 7pt 0; text-transform: uppercase; }
.imza { margin-top: 18pt; }
.imza p { margin: 0; text-align: left; }
.tarih { text-align: right; color: #6e7c87; font-size: 9pt; margin-bottom: 14pt; }
"""


def kur(metin):
    # Paragraflar bos satirla ayrilir. Metin icindeki satir sonlari
    # yalnizca sarma icindir; birlestirilir.
    parcalar = [p.strip() for p in metin.split("\n\n") if p.strip()]
    govde, imza = [], []
    for i, p in enumerate(parcalar):
        duz = " ".join(p.split())
        # BASLIK: tek satir, tamami buyuk harf.
        if "\n" not in p and duz == duz.upper() and len(duz) < 60:
            govde.append("<h2>%s</h2>" % _html.escape(duz))
        elif p.startswith("Yours sincerely"):
            imza = parcalar[i:]
            break
        else:
            govde.append("<p>%s</p>" % _html.escape(duz))
    imza_html = "".join(
        "<p>%s</p>" % _html.escape(s) if s.strip() else "<p>&nbsp;</p>"
        for blok in imza for s in blok.split("\n"))
    return ("<!doctype html><meta charset='utf-8'><style>%s</style>"
            "%s<div class='imza'>%s</div>" % (CSS, "".join(govde), imza_html))


async def bas(html):
    from playwright.async_api import async_playwright
    tmp = os.path.join(tempfile.gettempdir(), "kapak.html")
    open(tmp, "w", encoding="utf-8").write(html)
    os.makedirs(os.path.dirname(PDF), exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path=CHROME,
                                     args=["--no-sandbox",
                                           "--font-render-hinting=none"])
        pg = await b.new_page()
        await pg.goto("file://" + tmp, wait_until="networkidle")
        await pg.pdf(path=PDF, format="A4", print_background=True,
                     margin={"top": "24mm", "bottom": "22mm",
                             "left": "24mm", "right": "24mm"})
        await b.close()


if __name__ == "__main__":
    if not os.path.exists(KAYNAK):
        sys.exit("kaynak yok: %s" % KAYNAK)
    asyncio.run(bas(kur(open(KAYNAK, encoding="utf-8").read())))
    print("%s yazildi (%.1f KB)" % (PDF, os.path.getsize(PDF) / 1024))
