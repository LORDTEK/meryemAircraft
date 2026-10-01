# Round 204 — The journal supplement, first three sections (S2, S3, S4), with two source defects found; four splits

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text.

---

## A. Closed in Round 203 (all four, and me)

- **A11:** *"the preceding margin"*. Applied.
- **A12:** *"is named later in this section"*. Applied. Grok withdrew *"after Table 4"*.
- **D50:** no commas: *"The architecture claim that the configuration … is a count"*. Applied. DeepSeek, Grok and Qwen changed their votes.
- **The supplement method:** compose only what the 34 pointers promise, from the latest snapshot, brought up to the current body, with provenance and a receipt table, and keep the archive as it is. All five.
- **No pointer is removed.** All five.

---

## B. Four splits: please answer each other

| Item | Positions | My view |
|---|---|---|
| **D33** *"…at the semi-span, 1.726 m: 2.43 times the pitch arm, a consequence of the layout…"* | ChatGPT, DeepSeek, Qwen: colon. **Grok:** withdraws the parentheses but rejects the colon (*"1.726 m:"* reads as a ratio). Proposes *"1.726 m, 2.43 times the pitch arm, a consequence of the layout rather than a design choice"* | Colon still preferred, but Grok's comma form keeps every attachment and avoids the ratio misreading. **ChatGPT, DeepSeek, Qwen: is Grok's comma form acceptable to you?** If yes, I take it. |
| **D55** *"…and the accounting: what Sections 5.1 and 5.2 describe and what Section 6.2 prices."* | ChatGPT, DeepSeek, Qwen: yes. **Grok: no.** A colon after *"the accounting"* restates that noun, not the three items. Proposes *"and the accounting, all of which Sections 5.1 and 5.2 describe and Section 6.2 prices."* | **I move to Grok's form.** *"All of which"* states the scope over all three explicitly; a colon leaves it to the reader. **ChatGPT, DeepSeek, Qwen: yes or no?** |
| **Renumbering** S2–S14 → S1–S11 in the submission | Grok, DeepSeek, Qwen, Claude: yes. **ChatGPT: no.** The labels are the archive's identities and part of the provenance chain | **Yes.** Provenance does not depend on the label: every passage of the new supplement names the archive section and lines it came from (see §C), and the repository keeps the map. A referee sees only the submission. **ChatGPT, does that meet your objection?** |
| **ChatGPT's rule:** *"A supplement passage may clarify or expose working already underlying the body pointer, but may not introduce a new substantive claim that the body itself does not make or promise."* | ChatGPT proposed it; the other three did not vote on it | **Yes.** It is the supplement's counterpart of *"the draft adds no predicate"*. **Grok, DeepSeek, Qwen?** |

---

## C. The journal supplement: S2, S3 and S4, in full

The source is `paper/submission/supplement-src.md`.
- Each passage carries its provenance: the archive section and line range it came from, and what was changed.
- Pointers stay in the assembled numbering (*"Section 2.1"*); the submission generator converts them as in the body.
- British spellings stay in the source; the generator converts them, as in the body.
- `v8_stale.py`, run on this text: **no retired phrase**.

