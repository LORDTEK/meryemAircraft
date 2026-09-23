# Çok rotorlu payı, NASA'nın kendi biriminde — pay daralıyor, bir köşede işaret dönüyor

**Tarih: 2026-09-20, Tur 48. Adım 6 yazılırken bulundu.**
**Kod:** `aero/effective_ld.py` · **Çıktı:** `aero/effective-ld-result.txt`

---

## 1. Bulunan hata: iki farklı türden sayı yan yana konuyordu

Makale çok rotorlu karşılaştırmasını üç ayrı yerde (v7 satır 276–277, 2498–2499,
ve Adım 1'in dayanağı) şöyle yapıyor:

> *"the sizing set of Section 3.1 puts a turboshaft quadrotor at an **effective**
> lift-to-drag ratio of 4.9 … against this configuration's **aerodynamic** 8.8 to 10.8."*

Makale ikisinin **farklı türden sayı olduğunu söylüyor** ve *"offered for scale rather than
as a measured margin"* diye uyarıyor. **Uyarı doğru ama yetersiz:** bir okuyucu 4,9'a karşı
8,8–10,8 gördüğünde bir **iki kat** okur. Gerçek pay bu değil.

## 2. Çevrim — ve neden meşru olduğunun kanıtı

Johnson & Silva'nın gösterim listesi (s. 94, `cfd/1521_Johnson & Silva_122721.pdf`):

> `L/De   aircraft effective lift-to-drag ratio, WV/P`

Seyirde T = D, L = W ve P_mil = T·V/η_p olduğundan:

> **L/De = W·V/P_mil = (L/D) · η_p**

**"P hangi güç?" sorusu varsayılmadı, kaynaktan kanıtlandı.** Denklem (2) enerjiyi
`E = (Pc/η_c)·t` yazıyor ve η_c'yi *"the propulsion system efficiency in cruise"* diyor —
tek başına belirsiz. Kanıt askıdaki eşdeğerinden geliyor, denklem (3):

> `I = (Ph/ν)/η_h`  ve  `Ph = W√(W/2ρA)/FM`

Burada **Ph, FM zaten uygulanmış** askı gücüdür, yani **mil gücü**; η_h onun **dışında**
duruyor. Demek ki η_h rotorun aerodinamik verimi değil, elektrik zinciri verimidir —
rotorun işini FM yapıyor. Biçimsel simetriyle **η_c de elektrik zinciri verimidir ve
Pc mil gücüdür.** Dolayısıyla L/De propulsor verimini **içerir**, ve çarpan çift sayım
değildir.

**Çapraz denetim:** ters çevirip NASA araçlarının aerodinamik L/D'sini bulalım. η_p ≈ 0,80
ile tiltwing 8,6 → L/D ≈ 10,8; lift+cruise 8,5 → L/D ≈ 10,6. İkisi de bu sınıf için makul.
Çevrim saçma sayı üretmiyor.

## 3. Sonuç

| | L/De |
|---|---:|
| Bu yapılandırma, olumsuz köşe (L/D 8,80 × η_p 0,632) | **5,56** |
| Bu yapılandırma, elverişli köşe (L/D 10,82 × η_p 0,683) | **7,39** |
| Quadrotor, turboşaft (NASA Tablo 3) | 4,9 |
| Quadrotor, elektrik (NASA Tablo 3) | 5,8 |
| QSMR turboşaft / Side-by-side turboşaft | 5,4 / 5,9 |

| Karşılaştırma | Pay |
|---|---|
| Makalenin şimdiye kadar yan yana koyduğu çift (8,8–10,8 vs 4,9) | +80 % … +121 % |
| **Aynı birimde (5,56–7,39 vs 4,9)** | **+14 % … +51 %** |
| Elektrik quadrotor'a karşı (5,56–7,39 vs 5,8) | **−4 % … +27 %** |

## 4. İki şey söylenecek, ve ikincisi yumuşatılmayacak

**(a) İşaret, bizimle aynı enerji kaynağını kullanan araca karşı her köşede korunuyor.**
Turboşaft quadrotor 4,9; bizim en kötü köşemiz 5,56. Payın kapanması için η_p'nin 0,557'ye
düşmesi gerekirdi; hesaplanan en düşük değer 0,632. **Marj 0,075.**

**(b) Ama "her rotorlu aracı geçeriz" YANLIŞ.** NASA'nın elektrik quadrotor'u 5,8 ile bizim
olumsuz köşemizin **üstünde.** O araç verimini aynı görev için **1.742 lb batarya** ve
**iki kat ağırlıkla** (7.221 lb / 3.678 lb) satın alıyor — ki bu tam olarak Fatura 1'dir ve
çerçevenin kendi öngörüsüdür. **Ama verim ekseninde, tek başına, bizi geçiyor.**

## 5. Neyi değiştiriyor

> **"Farklı verim sınıfı" (different efficiency class) ifadesi ARTIK KULLANILMAZ.**
> +%14 bir sınıf farkı değildir. v7 satır 2506–2508'deki *"a vehicle that carries its cruise
> lift on a wing is in a different efficiency class from one that carries it on rotors"*
> cümlesi, **bu aracın gerçekleştirdiği pay** için fazla iddialıdır.

**Yapısal iddia ayakta, nicel iddia daralıyor, ve ikisi birbirinden ayrılıyor:**

- **Yapısal:** kaldırma bir yüzeyde mi taşınıyor, rotorda mı — bunu hiçbir boyutlandırma
  sözleşmesi değiştirmez. Bu **durum olarak** doğru kalıyor.
- **Nicel:** bu uçağın gerçekleştirdiği pay **+%14 … +%51**'dir, ve payı daraltan şey
  kanat değil **bizim kendi sabit hatve cezamızdır.** η_p = 0,85 olsaydı L/De 7,48–9,20
  olurdu. Yani pay mimarinin değil, **bu aracın pervane seçiminin** bir özelliğidir.

| Yer | Ne değişiyor |
|---|---|
| **Adım 6** | Karşılaştırma aynı birimde yapılıyor; "farklı sınıf" ifadesi yok |
| v7 satır 276–277, 2498–2499 | İki farklı türden sayının yan yana konması — v8'de tekrarlanmıyor |
| v7 satır 2506–2508 | *"different efficiency class"* — v8'de yok |
| Adım 11 (defter) | η_p cezası artık iki yerde birden görünüyor: menzil **ve** çok rotorlu payı |

## 6. Ölçek çekincesi — ama bir kaçış yolu olarak kullanılmıyor

NASA araçları 1.670–3.275 kg, bizimki 50 kg ve 1.000 kg. Reynolds sayısı büyük araçların
lehinedir, dolayısıyla küçük tasarımımız bu karşılaştırmada **dezavantajlıdır.** Ayrıca
NASA quadrotor'unun disk yüklemesi 3–3,5 lb/ft² (≈15–17 kg/m²) ile **alışılmadık ölçüde
düşük**, yani karşımızdaki quadrotor **iyi** bir quadrotor. Ve onların sayısı **Vbr**'de
(en iyi menzil hızı), bizimki ise **seçilmiş seyir noktasında** (1,49 × stall), ki v7
§2.12 bunun en iyi L/D noktası **olmadığını** açıkça söylüyor.

**Üç çekincenin üçü de karşı tarafın lehine.** Bu yüzden hiçbiri payı büyütmek için
kullanılmaz; yalnız karşılaştırmanın ne kadar kaba olduğunu söylemek için yazılır.

---

# Tur 48 — dört okuyucunun denetimi, ve iki kaynak denetimi

**Dördü de çevrimi onayladı.** ChatGPT belgeyi o turda açtı ve Cambridge kopyasının bağını verdi;
Grok açıkça *"bu tur hiçbir PDF açmadım, cebiri yargılıyorum"* dedi; DeepSeek ve Qwen de
açamadıklarını söyledi. **§2.1'in karşılığı çalıştı:** kimse açmadığı belgeden sayı vermedi.

## 1. Grok'un `P` itirazı — haklı soru, ama cevap bizim lehimize

> *"Turboşaft quadrotor için mil okuması doğal olan. Elektrik 5,8 için **tehlikeli** olan:
> o 5,8 `WV/P_batarya` ise, bizim 5,56–7,39'umuz aynı birimde değil."*

**Soru meşru ve kaynaktan kapanıyor. Ama Grok'un endişesi ters yönde.** Kaynağın ayrımı tam da
**batarya kapasitesi** türevinde yapılıyor (s. 640–655):

> `Ecap = Ecruise + Ehover + Ereserve`  (1)
>
> `Ecruise = (Pc/ηc) × time = WR/((L/De) ηc)`  (2)

**Yani elektrikli araçlar için L/De açıkça η_c'nin YUKARISINDA.** L/De batarya gücünü içerseydi,
NASA kendi batarya boyutlandırmasında zinciri **iki kez** saymış olurdu. Elektrik satırı, kanıtın
en güçlü olduğu satırdır — en zayıf olduğu değil.

Grok'un kendi çekincesi doğru uygulandı: *"Do not guess the sign."* Sayıyı tahmin etmedik, belgeyi
açtık.

## 2. ChatGPT'nin η_p tarifi itirazı — HAKLI, ve düzeltildi

> *"'0,632–0,683, gerçek burun paletinin gerçek askı ve seyir koşullarındaki iki noktalı
> çözümünden' — bu tarif yeterince doğru değil."*

**Haklı.** `aero/nose_propeller_crossing.py` çıktısı:

| pala | c_l | η |
|---|---|---:|
| 2 | 0,55 | 0,648 |
| 2 | 0,70 | **0,683** |
| 3 | 0,55 | **0,632** |
| 3 | 0,70 | 0,643 |

Aralık **dört palet ailesinin** yayılımıdır. *"İki nokta"* her paletin askı ve seyirde ayrı
çözülmesini anlatıyor — aralığın kaynağını değil. Cümle ikisini birbirine karıştırıyordu.

**Ve düzeltme bir şey daha açtı, ki üç okuyucu da braket eşleştirmesini sorgulamıştı:**

> **İki yayılım aynı türden değil.** C_D0 braketi **belirsizliktir** — tasarımcı gerçek uçağın
> nereye düşeceğini seçemez. Palet ailesi **sabitlenmemiş bir tasarım seçimidir** — tasarımcı
> en iyisini alır. İkisini tek bir *"olumsuz köşe"* diye sunmak, seçilmeyecek bir paleti
> belirsizlikmiş gibi göstermektir.

Sayfa artık çarpım matrisini veriyor (5,56 · 6,01 · 6,84 · 7,39) ve iki türü adlandırıyor.

## 3. DeepSeek'in dördüncü çekincesi — REDDEDİLDİ, kaynak tersini söylüyor

> *"Çok rotorlunun tahrik kayıpları bizimkinden küçüktür, çünkü **iki görevli uzlaşması yoktur.**"*

**Yanlış.** Kaynak §6.3, *"Trim of multi-rotor aircraft"* (satır 723–733), quadrotor'un askı ile
seyir arasında tam da o uzlaşmayı yaptığını gösteriyor:

> *"For the quadrotor, **both collective and rotor speed control were considered.** … Edgewise
> rotor flight has reduced induced power … followed by power increasing with speed as the
> parasite power increases. … With rotor speed control and fixed collective, the rotor rpm
> follows the power variation with speed, while the rotor C_T/σ increases with speed initially
> and then decreases. **The increase in C_T/σ might be limited by maximum blade loading, perhaps
> requiring a smaller design C_T/σ at hover (hence larger blade area).**"*

Son cümle bir iki-rejim uzlaşmasının tarifidir. Quadrotor rotorları **da** hem askı hem seyir
yapıyor. Çekince alınmadı.

**Yerine ChatGPT'nin dördüncü çekincesi alındı** — analiz zincirleri eşleşmiyor — ve doğrulandı:
kaynak §2.1 boyutlandırma için **NDARC**, §2.2 rotor için **CAMRAD II / CHARM** kullandığını
söylüyor (satır 189–211). Bizimki sürükleme dökümü + polar + ayrı BEMT.

## 4. Kenarda bulunan, ve 11/13. adıma ait

Aynı denetim sırasında: **tiltwing (L/De 8,6) collective kontrol kullanıyor ve uç hızını askıda
550 ft/s'den seyirde 300 ft/s'ye düşürüyor** (§5.5, satır 590–592, birinci elden). Bunlar tam
olarak bu mimarinin reddettiği **iki ayar.** 8,6'ya karşı 5,56–7,39, değişken hatve göbeğini
reddetmenin bedelinin dolaysız bir ölçüsüdür — **ve tiltlere karşı menzil/verim iddia
etmediğimiz eksende.** Adım 11 ve 13'ün malzemesi, Adım 6'nın değil.

**Dikkat:** *"Collective control is used, with hover tip speed 550 ft/sec and cruise tip speed
300 ft/sec"* cümlesi **§5.5 Tiltwing'e** aittir. Quadrotor'a atfedilmez — bir kez yanlış
atfetmeye çok yaklaştım.

---

# Tur 49 — dört okuyucunun ikinci turu, ve bir propagasyon hatası

## 1. Kabul edilen ve doğrulanan bulgular

**(a) *"Tasarımcı en iyisini alır"* fazla iddialıydı — ChatGPT, Grok, Qwen.**
ChatGPT'nin gerekçesi belirleyici: tasarımcı en yüksek η_p'li paleti **ancak** seçim ölçütü
askı FM kısıtı altındaki seyir verimiyse alır. Pala sayısı ve kesit yüklemesi aynı zamanda
yapısal yükleri, akustiği, motor çalışma noktasını, rotor ataletini ve imalatı yönetiyor —
**hiçbiri bu çalışmada modellenmiyor.** Cümle kaldırıldı; yerine iki okuma birden veriliyor.

**(b) Manşet yüzdesi, metnin kendisinin *"seçilmez"* dediği paletten geliyordu — Grok.**
Aritmetiği denetlendi, birebir doğru:

| | vs 4,9 | vs 5,8 |
|---|---|---|
| İncelenen zarf, 5,56–7,39 | +%14 … +%51 | **−%4** … +%27 |
| En iyi incelenen aile, 6,01–7,39 | +%23 … +%51 | **+%4** … +%27 |

**En iyi ailede işaret her iki referansa karşı da korunuyor.** Sayfa artık iki satırı birden
veriyor ve hiçbir köşeyi *"uçağın başarımı"* diye sunmuyor. Palet Adım 10'da sabitlenecek.

**(c) Üç fazla genel cümle — ChatGPT.** Üçü de düzeltildi:

| Yazılan | Sorun | Yazılan yeni hâli |
|---|---|---|
| *"A **rotorcraft's** discs must produce lift and propulsive force together"* | Rakip çok rotorlu; bileşik rotorlular ve gövdesi kaldıran helikopterler bunu çürütür | *"A **multirotor's** discs … throughout cruise"* |
| *"the surface **costs no power** to do its part"* | İndüklenmiş sürükleme güçtür | *"the wing produces its lift **without a separate continuous power supply of its own**"* |
| *"not reliable **for anyone** on this class of configuration"* | §2.2'nin yasakladığı evrensel iddia | *"**for the methods used here**, and for the published comparisons against which they were checked"* |

**(d) Beşinci çekince — Grok (irtifa) ve ChatGPT (kapanış).** İkisi de alındı.
Kaynak, birincil görevin *"5,000-ft altitude and ISA + 20°C"*'de uçulduğunu söylüyor
(s. 385, birinci elden); bizimki tamamen deniz seviyesi. **Yönü iddia edilmiyor** — hesaplanmadı.
Ve ChatGPT'nin ayrımı analiz zinciri çekincesine katlandı: NASA'nınki **kapanmış bir aracın**
etkin oranı, bizimki **kapanıştan önce** belirlenmiş bir seyir noktasındaki çevrilmiş metrik.

**(e) Hız uyuşmazlığının YÖNÜ — DeepSeek. İddia edilmedi, hesaplandı** (`aero/effective_ld.py`):

| braket ucu | seyir L/D | L/D_max (e=0,850) | L/D_max (e=0,817) |
|---|---:|---:|---:|
| elverişli | 10,82 | 11,88 | 11,65 |
| olumsuz | 8,80 | 10,28 | 10,08 |

**L/D_max her köşede seyir L/D'sinin üstünde.** Yani referansa en iyi hızı veriliyor, bize
verilmiyor, ve pay yine de pozitif. **Yön bu kadar; büyüklük iddia edilmiyor** — en iyi nokta
stall'ın 1,26 katı ve orada uçmak marj bırakmıyor, dolayısıyla bir seçenek değil.

**(f) Kanıt katmanları — ChatGPT.** *"The weight it pays … **is** the charge Section 2 describes
and Section 4 tests"* bir yorumdu. *"…is **consistent with** the mass charge Section 2
describes"* oldu; nedensel bağın kanıtı Adım 4'te, bu tabloda değil.

## 2. Reddedilen

**Qwen: *"beşinci çekince eksik değil, dördü kapsamlı."*** Alınmadı — iki bağımsız okuyucu
(irtifa, kapanış) ve bir hesap (hız yönü) aksini gösterdi.

## 3. Ve kimsenin göremeyeceği bir hata: PROPAGASYON

**Adım 6'da *"farklı verim sınıfı"* ifadesini emekliye ayırdık. Adım 9'da hâlâ canlıydı:**

> *"**Claimed.** A vehicle carrying its cruise lift on a wing is in a **different efficiency
> class** from one carrying it on rotors, and no sizing contract moves a vehicle between those
> classes."*

**Dört okuyucunun hiçbiri göremezdi — ellerinde Adım 9 yoktu.** Bu, §0.2'nin tam olarak
tarif ettiği hata sınıfı: *düzeltmenin kendisinin yayılmaması.* Bir ifadeyi emekliye ayırırken
**deponun tamamında aranmadı.**

**Kural eki:** bir ifade emekliye ayrıldığında, `grep -rn` ile **bütün v8 adımlarında** aranır
ve her örneği aynı turda düzeltilir. Bu tur `grep` ile denetlendi; düzyazıda kalmadı.

Adım 9 satırı artık: *"**Claimed, and bounded.** … The **size** of the resulting advantage is a
calculation, not a consequence of that fact."* — yani yapısal önerme ile nicel önerme ayrı.

## 4. Adım 9'a eklenen iki bölüm — DeepSeek

**(a) Her iddianın neye BAĞLI OLMADIĞI.** Bir okuyucu birini reddettiğinde ötekilerin ayakta
kalıp kalmadığını görebilsin diye. Ve en önemli satır: **mekanizma iddiası geçiş
aerodinamiğine bağlı değildir** — o bir donanım envanteri ifadesidir — ama **uçağın geçişi
yapabildiği iddiası bağlıdır**, ve Adım 7 o sınırın altında okunmalıdır.

**(b) Fiyatlanmamış bedel, Adım 1'de değil burada da.** Tepki torku kanalını bırakmanın
bedeli hiçbir yerde hesaplanmıyor; iddia mekanizma sınıfının elendiğidir, **elemenin dengede
elverişli olup olmadığı bu çalışmanın çözmediği bir sorudur.**

## 5. Adım 5'e üç düzeltme

- *"the landing gear's **reaction surface**"* — ChatGPT haklı, zemin zaten tepki yüzeyidir.
  *"the site supplies **no prepared launch or recovery infrastructure** of any kind"* oldu.
- *"Those numbers exist, **they close**, and Section 10 reports the closure"* — Grok haklı:
  Adım 5, Adım 10'un sonucunu önceden ilan edemez. *"Section 10 reports **whether** they close"*.
- **Kapalı çevrim askı kontrolü** *"gösterilmedi"* listesine eklendi (ChatGPT) — ve bırakılan
  tepki torku kanalıyla bağlandı.

## 6. Yazara bırakılan üç karar

1. **Açıklık verimi: 0,85 mi 0,817 mi** (Grok). Adım 10 kütleyi kapatmadan önce bir tanesi
   seçilmeli; Adım 6'nın poları şu an iyimser olanı kullanıyor.
2. **Palet ailesi: zarf (şimdi) mü, Adım 10'da seçilmiş tek palet mi** (ChatGPT B'yi tercih
   ediyor, ama Adım 10 yazılana kadar zarf doğru).
