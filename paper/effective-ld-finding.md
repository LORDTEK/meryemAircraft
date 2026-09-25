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

Johnson & Silva'nın gösterim listesi (s. 94, `references/1521_Johnson & Silva_122721.pdf`):

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
| Adım 7'de *"for anyone on this class of configuration"* — emekli evrensel geri gelmiş *(Tur 58 uygulamasında düzeltildi: bu satır ve a80650a commit mesajı "Adım 8" diyordu; değişiklik Adım 7'de)* | Grok | *"for the methods used here and the published comparisons against which they were checked"* |
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

## Tur 58 uygulaması — P1 ve P3 (yazarın kararı: *"P1 ve P3'ü uygula"*)

| Yer | Onaylı taslak | Yazılan | Neden farklı |
|---|---|---|---|
| Adım 1 sonu | *"The contribution is the architecture: a configuration that changes regime by rotating …"* | *"… a configuration **arranged to** change regime by rotating the airframe rather than its propulsors, and so carrying no mechanism that reorients a propulsor."* + üçlü *"are how that contribution is presented and priced"* | *"changes regime"* geçişin gösterildiğini ima ediyordu; Adım 7 ve 15 bunu iddia etmiyor (§0.2) |
| Adım 9 | — | Üçlü: *"The contribution is the architecture, and the paper presents it as the combination, …"* | **Yayılma (§3.1):** Adım 9 aynı üçlüyü katkı diye söylüyordu; P1'le çelişirdi |
| Adım 10 | *"… it does not prove the count, and it does not show the aircraft can be built."* | *"… it does not bear on the count of mechanism classes, which rests on the inventory of those sections alone."* | *"Can be built"* bir alt cümlede zaten var; *"the count"* bağlamsız okunuyordu |
| Adım 11 | *"… attributes that price to the three charges; it adds none."* | *"Like the closure, the ledger prices the arrangement; the count of mechanism classes is not an entry in it."* | *"It attributes. It does not add."* iki satır aşağıda zaten var; taslak katkıya yeri söylemiyordu |
| Adım 12 | *"This section tests whether … three quantities or one; it does not bear on the mechanism claim."* | *"Either answer leaves the mechanism claim where it was; that claim rests on the inventory of Sections 7 and 8."* | İlk yarı bölümün açılış sorusunu tekrarlıyordu |
| Adım 13 | *"… the mechanism claim is not a ranking and is not at stake here."* | Özü aynı; *"how the price computed in Sections 10 and 11 enters a comparison"* | — |

---

# Tur 59 — Tur 58 metnine (external-review-62, on beş adımın tamamı) yanıtlar

**Grok, DeepSeek, Qwen tam yanıt verdi; ChatGPT yalnız dosyayı aldığını ve ne denetleyeceğini yazdı, bulgu
vermedi.** Üçü de: argüman akıyor; P1 *"arranged to"* doğru güçte; P3 cümleleri iddia eklemiyor; Adım 7
birleştirme hamlesini taşıyor, büyütülmemeli; yasak eksenlerde ihlal yok.

| Ne | Kim | Denetim | Yapılan |
|---|---|---|---|
| **Kapanış geometrisi** — Adım 8'in tek planformu ile Adım 10'un dört alanı | Grok (C; yalnız çerçeve sorunu sandı) | **Gerçek hata, benim.** Adım 10'un alt uçları (1,98 m², 3,45 m, 1,20 m) **50 kg referans geometrisi**; en hafif kapanış 52,34 kg → 2,07 / 3,53 / 1,23. Hiçbir betik basmıyordu, hiçbir denetim sınamıyordu | Düzeltildi; `closure.py` artık basıyor; `verify.py`'de 7 yeni kontrol (eski alt ucu reddeder) → 52 kontrol |
| Adım 14 *"the regime change is made"* — P1'in emekli ettiği fiil | Grok (A) | Doğru; **Adım 15'te de ve Adım 7'de de vardı** (Grok yalnız 14'ü gördü) | Üçü de *"arranged to change regime"* |
| Adım 9 *"Section 8"* / öteki adımlar *"Sections 7 and 8"* | Grok (B), DeepSeek (2.3) | Doğru — geçen tur açık bıraktığım uç | Adım 9 eşitlendi |
| Adım 14 *"52 to 58 kg"* | Grok (D) | Doğru | *"52.3 to 57.5 kg"* |
| **Adım 8 aynı paragrafta kendisiyle çelişiyor**: ana cümle *"fail the second row"*, parantez *"not the second row"* | DeepSeek (2.1) | Doğru. **Ve denetimde ikinci bir çelişki çıktı:** parantezin *"the tip pairs do not lift"* ifadesi Adım 5 ile çelişiyor — kalkış payını uç çiftleri veriyor. Ayrıca *"meet none of the first three"* yanlıştı: tek yönelimde duruyorlar | Birinci başarısızlık kipi; *"sized for moments; they add the take-off margin (Section 5), but were not sized for weight support"* |
| Bill 3 oranı: Adım 11 2,4–3,2, Adım 12 4,19 | DeepSeek (2.2, 2.4) | Doğru — iki farklı uçak, aynı *"light design"* etiketi. 4,19 = 10,9/2,6 (50 kg referans); Adım 12 kendi *"Section 10'un değiştirmediği nicelikler"* kuralına rağmen motor derecesini kullanıyordu | Adım 12 *light/heavy design*'ı referans çifti olarak tanımlıyor; 4,19'un yanında Adım 11'in 2,4–3,2'si ve farkın nedeni |
| kW/kg iki farklı paydayla | Qwen | Doğru (0,168/0,036 = 4,67) | *"of take-off mass"* / *"of buffer"* |
| Adım 12 rotor terimi 0,0154, Adım 11 tablosunda 0,0169 | Qwen | Adım 11'in notu açıklıyor ama Adım 12 tek başına okunmuyordu | *"before the ten percent margin of the adverse end"* |
| Adım 3 *"zero of the three"* alıntılanırsa | Grok (E) | **Alınmadı** — aynı paragrafın bir sonraki cümlesi *"It does not mean an architecture that costs nothing"* | — |
| Adım 11 Fatura 2 başlığı ile tablo (göbek dahil) | DeepSeek | **Alınmadı** — tablo C_D0'ın tamamını bölüyor, kalın satırlar Fatura 2; %69/57 göbeği içermiyor | — |
| Adım 1 *"cover distance"* | DeepSeek (kendisi ihlal değil diyor) | **Alınmadı** — görevin ihtiyacı, karşılaştırma değil | — |
| Tekrar listeleri (tepki torku 7 adımda, kısmi gerçekleşme, geçiş gösterilmedi …) | Grok, DeepSeek, Qwen | Kayıt — kısaltma ertelendi (E1) | `v8-proportion.md` §5'e eklendi |
| İzleme listesi: Adım 10 nokta-kütle *"zero altitude loss"*, Adım 6 L/D_e tablosu, Adım 13 yüzdeleri | Grok | Hepsi zaten bağlamlı | — |

