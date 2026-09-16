# v8 kelime bütçesi — AIAA'nın kendi sayısıyla

**Kaynak:** AIAA *"Journal Page Limits and Word Count Guidelines"*, Ağustos 2024,
yazar tarafından yapıştırıldı. Birinci elden.

---

## 1. Kural

| | |
|---|---|
| Regular/Full Article | **7–10 basılı sayfa, 10 000–12 000 kelime** |
| Bir basılı sayfa | **1 400 kelime** *"veya şekil/tabloların kapladığı eşdeğer yer"* |
| Çift satır aralıklı müsvedde karşılığı | 10 punto Times ile **20–26 sayfa** |

**Şekil ve tablolar kelime olarak sayılıyor:**

| Nesne | Kelime karşılığı |
|---|---:|
| Tek sütun şekil veya tablo (3¼ inç) | **200** |
| Çift sütun şekil veya tablo (7 inç) | **450** |
| Büyük çift sütun tablo | **700** |

---

## 2. Şu anki durumun aritmetiği — sert

Elimizde **12 şekil ve 22 tablo** var. **34 nesne.**

| Senaryo | Nesnelerin yediği | 12 000'den metne kalan |
|---|---:|---:|
| Hepsi tek sütun (34 × 200) | **6 800** | **5 200** |
| Yarısı çift sütun (17×200 + 17×450) | **11 050** | **950** |

**Bu makale 5 200 kelimeye yazılamaz.** Yani sorun yalnızca gövdenin uzunluğu
değil: **nesne sayısı tek başına bütçenin yarısından fazlasını yiyor.**

Sonuç açık: **şekil ve tablo sayısı da düşecek**, metinle birlikte.

---

## 3. Önerilen bütçe

Üst sınıra (12 000) göre kurulmuş, ama editörün *"kısaltın"* deme hakkı saklı
olduğu için nefes payı bırakılmış.

| Kalem | Adet | Hesap | Kelime |
|---|---:|---|---:|
| **Metin** | — | — | **7 500** |
| Şekil, tek sütun | 3 | 3 × 200 | 600 |
| Şekil, çift sütun | 3 | 3 × 450 | 1 350 |
| Tablo, tek sütun | 5 | 5 × 200 | 1 000 |
| Tablo, çift sütun | 2 | 2 × 450 | 900 |
| Tablo, büyük çift sütun | 1 | 1 × 700 | 700 |
| | | | |
| **Toplam** | **6 şekil + 8 tablo** | | **12 050** |

**Yani hedef: ~7 500 kelime metin, 6 şekil, 8 tablo.**

Bugünkünden: metin 35 969 → 7 500 (**beşte bir**), şekil 12 → 6, tablo 22 → 8.

Daha rahat bir alternatif — metin 8 000, 5 şekil, 7 tablo → toplam ≈ 11 400.

**Hangi altı şekil ve hangi sekiz tablo kalacağı, v8 iskeleti kurulurken
karara bağlanacak.** Ölçüt tek: *bir nesne dört eksenden birine dair okuyucunun
inancını değiştirmiyorsa gövdede kalmaz.* Geri kalanı eke gider.

---

## 4. Şekil altyazıları — **11'i 12'si sınırı aşıyor**

> AIAA: *"Each figure must have a caption… **no more than 20-25 words**."*

Ölçüldü:

| Şekil | Kelime | | Şekil | Kelime |
|---|---:|---|---|---:|
| 1 | 49 | | 7 | 44 |
| 2 | 41 | | 8 | 47 |
| 3 | 38 | | 9 | 51 |
| 4 | 45 | | 10 | **70** |
| 5 | 40 | | 11 | 25 ✅ |
| 6 | 35 | | 12 | **82** |

**Yalnız Şekil 11 uyuyor.** Hepsi yeniden yazılacak. Altyazılarımız şu an
küçük birer paragraf — açıklamayı taşıyorlar. AIAA'da açıklama **metinde**
durur, altyazıda değil.

---

## 5. Çözünürlük — kural basit, ve bir şekil kalıyor

> AIAA: **çizgi resim için en az 600 dpi**, fotoğraf için 300 dpi.

Bizim şekillerimiz çizgi resim. Basılı genişliğe göre gereken piksel:

- **Tek sütun** (3¼ inç) → en az **1 950 px**
- **Çift sütun** (7 inç) → en az **4 200 px**

Ölçüldü:

- **Tek sütuna konursa:** 13 dosyanın 12'si geçiyor. **Yalnız
  `fig12b-climbing-entry.png` (1 860 px) kalıyor** — yeniden üretilecek.
- **Çift sütuna konursa:** yalnız `fig02-timeline.png` (4 200 px, tam sınırda)
  geçiyor. **Çift sütuna konacak her şekil yeniden üretilecek.**

Şekiller betikten üretildiği için bu mekanik bir iş: `figures/build/mkfig*.py`
içinde çıktı boyutu büyütülür. **Hangi şeklin hangi sütuna gideceği
kararlaştıktan sonra yapılacak** — önce karar, sonra üretim.

---

## 6. Öteki biçim şartları — kayda geçsin

- Şekil **3¼ × 3½ inçten büyükse müsvedde uzunluğuna eklenir.** Yani büyük
  şekil iki kere bedel ödetir: hem çift sütun sayılır hem sayfa büyütür.
- Benzer şekilleri **tek çok parçalı şekilde** toplamak yer kazandırır — ortak
  ölçek kullanılarak. Bizde Şekil 12 zaten (a)/(b); başkaları da birleştirilebilir.
- Altyazıda **şekil içindeki metin tekrarlanmaz.**
- Tablo: **sütunlar arasında dikey çizgi ve kenarlık yok**; gövdenin üstünde ve
  altında **çift çizgi**, sütun başlıklarının altında **tek çizgi**. Tablolar
  **resim olarak konmaz**, düzenlenebilir olmalı.
- Tablo dipnotları **a, b, c** ile, rakamla değil.
- Yan yatan tablo biçiminden kaçınılacak.

---

## 7. Bu bütçenin v8 planına söylediği

1. **Kesim hedefi metin için beşte bir, nesneler için yaklaşık üçte bir.**
   "Kısaltma" kelimesi bu ölçeği anlatmıyor; yeniden yazmaktan başka yol yok.
2. **Ek belge bu bütçenin dışında** — ama JoA *"the article… must be
   self-contained and stand on its own"* diyor ve hakem yalnız gövdeye bakıyor.
   Eke taşımak, gövdeyi eksik bırakmak değil.
3. **Altyazılar ayrı bir iş kalemi.** On bir tanesi yeniden yazılacak ve
   taşıdıkları açıklama metne taşınacak — silinmeyecek.
4. **Şekil üretimi karardan sonra.** Hangi şekil hangi sütunda, önce o.
