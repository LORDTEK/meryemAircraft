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

## 3. İsteğe bağlı — ikinci bağımsız deney

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
