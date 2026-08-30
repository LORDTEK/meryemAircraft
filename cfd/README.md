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

1. basamak deneyle ve sekiz yerleşik kodla karşılaştırıldı; sonuç
   `dogrulama.md`'de. Kısaca: Spalart-Allmaras kurulumumuz referans bandın
   üst ucunda (+%2,8), k-ω SST kurulumumuz ise her yerleşik kodun %5
   altında. Yerleşik kodlarda iki model arasındaki fark yalnızca %0,9
   olduğu için bu, model duyarlılığı değil **bizim SST kurulumumuzda bir
   kusurdur** ve 3. basamağa geçmeden kapatılması gerekir.

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

## Denetimin asimetrisi ve kapatılması

Bu çalışmada bulunan hataların çoğu, **bir eğilim yanlış yönde göründüğü
için bakıldığında** bulundu: momentum dengesindeki üç hata, %25 kesitinin
yakınsamaması, ayrılma ölçütündeki işaret hatası. Hepsi gerçek hataydı ve
bağımsız olarak doğrulandı — ama hepsine, sonuç tuhaf göründüğü için
bakıldı.

Bu tek yönlü bir taramadır ve sakattır: hoşa gitmeyen sonuçlarda hata
bulma olasılığı, hoşa gidenlerdekinden yüksek olur. Kabul edilen sonuçlar
denetlenmemiş kalır.

`denetim.py` o asimetriyi kapatıyor — eşikleri **önceden** yazılmış aynı
batarya, her vakaya, sonuç ne olursa olsun:

| vaka | C_L | kalıntı (son/ilk) | ayrılma |
|---|---:|---:|---:|
| A1–A4 | ≤ 1,2×10⁻⁵ | 0,60 – 0,97 | 0 % |
| B1–B4 | ≤ 2,3×10⁻⁵ | 0,82 – 0,96 | 0 % |
| R20–R200 | ≤ 4,9×10⁻⁶ | 0,60 – 0,66 | 0 % |
| kOmegaSST / SA | ≤ 2,1×10⁻⁶ | 0,60 / 0,80 | 0 % |
| %12 / %18 | ≤ 5,4×10⁻⁶ | 0,70 / 0,68 | 0 % / 1,0 % simetrik |
| **%25** | **4,8×10⁻²** | **2,89 ↑** | **11,2 %, 0/21 dengesiz** |

Kabul edilen sonuçların hepsi, reddedileni mahkûm eden aynı bataryadan
geçti. Tek işaretlenen vaka, zaten geri çekilmiş olan. Bu, tek yönlü
taramanın bu sefer yanlış bir kabule yol açmadığını **gösterir** —
iddia etmez.

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

### Salınımın yarısı yakınsama farkıydı

Farklı çözünürlükteki ağlar aynı yineleme sayısında **aynı ölçüde
yakınsamaz**: daha çok hücreli ağ aynı adımda daha geride kalır. 3 000
yinelemede B3'ün Ux kalıntısı 6,2×10⁻⁷, B4'ünki 8,3×10⁻⁷. Dolayısıyla
"hepsi 3 000'de" diye karşılaştırmak, ağ farkının üstüne yakınsama
farkını bindirir.

`kalinti.py` ikisini ayırıyor — C_D'yi eşit **kalıntı düzeyinde**
karşılaştırıyor:

| B3 → B4 farkı | |
|---|---:|
| aynı yineleme sayısında (3 000) | +0,77 % |
| eşit kalıntıda (1,5×10⁻⁶) | +0,34 % |
| eşit kalıntıda (1,2×10⁻⁶) | +0,40 % |

Salınımın yaklaşık yarısı yakınsama farkındanmış. Ama yarısı **kalıyor**:
eşit kalıntıda bile ardışık farkların işareti değişiyor, yani salınım
gerçek.

Dürüst ifade: **eşit yakınsamada en ince iki ağ C_D = 0,00769 – 0,00772
veriyor**, yani ±%0,2; ardışık üç seviye ise tekdüze olmadığı için resmî
bir mertebe ve GCI **verilemez**. Bu bir GCI değildir ve öyle
sunulmayacaktır.

## Alan boyutu: 20 veter yeterli

Büyüme oranı sabit tutularak (yakın alan değişmiyor, dışarıya yalnızca
katman ekleniyor) 20 → 200 vetere toplam etki **−%0,14**; adımlar
küçülerek yakınsıyor. Ağ belirsizliğinin bir mertebe altında, dolayısıyla
**20 veter yeterlidir** ve daha büyük alana geçmenin karşılığı yok.

Etki tamamen basınç sürüklemesinde; viskoz kısım dört alanda da
0,006397 – 0,006399 arasında sabit.

## Momentum dengesi ne ölçüyor — beklediğimden başka bir şey

Bu sınama, bağımsız bir doğrulama olsun diye kondu. Üç ayrı hatası
çıktı ve üçü de **eğilimin yanlış yönde olmasıyla** yakalandı:

1. `(2/3)k` terimi iki kez sayılıyordu — OpenFOAM'ın sıkıştırılamaz RAS
   çözücüsünde türbülans kinetik enerjisinin normal gerilme katkısı
   basıncın içindedir. Belirti: fark **alan büyüdükçe artıyordu**
   (%2,94 → %6,87), oysa büyük alan dengeyi iyileştirmeli.
