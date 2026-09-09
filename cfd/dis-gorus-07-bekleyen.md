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

---

## 6. DİĞER YZ'LERE SORULACAK — açık kalan kaynak soruları (09.09.2026)

### ⚠️ S1. inviscid → Oswald açıklık verimi oranı (0,85–0,90)

**Neden önemli:** §6.6 bu oranı **kaynaksız** kullanıyor ve şu an bir
**başlık sayısı** ona bağlı. Denge için gereken 9° burulma, iskoz olmayan
açıklık verimini 0,99'dan 0,865'e düşürdü. Aynı oranla:

| | inviscid | ima edilen Oswald | varsayılan 0,85 |
|---|---|---|---|
| burulmasız | 0,99 | 0,84–0,89 | içinde → temkinli |
| **burulmalı** | **0,865** | **0,735–0,78** | **üstünde → iyimser** |

Doğruysa seyir L/D 12,04 → **11,4–11,7**, menzil **%3–5** düşüyor
(1598 → ~1520–1550 km).

**Sorulacak:** Bu oran için **birincil bir kaynak** var mı? Ya da doğrudan
kuyruksuz/BWB bir kanat için ölçülmüş **Oswald** verimi? Alternatif olarak:
burulmalı kanadın iskoz hesabı olmadan bu soruyu kapatmanın savunulabilir
bir yolu var mı, yoksa menzil sayıları "koşullu" mu yazılmalı?

**Şu an metinde ne yazıyor:** düzeltme **yapılmadı**. Kaynaksız bir oranı
başlık sayısına yaymak, belirtilmiş bir varsayımı belirtilmemişle
değiştirmek olurdu. Yazılan şey yapısal nokta: varsayım artık bir hesapla
**üstten sınırlı değil.**

### 🔎 S1 KISMEN KAPANDI (09.09.2026 akşamı) — sonuç orandan bağımsız

Traub 2024 hem **inviscid** (AVL) hem **ölçülmüş** Oswald faktörü veriyor.
Kp'lerinden türettim (AR = 3):

| | ölçülen e | inviscid e | oran |
|---|---|---|---|
| düz (planar) | 0,947 | 1,001 | **0,946** |
| dairesel | 1,220 | 1,206 | 1,011 |
| köşegen | 1,179 | 1,105 | 1,067 |

İkisi 1'in **üstünde** — gerçek bir kanatta olamaz; duvar düzeltmesi
uygulanmamış bir tünel ölçümünü inviscid hesapla karşılaştırmanın
artefaktı. Yani bu veri oranı **sabitlemiyor**, gevşek sınırlıyor.

**Ama sonucun işareti bütün bantta ayakta:**

| oran | ima edilen Oswald e | seyir L/D | 12,04'e göre |
|---|---|---|---|
| 0,85 | 0,735 | 11,44 | −%5,0 |
| 0,90 | 0,778 | 11,68 | −%3,0 |
| 0,95 | 0,822 | 11,90 | −%1,2 |

**1'in altındaki her oran için** — yani iskozitesi olan her kanat için —
burulmalı açıklık verimi 0,85'in altında ve seyir L/D 12,04'ün altında.
Yalnızca **büyüklüğü** açık: %1–5.

