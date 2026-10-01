# Round 211 — Q-210: the Bill 3 sentence is protected (my error); S12 (scale) drafted

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text, including Section 6.3 in full.

---

## A. Closed in Round 210 (all four, and me)

- **S-67 result confirmed; P16: R1.** Closed.
- **S11: P15, P19, P20, P21: R1.** Closed.
- **The three flagged S11 changes are accepted:** the reordering, the archive correction (no loop term scales with hover power), and the absolute counts left out.

---

## B. Q-210 (P22), with a correction from me first

**My error.** In Round 210 I wrote that the Bill 3 sentence *"is not protected"*. **It is protected.** The register (`paper/v8-caveats.md`, Section 6.2 row) holds *"Bill 3 is removed from the engine and left standing on the electrical system."* So:
- **Its words cannot change except by the author's decision.** That applies to Qwen's form, which rewrites it, and to any clause inserted into it.
- **A new sentence placed after it, or a change to the pointer in brackets, does not touch its words.** It needs the five of us, not the author.

I did not check the register before writing *"not protected"*. That is the first rule of this stage.

**The body, Section 6.2** (the protected sentence is the second one):

> **But the full hover power passes through the electrical path, and that path is sized by it.** **Bill 3 is removed from the engine and left standing on the electrical system** (the propulsion-mass split is in Supplement S11).

| Reader | Grade | Proposal | Reading against the protection and the working |
|---|---|---|---|
| **Grok** | R4 | Change only the pointer: *"(Supplement S11 gives the propulsion-mass split; the loop computes no hover-rated mass for that path)"* | Leaves the protected words unchanged. States the limit, and makes no identification of a fraction with the path. |
| **ChatGPT** | R1 | No change. A more specific claim about which fraction is *"electrical"* would recreate the over-reading S-67 removed. | The warning is right, and it applies to any form that names a fraction as the path. Grok's form and mine do not name one. |
| **DeepSeek** | R4 | Repair 1: append *"; the electrical path itself is a physical attribution, not a term the loop computes."* Repair 2: delete the pointer and add a separate sentence, *"The loop computes no hover-rated mass for the electrical path; the path's share of the propulsion mass is inside the fixed fraction and scales with take-off mass."* | Repair 1 extends the protected sentence with a clause, so it goes to the author. *"The electrical path … is a physical attribution"* also calls the path an attribution; the attribution is the sentence about the path. Repair 2's second clause says the path's share *"is inside the fixed fraction"*. That is the identification no line of the code makes. |
| **Qwen** | R4 | Rewrite: *"Bill 3 is removed from the engine; the loop absorbs the electrical path into a fixed propulsion fraction rather than sizing it explicitly (…)"* | It changes protected words, so it goes to the author. It also identifies the path with the fixed fraction (*"absorbs … into"*), the step Grok withdrew in Round 209. |
| **Claude** | **R2**: the pointer delivers the split, but the split carries a qualification the body sentence does not state | **Keep the protected sentence and its pointer as they are, and add one sentence after them:** *"The sizing loop computes no hover-rated mass for the electrical path."* | The protected words are untouched. The limit moves into the body, where a reader of the body alone needs it. Nothing is said about which fraction the path occupies. Grok's pointer form is equivalent and also acceptable to me; it is a pointer change only, so the protected words are untouched either way. |

**Please:**
- answer each other's readings, mine included;
- say whether P22 needs any change, and if it does, which form;
- if the choice is between a pointer change (Grok) and an added sentence (Claude), say which.

Forms that change the protected words (DeepSeek's Repair 1, Qwen's) can go to the author only if the five of us prefer them.

---

## C. S12, drafted

S12 serves two pointers: P24 (the reference pair) and P25 (the buffer figures are inputs). It carries five protected rows. Every figure was checked against the code and its output this round, except the archive's transition powers, which are flagged below.

**Flagged changes:**
- **The 5 to 14 percent is now shown as arithmetic.** The heavy design's Bill 3 ratio under the light design's engine margin is 3.61.
- **The archive's *"three other candidates are excluded"* now names them, and the count word is dropped.** The candidates are solidity, dynamic pressure, and the shared tip speed and hub fraction.
- **The rotation time: a question for you.**
  - The archive gave the transition power as *"about 220 kW … about 13 kW"*. I could not reproduce that exactly: no script was found, and a momentum-power estimate from the moments gives about 200 kW and 12 kW.
  - I replaced it with figures `aero/rotation.py` prints: an inertia ratio of 255, a moment ratio of 41, and 4.96 s to keep the light design's margin.
  - **The subsection has no body pointer.** It is in S12 only because the author moved a protected row there (E15: *"A larger aircraft of this type turns more slowly, and must."*). Under ChatGPT's rule (no new claim the body does not make or promise), should it stay?

