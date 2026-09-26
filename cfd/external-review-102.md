# Round 98 — The rotorcraft axis is carried through Steps 6, 9, 10 and 15. The series-hybrid sentence is repaired and 7G is applied. Step 8 inventory, the last block, finds that the count of Section 7 may not hold in one of the tip pairs' two cruise states

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> New in the repository: `paper/v8/drafts/08-inventory.md`. Everything you are asked to vote on is quoted below.
>
> **The author asks, again, that you answer one another as well as me.** Where one of you objects, the others are invited
> to say whether the objection holds. §4 names each divided point with each reader's reason.

---

## 1. Confirmed and closed

- **Round 97's applied text** (R-5, R-6, S-28, the 1B heading, 7A, the table-completeness rule) is confirmed by all four
  of you.
- **S-27, "mixed", is confirmed** by all four of you (protected, 166). Grok proposes a refinement; see §4.3.
- **7L stays.** Grok yielded and Qwen changed its vote, so all five of us agree. The trace marks it as the bridge from the
  combination to the ledger, not as a restatement.

**My error in last round's table.** I wrote that the configuration is "behind at 6.00" against the all-electric
single-main-rotor helicopter at 6.0. It is a tie (Grok). The S-27 sentence itself does not say this.

---

## 2. Applied — all four of you and I agreed. Please confirm the text

**The cruise axis carried through the paper (P-a to P-h).**

| # | Now reads |
|---|---|
| P-a (6A) | *"On this axis the alternative is the **rotorcraft, multirotor and helicopter alike**, …"*; *"…the one thing the **rotorcraft family** structurally lacks: a surface that carries the cruise lift."* |
| P-b (6B) | *"**A rotorcraft meets that requirement completely.**"* |
| P-c (6C) | *"**A rotorcraft's rotors must produce** the lift and the propulsive force together, throughout cruise."* |
| P-d (6E, protected) | *"The compared vehicles are **1 660** to 3 275 kg"* |
| P-e (Step 9 table) | *"Cruise efficiency \| **Rotorcraft: multirotors and helicopters** \| **Claimed against multirotors, and bounded; against helicopters the published comparison is mixed and no advantage is claimed.** …"* |
| P-f (Step 9, item 2) | *"**2. It does not claim vertical capability against rotorcraft.**"* |
| P-g (Step 10) | *"…the currency in which **the rotorcraft comparison** is made"*; *"**No multirotor or helicopter** is sized in this work, so no range comparison is made **against either**"* |
| P-h (Step 15) | *"**Cruise efficiency, against rotorcraft — claimed against multirotors, and bounded; mixed against helicopters.**"*; *"Nothing is claimed against **rotorcraft** on vertical capability."* |

Source quotations and specific references keep their names: 6B's Bacchini & Cestino quotation (*"multirotors are efficient
in hover"*), the two reference quadrotors, and the quadrotor tail-sitters of Step 1. I swept every step for "multirotor" and
"quadrotor". No other family-level use remains.

**1G (S-29):** *"…series-hybrid propulsion **has been flown in a crewed motor glider and designed for small uncrewed
aircraft**."*

**7G:** *"…because the nose pair is sized at thrust equal to weight and no more. **This dual role is a dependency, reported
as one where the sizing is audited, and it does not make the tip pairs a dedicated lift system.**"* The verbatim Step 5D
sentence is gone.

**Protected (167):** the R-6 clause as a whole, *"this aircraft's vertical phases occupy about a minute in all (Section 2),
and how long each draws the peak is not computed here"*.

**P56 variant check:** *"combination of thrust settings produces a moment"* may stand only in Steps 7 and 8, and *"by any
combination of thrust settings"* only in Step 1. The self-test plants both in another step and catches them.

**Records.**
- The nothing-lost check caught seven sentences I had changed without freezing them. They are now in Supplements S1, S6,
  S7, S9 and S10.
- Seven more retired phrases, 111 in all.
- All checks pass; 167 protected. The body is 25 850 words.

---

## 3. Step 8 inventory — the last block — please confirm or correct

