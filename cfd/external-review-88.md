# Round 84 — 3B is applied, please confirm. S-5 is closed. The next two blocks, 3A and 3C, go to blind reading, and 3C turned up a broken reference in the source

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`9b2b62f`**.
> - Draft: `paper/v8/drafts/03-draft.md` (only 3A and 3C differ from the source).
> - Snapshot: `paper/v8/drafts/03AC-snapshot.md`.
>
> **Please read and answer §4 before you read §5.**

---

## 1. Closed

**S-5 is closed.** All four of you confirmed 3.1 as applied, and so did I.

---

## 2. 3B is applied — please confirm

All four of you and I accepted R1, R6, D3, D8 and D9, and the blind reading passed in all four replies. **The text now in
Step 3 is the draft you read, word for word.**

- **Words:** 271 → 247.
- **Supplement:** the original 3B is frozen in Supplement S3 as *"'Inverting the table' as it stood before recomposition (frozen
  snapshot)"*, which follows the rule that anything recomposed goes to the supplement whole.
- **Record in the step:** R1 is recorded as **a substantive repair of the source's miscount**, not a stylistic change
  (ChatGPT B).

**Checks after applying:**

- **Retired phrases** (DeepSeek: *"so that the miscount is not reintroduced"*). Two more are on the list, which is now at 66:
  *"The charges exist because the two regimes"* and *"sizing point leaves Bill 3"*.
- **The nothing-lost check now covers Step 3.**
- **The "again" flag** (DeepSeek) is recorded in the trace.

**My error in the checking tool.** When Step 3 was added to the nothing-lost check, it reported a loss in 3D, a block we had
not touched. The cause was in the tool: it stripped the bullet marks from the old text but not from the current text, so any
paragraph that runs into a bulleted list looked lost. I fixed it and tested it both ways:

- the tool's self-test still catches a deleted sentence;
- when I removed the 3B snapshot from the supplement, it reported exactly the five changed sentences.

The bug could only raise false alarms. It could never let a real loss pass, and the earlier runs raised no alarms.

---

## 3. Two decisions carried over

**3.1 Protect the pivot (Grok P35, ChatGPT D)**, the sentence *"Read one at a time, these are ways to pay. Read as a
conjunction, they are a condition."*

- In Round 82, Qwen said it is load-bearing but does not need protection.
- DeepSeek has not voted.
- **My position: protect it.** It is where the conjunction is derived; without it, 3C reads as an assertion.

**Qwen, DeepSeek:** your votes are the ones missing.

**3.2 The four departures of 3B mapped to the four parts of 3C** (ChatGPT C, DeepSeek, Grok P36, Qwen P2):

| 3B, R1 | 3C, *"Four parts"* | |
|---|---|---|
| the same hardware | same hardware | one to one |
| serving both duties | both duties | one to one |
| held in one orientation | one orientation | one to one |
| hover peak supplied other than by its continuously installed power | hover peak **from a store** | **3C is narrower, and says so** (*"a store is the narrower reading used here"*). It is marked as **narrower** in the trace, not as a restatement, so no later draft may "align" the two |

**All four map one to one.** S-6 is therefore closed by R1 at the level of the architecture as well as the count.

---

## 4. Blind reading of 3A and 3C — please answer this before §5

**3A (draft):**

> ## The escape condition
>
> This section asks what an architecture would have to do in order not to incur the three charges at all. The answer is a
> **definition**, derived by inverting the table, and it is stated here before any configuration is offered so that the
> standard is not taken from the thing it will be used to measure.

**3C (draft):**

> ### The condition
>
> > **An architecture does not incur the three charges if the propulsors that carry the weight, held in one orientation
> > relative to the airframe, produce both the hover thrust and the cruise thrust, and if the difference between the hover
> > peak and the cruise demand is supplied from a store rather than from permanently installed continuous power.**
>
> Four parts: **same hardware, both duties, one orientation, hover peak from a store.** The first three come from the first
> three departures; the fourth comes from the fourth.
>
> Two things in that sentence are choices rather than derivations. The inversion requires only *one orientation relative to
> the airframe*; **how** an architecture keeps that while changing flight regime — by rotating the whole body, or otherwise —
> is not in the inversion, and is treated as exposition rather than as part of the definition. And the fourth departure's
> exception lets the peak come from **any** source other than the continuously installed power; a store is the narrower
> reading used here, because it is what the configuration examined later uses and because a narrower condition is easier to
> fail.

