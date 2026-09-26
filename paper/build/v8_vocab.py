#!/usr/bin/env python3
"""v8 sozcuk dizini (Tur 100; Qwen P2, dort okuyucu + Claude).

Duzeltilen sozcuk ciftlerinin her gecisini adim ve cumlesiyle listeler. GECTI/KALDI DEMEZ: bir betik sozcugu bulur,
anlamini bulamaz (Claude'un siniri, dordu kabul etti). Cikti: paper/v8-vocab-concordance.md, insan okur.

Gruplar ve okunacak kural:
  ucret / para birimi  -- A': fatura (charge) para birimi (currency) degildir; tablo faturayi numarayla adlandirir
  transfer             -- dar anlam "transfer between charges", genis anlam korunan "The accounting claims transfer"
  rakip ailesi         -- sozcuk kilidi: aile duzeyi -> rotorcraft; belirli referans kalir; alinti dokunulmaz
  mekanizma / gecis    -- mekanizma iddiasi donanim hakkindadir; gecis (transition) iddiasi yapilmaz

--sina: bilinen bir gecisin (Adim 7'nin korunan cumlesi) listede ciktigini sinar.
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v8_stale import govde  # noqa: E402

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

GRUPLAR = [
    ("ucret / para birimi (charge / currency)", r"\b(charges?|charged|currenc(?:y|ies))\b"),
    ("transfer (dar / genis)", r"\btransfer\w*\b"),
    ("rakip ailesi (rotorcraft / multirotor / quadrotor / helicopter)",
     r"\b(rotorcraft|multirotors?|quadrotors?|helicopters?)\b"),
    ("mekanizma / gecis (mechanism / transition)", r"\b(mechanisms?|transitions?)\b"),
]


def cumleler(metin):
    metin = re.sub(r"(?m)^#+ .*$", "", metin)
    metin = re.sub(r"\s+", " ", metin.replace("*", ""))
    return [c.strip() for c in re.split(r"(?<=[.!?])\s+(?=[A-Z|])", metin) if c.strip()]


def dizin():
    out = {g: [] for g, _ in GRUPLAR}
    for f in sorted(glob.glob(os.path.join(KOK, "paper", "v8", "[0-9][0-9]-*.md"))):
        adim = os.path.basename(f)[:2]
        for c in cumleler(govde(open(f, encoding="utf-8").read())):
            for g, desen in GRUPLAR:
                bul = sorted(set(m.group(0).lower() for m in re.finditer(desen, c, re.I)))
                if bul:
                    out[g].append((adim, ", ".join(bul), c))
    return out


if __name__ == "__main__":
    d = dizin()
    if "--sina" in sys.argv:
        hedef = "That single move is what removes the need for the mechanism."
        tut = [c for _, _, c in d[GRUPLAR[3][0]] if hedef in c]
        print("SINAMA: bilinen gecis (Adim 7, mekanizma) %s" % ("bulundu" if tut else "BULUNAMADI"))
        if not tut:
            sys.exit("!! Sozcuk dizini bilinen gecisi bulamadi -- denetim bozuk.")
    yol = os.path.join(KOK, "paper", "v8-vocab-concordance.md")
    with open(yol, "w", encoding="utf-8") as o:
        o.write("# v8 sozcuk dizini (uretilmis; elle duzenlenmez)\n\n")
        o.write("`paper/build/v8_vocab.py` uretir. **Gecti/kaldi yoktur**: her satir bir insanin (ve okuyucularin) anlam "
                "okumasi icindir. Kurallar betigin basinda.\n\n")
        for g, _ in GRUPLAR:
            o.write("## %s — %d gecis\n\n| Adim | Sozcuk | Cumle |\n|---|---|---|\n" % (g, len(d[g])))
            for adim, s, c in d[g]:
                o.write("| %s | %s | %s |\n" % (adim, s, c.replace("|", "\\|")))
            o.write("\n")
    for g, _ in GRUPLAR:
        print("  %4d  %s" % (len(d[g]), g))
    print("  yazildi: paper/v8-vocab-concordance.md")
