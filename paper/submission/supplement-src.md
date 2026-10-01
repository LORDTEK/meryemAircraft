# Supplemental material (journal), source

<!-- Uretim kaynagi. Gonderim ureteci (sonraki adim) bunu LaTeX'e cevirir: "Section 2.1" -> "Sec. II.A", Amerikan yazimi, sayi bicimi.
     Kural (Tur 203, dort okuyucu + Claude; ChatGPT'nin eki oylamada): yalniz govdenin 34 atfinin vaat ettigi icerik; her parca bir arsiv
     kopyasindan gelir ve bugunku govdeye getirilir; emekli iddia yok; sayi kimligi korunur; her parcanin kaynagi src notunda. -->

## S2. The charges: working for Section 2.1

### The power ratio

<!-- for P01: "The ratio between the two demands follows from the governing equations rather than from any design choice (Supplement S2)".
     src: paper/v8/supplement.md, "Section 2 as it stood before recomposition into result sentences", Bill 3 (L756-L771). Verbatim except the Section number. -->

Taking hover power from momentum theory and cruise power from the drag polar,

    P_hover / W  = √(DL / 2ρ) / η_h                 (DL = W/A, disc loading)
    P_cruise / W = V / ((L/D) η_p)

so that

    P_hover / P_cruise = √(DL / 2ρ) · (L/D) / V · (η_p / η_h)

A vehicle with a disc loading of 100 N m⁻², a cruise lift-to-drag ratio of 15 and a cruise speed of 30 m s⁻¹ needs between three and four times as much power to hover as to cruise: the geometric terms alone give 3.2, and the efficiency ratio η_p/η_h carries it to about four when the cruise propeller is roughly a quarter more efficient than the hover rotor.

### The transfer with direct experimental support

<!-- for P02: "One of these transfers has direct experimental support (Supplement S2)".
     src: same snapshot, "The charges are coupled" (L805-L812). Change: dash pair -> parentheses (E33, protected S2 row, format only).
     ADDED (source fact, for reader vote): "and deducted from the battery mass" -- Bacchini thesis eq. (81), paper/bacchini-reading-record.md 5.2. -->

In the doctoral study whose wind-tunnel campaign Section 2.1 quotes [14], and in that document rather than in the journal article by the same author, which reports a different comparison, a retraction system removed thirty percent of the airframe's drag; the same work then costed it. Applied to a passenger eVTOL, with the mechanism assessed at five percent of vehicle mass and deducted from the battery mass, maximum range rose from 119 km to 121 km: a two-kilometre gain for a five-percent mass penalty. The same work finds the retraction's advantage elsewhere (the speed that maximises range rose by 5 m/s), which is a performance this accounting does not price. Bill 2 was converted almost exactly into Bill 1, and the transfer is the point rather than the small residue.

### The tilting row

<!-- for P03: "The tilting row, which needs both clarifications, is worked through in Supplement S2".
     src: same snapshot, "One row pays part of its cost…" (L795-L801), "Two clarifications…" (L822-L832), "The tilting row needs both clarifications" (L834-L839).
     Protected S2 rows (E16) carried, format only (E33). ADDED connector sentence (for reader vote): "The two clarifications of Section 2.1 apply to it as follows." -->

What a tilting architecture buys its unified propulsion group with is a mechanism: a pivot, an actuator, the gyroscopic coupling of a reorienting mass, and a control problem through the turn. The pivot and the actuator are paid in kilograms, although they are not lift-subsystem mass; the coupling and the control problem are paid in none of the three.

The two clarifications of Section 2.1 apply to it as follows. "No worse" is judged against the architecture the move modifies. A charge that architecture already paid, left no larger, is no worse. A charge it did not pay, imposed by the move, is worse; so is one it paid, enlarged by it. A remedy whose cost falls outside the three charges does not refute the accounting, but it is not thereby exempt from being counted. A framework that could absorb any cost by declaring it out-of-scope would be unfalsifiable, so the costs outside the three are listed, not waved away.

The tilting row needs both clarifications. If the architecture it modifies supplies its hover peak from a store, tilting without one imposes Bill 3 and the row is a transfer between charges. If that architecture already sizes its continuous plant by the hover peak, tilting leaves Bill 3 no worse; then, where the mechanism's kilograms are fewer than those of the lift group it removes, what keeps the row from refuting the accounting is the part of its cost that falls outside the three, which is why that part is listed.

## S3. The condition: working for Section 2.2

### What each departure costs

<!-- for P04: "What each departure costs is in Supplement S3".
     src: paper/v8/supplement.md S3 working part, the departures table (L921-L926); the note from "Section 3 as it stood before recomposition…" (L1096-L1100).
     Change: one dash -> comma (row 4). -->

| Departure | What it costs |
|---|---|
| Different hardware | Bills 1 and 2. The unused set is carried for the whole flight and, if exposed, drags. |
| Same hardware, but it serves only one duty | Bills 1 and 2 again. A propulsor that lifts and is then carried is a dedicated lift group under another name, whatever it shares with the cruise system. |
| Same hardware, both duties, different orientation | The tilting family. Bill 3 is incurred unless a store supplies the hover peak, and the mechanism that changes the orientation adds mass and introduces a control problem through the turn. |
| Same hardware, both duties, one orientation, different sizing point | Bill 3, unless the hover peak is supplied from somewhere other than the continuously installed power. |

The second departure is stated separately because it does real work later: a propulsor that produces a little thrust in cruise is not thereby serving both duties, and the distinction decides which parts of a configuration meet the condition and which do not.

### The six permitted costs

<!-- for P05: "Six costs are permitted, named here before any candidate is examined (the working is in Supplement S3)".
     src: "Section 3 as it stood before recomposition into result sentences", the six bullets (L1131-L1180) and the failure-mode note (L1199-L1201).
     BROUGHT UP TO THE CURRENT BODY (superseded wording not carried):
       (3) snapshot "it is priced where the transition is analysed" -> current body "Section 6.1 analyses the transition without pricing it" (Round 191, row 0);
       (5) snapshot "Attitude devices produce thrust in cruise" -> current body "produce no cruise thrust in that sense" (the tip pairs free-wheel at zero shaft torque in cruise, Round 130-131);
       (6) "Section 11" -> "Section 6.2".  Protected S3 row (E17) carried. Dashes -> parentheses or colons. -->

1) **A store.** It has the same duty-cycle character as Bill 1. The fourth part moves the hover peak off the continuous power plant and onto a store; that store delivers its peak for two percent of the flight and is carried for the rest. It is not Bill 1 as Section 2.1 defines it (it is not lift-subsystem mass), but it is mass carried for a duty that is briefly needed, which is the same complaint Bill 1 makes. The condition converts a power-system charge into a cost in kilograms and claims only that the three charges as named are not incurred. It does not claim the trade is favourable. Whether the store is lighter than the continuous power it displaces is a sizing result and is computed, not asserted.

2) **The electrical path.** The fourth part frees the continuous power plant from the hover peak. Everything between the store and the rotors (machines, power electronics, wiring) still passes the full hover power and is still sized by it. That is Bill 3 on the electrical path, and the condition does not remove it; it is carried in the ledger rather than in this definition.

3) **Rotating the airframe.** The condition refuses architectures that reorient a propulsor, and sets that refusal against the mechanism a tilt requires. An architecture that instead rotates its whole body faces the same physical problem: a ninety-degree change of the thrust axis relative to the flight path, with the moments, the authority and the control through the turn that implies. It is not one of the three charges and the condition does not eliminate it; Section 6.1 analyses the transition without pricing it. Saying otherwise would let a candidate win that line by wording.

4) **Hardware installed for the vertical phase that serves both duties.** The second departure is what carries the weight of this permission.

5) **Hardware used in both regimes for something other than propulsive thrust.** Cruise thrust in this paper means the thrust that balances cruise drag. Attitude devices produce no cruise thrust in that sense; they are used throughout the flight, so their duty cycle matches their presence and they fall outside Bill 1. They remain in the airstream, so the second charge reaches them. Attitude hardware does not stop the propulsor that carries the aircraft from meeting the condition, but it is carried through cruise without producing cruise thrust, which is the first failure mode of Section 2.2, and the charges are about everything the aircraft carries, so Bill 2 reaches it. An architecture in that position is a partial instantiation, the fourth failure mode: it meets the condition where it carries the aircraft and still pays one of the three elsewhere. The fourth failure mode is not a technicality. An architecture may meet the condition where it carries the aircraft and fail it elsewhere, and a paper that reported only the first half would be reporting the condition rather than the aircraft.

