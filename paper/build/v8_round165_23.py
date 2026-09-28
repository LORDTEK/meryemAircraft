import re,sys,os,glob
root=sys.argv[1]
f=glob.glob(os.path.join(root,'paper/v8/04-*.md'))[0]; s=open(f).read()
m=re.search(r"^## (?!Yazar)", s, re.M); e=re.search(r"^## Yazarın denetimi", s, re.M)
body=s[m.start():e.start()]
def rep(a,b):
    global body
    rx=r'\s+'.join(re.escape(w) for w in a.split())
    mm=list(re.finditer(rx,body)); assert len(mm)==1,(a[:50],len(mm))
    body=body[:mm[0].start()]+b+body[mm[0].end():]
rep(" The objection arises at the title, not at the ledger, so it is answered here — before any configuration is described — by testing a prediction the accounting makes against numbers this work did not produce.","")
rep("It checks one falsifiable consequence on one independent data set.","It checks one falsifiable consequence on one independent data set. The working is in Supplement S4.")
rep(", with the first half supplying the reason to expect the outcome: the weight charge is amplified by a multiplier, while the efficiency credit enters linearly through the cruise lift-to-drag ratio.",".")
rep(" **If some data set showed the credit covering the charge, Bill 1 would not be refuted** — the mass would still have been paid. What would be refuted is the expectation that the amplified charge outweighs the linear credit.","")
rep("A long enough mission is where the credit is most likely to cover the charge, and the mission used below is short.","The mission used below is short.")
rep("The dedicated lift group buys no cruise-efficiency advantage at all here — it is marginally behind — and the design gross weights differ by 687 lb in the tilt-wing's favour.","The design gross weights differ by 687 lb in the tilt-wing's favour.")
rep(", and the published weight breakdown is what makes it informative rather than merely large.",".")
rep(" **The published weight breakdown is consistent with the transfer property of Section 2 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce**: its three reported categories account for 580 lb of the 679 lb empty-weight difference, and the remaining 99 lb lies in categories it does not break out (Supplement S4).","")
rep(" That is the efficiency credit conceded and found insufficient, by the authors of the data rather than by the authors of the prediction.","")
rep("**The tilt-wing is consistent with the transfer property of Section 2, in someone else's data.** It does not escape","The tilt-wing does not escape")
rep(" A reader who wants to know whether the accounting flatters that configuration will have to wait for Section 11, where it is applied to it and where the answer is not uniformly favourable.","")
open(f,'w').write(s[:m.start()]+body+s[e.start():])
print('ok')