Dolayısıyla YZ'lere sorulacak soru daraldı: *oranı bilmemize gerek yok,
burulmalı kanadın **iskoz hesabı** lazım.* Bir de: 0,85 varsayımı
konvansiyonel (Ugwueze 2023 de AR 7,0'da aynı değeri kullanıyor), yani
dikkatsizlik değil — bu yüzden bu kadar uzun süre sorgulanmadan kaldı.

### S2. Şeridin yükseklik yasası — takas kapatılmadı

Sabit h/c seyirde sürüklemeyi %64 azaltıyor ama izdeki alanı %45
azaltıyor. Hangi mekanizmanın **asılı durumda** baskın olduğu belirlenmedi.

### S3. Uç çerçevesi fairing'inin toe açısı — BÜYÜKLÜK BULUNDU, İŞARET AÇIK

NACA TR-796: yüksek en-boy oranlı finler toe-out ister, düşük olanlar toe-in;
ve toe-out'ta arka fin perdövitese girerse **kararsızlaştırıcı** moment doğuyor.

**Büyüklük ölçülmüş (NASA TM-78767, 09.09.2026):** uç podlarında dikey kuyruk
taşıyan kuyruksuz ok kanatlı bir kargo konfigürasyonunda, (L/D)max için
**optimum toe açısı ~1,5°** (simetrik kesitli kuyruklar). Yani açı **bir-iki
derece mertebesinde**, on derece değil. Ve aynı testler L/D'nin üç kuyruk
tasarımında da "about the same" olduğunu buluyor, **%75 daha büyük alana
rağmen** — bizim "gereken veter zaten olması gerekenin içinde" argümanımızın
ölçümle gelen hâli.

**Açık kalan: İŞARET.** O çalışmanın finleri düşük en-boy oranlı ve toe-in
istiyor; TR-796 yüksek en-boy oranlılar için toe-out diyor; bizim çerçeveler
(1,42 m boy / on milimetrelerce veter, AR ~20-28) **her iki kaynağın da
aralığının dışında.**

**Sorulacak:** Çok yüksek en-boy oranlı (AR > 15) uç finlerinde toe açısının
işareti ne olmalı, ve perdövites arıza kipi bu AR'de nasıl davranıyor?

### 🔴 S4. Refleks kesitlerin gerçek C_m0 mertebesi — EN ÖNEMLİ AÇIK SORU

**Neden bu kadar önemli:** denge zincirinin tamamı buna bağlı. VLM taramasından
C_m derece başına 0,00629; kesit ne verirse burulma gerisini tamamlıyor:

| kesit C_m0 | gereken burulma | inviscid e | seyir L/D |
|---|---|---|---|
| 0 | 9,2° | 0,865 | 11,68 |
| **0,004 (elimizdeki tek ölçüm)** | **8,6°** | 0,875 | 11,73 |
| 0,020 | 6,0° | 0,937 | **12,01** |
| 0,050 | 1,3° | 0,986 | 12,21 |

Yani **0,02 veren bir kesit varsa, denge cezası neredeyse tamamen geri
kazanılıyor** ve §5.4'ün beşinci defter kalemi (%4,3) büyük ölçüde siliniyor.

**Elimizdeki kanıt tek bir sayı:** NACA TR-460'ın ölçtüğü 2R212 → **+0,004**.
1933 tarihli. Makalede bunun seçimi taşıdığı açıkça yazılı.

**Sorulacak — açıkça bu biçimde:** Elimizdeki tek ölçüm **1933 tarihli**
(NACA TR-460). Sayı sağlam, ama bir hakem *"doksan yıllık bir rapordan başka
dayanağınız yok mu?"* diye sorar ve haklı olur. **Aynı şeyi söyleyen daha
güncel, daha yerleşik, daha çok atıf alan bir yayın var mı?**

Aranan: refleks bir kesit için **ölçülmüş** (tercihen rüzgâr tüneli) C_m0,
kesit adıyla ve koşullarıyla. XFOIL/XFLR5 poları da kabul, ama kaynağı,
Reynolds'u ve doğrulaması belli olmalı. TR-460'ı **değiştirmek** değil,
**yanına koymak** istiyoruz — eski ölçüm sağlam, yalnız yalnız kalmasın.

⚠️ **Kullanmadığımız bir kaynak — ve nedeni.** Shinde 2020 (*Micromachines*
11(6):553) on refleks kesit için C_m0 tablosu veriyor, hepsi **10⁻⁴** ve hepsi
**negatif**. Ama aynı makale iki sayfa önce *"C_m0 must be positive"* diyor.
Kendi içinde tutarsız, ve gerçek refleks kesitlerin C_m0'ı standart
kaynaklarda 10⁻³–10⁻² anılır. **Bu tablodan hiçbir sayı alınmadı**; kaynak
yalnızca (a) denge gereksiniminin ifadesi ve (b) pratik kesit ailesinin listesi
için anılıyor. Uzlaştıramadığımız bir büyüklüğü aktarmayız.

**YZ'lere sorulacak ek soru:** Shinde'nin tablosu gerçekten hatalı mı, yoksa
bizim okumadığımız bir normalizasyon/işaret kuralı mı var?