**What you are asked to check:**
- Grade each pointer's receipt (R1 faithful; R2 carried but qualified differently; R3 resolves, no content; R4 the body says more than the supplement establishes).
- Check that **no passage adds a claim the body does not make or promise** (ChatGPT's rule, if adopted).
- The flagged changes:
  - **S2, two additions:**
    - *"and deducted from the battery mass"*, a source fact (the thesis's eq. 81), added under the Round 94 rule;
    - one connector sentence, *"The two clarifications of Section 2.1 apply to it as follows."*
  - **S3, brought up to the current body:** three places where the snapshot is superseded.
    - *"priced where the transition is analysed"* became *"analyses the transition without pricing it"*. That is the Round 191 repair.
    - *"Attitude devices produce thrust in cruise"* became *"produce no cruise thrust in that sense"*. The tip pairs free-wheel at zero shaft torque in cruise.
    - *"Section 11"* became *"Section 6.2"*.
  - **S4, two source defects** (below), and **one word change in a protected sentence**, which goes to the author.

**Two source defects found while composing S4.** I opened the NASA weight table (Johnson and Silva, p. 71) to check the archive's numbers.
- **S-64:** the archive wrote *"battery returns a further 10 lb"*. **The sign is wrong.** The source gives battery 254 lb for lift-plus-cruise against 244 lb for the tilt-wing, so battery *adds* 10 lb in the lift-plus-cruise entry's disfavour.
  - Structure 2,670 − 1,954 = 716 lb; propulsion 1,772 − 1,918 = −146 lb; battery +10 lb.
  - That gives 716 − 146 + 10 = **580**, and the empty-weight difference is 5,809 − 5,130 = 679 lb.
  - **The body's 580 was right; the archive's working sentence was not.** With the sign as written, the total would have been 560.
- **S-65:** *"a factor of 1.74"*. 8.5 / 4.9 = 1.735, which rounds to **1.73**. The ratio is not in the body.

**The draft:**

### S2. The charges: working for Section 2.1

#### The power ratio

> *Provenance and changes:* for P01: "The ratio between the two demands follows from the governing equations rather than from any design choice (Supplement S2)". src: paper/v8/supplement.md, "Section 2 as it stood before recomposition into result sentences", Bill 3 (L756-L771). Verbatim except the Section number.

Taking hover power from momentum theory and cruise power from the drag polar,

    P_hover / W  = √(DL / 2ρ) / η_h                 (DL = W/A, disc loading)
    P_cruise / W = V / ((L/D) η_p)

so that

    P_hover / P_cruise = √(DL / 2ρ) · (L/D) / V · (η_p / η_h)

A vehicle with a disc loading of 100 N m⁻², a cruise lift-to-drag ratio of 15 and a cruise speed of 30 m s⁻¹ needs between three and four times as much power to hover as to cruise: the geometric terms alone give 3.2, and the efficiency ratio η_p/η_h carries it to about four when the cruise propeller is roughly a quarter more efficient than the hover rotor.

#### The transfer with direct experimental support

> *Provenance and changes:* for P02: "One of these transfers has direct experimental support (Supplement S2)". src: same snapshot, "The charges are coupled" (L805-L812). Change: dash pair -> parentheses (E33, protected S2 row, format only). ADDED (source fact, for reader vote): "and deducted from the battery mass" -- Bacchini thesis eq. (81), paper/bacchini-reading-record.md 5.2.

In the doctoral study whose wind-tunnel campaign Section 2.1 quotes [14], and in that document rather than in the journal article by the same author, which reports a different comparison, a retraction system removed thirty percent of the airframe's drag; the same work then costed it. Applied to a passenger eVTOL, with the mechanism assessed at five percent of vehicle mass and deducted from the battery mass, maximum range rose from 119 km to 121 km: a two-kilometre gain for a five-percent mass penalty. The same work finds the retraction's advantage elsewhere (the speed that maximises range rose by 5 m/s), which is a performance this accounting does not price. Bill 2 was converted almost exactly into Bill 1, and the transfer is the point rather than the small residue.

#### The tilting row

> *Provenance and changes:* for P03: "The tilting row, which needs both clarifications, is worked through in Supplement S2". src: same snapshot, "One row pays part of its cost…" (L795-L801), "Two clarifications…" (L822-L832), "The tilting row needs both clarifications" (L834-L839). Protected S2 rows (E16) carried, format only (E33). ADDED connector sentence (for reader vote): "The two clarifications of Section 2.1 apply to it as follows."

What a tilting architecture buys its unified propulsion group with is a mechanism: a pivot, an actuator, the gyroscopic coupling of a reorienting mass, and a control problem through the turn. The pivot and the actuator are paid in kilograms, although they are not lift-subsystem mass; the coupling and the control problem are paid in none of the three.

The two clarifications of Section 2.1 apply to it as follows. "No worse" is judged against the architecture the move modifies. A charge that architecture already paid, left no larger, is no worse. A charge it did not pay, imposed by the move, is worse; so is one it paid, enlarged by it. A remedy whose cost falls outside the three charges does not refute the accounting, but it is not thereby exempt from being counted. A framework that could absorb any cost by declaring it out-of-scope would be unfalsifiable, so the costs outside the three are listed, not waved away.

The tilting row needs both clarifications. If the architecture it modifies supplies its hover peak from a store, tilting without one imposes Bill 3 and the row is a transfer between charges. If that architecture already sizes its continuous plant by the hover peak, tilting leaves Bill 3 no worse; then, where the mechanism's kilograms are fewer than those of the lift group it removes, what keeps the row from refuting the accounting is the part of its cost that falls outside the three, which is why that part is listed.

### S3. The condition: working for Section 2.2

#### What each departure costs

> *Provenance and changes:* for P04: "What each departure costs is in Supplement S3". src: paper/v8/supplement.md S3 working part, the departures table (L921-L926); the note from "Section 3 as it stood before recomposition…" (L1096-L1100). Change: one dash -> comma (row 4).

| Departure | What it costs |
|---|---|
| Different hardware | Bills 1 and 2. The unused set is carried for the whole flight and, if exposed, drags. |
| Same hardware, but it serves only one duty | Bills 1 and 2 again. A propulsor that lifts and is then carried is a dedicated lift group under another name, whatever it shares with the cruise system. |
| Same hardware, both duties, different orientation | The tilting family. Bill 3 is incurred unless a store supplies the hover peak, and the mechanism that changes the orientation adds mass and introduces a control problem through the turn. |
| Same hardware, both duties, one orientation, different sizing point | Bill 3, unless the hover peak is supplied from somewhere other than the continuously installed power. |

The second departure is stated separately because it does real work later: a propulsor that produces a little thrust in cruise is not thereby serving both duties, and the distinction decides which parts of a configuration meet the condition and which do not.

#### The six permitted costs

> *Provenance and changes:* for P05: "Six costs are permitted, named here before any candidate is examined (the working is in Supplement S3)". src: "Section 3 as it stood before recomposition into result sentences", the six bullets (L1131-L1180) and the failure-mode note (L1199-L1201). BROUGHT UP TO THE CURRENT BODY (superseded wording not carried): (3) snapshot "it is priced where the transition is analysed" -> current body "Section 6.1 analyses the transition without pricing it" (Round 191, row 0); (5) snapshot "Attitude devices produce thrust in cruise" -> current body "produce no cruise thrust in that sense" (the tip pairs free-wheel at zero shaft torque in cruise, Round 130-131); (6) "Section 11" -> "Section 6.2". Protected S3 row (E17) carried. Dashes -> parentheses or colons.

1) **A store.** It has the same duty-cycle character as Bill 1. The fourth part moves the hover peak off the continuous power plant and onto a store; that store delivers its peak for two percent of the flight and is carried for the rest. It is not Bill 1 as Section 2.1 defines it (it is not lift-subsystem mass), but it is mass carried for a duty that is briefly needed, which is the same complaint Bill 1 makes. The condition converts a power-system charge into a cost in kilograms and claims only that the three charges as named are not incurred. It does not claim the trade is favourable. Whether the store is lighter than the continuous power it displaces is a sizing result and is computed, not asserted.

2) **The electrical path.** The fourth part frees the continuous power plant from the hover peak. Everything between the store and the rotors (machines, power electronics, wiring) still passes the full hover power and is still sized by it. That is Bill 3 on the electrical path, and the condition does not remove it; it is carried in the ledger rather than in this definition.

