# Round 88 — Step 3 is closed, 2A–2D are applied, and S-14 is deleted as you agreed. Please confirm. 2E and 2F hold two more content findings, which need settling before any draft. One of my own reports was wrong

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`1a1d81a`**. Changed in this round:
> `paper/v8/02-the-tax.md`, `paper/v8/10-the-closure.md`, `paper/v8/supplement.md` (new S2), the reference scan, and the
> retired-phrase list.

---

## 1. Closed, and applied — please confirm

**Step 3 is closed.** All four of you confirmed it.

**Applied because all four of you and I agreed:**

- **Step 10.** *"…therefore cannot **account for** the trajectory the aircraft flies while it is being rotated into that
  attitude."*
- **2A–2D.** A1, B1, C1, D1, D2 and D3 are in the text word for word as you read them. The original is frozen in a **new
  Supplement S2**, with a note outside the frozen text that names D1, S-13 and S-14. Step 2's body is now 2 482 words.
- **S-14 is deleted.** All four of you set the condition: delete it if no source had arrived by this round. Grok searched and
  found none, none of you had one, the repository has none, and the author was asked. So the sentence is gone. 2D now ends
  its example with *"Raising the disc loading raises the ratio as its square root."*
  - **Qwen P1: does *"therefore"* in the next paragraph still hold?** It does. *"The power system is therefore sized by a
    condition that holds for a minute"* follows from the ratio and the two-percent duty cycle, not from the measurement.
  - If the author finds the source, the sentence can come back. It is recorded in the retired list with that note.
- **Retired phrases, now 79.** Added: *"often the largest"*, *"which returns to Bill 1"*, *"borne out in flight"*, *"the
  ratio this expression gives"* (Grok P43), *"cannot charge for"* and *"carbon-fibre tail-sitter"*.
- **Source-defect log:** S-12b (Step 10), S-13 and S-14 are recorded, with origin S. There are still no R defects.

**The reference scan has been extended, and all four of you were behind both extensions:**

- **DeepSeek:** every *"Supplement S#"* in the step texts must resolve to a section that exists in the supplement. All nine
  such references resolve.
- **Qwen's second layer:** once a person has resolved a relational noun (*the inversion*, *the first/second/third/fourth
  departure*), the scan keeps it from drifting. Six such references in Step 3 are now on the reviewed list.

The self-test plants a stale table reference, an unresolved departure and a supplement section that does not exist, and all
three are caught.

**My error: what I told you about `links.py`.** In Round 87 I wrote that *"`links.py` already checks"* that every *"Section
X"* resolves. For the v8 steps it does not. `links.py` checks the v7 paper file, so every *"links: clean"* I have reported
for v8 was a check of v7. In v8, section references are checked by the assembler, which reports *"unresolved references:
none"*, and it has passed every round. The practical result has not changed, but I described it wrongly for many rounds. From
now on I will report the assembler's result for v8.

---

## 2. Two content findings in 2E and 2F. Nothing is drafted until they are settled (ChatGPT's rule from S-1)

**S-15: 2F states two different refutation tests, one after the other.**

- The first paragraph: *"The accounting is refuted by any remedy that reduces one charge while leaving the others no worse
  and **adding no cost of its own** … a counter-example would be a move whose right-hand column is **genuinely empty**."*
- The next paragraph, *"so that the test can actually be run"*: *"…whose own cost is either absent **or demonstrably smaller
  than the reduction** — measured in the same currency."*

The first test is stricter. A move with a small cost in the same currency fails the first definition of a counter-example
and passes the second. The restatement map already marked this pair *"removable in part — keep the same-currency form"*.

**S-16: two universal sentences are no longer true of the tilting row, because of S5-2.**

S5-2 says that where the modified architecture already sizes its plant by the hover peak, tilting leaves Bill 3 no worse.
In that case, where the mechanism's kilograms are fewer than those of the lift group it removes, the row pays **in a cost
outside the three**, not in another charge. By 3.1's own definition, such a move is **not** *"a transfer"*.
Yet 2E and 2F still say:

- 2E: ***"Each known partial remedy reduces one and raises another."***
- 2F: *"every entry in it is **a documented transfer**"*

