# Step 14 — What does not close

**v8 taslağı, birinci yazım (Tur 56).** İskeletin 14. adımı: *"Kapanmayanlar — önce batarya, bilinen
engel olarak; sonra bilinmeyenler."* Adım 9 bu bölümü *"bir borç"* diye tanımladı: makalenin
cevaplamadığı ve daha iyi kanıtın cevaplayacağı sorular.

**Bu sayfa yeni bir hesaba dayanıyor:** `aero/buffer.py` → `aero/buffer-result.txt`. Tampon **bara
tabanında** (v7'nin `thrust.py`'de kurduğu istasyon kuralı), Adım 10'un dört kapanışında, ve tampon
özgül güçten **döngünün içinde** türetilerek. Döngü, özgül güç Adım 10'un ima ettiği değere
konunca Adım 10'u birebir üretiyor (üretmezse durur).

**Bu hesap iki yan bulgu çıkardı:**

- **3,8× artık 3,7–4,1×.** Adım 10'un kapanışları yayımlanmış tasarım değil: η_p daha düşük, motor daha
  büyük, kütle daha fazla. Kalkış talebi kapanışlarda 5,5–6,1 kW/kg; 1,49'a oranı 3,7–4,1.
- **Adım 11 ve 12'nin açık sayıları mil−mil çıkarmasıydı** — v7'nin kendi düzelttiği istasyon
  karışıklığı v8'e geri gelmişti. Bara tabanında: Adım 11 0,168–0,188 kW/kg (%12; önce 0,128–0,150,
  %17); Adım 12 0,202 → 0,199 (önce 0,166 → 0,162). **Sonuçlar değişmedi**: en çok tampon isteyen köşe
  yine en az tamponu alıyor; ölçekle değişim yine ~%2.

**Kaynak kuralı (§2.1):** ölçülmüş paket sayıları bu tur PDF'ten okundu. **v7'nin *"the highest rate
yet measured on a flown pack"* ifadesi kaynağa uymuyor:** 1,5 kW/kg **tezgâhtaki 24S1P test paketinde**
ölçüldü, uçan sistem 24S4P; ve *"yet"* aranmamış bir genelleme (§2.2). Gövdede yok.

**Kural denetimi:** 3,8×'in tek evi burası, tek paragraf (Grok, Tur 34) · Adım 10 onu anlatmıyor ·
mekanizma iddiası bu sayfadaki hiçbir kaleme bağlı değil — bu **denetlendi**, aşağıda.

---

## What does not close

Section 10 closed the sizing loop on a declared package and said that whether an aircraft can be
built to it is a different question. **This section is where that question is answered, and for the
first item the answer is no.** Section 9 called this section a debt: questions the paper does not
answer and that better evidence would. It is stated in that order — first the obstacle that is known,
then what is not known.

### First, the known obstacle: the energy store

**Every closure in Section 10 carries a buffer of 3.6 percent of take-off mass.** That figure is an
input, not a result (Sections 11 and 12). What it implies can be computed. Taken at the electrical bus,
where the buffer sits — the rotor demand divided by the machine and power-electronics efficiencies, less
what the engine delivers through its generator — **the four closures ask the buffer for 4.7 to 5.2 kW
per kilogram to hover, and 5.5 to 6.1 kW per kilogram to leave the ground** with the tip pairs at full
thrust, which is where the take-off margin comes from (Section 5).

**What has been measured is a fraction of that.** A 24-series nickel–cobalt–manganese pack designed,
bench-tested and flown in a 210 kg-class electric VTOL aircraft is rated, as a flight system, at
0.892 kW per kilogram continuous; its 13.5 kg unit pack, discharged on the bench at its highest tested
rate of 10.68C, delivered on average about 1.5 kW per kilogram and reached 55.1 °C against the 60 °C
limit its authors adopted. A NASA-funded design study adopts 4 kW per kilogram and describes that
figure as about twice that of existing batteries. **The take-off demand of Section 10's closures is 3.7
to 4.1 times the highest of the measured rates, and 6.2 to 6.8 times the flight system's continuous
rating**; hover alone is 3.1 to 3.5 times the highest measured rate. **The package Section 10 closes on
does not exist with any store the sources consulted here report as built.**

**Closing the loop on a measured store does not make the aircraft impossible; it makes it a different
aircraft.** Deriving the buffer inside the loop from the take-off demand at a given specific power, and
holding the fuel fraction so that range is unchanged:

| Buffer specific power | Take-off mass | Buffer | Change from Section 10 |
|---|---:|---:|---:|
| As Section 10 implies — 5.5 to 6.1 kW kg⁻¹ | 52.3 to 57.5 kg | 3.6 % | — |
| 4 kW kg⁻¹, the design-study assumption | 56.6 to 61.2 kg | 5.0 to 5.5 % | +6 to +8 % |
| About 1.5 kW kg⁻¹, the highest measured rate | 94.6 to 101.2 kg | 13.4 to 14.7 % | **+76 to +81 %** |
| 0.892 kW kg⁻¹, the flight system's continuous rating | about 335 kg | 22 to 25 % | set by nearness to non-closure |
| 0.724 kW kg⁻¹, the unit pack's continuous rating | **does not close** | — | — |

