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

## Elenen açıklama: duvar işlemi

`naca/sst_kurulum.py`, SST'ye özgü duvar koşullarını tek tek değiştiriyor.

| varyant | C_D | değişim |
|---|---:|---:|
| taban (mevcut kurulum) | 0,007691 | — |
| ω duvar fonksiyonu harmanlamasız | 0,007685 | −%0,08 |
| ν_t duvarda `calculated` | çözülemedi | — |
| k duvarda `kLowReWallFunction` | 0,007691 | %0,00 |
| ω duvarda ders kitabı 6ν/(β₁y²) | (koşuyor) | |

İlk hücrede ω zaten tam olarak 6ν/(β₁y²)'ye eşit (ölçüldü: 6,713e5'e
karşı 6,713e5), yani duvar fonksiyonu doğru değeri koyuyor. Harmanlama ve
k koşulu sonucu değiştirmiyor.

## Sırada

- **Düz levha** (`levha/duzlevha.py`): sıfır basınç gradyanında log
  tabakası dengesi. Yukarıdaki 0,88'in model kusuru mu yoksa ters
  gradyanın fiziği mi olduğunu ayıran sınama. Beklenti önceden yazılı.
- **Geometri** (`naca/tmr_geo.py`): TMR'ın kendi %11,894 profiliyle iki
  model. Bizimki %12, yani ~%0,9 daha kalın; bu ortak bir yanlılık üretir
  ve kaldırılmadan modele özgü kusur doğru ölçülemez. Beklenti önceden
  yazılı.

### Elde olmayan kaynak

`turbmodels.larc.nasa.gov/naca0012numerics_val_sa.html` sayfası indirildi
(`kaynak/naca0012_val.html`) ama dosyada yalnızca NASA sitesinin gezinme
menüsü var — sayısal veri yok, sayfa içeriği sonradan yükleniyor olmalı.
`kaynak/` altındaki üç "Print To PDF" dosyası da salt görüntü; metin
katmanı taşımıyorlar. Yani bu üç dosyadan hiçbir sayı okunamadı ve
hiçbiri bir sayısal iddianın dayanağı değildir.
