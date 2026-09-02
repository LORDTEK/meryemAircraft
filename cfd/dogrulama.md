# Doğrulama — çözücü gerçeği veriyor mu?

Bu dosya `cfd/README.md`'deki **denetimden** ayrıdır ve ayrı kalmalıdır.
Denetim, çözümün kendi içinde tutarlı ve çözünürlükten bağımsız olduğunu
gösterir. Doğrulama, çözümün **gerçeği** verip vermediğini gösterir.
İkincisi olmadan "çözücümüz doğrulandı" denemez.

Kaynaklar `cfd/kaynak/` altındadır ve depoya girmiştir. Sayılar
`cfd/veri/referans.py`'de, her birinin yanında nereden ve **nasıl**
okunduğu yazılı olarak durur.

## ÖZET — şu anki durum

Bu dosya kronolojik yazıldı: hipotezler kurulduğu sırayla, çürütülenler
çürütüldüğü yerde duruyor. Okuyanın 750 satır izlemesi gerekmesin diye
varılan yer burada:

**Doğrulanan.** Spalart–Allmaras kurulumumuz iki bağımsız vakada, iki
bağımsız referans kodla (Overflow, Cfl3d), **profil düzeyinde**
doğrulandı:

| vaka | ölçülen | sonuç |
|---|---|---|
| sıfır gradyanlı düz levha, Re_θ = 10⁴ | u⁺(y⁺) | ±0,06 u⁺ içinde |
| NACA 0012, Re = 6×10⁶, α = 0 | üst yüzey C_f | 91 yüzün %91'i iki kodun **arasında**, azami sapma %0,36 |

Karşılaştırma için: iki referans kod kendi aralarında ortalama %2,33
ayrılıyor. Ayrıca SA'nın ağ yakınsama yörüngesi Overflow'unkini izliyor
(en ince ağlarda %0,3).

Bu, ağı, şemaları, çözücü kurulumunu, u_τ çıkarımını ve kuvvet
integralini birlikte doğrular — hepsi SST ile ortaktır.

**Doğrulanmayan.** k-ω SST kurulumumuzda **gerçek ve ölçülmüş bir kusur**
var. Aynı ağda, aynı boru hattıyla:

| | kodlar arasında kalan yüz | azami sapma |
|---|---:|---:|
| bizim SA | %91 | %0,36 |
| bizim SST | **%0** | **%7,6** |

Düz levhada da aynı imza: +0,53 u⁺ kayma, her y⁺'ta.

**Elenenler** (tahminle değil, ölçülerek): serbest akış türbülansı (1000
kat), ağ (profilde üç, levhada iki kademe), duvar ω koşulu (iki onlu),
k duvar koşulu, a₁ sınırlayıcısı, SST'ye özgü makine (düz kOmega da
etkileniyor), ayrışım şemaları (beş varyant), geometri (%0,3),
Re_θ eşleştirme yordamı (şekil faktörü denetimi), yakınsama
(4× uzun koşu, altı basamağa kadar aynı).

**Kaynaktan okunan.** Koştuğumuz ikilinin tam kaynağı çekildi
(`apt-get source openfoam`). kOmega ve kOmegaSST ders kitabı biçiminde;
katsayılar standart ve log tabakası bağıntısını κ ≈ 0,41 ile sağlıyor.

**Bulunamayan: nedeni.** Ayarla referans bandına girmek denenmedi ve
denenmeyecek.

**Makaleye etkisi.** Birincil model SA. SST işaretlenerek raporlanacak.
Model belirsizliği kendi iki koşumuzdan kestirilemez; referans
literatürdeki yerleşik kod farkı kullanılacak (%0,9).

**İki düzeltme yapıldı** ve ikisi de aşağıda duruyor: (1) "hedef 1,000"
iddiasını fazla güçlü kurmuştum; (2) Şekil 4.1'in eksenini yanlış
kalibre etmiştim. İkisi de kendi denetimlerimle yakalandı, ikisi de
ilgili sayıları düzeltti.

## Referans değerler

| kaynak | koşul | C_D,0 |
|---|---|---:|
| **Ladson, NASA TM 4074, Şekil 28(b)** | M 0,15 · Re 6×10⁶ · geçiş %5c'de tetiklenmiş | **0,00807** ± 0,0002 |
| **McCroskey en iyi uyumu** (NASA TMR) | Re 6×10⁶ · tetiklenmiş · C_L = 0 | **0,00826** ± 0,0001 |

İkisi %2 içinde uyuşuyor.

Kaynak PDF'lerin metin katmanı yok (taranmış). Değerler 300 dpi'da
görüntüye çevrilip **ızgara çizgileri tespit edilerek** ve işaretçilerin
piksel ağırlık merkezi ölçülerek okundu. Her kalibrasyon, bilinen ızgara
değerleriyle çapraz doğrulandı — örneğin Ladson taramasında 0,010 ve 0,006
çizgileri geri okunduğunda 0,01000 ve 0,00600 çıktı.

**Kullanılmayan bir veri:** aynı şekilde `#60-W` (sarmalı geçiş şeridi)
işaretçisi 0,00897 veriyor. Raporun kendi metni sarmalı yöntemin zımpara
tanelerinden ötürü sürüklemeyi ~0,001 artırdığını söylüyor; bu yüzden o
seri referans alınmadı.

## Sonuç

| | C_D,0 | Ladson'a göre |
|---|---:|---:|
| Ladson deneyi | 0,00807 | — |
| McCroskey en iyi uyum | 0,00826 | +2,4 % |
| **k-ω SST** (bizim) | 0,00769 | **−4,7 %** |
| **Spalart-Allmaras** (bizim) | 0,00842 | **+4,3 %** |

**Deney bandı iki modelimizin tam arasında kalıyor.**

Bu, veriyi görmeden önce ölçtüğümüz şeyi bağımsız olarak doğruluyor:
türbülans modeli seçimi C_D'yi %9,4 oynatıyordu, bütün sayısal
belirsizliklerin (ağ ±%0,4, alan %0,1, y+ mertebesi %0,03) yirmi katı.
Şimdi görülüyor ki o %9,4'lük aralık gerçeği **içine alıyor**, ve hangi
modelin doğru olduğu ancak deneyle söylenebilirmiş — tam da söylediğimiz
gibi.

## Bu karşılaştırmanın üç koşul farkı

Hiçbiri gizlenmiyor; üçü de sonucu okurken bilinmeli.

**1. Geçiş.** Bizim çözümümüz tamamen türbülanslı (geçiş hücum
kenarında), Ladson %5 veterde tetiklenmiş. Tamamen türbülanslı akış daha
çok sürükleme üretir, yani bizim değerlerimiz deneyin biraz **üstünde**
çıkmalıydı. Bu, SST'nin %4,7 aşağıda kalmasını daha da anlamlı kılıyor ve
SA'nın %4,3 yukarıda olmasının bir kısmını açıklıyor. NASA TMR sayfası
yine de tetiklenmiş veriyi tamamen türbülanslı CFD için uygun referans
sayıyor ve bunu açıkça yazıyor.

**2. Geometri.** Biz kapalı firar kenarlı NACA 0012 kullanıyoruz (azami
kalınlık %12, firar kenarı x = 1'de sıfır kalınlıkta kapanıyor). NASA
TMR'ın **CFD ağları** bunun yerine 1,008930411365 ile ölçeklenmiş, azami
kalınlığı %11,894 olan bir kopya kullanır. Ladson'ın **rüzgâr tüneli
modeli** ise gerçek NACA 0012'dir (veter 60,10 cm, ölçüler tasarım
ordinatlarından 0,0002c'den az sapıyor) ve gerçek NACA 0012'nin firar
kenarı kördür. Yani bizim geometrimiz TMR'ın CFD geometrisinden çok
deneyin modeline yakın; ama kör firar kenarının taban sürüklemesi bizde
yok.

**3. Sıkıştırılabilirlik ve alan.** Bizimki sıkıştırılamaz, deney M = 0,15.
Ladson Şekil 27(a) `c_d,o`'nun M 0,15–0,36 arasında neredeyse düz olduğunu
gösteriyor. Dış sınırımız 20 veter, TMR'ınki 500; 20 → 200 vetere geçmenin
ölçülen etkisi −%0,14.

## Yan bulgu: `cd0.py`'nin geçiş seçimi doğruymuş

`aero/cd0.py` NeuralFoil'i `xtr = 0,05` ile çağırıyor. Ladson'ın
tetiklenmiş serisi **tam olarak %5 veterde** tetiklenmiştir. Yani makalenin
şerit hesabındaki geçiş varsayımı, bu alandaki yerleşik deney pratiğiyle
birebir örtüşüyor — daha önce yalnızca "gerçekçi" diye gerekçelendirilen
bir seçim, artık bir referans deneyle aynı noktada.

## Hâlâ eksik olan

NASA TMR'ın **CFL3D ve FUN3D referans sonuçları** alınamadı: doğrulama
sayfasındaki değerler bir alt bağlantının arkasında
(`naca0012numerics_val_sa.html`) ve o sayfa kaydedilmemiş. Bunlar
gelirse şunu ekleyebiliriz: yerleşik iki çözücü aynı vakada ne veriyor ve
onların ağ yakınsama davranışı bizimkiyle nasıl karşılaştırılıyor.

Ayrıca McCroskey'nin kendi raporu (NASA TM 100019, 1987,
`ntrs.nasa.gov/citations/19880002254`) çok sayıda NACA 0012 deneyini
eleştirel olarak karşılaştırıyor; en iyi uyum eğrisinin nasıl kurulduğunu
birinci elden okumak için o gerekir.


---

# Kod-kod karşılaştırması ve açılan sorun

Kaynaklar arasında **NAS-2016-01** (Jespersen, Pulliam, Childs, NASA Ames)
sekiz yerleşik kodun aynı vakadaki değerlerini veriyor. Bu, deneyden ayrı
ve ondan daha keskin bir sınama: aynı denklemleri çözen kodlar birbirine ne
kadar yakın?

α = 0°, Re = 6×10⁶, M = 0,15 (NAS-2016-01, Tablo 7.1 ve 7.2):

| kod | SA | SST |
|---|---:|---:|
| CFL3D | 0,00819 | 0,00809 |
| FUN3D | 0,00812 | 0,00808 |
| NTS | 0,00813 | 0,00809 |
| Joe | 0,00812 | — |
| SUMB | 0,00813 | — |
| TURNS | 0,00830 | — |
| GGNS | 0,00817 | — |
| Overflow | 0,00838 | 0,00821 |
| **ortalama** | **0,00819** | **0,00812** |
| yayılım | %3,2 | %1,6 |

| | bizim | referans aralığı | konum |
|---|---:|---|---|
| Spalart-Allmaras | 0,00842 | 0,00812 – 0,00838 | **sekizinin de üstünde** (+%2,8) |
| k-ω SST | 0,00769 | 0,00808 – 0,00821 | **dördünün de altında** (−%5,3) |

İki kurulumumuz da bandın dışında ve **ters yönlerde**. Aralarındaki
yayılım %9,5; referansların SA–SST farkı %0,9.

Çözünürlük değil: Overflow'un kendi SST ağ yakınsaması 57 921 hücrede
0,00826, 919 809 hücrede 0,00817 (Tablo 7.5). Bizim 82 944 hücredeki
değerimiz 0,00765.

## Elenen açıklama: serbest akış türbülansı

İlk aday, referansın SST için (μt/μ)∞ = 0,001 kullanması, bizimse 1,0
kullanmamızdı — bin kat fark. **Çürütüldü:**

