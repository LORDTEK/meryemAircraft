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
| N79 | **Yan rüzgârda devrilmezlik iddiası YOKTUR.** Tasarımcının konumu: gerekli takas yapıldı, araç şartların getirdiği ölçüde dayanım gösterir. Yolcu uçakları da sınır dışında iniş/kalkış iptal eder. Bu bir **sınır**, mimarinin anahtar meselesi değil |
| N80 | **Duruş tabanı, tasarım değiştirilmeden genişletilebilir.** Ayaklar dışa ötelenir. Aynı öteleme kumanda momenti kolunu da uzatır ($M=2TL$) → **tek değişken, iki kazanç.** Tasarımcı bunu uygulamıyor; **kullanıcıya bırakılan bir serbestlik** olarak kayda geçti |
| N81 | **Yenilik iddiası: bileşim.** Kanat-gövde bizim değil, VTOL bizim değil, sürükleme faturasının ölçümü bizim değil. Yeni olan: **taktik kullanım avantajını, seyir verimini koruyarak tek araçta birleştiren doğru bileşim.** Makale bu çerçeveden yazılır |
| N82 | **Makale yeniliği ile patent yeniliği ayrı testlerdir.** Makalede bileşim yeniliği meşrudur ve olağandır. Patentte bileşim istemi **aşikârlık** testine girer. İstem, N81'in çerçevesiyle değil, **somut ayrışma unsurlarıyla** yazılır |
| N83 | ⚠️ **UÇ İSKELETLERİ KAPORTALANMAK ZORUNDA.** Yuvarlak boru bırakılırsa dikmeler tek başına seyir sürüklemesinin **%70–93**'ünü üretir — araç uçmaz. Kaportalı kesitle (C_D≈0,15) pay **%12**'ye, iyi kaportayla **%6,5**'e iner. Bu bir tercih değil, **tasarım zorunluluğudur** |
| N84 | **KARAR: dikmeler kaportalanır.** Sabit kaporta, gövde eksenine hizalı, hareketli parça yok. Tasarım $C_D=0{,}15$ (iyimser 0,08 **kullanılmıyor**). Kaporta veteri ≈ 4×çap. Geçişte kaporta bir süre yüksek hücum açısında kalır; 2 sn ve düşük $q$ olduğu için kabul edildi |
| N85 | ⚠️ **MENZİL AŞAĞI REVİZE EDİLDİ: 2 140 km → 1 695 km** (19,8 sa → 15,7 sa). Eski sayı %22,2'lik toplam zincir verimi gerektiriyordu; bu ≈%35 motor verimi demek — küçük benzinli motorda gerçekçi değil. Yeni sayı **açık zincirle** verildi: 0,28×0,90×0,95×0,92×0,80 = **0,176** |
| N86 | 🔴 **DÜZELTME — "İRTİFA KAYBI ∝ $t_r^2$" YANLIŞTI.** Nokta-kütle benzetimi tersini veriyor: **yavaş dönüş DAHA AZ irtifa kaybettirir.** Sebep: dikey destek $T\cos\theta + L$'dir. Yavaş dönerken $\cos\theta$ yüksek kalır ve $L$ bu sürede birikir; hızlı dönerken $\cos\theta$, $L$ daha doğmadan çöker ve araç düşer. Eski model dönüş boyunca aracı **desteksiz** sayıyordu — o varsayım yanlış |
| N87 | **Sonuç: geçişte takas YOK.** Kumanda gücü $\propto 1/t_r^2$ (yavaş = ucuz) ve irtifa kaybı da $t_r$ ile azalıyor. **İki kısıt da aynı yönü gösteriyor: yavaş dön.** $t_r$ aşağıdan sınırlıdır, yukarıdan değil. Üst sınırı belirleyen şey irtifa değil; yakıt, yatay kayma ve taktik maruziyet |
| N88 | ⚠️ **Uç pervanelerinin boyutlandırma durumu değişti.** 16,2 N sayısı 2 sn'lik geçişten türetilmişti. Geçiş artık yavaş yapılacaksa boyutlandıran durum **geçiş değil, hover'da bozucu bastırmadır.** Yeniden boyutlandırma **açık iş** — bu oturumda yapılmadı |
| N89 | **T/W belirleyici parametredir.** T/W=1,1'de araç $t_r$ ne olursa olsun ~10 m kaybediyor; T/W=1,3'te 3 sn'de kayıp sıfırlanıyor. Tasarım varsayımı **T/W = 1,2** |
| N90 | **Winglet: yeni parça EKLENMEYECEK — istasyon zaten dolu.** Uç iskeletleri kanat ucunda, düzleme dik, her yön 0,71 m. $h/b = 0{,}41$; klasik winglet $h/b \approx 0{,}05$–$0{,}10$. **Dikmeler zaten herhangi bir winglet'ten 4–8 kat büyük bir uç yüzeyi.** Karar: N84 kaportası **simetrik dikme kesiti yerine profil (taşıyan) kesit** olarak yapılır. Ek parça yok, ek kütle yok, hareketli parça yok. Seyirde indiklenmiş sürükleme toplam sürüklemenin **%33,7**'si — kazanç için gerçek bir havuz var |
| N91 | ⚠️ **N90'ın kazancı SAYIYA DÖKÜLMEDİ.** Uç yüzeyi klasik winglet bandının çok dışında olduğu için ders kitabı formülleri geçerli değil; panel yöntemi ya da CFD ister. Mertebe: indiklenmişin %6'sı geri gelirse menzil +%2 (+34 km), %20 gelirse +%6,7 (+114 km). **Makalede sayı verilmeyecek**, yalnız mekanizma anlatılacak |
| N92 | ⚠️ N90'ın bedeli: taşıyan uç yüzeyi **kök eğilme momentini** artırır ve seyirde **yön kararlılığını** yükseltir. İkincisi, uç pervanelerinin yönelme komutu için daha fazla moment üretmesi demektir. Açık iş |
| N93 | ✅ **GEÇİŞE TIRMANARAK GİRİLİR — durağan hover'dan değil.** Araç geçiş irtifasına zaten tırmanarak varıyor; durup hover'a geçmek, bedeli ödenmiş dikey momentumu **çöpe atmaktır.** Giriş tırmanış hızı $w_0$, dönüş boyunca harcanacak bir **rezervdir** |
| N94 | **$w_0 = 5$ m/s irtifa kaybını pratikte sıfırlıyor**, $w_0 = 8$ m/s her koşulda sıfırlıyor. Bedeli yok denecek kadar az: T/W=1,2'de dikey ivme $(T/W-1)g = 1{,}96$ m/s², yani 5 m/s'ye **2,6 saniyede** ve **6,4 m** tırmanışta ulaşılıyor. Kinetik enerji 625 J — 103 kWh yakıtın yanında ölçülemez |
| N95 | **Uç pervaneleri KÜÇÜK kalır — 0,20 m.** Gerekçe tasarımcıdan: seyirde olumsuz etki istenmiyor, kumandayı garanti etsin ve bir miktar marj bıraksın yeter. N88'in yeniden boyutlandırması bu yönde çözüldü: geçiş artık boyutlandıran durum değil, hover'da bozucu bastırma öyle — ve o durum mevcut 16,2 N ile **~4 kat marjla** karşılanıyor (mertebe tahmini) |
| N96 | ✅ **BAHA doğrulandı: VTOL'dür.** Üretici föyü: "Runway Independent VTOL Mission Capability", dikey kalkış/iniş. 28 kg MTOW / 2 kg yük = **%7,1**. Tamamen elektrikli → menzil karşılaştırmasına **kapalı** |
| N97 | 🎯 **Rüzgâr sınırı bulundu — N79'u destekliyor.** BAHA föyü: **kalkış/iniş 15 kts (7,7 m/s), seyir 25 kts (12,9 m/s).** Yani sahadaki bir VTOL İHA'nın **yayımlanmış** kalkış/iniş rüzgâr sınırı, seyir sınırından düşüktür. "Yer rüzgârı işletme sınırı vardır" bu sınıfta **olağandır**, kuyruğa oturana özgü bir zayıflık değil. Bölüm 8.9'a girecek |
| N98 | ⚠️ **Şekil 2 düzeltildi.** Zaman çizelgesi hâlâ "XFY-1 pilot iş yükünden bitti" diyordu; NASA belgeleri bunu çürütmüştü ve **metin düzeltilmiş, şekil düzeltilmemişti.** Şekildeki dipnot da "kokpitte yer alan bir kısıt" diyordu. İkisi de motor/dişli kutusu güvenilirliği olarak düzeltildi; XFY-1 noktası 1955'ten **1954**'e alındı |
| N99 | ⚠️ **Bölüm 7.4'ün ilk iki tablosu bayattı.** İçindeki sayılar benzetimin eski bir sürümünden kalmıştı ve **aynı durum (50 kg, T/W=1,2, w₀=0, t_r=1 s) iki tabloda −11,3 m ve −14,2 m olarak geçiyordu.** Eski tabloda ayrıca ağır hatta 3 s → −17,0 / 4 s → −17,7 gibi **monoton olmayan** bir çift vardı — yani tablo, bir sonraki paragrafın "ilişki monotondur" cümlesini çürütüyordu. Her iki tablo `gecis2.py` ile yeniden üretildi; 52 hücrenin tamamı artık doğrulama betiğinden geçiyor |
| N100 | ⚠️ **Bölüm 7.4'te moment ile itki karışmıştı.** "Uç çiftinin kapasitesi 16 N·m" yazıyordu; 16,2 **newton**'luk itki değeri moment yerine kullanılmış. Doğrusu $M = 2TL = 2\times16{,}2\times0{,}71 = 23{,}0$ N·m. N95'teki "~4 kat marj" ancak bu doğru değerle çıkıyor (23/5 ≈ 4,6) |
| N101 | 🔴 **YENİ BULGU — pervane, gövdeden hızlı büyüyor.** Disk yükü sabit tutulunca disk alanı kütleyle orantılı büyümek zorunda (×20), yani pervane çapı ×4,50. Ama kanat yükü 25,3 → 45,0 kg/m² yükseldiği için açıklık yalnızca ×3,35 büyüyor. Sonuç: **çap/açıklık oranı 0,35'ten 0,47'ye çıkıyor.** Ağır hat, hafif hattın uzaktan çekilmiş fotoğrafı değildir — ve bu **Şekil 11'de çıplak gözle görülüyor.** "Oranlar korunuyor" iddiası bu yüzden dört büyüklükle sınırlandırıldı; ölçeklenmeyen büyüklük artık **iki** (geçiş süresi + bu). Giriş, Bölüm 6.4, Bölüm 9 ve Şekil 11 başlığı düzeltildi |
| N102 | ✅ **Askı gücü kütleyle DOĞRUSAL büyüyor.** 10,9 → 216,2 kW, yani ×19,8; kütle ×20. Klasik $L^{3,5}$ değil. Sebebi disk yükünün sabit tutulması: $P \propto W^{1,5}/\sqrt{A}$ ve $A \propto W$ ise $P \propto W$. Kare-küp yasası bu araçta **yalnızca dönüş (Tablo 4) tarafında** tam ödeniyor. Bölüm 6.4'ün kapanışı buna göre yeniden yazıldı |
| N103 | ✅ **Doğrulama betiği yazıldı** — `makale/uretim/dogrula.py`. Makalenin her başlık sayısını, makalenin kendi denklemleriyle bağımsız hesaplayıp metinle karşılaştırıyor: 33 kontrol + geçiş tablolarının 52 hücresi. Bayat sayı bir daha sessizce kalamaz |
| N104 | ✅ **Başvuru numarası kayda geçti: 2026/014570** (26.08.2026). Rüçhan bu tarihten işler; yurt dışı için son gün **26.08.2027.** Evrak numarası iç takip kaydıdır, dışarıya verilmez |

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