6) **The price of serving two regimes with one set of hardware.** Hardware that is not duplicated cannot be optimised twice: a propeller sized for hover thrust at zero forward speed is not the propeller a cruise design would choose, and if its geometry is fixed the compromise is paid in efficiency. The condition permits that cost and does not measure it. Section 6.2 does.

## S4. The independent check: working for Section 2.3

### The published designs used

<!-- for P06: "The working is in Supplement S4".
     src: paper/v8/supplement.md S4 working part, table (L1275-L1279); figures checked against the source in this round:
     Johnson & Silva [16], Table 3, p. 70 (references/1521_Johnson & Silva_122721.pdf): L/De 4.9 / 8.5 / 8.6; DGW 3,678 / 7,271 / 6,584 lb. -->

| Configuration (NASA sizing set [16]) | Effective L/D | Design gross weight | Dedicated lift group |
|---|---:|---:|---|
| Turboshaft quadrotor | 4.9 | 3 678 lb | none; the rotors serve both regimes |
| Turbo-electric lift-plus-cruise | 8.5 | 7 271 lb | yes: eight lift motors and a cruise motor |
| Turbo-electric tilt-wing | 8.6 | 6 584 lb | none: eight proprotors, reoriented |

### Why the second half of the prediction is not derived

<!-- src: "Section 4's paragraphs as they stood before the Round 184 shortening" (L1514) and "…before the Round 167 recomposition" (L1466).
     Protected S4 rows (E20) carried: the counter-set and "None is known to the authors." Change: "the mission used below" -> "the mission of Section 2.3"; dash -> colon. -->

Section 2.1 predicts the charge and the amplification; it does not prove that the credit must lose. A dedicated lift system raises the empty-mass fraction and may lower the energy fraction at the same time, and which wins is a closure result rather than a consequence of the accounting. If some data set showed the credit covering the charge, Bill 1 would not be refuted: the mass would still have been paid. What would be refuted is the expectation that the amplified charge outweighs the linear credit. A long enough mission is where the credit is most likely to cover the charge, and the mission of Section 2.3 is short. The counter-set is therefore a common-mission sizing study at longer range in which a dedicated-lift configuration is both more efficient and no heavier than one without. None is known to the authors.

### The weight breakdown

<!-- for P07: "… the remaining 99 lb lies in categories it does not break out (Supplement S4)".
     src: S4 working part (L1281-L1287), CORRECTED against the source (S-64): the archive wrote "battery returns a further 10 lb";
     the source gives battery 254 lb (lift-plus-cruise) against 244 lb (tilt-wing), so it ADDS 10 lb in the lift-plus-cruise entry's disfavour.
     Check: structure 2,670 − 1,954 = 716; propulsion 1,772 − 1,918 = −146; battery 254 − 244 = +10; 716 − 146 + 10 = 580; empty 5,809 − 5,130 = 679. -->

Of the empty-weight difference of 679 lb, structure accounts for 716 lb in the lift-plus-cruise entry's disfavour, propulsion returns 146 lb of it because the tilt-wing's mechanism is heavier, and battery adds a further 10 lb. Those three categories account for 580 lb of the 679; the remaining 99 lb lies in empty-weight categories the published table does not break out, and this work does not know how it is distributed. What the three reported categories do show is the transfer property of Section 2.1 (the mechanism giving part of the structural saving back), visible inside a weight breakdown this work did not produce.

### The source's own statement

<!-- src: "Section 4's paragraphs as they stood before the Round 184 shortening" (L1518). Protected S4 rows (E20) carried verbatim.
     Quotation checked this round: references/1521_Johnson & Silva_122721.pdf, text lines 495-496 ("… but not enough to counter the increase in structure and propulsion weight"). -->

And the source states the second half of the prediction in its own words, on a comparison the check does not use as its test. Discussing why the all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery weight compared with a quadrotor, *"but not enough to counter the increase in structure and propulsion weight."*

### The quadrotor contrast

<!-- src: S4 working part (L1289-L1300). Protected S4 row (E13) carried. Dashes -> colon and parentheses.
     Check: 8.5 / 4.9 = 1.735 -> 1.73 (the archive wrote 1.74: S-65); 7,271 / 3,678 = 1.977 -> 1.98.
     PROTECTED WORD CHANGE: "the isolation test above" -> "the isolation test of Section 2.3" (the supplement has no test above). Author approved, Round 204 (E34). -->

The quadrotor is reported for scale, and the isolation test of Section 2.3 is what carries the prediction. Against it the lift-plus-cruise configuration is about three-quarters better in cruise efficiency (a factor of 1.73) and nearly twice as heavy, a factor of 1.98. The efficiency credit is exactly what the accounting says a dedicated lift system buys, and the weight charge is exactly what it says the buyer pays: the charge survives the credit. But that contrast changes three things at once (dedicated lift group, powertrain, and whether a cruise wing exists at all), so it supports a weaker proposition than the prediction as stated: that adding a wing and a lift group together still costs mass.

## S5. The landing transition: working for Section 3

<!-- for P09: "… the landing transition is not the take-off transition run backwards, and no figure in this paper describes it (Supplement S5)".
     src: paper/v8/supplement.md, "Section 5 as it stood before the length pass", paragraph "Neither has the landing transition." (L1630-L1636).
     Changes: the lead "Neither has the landing transition." dropped (the heading carries it); bold removed; the closing clause shortened,
     since the body already says no figure describes it. No number. -->

The forward rotation and the reverse are not symmetric and must not be assumed to be. Going out, the rotation builds dynamic pressure while it turns, so lift arrives to replace the vertical component of thrust as that component falls. Coming back, the race runs backwards: dynamic pressure is falling while the aircraft is being turned, so lift is leaving at the moment the thrust vector has not yet returned to vertical. A model built for the first case cannot be read for the second by changing a sign, and no figure in this paper describes the second.

## S6. The cruise-efficiency comparison: working for Section 4

### The blade families

