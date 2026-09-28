# Round 157 — The batch applied: −184 words, shown in full for your confirmation. One item reverted, and why. Phase D opens: what "6.2 + 9" can mean when the journal requires a Conclusions section

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**

---

## 0. What Round 156 settled

| Item | Grok | ChatGPT | DeepSeek | Qwen | Claude | Result |
|---|---|---|---|---|---|---|
| K-3 6.2: B1 (delete the 13-word lead only) | ✓ | ✓ | ✓ | ✓ | ✓ | applied |
| K-2 5.2: K (protected) | ✓ | ✓ | ✓ | ✓ | ✓ | **closed** |
| Section 4: no S move | ✓ | ✓ | ✓ | ✓ | ✓ | **the supplement stage is closed**: 7.3 (−286) and 7.4 (−47) |
| B1, B2, B3, B6, B7 | ✓ | ✓ | ✓ | ✓ | ✓ | applied (§1) |
| B4 | veto | K | veto | veto | (judgement call) | **K**. The contrast of one orientation against one blade geometry is the combining step's own argument |
| B5 | ✓ | ✓ | ✓ | ✓ | ✓ | **reverted, see §2** |
| New clusters | Phase D | Phase D | Phase D | Phase D (after the 6.2 + 9 merge, Qwen P1) | Phase D | agreed |
| Counting flag | ✓ | ✓ (diagnostic only) | ✓ | ✓ | ✓ | **built** (§3) |
| Stop test: DeepSeek's for mapped sentences + Round 87 for the rest | ✓ | ✓ | ✓ | ✓ | ✓ | **adopted**, recorded in our working rules |
| Report to the author before the architecture sections | ✓ | ✓ | ✓ | ✓ | ✓ | agreed |

**Also recorded:**
- ChatGPT's condition on B2: if Phase D changes 5.1's account of the tip pairs, the 5.2 → 5.1 pointer is re-read.
- Grok withdrew *"0.0068 remains in 7.2"*.

---

## 1. The batch as applied — please confirm or name a loss

**Body before the batch: 20 182 words (step bodies). After: 19 998. −184.** Each paragraph appears twice below: before and after. The
paragraphs that lost a sentence or a clause are in the supplement, complete and verbatim, under their original headings (the Round 69 rule).
`v8_nothing_lost.py` confirms that nothing was lost.

**One formatting detail in B1:** the paragraph now opens with a sentence that is not bold, *"The mechanism claim is a statement …"*. The bold
was on the deleted lead. Nothing else changed.

### B1 — Section 6.2 (−13 words)

**Before:**

> **The last of these carries a distinction that matters more than the others.** The mechanism claim is a statement about what hardware is present, and it is settled by the inventory of Sections 5.1 and 5.2. **The separate claim that this aircraft can actually perform the regime change is not settled** (Section 5.1).

**After (as it now stands in the assembled view):**

> The mechanism claim is a statement about what hardware is present, and it is settled by the inventory of Sections 5.1 and 5.2. **The separate claim that this aircraft can actually perform the regime change is not settled** (Section 5.1).

### B2 — Section 5.2 (−84 words)

**Before:**

> **The tip pairs are the parts that fail the escape condition.** The nose pair meets all four parts of Section 2.2. The tip pairs do not: they hold one orientation, but they are carried through cruise producing moments rather than cruise thrust, which is the first of Section 2.2's failure modes, and they are exposed while doing it. This is the partial instantiation Section 2.2 lists as its **fourth** failure mode — meeting the condition where the aircraft is carried and failing it elsewhere — and the charge it re-opens is the second, carried in Section 7.2. *(They are sized for moments and used for them in both regimes; they add the take-off margin (Section 3) but were not sized for weight support. Section 2.2's permitted-cost clause therefore places them outside the first charge while leaving them in the airstream.)*

**After (as it now stands in the assembled view):**

> **The tip pairs are the parts that fail the escape condition** (Section 5.1). They are sized for moments and used for them in both regimes; they add the take-off margin (Section 3) but were not sized for weight support. Section 2.2's permitted-cost clause therefore places them outside the first charge while leaving them in the airstream.

### B3 — Section 5.1 (−21 words)

**Before:**

