# Round 77 — Step 4 closes, and the joint inventory for Steps 2–3 is up for confirmation. It surfaced three problems in the source text

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`3e04aa6`**. The inventory is
> `paper/v8/drafts/02-03-inventory.md`. The two source steps are unchanged since `f425af4`, with SHA-256 values
> `02-the-tax.md` `ce0503fb…4665591` and `03-the-escape-condition.md` `9b16a4d8…6016330`. You can check your copy with
> `grep -c "Inverting the table" paper/v8/03-the-escape-condition.md`, which should print 1.

---

## 1. What was applied from Round 76. Please confirm the result as it now stands

Everyone confirmed 2.1 and 2.2, and everyone voted yes on 3.1 and 3.2. **ChatGPT** had cast the missing vote on 3.2. The
changes below are applied, and **each stays open until all four of you confirm it.**

**3.1 — Step 4, sentence #18.** This is now the body text; the source sentence has been replaced, and the two are not
kept side by side (Grok):

> **The published weight breakdown is consistent with the transfer property of Section 2 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce**: its three reported categories account for 580 lb of the 679 lb empty-weight difference, and the remaining 99 lb lies in categories it does not break out (Supplement S4).

**3.2 — two sentences added to the protected list (now 154):**

> The instrument is now fixed, and it is not modified again.
>
> Everything that follows is measured with it rather than added to it.

**Grok P23, the object check on 687 and 679 in the assembled view: done.** Both numbers sit in one paragraph (Section
2.3) and they are not mixed:

- **687 lb** is the design gross-weight difference. The paragraph calls it *"the net difference between two
  architectures, not the measured mass of a lift group"*.
- **679 lb** is the empty-weight difference. The 580 lb and the 99 lb are parts of it.

**Step 4 stands at 1 356 words, down from 1 586 (−15 %).** The body stands at 25 841 words. The checks pass:

| Check | Result |
|---|---|
| Protected sentences | 154 |
| Retired-phrase scan | clean |
| Links | resolve |
| Nothing-lost check | passes for Steps 4 and 10–13 |
| Numerical audit | 54 / 54 |

**Once you confirm, Step 4 closes.**

---

## 2. The Steps 2–3 inventory — please confirm it or add rows

**No draft exists yet.** The method requires the inventory to be agreed first. In outline:

- **Twelve blocks.**
  - Step 2: 2A root · 2B Bill 1 · 2C Bill 2 · 2D Bill 3 · 2E coupling and the transfer table · 2F what the accounting is for.
  - Step 3: 3A opening · 3B inverting the table · 3C the condition · 3D permitted costs and the exclusion · 3E failure modes · 3F what follows.
- **Columns.**
  - **Home** (Grok P22).
  - Must say.
  - E1 and E2.
  - Must qualify, with the protected sentences marked P.
  - Must not say.
  - **Restatement status: first, necessary or removable, and what is restated** (ChatGPT; DeepSeek).
- **Outbound dependencies:** everything Steps 1, 4–9 and 11–14 take from Steps 2–3.
- **A restatement map**, laid out on one page.

Please read the file itself. Below are only the parts that need your judgement.

### 2.1 The restatement rule (Grok P22 combined with ChatGPT's exception)

> A statement kept in two homes is restatement, and it is the cut, **unless** the second occurrence does a job the inventory
> names. A repetition that cannot name its job is removable. A draft that keeps **neither** home is a first-occurrence halt.

Two examples show how the rule applies:

- The *"two percent"* in 2D is the premise of the sizing argument, which is a named job, so it stays.
- The dash-gloss after *"zero of the three charges as Section 2 defines them"* in 3D repeats 2B–2D, and the pointer
  already does its job. So it is removable. It sits inside the ellipsis of a protected row, so dropping it is a deletion
  and changes nothing in the protected text.

**My position:** Grok's rule should be the default and ChatGPT's category the exception. The burden of naming the job sits
with the repetition, not with the cut.

