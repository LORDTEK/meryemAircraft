# Kaynak defteri

**Doğrulama durumu:**
- `A` — **tam metin birinci elden okundu**
- `B` — özet/künye birinci elden okundu
- `C` — yalnızca arama motoru özeti; **doğrulanmadı**

> **2026-08-23 güncellemesi:** Dört kaynağın tam metni okundu (tasarımcı indirip
> yükledi). **İki sayı yanlış çıktı ve makaleden çıkarıldı.** Ayrıntı §0'da.

---

## 0. ⚠️ DÜZELTİLEN İKİ HATA

Aşağıdaki iki "bulgu" arama motoru özetlerinden gelmişti. Tam metin okununca
**ikisinin de kaynakta bulunmadığı** görüldü.

| Kullandığım ifade | Gerçek |
|---|---|
| "Hibrit kipte rotor-iz girişimi sürüklemeyi **%20–40** artırır" | ⛔ **Bu ifade K2'de YOK.** Ne metinde ne tablolarda böyle bir yüzde geçiyor. Kaynak, karşılaştırmayı **niteliksel** veriyor. Sayı muhtemelen bir yapay zekâ özet sitesinden türemiş |
| "Ölçülen en düşük parazit sürükleme katsayısı **C_D0 = 0,0397** (rotorlar ve kollar dâhil)" | ⛔ **0,0397 bir sürükleme katsayısı DEĞİL.** K2'nin Tablo 9'unda **$C_{M\alpha}$** — yunuslama momenti eğimi, üstelik **negatif** (−0,0397) |

**Ders:** arama motoru sentezleri sayı için kullanılamaz. Yazım kuralı 3 doğruydu.

---

## 1. Fatura 1 — kütle

### [K5] Silva ve ark. 2018 · **durum: A** · ⭐ **en güçlü kaynak**
**VTOL Urban Air Mobility Concept Vehicles for Technology Development**
NASA / AIAA 2018-3847 · DOI: 10.2514/6.2018-3847

NASA, aynı görev için dört mimariyi (Quadrotor, Side-by-Side, Lift+Cruise,
elektrikli/turboelektrik türevleri) NDARC ile boyutlandırıp karşılaştırıyor.
Görev: 6 yolcu, 1 200 lb faydalı yük.

**Doğrudan alıntı (s. 14):**
> *"The weight of the Lift+Cruise concepts is heavier in general than for the other
> vehicles. **This is not driven by the cruise power draw, as the L/De of the
> Lift+Cruise is indeed higher than the other vehicles.** Hover power is higher, but
> the most likely targets for reducing vehicle weight are **the extra empty weight
> items on board in hover (wing and propeller).**"*

**Doğrudan alıntı (s. 9):**
> *"In all cases, the battery-powered vehicles were the heaviest... The Side-by-Side
> concepts are lightest, followed by the Quadrotor, with the **Lift+Cruise being
> heaviest**."*

🎯 **Bu, Fatura 1'in bağımsız ve yetkili bir kaynakça, kendi kelimeleriyle
doğrulanmasıdır.** NASA diyor ki: lift+cruise en ağır olan; sebebi seyir gücü
**değil** (seyir verimi zaten daha iyi), sebebi **hover için taşınan boş ağırlık.**
Bölüm 3.2'nin tam olarak iddia ettiği şey budur.

**İkinci bulgu — N55'i destekliyor (s. 14):**
> *"Lowering disk loading could improve the hover performance, but the rotor diameter
> is at the constraint. **Adding more rotors may allow improvement in this regard**."*

NASA, disk alanını büyütmek için rotor **sayısını** artırmayı öneriyor — bizim
ölçek kaçışımızın (N55) aynısı.

⚠️ **Sınıf farkı:** Silva'nın aracı yolcu sınıfı (≈5 000 lb). Mimari bulgu
aktarılabilir, sayılar aktarılamaz.
⚠️ "Seyirde L/D ≈ 13,5" sayısı **doğrulanamadı** — Tablo 3'ün sütun hizası metin
çıkarımında bozuldu. **Kullanılmayacak.**

---

## 2. Fatura 2 — sürükleme

### [K1] Bacchini 2020 · durum: **A** ⭐ · **doktora tezi, açık erişim**
**Electric VTOL preliminary design and wind tunnel tests**
Doktora tezi, Politecnico di Torino, Havacılık Mühendisliği, 32. devre, Mart 2020.
Danışmanlar: Giulio Romeo, Enrico Cestino. **CC BY-NC-ND 4.0.**
`iris.polito.it` üzerinden serbest.

