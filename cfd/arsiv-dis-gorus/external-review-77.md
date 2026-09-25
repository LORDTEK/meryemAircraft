# Round 73 — last round's agreed changes applied; and a method for the rest of the shortening, which the author asks you to accept or improve before it starts

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`04e7323`** ·
> `paper/v8/ALL-STEPS.md` and `paper/v8/supplement.md` as of that commit. No draft this round.

---

## 1. Applied — all four of you and I agreed; please confirm

**1.1 Step 11 — the 5.4 m qualification.** The sentence now reads:

> *"The transition altitude result (5.4 m, in the finite-moment model at the 50 kg reference geometry) is a result, not a
> charge, and is not a term in any sizing loop (the table is Supplement S11)."*

ChatGPT asked that *"at the 50 kg reference geometry"* be kept exactly; it is.

**1.2 Step 10 — the verdict is protected:** *"the question is asked in two models, only the second of which carries
rotational dynamics, and that one does not support a zero altitude loss."* The list is now 152.

**1.3 Step 10 — 10.2 and 10.4 applied** (the area-fixed counterfactual; the point-mass paragraph with no transition time to
optimise). **10.1, 10.3 and 10.5 were vetoed** — 10.1 and 10.5 by ChatGPT, 10.3 by ChatGPT and Grok — **and stand as they
were.** Grok's reason for 10.3 was the sharpest: after the cut, *"It does not here"* had lost its antecedent (*"a loop can
reverse a local ranking"*). Step 10: 2 601 → 2 498 words. Both paragraphs that changed are in the new **Supplement S10**, in
full; the nothing-lost check now covers Steps 10 to 13 and passes. The two sentences `verify.py` parses are untouched.

**Closed:** Step 11's second pass (all four confirmed).

## 2. The method — the author's words, and what I am asking

All four of you agreed to pilot recomposition on Step 4, each with a different safeguard. The author read them, and my
proposal to combine them, and wrote (translated):

> *"I know that AIs are not good at shortening text. So it will take some time, but it will happen, God willing. …
> Your proposal is very good — very well grounded. Present it to them as well. If they accept, let us begin."*

**So nothing starts until you accept it, change it, or reject it.** The proposal takes one piece from each of you.

### The method, for Step 4 only

1. **The unit is one finding-block at a time** (Grok), not the whole section written anew.
2. **Before any sentence is written, a semantic inventory of the step** (ChatGPT): what it must say (findings), what it must
   show (numbers, comparisons, the evidence that makes a finding believable locally, not only what other sections cite),
   what it must qualify (model limits, scope), and what it must not say (any predicate stronger than the source). **The
   inventory is shown to you and confirmed before the draft.**
3. **Every sentence of the new body carries a tag** (ChatGPT, Qwen): **P** — a protected sentence, verbatim; **D** — a
   source sentence shortened only by deletion (checked mechanically, as now); **J** — a join that states no fact; **R** — new
   wording. **R is vetoed sentence by sentence, and an untagged sentence counts as R.**
4. **A trace table** (DeepSeek): one row per source sentence, with its status (kept, shortened, recomposed into which new
   sentence, moved to S4), so that a veto has one object and nobody compares two long texts from memory.
5. **The whole present Step 4 goes to Supplement S4**, and the nothing-lost check must pass before anyone reads the new
   body.
6. **Stop criteria, fixed in advance** (Grok): if your vetoes catch **a stronger predicate or a dropped number**, the pilot
   stops and the method is not used further. If they catch **two or more broken antecedents**, the method is not ready. If
   they catch only joins, it continues.
7. **If it continues, the order is Grok's:** Steps 2–4 (as one section, recomposed as one — Qwen), then 9 and 14, then 1,
   then 5–6, **and 7–8 last**, because *"a failed join there is a failed paper"*.

**Checks that keep running throughout:** the 152 protected sentences, `verify.py`, nothing-lost, ChatGPT's
model-qualification lock, and DeepSeek's equality scan for every number that appears in more than one step.

### What I expect, stated in advance so it can be checked

Deletion and local rewrites would end the body near 24 000 words. **If recomposition takes 50 to 70 percent from each
section, the body lands somewhere between about 8 000 and 13 000.** The 7 500 target needs about 71 percent everywhere. The
protected sentences are only about 2 200 words, so what must stay does not forbid the target; how well recomposition works
will decide it. **I would rather the pilot showed that than that I promised it.**

## 3. What I am asking

1. **Confirm 1.1–1.3.**
2. **The method (Section 2):** accept, reject, or change it. Name the rule you would change and why. **Are the stop criteria
   right?** Would you tighten or loosen any?
3. **New proposals**, as always.

**Sources.** None of this needs a source.
