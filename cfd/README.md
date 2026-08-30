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

## Sonuçlar

Tablolar `ozet.py`'nin çıktısıdır:

```
python3 cfd/ozet.py          # ekrana
python3 cfd/ozet.py --md     # markdown
```

Bu depoda daha önce makalenin 7.4'ündeki iki tablo bayat kalmış ve aynı
vaka iki yerde farklı sayılarla görünmüştü. `dogrula.py` onu yakaladı; o
günden beri kural şu: **bir sayı iki yerde duruyorsa, ikincisi elle
yazılmaz.**

Bütün katsayılar ikinci mertebe duvar gradyanıyla hesaplanmıştır.

### Kuvvet hesabının sınanması

`kuvvet.py` yük taşıyor (OpenFOAM'ın kendi aracı çalışmıyor), o yüzden
kendisi de sınandı — `kuvvet_sina.py`:

| sınama | sonuç |
|---|---|
| duvar yüzlerinin alanı ↔ profil çevresi | %0,003 |
| kapalı yüzeyin alan vektörü toplamı | 1 × 10⁻¹⁶ |
| C_L, simetrik profil α = 0 | −4 × 10⁻⁷ |
| y+ ölçülen ↔ hedeflenen | 0,93 ↔ 1,00 |
| dış sınırdan momentum dengesi | ağ inceldikçe yakınsıyor |

C_L'in sıfır çıkması bir sonuç değil **kontroldür**: ağ simetrisini,
çözücüyü ve kuvvet integralini aynı anda sınar.

## Üç kez yanılan şey, çözüm değil sınamanın kendisiydi

Bu kayda geçiyor çünkü üçü de aynı biçimde yakalandı — sayıya değil,
**eğilimin davranması gerektiği gibi davranıp davranmadığına** bakarak.

**1. Momentum dengesi.** İlk biçimi yalnızca `U(U·n) + p n` alıyordu.
Fark ağ inceldikçe **büyüyordu** (%11,6 → %15,4), oysa bağımsız bir
sınamadan beklenen tersi. Üç terim eksikti: Reynolds gerilmesinin
izotropik parçası (izde k ihmal edilemez), sınırdaki kayma, ve sahte
kütle kaynağı düzeltmesi — çözücü korunumlu yüz akısını korur, `U·S`'yi
değil. Eklendikten sonra %10,6 → %9,5.

**2. Alan boyutu.** İlk koşuda `n_normal` sabit tutuldu, dolayısıyla alan
büyüdükçe dış hücreler de gerildi; ölçülen şey saf alan boyutu değil,
alan boyutu **artı** bozulan uzak alan çözünürlüğü oldu. Belirti
sayılardaydı: fark her katlamada ~1 × 10⁻⁵ ile azalmıyordu, oysa uzak
alan hatası azalmalı. Büyüme oranı sabit tutulacak şekilde düzeltilince
20 → 50 veter farkı **+%0,16'dan −%0,08'e düştü ve işaret değişti** —
yani ilk ölçülen "alan etkisi"nin büyük kısmı sınamanın kendi kusuruydu.

**3. Richardson.** A ailesinde ilk hücre yüksekliği y+ = 1 hedefinden
geldiği için bütün seviyelerde sabit; ölçülen y+ bunu doğruluyor (0,96 /
0,92 / 0,93 / 0,96). Richardson tek bir `h` ölçüsü varsayar. Yine de
uygulanınca **p = 8,95** ve **GCI %0,02** çıkıyor — ikisi de sahte. İkinci
mertebeden bir şemadan 9. mertebe çıkmaz, ve GCI %0,02 "ağ hatası ihmal
edilebilir" diye okunurdu, oysa A2 ile A3 arasında C_D %6,3 değişiyor.
`yakinsama.py` artık bu ailede mertebe hesaplamayı reddediyor.

## Ağ yakınsaması hakkında söylenebilecek

B ailesi (düzgün inceltme) **salınımlı**: C_D düşüyor, düşüyor, sonra
yükseliyor. Ardışık farkların işareti değiştiği için resmî bir gözlenen
mertebe ve GCI **verilemez ve verilmeyecektir.**

Bileşenlere ayırınca salınımın yeri belli: basınç sürüklemesi düzgün
yakınsıyor, salınım tamamen **viskoz** kısımda.

İlk açıklama denemesi kısmen tuttu: duvar kayma gerilmesi birinci
mertebeden kestirildiğinde viskoz alt tabakadaki büküm görülmez ve
gradyan eksik çıkar; hata `d` ile orantılıdır. İkinci mertebe eklendi ve
düzeltme tam beklendiği gibi ölçeklendi — y+ 1,97'de %4,14, y+ 0,64'te
%0,03. Ama en ince iki ağda düzeltme ihmal edilebilir olduğu için
**B3 → B4 arasındaki %0,77'lik yükselişi açıklamıyor.** O yükseliş
çözümde, hesapta değil. Böylece kayma gerilmesi kestiriminin kendisi de
doğrulanmış oldu: y+ < 1'de mertebe seçimi sonucu değiştirmiyor.

Dürüst ifade: **C_D en ince üç ağda 0,00769 – 0,00781 bandında**, yani
yaklaşık ±%0,8. Bu bir GCI değildir.

## Bir yan bulgu: NeuralFoil'in geçiş sınırı

`cd0.py` NeuralFoil'e dayanıyor. Kalınlık çalışması için onu `xtr = 0`
ile çağırmak gerekti ve **çalışmadı**: verdiği C_D, xtr küçüldükçe önce
büyüyor, xtr ≈ 0,02'de tepe yapıyor, sonra düşüyor. Geçiş öne alındıkça
sürtünme monoton artmalı; bu fiziksel değil. NeuralFoil XFOIL üzerine
eğitilmiştir ve hücum kenarına çok yakın zorlanmış geçiş eğitim kümesinde
yok denecek kadar azdır.

| xtr | %12 | %18 | %25 | |
|---:|---:|---:|---:|---|
| 0,000 | 0,009502 | 0,010960 | 0,013055 | güvenilmez |
| 0,020 | 0,009992 | 0,011600 | 0,013804 | tepe, güvenilmez |
| 0,030 | 0,009881 | 0,011479 | 0,013663 | buradan sonra monoton |
| 0,050 | 0,009656 | 0,011221 | 0,013368 | **`cd0.py` bunu kullanıyor** |
| 0,200 | 0,008366 | 0,009512 | 0,011084 | |

`cd0.py`'nin kullandığı xtr = 0,05, güvenilmez bölgenin hemen üstünde.
Bu, aracın sınırına dair kendi başına bir bulgudur ve kalınlık
karşılaştırmasında yalnızca güvenilir bölgeden (xtr ≥ 0,03) geri atım
kullanılmasının gerekçesidir.
