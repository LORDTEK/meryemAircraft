# Step 12 — Scale does not lock two of the charges together; the third is not tested

**v8 taslağı, üçüncü yazım (Tur 56).** Tur 55 yanıtları: Reynolds bulgusu **modelin içinde bir
ayrıştırma**, nedensel iddia değil (DeepSeek) ve *"in this polar"* bulgu cümlesinin içinde (Grok,
ChatGPT); *"the whole of the fall"* → *"18 percent above"* (DeepSeek); düşük Re belirsizliği **iki
yönlü** ve hafif terim 0,0154 **daha belirsiz olanı** — Adım 10–11 onu taşıyor (DeepSeek; Adım 11'e
çekince eklendi); aralığın uçları fiziksel sınır değil (DeepSeek); Fatura 1–3 **bağlaşık, özdeş değil**
(dördü de; DeepSeek'in "bağlaşım bir sonuçtur" önerisi ChatGPT/Grok'un "özdeşlik değil" sınırıyla
birlikte alındı); *"requires only two non-locked charges"* (ChatGPT). **Kendi bulgum:** Adım 2'nin
başlığı *"The charges behave as one quantity in three currencies"* idi — Adım 12'nin sonucuyla
doğrudan çelişiyordu; iskeletin *"üç bağlaşık fatura"* niyetine göre düzeltildi.

**İkinci yazım (Tur 55).** İskeletin 12. adımı: *"Üç para biriminin gerçekten üç
olduğunun, tek niceliğin üç adı olmadığının kanıtı."*

**Birinci yazım bu vaadi daraltmıştı** (tampon her iki ölçekte de girdi; üç faturadan yalnız
ikisi sınanabiliyor). **İkinci yazım daha büyük bir şeyi düzeltiyor: Fatura 2'nin ölçekle
düşüşünün MEKANİZMASI yanlıştı, ve yanlışlık bir hesap hatasından geliyordu.**

**Tur 55'te ne oldu, kim buldu:**

