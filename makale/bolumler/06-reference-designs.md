# 6. Reference designs at two scales

A configuration argument is only as good as its willingness to become a number. This
section sizes two aircraft from the arrangement of Section 4 — one at 50 kg and one at
1000 kg, a factor of twenty apart in mass — using the same equations, the same
assumptions and the same architecture. The two points are not a light version and a
heavy version of different aircraft. They are the same aircraft at two sizes, and the
purpose of presenting both is to show that the proportions hold.

Every number below is calculated, not measured. Section 8 says what that means.

## 6.1 Sizing method

The method is elementary and the equations are given so that any result in this section can be
checked by hand.

**Hover.** Thrust equals weight and induced power follows from momentum theory,
v_i = √(T/2ρA) and P_i = T^1.5/√(2ρA), with disc loading DL = T/A as the governing parameter;
figure of merit gives shaft power.

**Cruise.** C_L = W/(qS) fixes the lift coefficient at the chosen speed, C_D = C_D0 + C_L²/(πARe)
gives the drag, and L/D is their ratio **at the cruise condition, not at the aircraft's best
point**. The familiar L/D_max = 0.5√(πARe/C_D0) occurs at one particular speed — 25.3 m s⁻¹ for
the light design, only 1.26 times its stall speed. Cruising there would leave too little margin,
so both designs cruise at 1.49 times stall and accept the lift-to-drag ratio that condition
gives. Using the maximum value while quoting a different cruise speed would overstate the
range, and an earlier version of this paper did exactly that.

**Range.** The series-hybrid chain is stated link by link rather than folded into one
efficiency, because the result is sensitive to it and a reader should be able to disagree with
any single link: engine 0.28, generator 0.90, power electronics 0.95, electric machine 0.92,
propeller 0.80 — **overall 0.176**. Fuel energy is 12.9 kWh kg⁻¹. The engine figure matters
most: 0.28 is representative of a small four-stroke at its best operating point, and it is why
the range figures below are lower than an optimistic estimate would give.

**Control.** Tip-pair thrust follows from M = 2TL = Iα, with the transition manoeuvre as the
sizing case.

**Assumptions carried throughout:** sea-level density; no compressibility; span efficiency
e = 0.85; C_D0 = 0.0248 for the light design, which is generous for a clean blended-wing body
and absorbs the tip-frame contribution of Section 5.2 — that contribution is 0.0043, or
seventeen percent of the assumed value, so the assumption is self-consistent rather than
optimistic. Both are carried as assumptions throughout, so that every downstream figure rests
on one stated basis. Section 6.6 computes both and reports what the computation does to them:
it bounds them rather than replacing them, which is a weaker but more honest claim.

## 6.2 Light reference design — 50 kg

| Quantity | Value |
|---|---:|
| Maximum take-off mass | 50 kg |
| Root chord | 0.97 m |
| Tip chord | 0.236 m |
| Span | 3.45 m |
| Wing area | 1.98 m² |
| Aspect ratio | 6.03 |
| Wing loading | 25.3 kg m⁻² |
| Main propeller diameter | 1.20 m |
| Disc loading | 44.2 kg m⁻² |
| Tip propeller diameter | 0.20 m |
| Frame post length | 0.71 m each direction |
| Stall speed | 20.1 m s⁻¹ |
| Cruise speed | 30 m s⁻¹ (108 km h⁻¹) |
| Cruise L/D | 12.0 |
| Hover power | 10.9 kW |
| Cruise power, electrical | 1.7 kW |
| Engine rating | 2.6 kW |
| Battery buffer | 1.8 kg (3.6 % MTOW) |
| Fuel | 8 kg |
| **Endurance** | **14.8 h** |
| **Range** | **1 598 km** |
| Transition time | 2 s |

The mass budget behind this — 30 % structure, 16 % propulsion chain, 4 % battery, 8 %
avionics and control, 16 % fuel, leaving 26 %, or 13 kg, for payload — is the allowance the
design is sized against, and it is asserted here rather than derived. Section 6.7 rebuilds
it from components and finds it can be met, with 2.2 kg in hand, on one condition that is
not demonstrated: a structural areal density no greater than 1.78 kg m⁻². Paper aircraft
are habitually lighter than the ones that get built, and no allowance for that has been
paid in this table beyond the contingency inside the build-up. Section 8.2 keeps this as
the single most likely place for these numbers to be wrong.

