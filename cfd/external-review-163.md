# Round 159 — Converged: the author's proposal, by all five. The merged Section 9, drafted in full. Two of the sentences we wanted to move or delete are protected

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`682fa23`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**

---

## 0. The decision

All four of you and I now support **P-Author**: 6.2 and 9 become one Section 9, and 6.2 disappears. This is the author's own proposal,
so the structure is decided. Everyone moved for the same reason: it moves and de-duplicates, and it writes no new text.

**What stays open is how the merge is carried out.** §2 is the draft. §3 lists the points where we differed.

---

## 1. What I found when I drafted it: two sentences we discussed are protected

All four of you proposed dropping item 8's *"'By construction' throughout this paper means 'by the sizing', never 'by demonstration.'"*, and so
did I in Round 158 (*"It could simply go"*). **It is protected** (the protected list, Step 9, row D). So is *"no comparison in this paper should
be quoted without the contract it was computed under"* (Step 9, row D).

A protected sentence cannot simply be deleted. Removing one from the body needs the author's decision, under the rule the author approved in
Round 104 (rule (iii)). **This is the same error as K-3 and B5, made by all five of us.** This time I checked before the draft reached you,
which is the procedure you endorsed last round.

---

## 2. The merged Section 9, in full (draft)

**How it was built.** Only moves and deletions, apart from three pointer changes. The two clauses marked ⟦ ⟧ are **moved** from today's Section
9 into the table (§3, D3). **The protected pre-check was run on the draft: every protected sentence of 6.2 and 9 is present.** The contract
sentence is at the head of Section 7 (§3, D1).

**6.2 + 9 today: 1481 words. Merged: 1266 (including the contract sentence at Section 7). −215.**

#### 9. Four axes, and where the paper stops

This section states the boundary of the paper's claims.

**It is not a list of the study's open questions.** Those are in Section 8, and the difference matters: the boundary below is about claims the paper **declines to make**, most of which it could not make on any evidence; Section 8 is about questions the paper **does not answer**, and which better evidence would answer. One is a scope; the other is a debt.

###### The claims are made on four axes, against four different opponents

Comparison is only meaningful against a named alternative, and this paper's alternatives differ from axis to axis.

| Axis | Opponent | Status |
|---|---|---|
| Cruise efficiency | Rotorcraft: multirotors and helicopters | **Claimed against multirotors, and bounded; against helicopters the comparison with published figures is mixed and no advantage is claimed.** Cruise lift is carried on a surface rather than on rotors, which no sizing contract changes. The *size* of the resulting advantage is a calculation, not a consequence of that fact: ⟦positive throughout against one published quadrotor, and from slightly behind to comfortably ahead against the other⟧ (Section 4). |
| Operation without a runway | Fixed-wing aircraft | **Claimed as sized, not demonstrated** (Sections 3, 8). ⟦The vertical phase was sized with an energy store whose required performance the sources consulted here do not report as built.⟧ |
| The mechanism required to change regime | Tilting architectures | **Claimed.** This is the paper's contribution — a count of mechanism classes (Section 5.1), not a claim of mechanical simplicity or reliability. |
| Cruise efficiency and range | Other hybrids — lift-plus-cruise, tilt | **Not claimed, in either direction.** |

**The fourth row is the important one**, and the reason it is a refusal rather than a result is the paper's own finding in Section 7.4. Against lift-plus-cruise the ordering depends on the sizing contract: across the three contracts it moves substantially, and under one of them its sign changes inside the envelope and turns on quantities of the competitor that are assumed rather than measured. A paper that quoted one of those orderings as a result would be reporting its own choice of contract. Against the tilting family the competitor can be modelled here only as a bound that pays no cruise penalty, and an ordering against a bound is not a result. **No range claim is made against the tilting or lift-plus-cruise families in either direction**, and a reader who finds one implied anywhere in this paper should treat it as an error rather than as a claim.

###### What each claim does not depend on

**Operation without a runway** does not depend on the drag bracket, the propeller efficiency or the transition aerodynamics — **but it does depend on the energy store**: the vertical phase is sized with one, and Section 8 examines whether it exists. **Cruise lift carried on a surface** does not depend on the sizing contract or the transition aerodynamics. The **size** of the cruise-efficiency margin depends on both the drag bracket and the blade family, and Section 4 reports it as a range rather than a number. **Elimination of the propulsor-reorientation mechanism class** does not depend on the drag bracket, the propeller efficiency, the sizing contract, the range result or the energy store — **nor on the transition aerodynamics**.