| μt/μ | ω∞ | C_D |
|---:|---:|---:|
| 1 | 9 | 0,00769073 |
| 0,1 | 90 | 0,00769062 |
| 0,01 | 900 | 0,00769053 |
| **0,001** | **9000** | **0,00769060** |

Bin katlık aralıkta toplam değişim **%0,0027**. Referansın kendi değeriyle
koştuğumuzda da aynı sonuç çıkıyor.

Duyarsızlığın fiziksel sebebi de ölçüldü: ω serbest akışta bozunuyor ve
ω(x) = ω₀/(1+βω₀x) **doyuma** gidiyor. 20 veterlik alanda doyum değeri
1/(0,0828×20) = 0,604 — ω∞ ne olursa olsun. Profilin 1 veter önünde
ölçülen değerler 0,64 ve 0,75. Yani gelen türbülansı serbest akış değeri
değil **alan boyutu** belirliyor. Referans kodlar 500 veter kullanıyor;
orada doyum 0,024.

Bu, kendi fizik argümanımın öngördüğü sonuçtu — yüksek serbest akış
viskozitesi sürüklemeyi artırır, azaltmaz. Hipotez yine de kuruldu ve
sınandı, çünkü argüman yanılabilirdi. Bir açıklama sınıfı temizce elendi.

## Farkın yeri — sınır tabakasının kendi yapısı

Toplam C_D farkın nerede olduğunu söylemez; `ortak/cf.py` söylüyor.
SST/SA sürtünme oranı:

| x/c | 0,02 | 0,10 | 0,30 | 0,51 | 0,98 |
|---|---:|---:|---:|---:|---:|
| C_f(SST)/C_f(SA) | 0,963 | **0,890** | 0,901 | 0,912 | 0,957 |

Açık ön bölgede yoğunlaşıyor ama **laminer bir bölge değil**: laminer
olsaydı C_f beş kat düşerdi, burada en fazla %11.

Farkın *nerede* olduğu bulundu; sıra *neyin* farklı olduğunda.

`ortak/duvaryasasi.py` sınır tabakası profilini duvar değişkenlerinde
çıkarıyor. Bu sınamanın **dışarıdan hiçbir veriye ihtiyacı yok**: referansı
fiziğin kendisi.

    logaritmik tabaka   u⁺ = (1/κ) ln y⁺ + B ,  κ = 0,41 , B = 5,0

x/c = 0,5'te, aynı ağda, aynı şemalarda, aynı kuvvet integraliyle:

| y⁺ | u⁺ (SA) | u⁺ (SST) | SA − log | SST − log |
|---:|---:|---:|---:|---:|
| 30 | 13,132 | 13,531 | −0,164 | **+0,236** |
| 50 | 14,421 | 15,238 | −0,120 | **+0,697** |
| 120 | 16,583 | 17,847 | −0,094 | **+1,170** |
| 200 | 17,924 | 19,313 | +0,001 | **+1,390** |

SA log yasasının üzerinde oturuyor. SST **yukarı kaymış**: aynı y⁺'ta daha
büyük u⁺, yani daha küçük u_τ, yani C_f = 2(u_τ/U)² doğrudan düşük.
u_τ/U: SA 0,04062, SST 0,03879.

Bunun anlamı: açık kuvvet integralinde ya da ağda değil, sınır tabakasının
kendi yapısında.

### Hangi denklemde?

Denge halindeki logaritmik tabakada k-ω ailesinin üç bağıntısı, modelin
kendi sabitlerinden çıkar — ölçüme dayanmaz:

    ν_t = κ u_τ y       k = u_τ²/√β*  (k⁺ = 3,333)      ω = u_τ/(√β* κ y)

Üçü birbirine bağlı (ν_t = k/ω), yani ikisi tutup biri tutmuyorsa okuma
hatası vardır. Ölçülen (x/c = 0,5, log tabakasının ortası, y⁺ ≈ 155):

| büyüklük | SST | SA |
|---|---:|---:|
| ν_t/(κ u_τ y) | **0,880** | 0,984 |
| k⁺ / 3,333 | 1,029 | — |
| ω / ω_denge | **1,170** | — |

Üçü kendi içinde tutarlı: 1,029 / 1,170 = 0,879. Yani **k doğru, ω ~%17
fazla**, ν_t bu yüzden ~%12 eksik. Kusur ω denklemindedir, k denkleminde
değil.

### Bu bir sayısal artık değil

Aynı ölçüm ağ ailesinin üç kademesinde:

| ağ | hücre | ilk hücre y⁺ | azami ν_t/(κ u_τ y) | ω/ω_denge |
|---|---:|---:|---:|---:|
| B2 | 16 448 | 1,54 | 0,880 | 1,188 |
| B3 | 36 864 | 1,04 | 0,880 | 1,173 |
| B4 | 82 944 | 0,70 | 0,882 | 1,163 |

Oran inceltmeyle **kıpırdamıyor**. Viskoz alt tabakadaki ω bozunumu
düzeliyor (5. hücrede asimptotun 2,90 → 2,49 → 1,82 katı) ama log
tabakasındaki denge sapması 0,88'de duruyor. Ayrışım hatası değil.

C_D'nin kendisi de aynı şeyi söylüyor — ağ inceltmesi salınımlı ve
referansa doğru **gitmiyor**:

| ağ | A ailesi C_D | B ailesi C_D |
|---|---:|---:|
| 1 | 0,008127 | 0,008494 |
| 2 | 0,007775 | 0,007804 |
| 3 | 0,007691 | 0,007691 |
| 4 | 0,007649 | 0,007750 |

### Ama bu henüz kusur KANITI değil

Dürüst olmak gerekirse burada durmak yanlış olur. x/c = 0,5'te basınç
gradyanı **ters** yönlüdür ve SST tam da ters gradyanda ν_t'yi bilerek
kısar — a₁ sınırlayıcısı bunun için vardır. Yani 0,88 modelin doğru
davranışı da olabilir; SA'nın 0,98 vermesi SA'nın karışım uzunluğunun
doğrudan κu_τy üzerine kurulu olmasından da gelebilir.

İki olasılığı ayırmanın yolu, basınç gradyanının **sıfır** olduğu bir
akışta aynı ölçümü yapmaktır: `levha/duzlevha.py`. Beklenti önceden
yazılı:

- Düz levhada oran ~1,00 çıkarsa kurulumumuz doğrudur, profildeki 0,88
  ters gradyanın fiziğidir, ve referans kodlarla aramızdaki %5 başka
  yerde aranmalıdır.
- Düz levhada da ~0,88 çıkarsa kusur kurulumun kendisindedir ve basınç
  gradyanından bağımsızdır.

Sonuç aşağıda: **(b) çıktı.**

## Duvar işlemi — ELENMEDİ, tersine en büyük kaldıraç çıktı

`naca/sst_kurulum.py`, SST'ye özgü duvar koşullarını tek tek değiştiriyor.

| varyant | C_D | tabana göre |
|---|---:|---:|
| taban (mevcut kurulum) | 0,007691 | — |
| ω duvar fonksiyonu harmanlamasız | 0,007685 | −%0,08 |
| ν_t duvarda `calculated` | çözülemedi | — |
| k duvarda `kLowReWallFunction` | 0,007691 | %0,00 |
| **ω duvarda yüze fixedValue 6ν/(β₁d₁²)** | **0,008704** | **+%13,2** |

**Bu satırı önce yanlış yazdım.** İlk dört varyant sonuç değiştirmeyince
"duvar işlemi elendi" diye kaydetmiştim; beşincisi henüz koşuyordu.
Beşincisi geldiğinde C_D %13 değişti. Doğrusu şudur: duvar ω koşulu bu
kurulumda **ölçülen en büyük tek kaldıraçtır** — ve referansla aramızdaki
%5'ten iki buçuk kat büyüktür.

Yön de anlamlı. Duvar fonksiyonu ile 0,00769 (bandın %6 altında), yüze
konan sabit değerle 0,00870 (bandın %6 üstünde). Referans bandı
(0,00808–0,00821) tam **ikisinin arasında**.

Beşinci varyantın neden bu kadar oynattığı da açık: 6ν/(β₁d₁²) formülü
ilk hücre *merkezindeki* ω'yı verir; onu duvar *yüzüne* koymak, gerçek
ω'nın çok daha büyük olduğu bir yere küçük bir değer koymaktır. ω az →
ν_t fazla → sürtünme fazla. Yani bu varyant "ders kitabı koşulu" değil,
ω'nın duvarda eksik belirtilmesidir; betikteki o adlandırma yanlıştı.

Ne kadar eksik olduğunu söyleyecek birinci elden bir kaynağım yok, o
yüzden bir çarpan iddia etmiyorum. Bunun yerine aralık taranıyor
(`levha/omega_duvar.py`).

## Düz levha: 0,88 basınç gradyanının fiziği DEĞİL

`levha/duzlevha.py`, sıfır basınç gradyanlı düz levha. Neden gerekliydi:
x/c = 0,5'te basınç gradyanı ters yönlüdür ve SST tam da orada ν_t'yi
bilerek kısar (a₁ sınırlayıcısı), yani 0,88 modelin doğru davranışı da
olabilirdi. Beklenti önceden yazılmıştı.

Ölçülen (x = 1 m, Re_x = 5×10⁶, log tabakasının ortası):

| | C_f | ν_t/(κ u_τ y) | k⁺/3,333 | ω/ω_denge |
|---|---:|---:|---:|---:|
| Spalart–Allmaras | 0,002727 | **0,969** | — | — |
| k-ω SST | 0,002622 | **0,859** | 0,958 | 1,111 |

Sıfır gradyan varsayımı ayrıca ölçüldü: levha boyunca dCp/dx = −0,0034.
Profilde aynı istasyondaki gradyan bunun ~150 katıdır.

SA log yasasının üzerinde (u⁺ − log = +0,09, düz) ve oran 0,97 — yani
**ölçüm makinesi doğru çalışıyor**, bu ölçümün iç denetimi budur. SST ise
sıfır gradyanda da 0,86. Profildeki 0,88 ile aynı.

Yani beklentideki (b) şıkkı çıktı: **kusur basınç gradyanından bağımsız,
kurulumun kendisindedir.** Ve yine ω'da: k %4 düşük, ω %11 fazla,
0,958/1,111 = 0,863 — ölçülen 0,859 ile tutarlı.

## Geometri: payı %0,3, açıklamıyor

`naca/tmr_geo.py`, TMR'ın kendi %11,894 kalınlıklı profiliyle iki modeli
koşuyor (bizimki kapalı firar kenarlı %12).

| model | %12 profil | TMR profili | değişim | referans bandı | durum |
|---|---:|---:|---:|---|---|
| k-ω SST | 0,00769 | 0,00767 | −%0,30 | 0,00808–0,00821 | dışında |
| Spalart–Allmaras | 0,00842 | 0,00839 | −%0,38 | 0,00812–0,00838 | dışında (kıl payı) |

Beklenti "ikisi de düşmeli" idi; düştüler, ama %1 değil %0,3. Geometri
ortak yanlılığın küçük bir parçası; SST'deki açığı açıklamıyor. SA ise
TMR profiliyle bandın üst sınırına (0,00838) 0,00839 ile değiyor.

## Düz levhanın birinci elden referansı bulundu — en güçlü doğrulama