### 11.1c Geçiş benzetimi (N86–N89) — **11.1b'nin yerine geçer**

2 serbestlik dereceli nokta-kütle benzetimi. $\theta$ (gövde ekseninin dikeyden
açısı) $t_r$ sürede 0→90° kinematik olarak sürülüyor; itki gövde ekseninde,
taşıma hıza dik, sürükleme hıza ters. $C_L=C_{L\alpha}\alpha$ tutukluğa kadar,
sonrası düz levha. Seyir hızına ulaşınca gaz sürüklemeye iniyor.

**İrtifa kaybı (m) — hafif hat, 50 kg:**

| $t_r$ | T/W=1,1 | **T/W=1,2** | T/W=1,3 | T/W=1,5 |
|---:|---:|---:|---:|---:|
| 0,5 s | −15,9 | −13,5 | −11,5 | −8,3 |
| 1 s | −14,0 | −11,3 | −8,8 | −3,0 |
| 2 s | −10,5 | **−6,6** | −1,6 | 0 |
| 3 s | −9,9 | **−0,3** | 0 | 0 |
| 4 s | −1,8 | **0** | 0 | 0 |

**İrtifa kaybı (m) — ağır hat, 1000 kg:**

| $t_r$ | T/W=1,1 | **T/W=1,2** | T/W=1,3 | T/W=1,5 |
|---:|---:|---:|---:|---:|
| 1 s | −26,6 | −22,1 | −18,2 | −11,5 |
| 2 s | −21,8 | −16,0 | −6,8 | −0,2 |
| 3 s | −17,0 | −6,3 | −0,6 | 0 |
| 4 s | −17,7 | **−0,6** | 0 | 0 |
| 5 s | −5,0 | **0** | 0 | 0 |

