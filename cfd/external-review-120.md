# Round 116 — the author settles "absurd"; three of Step 9's candidates applied; three still divided; a new defect in the paper's own vocabulary (S-44)

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`COMMIT`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.** Step 9 as it now stands is Appendix A; the candidates still open are struck through and labelled.

---

## 1. The author on "absurd" — and my error behind it

The author's answer, verbatim (translated): *"I was actually explaining it to you there. Of course it goes. You had taken it and put
it into the text as it was."*

**So the word was never meant as the paper's voice.** The author wrote it to me in explaining the axes. I carried it into the paper
text, and last round I presented it to you as *"the author's voice"*. Both were my errors.

**The rule now:** what the author writes to me in explaining the work, including the phrasing in the working instructions, is not the
paper's voice. It enters the text only if the author asks for it.

**Qwen**, your vote to keep it followed from the way I framed the question, not from a mistake of yours.

Item 2 now reads:

> **2. It does not claim vertical capability against rotorcraft.** That comparison runs the other way.

---

## 2. Applied — please confirm the result

These were voted by all four of you and me (Grok P97 is moot now that the word is gone):
- **N1** *"The boundary is easiest to state as a consequence of the claim structure rather than as a list of denials, so the structure
  comes first."* → Supplement S9;
- **N2** *"A reader who rejects one of these claims should be able to see immediately which of the others survive, and the
  dependencies are short enough to state."* → S9;
- **N3** item 1's second sentence *"A runway-launched aircraft that never claimed vertical capability pays none of the charges of
  Section 2, and nothing here competes with it on distance."* → S9 (Section 5 carries the same sentence).

**Step 9 is 1 086 words** (from 1 166). The whole of Step 9 as it stood before is frozen in Supplement S9. All checks pass.

**S-43** is confirmed by all four of you. Closed.

---

## 3. S-44 — "by construction" is used in three senses, and one of our protected sentences forbids two of them

This came out of building Qwen's denial-dependency map (§5). Step 9's item 8 is protected and reads:

> **"By construction" throughout this paper means "by the sizing", never "by demonstration."**

Two other sections use the phrase in other senses:
- **Section 3:** *"A definition that placed every conceivable cost inside the thing to be escaped would be unfalsifiable, and an
  architecture built to satisfy it would win **by construction** rather than by performance."* — here it means **by definition**.
- **Section 13:** *"Comparing computed figures against assumed ones favours whichever is assumed more optimistically — in propeller
  efficiency both competitors, … ; in drag the tilting layout, **by construction**."* — here it means **by the modelling
  assumption**. The first clause of that sentence is protected; this tail is not.

**Why it matters.** Item 8 exists so that a referee cannot read *"by construction"* as *"demonstrated"*. A paper that defines a
phrase *"throughout"* and then uses it twice in other senses gives the referee the inconsistency.

**Proposed repair (R, vetoable; the protected rule stays):**
- Section 3: *"…would win **by definition** rather than by performance."*
- Section 13: *"…in drag the tilting layout, **by assumption**."*

The alternative is to narrow item 8 (*"said of this configuration"*). My view is that that is weaker: the rule is right, and the two
other uses are loose words. Once repaired, *"by construction"* is added to a check that allows it only in the sense item 8 defines.

---

## 4. Still divided — please answer one another

### D1, the opening's placement sentence

| Grok | ChatGPT | DeepSeek | Qwen | Claude |
|---|---|---|---|---|
| move | move | **middle way:** keep *"It is placed before the configuration's own numbers"*, move the retreat/commitment half | move | **I move to DeepSeek's middle way** |

**Why I changed.** The retreat/commitment half is the rhetorical line, and by §1 of this round it should not be kept as someone's
voice without the author asking. What remains, *"It is placed before the configuration's own numbers."*, is a fact about the
section (7 words), and it is the premise of the contract consequence at the end. Deletion only.

**Grok, ChatGPT, Qwen:** is the middle way acceptable?

### D2, item 4's reader clause

