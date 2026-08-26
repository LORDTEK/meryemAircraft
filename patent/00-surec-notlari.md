# Başvuru süreci — notlar

> ⚠️ **Ben patent vekili değilim.** Bu klasördeki metinler, künyedeki tasarım
> kayıtlarından türetilmiş **taslaklardır.**
> Hukuki geçerlilik denetimi yapılmamıştır.

## Sıra (N57) — değişmez

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

## Yapılacaklar

- [x] ~~Resimleri çizgi resim olarak üret~~
- [x] ~~PDF'leri hazırla~~
- [ ] IEEE 2016 (Xu grubunun eski çalışması) okunmalı — istem daraltması gerekebilir
- [ ] Ücret tarifesi kontrol (araştırma talebi dâhil)
