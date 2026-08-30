# CFD — ikinci makalenin zemini

`aero/` girdap-kafes ve şerit yöntemiyle, makalenin varsaydığı iki katsayıyı
**sınırladı**. O kurulumun kendi kaydettiği en zayıf halkası şuydu:

> **Gövde bir profil değildir.** Şerit yöntemi kök kesitini %25 kalınlığında
> iki boyutlu bir NACA profili gibi ele alıyor. Kanat-gövde merkez gövdesinde
> akış iki boyutlu değildir.

Bu dizin o halkayı hedefliyor. Sorusu dar ve tek: **merkez gövdenin sıfır
kaldırma sürüklemesi, iki boyutlu şerit kuramının verdiği değere ne kadar
yakın, ve hangi yönde sapıyor?**

## Uçuş koşulu

Planformdan (`aero/planform.py`) türetilen değerler:

| | |
|---|---:|
| kök veteri | 0,970 m |
| uç veteri | 0,236 m |
| ortalama veter | 0,573 m |
| seyir hızı | 30 m/s |
| Mach | **0,088** — sıkıştırılamaz |
| Re (kök) | 2,0 × 10⁶ |
| Re (ortalama veter) | 1,2 × 10⁶ |
| Re (uç) | **4,9 × 10⁵** |

Uçtaki Re, `cd0.py`'de seçilen *tetikli geçiş* varsayımını destekliyor:
5 × 10⁵ civarında doğal geçiş yeri yüzey durumuna aşırı duyarlıdır, o yüzden
onu serbest bırakmak iyimserlik olur.

## Basamaklar

Doğrulama önce gelir. Sıra bilinçli:

1. **NACA 0012, iki boyutlu** — çözücünün, ağın ve kuvvet hesabının bilinen
   bir hâlde ne verdiği. Ağ bağımsızlığı, y+ ve türbülans modeli duyarlılığı
   burada ölçülür.
2. **Kalın kesit, iki boyutlu** — aynı kurulum, %25 kalınlıkta. Bu bir
   doğrulama değil: `cd0.py`'nin kullandığı NeuralFoil/XFOIL ile RANS'ın,
   şerit kuramının şüpheli olduğu kalınlıkta **ne kadar ayrıştığını** ölçer.
3. **Üç boyutlu merkez gövde** — asıl soru. 1 ve 2'nin verdiği güven payıyla.

Şu an **1. basamaktayız.**

## Araçlar ve iki engel

Çözücü: **OpenFOAM v1912** (Ubuntu paketi), `simpleFoam`, k-ω SST, sınır
tabakası çözümlenmiş (y+ ≈ 1, duvar fonksiyonu yok). 4 çekirdek, 15 GB.

Bu ortamda iki engele çarpıldı; ikisi de kayda geçiyor, çünkü sonucun nasıl
üretildiğini değiştiriyorlar.

**1. Fonksiyon nesnelerinin hiçbiri çalışmıyor.** `forceCoeffs`, `forces`,
`yPlus`, hatta `writeObjects` — hepsi `OSHA1stream` üzerinde
`error in IOstream "sha1"` verip çıkıyor. Kusur vakada değil kurulumda: stok
bir vakada da aynı sonuç alınıyor. Daha yeni bir OpenFOAM kurmak da mümkün
değil (aşağıya bakınız). Bu yüzden **katsayılar ve y+, çözümden sonra
yazılmış alanlardan `ortak/kuvvet.py` ile hesaplanıyor** — basınç kuvveti
∫p·S_f, kayma gerilmesi ν_eff·|U_t|/d. Yöntem `ortak/kuvvet.py`'nin
başında açık yazılıdır.

Bu, projenin geri kalanıyla tutarlı: `dogrula.py` de makalenin her sayısını
kendi denklemleriyle bağımsız yeniden hesaplıyor.

**2. Dış ağ erişimi kapalı.** `turbmodels.larc.nasa.gov`, `ntrs.nasa.gov`,
`reports.aerade.cranfield.ac.uk`, `semanticscholar.org`, `dl.openfoam.com` —
hepsi ortamın çıkış politikasınca engellendi. Yalnız paket depoları ve
GitHub raw açık.