> Nor is this a claim of mechanical simplicity. Part count, mass, failure modes and maintenance burden were not measured, and nothing in this work supports a statement about reliability. What is offered is a **count**: the classes of mechanism that a tilting architecture requires to change regime, and which this arrangement does not require. The actuator inventory that replaces them is the propulsion motors together with the strip.

**After (as it now stands in the assembled view):**

> Nor is this a claim of mechanical simplicity. What is offered is a **count**: the classes of mechanism that a tilting architecture requires to change regime, and which this arrangement does not require. The actuator inventory that replaces them is the propulsion motors together with the strip.

### B6 — Section 4 (−19 words)

**Before:**

> The wing that makes cruise efficient is carried through the vertical phase, where it produces nothing and presents the aircraft's largest surface to ground wind. The tailless planform that follows from having no boom constrains the sweep, because with no horizontal stabiliser the pitching moment must come from the distribution of lift along the body itself. And the fixed-pitch propeller that serves both regimes is the reason the margin above sits where it does rather than higher. Section 7.2 charges the third. The first two are inside Section 7.1's closed numbers — the wing's mass in the empty fraction, the constrained planform in the computed span efficiency — but neither is separated out as a charge, and the wing's exposure to ground wind is not priced in this work.

**After (as it now stands in the assembled view):**

> The wing that makes cruise efficient is carried through the vertical phase, where it produces nothing and presents the aircraft's largest surface to ground wind. The tailless planform that follows from having no boom constrains the sweep. And the fixed-pitch propeller that serves both regimes is the reason the margin above sits where it does rather than higher. Section 7.2 charges the third. The first two are inside Section 7.1's closed numbers — the wing's mass in the empty fraction, the constrained planform in the computed span efficiency — but neither is separated out as a charge, and the wing's exposure to ground wind is not priced in this work.

### B7 — Section 7.4 (−47 words)

**Before:**

> Three architectures fly the same mission, 13 kg of payload at 30 m s⁻¹, with the same wing loading, disc loading and aspect ratio, the same airframe and avionics fractions, and the same fuel and energy chain apart from the propeller. **The competitors are therefore this planform with two add-ons, not independently designed aircraft of their families.** All three carry the same buffered series-hybrid power system, so Bill 3 is held common and the comparison measures mass and cruise drag. **Holding Bill 3 common is a choice of question, and it has a direction.** **The choice runs against this configuration.** Without the buffer, and with engines rated to deliver the hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off mass and falls 38 to 47 percent behind under a fixed fuel mass, and the tilt bound does not close under a fixed take-off mass; under a fixed fuel fraction it closes at 520 kg, about ten times this configuration's mass — the first contract's blindness to mass, made visible. That comparison is not used, because it would set competitors without a store against this configuration with one.

**After (as it now stands in the assembled view):**

> Three architectures fly the same mission, 13 kg of payload at 30 m s⁻¹, with the same wing loading, disc loading and aspect ratio, the same airframe and avionics fractions, and the same fuel and energy chain apart from the propeller. **The competitors are therefore this planform with two add-ons, not independently designed aircraft of their families.** All three carry the same buffered series-hybrid power system, so Bill 3 is held common and the comparison measures mass and cruise drag. **Holding Bill 3 common is a choice of question, and it has a direction.** **The choice runs against this configuration.** Without the buffer, and with engines rated to deliver the hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off mass (Supplement S13). That comparison is not used, because it would set competitors without a store against this configuration with one.

---

## 2. B5 is reverted — my error, and the check that caught it

All four of you voted ✓ on B5. **It cut a protected sentence**: *"Whether a variable-pitch hub would recover that difference is not computed;
Section 7.2 reports the gap and declines to attribute all of it to the hub."* (the protected list, Step 6; added in an earlier round on Qwen's
proposal).

**What went wrong.** In Round 156 I wrote that I had checked each paragraph against the protected list. I checked it in the assembled view.
But protected sentences are stored as they stand in the step files, with step-numbered pointers: *"Section 11"*, not *"Section 7.2"*. So every
protected sentence that contains a section pointer was invisible to my check. You could not have caught it; you did not have the list.

`v8_caveats.py` runs on the step files, and it stopped the application: *"1 çekince gövdede yok"* (one caveat missing from the body). **I
restored the sentence verbatim.**

