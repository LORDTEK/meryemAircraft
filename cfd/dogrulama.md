# Doğrulama — çözücü gerçeği veriyor mu?

Bu dosya `cfd/README.md`'deki **denetimden** ayrıdır ve ayrı kalmalıdır.
Denetim, çözümün kendi içinde tutarlı ve çözünürlükten bağımsız olduğunu
gösterir. Doğrulama, çözümün **gerçeği** verip vermediğini gösterir.
İkincisi olmadan "çözücümüz doğrulandı" denemez.

Kaynaklar `cfd/kaynak/` altındadır ve depoya girmiştir. Sayılar
`cfd/veri/referans.py`'de, her birinin yanında nereden ve **nasıl**
okunduğu yazılı olarak durur.

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
| 5000 | 0,002954 | 0,002827 | **−%4,30** | −%0,22 | −%0,36 |
| 7000 | 0,002796 | 0,002669 | **−%4,54** | −%0,40 | −%0,53 |
| 9000 | 0,002679 | 0,002550 | **−%4,82** | −%0,43 | −%0,57 |
| 11000 | 0,002588 | 0,002481 | **−%4,13** | −%0,36 | −%0,67 |

Referansta iki model düz levhada **birbirinden %0,2–0,7 ayrılıyor.**
Bizde **%4,1–4,8.** Profildeki 9,4'lük ayrılmayla aynı yönde ve aynı
cinsten.

### Mutlak C_f'teki kayma bize ait, modele değil

Mutlak değerlerde SA'mız referansın %1,5–2,6 üstünde, SST'miz %1,5–2,9
altında. İkisi de Re_θ ile **aynı yönde** kayıyor (SA +1,5→+2,6, SST
−2,9→−1,5; ikisi de ~%1,2 artıyor). Ortak bileşen ikisini birden
etkileyen iki kurulum farkından geliyor ve dürüstlük gereği
kaldırılmamıştır:

- **Sıkıştırılabilirlik**: referans M = 0,2, bizimki sıkıştırılamaz.
- **Kapatma**: üst sınırımız H = 1 m'de kayma koşulu; levha boyunca
  dCp/dx = −0,0034 ölçüldü. Hafif elverişli gradyan sınır tabakasının
  iz bileşenini kısar, C_f'i biraz yükseltir, ve etkisi δ büyüdükçe
  büyür — ölçülen ortak eğilimin işareti ve gidişi bununla uyumlu.

Bu yüzden **mutlak C_f farkları modelin doğrulaması olarak okunmamalıdır**;
anlamlı olan iki model ARASINDAKİ fark, çünkü ortak bileşen ikisinde de
aynıdır. O fark referansta %0,4, bizde %4,5.

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

## Sıradaki şüpheli: kendi şema seçimimiz

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

## Sırada

- **Duvar ω taraması** (`levha/omega_duvar.py`): düz levhada iki onlu
  aralıkta duvar ω koşulu, yanında serbest akış ve ağ. Hedef **kesin ve
  dışarıdan ölçüm gerektirmiyor**: modelin kendi kapanış şartı
  ν_t = κu_τy. Beklenti önceden yazılı — oran 1,00'i kesiyorsa duvar
  işlemi bu açığı yönetiyordur; altı varyant da 0,86'da kalıyorsa kusur
  OpenFOAM'ın uygulamasındadır ve kaynağından okunmadan düzeltilemez.

### Elde olmayan kaynak

`turbmodels.larc.nasa.gov/naca0012numerics_val_sa.html` sayfası indirildi
(`kaynak/naca0012_val.html`) ama dosyada yalnızca NASA sitesinin gezinme
menüsü var — sayısal veri yok, sayfa içeriği sonradan yükleniyor olmalı.
`kaynak/` altındaki üç "Print To PDF" dosyası da salt görüntü; metin
katmanı taşımıyorlar. Yani bu üç dosyadan hiçbir sayı okunamadı ve
hiçbiri bir sayısal iddianın dayanağı değildir.