<!-- for P11: "Which blade a designer would choose also turns on structural loads, acoustics, the motor operating point, rotor inertia and manufacture,
     none of which is modelled in this work (Supplement S6)".
     src: paper/v8/supplement.md, "Section 6 as it stood before the length pass" (L1830-L1833 and L1856-L1861). Protected S6 row (E13) carried verbatim.
     Added (working under the body's "four nose-blade families", Section 6.1): the family definitions and each family's efficiency, from
     aero/nose-propeller-crossing.txt (aero/nose_propeller_crossing.py, rerun this round: identical output; hover figures of merit 0.591 to 0.603 against the target 0.599, the pitch found by a seven-step search). "Section 10 is where …" -> Section 6.1. -->

The four nose-blade families are two and three blades per rotor, each designed at two target section lift coefficients, 0.55 and 0.70, and each solved at its hover and its cruise condition by blade-element momentum theory. Their cruise propeller efficiencies are 0.648 and 0.683 with two blades and 0.632 and 0.643 with three, at the lower and the higher section lift coefficient respectively. Whether 0.683 is the blade a designer would actually choose is not settled here. It is the best of the four on cruise efficiency under the hover figure-of-merit constraint. Blade count and section loading also govern structural loads, acoustics, the motor operating point, rotor inertia and manufacture, and none of those is modelled in this work. Section 6.1 is where one blade is carried into a closed sizing loop.

### The compared vehicles

<!-- for P12: "The compared vehicles are larger than both designs studied here, which are of order 50 kg and 1 000 kg (Supplement S6)".
     src: paper/v8/supplement.md L1906-L1908 (protected S6 row E13 carried verbatim: "The compared vehicles are 1 660 to 3 275 kg").
     Checked this round against Johnson & Silva [16], Table 3, p. 70: rotorcraft design gross weights QSMR 3,951 / 5,980 lb, side-by-side
     3,665 / 5,547 lb, quadrotor 3,678 / 7,221 lb; 3,665 lb = 1,662 kg, 7,221 lb = 3,275 kg. Closed masses 52.3 and 57.5 kg: body Section 6.1 table.
     Change: "across the same bracket" -> "across its four closures" (52.3 kg is closure D, 57.5 kg closure A; they differ in blade as well as drag). -->

The compared vehicles are 1 660 to 3 275 kg: the six rotorcraft entries of the NASA sizing set [16] have design gross weights from 3 665 lb (the turboshaft side-by-side helicopter) to 7 221 lb (the all-electric quadrotor). The designs here are of order 50 kg and 1 000 kg, and Section 6.1 closes the 50 kg design between 52.3 and 57.5 kg across its four closures.

## S8. The strip and the fairing: working for Section 5.2

### The strip's geometry

<!-- for P13: "Roll comes instead from a strip on the lower surface (its geometry is in Supplement S8)".
     src: paper/v8/supplement.md, "Section 8's paragraphs as they stood before the Round 170 shortening" (L2736). Protected S8 row (E14) carried verbatim
     with the sentence that gives its "it" a referent. Geometry checked this round against aero/roll.py L55-L57 (SERIT_UZUNLUK = 1.20 x root chord,
     SERIT_H_IC/DIS = 0.02/0.06 m, SERIT_ACI = 45 deg in planform) and aero/planform.py (root chord 0.97 m); the strip runs from y = 0 to 1.164 m,
     1.164 / 1.726 = 67 percent of the semi-span. Change: "running 120 % of root chord" made explicit as a spanwise extent, which is how aero/roll.py
     uses it. -->

The reaction-torque channel is declined: every pair is operated torque-balanced, so no reaction torque is spent on control. What declining it costs is not counted in this work. The strip lies on the lower surface, inclined at 45° in planform, and runs outboard from the centreline over a spanwise extent of 120 percent of the root chord (1.164 m against a root chord of 0.97 m), so that it reaches 67 percent of the 1.726 m semi-span. Fully extended it stands 2 cm proud of the surface at its inboard end and 6 cm at its outboard end; extension scales that height.

### The fairing chord

<!-- for P14: "… sized against the criterion the tailless literature recommends it needs a chord of 39 mm, less than a 20 mm faired strut carries
     in any case (Supplement S8)".
     src: paper/v8/supplement.md L2569-L2575 ("What meets the ground"); working from aero/yaw.py, rerun this round: vortex-lattice planform alone
     C_n_beta = +0.00000 /rad; frame mid-chord arm 0.879 m aft of the CG; required side area C_n_beta S b / (a_f l_f) for both frames;
     frame length 2 x 0.71 = 1.42 m each, 2.84 m both; chord = area / 2.84 m: a_f = 3.0 -> 52 mm, 4.0 -> 39 mm, 5.0 -> 31 mm.
     Quotation checked this round: references/NACA-TR-796_…pdf, p. 428 ("… is usually greater than 0.001 per degree").
     The source's own discussion (same column): models flew at one-third of that value, best flying qualities above it; and for fins at the wing
     tips "the drag characteristics as well as the lift characteristics of the tip fins exert an influence on the directional stability".
     The 39 mm counts lift only. Round 205: all four and Claude chose to quote it in S8 (C1 (a)); Grok and DeepSeek asked for the one-third note too; Round 206: all four and Claude accepted the text with both notes. Open (Round 207): DeepSeek's "counts the frames' side force and not their drag". Quotation also checked in NACA ACR L4H19 (same wording). The 50 to 70 mm is a design assumption, not sourced. -->

The planform alone supplies no directional stability: a vortex-lattice solution of the planform without the frames returns a directional-stability derivative of zero, as a planar surface with nothing standing out of its plane should. The fairing on the tip frames therefore supplies all of it. The criterion is the value recommended for conventional airplanes, which the tailless literature applies to tailless ones: a directional-stability parameter *"usually greater than 0.001 per degree"* [24], 0.0573 per radian. With the frames' mid-chord 0.879 m aft of the centre of gravity, the side area required is C_nβ S b/(a_f l_f), where S and b are the reference area and span, l_f the arm and a_f the lateral lift-curve slope of the faired frame. Taken over the combined frame length of 2.84 m (two frames, each projecting 0.71 m on both sides of the planform), that area is a chord of 39 mm at an assumed a_f of 4.0 per radian, and 52 mm and 31 mm at 3.0 and 5.0. A 20 mm thick faired strut is taken to have a chord of 50 to 70 mm, a fineness ratio of 2.5 to 3.5 assumed here rather than sourced. The same report qualifies the criterion in two ways. Models were flown in the Langley free-flight tunnel with one-third of that value, though the best flying qualities came above it; and when fins stand at the wing tips, the moment arm of their drag is half the span, so that *"the drag characteristics as well as the lift characteristics of the tip fins exert an influence on the directional stability"* [24]. The chord derived here counts the frames' side force only.

## S10. The sizing loop and the transition: working for Section 6.1

### The loop

<!-- for P16: "Take-off mass sets the cruise power, cruise power the engine rating, engine rating the propulsion mass, and propulsion mass the take-off mass;
     the take-off mass is found by iteration as the fixed point of that loop (Supplement S10)" (S-67 repaired, Round 210; ChatGPT's wording, all four and Claude).
     src: paper/v8/supplement.md, "Section 10 as it stood before recomposition into result sentences", "Why the loop has to be iterative" (L3099-L3111).
     Protected S10 row (E15) carried: "If no fixed point exists, the declared sizing package does not close."
     WRITTEN AGAINST THE CODE, not the archive (aero/baseline.py boyutlandir() and mimariler(); aero/closure.py rerun this round, output identical
     to aero/closure-result.txt). For this configuration motor_hover=False: the engine is rated at 1.53 x the cruise electrical power; hover power
     is computed at the closed mass and reported; the rest of the propulsion mass is F_TAHRIK_SABIT = 0.108 of MTOW (code comment: propeller, shaft,
     mount, wiring), back-solved from the reference budget. The archive's "a term proportional to MTOW^1.5" is also wrong for the loop as
     run: disc loading is held fixed, so the disc area grows with the mass and hover power is proportional to MTOW. The body sentence (P16) says
     hover power sizes the installed power; Section 6.2 says the engine is sized by cruise and the electrical path by the hover power. Which
     "installed power" P16 means, and whether the loop as run supports it, is candidate S-67, put to the readers in Round 208. -->

The closure statement is

    MTOW = m_payload / (1 − f_empty − f_fuel)

with the fuel fraction fixed at 0.16. The empty fraction contains a propulsion term, f_prop = 0.108 + P_engine / (p_s · MTOW), in which the engine rating P_engine is 1.53 times the cruise electrical power at the take-off mass and p_s, 1.0 kW per kilogram, is the specific power assumed for the engine and generator. The take-off mass is found by iteration as the fixed point of that loop: mass sets the cruise power, cruise power the engine rating, the engine rating the propulsion mass, and the propulsion mass the take-off mass. The rest of the propulsion mass, the fixed 0.108, is a fraction back-solved from the reference design's own budget. Hover power, W^1.5/(FM √(2ρA)) with the disc area A set by the fixed disc loading, is computed at the closed mass and reported, and it does not size the engine. Because the disc loading is fixed, hover power is itself proportional to take-off mass, so any mass that scales with hover power scales as a fixed fraction does; the loop computes no hover-rated mass of its own. The buffer that supplies the hover deficit is a fixed 3.6 percent of take-off mass. If no fixed point exists, the declared sizing package does not close. That is a statement about that package rather than about whether some other package could, and the calculation then returns no number.

### What the loop holds fixed

<!-- src: same snapshot, "The inputs, and why there are four closures rather than one" (L3113-L3171), and "Section 10's paragraphs as they stood before the
     Round 172 shortening" for the current wording of two protected rows. Protected S10 rows carried: "The reference design's assumed zero-lift value of
     0.0248 is not used." (E15); "the control moment arms of Section 8 are therefore reference values that this closure does not re-derive" (E15; Section 8
     -> Section 5.2, renumbering only); "The closures do not take that reduction, and it has not been run through the loop." (E7).
     Figures checked against aero/closure.py output this round: loadings 25.3 kg/m2 and 44.2 kg/m2, AR 6.03; area 2.069-2.273 m2, span 3.532-3.702 m,
     nose disc 1.228-1.287 m, C_L 0.450; frame+rotor terms -4.3 to -12.9 %, Delta C_D0 -0.0009 to -0.0028; reference wing area 1.979 m2.
     CHANGED: the archive said the chord Reynolds number rises "about 7 %" across the closure range. Chord goes as the square root of area at fixed aspect
     ratio: (2.273/1.976)^0.5 = 1.072 from the 50 kg reference design to the heaviest closure, (2.273/2.069)^0.5 = 1.048 across the four closures.
     Both are now stated; 1.072^-0.2 = 0.986, the 1.4 percent. 0.0381/0.0285 = 1.337, the 34 percent. -->

