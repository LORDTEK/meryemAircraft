# Bir sonraki dış görüş metnine MUTLAKA girecekler

*(Bu dosya taslak deposudur; metin yazılırken buradan derlenecek.)*

## 1. CFD — geri alınan yorum ve yerine geçen ölçüt

- **Geri alındı:** "kararlı RANS iki ayrı durağan çözüme oturuyor."
  Delilin taşıdığından fazlaydı.
- Ayrılma topolojisi **birebir aynı**: %0,02 ters akış alanı, aynı x
  aralığı (1,003–1,740 m) — iki vakada da.
- Basınç farkı açıklık boyunca **düzgün dağılmış** (sekiz bandın her
  biri farkın ~1/8'i), yerel değil.
- **Simetri ölçütü:** simetrik NACA 00xx, burulma yok, α=0 → C_L = 0
  olmalı. bl_C = 1,45e−03; bl_E = 1,35e−04. bl_E **10,8 kat** daha
  yakın. Cp'de üst/alt asimetri: bl_C 0,0249, bl_E 0,0011 (her
  istasyonda ~10 kat).
- Asimetrinin indüklenen sürüklemesi ihmal edilebilir (≈1,1e−07,
  C_D'nin milyonda 9'u) → **sebep değil, belirti**.
- **Yeni ifade:** iki çözüm eşit değerde değil; bl_E daha iyi
  koşullanmış. Aralık (0,01201–0,01253) yine yazılıyor ama tek değer
  gerekirse bl_E, **artığa göre değil fiziğe göre** seçiliyor.
- Bu, YZ1 ("üçüncü başlangıç gerekmez") ile YZ3 ("gerekir")
  ayrışmasını çözdü: üçüncü koşu yerine simetri ölçütü karar verdi.
- **Sorulacak:** simetri ölçütü meşru mu? Ağ üst/alt simetrik değilse
  her iki vaka da eşit etkilenirdi — bu savunma yeterli mi?

## 2. Temel model — YZ3'ün bulduğu sözleşme sorunu

- Sabit yakıt kesri **kütle faturasını menzilden siliyor**.
- Üç sözleşme uygulandı; C'ye ×1,00 hediyesi hâlâ dururken:

  | | sabit kesir | sabit yakıt kütlesi | sabit MTOW+faydalı |
  |---|---|---|---|
  | B | −%14,4 | −%36,5 | −%72,6 |
  | C | +%12,0 | +%0,2 | −%19,1 |

- L/D çarpanıyla çapraz: 12 kutunun 3'ünde C önde, üçü de birinci
  sütunda.
- **YZ3'ün düzeltilen sayısı:** sabit yakıt kütlesinde elle −%7 demiş;
  60,3 kg'ı (sabit KESİR MTOW'u) kullanmış. Yakıt sabitlenince C'nin
  MTOW'u 55,9'a kapanıyor → model **+%0,2**. Sabit MTOW'da YZ3 tam
  tutuyor: −%19 / −%19,1, f_yakıt 0,116 / 0,116.
- **Sorulacak:** üç sözleşmeden hangisi Q1 için "ana" tablo olmalı?
  Yoksa üçü de eşit ağırlıkta mı verilmeli?

## 3. Ölçülmüş ve çürütülen küçük iddialar

- η_seyir menzile **etki etmiyor** (R formülünde yok) — YZ5'in "ikinci
  hediye" tespiti yalnızca kütle sütununda geçerli.
- B'nin yapısal cezası menzili değiştirmiyor, MTOW'u 86→117 kg yapıyor.
- Çift sayım **yok** (YZ1 §17 ve YZ3 §5.2 kontrol edildi).
- Motor derecelendirme payı: tam ayarsız ağır hatta motor **+%16,9**
  sapıyor, menzil −%0,1, L/D %0,0.

## 4. Yapılan makale değişiklikleri

- Başlık: "Eliminating" → **"Reducing"**.
- Yeni **§5.5** (karşılaştırmalı boyutlandırma, üç sözleşme).
- Yeni **§8.12** (koşulluluk: ölçülmemiş çarpan **ve** sözleşme).
- Yeni **§8.13** (motor payı tutarsızlığı).
- §6.6 ve §8 yeniden yazıldı (başlangıç yayılımı + simetri ölçütü).
- Özete karşılaştırma ve "tilt ailesine üstünlük iddia edilmiyor".

## 5. Şu an yapılan iş

**Bileşen düzeyinde kütle bütçesi.** Üç denetim de listeledi; YZ3 Q1
için zorunlu saydı. Sonucu bir sonraki metnin ana gövdesi olacak.