## 6.3 Heavy reference design — 1000 kg

| Quantity | Value |
|---|---:|
| Maximum take-off mass | 1000 kg |
| Root chord | 3.25 m |
| Span | 11.55 m |
| Wing area | 22.24 m² |
| Wing loading | 45.0 kg m⁻² |
| Main propeller diameter | 5.40 m |
| Disc loading | 43.7 kg m⁻² |
| Tip propeller diameter | 0.67 m |
| Frame post length | 2.38 m each direction |
| Cruise speed | 40 m s⁻¹ (144 km h⁻¹) |
| Cruise L/D | 13.6 |
| Hover power | 216.2 kW |
| Cruise power, electrical | 39.2 kW |
| Engine rating | 54.3 kW |
| Battery buffer | 40 kg (4.0 % MTOW) |
| Fuel | 160 kg |
| **Endurance** | **12.6 h** |
| **Range** | **1 814 km** |
| Transition time | 5.1 s |

The heavy design has a longer range than the light one despite a shorter endurance.
Both effects come from the same source: the larger aircraft cruises faster and, at a
higher Reynolds number, achieves a lower zero-lift drag coefficient and therefore a
better lift-to-drag ratio. Nothing in the architecture was changed to obtain this.

## 6.4 Scale behaviour

One qualification applies throughout: this is the scaling of the analytical sizing model — of
powers, loadings and mass *fractions*. Whether the heavy design's structure closes depends on
how shell areal density grows with size, which was not measured. Figure 11 shows the two
designs at a common scale. Four properties are preserved and one is not.

**Disc loading is held constant** — 44.2 and 43.7 kg m⁻². This is the rule that governs the
sizing rather than a coincidence of it. Hover power per unit weight is √(DL/2ρ), so fixing disc
loading fixes specific hover power: hover power rises from 10.9 kW to 216.2 kW, a factor of 19.8
against a mass factor of 20. **Hover power grows linearly with mass rather than as the L^3.5 of
the classical result**, and that is the whole benefit of fixing it. The cost is that disc area
must then grow as L³ rather than L², which for a fixed number of propellers is impossible. The
architecture has two ways out and uses both: a coaxial pair may be added at no architectural
cost, since every pair is torque-balanced on its own; and geometric similarity is not held.

**The propeller therefore grows faster than the airframe.** Wing loading rises from 25.3 to
45.0 kg m⁻², so span grows by 3.35 against the 4.50 by which the main propeller must grow. The
ratio of propeller diameter to span rises from 0.35 to 0.47: the heavy design is not the light
design photographed from further away, and its propeller occupies almost half its span. Nothing
in the argument fails because of this — the propeller is the nose of the aircraft rather than an
appendage, and disc loading is what is being held — but the claim that the configuration keeps
its proportions applies to the quantities named here and not to every dimension. Much above
1000 kg, a single nose pair can no longer hold the disc loading and a second must be added.

**The buffer fraction is preserved** (3.6 % of MTOW at 50 kg, 4.0 % at 1000 kg), so the
mechanism by which Bill 3 is avoided does not degrade with size, and **the frame drag fraction is
preserved** because frontal and wing area both scale as L².

**Transition time does not scale, and this is the exception.** The rotating moment follows
M = Iα with I ∝ mL², so the moment needed to turn the aircraft in a fixed time grows much
faster than the aircraft. Scaling the light design's two-second rotation to 1000 kg would demand
221.5 kW from the tip propellers — 102 % of hover power, which is to say it is not available:

**Table 4.** Tip-propeller power required to rotate the heavy reference design.

| Rotation time | Tip-propeller power, 4 total | Fraction of hover power |
|---:|---:|---:|
| 2 s | 221.5 kW | 102 % |
| 3 s | 65.6 kW | 30 % |
| 4 s | 27.7 kW | 13 % |
| **5.1 s** | **13.4 kW** | **6 %** |

