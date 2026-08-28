import asyncio, sys, math, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import render, autocrop, S
from PIL import Image, ImageDraw, ImageFont
import matplotlib
FD=os.path.join(os.path.dirname(matplotlib.__file__),"mpl-data","fonts","ttf")
def F(sz,b=False): return ImageFont.truetype(os.path.join(FD,"DejaVuSans%s.ttf"%("-Bold" if b else "")),sz)
OUT="/home/user/meryemAircraft/gorsel/cikti"
INK=(28,32,36); MUT=(110,120,128); A=(47,111,143); GR=(198,204,209); PAPER=(255,255,255)

res,r=asyncio.run(render({"side":(math.pi/2,0.0)},"hafif",w=1500,h=1100,scale=2,rmul=1.3))
sil,_=autocrop(res["side"],pad=8)
sil=sil.convert("RGBA")
# beyazi seffaf yap
px=sil.load()
for j in range(sil.height):
    for i in range(sil.width):
        rr,gg,bb,aa=px[i,j]
        if rr>247 and gg>247 and bb>247: px[i,j]=(255,255,255,0)
sil.thumbnail((330,330),Image.LANCZOS)

# asamalar: (etiket, aciklama, govde acisi deg, x, y)
FA=[("1  Stance","five contact points\nno launch equipment",90),
    ("2  Vertical take-off","nose pair above weight\nattitude held by tip pairs",90),
    ("3  Transition","rotate while climbing\nno altitude loss",45),
    ("4  Cruise","wing-borne, tailless\nnose pair at design point",0),
    ("5  Landing","reverse of transition\nsensor-referenced descent",90)]
W,H=2560,1240; PAD=80
fig=Image.new("RGB",(W,H),PAPER); d=ImageDraw.Draw(fig)
gy=H-300                      # zemin
d.line([(PAD,gy),(W-PAD,gy)],fill=GR,width=3)
xs=[PAD+150, PAD+600, PAD+1130, PAD+1690, PAD+2170]
yy=[None,   gy-390,  gy-540,   gy-560,   None]     # None = zemine otur
imgs=[]
for (lab,sub,ang),cx in zip(FA,xs):
    im=sil.rotate(-ang,expand=True,resample=Image.BICUBIC)
    imgs.append(im)
poz=[]
for k,((lab,sub,ang),cx,im) in enumerate(zip(FA,xs,imgs)):
    cy = (gy-im.height//2) if yy[k] is None else yy[k]
    poz.append((cx,cy))
# yorunge: 1 -> 4
d.line([(poz[0][0]+40,poz[0][1]-60),(poz[1][0],poz[1][1]+40),
        (poz[2][0],poz[2][1]+20),(poz[3][0],poz[3][1]+10)],fill=(224,229,233),width=5)
for (lab,sub,ang),(cx,cy),im in zip(FA,poz,imgs):
    fig.paste(im,(cx-im.width//2, cy-im.height//2), im)
for (lab,sub,ang),cx in zip(FA,xs):
    ty=gy+52
    d.text((cx-160,ty),lab,font=F(30,True),fill=INK)
    d.text((cx-160,ty+44),sub,font=F(24),fill=MUT,spacing=8)
d.text((PAD,44),"Flight profile — five phases",font=F(38,True),fill=INK)
d.text((PAD,96),"Body angle measured from the vertical. The aircraft rotates; nothing on the aircraft rotates relative to it.",
       font=F(25),fill=MUT)
fig.save(OUT+"/sekil09-ucus-profili.png"); print("Sekil 9:",fig.size)
