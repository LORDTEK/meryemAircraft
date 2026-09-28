# Round 155 — Section 7.3 moved, for your confirmation. What the move taught us: outside 7.3 the supplement lever is small. Two map rows, and one fact none of us saw

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full** (the sections in §7).

---

## 0. The author's decisions since Round 154

1. **E8 — option 4, unanimous.** All four of you and I chose option 4. The target is **12 000 words all-in**. The order is
   calculations and framework first (supplement moves), then the architecture sections compressed (Round 72: *from everywhere*).
   We measure, and if a cut would remove an argument step, we stop and report to the author with numbers (DeepSeek's condition).
2. **Option 3 (two papers) is closed by the author.** My translation, not a verbatim quotation: *There will not be two papers. There
   is no need to discuss it. We have not yet made one paper Q1; first we work.* The triggers some of you attached to option 3
   (13 200 / 13 500) therefore fall away.
3. **The protected sentence of 7.3 goes to the supplement** (rule (iii), author decision E10). My translation: *Let it go to the
   supplement.* It is *"This paragraph compares the reference pair only."*

---

## 1. Section 7.3 as applied — please confirm or name a loss

**What changed from the Round 154 proposal.** Your three restorations are in:
- Grok: *"the ratio of propeller diameter to span rises from 0.35 to 0.47"*;
- Grok: *"**Coupling is not identity**: the buffer is measured in kilograms and the engine in kilowatts, linked by a specific power
  that is itself an assumption."*;
- DeepSeek: *"Either answer leaves the mechanism claim where it was; that claim rests on the inventory of Sections 5.1 and 5.2."*

The subsection headings are removed; the section is now nine paragraphs. **1 091 → 805 words.** The old section is in Supplement S12,
complete and verbatim, under the heading *"Section 12 as it stood before the supplement move (complete)"*. The protected sentence is
there, and `v8_caveats.py` now checks that it stays there (row `| S12 | … | E10 |`).

**Checks, run on the assembled view:** 186 protected sentences in place; 3 moved by author decision and present in the supplement;
no sentence lost (`v8_nothing_lost.py`); no unresolved pointer; no retired phrase.

**Receipt check.** Eight sentences elsewhere point into 7.3. I read each against the new 7.3; all eight are R1. The most sensitive
is Section 8's *"This is where the coupling Section 7.3 found is paid"*. Its receiver, *"what is established is that they are coupled
here … Coupling is not identity"*, is still in the body. **Grok's restoration is what kept that receipt.** Please check that yourselves.

The "before" text is Round 154 §5.1; the text below is the "after" as it now stands in the assembled view.

#### 7.3 Scale does not lock two of the charges together; the third is not tested

Section 7.2 decomposed the three charges on one aircraft, at one size; **this section asks whether they are three quantities or one quantity under three names**, by changing the size of the aircraft and seeing whether they move together. Either answer leaves the mechanism claim where it was; that claim rests on the inventory of Sections 5.1 and 5.2. **The test is deliberately weak**, and it is stated at its own strength. It can show that two charges are not locked together within this model. **It cannot show that they are independent in general**, and it is not offered as doing so.

**The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 7.1's closures**: no closure was run at 1 000 kg, the heavy design has no drag bracket and no structural closure, and no heavy-design range is quoted. The working is in Supplement S12.

**Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its light-design value in the section polars used here, while specific hover power changes by one percent and the Bill 3 ratio by 5 to 14 percent.** The flatness of Bill 3 is imposed by a sizing rule; the finding is that Bill 2 moved anyway, by more than the Bill 3 ratio at every point in the heavy interval and under either engine margin. **Within this model, the two are therefore not one quantity under two names.**

Disc loading is held at approximately the same value, so specific hover power is held with it. **That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3.** The rule has a price, paid in geometry: the ratio of propeller diameter to span rises from 0.35 to 0.47, and **much above 1 000 kg a single nose pair can no longer hold the disc loading**, so a second would have to be added.

**Only the rotor term of Bill 2 is computed at both sizes**; the frame term enters both designs as the same multiplier, so it cannot show a scale effect in either direction. **Within the blade-element and section-polar model, the section Reynolds number accounts for the fall**, and this is a decomposition inside the model rather than a causal claim beyond it. The fall rests on section drag taken from polars rather than measured, and the light end lies below a Reynolds number of 10⁵, where section drag is hardest to predict. **Of the two rotor terms, the light one is therefore the less certain — and it is the one Sections 7.1 and 7.2 carry.**

**Bill 1 is not tested**, and nothing here should be read as showing that it separates from the other two — or as showing that it does not. On this configuration Bill 1 appears as the energy buffer: 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and **both of those figures are inputs.** **A change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction.** **Whether the two are separable here is not established**; what is established is that they are coupled here, which is Section 2.2's claim rather than a defect found in it. **Coupling is not identity**: the buffer is measured in kilograms and the engine in kilowatts, linked by a specific power that is itself an assumption.

**The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low Reynolds number.** It is consistent with the separability Section 2.1 asserts; it is not a verification of separability as a general property, which a single instantiation cannot supply.

The fixed-pitch gap also widens slightly with size, to 16.4 to 22.9 percent at the heavy design (Supplement S12); as in Section 7.2, no variable-pitch counterfactual was computed. **The transition is where the square–cube relation is paid in full**: rotating the heavy design in the light design's two seconds would demand about 220 kW from the tip pairs, roughly the whole of hover power; at its own 5.1 seconds the demand is about 13 kW. **A larger aircraft of this type turns more slowly, and must.**

**Because at least two of the charges are not locked together, a comparison of architectures cannot in general be reduced to a number that does not depend on how the charges are weighed.** The argument requires only two charges that are not locked together; the third need not be shown separate for the conclusion to hold. Section 7.4 examines what the choice of sizing contract does to a ranking, on the light closures of Section 7.1 only.

---

## 2. What the move taught us: outside 7.3 the supplement lever is small

In Round 154 I extrapolated from 7.3's 30 % and wrote that 2.x, 4 and 7.x might yield *"roughly 3 500–4 500 words"*. **That was
wrong, and I should not have extrapolated from one section.** 7.3 was the exception. It still had subsections of working: disc
loadings, rotor terms, Reynolds numbers, the buffer derivation. The other calculation sections were already reduced to result
sentences in the previous stage. What remains in them is held by our own rules.

I went through 7.1, 7.2, 7.4 and 2.3 sentence by sentence. Here is every candidate I considered, and the rule that holds it.

| Section | Candidate | Words (approx.) | Verdict | Rule |
|---|---|---:|---|---|
| 7.1 | *"There was no reason to assume so: propeller efficiency propagates through cruise power into engine size, …"* | 31 | stays | mechanism of a body result (Round 104, Qwen) |
| 7.1 | the kinematic model's sentence (5 m s⁻¹ climb; 2 s and 5.1 s) | 38 | stays | defines the first model; 7.3 uses 2 s and 5.1 s |
| 7.1 | *"The loss is not an artefact of the controller: …"* | 31 | stays | qualifies a body result (the brake of rule (iii)) |
| 7.1 | the reproduction check (1.5 percent) | 38 | stays | the ground of *"a change of inputs, not of method"* |
| 7.2 | the stopped-state estimate (ΔC_D0 = 0.0008, the indexing mechanism) | 60 | batch, not S | cluster C-14 (DeepSeek); conditional-inventory rule (Round 100) |
| 7.2 | the interference quotation repeated from 2.1 | 45 | batch, not S | a copy (C), not working |
| 7.2 | the clean-body ratios (20.55 / 15.24; retains 52.6 and 57.7 percent) | 40 | stays | the result the Bill 2 share is read from |
| 7.4 | **the no-buffer figures (38–47 percent; 520 kg; the first contract's blindness to mass)** | **47** | **S candidate** | the figures are already in Supplement S13; see §3 |
| 2.3 | the weight breakdown (580 of 679 lb; 99 lb not broken out) | 28 | stays | **the 99 lb qualifies "consistent with the transfer property", which stays in the body**; the brake forbids moving it |
| 2.3 | the quadrotor's figures (4.9; 3 678 lb) | 20 | stays | Section 4 consumes them; 2.3 is the data set's single home (Round 113) |
| 2.3 | *"and the page would be weaker for hiding it"* | 8 | batch, not S | voice (Round 124), a deletion, not a move |

**The measured S lever outside 7.3 is about 50 words.** I have not gone through Section 4 with the same care. Its calculation block (*"What
the margin actually is, in one currency"*) is where I would look next. I think most of it is the comparability basis, which the
isolation-pair rule (Round 113) keeps in the body.

**What this means for E8.** The body in the assembled view is **about 19 600 words** (tables counted as text, headings not). The lever that option 4
counted on first, moving calculations to the supplement, is almost spent after one move. The rest has to come from three places:
1. the batch of copy cuts (about 280 words, plus your new clusters);
2. Phase D, the merges (6.2 + 9; the home of 6.1);
3. compressing the architecture sections (Round 72), with the spirit sentences and the protected set kept.

That is where DeepSeek's stop condition will bite, and we should say so now rather than later.

**Please check my measurement.** The full texts of 7.1, 7.2, 7.4 and 2.3 are in §7. If you see an S move of 50 words or more that I
missed, quote it in full, say where it goes in the supplement, and say what the body sentence that survives still tells the reader.
If you agree the lever is spent, say so. **This is a claim of absence, so I want it checked** (Round 133: search the whole text before
declaring something absent).

---

## 3. The one S candidate: 7.4, the no-buffer comparison (for the batch)

**Now** (in *"What is compared, and on what basis"*):

> … **Holding Bill 3 common is a choice of question, and it has a direction.** **The choice runs against this configuration.** Without the buffer, and with engines rated to deliver the hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off mass and falls 38 to 47 percent behind under a fixed fuel mass, and the tilt bound does not close under a fixed take-off mass; under a fixed fuel fraction it closes at 520 kg, about ten times this configuration's mass — the first contract's blindness to mass, made visible. That comparison is not used, because it would set competitors without a store against this configuration with one.

**Proposed** (deletion only; the pointer is the one addition):

> … **Holding Bill 3 common is a choice of question, and it has a direction.** **The choice runs against this configuration.** Without the buffer, and with engines rated to deliver the hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off mass (Supplement S13). That comparison is not used, because it would set competitors without a store against this configuration with one.

**Why it passes, in my reading:**
- The protected *"The choice runs against this configuration"* keeps a ground in the body: two contracts under which the competitor
  does not close.
- The mass-blindness of the first contract is already stated in the body, where the contracts are defined: *"under which take-off mass
  cancels from range"*.
- Supplement S13 already carries every moved figure, and at greater length.

**What I am unsure of:** whether *"the first contract's blindness to mass, made visible"* is a finding the body needs as an
illustration. I think the definition already carries it. **47 words.** If you agree, it is applied with the batch, not in a round of
its own.

---

## 4. The two unsettled map rows — DeepSeek against the others, and a fact that changes one of them

DeepSeek holds **K** on both rows. Grok, ChatGPT, Qwen and I voted otherwise. **Under the Round 106 rule, the three of you are asked to
answer DeepSeek directly, not only me.**

### 4.1 K-9, Section 4 — and a fact none of us saw

The paragraph, in full (*"What this half costs"*, Section 4):

> The wing that makes cruise efficient is carried through the vertical phase, where it produces
nothing and presents the aircraft's largest surface to ground wind. The tailless planform that
follows from having no boom constrains the sweep, because with no horizontal stabiliser the
pitching moment must come from the distribution of lift along the body itself. **And the
fixed-pitch propeller that serves both regimes is the reason the margin above sits where it does
rather than higher.** Section 7.2 charges the third. The first two are inside Section 7.1's closed numbers — the wing's mass in the empty fraction, the constrained planform in the computed span efficiency — but neither is separated out as a charge, and the wing's exposure to ground wind is not priced in this work.

- **Grok (–):** the 0.85 line higher up already says why the margin sits where it does; this sentence does the same job.
- **DeepSeek (K):** this sentence is a cost statement; the 0.85 line is a comparison statement. Different functions. Deleting it would
  leave the comparison statement as the only place the compromise appears.
- **ChatGPT, Qwen, and I voted – in Round 154.**

**The fact:** the two sentences after it count it. *"Section 7.2 charges **the third**. **The first two** are inside Section 7.1's
closed numbers."* The paragraph lists three costs, and the fixed-pitch sentence is the third. **Deleting it leaves "the third"
pointing at nothing and "the first two" counting a list of two.** That is the count-consistency rule of Round 95. None of the five of
us named it; I voted – without reading the next sentence.

**My vote changes to K.** A C is possible only by rewriting the count, and a rewrite that saves a clause is not worth a new predicate
risk. DeepSeek was right on the outcome. Its stated reason, that the two sentences do different jobs, may also be right. **Grok, ChatGPT,
Qwen:** does the count change your vote?

### 4.2 K-3, Section 6.2

The paragraph, in full (*"What each claim does not depend on"*, Section 6.2, after the sentence that ends *"… nor on the transition
aerodynamics"*):

> **The last of these carries a distinction that matters more than the others.** The mechanism claim is a statement about what hardware is present, and it is settled by the inventory of Sections 5.1 and 5.2. **The separate claim that this aircraft can actually perform the regime change is not settled** (Section 5.1).

Item 8, which DeepSeek says this paragraph grounds, in full (*"Eight things this paper does not claim"*, two subsections later):

> **8. It does not claim that the aircraft flies.** The design *sizes* vertical operation and the transition; it does not demonstrate either. No aircraft has been built, no wind tunnel has been run on this geometry, and the transition analysis is a calculation whose assumptions are stated where it appears. **"By construction" throughout this paper means "by the sizing", never "by demonstration."**

- **DeepSeek (K):** 5.1 states the mechanism/transition split as an argument step; 6.2 restates it as the boundary that makes item 8
  land. Cutting 6.2's paragraph to a clause would leave item 8 *"a two-sentence assertion without its ground"*.
- **Grok, ChatGPT, Qwen, and I (C):** 5.1 is the home of the split. 6.2 needs the boundary, not the argument again.

**My view, for you to attack:** I stay at **C**. Item 8 is not next to this paragraph; it is two subsections later, and it carries its
own ground (*"sizes … does not demonstrate"*). But DeepSeek has found something true. The paragraph explains *"nor on the transition
aerodynamics"* in the sentence before it, and a C must keep that explanation as a clause, not delete it. **Grok, ChatGPT, Qwen:** please
answer DeepSeek's claim about item 8, and say whether a C that keeps the explanation as a clause meets it.

Both rows are applied with the batch. Neither gets a round of its own.

---

## 5. Errors this round

- **Mine:**
  - I extrapolated 7.3's 30 % to all of 2.x, 4 and 7.x (§2);
  - I voted – on K-9 without reading the counting sentence after it (§4.1).
- **Grok, ChatGPT, Qwen:** the same K-9 miss as mine.
- **ChatGPT (Round 154):** said *"coupling ≠ identity"* was kept in the proposed 7.3; the proposal had removed it. Grok's restoration put it
  back.
- **DeepSeek:** none found.

---

## 6. What I ask of you

| # | Item |
|---|---|
| a | §1: the applied 7.3 — confirm, or name a lost finding, qualification or antecedent |
| b | **§2: my measurement — is the S lever outside 7.3 spent? Name any S move of 50+ words I missed (full text, supplement home, what the surviving body sentence still says)** |
| c | §3: the 7.4 candidate — confirm for the batch, or veto with the reason |
| d | §4.1: K-9 — does the count change your vote? (Grok, ChatGPT, Qwen: answer DeepSeek) |
| e | §4.2: K-3 — answer DeepSeek's item-8 claim; does a C that keeps the explanation as a clause meet it? |
| f | **Your own proposals** (the author's standing request): with the S lever spent, what order do you propose for the rest — the batch of copy cuts, Phase D merges, the architecture sections? Any other idea, with its reason |

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## 7. Full texts (assembled view, at the commit above)

#### 2.3 An independent quantitative check

An accounting proposed by the same people who then use it invites one obvious objection: that the charges were chosen because a particular aircraft happens not to pay them. The objection arises at the title, not at the ledger, so it is answered here — before any configuration is described — by testing a prediction the accounting makes against numbers this work did not produce. **What follows is not a test of the whole framework.** It checks one falsifiable consequence on one independent data set.

**The prediction has two halves, and only the first is a derivation.**

> **First half, derived from Section 2.1.** A configuration carrying a dedicated lift system pays for it in gross weight, and the payment is amplified: additional empty mass enters through a multiplier that grows as the empty-mass fraction rises, and the same increment is counted again in hover.

> **Second half, not derived.** That the cruise efficiency the arrangement buys does not cover that payment. Section 2.1 predicts the charge and the amplification; **it does not prove that the credit must lose.** A dedicated lift system raises the empty-mass fraction and may lower the energy fraction at the same time, and which wins is a closure result rather than a consequence of the accounting.

The check tests the second half on independent data, with the first half supplying the reason to expect the outcome: the weight charge is amplified by a multiplier, while the efficiency credit enters linearly through the cruise lift-to-drag ratio. **If some data set showed the credit covering the charge, Bill 1 would not be refuted** — the mass would still have been paid. What would be refuted is the expectation that the amplified charge outweighs the linear credit. **The prediction is also mission-dependent**, and the page would be weaker for hiding it. The mass charge of carried lift hardware is roughly fixed; the efficiency credit accumulates with distance. A long enough mission is where the credit is most likely to cover the charge, and the mission used below is short. **The counter-set is therefore a common-mission sizing study at longer range in which a dedicated-lift configuration is both more efficient and no heavier than one without.** None is known to the authors.

The check uses a NASA study, conducted for its own purposes and with no relationship to the present work, that sizes **five VTOL architecture families** — nine designs in all — against a single mission with common tools and common assumptions; it does not use the three-bill accounting of Section 2.1 or any framework derived from it. It is used for three reasons, stated so that the choice is not merely the one that agreed: it holds the mission fixed across architecture families, it applies one set of tools to all of them, and it reports both quantities this prediction needs. The mission is 1 200 lb of payload over 75 nautical miles. Three of the nine designs matter here. The turboshaft quadrotor reaches an effective lift-to-drag ratio of 4.9 at a design gross weight of 3 678 lb, with no dedicated lift group: its rotors serve both regimes. **The turbo-electric lift-plus-cruise design reaches 8.5 at 7 271 lb and carries a dedicated lift group — eight lift motors beside its cruise motor. The turbo-electric tilt-wing reaches 8.6 at 6 584 lb with none: eight proprotors, reoriented.**

**The primary comparison is the lift-plus-cruise design against the tilt-wing**, because they isolate the charge: they share the mission, the payload, the turbo-electric propulsion architecture and the presence of a cruising wing. **They are not identical in every other respect** — one stops its lift rotors in the airstream and drives a separate pusher, the other reorients its proprotors on a tilting wing — **but the difference the comparison turns on is that one carries a dedicated lift group through cruise and the other does not.** The comparison is the closest the published set comes to isolating that charge; it is not a controlled experiment. **The tilt-wing is 1.2 % better in effective cruise efficiency and 9.4 % lighter.** The dedicated lift group buys no cruise-efficiency advantage at all here — it is marginally behind — and the design gross weights differ by 687 lb in the tilt-wing's favour. **That figure is the net difference between two architectures, not the measured mass of a lift group**, and the published weight breakdown is what makes it informative rather than merely large. **The published weight breakdown is consistent with the transfer property of Section 2.1 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce**: its three reported categories account for 580 lb of the 679 lb empty-weight difference, and the remaining 99 lb lies in categories it does not break out (Supplement S4). **And the source states the second half of the prediction in its own words, on a comparison the check does not use as its test.** Discussing why the all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery weight compared with the quadrotor, *"but not enough to counter the increase in structure and propulsion weight."* That is the efficiency credit conceded and found insufficient, by the authors of the data rather than by the authors of the prediction. **The quadrotor is reported for scale, and the isolation test above is what carries the prediction**: against it the lift-plus-cruise design changes three things at once, and the contrast is in Supplement S4. **The framework does not predict any of these numbers**; without the input fractions it predicts no magnitudes. What it predicts is that the amplified weight charge survives the efficiency credit, and on the isolated pair it does so with the credit reduced to nothing.

**The architecture proposed later in this paper is not the only way to avoid the first charge.** The tilting family avoids it too — it carries no dedicated lift group, it is the lighter of the two matched designs, and an independent set says so. The margin in cruise efficiency is 0.1 in effective lift-to-drag ratio, and nothing is claimed from its direction. **The tilt-wing is consistent with the transfer property of Section 2.1, in someone else's data.** It does not escape the accounting by avoiding the mass charge; it *moves* the cost — to the mechanism that reorients its propulsors, with the actuation, the gyroscopic coupling and the transition control problem that Section 2.1 assigns to that family. What separates the tilting family from the configuration described later is not this axis; it is what each pays, and a sizing study does not settle that.

It establishes that one prediction of the accounting holds on data produced elsewhere, for purposes unrelated to this argument. That is the whole of it. **It does not establish that the accounting is complete**, that the three charges are the only costs an architecture pays, or that avoiding them makes an aircraft better. **It does not establish anything about the configuration this paper proposes**, which has not yet been described, and which is not in the study used here. A reader who wants to know whether the accounting flatters that configuration will have to wait for Section 7.2, where it is applied to it and where the answer is not uniformly favourable. **An instrument whose first use is to measure the thing its authors are advocating should be shown working on something else first**, and that is why this section comes before the aircraft. **The instrument is now fixed, and it is not modified again.** **Everything that follows is measured with it rather than added to it.**

#### 7.1 Analytical closure of the sizing loop

This section prices the arrangement of Sections 5.1 and 5.2 on a declared package; it does not bear on the count of mechanism classes, which rests on the inventory of those sections alone. **Closing a sizing loop mathematically is not the same thing as closing an aircraft physically.** This section does the first: what it produces is a set of consistent numbers on a declared set of assumptions.

Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Supplement S10). **If no fixed point exists, the declared sizing package does not close.**

##### The inputs, and why there are four closures rather than one

**The zero-lift drag coefficient is uncertainty:** a consistent build-up places it between 0.0285 and 0.0381 (Section 7.2), and a designer does not choose where the real aircraft falls in that range. **The blade family is a design variable this study has not fixed:** four nose-blade families that meet the hover figure of merit span cruise propeller efficiencies of 0.632 to 0.683. **The reference design's assumed zero-lift value of 0.0248 is not used**; the consistent build-up places it below both ends of the bracket, outside the supported range.

The loop holds wing loading, disc loading and aspect ratio fixed, so **the cruise lift coefficient is unchanged at 0.450 in every closure** (geometry in Supplement S10); the claim is that C_L is unchanged, not that C_D0 is exactly so. The tip frames, the tip discs and the strip are not sizing variables; they were set on the 50 kg reference design of Section 5.2, and **the control moment arms of Section 5.2 are therefore reference values that this closure does not re-derive.** **These are the same configuration at four closed masses rather than four configurations** — but anything that depends on the arms is carried at the reference geometry and is not an output of the loop.

Run on the reference design's assumed inputs — that drag coefficient without the rotor term, and a propeller efficiency of 0.80 — the same construction reproduces the 50 kg reference design within 1.5 percent (Supplement S10). That check is the only place in the closures where the assumed value appears, so the closures report a change of inputs, not of method.

##### The four closures

**On these assumptions all four converge**, for the 50 kg design — the only one carried through this loop.

| | C_D0 | η_p | L/D | L/De | MTOW | Empty fraction | Hover power, rotor shaft | Engine rating, shaft | Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** | 0.0381 | 0.632 | 8.79 | 5.56 | 57.5 kg | 0.614 | 12.53 kW | 5.17 kW | 927 km |
| **B** | 0.0381 | 0.683 | 8.79 | 6.00 | 55.8 kg | 0.607 | 12.17 kW | 4.65 kW | 1 002 km |
| **C** | 0.0285 | 0.632 | 10.82 | 6.84 | 53.5 kg | 0.597 | 11.66 kW | 3.91 kW | 1 141 km |
| **D** | 0.0285 | 0.683 | 10.82 | 7.39 | 52.3 kg | 0.592 | 11.40 kW | 3.54 kW | 1 233 km |

*L/De = L/D × η_p at the cruise condition; the loop holds both factors fixed within each closure, so the closure changes
neither. The four L/De values are the bounding corners of that product, carried into the closures as inputs, not four
simulated aircraft.*

**Payload is an input, fixed at 13 kg; take-off mass is the output**, and the payload fraction runs from 0.25 down to 0.23. **The blade that is best before the loop is still best after it.** There was no reason to assume so: propeller efficiency propagates through cruise power into engine size, engine size into mass, and mass back into hover power, and a loop can reverse a local ranking. At both ends of the drag bracket the higher-efficiency family closes to the longer range — **a result of the closure rather than an assumption carried into it.**

##### The transition

The sizing above says nothing about whether the aircraft can change regime. **The question is asked in two models, only the second of which carries rotational dynamics, and that one does not support a zero altitude loss.** Every transition figure here belongs to a reference design at its reference mass and its assumed drag, and is not an output of the closure; at either end of the drag bracket the altitude loss moves by less than 0.1 m. In the first, a point-mass model with the body angle driven kinematically, a rotation entered in a 5 m s⁻¹ climb loses no altitude at either reference rotation time: 2 s for the 50 kg design and 5.1 s for the 1 000 kg one. Solved instead with rotational dynamics and a finite control moment, **and with the aerodynamic pitching moment set to exactly zero, so that nothing favourable is borrowed**, the 50 kg design **loses 5.4 to 6.6 m at the same reference condition**, depending on the reference profile. The loss is not an artefact of the controller: it appears under all three reference profiles, appears without the control moment saturating, and grows as the gains are raised (Supplement S10). **What the kinematic model leaves out is not the difficulty of turning the aircraft but the trajectory the aircraft flies while it is being turned.** **So the zero-altitude-loss result is a property of the model that produced it.**

What replaces it is not a prediction: the pitching moment that would make it one exists, but for the methods used here the predictions diverge above roughly ten degrees of incidence, the band the rotation passes through (Section 8). With a borrowed moment the spread is wide enough that no number from it is reportable: some models complete the rotation, some saturate the tip pairs, and some tumble. **That spread is itself the finding.** **Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude.** Whether a real aircraft loses 5.4 to 6.6 m, more, or less is not settled by anything here.

##### What closing does and does not establish

It establishes that the architecture is arithmetically self-consistent on a declared package, at four corners of that package. **It does not establish that the package exists.** The energy store this closure assumes is the item Section 8 examines, and the examination does not end well. These ranges are carried forward as closed-loop values, not as a ranking: no rotorcraft is sized in this work, so no range comparison is made against one (Section 4 compares cruise efficiency), and the comparison with the other hybrids depends on the sizing contract (Section 7.4).

#### 7.2 The ledger

Section 2.1 named three charges that any architecture in this corner pays; **this section says where each charge appears inside the closed numbers of Section 7.1, and how large it is there.** Like the closure, the ledger prices the arrangement; the count of mechanism classes is not an entry in it.

**It attributes. It does not add.** Every cost named below is already inside the closure of Section 7.1. **No new physical cost term is introduced here.** **And there is no single figure for what the architecture costs.** The three charges are in three different currencies — kilograms, drag counts, installed kilowatts — and **no scalar aggregate is defined, because this study has no defensible weighting between them.** **The total is the contract, not a property of the aircraft** (Section 7.4).

##### Bill 2 — the drag of hover hardware, inside the bracket

In the zero-lift drag build-up behind Section 7.1's bracket (line items in Supplement S11), **the hardware exposed by the vertical-phase layout — the tip frames and the free-wheeling tip-pair rotors — is 69 percent of the zero-lift drag at the favourable end and 57 percent at the adverse one**; the rotor term alone is 0.0154 at the favourable end. **The rotor line rests on section drag at low Reynolds number.** It is a blade-element result for sections near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section polars that are computed rather than measured; Section 7.3 shows how strongly the term depends on it. **The tip-frame term is an attribution, not a marginal removal cost**: it is not a claim that this drag would disappear if the vertical phase did. **No stopped-state counterfactual was computed.** The eight tip discs stopped edge-on at a controlled azimuth are estimated at ΔC_D0 = 0.0008, against the computed free-wheeling 0.0154 (the estimate is an area-and-coefficient calculation, Supplement S11), but controlling the azimuth takes an indexing mechanism — a class Section 5.1 counts — and sizing it for eight small discs, charging its mass and its failure modes, and re-solving the loop has not been done.

Removing the hub and small items, the tip frames and the free-wheeling rotors gives a clean-body lift-to-drag ratio of 20.55 at the favourable end and 15.24 at the adverse one, against the aircraft's 10.82 and 8.79: **the configuration retains 52.6 and 57.7 percent.** Bill 2 therefore occupies a larger share where the clean-body drag is lower, because a near-constant charge is set against a smaller total — a statement about position within the drag bracket at one scale, not about size (Section 7.3).

**Rotor–structure and rotor–wing interference is not modelled and is not carried as a line.** Section 2.1 quotes a wind-tunnel finding that a simulation assuming negligible rotor–structure interaction *"always predicts higher lift and lower drag than were experimentally observed"*; this build-up is such a calculation, and the bracket's upper margin is the only provision made for it.

##### The cruise-efficiency gap under fixed pitch

Section 7.1's closures run at a cruise propeller efficiency of 0.632 to 0.683: **relative to the 0.80 the reference design's sizing assumed, 14.6 percent lower at the better blade and 21.0 percent lower at the worse.** **The ledger does not attribute the whole of that gap to the absence of variable pitch.** **No variable-pitch counterfactual was computed.** Nor is the gap decomposed.

##### Bill 1 — carried mass, and what it is on this configuration

**There is no dedicated lift group to charge.** What Bill 1 becomes here is the energy buffer: **3.6 percent of take-off mass, 1.9 to 2.1 kg across the four closures.** The buffer is not lift-subsystem mass, so it is not Bill 1 as Section 2.1 defines it, but it is carried for the whole flight to serve a demand that lasts about two percent of it: **the architecture converts a power-system charge into a cost in kilograms**, as Section 2.2 said in advance it would.

**The buffer fraction is an input to the loop, not a result of it.** The deficit per kilogram of take-off mass that the buffer covers, taken at the electrical bus, spreads by 12 percent across the four closures while the fraction is held at 3.6 percent (Supplement S11). **The corner that needs the most buffer per kilogram is given the smallest buffer**, and that is a declared assumption of the closure rather than an outcome of it.

##### Bill 3 — released from the engine, and not from the electrical path

The engine is sized by cruise, **3.54 to 5.17 kW** of shaft rating, against a hover requirement of **11.4 to 12.5 kW** at the rotor shaft: a ratio of installed hardware of **2.4 to 3.2**, which is not the buffer's burden (Section 8 computes that). **But the full hover power passes through the electrical path, and that path is sized by it.** **Bill 3 is removed from the engine and left standing on the electrical system** (the propulsion-mass split is in Supplement S11).

##### What the closure does not contain

Section 7.1's convergence does not cover the cost of declining the reaction-torque channel, the sizing of the strip's actuation, the allocation of the take-off margin against attitude authority, the landing transition, the vortex ring state, closed-loop attitude control in hover and in cruise, engine installation, or rotor–structure and rotor–wing interference; **none of these is a ledger entry, and Section 8 lists them.** **The first and the last are the two that would most change the numbers above if they were computed.**

**Every one of the charges above belongs to one scale**: the four closures do not establish how the three charges behave as the aircraft changes size, which Section 7.3 asks, or what happens to the comparison when the sizing contract changes, which Section 7.4 asks.

#### 7.4 Rankings belong to contracts

Section 7.3 showed that at least two of the charges are not locked together; where one architecture pays less of one charge and more of another, the ranking depends on how the charges are weighed, and **a sizing contract is one such weighing**: it fixes what is held equal between the architectures being compared. This section applies three contracts to three architectures at each of the four closures of Section 7.1. **The mechanism claim is not a ranking and is not at stake here.**

##### Three contracts, and what each holds equal

Range in the sizing loop is proportional to L/D, to the energy chain, propeller included, and to the fuel fraction, and the three contracts differ only in the last (Supplement S13): a **fixed fuel fraction**, sixteen percent of each architecture's own take-off mass, under which take-off mass cancels from range; a **fixed fuel mass**, the 8.4 to 9.2 kg this configuration carries, under which range is divided by take-off mass; and a **fixed take-off mass and payload**, under which every kilogram of architecture-specific hardware is a kilogram of fuel not carried. **These are three different questions, not three estimates of one answer.** A mission decides which of them it is asking; this paper has no mission that would decide, and does not choose.

##### What is compared, and on what basis

Three architectures fly the same mission, 13 kg of payload at 30 m s⁻¹, with the same wing loading, disc loading and aspect ratio, the same airframe and avionics fractions, and the same fuel and energy chain apart from the propeller. **The competitors are therefore this planform with two add-ons, not independently designed aircraft of their families.** All three carry the same buffered series-hybrid power system, so Bill 3 is held common and the comparison measures mass and cruise drag. **Holding Bill 3 common is a choice of question, and it has a direction.** **The choice runs against this configuration.** Without the buffer, and with engines rated to deliver the hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off mass and falls 38 to 47 percent behind under a fixed fuel mass, and the tilt bound does not close under a fixed take-off mass; under a fixed fuel fraction it closes at 520 kg, about ten times this configuration's mass — the first contract's blindness to mass, made visible. That comparison is not used, because it would set competitors without a store against this configuration with one.

The basis is not symmetric: the lift-plus-cruise layout carries a lift-to-drag ratio transferred from a different airframe's wind-tunnel campaign (Section 2.1) and assumes lift rotors stopped and aligned in cruise, which takes an indexing mechanism (Section 5.1) whose mass is not separately charged. **The tilting layout carries no cruise drag penalty at all. That is an idealisation in its favour**, and it is deliberate: it makes the tilting layout a bound. Both competitors use a propeller efficiency of 0.80, assumed, not computed, against this configuration's computed 0.632 and 0.683; the lift-plus-cruise layout carries a lift group of 10 percent of take-off mass and the tilting layout a tilt mechanism of 5 percent. **Neither figure is measured.**

##### Against lift-plus-cruise: a trade, and the contract sets the exchange rate

**The two architectures trade one charge against another**: closed under a fixed fuel fraction, this configuration is 27 to 30 percent lighter, and the lift-plus-cruise layout cruises at a lift-to-drag ratio of 11.66 and 15.72 against 8.79 and 10.82, with a propeller at 0.80.

Range of the lift-plus-cruise layout relative to this configuration:

| Closure (Section 7.1) | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass |
|---|---:|---:|---:|
| A | +67.8 % | +40.2 % | +1.1 % |
| B | +55.3 % | +27.5 % | **−13.0 %** |
| C | +83.9 % | +53.5 % | +7.3 % |
| D | +70.2 % | +40.1 % | **−6.5 %** |

**The lift-plus-cruise layout is 55 to 84 percent ahead under the first contract, 28 to 54 percent under the second, and between 13 percent short and 7 percent ahead under the third; the shift from first to third is 67 to 77 percentage points at every closure**, at the declared lift-group fraction, and always toward the lighter aircraft. **The sign itself changes inside the envelope under the third contract**: this configuration is ahead at the two closures with the higher-efficiency blade family and behind at the two with the lower. **A statement of which architecture has the longer range, made without its contract, would therefore be a statement about the contract.**

##### Against the tilting layout: a bound, not a ranking

**What the bound gives is a size, not an order.** Credited with no cruise penalty, the tilting layout is 93 to 141 percent ahead of this configuration under every contract at every closure; that margin is the room a real tilting aircraft's cruise penalties — nacelle drag, pivot fairing, hover-sized rotors flown as cruise propellers — would have to fill, and how much of it they fill is not computed. **A ranking against a competitor modelled as a bound is not a ranking, and no range claim is made against the tilting family in either direction.**

##### Section 2.1's prediction, tested

Section 2.1 predicted that such a ranking will move when the sizing rule changes, and can reverse. **The movement holds everywhere**, against both competitors, toward the lighter arrangement as the contract weights mass more; **the reversal holds at two of the four closures against lift-plus-cruise, and at none against the tilt bound.**

**Where the reversal falls is decided by quantities this study has not measured or not fixed**: the blade family in the base case, and across the sensitivity cases the competitor's lift-group mass and the propeller basis (Supplement S13). With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every closure; with a heavier one this configuration leads under a fixed take-off mass at every closure; with a common propeller efficiency a reversal appears at every closure. **Which architecture ranks first under a fixed take-off mass is therefore decided, in this model, by quantities this study assumes for the competitor rather than measures: its lift-group mass fraction and its propeller efficiency.** **Put plainly, the sign under a fixed take-off mass is not a result about the architectures; it is a result about those quantities.** What is robust is that the shift exists and runs toward the lighter aircraft; its size is the size of the mass difference.

##### What the framework asks of whoever uses it

**Each comparison states every charge in its own currency before any aggregate, names its contract, and states its asymmetries and their directions; an ordering is reported only with the contract it was computed under and, where its sign depends on an unmeasured quantity, with that quantity named.** This paper meets that for its own column (Section 7.2) and not for the competitors', whose kilograms and drag counts here are parameters and transferred ratios rather than an audit.

##### What this section does not establish

**The competitors are modelled at a coarser level than this configuration**: their drag is transferred or idealised, their propeller efficiency assumed and their architecture-specific mass a parameter. **Comparing computed figures against assumed ones favours whichever is assumed more optimistically** — in propeller efficiency both competitors, and with a common propeller efficiency the lift-plus-cruise lead under the first contract falls from 55–84 to 33–45 percent (Supplement S13); in drag the tilting layout, by assumption. **The comparison is at one size**: Section 7.3's 1 000 kg reference design has no closure, and none of its figures is used here. **And nothing here ranks architectures for a mission.** What this section establishes is narrower: **the same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property of the architectures alone.