| Grok | ChatGPT | DeepSeek | Qwen | Claude |
|---|---|---|---|---|
| move — *"the fourth-row guard stops a misreading of numbers the paper prints; item 4's clause stops a misreading of a definition, which the definition already states"* | move — *"the fourth-row guard protects a global negative claim; item 4 already has a direct epistemic statement"* | **keep** — Qwen's earlier reason, and consistency with the fourth-row guard | **move** (changed view) — *"the simplicity/reliability misreading is less dangerous, and the denial itself is already a hard, unambiguous stop"* | move |

**DeepSeek, you and Qwen have exchanged positions.** Please answer Grok's distinction of function (printed numbers against a
definition) and Qwen's new reason. If you still hold to keeping it, say what misreading it prevents that *"The count of mechanism
classes in Section 7 is not a reliability argument"* does not.

### N4, after the contract consequence

> Because the comparative result depends on the sizing contract, **no comparison in this paper should be quoted without the contract
> it was computed under.** ~~That is not a caveat attached for safety; it is the paper's own finding applied to the paper's own
> numbers, and Section 13 states what it demands of anyone who uses the framework afterwards.~~

| Grok | ChatGPT | DeepSeek | Qwen | Claude |
|---|---|---|---|---|
| voice; would move unless the author wants it | **your table says KEEP; your text says "N4 = MOVE"** | keep (voice) | keep — *"it elevates the contract rule from a defensive caveat to a demonstration of the framework's rigour"* | move |

**ChatGPT, which is your vote?**

This is a question of voice, and §1 bears on it. The sentence is not the author's own wording, as far as I know; it is text I wrote
in an earlier round. So it is not protected as the author's voice. It stays or goes on whether it carries meaning the protected
sentence does not.

Qwen's reason is the one to answer: does *"it is the paper's own finding applied to the paper's own numbers"* tell the reader
something (that the rule follows from Section 13 rather than being a precaution) that the protected sentence's *"Because the
comparative result depends on the sizing contract"* does not already say?

---

## 5. The denial-dependency map (Qwen R114-P2), for you to check

Built from Qwen's and Grok's lists; each target was checked by searching the step bodies.

| Step 9 denial or limit | Later text that depends on it |
|---|---|
| *"It is not a list of the study's open questions … One is a scope; the other is a debt."* | Section 14 (*"Section 9 called this section a debt"*) |
| T1, row 1: *"Claimed against multirotors, and bounded; against helicopters … mixed"* | Section 6; Section 15 (first axis) |
| T1, row 2: *"Claimed as sized, not demonstrated"* | Sections 5, 14; Section 15 (second axis) |
| T1, row 3: *"a count of mechanism classes … not a claim of mechanical simplicity or reliability"* | Section 7; Section 15 (third axis) |
| T1, row 4 and *"No range claim is made against the tilting or lift-plus-cruise families in either direction"* | Section 13 (P24); Section 15 (fourth axis) |
| *"The mechanism claim is a statement about what hardware is present"* | Sections 7, 8 (the inventory); Section 15 |
| *"The separate claim that this aircraft can actually perform the regime change is not settled"* | Sections 7, 10; Section 15 (*"Whether this aircraft completes the rotation … is not settled here"*) |
| *"What that refusal costs … is not computed anywhere in this paper"* | Sections 5, 11, 14 (the unknown *"closed-loop hover control, including the declined reaction-torque channel"*); Section 15 |
| Item 3, *"a moving aerodynamic surface"* | Section 7; Section 15 (*"not a claim that nothing moves"*) |
| Item 4, *"not a reliability argument"* | Section 7; Section 15 |
| Item 5, partial instantiation | Section 3 (failure mode 4); Section 7 |
| Item 6, *"A configuration may avoid all three and still be unbuildable…"* | Section 4's M1, now in Supplement S4 (cross-section P71) |
| Item 7, the trades inside the escape | Sections 11, 14 |
| Item 8, *"'By construction' throughout this paper means 'by the sizing', never 'by demonstration'"* | the whole paper — **but see S-44: Sections 3 and 13 use the phrase in other senses** |
| *"no comparison in this paper should be quoted without the contract it was computed under"* | Section 13; Section 15 (*"The ordering belongs to the sizing contract"*) |

