# Başvuru süreci — notlar

> ⚠️ **Patent vekili tarafından hazırlanmamıştır.** Bu klasördeki metinler,
> tasarım künyesindeki kayıtlardan türetilmiş **taslaklardır.** Hukuki geçerlilik
> denetimi yapılmamıştır.

## ✅ DURUM: BAŞVURU YAPILDI

| | |
|---|---|
| **Başvuru numarası** | **2026/014570** |
| Evrak numarası | 2026-GE-595375 |
| Evrak tarihi | 26.08.2026 20:28:22 |

**Rüçhan tarihi bu başvurunun tarihidir.** Yurt dışı başvuruları için 12 aylık
süre bu tarihten işler: **26.08.2027**.

⚠️ Dışarıya verilecek tek numara **başvuru numarasıdır (2026/014570).** Evrak
numarası ve evrak tarihi TÜRKPATENT'in iç evrak takip kayıtlarıdır; yayında,
makalede ya da sosyal medyada paylaşılmaz.

Bu, projede bir eşiktir. Sonuçları:

- **Makale artık yayımlanabilir.** N57'nin sırası tamamlandı. Başvuru tarihi
  sabitlendiği için, bundan sonraki kendi yayımımız kendi başvurumuzun
  yeniliğini bozmaz.
- **Yurt dışı için 12 aylık rüçhan süresi başladı.** Bu süre içinde yapılacak
  başvurular Türkiye başvuru tarihinden yararlanır — Avrupa dâhil.
- **Araştırma talebi süresi işliyor** (başvuruyla birlikte talep edilmediyse
  12 ay). Kaçırılırsa başvuru geri çekilmiş sayılır.

### Sıradaki iş (dinlenildikten sonra)

Makalenin nereye konacağı konuşulacak: arXiv, Zenodo, SSRN ya da doğrudan
dergi. Karar verilmedi, acele yok.

⚠️ Makale yayımlanmadan önce yapılacak son kontroller:
- Teşekkür bölümü (genel ifade, marka/model adı yok)
- Conflicts of Interest: **bekleyen patent başvurusu beyan edilecek**
- Kaynak defterindeki `C` seviyesindeki kayıtlar (IEEE 2016, VFS 2025)

---

## Sıra (N57) — tamamlandı

```
prior-art taraması → başvuru ve makale birlikte yazılır → BAŞVURU → yayım
```

⚠️ **Makale, başvuru yapılmadan hiçbir yere konmaz.** arXiv dâhil.
Avrupa'da (EPC) kendi yayımına **tolerans yoktur**; bir gün önce yayımlanmış
makale, Avrupa patent hakkını tümüyle yok eder.

## Başvuru paketi

| Belge | Dosya | Durum |
|---|---|---|
| Tarifname | `pdf/01-tarifname.pdf` — 8 sayfa | ✅ hazır |
| İstemler | `pdf/02-istemler.pdf` — 3 sayfa, 17 istem | ✅ hazır |
| Özet | `pdf/03-ozet.pdf` — 1 sayfa, 127 kelime | ✅ hazır |
| Resimler | `pdf/04-resimler.pdf` — 5 sayfa | ✅ hazır |
| Başvuru formu | EPATS üzerinden çevrimiçi | — |

**Kaynak metinler:** `01-tarifname.md`, `02-istemler.md`, `03-ozet.md`
(çalışma notlarıyla birlikte). PDF'ler bu notlardan **arındırılmış** temiz
sürümlerdir; içerik `tarifname_icerik.py` içinde tutulur, `mkpdf.py` ile
üretilir.

## Başvuru türü

**Patent Başvurusu** seçilecek — faydalı model değil. Gerekçe: istem 17 bir
**yöntem istemidir** ve faydalı modelde korunmaz; ayrıca 20 yıl / 10 yıl farkı
ve yurt dışı başvuruları için daha sağlam temel. İşlemler sırasında faydalı
modele dönüşüm mümkündür — araştırma raporu olumsuz gelirse rota değiştirilebilir.

## ⚠️ 12 aylık araştırma süresi

**Araştırma talebi ve ücreti başvuru tarihinden itibaren 12 ay içinde**
yapılmalıdır. Yapılmazsa başvuru **geri çekilmiş sayılır.** Kaçırılması en kolay
ve en pahalı süre budur.

## Resimler — üretildi

Beşi de **siyah-beyaz çizgi resim** olarak sıfırdan çizildi (makale renderları
dönüştürülmedi). Üretici betik: `gorsel/uretim/patent-resimleri.py`

| Şekil | İçerik |
|---|---|
| Şekil 1 | Perspektif görünüş, tüm unsurlar numaralı |
| Şekil 2 | Üstten görünüş (planform) |
| Şekil 3 | Önden görünüş — uç iskeletleri ve dikey ayrım |
| Şekil 4 | **Alttan görünüş** — yuvarlanma şeridi (5) ve pervane izi (13) |
| Şekil 5 | Güç akış şeması — seri hibrit |

## Millî güvenlik — bilgi notu (düzeltildi)

⚠️ **Bu sorulacak bir şey değildir.** Daha önce "başvuru öncesi sorulacak ilk
soru" diye yazmıştım; yanlıştı. Kurum, başvuruları millî güvenlik yönünden
**kendisi değerlendirir** ve gerekirse Millî Savunma Bakanlığı'na yönlendirir.
Başvuru sahibi olarak yapılacak bir işlem yoktur.

