# Round 110 — Step 14 closed; J1 and D4 applied; the framework drafts: Steps 2 and 3 as result sentences; two defects found while drafting

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`4995059`**.
>
> The two drafts are in `paper/v8/drafts/02-recomposed.md` and `03-recomposed.md`, and in full in Appendices A and B below,
> for those of you who cannot open the files. Nothing in them has entered the step files yet. As always, answer one another as
> well as me.

---

## 1. Closed

- **Step 14 as applied, and S14's two new rows (S-39)**: confirmed by all four of you. Closed.
- **Three proposals adopted by all four of you and me:**
  - Grok P84: J3's two bands (kW per kilogram of buffer, at the bus, hover / take-off) are distinct objects from the 3.7–4.1×
    and 6.2–6.8× factors. Recorded in the coincidence register.
  - DeepSeek: the competitor's two assumed quantities (lift-group mass, propeller efficiency) are a pair in every trace.
    Recorded in the same register.
  - Qwen R108-P2: when Step 15 is drafted, every sentence is read against Step 14's sixteen unknowns. Recorded in the list of
    deferred items.
- **DeepSeek's proposal to protect Step 2's root sentence and Step 3's condition** is already met. Both are protected sentences
  (rows 182 and 180 of `paper/v8-caveats.md`).

---

## 2. J1 and D4 are applied — please confirm the result

All four of you voted yes. Step 14 now reads:

> **This section is where that question is answered, and for the first item the answer is no: the required store performance
> is not demonstrated by the sources consulted here.**

> **What has been measured is a fraction of that, and the store figures available are of four different kinds.**

Nothing else in the step changed. Step 14 is 1 165 words of prose.

---

## 3. What I checked in your Round 109 quotations

I searched every quotation in Step 2 and Step 3 as they stand now.

- **ChatGPT and DeepSeek:** every quotation is in the body, with one exception, below.
- **ChatGPT's Step 3 "core finding"** is set as a quotation but is not the source's words: *"an architecture avoids those three
  charges **only if** its propulsion arrangement uses the same propulsors across regimes without reorientation, and its
  continuously installed power is sized to cruise rather than hover"*.
  - The source states a sufficient condition: *"does not incur the three charges **if**"*.
  - P50 says the condition *"can be too narrow without being wrong"*. *"Only if"* makes it necessary, which is the reading P50
    exists to refuse.
  - The paraphrase also drops the store.
  - ChatGPT adds that *"the source's own wording for the condition is the authority here"*, and the draft keeps it.
- **Qwen** quoted three passages that are not in the body now:
  - the carbon-fibre tail-sitter, deleted in Round 88 because no source was found (S-14);
  - *"a counter-example would be a move whose right-hand column is genuinely empty"*, replaced in Round 89;
  - Step 3's opening with *"rather than by describing any aircraft"*, the pre-recomposition wording.

  All three survive only in the frozen snapshots of Supplements S2 and S3. Qwen's P2 still holds against the new sentence
  (*"the table above is where one would appear"*).
- **Grok** did not open the steps and said so. *"Calling them one would be loose"* is not in Step 3 now; it is in S3's frozen
  snapshot.
- **DeepSeek** proposes moving Step 3's *"detailed four departures table"*. Step 3 has no table: the departures are a paragraph,
  and Supplement S3 already carries them as a table.
- **DeepSeek on the Bacchini arithmetic** keeps it in the body in one list and moves it to S2 in the other. Which do you mean?

**One consequence for the supplement.** ChatGPT and Qwen both proposed moving the tail-sitter to S2. That means the frozen
snapshots are being read as if they were the journal supplement. When the supplement is split into the journal supplement and the
repository's audit archive, **the frozen snapshots go to the archive**, and no unsourced sentence goes to the journal. This is
recorded.

---

## 4. The framework drafts

### 4.1 Lengths, stated first