NAS-2016-01'in **4. bölümü** tam da kurduğum vaka: *2D Zero Pressure
Gradient Flat Plate*, M = 0,2, **Re = 5.000.000** birim uzunluk üzerinden.
Bizimki de Re = 1/(2×10⁻⁷) = 5×10⁶. Bölüm iki bağımsız kodun (Overflow ve
Cfl3d) sonuçlarını veriyor, üstelik ilgilendiği büyüklükler bizim
ölçtüklerimizin aynısı: C_f'in Re_θ'ya karşı değişimi ve Re_θ = 10000'de
u⁺ profili. Re_θ tanımını da veriyor (integralin üst sınırı u = %99,5 U∞);
kendi Re_θ'mızı o tanımla hesapladık.

**Okuma yöntemi.** Şekillerde sayısal tablo yok — ama PDF'teki şekiller
vektör grafik, yani eğrilerin düğüm noktaları dosyanın içinde sayı olarak
duruyor. Sayfa SVG'ye çevrilip eğri yolları doğrudan okundu
(`veri/nas_sekil.py`). Bu, şekli gözle okumaktan (raster
sayısallaştırma) niteliksel olarak farklıdır: okunan şey çizimin kendi
verisidir.

**Kalibrasyon varsayılmadı, sınandı.** Şekil 4.2'de üçüncü eğri Coles'in
ortalama hız profili ve logaritmik tabakada u⁺ = (1/κ)ln y⁺ + B'ye
oturmak zorunda. Çıkarılan eğri bu bağıntıya y⁺ = 100–300 arasında
**0,05'ten iyi** uyuyor. Uymasaydı okuma geçersiz olurdu; denetim
doğrudan bunun için var ve `karsilastir.py` denetim başarısızsa çalışmayı
durduruyor.

### u⁺ profili, Re_θ = 10000'de eşleştirilmiş

| y⁺ | bizim SA | Overflow | Cfl3d | fark | | bizim SST | Overflow | Cfl3d | fark |
|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| 30 | 13,235 | 13,289 | 13,204 | **−0,054** | | 13,134 | 12,643 | 12,656 | **+0,491** |
| 100 | 16,371 | 16,371 | 16,368 | **−0,000** | | 16,708 | 16,213 | 16,230 | **+0,495** |
| 200 | 18,001 | 18,030 | 18,026 | **−0,029** | | 18,521 | 17,957 | 17,974 | **+0,565** |
| 300 | 19,036 | 19,054 | 19,050 | **−0,018** | | 19,608 | 19,024 | 19,118 | **+0,584** |
| 500 | 20,567 | 20,567 | 20,567 | **−0,000** | | 21,129 | 20,597 | 20,614 | **+0,532** |
| 800 | 22,021 | 22,080 | 22,076 | **−0,059** | | 22,492 | 21,912 | 21,930 | **+0,579** |

**Bizim SA'mız iki bağımsız referans kodla ±0,06 u⁺ içinde çakışıyor.**
Bu, ağın, şemaların, u_τ çıkarımının ve kuvvet makinesinin doğrulanmasıdır
— hepsi SST ile ortak. **Bizim SST'miz ise her y⁺'ta düzgün olarak
+0,53 u⁺ kaymış.** Eğim aynı (κ doğru), eklenen sabit farklı: aynı hız
için daha küçük u_τ, dolayısıyla düşük sürtünme.

### C_f, Re_θ'ya karşı

| Re_θ | bizim SA | bizim SST | **bizim SST/SA** | ref. SST/SA (Overflow) | ref. SST/SA (Cfl3d) |
|---:|---:|---:|---:|---:|---:|
| 5000 | 0,002954 | 0,002827 | **−%4,30** | −%0,21 | −%0,35 |
| 7000 | 0,002796 | 0,002669 | **−%4,54** | −%0,26 | −%0,53 |
| 9000 | 0,002679 | 0,002550 | **−%4,82** | −%0,43 | −%0,55 |
| 11000 | 0,002588 | 0,002481 | **−%4,13** | −%0,45 | −%0,78 |

Referansta iki model düz levhada **birbirinden %0,2–0,8 ayrılıyor.**
Bizde **%4,1–4,8.** Profildeki 9,4'lük ayrılmayla aynı yönde ve aynı
cinsten.

Mutlak değerlerde (düzeltilmiş eksenle) SA'mız referansın %1,0–1,3
üstünde, SST'miz %2,7–3,3 altında.

### Mutlak C_f'teki kayma bize ait, modele değil

Mutlak değerlerde SA'mız referansın %1,0–1,3 üstünde, SST'miz %2,7–3,3
altında. İkisi de Re_θ ile **aynı yönde** kayıyor (SA +1,03→+1,30, SST
−3,33→−2,65; ikisi de ~%0,4–0,7 artıyor). Ortak bileşen ikisini birden
etkileyen iki kurulum farkından geliyor ve dürüstlük gereği
kaldırılmamıştır:

- **Sıkıştırılabilirlik**: referans M = 0,2, bizimki sıkıştırılamaz.
- **Kapatma**: üst sınırımız H = 1 m'de kayma koşulu; levha boyunca
  dCp/dx = −0,0034 ölçüldü. Hafif elverişli gradyan sınır tabakasının
  iz bileşenini kısar, C_f'i biraz yükseltir, ve etkisi δ büyüdükçe
  büyür — ölçülen ortak eğilimin işareti ve gidişi bununla uyumlu.

Bu yüzden **mutlak C_f farkları modelin doğrulaması olarak okunmamalıdır**;
anlamlı olan iki model ARASINDAKİ fark, çünkü ortak bileşen ikisinde de
aynıdır. O fark referansta %0,2–0,8, bizde %4,1–4,8.

## Duvar ω taraması: beklentinin (b) şıkkı çıktı

`levha/omega_duvar.py`, düz levhada duvar ω koşulunu iki onlu bir aralıkta
tarıyor, yanında serbest akış ve ağ. Hedef **kesin ve dışarıdan ölçüm
gerektirmiyor**: modelin kendi kapanış şartı ν_t = κu_τy = 1,000.

| varyant | C_f | ν_t/(κu_τy) | k⁺/3,333 | ω/ω_denge |
|---|---:|---:|---:|---:|
| taban (duvar fonksiyonu) | 0,002622 | 0,859 | 0,957 | 1,113 |
| serbest akış ÷100 | 0,002625 | 0,859 | 0,957 | 1,113 |
| ağ ince (y₁ yarı, 192 hücre) | 0,002661 | 0,859 | 0,958 | 1,116 |
| duvarda 1× 6ν/(β₁d₁²) | 0,002714 | 0,866 | 0,958 | 1,107 |
| duvarda 10× | 0,002630 | 0,860 | 0,957 | 1,113 |
| duvarda 100× | 0,002576 | 0,856 | 0,956 | 1,116 |

Duvar ω koşulu iki onluda değişirken C_f **%5,4** yayılıyor — ama
**oran 0,856–0,866'da duruyor.** Serbest akış ve ağ da bu vakada ayrıca
elendi.

Yani duvar işlemi C_f'i oynatıyor, log tabakası dengesizliğini
**düzeltmiyor**. Önceden yazılan beklentinin (b) şıkkı: kusur bu üç
değişkende değil.

**a₁ sınırlayıcısı da elenmiş durumda**, ve bu ayrı bir koşu
gerektirmedi: ölçülen k ve ω'dan k/ω = 0,957/1,113 = 0,860 çıkıyor ve bu
ölçülen ν_t oranının kendisi. Yani ν_t gerçekten k/ω'ya eşit —
sınırlayıcı devrede değil.

Geriye SST'ye özgü makine kalıyor: F₁ harmanlaması ve çapraz yayılım
terimi. `levha/model_ayirt.py` bunu ayırıyor — aynı ağ, aynı şemalar,
aynı sınır koşulları, tek fark model: düz kOmega (Wilcox), ki onda
harmanlama ve çapraz yayılım **yoktur**. Beklenti önceden yazılı.

## Model ayırt edici: kusur SST'ye özgü değil, ω ailesinde ortak

`levha/model_ayirt.py` — aynı ağ, aynı şemalar, aynı sınır koşulları,
tek fark model:

| model | C_f | ν_t/(κu_τy) | k⁺/3,333 | ω/ω_denge |
|---|---:|---:|---:|---:|
| Spalart–Allmaras | 0,002727 | **0,969** | — | — |
| kOmega (Wilcox) | 0,002760 | **0,881** | 0,959 | 1,089 |
| kOmegaSST | 0,002622 | **0,859** | 0,957 | 1,113 |

Düz k-ω'da F₁ harmanlaması ve çapraz yayılım **yoktur**, yine de açık
var. Önceden yazılan beklentinin (b) şıkkı: kusur SST'ye özgü makinede
değil, ω ailesinde ortak. (SST biraz daha kötü, 0,859'a karşı 0,881 —
ama asıl açık ikisinde de var.)

Bu koşu ayrıca bir yeniden üretim denetimidir: kOmegaSST bağımsız bir
dizinde, ayrı bir koşuda yine 0,859 verdi.

### DÜZELTME: "hedef 1,000" iddiasını fazla güçlü kurmuşum

Yukarıda ν_t = κu_τy'yi "modelin kendi kapanış şartı, dışarıdan ölçüm
gerektirmez" diye yazdım ve 0,86'yı bu hedefe göre bir **kusur ölçüsü**
gibi kullandım. **Bu fazla güçlü bir iddiaydı.**

Bağıntı, **denge halindeki** logaritmik tabakada kesindir. Düz levhanın
sınır tabakası ise akış yönünde **gelişmektedir**: k ve ω'nın taşınım
terimleri sıfır değildir, dolayısıyla doğru kurulmuş bir iki denklemli
model de sonlu Re_θ'da 1,000'i tam tutturmak zorunda değildir. SA'nın
0,97 vermesi bunu çürütmez: SA'nın ν_t'si doğrudan duvar uzaklığı
üzerine kuruludur, yani onda oran neredeyse tanım gereği 1'e yakın
çıkar. Bu, SA'nın bir özelliğidir; k-ω için 1,000'in doğru hedef
olduğunun kanıtı değildir.

**Kaynağı birinci elden okudum.** Koştuğum ikilinin tam kaynağı Ubuntu
arşivinden çekildi (`apt-get source openfoam`, 1912.200626-2build3):

- `kOmega`: β* = 0,09, β = 0,072, γ = 0,52, σ_k = σ_ω = 0,5;
  ν_t = k/ω (sınırlayıcı yok); ω üretimi γ·S², k üretimi ν_t·S².
  Ders kitabı Wilcox biçimi.
- `kOmegaSST`: β₁ = 0,075, γ₁ = 5/9, σ_ω1 = 0,5; β₂ = 0,0828,
  γ₂ = 0,44, σ_ω2 = 0,856; a₁ = 0,31, b₁ = 1, c₁ = 10.

Üç katsayı takımı da log tabakası bağıntısını sağlıyor:

| dal | β | γ | σ_ω | ima edilen κ |
|---|---:|---:|---:|---:|
| SST iç | 0,0750 | 0,5556 | 0,500 | 0,4082 |
| SST dış | 0,0828 | 0,4400 | 0,856 | 0,4102 |
| kOmega | 0,0720 | 0,5200 | 0,500 | 0,4099 |

Yani katsayılarda kusur yok ve bu, yukarıdaki düzeltmeyle uyumlu.

### Geriye ne kalıyor — ayakta kalan ve düşen

**Düşen:** 0,86'nın 1,00'den sapmasını "%14 model hatası" diye okumak.
Bu sayı artık bir kusur ölçüsü değil, yalnızca bir işarettir.

