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

İkinci sürümde formül düzeltilmeli: ya seyir hızı azami L/D noktasına
çekilmeli, ya da menzil gerçek seyir L/D'siyle hesaplanmalı.

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
5. **Göbek ölçüleri seçilmedi**; 30–50 mm aralığı bir sınır, ölçüm değil.