The reference design's assumed zero-lift value of 0.0248 is not used: the build-up of Section 6.2 places it below both ends of the bracket, outside the supported range. Propeller efficiency enters the loop twice, in the range expression and in the cruise power that sizes the engine, and both entries move together with the blade family in every closure; scaling one without the other would size the engine on one propeller and compute the range on another.

The loop holds wing loading (25.3 kg/m²), disc loading (44.2 kg/m²) and aspect ratio (6.03) fixed, so area, span and nose disc diameter follow the mass: across the four closures the wing area runs from 2.07 to 2.27 m², the span from 3.53 to 3.70 m and the nose disc diameter from 1.23 to 1.29 m, and the cruise lift coefficient is 0.450 in every one of them. The tip-frame length, the tip-disc diameter and the strip are not sizing variables. They were set on the 50 kg reference design of Section 5.2, and the control moment arms of Section 5.2 are therefore reference values that this closure does not re-derive.

The frame and rotor drag terms are coefficients on the reference wing area of 1.979 m², so holding them unchanged across the closures lets that hardware grow with the wing. Held at its reference size instead, the hardware would give terms 4 to 13 percent smaller across the four closures, 0.0009 to 0.0028 of zero-lift drag. The closures do not take that reduction, and it has not been run through the loop.

The drag polar is likewise a fixed input. Chord grows with the square root of area, so the chord Reynolds number is up to about 7 percent higher than on the reference design (about 5 percent across the four closures). On a turbulent flat-plate scaling, C_D0 ∝ Re^−0.2, 7 percent is a 1.4 percent change in the zero-lift coefficient, against a bracket whose two ends differ by 34 percent. The claim is that C_L is unchanged, not that C_D0 is exactly so.

### The check against the reference design

<!-- for P17: "Run on the reference design's own assumed inputs, the same construction reproduces that design within 1.5 percent (Supplement S10) …".
     src: same snapshot, "The construction is checked before it is used" (L3173-L3182), and the Round 170 paragraph (assumed inputs named).
     Figures from aero/closure.py, rerun this round: MTOW 49.35 / 50.10 kg (-1.5 %), L/D 11.88 / 11.88, range 1584.88 / 1583 km (+0.1 %).
     Change: "published" -> "the reference design's", as in the body. -->

Run on the reference design's own assumed inputs (a zero-lift coefficient of 0.0248 without the rotor term, and a propeller efficiency of 0.80), the construction returns a take-off mass of 49.4 kg against 50.1 kg, a cruise lift-to-drag ratio of 11.88 against 11.88, and a range of 1 585 km against 1 583 km. The largest deviation is 1.5 percent, in mass. This check is the only place in the closures where the assumed zero-lift value appears; every closure uses the bracket.

### The transition loss and the controller

<!-- for P18: "… the 50 kg design loses 5.4 to 6.6 m at the same reference condition; the loss is not an artefact of the controller (Supplement S10)".
     src: same snapshot, "The transition, and this is where the section turns" (L3236-L3288), with the Round 148 correction X-1 (the loss persists across
     the profiles; it is not unchanged). Protected S10 row (E15) carried: "Within the finite-moment dynamic model, with the aerodynamic moment set to zero,
     the manoeuvre costs altitude."
     Rerun this round of aero/transition_dynamics.py kos() (HAFIF: 50 kg, S 1.979 m2, Iyy 9.81 kg m2; M 23.0 N m; t_r 2 s; 5 m/s entry climb; C_m zero):
     linear 5.43 m, smooth (3t^2-2t^3) 6.33 m, bang-bang 6.57 m, saturation time 0.0 s in all three. Drag: C_D0 0.0285 / 0.0381 with e 0.817 moves each
     by at most 0.022 m. GAIN SWEEP: the archive's "reaching 17 m" has no script in the repository. The figure here is a NEW sensitivity run, not a reconstruction of the
     archived sweep (ChatGPT, Round 208); its design (Kd scaled as the square root of the Kp factor) was chosen this round. Script: aero/transition_gain_sweep.py (a copy of kos()
     with the PD gains as parameters; baseline Kp 25, Kd 10; output aero/transition-gain-sweep-result.txt): Kp x2, x4, x8, x16 with Kd x sqrt: 7.85, 8.71,
     16.32, 16.94 m, no saturation. -->

The 50 kg design is rotated in a three-degree-of-freedom model: the body angle follows a reference profile through a proportional-derivative controller whose moment is limited to the available control moment of 23.0 N·m, with a rotation time of 2 s, an entry climb of 5 m s⁻¹, and the aerodynamic pitching moment set to zero. The loss persists across three reference profiles: 5.43 m with a linear profile, 6.33 m with a smooth (cubic) one and 6.57 m with a bang-bang one, which is the body's 5.4 to 6.6 m. In none of the three does the control moment saturate. Raising the gains increases the loss rather than removing it: with the proportional gain raised sixteen-fold and the derivative gain four-fold, the loss is 16.9 m, again without saturation. With the zero-lift coefficient at either end of the bracket and an Oswald factor of 0.817 instead of the assumed 0.0248 and 0.85, each figure moves by at most 0.02 m. Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude.

### The range figures

<!-- src: "Section 10's paragraphs as they stood before the Round 172 shortening" (L3331). Protected S10 row (E15) carried:
     "no comparison in this paper should be quoted without the contract it was computed under." It follows the body's last paragraph of Section 6.1
     ("These ranges are carried forward as closed-loop values, not as a ranking … (Section 6.4)"); fuel fraction 0.16 from aero/baseline.py ORTAK. -->

The ranges of the four closures are closed-loop values at a fuel fraction fixed at 0.16, not a ranking. Because the comparative result depends on the sizing contract, no comparison in this paper should be quoted without the contract it was computed under.

## S11. The ledger: working for Sections 5.2 and 6.2

### The tip discs stopped: an estimate outside the closure

<!-- for P15 (Section 5.2): "… so the stopped-state drag estimates (Supplement S11) should be read as estimates for an assumed azimuth …" and
     P20 (Section 6.2): "… the eight tip discs stopped edge-on are estimated at ΔC_D0 = 0.0008 (Supplement S11) …".
     src: paper/v8/supplement.md S11, "The other cruise state of the tip discs" (L3381-L3390), carried there from v7 §3.3 Table 3 under S-53
     (closed Round 132, four readers + Claude). No script: an area-and-coefficient estimate (the archive's own qualification, carried verbatim
     in substance). The free-wheeling 0.0154 is the blade-element line of the build-up below (aero/ledger.py, rerun this round, output identical).
     ORDER CHANGED: this subsection now comes BEFORE the protected "Every cost named below is already inside the closure", so that sentence does
     not cover estimates that are outside the closure. -->

In the closure the tip pairs cruise free-wheeling at zero shaft torque. For the other admissible state, stopped, the eight tip discs of the 50 kg reference design are estimated as follows; neither stopped figure is part of the closure of Section 6.1.

| Tip discs in cruise | ΔC_D0 |
|---|---:|
| Free-wheeling at zero shaft torque (blade-element result, in the closure; favourable end) | 0.0154 |
| Stopped edge-on, azimuth controlled (estimate) | 0.0008 |
| Stopped broadside, azimuth uncontrolled (estimate) | 0.015 to 0.018 |