Step 8, *What it is made of, and what still moves* (assembled Sections 5.2 and 6.1), is 2 174 words, with 6 protected
sentences. Under the source-opening rule I opened NACA TR-796 for the C_nβ criterion. It supports the text: the recommended
C_nβ is *"usually greater than 0.001 per degree"*, and tailless aircraft *"should be as great as required on conventional
airplanes"*. It adds that models flew with a third of that value, which makes the 39 mm fairing conservative.

| Block | Must say | Candidate |
|---|---|---|
| **8A** Airframe | The planform is the wing; the geometry; sweep and longitudinal stability are one variable | 6G states the tailless constraint first; 8A keeps it as the inventory's reason → keep |
| **8B** Propulsion | Ten rotors in five counter-rotating pairs; fixed geometry (no cyclic, no collective, no variable-pitch hub, no reorienting mechanism); one machine per rotor; net angular momentum nominally zero | **S-30**, **S-31** |
| **8C** Energy path | Series hybrid; the engine drives no rotor; sized by cruise; the buffer takes the hover difference; no wattage here | **S-32** |
| **8D** Moments | Pitch and yaw from tip-pair differential thrust (yaw arm 2.43 × pitch arm); the same system assigned to the rotation (not demonstrated); roll by the strip; the reaction-torque channel declined; P *"What declining it costs is not counted in this work."* | — (Step 7H points here) |
| **8E** Ground | Five points; the fairing is the only vertical surface (39 mm needed); the flight control system is part of the mechanism; the tip frames do four jobs | *"It stands on its tail in its own storage attitude, with no launch equipment present."* repeats Step 5C → **remove**. The *"four jobs"* paragraph repeats Step 5C's *"One structure serves four purposes"* and the stance/arm coupling, and ends on the cruise exposure charge for the fifth time (3E, 5F, 7C, 7L, here) → **remove** |
| **8F** What moves | Orientation and pitch never change; the strip, in two halves; the actuator inventory; P *"How many actuators that is, this study does not fix."* | — |
| **8G** Not settled | The hover residual (body-axis naming; speed trim not shown, or a fourth duty on the strip); two cruise states of the tip pairs; the tip pairs fail the condition; the stopped state is not determinate | **S-33** |

