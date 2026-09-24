# Round 72 — the author's decision: shortening from everywhere; Step 11's second pass applied; the first draft of Step 10; and the method question this decision raises

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`@@C@@`** ·
> `paper/v8/ALL-STEPS.md` SHA-256 `@@A@@` · `paper/v8/supplement.md` `@@S@@`.
> Not applied: `paper/v8/drafts/10-draft.md` `@@D@@`.

---

## 1. The author's decision

Qwen's arithmetic went to the author. The answer, translated:

> *"We have to be realistic. Yes, you are right — the readers who warned, and you, all of you are right. If we are
> shortening, it will be shortened everywhere. All right, let us proceed that way, please."*

**So Steps 5–8 are no longer set apart from shortening.** What does not change is the rest of the soul rule: the
insight leads through placement, order and voice, and its ten protected sentences stay under the automated check. The
order of work also stands: the calculations first (Step 10 is the last of them), then the rest.

## 2. Closed and applied

**Confirmed by all four of you:** Step 13's second pass with DeepSeek's veto; Step 11's first pass with the 11.2 veto;
S11 and S13. **Decided, all five:** the first-occurrence test becomes a permanent step; the negative-sentence count is a
diagnostic at the voice pass, never a target; the map comes one round before the draft; the object of every
*"Section 10 …"* sentence is checked after the draft.

**Applied — please confirm: Step 11's second pass, (a) to (d), as you all accepted.** 2 044 → 1 957 words (2 144 at the
start). The two paragraphs whose wording changed:

> **The rotor line rests on section drag at low Reynolds number.** It is a blade-element result for
> blades whose sections run near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section polars that are computed rather than measured.
> Section 12 shows how strongly the term depends on it.

> **Removing the hub and small items, the tip frames and the free-wheeling rotors gives a clean-body lift-to-drag ratio of 20.55 at the favourable end and 15.24 at the adverse one**, against the aircraft's 10.82 and 8.79: **the configuration retains 52.6 and 57.7 percent**, so the non-clean-body terms remove 47.4 and 42.3 percent, with the frames and rotors the large majority.

## 3. ChatGPT's model-qualification lock finds a case already in the body

I ran it before drafting Step 10: every copy of **5.4 m** outside Step 10. There is one, in Step 11, and it has lost its
model:

> *"The transition altitude result (5.4 m) is a result, not a charge, and is not a term in any sizing loop."*

The table it came from (now Supplement S11) said *"5.4 m in the finite-moment model at the 50 kg reference geometry"*.
**Proposed (R, narrower, not stronger):** *"The transition altitude result (5.4 m, in the finite-moment model at the 50 kg
reference geometry) is a result, not a charge, …"* Vote, please.

## 4. Step 10 — your map additions, merged, and the first draft

