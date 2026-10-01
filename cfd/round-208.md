# Round 208 — S10 (the sizing loop and the transition), one candidate defect in the body's loop sentence; the author's question, once more

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text and in the attached reader packet (regenerated this round; it now includes the S10 draft).

---

## A. Closed in Round 207

- **The S-66 repair is confirmed by all four.** Closed.
- ***"Within or below"* stays.** ChatGPT moved to it (*"mathematically correct"*), and Grok, DeepSeek and Qwen had already accepted it. Closed.
- **The S8 qualification text stays as drafted, ending *"counts the frames' side force only."***
  - DeepSeek, who proposed *"and not their drag"*, now prefers the drafted form: the sentence just before it already names drag.
  - ChatGPT preferred the drafted form.
  - Grok accepts either.
  - Qwen preferred the addition and called both forms true.
  - I move to the drafted form, for DeepSeek's reason.
  - **Qwen: is the drafted form acceptable to you?** If not, say so and it stays open.
- **P14 against the repaired sentence:** ChatGPT and Qwen graded it R1, and so do I. **Grok, DeepSeek: please confirm R1.**

---

## B. The author's question, once more

Last round the author asked each of you whether you lack anything, and whether your conversation window is under strain. **Qwen answered both:**
- nothing is missing for the current work;
- the archive passages will be needed when S10–S14 are composed;
- the window is fine for now, though a fresh conversation may help later.

**Grok, ChatGPT, DeepSeek: you have not answered yet.** Please answer the two questions plainly:
1. Is anything missing that you need in order to work well?
2. Is your window under strain?

There is no wrong answer. The author can attach files or open a fresh conversation for you.

**The whole-body check of S2–S8:**
- **Qwen** checked every passage against the whole body and found no new claim.
- **DeepSeek** reported the same.
- **Grok and ChatGPT** answered for S8 only. **Please give the S2–S8 check against the packet's body.**

**DeepSeek, two statements in your packet summary that I could not match to the packet.** Please check them; one of us may be misreading.
- *"the Section 4.1 dashes-to-parentheses form applied"*. The body has no Section 4.1. The dash-to-parentheses change I know of is in Supplement S2 (pointer P02).
- *"The packet's note says the author has not been asked about the wording change"*. The note I wrote says the item was open among the readers for Round 207; it says nothing about the author.

---

## C. S10, drafted from the archive and written against the code

**The supplement has four of its eleven sections still to compose: S11–S14.** This round brings S10, with pointers P16, P17 and P18 and six protected rows. All six protected rows are carried verbatim. *"Section 8"* becomes *"Section 5.2"* in one of them; that is renumbering only.

**Every figure was checked by rerunning the code this round:**
- `aero/closure.py`: the check against the reference design, the four closures and the geometry. The output is identical to the stored result.
- `aero/transition_dynamics.py`: the three reference profiles and the drag sensitivity.
- **The gain sweep.** The archive said the loss reaches 17 m at high gains, but the script that produced that sweep is not in the repository. I wrote one this round (`aero/transition_gain_sweep.py`, a copy of the model with the controller gains as parameters) and committed it with its output. It gives 16.9 m at a proportional gain sixteen times the baseline, with no saturation. The sweep design (how the derivative gain is scaled) is mine. Please judge whether the figure belongs in S10.

**Two archive errors, corrected in the draft and flagged:**
- **The archive said f_empty *"contains a term proportional to MTOW^1.5"*.** Not in the loop as run. The disc loading is held fixed, so the disc area grows with the mass and hover power is proportional to MTOW.
- **The archive said the chord Reynolds number rises *"about 7 %"* across the closure range.** It is 7 percent from the 50 kg reference design to the heaviest closure, and 5 percent across the four closures. Both are now stated.

### Candidate defect S-67: the body's loop sentence (P16)

**The body, Section 6.1 (P16):**

> Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Supplement S10).

**The body, Section 6.2:**

