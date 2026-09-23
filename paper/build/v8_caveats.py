# -*- coding: utf-8 -*-
"""v8 KESILEMEYECEK CEKINCELER DENETIMI (Tur 61).

NEDEN VAR. Kisaltma basliyor. Bu projede en sik hata, kisa cumlenin guclu
cumle olmasi: iddiayi kendi gucunde tutan nitelendirme en kolay kesilen
sozcuktur. Okuyucular (Tur 60) bu nitelendirmeleri birebir alintiyla
listeledi: paper/v8-caveats.md. Bu betik her satirin, adiyla verilen adimin
Ingilizce govdesinde hala durdugunu sinar.

Bir satir bilerek cikarilir ya da baska adima tasinirsa, bu YAZARIN
kararidir ve v8-caveats.md'de kaydedilir -- betik susturulmaz.

--sina: bir cekinceyi bellekte silip denetimin YAKALADIGINI sinar.
"""
import glob
import os
import re
import sys

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(KOK, "paper", "build"))
from v8_stale import govde  # noqa: E402


def duz(s):
    s = s.replace("*", "").replace("’", "'").replace("\\|", "|")
    return re.sub(r"\s+", " ", s).strip().lower()


def liste():
    out = []
    for L in open(os.path.join(KOK, "paper", "v8-caveats.md"), encoding="utf-8"):
        m = re.match(r"^\| (\d+) \| (.+) \| ([GD+]+) \|$", L.rstrip("\n"))
        if m:
            out.append((int(m.group(1)), m.group(2), m.group(3)))
    return out


def adimlar():
    d = {}
    for f in glob.glob(os.path.join(KOK, "paper", "v8", "[0-9][0-9]-*.md")):
        d[int(os.path.basename(f)[:2])] = duz(govde(open(f, encoding="utf-8").read()))
    return d


def denetle(cek, adim):
    eksik = []
    for st, q, w in cek:
        parca = [duz(p).strip(" .,") for p in q.split("…") if duz(p).strip(" .,")]
        if not all(p in adim.get(st, "") for p in parca):
            eksik.append((st, q, w))
    return eksik


if __name__ == "__main__":
    cek, adim = liste(), adimlar()
    if not cek:
        sys.exit("!! v8-caveats.md okunamadi -- denetim bos donuyor, bu bir kusurdur.")
    if "--sina" in sys.argv:
        st, q, _ = cek[0]
        bozuk = dict(adim)
        bozuk[st] = bozuk[st].replace(duz(q.split("…")[0]).strip(" .,"), "")
        b = denetle(cek, bozuk)
        print("SINAMA: bir cekince silindi, denetim %d eksik buldu" % len(b))
        if not b:
            sys.exit("!! Denetim silinen cekinceyi YAKALAMADI -- denetim bozuk.")
    e = denetle(cek, adim)
    print("=== v8 KESILEMEYECEK CEKINCE DENETIMI ===")
    if e:
        for st, q, w in e:
            print("  !! Adim %d (%s): %s" % (st, w, q[:110]))
        sys.exit("%d cekince govdede yok." % len(e))
    print("  ok  %d cekincenin hepsi kendi adiminda duruyor." % len(cek))