**What you added, and where it actually lives.** Most of your additions are in Step 10, and the draft keeps them whole:
the closure statement and its fixed point (Qwen, DeepSeek); propeller efficiency entering twice (Qwen, DeepSeek); the
sizing rules and C_L 0.450 (Qwen, DeepSeek); the fixed polar (Qwen, DeepSeek); the payload fraction, the spreads and the
dominance of the drag bracket (DeepSeek); the construction check as a credibility check rather than an output (ChatGPT,
DeepSeek); the closures as one configuration at four masses (the protected *"These are the same configuration at four
closed masses rather than four configurations"*); the bracket as uncertainty (*"A designer does not choose where the real
aircraft falls in that range"*); the two transition models (ChatGPT, Grok).

**Several of Grok's and DeepSeek's items are not in Step 10**, so the Step 10 draft cannot lose them: the 3.6 percent buffer,
the 16 percent fuel fraction, disc loading near 44 kg m⁻², the engine sized by cruise, the take-off margin drawn from the tip
pairs, and the blade the hover requirement selects at 50 kg. Their homes are Steps 5, 7, 11, 12, 13 and 14. **The 50 kg reference
design is distinct from the closures:** Step 10 says so (*"for the 50 kg design, which is the only one carried through this
loop"*), and the draft keeps it.

**Grok P11 and P13:** the two sentences `verify.py` parses (the geometry across the closures; the 0.0009–0.0028 drag terms not
taken) are untouched, and both still parse. The transition subsection's verdict-first sentence stays verbatim.

**Result: 2 601 → 2 403 words (−8 %).** Five sentences leave for Supplement S10, two are shortened, and one pointer join is
marked ⟦ ⟧:

**10.1 — now:**

> **The blade family is a design variable this study has not fixed.** Four nose-blade families
> meet the hover figure of merit, and their cruise propeller efficiencies span **0.632 to
> 0.683**. A designer would choose one; the criteria that would decide the choice — structural
> loads, acoustics, the motor operating point, rotor inertia, manufacture — are not modelled
> here, so the study carries all four rather than pretending to have chosen.

**Proposed:**

> **The blade family is a design variable this study has not fixed.** Four nose-blade families
> meet the hover figure of merit, and their cruise propeller efficiencies span **0.632 to
> 0.683**. A designer would choose one; the criteria that would decide the choice are not modelled
> here, so the study carries all four rather than pretending to have chosen.

**10.2 — now:**

> **The sizing rules that keep that ratio valid as the mass moves are worth stating, because they
> also say what the four closures are geometrically.** The loop holds **wing loading, disc loading
> and aspect ratio** fixed, so area, span and disc diameter follow the mass: across the four
> closures the wing area runs 2.07 to 2.27 m², the span 3.53 to 3.70 m, and the nose disc diameter
> 1.23 to 1.29 m. **The cruise lift coefficient is unchanged at 0.450 in every one of them**, so the
> lift-to-drag ratio is an input that stays valid at the closed mass rather than one frozen at a mass
> the loop has left behind. Had wing **area** been held fixed instead, the lift coefficient would
> have risen with the closed mass, the induced term would have moved against the heavier closures,
> and the drag corners would be optimistic as reported.

**Proposed:**

> **The sizing rules that keep that ratio valid as the mass moves are worth stating, because they
> also say what the four closures are geometrically.** The loop holds **wing loading, disc loading
> and aspect ratio** fixed, so area, span and disc diameter follow the mass: across the four
> closures the wing area runs 2.07 to 2.27 m², the span 3.53 to 3.70 m, and the nose disc diameter
> 1.23 to 1.29 m. **The cruise lift coefficient is unchanged at 0.450 in every one of them**, so the
> lift-to-drag ratio is an input that stays valid at the closed mass rather than one frozen at a mass
> the loop has left behind.

**10.3 — now:**

> **And the blade that is best before the loop is still best after it.** There was no reason to
> assume so: propeller efficiency propagates through cruise power into engine size, engine size
> into mass, and mass back into hover power, and a loop can reverse a local ranking. It does not
> here — at both ends of the drag bracket the higher-efficiency family closes to the longer
> range. **That is a result of the closure rather than an assumption carried into it**, and it
> is reported because the opposite outcome would have been reported too.

**Proposed:**

> **And the blade that is best before the loop is still best after it.** It does not
> here — at both ends of the drag bracket the higher-efficiency family closes to the longer
> range. **That is a result of the closure rather than an assumption carried into it.**

**10.4 — now:**

> **In this point-mass model there is no transition time to optimise**, which is a simplification
> rather than a trade.
> The control moment required scales as 1/t_r² and the control power as 1/t_r³, and the altitude
> loss falls with t_r as well: all three point the same way, so the rotation time is set by what
> the actuator can do rather than by a balance between competing penalties.

**Proposed:**

*(leaves; to Supplement S10 verbatim)*

**10.5 — now:**

> **The loss is not an artefact of the controller.** It is unchanged across linear, bang-bang and
> smooth reference profiles; it appears without the control moment ever saturating; and it grows
> rather than vanishes as the gains are raised, reaching 17 m at gains high enough to track the
> reference almost exactly. **What the kinematic model leaves out is not the difficulty of turning
> the aircraft but the trajectory the aircraft flies while it is being turned**, so tighter tracking
> of a reference the rotational dynamics do not admit moves the aircraft further from the path it
> can actually fly, not closer.

**Proposed:**

> **The loss is not an artefact of the controller** ⟦(profiles, saturation and gains: Supplement S10)⟧. **What the kinematic model leaves out is not the difficulty of turning
> the aircraft but the trajectory the aircraft flies while it is being turned**, so tighter tracking
> of a reference the rotational dynamics do not admit moves the aircraft further from the path it
> can actually fly, not closer.

**10.6 — now:**

> **And these range figures are carried forward as the closed-loop values, not as a ranking.** No
> multirotor is sized in this work, so no range comparison is made against one — Section 6 compares
> the two families in cruise efficiency and says why it stops there. The comparison against the
> other hybrid architectures depends on the sizing contract and belongs to Section 13, which is
> where it is made.

**Proposed:**

> **And these range figures are carried forward as the closed-loop values, not as a ranking.** No
> multirotor is sized in this work, so no range comparison is made against one — Section 6 compares
> the two families in cruise efficiency and says why it stops there. The comparison against the
> other hybrid architectures depends on the sizing contract and belongs to Section 13, which is
> where it is made.

**Proposed protection (ChatGPT's protected-predicate list):** Step 10 already protects *"property of the model"*, *"does not
establish that the package exists"*, *"is not used"* and the finite-moment sentence. I propose adding the verdict: *"the
question is asked in two models, only the second of which carries rotational dynamics, and that one does not support a zero
altitude loss."*

## 5. The method question this decision raises — my view, for your criticism

**The measurement so far.** Deletion alone took 7 to 12 percent from each calculation step. With your rewrites, Step 12 is
down 37 percent in total, Steps 11 and 13 about 9 and 10 percent. **Continued this way, the body ends near 24 000 words** (my estimate: the
calculations at about 8 400, everything else down some 12 percent), not 7 500. The protected sentences total about **2 200 words**, so what must stay does not rule the target out. The method
does.

**My view:** the only method that reaches the target is **recomposition**. For each section, the body is written anew from
its dependency map: its findings, its protected sentences verbatim, the numbers other sections cite, and a join for each. The
whole original goes to the supplement, and the nothing-lost check proves it. Every recomposed section is R, so it is vetoed
sentence by sentence. **The risk is the one this project has paid for four times: summaries are where its errors come from.**
So I would **pilot it on one section and count the errors your vetoes catch** before using it widely. I would pilot it on
Step 4, the independent check: it is framework, not narrative, and its finding is one comparison.

**Your own method, if you see a better one.** How would you reach roughly a 70 percent reduction in Steps 1–9 and 14?

## 6. Your other proposals

| Proposal | By | My position |
|---|---|---|
| Model-qualification lock | ChatGPT | **Yes** — used in Section 3 |
| Closure-object test; range-provenance test | ChatGPT | **Yes, at each draft's confirmation** |
| Protected predicates | ChatGPT | **Yes** — Section 4's addition |
| After Step 10 is applied, check every closure number elsewhere for equality | DeepSeek | **Yes** — `verify.py` parses the geometry already; I will add the table values |
| Map and draft Steps 2–4 next | Qwen P1 | **Yes** — and Step 4 as the recomposition pilot, if you agree with Section 5 |
| Step 14's table of unknowns to S14 | Qwen P2 | **Already done in Round 62**: the table is in S14, and Step 14 carries a list |
| Step 9's eight refusals compressed at their homes | Qwen P3 | **Yes, when Step 9 is drafted** |
| Do not open 5–8 in this block | Grok P12 | **The author has now decided otherwise**; the order still puts the calculations and the framework first |

## 7. What I am asking

1. **Confirm** Step 11's second pass (Section 2).
2. **Section 3:** the 5.4 m qualification: yes or no.
3. **Section 4:** veto or accept the Step 10 draft; yes or no on protecting the verdict sentence.
4. **Section 5:** recomposition piloted on Step 4 — agree, disagree, or your own method.
5. **Section 6:** vote.
6. **New proposals**, as always.

**Sources.** None of this needs a source.
