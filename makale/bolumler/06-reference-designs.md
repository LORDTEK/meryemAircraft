# 6. Reference designs at two scales

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

A configuration argument is only as good as its willingness to become a number. This
section sizes two aircraft from the arrangement of Section 4 — one at 50 kg and one at
1000 kg, a factor of twenty apart in mass — using the same equations, the same
assumptions and the same architecture. The two points are not a light version and a
heavy version of different aircraft. They are the same aircraft at two sizes, and the
purpose of presenting both is to show that the proportions hold.

Every number below is calculated, not measured. Section 8 says what that means.

## 6.1 Sizing method

The method is deliberately elementary, and the equations are given so that any result
in this section can be checked by hand.

**Hover.** Thrust equals weight, and induced power follows from momentum theory:

    v_i = √(T / 2ρA)          P_i = T^1.5 / √(2ρA)

with the disc loading DL = T/A as the governing parameter. Figure of merit is applied
to obtain shaft power.

**Cruise.** Lift equals weight, which fixes the lift coefficient at the chosen cruise
speed; drag then follows from the polar, and the lift-to-drag ratio is the ratio of the
two at that point:

    C_L = W / (q S),   q = ½ ρ V²

    C_D = C_D0 + C_L² / (π · AR · e)

    L/D = C_L / C_D

This is evaluated **at the cruise condition**, not at the aircraft's best point. The
familiar expression L/D_max = 0.5 √(π·AR·e/C_D0) gives the *maximum* lift-to-drag ratio,
which occurs at one particular lift coefficient and therefore at one particular speed —
25.3 m s⁻¹ for the light design, only 1.26 times its stall speed. Cruising there would
leave too little margin, so both reference designs cruise at 1.49 times stall instead
and accept the lift-to-drag ratio that this condition gives. Using the maximum value
while specifying a different cruise speed would overstate the range, and an earlier
version of this paper did exactly that; the figures below are computed at the cruise
point.

**Range.** The series-hybrid chain is stated explicitly rather than folded into a
single efficiency, because the result is sensitive to it and a reader should be able to
disagree with any single link:

| Link | Value |
|---|---:|
| Internal-combustion engine | 0.28 |
| Generator | 0.90 |
| Power electronics | 0.95 |
| Electric machine | 0.92 |
| Propeller | 0.80 |
| **Overall** | **0.176** |

Fuel energy is taken as 12.9 kWh kg⁻¹. The engine figure is the one that matters most:
0.28 is representative of a small four-stroke engine at its best operating point, and
it is the reason the range figures below are lower than an optimistic estimate would
give.

**Control.** Tip-pair thrust follows from the required angular acceleration,
M = 2 T L = I α, with the transition manoeuvre as the sizing case.

**Assumptions carried throughout:** sea-level density; no compressibility; span
efficiency e assumed at 0.85; C_D0 assumed at 0.0248 for the light design, which is
generous for a clean blended-wing body and is intended to absorb the tip-frame
contribution of Section 5.2 — that contribution is 0.0043, or seventeen percent of the
assumed C_D0, so the assumption is self-consistent rather than optimistic. Both
coefficients remain assumptions in what follows. Section 6.6 does not replace them; it
bounds them by independent calculation, which is a weaker but more honest claim.

## 6.2 Light reference design — 50 kg

| Quantity | Value |
|---|---:|
| Maximum take-off mass | 50 kg |
| Root chord | 0.97 m |
| Tip chord | 0.236 m |
| Span | 3.45 m |
| Wing area | 1.98 m² |
| Aspect ratio | 6.00 |
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

One qualification applies to everything in this section. The scaling described here is the
scaling of the analytical sizing model — of powers, loadings and mass *fractions*. The
component build-up of Section 6.7 does not reproduce it for the structure: whether the
heavy design's mass closes depends on how shell areal density grows with size, which was
not measured. The fractions below are preserved by the sizing rules; they have not been
shown to be realisable at 1000 kg.

Five properties of the scaling are worth separating, because three of them are
favourable and two are not. Figure 11 shows the two designs at a common scale, and it
shows the second of the unfavourable ones directly.

**Disc loading is held constant.** The two designs sit at 44.2 and 43.7 kg m⁻². This is
not a coincidence of sizing but the rule that governs it. Hover power per unit weight
is √(DL/2ρ), so holding disc loading constant holds the specific hover power constant,
and the aircraft can grow without the hover condition running away. The effect is direct:
hover power rises from 10.9 kW to 216.2 kW, a factor of 19.8 against a mass factor of 20.
Hover power grows *linearly* with mass rather than as the L^3.5 of the classical result,
and that is the whole benefit of fixing the disc loading.

