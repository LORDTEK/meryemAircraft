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

## Üretilmiş şekiller

| # | Dosya | Durum |
|---|---|---|
| 4 | `sekil04-uc-gorunus.png` | ✅ |
| 5 | `sekil05-serbest-gorunus.png` | ✅ |
| 10a | `sekil10a-gecis-donus-suresi.png/.svg` | ✅ |
| 10b | `sekil10b-tirmanarak-giris.png/.svg` | ✅ |
| 11 | `sekil11-iki-olcek.png` | ✅ |
| 1,2,3,7,8,9 | kavramsal çizimler | ⏳ SVG olarak elde çizilecek |
| 6 | ok açısı / kalınlık dağılımı | ⏳ |
| 12 | `sekil12-menzil-LD.png/.svg` | ✅ |