3. **Qwen 1–9'un tam metnini istiyor; Grok her tur 1–9 yapıştırmaya karşı.** Bir kereye mahsus
   tam gönderim mi, yoksa Grok'un "tur başına bir adım" kuralı mı.

---

# Tur 50 — BÜTÜN okuması: yirmi iki dikiş kusuru, ve üçüncü propagasyon hatası

**Yazar Adım 9'un hiç gönderilmediğini ve parça–bütün–parça'nın hiç uygulanmadığını yakaladı.
Bütün gönderilince dördü birden dikişleri buldu.** Bu kayıt, hangisinin doğrulandığını ve
hangisinin reddedildiğini tutar.

## 1. BENİM HATAM, ve §3.1'in tam olarak tarif ettiği sınıftan — ÜÇÜNCÜ kez

**ChatGPT, DeepSeek ve Qwen bağımsız olarak aynı sayıyı buldu.** Adım 6 şunu diyordu:

> *"The span efficiency used throughout this section is the computed value, 0.817"*

ve aynı sayfada:

> *"L/D_max … 11.88 against 10.82, and 10.28 against 8.80"*

**11,88 ve 10,28, e = 0,85 değerleridir.** e = 0,817 ile 11,65 ve 10,08 çıkar — ve ben bunları
`aero/effective_ld.py` çıktısında **geçen tur kendim hesaplamıştım.** Betiği düzelttim,
**düzyazıyı düzeltmedim.**