**Qwen P1, the five classes checked against this inventory:**
- Pivot, nacelle actuator and variable-pitch hub are absent (8B: *"no cyclic pitch, no collective, no variable-pitch hub and
  no mechanism that changes a rotor's orientation relative to the airframe"*).
- Dedicated lift rotors are absent (8G: the tip pairs *"were not sized for weight support"*).
- **Stowing, indexing or stopping mechanism: absent only if the tip pairs free-wheel.** See S-33.

**Four source findings (S), to vote. None has been applied.**

- **S-33 — the most important.** Step 7's table counts *"Rotor stowing, indexing or stopping mechanism"* as absent. Step 8
  says the stopped state *"requires the stop to be produced by something — motor holding torque, an electrical brake, a
  mechanical lock"*, and that *"neither the means nor the azimuth is fixed by this study."*
  - In the free-wheeling state the count holds.
  - In the stopped state it holds only if the stop is motor holding torque.
  - The table's class is defined for dedicated lift rotors, and the tip pairs are not dedicated lift rotors. But a reader
    who sees a lock on a rotor will not accept a definitional escape, and I would not either.
  - Proposal, one sentence in 8G: *"The free-wheeling state needs no stopping means; the stopped state does, and if it were
    a brake or a lock rather than motor holding torque, the count of Section 7 would gain a class."*
  - Is that honest enough? Or should Step 7's table carry a footnote at the stopping row as well?
- **S-30 (8B).** *"…the net angular momentum of the propulsion system is nominally zero: rotating the airframe through
  ninety degrees **precesses nothing**, and no gyroscopic moment appears for the control system to cancel."* 8G offers a
  speed trim of the pairs as one way to absorb the hover torque residual. Two counter-rotating rotors at different speeds
  do not cancel their angular momentum.
  - Proposal: *"…precesses **nominally** nothing, and no gyroscopic moment appears **unless the pairs are speed-trimmed
    (below)**."*
- **S-31 (8B).** *"…the splitting gearbox and the mechanical governors that synchronise it are not required — **the
  arrangement that repeatedly defeated the XB-35**."* There is no source in the body or the repository, and "repeatedly
  defeated" is strong.
  - Proposal: remove the clause unless one of you gives a downloadable source. The sentence stands without it.
- **S-32 (8C) — our own rule.** *"The figures published for this configuration were closed on a propeller efficiency this
  work has since replaced with a computed one, and the re-closed set belongs to Section 10 rather than to an inventory.
  Quoting the superseded numbers beside a propulsion section that no longer assumes them is precisely the inconsistency this
  paper is trying not to commit."* This is a previous-version narrative, which the project keeps out of the journal body.
  - Proposal: *"No wattage is quoted here; the closed powers are Section 10's."*

---

## 4. Divided — please answer one another

**4.1 P-i: should *"So the second claim is narrower…"* (6D) mention the helicopters?**

| | Vote | Reason |
|---|---|---|
| Grok | add one sentence | otherwise the "narrower" paragraph silently drops the new opponent |
| Qwen | add a clause after *"a measurable advantage, not a change of category"*: *"— against the helicopters, mixed rather than an advantage"* | the helicopter result becomes part of the narrowing |
| ChatGPT | no change | the paragraph is about the two quadrotor references; the helicopter paragraph sits directly above |
| DeepSeek | no change | same |

**My view: no change.** The S-27 paragraph is the sentence immediately before. Repeating "mixed" one paragraph later
restates it, and our restatement rule cuts the second statement unless a job keeps it.

Grok and Qwen: is there a job the second statement does that S-27 does not? ChatGPT and DeepSeek: does Grok's "silently
drops" point hold for a reader who skips to the summarising paragraph?

**4.2 The series-hybrid rationale sentence.** All four of you want one sentence saying the series choice is architectural,
not a claim about efficiency. The place and wording differ:

| | Where | Wording |
|---|---|---|
| ChatGPT | where the series architecture is first introduced | *"The series arrangement is used here for the electrical path it gives the buffered hover peak, not because this study assumes it is the more efficient hybrid architecture."* |
| DeepSeek | 1G or Step 7 | names the parallel preference of the cited literature, then gives the architectural reason |
| Grok | 7D or 8 | the fourth part of the condition, not efficiency |
| Qwen | Step 7 or 8 | same idea |

**My view:** use ChatGPT's wording. It makes no claim about the parallel literature that we would then have to source
precisely. Put it in **7D's series-hybrid bullet**: the combination is where the reason belongs, and Step 8 describes the path
rather than the choice. DeepSeek, would you accept a sentence that does not name the parallel preference?

**4.3 Grok's refinement of S-27.** Grok prefers *"the two middle entries **lie in the envelope, one of them on the 6.00
corner**"* to *"fall inside its envelope"*. The others accepted the current wording.

My view: the current wording is true (6.0 lies within 5.56–7.39). The refinement adds a precision that no later text uses.
Will the others accept it, and does Grok insist?

---

## 5. New proposals, to vote

| # | Proposal | Who | My vote |
|---|---|---|---|
| a | **Opponent-family vocabulary lock.** Each use of "multirotor" is one of three kinds: a family-level statement (→ *rotorcraft*), a specific reference (kept), or a source quotation (untouched). | ChatGPT; Grok P64 and DeepSeek asked for the sweep | yes — the sweep in §2 is its first use |
| b | Qwen P1: a helicopter row in the Step 6 trace (mixed, no advantage) | Qwen | yes — recorded |
| c | Protect the Step 9 axis row as now worded, so the helicopter limit cannot drop | me | yes — it is a limit later text (Step 15) depends on |

---

## 6. What I am asking

1. Confirm §2.
2. §3: confirm or correct the Step 8 inventory; vote on the two 8E removals and on S-30, S-31, S-32 and S-33. On S-33, say
   whether Step 7's table needs a footnote too.
3. §4: answer one another on 4.1, 4.2 and 4.3.
4. §5 (a) to (c).
5. Your own proposals.

With Step 8, every block has had its inventory. What remains is confirming the applied text and closing the divided points.
Then the author will look at the target again, as the author decided in Round 77.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
