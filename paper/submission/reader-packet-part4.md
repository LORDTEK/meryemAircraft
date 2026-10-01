> **Reader packet, part 4 of 4** (commit `73b68ec`). Read all parts before answering; the round text says what to judge.

The loop holds wing loading (25.3 kg/m²), disc loading (44.2 kg/m²) and aspect ratio (6.03) fixed, so area, span and nose disc diameter follow the mass: across the four closures the wing area runs from 2.07 to 2.27 m², the span from 3.53 to 3.70 m and the nose disc diameter from 1.23 to 1.29 m, and the cruise lift coefficient is 0.450 in every one of them. The tip-frame length, the tip-disc diameter and the strip are not sizing variables. They were set on the 50 kg reference design of Section 5.2, and the control moment arms of Section 5.2 are therefore reference values that this closure does not re-derive.

The frame and rotor drag terms are coefficients on the reference wing area of 1.979 m², so holding them unchanged across the closures lets that hardware grow with the wing. Held at its reference size instead, the hardware would give terms 4 to 13 percent smaller across the four closures, 0.0009 to 0.0028 of zero-lift drag. The closures do not take that reduction, and it has not been run through the loop.

The drag polar is likewise a fixed input. Chord grows with the square root of area, so the chord Reynolds number is up to about 7 percent higher than on the reference design (about 5 percent across the four closures). On a turbulent flat-plate scaling, C_D0 ∝ Re^−0.2, 7 percent is a 1.4 percent change in the zero-lift coefficient, against a bracket whose two ends differ by 34 percent. The claim is that C_L is unchanged, not that C_D0 is exactly so.

#### The check against the reference design


Run on the reference design's own assumed inputs (a zero-lift coefficient of 0.0248 without the rotor term, and a propeller efficiency of 0.80), the construction returns a take-off mass of 49.4 kg against 50.1 kg, a cruise lift-to-drag ratio of 11.88 against 11.88, and a range of 1 585 km against 1 583 km. The largest deviation is 1.5 percent, in mass. This check is the only place in the closures where the assumed zero-lift value appears; every closure uses the bracket.

#### The transition loss and the controller


The 50 kg design is rotated in a three-degree-of-freedom model: the body angle follows a reference profile through a proportional-derivative controller whose moment is limited to the available control moment of 23.0 N·m, with a rotation time of 2 s, an entry climb of 5 m s⁻¹, and the aerodynamic pitching moment set to zero. The loss persists across three reference profiles: 5.43 m with a linear profile, 6.33 m with a smooth (cubic) one and 6.57 m with a bang-bang one, which is the body's 5.4 to 6.6 m. In none of the three does the control moment saturate. Raising the gains increases the loss rather than removing it: with the proportional gain raised sixteen-fold and the derivative gain four-fold, the loss is 16.9 m, again without saturation. With the zero-lift coefficient at either end of the bracket and an Oswald factor of 0.817 instead of the assumed 0.0248 and 0.85, each figure moves by at most 0.02 m. Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude.

#### The range figures


The ranges of the four closures are closed-loop values at a fuel fraction fixed at 0.16, not a ranking. Because the comparative result depends on the sizing contract, no comparison in this paper should be quoted without the contract it was computed under.

### S11. The ledger: working for Sections 5.2 and 6.2

#### The tip discs stopped: an estimate outside the closure


In the closure the tip pairs cruise free-wheeling at zero shaft torque. For the other admissible state, stopped, the eight tip discs of the 50 kg reference design are estimated as follows; neither stopped figure is part of the closure of Section 6.1.

| Tip discs in cruise | ΔC_D0 |
|---|---:|
| Free-wheeling at zero shaft torque (blade-element result, in the closure; favourable end) | 0.0154 |
| Stopped edge-on, azimuth controlled (estimate) | 0.0008 |
| Stopped broadside, azimuth uncontrolled (estimate) | 0.015 to 0.018 |

The stopped figures are an area-and-coefficient estimate with assumed solidity and section drag coefficients, not a propeller calculation; what is robust is the ratio between the states, not the values. The edge-on figure assumes an azimuth that something holds.

#### The line items of the drag bracket


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

#### The buffer against the deficit it covers


The buffer fraction is an input to the loop and is not re-derived from the hover energy the four closures need. What the buffer supplies is the hover demand less what the engine can deliver, taken at the electrical bus where the buffer sits: the rotor shaft power divided by the machine and power-electronics efficiencies (0.92 and 0.95), less the engine's shaft power times the generator efficiency (0.90).

| Closure | Deficit at the bus | Per kilogram of take-off mass | Buffer at 3.6 percent |
|---|---:|---:|---:|
| A | 9.68 kW | 0.1683 kW/kg | 2.07 kg |
| B | 9.74 kW | 0.1744 kW/kg | 2.01 kg |
| C | 9.82 kW | 0.1835 kW/kg | 1.93 kg |
| D | 9.86 kW | 0.1884 kW/kg | 1.88 kg |

