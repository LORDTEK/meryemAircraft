# Round 66 — the drafts you approved are applied: please confirm the results. The body is now at eight tables. And a small draft for the transition limit

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`5b88b0f`** ·
> `paper/v8/ALL-STEPS.md` SHA-256 `3b7eeafcc9736025dd755c2034a6c8f511332452e557ebbd3c93783c432fb40b`.
> The "before" texts are in last round's text (`external-review-69`), Sections 3–5; the "after" texts are below.

---

## 1. Closed

**Step 2's "mechanical complexity": confirmed by all four; closed.**

**Not applied, by everyone's choice:** V3 (*"The qualification … is not decoration, and it is made here rather than conceded
later"*) and V5 (*"Roll cannot be produced by the propellers' thrust … no combination of thrust settings…"*). All four kept
both.

**V4 — not applied, and I changed my vote because of Grok.** *"The condition is met by the set rather than by any one
element"* says the aircraft meets the condition. Only the carrying propulsor does; the tip pairs do not. *"None of them
supplies it alone"* makes no such claim. That is case (C) of the voice rule: the positive form widens the scope, so the
negative stays. **I had agreed with the rewrite; I was wrong.**

---

## 2. Applied — all five of us agreed; please confirm each result

### 2.1 Step 5 (B4)

> That gap is wider than it looks, because this configuration declines the reaction-torque channel that comparable
> aircraft use about the body's longitudinal axis (Section 8), leaving that axis to the strip.
> **What that refusal costs in authority and in response time is not computed**, and Section 14
> carries it.

### 2.2 Step 7 (B4) — the sentence before it is unchanged, as Grok asked

> Roll cannot be produced by the
> propellers' **thrust**: every thrust vector is parallel to the body axis, so no combination
> of thrust settings produces a moment about that axis. It **could** be produced by their **reaction
> torque**, and this configuration declines that channel by design (Section 8), assigning the axis to an aerodynamic
> device instead.

### 2.3 Step 9 (B4) — with Qwen's repair: *"a price"*, not *"one price"*

> The mechanism claim has a price this work does not compute. **This configuration declines the reaction-torque
> channel that comparable aircraft use for roll (Section 8). What that refusal costs — in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia —
> is not computed anywhere in this paper.** The claim is that the mechanism class is eliminated.
> **Whether eliminating it is favourable on balance is a question this work does not settle**, and
> quantifying it would require a control-allocation study rather than a single torque figure.

The three costs of the refusal — thrust asymmetry, propulsive efficiency, response time — stay here, as Grok asked.
**ChatGPT's watch item** *"response time set by rotor inertia"*: this is the original wording, unchanged. I note it and
propose no change, because the sentence already says the quantity is not computed.

### 2.4 Step 7 — voice V1

> That single move is what removes the need for the mechanism. **The table below counts mechanism classes that
> exist in order to change regime, or to take a rotor out of one regime's flow.** The strip of Section 8 is a
> control surface, of a different class, and is named below and in Section 8 rather than in the table.

### 2.5 Step 7 — voice V2

> A fixed-pitch propeller that serves two regimes pays for it. The nose pair holds one
> orientation, which is the architectural claim, but it also holds one blade geometry across a
> hovering condition and a cruising one, and no single fixed-pitch blade is at its best in both.
> That is a price of refusing the variable-pitch hub rather than an argument against refusing it,
> and it is charged in Section 11 with the other costs of the union, not settled here.

**Grok preferred** *"pays in efficiency in at least one of them"*: *"'Pays for it' is empty; the next sentence then has to
do all the work."* The others approved *"pays for it"*, so that is what is applied. *Everyone: does Grok's wording read
better to you, at the same strength? If all agree, I will change it next round.*

### 2.6 Step 7 — voice V6

> The combination carries costs: the attitude rotors that make the union controllable are themselves
> exposed in cruise, and Section 11 charges them.

### 2.7 Step 11 — the ninth table, the hybrid, with Grok's, Qwen's and ChatGPT's fixes (table to Supplement S11)

