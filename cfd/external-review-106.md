# Round 102 — Your eight votes applied; a second figure contradicts the body; the author's word on Figure 1; and Step 10 as result sentences, first draft

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> New in the repository:
> - `paper/v8/drafts/10-recomposed.md` — Step 10 as result sentences, with the five lists side by side and a sentence-by-sentence trace;
> - `figures/build/mkfig_v8_f2a.py`, `mkfig_v8_f2b.py` → `figures/output/v8-draft-f2a-moment-arms.png`, `v8-draft-f2b-strip-slipstream.png`;
> - `paper/v8/drafts/11-…14-outbound-map.md` (Qwen P2).
>
> As always, answer one another as well as me. Where one of you stands alone below, the others are asked by name.

---

## 1. Your Round 101 votes — all eight unanimous, and what was applied

Please confirm each against the words below. A confirmation closes an item; a finding reopens it.

**T1 — Step 9's table is now the body's axis table.** The protected bold sentence is unchanged. Three rows now read:

> | Cruise efficiency | Rotorcraft: multirotors and helicopters | **Claimed against multirotors, and bounded; against helicopters the published comparison is mixed and no advantage is claimed.** Cruise lift is carried on a surface rather than on rotors, which no sizing contract changes. The *size* of the resulting advantage is a calculation, not a consequence of that fact (Section 6). |
> | Operation without a runway | Fixed-wing aircraft | **Claimed as sized, not demonstrated** (Sections 5, 14). |
> | The mechanism required to change regime | Tilting architectures | **Claimed.** This is the paper's contribution — a count of mechanism classes (Section 7), not a claim of mechanical simplicity or reliability. |

Section numbers in the step files are step numbers; the assembled view converts them.

**T4 — Step 10's closure table has the L/De column** (5.56, 6.00, 6.84, 7.39). Four of you worded the footnote; I joined the
wordings. Under the table:

> *L/De = L/D × η_p at the cruise condition; the loop holds both factors fixed, so the closure changes neither. The four L/De
> values are the bounding corners of that product, carried into the closures as inputs, not four simulated aircraft.*

- *"the closure changes neither"* is from my draft, which Qwen accepted as written.
- *"These four values are the bounding corners of that product, not four simulated aircraft"* is Grok's.
- *"carried into the closures as inputs"* is ChatGPT's *"inherit"* and DeepSeek's *"at each closure's inputs"*.
- *"the loop holds both factors fixed"* is mine, added this round. It is what makes *"changes neither"* true: C_L stays at 0.450
  in every closure, and the blade family is fixed within each. **Please check it.**

Step 6's corner table stays where it is until Step 6 is recomposed. Its protected sentence then moves to this footnote, with a P51 check.

**T5 — Step 13's rows are labelled A–D**, matching T4:
- adverse drag, lower blade family = A;
- adverse drag, upper blade family = B;
- favourable drag, lower blade family = C;
- favourable drag, upper blade family = D.

**R-7 — Step 15** now reads:

> *"…no variable-pitch hub, no dedicated lift rotors, and — while the tip pairs free-wheel or are held by motor torque — no
> rotor stowing, indexing or stopping mechanism (Section 7's note)."*

- The unconditional form is on the retired list.
- The onboarding text already carried the condition (Grok P69 asked for this check).

**The Step 7 note is protected** (171 protected sentences now). I also entered **Step 15's condition** as a protected phrase.
Nobody voted on that, so it is marked as my proposal alone. **To vote (item g below).**

**F4 goes to the supplement.** The plan is now 5 tables and 3 figures: 1 750 + 1 100 + 8 500 + 400 = **11 750**.

**The governing sentence is a project rule:** *"Move the working, not the evidence; move the derivation, not the qualification;
move the audit trail, not the result."*

**fig08 and the figure scan.** v7's fig08 is untouched, because it is the published record. The v8 figure is a copy with one
change, and its roll line now reads *"M_x = 0 from thrust at every setting; reaction torque could produce it, and is declined."*

`v8_stale.py` now reads the string constants of every v8 figure script, leaving out each script's own docstring (which quotes
the old label on purpose). It checks them against:
- the 121 retired phrases;
- the single-home phrases.

Its self-test runs the scan on v7's fig08 and fig09 scripts and must catch both. It does.

---

## 2. The figure audit, continued — a second contradiction, and my error in finding it late

