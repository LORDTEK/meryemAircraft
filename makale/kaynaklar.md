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

### [K1] Bacchini & Cestino 2021 · durum: **C** ⚠️ · **hâlâ en kritik eksik**
**Impact of lift propeller drag on the performance of eVTOL lift+cruise aircraft**
*Aerospace Science and Technology* 109:106429 · DOI: 10.1016/j.ast.2020.106429

| Bulgu | Değer |
|---|---:|
| Pervaneleri içeri çekmenin parazit sürüklemeye etkisi | −%38 |
| Aynı menzilde seyir hızı kazancı | +%21 |
| Aynı hızda menzil kazancı | **+%13** |

**Neden önemli:** mimari-içi kontrollü karşılaştırma (aynı uçak, tek değişken),
ve sonucu menzil cinsinden veriyor.

🔴 **HÂLÂ C SEVİYESİNDE.** ScienceDirect ücretli; tasarımcı e-posta ile istedi.
**Bölüm 3.3 ve 5.2'nin yükünü bu taşıyor. Gelmezse o paragraflar niteliksele
çevrilmeli.**

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

### [K7] Kumanda yüzeysiz kuyruğa oturanlar · durum: **C**
- **Full Attitude Control of a VTOL tailsitter UAV**, IEEE, 2016
- **Full Attitude Control of an Efficient Quadrotor Tail-sitter VTOL UAV with
  Flexible Modes**, arXiv:1903.06393, 2019

⚠️ Bölüm 4.4'ün dayandığı kaynak. **Başvurudan önce
okunmalı.** arXiv olanı ücretsiz.

### [K8] Kuyruğa oturanın seyir üstünlüğü yerleşik kabuldür · durum: C
Makale bunu keşif gibi sunmaz; **türetimini** sunar (Bölüm 3.6).

---

## Öncelik sırası — bundan sonrası

| # | Kaynak | Durum | Neden |
|---|---|---|---|
| 1 | **K1 Bacchini & Cestino** | C | Bölüm 3.3 + 5.2'nin yükü. E-posta beklemede |
| 2 | **K7 arXiv:1903.06393** | C | Bölüm 4.4'ün dayanağı. **Ücretsiz** |
| 3 | K7 IEEE 2016 | C | Aynı. Ücretli |
| 4 | K6 VFS 2025 | C | Kilit açısı iddiası |