The stopped figures are an area-and-coefficient estimate with assumed solidity and section drag coefficients, not a propeller calculation; what is robust is the ratio between the states, not the values. The edge-on figure assumes an azimuth that something holds.

### The line items of the drag bracket

<!-- for P19 (Section 6.2): "In the drag build-up behind the bracket (line items in Supplement S11), the hardware exposed by the vertical-phase layout …
     is 69 percent of the zero-lift drag at the favourable end and 57 percent at the adverse one".
     src: archive S11 table (L3372-L3379) and "Section 11 as it stood before recomposition", "What this section does" and "Bill 2" (L3475-L3520);
     "Section 11's paragraphs as they stood before the Round 170 shortening" for the protected Bill 2 sentence.
     Protected S11 rows carried: "Every cost named below is already inside the closure of Section 10." (E15; Section 10 -> Section 6.1, renumbering
     only); "No new physical cost term is introduced here." (E15); "No line item at the adverse end is an independent measurement, and they should
     not be subtracted from one another as if they were." (E9); "Bill 2 therefore occupies a larger share where the clean-body drag is lower" (E15).
     Figures from aero/ledger.py, rerun this round (output identical to aero/ledger-result.txt): 0.0073/0.0142, 0.0015/0.0022, 0.0043/0.0047,
     0.0154/0.0169, 0.0285/0.0381; hover hardware 69 / 57 percent; clean body 20.55 / 15.24; retained 52.6 / 57.7 percent. The ten percent margin:
     aero/closure.py kapat(), pay = 1.1 at C_D0 0.0381 (0.0043 x 1.1 = 0.0047; 0.0154 x 1.1 = 0.0169).
     Not carried: the archive's absolute hover-hardware counts "0.0197 … 0.0216"; the script prints 0.0217 for the adverse end (unrounded sum),
     and the body does not use the counts. -->

Every cost named below is already inside the closure of Section 6.1. No new physical cost term is introduced here.

| Zero-lift drag build-up | favourable end | adverse end |
|---|---:|---:|
| Clean wetted surface | 0.0073 | 0.0142 |
| Hub and small items | 0.0015 | 0.0022 |
| Tip frames | 0.0043 | 0.0047 |
| Tip-pair rotors, free-wheeling | 0.0154 | 0.0169 |
| Total | 0.0285 | 0.0381 |

The two ends differ for two separate reasons. The clean surface and the hub are where the drag bracket itself lives, so their base values differ between the ends; on top of that, the adverse end carries a ten percent margin applied to the whole build-up, so the frames and rotors, which have the same base value at both ends, differ only by that margin. No line item at the adverse end is an independent measurement, and they should not be subtracted from one another as if they were.

The tip frames and the free-wheeling rotors together are 69 percent of the zero-lift drag at the favourable end and 57 percent at the adverse one. Removing the hub and small items, the tip frames and the free-wheeling rotors gives a clean-body lift-to-drag ratio of 20.55 at the favourable end and 15.24 at the adverse one, against the aircraft's 10.82 and 8.79: the configuration retains 52.6 and 57.7 percent. Bill 2 therefore occupies a larger share where the clean-body drag is lower, because a near-constant charge is set against a smaller total. That is a statement about position within the drag bracket at one scale, not about size (Section 6.3).

### The buffer against the deficit it covers

<!-- for P21 (Section 6.2): "The deficit per kilogram of take-off mass that the buffer covers, taken at the electrical bus, spreads by 12 percent across
     the four closures while the fraction is held at 3.6 percent (Supplement S11)".
     src: archive "Section 11 as it stood before recomposition", "Bill 1" (L3575-L3586). Figures from aero/buffer.py and aero/ledger.py, rerun this
     round: bus deficit 9.68 / 9.74 / 9.82 / 9.86 kW; per kilogram 0.1683 / 0.1744 / 0.1835 / 0.1884 kW; spread 11.9 percent; buffer 2.07 / 2.01 /
     1.93 / 1.88 kg. Efficiencies: machine 0.92, power electronics 0.95, generator 0.90 (aero/baseline.py, Mimari docstring; aero/buffer.py). -->

The buffer fraction is an input to the loop and is not re-derived from the hover energy the four closures need. What the buffer supplies is the hover demand less what the engine can deliver, taken at the electrical bus where the buffer sits: the rotor shaft power divided by the machine and power-electronics efficiencies (0.92 and 0.95), less the engine's shaft power times the generator efficiency (0.90).

| Closure | Deficit at the bus | Per kilogram of take-off mass | Buffer at 3.6 percent |
|---|---:|---:|---:|
| A | 9.68 kW | 0.1683 kW/kg | 2.07 kg |
| B | 9.74 kW | 0.1744 kW/kg | 2.01 kg |
| C | 9.82 kW | 0.1835 kW/kg | 1.93 kg |
| D | 9.86 kW | 0.1884 kW/kg | 1.88 kg |

The deficit per kilogram spreads by 12 percent across the four closures, and the closure that needs the most per kilogram, D, carries the smallest buffer.

### The propulsion-mass split

<!-- for P22 (Section 6.2): "Bill 3 is removed from the engine and left standing on the electrical system (the propulsion-mass split is in Supplement S11)".
     src: archive "Bill 3" (L3591-L3606) and the empty-mass paragraph (L3588-L3590). Figures from aero/ledger.py, rerun this round: propulsion
     0.198 (A) = 0.108 + 0.090, 0.176 (D) = 0.108 + 0.068; engine 5.17 / 3.54 kW; airframe 0.300, avionics 0.080 (aero/baseline.py ORTAK).
     CORRECTED against the code: the archive said "the propulsion mass fraction reflects it" (the electrical path sized by hover power) and called
     the variable part the part that "scales with installed power". The variable part is the ENGINE rating over 1.0 kW/kg (cruise-sized); no term
     of the loop scales with hover power. Same finding as S-67 (Round 208). Q-210 closed (Round 212, all five): the protected body sentence
     stays as it is, and the body adds after it "The sizing loop computes no hover-rated mass for the electrical path." -->

The propulsion fraction of the empty mass is 0.176 to 0.198 across the four closures, in two parts. A fixed 0.108 is back-solved from the reference design's own budget (the code's comment lists propeller, shaft, mount and wiring). The engine term is the engine rating divided by an assumed specific power of 1.0 kW per kilogram: 0.068 at closure D to 0.090 at closure A, following the cruise-sized rating of 3.54 to 5.17 kW. The hover power, 11.4 to 12.5 kW at the rotor shaft, passes through the electrical path whatever the engine is rated at, but the loop computes no hover-rated mass for that path; whatever of it lies in the fixed 0.108 scales with take-off mass, which at fixed disc loading is how hover power scales. The airframe (0.300) and avionics (0.080) fractions are construction constants held common across the three architectures of Section 6.4; they are not results of the ledger.

## S12. Scale: working for Section 6.3

### The reference pair

<!-- for P24 (Section 6.3): "The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 6.1's closures (Supplement S12)".
     src: paper/v8/supplement.md, "Section 12 as it stood before the supplement move (complete)" (archive S12, the moved working of Round 155).
     Protected S12 rows carried: "That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3." (E15);
     "This paragraph compares the reference pair only." (E10); "Much above 1 000 kg a single nose pair can no longer hold" (E15).
     Figures checked this round: 10.9 / 2.6 = 4.19 and 216.2 / 54.3 = 3.98 (the reference designs' own figures, aero/baseline.py comments and
     agir_dogrula(); paper/v8-evidence.md row "4,19 / 3,98"); engine margins 2.6 / 1.7 = 1.53 and 54.3 / 39.2 = 1.39 (aero/baseline.py);
     216.2 / (39.2 x 1.53) = 3.61, (4.19 - 3.61) / 4.19 = 14 percent, (4.19 - 3.98) / 4.19 = 5 percent; disc loading 50 / (pi 0.6^2) = 44.2 and
     1000 / (pi 2.7^2) = 43.7 kg/m2; 10.9 / 50 = 0.218 and 216.2 / 1000 = 0.216 kW/kg; diameter / span 1.2 / 3.452 = 0.35 and 5.4 / (6.0 x 22.24)^0.5
     = 0.47. ADDED: the heavy ratio under the light design's margin (3.61), which is the arithmetic behind the archive's "5 to 14 percent". -->

