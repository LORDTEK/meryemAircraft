# Dış görüş — Tur 3: ara durum ve anlık uyarı çağrısı

Bu metin, uzun bir koşu **sürerken** yazıldı. İki turdur mutabık kaldığımız
adımlar atıldı ve sonuçlar önceki iki turun dayandığı temel varsayımı
yıktı. Şu an 27 saatlik bir koşu dönüyor. Sormak istediğim şey basit:

> **Bu koşu bitmeden söylenmesi gereken bir şey var mı?**

Yani "sonuç gelince konuşuruz" değil, "şu an bildiğin ve benim
bilmediğim, koşuyu boşa çıkaracak bir şey varsa şimdi söyle" çağrısı.

---

## Giriş — nereden geldik

Kuyruk üstü oturan, karma kanat-gövde (BWB) gövdeli bir VTOL İHA
konfigürasyon çalışması. Makalenin açık kalan tek büyük belirsizliği
sıfır-kaldırma sürüklemesi:

| kaynak | C_D0 |
|---|---|
| analitik, temiz yüzey + geçişli sınır tabaka | 0,0073 |
| 3-B CFD, tam türbülanslı k-ω SST, GCI'li, ±%5 | 0,0141 |

Bu aralığı daraltmanın yolu geçiş (transition) modelli bir koşu.

**Ondan önceki iki turda size sunulan sorun şuydu:** OpenFOAM v1912'nin
tek geçiş modeli `kOmegaSSTLM` hem y⁺≈1 hem bir ω denklemi istiyor;
k-ω SST bizim ağda y⁺≈1'de beş ayrı denemede ıraksadı (61, 154, 68, 6,
54 adım; ikisinde `bounding omega`); Spalart–Allmaras aynı ağda sorunsuz
koşuyor ama SA tabanlı geçiş modeli OpenFOAM v1912'de yok.

İkiniz de aynı şeyi söylediniz ve haklıydınız: **özel türbülans modeli
(Medida γ-Re_θ-SA) yazma.** Ayrıca bir eksiği de yakaladınız: doğrulama
planımda **doğal geçiş vakası yoktu** (T3A/T3B yüksek-Tu bypass
vakalarıdır; bizim rejim Tu ≪ %1).

Mutabık kalınan iki adım:
- **Adım 1:** `blended false` testi, tek değişken, ≥600 adım.
- **Adım 2:** sabit geçiş konumu taraması (kodunu henüz yazma).

---

## Gelişme — ne yaptım, ne umdum, ne buldum

### 1. Kontrol koşusu — ve temel varsayımın çöküşü

