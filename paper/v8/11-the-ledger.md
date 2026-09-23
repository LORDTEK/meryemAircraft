# Step 11 — The ledger

**v8 taslağı, birinci yazım.** İskeletin 11. adımı.

**Kapsam Grok ve DeepSeek tarafından, Tur 52'de birlikte konuldu ve kabul edildi:**
defter **atıf yapar, eklemez.** Adım 10'un sayıları uç çerçeve sürüklemesini, sabit hatve
uzlaşmasını, burulma bedelini ve hepsinin kütle sonuçlarını **zaten içeriyor**; defter
bunları tekrar eklerse `closure_inputs.py`'de yakalanan çift sayımın düzyazı hâli olur.

**Kural denetimi:** hiçbir kalem eklenmiyor, **ayrılıyor** · DeepSeek'in ayrımı korunuyor
(ayrıştırılabilir / ayrıştırılamaz) · **tek bir "mimarinin bedeli" sayısı verilmiyor** ve
neden verilmediği yazılıyor · **3,8× burada GEÇMİYOR** (Grok: *"o paket 14'te tek paragraf
kalır"*) · sıralama yok, Adım 13'ün işi.

---

## The ledger

Section 2 named three charges that any architecture in this corner pays. Section 10 closed a
sizing loop. **This section puts the two together: it says where each charge appears inside
the closed numbers, and how large it is there.** Like the closure, the ledger prices the
arrangement; the count of mechanism classes is not an entry in it.

### What this section does, and the one thing it must not do

**It attributes. It does not add.** Every cost named below is already inside the closure of
Section 10 — in the drag bracket, in the propeller efficiency, in the empty-mass fraction, in the
engine rating. **No new physical cost term is introduced here.** The shares, ratios and
percentages below are new calculations, but each is a decomposition or a derived measure of a
quantity the closure already reported, and adding any of them again as a separate charge would be
double counting.

**Two kinds of item appear, and the difference is stated rather than smoothed over.** Some
costs were computed per source and can be split: the drag build-up has named terms, and the
mass fractions were solved separately. Others are inside a single computed quantity and **the
study did not separate them**; saying otherwise would invent a decomposition that was never
performed. Each is marked.

**And there is no single figure for what the architecture costs.** The three charges are in three
different currencies — kilograms, drag counts, installed kilowatts — and **no scalar aggregate is
defined, because this study has no defensible weighting between them.**

**The refusal has an address, and saying where it points is what keeps it from reading as an
unfinished cost section.** These three quantities become one number only under a sizing contract,
and that is Section 13: **the total is the contract, not a property of the aircraft.** For a
specific mission a designer weights them against that mission's own constraints. **Reporting them
is this paper's job; the weighting belongs to whoever has the mission.**

### Bill 2 — the drag of hover hardware, inside the bracket

The zero-lift drag coefficient of Section 10 is a build-up with named terms. Splitting it:

| | favourable end | adverse end |
|---|---:|---:|
| Clean wetted surface | 0.0073 | 0.0142 |
| Hub and small items | 0.0015 | 0.0022 |
| **Tip frames** | **0.0043** | **0.0047** |
| **Attitude rotors, free-wheeling** | **0.0154** | **0.0169** |
| Total | 0.0285 | 0.0381 |

*(The two columns differ for two separate reasons, and a reader dividing cells should know which
is which. The clean surface and the hub are where the drag bracket itself lives, so their base
values differ between the ends. On top of that, the adverse end carries a ten percent margin
applied to the whole build-up. The frames and rotors have the same base value at both ends and
differ only by that margin. **No line item at the adverse end is an independent measurement**, and
they should not be subtracted from one another as if they were.)*

**The rotor line rests on section drag at low Reynolds number.** It is a blade-element result for
blades whose sections run near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section
polars that are computed rather than measured, and section drag is hardest to predict in that range.
Section 12 shows how strongly the term depends on it.

**The hardware exposed by the vertical-phase layout is 69 percent of the zero-lift drag at the
favourable end and 57 percent at the adverse one.** The frames and the rotors they carry are the
majority of the aircraft's zero-lift drag in both cases, and the rotors alone are more than half
of it at the favourable end. **That is Bill 2 on this aircraft, in the terms Section 2 defined
it** — and the phrase is "exposed by the vertical-phase layout" rather than "dedicated lift group",
because Section 7 is precisely the claim that there is no dedicated lift group here.

**The tip-frame term is an attribution, not a marginal removal cost.** Section 8 gives the frames
four duties: landing gear, control moment arms, rotor support, and the fairing that is the
aircraft's only vertical surface. Their drag is charged to the hover-related hardware set because
that is the set the ledger is decomposing; **it is not a claim that this drag would disappear if
the vertical phase did**, since the landing and directional duties would still have to be met
somehow.

The same statement as a lift-to-drag ratio. **Removing all three non-clean-body terms — the hub
and small items, the tip frames and the free-wheeling rotors** — gives a clean-body ratio of
**20.55** at the favourable end and **15.24** at the adverse one, against the aircraft's **10.82**
and **8.79**. **The configuration retains 52.6 percent of its clean-body lift-to-drag ratio at the
favourable end and 57.7 percent at the adverse one**, so the non-clean-body terms remove 47.4 and
42.3 percent respectively, with the frames and rotors the large majority of what is removed.

**That ordering is the opposite of the one intuition offers, and the word that carries it has to
be exact.** Bill 2 has a **larger fractional burden where the clean-body drag is lower.** In
absolute counts it runs the other way — the frames and rotors are 0.0197 at the favourable end and
0.0216 at the adverse one — but the clean surface nearly doubles between the ends while that
charge moves by a tenth, so a near-constant charge is levied against a smaller total and takes a
larger share of it. **An architecture that improved its clean-body drag without touching its
exposed rotors would find this charge growing as a fraction, not shrinking.**

**This is a statement about position within the drag bracket at one scale.** Section 12 asks a
different question — how the same charge behaves as the aircraft changes size — and the two
answers are about different axes rather than in tension.

**One term inside Bill 2 is not separated, and it is not small in principle.** The build-up
computes each item on its own. **Rotor–structure and rotor–wing interference is not modelled
and is not carried as a line.** Section 2 quotes a wind-tunnel finding that a simulation
assuming negligible rotor–structure interaction *"always predicts higher lift and lower drag than
were experimentally observed"*; this build-up is such a calculation, and the bracket's upper margin
is the only provision made for it.

### The cruise-efficiency gap under fixed pitch

Section 10's closures run at a cruise propeller efficiency of 0.632 to 0.683, against the 0.80 the
published chain assumed. **Relative to that assumption the four fixed-blade closures are 14.6
percent lower at the better blade and 21.0 percent lower at the worse.**

**The ledger does not attribute the whole of that gap to the absence of variable pitch**, and the
distinction matters. What has been shown is that a blade meeting the hover figure of merit
delivers 0.632 to 0.683 in cruise, and that the published assumption was optimistic by that
margin. **No variable-pitch counterfactual was computed**, so nothing here establishes that a
variable-pitch hub would recover the whole difference to 0.80.

**Nor is the gap decomposed.** How much of it is blade twist, how much is section drag at the
cruise inflow angle, and how much is the operating point itself, this work does not say. Anything
finer would be a decomposition that was never performed.

### Bill 1 — carried mass, and what it is on this configuration

**There is no dedicated lift group to charge**, which is the architectural claim of Section 7
appearing as an absence in a ledger. What Bill 1 becomes here is the energy buffer: **3.6
percent of take-off mass, 1.9 to 2.1 kg across the four closures.**

**Section 3 said in advance that this would happen and refused to call it free.** The buffer is
not lift-subsystem mass, so it is not Bill 1 as Section 2 defines it — but it is mass carried
for the whole flight to serve a demand that lasts about two percent of it, which is the
complaint Bill 1 makes. **The architecture converts a power-system charge into a mass one.**
Whether that trade is favourable is what the closure tests, and the closure is where the answer
is: the engine it buys is 3.54 to 5.17 kW rather than one sized by a hover peak of 11.4 to
12.5 kW.

**The buffer fraction is an input to the loop, not a result of it**, and the closure does not
re-derive it from the hover energy the four corners actually need. Dimensionally a fixed fraction
is the right form: at constant disc loading the disc area grows with weight, so hover power is
linear in weight and hover energy with it. **But what the buffer supplies is the hover demand less
what the engine can deliver, and that deficit is not linear.** Taken at the electrical bus, where
the buffer sits — rotor shaft power divided by the machine and power-electronics efficiencies, less
the engine's shaft power times the generator's — it runs from 0.168 to 0.188 kW per kilogram of take-off mass across
the four closures, a spread of 12 percent, while the buffer fraction is held at 3.6 percent
throughout. **The corner that needs the most buffer per kilogram is given the
smallest buffer**, and that is a declared assumption of the closure rather than an outcome of it.

The rest of the empty-mass fraction, for completeness: airframe 0.300 and avionics 0.080 are
**construction constants held common across the three architectures** so that Section 13 compares
like with like — they are not results of this ledger — and propulsion runs 0.176 to 0.198.

### Bill 3 — released from the engine, and not from the electrical path

**This is the charge the architecture attacks most directly, and it is also the one where the
release is partial.**

The engine is sized by cruise: **3.54 to 5.17 kW** of shaft rating. The hover requirement is
**11.4 to 12.5 kW** at the rotor shaft. The ratio between the two is **2.4 to 3.2** — a ratio of
installed hardware, the factor by which the continuously installed power plant is smaller than the
peak the rotors must absorb. **It is not the buffer's burden**, which is taken at the electrical bus
rather than as the difference of these two shaft figures, and which Section 14 computes.

**But the full hover power passes through the electrical path, and that path is sized by it.**
Machines, power electronics and wiring between the buffer and the rotors carry 11.4 to 12.5 kW
whatever the engine is rated at. **Bill 3 is removed from the engine and left standing on the
electrical system**, and the propulsion mass fraction reflects it: of the 0.176 to 0.198 that
propulsion occupies, **0.108 is fixed and 0.068 to 0.090 scales with installed power.**

### What the closure does not contain at all

The items above are inside Section 10's numbers. **These are not**, and a reader should not
take the closure's convergence as covering them.

| Item | Status |
|---|---|
| **The cost of declining the reaction-torque channel** | Not computed. Thrust asymmetry, propulsive efficiency and the lag set by rotor inertia; quantifying it requires a control-allocation study rather than a torque figure. |
| **The transition altitude result** | 5.4 m in the finite-moment model at the reference geometry — **a result, not a charge**, and not a term in any sizing loop here. |
| **The strip's actuation** | Carried in the systems budget without sizing the mechanism. The number of actuators is not fixed by this study. |
| **The take-off margin** | Drawn from the tip pairs, because the nose pair is sized at thrust equal to weight. It competes with attitude authority and neither is closed against the other. |
| **Landing transition, vortex ring state, closed-loop hover control** | Not analysed. |
| **Engine installation — bay, intake, exhaust, cooling** | Absent from this work entirely. |
| **Rotor–structure and rotor–wing interference** | Inside Bill 2 in principle, absent from the build-up in practice. |

**The first and the last are the two that would most change the numbers above if they were
computed**, and neither is a small correction to a known quantity: one is a control problem the
study has not posed, and the other is a term the study's method is known to under-predict.

### What the ledger amounts to

**Three charges, three currencies, no total.** The non-clean-body drag terms remove 42.3 to 47.4
percent of the clean-body lift-to-drag ratio, and the hardware exposed by the vertical-phase
layout is the majority of the zero-lift drag. Bill 1 appears as a 3.6 percent buffer rather than a
lift group. Bill 3 is divided by 2.4 to 3.2 at the engine and is not divided at all on the
electrical path. **The cruise propeller efficiency sits 14.6 to 21.0 percent below the published
assumption under fixed pitch.**

**No charge on this page is a new one.** Every figure was already inside a quantity Section 10
reported, and this section's only work has been to say which part of which quantity it was.

**And every one of them belongs to one scale.** The four closures vary the drag uncertainty and
the blade-family choice at the reference size; **they do not establish how the three charges
behave as the aircraft changes size.** Section 12 asks whether they move together when the size
changes, and Section 13 asks what happens to the comparison when the sizing contract changes.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 59:** 0,168–0,188 kW/kg **kalkış kütlesi başına** (Adım 14'ün 4,7–5,2'si tampon kütlesi başına; 0,168/0,036 = 4,67) | Qwen; `aero/buffer-result.txt` |
| **Tur 58, P3:** defter düzeni fiyatlıyor; sayım bir kalem değil | Adım 9 bağımlılık tablosu; bu bölümün *"It attributes. It does not add."* |
| C_D0 dökümü: temiz yüzey, göbek, çerçeveler, rotorlar | `aero/drag_sweep.py` satır 41–48; `aero/ledger.py` |
| Askı donanımı C_D0'in %69'u (elverişli) / %57'si (olumsuz) | `aero/ledger-result.txt` |
| Temiz gövde L/D **20,55 / 15,24**; uçak 10,82 / 8,79; korunan %52,6 / %57,7 | `drag_sweep.zincir(cd0, pay=...)`; `ledger-result.txt` |
| **DÜZELTME, Tur 53 — Grok ve DeepSeek bağımsız olarak buldu.** `zincir()` olumsuz uçta marjsız çerçeve+rotor çıkarıyordu; az çıkarınca temiz gövde 14,29 görünüyordu, doğrusu 15,24. **Kapanışa etkisi YOK** — `carpan` bir orandır ve `LD_temiz × carpan = ld(toplam)` olarak sadeleşir; dört kapanış birebir aynı | `aero/drag_sweep.py:zincir` docstring; doğrulandı |
| Tampon bir **GİRDİ**; açık **bara tabanında** 0,168–0,188 kW/kg, yayılım %12; sabit %3,6 bunu izlemiyor (**Tur 56'da düzeltildi:** önceki 0,128–0,150 / %17 rotor milinden motor milini çıkarıyordu — v7'nin `thrust.py`'de düzelttiği istasyon karışıklığı) | `aero/ledger-result.txt` tampon denetimi (Grok sordu); `aero/buffer-result.txt` §1 |
| Gövde 0,300 ve aviyonik 0,080 **kuruluş sabiti**, defter sonucu değil | `baseline.py` `ORTAK`; üç mimaride de ortak |
| **Fatura 2 elverişli uçta DAHA AĞIR** — sabit rotor terimi küçülen toplamın daha büyük kesri | aynı çıktı; gerekçe dökümden doğrudan |
| Olumsuz uca **bütün döküme** %10 pay uygulanıyor | `drag_sweep.py` satır 48: `UST = (...) * 1.1` |
| Girişim modellenmedi; rüzgâr tüneli bulgusu | Adım 2, §2.3'ten: *"always predict higher lift and lower drag"* |
| η_p açığı %14,6 (0,683) ve %21,0 (0,632) | `aero/ledger-result.txt` |
| Açık kaynak başına **bölünmedi** | `nose_propeller_crossing.py` tek η veriyor, ayrışım yok |
| Tampon %3,6; 1,9–2,1 kg | `baseline.py` `f_tampon=0.036`; `ledger-result.txt` |
| Tamponun Fatura 1 karakteri taşıdığı **önceden** söylenmişti | Adım 3, izin verilen maliyetler, birinci madde |
| Gövde 0,300 · aviyonik 0,080 · tahrik 0,176–0,198 | `baseline.py` `ORTAK`; `ledger-result.txt` |
| Motor 3,54–5,17 kW; askı 11,4–12,5 kW; oran 2,4–3,2 | `aero/closure-result.txt` ve `ledger-result.txt` |
| Tahrik kesri: sabit 0,108 + güce bağlı 0,068–0,090 | `baseline.py` `F_TAHRIK_SABIT`; `ledger-result.txt` |
| Elektrik yolu askı gücüyle boyutlanıyor, motor değil | Adım 3, izin verilen maliyetler, ikinci madde |
| Kapanışta olmayanlar listesi | `paper/deferred-decisions.md` açık teknik kalemler |
| 5,4 m bir **sonuç**, bir kalem değil; referans geometride | Adım 10, geçiş bölümü |

**Bu sayfada BİLEREK olmayanlar:**

- **Hiçbir YENİ kalem.** Sayfanın tamamı Adım 10'un sayılarının içini söküyor. Grok ve
  DeepSeek'in şartı: *"Adım 10'un kapattığı bir kilogramı bile ekleme."*
- **Tek bir "mimarinin bedeli" sayısı.** Üç para birimi var; ağırlıklandırma dayanağı yok.
- **3,8× ve batarya paketi.** Adım 14'ün tek paragrafı (Grok'un şartı).
- **Hiçbir sıralama.** B ve C ile karşılaştırma Adım 13'ün işi.