The deficit per kilogram spreads by 12 percent across the four closures, and the closure that needs the most per kilogram, D, carries the smallest buffer.

#### The propulsion-mass split


The propulsion fraction of the empty mass is 0.176 to 0.198 across the four closures, in two parts. A fixed 0.108 is back-solved from the reference design's own budget (the code's comment lists propeller, shaft, mount and wiring). The engine term is the engine rating divided by an assumed specific power of 1.0 kW per kilogram: 0.068 at closure D to 0.090 at closure A, following the cruise-sized rating of 3.54 to 5.17 kW. The hover power, 11.4 to 12.5 kW at the rotor shaft, passes through the electrical path whatever the engine is rated at, but the loop computes no hover-rated mass for that path; whatever of it lies in the fixed 0.108 scales with take-off mass, which at fixed disc loading is how hover power scales. The airframe (0.300) and avionics (0.080) fractions are construction constants held common across the three architectures of Section 6.4; they are not results of the ledger.

### S12. Scale: working for Section 6.3

#### The reference pair


The test uses the 50 kg and 1 000 kg reference designs, sized by one method. No closure of Section 6.1 was run at 1 000 kg: the heavy design has no drag bracket and no structural closure, and no heavy-design range is quoted.

Disc loading is held at approximately the same value, 44.2 kg m⁻² at 50 kg and 43.7 at 1 000 kg, so specific hover power is held with it: 0.218 kW kg⁻¹ at the light design and 0.216 at the heavy. That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3. Section 6.2's measure of Bill 3, rotor-shaft hover power over engine shaft rating, is 4.19 at the light design (10.9 kW over 2.6 kW) and 3.98 at the heavy (216.2 kW over 54.3 kW). The two designs rate their engines at different margins over cruise power, 1.53 and 1.39; with the light design's margin, the heavy ratio would be 3.61. The ratio therefore moves by 5 to 14 percent across the factor of twenty, depending on an engine margin the sizing rule does not set. Section 6.2's 2.4 to 3.2 is the same ratio at the four closures. This paragraph compares the reference pair only.

The rule has a price, paid in geometry: the ratio of nose-propeller diameter to span rises from 0.35 to 0.47, and much above 1 000 kg a single nose pair can no longer hold the disc loading, so a second would have to be added.

#### The rotor term of Bill 2


Only the rotor term of Bill 2 is computed at both sizes; the frame term enters both designs as the same multiplier, so it cannot show a scale effect in either direction. At 50 kg the rotor term is 0.0154. At 1 000 kg, eight tip-rotor designs at section lift coefficients from 0.55 to 0.85, all meeting the hover figure of merit, give 0.0045 to 0.0100, that is 0.29 to 0.65 of the light value; the design at the light design's section lift coefficient, 0.68, gives 0.0068. Within the blade-element and section-polar model the section Reynolds number accounts for the fall: the median section Reynolds number rises from about 8.2 × 10⁴ to 5.6 × 10⁵, and the heavy blade brought down to the light design's Reynolds number gives 0.0181, 1.18 times the light value. The other candidates are excluded. The heavy blade is the more solid (1.33 times), which would raise its drag rather than lower it; dynamic pressure cancels (between 30 and 40 m s⁻¹ the heavy term changes by a factor of 0.911, against the 0.562 a dynamic-pressure effect would give); and the design tip speed (210 m s⁻¹) and the hub fraction (15 percent of radius) are the same at both sizes. This is a decomposition inside the model rather than a causal claim beyond it.

#### Bill 1


Both buffer figures are inputs: 0.036 of take-off mass in the light closures and 0.040 in the heavy design's sizing. A change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction. A buffer sized to the hover deficit at the same specific power would track hover power and engine rating, which are the Bill 3 measures, so that derivation cannot test whether Bill 1 separates.

#### The rotation time


The transition is where the square–cube relation is paid. The heavy design's pitch inertia is 255 times the light design's and its available control moment 41 times, so to keep the light design's moment margin it must rotate in about 5 s rather than 2 s (4.96 s computed; the heavy design uses 5.1 s). A larger aircraft of this type turns more slowly, and must.

### S13. Contracts: working for Section 6.4

#### The three contracts


Range in the sizing loop is R = f_fuel E* η_chain (L/D)/g, with E* the fuel's specific energy and η_chain the energy chain from fuel to thrust. The three architectures share E* and the chain apart from the propeller efficiency, which enters η_chain, and they differ in L/D. The three contracts differ only in the fuel fraction f_fuel:

1) fixed fuel fraction: every architecture carries 0.16 of its own take-off mass as fuel, so take-off mass cancels from range;
2) fixed fuel mass: every architecture carries the fuel this configuration carries at that closure, 9.20, 8.94, 8.56 and 8.37 kg at closures A to D, as a fraction of its own take-off mass;
3) fixed take-off mass and payload: every architecture is held at this configuration's take-off mass with the same 13 kg payload, and its fuel is what remains after its empty mass, so every kilogram of architecture-specific hardware is a kilogram of fuel not carried.

