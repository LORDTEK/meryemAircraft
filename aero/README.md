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

---

## 🔑 KAYNAKTAN ÇALIŞMAK — iki taşıyıcı iddia kapandı (09.09.2026)

35 PDF `kaynakca/` altına yüklendi ve okundu. İki sonuç, ikisi de metni
değiştirdi.

### 1. DENGE: refleks yapamıyor, burulma yapıyor

**NACA TR-460** (Jacobs, Ward & Pinkerton 1933), değişken yoğunluklu rüzgâr
tüneli, s. 52–53. Refleks orta çizgili kesitler:

| kesit | C_m0 (ölçülmüş) |
|---|---|
| NACA 2412 (normal kamber) | −0,044 |
| NACA 2R112 | −0,020 |
| NACA 0012 (simetrik) | −0,002 |
| **NACA 2R212 (refleks)** | **+0,004** |

Bizim gereksinimimiz **0,056**. Yani ölçülenin **on dört katı**. Pencerenin en
gevşek satırı bile (0,024) ölçülenin altı katı. **Refleks bu işi görmüyor** — ve
raporun kendi sonucu da refleks orta çizgilerin azami kaldırmayı düşürdüğü için
"questionable value" olduğu.

Daha önce metinde duran "refleks kesitler 0,02–0,05 verir" cümlesi yalnızca
atıfsız değil, **bir mertebe yanlıştı**. Silmekle iyi etmişiz.

**Çözüm burulma.** Ok açısı uçları geriye taşıdığı için uçtaki negatif burulma
burun-yukarı moment üretir; mekanizma **geometrik**, kesitsel değil, o yüzden
simetrik kesitli VLM onu doğrudan hesaplayabiliyor. `kararlilik.py`'ye
`denge_burulmasi()` eklendi:

| uç burulması | denge α | C_m | C_Di | e | seyir L/D |
|---|---|---|---|---|---|
| 0° | 6,68° | −0,058 | 0,01077 | 0,993 | 12,65 |
| −4° | 8,20° | −0,034 | 0,01102 | 0,971 | 12,56 |
| −6° | 8,98° | −0,021 | 0,01141 | 0,938 | 12,43 |
| **−9°** | **10,16°** | **−0,001** | 0,01237 | **0,865** | **12,11** |

**Uçak −9° uç burulmasıyla, sıfır kamberle seyirde dengeleniyor.** Bedeli
**%4,3 seyir L/D**. Bu, makalede hiç sayılmamış bir kalem: kuyruksuz olmanın
kendi vergisi.

⚠️ **İlk sürümde bir hata yaptım ve düzelttim.** C_Di'yi C_L'de doğrusal ara
değerle almıştım; C_Di C_L'de **karesel**, o yüzden e > 1 gibi fiziksel olarak
imkânsız değerler çıkıyordu (0° için 1,069). Şimdi C_L = 0,45'i veren α ikiye
bölerek **aranıyor** ve C_D orada doğrudan okunuyor. C_m doğrusal olduğu için
onda ara değer meşru.

**Bir varsayım emekli oldu.** §6.2, açıklık verimini gerekçesiz 0,85
varsaymıştı ve menzil sayıları ona dayanıyor. Dengeli kanadın hesaplanan değeri
**0,865** — varsayım %0,6 ile elverişsiz tarafta. **Menzil sayıları
değişmiyor**, ama artık dayanağı var.

### 2. YATIŞ: ölçüm gereksinimi kuşatıyor, ama şeridin yükseklik yasası yanlış

**Traub 2024** (*Aerospace* 11(9):728), AR=3 kanat, **%2 veter** Gurney, düşük
Re rüzgâr tüneli. Kritik olan: **iç 2/3 açıklık** düzenlemesi de ölçülmüş — bizim
şeridimizin kapladığı fraksiyonun aynısı. Ölçülen katsayılardan
(C_Lα 0,065/derece, α_ZL −3,25°; temiz 0,059 ve −1,53°):

| temiz C_L | iç-2/3 Gurney ile | ΔC_L |
|---|---|---|
| 0,30 | 0,442 | 0,142 |
| 0,45 | 0,608 | **0,158** |
| 0,60 | 0,773 | 0,173 |

Gereksinimimiz **0,12** — ölçülen bandın **altında**. Ama iki fark var ve ikisi
de aynı yöne çekiyor: Traub'un çıtası **firar kenarında ve akışa dik**, bizimki
alt yüzeyde ve oklu; onun kanadı **oksuz ve dikdörtgen**. Yani gösterim değil,
**mertebe desteği**.

**Aynı karşılaştırma bir tasarım hatası ortaya çıkardı.** Traub'un çıtası her
yerde %2 veter. Bizim şerit 2→6 cm doğrusal artarken veter daralıyor:

| şerit boyunca | yerel veter | yükseklik | h/c |
|---|---|---|---|
| kök | 0,969 m | 0,020 m | %2,1 |
| orta | 0,682 m | 0,040 m | %5,9 |
| dış uç | 0,436 m | 0,060 m | **%13,7** |

Gurney tipi cihazlar %2 civarında **doyuyor**, sürükleme ise artmaya devam
ediyor. Şeridin iç ucu doğru rejimde, **dış ucu çok ötesinde**: değiştirdiği
kaldırmayla orantısız sürükleme üretiyor. **Yükseklik yasası veter daralmasını
takip etmeli**, ona karşı gitmemeli. Bu, tarifin değil **konfigürasyonun**
değişmesi demek.

### Ders

Bu iki sonuç da hafızadan değil, **PDF açılıp sayı gözle görülerek** çıktı. Biri
bir iddiayı çürüttü (refleks), biri bir iddiayı destekledi ama yanında bir
tasarım hatası gösterdi (şerit yüksekliği). İkisi de aramayla ya da hatırlamayla
bulunamazdı.

---

## 🔑 SAPMA KAYNAKLARI OKUNDU (09.09.2026) — biri doğruladı, biri uyardı

### NASA TM-4649 (Moul ve ark. 1995) — dört adet 60° ok açılı uçan kanat

Rüzgâr tüneli, α = −8°…48°. Dikey kuyruksuz hâlde:

> *"each of these wings possessed **unstable or essentially neutral values of
> directional stability** for most of the angles of attack tested."*

**Bizim C_n_β = 0 sonucumuz bir VLM tuhaflığı değil.** Ölçülmüş davranış bu.
İkinci bir kaynak (NACA TR-796) aynı şeyi deneyim olarak söylüyor:
*"directional stability at low angles of attack for the wing alone has generally
been found to be inadequate."*

**Ama aynı rapor bir uyarı da taşıyor.** Ok kanatlarda yüksek hücum açısında
**pitch-up**, ve *"became more severe as aspect ratio was increased"*. Bazı
konfigürasyonlarda **hung stall** — burun aşağı otoritesi kurtarmaya yetmeyen bir
denge noktası.

Onların en-boy oranı 1,15–2,15; bizimki **6,03**. Mekanizmaları hücum kenarı
girdap patlaması ve bizim 45°/35° ok açılı AR-6 kanadımız onu aynı biçimde
üretmez. **Ama trend bizim aleyhimize** ve ortaya çıktığı açılar bizim geçişte
geçtiğimiz 17–22° ile örtüşüyor. Geçiş kontrol edilebilirliğini **açık tutmak
için ikinci bir sebep** — ve dengeleme için zaten gereken burulmayı istemek için
ikinci bir sebep (burulma ok kanatta kök-önce perdövites verir, pitch-up'ın
klasik çaresi).

### NACA TR-796 (1944) — kuyruksuz uçaklarda uç finleri

Üç şey verdi, üçü de metinde yoktu:

**1. Mimari seçimi doğruluyor.**
> *"If the tailless airplane has a swept-back wing, the usual practice is to
> place the vertical tail surfaces at the tips rather than at the center section
> in order to take advantage of the longer moment arm."*

Uç çerçevelerini moment kolu ve iniş yapısı için koymuştuk; meğer yön kararlılığı
yüzeyinin de istediği yer orasıymış.

**2. Benim hesabım eksik ama muhafazakâr.** Fin'in **sürüklemesi** yarım açıklık
kolunda etki ediyor, yani *"the drag characteristics as well as the lift
characteristics exert an influence"*. Ve profil-sürükleme ilkesiyle çalışan
finler, kaldırma ilkesiyle çalışanlardan **daha etkili** bulunmuş. Ben yalnız
kaldırmayla boyutlandırdım (a_f = 4/rad) → **gereken alanı fazla tahmin
etmişim**, az değil.

**3. Yeni bir tasarım gereksinimi: toe açısı.** En-boy oranı ~2'nin altındaki
finler **toe-in**, orta/yüksek olanlar **toe-out** ister. Bizim çerçeveler 1,42 m
boyunda ve on milimetrelerce veterde — ikinci sınıfta, yani **toe-out**. Ve
toe-out'un bir tehlikesi var: arka fin perdövitese girecek kadar sapma olursa
**büyük bir kararsızlaştırıcı moment** doğuyor; toe-in'de tersine kararlılaştırıcı.

Yani kılıfın bir toe açısına ihtiyacı var, o açının bir işareti var, ve gereken
işaret yanında bir arıza kipi getiriyor. Metne §4.4 ve §8'e yazıldı.

### Ne transfer eder, ne etmez — dikkat edilen ayrım

| bulgu | transfer eder mi |
|---|---|
| kuyruksuz kanatta C_n_β ≈ 0 | **eder** — geometrik, yanal kuvvet yüzeyi yok |
| uçları dikey yüzey yeri olarak kullanmak | **eder** — ok açısı kolu uzatıyor |
| fin sürüklemesinin katkısı, toe açısı | **eder** — geometriden bağımsız |
| yüksek α'da yanal kararsızlık (girdap patlaması) | **etmez** — 60°/AR-2'ye özgü |
| pitch-up eğilimi | **belirsiz** — mekanizma farklı ama trend aleyhte; açık bırakıldı |

Kaynakça 19 (NACA TR-796) ve 20 (NASA TM-4649) eklendi.

---

## 🔑 ÇERÇEVENİN DAYANAĞI ÜÇE ÇIKTI (09.09.2026)

YZ3'ün 11. turdaki uyarısı: çerçevenin dış tutarlılık sınaması **tek** bir NASA
çalışmasına dayanıyordu, ve kendi §5.5 karşılaştırmamız (tilt'e 1,00 kredisi biz
verdiğimiz için) kanıt sayılamazdı. İki kaynak okundu, dayanak üçe çıktı.

### Bacchini & Cestino 2019 — **yapılmış** üç uçak, sıralama tam tersine dönüyor

*Aerospace* 6(3):26, Tablo 16:

| | E-Hang 184 (çokrotorlu) | Cora (lift+cruise) | Lilium (yönlendirilmiş itki) |
|---|---|---|---|
| disk yükü N/m² | **440** | 880 | 7500 |
| toplam askı süresi | **20,5 dk** | 16,5 | 12,1 |
| seyir hızı | 100 km/s | 180 | **252** |
| pratik menzil | 42 km | 107 | **203** |

**Askıda en iyi olan seyirde en kötü, seyirde en iyi olan askıda en kötü.** Para
birimlerinin ayrı olması tam olarak budur.

Ve yazarlar iki transferi kendi cümleleriyle söylüyor:
- Cora için: *"parasitic drag caused by the pylons and vertical thrust
  propellers increases the power required in cruise"* → **f₂**
- Lilium için: askısı o kadar güç isteyen ki *"requires batteries with higher
  specific power"*, ve *"the aerodynamic advantages of this configuration are
  balanced by higher demands on the batteries and on the power electronics"*
  → **f₂ kazanıldı, f₃ ödendi**, bir çerçeve aramayan bir yazar tarafından
  bir takas olarak adlandırılmış.

⚠️ Kanıt olarak zayıf yanı: üç uçak yalnızca mimaride değil kütle, görev ve
olgunlukta da farklı, yani mekanizmayı izole etmiyor. Güçlü yanı: **var olan
uçaklar**, ve sayıları kimsenin boyutlandırma döngüsünün çıktısı değil.

### Johnson & Silva 2022 — NASA'nın BEŞ araçlı sürümü

*The Aeronautical Journal* 126(1295):59–91, Tablo 3. Makale şimdiye kadar
2018'in **dört** araçlı sürümüne (Silva ve ark.) dayanıyordu. Yenisi bir
**tiltwing** ekliyor:

| konsept | L/D_e | tasarım brüt ağırlık (lb) |
|---|---|---|
| quadrotor, turboşaft | 4,9 | 3 678 |
| QSMR, turboşaft | 5,4 | 3 951 |
| yan yana, elektrik | 7,2 | 5 547 |
| lift+cruise, elektrik | 7,9 | **9 482** |
| lift+cruise, turbo-elektrik | 8,5 | 7 271 |
| **tiltwing, turbo-elektrik** | **8,6** | 6 584 |

**Dikkat: tiltwing hem seyirde en verimli hem de lift+cruise'dan hafif.**
"Seyirde en iyi olan en ağırdır" diyen bir çerçeve bu satırla çürürdü. Bizimki
onu demiyor: tiltwing kaçınma koşulunun çoğunu sağlıyor (aynı tahrik hem askıda
hem seyirde, açıkta bir şey kalmıyor) ve bedeli **mekanizma**. Bu, §5.5'in tilt
hattını kendi boyutlandırdığında bulduğu takasın aynısı — ve tilt ailesine karşı
hiçbir yerde üstünlük iddia etmememizin sebebi.

Ayrıca doğrudan alıntılanabilir bir transfer cümlesi verdi:
> *"the high cruise efficiency of the lift+cruise type reduces the battery weight
> compared to the quadrotor, but not enough to counter the increase in structure
> and propulsion weight, so the all-electric lift+cruise aircraft is the heaviest
> design."*

### Düzeltilen bir ifade

§3.7 "highest cruise efficiency of **the group**" diyordu. Dört araçlı küme için
doğru, beş araçlı küme için **yanlış** (tiltwing 8,6 ile önde). "of **that**
group" oldu ve tiltwing satırı açıkça yazıldı. Kaynak okunmasa bu hata
gönderimde kalırdı.

Kaynakça 21 (Bacchini & Cestino 2019) ve 22 (Johnson & Silva 2022) eklendi.

---

## 🔑 İZ İÇİNDEKİ ETKİN HÜCUM AÇISI — geçişin en büyük açık kalemi daraldı (09.09.2026)

Folk (arXiv:2412.06197), hibrit İHA geçiş literatürünün derlemesi. İçinde bizim
hiç hesaba katmadığımız bir mekanizma var.

**Bizim α'mız GEOMETRİK**: gövde ekseniyle hız vektörü arasındaki açı. Ama burun
pervanesinin izi kanadın iç yarısının üzerinden geçiyor, ve iz **gövde ekseni
boyunca** olduğu için bileşke akış gövde eksenine yaklaşıyor — yani o bölgede
yerel hücum açısı geometrik olandan **küçük**.

    |Va| = sqrt(|Vw|² + |Vi|² + 2|Vi||Vw| cos α)
    α_etkin = arcsin(|Vi| sin α / |Va|)

Vw momentum kuramından: T = 2ρA(V+v)v → v; tam gelişmiş izde Vw = 2v, kanat
hizasında henüz gelişmemişse Vw = v. Hangisi doğru bilinmediği için **ikisi de**
veriliyor.

