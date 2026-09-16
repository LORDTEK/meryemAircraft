# Şekil üretimi

Şekiller **yeniden üretilebilir**. Bölüm 8.12'deki "başka bir grup bunu
bağımsız olarak deneyebilir" iddiasının somut karşılığıdır.

| Dosya | Ne yapar |
|---|---|
| `figlib.py` | 3B modeli başsız Chromium'da açar, kamerayı sürer, ekran görüntüsü alır, otomatik kırpar |
| `mkfig.py` | Şekil 5 (üç görünüş), Şekil 6 (serbest), Şekil 10 (iki ölçek) |
| `mkplot.py` | Şekil 12a (geçiş / dönüş süresi), Şekil 12b (tırmanarak giriş) |
| `mkfig03.py` | Şekil 3 (menzil – L/D düzlemi) |
| `transition2.py` | Geçiş benzetimi — 2 serbestlik dereceli nokta kütle |

**Bağımlılıklar:** `playwright`, `pillow`, `matplotlib`. Chromium yolu
`figlib.py` içindeki `CHROME` değişkeninde.

**Çalıştırma sırası:** `figlib.py` bir kütüphanedir, doğrudan çalıştırılmaz.
Önce `../kaynak/body-study.html` dosyasına render kancası enjekte edilmiş bir
kopya üretilir (kaynak dosya **değiştirilmez**), sonra `mkfig.py` çalışır.

⚠️ Kaynak model `../kaynak/body-study.html` bir IIFE içindedir; kanca
`window.__fig` olarak enjekte edilir. Enjeksiyon kodu `mkfig.py` başında.

## Şekil 3'ün iki bağımsız doğrulaması

Menzil bağıntısı $R = (m_e/m)\,E^*\,\eta\,(L/D)/g$ iki ayrı noktadan sınandı:

| Girdi | Hesap | Bağımsız değer |
|---|---:|---:|
| Pil hattı, L/D = 13,5 | **116 km** | Bacchini tezi, Cora tabanı: **119 km** |
| Hibrit hat, L/D = 12,7 | **1 693 km** | Bölüm 6.2: **1 695 km** |

Aynı basit bağıntı hem **dış bir yayımlanmış sonucu** hem de **bizim kendi
sayımızı** yeniden üretiyor. Bu, Bölüm 6.1'in menzil yönteminin bağımsız
kontrolüdür.

## Ölçek doğrulaması

Hafif ve ağır hattın çerçeveleme yarıçapları **3,399** oranında çıkıyor.
Beklenen uzunluk ölçeği **3,35**. Bu, iki hattın gerçekten aynı geometriden
ölçeklendiğinin bağımsız kontrolüdür.

## Üretilmiş şekiller — **12/12 TAMAM**

| # | Dosya | Üreten |
|---|---|---|
| 1 | `fig01-two-families.png/.svg` | `mkconcept.py` |
| 2 | `fig02-timeline.png/.svg` | `mkfig02.py` |
| 3 | `fig03-range-LD.png/.svg` | `mkfig03.py` |
| 4 | `fig04-three-bills.png/.svg` | `mkconcept.py` |
| 5 | `fig05-three-views.png` | `mkfig.py` (3B) |
| 6 | `fig06-general-view.png` | `mkfig.py` (3B) |
| 7 | `fig07-distributions.png/.svg` | `mkfig07.py` |
| 8 | `fig08-moment-arms.png/.svg` | `mkfig08.py` |
| 9 | `fig09-strip-slipstream.png/.svg` | `mkfig09.py` |
| 10 | `fig10-two-scales.png` | `mkfig.py` (3B) |
| 11 | `fig11-flight-profile.png` | `mkfig11.py` (3B + döndürme) |
| 12a | `fig12a-transition-rotation-time.png/.svg` | `mkplot.py` |
| 12b | `fig12b-climbing-entry.png/.svg` | `mkplot.py` |

> Numaralar makalenin **ilk atıf sırasına** göredir. Dosya adları da bu
> numarayı taşır; MDPI şekil dosyalarını ayrı yüklettiği için adın
> numarayla tutması gerekiyor. Numara bir daha kayarsa hem `figures/cikti`
> adları hem `paper/build/captions.py` hem de bu tablo birlikte döner.

**Şekil 9** planformu modelin ok açısı yasalarından yeniden kurar, iz sınırını
ve şeridi üzerine bindirir. Model izi çizmediği için bu şekil tamamen Python'da
üretilir; geometri yasaları `mkfig07.py` ile aynıdır.

## Yöntem notları

**Şekil 11'deki döndürme geometrik olarak doğrudur:** yunuslama ekseni yan görünüş
düzlemine dik olduğu için, yan görünüş silüetini döndürmek aracı gerçekten
döndürmekle aynı sonucu verir.

**Şekil 9'un ürettiği yeni sayı:** şerit, boyunun **%45,6**'sında iz sınırını
kesiyor (yarı-açıklığın %30,7'sinde). Yani iç %46 hover'da, dış %54 seyirde
çalışıyor. Bu sayı künyede yoktu; şekil üretilirken çıktı.

**Şekil 7 geometriyi bağımsız doğruladı:** modelin yasaları Python'da yeniden
kurulunca açıklık 3,453 m, alan 1,9785 m², AR 6,026 çıktı — künyeyle örtüşüyor.
Aynı hesap makale metnindeki **yanlış ok açılarını yakaladı**.
