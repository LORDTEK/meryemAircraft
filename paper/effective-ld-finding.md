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
