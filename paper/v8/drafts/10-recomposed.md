# Step 10 as result sentences — recomposed draft (Round 102; revised Round 103, to vote)

**Nothing here has entered `10-the-closure.md`.** Source: the step file's English body, 2 354 words, 97 sentences, 13 protected.
**This draft: about 915 words of prose (the table counted as an object), of which 204 are protected sentences.** Round 103: source 83 restored (D29b); the T4 footnote reads *"within each closure"*; R16 + P17 await the author's decision on rule (iii). Target for Steps 10–13 together: 1 550.

Tags: **P** protected, word for word · **D** one source sentence, shortened by deletion only · **J** two or more source
sentences joined, by deletion and joining words only · **R** recomposed — new wording, vetoable sentence by sentence.
Every sentence not carried moves to Supplement S10 as it stands (the governing sentence: move the working, not the evidence;
move the derivation, not the qualification; move the audit trail, not the result).

---

## 1. The five lists side by side

| Finding of Step 10 | Grok | ChatGPT | DeepSeek | Qwen | Claude | Draft |
|---|---|---|---|---|---|---|
| Four closures A–D on bracket × blade; same configuration at four closed masses (P) | body | body | body | body | body | body (J20, P15, table) |
| The closed values (mass, powers, ranges) | body (T4) | body | body (T4) | body | body (T4) | table + J21 |
| Bracket = uncertainty; blade family = unfixed variable | — | body | (inputs → supp.) | body | body | body (J7, J8) |
| 0.0248 not used (P) | — | body, one sentence | body | body | body | body (P9, D10) |
| **η_p enters twice** | — | body, one sentence | (inputs → supp.) | body | supp. | **supp. — divided** |
| **Sizing rules; C_L 0.450** | (geometry → supp.) | (geometry → supp.) | body | body | body | **body (J12, D13) — divided** |
| **Closure equation** | supp. | supp. | supp. | body | supp. | **supp.; the circle stays in words (R4)** |
| Construction check | supp. (working) | finding body, arithmetic supp. | body, one sentence | body | finding body | body (R18) |
| **Spreads; engine the most sensitive** | supp. | supp. | body | supp. | supp. | **supp. — DeepSeek alone for body** |
| **Drag dominates blade (2.8×, 2.4×)** | — | supp. | body | supp. | supp. | **supp. — DeepSeek alone for body** |
| Best blade still best after the loop | — | body | body | body | body | body (J24) |
| Reference arms not re-derived (P) | — | qualification body | — | — | body | body (J14) |
| Unscaled hardware, reduction not taken (P) | — | supp. (detail) | — | supp. | body (P) | body (R16, P17) — protected |
| Polar not re-solved per closure | — | — | supp. | supp. | qualifier body | body, qualifier only (D13) |
| Transition verdict: two models (P); 5.4 m finite-moment | body | body | body | body | body | body (P26, J28) |
| 0 m is a property of the model (P) | — | body | body | body | body | body (P30) |
| Loss not an artefact of the controller | — | — | body | body (one sentence) | body | body (J29) |
| 17 m; gains; profiles; point-mass equations; time histories | supp. | supp. | supp. | supp. | supp. | supp. |
| 2 s and 5.1 s reference times | keep if Step 12 needs them | supp. unless a later section needs them | supp. | — | body (Step 12 needs them) | body (R27) |
| Borrowed-moment spread (P "That spread is itself the finding") | — | — | supp. | — | body (P) | body (J32, P33) — protected |
| Does not establish the package exists (P) | — | body | body | body | body | body (P37) |
| Closed-loop values, not a ranking | — | — | body | body | body | body (R39) |

---

## 2. The draft

## Analytical closure of the sizing loop

[P1] This section prices the arrangement of Sections 7 and 8 on a declared package; it does not bear on the count of mechanism classes, which rests on the inventory of those sections alone. [P2] **Closing a sizing loop mathematically is not the same thing as closing an aircraft physically.** [D3] This section does the first: what it produces is a set of consistent numbers on a declared set of assumptions.

[R4] Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Supplement S10). [P5] **If no fixed point exists, the declared sizing package does not close.**

### The inputs, and why there are four closures