Constant disc loading means disc area must grow in proportion to weight. For a
geometrically similar aircraft, whose mass grows as L³, that is a demand for disc area to
grow as L³ rather than as L² — which for a fixed number of propellers is impossible. This
architecture has two ways out of that, and it uses both. It may add coaxial pairs, and
adding a pair is architecturally free because every pair is already torque-balanced on
its own; and, as the next paragraph records, it does not hold geometric similarity.

**The propeller grows faster than the airframe.** This is the second exception, and it
is visible in Figure 11 rather than hidden in it. Wing loading is not held constant: it
rises from 25.3 to 45.0 kg m⁻², so wing area grows by a factor of 11.2 and span by 3.35
— more than the 2.71 that geometric similarity at constant density would give, but well
short of the 4.50 by which the main propeller must grow to hold the disc loading. The ratio of
propeller diameter to span therefore rises from 0.35 to 0.47. The heavy design is not the
light design photographed from further away; its propeller occupies almost half its span.

Nothing in the argument of this paper fails because of that, since the propeller is the
nose of the aircraft rather than an appendage on it, and disc loading — the quantity the
hover power depends on — is what is being held. But the claim that the configuration
keeps its proportions across the range should be read as applying to the four quantities
named here and not to every dimension, and a design much heavier than 1000 kg would reach
the point where a single nose pair can no longer hold the disc loading and a second pair
must be added.

**The buffer fraction is preserved.** 3.6 % of MTOW at 50 kg and 4.0 % at 1000 kg. The
mechanism by which Bill 3 is avoided therefore does not degrade with size.

**The frame drag fraction is preserved.** Frontal area and wing area both scale as L²,
so the twelve percent of Section 5.2 holds at both ends.

**Transition time does not scale.** This is the exception, and it is stated plainly.
The control moment required to rotate the aircraft follows M = Iα with I ∝ mL², so the
moment needed to turn it in a fixed time grows much faster than the aircraft itself.
Scaling the light design's two-second rotation geometrically to 1000 kg would demand
221.5 kW from the tip propellers — 102 % of the hover power, which is to say it is not
available at all:

**Table 4.** Tip-propeller power required to rotate the heavy reference design.

| Rotation time | Tip-propeller power, 4 total | Fraction of hover power |
|---:|---:|---:|
| 2 s | 221.5 kW | 102 % |
| 3 s | 65.6 kW | 30 % |
| 4 s | 27.7 kW | 13 % |
| 5 s | 14.2 kW | 7 % |
| **5.1 s** | **13.4 kW** | **6 %** |

**The rule is that a larger aircraft turns more slowly.** The heavy design rotates in
5.1 seconds, at six percent of its hover power. That figure is not a round number chosen
for convenience: Section 7.6 shows it is the rotation time at which the heavy design holds
the same rotational control margin the light design holds at two seconds. An earlier
version of this study used four seconds, at which the tip propellers must supply thirteen
percent of hover power — nearly the whole of their allocation — and at which a smoothly
commanded rotation does not close at all.

This constraint is less costly than it first appears, and Section 7 explains why: a
slower rotation does not lose more altitude but less, so the scaling penalty on
transition time works in the same direction as the scaling penalty on control power
rather than against it. The larger aircraft is obliged to turn slowly, and turning
slowly is what it should do anyway.

The classical objection to scaling a VTOL aircraft up is that hover power required grows
as L^3.5 while power available grows as L³. Fixing the disc loading is what removes that
objection on the hover side, as the first item above shows. It does not remove it on the
transition side, and Table 4 is where it reappears: the rotation is the one place in this
aircraft where the square–cube relation is still paid in full.

## 6.5 Context

The following aircraft occupy the same mass range. They are listed to locate the
reference designs in a real field, not to rank them.

| Aircraft | MTOW | Payload | Payload fraction |
|---|---:|---:|---:|
| HAVELSAN BAHA [8] | 28 kg | 2 kg | 7.1 % |
| Textron Aerosonde Mk 4.7 VTOL [9] | 45.4 kg | 9.1 kg | 20.0 % |
| Baykar KALKAN [10] | 75 kg | ~3 kg internal | 4.0 % |
| HAVELSAN BULUT [11] | not published | 5 kg | — |
| Elroy Air Chaparral [12] | 865 kg | 136 / 227 kg | 15.7 / 26.2 % |
| Sabrewing Rhaegal-A [13] | 1400 kg | 360–450 kg | 25.7–32.1 % |
| Pipistrel Nuuva V300 [14] | 1700 kg | 408 kg | 24.0 % |

