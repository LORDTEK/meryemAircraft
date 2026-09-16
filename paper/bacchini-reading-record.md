# Bacchini tezi — birinci elden okuma kaydı

**Kaynak:** Bacchini, A. *Electric VTOL preliminary design and wind tunnel tests.*
Doktora tezi, Politecnico di Torino, Havacılık Mühendisliği, 32. devre, Mart 2020.
Danışmanlar: Giulio Romeo, Enrico Cestino. 196 sayfa.
Depoda: `references/conv_doctoral_dissertation_alessandro_bacchini-5_260916_203618.pdf`

**Okunan:** Bölüm 5 tamamı (Rüzgâr tüneli deneyleri, s. 120–169), §1.4, §1.5.
Aşağıdaki her sayı tezin kendi sayfasından alındı; hiçbiri özet ya da ikincil
kaynaktan değil.

---

## 1. ÖNCE ŞUNU ÇÖZELİM: 2021 dergi makalesi bu bölümün ta kendisi

Tezin §1.5.1 yayın listesi:

> Alessandro Bacchini, Enrico Cestino, Dries Verstraete, and Benjamin Van Magill.
> **Impact of takeoff propeller drag on the performance of lift+cruise eVTOL
> aircraft. (Under submission)**

Yani **Bölüm 5, AST 109:106429 (2021) olarak yayımlanan çalışmanın tez hâlidir.**
Aradığımız ölçümler elimizde, birinci elden.

⚠️ **Yazar adlarında uyuşmazlık var, atıf yazılmadan çözülecek.** Tez
*"Verstraete, and Benjamin **Van Magill**"* diyor; bizim `revision-list.md`
*"Magill, Verstraete"* yazmış. Soyadı **Van Magill** olabilir ve sıra farklı
olabilir. AIAA kaynakçada *"et al." kullanılmaz, bütün yazarlar tam yazılır*
diyor — yayımlanmış künye teyit edilmeden atıf yazılmaz.

---

## 2. Deney düzeneği

