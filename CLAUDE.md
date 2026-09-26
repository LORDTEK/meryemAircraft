# meryemAircraft — çalışma kuralları

## 0. İDDİANIN NE OLDUĞU. Bunu bir daha kaçırma.

Bu çalışmanın **var oluş nedeni mimari yeniliktir.** Menzil rekoru değildir.
Aşağıdaki dört satır projenin omurgasıdır ve her metin, her düzeltme, her
özet bunlarla tutarlı olmak zorundadır.

**Rakip kim, hangi eksende — dördü de ayrı:**

| Eksen | Rakip | Durum |
|---|---|---|
| **Menzil / seyir verimi** | **Döner kanatlılar: çok rotorlu VE helikopter** (yazar, Tur 97) | **Çok rotorluya karşı yeniyoruz** (elektrikli quadrotora karşı en düşük köşe hariç). **Helikoptere karşı sonuç karışık** ve öyle yazılır (Adım 6D, S-27). Üstünlük iddiası yalnız kanıtın taşıdığı yerde. |
| **Piste ihtiyaç / dikey iniş kalkış** | **Sabit kanatlı** | **Yeniyoruz. İnşa gereği.** |
| **Mekanik ve kontrol basitliği** | **Tilt mimarileri** | **Asıl katkı bu.** |
| Menzil, öteki hibritlere karşı | Lift+cruise, tilt | **İDDİA EDİLMİYOR.** Sözleşmeye göre oynar; lift+cruise'a karşı bir sözleşmede işaret zarfın içinde değişir (Adım 13). Tilt yalnız sınır olarak modellenebiliyor. |

**Yapılmayacak iki hata — ikisini de yaptım, ikisi de yazar tarafından
yakalandı:**

1. **Sabit kanatlıyla menzilde yarışmak.** Planörden daha uzağa gitmeyi kim
   iddia edebilir? Neden edelim? Mesafede çok rotorluyu yenmek yeterlidir.
2. **Çok rotorluyla dikey iniş kalkışta yarışmak.** Saçmadır. O eksende
   rakibimiz sabit kanatlıdır ve üstünlük inşa gereğidir.

Ben uzun süre tam tersini yaptım: menzilde sabit kanatla, taktik avantajda
çok rotorluyla yarıştım. Her karşılaştırmayı yanlış rakibe karşı kurdum.

**Tilt mimarilerine karşı iddia menzil DEĞİLDİR, mekanizmadır.** Tiltler
bugün yaygın değil; nedeni mekanik karmaşıklık, gyroskopik bağlaşım ve geçiş
kontrol problemi. Bu çalışma **o probleme alternatif bir çözüm öneriyor:**
aynı rejim geçişi, dönen hiçbir mekanizma olmadan, kumanda yüzeyi olmadan,
değişken hatve olmadan — yalnız sabit hatveli pervanelerin diferansiyel
itkisiyle. Katkı budur.

**Sayılar değişmez.** *(Tur 55 notu: aşağıdaki 24–45 / 32–36 v7'nin η_p 0,80 tabanıdır. v8 Adım 13,
hesaplanmış η_p tabanında: sabit yakıt kesrinde lift+cruise %55–84 önde, kütle üstünlüğü %27–30.
"Değişmez" = çerçeve değişince sayı eğilmez; hesap değişince sayı değişir.)* Menzil açığı 24–45 %, kütle üstünlüğü 32–36 %, bunların
hepsi dürüstçe raporlanmaya devam eder. Değişen şey **neyin iddia edildiğidir.**
Öteki hibritlere karşı menzil sıralaması bir boyutlandırma sonucudur, tez
değildir.

**"Genel mimari üstünlük iddiası yoktur" gibi bir cümle bir daha yazılmaz.**
Bir kez yazıldı, 4.2 ile çelişti ve makalenin kendi tezini inkâr etti.

**Helikopter de rakip. Yazar, Tur 97.** *"Helikopter için neden rakibimiz değil dedin? Sadece 4 rotorlular mı rakibimiz
olduğunu düşündün? … hareketli kanatlılardan (evet helikopterler de dahil) menzil olarak daha etkin."* Adım 1A zaten
"Rotorcraft and multirotors"ı tek aile sayıyordu; ben tabloyu "quadcopter" diye dar okudum ve S-27'ye "not extended to the
helicopter" yazdım. **Ama sayılar:** NASA Tablo 3'te (tek ortak birimli kaynak) helikopterler L/De 5,4–7,2; bizim zarf
5,56–7,39 → turboşaft tek rotorluya karşı her köşede önde, ortadaki ikisi zarfın içinde, elektrikli yan yana rotorluya
(7,2, kanatsız) karşı yalnız en üst köşe önde. Yazar (b)'yi seçti: *"helikopterleri de rakip say"* — eksen genişler, sonuç
dürüstçe karışık yazılır, üstünlük iddiası yok. **"Tüm hava araçlarından daha etkin" denmez:** aynı tabloda lift+cruise ve
tiltwing 7,9–8,6, zarfımızın tamamının üstünde; onlara karşı iddia mekanizmadır. **V-22'ye karşı güvenilirlik denmez**
(ölçülmedi; on elektrik makinesi); mekanizma sınıfı sayımı denir.

### 0.1 Üçüncü iddianın SINIRI. Bunu da bir daha aşma.

İddiayı düzeltirken hemen aşırıya kaçtım ve **makalenin kendi §2.10'uyla çelişen**
bir cümle yazdım: *"hareket eden mekanizma yok", "hiçbir aerodinamik kumanda
yüzeyi yok", "her eksendeki her moment diferansiyel itkiden".* Üçü de **yanlış.**

**Yatış (roll) itki vektörlerinden ÜRETİLEMEZ** — hepsi gövde eksenine paralel,
dolayısıyla hiçbir itki ayarı X_b etrafında moment vermiyor. Yatışı alt yüzeydeki
**değişken uzantılı şerit** sağlıyor ve makale ona *"uçaktaki tek hareketli
aerodinamik yüzey"* diyor.

