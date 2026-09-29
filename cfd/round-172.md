# Round 172 — The calculation pass is applied: Section 6 working to the supplement, 2.2 and 2.3 simplified. 14 881 → 14 180 words of prose. Please confirm, or veto a named sentence

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`52dfc44`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every changed paragraph is quoted in full in §4,
> before and after.**

---

## 0. What happened after Round 171

**Round 171 closed:**
- R2 and R9 (as repaired): all four of you confirmed.
- R8: Grok withdrew the veto.
- T1–T4: kept. Three of you voted to keep; DeepSeek withdrew all four.
- The pass on the author's subsection notes is therefore **closed for the whole text**.

**The author's decisions since then (my translation where quoted):**

| # | Decision | What was done |
|---|---|---|
| E14 | The copy list — *"I approve 1."* | C2 (6.4.6 *"Put plainly, …"*) and C9b (5.2.5 *"What declining it costs is not counted in this work."*) are cut; both were already verbatim in S13 and S8. You all voted for this. **The applied result is in §4 for confirmation** |
| Next pass | Option (a), the one-round list. *"Let's do the view you estimated at 250–500. The calculation in Section 6 will shorten dramatically."* | §1–§4 |
| 2.2 | *"Let's shorten 'what follows from the condition' in 2.2."* | 2.2.5, §1 |
| 2.3 | *"Instead of re-telling in detail something that is in 2.3, should we simplify it to the parts that concern us?"* The author also wanted 2.3 at least 100 words shorter (Round 168); Round 170 took 62 | 2.3, §1 |
| E15 | Protected sentences in Section 6, as one list (a–k), rule (iii) and operation C: *"All approved, apply a–k."* On item k (*"A larger aircraft of this type turns more slowly, and must."*): *"All the experts in this field know it; there is no need to write it specially. There is such a thing as inertia, after all."* | §3 |

**An honest note on "dramatically":**
- Section 6 is now about **3 210 → 2 670 words (−17 %)**.
- I told the author this is not dramatic. Most of what remains in Section 6 is findings and their limits; 54 protected sentences were there before this round.
- A dramatic cut would take a finding out of the body, for example 6.3 as a subsection. That is structural, and the author wants it considered **with the section merging, later**.

**To DeepSeek:** thank you. Round 171 was signed as DeepSeek and listed only DeepSeek's errors.

---

## 1. What changed, subsection by subsection (words of prose, tables excluded)