> **§3.1 "emekliye ayrılan ifade depoda aranır" diyor. Sayılar için de gerekiyormuş.**
> Bir betik düzeltildiğinde, o betiğin **çıktısını alıntılayan her düzyazı** aynı turda
> yeniden okunur. Kural genişletildi.

## 2. Grok'un iki bulgusu — ikisi de doğrulandı

**(a) Adım 8'in bayat watt'ları.** 1,9 / 2,6 / 10,9 kW ve 1,8 kg / %3,6, η_p = 0,80 zincirinin
sayıları. Adım 6'nın uçağı 0,632–0,683'te yaşıyor. **İkisi aynı anda güncel olamaz.**

Grok'un asıl tespiti daha derin: *"bu bir kez yakalandı ve etiketlendi; birleştirilmiş metinde
etiket yok."* **Doğru, ve sebebi benim.** Etiket Türkçe denetim tablosundaydı ve bütün
paketi hazırlarken o tabloları **çıkardım.** Yani:

> **Bir çekince yalnız Türkçe denetim tablosunda duruyorsa, İngilizce gövdede yok demektir.**
> Okuyucu onu asla görmez. Sayılar sayfadan **çıkarıldı**; yeniden kapanmış küme Adım 10'un işi.

**(b) *"Five propellers, and every one of them is a coaxial pair"*** — emekliye ayrılmış cümle
geri gelmişti. *"Five propeller stations, ten rotors"* oldu.

## 3. Adım 4'ün aritmetiği — bulgu doğru, SAYILARI yanlış

ChatGPT ve DeepSeek ikisi de *"716 − 146 = 570, metin 679 diyor, 109 lb açık"* dedi.
**İkisi de batarya satırını atlamış.** NASA Tablo 3'ten, birinci elden:

| | L+C TE | Tiltwing TE | fark |
|---|---:|---:|---:|
| Yapı | 2.670 | 1.954 | **+716** |
| Tahrik | 1.772 | 1.918 | **−146** |
| Batarya | 254 | 244 | **+10** |
| **toplam** | | | **580** |
| Boş ağırlık | 5.809 | 5.130 | **679** |

**Açık 109 değil, 99 lb** — ve Tablo 3'ün dökmediği kalemlerde. Sayfa artık dökümü tam
veriyor ve 99 lb'nin nerede olduğunu **bilmediğini** söylüyor.

Ayrıca ChatGPT'nin iki itirazı alındı: *"the only architectural difference"* fazla iddialıydı
(biri rotorunu akışta durduruyor, öteki kanadını eğiyor — başka farklar da var), ve
*"the dedicated lift group costs 687 lb"* nedenselliği tek donanım grubuna yüklüyordu.
687 lb **iki mimari arasındaki net fark**, bir kaldırma grubunun ölçülmüş kütlesi değil.

## 4. DeepSeek'in "zero-bill" bulgusu — öncülü yanlış, sonucu değerli

DeepSeek: *"tilt üç faturadan sıfırını ödüyor, o hâlde ad yanlış."* **Öncül yanlış:** Adım 2'nin
tablosu her çarenin neye **saldırdığını** ve ne **yarattığını** gösteriyor; saldırmadığı fatura
ayakta kalıyor. Tilt Fatura 1'e saldırıyor, **Fatura 3'e saldırmıyor** — tamponu yok, güç
kaynağı hâlâ askı tepesiyle boyutlanıyor. NASA'nın tiltwing'i bunu doğruluyor: *"a relatively
small battery **just to enable emergency landing** after loss of turboshaft power"* (§5.5).

**Ama belirsizlik gerçekti:** *"not one of the three"* ifadesi "net sıfır" diye okunabiliyordu.
Satır artık **Fatura 3'ün ayakta kaldığını açıkça yazıyor**, ve ad savunulabilir hâle geliyor.

**İkinci bulgusu da yarı doğru:** Adım 8'in uç çiftleri için *"Adım 3'ün ikinci satırı"* demesi
**yanlış** — o satır kaldıran ve sonra taşınan bir propulsor'ü tarif ediyor; uç çiftleri
kaldırmıyor. Düzeltildi: **dördüncü** başarısızlık kipi (kısmi gerçekleşme). Ve *"cruise thrust"*
Adım 3'te **tanımlandı**: seyir sürüklemesini dengeleyen itki.

## 5. Kabul edilen öteki dikişler

