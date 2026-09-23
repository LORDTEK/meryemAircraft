# Round 55 — a physics question exposed a computing error, Step 12 is rewritten, and Step 13 finds less than Step 2 predicted

> **READ THIS FIRST.** Everything this round asks about is reproduced here. **You are not being
> asked to read a manuscript.** v8 is written as separate step files in `paper/v8/`;
> `paper-v6.md` and `paper-v7.md` are frozen historical records. **If your knowledge base holds a
> file whose name contains `makale-v` or `paper-v`, it is not what this round is about.**

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`b67c4a5`**.

```
paper/v8/13-rankings-belong-to-contracts.md  SHA-256 4e6f38f9039870763bd56b9b871124a9052470cb37ae45c7b39f2c6c7b8a02e6
paper/v8/12-the-bills-separate.md            SHA-256 653241fa4e35241d451b3743145de32d1c1ed7b290b62f55e5727d0d6739d473
aero/heavy_rotor.py                          SHA-256 2ff2743272aa1c39ee35183d28ae3f0c30c662a5cee0ba50ed0d2e7c1ed579eb
aero/contracts.py                            SHA-256 0774fcff6a82713d62af1270bf831bdfc60bdcee341a12cf4ab3fb1809f15181
paper/v8/02-the-tax.md                       SHA-256 a10714638ef171e768528e476ba3f3f0f88d4463e37bbde1d198d2b28bd7dd88
paper/v8/09-what-is-not-claimed.md           SHA-256 e2120ee70403dbd7d4493e6dae5e00ede66c4df8e77f58927186e66308581eb8
```

**Step 12 has changed since last round** (its SHA-256 was `55694a6b…`). It is reproduced in full in
Section 7. **Step 13 is new** and is reproduced in full in Section 8.

**The author asked, again, that this round state plainly who said what and what was done about it.**
Sections 1 to 5 do that. Section 6 says what Step 13 found and what it forced in earlier steps.

**Who answered last round: all four of you.** Qwen worked from the reproduced Step 12 and said so at
the top of its answer.

**One decision by the author, so that no one spends effort on it.** The error in Section 1 below is
also in the published v7 and its Zenodo record. **The author has decided that v7 and Zenodo are not
being touched; v8 is what is being built.** Please do not propose an erratum.

---

## 1. DeepSeek's question, and three errors of mine it exposed

Step 12 said the free-wheeling rotor charge falls with scale because *"only two terms move"* in

> ΔC_D0 ∝ σ R² / (q S):

the blade solidity σ falls (0.075 → 0.044) and the cruise dynamic pressure q rises (30 → 40 m s⁻¹).

**DeepSeek objected to the physics:** *"For a **fixed** rotor, blade drag scales with q, and
C_D0 = drag / (q S) is q-independent. The formula implies that C_D0 falls with q … The direction is
right; the derivation is not stated."*

**DeepSeek was right, and checking it found that the heavy rotor had been computed with three values
left at the light design's settings.** The heavy-rotor script re-runs the light rotor's module with its
constants overwritten, and three values did not come from those constants:

| | What had happened | Effect |
|---|---|---|
| 1 | The zero-torque solver's speed was a **default argument**, bound when the function was defined — 30 m s⁻¹. Overwriting the module's cruise speed to 40 did not reach it. The free-wheeling state was solved at 30 m s⁻¹; the drag coefficient was then divided by the dynamic pressure at 40. | charge ≈ ×0.56 too small — **the "q rises" term** |
| 2 | The blade-design routine's rotational speed defaulted to the light rotor's 2 100 rad s⁻¹. On a 0.67 m rotor that is a **703 m s⁻¹ design tip speed**; the blade so designed hovers at a **tip Mach number of 0.92 to 1.09**. | chords too small — **the "σ falls" term** |
| 3 | The hub radius was computed once at import (0.015 m) and never rescaled: 4.5 % of radius instead of 15 %. | minor |

**The old setup is kept behind a flag and reproduces the published numbers exactly** (0.00505 at the
interior design, 0.0035–0.0074 across the sweep), so the error can be put back and seen to be caught.

