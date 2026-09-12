# 8. Limitations

This is a configuration study. It contains no experimental validation of any kind, and
the numbers in it are the output of elementary methods applied to a set of assumptions.
This section states what those limits are, in enough detail that a reader can judge how
much weight each result will bear. Several of the items below were discovered during the
study and changed its results; they are recorded here rather than smoothed away.

## 8.1 What is not shown

**No part of this study has been validated experimentally.** No wind-tunnel test, no flight
test, no hardware. Everything here is calculation, and the calculations rest on assumptions
stated in the sections that use them. Supplementary S5 enumerates every limitation item by item
with the break-even value of each assumption that has one. This section states the ones that
bear on the conclusions.

## 8.2 The three that could change a conclusion

**The buffer's specific power is the most exposed number in the paper.** Bill 3 is avoided by
sizing the engine for cruise and supplying the hover excess from a battery buffer, and the light
design's buffer implies **5.63 kW kg⁻¹** to hover and **6.48 kW kg⁻¹** to leave the ground. Both
figures are taken at the electrical bus, where the buffer is; an earlier version of this paper
differenced the rotor shaft against the engine shaft and reported 4.61, which understated the
demand by a fifth. A 24S nickel–cobalt–manganese pack designed, built, bench-tested from 0.2 C
to 10.68 C and flown in an electric VTOL aircraft measures **724 W kg⁻¹** continuous for the unit
pack and **892 W kg⁻¹** for the flight system, reaching roughly 1.5 kW kg⁻¹ at its maximum tested
rate with a thermal margin of 4.9 °C [47]. A NASA-funded design study adopts 4 kW kg⁻¹ and states
that this is "about twice that of existing batteries" [48]. Sized at the measured thermal ceiling
the buffer is **6.8 kg rather than 1.8 kg**, against 2.2 kg of unallocated mass; sized at the
measured continuous figure, 11.4 kg, which is nearly the whole payload. **The light design's mass
budget does not close at any measured specific power.** The defence available earlier — that a
short-duration buffer is a different product from an energy-optimised automotive pack — does not
survive, because the source above *is* that product. The gap to be closed is a factor of 3.8 on
the measured ceiling and 6.3 on the measured continuous rate. What would resolve it is a pack
demonstrating that at acceptable temperature, or a heavier buffer carried at the cost of payload
fraction.

**The aircraft leaves the ground on its control propellers, and that is a dependency rather than
a design feature.** Section 6.1 sizes hover power at thrust equal to weight, so the primary
propulsor supplies T/W = 1.00 exactly and no more. The margin to take off comes from the four
tip pairs, which raises the achievable ratio to 1.066 with full rotation authority retained and
1.132 with none — never to the 1.2 an earlier version of Section 7.4 assumed. Three things follow
and none of them is closed here: the take-off margin and the attitude authority are drawn from
the same four propellers and compete; the buffer must carry the tip pairs as well, which is the
6.48 kW kg⁻¹ above; and a rotation entered from rest, rather than from a climb, now loses 14.7 m
at the light design's own two seconds. The entry climb of Section 7.4 is therefore a requirement
of the configuration and not a refinement of it.

**The mass budget is bounded from below and the bound is thin.** The component build-up of
Supplementary S2 totals 11.88 kg against a 14.08 kg allowance, on the condition that average
structural areal density does not exceed **1.78 kg m⁻²** against the 1.5 assumed; at 1.78 the
payload is gone. A doctoral study of UAV sizing reports 1.05 kg m⁻² for a small UAV's monolithic
composite fuselage shell supported by internal structure [50], which places the assumption inside
the range small composite airframes are built to without establishing that this airframe reaches
it — that shell is carried by internal structure, while this one is the wing and carries flight
loads directly. The build-up contains no buckling, torsion, local load introduction, aeroelastic
sizing, fasteners, adhesive or paint, and 2.2 kg is what all of those must fit into. **Paper
aircraft are habitually lighter than the aircraft that get built.**

**The transition pitching moment is not computed, and Section 7.6 shows the computation is not
currently reliable for anyone on this class of configuration.** Three methods of three fidelities
fail above roughly ten degrees of incidence, the highest of them against wind-tunnel measurement
[39,44], and the incidences this aircraft passes through lie inside that band. **This item
belongs to measurement.** It asks for the pitching moment to about twenty-two degrees at low
dynamic pressure, on the outboard half of the wing — the inboard half lies in the slipstream and
sees four to eight degrees — and for trim at cruise incidence.

## 8.3 What is assumed rather than derived

The planform's sweep, taper and thickness distributions were **chosen, not optimised**. The
centre of gravity is a packaging assumption. The zero-lift drag coefficient of 0.0248 and the
span efficiency of 0.85 are assumptions; Section 6.6 bounds both by calculation and neither
replaces its assumption — the span efficiency computes to **0.817, optimistic by 3.9 percent**,
worth 1.4 percent of cruise lift-to-drag ratio and of the ranges quoted. Torque balance is exact
at cruise only, leaving a small residual in hover. The comparative sizing of Section 5.5 is
conditional on the two competing architectures being modelled at the same level of detail as
this one, which they are not: they are modelled from published fractions.

**The vortex-lattice results carry an untested magnitude error.** A published comparison on a
blended-wing-body of this class found the vortex-lattice lift coefficient low by thirty to
thirty-eight percent against RANS [39]. Section 6.6 argues that a near-constant multiplicative
error of that kind cancels in the ratios this paper takes from the solution — neutral point,
static margin, twist effectiveness — but the check that would confirm it is withheld in that
source. **This is the one exposure in the aerodynamic chain with no bound at all.**

## 8.4 What is sized but not closed

Attitude control is sized in every axis and closed in none. Roll asks for **ΔC_L ≈ 0.12** from
the strip, which published fence and Gurney data make plausible without establishing it for this
geometry, and the strip's measured weaknesses — degradation in turbulence, contested post-stall
behaviour, a dead band below seven percent of travel — all fall in conditions this configuration
uses it in. Directional stability asks for a **39 mm** fairing chord on a frame that already
exists, at a Reynolds number near 80 000 where thin symmetric sections are measured to be
nonlinear about zero incidence; whether such a fairing develops the side force credited to it is
not established, and the toe-out its aspect ratio requires carries a stall-related failure mode
at large sideslip that has not been computed. Hover disturbance rejection, ground handling,
crosswind and vertical descent have been checked only to order of magnitude or not at all.

## 8.5 Where this could most efficiently be attacked

Supplementary S5 lists six places. Two have been carried out and are folded into Section 6.6: a
three-dimensional solution for the centre body, and a viscous solution of the twisted planform
station by station. Of the remaining four, the one with no bound at all is a Reynolds-averaged or
panel solution of this planform's loading, to bound the magnitude question above. **Three of the
four can be carried out computationally; the fourth cannot, and saying otherwise was the most
consequential thing this study got wrong about itself.** Transition controllability rests on a
pitching moment that three methods of three different fidelities fail to predict above roughly
ten degrees of incidence, the highest of them against wind-tunnel measurement, so it is blocked
on data rather than on effort — as is the fin derivative of Section 4.4, for the reason
Supplementary S3 gives. An earlier version of this section stated that none of the four required
an experiment. The configuration is described in enough detail in Sections 4 and 6 for another
group to attempt any of them independently, by whichever of the two routes each one needs. The computational setup, the
grid-convergence study and the record of what failed along the way are in the repository, so
every result here can be re-run and checked rather than taken on trust.