Bunun sonucu şudur: **1. basamağın deneyle karşılaştırması bu oturumda
yapılamaz.** Ağ bağımsızlığı, y+ duyarlılığı, alan boyutu ve model
duyarlılığı — bunların hepsi dışarıdan veri gerektirmez ve yapılabilir; ama
bunlar *doğrulama* değil **denetimdir** (verification). Doğrulama için
birinci elden okunmuş deney verisi gerekir ve projenin kuralı bu:
sayısal iddialar yalnızca birinci elden okunan kaynaklara bağlanır.
Gerekli iki kaynak `kaynak-gerekli.md`'de yazılıdır.

## Ağ üreteci

`ortak/cagi.py` — iki boyutlu yapısal C-ağı, gmsh 2.2 → `gmshToFoam`.

Neden hazır ağlayıcı değil: sürükleme, duvar kayma gerilmesinin yüzey
üzerindeki integralidir; duvara komşu hücrenin yüzeye **dik** olması
doğrudan doğruya sonucun doğruluğudur. `blockMesh`'in düz kenarları bu
dikliği vermez, `snappyHexMesh` ise sınır tabakası katmanlarını yamalı
bırakır.

Temel ağın ölçülmüş nitelikleri (385 × 97 düğüm, 36 864 hücre):

| | |
|---|---:|
| ters dönmüş hücre | **0** |
| duvarda diklikten sapma | ortalama 0,87° · en fazla 3,50° |
| ortogonallik (checkMesh) | ortalama 10,5° · en fazla 57,9° |
| çarpıklık (checkMesh) | 0,32 |
| en-boy oranı | 5 000 ile sınırlı |

Üretim sırasında üç kusur bulunup düzeltildi; üçü de kodda gerekçesiyle
kayıtlı:

- Dış sınır noktaları iç eğrinin dağılımını miras alınca firar kenarında
  üst üste biniyor, ışınsal çizgiler orada buluşup hücreyi ters çeviriyordu
  (`_taban`).
- Firar kenarında normal alanı **süreksiz**: iz kesiğinin normali dikey,
  alt yüzeyinki ~8° yatık, aradaki hücre 2×10⁻⁴ veter. Yumuşatma yalnızca
  firar kenarı penceresine uygulanıyor — baştan sona uygulamak hücum
  kenarında duvar dikliğini 0,4°'den 10°'ye bozuyor (ölçüldü).
- İlk yürüme formülü `f(1−f)` terimini 20 veterlik uzaklıkla çarpıyor,
  alanın ortasında 5 vetere varan yer değiştirme üretiyordu. Yerine geçiş
  sabit bir fiziksel uzunlukta yapılıyor.

## Betikler

| Betik | Ne yapar |
|---|---|
| `ortak/cagi.py` | İki boyutlu yapısal C-ağı → gmsh `.msh` |
| `ortak/foamoku.py` | Küçük OpenFOAM ASCII okuyucu (polyMesh + alanlar) |
| `ortak/kuvvet.py` | C_L, C_D ve **ölçülmüş** y+ — yazılmış alanlardan |
| `naca/kur.py` | Eksiksiz `simpleFoam` vakası kurar |
| `naca/kos.sh` | Çevirir, `checkMesh`, çözer |

Ölçekleme: veter = 1 m, U = 1 m/s, ρ = 1, ν = 1/Re. Katsayılar doğrudan
çıkar. Hücum açısı **ağı döndürmez**, serbest akış vektörünü döndürür:
bütün açılar tek ağda çözülür, aradaki farklar ağdan değil akıştan gelir.

## İlk sonuç

NACA 0012, Re = 6 × 10⁶, α = 0°, 400 yineleme (henüz yakınsamamış):

| | |
|---|---:|
| C_L | **−0,000004** |
| C_D | 0,007621 |
| — basınç | 0,001235 |
| — viskoz | 0,006387 |
| y+ | ortalama 0,93 · en fazla 1,43 |

C_L'in sıfır çıkması tesadüf değil, **kontroldür**: simetrik profil sıfır
hücum açısında sıfır kaldırma verir. Ağ simetrisini, çözücüyü ve kuvvet
integralini aynı anda sınar. y+ ise varsayılmıyor, ölçülüyor.
