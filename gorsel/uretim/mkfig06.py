import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, math
OUT="/home/user/meryemAircraft/gorsel/cikti"
D2R=math.pi/180
P=dict(rootChord=0.97,sweepRoot=45.0,sweepTip=35.0,sweepTE=25.0,crop=67.0,tcRoot=25.0,tcTip=12.0)

# conv: LE ve TE'nin bulusacagi aciklik
def conv_span(p):
    lo,hi=0.1,60*p['rootChord']
    for _ in range(200):
        mid=(lo+hi)/2
        # mid'i bRef alarak entegre et, kesisim var mi
        n=4000; step=mid/n; x=0.0; y=0.0; hit=None
        for i in range(n):
            s=(p['sweepRoot']+(p['sweepTip']-p['sweepRoot'])*min((y+step/2)/mid,1))*D2R
            x+=math.tan(s)*step; y+=step
            if p['rootChord']+y*math.tan(p['sweepTE']*D2R)-x<=0: hit=y; break
        if hit is None: lo=mid
        else: hi=mid
        if abs(hi-lo)<1e-7: break
    return (lo+hi)/2
conv=conv_span(P)
half=conv*P['crop']/100
print(f"conv = {conv:.4f} m   yari-aciklik = {half:.4f} m   aciklik = {2*half:.3f} m")

n=1200; ys=np.linspace(0,half,n)
LE=np.zeros(n); x=0.0
for i in range(1,n):
    step=ys[i]-ys[i-1]
    s=(P['sweepRoot']+(P['sweepTip']-P['sweepRoot'])*min((ys[i]-step/2)/conv,1))*D2R
    x+=math.tan(s)*step; LE[i]=x
TE=P['rootChord']+ys*math.tan(P['sweepTE']*D2R)
ch=TE-LE
f=ys/half
tc=(P['tcRoot']+(P['tcTip']-P['tcRoot'])*f)
lam=P['sweepRoot']+(P['sweepTip']-P['sweepRoot'])*np.minimum(ys/conv,1)
Sw=2*np.trapezoid(ch,ys); AR=(2*half)**2/Sw
print(f"kanat alani = {Sw:.4f} m2   AR = {AR:.3f}   (kunye: 1.98 m2, AR 6.00)")
print(f"kok veter {ch[0]:.3f} m   uc veter {ch[-1]:.3f} m   sivrilme {ch[-1]/ch[0]:.3f}")
print(f"hucum kenari ok acisi: kokte {lam[0]:.1f} deg -> ucta {lam[-1]:.2f} deg")

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
 "axes.edgecolor":"#3A4046","axes.labelcolor":"#1C2024","text.color":"#1C2024",
 "xtick.color":"#3A4046","ytick.color":"#3A4046","axes.linewidth":0.9,
 "figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,3,figsize=(12.4,4.0))
A,B,Cc="#2F6F8F","#B03A2E","#6E7C87"
axs[0].plot(f,lam,lw=2.4,color=A,label="leading edge")
axs[0].plot(f,np.full_like(f,P['sweepTE']),lw=2.4,color=B,ls="--",label="trailing edge")
axs[0].set_ylabel("Sweep angle  (deg)"); axs[0].set_ylim(0,50)
axs[0].legend(frameon=False,fontsize=10,loc="lower left")
axs[0].annotate(f"{lam[0]:.0f}°",xy=(0.02,lam[0]),xytext=(0.06,lam[0]+3),fontsize=10,color=A)
axs[0].annotate(f"{lam[-1]:.1f}°",xy=(1,lam[-1]),xytext=(0.72,lam[-1]-5.5),fontsize=10,color=A)
axs[0].annotate("25° constant",xy=(0.5,25),xytext=(0.30,18),fontsize=10,color=B)
axs[0].set_title("(a)  Sweep distribution",loc="left",fontsize=12,fontweight="bold",pad=10)
axs[1].plot(f,tc,lw=2.4,color=A)
axs[1].set_ylabel("Thickness / chord  (%)"); axs[1].set_ylim(0,30)
axs[1].set_title("(b)  Thickness distribution",loc="left",fontsize=12,fontweight="bold",pad=10)
axs[1].annotate("25 %",xy=(0.02,25),xytext=(0.06,26.4),fontsize=10,color=A)
axs[1].annotate("12 %",xy=(1,12),xytext=(0.76,13.6),fontsize=10,color=A)
axs[2].plot(f,ch,lw=2.4,color=A)
axs[2].set_ylabel("Chord  (m)"); axs[2].set_ylim(0,1.1)
axs[2].set_title("(c)  Chord distribution",loc="left",fontsize=12,fontweight="bold",pad=10)
axs[2].annotate(f"{ch[0]:.2f} m",xy=(0.02,ch[0]),xytext=(0.06,ch[0]-0.13),fontsize=10,color=A)
axs[2].annotate(f"{ch[-1]:.3f} m",xy=(1,ch[-1]),xytext=(0.62,ch[-1]+0.10),fontsize=10,color=A)
for ax in axs:
    ax.set_xlabel("Semi-span station  $y/(b/2)$")
    ax.grid(True,lw=0.5,color="#E9ECEE"); ax.set_axisbelow(True); ax.set_xlim(0,1)
    for s in ("top","right"): ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(OUT+"/sekil06-dagilimlar.png",dpi=300); fig.savefig(OUT+"/sekil06-dagilimlar.svg")
print("Sekil 6 yazildi")
