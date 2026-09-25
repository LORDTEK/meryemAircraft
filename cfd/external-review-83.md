# Round 79 — all four of you accept the content of (d). Two wording points and one Step 4 word remain, and the final package is here for a last vote. S-5 is sharper than I reported, and I explain why

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`4bfed5e`**. Nothing in Steps 2–4 has changed since Round 78. Every
> text you are asked to vote on is quoted below in full, current wording first and proposed wording second.

---

## 1. Where (d) stands

| | Grok | ChatGPT | DeepSeek | Qwen | Me |
|---|---|---|---|---|---|
| Content of A, B, C | accept | accept | accept | accept | yes |
| Wording of A | **only with a limit**: the definition must not read as 2A's own; state that the root ranks above the charges | accept, as a clarification of existing vocabulary and not a redefinition | accept | accept | Grok is right; see A′ |
| Notation in B, *"1 in kilograms"* | **reject**: it repeats the very mix we diagnosed, because in this table *1* has meant Bill 1 | accept | accept | accept (*"perfectly captures"*) | Grok is right; see B′ |
| Column header | P27: the header has to say when a cell names a currency | — | propose renaming it | — | yes; see H |

**Because of Grok's two conditions, nothing is applied yet.** We followed the same practice in Round 76 with #18: when a
reader vetoes one wording, the narrower wording goes back to everyone before anything is applied. C is accepted by all
four as written, but it would contradict the table if it were applied alone. So the whole package goes to one final
vote.

---

## 2. The final package — please vote on each part

**A′ — a new passage in 2E, after *"…is tested in Section 12."*.** This replaces A.

> **A charge and its currency are not the same thing.** The mismatch of the root is the origin of all three charges; each
> charge is one specific payment, not the name of the currency it is paid in. Bill 1, as this accounting uses it, is the mass
> of a dedicated lift subsystem; Bill 2, the cruise drag of hover hardware left exposed; Bill 3, continuous power installed
> to a hover peak. A remedy's own cost can fall in kilograms, drag counts or installed kilowatts without being one of the
> three charges, and the table names such a cost in words rather than by a bill's number.

What changed from A, and why:

- **The root ranks above the charges** (Grok). The passage uses 2A's own wording, *"the origin of all three charges"*,
  which is a protected sentence in 2A.
- **"as this accounting uses it"** in place of Grok's *"as the table uses it"*. My reason: 3D and Step 11 use Bill 1 outside
  the table, in the condition and in the ledger. A definition limited to the table would leave their phrase *"as Section 2
  defines it"* pointing at the table only. **Grok, does this wording meet your limit?**
- **The last sentence reverses A.** A said *"a number names the currency"*. A′ says that numbers name bills and that any
  other cost is written in words. This is Grok's point: in this table *1* has always meant Bill 1.

**B′ — the tilt row, right-hand cell.** This replaces B.

> kilograms, not Bill 1 — the pivot and its actuators; **Bill 3 is left standing** — with no store, the power plant is still
> sized by the hover peak; and gyroscopic coupling and a transition control problem, which are **not among the three**

*(The words "Bill 3 is left standing" are unchanged here, but S-5 below may change them.)*

**C — the paragraph under the table.** Unchanged from Round 78. All four of you accepted it.

> **One row pays part of its cost in none of the three currencies, and that is not an oversight.** What a tilting
> architecture buys its unified propulsion group with is a mechanism — a pivot, an actuator, the gyroscopic coupling of a
> reorienting mass, and a control problem through the turn. The pivot and the actuator are paid in kilograms, although they
> are not lift-subsystem mass; the coupling and the control problem are paid in none of the three. That part is a cost, but
> it is not one of the three charges this accounting tracks, and the next section says why it is treated separately.

Grok's check that *"That part"* stays attached to coupling and control: it follows directly after them, so it holds.

**C4 and C5 — two further cells, which follow from A′.** A′ says numbers name bills. The pitch hub is not lift-subsystem
mass. And a failure mode is in no currency. So two more cells must change:

| Row | Current cell | Proposed cell |
|---|---|---|
| Variable pitch (C4) | 1 — pitch hub, actuation, and a new failure mode | kilograms, not Bill 1 — pitch hub and actuation; and a new failure mode, not among the three |
| Folding (C5) | 1 — mechanism, actuation, locking, a new failure mode | 1 — mechanism, actuation, locking; and a new failure mode, not among the three |

**H — the column header** (Grok P27, DeepSeek):

| Current | Proposed |
|---|---|
| Bill it creates | What it creates — a bill by its number, any other cost in words |

**On application:** Grok P26 is adopted. *"One row does not pay in any of the three currencies"* joins the retired-phrase
list, so any later sentence that restores it stops the pass.

**ChatGPT's pre-draft check, run on the table as the package would leave it:**

| Row | Cost | Currency | Named as a bill? | Where is it defined, or excluded? |
|---|---|---|---|---|
| Distributed lift | rotors and mounts; exposed rotors | kg; drag | 1; 2 | A′ |
| Folding | the mechanism on the lift group; a failure mode | kg; none | 1; no | A′; 2F (*"not thereby exempt from being counted"*) |
| **Tilt** | pivot and actuators; hover-sized plant; coupling and control | kg; kW; none | **no**; 3; no | A′ and C; S-5; C and 2F |
| **Variable pitch** | hub and actuation; a failure mode | kg; none | **no**; no | A′; 2F |
| Higher disc loading | hover power | kW | 3 | A′ |
| Lower disc loading | larger lift rotors | kg; drag | 1; 2 | A′, within the scope 2A sets (*"deliberately confined to architectures with a dedicated lift subsystem"*) |

**All six rows pass**, with one exception: the tilt row's Bill 3, which is S-5.

---

## 3. One word in Step 4 (Qwen). Your answers differed, so it goes to a vote

The current sentence in Step 4:

> It does not escape the accounting by avoiding the mass charge; it *moves* the charge — to the mechanism that reorients its
> propulsors, with the actuation, the gyroscopic coupling and the transition control problem that Section 2 assigns to that
> family.

How each of you read it:

- **Qwen:** under (d), *"moves the charge"* becomes inaccurate, so it must be fixed.
- **Grok:** it becomes *"loose, not false"*, so leave it.
- **ChatGPT:** it becomes consistent with the table.
- **DeepSeek:** it stays true.

**My view: Qwen's diagnosis is right, and Grok agrees with the diagnosis.** A′ introduces the distinction between a charge
and a currency. The very next section would then use *"the charge"* for the mechanism, which A′ says is not a charge. A
referee reading 2E and then Step 4 would see that. The smallest repair is a single word:

> It does not escape the accounting by avoiding the mass charge; it *moves* **the cost** — to the mechanism that reorients its
> propulsors, …

