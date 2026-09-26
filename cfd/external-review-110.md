# Round 106 — Step 11 is applied; drafts of Steps 12 and 13; and where you still differ, answer one another

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> - Step 11 is recomposed in `paper/v8/11-the-ledger.md`; its original is in Supplement S11 in full.
> - The drafts are `paper/v8/drafts/12-recomposed.md` and `13-recomposed.md`. Each has your lists side by side (§1), and a
>   trace (§3).

---

## 1. The author

> *"I approve E9; let it go to the supplement with the line items."* (Round 106)

> *"Where a disagreement persists, the AIs may give their views on one another's ideas."* (Round 106)

The second is not new; it is our Round 85 rule, repeated by the author. **§4 of this text is built for it.** Each point on which
you still differ is set out there with the names and the reasons. Please answer **one another** there, not only me.

---

## 2. Step 11 is applied — please confirm the result

The step now carries the draft you voted, with R15 (*"occupies"*) and J18 (the source's own sentence) as you confirmed.
- The line-item build-up and the protected sentence *"No line item at the adverse end is an independent measurement…"* are
  together in S11, under rule (iii) and the author's decision.
- `v8_caveats.py` checks that the sentence stands in S11.
- R15 is protected. The count stays at 171: one moved, one added.
- Nothing is lost.
- **Length: 1 969 → about 820 words.**

**Also applied, unanimously:**
- no Step 10 pointer (DeepSeek withdrew it);
- the negative-qualification audit list, used in the Step 12 trace;
- Grok P76 — *"total of the three"*, *"combined cost of the three bills"* and *"sum of the three bills"* are retired, and the scan
  enforces it;
- Grok P75 and Qwen R104-P2, recorded for Steps 12 and 14;
- DeepSeek's shortfall table, to be built when Step 13 is applied.

---

## 3. The drafts of Steps 12 and 13

**Each opens with its core finding in the source's words** (Grok P77, Qwen R105-P1). **All protected sentences are in the drafts:
10 of 10, and 14 of 14.**

**A plain fact first: both drafts are longer than Steps 10 and 11.**
- Step 12 is about 1 015 words, 57 % of its source.
- Step 13 is about 1 205 words, 60 %.

The reason is the same in both: their protected sentences qualify core findings that stay, so rule (iii) finds nothing to move.
Qwen said this of Step 12 last round. Section 4 lists the candidate cuts; I have not made them, because the cuts are yours to vote.

**Checks on your quotations** (each is in the draft files' §1):
- Every DeepSeek and Grok quotation is in the step bodies.
- Four of Qwen's Step 12 quotations come from the pre-compression Step 12, which has sat in Supplement S12 since Round 71:
  - *"returns 0.0181"*;
  - *"25.3 to 45.0"*;
  - *"0.202 kW kg⁻¹"*;
  - *"the fuller heavy blade would pay more"*.

  They already live where Qwen proposes to send them.
- DeepSeek's *"14 to 134 points"* is in S13, not the body.
- Two of Qwen's Step 13 quotations paraphrase the body's opening and its 67–77 sentence.

In all of these the meaning is right. The lesson from Round 104 stands: quote the step as it is now.

### Step 12 draft

> ## Scale does not lock two of the charges together; the third is not tested
> 
> [J1] Section 11 decomposed the three charges on one aircraft, at one size; **this section asks whether they are three quantities or one quantity under three names**, by changing the size of the aircraft and seeing whether they move together. [D2] Either answer leaves the mechanism claim where it was; that claim rests on the inventory of Sections 7 and 8. [P3] **The test is deliberately weak**, and it is stated at its own strength. [P4] It can show that two charges are not locked together within this model. **It cannot show that they are independent in general**, and it is not offered as doing so.
> 
> [J5] **The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 10's closures**: no closure was run at 1 000 kg, the heavy design has no drag bracket and no structural closure, and no heavy-design range is quoted.
> 
> ### Bill 3 — held nearly flat by a sizing rule, which is not a finding about Bill 3
> 
> [J6] Disc loading is held at approximately the same value, 44.2 kg m⁻² at 50 kg and 43.7 at 1 000 kg, so specific hover power is held with it: 0.218 kW kg⁻¹ at the light design and 0.216 at the heavy. [P7] **That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3.**
> 
> [J8] Section 11's measure of Bill 3, rotor-shaft hover power over engine shaft rating, is 4.19 at the light design and 3.98 at the heavy, and with the engine margins the two designs use it **moves by between 5 and 14 percent across the factor of twenty, depending on an engine margin the sizing rule does not set** (Supplement S12). *(Section 11's 2.4 to 3.2 is the same ratio at the four closures. [P9] This paragraph compares the reference pair only.)*
> 
> [J10] The rule has a price, paid in geometry: the ratio of propeller diameter to span rises from 0.35 to 0.47, and **much above 1 000 kg a single nose pair can no longer hold the disc loading**, so a second would have to be added.
> 
> ### Bill 2 — the rotor term falls, and in this model Reynolds number accounts for it
> 
> [D12] **Only the rotor term of Bill 2 is computed at both sizes**; the frame term enters both designs as the same multiplier, so it cannot show a scale effect in either direction. [J13] At 50 kg the rotor term is **0.0154**; at 1 000 kg the blade designed to the same section lift coefficient gives **0.0068**, and the blades swept give 0.0045 to 0.0100 — a direction that is the ordinary one and a factor that is not a measurement. [J14] **Within the blade-element and section-polar model, the section Reynolds number accounts for the fall**, rising from about 8 × 10⁴ to 5.6 × 10⁵; three other candidates are excluded (Supplement S12), and this is a decomposition inside the model rather than a causal claim beyond it.
> 
> [J15] The fall rests on section drag taken from polars rather than measured, and the light end lies below a Reynolds number of 10⁵, where section drag is hardest to predict. [P16] **Of the two rotor terms, the light one is therefore the less certain — and it is the one Sections 10 and 11 carry.**
> 
> ### Bill 1 — not tested, and the one available derivation would not test it
> 
> [J18] On this configuration Bill 1 appears as the energy buffer: 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and **both of those figures are inputs.** [P19] **A change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction.** [D20] A buffer sized to the hover deficit at the same specific power would track hover power and engine rating, which are the Bill 3 measures, so that derivation cannot test whether Bill 1 separates. [J21] **Whether the two are separable here is not established**; what is established is that they are coupled here, which is Section 3's claim rather than a defect found in it. [D22] **Coupling is not identity**: the buffer is measured in kilograms and the engine in kilowatts, linked by a specific power that is itself an assumption.
> 
> ### What the comparison establishes
> 
> [D23] **Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its light-design value in the section polars used here, while specific hover power changes by one percent and the Bill 3 ratio by 5 to 14 percent.** [D24] The flatness of Bill 3 is imposed by a sizing rule; the finding is that Bill 2 moved anyway, by more than the Bill 3 ratio at every point in the heavy interval and under either engine margin. [D25] **Within this model, the two are therefore not one quantity under two names.**
> 
> [P26] **Bill 1 is not tested**, and nothing here should be read as showing that it separates from the other two — or as showing that it does not. [P27] **The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low Reynolds number.** [P28] It is consistent with the separability Section 2 asserts; it is not a verification of separability as a general property, which a single instantiation cannot supply.
> 
> ### Two costs that scale does not relieve
> 
> [J29] **The cruise-efficiency gap under fixed pitch widens slightly with size**: 14.6 to 21.0 percent below the 0.80 assumed at the light design and **16.4 to 22.9 percent below it at the heavy one**, and as in Section 11 no variable-pitch counterfactual was computed. [J30] **The transition is where the square–cube relation is paid in full**: rotating the heavy design in the light design's two seconds would demand about 220 kW from the tip propellers, roughly the whole of hover power; at its own 5.1 seconds the demand is about 13 kW. [D31] **A larger aircraft of this type turns more slowly, and must.**
> 
> ### Why this section sits between the ledger and the contracts
> 
> [D32] **Because at least two of the charges are not locked together, a comparison of architectures cannot in general be reduced to a number that does not depend on how the charges are weighed.** [D33] The argument requires only two charges that are not locked together; the third need not be shown separate for the conclusion to hold. [D34] Section 13 examines what the choice of sizing contract does to a ranking, on the light closures of Section 10 only.

### Step 13 draft

> ## Rankings belong to contracts
> 
> [J1] Section 12 showed that at least two of the charges are not locked together; where one architecture pays less of one charge and more of another, the ranking depends on how the charges are weighed, and **a sizing contract is one such weighing**: it fixes what is held equal between the architectures being compared. [D2] This section applies three contracts to three architectures at each of the four closures of Section 10. [P3] **The mechanism claim is not a ranking and is not at stake here.**
> 
> ### Three contracts, and what each holds equal
> 
> [R4] Range in the sizing loop is proportional to L/D, to the energy chain, propeller included, and to the fuel fraction, and the three contracts differ only in the last (Supplement S13): a **fixed fuel fraction**, sixteen percent of each architecture's own take-off mass, under which take-off mass cancels from range; a **fixed fuel mass**, the 8.4 to 9.2 kg this configuration carries, under which range is divided by take-off mass; and a **fixed take-off mass and payload**, under which every kilogram of architecture-specific hardware is a kilogram of fuel not carried. [P5] **These are three different questions, not three estimates of one answer.** [D6] A mission decides which of them it is asking; this paper has no mission that would decide, and does not choose.
> 
> ### What is compared, and on what basis
> 
> [J7] Three architectures fly the same mission, 13 kg of payload at 30 m s⁻¹, with the same wing loading, disc loading and aspect ratio, the same airframe and avionics fractions, and the same fuel and energy chain apart from the propeller. [P8] **The competitors are therefore this planform with two add-ons, not independently designed aircraft of their families.** [J9] All three carry the same buffered series-hybrid power system, so Bill 3 is held common and the comparison measures mass and cruise drag. [P10] **Holding Bill 3 common is a choice of question, and it has a direction.** [P11] **The choice runs against this configuration.** [R12] Without the buffer, and with engines rated to deliver the hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off mass and falls 38 to 47 percent behind under a fixed fuel mass, and the tilt bound does not close under a fixed take-off mass; under a fixed fuel fraction it closes at 520 kg, about ten times this configuration's mass — the first contract's blindness to mass, made visible. That comparison is not used, because it would set competitors without a store against this configuration with one.
> 
> [J13] The basis is not symmetric: the lift-plus-cruise layout carries a lift-to-drag ratio transferred from a different airframe's wind-tunnel campaign (Section 2) and assumes lift rotors stopped and aligned in cruise, which takes an indexing mechanism (Section 7) whose mass is not separately charged. [P14] **The tilting layout carries no cruise drag penalty at all. That is an idealisation in its favour**, and it is deliberate: it makes the tilting layout a bound. [J15] Both competitors use a propeller efficiency of 0.80, assumed, not computed, against this configuration's computed 0.632 and 0.683; the lift-plus-cruise layout carries a lift group of 10 percent of take-off mass and the tilting layout a tilt mechanism of 5 percent. [P16] **Neither figure is measured.**
> 
> ### Against lift-plus-cruise: a trade, and the contract sets the exchange rate
> 
> [J17] **The two architectures trade one charge against another**: closed under a fixed fuel fraction, this configuration is 27 to 30 percent lighter, and the lift-plus-cruise layout cruises at a lift-to-drag ratio of 11.66 and 15.72 against 8.79 and 10.82, with a propeller at 0.80.
> 
> *(Table 5 when assembled — the contracts table, rows A–D, unchanged.)*
> 
> [J18] **The lift-plus-cruise layout is 55 to 84 percent ahead under the first contract, 28 to 54 percent under the second, and between 13 percent short and 7 percent ahead under the third; the shift from first to third is 67 to 77 percentage points at every closure**, at the declared lift-group fraction, and always toward the lighter aircraft. [D19] **The sign itself changes inside the envelope under the third contract**: this configuration is ahead at the two closures with the higher-efficiency blade family and behind at the two with the lower. [D20] **A statement of which architecture has the longer range, made without its contract, would therefore be a statement about the contract.**
> 
> ### Against the tilting layout: a bound, not a ranking
> 
> [P21] **What the bound gives is a size, not an order.** [J22] Credited with no cruise penalty, the tilting layout is 93 to 141 percent ahead of this configuration under every contract at every closure; that margin is the room a real tilting aircraft's cruise penalties — nacelle drag, pivot fairing, hover-sized rotors flown as cruise propellers — would have to fill, and [P23] how much of it they fill is not computed. [P24] **A ranking against a competitor modelled as a bound is not a ranking, and no range claim is made against the tilting family in either direction.**
> 
> ### Section 2's prediction, tested
> 
> [J25] Section 2 predicted that such a ranking will move when the sizing rule changes, and can reverse. **The movement holds everywhere**, against both competitors, toward the lighter arrangement as the contract weights mass more; **the reversal holds at two of the four closures against lift-plus-cruise, and at none against the tilt bound.**
> 
> [D26] **Where the reversal falls is decided by quantities this study has not measured or not fixed**: the blade family in the base case, and across the sensitivity cases the competitor's lift-group mass and the propeller basis (Supplement S13). [D26b] With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every closure; with a heavier one this configuration leads under a fixed take-off mass at every closure; with a common propeller efficiency a reversal appears at every closure. [P27] **Which architecture ranks first under a fixed take-off mass is therefore decided, in this model, by a mass fraction of the competitor that this study has not measured.** [P28] **Put plainly, the sign under a fixed take-off mass is not a result about the architectures; it is a result about that parameter**, and it is the one most worth measuring. [D29] What is robust is that the shift exists and runs toward the lighter aircraft; its size is the size of the mass difference.
> 
> ### What the framework asks of whoever uses it
> 
> [D30] **Each comparison states every charge in its own currency before any aggregate, names its contract, and states its asymmetries and their directions; an ordering is reported only with the contract it was computed under and, where its sign depends on an unmeasured quantity, with that quantity named.** [D31] This paper meets that for its own column (Section 11) and not for the competitors', whose kilograms and drag counts here are parameters and transferred ratios rather than an audit.
> 
> ### What this section does not establish
> 
> [J32] **The competitors are modelled at a coarser level than this configuration**: their drag is transferred or idealised, their propeller efficiency assumed and their architecture-specific mass a parameter. [P33] **Comparing computed figures against assumed ones favours whichever is assumed more optimistically** — in propeller efficiency both competitors, and with a common propeller efficiency the lift-plus-cruise lead under the first contract falls from 55–84 to 33–45 percent (Supplement S13); in drag the tilting layout, by construction. [D34] **The comparison is at one size**: Section 12's 1 000 kg reference design has no closure, and none of its figures is used here. [P35] **And nothing here ranks architectures for a mission.** [D36] What this section establishes is narrower: **the same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property of the architectures alone.

---

## 4. Where you still differ — answer one another (the author's request)

**(a) The length expectation**, for the redistribution the author will make later. The four positions:
- **Grok:** 40 % is right while protected sentences and their antecedents stay; do not raid Steps 5–8.
- **ChatGPT:** no ratio is a target; draft first, then measure.
- **DeepSeek:** raise the calculation budget to about 2 500, taken first from the framework (Sections 2.1–2.3).
- **Qwen:** Steps 12 and 13 must reach 20–25 %.

**The drafts now bear on this directly**, at 57 % and 60 % with no rule-(iii) candidate:
- Qwen, which of these sentences would you cut to reach 25 %, and does each cut pass the finding-or-calculation test?
- DeepSeek, which framework sentences would pay for the difference?
- Grok and ChatGPT, answer them.

**(b) Step 12 — "two costs that scale does not relieve"** (J29, J30, D31; about 95 words).
- **DeepSeek:** body.
- **ChatGPT:** supplement.
- **Qwen:** brief, or supplement.
- **Grok:** silent.
- **The draft:** brief, in the body. **My reason:** *"A larger aircraft of this type turns more slowly, and must"* is a scale finding about the
  architecture itself, and it is the only place the transition's scale law is stated.
- **To ChatGPT and Qwen:** is that reason enough? **To DeepSeek:** would you keep J30–D31 and let J29 go, since the fixed-pitch gap is
  in Step 11 already?

**(c) Step 12 — the Bill 3 ratio paragraph** (J8 + P9).
- **Qwen:** a rule-(iii) candidate, with caution.
- **DeepSeek:** body.
- **ChatGPT:** move the calculation, keep the result.
- **The draft:** keeps the result (5 to 14 %, on the engine margin) and P9; the margins and the 60.0 kW case go to S12.
- **To Qwen:** is P9 still needed once the margins are gone? It keeps Step 12's 4.19 apart from Step 11's 2.4–3.2 (the Round 60
  correction), so I think yes.

**(d) Step 13 — R12, the no-store comparison and 520 kg** (about 95 words).
- **Grok vetoed deleting the 520 kg sentence in Round 70**, as this step's own finding and the premise of *"That comparison is
  not used"*.
- **DeepSeek and ChatGPT:** asymmetry and competitor detail to the supplement.
- **The draft keeps R12, compressed.** Under the supplement rules, a move is not a deletion.
- **To Grok:** does your Round 70 reason still hold when the sentence would move to S13 with its premise, leaving P10 and P11 in
  the body? **To DeepSeek and ChatGPT:** does the body still need the fact that the choice *runs against* this configuration, which
  P11 asserts and R12 shows?

**(e) Step 13 — the asymmetry detail** (J13, J15).
- **Qwen:** keep the qualifiers in the body.
- **DeepSeek and ChatGPT:** detail to the supplement.
- **The draft:** keeps the qualifiers (P14, P16) and one clause each of what they qualify.
- **To each of you:** is *"transferred from a different airframe's wind-tunnel campaign"* a qualifier (body) or detail (supplement)?

---

## 5. New proposals, to vote

- **ChatGPT — contract identity for Step 13.** A Step 13 figure is valid only with configuration + competitor + contract +
  sensitivity state. My view: yes. T5's caption and D26b already carry it; I would add it as a field of the Step 13 outbound map.
- **Qwen R105-P2 — record the known coincidences once**, so the check stops re-flagging them. Examples: Step 13's +53.5 % against
  Step 10's 53.5 kg; 11.66 as an L/D against 11.66 kW; 17 as an L/D against 17 m. My view: yes, as a reviewed list, like
  `v8-refs-reviewed.md`.
- **Grok P78 — Step 12 must not bring Bill 1 back** through a phrase such as *"the last two at two scales"*. My view: yes.
  D33 (*"the third need not be shown separate"*) and P26 hold it.
- **Qwen R105-P3** is R104-P2, already adopted.

---

## 6. To vote

| # | Item | My vote |
|---|---|---|
| a | Confirm Step 11 as applied | confirm |
| b | Step 12 draft: veto any sentence by number (J/R tags included) | no veto |
| c | Step 13 draft: veto any sentence by number; R12 especially | no veto |
| d | §4 (a)–(e): answer one another | as stated there |
| e | §5 proposals | yes |

---

## 7. Your own proposals

As always: anything you see, with your reason. They go side by side to everyone next round.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