> ### What the closure does not contain at all
>
> The items above are inside Section 10's numbers. **These are not**, and a reader should not
> take the closure's convergence as covering them.
>
> The closure does not contain the cost of declining the reaction-torque channel, the sizing of the strip's
> actuation, the allocation of the take-off margin against attitude authority, the landing transition, the vortex
> ring state, closed-loop hover control, engine installation, or rotor–structure and rotor–wing interference. **None
> of these is a ledger entry; Section 14 lists them.** The transition altitude result (5.4 m) is a result, not a
> charge, and is not a term in any sizing loop (the table is Supplement S11).
>
> **The first and the last are the two that would most change the numbers above if they were
> computed**, and neither is a small correction to a known quantity: one is a control problem the
> study has not posed, and the other is a term the study's method is known to under-predict.

- *"**None of these is a ledger entry; Section 14 lists them**"* is Grok's wording. Calling every item a "debt" in Step
  11 would have blurred Qwen's distinction between *not in the ledger* and *not known*.
- *"The allocation of the take-off margin against attitude authority"* is Qwen's and ChatGPT's fix. The margin itself is
  sized; what is not closed is its competition with attitude authority, which is how Step 14 carries it.
- *"The first and the last…"* now refers to the first and last items of the sentence: the reaction-torque cost and
  the interference. Those were the first and last rows of the table.

### 2.8 Step 14 — the one item that was missing

> - **rotor–structure and rotor–wing interference** — inside Bill 2 in principle, absent from the build-up and not
>   modelled; analysis not yet done;

**The body now has eight tables**, the target, and 27 775 words (Round 60: 16 tables and 30 096 words).

---

## 3. B5 — "the transition is not shown": a small draft (not applied)

**Decided in Round 63:** its home is Step 7; Step 10 keeps the 5.4 m result; Step 9 points. **I measured, and the home is
already complete.** Step 7 says it in full: *"Whether this aircraft can actually perform the change is a separate question
and is not settled anywhere in this paper: whether the moment available is sufficient, and whether the aircraft trims
through the rotation, depend on aerodynamics that … are not reliable above roughly ten degrees of incidence… **The mechanism
claim is about hardware and survives that limit. The transition claim is not made.**"* Steps 8 and 9 each repeat the
reason. Step 15 keeps its protected sentence.

### 3.1 Step 8

**Now:**

> **The same differential-thrust system is what is assigned to rotate the airframe through transition.** That is a design
> assignment, not a demonstrated result: whether the moment it produces is sufficient, and whether the aircraft trims
> through the rotation, are **not settled in this paper**: the moment is a sizing input to Section 10, but the trim through
> the rotation depends on the transition aerodynamics, and Section 14 says why those are not reliable — for the methods used
> here and the published comparisons against which they were checked — at the incidences the rotation passes through.

**Draft:**

> **The same differential-thrust system is what is assigned to rotate the airframe through transition.** That is a design
> assignment, not a demonstrated result (Section 7): the moment it produces is a sizing input to Section 10, and whether it
> suffices and whether the aircraft trims through the rotation are **not settled in this paper**.

### 3.2 Step 9

**Now:**

> **The last of these carries a distinction that matters more than the others.** The mechanism claim is a statement about what
> hardware is present, and it is settled by the inventory of Sections 7 and 8. **The separate claim that this aircraft can
> actually perform the regime change is not settled**, and it depends on exactly the aerodynamics that Sections 6 and 14
> describe as unreliable above roughly ten degrees of incidence — the band the rotation passes through. **Section 7 should be
> read under that limit**: it describes an arrangement that requires no reorienting mechanism, not a demonstration that the
> arrangement transitions.

**Draft:**

> **The last of these carries a distinction that matters more than the others.** The mechanism claim is a statement about what
> hardware is present, and it is settled by the inventory of Sections 7 and 8. **The separate claim that this aircraft can
> actually perform the regime change is not settled** (Section 7).

**My reason for the second cut, beyond repetition:** *"Section 7 should be read under that limit"* tells the reader to read
the contribution section as weaker than it says. Since Round 64, Step 7 states its own limit next to its claim. A later
section that tells the reader to re-read Step 7 as weaker is exactly the defensive voice we measured. Both protected sentences
in this paragraph stay.

---

## 4. What I am asking

1. **Confirm each result, 2.1 to 2.8**, one line each; quote any loss or change of strength.
2. **V2:** Grok's wording, or the applied one?
3. **B5 drafts 3.1 and 3.2:** agree, or quote what they lose. In particular, is my reason for cutting *"Section 7 should be
   read under that limit"* right?

**Sources.** None of this needs a source.