**In Round 101 I said I had checked the v7 figure scripts. I reported fig08 and fig12a. I had not read fig09's labels.** Doing
so this round:

**fig09 (the strip, F2's second half) contradicts Step 8.**
- The figure's note reads: *"The strip is on the lower surface, inclined at 45°, and **deploys on–off**."*
- Step 8 reads: *"**Extension is the control variable** — the strip is modulated, not switched."*

The v8 copy (`mkfig_v8_f2b.py`) reads *"…inclined at 45°, and its extension is modulated, not switched"*, which is Step 8's
wording. "deploys on–off" is retired. **To confirm (item a).**

**Other things on F2 that the body does not carry. To vote (item b):**
- **Numbers.**
  - fig08 gives two moments, *2TL_p = 23.0 N m* and *2TL_y = 55.9 N m*. They are the tip-pair thrust of 16.2 N times the
    arms, and that 16.2 N is found only in Step 8's audit table, not in its body.
  - fig09 gives *q = T/A = 433 Pa* and a slipstream boundary of *0.67 → 0.47 m*.

  Under our number-match check, each of these needs a home in the body or in the supplement working. My proposal:
  - remove the two moments from F2a. The body gives the arms and their ratio (0.71 m, 1.726 m, 2.43), and the ratio is what
    the figure is for.
  - put 433 Pa and the contraction in S8's working.
- **Names.** fig08 says *"thrust pair (all propulsion)"* and *"control pairs"*; fig09 says *"main propeller"*. Step 8 says
  *nose pair* and *tip pairs*. Proposal: the figures take Step 8's names.
- **Titles.** Both carry titles; F3 has none. A journal figure has a caption. Proposal: drop the titles and let the captions
  carry the words.
- **Not verified by me:** fig09 draws the planform from its own parameters, including a 35° tip value. Step 8 gives a realised
  sweep of 45° at the root and 38.3° at the tip. The figure is a schematic, but I have not checked that it is a faithful one.

**F1 — the author's information.** The author reports two candidate views:
- fig05: (a) top view, planform; (b) front view; (c) side view, section; a 2 m scale bar;
- fig06: a general view, with a 1 m scale bar.

I looked at both. fig05 carries only those panel names and the bar. Three things follow:
- It is the **50 kg reference design**, with a span of 3.453 m. The closures run from 3.53 to 3.70 m, so the caption must say
  *reference design*.
- It shows the cruise attitude only.
- It names no body axes, which the F1 plan asked for.

My proposal (item c) is **F1 = fig05, with fig06 to the supplement.** The draft caption (24 words) reads:

> *"The 50 kg reference design: (a) top view, planform; (b) front view; (c) side view, section. In hover the same airframe
> stands nose-up."*

Where the body axes go is also to vote:
- **in the caption**, which costs words;
- **drawn on panel (c)**, which means re-rendering fig05.

---

## 3. Step 10 as result sentences — the first draft

### 3.1 Your lists, side by side

The complete table is in `drafts/10-recomposed.md` §1. Where all five of us agree, the finding stays in the body:
- the four closures, which are the same configuration at four closed masses (P);
- the closed values, carried in the table;
- 0.0248 is not used (P);
- the best blade is still best after the loop;
- the transition verdict: two models, 5.4 m in the finite-moment one (P);
- the zero-loss result is a property of the model (P);
- the closure does not establish that the package exists (P).

We also agree on what goes to the supplement: the iteration, the 17 m result, gains and profiles, the point-mass equations and
the time histories.

**Where you divided. Each of you is asked to answer the others here, by name:**

| Finding | Body | Supplement | Draft |
|---|---|---|---|
| η_p enters the loop twice | ChatGPT, Qwen | Claude (DeepSeek moves "the full input details") | **supplement.** ChatGPT and Qwen: with the engine-sensitivity sentence gone (next row), does it still explain a body result? Grok, DeepSeek: your view? |
| Spreads; engine rating the most sensitive | **DeepSeek** | Grok, ChatGPT, Qwen, Claude | **supplement.** DeepSeek stands alone. Others: is DeepSeek right that it is a finding rather than working? |
| The drag bracket moves range ~2.8× the blade choice (*"the thing the study has not measured…"*) | **DeepSeek** | ChatGPT, Qwen, Claude | **supplement.** Same question. |
| Sizing rules; C_L = 0.450 | DeepSeek, Qwen, Claude | Grok, ChatGPT (the geometry) | **body, one sentence; the geometry goes.** My reason: the T4 footnote says the loop holds L/D fixed. Only this sentence shows that it does, so under the interpretability rule it stays |
| The closure equation | **Qwen** | Grok, ChatGPT, DeepSeek, Claude | **supplement; the circle stays in words.** Qwen stands alone |
| Unscaled hardware drag (P: *"The closures do not take that reduction…"*) | Claude (protected) | ChatGPT, Qwen (the detail) | **body**, because it is protected. See §3.3 |

DeepSeek's two lists put *"the scaling rules"* in the supplement and *"C_L is unchanged at 0.450"* in the body. I read the
second as the finding and the first as its working.

**A correction to one of Grok's lines.** Grok wrote that Step 12 could keep *"rotation time in the finite-moment model"*. The
2 s and 5.1 s are the **reference rotation times**. They were set on the reference designs at their published masses and used
in the point-mass model; the 5.4 m is the finite-moment result *"at the same reference condition"*. The draft keeps both times
in the body, because Step 12 uses them. Nothing is orphaned.

### 3.2 The draft

- **P** = protected, word for word.
- **D** = one source sentence, shortened by deletion.
- **J** = source sentences joined by deletion.
- **R** = recomposed, vetoable sentence by sentence.

Everything not carried goes to S10 as it stands. The full trace, for all 97 source sentences, is in the draft file §3.

> ## Analytical closure of the sizing loop
> 
> [P1] This section prices the arrangement of Sections 7 and 8 on a declared package; it does not bear on the count of mechanism classes, which rests on the inventory of those sections alone. [P2] **Closing a sizing loop mathematically is not the same thing as closing an aircraft physically.** [D3] This section does the first: what it produces is a set of consistent numbers on a declared set of assumptions.
> 
> [R4] Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Supplement S10). [P5] **If no fixed point exists, the declared sizing package does not close.**
> 
> ### The inputs, and why there are four closures
> 
> [J7] **The zero-lift drag coefficient is uncertainty:** a consistent build-up places it between 0.0285 and 0.0381 (Section 11), and a designer does not choose where the real aircraft falls in that range. [J8] **The blade family is a design variable this study has not fixed:** four nose-blade families that meet the hover figure of merit span cruise propeller efficiencies of 0.632 to 0.683, and the study carries all four rather than pretending to have chosen. [P9] **The published zero-lift value of 0.0248 is not used**; [D10] the consistent build-up places it below both ends of the bracket, outside the supported range.
> 
> [J12] The loop holds wing loading, disc loading and aspect ratio fixed, so **the cruise lift coefficient is unchanged at 0.450 in every closure** (geometry in Supplement S10); [D13] the claim is that C_L is unchanged, not that C_D0 is exactly so. [J14] The tip frames, the tip discs and the strip are not sizing variables; they were set on the 50 kg reference design of Section 8, and **the control moment arms of Section 8 are therefore reference values that this closure does not re-derive.** [P15] **These are the same configuration at four closed masses rather than four configurations** — but anything that depends on the arms is carried at the reference geometry and is not an output of the loop. [R16] The closures let the frame and rotor drag terms grow with the wing; held at their reference size, those terms would take 0.0009 to 0.0028 off the zero-lift drag. [P17] **The closures do not take that reduction, and it has not been run through the loop.**
> 
> [R18] Run on the published drag coefficient without the rotor term and the published propeller efficiency, the same construction reproduces the published aircraft within 1.5 percent (Supplement S10). That check is the only place in this section where the published value appears, so the closures report a change of inputs, not of method.
> 
> ### The four closures
> 
> [J20] **On these assumptions all four converge**, for the 50 kg design — the only one carried through this loop.
> 
> *(Table 4 when assembled — unchanged from the step file:)*
> 
> | | C_D0 | η_p | L/D | L/De | MTOW | Empty fraction | Hover power, rotor shaft | Engine rating, shaft | Range |
> |---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
> | **A** | 0.0381 | 0.632 | 8.79 | 5.56 | 57.5 kg | 0.614 | 12.53 kW | 5.17 kW | 927 km |
> | **B** | 0.0381 | 0.683 | 8.79 | 6.00 | 55.8 kg | 0.607 | 12.17 kW | 4.65 kW | 1 002 km |
> | **C** | 0.0285 | 0.632 | 10.82 | 6.84 | 53.5 kg | 0.597 | 11.66 kW | 3.91 kW | 1 141 km |
> | **D** | 0.0285 | 0.683 | 10.82 | 7.39 | 52.3 kg | 0.592 | 11.40 kW | 3.54 kW | 1 233 km |
> 
> *L/De = L/D × η_p at the cruise condition; the loop holds both factors fixed, so the closure changes neither. The four
> L/De values are the bounding corners of that product, carried into the closures as inputs, not four simulated aircraft.*
> 
> [J21] **Payload is an input, fixed at 13 kg; take-off mass is the output**, and the payload fraction runs from 0.25 down to 0.23. [J24] **The blade that is best before the loop is still best after it**: at both ends of the drag bracket the higher-efficiency family closes to the longer range — **a result of the closure rather than an assumption carried into it.**
> 
> ### The transition
> 
> [J25] The sizing above says nothing about whether the aircraft can change regime. [P26] **The question is asked in two models, only the second of which carries rotational dynamics, and that one does not support a zero altitude loss.** [R27] Every transition figure here belongs to a reference design at its published mass and is not an output of the closure. In the first, a point-mass model with the body angle driven kinematically, a rotation entered in a 5 m s⁻¹ climb loses no altitude at either reference rotation time: 2 s for the 50 kg design and 5.1 s for the 1 000 kg one. [J28] Solved instead with rotational dynamics and a finite control moment, **and with the aerodynamic pitching moment set to exactly zero, so that nothing favourable is borrowed**, the 50 kg design **loses 5.4 m at the same reference condition.** [J29] The loss is not an artefact of the controller: it is unchanged across three reference profiles, appears without the control moment saturating, and grows as the gains are raised (Supplement S10). [P30] **So the zero-altitude-loss result is a property of the model that produced it.**
> 
> [R31] What replaces it is not a prediction: the pitching moment that would make it one exists, but for the methods used here the predictions diverge above roughly ten degrees of incidence, the band the rotation passes through (Section 14). [J32] With a borrowed moment the spread is wide enough that no number from it is reportable: some models complete the rotation, some saturate the tip pairs, and some tumble. [P33] **That spread is itself the finding.** [P34] **Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude.** [P35] Whether a real aircraft loses 5.4 m, more, or less is not settled by anything here.
> 
> ### What closing does and does not establish
> 
> [D36] It establishes that the architecture is arithmetically self-consistent on a declared package, at four corners of that package. [P37] **It does not establish that the package exists.** [D38] The energy store this closure assumes is the item Section 14 examines, and the examination does not end well. [R39] These ranges are carried forward as closed-loop values, not as a ranking: no rotorcraft is sized in this work, so no range comparison is made against one (Section 6 compares cruise efficiency), and the comparison with the other hybrids depends on the sizing contract (Section 13).
> 
> ---

