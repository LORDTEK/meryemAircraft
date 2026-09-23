# Round 56 — you agreed on the hard questions; checking your answers found two things none of you could see; and Step 14 is written

> **READ THIS FIRST.** Everything this round asks about is reproduced here. **You are not being
> asked to read a manuscript.** v8 is written as separate step files in `paper/v8/`;
> `paper-v6.md` and `paper-v7.md` are frozen historical records. **If your knowledge base holds a
> file whose name contains `makale-v` or `paper-v`, it is not what this round is about.**

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`36961cc`**.

```
paper/v8/14-what-does-not-close.md           SHA-256 301490035dbad819fa71939f81d63424d1457fa460ccca6e0a8bd4d8837d8bbc
paper/v8/13-rankings-belong-to-contracts.md  SHA-256 d178396bd5677be037f3439191cdfbdd8a58551c0021debfcdea6fd63abb190c
paper/v8/12-the-bills-separate.md            SHA-256 c2fd19c6d3a32b7b67e44d9b66fed5688e01abe53162ded7676898812a7d0a10
paper/v8/11-the-ledger.md                    SHA-256 94c33c1fc400deb0bb8bc7292bc5be93847a344f69195686775f56484293dc9c
paper/v8/02-the-tax.md                       SHA-256 14f42820a0bb648f7e6bde5f11bc18788acc6fc400c26917ba7d625d3d767b87
aero/buffer.py                               SHA-256 95d64608be9ee0ba2daefc1453ec5151ee6c53c1a291032dec002c03e2dc8364
aero/contracts.py                            SHA-256 ac69e03406ce4f27a38cc4274c7f388a09268ad1d98bd31234820a53c01015a9
```

**Step 14 is new** and is reproduced in full in Section 8. **Step 13 changed substantially** and is
reproduced in full in Section 7. **Steps 2, 11 and 12 changed in specific passages**, reproduced
verbatim in Section 6.

**The author asked, again, that this round state plainly who said what and what was done.**
Sections 1 to 5 do that.

**Who answered last round: all four of you.** Qwen said it could not fetch the repository and so could
not check the hashes — that is expected; the hashes are there so a reader who *can* fetch can check.

---

## 1. Where all four of you agreed — and what that settled

| Question | Grok | ChatGPT | DeepSeek | Qwen | Settled as |
|---|---|---|---|---|---|
| Is the Reynolds isolation fair? | Fair as a one-term hold | Yes, as a model isolation | As a decomposition, not causation | Fair | **Kept; worded as a decomposition inside the model** |
| Does "Bill 1 locked to Bill 3" collapse the framework? | No — *"not established,"* not *"the same charge"* | No — *"functionally coupled without being the same accounting quantity"* | Sound — and state the coupling as a result | No — a property of this configuration | **Both: coupled here (DeepSeek), coupling is not identity (the other three)** |
| Step 2 narrowed after its test — goalpost? | *"Correction of an overstatement"* | *"Not goalpost-moving"* | Correction — but say so in Step 2 | Correction | **Kept narrowed; not narrated in the body (see 3)** |
| Is Step 13's comparison worth reporting? | Yes, as a demonstration, not a ranking | Yes, as a conditional model comparison | Yes, with one framing change | Yes | **Kept, with the additions in Section 2** |
| Are the three obligations right? | Right three — but *"carry the audit"* is not met for the competitors | Right three | Right, plus a fourth; qualify the third | Right three | **Kept three; first expanded, third qualified** |

**Four independent readers converging on the same answers to the same five questions is what the
author wanted before going on.** The rest of this round is the detail.

---

## 2. What was taken, by reader

### Grok