**Reconstruct, using only the two drafts above:**

1. **3A:**
   - What does the section ask?
   - What is the answer's status (definition, result, or law)?
   - What is it derived from?
   - Why is it stated before any configuration?
2. **3C:**
   - What are the four parts?
   - Which two things are choices rather than derivations, and why is each one a choice?
3. **References.** What do *"the table"* (3A), *"the inversion"* and *"the fourth departure's exception"* (3C) each point to? Can
   you find each one without leaving Sections 2–3?
4. **Relative words and classification (Qwen P1).** Does any word imply a baseline? Does any cost go unclassified?

---

## 5. The trace — read only after answering §4

| # | Source (snapshot) | Tag | Why | Qualification / epistemic status lost | Cross-step |
|---|---|---|---|---|---|
| A1 | *The previous section listed moves that redistribute the three charges.* | **removed** | This repeats 2F. 2F is the agreed home of *decline vs redistribute*: *"The moves in the table are partial remedies: each accepts the duty-cycle mismatch and then redistributes what it costs"* and the protected *"Whether an architecture can decline the mismatch itself … is a different question"* | none; 2F carries it | 2F |
| A2 | *This one asks a different question: what would an architecture have to do in order not to incur **them** at all?* | **R** | Removing A1 would leave *"them"* with nothing to refer to, so R names *"the three charges"*. *"A different question"* goes, because its contrast now sits in 2F's protected sentence | none; the scope is the same (*"not … at all"*) | — |
| A3 | *…derived by inverting the table **rather than by describing any aircraft**, and it is stated here before any configuration…* | **D** | This is the restatement map's *"derived from the table, not from an aircraft"*, and its home is 2F: *"derived from the table above rather than from any aircraft"*. The checker flags *"rather"* | Nothing is lost: 2F keeps the negation, and the same sentence keeps *"so that the standard is not taken from the thing it will be used to measure."* **3A stays the home of *"stated before any configuration"*** (agreed in Round 78) | 2F; 3F (its repetition is judged when 3F is drafted) |
| C1 | the condition | **P** | — | — | Steps 7, 8, 14 |
| C2 | *Four parts: …* | kept, **locked** (Qwen P3) | — | — | Step 7 |
| C3 | *Two things in that sentence are choices rather than derivations, **and are marked as such**.* | **D** | The sentence itself is the marking | none | — |
| C4 | ***The table** requires only one orientation …; how … is not in **the table**, and …* | **R** | **S-7**, below | none | 3B |
| C5 | *And **the table's last row** permits the peak to come from any source …* | **R** | **S-7**, below. The narrowing to a store stays explicit (Grok P36, Qwen P2) | none | 3B R1; 3C part 4 |

**Words:** 3A 77 → 60 (−22 %); 3C 196 → 190. The checker flags exactly the three R sentences (A2, C4, C5) and the *"rather"*
in A3. All protected sentences are present.

### S-7: a reference in the source that has been broken since Round 64

In Round 64, 3B's table moved to Supplement S3 (*"The departures as a table (from Section 3)"*). The body kept two references
to it in 3C: *"The table requires only one orientation"* and *"the table's last row permits the peak…"*.

In the body, *"the table"* now points to **2E's** table. Neither reference fits it:

- 2E's table has no *"one orientation"* requirement;
- the last row of 2E's table is *"Lower disc loading, larger rotors"*, not the source of the peak.

**The two R sentences point the references back at 3B:** *"the inversion"* (the heading of 3B is *Inverting the table*) and
*"the fourth departure's exception"* (the *"unless…"* clause of 3B's fourth departure).

**Stop rule:** this counts as **one** broken reference, found and repaired within the round, so under the rule we agreed it
is counted and the work continues. If you see a second one, the work stops.

A search of Step 3 for any other stale reference to "table" or "row" found none.

---

## 6. What I am asking

1. **Confirm 3B as applied**, including the fix to the checking tool.
2. **3.1:** Qwen and DeepSeek, vote on protecting the pivot.
3. **§4, the blind reading:** answer it first.
4. **Vote on A1, A2, A3, C3, C4 and C5, one by one.**
5. **S-7:** is the repair right? Is there a second broken reference?
6. **New proposals.**

**Sources:** none are needed.
