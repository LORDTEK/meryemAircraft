# Step 10 — Analytical closure of the sizing loop

**v8 taslağı, birinci yazım.** İskeletin 10. adımı. **İlk sayısal adım** — 1'den 9'a
kadar hiçbir sayfa bu uçağa ait bir kapanış vermedi.

**Kural denetimi:** başlık *"and where it fails"* içermiyor (ChatGPT, Tur 34 — o ifade
batarya açığını bu bölüme çeker; açıklar 14'te yaşar) · *"analytical"* fiziksel kapanışı
zaten reddediyor · **3,8× burada GEÇMİYOR** (Grok'un şartı: *"bir sayı, iki rol, tek
paragraf"* — 3,8× yalnız Adım 14'ün) · Qwen'in şartı: *elverişli sonuç, sonra kırılma*
yapısı **bölünmeden, tek yerde** duruyor · menzil iddiası yalnız çok rotorluya karşı.

**Girdi yuvası Tur 51'de denetlendi.** ChatGPT ve Grok bir çift sayım yakaladı; kod
doğruladı. `aero/closure_inputs.py` yuvayı kuruluş sınamasıyla sabitliyor, `aero/closure.py`
dört kapanışı çalıştırıyor.

---

## Analytical closure of the sizing loop

This section prices the arrangement of Sections 7 and 8 on a declared package; it does not bear on
the count of mechanism classes, which rests on the inventory of those sections alone.

**Closing a sizing loop mathematically is not the same thing as closing an aircraft
physically.** This section does the first. What it produces is a set of consistent numbers
on a declared set of assumptions: if the assumptions hold, these masses, powers and ranges
follow from one another without contradiction. Whether an aircraft can be built to them is a
different question, and Section 14 is where the answer is not yet yes.

### Why the loop has to be iterative

The pieces depend on each other in a circle. Installed power sets the mass of the propulsion
system; propulsion mass raises the take-off mass; take-off mass raises the power needed to
hover; and the hover power is what sizes the installed power. The closure statement is

> MTOW = m_payload / (1 − f_empty − f_energy)

and f_empty contains a term proportional to installed power, which contains a term
proportional to MTOW^1.5. **A fixed point is sought by iteration. If no fixed point exists, the
declared sizing package does not close** — which is a statement about that package rather than
about whether some other package could — and the calculation says so rather than returning a
number.

### The inputs, and why there are four closures rather than one

Two quantities entering the loop are not single values, and **they are not the same kind of
quantity**, which is why they are carried separately rather than merged.

**The zero-lift drag coefficient is uncertainty.** A consistent build-up places it between
**0.0285 and 0.0381**, with the same rotor term at both ends. A designer does not choose where
the real aircraft falls in that range.

**The blade family is a design variable this study has not fixed.** Four nose-blade families
meet the hover figure of merit, and their cruise propeller efficiencies span **0.632 to
0.683**. A designer would choose one; the criteria that would decide the choice — structural
loads, acoustics, the motor operating point, rotor inertia, manufacture — are not modelled
here, so the study carries all four rather than pretending to have chosen.

**The published zero-lift value of 0.0248 is not used.** The consistent build-up places it
below both ends of the bracket, so it is not a conservative choice or an optimistic one; it is
outside the supported range, and closing the loop on it would mean closing on a number this
work has shown it cannot support.

**Propeller efficiency enters the loop twice, and both entries move together.** It appears in
the range expression, and it appears in the cruise power that sizes the engine. Scaling one
without the other would size the engine on one propeller and compute the range on another, and
the loop would be internally inconsistent while appearing to close. Both terms are scaled
with the blade family in every closure reported here.

**The reference point is the aerodynamic lift-to-drag ratio, not the effective one.** The
effective ratio of Section 6 already contains the propeller efficiency; it is the currency in
which the multirotor comparison is made, and it is not an input to a loop whose own chain supplies
that efficiency separately.

**The sizing rules that keep that ratio valid as the mass moves are worth stating, because they
also say what the four closures are geometrically.** The loop holds **wing loading, disc loading
and aspect ratio** fixed, so area, span and disc diameter follow the mass: across the four
closures the wing area runs 2.07 to 2.27 m², the span 3.53 to 3.70 m, and the nose disc diameter
1.23 to 1.29 m. **The cruise lift coefficient is unchanged at 0.450 in every one of them**, so the
lift-to-drag ratio is an input that stays valid at the closed mass rather than one frozen at a mass
the loop has left behind.

**Three things the loop does not scale, and a reader comparing this section with Section 8 should
know which is which.** The tip-frame length, the tip-disc diameter and the strip are not sizing
variables here. They were set on the reference geometry — the 50 kg reference design of Section 8 — and **the control moment arms of Section 8 are therefore reference
values that this closure does not re-derive.** Section 8 describes one aeroplane; this section
describes what its sizing rules give at four sets of inputs. **These are the same configuration at
four closed masses rather than four configurations** — but anything that depends on the arms is
carried at the reference geometry and is not an output of the loop.

**The frame and rotor drag terms are carried the same way.** They are coefficients on the reference
wing area of 1.979 m², and holding them unchanged across the closures is the same as letting that
hardware grow with the wing. Held at its reference size instead, it would give terms 4 to 13 percent
smaller across the four closures — 0.0009 to 0.0028 of zero-lift drag. **The closures do not take that
reduction, and it has not been run through the loop.**

**The drag polar is likewise a fixed input, and it is worth saying what that costs.** Chord grows
with area, so the chord Reynolds number rises about **7 %** across the closure range. On a
turbulent-flat-plate scaling, C_D0 ∝ Re^−0.2, that is a **1.4 %** change in the zero-lift
coefficient — against a bracket whose two ends differ by **34 %**. The polar is therefore not
re-solved per closure. **The claim made above is that C_L is unchanged, not that C_D0 is exactly
so.**

### The construction is checked before it is used

At the published assumption — the published drag coefficient with the rotor term omitted, and
the published propeller efficiency — the construction returns a take-off mass of **49.4 kg**
against the published 50.1, a cruise lift-to-drag ratio of **11.88** against 11.88, and a range
of **1 585 km** against 1 583. **The largest deviation is 1.5 percent**, in mass. The
construction reproduces the published aircraft, so the same construction run on the bracket is
reporting a change of inputs rather than a change of method. **This check is the only place in
this section where the published drag coefficient appears**; every closure reported below uses the
bracket.

### The four closures

**All four converge.** On these assumptions the analytical sizing loop closes for this
architecture — and for the 50 kg design, which is the only one carried through this loop; the 1 000 kg reference design appears below only through a transition time computed elsewhere.

| | C_D0 | η_p | L/D | MTOW | Empty fraction | Hover power, rotor shaft | Engine rating, shaft | Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** | 0.0381 | 0.632 | 8.79 | 57.5 kg | 0.614 | 12.53 kW | 5.17 kW | 927 km |
| **B** | 0.0381 | 0.683 | 8.79 | 55.8 kg | 0.607 | 12.17 kW | 4.65 kW | 1 002 km |
| **C** | 0.0285 | 0.632 | 10.82 | 53.5 kg | 0.597 | 11.66 kW | 3.91 kW | 1 141 km |
| **D** | 0.0285 | 0.683 | 10.82 | 52.3 kg | 0.592 | 11.40 kW | 3.54 kW | 1 233 km |

**Payload is an input, fixed at 13 kg; take-off mass is the output.** The closure returns 52.3 to
57.5 kg, and the payload fraction that follows runs from **0.25 down to 0.23**.

**The spreads are not alike, and the difference is the useful part.** Across the four, the spread
— (max − min)/min, auditable from the table above — is **9.9 percent** in take-off mass and in hover
power, **33.0 percent** in range and **46.1 percent** in engine rating.

**Engine rating is the most sensitive output in this envelope and mass is the least, and the
ordering follows from where each input enters.** Cruise power is W·V/(L/D)/η, so it carries the
drag bracket and the blade family directly — **and W is itself a closure output that has already
absorbed them through the mass loop.** Range carries them directly but escapes the mass feedback,
because the fuel fraction is fixed. Mass feels them only through the propulsion fraction, which is
a minority of the empty mass. **Only the engine is charged twice**, and that is why 46.1 percent
exceeds 33.0, which exceeds 9.9. This is a sensitivity property of the declared envelope, not
evidence that engine sizing is intrinsically unstable.

### Which input matters, and one question the closure answers

**The drag bracket dominates the blade family, and the four percentages are worth printing rather
than one ratio.** Holding the blade and moving across the drag bracket changes the mass by
**6.9 %** and the range by **23.1 %**. Holding the drag and moving across the blade families
changes the mass by **2.9 %** and the range by **8.1 %**. The drag uncertainty therefore produces
about **2.8 times** the range variation of the blade-family choice and about **2.4 times** the
mass variation.

**The thing the study has not measured moves the answer more than the thing it has not chosen.**
That is a statement about which of the two open questions is more consequential to resolve, not
about the intrinsic importance of drag against blade design.

**And the blade that is best before the loop is still best after it.** There was no reason to
assume so: propeller efficiency propagates through cruise power into engine size, engine size
into mass, and mass back into hover power, and a loop can reverse a local ranking. It does not
here — at both ends of the drag bracket the higher-efficiency family closes to the longer
range. **That is a result of the closure rather than an assumption carried into it**, and it
is reported because the opposite outcome would have been reported too.

### The transition, and this is where the section turns

The sizing above says nothing about whether the aircraft can change regime. **The verdict comes
first so that it cannot be missed: the question is asked in two models, only the second of which
carries rotational dynamics, and that one does not support a zero altitude loss.** The first model
is shown anyway, because the mechanism it exposes is real and the reason the second model differs
is the point.

**The first model is kinematically favourable, and the zero-loss result is valid within it.** Treating the aircraft as a
two-degree-of-freedom point mass and driving the body angle kinematically from zero to ninety
degrees, the altitude lost during the rotation falls as the rotation is made slower — the
aircraft is supported through the manoeuvre rather than falling through it. **Entering the
rotation while already climbing removes the loss entirely**: at a 5 m s⁻¹ entry climb the
altitude loss is zero at both reference rotation times — **two seconds for the 50 kg reference design and 5.1 seconds for the 1 000 kg one** — and it stays zero at every thrust-to-weight ratio from 1.066
down to 1.00. *(Both times, and the thrust-to-weight figures with them, were established on the
reference geometry at its published mass. The closure above does not re-derive any of them, and
none of them is an output of it.)* Nothing in that result requires the tip pairs
to contribute lift once the climb is acquired.

**The second model removes the result, and this is the sharper of the two limitations.** The
point-mass model prescribes the attitude and therefore cannot charge for the trajectory the
aircraft flies while it is being rotated into that attitude. Solved instead with rotational
dynamics and a finite control moment — **and with the aerodynamic pitching moment set to
exactly zero, so that nothing favourable is borrowed** — the 50 kg reference design **loses 5.4 m at the
same reference condition where the point-mass model reports none.** *(That figure, like the
rotation times, belongs to the reference geometry at its published mass; the closure above does
not re-derive it either.)*

**The loss is not an artefact of the controller.** It is unchanged across linear, bang-bang and
smooth reference profiles; it appears without the control moment ever saturating; and it grows
rather than vanishes as the gains are raised, reaching 17 m at gains high enough to track the
reference almost exactly. **What the kinematic model leaves out is not the difficulty of turning
the aircraft but the trajectory the aircraft flies while it is being turned**, so tighter tracking
of a reference the rotational dynamics do not admit moves the aircraft further from the path it
can actually fly, not closer.

**So the zero-altitude-loss result is a property of the model that produced it.** What replaces
it is not a prediction: the aerodynamic pitching moment that would make it one is precisely the
quantity Section 14 reports as **not predicted reliably** — the moment exists; what is missing is
a method that predicts it. **For the methods used here, and for the published comparisons against
which they were checked**, the predictions diverge above roughly ten degrees of incidence, which
is the band the rotation passes through. With
a borrowed moment the outcome depends on which moment is borrowed, and the spread is wide
enough that **no number from it is reportable** — some models complete the rotation, some
saturate the tip pairs, and some tumble. **That spread is itself the finding.** What survives is
not a transferable transition figure but a result for the model that was tested: **within the
finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs
altitude.** Whether a real aircraft loses 5.4 m, more, or less is not settled by anything here.

### What closing does and does not establish

**It establishes that the architecture is arithmetically self-consistent on a declared
package**, at four corners of that package, with mass, power and range agreeing with one
another and with the construction that reproduces the published aircraft.

**It does not establish that the package exists.** The energy store this closure assumes is
the item Section 14 examines, and the examination does not end well. Nothing in this section
should be read as a claim that the aircraft is buildable; the claim is narrower and is the one
the section's title makes — the loop closes analytically, on assumptions that are stated and
that Section 14 tests.

**And these range figures are carried forward as the closed-loop values, not as a ranking.** No
multirotor is sized in this work, so no range comparison is made against one — Section 6 compares
the two families in cruise efficiency and says why it stops there. The comparison against the
other hybrid architectures depends on the sizing contract and belongs to Section 13, which is
where it is made.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 73:** birinci geçişten 10.2 (alan sabit tutulsaydı karşı-olgusu) ve 10.4 (nokta kütle modelinde optimize edilecek süre yok paragrafı) uygulandı — dört okuyucu + Claude. **10.1, 10.3, 10.5 vetolandı** (ChatGPT; 10.3'e Grok da) → kaynak kaldı. Hüküm cümlesi korunan listeye | Tur 72 metni §4 |
| **Tur 61:** yayılım tablosu tek cümleye indi (dört okuyucu + Claude hemfikir, A6); dört sayı aynen | `aero/closure-result.txt` YAYILIMLAR |
| **Tur 60:** üç ölçeklenmeyen şey (uç disk çapı eklendi); çerçeve+rotor katsayıları S_ref 1,979 m² üzerinde — sabit tutmak donanımı kanatla büyütmek demek; referans boyutta kalsa %4–13, 0,0009–0,0028 küçülürdü, kapanış almıyor; terim birliği | Grok; `aero/closure.py`, `closure-result.txt`; `aero/tip_propeller.py` S_REF; `verify.py` iki yeni kontrol |
| **Tur 59:** kapanış geometrisi 2,07–2,27 m², 3,53–3,70 m, 1,23–1,29 m — eski alt uçlar (1,98 / 3,45 / 1,20) **50 kg referans geometrisiydi**, kapanış değil | `aero/closure.py` GEOMETRI bloğu, `closure-result.txt`; `verify.py` Adım 10 geometri denetimi (eski alt ucu reddeder) |
| **Tur 58, P3:** bu bölüm düzeni fiyatlıyor; mekanizma sayımı yalnız envantere dayanıyor | Adım 9 bağımlılık tablosu; Adım 15 (*"It rests on the inventory of Sections 7 and 8"*) |
| MTOW = m_faydalı/(1 − f_boş − f_enerji); f_boş kurulu güce, güç MTOW^1.5'e bağlı | §2.12; `aero/baseline.py:boyutlandir`, satır 104–124 |
| Tutarlı braket 0,0285–0,0381, rotor terimi iki uçta da 0,0154 | `aero/drag_sweep.py` satır 41–48 ve docstring |
| Yayımlanan 0,0248 **iki ucun da altında** | aynı betik, *"IKI UCUN DA ALTINDA"* çıktı satırı |
| η_p = 0,632–0,683, dört palet ailesi | `aero/nose-propeller-crossing.txt` |
| η_p döngüye **iki kez** giriyor; ikisi birlikte ölçekleniyor | `baseline.py:111` (`eta_seyir`) ve `:126` (`eta_zincir`); `chain_resolve.gorev_ile` |
| L/D yuvasına aerodinamik oran girer, L/De değil | `aero/closure_inputs.py`, kuruluş sınamasıyla |
| **Kuruluş sınaması:** 49,4 kg / 11,88 / 1.585 km vs yayımlanan 50,1 / 11,88 / 1.583 | `aero/closure.py`, sapma %1,5 · %0,0 · %0,1 |
| **Dört kapanış tablosu** | `aero/closure-result.txt` |
| Yayılımlar: MTOW %9,9 · askı %9,9 · menzil %33,0 · motor %46,1 | aynı çıktı |
| Sürükleme braketi: MTOW %6,9, menzil %23,1; palet ailesi: %2,9 ve %8,1 | aynı çıktı |
| En iyi palet kapanıştan **sonra da** en iyi, iki sürükleme ucunda da | aynı çıktı |
| Faydalı yük 13 kg; pay 0,23–0,25 | `baseline.py` GOREV `m_faydali`; `closure-result.txt` |
| Nokta kütle, iki serbestlik, kinematik gövde açısı; yavaş dönüş **daha az** kaybettiriyor | **§3.15** *Transition time: slower is better*, satır 2198–2212 |
| 5 m/s tırmanışla irtifa kaybı **sıfır**; referans süreler **2 s hafif, 5,1 s ağır**; T/W 1,066'dan 1,00'e | §3.15, satır 2217–2221 |
| Moment 1/t_r², güç 1/t_r³; optimum yok | §3.15, satır 2208–2214 |
| Dönme dinamiği + sonlu moment + **sıfır** aerodinamik moment → **5,4 m** | §3.15, satır 2224–2228; ve **§4.7** satır 2823–2827 |
| Kayıp kontrolcü artefaktı değil; üç profilde de aynı, doymadan, kazanç artınca **büyüyor**, 17 m'ye çıkıyor | §3.15, satır 2229–2234 |
| Ödünç momentle sonuç dağılıyor: kimi tamamlıyor, kimi doyuyor, kimi takla atıyor | §3.15, satır 2236–2240 |
| *"No current method"* ifadesi **kullanılmadı** — Adım 6'da daraltılan ifadenin geniş hâli; kendi denetimimde yakalandı | §3.1 propagasyon kuralı; Adım 6 *"for the methods used here"* |

**Bu sayfada BİLEREK olmayanlar:**

- **3,8× ve batarya açığı.** Grok'un şartı: bir sayı, iki rol, tek paragraf. Kapanış adımı
  ilan edilmiş paketin kapandığını söyler; **o paketin var olmadığını Adım 14 söyler.**
- **Öteki hibritlere karşı hiçbir sıralama.** Adım 13'ün işi.
- **Sabit kanatlıya karşı hiçbir şey.**
- **Defter kalemleri** — sürükleme dökümü, kütle dökümü, serbest dönen rotorların bedeli:
  Adım 11.
