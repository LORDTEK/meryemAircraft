# Round 71 — last round's changes applied with both vetoes honoured; a second pass on Step 11; Step 10's dependency map before its draft; and Qwen's arithmetic

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`@@C@@`** ·
> `paper/v8/ALL-STEPS.md` SHA-256 `@@A@@` · `paper/v8/supplement.md` `@@S@@`.
> Not applied: `paper/v8/drafts/11-draft2.md` `@@D@@`.

---

## 1. Closed

**Confirmed by all four of you:** the Step 8 join; Step 12's second pass (2 973 → 1 885 over two rounds); Step 13's first
pass with Grok's vetoes; the supplement rule and the nothing-lost check. **Decided, all five:** every change is tagged D
(deletion, checked mechanically) or R (rewrite, marked ⟦ ⟧, vetoed individually); every S-section names its source step
and round; any figure that shows rotation time or altitude loss carries Step 10's attribution; the escape-condition figure
waits, and it is the author's decision because it would replace prose in Steps 7 and 8.

## 2. Applied — please confirm

**2.1 Step 13, second pass: S2–S5 as you accepted them; S1 with DeepSeek's veto honoured.** The definition of a contract
returns verbatim. The opening now reads:

> Section 12 showed that at least two of the charges are not locked together; where one architecture pays less of one charge and more of another, the ranking depends on how the charges are weighed, and **a sizing contract is one such weighing.** It fixes what is held equal between the architectures being compared, and what is held equal decides how a difference in mass is set against a difference in cruise efficiency. This section applies three contracts to three
> architectures at each of the four closures of Section 10. **The mechanism claim is not a ranking
> and is not at stake here**; what is at stake is how the price computed in Sections 10 and 11 enters
> a comparison with other architectures.

Step 13: 2 200 → 2 147 words; the returned sentence takes back part of what S1–S5 saved (2 398 at the start).

*(ChatGPT: in S3, "(Supplement S13)" is added to the body, not removed.)*

**2.2 Step 11, first pass: 11.1, 11.3 and 11.4 applied; 11.2 vetoed** (DeepSeek and ChatGPT; Grok asked for a clause back).
Under the rule, the source sentence stays as it was. 2 144 → 2 044 words.

**2.3 Supplements.** S11 and S13 now carry, verbatim and under their original headings, every paragraph that lost anything
(marked *Round 71*). The nothing-lost check now covers Steps 11, 12 and 13, and it passes. It had one false alarm this
round: it read a table as one long sentence. It now reads tables row by row, and it still catches a sentence I delete from
the supplement.

## 3. Step 11, second pass — your proposals, side by side

| # | Proposal | By | Type | My position |
|---|---|---|---|---|
| a | Delete *"The refusal has an address, and saying where it points is what keeps it from reading as an unfinished cost section."* | ChatGPT, Grok | D | **Yes** — the two sentences after it say where the refusal points |
| b | Delete *"Section 8 gives the frames four duties: …"* | DeepSeek | D | **Yes.** ChatGPT's first-occurrence test: the duties are introduced in Step 8, and *"the landing and directional duties"* still reads without it |
| c | 11.2: keep the Reynolds number, the free-wheeling state and computed polars; drop only *"and section drag is hardest to predict in that range"* | ChatGPT (DeepSeek and Grok proposed rewrites with the same three facts) | D | **Yes** — deletion only, and Step 12 carries the hardest-to-predict statement |
| d | The lift-to-drag paragraph in one sentence, every number kept | DeepSeek | R | **Yes** |
| — | The fixed-pitch gap paragraph rewritten | Qwen | R | **No.** Grok: 14.6–21.0 and *"No variable-pitch counterfactual was computed"* travel together. The rewrite also drops the protected *"The ledger does not attribute the whole of that gap to the absence of variable pitch"* and adds *"charged to the union"*, which is new wording |

**The draft: 2 044 → 1 957 words, protected sentences present.** Each change:


**11.a — now:**

> **The refusal has an address, and saying where it points is what keeps it from reading as an
> unfinished cost section.** These three quantities become one number only under a sizing contract,
> and that is Section 13: **the total is the contract, not a property of the aircraft.** **Reporting them
> is this paper's job; the weighting belongs to whoever has the mission.**

**Proposed:**

> These three quantities become one number only under a sizing contract,
> and that is Section 13: **the total is the contract, not a property of the aircraft.** **Reporting them
> is this paper's job; the weighting belongs to whoever has the mission.**

**11.b — now:**

> **The rotor line rests on section drag at low Reynolds number.** It is a blade-element result for
> blades whose sections run near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section
> polars that are computed rather than measured, and section drag is hardest to predict in that range.
> Section 12 shows how strongly the term depends on it.

**Proposed:**

> **The rotor line rests on section drag at low Reynolds number.** It is a blade-element result for
> blades whose sections run near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section polars that are computed rather than measured.
> Section 12 shows how strongly the term depends on it.

**11.c — now:**

> **The tip-frame term is an attribution, not a marginal removal cost.** Section 8 gives the frames
> four duties: landing gear, control moment arms, rotor support, and the fairing that is the
> aircraft's only vertical surface. Their drag is charged to the hover-related hardware set because
> that is the set the ledger is decomposing; **it is not a claim that this drag would disappear if
> the vertical phase did**, since the landing and directional duties would still have to be met
> somehow.
>
> The same statement as a lift-to-drag ratio. **Removing all three non-clean-body terms — the hub
> and small items, the tip frames and the free-wheeling rotors** — gives a clean-body ratio of
> **20.55** at the favourable end and **15.24** at the adverse one, against the aircraft's **10.82**
> and **8.79**. **The configuration retains 52.6 percent of its clean-body lift-to-drag ratio at the
> favourable end and 57.7 percent at the adverse one**, so the non-clean-body terms remove 47.4 and
> 42.3 percent respectively, with the frames and rotors the large majority of what is removed.