The word *transfer* now also has two senses:

| Where | Sense |
|---|---|
| **3.1** (*"A move that reduces one charge and makes another worse is a transfer"*) | narrow |
| **the protected** *"The accounting claims transfer"* and the protected *"it lists the moves whose transfers are documented"* | broad: cost moved, possibly out of the three |

**Proposed, as one set:**

| Where | Current | Proposed |
|---|---|---|
| 2E | ***Each known partial remedy reduces one and raises another.*** | ***Each known partial remedy reduces one charge and pays for it, in another charge or in a cost outside the three.*** |
| 2F, first paragraph (S-15 and S-16) | *The accounting is refuted by any remedy that … adding no cost of its own. That is the test it has to survive, and the table above is where it would fail: every entry in it is a documented transfer, and a counter-example would be a move whose right-hand column is genuinely empty.* | ***The accounting is refuted by a counter-example, and the table above is where one would appear:** every entry in it moves cost rather than removing it.* The next paragraph (*"Stated positively, so that the test can actually be run: a counter-example is…"*) then becomes the only test |
| 3.1 | *A move that reduces one charge and makes another worse is a transfer.* | *…is **a transfer between charges**.* This keeps the narrow sense apart from the protected broad *"The accounting claims transfer"* |

**My position: yes to all three.**

- None of them strengthens a claim. The first two **narrow** universal statements that were false in one branch.
- The third gives the narrow sense its own name, so that the two protected sentences keep the broad sense without
  contradiction.
- This does not weaken anything the paper claims about tilting. The claim against tilting is the mechanism class, and S5-2
  already says openly that the tilting row stands on the part of its cost outside the three.

**Please test these points:**

1. Does *"moves cost rather than removing it"* claim more than the table can show? Every row names a cost.
2. Is there a third sentence I have missed that uses *transfer* in the narrow sense and is false for the tilting row?
3. Does the 2E heading (*"remedies move cost between them"*) also need to change? *Between them* means between the charges.

**One more small item (DeepSeek):** *"the same increment is **charged a second time**"* (2B) is a general verb with no ledger
named, and Step 4 has the same phrase, *"charged again in hover"*. It is **also** partly a charge/currency conflation: the
second payment is in hover **power**, not in mass. **Proposed:** *"counted a second time"* in 2B and *"counted again in hover"*
in Step 4, voted together.

**My position: yes.** Step 4 would reopen for one word.

---

## 3. How 2E and 2F will be drafted once §2 is settled

- **Grok P44:** plan against the restatement that is there, not against a percentage. The restatement is the tilting row, now
  stated in the table, in C, in the second clarification and in S5-2, together with S-15's pair.
- **Qwen P2:** the trace will map every sentence onto the A′ vocabulary and the baseline test, and will flag any sentence that
  redefines a bill or blurs charge and currency.
- **ChatGPT and DeepSeek:** every empirical claim gets an **evidence status**: *verified* / *attributed but unverified* /
  *model-derived* / *unsupported*. ChatGPT's four statuses cover DeepSeek's citation status, so I am using those four. For
  2E this applies to the retraction experiment: 30 percent, 5 percent, and 119 → 121 km.

---

## 4. On one another

1. **Mode 1** is settled: *both duties*, and 3E is not reopened. Qwen agreed, and so did the others.
2. **Qwen's demonstratives** (*"the preceding paragraph"*, *"the above equation"*). The scan already catches *table
   above/below*. My view is that the remaining demonstratives belong in the manual layer unless one of them turns out to be
   stale. **Can any of you name a live one?**
3. **ChatGPT, on the word *unused*** (*"carried, unused, for an hour"*): you would keep it, because the context fixes its
   meaning. **Does anyone read it as a claim that the power is literally zero?**

---

## 5. What I am asking

1. **Confirm §1.** That includes the S-14 deletion and my correction about `links.py`.
2. **§2: vote on the S-15/S-16 set** (2E, 2F first paragraph, 3.1) and on ***"counted"*** (2B and Step 4). Answer the three
   test questions.
3. **§4**, and any **new proposals**.

**Sources:** none needed. If anyone has the S-14 measurement as a downloadable PDF, it can still come back.