[J7] **The zero-lift drag coefficient is uncertainty:** a consistent build-up places it between 0.0285 and 0.0381 (Section 11), and a designer does not choose where the real aircraft falls in that range. [J8] **The blade family is a design variable this study has not fixed:** four nose-blade families that meet the hover figure of merit span cruise propeller efficiencies of 0.632 to 0.683, and the study carries all four rather than pretending to have chosen. [P9] **The published zero-lift value of 0.0248 is not used**; [D10] the consistent build-up places it below both ends of the bracket, outside the supported range.

[J12] The loop holds wing loading, disc loading and aspect ratio fixed, so **the cruise lift coefficient is unchanged at 0.450 in every closure** (geometry in Supplement S10); [D13] the claim is that C_L is unchanged, not that C_D0 is exactly so. [J14] The tip frames, the tip discs and the strip are not sizing variables; they were set on the 50 kg reference design of Section 8, and **the control moment arms of Section 8 are therefore reference values that this closure does not re-derive.** [P15] **These are the same configuration at four closed masses rather than four configurations** — but anything that depends on the arms is carried at the reference geometry and is not an output of the loop. [R16] The closures let the frame and rotor drag terms grow with the wing; held at their reference size, those terms would take 0.0009 to 0.0028 off the zero-lift drag. [P17] **The closures do not take that reduction, and it has not been run through the loop.**

[R18] Run on the published drag coefficient without the rotor term and the published propeller efficiency, the same construction reproduces the published aircraft within 1.5 percent (Supplement S10). That check is the only place in this section where the published value appears, so the closures report a change of inputs, not of method.

### The four closures

[J20] **On these assumptions all four converge**, for the 50 kg design — the only one carried through this loop.

*(Table 4 when assembled — unchanged from the step file:)*

| | C_D0 | η_p | L/D | L/De | MTOW | Empty fraction | Hover power, rotor shaft | Engine rating, shaft | Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** | 0.0381 | 0.632 | 8.79 | 5.56 | 57.5 kg | 0.614 | 12.53 kW | 5.17 kW | 927 km |
| **B** | 0.0381 | 0.683 | 8.79 | 6.00 | 55.8 kg | 0.607 | 12.17 kW | 4.65 kW | 1 002 km |
| **C** | 0.0285 | 0.632 | 10.82 | 6.84 | 53.5 kg | 0.597 | 11.66 kW | 3.91 kW | 1 141 km |
| **D** | 0.0285 | 0.683 | 10.82 | 7.39 | 52.3 kg | 0.592 | 11.40 kW | 3.54 kW | 1 233 km |

*L/De = L/D × η_p at the cruise condition; the loop holds both factors fixed
within each closure, so the closure changes neither. The four
L/De values are the bounding corners of that product, carried into the closures as inputs, not four simulated aircraft.*

[J21] **Payload is an input, fixed at 13 kg; take-off mass is the output**, and the payload fraction runs from 0.25 down to 0.23. [J24] **The blade that is best before the loop is still best after it**: at both ends of the drag bracket the higher-efficiency family closes to the longer range — **a result of the closure rather than an assumption carried into it.**

### The transition

[J25] The sizing above says nothing about whether the aircraft can change regime. [P26] **The question is asked in two models, only the second of which carries rotational dynamics, and that one does not support a zero altitude loss.** [R27] Every transition figure here belongs to a reference design at its published mass and is not an output of the closure. In the first, a point-mass model with the body angle driven kinematically, a rotation entered in a 5 m s⁻¹ climb loses no altitude at either reference rotation time: 2 s for the 50 kg design and 5.1 s for the 1 000 kg one. [J28] Solved instead with rotational dynamics and a finite control moment, **and with the aerodynamic pitching moment set to exactly zero, so that nothing favourable is borrowed**, the 50 kg design **loses 5.4 m at the same reference condition.** [J29] The loss is not an artefact of the controller: it is unchanged across three reference profiles, appears without the control moment saturating, and grows as the gains are raised (Supplement S10). [D29b] **What the kinematic model leaves out is not the difficulty of turning the aircraft but the trajectory the aircraft flies while it is being turned.** [P30] **So the zero-altitude-loss result is a property of the model that produced it.**