**What you are asked to check:**
- grade P24 and P25;
- apply ChatGPT's rule;
- judge the flagged changes and the rotation-time question.

### Section 6.3, in full

#### 6.3 Scale does not lock two of the charges together; the third is not tested

Section 6.2 decomposed the three charges on one aircraft, at one size; **this section asks whether they are three quantities or
one quantity under three names**, by changing the size of the aircraft and seeing whether they move together. **The test is deliberately weak**: it can show that two charges are not locked together within this
model; **it cannot show that they are independent in general.**

**The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 6.1's closures** (Supplement S12).

**Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its light-design value in the section
polars used here, while the Bill 3 ratio changes by 5 to 14 percent.** **Within this model, the two are therefore
not one quantity under two names.**

Within the
blade-element and section-polar model the section Reynolds number accounts for the fall, a decomposition inside the model rather than
a causal claim beyond it, and the light end lies below a Reynolds number of 10⁵, where section drag is hardest to predict. **Of the two
rotor terms, the light one is therefore the less certain — and it is the one Sections 6.1 and 6.2 carry.**

**Bill 1 is not tested.** It appears here as the energy buffer, 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and both figures are inputs (Supplement S12). Whether it is separable from Bill 3 here is not established;
that the two are coupled here is Section 2.2's claim, and coupling is not identity.

**The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low
Reynolds number.** **It is consistent with the separability Section 2.1 asserts; it is not a verification of separability as a general
property.**

**Because at least two of the charges are not locked together, a comparison of architectures cannot in general be reduced to a number
that does not depend on how the charges are weighed.** Section 6.4 examines what the choice of sizing contract does to a ranking, on the
light closures of Section 6.1 only.


### The draft

### S12. Scale: working for Section 6.3

#### The reference pair

