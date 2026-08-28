import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, math
from matplotlib.patches import Polygon as MPoly
OUT="/home/user/meryemAircraft/patent/resimler"
import os; os.makedirs(OUT,exist_ok=True)
D2R=math.pi/180
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,
 "figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
K="black"; LW=1.5; LWT=1.1     # patent: duz siyah cizgi, golge yok

# ---------- geometri ----------
rc,sr,st,ste,crop=0.97,45.0,35.0,25.0,67.0
refl=0.03; propD=1.20; propD2=0.20; tipPost=300.0; tipStub=5.0; tipTube=4.0
def conv_span():
    lo,hi=0.1,60*rc
    for _ in range(160):
        mid=(lo+hi)/2; n=2500; step=mid/n; x=0.0; y=0.0; hit=None
        for i in range(n):
            s=(sr+(st-sr)*min((y+step/2)/mid,1))*D2R
            x+=math.tan(s)*step; y+=step
            if rc+y*math.tan(ste*D2R)-x<=0: hit=y; break
        if hit is None: lo=mid
        else: hi=mid
    return (lo+hi)/2
conv=conv_span(); half=conv*crop/100
NP=260; ysp=np.linspace(0,half,NP); LE=np.zeros(NP); acc=0.0
for i in range(1,NP):
    stp=ysp[i]-ysp[i-1]
    s=(sr+(st-sr)*min((ysp[i]-stp/2)/conv,1))*D2R
    acc+=math.tan(s)*stp; LE[i]=acc
TE=rc+ysp*math.tan(ste*D2R)
ct=TE[-1]-LE[-1]; le=LE[-1]
Lp=ct*tipPost/100; Ls=ct*tipStub/100; rad=ct*tipTube/100/2
X0=half+rad*0.6
zLE=-le; zTE=-(le+ct); yTE=refl*ct
zGround=zTE-Ls; yKeel=refl*rc; zKeelS=-rc
print(f"half={half:.4f} ct={ct:.4f} le={le:.4f} Lp={Lp:.4f} Ls={Ls:.4f} zGround={zGround:.4f}")

# ---------- 3B parcalar: (x, y, z) ; z akis yonu (burun 0, arka negatif) ----------
def planform():
    up=[(x,0,-l) for x,l in zip(ysp,LE)]
    dn=[(x,0,-t) for x,t in zip(ysp[::-1],TE[::-1])]
    r=up+dn
    lft=[(-a,b,c) for a,b,c in r]
    return r+lft[::-1]

def disc(cx,cy,cz,D,n=96):
    a=np.linspace(0,2*math.pi,n)
    return [(cx+D/2*math.cos(t), cy+D/2*math.sin(t), cz) for t in a]

def frames():
    segs=[]
    for sd in (-1,1):
        X=sd*X0
        segs.append([(X,0,zLE),(X,yTE,zTE)])
        segs.append([(X,-Lp,zLE),(X,Lp,zLE)])
        segs.append([(X,yTE-Lp,zTE),(X,yTE+Lp,zTE)])
        segs.append([(X,yTE+Lp,zTE),(X,yTE+Lp,zGround)])
        segs.append([(X,yTE-Lp,zTE),(X,yTE-Lp,zGround)])
    segs.append([(0,yKeel,zKeelS),(0,yKeel,zGround)])
    return segs

def tipdiscs():
    d=[]
    for sd in (-1,1):
        X=sd*X0
        for yy in (Lp,-Lp): d.append(disc(X,yy,zLE,propD2))
    return d

def strip3d():
    zA0=rc*0.15; L=rc*1.20
    u=np.linspace(0,1,120); out=[]
    for sd in (1,-1):
        out.append([(sd*uu*L, -0.02, -(zA0+uu*L)) for uu in u])
    return out

# ---------- izdusum ----------
def proj(pts,az,el):
    ca,sa=math.cos(az),math.sin(az); ce,se=math.cos(el),math.sin(el)
    o=[]
    for x,y,z in pts:
        X=x*ca+z*sa
        Zt=-x*sa+z*ca
        Y=y*ce-Zt*se
        o.append((X,Y))
    return o

