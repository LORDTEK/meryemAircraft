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

## Sırada

`C_D0` hâlâ **varsayım** (0,0248). Bileşen bileşen kurulması gerekiyor:
kanat kesitlerinin ağdalı sürüklemesi (NeuralFoil şerit yöntemiyle), uç
iskeletlerinin kaportalı kesitleri, pervane göbekleri. Menzil doğrudan buna
bağlı olduğu için ikinci sürümün asıl işi budur.