| durum | geometrik | Vw = v | Vw = 2v |
|---|---|---|---|
| hafif, tırmanışla | 17,5° | 6,8° | 4,2° |
| hafif, duragan | 21,6° | 3,7° | 2,0° |
| ağır, duragan | 20,5° | 7,6° | 4,6° |
| ağır, tırmanışla | 5,4° | 4,7° | 4,2° |

**İz kanat alanının %50'sini (hafif) ve %63'ünü (ağır) kaplıyor.** Yani geçişin
en yüksek açılı anında bile **kanadın yarısı bağlı akışta.**

### Ne demek

§7.6'nın C_m bütçeleri, kanadın **tamamının** geometrik açıyı gördüğünü varsayarak
hesaplanmıştı. Yani **temkinliler**. Ve borçlu olduğumuz ölçüm daraldı: mesele
kanadın **dış** yarısı, izin dışında kalan kısım.

### Sınırlar (metne yazıldı)

- Folk, indirgenmiş modelin ~8 m/s üzerinde iz hızını **fazla tahmin ettiğini**
  kaydediyor (Reddinger'e atıfla). Dört durumdan üçü sınır içinde; dışında kalan
  tek durum (ağır, tırmanışla, 35,6 m/s) zaten yalnızca 5,4° geometrik açıda.
- Modelin doğrulaması Folk'ta Misiorowski'ye atfediliyor ve **onu okumadık**.
- Kaynak bir doktora yeterlik raporu, hakemli makale değil. Böyle anıldı.

`zarf.py`'ye `etkin_alfa()` eklendi. Kaynakça 23.

---

## ⚠️ KENDİ HATAM — açıklık verimi karşılaştırmasında kategori hatası (09.09.2026)

Burulma bulgusunu yazarken şunu söylemiştim: *"makalenin varsaydığı e = 0,85 ile
hesaplanan 0,865 arasında %0,6 fark var, varsayım elverişsiz tarafta ve doğru
çıktı; menzil sayıları değişmiyor."*

**Yanlış.** İkisi aynı büyüklük değil, ve bunu §6.6 zaten yazıyor:

- VLM'in verdiği **0,865 ISKOZ OLMAYAN (inviscid)** açıklık verimi.
- §6.2'nin varsaydığı **0,85 OSWALD** verimi — kaldırmaya bağlı iskoz
  sürüklemeyi de taşıyor.

§6.6'nın kendi zinciri: Oswald ≈ inviscid × 0,85–0,90. O zaman:

| | inviscid | ima edilen Oswald | varsayılan 0,85 |
|---|---|---|---|
| burulmasız (uçamaz) | 0,99 | 0,84–0,89 | **içinde**, alt ucunda → temkinli |
| burulmalı (uçar) | **0,865** | **0,735–0,78** | **ÜSTÜNDE** → iyimser |

Yani karşılaştırmayı doğru yapınca sonuç tersine dönüyor: **denge için gereken
burulma, açıklık verimi varsayımını güvenli kılan payı yiyor.** Eğer 0,85–0,90
oranı doğruysa seyir L/D 12,04 değil **11,4–11,7**, ve menzil %3–5 düşer
(1598 → 1518–1550 km).

### Ama düzeltmeyi YAPMADIM, ve sebebi

**0,85–0,90 oranı da kaynaksız.** §6.6'da genel bilgiden alınmış ve atfı yok.
Kaynaksız bir oranı bir başlık sayısına yaymak, belirtilmiş bir varsayımı
belirtilmemiş bir varsayımla değiştirmek olurdu.

Kaynak gerektirmeden söylenebilen **yapısal** nokta ise yazıldı: §6.6'dan önce
varsayım bir hesapla **üstten sınırlıydı**; artık değil. Menzil sayılarının doğru
olup olmadığı, bu çalışmada kimsenin ölçmediği bir katsayıya bağlı. §7.6, §6.6 ve
§8'e böyle geçti.

**Gereken iki şey:** (1) inviscid/Oswald oranı için bir kaynak, (2) burulmalı
kanadın iskoz hesabı.

---

## VLM'in metodolojik dayanağı (09.09.2026)

Artık **dört** sonuç VLM'den geliyor: açıklık verimi, tarafsız nokta, denge
burulması, yatış sönümlemesi. Dayanağı okundu.

**Falkner (ARC R&M 2749, 1952)** hangi büyüklüklerin hızlı, hangilerinin yavaş
yakınsadığını ayırıyor:

> *"the grading of spanwise circulation converges quickly"* · *"the local
> aerodynamic centre can be adequately defined by the use of two chordwise terms
> only"* · ama *"a reasonably accurate calculation of pressure distribution in
> the neighbourhood of a discontinuity in plan would require at least three or
> four terms."*

**Bizim aldığımız her büyüklük birinci sınıfta** (dolaşım ve aerodinamik merkez),
hiçbiri ikinci sınıfta (basınç dağılımı). Ve bu, yakınsama çalışmamızın bulduğuyla
birebir uyuşuyor: tarafsız nokta üç kat çözünürlükte %0,26 oynadı, ama açıklık
verimi varsayılan çözünürlüğün dört katına kadar **1'in üstünde** değerler verdi —
düzlemsel kanatta fiziksel olarak imkânsız, ve **çözülmemiş bir planform
süreksizliğinin imzası.** Bizim planform kırpılmış, yani süreksizliği var.

**Smith & Bhateley (NASA 1976)** sınırı işaretliyor: düşük en-boy oranı + yüksek
ok açısında hücum kenarı girdap ayrılması baskın ve doğrusal yöntem **emme
benzeşimiyle** genişletilmeli. Bizim seyir koşulumuz o rejimde değil (AR 6,03,
45° kök oku, α < 11°) — ama §7'nin geçiş açıları **o rejimde**. Orada hiçbir VLM
sonucu anılmıyor, ve sebebi artık yazılı.

Kaynakça 24 ve 25.

---

## S1 kısmen kapandı: sonuç orandan bağımsız (09.09.2026)

Traub 2024'ün Tablo 1a (ölçülen Kp) ve Tablo 2'sinden (AVL Kp) türettim,
AR = 3, e = 1/(π·AR·Kp):

| | ölçülen e | inviscid e | oran |
|---|---|---|---|
| düz | 0,947 | 1,001 | **0,946** |
| dairesel | 1,220 | 1,206 | 1,011 |
| köşegen | 1,179 | 1,105 | 1,067 |

⚠️ İkisi 1'in üstünde. Gerçek bir kanatta iskoz verim inviscid'i geçemez;
Traub duvar düzeltmesi uygulamadığını yazıyor ("tests were comparative in
nature"), yani bu bir artefakt. **Veri oranı sabitlemiyor.**

**Ama sonuç orana ihtiyaç duymuyor:** 1'in altındaki her oran için
burulmalı Oswald verimi 0,85'in **altında** kalıyor (0,735–0,822) ve seyir
L/D 12,04'ün **altında** (11,44–11,90). İşaret kesin, büyüklük açık: %1–5.

Metin buna göre yazıldı: oran seçilmiyor, tablo veriliyor, ve "iskozitesi
olan her kanat için" ifadesiyle sonuç orandan bağımsız kılınıyor.

Ayrıca Ugwueze 2023, AR 7,0'lık bir powered-lift eVTOL için **aynı 0,85'i**
kullanıyor — yani bizim varsayımımız dikkatsizlik değil konvansiyon, ve bu
yüzden bu kadar uzun sorgulanmadan kaldı. Metne bir cümleyle girdi.

## Wang & Zhou 2022 (küçük BWB İHA) — dengeleme her yolda pahalı

⚠️ Bu bölümü ilk yazdığımda kaynağa **"Zhang 2022"** demişim. Yanlış:
yazarlar Kelei Wang ve Zhou Zhou (*Aerospace* 9(1):36). Dosya
`Wang-Zhou-2022_...pdf` olarak yeniden adlandırıldı. Kaynakçada [44].

Onlar dengeyi **burulmayla değil refleksle** kuruyor, ve şunu yazıyorlar:
kesitlerin geniş açıklıkta refleks taşıması *"is not conducive to the
improvement of overall lift-to-drag performance."*

Yani BWB'de dengeye giden iki yol var — refleks ve burulma — ve **ikisi de
seyir verimi yiyor.** Bizim %4,3'ümüz yanlış yol seçmenin cezası değil,
kuyruksuz olmanın cezası. §5.4'ün beşinci defter kalemi bu okumayla
sağlamlaştı.

➕ **12.09.2026 eki.** Lampropoulos 2025 refleksle dengelemeyi *başarıyor*
(2,44° burulma yetiyor). Wang & Zhou'nun cümlesi o başarının **fiyatını**
söylüyor. İkisi birlikte okununca §5.4'ün çerçevesi doğrulanıyor: refleks
yolu **var**, ama bedava değil — bizim %4,3'ümüzün karşılığı orada L/D
kaybı olarak ödeniyor.

---

## Shinde 2020 — refleks ailesi bir mertebe yetersiz, ve bu artık kanıtlı

Uçan kanat için özel olarak derlenmiş **on refleks kesit** (E184, E186, E387,
FX69H083, NACA M5, M6, S5010, S5020, MH60, HS-522), XFLR5 ile hesaplanmış.
Tablo 1'deki C_m0 değerleri:

| kesit | C_m0 | | kesit | C_m0 |
|---|---|---|---|---|
| E184 | −0,000124 | | M6 | −0,000251 |
| E186 | −0,000042 | | S5010 | −0,000133 |
| E387 | −0,000141 | | S5020 | −0,000151 |
| FX69H083 | −0,000451 | | MH60 | −0,000711 |
| M5 | −0,000471 | | HS-522 | −0,000859 |

**Hepsi 10⁻⁴ mertebesinde.**

⚠️ **Dikkat — bu kaynağı olduğu gibi almadım.** Makalenin kendi metni *"for
trim flight, pitching moment coefficient at zero angle of attack, Cm0, must be
positive"* diyor, ama tablodaki on değerin hepsi **negatif**. Kendi içinde
tutarsız. Ayrıca gerçek refleks kesitlerin C_m0'ı standart kaynaklarda 10⁻³–10⁻²
mertebesinde anılır, 10⁻⁴ değil. Yani ya işaret kuralı ters, ya
normalizasyon farklı.

**DÜZELTİLDİ (aynı gün).** İlk yazımda bu tabloyu "mertebe kanıtı" olarak
kullanmıştım. Kaldırdım. Uzlaştıramadığımız bir büyüklüğü, ihtiyatlı bir
cümleyle sarmalasak bile, aktarmayız — hakem haklı olarak "sayısından
şüphelendiğiniz bir makaleyi neden anıyorsunuz?" diye sorar. Kaynak artık
yalnızca **(a)** denge gereksiniminin ifadesi ve **(b)** pratik kesit ailesinin
listesi için anılıyor; **hiçbir sayı alınmıyor.**

Tek **ölçülmüş** değer NACA TR-460'ın 2R212'si: **+0,004**, 1933. Metin, bu tek
sayının seçimi taşıdığını açıkça söylüyor.

### Sonuç: refleks + burulma takası yok

C_m derece başına 0,00629 (VLM taramasından). Kesit ne verirse burulma gerisini
tamamlıyor:

| kesit C_m0 | gereken burulma | inviscid e | seyir L/D |
|---|---|---|---|
| 0 | 9,2° | 0,865 | 11,68 |
| **0,004 (ölçülen)** | **8,6°** | 0,875 | 11,73 |
| 0,020 | 6,0° | 0,937 | 12,01 |
| 0,050 | 1,3° | 0,986 | 12,21 |

**Kaldıraç gerçek** — 0,02 veren bir kesit denge cezasının neredeyse tamamını
geri kazandırırdı. Elimizdeki tek ölçümde refleks dokuz derecenin yarım
derecesini alıyor, yani denge bir **burulma** sorunu olarak kalıyor.

Makale **temkinli dalı** seçiyor (9° ve cezası) ve bunu bir cümleyle kayda
geçiriyor: *modern bir refleks kesidin C_m0 = 0,02'ye ulaştığını bilen bir
okuyucu, tablonun üçüncü satırını tasarım noktası olarak okumalı ve denge
cezasını büyük ölçüde geri kazanılabilir saymalı.* Böylece sonuç, tek bir
1933 ölçümüne körü körüne bağlanmıyor — bağımlılık görünür oluyor.

**Bu, S4 olarak bekleyen sorular listesine girdi ve şu an oradaki en önemli
madde.**

Bu, burulma bulgusunu "uygun bir çözüm"den **zorunlu çözüme** çeviriyor.

Kaynakça 27.

---

## 🔑 GEÇİŞ LİTERATÜRÜ — açık kalemimiz alanın açık kalemiymiş, ve bir uyarı (09.09.2026)

Merak ettiğim soru: *başkaları geçişteki aerodinamik momenti nasıl elde etmiş —
ölçmüşler mi, yoksa onlar da mı varsaymış?*

### Cevap: varsaymışlar, hatta bizden az

**Li ve ark. 2020** (*IEEE/ASME Trans. Mechatronics*, açık hava uçuş denemeli):
aerodinamik modelini **yayımlanmış 2-B NACA 0012** kaldırma/sürükleme verisini
hücum açısı boyunca uydurarak kuruyor, kendi profilinin *"not exactly the same"*
olduğunu yazıyor, hatayı model-tabanlı denetleyici için kabul edilebilir sayıyor
— ve **hareket denklemlerinde hiç yunuslama momenti terimi taşımıyor.**

**Lyu ve ark. 2017** (IROS, uçuş denemeli): taşıyor ama **doğrusal** biçimde,
C_m = C_m0 + C_mα·α + C_mδ·δ, ve bunu manevranın tamamında kullanıyor.

Yani alanın pratiği: **ödünç bir kesit poları + kapalı çevrim.** Bizim §7.4'ün
kaldırma/sürükleme için yaptığının aynısı, moment için yaptığımızdan ise **daha
azı.** Açık kalemimiz alanın ortak açık kalemi.

### Ve bir UYARI — bizim tam sorumuzu uçuşta denemişler

Lyu ve ark. aracı **elevonlu ve elevonsuz** karşılaştırıyor. Elevonsuz hâlde,
yani **yalnız pervane fark itkisiyle** — bizim gibi:

> *"a well-controlled attitude response during hovering and transition"* ✓
> ama seviye uçuşta manevralar *"cause an oscillatory attitude response"*,
> **"motor saturations are observed"**, ve sebep:
> *"the increased aerodynamic moment but decreased motor thrust at high-speed
> level flight."*

**Bu, §7.6'nın moment bütçesinden çıkardığımız yapısal gerilimin uçuşta
gözlenmiş hâli.** Dar durum dönüşün yüksek açılı ORTASI değil, **SONU ve
ötesi**: aerodinamik moment V² ile büyürken pervane itkisi düşüyor.

⚠️ **Benzetmeyi fazla zorlamamak lazım** ve metinde öyle yazıldı: onların
yunuslama pervaneleri aracın **taşıyıcı rotorları**, kanat üzerinde ve kısa
kollu; bizimkiler 0,71 m çerçevelerde **adanmış kontrol pervaneleri**; araçları
daha küçük. Ama mekanizma aynı ve **gerçek bir uçağı doyurmuş.**

### Sonuç

Bu, dönüş sonundaki 0,050 ve 0,010'luk bütçelerin bu bölümün **bağlayıcı**
sayıları olduğunun en güçlü dış kanıtı. Ve pervane-tek kuyruk-üstü bir aracın
yunuslama otoritesinin **açıda değil hızda** sınanması gerektiğinin.

Kaynakça 28 ve 29.

---

## Carter 2021 (VT tezi) — iki şey: bir öncül, bir de ikinci kanıt

### 1. Kontrol ilkemizin öncülü var, ve bunu SÖYLEMEK lehimize

> *"One way to generate a larger pitching moment to assist with the transition
> from vertical to horizontal flight is to **add propellers away from the axis of
> rotation** of the tailsitter and **apply a differential thrust** to these
> propellers. This idea was explored at NASA AMES almost two decades ago."*

Bu, birebir bizim §4.4'ün ilkesi. Hakem bunu bulacak; ondan önce bizim
yazmamız iyi. §4.4'e eklendi, ve **neyin özgün olduğu** netleştirildi: mekanizma
değil, **kol ve muhasebe** — çerçeveler uç veterinin kesri değil **üç katı**
kadar uzanıyor, ve zaten gereken yapı oldukları için kol iniş takımına
faturalanıyor, kontrol sistemine değil.

⚠️ NASA AMES çalışmasını **okumadık**; Carter'ın ifadesine atıf veriliyor,
NASA raporuna değil.

### 2. "Geçiş tamam, seyir sorunlu" — İKİNCİ bağımsız örnek

UMD'nin CRC-20'si, rüzgâr tünelinden türetilmiş aerodinamikle:

> *"They were able to achieve transition to forward flight, but they had
> **poor control over the vehicle once in forward flight**."*

Lyu'nun motor doyması bulgusuyla **aynı bölünme**, farklı araç, farklı grup.
İki bağımsız program: **geçiş geçildi, seyir zor.**

Bu artık tek bir gözlem değil, bir **örüntü**. Ve tam olarak §7.6'nın kendi
bütçesinden çıkardığı yer: dar durum dönüşün sonu.

### 3. Yan bulgu — yöntemimize destek

"Morphing winglet tailsitter" projesi kanatçık dihedral açılarındaki kaldırmayı
**VLM ile** belirleyip sonra **deneyle doğrulamış**. Yani kuyruk-üstü bir aracın
taşıyıcı yüzeylerinde VLM kullanmanın uçuş-denemeli bir öncülü var.

### Dört bağımsız grupta ortak örüntü

| grup | L, D nereden | C_m nasıl |
|---|---|---|
| Li 2020 | ödünç NACA 0012 poları | **yok** |
| Lyu 2017 | — | doğrusal C_m0+C_mα·α+C_mδ·δ |
| Tohoku | rüzgâr tüneli | anılmıyor |
| UMD CRC-20 | rüzgâr tüneli | anılmıyor |

**Hiçbiri geçiş boyunca ölçülmüş bir C_m eğrisi kullanmıyor.** Bizim açığımız
alanın açığı — ve bunu artık dört örnekle söyleyebiliyoruz.

Kaynakça 30.

---

## Ross & Storms 1997 + Cheng & Pei 2024 (09.09.2026)

### 1. Şeridin yükseklik eşiği artık ÖLÇÜLMÜŞ ve ATIFLI

Daha önce "Gurney cihazları %2 civarında doyuyor" demiştim — **genel bilgiden**.
Şimdi ölçülmüş bir eşik var. NASA TM-112990, **basınç yüzüne** ve **firar
kenarına yakın ama tam üstünde değil** yerleştirilen "lift-enhancing tab"lar —
yani yayımlanmış literatürde bizim şeridimize **geometrik olarak en yakın**
cihaz:

> *"For flap heights less than about **1.5% c**, the maximum L/D can also
> increase. Flap heights greater than 1.5% c cause a **decrease** in the maximum
> L/D."*

Bizim şeridin her istasyonu bu eşiğin üstünde, dış ucu **dokuz katı**.

⚠️ **Ama bu eşik takası kapatmıyor** ve metinde öyle yazıldı: eşik **sürekli
açık** duran bir cihaz için. Bizimki yalnızca yatış komut edilirken açılıyor,
yani seyir sürüklemesi cezası **yapısı gereği aralıklı**. Ödemek açıkça yanlış
değil.

### 2. YENİ BULGU — şerit ters sapma üretiyor, ve bunu hiç yazmamışız

Şerit bulunduğu yarı kanadın **hem kaldırmasını hem sürüklemesini** artırıyor.
Uçak şeritten **uzağa yuvarlanıyor**, şeride **doğru sapıyor** — klasik ters
sapma (adverse yaw).

| yükseklik yasası | sürükleme | ters sapma momenti | sapma otoritesinin |
|---|---|---|---|
| mevcut (2→6 cm) | 16,7 N | **11,3 N·m** | %20–26'sı |
| sabit h/c = %2 | 5,7 N | 2,9 N·m | %5–7'si |

Mevcut sapma otoritesi 42,8–55,9 N·m. **Kapsanıyor** — ve tam da **en güçlü
eksen** tarafından kapsanıyor, ki sapmanın kolu yarı açıklık olduğu için öyle.
Ama bir kuplaj, yazılmamıştı, ve bir kontrol tasarımı buna pay ayırmak zorunda.
§4.4 ve §8'e eklendi.

### 3. "Transition corridor" — alanın bizim §7 için kullandığı ad

Cheng & Pei 2024: geçişin olurlu durum kümesine **geçiş koridoru** deniyor ve
karmaşık bir uçak modeli üzerindeki yörünge üretimini kısıtlı bir hareket
planlama problemine çeviriyor. Bizim §7.4'ün zarfı ve buradaki moment sınırları
tam olarak böyle bir koridor.

**Ve nerede uçulacağı konusunda alanın yerleşik görüşü var:**

> *"existing transition-corridor-based studies only try to plan the flight
> trajectory in the **middle of the corridor**, considering that the corridor
> bounds might be **sensitive to aerodynamic uncertainties and disturbance**."*

**Bizim referans dönüş süreleri koridorun tam SINIRINDA** (2 s ve 5,1 s,
eyleyici sınırlı alt sınırlar). Yani alanın kaçınmayı önerdiği yerdeyiz. Bu,
§7.6'nın kendi tavsiyesini — "bir tasarım yinelemesi her iki dönüşü de dörtte
bir uzatırdı" — **dışarıdan destekliyor**, ve alıntılanan 2 s / 5,1 s'nin
tasarım değil **yaklaşılan sınır** olarak okunması gerektiğini söylüyor.

Kaynakça 31 ve 32.

---

## 🔑 Buchholz 1993 — şerit ÜÇ EKSENİ birden yüklüyor (09.09.2026)

60° delta kanat, rüzgâr tüneli, ve kritik olan: **konik yükseklikli Gurney flap,
h/c_kök = 0,02 ve 0,05'te test edilmiş.** Bizim şeridin yükseklik yasası da kök
veterine göre %2,1 → %6,2. **Aynı geometrik aile, aynı aralık.**

### Ölçülmüş sonuç

> *"The flap **significantly increases nose down pitching moment**."*

Ve kaldırma eğrisinde **10°'ye varan kayma** (bizim ΔC_L = 0,12 gereksinimimizin
çok üstünde bir yetenek), fence'lerin aksine flap **L/D'yi yüksek kaldırma
katsayılarında artırıyor.**

### Bunun bizde karşılığı: üçüncü kuplaj

Şerit tek yarı kanatta açılınca:

1. **yatış** (istenen)
2. **ters sapma** (geçen tur bulundu): 2,9–11,3 N·m, sapma otoritesinin %5–26'sı
3. **burun aşağı yunuslama** (bu tur): artışın veter boyunca nerede doğduğuna bağlı

| artış nerede etkiyor | moment | ΔC_m |
|---|---|---|
| orta veter | 3,7 N·m | 0,005 |
| ¾ veter | 13,2 N·m | 0,019 |
| firar kenarı (üst sınır) | 22,7 N·m | **0,032** |

**§7.6'nın en dar yunuslama bütçesi 0,050** (dönüş sonu). Üst sınırda şerit
açmak bunun **üçte ikisini** yiyor.

### Çıkan gereksinim — yeniden tasarım değil, ÇİZELGELEME

**Yatış şeridi dönüşün sonunda komut edilmemeli** — yunuslama ekseninin en az
payının olduğu tek faz orası. Makale şeridin ne zaman kullanılabileceğine dair
hiçbir kısıt tanımlamamıştı; şimdi var.

⚠️ **Aşırı transfer etmedim.** Buchholz'un flapı **firar kenarında**; bizimki
%15 kök veterinden başlıyor ve köşegen. Yani kol daha kısa, moment daha küçük.
İşaret biliniyor, büyüklük **bracket** olarak veriliyor, ve artışın veter
boyunca nerede doğduğunun bu makalede hiç hesaplanmadığı §8'de yazılı.

Kaynakça 33.

---

## 🔑 KULLANICININ SORUSU — uç pervaneleri seyirde ne yapıyor? (09.09.2026)

Bu, makalede **hiç sorulmamış** bir soruydu ve kullanıcı sordu. Cevabı, konfigürasyonun
çalışıp çalışmamasını belirliyor.

Sekiz uç rotoru 0,20 m çapında; toplam disk alanı **0,2513 m²**, yani kanat
alanının **%12,7'si**. Yanlış durumda hava akışında bırakılacak küçük bir cisim değil.

| seyirde uç rotorları | ΔC_D0 | 0,0248'in |
|---|---|---|
| sıfır şaft yükünde serbest dönüyor | 0,0003–0,0008 | **%1–3** |
| kenarına durmuş, azimut seçilmiş | 0,0008 | %3 |
| **yassı durmuş, azimut denetimsiz** | **0,015–0,018** | **%61–74** |

**Birinci ile üçüncü satır arasındaki fark, çalışan bir konfigürasyonla
çalışmayan bir konfigürasyon arasındaki fark.** Ve varsayılan katsayılara
duyarsız, çünkü iki durum arasında **otuz kat** var.

### Ve bir ironi: §5.2'nin kendi iddiası tehlikedeydi

§5.2 şunu söylüyordu: *"A configuration with no rotor to stop needs neither
[indeksleme ne de geri çekme]."* Ama **uç çiftleri de rotor.** Seyirde
duruyorlarsa, iddia çöküyor — indeksleme mekanizması gerekirdi (ikinci satır).

**Serbest döndürmek, §5.2'nin iddiasını AYAKTA TUTAN şey.**

### Çözüm donanım değil, bir kontrol durumu

Sabit hatveli bir pervane serbest bırakılınca net şaft torkunun sıfır olduğu
ilerleme oranına oturur: iç kesitler sürüyor, dış kesitler frenliyor, dengeleniyor.
O noktada şaft iş yapmıyor — motor ne sürüyor ne frenliyor, elektriksel maliyet
denetleyicinin bekleme akımı ve yatak kayıpları. Kanatlar düşük hücum açısında,
akış ekli. **Bedava.**

### İki yeni sonuç

1. **§4.3'ün sabit hatve kararı feathering'i tasarım uzayından çıkarıyor.** Yani
   seçenek sadece ikisi: serbest dön ya da dur. Bu, argümanı "elverişli"den
   **belirleyici** hâle getiriyor.
2. Bu bir **kullanılabilirlik** gereksinimi: sekiz rotordan birinde sıkışmış
   yatak ya da fren arızası artık bir kontrol sorunu değil, **sürükleme sorunu**
   — ve büyük bir tanesi. Güvenilirlik analizi yok.

⚠️ Pervaneye özgü hiçbir hesap ya da ölçüm yok; doluluk ve kesit sürükleme
katsayısı **varsayım**. Sağlam olan **oran**, değerler değil. §8'e böyle yazıldı.

**Not:** Kullanıcı bu soruyu kendi mühendislik sezgisiyle sordu; kaynak
okumasından çıkmadı. Aç-kapa şeridin üç ekseni birden yüklediğini de önceden
biliyormuş. Bu turların bir kısmı, benim hesaplayarak vardığım yerlere onun
zaten sezgiyle varmış olduğunu doğrulamakla geçiyor.

---

## NASA TM-78767 (kuyruksuz ok kanatlı kargo uçağı) — toe açısının BÜYÜKLÜĞÜ (09.09.2026)

Uç podlarında dikey kuyruk taşıyan, kuyruksuz, ok kanatlı bir kargo
konfigürasyonu; rüzgâr tüneli.

**1. Toe açısı ölçülmüş: optimum ~1,5°.**
> *"the optimum toe-in angle appears to be about 1.5 degrees"* (simetrik kesitli
> kuyruklar; kamberli olan toe'ya "relatively insensitive").

S3'ün **büyüklük** kısmı kapandı: açı **bir-iki derece mertebesinde**, on değil.
Ve maliyeti küçük.

**2. Fin alanı L/D'yi neredeyse etkilemiyor.**
> *"(L/D)max is about the same with all three vertical-tail designs,
> **notwithstanding the 75% larger area** of VT2."*

Bu, bizim "gereken fairing veteri zaten olması gerekenin içinde" argümanımızın
**ölçümle gelen hâli** — tahminle değil.

**3. Üçüncü bağımsız doğrulama.**
> *"The destabilizing effect of adding nacelles to the podded wing is noted.
> The further addition of vertical tails **restores directional stability**."*

Kuyruksuz kanat yön kararsız; uçtaki dikey yüzeyler geri getiriyor. Artık üç
kaynak: TM-4649, TR-796, TM-78767.

### Açık kalan: İŞARET

| kaynak | fin AR | önerdiği |
|---|---|---|
| TM-78767 | düşük (pod kuyruğu) | **toe-in** ~1,5° |
| TR-796 | AR < 2 → toe-in, orta/yüksek → **toe-out** | işaret AR'a bağlı |
| **bizim çerçeveler** | **~20–28** | **iki kaynağın da aralığı dışında** |

Ve TR-796'nın uyarısı duruyor: toe-out'ta arka fin perdövitese girerse
**kararsızlaştırıcı** moment. Yani işaret seçimi bir arıza kipi seçimi.

S3 buna göre güncellendi: büyüklük bulundu, işaret soruluyor.

Kaynakça 34.

---

## 🔴 EN CİDDİ BULGU — tampon özgül gücü (09.09.2026)

Bacchini & Cestino 2019, eVTOL boyutlandırırken güç uygulamaları için Li-ion
özgül gücünü **paket düzeyinde** veriyor:

> *"Li-ion batteries for power applications have specific energy ranging from
> 100 to 250 Wh/kg and **specific power from 700 to 1300 W/kg**."*
> (Tesla Model S paketi: 735 W/kg, 157 Wh/kg — kasa, bağlantı ve termal
> yönetim dahil.)

**Bizim tampon 4,6 kW/kg istiyor.** Yani bu bandın üst ucunun **3,5–6,6 katı.**

| özgül güç | tampon kütlesi | MTOW'un |
|---|---|---|
| 0,735 kW/kg (onların varsaydığı paket) | 11,3 kg | %22,6 |
| 1,30 kW/kg (bandın üst ucu) | 6,4 kg | %12,8 |
| **4,61 kW/kg (bizim örtük varsayımımız)** | **1,8 kg** | **%3,6** |

Bandın üst ucunda tampon bütçelenenden **4,6 kg ağır**; elimizdeki pay 2,2 kg.
**Hafif hattın kütle bütçesi kapanmaz.**

### Savunma gerçek ama savunma

Onların rakamları **enerji için optimize edilmiş otomotiv paketi**; bizimki bir
dakika boşalan, **güç için optimize edilmiş** bir tampon — farklı ürün. Ama
okuduğumuz hiçbir kaynak o ürün için özgül güç vermiyor. Yani varsayım şu:
**kısa süreli bir tampon, otomotiv paketini 3,5–6 kat geçer.** *Türü itibarıyla
makul, büyüklüğü itibarıyla doğrulanmamış, ve Fatura 3 buna dayanıyor.*

### ⚠️ DÜZELTME (aynı gün) — enerji tarafını fazla sıkmışım

Kullanıcı haklı çıktı ve bu benim hatamdı. Tamponun **60 s boyunca sürekli**
boşaldığını varsaymıştım. Öyle değil: kalkışta boşalıyor, **dönüş başlayınca
kanat devralıyor ve talep düşüyor**, sonra saatlerce seyirde motordan doluyor,
inişte tekrar boşalıyor.

T/W = 1,2'de düşey ivme 0,2g; §7.4'ün girdiği 5 m/s tırmanışa **2,6 s ve 6,4 m**
sonra ulaşılıyor. Yani tam çekişli kalkış segmenti 10–20 s, 60 değil.

| kalkış segmenti | enerji | 180 Wh/kg'nin | 80 Wh/kg'nin |
|---|---|---|---|
| 10 s | 23 Wh | %7 | %16 |
| 20 s | 46 Wh | %14 | **%32** |
| 30 s | 69 Wh | %21 | %48 |

**Yüksek güçlü kimyanın düşük enerji yoğunluğunda bile 20 s'lik kalkış tamponun
üçte birini kullanıyor.** Yani "80 Wh/kg'de pay bitiyor" ifadem yanlıştı —
60 s'lik sürekli boşalma varsayımının ürünüydü. Enerji **bağlayıcı değil.**

### Ama güç tarafı geçici değil, ZEMIN

Kullanıcının "geçici taşma sorun olmaz" savı burada geçerli değil, ve sebebi
aritmetik: hover gücü T^1,5 ile gidiyor, yani T ~ P^(2/3).

| tampon özgül gücü | toplam güç | çıkan T/W | yerden kalkar mı |
|---|---|---|---|
| 0,735 kW/kg | 3,9 kW | 0,61 | **hayır** |
| 1,30 kW/kg | 4,9 kW | 0,71 | **hayır** |
| 2,50 kW/kg | 7,1 kW | 0,90 | **hayır** |
| 4,61 kW/kg | 10,9 kW | 1,20 | evet |

**Atıf verebildiğimiz özgül güçlerde uçak yerden kalkmıyor.** Tolere edilecek
kısa bir taşma yok, çünkü ortada kalkış yok. Tek çare daha ağır tampon — bu
yüzden bir **kütle bütçesi** açığı, uçuş dinamiği açığı değil.

### (eski hâli — 60 s varsayımıyla, artık geçersiz)

Gücü veren kimya daha az enerji taşır. Dikey faz ~60 s (makalenin kendi "bir
dakika mertebesinde" ifadesi):

| tampon enerji yoğunluğu | enerji sınırına | 60 s'ye göre pay |
|---|---|---|
| 180 Wh/kg | 141 s | 2,3× |
| 120 Wh/kg | 94 s | 1,6× |
| 100 Wh/kg | 78 s | 1,3× |
| **80 Wh/kg** | **62 s** | **1,0×** |

**80 Wh/kg'de pay tamamen bitiyor.** İki gereksinim birbirini çekiştiriyor.

### Değerlendirme

Bu, kabuk yüzey yoğunluğundan (1,5 kg/m²) **daha ciddi** bir açık: kabuk
"hedef" diye yazılıydı ve başabaşı biliniyordu; tampon özgül gücü ise hiç
kaynakla karşılaştırılmamıştı ve karşılaştırınca **bir mertebe yakın** çıkmadı.

§6.7 ve §8'e tablolarıyla yazıldı. Kullanıcının "acaba yeterli mi" sezgisinin
en somut karşılığı bu.

---

## ⚠️ TASARIMCI DÜZELTMESİ — şerit aç-kapa DEĞİL, çıkma miktarı sürekli (09.09.2026)

Kullanıcı (tasarımcı) belirtti: şeridin **çıkma miktarı esnek**, aç-kapa değil.
Makale dört yerde "on-off" diyordu ve bu **yanlıştı**. Düzeltildi.

### Neyi değiştirdi

**1. Sınır çevrimi analizi artık ÜST SINIR, tarif değil.**
±0,2° (50 ms) / ±9,4° (150 ms) rakamları, cihaz iki konuma indirgenseydi ne
olacağını gösteriyor. **Sürekli çıkışta o sınır çevrimi hiç oluşmuyor.** Yani
eyleyici hız gereksinimi bir *tavan*, bir *şart* değil.

**2. Kuplajlar çıkma miktarıyla ölçekleniyor.** Ters sapma (2,9–11,3 N·m) ve
burun aşağı yunuslama (ΔC_m 0,005–0,032) **tam açılmada** hesaplanmıştı. Kısmî
açılmada o kesir kadar. Dolayısıyla dönüş sonundaki çizelgeleme kısıtı, **tam
açılmaya** getirilmiş bir kısıt; küçük düzeltmeler her fazda kullanılabilir.

**3. Yükseklik sınırı kütleden değil KUPLAJDAN geliyor.** Kullanıcının işaret
ettiği nokta: şeridin kendi yapısı küçük bir kalem, yani 10 cm yerine 20 cm de
benzer kütle bütçesiyle mümkün. Ne kadar uzayabileceğini belirleyen şey, uç
pervanelerinin soğurabileceği sapma ve yunuslama bozulması — yani §4.4'ün kendi
hesabı. Bu, metne aynen böyle yazıldı.

### ⚠️ Konumlandırma riski — kullanıcıya sorulacak

Sürekli çıkışlı bir spoiler/çit, olağan anlamda bir **kumanda yüzeyidir**.
Makalenin ayırt edici cümlesi "no elevons, no rudder, no tilting mechanism" ve
§5.4 zaten şeridi "the one moving aerodynamic device" diye anıyor — yani
dürüstlük yerinde. Ama "aç-kapa, orantılı bir kumanda yüzeyi değil" cümlesi
şeridi kumanda yüzeylerinden **ayıran** ifadeydi ve o cümle artık yok.

Bir hakem şunu sorabilir: *"orantılı çıkışlı bir spoiler'ınız var; 'kumanda
yüzeyi yok' iddianız ne anlama geliyor?"* Cevap verilebilir (elevon/dümen yok,
menteşeli kumanda yüzeyi yok, tek cihaz var) ama **cevabın hazır olması lazım.**
Bu, YZ'lere sorulacaklar listesine girmeli.

---

## Yang 2020 — şeridin iki zayıf noktası, ikisi de bizim kullandığımız koşulda

Rüzgâr tüneli, DTU-LN221 profili, denetimli giriş türbülansı (%0,2 / %10,5 / %19),
Gurney yüksekliği %1–2 veter.

| bulgu | bizim için ne demek |
|---|---|
| *"became less effective after stall angle"* | geçiş, dış kanadın perdövites sonrasında olduğu açılardan geçiyor — yatış bozulmalarının en büyük olduğu yer |
| %19 türbülansta fayda *"negligible"* (%10,5'te +%2,7…+%14,4 L/D) | şeridin iç kısmı **kasten** pervane izinde, ve iz düşük türbülanslı değil |
| yükseklik çok önemli, kalınlık önemsiz | yükseklik yasası tartışmamızı destekliyor |

**İroni:** §4.4, şeridin izde olmasını bir **avantaj** olarak sunuyor ("sıfır
hızda bile çalışır"). Yang'ın ölçümü, izin aynı zamanda mekanizmanın **en zayıf
çalıştığı yer** olabileceğini söylüyor.

⚠️ Transfer sınırlı ve metinde yazılı: onların profili rüzgâr türbini profili,
türbülans ızgarayla üretilmiş serbest akış türbülansı, **pervane izi değil.**
Yön ölçülmüş, büyüklük aktarılamaz.

§4.4'e ve §8'e "asılı durumdaki yatış otoritesine ana risk" olarak yazıldı.

---

## 🔎 ARAMA SONUCU: kabuk yüzey yoğunluğu 35 kaynağın hiçbirinde yok

`kg/m2`, `areal density`, `structural mass fraction`, `empty weight fraction` —
otuz beş PDF'in tamamı tarandı, **sıfır sonuç.** Hafif hattın kütle bütçesinin
dayandığı 1,5 kg/m² için hâlâ tek kaynak yok. S7 olarak listeye eklendi.

---

## 🔴 Selig UIUC V1–V2 — S4'ü KAPATMIYOR, ve kapatamaz (12.09.2026)

S4 için arananı hatırlatayım: refleks bir kesit için **ölçülmüş** C_m0, kesit
adıyla. NACA TR-460'ın 1933'te ölçtüğü 2R212 → +0,004'ün *yanına* konacak,
daha güncel bir ölçüm.

**Selig bunu veremez, ve bunu kendisi yazıyor.** Cilt 1, s. 17:

> *"even though the current setup does not provide pitching moment data,
> airfoil moment coefficients have been determined computationally using either
> the Eppler, ISES or XFOIL code."*

Ve Bölüm 3'ün başında, Tablo 3.1'in hemen üstünde bir kez daha:

> *"The airfoil moment coefficients listed in Table 3.1 were determined
> computationally... The value given is representative of that over the low
> drag range."*

UIUC düzeneği **momenti hiç ölçmüyor**; taşıma ve direnç ölçülüyor, moment
hesaplanıyor ve yalnızca tünel düzeltmelerinde kullanılıyor. Yani bu iki cilt,
düşük Reynolds kesit verisinin en çok atıf alan deneysel derlemesi olmasına
rağmen, **bizim sorumuzun sınıfına ait bir sayı içermiyor.**

### Yine de çıkan üç şey

**1. Tablodaki tek uçan-kanat kesiti NEGATİF veriyor.**

| kesit | kalınlık | kamburluk | C_m,c/4 (hesaplanmış) |
|---|---|---|---|
| **MH45** (Repperle, *"designed for flying wings"*, hafif refleks) | %9,84 | %1,64 | **−0,006** |
| J5012 / NACA 0009 / NACA 64A010 / SD8020 (kuyruk kesitleri, simetrik) | %9–12 | %0,00 | 0,000 |
| geleneksel kamburlu kesitler (37 adet) | — | %1,5–10,2 | −0,012 … −0,290 |

MH45 açıkça uçan kanat için tasarlanmış, refleksli, ve hesaplanan momenti
**sıfırın altında.** Bu bizim lehimize bir sayı değil — aleyhimize. Refleksin
pozitif C_m0'ı bedavaya verdiği varsayımına karşı bir veri noktası, ve
Shinde'nin (hepsi negatif) tablosuyla aynı yöne bakıyor. İki bağımsız kaynakta
uçan-kanat kesitlerinin C_m,c/4'ü negatif çıkıyor.

⚠️ Selig'in kendi uyarısı var: *"The true characteristics of the MH45... are
difficult to ascertain from the polars since the wind-tunnel model was too
thick."* Model hatalı; ama C_m zaten modelden gelmiyor, koordinatlardan
hesaplanıyor — bu uyarı momenti kurtarmıyor.

**2. Tek pozitif değer refleks bir kesitten değil, KISITLI TASARIMDAN geliyor.**

M06-13-128 (B) — Miley, %12,81 kalınlık, **%5,16 kamburluk** — ve C_m,c/4 =
**+0,004.** Beş nokta kamburlukta pozitif moment, çünkü kesit bir *kısıt* altında
tasarlanmış; Selig şöyle diyor: *"the c_lmax is near 1.5, which is substantial
in light of the low pitching-moment constraint."*

Bizim için ilginç olan bu: **c_lmax ≈ 1,5 (Re 300k) ve C_m,c/4 ≈ +0,004 aynı
kesitte buluşabiliyor.** Denge zincirimizin istediği tam bu takas. Sayının
TR-460'ın ölçtüğü +0,004 ile birebir çakışması ise tesadüf sayılmalı — biri
ölçüm, öteki XFOIL/Eppler/ISES çıktısı.

⚠️ Selig aynı yerde uyarıyor: Re < 300k'da *"should not be given serious
consideration... owing to its high drag characteristics."* Bizim seyir
Reynolds'umuz bunun üstünde, ama kesit doğrudan alınacak bir aday değil.

**3. Kuyruk kesitlerinde sıfır etrafında doğrusalsızlık.**

Princeton'da denenen dört simetrik kesitin hepsi α ≈ 0'da taşıma eğrisinde
düzensizlik gösteriyor; NACA 64A010 en belirgini, ve Mueller & Batill'in
NACA 66₃-018'inde eğim 3°'lik bir bantta **işaret değiştiriyor.** Selig bunu
tam-hareketli stabilatör için uyarı olarak yazıyor. Bizde kuyruk yok, ama uç
finlerimiz düşük Re'de simetrik kesitli yüzeyler ve toe açısı tartışması (S3)
tam bu bandın içinde geçiyor: ~1,5°'lik bir toe açısı, doğrusalsızlığın
bulunduğu aralıkta duruyor. **S3'ün altına not edildi.**

### Karar

Selig, S4'ün cevabı değil; **S4'ün cevabının nerede olmadığını** gösteriyor.
Aranan şey düşük-Re model uçak kesit derlemelerinde yok, çünkü o tünellerin
çoğu momenti ölçmüyor. YZ'lere sorarken bunu açıkça söylemeliyiz, yoksa üçü de
bizi Selig'e yollar. Ölçülmüş C_m için gidilecek yer **moment ölçen** tüneller:
NACA/NASA raporları, ve düşük-Re tarafında Delft/Stuttgart tünel dizileri.

Makaleye **hiçbir Selig sayısı girmedi.** MH45'in negatifliği §8'e "refleksin
pozitif C_m0 verdiği varsayımı iki bağımsız kaynakta doğrulanmadı" olarak
yazılacak — bu bizim aleyhimize bir kalem, ve yazılması gerekiyor.

---

## 🔑 NACA TR-796 / ACR L4H19 (1944) — okuduğumuz en verimli tek kaynak (12.09.2026)

Önce bir tespit: `kaynakca/`'daki **iki dosya aynı rapordur.**
`NACA-ACR-L4H19_1944_tailless-tip-fins.pdf` savaş zamanı ön baskısı (Ekim 1944),
`NACA-TR-796_...pdf` yayımlanmış hâli. Aynı metin, aynı şekiller. Atıf
**TR-796'ya** yapılacak; ACR'ın OCR'ı kötü, alıntılar TR-796'dan alındı.

Bu rapor, açık kalemlerimizden **üçünü** kapatıyor ve **iki yenisini** açıyor.

### 1. S3 KAPANDI — toe açısının işareti en-boy oranına bağlı, ve bizimki TOE-OUT

Aradığımız tam bu cümleydi:

> *"If directional stability is to be obtained with tip fins of **low aspect
> ratio (less than about 2)**, the tip fin must be set with some initial
> **toe-in** because of the large induced drag associated with lifting surfaces
> of low aspect ratio... If, on the other hand, directional stability is to be
> obtained with tip fins of **moderate or high aspect ratio**, the tip fins must
> be set with some initial **toe-out.** With toed-out tip fins, the stabilizing
> moments are generated by the **outwardly directed lift**."*

Bizim uç çerçevelerimiz AR ≈ 20–28. Tereddütsüz "high aspect ratio" tarafı →
**toe-out.** TM-78767'den gelen büyüklük (~1,5°) duruyordu, işaret açıktı;
işaret artık da kapalı. **S3'ün birinci yarısı bitti.**

### 2. Ama aynı paragraf S3'ün ikinci yarısını KÖTÜ cevaplıyor

Perdövites arıza kipini de aynı yerde veriyor, ve bizim tarafımız kötü olan
taraf:

| kurulum | perdövitese giren fin | doğan moment |
|---|---|---|
| **toe-out** (bizimki) | **arka** fin | **büyük DESTABİLİZE edici** (artan direnç) |
| toe-in | ön fin | büyük STABİLİZE edici |

> *"When an airplane with toed-out tip fins is yawed to an angle sufficient to
> stall the rear tip fin, a **large destabilizing moment** is generated by the
> increased drag of the rear tip fin."*

Yani AR'ımızın dayattığı kurulum, **yan kayma büyüdüğünde kendi kendini
bozan** kurulumdur. Küçük β'da doğru çalışır, büyük β'da yön kararlılığı
işaret değiştirebilir. Bu bir **arıza kipi** ve §8'e yazılmalı: yan kayma
zarfının üst sınırı, arka uç finin perdövites açısıyla belirleniyor — ve o
sınırı biz hesaplamadık.

⚠️ Rapor bir üçüncü yol da veriyor: **profil-direnç finleri** (NACA 4306 tipi
kesit), sıfır taşımada toe-in'e kurulur, yan kaymada öndeki finin α'sı
negatifleşip ayrılmayla büyük profil direnci üretir. Langley serbest-uçuş
tünelinde denenen **en etkili** tip bu olmuş; sıralama: *profil-direnç >
endüklenen-direnç > taşıma* finleri. Taşıma finleri en zayıf, çünkü moment
kolları kısa (ok açısıyla belirlenen boyuna mesafe). **Bu bizim §4'teki
"sapma kolu = yarı açıklık" iddiasını doğruluyor** — o kol direnç
mekanizmasının kolu, ve rapor da *"the moment arm associated with the drag of
the tip fin is so large (one-half the span)"* diyor. Aynı sayı, 1944'ten.

### 3. ÖLÇÜT GELDİ — C_n_β için seçtiğimiz sayılar kendi uydurduğumuzdu, artık değil

> *"The directional stability... should be as great as required on conventional
> airplanes... The value of the directional-stability parameter C_n_β,
> recommended for conventional airplanes, is usually **greater than 0.001 per
> degree.** As evidenced from figure 14, however, models have been flown in the
> Langley free-flight tunnel with a value of C_n_β of only **one-third** this
> amount although the best flying qualities of these models were obtained with
> values of C_n_β in excess of 0.001."*

0,001/derece = **0,0573 /rad.** Serbest-uçuş tabanı = **0,0191 /rad.**

`sapma.py`'de kullandığımız 0,03 ve 0,05 /rad **bizim seçtiğimiz** sayılardı ve
ikisi de yerleşik ölçütün **altında.** Hedefler artık etiketleriyle birlikte
modülde; fairing veteri de ölçüt için yeniden hesaplandı. Ve rapor kuyruksuz
uçakların bu gereksinimden muaf olmadığını **açıkça** söylüyor — kaçış yok.

Yeniden hesabın sonucu (çerçeve boyu 2 × 0,71 m, iki çerçeve, a_f = 4,0):

| C_n_β (/rad) | gereken fairing veteri | nereden |
|---:|---:|---|
| 0,0191 | 13 mm | L4H19: serbest-uçuş tünelinde uçurulan en düşük |
| 0,0300 | 21 mm | bu çalışmanın seçtiği alt değer |
| 0,0500 | 34 mm | bu çalışmanın seçtiği üst değer |
| **0,0573** | **39 mm** | **L4H19: geleneksel uçaklar için ÖNERİLEN** |

**Ve bu iyi haber.** 20 mm kalınlıkta bir fairing'in veteri zaten tipik olarak
50–70 mm olur — yani yerleşik ölçüt, yapısal olarak nasılsa gerekecek bir
kaportanın **altında** kalıyor, %28–78 pay bırakarak. Yön kararlılığı bu
konfigürasyonda *ek bir yüzey* istemiyor; var olan çerçeveyi kaportalamak
yetiyor. Makaledeki "gereksinim" dili doğru kalıyor, ama gereksinimin
karşılanabilirliği artık ölçütlü.

⚠️ Payı fazla saymayalım: aşağıdaki 8. madde (gövdenin destabilize edici
katkısı) modelde yok, ve o pay bu payı yer.

### 4. Düşük C_n_r savunulabilir, ama YALNIZ C_n_β yeterliyse

Bizde C_n_r = −0,0023, çok küçük. Rapor bunun kuyruksuzda kaçınılmaz olduğunu
söylüyor ve şartlı bir teminat veriyor: küçük C_n_r *"will not be excessively
detrimental to the flying qualities **provided the directional stability of the
airplane is adequate**."* Yani iki açık kalemimiz bağımsız değil; C_n_r'ın
affedilmesi C_n_β'nın ölçütü tutturmasına bağlı. Ve uyarı ekliyor: yanal
salınımların sönümü **yüksek hızda kritik**, çünkü hem C_n_r hem yalpa-sapma
kuplajı düşük α'da azalıyor. **Bizim kritik durumumuz seyir.**

### 5. 🔴 YENİ AÇIK KALEM — şeridin ÖLÜ BANDI, ve ölçülmüş eşiği

> *"Unpublished tests of rearwardly located spoilers on two different models
> confirm the fact that **spoiler projections of less than 0.01c produce
> negligible changes in lift.**"*

Kullanıcının düzeltmesinden sonra şerit **sürekli değişken**; o hâlde bu eşik
kumanda kursunun altından bir **ölü bant** kesiyor. Ve şerit konik olduğu için
eşik her istasyonda aynı kumanda kesrinde aşılmıyor: dışta yükseklik büyük,
veter küçük — **dış uç önce çalışıyor.** `yatis.py`'ye `esik_istasyonu()` ve
`esik_kolu()` eklendi, gerçek planform veteriyle:

| kumanda kesri f | eşik istasyonu | etkin % | kol (m) | M/M_tam | doğrusal olsa |
|---:|---:|---:|---:|---:|---:|
| 0,050 | yok | 0 | — | **0,000** | 0,050 |
| 0,075 | 1,144 | 2,0 | 1,154 | 0,003 | 0,075 |
| 0,100 | 0,945 | 19,0 | 1,057 | 0,041 | 0,100 |
| 0,150 | 0,668 | 42,8 | 0,930 | 0,113 | 0,150 |
| 0,200 | 0,481 | 58,8 | 0,850 | 0,177 | 0,200 |
| 0,250 | 0,344 | 70,5 | 0,796 | 0,237 | 0,250 |
| 0,300 | 0,239 | 79,5 | 0,757 | 0,293 | 0,300 |
| 0,400 | 0,090 | 92,2 | 0,707 | 0,399 | 0,400 |
| 0,500 | 0,000 | 100,0 | 0,679 | 0,500 | 0,500 |

**Ve sonuç beklediğimden iyi çıktı.** Eşiği aşan kısım şeridin **en uzun kollu**
kısmı olduğu için, kaybedilen alanın büyük bölümü büyüyen kolla geri geliyor:
kol f = 0,5'te 0,679 m iken f = 0,1'de **1,057 m.** Bunun sayısal karşılığı:

- kursun **%25'inin üstünde** tepki doğrusaldan **%5 içinde** — kontrol
  tasarımı için pratikte doğrusal,
- **%15'in altında** momentin dörtte birinden fazlası kayıp,
- **%7'nin altında şerit hiçbir şey yapmıyor.**

Yani sürekli kumanda **sıfırdan başlamıyor**, ama bozukluk kursun dibine
hapsolmuş durumda. Küçük yatış düzeltmeleri için ölü bant gerçek; büyük
komutlar için önemsiz. Bu, kullanıcının "çıkma miktarı esnek" tasarımına karşı
bir itiraz **değil** — o tasarımın sayısallaştırılmış sınırı.

### 6. 🔴 İKİNCİ YENİ KALEM — tek yönlü çıkıntı ve yunuslama momenti

> *"If only **upgoing** spoiler projections are used, the pitching moments
> developed are **prohibitive.** A spoiler arrangement employing **equal up and
> down projections** would improve this condition."*

Bizim şeridimiz tek yönlü (yalnız alt yüzeyden çıkıyor). §4.4'te hesapladığımız
yunuslama kuplajı ΔC_m 0,005–0,032 idi ve "rahat değil" demiştik. **1944 aynı
şeyi seksen yıl önce, daha sert dille söylemiş.** Bu bağımsız bir doğrulama, ve
bir de çözüm öneriyor: iki yönlü (yukarı+aşağı eşit) çıkıntı. Bizim
konfigürasyonda alt yüzeyden aşağı, üst yüzeyden yukarı çıkabilen bir şerit
mümkün mü — bu **tasarım sorusu kullanıcıya sorulacak.**

### 7. Bir de PRECEDENT — otomatik kararlılık, 1944'te önerilmiş

> *"a tailless airplane of very low directional stability with fixed controls
> could be flown satisfactorily if an automatic pilot were geared to the
> directional control... Reference 1 includes the suggestion that the
> directional control could be linked with the aileron control in order to
> minimize the effects of adverse aileron yaw."*

Bizim yaklaşımımız tam bu: düşük doğal C_n_β + otomatik denetim, ve yatış
komutu ile sapma komutunun birlikte tahsisi (§4'teki ters sapma kuplajı için
zaten gerekiyordu). 1944'te "uçuş denemesi yok" notuyla önerilmiş; bugün
rutin. **Bu, konumlandırma riskimiz (S6) için savunma malzemesidir:** kontrol
yüzeyi yokluğunu otomatik denetimle kapatmak, alanın kendi literatüründe
kuyruksuz uçak için doğmuş bir fikirdir, bizim icadımız değil.

### 8. Ve bir UYARI — gövdenin destabilize edici etkisi modelimizde YOK

> *"The destabilizing effect of the fuselage and nacelle of tailless airplanes
> is usually **at least as great as** the stabilizing effects contributed by the
> wing alone."*

VLM planformdan C_n_β = 0 veriyor. Ama VLM'in **hacmi yok**: merkez gövdemiz
(BWB'nin kalın orta kesiti) yanal kuvvet üretir ve bu kuvvet CG'nin
önündedir → **destabilize edicidir.** Yani gerçek başlangıç noktası sıfır
değil, **sıfırın altı.** Fairing'in kapatması gereken açık, hesapladığımızdan
büyük. Bu bir sayı değil, bir **işaret** bulgusu — ama işaret aleyhimize ve
§8'e yazılmalı.

---

## 🔑 Şugar Gabor & Botez — S1 KAPATILABİLİR, ve alet zaten elimizde (12.09.2026)

⚠️ Önce bir özeleştiri: bu dosyayı `Gallay-Laurendeau_...` diye adlandırmışım.
**Yanlış.** İçeriği açıp bakınca yazarlar Oliviu Şugar Gabor, Andreea
Koreanschi, Ruxandra Mihaela Botez (ÉTS Montréal); Laurendeau yalnızca
kaynakçada ve teşekkürde geçiyor. Dosya
`SugarGabor-Botez_nonlinear-VLM-viscous-strip-coupling.pdf` olarak
yeniden adlandırıldı. Kaynakları "içerik doğrulayarak" adlandırdığımı
söylemiştim; bu dosyada yapmamışım.

### Yöntem tam olarak S1'in istediği şey

Doğrusal-olmayan VLM: kanadın açıklık istasyonlarında **iki boyutlu ağdalı**
çözüm (şerit kuramı) yapılıyor, çıkan şerit kuvvetleri kamber yüzeyine dağılmış
girdap halkalarının üç boyutlu kuvvetleriyle **eşleniyor.** Toplam direnç:

> C_D = C_Di + (1/S)·∫ c_d(y)·c(y) dy

Doğrulama: dC_L/dα'da **%0,51**, dC_m/dα'da **%0,32** hata. Maliyet: eşdeğer
CFD çözüm süresinin **~%1'i.**

### Bunun bizim için anlamı: S1'i BAŞKASINA SORMAMIZA GEREK YOK

S1'in kalan hâli şuydu: *"burulmuş kanadın ağdalı (Oswald) açıklık verimi
nedir?"* Bu yöntem tam onu veriyor. Ve **bileşenlerinin hepsi zaten
kodumuzda:**

| gereken | bizde ne var |
|---|---|
| burulmuş kanadın açıklık yükü | `vlm.py` / `kararlilik.py:denge_burulmasi()` |
| şerit başına 2-B ağdalı çözüm | `cd0.py` NeuralFoil'i (XFOIL üzerine eğitilmiş) **şerit şerit** çağırıyor |
| eksik olan tek şey | `cd0.py` kesit direncini **sıfır kaldırmada** okuyor; burulmuş kanadın **yerel C_l'inde** okumuyor |

Yani eksik olan bir araç değil, bir **çağrı noktası**: her şeridin VLM'den
gelen yerel C_l'ini NeuralFoil'e verip c_d'yi orada okumak, sonra burulmalı ve
burulmasız hâlleri karşılaştırmak. Bu yapıldığında S1 bir kaynak sorusu olmaktan
çıkıp **hesaplanmış bir sonuç** olur ve §6'daki "inviscid→Oswald oranı
varsayılmıştır" açığı kapanır.

**Kaynaklar bitince karar verilecek işler listesinin başına bu yazıldı.**
(Bugün yapmıyorum; kullanıcının talimatı önce kaynakları bitirmek.)

### Bir de yöntem notu — konvansiyon denetimimizi doğruluyor

Aynı makale, doğrulama bölümünde şunu açıkça yazıyor:

> *"the lift and pitching moment coefficients are calculated using the
> **average geometrical chord** (instead mean aerodynamic chord that is often
> used), and the pitching moment coefficient is calculated about the **root
> chord leading edge point**."*

Bu, bu çalışmada benim yaptığım referans-veter hatasının ta kendisidir: kararlılık
payı MAC'te, denge gereksinimi S/b'de idi. Ciddi bir yayın, hangi veteri ve
hangi momenti aldığını **tek cümlede** ilan etme gereği duyuyor. Bu,
`kararlilik.py:konvansiyon_denetimi()`'nin varlık sebebini dışarıdan
doğruluyor — §6'nın metodoloji kısmına bir cümlelik dayanak.

### Tasarım sonucu — endüklenen/profil takası standart

Yeniden tasarladıkları kanatta endüklenen direnç ortalama **%20** düşerken
profil direnci **%6'ya kadar** artıyor; net toplam direnç **%10** düşüyor. Bizim
burulma takasımız (e 0,993 → 0,865, yani endüklenen direnç artıyor, karşılığında
denge geliyor) aynı türden bir alışveriş; literatürde bu takasın iki yönlü
işlediği yerleşik.

---

## Gurney literatürü ikinci tur — biri lehimize, biri Yang'la ÇELİŞİYOR (12.09.2026)

### NASA TM-4071 (Neuhart & Pendergraft 1988) — mekanizma Reynolds'a karşı sağlam

Langley 16×24 inç **su tüneli**, akış görselleştirme, **Re = 8.588.** Yani
rüzgâr tüneli çalışmalarının **dört mertebe altında.** Buna rağmen:

> *"the effect of the Gurney flaps was in **qualitative agreement** with the
> investigations [at Re ~10⁶]... the general effects of the trailing-edge
> devices on the flow are the same, since an **effective increase in camber
> provides an inviscid effect to the first order**."*

**Bu bizim için önemli, çünkü asılı durumda şeridin Reynolds'u düşük.** Cihazın
çalışma mekanizması (etkin kamber artışı) birinci mertebede iskoz değil; bu
yüzden Reynolds dört mertebe düştüğünde bile *yön* korunuyor. §4.4'ün "sıfır
hızda bile çalışır" iddiası için bu, elimizdeki **en doğrudan** dayanak. Ama
görselleştirme çalışması: yön veriyor, **büyüklük vermiyor.**

İkinci bulgu bizim aleyhimize ve ölçülmüş: Roesch & Vuillet'nin Re = 0,75×10⁶
ölçümünde **0,0125c** şerit direnci temiz kanada göre **değiştirmiyor**, ama
**0,05c** şerit C_Lmax'ı artırırken *"a significant drag increase"* getiriyor;
Liebeck de 0,0125c üstünün direnç cezası göstereceğini söylüyor. **Bizim
şeridimiz h/c 0,021–0,137**, yani dış uçta ölçülmüş ceza bandının on katı
derinliğinde. §4.4'ün 16,7 N konuşlu direnci bir kestirimdi; artık yönü
ölçümle destekli.

Üçüncü bulgu: Gurney'in üst yüzey ayrılmasına faydası **α < 3,5°** ile sınırlı
bulunmuş, ve en büyük fayda en büyük şeritlerde. Geçiş koridorumuz bunun çok
üstünde açılardan geçiyor.

### Liu, Li & Sun 2025 (*Fluids*) — Yang'ın tersini söylüyor, ve bunu yazmak zorundayız

DDES, NACA0021, **α = 20° (derin perdövites)**, Re = 2,7×10⁵, Ma = 0,1,
Gurney yüksekliği **%2 veter** (bizim kök istasyonumuz %2,1 — neredeyse aynı).

| | EXP | CFD sade | CFD Gurney | değişim |
|---|---:|---:|---:|---:|
| C_l | 0,443 | 0,332 | 0,643 | **+%93,7** |
| C_d | 0,285 | 0,252 | 0,253 | **+%0,4** |
| L/D | 1,557 | 1,317 | 2,542 | +%93,0 |

Yani **derin perdövitesde taşımayı neredeyse ikiye katlıyor, direnci hiç
artırmadan.**

**Bu, Yang 2020'nin ölçtüğü *"became less effective after stall angle"* ile
ters yöne bakıyor.** Ve ben §4.4 ile §8'e Yang'a dayanarak "türbülans ve
perdövites sonrası bozulma, asılı durumdaki yatış otoritesine ana risk"
yazmıştım. **O cümleyi tek taraflı bırakmak artık dürüst olmaz.**

⚠️ Ama çelişkiyi de olduğundan büyük göstermeyelim, ve iki kaynağı eşit
ağırlıkta saymayalım:

| | Yang 2020 | Liu 2025 |
|---|---|---|
| yöntem | **rüzgâr tüneli ölçümü** | DDES (benzetim) |
| ölçülen | L/D iyileşmesinin türbülansla ve α ile azalması | tek bir α'da C_l artışı |
| serbest akış türbülansı | %0,2 / %10,5 / **%19** | temiz |
| taban doğruluğu | ölçüm | **sade kanat C_l'i deneyin %25 altında** (0,332 vs 0,443) |

Liu'nun Gurney farkı, deneyden dörtte bir sapan bir taban üzerinde
hesaplanmış. Ve iki çalışma **aynı şeyi ölçmüyor**: Yang'ınki türbülans
ekseni, Liu'nunki α ekseni. Doğru okuma şu: **perdövites sonrası etkinlik
tartışmalı; türbülans duyarlılığı ise yalnız Yang'da ölçülmüş ve
çürütülmemiş.**

§4.4 ve §8 buna göre düzeltilecek: risk duruyor, ama "oybirliği" değil.

---

## 🔴 Panagiotou 2021 (quasi-3D BWB) — yöntemimize en sert itiraz, ve beklenmedik bir savunma (12.09.2026)

*Aerospace* 8(13). Taktik bir BWB İHA prototipi üzerinde üç yöntem
karşılaştırılıyor: CFD (RANS, Spalart–Allmaras, y⁺<5), XFLR5 3-B (VLM), ve
kendi önerdikleri quasi-3-B yöntem. Re = 2.932.000, MAC bazlı.

### 1. 🔴 VLM, BWB'de taşımayı %30–38 EKSİK veriyor

| α | CFD | XFLR5 3-B (VLM) | quasi-3-B | VLM sapması | quasi-3-B sapması |
|---:|---:|---:|---:|---:|---:|
| −4 | −0,2669 | −0,1659 | −0,2392 | **%37,8** | %10,4 |
| 0 | 0,1476 | 0,0920 | 0,1483 | **%37,7** | %0,5 |
| 4 | 0,5647 | 0,3489 | 0,5462 | **%38,2** | %3,3 |
| 8 | 0,9583 | 0,6022 | 0,9376 | **%37,2** | %2,2 |
| 12 | 1,2259 | 0,8497 | 1,2425 | **%30,7** | %1,4 |

Ve trim bölümünde VLM'i **tamamen dışarıda bırakıyorlar:**

> *"Due to the **large deviation** between the XFLR and CFD results for the
> clean configuration, the former method is **not included** at the present
> section."*

**Bu bizim dört sonucumuzun altını oyuyor:** açıklık verimi, tarafsız nokta,
denge burulması, yatış sönümlemesi — hepsi VLM'den.

### Ama panik etmeden bakınca — sapma bir ÖLÇEK, bir şekil hatası değil

Sapma α boyunca neredeyse sabit: %37,8 / %37,7 / %38,2 / %37,2 / %30,7. Yani
eğri **çarpımsal bir katsayıyla** (≈0,62–0,68) küçülmüş, biçim değiştirmemiş.
Bunun önemi şu: §6'nın VLM savunması zaten *"buradan alınan her büyüklük
dolaşım veya aerodinamik merkez türündendir"* diyor — ve

- x_np = −(dC_m/dC_L)·c + x_ref bir **orandır**; pay ve payda aynı katsayıyla
  ölçeklenirse **değişmez**;
- burulma etkinliği (derece başına C_m) aynı katsayıyla **eksik** çıkar, yani
  gerçekte gereken burulma hesapladığımızdan **AZ** olur → lehimize.

⚠️ **Ama bu çıkarımın kilit varsayımı denetlenemiyor:** C_m'in de C_L ile aynı
katsayıyla ölçeklendiğini bilmemiz gerekiyor. Makalenin Tablo 4'ü tam olarak
bu karşılaştırma — ve tabloda sayılar yerine **"Data restrictions apply"**
yazıyor. Yani kontrol edilebilecek tek yerde veri kapalı.

⚠️ İkinci uyarı, kendi lehimize olmayan tarafta: %38'lik bir açık, kalınlık
etkisinden beklenenden **büyük.** Onların XFLR5 kurulumunun gövdeyi hiç
modellemediğinden şüpheleniyorum (makale söylemiyor). Bizim planformumuzda
merkez kesit **kanadın parçası** olarak modelde var — sıfır kalınlıkta bir
kamber yüzeyi olarak. Yani bizim açığımız onlarınkinden küçük olmalı, ama
sıfır değil: VLM'in hacmi yok, BWB'nin gövdesi hacimle taşıyor.

**Sonuç: §6'ya yazılacak bir maruziyet.** "VLM'den yalnız oran ve şekil
alıyoruz" savunması ayakta, ama artık *sınanmış* bir sayıya karşı ayakta
duruyor ve o sayı büyük. Ve bu, S1 için önerdiğim iç hesabın (yerel C_l'de
NeuralFoil) gerekçesini güçlendiriyor.

### 2. ✅ Ve beklenmedik bir savunma — burulma ÜÇÜNCÜ bir iş yapıyor

Aynı makale, α ≥ 8°'de kendi yönteminin de C_m'i kaçırdığını söylüyor ve
sebebini veriyor:

> *"likely linked to leading-edge separation over the main body... **The main
> wing stalls before the main body, causing the BWB to pitch-up.**"*

Bu, §7.4'teki NASA pitch-up uyarısından **farklı bir mekanizma.** NASA'nınki
düşük en-boy oranı + hücum kenarı girdap patlaması; biz ondan "AR 6,03, o
sınıfta değiliz" diye korunuyorduk. **Panagiotou'nun mekanizması en-boy
oranına bakmıyor** — planformun hangi parçasının önce perdövitese girdiğine
bakıyor. Yani o savunmamız bu mekanizmaya karşı işlemiyor.

**Ama burulma işliyor.** Ok açılı bir kanatta washout kökü önce perdövitese
sokar; BWB'de **kök = gövdedir.** Yani −9° washout, gövdeyi kanattan önce
perdövitese sokarak Panagiotou'nun pitch-up sırasını **tersine çeviriyor.**

Böylece washout'un gerekçesi üçe çıktı:
1. denge (C_m0 açığını kapatıyor) — §7.6,
2. ok açılı kanatta uç perdövitesini geciktirmek — §7.4,
3. **BWB pitch-break'in perdövites sırasını tersine çevirmek** — yeni.

%4,3'lük cezanın karşılığı gittikçe artıyor. Bu, defterin **beşinci kalemini**
haklı çıkarmaz ama bağlamını değiştirir: o ceza tek bir iş için ödenmiyor.

---

## ⚠️ Lampropoulos 2025 (BWB düşük-Mach) — §7'deki bir cümlem fazla güçlü (12.09.2026)

*Fluids* 10(54). BWB İHA, Mach ~0,1, XFLR5 panel yöntemi + OpenFOAM
(Spalart–Allmaras, y⁺<10, ~10 milyon hücre), CMA-ES ile trim optimizasyonu.

### Ne yapmışlar

Tasarım değişkenleri: kök kesit insidansı (0–4°), seyir α (0–4°), **doğrusal
burulma (2–5°)**, ve beş kanat kesidinin her biri için **refleks seviyesi
(1–5)** — refleks, standart NACA2412'nin kamber çizgisinin arka kısmını yukarı
doğru bükerek, kalınlık dağılımı korunarak üretiliyor.

Sonuç: α = 1,2°, insidans = 1,52°, **toplam burulma = 2,44°.**

### Bu, §7'deki şu cümleyi zorluyor

> *"**Reflex does not trim this aircraft, and no plausible amount of it
> would.**"*

Bu cümleyi NACA TR-460'ın ölçtüğü 2R212 değerine (+0,004) dayanarak yazmıştım
ve **ölçüm için doğru.** Ama *"hiçbir makul miktarı"* ifadesi, refleksi bir
tasarım değişkeni olarak parametreleyen ve onunla trim kapatan yayımlanmış bir
optimizasyon karşısında ayakta duramaz. Doğru ifade şu olmalı: **elimizdeki
tek ölçümün büyüklüğündeki refleks bu uçağı dengelemez.** Daha güçlü bir
refleksin ne verdiği, S4'ün ta kendisidir — ve bu kaynak S4'ü *çözmüyor*,
**önemini artırıyor**, çünkü 2,44°'lik bir burulmayla kapanan bir trim, o
kesitlerin 0,004'ten hayli fazlasını verdiğini ima ediyor.

⚠️ Karşılaştırmayı da dürüst kuralım, bizim aleyhimize okunmasın diye: onların
kapattığı denge **bizimkinden hafif bir gereksinim.** Statik payları
**%8,1 MAC**, bizimki **%12,5 MAC**; daha küçük pay, daha az trim momenti
demektir.

### Ve buradan iki sayı LEHİMİZE çıkıyor

**1. Statik pay ölçütü.** Makale kendi payını şöyle değerlendiriyor:

> *"The non-dimensional static margin with respect to mean aerodynamic chord
> is **0.081.** This value is **marginally outside the typical range** for
> static longitudinal stability that... lies **between 0.1 and 0.3**."*
> Ve C_m_α = −0,086, *"when a typical range is considered to be between −0.3
> and −1.5"*.

Bizim **%12,5**'imiz bu aralığın **içinde**, onlarınki **dışında** — ve makale
kendi konfigürasyonu için *"forward movement of the center of gravity or
additional reflex of the airfoils is advisable"* diyor. §7.6'daki CG penceresi
artık yayımlanmış bir ölçüte karşı konumlanabiliyor.
⚠️ C_m_α'mızı henüz bu biçimde yazmadık; yazmadan önce C_L_α ile
hesaplanmalı (pay × C_L_α). Not edildi.

**2. BWB pitch-up'ın kaçınılmaz olmadığı — ölçülmüş bir karşı örnek.**

> *"it remains longitudinally statically stable, even at high α values,
> **without the pitch-up tendency which is typical of BWB designs with
> back-swept wings**"*, perdövites açısı 20°'nin üstünde.

Yani (a) pitch-up eğilimi ok kanatlı BWB'ler için *tipik* — Panagiotou ve
NASA'dan sonra **üçüncü** bağımsız kaynak; ve (b) refleks + burulma ile
**giderilebiliyor.** Bu, bir gün önce §7'ye yazdığım "burulma perdövites
sırasını tersine çeviriyor" savını dışarıdan destekliyor.

---

## Son üç kaynak — biri ağır, ikisi bağlam (12.09.2026)

### Wang & Zhou 2022 — 🔑 en büyük açık kalemimizin konumunu değiştiriyor

Küçük BWB İHA, dağıtık elektrikli itki, RANS + **rüzgâr tüneli** (1:1,8 ölçek,
paslanmaz çelik model, 68 m/s, Re = 2,0×10⁶).

| α aralığı | CFD ile ölçüm |
|---|---|
| −6° … 10° | *"both the aerodynamic force values and the variation trends are in **quite good agreement**"* |
| 10° … 26° | *"show **remarkable differences** between the numerical and experimental results"* |

Maks L/D = 22,31 (α = 4°), ve **"soft-stall performance"** gözlenmiş.

**Bunun bizim için değeri şu.** §8'in 3. maddesi — geçişin yunuslama momenti —
şimdiye kadar *"biz hesaplamadık"* diye duruyordu. Artık şöyle durabilir:
**o hesabı bu konfigürasyon sınıfında kimse güvenilir yapamıyor.** Üç farklı
sadakat düzeyi aynı yerde tökezliyor:

| yöntem | nerede bırakıyor | kaynak |
|---|---|---|
| VLM | α > 8° | Panagiotou 2021 |
| quasi-3-B | α > 8° | Panagiotou 2021 |
| **RANS** | **α > 10°, ve ölçüme karşı** | **Wang & Zhou 2022** |

Ve bizim geçiş açılarımız (17,5°–21,6° geometrik) bu bandın **içinde.** Yani
kalem hesaba değil **ölçüme** ait; §7'ye ve §8'e böyle yazıldı. Bu, hakem
karşısında çok daha savunulabilir bir konum.

⚠️ Dosya adı hatası: bunu `Zhang-2022_...` diye adlandırmışım; yazarlar Kelei
Wang ve Zhou Zhou. Yeniden adlandırıldı. **Bu, bugün yakaladığım ikinci
adlandırma hatası** (öteki Şugar Gabor). Kaynakları içerik doğrulayarak
adlandırdığımı söylemiştim; iki dosyada yapmamışım, ve ikisini de kendi
okumam ortaya çıkardı.

### Saeed 2009 (Cambridge, lamineer uçan kanat) — yalnız bir ölçek bağlamı

80 m açıklık, 69 ton, M 0,58, 10.900 m. Bizim sınıfımızdan tamamen uzak. Tek
aktarılabilir nokta: kesit **kalınlık oranını %28** seçiyorlar ve C_D0'ın t/c
ile büyümesinin *"weak"* olduğunu gösteriyorlar. Bizim %25 kalınlıkta merkez
gövdemiz bu konfigürasyon sınıfı için **aykırı değil**, olağan. Ama Mach ve
Reynolds rejimleri bambaşka; makaleye **sayı olarak girmiyor**, yalnızca
"25% kalınlık bu sınıf için normal" savı gerekirse dayanak.

### Notre Dame / Valkyrie (1991) — sonucumuzu doğruluyor ama ATIF YAPMAYACAĞIZ

NASA/USRA öğrenci tasarım önerisi (Boeing sponsorlu). Uçan kanat, ve tam
bizim kesidimizi kullanıyor: **NACA 2R212.**

> *"A **2° reflex** in the trailing edge of this airfoil provides a zero moment
> coefficient about the aerodynamic center... allows the Valkyrie to trim
> during cruise at an angle of attack of 8° with a corresponding **elevator
> deflection of −8°.** Although reflexing the trailing flap to trim does
> increase the drag generated by the wing by **raising the C_D0 to 0.0314**."*

Yani: 2R212 **tek başına dengelemiyor.** Üstüne 2° hücum-kenarı refleksi *ve*
−8° elevatör gerekiyor, *ve* C_D0 0,0314'e çıkıyor. Bu, §7'nin sonucunun
bağımsız bir tasarımda birebir karşılığı — ve dengelemenin direnç ödediğinin
**üçüncü** örneği (Wang & Zhou ve Lampropoulos'tan sonra).

❌ **Ama makaleye atıf yapmıyoruz.** Bu bir öğrenci tasarım önergesi — gri
literatür. Hakem haklı olarak sorar. Bulgu burada kalsın; makaledeki aynı
sonuç zaten TR-460'ın kendi ölçümüne dayanıyor ve ona ihtiyacı yok.

---

# YZ TURU 13 — gelen kaynaklar (12.09.2026)

Kullanıcı YZ1/YZ3/YZ5/YZ6'nın verdiği bağlantılardan indirdiklerini depoya
koydu: 19 dosya. Hepsini **açtım**, künyelerini doğruladım, üçü mükerrer
çıktı, biri de iddia edilen kaynak değildi.

| dosya | iddia | gerçek |
|---|---|---|
| `19930091108` | TR-460 | ✅ TR-460 — **elimizde zaten var**, silindi |
| `19930091873` | "spoiler ölü bant PDF'i" | ✅ TR-796 — **elimizde zaten var**, silindi |
| `fluids-10-03-00054` | Lampropoulos | ✅ doğru — **elimizde zaten var**, silindi |
| `19930082661` | "NACA TN 1862, Polhamus, süpürme" | ❌ **Doris Cohen, düz ok kanatların SÜPERSONİK taşıması + errata.** İlgisiz. Adı `YANLIS-KAYNAK_...` yapıldı, kayıt kalsın diye duruyor |
| `tstastny_phd_thesis` | "Olsson master tezi" | ❌ Stastny'nin doktora tezi, konusu *sabit kanat düşük irtifa kontrolü*. (YZ1 bunu kendisi de söylemişti.) |
| `Lv_9319` | "Shkarayev'in yakın metni" | kısmen: Lv ve diğ. 2013, *adaptive proprotors*. Ortak yazar yalnız Moschetta |
| `no.ntnu_...` | "tailsitter sys-ID" | ⚠️ FoxTech **Babyshark** — kuyruk-oturur değil, quadplane |

Geri kalan 12'si gerçekten işe yarar ve ikisi bizi **ciddi biçimde
değiştiriyor.**

## 🔴 S4 KAPANDI — ve bizim aleyhimize kapandı

Geçen tur Lampropoulos'a bakıp §7'deki *"no plausible amount of reflex
would trim this aircraft"* cümlesini yumuşatmış, yerine **"2,44°'lik bir
burulma, kesitlerin 0,004'ten hayli fazla verdiğini ima ediyor"** diye bir
cümle koymuştum. **O cümle bir çıkarımdı, okuma değildi — ve yanlıştı.**
İki yeni NACA kaynağı, momenti gerçekten ölçen tünelde, tam tersini
gösteriyor.

### NACA TN-388 (Defoe) — üç refleks kesit, VDT, Re ≈ 3,1×10⁶

Üç yaygın kesidin (Navy 60, Boeing 106, Gött. 398) arka kamber çizgisi %30
veterden itibaren değiştirilmiş; yeni çizgi **ince kanat kuramına göre
çeyrek veterde SIFIR moment** verecek şekilde seçilmiş. Ölçüm:

> *"The pitching moment coefficients for the reflexed airfoil are
> **practically zero**..."*

| kesit | C_m (C_L = 0) |
|---|---:|
| Gött. 398 / B106 / N60 (normal) | −0,082 / −0,052 / −0,080 |
| **Gött. 398R / B106R / N60R (refleks)** | **−0,007 / −0,001 / ≈−0,001** |
| NACA M6 | −0,001 |

Ve iki maliyet, ölçülmüş: C_Lmax **%12 düşük**; eşit C_L'de profil direnci
refleksli kesitte **daha yüksek** (yalnız küçük C_L'de değil).

### NACA 4400R serisi (Wartime Report) — tasarım hedefi ZATEN NEGATİF

Orta kamber çizgisi, ince kanat kuramından **C_m = −0,03** verecek şekilde
türetilmiş. Ve rapor: *"the design pitching-moment coefficient **was
realized**."* Tablo I, ölçülmüş:

| kesit | c_m,c/4 |
|---|---:|
| 4409R | −0,025 |
| 4412R | −0,030 |
| 4415R | −0,031 |
| 4418R | −0,030 |

C_Lmax cezası burada da ölçülmüş: **%10**.

### Toplam tablo — dokuz ölçülmüş kesit, bir tanesi pozitif

| kesit | C_m,c/4 | kaynak |
|---|---:|---|
| **NACA 2R212** | **+0,004** | TR-460 |
| B106R | −0,001 | TN-388 |
| N60R | ≈−0,001 | TN-388 |
| NACA M6 | −0,001 | TN-388 |
| Gött. 398R | −0,007 | TN-388 |
| 4409R | −0,025 | 4400R WR |
| 4412R / 4415R / 4418R | −0,030 / −0,031 / −0,030 | 4400R WR |

**Refleks, yapılıp ölçüldüğü hâliyle, negatif momenti GİDERMEK için bir
araçtır — pozitif moment ÜRETMEK için değil.** Bizim ihtiyacımız +0,056.

**Ne yaptım:** §7'deki çıkarım cümlesi kaldırıldı, yerine ölçülmüş tablo
kondu. Duyarlılık tablosuna "ölçülmüş emsal" sütunu eklendi ve 0,020 ile
0,050 satırlarının karşısında **"none"** yazıyor. "0,02 veren modern bir
kesit bilen okur üçüncü satırı tasarım noktası saysın" cümlesi de kaldırıldı
— artık dokuz ölçüme karşı duruyor.

**Ve bu bizi güçlendiriyor.** Burulma artık iki seçenekten biri değil;
**ölçülmüş dayanağı olan tek seçenek.** %4,3'lük ceza kalkmıyor ama
alternatifi olmadığı gösterilmiş oluyor.

## 🔴 S5 DAHA DA KÖTÜLEŞTİ — ve bir YZ okuması yanlıştı

### Yu ve diğ. 2025 — tasarlanmış, üretilmiş, UÇURULMUŞ paket

24S NCM paket, VS-210 eVTOL'da altı kalkış–asılı–iniş çevrimi boyunca uçmuş.
Tezgâhta 0,2C–10,68C arası ölçülmüş. **Paket düzeyinde ölçülmüş özgül güç:**

- 724 W/kg sürekli (24S1P, 110 A ≈ 5C)
- 892 W/kg (24S4P uçuş sistemi, 440 A)
- 10,68C'de ≈ **1,5 kW/kg** — ve orada paket **55,1 °C**, 60 °C sınırına
  **4,9 °C** pay kalmış.

Yani "otomotiv paketi bizim ürünümüz değil" savunmamız çöktü: **bu kaynak
tam bizim ürünümüz**, ve tavanı 1,5 kW/kg.

### ⚠️ Ve YZ1'in karşı-kaynağı iddia edileni söylemiyor

YZ1, NASA NIAC 2022 raporunu *"4,6 kW/kg artık tamamen hayal değil"*
gerekçesi olarak verdi. **Raporu açtım. Tam tersini söylüyor:**

> *"The specific energy (200 Wh/kg) is consistent with existing prototype
> lithium-ion batteries. However, the specific power (4 kW/kg) is about
> **twice that of existing batteries**."*

Yani NIAC'ın 4 kW/kg'ı bir **gelecek teknoloji varsayımı**, ve rapor bunun
mevcudun iki katı olduğunu açıkça yazıyor. Bizim lehimize değil, **aleyhimize
üçüncü bağımsız ifade.** (Kullanıcının uyarısı burada birebir karşılık buldu:
kaynağı açmadan aktarsaydım makaleye yanlış bir savunma girecekti.)

### Sonuç — sayı büyüdü

| özgül güç | tampon kütlesi | bütçe |
|---|---:|---|
| 0,892 kW/kg (ölçülmüş sürekli) | 9,3 kg | kapanmaz |
| 1,5 kW/kg (ölçülmüş termal tavan) | **5,5 kg** | **kapanmaz** (pay 2,2 kg, açık 3,7 kg) |
| 4,61 kW/kg (bizim varsayım) | 1,8 kg | — |

§6'ya olduğu gibi yazıldı. **Bu artık makalenin en açık yeri** ve
"farklı ürün" savunmasıyla kapatılamaz.

## S9 KAPANMADI — YZ1'in "NACA 1034 yeterli" demesi doğru değil

YZ1, iki yönlü şerit sorusunu *"artık kapatılabilir"* saydı. Raporu açtım:
**kapatmıyor.**

TR-1034, **spoiler aileron'ların HIZ FRENİ / süzülme yolu denetimi olarak**
kullanımını ölçüyor (NACA 65-210 ve 65₂-215 kanatlar, tam açıklık yarıklı
flap, Mach 0,13–0,71). Ölçtüğü yunuslama momenti **simetrik** açılımın
(iki kanat birden) momenti. Bizim sorumuz ise **tek kanatta üst+alt**
yüzeyden eşit çıkıntı — TR-796'nın önerdiği düzen. O düzen bu raporda yok.

**S9 açık kalıyor**, ve YZ'lere tekrar sorulacak, bu kez yanlış anlaşılmayacak
biçimde.

### Ama TR-1034 başka bir şey veriyor, ve o işimize yarıyor

> *"The plug and retractable ailerons investigated, when used as speed
> brakes, had **only a small effect on the wing pitching moments.** The
> rolling effectiveness of the ailerons **will not be impaired** by such use
> and should be as good as the effectiveness when the ailerons are projected
> in normal manner from the retracted position."*

İkisi birden bizim mimarimize uyuyor:

1. Şerit **iki kanatta birden** açılırsa bir hız frenidir, ve bu sınıftan bir
   cihazın simetrik açılımı yunuslamayı **az** bozuyor. Bizim ΔC_m kaygımız
   tek taraflı açılıma aitti; simetrik kullanım o cezayı ödemiyor.
2. Ve hız freni görevi **yatış otoritesini yemiyor** — cihaz aynı anda iki işi
   yapabiliyor.

Yani şeridin üçüncü bir rolü var: **iniş/alçalma yolu denetimi.** Bu, makalenin
"aynı donanım, iki iş" savının bir örneği daha, ve şu ana kadar hiç
yazılmamıştı. §4.4'e eklenecek.

⚠️ Aktarım sınırı: onların kanadı geleneksel, yarıklı flaplı, Mach'ları bizden
yüksek, ve cihaz **üst** yüzeyden çıkıyor; bizimki alt yüzeyde 45° ok açılı
bir şerit. Yön aktarılabilir, büyüklük aktarılamaz.

---

# ✅ S1 HESAPLANDI — `aero/iskoz.py` (12.09.2026)

Yöntem: VLM panel kuvvetlerinden her açıklık şeridinin **yerel c_l**'i
çıkarılıyor; NeuralFoil o şeridin **kendi c_l'inde** çağrılıyor (α ikiye
bölerek aranıyor, doğrusal ara değer YOK — o hatayı daha önce yapmıştım);
profil direnci açıklık boyunca integre ediliyor.

**Önce denetim, sonra sonuç.** Modül dört test koşuyor ve geçmeden hiçbir
sayı vermiyor:

| test | sonuç |
|---|---|
| şerit toplamı = çözücünün C_L'i | 0,269884 = 0,269884 |
| panel kuvvet toplamı = çözücünün C_L'i | 0,269884 = 0,269884 |
| şerit genişlikleri toplamı = açıklık | 3,4528 = 3,4528 |
| hiçbir şeritte saçma c_l yok | 0,088 … 0,343 |

⚠️ Üçüncü test **ilk koşumda kaldı** (3,4577 vs 3,4528, %0,14 taşma): şerit
genişliğini komşu merkezlerden türetince en dıştaki şerit yarım genişlik
dışarı taşıyordu. Panel geometrisinden (girdap bacağı köşeleri) alınacak
şekilde düzeltildi. Küçük bir taşma ama integrali doğrudan şişirirdi.

## 🔴 VE BİR KATEGORİ HATASI — kendim yakaladım, kayda geçiyor

İlk koşumda şu oranı yazdırdım: **Oswald/inviscid = 1,0785.** Yani "iskoz
verim, inviscid verimden büyük" — fiziksel değil.

Sebep: `e = C_L²/(πAR·C_Di)` formülü **yalnızca burulmasız** kanatta geçerli,
çünkü orada C_Di ∝ C_L². Burulmuş kanatta induklenen sürükleme C_L = 0'da
sıfır değildir ve en küçük değerini sıfırdan farklı bir C_L'de alır. O formül
burulmuş kanatta C_L = 0,03'te **e = 0,024** verdi. Ve ben parabol-uydurma
e'si (poların *eğriliği*) ile nokta e'sini (oradaki *mutlak* sürükleme)
bölmüştüm — iki **farklı büyüklüğü**.

Bu, daha önce yaptığım inviscid/Oswald kategori hatasının aynı ailesinden.
Doğru tanım, makalenin e'yi kullandığı denklemle tutarlı olan **nokta**
tanımıdır:

    e(C_L) = C_L² / (π AR [ C_Di(C_L) + C_Dp(C_L) − C_Dp(0) ])

C_Dp(0) zaten C_D0'in içinde olduğu için çıkarılıyor; yoksa çift sayılır.
Modül artık bunu kullanıyor ve gerekçe kodun içinde yazılı.

## Sonuç

| | inviscid e | **Oswald e** | oran |
|---|---:|---:|---:|
| burulmasız | 0,990 | 0,931 | 0,940 |
| **trim (−9° washout)** | **0,859** | **0,817** | **0,951** |

**Makale oranı 0,85–0,90 varsayıyordu; hesaplanan 0,94–0,95.** Yani iskoz
cezası varsayılandan **küçük** — ödünç alınan kural fazla kötümsermiş.

**Ama sonuç yine de varsayımın altında**, çünkü başlangıç noktası düşük:
burulmuş kanat 0,859'dan başlıyor, çarpım **0,817**'de kalıyor. Makalenin
kullandığı 0,85'e göre **%3,9 iyimser**, seyir L/D 12,04 yerine **11,87**
(%1,4 kayıp). Daha önce §7.6'nın korktuğu %3–5 değil.

Çapraz denetim: burulmasız inviscid e = 0,990, `vlm.py`'nin 104 şeritte
belgelediği 0,9890 ile tutuyor. ✓

## Ok açısı — ve neden basit-ok kuramı buraya uygulanamaz

| konvansiyon | C_Dp |
|---|---:|
| akım yönlü (cd0.py ile aynı) | 0,01348 |
| normal kesit (basit-ok) | 0,00745 |

**İki kat fark.** Bu bir belirsizlik değil, bir **geçersizlik** işareti:
basit-ok kuramı basınç alanını ok çizgisine dik bileşenle kurar, ama
sürtünme yüzeyin üzerinden **V** ile akar, V·cosΛ ile değil. Sürtünmeyi
cos³ ile küçültmek fiziksel değil. YZ5 ve YZ1 de aynı yöne işaret etti.
Ana sonuç akım yönlü şeritle kuruldu — hem doğru olan o, hem de `cd0.py`'nin
C_D0'i öyle kuruldu, aksi halde iki sayı toplanamaz.

## İki sınır, ikisi de makalede yazılı

1. VLM kesitleri **simetrik**. Kamberli bir kesit aynı yerel c_l'i daha küçük
   α'da ve genellikle daha küçük c_d ile üretir → bu sayı bir **alt sınır**.
2. Şerit kuramı ok açısını ihmal ediyor, kök ok açımız 45°.

Polar verisi `aero/iskoz-sonuc.json`'a yazılıyor, yeniden analiz için
VLM'i tekrar koşmaya gerek yok.

---

# Tur 14 — dört bağımsız dış okuma, ve benim kendi denetimim

Dört yapay zekâya v5'in ilk sürümü verildi. Dördü de bulgu getirdi. **Hiçbiri
olduğu gibi kabul edilmedi**; her iddia dosyaya, betiğe veya elimizdeki PDF'e
karşı sınandı. Aşağısı hem düzeltilenlerin hem de **çürütülenlerin** kaydıdır,
çünkü ikincisi de bu projenin yöntemine dahil.

## En utanç verici: §5.5 yanlış tabloyu taşıyordu

Gövdedeki "üç mimarinin karşılaştırmalı boyutlandırması" tablosu, aslında
S6.1'deki **Bacchini & Cestino'nun üç *uçan* eVTOL'ü** tablosuydu — sütun
başlıkları "Tail-sitter / Lift+cruise / Tilt-rotor" olarak değiştirilmiş.
"Tail-sitter" sütunu E-Hang 184'tü. Bizim uçağımızın menzili 1 600 km; orada
42 km yazıyordu. Üstündeki cümle "üç sözleşme" vaat ediyordu, tabloda sözleşme
yoktu.

Dördün üçü bunu yakaladı. **Sebebi belliydi: v5 el ile toparlanmıştı.**
Bu yüzden `makale/uretim/mkv5.py` yazıldı — belge artık bölüm dosyalarından
her seferinde yeniden kuruluyor, kelime sayıları sayılıyor, ek dizini iki
belgede tek kaynaktan üretiliyor, atıf boşluğu/hayaleti denetleniyor.

## T/W çelişkisi — en çok şeyi değiştiren bulgu

§6.1 "thrust equals weight" diyor. FM = 0,599, tek 1,20 m disk, 490,5 N →
**10 895 W**. Yani 6.2'nin yazdığı 10,9 kW tam olarak **T/W = 1,00**'dir.

Ama S2'nin tamponlu güç tablosu aynı 10,9 kW'a "T/W 1,20" yazıyordu (bütün
sütun 1,2 kat şişkin), ve §7.4 "T/W = 1,2'de 0,2 g" diyerek makalenin manşet
sonucunu — *tırmanarak girince irtifa kaybı sıfır* — o orana dayandırıyordu.

`aero/itki.py` bunu dışarıdan bir varsayımla kapatmıyor. Uçağın elindeki tek
ek dikey itki kaynağı **uç çiftleridir**, ve dönme sırasında onlar zaten dönmeyi
üretiyor. Bang-bang profilinde üst çiftler tam itkide, alt çiftler sıfırda
(M = 2TL) — ve üst çiftler hâlâ yukarı itiyor. Çıkan takas:

| korunan yunuslama momenti | dikey katkı | T/W |
|---|---:|---:|
| %100 (23,0 N·m) | 32,4 N | **1,066** |
| %50 | 48,6 N | 1,099 |
| %0 | 64,8 N | **1,132** |

1,200 hiçbir ayarda ulaşılmıyor.

**Manşet yine de ayakta.** Geçiş benzetimi ulaşılabilir her oranda yeniden
koşturuldu: referans dönme sürelerinde (hafif 2 s, ağır 5,1 s) 5 m/s girişle
irtifa kaybı **sıfır** — T/W = 1,00'de bile. Değişen, o tırmanışı *kazanmanın*
maliyeti: 0,132 g, 3,9 s, 9,6 m — eskiden 0,2 g, 2,6 s, 6,4 m deniyordu. Ve
dinlenmeden başlayan dönüş belirgin şekilde kötüleşti (hafif 2 s'de −9,1 değil
−14,7 m). Tırmanışla giriş artık bir incelik değil, bir **gereklilik**.

Yan ürün: uç pervanelerinin ikinci bir görevi ortaya çıktı — kalkış itki payı.
Ama bu bir bağımlılık, çünkü kalkış payı ile yunuslama otoritesi **aynı dört
pervaneden** çekiliyor ve ikisi birden tam alınamıyor.

`dogrula.py` artık hem §7.4'ün gövde tablosunu ulaşılabilir T/W'de, hem de
manşetin kendisini kilitliyor (68 hücre, sıfır sapma).

## Batarya: üç ayrı istasyondan çıkarma

4,61 kW/kg şöyle bulunmuştu: (10,9 − 2,6)/1,8. Ama 10,9 **rotor milinde**,
2,6 **motor milinde**, batarya **elektrik barasında**. Zincir link link:

| istasyon | hafif tasarım, hover |
|---|---:|
| burun pervane mili | 10,90 kW |
| ÷ makine 0,92 | 11,85 kW |
| ÷ güç elektroniği 0,95 | **12,47 kW bara talebi** |
| motor 2,60 × jeneratör 0,90 | **2,34 kW bara arzı** |
| **tampon** | **10,13 kW → 5,63 kW/kg** |

Uç çiftleri de sayılırsa (kalkış için gerekli) **6,48 kW/kg**. Ölçülmüş termal
tavana açık **3,8 kat**, ölçülmüş sürekli hıza **6,3 kat**. Zaten en açık sayı
daha da açıldı.

## Selig ölü bandı — elimizdeki kaynakta duruyordu

Bir okuma, 39 mm kaportanın C_lα = 4,0 /rad varsayımının düşük Re'de sorunlu
olduğunu söyledi ama bizde olmayan bir kaynağa dayandı. **Elimizdeki Selig
Cilt 2'de doğrudan buldum:**

> "past work on **symmetrical** airfoils has shown that a **deadband often
> appears in the lift curve near zero degrees**… Interestingly, cambered
> airfoils do not appear to have a similar, intrinsic deadband region."

ve bir başka kesit için, Re 60 000 ve 100 000'de ölü bant var, daha yüksek
Re'de yok — "this type of behavior is **usually only seen on symmetrical
airfoils at low Re's**".

Kaportamız: **simetrik, Re ≈ 80 000, 1–2° toe**. Tam bandın içinde. Yani 4,0
artık "2π'den küçük olduğu için muhafazakâr" değil, bir **üst sınır** — çünkü
ölçümlerin kaldırdığı şey eğimin büyüklüğü değil, eğrinin o bölgede
**doğrusallığı**. Sıfırdan geçen doğrusal bir türevle hesaplanan yön kararlılığı
marjı, verilerin "yok" dediği tek parça üzerinde hesaplanmış oluyor.

Aynı kaynak çareyi de adlandırıyor ve bize bedava: **kamburluk**. Dışa kamburlu
ve dışa toe'lu bir kaporta, doğrusal parçası olan bir eğrinin üzerinde çalışır.
Makale o kaportayı **boyutlandırmıyor** — ölçmediği bir eğriden eğim seçmek,
az önce kaydettiği hatanın tekrarı olurdu.

## Çürütülenler — bunlar dışarıdan geldi ve tutmadı

| iddia | gerçek |
|---|---|
| "Sabit yakıt kütlesi sütunu yanlış: −36,5 değil −50,2" | **Makale doğru.** Yeniden boyutlandırınca −36,6 / +0,3 çıkıyor. İtiraz MTOW'u birinci sütundan sabit tutmuş; o bir sözleşme değil, iki kuralın karışımı. |
| "Eş eksenli çift 2A alanıyla hesaplanmalı, FM 0,495" | Eş eksenli çiftin standart muamelesi **tek disk + girişim kaybı**dır. Makale tam onu yapıyor. |
| "Dayanıklılık aritmetiği kapanmıyor" | Kapanıyor: D = 40,875 N → 1 226 W itki → /0,80/0,92 = 1 666 W; 24,71 kWh ÷ 1,666 = 14,83 h → 1 602 km. İtiraz 1,7'yi yuvarlanmış almış. |
| "NASA sayıları yanlış, doğrusu 4,9/3 735 ve 9,3/7 517" | **Johnson & Silva PDF'ini açtım**: quadrotor/turboshaft 4,9 / 3 678; lift+cruise/turbo-electric 8,5 / 7 271. Bizim sayılarımız birebir doğru. Yanlış olan tek şey atıf numarasıydı ([7] → [22]). |

Son satır özellikle önemli: iddia "üç şey aynı anda yanlış" diyordu; kaynağı
açınca **bir şey** yanlış çıktı. Kaynağa bakmadan karar vermenin iki yönü de
var.

## §3.7'nin asıl kusuru — dördü de kaçırdı

Atıf yanlıştı, evet. Ama asıl sorun mantıktaydı: "özel kaldırma sistemi taşıyan
konfigürasyon **daha düşük seyir verimi ve** daha yüksek ağırlık göstermeli"
deniyor, ve kanıt olarak quadrotor (4,9 / 3 678) → lift+cruise (8,5 / 7 271)
çifti veriliyordu. Ama quadrotor'da özel kaldırma sistemi **yok** ve verimi
*düşük*; lift+cruise'da **var** ve verimi *yüksek*. Tablo o sıralamayı
göstermiyor.

Doğru — ve daha keskin — tahmin şu: ağırlık cezası, mimarinin satın aldığı
seyir verimiyle **telafi edilmiyor**. Bu, bariz savunmayı yasaklıyor. Ve tablo
tam onu gösteriyor: %70 daha iyi seyir verimi, neredeyse iki katı ağırlık.
§3.2 ve §9 bunu zaten doğru söylüyordu; yalnız §3.7 kendi kaynağını yanlış
okumuştu.

## Kalanlar

- S1 süreklilik tablosundan **%10 artık payı satırı** düşmüştü; toplamlar
  betikte doğruydu, tablo kendi toplamını vermiyordu. Satır eklendi, ikame
  edilen aralık tek kurala oturtuldu: **0,0201 – 0,0231**.
- S4'ün muhafazakâr dönme marjı **1,59 değil 1,14** (17,6/15,4), yumuşak
  profilde **0,76**. "Still comfortable" cümlesi kaldırıldı.
- §7.4 "control **power** ∝ 1/t²" diyordu; moment 1/t², **güç 1/t³** — ve
  Tablo 4 zaten 1/t³. (Girişleri t³ ile çarpınca %0,3 içinde sabit.)
- S6 "menzil itki verimini içermez" diyordu; pervane 0,80, **η_chain'in
  içinde**. Düzeltme eğik mimarinin fixed-fraction avantajını +%12'den
  ≈ −%5'e çeviriyor — yani **aleyhine**, lehine değil.
- §8.5 ve S5.17 "hiçbiri deney gerektirmiyor" diyordu, sonuç bölümü ise "bu
  artık doğru değil". İkisi de düzeltildi: geçiş yunuslama momenti **ve**
  kaporta türevi tünel istiyor.
- Girişteki sıfır-fatura cümlesi §5.3'ün nitelendirmesini taşımıyordu.
- **S5 eski 8.1–8.17 numaralandırmasını koruyordu**, gövdedeki 8.1–8.5 ile
  çakışıyordu; beş ekte altı kırık atıf. S5.1–S5.17 yapıldı, atıflar tek tek
  bağlamıyla doğrulandı — kaskad regex yok (o hatayı bir kez yaptım).
- Şekil 7 ve 8 kısaltmada atıflarını kaybetmiş, ikisi de §4.4'e ait. Geri
  bağlandı; on iki şeklin hepsi yerleşiyor.
- "measured uncertainty budget" → "quantified sensitivity budget"; "exactly
  three" → üç yinelenen ücret; kaçış koşulu dört parçalı verildi (tampon şartı
  dahil); VLM iptal argümanı koşullu yapıldı; AR 6,00 → 6,03; [47] 2026;
  Funding beyanı dolduruldu.

## Açık kalanlar

1. **Drones'un format zorunluluğu.** mdpi.com proxy'de bloklu, açamadım. Ve
   iki okuma birbiriyle çelişiyor: biri IMRaD'ın zorunlu olduğunu, diğeri
   uzunluk sınırı olmadığını söylüyor. Yazarların bizzat bakması gerek.
2. **Çift taraflı şerit ölçümü.** Aradığımız cihazın modern adı **split drag
   rudder** — B-2'nin, YB-49'un kullandığı şey; DLR-F19 üzerinde de denenmiş.
   TR-796'nın 1944'te "veri yetersiz" dediği düzenek sonradan kuruldu ve
   ölçüldü. **Hiçbirini açmadım**; bu bir arama yönü, atıf değil. Arama
   özetleri iki şey ima ediyor, ikisi de doğrulanmamış: çift taraflı çıkıntı
   yunuslama momentini büyük ölçüde iptal ediyor (lehimize), ve ürettiği
   yuvarlanma momenti hücum açısıyla **işaret değiştiriyor** (aleyhimize,
   çünkü geçişte 17–22°'ye çıkıyoruz).
