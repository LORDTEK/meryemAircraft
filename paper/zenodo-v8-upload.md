# Zenodo v8 — ne yüklenecek, hangi alana ne yazılacak

Zenodo'ya ben giremiyorum; aşağısı el ile yapılacak işin tamamı, sırayla.

## 1. Doğru yere yükle

**v7 kaydına git ve "New version" de.** Sıfırdan yeni kayıt açma: concept DOI
(`10.5281/zenodo.22144194`) zinciri kopar. v7 silinmez, DOI'si çalışmaya devam eder.

## 2. Yüklenecek dosyalar (hepsi `paper/zenodo-v8/` içinde)

| Dosya | Ne | SHA-256 (ilk 12) |
|---|---|---|
| `meryemAircraft-v8.pdf` | makale (33 sayfa) | `45e5ed5585fc` |
| `meryemAircraft-v8-supplement.pdf` | ek (S1–S11, 14 sayfa) | `5d33e4041878` |
| `meryemAircraft-v8-source.zip` | iki belgenin LaTeX kaynağı, sınıf dosyası, Şekil 1 | `0a6931ad5015` |

Gönderilen metinden iki fark var, başka yok (sözcük düzeyinde metin karşılaştırması):
1. **M-01:** gövde Tablo 6 *"(Secs. III, VII)"*, ek S11 başlığı *"Working for Secs. III, VI.B and VII"*.
2. **Basitlik iddiası (yazarın kararı, 2026-10-17, seçenek b):** dört yerde değişti.
   - V.A: *"The arrangement is therefore mechanically simpler than a tilting architecture: a moving mechanism is more complex than a fixed structure, and the mechanism classes a tilting architecture needs to change regime are absent here; …"*
   - Tablo 6: *"… are absent (Sec. V.A), so the arrangement is mechanically simpler."*
   - VIII.D: *"It does not claim mechanical simplicity"* maddesi çıktı; başlık *"Seven Things …"*.
   - VIII.E: *"The aircraft is therefore mechanically simpler than a tilting architecture, though not one in which nothing moves."*

   Güvenilirlik iddiası eklenmedi.

## 3. Alanlar

- **Version:** `v8`
- **Publication date:** yükleme günü
- **Title:** `meryemAircraft: Tail-Sitting Blended-Wing Body for Vertical Takeoff Without Propulsor Reorientation`
- **Authors, Keywords, License:** v7 kaydındakiler; dokunma.
- **Description:** `paper/zenodo-v8.md` içeriğini olduğu gibi yapıştır.

## 4. Yükledikten sonra

Yeni sürüm DOI'sini bana söyle; kayda işlerim.

Doğrulama: `sha256sum paper/zenodo-v8/*`