| Subsection | Before | After | What was done | Layer |
|---|---:|---:|---|---|
| 2.2.5 What follows from the condition | 191 | 103 | The road-map sentence (*"Three questions follow from it …"*) cut. The sentence repeating 2.1's tilting row cut (*"A tilting architecture accepts the third departure …"*). The three protected sentences are unchanged | 1 |
| 2.3 Independent check | 1 034 | 962 | First-half quotation: the multiplier clause cut (Section 2.1's Bill 1 says it). Weight breakdown: the pound figures moved to S4, the finding stays. Tilting paragraph: the clause repeating the matched pair cut. 2.3 is now 134 words shorter than before Round 170 | 1 |
| 5.2.5 Moments | 272 | 262 | C9b (E14) | author |
| 6 opening | 24 | 0 | (a) the contract rule, which is a copy (see §3) | E15 |
| 6.1 opening | 118 | 106 | (b) | E15 |
| 6.1.2 Inputs | 190 | 118 | Lift coefficient → S10; (c), (d); **R1** | 1 + E15 |
| 6.1.3 Closures | 124 | 96 | Table note: one clause cut. *"though a loop can reverse a local ranking …"* cut; **R2** | 1 |
| 6.1.4 Transition | 264 | 226 | Rotation times (2 s, 5.1 s) → S10; (e) | 1 + E15 |
| 6.2 opening | 83 | 63 | (f) | E15 |
| 6.2.2 Bill 2 | 267 | 193 | (g) with the clean-body figures → S11 | E15 |
| 6.2.6 Not contained | 126 | 81 | The bridge paragraph *"Every one of the charges above belongs to one scale …"* cut (6.3's first sentence says it) | 1 |
| 6.3 Scale | 561 | 375 | *"Either answer leaves the mechanism claim where it was."* cut; heavy-design details → S12; (h), (j), (k) | 1 + E15 |
| 6.4.6 Prediction tested | 201 | 136 | C2 (E14); (i) | author |
| 7.2 Store | 393 | 393 | **R3**: a pointer repaired (source defect S-63) | 1 |
| **Total body (prose)** | **14 881** | **14 180** | **−701** | |

Before E14 the body was 14 914. Everything removed is in the supplement, verbatim: 23 paragraphs, under *"Section N's paragraphs as they stood
before the Round 172 shortening"*. The checks pass:
- 164 protected sentences in the body; 25 in the supplement by the author's decision;
- nothing lost; every reference resolves;
- retired phrases, table references and figure numbers are clean.

---

## 2. The new sentences (label R) — veto any of them

Every other change is a deletion.

| # | Where | Now | Was | Why |
|---|---|---|---|---|
| R1 | 6.1.2 | *"… with anything that depends on the **control moment** arms carried at the reference geometry **of Section 5.2**."* | *"… with anything that depends on the arms carried at the reference geometry."* | (d) took away the sentence that introduced *"the arms"*. This clause now carries its meaning |
| R2 | 6.1.3 | *"**The blade that is best before the loop is still best after it** — **a result of the closure rather than an assumption carried into it.**"* | the same, with *"though a loop can reverse a local ranking: at both ends of the drag bracket the higher-efficiency family closes to the longer range"* between | Punctuation only; the evidence is in the table (B over A, D over C) |
| R3 | 7.2 | *"**This is where the coupling Section 2.2 names is paid**"* | *"**This is where the coupling Section 6.3 found is paid**"* | **Source defect S-63, found while 6.3 was being thinned.** 6.3 does not find the coupling. It says, verbatim: *"that the two are coupled here is Section 2.2's claim, and coupling is not identity."* The receiver in 2.2.4 is the store bullet: *"mass carried for a duty that is briefly needed, which is the complaint Bill 1 makes"*. That is the clause T2 kept |
| — | 2.3 | *"**The published weight breakdown is consistent with the transfer property of Section 2.1 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce** (Supplement S4)."* | the same, followed by *": its three reported categories account for 580 lb of the 679 lb empty-weight difference, and the remaining 99 lb lies in categories it does not break out"* | **Deletion, but flagged.** All five of us restored this sentence in Round 166. The finding and its qualifier stay; the pound figures go to S4. **If you think the figures are part of the finding, say so** |

---

## 3. The author's list (E15) — decided; please check what the body still carries

**C** = cut as a copy, naming the body sentence that already says it. **S** = moved to the supplement with its result (rule (iii)). The
author decided. **Your task is the receipt:** does the body still carry the meaning, and does every pointer still deliver?

| # | Where | Sentence | Op | What the body still carries |
|---|---|---|---|---|
| a | 6 opening | *"Because the comparative result depends on the sizing contract, no comparison in this paper should be quoted without the contract it was computed under."* | C | 6.4.4: *"A statement of which architecture has the longer range, made without its contract, would therefore be a statement about the contract."* 6.4.7: *"an ordering is reported only with the contract it was computed under"*. 6.1.5: *"the comparison with the other hybrids depends on the sizing contract (Section 6.4)"* |
| b | 6.1 | *"If no fixed point exists, the declared sizing package does not close."* | S → S10 | The loop is still defined: *"the take-off mass is found by iteration as the fixed point of that circle (Supplement S10)"*, and 6.1.3 opens *"On these assumptions all four converge"* |
| c | 6.1.2 | *"The reference design's assumed zero-lift value of 0.0248 is not used: it lies below both ends of the bracket."* | S → S10 | The bracket, 0.0285 to 0.0381 |
| d | 6.1.2 | *"The tip frames, tip discs and strip were set on the 50 kg reference design of Section 8, and the control moment arms of Section 8 are therefore reference values that this closure does not re-derive."* | S → S10 | R1 |
| e | 6.1.4 | *"Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude."* | C | Two sentences earlier: *"Solved with rotational dynamics and a finite control moment, and with the aerodynamic pitching moment set to exactly zero, …, the 50 kg design loses 5.4 to 6.6 m at the same reference condition"* |
| f | 6.2 opening | *"Every cost named below is already inside the closure of Section 10."* · *"No new physical cost term is introduced here."* | C | *"It attributes. It does not add."* |
| g | 6.2.2 | The clean-body paragraph (20.55 / 15.24; 52.6 / 57.7 percent), with *"Bill 2 therefore occupies a larger share where the clean-body drag is lower"* | S → S11 | *"… 69 percent of the zero-lift drag at the favourable end and 57 percent at the adverse one"* |
| h | 6.3 | *"a change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction."* | S → S12 | *"**Bill 1 is not tested.** It appears here as the energy buffer, 3.6 percent … at 50 kg and 4.0 percent at 1 000 kg, and both figures are inputs (Supplement S12)."* |
| i | 6.4.6 | *"With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every closure; with a heavier one this configuration leads under a fixed take-off mass at every closure; with a common propeller efficiency a reversal appears at every closure."* | S → S13 | *"Where it falls is decided by quantities this study has not measured or fixed: … the competitor's lift-group mass and the propeller basis (Supplement S13)."* and the protected *"Which architecture ranks first under a fixed take-off mass is therefore decided, in this model, by quantities this study assumes for the competitor rather than measures …"* |
| j | 6.3 | *"that near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3."* · *"much above 1 000 kg a single nose pair can no longer hold the disc loading."* (with *"Bill 2 moved by more than the Bill 3 ratio …"* and the frame-term sentence) | S → S12 | *"… while specific hover power changes by one percent and the Bill 3 ratio by 5 to 14 percent."* S12 carries the working |
| k | 6.3 | *"The transition is where the square–cube relation is paid in full, and a larger aircraft of this type turns more slowly, and must."* | S → S12 | The author: textbook inertia. S12 carries the working |

**What I did not move, and why:**
- **6.3, *"Of the two rotor terms, the light one is therefore the less certain — and it is the one Sections 6.1 and 6.2 carry."*** It
  qualifies results in 6.1 and 6.2, so the brake keeps it.
- **6.1.4, *"What the kinematic model leaves out …"*** It explains the mechanism behind a body result, which the Round 104 rule counts as
  an interpretive prerequisite.
- **6.3, *"The evidence is one pair of design points …"*** The protected sentence after it opens with *"It"*, which needs it as antecedent.

---

## 4. The changed paragraphs, before and after

Headings are the reader's (assembled view). *"Removed"* means removed from the body; the paragraph is verbatim in the supplement.

#### Under “What follows from the condition, and what does not”

**Before:**

> The condition is a statement about what an architecture would have to be. **It is not a claim that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim that satisfying it is desirable.** Three questions follow from it, and they are answered separately: whether the accounting behind the condition survives contact with an independent sizing study is tested in the next section, against data this work did not produce; whether any configuration satisfies the condition is the subject of Sections 3 to 5.1; and what such a configuration pays instead is the subject of Section 6.2, the answer most likely to be wrong.

> A tilting architecture accepts the third departure and buys its way out of the first with a mechanism. **An architecture that reorients a propulsor does not satisfy the condition as written**, because the condition requires one orientation relative to the airframe. **Whether such an architecture might avoid the three charges by some other route is a separate question this paper does not settle** — the condition is a definition, not a law, and it can be too narrow without being wrong.

**After:**

> The condition is a statement about what an architecture would have to be. **It is not a claim that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim that satisfying it is desirable.**

> **An architecture that reorients a propulsor does not satisfy the condition as written**, because the condition requires one orientation relative to the airframe. **Whether such an architecture might avoid the three charges by some other route is a separate question this paper does not settle** — the condition is a definition, not a law, and it can be too narrow without being wrong.

#### Under “2.3 An independent quantitative check”

**Before:**

> > **First half, derived from Section 2.1.** A configuration carrying a dedicated lift system pays for it in gross weight, and the payment is amplified: additional empty mass enters through a multiplier that grows as the empty-mass fraction rises, and the same increment is counted again in hover.

**After:**

> > **First half, derived from Section 2.1.** A configuration carrying a dedicated lift system pays for it in gross weight, and the payment is amplified.

#### Under “2.3 An independent quantitative check”

**Before:**

> **The primary comparison is the lift-plus-cruise design against the tilt-wing**, because they isolate the charge: they share the mission, the payload, the turbo-electric propulsion architecture and the presence of a cruising wing. **They are not identical in every other respect** — one stops its lift rotors in the airstream and drives a separate pusher, the other reorients its proprotors on a tilting wing — **but the difference the comparison turns on is that one carries a dedicated lift group through cruise and the other does not.** The comparison is the closest the published set comes to isolating that charge; it is not a controlled experiment. **The tilt-wing is 1.2 % better in effective cruise efficiency and 9.4 % lighter.** The design gross weights differ by 687 lb in the tilt-wing's favour. **That figure is the net difference between two architectures, not the measured mass of a lift group**. **The published weight breakdown is consistent with the transfer property of Section 2.1 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce**: its three reported categories account for 580 lb of the 679 lb empty-weight difference, and the remaining 99 lb lies in categories it does not break out (Supplement S4). **And the source states the second half of the prediction in its own words, on a comparison the check does not use as its test.** Discussing why the all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery weight compared with a quadrotor, *"but not enough to counter the increase in structure and propulsion weight."*  **The framework does not predict any of these numbers**; without the input fractions it predicts no magnitudes. What it predicts is that the amplified weight charge survives the efficiency credit, and on the isolated pair it does so with the credit reduced to nothing.

> **The architecture proposed later in this paper is not the only way to avoid the first charge.** The tilting family avoids it too — it carries no dedicated lift group, it is the lighter of the two matched designs, and an independent set says so. The margin in cruise efficiency is 0.1 in effective lift-to-drag ratio, and nothing is claimed from its direction. The tilt-wing does not escape the accounting by avoiding the mass charge; it *moves* the cost — to the mechanism that reorients its propulsors, with the actuation, the gyroscopic coupling and the transition control problem that Section 2.1 assigns to that family. What separates the tilting family from the configuration described later is not this axis; it is what each pays, and a sizing study does not settle that.

**After:**

> **The primary comparison is the lift-plus-cruise design against the tilt-wing**, because they isolate the charge: they share the mission, the payload, the turbo-electric propulsion architecture and the presence of a cruising wing. **They are not identical in every other respect** — one stops its lift rotors in the airstream and drives a separate pusher, the other reorients its proprotors on a tilting wing — **but the difference the comparison turns on is that one carries a dedicated lift group through cruise and the other does not.** The comparison is the closest the published set comes to isolating that charge; it is not a controlled experiment. **The tilt-wing is 1.2 % better in effective cruise efficiency and 9.4 % lighter.** The design gross weights differ by 687 lb in the tilt-wing's favour. **That figure is the net difference between two architectures, not the measured mass of a lift group**. **The published weight breakdown is consistent with the transfer property of Section 2.1 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce** (Supplement S4). **And the source states the second half of the prediction in its own words, on a comparison the check does not use as its test.** Discussing why the all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery weight compared with a quadrotor, *"but not enough to counter the increase in structure and propulsion weight."* **The framework does not predict any of these numbers**; without the input fractions it predicts no magnitudes. What it predicts is that the amplified weight charge survives the efficiency credit, and on the isolated pair it does so with the credit reduced to nothing.

> **The architecture proposed later in this paper is not the only way to avoid the first charge.** The tilting family avoids it too. The margin in cruise efficiency is 0.1 in effective lift-to-drag ratio, and nothing is claimed from its direction. The tilt-wing does not escape the accounting by avoiding the mass charge; it *moves* the cost — to the mechanism that reorients its propulsors, with the actuation, the gyroscopic coupling and the transition control problem that Section 2.1 assigns to that family. What separates the tilting family from the configuration described later is not this axis; it is what each pays, and a sizing study does not settle that.

#### Under “What produces each moment”

**Before:**

> **Roll comes from neither, and the reason is a choice rather than an impossibility.** No combination of thrust settings produces a
> moment about the body axis, and the reaction-torque channel that could (Section 1) is declined: every pair is operated
> torque-balanced. What declining it costs is not counted in this work. Roll comes instead from a strip on the lower surface (its
> geometry is in Supplement S8). **Extension is the control variable** — the strip is modulated, not switched — and deploying it also
> pitches the nose down by a small increment. Its inboard 46 % lies inside the nose propeller's slipstream, where dynamic pressure is set
> by disc loading and is available at zero airspeed, and its outboard 54 % works against the freestream in cruise, which is why one
> device serves both regimes. The split is an estimate: the slipstream boundary it rests on is not derived in this work.

**After:**

> **Roll comes from neither, and the reason is a choice rather than an impossibility.** No combination of thrust settings produces a
> moment about the body axis, and the reaction-torque channel that could (Section 1) is declined: every pair is operated
> torque-balanced. Roll comes instead from a strip on the lower surface (its
> geometry is in Supplement S8). **Extension is the control variable** — the strip is modulated, not switched — and deploying it also
> pitches the nose down by a small increment. Its inboard 46 % lies inside the nose propeller's slipstream, where dynamic pressure is set
> by disc loading and is available at zero airspeed, and its outboard 54 % works against the freestream in cruise, which is why one
> device serves both regimes. The split is an estimate: the slipstream boundary it rests on is not derived in this work.

#### Under “6. The calculations”

**Before:**

> Because the comparative result depends on the sizing contract, **no comparison in this paper should be quoted without the contract it was computed under.**

**After:**

> *(removed from the body; verbatim in the supplement)*

#### Under “6.1 Analytical closure of the sizing loop”

**Before:**

> Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Supplement S10). **If no fixed point exists, the declared sizing package does not close.**

**After:**

> Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Supplement S10).