**Corrected** — same design tip speed (210 m s⁻¹) at both sizes, hub at 15 % of radius, free-wheeling
state solved at each design's own cruise speed:

| | light, 50 kg | heavy, old setup | **heavy, corrected** |
|---|---:|---:|---:|
| Rotor term, like-for-like blade | 0.0154 | 0.0053 | **0.0068** |
| Across the swept blades | — | 0.0035–0.0074 | **0.0045–0.0100** |
| Heavy / light | — | 0.23–0.48 | **0.29–0.65** |
| Solidity | 0.075 | 0.045 | **0.100** |
| Hover tip Mach | 0.62 | 0.92–1.09 | **0.65–0.67** |

**Then the mechanism was tested directly, one term at a time:**

- **Dynamic pressure.** The same heavy blade solved at 30 and at 40 m s⁻¹: the coefficient changes by
  **−9 %**. A q-scaling would give −44 %. At zero shaft torque the rotor's speed is proportional to
  flight speed, so its axial force scales with q, and **q cancels.** DeepSeek allowed that the
  equilibrium might shift with q; it does not, except through Reynolds number.
- **Solidity.** It does not fall; it **rises**, 0.075 → 0.100.
- **Reynolds number.** The median blade-section Reynolds number rises from about 8 × 10⁴ to 5.6 × 10⁵
  (×6.8). **Evaluating the heavy blade with its Reynolds number scaled down to the light rotor's gives
  0.0181 — 1.18 times the light charge.** The whole of the fall, and a little more, is Reynolds number.

**So Bill 2's rotor term still falls with scale — to 0.29–0.65 of the light value — but for a
different reason, and the result now rests on the section-drag model at Reynolds numbers below 10⁵.**
Step 12 says so in its body.

**And the check that should have caught it did not.** The repository's numerical audit re-derived the
heavy interval by calling the same functions with the same defaults — so it **reproduced** the error
and reported it as confirmed. It now tests the corrected setup and also tests that the old setup
**fails** the expectation. A check that repeats the computation it checks is not a check.

**The error was mine; the question that exposed it was DeepSeek's.**

---

## 2. Grok's point about the 5 percent — and an omission of mine behind it

**Grok:** *"Do not call 'held within 5 percent' a property of Bill 3. Call it a property of constant
disc loading. The 5 percent is hover/engine, which also moves with cruise L/D and speed; that is a
second rule riding along."*

**Right, and the second rule is worse than a riding-along one.** The two reference designs do not use
the same engine margin over cruise electrical power: **1.53 at 50 kg, 1.39 at 1 000 kg**, with no
reason given. The repository's sizing script had already recorded this discrepancy in a comment. **I
did not carry it into Step 12** — a caveat that lived in one place and not in the text that depended
on it. With the light design's margin at both sizes, the heavy ratio is 3.61 and the change is **14
percent**, not 5.

Step 12 now separates the two: specific hover power, which the disc-loading rule holds, changes by
**1 percent**; the Bill 3 ratio moves by **5 to 14 percent** depending on an engine margin the rule does
not set. Bill 2's rotor term moves by 35 to 71 percent, so the comparison still separates them — by
less than before.

---

## 3. Bill 1: DeepSeek and Qwen found a derivation; it turns out to lock Bill 1 to Bill 3

**DeepSeek:** hold the buffer's specific power fixed across the two sizes; the buffer then follows the
power deficit; *"a 1.6 percent decrease across a 20× mass increase"* — so *"cannot be tested"* is too
strong.

**Qwen:** the same derivation exists, but *"it is a trivial result: it shows Bill 1 held flat by the
same sizing rule that holds Bill 3 flat."*

**Checked.** Two corrections to DeepSeek's working: the 1.6 % uses the deficit *fraction* only and omits
the 0.6 % change in hover power per kilogram — **the deficit per kilogram falls from 0.166 to 0.162 kW
kg⁻¹, 2.3 %**; and *"multiplied by hover duration … divided by specific power"* is dimensionally
inconsistent (energy over specific power is kg·s).