| Point | Done |
|---|---|
| *"Weaken the factor, not the direction"* — put *"in this polar"* into the finding sentence | **Taken**: *"At every point in it, and in the section polars used here, the heavy charge is between 0.29 and 0.65 of the light one — a direction that is the ordinary one and a factor that is not a measurement"* |
| *"'Entirely' is slightly strong"* | **Taken** — replaced (see DeepSeek) |
| Bill 3 held common is *"a choice of question"*; say so in one sentence | **Taken**, and its direction was **computed** (Section 3) |
| *"The competitors are this planform with two add-ons. Say that."* | **Taken**, verbatim in substance |
| *"Do not let 93–141 % leave the page without 'bound' in the same sentence"* | **Taken** — both occurrences |
| *"Carry the audit"* is met for this aircraft, not for the competitors | **Taken**: *"This paper meets that for its own column and not for the competitors'"* |
| *"Then write 14."* | **Done** — Section 8 |

### ChatGPT

| Point | Done |
|---|---|
| Attribute the Reynolds result *"within the blade-element/section-polar model"* | **Taken**, in those words |
| *"The three bills are distinct accounting quantities, not assumed to be independent physical causes"* — put it in Step 2 | **Taken** — and it exposed a contradiction none of you could see (Section 4) |
| Step 2's prediction as a conditional: reversal *"only when the changed weighting crosses the relevant break-even point"* | **Taken** (Qwen proposed the same) |
| Bill 3 held common needs an explicit sentence — *"Without it, the reader could think Bill 3 was omitted because it was inconvenient"* | **Taken** |
| *"The argument requires only two non-locked charges; the third need not be shown separately"* | **Taken** |

### DeepSeek

| Point | Done |
|---|---|
| Isolation is a decomposition, not causation — *"Reynolds number is not an independent variable"* | **Taken**: *"a decomposition inside the model rather than a causal claim beyond it"* |
| The low-Re uncertainty is **two-sided**; name both directions | **Taken** |
| *"If a reader is going to doubt 0.0068, they should doubt 0.0154 first"* | **Taken, narrowed** — *"of the two rotor terms, the light one is the less certain"*, not *"the largest uncertainty in the chain"*; and the caveat now also stands in Step 11, where 0.0154 first appears |
| *"The whole of the fall, and a little more"* → give the 18 % | **Taken** |
| The 0.29–0.65 ends are the sweep's ends, not a physical bound | **Taken** |
| State the Bill 1–Bill 3 coupling as a result | **Taken**, with the other three's limit: *"Coupling is not identity"* |
| Bill 3 held common runs **against** this configuration — say the direction | **Computed and confirmed** (Section 3) |
| A fourth obligation: state the basis with its asymmetries | **Folded into the first**: *"Carry the audit, for every column … and state the basis of the comparison with its asymmetries and their directions"* |
| Qualify *"refuse the bare ranking"* — an ordering stable across every contract is reportable | **Taken** |
| Sensitivity cases should be citable, not only in the repository | **Taken**: the table is in the section; the data-availability statement is on the process list |

### Qwen

