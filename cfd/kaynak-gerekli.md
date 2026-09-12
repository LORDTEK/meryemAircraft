# Doğrulama için gereken kaynaklar

Bu oturumun çalıştığı ortamda dış ağ erişimi kapalı: `turbmodels.larc.nasa.gov`,
`ntrs.nasa.gov`, `reports.aerade.cranfield.ac.uk`, `semanticscholar.org` —
hepsi çıkış politikasınca engellendi. Yalnız paket depoları ve GitHub raw açık.

Bu, yapılabilenle yapılamayanı net biçimde ayırıyor:

| | dış veri gerekir mi | durum |
|---|---|---|
| Ağ bağımsızlığı | hayır | yapılıyor |
| y+ duyarlılığı | hayır | yapılabilir |
| Alan boyutu duyarlılığı | hayır | yapılabilir |
| Türbülans modeli duyarlılığı | hayır | yapılabilir |
| Şema mertebesi duyarlılığı | hayır | yapılabilir |
| **Deneyle karşılaştırma** | **evet** | **bekliyor** |

İlk beşi *denetimdir* (verification): çözümün kendi içinde tutarlı ve
çözünürlükten bağımsız olduğunu gösterir. Sonuncusu *doğrulamadır*
(validation): çözümün gerçeği verip vermediğini gösterir. İkisi aynı şey
değildir ve ikincisi olmadan "çözücümüz doğrulandı" denemez.

Projenin kuralı gereği sayısal karşılaştırma yalnızca **birinci elden
okunan** kaynağa bağlanır. Aşağıdaki iki dosya depoya girerse 1. basamak
tamamlanır.

## 1. Ladson (1988) — birincil deney verisi

> Charles L. Ladson, *Effects of Independent Variation of Mach and Reynolds
> Numbers on the Low-Speed Aerodynamic Characteristics of the NACA 0012
> Airfoil Section*, NASA TM 4074, 1988.

https://ntrs.nasa.gov/api/citations/19880019495/downloads/19880019495.pdf

Langley düşük türbülanslı basınçlı tünel. Re = 3–12 × 10⁶, Mach 0,05–0,36,
geçiş tetiklenmiş. Bizim ihtiyacımız: **Re = 6 × 10⁶, düşük Mach**'ta
C_D ve C_L'in hücum açısıyla değişimi — özellikle α = 0'daki C_D.

Not: Ladson'ın en düşük Re'si 3 × 10⁶. Bizim aracımızın kök Re'si
2 × 10⁶, uç Re'si 4,9 × 10⁵. Yani bu kaynak *çözücüyü* doğrular, aracın
çalıştığı Re aralığını değil. Bu ayrım ikinci makalede açıkça yazılmalı.

## 2. NASA Türbülans Modelleme Kaynağı — referans CFD

https://turbmodels.larc.nasa.gov/naca0012_val.html
https://turbmodels.larc.nasa.gov/naca0012numerics_val.html

Aynı vakanın CFL3D ve FUN3D ile, ağ seviyelerine göre çözülmüş sonuçları.
Bize iki şey verir: (a) yerleşik iki çözücünün aynı vakada ne verdiği,
(b) onların ağ yakınsama davranışı — bizimkiyle karşılaştırılacak.

Sayfaların HTML'i ya da PDF çıktısı yeterli.

## 3. Kalın kesit verisi — YENİ, ve artık öncelikli

Bu, çalışma sırasında ortaya çıktı. Kök kesitimiz %25 kalınlığında ve
orada **kararlı RANS yakınsamıyor**: akış kararsız, firar kenarı ayrılması
salınıyor (`cfd/README.md`, 2. basamak). Zamana bağlı çözüme geçildi ama
onu doğrulayacak deney verisi yok.

> Eastman N. Jacobs, Kenneth E. Ward, Robert M. Pinkerton, *The
> Characteristics of 78 Related Airfoil Sections from Tests in the
> Variable-Density Wind Tunnel*, NACA Report 460, 1933.

https://ntrs.nasa.gov/citations/19930091108

NACA 0006'dan **0025'e** kadar simetrik kesitlerin C_D verisini içerir —
yani tam olarak bizim kalınlık taramamızın kapsadığı aralık. Bir uyarı:
değişken yoğunluklu tünelin türbülans düzeyi yüksekti ve sonuçlar
"etkin Reynolds sayısı" düzeltmesiyle verilir; bu düzeltmenin nasıl
uygulandığı raporun kendisinde yazılıdır ve birinci elden okunması gerekir.

Bu dosya şunu çözer: **kalınlıkla C_D'nin nasıl arttığı ölçülmüş mü, ve
bizim %12 → %18 → %25 eğilimimiz ona uyuyor mu?**

## 4. İsteğe bağlı — ikinci bağımsız deney

> N. Gregory, C. L. O'Reilly, *Low-Speed Aerodynamic Characteristics of NACA
> 0012 Aerofoil Section, including the Effects of Upper-Surface Roughness
> Simulating Hoar Frost*, ARC R&M 3726, 1970.

https://reports.aerade.cranfield.ac.uk/bitstream/handle/1826.2/3003/arc-rm-3726.pdf

Re = 3 × 10⁶. Tek bir deneye dayanmamak için ikinci bir ölçüm iyi olur;
zorunlu değil.

## Nereye