| | Source | Draft | Ratio | Plan |
|---|---:|---:|---:|---:|
| Step 2 | 2 189 | 1 842 | 84 % | 750 |
| Step 3 | 1 654 | 1 305 | 79 % | 650 |
| Together | 3 843 | 3 147 | 82 % | 1 400 |

ChatGPT and Qwen (P3) said this before I drafted it: the framework's definitions and its 24 protected sentences set a floor.
- In Step 2, the definitions, the table and the protected sentences are most of what is left.
- In Step 3, most of what is left is the six permitted costs, each with its protected clause and the reason for it.

Section 4.4 lists what else could move, with the words each would save.

### 4.2 How the drafts were made

- **The core comes first** (Grok P85).
  - Step 3 opens with its core: the definition, derived by inversion, stated before any configuration.
  - Step 2 opens with P1, Qwen's core (*"only meaningful if the cost is stated first…"*). The root follows as the first finding,
    in the second paragraph.
  - **Is that acceptable under P85?** Putting the root first would need a new transition sentence.
- **Deletion only**, checked by `v8_draft_check.py`:
  - no new predicate, no deleted negative, every protected sentence present;
  - two pointers added, in ⟦ ⟧: *"(Supplement S2)"*, and in Step 3 *"What each departure costs is in Supplement S3."*;
  - one word restored, *"Wind-tunnel"* (S-40, §5).
- **A fix to the checker, made while drafting.** It did not split sentences that end in a closing quotation mark. A sentence ending
  in a quotation therefore ran into the next one, and a correct sentence was flagged as new. It now splits there. I tested it by
  putting two errors back into the Step 2 draft (*"is a census"*, *"as its cube"*); both were caught.

### 4.3 What moves, and what stays against a proposal to move it

**Step 2 — moves to S2:**
- the example vehicle (all five of us);
- the two component equations (DeepSeek, Qwen);
- the twenty-six stationary propellers (Qwen);
- the quadplane's first finding;
- the tilt-prop incident behind the second NASA quotation;
- nine sentences and four clauses of explanation, restatement or transition, each listed in the draft's §3;
- one pointer clause that Section 3 does not honour (S-41, §5).

**Step 2 — stays against a proposal to move it:**
- **The ratio equation.** *"The quantities on the right come from the configuration…"* needs it (P71). ChatGPT keeps all the
  equations; DeepSeek and Qwen move them. I keep the ratio and move the two components.
- **The Bacchini arithmetic** (30 %, 5 %, 119 → 121 km). Grok and Qwen move it.
  - P50 is protected: *"The same work finds the retraction's advantage **elsewhere**…"*. *"Elsewhere"* is measured against the
    range result.
  - D51, *"Bill 2 was converted almost exactly into Bill 1"*, is a derived statement. Without the 30 % and the 5 % it would
    read as asserted, which is the protection criterion.
  - The pair is P71's. **Grok and Qwen: does this change your view?**
- **The wind-tunnel motors sentence, and the quadplane's simulation finding.** Section 13 (*"a different airframe's wind-tunnel
  campaign (Section 2)"*) and Section 11 (J18) point at them.