All entries are taken from manufacturers' published material. Payload definitions are not consistent between them — some quote internal payload, some external, some both — and empty weights are generally not published. The lightest entry has been confirmed from its manufacturer's data sheet as a vertical take-off aircraft [8].

Three statements can be made about this table and a fourth cannot.

First, the field is real and populated, at both ends of the mass range considered here.
Second, payload fraction rises with size across the field, from a few percent at the
light end to roughly a quarter at the heavy end, which is the ordinary consequence of
fixed costs not scaling down. Third, none of these aircraft connects an
internal-combustion engine directly to a lifting rotor; every one of them uses either a
generator or separate electric lift, which is independent confirmation that the series
arrangement of Section 4.3 is the practical choice at this scale rather than an
unusual one.

The fourth statement — that the reference designs outperform these aircraft — is not
made, and the numbers in Sections 6.2 and 6.3 should not be read as making it. Those
numbers are calculated from a mass budget with an unpaid structural margin; the numbers
in this table describe aircraft that exist and fly. Placing a calculation beside a
measurement and declaring a winner would be a category error, and the comparison is
offered only to show that the reference designs fall inside the field rather than
outside it.

A further caution applies to any comparison of endurance or range across this table.
Several of these aircraft are fully electric, and for those the endurance figure is set
by battery specific energy rather than by configuration. The lightest entry, for
instance, is an all-electric fixed-wing VTOL quoting up to two hours of endurance;
setting the fuel-burning reference design of Section 6.2 against that number would
compare energy sources, not architectures, and would say nothing about the argument of
this paper.

What can properly be compared, once these aircraft have been built and flown, is range
at similar payload — not payload at similar range. A configuration that carries a
comparable load further is making an architectural claim; a configuration that carries
a heavier load is making a claim about mass budgeting, which is exactly the part of
this study that is least validated.

## 6.6 Independent checks on the two assumed coefficients

The two coefficients that carry the most weight in Section 6 — span efficiency and
zero-lift drag — were assumed rather than derived. They remain assumed. What follows
does not replace them with computed values; it asks a narrower question that can be
answered honestly: **are the assumed values inside the range that a calculation gives,
and on which side?**

**What the vortex-lattice method is being asked for, and what it is not.** Four results in
this paper come from a vortex-lattice solution: the span efficiency below, the neutral point
of Section 7.6, the twist required to trim, and the roll damping of Section 4.4. Falkner's
account of the method's accuracy [24] separates the quantities it settles quickly from those
it does not, and the separation is favourable here. He reports that "the grading of spanwise
circulation converges quickly" and that "the local aerodynamic centre can be adequately defined
by the use of two chordwise terms only", while "a reasonably accurate calculation of pressure
distribution in the neighbourhood of a discontinuity in plan would require at least three or
four terms". Every quantity taken from the method here is of the first kind — circulation and
aerodynamic centre — and none is of the second. That is consistent with what the convergence
study found: the neutral point moved 0.26 percent over a threefold refinement, while the span
efficiency needed four times the default resolution before it stopped returning values above
unity, which is physically impossible for a planar wing and is the signature of an
under-resolved plan discontinuity — this planform is cropped, and therefore has one.

**A second boundary is worth stating because it marks where the method is not used.** For
wings of low aspect ratio and high sweep, leading-edge vortex separation dominates and the
linear method must be extended by a suction analogy to follow it [25]. That regime is not this
wing's cruise condition — aspect ratio 6.03 at 45° root sweep, at incidences under eleven
degrees — but it *is* the regime of the transition incidences in Section 7. No vortex-lattice
result is quoted there, and this is why.

**A third boundary was found by reading, and it is the sharpest of the three because it is a
measured number rather than a statement of scope.** A study of a tactical blended-wing-body UAV
compared a vortex-lattice solution against RANS at the same condition and found the
vortex-lattice lift coefficient low by **thirty to thirty-eight percent** across incidences
from −4° to 12°, and excluded the method from its trim analysis on that basis [39]. That is a
configuration of the same class as this one, and the four results above rest on the same kind
of solution.