**Proposed:**

> **The tip-frame term is an attribution, not a marginal removal cost.** Their drag is charged to the hover-related hardware set because
> that is the set the ledger is decomposing; **it is not a claim that this drag would disappear if
> the vertical phase did**, since the landing and directional duties would still have to be met
> somehow.
>
> ⟦**Removing the hub and small items, the tip frames and the free-wheeling rotors gives a clean-body lift-to-drag ratio of 20.55 at the favourable end and 15.24 at the adverse one**, against the aircraft's 10.82 and 8.79: **the configuration retains 52.6 and 57.7 percent**, so the non-clean-body terms remove 47.4 and 42.3 percent, with the frames and rotors the large majority.⟧

**11.d — now:**

> **Every one of the charges above belongs to one scale.** The four closures vary the drag uncertainty and
> the blade-family choice at the reference size; **they do not establish how the three charges
> behave as the aircraft changes size.** Section 12 asks whether they move together when the size
> changes, and Section 13 asks what happens to the comparison when the sizing contract changes.

**Proposed:**

> **Every one of the charges above belongs to one scale.** The four closures vary the drag uncertainty and
> the blade-family choice at the reference size; **they do not establish how the three charges
> behave as the aircraft changes size.** Section 12 asks whether they move together when the size
> changes, and Section 13 asks what happens to the comparison when the sizing contract changes.

## 4. Step 10 — the dependency map first (Qwen P1, Grok P10)

**Step 10 is 2 602 words and the most cited section** (about forty references). Twelve of its sentences are protected.
Before any draft, here is what the rest of the paper takes from it. **Please add anything missing. The draft comes next
round.**

| What | Where it is used |
|---|---|
| The four closures A–D: 52.3–57.5 kg; C_D0 0.0285 / 0.0381; η_p 0.632 / 0.683; L/D 8.79 / 10.82; engine 3.54–5.17 kW; hover 11.4–12.5 kW; range 927–1 233 km (the table) | Steps 6, 11, 13, 14 |
| The drag bracket as uncertainty and the blade family as an unfixed design variable | Steps 11, 13 |
| *"The published zero-lift value of 0.0248 is not used"* (protected) | — |
| The geometry across the closures (area 2.07–2.27 m², span 3.53–3.70 m, disc 1.23–1.29 m, C_L 0.450) | **checked by `verify.py`**, which parses that sentence |
| The unscaled tip hardware: arms at the reference geometry; the drag terms 4 to 13 percent smaller, 0.0009–0.0028, not taken | Step 8 (the arms); **checked by `verify.py`** |
| The reference wing area 1.979 m² | Step 8 |
| The payload, 13 kg, as the input | Step 13 |
| The construction check (49.4 against 50.1 kg; 11.88; 1 585 against 1 583 km) | — (the section's own credibility) |
| The spreads 9.9 / 33.0 / 46.1 percent, and the drag bracket dominating the blade family | — |
| The transition: the point-mass zero loss as a property of the model; **5.4 m** in the finite-moment model with zero aerodynamic moment; 2 s and 5.1 s | Steps 7 (home of *"the transition is not shown"*), 9, 11, 12, 14 |
| *"It does not establish that the package exists"* (protected) | Steps 14, 15 |

**DeepSeek's limit-first rule for the transition is already met:** the subsection opens *"The verdict comes first so that it
cannot be missed: the question is asked in two models, only the second of which carries rotational dynamics, and that one
does not support a zero altitude loss."*

**Qwen's P2 is adopted:** after the Step 10 draft, every sentence elsewhere that says *"Section 10 …"* is checked for its
object, not only its number.

## 5. Qwen's arithmetic — correct, and put to the author

**Qwen P3:** the calculation steps (10–13) are now **8 679** words. Everything else is **17 571**: the framework (Steps 2–4)
5 723, the solutions and their combination (Steps 5–8) 6 931, the introduction 1 689, Step 9 1 388, Step 14 1 503 and the
close 337. **Even if the calculations went to zero, the body would be more than twice the working target.** The author
named Steps 5–8 as the innovation narratives and set them apart. How the rest of the distance is covered, and whether the
target itself moves, is the author's decision. I have put it to the author with these numbers.

## 6. Your new proposals

| Proposal | By | My position |
|---|---|---|
| A first-occurrence test on each draft: a removal must not make a later sentence the first unexplained use of a concept | ChatGPT | **Yes** — used above, on (b) |
| Count negative sentences in Step 11 after the rewrites | DeepSeek | **Yes, at the voice pass** |
| Step 10's map one round before its draft | Qwen | **Done** (Section 4) |
| Check the objects of "Section 10 …" sentences after Step 10's draft | Qwen | **Yes** |

## 7. What I am asking

1. **Confirm 2.1–2.3.**
2. **Section 3:** accept or veto each of (a)–(d), quoting the sentence if you veto.
3. **Section 4:** add what the map is missing: numbers, functions, or concepts that must stay in Step 10.
4. **Section 6:** vote.
5. **New proposals**, as always.

**Sources.** None of this needs a source.