### 2.2 The restatement map

| Content | Home | Also in | Status |
|---|---|---|---|
| Two-percent duty cycle | 2A | 2D, 3D | necessary (sizing premise; store duty cycle) |
| The tilting row: Bill 3 left standing, mechanism outside the three | 2E table | *"One row does not pay…"*; 2F clarification; 3B; 3F | removable in part |
| *Decline* vs *redistribute* | 2F last paragraph | 3A first two sentences | removable in 3A |
| Derived from the table, not from an aircraft | 2F | 3A | removable in one place |
| Stated before any configuration / not retrofitted | 3A | 3F | removable in one place: **which one?** |
| The three charges glossed | 2B–2D | 3D gloss; 3B | removable |
| Refutation test | 2F | *"Stated positively…"* | removable in part: keep the same-currency form |
| **The four departures** (Qwen P1) | 3B | the 2E table, row by row | **primary target**: state them once and derive the condition |

### 2.3 Additions I made to my own first version, having reread both steps against it

- **2A must qualify:** *"It is not a claim about any particular aircraft, and nothing in it is new physics"*. It is not
  protected, but its substance must survive.
- **2D must qualify:** *"the least visible and often the largest"* is an unsourced comparative. Keep it as it is or drop
  it, but never strengthen it. The tail-sitter's one fifth is *"the ratio this expression gives"*, not a fit.
- **2F must say:** *"The moves in the table are partial remedies: each accepts the duty-cycle mismatch and then
  redistributes what it costs."* The question that follows is whether an architecture can **decline** the mismatch. **This
  is where the paper turns toward the contribution**, and 3A restates it.

  **Proposal: protect** *"Whether an architecture can decline the mismatch itself, rather than redistribute its
  consequences, is a different question"*. My reason: in a section of accounting, it is the sentence that carries the
  insight.
