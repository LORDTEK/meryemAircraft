import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
OUT="/home/user/meryemAircraft/gorsel/cikti"; g=9.81
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
 "axes.edgecolor":"#3A4046","axes.labelcolor":"#1C2024","text.color":"#1C2024",
 "xtick.color":"#3A4046","ytick.color":"#3A4046","axes.linewidth":0.9,
 "figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
def egim(frac,Estar,eta): return frac*Estar*eta/g/1000.0
Sa=egim(0.33,157*3600,0.75*0.60); Sb=egim(0.16,12.9*3.6e6,0.176)
print(f"pil {Sa:.2f} km/birim  ·  hibrit {Sb:.1f} km/birim")
print(f"  dogrulama pil    L/D 13.5 -> {Sa*13.5:.0f} km   (tez: Cora tabani 119 km)")
print(f"  dogrulama hibrit L/D 12.0 -> {Sb*12.0:.0f} km   (Bolum 6.2: 1598 km)")

OLC=[(9.0,"propellers\nperpendicular"),(13.0,"hover hardware installed,\npropellers aligned"),
     (17.0,"clean airframe,\nno hover hardware")]
x=np.linspace(7,19,200)
fig=plt.figure(figsize=(8.6,9.6))
gs=fig.add_gridspec(2,1,hspace=0.30,top=0.905,bottom=0.215,left=0.115,right=0.965)
axs=[fig.add_subplot(gs[0]),fig.add_subplot(gs[1])]
for ax,(Sl,ttl,sub,col) in zip(axs,[
 (Sa,"(a)  Battery-electric","battery 33 % of mass · 157 Wh/kg · 60 % of energy to cruise","#6E7C87"),
 (Sb,"(b)  Series hybrid, liquid fuel","fuel 16 % of mass · 12.9 kWh/kg · chain efficiency 0.176","#2F6F8F")]):
    ax.plot(x,Sl*x,lw=2.4,color=col,zorder=3)
    ax.set_title(ttl,loc="left",fontsize=12.5,fontweight="bold",pad=20)
    ax.text(0,1.035,sub,transform=ax.transAxes,fontsize=9.5,color="#6E7C87")
    ax.grid(True,lw=0.5,color="#E9ECEE"); ax.set_axisbelow(True)
    for s in ("top","right"): ax.spines[s].set_visible(False)
    ax.set_ylabel("Range  (km)"); ax.set_xlim(7,19.6); ax.set_ylim(0,Sl*19.6*1.30)
    for v,_ in OLC:
        ax.axvline(v,color="#C6CCD1",lw=0.9,ls=(0,(4,3)),zorder=1)
        ax.plot([v],[Sl*v],"o",ms=9,color=col,zorder=5)
    ax.annotate("",xy=(13,Sl*13),xytext=(17,Sl*17),
                arrowprops=dict(arrowstyle="->",color="#B03A2E",lw=1.9,shrinkA=8,shrinkB=8))
for v,lab in OLC:
    axs[0].annotate(lab,xy=(v,0),xytext=(v,Sa*19.6*1.27),ha="center",va="top",
                    fontsize=9.3,color="#3A4046",linespacing=1.35)
axs[0].text(15.0,Sa*17.9,"−24 % of L/D",fontsize=10,color="#B03A2E",ha="center",fontweight="bold")
axs[1].text(15.0,Sb*17.9,"= −24 % of range",fontsize=10,color="#B03A2E",ha="center",fontweight="bold")
# bizim tasarimlar SADECE hibrit panelde
for v,lab,dx,dy in ((12.0,"this study\n50 kg",-1.9,1.34),(13.6,"this study\n1000 kg",2.9,0.72)):
    axs[1].plot([v],[Sb*v],"o",ms=9.5,mfc="white",mec="#12303F",mew=2.2,zorder=6)
    axs[1].annotate(lab,xy=(v,Sb*v),xytext=(v+dx,Sb*19.6*dy*0.72),ha="center",
                    fontsize=9.3,color="#12303F",linespacing=1.35,
                    arrowprops=dict(arrowstyle="-",color="#12303F",lw=0.9,shrinkB=8))
axs[1].set_xlabel("Cruise lift-to-drag ratio  L/D",labelpad=8)
fig.text(0.115,0.128,
 "Filled markers — L/D measured in wind-tunnel tests of one airframe in three of the four configurations tested.\n"
 "Open markers — L/D calculated for the reference designs of this study; not measured.\n"
 "Each line gives range for one fixed energy system: the markers locate L/D values only, and are\n"
 "not claims about the range of the aircraft those measurements came from.",
 fontsize=9,color="#6E7C87",linespacing=1.75,va="top")
fig.savefig(OUT+"/sekil12-menzil-LD.png",dpi=300)
fig.savefig(OUT+"/sekil12-menzil-LD.svg")
print("Sekil 12 yazildi")
