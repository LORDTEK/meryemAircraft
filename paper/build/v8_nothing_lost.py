# -*- coding: utf-8 -*-
"""Kisaltilan adimlarda HIC BIR SEY KAYBOLMADI mi (Tur 70; Qwen'in onerisi).

Her kisaltilan adimin kisaltmadan onceki hali (commit) alinir; o halin her cumlesi ya
simdiki govdede ya da paper/v8/supplement.md'de AYNEN (bosluk ve * farki haric) bulunmali.
--sina: ekten bir cumle silip yakalandigini sinar.
"""
import glob, os, re, subprocess, sys
KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Tur 86: kisaltma DEGIL, oylanmis icerik duzeltmesi -- eski cumle bilerek emekli edildi (emekli listesinde);
# yeni hali govdede aranir. Eski cumle eke konmaz (emekli ifadeyi dergiye tasimamak icin).
DEGISTI = {
    "That is an idealisation in its favour, and it is deliberate: it makes the tilt row a bound.":
        "That is an idealisation in its favour, and it is deliberate: it makes the tilting layout a bound.",
    "Whatever that store turns out to cost, holding it common charges all three the same assumption.":
        "Whatever that store turns out to cost, holding it common puts the same assumption on all three.",
    "The point-mass model prescribes the attitude and therefore cannot charge for the trajectory the aircraft flies while it is being rotated into that attitude.":
        "The point-mass model prescribes the attitude and therefore cannot account for the trajectory the aircraft flies while it is being rotated into that attitude.",
    "The architecture converts a power-system charge into a mass one.":
        "The architecture converts a power-system charge into a cost in kilograms.",
}
ONCE = {2: "d2ca894", 3: "46b9628", 4: "8c4d712", 10: "024005c", 11: "65ae7de", 12: "c9fcdd7", 13: "c9fcdd7"}   # kisaltmadan onceki commit


def govde(s):
    m = re.search(r"^## (?!Yazar)", s, re.M); e = re.search(r"^## Yazarın denetimi", s, re.M)
    return s[m.start():e.start() if e else len(s)]


def duz(x):
    return re.sub(r"\s+", " ", x.replace("*", "")).strip()


def cumleler(x):
    x = re.sub(r"(?m)^#+ .*$", "", x)
    x = re.sub(r"(?m)^\s*- ", "", x)
    out = []
    for p in re.split(r"\n\s*\n", x):               # once paragraf, sonra cumle
        if p.lstrip().startswith("|"):               # tablo: satir satir
            out += [duz(L) for L in p.splitlines() if L.strip() and not re.match(r"^\|[-: |]+\|$", L.strip())]
            continue
        out += [c.strip() for c in re.split(r"(?<=[.!?])\s+(?=[A-Z(*])", duz(p)) if len(c.strip()) > 3]
    return out


ek = duz(re.sub(r"(?m)^\s*- ", "", open(os.path.join(KOK, "paper", "v8", "supplement.md"), encoding="utf-8").read()))
if "--sina" in sys.argv:
    ek = ek.replace("The heavy design is not the light design photographed from further away.", "")
kayip = 0
for n, c in ONCE.items():
    yol = os.path.relpath(glob.glob(os.path.join(KOK, "paper", "v8", "%02d-*.md" % n))[0], KOK)
    eski = subprocess.run(["git", "-C", KOK, "show", "%s:%s" % (c, yol)], capture_output=True, text=True, check=True).stdout
    simdi = duz(re.sub(r"(?m)^\s*- ", "", govde(open(os.path.join(KOK, yol), encoding="utf-8").read())))   # Tur 84: madde imi eski metinde siliniyordu, simdikinde de silinmeli
    for k in cumleler(govde(eski)):
        if k in DEGISTI:
            if duz(DEGISTI[k]) not in simdi:
                kayip += 1
                print("  KAYIP Adim %d (degisen cumlenin yeni hali yok): %s" % (n, DEGISTI[k][:100]))
            continue
        if k not in simdi and k not in ek:
            kayip += 1
            print("  KAYIP Adim %d: %s" % (n, k[:110]))
print("  %s  kisaltilan adimlar (%s): %s" % ("ok" if not kayip else "!!", ", ".join(map(str, ONCE)),
      "hicbir cumle kaybolmadi" if not kayip else "%d cumle ne govdede ne ekte" % kayip))
sys.exit(1 if kayip else 0)
