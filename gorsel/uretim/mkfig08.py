import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, math
from matplotlib.patches import Circle, Polygon
OUT="/home/user/meryemAircraft/gorsel/cikti"; D2R=math.pi/180
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
 "figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
INK="#1C2024"; MUT="#6E7C87"; A="#2F6F8F"; R="#B03A2E"; TEAL="#1F8A8A"

# --- planform (Sekil 6 ile ayni yasalar) ---
rc,sr,st,ste,crop=0.97,45.0,35.0,25.0,67.0
def conv_span():
    lo,hi=0.1,60*rc
    for _ in range(200):
        mid=(lo+hi)/2; n=3000; step=mid/n; x=0.0; y=0.0; hit=None
        for i in range(n):
            s=(sr+(st-sr)*min((y+step/2)/mid,1))*D2R
            x+=math.tan(s)*step; y+=step
            if rc+y*math.tan(ste*D2R)-x<=0: hit=y; break
        if hit is None: lo=mid
        else: hi=mid
        if abs(hi-lo)<1e-7: break
    return (lo+hi)/2
conv=conv_span(); half=conv*crop/100
n=600; ys=np.linspace(0,half,n); LE=np.zeros(n); acc=0.0
for i in range(1,n):
    step=ys[i]-ys[i-1]
    s=(sr+(st-sr)*min((ys[i]-step/2)/conv,1))*D2R
    acc+=math.tan(s)*step; LE[i]=acc
TE=rc+ys*math.tan(ste*D2R)

# --- serit ---
zA0=rc*0.15; L=rc*1.20
uu=np.linspace(0,1,300); sx=uu*L; sz=zA0+uu*L
# --- iz siniri: 0.67 -> 0.47, kok veteri boyunca ---
r0,r1=0.67,0.47
def rz(z): return np.where(z<=rc, r0+(r1-r0)*np.clip(z,0,rc)/rc, r1)
# kesisim
uc=(r0-(r0-r1)*zA0/rc)/(L+(r0-r1)*L/rc)
xc,zc=uc*L, zA0+uc*L
print(f"yari-aciklik {half:.4f} m   serit dis ucu {L:.3f} m = %{100*L/half:.1f}")
print(f"iz: %{100*r0/half:.1f} -> %{100*r1/half:.1f} yari-aciklik")
print(f"kesisim: u={uc:.3f} ({100*uc:.1f}% serit boyu)  x={xc:.3f} m = %{100*xc/half:.1f} yari-aciklik")

fig,ax=plt.subplots(figsize=(9.6,8.2))
zz=np.linspace(0,1.45,300); rr=rz(zz)
ax.fill_betweenx(zz,-rr,rr,color="#E7F2F2",zorder=1)
ax.plot(rr,zz,color=TEAL,lw=1.5,ls=(0,(5,3)),zorder=3)
ax.plot(-rr,zz,color=TEAL,lw=1.5,ls=(0,(5,3)),zorder=3)
poly=np.concatenate([np.stack([ys,LE],1),np.stack([ys[::-1],TE[::-1]],1)])
polym=poly.copy(); polym[:,0]*=-1
for pp in (poly,polym):
    ax.add_patch(Polygon(pp,closed=True,fc="#F5F0E2",ec="#B9AE93",lw=1.6,zorder=2))
ax.add_patch(Circle((0,0),0.60,fill=False,ec=A,lw=2.0,zorder=4))
for sd in (1,-1):
    inb=uu<=uc; outb=uu>=uc
    ax.plot(sd*sx[inb],sz[inb],color=TEAL,lw=5.0,solid_capstyle="round",zorder=6)
    ax.plot(sd*sx[outb],sz[outb],color=R,lw=5.0,solid_capstyle="round",zorder=6)
ax.plot([xc,-xc],[zc,zc],"o",ms=8,mfc="white",mec=INK,mew=1.8,zorder=7)
# etiketler
ax.annotate("main propeller\n$D$ = 1.20 m",xy=(-0.44,-0.41),xytext=(-2.30,-0.60),
            fontsize=10.4,color=A,ha="left",va="center",linespacing=1.4,
            arrowprops=dict(arrowstyle="-",color=A,lw=0.9))
ax.annotate("inboard 46 % of the strip lies inside\nthe slipstream  →  authority at zero\nairspeed, where $q_\\infty$ is nil",
            xy=(0.291,0.437),xytext=(0.92,-0.60),fontsize=10.2,color=TEAL,ha="left",va="center",
            linespacing=1.5,arrowprops=dict(arrowstyle="->",color=TEAL,lw=1.1))
ax.annotate("outboard 54 % lies outside it\n→  roll in cruise",
            xy=(-1.02,1.16),xytext=(-2.38,0.44),fontsize=10.2,color=R,ha="left",va="center",
            linespacing=1.5,arrowprops=dict(arrowstyle="->",color=R,lw=1.1))
ax.annotate("2 cm",xy=(0.02,0.155),xytext=(-0.62,-0.08),fontsize=10,color=INK,
            ha="right",va="center",arrowprops=dict(arrowstyle="->",color=INK,lw=0.9))
ax.annotate("6 cm  ·  outer end at\n67 % of semi-span",xy=(1.164,1.305),xytext=(1.42,1.66),
            fontsize=10,color=INK,ha="left",va="center",linespacing=1.45,
            arrowprops=dict(arrowstyle="->",color=INK,lw=0.9))
ax.annotate("slipstream boundary\n0.67 m  →  0.47 m",xy=(0.52,1.62),xytext=(0.10,2.24),
            fontsize=10.4,color=TEAL,ha="center",va="center",linespacing=1.45,
            arrowprops=dict(arrowstyle="->",color=TEAL,lw=1.0))
ax.plot([half],[TE[-1]],"|",ms=11,color=MUT,mew=1.6)
ax.text(half+0.06,TE[-1]+0.16,"tip\n$b/2$ = 1.73 m",ha="center",va="top",fontsize=9.6,
        color=MUT,linespacing=1.35)
ax.set_xlim(-2.40,2.30); ax.set_ylim(2.45,-0.95); ax.set_aspect("equal"); ax.axis("off")
ax.set_title("Roll strip and the main-propeller slipstream — view from below",
             loc="left",fontsize=12.8,fontweight="bold",pad=8)
ax.text(-2.40,2.62,"One device, two regimes. The strip is on the lower surface, inclined at 45°, "
        "and deploys on–off.\nIn hover the slipstream supplies the dynamic pressure "
        "($q = T/A$ = 433 Pa) that the freestream cannot.",
        fontsize=9.6,color=MUT,linespacing=1.7,va="top")
fig.savefig(OUT+"/sekil08-kanatcik-iz.png",dpi=300,bbox_inches="tight")
fig.savefig(OUT+"/sekil08-kanatcik-iz.svg",bbox_inches="tight"); print("Sekil 8 yazildi")