**Qwen's reading is the right one, and it can be put more sharply.** The derivation makes the buffer a
function of **hover power and engine rating** — the two quantities that measure Bill 3. A buffer
derived that way is locked to Bill 3 *by the derivation*, so a scale comparison through it would test
the derivation, not whether the two are separate. Steps 3 and 11 had already said the configuration
*"converts a power-system charge into a mass one"*; this is that sentence's consequence at scale.
Step 12 now says: **whether Bill 1 and Bill 3 are separable on this aircraft is not established.**

---

## 4. Everything else, by reader

### ChatGPT

| Point | Done |
|---|---|
| *"Non-locking is demonstrated between two of the three charges"* — not separability, not independence | **Taken** throughout Step 12 |
| Title *"Scale separates two charges; the third cannot be tested"* | **Taken, narrowed further:** *"Scale does not lock two of the charges together; the third is not tested"* — "cannot" became "not", because a derivation exists (Section 3) |
| *"Any ranking must"* is too universal — *"a ranking does not necessarily require weighting if one architecture dominates another on every relevant criterion"* | **Taken.** *"where one architecture pays less of one charge and more of another, the ranking depends on the weighting."* Step 13 then meets a near-case of exactly this (Section 6) |
| *"No quantity already computed in this work provides a scale-derived buffer requirement independent of the energy-store model"* | **Taken**, adapted to include the hover and engine powers |
| The published scale comparison needs a primary citation | **Moot** — the rewritten body no longer quotes it |

### Grok

| Point | Done |
|---|---|
| The 5 percent is a property of constant disc loading, with a second rule | **Taken**, and it found the engine-margin omission (Section 2) |
| *"Say once that both ends of this comparison are the published reference pair, not the Section 10 closures"* | **Taken**, with the reason: mixing them would manufacture a scale change that is a propeller update at one end |
| *"'Light design is the harder case for Bill 2' is earned by the rotor term … Leave the sentence on the rotor term"* | **Taken.** And *"the opposite of the usual expectation"* was removed — it had no source |
| Square–cube rotation stays out of the three-charge table | **Kept** |
| *"What 13 cannot inherit: a claim that the mass bill is the thing that flips"* | **Kept.** Step 13 says the contract weighs a mass difference against a cruise-efficiency difference, and names what each side contains |
| *"Then write 13 on the light four-closure envelope only"* | **Done.** No heavy figure in Step 13 |

### DeepSeek

| Point | Done |
|---|---|
| The q-cancellation objection | **Taken — Section 1** |
| Bill 1 test at fixed specific power | **Checked — Section 3.** Arithmetic corrected; the test locks Bill 1 to Bill 3 |
| Disc loading 44.2 vs 43.7 is not "constant" | **Taken:** *"held at approximately the same value … one percent apart"* |
| Bridge Step 10's 52–58 kg to the published 50 kg | **Taken:** Section 10 closed only the light design; no closure could be run at 1 000 kg on the same footing |
| *"The heavy design cruises faster at a better L/D"* depends on an unstated basis | **Removed.** The engine side is now described by its margin, not explained by L/D |
| Sweep Steps 1–9 for unqualified "50 kg" | **Run: none found.** Step 6 already bridges to 52–58 kg |
| *"The argument requires only two"* | **Taken**, with Qwen's and Grok's same point |
| Q2: *"Bill 2 responds physically, Bill 3 responds to the design rule"* | **Declined.** Bill 2's rotor term also follows design choices — blade design and cruise speed, and now chord and speed through Reynolds number. Also: holding disc loading free does not give W^1.5 under geometric similarity; W^1.5 is the fixed-disc-area exponent |
| Q3: state the refusal positively | **Moot** — the three-digit agreement is gone with the mechanism it belonged to |

### Qwen

| Point | Done |
|---|---|
| Bill 1 derivation is trivial — held flat by the same rule | **Taken, sharpened — Section 3** |
| *"Lead with the difference, not the flatness"* | **Taken** in *"What the comparison establishes"* |
| *"The argument requires only that at least two charges move independently"* | **Taken** |
| State why no heavy range is given | **Taken:** the figures either omit the rotor charge or carry an assumed propeller efficiency, and none carries both |
| Step 12 should not use the buffer as evidence without noting it is an input | **Already so**; Step 12 uses it as evidence of nothing |