- **DeepSeek** *"ΔC_D0 ∝ σR²/(qS)"* formülünü sorguladı: sabit bir rotorda kuvvet q ile
  ölçeklenir, katsayı q'dan bağımsız olmalıdır. **Haklıydı.** Denetlerken `aero/heavy_rotor.py`'de
  **üç kurulum hatası** buldum — üçü de ağır hattın hafif hattın değerlerinde kalmasıydı:
  (1) `sifir_tork(c, th, V=V_SEYIR)` varsayılanı tanım anında 30 m/s'ye bağlanmış, denge 30 m/s'de
  çözülüp 40 m/s'nin q'suna bölünmüş; (2) `hover_tasarla` hafif rotorun 2100 rad/s tasarım devrini
  ağır rotora uygulamış — 0,67 m'de **703 m/s tasarım uç hızı**, palet askıda **uç Mach ≈ 1,0**'da;
  (3) göbek 0,015 m'de kalmış (%4,5 R). v7'nin *"dolgunluk düşer, q artar"* mekanizması **bu iki
  hatanın imzasıydı.** Düzeltilmiş hesap: terim **0,0045–0,0100** (hafifin 0,29–0,65'i), dinamik
  basınç **sadeleşiyor**, dolgunluk **artıyor** (0,075 → 0,100), ve düşüşün **tamamı Reynolds
  sayısından** (aynı Re'de ağır rotor hafifin 1,18 katı öder). `aero/heavy-rotor-result.txt`.
- **`paper/build/verify.py` bu hatayı yakalamıyor, YENİDEN ÜRETİYORDU** — aynı varsayılan
  argümanlarla çağırıp 0,0035–0,0074'ü "doğruluyordu." Düzeltildi; artık eski kurulumu reddettiği de
  sınanıyor (benim bulgum).
- **Grok** %5'lik askı/motor oranının motor tarafında *"ikinci bir kural"* taşıdığını söyledi.
  **Haklıydı ve durum daha kötü:** iki yayımlanmış tasarımın motor payı **aynı değil** (1,53 ve
  1,39). Bu `aero/baseline.py`'de **zaten kayıtlıydı** ve Adım 12'ye taşımamıştım — **benim
  ihmalim.** Eşit payla oran %14 değişir.
- **ChatGPT:** *"ayrışma"* değil *"kilitlenmeme"*; başlık; *"any ranking must"* fazla evrensel.
- **DeepSeek ve Qwen:** Fatura 1'i sabit özgül güçle türetmek mümkün. **Doğru, ama türetim Fatura 1'i
  Fatura 3'ün iki niceliğinin fonksiyonu yapıyor** — sınanan şey türetim olur, ayrışma değil.
  DeepSeek'in %1,6'sı **%2,3** olmalı (askı/kg değişimini atlamış).
- **Kendi bulgum:** Adım 12'nin birinci yazımı sabit hatve açığını *"refusing the variable-pitch hub
  costs"* diye göbeğe atfediyordu — **ChatGPT'nin Tur 53'te Adım 11'de yakaladığı aşırı atfın
  aynısı**, Adım 12'ye yayılmamıştı (§3.1). Adım 11'in dili getirildi.
- **Kendi bulgum:** İngilizce yeniden adlandırma commit'i (`d2c181c`) `rotation.py`, `roll.py`,
  `yaw.py` ve `cfd/plate/` altında üç betikte eski modül adlarını bırakmış; betikler **çalışmıyordu.**
  Tablo 15'in sayıları hiçbir betik çıktısında yok; onarılan `rotation.py`'den **%2 içinde** yeniden
  üretiliyor — gövdede yuvarlatıldı.

**Kural denetimi:** hiçbir ağır tasarım MENZİLİ verilmiyor · 3,8× GEÇMİYOR · iki uç **yayımlanmış
çift** (Adım 10 kapanışları değil) · *"harder case"* yalnız rotor terimi için · Adım 13'e
*"kütle faturası devrilir"* iddiası devredilmiyor (Grok).

---

## Scale does not lock two of the charges together; the third is not tested

Section 11 decomposed the three charges on one aircraft, at one size. **This section asks a
different question: are they three quantities, or one quantity under three names?** The test is
to change the size of the aircraft and see whether they move together. If they did, the framework
of Section 2 would be a single cost described three ways, and a ledger in three currencies would be
a ledger in one.

**The test is deliberately weak, and it is stated at its own strength.** It can show that two
charges are not locked together within this model. It cannot show that they are independent in
general, and it is not offered as doing so.

**This is a different axis from the one Section 11 examined.** There, Bill 2's share of the
zero-lift drag was compared at the two ends of the drag bracket, at a fixed size. Here the size
changes. The two answers are about different variables and do not bear on each other.

### What is compared, and why it is these two points

**Section 10 closed only the light design, at 52.3 to 57.5 kg. No closure was run at 1 000 kg**, and
none could be run on the same footing: the heavy design has neither a drag bracket nor a structural
closure (both below). A scale comparison therefore cannot be made from Section 10's closures. **It
is made between the two reference designs, 50 kg and 1 000 kg, sized by one method, and both ends are
taken from that pair.** Taking one end from Section 10 and the other from the reference pair would manufacture a scale
change that is really a propeller-efficiency update applied to one end only.

**The quantities used are ones Section 10 did not replace.** Disc loading is a sizing rule
Section 10 holds. The buffer fraction is an input to its loop. The free-wheeling rotor term is the
value Section 10 carries at both ends of its bracket at 50 kg, and it is computed here at 1 000 kg by
the same method. **The total zero-lift drag, the propeller efficiency, the range and the closed mass
are not used.** No heavy-design range is quoted: the figures available for it either omit the
free-wheeling rotor charge or carry an assumed rather than a computed propeller efficiency, and none
carries both.

**Two conditions travel with the heavy design.** It has no drag bracket; it stands on a single
zero-lift coefficient with no equivalent bound. And **its structural closure is undetermined**: shell
mass scales with wetted area while take-off mass scales with volume, so the structural fraction
depends on how areal density grows with size, and that exponent has not been measured. **The
comparison below uses powers, loadings and drag terms; it does not use the structure**, which is why
it can be made at all.

### Bill 3 — held nearly flat by a sizing rule, which is not a finding about Bill 3

**Disc loading is held at approximately the same value**: 44.2 kg m⁻² at 50 kg and 43.7 at
1 000 kg, one percent apart. At a given figure of merit, specific hover power depends only on disc
loading, so holding it holds hover power per unit weight — **0.218 kW kg⁻¹ at the light design and
0.216 at the heavy**, within one percent. Hover power rises from 10.9 kW to 216.2 kW, a factor of 19.8
against a mass factor of 20. **Hover power grows linearly with mass rather than as the L^3.5 of the
classical result.**

**That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3.**
What it establishes is narrower and still useful: the hover side of Bill 3 *can* be held flat across
a factor of twenty in mass by a single sizing choice.

**The measure Section 11 uses for Bill 3 — hover power divided by engine rating — carries a second
quantity, and it does not travel as cleanly.** The ratio is 4.19 at the light design and 3.98 at the
heavy, a change of 5 percent. But the engine is sized by cruise, not by disc loading, and **the two
reference designs do not use the same engine margin**: the engine is rated at 1.53 times cruise
electrical power at 50 kg and 1.39 times at 1 000 kg. With the light design's margin at both sizes the
heavy engine would be 60.0 kW and the ratio 3.61, a change of 14 percent. **The Bill 3 ratio therefore
moves by between 5 and 14 percent across the factor of twenty, depending on an engine margin the
sizing rule does not set.**

**The rule has a price, and it is paid in geometry.** Holding disc loading constant makes disc area
grow as L³ rather than L², so the nose propeller grows faster than the airframe. Wing loading rises
from 25.3 to 45.0 kg m⁻², span grows by a factor of 3.35 and the main propeller by 4.50, and **the
ratio of propeller diameter to span rises from 0.35 to 0.47.** The heavy design is not the light
design photographed from further away. **Much above 1 000 kg a single nose pair can no longer hold
the disc loading**, and a second would have to be added — which the architecture permits, since
every pair is torque-balanced on its own.

### Bill 2 — the rotor term falls, and in this model Reynolds number accounts for it

**Only the rotor term of Bill 2 is computed at both sizes.** The frame term enters both reference
designs as the same multiplier on clean lift-to-drag ratio, by construction, so it cannot show a scale
effect in either direction.

**The rotor term is computed by one method at both sizes**: the blade designed for its own hover
thrust at the same design tip speed, the hub at the same fraction of the radius, and the free-wheeling
state solved at each design's own cruise speed. At 50 kg it is **0.0154**. At 1 000 kg the blade
designed to the same section lift coefficient gives **0.0068 — 0.44 of the light value.** Across the
blade designs swept, design section lift coefficient 0.55 to 0.85, the heavy term runs from **0.0045
to 0.0100**, and every design in that range meets the heavy design's hover requirement with margin — a
figure of merit of 0.75 to 0.77 against the 0.599 required. At 50 kg the hover requirement selects the
blade; at 1 000 kg nothing selects within the interval, and its ends are the ends of the swept blade
family, not a physical bound. **At every point in it, and in the section polars used here, the heavy
charge is between 0.29 and 0.65 of the light one** — a direction that is the ordinary one and a factor
that is not a measurement, for the reason given below.

**The mechanism is not the obvious one, and it is not the one a dimensional argument suggests.**
Three candidates can be excluded directly:

- **Geometry.** The eight tip discs total 0.251 m² against 1.98 m² of wing at 50 kg, and 2.82 m²
  against 22.24 m² at 1 000 kg — **a disc-to-wing area ratio of 0.127 at both sizes.** The wing does
  not outgrow the discs.
- **Dynamic pressure.** A rotor turning freely at zero shaft torque settles at a rotational speed
  proportional to the flight speed, so its axial force scales with dynamic pressure and a coefficient
  referenced to that pressure does not. Solving the heavy blade's free-wheeling state at 30 and at
  40 m s⁻¹ confirms it: the coefficient changes by **9 percent** — itself a Reynolds-number effect —
  not by the 44 percent a dynamic-pressure scaling would give.
- **Solidity.** The heavy blade is not thinner; it is fuller — **0.100 against 0.075** for blades
  designed to the same section lift coefficient.

**Within the blade-element and section-polar model, the section Reynolds number accounts for the
fall.** In the free-wheeling state the median blade-section Reynolds number rises from about 8 × 10⁴
at 50 kg to 5.6 × 10⁵ at 1 000 kg, a factor of 6.8, because the chords are longer and the flight speed
higher. **Evaluating the heavy blade with its section Reynolds number scaled down to the light rotor's
returns 0.0181 — 18 percent above the light charge.** At equal Reynolds number the fuller heavy blade
would pay more, not less. Reynolds number is not an independent variable — it follows from the chord
and the speed each rotor has — so this is a decomposition inside the model rather than a causal claim
beyond it: for the chords and speeds these two designs have, the fall is what lower section drag at a
higher Reynolds number gives.

**That places a condition on the result, and it runs both ways.** The fall rests on how section drag
changes between 8 × 10⁴ and 5.6 × 10⁵, which is taken from the section polars used for every rotor in
this work rather than measured, and the light end lies below a Reynolds number of 10⁵, where section
drag is hardest to predict. **The direction — lower section drag at higher Reynolds number — is the
ordinary one; the size of the fall is as good as the section model at the low end.** If the light
blade's real section drag is higher than the polars give, the light charge is larger and the fall is
larger; if it is lower, the fall is smaller — the heavy end, at the higher Reynolds number, being the
better predicted of the two. **Of the two rotor terms, the light one is therefore the
less certain — and it is the one Sections 10 and 11 carry.**

**The result does not touch the structural question.** It comes from blade-element solutions on two
sized rotors at their own conditions; it would remain a result even if the heavy airframe were shown
not to close. **For the rotor term, the light design is the harder case.** That statement is not
extended to Bill 2 as a whole, because the frame term is not computed at the heavy design and the
heavy design has no drag bracket.

### Bill 1 — not tested, and the one available derivation would not test it

**On this configuration Bill 1 appears as the energy buffer**, as Section 11 set out, since there is
no dedicated lift group to charge. The buffer is 3.6 percent of take-off mass at 50 kg and 4.0
percent at 1 000 kg.

**Both of those figures are inputs.** Neither is derived from the hover energy the aircraft needs;
each was chosen for its design point and carried into the sizing. **A change from 3.6 to 4.0 percent
is a change between two choices, not a scaling result**, and it cannot be offered as evidence that
Bill 1 moves with size in either direction.

**A derivation is available without settling what specific power a store can deliver, and it is
stated here because it shows why it is not used.** If the buffer is sized to supply the hover deficit
— hover power less engine rating — at a specific power that is the same at both sizes, its mass
fraction follows the deficit per kilogram: 0.166 kW kg⁻¹ at 50 kg and 0.162 at 1 000 kg, a fall of
about 2 percent. **But that derivation makes the buffer a function of the hover power and the engine
rating, which are the two quantities that measure Bill 3.** A buffer derived that way is locked to
Bill 3 by the derivation itself, and comparing the two across scale would test the derivation, not
whether they are separate. Sizing the buffer by energy instead adds a hover duration, which is a
mission choice, and changes nothing in that argument.

**No quantity computed in this work gives a buffer requirement at scale that is independent of the
hover and engine powers and of an assumed specific power or energy.** On this aircraft Bill 1 takes
the form of the device that releases Bill 3 from the engine, as Section 3 anticipated, and **whether
the two are separable here is not established.**

**What is established is that they are coupled here, and that is Section 3's claim rather than a
defect found in it.** The buffer is the conversion the fourth part of the escape condition permits:
kilowatts of hover peak paid in kilograms of store. **Coupling is not identity.** The buffer is
measured in kilograms and the engine in kilowatts, linked by a specific power that is itself an
assumption; and the coupling belongs to an aircraft that meets the escape condition, not to the
framework — a lift-plus-cruise aircraft pays a lift group whose mass is not a function of its cruise
engine.

**Nor is the structural mass a substitute.** The shell-mass exponent governs how the airframe
fraction scales, and it is unmeasured; but the airframe is not Bill 1 as Section 2 defines it — it
is the structure every architecture carries — and treating it as the mass bill would change the
definition to fit the test. What specific power a store of the required mass must deliver is the
item Section 14 examines and does not resolve.

### What the comparison establishes

**Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its
light-design value in the section polars used here, while specific hover power changes by one percent
and the Bill 3 ratio by 5 to 14 percent.** The flatness of Bill 3 is imposed by a sizing rule; the finding is that Bill 2 moved anyway,
by more than the Bill 3 ratio at every point in the heavy interval and under either engine margin.
**Within this model, the two are therefore not one quantity under two names.**

**Bill 1 is not tested**, for the reason given above, and nothing here should be read as showing
that it separates from the other two — or as showing that it does not.

**And the evidence is one pair of design points, computed by one method, with the Bill 2 result
resting on a section-drag model at low Reynolds number.** It is consistent with the separability
Section 2 asserts; it is not a verification of separability as a general property, which a single
instantiation cannot supply.

### Two costs that scale does not relieve

Neither is one of the three charges, and both are reported because a section about what scale does
to this aircraft would be incomplete without them.

**The cruise-efficiency gap under fixed pitch does not close with size; it widens slightly.**
Computed at each reference design's cruise thrust, a nose-pair blade that meets the hover requirement
delivers a cruise efficiency 14.6 to 21.0 percent below the 0.80 assumed at the light design and
**16.4 to 22.9 percent below it at the heavy one.** As in Section 11, no variable-pitch counterfactual
was computed, so this is not a measure of what refusing the hub costs; it is a measure of what a fixed
blade that hovers delivers in cruise, and that does not improve with size.

**The transition is where the square–cube relation is paid in full.** The moment needed to rotate
the aircraft follows M = Iα with I ∝ mL², so the moment required for a fixed rotation time grows
much faster than the aircraft. **Rotating the heavy design in the light design's two seconds would
demand about 220 kW from the tip propellers — roughly the whole of hover power**, which is not
available. At 5.1 seconds, the heavy design's rotation time, the demand falls to about 13 kW, 6
percent of hover power. **A larger aircraft of this type turns more slowly, and must.** Hover power
escapes the classical scaling objection by fixing disc loading; the rotation does not escape it.

### Why this section sits between the ledger and the contracts

**The next section needs only what this one shows.** If the three charges were one quantity, a single
number could rank architectures whatever weight each charge was given. **Because at least two of them
are not locked together, a comparison of architectures cannot in general be reduced to a number that
does not depend on how the charges are weighed: where one architecture pays less of one charge and
more of another, the ranking depends on the weighting.** The argument requires only two charges that
are not locked together; the third need not be shown separate for the conclusion to hold. A third
shown to be separate would strengthen it; a third shown to be locked to one of the others would
leave it standing.

Section 13 examines what the choice of sizing contract does to a ranking, on the light closures of
Section 10 only.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| Adım 10 yalnız hafif tasarımı kapattı, 52,3–57,5 kg; 1000 kg'da kapanış yok | `aero/closure-result.txt`; Adım 10 satır 109–111 |
| Disk yüklemesi 44,2 / 43,7 kg/m², %1,1 fark | v7 §3.9 satır 1768; §3.8 Tablo 13 |
| Askı gücü 10,9 → 216,2 kW, ×19,8 vs kütle ×20 | v7 §3.9 satır 1769–1771 |
| Özgül askı gücü 0,218 / 0,216 kW/kg, fark %0,6 | hesaplandı: 10,9/50,1 ve 216,2/1000 |
| Askı/motor oranı 4,19 / 3,98, değişim %5 | hesaplandı: 10,9/2,6 ve 216,2/54,3 (v7 Tablo, satır 1619 ve 1683) |
| **Motor payı 1,53 / 1,39** — iki tasarımda farklı | 2,6/1,7 ve 54,3/39,2 (v7 satır 1618–1619, 1682–1683); `aero/baseline.py` satır 447–461 (zaten kayıtlıydı) |
| Eşit payla ağır motor 60,0 kW, oran 3,61, değişim %14 | hesaplandı: 39,2 × 2,6/1,7 = 59,95; 216,2/59,95 |
| Kanat yüklemesi 25,3 → 45,0; açıklık ×3,35, pervane ×4,50; pervane/açıklık 0,35 → 0,47 | v7 §3.9 satır 1824–1827; `verify.py` ölçek blokları |
| 1000 kg'ın üstünde ikinci çift gerekir | v7 §3.9 satır 1830–1831 |
| Çerçeve terimi iki referans tasarımda aynı çarpan (1/1,12) — inşa gereği | `aero/baseline.py` satır 165 ve 463–464 (`LD_temiz = 13,6 × 1,12`); v7 satır 1421–1422 (*"1/1.12 … covering the tip frames alone"*) |
| **Hafif rotor terimi 0,0154, c_l 0,68, dolgunluk 0,0754** | `aero/tip_propeller.py` (bu tur yeniden koşuldu: 0,01535; c_l 0,70'te FM 0,350 — seçimi askı şartı yapıyor) |
| **Ağır rotor terimi 0,0068 (c_l 0,68), aralık 0,0045–0,0100, oran 0,29–0,65** | `aero/heavy-rotor-result.txt` (düzeltilmiş kurulum) |
| Ağır FM 0,75–0,77, askı uç Mach 0,65–0,67 | aynı |
| Disk/kanat alanı 0,127 iki ölçekte de | v7 §3.9 satır 1783–1785 |
| **q deneyi: aynı ağır palet 30 → 40 m/s'de katsayı −%9, q ölçeklemesi −%44 verirdi** | `aero/heavy-rotor-result.txt`, MEKANİZMA bloğu: 0,00748 → 0,00681 |
| **Dolgunluk 0,075 → 0,100 (artıyor)** | aynı; ×1,33 |
| **Medyan kesit Re 8,2×10⁴ → 5,6×10⁵ (×6,8); hafif Re'de ağır palet 0,0181 = hafifin 1,18 katı** | aynı, Re deneyi |
| Kesit kutupları NeuralFoil, NACA 0012 — ölçülmedi | `aero/tip_propeller.py` `kesit_kuvvet`, satır 57 ve 80–85 |
| Düşük Re belirsizliği iki yönlü: hafif terim eşit-Re deneyinde Re ile monoton (düşük Re → büyük terim) | `heavy-rotor-result.txt`: 0,0068 (Re 5,6×10⁵) → 0,0181 (hafif Re'ye indirilmiş) |
| Ağır tasarımın sürükleme braketi yok | v7 §3.8 satır 1750–1754 |
| Ağır yapısal kapanış belirlenmemiş; kabuk üssü ölçülmedi | v7 §3.8 satır 1690–1698 |
| Tampon %3,6 ve %4,0 İKİSİ DE GİRDİ | `aero/mass.py` `m_pil` parametresi; `baseline.py` `f_tampon`; türeten kod yok |
| Açık/kg 0,166 → 0,162, düşüş %2,3 (yayımlanmış paylarla) | hesaplandı: (10,9−2,6)/50,1 ve (216,2−54,3)/1000 |
| Tampon "Fatura 3'ü motordan kurtaran aygıt" — Adım 3 önceden söyledi | Adım 3 satır 73–79; Adım 11 satır 129–132 |
| Sabit hatve açığı hafif %14,6–21,0, ağır %16,4–22,9 (**birinci yazımda 23,0 idi; betik 22,9 veriyor** — 1 − 0,616/0,80 yuvarlanmış η'dan) — **her ikisi yayımlanmış seyir itkisinde** (L/D 12,0 ve 13,6) | `aero/nose-propeller-crossing.txt`, `aero/nose-propeller-heavy.txt`; `nose_propeller.py` satır 156, `nose_propeller_heavy.py` satır 24 |
| **Geçiş: 2 s → ~220 kW (~%100); 5,1 s → ~13 kW (%6)** — v7 Tablo 15 (221,5 / 13,4) **hiçbir betik çıktısında yok**; onarılan `rotation.py`: 5,1 s'de üçgen profil 127,0 N/çift → 4 çift × 6486 W × (127,0/200,1)^1,5 = **13,1 kW**; ×(5,1/2)³ → **217,6 kW (%101)**. Tablo %2 içinde tutuyor; gövdede yuvarlatıldı | v7 satır 1842–1849; `aero/rotation.py` (bu tur onarıldı) |

**Bu sayfada BİLEREK olmayanlar:**

- **Hiçbir ağır tasarım menzili.** Elimizdeki her biri kısmi: 1.814 km (rotor yüklenmemiş, η_p 0,80),
  1.571 km (rotor yüklenmiş — **ama hatalı 0,0051 ile**, η_p 0,80), 1.398–1.517 km (η_p yeniden
  çözülmüş, rotor yüklenmemiş). Doğru rotor terimi ile hesaplanan η_p'yi birlikte taşıyan kapanış yok.
- **`ΔC_D0 ∝ σR²/(qS)` formülü ve üç haneli uyum.** Mekanizma yanlıştı; formül gövdeden çıktı.
  Gövde **"önceki sürüm"** anlatısı taşımıyor (CLAUDE.md §4); doğru mekanizma şimdiki zamanda yazıldı.
- **3,8× ve batarya özgül gücü.** Adım 14.
- **Kabuk kütlesi Fatura 1 olarak.** Tanımı sınava uydurmak olur.
- **"Fatura 2 fiziksel, Fatura 3 sözleşmesel" çerçevesi (DeepSeek).** Reddedildi: Fatura 2'nin terimi
  de tasarım seçimlerine bağlı (palet tasarımı, seyir hızı; şimdi Reynolds sayısı, yani veter ve hız).
- **Adım 13'e "kütle faturası devrilir" devri.** Grok: 13'ün sözleşmeleri yakıt kesri, yakıt kütlesi,
  kalkış kütlesi tartar; bunlar Fatura 2'ye karşı Fatura 3 değildir. Devir cümlesi yalnız
  *"ağırlık seçimine bağlı"* diyor.