Two things keep the argument of the previous paragraphs standing, and one of them cannot be
checked. The deviation is nearly constant with incidence — 37.8, 37.7, 38.2, 37.2 and 30.7
percent — which is the signature of a multiplicative error in the magnitude of the loading
rather than an error in its distribution. A neutral point is a ratio of derivatives and a
static margin is a ratio of lengths; a factor common to lift and moment cancels in both, and
the twist effectiveness would be *under*-stated, meaning the twist actually required to trim
would be smaller than Section 7.6 reports rather than larger. That argument depends entirely on
the moment scaling with the lift, and the pitching-moment comparison in that paper is published
with its values withheld. **The check that would settle it is precisely the one the source does
not permit.**

What can be said without it is narrower. The likeliest origin of a deficit that large is the
volume of the centre body, which a vortex-lattice method represents as a camber surface of zero
thickness and which on a blended wing carries a real share of the lift; the cited study does not
say whether its model included the body at all. The planform solved here carries its centre
section as part of the lifting surface, so the same deficit should not transfer at full size.
But it does not transfer to zero either, and **the honest statement is that the vortex-lattice
results in this paper carry an untested magnitude error of unknown size, bounded above by a
published comparison on a similar configuration, and that every use made of them here is of a
kind that a magnitude error does not disturb.** Confirming that would take a viscous or
Reynolds-averaged solution of this planform, which is named in Section 8 as the first thing
worth computing next.

**Span efficiency.** A vortex-lattice solution of the planform of Section 4.2 [15] gives
an inviscid span efficiency of 0.99. That is not the same quantity as the 0.85 used here.
The vortex-lattice figure counts only the departure of the induced drag from the
elliptic ideal; the 0.85 is an Oswald-type efficiency that also carries the viscous
drag due to lift, which for a clean wing runs at roughly 85 to 90 percent of the
inviscid value. The two are consistent. Reporting the calculation as an improvement on
the assumption would be a category error, and it is not claimed.

**Section 7.6 unsettles this, and the unsettling is not resolved here.** The 0.99 belongs to
the untwisted planform, and the untwisted planform cannot be trimmed; the trimmed wing computes
to 0.865, which under the same reasoning implies an Oswald value of 0.735 to 0.78 — below the
assumed 0.85 rather than above it. The ratio between the two efficiencies is itself a range
this study has not sourced, so the assumption is not revised on the strength of it. What has
changed is that it is no longer bounded from above by a calculation, and Section 8 says so.

The same solution gives a lift-curve slope of 3.87 rad⁻¹ against the 4.72 rad⁻¹ that
the transition simulation of Section 7.4 assumes — eighteen percent lower, and in the
unfavourable direction. Section 8.6 reports what that does to the transition results.

**Zero-lift drag.** A strip calculation over the span, taking section drag coefficients
at zero lift from a physics-informed aerofoil model [16] and adding the tip frames and the propeller hubs, gives:

| Contribution | Light design |
|---|---:|
| Wing and body, clean surface | 0.0073 |
| Wing and body, transition tripped near the leading edge | 0.0129 |
| Tip frames, faired | 0.0043 |
| Tip-propeller hubs | 0.0015 – 0.0020 |
| **Total** | **0.0131 – 0.0210** |

The frame term reproduces the 0.0043 of Section 5.2, which was reached by a different
route, and it comes out the same for the heavy design — an independent confirmation of
the scale invariance claimed in Section 6.4. The hub term is bounded by hardware rather
than guessed: each tip rotor must deliver about 0.83 kgf on a 0.20 m propeller, which
places it in the standard 22 mm stator class whose outer cans measure roughly 28 mm.

**The assumed 0.0248 lies above the whole of that range.** The assumption is therefore
conservative in every scenario considered, not merely in the pessimistic one. Because
range is linear in lift-to-drag ratio, the reference designs of Sections 6.2 and 6.3
would gain rather than lose if the calculation were adopted — which is the reason it is
not adopted. An assumption that is declared and shown to be conservative is a smaller
target than a calculation whose weakest link, discussed in Section 8.4, is the
treatment of a twenty-five percent thick centre body as a two-dimensional section.

**A three-dimensional solution for the centre body.** The weakness just named has since
been removed. Section 8.17 lists it first among the places these results should be
attacked, and the calculation it asks for has now been carried out: a structured
Reynolds-averaged solution over the planform of Section 4.2, at the cruise Reynolds
number and at zero lift, resolving the wing and blended body as a three-dimensional
surface rather than as stacked sections. It gives a wing-and-body zero-lift drag of

