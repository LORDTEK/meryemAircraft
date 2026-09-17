# v8 — İçindekiler önerisi (benimki)

**Tur 29'da dört dış okuyucudan istenen şeyin bana ait cevabı.** Onlara gönderilen
metne **bilerek konmadı** — konsaydı onları çıpalardım, ki Tur 28'de yazarın
yakaladığı kusur tam olarak buydu. Bu dosya, dördünün cevabıyla birlikte, aynı
şartlarda paylaşılacak.

**Bütçe:** `v8-budget.md` — 12 000 kelimenin içinde kalmak üzere
**7 450 kelime metin + 6 şekil + 8 tablo.** Aşağıdaki dağılım bütçeyi **birebir**
kapatıyor: nesneler 4 550, metin 7 450, toplam 12 000.

**Kurucu ilke:** makalenin öznesi, **piste ihtiyaç duymama ile kanatla seyir
menzilini tek uçakta birleştiren yapıdır** — ve yeni olan, bu birleşmeye
*propulsor'ü yeniden yönlendiren hiçbir mekanizma olmadan* ulaşılmasıdır. Her bölüm
ya bu birleşmenin neden zor olduğunu ya da bu uçağın onun için ne ödediğini
anlatır. **Hiçbir hesap kendi başına anlatılmaz.**

---

## Bölümler

### 1. Introduction — 900 kelime · Şekil 1 · Tablo 1

İki aile, her biri yarıyı tutuyor: döner kanat piste ihtiyaç duymaz ve kötü seyreder;
sabit kanat iyi seyreder ve piste muhtaçtır. Yetmiş yıllık hibrit tarihi iki yarıyı
birden tutma denemesidir ve her denemenin bir bedeli olmuştur. Bu makale o bedeli
**mimari** sayar, muhasebesini kurar, ve bedeli ödemeden birleşmeyi sağlayan bir
yapılandırma sunar.

Bölüm, dört eksenli iddia tablosuyla **biter** — okuyucu burada bırakırsa bile
katkıyı almış olur.

- **Şekil 1** *(tek sütun)* — iki aile ve hiçbirinin tutmadığı köşe.
- **Tablo 1** *(çift sütun)* — dört eksen, dört ayrı rakip, dördünün durumu;
  **menzil iddiasının öteki hibritlere karşı reddedildiği dahil.**

### 2. The architectural tax — 1 200 kelime · Şekil 2 · Tablo 2

Üç para birimi: seyirde taşınan askı donanımının **kütlesi**, açıkta kalan
donanımın **sürüklemesi**, uçuşun yüzde ikisinde geçerli bir koşula göre
boyutlandırılmış **sürekli güç**. Taranan her çare birini azaltırken ötekini
artırır. Bedeli böyle yazmak **kaçış koşulunu** görünür kılar: tek donanım seti,
tek yönelim, askı tepesi bir tamponda.

- **Şekil 2** *(çift sütun)* — üç fatura ve aralarındaki devirler.
- **Tablo 2** *(büyük çift sütun)* — çareler ve her birinin hangi faturayı hangisine
  çevirdiği.

### 3. The framework against data it did not produce — 650 kelime · Tablo 3

Çerçevenin **çürütülebilir** öngörüsü: ağırlık cezası, verim kazancını aşar. İki dış
sınama:

- **NASA boyutlandırma seti** — turboşaft quadrotor L/D 4,9 / 3 678 lb; turbo-elektrik
  lift+cruise L/D 8,5 / 7 271 lb. Seyir verimi %70 daha iyi, neredeyse iki katı ağır.
  Öngörü tutuyor.
- **Bacchini rüzgâr tüneli** — standart quadplane'e karşı %34 sürükleme azalması;
  mekanizma 2 456 g'ın 200 g'ı; %30 azalma + %5 kütle uygulandığında menzil
  119 → 121 km, yani **%2'nin altında.** Fatura devri ölçülmüş ve fiyatlanmış.

**Bu bölüm makalenin en ucuz kazancıdır:** "yazarlar teoriyi kendi uçaklarına mı
uydurdu" sorusunu daha sorulmadan kapatır.

