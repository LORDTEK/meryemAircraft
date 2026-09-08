# Bir sonraki dış görüş metnine MUTLAKA girecekler

*(Bu dosya taslak deposudur; metin yazılırken buradan derlenecek.)*

## 1. CFD — geri alınan yorum ve yerine geçen ölçüt

- **Geri alındı:** "kararlı RANS iki ayrı durağan çözüme oturuyor."
  Delilin taşıdığından fazlaydı.
- Ayrılma topolojisi **birebir aynı**: %0,02 ters akış alanı, aynı x
  aralığı (1,003–1,740 m) — iki vakada da.
- Basınç farkı açıklık boyunca **düzgün dağılmış** (sekiz bandın her
  biri farkın ~1/8'i), yerel değil.
- **Simetri ölçütü:** simetrik NACA 00xx, burulma yok, α=0 → C_L = 0
  olmalı. bl_C = 1,45e−03; bl_E = 1,35e−04. bl_E **10,8 kat** daha
  yakın. Cp'de üst/alt asimetri: bl_C 0,0249, bl_E 0,0011 (her
  istasyonda ~10 kat).
- Asimetrinin indüklenen sürüklemesi ihmal edilebilir (≈1,1e−07,
  C_D'nin milyonda 9'u) → **sebep değil, belirti**.
- **Yeni ifade:** iki çözüm eşit değerde değil; bl_E daha iyi
  koşullanmış. Aralık (0,01201–0,01253) yine yazılıyor ama tek değer
  gerekirse bl_E, **artığa göre değil fiziğe göre** seçiliyor.
- Bu, YZ1 ("üçüncü başlangıç gerekmez") ile YZ3 ("gerekir")
  ayrışmasını çözdü: üçüncü koşu yerine simetri ölçütü karar verdi.
- **Sorulacak:** simetri ölçütü meşru mu? Ağ üst/alt simetrik değilse
  her iki vaka da eşit etkilenirdi — bu savunma yeterli mi?

## 2. Temel model — YZ3'ün bulduğu sözleşme sorunu

- Sabit yakıt kesri **kütle faturasını menzilden siliyor**.
- Üç sözleşme uygulandı; C'ye ×1,00 hediyesi hâlâ dururken:

  | | sabit kesir | sabit yakıt kütlesi | sabit MTOW+faydalı |
  |---|---|---|---|
  | B | −%14,4 | −%36,5 | −%72,6 |
  | C | +%12,0 | +%0,2 | −%19,1 |

- L/D çarpanıyla çapraz: 12 kutunun 3'ünde C önde, üçü de birinci
  sütunda.
- **YZ3'ün düzeltilen sayısı:** sabit yakıt kütlesinde elle −%7 demiş;
  60,3 kg'ı (sabit KESİR MTOW'u) kullanmış. Yakıt sabitlenince C'nin
  MTOW'u 55,9'a kapanıyor → model **+%0,2**. Sabit MTOW'da YZ3 tam
  tutuyor: −%19 / −%19,1, f_yakıt 0,116 / 0,116.
- **Sorulacak:** üç sözleşmeden hangisi Q1 için "ana" tablo olmalı?
  Yoksa üçü de eşit ağırlıkta mı verilmeli?

## 3. Ölçülmüş ve çürütülen küçük iddialar

- η_seyir menzile **etki etmiyor** (R formülünde yok) — YZ5'in "ikinci
  hediye" tespiti yalnızca kütle sütununda geçerli.
- B'nin yapısal cezası menzili değiştirmiyor, MTOW'u 86→117 kg yapıyor.
- Çift sayım **yok** (YZ1 §17 ve YZ3 §5.2 kontrol edildi).
- Motor derecelendirme payı: tam ayarsız ağır hatta motor **+%16,9**
  sapıyor, menzil −%0,1, L/D %0,0.

## 4. Yapılan makale değişiklikleri

- Başlık: "Eliminating" → **"Reducing"**.
- Yeni **§5.5** (karşılaştırmalı boyutlandırma, üç sözleşme).
- Yeni **§8.12** (koşulluluk: ölçülmemiş çarpan **ve** sözleşme).
- Yeni **§8.13** (motor payı tutarsızlığı).
- §6.6 ve §8 yeniden yazıldı (başlangıç yayılımı + simetri ölçütü).
- Özete karşılaştırma ve "tilt ailesine üstünlük iddia edilmiyor".

## 5. Şu an yapılan iş

**Bileşen düzeyinde kütle bütçesi.** Üç denetim de listeledi; YZ3 Q1
için zorunlu saydı. Sonucu bir sonraki metnin ana gövdesi olacak.