The test uses the 50 kg and 1 000 kg reference designs, sized by one method. No closure of Section 6.1 was run at 1 000 kg: the heavy design has no drag bracket and no structural closure, and no heavy-design range is quoted.

Disc loading is held at approximately the same value, 44.2 kg m⁻² at 50 kg and 43.7 at 1 000 kg, so specific hover power is held with it: 0.218 kW kg⁻¹ at the light design and 0.216 at the heavy. That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3. Section 6.2's measure of Bill 3, rotor-shaft hover power over engine shaft rating, is 4.19 at the light design (10.9 kW over 2.6 kW) and 3.98 at the heavy (216.2 kW over 54.3 kW). The two designs rate their engines at different margins over cruise power, 1.53 and 1.39; with the light design's margin, the heavy ratio would be 3.61. The ratio therefore moves by 5 to 14 percent across the factor of twenty, depending on an engine margin the sizing rule does not set. Section 6.2's 2.4 to 3.2 is the same ratio at the four closures. This paragraph compares the reference pair only.

The rule has a price, paid in geometry: the ratio of nose-propeller diameter to span rises from 0.35 to 0.47, and much above 1 000 kg a single nose pair can no longer hold the disc loading, so a second would have to be added.

### The rotor term of Bill 2

<!-- for P24 (the comparison's Bill 2 side; the body's "falls to between 0.29 and 0.65 … in the section polars used here" and its Reynolds-number sentence).
     src: same archive snapshot, "Bill 2 — the rotor term falls" paragraph. Figures from aero/heavy_rotor.py (corrected setup, Round 55), stored output
     aero/heavy-rotor-result.txt, rerun this round: eight designs c_l 0.55-0.85, all FM >= 0.599, dC_D0 0.00447-0.01003, ratio to 0.01535 = 0.29-0.65;
     c_l 0.68: 0.00681; median section Re 81 689 -> 556 336; heavy blade at the light Re: 0.01810 = 1.18 x; solidity 0.0754 -> 0.0999 (x 1.33);
     q test 0.00748 at 30 m/s, 0.00681 at 40 m/s (0.911, against 1/1.778 = 0.562); tip speed 210 m/s and hub 15 percent of radius at both sizes.
     CHANGED: the archive's "three other candidates are excluded" now names them; the count word is dropped (the list has solidity, dynamic pressure,
     and the shared tip speed and hub fraction). -->

Only the rotor term of Bill 2 is computed at both sizes; the frame term enters both designs as the same multiplier, so it cannot show a scale effect in either direction. At 50 kg the rotor term is 0.0154. At 1 000 kg, eight tip-rotor designs at section lift coefficients from 0.55 to 0.85, all meeting the hover figure of merit, give 0.0045 to 0.0100, that is 0.29 to 0.65 of the light value; the design at the light design's section lift coefficient, 0.68, gives 0.0068. Within the blade-element and section-polar model the section Reynolds number accounts for the fall: the median section Reynolds number rises from about 8.2 × 10⁴ to 5.6 × 10⁵, and the heavy blade brought down to the light design's Reynolds number gives 0.0181, 1.18 times the light value. The other candidates are excluded. The heavy blade is the more solid (1.33 times), which would raise its drag rather than lower it; dynamic pressure cancels (between 30 and 40 m s⁻¹ the heavy term changes by a factor of 0.911, against the 0.562 a dynamic-pressure effect would give); and the design tip speed (210 m s⁻¹) and the hub fraction (15 percent of radius) are the same at both sizes. This is a decomposition inside the model rather than a causal claim beyond it.

### Bill 1

<!-- for P25 (Section 6.3): "It appears here as the energy buffer, 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and both figures are
     inputs (Supplement S12)". src: same archive snapshot, "Bill 1 — not tested". Protected S12 row (E15) carried: "A change from 3.6 to 4.0 percent is a
     change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction."
     Inputs checked: light closures f_tampon 0.036 (aero/closure.py), heavy design f_tampon 0.04 (aero/baseline.py mimariler() default, agir_dogrula()). -->

Both buffer figures are inputs: 0.036 of take-off mass in the light closures and 0.040 in the heavy design's sizing. A change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction. A buffer sized to the hover deficit at the same specific power would track hover power and engine rating, which are the Bill 3 measures, so that derivation cannot test whether Bill 1 separates.

### The rotation time

<!-- No body pointer: carried because the protected row was moved here by the author's decision (E15): "A larger aircraft of this type turns more slowly,
     and must." src: same archive snapshot, "Two costs that scale does not relieve".
     CHANGED: the archive's "about 220 kW … about 13 kW" could not be reproduced exactly (no script found; a momentum-power estimate from
     aero/rotation.py's moments gives about 200 kW and 12 kW). Replaced by figures aero/rotation.py prints, rerun this round: pitch inertia 9.813 and
     2503 kg m2 (ratio 255.1), available moment 23.0 and 952 N m (ratio 41.4), rotation time that keeps the light design's moment margin 4.96 s, the
     heavy design's 5.1 s. Put to the readers in Round 211: whether this subsection stays (it carries a protected row the body does not point to). -->

The transition is where the square–cube relation is paid. The heavy design's pitch inertia is 255 times the light design's and its available control moment 41 times, so to keep the light design's moment margin it must rotate in about 5 s rather than 2 s (4.96 s computed; the heavy design uses 5.1 s). A larger aircraft of this type turns more slowly, and must.

## S13. Contracts: working for Section 6.4

### The three contracts

<!-- for P26 (Section 6.4): "Range in the sizing loop is proportional to L/D, to the energy chain and to the fuel fraction, and the three contracts differ only in
     the last (Supplement S13) …". src: archive "Section 13's paragraphs as they stood before compression", "Three contracts, and what each holds equal".
     Checked against the code this round: aero/baseline.py menzil_ver() (R = f_fuel E* eta_chain L/D / g), sabit_yakit(), sabit_MTOW(); aero/contracts.py,
     rerun this round, output identical to aero/contracts-result.txt (fuel 9.20 / 8.94 / 8.56 / 8.37 kg at closures A-D). -->

Range in the sizing loop is R = f_fuel E* η_chain (L/D)/g, with E* the fuel's specific energy and η_chain the energy chain from fuel to thrust. The three architectures share E* and the chain apart from the propeller efficiency, which enters η_chain, and they differ in L/D. The three contracts differ only in the fuel fraction f_fuel:

1) fixed fuel fraction: every architecture carries 0.16 of its own take-off mass as fuel, so take-off mass cancels from range;
2) fixed fuel mass: every architecture carries the fuel this configuration carries at that closure, 9.20, 8.94, 8.56 and 8.37 kg at closures A to D, as a fraction of its own take-off mass;
3) fixed take-off mass and payload: every architecture is held at this configuration's take-off mass with the same 13 kg payload, and its fuel is what remains after its empty mass, so every kilogram of architecture-specific hardware is a kilogram of fuel not carried.

### The per-closure numbers

<!-- for P28 (Section 6.4): "The per-closure numbers are in Supplement S13." src: archive S13 first table (L4126-L4132); figures from aero/contracts.py, rerun this
     round. Added from the same output: the mass ratio under the first contract and the shift. -->

Range of the lift-plus-cruise layout relative to this configuration (positive: lift-plus-cruise ahead), and the mass ratio under the first contract:

| Closure | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass | Shift, first to third | Lift-plus-cruise mass / this configuration's, first contract |
|---|---:|---:|---:|---:|---:|
| A | +67.8 % | +40.2 % | +1.1 % | 66.8 points | 1.392 |
| B | +55.3 % | +27.5 % | −13.0 % | 68.3 points | 1.433 |
| C | +83.9 % | +53.5 % | +7.3 % | 76.6 points | 1.378 |
| D | +70.2 % | +40.1 % | −6.5 % | 76.7 points | 1.409 |

The tilting layout, credited with no cruise penalty, is 93 to 141 percent ahead under every contract at every closure.

### Without the common buffer