**The rule is that a larger aircraft turns more slowly.** The heavy design rotates in 5.1 s at
six percent of hover power — not a round number but the rotation time at which it holds the same
control margin the light design holds at two seconds (Section 7.6). The constraint is less costly
than it looks, because Section 7.4 shows a slower rotation loses *less* altitude: the scaling
penalty on transition time works with the penalty on control power rather than against it. The
classical objection to scaling a VTOL aircraft — hover power growing as L^3.5 against power
available as L³ — is removed on the hover side by fixing disc loading. It is not removed on the
transition side, and Table 4 is where it reappears: **the rotation is the one place in this
aircraft where the square–cube relation is still paid in full.**

## 6.5 Context

The following aircraft occupy the same mass range. They are listed to locate the reference
designs in a real field, not to rank them.

| Aircraft | MTOW | Payload | Payload fraction |
|---|---:|---:|---:|
| HAVELSAN BAHA [8] | 28 kg | 2 kg | 7.1 % |
| Textron Aerosonde Mk 4.7 VTOL [9] | 45.4 kg | 9.1 kg | 20.0 % |
| Baykar KALKAN [10] | 75 kg | ~3 kg internal | 4.0 % |
| HAVELSAN BULUT [11] | not published | 5 kg | — |
| Elroy Air Chaparral [12] | 865 kg | 136 / 227 kg | 15.7 / 26.2 % |
| Sabrewing Rhaegal-A [13] | 1400 kg | 360–450 kg | 25.7–32.1 % |
| Pipistrel Nuuva V300 [14] | 1700 kg | 408 kg | 24.0 % |

All entries are from manufacturers' published material; payload definitions are not consistent
between them and empty weights are generally not published.

Three statements can be made and a fourth cannot. The field is real and populated at both ends
of the range. Payload fraction rises with size across it, from a few percent to roughly a
quarter, which is the ordinary consequence of fixed costs not scaling down. And **none of these
aircraft connects an internal-combustion engine directly to a lifting rotor** — every one uses
either a generator or separate electric lift, which is independent confirmation that the series
arrangement of Section 4.3 is the practical choice at this scale rather than an unusual one.

**The fourth statement — that the reference designs outperform these aircraft — is not made.**
Sections 6.2 and 6.3 are calculated from a mass budget with an unpaid structural margin; this
table describes aircraft that exist and fly. Placing a calculation beside a measurement and
declaring a winner would be a category error. Several entries are also fully electric, for
which endurance is set by battery specific energy rather than by configuration, so comparing
them with a fuel-burning design would compare energy sources rather than architectures. What
could properly be compared, once such aircraft are built, is **range at similar payload** — a
configuration carrying a comparable load further is making an architectural claim, while one
carrying a heavier load is making a claim about mass budgeting, which is the least validated
part of this study.

## 6.6 Independent checks on the two assumed coefficients

Both coefficients carried through Sections 6.2 and 6.3 were assumed. Both have since been
computed, and the computations are reported in full in Supplementary S1. Neither replaces its
assumption in the figures above — those are quoted on one stated basis throughout — but each
bounds it, and the direction of each is stated here.

**Zero-lift drag.** A Reynolds-averaged solution of the wing and body gives C_D0 between
0.0120 and 0.0148, against the 0.0248 assumed. The spread is the turbulence closure:
0.01475 with Spalart–Allmaras and 0.01201 to 0.01253 with k-ω SST, eighteen percent apart
at matched wall resolution. **The assumption lies above the whole of that range**, so it is
conservative rather than optimistic. Two things S1 does not settle: the solutions are fully
turbulent, so the clean-surface figure of 0.0073 from the strip method is untested and the gap
between it and 0.0120–0.0148 is now the largest single uncertainty in the zero-lift drag; and
the wall-resolved SST case admits more than one stationary solution, two converged starts
settling 4.3 percent apart in the pressure component.