**At the highest measured rate the aircraft exists and is three-quarters heavier**, with a buffer of
about fourteen percent of take-off mass rather than 3.6. Held instead at Section 10's closed masses, it
carries a payload of about 7 kg rather than 13. At the flight system's continuous rating the loop only
just closes, and the mass it returns is set by how near the loop is to not closing rather than by
anything about the aircraft. At the unit pack's continuous rating it does not close at all.

**This is where the coupling Section 12 found is paid.** The buffer is the conversion the escape
condition permits — kilowatts of hover peak paid in kilograms of store — and at a measured specific
power the conversion costs thirteen to fifteen percent of take-off mass instead of 3.6. **The escape
from Bill 3 is real in the sense Section 3 defined it, and its price depends on a component whose
required performance has not been demonstrated.** Section 13 holds the store common to all three
architectures at 3.6 percent; how its orderings would move with a measured store is not computed.

### What the obstacle does not touch

**The mechanism claim does not depend on it.** Sections 7 and 8 count the classes of mechanism that a
tilting architecture needs to change regime and this one does not; that is a statement about hardware,
and a heavier store changes none of it. **The cruise-efficiency comparison of Section 6 does not depend
on it either**: it is made in effective lift-to-drag ratio, a ratio of aerodynamic and propulsive
efficiencies that the buffer's mass does not enter. **What the obstacle bears on is whether this
aircraft, at these numbers, can be built** — which the paper does not claim.

### Then what is not known

The remaining items are not known obstacles; they are questions this work has not answered. They are
grouped by what would settle them.

| Item | Bears on | What would settle it |
|---|---|---|
| **The pitching moment through the transition.** Three methods of three fidelities diverge above about ten degrees of incidence; the rotation passes through that band, peaking near 18 to 22 degrees on the reference geometry, with the inboard half of the wing in the slipstream at a much lower effective incidence. | Whether the aircraft trims through the rotation (Sections 7 and 10) | **Measurement**: the outboard wing's pitching moment to about 22 degrees at low dynamic pressure, and trim at the attached-flow end of the rotation |
| **Section drag at low Reynolds number.** The attitude rotors' free-wheeling charge rests on section polars below a Reynolds number of 10⁵, and the uncertainty runs both ways. | The 0.0154 rotor term in every closure (Sections 10 and 11) and the size of Bill 2's fall with scale (Section 12) | **Measurement**: the drag of a free-wheeling attitude rotor, or of its sections, at about 8 × 10⁴ |
| **The airframe's mass.** It enters the loop as a construction constant, thirty percent of take-off mass (Section 11). A component build-up at the reference mass leaves room for the 13 kg payload only if the average shell areal density stays at or below 1.78 kg m⁻², against 1.50 assumed; the build-up carries a contingency rather than a structural sizing, and it has not been re-run at Section 10's closed masses. At the heavy design the shell-mass exponent is not measured at all. | Every closed mass | **Structural sizing**, then a built article |
| **The competitor's lift-group mass.** It decides the sign of the fixed-take-off-mass ordering in Section 13. | Section 13's sensitivity, not a claim | **Measured inventories** of lift-plus-cruise aircraft of this class |
| **Closed-loop hover control**, including the cost of declining the reaction-torque channel, and the allocation of the tip pairs between take-off margin and attitude authority, which compete for the same propellers. | Whether hover is controllable with the authority computed (Sections 5 and 8) | **Analysis not yet done**: a control-allocation study, then simulation |
| **Vertical descent and the landing transition.** Neither is analysed; the vortex ring state is not assessed, and the landing transition is not the take-off transition run backwards. | Whether the aircraft can come down as it went up (Section 5) | **Analysis not yet done** |
| **Engine installation** — bay, intake, exhaust, cooling. | Mass, drag and packaging | **Absent from this work entirely** |
| **Atmosphere.** Every number here is at sea level. | The comparison in Section 6, made against a mission flown at altitude | **Analysis**: the direction of the effect has not been computed |

**None of these is a small correction to a known quantity.** Two of them belong to measurement rather
than to more computation: the transition moment, because three methods have been tried against it and
disagree, and the low-Reynolds section drag, because the one method used here is least reliable exactly
there. Two — hover control and the descent — are analyses this study has not posed. One — the engine
installation — is not in the work at all.

### What this section amounts to