3) **Rotating the airframe.** The condition refuses architectures that reorient a propulsor, and sets that refusal against the mechanism a tilt requires. An architecture that instead rotates its whole body faces the same physical problem: a ninety-degree change of the thrust axis relative to the flight path, with the moments, the authority and the control through the turn that implies. It is not one of the three charges and the condition does not eliminate it; Section 6.1 analyses the transition without pricing it. Saying otherwise would let a candidate win that line by wording.

4) **Hardware installed for the vertical phase that serves both duties.** The second departure is what carries the weight of this permission.

5) **Hardware used in both regimes for something other than propulsive thrust.** Cruise thrust in this paper means the thrust that balances cruise drag. Attitude devices produce no cruise thrust in that sense; they are used throughout the flight, so their duty cycle matches their presence and they fall outside Bill 1. They remain in the airstream, so the second charge reaches them. Attitude hardware does not stop the propulsor that carries the aircraft from meeting the condition, but it is carried through cruise without producing cruise thrust, which is the first failure mode of Section 2.2, and the charges are about everything the aircraft carries, so Bill 2 reaches it. An architecture in that position is a partial instantiation, the fourth failure mode: it meets the condition where it carries the aircraft and still pays one of the three elsewhere. The fourth failure mode is not a technicality. An architecture may meet the condition where it carries the aircraft and fail it elsewhere, and a paper that reported only the first half would be reporting the condition rather than the aircraft.

6) **The price of serving two regimes with one set of hardware.** Hardware that is not duplicated cannot be optimised twice: a propeller sized for hover thrust at zero forward speed is not the propeller a cruise design would choose, and if its geometry is fixed the compromise is paid in efficiency. The condition permits that cost and does not measure it. Section 6.2 does.

### S4. The independent check: working for Section 2.3

#### The published designs used

> *Provenance and changes:* for P06: "The working is in Supplement S4". src: paper/v8/supplement.md S4 working part, table (L1275-L1279); figures checked against the source in this round: Johnson & Silva [16], weight table p. 71 (references/1521_Johnson & Silva_122721.pdf): L/De 4.9 / 8.5 / 8.6; DGW 3,678 / 7,271 / 6,584 lb.