---

## 6. DİĞER YZ'LERE SORULACAK — açık kalan kaynak soruları (09.09.2026)

### ⚠️ S1. inviscid → Oswald açıklık verimi oranı (0,85–0,90)

**Neden önemli:** §6.6 bu oranı **kaynaksız** kullanıyor ve şu an bir
**başlık sayısı** ona bağlı. Denge için gereken 9° burulma, iskoz olmayan
açıklık verimini 0,99'dan 0,865'e düşürdü. Aynı oranla:

| | inviscid | ima edilen Oswald | varsayılan 0,85 |
|---|---|---|---|
| burulmasız | 0,99 | 0,84–0,89 | içinde → temkinli |
| **burulmalı** | **0,865** | **0,735–0,78** | **üstünde → iyimser** |

Doğruysa seyir L/D 12,04 → **11,4–11,7**, menzil **%3–5** düşüyor
(1598 → ~1520–1550 km).

**Sorulacak:** Bu oran için **birincil bir kaynak** var mı? Ya da doğrudan
kuyruksuz/BWB bir kanat için ölçülmüş **Oswald** verimi? Alternatif olarak:
burulmalı kanadın iskoz hesabı olmadan bu soruyu kapatmanın savunulabilir
bir yolu var mı, yoksa menzil sayıları "koşullu" mu yazılmalı?

**Şu an metinde ne yazıyor:** düzeltme **yapılmadı**. Kaynaksız bir oranı
başlık sayısına yaymak, belirtilmiş bir varsayımı belirtilmemişle
değiştirmek olurdu. Yazılan şey yapısal nokta: varsayım artık bir hesapla
**üstten sınırlı değil.**

### 🔎 S1 KISMEN KAPANDI (09.09.2026 akşamı) — sonuç orandan bağımsız

Traub 2024 hem **inviscid** (AVL) hem **ölçülmüş** Oswald faktörü veriyor.
Kp'lerinden türettim (AR = 3):

| | ölçülen e | inviscid e | oran |
|---|---|---|---|
| düz (planar) | 0,947 | 1,001 | **0,946** |
| dairesel | 1,220 | 1,206 | 1,011 |
| köşegen | 1,179 | 1,105 | 1,067 |

İkisi 1'in **üstünde** — gerçek bir kanatta olamaz; duvar düzeltmesi
uygulanmamış bir tünel ölçümünü inviscid hesapla karşılaştırmanın
artefaktı. Yani bu veri oranı **sabitlemiyor**, gevşek sınırlıyor.

**Ama sonucun işareti bütün bantta ayakta:**

| oran | ima edilen Oswald e | seyir L/D | 12,04'e göre |
|---|---|---|---|
| 0,85 | 0,735 | 11,44 | −%5,0 |
| 0,90 | 0,778 | 11,68 | −%3,0 |
| 0,95 | 0,822 | 11,90 | −%1,2 |

**1'in altındaki her oran için** — yani iskozitesi olan her kanat için —
burulmalı açıklık verimi 0,85'in altında ve seyir L/D 12,04'ün altında.
Yalnızca **büyüklüğü** açık: %1–5.

