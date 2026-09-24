# Round 69 — Step 12 is applied; the twelve joins are repaired; a second pass on Step 12 from your rewrites; and the first draft of Step 13

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`32d19c7`** ·
> `paper/v8/ALL-STEPS.md` SHA-256 `99e2b167e67474be2c8720317560993944b5f15231834bbc7339d93cd89fc6b4` ·
> `paper/v8/supplement.md` `d85ae6483d79845726f9685a97953b08a8747974e0e6cc60537be5c28ada7059` ·
> `paper/v8/ASSEMBLED.md` `ac6de855e074e237dfe518678f70062bc90e2852a8b9f5965d65249075ad69d9`.
> Not applied: `paper/v8/drafts/12-draft2.md` `077837a1a6b45d45cb590e4a3ec94884e02be622622516d58100aa86b34c80c8` and
> `paper/v8/drafts/13-draft.md` `03ebe7a0b1303eb317eda7c35744678b2901365fc20daeb0639d1478d51fd615`.

---

## 1. Applied — please confirm

**Step 12: none of you vetoed the draft, and it is applied exactly as shown last round** (the ⟦ ⟧ marks removed; the
pointer to S12 stays). 2 973 → 2 152 words. **Supplement S12** holds, in full and verbatim, every paragraph of Step 12
that lost a sentence or a clause, under its original subsection heading. That includes Grok's *"Taking one end from
Section 10 and the other from the reference pair would manufacture a scale change…"* and DeepSeek's two flagged
passages (*"The result does not touch the structural question…"*; the figure of merit 0.75–0.77 against 0.599).

**Protected (all four of you and I):** *"Of the two rotor terms, the light one is therefore the less certain — and it is
the one Sections 10 and 11 carry."* The list is now 151.

**Closed, all five agreeing:** the Step 8 split; no merge of Steps 10 and 11; no definitions table; soul sentences first
or last only as a test in the final voice pass; a figure replaces a body table; the v7 figure rule. **Grok, thank you
for the correction on the quotation.**

## 2. The twelve joins — repaired in the view; please confirm

**DeepSeek's and Grok's repair, applied in the generator:** Step 7 is now **5.1** and Step 8 is **5.2**, rather than both
being "5". No source sentence changed. **All twelve joins are resolved, and none remains:**

- *"which is what Section 5 describe"* → *"which is what Sections 5.1 and 5.2 describe"* (Step 9); likewise *"Sections 5.1
  and 5.2 count the classes of mechanism"* (Step 14) and the other five *"Sections 7 and 8"*: the verbs agree again.
- The five self-pointers now point to the sibling subsection: 5.2 opens *"Section 5.1 claimed that a class of mechanism
  is absent"*; Step 7's three pointers read *"Section 5.2"*.