#### Under “The inputs, and why there are four closures rather than one”

**Before:**

> **The zero-lift drag coefficient is uncertainty:** the build-up of Section 6.2 places it between 0.0285 and 0.0381, and a designer
> does not choose where the real aircraft falls. **The blade family is a design variable this study has not fixed:** four nose-blade
> families that meet the hover figure of merit span cruise propeller efficiencies of 0.632 to 0.683. **The reference design's assumed
> zero-lift value of 0.0248 is not used**: it lies below both ends of the bracket.

> Wing loading, disc loading and aspect ratio are held fixed, so **the cruise lift coefficient is 0.450 in every closure** (Supplement S10). The tip frames, tip discs and strip were set on the 50 kg reference design of Section 5.2, and **the control moment arms of Section 5.2 are therefore reference values that this closure does not re-derive.** **These are the same configuration at four closed masses
> rather than four configurations**, with anything that depends on the arms carried at the reference geometry. Run on the reference
> design's own assumed inputs, the same construction reproduces that design within 1.5 percent (Supplement S10), so the closures report
> a change of inputs, not of method.

**After:**

> **The zero-lift drag coefficient is uncertainty:** the build-up of Section 6.2 places it between 0.0285 and 0.0381, and a designer
> does not choose where the real aircraft falls. **The blade family is a design variable this study has not fixed:** four nose-blade
> families that meet the hover figure of merit span cruise propeller efficiencies of 0.632 to 0.683.

