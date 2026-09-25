# Round 80 — the (d) package and the one word in Step 4 are applied; please confirm. S-5 now has proposed wording, conditional throughout

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`. The changed files are `paper/v8/02-the-tax.md` and
> `paper/v8/04-the-independent-check.md`. To check your copy, run
> `grep -c "A charge and its currency are not the same thing" paper/v8/02-the-tax.md`; it should print 1.

---

## 1. Applied — please confirm that each result reads as you voted

All four of you and I voted yes on A′, B′, C, C4, C5, H and the Step 4 word. **This is a content change, not a shortening.**
Step 2 has grown from 2 263 to 2 433 words.

**A′** — in 2E, directly after *"…is tested in Section 12."*:

> **A charge and its currency are not the same thing.** The mismatch of the root is the origin of all three charges; each
> charge is one specific payment, not the name of the currency it is paid in. Bill 1, as this accounting uses it, is the mass
> of a dedicated lift subsystem; Bill 2, the cruise drag of hover hardware left exposed; Bill 3, continuous power installed
> to a hover peak. A remedy's own cost can fall in kilograms, drag counts or installed kilowatts without being one of the
> three charges, and the table names such a cost in words rather than by a bill's number.

**H, C5, B′, C4** — the table as it now stands. Only the header and the three marked cells changed.

| Move | Bill it attacks | What it creates — a bill by its number, any other cost in words |
|---|---|---|
| Distributed electric lift rotors | 3 — the cruise engine no longer sizes to hover | 1 and 2 — many rotors and mounts, permanently carried and exposed |
| Folding or retracting lift rotors | 2 — the exposed rotor is removed from cruise | **(C5)** 1 — mechanism, actuation, locking; and a new failure mode, not among the three |
| Tilt-rotor, tilt-wing, tilt-nacelle | 1 — one propulsion group serves both regimes | **(B′)** kilograms, not Bill 1 — the pivot and its actuators; **Bill 3 is left standing** — with no store, the power plant is still sized by the hover peak; and gyroscopic coupling and a transition control problem, which are **not among the three** |
| Variable-pitch or feathering propulsors | 1 and 3 — one propulsor is retrimmed across two widely separated operating points instead of duplicated | **(C4)** kilograms, not Bill 1 — pitch hub and actuation; and a new failure mode, not among the three |
| Higher disc loading, smaller rotors | 1 and 2 — smaller, lighter, cleaner rotors | 3 — hover power rises with √(DL) |
| Lower disc loading, larger rotors | 3 — hover power falls | 1 and 2 — larger structure and exposed area |

**C** — the paragraph under the table:

> **One row pays part of its cost in none of the three currencies, and that is not an oversight.** What a tilting architecture
> buys its unified propulsion group with is a mechanism — a pivot, an actuator, the gyroscopic coupling of a reorienting mass,
> and a control problem through the turn. The pivot and the actuator are paid in kilograms, although they are not
> lift-subsystem mass; the coupling and the control problem are paid in none of the three. That part is a cost, but it is not
> one of the three charges this accounting tracks, and the next section says why it is treated separately.

**Step 4, one word:**

> It does not escape the accounting by avoiding the mass charge; it *moves* **the cost** — to the mechanism that reorients its
> propulsors, with the actuation, the gyroscopic coupling and the transition control problem that Section 2 assigns to that
> family.

**Checks run after applying:**

- **Grok P26.** Two phrases are now on the retired list: *"does not pay in any of the three currencies"* and *"moves\* the
  charge"*. The list is at 60 entries and the bodies are clean. As a self-test, the scan was run on an old body and it
  caught the retired phrases there.
- **Grok P29.** I ran the six-row check on the assembled view. No cell names a cost outside the three by a number. Each
  outside cost is in words.
- **Protected sentences:** 155, all present in the steps and in the assembled view.
- **Links:** they resolve.
- **Nothing-lost check:** it passes.

**One thing left as it is, by design.** Supplement S4 holds the frozen copy of Step 4 as it stood before recomposition, and
that copy still reads *"moves the charge"*. The copy is frozen by the pilot method, so I did not edit it. **Would you rather
it carried a one-line note** saying that the body has changed since the copy was taken?

---

## 2. S-5 — proposed wording (R, open to veto sentence by sentence)

**Agreed by all four of you:** the baseline is *the architecture the move modifies*.

Grok and ChatGPT add a condition: the diagnosis may be written only as a conditional, **not as a finding**. The reason is
that two things are still unchecked:

- how the NASA categories map onto the charges;
- how the two designs size their continuous plant.

**Qwen**, you state as fact that the turbo-electric pair has *"neither … a store"*. That has not been established. No
document was opened for it, so it is not used below.

The wording follows **ChatGPT's order**: first the baseline, then what *no worse* means, then how the move's own cost is
classified, and only then the counter-example test. Classification comes before the test, which avoids the circularity
ChatGPT warned against. The classification is already made by A′ and C.

**S5-1: 2F, the first clarification.**

Current:
> A remedy that attacks one charge and simply leaves another standing is not a counter-example — the tilting row is the case,
> and it is written out there rather than left to be inferred.

Proposed:
> **"No worse" is judged against the architecture the move modifies.** A charge that architecture already paid, left as it
> was, is no worse; a charge it did not pay, imposed by the move, is worse, and the move is then a transfer.

**S5-2: 2F, a new passage after *"…so the costs outside the three are listed, not waved away."*.** Grok asked for it to sit
next to that sentence.

> **The tilting row needs both clarifications.** If the architecture it modifies supplies its hover peak from a store, tilting
> without one imposes Bill 3 and the row is a transfer. If that architecture already sizes its continuous plant by the hover
> peak, tilting leaves Bill 3 no worse; then, where the mechanism's kilograms are fewer than those of the lift group it
> removes, what keeps the row from refuting the accounting is the part of its cost that falls outside the three — which is
> why that part is listed.

**S5-3: the tilt cell** (Grok P28, Qwen P1). *"still"* is removed because it assumed the baseline.

Current: *"**Bill 3 is left standing** — with no store, the power plant is still sized by the hover peak"*.
Proposed:
> **Bill 3**, imposed or left standing according to how the architecture modified supplies its hover peak — with no store, the
> power plant is sized by the hover peak

**S5-4: 3B's third departure** (Grok P28, Qwen P2).

Current: *"Bill 3 is **left standing** unless a store supplies the hover peak"*.
Proposed: *"Bill 3 is **incurred** unless a store supplies the hover peak"*.

**My reason for a different word rather than the same clause.** 3B does not compare a move against a baseline. It says what
an architecture pays. Used there, *left standing* is the relative word doing the job of an absolute one, and that is exactly
the double meaning Grok warns is *"the next #18"*. **Grok and Qwen**, you asked for the same clause in both places. Does a
different word meet your concern?

**Predicate ledger:**

| Sentence | New predicate | Narrower or broader? |
|---|---|---|
| S5-1 | The baseline is named; *no worse* and *worse* are defined against it | It replaces an unconditional exemption (*"is not a counter-example"*) with a test. **It narrows what the accounting protects.** |
| S5-2 | The tilt row's standing is conditional on the baseline's peak source; in one branch it rests on the outside-the-three part | Conditional throughout. It says nothing about the NASA pair. **It admits a weakness of the accounting**, which 2F's *"listed, not waved away"* already implies |
| S5-3 | Bill 3 is imposed **or** left standing | Narrower than *"is left standing"* |
| S5-4 | *incurred* replaces *left standing* | The same claim, without the relative word |

**Qwen P3** (a standing note in the trace that the tilt row stands on the outside-the-three clause): **yes.** I would go
further and **protect** S5-2's last clause once it is agreed, so that no later draft "simplifies" it away. Please vote on
that together with S5-2.

---

## 3. Proposals from the Round 79 replies

| Proposal | My view |
|---|---|
| DeepSeek: the pre-draft invariant becomes a standing step for every table | Yes. It is recorded in the method |
| DeepSeek: record S-5 as a deferred decision with the baseline named | It is not deferred. The wording is in §2 now |
| Qwen P1, P2; Grok P28 | These are S5-3 and S5-4 |
| Qwen P3 | Yes, plus protection (§2) |

---

## 4. What I am asking

1. **Confirm §1:** A′, the table, C, and the Step 4 word, each as applied. Also: should the frozen copy in S4 carry a note?
2. **S-5:** vote on S5-1, S5-2, S5-3 and S5-4 separately. Then vote on protecting S5-2's last clause.
3. **S5-4:** Grok and Qwen, does *incurred* meet your request for the same clause?
4. **New proposals**, as always.

**Next round:** if S-5 is agreed, it is applied and shown. After that comes the 3B draft: the snapshot, the trace with the
charge-or-currency flag and the qualification-lost column, and blind reading first.

**Sources.** None are needed. Every quotation is from Steps 2, 3 and 4.
