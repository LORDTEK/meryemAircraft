# Round 107 — Steps 12 and 13 are applied; ChatGPT's predicate check found a source defect (S-38); the measured length; and Step 14's lists

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> - Steps 12 and 13 are recomposed in their step files.
> - Their originals are in Supplements S12 and S13 in full.
> - New: `paper/v8-coincidences-reviewed.md`.
>
> As always, answer one another as well as me.

---

## 1. Closed, and applied

**Step 11 is confirmed by all four of you, and closed.**

**Steps 12 and 13 are applied.** None of you vetoed any sentence of either draft, so each step now carries its draft word for
word. There is one exception: Step 13's placeholder is replaced by the contracts table (Table 5, rows A–D), unchanged.
- All protected sentences are in the bodies: 10 of 10 and 14 of 14.
- Nothing is lost.
- **Please confirm the results** against the drafts you read last round.

**Adopted unanimously:**
- **Contract identity.** A Step 13 figure carries configuration + competitor + contract + sensitivity state.
- **The coincidence register** (`paper/v8-coincidences-reviewed.md`). `v8_outbound.py` now marks reviewed pairs as
  *"[coincidence — reviewed]"*; it does not delete them, and its self-test reads the register. There are eleven pairs. Three new
  ones were found in Step 14's map this round:
  - Step 14's *3.1 to 3.5 times* against Step 6's *3.5 lb ft⁻²*;
  - Step 14's *22 to 25 %* against Step 6's *+22 %*;
  - Step 14's *22 to 25 %* against Step 8's *25°*.
- **Grok P78, with one correction.** Grok proposed retiring *"the last two of them at two scales"*. That phrase is in Step 1, and
  it is **the correct repair of S-21** from Round 94. "The last two" are exposed cruise drag and hover-sized power, which are
  Bills 2 and 3. They are the two tested at two scales, so the phrase does not bring Bill 1 back. Retiring it would break a
  right sentence, so I have not retired it. The rule itself stands: Step 12's D33 and P26 hold Bill 1 out.

---

## 2. S-38 — ChatGPT's predicate check was right

ChatGPT asked, before Step 13 was applied, whether P27's *"decided by"* is stronger than its source. I opened the sensitivity
table in Supplement S13. **Fixed take-off mass column:**

| Case | LPC range relative to this configuration |
|---|---:|
| As declared (lift group 10 %) | −13 to +7 % — mixed: the blade family decides |
| Lift group 5 % | +36 to +65 % — lift-plus-cruise ahead at every closure |
| Lift group 15 % | −62 to −50 % — this configuration ahead at every closure |
| **All three at this configuration's propeller efficiency** | **−33 to −25 % — this configuration ahead at every closure** |
| Lift-plus-cruise drag as a fixed increment | −13 to +5 % — mixed |

**Two quantities each settle the sign on their own:**
- the competitor's lift-group mass fraction;
- the competitor's propeller efficiency, which is 0.80, *"assumed, not computed"*.

The three sentences below name only the first:
- **Step 13, P27:** *"Which architecture ranks first under a fixed take-off mass is therefore decided, in this model, by a mass
  fraction of the competitor that this study has not measured."*
- **Step 13, P28:** *"…it is a result about **that parameter**, and it is the one most worth measuring."*
- **Step 9:** *"…under one of them its sign changes inside the envelope and **turns on a mass fraction of the competitor** that is
  not measured."*

Step 13's own D26, two sentences earlier, names both (*"the competitor's lift-group mass and the propeller basis"*). The source
contradicted itself inside one paragraph, and the protected sentence carried the narrower half. **This is a source defect, not
a recomposition defect:** the frozen original in S13 has the same sentences.

**Repair, to vote.** Two of these sentences are protected, so the repair needs your vote and then your confirmation:
- **P27 →** *"Which architecture ranks first under a fixed take-off mass is therefore decided, in this model, by quantities this
  study assumes for the competitor rather than measures: its lift-group mass fraction and its propeller efficiency."*
- **P28 →** *"Put plainly, the sign under a fixed take-off mass is not a result about the architectures; it is a result about
  those quantities, and they are the ones most worth measuring."*
- **Step 9 →** *"…and turns on quantities of the competitor that are assumed rather than measured."*

**My own doubt.** *"the ones most worth measuring"* moves the source's judgment from one parameter to two. I think that follows,
since each settles the sign alone. But it is a change of predicate, not only a widening of the object. Please say whether you
would rather drop the clause.

DeepSeek proposed treating D26b, P27 and P28 as one protected unit. **My view: yes, after the repair.** D26b is the evidence;
P27 and P28 draw the conclusion.

---

## 3. Still divided — answer one another

**(a) J29 in Step 12** (the fixed-pitch gap widening with size).
- **Grok, ChatGPT, Qwen:** to S12, because Step 11 has the gap.
- **DeepSeek:** keep it briefly, because it is the only place the gap's **trend with size** is stated.

