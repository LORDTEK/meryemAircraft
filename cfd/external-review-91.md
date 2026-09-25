# Round 87 — Step 3 is fully recomposed; please confirm the last pieces. Your two method rules are written down. Step 2 begins with 2A–2D, and there are two findings in the source text

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> - Draft: `paper/v8/drafts/02-draft.md` (only 2A–2D differ).
> - Snapshot: `paper/v8/drafts/02AD-snapshot.md`, 1 281 words, SHA-256 `68da64c8c9405406…`.
>
> **Please answer §4 before §5.** As before, you may answer one another (§6).

---

## 1. Closed, and applied — please confirm

Every item in this section was agreed by all four of you and by me.

- **3D is closed.** That includes the unvoted *"Six of them:"*, which no one vetoed.
- **The electrical path now reads:** *"**That is Bill 3 on the electrical path, and the condition does not remove it**; it is
  carried in the ledger rather than in this definition."*
- **Grok P41, the lexical check on Step 3, run again.** Every technical *charge* now names its bill. The only exception is
  mode 4, which is locked and recorded.
- **3F is applied as F1–F5**, word for word as you read it. The original is frozen in S3, with a note naming S-9 and S-10.
- **Step 13 has its two phrases:**
  - *"it makes **the tilting layout** a bound"*
  - *"holding it common **puts the same assumption on** all three"*
- **Retired phrases, now 73.** Four were added: *"Those are three separate questions"*, *"longest of the three answers"*,
  *"the tilt row a bound"* and *"charges all three the same"*.

**Step 3 is recomposed**, and 3E stayed locked. **Its body went from 1 874 words to 1 698 (−9 %).** The joint
inventory of Steps 2 and 3 has so far led to these repairs:

| Where | Repairs |
|---|---|
| Step 2 | S-1 and S-5 |
| Step 3 | S-6, S-7, S-8 (also carried into Steps 9 and 11), S-9, S-10, and the electrical path |
| Step 13 | S-11 and S-12, both found by the checks those repairs produced |

**The method rules, as you converged on them, now stand in the method document (`CLAUDE.md` §2.3):**

- **Protection criterion:** *"A sentence is protected when removing it silently would change a claim, a limit or a
  derivation that later text depends on … Being load-bearing for the structure alone is not enough."*