**Span efficiency.** A vortex-lattice solution gives an inviscid span efficiency of 0.990 for
the untwisted planform and 0.859 for the wing twisted to trim. Those are not the quantity the
drag build-up needs: an Oswald-type efficiency also carries the viscous drag due to lift. An
earlier version of this paper converted between them with a borrowed rule of 85 to 90 percent
and reported an implied value of 0.735 to 0.78. S1 computes the conversion instead, on this
planform, by calling the section solver at **each spanwise station's own local lift
coefficient** rather than at zero lift and integrating the profile drag across the span — the
two-dimensional-viscous-coupled-to-three-dimensional-circulation construction of the non-linear
vortex-lattice literature [40]. Before any number is taken from it, the strip decomposition is
checked against the solver it comes from: the strip loads reproduce the solver's own lift
coefficient to six decimal places.

| | Inviscid e | **Oswald e** | Ratio |
|---|---:|---:|---:|
| Untwisted planform | 0.990 | 0.931 | 0.940 |
| **Trimmed, −9° washout** | **0.859** | **0.817** | **0.951** |

**The borrowed rule was wrong in the favourable direction and the conclusion is unchanged in
the unfavourable one.** The viscous penalty is 5 to 6 percent rather than 10 to 15, but the
trimmed wing starts from 0.859, so the Oswald efficiency lands at **0.817 — below the assumed
0.85 by 3.9 percent**. At that value the cruise lift-to-drag ratio is **11.87 against 12.04**,
and the range figures of Section 6.3 are optimistic by the same 1.4 percent. Two limits belong
with the number: the vortex-lattice sections are symmetric, so a cambered section reaching the
same local lift coefficient at lower incidence would carry less drag and the figure is a
**lower bound**; and strip integration ignores sweep, which at 45° at the root is not a small
omission, though the alternative — simple-sweep theory — halves the profile drag, which is a
sign that the transformation does not apply to skin friction rather than a measure of the
uncertainty.

**What the vortex-lattice method is being asked for, and a bound on it that has no bound.**
Four results here come from a vortex-lattice solution: the span efficiency, the neutral point,
the twist required to trim, and the roll damping. Falkner separates the quantities the method
settles quickly — spanwise circulation, local aerodynamic centre — from those it does not, and
every quantity taken here is of the first kind [24]. But a published comparison on a
blended-wing-body of this class found the vortex-lattice lift coefficient low by **thirty to
thirty-eight percent** against RANS, and excluded the method from its trim analysis on that
basis [39]. The deviation there is nearly constant with incidence, which is the signature of a
multiplicative error in the magnitude of the loading rather than an error in its distribution —
and a factor common to lift and moment cancels in a ratio of derivatives. That argument depends
on the moment scaling with the lift, and the pitching-moment comparison in that source is
published with its values withheld. **The vortex-lattice results here therefore carry an
untested magnitude error of unknown size, bounded above by a published comparison on a similar
configuration, and every use made of them is of a kind a magnitude error does not disturb.**
Section 8 lists settling this as the one exposure in the aerodynamic chain with no bound at all.

## 6.7 A component build-up of the mass budget

The sizing above assumes an empty-mass fraction rather than deriving one. Supplementary S2
builds the 50 kg design's mass item by item — structure from wetted area and an assumed shell
areal density, tip frames sized by a vertical landing case, propulsion, energy, avionics and
systems — and reports the break-even value of every assumption in it.

**The build-up closes, and it closes on one number.** The total is 11.88 kg against a 14.08 kg
allowance, leaving 2.2 kg unallocated. It closes on the condition that the average structural
areal density does not exceed **1.78 kg m⁻²**, against the 1.5 assumed; at 1.78 the payload is
gone. A doctoral study of unmanned-aircraft sizing reports 1.05 kg m⁻² for a small UAV's
monolithic composite fuselage shell supported by an internal structure [50], which places the
assumption inside the range small composite airframes are built to without establishing that
this airframe reaches it — that shell is carried by an internal structure, while this one is
the wing and carries flight loads directly.

**The build-up came in lighter than the target, and that is a warning rather than a result.**
Paper aircraft are habitually lighter than the aircraft that get built. What S2 does not
contain is buckling, torsion, local load introduction, aeroelastic sizing, fasteners, adhesive,
paint, or the mass of anything the design has not yet specified — and the 2.2 kg of margin is
what all of those must fit into. Section 8.2 states the item as bounded from below rather than
demonstrated.