> **DÜZELTME, Tur 47 — bu maddenin kendisi fazla iddialıydı.** Önceki hâli *"yatış
> eşeksenli pervanelerle üretilemez"* diyordu. **Yanlış.** §2.9 her rotorun **kendi
> elektrik makinesinde** olduğunu söylüyor; iki karşıt rotor farklı devirlerde
> döndürülürse torkları birbirini götürmez ve net tork X_b etrafındadır. Burun
> rotoru başına askıda **24,9–27,5 N·m** (hesaplandı: `aero/reaction_torque.py`,
> seçilmiş paletlerden; çift gücü makalenin 10,9 kW'ını %1,7 içinde yeniden
> üretiyor); **%30 dengesizlik 7,5–8,2 N·m** verir, yani şeridin askıdaki
> aralığının (6–12 N·m) **içinde.** Ve literatür bu kanalı **kullanıyor**:
> Zhang ve ark. 2012, eşeksenli çift rotorlu kuyruk üstüde *"Roll motion is
> controlled by the **differential velocity of the two motors**"* diyor
> (`references/ica20120400001_12673514.pdf`). Ayrıca makale kendisiyle de çelişiyordu:
> §2.9 askı tork artığı için *"the **speed trim of the pairs**"* diyor.
>
> **Doğru ifade:** yatış itkiden üretilemez, **tepki torkundan üretilebilir**, ve bu
> yapılandırma onu kontrol kanalı olarak **kullanmamayı seçer.** *"Fiziksel
> imkânsızlık"* değil, **tasarım kısıtı.** Bedeli — itki asimetrisi, verim, rotor
> ataletinden gelen yecikme — **sayılmadı;** açık kalem.

**EKSENLER ASKI İLE SEYİR ARASINDA GÖREV DEĞİŞTİRİR.** Askıda burun yukarıdayken
X_b dikeydir. Dolayısıyla: sağ/sol uç çifti (gövde sapması) askıda **bank** yapar;
şerit (gövde yatışı) askıda **yön** değiştirir. §2.10'un *"enough for a thirty-degree
bank"* cümlesi askı paragrafındadır ve **yanlıştır** — şerit askıda bank değil yön
verir. Literatür bunu 2014'te adlandırmış: *"the definition of the roll and yaw angles
are **interchanged**"* (Wang ve ark., `references/2014_0529_paper.pdf`).
**Askı ile seyir eksen adları asla karıştırılmaz.**

**Doğru iddia dar olanıdır:**

> Tilt mimarilerine karşı ortadan kaldırılan şey **propulsor'ü yeniden
> yönlendiren mekanizma sınıfıdır** — pivot yok, nasel eyleyicisi yok, değişken
> hatve göbeği yok, dönen kütleden gyroskopik moment yok. **Uçakta hiç hareketli
> parça olmadığı DEĞİL.** Yunuslama ve sapma diferansiyel itkiden; yatış
> şeritten. Eyleyici envanteri: motorlar **artı bir şerit eyleyicisi.**

**"Mekanik olarak daha basit" de denmez** — parça sayısı, kütle, arıza kipi,
bakım hiçbiri ölçülmedi. Denen şey bir **sayımdır**, güvenilirlik iddiası değil.

Bunu üç dış okuyucu bağımsız olarak yakaladı ve biri yanlış dosyayı okurken
yakaladı, çünkü §2.10 her iki sürümde de aynıydı. **Ders: bir iddiayı
düzeltirken, yeni iddianın makalenin kendi bölümleriyle çelişip çelişmediğini
denetle.** Doğru çerçeve, yanlış kapsamla yazılırsa yine yanlıştır.

### 0.2 Aynı hata ÜÇÜNCÜ kez oldu. Kural artık mekanik.

§2.10 çelişkisini düzeltirken §3.17'ye *"şerit yunuslama momenti üretmez"*
yazdım. §2.10 ise şeridin **burnu aşağı yunuslattığını** söylüyor
(ΔC_m 0,005–0,032). Yine düzeltmenin kendisi yeni bir çelişki doğurdu.
Ayrıca dayanağı olmayan bir sayı uydurdum: *"artı bir şerit eyleyicisi."*
Makale şeridin eyleyici sayısını hiçbir yerde vermiyor; §2.10 onu **iki
yarım** olarak tarif ediyor.

**Bundan sonraki kural — istisnasız:**

> Bir iddiayı ya da bir özeti yazdıktan sonra, içindeki **her olgusal
> yüklem** için o iddianın özetlediği bölümü AÇ ve oku. Sayı veriyorsan
> o sayının kaynakta geçtiğini gör. Bir şeyin *olmadığını* söylüyorsan,
> onun olduğunu söyleyen bir bölüm var mı diye ara.

Üç turda üç kez: "hiçbir mimari üstünlük yok" (4.2 ile çelişti),
"hareket eden mekanizma yok" (2.10 ile çelişti), "şerit yunuslama momenti
üretmez" (yine 2.10 ile çelişti). Üçü de **özet yazarken** oldu. Özet
yazmak, bu projede en yüksek hata oranlı iştir.

### 0.3 DÖRDÜNCÜ kez, ve bu kez dış okuyucular yakaladı.

Tur 29'da dış okuyuculara giden metne şunu yazdım — üstelik tam da *"bunu
unutma"* diye kendime not düştüğüm paragrafın içinde:

> *"a configuration that unites the tactical freedom of a rotorcraft with **the
> range of a fixed-wing aircraft**"*

**Bu, §0'ın birinci yasak hatasıdır:** sabit kanatlıyla menzilde yarışmak. İki dış
okuyucu bağımsız olarak yakaladı.

**Bundan sonra kullanılacak ifade:**