- **Tablo 3** *(tek sütun)* — iki dış sınama ve sonuçları.

### 4. The configuration — 1 300 kelime · Şekil 3 · Şekil 4 · Tablo 4

Kuyruğuna oturan kanat-gövde, 50 kg referans. Bütün itki **burundaki tek eşeksenli
karşıt dönüşlü çiftten**; o çift seyir propulsor'üdür ve baştan sona tasarım
noktasında çalışır. Kanat ucu çerçevelerindeki dört küçük çift **yalnız yönelim
momenti** üretir.

Kaçış koşulunun nasıl sağlandığı burada gösterilir. Sonra kumanda: yunuslama ve sapma
diferansiyel itkiden; **yatış eşeksenli ve tork dengeli çiftlerle üretilemez** ve alt
yüzeydeki değişken uzantılı şeritten gelir — uçaktaki tek hareketli aerodinamik yüzey,
ki burnu ΔC_m 0,005–0,032 kadar aşağı da yunuslatır.

- **Şekil 3** *(tek sütun)* — genel görünüş.
- **Şekil 4** *(çift sütun)* — moment kolları ve şerit; yatışın neden itkiden
  gelemediği görülsün.
- **Tablo 4** *(tek sütun)* — **mekanizma envanteri: olmayan ile olan.** Pivot yok,
  nasel eyleyicisi yok, değişken hatve göbeği yok, dönen kütleden gyroskopik moment
  yok; **olan:** motorlar ve şerit. **Makalenin katkısının tablosu budur.**

### 5. What the union costs — 1 650 kelime · Şekil 5 · Tablo 5 · Tablo 6

Üç fatura, bu uçak için tek tek.

- **Fatura 1, kütle** — lift+cruise'a karşı %32–36 üstünlük, üç sözleşmenin üçünde de.
- **Fatura 2, sürükleme** — kaçınıldığı varsayılan ama kaçınılmayan kalem: kendi tutum
  rotorlarının serbest dönme sürüklemesi, **ΔC_D0 = 0,0154**, temiz gövdenin **%62'si**.
  Bacchini'nin ölçtüğü karşılık **%65**. Ve serbestlik ile hizalanmanın ayrı durumlar
  olduğu: serbest bırakılan pervane hizalanmaz, döner.
- **Fatura 3, güç** — motor için kaçınılmış, elektrik yolu için kaçınılmamış.
  **3,8 kat** batarya özgül gücü; ölçülen oranda bütçe **%38 daha ağır** kapanıyor.
  Yazarın kuralı burada işler: sayı gövdede, tam çevrim S2'de.

- **Şekil 5** *(tek sütun)* — menzil–L/D.
- **Tablo 5** *(tek sütun)* — sürükleme defteri.
- **Tablo 6** *(tek sütun)* — kütle karşılaştırması.

### 6. Rankings belong to contracts, not to architectures — 850 kelime · Şekil 6 · Tablo 7

Makalenin **yöntemsel** sonucu, ve bence en çok atıf alacak yeri.

Eşit yakıt oranında lift+cruise **%24–45** önde; eşit kalkış kütlesinde kuyruk-oturan
**%29–43** önde; eşit yakıt kütlesinde **işaret aralığın içinde değişiyor.**
Dolayısıyla **sözleşmesi söylenmeden verilen bir sıralama sonuç değildir** — ve
bu yüzden öteki hibritlere karşı menzil üstünlüğü **iddia edilmiyor.** Reddetme
burada, gerekçesiyle birlikte durur.

- **Şekil 6** *(çift sütun)* — sıralamanın sözleşmeyle tersine dönüşü.
- **Tablo 7** *(çift sütun)* — üç sözleşme, üç sıralama.

### 7. What is not closed — 600 kelime · Tablo 8

Hiçbiri yumuşatılmadan, her biri kapatacak şeyle birlikte.

Geçiş yunuslama momenti (en büyüğü, hiçbir yöntem güvenilir öngörmüyor) · yatış
otoritesi ΔC_L ≈ 0,12 ödünç · serbest dönme sürüklemesi hesaplanmış, ölçülmemiş ·
batarya açığı · yön kararlılığı 39 mm fairing'e bağlı.

