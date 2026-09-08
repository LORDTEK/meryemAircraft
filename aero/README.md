# Aerodinamik hesap — ikinci sürümün zemini

Makalenin 8.12'si, sonuçları sınayacak dört analiz sayıyor. Bu dizin ilk
ikisini yürütüyor: **varsayılan aerodinamik katsayıları hesaplanmışla
değiştirmek.**

Çözücü: [AeroSandbox](https://github.com/peterdsharpe/AeroSandbox) girdap-kafes
yöntemi (VLM). Kendi çözücümüzü yazmadık — hakemin "çözücünü doğruladın mı?"
sorusunun karşılığı, yerleşik ve bağımsız bir kod kullanmaktır.

## Betikler

| Betik | Ne yapar |
|---|---|
| `planform.py` | Planformu makalenin ok açısı yasalarından yeniden kurar; künye değerleriyle karşılaştırır |
| `vlm.py` | Girdap-kafes çözümü: kaldırma eğrisi eğimi ve açıklık verimi |
| `duyarlilik.py` | Geçiş tablolarının, hesaplanmış eğime dayanıp dayanmadığını sınar |

`python3 planform.py` — planform açıklık, alan, AR, uç veteri ve uç ok açısını
künyeyle **%0,2'nin altında** farkla yeniden üretiyor.

## Çözücü doğrulaması

Kendi geometrimize uygulamadan önce, bilinen bir hâl üzerinde sınandı:
AR = 6 dikdörtgen kanat, NACA 0012.

| şerit × veter | CL_α (/rad) | e |
|---:|---:|---:|
| 12 × 8 | 4.325 | **1.028** |
| 24 × 10 | 4.268 | 1.006 |
| 40 × 12 | 4.244 | 0.997 |
| 80 × 16 | 4.225 | 0.990 |

Kaba kafeste **e > 1** çıkıyor — fiziksel olarak imkânsız, indüklenen
sürüklemenin yetersiz çözünürlükte az tahmin edilmesinin klasik belirtisi.
40 şeritten sonra fiziksel aralığa oturuyor ve değişim %0,5'in altına iniyor.
Kendi planformumuzda da aynı yakınsama taraması yapıldı; 78 şerit kullanıldı.

## Bulgular

### 1. Açıklık verimi — varsayım doğrulandı, çürütülmedi

VLM, planformumuz için **e = 0,995** veriyor. Makale **0,85** varsayıyor.
**Bu ikisi aynı büyüklük değildir ve fark bir hata değildir.**

VLM'in verdiği, *ağdasız* açıklık verimidir: yalnızca indüklenen sürüklemenin
eliptik dağılımdan ne kadar saptığını ölçer. Makaledeki 0,85 ise sürükleme
polarındaki Oswald tipi bir katsayıdır ve kaldırmaya bağlı **ağdalı**
sürüklemeyi de içerir; temiz bir kanatta ağdasız değerin yaklaşık %85–90'ı
olur. 0,995 × 0,86 ≈ 0,85.

Yani hesap, varsayımı **yerinde çıkarıyor**. "Hesapladık, varsaydığımızdan
iyiymiş" demek yanlış olurdu — farklı iki büyüklüğü karşılaştırmak olurdu.

### 2. Kaldırma eğrisi eğimi — benzetim %18 fazla varsayıyor

| | CL_α |
|---|---:|
| `gecis2.py` varsayımı, 2π/(1+2/AR) | 4,72 /rad |
| VLM hesabı | **3,87 /rad** |

Fark %18 ve yön kötü tarafa: benzetim, geçiş sırasında kaldırmanın gerçekte
olduğundan hızlı toparlandığını sanıyor.

### 3. Ama geçiş sonuçları buna dayanıyor

`duyarlilik.py` iki eğimle de tabloları üretiyor. En büyük sapma **4,0 m** ve o
da makalede referans olarak verilmeyen bir noktada (hafif hat, 1 s dönüş,
w₀ = 5 m/s). Yayımlanmış tablolardaki değişim en çok **1,2 m**.

**Referans profillerin ikisi de — hafif hat 2 s, ağır hat 4 s, w₀ = 5 m/s —
her iki eğimde de sıfır irtifa kaybı veriyor.** Bölüm 7.4'ün savı, kaldırma
eğrisi eğimindeki %18'lik hataya dayanacak kadar sağlam.

### 4. `C_D0` bileşen bileşen kuruldu

`cd0.py` şerit yöntemiyle kanat/gövdeyi, `ozet.py` sonuçları toplar. Kesit
sürükleme katsayıları NeuralFoil'den (XFOIL üzerine eğitilmiş) **sıfır
kaldırmada** alınıyor — `C_D0`'ın tanımı budur.

İki yüzey senaryosu ayrı ayrı hesaplandı: *serbest geçiş* (temiz, cilalı;
XFOIL'in kendi tahmini — iyimser) ve *tetikli geçiş* (geçiş %5 veterde
zorlanır; üretilmiş, boyalı bir yüzey için gerçekçi).

**Hafif hat, 50 kg:**

| bileşen | serbest | tetikli |
|---|---:|---:|
| kanat / gövde | 0,00729 | 0,01285 |
| uç iskeletleri (kaportalı) | 0,00431 | 0,00431 |
| uç pervane göbekleri (30–50 mm) | 0,00171–0,00476 | aynı |
| **C_D0** | **0,0133** | **0,0189 – 0,0241** |

Çerçeve terimi **0,00431** çıkıyor; makalenin 5.2'sinde bağımsız olarak
hesaplanmış **0,0043** ile örtüşüyor. Ağır hatta da aynı değer çıkıyor —
6.4'ün "çerçeve sürükleme payı ölçekle korunur" savının doğrulanması.

**Makalenin varsaydığı 0,0248, hesaplanan aralığın en üstünde ya da biraz
üzerinde.** Varsayım kötümserdi; hesap onu çürütmüyor, sınırlıyor.

### 5. Ama bir tutarsızlık çıktı: azami L/D ile seyir L/D'si karışmış

Makale `L/D ≈ 0,5√(π·AR·e/C_D0)` kullanıyor. Bu bağıntı **azami** L/D'yi verir
ve o da belirli bir kaldırma katsayısında (C_L = √(C_D0·π·AR·e)) oluşur.
Hafif hat için bu C_L = 0,632, yani **25,3 m/s**. Oysa seyir hızı **30 m/s**
olarak belirlenmiş; orada C_L = 0,450 ve gerçek L/D **12,03**, 12,74 değil.

Menzil bu yüzden **%5,6 fazla** hesaplanmış. Ama `C_D0` da fazla varsayıldığı
için iki hata ters yönde çalışıyor ve büyük ölçüde birbirini götürüyor:

| | C_D0 | seyirde L/D | menzil |
|---|---:|---:|---:|
| kötümser hesap | 0,0241 | 12,26 | 1 634 km |
| **makale** | 0,0248 | 12,70 | **1 695 km** |
| orta hesap | 0,0189 | 14,30 | 1 907 km |
| iyimser hesap | 0,0133 | 17,38 | 2 317 km |

Yayımlanmış 1 695 km, hesaplanan aralığın **alt ucuna yakın** duruyor. Ağır
hatta da aynı: yayımlanan 1 868 km'ye karşı 1 801 – 2 425 km.

**Düzeltildi (v2).** İki seçenek vardı: seyir hızını azami L/D noktasına
çekmek (25,3 m/s), ya da menzili gerçek seyir L/D'siyle hesaplamak. Birincisi
tutunma hızının yalnızca 1,26 katına iner — geçiş için fazla dar bir pay.
Bu yüzden ikincisi seçildi: seyir hızı 30 m/s'de kaldı, menzil seyir noktası
polarından hesaplandı. Yayımlanan değerler **1 598 km** (hafif) ve
**1 814 km** (ağır).

## Bu kurulumun sınırları

Bunlar hesabın zayıf yerleri; sıraları önem sırasıdır.

1. **En zayıf halka: gövde bir profil değildir.** Şerit yöntemi kök kesitini
   %25 kalınlığında iki boyutlu bir NACA profili gibi ele alıyor. Kanat-gövde
   merkez gövdesinde akış iki boyutlu değildir. Kanat terimi toplamın en büyük
   parçası olduğu için bu, kurulumun baskın belirsizliğidir.
2. **Kesitler simetrik alındı.** Makalenin tarif ettiği kamber ve refleks
   dağılımları burada yok. Sıfır kaldırma sürüklemesi ılımlı kambere birinci
   mertebede duyarsızdır, ama duyarsız demek bağımsız demek değildir.
3. **Ok açısı düzeltmesi yok.** Şeritler serbest akışa dik alındı; basit ok
   açısı kuramı kesit üzerindeki etkin hızı düşürürdü.
4. **Girişim ve bağlantı sürüklemesi** yalnızca %10'luk artık payı içinde.
5. ~~**Göbek ölçüleri seçilmedi**~~ — **çözüldü, aşağıya bakınız.**

### 6. Göbek ölçüsü piyasadan bağlandı

Her uç rotoru 8 inç pervanede **0,83 kgf** ve **168 W** vermeli. Bu, 22 mm
statorlu standart sınıfın tam ortası. Piyasadaki karşılıkları:

| motor | dış kovan çapı | ağırlık | not |
|---|---:|---:|---|
| T-Motor MT2216 (V2) | **27,8 mm** | 75 g | 22×16 stator, 8–10 inç pervane sınıfı |
| 2212 920 KV (yaygın) | 28 mm | 60 g | 9 inç pervanede ~0,5 kgf — bizim için **küçük kalır** |

Yani gerçekçi kovan çapı **28 mm**, montaj ve kaporta payıyla en fazla 32 mm.
Önceki 50 mm üst sınırı gereksiz kötümserdi. Bu, göbek terimini
**0,0048'den 0,0015 – 0,0020'ye** indiriyor ve `C_D0` aralığını daraltıyor:

| hal | C_D0 | seyirde L/D | menzil |
|---|---:|---:|---:|
| iyimser (temiz yüzey, 28 mm) | 0,0131 | 17,53 | 2 337 km |
| orta (tetikli, 28 mm) | 0,0187 | 14,41 | 1 920 km |
| kötümser (tetikli, 32 mm, +%10) | 0,0210 | 13,39 | 1 785 km |
| **makale (varsayım 0,0248)** | 0,0248 | **12,0** | **1 598 km** |

**Varsayılan 0,0248 artık hesaplanan aralığın tamamının üstünde.** Yani varsayım
tek bir senaryoda değil, her senaryoda kötümser.

Göbek **kaportalanmıyor** ve bu bilinçli bir karar. Kullanılan C_D = 0,6, çıplak
silindir (0,9) ile kaportalı nacelle (0,2) arasında orta bir değerdir; pervane
somununun doğal spinner etkisini ve koaksiyel çiftte arkadaki motorun öndekinin
izinde kalmasını hesaba katar. Kaportalamanın kazancı `C_D0`'da yalnızca **0,0010**,
L/D'de %0,5'ten az — sonucu değiştirmediği için tasarımı bağlamıyoruz.

## Hacim kapanışı — `hacim.py`

Kanat-gövde yükü gövdenin **içinde** taşır, dolayısıyla görev seçiminden önce
sorulması gereken şey şudur: yük zaten sığıyor mu?

| | brut | kullanılabilir (~%55) | yüksüz dolum | yüke kalan |
|---|---:|---:|---:|---:|
| hafif, 50 kg | 185 L | 102 L | 21 L | **81 L** |
| ağır, 1000 kg | 6 936 L | 3 815 L | 768 L | **3 047 L** |

13 kg yükün 81 litreye sığması için yoğunluğunun yalnızca **0,16 kg/L** olması
yeterli. Su 1,0 · elektronik ~0,8 · köpük kargo ~0,3 kg/L — **hepsi sığar.**

**Konfigürasyon hacim değil kütle sınırlı.** Görev seçimi iç hacmi zorlamıyor;
yapıyı ve yük yollarını etkiliyor, o da kütle bütçesidir — makalenin 8.2'de
zaten "en çok yanılma ihtimali olan yer" dediği kalem.

---

## `temel.py` — karşılaştırmalı temel: dış denetim sonrası düzeltmeler (08.09.2026)

İki bağımsız denetim de aynı yere işaret etti: hesap tutarlı, ama
**C'ye (tilt) verilen varsayımlar sonucu hesap başlamadan belirliyor.**
Yapılan düzeltmeler ve **ölçülen** sonuçları:

### 1. C'nin seyir cezası artık parametre ve taranıyor

Önce: `LD_carpan = 1.0` sabit, "tilt'in lehine, kasten" notuyla.
Şimdi: `C_LD` ve `C_eta` parametre; varsayılan 1,00 **idealleştirilmiş
üst sınır** olarak etiketli, `duyarlilik_C()` taramayı basıyor.

C'nin A'ya göre menzili (%):

| L/D çarpanı | 1,00 | 0,96 | 0,92 | **0,88** | 0,85 |
|---|---|---|---|---|---|
| menzil farkı | +12,0 | +7,5 | +3,0 | **−1,4** | −4,8 |

**Eşik çarpan ≈ 0,89.** Bu, A'nın kendi uç çerçeve cezasının (1/1,12 =
0,893) neredeyse tam olarak aynısı. Yani ölçülen ifade şudur:

> **Tilt, ancak eğme mekanizması seyirde en az A'nın uç çerçeveleri
> kadar sürükleme öderse A'nın gerisine düşer.** Bu ölçülmedi;
> dolayısıyla "A tilt'ten iyidir" denemez.

### 2. η_seyir'in menzile etkisi YOK — denetimin yarısı düzeltildi

YZ5, C'ye A'nın η_seyir'inin de verilmesini "ikinci hediye" olarak
işaretledi ve "P_seyir'de L/D ile η çarpılıyor, ikisini birden
bağışlamak Bill 2'yi kapatır" dedi. **Ölçüm bunu yalnızca yarı
doğruluyor:**

    R = f_yakıt · E* · η_zincir · (L/D) / g        → η_seyir YOK

η_seyir yalnızca P_seyir → P_kurulu → motor kütlesi → MTOW zincirine
girer. Tarama:

| | η×1,00 | η×0,95 | η×0,90 | η×0,85 |
|---|---|---|---|---|
| C'nin menzili | +%12,0 | +%12,0 | +%12,0 | +%12,0 |
| C'nin MTOW'u (kg) | 60,3 | 61,0 | 61,8 | 62,7 |

Yani η gerçekten bir hediyedir, ama **kütle sütununda**, menzil
sütununda değil. Menzil üstünlüğünün tamamı L/D çarpanından geliyor.
Bu, hediyeyi küçültmez — sadece nereye düştüğünü değiştirir; ve
"iddiayı belirleyen tek serbest parametre L/D çarpanıdır" tespitini
**güçlendirir**.

