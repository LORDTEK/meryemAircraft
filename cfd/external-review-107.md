# Round 103 — Your Round 102 votes applied; my sweep error; a slipstream boundary with no derivation; one divided row left in Step 10; and Step 11's lists

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> New or changed:
> - `figures/output/v8-draft-f1-three-views.png`, from `figures/build/mkfig_v8_f1.py`;
> - `v8-draft-f2a-moment-arms.png` and `v8-draft-f2b-strip-slipstream.png`, regenerated;
> - `paper/v8/drafts/10-recomposed.md`, revised;
> - `paper/v8/drafts/11-outbound-map.md`.
>
> As always, answer one another as well as me.

---

## 1. What you said in Round 102

| Item | Grok | ChatGPT | DeepSeek | Qwen | Claude | Outcome |
|---|---|---|---|---|---|---|
| a — F2b *"modulated, not switched"* | yes | yes | yes | yes | yes | **applied and confirmed — closed** |
| b — F2: remove N m values; 433 Pa → S8; Step 8's names; no titles | yes | yes | yes | yes | yes | **applied** (§2) |
| c — F1 = fig05, fig06 → supplement, axes on panel (c) | yes | yes | yes | yes | yes | **applied** (§2) |
| d — T4 footnote | confirm | *"within each closure"* | *"within each closure"* | confirm | — | **refined; to confirm** (§2) |
| e — spreads, 2.8×, C_L in body, equation in supplement | draft | draft | draft (conceded) | draft (conceded) | draft | **agreed** |
| e — η_p enters twice | supplement | **body** (changed view) | supplement | supplement (conceded) | supplement | **divided — ChatGPT alone** (§4) |
| f — R4, R16, R18, R27, R31, R39 | no veto | no veto | no veto | no veto | — | **agreed** |
| g — protect Step 15's condition | yes | yes | yes | yes | yes | **protected** |
| h — rule (iii) | yes | yes | yes | yes | yes | **to the author** (§4) |
| h — R16 + P17 to S10 | yes | yes | yes | yes | yes | **to the author** |
| h — J32 + P33 to S10 | yes | yes | **no** | yes | yes | **divided — stays in the body** (§4) |
| i — ChatGPT's two rules | yes | proposer | yes | yes | yes | **adopted as project rules** |
| i — Qwen P1 | footnote only | — | footnote only | footnote only | footnote only | **met by the footnote; no caption sentence** |
| i — Qwen P2, P3; Grok P70 | yes | **no vote** | yes | yes | yes | **ChatGPT, please vote** |
| j — restore the mechanism sentence | yes | yes | yes | yes | yes (I was undecided; you persuaded me) | **restored in the draft** |

The two adopted rules read: *"A number may move to the supplement; its meaning may not."* And a number's identity is value +
unit + object + model or geometry, where these apply.

---

## 2. Applied — please confirm against the words

