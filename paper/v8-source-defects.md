# Kaynak kusurları kütüğü (Tur 87; Qwen P1, DeepSeek, ChatGPT'nin köken alanı)

Envanter ve iz tablosunun **kaynak metinde** bulduğu kusurlar. Köken **S** = kaynakta zaten vardı; **R** = yeniden kurma
kırdı (şimdiye dek **R yok**). Durma kuralı yalnız R'yi ve onarılmamış kusuru sayar (CLAUDE.md §2.3). Bir blok yeniden
açılırsa bu kusurlar geri gelmesin diye her birinin emekli ifadesi `v8_stale.py`'de.

| # | Tur | Nerede | Kusur | Onarım | Köken |
|---|---|---|---|---|---|
| #18 | 76–77 | Adım 4 | "shows the transfer property" envanterin izin verdiğinden güçlü | "is consistent with" + 580/679/99 | S |
| S-1 | 77–80 | Adım 2E | tablo fatura ile para birimini karıştırıyor; "One row does not pay in any of the three currencies" yanlış | A′, B′, C, C4, C5, H | S |
| S-5 | 78–83 | Adım 2F | "no worse" tabansız; "leaves another standing is not a counter-example" olumlu sınamayla çelişiyor | S5-1..S5-4, 3.1 | S |
| S-6 | 83–84 | Adım 3B | üç özellik sayılıyor, dört sapma listeleniyor | R1 | S |
| S-7 | 84–85 | Adım 3C | "the table" Tur 64'te S3'e taşınan tabloya işaret ediyordu | C4, C5 | S (Tur 64 taşımasının artığı) |
| S-8 | 85–86 | Adım 3, 9, 11 | "a mass one" / "charges that refusal" — fatura sözcüğü fatura olmayan şey için | "a cost in kilograms" / "sets" | S |
| S-9 | 86–87 | Adım 3F | "Those are three separate questions" yanlış üçlüye işaret ediyor | F1 | S |
| S-10 | 86–87 | Adım 3F | "Section 11 … the longest of the three answers" yanlış | F2 | S |
| S-11 | 86–87 | Adım 13 | "the tilt row" — gövde tablosunda tilt satırı yok (S13'e taşınmış) | "the tilting layout" | S (taşıma artığı) |
| S-12 | 86–87 | Adım 13 | "charges all three the same assumption" — fatura sözcüğü genel fiil | "puts the same assumption on all three" | S |
| açık | 86 | Adım 3E mod 4 | "re-opens the charge it fails" gevşek (bir parça koşulun bir parçasını başarısız kılar, fatura yeniden açılır) | 3E kilitli; ertelendi | S |
| aday | 87 | Adım 10 | "cannot charge for the trajectory" — fatura sözcüğü genel fiil | oylamada: "cannot account for" | S |

**Kümelenme (Qwen):** 12 kusurun 3'ü **taşıma artığı** (S-7, S-11 ve ilk durumu S-1'in bir kısmı): bir tablo ya da paragraf
başka yere taşındığında geride kalan atıf. `v8_refs.py` bunun için var.
