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
the closed numbers, and how large it is there.**

### What this section does, and the one thing it must not do

**It attributes. It does not add.** Every cost named below is already inside the closure of
Section 10 — in the drag bracket, in the propeller efficiency, in the empty-mass fraction, in
the engine rating. **Adding any of them again would be double counting**, and the numbers that
follow are decompositions of quantities already reported rather than new charges on top of them.

**Two kinds of item appear, and the difference is stated rather than smoothed over.** Some
costs were computed per source and can be split: the drag build-up has named terms, and the
mass fractions were solved separately. Others are inside a single computed quantity and **the
study did not separate them**; saying otherwise would invent a decomposition that was never
performed. Each is marked.

**And there is no single figure for what the architecture costs.** The three charges are in
three different currencies — kilograms, drag counts, installed kilowatts — and a reader who
wants one number would have to be given a weighting this work has no basis for choosing. **The
ledger reports three quantities and refuses to collapse them.**

### Bill 2 — the drag of hover hardware, inside the bracket

The zero-lift drag coefficient of Section 10 is a build-up with named terms. Splitting it:

| | favourable end | adverse end |
|---|---:|---:|
| Clean wetted surface | 0.0073 | 0.0142 |
| Hub and small items | 0.0015 | 0.0022 |
| **Tip frames** | **0.0043** | **0.0047** |
| **Attitude rotors, free-wheeling** | **0.0154** | **0.0169** |
| Total | 0.0285 | 0.0381 |

*(The adverse end carries a ten percent margin applied to the whole build-up, which is why
every term differs between the columns.)*

**The hover hardware is 69 percent of the zero-lift drag at the favourable end and 57 percent
at the adverse one.** The frames and the rotors they carry are the majority of the aircraft's
zero-lift drag in both cases, and the rotors alone are more than half of it at the favourable
end. **That is Bill 2 on this aircraft, in the terms Section 2 defined it.**

The same statement as a lift-to-drag ratio: removing the frames and the rotors gives a
clean-body ratio of **20.55** at the favourable end and **14.29** at the adverse one, against
the aircraft's **10.82** and **8.79**. **The configuration retains 53 percent of its clean-body
lift-to-drag ratio at the favourable end and 62 percent at the adverse one.**

**That ordering is the opposite of the one intuition offers, and it is worth stating plainly.**
Bill 2 is *heavier* where the rest of the aircraft is cleaner. The rotor term barely moves
between the two ends, while the clean surface nearly doubles; so at the favourable end a
near-constant charge is levied against a smaller total, and it takes a larger share. **An
architecture that improved its clean-body drag without touching its exposed rotors would find
this charge growing as a fraction, not shrinking.**

**One term inside Bill 2 is not separated, and it is not small in principle.** The build-up
computes each item on its own. **Rotor–structure and rotor–wing interference is not modelled
and is not carried as a line.** Section 2 quotes a wind-tunnel finding that a simulation
assuming negligible rotor–structure interaction *"always predicts higher lift and lower drag than
were experimentally observed"*; this build-up is such a calculation, and the bracket's upper margin
is the only provision made for it.

### The price of fixed pitch, inside the propeller efficiency

Section 10's closures run at a cruise propeller efficiency of 0.632 to 0.683, against the 0.80
the published chain assumed. **That gap — 14.6 percent at the better blade and 21.0 percent at
the worse — is the price of refusing the variable-pitch hub**, paid by one blade geometry
serving a hovering condition and a cruising one.

**It is not decomposed, and it should not be read as though it were.** How much of the gap is
blade twist, how much is section drag at the cruise inflow angle, and how much is the operating
point itself, this work does not say. **The statement the ledger can make is that the computed
efficiency is what a blade meeting the hover figure of merit delivers in cruise, and that the
published assumption was optimistic by that margin.** Anything finer would be a decomposition
that was never performed.

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

The rest of the empty-mass fraction, for completeness, is airframe 0.300 and avionics 0.080,
both held common across architectures by Section 10's construction, and propulsion 0.176 to
0.198.

### Bill 3 — released from the engine, and not from the electrical path

**This is the charge the architecture attacks most directly, and it is also the one where the
release is partial.**

The engine is sized by cruise: **3.54 to 5.17 kW**. The hover requirement is **11.4 to
12.5 kW**. The buffer supplies the difference for the vertical phase, and the ratio between the
two is **2.4 to 3.2** — that is the factor by which the continuously installed power plant is
smaller than the peak the aircraft must produce.

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

**Three charges, three currencies, no total.** Bill 2 takes 38 to 47 percent of the clean-body
lift-to-drag ratio and is the majority of the zero-lift drag. Bill 1 appears as a 3.6 percent
buffer rather than a lift group. Bill 3 is divided by 2.4 to 3.2 at the engine and is not
divided at all on the electrical path. **Refusing the variable-pitch hub costs 14.6 to 21.0
percent of cruise propeller efficiency.**

**None of those numbers is new here.** Every one was already inside a quantity Section 10
reported, and this section's only work has been to say which part of which quantity it was.
Section 12 asks whether the three separate with scale, and Section 13 asks what happens to the
comparison when the sizing contract changes.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| C_D0 dökümü: temiz yüzey, göbek, çerçeveler, rotorlar | `aero/drag_sweep.py` satır 41–48; `aero/ledger.py` |
| Askı donanımı C_D0'in %69'u (elverişli) / %57'si (olumsuz) | `aero/ledger-result.txt` |
| Temiz gövde L/D 20,55 / 14,29; uçak 10,82 / 8,79; korunan %53 / %62 | `drag_sweep.zincir()`; aynı çıktı |
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
