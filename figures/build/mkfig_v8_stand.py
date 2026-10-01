"""v8 Sekil 1: ucak kuyrugunun ustunde dururken, ust capraz gorunus (yazarin istegi, Tur 202:
"Kuyrugunun ustune otururken ust caprazdan bir resim"). 50 kg referans tasarim ("hafif" hat), modelin
dik durus kipi (figures/source/body-study.html, show.stand; yer izgarasi yere basan duzlemde).
Etiket ve olcek cubugu yok (perspektifte tek bir olcek yanlis okunur); aciklik altyazida, govdedeki deger. Sekildeki her ad ve durum govdede tanimli (gorsel oncul kurali, Tur 103).
Calistirma: python3 figures/build/mkfig_v8_stand.py  (playwright + Chromium gerekir)
"""
import asyncio, os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import model_hazirla, HIDE, autocrop, CHROME
from playwright.async_api import async_playwright
from PIL import Image, ImageDraw, ImageFont
import matplotlib

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(KOK, "figures", "output", "v8-f1-standing.png")
TMP = "/tmp/meryemAircraft-render/stand"
AZ, EL = -0.62, float(os.environ.get("EL", "0.55"))   # kamera: govdeye gore yatay aci, yukseklik (radyan)
W, H, SC, RMUL = 1600, 1400, 2, 1.45
INK = (28, 32, 36)
FD = os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")

async def main():
    os.makedirs(TMP, exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path=CHROME,
            args=["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--no-sandbox"])
        pg = await b.new_page(viewport={"width": W, "height": H}, device_scale_factor=SC)
        await pg.goto("file://" + model_hazirla(), wait_until="load"); await pg.wait_for_timeout(2500)
        await pg.evaluate(HIDE)
        await pg.evaluate("__fig.toggle('stations',false); __fig.toggle('grid',true);")
        await pg.evaluate("__fig.hat('hafif')"); await pg.wait_for_timeout(900)
        # pala sayisi hesap kodundakiyle ayni: burun ve uc rotorlari iki palali (aero/nose_propeller_altitude.py "2 pala", aero/tip_propeller.py B = 2)
        await pg.evaluate("__fig.P.bladesF=2; __fig.P.bladesR=2; __fig.toggle('stand',true); __fig.rebuild();"); await pg.wait_for_timeout(600)
        fr = await pg.evaluate(f"__fig.frameAll({RMUL})")
        span = await pg.evaluate("__fig.bounds().span")
        await pg.evaluate(f"__fig.setCam({{az:{AZ},el:{EL},r:{fr['r']}}})"); await pg.wait_for_timeout(700)
        p0 = TMP + "/stand-nogrid.png"
        await pg.evaluate("__fig.toggle('grid',false); __fig.rebuild();"); await pg.wait_for_timeout(500)
        await pg.evaluate(f"__fig.setCam({{az:{AZ},el:{EL},r:{fr['r']}}})"); await pg.wait_for_timeout(500)
        await pg.locator("#gl").screenshot(path=p0)
        await pg.evaluate("__fig.toggle('grid',true); __fig.rebuild();"); await pg.wait_for_timeout(500)
        await pg.evaluate(f"__fig.setCam({{az:{AZ},el:{EL},r:{fr['r']}}})"); await pg.wait_for_timeout(500)
        p = TMP + "/stand.png"
        await pg.locator("#gl").screenshot(path=p)
        await b.close()
    return p0, p, fr["r"], span

p0, p, r, span = asyncio.run(main())
# ucagin kutusu izgarasiz goruntuden; izgarali goruntu o kutunun biraz genisletilmisiyle kirpilir
from PIL import ImageChops
g = Image.open(p0).convert("RGB"); bg = Image.new("RGB", g.size, g.getpixel((2, 2)))
bx = ImageChops.difference(g, bg).convert("L").point(lambda v: 255 if v > 12 else 0).getbbox()
mx, my = int(0.10 * (bx[2] - bx[0])), int(0.10 * (bx[3] - bx[1]))
im = Image.open(p).convert("RGB").crop((max(0, bx[0] - mx), max(0, bx[1] - my), min(g.width, bx[2] + mx), min(g.height, bx[3] + my)))
im.save(OUT, dpi=(600, 600))
print("Sekil:", OUT, im.size, "| span", round(span, 3), "m | el", EL)