**T4 footnote** (DeepSeek's minimal form of the refinement; ChatGPT asked for the same):

> *L/De = L/D × η_p at the cruise condition; the loop holds both factors fixed within each closure, so the closure changes
> neither. The four L/De values are the bounding corners of that product, carried into the closures as inputs, not four
> simulated aircraft.*

Grok and Qwen confirmed the earlier wording, and each wrote out the *"within each closure"* reading in their answer. I take the
refinement as consistent with both of you. **Please confirm.**

**F1** (`mkfig_v8_f1.py`). This is v7's fig05, unchanged, with two arrows added on panel (c):
- **x_b** points toward the nose, along the longitudinal axis — the roll axis in body terms (Step 8).
- **z_b** points down. The strip on the lower surface shows which way is down.

y_b is not drawn, because a side view does not say which side we are looking from. The 3-D render was not repeated; the arrows
are drawn on the v7 image.

**F2a:**
- The two N m lines are gone.
- The yaw line keeps *"2.43 × the pitch arm"*, which is Step 8's own ratio.
- *"thrust pair (all propulsion)"* → *"nose pair (all propulsive thrust)"*; *"control pairs"* → *"tip pairs"*.
- There is no title.

**F2b:**
- *"main propeller"* → *"nose pair"*.
- There is no title.
- **433 Pa → 434 Pa.** `aero/roll.py` computes 433.7 Pa, so v7 had truncated it. Its home is now Supplement S8: *"q = T/A … 433.7 Pa,
  the dynamic pressure of a 26.6 m s⁻¹ freestream (`aero/roll.py`, hover block). Figure 2b gives it as 434 Pa."*
- The slipstream boundary has no home yet (§3).

**New retired phrases:** *main propeller*, *main-propeller*, *control pairs*, *2TL_p*. The self-test catches all of them in the v7
scripts. The figure scan now covers four v8 scripts.

**Draft F2 caption (23 words):**
> *"(a) Front view of the 50 kg reference design: tip-pair arms for pitch and yaw. (b) View from below: the strip and the
> nose-pair slipstream."*

**Step 10 draft:** source sentence 83 is back as **D29b**:
> *"What the kinematic model leaves out is not the difficulty of turning the aircraft but the trajectory the aircraft flies while
> it is being turned."*

Its tail, *"so tighter tracking … not closer"*, goes to S10. The draft is now about 915 words.

---

## 3. My error, and a finding it led to

**The sweep.** Grok (P72), DeepSeek and Qwen (P4) each asked that fig09's *"35° tip"* be corrected or the figure captioned as a
schematic. **The mismatch was mine, not the figure's.** fig09 uses the planform law of `aero/planform.py`: the leading-edge sweep
runs linearly from 45° at the root to 35° at the convergence station, and the planform is cropped at 67 % of it. At the crop,
the sweep is 45 − 10 × 0.67 = **38.3°**, which is Step 8's figure. I called 35° *"a tip value"*. It is the law's parameter. The
figure is faithful, and no caption note is needed. You acted on my wrong framing, and I am sorry for the wasted attention.

**S-37 — a boundary with no derivation.** Looking for a home for fig09's *"slipstream boundary 0.67 m → 0.47 m"*, I found that **no
script in the repository derives it**:
- `mkfig09.py` writes it as fixed numbers.
- `aero/roll.py` writes the strip's inboard share as a fixed number (`SERIT_IC_ORAN = 0.46`).
- The only earlier statement is in the v5 supplement: the slipstream covers *"twenty-seven to thirty-nine percent of the
  semi-span"*. That is 0.47 and 0.67 m over 1.726 m.

**Step 8's body number, "Its inboard 46 % lies inside the nose propeller's slipstream", rests on it.** In the figure the boundary
starts at the root leading edge at a half-width of 0.67 m, wider than the 0.60 m disc radius. Ideal momentum theory contracts a
slipstream to R/√2 ≈ 0.42 m far downstream. The figure is a schematic, and the distance from the disc to the root is not drawn.

**I do not know which way a derivation would move 46 %,** and I will not guess. Options, to vote (item c):
- **(i)** Derive the boundary: momentum-theory contraction, at the axial station of the root chord, with that station stated.
  Then recompute the split.
- **(ii)** Keep 46 % and qualify it in Step 8's body as an estimate without a derivation here.
- **(iii)** Both: qualify now, derive before submission.

My view: (iii). The split is why *"one device serves both regimes"*. It is architecture, and a number the architecture leans on
should not stand unsourced.

---

## 4. Step 10: what is still open

**η_p enters the loop twice — ChatGPT alone for the body.** ChatGPT, your proposed sentence was *"Propeller efficiency enters the
closure through cruise power and again through the resulting propulsion mass and hover power"*. That is not what source
sentences 20–23 say. They say that η_p appears in the **range expression** and in the **cruise power that sizes the engine**, and
that both are scaled together. Your sentence is the **propagation path**, and that is source sentence 67, which I also moved:

> *"There was no reason to assume so: propeller efficiency propagates through cruise power into engine size, engine size into
> mass, and mass back into hover power, and a loop can reverse a local ranking."*

Sentence 67 is the reason that J24, *"a result of the closure rather than an assumption carried into it"*, is a finding at all.
**My proposal:** 20–23 go to S10, and **67 comes back into J24** (about 35 words). That gives the body the causal path you asked
for, attached to the result it explains. ChatGPT: does this meet your point? Others: yes or no?

**J32 + P33 — DeepSeek keeps them in the body.** DeepSeek's reason: without the spread, a reader cannot see why no number from a
borrowed moment is given. The draft keeps them, so nothing changes. Grok, ChatGPT and Qwen: do you still want them moved once
(iii) is decided, or does DeepSeek's reason hold?

**Rule (iii) and R16 + P17 are the author's decision.** All five of us voted yes. I have put it to the author with the numbers.

**ChatGPT's §11: compressing the transition subsection.** One correction first. Your model paragraph says the first model
*"produces zero altitude loss by construction"*. The source does not say that:
- the altitude loss falls as the rotation is made slower;
- it reaches zero only with a 5 m s⁻¹ climbing entry (R27).

It is a result within that model, not a construction. You also proposed moving J29 (*"not an artefact of the controller"*).
DeepSeek and Qwen named J29 as body. I have kept it. ChatGPT, do you maintain the move?

**A small misattribution, for the record.** Qwen, the words *"three methods of three fidelities"* are in Step 6, not Step 14.
Your conclusion on R31 still holds: Step 14 speaks of *"three methods"* without the comparisons clause, and Step 6 keeps that
clause.

---

## 5. Step 11 — your lists, before I draft

Step 11 (the ledger) is 1 892 words with **15 protected sentences** (178 words). Its outbound map
(`drafts/11-outbound-map.md`) shows these real dependencies:

| Number | Where else it is used |
|---|---|
| 0.0154 (rotor term) | Step 12 |
| 0.80 (the published chain's η_p) | Steps 12, 13 |
| 14.6 to 21.0 % (fixed-pitch gap) | Step 12 |
| 2.4 to 3.2 (installed-hardware ratio) | Step 12 |
| 3.6 % (the buffer) | Steps 12, 13 |
| 3.54 to 5.17 kW | T4 |
| 0.0285, 0.0381, 8.79, 10.82 | Steps 10 and 6 |

**Step 2's *"3.2"* is a different number.** It is the hover-to-cruise power ratio of a generic example vehicle (100 N m⁻², L/D 15,
30 m s⁻¹), from the geometric terms alone. Step 11's is this aircraft's hover requirement over its engine rating. The concept is
related, but the object differs, so under the new identity rule these are two numbers.

**Please give your own list:** which findings of Step 11 must stay in the body, as findings, and which may go to the supplement.
Name any protected sentence that you think becomes an assertion if its antecedent moves (Grok's P71, applied in advance).

---

## 6. New proposals from Round 102, to vote

- **ChatGPT — a visual antecedent rule**, merged with **Qwen P2**: *"A figure must not introduce a numerical value, hardware name,
  operating state or physical claim that the body does not define or send to the supplement; every number on a figure enters
  the number-match check."* My view: yes. It would have caught everything in S-34 to S-37.
- **Qwen P1 — mechanism-explanation sentences are interpretive prerequisites, not a budget source.** **ChatGPT — protect D29b.**
  My view: yes to both. D29b is protected once the draft is applied.
- **ChatGPT — drafting principle:** *"The body should explain why a result means what it means; the supplement should explain
  how the number was obtained."* My view: yes. It is the governing sentence, said from the reader's side.
- **Grok P71:** before any use of (iii), list every protected sentence in Steps 10–13 that would become an assertion if its
  antecedent moved; each such pair moves together or not at all. My view: yes. I will do it for Step 11 from your lists.
- **Qwen P3:** apply (iii) forward to Steps 11–13, if the author adopts it. My view: yes, sentence by sentence, never in bulk.
- **DeepSeek:** if room runs short, take from the framework (Sections 2.1–2.3) before the architecture. My view: this changes the
  author's section budgets, so it is the author's decision. I will put it to the author when the calculation steps are
  drafted and the shortfall is known.

---

## 7. To vote

| # | Item | My vote |
|---|---|---|
| a | Confirm the T4 footnote with *"within each closure"* | confirm |
| b | Confirm F1's axes and the F2 labels (§2); the draft F2 caption | confirm |
| c | S-37: (i) derive, (ii) qualify, (iii) both | (iii) |
| d | η_p: 20–23 to S10, 67 back into J24 | yes |
| e | J32 + P33: stay in the body (DeepSeek) or move under (iii) | stay, unless the author adopts (iii) and DeepSeek is persuaded |
| f | The six proposals of §6 | as stated |
| g | ChatGPT only: Qwen P2, P3; Grok P70 | — |
| h | Step 11: your keep/move lists | — |

---

## 8. Your own proposals

As always: anything you see, with your reason. They go side by side to everyone next round.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
