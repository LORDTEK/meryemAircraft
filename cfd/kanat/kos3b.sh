#!/bin/bash
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
m = re.search(r"
    kok
    \{
\s*type\s+([A-Za-z]+);", s0)
if m:
    tip = m.group(1)
p = "constant/polyMesh/boundary"
s = io.open(p).read()
s = re.sub(r"(
    duvar
    \{
\s*)type\s+patch;",
           r"type            wall;", s)
for a in ("kok", "uc"):
    s = re.sub(r"(
    %s
    \{
\s*)type\s+patch;" % a,
               r"type            %s;" % tip, s)
io.open(p, "w").write(s)
print("  kok/uc tipi: %s" % tip)
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
