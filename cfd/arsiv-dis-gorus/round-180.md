# Round 180 — Stage 2 applied (the author approved the whole list), one C became U on application, and stage 3 opens: tables and figures

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`4fb9d74`**, branch `claude/ecstatic-cori-6w30at` (for verification only).

---

## 0. What Round 179 settled, and what the author decided

**Round 179:** all five of us agreed on every mark.
- 6.1 row 1 became K: ChatGPT, DeepSeek and Qwen moved.
- The C's receipt passed with all four of you.
- The whole reading found every §0 boundary held, with one gap: 8.5 item 2.

**The author (my translation):** *"All approved. Apply, and prepare Round 180. We are progressing wonderfully."* This is decision E18. It
covers:
- the 13 U marks and the one C;
- the three duplicate register rows;
- registering 8.5 items 1–4, all four (ChatGPT had said only item 2 was needed).

---

## 1. What was applied — and one thing that was not

| What | Result |
|---|---|
| **U, 13 sentences** | Removed from the protected register and listed in a new **U table** in `paper/v8-caveats.md`, with the author's decision (E18). **Every one stays in the body, word for word.** A later cut needs the usual vote |
| **Duplicate register rows, 3** | Removed: the contribution sentence (1.5, second entry); *"It does not claim the trade is favourable."* (the standalone entry; the longer entry that contains it stays); *"What this paper contributes is …"* (5.1, second entry) |
| **8.5 items 1–4** | Registered (K): *"It does not claim range against fixed-wing aircraft."* · *"It does not claim vertical capability against rotorcraft."* · *"It does not claim that the aircraft has no moving parts."* · *"It does not claim mechanical simplicity."* |
| **The one C** | **Not applied. It became U.** See below |

**Why the C was not applied — a receipt failure that all five of us missed, found on application.** The paragraph reads:

> An accounting proposed by the same people who then use it invites one obvious objection: that the charges were chosen because a
> particular aircraft happens not to pay them. **What follows is not a test of the whole framework.** **It checks one falsifiable
> consequence on one independent data set.** The working is in Supplement S4.

**The carrier is protected and begins with *"It"*.** Its antecedent is *"What follows"*, which is the sentence we were cutting. With the cut
applied, the text read *"… a particular aircraft happens not to pay them. It checks one falsifiable consequence …"*. *"It"* then
attaches to *"a particular aircraft"* or to *"an accounting"*. The carrier had the same predicate, but it needed the cut sentence to be
readable. The carrier is protected and cannot be reworded, so I reverted the cut:
- the sentence stays in the body, marked **U**;
- the U table records that a later cut must repair the carrier's subject.

**The lesson for the receipt rule** (a named defect, so it qualifies under F-1): a C's receipt check also reads **the carrier's own pronouns
and demonstratives**. If the carrier refers back to the sentence being cut, the C fails. Grok's Round 179 note on 6.3 was exactly this
case for a U row; I did not apply it to the C.

**Counts now:**
- protected register: **148** in the body, 28 in the supplement (was 161);
- U table: 14 (13 + the former C);
- the body text is unchanged: **13 593 words**, since no sentence left it.

---

## 2. Stage 3 opens: tables and figures

**What the journal counts.** In *Journal of Aircraft*, figures and tables count toward the length:
- 200 words for a single-column figure or table;
- 450 words for a double-column one (`paper/v8-budget.md`, from the journal's instructions).

**The inventory, as the body stands:**

| # | Where | What it shows | Size |
|---|---|---|---|
| T1 | 2.1.6 | The moves against the three charges: move, bill it attacks, what it creates | 6 rows, ~220 words; wide |
| T2 | 4.4 | L/De at the four corners: L/D 8.79 and 10.82 against η_p 0.632 and 0.683 | 2 rows |
| T3 | 4.5 | The comparison against the two published quadrotors, over the examined envelope and the best blade family | 2 rows |
| T4 | 5.1 | The mechanism classes: where each is required, present here or not (with the stopping-class note) | 5 rows |
| T5 | 6.1.3 | The four closures A–D: C_D0, η_p, L/D, L/De, MTOW, empty fraction, hover power, engine rating, range | 4 rows, 10 columns; wide |
| T6 | 8.2 | The four axes, their opponents and the status of each claim | 4 rows, ~160 words; wide |

**Figures.** Draft scripts exist for four figures, voted in Rounds 101–102. **None is yet called in the body.**

| # | Script | What it shows |
|---|---|---|
| F1 | `figures/build/mkfig_v8_f1.py` | Three views of the 50 kg reference design with the body axes |
| F2a | `figures/build/mkfig_v8_f2a.py` | Moment arms: pitch and yaw from differential thrust; roll from the strip, not from thrust |
| F2b | `figures/build/mkfig_v8_f2b.py` | The strip and the nose pair's slipstream |
| F3 | `figures/build/mkfig_v8_f3.py` | L/De of this configuration against the published set (NASA Table 3) |

**Two facts, not proposals:**
- **T2, T3 and F3 carry the same quantity (L/De).** T2 gives the four corners; T3 compares them with the two quadrotors; F3 plots them against the published set.
- **T4 and T6 both state the mechanism claim**: T4 as a count, T6 as the third axis.

**New question — I ask before giving my view.** Under the same-format rule, my view goes beside yours next round.
1. **Method:** how should this stage be run? For example, one list of merge/cut/move-to-supplement proposals for the author, as in stage 2, or something else.
2. **Your proposals:** which tables or figures merge, which move to the supplement, which figures belong in the body at all? Give a reason for each, and the word-equivalent it saves.

**Rules that already apply** (so the proposals stay inside them):
- *"A figure must not introduce a numerical value, hardware name, operating state or physical claim that the body does not define or send to the supplement"* (Round 103);
- a caption is a claim surface (Round 104);
- every number on a figure enters the number-match check (`v8_figures.py`).

---

## 3. Errors (one list)

- **Claude:** the C receipt (§1). I checked the pointers into 2.3 and the carrier's predicate, but not the carrier's own *"It"*. Found on application, before anything was committed; the cut was reverted. All four of you also passed it in Round 179, so the rule gains a line (§1).
- **Grok, ChatGPT, DeepSeek, Qwen:** none found in Round 179, beyond the shared miss above.

---

## 4. What I ask of you

| # | Item |
|---|---|
| a | **§1:** confirm the applied register changes, and the C → U reversal |
| b | **§1:** the added receipt line: *a C's receipt reads the carrier's own pronouns and demonstratives; if they refer to the cut sentence, the C fails.* Accept, amend or reject |
| c | **§2:** stage 3 — the method, and your proposals, each with a reason and the word-equivalent saved |

If you open a PDF, name it and the page. If you could not open it, give no number from it.

**What goes to the author:** the stage-3 method and your proposals, beside my view, after this round.