> **piste ihtiyaç duymayan dikey işletim** ile **kanatla seyir verimini**
> birleştiren, ve bu birleşmeye **propulsor'ü yeniden yönlendiren hiçbir mekanizma
> olmadan** ulaşan yapılandırma.

"Sabit kanadın menzili" **denmez.** Menzil iddiası yalnız çok rotorluya karşıdır.

Ayrıca *"inşa gereği"* (by construction) ifadesi dikkatli kullanılacak: tasarım
dikey işletimi **boyutlandırıyor**, ama geçiş ve uçabilirlik **gösterilmedi**.

### 0.4 Merkez ne demek — yazarın düzeltmesi.

Tur 29'da yazarın konumunu dış okuyuculara **yanlış aktardım**: mimarinin merkez
olmasını *"geri kalan her şey ya muhasebedir ya da ödenen bedeldir"* diye yazdım.
Bu, çerçeveyi araçsal gösterdi ve turun bir kısmını yanlış yere götürdü.

**Yazarın gerçek konumu:** *"Ben işin merkezi derken diğer kısımlarının olmayacağını
söylemedim."* **Ana akış ve gölgelenmeyecek olan, anlatılan yeniliktir. Ama bugüne
kadar yapılmış hesaplar da doğru şekilde, doğru yerinde eklenecektir.** İkisi
birden; biri ötekinin pahasına değil.

### 0.5 Aşama atlama. Yazarın ikinci düzeltmesi.

Tur 29'da dış okuyuculardan kelime bütçeli, şekil ve tablo atamalı bir içindekiler
istedim. **Yanlış aşamanın sorusuydu.** Yazarın istediği çok daha geride:

> *"Çok kabaca genel anlatım akış taslağı oluşturmaya çalışıyorum. Tablolar falan
> çok detay şeyler."*

Yazarın kendi örneği — bir saniyede, yalnız *şekil* olarak verilmiş:

> giriş · mevcut durum · şu soruna çözüm · bu soruna çözüm · **çözümlerin
> birleştirilmesi** · ortaya çıkan ürünün sorunsuzluğu · mevcut hesaplar · sonuç

**Dikkat: "çözümlerin birleştirilmesi" kendi başına bir adım.** Bir sonuç bölümünün
içine sıkıştırılmış bir yan ürün değil, argümanın adı konmuş bir hamlesi. Beş ayrı
içindekiler önerisinin hiçbirinde böyle bir adım yoktu.

**Kural: önce en kaba hat, sonra ayrıntı.** Bütçe, tablo sayısı, şekil ataması —
hepsi kabul edilmiş akışın üstüne kurulur, öncesine değil.

### 0.6 Katkı sayısı. Yazarın kararı, Tur 35.

DeepSeek iki katkı önerdi (uçak; çerçeve+sözleşme sonucu). Grok bir katkıda ısrar etti:
*"sonuç, ikinci ve eşit bir buluş değil"* ve *"özette iki katkı yine iki makale gibi
okunur"* — masadan ret tam olarak buydu. Masada aslında **üç** aday vardı:

| | Ne | Türü |
|---|---|---|
| **A** | Mimari — kaçış koşulunu propulsor'ü döndüren mekanizma olmadan karşılayan yapı | **buluş** |
| **B** | Üç faturalı çerçeve — taşınan askı kütlesi, açıkta seyir sürüklemesi, askı tepesiyle boyutlanan sürekli güç | **yöntem** |
| **C** | Sıralamalar mimariye değil boyutlandırma sözleşmesine aittir; sıra tersine döner | **bulgu** |

**Karar — tek katkı: mimari.** Çerçeve, mimari iddiayı **denetlenebilir kılan araçtır**;
eşit ikinci katkı değildir, ama süs de değildir: kendi adımlarını (2, 3, 4, 12, 13) tam
boyuyla korur. Sözleşme bağımlılığı **belirgin biçimde, bir bulgu olarak** söylenir —
makalenin savunduğu ikinci bir tez olarak değil.

**Bu, v7'nin 227. satırının bilerek tersine çevrilmesidir:**

> *"**Contributions.** The primary contribution is a framework; the aircraft is the case
> that instantiates it."*

Gerekçe §0.4'tür: merkez mimaridir, ama öteki kısımlar yok olmaz; hesaplar doğru yerinde
tam olarak durur.

**Bedeli bilerek kabul edildi:** hakem uçağı reddederse, v7'nin sıralaması ayakta bir
çerçeve bırakıyordu; v8'inki bırakmıyor. Buna karşılık, bizi koruyan o sıralama aynı
zamanda bizi *"iki makale"* gibi gösterip masadan attıran sıralamaydı.

### 0.7 Menzil sayısı tez değildir. Yazarın duruşu, Tur 38.

Burun çifti hesabı programa alınırken yazar şunu söyledi ve bu, hesabın riskini
tanımlayan cümledir:

> *"Lütfen menzile çok takılma. 1600 km değil de 1000 km olsa inan ki hiç ama hiç bir şey
> kaybetmem. Herhangi bir quadcopter 1000 km gidebilir mi? Dolayısıyla menzil ile ilgili
> bilimsel bölgede kaldığımız sürece sonuç hiç önemli değil."*

Bu §0'ın yeniden ifadesidir: **menzil iddiası yalnız çok rotorluya karşıdır** ve o eksende
pay o kadar geniştir ki bir hesabın sayıyı aşağı çekmesi tezi tehdit etmez.

**Pratik sonucu şudur:** bir hesabın menzili düşürmesi, o hesabı yapmamak için gerekçe
değildir. Tersine — menzil sayısı tez olmadığı için hesabı **rahatça** yapabiliriz.
Kaybedilecek şey bir sayı, korunacak şey dürüstlüktür, ve bu takas her seferinde kabul
edilir.

**Yine de sayı tahmin edilmez.** Grok'un uyarısı geçerli: *"Do not guess the sign."*
Hesabın işareti hesaptan önce söylenmez.

### 0.8 Makalenin ruhu. Yazarın duruşu, Tur 61.