2. Kütle akısı `U·S`'den alınıyordu; çıkışta U sıfır-gradyan olduğu için
   bu, çözücünün koruduğu `phi`'yi yeniden üretmez. `phi`'ye geçilince
   kapalı yüzeydeki net kütle akısı 1×10⁻⁴ → 3×10⁻⁸.
3. Sınır alanı hiç okunmuyordu (ayrıştırma hatası, aşağıda).

Üçü düzeltilince geriye kalan fark bir **yöntem hatası değil, çözüm
yakınsamasının ölçüsü** çıktı:

| yineleme | B3 farkı |
|---:|---:|
| 500 | +13,00 % |
| 1 500 | +7,36 % |
| 2 500 | +3,32 % |
| 3 000 | **+2,23 %** |

Tekdüze düşüyor ve 3 000'de hâlâ düşmekte. Bunun pratik önemi büyük:
**duvar integrali bu evrilmeye çok daha az duyarlı** (B4'te 500
yinelemede 2,9×10⁻⁶). Yani C_D yakınsamış *görünürken* çözüm hâlâ
evriliyor olabilir — ve bunu ancak momentum dengesi gösteriyor. Büyük bir
fark, önce yineleme sayısını sorgulatmalı; ağı ya da yöntemi değil.

## Bir ayrıştırma hatası: sınır değerleri hiç okunmuyordu

`foamoku.Alan`'daki düzenli ifade `boundaryField` kelimesinin **kendisini**
eşleştiriyor, gövdesi bütün yamaları kapsadığı için `findall` bir tek onu
buluyordu. Sonuç: yama sözlüğü yalnızca `boundaryField` anahtarını
taşıyor, her `yama_degeri` çağrısı `None` dönüyor ve bütün sınır değerleri
**sessizce komşu hücre değerine düşüyordu.**

Sürüklemeye etkisi ölçüldü: **≤ %0,01.** Çünkü y+ ≈ 1'de ilk hücrenin
`nut`'u zaten neredeyse sıfırdır, yani `ν + ν_t,hücre` ile `ν` arasında
fark yok. Hata gerçekti ama sonucu değiştirmiyordu — ve bu, varsayımla
değil ölçümle söyleniyor.

## ⚠️ GERİ ÇEKİLDİ — "türbülans modeli baskın belirsizliktir"

Bu bölüm önce şunu söylüyordu: aynı ağda k-ω SST ile Spalart-Allmaras
arasında %9,4 fark var, bu bütün sayısal belirsizliklerin yirmi katı,
dolayısıyla baskın belirsizlik türbülans modelidir.

**Yanlıştı.** Referans veri geldiğinde çürüdü.

`NAS-2016-01` (Jespersen, Pulliam, Childs, NASA Ames) sekiz yerleşik kodun
aynı vakadaki değerlerini veriyor. α = 0°, Re = 6×10⁶, M = 0,15:

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

Yerleşik kodlarda iki model arasındaki fark **%0,9**. Bizde %9,4.

| | bizim | referans ortalaması | fark |
|---|---:|---:|---:|
| Spalart-Allmaras | 0,00842 | 0,00819 | **+2,8 %** |
| k-ω SST | 0,00769 | 0,00812 | **−5,3 %** |

Yani SA'mız referans bandının üst ucunda oturuyor; **SST'miz her yerleşik
kodun %5 altında.** Ölçtüğümüz %9,4 model duyarlılığı değil, SST
kurulumumuzdaki bir kusurdu.

Çözünürlük değil: Overflow'un kendi SST ağ yakınsaması 57 921 hücrede
0,00826, 919 809 hücrede 0,00817 veriyor (NAS-2016-01, Tablo 7.5). Bizim
82 944 hücredeki değerimiz 0,00765.

**Bulunan aday sebep.** Aynı raporun 13. sayfası referans uygulamayı
yazıyor: SST için serbest akışta (μt/μ)∞ = **0,001**. Biz **1,0**
kullanmışız — bin kat büyük. `k` doğruydu (%0,1 şiddet, referansın
%0,088–0,104'üyle uyumlu), ama ω∞ = k/ν_t olduğu için bizimki 9,
referansınki 9000. Bu değişken **SA'da yoktur** — SA'nın oturup SST'nin
oturmamasının nedeni bu olabilir. `naca/serbest.py` bu tek değişkeni
tarıyor; beklenti betiğin başında **önceden** yazılı.

**Bu neden burada duruyor.** Yanlış bölümü silmek yerine geri çekilmiş
olarak bırakıyorum: sonucun nasıl kurulduğu, nasıl çürütüldüğü ve neyle
çürütüldüğü kaydın parçasıdır. Bir sayının yanlış olduğunu göstermek, onu
hiç yazmamış gibi davranmaktan daha çok bilgi taşır.

Bu arada geriye kalan sayısal belirsizlikler değişmedi ve hâlâ küçük:

| kaynak | belirsizlik |
|---|---:|
| ağ çözünürlüğü (eşit yakınsamada) | ±0,2 – 0,4 % |
| alan boyutu (20 veter) | 0,1 % |
| yineleme yakınsaması | ~0,1 % |
| duvar gradyanı mertebesi (y+ < 1) | 0,03 % |

Doğrulamanın tamamı için `dogrulama.md`.

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
