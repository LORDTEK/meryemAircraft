# Kaynakça — yerel PDF dizini

Bu dizin, çalışma sırasında doğrudan okunan birincil kaynakları tutar.
Makalenin atıf listesi burada değil, `makale/bolumler/10-references.md`
dosyasındadır. Buradaki dosyalar okunmak için var, atıf için değil.

**Depoda iki kaynak dizini var, karıştırılmamalı:**

| Dizin | İçerik | Neden ayrı |
|---|---|---|
| `cfd/kaynak/` | CFD doğrulama kaynakları (NASA TMR, NAS teknik raporu, NACA 0012 doğrulama vakası) | Sayısal iddialara **dayanak**. `cfd/veri/referans.py` ve `cfd/ortak/cagi.py` bu dosyalara sayfa numarasıyla atıf yapar; taşınırsa kod bozulur. |
| `kaynakca/` (bu dizin) | Genel okuma kaynakları | Koda gömülü atıf yok. Okunup anlaşılmak için var. |

| Dosya | Kaynak | Neden burada |
|---|---|---|
| `Langtry_2006_PhD.pdf` | Langtry, R.B. (2006), *A Correlation-Based Transition Model using Local Variables for Unstructured Parallelized CFD Codes*, doktora tezi, Universität Stuttgart | γ-Re_θ geçiş modelinin birincil kaynağı. Ağ gereksinimleri (y⁺ ≈ 1, normal genişleme oranı 1.1-1.15, sınırlı 2. mertebe upwind) s. 42-43. OpenFOAM'ın `kOmegaSSTLM` modeli bunun uygulamasıdır. |
| `Medida_2014_PhD_Maryland.pdf` | Medida, S. (2014), *Correlation-based Transition Modeling for External Aerodynamic Flows*, doktora tezi, University of Maryland | γ-Re_θ-SA modeli: geçiş denklemlerini k-ω yerine Spalart–Allmaras'a bağlar. Model §3.4'te tam haliyle. Bkz. `cfd/gecis-modeli-fizibilite.md`. |
| `7178ed2b-...pdf` | TÜRKPATENT, *Patent/Faydalı Model Başvuru Kılavuzu* | Patent başvurusu hazırlanırken kullanıldı. |

## Notlar

- `Kap01_05_1.pdf` silindi: `Langtry_2006_PhD.pdf` ile bit-bit aynıydı
  (md5 `937e4f6f3e2cc66b03b8903d033b01f9`).
- Dosyalar git geçmişinde kalıcı olduğu için silmek depo boyutunu
  küçültmez; bu yüzden ileride kaynak eklerken boyuta dikkat.
- Yeni kaynak eklenirken bu tabloya bir satır eklenmeli; yoksa altı ay
  sonra dosyanın neden orada olduğu bilinmez.
