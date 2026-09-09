# meryemAircraft

**Kuyruğuna oturan, kanat-gövde biçimli, kumanda yüzeyi bulunmayan bir insansız hava
aracı konfigürasyonu — ve onun üzerinden kurulan bir maliyet çerçevesi.** Bu depo,
tasarımın kaydını, ondan üretilen bilimsel makaleyi ve makaledeki her sayıyı yeniden
üreten betikleri barındırır.

Aracın tüm itkisi burundaki **tek bir eş eksenli karşıt dönüşlü pervane çiftinden**
gelir; kanat uçlarındaki dört küçük çift yalnızca yönelim momenti üretir; gövde
altındaki aç-kapa bir **şeride**, gövde eksenine paralel itki vektörlerinin
üretemediği yalpa momenti **atanmıştır**. Elevon, dümen, eğilme mekanizması, geri
çekme mekanizması ve ayrı bir kaldırma sistemi yoktur.

---

## Makale

**The Architectural Cost of Hybrid VTOL: meryemAircraft, a Propeller-Driven
Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System**
Meryem Gülmen, Berke Gülmen, Ömer Gülmen · 2026

Hibrit VTOL hava araçları piste bağımsızlığı kanatla seyirle birleştirir ve bunun
bedelini seyir verimliliğinden öder. Makale bu bedeli bir uygulama kusuru değil
**mimari** sayar ve bir muhasebe çerçevesi olarak kurar: bedel üç para biriminde
tahakkuk eder — seyirde taşınan askı donanımının **kütlesi**, açıkta kalan askı
donanımının **sürüklemesi**, ve uçuşun yaklaşık yüzde ikisinde geçerli bir koşula
göre boyutlandırılmış **güç sistemi**. Burada taranan her çare bunlardan birini
azaltırken bir diğerini artırır. Bedeli böyle ifade etmek, ondan kaçınma koşulunu
açık eder. İkinci bir sonuç yöntemseldir: mimari karşılaştırmalar seçilen
**boyutlandırma sözleşmesine** bağlıdır, ve sabit yakıt kesri kütle faturasını menzil
sütunundan tümüyle siler — bu yüzden tek sözleşme değil üçü birden raporlanır.
meryemAircraft, kaçınma koşulunu sağlayan **vaka analizidir**.

