# 4. Discussion

This section places the results against existing aircraft and existing
literature, then states what is not shown. Sections 4.1 and 4.2 are interpretation;
Sections 4.3 to 4.7 are limitations, ordered by whether they could change a conclusion.

## 4.1 Context

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
arrangement of Section 2.9 is the practical choice at this scale rather than an unusual one.

**The fourth statement — that the reference designs outperform these aircraft — is not made.**
Sections 3.7 and 3.8 are calculated from a mass budget with an unpaid structural margin; this
table describes aircraft that exist and fly. Placing a calculation beside a measurement and
declaring a winner would be a category error. Several entries are also fully electric, for
which endurance is set by battery specific energy rather than by configuration, so comparing
them with a fuel-burning design would compare energy sources rather than architectures. What
could properly be compared, once such aircraft are built, is **range at similar payload** — a
configuration carrying a comparable load further is making an architectural claim, while one
carrying a heavier load is making a claim about mass budgeting, which is the least validated
part of this study.

## 4.2 Why the market looks the way it does

One observable consequence supports the argument, and it has been stated independently.
Surveying the field, the study cited above concludes that multirotors are efficient in
hover and suited to short-range missions, that vectored-thrust aircraft are efficient in
cruise and suited to long-range missions, and that "lift plus cruise eVTOLs are a
compromise, but they are slowed down by the drag of the lift propellers."

 Hybrid VTOL aircraft occupy a narrow
band of the mission space. Below it, where range requirements are short, a multirotor
is cheaper and simpler and pays none of these bills because it never claimed cruise
efficiency. Above it, where range requirements are long, a runway-launched fixed-wing
aircraft is more efficient and pays none of them because it never claimed vertical
capability. The hybrid sits between the two, and the width of that band is set by how
much cruise efficiency the architecture had to surrender.

An architecture that surrenders less does not merely perform better inside the band. It
widens the band.


This is a configuration study. It contains no experimental validation of any kind, and
the numbers in it are the output of elementary methods applied to a set of assumptions.
This section states what those limits are, in enough detail that a reader can judge how
much weight each result will bear. Several of the items below were discovered during the
study and changed its results; they are recorded here rather than smoothed away.

## 4.3 What is not shown

**No part of this study has been validated experimentally.** No wind-tunnel test, no flight
test, no hardware. Everything here is calculation, and the calculations rest on assumptions
stated in the sections that use them. Supplementary S5 enumerates every limitation item by item
with the break-even value of each assumption that has one. This section states the ones that
bear on the conclusions.

## 4.4 The three that could change a conclusion

**The buffer's specific power is the most exposed number in the paper.** Bill 3 is avoided by
sizing the engine for cruise and supplying the hover excess from a battery buffer, and the light
design's buffer implies **5.63 kW kg⁻¹** to hover and **6.48 kW kg⁻¹** to leave the ground. Both
figures are taken at the electrical bus, where the buffer is; an earlier version of this paper
differenced the rotor shaft against the engine shaft and reported 4.61, which understated the
demand by a fifth. A 24S nickel–cobalt–manganese pack designed, built, bench-tested from 0.2 C
to 10.68 C and flown in an electric VTOL aircraft measures **724 W kg⁻¹** continuous for the unit
pack and **892 W kg⁻¹** for the flight system, reaching roughly 1.5 kW kg⁻¹ at its maximum tested
rate with a thermal margin of 4.9 °C [47]. A NASA-funded design study adopts 4 kW kg⁻¹ and states
that this is "about twice that of existing batteries" [48]. The defence available earlier — that a
short-duration buffer is a different product from an energy-optimised automotive pack — does not
survive, because the source above *is* that product.

**An earlier version of this section then compared a 6.8 kg buffer against 2.2 kg of unallocated
mass and concluded that the budget does not close at any measured specific power. That comparison
was a subtraction inside a box that had been sized on the number being replaced, and the
conclusion drawn from it was too strong.** A heavier buffer raises take-off mass, which raises
hover power, which raises the buffer again; at constant disc loading that feedback is linear
rather than divergent, so it accumulates to a finite answer and the answer is not where the
subtraction pointed. Closing the loop — holding wing and disc loading, holding the fuel fraction
so that range is preserved, and rebuilding the component budget at each step — gives:

| Buffer specific power | Take-off mass at 13 kg payload | Buffer | Range | Payload if held at 50 kg |
|---|---:|---:|---:|---:|
| 0.724 kW kg⁻¹, measured continuous | **no solution** | — | — | 0.9 kg |
| 0.892 kW kg⁻¹, measured continuous | 162.0 kg | 42.4 kg | 1 600 km | 3.9 kg |
| **1.5 kW kg⁻¹, measured thermal ceiling** | **68.9 kg** | **10.7 kg** | **1 600 km** | **9.2 kg** |
| 5.63 kW kg⁻¹, assumed here | 50.0 kg | 1.8 kg | 1 600 km | 13.0 kg |

*The range column is constant by construction: the loop holds the fuel fraction so that range is
preserved while mass is solved for. Its value is the published one; on the drag bracket of
Section 3.6 the same column would read 1 173 to 1 442 km throughout, without changing any mass in
the table.*

The right-hand column is the same loop run the other way and it needs its arithmetic stated,
because the figure is not a subtraction from the payload. Take-off demand at 50 kg is 11.66 kW at
the bus, so a 1.5 kW kg⁻¹ buffer masses 7.78 kg against the 1.8 kg already budgeted. The extra
5.98 kg does not come off the 13 kg payload directly: the component build-up leaves **2.2 kg
unallocated above the payload**, and the buffer takes that first. Payload falls by the remaining
3.8 kg, to 9.2. **That figure therefore spends the whole of the structural margin** — the 2.2 kg
into which Section 4.4 below says buckling, torsion, local load introduction, fasteners, adhesive
and paint must all fit. Read without that condition the column is too kind by 2.2 kg.

**At the highest rate yet measured on a flown pack the aircraft exists.** It is 38 percent
heavier than the reference design, it carries a buffer of 15.6 percent of take-off mass rather
than 3.6, and its range is unchanged because the fuel fraction is what sets range. Held instead
at 50 kg, it carries 9.2 kg rather than 13. At the pack's *continuous* rating the loop does not
converge at all for the take-off demand, so the sharper statement survives there.

The correction cuts both ways and both should be stated. The reference design is not unreachable,
which is what the earlier sentence implied; and the comparison that opens this paper is made at
50 kg against a lift-plus-cruise layout at 86 kg, so an obvious reading is that at a measured pack
the margin falls to 69 against 86 — twenty percent rather than forty-two. **That reading is wrong,
and it is wrong in this configuration's favour, which is why it is corrected here rather than
left standing.** It grows A on the measured pack while holding B at a mass sized on the assumed
one. Section 3.6 now re-sizes all three architectures on the same buffer fraction, and the
lift-plus-cruise layout is the one that suffers: its hover power per unit mass is the highest of
the three, the buffer feeds back through hover power, and somewhere between eighteen and twenty
percent of take-off mass its budget stops closing altogether. **What the measured pack costs is
not this architecture's margin but the competing architecture's existence.** The figure that does
move against this paper is the rotor drag of Section 3.3, which takes the mass margin from
forty-two percent to thirty-seven and reverses the range comparison under one of the three
contracts.

**The aircraft leaves the ground on its control propellers, and that is a dependency rather than
a design feature.** Section 2.12 sizes hover power at thrust equal to weight, so the primary
propulsor supplies T/W = 1.00 exactly and no more. The margin to take off comes from the four
tip pairs, which raises the achievable ratio to 1.066 with full rotation authority retained and
1.132 with none — never to the 1.2 an earlier version of Section 3.15 assumed. Three things follow
and none of them is closed here: the take-off margin and the attitude authority are drawn from
the same four propellers and compete; the buffer must carry the tip pairs as well, which is the
6.48 kW kg⁻¹ above; and a rotation entered from rest, rather than from a climb, now loses 14.7 m
at the light design's own two seconds. The entry climb of Section 3.15 is therefore a requirement
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

**The transition pitching moment is not computed, and Section 3.17 shows the computation is not
currently reliable for anyone on this class of configuration.** Three methods of three fidelities
fail above roughly ten degrees of incidence, the highest of them against wind-tunnel measurement
[39,44], and the incidences this aircraft passes through lie inside that band. **This item
belongs to measurement.** It asks for the pitching moment to about twenty-two degrees at low
dynamic pressure, on the outboard half of the wing — the inboard half lies in the slipstream and
sees four to eight degrees — and for trim at cruise incidence.

## 4.5 What is assumed rather than derived