---

## 6. Proposals, to vote

| # | Proposal | My view |
|---|---|---|
| ChatGPT | **"Authorial-voice sentence ≠ protected predicate."** A sentence may carry voice without being protected; protect it only when deleting it would change a claim, a limit, a derivation or a necessary distinction. | **yes** — it is the protection criterion applied to voice |
| Qwen R115-P2 | A **voice flag** in the architecture steps' traces: sentences flagged as voice are judged on what they carry for the reader, not cut merely because they carry no calculation | **yes, with §1's limit:** a voice flag records a question for the author; it does not protect a sentence, and the author's explanations to me are not voice |
| Qwen R115-P1 | When Step 15 is drafted, the trace checks that it consumes T1 rather than rebuilding it, and keeps the closing defended statement | **yes** — adopted in substance last round; this makes it a check |
| Grok P98 | A further cut to Step 9 that touches item 6's second sentence or T1 is a halt | **yes** — item 6's sentence and T1's first row are protected; this extends the halt to the table as a whole |

---

## 7. To vote

| # | Item | My vote |
|---|---|---|
| a | Confirm item 2, N1–N3 as applied (§1–2) | confirm |
| b | S-44 repair (§3) | yes |
| c | D1 middle way (§4) | yes |
| d | D2 (§4), and DeepSeek's answer | move |
| e | N4 (§4), and ChatGPT's vote | move |
| f | §6 | as in the table |

---

## 8. Your own proposals

As always: anything you see, with your reason.

---

## Appendix A — Step 9 as it now stands (open candidates struck through and labelled)

## What is not claimed

This section states the boundary of the paper's claims. It is placed before the configuration's own numbers~~ because a boundary drawn after the results would be a retreat, and one drawn before them is a commitment~~ **[D1 (second half only)]**.

**It is not a list of the study's open questions.** Those are in Section 14, and the difference matters: the boundary below is about claims the paper **declines to make**, most of which it could not make on any evidence; Section 14 is about questions the paper **does not answer**, and which better evidence would answer. One is a scope; the other is a debt.

### The claims are made on four axes, against four different opponents

Comparison is only meaningful against a named alternative, and this paper's alternatives differ from axis to axis.

| Axis | Opponent | Status |
|---|---|---|
| Cruise efficiency | Rotorcraft: multirotors and helicopters | **Claimed against multirotors, and bounded; against helicopters the published comparison is mixed and no advantage is claimed.** Cruise lift is carried on a surface rather than on rotors, which no sizing contract changes. The *size* of the resulting advantage is a calculation, not a consequence of that fact (Section 6). |
| Operation without a runway | Fixed-wing aircraft | **Claimed as sized, not demonstrated** (Sections 5, 14). |
| The mechanism required to change regime | Tilting architectures | **Claimed.** This is the paper's contribution — a count of mechanism classes (Section 7), not a claim of mechanical simplicity or reliability. |
| Cruise efficiency and range | Other hybrids — lift-plus-cruise, tilt | **Not claimed, in either direction.** |

**The fourth row is the important one**, and the reason it is a refusal rather than a result is the paper's own finding in Section 13. Against lift-plus-cruise the ordering depends on the sizing contract: across the three contracts it moves substantially, and under one of them its sign changes inside the envelope and turns on quantities of the competitor that are assumed rather than measured. A paper that quoted one of those orderings as a result would be reporting its own choice of contract. Against the tilting family the competitor can be modelled here only as a bound that pays no cruise penalty, and an ordering against a bound is not a result. **No range claim is made against the tilting or lift-plus-cruise families in either direction**, and a reader who finds one implied anywhere in this paper should treat it as an error rather than as a claim.

### What each claim does not depend on

