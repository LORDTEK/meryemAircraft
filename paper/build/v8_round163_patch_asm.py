import sys
p=sys.argv[1]+'/paper/build/v8_assemble.py'; s=open(p).read()
a='''kes = next(i for i, p in enumerate(p8) if p.startswith("### What this inventory does not settle"))
basarisiz = next(i for i, p in enumerate(p8) if p.startswith("**The tip pairs are the parts that fail"))
envanter = p8[:kes] + [p8[basarisiz]]
kalan = [p for i, p in enumerate(p8[kes:], kes) if i != basarisiz]'''
b='''# Tur 163: "does not settle" basligi kaynakta yoksa (dagitilmis 5.2) Adim 8 bolunmez; 5.2 = butun govde.
kes = next((i for i, p in enumerate(p8) if p.startswith("### What this inventory does not settle")), None)
basarisiz = next(i for i, p in enumerate(p8) if p.startswith("**The tip pairs are the parts that fail"))
if kes is None:
    envanter, kalan, kes = p8, [], len(p8)
else:
    envanter = p8[:kes] + [p8[basarisiz]] if basarisiz > kes else p8[:kes]
    kalan = [p for i, p in enumerate(p8[kes:], kes) if i != basarisiz]'''
assert a in s; s=s.replace(a,b)
a='''k_ad = kalan[0][4:].strip()
parca.append("### 5.2 %s\\n\\n%s\\n\\n#### %s\\n\\n%s" % (ad8, alt("\\n\\n".join(envanter)), k_ad, alt("\\n\\n".join(kalan[1:]))))'''
b='''if kalan:
    k_ad = kalan[0][4:].strip()
    parca.append("### 5.2 %s\\n\\n%s\\n\\n#### %s\\n\\n%s" % (ad8, alt("\\n\\n".join(envanter)), k_ad, alt("\\n\\n".join(kalan[1:]))))
else:
    parca.append("### 5.2 %s\\n\\n%s" % (ad8, alt("\\n\\n".join(envanter))))'''
assert a in s; s=s.replace(a,b)
s=s.replace('''% (kes, len(kalan) - 1))''','''% (kes, max(len(kalan) - 1, 0)))''')
open(p,'w').write(s)
c=sys.argv[1]+'/paper/v8-caveats.md'; t=open(c).read()
t=t.replace("| 14 | These masses are the Section 10 package with one input changed. | D |\n","").replace("| 14 | They are not a structural closure at 100 kg | D |\n","")
t=t.replace("| S9 | By construction\"","| S14 | These masses are the Section 10 package with one input changed. | E12 |\n| S14 | They are not a structural closure at 100 kg | E12 |\n| S9 | By construction\"")
open(c,'w').write(t)
print('patched')
