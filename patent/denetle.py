# -*- coding: utf-8 -*-
"""Uretilen PDF'leri kilavuza ve bildirime karsi OLCEREK denetler."""
import subprocess, re, sys, os
D = "/home/user/meryemAircraft/patent/pdf"
hata = []

def bbox(p):
    g = "/tmp/_b.xhtml"
    subprocess.run(["pdftotext", "-bbox-layout", p, g], check=True)
    s = open(g, encoding="utf-8").read(); os.unlink(g)
    return re.findall(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', s, re.S)

# --- 1) Sayfa numaralari: surekli 1..12, DUZ bicim (n/toplam DEGIL) ---
gorulen = []
for ad in ("01-tarifname.pdf", "02-istemler.pdf", "03-ozet.pdf"):
    for w, h, ic in bbox(D + "/" + ad):
        h = float(h)
        alt = [m for m in re.finditer(
            r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="[\d.]+" yMax="([\d.]+)">([^<]*)</word>', ic)
            if float(m.group(2)) > h - 56.7]
        gorulen.append([m.group(4) for m in alt])
bek = [[str(i)] for i in range(1, 13)]
if gorulen != bek:
    hata.append("sayfa numaralari: %r != %r" % (gorulen, bek))

# --- 2) Resim sayfalari: n/5, metin sayfalarindan FARKLI bicim ---
res = []
for w, h, ic in bbox(D + "/04-resimler.pdf"):
    ust = [m.group(3) for m in re.finditer(
        r'<word xMin="[\d.]+" yMin="([\d.]+)" xMax="[\d.]+" yMax="[\d.]+">([^<]*)</word>'.replace("([^<]*)", "([^<]*)"), ic)] if False else None
    ust = [m.group(2) for m in re.finditer(
        r'<word xMin="[\d.]+" yMin="([\d.]+)" xMax="[\d.]+" yMax="[\d.]+">([^<]*)</word>', ic)
        if float(m.group(1)) < 56.7]
    res.append(ust)
bekr = [["%d/5" % i] for i in range(1, 6)]
if res != bekr:
    hata.append("resim sayfa numaralari: %r != %r" % (res, bekr))

# --- 3) Satir numaralari: her sayfada 5,10,15... olugda (xMin < 85pt) ---
top_satir = top_num = 0
for ad in ("01-tarifname.pdf", "02-istemler.pdf", "03-ozet.pdf"):
    for w, h, ic in bbox(D + "/" + ad):
        h = float(h); alt_sinir = h - 56.7
        satirlar = []
        for m in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>', ic, re.S):
            y0, y1 = float(m.group(2)), float(m.group(4))
            if y0 >= alt_sinir: continue
            kel = re.findall(r'<word xMin="([\d.]+)"[^>]*>([^<]*)</word>', m.group(5))
            satirlar.append((y0, y1, kel))
        satirlar.sort()
        birlesik = []
        for (y0, y1, kel) in satirlar:
            if birlesik and y0 < birlesik[-1][1] - 2.0:
                birlesik[-1] = (birlesik[-1][0], max(birlesik[-1][1], y1), birlesik[-1][2] + kel)
            else:
                birlesik.append((y0, y1, list(kel)))
        for i, (y0, y1, kel) in enumerate(birlesik, 1):
            top_satir += 1
            # olukta (sol kenar boslugunda) duran kelime = satir numarasi
            oluk = [t for (x, t) in kel if float(x) < 85.0 and t.strip().isdigit()]
            if i % 5 == 0:
                top_num += 1
                if oluk != [str(i)]:
                    hata.append("%s s.? satir %d: oluk %r bekleniyordu ['%d']" % (ad, i, oluk, i))
            elif oluk:
                hata.append("%s satir %d: numarasiz olmali ama %r var" % (ad, i, oluk))

# --- 4) Baslik OZET'te ve TARIFNAME'de AYNI ---
t = subprocess.run(["pdftotext", "-f", "1", "-l", "1", D + "/01-tarifname.pdf", "-"],
                   capture_output=True, text=True).stdout
o = subprocess.run(["pdftotext", D + "/03-ozet.pdf", "-"], capture_output=True, text=True).stdout
def bas(x, unsur):
    sat = [s.strip() for s in x.split("\n") if s.strip()]
    assert sat[0] == unsur, (sat[0], unsur)
    cik = []
    for s in sat[1:]:
        if s.isupper() or s.startswith(("KUYRU", "YÜZEY", "AİT")): cik.append(s)
        else: break
    return " ".join(cik)
bt, bo = bas(t, "TARİFNAME"), bas(o, "ÖZET")
if bt != bo:
    hata.append("baslik farkli:\n  T: %r\n  O: %r" % (bt, bo))

# --- 5) Ozette gomulu resim ve "Yayimlanacak" olmamali ---
im = subprocess.run(["pdfimages", "-list", D + "/03-ozet.pdf"], capture_output=True, text=True).stdout
if len([l for l in im.strip().split("\n") if l and l[0].isdigit() or l.strip()[:1].isdigit()]) > 0:
    n = len([l for l in im.split("\n")[2:] if l.strip()])
    if n: hata.append("ozette %d gomulu resim var" % n)
if "Yayımlanacak" in o or "Yayimlanacak" in o:
    hata.append("ozette 'Yayimlanacak' gecıyor")

# --- 6) Kenar marjlari (kilavuz s.18): ust 2-4, sol 2.5-4, sag 2-3, alt 2 cm ---
MM = 72 / 25.4
for w, h, ic in bbox(D + "/01-tarifname.pdf")[:1]:
    w, h = float(w), float(h)
    xs = [float(m.group(1)) for m in re.finditer(r'<word xMin="([\d.]+)"', ic)]
    xe = [float(m.group(1)) for m in re.finditer(r'<word xMin="[\d.]+" yMin="[\d.]+" xMax="([\d.]+)"', ic)]
    sol, sag = min(xs) / MM, (w - max(xe)) / MM
    if not (25 <= sol <= 40): hata.append("sol marj %.1f mm (25-40 olmali)" % sol)
    if not (20 <= sag <= 30): hata.append("sag marj %.1f mm (20-30 olmali)" % sag)
    print("  marj: sol %.1f mm, sag %.1f mm" % (sol, sag))

print("  satir: %d toplam, %d numarali" % (top_satir, top_num))
print("  sayfa: %s" % [g[0] for g in gorulen])
print("  resim: %s" % [r[0] for r in res])
print("  baslik ayni: %s" % (bt == bo))
print()
if hata:
    print("HATA (%d):" % len(hata)); [print("  - " + x) for x in hata]; sys.exit(1)
print("TUM DENETIMLER GECTI")
