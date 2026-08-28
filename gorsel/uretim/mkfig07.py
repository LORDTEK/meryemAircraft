import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
OUT="/home/user/meryemAircraft/gorsel/cikti"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
 "axes.edgecolor":"#3A4046","text.color":"#1C2024",
 "figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
b2=1.7264; L=0.71; Dm=1.20; Dt=0.20
INK="#1C2024"; A="#2F6F8F"; R="#B03A2E"; MUT="#6E7C87"; GR="#C6CCD1"

fig,ax=plt.subplots(figsize=(9.8,7.4))
# kanat (on gorunusten ince bir sey)
ax.plot([-b2,b2],[0,0],lw=5,color="#E4DCC8",solid_capstyle="round",zorder=2)
ax.plot([-b2,b2],[0,0],lw=1.0,color="#B9AE93",zorder=3)
# ana pervane
ax.add_patch(Circle((0,0),Dm/2,fill=False,ec=A,lw=2.4,zorder=4))
ax.plot([0],[0],"o",ms=7,color=A,zorder=5)
# dikmeler + uc pervaneleri
for sx in (-1,1):
    ax.plot([sx*b2,sx*b2],[-L,L],lw=2.0,color=MUT,zorder=3)
    for sy in (-1,1):
        ax.add_patch(Circle((sx*b2,sy*L),Dt/2,fill=False,ec=R,lw=2.2,zorder=4))
        ax.plot([sx*b2],[sy*L],"o",ms=4,color=R,zorder=5)
# olculer
def dim(x0,y0,x1,y1,txt,off=0.0,c=INK,ha="center",va="center",fs=10.5):
    ax.annotate("",xy=(x1,y1),xytext=(x0,y0),
                arrowprops=dict(arrowstyle="<->",color=c,lw=1.2,shrinkA=0,shrinkB=0))
    ax.text((x0+x1)/2,(y0+y1)/2+off,txt,ha=ha,va=va,fontsize=fs,color=c,
            bbox=dict(fc="white",ec="none",pad=1.6))
dim(-b2,-1.30,b2,-1.30,"span  $b$ = 3.453 m",0.0)
dim(b2+0.30,0,b2+0.30,L,"$L_p$ = 0.71 m",0.0,MUT)
dim(b2+0.72,-L,b2+0.72,L,f"{2*L:.2f} m",0.0,MUT)
ax.annotate("",xy=(Dm/2,0.80),xytext=(-Dm/2,0.80),
            arrowprops=dict(arrowstyle="<->",color=A,lw=1.2))
ax.text(0,0.87,"$D$ = 1.20 m",ha="center",fontsize=10.5,color=A,
        bbox=dict(fc="white",ec="none",pad=1.6))
ax.text(-b2-0.34,L,"$d$ = 0.20 m",ha="right",va="center",fontsize=10.5,color=R)
# etiketler
ax.text(0,-0.68,"thrust pair\n(all propulsion)",ha="center",va="top",fontsize=10.5,color=A,linespacing=1.4)
ax.text(-b2-0.34,-L,"control\npairs",ha="right",va="center",fontsize=10.5,color=R,linespacing=1.4)
# ---- moment blogu: diyagramin ALTINDA ----
ax.axhline(-1.62,xmin=0.03,xmax=0.97,color=GR,lw=0.9)
ax.text(0,-1.80,"All thrust vectors are parallel to the body $x$ axis:   "
        r"$\mathbf{F}=(F_x,\,0,\,0)$",ha="center",va="top",fontsize=11.5,color=INK)
ax.text(-1.30,-2.12,r"pitch",ha="left",va="top",fontsize=11,color=INK,fontweight="bold")
ax.text(-0.62,-2.12,r"$M_y = z\,F_x$      upper vs lower pairs",ha="left",va="top",fontsize=11,color=INK)
ax.text(-1.30,-2.40,r"yaw",ha="left",va="top",fontsize=11,color=INK,fontweight="bold")
ax.text(-0.62,-2.40,r"$M_z = -y\,F_x$     left vs right pairs",ha="left",va="top",fontsize=11,color=INK)
ax.text(-1.30,-2.68,r"roll",ha="left",va="top",fontsize=11,color=R,fontweight="bold")
ax.text(-0.62,-2.68,r"$M_x = y F_z - z F_y = 0$    identically, at every thrust setting",
        ha="left",va="top",fontsize=11,color=R)
ax.set_xlim(-2.95,3.05); ax.set_ylim(-3.00,1.15); ax.set_aspect("equal"); ax.axis("off")
ax.set_title("Propeller placement and moment arms — front view",
             loc="left",fontsize=12.5,fontweight="bold",pad=6)
fig.tight_layout()
fig.savefig(OUT+"/sekil07-moment-kollari.png",dpi=300,bbox_inches="tight")
fig.savefig(OUT+"/sekil07-moment-kollari.svg",bbox_inches="tight")
print("Sekil 7 yazildi")
