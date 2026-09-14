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
| v7 | `makale-v7.md`, `makale-v7-ek.md` | çalışılan sürüm | Zenodo'ya yükleniyor |

Sürüm numarası `makale/uretim/surum.py` içindedir ve **tek yerdedir**. Önce
öyle değildi: `mkdocx.py`, `mkekpdf.py` ve `baglanti.py` kendi kopyalarını
tutuyordu, ve `baglanti.py` sabit `"v6"` okuduğu için sürüm v7'ye çıktığında
**bayat dosyayı denetleyip "temiz" diyordu.** Geçtiğini sandığın bir denetim,
hiç olmayandan beterdir; bu depoda ikinci kez oldu.