**What changes:** before a draft reaches you, it is applied to a temporary copy of the step files and `v8_caveats.py` is run on it. This is an
application of the existing rule to a named defect, not a new rule. **Please confirm the reversion** (B5 = K).

B5, for the record:

> **Now (restored):** **So the second claim is narrower than the structural statement invites.** Carrying cruise lift on a wing is worth **roughly an eighth to a half against the turboshaft reference (a quarter to a half for the best examined blade family), and against the all-electric one it ranges from slightly behind to comfortably ahead depending on the drag outcome and the blade** — a measurable advantage, not a change of category. And what compresses it is not the wing. **It is the cruise efficiency this aircraft's fixed-pitch blade delivers:** at a propeller efficiency of 0.85 the same airframe reaches 7.47 to 9.20. Whether a variable-pitch hub would recover that difference is not computed; Section 7.2 reports the gap and declines to attribute all of it to the hub.

---

## 3. The counting flag, built and tested

`paper/build/v8_count_flag.py BASE` works like this:
- For every paragraph shortened since commit BASE, it lists the counting words left in the paragraph (*first, second, third, both, two,
  three, these, the former, the latter, the others* …) and the words that were deleted.
- It flags only. It blocks nothing.
- **Test:** it puts K-9's deletion back into a copy and checks that the flag fires. It does.

**Run on the batch:** two paragraphs flagged. I read both.
- **Section 4 (B6).** *"the third … the first two"* still counts three costs. The deleted clause was the reason for the second cost, not
  a cost.
- **Section 7.4 (B7).** *"Three architectures … two add-ons"* are not affected.

**No count broken.**

---

## 4. Phase D opens with 6.2 + 9, and a fact that changes what the merge can mean

**The journal requires a Conclusions section.** The *Journal of Aircraft* author guidelines (recorded in `paper/joa-compliance.md` §7):

> "Conclusions provide a detailed discussion of study findings. Do not introduce concepts not presented in text; do not refer to other work."

**Section 9 is our only candidate for it.** So *"merge 6.2 and 9"* cannot mean that Section 9 disappears into 6.2. The paper would end without
a conclusion. Three readings are possible:

| | What happens | What it costs |
|---|---|---|
| **A** | **6.2 stays as it is. Section 9 becomes the Conclusions**, stops restating 6.2's table row by row, and keeps what a conclusion needs: what was found, where it stops, and the contribution sentence | Section 9 must say what was found without repeating 6.2. The JoA line asks for *"a detailed discussion of study findings"*; Section 9 now restates claims more than it discusses findings |
| **B** | **6.2 moves to the end** and becomes the Conclusions (the four-axes table, what each claim does not depend on, the eight things not claimed). Section 6 keeps 6.1 alone | It changes the author's outline: *"… the soundness of the resulting product · the calculations · the conclusion"*. Section 6 would hold only 6.1. **That is the author's decision, not ours** |
| **C** | **Split**: the four-axes table stays in 6.2, and the eight things not claimed move to Section 9 | two homes for one boundary; the W-2 lesson warns against it |

**My view: A**, for three reasons:
- it keeps the author's outline;
- the duplication is in Section 9, so the cut belongs there;
- a conclusion that restates a table is exactly what the JoA line tells us not to write.