- **Tablo 8** *(tek sütun)* — açık maddeler ve her birini neyin kapatacağı.

### 8. Conclusions — 300 kelime

Birleşme, mekanizma sayımı, sözleşme sonucu, açık maddeler. **Kaynak atfı yok** —
AIAA açıkça yasaklıyor.

---

## Bütçe denetimi

| | Adet | Birim | Kelime |
|---|---:|---:|---:|
| Şekil, tek sütun (1, 3, 5) | 3 | 200 | 600 |
| Şekil, çift sütun (2, 4, 6) | 3 | 450 | 1 350 |
| Tablo, tek sütun (3, 4, 5, 6, 8) | 5 | 200 | 1 000 |
| Tablo, çift sütun (1, 7) | 2 | 450 | 900 |
| Tablo, büyük çift sütun (2) | 1 | 700 | 700 |
| **Nesneler** | **14** | | **4 550** |
| **Metin** | | | **7 450** |
| **TOPLAM** | | | **12 000** |

---

## Neyi düşürdüm, ve neden

**22 tablodan 8'e, 12 şekilden 6'ya.** Ölçüt tekti: *bir nesne dört eksenden birine
dair okuyucunun inancını değiştirmiyorsa gövdede kalmaz.*

| Gövdeden çıkan | Nereye |
|---|---|
| RANS ağ/duvar/kapatma/başlangıç matrisi | S1 — gövdede yalnız yakınsamış K_L = 0,796 ve kaba ağın anlaşmayı olduğundan iyi gösterdiği cümlesi |
| Bileşen bileşen kütle kurulumu | S2 — gövdede tek kütle karşılaştırma tablosu |
| Kontrol eksenlerinin tam türetimi | S3 |
| Dönme otoritesi ve denge süpürmeleri | S4 |
| 1000 kg ağır hat — ayrı bir paralel makale gibi duruyor | S6 — gövdede tek ölçek paragrafı |
| Geçiş benzetiminin altı alt bölümü | S4 — gövdede iki paragraf: dönme, modellenmemiş iniş, tıkalı C_m |
| Yetmiş yıllık tarihçe — şu an bir kitap bölümü | Giriş'te bir buçuk paragraf; görev-çevrimi uyuşmazlığını kurmaya yeter |
| Pervane-element türetiminin adımları | S6 — gövdede sonuç: 0,0154 ve ne anlama geldiği |

**Gövdede tutulanlar**, hiçbiri pazarlık konusu değil: kaçış koşulu · dört eksen
tablosu · tilt'e karşı mekanizma sayımı (şeritle **aynı nefeste**) · NASA sınaması ·
Bacchini karşılaştırması · 0,0154 ve temiz gövdenin %62'si oluşu · üç sözleşmenin
tersine dönüşü · açık maddeler.

---

## Kendi önerim hakkında bildiğim zayıflıklar

Dördü de bunu görsün diye yazıyorum.

1. **Bölüm 5, 1 650 kelimeyle üç faturayı da anlatmak zorunda** ve bu dar. Sıkışırsa
   Fatura 1 kısalır, çünkü kütle üstünlüğü tek tabloyla anlatılabilecek en kolay
   kalem. **Fatura 2 kısalmaz** — makalenin en büyük sayısı ve tek dış ölçüm teması
   orada.
2. **Bölüm 3'ü ayrı bir bölüm yapmak tartışmalı.** Bölüm 2'nin sonuna
   sıkıştırılabilirdi. Ayrı tuttum çünkü *"bu teori kendi uçağına mı uyduruldu"*
   itirazının cevabı kendi başlığını hak ediyor; ama bu bir tercih, zorunluluk değil.
3. **Şekil 3'ün tek sütuna sığması şüpheli.** Genel görünüş 3¼ inçte okunmayabilir;
   çift sütuna çıkarsa bütçeden 250 kelime daha gider ve metin 7 200'e iner.
4. **Design Forum / Full-Length kararı bu iskeleti değiştirmiyor** — ikisi de
   10–12 bin kelime ve 100–200 kelimelik özet istiyor. Karar hakemlik meselesi,
   yapı meselesi değil.
