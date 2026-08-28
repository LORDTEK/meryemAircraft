import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
OUT="/home/user/meryemAircraft/gorsel/cikti"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
 "figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
INK="#1C2024"; MUT="#6E7C87"; A="#2F6F8F"; R="#B03A2E"; GR="#D3D9DD"
# (yil, ad, not, taraf, dal yuksekligi, etiket x kaymasi)
OL=[(1934,"Burnelli lifting fuselage","flew; no production orders",+1,1.00,-0.6),
    (1942,"Vought V-173","≈190 flights",-1,0.62,-1.4),
    (1946,"Northrop XB-35","ended by gearboxes,\nnot by the wing",+1,0.62,+0.2),
    (1947,"Vought XF5U","completed, never flown;\njet era arrived",-1,1.02,+1.8),
    (1952,"Handley Page Victor","crescent wing, in service",+1,1.00,+2.6),
    (1954,"Lockheed XFV-1","intended engine\nnever delivered",-1,0.62,+2.6),
    (1954,"Convair XFY-1","full cycle achieved;\nended by engine and\ngearbox reliability",+1,0.34,+4.6),
    (2012,"hybrid VTOL UAS","lift+cruise and tilt,\nin service",-1,0.70,0.0)]
fig,(axL,axR)=plt.subplots(1,2,figsize=(14.0,6.4),sharey=True,
                           gridspec_kw={"width_ratios":[3.05,1.0],"wspace":0.045})
for ax,(x0,x1),ticks in ((axL,(1930,1962),(1940,1950,1960)),(axR,(2005,2024),(2010,2020))):
    ax.set_xlim(x0,x1); ax.set_ylim(-1.55,1.55); ax.axis("off")
    ax.plot([x0+0.4,x1-0.4],[0,0],color=INK,lw=2,zorder=2)
    for yr in ticks:
        ax.plot([yr],[0],"|",ms=13,color=INK,mew=1.7,zorder=3)
        ax.text(yr,-0.11,str(yr),ha="center",va="top",fontsize=10.5,color=MUT)
for yr,name,note,side,h,dx in OL:
    ax = axL if yr<1990 else axR
    col = R if "XFY" in name else A
    y1=h*side; lx=yr+dx
    ax.plot([yr],[0],"o",ms=9,color=col,zorder=5)
    ax.plot([yr,yr,lx],[0.14*side,y1,y1],color=GR,lw=1.3,zorder=1)
    va="bottom" if side>0 else "top"
    ax.text(lx,y1+0.055*side,name,ha="center",va=va,fontsize=10.9,
            fontweight="bold",color=col)
    ax.text(lx,y1+0.30*side if side>0 else y1-0.28,note,ha="center",va=va,
            fontsize=9.4,color=MUT,linespacing=1.4)
# kirik eksen isareti
for ax,xx in ((axL,1962),(axR,2005)):
    for dy in (-0.055,0.055):
        ax.plot([xx-0.55,xx+0.55],[dy-0.05,dy+0.05],color="white",lw=5,
                clip_on=False,zorder=6,solid_capstyle="butt")
        ax.plot([xx-0.55,xx+0.55],[dy-0.05,dy+0.05],color=INK,lw=1.4,
                clip_on=False,zorder=7,solid_capstyle="butt")
fig.suptitle("Seventy years of attempts to merge the two families",x=0.055,y=0.975,
             ha="left",fontsize=13.5,fontweight="bold")
fig.text(0.055,0.045,"Marked in red: the one programme that completed the full cycle — vertical take-off, "
         "transition, cruise, transition, vertical landing.\nTwo contemporary NASA reviews record that its "
         "testing was curtailed by engine and gear-box reliability, not by the configuration.",
         fontsize=9.7,color=MUT,linespacing=1.7)
fig.subplots_adjust(top=0.90,bottom=0.155,left=0.03,right=0.985)
fig.savefig(OUT+"/sekil02-zaman-cizelgesi.png",dpi=300)
fig.savefig(OUT+"/sekil02-zaman-cizelgesi.svg"); print("Sekil 2 yenilendi")
