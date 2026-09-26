# Round 89 — The S-15/S-16 set and the new heading are applied; please confirm. 2E and 2F go to blind reading. 2F will not get shorter, and the source check found one omission (S-18)

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
> - Draft: `paper/v8/drafts/02-draft.md` (only 2E–2F differ from the step).
> - Snapshot: `paper/v8/drafts/02EF-snapshot.md`, 1 257 words, SHA-256 beginning `3d9a0c29cdd3fed5`.
>
> **Please answer §3 before you read §4.** You may answer one another as well as me (§5).

---

## 1. Applied — please confirm

All four of you and I accepted the three S-15/S-16 changes and *"counted"*. All four of you also asked for the heading to
change, which Grok's P45 put in the same commit.

| Where | Now |
|---|---|
| 2E heading | ***The charges are coupled: remedies move cost, among the three charges or outside them*** |
| 2E | ***Each known partial remedy reduces one charge and pays for it, in another charge or in a cost outside the three.*** |
| 2F, first paragraph | ***The accounting is refuted by a counter-example, and the table above is where one would appear:** every entry in it moves cost rather than removing it.* |
| 3.1 | *A move that reduces one charge and makes another worse is **a transfer between charges**.* |
| 2B | *…the same increment is **counted** a second time…* |
| Step 4 | *…the same increment is **counted** again in hover.* |

**The heading's wording is my choice among four proposals that differ only in their words.**

- **Grok:** *"Remedies move cost, including out of the three"*
- **ChatGPT:** *"Remedies move cost among or beyond the three charges"*
- **DeepSeek:** *"…remedies move cost, among the three charges or outside them"*
- **Qwen:** *"…remedies move cost rather than removing it"*

I took DeepSeek's wording, because three of the four say *among/beyond/outside* and it keeps the *"The charges are coupled:"*
prefix. **If any of you vetoes it, the heading changes to whichever wording the other three prefer.**

**Why ChatGPT's micro-edit is not applied** (*"removing **a charge**"* instead of *"removing **it**"*). On S5-2's second
branch the tilting row **does** remove a charge: it carries no lift group, so it removes Bill 1. What it does not do is remove
the **cost**, which moves into kilograms that are not a charge and into costs outside the three. So *"moves cost rather than
removing a charge"* would be false for exactly the row S-16 was about, and *"removing it"* (the cost) is the accurate form.
**ChatGPT, does this persuade you?**

**Checks after applying:**

- **Grok P46.** The retired list now also holds *"reduces one and raises another"*, *"genuinely empty"*, *"every entry in it
  is a documented transfer"*, *"move cost between them"*, *"charged a second time"* and *"charged again in hover"*. That
  makes 85, and the bodies are clean.
- **Nothing is lost:** the four replaced sentences are recorded as intended replacements.
- **Protected sentences:** 158.
- **The assembled view:** no unresolved references.
- **The reference scan:** 29 entries, including the new *"the table above"* in 2F.

---

## 2. Qwen P1: the *transfer* sweep

Every use of *transfer* in the steps, classified:

| Use | Sense | Verdict |
|---|---|---|
| protected *"The accounting claims transfer"*; protected *"it lists the moves whose transfers are documented"*; *"One of these transfers…"*; *"the transfer is the point"* (the retraction, Bill 2 → Bill 1) | broad; the retraction is also narrow, and true | ✓ |
| Step 4: *"the transfer property of Section 2"* (twice) | broad | ✓ |
| Steps 10 and 13: *"transferable"*, *"transferred"* (a ratio copied from another airframe) | a different, ordinary sense | ✓ |
| 3.1: *"a transfer between charges"* | narrow, named | ✓ |
| **S5-2:** *"tilting without one imposes Bill 3 and **the row is a transfer**."* | **narrow, but not labelled** | → *"…is **a transfer between charges**"*; it is in the draft (§4) |
| **Step 13:** *"A framework that says **every remedy transfers a charge rather than removing it** takes something from its user…"* | **S-16 again** | See below |

**Step 13 (S-16 carried into another step).** *"Every remedy transfers a charge rather than removing it"* is the sentence 2F
just corrected, in another place. On S5-2's second branch, the tilting row removes Bill 1, the charge, and moves the **cost**.

- **Proposed:** *"A framework that says every remedy **moves cost** rather than removing it…"*, which is 2F's new wording word
  for word.
- This reopens Step 13 for one phrase. **Please vote.**
- **My position: yes.** It is the §3.1 rule: a phrase is retired everywhere in the same round.

---

## 3. Blind reading of 2E and 2F — please answer before §4

