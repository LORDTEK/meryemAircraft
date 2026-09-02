# -*- coding: utf-8 -*-
"""Uc boyutlu vakayi kurar -- iki boyutlusundan YALNIZCA agiyla ayrilarak.

Tasarim karari. Alan dosyalarini, ayrik sema secimlerini, cozucu ayarlarini
ve turbulans kurulumunu YENIDEN YAZMIYORUZ; naca/kur.py cagriliyor ve
ciktisinin yalnizca iki parcasi degistiriliyor:

  1. ag.msh -> uc boyutlu ag
  2. 0/* icindeki "(on|arka) empty" -> "(kok|uc) <tip>"

Sebep: iki boyutlu ile uc boyutlu arasindaki farkin AGDAN geldigini iddia
edebilmek icin, geri kalan her seyin bit bit ayni olmasi gerekir. Ayri bir
kurucu yazilsaydi, cikan fark "uc boyutluluk mu, yoksa fark gozden kacan bir
sema ayari mi?" sorusunu acik birakirdi.

Degistirmenin sessizce basarisiz olmamasi icin her dosyada ESLESME SAYISI
denetleniyor.
"""
import os
import re
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BURA, "..", "naca"))
sys.path.insert(0, BURA)
from kur import kur as kur2b                          # noqa: E402


def kur3b(dizin, ag, kok="symmetryPlane", uc="symmetryPlane", **kw):
    """ag: KanatAgi ornegi. kw, naca/kur.py'nin kur()'una gecer."""
    kw.setdefault("kod", "0012")
    bilgi2 = kur2b(dizin, **kw)

    # 1) agi degistir
    yeni = ag.yaz(os.path.join(dizin, "ag.msh"))

    # 2) yamalari degistir
    eski = ('    "(on|arka)"\n    {\n        type            empty;\n    }\n')
    yerine = ('    kok\n    {\n        type            %s;\n    }\n'
              '    uc\n    {\n        type            %s;\n    }\n' % (kok, uc))
    n = 0
    for ad in sorted(os.listdir(os.path.join(dizin, "0"))):
        p = os.path.join(dizin, "0", ad)
        s = open(p).read()
        adet = s.count(eski)
        if adet != 1:
            raise RuntimeError("0/%s icinde on|arka blogu %d kez gecti, "
                               "1 bekleniyordu" % (ad, adet))
        open(p, "w").write(s.replace(eski, yerine))
        n += 1
    if n == 0:
        raise RuntimeError("0/ bos -- kur2b calismamis olabilir")

    # 3) 2B'ye ozgu sema kalintisi kalmadigini dogrula
    for ad in ("fvSchemes", "fvSolution", "controlDict"):
        s = open(os.path.join(dizin, "system", ad)).read()
        if "empty" in s:
            raise RuntimeError("system/%s icinde 'empty' gecıyor" % ad)

    bilgi = dict(bilgi2 or {})
    bilgi.update(yeni)
    bilgi["alan_dosyasi"] = n
    return bilgi


KOS = """#!/bin/bash
# Uc boyutlu vakayi cevirip cozer.  kullanim: kos3b.sh <vaka> [cekirdek]
set -e
VAKA="$1"; CEK="${2:-4}"
. /usr/share/openfoam/etc/bashrc >/dev/null 2>&1
cd "$VAKA"
rm -rf constant/polyMesh processor* log.*
gmshToFoam ag.msh > log.gmshToFoam 2>&1

# gmshToFoam her yamayi 'patch' yapar. Duvarin 'wall' olmasi turbulans
# modelinin duvar mesafesi ve duvar islemleri icin sarttir. kok/uc'un
# tipini vakayi kuran belirler; burada 0/U'daki tipten OKUNUR, varsayilmaz.
python3 - <<'PY2'
import re, io
tip = "symmetryPlane"
s0 = io.open("0/U").read()
m = re.search(r"\n    kok\n    \{\n\s*type\s+([A-Za-z]+);", s0)
if m:
    tip = m.group(1)
p = "constant/polyMesh/boundary"
s = io.open(p).read()
s = re.sub(r"(\n    duvar\n    \{\n\s*)type\s+patch;",
           r"\1type            wall;", s)
for a in ("kok", "uc"):
    s = re.sub(r"(\n    %s\n    \{\n\s*)type\s+patch;" % a,
               r"\1type            %s;" % tip, s)
io.open(p, "w").write(s)
print("  kok/uc tipi: %s" % tip)
PY2

checkMesh > log.checkMesh 2>&1 || true
grep -E "Max aspect|non-orthogonality|skewness|negative|Mesh OK|FAILED" log.checkMesh | sed 's/^/  /'

UYG=$(sed -n 's/^ *application *\\([A-Za-z]*\\);.*/\\1/p' system/controlDict | head -1)
UYG=${UYG:-simpleFoam}
echo "  cozucu: $UYG"
if [ "$CEK" -gt 1 ]; then
  decomposePar > log.decomposePar 2>&1
  mpirun --allow-run-as-root -np "$CEK" "$UYG" -parallel > log.$UYG 2>&1
  reconstructPar > log.reconstructPar 2>&1
else
  "$UYG" > log.$UYG 2>&1
fi
tail -3 log.$UYG
"""

if __name__ == "__main__":
    p = os.path.join(BURA, "kos3b.sh")
    open(p, "w").write(KOS)
    os.chmod(p, 0o755)
    print("yazildi:", p)