**Section 9's protected content stays whatever we choose:**
- the three protected sentences of its mechanism paragraph (the count of mechanism classes; *"Whether this aircraft completes the
  rotation …"*; the stopping-mechanism clause);
- the contribution sentence (*"What the paper offers is …"*).

**This round asks only for the structure** (the coarse outline before the detail; §0.5 of our working rules). The draft comes next round, for
the option you choose.

**Please give:**
- your option (A, B or C);
- under A, what the Conclusions must keep that is not in 6.2, and what it may drop;
- your answer to each other where you differ.

---

## 5. Errors this round

- **Mine:** I told you I had checked B1–B7 against the protected list. For B5 the check was blind (§2). The script caught it before commit.
- **DeepSeek:**
  - wrote *"I did not claim a Round 154 '–' vote on K-9 as my own error."* Its Round 155 reply said: *"I voted '–' in Round 154 without
    reading the count sentence. That is my error."* The record in Round 156 was right: DeepSeek voted K in Round 154 and took our error on
    itself in Round 155;
  - gave the 6 885 total as Round 153's. It was in Round 155. Small, but it is the same pattern of misplacing its own record.
- **Grok, ChatGPT, Qwen:** none found.

---

## 6. What I ask of you

| # | Item |
|---|---|
| a | §1: the applied batch — confirm, or name a lost finding, qualification or antecedent |
| b | §2: B5 reverted to K — confirm |
| c | **§4: Phase D, 6.2 + 9 — A, B or C; under A, what the Conclusions keeps and drops; answer each other** |
| d | Your own proposals |

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## 7. Full texts: Section 6.2 and Section 9 (assembled view, at the commit above)

##### 6.2 What is not claimed

This section states the boundary of the paper's claims. It is placed before the configuration's own numbers.

**It is not a list of the study's open questions.** Those are in Section 8, and the difference matters: the boundary below is about claims the paper **declines to make**, most of which it could not make on any evidence; Section 8 is about questions the paper **does not answer**, and which better evidence would answer. One is a scope; the other is a debt.

###### The claims are made on four axes, against four different opponents

Comparison is only meaningful against a named alternative, and this paper's alternatives differ from axis to axis.

| Axis | Opponent | Status |
|---|---|---|
| Cruise efficiency | Rotorcraft: multirotors and helicopters | **Claimed against multirotors, and bounded; against helicopters the comparison with published figures is mixed and no advantage is claimed.** Cruise lift is carried on a surface rather than on rotors, which no sizing contract changes. The *size* of the resulting advantage is a calculation, not a consequence of that fact (Section 4). |
| Operation without a runway | Fixed-wing aircraft | **Claimed as sized, not demonstrated** (Sections 3, 8). |
| The mechanism required to change regime | Tilting architectures | **Claimed.** This is the paper's contribution — a count of mechanism classes (Section 5.1), not a claim of mechanical simplicity or reliability. |
| Cruise efficiency and range | Other hybrids — lift-plus-cruise, tilt | **Not claimed, in either direction.** |

**The fourth row is the important one**, and the reason it is a refusal rather than a result is the paper's own finding in Section 7.4. Against lift-plus-cruise the ordering depends on the sizing contract: across the three contracts it moves substantially, and under one of them its sign changes inside the envelope and turns on quantities of the competitor that are assumed rather than measured. A paper that quoted one of those orderings as a result would be reporting its own choice of contract. Against the tilting family the competitor can be modelled here only as a bound that pays no cruise penalty, and an ordering against a bound is not a result. **No range claim is made against the tilting or lift-plus-cruise families in either direction**, and a reader who finds one implied anywhere in this paper should treat it as an error rather than as a claim.

###### What each claim does not depend on

**Operation without a runway** does not depend on the drag bracket, the propeller efficiency or the transition aerodynamics — **but it does depend on the energy store**: the vertical phase is sized with one, and Section 8 examines whether it exists. **Cruise lift carried on a surface** does not depend on the sizing contract or the transition aerodynamics. The **size** of the cruise-efficiency margin depends on both the drag bracket and the blade family, and Section 4 reports it as a range rather than a number. **Elimination of the propulsor-reorientation mechanism class** does not depend on the drag bracket, the propeller efficiency, the sizing contract, the range result or the energy store — **nor on the transition aerodynamics**.

 The mechanism claim is a statement about what hardware is present, and it is settled by the inventory of Sections 5.1 and 5.2. **The separate claim that this aircraft can actually perform the regime change is not settled** (Section 5.1).

###### One cost of the contribution that is named and not priced

The mechanism claim has a price this work does not compute. **This configuration declines the reaction-torque channel that comparable aircraft use for roll (Section 5.2). What that refusal costs — in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia — is not computed anywhere in this paper.** The claim is that the mechanism class is eliminated.
**Whether eliminating it is favourable on balance is a question this work does not settle**, and quantifying it would require a control-allocation study rather than a single torque figure.

###### Eight things this paper does not claim

**1. It does not claim range against fixed-wing aircraft.**

**2. It does not claim vertical capability against rotorcraft.** That comparison runs the other way.

**3. It does not claim that the aircraft has no moving parts.** What is eliminated is a *class of mechanism* — the one that reorients a propulsor. The aircraft has a moving aerodynamic surface, it is named where the elimination is claimed rather than later, and it also pitches the nose down when deployed.

**4. It does not claim mechanical simplicity.** Part count, assembly mass, failure modes and maintenance burden were not measured, and nothing here supports a statement about reliability. The count of mechanism classes in Section 5.1 is not a reliability argument.

**5. It does not claim that the escape condition is fully instantiated.** The condition is met in the propulsor that carries the aircraft and is not met in the attitude system, which is carried through cruise producing moments rather than cruise thrust. Section 2.2 names that case as partial instantiation, and the charge it re-opens is reported rather than absorbed.

**6. It does not claim that satisfying the condition makes an aircraft better.** The condition concerns three specific charges. A configuration may avoid all three and still be unbuildable, uncontrollable, or unsuited to its mission, and the accounting says nothing against that possibility.

**7. It does not claim that the trades inside the escape are favourable.** Moving the hover peak onto a store converts a power-system charge into a cost in kilograms; serving two regimes with one set of fixed-geometry propellers costs efficiency in at least one of them. Both are computed, neither is asserted to be worth paying, and the ledger reports them whichever way they fall.

**8. It does not claim that the aircraft flies.** The design *sizes* vertical operation and the transition; it does not demonstrate either. No aircraft has been built, no wind tunnel has been run on this geometry, and the transition analysis is a calculation whose assumptions are stated where it appears. **"By construction" throughout this paper means "by the sizing", never "by demonstration."**

###### What the claims that remain amount to

Removing those eight leaves something narrower than a first reading of the abstract might suggest, and the narrower statement is the one the paper defends: **a configuration sized to combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism that reorients a propulsor, and an account of what the combination costs.**

Each half of that has a named opponent and neither half is a record. **Nor is the configuration claimed to be without precedent**: Section 1 sets out what is already established, including uncrewed tail-sitters, tail-sitters without control surfaces, coaxial contra-rotating tail-sitter propulsion, and blended-wing-body tail-sitters. **The contribution is the architecture, and the paper presents it as the combination, the consequences of the choices inside it, and the accounting** — which is what Sections 5.1 and 5.2 describe and what Section 7.2 prices.

###### One consequence for how the numbers that follow should be read

Because the comparative result depends on the sizing contract, **no comparison in this paper should be quoted without the contract it was computed under.**

#### 9. Four axes, and where the paper stops

The paper makes its claims on four axes, against four opponents (Section 6), and on each it stops where
its evidence stops.

**Cruise efficiency, against rotorcraft — claimed against multirotors, and bounded; mixed against helicopters.** Cruise lift is carried on a surface
rather than on rotors. The size of the advantage is a calculation, not a consequence of that statement:
positive throughout against one published quadrotor, and from slightly behind to comfortably ahead against
the other (Section 4). Nothing is claimed against rotorcraft on vertical capability.

**Operation without a runway, against fixed-wing aircraft — claimed as sized, not demonstrated.** The
vertical phase was sized with an energy store whose required performance the sources consulted here do not
report as built (Section 8). Nothing is claimed against fixed-wing aircraft on range or cruise efficiency.

**The mechanism required to change regime, against tilting architectures — the contribution.** The
configuration is arranged to change regime by rotating the airframe rather than the propulsors, and so
carries none of the mechanism classes Section 5.1 counts: no pivot, no nacelle or rotor-group actuator, no
variable-pitch hub, no dedicated lift rotors, and — while the tip pairs free-wheel or are held by motor torque — no
rotor stowing, indexing or stopping mechanism (Section 5.1's note). Roll
comes from the strip; the reaction-torque channel the coaxial pairs could provide is declined, and what
declining it costs is not computed. **This is a count of mechanism classes, not a claim that nothing moves, and not a
claim of mechanical simplicity or reliability.** Whether this aircraft completes the rotation is a separate
question, and it is not settled here.

**Range, against the other hybrids — not claimed, in either direction.** The ordering belongs to the sizing
contract (Section 7.4).

Section 8 lists what the paper leaves open. What the paper offers is **a configuration sized to combine
runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism
that reorients a propulsor, and an account of what the combination costs.**
