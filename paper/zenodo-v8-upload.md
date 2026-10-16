# Zenodo v8 — ne yüklenecek, hangi alana ne yazılacak

Zenodo'ya ben giremiyorum; aşağısı el ile yapılacak işin tamamı, sırayla.

## 1. Doğru yere yükle

**v7 kaydına git ve "New version" de.** Sıfırdan yeni kayıt açma: concept DOI
(`10.5281/zenodo.22144194`) zinciri kopar. v7 silinmez, DOI'si çalışmaya devam eder.

## 2. Yüklenecek dosyalar (hepsi `paper/zenodo-v8/` içinde)

| Dosya | Ne | SHA-256 (ilk 12) |
|---|---|---|
| `meryemAircraft-v8.pdf` | makale (33 sayfa) | `cfef04389de3` |
| `meryemAircraft-v8-supplement.pdf` | ek (S1–S11, 14 sayfa) | `5280cc7edc44` |
| `meryemAircraft-v8-source.zip` | iki belgenin LaTeX kaynağı, sınıf dosyası, Şekil 1 | `c22f2c2b71cb` |

Bunlar Journal of Aircraft'a gönderilen metnin **M-01 düzeltilmiş** hâlidir:
gövde Tablo 6 *"(Secs. III, VII)"*, ek S11 başlığı *"Working for Secs. III, VI.B and VII"*.
Başka hiçbir fark yok (metin karşılaştırması: yalnız bu iki satır).

## 3. Alanlar

- **Version:** `v8`
- **Publication date:** yükleme günü
- **Title:** `meryemAircraft: Tail-Sitting Blended-Wing Body for Vertical Takeoff Without Propulsor Reorientation`
- **Authors, Keywords, License:** v7 kaydındakiler; dokunma.
- **Description:** `paper/zenodo-v8.md` içeriğini olduğu gibi yapıştır.

## 4. Yükledikten sonra

Yeni sürüm DOI'sini bana söyle; kayda işlerim.

Doğrulama: `sha256sum paper/zenodo-v8/*`