**Ders (§3.1 bir kez daha):** geometri aralığı elle yazılmıştı ve 50 kg tasarımdan kalan alt uç hiçbir
denetimden geçmiyordu. Grok yalnız iki bölümün birbirine iki uçak gibi okunabileceğini söyledi; sayıyı
yeniden hesaplayınca alt ucun kapanışa hiç ait olmadığı çıktı.

**Tur 59, metin hazırlanırken — düzeltmenin yan hasarı (§0.2):** Adım 12'ye eklediğim parantez *"the
engine rating is a quantity Section 10 did replace"* diyordu; aynı bölümün kuralı *"The quantities used are
ones Section 10 did not replace"*. Metni kurmadan önce düzeltilen pasajları yeniden okurken bulundu. Kural
*"with one exception"* oldu ve istisna adıyla yazıldı.

---

# Tur 60 — Tur 59 metnine (external-review-63) yanıtlar: Grok, ChatGPT, DeepSeek

**Üçü de:** Tur 59 düzeltmeleri kaynaklarına sadık; geometri, 4,19 / 2,4–3,2 ayrımı, *"arranged to"* doğru.
**ChatGPT bu tur tam yanıt verdi** (geçen turun altı sorusu dahil). Yeni matematiksel çelişki yok.

| Ne | Kim | Denetim | Yapılan |
|---|---|---|---|
| **Adım 3 ile Adım 8 çelişiyor**: Adım 3 *"attitude hardware does not violate it"*, Adım 8 uç çiftleri birinci başarısızlık kipine düşüyor | DeepSeek | Doğru — ve Adım 7 ile 8 de uç çiftlerini başarısız parça sayıyor; aykırı olan Adım 3 | Adım 3: taşıyan propulsor'ün koşulu karşılamasını engellemez, ama birinci kipe düşer; mimari kısmi |
| **Uç donanımı ölçeklenmiyor** — Adım 10 alanı/açıklığı büyütüyor, uç diskleri ve çerçeveler sabit | Grok | Doğru, **ve bir katman daha derinde:** çerçeve+rotor terimleri S_ref = 1,979 m² üzerinde katsayı; kapanışlarda sabit tutulmaları donanımı kanatla büyütmek demek. Referans boyutta kalsa %4–13 küçülürlerdi (0,0009–0,0028). İşaret kapanışın lehine; kapanış almıyor | Adım 10: üç ölçeklenmeyen şey + bir paragraf; `closure.py` basıyor, `verify.py` iki kontrol (54) |
| *"light design"* adımdan adıma farklı uçak | ChatGPT, DeepSeek | Doğru: Adım 8/10'da 50 kg referans, bir yerde kapanışlar, Adım 12'de yerel tanım | Adım 8 *"the 50 kg reference design"*'ı tanımlıyor; 5, 10, 11, 13, 14 buna bağlandı; çıplak *light/heavy design* yalnız Adım 12'de, yerel tanımıyla |
| Adım 13 tilt paragrafı sıralama dili taşıyor (*"leads under every contract"*) | ChatGPT | Mantıken savunulur, ama §0'ın dördüncü ekseni bakımından en açık artık risk | *"What the bound gives is a size, not an order"*: pay, gerçek tilt'in seyir cezalarının doldurması gereken alan; doldurma hesaplanmadı |
| Adım 15 *"moments rather than thrust"* — askıda itki üretiyorlar | Grok | Doğru; **Adım 9'da da aynısı** | ikisi de *"cruise thrust"* |
| Adım 8 parantezi ikinci satırı dar tarif ediyor; ve *ne olmadıklarını* anlatıyor | DeepSeek, Grok | Doğru | Parantez yalnız ne olduklarını söylüyor |
| Adım 14 tablo birimi | Grok | Doğru | *"per kilogram of buffer"* |
| Adım 6 *"52 and 58"* | DeepSeek | Doğru | 52,3–57,5 |
| Adım 12: *"1 % saf ölçek sonucu, ayrışma argümanı ona dayansın"* | DeepSeek | **Alınmadı** — Adım 12'nin kendisi %1'in *"a property of the constant-disc-loading rule, not a finding about Bill 3"* olduğunu söylüyor; öneri bununla çelişirdi | — |
| Adım 7'ye ileri atıf (hangi kip Adım 8'de) | DeepSeek | **Alınmadı** — Adım 7'nin gerekçesi (açıkta, yatırılamıyor) Adım 8 ile tutarlı; kısaltma öncesi ekleme yapılmıyor | — |
| Adım 12 Bill 3 paragrafı kapanış sonucu olarak alıntılanamaz | Grok | Metin zaten *"This paragraph compares the reference pair only"* diyor | — |
| Tekrar kayıtları | üçü | Kayıt | `v8-proportion.md` |

---

# Tur 61 — Tur 60 metnine (kısaltma hazırlığı) yanıtlar; yazarın yöntem ve ruh kararı

**Yazar, Tur 61:** tur metinleri yalnız değişiklikleri taşır; kısaltma doğrudan yapılmaz; herkesin önerisi herkese
yan yana sunulur; önce hemfikir olunanlar; ve *"bu makalenin ruhu"* yazarın sunduğu üstünlüktür — *"'yet another'
hesap kitap işi"* değil; *"Hesap kısmını neden yaptık? Q1 için."* → CLAUDE.md §0.8, §2.3.

**Cevap verenler:** Grok ve DeepSeek tam; **ChatGPT ve Qwen yalnız dosyaları aldıklarını söyledi**, görev beklediler.
Tur 61 metni en başta *"This is a task. Please answer it now"* diyor.

**Denetim:** iki okuyucunun 102 çekince alıntısının hepsi metinde, adıyla verilen adımda (üçü hafif yeniden ifade →
birebir hâline getirildi; ikisi ortak → 100 satır). `paper/v8-caveats.md` + `paper/build/v8_caveats.py` (`--sina`).

