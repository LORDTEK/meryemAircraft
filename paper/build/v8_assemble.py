# -*- coding: utf-8 -*-
"""paper/v8/ASSEMBLED.md: on bes adimi kabul edilen dokuz bolume dizen URETILMIS GORUNUM (Tur 68).

Kaynak adim dosyalaridir; bu betik hicbir kaynak cumleyi degistirmez. Yaptigi uc sey:
  1. Adimlari dokuz bolumun altina dizer (B1, B2, B3, Adim 14 kendi bolumu).
  2. Adim 8'i B1'e gore boler: envanter + "These are the parts that fail" birlestirme
     bolumunde; "What this inventory does not settle" kalani saglamlik bolumunde.
  3. "Section N" atiflarini yeni numaralara cevirir. Ayni bolume dusen coklu atiflar
     ("Sections 7 and 8" -> "Section 5") birlestirilir ve EKLEM listesine yazilir: fiil
     uyumu gibi duzeltmeler kaynakta yapilmaz, gosterilip oylanir.

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

HARITA = {1: "1", 2: "2.1", 3: "2.2", 4: "2.3", 5: "3", 6: "4", 7: "5", 8: "5", 9: "6",
          10: "7.1", 11: "7.2", 12: "7.3", 13: "7.4", 14: "8", 15: "9"}
EVDEKI = {1: "1", 2: "2", 3: "2", 4: "2", 5: "3", 6: "4", 7: "5", 8: "5", 9: "6",
          10: "7", 11: "7", 12: "7", 13: "7", 14: "8", 15: "9"}


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
        if kaydet and any(EVDEKI[n] == EVDEKI[adim] for n in nums) and EVDEKI[adim] not in ("7", "2"):
            eklemler.append((adim, m.group(0), out + "  (kendi bolumune atif)"))
        return out
    return ATIF.sub(f, metin)


def adim_metni(n, seviye):
    ad, b = baslik_ayir(govde(n))
    return ad, cevir(b, n)


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
kes = next(i for i, p in enumerate(p8) if p.startswith("### What this inventory does not settle"))
basarisiz = next(i for i, p in enumerate(p8) if p.startswith("**These are the parts that fail"))
envanter = p8[:kes] + [p8[basarisiz]]
kalan = [p for i, p in enumerate(p8[kes:], kes) if i != basarisiz]
parca.append("### 5.2 %s\n\n%s" % (ad8, alt("\n\n".join(envanter))))

# 6: Adim 8 kalani + Adim 9
parca.append("## 6. The soundness of the resulting product")
k_ad = kalan[0][4:].strip()
parca.append("### 6.1 %s\n\n%s" % (k_ad, alt("\n\n".join(kalan[1:]))))
ad, b = adim_metni(9, 3)
parca.append("### 6.2 %s\n\n%s" % (ad, alt(b)))

# 7: 10-13
parca.append("## 7. The calculations")
for i, n in enumerate((10, 11, 12, 13), 1):
    ad, b = adim_metni(n, 3)
    parca.append("### 7.%d %s\n\n%s" % (i, ad, alt(b)))

# 8, 9
for s, n in ((8, 14), (9, 15)):
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
govdeler = sum(len(govde(n).split()) for n in range(1, 16))
print("ASSEMBLED.md: %d kelime (adim govdeleri %d; fark = yeni basliklar)" % (len(metin.split()), govdeler))
print("Adim 8 bolunmesi: envanter %d paragraf + 'parts that fail' -> 5.2; kalan %d paragraf -> 6.1"
      % (kes, len(kalan) - 1))
print("EKLEM (%d) — kaynakta degistirilmedi, gosterilecek:" % len(eklemler))
for a, e, y in eklemler:
    print("   Adim %2d: %-28s -> %s" % (a, e, y))
kalan_atif = set(re.findall(r"Sections? (\d+(?:\.\d)?)", metin))
gecerli = {"1", "2", "3", "4", "5", "6", "7", "8", "9"} | {"2.1", "2.2", "2.3"} | {"7.%d" % i for i in range(1, 5)}
print("cozulmeyen atif:", sorted(kalan_atif - gecerli) or "yok")
if eksik:
    print("EKSIK KORUNAN CUMLE:", eksik)
    sys.exit(1)
print("  ok  150 korunan cumlenin hepsi gorunumde.")
