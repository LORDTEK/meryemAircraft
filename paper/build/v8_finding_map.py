# -*- coding: utf-8 -*-
"""Bulgu haritasi aday cikarimi (Tur 153, birlestirme asamasi A evresi; yazar onayi Tur 153).

Birlesik gorunumde (ASSEMBLED.md) her kume icin desene uyan cumleleri bolum basligiyla listeler ve korunan
cumleleri isaretler. Cikti ADAYDIR: hangi cumlenin bulguyu gercekten soyledigi, islevi ve islemi insan okur.
"""
import os
import re
import sys

KOK = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v8_caveats import duz, liste  # noqa: E402

KUMELER = [
    ("K-1", "four axes and their opponents", r"opponent|four axes|claimed against|Nothing here is claimed"),
    ("K-2", "the declined reaction-torque channel", r"reaction[- ]torque"),
    ("K-3", "transition assigned, sized, analysed, not demonstrated", r"transition|completes the rotation|through the rotation|regime change"),
    ("K-4", "partial instantiation: the tip pairs fail the condition", r"partial|parts that fail|fail(s)? the condition|re-open"),
    ("K-5", "a count, not mechanical simplicity or reliability", r"mechanical simplicity|reliability"),
    ("K-6", "methods diverge above about ten degrees", r"ten degrees"),
    ("K-7", "the buffer: kilograms for kilowatts, an input", r"buffer"),
    ("K-8", "rankings belong to the sizing contract", r"contract"),
    ("K-9", "the fixed-pitch compromise; no variable-pitch counterfactual", r"fixed-pitch|variable-pitch|variable pitch|feather"),
    ("C-10", "the wing carried through hover / ground wind", r"vertical phase, where it produces|ground wind|exposure to ground"),
    ("C-11", "tailless planform and sweep", r"tailless|sweep"),
    ("C-12", "the energy store", r"\bstore\b"),
    ("C-13", "the strip", r"\bstrip\b"),
]


def cumleler(metin):
    bolum = ""
    for par in re.split(r"\n\s*\n", metin):
        m = re.match(r"^(#{2,4}) (.*)", par.strip())
        if m:
            n = re.match(r"(\d+(?:\.\d+)?)\.? ", m.group(2))
            if n:
                bolum = n.group(1)
            continue
        for c in re.split(r"(?<=[.!?])\s+(?=[A-Z*(\"])", " ".join(par.split())):
            yield bolum, c


if __name__ == "__main__":
    metin = open(os.path.join(KOK, "paper", "v8", "ASSEMBLED.md"), encoding="utf-8").read()
    korunan = [duz(q).strip(" .,") for _, q, _ in liste()]
    for kod, ad, desen in KUMELER:
        rx = re.compile(desen, re.I)
        bulunan = [(b, c) for b, c in cumleler(metin) if rx.search(c)]
        print("=== %s %s (%d)" % (kod, ad, len(bulunan)))
        for b, c in bulunan:
            d = duz(c).strip(" .,")
            k = "P" if any(q and (q in d or d in q) for q in korunan) else " "
            print("  [%s] %-4s %s" % (k, b, c if "--tam" in sys.argv else c[:220]))
