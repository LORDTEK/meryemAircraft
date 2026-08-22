# meryemAircraft — Tasarım Künyesi

**Durum:** Taslak 01 · Anlatım aşaması tamamlandı, hesap aşaması başlamadı
**Kapsam:** Bu belge projenin tek doğruluk kaynağıdır. Makale, patent tarifnamesi,
görsel, sunum ve video buradan türetilir.
**Gizlilik:** Yayımlanmamıştır. Patent başvurusu öncesi kamuya açıklanmamalıdır.

---

## 1. Tek cümlelik tanım

Pist gerektirmeden dikey kalkıp inen, seyir uçuşunu gövdesinin tamamıyla taşıyıcı
kanat olarak yapan, tüm kumandasını hareketli yüzey kullanmadan pervanelerden alan,
pervaneli ve insansız bir yük taşıyıcısı.

## 2. Çözülen problem

Sabit kanat ve döner kanat, iki ayrı sınırın iki ayrı tarafında durur:

| | Üstünlük | Sınır |
|---|---|---|
| Sabit kanat | Menzil, yük verimliliği | Pist / altyapı zorunluluğu |
| Döner kanat | Dikey kalkış, havada asılı kalma | Menzilde verimsizlik |

Bugüne kadarki birleştirme denemeleri (hibrit VTOL) **taktik kullanımı seyir
veriminden keserek** satın almıştır. Bu kesinti mimariden doğar, uygulama
kalitesinden değil.

**Çekirdek iddia:** Bu tasarım o kesintiyi ödemez.

## 3. Yeniliğin çekirdeği

Unsurların tek tek ataları vardır; yenilik **bileşimdedir**:

1. Kuyruğa oturan, değişken ok açılı **kanat-gövde** planformu
2. Burunda **tek ana itki kaynağı** (koaksiyel karşıt dönüşlü çift)
3. Kanat uçlarındaki sabit iskeletlerde, **yalnız kumanda görevli** dört çift
4. **Hiç kumanda yüzeyi yok** — elevon yok, rudder yok
5. Yuvarlanma için gövde altında, **ana pervane izinde** çalışan seviye kontrollü kanatçık
6. Uç iskeletlerinin aynı zamanda **iniş yapısı** olması
7. **Hareketli parça neredeyse yok** — tilt yok, değişken hatve yok

---

## 4. Kısıtlar ve ilkeler

| Kod | Kısıt |
|---|---|
| K1 | Ses altı, mütevazı seyir hızı |
| K2 | Jet yok; itki pervaneli |
| K3 | Yüksek irtifa gereksinimi yok |
| N14 | **Sadelik birincil tasarım kısıtıdır** |
| N47 | Bir sorun ancak **her yük için** varsa çekirdeğe aittir; yoksa eke gider |
| N49 | Sınırlayıcı **kütledir**, hacim değil |
| N51 | Başarı ölçütü: **faydalı yük oranı** (m_yük / MTOW) |

---

## 5. Konfigürasyon

### 5.1 Planform ve kesit

| Kod | Karar |
|---|---|
| N3 | Kanat-gövde (blended wing body) mimarisi |
| N5 | Açıklık, yapısal sınıra kadar uzun (indüklenmiş sürükleme ∝ 1/b²) |
| N6 | Merkez veteri > uç veteri (sivrilme) |
| N19 | Tüm gövde boyunca **taşıyıcı, kamburlu** kesit; art kısımda **refleks var ve kalır**. Trim pasiftir, geometriden gelir |
| N20 | Kalınlık oranı merkezden uca azalır (yakl. %19 → %9; literatür bandı merkez %15,2–19,4, %25 yarı-açıklıkta %8,3–11,8) |
| N22 | **Değişken ok açısı**: burunda 40°, en arkada 20°. Hücum ve firar kenarları teorik olarak birleşir; yapısal gereklilik nerede derse orada kırpılır |
| N23 | Ok açısı / kalınlık / veter dağılımları **tek bir bütün** olarak ele alınır |
| N24 | N22'nin asıl işlevi: **düşük hızda uç tutukluğu ve yunuslama-yukarı önlenmesi**. N8 ile doğrudan bağlantılıdır |
| N7 | Ok açısı iki iş görür: aerodinamik verim + kuyruksuz yunuslama moment kolu |
| N27 | **Kırpma, planformun baskın kaldıracıdır** |

> **Tarihsel dayanak:** Hilal kanat (Handley Page Victor, Lachmann/Lee) aynı üçlü
> dağılımı kullanmıştır: kökten uca 48,5° → 37,5° → 26,75°, veter ve kalınlık
> birlikte azalarak. Gerekçesi transonikti; bizimki uç tutukluğudur.
> **Açık iş:** hilal kanadın neden yaygınlaşmadığı araştırılacak (D1).

### 5.2 İtki