[R31] What replaces it is not a prediction: the pitching moment that would make it one exists, but for the methods used here the predictions diverge above roughly ten degrees of incidence, the band the rotation passes through (Section 14). [J32] With a borrowed moment the spread is wide enough that no number from it is reportable: some models complete the rotation, some saturate the tip pairs, and some tumble. [P33] **That spread is itself the finding.** [P34] **Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude.** [P35] Whether a real aircraft loses 5.4 m, more, or less is not settled by anything here.

### What closing does and does not establish

[D36] It establishes that the architecture is arithmetically self-consistent on a declared package, at four corners of that package. [P37] **It does not establish that the package exists.** [D38] The energy store this closure assumes is the item Section 14 examines, and the examination does not end well. [R39] These ranges are carried forward as closed-loop values, not as a ranking: no rotorcraft is sized in this work, so no range comparison is made against one (Section 6 compares cruise efficiency), and the comparison with the other hybrids depends on the sizing contract (Section 13).

---

## 3. Trace — every source sentence (numbered as `v8_outbound`-style splitting of the step body gives them)

| Source | Opening words | Fate |
|---:|---|---|
| 1 | This section prices the arrangement… | **P1** |
| 2 | Closing a sizing loop mathematically… | **P2** |
| 3–4 | This section does the first. What it produces… | **D3** (the clause *"if the assumptions hold, these masses … without contradiction"* → S10) |
| 5 | Whether an aircraft can be built to them… | S10; carried by P2 and P37–D38 |
| 6–9 | The pieces depend on each other… the closure statement… iteration | **R4** (the equation and the MTOW^1.5 term → S10) |
| 10 | If no fixed point exists… | **P5** (its tail *"which is a statement about that package…"* → S10) |
| 11 | Two quantities … not the same kind of quantity | S10; the two bold labels of J7 and J8 carry it |
| 12–14 | The zero-lift drag coefficient is uncertainty… | **J7** (*"with the same rotor term at both ends"* → S10; pointer to Section 11 added) |
| 15–17 | The blade family is a design variable… | **J8** (the list of criteria → S10) |
| 18 | The published zero-lift value of 0.0248 is not used. | **P9** |
| 19 | The consistent build-up places it below both ends… | **D10** |
| 20–23 | Propeller efficiency enters the loop twice… | **S10 — divided** (ChatGPT and Qwen: body) |
| 24–25 | The reference point is the aerodynamic lift-to-drag ratio… | S10; the table's L/D and L/De columns and footnote carry the distinction |
| 26–28 | The sizing rules … C_L unchanged at 0.450 | **J12** (area, span, disc ranges → S10) |
| 29 | Three things the loop does not scale… | S10 |
| 30–31 | The tip-frame length … reference values | **J14** |
| 32 | Section 8 describes one aeroplane… | S10 |
| 33 | These are the same configuration at four closed masses… | **P15** |
| 34–36 | The frame and rotor drag terms … 4 to 13 percent … 0.0009 to 0.0028 | **R16** (1.979 m² and 4–13 % → S10) |
| 37 | The closures do not take that reduction… | **P17** |
| 38–41 | The drag polar is likewise a fixed input … 7 % … 1.4 % … 34 % | S10 |
| 42 | The claim made above is that C_L is unchanged… | **D13** |
| 43–46 | At the published assumption … 49.4 / 11.88 / 1 585 … 1.5 percent … the only place | **R18** (the three pairs of numbers → S10) |
| 47–48 | All four converge. On these assumptions… | **J20** (the 1 000 kg clause → S10; R27 carries the 1 000 kg design's rotation time) |
| 49–50 | (table footnote) | the table, unchanged |
| — | Payload is an input… 0.25 down to 0.23 | **J21** |
| 52–59 | The spreads … 9.9 / 33.0 / 46.1 … only the engine … not evidence of instability | **S10 — divided** (DeepSeek: body) |
| 60–65 | The drag bracket dominates … 6.9 / 23.1 / 2.9 / 8.1 … 2.8 and 2.4 … the thing the study has not measured… | **S10 — divided** (DeepSeek: body) |
| 66, 68, 69 | And the blade that is best … at both ends … a result of the closure | **J24** (69's tail *"reported because the opposite outcome would have been reported too"* → S10) |
| 67 | There was no reason to assume so… | S10 |
| 70 | The sizing above says nothing… | **J25** (verbatim) |
| 71 | The verdict comes first… two models… | **P26** (the lead-in *"The verdict comes first so that it cannot be missed"* → S10) |
| 72–73 | The first model is shown anyway… kinematically favourable… | S10 |
| 74–77 | Treating the aircraft as a point mass … slower loses less … 5 m s⁻¹ … 2 s and 5.1 s … T/W 1.066 to 1.00 … (reference geometry) … tip pairs need not lift | **R27** (slower-is-better, T/W range and the tip-pair clause → S10; the reference-geometry qualification becomes R27's first sentence and covers every transition figure) |
| 78–79 | The second model removes the result… cannot account for the trajectory… | S10 — **my least certain move**; see §5 |
| 80–81 | Solved instead with rotational dynamics … 5.4 m … (reference geometry) | **J28** (the parenthesis is carried by R27) |
| 81–82 | The loss is not an artefact of the controller … 17 m | **J29** (the three profile names and 17 m → S10) |
| 83 | What the kinematic model leaves out… | **D29b** — restored (Round 102: all four + Claude); its tail *"so tighter tracking … not closer"* → S10 |
| 84 | So the zero-altitude-loss result… | **P30** |
| 85–86 | What replaces it is not a prediction … the moment exists … ten degrees | **R31** (*"and for the published comparisons against which they were checked"* → S10; this narrows, it does not widen) |
| 87 | With a borrowed moment … | **J32** |
| 88 | That spread is itself the finding. | **P33** |
| 89 | What survives … within the finite-moment dynamic model… | **P34** (the lead-in → S10) |
| 90 | Whether a real aircraft loses 5.4 m… | **P35** |
| 91 | It establishes that the architecture is arithmetically self-consistent… | **D36** (*"with mass, power and range agreeing…"* → S10) |
| 92 | It does not establish that the package exists. | **P37** |
| 93 | The energy store this closure assumes… | **D38** (verbatim) |
| 94 | Nothing in this section should be read as a claim that the aircraft is buildable… | S10; carried by P2 and P37 |
| 95–97 | And these range figures … no multirotor or helicopter is sized … Section 13 | **R39** (*"multirotor or helicopter"* → *"rotorcraft"*, the vocabulary lock's family-level word) |

## 4. Numbers that leave Step 10's body (against `10-outbound-map.md`)

| Number | Leaves for S10 | Who else carries it | Status |
|---|---|---|---|
| 1.979 m² | yes | Step 8, with its own reason (the reference geometry) | safe |
| 2 s, 5.1 s | **no** — kept in R27 | Step 12 | safe |
| 1 000 kg | kept in R27 | Steps 6, 12 | safe |
| 0.0285, 0.0381, 0.632, 0.683 | kept | Steps 6, 11, 13 | safe |
| 8.79, 10.82, 52.3–57.5, 927–1 233, 3.54–5.17 | kept in the table | Steps 6, 11, 13, 14 | safe |
| MTOW^1.5 | yes | Step 2 (its own derivation); Step 14's 1.5 is kW/kg, a coincidence | safe |
| 17 m | yes | Step 13's 17 is an L/D, a coincidence | safe |
| 2.4 | yes | Steps 11 and 12 use 2.4 as a power ratio, a coincidence | safe |
| 9.9, 33.0, 46.1, 6.9, 23.1, 2.9, 8.1, 2.8 | yes | nowhere else | safe |
| 2.07–2.27 m², 3.53–3.70 m, 1.23–1.29 m, 7 %, 1.4 %, 34 %, 4–13 %, 1.066, 49.4, 11.88, 1 585 | yes | nowhere else | safe |

## 5. Where the draft is weakest, in my own view

- **(Round 103: resolved — restored by all five.)** **The mechanism of the verdict moved (sentences 79 and 83).** *"What the kinematic model leaves out is not the difficulty of
  turning the aircraft but the trajectory the aircraft flies while it is being turned."* No reader named it. It is the reason
  the two models differ, and a referee may ask for it. It costs about 45 words. I moved it for the budget; I am not sure I
  should have.
- **About 915 words is not the target.** It is 38 % of the source; Steps 10–13 must reach 19 % together. 204 words are protected, and
  most of the rest are the antecedents that protected sentences need to be read correctly.
