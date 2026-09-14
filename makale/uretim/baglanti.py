# -*- coding: utf-8 -*-
"""BAG DOKUSU DENETIMI -- isaretciler, sayimlar, atiflar.

NEDEN VAR. dogrula.py SAYILARI denetler ve iyi yapar: 40 kontrol, her biri
bir hesabi yeniden kosturup metindekiyle karsilastirir. Tur 22'de disaridan
gelen dort bulgunun HICBIRI o denetimden gecmezdi, cunku hicbiri bir sayi
hatasi degildi:

  - "Section 3.2" deniyordu, anlatilan sey 3.1'deydi (iki yerde),
  - Tablo 1 ustyazisi "dort yapilandirma" diyordu, tabloda uc satir vardi,
  - Tablo 4 ustyazisi "dort tasarim" diyordu, tabloda yedi satir vardi,
  - Girise konan bir kapsam cumlesi makalenin kendi iddiasini reddediyordu.

Ilk ucu MEKANIK. Ortak kokleri su: bir etiket, bir isaretci ya da bir sayim
artik gosterdigi seyi tarif etmiyor. Sayi avlayan bir gecis bunlarin
uzerinden kayar. Bu betik tam da onlari arar.

NE YAPMAZ. Dorduncusunu -- kapsam cumlesi -- hicbir betik yakalayamaz; onu
bir insan yakaladi ve bu kayda gecmistir.
"""
import os, re, sys

BURA = os.path.dirname(os.path.abspath(__file__))
MAKALE = os.path.abspath(os.path.join(BURA, ".."))
sys.path.insert(0, BURA)
from surum import SURUM                 # sabit "v6" yazıliydi; surum
KAYNAK = os.path.join(MAKALE, "makale-%s.md" % SURUM)   # kayinca BAYAT dosyayi denetliyordu

SAYI = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
        "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
        "twelve": 12}

s = open(KAYNAK, encoding="utf-8").read()
L = s.split("\n")
sap, goz = [], []

# ------------------------------------------------- 1. bolum isaretcileri
bolumler = set()
for l in L:
    m = re.match(r"^#{1,3}\s+(\d+)(\.\d+)?\.?\s", l)
    if m:
        bolumler.add(m.group(1) + (m.group(2) or ""))   # "4" ya da "4.2"
atif = {m.group(1) for m in re.finditer(r"Section (\d+(?:\.\d+)?)", s)}
yok = sorted(atif - bolumler, key=lambda x: [int(p) for p in x.split(".")])
print("%-46s %s" % ("bolum basligi", len(bolumler)))
print("%-46s %s" % ("atif alan bolum", len(atif)))
if yok:
    sap.append("var olmayan bolume atif: %s" % ", ".join(yok))

# ------------------- 1b. ISARETCI DOGRU YERE MI COZULUYOR? (anlam denetimi)
# Qwen'in tur 23 kapanisi: "bu projede kurulan her denetim bir atfin
# COZULDUGUNU sinar, hicbiri DOGRU seye cozuldugunu sinamaz." Haklidir ve
# ornegi vardir: "Section 3.2" var olan bir bolumdur, ama NASA dizisi
# 3.1'dedir; isaretci hem iyi bicimli hem yanlisti ve uc tur, dort okuyucu
# ve bir denetimden gecti.
#
# Tam otomasyon imkansiz. Ama isaretcinin gectigi CUMLEDE ayirt edici bir
# sayi varsa -- "Section N.M puts a quadrotor at 4.9" gibi -- o sayinin
# N.M bolumunun icinde gecip gecmedigi sinanabilir. Gecmiyorsa isaretci
# muhtemelen yanlis yeri gosteriyordur. Uyari, hata degil.
govde = {}
for i, l in enumerate(L):
    m = re.match(r"^#{1,3}\s+(\d+)(\.\d+)?\.?\s", l)
    if m:
        ad = m.group(1) + (m.group(2) or "")
        j = i + 1
        while j < len(L) and not re.match(r"^#{1,3}\s+\d", L[j]):
            j += 1
        govde[ad] = "\n".join(L[i:j])

