# Şekil üretimi

Şekiller **yeniden üretilebilir**. Bölüm 8.12'deki "başka bir grup bunu
bağımsız olarak deneyebilir" iddiasının somut karşılığıdır.

| Dosya | Ne yapar |
|---|---|
| `figlib.py` | 3B modeli başsız Chromium'da açar, kamerayı sürer, ekran görüntüsü alır, otomatik kırpar |
| `mkfig.py` | Şekil 4 (üç görünüş), Şekil 5 (serbest), Şekil 11 (iki ölçek) |
| `mkplot.py` | Şekil 10a (geçiş / dönüş süresi), Şekil 10b (tırmanarak giriş) |
| `mkfig12.py` | Şekil 12 (menzil – L/D düzlemi) |
| `gecis2.py` | Geçiş benzetimi — 2 serbestlik dereceli nokta kütle |

**Bağımlılıklar:** `playwright`, `pillow`, `matplotlib`. Chromium yolu
`figlib.py` içindeki `CHROME` değişkeninde.

**Çalıştırma sırası:** `figlib.py` bir kütüphanedir, doğrudan çalıştırılmaz.
Önce `../kaynak/govde-etudu.html` dosyasına render kancası enjekte edilmiş bir
kopya üretilir (kaynak dosya **değiştirilmez**), sonra `mkfig.py` çalışır.

⚠️ Kaynak model `../kaynak/govde-etudu.html` bir IIFE içindedir; kanca
`window.__fig` olarak enjekte edilir. Enjeksiyon kodu `mkfig.py` başında.

## Şekil 12'nin iki bağımsız doğrulaması

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
| 1 | `sekil01-iki-aile.png/.svg` | `mkconcept.py` |
| 2 | `sekil02-zaman-cizelgesi.png/.svg` | `mkfig02.py` |
| 3 | `sekil03-uc-fatura.png/.svg` | `mkconcept.py` |
| 4 | `sekil04-uc-gorunus.png` | `mkfig.py` (3B) |
| 5 | `sekil05-serbest-gorunus.png` | `mkfig.py` (3B) |
| 6 | `sekil06-dagilimlar.png/.svg` | `mkfig06.py` |
| 7 | `sekil07-moment-kollari.png/.svg` | `mkfig07.py` |
| 8 | `sekil08-kanatcik-iz.png/.svg` | `mkfig08.py` |
| 9 | `sekil09-ucus-profili.png` | `mkfig09.py` (3B + döndürme) |
| 10a | `sekil10a-gecis-donus-suresi.png/.svg` | `mkplot.py` |
| 10b | `sekil10b-tirmanarak-giris.png/.svg` | `mkplot.py` |
| 11 | `sekil11-iki-olcek.png` | `mkfig.py` (3B) |
| 12 | `sekil12-menzil-LD.png/.svg` | `mkfig12.py` |

**Şekil 8** planformu modelin ok açısı yasalarından yeniden kurar, iz sınırını
ve şeridi üzerine bindirir. Model izi çizmediği için bu şekil tamamen Python'da
üretilir; geometri yasaları `mkfig06.py` ile aynıdır.

## Yöntem notları

**Şekil 9'daki döndürme geometrik olarak doğrudur:** yunuslama ekseni yan görünüş
düzlemine dik olduğu için, yan görünüş silüetini döndürmek aracı gerçekten
döndürmekle aynı sonucu verir.

**Şekil 8'in ürettiği yeni sayı:** şerit, boyunun **%45,6**'sında iz sınırını
kesiyor (yarı-açıklığın %30,7'sinde). Yani iç %46 hover'da, dış %54 seyirde
çalışıyor. Bu sayı künyede yoktu; şekil üretilirken çıktı.

**Şekil 6 geometriyi bağımsız doğruladı:** modelin yasaları Python'da yeniden
kurulunca açıklık 3,453 m, alan 1,9785 m², AR 6,026 çıktı — künyeyle örtüşüyor.
Aynı hesap makale metnindeki **yanlış ok açılarını yakaladı**.