**Benim hatam, bu turda bulundu:** yazarın akış öğesi *"ortaya çıkan ürünün sorunsuzluğu"*nu Tur 57'den beri
*"why the result holds"* diye çevirmişim. DeepSeek bu başlığın altına ölçek ve sözleşme bulgularını koydu. Doğrusu
*"the soundness of the resulting product"*. Başlangıç metni düzeltildi; Tur 61'de açıkça yazıldı.

**Benim uzlaşı özetimde bir hata daha, göndermeden önce bulundu:** tablolarda yedi uzlaşı yazmıştım; Grok sekize inmek
için Adım 9'un dört eksen tablosunu düşürüyor. Uzlaşı altı.

Uzlaşı ve ayrışmalar: `paper/v8-shortening-consensus.md` (A1–A9, B1–B8, C1–C3).

---

# Tur 62 — Tur 61 metnine dört cevap; ilk kısaltma kümesi (dört okuyucu + Claude hemfikir)

**Yazar:** *"Her metinde elbette kendi görüşlerin de olsun … Sen de dahil herkesin hemfikir olduğu kısaltmalar uygulansın."*
→ CLAUDE.md §2.3 eki. Yazar cevapları okumuyor, bana yapıştırıyor.

**Dördü de tam cevap verdi** (ChatGPT ve Qwen bu kez görevi yaptı). Oylar: `v8-shortening-consensus.md`, Tur 61 bölümü.

**Uygulanan (beşimiz hemfikir):** Adım 15 kısa kapanış (1 023 → 337); Adım 10 yayılım tablosu → cümle; Adım 13 duyarlılık
tablosu → Ek S13; Adım 14 bilinmeyenler tablosu → Ek S14 (gövdede liste); Adım 11 kapanışı açılışı tekrar etmiyor; Adım 9
bağımlılık tablosu → düzyazı; Adım 1 ret cümlesi katkıdan önce. **30 096 → 28 515 kelime, 16 → 12 tablo.**

**Uygularken bulunan (§0.2):** Adım 13'te *"the table above shows the size of it"* taşınan duyarlılık tablosunun bir
satırına işaret ediyordu — gövdede sarkık kalacaktı. Rakam gövdeye yazıldı (+55…+84 → +33…+45 %).

**Çekince listesi:** 35 ekleme (hepsi doğrulandı), Adım 8 cümlesi tamlandı, 5 ruh cümlesi (benim önerim) → 140 satır.
Çıkarma önerileri (Grok 3, Qwen 2) uygulanmadı — DeepSeek karşı.

---

# Tur 63 — Tur 62 metnine dört cevap; "sonuç teyit edilmeden kapanmaz" kuralı

**Yazar:** uygulanan eylemin **sonucu** gösterilmeli ve teyit edilmeli; yanlış anlama olabilir (CLAUDE.md §2.3).

**Grok, uygulanan bir kısaltmada gerçek kayıp buldu:** Adım 14'ün listesinde kapalı döngü askı kontrolü maddesinden *"the
allocation of the tip pairs between take-off margin and attitude authority, which compete for the same propellers"* düşmüştü —
Adım 5 ve 7'nin tartıştığı "ikinci iş". **Benim hatam**: tabloyu listeye çevirirken bir hücrenin üç parçasından birini
atladım. Geri kondu.