# Cumleyi noktaya gore bolmek BURADA CALISMAZ: "3.2" ve "4.9" zaten nokta
# icerir, o yuzden cumle sinirlari sayinin ortasindan geciyordu ve denetim
# hicbir sey bulamiyordu. Ilk yazimi boyleydi ve sessizce bos donuyordu --
# calistigini sanmak, calismamasindan beterdi. Simdi sabit bir pencere.
for m in re.finditer(r"Section (\d+\.\d+)", s):
    hedef = m.group(1)
    cumle = s[m.end():m.end() + 150]     # isaretciden SONRAKI pencere
    if hedef not in govde:
        continue
    # ILK YAZIMI FAZLA GEVSEKTI: ilk tutmayan sayida bagirıyordu ve temiz
    # bir belgede dort yanlis alarm uretti. Cumlede gecen her sayinin hedef
    # bolumde bulunmasi gerekmez -- "3.1 ... 4.9 ... bizim 8.8'imize karsi"
    # cumlesinde 8.8 BIZIM sayimizdir, 3.1'de olmasi beklenmez. Dogru kural:
    # sayilardan EN AZ BIRI hedefte geciyorsa isaretci muhtemelen dogrudur;
    # HICBIRI gecmiyorsa suphelidir.
    sayilar = [x for x in re.findall(r"\b\d+\.\d+\b", cumle)
               if x != hedef and x not in govde]
    if sayilar and not any(x in govde[hedef] for x in sayilar):
        goz.append("Section %-5s atfi %s sayilarini animsatiyor; HICBIRI "
                   "%s'in govdesinde yok" % (hedef, "/".join(sayilar[:3]), hedef))

# --------------------------- 2. ustyazidaki sayim, tablonun satir sayisi
for i, l in enumerate(L):
    m = re.match(r"^\*\*Table (\d+)\.\*\*\s+(.*)$", l)
    if not m:
        continue
    no, cap = m.group(1), m.group(2)
    j = next((k for k in range(i, min(i + 6, len(L))) if L[k].startswith("|")), None)
    if j is None:
        sap.append("Table %s ustyazisinin ardinda tablo yok" % no)
        continue
    e = j
    while e < len(L) and L[e].startswith("|"):
        e += 1
    satir = e - j - 2                       # baslik ve ayirici disi
    # Ustyazinin ILK sayi sozcugu, tablonun neyi saydigini iddia eder.
    # Ustyazidaki sayi sozcugu satir sayisi OLABILIR de olmayabilir de:
    # "one uncrewed airframe", "eight tip discs", "three architectures"
    # hicbiri satir saymaz. Otomatik karar vermek yanlis alarm uretiyor,
    # o yuzden burada karar verilmez -- tutmayanlar INSANA listelenir.
    for k in re.finditer(r"\b(%s)\b" % "|".join(SAYI), cap, re.I):
        if SAYI[k.group(1).lower()] == satir:
            break
    else:
        varsa = re.findall(r"\b(%s)\b" % "|".join(SAYI), cap, re.I)
        if varsa:
            goz.append("Table %-3s ustyazi sayi sozcugu %-8s tabloda %d satir"
                       % (no, "/".join(varsa), satir))

# ------------------------------------------ 3. tablo/sekil atif butunlugu
sys.path.insert(0, BURA)
from kapaklar import FIGS                                     # noqa: E402

for tur, desen in (("Table", r"\*\*Table (\d+)\.\*\*"),
                   ("Figure", None)):
    if True:
        # Sekil altyazilari bu belgede degil; tanim kapaklar.py'dedir.
        tanimli = ({int(n) for n, _, _ in FIGS} if desen is None
                   else {int(x) for x in re.findall(desen, s)})
        atifli = {int(x) for x in re.findall(r"(?<!\*\*)%s (\d+)" % tur, s)}
        eksik = sorted(atifli - tanimli)
        atifsiz = sorted(tanimli - atifli)
        print("%-46s tanimli %d, atifsiz %s, tanimsiza atif %s"
              % (tur, len(tanimli), atifsiz or "yok", eksik or "yok"))
        if eksik:
            sap.append("var olmayan %s'ya atif: %s" % (tur, eksik))
        if atifsiz:
            sap.append("%s atif almiyor: %s" % (tur, atifsiz))

# -------------------------------------------------------------- 4. rapor
print()
if goz:
    print("GOZ AT -- otomatik karar VERILMEYEN, insana birakilan noktalar.")
    print("Cogu mesru; tutmayanlari bir insan acip bakmali.")
    for x in goz:
        print("   " + x)
    print()
if sap:
    print("=" * 62)
    for x in sap:
        print("  !! " + x)
    sys.exit("\n%d bag dokusu sapmasi -- duzelt ve tekrar calistir" % len(sap))
print("bag dokusu temiz: isaretciler cozuluyor, sayimlar tutuyor.")