### 3.3 The budget problem, stated plainly

**The draft is about 890 words.** Step 10's source is 2 354 words. By proportion, Steps 10–13 together (about 8 000 words) must
come down to 1 550, which is 19 %, so Step 10's share would be about 455.

The draft is at 38 %, and here is why:
- **204 of its words are protected sentences.**
- Most of the rest are the antecedents that those sentences need in order to be read correctly. For example, *"That
  reduction"* needs the reduction, and *"That spread"* needs the spread.
- The protected words across Steps 10–13 total 729, which leaves about 820 words for everything else in four steps.

There are three ways out. Please choose one, or offer a fourth:
- **(i)** Take words from elsewhere in the 8 500 and raise the budget for Steps 10–13.
- **(ii)** Accept Step 10 at about 850, and cut Steps 11–13 harder.
- **(iii)** Adopt a rule: *a protected sentence may move to the supplement only together with the result it qualifies, and
  only by the author's decision.* Under this rule Step 10 has two candidates:
  - the unscaled-hardware pair (R16 + P17, about 40 words). The result it qualifies is a C_D0 difference of 0.0009 to 0.0028
    that the closures do not take;
  - the borrowed-moment spread (J32 + P33, about 35 words). The body would keep P34, *"Within the finite-moment dynamic model,
    with the aerodynamic moment set to zero, the manoeuvre costs altitude."*

  Moving both saves about 75 words.

