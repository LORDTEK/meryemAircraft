import asyncio, os, math
from playwright.async_api import async_playwright
from PIL import Image, ImageChops
S="/tmp/claude-0/-home-user-meryemAircraft/dec69a2c-0837-54ea-ab5a-1b131a81b67f/scratchpad"
CHROME="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
HIDE="""document.querySelectorAll('.viewtag,.hint,.scalebar,.warn').forEach(e=>e.style.display='none');
        const a=document.querySelector('aside'); if(a)a.style.display='none';
        const st=document.querySelector('.stage');
        st.style.cssText='position:fixed;left:0;top:0;width:100vw;height:100vh;z-index:99999;margin:0;padding:0;border:0';
        const cv=document.getElementById('gl');
        cv.style.cssText='width:100%;height:100%;display:block';
        document.documentElement.setAttribute('data-theme','light');
        document.documentElement.style.setProperty('--canvas-top','#FFFFFF');document.documentElement.style.setProperty('--canvas-bot','#FFFFFF');window.dispatchEvent(new Event('resize'));"""

def autocrop(path, pad=24, bg=None):
    im=Image.open(path).convert("RGB")
    if bg is None: bg=im.getpixel((2,2))
    diff=ImageChops.difference(im, Image.new("RGB",im.size,bg)).convert("L")
    bb=diff.point(lambda p: 255 if p>6 else 0).getbbox()
    if not bb: return im,bg
    l,t,r,b=bb
    l=max(0,l-pad); t=max(0,t-pad); r=min(im.width,r+pad); b=min(im.height,b+pad)
    return im.crop((l,t,r,b)), bg

async def render(views, hat="hafif", stand=False, w=1800, h=1300, scale=2, rmul=1.18, outdir=None):
    """views: {ad:(az,el)} -> {ad: dosya yolu}. Ayni r kullanilir (ayni olcek)."""
    outdir=outdir or S+"/raw"; os.makedirs(outdir,exist_ok=True)
    res={}
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path=CHROME,
            args=["--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader","--no-sandbox"])
        pg=await b.new_page(viewport={"width":w,"height":h},device_scale_factor=scale)
        await pg.goto("file://"+S+"/render-model.html", wait_until="load"); await pg.wait_for_timeout(2500)
        await pg.evaluate(HIDE)
        await pg.evaluate("__fig.toggle('grid',false); __fig.toggle('stations',false);")
        await pg.evaluate(f"__fig.hat('{hat}')"); await pg.wait_for_timeout(900)
        await pg.evaluate(f"__fig.toggle('stand',{'true' if stand else 'false'})")
        fr=await pg.evaluate(f"__fig.frameAll({rmul})")
        r=fr['r']
        for name,(az,el) in views.items():
            await pg.evaluate(f"__fig.setCam({{az:{az},el:{el},r:{r}}})")
            await pg.wait_for_timeout(500)
            p=f"{outdir}/{hat}{'-stand' if stand else ''}-{name}.png"
            await pg.locator("#gl").screenshot(path=p); res[name]=p
        await b.close()
    return res, r