---

## 5. What I found myself this round

- **An over-attribution that ChatGPT caught in Step 11 two rounds ago had been repeated in Step 12.**
  Step 12 said *"refusing the variable-pitch hub costs as much or more at the larger size."* Step 11 now
  says no variable-pitch counterfactual was computed. Step 12 carries Step 11's language.
- **The heavy fixed-pitch gap is 16.4 to 22.9 percent**, not 23.0 — the script prints 22.9.
- **An earlier renaming of the repository's files broke six scripts** (calls left under old module
  names). One of them is the rotation script behind the transition figures Step 12 quotes. Repaired;
  three re-run, three compiled only (they need a CFD solver).
- **The transition figures (221.5 kW, 13.4 kW) appear in no script output.** The repaired rotation
  script reproduces them within 2 percent (217.6 and 13.1 kW). Step 12 now gives them rounded: *about*
  220 kW, *about* 13 kW.
- **Step 2 referred to "Table 1"**, and v8 has no numbered tables. Fixed.
- **A new check** now scans the English body of every v8 step for 22 retired phrases and numbers, and
  tests itself by catching 10 of them in last round's Step 12.
- **Two errors in my first draft of Step 13**, caught before sending: one sentence said the tilt layout
  was *"not behind on either count"* — it is 0.5 to 5.4 percent heavier, so there is a trade, only a
  lopsided one; and my first repair of Step 9 put a number into a section the skeleton defines as
  coming *before any number*.

---

## 6. What Step 13 found — and what it did to Steps 2, 9 and 10

**Step 13 needed a computation that did not exist.** Three architectures — this configuration,
lift-plus-cruise, tilt — sized under three contracts (fixed fuel fraction, fixed fuel mass, fixed
take-off mass and payload) at each of Step 10's four closures. This configuration's column reproduces
Step 10 exactly.

**The basis is stated in Step 13 with each asymmetry's direction**, and it is the part I most want
checked: this configuration's propeller efficiency is computed (0.632 / 0.683); the other two are
assumed at 0.80. Lift-plus-cruise drag is a ratio (13/17) measured on a different airframe with lift
propellers locked parallel to the flow. The tilt carries no cruise drag penalty at all — a deliberate
bound. Lift-group mass (10 %) and tilt mechanism (5 %) are parameters. Bill 3 is held common: all
three carry the same buffered series-hybrid power system.

**Against lift-plus-cruise** (its range relative to this configuration):

| | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass |
|---|---:|---:|---:|
| Four closures | +55 to +84 % | +28 to +54 % | **−13 to +7 %** |

The contract moves the comparison by 67 to 77 points at every closure, always toward the lighter
aircraft. **Under a fixed take-off mass the sign changes inside the envelope** — this configuration is
ahead with the higher-efficiency blade family, behind with the lower. And the sign turns on an
unmeasured parameter: **with the lift group at 5 % this configuration is ahead nowhere; at 15 % it is
ahead under a fixed take-off mass at every closure.** Giving all three the same propeller efficiency
also produces a reversal at every closure.

**Against the tilt**, as modelled: ahead by 93 to 141 percent under every contract at every closure. A
bound, not a ranking.

**This forced three changes elsewhere, and one of them needs your judgement.**

- **Step 2 made a prediction:** *"where an arrangement pays one charge heavily in order to escape
  another, the ranking against a differently-balanced arrangement **will reverse** when the sizing rule
  changes. Section 13 tests that prediction."* Step 13 found the **movement** everywhere, but the
  **reversal** at only two of four closures against lift-plus-cruise and at none against the tilt bound.
  **I narrowed Step 2 to:** *"… its ranking … will move when the sizing rule changes — toward the
  lighter arrangement as the rule weights mass more — and can reverse."* **That is a prediction
  narrowed after its test.** I think the original overstated what the framework implies — the
  framework gives the direction; whether a reversal occurs depends on magnitudes — but I may be moving
  a goalpost. **Question 3 asks you directly.**