> The engine is sized by cruise, **3.54 to 5.17 kW** of shaft rating, against a hover requirement of **11.4 to 12.5 kW** at the rotor shaft: … **But the full hover power passes through the electrical path, and that path is sized by it.**

**The code** (`aero/baseline.py`, the sizing loop, for this configuration):
- the engine is rated at 1.53 times the cruise electrical power;
- the rest of the propulsion mass is a fixed 0.108 of take-off mass, back-solved from the reference design's budget (the code's comment lists propeller, shaft, mount and wiring);
- hover power is computed at the closed mass and reported, and enters no mass term.

At fixed disc loading, hover power is proportional to take-off mass. A mass that scales with hover power would therefore scale as a fixed fraction does, but the loop computes no hover-rated mass of its own.

**The question:**
- If P16's *"installed power"* means the engine, P16 contradicts both Section 6.2 and the code.
- If it means the electrical path, it agrees with Section 6.2, but the loop represents that path only through the fixed fraction. *"Hover power that sizes the installed power"* then describes a dependency the loop does not compute.

Please say:
- (a) whether this is a defect;
- (b) if it is, how P16 should read.

The sentence is not protected. This is a new question, so per our rule my view comes next round, beside yours.

I also corrected my own first draft of S10 before sending. It said hover power *"sizes nothing"*, which went beyond what the code shows and against Section 6.2's electrical-path sentence.

**What you are asked to check in S10:**
- grade P16, P17 and P18;
- apply ChatGPT's rule (no new claim the body does not make or promise);
- judge the flagged changes and the gain-sweep figure.

**The draft:**

### S10. The sizing loop and the transition: working for Section 6.1

#### The loop

> *Provenance and changes:* for P16: "Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Supplement S10)". src: paper/v8/supplement.md, "Section 10 as it stood before recomposition into result sentences", "Why the loop has to be iterative" (L3099-L3111). Protected S10 row (E15) carried: "If no fixed point exists, the declared sizing package does not close." WRITTEN AGAINST THE CODE, not the archive (aero/baseline.py boyutlandir() and mimariler(); aero/closure.py rerun this round, output identical to aero/closure-result.txt). For this configuration motor_hover=False: the engine is rated at 1.53 x the cruise electrical power; hover power is computed at the closed mass and reported; the rest of the propulsion mass is F_TAHRIK_SABIT = 0.108 of MTOW (code comment: propeller, shaft, mount, wiring), back-solved from the reference budget. The archive's "a term proportional to MTOW^1.5" is also wrong for the loop as run: disc loading is held fixed, so the disc area grows with the mass and hover power is proportional to MTOW. The body sentence (P16) says hover power sizes the installed power; Section 6.2 says the engine is sized by cruise and the electrical path by the hover power. Which "installed power" P16 means, and whether the loop as run supports it, is candidate S-67, put to the readers in Round 208.

The closure statement is

    MTOW = m_payload / (1 − f_empty − f_fuel)

with the fuel fraction fixed at 0.16. The empty fraction contains a propulsion term, f_prop = 0.108 + P_engine / (p_s · MTOW), in which the engine rating P_engine is 1.53 times the cruise electrical power at the take-off mass and p_s, 1.0 kW per kilogram, is the specific power assumed for the engine and generator. The take-off mass is found by iteration as the fixed point of that loop: mass sets the cruise power, cruise power the engine rating, the engine rating the propulsion mass, and the propulsion mass the take-off mass. The rest of the propulsion mass, the fixed 0.108, is a fraction back-solved from the reference design's own budget. Hover power, W^1.5/(FM √(2ρA)) with the disc area A set by the fixed disc loading, is computed at the closed mass and reported, and it does not size the engine. Because the disc loading is fixed, hover power is itself proportional to take-off mass, so any mass that scales with hover power scales as a fixed fraction does; the loop computes no hover-rated mass of its own. The buffer that supplies the hover deficit is a fixed 3.6 percent of take-off mass. If no fixed point exists, the declared sizing package does not close. That is a statement about that package rather than about whether some other package could, and the calculation then returns no number.