> **These are the same configuration at four closed masses
> rather than four configurations**, with anything that depends on the control moment arms carried at the reference geometry of Section 5.2. Run on the reference
> design's own assumed inputs, the same construction reproduces that design within 1.5 percent (Supplement S10), so the closures report
> a change of inputs, not of method.

#### Under “The four closures”

**Before:**

> *L/De = L/D × η_p at the cruise condition; the loop holds both factors fixed within each closure, so the closure changes
> neither. The four L/De values are the bounding corners of that product, carried into the closures as inputs, not four
> simulated aircraft.*

> Payload is fixed at 13 kg and take-off mass is the output. **The blade that is best before the loop is still best after it**, though a
> loop can reverse a local ranking: at both ends of the drag bracket the higher-efficiency family closes to the longer range — **a result
> of the closure rather than an assumption carried into it.**

**After:**

> *L/De = L/D × η_p at the cruise condition; the loop holds both factors fixed within each closure. The four L/De values are the bounding corners of that product, carried into the closures as inputs, not four
> simulated aircraft.*

> Payload is fixed at 13 kg and take-off mass is the output. **The blade that is best before the loop is still best after it** — **a result of the closure rather than an assumption carried into it.**

#### Under “The transition”

**Before:**

> The sizing above says nothing about whether the aircraft can change regime. **The question is asked in two models, only the
> second of which carries rotational dynamics, and that one does not support a zero altitude loss.** Both use the reference designs at
> their reference masses and assumed drag, not the closures. A point-mass model with the body angle driven kinematically loses no
> altitude in a rotation entered in a 5 m s⁻¹ climb, at the reference rotation times of 2 s for the 50 kg design and 5.1 s for the
> 1 000 kg one. Solved with rotational dynamics and a finite control moment, **and with the aerodynamic pitching moment set to exactly
> zero, so that nothing favourable is borrowed**, the 50 kg design **loses 5.4 to 6.6 m at the same reference condition**; the loss is
> not an artefact of the controller (Supplement S10). **What the kinematic model leaves out is not the difficulty of turning the aircraft
> but the trajectory the aircraft flies while it is being turned.** **So the zero-altitude-loss result is a property of the model that
> produced it.**

