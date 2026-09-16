# -*- coding: utf-8 -*-
"""EK MALZEMEYI PDF'E BASAR -- paper/pdf/meryemAircraft-ek.pdf

NEDEN VAR. Zenodo kaydina ve dergiye gidecek ek malzeme simdiye kadar
yalniz markdown olarak vardi. Hakem alti eki tek bir PDF'te ister; okuyucu
da oyle. Makalenin PDF'i mkpaper.py'den cikiyor, bu betik ayni CSS ile
ekleri basar -- iki cikti ayni gorunsun diye stil oradan ITHAL EDILIYOR,
kopyalanmiyor; kopyalasaydim ikisi zamanla ayrisirdi.

Sekil yok, oyle olmali: her sekil govdede.
"""
import os, re, sys, tempfile, asyncio

BURA = os.path.dirname(os.path.abspath(__file__))
MAKALE = os.path.abspath(os.path.join(BURA, ".."))
sys.path.insert(0, BURA)

from version import SURUM   # elle kopyalanmis "v6" idi; artik tek kaynak
KAYNAK = os.path.join(MAKALE, "paper-%s-supp.md" % SURUM)
PDF = os.path.join(MAKALE, "pdf", "meryemAircraft-ek.pdf")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"


def stil():
    """mkpaper.py'nin CSS'ini calistirmadan ceker."""
    s = open(os.path.join(BURA, "mkpaper.py"), encoding="utf-8").read()
    m = re.search(r'^CSS = """(.*?)"""', s, re.M | re.S)
    if not m:
        sys.exit("mkpaper.py icinde CSS bulunamadi")
    return m.group(1)


def markdown_html(md):
    try:
        import markdown
    except ImportError:
        sys.exit("markdown paketi yok: pip install markdown")
    return markdown.markdown(
        md, extensions=["tables", "fenced_code", "sane_lists", "attr_list"])


async def bas(html):
    from playwright.async_api import async_playwright
    tmp = os.path.join(tempfile.gettempdir(), "meryemAircraft-ek.html")
    open(tmp, "w", encoding="utf-8").write(html)
    os.makedirs(os.path.dirname(PDF), exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch(
            executable_path=CHROME,
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


if __name__ == "__main__":
    if not os.path.exists(KAYNAK):
        sys.exit("once mkrelease.py calistirin: %s yok" % KAYNAK)
    md = open(KAYNAK, encoding="utf-8").read()
    html = ("<!doctype html><html lang='en'><head><meta charset='utf-8'>"
            "<title>meryemAircraft — Supplementary Material</title>"
            "<style>%s</style></head><body>%s</body></html>"
            % (stil(), markdown_html(md)))
    asyncio.run(bas(html))
    print("%s yazildi (%.1f MB)" % (PDF, os.path.getsize(PDF) / 1e6))