I checked every other use of *charge* in Step 4. Each one (*"the weight charge"*, *"the mass charge of carried lift
hardware"*, *"the first charge"*) refers to Bill 1 itself, and none of them changes. **This would reopen a closed step by one
word, so it needs the vote of all four of you.** If anyone says no, the sentence stays as it is and the looseness is
recorded.

---

## 4. S-5 is sharper than I reported

All four of you accept that there is a gap, although Qwen calls it *"a slight ambiguity"*. DeepSeek and Qwen name the
baseline as **the architecture the move modifies**, and so do I. ChatGPT asks for the baseline to come from 2F's own logic.
Grok lists three candidates.

**What I had not connected in Round 78.** Step 4 says the isolated pair *"share the mission, the payload, **the turbo-electric
propulsion architecture** and the presence of a cruising wing"*. If both aircraft size their continuous plant by the hover
peak (I have not checked this), then in that pair *"Bill 3 is left standing"* means *no worse*. In that case:

- The tilt-wing reduces Bill 1: it has no lift group.
- Bill 3 is no worse.
- Its own cost in kilograms, the mechanism, is **smaller** than the saving. Step 4's own words are *"giving **part** of the
  structural saving back"*.

**2F's positive test defines a counter-example in exactly that form:** a remedy that reduces one charge, leaves the other
two no worse, and whose own cost is demonstrably smaller than the reduction, in the same currency. And 2F says: *"a remedy
that is simply a better bargain in one currency refutes it."*

**What stands between the tilt-wing and a refutation** is therefore neither *"left standing"* nor Bill 3. It is the other
clarification in 2F: *"a remedy whose cost falls **outside** the three charges does not refute the accounting"*. In other
words, the tilt-wing is not a counter-example because of the coupling and the control problem.

2F itself warns against exactly this: *"A framework that could absorb any cost by declaring it out-of-scope would be
unfalsifiable."* 2F also answers the warning: costs outside the three *"are listed, not waved away"*.

**I do not claim that the accounting is refuted.** Two things are unchecked:

- how NASA's *structure* and *propulsion* categories map onto the charges;
- whether the two designs size their continuous plant by hover.

**My claim is narrower.** Once the baseline is named, the tilt row survives 2F's test only through the clause about costs
outside the three. The paper should say that openly, not leave it to *"left standing"*.

**My position:**

- 2F should name the baseline: the architecture the move modifies.
- The tilt row's Bill 3 depends on how that architecture supplies its hover peak. **If the peak comes from a store, tilting
  without a store *creates* Bill 3, which is a transfer. If the peak comes from continuous plant sized by hover, tilting
  leaves Bill 3 standing, and the row stands only on the outside-the-three clause.**
- No wording yet.
- **No 3B draft until this is settled** (ChatGPT). 3B's third departure uses the same words: *"Bill 3 is left standing unless
  a store supplies the hover peak"*.

**One question to all of you.** The contribution does not depend on tilt paying more. It is the mechanism class. So does
saying openly that tilt is shielded only by costs outside the three weaken anything the paper claims? My reading is that it
does not: Step 4 already says the tilt-wing is the lighter design. But I would rather hear it from you.

---

## 5. Small corrections, and proposals

- **Qwen, Q2:** *"which is why Step 11 says it 'makes the same complaint'"*. Step 11 says this of the **buffer**, not of the
  tilt mechanism.
- **Qwen, S-5:** *"the accounting only claims that if you carry a dedicated lift group, you pay Bill 1"*. 2F says *"The
  accounting claims transfer."* Your *"another of the three charges standing"* is a useful clarification, and it is part of
  the S-5 package once the baseline is agreed.
- **Grok and ChatGPT, both accepted:** your corrections to Round 77 stand.

| Proposal | My view |
|---|---|
| Grok P26: retire the *"One row…"* phrase | Adopted on application (§2) |
| Grok P27, DeepSeek: header | This is H |
| ChatGPT: a charge/currency invariant before drafting | Run in §2; it becomes a standing pre-draft step for every table |
| Qwen P1, Grok P24: a charge-or-currency flag in the trace | Yes; one column |
| Qwen P2: tighten Step 11's buffer sentence under (d) | Recorded for when Step 11 is next opened; not now |

---

## 6. What I am asking

1. **Vote on A′, B′, C, C4, C5 and H, each separately.** Grok, does A′ meet your limit?
2. **Vote on the one-word change in Step 4**: *"moves the charge"* → *"moves the cost"*.
3. **S-5:**
   - Is the baseline *the architecture the move modifies*?
   - Do you agree that the tilt row survives only on the clause about costs outside the three?
   - Does saying so weaken anything?
4. **New proposals**, as always.

**Next round:** if every part is agreed, the package is applied and shown before and after for your confirmation. S-5
wording follows once the baseline is agreed. **3B drafting waits for both.**

**Sources.** No new source is needed. Every quotation is from Steps 2 and 4 and from Supplement S4.
