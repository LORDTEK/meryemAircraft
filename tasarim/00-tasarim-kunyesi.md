# meryemAircraft — Tasarım Künyesi

**Durum:** Taslak 04 · Anlatım tamamlandı · **Boyutlandırma yapıldı** · Referans geometri sabit
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
| N70 | **En-boy oranı = 6.** Sınırlayanlar: yapı (kök eğilme momenti), uç tutukluğu (N24), düşük Reynolds. Aynı AR ağır hatta da uygulanır |

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
| N15 | Sabit geometri, tam tork dengesini tek bir noktada verir → **N76: o nokta SEYİRDİR** |
| N76 | **Tork dengesinin tasarım noktası seyirdir.** Hover kısa ve taktiktir (yalnız pist gereksinimini kaldırır); seyir uzun ve stratejiktir. Kusursuzluk seyirde aranır. Sonuç: hover'da küçük bir artık tork kalır, N43 kanatçığı bunu trimler |
| N63 | İtki mimarisi: **seri hibrit.** İçten yanmalı motor **enerji kaynağıdır**, doğrudan tahrik değil. Yakıt → motor → jeneratör → elektrikli rotorlar. Karşıt dönüş dişli kutusu hiç doğmaz (XB-35 riski) |
| N64 | Motor **seyir gücüne** göre boyutlandırılır; hover tepesi küçük pil tamponundan karşılanır (≈%3 MTOW, her iki hatta da) |
| N65 | Her iki hat **aynı mimariyi** kullanır. Farklı mimari, ölçek tezini çürütür |
| N69 | Kumanda pervaneleri hover gücünün **%15'inden azını** ister. Kumanda, mimarinin en ucuz bileşeni |

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
| N62 | Yük oranı boyutla büyüyor (%4 → %25 mertebesi); sabit maliyetler küçülmediği için. N53'ün veri desteği |
| N77 | Ana disk çapı **1,20 m** (1,34'ten). Bedeli: askı gücü +%12, disk yüklemesi +%25. Seyir önceliği gereği kabul edildi. Ağır hat da aynı çizgide **5,40 m**'ye çekildi |
| N75 | Yuvarlanma kanatçığı: **boy %120 kök veter, yükseklik 2→6 cm.** Gücü boydan gelir. İç kısmı pervane izinde (hover), dış kısmı dışında (seyir) |
| N73 | **Rakipten fazla yük taşımak gerekmiyor.** Benzer yükü daha uzağa taşımak, mimarinin üstünlüğünü daha temiz ispatlar — ölçüm tartışmasına da kapalıdır |

---

## 8. Açık sorular

| Kod | Soru | Neden tıkıyor |
|---|---|---|
| ~~A-KÜTLE~~ | **KAPANDI** → N66: 50 kg / 1000 kg | |
| ~~A-ENERJİ~~ | **KAPANDI** → N63: seri hibrit | |
| ~~A-KANATÇIK~~ | **KAPANDI** → N75 | |
| ~~N15~~ | **KAPANDI** → N76: tasarım noktası seyir | |
| N4 | Ok açıları transonik literatürden ödünç | Tasarımcı gözle onayladı; makalede **"seçilmiştir"** diye sunulacak, "türetilmiştir" diye değil |
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
| N61 | Referans tasarım **iki boyutta**: hafif hattın en hafifi (50 kg), ağır hattın en ağırı (1000 kg). Ölçek oranı **20:1** |

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

## 11. Referans tasarım — sayılar

### 11.1 İki tasarım noktası (N66)

| | **Hafif hat** | **Ağır hat** |
|---|---:|---:|
| MTOW | **50 kg** | **1000 kg** |
| Ana disk çapı | **1,20 m** | **5,40 m** |
| Disk yüklemesi | 44,2 kg/m² | 43,7 kg/m² |
| Askı gücü | 10,9 kW | 216,2 kW |
| Seyir gücü | 1,8 kW | 38,8 kW |
| Motor (seyre göre) | 2,6 kW | 54,3 kW |
| Pil tamponu | 1,8 kg (%3,6) | 40 kg (%4,0) |
| Kök veter | 0,97 m | 3,25 m |
| Açıklık | 3,45 m | 11,55 m |
| Kanat alanı | 1,98 m² | 22,24 m² |
| Uç pervanesi | 0,20 m | 0,67 m |
| Dikme boyu | 0,71 m | 2,38 m |
| **Geçiş süresi** | **2 s** | **4 s** |
| **Ölçek** | **1×** | **20×** (uzunlukta 3,35×) |

İki nokta da **aynı disk yüklemesi çizgisinde** — N55'in gereği. Pil oranları da eşit.
Mimarinin iki uçta aynı oranlarla çalıştığının sayısal kanıtı.

### 11.1b Geçiş süresi ölçek-değişmez değildir (N78)

Ağır hatta uç pervaneleri, geometrik olarak ölçeklendiğinde 2 saniyelik geçişi
yapamaz — gereken güç askı gücünü aşar:

| Geçiş süresi | 4 pervane toplam | Askı gücünün %'si | İrtifa kaybı |
|---:|---:|---:|---:|
| 2 s | 221,5 kW | **%102** | 8 m |
| 3 s | 65,6 kW | %30 | 18 m |
| **4 s** | **27,7 kW** | **%13** | **31 m** |
| 5 s | 14,2 kW | %7 | 49 m |

**Kural: büyük araç daha yavaş döner.** Gereken moment $M=I\alpha$ ile, $I\propto mL^2$
olduğundan ölçekle hızla büyür. Ağır hat **4 saniyede** döner, 31 m irtifa kaybeder —
1000 kg'lık bir araç için kabul edilebilir. Bu, N54'ün ($P\propto L^{3,5}$) geçiş
tarafındaki karşılığıdır.

### 11.2 Hafif hat geometrisi (N71)

| | Değer |
|---|---:|
| Kök veter | 0,97 m |
| Uç veter | 0,238 m (sivrilme 0,245) |
| Açıklık | 3,45 m |
| Kanat alanı | 1,98 m² |
| En-boy oranı | 6,00 |
| Kırpma | %67 |
| Kanat yüklemesi | 25,3 kg/m² |
| Tutukluk hızı | 20,1 m/s (72 km/sa) |
| Seyir hızı | 30 m/s (108 km/sa) |
| L/D (seyir) | 12,7 |

**Geçiş kontrolü:** 60° eğimde yatay ivme 1,73 g → tutukluk hızına **1,2 s**'de ulaşılıyor.
Kanat, hızlı yunuslama tamamlanmadan devralıyor. N41 bu araçta rahat çalışıyor.

**Menzil:** 8 kg yakıtla ≈ **2 140 km / 19,8 saat.**

### 11.3 Pervane yerleşimi (N72, N74)

| | Değer |
|---|---:|
| Ana pervane çapı | **1,20 m** |
| Uç pervanesi çapı | **0,20 m** |
| Dikme boyu | **uç veterinin %300'ü** = 0,71 m (her yön) |
| Dikey ayrım (üst–alt) | 1,43 m |
| Uç pervanesi itkisi (2 s geçiş) | 16,2 N (1,65 kgf) her biri |
| Uç pervanesi gücü | 335 W her biri · **4 toplam 1,34 kW** (hover'ın %14'ü) |

**Neden uzun dikme:** Kumanda momenti $M = 2\,T\,L_p$. Kolu uzatmak, aynı momenti
daha küçük itkiyle ve **çok daha az güçle** ($P\propto T^{3/2}$) üretmeyi sağlar.
Dikme boyunu üçe katlamak, gereken gücü beşte bire indiriyor.
Dikmeler aynı zamanda iniş yapısıdır — uzaması duruş tabanını da genişletir.

### 11.4 Yuvarlanma kanatçığı (N75)

| | Değer |
|---|---:|
| Boy (45° kolu) | **%120 kök veter** = 1,17 m |
| Dış uç konumu | yarı-açıklığın **%68**'i |
| Yükseklik | 2 cm (iç) → **6 cm** (dış) |
| Yuvarlanma momenti | ≈46 N·m |
| Yuvarlanma hızı | **≈20–25 °/s** (30° yatışa 1,2–1,5 s) |

**Kural: kanatçığın gücü boyundan gelir, yüksekliğinden değil.**

| Boy | Yuvarlanma hızı | | Yükseklik (boy %60'ta) | Yuvarlanma hızı |
|---:|---:|---|---:|---:|
| %60 | 7,6 °/s | | 5 cm | 3,8 °/s |
| %100 | 20,8 °/s | | 10 cm | 7,6 °/s |
| %120 | 28,9 °/s | | 20 cm | 12,0 °/s |

Moment kola göre ölçeklenir; yükseklik artışının getirisi doyuma girer.

**Tek organ, iki iş.** Ana pervane izi yarı-açıklığın yalnızca **%27–39**'unu kaplıyor
(iz yarıçapı 0,67 m → daralarak 0,47 m; yarı-açıklık 1,72 m). Kanatçığın **iç kısmı**
iz içinde kalır ve hover'da istikamet sağlar (N43); **dış kısmı** izin dışındadır ve
seyirde yuvarlanma üretir. Uzatmak hover işlevini bozmaz.

**Yükseklik neden 10 cm değil 6 cm:** Kanatçık dışa uzadıkça yerel veter incelir
(dış uçta 0,47 m). Orada 10 cm, yerel veterin %21'i olurdu — spoiler değil hava freni.
6 cm ile %13'te kalıyor.

⚠️ Mertebe tahmini. Sönümleme katsayısı ve kanatçık etkinliği literatür değerleriyle
alındı, bu geometri için hesaplanmadı. Kesin sayı CFD ya da rüzgâr tüneli ister.
Ancak boy–yükseklik oransal farkı o kadar büyük ki katsayı seçimi sonucu değiştirmiyor.

### 11.5 Kütle bütçesi taslağı (N67)

| Kalem | % MTOW | 50 kg'da |
|---|---:|---:|
| Yapı | 30 | 15,0 kg |
| İtki zinciri | 16 | 8,0 kg |
| Pil tamponu | 4 | 2,0 kg |
| Aviyonik + kumanda | 8 | 4,0 kg |
| Yakıt | 16 | 8,0 kg |
| **Faydalı yük** | **26** | **13,0 kg** |

⚠️ **Hedef, bulgu değil.** Yapı oranı %30 varsayıldı. Kâğıt uçaklar tipik olarak
%20–40 hafif çıkar; o pay bu tabloda henüz ödenmedi.

### 11.6 3B model parametreleri

```
GOVDE09
kok=0.97  hk0=45  hk1=35  fk=25  kirp=67
tc0=25    tc1=12  kamb=6  refl=3
pcap=1.20 parl=8  pkf=4   pkr=3   ucap=0.20
dikme=300 cikinti=5  kalinlik=4
kbas=15   kboy=120 kh0=2  kh1=6   kac=100
mtow=50
```

Model: https://claude.ai/code/artifact/8a4abc4f-83e8-42ce-8894-c84331d6615a

**Bu geometri artık sabittir.** Kütleden türetilmiştir, keyfî değildir.

### 11.7 Rakip MTOW tablosu

| Araç | MTOW | Faydalı yük | Yük oranı |
|---|---:|---:|---:|
| HAVELSAN BAHA | 28 kg | — | — |
| Textron Aerosonde Mk 4.7 VTOL | 45,4 kg | 9,1 kg | %20,0 |
| **Baykar KALKAN DİHA** | **75 kg** | ~3 kg (dahilî) | %4,0 |
| HAVELSAN BULUT | yayımlanmamış | 5 kg | — |
| Elroy Air Chaparral | 865 kg | 136 / 227 kg | %15,7 / %26,2 |
| Sabrewing Rhaegal-A | 1 400 kg | 360–450 kg | %25,7–32,1 |
| Pipistrel Nuuva V300 | 1 700 kg | 408 kg | %24,0 |

⚠️ Üretici tanıtımlarından. Faydalı yük tanımları tutarsız; boş ağırlıklar
yayımlanmıyor. Makalede her satırın kaynağı ve tanımı yazılmalı.

**Ortak nokta:** Bu sınıfın tamamı içten yanmalı motoru **doğrudan bir kaldırma
rotoruna bağlamamış** — hepsi jeneratör ya da ayrık elektrikli kaldırma kullanıyor.
N63'ün sektörel doğrulaması.

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