> *Provenance and changes:* for P24 (Section 6.3): "The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 6.1's closures (Supplement S12)". src: paper/v8/supplement.md, "Section 12 as it stood before the supplement move (complete)" (archive S12, the moved working of Round 155). Protected S12 rows carried: "That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3." (E15); "This paragraph compares the reference pair only." (E10); "Much above 1 000 kg a single nose pair can no longer hold" (E15). Figures checked this round: 10.9 / 2.6 = 4.19 and 216.2 / 54.3 = 3.98 (the reference designs' own figures, aero/baseline.py comments and agir_dogrula(); paper/v8-evidence.md row "4,19 / 3,98"); engine margins 2.6 / 1.7 = 1.53 and 54.3 / 39.2 = 1.39 (aero/baseline.py); 216.2 / (39.2 x 1.53) = 3.61, (4.19 - 3.61) / 4.19 = 14 percent, (4.19 - 3.98) / 4.19 = 5 percent; disc loading 50 / (pi 0.6^2) = 44.2 and 1000 / (pi 2.7^2) = 43.7 kg/m2; 10.9 / 50 = 0.218 and 216.2 / 1000 = 0.216 kW/kg; diameter / span 1.2 / 3.452 = 0.35 and 5.4 / (6.0 x 22.24)^0.5 = 0.47. ADDED: the heavy ratio under the light design's margin (3.61), which is the arithmetic behind the archive's "5 to 14 percent".

The test uses the 50 kg and 1 000 kg reference designs, sized by one method. No closure of Section 6.1 was run at 1 000 kg: the heavy design has no drag bracket and no structural closure, and no heavy-design range is quoted.

Disc loading is held at approximately the same value, 44.2 kg m⁻² at 50 kg and 43.7 at 1 000 kg, so specific hover power is held with it: 0.218 kW kg⁻¹ at the light design and 0.216 at the heavy. That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3. Section 6.2's measure of Bill 3, rotor-shaft hover power over engine shaft rating, is 4.19 at the light design (10.9 kW over 2.6 kW) and 3.98 at the heavy (216.2 kW over 54.3 kW). The two designs rate their engines at different margins over cruise power, 1.53 and 1.39; with the light design's margin, the heavy ratio would be 3.61. The ratio therefore moves by 5 to 14 percent across the factor of twenty, depending on an engine margin the sizing rule does not set. Section 6.2's 2.4 to 3.2 is the same ratio at the four closures. This paragraph compares the reference pair only.

The rule has a price, paid in geometry: the ratio of nose-propeller diameter to span rises from 0.35 to 0.47, and much above 1 000 kg a single nose pair can no longer hold the disc loading, so a second would have to be added.

#### The rotor term of Bill 2

> *Provenance and changes:* for P24 (the comparison's Bill 2 side; the body's "falls to between 0.29 and 0.65 … in the section polars used here" and its Reynolds-number sentence). src: same archive snapshot, "Bill 2 — the rotor term falls" paragraph. Figures from aero/heavy_rotor.py (corrected setup, Round 55), stored output aero/heavy-rotor-result.txt, rerun this round: eight designs c_l 0.55-0.85, all FM >= 0.599, dC_D0 0.00447-0.01003, ratio to 0.01535 = 0.29-0.65; c_l 0.68: 0.00681; median section Re 81 689 -> 556 336; heavy blade at the light Re: 0.01810 = 1.18 x; solidity 0.0754 -> 0.0999 (x 1.33); q test 0.00748 at 30 m/s, 0.00681 at 40 m/s (0.911, against 1/1.778 = 0.562); tip speed 210 m/s and hub 15 percent of radius at both sizes. CHANGED: the archive's "three other candidates are excluded" now names them; the count word is dropped (the list has solidity, dynamic pressure, and the shared tip speed and hub fraction).

Only the rotor term of Bill 2 is computed at both sizes; the frame term enters both designs as the same multiplier, so it cannot show a scale effect in either direction. At 50 kg the rotor term is 0.0154. At 1 000 kg, eight tip-rotor designs at section lift coefficients from 0.55 to 0.85, all meeting the hover figure of merit, give 0.0045 to 0.0100, that is 0.29 to 0.65 of the light value; the design at the light design's section lift coefficient, 0.68, gives 0.0068. Within the blade-element and section-polar model the section Reynolds number accounts for the fall: the median section Reynolds number rises from about 8.2 × 10⁴ to 5.6 × 10⁵, and the heavy blade brought down to the light design's Reynolds number gives 0.0181, 1.18 times the light value. The other candidates are excluded. The heavy blade is the more solid (1.33 times), which would raise its drag rather than lower it; dynamic pressure cancels (between 30 and 40 m s⁻¹ the heavy term changes by a factor of 0.911, against the 0.562 a dynamic-pressure effect would give); and the design tip speed (210 m s⁻¹) and the hub fraction (15 percent of radius) are the same at both sizes. This is a decomposition inside the model rather than a causal claim beyond it.

#### Bill 1

> *Provenance and changes:* for P25 (Section 6.3): "It appears here as the energy buffer, 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and both figures are inputs (Supplement S12)". src: same archive snapshot, "Bill 1 — not tested". Protected S12 row (E15) carried: "A change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction." Inputs checked: light closures f_tampon 0.036 (aero/closure.py), heavy design f_tampon 0.04 (aero/baseline.py mimariler() default, agir_dogrula()).

Both buffer figures are inputs: 0.036 of take-off mass in the light closures and 0.040 in the heavy design's sizing. A change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction. A buffer sized to the hover deficit at the same specific power would track hover power and engine rating, which are the Bill 3 measures, so that derivation cannot test whether Bill 1 separates.

#### The rotation time

> *Provenance and changes:* No body pointer: carried because the protected row was moved here by the author's decision (E15): "A larger aircraft of this type turns more slowly, and must." src: same archive snapshot, "Two costs that scale does not relieve". CHANGED: the archive's "about 220 kW … about 13 kW" could not be reproduced exactly (no script found; a momentum-power estimate from aero/rotation.py's moments gives about 200 kW and 12 kW). Replaced by figures aero/rotation.py prints, rerun this round: pitch inertia 9.813 and 2503 kg m2 (ratio 255.1), available moment 23.0 and 952 N m (ratio 41.4), rotation time that keeps the light design's moment margin 4.96 s, the heavy design's 5.1 s. Put to the readers in Round 211: whether this subsection stays (it carries a protected row the body does not point to).

The transition is where the square–cube relation is paid. The heavy design's pitch inertia is 255 times the light design's and its available control moment 41 times, so to keep the light design's moment margin it must rotate in about 5 s rather than 2 s (4.96 s computed; the heavy design uses 5.1 s). A larger aircraft of this type turns more slowly, and must.


---

## D. Your own proposals

Open, as always.

---

## E. Errors (one list)

- **Claude:** *"The sentence is not protected"* (Round 210, Q-210). It is protected. I wrote it without checking the register.
- **Claude:** the archive's transition powers (*"about 220 kW … about 13 kW"*) came from a calculation whose script is not in the repository. Not carried; flagged in §C.
- **Readers:** none found in Round 210.

---

## F. What goes to the author

**Possibly one item.** If the five of us prefer a form that changes the protected Bill 3 sentence (Section 6.2), that goes to the author with the alternatives. Otherwise, nothing.