**Qwen:** Adım 11 kapanışından çıkan cümle çekince listesinde değildi; özü açılışta (*"No new physical cost term is introduced
here."*) → listeye eklendi.

**Uygulandı (beşimiz):** N2 (Adım 4 tablosu düzyazıya) ve N4 (ağırlık dökümü + quadrotor karşıtlığı Ek S4'e; gövdede
sonuç ve *"categories do not account for the whole difference"*). Tablo gidince iki *"the row"* işaretçisi *"the entry"* oldu.

**Denetim düzeltmesi:** `v8_caveats.py` alıntı bloklarındaki satır başı `>` işaretini görmüyordu; Adım 3'ün koşul cümlesi
yanlışlıkla eksik görünüyordu. Düzeltildi.

**Tuhaflık:** DeepSeek'in cevabı Q4'te *"I am not DeepSeek"* diyor ve kendi eski görüşünü üçüncü şahısla anıyor. Oyu B2'de
tek bölüme döndü. Kayda geçti; yazara söylenecek.

---

# Tur 64 — Tur 63 metnine dört cevap; ikinci teyit turu

**Teyit:** Adım 14 onarımı, Adım 11 (Qwen'in şartı), N2, ağırlık dökümü taşıması, işaretçi düzeltmeleri → dördü de ✓,
**kapandı**. Quadrotor karşıtlığı: Qwen'in şartı (*"the isolation test above is what carries the prediction"* özü) →
geri kondu, yeniden teyide.

**Karara bağlananlar (beşimiz):** B1 (Grok'un dilimi), B6 (olgu 6'da; sayı ve ret 11'de), B7 (Adım 2 aktarım + Adım 9 dört
eksen tabloları gövdede; Adım 11 dökümü **her rakamıyla** düzyazıya — Grok ve Qwen'in şartı; ChatGPT itirazını geri çekti),
*"removes the need for the mechanism"*, N1, N3 (Qwen'in *"the only one of those documented obstacles"* düzeltmesiyle).

**Uygulandı:** hepsi; önce/sonra Tur 64 metninde.

**Uygularken bulunan eski hata:** Adım 3 *"The second row of the inverted table — same hardware, different orientation"*
diyordu; farklı yönelim üçüncü satırdı (*"tek görev"* satırı sonradan araya girmiş, atıf bayat kalmış). Düzeltildi.

**DeepSeek'in N1 uyarısı yanlış atıf:** *"gyroscopic coupling"* Adım 3'te değil Adım 2'deydi (Grok doğru söyledi).
DeepSeek bu tur kendi adıyla cevap verdi ve geçen turki karışıklığı düzeltti.

**Yazarın sorusu — ruh yerinde mi:** ölçüm — katkı %5,8'de adlandırılıyor; ama ağırlık hâlâ hesaplarda (10–14 %42, 7–8 %13)
ve **cümlelerin %45'i olumsuz** kurulmuş; birleştirme adımında (7) %50, Adım 9'da %61, kapanışta %72. Okuyuculara soruldu.

---

# Tur 65 — Tur 64 metnine dört cevap; cfd/ düzeni

**Düzen (yazar):** `cfd/` kökünde yalnız güncel tur metni ve başlangıç metni; eski turlar `cfd/arsiv-dis-gorus/`; kaynak PDF'ler
`references/`. Toplu yol güncellemesi `cfd/README.md` atıflarını da yanlışlıkla `references/`'e çevirmişti (`references/README.md`
listede olduğu için) — aynı commit'te geri alındı. İki PDF'in aynı NASA belgesi (TM-81280) olduğu not edildi.

**Teyit:** Tur 64'ün beş sonucu dördünce teyit edildi → kapandı. **Dört okuyucu da cevaba adıyla başladı.**

**Uygulandı (beşimiz):** Adım 2'den *"mechanical complexity"* çıktı.

**Ruh:** dördü de ölçüme katıldı. ChatGPT: *"ruh kaybolmamış; retorik ağırlık merkezi henüz ruhun olduğu yere taşınmamış"*;
kelime payı argüman ağırlığı değildir. Ses geçişi kuralı (A–D) ChatGPT'nin.

**Taslak olarak sunuldu (uygulanmadı):** B4 tek ev — Adım 5 işaretçi, Adım 7 tek cümle, Adım 9 yalnız sınır; Adım 7 ses önerileri
V1–V6 (V3 ve V5'e karşıyım, gerekçeli); dokuzuncu tablo için melez öneri (tablo S11'e, Adım 11'de bir sınır cümlesi, borçlar
Adım 14'te — birleştirmede yalnız rotor–yapı ve rotor–kanat girişimi eksik çıktı).

---

# Tur 66 — Tur 65 metnine dört cevap

**Kapandı:** Adım 2 (*"mechanical complexity"*) — dördü de teyit etti.

**Uygulandı (dört okuyucu + Claude):** B4 — Adım 5 işaretçi, Adım 7 tek cümle, Adım 9 yalnız sınır (Qwen: *"one price"* → *"a price"*);
Adım 7 ses geçişi V1, V2, V6; dokuzuncu tablo melez çözümle Ek S11'e (Grok: *"None of these is a ledger entry"*; Qwen ve ChatGPT:
*"the allocation of the take-off margin against attitude authority"*); Adım 14'e rotor–yapı/kanat girişimi eklendi.

**Uygulanmadı:** V3 ve V5 (herkes korudu); **V4 — Grok'un itirazıyla görüşümü değiştirdim**: *"the condition is met by the set"*
uçağın koşulu karşıladığını ima ediyor; uç çiftleri karşılamıyor. ChatGPT'nin *"set by rotor inertia"* uyarısı: ifade özgün metinde
de böyle, değişmedi — not edildi. Grok V2 için *"pays in efficiency in at least one of them"* ifadesini tercih ediyor — soruldu.

**B5 ölçümü:** *"geçiş gösterilmedi"* Adım 7'de tam; Adım 8 ve 9 gerekçeyi tekrar ediyor → taslak (uygulanmadı).

---

# Tur 67 — Tur 66 metnine dört cevap

**Kapandı (dördü de teyit):** 2.1–2.8 — B4 (Adım 5, 7, 9), V1, V6, dokuzuncu tablo (Ek S11), Adım 14'e girişim.
**Uygulandı (beşimiz):** V2 Grok'un ifadesiyle (*"pays in efficiency in at least one of them"*; dördü de tercih etti); B5 — Adım 8
işaretçi, Adım 9'dan *"Section 7 should be read under that limit"* çıktı.
**Yazar:** okuyucuların kendi önerileri de istensin → CLAUDE.md §2.3.
**Hız ölçümü:** Tur 60 30 096 → Tur 67 27 689. İlk kısaltma turu (62) −1 581; sonraki beş tur (63–67) ortalama **~165**
(−186, −315, −2, −237, −86). 7 500'e: altı turun ortalamasıyla (~400) **~50 tur**, son beşin hızıyla **>100 tur**. *(Yazara
önce yalnız ~50 dedim; son turların hızı daha düşük — düzeltildi.)*

**Claude'un ilk önerisi — yazar reddetti, geri çekildi:** bölüm bölüm kelime bütçesi (hesaplar 10 120 → 1 600, birleştirme
~2 900 → 1 300 …) ve ilk iş birleştirme bölümünün sıkıştırılmış taslağı. Yazar: *"Ama çözüm senin sunduğun gibi budamak olamaz.
Ne kadar tur gerektiğini onlara da söyle böyle giderse. Onların çözüm önerileri neyse onu da dinleyelim. Ama ben en az 6-8 tur
daha makul adımları tercih ediyorum. Belki onlardan güzel fikirler gelir bu arada. Olmazsa da artık, getirmiş olduğum eşsiz
yenilik anlatılarının dışında kalan hesap kısımları yontmada yeteneğinizi gösterirsiniz :D … Bu şekilde sunamam."* **Hatam:**
bütçe kelime sayısını sürücü yaptı, yenilik anlatılarına da hesaplara uygulandığı gibi uygulandı ve işe kalpten başladı (§0.8
ile ters); üstelik okuyucu önerilerinin yerine benim taslaklarımı koyuyordu (§2.3 ile ters).

**Yerine (Tur 67 metni §3):** ölçüm (~50 / >100 tur), yazarın sözleri birebir çeviriyle, geri çekilen önerinin bir cümlelik
kaydı, okuyuculardan hız için **kendi çözümleri**. Benim görüşüm (eleştiriye): **tutma listesi** — bir adım için her birimiz
gövdede kalması gerekeni yazar (bulgusu, sınırı, makalenin başka yerde andığı her sayı); herhangi birinin listesindeki kalır;
gerisi eke **aynen** gider; önce/sonra gösterilir, teyit edilir. Güvenlik aynı (tek itiraz cümleyi tutar), birim büyür. Önce
hesap kısımlarında. Zayıf yanı: taşır ama yeniden yazmaz; eklem onarımları ayrıca gösterilmeli. Kayıt: `deferred-decisions.md` E4.

---

# Tur 68 — Tur 67 metnine dört cevap; hız için çözümler

**Kapandı (dördü de teyit):** V2 (Grok'un ifadesi) ve B5 (Adım 8, 9). Grok: geliş açısı bandı Adım 8'e geri dönmesin.

**Hız çözümleri:**
- **Grok:** tutma listesine karşı (*"The unit grew; the veto did not"*). Önce yapıyı birleştir (başlık ve dosya birleşimi,
  ifade değişmeden); sonra her tur bir hesap adımının sıkıştırılmış taslağı, sıra 12, 13, 11, 10 (10 en çok atıf alan, en
  sona); taslak her korunan cümleyi ve başka adımın andığı her sayıyı tutar; veto: düşen sayı ya da güçlenen yüklem → kaynak
  cümle aynen döner. 7–8 bu blokta açılmaz. Bütçe yok.
- **ChatGPT:** tutma listesine karşı (*"a union of five people's anxieties"*); yerine **işlev** korunur, en kısa sadık ifade
  gövdede kalır. Bağımlılık haritası, üç katman (gövde / ek / silinebilir), önce yapıyı birleştir, 10–14 sırayla, sonra
  eklemler, en sonda ses geçişi. 7 500 ara ölçüt değil.
- **DeepSeek:** tutma listesini destekledi, zorunlu taban (korunan listeler) ve sabit sıra (10–14, **sonra 5–8**) ile; üç
  başarısızlık noktası: toplu atlama, gövdenin iddiaya dönmesi, eklemlerin pahalı olması.
- **Qwen:** tutma listesine karşı (*"a skeleton, not a paper"*); bölüm taslağı, korunan listelere karşı yazılır, tek veto
  taslağı düşürür — **ama hedef kelime sayısıyla** (10–13 için ~3 000): yazarın reddettiği bütçe.

**Benim görüşüm değişti:** tutma listesini geri çektim (üç okuyucunun gerekçesi doğru). Yerine dördünden birer parça alan
plan (Tur 68 metni §6): yapı **üretilmiş görünüm** olarak birleşir (kaynak adım dosyaları; denetimler değişmez); her hesap
adımından önce bağımlılık haritası; taslağı ben yazarım, okuyucu tarifinden; **taslak yeni yüklem eklemez** (her cümle kaynak
cümle, yalnız silmeyle kısalmış kaynak cümle ya da olgu söylemeyen bağlantı); Grok'un vetosu; sıra 12, 13, 11, 10; 5–8
bu blokta açılmaz, sonrası yazarın kararı; bütçe yok; şekil tabloyu değiştirir, çoğaltmaz.

**Denetimde bulunanlar (okuyuculara düzeltme olarak):** korunan liste **150** (140 + 10) — Grok ve DeepSeek 145, Qwen 135
dedi; Adım 12 **2 974** kelime ve Tur 60'tan beri **aynı** (Qwen ~2 500); ChatGPT tutma listesini yazara maletti; Grok'un
*"the loop closes; the package is not shown to exist"* alıntısı metinde yok (Adım 10: *"It does not establish that the
package exists"*; 14/15: *"The loop closes; the aircraft is not shown to"*); Grok P5 yazara *"until the calculations have
been cut"* dedirtti — yazarın sözü sıra koymuyor; Qwen P4'ün tanım tekrarı: tanımın tek evi Tur 60'tan beri Adım 8.

**Yeni bulgu — v7 şekilleri olduğu gibi kullanılamaz.** v7'nin 12 şekli `figures/output/`'ta; v8'de şekil yok. **Şekil 11**
(beş evre) v8'in geri aldığı üç ifade taşıyor: alt başlık *"nothing on the aircraft rotates relative to it"* (şerit
hareketli — Adım 7: *"the only moving aerodynamic surface"*; §0.1'in aşırı iddiası); geçiş paneli *"no altitude loss"*
(Adım 10: nokta kütle modelinin özelliği; sonlu momentli model 5,4 m kaybediyor); iniş paneli *"reverse of transition"*
(Adım 5: *"not symmetric … no figure in this paper describes the landing transition"* — korunan cümleyle çelişir). Kaynak:
`figures/build/mkfig11.py` satır 25, 27, 52. Ayrıca v7 gövdesi (satır 2121–2122) *"Nothing on the aircraft rotates
relative to the aircraft at any point in it"* diyor. v7'ye dokunulmaz (K6); kural önerisi: v7 şekli v8'e ancak etiketleri
metin gibi denetlendikten sonra girer.

**Adım 12'nin düşük Re sınırı korunmuyor:** *"Of the two rotor terms, the light one is therefore the less certain — and it
is the one Sections 10 and 11 carry"* listede değil (Grok P3 bunu tutmak istiyor) → eklenmesi önerildi (oylamaya).

**Yazarın kararı (Tur 68, gönderilmeden önce):** plan **(b)** — oylamaya gönderilmeden onaylandı: *"b şıkkı."* Ayrıca yazar:
*"Grok dil modeli olarak kısa anlatımlı metinlerle … daha çok geliştirildi. Dolayısıyla Grok'un kısaltma konusunda önerileri
bazen daha isabetli de olabilir."* → Adım 12 taslağında Grok P3'ün tarifi esas alındı; okuyucu metnine bu not **yazılmadı**
(öteki okuyucuları Grok'a yaslanmaya itmesin diye; eşik ve veto aynen).

**İlk iki ürün (uygulanmadı, gösterildi):**
- `paper/v8/ASSEMBLED.md` (`paper/build/v8_assemble.py`): dokuz bölüm, adım 8 B1'e göre bölündü, atıflar yeniden
  numaralandı; 150 korunan cümle görünümde (yeni numaralarla); `--sina` silineni yakalıyor; 12 eklem listelendi
  (7 × *"Sections 7 and 8"* → *"Section 5"*, ikisi fiil uyumunu bozuyor; 5 kendi bölümüne atıf).
- `paper/v8/drafts/12-draft.md` (`paper/build/v8_draft_check.py`): 2 973 → 2 151 kelime; 27 cümle çıktı (Ek S12'ye aynen),
  13 kısaldı, 76 aynen. **Yalnız silme** kuralı mekanik denetleniyor. **Öğrenilen:** silme de anlamı ters çevirebilir
  (*"Coupling is not identity"* → *"is identity"*) — denetim silinen olumsuzluk/niteleyiciyi reddediyor; `--sina` ile
  sınandı; kendi taslağımda iki silmeyi yakaladı (*"without settling…"*, *"less"* içeren tanım) → geri kondu.

---

# Tur 69 — Tur 68 metnine dört cevap

**Kararlar (dördü + Claude):** Adım 12 taslağına **veto yok** → uygulandı (2 973 → 2 152), kaybı olan her paragraf Ek S12'de
aynen; düşük Re sınır cümlesi korunan listede (151); Adım 8 bölünmesi kabul; 10+11 birleşimi yok; tanım tablosu yok; ruh
cümlesi konumu yalnız son ses geçişinde sınama; şekil tabloyu değiştirir; v7 şekil kuralı kabul.

**Eklemler:** DeepSeek ve Grok'un önerisiyle görünümde Adım 7 → 5.1, Adım 8 → 5.2; on iki eklemin hepsi çözüldü (fiil
uyumu, kendine atıf). Qwen'in regex önerisi gereksizleşti.

**Açık:** *"These are the parts that fail the escape condition"* (korunan) — DeepSeek: *"The tip pairs are the parts…"*;
Grok: *"Of the hardware just listed, these are…"*; ChatGPT, Qwen: olduğu gibi. Claude: DeepSeek'inki.

**Adım 12 ikinci geçiş (taslak, uygulanmadı):** okuyucu yeniden yazımları — R1 Grok (+ Claude: *sized by one method*, kapsam
cümlesi, ölçülmemiş üstel), R2 DeepSeek, R3 DeepSeek (+ *in the free-wheeling state*), R4 Grok, R5 Grok, D1 ve D2 ChatGPT →
2 152 → 1 873. Alınmayanlar ve gerekçeleri: ChatGPT'nin kendi çekince koyduğu mekanizma cümlesi (daha güçlü); üç "genel
değil" cümlesinin birleşmesi (üç ayrı şeyi koruyor); Qwen'in Bill 1 yeniden yazımı (*"by definition"* daha güçlü; Adım 14'ün
dayandığı bağlaşım cümlelerini düşürüyor); Qwen'in *"Why this section sits"* yeniden yazımı (kapsam cümlesini düşürüyor).

**Adım 13 ilk taslak (yalnız silme):** 2 398 → 2 117 (−%12); 14 korunan cümle; tek yargı: Adım 9'un dördüncü satırına
uygulanan kural cümlesi çıktı (retin evi Adım 9 ve 15). Ek S13'e aynen gidecek.

**Yazar notu uygulanışı:** Grok notu okuyucu metnine yine yazılmadı; seçimlerin gerekçesi tabloda.

---

# Tur 70 — Tur 69 metnine dört cevap

**Teyit (dördü):** Adım 12 birinci geçiş + S12; on iki eklem → **kapandı**. Şekil kararları (şekil–iddia denetimi, hedef
taraftan atıf denetimi, Şekil 11'in Grok P8'e göre yeniden kurulması, DeepSeek şekilleri yalnız yerine geçerek, Adım 11
sınır cümlesi bölünmesi) → **kapandı**.

**Uygulandı (dördü + Claude):** Adım 8 korunan cümle → *"The tip pairs are the parts that fail the escape condition"*
(Qwen oyunu değiştirdi; Grok kendi önerisini geri çekti). Adım 12 ikinci geçiş R1–R5, D1, D2 + Grok'un iki geri koyması
(2 152 → 1 885). Adım 13 birinci geçiş, **Grok'un 13.2 vetosuyla** (520 kg cümlesi kaldı) ve 13.3 ile *"The contract is
chosen by the mission…"* geri kalarak (2 398 → 2 200).

**Hatalarım:** (1) Adım 12 kaydına *"değişen paragrafların özgün hâli zaten S12'de"* yazdım — *"Two conditions travel…"*
yoktu; yeni `v8_nothing_lost.py` ilk koşuda yakaladı, eklendi. (2) Birleştirici eski Adım 8 cümlesine bağlıydı; zincirde
hata görülmeden commit edildi, bir commit bayat görünüm taşıdı; bir sonraki commit'te düzeldi.

**Taslak (uygulanmadı):** Adım 13 ikinci geçiş (Qwen RW-13A–D, ChatGPT'nin tek cümlesi + iki cümle; 2 200 → 2 116);
DeepSeek ve Grok'un 13.2/13.3 yeniden yazımları korunan cümle düşürdüğü için alınmadı. Adım 11 birinci taslak (yalnız
silme, 2 144 → 2 002).

**Gövde:** 26 389 (Tur 67: 27 689).

---

# Tur 71 — Tur 70 metnine dört cevap

**Teyit (dördü):** 2.1–2.4 → kapandı. **Karar (beşimiz):** D/R etiketi; ek bölümlerinde kaynak adım + tur; şekillerde dönüş
süresi/irtifa kaybına Adım 10 atfı; kaçış koşulu şekli sonraya, yazarın kararı.

**Uygulandı:** Adım 13 ikinci geçiş S2–S5; **S1'e DeepSeek vetosu** → sözleşme tanımı aynen geri (2 200 → 2 147). Adım 11
birinci geçiş 11.1, 11.3, 11.4; **11.2'ye veto** (DeepSeek, ChatGPT) → kaynak kaldı (2 144 → 2 044). S11 ve S13'e kaybı olan
paragraflar tam; `v8_nothing_lost.py` 11–13'ü kapsıyor, tabloyu satır satır okuyor.

**Taslak:** Adım 11 ikinci geçiş (a, b, c silme; d yeniden yazım) 2 044 → 1 957. Qwen RW-11A alınmadı (korunan cümleyi düşürüyor).
**Adım 10 bağımlılık haritası** (Qwen P1, Grok P10) — taslak gelecek tur.

**Qwen P3 — hesap:** hesap adımları 8 679, geri kalan 17 571 (çerçeve 5 723, yenilik anlatıları 5–8 6 931). **Hesaplar sıfıra
inse bile gövde hedefin iki katından fazla.** Yazara soruldu.

---

# Tur 72 — Tur 71 metnine dört cevap; yazarın kararı

**Yazar:** *"Gerçekçi olmak durumundayız. … Kısaltacaksak heryerden kısalacak. Tamam, o şekilde ilerleyelim lütfen."*

**Teyit (dördü):** 2.1–2.3 → kapandı. **Uygulandı (dördü + Claude):** Adım 11 ikinci geçiş (a)–(d), 2 044 → 1 957; S11'e 4
paragraf. **Karar:** ilk geçiş sınaması kalıcı; olumsuz cümle sayımı yalnız tanı; harita taslaktan bir tur önce; "Section 10"
cümlelerinin nesnesi denetlenir.

**ChatGPT'nin model kilidi gerçek bir durum buldu:** Adım 11 *"The transition altitude result (5.4 m) is a result, not a
charge"* modelini yitirmiş (S11 tablosunda vardı) → nitelemenin geri konması oylamada.

**Adım 10:** okuyucu harita eklerinin çoğu Adım 10'da ve taslak koruyor; Grok/DeepSeek'in bazıları (tampon %3,6, yakıt kesri
%16, disk yükü 44, motor seyirle, kalkış payı, 50 kg'daki palet seçimi) Adım 10'da **yok** — evleri 5, 7, 11–14. Taslak
(yalnız silme) 2 601 → 2 403; `verify.py`'nin ayrıştırdığı iki cümle dokunulmadı; hüküm cümlesinin korunması önerildi.

**Yöntem sorusu:** yalnız silme adım başına %7–12 → gövde ~24 000'de biter; korunan cümle tabanı ~2 200 kelime. Önerim:
bölüm bölüm yeniden kurma (R, cümle cümle veto), önce Adım 4'te deneme, veto edilen hataları say.

---

# Tur 73 — Tur 72 metnine dört cevap; yöntem önerileri yazara

**Teyit (dördü):** Adım 11 ikinci geçiş → kapandı. **Uygulandı (dördü + Claude):** Adım 11'de 5,4 m cümlesine model ve
geometri; Adım 10 hüküm cümlesi korunan listede (152); Adım 10'dan 10.2 ve 10.4 (2 601 → ~2 520). **Veto:** 10.1 ve 10.5
(ChatGPT), 10.3 (ChatGPT, Grok) → kaynak kaldı. S10 açıldı.

**Yöntem (yazar: "önerileri ve kendi önerini yaz, ona göre karar vereyim"):**
- Dördü de Adım 4'te yeniden kurma denemesine evet.
- ChatGPT: "anlam envanteri" (söylenmesi / gösterilmesi / nitelenmesi / söylenmemesi gereken); her cümleye P/D/J/R etiketi;
  beş geçme koşulu; hedef %50–70.
- Grok: yalnız deneme, yaygınlaştırma kararı sonuca bağlı; durma ölçütü (güçlenen yüklem ya da düşen NASA sayısı → dur;
  iki+ kırık öncül → yöntem hazır değil); birim "bir bulgu bloğu"; sıra 10 → 2–4 → 9, 14 → 1 → 5–6 → 7–8 en son.
- DeepSeek: cümle cümle iz tablosu (özgün, taslak, durum, varış, korunan kayıt); çok adımda geçen her sayıya eşitlik taraması.
- Qwen: "yeni olgu yok" sınıflaması (korunan / atıf alan sayı-tanım-çekince / olgu söylemeyen bağlantı); etiketsiz özet cümle
  en sıkı vetoya; 2–4 tek bölüm olarak yeniden kurulsun (B2).

---

# Tur 74 — Tur 73 metnine dört cevap; yöntem kabul, deneme başladı

**Teyit (dördü):** 1.1–1.3 → kapandı. **Yöntem:** dördü de değişikliklerle kabul etti; yazarın şartı sağlandı. Ayrışan yerlerde
**katı olan** alındı: bulgu bloğu = bulgu + asgari yerel kanıt + nitelik (ChatGPT); 2–4 blok blok (Grok); envanter tablo +
dış bağımlılıklar (Qwen) + herkes satır ekleyebilir (DeepSeek); J'nin tanımı ve fiil listesi (ChatGPT, Qwen); her R için yüklem
defteri (ChatGPT); iz tablosunda kanıt rolü ve sayı nesnesi (ChatGPT, Grok); S4 dondurulur; sıra envanter → iz → taslak.
**Durma:** güçlenen yüklem; gereken sayının düşmesi; modelini yitiren sayı; uydurulmuş nedensellik; yeri değişen ilk geçiş;
"sıkışmış ama inanılmaz"; ikinci kırık öncül. DeepSeek'in "düşen sayıda bir onarım turu" önerisi alınmadı (üç okuyucu daha katı)
— DeepSeek'e soruldu. Yüzde ölçüt değil.

**Adım 4 envanteri** (`paper/v8/drafts/04-inventory.md`), altı blok. **Kendi hatam, envanterde:** B1'in çıkarımsal kanıtına
*"so the aircraft cannot have shaped it"* yazmıştım — kaynağın değil benim çıkarımım, daha güçlü; kaynak cümleyle değiştirildi.

---

# Tur 75 — Tur 74 metnine dört cevap; Adım 4 denemesi

**Yöntem:** beşimiz kabul; DeepSeek onarım turu önerisini geri çekti. **Envanter:** altı blok dördünce teyit; eklenen satırlar
(Grok, ChatGPT, DeepSeek, Qwen) envanterde. Qwen'in iki eki gövdedeki mevcut cümlelerle zaten taşınıyor.

**Deneme ürünleri (uygulanmadı):** dondurulmuş kopya (`04-snapshot.md`), etiketli taslak (`04-pilot.py` → `04-draft.md`), iz
tablosu (`04-trace.md`, 51 kaynak cümle), yüklem defteri. **Sonuç: 1 586 → 1 323 (−%17)**; D 724, P 378, R 216 kelime (5 cümle);
5 kaynak cümle (geçiş/tekrar) çıktı. D/P cümlelerinin hepsi silmeyle türedi, olumsuzluk silinmedi; korunanlar tam.
**Bulgu:** envanter neredeyse her şeyi yerinde tutuyor; yeniden kurma Adım 4'ten %17 aldı, %50–70 değil. Kazanç tekrarı
bol bölümlerden gelecek. Metinde iki sayma hatamı (R cümle sayısı, cümle numarası) göndermeden düzelttim.

---

# Tur 76 — Tur 75 metnine dört cevap; Adım 4 denemesinin sonucu

**Kör okuma:** dördü de bulgu, kapsam ve sınırı doğru buldu. ChatGPT taslakta olmayan 716/146/10'u yazdı (envanterden
bulaşma). **R:** #2, #10, #15, #28 dördü de kabul; **#18'e ChatGPT vetosu** ("shows" → "is consistent with"; sayılar kalsın) →
kaynak cümle döndü; daraltılmış hâli oylamada. **DeepSeek:** B6'da nitelik düşmüştü (kaynak 44–45) → geri. **Durma koşulu
ateşlenmedi** (ChatGPT "güçlenen yüklem" dedi; ama "shows" kaynağın kendi sözü — envanter kaynaktaki sorunu ortaya çıkardı).

**Uygulandı:** Adım 4 = yeniden kurulmuş metin, 1 586 → 1 339 (−%16); özgün Adım 4 donmuş hâliyle S4'te; nothing-lost 4'ü kapsıyor.
**Sıradaki:** Adım 2–3 için tek envanter, blok blok taslak. Korunacak aday: araç sabit cümleleri (G, Q, D evet; C'ye soruldu).


# Tur 77 — Tur 76 metnine dört cevap; Adım 4 kapanışa, Adım 2–3 envanteri

**Yazar:** *"Süreci şimdi bırakmak çok saçma olur. Adımları, planladığımı şekilde işleyelim."* Hedef sorusu adımlar
bitince (E4).

**Oylar:** 2.1 ve 2.2 dördü de teyit. 3.1 (#18 daraltılmış, 580/679/99 gövdede) dördü de evet → uygulandı. 3.2 (iki
"araç sabit" cümlesi korunan) dördü de evet → uygulandı, korunan 154. **Grok P23:** 687 (tasarım brüt ağırlık farkı) ile
679 (boş ağırlık farkı) birleştirilmiş görünümde tek paragrafta, karışmıyor. Adım 4 1 356 kelime (−%15).

**Adım 2–3 envanteri** (`paper/v8/drafts/02-03-inventory.md`): 12 blok; Ev (Grok P22), yineleme durumu (ChatGPT;
DeepSeek "neyin yinelemesi"), 3B birincil hedef (Qwen P1), 3E ve 3C'nin dört parçası kilitli (Qwen P3 genişletildi —
Adım 7 dört parçayı kendi sözüyle sayıyor). Qwen'in "Adım 15 de atıf yapıyor" dediği yanlış (arandı). Yineleme kuralı:
Grok P22 varsayılan, ChatGPT'nin "gerekli yineleme"si ancak işini adlandırırsa.

**Envanterin kaynakta bulduğu üç sorun (uygulanmadı, okuyuculara):** **S-1** tablonun mekanizma satırları tek kurala
uymuyor — katlama ve hatve göbeği Fatura 1, eğme mekanizması "üçünün dışında". Görev döngüsü kuralında tuhaf satır eğme;
kaldırma alt sistemi kütlesi kuralında (makale bunu 3D'de ve Adım 11'de zaten uyguluyor) tuhaf satır hatve göbeği. Benim
görüşüm (c): hatve göbeği satırı düzelir, eğme satırı mekanizma kütlesinin Fatura 1'in görev döngüsü karakterini
taşıdığını açıkça söyler; Adım 4'e dokunmaz. **Kendi hatam:** ilk yazımda (a) dedim; Adım 4'ün eğme paragrafını
okuyunca (a)'nın kapanmakta olan Adım 4'ü üç yerde yeniden açtığını ve makalenin zaten ikinci kuralı kullandığını
gördüm. **S-2** 3F'de "the first" belirsiz. **S-3** Adım 12'nin "separability Section 2 asserts"ı Adım 2'den güçlü olabilir.

**Koruma önerisi (Claude):** *"Whether an architecture can decline the mismatch itself, rather than redistribute its
consequences, is a different question"* — hesap bölümünde kavrayışı taşıyan cümle.

# Tur 78 — Tur 77 metnine dört cevap; Adım 4 kapandı; S-1 derinleşti

**Oybirliği (4 + Claude):** Adım 4 teyit → **KAPANDI**. Yineleme kuralı; "stated before any configuration" evi 3A; P3 kilidi
3C'nin dört parçasına; S-2 "the first departure"; S-3 Adım 12 açılınca "distinctness"; **"decline" cümlesi korunan (155).**

**S-1:** Grok (c) ama "2A'dan çıkıyormuş gibi yapma", uygulama kısaltma içinde değil; DeepSeek ve Qwen (c); **ChatGPT HOLD**:
Adım 2 Fatura 1'i açıkça kaldırma alt sistemi kütlesi diye tanımlıyor mu? **Denetim:** tanımlamıyor (örnekle tanımlıyor; açık
ifade yalnız 3D ve Adım 11'de, ikisi de "Section 2 böyle tanımlar" diyor). **Daha derini:** metin iki sözlük kullanıyor —
**fatura** (belirli ödeme) ve **para birimi** (kg, sürükleme, kW; 2E'nin kendi tanımı). Tablonun sağ sütunu ikisini karıştırıyor:
hatve göbeği satırı birimi yazıyor, eğme satırı faturayı yazıp pivot kilogramlarını atlıyor (3B "adds mass"; S4 146 lb). Dolayısıyla
*"One row does not pay in any of the three currencies"* (a), (b), (c)'nin hepsinde yanlış. **Aday (d):** fatura ile birimi ayır
(2E'de üç değişiklik, önce/sonra Tur 78 metninde). **Taslak yok, (d) çözülene dek.**

**Kendi hatam (Tur 77):** (a) "Adım 4'ü üç yerde yeniden açar" dedim — yanlış; Adım 4 zaten mekanizmanın kütle ödediğini
söylüyor, çelişen şu anki eğme satırı. 146 lb kendi kurduğum S4'teydi. **Okuyucu hataları:** Grok "One row stays true" (değil);
Qwen'in hatve göbeği ayrımı satırın yazılışına uymuyor, S-3'te Adım 12'nin bulgusunu ters yazdı.

**S-5 (soru):** 2F'nin olumlu sınaması "no worse" diyor, açıklaması "leaves another standing is not a counter-example" — hangi
tabana göre söylenmiyor; Adım 4'ün tilt-wing verisi (146 / 716 lb) sınamayı koşulabilir kılıyor. Bulgu değil, soru.

# Tur 79 — Tur 78 metnine dört cevap; (d) içerikte oybirliği, sözcükte Grok'un iki şartı

**(d):** A, B, C içeriğini dördü de kabul. Grok: tanım 2A'nınki gibi okunmasın, kök faturalardan üstün sıralansın; B'deki
*"1 in kilograms"* reddi (tabloda 1 hep Fatura 1 demek). DeepSeek ve Grok başlığın değişmesini istedi. → **Hiçbir şey
uygulanmadı** (Tur 76 emsali); son paket A′, B′, C, C4, C5, H oylamada. ChatGPT'nin fatura/birim değişmezi tabloya
koşuldu: tilt satırının Fatura 3'ü dışında altı satır geçiyor.

**Adım 4, tek kelime:** Qwen "moves the charge" (d)'den sonra yanlış; Grok "gevşek, yanlış değil, bırak"; ChatGPT ve DeepSeek
"tutarlı". Benim görüşüm: Qwen'in teşhisi doğru → "moves the cost", kapanmış adımı tek kelimeyle açar, oybirliği gerek.

**S-5 keskinleşti (kendi eksiğim Tur 78'de):** Adım 4 eşleştirilmiş çiftin *"turbo-electric propulsion architecture"*ı
paylaştığını söylüyor. İkisi de sürekli gücü askıya göre boyutluyorsa (denetlemedim) "left standing" = "no worse" ve Adım 4'ün
kendi *"giving part of the structural saving back"* ifadesi 2F'nin karşı-örnek tanımının kilogramdaki biçimi. Satırı ayakta
tutan yalnız *"cost falls outside the three charges"* maddesi. Çürüme iddiası yok; iki şey denetlenmedi. **3B taslağı S-5
çözülene dek yok** (ChatGPT). Küçük düzeltmeler: Qwen buffer/tilt karıştırdı; "accounting claims transfer".
