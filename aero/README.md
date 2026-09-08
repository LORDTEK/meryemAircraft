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

---

## Karşılaştırma sözleşmeleri — üçüncü denetimin bulduğu (08.09.2026)

YZ1 ve YZ5'in ikisi de "sabit yakıt kesrinde menzilin MTOW'dan bağımsız
olması Breguet'nin doğru bir özelliğidir, hata değildir" dedi. Doğru —
ama YZ3 bunun **karşılaştırma sözleşmesi** olarak tehlikeli olduğunu
gördü ve haklı çıktı:

    R = (E* η_zincir / g) · (L/D) · (m_yakıt / MTOW)

    sabit KESİR  → m_yakıt/MTOW sabit → R, MTOW'dan bağımsız
    sabit KÜTLE  → R ∝ (L/D)/MTOW      → kütle cezası geri gelir
    sabit MTOW   → f_yakıt = 1 − f_boş − m_faydalı/MTOW

Sabit kesirde **daha ağır mimari orantılı olarak daha fazla yakıt
taşıyor** ve kütle faturası menzilden siliniyor. Üç sözleşme
uygulandı (`sozlesmeler()`), C'ye ×1,00 hediyesi hâlâ duruyorken:

| C'nin A'ya göre menzili | sözleşme 1 (sabit kesir) | sözleşme 2 (sabit yakıt kütlesi) | sözleşme 3 (sabit MTOW + faydalı yük) |
|---|---|---|---|
| **+%12,0** | **+%0,2** | **−%19,1** |

B üç sözleşmede de kaybediyor ve gittikçe kötüleşiyor: −%14,4 / −%36,5
/ −%72,6.

L/D çarpanıyla birlikte tarandığında:

| C'nin L/D çarpanı | söz. 1 | söz. 2 | söz. 3 |
|---|---|---|---|
| ×1,00 | +%12,0 | +%0,2 | −%19,1 |
| ×0,96 | +%7,5 | −%4,3 | −%23,6 |
| ×0,92 | +%3,0 | −%8,9 | −%28,2 |
| ×0,88 | −%1,4 | −%13,4 | −%32,7 |

**Yani C'nin üstünlüğü tek bir kutuda yaşıyor: sözleşme 1 + ×1,00.**
Diğer sekiz kutunun yedisinde A önde.

### YZ3'ün bir sayısının düzeltilmesi

YZ3, sabit yakıt kütlesi için elle şunu hesapladı:

    R_C/R_A = (13,44/12,00)·(50,0/60,3) ≈ 0,93   → C %7 kötü

Yön doğru, sayı değil: 60,3 kg, **sabit kesir** sözleşmesinin MTOW'u.
Yakıt kütlesi sabitlenince C'nin MTOW'u da kapanarak 55,9 kg'a düşüyor
(daha az yakıt → daha hafif uçak → daha az kurulu güç). Modelin
verdiği: **+%0,2**, yani berabere. Sabit MTOW sözleşmesinde ise YZ3'ün
sayısı **tam tutuyor**: elle −%19, model −%19,1; f_yakıt = 1 − 0,624 −
0,26 = 0,116, modelinki de 0,116.

### Çift sayım kontrolü (YZ3 §5.2)

`LD_temiz = 13,44 = 12,0 × 1,12` olarak tanımlı; A'ya sonra `1/1,12`
uygulanıyor ve tam 12,00 çıkıyor. Doğrulama tablosu bunu kilitliyor.
**Çift sayım yok.**

---

## `kutle.py` — bileşen düzeyinde kütle bütçesi (08.09.2026)

Üç dış denetim de listeledi; YZ3 Q1 için zorunlu saydı. Makale §6.2'nin
kesirleri (%30 yapı / %16 tahrik / %4 pil / %8 aviyonik / %16 yakıt →
%26 faydalı yük) **aşağıdan yukarı** yeniden kuruldu. İlke: hiçbir
kalem hedef kesirden geri çözülmedi — yoksa sınama değil, kendini
doğrulama olurdu.

### İlk koşu bir uyarı verdi