Dolayısıyla YZ'lere sorulacak soru daraldı: *oranı bilmemize gerek yok,
burulmalı kanadın **iskoz hesabı** lazım.* Bir de: 0,85 varsayımı
konvansiyonel (Ugwueze 2023 de AR 7,0'da aynı değeri kullanıyor), yani
dikkatsizlik değil — bu yüzden bu kadar uzun süre sorgulanmadan kaldı.

### ✅ S1 ARTIK YZ'LERE SORULMAYACAK — kendimiz hesaplayacağız (12.09.2026)

Şugar Gabor & Botez'in doğrusal-olmayan VLM'ini okuyunca anlaşıldı ki
aradığımız "iskoz hesabı" bir araç sorunu değil. Yöntem: her açıklık şeridinde
2-B ağdalı çözüm, sonuç 3-B girdap halkalarıyla eşleniyor;
C_D = C_Di + (1/S)∫c_d(y)c(y)dy. Doğrulama dC_L/dα'da %0,51, maliyet CFD'nin
%1'i.

**Ve bileşenlerin hepsi bizde zaten var:** `vlm.py` burulmuş kanadın açıklık
yükünü veriyor, `cd0.py` NeuralFoil'i şerit şerit çağırıyor. Tek eksik,
`cd0.py`'nin kesit direncini **sıfır kaldırmada** okuması — burulmuş kanadın
**yerel C_l'inde** okumuyor.

Yani S1 bir kaynak sorusu değil, **yapılmamış bir hesap.** YZ'lerden bunun
için kaynak istemeyeceğiz. Kaynak okuması bitince yapılacak işler listesinin
başında.

⚠️ Onlara yine de sorulacak **tek** şey kalıyor, ve o bir yöntem sorusu:
NeuralFoil/XFOIL sınıfı bir 2-B çözücüyü burulmuş bir kanadın yerel C_l'inde
çağırıp profil direncini toplamak, **ok açılı** bir kanatta ne kadar
güvenilir? (Şerit kuramı ok açısını ihmal eder; bizim kök ok açımız büyük.)
Ok açısı düzeltmesi olarak ne kullanılıyor — cos yasası mı, yoksa akıma dik
kesit mi?

### S2. Şeridin yükseklik yasası — takas kapatılmadı

Sabit h/c seyirde sürüklemeyi %64 azaltıyor ama izdeki alanı %45
azaltıyor. Hangi mekanizmanın **asılı durumda** baskın olduğu belirlenmedi.

### S3. Uç çerçevesi fairing'inin toe açısı — BÜYÜKLÜK ve İŞARET KAPANDI

NACA TR-796: yüksek en-boy oranlı finler toe-out ister, düşük olanlar toe-in;
ve toe-out'ta arka fin perdövitese girerse **kararsızlaştırıcı** moment doğuyor.

**Büyüklük ölçülmüş (NASA TM-78767, 09.09.2026):** uç podlarında dikey kuyruk
taşıyan kuyruksuz ok kanatlı bir kargo konfigürasyonunda, (L/D)max için
**optimum toe açısı ~1,5°** (simetrik kesitli kuyruklar). Yani açı **bir-iki
derece mertebesinde**, on derece değil. Ve aynı testler L/D'nin üç kuyruk
tasarımında da "about the same" olduğunu buluyor, **%75 daha büyük alana
rağmen** — bizim "gereken veter zaten olması gerekenin içinde" argümanımızın
ölçümle gelen hâli.

### ✅ S3'ÜN İŞARETİ KAPANDI (12.09.2026) — soru yerini daha kötü bir soruya bıraktı

TR-796'yı baştan sona okuyunca, "her iki kaynağın da aralığının dışındayız"
gerekçesi **çürüdü.** Kural bir korelasyon değil, *hangi kuvvetin iş yaptığına*
dair bir ifade:

> düşük AR → toe-**in**, çünkü stabilize edici moment o yüzeylerin taşıdığı
> **büyük endüklenen dirençten** doğuyor;
> orta/yüksek AR → toe-**out**, çünkü moment **"the outwardly directed lift"**ten
> doğuyor.

AR'ı yükseltmek dengeyi dirençten taşımaya doğru **daha da** kaydırır. Yani
AR ~20 kuralı aşmıyor, kuralı **güçlendiriyor.** İşaret: **toe-out.**
Makaleye bu gerekçeyle yazıldı; eski "işaret açık" ifadesi kaldırıldı.

**Yerine geçen soru daha sert, ve YZ'lere bu sorulacak.** Fairing veteri 39 mm,
seyirde **Re ≈ 80.000.** Varsaydığımız a_f = 4/rad hiçbir Reynolds'ta ölçüm
değil, bu Reynolds'ta ise iyimser. Ve Selig'in derlemesi tam bu bandı vuruyor:
Princeton'da denenen dört simetrik kesidin (J5012, NACA 0009, NACA 64A010,
SD8020) hepsi α ≈ 0 civarında doğrusalsızlık gösteriyor; Mueller & Batill'in
NACA 66₃-018'inde taşıma eğrisinin eğimi **3°'lik bir bantta işaret
değiştiriyor** — bizim toe açımız 1,5°, yani tam o bandın içinde.

**SORU:** Re ≈ 10⁵ mertebesinde, veter uzunluğu on milimetrelerce olan ince
simetrik bir fin, 1–2°'lik sabit toe açısında beklenen yan kuvveti üretir mi?
Bu Reynolds'ta ölçülmüş bir C_y_β / a_f değeri var mı? (Aradığımız, "düşük Re
kötüdür" genellemesi değil; **sayı.**)

**İKİNCİ SORU (arıza kipi):** toe-out'ta arka fin perdövitese girdiğinde
kararsızlaştırıcı moment doğuyor. Bu, kullanılabilir yan kayma zarfına bir üst
sınır koyar. Bu sınırın hesaplandığı ya da ölçüldüğü bir çalışma var mı?