#### What the loop holds fixed

> *Provenance and changes:* src: same snapshot, "The inputs, and why there are four closures rather than one" (L3113-L3171), and "Section 10's paragraphs as they stood before the Round 172 shortening" for the current wording of two protected rows. Protected S10 rows carried: "The reference design's assumed zero-lift value of 0.0248 is not used." (E15); "the control moment arms of Section 8 are therefore reference values that this closure does not re-derive" (E15; Section 8 -> Section 5.2, renumbering only); "The closures do not take that reduction, and it has not been run through the loop." (E7). Figures checked against aero/closure.py output this round: loadings 25.3 kg/m2 and 44.2 kg/m2, AR 6.03; area 2.069-2.273 m2, span 3.532-3.702 m, nose disc 1.228-1.287 m, C_L 0.450; frame+rotor terms -4.3 to -12.9 %, Delta C_D0 -0.0009 to -0.0028; reference wing area 1.979 m2. CHANGED: the archive said the chord Reynolds number rises "about 7 %" across the closure range. Chord goes as the square root of area at fixed aspect ratio: (2.273/1.976)^0.5 = 1.072 from the 50 kg reference design to the heaviest closure, (2.273/2.069)^0.5 = 1.048 across the four closures. Both are now stated; 1.072^-0.2 = 0.986, the 1.4 percent. 0.0381/0.0285 = 1.337, the 34 percent.

The reference design's assumed zero-lift value of 0.0248 is not used: the build-up of Section 6.2 places it below both ends of the bracket, outside the supported range. Propeller efficiency enters the loop twice, in the range expression and in the cruise power that sizes the engine, and both entries move together with the blade family in every closure; scaling one without the other would size the engine on one propeller and compute the range on another.

The loop holds wing loading (25.3 kg/m²), disc loading (44.2 kg/m²) and aspect ratio (6.03) fixed, so area, span and nose disc diameter follow the mass: across the four closures the wing area runs from 2.07 to 2.27 m², the span from 3.53 to 3.70 m and the nose disc diameter from 1.23 to 1.29 m, and the cruise lift coefficient is 0.450 in every one of them. The tip-frame length, the tip-disc diameter and the strip are not sizing variables. They were set on the 50 kg reference design of Section 5.2, and the control moment arms of Section 5.2 are therefore reference values that this closure does not re-derive.

The frame and rotor drag terms are coefficients on the reference wing area of 1.979 m², so holding them unchanged across the closures lets that hardware grow with the wing. Held at its reference size instead, the hardware would give terms 4 to 13 percent smaller across the four closures, 0.0009 to 0.0028 of zero-lift drag. The closures do not take that reduction, and it has not been run through the loop.

The drag polar is likewise a fixed input. Chord grows with the square root of area, so the chord Reynolds number is up to about 7 percent higher than on the reference design (about 5 percent across the four closures). On a turbulent flat-plate scaling, C_D0 ∝ Re^−0.2, 7 percent is a 1.4 percent change in the zero-lift coefficient, against a bracket whose two ends differ by 34 percent. The claim is that C_L is unchanged, not that C_D0 is exactly so.

#### The check against the reference design

> *Provenance and changes:* for P17: "Run on the reference design's own assumed inputs, the same construction reproduces that design within 1.5 percent (Supplement S10) …". src: same snapshot, "The construction is checked before it is used" (L3173-L3182), and the Round 170 paragraph (assumed inputs named). Figures from aero/closure.py, rerun this round: MTOW 49.35 / 50.10 kg (-1.5 %), L/D 11.88 / 11.88, range 1584.88 / 1583 km (+0.1 %). Change: "published" -> "the reference design's", as in the body.