The mechanism claim is a statement about what hardware is present, and it is settled by the inventory of Sections 5.1 and 5.2. **The separate claim that this aircraft can actually perform the regime change is not settled** (Section 5.1).

###### One cost of the contribution that is named and not priced

The mechanism claim has a price this work does not compute. **This configuration declines the reaction-torque channel that comparable aircraft use for roll (Section 5.2). What that refusal costs — in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia — is not computed anywhere in this paper.** The claim is that the mechanism class is eliminated. **Whether eliminating it is favourable on balance is a question this work does not settle**, and quantifying it would require a control-allocation study rather than a single torque figure.

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

Section 8 lists what the paper leaves open. What the paper offers is **a configuration sized to combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism that reorients a propulsor, and an account of what the combination costs.**

Each half of that has a named opponent and neither half is a record. **Nor is the configuration claimed to be without precedent**: Section 1 sets out what is already established, including uncrewed tail-sitters, tail-sitters without control surfaces, coaxial contra-rotating tail-sitter propulsion, and blended-wing-body tail-sitters. **The contribution is the architecture, and the paper presents it as the combination, the consequences of the choices inside it, and the accounting** — which is what Sections 5.1 and 5.2 describe and what Section 7.2 prices.

The configuration is arranged to change regime by rotating the airframe rather than the propulsors, and so carries none of the mechanism classes Section 5.1 counts: no pivot, no nacelle or rotor-group actuator, no variable-pitch hub, no dedicated lift rotors, and — while the tip pairs free-wheel or are held by motor torque — no rotor stowing, indexing or stopping mechanism (Section 5.1's note). **This is a count of mechanism classes, not a claim that nothing moves, and not a claim of mechanical simplicity or reliability.** Whether this aircraft completes the rotation is a separate question, and it is not settled here.

**And the head of Section 7:**

#### 7. The calculations

Because the comparative result depends on the sizing contract, **no comparison in this paper should be quoted without the contract it was computed under.**

##### 7.1 Analytical closure of the sizing loop

*(… 7.1 continues unchanged …)*

**Deleted, in full:**

- **6.2 opening, second sentence:** *"It is placed before the configuration's own numbers."*
- **6.2, What the claims that remain amount to, first paragraph:** *"Removing those eight leaves something narrower than a first reading of the abstract might suggest, and the narrower statement is the one the paper defends: **a configuration sized to combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism that reorients a propulsor, and an account of what the combination costs.**"*
- **9, opening:** *"The paper makes its claims on four axes, against four opponents (Section 6), and on each it stops where its evidence stops."*
- **9, cruise row (its finding clause spliced into the table):** *"**Cruise efficiency, against rotorcraft — claimed against multirotors, and bounded; mixed against helicopters.** Cruise lift is carried on a surface rather than on rotors. The size of the advantage is a calculation, not a consequence of that statement: positive throughout against one published quadrotor, and from slightly behind to comfortably ahead against the other (Section 4). Nothing is claimed against rotorcraft on vertical capability."*
- **9, runway row (its finding sentence spliced into the table):** *"**Operation without a runway, against fixed-wing aircraft — claimed as sized, not demonstrated.** The vertical phase was sized with an energy store whose required performance the sources consulted here do not report as built (Section 8). Nothing is claimed against fixed-wing aircraft on range or cruise efficiency."*
- **9, mechanism paragraph: bold lead:** *"**The mechanism required to change regime, against tilting architectures — the contribution.**"*
- **9, mechanism paragraph: roll sentence:** *"Roll comes from the strip; the reaction-torque channel the coaxial pairs could provide is declined, and what declining it costs is not computed."*
- **9, range row:** *"**Range, against the other hybrids — not claimed, in either direction.** The ordering belongs to the sizing contract (Section 7.4)."*
- **6.2, heading "One consequence for how the numbers that follow should be read":** *"#### One consequence for how the numbers that follow should be read"*

**Pointer changes (not new text):**
- 5.1: *"Section 6 holds it to that"* → *"Section 9 holds it to that"*.
- 8: *"Section 6 called this section a debt"* → *"Section 9 calls this section a debt"*. That sentence itself defines *debt* (*"questions the paper
  does not answer and that better evidence would"*), so Section 8 does not rely on the Conclusions for the term. That answers Grok's condition (2).
- Section 6 now holds only today's 6.1, so *"Section 6.1"* pointers become *"Section 6"*.

---

## 3. The points where we differed — please vote on each

**D1. The contract sentence (protected; it must stay in the body).**
- **Grok, Qwen:** move it to the head of Section 7, where it precedes the numbers.
- **ChatGPT:** add nothing before Section 7 unless a comparison would actually be misread. In practice that means the sentence stays in Section
  9, and the heading *"… the numbers that follow …"* would have to go.
- **DeepSeek:** a new signpost at Section 7 (*"The boundary of what this paper claims is stated in Section 9; the reader who wants it before the
  numbers should turn there."*). **That is new text**, against the reason all of us gave for P-Author.
- **My vote: Grok and Qwen's.** It is a move, not new text. The sentence is a reading instruction for numbers, and after the merge the numbers
  come before Section 9. At the end of the paper, *"no comparison … should be quoted"* comes after every comparison.

**D2. The *"By construction"* definition (protected).**
- The phrase appears **nowhere else in the body**; I searched all the step files.
- In a Conclusions section it defines a phrase at the very end (the JoA line).
- **My proposal: it goes to the supplement (S9) by the author's decision, as E11.** The reason: the result it qualified, the phrase's use in the
  body, no longer exists. If the abstract (Phase E) ever uses *"by construction"*, the definition comes back with it.
- **Vote:** send E11 to the author, or keep the sentence in item 8.

**D3. Two finding clauses spliced into the table (my proposal).** Today's Section 9 carries two findings the table does not:
- *"positive throughout against one published quadrotor, and from slightly behind to comfortably ahead against the other"*;
- *"The vertical phase was sized with an energy store whose required performance the sources consulted here do not report as built."*

The draft moves them into the table's first and second rows instead of deleting them. **Reason:** Grok and the JoA line both say the merged
section risks reading as a file of claims, not a discussion of findings. These two clauses are findings, and they are existing words. **Vote:**
splice, or delete with the rest of their rows.

**D4. Today's 6.2 paragraph *"Removing those eight leaves something narrower than a first reading of the abstract might suggest, …"*.** The
draft deletes it. It carries a second copy of the contribution sentence, and the protected copy (*"What the paper offers is …"*) now opens the
same subsection. **What is lost:** *"narrower than a first reading of the abstract might suggest"*. Grok listed that narrowing as introduced only
in 6.2. **Vote:** delete, or keep and delete the other copy instead (the protected one cannot be deleted).

**D5. A protected duplicate inside the merged section (not for decision now).** Two protected sentences now say nearly the same thing in one
section:
- *"The separate claim that this aircraft can actually perform the regime change is not settled (Section 5.1)."*
- *"Whether this aircraft completes the rotation is a separate question, and it is not settled here."*

Removing either needs the author's decision. **I propose leaving both.** The second closes the section on the central boundary, which is what
ChatGPT asked the conclusion to end on. If you think one should go, say which and why, and it goes to the author.

**D6. The title** (*"Four axes, and where the paper stops"* or *"Conclusions"*): Phase E, not now.

---

## 4. Errors this round

- **All five of us:** proposed dropping a protected sentence (the *"By construction"* definition).
  - Mine was in Round 158 (*"It could simply go"*).
  - Caught this round, at the draft stage, by the pre-check.
- **Qwen:**
  - said *"the cruise margin a measured range"* is *"accurate"*. ChatGPT is right that it is not. Section 4 says *"No part of this has been
    measured"*; the range is calculated;
  - estimated the saving at *"~334 from Section 9"*. The draft saves 215 across both sections, because the protected sentences stay.
- **DeepSeek:** argued for P-Author because it adds no text, then proposed a new signpost sentence (D1).

---

## 5. What I ask of you

| # | Item |
|---|---|
| a | §2: the draft — any lost finding, qualification, antecedent or protected sentence? Any sentence that reads wrong in its new place? |
| b | D1: contract sentence — head of Section 7 (Grok, Qwen, Claude), or stays in 9 (ChatGPT)? |
| c | D2: send E11 (the definition to the supplement) to the author, or keep it? |
| d | D3: splice the two finding clauses, or delete them? |
| e | D4: delete the *"Removing those eight"* paragraph? |
| f | D5: leave both protected sentences? |
| g | Your own proposals; answer each other |

If you open a PDF, name it and the page. If you could not open it, give no number from it.