def draw(ax,az,el,show=("body","mainprop","frames","tipprops","strip")):
    if "body" in show:
        p=proj(planform(),az,el)
        ax.add_patch(MPoly(p,closed=True,fc="white",ec=K,lw=LW,zorder=5))
    if "mainprop" in show:
        for gz in (0.0,-0.06):
            ax.add_patch(MPoly(proj(disc(0,0,gz,propD),az,el),closed=True,
                               fc="none",ec=K,lw=LWT,zorder=7))
    if "frames" in show:
        for sg in frames():
            q=proj(sg,az,el); ax.plot(*zip(*q),color=K,lw=LW,zorder=6,solid_capstyle="round")
    if "strip" in show:
        for sgl in strip3d():
            q=proj(sgl,az,el); ax.plot(*zip(*q),color=K,lw=2.6,zorder=9,solid_capstyle="round")
    if "tipprops" in show:
        for d in tipdiscs():
            ax.add_patch(MPoly(proj(d,az,el),closed=True,fc="white",ec=K,lw=LWT,zorder=8))
    ax.set_aspect("equal"); ax.axis("off")

def ref(ax,txt,xy,xytext):
    ax.annotate(txt,xy=xy,xytext=xytext,fontsize=13,color=K,ha="center",va="center",
                arrowprops=dict(arrowstyle="-",color=K,lw=0.9,shrinkA=2,shrinkB=2))


from PIL import Image as _I, ImageChops as _IC
def _trim(p,pad=26):
    im=_I.open(p).convert("RGB"); bg=im.getpixel((1,1))
    d=_IC.difference(im,_I.new("RGB",im.size,bg)).convert("L")
    bb=d.point(lambda x:255 if x>8 else 0).getbbox()
    if not bb: return
    l,t2,r,b=bb
    im.crop((max(0,l-pad),max(0,t2-pad),min(im.width,r+pad),min(im.height,b+pad))).save(p)

AZ,EL=-0.62,1.00
def PP(az,el):
    return lambda p: proj([p],az,el)[0]

def sekil(no,az,el,show,refs,figsize=(9.2,7.4),extra=None):
    fig,ax=plt.subplots(figsize=figsize)
    draw(ax,az,el,show=show)
    P=PP(az,el)
    if extra: extra(ax,P)
    lab=[]
    for txt,tgt,off in refs:
        p=P(tgt); q=(p[0]+off[0],p[1]+off[1]); ref(ax,txt,p,q); lab.append(q)
    if lab:   # etiketleri autoscale'e dahil et
        ax.plot([a for a,_ in lab],[b for _,b in lab],linestyle="none",marker="o",
                markersize=0.1,alpha=0.0)
    ax.margins(0.16)
    fig.savefig(f"{OUT}/sekil-{no}.png",dpi=300,bbox_inches="tight")
    fig.savefig(f"{OUT}/sekil-{no}.svg",bbox_inches="tight"); plt.close(fig)
    _trim(f"{OUT}/sekil-{no}.png")
    print("  Sekil",no)

FULL=("body","mainprop","frames","tipprops","strip")

# ---- Sekil 1: perspektif ----
sekil(1,AZ,EL,FULL,[
 ("1",(1.05,0,-1.05),(0.55,-0.30)),
 ("2",(0.0,propD/2,0.0),(-0.62,0.42)),
 ("3",(X0,0.0,zLE-ct*0.5),(0.60,-0.22)),
 ("3a",(X0,Lp*0.6,zLE),(0.46,0.34)),
 ("3b",(-X0,-Lp*0.6,zLE),(-0.50,-0.34)),
 ("4",(X0,Lp,zLE),(0.42,0.40)),
 ("5",(0.62,-0.02,-(rc*0.15+0.62)),(-0.30,-0.52)),
 ("6",(0,yKeel,(zKeelS+zGround)/2),(0.58,0.16)),
])

# ---- Sekil 2: ustten ----
sekil(2,0.0,math.pi/2-1e-4,FULL,[
 ("1",(0.95,0,-0.95),(0.52,-0.26)),
 ("2",(0.42,0,0.0),(0.34,0.40)),
 ("3",(X0,0,zLE-ct*0.5),(0.42,0.0)),
 ("4",(X0,Lp,zLE),(0.34,0.34)),
 ("5",(0.62,-0.02,-(rc*0.15+0.62)),(-0.34,-0.30)),
 ("6",(0,yKeel,(zKeelS+zGround)/2),(0.42,-0.10)),
])

# ---- Sekil 3: onden ----
sekil(3,0.0,0.0,FULL,[
 ("1",(1.25,0,-0.9),(0.10,-0.30)),
 ("2",(propD/2*0.7,propD/2*0.7,0),(0.34,0.34)),
 ("3a",(X0,Lp*0.55,zLE),(0.40,0.16)),
 ("3b",(X0,-Lp*0.55,zLE),(0.40,-0.16)),
 ("4",(X0,Lp,zLE),(0.20,0.34)),
],figsize=(9.6,6.2))