> ⚠️ **Dergi makalesi (AST 109:106429, 2021) hâlâ okunmadı.** Sayılar **tezden**
> alınmıştır ve **teze atıf yapılacaktır.** İkisi aynı çalışmadan doğuyor ama
> okumadığımız metne atıf yapmayız.

#### Deney

Tek gövde, dört yapılandırma, rüzgâr tüneli. Model: **Mini Talon** İHA
(+ Krossblade **SkyProwler** gövdesiyle ikinci model). 10–30 m/s.

| Model | Yapılandırma |
|---|---|
| Mini Talon 1 | temiz uçak (VTOL donanımı yok) |
| Mini Talon 2 | geri çekme sistemli — pervaneler açık / çekilmiş |
| Mini Talon 3 | **standart quadplane** — pervaneler dik / akışa paralel / pervanesiz / motorsuz |

#### 🎯 Bulgu 1 — L/D merdiveni (Mini Talon 3, azami L/D)

| Yapılandırma | Azami L/D |
|---|---:|
| Motorsuz (≈temiz uçak) | **≈17** |
| Motorlu, pervaneler **akışa paralel** | **≈13** |
| Motorlu, pervaneler **akışa dik** | **≈9** |

**Bu tablo Fatura 2'nin en temiz ifadesidir.** Tek uçak, tek tünel, tek oturum.
VTOL donanımını takmak L/D'nin **%24'ünü** götürüyor (17→13). Pervaneyi akışa
hizalayamamak **%31 daha** götürüyor (13→9).

SkyProwler: çekilmiş **≈11**, açık **≈8**.

#### Bulgu 2 — sürükleme azaltma (Tablo 35)

| Karşılaştırma | Azalma |
|---|---:|
| Mini Talon 2, açık → çekilmiş | 63% |
| **Mini Talon 3 (standart quadplane) → Mini Talon 2 çekilmiş** | **34%** |
| SkyProwler, açık → çekilmiş | **30%** |

⚠️ **Yazarın kendi uyarısı:** %63 doğru karşılaştırma **değildir** — aracı kendisiyle
kıyaslıyor. Doğru kıyas standart quadplane'e karşıdır: **%34.** Bu dürüstlüğü
makalede anmaya değer.

#### 🎯 Bulgu 3 — bedel motorlarda, pervane kanadında değil

> *"The difference between propellers parallel to the airflow and without propellers
> is **modest**. The drag produced by the **motors is significant**."*

Yani ceza esas olarak **motorlar ve taşıyıcı kollardan** geliyor. Pervaneyi
serbest bırakmak ya da yelpazelemek bunu **çözmez** — kütle zaten gemide.

#### Bulgu 4 — kilit açısı iddiası doğrulandı

> *"their takeoff propellers **must be free to rotate and to align to the airflow**"*

Bölüm 5.2'den doğrulanamadığı için çıkardığım iddia **geri geldi**, üstelik
ölçümle: dik %9, paralel %13.

#### 🎯 Bulgu 5 — **devredilebilirlik tezimizin deneysel kanıtı**

Kitty Hawk Cora verisine %30 sürükleme azaltma + **%5 sistem kütlesi** uygulanınca:

| | Değer |
|---|---:|
| Azami menzil | 119 km → **121 km** (+%1,7) |
| Azami menzil hızı | **+5 m/s** |
| 80 km'lik görev | **10 m/s daha hızlı** uçulabiliyor |
| Gözetleme İHA'sı için fayda | **sınırlı** (havada kalış düşük hızda azamileşir, orada sürükleme azaltma az etkili) |

🎯 **Bu, Bölüm 3.5'in tam olarak iddia ettiği şeydir.** Sürüklemenin %30'u
kaldırıldı, karşılığında kütlenin %5'i ödendi, menzil kazancı **%1,7**'de kaldı.
**Fatura ödenmedi, devredildi.** Elimizdeki en güçlü deneysel destek bu.

#### Ölçekleme uyarısı (§5.4.3)

Sürükleme azaltması model ölçekten tam ölçeğe **sabit** varsayılmış; yazar bunu
"muhafazakâr" sayıyor.

#### ⛔ Çıkarılan sayılar

| Arama motorundan gelen | Tezde bulunan |
|---|---|
| "%38 parazit sürükleme azalması" | **Yok.** Tezde 63 / 34 / 30 var |
| "aynı hızda **+%13 menzil**" | **Yok.** Tezde 119→121 km = **+%1,7** |
| "aynı menzilde +%21 hız" | Tezde **+5 m/s** ve "80 km görev 10 m/s daha hızlı" |

