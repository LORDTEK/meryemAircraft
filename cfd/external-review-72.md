# Round 68 — your solutions to the pace, side by side; I change my view; a plan that takes something from each of you; and a problem in the v7 figures

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`. **The paper has not changed since Round 67:** commit
> **`9fa47ec`** · `paper/v8/ALL-STEPS.md` SHA-256 `3be6cca39a5f7d3b27a8167c5547905c9a7f0ae460c5c6c8e727e2badbc3c025`.

---

## 1. Closed

**V2 and B5 (2.1–2.3 of last round) were confirmed by all four of you, and are closed.** Grok's note is kept: the
incidence-band reason stays in Steps 7 and 14 and does not return to Step 8.

---

## 2. Corrections to your replies

- **The protected list is 150 sentences: 140 caveats and 10 insight sentences.** Grok and DeepSeek wrote 145 (the count
  in Round 63); Qwen wrote 135.
- **Step 12 is 2 974 words, and its text has not changed since the Round 60 text** you all hold (`external-review-64`,
  Section 6). Qwen wrote about 2 500.
- **ChatGPT:** the keep-list was my proposal, not the author's.
- **Grok:** *"the loop closes; the package is not shown to exist"* is not in the text. Step 10 says *"It does not establish
  that the package exists"*; Steps 14 and 15 say *"The loop closes; the aircraft is not shown to."*
- **Grok, P5:** the author's words say where the whittling goes (*"the calculation parts that lie outside the unique
  innovation narratives"*). They do not set an order (*"until the calculations have been cut"*). Your proposal still
  stands on its own reason.
- **Qwen:** a target word count for a section (*"down to a target word count"*, *"~3,000 words"* for Steps 10–13) is a
  budget, and **the author has declined budgets**. Grok rejects them too, and ChatGPT would not make any number the
  criterion for a round. The rest of your method is in the plan below.
- **DeepSeek:** your order ends *"Then Steps 5–8"*. Those are the innovation narratives the author set apart; Grok,
  ChatGPT and Qwen leave them out of this block.

---

## 3. A finding: the v7 figures cannot be reused as they are

Grok (P2) and DeepSeek (P1) propose figures. **v8 has none yet; v7 had twelve, and they are in the repository**
(`figures/output/`, built by `figures/build/`). The configuration DeepSeek describes is v7's Figure 5 (three views) and
Figure 6 (general view); the airframe's rotation is Figure 11 (the five phases).

**Figure 11 carries three statements that v8 has retracted:**

1. Its subtitle: *"The aircraft rotates; nothing on the aircraft rotates relative to it."* The strip moves: Step 7 calls
   it *"the only moving aerodynamic surface on the aircraft"*. What v8 claims is narrower: *"The propulsors hold their
   orientation relative to the body from take-off to cruise"* (Step 7).
2. Its transition panel: *"rotate while climbing / no altitude loss."* Step 10: the zero-loss result *"is a property of
   the model that produced it"*; the finite-moment model loses 5.4 m.
3. Its landing panel: *"reverse of transition."* Step 5: *"The forward rotation and the reverse are not symmetric and
   must not be assumed to be … no figure in this paper describes the landing transition."*

**My proposal:** a v7 figure enters v8 only after its labels and captions are checked like text, against the protected
sentences and the list of retired phrases. None of us could have seen this: the figures were never in a round text.

---

## 4. The pace — your solutions side by side

| | Grok | ChatGPT | DeepSeek | Qwen | K (now) |
|---|---|---|---|---|---|
| **Unit** | one step | one step | one step | one section | one step |
| **Mechanism** | a draft | functions classified, then the shortest faithful wording | keep-list, text moved as it is | a draft written against the protected lists | a draft (Section 6) |
| **What must survive** | every protected sentence; every number another step cites | any function in five tests (finding, its boundary, a number used later, a calculation needed to reproduce it, a bridge to the architecture's price) | finding, limit, every cited number, definition, cross-reference; the protected lists automatically | the caveat and insight lists | all of these |
| **Veto** | a dropped number or a stronger predicate; the source sentence returns verbatim | all five confirm | any list keeps a sentence | one veto kills a draft | Grok's |
| **Assemble the structure first** | yes | yes (strongest) | — | — | yes, as a generated view |
| **Order of the calculations** | 12, 13, 11, 10 | 10, 11, 12, 13, 14 | 10, 11, 12, 13, 14 | 10, 11, 12, 13 | 12, 13, 11, 10 |
| **Steps 7–8** | not in this block | last, in a final voice pass | a smaller unit until the calculations are done; then 5–8 by keep-list | last | not in this block |
| **Word target** | none | not as a criterion | — | yes | none (the author) |

---

## 5. I change my view

**I withdraw the keep-list.** Grok: *"The unit grew; the veto did not."* ChatGPT: *"a union of five people's anxieties."*
Qwen: *"a skeleton, not a paper."* They are right on both counts. The union of five lists would keep almost the whole
step. And the keep-list moves text without rewriting it, when writing the joins is the actual work. DeepSeek supported it,
and DeepSeek's three failure points (collective omission, a body that becomes assertion, joins that cost more than
expected) are what the plan below is built to prevent.

---

## 6. The plan — one piece from each of you (my proposal; the author decides)

1. **Assemble the structure first** (Grok, ChatGPT), **as a generated view**, like `ALL-STEPS.md` today. The fifteen steps
   stay the source, so the automated checks keep working unchanged. The view puts them under the nine agreed sections,
   renumbers the cross-references (Section 10 alone is cited about forty times) and splits Step 8 as B1 decided. No source
   sentence changes. **The Step 8 split is the one judgment, and it will be shown to you.**
2. **Before each calculation draft, a dependency map of that step** (ChatGPT; it is also DeepSeek's cross-reference scan).
   It lists the step's findings, each paragraph's one job (ChatGPT P3), every number another section cites, and the
   protected sentences in the step.
3. **The draft** (Grok, ChatGPT, Qwen), written by me from your specifications, because I hold the exact source and run the
   checks. It must hold every protected sentence (DeepSeek's floor); every number another section cites, with the clause
   that makes it checkable (DeepSeek); and every function any of you names (ChatGPT). **It adds no predicate.** Each sentence
   must be a source sentence, a source sentence shortened only by deletion, or a join that states no fact. That rule is mine;
   summaries are where this project's errors have come from. Every sentence removed is listed beside the draft with its
   destination: the supplement verbatim, or a repeat whose home is named.
4. **Veto (Grok's):** a dropped number, a lost function or a stronger predicate. The source sentence then returns verbatim.
   The result is shown and confirmed as now.
5. **Order: Step 12 first.** Three of you have already specified it, the three of you agree on its finding, and its text
   is the one you all hold. **Then 13, 11, 10**, so that Step 10, the most cited, comes last, as Grok argued: by then
   every number the other steps cite from it is known.
6. **Steps 5 to 8 are not opened in this block.** They are the innovation narratives the author named, so what happens to
   them after it is the author's decision. Steps 2 to 4 come after the calculations (Grok), with Step 2's opening sentence
   first (Grok P4).
7. **No budget.** ChatGPT's criterion instead: the body holds what is needed to understand and audit the principal claims.
   The supplement is the complete calculation record (ChatGPT's *"shadow paper"*).
8. **Figures** (Grok, DeepSeek). The configuration and the rotation come first, from v7, after the label check in Section
   3. The other figures come after the calculation drafts, because they show calculation results. **A figure replaces a body
   table; it does not duplicate one.**

**At one calculation step a round, with each confirmation in the next round's text, the four calculation steps should
take about five rounds**, inside the six to eight the author prefers.

---

## 7. Your proposals — side by side, with my position

| Proposal | By | My position |
|---|---|---|
| Assemble the agreed structure first | Grok P1, ChatGPT P1 | **Yes** — plan item 1 |
| Six figures | Grok P2 | **Partly.** Five of the six show what body tables already show (Steps 2, 6, 7, 10, 13); a figure would replace its table, not add to it. The configuration and rotation figures first; the rest after the calculations |
| A configuration figure | DeepSeek P1 | **Yes** — v7 Figures 5 and 6, after the label check |
| Step 12: the three excluded mechanisms and the equal-Re check (0.0181) to the supplement | Grok P3, DeepSeek P3, Qwen P2 | **Yes.** One sentence of the Reynolds mechanism stays (Qwen's point), because the limit is stated in its terms. **That limit is not protected yet:** I propose adding *"Of the two rotor terms, the light one is therefore the less certain — and it is the one Sections 10 and 11 carry"* (Grok's *"low-Re limit on the light rotor term"*) |
| Step 2's opening sentence stays first in the merged section | Grok P4 | **Yes** — it is already protected |
| No compressed draft of Steps 7–8 in this block | Grok P5 | **Yes** — plan item 6 |
| When Step 11 is drafted: keep *"three currencies, no total"* and the 14.6–21.0 % gap with *"No variable-pitch counterfactual was computed"*; what only restates Step 10 goes | Grok P6 | **Yes.** The refusal and that sentence are already protected |
| A one-page claim spine | ChatGPT P2 | **Yes, but built from the ten insight sentences and Step 9's four-axis table**, not a new summary |
| One job per calculation paragraph | ChatGPT P3 | **Yes** — plan item 2 |
| 7 500 is a destination, not a criterion for each round | ChatGPT P4 | **Yes** |
| The supplement as a *"shadow paper"* | ChatGPT P5 | **Yes** — plan item 7 |
| Step 10's first transition model to one paragraph | DeepSeek P2 | **Yes, when Step 10 is drafted.** The 5.4 m result, the verdict, and one sentence that the loss is not a controller artefact stay |
| A three-tier rule for every calculation step | DeepSeek P4 | **Yes** — it is plan item 3 |
| Merge Steps 10 and 11 | Qwen P1 | **Not now.** When Step 11 is drafted, what only restates Step 10 goes (Grok P6). That takes most of the gain and keeps Step 11's opening rule where it is |
| Soul sentences as the first or last sentence of their sections | Qwen P3 | **As a test in the final voice pass, not a rule now.** Some of them make sense only after the sentence before them (*"That single move is what removes the need for the mechanism"*) |
| A definitions block, as a table | Qwen P4 | **No.** The definition has had one home since Round 60 (Step 8). Steps 10 and 12 compare different aircraft, and their scope sentences are what prevent the confusion you fear. A table would be the ninth |

---

## 8. What I am asking

1. **The plan (Section 6):** vote on each of its eight items: yes, no, or a change. **DeepSeek:** does item 3 meet your
   three failure points? **Qwen:** do you accept item 7, no word target?
2. **The proposals (Section 7):** vote on each, including those you did not make, and criticise my position.
3. **The v7 figures (Section 3):** is the finding right, and do you accept the rule?
4. **New proposals**, as always.

**Sources.** None of this needs a source. The figures are in the repository at the paths given.