**The loop closes; the aircraft is not shown to.** At the energy store the paper can name the gap
exactly, in specific power and in take-off mass. Everywhere else it can name only what would settle the
question. **The architecture
claim — that the regime change is made with no mechanism that reorients a propulsor — is a count of
hardware, and nothing in this section reaches it.** What this section reaches is the aircraft, and the
paper has not claimed the aircraft.

The last section returns to the four axes of Section 9 and states what is claimed on each.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| Kapanışlar %3,6 tampon taşıyor; tampon girdi | `closure.py` (`f_tampon=0.036`); Adım 11–12 |
| Bara kuralı: P_mil/(0,92×0,95) − P_motor×0,90 | `aero/thrust.py` satır 21–30 ve 168–170; `aero/buffer.py` |
| Aşkı 4,68–5,23, kalkış 5,53–6,09 kW/kg | `buffer-result.txt` §1 |
| Kalkış talebi = aşkı × (1 + 4×335/10 900) = ×1,123, uç çiftleri tam (T/W 1,132) | `buffer.py` `UC_PAYI`; `thrust.py` |
| **Yu ve ark. 2026:** VS-210, 210 kg sınıfı; 24S4P uçan sistem 892 W/kg sürekli (4×110 A'dan hesaplanmış); 24S1P 13,5 kg | `references/Yu-2025_24S-NCM-battery-eVTOL-IN-FLIGHT_Batteries.pdf`, Tablo 3 (bu tur açıldı) |
| **~1,5 kW/kg türetildi:** 10,68C'de 1394,3 Wh, 4 dk 09 s, 13,5 kg → 1,49 kW/kg ortalama | aynı, deşarj tabloları (satır 707, 759 metin çıktısında) |
| 55,1 °C, sınır 60 °C, ısıl pay 4,9 °C; yerel sıcak noktalar ölçülmemiş | aynı, §3 ve Özet |
| **Barrett ve ark. 2023 (NIAC):** *"the specific power (4 kW/kg) is about twice that of existing batteries"* | `references/Barrett-2023_NIAC_solid-state-EAD-propulsion_MIT.pdf` (bu tur açıldı) |
| Oranlar: kalkış/1,49 = 3,7–4,1; kalkış/0,892 = 6,2–6,8; aşkı/1,49 = 3,1–3,5 | `buffer-result.txt` §1 (aşkı oranı: 4,68/1,49 = 3,14; 5,23/1,49 = 3,51) |
| Döngü tablosu (5 satır); 4 kW/kg satırı +6,5…+8,2 % | `buffer-result.txt` §3; sınama §2 |
| Sabit MTOW'da faydalı yük ~7 kg (7,2–7,4) | `buffer-result.txt` §4 |
| Menzil değişmez (yakıt kesri sabit, L/D sabit) | `buffer.py` döngüsü; Adım 13'ün sözleşme 1 mantığı |
| Etkin L/D = (L/D)·η_p, kütleden bağımsız | Adım 6 |
| Adım 13 tamponu ortak tutuyor | Adım 13 |
| Geçiş: ~10° üstü üç yöntem sapıyor | Adım 10 satır 207–211 |
| **Tepe hücum 17,5° (5 m/s tırmanışla), 21,6° (düz askıdan); iç yarı 4–8° etkin; ölçüm dış yarı için ~22°'ye kadar; zor kısım bağlı akış ucu** | v7 §3.17 satır 2329–2341, §4.4 satır 2651–2654 — **v7 hesabı, bu tur yeniden koşulmadı**; referans geometride |
| Düşük Re, iki yönlü | Adım 12 |
| Kabuk yoğunluğu kırılma 1,783 kg/m², taban 1,50; kurulum yayımlanmış kütlede; %12 belirsizlik payı | `aero/mass.py` çıktısı (bu tur koşuldu): *"kabuk kg/m2 taban 1.50 -> kirilma 1.783"*, *"belirsizlik payi (kurunun %12'i)"* |
| Kabuk üssü ölçülmedi (ağır) | Adım 12 |
| Kaldırma grubu kesri işareti belirliyor | Adım 13 |
| Kontrol, girdap halkası, iniş geçişi, motor yerleşimi | Adım 5; Adım 11 *"What the closure does not contain"* |
| Deniz seviyesi; NASA görevi 5000 ft ISA+20 | Adım 6 satır 182–185 |

**Bu sayfada BİLEREK olmayanlar:**

- **Ağır tasarımın tamponu.** Ağır tasarımın kapanışı yok (Adım 12).
- **Tampon ölçüldüğünde lift+cruise'a ne olduğu.** v7 lift+cruise'un daha çok acı çektiğini söylüyordu
  (askı gücü/kütle en yüksek); aynı disk yüklemesinde bu **denetlenmedi** ve iddia edilmedi.
- **"Bataryalar gelişiyor" iyimserliği.** Gelecek özgül güç tahmini yok.
- **Motor pay farkı (1,53 / 1,39).** Yalnız Adım 12'yi etkiliyor, orada söylendi.
