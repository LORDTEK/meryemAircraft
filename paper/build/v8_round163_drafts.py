import re,sys,os
root=sys.argv[1]; variant=sys.argv[2]   # A1 | A2
def rd(n):
    import glob
    f=glob.glob(os.path.join(root,'paper/v8/%02d-*.md'%n))[0]; s=open(f).read()
    m=re.search(r"^## (?!Yazar)", s, re.M); e=re.search(r"^## Yazarın denetimi", s, re.M)
    return f,s,m.start(),e.start()
J=lambda p: p if p.lstrip().startswith(('|','#')) else ' '.join(p.split())
def sub(p,a,b):
    a2=' '.join(a.split()); assert a2 in p,(a2[:60]); return p.replace(a2,b)
# ---- A (step 8)
f,s,a,e=rd(8)
P=[J(x) for x in re.split(r'\n\s*\n',s[a:e]) if x.strip()]
assert P[-1]=='---'; P=P[:-1]
# common cuts
P[23]=sub(P[23]," This is a control question rather than a property of the hardware, and it is stated as one.","")
P[24]=sub(P[24]," — the aircraft's longitudinal axis, which is the roll axis in body terms (Section 8, *The propulsion*)","")
P[26]=sub(P[26],", and only one of them is physically closed","")
P[3]=sub(P[3],"; Section 10 re-closes it at four masses, and Section 12 sets it beside a 1 000 kg reference design","")
P[19]=sub(P[19]," The configuration replaces a pilot's workload with computation, and the computer is the part that does it.","")
P[21]=sub(P[21],", and naming a number here would be inventing one","")
res=[P[23],P[24],P[25]]; cruise=[P[26],P[28]]; fail=P[27]
if variant=='A1':
    res[2]=sub(res[2],"That axis is the one the configuration has chosen not to command with the propellers, which is why the residual is awkward: the tip pairs cannot absorb it by thrust differential, because their thrust vectors are parallel to that axis too, and","The residual is awkward: the tip pairs cannot absorb it by thrust differential, and")
    body=P[0:9]+cruise+P[9:16]+res+P[16:22]+[fail]
else:
    body=P[0:22]+[fail,P[22]]+res+cruise
new8=s[:a]+"\n\n".join(body)+"\n\n---\n\n"+s[e:]
open(f,'w').write(new8)
# ---- B (step 14)
f,s,a,e=rd(14)
Q=[J(x) for x in re.split(r'\n\s*\n',s[a:e]) if x.strip()]
assert Q[-1]=='---'; Q=Q[:-1]
assert Q[6].startswith('**Closing the loop on a measured store')
Q[6]="Closed again on the measured bench rate of about 1.5 kW per kilogram, the same package becomes 76 to 81 percent heavier, a sensitivity of that package with one input changed rather than a structural closure (Supplement S14)."
assert Q[12].startswith('The remaining items are not known obstacles')
Q[12]="Eighteen further questions are open, and Supplement S14 lists each with what it bears on and what would settle it."
new14=s[:a]+"\n\n".join(Q)+"\n\n---\n\n"+s[e:]
open(f,'w').write(new14)
print('ok',variant)