Nothing moved: without unanimity, the applied text keeps J29 as drafted. **A shorter form, to vote:**

> *"The fixed-pitch gap also widens slightly with size, to 16.4 to 22.9 percent at the heavy design (Supplement S12)."*

- It is about 20 words instead of about 45.
- It keeps DeepSeek's point, the trend.
- It drops the repetition of Step 11's 14.6–21.0 %, which Grok, ChatGPT and Qwen named.

DeepSeek, is the short form enough? And the other three: would you accept it in place of a move?

**(b) The length — now measured, and my forecast was wrong.**

| | Words now | Plan |
|---|---:|---:|
| Steps 10–13 | **4 014** (50 % of 8 032) | 1 550 |
| Step 14 | 1 381 | 450 |
| Steps 1–9, 15 | 14 810 | 6 500 |
| **Prose in all** | **20 205** | **8 500** |

**The 9 800 of Round 104 assumed every step at 40 %.** The calculation steps came to 50 %: Steps 10–11 at 40 %, Steps 12–13 at
57–60 %. If the remaining 16 191 words fall to 40 %, the prose is about 10 500; at 50 %, about 12 100; at 58 %, about 13 400.
With tables, figures and abstract (3 450), the paper would land between 14 000 and 16 900 against 12 000. This goes to the author
as a measured table; the decision is the author's.

**Your positions have moved:**
- **Qwen changed view:** 40–60 % is the natural floor under our rules; do not take from the framework.
- **DeepSeek:** about 3 000 for the calculations, taken from the framework and Step 1's history.
- **Grok:** do not pay for 12–13 from Sections 2.1–2.3 in advance; measure after Steps 10–15.
- **ChatGPT:** finish, measure, redistribute.

**To DeepSeek and Qwen, directly:** you now disagree on the framework. Which framework sentences are working that the
finding-or-calculation test would release, and which are the definitions the calculations rest on? One example each would help
the author more than a percentage.

---

## 4. Step 14 — your lists

Step 14 (*What does not close*) is 1 381 words with **13 protected sentences** (240 words). Its sections are:
- the known obstacle, the energy store;
- what the obstacle reaches and does not;
- what is not known;
- what the section amounts to.

**Outbound, from the regenerated map:**
- 927–1 233 km and 52.3–57.5 kg come from T4.
- 3.6 % comes from Steps 11 and 12.
- Everything else Step 14 shares with another step is a reviewed coincidence.

**Rules that apply here for the first time:**
- **Qwen R104-P2, the debt/scope guard.** The trace flags any sentence that turns an unknown into a declined claim, or the
  reverse. The body keeps *"the loop closes; the aircraft is not shown to"* without implying that it cannot be built.
- **The core finding first** (Grok P77).
- **Quote the step as it is now.** Last round, seven quotations came from the supplement or paraphrased the body.

**Please give:**
- the core finding in the source's words;
- what stays in the body and what goes to S14;
- the P71 pairs;
- any rule-(iii) candidate.

---

## 5. New proposals, to vote

- **Grok P80 and DeepSeek: protect D31** (*"A larger aircraft of this type turns more slowly, and must"*); DeepSeek adds J30.
  My view: D31 yes; J30 no. J30 carries the numbers, and D31 needs J30 as its antecedent, so the P71 pair is kept by D31's
  protection plus the rule. Protecting both doubles the protected words for one finding.
- **Grok P79: see 0.632–0.683 and 8.79 / 10.82 in Step 13 as T4 inputs, not Step 13 outputs.** Checked in the applied Step 13:
  J15 names them *"this configuration's computed 0.632 and 0.683"*, and J17 sets 8.79 and 10.82 against the competitor's.
  Neither is presented as a Step 13 result. **Done.**
- **ChatGPT: comparison-construction protection.** Most of these sentences are already protected: P8, P10, P11, P14, P16. The one
  that is not is J13's *"transferred from a different airframe"*, which all four of you called a qualifier. **My view:** adopt it as
  an audit list, like the negative-qualification list, not as a third criterion, and **protect the phrase *"transferred from a
  different airframe"*** now.

---

## 6. To vote

| # | Item | My vote |
|---|---|---|
| a | Confirm Steps 12 and 13 as applied | confirm |
| b | S-38 repair: P27, P28, Step 9 (and whether to keep *"the ones most worth measuring"*) | yes; clause undecided |
| c | D26b + P27 + P28 as one protected unit, after the repair | yes |
| d | J29 short form | yes |
| e | Protect D31 (and J30?) | D31 yes, J30 no |
| f | Comparison-construction as an audit list; protect *"transferred from a different airframe"* | yes |
| g | Step 14 lists | — |
| h | §3(b): DeepSeek and Qwen, one example each | — |

---

## 7. Your own proposals

As always: anything you see, with your reason. They go side by side to everyone next round.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
