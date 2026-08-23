import math
rho=1.225; g=9.81

def sim(m,S,AR,Tw,tr,Vcr,w0=0.0,dt=0.0002,e=0.85,CD0=0.0248,astall=math.radians(12)):
    """w0 = gecise girerken TIRMANIS hizi (m/s, yukari +)"""
    W=m*g; Tmax=Tw*W
    h=0.0; vx=0.0; vh=w0; t=0.0
    hmin=0.0; tk=None
    CLa=2*math.pi/(1+2/AR)
    while t<max(tr*4,20):
        th=math.radians(90)*min(t/tr,1.0)
        bx,bh=math.sin(th),math.cos(th)
        V=math.hypot(vx,vh)
        if V>1e-6:
            ux,uh=vx/V,vh/V
            al=-math.atan2(bx*uh-bh*ux, bx*ux+bh*uh)
        else:
            ux,uh,al=bx,bh,0.0
        a=abs(al)
        CL=CLa*al if a<=astall else math.copysign(2*math.sin(a)*math.cos(a),al)
        CD=CD0+CL*CL/(math.pi*AR*e)+2*math.sin(a)**3
        q=0.5*rho*V*V; L=q*S*CL; D=q*S*CD
        if tk is None and L>=W: tk=t
        T=Tmax if math.hypot(vx,vh)<Vcr or vx<Vcr*0.95 else min(Tmax,D)
        vx+=((T*bx-L*uh-D*ux)/m)*dt
        vh+=((T*bh+L*ux-D*uh)/m-g)*dt
        h+=vh*dt; t+=dt
        hmin=min(hmin,h)
        if tk is not None and vx>=Vcr and t>tr: break
    return hmin,tk

def tirmanis_hizi(m,S,Tw,CD0=0.0248):
    """duz dikey tirmanista denge hizi degil; sadece net ivme ile 1 sn'de ulasilan hiz"""
    return (Tw-1.0)*g

print("Bir sey once: dikey tirmanis ivmesi = (T/W - 1)*g")
for Tw in (1.1,1.2,1.3,1.5):
    print(f"   T/W={Tw}: a={(Tw-1)*g:.2f} m/s2  -> 10 m/s'ye {10/((Tw-1)*g):.1f} s, o sure icinde {0.5*(Tw-1)*g*(10/((Tw-1)*g))**2:.0f} m tirmanir")
print()
for ad,m,S,Vcr in (("HAFIF 50 kg",50,1.98,30.0),("AGIR 1000 kg",1000,22.24,40.0)):
    print(f"=== {ad} — irtifa kaybi (m), giris tirmanis hizina gore ===")
    hdr=[f"w0={w}" for w in (0,2,5,8,12)]
    for Tw in (1.1,1.2,1.3):
        print(f"  T/W={Tw}")
        print(f"    {'t_r':>5}",*[f"{x:>9}" for x in hdr])
        for tr in ((1,2,3,4,6) if m==50 else (2,3,4,5,8)):
            row=[]
            for w0 in (0,2,5,8,12):
                hmin,tk=sim(m,S,6,Tw,tr,Vcr,w0=w0)
                row.append(f"{hmin:9.1f}")
            print(f"    {tr:5.1f}",*row)
        print()
