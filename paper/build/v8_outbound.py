#!/usr/bin/env python3
"""Bir adimin sayilarinin baska adimlarda nerede gectigini haritalar (Tur 101; Grok, dort okuyucu + Claude).

Kisaltma asamasi (yazar karari, Tur 101) Adim 10'a dokunmadan once her disa giden sayinin haritasini ister:
Adim 10'daki bir sayi baska bir adimda da geciyorsa, o sayi Adim 10'dan ekle birlikte giderse oteki adim
dayanaksiz kalir. Harita karar vermez, listeler.

Kullanim:  v8_outbound.py 10         -> paper/v8/drafts/10-outbound-map.md
           v8_outbound.py 10 --sina  -> bilinen bir gecisi (52.3, Adim 14) buldugunu sinar
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v8_stale import govde  # noqa: E402

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 1 233, 0.0285, 57.5, 5.1, 3.6 ... ; tek haneli tamsayilar ve yuzde isaretsiz kucuk sayilar gurultu
SAYI = re.compile(r"(?<![\w.])(\d{1,3}(?: \d{3})+|\d+\.\d+|\d{2,})(?![\w.]*\d)")
GURULTU = {"10", "11", "12", "13", "14", "15", "20", "30", "50", "90", "100"}


def adimlar():
    out = {}
    for f in sorted(glob.glob(os.path.join(KOK, "paper", "v8", "[0-9][0-9]-*.md"))):
        out[os.path.basename(f)[:2]] = govde(open(f, encoding="utf-8").read())
    return out


def sayilar(metin):
    duz = re.sub(r"\s+", " ", metin.replace("*", ""))
    return sorted(set(m.group(1) for m in SAYI.finditer(duz)) - GURULTU)


def harita(n):
    a = adimlar()
    kaynak = "%02d" % n
    out = []
    for s in sayilar(a[kaynak]):
        yer = []
        for k, m in a.items():
            if k == kaynak:
                continue
            duz = re.sub(r"\s+", " ", m.replace("*", ""))
            m2 = re.search(r"(?<![\w.])" + re.escape(s) + r"(?![\w]|\.\d)", duz)
            if m2:
                yer.append((k, duz[max(0, m2.start() - 45):m2.end() + 30]))
        if yer:
            d0 = re.sub(r"\s+", " ", a[kaynak].replace("*", ""))
            m0 = re.search(r"(?<![\w.])" + re.escape(s) + r"(?![\w]|\.\d)", d0)
            out.append((s, d0[max(0, m0.start() - 45):m0.end() + 30] if m0 else "", yer))
    return out


if __name__ == "__main__":
    n = int(sys.argv[1])
    h = harita(n)
    if "--sina" in sys.argv:
        tut = [s for s, _, yer in h if s == "52.3" and "14" in [k for k, _ in yer]]
        print("SINAMA: 52.3 -> Adim 14 %s" % ("bulundu" if tut else "BULUNAMADI"))
        if not tut:
            sys.exit("!! Harita bilinen gecisi bulamadi -- denetim bozuk.")
    yol = os.path.join(KOK, "paper", "v8", "drafts", "%02d-outbound-map.md" % n)
    with open(yol, "w", encoding="utf-8") as o:
        o.write("# Adim %d'den disa giden sayilar (uretilmis; `paper/build/v8_outbound.py %d`)\n\n" % (n, n))
        o.write("Adim %d'deki her sayi ve onu da tasiyan adimlar. Bir sayi eke giderse, listelenen adimlar "
                "ya o sayiyi kendi gerekcesiyle tasir ya da ekteki yerini gosterir. Karar vermez.\n\n" % n)
        o.write("| Sayi | Adim %d'deki baglami | Baska adimlardaki baglami (rastlanti olabilir; insan okur) |\n|---|---|---|\n" % n)
        for s, c0, yer in h:
            o.write("| %s | …%s… | %s |\n" % (s, c0.replace("|", "/"),
                    "<br>".join("**%s:** …%s…" % (k, c.replace("|", "/")) for k, c in yer)))
    print("  %d sayi Adim %d disinda da geciyor; yazildi: %s" % (len(h), n, os.path.relpath(yol, KOK)))