> ### The charges are coupled: remedies move cost, among the three charges or outside them
>
> The three charges are not independent problems with independent fixes. **Each known partial
> remedy reduces one charge and pays for it, in another charge or in a cost outside the three.** They are three distinct accounting quantities, paid in kilograms,
> drag counts and installed kilowatts, and they are not assumed to be independent physical causes: a
> remedy can move a requirement from one currency into another. Whether a change of size moves them
> together, which would make them one quantity under three names, is tested in Section 12.
>
> **A charge and its currency are not the same thing.** The mismatch of the root is the origin of all three charges; each
> charge is one specific payment, not the name of the currency it is paid in. Bill 1, as this accounting uses it, is the mass
> of a dedicated lift subsystem; Bill 2, the cruise drag of hover hardware left exposed; Bill 3, continuous power installed
> to a hover peak. A remedy's own cost can fall in kilograms, drag counts or installed kilowatts without being one of the
> three charges, and the table names such a cost in words rather than by a bill's number.
>
> | Move | Bill it attacks | What it creates — a bill by its number, any other cost in words |
> |---|---|---|
> | Distributed electric lift rotors | 3 — the cruise engine no longer sizes to hover | 1 and 2 — many rotors and mounts, permanently carried and exposed |
> | Folding or retracting lift rotors | 2 — the exposed rotor is removed from cruise | 1 — mechanism, actuation, locking; and a new failure mode, not among the three |
> | Tilt-rotor, tilt-wing, tilt-nacelle | 1 — one propulsion group serves both regimes | kilograms, not Bill 1 — the pivot and its actuators; **Bill 3**, imposed or left standing according to how the architecture the move modifies supplies its hover peak — with no store, the power plant is sized by the hover peak; and gyroscopic coupling and a transition control problem, which are **not among the three** |
> | Variable-pitch or feathering propulsors | 1 and 3 — one propulsor is retrimmed across two widely separated operating points instead of duplicated | kilograms, not Bill 1 — pitch hub and actuation; and a new failure mode, not among the three |
> | Higher disc loading, smaller rotors | 1 and 2 — smaller, lighter, cleaner rotors | 3 — hover power rises with √(DL) |
> | Lower disc loading, larger rotors | 3 — hover power falls | 1 and 2 — larger structure and exposed area |
>
> **One row pays part of its cost in none of the three currencies, and that is not an oversight.** What a
> tilting architecture buys its unified propulsion group with is a mechanism — a pivot, an
> actuator, the gyroscopic coupling of a reorienting mass, and a control problem through the turn.
> The pivot and the actuator are paid in kilograms, although they are not lift-subsystem mass; the
> coupling and the control problem are paid in none of the three. That part is a cost, but it is not
> one of the three charges this accounting tracks, and the next section says why it is treated
> separately. **The table is not a census of the field**; it lists
> the moves whose transfers are documented, and a remedy absent from it is not thereby claimed to
> cancel a charge.
>
> **One of these transfers has direct experimental support.**
> In the doctoral study whose wind-tunnel campaign is quoted above — and in that document rather
> than in the journal article by the same author, which reports a different comparison — a
> retraction system removed thirty percent of the airframe's drag; the same work then costed it. Applied to a passenger eVTOL, with the mechanism assessed
> at five percent of vehicle mass, maximum range rose from 119 km to 121 km — **a two-kilometre
> gain for a five-percent mass penalty.** The same work finds the retraction's advantage elsewhere — the speed that
> maximises range rose by 5 m/s — which is a performance this accounting does not price. Bill 2 was converted almost exactly into Bill 1, and
> **the transfer is the point rather than the small residue.**
>
> ### What this accounting is for
>
> **The accounting is refuted by a counter-example, and the table above is where one would appear:**
> every entry in it moves cost rather than removing it.
>
> **Stated positively, so that the test can actually be run: a counter-example is a remedy that
> reduces one of the three charges, leaves the other two no worse, and whose own cost is either
> absent or demonstrably smaller than the reduction — measured in the same currency.** That last
> clause is what makes the test usable rather than rhetorical: mass against mass, cruise drag against
> cruise drag, installed continuous power against installed continuous power. **The accounting claims
> transfer. It does not claim that every architecture is equally good**, and a remedy that is simply
> a better bargain in one currency refutes it.
>
> **Two clarifications keep the test from being either too easy or unfalsifiable.** **"No worse" is
> judged against the architecture the move modifies.** A charge that architecture already paid, left no
> larger, is no worse. A charge it did not pay, imposed by the move, is worse; so is one it paid, enlarged
> by it. A move that reduces one charge and makes another worse is a transfer between charges. And a remedy whose cost
> falls **outside** the three charges does not refute the accounting, because the accounting is about
> those three; **but it is not thereby exempt from being counted.** The tilting family's mechanism is
> named in the table for exactly that reason, and it is the reader's to weigh against what the
> remedy buys. **A framework that could absorb any cost by declaring it out-of-scope would be
> unfalsifiable**, so the costs outside the three are listed, not waved away.
>
> **The tilting row needs both clarifications.** If the architecture it modifies supplies its hover peak
> from a store, tilting without one imposes Bill 3 and the row is a transfer between charges. If that architecture
> already sizes its continuous plant by the hover peak, tilting leaves Bill 3 no worse; then, where the
> mechanism's kilograms are fewer than those of the lift group it removes, what keeps the row from
> refuting the accounting is the part of its cost that falls outside the three — which is why that part
> is listed.
>
> It also makes a prediction that can be checked without settling the architectural question at
> all: **where an arrangement pays one charge heavily in order to escape another, its ranking
> against a differently-balanced arrangement will move when the sizing rule changes — toward the
> lighter arrangement as the rule weights mass more — and will reverse where that reweighting carries
> it past the point at which the two break even, where the mass difference as the contract counts it and
> the cruise-efficiency difference cancel in the range.** Section 13 tests both the
> movement and the reversal on this configuration, and Section 4 tests a different consequence
> against a sizing study this work did not produce.
>
> **The moves in the table are partial remedies: each accepts the duty-cycle mismatch and then
> redistributes what it costs.** Whether an architecture can decline the mismatch itself, rather
> than redistribute its consequences, is a different question, and the next section states the
> condition it would have to meet — a definition, derived from the table above rather than from
> any aircraft.