`blended false` hipotezini sınamak için önce bir **kontrol** kurdum
(YZ1'in istediği Run A): başarılı SA y⁺≈1 vakasının ağı, sınır koşulları,
şemaları ve gevşetmesi aynen; yalnızca `RASModel` SA → kOmegaSST. Yani
kaydımızdaki 4. denemenin yapılandırması. Beklentim: 6. adımda çökmesi.

**Kontrol, kaydın erken davranışını birebir üretti:**

| adım | log |
|---|---|
| 1 | `bounding omega, min −3 480 005, max 9,6448e+07` |
| 3 | `bounding omega, min −3,891` |
| 6 | `bounding omega, min −7,235` ← kayıtta "burada çöktü" yazan yer |
| 8 | `bounding omega, min −1225,7` |

6. adımdaki −7,235, kaydın yazdığı −7,24 ile aynı. Sayısal yol özdeş.

**Ama çökmedi.** 1000 adım koştu, temiz bitti. Kaydın saydığı beş çöküş
noktasının (6, 54, 61, 68, 154) hepsi geçildi. `bounding` olayları erken
geçici rejimde toplanıyor (81 olayın hepsi ilk ~200 adımda), k tepe yapıp
(14 256; serbest akım k = 1,5e−06) geri iniyor. Son adımda basınç artığı
1,2e−06.

**Sonuç:** "k-ω SST bu ağda y⁺≈1'de koşamıyor" önermesi — iki turdur
konuştuğumuz her şeyin çıkış noktası — **yanlış.** Dolayısıyla
`kOmegaSSTLM` yolu hiç C++ yazmadan açık. `blended` sorusu bir çökme
sorusu olmaktan çıkıp model-biçim duyarlılığı sorusuna dönüştü, yani
YZ1'in dediği çerçeveye.

Kaydımızdaki "beş deneme, beşi de çöktü" bölümü düzeltildi. Aradaki
farkın nerede olduğunu kesin bilmiyorum; en olası aday `limited`
katsayısı (1. ve 3. denemeler 0,33; bu koşu 0,25) ama 1/3/6. adımlardaki
sınırlama değerlerinin birebir aynı olması, 4. denemenin de aslında
çökmediğine işaret ediyor.

### 2. `kOmegaSSTLM` bu kurulumda çalışıyor mu — evet

Ciddi bir risk vardı: aynı kurulumda `forceCoeffs`, `yPlus`,
`postProcess` ve `mapFields` **kırık** (OSHA1stream). İlk LM koşusu tam
o hatayla öldü: `FOAM FATAL IO ERROR: error in IOstream "sha1"`.

"Demek LM de kırık" demek kolaydı. Değildi: OpenFOAM'ın kendi T3A eğitim
vakası üç `functionObject` içeriyor ve kırık olan onlar. `functions { }`
yapılıp yeniden koşuldu: **269 iterasyonda yakınsadı.**

### 3. T3A doğrulaması — model çalışıyor, geçişi %25 erken veriyor

T3A vakası OpenFOAM kaynağıyla **deneysel veriyle birlikte** geliyor
(Savill 1993/1996). C_f elden hesaplandı (functionObject kırık):

| bölge | fark (CFD − deney) |
|---|---|
| laminer (x 0,045–0,295) | +6,6% … +11,0% |
| geçiş (x 0,395–0,695) | +19% … +47% |
| türbülanslı (x 0,795–1,495) | −6,7% … +1,2% |

Türbülanslı bölgedeki ±%5, hem modelin hem benim C_f hesabımın sağlam
olduğunu gösteriyor. Geçiş bölgesindeki fark sapma değil **kayma**:
C_f minimumu CFD'de Re_x ≈ 1,16e5, deneyde ≈ 1,4e5 — yaklaşık **%25
erken**. Yön muhafazakâr: erken geçiş laminer bölgeyi kısaltır,
sürüklemeyi fazla verir.

### 4. Doğal geçiş — DENENDİ, BAŞARISIZ

Sizin yakaladığınız eksik buydu, kapatmaya çalıştım. Langtry (2006) tez
Bölüm 4 tablosundan hücum kenarı değerleriyle iki vaka daha kuruldu
(aynı ağ, aynı akışkan, yalnızca U, k, ω, Re_θt değişti):

| vaka | U | Tu | μ_t/μ | beklenen | ölçülen |
|---|---|---|---|---|---|
| T3A | 5,4 | %3,3 | 12,0 | Re_x ≈ 1,4e5 | 1,16e5 ✓ |
| T3A− | 19,8 | %0,874 | 8,72 | ~1e6 | ~3e6, alanın ucunda — **çok geç** |
| S–K | 50,1 | %0,3 | 1,0 | ≈3e6 (Langtry s.63) | ~2e4'ten türbülanslı — **çok erken** |

Sıralama ters: S–K'nın Tu'su daha düşük, geçişi daha geç olmalıydı.

**Bir hipotezi çürüttüm.** y⁺'ı suçladım (Langtry s.42: y⁺ > 5 olursa
geçiş yukarı kayar). Ölçtüm:

| vaka | y⁺ ort | y⁺ max |
|---|---|---|
| T3A | 0,32 | 0,39 |
| T3A− | 0,58 | 0,93 |
| S–K | 2,74 | 3,29 |

Üçü de eşiğin altında. **Ağ çözünürlüğü sebep değil.**

**Gerçek sebep ölçüldü:** hücum kenarında durma noktası k üretimi.
Duvara komşu hücrede, LE'den 0,6 mm sonra k'nın serbest akıma oranı:

| vaka | U | k(LE+0,6mm) / k∞ |
|---|---|---|
| T3A | 5,4 | **0,43×** |
| T3A− | 19,8 | **10,5×** |
| S–K | 50,1 | **72,7×** |

k-ω ailesinin bilinen durma noktası anomalisi. Eğitim ağının eliptik
hücum kenarı U = 5,4 için ayarlanmış; U = 50,1'de 73 katlık k sıçraması
sınır tabakayı hemen tetikliyor. T3A−'de sıçrama tetiklemiyor ama bu kez
serbest akım çürümesi baskın: Tu levha boyunca %0,874'ten ~%0,45'e
iniyor, Re_θt 769'dan 1164'e çıkıyor, geçiş alanın ucuna atılıyor.

**Dürüst ifade: doğal geçiş rejiminde model DOĞRULANMADI.** T3A eğitim
ağı ölçeklenerek yeniden kullanılamıyor; Langtry her vaka için ayrı ağ
kullanmış.

### 5. Serbest akım çürümesi — kanat vakası için ölçüldü

Kanadın giriş sınırı 100 veter uzakta. SST'nin kaynak terimsiz çürümesi
analitik olarak (β = 0,0828, β* = 0,09), mevcut kurulum değerleriyle:

| | giriş | hücum kenarında |
|---|---|---|
| Tu | %0,100 | **%0,0168** |
| ν_t/ν | 1,000 | 0,752 |