| # | Bulgu | Kim |
|---|---|---|
| 1 | Adım 2 *"four VTOL architectures"* → **beş aile** (zaten Tur 45'te bilinip yapılmamıştı) | ChatGPT, Grok |
| 2 | Adım 9 *"Cruise efficiency **and range** \| Multirotors"* — Adım 6 çok rotorluya karşı hiç menzil sayısı vermiyor | ChatGPT |
| 3 | Adım 7 *"What is new is that…"* Adım 1'in hak ettiğinden geniş | ChatGPT |
| 4 | Adım 7'nin mekanizma tablosundaki **elevon/rudder satırı** — kumanda yüzeyi rejim değiştiren bir mekanizma değil; çıkarıldı ve tablonun **ne saydığı** yazıldı | ChatGPT |
| 5 | Adım 7 geçiş sınırını **kendisi** söylemeli, Adım 9'a bırakmamalı | DeepSeek, Grok |
| 6 | Adım 8 *"no variable mechanism of any kind"* komut edilen devirle çelişiyor | ChatGPT, Grok |
| 7 | Adım 8'in iç içe mil iddiası geri gelmişti; yeniden daraltıldı | ChatGPT |
| 8 | Adım 8 trim sorusunu Adım 10'a yolluyordu; Adım 10 kütle döngüsü — **14'e** | Grok |
| 9 | Adım 7 *"same job"* vs Adım 3'ün *"job"* reddi → **both duties** | Grok |
| 10 | Uç çerçeveleri **üç** değil **dört** iş yapıyor (fairing dördüncü) | DeepSeek |
| 11 | Adım 1 *"three of the four objections"* — kaynağın listesi daha uzun; cümle **silindi** | ChatGPT |
| 12 | Adım 1 *"what is unoccupied is the corner"* ile *"the third route is occupied"* çelişiyordu | ChatGPT |
| 13 | Adım 1'in yatış cümlesi Adım 7'nin tepki torku düzeltmesini **öncelemiyordu** | DeepSeek |
| 14 | Adım 2'nin çürütülebilirlik cümlesi tilt satırıyla çelişiyordu | ChatGPT |
| 15 | Adım 6'nın kapanış paragrafı hâlâ *"14 to 51 percent"* diyordu — atılan paletin zarfı | Grok |

## 6. Reddedilen / alınmayan

- **Qwen: *"başka çelişki yok, her iddia tutarlı."*** Alınmadı — on beş tane daha vardı ve
  Qwen'in kendi bulduğu tek sayı dışında hiçbirini görmedi.
- **DeepSeek: Adım 1'in 1954 anlatısı iki cümleye insin.** Oran meselesi, hata değil;
  **yazara bırakıldı.**
- **"Zero-bill condition" adının değiştirilmesi.** Tilt satırı düzeltilince ad savunulabilir
  oluyor; yine de **yazara bırakıldı.**

## 7. İki karar — dördü de aynı yerde

**C_D0: tutarlı braket 0,0285–0,0381, yayımlanan 0,0248 değil.** Dördü de. Gerekçe: sweep o
değeri **iki ucun da altına** koydu; Adım 6 zaten braketi kullanıyor; Adım 10'un onu
kullanması makalenin kendi desteklemediğini ilan ettiği bir sayı üzerinde kapanmak olurdu.

**Zarf kapalı döngüden geçebilir, ve mekanizması Grok'ta.** `baseline.py` **L/D'yi girdi olarak
alıyor** — döngünün içinde dört geometri olmasına gerek yok. Matrisin dört köşesi dört girdi,
dört kapanış, dört kütle, dört menzil. ChatGPT aynı şeyi 4 palet × 2 C_D0 = sekiz kapanış
olarak söylüyor ve bir ihtimali ekliyor: **en iyi palet kapanıştan sonra en iyi kalmayabilir**,
çünkü etkisi güç, kütle ve yakıt üzerinden yayılıyor. Öyle çıkarsa makale bir şey **öğrenir.**


---

# Tur 51 — Adım 10'un girdi yuvasında bir çift sayım, ve beşinci propagasyon hatası

## 1. ChatGPT ve Grok bağımsız olarak aynı hatayı buldu: ADIM 10'UN PLANI YANLIŞTI

Tur 54 metninde planı şöyle yazdım:

> *"L/De matrisinin dört köşesi, L/D'yi girdi alan `baseline.py`'ye dört girdi olarak taşınır."*

**İkisi de bunun çift sayım olacağını söyledi. Kod denetlendi; haklılar.**

### Tuzak 1 — L/De'yi L/D yuvasına koymak

```
baseline.py:126   R = f_yakit × E* × eta_zincir × (L/D) / g
baseline.py:43    eta_zincir = 0.176 = 0.2202 × 0.80
```

`eta_zincir` **zaten pervaneyi içeriyor.** `L/De = (L/D)·η_p`'yi L/D yuvasına koymak η_p ile
**iki kez** çarpmak olurdu.

### Tuzak 2 — kimsenin görmediği, ve daha sinsi olan

Döngüde **iki** verim parametresi var:

```
baseline.py:111   P_seyir = W × V / LD / eta_seyir      <- MOTORU boyutlandırır
baseline.py:126   R       = ... eta_zincir × (LD) ...   <- MENZİLİ verir
```

`eta_seyir = 0,721` de pervaneyi içeriyor — §2.12'nin 1,7 kW'ından geri çözülmüş.
**Yalnız `eta_zincir` ölçeklenseydi, motor ESKİ pervaneye göre boyutlanır, menzil YENİ
pervaneye göre hesaplanırdı.** Kapanış kendi içinde tutarsız olurdu — ve bu tam olarak bu
projenin tekrar tekrar düştüğü hata sınıfı, bu kez boyutlandırma döngüsünün içinde.

### Doğrusu zaten depodaydı

`chain_resolve.gorev_ile(eta_p)` iki terimi de ölçekliyor:

```python
g["eta_zincir"] = ZINCIR_PERVANESIZ * eta_p
g["eta_seyir"]  = BL.GOREV["eta_seyir"] * eta_p / ETA_P_MAKALE
```

**Yani mekanizma doğruydu, benim tarifim yanlıştı.** `aero/closure_inputs.py` bunu sabitliyor
ve bir kuruluş sınamasıyla koruyor: `gorev_ile(0,80)` yayımlanan GOREV'i %0,11 içinde yeniden
üretiyor; üretmezse betik duruyor.

| | C_D0 | η_p | **L/D** | eta_zincir | eta_seyir |
|---|---:|---:|---:|---:|---:|
| A | 0,0381 | 0,632 | **8,80** | 0,13920 | 0,56959 |
| B | 0,0381 | 0,683 | **8,80** | 0,15043 | 0,61555 |
| C | 0,0285 | 0,632 | **10,82** | 0,13920 | 0,56959 |
| D | 0,0285 | 0,683 | **10,82** | 0,15043 | 0,61555 |

**L/D sütununa aerodinamik oran girer.** L/De yalnız Adım 6'nın çok rotorlu karşılaştırmasının
birimidir; boyutlandırma döngüsünün girdisi değildir.

**DeepSeek'in iki doğrulama sorusunun yanıtı, koddan:** η_p bir **girdi**, döngü değişkeni
değil — `baseline.py` pervane boyutlandırmıyor. Ve **motor boyutu dört kapanışta değişir**,
çünkü `P_seyir` `eta_seyir`'e bağlı; Adım 10 motor büyüklüğünün yayılımını da raporlayacak.

## 2. Beşinci propagasyon hatası — DeepSeek buldu

Adım 8'de uç çerçevelerini *"üç iş"*ten **dört işe** çıkardım. **Adım 5 hâlâ *"three purposes"*
diyordu.** Yani düzeltmenin kendisi yayılmadı — aynı tur içinde. §3.1'in beşinci örneği.

## 3. Öteki kabul edilenler

| Bulgu | Kim |
|---|---|
| Adım 7 *"the condition it is built to satisfy"* tam kaçışı ima ediyordu; uçak **kısmi** gerçekleşme → *"the condition **its primary propulsor** is designed to satisfy… the price the configuration pays for **pursuing** it"* | ChatGPT |
| Adım 6 *"every corner is **reachable**"* → *"bounding combinations permitted by two independent model inputs… **not four demonstrated aircraft states**"* | ChatGPT, Grok |
| Adım 3'ün **ters tablosunda** tilt satırı Fatura 3'ü anmıyordu — Adım 2 düzeltildi, Adım 3 kalmıştı | DeepSeek |
| Çürütülebilirlik **olumlu** biçimde yazılmalı: neyin sayılacağı | Grok |
| Mekanizma tablosu başlığı değişken hatve satırını kapsamıyordu → *"or to take a rotor out of one regime's flow"* | DeepSeek |
| Kısmi gerçekleşmenin **koşul** hakkında değil **faturalar** hakkında olduğu netleştirildi | Qwen |

**Çürütülebilirliğin yeni hâli, Grok'un istediği olumlu ifade:**

> *"a counter-example is a remedy that reduces one of the three charges, leaves the other two no
> worse, and whose own cost is either absent or demonstrably smaller than the reduction —
> **measured in the same currency**."*

Aynı para birimi kuralı testi kullanılabilir kılıyor: kütleye karşı kütle, sürüklemeye karşı
sürükleme. DeepSeek'in *"dış maliyetler testten dışlanınca test çok zayıflıyor"* itirazı da
bununla karşılanıyor.

## 4. Zaten düzeltilmiş olanlar — okuyucular eski metne bakmış

- **DeepSeek #2:** *"izin verilen maliyetler maddesi 'koşul onlar hakkında bir şey söylemiyor'
  diyor."* **O cümle geçen tur zaten kaldırılmıştı.**
- **Grok:** *"Adım 6'nın kapanış cümlesi hâlâ 14–51 diyorsa…"* — şartlı söyledi, demiyor.

## 5. Qwen

Tur 51'de Adım 10 mekanizmasını **onayladı** — *"The sizing loop takes L/De as an input, not L/D
and η_p separately. This mechanism is correct."* **Yanlış**, ve ChatGPT ile Grok'un bulduğu tam
olarak bu. Ardından menzil denklemini on beş kez tekrarlayan bir döngüye girdi ve kendi
tekrarının içinde cevabı taşıdığı hâlde (*"η_chain includes η_p"*) sonucu çıkaramadı.
**Onayı kullanılmadı.**

---

# Tur 52 — Adım 10'un denetimi: ALTINCI propagasyon hatası, ve o da benim

## 1. Reddettiğim karşılaştırmayı iki adım sonra kendim yaptım

Adım 6'nın *"bilerek olmayanlar"* listesi şunu diyor:

> **Çok rotorluya karşı hiçbir MENZİL sayısı.** Bu çalışmada boyutlandırılmış bir çok rotorlu
> yok; menzil karşılaştırması iddia edilse **uydurma** olurdu.

Ve Adım 9'un tablosundan *"and range"* ifadesini geçen tur çıkardım. **Sonra Adım 10'a şunu
yazdım:**

> ~~*"Even the lowest of them, 927 km, is not a number the rotorcraft family reaches."*~~

**Grok:** *"That sentence is the comparison, without a number on the other side. Delete it, or
replace it with a cited published endurance from a named vehicle. Do not let 927 km become a
ranking."* ChatGPT bağımsız olarak aynı yere işaret etti.

**Altıncı propagasyon hatası, ve en utanç verici olanı:** iddiayı iki adımdan kaldırıp üçüncüde
yeniden kurdum. Cümle çıkarıldı; yerine menzillerin **kapalı döngü değerleri** olarak taşındığı
ve hiçbir sıralama kurmadığı yazıldı.

## 2. Grok'un iki yapısal bulgusu

**(a) *"On these assumptions the architecture closes"* yalnız HAFİF hat için doğru.**
`aero/closure.py` ağır tasarımı çalıştırmıyor (denetlendi: sıfır atıf). Ağır hat sayfada yalnız
5,1 s dönüş süresiyle görünüyordu — sanki bu döngüden geçmiş gibi. Cümle *"for the **light**
design, which is the only one carried through this loop"* oldu, ve dönüş sürelerine *"both times
were sized on the reference geometry at its published mass; the closure above does not re-derive
them"* notu eklendi.

**(b) L/D girdi olarak donduruluyor; 57,5 kg'da C_L yükselir mi?** **Hayır, ve nedeni
görünür kılındı.** Döngü **kanat yüklemesini** sabit tutuyor (`S = MTOW/25,3`), dolayısıyla kanat
alanı kütleyle büyüyor ve seyir kaldırma katsayısı **dört kapanışta da tam 0,450**:

| MTOW | S | C_L |
|---|---|---|
| 49,35 kg | 1,951 m² | 0,4502 |
| 52,34 kg | 2,069 m² | 0,4502 |
| 57,51 kg | 2,273 m² | 0,4502 |

Grok'un endişesi geçersiz **ama sorusu doğruydu** — bir hakem aynısını sorardı. Sayfa artık kuralı
açıkça yazıyor ve alternatifin (kanat *alanını* sabitlemek) köşeleri iyimser yapacağını söylüyor.

## 3. DeepSeek'in sayısal tutarsızlığı — ve beklenenden büyük çıktı

*"Adım 6 alt ucu 8,80 diyor, Adım 10 8,79."* Denetlendi: `drag_sweep.ld(0.0381) = **8,79024**`.
Yani **8,79 doğru yuvarlama**, ve v7'nin Tablo 9'u 8,80 basmış.

**Ama etkisi tek haneden fazlaydı:** Adım 6'nın çarpım matrisi *yuvarlanmış* 8,80'den
hesaplanıyordu. Hassas değerle:

| | önce | sonra |
|---|---|---|
| B köşesi (8,79024 × 0,683) | 6,01 | **6,00** |
| turboşaft quadrotor'a karşı zarf | +%14 … +%51 | **+%13 … +%51** |
| en iyi aile | +%23 … +%51 | **+%22 … +%51** |
| elektrik quadrotor'a karşı, en iyi aile | +%4 … +%27 | **+%3 … +%27** |
| η_p = 0,85 olsaydı | 7,48–9,20 | **7,47–9,20** |

`effective_ld.py` artık hassas değerleri kullanıyor ve payları bir ondalıkla basıyor.

## 4. DeepSeek'in motor gerekçesi benimkinden keskin — alındı

Ben *"motor seyir gücüyle boyutlanıyor, kütle yalnız tahrik kesrinden hissediyor"* demiştim.
DeepSeek daha keskinini verdi ve doğru:

> **Motor, döngünün İKİ KEZ ücretlendirdiği tek çıktı.** Seyir gücü `W·V/(L/D)/η` — L/D ve η
> doğrudan içinde, **ve W'nin kendisi onları kütle döngüsünden zaten soğurmuş bir kapanış
> çıktısı.** Menzil doğrudan taşıyor ama kütle geri beslemesinden kaçıyor, çünkü yakıt kesri
> sabit. Kütle yalnız tahrik kesrinden hissediyor. **Yalnız motor çarpımı görüyor** — %46,1 >
> %33,0 > %9,9 sıralaması bundan.

## 5. Kabul edilen öteki düzeltmeler

| Düzeltme | Kim |
|---|---|
| *"the architecture closes"* → *"the analytical sizing loop closes for this architecture"* | ChatGPT |
| *"if none exists, the architecture does not close"* → *"the declared sizing package does not close"* | ChatGPT |
| Yayılım tanımı yazıldı: **(max − min)/min** | ChatGPT |
| *"most favourable case that can be constructed"* ve *"floor"* fazla genişti → *"within the finite-moment dynamic model… whether a real aircraft loses 5,4 m, more, or less is not settled by anything here"* | ChatGPT |
| **Hüküm önce:** *"only the second carries rotational dynamics, and that one does not support a zero altitude loss"* — okuyucu sayfayı yarıda bıraksa bile | Grok |
| *"no transition time to optimise"* → *"**in this point-mass model** there is no…"* | Grok |
| *"three to one"* → dört yüzde ayrı ayrı; **2,8×** menzilde, **2,4×** kütlede | Grok, ChatGPT |
| Faydalı yük **girdi**, MTOW çıktı — nedensel yön düzeltildi | DeepSeek |
| 0,0248'in **yalnız kuruluş sınamasında** geçtiği yazıldı | DeepSeek |
| *"50 kg ve 1000 kg"* → *"of order 50 kg and 1 000 kg — Section 10 closes the light one between 52 and 58 kg"* | DeepSeek |

**Kazanç-büyümesinin açıklaması için DeepSeek'in cümlesi yerine KAYNAĞIN kendi cümlesi alındı:**
*"What the kinematic model omits is not the difficulty of turning the aircraft but the trajectory
the aircraft flies while it is being turned"* (§3.15). Kendi açıklamamı uydurmadım.

## 6. DeepSeek'in defter uyarısı — Adım 11 yazılmadan kaydedilmeli

> *"Adım 10 zaten şunları yükledi: uç çerçeve ve serbest dönen rotor sürüklemesi (L/D braketinin
> içinde), sabit hatve uzlaşması (η_p aralığının içinde), burulma bedeli (0,817'nin içinde),
> ve hepsinin kütle/güç sonuçları (MTOW'un içinde). **Defter bunları TEKRAR eklerse, bu düz
> yazıda yapılan aynı çift sayımdır.**"*

**Defterin işi dar olmalı:** kapanışın sayılarının **neyi zaten içerdiğini** çözmek, ve **neyi
içermediğini** adlandırmak (tepki torku kanalını bırakmanın bedeli, 5,4 m geçiş tabanı, şeridin
eyleyici kütlesi, uç çiftlerine bağlı kalkış marjı). `paper/deferred-decisions.md`'ye yazıldı.

## 7. Qwen

Q1–Q3 kullanışlıydı; kuruluş sınamasını bir güç olarak adlandırması yerindeydi. **Q4 ve Q5 yine
döngüye girdi** — aynı paragrafı beş altı kez tekrarlayıp *"OK, I think I'm overcomplicating
this"* diyerek yeniden başladı. Bu, üst üste ikinci tur.

---

# Tur 54 — Adım 12 yazılırken: iskeletin vaadi daraldı

## 1. Fatura 1 ölçekte SINANAMIYOR — tampon her iki ölçekte de girdi

İskelet Adım 12'ye *"üç para biriminin gerçekten üç olduğunun kanıtı"* diyordu. v7 §3.9 *"the
mass bill rises"* diyor ve tamponu %3,6 → %4,0 veriyor.

**Denetlendi: ikisi de girdi.** `aero/mass.py` tamponu `m_pil` parametresi olarak alıyor
(varsayılan 1,8 kg); `baseline.py` `f_tampon` olarak. **Hiçbir kod tamponu askı enerjisinden
türetmiyor.** Adım 11'de Grok'un şüphesiyle hafif ölçek için bulunan şey, ağır ölçekte de aynı.

**Sonuç:** %3,6 → %4,0 iki seçim arasındaki fark, bir ölçekleme sonucu değil. **Üç faturadan
yalnız ikisi ölçekte sınanabiliyor** — Fatura 2 düşüyor (hesaplandı), Fatura 3 %5 içinde tutuluyor
(tasarım kuralıyla). Ayrışma bu ikisi arasında gösteriliyor; Fatura 1 sınanmamış.

**Ve kabuk kütlesi yerine konmuyor:** gövde her mimarinin taşıdığı yapıdır, Adım 2'nin Fatura 1'i
değil. Onu *"kütle faturası"* saymak tanımı sınava uydurmak olurdu.

**Tamponu türetmek mümkün ama yapılmadı** — o, batarya özgül gücü sorusuna, yani Adım 14'ün 3,8×
paragrafına girer. Grok'un şartı korunuyor.

## 2. v7'nin üç haneli uyumu doğrulanamadı

v7 §3.9: *"solidity falls from 0.075 to 0.044 … Their product, 1.73 × 1.78 = 3.08, is the
predicted ratio; the computed ratio is 3.04."*

- 0,075 / 0,044 = **1,70**, 1,73 değil. Çarpım **3,03**, 3,08 değil.
- 0,075 ve 0,044 **hiçbir betik çıktısında yok** — yalnız v7 düzyazısında (`grep` ile arandı).
- v7'nin kendisi hesaplanan oranın aralık boyunca 2,08–4,40 oynadığını söylüyor.

**Adım 12 üç haneli uyumu iddia etmiyor.** Mekanizma, yön ve mertebe veriliyor; oran *"yaklaşık
üç"*. §4 gereği gövdede *"v7 şöyle diyordu"* anlatısı yok; tutarsızlık yalnız burada kayıtlı.

## 3. Ağır tasarım menzili hiç verilmiyor

Elimizdeki her ağır menzil bir bakımdan kısmi: 1.814 km (rotor yüklenmemiş, η_p 0,80), 1.571 km
(rotor yüklenmiş, η_p 0,80), 1.398–1.517 km (η_p yeniden çözülmüş, rotor yüklenmemiş). **İkisini
birden taşıyan kapanış yok.** Adım 12'nin ihtiyacı da yok — ayrışma güçler, yüklemeler ve
sürükleme terimleriyle gösteriliyor.

---

# Tur 55 — Adım 12'nin dört okuyucu yanıtı: Fatura 2'nin mekanizması bir hesap hatasıydı

## 1. Ağır rotor terimi üç kurulum hatasıyla hesaplanmıştı (DeepSeek'in işaretiyle bulundu)

**DeepSeek:** *"For a fixed rotor, blade drag scales with q, and C_D0 = drag / (q S) is
q-independent. The formula implies that C_D0 falls with q."* Formülün türetimi açık değil dedi.

**Denetlendi ve haklı çıktı.** `aero/heavy_rotor.py` `tip_propeller`'ın modül sabitlerini ağır
değerlerle değiştirip aynı fonksiyonları çağırıyordu. Üç değer modül sabitinden gelmiyordu:

| | Ne olmuştu | Etkisi |
|---|---|---|
| 1 | `sifir_tork(c, th, V=V_SEYIR)` — varsayılan argüman **tanım anında** 30 m/s'ye bağlı. Denge 30 m/s'de çözüldü, `dcd0()` ise 40 m/s'nin q'suna böldü | terim ~×0,56 küçük; **"q artar, fatura düşer" mekanizmasının imzası** |
| 2 | `hover_tasarla(..., om=2100.0)` — hafif rotorun tasarım devri. 0,67 m'de **703 m/s tasarım uç hızı**; palet askıda **uç Mach 0,92–1,09** | veter küçük; **"dolgunluk 0,075 → 0,044 düşer" teriminin imzası** |
| 3 | `r_h = 0,15 R` ithal anında 0,015 m; R değişince güncellenmedi | göbek %4,5 R |

**`--eski` bayrağı eski kurulumu aynen üretiyor:** c_l 0,70'te 0,00505 (≈ 0,0051), aralık
0,00350–0,00740 — v7'nin sayıları birebir. Hata geri konunca yakalanıyor.

**Düzeltilmiş kurulum** (aynı tasarım uç hızı 210 m/s, göbek 0,15 R, denge 40 m/s'de):

| c_l | FM | askı Mach | dolgunluk | ΔC_D0 | /hafif |
|---|---|---|---|---|---|
| 0,55 | 0,768 | 0,67 | 0,1122 | 0,01003 | 0,65 |
| 0,68 | 0,769 | 0,66 | 0,0999 | 0,00681 | 0,44 |
| 0,85 | 0,751 | 0,65 | 0,0878 | 0,00447 | 0,29 |

**Mekanizma deneyi (c_l 0,68):**
- **q:** aynı ağır palet 30 → 40 m/s: 0,00748 → 0,00681, **−%9**. q ölçeklemesi −%44 verirdi.
  Sıfır torkta serbest dönen rotorun devri hızla orantılı; kuvvet q ile ölçekleniyor, **q sadeleşiyor.**
  Kalan −%9 Reynolds etkisi.
- **Dolgunluk:** 0,0754 → 0,0999, **×1,33 — artıyor.**
- **Reynolds:** medyan kesit Re 81.689 → 556.336, ×6,81. Ağır palet hafif hattın Re'sine
  indirilince 0,0181 = **hafifin 1,18 katı.** Düşüşün tamamı (ve biraz fazlası) Reynolds'tan.

**Sonuç:** Fatura 2'nin rotor terimi ölçekle **hâlâ düşüyor** (0,29–0,65), ama mekanizma
**tamamen değişti** ve sonuç artık **düşük Re'deki kesit sürüklemesi modeline** (NeuralFoil,
NACA 0012, ölçülmedi) dayanıyor. Hafif uç 10⁵'in altında.

**Etkilenen v7 yerleri (dondurulmuş kayıt, düzeltilmedi):** §3.8 Tablo 14 (0,0051, C_D0 0,0251,
L/D 11,78, 1.077 kg, 1.571 km), §3.8 *"figure of merit is 0.65 to 0.66"*, §3.9 mekanizma paragrafı
ve 3,04/3,08 uyumu. **Zenodo'daki sürüm bu hatayı taşıyor** → `deferred-decisions.md`.

## 2. `verify.py` hatayı YENİDEN ÜRETİYORDU

Ağır rotor denetimi betikle aynı varsayılan argümanlarla çağırıyordu (`sifir_tork(_c, _th)`,
`hover_tasarla(cl_hedef=_cl, T_hedef=_T)`), dolayısıyla aynı hatayı tekrarlayıp 0,0035–0,0074'ü
"doğruluyordu." §3'ün *"sessizce boş dönen denetim"* sınıfının akrabası: **boş dönmüyor, yanlışı
onaylıyor.** Düzeltildi; artık düzeltilmiş kurulumu sınıyor **ve eski kurulumun bu beklentiyi
karşılamadığını da** sınıyor. 45 kontrol, 0 sapma.

## 3. Yeniden adlandırma commit'i betikleri kırmıştı (kendi bulgum)

`d2c181c` (*"Bütün depo İngilizce adlandırmaya geçirildi"*) ithalleri değiştirmiş, çağrıları
bırakmış: `rotation.py` (`kutle.butce` ×2), `roll.py` ve `yaw.py` (`donme.dagilim`),
`cfd/plate/{model_discriminate,schemes,omega_wall}.py` (`duzlevha.kur`). **Hepsi NameError.**
Onarıldı; `rotation.py`, `roll.py`, `yaw.py` koşuldu (çıkış 0). `cfd/plate` OpenFOAM ister,
yalnız derlendi.

**Tablo 15 (221,5 / 65,6 / 27,7 / 13,4 kW) hiçbir betik çıktısında yok.** Onarılan `rotation.py`:
5,1 s'de üçgen profil 127,0 N/çift → 4 × 6486 W × (127,0/200,1)^1,5 = **13,1 kW**; ×(5,1/2)³ →
**217,6 kW (%101)**. Tablo %2 içinde tutuyor; Adım 12 gövdesinde **yuvarlatıldı** (~220 / ~13 kW).

## 4. Fatura 3 oranı motor payı taşıyor (Grok'un işaretiyle; benim ihmalim)

**Grok:** *"The 5 percent is hover/engine, which also moves with cruise L/D and speed; that is a
second rule riding along."*

Daha kötüsü: iki yayımlanmış tasarımın motor payı **aynı değil** — 2,6/1,7 = **1,53** ve
54,3/39,2 = **1,39**. `aero/baseline.py` satır 447–461 bunu **zaten kaydetmişti** (*"makale bunu
hiçbir yerde söylemiyor"*). Adım 12'yi yazarken taşımadım — §3.1'in *"çekince yalnız Türkçe
yerde duruyorsa İngilizce gövdede yok demektir"* sınıfı, bu kez kaynak bir betik yorumu.

Eşit payla ağır motor 60,0 kW, oran 3,61, değişim **%14**. Gövde artık **%5–14** diyor.

## 5. Fatura 1 türetimi (DeepSeek, Qwen)

**DeepSeek:** sabit özgül güçte tampon kesri açık/kg'yi izler, %1,6 düşer, *"cannot be tested"*
yanlış. **Aritmetik eksik:** yalnız açık kesrini (1−1/4,19 → 1−1/3,98) almış, askı/kg'nin
0,2176 → 0,2162 değişimini atlamış. Doğrusu (10,9−2,6)/50,1 = 0,1657 → (216,2−54,3)/1000 = 0,1619,
**−%2,3.** Ayrıca *"multiplied by hover duration … divided by specific power"* boyutsal olarak
tutarsız (enerji / özgül güç = kg·s).

**Qwen:** türetim mümkün ama önemsiz — Fatura 1'i Fatura 3'ü düz tutan kuralla düz tutar.

**Benim vardığım daha keskin hâl:** türetim tamponu **askı gücü ile motor derecesinin**, yani
Fatura 3'ü ölçen **iki niceliğin fonksiyonu** yapıyor. Böyle türetilen tampon Fatura 3'e
**türetimin kendisiyle kilitli**; ölçek karşılaştırması ayrışmayı değil türetimi sınar. Adım 3 ve
11 zaten *"yapılandırma bir güç faturasını kütle faturasına çeviriyor"* diyordu — bu, o cümlenin
ölçekteki sonucu. Gövde: *"whether the two are separable here is not established."*

## 6. Reddedilenler

- **DeepSeek Q2, "Fatura 2 fiziksel, Fatura 3 sözleşmesel":** Fatura 2'nin terimleri de tasarım
  seçimi (palet, seyir hızı; şimdi Reynolds, yani veter ve hız). Ayrıca *"W^1.5"* sabit disk
  alanının üssü; geometrik benzerlikte askı gücü W^(7/6).
- **ChatGPT'nin "yayımlanmış ölçek karşılaştırmasına birincil kaynak" notu:** gövde artık
  3,08'i hiç anmıyor; düştü.

## 7. Uygulananlar (kim)

| Ne | Kim |
|---|---|
| Başlık: *"Scale does not lock two of the charges together; the third is not tested"* | ChatGPT (önerisi daraltıldı) |
| *"kilitlenmeme"*, *"independent"* değil | ChatGPT |
| Devir: *"any ranking must"* → *"where one architecture pays less of one charge and more of another"* | ChatGPT |
| *"The argument requires only two"* | DeepSeek, Qwen, Grok |
| İki uç yayımlanmış çift; Adım 10 köprüsü | Grok, DeepSeek |
| Disk yüklemesi *"approximately"*, %1 | DeepSeek |
| *"cruises faster at a better L/D"* çıkarıldı (ağır L/D temeli) | DeepSeek |
| Farkla başla, düzlükle değil | Qwen |
| *"harder case"* yalnız rotor terimi; *"usual expectation"* çıkarıldı | Grok |
| Ağır menzil gerekçesi somut | Qwen |
| Sabit hatve açığı 23,0 → **22,9** (betik) | kendi denetimim |
| *"Refusing the variable-pitch hub costs as much or more"* — **ChatGPT'nin Tur 53'te Adım 11'de yakaladığı aşırı atıf Adım 12'de tekrar etmişti** (§3.1 yayılma); Adım 11'in dili getirildi, emekli listesine eklendi | kendi denetimim |
| Adım 11 devri: *"tests that separation directly"* → *"asks whether they move together"* | kendi denetimim |

## 8. `paper/build/v8_stale.py` — yeni

§3.1 v8 için makineye devredildi: 17 emekli ifade/sayı, İngilizce gövdeler + ALL-STEPS. `--sina`
eski Adım 12'yi (d64d4ea) tarıyor ve **10 emekli değer yakalıyor**; ilk koşuda yeniden kurulmamış
ALL-STEPS.md'yi de yakaladı.

## 9. "50 kg" taraması (DeepSeek)

1–11'in İngilizce gövdelerinde niteliksiz *"50 kg"* **yok.** Adım 6 zaten köprü kuruyor
(*"Section 10 closes the light one between 52 and 58 kg"*); Adım 10'daki 50,1 inşa sınamasında.

---

# Tur 55 (devam) — Adım 13 yazıldı: sıralama sözleşmeye ait, ama tersine dönme zarfın yarısında

## 1. Yeni hesap: `aero/contracts.py`

Adım 10'un dört kapanışının her birinde üç mimari × üç sözleşme. A'nın sütunu Adım 10'u birebir
üretiyor (üretmezse betik durur). Taban: A η_p hesaplanmış (0,632/0,683), B ve C 0,80 (varsayım;
`chain_resolve.py`'nin mimariye özgü gerekçesi); tampon %3,6 hepsinde, motor seyre boyutlu hepsinde
(Fatura 3 ortak); B 13/17 ve %10 kaldırma grubu; C 1,00 ve %5 eğme.

**Sonuç (B/A menzil farkı):** sabit kesir +55…+84 %, sabit yakıt +28…+54 %, sabit MTOW −13…+7 %.
Salınım 67–77 puan. **Sabit MTOW'da işaret zarfın içinde değişiyor:** üst palet ailesinde A önde,
altta B önde. Tilt her yerde +93…+141 % önde (sınır). Kütle: B %38–43 ağır → A %27–30 hafif.

**Duyarlılık:** kaldırma grubu %5 → A hiçbir yerde önde değil; %15 → sabit MTOW'da her yerde önde;
hepsi aynı η_p → sabit MTOW'da her yerde önde; B cezası sabit artış → taban ile aynı desen.

## 2. v7'den farkı ve nedeni (gövdede yok, §4)

v7 Tablo 9: B/A +24…+45 % (sabit kesir), kütle üstünlüğü %32–36 — hepsi η_p 0,80 tabanında.
Hesaplanmış η_p A'nın seyir gücünü ve motorunu büyütüyor (itki kesri 0,176–0,198), B ve C 0,80'de
kalıyor; olumsuz uçta ×1,1 pay. Menzil açığı büyüdü, kütle üstünlüğü küçüldü. §0.7: sayı tez değil.

## 3. Yayılım (§3.1)

- **Adım 2'nin öngörüsü** *"will reverse when the sizing rule changes"* idi. Adım 13 tersine dönmeyi
  dört kapanışın ikisinde buldu. Cümle *"will move … toward the lighter arrangement … and can
  reverse"* oldu. **Bu, sınanmadan sonra daraltmadır** — okuyuculara açıkça soruluyor.
- **Adım 9** *"it reverses across the three contracts"* → sözleşmeyle oynuyor, bir sözleşmede işaret
  zarfın içinde değişiyor, ölçülmemiş bir kesre bağlı; tilt bir sınır. **Sayı konmadı** — iskelet
  Adım 9'u *"hiçbir sayıdan önce"* diye tanımlıyor; ilk düzeltmede "some seventy points" yazmıştım,
  çıkardım.
- **Adım 10** *"where it is made and where it reverses"* → *"where it is made"*.
- **CLAUDE.md §0** eksen tablosu ve 24–45 / 32–36 notu.
- `v8_stale.py`'ye dört emekli ifade eklendi (22 değer).

## 4. Kendi yakaladıklarım

- Adım 13'ün ilk yazımında tilt için *"not behind on either count"* — **yanlış**, tilt %0,5–5,4 ağır.
  Doğrusu: takas var ama çok dengesiz; sabit MTOW bile tilt'i %93–130 önde bırakıyor.
- **Adım 2'de sarkan atıf:** *"the doctoral study whose wind-tunnel campaign supplies Table 1"* — v8'de
  numaralı tablo yok. *"is quoted above"* oldu.

---

# Tur 56 — Tur 55 metnine (external-review-59) dört yanıt

**Dördü de:** Reynolds ayrıştırması adil; Fatura 1'in Fatura 3'e kilitlenmesi sağlam ve *"aynı
fatura"* demek değil; Adım 2'nin daraltılması **düzeltme, kale taşıma değil**; Adım 13 bildirilmeye
değer, ama sıralama olarak değil; üç yükümlülük doğru.

## Uygulananlar

| Ne | Kim |
|---|---|
| Reynolds bulgusu *"within the blade-element and section-polar model"*; ayrıştırma, nedensellik değil | ChatGPT, DeepSeek, Grok |
| *"in the section polars used here"* bulgu cümlesinin içinde | Grok |
| *"the whole of the fall, and a little more"* → *"18 percent above"* | DeepSeek |
| Düşük Re belirsizliği iki yönlü; hafif terim daha belirsiz; Adım 11'e çekince | DeepSeek |
| Aralık uçları fiziksel sınır değil | DeepSeek |
| Fatura 1–3 *"bağlaşık, özdeş değil"*; bağlaşım Adım 3'ün iddiası | DeepSeek (pozitif ifade) + ChatGPT/Grok/Qwen (sınır) |
| *"requires only two charges that are not locked together"* | ChatGPT |
| Adım 2 öngörüsü koşullu biçim (*"break even"*) | ChatGPT, Qwen |
| Fatura 3 ortak = soru seçimi, yönü **hesaplandı** (aleyhimize; rakipler tamponsuz: B 381 kg, s3'te kapanmıyor) ve neden kullanılmadığı (A'nın tamponu Adım 14'ün sorusu) | Grok, ChatGPT, DeepSeek |
| Rakipler *"bu planform artı iki ek"* | Grok |
| Tilt 93–141'in her cümlesinde *"bound"* | Grok |
| *"Carry the audit"* rakip sütunları için karşılanmıyor; temel/asimetri beyanı buna katlandı | Grok, DeepSeek |
| Tüm sözleşmelerde kararlı sıralama bildirilebilir | DeepSeek |
| İşaret bir parametre sonucudur, en çok ölçülmeye değer | Qwen |
| Duyarlılık tablosuna kayma sütunu; (d) durumu betiğe | kendi denetimim |

## Reddedilen / düzeltilen iddialar

- **DeepSeek: kayma "hesaplanan–varsayılan asimetriye dayanıklı".** Denetlendi: pervane ve sürükleme
  tabanına dayanıklı (65–77 puan) ama **kaldırma grubuna değil** (14–134). "Some seventy points"
  sonuç cümlesinden çıktı; kayma, kütle farkının kendisi.
- **DeepSeek: "L/D'ler farklı tabanda".** İkisi de aynı temiz gövde üzerinde aerodinamik oran; η_p
  aynı cümlede ayrı veriliyor. Yalnız uçlar adlandırıldı.
- **DeepSeek: Adım 2'ye "bu cümlenin eski hâli şöyleydi" yazılsın.** Reddedildi: CLAUDE.md §4 — dergi
  gövdesinde önceki sürüm anlatısı yok. Daraltma Türkçe başlıkta ve burada kayıtlı.
- **DeepSeek: 0,0154 "zincirdeki en belirsiz nicelik".** Fazla geniş (temiz yüzey braketi de geniş).
  *"İki rotor teriminden daha belirsiz olanı"* yazıldı.

## Kendi bulgum: Adım 2'nin başlığı Adım 12 ile çelişiyordu

*"The charges behave as one quantity in three currencies"* — Adım 12 tam tersini sınıyor ve *"not one
quantity under two names"* diyor. Okuyucuların elinde Adım 2 yoktu, göremezlerdi. İskeletin niyeti
*"üç bağlaşık fatura"*. Başlık *"The charges are coupled: remedies move cost between them"* oldu.
§0.2 sınıfı: bir sonuç yazıldığında, **onu önceden tarif eden başlıklar** da açılıp okunur.

---

# Tur 56 (devam) — Adım 14 yazıldı; tampon bara tabanında, ve bir istasyon karışıklığı geri gelmişti

## 1. `aero/buffer.py`

Adım 10'un dört kapanışında tampon talebi **bara tabanında** (`thrust.py`'nin kuralı: P_mil/(0,92×0,95)
− P_motor×0,90). Kapanışların ima ettiği özgül güç: askı 4,68–5,23, kalkış 5,53–6,09 kW/kg. Tampon
özgül güçten döngü içinde türetilince döngü Adım 10'u birebir üretiyor (sınama).

Ölçülmüş özgül güçte (Yu ve ark. 2026, bu tur PDF'ten okundu): 1,49 kW/kg → 94,6–101,2 kg (+%76–81),
tampon %13,4–14,7; 0,892 → ~335 kg (kapanmamaya yakın); 0,724 → kapanmıyor; 4,0 (Barrett NIAC) →
56,6–61,2 kg. Sabit MTOW'da faydalı yük 1,49'da ~7 kg.

**3,8× → 3,7–4,1×** (kalkış/1,49). v7'nin 3,8'i yayımlanmış tasarımdaydı (5,63/1,5).

## 2. İstasyon karışıklığı v8'e geri gelmişti (kendi bulgum)

v7, `thrust.py`'de *"(10,9 − 2,6)/1,8 rotor milinden motor milini çıkarıyor"* diye 4,61'i 5,63'e
düzeltmişti. **Ama Adım 11'in açık sayısı (`ledger.py`) ve Adım 12'nin Fatura 1 türetimi aynı mil−mil
çıkarmasını yapıyordu.** Bara tabanında: Adım 11 0,168–0,188 kW/kg (%12; önce 0,128–0,150, %17), Adım 12
0,202 → 0,199 (önce 0,166 → 0,162). Sonuçlar (en çok tampon isteyen köşe en az tamponu alıyor; ölçekle
~%2) değişmedi. `ledger.py` düzeltildi, iki adım ve Türkçe tabloları güncellendi, emekli listesine
eklendi. **§3.1 sınıfı: bir düzeltme (v7'nin istasyon kuralı) yeni yazılan koda yayılmamıştı.**

## 3. Kaynak

- Yu ve ark. 2026 (*Batteries* 12:317): Tablo 3 — 724 W/kg (24S1P, 110 A), 892 W/kg (24S4P, 4×110 A'dan
  hesaplanmış); 10,68C: 1394,3 Wh, 4 dk 09 s, 13,5 kg → **1,49 kW/kg türetildi**; 55,1 °C, sınır 60 °C.
- **v7'nin *"the highest rate yet measured on a flown pack"* ifadesi kaynağa uymuyor**: 1,5 kW/kg tezgâhtaki
  24S1P'de; uçan 24S4P. *"yet"* aranmamış (§2.2). v8 gövdesinde yok; emekli listesinde.
- Barrett ve ark. 2023: *"the specific power (4 kW/kg) is about twice that of existing batteries"* — birebir.

## 4. Adım 14'ün ilk yazımında kendi yakaladıklarım (§0.2)

- *"Section 13 … none of its orderings rests on this item"* — yanlış; tampon ağırlaşınca sıralamalar
  kayabilir, hesaplanmadı.
- Düşük Re için *"yöntemler denendi ve çelişiyor"* — yanlış; tek yöntem kullanıldı.
- 4 kW/kg satırı +6,5 aşağı yuvarlanmalıydı (+6…+8).
- Kapanış paragrafında *"a factor of about four"* — 3,8×'in tek evi kuralını çiğniyordu; çıkarıldı.
- Kabuk yoğunluğu: *"meets it"* değil *"leaves room for the 13 kg payload"* (`mass.py`'nin kırılma tanımı).

---

# Tur 57 — Tur 56 metnine (external-review-60) dört yanıt

**Dördü de:** tampon paragrafının gücü doğru; *"the aircraft exists"* fazla (ChatGPT, Qwen, DeepSeek;
Grok: *"loop sensitivity, not a second aircraft"*); mekanizma iddiası depodan bağımsız; Adım 2'nin
başlığı ve koşullu öngörüsü 12–13 ile tutarlı.

## Uygulananlar

| Ne | Kim |
|---|---|
| *"the aircraft exists"* → *"the loop closes"*; yeniden kapanış paketin duyarlılığı, 100 kg'da yapısal kapanış değil; %30 gövde iki kat kütlede kanıtlanmamış | ChatGPT, Qwen, DeepSeek, Grok |
| Anma türleri farklı: tepe talep / tezgâh ortalaması / sürekli / tasarım varsayımı; 3,7–4,1 tepe-tezgâh oranı | Grok, ChatGPT |
| Hangi kural: kanat/disk yüklemesi ve AR sabit → L/D ve menzil taşınıyor | DeepSeek |
| Depo **neye ulaşıyor**: kapalı kütleler ve 13 kg; 927–1233 km yalnız yakıt kesri tutulduğu için; Adım 5'in dikey evresi; Adım 13 | Grok, DeepSeek |
| Adım 6: **oran olarak** etkilenmez; uçak karşılaştırması olarak Adım 10'un kütlelerini anlatır | Grok |
| Defter dönüşümü ucuz depoda kaydetti, burada gerçek fiyatı | DeepSeek |
| Tablo: tampon enerjisi (4 dk), elektrik yolu tepe/ısıl, şerit+fairing, durdurulmuş hâl, yer işletimi/iniş yükleri; gövde satırı analiz + inşa | Grok, ChatGPT, Qwen, DeepSeek |
| *"measurement"* → *"validated data"* | ChatGPT |
| İstasyon etiketleri: Adım 10 tablosu, Adım 11 ve 12'nin Fatura 3 oranı (*"a ratio of installed hardware"*); Adım 11'in *"the buffer supplies the difference"* cümlesi kaldırıldı | Grok, ChatGPT, DeepSeek |
| Adım 2: *"break even"* tanımlandı | DeepSeek |
| Adım 13: *"Until that item is settled, … neutral"* → *"holding it common charges all three the same assumption"* | Grok (açmadan, tek cümle) |

## Denetimin bulduğu: `baseline.py`'de ikinci istasyon karışıklığı (DeepSeek'in önerisiyle)

DeepSeek: *"Worth a one-line audit of the script."* Denetlendi: `motor_hover=True` yolunda motor derecesi
**rotor milindeki askı gücüne eşit** alınıyordu. Seri hibritte motor mili = askı / (0,92×0,95×0,90) =
askı × 1,27. Bu yol yalnız Adım 13'ün (d) durumunu (tamponsuz rakipler) etkiliyor.
`motor_hover_carpan` eklendi (varsayılan 1,0 — v7 tablolarını korur; verify 45/45).

**Düzeltilmiş (d):** lift+cruise sözleşme 1 ve 3'te **kapanmıyor**, sözleşme 2'de %38–47 geride; tilt
sınırı sözleşme 1'de 520 kg (~10×), menzil önü değişmeden; sözleşme 3'te kapanmıyor. (Eski: 381 kg,
−23…−11.) Yön aynı, büyüklük daha keskin. Tur 56 metnindeki 381 kg bu yüzden yanlıştı.

## Reddedilen / düzeltilen

- **DeepSeek: pist iddiası depoya bağlı değil** ("sized, not demonstrated"). Kısmen yanlış: dikey evre
  **bu depoyla** boyutlandı; ölçülmüş depoda yalnız daha ağır pakete boyutlu. Adım 14 bunu söylüyor.
- **Qwen'in iki "Step 8" alıntısı** (*"the quantity a future measurement must return is ΔC_L"*, *"whether
  such a fairing develops the side force"*) **v8'de yok, v7'den** (v7 satır 836). "Step 2.9 / 3.4"
  pasajları da v7'nin §2.9/§3.4'ü. Qwen yine bilgi tabanındaki v7'yi okudu. **Öz yine de doğru**
  (şerit ve fairing ölçülmedi) ve tabloya girdi.
- **DeepSeek: 4,19 "understated"; ortak istasyonda ~5,33.** Oran hatalı değil, **tanımsızdı**: rotor mili
  askı / motor mili derece bir donanım oranıdır. Etiketlendi (ChatGPT'nin 1. seçeneği).

---

# Tur 57 (devam) — oran incelemesi, son bölüm, ve son bölümün açtığı iki eski çelişki

**Yazar:** *"Kısaltma işi şimdilik yapılmayacak. Mutmain olmadan kısaltma olmayacak. Oran işini yap. Adım 9
için dört ekseni tekrarla. Son bölümü yaz."*

## Oran (`paper/v8-proportion.md`)

Katkının net cümlesi metnin **%57**'sinde ilk kez geçiyor; Adım 7 (birleştirme) %4,8; hesaplar (10–14)
%42,5 ve mekanizmaya neredeyse hiç dönmüyor; Adım 12 en uzun (%10). §0.6 çerçeve adımlarının boyunu
koruduğu için teşhis kesmeye değil **yerleştirmeye** yönelik: P1 (Adım 1'e katkı cümlesi), P3 (10–13'e yer
cümlesi) öneri; P2 (son bölüm katkıyı merkeze koyar) uygulandı. Kısaltma yok.

## Son bölüm (Adım 15)

Adım 9'un dört ekseni sırasıyla, her biri neye dayandığıyla; sayı yok, atıf yok; katkı üçüncü eksende
merkezde. §0.2 denetiminde beş kendi hatam düzeltildi (sürekli anma, *"whose cost"*, *"nothing else in
the paper"*, *"a ranking is a weighting"* evrenselliği, Adım 6'dan taşınan aşırı atıf).

## Son bölümü yazmak iki eski çelişkiyi açtı

1. **Adım 9'un bağımlılık tablosu:** pist iddiası *"does not depend on … the battery gap"*. Adım 14 dikey
   evrenin bu depoyla boyutlandığını gösterdi. Düzeltildi: *"it does depend on the energy store"*.
2. **Adım 6:** *"It is this aircraft's own refusal of the variable-pitch hub"* — Tur 53'te ChatGPT'nin Adım
   11'de yakaladığı aşırı atıf Adım 6'ya yayılmamıştı (§3.1, bir kez daha). Düzeltildi; emekli listesinde.

---

# Tur 58 — Tur 57 metnine (external-review-61) dört yanıt

**Dördü de:** Adım 15 kaynaklarına sadık; mekanizma ekseni dar gücünde; P1 ve P3 doğru; Adım 7 büyütülmesin;
Adım 14'ün *"the loop closes"* ifadesi tutuyor.

| Ne | Kim | Yapılan |
|---|---|---|
| Kapanış cümlesi *"combines runway-independent vertical operation"* → boyutlandı, gösterilmedi | ChatGPT (*"mandatory"*) | Adım 15 **ve Adım 9**: *"sized to combine … arranged to do so … and an account of what the combination costs"* |
| Adım 9 ile 15'in "bağlı değil" listeleri farklı | Grok, DeepSeek | İkisi de: sürükleme, η_p, sözleşme, menzil sonucu, depo, geçiş aerodinamiği |
| Adım 8'de *"for anyone on this class of configuration"* — emekli evrensel geri gelmiş | Grok | *"for the methods used here and the published comparisons against which they were checked"* |
| Adım 6: *"at e = 0.85 … 7.48"* — gösterim çarpışması ve süpürülmemiş 7,48 | Grok, DeepSeek | *"η_p = 0.85 … 7.47"* |
| Adım 15 mekanizma listesi: değişken hatve ve özel kaldırma rotorları "yeniden yönlendirme" değil | Grok | *"— nor any of the other mechanism classes that architectures use to change regime or to take a rotor out of one regime's flow"* |
| *"one of the measured continuous ratings"* belirsiz | DeepSeek | *"the unit pack's continuous rating"* |
| Adım 5: *"the difference between that peak and the cruise demand"* + depo çekincesi | DeepSeek | *"what the engine cannot deliver of that peak — at a specific power Section 14 examines"* |
| Adım 15 bilinmeyenleri sıkıştırıyor | DeepSeek | *"Section 14 gives the full list"*; sertifikasyon tek cümle |
| Tabloya: palet ailesi seçim ölçütleri | ChatGPT | satır eklendi (Adım 10'un kendi listesi) |
| Tabloya: askı tork artığı | Qwen (bu kez v8'den, doğru) | hover-control satırına |
| İrtifa satırı: kendi duyarlılığı hesaplandı, Adım 6 karşılaştırmasına etkisi hesaplanmadı | DeepSeek | eklendi |
| 335 kg satırına marjinallik | DeepSeek | **Alınmadı** — tablo ve metin zaten *"set by nearness to non-closure"* ve *"only just closes"* diyor |
| Dört ekseni Adım 1/2'de adlandırmak | DeepSeek (isteğe bağlı) | **Alınmadı** — iskelet yazarın; P1 ile birlikte yazara soruluyor |
| P1, P3 | dördü de *"evet"* | **Yazarın kararı (E3)**; taslak cümleler yazara sunuldu |

**Qwen bu tur yalnız v8 metninden çalıştı** ve Adım 8'den doğru bir kalem (askı tork artığı) getirdi.
