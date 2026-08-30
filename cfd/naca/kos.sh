#!/bin/bash
# Bir vakayi cevirip cozer.  kullanim:  kos.sh <vaka-dizini> [cekirdek]
set -e
VAKA="$1"; CEK="${2:-4}"
. /usr/share/openfoam/etc/bashrc >/dev/null 2>&1

cd "$VAKA"
rm -rf constant/polyMesh processor* log.*
gmshToFoam ag.msh > log.gmshToFoam 2>&1

# gmshToFoam butun yamalari 'patch' yapar. Duvarin 'wall' olmasi
# turbulans modelinin duvar mesafesini ve duvar islemlerini dogru
# kurmasi icin sarttir; on/arka ise iki boyutlu cozum icin 'empty'.
python3 - <<'PY'
import re, io
p = "constant/polyMesh/boundary"
s = io.open(p).read()
s = re.sub(r"(\n    duvar\n    \{\n\s*)type\s+patch;", r"\1type            wall;", s)
for a in ("on", "arka"):
    s = re.sub(r"(\n    %s\n    \{\n\s*)type\s+patch;" % a,
               r"\1type            empty;", s)
io.open(p, "w").write(s)
PY

checkMesh > log.checkMesh 2>&1 || true
grep -E "Max aspect|non-orthogonality|skewness|negative" log.checkMesh | sed 's/^/  /'

# Cozucu controlDict'ten OKUNUR, varsayilmaz. Onceden simpleFoam sabit
# yazilmisti; zamana bagli bir vaka kurulunca (pimpleFoam, backward ddt,
# PIMPLE sozlugu) yine simpleFoam calisti, iraksadi ve SIGFPE verdi.
# Belirti yanilticiydi -- yigin izi "pimpleFoam cokmus" gibi degil,
# "/usr/bin/simpleFoam" diyordu.
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