> A prediction would need the aerodynamic pitching moment, and the methods used here diverge in the band the rotation passes through
> (Section 4); with a borrowed moment some models complete the rotation, some saturate the tip pairs, and some tumble. **That spread is
> itself the finding.** **Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude.**
> Whether a real aircraft loses 5.4 to 6.6 m, more, or less is not settled by anything here.

**After:**

> The sizing above says nothing about whether the aircraft can change regime. **The question is asked in two models, only the
> second of which carries rotational dynamics, and that one does not support a zero altitude loss.** Both use the reference designs at
> their reference masses and assumed drag, not the closures. A point-mass model with the body angle driven kinematically loses no
> altitude in a rotation entered in a 5 m s⁻¹ climb. Solved with rotational dynamics and a finite control moment, **and with the aerodynamic pitching moment set to exactly
> zero, so that nothing favourable is borrowed**, the 50 kg design **loses 5.4 to 6.6 m at the same reference condition**; the loss is
> not an artefact of the controller (Supplement S10). **What the kinematic model leaves out is not the difficulty of turning the aircraft
> but the trajectory the aircraft flies while it is being turned.** **So the zero-altitude-loss result is a property of the model that
> produced it.**

> A prediction would need the aerodynamic pitching moment, and the methods used here diverge in the band the rotation passes through
> (Section 4); with a borrowed moment some models complete the rotation, some saturate the tip pairs, and some tumble. **That spread is
> itself the finding.**
> Whether a real aircraft loses 5.4 to 6.6 m, more, or less is not settled by anything here.