**Monoton.** Optimum yok, doyum var.

**İrtifa kaybı (m), geçişe TIRMANARAK girildiğinde — hafif hat, T/W=1,2 (N93/N94):**

| $t_r$ | $w_0=0$ | $w_0=2$ m/s | $w_0=5$ m/s | $w_0=8$ m/s |
|---:|---:|---:|---:|---:|
| 1 s | −14,2 | −10,3 | −0,4 | **0** |
| 2 s | −9,1 | −0,4 | **0** | **0** |
| 3 s | −0,8 | **0** | **0** | **0** |
| 4 s | **0** | **0** | **0** | **0** |

Ağır hatta da aynı: $w_0=5$ m/s, $t_r\ge2$ s için kayıp sıfır.

**Tasarım profili: $w_0 = 5$ m/s ile girilir, $t_r = 3$ s'de dönülür, irtifa kaybı sıfır.** Eski 11.1b tablosundaki "2 sn → 8 m,
4 sn → 31 m" sayıları **kullanılmayacak.**

⚠️ Benzetim **dönme dinamiğini modellemiyor** — $\theta$ kinematik sürülüyor.
Uç pervanesi itkisi bu benzetimden çıkmaz (N88).

### 11.1b Geçiş süresi ölçek-değişmez değildir (N78) — ⚠️ **KISMEN GEÇERSİZ, bkz. 11.1c**

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