# ---- Sekil 4: alttan, serit ve iz ----
def izler(ax,P):
    r0,r1=0.67,0.47
    for sd in (1,-1):
        zz=np.linspace(0,1.90,80)
        rr=np.where(zz<=rc, r0+(r1-r0)*np.clip(zz,0,rc)/rc, r1)
        q=[P((sd*a,0,-b)) for a,b in zip(rr,zz)]
        ax.plot(*zip(*q),color=K,lw=1.0,ls=(0,(6,4)),zorder=10)
sekil(4,0.0,-(math.pi/2-1e-4),FULL,[
 ("1",(1.05,0,-1.05),(0.50,0.26)),
 ("2",(0.42,0,0.0),(0.34,-0.40)),
 ("5",(0.75,-0.02,-(rc*0.15+0.75)),(0.40,0.26)),
 ("13",(-0.526,0,-0.70),(-1.62,0.46)),
 ("6",(0,yKeel,(zKeelS+zGround)/2),(0.44,0.12)),
],extra=izler)
print("Sekil 1-4 tamam")


# ================= SEKIL 5 — seri hibrit guc akis semasi =================
from matplotlib.patches import FancyArrow, Rectangle
fig,ax=plt.subplots(figsize=(12.4,4.8))
BW,BH=2.25,1.60
kut=[("11\nYAKIT DEPOSU",0.0),("7\nİÇTEN YANMALI\nMOTOR",3.1),
     ("8\nJENERATÖR",6.2),("10\nELEKTRİK\nMOTORLARI",9.3)]
for txt,x in kut:
    ax.add_patch(Rectangle((x,0),BW,BH,fc="white",ec=K,lw=LW))
    ax.text(x+BW/2,BH/2,txt,ha="center",va="center",fontsize=11.5,linespacing=1.35)
for x in (2.25,5.35,8.45):
    ax.annotate("",xy=(x+0.85,BH/2),xytext=(x,BH/2),
                arrowprops=dict(arrowstyle="-|>",color=K,lw=LW,mutation_scale=17))
# pil tamponu
ax.add_patch(Rectangle((5.8,-2.30),BW,1.10,fc="white",ec=K,lw=LW))
ax.text(5.8+BW/2,-2.30+0.55,"9\nPİL TAMPONU",ha="center",va="center",fontsize=11.5,linespacing=1.35)
ax.annotate("",xy=(6.95,-0.02),xytext=(6.95,-1.18),
            arrowprops=dict(arrowstyle="-|>",color=K,lw=LW,mutation_scale=17))
ax.annotate("",xy=(7.30,-1.18),xytext=(7.30,-0.02),
            arrowprops=dict(arrowstyle="-|>",color=K,lw=LW,mutation_scale=17))
# pervanelere dagilim
ax.add_patch(Rectangle((12.4,0.95),2.05,1.15,fc="white",ec=K,lw=LW))
ax.text(12.4+1.025,0.95+0.575,"2\nBURUN ÇİFTİ",ha="center",va="center",fontsize=11,linespacing=1.35)
ax.add_patch(Rectangle((12.4,-1.30),2.05,1.15,fc="white",ec=K,lw=LW))
ax.text(12.4+1.025,-1.30+0.575,"4\nUÇ ÇİFTLERİ",ha="center",va="center",fontsize=11,linespacing=1.35)
ax.plot([11.55,11.95],[BH/2,BH/2],color=K,lw=LW)
ax.plot([11.95,11.95],[-0.72,1.52],color=K,lw=LW)
for yy in (1.52,-0.72):
    ax.annotate("",xy=(12.4,yy),xytext=(11.95,yy),
                arrowprops=dict(arrowstyle="-|>",color=K,lw=LW,mutation_scale=17))
ax.text(6.95,-2.68,"(askı tepesi)",ha="center",fontsize=10,style="italic")
ax.set_xlim(-0.6,15.1); ax.set_ylim(-3.2,2.4); ax.set_aspect("equal"); ax.axis("off")
fig.savefig(OUT+"/sekil-5.png",dpi=300,bbox_inches="tight")
_trimlater=True
fig.savefig(OUT+"/sekil-5.svg",bbox_inches="tight"); plt.close(fig)
print("  Sekil 5")

_trim(OUT+"/sekil-5.png")
print("kirpma tamam")