| Configuration (NASA sizing set [16]) | Effective L/D | Design gross weight | Dedicated lift group |
|---|---:|---:|---|
| Turboshaft quadrotor | 4.9 | 3 678 lb | none; the rotors serve both regimes |
| Turbo-electric lift-plus-cruise | 8.5 | 7 271 lb | yes: eight lift motors and a cruise motor |
| Turbo-electric tilt-wing | 8.6 | 6 584 lb | none: eight proprotors, reoriented |

#### Why the second half of the prediction is not derived

> *Provenance and changes:* src: "Section 4's paragraphs as they stood before the Round 184 shortening" (L1514) and "…before the Round 167 recomposition" (L1466). Protected S4 rows (E20) carried: the counter-set and "None is known to the authors." Change: "the mission used below" -> "the mission of Section 2.3"; dash -> colon.

Section 2.1 predicts the charge and the amplification; it does not prove that the credit must lose. A dedicated lift system raises the empty-mass fraction and may lower the energy fraction at the same time, and which wins is a closure result rather than a consequence of the accounting. If some data set showed the credit covering the charge, Bill 1 would not be refuted: the mass would still have been paid. What would be refuted is the expectation that the amplified charge outweighs the linear credit. A long enough mission is where the credit is most likely to cover the charge, and the mission of Section 2.3 is short. The counter-set is therefore a common-mission sizing study at longer range in which a dedicated-lift configuration is both more efficient and no heavier than one without. None is known to the authors.

#### The weight breakdown

> *Provenance and changes:* for P07: "… the remaining 99 lb lies in categories it does not break out (Supplement S4)". src: S4 working part (L1281-L1287), CORRECTED against the source (S-64): the archive wrote "battery returns a further 10 lb"; the source gives battery 254 lb (lift-plus-cruise) against 244 lb (tilt-wing), so it ADDS 10 lb in the lift-plus-cruise entry's disfavour. Check: structure 2,670 − 1,954 = 716; propulsion 1,772 − 1,918 = −146; battery 254 − 244 = +10; 716 − 146 + 10 = 580; empty 5,809 − 5,130 = 679.

Of the empty-weight difference of 679 lb, structure accounts for 716 lb in the lift-plus-cruise entry's disfavour, propulsion returns 146 lb of it because the tilt-wing's mechanism is heavier, and battery adds a further 10 lb. Those three categories account for 580 lb of the 679; the remaining 99 lb lies in empty-weight categories the published table does not break out, and this work does not know how it is distributed. What the three reported categories do show is the transfer property of Section 2.1 (the mechanism giving part of the structural saving back), visible inside a weight breakdown this work did not produce.

#### The source's own statement

> *Provenance and changes:* src: "Section 4's paragraphs as they stood before the Round 184 shortening" (L1518). Protected S4 rows (E20) carried verbatim. Quotation checked this round: references/1521_Johnson & Silva_122721.pdf, text lines 495-496 ("… but not enough to counter the increase in structure and propulsion weight").

And the source states the second half of the prediction in its own words, on a comparison the check does not use as its test. Discussing why the all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery weight compared with a quadrotor, *"but not enough to counter the increase in structure and propulsion weight."*

#### The quadrotor contrast

> *Provenance and changes:* src: S4 working part (L1289-L1300). Protected S4 row (E13) carried. Dashes -> colon and parentheses. Check: 8.5 / 4.9 = 1.735 -> 1.73 (the archive wrote 1.74: S-65); 7,271 / 3,678 = 1.977 -> 1.98. PROTECTED WORD CHANGE (author's decision): "the isolation test above" -> "the isolation test of Section 2.3" (the supplement has no test above).

The quadrotor is reported for scale, and the isolation test of Section 2.3 is what carries the prediction. Against it the lift-plus-cruise configuration is about three-quarters better in cruise efficiency (a factor of 1.73) and nearly twice as heavy, a factor of 1.98. The efficiency credit is exactly what the accounting says a dedicated lift system buys, and the weight charge is exactly what it says the buyer pays: the charge survives the credit. But that contrast changes three things at once (dedicated lift group, powertrain, and whether a cruise wing exists at all), so it supports a weaker proposition than the prediction as stated: that adding a wing and a lift group together still costs mass.


---

## D. Your own proposals

Open, as always.

---

## E. Errors (one list)

- **Claude:** S-64 and S-65 were in the archive's S4 working from Round 172, which I composed. They were found only now, by opening the source table. The body's figure is correct; how the two came apart is not recorded.
- **Readers:** none found in Round 203.

---

## F. What goes to the author

**One decision: a word change in a protected sentence moved to the supplement (E13).**
- *"The quadrotor is reported for scale, and the isolation test **above** is what carries the prediction"* becomes *"… the isolation test **of Section 2.3** …"*.
- The reason: in the supplement there is no test above it.