| Kod | Karar |
|---|---|
| N11 | Her pervane bir **koaksiyel karşıt dönüşlü çifttir**. Tek gerekçe: **ters torkun elimine edilmesi** |
| N12 | Çift içinde **hız farkı yok**; değişken mekanik unsur yok |
| N13 | Çiftteki iki pervanenin **burulma dağılımları farklıdır** (sabit). Alt rotor daralmış izde çalıştığı için bu, tork dengesinin şartıdır |
| N16 | Hız farkı yasağı **çift içindedir**; farklı çiftler farklı devirde dönebilir |
| N18 | Çift içinde eşit devir. Akustik ve titreşim sabit-geometri kaldıraçlarıyla yönetilir: eksenel aralık, kanat sayısı farkı, çap farkı, burulma dağılımı |
| N29 | Ana pervane disk çapı **4,0 m** (referans) |
| N32 | Ön dikmelerin üst ve alt uçlarında **dört çift daha**. Toplam **beş çift** |
| N17 | Enerji türü açık: elektrik veya içten yanmalı. İçten yanmalıysa **her çift için bir motor** |
| N36 | Koaksiyel çift **net açısal momentumu da siler** → geçişte jiroskopik moment doğmaz. Kuyruğa oturanların klasik sorunu bu yolla düşer |
| N15 | ⚠️ Sabit geometri, tam tork dengesini **tek bir çalışma noktasında** verir |

### 5.3 Yapı

| Kod | Karar |
|---|---|
| N28 | Kanat uçlarında dikey iskelet: uç veteri boyunca çubuk; iki ucunda yukarı ve aşağı dikmeler (her yön ≈ 1 veter); **arka dikmenin** uçlarından geriye çubuğun ¼'ü kadar çıkıntılar |
| N30 | Kök firar kenarı ortasından geriye **tek orta omurga**; arka ucu uç çıkıntılarıyla aynı düzlemde biter |
| N31 | Araç **kuyruğa oturur.** Beş nokta temas: iki uçta üst ve alt çıkıntılar + orta omurga. Temas düzlemi gövde eksenine diktir |

### 5.4 Kumanda

| Kod | Karar |
|---|---|
| N8 | **Elevon yok, rudder yok** |
| N10 | Yunuslama, yönelme, hover, kalkış, iniş ve seyir: hepsinin kökeni pervanelerdir. Kanat-gövde yalnız seyirde katkı sunar |
| N33 | Ana pervane = **itki**. Çevre pervaneleri = **yalnız kumanda**; seyirde itkiye katkı vermez |
| N43 | Yuvarlanma: gövde **alt yüzeyinde**, merkeze yakın başlayıp 45° ile arkaya-dışa giden, **seviye kontrollü** kanatçık. Kanat uçlarına ulaşmaz — **ana pervane izinde** kalır. Açıldığında ≈2 cm → 10 cm. **Tasarımın ilk hareketli parçası** |

> **İz dinamik basıncı:** q_iz = T/A — yani tam olarak disk yüklemesi.
> Kanatçık bu sayede sıfır hava hızında da çalışır.

---

## 6. Uçuş profili

```
1. DURUŞ      Beş nokta üzerinde dik, burun yukarı
2. KALKIŞ     Ana pervane; çevre pervaneleri yalnız küçük düzeltmeler
3. GEÇİŞ      Üst çevre çifti → hızlı yunuslama → yatay
4. SEYİR      Ana itki + gövdenin tamamı taşıyıcı kanat + kanatçıkla yuvarlanma
5. İNİŞ       Alt çevre çifti → dikey yönelim → beş nokta üzerine oturuş
```

| Kod | Karar |
|---|---|
| N34 | Geçiş: üst çift → yataya meyil. İniş: alt çift → dikeye dönüş |
| N37 | Geçiş **hover'dan** başlar; başlangıçta aerodinamik direnç yoktur (q → 0). Kritik bölge **orta yaydır**: yüksek hücum açısı + artan dinamik basınç |
| N41 | Geçiş **hızlı yunuslama** ile yapılır. İrtifa kaybı ∝ t_r², gereken kumanda itkisi ∝ 1/t_r². Optimum, uç pervanelerini boyutlandırır |
| N42 | Yüksek eğimde a_yatay = g·tanθ (45°→1,0 g, 60°→1,73 g, 70°→2,75 g). İtki tekilliğine ulaşılamaz; kanat birkaç saniyede devralır |
| N38 | İrtifayı korumak için T = W/cosθ. 60°'den sonra kanadın devralması şarttır |
| N48 | **Boyutlandırma koşulu: tam yüklü hover.** Ana pervaneyi ve motor tipini bu belirler |

---

## 7. Görev ve konumlandırma

| Kod | Karar |
|---|---|
| N45 | Görev **belirsiz bırakılır.** Araç bir faydalı yük taşıyıcısıdır; yangın söndürme, lojistik, afet, tıbbi sevkiyat birer örnektir |
| N46 | Sıvı yükün duruşla kayması, çalkalanma ve hızlı boşaltma **sıvı ekine** taşındı — çekirdek değil |
| N52 | Kütle büyümesi kendini besler: MTOW = m_yük / (1 − f_boş − f_enerji). Askı cezası W^1.5 |
| N53 | **Ölçek, tasarımın koz kartıdır.** Klasik sabit kanadın ölçek tavanı altyapıdır (pist, taksi yolu, hangar); multirotorunki menzildir. Bu mimaride ikisi de yoktur |
| N54 | Ölçekleme sınırı **askı gücündedir**: P_gerekli/P_mevcut ∝ L^0,5 |
| N55 | Kaçış: **sabit disk yüklemesi.** Disk alanı ağırlıkla (L³) büyütülürse ölçekleme bedavadır. Mimaride çift eklemek serbest olduğu için bu mümkündür |
| N56 | Konumlandırma: rakip diğer hava araçları değil, **havalimanı altyapısıdır** |

