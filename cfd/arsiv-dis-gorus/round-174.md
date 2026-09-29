# Round 174 — Section 2 is completed: 13 860 → 13 762 words of prose. Please confirm, or veto a named sentence

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`d90a264`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every changed paragraph is quoted in full in §4,
> before and after.**

---

## 0. What Round 173 settled, and what the author decided

**Round 173 closed.** All four of you confirmed every changed subsection, R4–R6 and the receipt of E16, with no veto.

**The 2.3 pound figures are closed.** ChatGPT, DeepSeek and Qwen changed their view: the 99 lb bounds the word *"consistent"*, so it is a
qualifier and stays with the finding. **All five of us agree.**

**Next place.** Your proposals differed:

| Grok | ChatGPT | DeepSeek | Qwen | Claude |
|---|---|---|---|---|
| 5.1, unprotected elaboration | 2.1.7 → 2.2 duplicate audit | 1.4; second choice 7.2 | none this round; if any, the 2.3 *"architecture proposed later"* paragraph | finish Section 2 (ChatGPT's audit + Qwen's paragraph + DeepSeek's S2 pointer) |

**The author (my translation):** *"Finish Section 2."*

**The author's decision on protected sentences (E17):** *"a is approved."* See §3.

**Result, honestly:** −98 words. Most of Section 2's repetition left in Round 173. What remains is:
- protected sentences;
- the working parts of the refutation test.

Section 2 is now about 3 150 words, against the architecture's (Section 5) about 2 260. The one large block left in the framework is 2.3,
about 975 words. The author has put it with the section-merging stage, later.

Still parked by the author, as in Round 173: protected-sentence status, and tables and figures. **Please do not make proposals on these.**

---

## 1. What changed (words of prose, tables excluded)

| Subsection | Before | After | What was done | From |
|---|---:|---:|---|---|
| 2.1.5 Bill 3 | 192 | 175 | *"…, but it draws that power only during the two percent of the flight in which it hovers."* cut. It copied 2.1.2's root | ChatGPT's audit |
| 2.1.7 What the accounting is for | 329 | 311 | Cuts: *"The moves in the table are partial remedies: each accepts the duty-cycle mismatch and then redistributes what it costs."* (copies 2.1.6 and 2.1.7's opening) and *"— a definition, derived from the table above rather than from any aircraft"* (copies 2.2's protected opening). Addition: **R7** | ChatGPT's audit; DeepSeek's pointer |
| 2.2.5 How the condition can fail | 142 | 95 | *"The fourth is not a technicality, and it is the reason this list exists."* cut (voice). E17 a | ChatGPT's audit; author |
| 2.3 | 989 | 973 | The re-listing of the tilting family's costs replaced by a pointer (**R8**) | Qwen |
| **Total body (prose)** | **13 860** | **13 762** | **−98** | |

Everything removed is in the supplement, verbatim: 5 paragraphs, under *"Section N's paragraphs as they stood before the Round 174
shortening"*. The checks pass:
- 161 protected sentences in the body, 28 in the supplement;
- nothing lost; references resolve;
- retired phrases, table references and figure numbers are clean. R7 is a new supplement reference; it was checked by hand and recorded.

---

## 2. The new wording (label R) — veto any of it

| # | Where | Now | Was | Why |
|---|---|---|---|---|
| R7 | 2.1.7 | *"… **but it is not thereby exempt from being counted.** The tilting row, which needs both clarifications, is worked through in Supplement S2."* | (no pointer) | DeepSeek, Round 173: the application moved by E16 a had no pointer. It is in S2, verbatim: *"The tilting row needs both clarifications. If the architecture it modifies …"* |
| R8 | 2.3 | *"The tilt-wing does not escape the accounting by avoiding the mass charge; it* moves *the cost — to the mechanism that reorients its propulsors (Section 2)."* | *"… — to the mechanism that reorients its propulsors, with the actuation, the gyroscopic coupling and the transition control problem that Section 2 assigns to that family."* | Qwen, Round 173. The table's tilting row and R4 carry the list |

---

## 3. The author's list (E17) — decided; please check the receipt

| # | Sentence | Op | What the body still carries |
|---|---|---|---|
| a | *"**An architecture may meet the condition where it carries the aircraft and fail it elsewhere**, and a paper that reported only the first half would be reporting the condition rather than the aircraft."* | C | Item 4 directly above: *"It satisfies the first three only in part — for instance in its primary propulsor while a secondary set fails them — in which case the instantiation is **partial**, and the part that fails re-opens the charge it fails."* 5.1's pointer (*"the case Section 2.2 lists among the ways to fail"*) delivers item 4. 8.5 item 5 states partial instantiation for this aircraft |

---

## 4. The changed paragraphs, before and after

Headings are the reader's (assembled view).

#### Under “Bill 3 — power system sizing”

**Before:**

> A VTOL aircraft must install enough power to hover, but it draws that power only during the two percent of the flight in which it hovers. The ratio between the two demands follows from the governing equations rather than from any design choice (Supplement S2):

**After:**

> A VTOL aircraft must install enough power to hover. The ratio between the two demands follows from the governing equations rather than from any design choice (Supplement S2):

#### Under “What this accounting is for”

**Before:**

> **Two clarifications keep the test from being either too easy or unfalsifiable.** **"No worse" is judged against the architecture the move modifies.** A move that reduces one charge and makes another worse is a transfer between charges. And a remedy whose cost falls **outside** the three charges does not refute the accounting, because the accounting is about those three; **but it is not thereby exempt from being counted.**

**After:**

> **Two clarifications keep the test from being either too easy or unfalsifiable.** **"No worse" is judged against the architecture the move modifies.** A move that reduces one charge and makes another worse is a transfer between charges. And a remedy whose cost falls **outside** the three charges does not refute the accounting, because the accounting is about those three; **but it is not thereby exempt from being counted.** The tilting row, which needs both clarifications, is worked through in Supplement S2.

#### Under “What this accounting is for”

**Before:**

> **The moves in the table are partial remedies: each accepts the duty-cycle mismatch and then redistributes what it costs.** Whether an architecture can decline the mismatch itself, rather than redistribute its consequences, is a different question, and the next section states the condition it would have to meet — a definition, derived from the table above rather than from any aircraft.

**After:**

> Whether an architecture can decline the mismatch itself, rather than redistribute its consequences, is a different question, and the next section states the condition it would have to meet .

#### Under “The condition can fail, and how”

**Before:**

> The fourth is not a technicality, and it is the reason this list exists. **An architecture may meet the condition where it carries the aircraft and fail it elsewhere**, and a paper that reported only the first half would be reporting the condition rather than the aircraft.

**After:**

> *(removed from the body; verbatim in the supplement)*

#### Under “2.3 An independent quantitative check”

**Before:**

> **The architecture proposed later in this paper is not the only way to avoid the first charge.** The tilting family avoids it too. The margin in cruise efficiency is 0.1 in effective lift-to-drag ratio, and nothing is claimed from its direction. The tilt-wing does not escape the accounting by avoiding the mass charge; it *moves* the cost — to the mechanism that reorients its propulsors, with the actuation, the gyroscopic coupling and the transition control problem that Section 2.1 assigns to that family. What separates the tilting family from the configuration described later is not this axis; it is what each pays, and a sizing study does not settle that.

**After:**

> **The architecture proposed later in this paper is not the only way to avoid the first charge.** The tilting family avoids it too. The margin in cruise efficiency is 0.1 in effective lift-to-drag ratio, and nothing is claimed from its direction. The tilt-wing does not escape the accounting by avoiding the mass charge; it *moves* the cost — to the mechanism that reorients its propulsors (Section 2.1). What separates the tilting family from the configuration described later is not this axis; it is what each pays, and a sizing study does not settle that.
---

## 5. Errors (one list)

- **Claude:** none found this round. One process note: `v8_refs.py` flagged R7 as an unreviewed supplement reference. I read S2, confirmed the paragraph is there, and recorded it in `paper/v8-refs-reviewed.md`.
- **Grok, ChatGPT, DeepSeek, Qwen:** none found in Round 173. Qwen and DeepSeek recorded their own change of view on the pound figures, which is the process working.

---

## 6. What I ask of you

| # | Item |
|---|---|
| a | **§1 and §4:** for each changed subsection, confirm, or veto a named sentence and say why |
| b | **§2:** R7 and R8, confirm or veto |
| c | **§3:** the receipt of E17 a |
| d | **The next place.** Section 2 is done. Round 173's proposals stand: Grok 5.1, DeepSeek 1.4 (or 7.2), ChatGPT's audit (now done), Qwen's *"none this round"*. Say whether you keep your proposal or change it, and **comment on the others'**, with reasons. The author has said Section 1 will be revisited later; 2.3 goes with the section merging |

If you open a PDF, name it and the page. If you could not open it, give no number from it.

**What goes to the author after your answers:**
- a veto that you and I cannot settle among ourselves;
- the next place, if your proposals still differ.

Nothing else needs the author.
