# Bacchini 2021 — okuma planı ve karşılaştırmanın şekli

**Durum: kaynak elde YOK, bekleniyor.** Bu dosya, PDF geldiğinde işin yorum
değil mekanik olması için önceden yazıldı. **Buradaki hiçbir sayı Bacchini
2021'den değildir** — hepsi bizim kendi makalemizden, yerinden okunarak.

> Bacchini, A.; Cestino, E.; Magill, B.; Verstraete, D. *Impact of lift
> propeller drag on the performance of eVTOL lift+cruise aircraft.*
> Aerospace Science and Technology **2021**, 109, 106429.

**Kural (`references.md` düzeni):** bu kaynağa, PDF birinci elden okunana kadar
**hiçbir sayı bağlanmaz.** Arama motoru özetlerinde dolaşan "%38 / %13" gibi
değerler bu projede üç kez yanlış çıkmış bir kaynak sınıfındandır. Okunmadan
yazılmaz.

---

## 1. Bizim tarafımız — karşılaştırmaya girecek sayılar, kaynağıyla

Hepsi `paper/paper-v7.md` §3.3'ten, referans geometri `§2` ve Tablo 4'ten.

| Büyüklük | Değer | Nerede |
|---|---|---|
| Referans kanat alanı | 1,979 m² (açıklık 3,453 m, AR 6,03) | §2 |
| Uç pervane sayısı | **8 disk** (dört eşeksenli çift) | §3.3 |
| Toplam süpürülen alan | 0,251 m² = **kanat alanının %12,7'si** | §3.3 |
| Hesaplanan durum | **serbest dönme** — net şaft torku sıfır, 30 m s⁻¹'de | Tablo 4 |
| Seçilen tasarım | kesit c_l 0,68 · FM 0,63 · 25 000 rpm · uç Mach 0,77 | Tablo 4 |
| **Serbest dönme yükü** | **ΔC_D0 = 0,0154** (kanat alanına indirgenmiş) | Tablo 4 |
| Varsayılan temiz gövde C_D0 | 0,0248 | §3.3 |
| Yükün payı | 0,0154 / 0,0248 = **%62** | §3.3 |
| Durdurulmuş, kenarı öne | 0,0008 — **yirmi kat ucuz** | Tablo 3 |
| Durdurulmuş, yanlamasına | 0,015 – 0,018 | Tablo 3 |
| Yöntem | pervane-element momentum kuramı, yedi tasarım taranmış | §3.3 |

**Kritik nokta: bizimki ölçülmedi.** 0,0154 bir hesaptır ve makalenin en büyük
tek defter kalemidir.

---

## 2. Karşılaştırma NEDEN birebir değil — önce bu anlaşılmalı

**Onların ölçtüğü durum ile bizim hesapladığımız durum aynı değil.**

- Bizimki **serbest dönen** pervane: şaft yükü sıfır, rotor 25 000 rpm'de dönüyor.
- Onlarınki, başlıktan ve bilinen özetinden, **durdurulmuş / geri çekilmiş**
  kaldırma pervanesi.

Bu fark karşılaştırmayı **zayıflatmaz, konumlandırır** — ve bunu makalede böyle
yazmak zorundayız. Aksi hâlde bir hakem "aynı şeyi ölçmemişler" der ve haklı olur.

**İki ayrı karşılaştırma biçimi mümkün; hangisinin kurulacağına okuduktan sonra
karar verilecek:**

### Biçim A — büyüklük mertebesi doğrulaması
Onların açıkta kalan kaldırma pervanesi için **ölçtüğü** sürükleme ile bizim
açıkta kalan uç pervanelerimiz için **hesapladığımız** sürükleme aynı mertebede mi?
Bu, 0,0154'ün fiziğine dış bir dokunuş sağlar.

### Biçim B — çerçevenin doğrulanması *(muhtemelen daha güçlü)*
Bizim çerçevemiz her çarenin bir faturayı başka bir faturaya **dönüştürdüğünü**
söylüyor. Pervaneyi geri çekmek tam olarak budur: **Fatura 2 (sürükleme)
→ Fatura 1 (mekanizma kütlesi).** Bacchini bu dönüşümü *ölçmüş*. Eğer öyleyse
bu, çerçevenin tek dış **deneysel** dayanağıdır — NASA boyutlandırma seti
hesapsal bir testti, bu ölçümsel olur.

Ayrıca §3.3 şu anda şunu açıkça itiraf ediyor: indeksleme/geri çekme
mekanizmasının maliyeti ile yirmi kat sürükleme tasarrufu arasındaki ticaret
**bu makalede hiçbir yerde yapılmamıştır.** Bacchini o ticaretin ölçülmüş
tarafını taşıyor olabilir.

---

## 3. Okurken cevaplanacak sorular — sırayla

Bunlar cevaplanmadan tek bir cümle yazılmaz.

**Geometri ve durum**
1. Kaç kaldırma pervanesi, hangi çap, hangi disk yüklemesi?
2. Ölçüm hangi durumda: durdurulmuş mu (hangi azimut?), geri çekilmiş mi,
   serbest dönen bir durum var mı?
3. Rüzgâr tüneli mi, uçuş mu, hesap mı — hangisi hangi sayıyı üretti?

**İndirgeme tabanı — en kritik kalem**
4. Sürükleme **hangi referans alana** indirgenmiş? Kanat alanı mı, disk alanı mı,
   frontal alan mı? *(Bizimki kanat alanına.)* Taban farklıysa karşılaştırma
   ancak yeniden indirgenerek yapılır.
5. Bildirilen azalma **parazit sürüklemenin** mi yoksa **toplam sürüklemenin** mi
   yüzdesi?
6. Hangi uçuş koşulu: hız, Reynolds, irtifa?

**Bizimkiyle ilişki**
7. Pervanelerin süpürdüğü alan, kanat alanının yüzde kaçı?
   *(Bizde %12,7 — bu oran tutmuyorsa yüzdeler doğrudan kıyaslanamaz.)*
8. Menzil/performans kazancı hangi sözleşmeyle hesaplanmış? Sabit kütle mi,
   sabit batarya mı? *(Bizim kendi sonucumuz sözleşmeye göre tersine dönüyor;
   onlarınki hangi sözleşmede duruyor?)*
9. Geri çekme mekanizmasının **kütlesini** fiyatlamışlar mı? Fiyatlamışlarsa
   bu, §3.3'ün "yapılmamıştır" dediği ticaretin ölçülmüş tarafıdır.

**Dürüstlük denetimi**
10. Bizim hesabımızı **çürüten** bir şey var mı? Varsa önce o yazılır.

---

## 4. Yazıldığında nereye girecek

- **§3.3, Tablo 4'ten hemen sonra.** Bir paragraf, kaynakça satırı değil.
- Tartışmada, çerçeve doğrulaması olarak (Biçim B çıkarsa).
- `references.md`'ye durum kaydı: **A** (birinci elden okundu) olarak.
- `revision-list.md` §1 kapanır.

**v8 kuralı burada da geçerli:** *"bir önceki sürümde bu kaynak yoktu"* diye
yazılmaz. Kaynak, hep oradaymış gibi yerine oturur. Eksikliğin tarihi depoda
durur, makalede durmaz.
