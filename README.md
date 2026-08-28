# meryemAircraft

**Kuyruğuna oturan, kanat-gövde biçimli, kumanda yüzeyi bulunmayan bir insansız hava
aracı konfigürasyonu.** Bu depo, o tasarımın kaydını ve ondan üretilen bilimsel
makaleyi barındırır.

Aracın tüm itkisi burundaki **tek bir koaksiyel karşıt dönüşlü pervane çiftinden**
gelir; kanat uçlarındaki dört küçük çift yalnızca yönelim momenti üretir; gövde
altındaki aç-kapa bir **şerit**, gövde eksenine paralel itki vektörlerinin
üretemediği yuvarlanma momentini sağlar. Elevon, dümen, eğilme mekanizması, geri
çekme mekanizması ve ayrı bir kaldırma sistemi yoktur.

---

## Makale

**Eliminating the Cruise-Efficiency Penalty of Hybrid VTOL: The meryemAircraft
Tail-Sitting Blended-Wing-Body Configuration with Propeller-Only Control**
Meryem Gülmen, Berke Gülmen, Ömer Gülmen · 2026

Hibrit VTOL hava araçları, piste bağımsızlığı kanatla seyir yeteneğiyle birleştirir
ama bunu seyir verimliliğinden ödeyerek yapar. Makale, bu bedelin bir uygulama kusuru
değil **mimari** olduğunu savunur ve üç para biriminde ödendiğini gösterir: seyirde
taşınan askı donanımının kütlesi, seyirde açıkta kalan askı donanımının sürüklemesi,
ve uçuşun yaklaşık yüzde ikisinde geçerli bir koşula göre boyutlandırılmış güç
sistemi. Bilinen her mimari çare bu üçünden birini azaltırken bir diğerini artırır.
Bedeli bu biçimde ifade etmek, ondan kaçınma koşulunu da açık eder — ve makale o
koşulu sağlayan bir konfigürasyon önerir.

| | |
|---|---|
| DOI | [10.5281/zenodo.22144194](https://doi.org/10.5281/zenodo.22144194) — her zaman en son sürüme gider |
| Bu sürüm (v1) | [10.5281/zenodo.22144195](https://doi.org/10.5281/zenodo.22144195) |
| PDF | [`makale/pdf/meryemAircraft-makale.pdf`](makale/pdf/meryemAircraft-makale.pdf) — 44 sayfa, 12 şekil |
| Tek dosya kaynak | [`makale/makale.md`](makale/makale.md) |
| Bölüm bölüm | [`makale/bolumler/`](makale/bolumler/) |
| Kaynakça | [`makale/kaynakca-en.md`](makale/kaynakca-en.md) |

> ⚠️ **Çalışma analitiktir.** Rüzgâr tüneli, hesaplamalı akışkanlar dinamiği ya da
> uçuş denemesi verisi **yoktur**; sayılar, belirtilen varsayımlardan türetilmiş
> analitik kestirimlerdir ve kütle bütçesi bir hedeftir, bulgu değil. Makalenin
> 8. bölümü bu sınırları tek tek sayar, 8.12 ise bu sonuçları sınayacak dört
> analizi listeler. Hiçbiri deney gerektirmez.

---

## Ne var burada

```
makale/     Makale: bölümler, tek dosya kaynak, PDF, kaynakça
  uretim/     Derleyici ve doğrulama betiği
gorsel/     On iki şekil
  kaynak/     Parametrik geometri modeli
  uretim/     Şekilleri ve geçiş benzetimini üreten betikler
  cikti/      Yayına hazır png / svg
patent/     Türkiye patent başvurusunun metinleri ve çizimleri
tasarim/    Tasarım künyesi — her kararın, verildiği andaki gerekçesiyle kaydı
kaynakca/   Okunan literatürün kaydı
```

## Yeniden üretilebilirlik

Makaledeki her sayı ve her şekil bu depodaki betiklerden yeniden üretilebilir.
Bu, 8.12'deki *"başka bir grup bunu bağımsız olarak deneyebilir"* davetinin
somut karşılığıdır.

| Betik | Ne yapar |
|---|---|
| `makale/uretim/mkmakale.py` | Bölümleri, şekilleri ve kaynakçayı tek PDF'te derler |
| `makale/uretim/dogrula.py` | **Makalenin her başlık sayısını, makalenin kendi denklemleriyle bağımsız hesaplayıp metinle karşılaştırır** |
| `gorsel/uretim/gecis2.py` | Geçiş benzetimi — iki serbestlik dereceli nokta kütle |
| `gorsel/uretim/mkfig*.py` | On iki şeklin üreticileri |
| `gorsel/uretim/figlib.py` | 3B modeli başsız Chromium'da açar, kamerayı sürer, görüntü alır |
| `gorsel/uretim/mklinkedin.py` | Paylaşım kartı |

`dogrula.py` şu an **38 kontrol** ve geçiş tablolarının **52 hücresini** sınıyor;
sapma yok. Betik, derleme sırasında iki tablonun bayat kaldığını ve bir yerde
momentin itkiyle karıştırıldığını yakaladı.

**Bağımlılıklar:** `python3`, `matplotlib`, `pillow`, `markdown`, `playwright`
(başsız Chromium — üç boyutlu şekiller ve PDF için).

Betikler bulundukları yerden çalışır; depo dışında bir yola ihtiyaç duymazlar.
Üç boyutlu şekiller `gorsel/kaynak/govde-etudu.html` modelinden üretilir:
`figlib.py` modelin bir **kopyasına** render kancası enjekte eder, kaynak dosya
değiştirilmez. Chromium başka bir yerdeyse `CHROME_PATH` ile gösterilebilir.

## Kaynak kullanımı

Sayısal ve tarihsel iddiaların tamamı **birinci elden okunan** kaynaklara
dayandırılmıştır; okunmayan kaynaklara hiçbir sayı bağlanmamıştır. Bu ayrım
makalenin 8.11'inde açıkça yazılıdır. `makale/kaynaklar.md`, hangi kaynağın ne
düzeyde doğrulandığını ve arama motoru özetlerinden gelen **üç yanlış sayının**
birinci el okumayla nasıl yakalandığını kaydeder.

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
