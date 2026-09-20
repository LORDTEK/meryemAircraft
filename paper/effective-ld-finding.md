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