### 🔴 S4. Refleks kesitlerin gerçek C_m0 mertebesi — EN ÖNEMLİ AÇIK SORU

**Neden bu kadar önemli:** denge zincirinin tamamı buna bağlı. VLM taramasından
C_m derece başına 0,00629; kesit ne verirse burulma gerisini tamamlıyor:

| kesit C_m0 | gereken burulma | inviscid e | seyir L/D |
|---|---|---|---|
| 0 | 9,2° | 0,865 | 11,68 |
| **0,004 (elimizdeki tek ölçüm)** | **8,6°** | 0,875 | 11,73 |
| 0,020 | 6,0° | 0,937 | **12,01** |
| 0,050 | 1,3° | 0,986 | 12,21 |

Yani **0,02 veren bir kesit varsa, denge cezası neredeyse tamamen geri
kazanılıyor** ve §5.4'ün beşinci defter kalemi (%4,3) büyük ölçüde siliniyor.

**Elimizdeki kanıt tek bir sayı:** NACA TR-460'ın ölçtüğü 2R212 → **+0,004**.
1933 tarihli. Makalede bunun seçimi taşıdığı açıkça yazılı.

**Sorulacak — açıkça bu biçimde:** Elimizdeki tek ölçüm **1933 tarihli**
(NACA TR-460). Sayı sağlam, ama bir hakem *"doksan yıllık bir rapordan başka
dayanağınız yok mu?"* diye sorar ve haklı olur. **Aynı şeyi söyleyen daha
güncel, daha yerleşik, daha çok atıf alan bir yayın var mı?**

Aranan: refleks bir kesit için **ölçülmüş** (tercihen rüzgâr tüneli) C_m0,
kesit adıyla ve koşullarıyla. XFOIL/XFLR5 poları da kabul, ama kaynağı,
Reynolds'u ve doğrulaması belli olmalı. TR-460'ı **değiştirmek** değil,
**yanına koymak** istiyoruz — eski ölçüm sağlam, yalnız yalnız kalmasın.

⚠️ **Kullanmadığımız bir kaynak — ve nedeni.** Shinde 2020 (*Micromachines*
11(6):553) on refleks kesit için C_m0 tablosu veriyor, hepsi **10⁻⁴** ve hepsi
**negatif**. Ama aynı makale iki sayfa önce *"C_m0 must be positive"* diyor.
Kendi içinde tutarsız, ve gerçek refleks kesitlerin C_m0'ı standart
kaynaklarda 10⁻³–10⁻² anılır. **Bu tablodan hiçbir sayı alınmadı**; kaynak
yalnızca (a) denge gereksiniminin ifadesi ve (b) pratik kesit ailesinin listesi
için anılıyor. Uzlaştıramadığımız bir büyüklüğü aktarmayız.

**YZ'lere sorulacak ek soru:** Shinde'nin tablosu gerçekten hatalı mı, yoksa
bizim okumadığımız bir normalizasyon/işaret kuralı mı var?

⚠️ **Selig UIUC'yi bizim adımıza aramayın — baktık, cevap orada yok.**
*Low-Speed Airfoil Data* Cilt 1–2 (düşük Re kesit verisinin en çok atıf alan
deneysel derlemesi) momenti **ölçmüyor.** Kendi ifadesi: *"the current setup
does not provide pitching moment data, airfoil moment coefficients have been
determined computationally using either the Eppler, ISES or XFOIL code."*
Tablo 3.1'in tamamı hesaplanmış değerdir.

Ve oradan çıkan sayı **aleyhimize:** derlemedeki tek uçan-kanat kesiti olan
**MH45** (Repperle, hafif refleks, %9,84 kalınlık) → **C_m,c/4 = −0,006.**
Shinde'nin (hepsi negatif) tablosuyla aynı yöne bakıyor. Yani artık *iki*
bağımsız kaynakta uçan-kanat/refleks kesitlerinin C_m,c/4'ü negatif çıkıyor ve
pozitif C_m0 varsayımı yalnız TR-460'a dayanıyor.

Tek pozitif değer refleksten değil kısıtlı tasarımdan geliyor: **M06-13-128**
(Miley, %5,16 kamburluk) → **+0,004**, *"c_lmax near 1.5... in light of the low
pitching-moment constraint."* Bu, aradığımız takasın var olduğunu gösteriyor
ama yine hesaplanmış bir sayı.

