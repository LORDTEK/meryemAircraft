# Dış görüş — Tur 4: yerelleşmiş k kaçışı

Önceki turda "27 saatlik koşu dönüyor, bitmeden söylenmesi gereken bir şey
var mı" diye sormuştum. İkiniz de "durdurma, fizik ayarlarına dokunma,
ara yazmaların olduğundan emin ol" dediniz. Ara yazmalar vardı ve **onlar
sayesinde teşhis yapılabildi.**

Koşu bitmedi. **İki kez çöktü.** Sebebi ölçüldü, çaresi yok. Bu metin
teşhisin kaydı ve bir soru.

---

## Giriş — bağlam

Kuyruk üstü oturan, BWB gövdeli VTOL İHA konfigürasyon çalışması.
OpenFOAM v1912, `simpleFoam`, yapısal C-grid, 2 263 560 hücre,
Re_kök = 1,99e6, α = 0°.

Koşulan: **k-ω SST, y⁺≈1, tam türbülanslı, 5000 adım.** Amaç, sürükleme
belirsizlik tablosundaki boş hücreyi doldurmak:

| | SA | k-ω SST |
|---|---|---|
| y⁺≈20 | 0,01452 | 0,01344 |
| y⁺≈1 | **0,014750** (5000 adım, sorunsuz) | **bu koşu** |

---

## Gelişme

### 1. İki çöküş

| koşu | başlangıç | çöküş | kusur |
|---|---|---|---|
| A | tek biçimli alan, adım 0 | **2169** | `SIGFPE`, hız denklemi, `symGaussSeidelSmoother` |
| B | A'nın 2000. adımından | **2186** | aynı |

### 2. Dört hipotez ÖLÇÜMLE çürütüldü

| hipotez | ölçüm | sonuç |
|---|---|---|
| basınç çözücü `relTol` gevşetmem (0,01 → 0,05) | iki ayarla da ~aynı yerde patlıyor (2144 / 2165) | **çürütüldü** |
| uç kapak, azami çarpıklık 89,7° | patlama z/yarı = 0,458, uçta değil | **çürütüldü** |
| patlama yerinde kötü ağ | orada azami dikey-olmayanlık **39,29°**, ortalama 26,94° | **çürütüldü** |
| kesit t/c'sinin tamsayıya yuvarlanması | üreteç kesirli t/c geçiyor, yüzeyde basamak yok | **çürütüldü** |

Ağın gerçekten kötü yüzleri (89,65°) **iz kesiğinde**, z/yarı = 5,0–5,6,
kanattan çok uzakta — patlamayla ilgisiz.

### 3. Patlamanın yeri

| | |
|---|---|
| açıklık | z/yarı = **0,458** — tam ağ istasyonu 11'de |
| veter | yerel **x/c = 0,11**, üst yüzey |
| duvardan | ~0,0008 m ≈ yerel sınır tabakanın %35'i |

Geometride orada kırılma yok: ok açısı 41,968 → 41,935 → 41,901, veter
ve t/c düzgün.

### 4. Mekanizma — patlamadan ÖNCE (adım 2100) ölçüldü

Patlama noktasındaki duvar-normal sütun:

| duvardan | k | ω | ν_t/ν |
|---|---|---|---|
| ilk hücre | 0,475 | 5,29e6 | 0,18 |
| 0,0008 m | **8,205** | 2,17e4 | **625** |
| 0,0047 m | 5,793 | 9 409 | **1107** |

U∞ = 1 olduğu için k = 8,2, türbülans şiddeti √(2k/3)/U = **%234**
demektir. Türbülanslı sınır tabaka için beklenen k ≈ 0,005 — yani
**1600 kat fazla.**

Ve tamamen yerel. Açıklık bandına göre k_max:

| z/yarı | k_max |
|---|---|
| 0,3–0,4 | 2,32 |
| **0,4–0,5** | **8,21** |
| 0,5–0,6 | 0,0160 |
| 0,6–0,7 | 0,0089 |
| 0,9–1,0 | 0,0584 |

Komşu bantlar fiziksel mertebede (0,0089 ≈ beklenen 0,005). **Bir bant
1000 kat fazla.**

### 5. Asıl bulgu — tarihçe

k_max'in bütün koşu boyunca izi:

| adım | k_max |
|---|---|
| 15 | 1,72 |
| **61** | **10 391** |
| 107 | 3 132 |
| 1563 | 41,7 |
| 1791 | 21,1 |
| 1980 | 11,5 |
| 2135 | 7,34 |
| 2180 | 337 899 → çöküş |

Yani hot spot **başlangıç geçici rejiminde doğdu** (61. adımda 10 391),
sonraki 2000 adımda üç mertebe söndü — ama fiziksel değere (0,005) hiç
inemedi, 7,3'te takıldı ve oradan patladı.