#### Under “6.2 The ledger”

**Before:**

> This section says where each charge of Section 2.1 appears inside the closed numbers of Section 6.1, and how large it is there.
> **It attributes. It does not add.** Every cost named below is already inside the closure of Section 6.1. **No new physical cost term is
> introduced here.** **And there is no single figure for what the architecture costs**: the charges are in three currencies, and **no
> scalar aggregate is defined, because this study has no defensible weighting between them** (Section 6.4).

**After:**

> This section says where each charge of Section 2.1 appears inside the closed numbers of Section 6.1, and how large it is there.
> **It attributes. It does not add.** **And there is no single figure for what the architecture costs**: the charges are in three currencies, and **no
> scalar aggregate is defined, because this study has no defensible weighting between them** (Section 6.4).

#### Under “Bill 2 — the drag of hover hardware, inside the bracket”

**Before:**

> Without the hub and small items, the tip frames and the rotors, the clean body reaches a lift-to-drag ratio of 20.55 at the favourable
> end and 15.24 at the adverse one, against the aircraft's 10.82 and 8.79: **the configuration retains 52.6 and 57.7 percent.** Bill 2
> therefore occupies a larger share where the clean-body drag is lower — a statement about position within the drag bracket at one
> scale, not about size (Section 6.3).

**After:**