**Tünel:** Sydney Üniversitesi 7 ft × 5 ft alçak hızlı rüzgâr tüneli, 1–38 m/s.
**Ölçüm:** ATI mini 45 altı bileşenli yük hücresi (10 N·m / 290 N'a kadar),
2000 Hz'de 2 saniye örnekleme. Hücre önce sıfırlanıyor, sonra hücum açısı
süpürmesiyle dara alınıyor.

**Dört model:**

| Model | Ne |
|---|---|
| **Mini Talon 1** | Temiz — askı pervanesi yok. Gövdesi delikli olanla **aynı boyda**, yani karşılaştırma dürüst |
| **Mini Talon 2** | Geri çekme sistemli. Kirişler elle açılıp kapanıyor, **0° / 30° / 60° / 90°**'de kilitleniyor. Eyleyici yok |
| **Mini Talon 3** | **Standart quadplane** — kanatlara gövdeye paralel iki adet 80 cm alüminyum çubuk, üstünde VTOL motorları |
| **SkyProwler** | Krossblade'in gövdesi + 3B basılmış kanat/kuyruk |

**Referans (Tablo 34):** 17,5 m/s · Re = 280 000 · kütle 2,45 kg · S = 0,314 m² ·
açıklık 1,28 m · veter 0,245 m · **seyir C_L = 0,4**

⚠️ **Tezin kendi sınırı:** SkyProwler modelinin kuyruğu *"doesn't have an
aerodynamic shape, its thickness is constant"*. O modelin mutlak L/D değerleri
bu yüzden az yük taşır.

---

## 3. Ölçülen sayılar

### 3.1 Sürükleme katsayıları, C_L = 0,4'te (Şekil 134 ve 147–150 polarlarından)

| Yapılandırma | C_D |
|---|---:|
| Mini Talon 1, temiz | **0,029** |
| Mini Talon 2, pervaneler çekilmiş | **0,029** *(temizle aynı)* |
| **Mini Talon 3, pervaneler akışa paralel — standart quadplane** | **0,044** |
| Mini Talon 2, pervaneler 90° açıkta | **0,079** |
| SkyProwler, çekilmiş (20 m/s) | 0,062 |
| SkyProwler, açık (20 m/s) | 0,088 |

### 3.2 Sürükleme azaltma (Tablo 35)

| Kıyas | Azalma |
|---|---:|
| Mini Talon 2, açık → çekilmiş | 63 % |
| **Mini Talon 3 → Mini Talon 2 çekilmiş** | **34 %** |
| SkyProwler, açık → çekilmiş | 30 % |

**Yazarın kendi uyarısı, birebir:** *"The drag reduction measured above is not
enough because the Mini Talon 2 with propellers retracted must not be compared
to itself with propellers open but with the standard quadplane represented by
Mini Talon 3."* — Yani **%63 yanlış kıyastır, doğru olan %34'tür.** Bu dürüstlük
anılmaya değer.

### 3.3 L/D merdiveni — bizim Tablo 1'imiz, doğrulandı

**Mini Talon 3 (standart quadplane) grubu:**

| Yapılandırma | Azami L/D |
|---|---:|
| Motorsuz (≈ temiz uçak) | **≈ 17** |
| Motorlu, pervanesiz | ≈ 13 |
| Motorlu, pervaneler **akışa paralel** | **≈ 13** |
| Motorlu, pervaneler **akışa dik** | **≈ 9** |

✅ **Makalemizin Tablo 1'indeki 17 / 13 / 9 merdiveni doğrudur.**

Ayrı bir grup (Mini Talon 1 ve 2): temiz ve çekilmiş **16–18**, 90° açık **6–9**.

### 3.4 Ceza nerede — birebir alıntı

> *"The difference between propellers parallel to the airflow and without
> propellers is **modest**. The drag produced by the **motors is significant**."*

Ceza esas olarak **motorlarda ve taşıyıcı kirişlerde**, pervane kanadında değil.
Ve yazar ekliyor: kirişlerin ürettiği sürükleme *"limited"*.

---

## 4. 🎯 EN ÖNEMLİ BULGU — tezin tavsiyesi ile bizim hesabımız çelişiyor

Tez, ölçümden şu sonucu çıkarıyor (birebir):

> *"Propellers perpendicular to the airflow generate much more drag than
> propellers parallel to the airflow. This is an important indication for standard
> quadplanes, **their takeoff propellers must be free to rotate and to align to
> the airflow.**"*

**Ama tez, serbest dönen bir pervane ölçmedi.** Ölçtüğü şey **sabitlenmiş**
pervanelerdi — dik ve paralel, iki ayrı kilitli konumda. *"Serbest dönmek"* ile
*"akışa hizalanmak"* **aynı durum değildir**, ve birincisi ikincisini üretmez:

- **Serbest bırakılan pervane hizalanıp durmaz — döner.** Bizim §3.3'ümüz sıfır
  şaft torkunda 25 000 rpm hesaplıyor ve diski süpürüyor.
- Bizim hesabımıza göre serbest dönme **ΔC_D0 = 0,0154**; kenarı öne kilitlenmiş
  hâl **0,0008**. **Yirmi kat fark.**
- Yani *"hizalanmış"* hâli elde etmek için pervaneyi **tutan bir indeksleme
  mekanizması** gerekir — ki o bir kütle ve bir arıza kipidir. **Yine Fatura 1.**

**Bu, bizim katkımızın tam olarak durduğu yer.** Tezin tavsiyesi ölçüme dayanıyor
ama ölçülmemiş bir duruma genelleniyor; bizim hesabımız o genellemeyi
sınırlandırıyor. Ve §3.3'ün kendi itirafı — *"indeksleme mekanizmasının maliyeti
ile yirmi kat sürükleme tasarrufu arasındaki ticaret bu makalede hiçbir yerde
yapılmamıştır"* — artık dışarıdan bir sayıyla beslenebilir (§5).

---

## 5. Fatura 2 → Fatura 1 dönüşümü, ölçülmüş ve modellenmiş

### 5.1 Mekanizmanın kütlesi, model ölçeğinde (Tablo 33)

Mini Talon VTOL kütle bütçesi: toplam **2 456 g**, bunun
**geri çekme mekanizmaları 200 g** = **%8,1**.

### 5.2 Kitty Hawk Cora'ya uygulanması (§5.4.1)

Cora verisi (Tablo 36): C_D0 = 0,0438 · k = 0,0294 · S = 10 m² · m = 1 224 kg ·
η = 0,75 · E* = 157 Wh/kg · batarya kütle oranı %33 · seyir enerji payı %60.

**Ve kritik olan denklem (81):** geri çekme sisteminin kütlesi **doğrudan batarya
kütlesinden düşülüyor.** Yazarın gerekçesi birebir: *"the battery is the only part
of the eVTOL that can be changed without affecting everything else."*

**Sonuç: %30 sürükleme azalması + %5 sistem kütlesi →**

| | |
|---|---|
| Azami menzil | 119 km → **121 km** *(+%1,7)* |
| Azami menzil hızı | **+5 m/s** |
| 80 km'lik görev | **10 m/s daha hızlı** |

**Bu, çerçevemizin söylediği şeyin ölçülmüş ve hesaplanmış hâlidir:** sürükleme
faturası kütle faturasına çevrildi, takas açıkça modellendi, ve **menzilde net
kazanç neredeyse sıfır.** Yazarın kendi vurgusu da menzilde değil **hızda** —
çünkü menzil kazancı *"slightly"*.

### 5.3 Gözetleme dronları (§5.4.2)

Dayanıklılık için kazanç **daha da küçük**: azami uçuş süresi düşük hızda,
C_L^1.5/C_D azamisinde; sürükleme azaltması orada daha az etkili.

---

## 6. ⚠️ ÖLÇEKLEME — tezle bizim aramızda çözülmesi gereken bir gerilim

Tez §5.4.3, model ölçeğindeki azalmayı tam ölçeğe taşımayı **muhafazakâr**
sayıyor, şu gerekçeyle: aynı askı başarımını korumak için disk alanı geometrik
büyütmeden **daha hızlı** büyümek zorunda (kütle ~ L³, disk alanı ~ L²). Daha
büyük disk alanı → **daha çok VTOL sürüklemesi** → geri çekmenin kazancı tam
ölçekte **daha büyük**.

**Bizim §3.9'umuz ters yöne gidiyor:** serbest dönme yükü 50 kg'da 0,0154'ten
1000 kg'da 0,0051'e **düşüyor.**

İkisi de aynı fiziği söylüyor olabilir — bizim Şekil 10 altyazımız da *"disk
yüklemesini sabit tutmak pervaneyi gövdeden hızlı büyütüyor"* diyor — ama
sonuçlar zıt yönde. Aradaki fark muhtemelen diskin **kendi sürükleme
katsayısının** Reynolds ve uç Mach ile değişmesinden geliyor.

**Bu, yazılmadan önce §3.8 ve §3.9 açılıp denetlenecek.** İki kaynağı yan yana
koyan bir hakem bunu sorar. *(CLAUDE.md §0.2)*

---

## 7. Yan bulgu: ikinci bir dış kaynak

Tez §5.1, geri çekme üzerine **başka bir rüzgâr tüneli çalışmasına** işaret
ediyor: **Stahl, Rößler, Hornung** [111] — iki kanatlı rotoru bir yuvaya çeken
mekanizma; küçük insansız hava araçları için seyir dayanıklılığında **%1–6**,
yolcu eVTOL'leri için **%10** artış tahmin ediyorlar. Bizde yok. Bulunursa
Fatura 2 tartışmasını güçlendirir.

---

## 8. Okumanın sonucu — ne değişti

1. ✅ **Tablo 1'in 17/13/9 merdiveni doğrulandı.**
2. ✅ **%34 ve %30 sayıları doğrulandı**, ve %63'ün yazarın kendisince yanlış
   kıyas ilan edildiği doğrulandı.
3. ❌ **Elimizdeki "%38 sürükleme / %13 menzil" sayıları tezde YOK.** Tezin
   sayıları %34 ve +%1,7. O iki sayı arama motoru özetinden gelmişti ve
   **makaleye girmezler.**
4. 🎯 **Yeni ve bize ait bir nokta doğdu:** tezin *"serbest dönsün ve hizalansın"*
   tavsiyesi, sabit pervane ölçümünden serbest dönen duruma yapılmış bir
   genellemedir; bizim hesabımız o genellemeyi sınırlandırır.
5. 🎯 **Fatura dönüşümü dışarıdan bir sayıyla beslendi:** mekanizma %5–8 kütle,
   karşılığında %30 sürükleme, net menzil kazancı +%1,7.
6. ⚠️ **Ölçekleme gerilimi açık madde.**
7. ⚠️ **Yazar adları teyit edilecek** (Van Magill?).