- **Step 9** said the ranking against the other hybrids *"reverses across the three contracts reported
  in Section 13."* Now: it moves substantially, and under one contract its sign changes inside the
  envelope and turns on an unmeasured mass fraction; against the tilt the competitor is only a bound.
- **Step 10** said Section 13 is *"where it is made and where it reverses."* Now: *"where it is made."*

**For the record, not for the paper:** the corresponding published comparison (v7) had lift-plus-cruise
+24 to +45 % under a fixed fuel fraction and a mass advantage of 32 to 36 %. Step 13's figures are +55
to +84 % and 27 to 30 %. The difference is the computed propeller efficiency: it enlarges this
configuration's cruise power and engine, and the competitors keep 0.80.

---

## 7. Step 12, in full (second writing)

### Scale does not lock two of the charges together; the third is not tested

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

#### What is compared, and why it is these two points

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

#### Bill 3 — held nearly flat by a sizing rule, which is not a finding about Bill 3

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

#### Bill 2 — the rotor term falls, and the reason is Reynolds number

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
blade; at 1 000 kg nothing selects within the interval, and its ends are the ends of the sweep. **At
every point in it the heavy charge is between 0.29 and 0.65 of the light one.**

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

**What moves is the section Reynolds number.** In the free-wheeling state the median blade-section
Reynolds number rises from about 8 × 10⁴ at 50 kg to 5.6 × 10⁵ at 1 000 kg, a factor of 6.8, because
the chords are longer and the flight speed higher. **Evaluating the heavy blade with its section
Reynolds number scaled down to the light rotor's returns 0.0181 — 1.18 times the light charge.** At
equal Reynolds number the heavy rotor would pay slightly more, as its fuller blade suggests; the whole
of the fall, and a little more, comes from the lower section drag at the higher Reynolds number.

**That places a condition on the result.** The fall rests on how section drag changes between 8 × 10⁴
and 5.6 × 10⁵, which is taken from the section polars used for every rotor in this work rather than
measured, and the light end lies below a Reynolds number of 10⁵, where section drag is hardest to
predict. The direction — lower section drag at higher Reynolds number — is the ordinary one. **The size of the fall is as good
as the section model at the low end.**

**The result does not touch the structural question.** It comes from blade-element solutions on two
sized rotors at their own conditions; it would remain a result even if the heavy airframe were shown
not to close. **For the rotor term, the light design is the harder case.** That statement is not
extended to Bill 2 as a whole, because the frame term is not computed at the heavy design and the
heavy design has no drag bracket.

#### Bill 1 — not tested, and the one available derivation would not test it

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

**Nor is the structural mass a substitute.** The shell-mass exponent governs how the airframe
fraction scales, and it is unmeasured; but the airframe is not Bill 1 as Section 2 defines it — it
is the structure every architecture carries — and treating it as the mass bill would change the
definition to fit the test. What specific power a store of the required mass must deliver is the
item Section 14 examines and does not resolve.

#### What the comparison establishes

**Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its
light-design value, while specific hover power changes by one percent and the Bill 3 ratio by 5 to 14
percent.** The flatness of Bill 3 is imposed by a sizing rule; the finding is that Bill 2 moved anyway,
by more than the Bill 3 ratio at every point in the heavy interval and under either engine margin.
**Within this model, the two are therefore not one quantity under two names.**

**Bill 1 is not tested**, for the reason given above, and nothing here should be read as showing
that it separates from the other two — or as showing that it does not.

**And the evidence is one pair of design points, computed by one method, with the Bill 2 result
resting on a section-drag model at low Reynolds number.** It is consistent with the separability
Section 2 asserts; it is not a verification of separability as a general property, which a single
instantiation cannot supply.

#### Two costs that scale does not relieve

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

#### Why this section sits between the ledger and the contracts