**0.01475 with the Spalart–Allmaras closure and 0.01201 – 0.01253 with k-ω SST** — a
range rather than a single figure, and not for one reason but for two. Nothing in these
solutions selects between the two closures, so the eighteen percent between them is
carried openly; and the SST value itself is not unique, because two well-converged
solutions of the same case from two materially different starting fields settle four
percent apart. That second finding is set out below, since it bears on how much weight
any of these numbers will hold.

Against the 0.0129 of the tripped strip estimate, the Spalart–Allmaras value is fifteen
percent higher and the SST values between two and seven percent lower; the strip method
is therefore bracketed rather than simply beaten. Substituting each in turn raises the
total to between 0.0203 and 0.0230. **The assumed 0.0248 lies above all of them**, so the
conclusion of the previous paragraph survives the more expensive calculation under either
closure and under either initialisation; the margin is twenty-two percent on the most
optimistic value and eight percent on the conservative one. The assumption is not
replaced here either, for the same reason as before. Where a single number is needed
downstream, the conservative value is carried.

Neither range is a probabilistic uncertainty band, and neither is reported as one. The
remaining terms are measured rather than asserted:

| Source of uncertainty | Magnitude |
|---|---:|
| Iterative convergence | 0.1 % |
| Spatial discretisation, three grids of 0.27 – 2.66 M cells | < 0.1 % |
| Wall resolution, y⁺ 43 → 20 | 10 % |
| Wall resolution, y⁺ 20 → 1, Spalart–Allmaras | + 1.6 % |
| Wall resolution, y⁺ 20 → 1, k-ω SST | − 6.7 % |
| Turbulence-model spread, k-ω SST against Spalart–Allmaras, at y⁺ ≈ 20 | 8 % |
| **Turbulence-model spread, the same pair at y⁺ ≈ 1** | **18 %** |
| **Initialisation spread, k-ω SST at y⁺ ≈ 1, two starting fields** | **4.3 %** |

The dominant term is the turbulence model, not the grid — which is worth stating plainly,
because grid convergence is the check a reader expects and it turns out to bound the
smallest of the terms. The last two rows are labelled *spread* rather than *uncertainty*
deliberately: two closures do not sample a distribution, and the interval between them
carries no claim that the true value lies inside it. The same caution applies to the last
row, which reports two starting fields and not a population of them. Three further results
are recorded because they are easy to get wrong in either direction.

The forces converge far more slowly than the residuals: at a velocity residual of
1.6 × 10⁻⁵ the computed drag was still fifty-five percent above its converged value, so a
solution stopped on residuals alone would have been badly wrong.

The wall-resolution sensitivity does not saturate, and it does not even share a sign
between the two models. Resolving the wall raises the Spalart–Allmaras drag by 1.6
percent and lowers the k-ω SST drag by 6.7 percent, so the spread between the models
doubles — from 8 percent at y⁺ ≈ 20 to 18 percent at y⁺ ≈ 1. No single wall-resolution
correction is therefore assumed. An earlier version of this section quoted a single value
with a five percent band, obtained by averaging one model at y⁺ ≈ 1 against the other at
y⁺ ≈ 20; that mixes two wall resolutions and understates the model-form term.

**The wall-resolved SST solution is not independent of its starting field.** It cannot be
started from a uniform field at all: from uniform initial conditions the run develops a
localised region of non-physical turbulent kinetic energy near the leading edge at
mid-span, which decays over some two thousand iterations without reaching a physical
level and then diverges. Two starts that do converge were therefore compared — one warmed
from the converged Spalart–Allmaras field, one mapped from the converged SST solution at
y⁺ ≈ 20 on the coarser grid. The two initial fields differ by an order of magnitude in
peak eddy viscosity and by a factor of six in peak turbulent kinetic energy; the cases
are otherwise identical, sharing the same grid file, the same transport and turbulence
properties, and the same boundary conditions. Both ran five thousand iterations without
bounding, the mapped start reaching the lower velocity residual of the two, 1.0 × 10⁻⁷.

They do not agree. The drag coefficients are 0.01253 and 0.01201, four and three tenths of
a percent apart, and the difference lies almost entirely in the pressure component:
0.00386 against 0.00336, thirteen percent, while the viscous components agree to three
parts in a thousand. A converged steady solution should not depend on its starting point;
here it demonstrably does.

