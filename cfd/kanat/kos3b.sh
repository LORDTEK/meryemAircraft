#!/bin/bash
# Uc boyutlu vakayi cevirip cozer.  kullanim: kos3b.sh <vaka> [cekirdek]
#
# Bu dosya ELDEN yazilir. Onceki surumde kur3b.py icinde bir Python dizgesi
# olarak tutuluyordu ve gomulu Python'un duzenli ifadelerindeki \n kacislari
# dizge cozumlemesinde yenip betigi bozuyordu (SyntaxError: unterminated
# string literal). Uretilen betikte kacis katmani ikiye ciktigi icin boyle
# oldu; katman kaldirildi.
set -e
VAKA="$1"; CEK="${2:-4}"
. /usr/share/openfoam/etc/bashrc >/dev/null 2>&1
cd "$VAKA"
rm -rf constant/polyMesh processor* log.*
# -keepOrientation ZORUNLU.
#
# gmshToFoam varsayilan olarak altigenleri KENDI sezgisiyle yeniden
# yonlendirir. O sezgi ince hucrelerde basarisiz oluyor: y+ = 1 aginda
# 31 868 hucreyi negatif, 99 193 yuzu yanlis yonlu yapiyordu ve azami
# dikey olmayanligi 179,96 dereceye cikariyordu.
#
# Kusurun agda OLMADIGI gosterildi: .msh dosyasindaki 2 271 040 altigenin
# hicbirinin hacmi negatif degil. Ustelik tek bir bozuk hucre incelendi --
# gmshToFoam'in kurdugu 6 yuz, uretecin sablonuyla BIREBIR ayni (6/6), ama
# hacim .msh sirasiyla +6,577e-9, polyMesh'ten -6,577e-9. Buyukluk ayni,
# yalnizca yonelim ters.
#
# -keepOrientation ile ayni ag: 0 negatif hucre, 0 yanlis yonlu yuz,
# azami dikey olmayanlik 89,69. Bu bayrak olmadan y+ = 1 agi -- yani
# gecis modelinin gerektirdigi ag -- kurulamiyor.
gmshToFoam -keepOrientation ag.msh > log.gmshToFoam 2>&1

# gmshToFoam her yamayi 'patch' yapar. Duvarin 'wall' olmasi turbulans
# modelinin duvar mesafesi ve duvar islemleri icin sarttir. kok/uc'un tipi
# 0/U'dan OKUNUR, varsayilmaz -- vakayi kuran karar verir.
python3 - <<'PY2'
import re, io
U = io.open("0/U").read()
tip = "symmetryPlane"
m = re.search(r"\n    kok\n    \{\n\s*type\s+([A-Za-z]+);", U)
if m:
    tip = m.group(1)
# UC AYRI. Onceden kok ile ayni tipe cevriliyordu; yanlisti. Kanat ucta
# bitmiyor, uc duzleminden disariya akis var ve o duzlem serbest akisa
# aciliyor -- 0/U'da "(disalan|uc)" olarak disalan ile ayni kosulu aliyor.
# symmetryPlane yapmak orada akisi duzleme TEYELLER, yani uc girdabini
# yapay olarak bastirirdi. Serbest akis yamasi 'patch' KALMALIDIR.
uc_serbest = '"(disalan|uc)"' in U
p = "constant/polyMesh/boundary"
s = io.open(p).read()
s = re.sub(r"(\n    duvar\n    \{\n\s*)type\s+patch;",
           r"\1type            wall;", s)
s = re.sub(r"(\n    kok\n    \{\n\s*)type\s+patch;",
           r"\1type            %s;" % tip, s)
if not uc_serbest:
    s = re.sub(r"(\n    uc\n    \{\n\s*)type\s+patch;",
               r"\1type            %s;" % tip, s)
io.open(p, "w").write(s)
print("  kok tipi: %s   uc: %s" % (tip, "serbest akis (patch)" if uc_serbest else tip))
PY2

checkMesh > log.checkMesh 2>&1 || true
grep -E "Max aspect|non-orthogonality|skewness|negative|Mesh OK|FAILED" log.checkMesh | sed 's/^/  /'

UYG=$(sed -n 's/^ *application *\([A-Za-z]*\);.*/\1/p' system/controlDict | head -1)
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