**Step 3 — moves to S3:**
- the four one-sentence departures (S3's table already carries them);
- the parenthesis on the second departure;
- eight sentences that restate a part of the condition or the fourth failure mode, or give a rationale or a transition that a
  kept sentence already carries; each is listed in the draft's §3.

**Step 3 — stays:**
- **"Two things in that sentence are choices"** (none of you named it). It says the store is the narrower reading, chosen
  because *"a narrower condition is easier to fail"*. It qualifies the definition.
- **The tip frames' *"landing gear because the aircraft stands on its tail"*.** It is why *"the exclusion does not reach them"*.
- **The two sentences before *"as written"*** (*"refused by a means other than the one the field has adopted"*). This is the
  first place the section sets the condition against the field's route, the tilting architecture. ChatGPT calls it movable setup.
  The author's rule is that the architecture is carried by placement, order and voice, so I keep it. Please say.

**Rule (iii):** there is no candidate in either step. No protected sentence moves.
- ChatGPT and DeepSeek called the example vehicle a rule-(iii) move. Qwen is right that it is not one: no protected sentence
  goes with it.

**Negative qualifications** that the drafts remove are listed one by one in each draft's §3, with where their point is still
carried. Every other *"not"* in the two sources is in the drafts.

### 4.4 Further moves, to vote

| # | What | Words | Proposed by | My view |
|---|---|---:|---|---|
| O1 | Step 2's structural-half paragraph (second NASA review) → S2 whole | ~65 | Qwen | **yes** — no later section uses it, and D10 keeps *"structural reinforcement"* in Bill 1's list |
| O2 | The Bacchini arithmetic → S2 | ~60 | Grok, Qwen | **no** — P50 and D51 (§4.3) |
| O3 | Step 2's NASA five-family paragraph → S2 | ~80 | Qwen; ChatGPT (conditional) | **not yet** — the same study is introduced in Sections 1, 2 and 4; choose its one home when Step 4 is recomposed |
| O4 | Step 3's *"Two things … are choices"* → S3 | ~95 | nobody | **no** (§4.3) |

---

## 5. Two defects found while drafting — both need your vote

**S-40 — a source's label dropped, and my own mislabelled sentence.**
- v7 read *"**Wind-tunnel** characterisation of a QuadPlane…"*. The reference list gives the source as Mathur and Atkins (2023),
  *Wind Tunnel Testing and Aerodynamic Characterization of a QuadPlane Uncrewed Aircraft System*. I have not opened the PDF; it is
  not in the repository. Step 2 lost the word; it reads *"Characterisation of a
  quadplane found…"*.
- **My error.** Section 11's source sentence read *"Section 2 quotes a wind-tunnel finding that…"*. In Round 105 I offered it as
  **J18**, *"Section 2's wind-tunnel source found that…"*.
  - That is not a deletion; the label J was wrong.
  - Since Step 2 names only one source as wind-tunnel work (Bacchini's), it ties the simulation finding to the wrong source.
- **Proposed repair:**
  - Step 2's R25 restores *"Wind-tunnel"*.
  - Section 11's J18 returns to its source sentence, word for word: *"Section 2 quotes a wind-tunnel finding that a simulation
    assuming negligible rotor–structure interaction "always predicts higher lift and lower drag than were experimentally
    observed"; this build-up is such a calculation, and the bracket's upper margin is the only provision made for it."* That is
    five words longer than J18.

**S-41 — a pointer that Section 3 does not honour.**
- Step 2 says of the tilting mechanism's cost outside the three charges: *"…and the next section says why it is treated
  separately."*
- Section 3 does not say why. It says the condition refuses reorientation, and that a tilting architecture buys its way out of
  the first departure with a mechanism.
- **Proposed repair:** delete the clause. The draft does.
- If you read Section 3 as saying why, please quote the sentence.

---

## 6. Proposals from Round 109, to vote

- **Grok P85** — each draft opens with its core. My view: yes; see §4.2 for how Step 2 meets it.
- **Grok P86** — Step 2's 3.2 and Step 11's 2.4–3.2 stay apart. My view: yes. The register keeps the row; the 3.2 now lives in
  S2 with its example.
- **Qwen P1 — a definition register.** The root sentence and the condition are protected already. The five sentences that carry
  the other definitions are not. **Proposal: protect these five, as the register:**
  1. *"A charge and its currency are not the same thing."*
  2. *"Bill 1, as this accounting uses it, is the mass of a dedicated lift subsystem; Bill 2, the cruise drag of hover hardware
     left exposed; Bill 3, continuous power installed to a hover peak."*
  3. *"Four parts: same hardware, both duties, one orientation, hover peak from a store."*
  4. *"…a counter-example is a remedy that reduces one of the three charges, leaves the other two no worse, and whose own cost is
     either absent or demonstrably smaller than the reduction — measured in the same currency."*
  5. *"\"No worse\" is judged against the architecture the move modifies."*

  My view: yes. `v8_caveats.py` then checks them every round.
- **Qwen P2** — T3 stays a table. My view: yes; the draft leaves it unchanged.
- **Qwen P3** — Step 3's protected density is the floor. My view: yes, as a statement for the author.
- **ChatGPT — a rule for the framework:** *"Compress Step 2 by moving working; compress Step 3 by removing explanatory repetition.
  Do not compress either by removing the boundary that tells the reader what the accounting or condition does not establish."*
  My view: yes, and for Step 4 as well.

---

## 7. Where you disagree — please answer one another

- **The Bacchini arithmetic.**
  - Grok and Qwen: move it.
  - DeepSeek: both, in two lists.
  - ChatGPT: silent.
  - Me: keep it (P50, D51).
- **Bill 3's equations.**
  - ChatGPT: keep them; *"I would not move the equations wholesale unless the shortened body still tells the reader why
    installed continuous power is sized by hover rather than cruise"*.
  - DeepSeek and Qwen: move them.
  - Me: keep the ratio only.
  - **ChatGPT, is the ratio enough for your condition? DeepSeek and Qwen, is the ratio acceptable to you?**
- **Rule (iii) and the example vehicle.**
  - ChatGPT and DeepSeek: a rule-(iii) move.
  - Qwen and me: no protected sentence goes with it, so the rule does not apply.
- **The tilting setup in Step 3** (§4.3). ChatGPT: movable. Me: it stays.

---

## 8. To vote

| # | Item | My vote |
|---|---|---|
| a | Confirm J1 and D4 as applied (§2) | confirm |
| b | Step 2 draft: veto any sentence by its number (Appendix A) | no veto |
| c | Step 3 draft: veto any sentence by its number (Appendix B) | no veto |
| d | O1–O4 (§4.4) | yes, no, not yet, no |
| e | S-40 repair (§5) | yes |
| f | S-41 repair (§5) | yes |
| g | §6 proposals | yes |
| h | §7: answer one another | — |

---

## 9. Your own proposals

As always: anything you see, with your reason. In particular, **what else in Steps 2 and 3 could move** without taking a
boundary with it.

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## Appendix A — Step 2, the draft (tags as in Steps 10–14; ⟦ ⟧ marks an added pointer or word)

## The tax

[P1] **A claim that one architecture escapes a cost shared by the others is only meaningful if the cost is stated first, in terms that do not presume the escape.** [D2] This section states it. [D3] It is not a claim about any particular aircraft, and nothing in it is new physics; what it provides is the accounting that the rest of the paper is checked against.

### The root: a duty cycle that does not match the hardware

[D4] For a mission of one hour, a take-off, a transition, a return transition and a landing occupy on the order of a minute — **roughly two percent of the flight.** [D5] **An architecture that provides the vertical phase with a dedicated lift subsystem therefore carries it for fifty times as long as it uses it.** [D6] This is not an implementation defect and it cannot be removed by making the subsystem better, because it is a statement about duty cycle rather than about quality. [P7] **The mismatch between how long a component is needed and how long it is present is the origin of all three charges below.**

[P8] The statement is deliberately confined to architectures with a dedicated lift subsystem, because that is the family the charges describe. [D9] Whether any architecture avoids the mismatch — and what it pays instead — is the subject of the next section, and it is not settled here.

### Bill 1 — mass

[D10] A lift-plus-cruise aircraft carries two propulsion groups: rotors, motors, mounts, wiring and structural reinforcement for the vertical phase, and a separate propulsor for cruise. [D11] The vertical group provides no required lift or thrust during cruise and is lifted anyway.

[D12] Its cost is not linear. [D13] Mass growth feeds itself — MTOW = m_payload / (1 − f_empty − f_energy) puts additional empty mass through a multiplier that grows as the denominator shrinks — and in the vertical phase the same increment is counted a second time, because at a fixed disc area hover power scales with W^1.5. [D14] *(The exponent is a property of the scaling rule chosen: holding disc loading constant instead makes hover power grow linearly with weight, and Section 12 uses that.)* [D15] A modest dead-mass fraction becomes a large payload penalty.

[D16] **This charge has been identified independently, and by a source with no interest in the present argument.** [D17] A NASA study sizing five VTOL architecture families against a common mission with common tools found the lift-plus-cruise concepts the heaviest of the vehicles examined, and named the cause: not the cruise power draw, since the lift-plus-cruise effective lift-to-drag ratio is the higher of the set, but *"the extra empty weight items on board in hover."* [D18] That is Bill 1 stated by an independent source in its own terms: not a failure of engineering, but the cost of an architecture.

[D19] A second NASA review gives the structural half as a general principle: to transmit power safely to the extremities of the planform, *"very strong (and fatigue-resistant) structures must be incorporated with an obvious weight penalty."* [D20] Distributing lift or thrust across the span therefore obliges the structure that reaches it to keep transmitting power there — charged to mass, whether or not the distributed propulsors are running.

### Bill 2 — drag

[D21] The second payment falls on architectures that leave hover hardware exposed in forward flight: rotors stopped in the airstream, the booms that carry them, and the interference between their wakes and the wing. [D22] Cruise drag has other sources on any aircraft; what is charged here is the part attributable to hardware retained for a phase that is over.

[D23] Wind-tunnel work on a hybrid airframe found that the difference between propellers parallel to the airflow and no propellers at all is modest, while *"the drag produced by the motors is significant."* [D24] The bill is charged mainly by the motors and the beams that carry them — hardware that cannot be feathered, folded or aligned away, **because its cost is its presence.** [R25] ⟦Wind-tunnel⟧ characterisation of a quadplane found drag in the hybrid regime exceeding either pure mode through adverse flow interaction, and that a simulation assuming negligible rotor–structure interaction *"always predicts higher lift and lower drag than were experimentally observed."*

[D26] **The important property of this charge is not its size but where it falls.** [D27] It is charged per unit time in cruise — so it grows with exactly the quantity the aircraft exists to maximise.

### Bill 3 — power system sizing

[D28] A VTOL aircraft must install enough power to hover, but it draws that power only during the two percent of the flight in which it hovers. [J29] The ratio between the two demands follows from the governing equations rather than from any design choice⟦ (Supplement S2)⟧:

    P_hover / P_cruise = √(DL / 2ρ) · (L/D) / V · (η_p / η_h)

[D30] **The quantities on the right come from the configuration and from the propulsion operating points, not from the duration of the hover phase.** [D31] η_h and η_p are not configuration constants, they depend on the propeller and on the condition it is run at, and Section 11 computes what happens when one fixed-pitch blade has to supply both. [D32] Raising the disc loading raises the ratio as its square root.

[D33] The power system is therefore sized by a condition that holds for a minute and is then carried, unused, for an hour. [D34] Sizing by hover means an oversized engine, or a battery that must deliver a peak it will rarely be asked for, or both — and whichever is chosen, the extra installed capacity is mass: a cost in kilograms, though not Bill 1.

### The charges are coupled: remedies move cost, among the three charges or outside them

[D35] The three charges are not independent problems with independent fixes. [D36] **Each known partial remedy reduces one charge and pays for it, in another charge or in a cost outside the three.** [P37] They are three distinct accounting quantities, paid in kilograms, drag counts and installed kilowatts, and they are not assumed to be independent physical causes: a remedy can move a requirement from one currency into another. [D38] Whether a change of size moves them together, which would make them one quantity under three names, is tested in Section 12.

[D39] **A charge and its currency are not the same thing.** [D40] The mismatch of the root is the origin of all three charges; each charge is one specific payment, not the name of the currency it is paid in. [D41] Bill 1, as this accounting uses it, is the mass of a dedicated lift subsystem; Bill 2, the cruise drag of hover hardware left exposed; Bill 3, continuous power installed to a hover peak. [D42] A remedy's own cost can fall in kilograms, drag counts or installed kilowatts without being one of the three charges, and the table names such a cost in words rather than by a bill's number.

| Move | Bill it attacks | What it creates — a bill by its number, any other cost in words |
|---|---|---|
| Distributed electric lift rotors | 3 — the cruise engine no longer sizes to hover | 1 and 2 — many rotors and mounts, permanently carried and exposed |
| Folding or retracting lift rotors | 2 — the exposed rotor is removed from cruise | 1 — mechanism, actuation, locking; and a new failure mode, not among the three |
| Tilt-rotor, tilt-wing, tilt-nacelle | 1 — one propulsion group serves both regimes | kilograms, not Bill 1 — the pivot and its actuators; **Bill 3**, imposed or left standing according to how the architecture the move modifies supplies its hover peak — with no store, the power plant is sized by the hover peak; and gyroscopic coupling and a transition control problem, which are **not among the three** |
| Variable-pitch or feathering propulsors | 1 and 3 — one propulsor is retrimmed across two widely separated operating points instead of duplicated | kilograms, not Bill 1 — pitch hub and actuation; and a new failure mode, not among the three |
| Higher disc loading, smaller rotors | 1 and 2 — smaller, lighter, cleaner rotors | 3 — hover power rises with √(DL) |
| Lower disc loading, larger rotors | 3 — hover power falls | 1 and 2 — larger structure and exposed area |

[D43] **One row pays part of its cost in none of the three currencies, and that is not an oversight.** [D44] What a tilting architecture buys its unified propulsion group with is a mechanism — a pivot, an actuator, the gyroscopic coupling of a reorienting mass, and a control problem through the turn. [D45] The pivot and the actuator are paid in kilograms, although they are not lift-subsystem mass; the coupling and the control problem are paid in none of the three. [D46] That part is a cost, but it is not one of the three charges this accounting tracks. [P47] **The table is not a census of the field**; it lists the moves whose transfers are documented, and a remedy absent from it is not thereby claimed to cancel a charge.

[D48] **One of these transfers has direct experimental support.** [J49] In the doctoral study whose wind-tunnel campaign is quoted above — and in that document rather than in the journal article by the same author, which reports a different comparison — a retraction system removed thirty percent of the airframe's drag; applied to a passenger eVTOL, with the mechanism assessed at five percent of vehicle mass, maximum range rose from 119 km to 121 km — **a two-kilometre gain for a five-percent mass penalty.** [P50] The same work finds the retraction's advantage elsewhere — the speed that maximises range rose by 5 m/s — which is a performance this accounting does not price. [D51] Bill 2 was converted almost exactly into Bill 1, and **the transfer is the point rather than the small residue.**

### What this accounting is for

[D52] **The accounting is refuted by a counter-example, and the table above is where one would appear:** every entry in it moves cost rather than removing it.

[D53] **Stated positively, so that the test can actually be run: a counter-example is a remedy that reduces one of the three charges, leaves the other two no worse, and whose own cost is either absent or demonstrably smaller than the reduction — measured in the same currency.** [P54] **The accounting claims transfer. It does not claim that every architecture is equally good**, and a remedy that is simply a better bargain in one currency refutes it.

[D55] **Two clarifications keep the test from being either too easy or unfalsifiable.** [D56] **"No worse" is judged against the architecture the move modifies.** [D57] A charge that architecture already paid, left no larger, is no worse. [D58] A charge it did not pay, imposed by the move, is worse; so is one it paid, enlarged by it. [D59] A move that reduces one charge and makes another worse is a transfer between charges. [P60] And a remedy whose cost falls **outside** the three charges does not refute the accounting, because the accounting is about those three; **but it is not thereby exempt from being counted.** [P61] **A framework that could absorb any cost by declaring it out-of-scope would be unfalsifiable**, so the costs outside the three are listed, not waved away.

[D62] **The tilting row needs both clarifications.** [D63] If the architecture it modifies supplies its hover peak from a store, tilting without one imposes Bill 3 and the row is a transfer between charges. [P64] If that architecture already sizes its continuous plant by the hover peak, tilting leaves Bill 3 no worse; then, where the mechanism's kilograms are fewer than those of the lift group it removes, what keeps the row from refuting the accounting is the part of its cost that falls outside the three — which is why that part is listed.

[D65] It also makes a prediction that can be checked without settling the architectural question at all: **where an arrangement pays one charge heavily in order to escape another, its ranking against a differently-balanced arrangement will move when the sizing rule changes — toward the lighter arrangement as the rule weights mass more — and will reverse where that reweighting carries it past the point at which the two break even, where the mass difference as the contract counts it and the cruise-efficiency difference cancel in the range.** [D66] Section 13 tests both the movement and the reversal on this configuration, and Section 4 tests a different consequence against a sizing study this work did not produce.

[D67] **The moves in the table are partial remedies: each accepts the duty-cycle mismatch and then redistributes what it costs.** [P68] Whether an architecture can decline the mismatch itself, rather than redistribute its consequences, is a different question, and the next section states the condition it would have to meet — a definition, derived from the table above rather than from any aircraft.

---

## Appendix B — Step 3, the draft

## The escape condition

[D1] This section asks what an architecture would have to do in order not to incur the three charges at all. [P2] The answer is a **definition**, derived by inverting the table, and it is stated here before any configuration is offered so that the standard is not taken from the thing it will be used to measure.

### Inverting the table

[D3] **A charge appears wherever the two regimes are served by hardware that departs from one of four things: the same hardware, serving both duties, held in one orientation, with the hover peak supplied other than by its continuously installed power.**⟦ What each departure costs is in Supplement S3.⟧ [P4] Read one at a time, these are ways to pay. Read as a conjunction, they are a condition.

### The condition

[P5]
> **An architecture does not incur the three charges if the propulsors that carry the weight,
> held in one orientation relative to the airframe, produce both the hover thrust and the cruise
> thrust, and if the difference between the hover peak and the cruise demand is supplied from
> a store rather than from permanently installed continuous power.**

[D6] Four parts: **same hardware, both duties, one orientation, hover peak from a store.** [D7] The first three come from the first three departures; the fourth comes from the fourth.

[D8] Two things in that sentence are choices rather than derivations. [D9] The inversion requires only *one orientation relative to the airframe*; **how** an architecture keeps that while changing flight regime — by rotating the whole body, or otherwise — is not in the inversion, and is treated as exposition rather than as part of the definition. [D10] And the fourth departure's exception lets the peak come from **any** source other than the continuously installed power; a store is the narrower reading used here, because it is what the configuration examined later uses and because a narrower condition is easier to fail.

### What the condition does not say, and this matters more than what it says

[P11] **It means zero of the three charges as Section 2 defines them.** **It does not mean an architecture that costs nothing, and it does not mean an architecture that carries nothing for the vertical phase.** [D12] A definition that placed every conceivable cost inside the thing to be escaped would be unfalsifiable, and an architecture built to satisfy it would win by construction rather than by performance.

[D13] The costs the condition permits are named here, before any candidate is examined. Six of them:

- [P14] **A store is permitted, and it has the same duty-cycle character as Bill 1.** [D15] It is not Bill 1 as Section 2 defines it — it is not lift-subsystem mass — **but it is mass carried for a duty that is briefly needed, which is the same complaint Bill 1 makes.** [D16] The condition converts a power-system charge into a cost in kilograms and claims only that the three charges as named are not incurred. [P17] **It does not claim the trade is favourable.** [D18] Whether the store is lighter than the continuous power it displaces is a sizing result and is computed, not asserted.
- [P19] **Releasing the engine is not releasing the electrical path.** [D20] Everything between the store and the rotors — machines, power electronics, wiring — still passes the full hover power and is still sized by it. [D21] **That is Bill 3 on the electrical path, and the condition does not remove it**; it is carried in the ledger rather than in this definition.
- [P22] **Rotating the airframe is permitted and is not priced here.** [D23] **An architecture that rotates its whole body faces the same physical problem** — a ninety-degree change of the thrust axis relative to the flight path, with the moments, the authority and the control through the turn that implies. [D24] It is not one of the three charges and the condition does not eliminate it; it is priced where the transition is analysed.
- [D25] **Hardware installed for the vertical phase is permitted if it serves both duties**, and the second departure is what carries the weight.
- [D26] **Hardware used in both regimes for something other than propulsive thrust is permitted, and its cruise drag is not eliminated.** [D27] *Cruise thrust in this paper means the thrust that balances cruise drag.* [D28] Attitude devices produce thrust in cruise, but they produce no cruise thrust in that sense; they are used throughout the flight, so their duty cycle matches their presence and they fall outside Bill 1. [D29] **They remain in the airstream, so the second charge reaches them.** [D30] **Attitude hardware does not stop the propulsor that carries the aircraft from meeting the condition, but it is carried through cruise without producing cruise thrust, which is the first failure mode below — and the charges are about everything the aircraft carries, so Bill 2 reaches it.** [D31] The condition permits such hardware outside the first charge and does not make it free.
- [P32] **Serving two regimes with one set of hardware has a price of its own.** [D33] Hardware that is not duplicated cannot be optimised twice: a propeller sized for hover thrust at zero forward speed is not the propeller a cruise design would choose, and if its geometry is fixed the compromise is paid in efficiency. [P34] **The condition permits that cost and does not measure it.** [D35] Section 11 does.

[D36] **One exclusion, stated narrowly.** [D37] Structure, surfaces and actuation present for reasons other than the vertical phase are not charged **as duty-cycle mismatch under this accounting**. [D38] That is a statement about which ledger they belong in, not a claim that they are free, and it does not apply to a part that would not exist but for the vertical phase. [D39] The tip frames are the case that tests it: they are landing gear because the aircraft stands on its tail. [D40] **Their mass is charged in the build-up and their drag in the ledger; the exclusion does not reach them.**

### The condition can fail, and how

[D41] An architecture fails the condition if **any** of the following holds:

1. It carries a propulsor through cruise that produces no cruise thrust.
2. It changes the orientation of a propulsor relative to the airframe in order to change regime.
3. Its continuously installed power is sized by the hover requirement rather than by cruise.
4. It satisfies the first three only in part — for instance in its primary propulsor while a secondary set fails them — in which case the instantiation is **partial**, and the part that fails re-opens the charge it fails.

[D42] The fourth is not a technicality, and it is the reason this list exists. [P43] **An architecture may meet the condition where it carries the aircraft and fail it elsewhere**, and a paper that reported only the first half would be reporting the condition rather than the aircraft.

### What follows from the condition, and what does not

[D44] The condition is a statement about what an architecture would have to be. [P45] **It is not a claim that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim that satisfying it is desirable.** [D46] Three questions follow from it, and they are answered separately: whether the accounting behind the condition survives contact with an independent sizing study is tested in the next section, against data this work did not produce; whether any configuration satisfies the condition is the subject of Sections 5 to 7; and what such a configuration pays instead is the subject of Section 11, the answer most likely to be wrong.

[D47] The third departure is refused by a means other than the one the field has adopted. [D48] A tilting architecture accepts that departure and buys its way out of the first departure with a mechanism. [P49] **An architecture that reorients a propulsor does not satisfy the condition as written**, because the condition requires one orientation relative to the airframe. [P50] **Whether such an architecture might avoid the three charges by some other route is a separate question this paper does not settle** — the condition is a definition, not a law, and it can be too narrow without being wrong.
