#!/bin/bash
# Ayristirilmis bir vakayi SIFIRLAMADAN son yazilan zamandan surdurur.
#
# Neden var: bu ortamda konteyner yeniden baslayabiliyor ve kosan her sey
# oluyor. Bir kez oldu ve 4152 zaman adimi (t = 0,414'e kadar) yarim
# kaldi. kos.sh vakayi bastan kurar -- processor* dizinlerini ve agi
# siler -- yani surdurmek icin kullanilamaz. Bu betik yalnizca
# controlDict'i ayarlar ve mevcut ayristirma uzerinde cozucuyu yeniden
# baslatir; ag da, o ana kadar hesaplanan zamanlar da korunur.
#
#   kullanim:  devam.sh <vaka-dizini> <yeni-endTime> [cekirdek]
set -e
VAKA="$1"; SON="$2"; CEK="${3:-4}"
. /usr/share/openfoam/etc/bashrc >/dev/null 2>&1
cd "$VAKA"

if [ ! -d processor0 ]; then
  echo "devam.sh: processor0 yok -- bu vaka ayristirilmamis, kos.sh kullanin" >&2
  exit 1
fi
ONCE=$(ls processor0 | grep -E '^[0-9]' | sort -g | tail -1)
echo "devam: son yazilan zaman $ONCE -> $SON"

UYG=$(sed -n 's/^ *application *\([A-Za-z]*\);.*/\1/p' system/controlDict | head -1)
sed -i 's/^startFrom .*/startFrom       latestTime;/' system/controlDict
sed -i "s/^endTime .*/endTime         $SON;/" system/controlDict

# log dosyalarinin ustune yazma: eskisi saklanir, yenisi eklenir
i=1; while [ -e "log.$UYG.$i" ]; do i=$((i+1)); done
[ -e "log.$UYG" ] && mv "log.$UYG" "log.$UYG.$i"

mpirun --allow-run-as-root -np "$CEK" "$UYG" -parallel > "log.$UYG" 2>&1
reconstructPar -latestTime > log.reconstructPar 2>&1
tail -3 "log.$UYG"
