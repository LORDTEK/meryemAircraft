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
    "Each known partial remedy reduces one and raises another.":
        "Each known partial remedy reduces one charge and pays for it, in another charge or in a cost outside the three.",
    "The accounting is refuted by any remedy that reduces one charge while leaving the others no worse and adding no cost of its own.":
        "The accounting is refuted by a counter-example, and the table above is where one would appear: every entry in it moves cost rather than removing it.",
    "That is the test it has to survive, and the table above is where it would fail: every entry in it is a documented transfer, and a counter-example would be a move whose right-hand column is genuinely empty.":
        "The accounting is refuted by a counter-example, and the table above is where one would appear: every entry in it moves cost rather than removing it.",
    "A move that reduces one charge and makes another worse is a transfer.":
        "A move that reduces one charge and makes another worse is a transfer between charges.",
    "A framework that says every remedy transfers a charge rather than removing it takes something from its user in return.":
        "A framework that says every remedy moves cost rather than removing it takes something from its user in return.",
    "They are three distinct accounting quantities — kilograms, drag counts, installed kilowatts — and they are not assumed to be independent physical causes: a remedy can move a requirement from one currency into another.":
        "They are three distinct accounting quantities, paid in kilograms, drag counts and installed kilowatts, and they are not assumed to be independent physical causes: a remedy can move a requirement from one currency into another.",
    "The architecture converts a power-system charge into a mass one.":
        "The architecture converts a power-system charge into a cost in kilograms.",
    "If Section 10's take-off masses are retained instead, the payload falls to about 7 kg rather than 13.":
        "If Section 10's take-off masses are retained instead of re-closing at the bench rate, the payload falls to about 7 kg rather than 13.",
    "What has been measured is a fraction of that, and the figures available are of three different kinds.":
        "What has been measured is a fraction of that, and the figures available are of four different kinds.",
    "The comparison is between unlike ratings: a peak demand held through the vertical phases, a bench average over minutes, a continuous rating, and a design assumption.":
        "The comparison is between unlike ratings: a peak demand held through the vertical phases, a bench average over minutes, a continuous rating, a design assumption, and a literature figure the study cites without its rating.",
}
ONCE = {2: "d2ca894", 9: "eb22a83", 14: "9f4cfcb", 3: "46b9628", 4: "8c4d712", 10: "024005c", 11: "65ae7de", 12: "c9fcdd7", 13: "c9fcdd7", 1: "e4b6847", 5: "fc646cb", 6: "38d5324", 7: "555b73b", 8: "0b4b24f"}   # kisaltmadan onceki commit


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
