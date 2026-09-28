# -*- coding: utf-8 -*-
"""paper/v8/ASSEMBLED.md: on bes adimi kabul edilen dokuz bolume dizen URETILMIS GORUNUM (Tur 68).

Kaynak adim dosyalaridir; bu betik hicbir kaynak cumleyi degistirmez. Yaptigi uc sey:
  1. Adimlari dokuz bolumun altina dizer (B1, B2, B3, Adim 14 kendi bolumu).
  2. Adim 8'i B1'e gore boler: envanter + "These are the parts that fail" birlestirme
     bolumunde; "What this inventory does not settle" kalani saglamlik bolumunde.
  3. "Section N" atiflarini yeni numaralara cevirir (Tur 69: Adim 7 -> 5.1, Adim 8 -> 5.2;
     "Sections 7 and 8" -> "Sections 5.1 and 5.2", fiil uyumu bozulmaz). Ayni numaraya
     dusen coklu atif ya da kendi alt bolumune atif EKLEM listesine yazilir.

Denetim: 150 korunan cumlenin hepsi gorunumde aranir; bulunmayan varsa cikis kodu 1.
"""
import glob
import os
import re
import sys

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V8 = os.path.join(KOK, "paper", "v8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v8_caveats import duz, liste  # noqa: E402

HARITA = {1: "1", 2: "2.1", 3: "2.2", 4: "2.3", 5: "3", 6: "4", 7: "5.1", 8: "5.2", 9: "8",   # Tur 160: Adim 9 Adim 15e birlesti (emekli)
          10: "6.1", 11: "6.2", 12: "6.3", 13: "6.4", 14: "7", 15: "8"}   # Tur 162: eski Bolum 6 5.2ye girdi; 7-9 -> 6-8
EVDEKI = {1: "1", 2: "2", 3: "2", 4: "2", 5: "3", 6: "4", 7: "5", 8: "5", 9: "8",
          10: "6", 11: "6", 12: "6", 13: "6", 14: "7", 15: "8"}


def govde(n):
    f = glob.glob(os.path.join(V8, "%02d-*.md" % n))[0]
    s = open(f, encoding="utf-8").read()
    m = re.search(r"^## (?!Yazar)", s, re.M)
    t = re.search(r"^## Yazarın denetimi", s, re.M)
    b = s[m.start():t.start() if t else len(s)].rstrip()
    return re.sub(r"\n---\s*$", "", b).rstrip()


def baslik_ayir(b):
    ilk, _, geri = b.partition("\n")
    return ilk[3:].strip(), geri.strip()


def alt(b):
    return re.sub(r"(?m)^### ", "#### ", b)


eklemler = []
ATIF = re.compile(r"\b(Sections?) (\d+)((?:(?:, | and | to |–)\d+)*)(?!\d|\.\d)")


def cevir(metin, adim, kaydet=True):
    def f(m):
        nums = [int(m.group(2))] + [int(x) for x in re.findall(r"\d+", m.group(3))]
        if any(n not in HARITA for n in nums):
            return m.group(0)
        yeni = [HARITA[n] for n in nums]
        seps = re.findall(r", | and | to |–", m.group(3))
        tek = []
        for y in yeni:
            if y not in tek:
                tek.append(y)
        if len(tek) < len(yeni):
            sonuc = "Section " + tek[0] if len(tek) == 1 else "Sections " + " and ".join(tek)
            if kaydet:
                eklemler.append((adim, m.group(0), sonuc))
            return sonuc
        out = m.group(1) + " " + yeni[0]
        for s, y in zip(seps, yeni[1:]):
            out += s + y
        if kaydet and any(HARITA[n] == HARITA[adim] for n in nums):
            eklemler.append((adim, m.group(0), out + "  (kendi bolumune atif)"))
        return out
    return ATIF.sub(f, metin)


# Bolunmus adima (Adim 8 -> 5.2 + 6.1) acik atiflar (Tur 147, W-1): kaynakta alt basligi adlandirilir,
# gorunumde dogru alt bolum numarasina cevrilir. Ciplak "Section 8" 5.2'ye gider.
BOLUNMUS = {"(Section 8, *What this inventory does not settle*)": "(Section 5.2)",   # Tur 162: alt bolum 5.2nin sonunda   # Tur 160: 6.2 kalkti, 6 tek parca
            "(Section 8, *The propulsion*)": "(Section 5.2)"}


def adim_metni(n, seviye):
    ad, b = baslik_ayir(govde(n))
    # Tur 160: BOLUNMUS ciktisi ("Section 6") adim numarasiyla karisir (Adim 6 -> 4); cevirden once yer tutucu, sonra geri.
    for i, (k, v) in enumerate(BOLUNMUS.items()):
        b = b.replace(k, "\u27e6B%d\u27e7" % i)
    b = cevir(b, n)
    for i, (k, v) in enumerate(BOLUNMUS.items()):
        b = b.replace("\u27e6B%d\u27e7" % i, v)
    return ad, b


parca = ["# v8 — assembled view (generated; the fifteen steps are the source)\n"]

# 1
ad, b = adim_metni(1, 2)
parca.append("## 1. %s\n\n%s" % (ad, b))

# 2: 2, 3, 4
parca.append("## 2. The charges, the condition, an independent check")
for i, n in enumerate((2, 3, 4), 1):
    ad, b = adim_metni(n, 3)
    parca.append("### 2.%d %s\n\n%s" % (i, ad, alt(b)))

# 3, 4
for s, n in ((3, 5), (4, 6)):
    ad, b = adim_metni(n, 2)
    parca.append("## %d. %s\n\n%s" % (s, ad, b))

# 5: 7 + Adim 8 envanteri + "These are the parts that fail"
parca.append("## 5. Combining the solutions")
ad, b = adim_metni(7, 3)
parca.append("### 5.1 %s\n\n%s" % (ad, alt(b)))
ad8, b8 = adim_metni(8, 3)
p8 = b8.split("\n\n")
# Tur 163: "does not settle" basligi kaynakta yoksa (dagitilmis 5.2) Adim 8 bolunmez; 5.2 = butun govde.
kes = next((i for i, p in enumerate(p8) if p.startswith("### What this inventory does not settle")), None)
basarisiz = next(i for i, p in enumerate(p8) if p.startswith("**The tip pairs are the parts that fail"))
if kes is None:
    envanter, kalan, kes = p8, [], len(p8)
else:
    envanter = p8[:kes] + [p8[basarisiz]] if basarisiz > kes else p8[:kes]
    kalan = [p for i, p in enumerate(p8[kes:], kes) if i != basarisiz]
# Tur 162 (yazar): eski Bolum 6 ("What this inventory does not settle") 5.2'nin SON alt bolumu; Bolum 6 kalkti.
if kalan:
    k_ad = kalan[0][4:].strip()
    parca.append("### 5.2 %s\n\n%s\n\n#### %s\n\n%s" % (ad8, alt("\n\n".join(envanter)), k_ad, alt("\n\n".join(kalan[1:]))))
else:
    parca.append("### 5.2 %s\n\n%s" % (ad8, alt("\n\n".join(envanter))))

# 6: 10-13 (Tur 160, D1: Adim 10'un ilk paragrafi sozlesme cumlesiyse 6.1'in basligindan ONCE, Bolum 6'nin basina)
parca.append("## 6. The calculations")
for i, n in enumerate((10, 11, 12, 13), 1):
    ad, b = adim_metni(n, 3)
    if n == 10 and b.startswith("Because the comparative result depends on the sizing contract"):
        ilk, _, b = b.partition("\n\n")
        parca.append(ilk)
    parca.append("### 6.%d %s\n\n%s" % (i, ad, alt(b)))

# 7, 8
for s, n in ((7, 14), (8, 15)):
    ad, b = adim_metni(n, 2)
    parca.append("## %d. %s\n\n%s" % (s, ad, b))

metin = "\n\n".join(parca) + "\n"
open(os.path.join(V8, "ASSEMBLED.md"), "w", encoding="utf-8").write(metin)

# denetim (--sina: bir korunan cumleyi bellekte silip yakalandigini sinar)
d = duz(metin)
if "--sina" in sys.argv:
    q0 = liste()[0][1].split("…")[0]
    d = d.replace(duz(q0).strip(" .,"), "")
eksik = []
for adim, q, _ in liste():
    q = cevir(q, adim, kaydet=False)   # korunan cumle de yeni numarayla aranir
    for p in [duz(x).strip(" .,") for x in q.split("…") if duz(x).strip(" .,")]:
        if p not in d:
            eksik.append((adim, q[:70]))
govdeler = sum(len(govde(n).split()) for n in range(1, 16) if n != 9)
print("ASSEMBLED.md: %d kelime (adim govdeleri %d; fark = yeni basliklar)" % (len(metin.split()), govdeler))
print("Adim 8 bolunmesi: envanter %d paragraf + 'tip pairs … fail' -> 5.2; kalan %d paragraf -> 5.2 sonu"
      % (kes, max(len(kalan) - 1, 0))); print("  (Tur 162: kalan -> 5.2 son alt bolum; Adim 9 emekli, Bolum 8 = Adim 15)")
print("EKLEM (%d) — kaynakta degistirilmedi, gosterilecek:" % len(eklemler))
for a, e, y in eklemler:
    print("   Adim %2d: %-28s -> %s" % (a, e, y))
# Q-P1 (Tur 148; W-1'e bagli, dort okuyucu + Claude): bolunmus adima (Adim 8) giden ciplak atiflar ve
# 5.2 / 6.1 icindeki numarasiz isaretciler INSAN OKUSUN diye listelenir; hangi alt bolumu kastettigini
# betik bilemez. --sina-bolunmus: W-1'in "(below)"unu 5.2'ye geri koyar ve listede gorundugunu sinar.
def bolunmus_liste(metin):
    out = []
    for n in [x for x in range(1, 16) if x != 9]:
        for m in re.finditer(r"[^.]*\bSections? (?:\d+(?:, | and ))*8(?!\d|\.\d|, \*)[^.]*\.", govde(n)):
            out.append(("Adim %d -> 5.2" % n, " ".join(m.group(0).split())[:110]))
    for bas, son in (("### 5.2 ", "## 6."),):
        b = metin[metin.index(bas):metin.index(son, metin.index(bas))]
        for m in re.finditer(r"[^.]*\b(above|below)\b[^.]*\.", b):
            out.append((bas.strip("# "), " ".join(m.group(0).split())[:110]))
    return out


if "--sina-bolunmus" in sys.argv:
    # Tur 162: 5.2'de artik mesru bir "(below)" var; sinama, 5.2 bolgesine YENI bir numarasiz isaretci koyup listenin bir artmasini ister.
    metin_s = metin.replace("fail the escape condition** (Section 5.1)", "fail the escape condition** (below)")
    yakaladi = metin_s != metin and len(bolunmus_liste(metin_s)) == len(bolunmus_liste(metin)) + 1
    print("  %s  --sina-bolunmus: W-1 '(below)' geri kondu, liste %s" % ("ok" if yakaladi else "!!", "gosterdi" if yakaladi else "GOSTERMEDI"))
    sys.exit(0 if yakaladi else 1)
bl = bolunmus_liste(metin)
print("BOLUNMUS ADIM ISARETCILERI (%d) — insan okusun:" % len(bl))
for yer, c in bl:
    print("   %-16s %s" % (yer, c))
kalan_atif = set(re.findall(r"Sections? (\d+(?:\.\d)?)", metin))
gecerli = {"1", "2", "3", "4", "5", "6", "7", "8", "2.1", "2.2", "2.3", "5.1", "5.2"} | {"6.%d" % i for i in range(1, 5)}
print("cozulmeyen atif:", sorted(kalan_atif - gecerli) or "yok")
if eksik:
    print("EKSIK KORUNAN CUMLE:", eksik)
    sys.exit(1)
print("  ok  %d korunan cumlenin hepsi gorunumde." % len(liste()))