**The next section needs only what this one shows.** If the three charges were one quantity, a single
number could rank architectures whatever weight each charge was given. **Because at least two of them
are not locked together, a comparison of architectures cannot in general be reduced to a number that
does not depend on how the charges are weighed: where one architecture pays less of one charge and
more of another, the ranking depends on the weighting.** The argument requires only two. A third
shown to be separate would strengthen it; a third shown to be locked to one of the others would
leave it standing.

Section 13 examines what the choice of sizing contract does to a ranking, on the light closures of
Section 10 only.

---

## 8. Step 13, in full (first writing)

### Rankings belong to contracts

Section 12 showed that at least two of the three charges are not locked together, and drew the
consequence: where one architecture pays less of one charge and more of another, a ranking depends
on how the charges are weighed. **A sizing contract is one such weighing.** It fixes what is held
equal between the architectures being compared, and what is held equal decides how a difference in
mass is set against a difference in cruise efficiency. This section applies three contracts to three
architectures at each of the four closures of Section 10.

#### Three contracts, and what each holds equal

Range in the sizing loop is

> R = (E* η / g) · (L/D) · (m_fuel / m_TO),

where E* is the fuel's specific energy and η the energy chain, propeller included. The three
contracts differ only in the last factor.

- **Fixed fuel fraction.** Every architecture carries sixteen percent of its own take-off mass as
  fuel. **Take-off mass cancels from range**, which is then set by L/D and the chain alone. A
  heavier architecture shows its mass in the take-off-mass column and nowhere in the range column.
- **Fixed fuel mass.** Every architecture carries the fuel this configuration carries at the same
  closure — 8.4 to 9.2 kg. **Range is divided by take-off mass**, so a heavier aircraft flies the
  same fuel less far.
- **Fixed take-off mass and payload.** Every architecture is held to this configuration's closed
  mass and its 13 kg payload. **Fuel is what remains after the empty mass**, so every kilogram of
  architecture-specific hardware is a kilogram of fuel not carried.

**These are three different questions, not three estimates of one answer.** The first asks which
aircraft converts a fuel fraction into distance more efficiently; the second, which flies further on
a given tank; the third, which flies further at a given gross weight. A mission decides which of
them it is asking. This paper has no mission that would decide, and does not choose.

#### What is compared, and on what basis

**Three architectures fly the same mission**: 13 kg of payload at 30 m s⁻¹, with the same wing
loading, disc loading and aspect ratio, the same airframe and avionics fractions, and the same fuel
and energy chain apart from the propeller. **All three carry the same buffered series-hybrid power
system** — a buffer of 3.6 percent of take-off mass and an engine sized by cruise — so Bill 3 is held
common, and what the comparison measures is mass and cruise drag. This configuration is the first
architecture; the others are a lift-plus-cruise layout and a tilting one.

**The basis is not symmetric, and each asymmetry is stated with its direction.**

- **Drag.** All three share the clean airframe at each end of the drag bracket. This configuration
  carries its exposed frames and free-wheeling rotors, as in Sections 10 and 11. The lift-plus-cruise
  layout carries the ratio measured in the wind-tunnel campaign quoted in Section 2 — maximum
  lift-to-drag ratio about 17 clean and about 13 with the lift hardware installed and its propellers
  locked parallel to the flow — **transferred from a different airframe**, and assuming lift rotors
  stopped and aligned in cruise, which takes an indexing mechanism (Section 7) whose mass is not
  separately charged. **The tilting layout carries no cruise drag penalty at all.** That is an
  idealisation in its favour, and it is deliberate: it makes the tilt row a bound.
- **Propeller efficiency.** This configuration uses the computed 0.632 and 0.683 of Section 10. The
  other two use 0.80 — the lift-plus-cruise layout because its cruise propeller does nothing else,
  the tilting layout because it has a variable-pitch hub. **Both are assumed, not computed**, and the
  asymmetry runs against this configuration; it is tested below.
- **Mass.** The lift-plus-cruise layout carries a lift group of 10 percent of take-off mass and the
  tilting layout a tilt mechanism of 5 percent. **Neither figure is measured.** The first turns out to
  decide the sign of one result, and it is varied below.

#### Against lift-plus-cruise: a trade, and the contract sets the exchange rate

