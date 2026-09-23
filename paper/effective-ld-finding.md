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