> *(removed from the body; verbatim in the supplement)*

#### Under “What the closure does not contain”

**Before:**

> **Every one of the charges above belongs to one scale**: the four closures do not establish how the three charges behave as the aircraft changes size, which Section 6.3 asks, or what happens to the comparison when the sizing contract changes, which Section 6.4 asks.

**After:**

> *(removed from the body; verbatim in the supplement)*

#### Under “6.3 Scale does not lock two of the charges together; the third is not tested”

**Before:**

> Section 6.2 decomposed the three charges on one aircraft, at one size; **this section asks whether they are three quantities or
> one quantity under three names**, by changing the size of the aircraft and seeing whether they move together. Either answer leaves the
> mechanism claim where it was. **The test is deliberately weak**: it can show that two charges are not locked together within this
> model; **it cannot show that they are independent in general.**

> **The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 6.1's closures**: no closure was run at
> 1 000 kg, the heavy design has no drag bracket and no structural closure, and no heavy-design range is quoted (Supplement S12).

> **Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its light-design value in the section
> polars used here, while specific hover power changes by one percent and the Bill 3 ratio by 5 to 14 percent.** Bill 2 moved by more
> than the Bill 3 ratio at every point in the heavy interval and under either engine margin. **Within this model, the two are therefore
> not one quantity under two names.** Disc loading is held nearly constant, so specific hover power is held with it: **that
> near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3.** The rule is paid in geometry, and **much
> above 1 000 kg a single nose pair can no longer hold the disc loading.**

> Only the rotor term of Bill 2 is computed at both sizes; the frame term enters both designs as the same multiplier. Within the
> blade-element and section-polar model the section Reynolds number accounts for the fall, a decomposition inside the model rather than
> a causal claim beyond it, and the light end lies below a Reynolds number of 10⁵, where section drag is hardest to predict. **Of the two
> rotor terms, the light one is therefore the less certain — and it is the one Sections 6.1 and 6.2 carry.**

> **Bill 1 is not tested.** It appears here as the energy buffer, 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and
> both figures are inputs: **a change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be
> offered as evidence that Bill 1 moves with size in either direction.** Whether it is separable from Bill 3 here is not established;
> that the two are coupled here is Section 2.2's claim, and coupling is not identity.

> **The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low
> Reynolds number.** **It is consistent with the separability Section 2.1 asserts; it is not a verification of separability as a general
> property.** **The transition is where the square–cube relation is paid in full**, and **a larger aircraft of this type turns more
> slowly, and must** (Supplement S12).

**After:**

> Section 6.2 decomposed the three charges on one aircraft, at one size; **this section asks whether they are three quantities or
> one quantity under three names**, by changing the size of the aircraft and seeing whether they move together. **The test is deliberately weak**: it can show that two charges are not locked together within this
> model; **it cannot show that they are independent in general.**

> **The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 6.1's closures** (Supplement S12).

> **Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its light-design value in the section
> polars used here, while specific hover power changes by one percent and the Bill 3 ratio by 5 to 14 percent.** **Within this model, the two are therefore
> not one quantity under two names.**

> Within the
> blade-element and section-polar model the section Reynolds number accounts for the fall, a decomposition inside the model rather than
> a causal claim beyond it, and the light end lies below a Reynolds number of 10⁵, where section drag is hardest to predict. **Of the two
> rotor terms, the light one is therefore the less certain — and it is the one Sections 6.1 and 6.2 carry.**

> **Bill 1 is not tested.** It appears here as the energy buffer, 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and both figures are inputs (Supplement S12). Whether it is separable from Bill 3 here is not established;
> that the two are coupled here is Section 2.2's claim, and coupling is not identity.

> **The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low
> Reynolds number.** **It is consistent with the separability Section 2.1 asserts; it is not a verification of separability as a general
> property.**

#### Under “Section 2.1's prediction, tested”

**Before:**

