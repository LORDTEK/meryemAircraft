import sys, math, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
exec(open(S+"/transition2.py").read().split("def tirmanis_hizi")[0]) if False else None
from transition2 import sim
OUT="/home/user/meryemAircraft/figures/cikti"

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
 "axes.edgecolor":"#3A4046","axes.labelcolor":"#1C2024","text.color":"#1C2024",
 "xtick.color":"#3A4046","ytick.color":"#3A4046","axes.linewidth":0.9,
 "figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

# ITME/AGIRLIK ORANLARI UYDURMA DEGIL, TASIT NE VERIYORSA O.
# Onceki surum 1,1 / 1,2 / 1,3 / 1,5 ciziyordu. Bunlarin hicbirini kurulu
# guc vermiyor: 2.12 havada durma gucunu itme=agirlik'te boyutlandiriyor,
# yani ana pervane T/W = 1,00. Fazlasi yalniz uc ciftlerinden gelir ve
# donus sirasinda ust cift tam, alt cift sifir calisir. Kalan:
#   hafif  1,066 (tam donus otoritesi elde) ... 1,132 (hic otorite yok)
#   agir   1,041 (tam donus otoritesi elde) ... 1,082 (hic otorite yok)
# 3.15'teki tablo alt uctan gelir. Sekil de oradan gelmeli; 1,2 ile cizili
# bir sekil metnin "1,2'yi kurulu guc hicbir ayarda vermez" cumlesiyle
# ayni sayfada duramaz.
TW={50:(1.066,1.132),1000:(1.041,1.082)}
RENK=("#2F6F8F","#12303F")
ETIKET={1.066:"T/W = 1.066  (full rotation authority retained)",
        1.132:"T/W = 1.132  (no authority retained)",
        1.041:"T/W = 1.041  (full rotation authority retained)",
        1.082:"T/W = 1.082  (no authority retained)"}

fig,axs=plt.subplots(1,2,figsize=(9.2,3.9))
for ax,(ad,m,Sw,Vcr,trs) in zip(axs,[("(a)  50 kg",50,1.98,30.0,[0.5,0.75,1,1.5,2,2.5,3,3.5,4,5]),
                                     ("(b)  1000 kg",1000,22.24,40.0,[1,1.5,2,2.5,3,3.5,4,4.5,5,6])]):
    for Tw,col in zip(TW[m],RENK):
        ys=[-sim(m,Sw,6,Tw,tr,Vcr)[0] for tr in trs]
        ax.plot(trs,ys,marker="o",ms=4,lw=1.9,color=col,label=ETIKET[Tw])
    ax.set_xlabel("Rotation time $t_r$  (s)")
    ax.set_title(ad,loc="left",fontsize=12,fontweight="bold",pad=10)
    ax.grid(True,lw=0.5,color="#E3E7EA"); ax.set_axisbelow(True)
    for s in ("top","right"): ax.spines[s].set_visible(False)
    ax.set_ylim(bottom=-0.6)
    ax.legend(frameon=False,fontsize=8.5)
axs[0].set_ylabel("Altitude loss  (m)")
axs[1].annotate("slower rotation → less altitude lost",xy=(0.97,0.93),xycoords="axes fraction",
                ha="right",fontsize=10,color="#2F6F8F",style="italic")
fig.tight_layout()
fig.savefig(OUT+"/fig12a-transition-rotation-time.png",dpi=300)
fig.savefig(OUT+"/fig12a-transition-rotation-time.svg")
print("Sekil 12a yazildi")

# --- 12b: tirmanarak giris ---
fig,ax=plt.subplots(figsize=(6.2,4.4))
trs=[0.5,0.75,1,1.5,2,2.5,3,4]
for w0,col,st in ((0,"#B9C2C9","-"),(2,"#6E7C87","-"),(5,"#2F6F8F","-"),(8,"#12303F","-")):
    ys=[-sim(50,1.98,6,1.066,tr,30.0,w0=w0)[0] for tr in trs]
    ax.plot(trs,ys,marker="o",ms=4,lw=1.9,color=col,ls=st,label=f"$w_0$ = {w0} m/s")
ax.set_xlabel("Rotation time $t_r$  (s)"); ax.set_ylabel("Altitude loss  (m)")
ax.set_title("Entering the rotation while climbing  ·  50 kg, T/W = 1.066",
             loc="left",fontsize=11.5,fontweight="bold",pad=10)
ax.grid(True,lw=0.5,color="#E3E7EA"); ax.set_axisbelow(True); ax.set_ylim(bottom=-0.6)
for s in ("top","right"): ax.spines[s].set_visible(False)
ax.legend(frameon=False,fontsize=10)
fig.tight_layout(); fig.savefig(OUT+"/fig12b-climbing-entry.png",dpi=300)
fig.savefig(OUT+"/fig12b-climbing-entry.svg"); print("Sekil 12b yazildi")