| | |
|---|---|
| DOI (her zaman son sürüm) | [10.5281/zenodo.22144194](https://doi.org/10.5281/zenodo.22144194) — şu an **v4** |
| v4 kaydı | <https://zenodo.org/records/22664634> |
| İlk sürüm (v1, değişmez) | [10.5281/zenodo.22144195](https://doi.org/10.5281/zenodo.22144195) |
| PDF | [`makale/pdf/meryemAircraft-makale.pdf`](makale/pdf/meryemAircraft-makale.pdf) — 71 sayfa, 12 şekil |
| Tek dosya kaynak | [`makale/makale.md`](makale/makale.md) |
| Bölüm bölüm | [`makale/bolumler/`](makale/bolumler/) |
| Kaynakça | [`makale/kaynakca-en.md`](makale/kaynakca-en.md) |
| Hedef dergi | **Drones** (MDPI) — ilk gönderim; gerekçe ve bilinen risk [`makale/00-yol-plani.md`](makale/00-yol-plani.md) |

---

## Neyin gösterildiği, neyin gösterilmediği

Bu, deponun en önemli bölümüdür. Makale bir **konfigürasyon çalışmasıdır**; rüzgâr
tüneli ve uçuş verisi **yoktur**. Aşağıdaki ayrım makalenin her yerinde tutulur ve
burada da tutulur.

| | durum |
|---|---|
| Üç faturalı çerçeve ve kaçınma koşulu | **kurulmuş**; bağımsız yayımlanmış bir boyutlandırma çalışmasına karşı tutarlılık sınamasından geçiyor |
| Üç boyutlandırma sözleşmesi | **hesaplanmış**; tek sözleşmeden çıkan sıralamaların neden aldatıcı olduğu gösteriliyor |
| Statik yunuslama kararlılığı | **gösterilmiş** — girdap kafes, tarafsız nokta MAC'in %34,4'ü, marj +%12,5 (yakınsamış) |
| Seyirde denge (trim) | **gösterilmemiş** — gereken kamber momenti 0,056 olarak *nicelenmiş*; kamber/refleks dağılımı tanımlı değil |
| Yatış otoritesi | **gösterilmemiş** — atalet (25,0 kg·m²) ve sönümleme (\|C_l_p\| = 0,358) bu planform için hesaplandı; 20°/s için 27,1 N·m gerekiyor, şeridin kendi kuvveti bunun ~üçte birini veriyor, gerisi ΔC_L ≈ 0,12 *gereksinimi* |
| Sapma otoritesi | **rahat** — kol yarı açıklık olduğu için yunuslamanınkinin 2,43 katı (55,9 N·m'ye karşı 23,0) |
| Yön kararlılığı | **gösterilmemiş** — planform C_n_β = 0 veriyor; uç çerçevesi fairing'inden gelmek zorunda, gereken veter 21–34 mm |
| Geçiş kontrol edilebilirliği | **açık** — uç pervaneler ataleti döndürüyor, aerodinamik momenti döndürdükleri gösterilmedi. Çalışmanın en büyük açık kalemi |
| Kütle bütçesi, 50 kg | **koşullu kapanıyor** — kabuk yüzey yoğunluğu ≤ 1,78 kg/m² kalırsa 2,2 kg pay; 1,5 kg/m² bir hedeftir, ölçüm değil |
| Kütle bütçesi, 1000 kg | **kapanmıyor** — ağır nokta bir ölçek uzantısıdır, ikinci bir tasarım noktası değil |
| Sıfır taşıma sürüklemesi | **sınırlanmış, değiştirilmemiş** — 3B çözüm C_D0 = 0,0141 ± ~%5 veriyor; varsayılan 0,0248 hâlâ üstünde |

Kısacası: **yönelim kontrolü her eksende boyutlandırılmış, hiçbir eksende
kapatılmamıştır.** Makale bunu böyle yazar.

---

## Ne var burada

```
makale/     Makale: bölümler, tek dosya kaynak, PDF, kaynakça, yol planı
  uretim/     Derleyici ve doğrulama betiği
aero/        Bağımsız hesaplar — her biri kendi gerekçesini ve sınırını yazar
gorsel/     On iki şekil
  kaynak/     Parametrik geometri modeli
  uretim/     Şekilleri ve geçiş benzetimini üreten betikler
  cikti/      Yayına hazır png / svg
cfd/        OpenFOAM kurulumu, doğrulama kaydı ve dış değerlendirme yazışmaları
patent/     Türkiye patent başvurusunun metinleri ve çizimleri
tasarim/    Tasarım künyesi — her kararın, verildiği andaki gerekçesiyle kaydı
kaynakca/   Okunan literatürün kaydı
sunum/      Sunum malzemesi
video/      Görselleştirme
```

## Yeniden üretilebilirlik

Makaledeki her sayı ve her şekil bu depodaki betiklerden yeniden üretilebilir.

| Betik | Ne yapar |
|---|---|
| `makale/uretim/mkmakale.py` | Bölümleri, şekilleri ve kaynakçayı tek PDF'te derler |
| `makale/uretim/dogrula.py` | **Makalenin her başlık sayısını, makalenin kendi denklemleriyle bağımsız hesaplayıp metinle karşılaştırır** |
| `aero/planform.py` | Ok açısı yasalarından planformu yeniden kurar; künye değerleriyle sınar |
| `aero/temel.py` | Üç mimarinin kapalı çevrim boyutlandırması ve üç sözleşme |
| `aero/kutle.py` | Bileşen bileşen kütle bütçesi, kabuk yoğunluğu başabaşı, tampon sınaması |
| `aero/vlm.py` · `aero/cd0.py` | Girdap kafes ve `C_D0` kurulumu |
| `aero/kararlilik.py` | Tarafsız nokta, statik marj, denge gereksinimi, **konvansiyon denetimi** |
| `aero/donme.py` · `aero/zarf.py` | Geçiş dönme dinamiği ve tasarım zarfı |
| `aero/yatis.py` | Yatış ataleti, sönümlemesi, otorite gereksinimi, aç-kapa sınır çevrimi |
| `aero/sapma.py` | Sapma ataleti, otoritesi, yön kararlılığı gereksinimi |
| `aero/hacim.py` · `aero/duyarlilik.py` | Hacim kapanışı ve eğim duyarlılığı |
| `gorsel/uretim/gecis2.py` | Geçiş benzetimi — iki serbestlik dereceli nokta kütle |
| `gorsel/uretim/mkfig*.py` · `mkconcept.py` | On iki şeklin üreticileri |
| `gorsel/uretim/figlib.py` | 3B modeli başsız Chromium'da açar, kamerayı sürer, görüntü alır |

`dogrula.py` şu an **40 kontrol** ve geçiş tablolarının **52 hücresini** sınıyor;
sapma yok. Betik, derleme sırasında iki tablonun bayat kaldığını ve bir yerde
momentin itkiyle karıştırıldığını yakaladı.

**Bağımlılıklar:** `python3`, `matplotlib`, `pillow`, `markdown`, `playwright`
(başsız Chromium — üç boyutlu şekiller ve PDF için); `aero/` için ayrıca
`aerosandbox` ve `neuralfoil`.

Betikler bulundukları yerden çalışır; depo dışında bir yola ihtiyaç duymazlar.
Üç boyutlu şekiller `gorsel/kaynak/govde-etudu.html` modelinden üretilir:
`figlib.py` modelin bir **kopyasına** render kancası enjekte eder, kaynak dosya
değiştirilmez. Chromium başka bir yerdeyse `CHROME_PATH` ile gösterilebilir.

## Dış değerlendirme kaydı

Makale, gönderimden önce birbirinden bağımsız üç dil modeline **tur tur** okutuldu
ve her turun metni [`cfd/dis-gorus-*.md`](cfd/) altında saklandı. Bu bir doğrulama
değil, bir **hata avıdır** ve avın kayıtları tutulmuştur — bulunan hatalar
düzeltilmekle kalmayıp `aero/README.md` içinde neyin neden yanlış olduğuyla birlikte
yazılıdır. Süreçte çöken iddialar arasında şunlar var: yunuslama momentinin 4TL değil
**2TL** olduğu; ağırlık merkezinin elle yerleştirilmesinin saçma bir statik marj
verdiği; statik marjla denge gereksiniminin **iki farklı referans veterle**
yazıldığı; ve §4.4'ün 46 N·m'lik yatış momentinin şeridin kendi kuvvetinden
**gelemeyeceği**.

## Kaynak kullanımı

Sayısal ve tarihsel iddiaların tamamı **birinci elden okunan** kaynaklara
dayandırılmıştır; okunmayan kaynaklara hiçbir sayı bağlanmamıştır. Bu ayrım
makalenin 8. bölümünde açıkça yazılıdır. `makale/kaynaklar.md`, hangi kaynağın ne
düzeyde doğrulandığını ve arama motoru özetlerinden gelen **üç yanlış sayının**
birinci el okumayla nasıl yakalandığını kaydeder.

## Sürüm geçmişi

| Sürüm | Tarih | Öz |
|---|---|---|
| **v4** | 2026-09-08 | Çerçeve merkezli yeniden kurgu; kabiliyet cümleleri gereksinim diline çevrildi. Üç kontrol ekseni denetlendi: yunuslama (CG hacim ağırlıklı, marj +%12,5, denge 0,056), yatış (46 N·m çöktü, ΔC_L ≈ 0,12 gereksinimine dönüştü), sapma (otorite 2,4 kat, yön kararlılığı fairing'e bağlı). İki referans veter birleştirildi; dönme süreleri "pay" değil **eyleyici sınırlı alt sınır** oldu. |
| v3 | 2026-09-05 | Merkez gövde için 3B çözüm: kanat/gövde C_D0 = 0,0141 ± ~%5, varsayılan 0,0248 hâlâ üstünde. 8.1 "No experimental validation" oldu. |
| v2 | 2026-08-29 | Menzil yöntemi düzeltildi (azami L/D yerine seyir noktası poları): 1 695 → **1 598 km**. Bölüm 6.6 eklendi; hacim kapanışı yapıldı. |
| v1 | 2026-08 | İlk yayım. |

Yayımlanmış sürümler **değişmez**; her biri kendi DOI'siyle erişilebilir durumdadır.

## Patent

Konfigürasyon için Türkiye'de patent başvurusu yapılmıştır (2026-08). `patent/`
altındaki metinler ve çizimler başvuruya esas alınan taslaklardır. Bir patent
vekili tarafından hazırlanmamıştır.

## Lisans

Metin, şekiller ve betikler: **AGPL-3.0** — bkz. [LICENSE](LICENSE).
Makalenin Zenodo'daki sürümü **CC BY 4.0** ile yayımlanmıştır.

---

*Yapay zekâ araçları bu çalışmanın hazırlanmasında literatür taraması, sayısal
denetim ve dil düzeltmesi için kullanılmıştır. Tüm tasarım kararları, mühendislik
yargıları ve iddialar yazarlara aittir.*