#### The per-closure numbers


Range of the lift-plus-cruise layout relative to this configuration (positive: lift-plus-cruise ahead), and the mass ratio under the first contract:

| Closure | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass | Shift, first to third | Lift-plus-cruise mass / this configuration's, first contract |
|---|---:|---:|---:|---:|---:|
| A | +67.8 % | +40.2 % | +1.1 % | 66.8 points | 1.392 |
| B | +55.3 % | +27.5 % | −13.0 % | 68.3 points | 1.433 |
| C | +83.9 % | +53.5 % | +7.3 % | 76.6 points | 1.378 |
| D | +70.2 % | +40.1 % | −6.5 % | 76.7 points | 1.409 |

The tilting layout, credited with no cruise penalty, is 93 to 141 percent ahead under every contract at every closure.

#### Without the common buffer


If the competitors carry no buffer and rate their engines to the hover demand, the lift-plus-cruise layout does not close at any of the four closures under a fixed fuel fraction or a fixed take-off mass; under a fixed fuel mass it is 38 to 47 percent behind this configuration. This case is not used in Section 6.4's comparison; it shows only the direction of the choice to hold Bill 3 common.

#### Sensitivity


| Case | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass | Shift, first to third |
|---|---:|---:|---:|---:|
| As declared (lift group 10 % of take-off mass, competitors' propeller efficiency 0.80) | +55 to +84 % | +28 to +54 % | −13 to +7 % | 67 to 77 points |
| Lift group 5 % of take-off mass | +55 to +84 % | +47 to +76 % | +36 to +65 % | 14 to 24 points |
| Lift group 15 % of take-off mass | +55 to +84 % | +8 to +31 % | −62 to −50 % | 117 to 134 points |
| All three at this configuration's propeller efficiency | +33 to +45 % | +6 to +17 % | −33 to −25 % | 65 to 72 points |
| Lift-plus-cruise drag as a fixed increment, not a ratio | +59 to +75 % | +31 to +45 % | −13 to +5 % | 67 to 75 points |

With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every closure; with a heavier one this configuration leads under a fixed take-off mass at every closure; with a common propeller efficiency a reversal appears at every closure. The quantities that decide the sign are assumed for the competitor rather than measured: its lift-group mass fraction and its propeller efficiency. The sign under a fixed take-off mass is not a result about the architectures; it is a result about those quantities.

### S14. What does not close: working for Sections 3, 6.2 and 7

#### The measured store figures


The flown system is a 24-series nickel–cobalt–manganese pack designed, bench-tested and flown in a 210 kg-class electric VTOL aircraft [25]. As a flown system (24S4P) it is rated at 0.892 kW per kilogram continuous; its 13.5 kg unit pack (24S1P) is rated at 0.724 kW per kilogram continuous. Discharged on the bench at its highest tested rate, 10.68C (235 A), the unit pack delivered 1 394 Wh in about 249 s, on average about 1.5 kW per kilogram for about four minutes, and reached 55.1 °C against the 60 °C limit its authors adopted. Against that bench average the take-off demand of the four closures, 5.5 to 6.1 kW per kilogram of buffer, is 3.7 to 4.1 times, and hover alone, 4.7 to 5.2 kW per kilogram, is 3.1 to 3.5 times.

#### The loop closed again on a measured store


Closing the loop on a measured store is a sensitivity of the package, not a second aircraft. The buffer is derived inside the loop from the take-off demand at a given specific power; everything else is Section 6.1's: the same fractions, including an airframe at thirty percent of take-off mass, and the same wing loading, disc loading and aspect ratio, so the lift-to-drag ratio is carried unchanged and, with the fuel fraction held, so is the range. These masses are the Section 6.1 package with one input changed. They are not a structural closure at 100 kg, and whether the airframe fraction holds at twice the mass it was set at is not established.

| Buffer specific power, per kilogram of buffer | Take-off mass | Buffer | Change from Section 6.1 |
|---|---:|---:|---:|
| As Section 6.1 implies: 5.5 to 6.1 kW kg⁻¹ | 52.3 to 57.5 kg | 3.6 % | — |
| 4 kW kg⁻¹, the design-study assumption [26] | 56.6 to 61.2 kg | 5.0 to 5.5 % | +6.5 to +8.2 % |
| About 1.5 kW kg⁻¹, the unit pack's bench rate | 94.6 to 101.2 kg | 13.4 to 14.7 % | +76 to +81 % |
| 0.892 kW kg⁻¹, the flown system's continuous rating | about 335 kg | 22 to 25 % | set by nearness to non-closure |
| 0.724 kW kg⁻¹, the unit pack's continuous rating | does not close | — | — |

If Section 6.1's take-off masses are kept instead of re-closing at the bench rate, the payload falls to about 7 kg rather than 13. At the flown system's continuous rating the loop only just closes, and the mass it returns is set by how near the loop is to not closing rather than by anything about the aircraft.

#### The open questions


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

