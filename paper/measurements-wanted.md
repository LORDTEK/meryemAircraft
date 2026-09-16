# "Ölçüm" derken ne kastedildiği

Yazar haklı olarak sordu: *ne ölçümü?* Bu dosya onu somutlaştırır. Kaynağı
makalenin kendi bölümleridir; her sayı yerinden okunarak yazıldı.

**Ölçüm = fiziksel deney.** Hesap değil, simülasyon değil. Gerçek donanım, gerçek
akış, gerçek kuvvet ölçer. Makalenin bugün **hesapla** duran birkaç sayısı var;
bunlardan ikisi küçük bir rüzgâr tünelinde ölçülebilir. **Uçan bir prototip
gerekmiyor.**

---

## 1. BİRİNCİ ÖNCELİK — serbest dönen pervanenin sürüklemesi

**Makaledeki değer: C_D0 = 0,0154** (50 kg tasarım, §3.3).

Neden bu birinci:

- Sizing'in varsaydığı **toplam sıfır-kaldırma sürüklemesinin yüzde 62'si** tek başına
  bu kalem (§3.3).
- Kanat ucu çerçevelerine biçilen 0,0043'ün **üç buçuk katı.**
- Ve **menzil sonucunu üreten sayı budur** — eşit yakıt oranı sözleşmesinde
  lift+cruise'a menzil kaybetmemizin sebebi, kendi tutum pervanelerimizin serbest
  dönerken ürettiği bu sürükleme.
- Karşılaştırma için: aynı pervane **durdurulup kenarı öne alınsa** 0,0008 — yani
  **yirmi kat** fark. Makalenin en büyük kalemi, yirmi kat aralığın neresinde
  olduğumuza dair bir hesaba dayanıyor.

**Nasıl ölçülür:** bir pervane, mili serbest dönecek şekilde (şaft yükü sıfır) bir
çubuğa/kuvvet ölçere bağlanır, seyir dinamik basıncında tünelde döndürülür, ekseni
yönündeki kuvvet okunur. Aynı düzenekte mil kilitlenip kenarı öne alınarak ikinci
okuma yapılır. İstenen çıktı iki okumanın farkıdır.

**Neden Bacchini 2021 bunu bizim için yapmıyor:** o çalışma **durdurulmuş ve geri
çekilmiş** pervaneyi ölçtü. Bizimki **serbest dönen.** Aynı olgunun iki ayrı hâli.
Bu yüzden o kaynak bizim hesabımızın yerine geçmez — onu **konumlandırır**, ve bu
yüzden makaleye girmesi zaten zorunlu (bkz. `revision-list.md` §1).

**Dürüst uyarı:** katsayı boyutsuzdur ama Reynolds sayısı küçük ölçekte tutmaz.
Küçük bir tünelde alınan sayı doğrudan 0,0154'ün yerine konamaz; **hesabın fiziğini
sınar**, değerini yerine koymaz. Bunu sonuçta böyle yazmak zorundayız.

---

## 2. İKİNCİ ÖNCELİK — şeridin yatış otoritesi

**Makaledeki değer: ΔC_L ≈ 0,12** (§2.10, §4.6).

§4.6 bunu kendi ağzıyla söylüyor: yayımlanmış fence ve Gurney verileri bu değeri
*"makul kılıyor ama bu geometri için kurmuyor."* Yani ödünç alınmış bir sayı.

Neden önemli: **yatış, eşeksenli pervanelerin üretemediği tek eksendir** (§2.10).
Uçağın bütün yatış otoritesi bu şeritte. ΔC_L orada değilse uçağın yatış kumandası
yok demektir — bu, defter kalemi değil, uçabilirlik sorusudur.

**Nasıl ölçülür:** şeridi taşıyan kanat kesitinden bir parça, küçük bir tünelde,
şerit açık ve kapalı iki durumda kaldırma farkı okunur. Yarım günlük bir iş.

---

## 3. Ölçülmesi zor olan — geçiş yunuslama momenti

Highlights'ın kendi cümlesi: *"transition controllability rests on a pitching moment
no current method predicts reliably."* Bu, 1 ve 2'den farklı olarak sabit bir
düzenekte okunmuyor; dönen bir tertibat ya da serbest uçuş istiyor. **Şimdilik
kapsam dışı.**

---

## 4. Neden yapılmalı — sıra önemli

Bunu dergi istediği için değil, **makalenin en büyük sayısı bugüne kadar hiçbir
teraziye konmadığı için** yapıyoruz. Dergi yararı arkadan gelen bir sonuçtur:

- *Drones*'un yazılı laboratuvar-ölçeği şartı karşılanır ve o kapı yeniden açılır.
- *Journal of Aircraft* ve *Aerospace Science and Technology*'de hakem aşaması
  maddeten güçlenir — "bunu ne doğruluyor" sorusunun bir cevabı olur.
- Ve makalenin kendi açık maddesi kapanır.

**Gereken tesis:** kuvvet ölçerli küçük bir ses altı rüzgâr tüneli. Havacılık
bölümü olan üniversitelerde bulunur. Uçan demonstratör, pist, izin, sigorta —
hiçbiri bu iki ölçüm için gerekli değil.