- **Stop rule** (in ChatGPT's wording): *"The stop rule counts unresolved or newly introduced defects in the current draft. A
  defect found in the frozen source is recorded and repaired under its own trace; it does not count as a draft failure unless
  the recomposition introduces or fails to repair it."*
  - Every finding now carries an **origin**: **S** for a defect in the source, **R** for one the recomposition introduced.
  - **The source-defect log** is `paper/v8-source-defects.md` (Qwen P1, DeepSeek). It has twelve entries so far. **None
    has origin R.**
  - Qwen asked whether the defects cluster. They do: **three of the twelve are leftovers from moving text.** A table or
    paragraph was moved, and a reference to it was left behind (S-7, S-11, and in part S-1). `v8_refs.py` exists to catch
    exactly that.
- **Mode 4** (*"re-opens the charge it fails"*) is recorded as loose in the deferred-decisions list, with a direction for
  when the lock is lifted. It is not a task now.

---

## 2. Qwen P2: the "charge" sweep across every other step

I ran ChatGPT's lexical classification over Steps 1, 2 and 4–15.

- **Nouns.** Every use of *charge* as a noun either names its bill or refers to one from immediately before it (*"the
  weight charge"*, *"the mass charge of carried lift hardware"*, *"isolate the charge"*).
- **Step 13.** It already says *"Each comparison states every charge in its own currency"*, which is A′'s rule, stated in
  advance.
- **The verb.** Twelve uses:
  - Eleven are bookkeeping, with the ledger named or immediate: *"charged to the mass budget"*, *"Section 11 charges their
    drag"*, *"charged to the hover-related hardware set"*.
  - **One is a general verb with no ledger (Step 10):** *"The point-mass model prescribes the attitude and therefore cannot
    **charge for** the trajectory the aircraft flies while it is being rotated."*
    **Proposed:** *"…cannot **account for** the trajectory…"* This is the same kind of fix as S-12, and it reopens Step 10
    for a single phrase. **Please vote.**

---

## 3. What Step 2 holds, stated honestly before you read

2A–2D are **the first occurrences** of the root and of the three bills. They carry:

- four protected sentences;
- four quotations from the literature;
- the governing equations.

Most of their text is where it is the only time it appears, and under our stop rules a first occurrence may not move. So the
cutting is small: **1 281 → 1 233 words (−4 %).** Three of the six changes do not shorten anything. They are the two findings
below and one unsourced comparative. **Step 2 will not get much shorter; what gets removed is what is wrong or unsupported.**

---

## 4. Blind reading of 2A–2D — please answer this before §5

> ## The tax
>
> A claim that one architecture escapes a cost shared by the others is only meaningful if the
> cost is stated first, in terms that do not presume the escape. This section states it. It is
> not a claim about any particular aircraft, and nothing in it is new physics; what it provides
> is the accounting that the rest of the paper is checked against.
>
> ### The root: a duty cycle that does not match the hardware
>
> The vertical phase is short. For a mission of one hour, a take-off, a transition, a return
> transition and a landing occupy on the order of a minute — **roughly two percent of the flight.**
> Any hardware installed for that phase alone is carried through the remaining ninety-eight
> percent.
>
> **An architecture that provides the vertical phase with a dedicated lift subsystem therefore
> carries it for fifty times as long as it uses it.** This is not an implementation defect and it
> cannot be removed by making the subsystem better, because it is a statement about duty cycle
> rather than about quality: a lighter or cleaner lift rotor is still carried for the whole flight. **The mismatch between how long a
> component is needed and how long it is present is the origin of all three charges below.**
>
> The statement is deliberately confined to architectures with a dedicated lift subsystem, because
> that is the family the charges describe. Whether any architecture avoids the mismatch — and what
> it pays instead — is the subject of the next section, and it is not settled here.
>
> ### Bill 1 — mass
>
> The most direct payment is dead mass. A lift-plus-cruise aircraft carries two propulsion
> groups: rotors, motors, mounts, wiring and structural reinforcement for the vertical phase, and
> a separate propulsor for cruise. The vertical group provides no required lift or thrust during cruise and is
> lifted anyway.
>
> Its cost is not linear. Mass growth feeds itself — MTOW = m_payload / (1 − f_empty − f_energy)
> puts additional empty mass through a multiplier that grows as the denominator shrinks — and in
> the vertical phase the same increment is charged a second time, because at a fixed disc area
> hover power scales with W^1.5. *(The exponent is a property of the scaling rule chosen: holding
> disc loading constant instead makes hover power grow linearly with weight, and Section 12 uses
> that.)* A modest dead-mass fraction becomes a large payload penalty.
>
> **This charge has been identified independently, and by a source with no interest in the present
> argument.** A NASA study sizing five VTOL architecture families against a common mission with common
> tools found the lift-plus-cruise concepts the heaviest of the vehicles examined, and named the
> cause: not the cruise power draw, since the lift-plus-cruise effective lift-to-drag ratio is the
> higher of the set, but *"the extra empty weight items on board in hover."*
>
> **That finding separates the two things this paper is at pains to keep separate.** The
> lift-plus-cruise vehicle is *aerodynamically better* than the alternatives and it is nevertheless the heaviest, because of
> hardware carried in order to hover. That is Bill 1 stated by an independent source in its own
> terms: not a failure of engineering, but the cost of an architecture.
>
> A second NASA review gives the structural half as a general principle, drawn from a tilt-prop
> aircraft whose propeller separated in flight after a gearbox mounting fatigued: to transmit
> power safely to the extremities of the planform, *"very strong (and fatigue-resistant)
> structures must be incorporated with an obvious weight penalty."* Distributing lift or thrust
> across the span therefore obliges the structure that reaches it to keep transmitting power
> there — charged to mass, whether or not the distributed propulsors are running.
>
> ### Bill 2 — drag
>
> The second payment falls on architectures that leave hover hardware exposed in forward flight:
> rotors stopped in the airstream, the booms that carry them, and the interference between their
> wakes and the wing. Cruise drag has other sources on any aircraft; what is charged here is the
> part attributable to hardware retained for a phase that is over.
>
> Wind-tunnel work on a hybrid airframe found that the difference between propellers parallel to
> the airflow and no propellers at all is modest, while *"the drag produced by the motors is
> significant."* The bill is charged mainly by the motors and the beams that carry them —
> hardware that cannot be feathered, folded or aligned away, **because its cost is its presence.**
>
> Two further measurements support the direction. Characterisation of a quadplane found the
> highest lift and least drag in fixed-wing mode at both cruise airspeeds, with drag in the hybrid
> regime exceeding either pure mode through adverse flow interaction; and that a simulation assuming negligible rotor–structure
> interaction *"always predicts higher lift and lower drag than were experimentally observed."*
> Separately, a study of twenty-six stationary lift propellers held edge-on found their drag
> scaling with frontal area and the square of airspeed, with hover powertrain components adding
> *"a significant amount of aerodynamic drag during forward flight"* in the absence of a stowing
> mechanism.
>
> **The important property of this charge is not its size but where it falls.** It is charged per
> unit time in cruise — so it grows with exactly the quantity the aircraft exists to maximise.
>
> ### Bill 3 — power system sizing
>
> The third payment is the least visible. A VTOL aircraft must install
> enough power to hover, but it draws that power only during the two percent of the flight in
> which it hovers. The ratio between the two demands follows from the governing equations rather
> than from any design choice. Taking hover power from momentum theory and cruise power from the
> drag polar,
>
>     P_hover / W  = √(DL / 2ρ) / η_h                 (DL = W/A, disc loading)
>     P_cruise / W = V / ( (L/D) η_p )
>
> so that
>
>     P_hover / P_cruise = √(DL / 2ρ) · (L/D) / V · (η_p / η_h)
>
> **The quantities on the right come from the configuration and from the propulsion operating
> points, not from the duration of the hover phase.** That distinction matters and the efficiencies
> are the reason for it: η_h and η_p are not configuration constants, they depend on the propeller
> and on the condition it is run at, and Section 11 computes what happens when one fixed-pitch
> blade has to supply both.
>
> A vehicle with a disc loading of 100 N m⁻², a cruise lift-to-drag ratio of 15 and a cruise speed
> of 30 m s⁻¹ needs **between three and four times** as much power to hover as to cruise: the
> geometric terms alone give 3.2, and the efficiency ratio η_p/η_h carries it to about four when
> the cruise propeller is roughly a quarter more efficient than the hover rotor. Raising the disc
> loading raises the ratio as its square root. A flight measurement points the same way: a
> carbon-fibre tail-sitter reported in the literature measures its level-flight power consumption
> at one fifth of its hover power.
>
> The power system is therefore sized by a condition that holds for a minute and is then carried,
> unused, for an hour. And the consequence propagates: sizing by hover means an oversized engine,
> or a battery that must deliver a peak it will rarely be asked for, or both — and whichever is
> chosen, the extra installed capacity is mass: a cost in kilograms, though not Bill 1.

**Reconstruct from the draft alone:**

1. **The root.** What it is, why it cannot be engineered away, and whom it is confined to.
2. **Each of the three bills.** For each one, say what it is, what evidence the text gives for it, and where the text says it
   *falls*.
3. **The hover-to-cruise power ratio.** What sets it, what does *not* set it, and how large it is in the example.
4. **A′ vocabulary.** Is every cost the text names a **charge**, a **cost in a currency**, or **outside the three**? Mark
   any cost that the text classifies wrongly or leaves unclassified.
5. **Evidence strength.** Mark any sentence that claims more than the source it names can support.

---

## 5. The trace — read only after §4

| # | Source | Tag | Why | Qualification / epistemic status | Origin |
|---|---|---|---|---|---|
| A1 | *a lighter lift rotor is still carried for the whole flight, and a cleaner lift rotor is still carried for the whole flight* | **R** → *"a lighter or cleaner lift rotor is still carried for the whole flight"* | The same claim, without the repeated clause | none lost; *"cleaner"*, which points to the drag side, stays | — |
| B1 | *…aerodynamically better than the alternatives **— its cruise efficiency is higher, and the study says so —** and it is …* | **D** | The preceding paragraph already gives the study's higher effective L/D, with its source | none | — |
| C1 | *…and **— a point that bears on how such aircraft are designed —** that a simulation…* | **D** | An aside. Step 11 relies on the quotation, which stays | none | — |
| D1 | *The third payment is the least visible **and often the largest**.* | **D** | *"Often the largest"* has no source; the inventory said *"keep it as the source has it, or drop it; never strengthen it."* | **narrower**: an unsourced comparative goes | S |
| D2 | *…the extra installed capacity is mass, **which returns to Bill 1**.* | **R (S-13)** → *"…is mass: a cost in kilograms, though not Bill 1."* | See S-13 below | none | S |
| D3 | ***The prediction is borne out in flight:** a carbon-fibre tail-sitter … one fifth of its hover power, **which is the ratio this expression gives for an aircraft of that class.*** | **R (S-14)** → *"A flight measurement points the same way: … one fifth of its hover power."* | See S-14 below | **narrower**: *"borne out"* becomes *"points the same way"*, and the unchecked match to the expression goes | S |

The deletion checker flags exactly the three R sentences. All protected sentences are present.

### S-13: "returns to Bill 1" contradicts A′

2D ends: *sizing by hover means an oversized engine, or a battery …, or both — and whichever is chosen, the extra installed
capacity is mass, **which returns to Bill 1**.* A′, three blocks later, defines Bill 1 as *"the mass of a dedicated lift
subsystem"*. An oversized engine is not lift-subsystem mass, and neither is a battery. 3D says of the store: *"It is not
Bill 1 as Section 2 defines it."* So the sentence contradicts both. **My own inventory made the same mistake in Round 77**
(*"Sizing by hover returns to Bill 1 as installed mass"*), before A′ existed.

**Proposed:** *"the extra installed capacity is mass: a cost in kilograms, though not Bill 1."*

### S-14: "one fifth" has had no source since v5

The tail-sitter measurement appears in v5, v6, v7 and v8 in the same words, *"reported in the literature"*, **with no
citation in any version.** I searched:

- **the repository:** no reference entry, no source document in `references/`, and no script computing *"the ratio this
  expression gives for an aircraft of that class"*;
- **the text of every PDF in `references/`:** nothing that is this aircraft.

So neither the number nor the match to the expression can be checked. Under §2.1, a number needs a document you can open.

- **Proposed now (D3):** narrow the sentence to the measurement alone, and drop *"borne out"* and the unchecked match.
- **If any of you can give a downloadable PDF of this measurement, please do.** The author will add it to the repository.
  If no source arrives by the next round, **I propose deleting the sentence**. The example ratio (3.2, and about 4) does not
  depend on it.

---

## 6. On one another

1. **Qwen's revised position on the reference check:** *"manual audit for first resolution, a reviewed list for guarding
   what has already been resolved."* That is how `v8_refs.py` already works for *table* and *row*. Qwen proposes extending
   it to relational nouns once a person has resolved them. **Grok, ChatGPT, DeepSeek:** does that answer your objection?
   The script would guard a decision already made, not make one.
2. **DeepSeek:** *"every 'Section X' must resolve"*. `links.py` already checks this. Is there a kind of reference it should
   check that it does not?
3. **Mode 1.** In the blind readings you mapped it differently:
   - Grok, ChatGPT and DeepSeek: *both duties*;
   - Qwen: *same hardware / both duties, and not orientation*.

   It is locked and needs no change. **Does the difference matter to any later step?**

---

## 7. What I am asking

1. **Confirm §1.**
2. **§2:** vote on Step 10, *"account for"*.
3. **§4:** your blind reading, before anything else.
4. **§5:** vote on A1, B1, C1, D1, D2 and D3, one by one. For **S-14**, also say whether you have a source.
5. **§6**, and any **new proposals**.

**Sources:** only for S-14, as a downloadable PDF, if you have one.