İlk sürüm **%42,8 faydalı yük** verdi; hedef %26. Aşağıdan yukarı bir
bütçe kendi hedefini %60 aşıyorsa önce **kalem aranır**. Arandı ve yedi
kategori eksik çıktı: bağlantı elemanı/yapıştırıcı/boya, erişim
kapakları, motor yatağı-soğutma-egzoz, eş eksenli göbek-mil-yatak,
sinyal demeti, faydalı yük arayüzü, iniş temas pedleri. Ayrıca ön
tasarımda standart olan **belirsizlik payı** (kurunun %12'si) yoktu.

### Hafif hat (50 kg) — kapanıyor

| grup | ölçülen | hedef | fark |
|---|---|---|---|
| yapı | %23,8 | %30 | −6,2 puan |
| tahrik | %15,2 | %16 | −0,8 puan |
| pil | %3,6 | %4 | −0,4 puan |
| aviyonik + sistem + pay | %11,0 | %8 | +3,0 puan |
| yakit | %16,0 | %16 | 0,0 |
| **faydalı yük** | **%30,4** | **%26** | **+2,2 kg** |

En büyük tek kalem kabuk (6,20 kg, %12,4); ikincisi iç yapı (2,79 kg).

### Kırılma değerleri — 13 kg hangi noktada kapanmaz

| varsayım | taban | kırılma | pay |
|---|---|---|---|
| **kabuk kg/m²** | **1,50** | **1,783** | **%19** |
| iç yapı / kabuk | 0,45 | 0,723 | %61 |
| bağlantı oranı | 0,10 | 0,297 | %197 |
| belirsizlik payı | 0,12 | 0,219 | %82 |
| motor kW/kg | 4,00 | 2,433 | %39 |
| ICE+jeneratör kW/kg | 1,00 | 0,623 | %38 |

**Sonuç tek bir sayıya asılı: kabuk alan yoğunluğu.** Diğer bütün
varsayımların payı %38–197 arasında; kabuğunki %19. 1,78 kg/m²'nin
üstünde bir kaplama, 13 kg faydalı yükü kapatmaz.

### ⚠️ DÜZELTME (08.09.2026) — pay iki kez sayılmıştı

Önce şöyle yazmıştım: *"bütçeye daha 4,5 kg sayılmamış kütle girebilir."*
**Yanlış.** Kırılma payı 0,219 × 22,320 = **4,888 kg**, belirsizlik
satırının **toplamıdır**; bunun 2,678 kg'ı zaten bütçede duruyor. Ek
olarak kaldırılabilen kütle:

    4,888 − 2,678 = 2,210 kg

Bu da zaten bildirilen **2,2 kg payın kendisi**. İki sayı hiçbir zaman
bağımsız değildi; aynı payı iki kez saymışım. Bu hatayı dışarıdan bir
denetim yakaladı.

**Doğru ifade:** bütçe 2,2 kg pay taşıyor, nokta. İlk turda 3,4 kg'lık
kalem kaçırdığım düşünülürse bu **rahat bir pay değil** — kaçırdığım
kalemler bir kez daha o büyüklükte çıkarsa iddia düşer.

### Yapıyı mukavemet belirlemiyor

Kök eğilme momenti 934 N·m, kiriş başlığı alanı **10,7 mm²**, başlık
kütlesi **41 gram** — MTOW'un binde 8'i. Ağır hatta bile ~%0,3. Yani bu
boyutlarda yapıyı belirleyen **asgari kaplama kalınlığı ve montajdır,
mukavemet değildir.** Bu, %25 kalın merkez gövdenin yapısal bir bedel
ödemediğini de açıklıyor.

### Ağır hat (1000 kg) — AÇIK SORU

Kabuk kütlesi ~ σ_alan · S_ıslak ~ ölçek²; MTOW ~ ölçek³. σ_alan sabit
kalırsa kabuk **kesri** ölçekle 1/ölçek düşer — büyük uçakta kaplama
incelmediği için bu açıkça yanlış. Sabit kesir için σ_alan ~ ölçek¹
gerekir. Gerçek üs ikisinin arasında; tarandı:

| üs | kabuk kg/m² | yapı kg | faydalı kg (hedef 260) |
|---|---|---|---|
| 0,00 | 1,50 | 197,3 | 359,0 ✓ |
| 0,25 | 2,03 | 238,4 | 313,0 ✓ |
| **0,467** | **2,64** | — | **260 (kırılma)** |
| 0,50 | 2,74 | 294,1 | 250,6 ✗ |
| 1,00 | 5,02 | 471,0 | 52,4 ✗ |

**Ağır hat, kabuk alan yoğunluğu ölçek^0,467'den yavaş büyürse
kapanıyor; hızlı büyürse kapanmıyor.** Bu üssün ne olduğu ölçülmedi ve
bu, 1000 kg hattının gerçek açık sorusudur — hafif hattınkinden daha
büyük bir belirsizlik.

### Düzeltilen hata

İlk sürümde uç çerçeve postunun **çapı ölçekle büyümüyordu** (50 mm'de
sabit). Ağır hatta 50 mm'lik boruya 44 mm et kalınlığı istedi ve yapıyı
370 kg gösterdi. Çap kök veterine bağlandı (%5); hafif hat sayıları
değişmedi (ölçek = 1), ağır hat düzeldi.

---

## Pil tamponu GÜÇ sınırlı — makalede hiç yazmıyordu (08.09.2026)

Dış denetim sordu: 1,8 kg pil, hover ile motor derecelendirmesi
arasındaki farkı gerçekten besleyebilir mi? Ölçüldü (`pil_sinami()`):

| | hafif hat | ağır hat |
|---|---|---|
| pilden istenen güç | 8,3 kW | 161,9 kW |
| pil kütlesi | 1,8 kg | 40,0 kg |
| **gereken özgül güç** | **4,61 kW/kg** | **4,05 kW/kg** |
| 180 Wh/kg'da C-oranı | 26C | 22C |
| enerji sınırına geçiş | 141 s hover | 160 s hover |

**Bulgu:** tampon, §7'nin uçuş profilindeki hover süreleri boyunca
**enerji değil güç** sınırlıdır. Ve 26C verebilen hücreler tipik olarak
180 Wh/kg'ın altında kalır — o zaman enerji eşiği de aşağı iner.

Yani 1,8 kg serbest bir parametre değil, **bir hücre seçimi
şartnamesidir** ve zorlayıcı bir şartnamedir. Makale bunu hiçbir yerde
söylemiyordu; §6.7'ye eklendi.

## Eksik kalem kontrolü — dört kategori doğrulandı

Denetimlerin "muhtemelen unuttuğun" dediği dört kalem bütçede **var**:

| kalem | nerede | kg |
|---|---|---|
| pervane palleri + eş eksenli göbek | TAHRİK | 0,400 + 0,044 + 0,140 |
| güç elektroniği (hover tepesine boyutlu) | TAHRİK | 0,610 |
| yakıt kabı/pompa/hat | SİSTEM | 0,960 |
| kumanda tahriki | SİSTEM | 0,271 (yalnız şerit) |

Son satır küçük çünkü **bu uçakta kumanda yüzeyi yok** — makalenin
merkezi iddiası bu; şerit tek hareketli aerodinamik parça.

**Ayrı modellenmeyen tek kategori: yerel yük girişi.** Uç çerçeve
kökleri, burun motoru yatağı, faydalı yük/yakıt/pil mesnetleri kabuk ve
iç yapı payının içinde sayılıyor, ayrıca boyutlandırılmıyor. Bu yük
yolları payın içerdiğinden pahalıya çıkarsa aynı 2,2 kg'dan çıkar.
Kayda geçti (§8.2).

---

## `donme.py` — geçiş dönme dinamiği ve uç pervane boyutlandırması (08.09.2026)

§8.14'ün 3. maddesi *"uç pervaneleri mertebe tahminiyle değil düzgün
boyutlandırmak"* diyor. Tam 6-DoF bunun için gerekli değil — ve zaten
yapılamaz: 90°'ye kadar `C_m(α)` verisi yok, deneysiz üretilemez.

**Bunun yerine kurulan şey daha dar ve daha sağlam: atalet alt sınırı.**
Uç pervaneler uçağın ataletini bile döndüremiyorsa aerodinamik momenti
hiç döndüremez. Yetiyorsa, aerodinamik marjın bilinmediği açıkça yazılır.

Dönme ekseni: uç çerçeveleri planforma **dik** uzanıyor (§4.3), üst/alt
çift farkı → gövde x'i boyunca kuvvet × gövde z kolu → **açıklık ekseni
etrafında yunuslama.** Geçişin döndüğü eksen de bu. Yani I_yy gerekli.

### Atalet, kütle bütçesinden

`kutle.py`'nin kalem kütleleri `planform.py`'nin geometrisine dağıtıldı
(kabuk/iç yapı planforma yayılı, uç çerçeveleri z boyunca çubuk, uç
motorları z = ±0,71 m'de nokta, merkez gövde kalemleri veter boyunca).
Yalnızca **konumlar** varsayım; kütleler bütçeden geliyor.

| | I_yy | CG (kök veterinin) |
|---|---|---|
| hafif 50 kg | ~~7,04 kg·m²~~ | ~~%57~~ |
| ağır 1000 kg | ~~1918 kg·m²~~ | ~~%58~~ |

⚠️ **Bu tablo GEÇERSİZ.** Konumlar elle yerleştirilmişti ve iç hacme
bakılmamıştı; aşağıdaki "DÜZELTME" bölümüne bakınız. Geçerli değerler
hacme orantılı yerleştirmeden: **9,813 kg·m² / %80,2** ve
**2503,069 kg·m² / %82**.

### §7.4'ün rampası sonlu momentle üretilemez

Mevcut benzetim θ = 90°·(t/t_r), yani **doğrusal rampa**: ivmesi her
yerde sıfır, iki ucunda sonsuz. Sonlu momentle üretilebilen en yakın
profil, hız ve ivmesi uçlarda sıfırlanan yumuşak profildir:

    α_tepe = 6 · Δθ / t_r²        (yumuşak)
    α_tepe = 4 · Δθ / t_r²        (üçgen / bang-bang)

Bu, mevcut modelin sessiz bir varsayımıydı; artık sayısı var.

### Sonuç — ikisi de yetiyor, ama payları farklı

| | I_yy·α (yumuşak) | mevcut moment | **pay** | en kısa dönme |
|---|---|---|---|---|
| hafif, t_r = 2 s | 16,6 N·m | 46,0 N·m | **2,8×** | 1,20 s |
| ağır, t_r = 4 s | 1130 N·m | 1905 N·m | **1,69×** | 3,08 s |

Hafif hatta atalet için gereken itki **5,84 N/çift** — makalenin
verdiği 16,2 N'un yalnızca **%36'sı**.

Ağır hattın uç itkisi makalede verilmemiş; %12 güç payından hesaplandı
(6486 W/çift → 200,1 N/çift).

### Makalenin kendi sayısının denetimi

16,2 N / 335 W / D=0,20 m → momentum teorisi **FoM = 0,702** ve **eş
eksenli kayıp yok** varsayımına denk. Makalenin kendi hover FoM'u
0,599. Onu ve %15 eş eksenli kaybı uygularsak itki 12,4 N'a düşüyor —
**pay yine 2,1×.** Yani sonuç bu farktan etkilenmiyor; ama 16,2 N'un
neye dayandığı makalede yazmıyor.

### Ölçek yasası — makalenin nitel iddiasının sayısı

    M_mevcut ~ ölçek³ ,  I_yy ~ ölçek⁵ ,  α ~ 1/t_r²
    pay ~ t_r² / ölçek²        →  aynı pay için t_r ~ ölçek

Ölçek 3,345 kat; aynı payı korumak için t_r 2 s'den **6,69 s**'ye
çıkmalıydı. Tasarım 4 s kullanıyor, bu yüzden payı 2,8× yerine 1,69×.
§7.4 zaten *"daha büyük uçak daha yavaş dönmeli"* diyordu; bu, o
cümlenin sayısal karşılığı ve **payın ölçekle daraldığını** gösteriyor.

### Bunun kapsamadığı

Aerodinamik yunuslama momenti. Basınç merkezi 0→90° arasında göç eder
ve o momenti karşılamak için gereken itki burada **hesaplanmadı**;
C_m(α) verisi yok. Dolayısıyla 2,8× ve 1,69× **atalet payıdır**, toplam
kontrol payı değil. Aerodinamik moment bu payı yiyebilir.

---

## ⚠️ DÜZELTME — dönme momenti modeli yanlıştı (08.09.2026)

Dış denetim yakaladı ve haklı: `donme.py`'nin ilk sürümü mevcut
momenti **4TL** alıyordu. Yanlış. 4TL, **alt çiftlerin −T üretmesini**,
yani itkinin tersine çevrilebilmesini gerektirir. Bu uçakta pervaneler
tersine çalışmıyor; itki negatif olamaz.

İtki negatif olamıyorsa en büyük fark, üst çiftler tepe değerde ve alt
çiftler **sıfırda** iken oluşur. İki üst çift vardır:

    M_maks = 2 · T_maks · L

Bu, makalenin §4.4'te ve §7.4'te **zaten yazdığı** bağıntıdır. İlk sürüm
makalenin kendisiyle çelişiyordu — iç tutarsızlık, dışarıdan görüldü.

### İkinci düzeltme: yapılabilirlik en UCUZ profille sınanır

İlk sürüm yumuşak profili (α = 6Δθ/t_r²) kullanıyordu. Yapılabilirlik
bir **gerek şart** sınamasıdır: *"bu hiç yapılabilir mi"* sorusunun
cevabı en az ivme isteyen profille verilir — üçgen (bang-bang),
α = 4Δθ/t_r². Varsayılan o yapıldı; yumuşak profil ayrıca raporlanıyor.

### Düzeltilmiş sonuç

| | mevcut M | üçgen: gereken → **pay** | yumuşak: gereken → **pay** |
|---|---|---|---|
| hafif, t_r = 2 s | 23,0 N·m | 11,1 → **2,08×** | 16,6 → **1,39×** |
| ağır, t_r = 4 s | 952,3 N·m | 753,3 → **1,26×** | 1130,0 → **0,84× ✗** |

**Ağır hattın 4 saniyelik dönüşü yalnızca en ucuz profille kapanıyor.**
Daha yumuşak bir kumanda 4,36 s ister. En kısa dönme süreleri: hafif
1,39 / 1,70 s; ağır **3,56 / 4,36 s**.

Hafif hattın 16,2 N'u yerine temkinli 12,4 N kullanılırsa (makalenin
kendi FoM 0,599'u + %15 eş eksenli kayıp) mevcut moment 17,6 N·m'ye
düşer, üçgen payı **1,59×** olur. Ağır hattın 200,1 N'u zaten bu
temkinli esasla hesaplandı.

### Üçüncü düzeltme: ölçek paragrafı varsayımdan değil ölçümden

İlk sürüm geometrik benzerlik varsaydı (M ~ ölçek³, I ~ ölçek⁵ →
pay ~ t_r²/ölçek²). **İki referans tasarım geometrik olarak benzer
değil:** açıklık 3,345 kat büyürken kütle 20 kat büyüyor (3,345³ =
37,4 ≠ 20) ve kanat yüklemesi 25,3 → 45,0 kg/m². O türetim geçersizdi.

Ölçülen oranlar:

| | ağır / hafif |
|---|---|
| I_yy | **272,5** (açıklık³ = 37,4; ⁵ = 418,7 — ikisi de değil) |
| M_mevcut | **41,4** |
| gereken moment (α oranı 0,25 ile) | 68,1 |
| **pay oranı** | **0,61 — ağır hatta %39 daralıyor** |

Hafif hattın payını korumak için ağır hattın dönme süresi **5,13 s**
olmalıydı; tasarım 4 s kullanıyor.

**Bir dış iddia çürütüldü:** "50→1000 kg için doğrusal ölçek 20^(1/3) =
2,714 olmalı" denildi. Değil — o, sabit yoğunlukta geometrik benzerlik
varsayar. Makalenin kendi künye tablosu açıklığı 3,4528 → 11,55 m
veriyor, yani **3,345**. Tasarımlar benzer değil, bu yüzden 2,714
geçerli değil.

## §7.4'ün irtifa kaybı, profil seçimine duyarlı mı — ÖLÇÜLDÜ

§7.4'ün tabloları doğrusal θ rampasına dayanıyor ve o rampa sonlu
momentle üretilemez. Üç profille yeniden koşuldu (irtifa kaybı, m):

| | T/W | w0=0: doğrusal / yumuşak / üçgen | w0=5 |
|---|---|---|---|
| hafif | 1,1 | −13,2 / −14,5 / −14,9 | **0 / 0 / 0** |
| hafif | 1,2 | −9,1 / −10,5 / −10,9 | **0 / 0 / 0** |
| hafif | 1,3 | −2,1 / −2,7 / −2,9 | **0 / 0 / 0** |
| ağır | 1,1 | −17,7 / −19,5 / −20,5 | **0 / 0 / 0** |
| ağır | 1,2 | **−1,4 / −13,4 / −11,6** | **0 / 0 / 0** |
| ağır | 1,3 | 0 / 0 / 0 | **0 / 0 / 0** |

**Ana sonuç sağlam:** *"tırmanışta girmek irtifa kaybını tamamen
kaldırır"* üç profilde de, iki tasarımda da, her T/W'de geçerli. Ağır
hat için 4,36 ve 5,13 s'de de sıfır.

**Ama bir girdi ciddi kaydı:** ağır hat, T/W = 1,2, tırmanışsız giriş —
doğrusal profilde −1,4 m, sonlu momentli profillerde −11,6/−13,4 m.
Yaklaşık **12 metre**. Bu, yayımlanmış bir tablo değeri ve düzeltilmeli.

---

## Ağır hattın geçiş süresi 4 s → 5,1 s (08.09.2026)

`donme.py`'nin düzeltilmiş hâli, ağır hattın 4 saniyelik dönüşünün bir
**sınır** olduğunu gösterdi: üçgen profilde pay 1,26, yumuşak profilde
**0,84 — kapanmıyor.**

Ölçek oranından türetilen doğru değer: I_yy 272,5 kat büyüyor, mevcut
moment 41,4 kat. Payın korunması için gereken moment de 41,4 kat
büyümeli → **t_r = 5,13 s.** Yuvarlanmış: **5,1 s.**

| | t_r | üçgen payı | yumuşak payı | uç pervane gücü |
|---|---|---|---|---|
| eski | 4,0 s | 1,26 | **0,84 ✗** | %13 |
| **yeni** | **5,1 s** | **2,05** | **1,37** | **%6** |
| hafif (karşılaştırma) | 2,0 s | 2,08 | 1,39 | — |

**Değişikliğin maliyeti yok, üç kazancı var:** paylar hafif hattınkine
eşitleniyor, uç pervane gücü %13'ten %6'ya iniyor (makalenin **kendi
Tablo 4'ünden**), ve irtifa kaybı tırmanışlı girişle üç profilde de
sıfır kalıyor.

**Not — bulgu makalenin kendi Tablo 4'üyle çelişmiyor, onu tekrarlıyor.**
Tablo 4 zaten 4 s'nin uç pervane payının neredeyse tamamını (%13)
yediğini söylüyordu. `donme.py` bunu moment cinsinden yeniden buldu ve
üzerine **dönme profilini** ekledi — Tablo 4 profil ayrımı yapmıyordu.

## Aerodinamik moment eşiği — atalet küçük terim çıktı

Aerodinamik momenti tahmin etmiyoruz (C_m(α) verisi yok). Kabuk alan
yoğunluğunda işe yarayan teknik: **payı tüketecek değeri vermek.**

    C_m_eşik = (M_mevcut − M_gereken) / (q · S · c_ort)

| V (m/s) | 10 | 15 | 20 | 30 |
|---|---|---|---|---|
| hafif (11,9 N·m artıyor) | 0,172 | **0,076** | 0,043 | 0,019 |
| ağır (489 N·m artıyor) | 0,186 | **0,083** | 0,047 | 0,021 |

Ok kanatlı planformlarda stall sonrası C_m rutin olarak **0,1–0,3.**

**Yani atalet bu problemin küçük terimi.** §7.6'nın 2,05/2,08 payları,
manevranın kapandığının delili **değil**; yalnızca ataletin onu
engellemediğinin delili. Makaleye bu şekilde yazıldı ve **geçiş
kontrol edilebilirliği, kütle bütçesinin önüne geçerek çalışmanın en
büyük açık kalemi ilan edildi.**

---

## `zarf.py` — geçiş tasarım zarfı: hücum açısı 90°'ye ÇIKMIYOR (08.09.2026)

§7.6 eşiği tek bir temsili hızda hesaplıyordu ve bu, yanlış bir soru
sordurtuyordu: *"90 dereceye kadar C_m ne kadar?"*

**Ölçüldü: geçiş boyunca hücum açısı 90 dereceye çıkmıyor.** GÖVDE açısı
90° dönüyor, ama bağıl rüzgâr da onunla birlikte dönüyor — çünkü uçak
aynı anda hızlanıyor ve tırmanıyor.

7.4'ün kendi yörüngesi kullanıldı; yeni fizik yok.

| | giriş | en büyük α | o anda V | **C_m bütçesi** |
|---|---|---|---|---|
| hafif | 5 m/s tırmanış | **17,5°** | 7,3 m/s | **0,322** |
| hafif | tırmanışsız | **21,6°** | 2,8 m/s | **2,174** |
| ağır | 5 m/s tırmanış | 5,4° | 35,6 m/s | 0,015 |
| ağır | tırmanışsız | **20,5°** | 6,8 m/s | **0,404** |

### Kısıt ikiye ayrılıyor ve ikisi FARKLI problemler

**1. Dönüşün ortası — yüksek açı, düşük hız.** α = 17–22°, V = 2,8–7,3
m/s → bütçe **0,32–2,17**. Rahat. Korktuğum rejim buymuş ve **kolay
olan buymuş**, çünkü q küçük.

**2. Dönüşün sonu — düşük açı, yüksek hız.** α = 5–6,5°, V = 14,7–35,6
m/s → bütçe **0,079 (hafif) / 0,015 (ağır)**. Dar. **Ama bu bir stall
sonrası problemi değil** — kuyruksuz bir uçağın seyir hücum açısındaki
sıradan **denge (trim)** sorusudur. Seyir için dengelenmiş bir uçakta
CG etrafındaki C_m ≈ 0'dır; soru, o anda dengeden ne kadar uzak
olduğudur, ki bu bir **ağırlık merkezi yerleşimi** sorusudur.

### Açık kalemin yeniden tanımı

**Eski (yanlış):** *"90 dereceye kadar C_m(α) gerekiyor, bu rüzgâr
tüneli ister."*

**Yeni (ölçülmüş):** iki ayrı ve daha küçük gereksinim —
- **(a)** ~22 dereceye kadar C_m, düşük q'da. Hafif stall sonrası;
  mevcut veriye çok daha yakın bir rejim.
- **(b)** seyir hücum açısı civarında C_m — ki bu **her kuyruksuz
  tasarımın zaten cevaplaması gereken denge sorusudur**, geçişe özgü
  değil.

Bu, açık kalemi **ortadan kaldırmıyor ama küçültüyor ve
tanınabilir hâle getiriyor.**

### Kaydedilmesi gereken sınır

α(t) **nokta kütle** yörüngesinden geliyor: gövde ekseni ile hız vektörü
arasındaki açı. Yörünge yanlışsa açı da yanlıştır.

Ayrıca dönme hızının kendisi gövde boyunca **yerel** hücum açısını
değiştiriyor; hesaplandı: ω·(c/2)/V → hafif hatta tırmanışlı girişte
**±3,1°**, tırmanışsız girişte **±8,6°**. Yani tırmanışsız girişte
21,6°'lik ortalama açının üstüne ±8,6° biniyor ve gövdenin bazı
kısımları ~30° görüyor. İhmal edilemez; metne yazıldı.

---

## ⚠️ `kararlilik.py` — SEYIRDE DENGE SAĞLANAMIYOR (08.09.2026)

Dış denetimin ikisi de aynı yere bastı: §7.6'nın "dönüşün sonundaki dar
bütçe, kuyruksuz bir uçağın **sıradan** denge sorusudur" ifadesi
gösterilmemişti — ve bu uçakta elevon yok, refleks tarif edilmemiş, CG
kök veterinin %57'sinde. Biri bunu "credible panel/VLM static trim
analysis" ile kapatmayı önerdi. Yapıldı.

### Girdap-kafes sonucu — yakınsamış

| çözünürlük | tarafsız nokta |
|---|---|
| 6 kesit, sr 4, cr 8 | 0,8611 m |
| 14 kesit, sr 8, cr 12 | 0,8591 m |
| 20 kesit, sr 10, cr 16 | **0,8589 m** |

%0,26 değişim; yakınsamış.

**Tarafsız nokta = MAC'in %34,3'ü.** Bu, ok kanatlı bir planform için
tamamen olağan bir değer — yani VLM sonucu güvenilir.

### Sorun geometride değil, AĞIRLIK MERKEZİNDE

Ok açısı yüzünden MAC hücum kenarı kök veterinin **%65,5**'inde, çeyrek
MAC ise **%82,3**'ünde. Ama `donme.py`'nin kütle dağılımı CG'yi kök
veterinin **%57**'sine koyuyor — yani **MAC'in hücum kenarının bile
önüne.**

| CG (kök veterinin) | statik marj (MAC) | seyirde gereken denge C_m | gereken moment |
|---|---|---|---|
| **%57 (mevcut varsayım)** | **%47** | **0,240** | **150 N·m** |
| %70 | %28 | 0,141 | 88 N·m |
| %80 | %13 | 0,065 | 41 N·m |
| %85 | %5 | 0,027 | 17 N·m |

**Mevcut uç pervane momenti: 23 N·m.**

### Bulgu

**Varsayılan kütle dağılımıyla uçak seyirde dengelenemiyor — 6,5 kat
farkla.** Gereken 150 N·m, mevcut 23 N·m.

Denge momenti aerodinamik olarak, **refleks kamberden** gelmelidir
(kuyruksuz uçaklarda standart çözüm). Ama gereken C_m0 = 0,240;
refleksli profiller tipik olarak **+0,02 ile +0,05** verir. Bir mertebe
fark var.

### Bunun ne olduğu ve ne OLMADIĞI

**Bu bir VLM hatası değil** — tarafsız nokta %34 MAC, tamamen normal.

**Bu makalenin bir hatası da tam olarak değil** — çünkü **makale CG
konumunu hiçbir yerde belirtmiyor.** %57 benim `donme.py` içindeki
bileşen konumu varsayımımdan geliyor ve orada zaten "yalnızca konumlar
varsayım" diye işaretlenmişti.

**Bu, makalenin söylemediği bir TASARIM KISITI:** kuyruksuz bir uçak
olarak meryemAircraft'ın CG'si çeyrek-MAC'in yakınında olmak zorunda,
yani kök veterinin **%80'inden geriye**. Yakıt, faydalı yük ve motorun
nereye konduğu serbest bir seçim değil.

### Sonuçları

1. **§7.6'nın "sıradan denge sorusu" ifadesi fazla rahat.** Gösterilmesi
   gerekiyordu, gösterilince sıradan çıkmadı.
2. **Kütle bütçesi (§6.7) etkileniyor:** kalemlerin veter yönündeki
   konumu artık serbest değil, kısıtlı.
3. **Atalet hesabı (§7.6) etkileniyor:** CG geriye giderse I_yy değişir.
4. **Bu, hakemin bulacağı türden bir açık.** Kendimiz bulmamız çok daha
   iyi.

### SINIR

`vlm.py`'nin kesitleri **simetrik NACA**; makalenin tarif ettiği kamber
ve refleks dağılımları modelde **yok**. Dolayısıyla bu koşum
**kararlılığı** (C_m_α, tarafsız nokta) verir — ki bunlar kambere
birinci mertebede duyarsızdır — ama **dengeyi (C_m0)** vermez. Gereken
C_m0 hesaplanabildi; sağlanıp sağlanamayacağı kamber tanımlanmadan
bilinemez.

### DÜZELTME — hatayı ben yapmışım, ve tablo tersine döndü

Yukarıdaki "%57 CG" **benim** varsayımımdı ve **yanlıştı**: `donme.py`'de
yakıtı, yükü ve motoru veter boyunca elle yerleştirmiş, **iç hacmin
nerede olduğuna bakmamıştım.**

İç hacmin **mutlak** ağırlık merkezi ölçüldü: **kök veterinin %78,3'ü.**
Ok açısı hacmi geriye taşıyor — dış kesitler kök firar kenarının çok
arkasında. Yapının kendi merkezi de %99,1'de.

**Taşınabilir kütle hacme orantılı dağıtılınca:**

| | eski (elle yerleştirme) | yeni (hacme orantılı) |
|---|---|---|
| CG | %57 kök veter | **%80,2** |
| statik marj | +%47 MAC (saçma) | **+%12,4 MAC** (olağan) |
| seyirde denge C_m | 0,240 (imkânsız) | **0,063** |
| I_yy | 7,04 kg·m² | **9,813 kg·m²** |
| dönme payı (üçgen) | 2,08× | **1,49×** |
| dönme payı (yumuşak) | 1,39× | **0,99×** |

**Kuyruksuz tasarımda tipik statik marj %5–15 MAC.** %12,4 tam ortada.
Yani konfigürasyon **doğal olarak kararlı** ve bunu ok açısına borçlu.

### Geriye kalan gerçek kısıt

Seyirde denge için gereken **C_m0 = 0,063**; refleksli profiller tipik
olarak **+0,02 – +0,05** verir. Aynı mertebede ama üstünde.

| CG (kök veterinin) | statik marj | gereken C_m0 |
|---|---|---|
| %78 | %16 | 0,083 |
| **%80,2 (hacim doğal)** | **%12,4** | **0,063** |
| **%83,3** | **%7,8** | **0,040** ← refleksle ulaşılabilir |
| %85 | %5,3 | 0,027 |

CG'yi %80,2'den %83,3'e almak **3 cm**'lik bir iç yerleşim değişikliği
ve statik marjı hâlâ olağan bandın içinde bırakıyor. Yani **tasarım
kapanıyor** — ama bu, makalenin söylemediği bir kısıt.

### Makaleye girecek kısıt

> Kuyruksuz bir uçak olarak meryemAircraft'ın ağırlık merkezi kök
> veterinin **%80–85'i** arasında olmak zorundadır. Bu aralık, iç hacmin
> doğal merkeziyle (%78,3) neredeyse çakışıyor — yani kısıt zorlayıcı
> değil, ama **serbest de değil** ve bugüne kadar yazılmamıştı.

### Etkilediği sayılar

- **§7.6 atalet:** I_yy 7,04 → **9,68 kg·m²**; hafif hat dönme payı
  2,08 → **1,51×**. Hâlâ yeterli ama daha dar.
- **§6.7 kütle bütçesi:** **toplamlar değişmiyor.** Değişen, kalemlerin
  nereye konabileceği. Yani bütçe **çözülmedi, daha da kısıtlandı.**
- **§7.6'nın "sıradan denge sorusu" ifadesi:** artık gösterilmiş, ve
  gerçekten sıradan çıktı — ama gösterilmesi gerekiyordu.

---

## DÜZELTME 2 — referans veter karışmış (08.09.2026, geç)

Yukarıdaki tablo **statik marjı MAC üzerinden** (%12,4) ama **denge
gereksinimini S/b üzerinden** (0,063) veriyordu. İkisi aynı büyüklüğün
iki farklı boyutsuzlaştırılması değil; aynı hesabın iki farklı referans
veterle yazılması. Bu, makaleye de aynen geçmişti.

Ölçülen: gerçek **MAC = 0,6514 m**, MAC hücum kenarı x = 0,6354 m,
ortalama geometrik veter S/b = 0,5730 m. Aralarında %13,7 fark var.

`kararlilik.py` artık **her yerde MAC** kullanıyor — VLM'in kendi
boyutsuzlaştırmasında da. Tarafsız nokta değişmiyor (x_np = c_ref ×
eğim çarpımı referanstan bağımsız), oran değişiyor.

| CG (kök veterinin) | statik marj (%MAC) | gereken denge C_m |
|---|---|---|
| %78 | +%15,7 | 0,071 |
| **%80,2 (hacim kuralı)** | **+%12,5** | **0,056** |
| %83 | +%8,3 | 0,037 |
| %85 | +%5,3 | 0,024 |

C_L_seyir = 0,45 (50 kg, 30 m/s, S = 1,9785 m²; perdövites 20,1 m/s'nin
1,49 katı). Refleks kesitler tipik 0,02–0,05 verdiğinden **pencerenin
üst yarısı ulaşılabilir, alt yarısı değil.**

### CG artık bir ÖLÇÜM değil, bir TASARIM KURALI olarak yazılıyor

Üç dış değerlendirmenin de istediği ayrım: hacme orantılı yerleştirme
bir *varsayım*. Metin (§7.6) artık bunu açıkça "first-order packaging
rule" diye adlandırıyor, tek bir referansla veriyor (0,778 m = kök
veterinin %80,2'si = MAC'in %21,9'u), yakıt yanınca CG'nin +0,3 puan
kaydığını söylüyor, ve pencereyi tablo olarak veriyor.

### Kararlılık GÖSTERİLİYOR, denge GÖSTERİLMİYOR

Ayrıca ayrıldı: §7.6 artık "**Static stability is shown**" ve "**Trim is
not shown. It is a requirement, and the requirement is quantified**"
diye iki ayrı başlık taşıyor. "The aircraft is trimmed" cümlesi metinde
hiçbir yerde yok.

### Dönme süreleri: pay değil, ALT SINIR

Eski metin 4 s'lik ağır hattı "1,26 / 0,84 pay" diye anıyordu; bunlar
**eski atalete** aitti. Düzeltilmiş atalete karşı 4 s'te paylar **0,97 /
0,65** — yani iki profilde de olanaksız. 5,1 s'te 1,57 / 1,05. Hafif hat
2 s'te 1,49 / 0,99, yumuşak asgarisi 2,01 s.

Yani **iki referans dönme süresi de yumuşak profilde eyleyici sınırında**;
metin artık bunları "actuator-limited lower bounds" diye yazıyor, "pay"
diye değil.

### §7, §8, §9'da düzeltilen bayat sayılar

| yer | eski | yeni |
|---|---|---|
| §7.6 en dar bütçe (hafif) | 0,079 | **0,050** |
| §7.6 en dar bütçe (ağır) | 0,015 | **0,010** |
| §7.6 ağır 4 s payları | 1,26 / 0,84 | **0,97 / 0,65** |
| §7.6 asgari dönme (ağır) | 3,56 / 4,36 s | **4,06 / 4,98 s** |
| §7.5 irtifa kaybı sınaması | 4,36 ve 5,13 s | **4,06 ve 4,98 s** (sıfır, doğrulandı) |
| §8, §9 dönme payı | 2,08 / 2,05 | **1,49 / 1,57** (üçgen) |
| §9 orta-dönüş C_m | 0,32 | **0,21** |
| §7.6 denge C_m | 0,063 | **0,056** |
| §7.6 statik marj | %12,4 | **%12,5** |

`dogrula.py`: 40 kontrol, 0 sapma.

---

## `kararlilik.py` — KONVANSIYON DENETIMI (08.09.2026)

Referans veter hatasi bir *konvansiyon* hatasiydi, aritmetik degil.
Ayni aileden ikincisinin OLMADIGINI varsaymak yetmez. Alti sinama
eklendi; ucu dogrudan cozucuye soruluyor, biri boyutlu yoldan bagimsiz
turetiliyor.

| sinama | sonuc |
|---|---|
| baslangic noktasi ortak (kok hucum kenari) | GECTI, x_le = 0 |
| isaret: kok LE'ye gore C_m(α>0) < 0 | GECTI, −0,357 |
| x_ref = x_np'de dC_m/dC_L → 0 | GECTI, −0,004 (LE'de −1,319 idi) |
| x_ref = x_cg'de dC_m/dC_L = −marj | GECTI, çözücü −0,128 / formül −0,125 |
| C_m hıza bağımsız | GECTI, 20 ve 40 m/s aynı |
| W(x_np−x_cg) = C_L·marj·q·S·MAC | GECTI, 39,824 N·m ↔ 39,824 N·m |

**6 sınama, 0 kaldı.** Dördüncüdeki 0,003'lük fark eğrilikten: marj
tarafsız noktadan türetilirse %12,5, çözücünün CG momentinden doğrudan
türetilirse %12,8. Metne yazıldı.

---

## ⚠️ `yatis.py` — 46 N·m NEREDEN GELİYOR? (08.09.2026)

YZ3 (9. tur) makalenin en zayıf **taşıyıcı** iddiasının denge değil
**yatış** olduğunu söyledi. Haklıydı ve sayı tutmadı.

### Hesaplanabilen kısım hesaplandı

- **I_xx = 25,010 kg·m²** — yunuslama ataletinin (9,813) 2,5 katı,
  çünkü kütle veterce değil açıklıkça yayılı. Yatış ekseni bugüne dek
  hiç bakılmamıştı.
- **|C_l_p| = 0,358** — literatürden değil, bu planformdan. Yöntem:
  kanada helis açısı kadar burulma, θ(y) = −atan(p·y/V), ve doğan
  moment. p'de doğrusal (0,1–0,4 rad/s'de %0,3 sapma), çözünürlükte
  yakınsamış (0,3536–0,3631, %1,3).
- seyirde sönümleme eğimi **77,6 N·m/(rad/s)**, zaman sabiti **0,32 s**.

### Gereksinim tersine çevrildi

| hedef | gereken moment |
|---|---|
| 20°/s | **27,1 N·m** |
| 25°/s | 33,9 N·m |
| §4.4'ün 46 N·m'si | → 34,0°/s |

30° yatışa ~1,21 s çıkıyor; §4.4 "1,2–1,5 s" diyordu. **Bu tutuyor.**

### BULGU — 46 N·m şeridin kendi kuvvetinden GELEMEZ

Şerit, Şekil 8'in üretim betiğine göre planformda 45° köşegen bir çit
(uzunluk 1,164 m, yükseklik 2→6 cm, alan 0,0466 m²). Oklu bir çit için
normal kuvvet cos²(ok) ile ölçeklenir.

| mekanizma | moment |
|---|---|
| şeridin kendi kuvveti, C_N = 1,3 (üst sınır) | **11,3 N·m** |
| yarı kanadın dolaşımını değiştirmesi, ΔC_L = 0,10 | 22,4 N·m |
| ΔC_L = 0,15 | 33,7 N·m |
| ΔC_L = 0,20 | **44,9 N·m** ← 46'nın geldiği yer |

46 N·m için gereken C_N **5,28** olurdu; akışa dik düz levha 1,1–1,3
verir. Yani şeridin kendi sürüklemesi dört kat eksik.

**Demek ki moment ikinci mekanizmadan geliyor** — şerit, üstünde
durduğu yarı kanadın dolaşımını değiştiriyor (Gurney/çit etkisi), ve
etkiyen alan şeridin değil **kanadın** alanı (0,8024 m²). Metin hangi
mekanizmayı kastettiğini hiç söylemiyordu.

20°/s için gereken **ΔC_L ≈ 0,12**. %1–2 veter Gurney şeritleri
0,1–0,3 veriyor: **makul ama gösterilmiş değil.** Denge için ne
yaptıysak (gereksinimi nicelemek, kapanışı iddia etmemek) burada da o
yapıldı.

### Asılı durum daha zor, ve sebebi sayısal değil yapısal

V = 0'da **aerodinamik sönümleme yok** — yatış ekseni çift
integratör. İz içindeki yarı kanat (0,4907 m², kol 0,282 m) ve
q_iz = 433,7 N/m² ile ΔC_L 0,10–0,20 → 6,0–12,0 N·m → 30° yatışa
1,5–2,1 s. Ama hız oturmuyor; şerit kapatılmak zorunda. Yani asılı
durumda yatış kontrolü seyirdekinden DAHA sıkı bir problem — olağanın
tersi.

### Aç-kapa olmak tek başına diskalifiye değil

Birinci mertebe dinamikte ölü bant + eyleyici gecikmesi:

| ölü bant | gecikme | sınır çevrimi |
|---|---|---|
| 2° | 50 ms | ±0,2° |
| 2° | 150 ms | **±9,4°** |
| 5° | 50 ms | ±0,0° |

Yani cihaz **hızlıysa kullanılabilir, yavaşsa değil**, ve eşik gerçek
eyleyicilerin ayrıştığı bir bantta. Bu, makalenin daha önce hiç
yazmadığı bir eyleyici gereksinimi. Kapalı çevrim kararlılık analizi
DEĞİLDİR.

---

## `sapma.py` — SAPMA: OTORİTE BOL, KARARLILIK YOK (08.09.2026)

Üç değerlendirmenin **üçü de** dondurmadan önce sapma eksenine bakılmasını
istedi. Bakıldı ve eksen ikiye ayrıldı.

### Kolay yarı: otorite

- **I_zz = 33,706 kg·m²** (I_xx 25,010 + I_yy 9,813 = 34,823; uçak
  neredeyse düzlemsel olduğu için yakın).
- **Kol farkı, makalede hiç söylenmemiş:** yunuslama çerçeve boyundan
  (0,71 m), sapma **yarı açıklıktan** (1,726 m) — yani **2,43 kat**.
- Mevcut moment 55,9 N·m (16,2 N) / 42,8 N·m (temkinli 12,4 N);
  yunuslamanınki 23,0 / 17,6. **Sapma, düzenin en güçlü ekseni.**
- Atalet sınırı: 73–95°/s², 15° sapmaya 0,56–0,64 s.

### Açık yarı: kararlılık

Girdap kafes, yan kayma açısında **C_n_β = 0** veriyor. Hata değil:
düzlemsel kanadın yanal kuvvet üretecek yüzeyi yok. Ok açısı
**C_l_β = −0,0447/rad** veriyor — yani ok, *yalpa* kararlılığını
sağlıyor, *sapma* kararlılığını sağlamıyor. Profil sürüklemesinden gelen
sönümleme de ihmal edilebilir: **C_n_r = −0,0023**, τ = 68 s.

**Demek ki yön kararlılığı uç çerçevelerinden gelmek zorunda** — seyirde
kanat düzlemine dik duran tek yüzeyler onlar. Kol 0,879 m; a_f = 4 ile:

| hedef C_n_β | gereken yanal alan | fairing veteri |
|---|---|---|
| 0,03 | 0,058 m² | **21 mm** |
| 0,05 | 0,097 m² | **34 mm** |
| 0,08 | 0,155 m² | 55 mm |

20 mm kalınlıklı bir fairing'in veteri zaten 50–70 mm. Yani gereksinim
rahatlıkla içeride.

### ASIL BULGU

**Fairing artık yalnızca bir sürükleme önlemi değil, aynı zamanda yön
kararlılığı yüzeyi ve sapma sönümlemesinin ana kaynağı.** §5.2 onu
sadece sürükleme kalemi olarak tanıtmıştı. Çerçeve kesiti artık iki
yönden kısıtlı; yalnız sürüklemeye bakarak seçmek yarım kanıtla seçmek
olurdu.

Yatıştaki gibi: **otorite gösterilmiyor, boyutlandırılıyor.**

---

## §3.7 — kendi karşılaştırmamız kanıt değil, ÖRNEK (08.09.2026)

YZ3'ün uyarısı: §5.5'in tilt hattına *cruise-drag çarpanı 1,00*
veriliyor (mekanizma aerodinamik olarak bedava sayılıyor) ve sonra aynı
karşılaştırma çerçevenin doğrulaması gibi kullanılıyorsa bu dairesel.

Haklı. §3.7 düzeltildi: **kanıt ağırlığı yalnız NASA çalışmasında**;
§5.5 çerçevenin uygulandığında neye benzediğini gösteren bir örnek.

Not: tilt duyarlılığı **zaten** makalede vardı (§5.5'te çarpan taraması
1,00/0,96/0,92/0,88, işaret değişimi ~0,89'da, ve "hiçbir yönde üstünlük
iddiası yok" cümlesi). 10. tur metninde onu "denetlenmedi" diye
listelemem hatalıydı.

### CFD kontrolü (YZ3'ün küçük sorusu) — düzeltme gerekmedi

Belirsizlik tablosunda başlangıç yayılımı zaten var (%4,3), simetri
zaten seçim ölçütü olarak yazılı, ve `bl_E` "reference state" diliyle
anılıyor. Dokunulmadı.
