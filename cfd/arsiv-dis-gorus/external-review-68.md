# Round 64 — five more agreed changes applied and shown; an old error found while applying one; and the author asks whether the paper still has its soul

> **This is a task. Please answer it now.**
>
> **New, please: begin your reply with your name alone on the first line** — *Grok*, *ChatGPT*, *DeepSeek*
> or *Qwen*. The author pastes your replies to me and this spares him labelling them.
>
> Every change is shown before and after, verbatim. Everything else is as in the Round 60 text
> (`external-review-64`, Section 6), amended by Rounds 62 and 63.
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`5035e73`** ·
> `paper/v8/ALL-STEPS.md` SHA-256 `7e087ab3cc85454c9545f441215fe4617d8493fd38fbf69b01b6c67caad7e654` ·
> `paper/v8/supplement.md` SHA-256 `e05f6b5aad731785d263269868a6701facb40c311f82fb11f4fd831e777fd859`

---

## 1. The author's question this round — is the soul still there?

The author asked me, in effect: *we asked the readers about the soul; is the reason this paper exists still
in it, or has it turned into something else?* I measured before answering. **My answer, which I am asking
you to check:**

**It has not been lost, but it has not yet been made to lead, and the voice works against it.**

- **Named early and protected.** The contribution is named 5.8 % of the way into the text (Step 1, ending
  on the contribution since Round 62), and ten sentences that carry it are under the same automated
  check as the caveats.
- **Still outweighed.** The calculations (Steps 10–14) are **42 %** of the text; the combining section
  (Steps 7–8) is **13 %**. Our agreed structure makes 7–8 the centre, but the structure has not been
  built yet. So far we have removed words, not moved weight.
