# meryemAircraft — çalışma kuralları

## 0. İDDİANIN NE OLDUĞU. Bunu bir daha kaçırma.

Bu çalışmanın **var oluş nedeni mimari yeniliktir.** Menzil rekoru değildir.
Aşağıdaki dört satır projenin omurgasıdır ve her metin, her düzeltme, her
özet bunlarla tutarlı olmak zorundadır.

**Rakip kim, hangi eksende — dördü de ayrı:**

| Eksen | Rakip | Durum |
|---|---|---|
| **Menzil / seyir verimi** | **Çok rotorlu (quadcopter)** | **Yeniyoruz. Yeter.** |
| **Piste ihtiyaç / dikey iniş kalkış** | **Sabit kanatlı** | **Yeniyoruz. İnşa gereği.** |
| **Mekanik ve kontrol basitliği** | **Tilt mimarileri** | **Asıl katkı bu.** |
| Menzil, öteki hibritlere karşı | Lift+cruise, tilt | **İDDİA EDİLMİYOR.** Sözleşmeye göre tersine döner. |

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

**Sayılar değişmez.** Menzil açığı 24–45 %, kütle üstünlüğü 32–36 %, bunların
hepsi dürüstçe raporlanmaya devam eder. Değişen şey **neyin iddia edildiğidir.**
Öteki hibritlere karşı menzil sıralaması bir boyutlandırma sonucudur, tez
değildir.

**"Genel mimari üstünlük iddiası yoktur" gibi bir cümle bir daha yazılmaz.**
Bir kez yazıldı, 4.2 ile çelişti ve makalenin kendi tezini inkâr etti.

### 0.1 Üçüncü iddianın SINIRI. Bunu da bir daha aşma.

İddiayı düzeltirken hemen aşırıya kaçtım ve **makalenin kendi §2.10'uyla çelişen**
bir cümle yazdım: *"hareket eden mekanizma yok", "hiçbir aerodinamik kumanda
yüzeyi yok", "her eksendeki her moment diferansiyel itkiden".* Üçü de **yanlış.**

**Yatış (roll) eşeksenli pervanelerle ÜRETİLEMEZ.** §2.10 bunu türetiyor: her
çift eşeksenli ve tork dengeli, hiçbir ayar yatış momenti vermiyor. Yatışı alt
yüzeydeki **değişken uzantılı şerit** sağlıyor ve makale ona *"uçaktaki tek
hareketli aerodinamik yüzey"* diyor.

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

## 3. Doğrulama

Hiçbir iddia denetlenmeden aktarılmaz — ne YZ'lerinki ne benimki.

- `paper/build/verify.py` — sayısal denetim (43 kontrol) + yasaklı bayat
  değer listesi.
- `paper/build/links.py` — bağ dokusu: işaretçiler çözülüyor mu, **doğru
  yere mi** çözülüyor, tablo/şekil atıfları tutuyor mu.
- Bir denetim yazdığında **eski hatayı geri koyup yakalayıp yakalamadığını
  sına.** Sessizce boş dönen bir denetim, hiç olmayandan beterdir; bu bir kez
  oldu.

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