<!-- for P27 (Section 6.4): "… without the buffer, and with engines rated to the hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction
     or a fixed take-off mass (Supplement S13)". src: aero/contracts.py case (d), rerun this round: lift-plus-cruise "KAPANMADI" (does not close) under
     contracts 1 and 3 at every closure; under contract 2, -46.6 to -38.4 percent. Not used in Section 6.4's comparison. -->

If the competitors carry no buffer and rate their engines to the hover demand, the lift-plus-cruise layout does not close at any of the four closures under a fixed fuel fraction or a fixed take-off mass; under a fixed fuel mass it is 38 to 47 percent behind this configuration. This case is not used in Section 6.4's comparison; it shows only the direction of the choice to hold Bill 3 common.

### Sensitivity

<!-- for P29 (Section 6.4): "… across the sensitivity cases the competitor's lift-group mass and the propeller basis (Supplement S13)" and P30: "… with a common propeller
     efficiency the lift-plus-cruise lead under the first contract falls from 55–84 to 33–45 percent (Supplement S13)". src: archive S13 second table (L4136-L4144) and
     "Section 13's paragraphs as they stood before the Round 172 shortening" (L4417 version). Protected S13 rows carried: "With a lighter lift group … a reversal
     appears at every closure." (E15) and "The sign under a fixed take-off mass is not a result about the architectures; it is a result about those quantities."
     (E14; the archive's lead-in "Put plainly," is not part of the register text and is not carried). Figures from aero/contracts.py cases (a), (b) 5 % and 15 %,
     (c), rerun this round: every range and shift matches the archive table. The antecedent sentence for "those quantities" restates the body's Section 6.4. -->

| Case | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass | Shift, first to third |
|---|---:|---:|---:|---:|
| As declared (lift group 10 % of take-off mass, competitors' propeller efficiency 0.80) | +55 to +84 % | +28 to +54 % | −13 to +7 % | 67 to 77 points |
| Lift group 5 % of take-off mass | +55 to +84 % | +47 to +76 % | +36 to +65 % | 14 to 24 points |
| Lift group 15 % of take-off mass | +55 to +84 % | +8 to +31 % | −62 to −50 % | 117 to 134 points |
| All three at this configuration's propeller efficiency | +33 to +45 % | +6 to +17 % | −33 to −25 % | 65 to 72 points |
| Lift-plus-cruise drag as a fixed increment, not a ratio | +59 to +75 % | +31 to +45 % | −13 to +5 % | 67 to 75 points |

With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every closure; with a heavier one this configuration leads under a fixed take-off mass at every closure; with a common propeller efficiency a reversal appears at every closure. The quantities that decide the sign are assumed for the competitor rather than measured: its lift-group mass fraction and its propeller efficiency. The sign under a fixed take-off mass is not a result about the architectures; it is a result about those quantities.

## S14. What does not close: working for Sections 3, 6.2 and 7

### The measured store figures

<!-- for P31 (Section 7): "… its unit pack, discharged on the bench at its highest tested rate, delivered on average about 1.5 kW per kilogram (Supplement S14)".
     src: archive S14, "Section 14 as it stood before recomposition into result sentences", store paragraph. Checked this round against
     references/Yu-2025_24S-NCM-battery-eVTOL-IN-FLIGHT_Batteries.pdf [25]: 24S1P unit pack 13.5 kg; 10.68C (235 A), the maximum discharge condition considered;
     Table 7: 16.26 Ah, 1394.3 Wh at 10.68C -> 16.26/235 h = 249 s, 1394.3 Wh / 249 s / 13.5 kg = 1.49 kW/kg (aero/buffer.py uses 1.49); 55.1 deg C,
     4.9 deg C margin to the authors' 60 deg C; 724 W/kg (110 A) unit pack and 892 W/kg (440 A) 24S4P system; VS-210, 210 kg-class MTOW.
     Demand ratios from aero/buffer.py, rerun this round (identical): hover 4.68-5.23, take-off 5.53-6.09 kW/kg; /1.49 -> 3.1-3.5 and 3.7-4.1. -->

The flown system is a 24-series nickel–cobalt–manganese pack designed, bench-tested and flown in a 210 kg-class electric VTOL aircraft [25]. As a flown system (24S4P) it is rated at 0.892 kW per kilogram continuous; its 13.5 kg unit pack (24S1P) is rated at 0.724 kW per kilogram continuous. Discharged on the bench at its highest tested rate, 10.68C (235 A), the unit pack delivered 1 394 Wh in about 249 s, on average about 1.5 kW per kilogram for about four minutes, and reached 55.1 °C against the 60 °C limit its authors adopted. Against that bench average the take-off demand of the four closures, 5.5 to 6.1 kW per kilogram of buffer, is 3.7 to 4.1 times, and hover alone, 4.7 to 5.2 kW per kilogram, is 3.1 to 3.5 times.

### The loop closed again on a measured store

<!-- for P32 (Section 7): "… closed again at the bench rate, it becomes 76 to 81 percent heavier, a sensitivity with one input changed rather than a structural
     closure (Supplement S14)". src: same archive snapshot, re-closure paragraph and table. Protected S14 rows carried (E12): "These masses are the Section 10
     package with one input changed." (Section 10 -> Section 6.1, renumbering only) and "They are not a structural closure at 100 kg".
     Figures from aero/buffer.py, rerun this round (identical to aero/buffer-result.txt): 4.0 kW/kg 56.6-61.2 kg, 5.0-5.5 %, +6.5 to +8.2 %; 1.49 kW/kg
     94.6-101.2 kg, 13.4-14.7 %, +75.9 to +80.8 %; 0.892 kW/kg 333.5-335.2 kg, 22.3-24.6 %; 0.724 kW/kg does not close; payload at the closures' masses
     with the bench rate 7.2-7.4 kg. CHANGED: the archive's "+6 to +8 %" is now +6.5 to +8.2 % (6.5 does not round to 6). -->

Closing the loop on a measured store is a sensitivity of the package, not a second aircraft. The buffer is derived inside the loop from the take-off demand at a given specific power; everything else is Section 6.1's: the same fractions, including an airframe at thirty percent of take-off mass, and the same wing loading, disc loading and aspect ratio, so the lift-to-drag ratio is carried unchanged and, with the fuel fraction held, so is the range. These masses are the Section 6.1 package with one input changed. They are not a structural closure at 100 kg, and whether the airframe fraction holds at twice the mass it was set at is not established.

| Buffer specific power, per kilogram of buffer | Take-off mass | Buffer | Change from Section 6.1 |
|---|---:|---:|---:|
| As Section 6.1 implies: 5.5 to 6.1 kW kg⁻¹ | 52.3 to 57.5 kg | 3.6 % | — |
| 4 kW kg⁻¹, the design-study assumption [26] | 56.6 to 61.2 kg | 5.0 to 5.5 % | +6.5 to +8.2 % |
| About 1.5 kW kg⁻¹, the unit pack's bench rate | 94.6 to 101.2 kg | 13.4 to 14.7 % | +76 to +81 % |
| 0.892 kW kg⁻¹, the flown system's continuous rating | about 335 kg | 22 to 25 % | set by nearness to non-closure |
| 0.724 kW kg⁻¹, the unit pack's continuous rating | does not close | — | — |

If Section 6.1's take-off masses are kept instead of re-closing at the bench rate, the payload falls to about 7 kg rather than 13. At the flown system's continuous rating the loop only just closes, and the mass it returns is set by how near the loop is to not closing rather than by anything about the aircraft.

### The open questions

<!-- for P08 (Section 3, the vortex ring state), P10 (Section 3, the cost of declining the reaction-torque channel), P23 (Section 6.2, what the closure does not
     contain), P33 (Section 7, "Eighteen further questions are open, and Supplement S14 lists each with what it bears on and what would settle it") and P34
     (Section 8, "Section 7 and Supplement S14 list what the paper leaves open").
     src: archive S14 table (L4439-L4459). Section references renumbered from step to section numbers (5->3, 6->4, 7->5.1, 8->5.2, 10->6.1, 11->6.2, 12->6.3,
     13->6.4, 14->7). Brought up to the current body: the electrical-path row no longer says the path "enters the loop as a mass fraction" (the S-67 / Q-210
     finding; it now says the loop computes no mass for it sized to that peak); the strip-and-fairing row adds the fairing's assumed slope and side-force-only
     limit (S-66, Supplement S8); the descent row points to Supplement S5; the store-types row names its source [23]. Eighteen rows are open questions; the
     store-types row is marked as part of the known obstacle and is not counted. Not rerun this round: the transition incidence (18-22 deg) and the shell
     areal density (1.78 against 1.50 kg/m2), carried from the archive table as accepted in Rounds 135-140. Quotation [23] and page [3] p. 320 as verified in
     earlier rounds (references-draft notes). -->

Section 7 lists eighteen questions this work has not answered. Each is given here with what it bears on and what would settle it; one further row, on store types, belongs to the known obstacle and is not one of the eighteen.

| Item | Bears on | What would settle it |
|---|---|---|
| **The pitching moment through the transition.** Three methods of three fidelities diverge above about ten degrees of incidence; the rotation passes through that band, peaking near 18 to 22 degrees on the 50 kg reference geometry, with the inboard half of the wing in the slipstream at a much lower effective incidence. | Whether the aircraft trims through the rotation (Sections 5.1 and 6.1) | Validated aerodynamic data: a measurement of the outboard wing's pitching moment to about 22 degrees at low dynamic pressure and of trim at the attached-flow end of the rotation, or a higher-fidelity method validated against one |
| **Section drag at low Reynolds number.** The tip-pair rotors' free-wheeling charge rests on section polars below a Reynolds number of 10⁵, and the uncertainty runs both ways. | The rotor term in every closure, 0.0154, carried as 0.0169 at the adverse end with the build-up's ten percent margin (Sections 6.1 and 6.2); the size of Bill 2's fall with scale (Section 6.3); and the tip-rotor blade itself, which the hover requirement selects on the same polars (Supplement S12) | Validated data: the drag of a free-wheeling tip rotor, or of its sections, at about 8 × 10⁴, or a method validated there |
| **The tip pairs' other cruise state.** Free-wheeling is determinate and computed; stopped is a family of states whose means and azimuth are not fixed (Section 5.2; Supplement S11). | Whether a lower-drag cruise state is available, and at what mechanism cost | Analysis, or a measurement of one stopped state |
| **The tip pairs' shaft power off the free-wheeling state in cruise.** Attitude moments in cruise are commanded departures from the zero-shaft-torque state, and the shaft power they take is not computed (Section 5.2). | Cruise energy | Analysis of cruise attitude demand and of the tip pairs' shaft power off the zero-torque state |
| **The buffer's energy, not only its power.** The store is sized here by power. Whether it also holds the energy for the vertical phases and their reserves, and how it is recharged in cruise, depends on a hover duration this work does not fix; at the bench rate the unit pack emptied in about four minutes. | Whether the store sized by power is also large enough | Analysis against a defined mission profile |
| *Other store types (part of the known obstacle; not one of the eighteen).* A supercapacitor store is tabulated in one survey at specific-power ranges that include values at the level the buffer requires, 500 to 10 000 W/kg from one cited source and 10 000 to 100 000 W/kg from another, at 1 to 10 Wh/kg [23]. The table has no battery–supercapacitor row; the combination enters only through the survey's own qualification on this class: *"Supercapacitors exhibit low specific energy but outstanding specific power at high cost suggesting that this technology is more appropriate in a hybrid energy storage approach (e.g. supercapacitors and batteries)."* | Whether a store other than a battery, alone or combined with one, closes the buffer at the required power and holds the vertical phases' energy | Analysis against a defined mission profile; not computed here |
| **The electrical path at peak.** Machines, power electronics, wiring and their cooling carry the full take-off demand; the loop computes no mass for them sized to that peak and its heat (Section 6.2; Supplement S11). | Whether the path that delivers the buffer's power exists at the mass assumed | Component sizing and thermal analysis |
| **The airframe's mass.** It enters the loop as a construction constant, thirty percent of take-off mass (Supplement S11). A component build-up at the reference mass leaves room for the 13 kg payload only if the average shell areal density stays at or below 1.78 kg m⁻², against 1.50 assumed; the build-up carries a contingency rather than a structural sizing, and it has not been re-run at Section 6.1's closed masses, still less at the masses the store re-closure returns. At the 1 000 kg reference design the shell-mass exponent is not measured at all. | Every closed mass | Structural sizing (analysis), then a built article (measurement) |
| **The strip and the fairing.** The strip's effect on this planform is computed, not measured, and its actuation is carried in the systems budget without being sized (Section 5.2). The fairing is sized against a published stability criterion at an assumed lateral lift-curve slope, counts the frames' side force only, and the side force it develops is not measured (Supplement S8). | The strip: the body roll axis, which appears as bank in cruise and as a change of heading in hover (Section 5.2). The fairing: directional stability in cruise | Measurement of both surfaces; sizing of the actuation |
| **Closed-loop attitude control, in hover and in cruise**, including the cost of declining the reaction-torque channel, which would act about the body roll axis in both regimes (Section 5.2), the absorption of the hover torque residual left by trimming each pair's torque balance at cruise (Section 5.2), and the allocation of the tip pairs between take-off margin and attitude authority, which compete for the same propellers. | Whether the aircraft is controllable with the authority computed, in hover and in cruise (Sections 3 and 5.2) | Analysis not yet done: a control-allocation study, then simulation |
| **Vertical descent and the landing transition.** Neither is analysed; the vortex ring state is not assessed, and the landing transition is not the take-off transition run backwards (Supplement S5). | Whether the aircraft can come down as it went up (Section 3) | Analysis not yet done |
| **Ground handling and landing loads.** The stance base is a parameter against static crosswind (Section 3), and the wing's exposure to ground wind is not priced (Section 4); the response to a landing with lateral velocity or on uneven ground, and handling between flights, are not assessed. | Operation from unprepared sites | Analysis not yet done |
| **The competitor's lift-group mass.** It is one of the two assumed quantities that decide the sign of the fixed-take-off-mass ordering in Section 6.4; the other is the competitor's cruise propeller efficiency. | Section 6.4's sensitivity, not a claim | Measured inventories of lift-plus-cruise aircraft of this class |
| **The competitor's cruise propeller efficiency.** Assumed at 0.80, not computed; with all three architectures at this configuration's propeller efficiency, this configuration leads under a fixed take-off mass at every closure (Supplement S13). | Section 6.4's sensitivity, not a claim | Computation of that propeller at its operating point |
| **Rotor–structure and rotor–wing interference, in cruise and in hover.** In cruise it is inside Bill 2 in principle, absent from the build-up and not modelled (Section 6.2); the drag bracket's upper margin is the only provision made for it. In hover the nose pair's slipstream runs over the inboard wing and the strip (Section 5.2), and any force or moment it produces there beyond the strip's commanded action is not computed. On a quadrotor tail-sitter reported in 2013 the slipstream acting on a wing under the propellers made control about the thrust axis difficult, and the wing was moved out of it ([3], p. 320); that aircraft used single rotors, and whether a contra-rotating pair changes the effect is not computed. | Bill 2, and so every closure; in hover, the control about the body roll axis and the hover torque balance (Sections 3 and 5.2) | Analysis not yet done |
| **Engine installation**: bay, intake, exhaust, cooling. | Mass, drag and packaging | Absent from this work entirely |
| **Blade-family selection.** The criteria that would choose among the blade families (structural loads, acoustics, the motor operating point, rotor inertia, manufacture) are not modelled (Section 4; Supplement S6). | Which point of the envelope the aircraft occupies | Analysis not yet done |
| **The variable-pitch counterfactual.** Whether a variable-pitch hub would recover the fixed-pitch cruise-efficiency gap is not computed (Sections 4 and 6.2). | The cruise-efficiency gap (Section 6.2) | A variable-pitch counterfactual closed through the same loop |
| **Atmosphere.** Every number here is at sea level; the configuration's own altitude sensitivity has been computed for hover power and propeller efficiency, but its effect on the Section 4 comparison has not. | The comparison in Section 4, made against a mission flown at altitude | Analysis; the direction of the effect has not been computed |