Bilinmesi gereken tek şey: böyle bir karar çıkarsa başvuru gizli tutulabilir ve
yayımı ertelenebilir. **Bu durumda makale yayım planı da etkilenir.**

## Ödemesiz süre haritası — hatırlatma

| Ülke / bölge | Kendi yayımına tolerans |
|---|---|
| Türkiye | 12 ay |
| ABD | 12 ay |
| **Avrupa (EPC)** | **YOK** |
| Japonya | 12 ay (şartlı) |
| Çin | 6 ay (dar) |

## PDF üretiminde yakalanan hatalar (kayıt)

Bu hatalar **gözle bakılarak** bulundu; metin çıkarımı hiçbirini yakalamamıştı.
Ders: PDF üretildikten sonra her sayfa görüntü olarak açılıp bakılmalıdır.

| Hata | Sebep | Çözüm |
|---|---|---|
| Özette "Şekil 1" satırının altı boş | Şekil metin olarak anılmış, gömülmemiş | Şekil 1 özete gömüldü |
| Resimlerde "Şekil N" iki kere | Başlık hem PNG'ye gömülü hem PDF'te | PNG'ler başlıksız yeniden üretildi |
| Şekil 4'te **13 numarası görünmüyor** | matplotlib etiketleri eksen sınırlarını genişletmiyor → kırpılıyor | Etiket konumları görünmez nokta olarak autoscale'e dâhil edildi + etiket kanat dışına taşındı |
| Resimler sayfada küçük | Çizim alanında geniş beyaz boşluk | PNG'ler otomatik kırpıldı |
| "Şekillerdeki referans numaraları" başlığı tablosundan ayrı sayfada | Sayfa sonu denetimi yok | `page-break-after: avoid` |

## Yapılacaklar

- [x] ~~Resimleri çizgi resim olarak üret~~
- [x] ~~PDF'leri hazırla~~
- [ ] IEEE 2016 (Xu grubunun eski çalışması) okunmalı — istem daraltması gerekebilir
- [ ] Ücret tarifesi kontrol (araştırma talebi dâhil)

---

## Şekli inceleme yanıtı — 2026/014570 (bildirim 31.08.2026)

TÜRKPATENT şekli inceleme bildirimi dört eksik saydı. Dördü de giderildi
ve her biri **ölçülerek** doğrulandı (üretildi demek düzeldi demek
değil). Yanıt için son tarih: bildirimden itibaren iki ay.

| # | İstenen | Yapılan | Doğrulama |
|---|---|---|---|
| 1 | Tarifname → İstemler → Özet'te birbirini takip eden sayfa numarası | Üç bölüm tek belge olarak dizilip `page_ranges` ile bölündü | 1/12…8/12, 9/12…11/12, 12/12 |
| 2 | Üç bölümde satır numaralandırması | Üretilen PDF'ten gerçek satır kutuları okunup damgalandı | 315 satır denetlendi, 58 numaralı, **hata 0** |
| 3 | Buluş başlığı Özet'e eklenmeli, aynı olmalı | Aynı `BASLIK` değişkeninden geliyor | İki PDF'in başlığı **birebir aynı** |
| 4 | Özet'teki şekil ve "Yayımlanacak şekil:" ibaresi çıkarılmalı | Gömülü PNG kaldırıldı, ibare "Şekil 1"e indirildi | Gömülü görüntü **0**, "Yayımlanacak" **0** |

**Kapsam aşımı yok.** Tarifname ve İstemler metin kaynakları
(`tarifname_icerik.py`, `01-tarifname.md`, `02-istemler.md`)
değiştirilmedi — `git diff` boş. Özet'teki iki değişiklik (başlık
eklenmesi, şeklin çıkarılması) bildirimin kendi talebidir.

### Satır numaralandırmada iki hata yaptım, ikisi de ölçümle bulundu

1. Satır kutularını **tarayıcıda** ölçüyordum (1280 px genişlik), PDF
   ise A4 baskı alanında (165 mm) diziliyordu — satır sonları farklıydı.
   Düzeltme: gövde genişliği 165 mm'ye sabitlendi.
2. Bu düzelttikten sonra 1. sayfa tuttu ama 5. ve 8. sayfalar kaydı.
   Nedeni: başlıklardaki `break-after: avoid` sayfalama sırasında
   içeriği itiyor, mutlak konumlu numaralar yerinde kalıyordu.

Tahmin etmeyi bırakıp **üretilen PDF'ten** ölçmeye geçildi:
`pdftotext -bbox-layout` ile her sayfadaki gerçek satır kutuları okunup
numaralar `reportlab` ile oraya damgalanıyor. Tablo hücreleri ayrı
`<line>` geldiği için aynı görsel satırdakiler birleştiriliyor.

### ÇÖZÜLMEMİŞ: numaralandırma düzeni doğrulanamadı

Bildirimin işaret ettiği **Patent-Faydalı Model Başvuru Kılavuzu'na
erişemedim** (ağ vekili 403 döndürüyor). Bu yüzden şu seçim
**doğrulanmamıştır**: numaralar **her sayfada** 5, 10, 15… diye
başlıyor (PCT Kural 11.8'in "sets of five" uygulaması). Alternatif,
bölüm boyunca sürekli numaralandırmadır.

Değiştirmek tek satır: `mkpdf.py` içinde `SATIR_SAYFA_BASI = False`.

**Kılavuz indirilip bakılmadan gönderilmemelidir.**