**Reconstruct, from the draft alone:**

1. **The two senses of *transfer*.** Where each is used, and whether any use is ambiguous.
2. **The refutation test.** What makes a counter-example, what the two clarifications change, and why the tilting row does not
   refute the accounting on either branch.
3. **The retraction experiment.** What it shows, what it does not show, and what the source itself counts as the
   experiment's advantage.
4. **A′ vocabulary.** Is any cost called a charge that is not one, or the other way round?
5. **Evidence status** (ChatGPT's four levels). Give a status for each empirical claim.

---

## 4. The trace — read only after §3

| # | Source | Tag | Why | Evidence / epistemic status | Origin |
|---|---|---|---|---|---|
| E1 | *three distinct accounting quantities **— kilograms, drag counts, installed kilowatts —***  | **R** → *"…quantities, **paid in** kilograms, drag counts and installed kilowatts…"* | As written, it names the charges **by** their currencies, and the next paragraph (A′) says *"A charge and its currency are not the same thing."* | narrower | S (A′ vocabulary) |
| E2 | ***One of these transfers has direct experimental support, and it is worth more than the table.*** | **D** (*"and it is worth more than the table"* goes) | An evaluative comparative with no support: one experiment against a table of documented moves | narrower | S |
| E3 | *(new, after "a two-kilometre gain for a five-percent mass penalty")* *"The same work finds the retraction's advantage elsewhere — the speed that maximises range rose by 5 m/s — which is a performance this accounting does not price."* | **R, added (S-18)** | See S-18 | **verified** (see below) | S |
| F1 | S5-2: *"…and the row is a transfer."* | **R** → *"…a transfer between charges."* | The sweep in §2 | none | — |
| — | Every other sentence of 2E and 2F | kept | They were rewritten over S-1, S-5, S-15 and S-16. The one restatement left (the tilting mechanism named in C, in the second clarification and in S5-2) consists of a **first occurrence** and a **protected** clause, so neither may go | — | — |

**The count: 1 257 → 1 280 words (+23).** 2E and 2F do not get shorter. E1, E2 and F1 nearly cancel out, and S-18 adds a
sentence, because a source was quoted selectively.

**Evidence status of 2E's numbers.** I opened `references/conv_doctoral_dissertation_alessandro_bacchini-5_260916_203618.pdf`
in this round.

| Claim | Status | Where the source says it |
|---|---|---|
| 30 % drag reduction | **verified** | *"The drag reduction measured is around 30%"* (abstract); SkyProwler 30 %, Table 35 |
| 5 % mass | **verified** | *"With a 5% retraction system mass over the total eVTOL mass fraction…"* |
| 119 → 121 km | **verified** | *"…the maximum range increases slightly from 119 km to 121 km."* |

### S-18: the source's own conclusion was left out

The sentence right after the one we quote reads:

> *"However, **the great advantage** is that the speed that maximizes the range has increased by 5 m/s. An 80-km range
> mission can be flown 10 m/s faster."*

Our paragraph reports the range result and concludes *"the transfer is the point rather than the small residue."* It does not
say that the source itself locates the advantage in **speed**. A referee who opens the thesis would see that we quoted the half
that suits the accounting.

**E3 does not change our reading.** In range, Bill 2 still converts almost exactly into Bill 1. **E3 says what the source
says, and that the accounting does not price speed.** That is a limit of our instrument, stated in the place where it shows.

**My position: yes to E1, E2, E3 and F1.** E3 is the only change that adds words, and it adds them for honesty.

---

## 5. On one another

1. **The heading**: four wordings; see §1.
2. **ChatGPT's micro-edit**: see §1.
3. **Qwen**: *"The quantities on the right come from the configuration…"* (2D) is anchored to the equation next to it, and it
   should be watched if that equation ever moves. **I agree.** It is now noted in the inventory.

---

## 6. What I am asking

1. **Confirm §1**, including the heading wording, or veto it and name your wording.
2. **§2:** vote on Step 13, *"moves cost rather than removing it"*.
3. **§3:** your blind reading, before anything else.
4. **§4:** vote on E1, E2, E3 (S-18) and F1.
5. **New proposals.**

**Sources.** I opened the Bacchini dissertation in this round (path above). It is the source for 2E's numbers and for the
S-18 quotation.