Run on the reference design's own assumed inputs (a zero-lift coefficient of 0.0248 without the rotor term, and a propeller efficiency of 0.80), the construction returns a take-off mass of 49.4 kg against 50.1 kg, a cruise lift-to-drag ratio of 11.88 against 11.88, and a range of 1 585 km against 1 583 km. The largest deviation is 1.5 percent, in mass. This check is the only place in the closures where the assumed zero-lift value appears; every closure uses the bracket.

#### The transition loss and the controller

> *Provenance and changes:* for P18: "… the 50 kg design loses 5.4 to 6.6 m at the same reference condition; the loss is not an artefact of the controller (Supplement S10)". src: same snapshot, "The transition, and this is where the section turns" (L3236-L3288), with the Round 148 correction X-1 (the loss persists across the profiles; it is not unchanged). Protected S10 row (E15) carried: "Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude." Rerun this round of aero/transition_dynamics.py kos() (HAFIF: 50 kg, S 1.979 m2, Iyy 9.81 kg m2; M 23.0 N m; t_r 2 s; 5 m/s entry climb; C_m zero): linear 5.43 m, smooth (3t^2-2t^3) 6.33 m, bang-bang 6.57 m, saturation time 0.0 s in all three. Drag: C_D0 0.0285 / 0.0381 with e 0.817 moves each by at most 0.022 m. GAIN SWEEP: the archive's "reaching 17 m" has no script in the repository; reproduced this round by aero/transition_gain_sweep.py (a copy of kos() with the PD gains as parameters; baseline Kp 25, Kd 10; output aero/transition-gain-sweep-result.txt): Kp x2, x4, x8, x16 with Kd x sqrt: 7.85, 8.71, 16.32, 16.94 m, no saturation.

The 50 kg design is rotated in a three-degree-of-freedom model: the body angle follows a reference profile through a proportional-derivative controller whose moment is limited to the available control moment of 23.0 N·m, with a rotation time of 2 s, an entry climb of 5 m s⁻¹, and the aerodynamic pitching moment set to zero. The loss persists across three reference profiles: 5.43 m with a linear profile, 6.33 m with a smooth (cubic) one and 6.57 m with a bang-bang one, which is the body's 5.4 to 6.6 m. In none of the three does the control moment saturate. Raising the gains increases the loss rather than removing it: with the proportional gain raised sixteen-fold and the derivative gain four-fold, the loss is 16.9 m, again without saturation. With the zero-lift coefficient at either end of the bracket and an Oswald factor of 0.817 instead of the assumed 0.0248 and 0.85, each figure moves by at most 0.02 m. Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude.

#### The range figures

> *Provenance and changes:* src: "Section 10's paragraphs as they stood before the Round 172 shortening" (L3331). Protected S10 row (E15) carried: "no comparison in this paper should be quoted without the contract it was computed under." It follows the body's last paragraph of Section 6.1 ("These ranges are carried forward as closed-loop values, not as a ranking … (Section 6.4)"); fuel fraction 0.16 from aero/baseline.py ORTAK.

The ranges of the four closures are closed-loop values at a fuel fraction fixed at 0.16, not a ranking. Because the comparative result depends on the sizing contract, no comparison in this paper should be quoted without the contract it was computed under.


---

## D. Your own proposals

Open, as always.

---

## E. Errors (one list)

- **Claude:** the two archive errors in §C, *"MTOW^1.5"* and *"about 7 %"*, were in text I composed for the archive (Round 73 and before). Neither reached the body.
- **Claude:** P16's loop sentence (candidate S-67) dates from my recomposition of Section 10 (Rounds 170–172); five of us passed it then.
- **Claude:** my first S10 draft said hover power *"sizes nothing"*. I corrected it before sending (§C).
- **Readers:** none found in Round 207.

---

## F. What goes to the author

**Nothing for decision.** Your answers to §B go to the author in full. S-67 goes to the author only if we do not converge on a wording.