---

## 8. Açık sorular

| Kod | Soru | Neden tıkıyor |
|---|---|---|
| **A-KÜTLE** | MTOW ve faydalı yük oranı nedir? | Disk yüklemesi, askı gücü, yapı, enerji — hepsi buna bağlı |
| **A-ENERJİ** | Elektrik mi, içten yanmalı mı? | Tam yüklü hover, bataryanın en zorlandığı durum. Mimariyi değiştirir |
| N40 | Hover'da istikamet otoritesi yeterli mi? | N43 açığı sıfırdan "küçük ama gerçek"e taşıdı; yeterlilik sayıyla belirlenecek |
| N44 | ⚠️ N1 ile N43 birbirini törpüler | Disk büyüdükçe iz zayıflar (q = T/A) |
| N15 | Tam tork dengesi hangi noktada kurulacak? | Hover mu, seyir mi |
| N4 | Ok açısı değerleri | 20–40° bandı **transonik nakliye** bağlamından geldi; bizim rejimimize göre yeniden türetilecek |
| D1 | Hilal kanat neden yaygınlaşmadı? | Victor'u dayanak göstermeden önce bilinmeli |
| N6 | Sivrilme dağılımının nihai biçimi | Sonraya bırakıldı |

---

## 9. Prior art — ön tarama

> Bu bölümün ayrıntısı **kamuya açık kayıttan çıkarılmıştır.** İçeriği, kendi başvurumuzun istemlerine ilişkin iç değerlendirmemizdi. Kayıt yazarlarda durmaktadır.

## 10. Strateji

| Kod | Karar |
|---|---|
| N57 | Sıra: **prior-art taraması → başvuru ve makale birlikte yazılır → başvuru → yayım** |
| — | Kural: **makale ⊆ başvuru.** Makale, başvuruda anlatılandan fazlasını anlatmaz |
| N50 | Patent istemi **konfigürasyonu** korumalı, görevi değil |
| N58 | Hedef **ürün değil mimaridir.** Rakip şirket ismi üzerinden kurgu yapılmaz; "yendik" cümlesi metinde geçmez |
| N59 | Referans tasarım bir **varlık kanıtıdır**, rakiplerin bandına bilerek yerleştirilir. Ölçek, sessiz üstünlük olarak sonda gösterilir |
| N60 | Karşılaştırma grafiği ayrı sayfa; referans tasarımın sayıları çıkınca kurulur |

**Ödemesiz süre haritası** (yayımdan önce başvuru şart):

| Ülke / bölge | Kendi yayımına tolerans |
|---|---|
| Türkiye | 12 ay |
| ABD | 12 ay |
| **Avrupa (EPC)** | **Yok** |
| Japonya | 12 ay (şartlı) |
| Çin | 6 ay (dar) |

⚠️ Millî güvenlik bakımından önem taşıyan buluşlar için TÜRKPATENT başvuruyu MSB'ye
yönlendirebilir. Vekile ilk sorulacaklardan biri budur.

---

## 11. Referans model — 3B parametreler

Etkileşimli model: değişken ok açılı kanat-gövde + beş pervane çifti + uç iskeletleri
+ orta omurga + yuvarlanma kanatçığı.

```
GOVDE05
kok=4.0  hk0=45.0  hk1=35.0  fk=25.0  kirp=50
tc0=25.0 tc1=12.0  kamb=6.0  refl=3.0
pcap=4.0 parl=8.0  pkf=4  pkr=3  ucap=0.5
dikme=100  cikinti=5  kalinlik=4.0
kbas=15  kboy=55  kh0=2  kh1=10  kac=100

→ b=10,63 m · S=29,02 m² · AR=3,89 · A_disk(ana)=12,57 m²
```

**Bu değerler görsel çalışma taslağıdır, tasarım kararı değildir.** Sayılar, kütle ve
enerji kararı verildikten sonra kendi uçuş rejimimize göre yeniden türetilecektir.

---

## 12. Sözlük

| Terim | Tanım |
|---|---|
| Ok açısı | Bu belgede **hücum kenarından** ölçülür |
| Kırpma | Hücum ve firar kenarlarının teorik birleşme açıklığının yüzdesi |
| Kalınlık / kambur / refleks | Yerel vetere oranla |
| Çift | Koaksiyel karşıt dönüşlü iki pervaneden oluşan tek organ |
| Çevre pervaneleri | Kanat uçlarındaki dört çift (yalnız kumanda) |

---

*Bu belge konuşma kaydından derlenmiştir. Her madde, karara varıldığı andaki
gerekçesiyle birlikte kayıtlıdır.*
