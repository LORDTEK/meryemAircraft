import asyncio, sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import render, autocrop, S
from PIL import Image, ImageDraw, ImageFont
import matplotlib
FD=os.path.join(os.path.dirname(matplotlib.__file__),"mpl-data","fonts","ttf")
def F(sz,b=False): return ImageFont.truetype(os.path.join(FD,"DejaVuSans%s.ttf"%("-Bold" if b else "")),px(sz))
OUT="/home/user/meryemAircraft/figures/cikti"; os.makedirs(OUT,exist_ok=True)
INK=(28,32,36); MUT=(110,120,128); PAPER=(255,255,255)
MARJ=1.42; W,H,SC=1700,1250,3

# SC, Chromium'un aygit piksel orani. 2'den 3'e cikarildi: 15 cm genislikte
# Sekil 6 yalnizca 258 dpi veriyordu ve MDPI kombinasyon sekillerinde 300'un
# altina inmiyor. Ama asagidaki butun piksel sabitleri (PAD, GAP, yazi
# boyutlari, cizgi kalinliklari) SC=2 icin yazilmisti; SC'yi tek basina
# buyutmek marjlari ve yazilari GORELI olarak kucultur, yani cozunurlugu
# duzeltirken duzeni bozar. K bunu birlikte olcekler; SC ne olursa olsun
# sekil ayni gorunur, yalnizca daha cok piksel tasir.
K = SC / 2.0
def px(n): return max(1, int(round(n * K)))

def mpp(r,hpx):            # metre / piksel (hedef derinliginde)
    return 2*r*math.tan(0.35)/hpx

def scalebar(d,x,y,px_per_m,total_w,label=None):
    """gorsel olcek cubugu: 1-2-5 serisinden uygun uzunluk"""
    target=total_w*0.22
    for m in (0.1,0.2,0.5,1,2,5,10,20):
        if m*px_per_m>=target: break
    L=m*px_per_m
    d.line([(x,y),(x+L,y)],fill=INK,width=px(3))
    for xx in (x,x+L): d.line([(xx,y-px(7)),(xx,y+px(7))],fill=INK,width=px(3))
    t=label or (f"{m:g} m")
    d.text((x+L+px(14),y-px(11)),t,font=F(24),fill=INK)

async def build():
    # --- hafif hat: dort gorunus, ayni r ---
    V={"top":(0.0,1.4499),"front":(0.0,0.0),"side":(math.pi/2,0.0),"iso":(-0.55,0.42)}
    res_h,r_h=await render(V,"hafif",w=W,h=H,scale=SC,rmul=MARJ)
    res_a,r_a=await render({"iso":(-0.55,0.42)},"agir",w=W,h=H,scale=SC,rmul=MARJ)
    print("r hafif",round(r_h,2)," r agir",round(r_a,2)," oran",round(r_a/r_h,3))
    return res_h,r_h,res_a,r_a

res_h,r_h,res_a,r_a=asyncio.run(build())
PPM_h=1.0/mpp(r_h,H*SC)     # piksel / metre (hafif)
PPM_a=1.0/mpp(r_a,H*SC)
print("piksel/metre  hafif",round(PPM_h,1)," agir",round(PPM_a,1))

# ================= SEKIL 5 : uc gorunus =================
top,_=autocrop(res_h["top"],pad=px(40))
fr,_ =autocrop(res_h["front"],pad=px(40))
sd,_ =autocrop(res_h["side"],pad=px(40))
PAD=px(70); GAP=px(70); CAP=px(52)
rowW=max(top.width, fr.width+GAP+sd.width)
Hh=CAP+top.height+GAP+CAP+max(fr.height,sd.height)
fig=Image.new("RGB",(rowW+2*PAD, Hh+2*PAD+px(80)), PAPER); d=ImageDraw.Draw(fig)
y=PAD
d.text((PAD,y),"(a)  Top view — planform",font=F(30,True),fill=INK); y+=CAP
fig.paste(top,(PAD+(rowW-top.width)//2,y)); y+=top.height+GAP
d.text((PAD,y),"(b)  Front view",font=F(30,True),fill=INK)
d.text((PAD+fr.width+GAP,y),"(c)  Side view — section",font=F(30,True),fill=INK); y+=CAP
fig.paste(fr,(PAD,y)); fig.paste(sd,(PAD+fr.width+GAP,y))
scalebar(d,PAD,fig.height-PAD-px(8),PPM_h,rowW)
fig.save(OUT+"/fig05-three-views.png",dpi=(600,600)); print("Sekil 5:",fig.size)

# ================= SEKIL 6 : serbest gorunus =================
im,_=autocrop(res_h["iso"],pad=px(50))
fig=Image.new("RGB",(im.width+2*PAD, im.height+2*PAD+px(70)), PAPER)
fig.paste(im,(PAD,PAD)); d=ImageDraw.Draw(fig)
scalebar(d,PAD,fig.height-PAD-px(8),PPM_h,im.width)
fig.save(OUT+"/fig06-general-view.png",dpi=(600,600)); print("Sekil 6:",fig.size)

# ================= SEKIL 10 : iki hat ayni olcekte =================
ih,_=autocrop(res_h["iso"],pad=px(20)); ia,_=autocrop(res_a["iso"],pad=px(20))
k=(r_h/r_a)                       # hafif'i ayni olcege kucult
ih=ih.resize((max(1,int(ih.width*k)),max(1,int(ih.height*k))),Image.LANCZOS)
GAP=px(110)
cw=ih.width+ia.width+GAP; ch=max(ih.height,ia.height)
fig=Image.new("RGB",(cw+2*PAD, ch+2*PAD+px(150)), PAPER)
d=ImageDraw.Draw(fig)
base=PAD+px(70)
fig.paste(ih,(PAD, base+ch-ih.height))
fig.paste(ia,(PAD+ih.width+GAP, base+ch-ia.height))
d.text((PAD,PAD+px(10)),"50 kg",font=F(32,True),fill=INK)
d.text((PAD+ih.width+GAP,PAD+px(10)),"1000 kg",font=F(32,True),fill=INK)
d.text((PAD,PAD+px(48)),"span 3.45 m",font=F(24),fill=MUT)
d.text((PAD+ih.width+GAP,PAD+px(48)),"span 11.55 m   ·   20x in mass, 3.35x in length",font=F(24),fill=MUT)
scalebar(d,PAD,fig.height-PAD-px(8),PPM_a,cw)
fig.save(OUT+"/fig10-two-scales.png",dpi=(600,600)); print("Sekil 10:",fig.size)