- **Grok:** the other families were renumbered too — Step 3 is 2.2 and Step 4 is 2.3 (for example *"The nose pair meets
  all four parts of Section 2.2"*). The generator reports any reference that resolves to no section; none does.
- **Qwen:** your regex is no longer needed; the numbering removed the cause.

The generator's check still finds all 151 protected sentences in the view, with the new section numbers.

## 3. One join still open — a protected sentence

*"These are the parts that fail the escape condition"* now follows *"What moves"* (the strip and shaft speed).

| | Proposal |
|---|---|
| DeepSeek | *"**The tip pairs are the parts that fail the escape condition**"* — same strength, correct antecedent |
| Grok | *"Of the hardware just listed, these are the parts that fail the escape condition."* |
| ChatGPT, Qwen | reads as it is |

**My position: DeepSeek's.** It names its subject, and its next sentence (*"The nose pair meets all four parts… The tip
pairs do not"*) already says the same. Grok's still leaves *these* to be resolved, and *the hardware just listed*
includes the nose pair and the strip. The sentence is protected (DeepSeek's own entry), so the list would change in the
same commit, with old and new shown. Vote, please.

## 4. Step 12, second pass — your rewrites, side by side

Deletion alone stopped at 2 152. You proposed rewrites. **Each rewrite is a new wording, so each needs your veto
individually.** Where you overlapped I took one rewrite per paragraph, and the table gives my reason for the choice.

| # | Paragraph | Proposed by | My position |
|---|---|---|---|
| R1 | What is compared (two paragraphs) | Grok; Qwen and DeepSeek similar | **Grok's, with three things restored:** *"sized by one method"*, the scope sentence (*the light design / the heavy design*) — the rest of the section uses those names — and that the structural exponent is not measured. Qwen's drops the drag-bracket condition; DeepSeek's drops *"none could be run on the same footing"* |
| R2 | The engine margin | DeepSeek | **Yes** — same numbers |
| R3 | The Reynolds sentence | DeepSeek | **Yes, keeping *"in the free-wheeling state"*** — the condition the number belongs to |
| R4 | The Bill 1 derivation | Grok; Qwen | **Grok's.** Qwen's says *"by definition"*, which is stronger than the source's *"by the derivation itself"*, and drops *"Coupling is not identity"* and *"they are coupled here"*, which Step 14 relies on |
| R5 | The rotation moment | Grok | **Yes:** *"The moment for a fixed rotation time grows as mL²."* The 220 kW and 13 kW figures stay |
| D1 | *"The next section needs only what this one shows."* | ChatGPT | **Delete** — a transition; the paragraph Step 13 consumes stays whole (Grok's condition) |
| D2 | *"What specific power a store… Section 14 examines and does not resolve."* | ChatGPT | **To S12** |
| — | ChatGPT's own rewrite of the mechanism sentence | ChatGPT | **Not taken** — ChatGPT noted it is stronger (*"the remaining fall is accounted for"*) |
| — | Collapse the three "not general" sentences | ChatGPT | **No.** They guard three different things: the test's reach (protected), Bill 1's untested status, and the scale result's generality |
| — | Qwen's rewrite of *"Why this section sits…"* | Qwen | **No** — it drops *"The argument requires only two charges…"*, which is the scope of what Step 13 takes |

**The second-pass draft, 2 152 → 1 873 words, rewrites marked ⟦ ⟧; every protected sentence present:**

> ## Scale does not lock two of the charges together; the third is not tested
>
> Section 11 decomposed the three charges on one aircraft, at one size. **This section asks a
> different question: are they three quantities, or one quantity under three names?** The test is
> to change the size of the aircraft and see whether they move together. If they did, the framework
> of Section 2 would be a single cost described three ways. Either answer leaves the mechanism claim
> where it was; that claim rests on the inventory of Sections 7 and 8.
>
> **The test is deliberately weak, and it is stated at its own strength.** It can show that two
> charges are not locked together within this model. It cannot show that they are independent in
> general, and it is not offered as doing so.
>
> ### What is compared, and why it is these two points
>
> ⟦**The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 10's closures. No closure was
> run at 1 000 kg.** In this section *the light design* and *the heavy design* mean those two reference designs. **The
> comparison uses powers, loadings and the rotor drag term; the heavy design has no drag bracket and no structural closure
> — the exponent that would give one has not been measured — and no heavy-design range is quoted.**⟧
>
> ### Bill 3 — held nearly flat by a sizing rule, which is not a finding about Bill 3
>
> **Disc loading is held at approximately the same value**: 44.2 kg m⁻² at 50 kg and 43.7 at
> 1 000 kg, one percent apart. At a given figure of merit, specific hover power depends only on disc
> loading, so holding it holds hover power per unit weight — **0.218 kW kg⁻¹ at the light design and
> 0.216 at the heavy**, within one percent. Hover power rises from 10.9 kW to 216.2 kW, a factor of 19.8
> against a mass factor of 20. **Hover power grows linearly with mass rather than as the L^3.5 of the
> classical result.**
>
> **That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3.**
> What it establishes is narrower and still useful: the hover side of Bill 3 *can* be held flat across
> a factor of twenty in mass by a single sizing choice.
>
> **The measure Section 11 uses for Bill 3 — rotor-shaft hover power divided by engine shaft rating, a
> ratio of installed hardware rather than a deficit — carries a second quantity, and it does not travel
> as cleanly.** The ratio is 4.19 at the light design and 3.98 at the
> heavy, a change of 5 percent. *(Section 11's 2.4 to 3.2 is the same ratio at the four closures. This paragraph compares the reference pair only.)* ⟦The engine is sized by cruise, and **the two designs use different margins**: 1.53 times cruise electrical power at
> 50 kg, 1.39 at 1 000 kg. At the light design's margin the heavy engine would be 60.0 kW, ratio 3.61 — 14 percent.⟧ **The Bill 3 ratio therefore
> moves by between 5 and 14 percent across the factor of twenty, depending on an engine margin the
> sizing rule does not set.**
>
> **The rule has a price, and it is paid in geometry.** Holding disc loading constant makes disc area
> grow as L³ rather than L², so the nose propeller grows faster than the airframe. The
> ratio of propeller diameter to span rises from 0.35 to 0.47. **Much above 1 000 kg a single nose pair can no longer hold
> the disc loading**, and a second would have to be added — which the architecture permits, since
> every pair is torque-balanced on its own.
>
> ### Bill 2 — the rotor term falls, and in this model Reynolds number accounts for it
>
> **Only the rotor term of Bill 2 is computed at both sizes.** The frame term enters both reference
> designs as the same multiplier on clean lift-to-drag ratio, by construction, so it cannot show a scale
> effect in either direction.
>
> **The rotor term is computed by one method at both sizes.** At 50 kg it is **0.0154**. At 1 000 kg the blade
> designed to the same section lift coefficient gives **0.0068 — 0.44 of the light value.** Across the
> blade designs swept, design section lift coefficient 0.55 to 0.85, the heavy term runs from **0.0045
> to 0.0100**. At 50 kg the hover requirement selects the
> blade; at 1 000 kg nothing selects within the interval, and its ends are the ends of the swept blade
> family, not a physical bound. **At every point in it, and in the section polars used here, the heavy
> charge is between 0.29 and 0.65 of the light one** — a direction that is the ordinary one and a factor
> that is not a measurement, for the reason given below.
>
> **The mechanism is not the obvious one, and it is not the one a dimensional argument suggests.**
> Three candidates can be excluded directly (geometry, dynamic pressure and solidity; Supplement S12).
>
> ⟦**Within the blade-element and section-polar model, the section Reynolds number accounts for the fall:** in the
> free-wheeling state the median rises from about 8 × 10⁴ at 50 kg to 5.6 × 10⁵ at 1 000 kg, a factor of 6.8.⟧ Reynolds number is not an independent variable — it follows from the chord
> and the speed each rotor has — so this is a decomposition inside the model rather than a causal claim
> beyond it.
>
> **That places a condition on the result, and it runs both ways.** The fall rests on how section drag
> changes between 8 × 10⁴ and 5.6 × 10⁵, which is taken from the section polars used for every rotor in
> this work rather than measured, and the light end lies below a Reynolds number of 10⁵, where section
> drag is hardest to predict. **The direction — lower section drag at higher Reynolds number — is the
> ordinary one; the size of the fall is as good as the section model at the low end.** If the light
> blade's real section drag is higher than the polars give, the light charge is larger and the fall is
> larger; if it is lower, the fall is smaller. **Of the two rotor terms, the light one is therefore the
> less certain — and it is the one Sections 10 and 11 carry.**
>
> **For the rotor term, the light design is the harder case.** That statement is not
> extended to Bill 2 as a whole, because the frame term is not computed at the heavy design and the
> heavy design has no drag bracket.
>
> ### Bill 1 — not tested, and the one available derivation would not test it
>
> **On this configuration Bill 1 appears as the energy buffer**, as Section 11 set out, since there is
> no dedicated lift group to charge. The buffer is 3.6 percent of take-off mass at 50 kg and 4.0
> percent at 1 000 kg.
>
> **Both of those figures are inputs.** Neither is derived from the hover energy the aircraft needs. **A change from 3.6 to 4.0 percent
> is a change between two choices, not a scaling result**, and it cannot be offered as evidence that
> Bill 1 moves with size in either direction.
>
> ⟦**A buffer sized to the hover deficit at the same specific power at both sizes would track hover power and engine
> rating, which are the Bill 3 measures, so that derivation cannot test whether Bill 1 separates.**⟧
>
> **No quantity computed in this work gives a buffer requirement at scale that is independent of the
> hover and engine powers and of an assumed specific power or energy.** On this aircraft Bill 1 takes
> the form of the device that releases Bill 3 from the engine, as Section 3 anticipated, and **whether
> the two are separable here is not established.**
>
> **What is established is that they are coupled here, and that is Section 3's claim rather than a
> defect found in it.** **Coupling is not identity.** The buffer is
> measured in kilograms and the engine in kilowatts, linked by a specific power that is itself an
> assumption; and the coupling belongs to an aircraft that meets the escape condition, not to the
> framework — a lift-plus-cruise aircraft pays a lift group whose mass is not a function of its cruise
> engine.
>
> ### What the comparison establishes
>
> **Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its
> light-design value in the section polars used here, while specific hover power changes by one percent
> and the Bill 3 ratio by 5 to 14 percent.** The flatness of Bill 3 is imposed by a sizing rule; the finding is that Bill 2 moved anyway,
> by more than the Bill 3 ratio at every point in the heavy interval and under either engine margin.
> **Within this model, the two are therefore not one quantity under two names.**
>
> **Bill 1 is not tested**, for the reason given above, and nothing here should be read as showing
> that it separates from the other two — or as showing that it does not.
>
> **And the evidence is one pair of design points, computed by one method, with the Bill 2 result
> resting on a section-drag model at low Reynolds number.** It is consistent with the separability
> Section 2 asserts; it is not a verification of separability as a general property, which a single
> instantiation cannot supply.
>
> ### Two costs that scale does not relieve
>
> **The cruise-efficiency gap under fixed pitch does not close with size; it widens slightly.**
> Computed at each reference design's cruise thrust, a nose-pair blade that meets the hover requirement
> delivers a cruise efficiency 14.6 to 21.0 percent below the 0.80 assumed at the light design and
> **16.4 to 22.9 percent below it at the heavy one.** As in Section 11, no variable-pitch counterfactual
> was computed, so this is not a measure of what refusing the hub costs.
>
> **The transition is where the square–cube relation is paid in full.** ⟦The moment for a fixed rotation time grows as mL².⟧ **Rotating the heavy design in the light design's two seconds would
> demand about 220 kW from the tip propellers — roughly the whole of hover power**, which is not
> available. At 5.1 seconds, the heavy design's rotation time, the demand falls to about 13 kW, 6
> percent of hover power. **A larger aircraft of this type turns more slowly, and must.**
>
> ### Why this section sits between the ledger and the contracts
>
> If the three charges were one quantity, a single
> number could rank architectures whatever weight each charge was given. **Because at least two of them
> are not locked together, a comparison of architectures cannot in general be reduced to a number that
> does not depend on how the charges are weighed: where one architecture pays less of one charge and
> more of another, the ranking depends on the weighting.** The argument requires only two charges that
> are not locked together; the third need not be shown separate for the conclusion to hold.
>
> Section 13 examines what the choice of sizing contract does to a ranking, on the light closures of
> Section 10 only.

## 5. Step 13 — the first draft (deletion only)

**Dependency map.** Step 2's prediction is tested here; Step 9's fourth row and Step 15 state the refusal this section
supports; Step 11's common airframe and avionics fractions and Step 14's common store (3.6 percent) are its basis.
**Fourteen protected sentences** are in it.

**Result: 2 398 → 2 117 words (−12 %).** That is small, and honestly so: most of Step 13 is limits, and fourteen of its
sentences are protected. **The one judgment:** the sentence that applied the framework's rule to *"the fourth row of
Section 9"* leaves; the refusal's home is Section 9 (and Section 15), and *"no range claim is made against the tilting
family in either direction"* stays here. Everything that leaves goes to Supplement S13 verbatim. **Every change, before
and after:**

**13.1 — before:**

> - **Fixed fuel fraction.** Every architecture carries sixteen percent of its own take-off mass as
>   fuel. **Take-off mass cancels from range**, which is then set by L/D and the chain alone. A
>   heavier architecture shows its mass in the take-off-mass column and nowhere in the range column.
> - **Fixed fuel mass.** Every architecture carries the fuel this configuration carries at the same
>   closure — 8.4 to 9.2 kg. **Range is divided by take-off mass**, so a heavier aircraft flies the
>   same fuel less far.
> - **Fixed take-off mass and payload.** Every architecture is held to this configuration's closed
>   mass and its 13 kg payload. **Fuel is what remains after the empty mass**, so every kilogram of
>   architecture-specific hardware is a kilogram of fuel not carried.

**After:**

> - **Fixed fuel fraction.** Every architecture carries sixteen percent of its own take-off mass as
>   fuel. **Take-off mass cancels from range**, which is then set by L/D and the chain alone.
> - **Fixed fuel mass.** Every architecture carries the fuel this configuration carries at the same
>   closure — 8.4 to 9.2 kg. **Range is divided by take-off mass**, so a heavier aircraft flies the
>   same fuel less far.
> - **Fixed take-off mass and payload.** Every architecture is held to this configuration's closed
>   mass and its 13 kg payload. **Fuel is what remains after the empty mass**, so every kilogram of
>   architecture-specific hardware is a kilogram of fuel not carried.

**13.2 — before:**

> **Holding Bill 3 common is a choice of question, and it has a direction.** It is made so that the
> contract can be seen acting on a mass difference against a cruise-efficiency difference; it is not a
> claim that those families would use this power system, and the tilting family as Section 2 describes
> it has no store at all. **The choice runs against this configuration.** Given no buffer and an engine
> rated to deliver the hover demand through the generator, the power electronics and the machines
> instead, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off
> mass, and under a fixed fuel mass falls 38 to 47 percent behind; the tilt bound does not close under a
> fixed take-off mass. **Under a fixed fuel fraction the tilt bound closes at 520 kg — about ten times
> this configuration's mass — with its range lead unchanged at 103 to 141 percent**: the first
> contract's blindness to mass, made visible. **That comparison is not used**, because it would set
> competitors without a store against this configuration with one — a buffer of 3.6 percent whose
> feasibility is the item Section 14 examines. Whatever that store turns out to cost, holding it common
> charges all three the same assumption.

**After:**

> **Holding Bill 3 common is a choice of question, and it has a direction.** It is made so that the
> contract can be seen acting on a mass difference against a cruise-efficiency difference; it is not a
> claim that those families would use this power system, and the tilting family as Section 2 describes
> it has no store at all. **The choice runs against this configuration.** Given no buffer and an engine
> rated to deliver the hover demand through the generator, the power electronics and the machines
> instead, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off
> mass, and under a fixed fuel mass falls 38 to 47 percent behind; the tilt bound does not close under a
> fixed take-off mass. **That comparison is not used**, because it would set
> competitors without a store against this configuration with one — a buffer of 3.6 percent whose
> feasibility is the item Section 14 examines. Whatever that store turns out to cost, holding it common
> charges all three the same assumption.

**13.3 — before:**

> - **Drag.** All three share the clean airframe at each end of the drag bracket. This configuration
>   carries its exposed frames and free-wheeling rotors, as in Sections 10 and 11. The lift-plus-cruise
>   layout carries the ratio measured in the wind-tunnel campaign quoted in Section 2 — maximum
>   lift-to-drag ratio about 17 clean and about 13 with the lift hardware installed and its propellers
>   locked parallel to the flow — **transferred from a different airframe**, and assuming lift rotors
>   stopped and aligned in cruise, which takes an indexing mechanism (Section 7) whose mass is not
>   separately charged. **The tilting layout carries no cruise drag penalty at all.** That is an
>   idealisation in its favour, and it is deliberate: it makes the tilt row a bound.
> - **Propeller efficiency.** This configuration uses the computed 0.632 and 0.683 of Section 10. The
>   other two use 0.80 — the lift-plus-cruise layout because its cruise propeller does nothing else,
>   the tilting layout because it has a variable-pitch hub. **Both are assumed, not computed**, and the
>   asymmetry runs against this configuration; it is tested below.
> - **Mass.** The lift-plus-cruise layout carries a lift group of 10 percent of take-off mass and the
>   tilting layout a tilt mechanism of 5 percent. **Neither figure is measured.** The first turns out to
>   decide the sign of one result, and it is varied below.

**After:**

> - **Drag.** All three share the clean airframe at each end of the drag bracket. This configuration
>   carries its exposed frames and free-wheeling rotors, as in Sections 10 and 11. The lift-plus-cruise
>   layout carries the ratio measured in the wind-tunnel campaign quoted in Section 2 — maximum
>   lift-to-drag ratio about 17 clean and about 13 with the lift hardware installed and its propellers
>   locked parallel to the flow — **transferred from a different airframe**, and assuming lift rotors
>   stopped and aligned in cruise, which takes an indexing mechanism (Section 7) whose mass is not
>   separately charged. **The tilting layout carries no cruise drag penalty at all.** That is an
>   idealisation in its favour, and it is deliberate: it makes the tilt row a bound.
> - **Propeller efficiency.** This configuration uses the computed 0.632 and 0.683 of Section 10. The
>   other two use 0.80. **Both are assumed, not computed**, and the
>   asymmetry runs against this configuration; it is tested below.
> - **Mass.** The lift-plus-cruise layout carries a lift group of 10 percent of take-off mass and the
>   tilting layout a tilt mechanism of 5 percent. **Neither figure is measured.** The first turns out to
>   decide the sign of one result, and it is varied below.

**13.4 — before:**

> **There is a trade, but it is lopsided.** The tilting layout closes 0.5 to 5.4 percent heavier than
> this configuration, and it cruises at the clean airframe's lift-to-drag ratio with a propeller at 0.80:
> it is credited with no nacelle drag, no pivot fairing, and no penalty for flying hover-sized rotors as
> cruise propellers. **Even the contract that weights mass most** — a fixed take-off mass, in which every
> kilogram of tilt mechanism is a kilogram of fuel not carried — **leaves the bound's margin at 93 to 130 percent.**
> The contract moves the comparison, as Section 12 says it must where there is a trade; none of the
> three moves it far enough to matter. A ranking against a competitor modelled as a bound is not a
> ranking, and **no range claim is made against the tilting family in either direction.**
> The claim this paper makes against that family is about mechanism (Sections 7 and 8), and nothing in
> this section bears on it.

**After:**

> **There is a trade, but it is lopsided.** The tilting layout closes 0.5 to 5.4 percent heavier than
> this configuration, and it cruises at the clean airframe's lift-to-drag ratio with a propeller at 0.80. **Even the contract that weights mass most** — a fixed take-off mass, in which every
> kilogram of tilt mechanism is a kilogram of fuel not carried — **leaves the bound's margin at 93 to 130 percent.**
> The contract moves the comparison, as Section 12 says it must where there is a trade; none of the
> three moves it far enough to matter. A ranking against a competitor modelled as a bound is not a
> ranking, and **no range claim is made against the tilting family in either direction.**
> The claim this paper makes against that family is about mechanism (Sections 7 and 8), and nothing in
> this section bears on it.

**13.5 — before:**

> **The size of the shift behaves the same way.** It barely moves when the propeller or drag basis is
> changed — 65 to 77 points across those cases — because those asymmetries enter all three contracts
> alike. It moves a great deal with the lift group, from 14 to 134 points, because the shift *is* the
> mass difference being counted. **What is robust is that the shift exists and runs toward the lighter
> aircraft; its size is the size of the mass difference.**

**After:**

> **The size of the shift behaves the same way.** **What is robust is that the shift exists and runs toward the lighter
> aircraft; its size is the size of the mass difference.**

**13.6 — before:**

> **Carry the audit, for every column.** State each charge in its own currency — kilograms, drag
> counts, installed kilowatts — before any aggregate, and state the basis of the comparison with its
> asymmetries and their directions. An aggregate that arrives without its parts cannot be checked, and
> the parts are where the comparison is decided. **This paper meets that for its own column** (Section
> 11) **and not for the competitors'**, whose kilograms and drag counts here are parameters and transferred
> ratios rather than an audit — which is one more reason no ranking against them is offered.
>
> **Name the contract.** A comparison of architectures is a comparison under a contract. The contract is
> chosen by the mission rather than by the analyst, and a comparison that does not state one has chosen
> one silently.
>
> **Refuse the bare ranking.** Report an ordering only with the contract it was computed under, and,
> where its sign depends on an unmeasured quantity, with that quantity named. An ordering that holds
> under every contract examined may be reported as such — that is a stronger statement than any one
> contract gives, and it still names the contracts. Applied to this paper's
> own numbers, the rule is the fourth row of Section 9: **no range claim is made against lift-plus-cruise
> or tilting layouts**, because the ordering against the first depends on the contract and on the
> competitor's lift-group mass, and the ordering against the second is against a bound.

**After:**

> **Carry the audit, for every column.** State each charge in its own currency — kilograms, drag
> counts, installed kilowatts — before any aggregate, and state the basis of the comparison with its
> asymmetries and their directions. **This paper meets that for its own column** (Section
> 11) **and not for the competitors'**, whose kilograms and drag counts here are parameters and transferred
> ratios rather than an audit.
>
> **Name the contract.** A comparison of architectures is a comparison under a contract.
>
> **Refuse the bare ranking.** Report an ordering only with the contract it was computed under, and,
> where its sign depends on an unmeasured quantity, with that quantity named.

**13.7 — before:**

> **And nothing here ranks architectures for a mission.** Which contract a mission implies, and which
> architecture it then favours, is the user's question. What this section establishes is narrower: **the
> same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by
> tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property
> of the architectures alone.
>

**After:**

> **And nothing here ranks architectures for a mission.** Which contract a mission implies, and which
> architecture it then favours, is the user's question. What this section establishes is narrower: **the
> same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by
> tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property
> of the architectures alone.

**Further cuts need rewrites.** Grok's specification was *"the three-contract table plus the tilt bound"*. Which
paragraphs would you replace, and with what sentence?

## 6. Your new proposals — side by side, with my position

| Proposal | By | My position |
|---|---|---|
| Figure-to-claim audit: geometry, motion arrows, labels, numbers — each checked like prose | ChatGPT | **Yes** — it is the v7 rule made operational |
| Cross-references checked from the destination's side before a compression closes | ChatGPT | **Yes** — the generator now refuses unresolved references; the conceptual check is ours, at confirmation |
| Rebuilt Figure 11: subtitle = Step 7's sentence; a rotation but no zero-loss claim; **no landing panel** | Grok P8 | **Yes** — each follows from a protected sentence (Steps 7, 10, 5) |
| Figures for the four-axis table, the scale comparison, the energy-store gap | DeepSeek | **Only as replacements**, and only after the calculations are drafted; the four-axis table stays for now |
| Step 11's bounding sentence split into two if it runs long | Qwen | **Yes, when Step 11 is drafted** |

## 7. The pace, honestly

The body is **26 852 words** (Round 67: 27 689). Deletion alone takes 12 to 28 percent from a calculation step, because
the limits stay whole. **The rest is in rewrites like Section 4's**, which is why each needs your eye. If Section 4 passes,
Step 12 will have gone from 2 973 to 1 873 in two rounds.

## 8. What I am asking

1. **Confirm** Section 1 (Step 12 applied as shown; S12) and Section 2 (the joins).
2. **Section 3:** DeepSeek's, Grok's, or as it is.
3. **Section 4:** veto or accept each of R1–R5, D1, D2 — quoting the sentence if you veto.
4. **Section 5:** veto on a dropped number, a lost function or a stronger predicate; then your further cuts, as rewrites.
5. **Section 6:** vote.
6. **New proposals**, as always.

**Sources.** None of this needs a source.
