"""Uc boyutlu modeli bassiz Chromium'da acar, kamerayi surer, goruntu alir.

Model dosyasi (gorsel/kaynak/govde-etudu.html) bir IIFE icindedir ve disaridan
surulemez. Burasi onun bir KOPYASINA render kancasi enjekte eder; kaynak dosya
degistirilmez. Kopya gecici dizine yazilir, gerekince yeniden uretilir.
"""
import asyncio, os, math, tempfile, hashlib
from playwright.async_api import async_playwright
from PIL import Image, ImageChops

BURA = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.abspath(os.path.join(BURA, "..", ".."))
MODEL = os.path.join(KOK, "gorsel", "kaynak", "govde-etudu.html")
S = os.path.join(tempfile.gettempdir(), "meryemAircraft-render")

CHROME = os.environ.get("CHROME_PATH", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")

# Modelin ic degiskenlerini disariya acan kanca. Kaynak dosyaya DOKUNULMAZ;
# yalnizca kopyaya, IIFE kapanmadan hemen once eklenir.
KANCA = """

/* ==== RENDER KANCASI — yalnizca sekil uretimi icin ==== */
window.__fig={
  cam:cam, show:show, P:P,
  setCam:function(o){ camT=null; Object.keys(o).forEach(function(k){cam[k]=o[k];}); },
  hat:function(a){ hatUygula(a); },
  rebuild:function(){ rebuild(false); },
  toggle:function(k,v){ show[k]=v; },
  bounds:function(){
    var half=M.span/2;
    var zmax=PR?PR.zTip:0, zmin=FR?Math.min(M.zMin,FR.zBack):M.zMin;
    var ytop=FR?FR.yTop:0.2, ybot=FR?FR.yBot:-0.2;
    return {xmin:-half,xmax:half,ymin:ybot,ymax:ytop,zmin:zmin,zmax:zmax,span:M.span};
  },
  /* bbox merkezine bak, tum cismi cerceveye sigdir */
  frameAll:function(marj){
    marj=marj||1.15;
    var b=this.bounds();
    cam.tx=(b.xmin+b.xmax)/2; cam.ty=(b.ymin+b.ymax)/2; cam.tz=(b.zmin+b.zmax)/2;
    var dx=b.xmax-b.xmin, dy=b.ymax-b.ymin, dz=b.zmax-b.zmin;
    var R=0.5*Math.sqrt(dx*dx+dy*dy+dz*dz);
    cam.r=marj*R/Math.tan(0.35);   /* persp fov 0.70 rad */
    camT=null;
    return {r:cam.r, R:R, b:b};
  }
};"""

CAPA = "\nrebuild(false);\ndraw();\n})();"


def model_hazirla():
    """Kancasi enjekte edilmis kopyayi uretir, yolunu doner."""
    if not os.path.exists(MODEL):
        raise FileNotFoundError("Model bulunamadi: %s" % MODEL)
    kaynak = open(MODEL, encoding="utf-8").read()
    if CAPA not in kaynak:
        raise RuntimeError(
            "Model dosyasinda enjeksiyon capasi bulunamadi. govde-etudu.html "
            "degismis olabilir; figlib.KANCA'nin nereye gireceginin yeniden "
            "belirlenmesi gerekiyor.")
    icerik = kaynak.replace(CAPA, KANCA + CAPA, 1)
    os.makedirs(S, exist_ok=True)
    hedef = os.path.join(S, "render-model.html")
    imza = hashlib.sha1(icerik.encode("utf-8")).hexdigest()
    imza_yolu = hedef + ".sha1"
    if (not os.path.exists(hedef) or not os.path.exists(imza_yolu)
            or open(imza_yolu).read().strip() != imza):
        open(hedef, "w", encoding="utf-8").write(icerik)
        open(imza_yolu, "w").write(imza)
    return hedef
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
        await pg.goto("file://"+model_hazirla(), wait_until="load"); await pg.wait_for_timeout(2500)
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