**Menzil (N85, revize):** 8 kg yakıtla **≈ 1 695 km / 15,7 saat.**

Zincir açıkça: içten yanmalı 0,28 × jeneratör 0,90 × güç elektroniği 0,95 ×
elektrik motoru 0,92 × pervane 0,80 = **0,176**. Benzin 12,9 kWh/kg.
Faydalı itki gücü $D\cdot V = 38{,}6 \times 30 = 1{,}16$ kW.

⚠️ Eski 2 140 km sayısı %22,2 zincir verimi varsayıyordu (≈%35 motor verimi).
Küçük benzinli motorda gerçekçi değil. **Kullanılmayacak.**

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

### 11.5b Uç iskeleti sürüklemesi — N83

Hafif hat, seyir: $q = 551$ Pa, toplam seyir sürüklemesi $D = W/(L/D) = 38{,}6$ N.
Dikmeler: 2 uç × 2 yön × 0,71 m = **2,84 m** toplam açıkta uzunluk, akışa **dik**.

| Dikme kesiti | $C_D$ | $d=15$ mm | $d=20$ mm | $d=25$ mm |
|---|---:|---:|---:|---:|
| Yuvarlak boru | 1,15 | %70 | **%93** | %117 |
| Kaportalı dikme | 0,15 | %9,1 | **%12,2** | %15,2 |
| İyi kaportalı | 0,08 | %4,9 | **%6,5** | %8,1 |

