import re,sys,os,glob
root=sys.argv[1]
def rd(n):
    f=glob.glob(os.path.join(root,'paper/v8/%02d-*.md'%n))[0]; s=open(f).read()
    m=re.search(r"^## (?!Yazar)", s, re.M); e=re.search(r"^## Yazarın denetimi", s, re.M)
    return f,s,m.start(),e.start()
def rep(n,a,b):
    f,s,st,en=rd(n); body=s[st:en]
    nb=' '.join(body.split('\n'))  # not used
    rx=r'\s+'.join(re.escape(w) for w in a.split())
    m=list(re.finditer(rx,body)); assert len(m)==1,(n,a[:50],len(m))
    body=body[:m[0].start()]+b+body[m[0].end():]
    open(f,'w').write(s[:st]+body+s[en:])
# C1: 6.4 table out
f,s,st,en=rd(13); body=s[st:en]
m=re.search(r"Range of the lift-plus-cruise layout relative to this configuration:\s*\n\s*\n(\|.*\|\s*\n)+",body); assert m
open(os.path.join(root,'c1_table.txt'),'w').write(m.group(0))
body=body[:m.start()]+body[m.end():].lstrip('\n')
open(f,'w').write(s[:st]+body+s[en:])
# C2
rep(14," Section 15 calls this section a debt: questions the paper does not answer and that better evidence would.","")
# C3 (6.2 list)
rep(11,"Section 10's convergence does not cover the cost of declining the reaction-torque channel, the sizing of the strip's actuation, the allocation of the take-off margin against attitude authority, the landing transition, the vortex ring state, closed-loop attitude control in hover and in cruise, engine installation, or rotor–structure and rotor–wing interference; **none of these is a ledger entry, and Section 14 lists them.** **The first and the last are the two that would most change the numbers above if they were computed.**",
 "Section 10's convergence does not cover the items Supplement S14 lists, and **none of these is a ledger entry**; of them, **the cost of declining the reaction-torque channel and rotor–structure and rotor–wing interference are the two that would most change the numbers above if they were computed.**")
# pointer repairs
rep(5,"is an open question in Section 14 rather than an answered one here.","is an open question in Supplement S14 rather than an answered one here.")
rep(15,"Section 14 lists what the paper leaves open.","Section 14 and Supplement S14 list what the paper leaves open.")
print('ok')
