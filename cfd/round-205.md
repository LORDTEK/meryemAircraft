# Round 205 — The journal supplement continued: S5, S6 and S8, with two questions on the fairing chord

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text.

---

## A. Closed in Round 204 (all four, and me), and the author's decision

- **D33:** *"at the semi-span, 1.726 m, 2.43 times the pitch arm"*. Grok proposed the comma form; it keeps every attachment and avoids reading *"1.726 m:"* as a ratio. Applied, and checked in the output.
- **D55:** *"and the accounting, all of which Sections 5.1 and 5.2 describe"*. Grok proposed *"all of which"*; it states the scope over all three items. Applied, and checked in the output.
- **Renumbering:** the journal supplement is numbered S1–S11. ChatGPT's point is met by the provenance note on every passage and the map kept in the repository.
- **ChatGPT's rule:** *"A supplement passage may clarify or expose working already underlying the body pointer, but may not introduce a new substantive claim that the body itself does not make or promise."* Adopted.
- **P01–P07:** all graded R1. **S-64 and S-65:** accepted.
- **The author (E34):** approved the word change in the protected sentence: *"the isolation test **of Section 2.3** is what carries the prediction"*. Applied.
- **ChatGPT also graded P08 and P09** in Round 204, before those passages existed. P09 is composed below, so please grade it against the text. P08 belongs to S14, which comes later.

---

## B. The journal supplement: S5, S6 and S8, in full

The source is `paper/submission/supplement-src.md`. The conventions are the same as in Round 204:
- each passage carries its provenance (archive section and lines, and what changed);
- pointers stay in the assembled numbering, and the generator converts them;
- British spelling stays in the source, and the generator converts it.

`v8_stale.py` finds no retired phrase in this text.

**What you are asked to check:**
- Grade each receipt: **P09, P11, P12, P13, P14** (R1 faithful; R2 carried but qualified differently; R3 resolves with no content; R4 the body says more than the supplement establishes).
- Check each passage against ChatGPT's rule: does it add a claim the body does not make or promise?
- The flagged changes:
  - **S6, an addition:** the four blade families named, each with its cruise efficiency. The body says *"four nose-blade families"* and gives only the range. I reran the script that produces them this round (see the provenance note).
  - **S6:** *"across the same bracket"* becomes *"across its four closures"*. The two closed masses differ in blade as well as in drag, so *"the same bracket"* was too narrow.
  - **S8, the strip:** *"running 120 % of root chord"* becomes an explicit spanwise extent, which is how the roll script uses it. The protected sentence *"What declining it costs is not counted in this work."* is carried with the sentence before it, which gives its *"it"* a referent.
  - **S8, the fairing:** the working is set out from the script, rerun this round. Two questions follow in §C.

**Sources opened this round:**
- **Johnson and Silva, Table 3.** It is on **p. 70**, not p. 71 as I wrote in Round 204. See §E. The six rotorcraft design gross weights run from 3,665 lb to 7,221 lb, which is 1,662 kg to 3,275 kg.
- **NACA Report 796, p. 428.** The quotation is verbatim. The paragraph around it is recorded in the provenance note.

**The draft:**

### S5. The landing transition: working for Section 3

> *Provenance and changes:* for P09: "… the landing transition is not the take-off transition run backwards, and no figure in this paper describes it (Supplement S5)". src: paper/v8/supplement.md, "Section 5 as it stood before the length pass", paragraph "Neither has the landing transition." (L1630-L1636). Changes: the lead "Neither has the landing transition." dropped (the heading carries it); bold removed; the closing clause shortened, since the body already says no figure describes it. No number.

The forward rotation and the reverse are not symmetric and must not be assumed to be. Going out, the rotation builds dynamic pressure while it turns, so lift arrives to replace the vertical component of thrust as that component falls. Coming back, the race runs backwards: dynamic pressure is falling while the aircraft is being turned, so lift is leaving at the moment the thrust vector has not yet returned to vertical. A model built for the first case cannot be read for the second by changing a sign, and no figure in this paper describes the second.

### S6. The cruise-efficiency comparison: working for Section 4

#### The blade families