Langtry korelasyonuna sokulunca Re_θt 1137 yerine **1938** (+%70).

Çare kurulumda mevcut: OpenFOAM v1912'nin `kOmegaSST`'si `decayControl`
taşıyor (`kOmegaSSTBase.C:391`), ω denklemine +ρβω∞², k denklemine
+ρβ*ω∞k∞ ekliyor (Spalart–Rumsey ortam kaynağı). Varsayılanı `false`.

---

## Şu an ne dönüyor

k-ω SST, y⁺≈1, tam türbülanslı, **5000 adıma** koşuyor (şu an 1000'i
geçti). Amaç: bu ağda k-ω'nın y⁺=1 C_D0'ını almak.

**Neden 5000:** SA y⁺=1 koşusunda kuvvetler artıktan çok daha yavaş
oturmuştu — 2000. adımda C_D = 0,0228 iken 5000'de 0,0147 (%55 fark).
Kendi ara ölçümüm de bunu doğruluyor: 200. adımda C_D = **−1,52**
(negatif), basınç alanı henüz anlamsız. Artığa bakıp erken durmak bu
vakada ciddi hata olur.

**Süre:** ~22 s/adım, kalan ~4000 adım → ~24 saat.

Bu arada bir işletim hatası yaptım ve düzelttim: koşuyu sürdürecek
bekleme döngüm `pgrep -f "simpleFoam -parallel"` kullanıyordu, ama o
döngünün kendi komut satırı bu dizgeyi içerdiği için `pgrep` kendini
buluyordu; koşul hiç sağlanmadı ve koşu 1000'de bitip bir süre boşta
kaldı. Yeniden başlatıldı, `startFrom latestTime` ile kayıp yok.

---

## Sorular — ama asıl istediğim şey aşağıdaki 0. madde

**0. Bu koşu bitmeden söylemem gereken bir şey var mı?**
27 saatlik bir koşu dönüyor. Elinizde, "o koşunun sonucu şu yüzden işe
yaramayacak" veya "onu koşarken şunu da ölçmeliydin" diyebileceğiniz bir
şey varsa **şimdi** söyleyin; koşuyu durdurmadan ölçüm ekleyebilirim.
Beklediğim türden şeyler: kaçırdığım bir ayar, bir kontrol koşusu, bir
alan yazdırma isteği, ya da bu C_D0'ın hangi anlamda karşılaştırılabilir
olduğuna dair bir uyarı.

**1. "Beş çöküş yeniden üretilemedi" bulgusunu nasıl yorumlarsınız?**
Erken sınırlama değerleri birebir aynı, sonrası farklı. Bu bir yapılandırma
farkı mı (en olası aday `limited` 0,33 vs 0,25), yoksa kaydın kendisi mi
hatalıydı? Bunu makalede nasıl ifade etmeli — "önceki rapor düzeltildi"
demek yeterli mi?

**2. Doğal geçiş doğrulaması için ne kadar ileri gitmeli?**
Vakaya özel ağ kurmak (Langtry'nin yaptığı) ciddi iş. Alternatif: kanadın
kendi hücum kenarı çözünürlüğünü doğrudan sınamak ve doğal geçişi
canonical vakada hiç doğrulamamak. İkincisi bir konfigürasyon makalesi
için savunulabilir mi, yoksa "doğrulanmamış modelle üretilmiş sayı"
diye reddedilir mi?

**3. Durma noktası k üretimi kanatta ne yapar?**
BWB kök kesiti %25 kalın, hücum kenarı yarıçapı büyük. Re_kök = 1,99e6.
Levhada ölçtüğüm 73× sıçrama orada ne kadar olur, ve geçiş modeli
koşulacaksa hangi çare gerekir — üretim sınırlayıcısı (`Pk` limiter),
hücum kenarı ağ sıklaştırması, yoksa Kato–Launder türü bir düzeltme mi?

**4. `decayControl` doğru çare mi?**
Alternatif, giriş k/ω'sını hücum kenarında istenen Tu'yu verecek şekilde
yükseltmek. Hangisi daha savunulabilir? `decayControl` ile serbest akımda
yapay bir kaynak terimi taşımanın bir bedeli var mı?

**5. Adım 2 (sabit geçiş taraması) hâlâ gerekli mi?**
`kOmegaSSTLM` artık kullanılabilir olduğuna göre, sabit geçiş taraması
bir "vekil" olmaktan çıkıp gereksizleşti mi — yoksa modelin doğal geçiş
rejiminde doğrulanmamış olması yüzünden hâlâ değerli bir çapa mı?

**6. Atladığım ne var?**
Bir önceki turda bu soruyu sordum ve ikiniz de gerçek bir eksik
yakaladınız (doğal geçiş vakası). Aynı soruyu tekrar soruyorum.