> *"Yazarın (yani benim) özellikle sunmuş olduğu üstünlük olarak belirttiği şey bu makalenin ruhu olmak
> zorunda. Yoksa 'yet another' hesap kitap işi olmasını istemiyorum. Görülememişi görmüş olmanın haklı
> gururunu taşıyorum. Hesap kısmını neden yaptık? Q1 için."*

**Sonuç:** makale bir hesap makalesi değil, **bir kavrayışın sunumudur.** Hesaplar o kavrayışı Q1 hakemi
önünde **denetlenebilir ve inandırıcı** kılmak için vardır; kendi başlarına amaç değildir. Kısaltmada, yapıda
ve seste merkez mimaridir.

**Ama ruh, yüklemi genişletmez.** §0.1–0.3'ün dar gücü aynen durur: *"arranged to"*, mekanizma sınıfı sayımı,
basitlik iddiası yok, öncelik iddiası yalnız *"bulunamadı"* biçiminde (§2.2). Kavrayışı taşıyan şey
**yerleşim, sıra ve ses**tir; daha güçlü bir cümle değil. Daha güçlü cümle, Tur 46'da daraltılan boşluk
iddiasını yeniden açar ve bizi masadan attırır. **Açık gerilim (yazara soruldu, Tur 61):** Adım 1'in
*"not a claim that the route was waiting to be found"* ifadesi ile yazarın *"görülememişi görmüş olmak"*
duruşu.

## 1. Yazışma ve üslup

- Kullanıcıyla **Türkçe**. Öteki YZ'lere (ChatGPT, Grok, DeepSeek, Qwen)
  giden metinler **İngilizce**.
- Acımasız dürüstlük. Cesaretlendirme yok. Aşırı mühendislik yok.
- Kullanıcı YZ yorumlarını uzun uzun okumaz; **özetle.**

## 2. Dış görüş metinlerinin standardı

Her metin **kendi kendine yetmeli** ve süreci çıplaklığıyla ortaya koymalı:
ne yaptın, ne buldun, ne umuyordun, hangi aşamadasın, hangi aşamalar için
özellikle yorum istiyorsun, bir önceki turdaki iddialar ne oldu. **Herkes her
şeyi bilsin.**

- **Okuyucuya dosyayı doğrulama yolu ver:** depo bağı, commit karması,
  SHA-256, birkaç saniyelik arama. Bir okuyucu bayat dosya okuduysa hüküm
  verme, **kontrol imkânı ver.** Bu ders pahalıya öğrenildi.
- Kendi bulgularını ve **kendi hatalarını** da yaz. Bir düzeltmenin yan
  hasarıysa öyle işaretle.
- Büyük aşama öncesi **parça–bütün–parça** okuma iste.

### 2.1 Kaynak kuralı, ve onu taşınabilir kılan sınır. Tur 44–46.

**Kural (Tur 44, yazar):** *"Herkes iddialarının kaynağını indirilebilir PDF bağlantı olarak
versin. Ben de indirip GitHub'a yükleyeyim."* Yazar indirir, depoya girer, o andan sonra
**herkes aynı dosyadan alıntılar.**

**İki turda iki kez işe yaradı ve ikisinde de farklı yönde:**

- **Tur 45:** dört okuyucu NASA sayıları için dört ayrı küme verdi. Belgeler yüklenip okununca
  **üç ayrı belge** oldukları çıktı ve her biri kendi belgesi için doğruydu. **Bizim
  sayılarımız doğrulandı.**
- **Tur 46:** üç okuyucu Adım 1'in boşluk cümlesini çürüttü. Belgeler okununca **haklı
  oldukları** çıktı. **Bizim iddiamız daraltıldı.**

**Ama kural ağır.** Yazar: *"Bu şekilde olunca da çok iş çıkıyormuş."* Bazı bağlar
indirilemedi, bazıları açılmadı. Taşınabilir olması için sınırı var:

> **PDF yalnız bir iddiayı ÇÜRÜTEBİLECEK şeyler için istenir:**
> **(a) öncelik ve yenilik iddiaları** — "bu daha önce yapılmadı" diyen her cümle,
> **(b) sayılar** — tablodan alınan her değer,
> **(c) birebir alıntılar.**
>
> **Görüş, yargı, yapı önerisi, üslup eleştirisi için PDF istenmez.** Bu turların çoğu
> değeri oradan geliyor ve onlar kaynak gerektirmiyor.

**Ve karşılığı verilir:** hangi belgeyi **o turda açtığını** söylemeyen bir sayı kullanılmaz.
Açamadıysa sayı vermemesi istenir — çekinceli bir sayı, sayı olmamasından beterdir, çünkü
kayda veri gibi girer.

