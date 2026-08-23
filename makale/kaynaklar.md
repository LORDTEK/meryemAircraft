# Kaynak defteri

**Doğrulama durumu kodları:**
- `A` — makalenin tam metni birinci elden okundu
- `B` — özet/künye birinci elden okundu, tam metin okunmadı
- `C` — yalnızca arama motoru özeti; **sayı birinci elden doğrulanmadı**

> ⚠️ Bu oturumda ağ çıkışı kısıtlıydı (arxiv, sciencedirect, ntrs.nasa.gov,
> iopscience, mdpi, semanticscholar, openalex — hepsi `EGRESS_BLOCKED`).
> Aşağıdaki kayıtların tamamı **C** seviyesindedir. Makale yayıma gitmeden önce
> her biri en az **B** seviyesine çıkarılmalıdır.

---

## Fatura 2 — seyirde açıkta duran hover donanımının bedeli

### [K1] Bacchini & Cestino 2021 — **en güçlü kaynak** · durum: C
**Impact of lift propeller drag on the performance of eVTOL lift+cruise aircraft**
*Aerospace Science and Technology*, cilt 109, madde 106429, 2021.
DOI: 10.1016/j.ast.2020.106429

Rüzgâr tüneli: aynı eVTOL modeli, pervaneler **açıkta** ve **içeri çekilmiş** hâlde.

| Bulgu | Değer |
|---|---:|
| Pervaneleri içeri çekmenin parazit sürüklemeye etkisi | **−%38** |
| Aynı menzilde seyir hızı kazancı | **+%21** |
| Aynı hızda menzil kazancı | **+%13** |

**Neden en güçlüsü:** Bu bir **mimari-içi kontrollü karşılaştırmadır.** Aynı uçak,
aynı kanat, aynı Reynolds sayısı, aynı görev — tek değişken hover donanımının
açıkta olup olmaması. Kanat tasarımı, ölçek veya görev farkından gelen hiçbir
karıştırıcı değişken yok. Faturayı **izole eden** tek kaynak budur.

**Daha da değerlisi:** sonucu sürükleme katsayısı olarak değil, **menzil ve hız**
olarak veriyor. Yani faturayı, makalenin konuştuğu para biriminden ödüyor.

### [K2] QuadPlane rüzgâr tüneli karakterizasyonu · durum: C
**Wind Tunnel Testing and Aerodynamic Characterization of a QuadPlane
Uncrewed Aircraft System** · arXiv:2301.12316

| Bulgu | Değer |
|---|---:|
| Hibrit kipte rotor-iz girişiminin sürüklemeye etkisi | **+%20–40** (düz uçuş kipine göre) |
| Ölçülen en düşük parazit sürükleme katsayısı | **C_D0 = 0,0397** (VTOL rotorları ve kolları dâhil) |
| En yüksek taşıma / en düşük sürükleme | **düz uçuş kipinde** (her iki seyir hızında) |
| Girişimin en yüksek olduğu hâl | beş rotorun da döndüğü an |

⚠️ **K1 ile K2 aynı şeyi ölçmüyor.** K2 rotorlar dönerken *girişim* sürüklemesini,
K1 rotorlar durmuşken *parazit* sürüklemesini veriyor. Makalede yan yana
konurken bu ayrım açıkça yazılmalı, yoksa hakem ilk buraya vurur.

### [K3] Kanat üzerinde duran dikey pervaneler · durum: C
**Aerodynamic performance of aircraft wings with stationary vertical lift propellers**
*Aerospace Science and Technology*, Ağustos 2023.
DOI: 10.1016/j.ast.2023.108524 *(numara doğrulanmalı)*

Rüzgâr tüneli: bir kanat üzerinde iki tandem, kenar-akışlı, **duran** pervane.
Niteliksel bulgu: duran pervaneler, akış ayrılması ve büyük ön alan nedeniyle
**ciddi sürükleme üretir**; hover güç aktarma organları saklanmadığı sürece ileri
uçuşta belirgin sürükleme ekler. *Sayısal değer alınamadı.*

