# Round 83 — 3.1 is applied and S-5 is closed. The work on 3B begins: a frozen snapshot, a draft for you to read blind, and then the trace. The trace also records one problem in the source text

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`.
> - Draft: `paper/v8/drafts/03-draft.md`. Only 3B differs from the source.
> - Snapshot: `paper/v8/drafts/03B-snapshot.md`, taken from the current Step 3, which already contains S5-4 (Grok P34).
>   It is 271 words; the first 16 hex characters of its SHA-256 are `4ca6fe342462244c`.
>
> **Please read §3 and answer it before you read §4.**

---

## 1. Closed

These items are confirmed by all four of you and by me:

- 3.2, the protected condition together with its clause;
- 3.3, *"is consistent with"* in Step 4;
- the S4 note.

Grok accepted the three-sentence form of 3.1 in both of its replies. ChatGPT, DeepSeek and Qwen accepted it as well.

**3.1 as applied (2F):**

> **"No worse" is judged against the architecture the move modifies.** A charge that architecture already paid, left no larger, is
> no worse. A charge it did not pay, imposed by the move, is worse; so is one it paid, enlarged by it. A move that reduces one
> charge and makes another worse is a transfer.

**Please confirm this last application. Once you do, S-5 is closed.** The checks all pass:

| Check | Result |
|---|---|
| Protected sentences | 156 |
| Retired phrases | 64 |
| Assembled view | 156 of 156 |

---

## 2. What to expect from 3B

**3B holds less repetition than we planned for, and I say so before you read the draft.** Qwen P1 (Round 77) named the
four departures as the main place to cut, because they restate the 2E table. Qwen's own P2 (Round 78), which we adopted,
then kept the two as separate views of the same thing: **2E is the accounting view, and 3B the architectural view.** The
tilting departure also sits on the axis the contribution stands on, and I left it untouched.

What remains removable in 3B is:

- one gloss of the charges, which the restatement rule removes;
- one relative word;
- a few words inside the parenthesis.

**The result is 271 → 247 words (−9 %).** That is below Step 4's −15 %. Grok warned about this: *"plan against 16 percent."*

---

## 3. Blind reading — please answer this before you read §4

**The draft of 3B:**

> ### Inverting the table
>
> **A charge appears wherever the two regimes are served by hardware that departs from one of four things: the same
> hardware, serving both duties, held in one orientation, with the hover peak supplied other than by its continuously
> installed power.** **Different hardware** costs Bills 1 and 2. **The same hardware serving only one duty** costs them
> again: a propulsor that lifts and is then carried is a dedicated lift group under another name, whatever it shares with the
> cruise system. **The same hardware serving both duties in a different orientation** is the tilting family: Bill 3 is
> incurred unless a store supplies the hover peak, and the mechanism that changes the orientation adds mass and introduces a
> control problem through the turn. **The same hardware, both duties, one orientation, but a different sizing point** incurs
> Bill 3 — unless the hover peak is supplied from somewhere other than the continuously installed power.
>
> Read one at a time, these are ways to pay. Read as a conjunction, they are a condition.
>
> *(The second departure is stated separately because it does real work later: a propulsor that produces a little thrust in
> cruise is not thereby serving both duties, and the distinction decides which parts of a configuration meet the condition
> and which do not. "Serving both duties" is the accurate form; hover thrust and cruise thrust are not the same **job** in any
> ordinary engineering sense — one supports weight, the other balances drag.)*

**Using only the draft above, reconstruct the following:**

1. The four departures, and the charge each one brings, **as a charge or as a cost in a currency** (the A′ vocabulary).
2. Where the **condition** comes from. Is it derived here, or only asserted?
3. Why the second departure is kept separate from the first.
4. **Relative vocabulary** (Qwen P2). Does any word imply a comparison with a baseline, such as *left standing*, *still*,
   *remains*, *survives* or *leaves*? 3B should read in absolute terms throughout.
5. **ChatGPT's test for "transfer".** The word does not appear in 3B, because departures are *ways to pay*, not *moves*.
   Does anything in the draft nevertheless read as a transfer, meaning one charge down and another up?

---

## 4. The trace — read this only after answering §3

Tags are **P** (protected), **D** (deletion only), **R** (rewrite, which you can veto one sentence at a time) and **J**
(joining sentence). Flags: **C** = charge, **$** = cost in a currency, **O** = outside the three.

| # | Source sentence (snapshot) | Tag | C / $ / O | Relative word | Qualification or epistemic status lost | Maps to 3C | Cross-step |
|---|---|---|---|---|---|---|---|
| 1 | *The charges exist **because** the two regimes are served by hardware that is not the same hardware, not serving both duties, and not held in one orientation.* | **R1** (merged with 2) | C | — | The causal *"because"* becomes *"wherever"*, a statement of co-occurrence. This is **weaker**, and it avoids setting a second origin beside 2A's *"the origin of all three charges"*. Three properties become **four** (see S-6) | parts 1–4 | 2A (root); A′ |
| 2 | *Depart from any one of those and a charge appears.* | R1 | C | — | The same universality (*"any one" → "wherever … one of four"*) | — | — |
| 3 | ***Different hardware** costs Bills 1 and 2: the unused set is carried for the whole flight and, if exposed, drags.* | **D** (the gloss after the colon goes) | C | — | None: the gloss restates 2B–2C, and the restatement rule removes it | part 1 | 2B, 2C |
| 4 | *The same hardware serving only one duty … whatever it shares with the cruise system.* | kept | C | *again* (its reference, Bills 1 and 2, is named) | — | part 2 | 3D bullet 4 repeats *"whatever else it shares with the cruise system"*. **3B is the home**; 3D's repetition is judged when 3D is drafted |
| 5 | *The same hardware serving both duties in a different orientation is the tilting family: … through the turn.* | kept | C (Bill 3); **$** (*adds mass* is in kg and is not Bill 1, per A′); **O** (control problem) | — | — | part 3 | 2E tilt row; S3 |
| 6 | *…a different sizing point **leaves** Bill 3 — unless …* | **R6** | C | **leaves → incurs**, the same repair as S5-4 | None | part 4 (3C narrows the peak's source to a store, and says so) | 3C |
| 7 | *Read one at a time, these are ways to pay. Read as a conjunction, they are a condition.* | kept, **load-bearing** (Qwen P1) | — | — | — | the derivation | 3A, 3C |
| 8 | *The second departure is stated separately **rather than folded into the first** because …* | **D** | — | — | The checker flags *"rather"*. The alternative is already implied by *"separately"*, so I judge nothing is lost. **Veto if you disagree** | part 2 | Steps 7 and 8 (tip pairs) |
| 9 | *"Serving both duties" is the accurate form; … **in any ordinary engineering sense** — one supports weight, the other balances drag — **and calling them one would be loose**.* | **D** (the final clause goes) | — | — | The checker flags *"would"*. The removed clause restates the first half of the sentence. **The hedge *"in any ordinary engineering sense"* is kept**, because deleting it would make the claim stronger | — | — |

**The deletion checker** (`v8_draft_check.py 3`) reports:

- It flags exactly the two expected **R** sentences (1+2, and 6) as not derivable by deletion.
- It flags the two deletions shown in rows 8 and 9.
- All protected sentences are present, and nothing else in Step 3 changed.

### S-6: the source's own miscount, which R1 repairs

The source's first sentence names **three** properties: the same hardware, both duties, one orientation. Its second sentence
says *"Depart from any one of **those**"*. Then the paragraph lists **four** departures. The fourth, a different sizing
point, departs from none of the three properties named. 3C then derives **four** parts, and says *"the fourth comes from the
fourth."* So the source has four departures but only three properties they depart from.

**R1 lists four.** Their wording follows 3C, except that the fourth is kept at the broader reading 3B uses, *"other than by
its continuously installed power"*. 3C narrows that to *a store*, and 3C says so itself.

**Is this a stop (Qwen P2)?** My view is that it is not. The problem sits inside 3B, and the R sentence that repairs it is
open to veto. S-1 was different: it involved the framework. **If any of you judge that S-6 reaches past 3B, the draft stops
here** and S-6 is carried forward on its own.

---

## 5. Proposals from Round 82

| Proposal | What I did |
|---|---|
| Grok P34: take the snapshot from the current Step 3 | Done |
| DeepSeek: add a baseline check to the pre-draft invariant (could the baseline already pay the raised charge?) | Added. The invariant is: row → modified architecture → raised charge, imposed or enlarged → cost → currency → bill or outside → where defined |
| DeepSeek: carry the "reduces one, raises another" test into the 3B trace | It does not apply. 3B lists ways to pay, not moves. It applies to 2E and 2F when they are drafted |
| ChatGPT: blind-read *transfer* explicitly | Question 5 in §3. It fully applies at 2E and 2F |
| Qwen P1: the pivot sentence is load-bearing | Adopted (row 7). **A small correction:** the source reads *"Read one at a time, these are ways to pay. Read as a conjunction, they are a condition."* Your quotation (*"Read downwards, the table is a list of ways to pay"*) is not in the text |
| Qwen P2: stop on findings instead of pushing on to the draft | Adopted. S-6 is the test case (§4) |

---

## 6. What I am asking

1. **Confirm that 3.1 is applied**, which closes S-5.
2. **§3: your blind reconstruction.** Give it first, before you have read the trace.
3. **Vote on each sentence:**
   - **R1** (rows 1 and 2);
   - **R6** (*incurs*);
   - **D3** (the gloss);
   - **D8** (*rather than folded into the first*);
   - **D9** (*and calling them one would be loose*).
4. **S-6:** does it stop the draft, or is R1 enough?
5. **New proposals.**

**Sources:** none needed.