**Üçüncü kez:** arama motoru sentezi sayı için kullanılamaz.

### [K2] Wind Tunnel Testing of a QuadPlane UAS · durum: **A**
arXiv:2301.12316

**Doğrulanan alıntılar:**
> *"The highest lift and least drag is experimentally observed in **Plane mode** for
> both cruise airspeeds."*

> *"Drag in Quadrotor mode is generally less than drag in Hybrid mode **due to
> adverse flow interactions** in Hybrid mode."*

> *"The simulation model... based on ideal case assumptions of **negligible flow
> interaction** between rotors and the vehicle structure, **always predicts higher
> lift and lower drag than were experimentally observed.**"*

**Tablo 7 + 8'den türetilebilen sayı** (α=0, doğrusal uyum):

| $V_a$ | Plane toplam | Hibrit toplam ($C_{DP_0}+C_{DQ_0}$) | Oran |
|---:|---:|---:|---:|
| 11 m/s | 0,3154 | 0,3127 + 0,3519 = 0,6646 | **2,11×** |
| 15 m/s | 0,2398 | 0,2400 + 0,2891 = 0,5291 | **2,21×** |

⚠️ **Bu sayı dikkatli kullanılmalı, üç sebeple:**
1. Hibrit kipte rotorlar **dönüyor** ve taşımaya katkı veriyor → temiz bir seyir
   sürüklemesi karşılaştırması değil.
2. Plane kipinde dikey rotorlar **zaten takılı** (yalnızca durmuş). Yani kaynak,
   "kaldırma rotoru taşımanın bedeli"ni hiç ölçmüyor — ölçemez, çünkü rotorsuz
   hâli test etmiyor.
3. Toplamın $C_{DP}+C_{DQ}$ şeklinde eklenebilir olduğu bizim varsayımımız.

**Makalede kullanılacak olan:** doğrulanmış niteliksel alıntılar. Türetilmiş
2,1× oranı yalnızca dipnotta ve üç uyarısıyla.

### [K3] Sahwee ve ark. 2019 · durum: **A**
**Drag Assessment of Vertical Lift Propeller in Forward Flight for Electric
Fixed-Wing VTOL UAV** · IOP Conf. Ser.: Mater. Sci. Eng. 705:012007
DOI: 10.1088/1757-899X/705/1/012007

Rüzgâr tüneli, **26 pervane örneği** (5–9 inç), akışa dik yerleştirilmiş, durgun.

> *"Without complex mechanism to store the inactive hover powertrain, the hover
> powertrain components added a **significant amount of aerodynamic drag** during
> forward flight."*

**Bulgular:** sürükleme çapla (ön alanla) doğru orantılı; $V^2$ ile artıyor; hatve
arttıkça artıyor. **En düşük sürükleme = en küçük çap + en düşük hatve.**

🎯 **Bizim için doğrudan sonuç:** N95 — uç pervanelerini **0,20 m'de küçük
tutma** kararı bu kaynakla desteklenir. Aynı zamanda K2'nin niteliksel
bulgusunun bağımsız ikinci teyididir.

### [K4] NASA Lift+Cruise yüksek-doğruluklu CFD · durum: **A** (kısmen ilgili)
**High-Fidelity Simulations of Lift+Cruise VTOL Urban Air Mobility**
NTRS 20230016503 · AIAA SciTech 2024

⚠️ **Beklediğimiz içeriği vermiyor:** çalışma **hover (helikopter kipi)** odaklı;
seyirde durmuş rotor sürüklemesini incelemiyor.

Kullanılabilir tek bulgu: hover'da gövdeden gelen **negatif taşıma (download)
araç ağırlığının ≈%10'u**. Bu, lift+cruise'un hover'da ödediği ek bir bedeldir ve
Bölüm 3'e dipnot olarak girebilir.

⛔ Bölüm 5.2'deki "kilit açısı serbest akışa hizalı olmalı" ifadesi **bu kaynaktan
doğrulanamadı** — o iddia VFS 2025 bildirisine (K6) aitti ve okunmadı.

---

## 3. Yenilik sınırı

### [K6] VFS Forum 81 (2025) · durum: **C**
**Aerodynamic Analysis of Stopped and Stopping Rotors in Lift+Cruise eVTOL
Configurations** · Okunmadı. İddia: serbest akışa hizalı kilit açısı sürüklemeyi
en aza indirir. **Doğrulanana kadar makalede kullanılmayacak.**

### [K7] Xu, Gu, Qing, Lin, Zhang 2019 · durum: **A** ⭐
**Full Attitude Control of an Efficient Quadrotor Tail-sitter VTOL UAV with
Flexible Modes** · arXiv:1903.06393

