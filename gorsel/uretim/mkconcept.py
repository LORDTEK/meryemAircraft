import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
OUT="/home/user/meryemAircraft/gorsel/cikti"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
 "figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
INK="#1C2024"; MUT="#6E7C87"; A="#2F6F8F"; R="#B03A2E"; GR="#D8DDE1"; BG="#F2F5F6"

# ================= SEKIL 1 : iki aile ve sinirlari =================
fig,ax=plt.subplots(figsize=(8.2,6.6))
ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis("off")
ax.annotate("",xy=(9.6,0.9),xytext=(0.9,0.9),arrowprops=dict(arrowstyle="->",color=INK,lw=1.5))
ax.annotate("",xy=(0.9,9.6),xytext=(0.9,0.9),arrowprops=dict(arrowstyle="->",color=INK,lw=1.5))
ax.text(5.3,0.32,"Runway independence  →",ha="center",fontsize=12,color=INK)
ax.text(0.34,5.3,"Cruise efficiency  →",va="center",rotation=90,fontsize=12,color=INK)
def box(x,y,w,h,t,s,col,fc):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.16,rounding_size=0.22",
                fc=fc,ec=col,lw=1.9))
    ax.text(x+w/2,y+h-0.42,t,ha="center",va="top",fontsize=12.5,fontweight="bold",color=col)
    ax.text(x+w/2,y+h-1.05,s,ha="center",va="top",fontsize=10.3,color=MUT,linespacing=1.5)
box(1.25,6.15,3.3,2.9,"Fixed wing","efficient cruise\n\nbound by the ground:\nrunway, catapult,\npavement",A,"#EDF3F6")
box(5.5,1.35,3.3,2.9,"Rotary wing","no infrastructure\n\nbound by energy:\npower spent every\nsecond of flight",R,"#FBEFED")
box(5.5,6.15,3.3,2.9,"the target","both at once\n\nseventy years of\nattempts to reach\nthis corner",INK,"#F2F5F6")
ax.add_patch(FancyArrowPatch((4.75,7.6),(5.3,7.6),arrowstyle="->",color=MUT,lw=2,mutation_scale=18))
ax.add_patch(FancyArrowPatch((7.15,4.45),(7.15,5.95),arrowstyle="->",color=MUT,lw=2,mutation_scale=18))
ax.set_title("Two configuration families and the limit of each",loc="left",
             fontsize=13,fontweight="bold",pad=12)
fig.tight_layout(); fig.savefig(OUT+"/sekil01-iki-aile.png",dpi=300,bbox_inches="tight")
fig.savefig(OUT+"/sekil01-iki-aile.svg",bbox_inches="tight"); print("Sekil 1")

# ================= SEKIL 2 : zaman cizelgesi =================
OL=[(1934,"Burnelli\nlifting fuselage","flew; no production\norders",1),
    (1942,"Vought V-173","≈190 flights",-1),
    (1946,"Northrop XB-35","gearboxes, not the wing",1),
    (1947,"Vought XF5U","completed, never flown\njet era",-1),
    (1952,"Handley Page Victor","crescent wing\nin service",1),
    (1954,"Lockheed XFV-1","engine never delivered",-1),
    (1954.9,"Convair XFY-1","full transition achieved\nended by pilot workload",1),
    (2010,"hybrid VTOL UAS","lift+cruise and tilt\nin service",-1)]
fig,ax=plt.subplots(figsize=(13.2,5.4))
ax.set_xlim(1928,2028); ax.set_ylim(-1.25,1.25); ax.axis("off")
ax.plot([1930,2026],[0,0],color=INK,lw=2)
for yr in (1940,1960,1980,2000,2020):
    ax.plot([yr],[0],"|",ms=12,color=INK,mew=1.6)
    ax.text(yr,-0.10,str(yr),ha="center",va="top",fontsize=10.5,color=MUT)
for x,t,s,side in OL:
    col=R if "XFY" in t else A
    ax.plot([x],[0],"o",ms=9,color=col,zorder=4)
    y0=0.16*side; y1=(0.52 if side>0 else -0.46)
    ax.plot([x,x],[y0,y1],color=GR,lw=1.4,zorder=1)
    va="bottom" if side>0 else "top"
    ax.text(x,y1+(0.05*side),t,ha="center",va=va,fontsize=10.8,fontweight="bold",
            color=col,linespacing=1.35)
    ax.text(x,y1+(0.33*side) if side>0 else y1-0.30,s,ha="center",va=va,
            fontsize=9.4,color=MUT,linespacing=1.4)
ax.set_title("Seventy years of attempts to merge the two families",loc="left",
             fontsize=13,fontweight="bold",pad=6)
ax.text(1930,-1.16,"Marked in red: the one programme that completed the full cycle and was ended "
        "by a constraint located in the cockpit.",fontsize=9.6,color=MUT)
fig.tight_layout(); fig.savefig(OUT+"/sekil02-zaman-cizelgesi.png",dpi=300,bbox_inches="tight")
fig.savefig(OUT+"/sekil02-zaman-cizelgesi.svg",bbox_inches="tight"); print("Sekil 2")

# ================= SEKIL 3 : uc fatura =================
fig,ax=plt.subplots(figsize=(9.0,8.4))
ax.set_xlim(0,10); ax.set_ylim(-0.2,10); ax.set_aspect("equal"); ax.axis("off")
P={"mass":(5.0,8.05),"drag":(1.75,2.65),"size":(8.25,2.65)}
TX={"mass":("Bill 1  ·  MASS","hover hardware carried\nfor the whole flight"),
    "drag":("Bill 2  ·  DRAG","hover hardware exposed\nin the cruise airstream"),
    "size":("Bill 3  ·  SIZING","power system sized by\na 2 % condition")}
for k,(cx,cy) in P.items():
    ax.add_patch(Circle((cx,cy),1.42,fc=BG,ec=A,lw=2.1,zorder=3))
    ax.text(cx,cy+0.44,TX[k][0],ha="center",fontsize=11.6,fontweight="bold",color=A,zorder=4)
    ax.text(cx,cy-0.06,TX[k][1],ha="center",va="top",fontsize=9.5,color=MUT,
            linespacing=1.45,zorder=4)
def curve(p0,p1,txt,rad,tx,ty):
    ax.add_patch(FancyArrowPatch(p0,p1,connectionstyle=f"arc3,rad={rad}",
        arrowstyle="->",color=R,lw=1.9,mutation_scale=18,shrinkA=104,shrinkB=104,zorder=2))
    ax.text(tx,ty,txt,ha="center",fontsize=9.7,color=R,linespacing=1.4,
            bbox=dict(fc="white",ec="none",pad=2.4),zorder=5)
curve(P["size"],P["mass"],"distributed\nelectric lift",0.22,8.35,5.9)
curve(P["mass"],P["drag"],"folding /\nretraction",0.22,1.75,5.9)
curve(P["drag"],P["size"],"smaller rotors,\nhigher disc loading",0.22,5.0,1.35)
ax.set_title("Three bills — and the moves that convert one into another",
             loc="left",fontsize=13,fontweight="bold",pad=10)
ax.text(0.1,-0.05,"Every known architectural remedy reduces one bill by increasing another.\n"
        "The measured instance: removing 30 % of drag at a cost of 5 % of mass moved the range by under 2 %.",
        fontsize=9.8,color=MUT,linespacing=1.6)
fig.tight_layout(); fig.savefig(OUT+"/sekil03-uc-fatura.png",dpi=300,bbox_inches="tight")
fig.savefig(OUT+"/sekil03-uc-fatura.svg",bbox_inches="tight"); print("Sekil 3")