| Point | Done |
|---|---|
| Direction robust, magnitude model-dependent — make the split explicit | **Taken** |
| The sign under a fixed take-off mass *"is a parameter choice"* — say it bluntly | **Taken**: *"the sign under a fixed take-off mass is not a result about the architectures; it is a result about that parameter, and it is the one most worth measuring"* |
| Step 2 could say the ranking *"reverses where the mass difference is large enough"* | **Taken** (with ChatGPT's wording) |

---

## 3. What checking your answers found

**DeepSeek:** *"The 67–77 point shift … is robust to the computed-vs-assumed asymmetry, because that
asymmetry is identical in all three contracts."*

**Half right, and the half that is wrong mattered.** The shift was computed for every sensitivity case:

| Case | Shift, fixed fuel fraction → fixed take-off mass |
|---|---:|
| As reported | 67 to 77 points |
| All three at this configuration's propeller efficiency | 65 to 72 |
| Lift-plus-cruise drag as a fixed increment | 67 to 75 |
| **Lift group 5 % of take-off mass** | **14 to 24** |
| **Lift group 15 % of take-off mass** | **117 to 134** |

**Robust to the propeller and drag basis; not robust to the lift group** — because the shift *is* the
mass difference being counted. Step 13 had said the orderings *"differ by some seventy points"*; that
figure belongs to the declared 10 % lift group and is now stated that way.

**DeepSeek, Grok, ChatGPT: holding Bill 3 common runs against this configuration.** I did not assume
the sign; I computed it. With the competitors given no buffer and an engine sized by hover, the
lift-plus-cruise layout closes at **381 kg**, falls 11 to 23 % behind under a fixed fuel mass, and **does
not close** under a fixed take-off mass; the tilt bound falls 75 to 98 % behind there, or does not close.
**And under a fixed fuel fraction the lift-plus-cruise lead is unchanged at 55 to 84 % although the
aircraft is seven times heavier** — the first contract's blindness to mass, made visible. That comparison
is **not used**, and Step 13 says why: it would set competitors without a store against this
configuration with one whose feasibility Step 14 examines — and Step 14 finds it wanting.

**Declined:**

- **DeepSeek:** add to Step 2 *"An earlier form of this sentence said the ranking will reverse …"* — the
  author's rule is that the journal body carries no "an earlier version said" narrative; the narrowing is
  recorded in the repository and in this text.
- **DeepSeek:** *"the competitors' L/D 11.66–15.72 vs this configuration's 8.79–10.82 … are not directly
  comparable"* — they are: both are aerodynamic ratios on the same clean airframe, and propeller
  efficiency is given separately in the same sentence. The sentence now names which end each number
  belongs to.

---

## 4. Something none of you could see: Step 2 contradicted Step 12

Adding ChatGPT's sentence to Step 2 meant reading the paragraph it went into. **Its heading was:**

> *"The charges behave as one quantity in three currencies"*

**Step 12 tests exactly that and concludes the opposite** — *"not one quantity under two names."* Your
copies did not contain Step 2, so no one could have caught it. The skeleton's intent was *"three coupled
charges; every remedy transfers."* **The heading is now** *"The charges are coupled: remedies move cost
between them"*, followed by ChatGPT's sentence and a pointer to Step 12. The full paragraph is in
Section 6.

---

## 5. What writing Step 14 found

**First, an error of the same kind v7 had already corrected — back in v8.** The buffer sits at the
electrical bus. The rotor's demand reaches it through the machine (0.92) and power electronics (0.95);
the engine's output reaches it through the generator (0.90). v7 once subtracted engine *shaft* power from
rotor *shaft* power and divided by the buffer, got 4.61 kW/kg, and corrected it to 5.63 at the bus.
**Step 11's buffer deficit and Step 12's Bill 1 derivation both made the same shaft-minus-shaft
subtraction.** At the bus:

| | before | after |
|---|---|---|
| Step 11, deficit per kg across the four closures | 0.128–0.150 kW/kg, spread 17 % | **0.168–0.188, spread 12 %** |
| Step 12, deficit per kg, 50 kg → 1 000 kg | 0.166 → 0.162 | **0.202 → 0.199** |

**Neither conclusion moved:** the corner needing the most buffer per kilogram still gets the least, and
the change with scale is still about 2 %. The script and both steps are corrected. **This was mine: a
correction made once in v7's code had not reached code written for v8.**

**Second, the specific-power gap has a new value.** The published figure — a buffer *"specific power 3.8
times the highest rate yet measured on a flown pack"* — was computed at the published design. Section 10's closures are
different aircraft: lower propeller efficiency, larger engine, more mass. At the bus they ask the buffer
for **4.7–5.2 kW/kg to hover and 5.5–6.1 kW/kg to take off**, which is **3.7 to 4.1 times** the highest
measured rate. It lives in one paragraph, as Grok required in the skeleton round.

**Third, the source did not say what the published text said.** The battery study was opened this round
(PDF in the repository). Its 724 W/kg and 892 W/kg are in its Table 3 — the second is the *flown* 24S4P
system, calculated from four times the validated continuous current. **The ~1.5 kW/kg is not a table
entry**: it is derived from the 10.68C bench discharge of the 13.5 kg **24S1P test pack** (1394.3 Wh in
4 min 09 s → 1.49 kW/kg). So the published phrase *"the highest rate yet measured on a flown pack"* was
wrong twice — the rate was measured on the bench pack, not the flown one, and *"yet"* is a claim about
the whole literature that was never searched. Step 14 says what the source says.

**Fourth, deriving the buffer inside the loop.** The loop now sizes the buffer from the take-off demand
at a given specific power; set to the specific power Section 10 implies, it reproduces Section 10
exactly. At about 1.5 kW/kg it closes at **95 to 101 kg (+76 to +81 %)** with a buffer of 13–15 % of
take-off mass; at the flown system's continuous rating, near 335 kg, a figure set by nearness to
non-closure; at the unit pack's continuous rating, not at all. Range is unchanged because the fuel
fraction is held.

**And four errors in my own first draft of Step 14, caught before sending** (the rule that every factual
predicate is checked against its source after writing):

- *"Section 13 holds the store common, so none of its orderings rests on this item"* — false; with a
  heavier common store the orderings could move, and that is not computed. Now said.
- *"The transition moment and the low-Reynolds drag belong to measurement because the methods tried
  disagree"* — true of the first; the second rests on one method, least reliable exactly there.
- A +6.5 % rounded up to +7.
- *"A factor of about four"* in the closing paragraph — a second home for the one number Grok said gets
  one home. Removed.

---

## 6. The changed passages of Steps 2, 11 and 12, verbatim

### Step 2 — the heading that contradicted Step 12, and the prediction

#### The charges are coupled: remedies move cost between them

The three charges are not independent problems with independent fixes. **Each known partial
remedy reduces one and raises another.** They are three distinct accounting quantities — kilograms,
drag counts, installed kilowatts — and they are not assumed to be independent physical causes: a
remedy can move a requirement from one currency into another. Whether a change of size moves them
together, which would make them one quantity under three names, is tested in Section 12.

*(… table of remedies unchanged …)*

It also makes a prediction that can be checked without settling the architectural question at
all: **where an arrangement pays one charge heavily in order to escape another, its ranking
against a differently-balanced arrangement will move when the sizing rule changes — toward the
lighter arrangement as the rule weights mass more — and will reverse where that reweighting carries
it past the point at which the two break even.** Section 13 tests both the
movement and the reversal on this configuration, and Section 4 tests a different consequence
against a sizing study this work did not produce.

---

### Step 11 — the buffer deficit at the bus, and the low-Reynolds caveat on the rotor line

**The rotor line rests on section drag at low Reynolds number.** It is a blade-element result for
blades whose sections run near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section
polars that are computed rather than measured, and section drag is hardest to predict in that range.
Section 12 shows how strongly the term depends on it.

*(…)*

**The buffer fraction is an input to the loop, not a result of it**, and the closure does not
re-derive it from the hover energy the four corners actually need. Dimensionally a fixed fraction
is the right form: at constant disc loading the disc area grows with weight, so hover power is
linear in weight and hover energy with it. **But what the buffer supplies is the hover demand less
what the engine can deliver, and that deficit is not linear.** Taken at the electrical bus, where
the buffer sits — rotor shaft power divided by the machine and power-electronics efficiencies, less
the engine's shaft power times the generator's — it runs from 0.168 to 0.188 kW per kilogram across
the four closures, a spread of 12 percent, while the buffer fraction is held at 3.6 percent
throughout. **The corner that needs the most buffer per kilogram is given the
smallest buffer**, and that is a declared assumption of the closure rather than an outcome of it.

---

### Step 12 — the Bill 2 and Bill 1 subsections as they now stand

#### Bill 2 — the rotor term falls, and in this model Reynolds number accounts for it

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
— the hover demand at the electrical bus less what the engine delivers there — at a specific power
that is the same at both sizes, its mass fraction follows the deficit per kilogram: 0.202 kW kg⁻¹ at
50 kg and 0.199 at 1 000 kg, a fall of about 2 percent. **But that derivation makes the buffer a function of the hover power and the engine
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

---

## 7. Step 13, in full (second writing)

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
and energy chain apart from the propeller. **The competitors are therefore this planform with two
add-ons**, not independently designed aircraft of their families. **All three carry the same buffered
series-hybrid power system** — a buffer of 3.6 percent of take-off mass and an engine sized by cruise —
so Bill 3 is held common, and what the comparison measures is mass and cruise drag. This configuration
is the first architecture; the others are a lift-plus-cruise layout and a tilting one.

**Holding Bill 3 common is a choice of question, and it has a direction.** It is made so that the
contract can be seen acting on a mass difference against a cruise-efficiency difference; it is not a
claim that those families would use this power system, and the tilting family as Section 2 describes
it has no store at all. **The choice runs against this configuration.** Given no buffer and an engine
sized by hover instead, the lift-plus-cruise layout closes at 381 kg, falls 11 to 23 percent behind
under a fixed fuel mass, and does not close at all under a fixed take-off mass; the tilt bound falls
75 to 98 percent behind under a fixed take-off mass, or does not close. **Under a fixed fuel fraction
the lift-plus-cruise lead is unchanged, at 55 to 84 percent, although the aircraft is now seven times
heavier** — the first contract's blindness to mass, made visible. **That comparison is not
used**, because it would set competitors without a store against this configuration with one — a
buffer of 3.6 percent whose feasibility is the item Section 14 examines. Until that item is settled,
the common store is the neutral choice.

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
lighter**. In return the lift-plus-cruise layout cruises at a lift-to-drag ratio of 11.66 at the
adverse end of the drag bracket and 15.72 at the favourable end, against 8.79 and 10.82 — both
aerodynamic ratios on the same clean airframe — with a propeller at 0.80 against 0.632 to 0.683.

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
first contract to the third shifts the comparison by **67 to 77 percentage points at every closure**
at the declared lift-group fraction, and always toward the lighter aircraft.

**The sign itself changes inside the envelope under the third contract.** This configuration is
ahead at the two closures with the higher-efficiency blade family and behind at the two with the lower.
**A statement of which architecture has the longer range, made without its contract, would therefore
be a statement about the contract.**

#### Against the tilting layout: a bound, not a ranking

**The tilting layout, modelled as a bound, leads under every contract at every closure — by 93 to 141
percent.** Moving from the first contract to the third shifts the comparison by 1 to 18 points toward
this configuration, and nowhere near a reversal.

**There is a trade, but it is lopsided.** The tilting layout closes 0.5 to 5.4 percent heavier than
this configuration, and it cruises at the clean airframe's lift-to-drag ratio with a propeller at 0.80:
it is credited with no nacelle drag, no pivot fairing, and no penalty for flying hover-sized rotors as
cruise propellers. **Even the contract that weights mass most** — a fixed take-off mass, in which every
kilogram of tilt mechanism is a kilogram of fuel not carried — **leaves the bound 93 to 130 percent
ahead.**
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
the case above it is the blade family, which Section 10 leaves open. Across the sensitivity cases below
it is the competitor's lift-group mass and the propeller basis:

| Case | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass | Shift, first to third |
|---|---:|---:|---:|---:|
| As above | +55 to +84 % | +28 to +54 % | −13 to +7 % | 67 to 77 points |
| Lift group 5 % of take-off mass | +55 to +84 % | +47 to +76 % | +36 to +65 % | 14 to 24 points |
| Lift group 15 % of take-off mass | +55 to +84 % | +8 to +31 % | −62 to −50 % | 117 to 134 points |
| All three at this configuration's propeller efficiency | +33 to +45 % | +6 to +17 % | −33 to −25 % | 65 to 72 points |
| Lift-plus-cruise drag as a fixed increment, not a ratio | +59 to +75 % | +31 to +45 % | −13 to +5 % | 67 to 75 points |

*(Range of the lift-plus-cruise layout relative to this configuration, across the four closures.)*

**With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every
closure; with a heavier one this configuration leads under a fixed take-off mass at every closure.**
Giving all three the same propeller efficiency also produces a reversal at every closure. **Which
architecture ranks first under a fixed take-off mass is therefore decided, in this model, by a mass
fraction of the competitor that this study has not measured** — and the fixed-fuel-fraction column,
where mass does not enter, does not move with it at all. **Put plainly, the sign under a fixed take-off
mass is not a result about the architectures; it is a result about that parameter**, and it is the
one most worth measuring.

**The size of the shift behaves the same way.** It barely moves when the propeller or drag basis is
changed — 65 to 77 points across those cases — because those asymmetries enter all three contracts
alike. It moves a great deal with the lift group, from 14 to 134 points, because the shift *is* the
mass difference being counted. **What is robust is that the shift exists and runs toward the lighter
aircraft; its size is the size of the mass difference.**

#### What the framework asks of whoever uses it

A framework that says every remedy transfers a charge rather than removing it takes something from
its user in return. **It asks for three things, and this paper holds itself to them.**

**Carry the audit, for every column.** State each charge in its own currency — kilograms, drag
counts, installed kilowatts — before any aggregate, and state the basis of the comparison with its
asymmetries and their directions. An aggregate that arrives without its parts cannot be checked, and
the parts are where the comparison is decided. **This paper meets that for its own column** (Section
11) **and not for the competitors'**, whose kilograms and drag counts here are parameters and transferred
ratios rather than an audit — which is one more reason no ranking against them is offered.

**Name the contract.** A comparison of architectures is a comparison under a contract. The contract is
chosen by the mission rather than by the analyst, and a comparison that does not state one has chosen
one silently.

**Refuse the bare ranking.** Report an ordering only with the contract it was computed under, and,
where its sign depends on an unmeasured quantity, with that quantity named. An ordering that holds
under every contract examined may be reported as such — that is a stronger statement than any one
contract gives, and it still names the contracts. Applied to this paper's
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
same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by
tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property
of the architectures alone.

---

## 8. Step 14, in full (first writing)

### What does not close

Section 10 closed the sizing loop on a declared package and said that whether an aircraft can be
built to it is a different question. **This section is where that question is answered, and for the
first item the answer is no.** Section 9 called this section a debt: questions the paper does not
answer and that better evidence would. It is stated in that order — first the obstacle that is known,
then what is not known.

#### First, the known obstacle: the energy store

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

#### What the obstacle does not touch

**The mechanism claim does not depend on it.** Sections 7 and 8 count the classes of mechanism that a
tilting architecture needs to change regime and this one does not; that is a statement about hardware,
and a heavier store changes none of it. **The cruise-efficiency comparison of Section 6 does not depend
on it either**: it is made in effective lift-to-drag ratio, a ratio of aerodynamic and propulsive
efficiencies that the buffer's mass does not enter. **What the obstacle bears on is whether this
aircraft, at these numbers, can be built** — which the paper does not claim.

#### Then what is not known

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

#### What this section amounts to

**The loop closes; the aircraft is not shown to.** At the energy store the paper can name the gap
exactly, in specific power and in take-off mass. Everywhere else it can name only what would settle the
question. **The architecture
claim — that the regime change is made with no mechanism that reorients a propulsor — is a count of
hardware, and nothing in this section reaches it.** What this section reaches is the aircraft, and the
paper has not claimed the aircraft.

The last section returns to the four axes of Section 9 and states what is claimed on each.

---

## 9. What I am asking

1. **Step 14's first item.** The section says the package Section 10 closes on *"does not exist with any
   store the sources consulted here report as built"*, and then re-closes the loop at measured specific
   powers. **Is the energy-store paragraph at the right strength** — and is the re-closure at about
   1.5 kW/kg (95–101 kg) legitimate in a loop whose airframe is a fixed fraction, or does it overreach
   once the aircraft is twice the mass the fractions were set at?
2. **"What the obstacle does not touch."** The section argues that neither the mechanism claim nor the
   cruise-efficiency comparison against multirotors depends on the store. **Is that true — and is there
   a claim in the paper that the store *does* reach and the section fails to name?**
3. **The unknowns table.** Is anything missing, and is anything classified wrongly — measurement versus
   analysis not yet done versus absent?
4. **The station error.** Steps 11 and 12 subtracted shaft from shaft; both are now at the bus. **Is
   there any other place in Steps 1–14, as you have them, where powers at different stations are
   combined?**
5. **Step 2's new heading and conditional prediction.** Do they now agree with what Steps 12 and 13
   found? (Section 6 has both passages.)

**No source is needed for any of this.** PDFs only for priority claims, numbers taken from tables,
and verbatim quotations.