- **The voice is defensive.** I counted sentences containing a negation (*not, no, never, nothing, none,
  nor, cannot*). **45 % of all sentences** have one. **Step 7, the combining step, has 50 %**; Step 9 has
  61 %; the close has 72 %. Some of those negations are the insight itself (*"no mechanism that reorients a
  propulsor"*), and many are caveats that must stay. But a paper whose central section says half its
  sentences in the negative reads as a list of things it does not claim.

Last round ChatGPT put the risk exactly: *with only the caveat list, the paper gradually becomes a defence
text; with only the insight list, a promotional one.* **We have 140 caveats and 10 insight sentences.** The
process so far has been much better at preventing over-claim than at making the insight lead.

**My proposal, for your criticism:** a *voice pass* on Step 7 before any further cuts there. For each
negative sentence in Step 7, decide: is it a caveat on the list (it stays as written), or is it negative
framing of something that can be said positively **at the same strength**? Example of the second kind,
from Step 7: *"There is no dedicated lift system to carry"* could be *"Every propulsor that lifts the aircraft
also drives it in cruise"* — only if that is true of the tip pairs too, **which it is not**, so this one stays
negative. That is the discipline: a positive rewrite is allowed only where it is not stronger.

---

## 2. Last round's results — your confirmations

| Change | G | C | D | Q | Status |
|---|---|---|---|---|---|
| Step 14 repaired (the lost clause) | ✓ | ✓ | ✓ | ✓ (S14 keeps the original row verbatim — it does) | **Closed** |
| Step 11 — Qwen's condition | — | ✓ | ✓ | ✓ | **Closed**; Qwen's extra sentence *"Every cost named below is already inside the closure of Section 10"* is now protected |
| Step 4 table → prose | ✓ | ✓ | ✓ | ✓ | **Closed** |
| Step 4 weight breakdown → S4 | ✓ | ✓ | ✓ | ✓ (S4 has it verbatim — it does) | **Closed** |
| Step 4 quadrotor contrast → S4 | ✓ | ✓ | ✓ | **only if** *"the isolation test above is what carries the prediction"* returns | **Repaired** (3.1), back to all |
| Step 4 pointers | ✓ | ✓ | ✓ | ✓ | **Closed** |

## 3. Decided — all five of us

- **B1** (Grok's slice): the combining section keeps the count, the strip, the declined channel and which
  parts fail; the soundness section keeps Step 9 and the unsettled remainder of Step 8.
- **B6**: the phenomenon in Step 6; the 14.6–21.0 % figure and *"No variable-pitch counterfactual was computed"*
  in Step 11; Step 6 keeps its own limit (*"…would recover that difference is not computed…"*, now protected).
- **B7**: Step 2's transfer table and Step 9's four-axis table stay in the body. **Step 11's build-up becomes
  prose carrying every figure** — Grok's and Qwen's condition — which is what I applied (3.2). *ChatGPT withdrew
  its objection.*
- **"removes the need for the mechanism"**; **N1**; **N3** with Qwen's wording fix.

---

## 4. Applied this round — please confirm each result

### 4.1 Step 4 — Qwen's condition

**Before:**

> **The quadrotor is reported for scale, not as the test**: against it the lift-plus-cruise design
> changes three things at once, and the contrast is in Supplement S4.

**After:**

> **The quadrotor is reported for scale, and the isolation test above is what carries the
> prediction**: against it the lift-plus-cruise design changes three things at once, and the contrast is in
> Supplement S4.

### 4.2 Step 11 — the build-up table becomes prose, every figure kept (table to Supplement S11)

**Before (the table is in the Round 60 text; this is the text around it):**

> The zero-lift drag coefficient of Section 10 is a build-up with named terms. Splitting it:
>
> | | favourable end | adverse end |
> |---|---:|---:|
> | Clean wetted surface | 0.0073 | 0.0142 |
> | Hub and small items | 0.0015 | 0.0022 |
> | **Tip frames** | **0.0043** | **0.0047** |
> | **Attitude rotors, free-wheeling** | **0.0154** | **0.0169** |
> | Total | 0.0285 | 0.0381 |
>
> *(The two columns differ for two separate reasons, and a reader dividing cells should know which
> is which. The clean surface and the hub are where the drag bracket itself lives, so their base
> values differ between the ends. On top of that, the adverse end carries a ten percent margin
> applied to the whole build-up. The frames and rotors have the same base value at both ends and
> differ only by that margin. **No line item at the adverse end is an independent measurement**, and
> they should not be subtracted from one another as if they were.)*

**After:**

> The zero-lift drag coefficient of Section 10 is a build-up with named terms. At the favourable end it is 0.0073 for the clean wetted surface, 0.0015 for the hub and small items,
> **0.0043 for the tip frames and 0.0154 for the free-wheeling attitude rotors**, 0.0285 in all; at the
> adverse end the same terms are 0.0142, 0.0022, **0.0047 and 0.0169**, 0.0381 in all.
>
> *(The two ends differ for two separate reasons, and a reader dividing one term by another should know which is which. The clean surface and the hub are where the drag bracket itself lives, so their base
> values differ between the ends. On top of that, the adverse end carries a ten percent margin
> applied to the whole build-up. The frames and rotors have the same base value at both ends and
> differ only by that margin. **No line item at the adverse end is an independent measurement**, and
> they should not be subtracted from one another as if they were.)*

The note now says *"the two ends"* and *"dividing one term by another"* instead of *"columns"* and *"cells"*.

### 4.3 Step 3 — N1 applied (table to Supplement S3)

> Depart from any one of those and a
> charge appears. **Different hardware** costs Bills 1 and 2: the unused set is carried for the whole
> flight and, if exposed, drags. **The same hardware serving only one duty** costs them again: a
> propulsor that lifts and is then carried is a dedicated lift group under another name, whatever it
> shares with the cruise system. **The same hardware serving both duties in a different orientation**
> is the tilting family: Bill 3 is left standing unless a store supplies the hover peak, and the
> mechanism that changes the orientation adds mass and introduces a control problem through the turn.
> **The same hardware, both duties, one orientation, but a different sizing point** leaves Bill 3 —
> unless the hover peak is supplied from somewhere other than the continuously installed power.
>
> Read one at a time, these are ways to pay. Read as a conjunction, they are a condition.

The four references to *"row"* now say *"departure"*.

**And an old error found while applying it.** Step 3 said *"The second row of the inverted table — same
hardware, different orientation"*. **Different orientation was the third row.** The second is "one duty". The
"one duty" row was added to the table after that sentence was written, and the reference was never updated.
None of us had caught it.

**Before:**

> One consequence is worth stating now, because it shapes everything after it. The second row of
> the inverted table — same hardware, different orientation — is refused by a means other than the
> one the field has adopted. A tilting architecture accepts that row and buys its way out of the
> first with a mechanism.

**After:**

> One consequence is worth stating now, because it shapes everything after it. The third departure — same hardware, both duties, different orientation — is refused by a means other than the
> one the field has adopted. A tilting architecture accepts that departure and buys its way out of the first with a mechanism.

### 4.4 Step 1 — N3 applied (the removed material to Supplement S1)

With Qwen's fix: *"they are the only one of those documented obstacles an uncrewed aircraft removes"*, which
keeps Step 5's limit (*"That disposes of the spatial-orientation objection and nothing else"*).

> ### The third route is established, and some of its difficulties are inherited
>
> There is a third way to put one set of propulsors into both regimes without reorienting them: **point the
> thrust line at the ground and let the whole aircraft rotate.** It is neither new nor untried nor abandoned.
> The Convair XFY-1 flew it in 1954 and completed six transitions to conventional flight *"before testing was
> curtailed because of engine and gear-box reliability problems"*, and uncrewed tail-sitters have revisited the
> route continuously since. The pilot's spatial orientation and workload, recorded for that programme, were real
> and severe, **but they are not what curtailed the testing**, and they are the only one of those documented
> obstacles an uncrewed aircraft removes.
>
> **Some of the difficulties were real, internal, and are inherited here.** A tail-sitting vertical descent is
> harder than a runway landing; a tail-sitter on the ground is more exposed to crosswind; and propellers whose
> thrust vectors are all parallel to the body axis produce no rolling moment **by any combination of thrust
> settings**. The reaction-torque channel that other coaxial tail-sitters use about that axis is a choice this
> configuration declines rather than a limit it inherits (Sections 7 and 8). Precise hovering, ground gusts and
> the absence of a thrust-borne rolling moment are configuration facts, and they are inherited.
>
> Three things are available now that were not: electric drive on each individual rotor, sensor-based attitude
> reference, and enough onboard computation that stability need not come from the airframe alone. **The uncrewed
> tail-sitter literature has been exploiting exactly those three for over a decade**, which is why the gap below is
> not a historical one.

### 4.5 Step 7 — the protected sentence, reworded (the protected list changed in the same commit)

**Before:** > That single move is what removes the mechanism.

**After:** > That single move is what removes the need for the mechanism.

**Size:** 28 014 words, **9 tables** in the body (Round 60: 30 096 and 16). Target: about 7 500 and 8.

---

## 5. My positions on what is new — please criticise them

**Step 2 still says "mechanical complexity".** Its transfer table's tilt row reads *"…together with mechanical
complexity, gyroscopic coupling and a transition control problem, which are not among the three."* We removed
*"complexity"* from Step 3 because it is not measured anywhere (ChatGPT). **The same objection applies here.**
Qwen asked that this wording be protected. I would instead remove *"mechanical complexity,"* and keep the
gyroscopic coupling and the transition control problem, which Step 2's own prose names (*"a pivot, an
actuator, the gyroscopic coupling of a reorienting mass, and a control problem through the turn"*). *Qwen
especially: does removing it lose something your protection was meant to keep?*

**ChatGPT's watch items.** *"Introduces a control problem through the turn"* (Step 3) is at the strength the
table already had: *"is itself mass, complexity and a control problem through the turn"*. It is not new. *"Exploiting
exactly those three for over a decade"* (Step 1) is unchanged text, and Step 1's next subsection lists the
literature that supports it. I note both; I propose no change.

**What comes next.** B4 and B5 need pointer edits in several steps (the declined channel is stated in Steps 1, 5,
7, 8, 9, 14 and 15; *"the transition is not shown"* in 1, 5, 7, 8, 9, 10, 14 and 15). **I will bring those as
drafts next round, one step at a time, not applied.** The ninth table (Step 11's *"What the closure does not contain
at all"*) is the obvious candidate to reach eight; Grok once proposed merging it into Step 14's list.

---

## 6. What I am asking

1. **Confirm or reject each result in Section 4** (4.1 to 4.5), one line each; quote any loss or change of strength.
2. **The soul (Section 1).** Do you agree with my measurement and my reading of it? If not, what do you see
   instead? **Then, for Step 7:** name up to three negative sentences that are *not* caveats and could be said
   positively at the same strength, with your rewrite; or say that none can.
3. **Step 2's "mechanical complexity"**: remove, or keep, and why.
4. **The ninth table** (Step 11's "What the closure does not contain at all"): merge into Step 14's list, move
   to the supplement, or keep?

**Sources.** None of this needs a source. PDFs only for priority claims, numbers taken from tables and verbatim
quotations — and say which document you opened in this conversation for any number you give.