The two solutions are not, however, of equal standing, and the criterion that separates
them is geometric rather than numerical. The sections are symmetric and untwisted and the
incidence is zero, so the lift coefficient must vanish. The mapped solution returns
1.3 × 10⁻⁴ and the warm-started one 1.5 × 10⁻³ — an order of magnitude further from the
value the geometry requires. The same asymmetry appears locally: at mid-span and
three-quarter chord the upper and lower surface pressure coefficients differ by 0.0011 in
the mapped solution and by 0.0249 in the warm-started one, where symmetry requires zero,
and the ratio holds at every station examined. The induced drag of that residual lift is
negligible — of order 10⁻⁷, nine parts per million of the total — so the asymmetry is a
symptom and not the cause of the drag difference; but it is a physical test that one
solution passes and the other does not.

Two further diagnostics bear on where the difference lives. The reverse-flow area on the
wall is 0.02 percent in both solutions and occupies the same streamwise interval in both,
so the two are not settling into visibly different separation topologies. And the
pressure-drag difference is distributed almost evenly across the inner span — each of
eight bands carries roughly an eighth of it — and concentrated in the rear quarter of the
chord, where the mapped solution recovers more pressure. An earlier version of this section
read the even spanwise distribution as evidence against a second solution branch; that
inference is withdrawn, since a second stationary state need not be spatially localised.
What can be said is narrower: the two solutions share a separation topology, and the one
that better satisfies the symmetry the geometry imposes also recovers more trailing-edge
pressure.

Both values are reported, because a third starting field has not been tried and nothing
shows one would fall inside the interval; 0.01201 – 0.01253 is a measured spread and not
a bound. Where a single value from this pair is wanted, the mapped solution is taken as
the reference state, on the grounds that it carries the smaller residual lift and surface
asymmetry. That is a selection criterion and not a proof: it does not establish that the
warm-started solution is unphysical, only that it is further from a symmetry the geometry
requires. The defence that a non-symmetric mesh would bias both cases equally is a
supporting argument rather than a demonstration, since the equations are non-linear and a
fixed mesh bias can couple differently to two different starting fields.

**What this does not settle.** The solution is fully turbulent throughout. It therefore
speaks to the tripped row of the table above and not to the clean-surface row, and the
gap between those two rows — 0.0073 against 0.0120–0.0148 — is now the largest single
uncertainty in the zero-lift drag, larger than the spread between the two closures. Closing it requires a transition-sensitive model,
which needs a wall-resolved grid and a two-equation formulation at the same time. That
combination now converges, and the Langtry–Menter γ–Reθ model reproduces the ERCOFTAC
T3A flat plate to within a few percent in the turbulent region while predicting transition
about twenty-five percent early in Reynolds number. But T3A is a bypass case at three
percent freestream turbulence, and the present cruise condition is an order of magnitude
quieter; attempts to validate the model in that regime were not successful, for reasons
traced to leading-edge turbulence production and freestream decay rather than to the
model itself. The clean-surface bound therefore remains where the strip calculation left
it, and no transition-model drag figure is claimed.

**Internal volume.** One closure that the mass budget does not address is whether the
payload fits. The body's gross internal volume follows from the thickness distribution:
185 litres for the light design. Taking rather more than half of that as usable and
subtracting fuel, buffer, powerplant and avionics leaves about 80 litres for 13 kg of
payload, which requires a mean density of only 0.16 kg per litre. The configuration is
mass-limited rather than volume-limited, and the choice of mission therefore constrains
the structure and the load paths rather than the internal arrangement.

## 6.7 A component build-up of the mass budget

The fractions used in Sections 6.2 and 6.3 are asserted, and Section 8.2 says so. This
section replaces the assertion for the light design with a build-up from components. The
rule followed throughout is that no item may be derived from the fraction it is meant to
test: every line comes either from the geometry and a stress calculation, or from a
specific quantity — an areal density, a specific power — stated openly and then varied.

**Structure.** The wetted area follows from the planform of Section 4.2 and the NACA 00xx
thickness distribution: 4.14 m² against 1.98 m² of planform. A carbon–epoxy sandwich shell
at 1.5 kg m⁻² gives 6.20 kg, with ribs, bulkheads and bonded joints taken at 45 percent of
the shell. The tip frames are sized by a vertical landing case, since this aircraft lands on them: a
3 g arrival, half the weight through one frame, the post treated as a cantilever of the
stated length, giving 0.95 kg for both frames including fittings. That case is not shown to
be the worst one — an off-axis touchdown, a ground gust against the planform standing on
its tail, or the thrust moment of the nose pair may govern the frame root or the joint into
the wing instead — and no combined case was run.
Fasteners, adhesive, filler and paint are charged at 10 percent of primary structure and
access panels at 6 percent. The total is 11.88 kg, 23.8 percent of take-off mass.