### [K4] Duran ve durmakta olan rotorlar · durum: C
**Aerodynamic Analysis of Stopped and Stopping Rotors in Lift+Cruise eVTOL
Configurations** · Vertical Flight Society 81st Annual Forum, 2025.

Bulgu: rotorun kilitlendiği açı önemlidir; **serbest akışa hizalı kilit açısı**
sürüklemeyi ve asimetriyi en aza indirir. Yani bu mimaride sürükleme, ancak
**ek bir indeksleme mekanizmasıyla** kabul edilebilir seviyeye çekiliyor —
mekanizma da Fatura 1'e yazılıyor.

### [K5] NASA Lift+Cruise referans aracı · durum: C
**VTOL Urban Air Mobility Concept Vehicles for Technology Development**
(Silva ve ark., NASA) ve ilgili yüksek-doğruluklu CFD çalışmaları.

| Bulgu | Değer |
|---|---:|
| Seyirde çalışma L/D | **≈ 13,5** |
| Sürükleme dökümüne dâhil olanlar | gövde, rotor göbekleri, **kollar**, dikey kuyruk, iniş takımı |
| Rotor kipi | uçak kipinde bıçak ekseni gövde eksenine hizalı kilitleniyor |

⚠️ **Bu sayı bizim 12,7'mizle doğrudan karşılaştırılamaz.** NASA aracı yolcu
sınıfı, çok daha yüksek Reynolds sayısı ve farklı açıklık oranı. Makalede
"bizimki daha iyi" imasına **asla** dönüştürülmeyecek (N58, yazım kuralı 2).
Kullanımı yalnızca **mertebe bağlamı** vermektir.

---

## Kuyruğa oturanın seyir üstünlüğü — **yenilik açısından dikkat**

### [K6] Yerleşik kabul · durum: C
Kuyruğa oturanın lift+cruise'a göre seyirde daha verimli olduğu, akademik
literatürde ve uygulayıcı belgelerinde (ör. PX4 VTOL kılavuzu) **zaten yerleşik
bir kabuldür**: birincil itki sistemi seyre dönüştüğü için ikinci sistemin ölü
ağırlığı doğmaz.

⚠️ **Sonuç: "kuyruğa oturan daha verimlidir" iddiası YENİ DEĞİLDİR.**
Makale bunu bir keşif gibi sunamaz. Sunabileceği şey, bu bilinen üstünlüğün
**neden mimari bir zorunluluk olduğunun** açık türetimi (Bölüm 3.6) ve
**bileşimin kendisidir**.

### [K7] Kumanda yüzeysiz kuyruğa oturanlar · durum: C
- **Full Attitude Control of a VTOL tailsitter UAV**, IEEE, 2016
- **Full Attitude Control of an Efficient Quadrotor Tail-sitter VTOL UAV with
  Flexible Modes**, arXiv:1903.06393, 2019

⚠️ **Kritik bulgu.** Literatürde "hiçbir kumanda yüzeyi olmadan, yalnızca motor
diferansiyel itkisiyle tüm uçuş kiplerinde çalışan" kumanda sistemi **zaten
sunulmuştur.** Ayrıca kuyruğa oturanın **kanat-gövde (BWB), kuyruksuz** olması
literatürde "tipik" diye tarif ediliyor.

**Ama:** bu araçlar dört pervaneyi açıklığa dağıtır ve yuvarlanmayı çoğunlukla
**pervane izindeki elevonlarla** çözer. Bizde tek merkezî itki var, açıklığa
dağıtılmış itki yok, ve yuvarlanma **oransal bir kumanda yüzeyiyle değil**,
gövde altındaki aç-kapa şeritle çözülüyor.

**Yapılacak:** yenilik iddiası, bu kaynaklar okunmadan Bölüm 4'te ve patent
isteminde **daraltılarak** yazılmalı. Prior-art taramasına (künye §9) eklenecek.

---

## Makaleye girmeyecek olan

**"Yüksek seyir hızında rotor kaynaklı sürükleme kanadın biçim sürüklemesini
geçer."** — Bu ifade için **hiçbir kaynak bulunamadı.** Bölüm 3'ten çıkarıldı.
Doğrulanmamış sayı vermektense az söylemek yeğdir (yazım kuralı 3).