**Dolayısıyla soruyu şöyle daraltıyoruz:** *momenti gerçekten ölçen* bir
tünelde (NACA/NASA, Delft, Stuttgart tipi) alınmış, refleks veya düşük-moment
kısıtıyla tasarlanmış bir kesidin C_m,c/4'ü — kesit adı, Reynolds ve tünel
belirtilerek. Hesaplanmış (XFOIL/Eppler/ISES) değer **ikinci sınıf kanıt**
sayılacak, ve bunu kabul ediyorsak da kaynağında hesap olduğu yazılacak.

### S5. Kısa süreli, güç için optimize edilmiş tampon — ölçülmüş özgül güç?

Tampon **4,6 kW/kg** istiyor. Okuduğumuz tek kaynak (Bacchini & Cestino 2019)
güç uygulamaları için **paket düzeyinde 700–1300 W/kg** veriyor. Bandın üst
ucunda tampon 1,8 kg yerine **6,4 kg** olur ve hafif hattın bütçesi kapanmaz.

Güç **zemin**, geçici değil: T ~ P^(2/3) olduğu için 1,3 kW/kg'de T/W = 0,71
çıkıyor, uçak yerden kalkmıyor. Enerji tarafı ise rahat (20 s'lik kalkışta
tamponun %14–32'si).

**Sorulacak:** Bir dakika boşalan, **güç için optimize edilmiş** bir tampon için
(otomotiv traksiyon paketi değil) **ölçülmüş** özgül güç veren bir kaynak var mı?
Hücre düzeyi kabul, ama paket cezası (kasa, bağlantı, termal) ayrıca sorulmalı.

### S6. "Kumanda yüzeyi yok" iddiasının sınırı

Tasarımcı belirtti: yatış şeridinin **çıkma miktarı sürekli**, aç-kapa değil.
Metin düzeltildi. Ama bu, şeridi kumanda yüzeylerinden ayıran cümleyi
("aç-kapa, orantılı bir kumanda yüzeyi değil") ortadan kaldırdı.

**Sorulacak:** Sürekli çıkışlı bir alt-yüzey spoiler'ı varken "no control
surfaces" konumlandırması savunulabilir mi, yoksa iddia "no elevons, no rudder,
no hinged surfaces — one variable-extension strip" biçiminde mi kurulmalı?
Hakem buradan girer mi?

### S7. Kabuk yüzey yoğunluğu (1,5 kg/m²) — ELİMİZDEKİ 35 KAYNAKTA YOK

Otuz beş PDF'in tamamını "kg/m2", "areal density", "structural mass fraction",
"empty weight fraction" için taradım: **hiçbirinde yok.** Yani hafif hattın
kütle bütçesinin dayandığı sayı için elimizde hâlâ tek bir kaynak bile yok.

**Sorulacak:** Kompozit bir İHA gövde/kanat kabuğu için **ölçülmüş** yüzey
yoğunluğu (kg/m²) veren bir kaynak var mı? Başabaş 1,78 kg/m²; varsayılan 1,5.
Ayrıca: bu büyüklük ölçekle nasıl gidiyor (ağır hattın kapanmamasının sebebi
tam olarak bu bilinmiyor).

### S8. Şeridin türbülansta ve perdövites sonrasında zayıflaması

Yang 2020: Gurney flap *"became less effective after stall angle"*, ve %19
türbülans yoğunluğunda fayda *"negligible"* (%10,5'te hâlâ +%2,7…+%14,4 L/D).

**Bizim için ikisi de kritik:** (a) geçiş, dış kanadın perdövites sonrasında
olduğu açılardan geçiyor; (b) şeridin iç kısmı **kasten** pervane izinde, ve iz
düşük türbülanslı bir ortam değil. Yani §4.4'ün "izde olduğu için sıfır hızda
çalışır" avantajı, mekanizmanın en zayıf çalıştığı yer olabilir.

**Sorulacak:** Pervane izi içindeki bir Gurney/çit cihazının etkinliğini ölçen
bir çalışma var mı? İz türbülans yoğunluğu tipik olarak ne mertebede?

### S9. İki yönlü şerit — tek yönlü çıkıntının yunuslama cezası (12.09.2026)

NACA TR-796, kuyruksuz uçaklarda spoiler'ın aileron olarak kullanımı için şunu
söylüyor:

> *"If only **upgoing** spoiler projections are used, the pitching moments
> developed are **prohibitive.** A spoiler arrangement employing **equal up and
> down projections** would improve this condition but the data available are
> insufficient for evaluating conclusively the merits of such a system."*

Bizim şerit tek yönlü (yalnız alt yüzey). §4.4'te hesapladığımız kuplaj
ΔC_m 0,005–0,032 ve bunu **çizelgeleme kısıtıyla** çözdük (dönüşün sonunda
şerit kullanılmayacak). 1944'ün önerdiği yapısal çözümü ise hiç incelemedik.

**Sorulacak:** 1944'ten bu yana iki yönlü (eşit yukarı+aşağı) çıkıntılı
spoiler/şerit düzeni ölçülmüş mü? Yunuslama kuplajını gerçekten götürüyor mu,
ve yatış otoritesinden ne kadar götürüyor? Bir de: bizim gibi **alt yüzeyde,
45° planform ok açısıyla** duran bir şerit için üst yüzeyden simetrik bir
ikizini çıkarmak, yatış momentlerini gerçekten toplar mı yoksa birbirini yer
mi? (Üstteki şerit ters işaretli ΔC_L üretir; toplanması gerekenin işareti
bizde net değil.)

⚠️ Not: kullanıcının tasarım kararı tek şerit ve sürekli açılım. Bu soru o
kararı değiştirme önerisi değil, **§8'e yazılmış incelenmemiş alternatifin**
kapatılması için.

### S10. Ölü bandın altı — küçük yatış düzeltmeleri nasıl yapılacak?

TR-796'nın ölçümü: **0,01 veterden alçak çıkıntılar taşımada "negligible"
değişiklik veriyor** (iki ayrı model). Şerit konik olduğu için bu, kumanda
kursunun altından kademeli bir ölü bant kesiyor — `yatis.py:esik_istasyonu()`:

| kumanda kesri | üretilen moment / tam |
|---:|---:|
| 0,05 | 0,000 |
| 0,10 | 0,041 |
| 0,15 | 0,113 |
| 0,25 | 0,237 |
| ≥ 0,25 | doğrusaldan %5 içinde |

Yani şerit **büyük komutlarda doğrusal, küçük komutlarda kör.** Bu, eşik
cihazlarında alışılmışın tersi (genelde büyük komutlar doyar, küçükler
çalışır) ve koniklikten geliyor.

**Sorulacak:** Ölü bandı kapatmanın bilinen yolları neler? (Dither, iki
kademeli açılım, kök tarafında daha yüksek bir başlangıç profili, ya da küçük
düzeltmeleri tamamen diferansiyel itkiye bırakmak.) Uçuş kontrolünde bu
sınıftan bir cihazla küçük genlikli düzeltme yapılmış örnek var mı?

### 🎯 S11. İKİ ADLI HEDEF — bunları bulmalarını isteyeceğiz (12.09.2026)

Bu ikisi belirsiz bir "kaynak arayın" isteği değil; **tam künyeleriyle** iki
yayın. YZ'lerden indirilebilir bağlantı istiyoruz.

**(a) En büyük açık kalemimize doğrudan bakan kaynak:**

> **Olsson, C.; Verling, S. L.; Stastny, T.; ve diğ. "Full envelope system
> identification of a VTOL tailsitter UAV." AIAA 2021-1054.**

Neden: §8'in 3. maddesi, geçiş boyunca **yunuslama momentini** istiyor —
22°'ye kadar, düşük dinamik basınçta. Bu makale, gerçek bir kuyruk-oturur
İHA'nın (WingtraOne) **tüm uçuş zarfında** aerodinamik katsayılarını **uçuş
verisinden** tanımlıyor. Zhong 2023 bunu *"the model was well suited for
predicting the forces and moments"* diye anıyor. Eğer C_m(α) eğrisi bu
makalede varsa, alanın bizim aradığımız şeye en çok yaklaşmış ölçümüdür.

**(b) Dikey uçuş için kesit/konfigürasyon aerodinamiği:**

> **Shkarayev, S.; Moschetta, J.-M.; Bataille, B. "Aerodynamic design of micro
> air vehicles for vertical flight." *Journal of Aircraft* 2008; 45(5):
> 1715–1724.**

Neden: dikey uçuş için tasarlanmış araçların aerodinamiği; yüksek α verisi
içermesi muhtemel.

**İstenen:** PDF bağlantısı, ya da en azından C_m(α) verisinin hangi
şekil/tabloda olduğu ve hangi α aralığını kapsadığı.

### 📌 S4 için ek hedef (aynı kaynaktan)

Lampropoulos 2025 (*Fluids* 10(54)) bir BWB'yi **refleksi tasarım değişkeni
yaparak** (NACA2412'nin arka kamber çizgisi yukarı bükülüyor, seviye 1–5)
ve yalnızca **2,44° burulmayla** dengeliyor. Ama **hiçbir yerde o reflekslerin
C_m0'ını vermiyor.**

**Sorulacak:** Refleks seviyesi parametrelenmiş kesitler için C_m0 değeri
yayımlanmış mı? Yani "arka kamberi şu kadar bükersen C_m0 şu olur" diyen bir
kaynak? Bu, S4'ün tablosunu (C_m0 = 0,004 → 0,050 arası) gerçek kesitlerle
doldurmamızı sağlar.

---

# TUR 13 SONUCU — üç soru kapandı, biri kapanmadı, biri kötüleşti (12.09.2026)

YZ1/YZ3/YZ5/YZ6'nın verdiği bağlantılardan indirilen 19 dosyanın hepsi açıldı.
Üçü mükerrer, biri iddia edilen kaynak değildi. Aşağısı geri kalanın sonucu.

## ✅ S1 CEVAPLANDI — kendimiz hesapladık

`aero/iskoz.py` yazıldı: VLM panel kuvvetlerinden her açıklık şeridinin yerel
c_l'i çıkarılıyor, NeuralFoil o şeridin **kendi c_l'inde** çağrılıyor, profil
direnci integre ediliyor. Şerit ayrıştırması çözücünün C_L'ini altı hanede
yeniden üretiyor (denetim modülün içinde).

⚠️ **Ve bu hesap yaparken bir kategori hatasına düştüm, kendim yakaladım,
kayda geçsin:** e = C_L²/(πAR·C_Di) formülü **yalnızca burulmasız** kanatta
geçerli. Burulmuş kanatta induklenen sürükleme C_L = 0'da sıfır değil, ve en
küçük değerini sıfırdan farklı bir C_L'de alıyor. İlk koşumda bu formül
C_L = 0,03'te e = 0,024 verdi, ve parabol-uydurma e'si ile nokta e'sini
bölünce **1,08** — yani "Oswald > inviscid" — gibi fiziksel olmayan bir oran
çıktı. Oran anlamsızdı, sonuç değil. Doğru tanım makaleyle tutarlı **nokta**
tanımıdır ve modülde artık o kullanılıyor. (Bu, daha önce yaptığım
inviscid/Oswald kategori hatasının aynı ailesinden.)

**YZ'lere artık sorulmayacak.** Yalnız bir yöntem sorusu kaldı, aşağıda.

## 🔴 S4 KAPANDI — ve bizim ALEYHİMİZE

Aradığımız şey buydu: refleks bir kesit için, momenti gerçekten ölçen bir
tünelde alınmış C_m0. **Geldi, ve umduğumuzun tersini söylüyor.**

| kesit | C_m,c/4 (ölçülmüş) | kaynak |
|---|---:|---|
| **NACA 2R212** | **+0,004** | TR-460 |
| B106R / N60R / NACA M6 | −0,001 | **TN-388** (VDT, Re 3,1×10⁶) |
| Gött. 398R | −0,007 | TN-388 |
| 4409R / 4412R / 4415R / 4418R | −0,025 / −0,030 / −0,031 / −0,030 | **4400R WR** |

TN-388'in refleks kesitleri, orta kamber çizgisi ince kanat kuramından
**sıfır** moment verecek şekilde tasarlanmış ve ölçüm *"practically zero"*
diyor. 4400R serisinin tasarım hedefi zaten **−0,03**, ve rapor *"the design
pitching-moment coefficient was realized"* diyor.

**Dokuz ölçülmüş kesit, yalnız biri pozitif.** Refleks, yapılıp ölçüldüğü
hâliyle, negatif momenti **gidermek** için bir araç; pozitif moment
**üretmek** için değil. Bize gereken +0,056.

İki maliyet de ölçülmüş: C_Lmax **%12** (TN-388) ve **%10** (4400R) düşüyor —
ve C_Lmax, kuyruk-oturur bir uçağın geçişte en çok ihtiyaç duyduğu şey.

**Bu bizi güçlendiriyor:** burulma artık iki seçenekten biri değil, ölçülmüş
dayanağı olan **tek** seçenek.

**Bundan sonra S4 için kaynak ARAMAYIN.** Kapandı.

## 🔴 S5 KÖTÜLEŞTİ — ve bir YZ okuması yanlıştı

**Yu ve diğ. 2025** (*Batteries* 12(9):317): 24S NCM paket, tasarlanmış,
üretilmiş, VS-210 eVTOL'da **uçurulmuş**. Ölçülmüş paket düzeyi özgül güç
**724 W/kg** (5C sürekli) ve **892 W/kg**; 10,68C'de ≈**1,5 kW/kg**, ve orada
paket 55,1 °C — 60 °C sınırına 4,9 °C pay.

Bu, "otomotiv paketi bizim ürünümüz değil" savunmamızı bitiriyor: **bu kaynak
tam bizim ürünümüz.** 1,5 kW/kg'da tampon 1,8 kg yerine **5,5 kg**; payımız
2,2 kg, açık 3,7 kg. **Hafif hattın bütçesi kapanmıyor.**

⚠️ **YZ1'e:** NASA NIAC raporunu *"4,6 kW/kg artık tamamen hayal değil"*
gerekçesiyle verdiniz. Raporu açtık; **tam tersini söylüyor:**

> *"the specific power (4 kW/kg) is about **twice that of existing
> batteries**."*

Yani o 4 kW/kg bir **gelecek teknoloji varsayımı** ve rapor bunu açıkça
yazıyor. Bizim lehimize değil, aleyhimize **üçüncü** bağımsız ifade. Lütfen
bundan sonra sayıyı bağlamıyla birlikte verin — bu haliyle makaleye yanlış
bir savunma girecekti.

## ❌ S9 KAPANMADI — NACA 1034 bu soruyu cevaplamıyor

YZ1 *"Two-sided spoiler: NACA 1034 yeterli, artık kapatılabilir"* dedi.
Raporu açtık: **kapatmıyor.** TR-1034, spoiler aileron'ların **hız freni /
süzülme yolu denetimi** olarak kullanımını ölçüyor — yani **iki kanatta
birden simetrik** açılım. Bizim sorumuz **tek kanatta üst+alt** eşit çıkıntı
(TR-796'nın önerdiği düzen). O düzen bu raporda yok.

**Soru aynen duruyor:** 1944'ten bu yana, tek bir kanat yarısında üst ve alt
yüzeyden eşit çıkıntı yapan bir spoiler/şerit düzeni ölçülmüş mü?

(TR-1034 yine de işe yaradı: simetrik açılımda yunuslama etkisi küçük ve
yatış otoritesi bozulmuyor — yani şerit aynı anda bir alçalma yolu denetimi.
Makaleye üçüncü rol olarak eklendi.)

## 🟡 S3'ün ardılı — hâlâ açık, ve en iyi cevap YZ5'ten geldi

39 mm veterli fin, Re ≈ 80.000. YZ5 mertebe verdi (düşük Re'de ince simetrik
kesitlerde C_lα *"3,0–3,5 rad⁻¹ civarına düşer"*) ve Lissaman 1983'ü
gösterdi. Bu bir **mertebe**, bizim istediğimiz **ölçüm** değil, ama yönü
doğruluyor: varsaydığımız 4,0 rad⁻¹ iyimser.

**Hâlâ aranıyor:** Re ≈ 10⁵'te, on milimetrelerce veterli ince simetrik bir
fin için **ölçülmüş** C_lα veya yan kuvvet türevi.

## 🟢 S7 — ilerledi ama kapanmadı

YZ1'in verdiği iki kaynak indirildi: Pollet'in ISAE-SUPAERO tezi (İHA
boyutlandırmada açık yüzey yoğunluğu varsayımları) ve Juno Composites'in
imalatçı verisi (1,4–1,6 kg/m²). İkincisi **imalatçı iddiası**, hakemli
ölçüm değil. 1,5 kg/m² artık "literatürde karşılıksız" değil, ama hâlâ
**varsayım**.

## ➕ YENİ — tek kalan yöntem sorusu

Şerit kuramıyla profil direnci integre ederken ok açısı (kökte 45°) nasıl
ele alınmalı? İki seçeneği de hesapladık ve aralarında **iki kat** fark
çıktı (C_Dp 0,01303 akım yönlü, 0,00623 basit-ok). Bu bir belirsizlik değil,
basit-ok kuramının **sürtünmeye uygulanamayacağının** işareti gibi duruyor:
basınç alanı ok çizgisine dik bileşenle kurulur ama sürtünme yüzeyin
üzerinden V ile akar, V·cosΛ ile değil.

YZ5 ve YZ1 de aynı yöne işaret etti. **Sorumuz:** bu gerekçeyi doğrudan
söyleyen, atıf yapılabilir bir kaynak var mı? (Ders kitabı düzeyi yeterli —
Drela, Katz & Plotkin, Torenbeek, DATCOM.)
