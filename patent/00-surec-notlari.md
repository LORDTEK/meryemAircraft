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

---

## Kılavuz denetimi (02.09.2026)

Başvuru sahibi, TÜRKPATENT **Patent/Faydalı Model Başvuru Kılavuzu**'nu
(`kaynakca/7178ed2b-...pdf`, "Patent kılavuz 2022", 48 s.) repoya koydu.
Şekli inceleme bildirimine verilen cevap, kılavuza karşı **birinci elden**
denetlendi. Bildirimde adı geçmeyen **dört uygunsuzluk daha** çıktı.

Belirleyici kaynak, kılavuzun **s.18**'indeki kenar marjı şeması: tarifname
ve resim sayfalarının nasıl görünmesi gerektiğini tek çizimde gösteriyor.

### Bildirimin dört maddesi — durum değişmedi, hepsi karşılanıyor

Sayfa numaralarının sürekliliği, satır numaralandırması, Özet'e başlık
eklenmesi, Özet'ten şeklin çıkarılması: dördü de yerinde.

### Kılavuzdan çıkan, bildirimde olmayan dört düzeltme

**1. Satır numarası aralığı — DEĞİŞİKLİK YOK, doğrulandı.**
> s.15: "Her bir sayfanın satırları, her beş satırda bir; beş ve beşin
> katları olacak şekilde numaralandırılmalıdır."

"Her bir sayfanın" ifadesi, numaralandırmanın **her sayfada yeniden**
başladığını söylüyor. s.18 şeması da bunu gösteriyor (tek sayfada
5…35). Kodda `SATIR_SAYFA_BASI = True` zaten böyleydi. Cevap gönderilmeden
önce açık bırakılan tek soru buydu; kılavuz onu kapattı.

**2. "TARİFNAME" başlığı eksikti — EKLENDİ.**
> s.13: "Tarifnamenin en başına 'TARİFNAME', bunun altına da 'Buluş
> Başlığı' yazılmalıdır."

Belge doğrudan buluş başlığıyla başlıyordu. s.18 şemasında ilk satır
"TARİFNAME", altındaki buluş başlığı; ilk satır numarası (5) "Teknik
Alan"a düşüyor. Üretilen belgede de öyle: TARİFNAME=1, başlık=2-4,
TEKNİK ALAN=5.

**3. Özette sıra tersti — DÜZELTİLDİ.**
> s.15: "Özetin en başına 'ÖZET', bunun altına da buluş başlığı
> yazılmalıdır."

Bildirime cevapta başlık **üstte**, "ÖZET" **altta** konmuştu. Kılavuz
bunun tersini istiyor. Sıra çevrildi. (Başlığın tarifnamedekiyle aynı
olma şartı zaten kodla garanti — ikisi de tek `BASLIK` değişkeninden.)

**4. Sayfa numarası biçimi yanlıştı — DÜZELTİLDİ.**
> s.15: "Resim sayfalarının numaralandırılması, **diğerlerinden farklı**
> olmalıdır. Bu numaralandırma, 'ilgili sayfanın numarası / toplam resim
> sayfası sayısı' şeklinde olmalıdır."

"n/toplam" biçimi **resim sayfalarına ait**. Metin sayfaları ondan farklı,
yani düz ardışık numara taşımalı. Bizde ikisi de "n / toplam" idi. s.18
şeması açık: metin sayfasında altta ortada yalnız "1", resim sayfasında
üstte "1/3". Ayrıldı: metin 1…12, resim 1/5…5/5 (üstte, sağda).

**5. Satır numaraları sol marja taşıyordu — DÜZELTİLDİ.**
Ölçüldü: numaraların sol kenarı kâğıt kenarından **21,5 mm**'deydi;
kılavuzun (s.18) asgari sol marjı **2,5 cm**. Numaralar sağa kaydırıldı
(sağ kenarları 31 mm); iki haneli numara 27,8 mm'de başlıyor, metin
34 mm'de. Yeni ölçüm: 27,5 mm. Hem kılavuzun asgari marjına hem PCT
Kural 11.8'in "marjın sağında" şartına uyuyor.

### Değişiklik gerekmediği ölçülerek doğrulananlar

| Şart (kılavuz) | Bizde | Sonuç |
|---|---|---|
| Sol marj 2,5–4 cm | 27,5 mm | ✔ |
| Sağ marj 2–3 cm | 20,1 mm | ✔ |
| Üst 2–4 cm / alt 2 cm | 25 / 20 mm | ✔ |
| Satır arası 1,5 | 20,25 pt ölçüldü (Word 1,5 ≈ 19,8 pt) | ✔ |
| "İstem sayfasının başına SADECE 'İSTEMLER'" | başlık tekrarlanmıyor | ✔ |
| Her unsur yeni sayfada | `break-before: page` | ✔ |
| Resimde çerçeve/renk/gölge yok, yazı yok | yalnız referans no + "Şekil n" | ✔ |
| Bültende yayımlanacak resim ilk sayfada | Şekil 1 ilk sayfada | ✔ |

### Doğrulama

`denetle.py` üretilen PDF'leri ölçerek denetliyor (görsel kontrol değil):

- sayfa numaraları: `['1'…'12']`, tarifname→istemler→özet sırasında sürekli
- resim sayfaları: `['1/5'…'5/5']`, üstte, metinden farklı biçimde
- satır numaraları: **316 satır, 59 numaralı, 0 hata** (5'in katlarında var,
  diğerlerinde yok — ikisi de denetleniyor)
- başlık tarifname ile özette birebir aynı
- özette gömülü resim yok, "Yayımlanacak" geçmiyor
- marjlar sınırlar içinde

**Kapsam aşımı yok.** `tarifname_icerik.py`, `01-tarifname.md`,
`02-istemler.md`, `03-ozet.md` üzerinde `git diff` boş; 17 istemin hepsi
yerinde. Değişenlerin tamamı dizgi (`mkpdf.py`, `mkpdf_css.py`).

---

## Şekli eksiklikler GİDERİLDİ — Kurum bildirimi (02.09.2026)

TÜRKPATENT, 02/09/2026 tarihli bildirimle şekli eksikliklerin giderildiğini
tespit etti (SMK m.95/3, Yönetmelik m.96/1). Başvuru 2026/014570 şekli
incelemeyi geçti.

**Sırada ne var**

- **Araştırma raporu.** Araştırma talebi başvuruyla birlikte yapılmış ve
  ücreti ödenmiş; Kurum raporu düzenleyip gönderecek (SMK m.96/2,
  Yönetmelik m.97/3). Ayrıca bir işlem gerekmiyor.
- **Yayım.** Başvuru tarihinden (26/08/2026) itibaren **18 ay** dolunca
  Bültende yayımlanır → **26/02/2028**. Erken yayım talebiyle öne
  çekilebilir.
- **Yıllık ücretler.** Üçüncü yıldan başlayarak her yıl vadesinde. Vade
  günü başvuru tarihine denk gelen ay ve gün: **26 Ağustos**. İlk vade
  **26/08/2028**. Ödenmezse ek ücretle altı ay daha (26/02/2029'a kadar);
  o da kaçırılırsa **başvuru geçersiz** olur.

**Makale yayım planına etkisi.** Daha önce not edilen ödemesiz süre
haritası şimdi bağlayıcı hâle geliyor: Avrupa'da (EPC) kendi yayımına
tolerans **yoktur**. Başvuru 26/02/2028'de yayımlanacak; makalenin ondan
önce yayımlanması EPC yolunu kapatır. Makale bu tarihten sonraya
planlanmalı ya da EPC'den bilinçli olarak vazgeçilmelidir.
