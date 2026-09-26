# Step 2 as result sentences — first recomposed draft (Round 110, to vote)

**Nothing here has entered `02-the-tax.md`.** Source: the step's English body, 2 189 words of prose, 11 protected sentences.
Tags: **P** protected, word for word · **D** one source sentence, shortened by deletion or not at all · **J** source sentences
joined by deletion · **R** recomposed, vetoable by number. Pointers added are in ⟦ ⟧. The deletion check
(`v8_draft_check.py 2 --taslak paper/v8/drafts/02-draft2.md`) passes: no new predicate, no deleted negative, all 11 protected
sentences present. The removed and shortened sentences are listed in `02-draft2-removed.md`; if the draft is applied, the whole
current step is frozen in Supplement S2, as for Steps 10–14.

## 1. The lists (Round 109), in short

| Finding | Grok | ChatGPT | DeepSeek | Qwen | Claude | Draft |
|---|---|---|---|---|---|---|
| Opening: stated first, not about any aircraft, no new physics | — | body (P) | body (neg.) | body (core) | body | P1, D2, D3 |
| Root: two percent, fifty times, not a defect, root sentence (P), confined (P), not settled here | body | body | body | body | body | D4–D9 |
| Bill 1: two groups, lifted anyway; multiplier and W^1.5, with the exponent note | — | finding + mechanism body, algebra movable | body | body | body (Step 4's *"derived from Section 2"* needs it) | D10–D15 |
| Bill 1: NASA five-family study | — | movable if proposition kept | body | → S2, keep *"not a failure of engineering…"* | body for now (see §4, O3) | D16–D18 |
| Bill 1: the structural half (second NASA review) | — | movable | quote → S2, result body | → S2 | body, incident detail → S2 (see O1) | D19, D20 |
| Bill 2: definition and exclusion | body | body (neg.) | — | body | body | D21, D22 |
| Bill 2: wind-tunnel motors; quadplane; 26 propellers | — | movable | — | → S2 | motors and the simulation finding body (Sections 11 and 13 point here); 26 propellers → S2 | D23–R25 |
| Bill 2: *"not its size but where it falls"*; per unit time | — | — | — | body | body | D26, D27 |
| Bill 3: equations | — | keep | → S2 | → S2 | **keep the ratio only** — *"the quantities on the right"* needs it | J29 |
| Bill 3: *"not from the duration"*; η not constants | — | body (neg.) | body | body | body | D30, D31 |
| Bill 3: example vehicle (100 N m⁻², L/D 15, 30 m s⁻¹, 3.2, about four) | → S2 | → S2 | → S2 | → S2 | → S2 | out; D32 (square root) stays |
| Coupling; charge/currency; three bill definitions | body | body | body | body | body | D35–D42 |
| Table T3 | body | — | body | **stays a table** (P2) | body | unchanged |
| One row outside the three; not a census (P) | body | — | body | body | body | D43–P47 |
| Bacchini: 30 %, 5 %, 119 → 121 km; speed (P); *"the transfer is the point"* | arithmetic → S2 | — | body, and also → S2 (both) | arithmetic → S2 | **body** — P50 and D51 need it (§3) | D48–D51 |
| Refutation test, *"no worse"* baseline, outside-the-three pair (P), unfalsifiable (P), tilting row (P) | body | body | body | body | body | D52–P64 |
| Prediction; Sections 13 and 4 test it | — | — | — | — | body — Section 13 tests it | D65, D66 |
| Partial remedies; the bridge (P) | — | body | — | body | body | D67, P68 |

**Check on quotations (every quotation searched in the step as it is now).**
- **ChatGPT, DeepSeek:** every quotation from Step 2 is in the body. DeepSeek's *"The three are not assumed to be independent
  physical causes"* reads *"they are not assumed…"* in the body; the meaning is the same.
- **Qwen:** two items are not in the body.
  - *"Carbon-fibre tail-sitter ratio"* was removed from the body in Round 88: no source for it was found. It survives only in
    Supplement S2's frozen snapshot. ChatGPT also names it as a move candidate. **It must not reach the journal supplement**
    (see §5 of the round text).
  - Qwen's P2 quotes *"a counter-example would be a move whose right-hand column is genuinely empty"*. That sentence was replaced
    in Round 89. The body now reads *"The accounting is refuted by a counter-example, and the table above is where one would
    appear: every entry in it moves cost rather than removing it."* Qwen's point stands against the new sentence.
- **Grok** did not open the step and said so. *"Bill 1 / 2 / 3 is not the name of the currency"* paraphrases *"each charge is
  one specific payment, not the name of the currency it is paid in"*.

## 2. The draft

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

## 3. Trace, pairs and audits

| Source paragraph | Fate |
|---|---|
| Opening (3) | P1, D2, D3 |
| Root, duty cycle (3) | D4 (*"The vertical phase is short."* and *"Any hardware installed for that phase alone is carried through the remaining ninety-eight percent."* → S2) |
| Root, fifty times (3) | D5, D6 (*"a lighter or cleaner lift rotor is still carried for the whole flight"* → S2), P7 |
| Confined (2) | P8, D9 |
| Bill 1, two groups (3) | D10, D11 (*"The most direct payment is dead mass."* → S2) |
| Bill 1, not linear (4) | D12–D15 |
| NASA study (2) | D16, D17 |
| *"That finding separates…"* (3) | D18; the first two sentences → S2 (D17 already says the vehicle is aerodynamically better and heaviest) |
| Structural half (2) | D19 (*"drawn from a tilt-prop aircraft whose propeller separated in flight after a gearbox mounting fatigued"* → S2), D20 |
| Bill 2, definition (2) | D21, D22 |
| Wind-tunnel motors (2) | D23, D24 |
| Further measurements (3) | R25 (*"Two further measurements support the direction."*, *"the highest lift and least drag in fixed-wing mode at both cruise airspeeds"* and the twenty-six propellers → S2; **"Wind-tunnel" restored**, S-40) |
| Where it falls (2) | D26, D27 |
| Bill 3, equations (4 + equations) | D28 (*"The third payment is the least visible."* → S2), J29 (the two component equations and *"Taking hover power from momentum theory…"* → S2), D30, D31 (*"That distinction matters and the efficiencies are the reason for it"* → S2) |
| Example vehicle (2) | the example → S2; D32 stays |
| Propagation (2) | D33, D34 (*"And the consequence propagates"* → S2) |
| Coupling (4) | D35, D36, P37, D38 |
| Charge and currency (4) | D39–D42 |
| Table | unchanged |
| One row (5) | D43–D46 (*"and the next section says why it is treated separately"* → S2; S-41), P47 |
| Bacchini (5) | D48, J49 (*"the same work then costed it"* → S2), P50, D51 |
| Refuted (1) | D52 |
| Stated positively (4) | D53, P54 (*"That last clause is what makes the test usable…"* → S2) |
| Two clarifications (9) | D55–P61 (*"The tilting family's mechanism is named in the table for exactly that reason…"* → S2; P61 says the same: *"so the costs outside the three are listed"*) |
| Tilting row (3) | D62, D63, P64 |
| Prediction (2) | D65, D66 |
| Partial remedies (2) | D67, P68 |

**Words:** 1 842 of prose, **84 %** of the source (2 189). The plan gives 750. Section 4 of the round text says why, and
offers what else could move.

**P71 pairs checked:**
- P7 (root) needs D4–D5 (the duty cycle) and D41 (what the three charges are).
- **P50 (protected) needs J49**: *"elsewhere"* is measured against the 119 → 121 km result. D51 (*"converted almost exactly"*)
  needs J49's 30 % and 5 %. This is why I keep the Bacchini arithmetic in the body, against Grok's and Qwen's proposal.
- D30 (*"the quantities on the right"*) needs the ratio equation: J29 keeps it.
- D14 (the exponent note) needs D13's W^1.5.
- P47, P60, P61 need T3 and D43–D46.
- P64 needs D63 and T3's tilting row.
- D65 is what Section 13's J25 tests.

**Rule (iii):** no candidate. The example vehicle carries no protected sentence, so it moves without the rule (Qwen). No
protected sentence moves.

**Negative-qualification audit** — every *"not"* the draft removes:
- *"a lighter or cleaner lift rotor is still carried"* — no negative; it illustrates D6, whose negative stays.
- *"and the next section says why it is treated separately"* — a pointer that Section 3 does not honour (S-41).
- *"That last clause is what makes the test usable rather than rhetorical"* — explanation; D53's *"measured in the same
  currency"* stays.
- *"The tilting family's mechanism is named in the table for exactly that reason"* — P61 carries the same point.
- Every other *"not"* in the source is in the draft.

**Inbound pointers kept:**
- Section 14's *"about a minute in all (Section 2)"* → D4.
- Section 13's *"a different airframe's wind-tunnel campaign (Section 2)"* → D23.
- Section 11's J18 → R25, with S-40.
- Section 4's *"First half, derived from Section 2"* → D13.
- Section 12's constant-disc-loading rule → D14.