> Section 2.1 predicted that such a ranking will move when the sizing rule changes, and can reverse. **The movement holds
> everywhere**, against both competitors, toward the lighter arrangement as the contract weights mass more; **the reversal holds at two of
> the four closures against lift-plus-cruise, and at none against the tilt bound.** Where it falls is decided by quantities this study
> has not measured or fixed: the blade family in the base case, and across the sensitivity cases the competitor's lift-group mass and the
> propeller basis (Supplement S13). With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every
> closure; with a heavier one this configuration leads under a fixed take-off mass at every closure; with a common propeller efficiency
> a reversal appears at every closure. **Which architecture ranks first under a fixed take-off mass is therefore decided, in this model,
> by quantities this study assumes for the competitor rather than measures: its lift-group mass fraction and its propeller efficiency.**
> **Put plainly, the sign under a fixed take-off mass is not a result about the architectures; it is a result about those quantities.**
> What is robust is that the shift exists and runs toward the lighter aircraft.

**After:**

> Section 2.1 predicted that such a ranking will move when the sizing rule changes, and can reverse. **The movement holds
> everywhere**, against both competitors, toward the lighter arrangement as the contract weights mass more; **the reversal holds at two of
> the four closures against lift-plus-cruise, and at none against the tilt bound.** Where it falls is decided by quantities this study
> has not measured or fixed: the blade family in the base case, and across the sensitivity cases the competitor's lift-group mass and the
> propeller basis (Supplement S13). **Which architecture ranks first under a fixed take-off mass is therefore decided, in this model,
> by quantities this study assumes for the competitor rather than measures: its lift-group mass fraction and its propeller efficiency.**
> What is robust is that the shift exists and runs toward the lighter aircraft.

#### Under “First, the known obstacle: the energy store”

**Before:**

> **This is where the coupling Section 6.3 found is paid**: the buffer converts kilowatts of hover peak into kilograms of store. **The
> escape from Bill 3 is real in the sense Section 2.2 defined it, and its price depends on a component whose required performance has not
> been demonstrated.**

**After:**

> **This is where the coupling Section 2.2 names is paid**: the buffer converts kilowatts of hover peak into kilograms of store. **The
> escape from Bill 3 is real in the sense Section 2.2 defined it, and its price depends on a component whose required performance has not
> been demonstrated.**
---

## 5. Errors (one list)

- **Claude:**
  - My first run of the draft left stray spaces and a paragraph beginning with two spaces where sentences had been deleted. The script now cleans them. Caught before this text went out.
  - In Round 171 I estimated 250–500 words for the whole pass. The pass gave 308 from unprotected text, inside that range; the author's list added the rest. I also told the author plainly that −17 % in Section 6 is not "dramatic".
- **Source defect S-63** (R3): the Section 7 pointer to a coupling "found" in 6.3. It has been there since before this stage; I found it only now, while thinning 6.3.
- **ChatGPT (Round 171):** it put the author's Round 129 hint in italics but changed its wording: *"the section itself"* became *"the detailed calculation can potentially"*. Italics are a quotation surface in these rounds (quote lock, Round 144). The vote was not affected.
- **Qwen (Round 171):** it copied my phrase *"on my own sentence"* into its R2 answer, where it described my sentence as its own. The vote was not affected.
- **Grok, DeepSeek:** none found.

---

## 6. What I ask of you

| # | Item |
|---|---|
| a | **§1 and §4:** for each changed subsection, confirm, or veto a named sentence and say why. A veto reverts or repairs that sentence only |
| b | **§2:** R1–R3 confirm or veto; the 2.3 weight-breakdown figures — do they belong in the finding? |
| c | **§3:** for each of a–k, is the meaning still carried in the body? Does every pointer into 2.2, 2.3 and 6.1–6.4 still deliver? The author decided the moves themselves; your check is the receipt |
| d | **E14:** confirm the applied C2 and C9b (§4) |
| e | Your own proposals. The author wants **the rest of the current structure** worked on before sections are merged. Name the next place, with a reason |

If you open a PDF, name it and the page. If you could not open it, give no number from it.

**What goes to the author after your answers:**
- only a veto that you and I cannot settle among ourselves;
- the next place to work, from your proposals in (e).

Nothing else needs the author.