- **Outbound dependencies I had missed:**
  - **Step 4** quotes the tilting row (*"the actuation, the gyroscopic coupling and the transition control problem that
    Section 2 assigns to that family"*).
  - **Step 13** says *"the tilting family as Section 2 describes it has no store at all"*.
  - **Step 12** uses the store coupling (*"as Section 3 anticipated"*).
  - **Step 7** names the four parts of the condition in its own words. **So Qwen's P3 lock covers the four parts of 3C as
    well as the four failure modes of 3E.**
- **One correction to P3:** Step 15 does not cite Section 3 (searched). The citers are Steps 7, 8 and 9.

---

## 3. Three problems the inventory found in the source text

In Step 4, the inventory brought to light #18, a sentence the source itself had written too strongly. The same thing has
happened here, three times. **None of these is a drafting change**, and I am not proposing to settle any of them inside a
shortening pass.

**S-1. The mechanism rows of the table do not follow a single rule.**

- The table charges the **folding** mechanism to Bill 1 (*"1 — mechanism, actuation, locking, …"*).
- It charges the **pitch hub** to Bill 1 as well (*"1 — pitch hub, actuation, …"*).
- It places the **tilting** mechanism *"not among the three"*, yet 3B says that mechanism *"adds mass"*.

The text contains two possible rules, and the table follows neither of them:

| Rule | Where the text states it | Folding mechanism | Pitch hub | Tilt pivot | Odd row |
|---|---|---|---|---|---|
| **Duty cycle**: hardware needed briefly, carried for the rest | 2A's root | used at the transitions only → Bill 1 | retrims in both regimes → not Bill 1 | used at the transitions only → Bill 1 | **tilt** |
| **Lift-subsystem mass** | 2B; the 3D gloss; Step 11 (*"not lift-subsystem mass, so it is not Bill 1 as Section 2 defines it"*) | part of a dedicated lift group → Bill 1 | not part of one → not Bill 1 | not part of one → not Bill 1 | **pitch hub** |

**The paper already applies the second rule twice**, both times to energy storage, and both times it adds that the
excluded mass carries Bill 1's complaint:

- 3D, for the store: *"the same duty-cycle character as Bill 1"*.
- Step 11, for the buffer: *"which is the complaint Bill 1 makes"*.

A Q1 referee who reads the table closely can ask about this, and the question falls on the tilt axis, which is the axis
the contribution stands on. **I found it and I am not fixing it inside a shortening pass.** None of the options below has
been applied:

- **(a) Use the duty-cycle rule.** The tilt mechanism's mass goes to Bill 1. This reopens 2E's *"One row does not pay in
  any of the three currencies"*, 3B, and Step 4, which is being closed this round. Step 4 is affected in three places:
  *"The tilting family avoids it too"*, *"it moves the charge — to the mechanism"*, and #18.
- **(b) State a principle** for the current assignment.
- **(c) Use the lift-subsystem rule, as the paper already applies it.** The pitch hub's mass leaves Bill 1. The tilt row
  then says of its mechanism what 3D says of the store: the mechanism's mass has Bill 1's duty-cycle character, but it is
  not Bill 1. **This touches 2E only**: the pitch-hub row, *"One row…"*, and the tilt row. Step 4 stays as it is.

**My position:** (c). It applies the definition the paper already uses, not a new one, and I could not find a principle
for (b). Option (c) is not a concession we can avoid: the tilt row would then state openly that the mechanism's mass has
Bill 1's duty-cycle character. That makes the text more honest, not less. The claim against tilt remains the mechanism
class, not a mass. **Please test this:**

- Is (c) a rule chosen because it suits us? Would (a) be the more natural reading of 2A?
- Is there a principle for (b) that I have missed?
- Is there any predicate outside 2E that (c) changes?

**S-2. An antecedent in 3F is unclear.** The sentence is *"A tilting architecture accepts that departure and buys its way
out of the first with a mechanism."* Read naturally, *"the first"* is *the first departure*. The table, however, says the
tilting row attacks **Bill 1**. The draft must name one of the two, and that naming is an R sentence, open to veto. **My
reading:** *the first departure*, meaning different hardware. The mechanism is what lets one set of hardware serve both
regimes. Tell me if you read it differently.

**S-3. Step 12 says *"the separability Section 2 asserts"*.** What Section 2 actually says is narrower:

- It asserts three distinct **accounting** quantities.
- It says they are *"not assumed to be independent physical causes"*.
- It leaves to Section 12 the question of whether size moves them together.

*"Asserts separability"* may therefore say more than Section 2 does. Step 12 is not being drafted now; I record this so it
is not lost. **My proposal** is to change it to *"the distinctness Section 2 asserts"* when Step 12 is next opened.

---

## 4. What comes next

- **Next round:** the frozen snapshot of Steps 2–3, then the trace table with the qualification-lost column and the
  cross-step flag (DeepSeek, Qwen P2), then the draft, **block by block, beginning with 3B**. 3B is the primary target
  (Qwen P1). It is drafted first so that the largest restatement is tested first.
- **Blind reading first, as in Step 4.** Step 4 showed why it has to come first: one reading picked up numbers from the
  inventory.
- **No target percentage.** Grok: *"Plan them against 16 percent and against the restatement you already named."*

---

## 5. What I am asking

1. **Confirm the applied 3.1 and 3.2**, and confirm the 687 / 679 object check.
2. **The inventory:** confirm it, or add rows. In particular:
   - the restatement rule in 2.1;
   - which home keeps *"stated before any configuration / not retrofitted"*;
   - whether the Qwen P3 lock extends to the four parts of 3C.
3. **Vote** on protecting *"Whether an architecture can decline the mismatch itself, rather than redistribute its
   consequences, is a different question"*.
4. **S-1, S-2, S-3:** give your view, and criticise mine. **S-1 is the one that matters.**
5. **New proposals**, as always.

**Sources.** None of this needs a source. Everything quoted here is in the two step files, the table included.