**Doğrulanan alıntı (özet):**
> *"This control system is working in all flight modes **without any control surfaces
> but motor differential thrusts**."*

**Doğrulanan alıntı (§II.A):**
> *"In the latest version, there is **no aileron and elevator** which means servos are
> no longer needed. The control moments are produced by the **propeller differential
> thrusts only**."*

**Araç (Tablo I):** yamuk kanat, **MH-115** profil, açıklık **0,90 m**, sivrilme 0,48,
**ok açısı 7,3°**, kök veter 0,20 m, **dört tek rotor** (APC 9×6E), elektrikli.

**Kumanda yüzeysizliğin gerekçeleri (bizim Bölüm 4.4'ü destekler):**
1. Servo ve ilgili yapı toplam ağırlığın **≈%5**'i; kaldırılması ölü ağırlığı azaltır
2. Kumanda yüzeyi **tutukluk açısının üstünde otoritesini yitirir**; rotor etkinliği
   hücum açısından **çok az** etkilenir
3. Servo, dişli kutusundan gelen doğrusalsızlık ve ek dinamik getirir → kumanda
   bant genişliğini sınırlar

**Uçuş testi bulgusu (Bölüm 3.4'ü doğruluyor):**
> *"the power consumption at level flight is **five times less** than that of in
> hovering"*

Bizim $P_{hover}/P_{cruise}$ türetimimiz bu sınıf için ~4–5 veriyor. **Ölçülmüş
teyit.**

🎯 **En kritik bulgu — mimari çatallık:** araç dört **tek** rotor kullanıyor ve
yuvarlanmayı **diferansiyel tepki torkundan** alıyor. Bizim koaksiyel çiftimiz o
torku tasarım gereği sıfırlıyor. **Onların yuvarlanma aktüatörü, bizim bilerek yok
ettiğimiz şeydir.**

⚠️ **Full Attitude Control of a VTOL tailsitter UAV**, IEEE 2016 — **hâlâ okunmadı**
(ücretli). Aynı grubun önceki çalışması; o sürümde kumanda yüzeyi vardı.

### [K8] Kuyruğa oturanın seyir üstünlüğü yerleşik kabuldür · durum: C
Makale bunu keşif gibi sunmaz; **türetimini** sunar (Bölüm 3.6).

---

## Öncelik sırası — bundan sonrası

| # | Kaynak | Durum | Neden |
|---|---|---|---|
| 1 | **K1 Bacchini ve ark.** | C | Bölüm 3.3 + 5.2'nin yükü. **Yol 1: doktora tezi, açık erişim** |
| 2 | ~~K7 arXiv:1903.06393~~ | ✅ **A** | Okundu. Bölüm 4.4'ün mimari çatallık savı buna dayanıyor |
| 3 | K7 IEEE 2016 | C | Aynı grubun eski sürümü. Ücretli. Düşük öncelik |
| 4 | K6 VFS 2025 | C | Kilit açısı iddiası. Makaleden zaten çıkarıldı |

---

## 4. Rakip verisi

### [K9] HAVELSAN BAHA üretici föyü · durum: **A** (üretici belgesi)

| | Değer |
|---|---:|
| MTOW | 28 kg (yük dâhil) |
| Faydalı yük | 2 kg → **%7,1** |
| Açıklık / boy | 4,0 m / 2,1 m |
| Seyir hızı | 75–80 km/sa (40–43 kts) |
| Havada kalış | **2 saate kadar** |
| Tavan / işletme irtifası | 10 000 ft / 8 000 ft |
| Veri bağı | 50 km (opsiyonel 80 km) |
| İtki **ve** VTOL | **Elektrik motoru** |
| **Rüzgâr sınırı** | **kalkış/iniş 15 kts · seyir 25 kts** |

✅ **VTOL olduğu doğrulandı** — "Runway Independent VTOL Mission Capability".
Açık iş kapandı.

🎯 **Rüzgâr sınırı satırı N79'un dayanağıdır.** Sahadaki bir VTOL İHA'nın
**yayımlanmış** kalkış/iniş rüzgâr sınırı seyir sınırından düşük. Yer rüzgârı
işletme sınırı bu sınıfta olağandır. Bölüm 8.9'a girdi.

⚠️ **Menzil/havada kalış karşılaştırmasına kapalı:** araç tamamen elektrikli,
2 saat **pil sınırıdır**. Bizim hibrit 15,7 saatimizle karşılaştırmak enerji
kaynaklarını karşılaştırmak olur, mimarileri değil.