Span bending is not what sizes the spar, and this is worth recording, because a thick
blended centre body invites the assumption that it must be. At an ultimate load factor of
5.25 the root bending moment is 934 N m; carried at 400 MPa over a structural depth of 0.9
times the root thickness, the caps require 10.7 mm² of carbon and weigh 41 grams. The claim
that figure supports is narrow and is stated narrowly: **global span bending is not the
sizing driver in this static model.** It says nothing about the failure modes the model
does not contain — sandwich and face-sheet buckling, core shear, torsion, load introduction
at the frame roots and the nose mount, minimum manufacturing gauge, damage tolerance,
aeroelastic margin — and none of those is a reason to reduce the shell and internal-structure
allowances above. Those allowances are where such mass would have to live, and the 41 grams
does not license trimming them.

**Propulsion.** The nose motor is sized by hover peak power and the engine by cruise,
which is the configuration's central claim and is visible in the budget as such: 2.73 kg
of electric machine against 2.60 kg of engine and generator, at 4 kW kg⁻¹ and 1 kW kg⁻¹
respectively. Adding the tip motors at twelve percent of nose power, the propellers, the
coaxial hubs, the power electronics at 20 kW kg⁻¹, the engine mounting with its cooling
and exhaust, and the power cabling gives 7.60 kg, 15.2 percent.

**Systems, energy and contingency.** Avionics, fuel system, strip actuation, signal harness
and payload interface total 2.84 kg. There are no elevon or rudder actuators to add, since
the aircraft has neither; the strip is its only moving aerodynamic device and its actuation
is carried here. Fuel and battery are as sized, 9.80 kg. A contingency of 12 percent of dry
mass — ordinary preliminary-design practice — adds 2.68 kg.

**The battery buffer is specified by power, not by energy, and this has not been stated
before.** It must supply the difference between hover power and engine rating, 8.3 kW at
the light design point, from 1.8 kg — a specific power of 4.6 kW kg⁻¹, or about 26 C at
180 Wh kg⁻¹. Energy is not the binding constraint until roughly 140 seconds of hover, well
beyond the profile of Section 7; below that the buffer is power-limited. The heavy design
is in the same regime, 4.1 kW kg⁻¹ at 22 C. That places the buffer in the high-power
lithium-ion or lithium-polymer class — cells rated for twenty to thirty times their
capacity in continuous discharge — rather than in the high-energy class a range-driven
selection would reach for.

**How demanding, measured against the only figures this study has read, is the most exposed
number in the whole mass budget.** Bacchini and Cestino, sizing electric VTOL aircraft, take
735 W kg⁻¹ at pack level from an automotive traction pack and report that "Li-ion batteries for
power applications have… specific power from 700 to 1300 W kg⁻¹" [21]. The buffer here asks for
**4.6 kW kg⁻¹**, three and a half to six and a half times the top of that range. Sized at
figures from that range instead:

| Buffer specific power | Buffer mass | Fraction of MTOW |
|---|---:|---:|
| 0.735 kW kg⁻¹ (the pack they assume) | 11.3 kg | 22.6 % |
| 1.30 kW kg⁻¹ (top of their quoted range) | 6.4 kg | 12.8 % |
| **4.61 kW kg⁻¹ (this study, implicitly)** | **1.8 kg** | **3.6 %** |

At the top of their range the buffer would be 4.6 kg heavier than budgeted, against the 2.2 kg
of unallocated mass this section leaves. **The light design's mass budget would not close.**

The defence is real but it is a defence, not a measurement: their figures are for an
energy-optimised automotive pack, and a buffer discharged for a minute at a time is a different
product optimised for the opposite thing. Nothing this study has read gives a specific power for
that product. **The assumption is therefore that a short-duration buffer beats an automotive
traction pack by a factor of three and a half to six — plausible in kind, unverified in
magnitude, and load-bearing for Bill 3.**

**The energy side is a different matter, and it is far more comfortable than the power side.**
The buffer does not discharge continuously for the whole vertical phase. It discharges through
the take-off, which ends when the rotation begins and the wing starts carrying the aircraft;
it then recharges from the engine over hours of cruise, and discharges again for the landing.
At a thrust-to-weight ratio of 1.2 the vertical acceleration is 0.2 g, so the 5 m s⁻¹ climb
from which Section 7.4 enters the rotation is reached in 2.6 s and 6.4 m. A take-off segment of
ten to twenty seconds at full draw is generous. Against that:

| Take-off segment at full draw | Energy used | of a 180 Wh kg⁻¹ buffer | of an 80 Wh kg⁻¹ buffer |
|---:|---:|---:|---:|
| 10 s | 23 Wh | 7 % | 16 % |
| 20 s | 46 Wh | 14 % | 32 % |
| 30 s | 69 Wh | 21 % | 48 % |

Even at the low energy density that a high-power chemistry would carry, a twenty-second take-off
uses a third of the buffer. **The binding constraint is power, not energy, and it stays that way
under any plausible take-off duration.**

That distinction matters, because it says what would *not* rescue the specific-power figure.
A shortfall in power is not a transient to be ridden out. Hover power goes as thrust to the
three-halves, so thrust goes as power to the two-thirds, and a buffer delivering less simply
buys less thrust:

| Buffer specific power | Total power available | Resulting T/W | Leaves the ground |
|---|---:|---:|---|
| 0.735 kW kg⁻¹ | 3.9 kW | 0.61 | no |
| 1.30 kW kg⁻¹ | 4.9 kW | 0.71 | no |
| 2.50 kW kg⁻¹ | 7.1 kW | 0.90 | no |
| 4.61 kW kg⁻¹ | 10.9 kW | 1.20 | yes |

**At the specific powers this study has a citation for, the aircraft does not lift off**, so
there is no brief overshoot to tolerate and no manoeuvre that shortens the exposure. The only
remedy is a heavier buffer, which is why this appears as a mass-budget exposure rather than a
flight-dynamics one. The buffer masses used here are a cell-selection requirement rather than a
free parameter, and it is the specific power, not the energy, that has to be found.

| Group | Build-up | Assumed in 6.2 |
|---|---:|---:|
| Structure | 23.8 % | 30 % |
| Propulsion chain | 15.2 % | 16 % |
| Battery buffer | 3.6 % | 4 % |
| Systems and contingency | 11.0 % | 8 % |
| Fuel | 16.0 % | 16 % |
| **Payload, as residual** | **30.4 %** | **26 %** |

**Where the mass may sit is also constrained, and the constraint was not previously
stated.** The budget above says how much each item weighs and not where it sits. Section 7.6
adopts a first-order packaging rule in the absence of an internal layout — masses distributed
in proportion to internal volume — and shows that the resulting centre of gravity has to lie
in a band whose aft limit is firm and whose forward limit is not: aft of roughly 85 percent of
root chord the static margin falls below the usual tailless band, while the forward limit
depends on how much camber moment the sections can supply, which this paper does not fix. The sweep carries the neutral point to 0.859 m
from the root leading edge, well aft of the root chord's midpoint, which is what makes such
an aft centre of gravity admissible at all. The internal volume's own centroid is at 78.3
percent, so an arrangement that simply follows the available volume lands just forward of the
window; fuel, payload and engine therefore cannot be placed for convenience, and the budget
above should be read as constrained in position as well as in magnitude.

The build-up closes with 2.2 kg in hand — **conditionally, and the conditions are the
result.** It closes if the average structural areal density is no more than 1.78 kg m⁻²,
and if everything still outside the model together stays under that same 2.2 kg. Neither is
demonstrated here; the 1.5 kg m⁻² used is an aggressive target for a composite airframe of
this class rather than a measured property of one that has flown. Why a build-up coming in
lighter than its own target should be read as a warning rather than a confirmation is set
out in Section 8.2.

**The heavy design is not closed by this exercise, and no claim is made that it closes.**
Shell mass scales as areal density times wetted area, so as the square of linear scale,
while take-off mass scales as the cube; holding areal density constant would make the shell
fraction fall as the inverse of scale, which is plainly wrong, since skins on larger
aircraft are not thinner. Holding the fraction constant instead requires areal density to
grow linearly with scale. The truth lies between, and the exponent has not been measured.
Sweeping it puts the 1000 kg design's 260 kg payload at break-even at an exponent of 0.467,
an areal density of 2.64 kg m⁻², closing below and failing above. No attempt is made here
to argue for a value on either side of that threshold, because any such argument would be a
structural model standing in for a measurement. What the sweep establishes is the
statement itself: **the component build-up does not demonstrate closure of the heavy
design.** That, and not any of the light-design assumptions, is the largest open question
in the mass budget of this study, and it qualifies the scale-invariance of Section 6.4 —
which holds for the analytical sizing fractions and has not been shown to hold for the
structure that must realise them.