### 3. B'nin yapısal kesri artık ayrılabilir

`B_govde_ek` eklendi (`duyarlilik_B()`). Dağıtılmış kaldırmanın yapısal
cezası:

| f_gövde_ek | 0,00 | 0,02 | 0,04 | 0,06 |
|---|---|---|---|---|
| MTOW (kg) | 86,0 | 99,1 | 116,9 | 142,5 |
| menzil (km) | 1370 | 1370 | 1370 | 1370 |

**Menzil etkilenmiyor**, faydalı yük payı 0,151 → 0,091'e düşüyor.
Eksiklik gerçek, ama A > B sonucunun yönünü değiştirmiyor, güçlendiriyor.

### 4. Ağır hat: "yeniden ayar yok" iddiası artık gerçekten sınanıyor

`agir_ayarsiz()` eklendi — motor payı da hafif hattın 1,529'unda tutulur:

| | tam ayarsız (1,529) | makalenin payıyla (1,385) | makale |
|---|---|---|---|
| MTOW | 1036,8 kg (+%3,7) | 1013,4 kg (+%1,3) | 1000 |
| motor | 63,5 kW (**+%16,9**) | 56,2 kW (+%3,5) | 54,3 |
| menzil | 1813 km (−%0,1) | 1813 km (−%0,1) | 1814 |
| L/D | 13,60 (%0,0) | 13,60 (%0,0) | 13,6 |

Menzil ve L/D istisnadan **etkilenmiyor**; sapma tamamen motor
derecelendirme payında. Yani ölçek öngörüsü sağlam, tutarsızlık
makalenin kendi iki tasarımı arasında.

### 5. Düzey 2 "korkuluk" olarak etiketlendi

Gerçek bir lift+cruise kaldırmayı bataryayla yapar; motoru hover'a
boyutlamaz. Düzey 2 o mimariyi temsil etmiyor, çıktı başlığında böyle
yazıyor. Adil karşılaştırma Düzey 1'dir.

### 6. Ölü alan kaldırıldı

`Mimari.f_tahrik = 0.16` tanımlıydı ama `boyutlandir()` onu hiç
kullanmıyordu (tahrik kesri her turda kurulu güçten yeniden
hesaplanıyor). **Çift sayım yoktu** — YZ1'in şüphesi kontrol edildi ve
çürütüldü — ama alan yanıltıcıydı; silindi.

### Düzey 1 sayıları değişmedi

Yeniden yapılandırma davranışı korudu: A 50,0 kg / 1600 km, B 86,0 kg /
1370 km, C 60,3 kg / 1792 km. Değişen, bu sayıların **hangi
varsayımdan geldiğinin ölçülmüş olması**.