**The two architectures trade one charge against another.** Closed under a fixed fuel fraction, the
lift-plus-cruise layout is **38 to 43 percent heavier** — its lift group, amplified by the mass loop,
partly offset by this configuration's larger engine — so this configuration is **27 to 30 percent
lighter**. In return the lift-plus-cruise layout cruises at a lift-to-drag ratio of 11.66 to 15.72
against 8.79 to 10.82, with a propeller at 0.80 against 0.632 to 0.683.

Range of the lift-plus-cruise layout relative to this configuration:

| Closure (Section 10) | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass |
|---|---:|---:|---:|
| Adverse drag, lower blade family | +67.8 % | +40.2 % | +1.1 % |
| Adverse drag, upper blade family | +55.3 % | +27.5 % | **−13.0 %** |
| Favourable drag, lower blade family | +83.9 % | +53.5 % | +7.3 % |
| Favourable drag, upper blade family | +70.2 % | +40.1 % | **−6.5 %** |

**Under a fixed fuel fraction the mass difference does not reach the range column**, and the
lift-plus-cruise layout flies 55 to 84 percent further. Under a fixed fuel mass the difference enters
as a divisor, and its lead falls to 28 to 54 percent. Under a fixed take-off mass it enters as fuel not
carried, and **the lift-plus-cruise layout lands between 13 percent short of this configuration's
range and 7 percent beyond it.** Moving from the
first contract to the third shifts the comparison by **67 to 77 percentage points at every closure**,
and always toward the lighter aircraft.

**The sign itself changes inside the envelope under the third contract.** This configuration is
ahead at the two closures with the higher-efficiency blade family and behind at the two with the lower.
**A statement of which architecture has the longer range, made without its contract, would therefore
be a statement about the contract.**

#### Against the tilting layout: a bound, not a ranking

**The tilting layout, as modelled, leads under every contract at every closure — by 93 to 141
percent.** Moving from the first contract to the third shifts the comparison by 1 to 18 points toward
this configuration, and nowhere near a reversal.

**There is a trade, but it is lopsided.** The tilting layout closes 0.5 to 5.4 percent heavier than
this configuration, and it cruises at the clean airframe's lift-to-drag ratio with a propeller at 0.80:
it is credited with no nacelle drag, no pivot fairing, and no penalty for flying hover-sized rotors as
cruise propellers. **Even the contract that weights mass most** — a fixed take-off mass, in which every
kilogram of tilt mechanism is a kilogram of fuel not carried — **leaves it 93 to 130 percent ahead.**
The contract moves the comparison, as Section 12 says it must where there is a trade; none of the
three moves it far enough to matter. A ranking against a competitor modelled as a bound is not a
ranking, and **no range claim is made against the tilting family in either direction.**
The claim this paper makes against that family is about mechanism (Sections 7 and 8), and nothing in
this section bears on it.

#### Section 2's prediction, tested

**Section 2 predicted that where an arrangement pays one charge heavily in order to escape another,
its ranking against a differently-balanced arrangement will move when the sizing rule changes, and
can reverse.** Both parts can now be checked.

- **The movement holds everywhere**, against both competitors, in the predicted direction: toward the
  lighter arrangement as the contract weights mass more.
- **The reversal holds at two of the four closures against lift-plus-cruise, and at none against the
  tilt bound.**

**Where the reversal falls is decided by quantities this study has not measured or not fixed.** In
the case above it is the blade family, which Section 10 leaves open. Across the sensitivity cases in
the repository it is the competitor's lift-group mass and the propeller basis:

| Case | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass |
|---|---:|---:|---:|
| As above | +55 to +84 % | +28 to +54 % | −13 to +7 % |
| Lift group 5 % of take-off mass | +55 to +84 % | +47 to +76 % | +36 to +65 % |
| Lift group 15 % of take-off mass | +55 to +84 % | +8 to +31 % | −62 to −50 % |
| All three at this configuration's propeller efficiency | +33 to +45 % | +6 to +17 % | −33 to −25 % |
| Lift-plus-cruise drag as a fixed increment, not a ratio | +59 to +75 % | +31 to +45 % | −13 to +5 % |