**Ayakta kalan ikisi:**

1. **Profil karşılaştırması** (`levha/karsilastir.py`). SA'mız iki
   bağımsız referans kodla ±0,06 u⁺ içinde, SST'miz +0,53 u⁺ kaymış —
   aynı vaka, aynı model, eşleştirilmiş Re_θ. Bu **varsayımsızdır** ve
   asıl kanıt budur. SST'deki uyuşmazlık gerçektir.

2. **Oranın varyantlara duyarsızlığı.** Serbest akış, ağ, duvar ω
   koşulu (iki onlu), şemalar ve model değişirken oran 0,856–0,881
   arasında kalıyor. Bu bir *karşılaştırmadır*, mutlak bir hedefe
   dayanmaz, dolayısıyla düzeltmeden etkilenmez: o değişkenlerin hiçbiri
   SST/SA farkını üretmiyor.

Betiklerdeki "HEDEF 1,000 — modelin kendi kapanış şartı" satırları da bu
çekinceyle düzeltildi.

## Şema taraması: o da elendi

`levha/sema.py`, beş varyant, hepsi kOmegaSST:

| varyant | C_f | ν_t/(κu_τy) |
|---|---:|---:|
| taban | 0,002622 | 0,859 |
| türbülans gradyanları sınırsız | 0,002620 | 0,859 |
| U gradyanı sınırsız | 0,002622 | 0,859 |
| bütün gradyanlar sınırsız | 0,002621 | 0,859 |
| k/ω taşınımı sınırsız merkezi | 0,002621 | 0,859 |

Hücre sınırlayıcısı hipotezi (SA'nın `grad(nuTilda)`'sı sınırsız, ω
modellerininki değil) **çürüdü**: sınırlayıcıyı tamamen kaldırmak hiçbir
şeyi değiştirmiyor.

## Eşleştirme yordamının denetimi

Re_θ eşleştirmesi kendi hesabımıza dayanıyor, o yüzden ayrıca
denetlendi. Şekil faktörü H = δ*/θ:

| model | x | Re_θ | δ* | θ | **H** |
|---|---:|---:|---:|---:|---:|
| SA | 1,305 | 10052 | 2,640e−3 | 2,010e−3 | **1,313** |
| SST | 1,372 | 9911 | 2,620e−3 | 1,982e−3 | **1,322** |

Re_θ ≈ 10⁴'te türbülanslı sınır tabakası için beklenen aralıkta. Ayrıca
duyarlılık: Re_θ'da %5 hata C_f'i %0,9, u⁺'ı ~0,12 kaydırır. Ölçülen
kayma 0,53. Yani eşleştirme hatası bunu açıklayamaz.

## Nerede kaldık — açık ve dürüst durum

**Kurulan (sağlam):**

- **Boru hattımız doğrulandı.** SA'mız, aynı vakada iki bağımsız
  referans kodla profil boyunca ±0,06 u⁺ içinde. Bu; ağ üreticisini,
  şemaları, çözücü kurulumunu, u_τ çıkarımını ve kuvvet integralini
  birlikte doğrular — hepsi SST ile ortaktır.
- **SST kurulumumuzda gerçek bir uyuşmazlık var:** +0,53 u⁺, her y⁺'ta,
  eşleştirilmiş Re_θ'da. C_f'te modeller arası fark bizde %4,1–4,8,
  referansta %0,2–0,7.

**Elenen (ölçülerek, tahminle değil):** serbest akış türbülansı (1000
kat), ağ (üç kademe profilde, iki kademe levhada), duvar ω koşulu (iki
onlu), k duvar koşulu, a₁ sınırlayıcısı, SST'ye özgü makine (kOmega da
etkileniyor), ayrışım şemaları (beş varyant), geometri (%0,3), eşleştirme
yordamı (H denetimi).

**Kaynaktan okunan:** koştuğum ikilinin tam kaynağı çekildi. kOmega ve
kOmegaSST ders kitabı biçiminde, katsayılar standart ve log tabakası
bağıntısını κ ≈ 0,41 ile sağlıyor. Uygulamada gözle görülür bir
anormallik yok.

**Bulunamayan:** uyuşmazlığın nedeni. Bunu bulamadım. Ayarla bandın
içine girmeyi denemedim ve denemeyeceğim; öyle bir sayı doğrulama
olmazdı.

**Sınanmayı bekleyen tek madde:** yakınsama. Koşular `residualControl`
hedefine inmiyor, 4000 adımda kalıntılar 1e-6 civarında düzleşiyor.
16 000 adımlık denetim kuyrukta.

## Bunun makaleye etkisi

1. **Birincil model SA olacak.** Doğrulanan o. Bu bir tercih değil,
   ölçümün sonucu.
2. **SST sonuçları rapor edilecek ama işaretlenecek**, ve bilinen
   yanlılığıyla birlikte verilecek.
3. **Model belirsizliği kendi iki koşumuzdan kestirilemez.** Plan
   "3-B gövde iki modelle koşulsun, fark belirsizlik olsun" idi; bu
   artık geçersiz, çünkü bizim SST/SA farkımız modelin değil
   kurulumumuzun farkını taşıyor. Model belirsizliği için referans
   literatürdeki yerleşik kod farkı kullanılacak (NAS-2016-01, alfa = 0:
   SA ortalama 0,00819, SST ortalama 0,00812 — %0,9).

## DÜZELTME 2: Şekil 4.1'in eksenini yanlış kalibre etmişim

Şekil 4.1'in (C_f – Re_θ) x eksenini **çerçeve kenarlarından** 4000–12000
diye almıştım. Yanlıştı: eksen **4000–13000.**

Nasıl yakalandı: eksende 19 tik var, yani 18 aralık. Aralık 4000–12000
olsaydı 2000'lik etiketler tam sayı tike düşmezdi (4,5 tik); 4000–13000
olduğunda tam 4 tike düşüyor. Şüphelenip **etiket gliflerinin sayfa
üzerindeki konumlarını** okudum:

| varsayım | artıkların saçılımı |
|---|---:|
| çerçeve sağı = 12000 | 6,495 (artıklar +1,13'ten +19,50'ye açılıyor) |
| **çerçeve sağı = 13000** | **0,009** (artıklar +1,12'de sabit) |

Doğru kalibrasyonda artıklar sabit olmak zorunda — o sabit, glifin sol
kenarı ile metnin merkezi arasındaki yanlılıktır. Yelpaze gibi açılması
kalibrasyonun yanlış olduğunun kanıtıdır.

Bu denetim artık `veri/nas_sekil.py` içinde `eksen_denetimi()` olarak
duruyor ve `levha/karsilastir.py` saçılım 0,05'i aşarsa **çalışmayı
durduruyor**. Kaynağı: çerçeve kenarı her şekilde eksen ucuna denk
düşmüyor — 4.1 ve 4.2'de düşüyor, Şekil 7.4'te düşmüyor (orada
çerçevenin sol kenarı x/c = −0,040).

**Neyi değiştirdi:** yukarıdaki C_f tablosunun mutlak değerleri. SA'mızın
sapması %1,5–2,6'dan **%1,0–1,3'e** indi (ve Re_θ ile eğilimi düzleşti),
SST'mizinki %1,5–2,9'dan **%2,7–3,3'e** çıktı.

**Neyi değiştirmedi:** u⁺ profili karşılaştırmasını (Şekil 4.2'nin
kalibrasyonu tiklerle ve log yasasıyla iki kez doğrulanmıştı) ve
modeller arası farkı (o kendi koşularımızdan geliyor). Yani asıl kanıt
etkilenmedi; ama yayımladığım bir sayı tablosu yanlıştı ve düzeltildi.

## SA ağ yakınsaması ve profil üzerinde C_f — asıl vakada doğrulama

Ağ taraması SST ile yapılmıştı; makalede güveneceğimiz model SA olduğu
için B ailesi SA ile yeniden koşuldu.

| ağ | hücre | y⁺ort | bizim C_D | | Overflow SA (hücre) | C_D |
|---|---:|---:|---:|---|---:|---:|
| B1 | 7 310 | 2,11 | 0,009848 | | 3 729 | 0,00978 |
| B2 | 16 448 | 1,43 | 0,008983 | | 14 625 | 0,00879 |
| B3 | 36 864 | 0,97 | 0,008416 | | 57 921 | 0,00842 |
| B4 | 82 944 | 0,66 | **0,008234** | | 919 809 | **0,00821** |

İki yakınsama yörüngesi birbirini izliyor. Bizim en ince ağımız 0,008234,
Overflow'un en incesi 0,00821 — **%0,3.** İkisi de hâlâ inceltmeyle
düşüyor (bizde B3→B4 %2,2, Overflow'da 230k→920k %2,0), yani ikisi de
tam yakınsamış değil; bu ortak davranış da anlamlı.

Hücre sayıları kodlar ve ağ topolojileri arasında birebir
karşılaştırılamaz; tablo bir eşleştirme değil, iki eğrinin yan yana
konmasıdır.

### Profil düzeyinde: yüzey sürtünmesi dağılımı

`veri/nas_sekil.py` Şekil 7.4'ten SA modeli için üst yüzeydeki C_f
dağılımını çıkarıyor. Kalibrasyon iki kez sınandı: Cp eğrisinin azami
değeri **1,0058** ve konumu **x/c = 0** — M = 0,15 için kuramsal durma
basıncı 1 + M²/4 = 1,0056, konumu hücum kenarı.

| x/c | bizim (B4) | Overflow | Cfl3d |
|---:|---:|---:|---:|
| 0,050 | 0,005846 | 0,005899 | 0,005768 |
| 0,100 | 0,005297 | 0,005318 | 0,005248 |
| 0,201 | 0,004540 | 0,004573 | 0,004487 |
| 0,296 | 0,004046 | 0,004064 | 0,003990 |
| 0,506 | 0,003274 | 0,003306 | 0,003245 |
| 0,705 | 0,002721 | 0,002744 | 0,002688 |
| 0,902 | 0,002018 | 0,002079 | 0,001996 |

Yedi istasyonun **yedisinde de bizim değerimiz iki referans kodun
arasında.** Yoğun örneklemeyle: x/c 0,03–0,95 arasındaki **91 duvar
yüzünün 83'ünde (%91)** arada; dışarıda kaldığı yerlerde sapma en fazla
**%0,36.** Karşılaştırma için: Overflow ile Cfl3d kendi aralarında
ortalama **%2,33**, en fazla %4,18 ayrılıyor.

Yani SA'mız, iki yerleşik kodun kendi aralarındaki farktan **daha yakın**
duruyor onlara.

Çekinceler, kaldırılmadı: referans ağı 897×257 (230 529 hücre), bizimki
82 944; bizim geometrimiz kapalı firar kenarlı %12, referansınki TMR'ın
%11,894'ü. Daha kaba TMR-geometrisi koşusu (36 864 hücre) yüzlerin
%55'inde arada kalıyor — yani kuşatma ince ağın özelliği, beklendiği
gibi.

**Bunun anlamı:** SA kurulumumuz artık iki bağımsız vakada, iki bağımsız
referans kodla, profil düzeyinde doğrulanmıştır — düz levhada u⁺
(±0,06), profilde C_f (kodlar arası farkın içinde). Makalenin birincil
modeli olarak SA'yı kullanmak bu ölçümlere dayanıyor.

## Aynı ölçüm, SST için: açık profilde de aynı

Şekil 7.6 aynı düzende SST modelinin C_f dağılımını veriyor. Aynı
kalibrasyon denetimi geçti (azami Cp = 1,0058, konum x/c = 0).

| x/c | bizim SST (B4) | Overflow SST | Cfl3d SST | fark |
|---:|---:|---:|---:|---:|
| 0,050 | 0,005473 | 0,005921 | 0,005761 | **−%7,6** |
| 0,100 | 0,004923 | 0,005311 | 0,005159 | **−%7,3** |
| 0,201 | 0,004228 | 0,004512 | 0,004426 | **−%6,3** |
| 0,296 | 0,003781 | 0,004007 | 0,003935 | **−%5,6** |
| 0,506 | 0,003079 | 0,003261 | 0,003201 | **−%5,6** |
| 0,705 | 0,002575 | 0,002708 | 0,002657 | **−%4,9** |
| 0,902 | 0,001937 | 0,002047 | 0,002004 | **−%5,4** |

**91 duvar yüzünün sıfırı** iki referans kodun arasında. Karşılaştırma
için aynı ağda SA'mız **%91'inde** arada.

Yan yana koyunca resim şu:

| | ağ | kodlar arasında kalan yüz | azami sapma |
|---|---|---:|---:|
| bizim SA | B4 (82 944) | %91 | %0,36 |
| bizim SST | B4 (82 944) | %0 | %7,6 |

Aynı ağ, aynı şemalar, aynı çözücü, aynı kuvvet integrali, aynı sonradan
işleme. Ayrılan tek şey türbülans modeli. Açık firar kenarına doğru
azalıyor (hücum kenarında %7,6, x/c = 0,7'de %4,9) — düz levhadaki
u⁺ kaymasının işaretiyle ve büyüklüğüyle tutarlı.

## ~~Sıradaki şüpheli: kendi şema seçimimiz~~ — ÇÜRÜTÜLDÜ

> Bu bölüm bir hipotez kurarken yazıldı ve **sınandı, çürüdü.**
> Sonucu yukarıdaki "Şema taraması: o da elendi" bölümünde:
> beş varyantın beşi de 0,859 veriyor, sınırlayıcıyı tamamen
> kaldırmak hiçbir şeyi değiştirmiyor. Silmiyorum, çünkü
> beklenti önceden yazılmıştı ve çürütülmüş bir hipotez de
> kayıttır. Aşağısı o zamanki metindir.

ω ailesi ile SA arasında kurulumumuzda **gerçek bir asimetri** var ve bu
bizim kendi seçimimiz:

```
grad(U)        cellLimited Gauss linear 1
grad(k)        cellLimited Gauss linear 1
grad(omega)    cellLimited Gauss linear 1
grad(nuTilda)  — listede YOK, default'a düşüyor: Gauss linear
```

SA'nın türbülans değişkeninin gradyanı sınırlandırılmamış, iki ω
modelininki sınırlandırılmış. ω duvar yakınında y⁻² gibi davranır;
gerilmiş ağda hücre sınırlayıcısı orada ısırabilir. `levha/sema.py` beş
varyantla bunu sınıyor; beklenti önceden yazılı:

- **(a)** Bir varyant oranı ~1,00'e taşırsa kusur bizim şema
  seçimimizdir. Düzeltilir ve düzeltilmesi meşrudur — şema bir *ayrışım
  seçimidir*, uydurulmuş bir model sabiti değil. O durumda **bütün NACA
  sonuçları düzeltilmiş şemayla yeniden koşulur**; eski sayılar kalmaz.
- **(b)** Hiçbiri taşımazsa şema da elenir. Geriye OpenFOAM'ın ω denklemi
  uygulaması kalır; kaynağından okunmadan düzeltilemez, **rapor edilir**.

## Yakınsama da elendi — son açık madde

Koşular `residualControl` hedefine (1e-8) inmiyor; 4000 adımda
kalıntılar düzleşip endTime'a çarpıyor, "SIMPLE solution converged"
iletisi hiç çıkmıyor. Referans rapor kendi koşularında kalıntıların
13 mertebe düştüğünü söylüyor, bizimki ~6.

Bunun sonucu etkilemediğini *düşünmek* için gerekçem vardı (SA aynı
kalıntı seviyesinde referansla çakışıyor) ama gerekçe kanıt değil.
İki ölçüm yapıldı.

**Kalıntı geçmişi.** Son %10'da hiç hareket yok:

| değişken | 1/8'de | sonda | son %10'da oran |
|---|---:|---:|---:|
| SA, Ux | 1,37e−5 | 6,34e−9 | 1,000 |
| SA, nuTilda | 1,46e−5 | 2,70e−6 | 0,992 |
| SST, k | 7,44e−6 | 1,38e−6 | 0,977 |
| SST, ω | 1,96e−8 | 4,25e−9 | 1,000 |

Kalıntılar %25'te platoya oturmuş ve orada duruyor. Bu bir plato, süren
bir yakınsama değil.

**Dört kat uzun koşu.** `levha/duzlevha.py uzun`, 16 000 adım:

| model | 4 000 adım | 16 000 adım |
|---|---|---|
| SA | C_f = 0,002727 ; ν_t/(κu_τy) = 0,969 | C_f = 0,002727 ; 0,969 |
| SST | C_f = 0,002622 ; 0,859 | C_f = 0,002622 ; 0,859 |

**Altı basamağa kadar aynı.** Yakınsama elendi.

## SA ile ağ yakınsaması artık RESMÎ olarak ölçülebiliyor

SST ile bu mümkün değildi: B ailesi salınımlıydı (en ince ağda C_D
0,007691'den 0,007750'ye **yükseliyordu**) ve Richardson sahte bir
p = 8,95 ile %0,02'lik anlamsız bir GCI veriyordu. SA ile iki aile de
tekdüze:

| ağ | hücre | SA C_D | SST C_D |
|---|---:|---:|---:|
| B1 | 7 310 | 0,009848 | 0,008494 |
| B2 | 16 448 | 0,008983 | 0,007804 |
| B3 | 36 864 | 0,008416 | 0,007691 |
| B4 | 82 944 | **0,008234** | 0,007750 ← yükseldi |

Richardson (B2, B3, B4), inceltme oranı r ≈ 1,50:

- gözlenen mertebe **p = 2,82**
- h → 0 kestirimi **C_D = 0,008149**
- en ince ağın **GCI = %1,29**

p, şemaların resmî mertebesinin (2) üzerinde. Bu tek başına iyi haber
değildir — asimptotik bölgeye tam girilmemiş ya da hataların rastlantısal
olarak birbirini götürüyor olması da p'yi şişirir. Bu yüzden ihtiyatlı
değer de veriliyor: **p = 2 alınırsa GCI = %2,21.**

    C_D = 0,008234  ±%1,29 (gözlenen p)   ±%2,21 (ihtiyatlı, p = 2)

Richardson kestirimi 0,008149; Overflow'un en ince ağı (919 809 hücre)
0,00821 veriyor — aralarında **%0,74.** İkisi de aynı yönden, aşağıdan
yaklaşıyor.

### y+ duyarlılığı da modele bağlı çıktı

A4 ile B4 aynı hücre sayısında (82 944) ve aynı topolojide; tek fark
duvar aralığı:

| model | A4 (y⁺≈1,0) | B4 (y⁺≈0,65) | fark |
|---|---:|---:|---:|
| **SA** | 0,008252 | 0,008234 | **−%0,22** |
| SST | 0,007649 | 0,007750 | **+%1,33** |

SA'nın duyarlılığı SST'nin **altıda biri**. Bu, `yplus.py`'nin kendi
gerekçesinin öngördüğü sonuçtur: oradaki mekanizma
`omegaWallFunction`'ın harmanlaması ve ω ~ 6ν/(β₁y²)'nin y → 0'da
ıraksamasıdır; **SA'da ω denklemi yoktur.** Öngörü önce yazıldı, sonra
elde olan veriyle doğrulandı.

Yani B ailesindeki salınım da, y+ duyarlılığı da SST kusurunun
belirtileri arasına giriyor.

## SST'nin y⁺ ile ıraksaması — kusurun en keskin belirtisi

`naca/yplus.py`: ağ topolojisi **sabit** (384×144×96, 82 944 hücre),
yalnızca duvar aralığı değişiyor.

| y⁺ ölçülen | C_D (SST) | artış |
|---:|---:|---:|
| 1,44 | 0,007614 | — |
| 0,96 | 0,007649 | +0,000035 |
| 0,64 | 0,007750 | +0,000101 |
| 0,39 | 0,007880 | +0,000130 |

Çözümlenmiş sınır tabakasında (y⁺ < 1,5) sonucun duvar aralığından
**bağımsız olması gerekir.** Değil: aralık boyunca %3,50 kayıyor. Daha
kötüsü, **artışlar hızlanıyor** — yani y⁺ → 0'da bir değere yakınsamıyor,
ıraksıyor. Bu kurulumun y⁺-yakınsamış bir cevabı yok.

Mekanizma zaten adlandırılmıştı: duvarda ω ~ 6ν/(β₁y²) ve bu, y → 0'da
ıraksar. Ayrık işlem bunu taşıyamıyor.

Bu bulgu üç şeyi birden açıklıyor:

1. **B ailesindeki salınım.** B'de her aralık birlikte inceliyor, yani
   y⁺ de değişiyor; A'da duvar aralığı sabit. SST'nin y⁺ duyarlılığı
   B'yi salındırıyor, A'yı bırakıyor.
2. **Neden tek bir "SST C_D'miz" yok.** 0,00761 ile 0,00788 arasında
   herhangi bir değer, yalnızca duvar aralığı seçilerek elde edilebilir.
   Referans bandı (0,00808–0,00821) bu aralığın hemen üstünde.
3. **Neden ağ yakınsaması SST ile resmî olarak ölçülemedi.** Richardson
   tek bir h ölçüsü varsayar; burada ikinci ve bağımsız bir ölçek
   (duvar aralığı) sonucu sürüklüyor.

### Aynı tarama SA ile: öngörüm ham haliyle YANLIŞTI, düzeltilmiş haliyle doğru

Öngörüyü "SA'da ω denklemi yoktur, dolayısıyla **duyarlılık çok daha
küçük olmalı**" diye yazmıştım. Ölçüm:

| y⁺ | SA C_D | birim y⁺ eğimi | | SST C_D | birim y⁺ eğimi |
|---:|---:|---:|---|---:|---:|
| 1,5 | 0,008657 | — | | 0,007614 | — |
| 1,0 | 0,008252 | **−7,71e−4** | | 0,007649 | +7,27e−5 |
| 0,65 | 0,008234 | −5,55e−5 | | 0,007750 | +3,20e−4 |
| 0,4 | 0,008211 | −8,65e−5 | | 0,007880 | **+5,09e−4** |

y⁺ 1,5 → 1,0 aralığında SA'nın duyarlılığı SST'nin **on katı**. Yani
öngörü, yazıldığı haliyle yanlış. Duyarlılığın *büyüklüğü* üzerine
kurmakla hata etmişim.

Doğru ayrım büyüklükte değil **gidişte**:

- **SA'nın eğimi çöküyor**: −7,71e−4 → −5,55e−5 → −8,65e−5. İlk adımdan
  sonra bir mertebe düşüyor ve orada kalıyor. Yani y⁺ = 1,5 sınır
  tabakasını henüz çözmüyor; 1'in altında çözüm oturuyor. **Yakınsama.**
- **SST'nin eğimi büyüyor**: +7,27e−5 → +3,20e−4 → +5,09e−4, yedi kat.
  Duvara yaklaştıkça çözüm daha hızlı kayıyor. **Iraksama.**

Çözümlenmiş bölgede (y⁺ ≤ 1) yayılım: **SA %0,50, SST %3,02.** Altı kat
fark — ama asıl olan, SA'nın bir değere gitmesi, SST'nin gitmemesi.

SA'nın y⁺ ≤ 1'deki üç noktasından doğrusal dışdeğerleme
C_D(y⁺→0) = 0,008186 veriyor; üretim seçimimiz olan y⁺ ≈ 1 buna göre
**+%0,81.** SST için böyle bir dışdeğerleme savunulamaz, çünkü eğim
büyüyor.

Pratik sonuç: SA için y⁺ ≈ 1 seçimi ölçülmüş bir dayanağa sahip ve
duvar çözünürlüğü belirsizliği **%0,8**. SST için "seçilmiş y⁺" diye bir
şey yoktur — hangi y⁺ seçilirse ona karşılık bir cevap çıkar.

## %25 kesiti: URANS sonucu, ve İKİ yanlış iddiamın düzeltmesi

Bu satır için iki kez yanlış şey söyledim. İkisi de burada duruyor.

**Yanlış 1 (kararlı çözücüye bakarak):** *"Akış kararsız; firar kenarı
ayrılması iki yüzey arasında taraf değiştiriyor."* Belirtiler gerçekti
(C_L ±2,6×10⁻², kalıntılar yükseliyor, ayrılma t=2000'de 23 yüz hepsi
üstte, t=4000'de 8 üst/20 alt) ama **yorum yanlıştı**: bunlar akışın
değil, SIMPLE çözücüsünün ürettiği asimetrilerdi.

**Yanlış 2 (URANS'ın ilk yarısına bakarak):** *"Akış kararlı; C_L üstel
sönümleniyor, C_D 0,01357'ye oturuyor."* Bu da erkendi — o sırada
salınımın yalnızca ilk yarım çevrimini görmüştüm.

**Doğrusu (t = 1,86'ya, yani 1,9 veter geçiş süresine kadar koşuldu):**

| büyüklük | ölçülen |
|---|---|
| C_L | \|C_L\| ≤ 3,5×10⁻⁷ boyunca — **simetrik, dökülme yok** |
| C_D bandı | 0,013720 (t=0,60) … 0,014014 (t=1,09) |
| zaman ortalaması, t = 0,60–1,85 | **C_D = 0,013872** |
| salınım genliği | **±%1,06** |

Yani akış **simetriktir ve dökülmez**, ama kararlı da değildir: C_D
yavaş, simetrik bir kipte ±%1 salınıyor (ayrılma bölgesi nefes alıyor).
t = 1,86'da hâlâ tam oturmamıştı; daha uzun koşmak bu satırın
belirsizliğini ağ belirsizliğinin (%1,3) altına indirmezdi, o yüzden
pencere ortalaması ve bandı **olduğu gibi** raporlanıyor.

Kararlı çözücünün aynı vakada verdikleri, karşılaştırma için:

| | C_D | zaman ortalamasına göre |
|---|---:|---:|
| kararlı, 4000 adım | 0,013920 | +%0,34 |
| kararlı, 16000 adım | 0,013542 | **−%2,38** |

Uzun koşmak **daha kötü** yaptı — savrulduğunun ayrı bir kanıtı.

### Kararlı çözücü neden başarısız? Basınç lineer çözücüsü DEĞİL

Hipotez kurulmuştu: aynı ağda GAMG basınç denkleminde tıkanıyor (en-boy
oranı 5000, dik-olmayanlık 61°), belki SIMPLE her adımda tutarsız bir
basınç alanıyla ilerliyor. Sınandı ve **çürüdü**:

| çözücü | C_D | C_L | Ux kalıntısı | p kalıntısı |
|---|---:|---:|---|---|
| GAMG | 0,013920 | +2,6e−2 | yükseliyor | — |
| PCG+DIC | 0,013892 | +1,99e−2 | yükseliyor (1,27) | **düşüyor** (0,065) |

Basınç kalıntısı artık düzgün düşüyor — lineer çözücü işini yapıyor — ve
başarısızlık yine de sürüyor. Demek ki sorun momentum/türbülans
eşleşmesinde. Nedeni bulunamadı; **rapor ediliyor, gizlenmiyor.**

### Kalınlık çalışmasının sonucu

| t/c | C_D | NF (xtr→0) | oran |
|---|---:|---:|---:|
| %12 | 0,009933 | 0,010113 | 0,982 |
| %18 | 0,011460 | 0,011813 | 0,970 |
| %25 | 0,013872 ±%1,06 | 0,014146 | 0,981 |

**Oranların oranı** — geçiş uyuşmazlığına dayanıklı ölçü:

| | değer |
|---|---:|
| (%18 oranı)/(%12 oranı) | 0,988 |
| **(%25 oranı)/(%12 oranı)** | **0,998** |

**İki boyutta, %12 ile %25 arasında şerit kuramı kalınlıkla
ayrışmıyor.** Oran 1'den ayırt edilemiyor. Bu, 2. basamağın cevabıdır:
kök kesitindeki belirsizlik kalınlıktan değil, **üç boyutluluktan**
gelmelidir — ve onu 3. basamak ölçecek.

## Sırada

- **3-B gövde** (ikinci makalenin 3. adımı): birincil model SA ile.

### Elde olmayan kaynak

`turbmodels.larc.nasa.gov/naca0012numerics_val_sa.html` sayfası indirildi
(`kaynak/naca0012_val.html`) ama dosyada yalnızca NASA sitesinin gezinme
menüsü var — sayısal veri yok, sayfa içeriği sonradan yükleniyor olmalı.
`kaynak/` altındaki üç "Print To PDF" dosyası da salt görüntü; metin
katmanı taşımıyorlar. Yani bu üç dosyadan hiçbir sayı okunamadı ve
hiçbiri bir sayısal iddianın dayanağı değildir.

---

## R=200 alan anomalisi — kapandı (02.09.2026)

2-B'de açık kalan son maddeydi. İki ayrı ölçümle kapandı; biri **hipotezi
çürüttü**, öteki **anomaliyi ayrıştırdı**.

### Hipotez ÇÜRÜTÜLDÜ

Yazılı hipotez şuydu: SA'nın taşıdığı nuTilda'nın yok olma terimi
~(nuTilda/d)² biçimindedir; alan büyüdükçe d büyür, yok olma zayıflar,
girişten gelen nuTilda daha az bozunarak sınır tabakasına ulaşır ve daha
büyük girdap viskozitesi daha yüksek sürükleme verir.

**Birinci ölçüm — duyarlılık var ve yönü uyuyor** (`sa_serbest.py`,
R=200, üç serbest akış değeri):

| nuTilda∞ | C_D | yerleşiğe göre |
|---|---|---|
| 3ν | 0,008432 | — |
| 0,3ν | 0,008396 | −0,43% |
| 0,03ν | 0,008372 | −0,72% |

Düşüş tekdüze ve yönü hipotezle uyumlu. Büyüklük de yeterli görünüyordu:
açıklanması gereken %0,31 için bir onluk nuTilda değişimi %0,43 veriyor.

**İkinci ölçüm — mekanizma yok** (`nutilda_ulasan.py`). Hipotez, R=200'de
profile *ulaşan* nuTilda'nın R=100'dekinden büyük olmasını gerektirir.
Durma çizgisi üzerinde, hücum kenarının önünde ölçüldü:

| x | nuTilda (R=100) | nuTilda (R=200) | oran |
|---|---|---|---|
| −0,50 | 5,000007e−07 | 5,000010e−07 | 1,0000 |
| −0,20 | 5,000035e−07 | 5,000044e−07 | 1,0000 |
| −0,10 | 5,000065e−07 | 5,000085e−07 | 1,0000 |
| −0,05 | 5,000140e−07 | 5,000177e−07 | 1,0000 |
| −0,02 | 5,000218e−07 | 5,000318e−07 | 1,0000 |

Serbest akış değeri 3ν = 5,0e−07. **nuTilda hiç bozunmuyor** — ne
R=100'de ne R=200'de. Nicel denetim %0,31'i açıklamak için ~5 kat oran
istiyordu; ölçülen **1,0000**. Üç mertebe eksik.

Yani hipotezin (b) şıkkı gerçekleşti: **hipotez yanlıştır.** Serbest akış
nuTilda'sının C_D'yi etkilediği doğru, ama bu etki *sınır koşulunun
değerinden* geliyor, yol boyunca bozunmadan değil — bozunma yok. Alan
boyutu bu değeri değiştirmiyor.

### Anomali AYRIŞTIRILDI

Asıl sebep başka yerdeydi ve tarama tasarımının kendisindeydi. `alan.py`,
büyüme oranını sabit tutmak için `n_normal`'ı her R için yeniden seçiyordu:

    R=20 → 96 katman, R=50 → 103, R=100 → 108, R=200 → 113

Yani R=100'den R=200'e geçerken **iki şey birden** değişti. Ayrıldı
(`alan_ayristir.py`):

| vaka | C_D |
|---|---|
| R=100, n=108 | 0,008406 |
| R=100, n=113 | 0,008388 |
| R=200, n=113 | 0,008432 |

| etki | değer |
|---|---|
| saf alan (n=113 sabit, R 100→200) | **+0,52%** |
| uzak alan çözünürlüğü (R=100, n 108→113) | **−0,21%** |
| toplam | **+0,31%** |

Taramanın R=100→R=200 için ölçtüğü değer de **+0,31%**. Aritmetik
kapanıyor: gözlenen "anomali", zıt işaretli iki etkinin toplamıdır.

### Yöntem bulgusu

Bu ağ ailesinde **alan boyutu ile uzak alan çözünürlüğü bağımsız
değiştirilemez.** R'yi büyütüp hem `n_normal`'ı hem büyüme oranını sabit
tutmak mümkün değildir; biri sabitlenirse öteki kayar. Dolayısıyla "saf
alan taraması" diye bir şey yoktur ve `alan.py`'nin büyüme oranını
sabitleme önlemi bir karıştırıcıyı diğeriyle değiştirmiştir. Sonucu
geçersiz kılmaz ama **ne ölçüldüğünü** değiştirir ve makalede böyle
yazılmalıdır.

Büyüklük bağlamı: hem toplam (%0,31) hem saf alan etkisi (%0,52), ağ
belirsizliği olarak ölçülen **GCI %1,29**'un altındadır.

### Tekrarlanabilirlik

İki yerleşik değer sıfırdan yeniden kurulup yeniden çözüldü ve birebir
çıktı: R=200/n=113 → **0,008432**; R=100/n=108 → **0,008406**. Yukarıdaki
farklar kurulum gürültüsü değildir.

---

## 3-B ağ üreteci — sınama (02.09.2026)

Üreteç yeni koddur. Üzerine kanat kurup sonuç üretmeden önce kendisi
sınandı: sabit kesitli, ok açısız, sivrilmesiz kanat, iki ucunda da
`symmetryPlane`. Akış açıklık boyunca değişmez, yani problem **fiziksel
olarak iki boyutludur** ve doğrulanmış 2-B sonucunu yeniden üretmelidir.

İki kurulum arasındaki **tek fark ağdır**: alan dosyaları, şemalar, çözücü
ayarları ve türbülans kurulumu ikisine de `naca/kur.py`'den aynı şekilde
geliyor (`kur3b.py`), ayrıştırma da aynı (hierarchical 2 2 1).

| vaka | hücre | C_D | 2-B'ye göre | C_D viskoz | C_D basınç | C_L |
|---|---|---|---|---|---|---|
| 2-B (`empty`) | 43 392 | 0,008388 | — | 0,007010 | 0,001378 | −4,0e−07 |
| 3-B nk=2 | 43 392 | 0,008409 | +0,249% | +0,298% | **0,000%** | −1,3e−07 |
| 3-B nk=3 | 86 784 | 0,008409 | +0,252% | +0,302% | −0,000% | −3,5e−07 |
| 3-B nk=5 | 173 568 | 0,008392 | **+0,050%** | +0,060% | −0,000% | −3,6e−07 |

### Önden yazılan beklentilerin karşılığı

**(a) "C_D binde birkaçtan fazla sapmamalı" — nk=5'te TUTTU.** Binde 0,5;
GCI %1,29'un yirmide biri. nk=2 ve nk=3'te binde 2,5 ile sınırın
kenarında.

**(b) "Dilim sayısı sonucu DEĞİŞTİRMEMELİ" — TUTMADI.** nk=2 ve nk=3 aynı
(+0,25%), nk=5 beşte birine iniyor (+0,05%). Kendi ölçütüme göre açıklık
yönü çözüme sızıyor. Sızıntı **incelttikçe küçülüyor**, yani formülasyon
hatası değil ayrıklaştırma hatası; ama sızıyor.

**(c) "C_L sıfır kalmalı" — TUTTU.** Üçünde de ~1e−07 (Ux ~1,18'e karşı).

### DÜZELTME — nk=5'ten önce yazdığım sonuç yanlıştı

nk=2 ve nk=3'ün birebir aynı çıkması üzerine şunu yazmıştım: *"+%0,249
açıklık çözünürlüğünün artefaktı değil; geriye `empty` ile
`symmetryPlane` arasındaki sabit kayma kalıyor."*

**Yanlıştı.** nk=5 sapmayı beşte birine indirdi; demek ki açıklık
çözünürlüğüne bağlı. İki noktanın uyuşması bana yayla (plato) gibi
göründü, oysa üçüncü nokta öyle olmadığını gösterdi. Ders: iki nokta
yakınsama iddiası için yeterli değil.

### Ne olduğu ölçüldü, sebebi bulunamadı

Ölçerek **elenenler**:

| aday | ölçüm | sonuç |
|---|---|---|
| basınç alanı | C_D basınç farkı 0,000% | elendi |
| duvar uzaklığı | yüz yüze oran 1,00000000 | elendi |
| girdap viskozitesi alanı | max nut 1,6858e−4 / 1,6860e−4 | elendi |
| yakınsama | son iki yazım arası sürüklenme üçünde de +0,010% | elendi |
| açıklık hızı sızması | max\|Uz\| = 8,4e−17 (nk=2), 4,6e−07 (nk=5) | elendi |
| ikinci mertebeye düşme | 256/256, 512/512, 1024/1024 karşı hücre bulundu | elendi |
| alan ayrıştırması | üçünde de hierarchical (2 2 1), z'de bölmüyor | elendi |

**Bulunan.** Sapmanın tamamı sürtünmede ve duvara bitişik hücredeki teğet
hızda. 2-B'de bu hız yüzey boyunca **tekdüze azalıyor**:

    7,79 → 7,42 → 7,30 → 7,19 → 7,06 → 6,94 → 6,81   (×10⁻²)

3-B'de azalmıyor — **testere dişi** var:

    7,79 → 7,68 → 7,31 → 7,43 → 7,30 → 7,17 → 7,03   (nk=2)

Genlik ~%3,3, x ∈ [0,07, 0,13] aralığında, üst ve alt yüzeyde birebir
simetrik. İntegralde büyük ölçüde **birbirini götürüyor** (net +0,25%) ve
götürme nk arttıkça iyileşiyor: binde 1'i aşan yüz sayısı 58 → 53 → 16.

Sebebi bulunamadı. Testere dişinin 2-B'de hiç olmayıp 3-B'de çıkması,
z yüzlerinin ayrıklaştırmaya girmesiyle ilgili olmalı, ama hangi terim
üzerinden olduğu ölçülmedi. **Uydurma yapılmadı, olduğu gibi yazılıyor.**

### Sonuç: üreteç kullanılabilir, kaydıyla birlikte

nk=5'te 3-B kurulum, doğrulanmış 2-B sonucunu **binde 0,5 içinde** yeniden
üretiyor — ağ belirsizliğinin (GCI %1,29) yirmide biri. Kanat hesabına bu
kayıtla geçilebilir; 3-B sonuçları raporlanırken bu artık sapma ve testere
dişi belirtilmelidir.

### Ağ yığmanın kendisi bozulma katmıyor (ayrı kontrol)

Aynı ayarlarla (96×48×24, R=20) kurulan 2-B ve 3-B ağların `checkMesh`
çıktıları **on basamak birebir**: azami dikey olmayanlık 74,97839532,
azami çarpıklık 0,3463110026. Açıklık yönünde yığma, ağa ek bozulma
katmıyor. nk=5'te azami en-boy oranı da 2-B'nin değerine (4999,999887)
iniyor.

---

## VLM çapraz denetimi — kurulum ve bulunan kusur (02.09.2026)

3-B CFD'nin karşılaştırılacağı bağımsız araç `aero/vlm.py` (AeroSandbox
girdap-kafes). Kullanmadan önce **kendisi denetlendi** ve bir kusur çıktı.

### Çözünürlük yakınsamamıştı — ve bunu fiziği aşarak belli etti

Kodun kullandığı çözünürlük (52 şerit) açıklık verimini **e = 1,0067**
veriyordu. Düzlemsel bir kanatta e **1'i aşamaz**; eliptik yükleme tam 1
verir. Yani sonuç yakınsamamıştı ve bu, fiziksel sınırın aşılmasından
anlaşıldı.

Sebep: yakınsama sınaması **dikdörtgen AR=6 kanatta** yapılmış ve bu
planforma taşındığı varsayılmıştı. Taşınmıyor.

Gerçek planformda ölçüldü (veter çözünürlüğü 12 sabit, α = 4°):

| şerit | e | CL(4°) |
|---|---|---|
| 52 (eski varsayılan) | **1,0067** | 0,27044 |
| 104 | 0,9890 | 0,26988 |
| 216 | 0,9845 | 0,26946 |
| Richardson h→0 (p = 1,98) | **0,9830** | — |

Veter yönü de etkiliyor: 104 şeritte veter 12→24 ile e 0,9890 → 0,9936.
İki yön birlikte düşünüldüğünde **e ≈ 0,98–0,99**.

`CL_α` ise yakınsamış: 52 şeritte 3,874 /rad, 216 şeritte 3,842 /rad —
altı kat çözünürlükte %0,8 değişim. Gözlenen mertebe düşük (p = 0,42), o
yüzden Richardson değeri değil **ölçülen aralık** verilmelidir.

Varsayılan çözünürlük 104 şeride çıkarıldı; `yakinsama()` eklendi.

Makaledeki **0,85 varsayımı** karşısında ölçülen 0,98–0,99, kanadın
varsayılandan belirgin biçimde verimli olduğunu söylüyor — ama sayının
kendisi bu yakınsama kaydıyla verilmelidir.

### Kendi hesabımda işaret hatası (düzeltildi)

Richardson'u ilk yazışımda `f_ince − (f_ince − f_orta)/(r^p − 1)` kullandım;
doğrusu **artı**. Yanlış işaret, extrapolasyonu üç ölçümün de dışına
düşürdü (e için 0,986, CL için 0,27072) — dizi azalırken sınırın en küçük
değerin altında olması gerektiğinden yakalandı. Düzeltilmiş değerler
yukarıdadır.

---

## Gerçek planform ağı — 3-B normal boyunca yürüme UYGULANDI, İŞE YARAMADI (02.09.2026)

### İstenen yapıldı, ölçüldü, tutmadı

Kesit düzlemi yerine lofte edilmiş yüzeyin gerçek 3-B normali boyunca
yürüme uygulandı. `checkMesh` ile ölçüldü:

| yürüme doğrultusu | negatif hücre | azami dikey olmayanlık | çarpıklık |
|---|---|---|---|
| kesit düzlemi (2-B normal) | 35 890 | 180,0° | 43,8 |
| **gerçek 3-B yüzey normali** | **36 047** | 180,0° | **120,5** |
| bütün istasyonlarda ortak normal | 35 893 | 179,9° | 147,2 |

**Yürüme doğrultusu baskın etken değil.** Üçü de aynı mertebede kötü.
3-B normal çarpıklığı üç kat artırdı: eğim yalnızca profil bölgesinde ve
yalnızca iç istasyonlarda verildiği için iz kesiği ekleminde ve kök/uç
düzlemlerinde sıçrıyor. Varsayılan `kesit`e geri alındı; seçenek kodda
kayıt olarak duruyor.

Düz kanat regresyonu korundu: sabit kesitte 3-B normal 2-B'ye indirgeniyor,
z hiç kaymıyor.

### Vekil ölçütüm yanıltmıştı — düzeltme

Önceki ayrıştırmayı kendi tetrahedral hacim işlevimle yapmıştım.
`checkMesh` ile tekrarlandı; **sıralama doğru, büyüklükler yanlıştı**:

| değişen | benim vekil ölçütüm | checkMesh |
|---|---|---|
| düz | 0 | 0 |
| ok açısı | 0 | 0 |
| sivrilme | 0 | 15 |
| kalınlık | 3582 | **25 294** |
| gerçek planform | 3398 | 24 185 |

Sonuç aynı — kusuru doğuran kalınlık değişimi — ama ölçüt artık doğru.

### Mekanizma kuruldu ve ÖNGÖRÜ TUTTU

Duvar yüzünün çarpıklığı ≈ |∂²y/∂x∂z|·Δx·Δz = 1,57e−4; duvar hücresi
y⁺=1'de 8,9e−6. Oran **17,6** — yüz, hücrenin kendi yüksekliğinin 18 katı
kadar çarpık. Hücre bu durumda kaçınılmaz olarak bozulur, **yürüme
doğrultusundan bağımsız olarak** (üç seçeneğin de aynı çıkması bundan).

Koşmadan önce yazılan öngörü: duvar aralığı ~59 kat büyütülürse (y⁺≈60)
çarpıklık hücre yüksekliğinin 0,3'üne iner ve negatif hücreler kaybolmalı.

| y⁺ | negatif hücre |
|---|---|
| 1 | 24 185 |
| 10 | 902 |
| 30 | 27 |
| 60 | **22** |
| 120 | 22 |

Üç mertebe düştü. **Mekanizma doğrulandı.**

### Kalan kusur — AÇIKLANAMADI

22'de plato yapıyor, sıfırlanmıyor. Ayrıca y⁺=60'ta bile yüzlerin **%23'ü**
70°'yi aşıyor ve azami dikey olmayanlık 155,7°'de çakılı. İstasyon sayısı
13→25→49 yapıldığında bu **hiç değişmiyor** (şiddetli yüz oranı sabit) —
yani açıklık çözünürlüğü değil.

Denenip **ölçümle elenen** hipotezler:

| hipotez | sonuç |
|---|---|
| duvar aralığını bütün istasyonlarda sabitlemek | KÖTÜLEŞTİ (6351→11 283) |
| veter dağılımını tek kesitten üretmek | kısmen iyileştirdi (28 325→24 185) |
| 3-B yüzey normali boyunca yürümek | KÖTÜLEŞTİ (çarpıklık 44→120) |
| iz/hücum kenarı aralıklarını mutlaklaştırmak | KÖTÜLEŞTİ (sivrilme 15→75) |
| açıklık istasyonunu artırmak | ETKİSİZ |

Dördü de yanlış çıktı ve dördü de kayda geçti. **Gerçek planform hesabı
koşulmayacak** — bozuk ağdan sayı üretilmez.

### Şiddetli yüzler nerede — çıkarıldı (02.09.2026)

`checkMesh`'in yazdığı yüz kümeleri (`nonOrthoFaces`, `skewFaces`,
`wrongOrientedFaces`) polyMesh'ten okunup her yüzün **merkezi ve normali**
hesaplandı. Sonuç iki ayrı problem gösterdi.

**(A) Şiddetli dikey olmayanlığın %98'i AÇIKLIK yüzü ve UZAK ALANDA.**
Veter ortasından ortanca uzaklık **29 veter**, x ortancası −11, %95'i 62
verete kadar. Kanadın yanında değil.

**(B) Negatif hücreler ve yanlış yönlü yüzler DÜZLEM İÇİ ve UÇTA.**
x ∈ [1,56 – 1,77], z ∈ [1,22 – 1,65]. Yarı açıklık 1,73, uç veteri
1,54'ten 1,78'e. Yani hepsi **açıklığın dış %25'inde, kanadın üstünde**.

#### (A) çözüldü — iki etki bağımsızmış

(A)'nın sebebi radyal dağılımın istasyonlar arasında uyuşmaması: `dy`
vetere göre ölçeklendiğinde kökte 8,6e−6, uçta 2,1e−6'dan başlayıp ikisi
de 100'e ulaşıyor, dolayısıyla **aynı j farklı yarıçapa** düşüyor.

| yapılandırma | negatif | şiddetli yüz |
|---|---|---|
| dy ölçekli, y⁺=60 | 24 | 112 228 |
| **dy sabit, y⁺=60** | 29 | **7 274** |

**15 kat düşüş.** Bu, önceki "dy_sabit kötüleştirdi" kaydımı düzeltiyor:
onu y⁺=1'de ölçmüştüm, orada duvar çarpıklığı her şeyi bastırıyordu. İki
etki bağımsız — y⁺ duvarı, `dy_sabit` orta/uzak alanı düzeltiyor.

Uzak alan merkezini mutlaklaştırmak ayrıca denendi; tek başına %6 kazandırdı
(119 650 → 112 228), kalıcı olarak açık bırakıldı.

#### (B) çözülemedi

Uçta veter 0,236, kökte 0,97; açıklık adımı sabit olduğu için Δz/c oranı
0,15'ten 0,61'e çıkıyor ve son iki istasyon arasında veter %26 değişiyor.
İstasyonları uca doğru sıklaştırmak denendi: Δz/c gerçekten sabitlendi
(0,272–0,280) ama **kötüleşti** — negatif hücre 29 → 211. Muhtemelen Δz/c'yi
sabitlemek kök tarafında Δz'yi büyütüp kusuru oraya taşıyor.

#### Ölçülen en iyi yapılandırma

`dy_sabit=True`, mutlak uzak alan, tekdüze istasyon, y⁺=60:
**29 negatif hücre, 10 329 şiddetli yüz (%0,6), azami 155,8°.**
Hâlâ `Mesh OK` değil — 29 negatif hücre çözümü engeller.

#### Ölçümle elenen hipotezler (toplam beş)

| hipotez | sonuç |
|---|---|
| sabit duvar aralığı (y⁺=1'de) | kötüleşti — ama y⁺=60'ta 15 kat İYİLEŞTİRDİ |
| 3-B yüzey normali boyunca yürüme | kötüleşti (çarpıklık 44→120) |
| iz/hücum kenarı aralıklarını mutlaklaştırma | kötüleşti (15→75) |
| açıklık istasyonunu artırma | etkisiz |
| uca doğru sıklaştırma | kötüleşti (29→211) |

---

## Uç kapanışı — karar verildi ve kuruldu (02.09.2026)

### Karar: düz uç kapağı

- Uç veteri **sıfır değil** (0,2364). Sivri ya da yuvarlatılmış uç, olmayan
  bir geometri uydurmak olurdu.
- Düz kapak sonlu kanat için yerleşik işlemdir; ONERA M6 doğrulama vakası
  bunu kullanır — ileride dış veriyle karşılaştırma yolu açık kalır.
- VLM çapraz denetimi (CL_α, e) ancak gerçek sonlu kanatta anlamlıdır;
  uca simetri düzlemi koymak sonsuz kanat modellemek olurdu.

**Kapsam dışı, açıkça:** patentteki **uç iskeletleri** (parça 3, planform
düzlemine dik yukarı ve aşağı uzanan) modellenmiyor. Uç akışını esaslı
biçimde değiştirirler. Bu ilk 3-B vaka "uç iskeletsiz kanat"tır.

### Topolojinin gerektirdiği

Uçtan **dışarıda** da akış vardır ve profil deliği orada kapanmalıdır. Tek
bloklu C-ağı yığını bu topoloji değişimini ifade edemez. Eklenen:

1. Uç düzleminden dışarı `n_uc` istasyon (hepsi uç kesiti geometrisiyle;
   orada profil çizgisi artık duvar değil **iç** çizgidir).
2. Profil kesitini dolduran bir **iç blok** (H-ağı). Alt yüzeydeki m'inci
   nokta ile üst yüzeydeki NF−m'inci nokta aynı x'te (ölçüldü: 65
   indeksin 65'i), dolayısıyla ikisi arası düzgün bölünebiliyor.
3. Bu iç bloğun **uç düzlemindeki tabanı kapak duvarıdır**.
4. Hücum ve firar kenarında alt ile üst aynı noktaya düştüğü için oradaki
   hücreler **prizma** olarak yazılıyor (tekrar eden düğümle hexa yazmak
   sıfır alanlı yüz üretirdi).

`gmshToFoam` topolojiyi kabul etti: 1 065 600 hexa + 384 prizma, 6 yama.

### Bu turda bulunan iki gerçek kusur

**(1) Kıymık istasyon.** `gercek_istasyonlar` ince listeyi dilimleyip son
istasyonu ayrıca ekliyordu; bölme tam gelmediğinde en sonda **8 kat ince**
bir aralık kalıyordu (0,0173'e karşı 0,142) — ve tam **uçta**. Ara
değerlemeyle giderildi (Δz oranı 8,2 → 1,00). *Temel ağdaki 29 negatif
hücreyi değiştirmedi*, yani kusurların sebebi bu değilmiş; düzeltme yine
de doğru.

**(2) Kapak bloğunun sarım yönü tersti.** Sarım `+m` sonra `+q` idi;
(+m)×(+q) ekseni −z'ye bakıyor, oysa hücrenin üstü +k = +z. Bütün kapak
hücreleri **sol elli** çıkıyordu.

| | negatif hücre | çarpıklık |
|---|---|---|
| ters sarım | 462 | 3,9e15 |
| **düzeltilmiş** | **101** | 162 |

### Kalan kusur — yeri kesin, sebebi yapısal

Kapaklı ağ 101 negatif hücre veriyor; kapaksız temel 29. Fazladan 72
hücre **kapak çözünürlüğünden tamamen bağımsız** (n_kapak = 4, 8, 16, 32 →
hepsi 101), yani kapak H-ağının içinde değil.

Yerleri çıkarıldı: **x ≈ 1,78** (uç kesitinin firar kenarı 1,775),
z ortanca 2,2–2,7, %95'i 13,8–18,8 — yani **uç firar kenarından dışarı
uzanan iz kesiği çizgisi boyunca**.

Sebep yapısal: orada üç şey aynı çizgide buluşuyor — kapağın **çöken firar
kenarı** (kapalı FK olduğu için nokta), **iz kesiği** (üst ve alt düğümler
birleşik) ve halka bloğu. Tekil bir çok-blok eklemi. Kapalı firar kenarı
korunduğu sürece herhangi bir iç ağ orada çökmek zorunda.

Bunu aşmak topoloji kararı gerektirir (uçta C→C-O ya da H-O geçişi, ya da
firar kenarını açık bırakıp iz kesiğini ona göre kurmak). **Uydurma
yapılmadı; ağ geçerli değil, geçerli olmadığı yazılıyor ve gerçek planform
hesabı koşulmuyor.**

### Açık firar kenarı denendi — ölçüldü, İŞE YARAMADI (02.09.2026)

Kapağın çöken firar kenarı ile iz kesiğinin aynı çizgide buluşmasını
çözmek için firar kenarı açık bırakıldı.

**Fikir topolojik olarak doğru ve değişiklik küçük.** Açık firar
kenarında profilin ilk noktası (1,−δ), son noktası (1,+δ) ve **ayrıdır**;
kapak bloğunun m=0 kenarı artık çökmez. İz kesiği zaten (1+fk, 0)'dan
başlıyordu ve orada birleşmeye devam eder — C-ağı kapalı kalır, sivri
nokta yalnızca (1,0)'dan (1+fk,0)'a kayar. Ölçüldü: **prizma sayısı
384 → 192**, yani firar kenarı çökmesi gerçekten kalktı.

Ama toplam kötüleşti:

| yapılandırma | kapaksız negatif | kapaklı negatif | şiddetli yüz |
|---|---|---|---|
| **kapalı FK** | **29** | **101** | **13 837** |
| açık FK, fk = 2e−4 | 104 | 234 | 22 711 |
| açık FK, fk = δ | 70 | 176 | 79 881 |

**Neden.** İz kesiğinin ilk hücresi 2e−4 veter (kapalı, sivri firar
kenarı için seçilmişti); açık firar kenarının yarı kalınlığı δ ise t/c
0,12'de 1,26e−3, 0,25'te 2,6e−3. Profilin ilk noktası (1,−δ) ile ondan
önceki iz noktası (1+fk, 0) arasındaki kenar **6 ilâ 13 kat dik** çıkıyor
ve oradaki hücre aşırı çarpık oluyor. `fk` δ'ya eşitlenip kenar ~45°'ye
getirildi: negatifler düzeldi (104 → 70) ama bu sefer iz dağılımı
kabalaşıp şiddetli yüzler patladı (13 672 → 71 429).

İki gereksinim çelişiyor: `fk` küçük olmalı (iz çözünürlüğü için) ve δ
kadar olmalı (firar kenarı köşesi için).

**Doğrusu ne olurdu.** Firar kenarı tabanının profile DÂHİL edilmesi:
iç eğri, iz kesiğinin taban orta noktasından başlayıp tabanın alt yarısı
→ alt yüzey → hücum kenarı → üst yüzey → tabanın üst yarısı → iz kesiği
diye kurulmalı. Bu, doğrulanmış iki boyutlu üretecin iç eğri kuruluşunu
ve `profil_x` gösterimini değiştirmeyi gerektirir — yani 2-B doğrulama
zincirini yeniden koşmayı. Yapılmadı.

Varsayılan **kapalı**ya geri alındı; seçenek ölçülmüş kayıt olarak kodda.

### Uç kapanışının şu anki durumu

En iyi ölçülen: kapalı FK + düz uç kapağı → **101 negatif hücre**
(kapaksız temel 29). `Mesh OK` değil. Gerçek planform hesabı hâlâ
koşulmuyor.