The planform's sweep, taper and thickness distributions were **chosen, not optimised**. The
centre of gravity is a packaging assumption. The zero-lift drag coefficient of 0.0248 and the
span efficiency of 0.85 are assumptions; Section 3.10 bounds both by calculation and neither
replaces its assumption — the span efficiency computes to **0.817, optimistic by 3.9 percent**,
worth 1.4 percent of cruise lift-to-drag ratio and of the ranges quoted. **The drag assumption is
the more serious of the two and it moved this round.** Counting the free-wheeling rotors of
Section 3.3, which no earlier version of the build-up contained, puts the computed bracket at
0.0216 to 0.0380 with 0.0248 inside it rather than above it. Every lift-to-drag ratio, range and
architectural comparison in this paper is computed on 0.0248; **re-deriving them on a bracket that
now surrounds it is the largest single piece of unfinished work here**, and it is more likely to
move the comparative results of Section 3.6 than anything else left open. Torque balance is exact
at cruise only, leaving a small residual in hover. The comparative sizing of Section 3.6 is
conditional on the two competing architectures being modelled at the same level of detail as
this one, which they are not: they are modelled from published fractions.

**The vortex-lattice results carry an untested magnitude error, and the part of the chain it
threatens is not the part that was defended.** A published comparison on a blended-wing-body of
this class found the vortex-lattice lift coefficient low by thirty to thirty-eight percent
against RANS [39]. Section 3.10 argues that a near-constant multiplicative error of that kind
cancels in the ratios this paper takes from the solution — neutral point, static margin, twist
effectiveness — but the check that would confirm it is withheld in that source, so the argument
stands unverified. An earlier version of this section called this the one exposure in the
aerodynamic chain with no bound at all. **It now has one, and the bound points somewhere else.**
Perturbing the spanwise loading shape and re-solving shows that a one-degree mid-span
redistribution moves the neutral point by 0.15 percent of mean chord and the trim twist by 0.38
degrees; the neutral point would need a redistribution of 33 degrees to matter and the trim twist
one of 2.6. **The static margin — the quantity the cancellation argument exists to protect — is
the robust half. The trim twist is thirteen times more sensitive and the argument never covered
it.**

**A Reynolds-averaged solution has since supplied the missing redistribution, on three meshes
rather than one, and the answer is that the threshold is exceeded and the exceedance does not
matter much.** The local loading ratio holds to within five percent of a constant across nine
tenths of the span, which is direct support for the cancellation argument and the first evidence
for it of any kind. Refinement matters: the coarse mesh put the residual at 1.7 degrees of
equivalent redistribution and the converged solution puts it at **2.75 against a 2.6-degree
threshold**, so the first reading was under-resolution rather than agreement. **Carrying the
exceedance through the measured chain moves the trim twist by one degree, the span efficiency
from 0.817 to 0.799, and every cruise efficiency and range in this paper by 0.8 percent** — an
order of magnitude inside the drag bracket already applied to the same numbers. The exposure that
had no bound is therefore bounded, exceeded and quantified, in that order, and the trim chain
stands.

What does not resolve with refinement is the outboard tenth of the span, where the disagreement
is undiminished across a threefold change in cell count. That is where a vortex-lattice method
would be expected to fail and nothing in this paper is taken from that region alone, but a
strip-based estimate that depended on it would not be safe. Two limits belong with all of it: the
runs are untwisted, because the mesh generator has no field for twist; and the overall lift ratio
runs opposite to the published comparison cited above, which the paper reports rather than
reconciles.

## 4.6 What is sized but not closed

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

## 4.7 Where this could most efficiently be attacked

Supplementary S5 lists six places. Two have been carried out and are folded into Section 3.10: a
three-dimensional solution for the centre body, and a viscous solution of the twisted planform
station by station. Of the remaining four, the most valuable is a Reynolds-averaged or
panel solution of this planform's loading — no longer because that exposure is unbounded, but
because it is now the one input a single number would close: Section 3.10 supplies the
sensitivity to a redistribution, and such a solution would supply the redistribution. **Three of the
four can be carried out computationally; the fourth cannot, and saying otherwise was the most
consequential thing this study got wrong about itself.** Transition controllability rests on a
pitching moment that three methods of three different fidelities fail to predict above roughly
ten degrees of incidence, the highest of them against wind-tunnel measurement, so it is blocked
on data rather than on effort — as is the fin derivative of Section 2.10, for the reason
Supplementary S3 gives. An earlier version of this section stated that none of the four required
an experiment. The configuration is described in enough detail in Sections 2 and 3 for another
group to attempt any of them independently, by whichever of the two routes each one needs. The computational setup, the
grid-convergence study and the record of what failed along the way are in the repository, so
every result here can be re-run and checked rather than taken on trust.