Bu, tek biçimli başlangıç alanını (k = 1,5e−06, ω = 3,08 her yerde)
doğrudan işaret ediyor: erken adımlardaki şiddetli geçici rejim yerel
bir k yığını yaratıyor, sönüyor ama tamamen temizlenmiyor, sonra
kararsızlaşıyor. SST'nin üretim sınırlayıcısı (P_k ≤ 10 β* k ω) onu
tutamıyor.

### 6. Bu turda üç kez yanıldım

Kayda geçirdim, tekrar etmemek için burada da yazıyorum:

1. **"Referans alanı hatası var, bütün 3-B C_D'ler %1,05 düşük."**
   Kod okumasıyla vardım (varsayılan `Aref=1.0`, hiçbir çağıran geçmiyor).
   Sonucu doğrudan sınayınca kayıttaki değerin zaten ölçülmüş alanla
   üretildiği çıktı. Geri alındı.
2. **"`relTol` çöküşün sebebi, tek değişkenle kanıtlandı."** 12 adım
   geçmeyi kanıt saydım; 17 adım sonra aynı çöküş geldi.
3. **Tanılama hatası.** `bounding k, min: X max: Y average: Z` satırında
   `$NF` **average**'dır. Ortalamayı okuyup "k_max" diye raporladım;
   "koşu sağlıklı, k_max 1,77" dediğim anda gerçek k_max 1 377 609'du.

---

## Sonuç — sorular

### 0. En önemlisi: başlangıç alanı hipotezi doğru mu?

Tarihçe (61. adımda 10 391 → 2135'te 7,3 → patlama) bana şunu
söylüyor: **sorun çözümün kendisinde değil, ona nasıl varıldığında.**

Elimde bu ağda **yakınsamış bir SA çözümü** var (y⁺=1, 5000 adım,
C_D = 0,014750). Ondan k ve ω türetip k-ω koşusunu oradan başlatmayı
düşünüyorum. Ama:

- `mapFields` bu kurulumda **kırık** (segfault), aynı ağ olduğu için
  gerekmiyor da — alanları doğrudan yazabilirim.
- SA yalnızca ν_t veriyor; k ve ω'ya ayırmak için ek bir varsayım
  gerekiyor. Yerel denge varsayımıyla ω = S/√(β*) ve k = ν_t·ω
  düşünüyorum. **Bu doğru mu, yoksa daha standart bir yol var mı?**

### 1. Yerelleşmiş k kaçışının bilinen çaresi ne?

Tek bir açıklık istasyonunda, hücum kenarına yakın, sınır tabaka içinde
k'nın 1000 kat şişmesi ve komşu istasyonların temiz kalması — bu bilinen
bir arıza kipi mi? Literatürde adı var mı?

### 2. Denenmemiş dört çareden hangisi?

1. k ve ω gevşetmesini düşürmek (0,5 → 0,3).
2. `nutLowReWallFunction` yerine `nutUSpaldingWallFunction` (y⁺≈1'de de
   geçerli; k'nın duvar koşulu da değişir — şu an `fixedValue 1e-14`).
3. Üretim sınırlayıcısını sıkmak, ya da Kato–Launder.
4. O istasyonda açıklık yönünde ağı sıklaştırmak.

Sıralamanız ne olurdu? Hiçbirini denemedim çünkü bu turda iki kez
"çare buldum" deyip yanıldım.

### 3. Duvar işlemi seçimi doğru mu?

y⁺≈1'de kurulum şu: `nut` → `nutLowReWallFunction`, `k` → duvarda
`fixedValue 1e-14`, `omega` → `omegaWallFunction blended true`.
İlk hücrede ölçülen: k = 0,475, ω = 5,29e6, ν_t/ν = 0,18.
Bu üçlü y⁺≈1 + SST için doğru mu?

### 4. Bu, makale için gerçekten gerekli mi?

SA aynı ağda y⁺=1'de zaten koştu ve sonucu var. Kaybedilen, 2×2
tablosunun dördüncü hücresi — "model etkisi y⁺=1'de ne kadar" sorusu.
Model etkisi y⁺≈20–43'te ölçülmüş durumda (%2,7–8,1).

**Bu tek hücre için ne kadar uğraşmalı?** Yoksa "duvar çözümlü sonuç
SA'dan alındı, k-ω o çözünürlükte yerel bir kararsızlık verdi ve
kullanılmadı" diye dürüstçe yazıp geçmek mi doğru?

### 5. Atladığım ne var?

Önceki iki turda bu soruyu sordum ve ikinizde de gerçek bir eksik
çıktı. Yine soruyorum.