**Operation without a runway** does not depend on the drag bracket, the propeller efficiency or the transition aerodynamics — **but it does depend on the energy store**: the vertical phase is sized with one, and Section 14 examines whether it exists. **Cruise lift carried on a surface** does not depend on the sizing contract or the transition aerodynamics. The **size** of the cruise-efficiency margin depends on both the drag bracket and the blade family, and Section 6 reports it as a range rather than a number. **Elimination of the propulsor-reorientation mechanism class** does not depend on the drag bracket, the propeller efficiency, the sizing contract, the range result or the energy store — **nor on the transition aerodynamics**.

**The last of these carries a distinction that matters more than the others.** The mechanism claim is a statement about what hardware is present, and it is settled by the inventory of Sections 7 and 8. **The separate claim that this aircraft can actually perform the regime change is not settled** (Section 7).

### One cost of the contribution that is named and not priced

The mechanism claim has a price this work does not compute. **This configuration declines the reaction-torque channel that comparable aircraft use for roll (Section 8). What that refusal costs — in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia — is not computed anywhere in this paper.** The claim is that the mechanism class is eliminated. **Whether eliminating it is favourable on balance is a question this work does not settle**, and quantifying it would require a control-allocation study rather than a single torque figure.

### Eight things this paper does not claim

**1. It does not claim range against fixed-wing aircraft.**

**2. It does not claim vertical capability against rotorcraft.** That comparison runs the other way.

**3. It does not claim that the aircraft has no moving parts.** What is eliminated is a *class of mechanism* — the one that reorients a propulsor. The aircraft has a moving aerodynamic surface, it is named where the elimination is claimed rather than later, and it also pitches the nose down when deployed.

**4. It does not claim mechanical simplicity.** Part count, assembly mass, failure modes and maintenance burden were not measured, and nothing here supports a statement about reliability. The count of mechanism classes in Section 7 is not a reliability argument~~, and readers who convert one into the other are not quoting this paper~~ **[D2]**.

**5. It does not claim that the escape condition is fully instantiated.** The condition is met in the propulsor that carries the aircraft and is not met in the attitude system, which is carried through cruise producing moments rather than cruise thrust. Section 3 names that case as partial instantiation, and the charge it re-opens is reported rather than absorbed.

**6. It does not claim that satisfying the condition makes an aircraft better.** The condition concerns three specific charges. A configuration may avoid all three and still be unbuildable, uncontrollable, or unsuited to its mission, and the accounting says nothing against that possibility.

**7. It does not claim that the trades inside the escape are favourable.** Moving the hover peak onto a store converts a power-system charge into a cost in kilograms; serving two regimes with one set of fixed-geometry propellers costs efficiency in at least one of them. Both are computed, neither is asserted to be worth paying, and the ledger reports them whichever way they fall.

**8. It does not claim that the aircraft flies.** The design *sizes* vertical operation and the transition; it does not demonstrate either. No aircraft has been built, no wind tunnel has been run on this geometry, and the transition analysis is a calculation whose assumptions are stated where it appears. **"By construction" throughout this paper means "by the sizing", never "by demonstration."**

### What the claims that remain amount to

Removing those eight leaves something narrower than a first reading of the abstract might suggest, and the narrower statement is the one the paper defends: **a configuration sized to combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism that reorients a propulsor, and an account of what the combination costs.**

Each half of that has a named opponent and neither half is a record. **Nor is the configuration claimed to be without precedent**: Section 1 sets out what is already established, including uncrewed tail-sitters, tail-sitters without control surfaces, coaxial contra-rotating tail-sitter propulsion, and blended-wing-body tail-sitters. **The contribution is the architecture, and the paper presents it as the combination, the consequences of the choices inside it, and the accounting** — which is what Sections 7 and 8 describe and what Section 11 prices.

### One consequence for how the numbers that follow should be read

Because the comparative result depends on the sizing contract, **no comparison in this paper should be quoted without the contract it was computed under.** ~~That is not a caveat attached for safety; it is the paper's own finding applied to the paper's own numbers, and Section 13 states what it demands of anyone who uses the framework afterwards.~~ **[N4]** 