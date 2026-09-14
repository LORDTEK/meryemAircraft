# Sürümler — hangi dosya nerede yayımlandı

Bu dosya bir tuzağı kapatmak için var. Depoda `makale-v5.md`, `makale-v6.md`
ve `makale-v7.md` yan yana duruyor; bir okuyucu haklı olarak "v6 dosyası
Zenodo'daki v6'dır" diye varsayar. Bir süre **öyle değildi**: v6 yatırıldıktan
sonra `makale-v6.md` üzerinde çalışmaya devam edildi, yani depodaki v6 ile
yayımlanmış v6 sessizce ayrıştı. Bu depoda "aynı ad, iki içerik" hatası daha
önce de dışarıya sızmıştı.

**Kural: yayımlanmış bir sürümün dosyası bir daha değiştirilmez.** Düzeltme
yeni bir sürüm numarası alır.

| Sürüm | Depodaki dosya | Yayımlandığı commit | Durum |
|---|---|---|---|
| v5 | `makale-v5.md`, `makale-v5-ek.md` | — | Zenodo'da yayımlandı |
| v6 | `makale-v6.md`, `makale-v6-ek.md` | `f208eca` | Zenodo'da yayımlandı; **dosya o hale geri alındı** |
| v7 | `makale-v7.md`, `makale-v7-ek.md` | `8138b62` | Zenodo'da yayımlandı — DOI `10.5281/zenodo.22745666`, sha `c5b0cd898d20` |

Sürüm numarası `makale/uretim/surum.py` içindedir ve **tek yerdedir**. Önce
öyle değildi: `mkdocx.py`, `mkekpdf.py` ve `baglanti.py` kendi kopyalarını
tutuyordu, ve `baglanti.py` sabit `"v6"` okuduğu için sürüm v7'ye çıktığında
**bayat dosyayı denetleyip "temiz" diyordu.** Geçtiğini sandığın bir denetim,
hiç olmayandan beterdir; bu depoda ikinci kez oldu.


## Sürüm DOI'si makaleye konmaz

Bir sürümün DOI'si, o sürüm yatırıldıktan **sonra** doğar. Makale kendi sürüm
DOI'sini içeremez; içermeye kalkarsa yatırılan dosya ile yereldeki dosya
ayrışır — yani yukarıdaki kural ihlal edilir. Bir kez denendi ve geri alındı.

**Makale yalnızca concept DOI taşır** (`10.5281/zenodo.22144194`), ki zaten
tam olarak bunun için vardır: her zaman en son sürüme çözülür.

**Sürüm DOI'si kapak mektubuna ait**, arşivlenen belgeye değil. Kapak mektubu
arşivlenmez, sonradan yazılır ve ikisini birden verebilir.
