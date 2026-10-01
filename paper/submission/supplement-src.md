# Supplemental material (journal), source

<!-- Uretim kaynagi. Gonderim ureteci (sonraki adim) bunu LaTeX'e cevirir: "Section 2.1" -> "Sec. II.A", Amerikan yazimi, sayi bicimi.
     Kural (Tur 203, dort okuyucu + Claude; ChatGPT'nin eki oylamada): yalniz govdenin 34 atfinin vaat ettigi icerik; her parca bir arsiv
     kopyasindan gelir ve bugunku govdeye getirilir; emekli iddia yok; sayi kimligi korunur; her parcanin kaynagi <!-- src --> notunda. -->

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

<!-- for P16: "Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power;
     the take-off mass is found by iteration as the fixed point of that circle (Supplement S10)".
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
     by at most 0.022 m. GAIN SWEEP: the archive's "reaching 17 m" has no script in the repository; reproduced this round by aero/transition_gain_sweep.py (a copy of kos()
     with the PD gains as parameters; baseline Kp 25, Kd 10; output aero/transition-gain-sweep-result.txt): Kp x2, x4, x8, x16 with Kd x sqrt: 7.85, 8.71,
     16.32, 16.94 m, no saturation. -->

The 50 kg design is rotated in a three-degree-of-freedom model: the body angle follows a reference profile through a proportional-derivative controller whose moment is limited to the available control moment of 23.0 N·m, with a rotation time of 2 s, an entry climb of 5 m s⁻¹, and the aerodynamic pitching moment set to zero. The loss persists across three reference profiles: 5.43 m with a linear profile, 6.33 m with a smooth (cubic) one and 6.57 m with a bang-bang one, which is the body's 5.4 to 6.6 m. In none of the three does the control moment saturate. Raising the gains increases the loss rather than removing it: with the proportional gain raised sixteen-fold and the derivative gain four-fold, the loss is 16.9 m, again without saturation. With the zero-lift coefficient at either end of the bracket and an Oswald factor of 0.817 instead of the assumed 0.0248 and 0.85, each figure moves by at most 0.02 m. Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude.

### The range figures

<!-- src: "Section 10's paragraphs as they stood before the Round 172 shortening" (L3331). Protected S10 row (E15) carried:
     "no comparison in this paper should be quoted without the contract it was computed under." It follows the body's last paragraph of Section 6.1
     ("These ranges are carried forward as closed-loop values, not as a ranking … (Section 6.4)"); fuel fraction 0.16 from aero/baseline.py ORTAK. -->

The ranges of the four closures are closed-loop values at a fuel fraction fixed at 0.16, not a ranking. Because the comparative result depends on the sizing contract, no comparison in this paper should be quoted without the contract it was computed under.