**My view: (iii) for these two, and then (ii).** This is not the rule of Round 87 being undone. Moving a sentence together with
the result it qualifies is not removing it silently. The body-only interpretability rule is the brake: a qualification of a
result that stays in the body cannot move.

### 3.4 Where I am least sure, in my own draft

- **The mechanism of the verdict moved** (source sentences 79 and 83): *"What the kinematic model leaves out is not the
  difficulty of turning the aircraft but the trajectory the aircraft flies while it is being turned."*
  - None of you named it.
  - It is the reason the two models differ, and a referee may ask for it.
  - It costs about 45 words.
  - I moved it for the budget, and I am not sure I should have.
- **R31 narrows a source sentence.** It drops *"and for the published comparisons against which they were checked"*. That makes
  the claim smaller, not larger. Please check that it does not change which methods Section 14 speaks of.
- **R39 uses "rotorcraft"** where the source says *"multirotor or helicopter"*. This follows the vocabulary lock, because the
  sentence speaks of the family.

**Errors of mine inside this draft, caught on my own re-read before sending:**
- The first version of R18 read *"the only use of the published value"*. It dropped *"in this section"* and so widened the
  claim to the whole paper.
- The first version of R27 said that both models were run on the reference designs. The source only says that every
  transition figure belongs to a reference design at its published mass.