> *Provenance and changes:* for P11: "Which blade a designer would choose also turns on structural loads, acoustics, the motor operating point, rotor inertia and manufacture, none of which is modelled in this work (Supplement S6)". src: paper/v8/supplement.md, "Section 6 as it stood before the length pass" (L1830-L1833 and L1856-L1861). Protected S6 row (E13) carried verbatim. Added (working under the body's "four nose-blade families", Section 6.1): the family definitions and each family's efficiency, from aero/nose-propeller-crossing.txt (aero/nose_propeller_crossing.py, rerun this round). "Section 10 is where …" -> Section 6.1.

The four nose-blade families are two and three blades per rotor, each designed at two target section lift coefficients, 0.55 and 0.70, and each solved at its hover and its cruise condition by blade-element momentum theory. Their cruise propeller efficiencies are 0.648 and 0.683 with two blades and 0.632 and 0.643 with three, at the lower and the higher section lift coefficient respectively. Whether 0.683 is the blade a designer would actually choose is not settled here. It is the best of the four on cruise efficiency under the hover figure-of-merit constraint. Blade count and section loading also govern structural loads, acoustics, the motor operating point, rotor inertia and manufacture, and none of those is modelled in this work. Section 6.1 is where one blade is carried into a closed sizing loop.

#### The compared vehicles

> *Provenance and changes:* for P12: "The compared vehicles are larger than both designs studied here, which are of order 50 kg and 1 000 kg (Supplement S6)". src: paper/v8/supplement.md L1906-L1908 (protected S6 row E13 carried verbatim: "The compared vehicles are 1 660 to 3 275 kg"). Checked this round against Johnson & Silva [16], Table 3, p. 70: rotorcraft design gross weights QSMR 3,951 / 5,980 lb, side-by-side 3,665 / 5,547 lb, quadrotor 3,678 / 7,221 lb; 3,665 lb = 1,662 kg, 7,221 lb = 3,275 kg. Closed masses 52.3 and 57.5 kg: body Section 6.1 table. Change: "across the same bracket" -> "across its four closures" (52.3 kg is closure D, 57.5 kg closure A; they differ in blade as well as drag).

The compared vehicles are 1 660 to 3 275 kg: the six rotorcraft entries of the NASA sizing set [16] have design gross weights from 3 665 lb (the turboshaft side-by-side helicopter) to 7 221 lb (the all-electric quadrotor). The designs here are of order 50 kg and 1 000 kg, and Section 6.1 closes the 50 kg design between 52.3 and 57.5 kg across its four closures.

### S8. The strip and the fairing: working for Section 5.2

#### The strip's geometry

> *Provenance and changes:* for P13: "Roll comes instead from a strip on the lower surface (its geometry is in Supplement S8)". src: paper/v8/supplement.md, "Section 8's paragraphs as they stood before the Round 170 shortening" (L2736). Protected S8 row (E14) carried verbatim with the sentence that gives its "it" a referent. Geometry checked this round against aero/roll.py L55-L57 (SERIT_UZUNLUK = 1.20 x root chord, SERIT_H_IC/DIS = 0.02/0.06 m, SERIT_ACI = 45 deg in planform) and aero/planform.py (root chord 0.97 m); the strip runs from y = 0 to 1.164 m, 1.164 / 1.726 = 67 percent of the semi-span. Change: "running 120 % of root chord" made explicit as a spanwise extent, which is how aero/roll.py uses it.

The reaction-torque channel is declined: every pair is operated torque-balanced, so no reaction torque is spent on control. What declining it costs is not counted in this work. The strip lies on the lower surface, inclined at 45° in planform, and runs outboard from the centreline over a spanwise extent of 120 percent of the root chord (1.164 m against a root chord of 0.97 m), so that it reaches 67 percent of the 1.726 m semi-span. Fully extended it stands 2 cm proud of the surface at its inboard end and 6 cm at its outboard end; extension scales that height.

#### The fairing chord

> *Provenance and changes:* for P14: "… sized against the criterion the tailless literature recommends it needs a chord of 39 mm, less than a 20 mm faired strut carries in any case (Supplement S8)". src: paper/v8/supplement.md L2569-L2575 ("What meets the ground"); working from aero/yaw.py, rerun this round: vortex-lattice planform alone C_n_beta = +0.00000 /rad; frame mid-chord arm 0.879 m aft of the CG; required side area C_n_beta S b / (a_f l_f) for both frames; frame length 2 x 0.71 = 1.42 m each, 2.84 m both; chord = area / 2.84 m: a_f = 3.0 -> 52 mm, 4.0 -> 39 mm, 5.0 -> 31 mm. Quotation checked this round: references/NACA-TR-796_…pdf, p. 428 ("… is usually greater than 0.001 per degree"). The source's own discussion (same column): models flew at one-third of that value, best flying qualities above it; and for fins at the wing tips "the drag characteristics as well as the lift characteristics of the tip fins exert an influence on the directional stability". The 39 mm counts lift only. Whether the supplement quotes that is put to the readers (Round 205). The 50 to 70 mm is a design assumption, not sourced.

The planform alone supplies no directional stability: a vortex-lattice solution of the planform without the frames returns a directional-stability derivative of zero, as a planar surface with nothing standing out of its plane should. The fairing on the tip frames therefore supplies all of it. The criterion is the value recommended for conventional airplanes, which the tailless literature applies to tailless ones: a directional-stability parameter *"usually greater than 0.001 per degree"* [24], 0.0573 per radian. With the frames' mid-chord 0.879 m aft of the centre of gravity, the side area required is C_nβ S b/(a_f l_f), where S and b are the reference area and span, l_f the arm and a_f the lateral lift-curve slope of the faired frame. Taken over the combined frame length of 2.84 m (two frames, each projecting 0.71 m on both sides of the planform), that area is a chord of 39 mm at an assumed a_f of 4.0 per radian, and 52 mm and 31 mm at 3.0 and 5.0. A 20 mm thick faired strut is taken to have a chord of 50 to 70 mm, a fineness ratio of 2.5 to 3.5 assumed here rather than sourced.


---

## C. Two questions on the fairing chord (new; your views first, mine next round)

**C1. The source's own qualification.** NACA Report 796 gives the 0.001 per degree criterion. The same column of p. 428 also says:
- models have been flown with one-third of that value, but the best flying qualities came above it;
- for fins at the wing tips, *"the drag characteristics as well as the lift characteristics of the tip fins exert an influence on the directional stability"*.

Our frames stand at the wing tips. The 39 mm counts only the frames' side force (lift); it does not count their drag. Under the Round 94 rule, a qualification found in an opened source is either quoted or recorded as omitted, with the reason. The options:
- (a) S8 quotes the tip-fin sentence and states that the 39 mm counts lift only;
- (b) the qualification is recorded in the evidence file as omitted, with the reason;
- (c) another form.

**C2. The body's comparison and the assumed slope.** The body says the fairing *"needs a chord of 39 mm, less than a 20 mm faired strut carries in any case"*. Rerunning the script shows that the 39 mm rests on an assumed lateral lift-curve slope of 4.0 per radian. The script also tabulates 3.0 and 5.0:

| Slope | Chord |
|---:|---:|
| 3.0 per radian | 52 mm |
| 4.0 per radian | 39 mm |
| 5.0 per radian | 31 mm |

The 50 to 70 mm for a 20 mm strut is a design assumption, not a sourced figure. At 3.0 the required chord falls *inside* that range, not below it.
- Is the body's *"less than … in any case"* an R4 (the body says more than the supplement establishes)? If it is, this is a candidate source defect, **S-66**.
- The options:
  - (a) the body keeps its sentence, and S8 shows the sensitivity (as drafted);
  - (b) the body sentence changes, for example to *"within what a 20 mm faired strut carries in any case"*, and names the slope as assumed;
  - (c) another form.

The body sentence is not protected. **Directional stability still asks for no new surface at any of the three slopes**: in every case the chord is that of a fairing on a frame that is already there.

---

## D. Your own proposals

Open, as always.

---

## E. Errors (one list)

- **Claude:** in Round 204 I cited Johnson and Silva's Table 3 as *"p. 71"*, both in the S4 provenance note and in the S-64 row. **It is p. 70** (PDF page 12); p. 71 holds Fig. 6 and the vehicle descriptions. The numbers are unaffected. Corrected in both places.
- **Claude, an observation parked under F-1 (not a defect in the body):** the roll script integrates the strip's area over its **spanwise extent** (1.164 m), while the strip lies at 45° in planform, so its length along itself is longer. No body sentence gives a strip force or a roll moment, so no body number depends on it. The observation is recorded in `paper/v8-parking.md` and not recomputed.
- **Readers:** none found in Round 204.

---

## F. What goes to the author

**Nothing this round.** C2 goes to the author only if you propose changing the body sentence and do not converge.