*(Range of the lift-plus-cruise layout relative to this configuration, across the four closures.)*

**With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every
closure; with a heavier one this configuration leads under a fixed take-off mass at every closure.**
Giving all three the same propeller efficiency also produces a reversal at every closure. **Which
architecture ranks first under a fixed take-off mass is therefore decided, in this model, by a mass
fraction of the competitor that this study has not measured** — and the fixed-fuel-fraction column,
where mass does not enter, does not move with it at all.

#### What the framework asks of whoever uses it

A framework that says every remedy transfers a charge rather than removing it takes something from
its user in return. **It asks for three things, and this paper holds itself to them.**

**Carry the audit.** State each charge in its own currency — kilograms, drag counts, installed
kilowatts — before any aggregate, as Section 11 does. An aggregate that arrives without its parts
cannot be checked, and the parts are where the comparison is decided.

**Name the contract.** A comparison of architectures is a comparison under a contract. The contract is
chosen by the mission rather than by the analyst, and a comparison that does not state one has chosen
one silently.

**Refuse the bare ranking.** Report an ordering only with the contract it was computed under, and,
where its sign depends on an unmeasured quantity, with that quantity named. Applied to this paper's
own numbers, the rule is the fourth row of Section 9: **no range claim is made against lift-plus-cruise
or tilting layouts**, because the ordering against the first depends on the contract and on the
competitor's lift-group mass, and the ordering against the second is against a bound.

#### What this section does not establish

**The competitors are modelled at a coarser level than this configuration.** Their drag is a ratio
transferred from another airframe or an idealisation; their propeller efficiency is assumed; their
architecture-specific mass is a parameter. This configuration's drag and propeller efficiency are
computed. **Comparing computed figures against assumed ones favours whichever is assumed more
optimistically**. In propeller efficiency that is both competitors, and the table above shows the
size of it; in drag it is the tilting layout, by construction.

**The comparison is at one size.** Section 12's heavy design has no closure, and none of its figures
is used here.

**And nothing here ranks architectures for a mission.** Which contract a mission implies, and which
architecture it then favours, is the user's question. What this section establishes is narrower: **the
same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that differ
by some seventy points and, inside the envelope, in sign** — so the ordering is not a property of the
architectures alone.

---

## 9. What I am asking

1. **Step 12's new mechanism.** The rotor charge's fall with scale is now attributed entirely to
   section Reynolds number, isolated by re-evaluating the heavy blade at the light rotor's Reynolds
   number. **Is that a fair isolation?** And since the whole scale result for Bill 2 now rests on
   section drag below Re = 10⁵, **is the caveat in the body enough, or should the result be weakened
   further?**
2. **The Bill 1 argument.** Step 12 says a buffer derived from the hover deficit is locked to Bill 3 by
   the derivation, so separability of Bill 1 and Bill 3 is not established on this aircraft. **Is that
   sound — and does it prove too much?** Does it amount to saying that on this configuration Bill 1 and
   Bill 3 are one charge, and if so, what does that do to the framework of Step 2?
3. **Step 2's prediction, narrowed after its test.** *"Will reverse"* became *"will move … and can
   reverse"* once Step 13 found a reversal at two of four closures. **Is that the correction of an
   overstatement, or a moved goalpost?** If the latter, what should Step 2 say — keep the strong form and
   let Step 13 report it as partly failed?
4. **Step 13's basis.** This configuration computed; the competitors assumed (0.80), transferred (13/17)
   or idealised (tilt). **Is the comparison worth reporting in this form at all? Is there an asymmetry I
   have not named?** In particular: is holding Bill 3 common — all three buffered — the right choice for
   a section about rankings, or does it remove the one charge this configuration was built to escape?
5. **What the framework asks of its user.** Step 13 names three obligations — carry the audit, name the
   contract, refuse the bare ranking. **Are those the right three, and does the paper actually meet
   them?**

**No source is needed for any of this.** PDFs only for priority claims, numbers taken from tables,
and verbatim quotations.