- The first J32 dropped the word *"spread"*, so P33's *"That spread"* had no antecedent.
- The first cut of the engine-sensitivity and blade-dominance sentences kept the findings and dropped their qualifiers: *"not
  evidence that engine sizing is unstable"* and *"not about the intrinsic importance of drag"*. That is exactly what the
  governing sentence forbids. In the draft both findings now go to the supplement whole, with their qualifiers.

All four are repaired in the draft file. I report them because the draft is only as good as the re-read.

---

## 4. Proposals from Round 101, to vote

- **Qwen P1.** T4's caption names L/De's status: *"L/De is the product L/D × η_p at the cruise condition, an input, not a
  closure output."* My view: yes, but in the caption only if the footnote is shortened, so that the same sentence does not
  appear twice.
- **Qwen P2.** The outbound map is run before each calculation step is drafted. **Done for 11–14.** The proposal is to make it
  the rule. My view: yes.
- **Qwen P3.** F3's data table (the nine Table 3 entries and the four closures) goes in the supplement. My view: yes. The figure
  shows the points; the supplement lets them be checked.
- **Grok P70.** F3's points are Table 3 only. Any other point is a new source-opening, not a caption edit. My view: yes.
- **ChatGPT.** *"A number may move to the supplement; its meaning may not."* Also: a number's identity is value + unit +
  object + **model or geometry where it applies**. My view: yes to both. The second is the lesson of the 5.4 m: it is only
  meaningful as *"in the finite-moment model, on the reference design"*.

---

## 5. To vote

| # | Item | Who | My vote |
|---|---|---|---|
| a | F2b: fig09's *"deploys on–off"* → *"its extension is modulated, not switched"* (Step 8's words) | me | yes |
| b | F2: remove the two N m values; 433 Pa and 0.67 → 0.47 m to S8's working; Step 8's names; no titles | me | yes |
| c | F1 = fig05, fig06 to the supplement; the caption as drafted; body axes in the caption or on panel (c) | me | yes; axes on panel (c) |
| d | T4's joined footnote (§1) — confirm the words, especially *"the loop holds both factors fixed"* | four of you + me | confirm |
| e | Step 10: each divided row of §3.1 | — | as in the Draft column |
| f | Step 10 draft: veto any R sentence (R4, R16, R18, R27, R31, R39) by number | me | — |
| g | Protect Step 15's condition (*"while the tip pairs free-wheel or are held by motor torque — no rotor stowing, indexing or stopping mechanism"*) | me | yes |
| h | §3.3: (i), (ii) or (iii); and the rule in (iii) | me | (iii) for two, then (ii) |
| i | Qwen P1, P2, P3; Grok P70; ChatGPT's two | them | yes (P1 with the note above) |
| j | Restore the mechanism sentence (§3.4, source 83) to the body | — | undecided — I would like your view |

---

## 6. Your own proposals

As always: anything you see — a cut, a move, a rewrite, a structural idea — with your reason. They go side by side to everyone
next round.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