`cfd/kaynak/` altına, indirildiği adı bozmadan. Sonra `cfd/veri/`
içine sayısal tablolar çıkarılır ve `cfd/dogrula.py` karşılaştırmayı yapar.

## Bir uyarı

Bu verilerin GitHub'daki çeşitli CFD depolarında kopyaları var. Onlar
**kullanılmayacak**. Bu proje daha önce arama motoru özetlerinden gelen üç
yanlış sayıyı birinci el okumayla yakaladı (`makale/kaynaklar.md`); ikinci
elden aktarılmış bir tabloya çözücü doğrulaması bağlamak aynı hatayı
tekrarlamak olur.

---

# Tur 14 — çift taraflı şerit için indirilecekler (S9)

**Ne arıyoruz.** Tek kanat yarısında, **üstte ve altta eşit çıkıntı** yapan bir
şeridin ürettiği yuvarlanma momenti ve yunuslama momenti. NACA TR-796 (1944)
bu düzeneği tek taraflı spoiler'ın "prohibitive" yunuslama momentine çare
olarak **öneriyor** ama "veri yetersiz" diyor. Şimdiye kadar aradığımız yerde
(NACA/NASA raporları) bulamadık.

**Neden bulamadık.** Yanlış isimle arıyorduk. Bu cihazın modern adı
**split drag rudder** — bazen *drag rudder*, *split flap*, *split aileron*,
*deceleron*. B-2'de, YB-49'da, X-47B'de bu var. Yani TR-796'nın önerdiği
düzenek gerçekten kuruldu, uçtu ve ölçüldü; NACA raflarında değil, çağdaş
uçan-kanat literatüründe.

**Dikkat — cihaz aynı, amaç farklı.** Yayınların neredeyse tamamı bunu bir
**yaw** cihazı olarak karakterize ediyor (sürükleme farkıyla dönüş), bizimki
ise bir **roll** cihazı (kaldırma bozarak yatış). Aradığımız sayı onların
yan ürünü. Bu yüzden özetlere bakmak yetmez, **tabloya** bakmak gerek.

## İndirilecekler — öncelik sırasıyla

**1. DLR-F19 / SAGITTA kontrol cihazı çalışması** — tek taraflı ve çift taraflı
spoiler'ı, wingtip flap'i ve **split flap**'i aynı modelde karşılaştırıyor.
Bizim sorumuza en yakın olan bu.

> Liersch, C. M. et al. *Control device effectiveness studies of a 53° swept
> flying wing configuration. Experimental, computational, and modeling
> considerations.*
> https://elib.dlr.de/128954/

Bu adres benim ortamımda **bloklu**, açamadım. Sizde açılıyorsa PDF'i indirin.
Açılmazsa aynı çalışmanın rüzgâr tüneli raporu:

> *Wind Tunnel Report TN2621: Static Force, Moment, Surface Pressure and PSP
> Measurements on the DLR-F19 Configuration including Spoiler Geometries and
> Control Surfaces.*
> https://elib.dlr.de/110803/

**2. Split drag rudder'ın kanat açıklığı boyunca yerleşimi** — başlığında
doğrudan "rolling and yawing moments" geçiyor, yani aradığımız eşleşmeyi
veriyor olabilir.

> *Investigating the effect of the placement of the split drag rudder control
> system along the wing span of a flying wing aircraft on rolling and yawing
> moments.*
> researchgate.net/publication/369857093

**3. Farklı hücum açılarında split drag rudder** — bizim için kritik olan
α bağımlılığını veriyor olabilir. Geçiş sırasında 17–22°'ye çıkıyoruz.

> *Optimization of split drag rudder mechanism at different angles of attack in
> a flying wing airplane.*
> researchgate.net/publication/366325121

**4. Yedek** — aynı ailenin daha eski ve daha genel iki incelemesi:

> *Control features and application characteristics of split drag rudder
> utilized by flying wing.* researchgate.net/publication/286967038
> *Control Characteristics Analysis of Split-Drag-Rudder.*
> researchgate.net/publication/271977076

## Ne aranacak — açtıktan sonra

PDF'i açınca **üç sayı** arayın, ve bulduğunuz **cümleyi** getirin, özeti değil:

1. **ΔC_l** (yuvarlanma momenti katsayısı) çıkıntı yüksekliğine karşı.
   Bizim ihtiyacımız ΔC_L ≈ 0,12 eşdeğeri.
2. **ΔC_m** (yunuslama momenti) — çift taraflı düzenekte gerçekten iptal
   oluyor mu, ve ne kadar?
3. **Hücum açısı bağımlılığı.** Arama özetleri, yuvarlanma momentinin α ile
   **işaret değiştirdiğini** ima ediyor: α arttıkça alt kanadın profil
   sürüklemesi artıp üstünki azalıyor, cihaz aşağı kırılmış bir aileron gibi
   davranmaya başlıyor. **Bu doğruysa bizim aleyhimize**, çünkü geçişte tam o
   bölgedeyiz. Ben bunu doğrulamadım — özetten okudum, PDF'den değil.

## Uyarı, bir kez daha

Yukarıdaki üç imanın **hiçbirini açmadım**. Bunlar arama sonucu başlıkları ve
arama motoru özetleri. Bu projede daha önce iki kez, teklif edildiği şeyin
tersini söyleyen kaynak geldi. Bu liste bir **arama yönü**dür, atıf değildir;
hiçbiri okunmadan makaleye girmeyecek.