*(Toplam seyir sürüklemesinin yüzdesi. $Re \approx 3$–$5\times10^4$, kritik altı.)*

**Sonuç:** yuvarlak boru seçilirse araç uçmaz — dikmeler kanadın tamamı kadar
sürükleme üretir. **Kaportalama zorunludur.** Kaportalıyken bedel gerçek ama
ödenebilir: seyir sürüklemesinin ~%12'si.

**Ölçek-değişmezlik:** dikme ön alanı $\propto L^2$, kanat alanı da $\propto L^2$.
Geometrik ölçeklemede ve eşit seyir dinamik basıncında **bu oran korunur** — ağır
hatta da ~%12. Fatura ölçekle büyümüyor.

⚠️ $C_D$ değerleri literatür mertebeleridir; bu kesit için hesaplanmadı. Dikme
kesiti henüz seçilmedi. **Açık iş.**

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
| **HAVELSAN BAHA** (üretici föyü, doğrulandı) | **28 kg** | **2 kg** | **%7,1** |
| Textron Aerosonde Mk 4.7 VTOL | 45,4 kg | 9,1 kg | %20,0 |
| **Baykar KALKAN DİHA** | **75 kg** | ~3 kg (dahilî) | %4,0 |
| HAVELSAN BULUT | yayımlanmamış | 5 kg | — |
| Elroy Air Chaparral | 865 kg | 136 / 227 kg | %15,7 / %26,2 |
| Sabrewing Rhaegal-A | 1 400 kg | 360–450 kg | %25,7–32,1 |
| Pipistrel Nuuva V300 | 1 700 kg | 408 kg | %24,0 |

⚠️ Üretici tanıtımlarından. Faydalı yük tanımları tutarsız; boş ağırlıklar
yayımlanmıyor. Makalede her satırın kaynağı ve tanımı yazılmalı.

**BAHA — üretici föyünden doğrulandı (N96):** sabit kanat, **dikey kalkış/iniş
yapıyor** (açık iş kapandı). MTOW 28 kg, faydalı yük 2 kg, açıklık 4 m, boy 2,1 m,
seyir 75–80 km/sa, **havada kalış 2 saate kadar**, tavan 10 000 ft, veri bağı 50 km.
İtki ve VTOL sistemi **elektrik motoru**.

⚠️ **BAHA ile menzil karşılaştırması YAPILMAYACAK.** Araç **tamamen elektrikli**;
2 saatlik havada kalışı **pil sınırıdır, mimari sınır değil.** Bizim seri hibrit
15,7 saatimizi onun 2 saatine karşı koymak, mimarileri değil **enerji kaynaklarını**
karşılaştırmak olur — Bölüm 6.5'te reddettiğimiz kategori hatasının aynısı.

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