**Kaynak açma kuralı (Tur 94; DeepSeek, Qwen P1; dört okuyucu + Claude).** *"When a source is opened to verify a
figure or a quotation, the paragraph around it and the source's own discussion or conclusion on the same quantity are
read and recorded in the evidence file. A qualification or contrary figure found there is either quoted in the body or
recorded as omitted, with the reason."* Gerekçe: dört seçici alıntı — S-18 (Bacchini, hız kazancı), S-19 (Barrett 3 kW/kg),
S-20 (Barrett'in kendi "may be possible" sonucu), S-22 (DelftaCopter değişken hatveli). Son ikisi kural oylanmadan,
kuralı uygulayarak bulundu.

**Sayı tutarlılığı adımı (Tur 95; DeepSeek, ChatGPT'nin genişletmesi; dört okuyucu + Claude).** Bir cümle sayılmış bir
listeye öğe ekler, çıkarır, böler ya da birleştirirse, yakındaki her sayı (*"three kinds"*, *"four parts"*, *"one historical
difficulty"*) ve o listeyi sayan her cümle değişiklik uygulanmadan önce yeniden okunur. Grok P51'in ikizi: P51 sonraki cümlenin
göstericilerini, bu paragrafın sayılarını okur. Örnek: R-3. (Genişletilmiş biçim Tur 96'da dört okuyucu + Claude.)

**Tanık kapsamı denetimi (Tur 96; ChatGPT; dört okuyucu + Claude).** Bir kaynak bir uçak sınıfı hakkındaki cümleyi
destekliyorsa, tanığın cümlenin söz ettiği **aynı nüfusa ve kapsama** ait olduğu denetlenir. Örnek: insansız uçuşla açılan
bir paragrafa insanlı V-22 tanığı önerdim; üç okuyucu reddetti. **Kaynak-sonuç işareti (DeepSeek):** açılan her kaynak için
kaynağın kendi sonucunun alıntılanan rakamla ilişkisi `paper/v8-evidence.md`'de kaydedilir (destekler / niteler / yumuşatır /
çelişir / söylemiyor — ChatGPT'nin değerleri).

**Tablo bütünlüğü denetimi (Tur 97; ChatGPT; dört okuyucu + Claude).** Bir kaynak tablosu tam açılıp bir karşılaştırmayı
sınırlamak için kullanıldığında, iddiaya değebilecek her satır hesaba katılır — yalnızca neden alınmadığını kaydetmek için
bile olsa. Örnek: S-27 (J&S Tablo 3'teki helikopterler).

**Rakip ailesi sözcük kilidi (Tur 99; ChatGPT; dört okuyucu + Claude).** "Multirotor" her geçişte üç türden biridir:
aile düzeyinde ifade (→ *rotorcraft*), belirli referans (kalır: iki quadrotor, quadrotor kuyruk üstüleri), kaynak alıntısı
(dokunulmaz). Eksen değişince her ifade bu üçe göre sınıflanır.

**Koşullu envanter kuralı (Tur 100; ChatGPT; dört okuyucu + Claude).** Bir donanım sınıfı envanterinde bir öğenin varlığı
çözülmemiş bir işletim durumuna ya da uygulama seçimine bağlıysa, o öğe kesin olarak "yok" sayılmaz; koşul envanterin
evinde ve ona dayanan her sayımda görünür. Örnek: S-33 (uç rotorların durdurma aracı).

### 2.2 Yenilik iddiası yazmadan önce. Tur 46'nın bedeli.

Adım 1'e *"1954'te bir kez uçuruldu ve tekrar ele alınmadı"* ve *"her mimari bunu propulsor'ü
yeniden yönlendirerek yapar"* yazdım. **İkisi de yanlıştı** ve üç dış okuyucu bağımsız olarak
yakaladı. İnsansız kuyruk üstü literatürü on yıldır sürüyor; kumanda yüzeysiz kuyruk üstü
2013'te deneysel doğrulamayla bildirildi; BWB kuyruk üstü 2025'te afet müdahalesi için
bildirildi; ve sabit hatvenin iki rejimde birden verimli olamaması **bilinen bir sonuç.**

**Kural:** *"yapılmadı", "tek", "ilk", "tekrar ele alınmadı"* gibi her cümle için **önce
aranır.** Bulunamaması aranmadığının kanıtı değildir; bu yüzden iddia **"bulunamadı"**
biçiminde ve **aranan yer adlandırılarak** yazılır.

**Ve boşluk iddiası daraldığında zayıflamaz.** Doğru biçim şudur: neyin zaten dolu olduğu
**boşluktan önce** sayılır, sonra bulunmayan şey **bir arada ve bedeliyle** tarif edilir.

### 2.3 Tur metninin biçimi ve kısaltma yöntemi. Yazar, Tur 61.

> *"Bundan sonraki metinlerde tüm içeriği boca etmemize gerek yok. … İteratif gidebiliriz, dolayısıyla
> değişiklikleri sunmakla yetinebiliriz. Kısaltmaları doğrudan yapmayacağız. Herkesin fikrini herkese
> sunup herkesin görüşünü alacağız. … Hemfikir olunan hususların işlenmesine öncelik verilebilir."*

- **Dosya düzeni (yazar, Tur 65 — "kolayca güncel soru dosyasına erişebileyim"):** `cfd/` kökünde yalnız **güncel
  tur metni** ve `reader-onboarding.md` durur; yeni tur yazılınca bir öncekisi **aynı commit'te**
  `cfd/arsiv-dis-gorus/`'a taşınır ve `cfd/README.md`'nin başındaki işaretçi güncellenir. Kaynak PDF'ler
  `references/`'e gider; `cfd/source/` CFD kodunun açtığı dosyalardır, yerinde kalır.
- **Tur metni yalnız değişiklikleri taşır.** Tam metin okuyucuların penceresinde zaten var (son tam metin
  hangi turdaysa ona atıf yapılır, commit karmasıyla). Yeni pencere açan okuyucu için `cfd/reader-onboarding.md`.
- **Kısaltma doğrudan yapılmaz.** Her okuyucunun önerisi öteki okuyuculara **yan yana** sunulur; görüş alınır.
- **Önce hemfikir olunanlar işlenir**; ayrışanlar herkese geri sorulur. Karar yazarındır.
- Tutulan belge: `paper/v8-shortening-consensus.md` (hemfikir / ayrışan / açık).
- **Kesilemeyecek çekinceler:** `paper/v8-caveats.md`, denetimi `paper/build/v8_caveats.py`.

**Ek, Tur 62 (yazar):** *"Her metinde elbette kendi görüşlerin de olsun. … senin görüşlerin hakkında da fikir beyan
etsinler. Yoksa sadece kendi kendilerini yargılarlarsa, sen bana eşdeğer gibi olursun ki hoş değil."* Ve: *"Sen de
dahil herkesin hemfikir olduğu kısaltmalar uygulansın."*

- **Ben de bir okuyucuyum, hakem değilim.** Her tur metninde her açık madde için **kendi görüşüm ve gerekçem**
  yazılır ve okuyuculardan **benim görüşümü de eleştirmeleri** istenir. Oylama tablosunda ben de bir sütunum.
- **Uygulama eşiği: dört okuyucu + ben.** Biri bile karşıysa uygulanmaz, geri sorulur. Karar yine yazarındır;
  yazar okuyucu cevaplarını kendisi okumaz, **bana yapıştırır** — bu yüzden yazara verilen özet eksiksiz ve dürüst
  olmak zorunda: kim ne dedi, ne uygulandı, ne neden uygulanmadı, benim hatalarım.
- **Uygulanan bir kısaltma, sonucu herkes tarafından teyit edilene kadar KAPANMAZ.** Yazar, Tur 63: *"'Herkes
  hemfikir oldu ve Adım 15'in uzun olduğuna hükmettik. 2000 kelimeden 30 kelimeye düşürdüm. Bu konuyu artık
  kapatıyorum.' Böyle çalışma olmaz. Bütün emekler zayi olur. Hemfikir olarak yapılan eylemin sonucunu da göstermen
  gerekiyor. Sonuç derken kaç kelimeye indiği değil elbette. Olur da bir yanlış anlama olmuş olabilir çünkü."*
  Döngü: **hemfikir → uygulandı → sonuç birebir gösterildi → her okuyucu teyit etti → kapandı.** Biri kayıp ya da
  güç değişimi bulursa düzeltilir ve düzeltilmiş hâli yeniden teyide gider. (İlk örnek: Tur 62'de Adım 14'ün
  listesinden bir yan cümle düşmüştü; Grok yakaladı.) Yazara verilen özette de sonuç anlatılır, sayı değil.
- **Okuyucuların kendi önerileri de istenir.** Yazar, Tur 67: *"Onların da önerileri varsa onlar da söylesinler. Neden
  olmasın? Belki faydalı fikirler çıkar."* Her tur metni, sorulan sorulardan bağımsız olarak **açık bir öneri bölümü**
  taşır (kısaltma, taşıma, yeniden yazım, yapı, fikir — gerekçeli). Gelen öneriler bir sonraki turda herkese **yan
  yana** sunulur ve benim görüşümle birlikte oylanır.
- **Uygulanan her kısaltma bir sonraki tur metninde önce/sonra birebir gösterilir.** Taşınan malzeme
  `paper/v8/supplement.md`'ye aynen gider; gövdede bulgusu ve sınırı kalır.
- **Hız sorunu budamayla çözülmez.** Yazar, Tur 67: *"Ama çözüm senin sunduğun gibi budamak olamaz. … Ama ben en az 6-8
  tur daha makul adımları tercih ediyorum. Belki onlardan güzel fikirler gelir bu arada. Olmazsa da artık, getirmiş olduğum
  eşsiz yenilik anlatılarının dışında kalan hesap kısımları yontmada yeteneğinizi gösterirsiniz :D"* Ben her bölüme kelime
  bütçesi koyup işe birleştirme bölümünden, yani kalpten başlamayı önermiştim. **Kelime sayısı kesimin sürücüsü olmaz;
  yontulacaksa önce yenilik anlatılarının dışındaki hesap kısımları yontulur.** Hız için okuyucuların çözümleri istenir;
  yedek yol `paper/deferred-decisions.md` E4'te.
- **Okuyucular birbirine de cevap verir (yazar, Tur 85).** *"Mesela bir okuyucu ikna olmadı diyelim bir an için. Onunla
  diğer okuyucular da fikir üzerine beyanatları olsun. Yani birbirlerinin olumlu/olumsuz görüşlerine de bir şey söylemek
  isterlerse çekinmesinler."* Her tur metni, ayrışan ya da tek kalan görüşleri **adıyla ve yan yana** koyar ve öteki
  okuyuculardan o görüşlere (yalnız bana değil) cevap ister. İkna olmayan okuyucunun gerekçesi öbürlerine açıkça sorulur.
- **Koruma ölçütü (Tur 87, dört okuyucu + Claude):** *"A sentence is protected when removing it silently would change a
  claim, a limit or a derivation that later text depends on: a derived statement would read as asserted, or a limited claim
  as broader. Being load-bearing for the structure alone is not enough."*
- **Durma kuralı neyi sayar (Tur 87, dört okuyucu + Claude; ChatGPT'nin yazımı):** *"The stop rule counts unresolved or
  newly introduced defects in the current draft. A defect found in the frozen source is recorded and repaired under its own
  trace; it does not count as a draft failure unless the recomposition introduces or fails to repair it."* İz tablosunda her
  bulgu **köken** alanı taşır: **S** (kaynak kusuru) / **R** (yeniden kurmanın kırdığı). Kaynak kusurları
  `paper/v8-source-defects.md`'de. Tur 84'te S-7'yi durma hakkından saymam yanlıştı.
- **Bir okuyucunun penceresi dolarsa (yazar, Tur 91).** *"Sohbet pencere dolarsa bir okuyucunun, sana haber vereceğim. O
  esnada diğer okuyucuların cevaplarını da vereceğim. Ama sen de bana yeni pencereden başlayabilecek şey vereceksin."* →
  `cfd/reader-onboarding.md` **her tur güncel tutulur** (§6 "Where the work stands" her tur yeniden yazılır). Yazar haber
  verince: o okuyucuya **başlangıç metni + güncel tur metni** gider; okuyucunun gecikmeli cevabı gelince bir sonraki turda
  işlenir. Uygulama eşiği değişmez: o okuyucunun oyu gelmeden oylanan madde uygulanmaz.
- **Plan (yazar onayı, Tur 68).** Yapı üretilmiş görünüm olarak birleşir (`paper/build/v8_assemble.py` →
  `paper/v8/ASSEMBLED.md`; kaynak adım dosyaları). Hesap adımları taslakla kısalır: **taslak yeni yüklem eklemez**, her
  cümle kaynak cümlenin yalnız silmeyle kısalmış hâlidir (`paper/build/v8_draft_check.py`); **silme de anlamı ters
  çevirebilir** — silinen olumsuzluk/niteleyici reddedilir. Yazar: *"Grok'un kısaltma konusunda önerileri bazen daha
  isabetli de olabilir."* — kısaltma tariflerinde Grok'un önerisi ağırlıklı okunur; eşik ve veto değişmez.
- **Kısaltma HER YERDEN (yazar, Tur 72).** Qwen'in hesabı (hesaplar sıfıra inse bile gövde hedefin iki katı) yazara
  gitti: *"Gerçekçi olmak durumundayız. Evet haklısınız, uyarıyı yapan arkadaşlar da sen de hepiniz haklısınız.
  Kısaltacaksak heryerden kısalacak. Tamam, o şekilde ilerleyelim lütfen."* → Adım 5–8 artık kısaltmanın dışında
  değil. Ruh kuralı durur: kavrayış yerleşim, sıra ve sesle taşınır; on ruh cümlesi korunur. Sıra: önce hesaplar, sonra
  çerçeve, sonra gerisi. **Ölçüm (Tur 72):** yalnız silme adım başına %7–12; bu yolla gövde ~24 000'de biter. Hedef
  yöntemle ancak **yeniden kurma** (recomposition) ile — önce bir bölümde deneme, veto sayılır (Tur 72 metni §5).
- **Yeniden kurma yöntemi (yazar, Tur 73).** *"Yapayzekaların metin kısaltmada iyi olmadığını biliyorum. Dolayısıyla biraz
  zaman alacak ama olacak Allah'ın izniyle."* Birleşik öneri okuyuculara sunuldu; **kabul ederlerse başlanır.** Kurallar:
  birim bir bulgu bloğu; önce anlam envanteri (söylenecek / gösterilecek / nitelenecek / söylenmeyecek) okuyucu teyidiyle;
  her cümle P/D/J/R etiketli, etiketsiz = R, R cümle cümle vetolu; iz tablosu; özgün adım eke tam; durma: güçlenen yüklem
  ya da düşen sayı → dur, iki+ kırık öncül → hazır değil; sıra 4 → 2–3 (tek bölüm) → 9, 14 → 1 → 5–6 → 7–8 en son.

## 3. Doğrulama

Hiçbir iddia denetlenmeden aktarılmaz — ne YZ'lerinki ne benimki.

- `paper/build/verify.py` — sayısal denetim (45 kontrol) + yasaklı bayat
  değer listesi (yalnız v7 bölümleri).
- `paper/build/v8_stale.py` — v8 İngilizce gövdelerinde emekli ifade/sayı
  denetimi; `--sina` eski hatayı yakaladığını sınar. `v8_all_steps.py` ALL-STEPS.md'yi kurar.
- `paper/build/v8_caveats.py` — kesilemeyecek çekincelerin (`paper/v8-caveats.md`) hâlâ kendi
  adımlarında durduğunu sınar; `--sina` silinen bir çekinceyi yakaladığını sınar.
- `paper/build/v8_assemble.py` — birleştirilmiş görünüm; 150 korunan cümle görünümde mi (`--sina`).
- `paper/build/v8_draft_check.py NN` — taslak yalnız silmeyle mi türedi, olumsuzluk silinmiş mi (`--sina`).
- `paper/build/v8_nothing_lost.py` — kısaltılan adımların her cümlesi gövdede ya da ekte mi (`--sina`). Ek kuralı (Qwen, Tur 69):
  kaybı olan her paragraf eke **tam** ve özgün başlığıyla gider.
- `paper/build/links.py` — bağ dokusu: işaretçiler çözülüyor mu, **doğru
  yere mi** çözülüyor, tablo/şekil atıfları tutuyor mu.
  **DİKKAT (Tur 88):** `links.py` **v7** kâğıdını (`paper-v7.md`) denetler, v8 adımlarını DEĞİL. v8'de "Section X"
  çözülmesini `v8_assemble.py` ("cozulmeyen atif") denetler. Tur 88'e dek v8 için "links temiz" diye raporladığım v7'ydi.
- `paper/build/v8_refs.py` — v8'de tablo/satır atıfları, elle çözülmüş ilişkisel adlar (*the inversion*, *the N-th
  departure*) ve "Supplement S#" atıfları; gözden geçirilmiş liste `paper/v8-refs-reviewed.md` (`--sina`).
- Bir denetim yazdığında **eski hatayı geri koyup yakalayıp yakalamadığını
  sına.** Sessizce boş dönen bir denetim, hiç olmayandan beterdir; bu bir kez
  oldu.

### 3.1 Emekliye ayrılan ifade DEPONUN TAMAMINDA aranır. Tur 49.

Adım 6'da *"different efficiency class"* ifadesini emekliye ayırdım ve gerekçesini
yazdım. **Adım 9'da aynı ifade canlı kaldı** ve üstelik makalenin iddia tablosunda,
*"Claimed"* satırında duruyordu. Dört dış okuyucunun hiçbiri göremezdi — ellerinde
Adım 9 yoktu.

Bu §0.2'nin hata sınıfının yeni bir biçimi: orada **düzeltme yeni bir çelişki
doğuruyordu**, burada **düzeltme hiç yayılmadı.** İkisi de "düzeltirken denetle"
ailesinden.

> **Kural:** bir ifade, bir sayı ya da bir iddia emekliye ayrıldığında, aynı turda
> `grep -rn` ile **bütün v8 adımlarında ve bütün bulgu kayıtlarında** aranır. Her
> örneği düzeltilir. "Değiştirdim" demeden önce arama çıktısı görülür.
>
> Aynısı sayılar için zaten var (`verify.py`'nin bayat değer listesi). **İfadeler
> için yoktu.** Yeni bir ifade emekliye ayrıldığında o listeye de eklenmeli.

**GENİŞLETME, Tur 50 — aynı sınıf ÜÇÜNCÜ kez, ve bu kez bir betik yüzünden.**
Adım 6'ya *"e = 0,817 kullanılıyor"* yazdım, ama aynı sayfadaki L/D_max sayıları
11,88 ve 10,28 idi — yani **e = 0,85 değerleri.** Doğrusu 11,65 ve 10,08, ve bunları
bir tur önce **kendim hesaplamıştım.** Betiği düzelttim; **düzyazıyı düzeltmedim.**
Üç dış okuyucu bağımsız olarak yakaladı.

> **Bir betik düzeltildiğinde, o betiğin çıktısını alıntılayan HER düzyazı aynı turda
> yeniden okunur.** Betik artık doğru olduğu için sayının doğru olduğunu varsayma;
> sayı düzyazıya **elle** kopyalanmıştı ve orada kalır.

**VE ÇEKİNCENİN YERİ. Grok, Tur 50.** Adım 8'in bayat watt'ları bir kez yakalanıp
etiketlenmişti — ama etiket **Türkçe denetim tablosundaydı.** Dış okuyuculara giden
pakette o tablolar çıkarılıyor, dolayısıyla okuyucu etiketi **hiç görmedi** ve sayılar
güncelmiş gibi durdu.

> **Bir çekince yalnız Türkçe denetim tablosunda duruyorsa, İngilizce gövdede yok
> demektir.** Makaleye girecek her nitelendirme **gövdeye** yazılır. Türkçe tablo
> yazarın denetimi içindir, okuyucunun uyarısı için değil.

**GENİŞLETME, Tur 68 — şekil etiketi de metindir.** v7'nin Şekil 11'i v8'in geri aldığı üç ifadeyi taşıyor
(*"nothing on the aircraft rotates relative to it"*, *"no altitude loss"*, *"reverse of transition"* —
`figures/build/mkfig11.py`). Şekiller hiçbir tur metnine girmediği için hiçbir okuyucu göremezdi; emekli ifade taraması
da şekilleri kapsamıyor. **Kural:** bir v7 şekli v8'e ancak etiketi, alt başlığı ve altyazısı korunan cümlelere ve emekli
ifade listesine karşı metin gibi denetlendikten sonra girer; girdiği anda `v8_stale.py` taramasına eklenir.

### 3.2 Ertelenmiş kararlar unutulmaz. Tur 50.

Yazar: *"Ben unutabilirim sen sağa sola notunu al."*

> **`paper/deferred-decisions.md`** — yazarın açıkça *"sonraya"* dediği her şey oraya yazılır,
> ve **her tur sonunda o listeye bakılır.** Şu an açık olan ikisi: **kısaltma/oran** (10–14
> yazıldıktan sonra, tek seferde) ve **"zero-bill condition" adı.**

### 3.3 Bir modülü başka ölçekte koşturmak. Tur 55.

`aero/heavy_rotor.py`, `tip_propeller`'ın modül sabitlerini ağır değerlerle değiştirip aynı
fonksiyonları çağırıyordu. **Üç değer değişmedi:** varsayılan argüman (`V=V_SEYIR`, tanım anında
bağlanır), imzadaki sabit (`om=2100.0`), ithal anında türetilmiş sabit (`r_h`). Ağır rotor terimi
yanlış mekanizmayla v7'ye, Zenodo'ya ve Adım 12'ye girdi. **`verify.py` aynı çağrıyı yaptığı için
hatayı doğruladı.** DeepSeek'in bir fizik sorusu (*"sabit rotorda q sadeleşmeli"*) açtı.

> **Kural:** bir betik başka bir modülü başka koşulda koşturuyorsa, çağrılan fonksiyonların
> kullandığı **her koşul değeri çıktının başına basılır** (hız, devir, göbek, referans alan).
> Ve denetlediği hesabı aynı çağrıyla tekrarlayan bir denetim denetim değildir: **eski hatayı
> REDDETTİĞİ ayrıca sınanır.**

## 4. Depo

- Geliştirme dalı: `claude/ecstatic-cori-6w30at`. `main` de güncel tutulur.
- **Başka hiçbir repository'ye dokunulmaz.** Başkalarının uzun emeği var.
- Yayın: Zenodo (kök DOI 10.5281/zenodo.22144194).
- **Hedef dergi: *Journal of Aircraft* (AIAA).** *Drones*'a gönderildi
  (`drones-4595522`, 2026-09-14), kapsam dışı bulunup *Aerospace*'e aktarıldı,
  orada da aynı gün masadan reddedildi. **Hakeme hiç gitmedi.** Kayıt:
  `paper/drones-submission.md` §10, hedef denetimi `paper/target-journal.md`.
- **Dergi şartı kuralı — bu bedeli bir kez ödedik.** Bir hedef dergi adı
  konmadan önce o derginin aims, scope ve özel şartları **baştan sona okunur**
  ve şart şart makaleyle karşılaştırılıp yazılır. *Drones*'un kapsam sayfasında
  *"genel teorik uçak tasarımı makaleleri için en azından laboratuvar ölçeğinde,
  insansız bir platformdan deneysel veriyle doğrulama"* şartı yazılıydı; hiç
  açmadım. Makaleyi kendine karşı denetleyip gideceği yere karşı hiç
  denetlemeyen bir düzen, yanlış şeyi denetliyor demektir.
- **v8 yeniden kurgulanır, kısaltılmaz.** Ve dergi gövdesinde *"bir önceki
  sürümde şöyleydi"* anlatısı **bulunmaz** — makale tek başına yeter olmalıdır;
  düzeltme tarihi depoda durur. Gerekçesini o anlatının içinde taşıyan sayılar
  gerekçeleriyle birlikte **şimdiki zamanda yeniden yazılır**, silinmez.
- YZ kullanım beyanında **marka/model/şirket adı geçmez**; YZ yazar satırında
  asla yer almaz.
- Uygulama alanları: **orman yangını gözlem/müdahale** ve **piste ihtiyaç
  duymayan yerlere kargo.**
