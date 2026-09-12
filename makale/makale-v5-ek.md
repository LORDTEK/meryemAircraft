# Supplementary Material — meryemAircraft

*Supplementary material to "The Architectural Cost of Hybrid VTOL: meryemAircraft, a Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System".*

These six files carry the derivations behind the results stated in the paper. Each was a
section of an earlier, longer version and is reproduced without abridgement, so that every
number quoted in the main text can be traced to the calculation that produced it. The
computational setup, the scripts, and a running record of the corrections made during the
study are in the repository the paper cites.

**Contents**

- **Supplementary S1** — Independent checks on the two assumed aerodynamic coefficients (3441 words)
- **Supplementary S2** — A component build-up of the mass budget (2730 words)
- **Supplementary S3** — Control axes in full (6560 words)
- **Supplementary S4** — Rotational authority, trim, and the transition envelope (7510 words)
- **Supplementary S5** — The limitations in full (6505 words)
- **Supplementary S6** — The three bills stated formally, and a comparative sizing (3001 words)

---

# Supplementary S1 — Independent checks on the two assumed aerodynamic coefficients

*Supplementary material to "The Architectural Cost of Hybrid VTOL:
meryemAircraft, a Propeller-Driven Tail-Sitting Blended-Wing-Body Without a
Dedicated Lift System".*

This material was Section 6.6 of an earlier, longer version of the paper.
It is reproduced here in full so that every number quoted in the main text can
be traced to the calculation that produced it. The computational setup, the
scripts, and the record of what failed along the way are in the repository the
paper cites.

---

## S1.1 Independent checks on the two assumed coefficients

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
kind that a magnitude error *would not* disturb if the moment scales with the lift by the same
factor.** That conditional cannot be discharged from the source, and nothing else in the
literature read here discharges it either. It is stated as a conditional and carried as one. Confirming that would take a viscous or
Reynolds-averaged solution of this planform, which is named in Section 8 as the first thing
worth computing next.

**Span efficiency.** A vortex-lattice solution of the planform of Section 4.2 [15] gives
an inviscid span efficiency of 0.99. That is not the same quantity as the 0.85 used here.
The vortex-lattice figure counts only the departure of the induced drag from the
elliptic ideal; the 0.85 is an Oswald-type efficiency that also carries the viscous
drag due to lift, which for a clean wing runs at roughly 85 to 90 percent of the
inviscid value. The two are consistent. Reporting the calculation as an improvement on
the assumption would be a category error, and it is not claimed.

**Section 7.6 unsettles this, and the ratio has since been computed rather than assumed.** The
0.99 belongs to the untwisted planform, and the untwisted planform cannot be trimmed. An earlier
version of this paper carried the trimmed case forward with the same 85-to-90-percent rule and
reported an implied Oswald value of 0.735 to 0.78. That rule was borrowed, and it turns out to
be too pessimistic.

The calculation replacing it is the one the method of Section 6.6 was already equipped to make.
The vortex-lattice solution gives the loading of the twisted wing station by station; the
section solver used for the zero-lift drag build-up is then called at **each station's own local
lift coefficient** rather than at zero lift, and the profile drag integrated across the span.
This is the two-dimensional-viscous-coupled-to-three-dimensional-circulation construction used
in the non-linear vortex-lattice literature [40], carried out on this planform. Before any
result is taken from it, the strip decomposition is checked against the solver it comes from:
summing the strip loads reproduces the solver's own lift coefficient to six decimal places, and
the strip widths sum to the span.

Taking the lift-dependent drag to be the induced drag plus the rise in profile drag above its
zero-lift value — the quantity an Oswald efficiency has to carry, since the zero-lift part is
already inside C_D0:

| | Inviscid e | **Oswald e** | Ratio |
|---|---:|---:|---:|
| Untwisted planform | 0.990 | 0.931 | 0.940 |
| **Trimmed, −9° washout** | **0.859** | **0.817** | **0.951** |

**The borrowed ratio was wrong in the favourable direction and the conclusion is unchanged in
the unfavourable one.** The viscous penalty is 5 to 6 percent rather than 10 to 15, but the
trimmed wing starts from 0.859, so the Oswald efficiency lands at **0.817 — below the assumed
0.85 by 3.9 percent**, not at the 0.735 to 0.78 previously feared. At that value the cruise
lift-to-drag ratio is **11.87 against the 12.04 the assumption gives**, a shortfall of 1.4
percent rather than the 3 to 5 percent Section 7.6 had allowed for.

Two limits belong with the number. The vortex-lattice sections are symmetric, so the profile
drag is that of a wing reaching each local lift coefficient without camber; a cambered section
reaches the same lift at lower incidence and usually at lower drag, which makes this a
**lower bound on the efficiency** rather than an estimate of it. And the strip method ignores
sweep. Evaluating the same integral under simple-sweep theory instead — normal-component
velocity and chord throughout — halves the profile drag, which is not a measure of uncertainty
but a sign that the transformation does not apply to friction: the pressure field is set by the
component normal to the sweep line, but the boundary layer runs over the surface at the full
freestream speed. The flow-aligned convention is used here, and it is also the convention the
zero-lift build-up uses, so the two numbers compose.

The same solution gives a lift-curve slope of 3.87 rad⁻¹ against the 4.72 rad⁻¹ that
the transition simulation of Section 7.4 assumes — eighteen percent lower, and in the
unfavourable direction. Section 8.6 reports what that does to the transition results.

**Zero-lift drag.** A strip calculation over the span, taking section drag coefficients
at zero lift from a physics-informed aerofoil model [16] and adding the tip frames and the propeller hubs, gives:

| Contribution | Lower bound | Upper bound |
|---|---:|---:|
| Wing and body | 0.0073 (clean surface) | 0.0129 (transition tripped) |
| Tip frames, faired | 0.0043 | 0.0043 |
| Tip-propeller hubs | 0.0015 (30 mm can) | 0.0020 (50 mm can) |
| Subtotal | 0.0131 | 0.0191 |
| Excrescence allowance | none | +10 % |
| **Total** | **0.0131** | **0.0210** |

The two columns are deliberately not the same calculation. The lower bound takes the clean
surface, the smaller hub and no allowance for excrescences; the upper bound takes the tripped
surface, the larger hub and ten percent for fasteners, joints, antennas and surface
imperfection. The interval is a bracket rather than an error bar, and the allowance row was
omitted from an earlier version of this table, which therefore did not sum to its own total.

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
is therefore bracketed rather than simply beaten. Substituting each in turn for the wing-and-body
row, and carrying the larger hub and the ten percent allowance in every case so that the three
are compared on one convention, gives **0.0201 with the low SST value, 0.0207 with the high one
and 0.0231 with Spalart–Allmaras**. **The assumed 0.0248 lies above all of them**, so the
conclusion of the previous paragraph survives the more expensive calculation under either
closure and under either initialisation; the margin is twenty-three percent on the most
optimistic value and seven percent on the conservative one. The assumption is not
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
shows one would fall inside the interval; 0.01201 – 0.01253 is a computed spread and not
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

---

# Supplementary S2 — A component build-up of the mass budget

*Supplementary material to "The Architectural Cost of Hybrid VTOL:
meryemAircraft, a Propeller-Driven Tail-Sitting Blended-Wing-Body Without a
Dedicated Lift System".*

This material was Section 6.7 of an earlier, longer version of the paper.
It is reproduced here in full so that every number quoted in the main text can
be traced to the calculation that produced it. The computational setup, the
scripts, and the record of what failed along the way are in the repository the
paper cites.

---

## S2.1 A component build-up of the mass budget

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
5.25 the root bending moment is 934 N·m; carried at 400 MPa over a structural depth of 0.9
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
before.** It must supply the difference between what the propellers demand and what the engine
delivers — but that difference has to be taken at one station, and an earlier version of this
section did not take it at one. It subtracted the engine's 2.6 kW of *shaft* power from the
rotor's 10.9 kW of *shaft* power and divided the remainder by the buffer mass, giving
4.61 kW kg⁻¹. The buffer sits on the electrical bus, which is neither of those stations. Running
the chain of Section 6.1 link by link instead:

| Station | Light design, hover |
|---|---:|
| Nose propeller shaft | 10.90 kW |
| ÷ electric machine, 0.92 | 11.85 kW |
| ÷ power electronics, 0.95 | **12.47 kW demanded at the bus** |
| Engine shaft 2.60 kW × generator 0.90 | **2.34 kW supplied at the bus** |
| **Buffer** | **10.13 kW** |

which is **5.63 kW kg⁻¹** from 1.8 kg, or about 31 C at 180 Wh kg⁻¹ — twenty-two percent above
the figure previously carried, and in the unfavourable direction. Taking the tip pairs as well,
which Section 7.4 shows the aircraft needs in order to leave the ground at all, the bus demand
rises to 14.00 kW and the buffer to 11.66 kW, or **6.48 kW kg⁻¹** at 36 C. The heavy design sits
on the same line: 198.5 kW of buffer on 40 kg, **4.96 kW kg⁻¹**, rising to 5.54 kW kg⁻¹ if the
tip pairs are counted. Energy is not the binding constraint until roughly 140 seconds of hover,
well beyond the profile of Section 7; below that the buffer is power-limited. That places the
buffer well past the high-power lithium-ion or lithium-polymer class — cells rated for twenty to
thirty times their capacity in continuous discharge — and the paragraphs below measure how far
past.

**How demanding, measured against the only figures this study has read, is the most exposed
number in the whole mass budget.** Bacchini and Cestino, sizing electric VTOL aircraft, take
735 W kg⁻¹ at pack level from an automotive traction pack and report that "Li-ion batteries for
power applications have… specific power from 700 to 1300 W kg⁻¹" [21]. The buffer here asks for
**5.63 kW kg⁻¹** to hover and 6.48 to take off, four and a third to nearly nine times the top of
that range. Sized at figures from that range instead, on the hover requirement alone:

| Buffer specific power | Buffer mass | Fraction of MTOW |
|---|---:|---:|
| 0.735 kW kg⁻¹ (the pack they assume) | 13.8 kg | 27.6 % |
| 1.30 kW kg⁻¹ (top of their quoted range) | 7.8 kg | 15.6 % |
| **5.63 kW kg⁻¹ (this study, implicitly)** | **1.8 kg** | **3.6 %** |

At the top of their range the buffer would be 6.0 kg heavier than budgeted, against the 2.2 kg
of unallocated mass this section leaves. **The light design's mass budget would not close.**

The defence available at that point was that those figures are for an energy-optimised
automotive pack, while a buffer discharged for a fraction of a minute is a different product
optimised for the opposite thing. **That defence has since been tested against a measurement of
the right product, and it does not survive.** A 24S nickel–cobalt–manganese pack was designed,
built, bench-tested across discharge rates from 0.2 C to 10.68 C and then flown in an electric
VTOL aircraft through six take-off, hover and landing cycles [47]. Its measured pack-level
specific power is **724 W kg⁻¹** continuous for the unit pack and **892 W kg⁻¹** for the
four-parallel flight system — inside the range quoted above, not above it. Its maximum tested
rate, 10.68 C, corresponds to roughly **1.5 kW kg⁻¹**, and at that rate the pack reached
55.1 °C against a 60 °C limit: a thermal margin of 4.9 °C. That is the ceiling of a pack built
for exactly this duty, instrumented, and flown.

A third source points the same way from the other direction. A NASA-funded design study of
electrically propelled aircraft adopts a battery specific power of 4 kW kg⁻¹ and states plainly
that this is "about **twice that of existing batteries**" [48] — that is, it treats a figure
below the one assumed here as a future technology level rather than a present one.

| Source | Specific power | Kind |
|---|---:|---|
| Measured eVTOL pack, continuous [47] | 0.72–0.89 kW kg⁻¹ | flight-tested measurement |
| Same pack at its maximum tested rate [47] | ≈ 1.5 kW kg⁻¹ | measurement, 4.9 °C thermal margin |
| Li-ion for power applications [21] | 0.7–1.3 kW kg⁻¹ | literature range |
| Assumed future level in a design study [48] | 4 kW kg⁻¹ | stated as ≈ 2× what exists |
| **This study, implicitly — hover** | **5.63 kW kg⁻¹** | **assumption** |
| **This study, implicitly — take-off** | **6.48 kW kg⁻¹** | **assumption** |

Sized at the measured thermal ceiling of 1.5 kW kg⁻¹ the buffer becomes **6.8 kg** rather than
1.8 kg — 5.0 kg heavier, against 2.2 kg of unallocated mass — and 7.8 kg if it must also lift
the aircraft off the ground. Sized at the measured continuous figure it becomes 11.4 kg, or
23 percent of take-off mass, which is most of the payload. **The light design's mass budget does
not close at any measured specific power, and this is the single most exposed number in the
paper.** It is not resolved by arguing that the buffer is a different product: the source above
*is* that product, built and flown. The gap to be closed is a factor of **3.8 on the measured
thermal ceiling and 6.3 on the measured continuous rate**. What would resolve it is a pack
demonstrating that, at acceptable temperature, or a heavier buffer carried at the cost of
payload fraction. Section 8 states which.

Both figures in this paragraph are larger than the ones an earlier version reported, and the
reason is bookkeeping rather than new evidence: the buffer power was previously taken as a
difference between two shaft stations and is now taken at the bus, where the buffer is.

**The energy side is a different matter, and it is far more comfortable than the power side.**
The buffer does not discharge continuously for the whole vertical phase. It discharges through
the take-off, which ends when the rotation begins and the wing starts carrying the aircraft;
it then recharges from the engine over hours of cruise, and discharges again for the landing.
At the achievable thrust-to-weight ratio of 1.132 the vertical acceleration is 0.132 g, so the
5 m s⁻¹ climb from which Section 7.4 enters the rotation is reached in 3.9 s and 9.6 m — and in
7.7 s and 19.3 m if full rotation authority is held in reserve. A take-off segment of ten to
twenty seconds at full draw therefore remains generous, though less so than at the 1.2 an
earlier version assumed. Against that:

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
| 0.735 kW kg⁻¹ | 3.9 kW | 0.50 | no |
| 1.30 kW kg⁻¹ | 4.9 kW | 0.59 | no |
| 2.50 kW kg⁻¹ | 7.1 kW | 0.75 | no |
| 5.63 kW kg⁻¹ | 10.9 kW | 1.00 | only just |

An earlier version of this table read 0.61, 0.71, 0.90 and 1.20 in the third column. Those
figures were a fifth too high at every row, because they were scaled from an assumed T/W of 1.2
at the top of the column while 10.9 kW is, by the sizing statement of Section 6.1 — thrust equal
to weight — the power for T/W = 1.00 exactly. The correction makes the bottom row worse in two
ways at once: the specific power it demands rises, for the reason given below, and what it buys
is a hover rather than a take-off. Leaving the ground needs the tip pairs as well.

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

---

# Supplementary S3 — Control axes in full

*Supplementary material to "The Architectural Cost of Hybrid VTOL: meryemAircraft, a
Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System".*

This was Section 4.4 of an earlier, longer version of the paper. It is reproduced in full so
that every control-axis number quoted in the main text can be traced to the calculation that
produced it. The scripts that produce these numbers, and the record of the corrections made to
them during the study, are in the repository the paper cites.

---

## S3.1 Control without control surfaces

The nose pair produces thrust. The four tip pairs produce moments. They are not lift
rotors and they are not sized to hover the aircraft; in the vertical phase they carry
under fifteen percent of the total power. For the light reference design each tip pair
is 0.20 m in diameter and produces 16.2 N during the transition manoeuvre, drawing
335 W, for a total of 1.34 kW across the four.

The principle is not new, and the paper is better for saying so. A survey of tail-sitter
development identifies it directly: "one way to generate a larger pitching moment to assist
with the transition from vertical to horizontal flight is to add propellers away from the axis
of rotation of the tail-sitter and apply a differential thrust to these propellers", and traces
the idea to work at NASA Ames around the turn of the century [30]. What is particular here is
not the mechanism but the arm and the accounting: the frames reach three tip chords rather than
a fraction of one, and they are structure the aircraft needs anyway, so the arm is charged to
the landing gear rather than to the control system.

The tip pairs sit at the ends of rigid frames that extend from each wing tip
perpendicular to the planform, above and below, by three hundred percent of the local
tip chord — 0.71 m in each direction, giving a vertical separation of 1.42 m between
the upper and lower pairs. Figure 7 gives the placement and the resulting moment
arms. The frames are long on purpose. The control moment is
M = 2 T L, so lengthening the arm buys the same moment with less thrust; and because
propeller power goes as thrust to the three-halves power, tripling the arm reduces the
power required for a given moment to roughly one fifth. The frames are structure that
is already needed for another reason, as Section 4.5 explains, so the arm is nearly
free.

Pitch and yaw are produced by the same four actuators, but not with the same arm, and the
difference has not previously been stated. Differential thrust between the upper and lower
pairs produces a moment about the spanwise axis through the frame length, 0.71 m; differential
thrust between the left and right pairs produces a moment about the remaining axis through the
**semi-span, 1.726 m**. The yaw arm is therefore 2.43 times the pitch arm, and since the
thrust available is the same, so is the moment: 55.9 N·m against 23.0 N·m at the quoted
tip thrust, or 42.8 against 17.6 on the conservative thrust of Section 7.6. Yaw is the
strongest axis this arrangement has, and it is strongest for a geometric reason rather than
a designed one. In hover these are the two axes the aircraft must control against
disturbance; in cruise, with the airframe rotated through ninety degrees, the same four
actuators address the same two axes with their roles exchanged. No actuator changes its
function, its orientation, or its mounting.

Roll is different, and this is the one place where propellers alone are not sufficient.
The result is elementary but decisive. Every propeller on this aircraft has its thrust
vector parallel to the body's longitudinal axis, so each thrust is a force
**F** = (F_x, 0, 0) applied at a station **r** = (x, y, z). The moment about the
longitudinal axis is

    M_x = y F_z − z F_y = 0

identically, for every propeller, at every thrust setting, regardless of where it is
mounted. No arrangement of parallel thrust vectors, and no number of them, can produce a
rolling moment. The only roll moment available from the propulsion system is the
residual reaction torque, which the counter-rotating arrangement of Section 4.3 has
deliberately reduced to nearly zero. The two design decisions oppose one another, and
the opposition is real rather than apparent.

This is the same limitation that constrains every tail-sitter, and it is worth being
precise about how others resolve it, because the resolution here is not a variation on
theirs but a consequence of a different decision made earlier.

Contemporary tail-sitters resolve it in one of two ways. Some place elevons in the
propeller wash, which is a control surface by any definition. Others — including a
carbon-fibre quadrotor tail-sitter that achieves full attitude control in every flight
mode with no control surfaces at all — carry four separate single-rotation propellers
and take their rolling moment from the *differential reaction torque* between them.
That is the same mechanism a multirotor uses for yaw, appearing as roll once the
airframe is rotated into wing-borne flight.

The second solution is unavailable here, and unavailable by construction. The coaxial
counter-rotating arrangement of Section 4.3 exists precisely to cancel reaction torque,
and it cancels the roll actuator along with it. The two decisions are not merely in
tension, as noted above; they are mutually exclusive. A tail-sitter cannot both null its
reaction torque and use that torque to roll.

This is the fork at which the present configuration departs from its nearest relatives,
and it is why the strip is not an accessory. It is the element that makes the
combination possible. The
resolution adopted here is different in kind. A single strip on the lower surface,
inclined at forty-five degrees, extends by a commanded amount rather than snapping between
two positions. The extension is the control variable, so the rolling moment is modulated by
how far the strip stands proud of the surface rather than by how long it is held out. For the light reference design it runs one hundred and twenty percent of the
root chord in length, reaching outboard to sixty-seven percent of the semi-span, and
stands 2 cm high at its inboard end and 6 cm at its outboard end.

Its authority comes from its length, not its height. The moment scales with the moment
arm, whereas the benefit of additional height saturates: at constant length, doubling
the height from 5 cm to 10 cm roughly doubles the roll rate, while extending the length
from sixty to one hundred and twenty percent of root chord raises it almost fourfold.
This comparison is robust to how the strip's force is modelled, because the length enters
both the affected area and the moment arm while the height enters only the first.

**Because extension is the control variable, the strip has a threshold, and the threshold has
been measured.** Tests of rearwardly located spoilers on two models established that
"projections of less than 0.01c produce negligible changes in lift", and warned that a device
with that property is poor as a control because "a small stick movement produces no change in
trim, whereas a larger movement of the stick may produce large changes" [19]. The strip here is
tapered, so the threshold is not crossed everywhere at once: height grows outboard while chord
shrinks, and the outboard end reaches one percent of local chord at seven percent of full
extension while the root does not reach it until forty-eight percent. Evaluated on the actual
chord distribution, the strip is wholly inert below seven percent of commanded travel and
wholly active above fifty.

| Commanded extension | First active station | Active length | Effective arm | Rolling moment, fraction of full |
|---:|---:|---:|---:|---:|
| 0.05 | none | 0 % | — | **0.000** |
| 0.10 | 0.945 m | 19 % | 1.057 m | 0.041 |
| 0.15 | 0.668 m | 43 % | 0.930 m | 0.113 |
| 0.20 | 0.481 m | 59 % | 0.850 m | 0.177 |
| 0.30 | 0.239 m | 80 % | 0.757 m | 0.293 |
| 0.40 | 0.090 m | 92 % | 0.707 m | 0.399 |
| 0.50 | root | 100 % | 0.679 m | 0.500 |

The last column is the one that matters, and it is more benign than the threshold suggests. The
part of the strip that survives the threshold is the part with the longest arm — the effective
arm rises from 0.679 m at full extension to 1.057 m at one tenth of it — so most of the lost
area is bought back by the lengthened arm. Above a quarter of travel the response is linear to
within five percent; below fifteen percent more than a quarter of the commanded moment is
missing; below seven percent there is none. **Continuous extension therefore does not give
continuous authority from zero**, and a control design would have to carry that dead band
explicitly. It bounds small corrections rather than large ones, which is the opposite of the
usual complaint about a threshold device, and it is a consequence of the taper rather than of
the concept: a strip of constant height fraction would cross the threshold everywhere at once.

**What the roll axis costs, and what it is opposed by, are computed here.** The roll axis
had not been examined with the care given to pitch, and doing so separates a part that can
be computed for this geometry from a part that cannot. Distributing the component masses of
Section 6.7 by the same volume-weighted rule used for pitch gives a roll inertia of
**25.0 kg·m²** — two and a half times the pitch inertia of 9.81 kg·m², because the mass is
spread along the span rather than along the chord. Roll damping was then computed for this
planform rather than taken from the literature: imposing the helix-angle twist
θ(y) = −arctan(p y / V) on a vortex-lattice solution of the actual geometry gives a damping
coefficient of magnitude **|C_l_p| = 0.358**, linear in roll rate to 0.4 rad s⁻¹ and
converged to within 1.3 percent over a threefold resolution refinement. At the cruise
condition this is a damping slope of 77.6 N·m per rad s⁻¹ and a roll time constant of
**0.32 s**, so the roll response is damping-dominated within a third of a second and the
steady rate, not the initial acceleration, is what a control moment buys.

**The requirement follows, and it is a requirement rather than a demonstration.** A steady
roll rate of twenty degrees per second at cruise needs **27.1 N·m**, and twenty-five degrees
per second needs 33.9 N·m; time to a thirty-degree bank is then about 1.2 s. Whether the
strip supplies that depends on which mechanism it works by, and the two candidates do not
agree:

| Mechanism | Rolling moment | Steady roll rate |
|---|---:|---:|
| The strip's own force, as a swept fence (C_N = 1.3, an upper bound) | 11.3 N·m | 8.4 ° s⁻¹ |
| A change in the half-wing's circulation, ΔC_L = 0.10 | 22.4 N·m | 16.6 ° s⁻¹ |
| the same, ΔC_L = 0.15 | 33.7 N·m | 24.8 ° s⁻¹ |
| the same, ΔC_L = 0.20 | 44.9 N·m | 33.1 ° s⁻¹ |

The strip's own force cannot produce the twenty to twenty-five degrees per second this
configuration needs — it falls short by a factor of about three, and an earlier version of
this paper quoted 46 N·m without saying where it came from. The moment must therefore come
from the second mechanism: the strip changes the circulation of the half-wing it sits on,
which is how a Gurney flap or a low fence works, and the affected area is the wing's, not
the strip's. Twenty degrees per second then asks for **ΔC_L ≈ 0.12** over the strip's span.

**That figure can be compared against a measurement, and the comparison is favourable.** Traub
[18] tested an aspect-ratio-three wing in a low-speed tunnel with a Gurney flap two percent of
chord in height, in two spanwise arrangements: full span, and **the inboard two-thirds only**.
The second is the same spanwise fraction the strip occupies here. From the measured lift-curve
slopes and zero-lift angles of that inboard case, the increment at lift coefficients spanning
the present cruise condition is:

| Clean C_L | With inboard flap | ΔC_L |
|---:|---:|---:|
| 0.30 | 0.442 | 0.142 |
| 0.45 | 0.608 | 0.158 |
| 0.60 | 0.773 | 0.173 |

The requirement of 0.12 sits below the measured range rather than above it. **Two differences
keep this short of a demonstration, and both cut the same way.** Traub's flap is at the
trailing edge and perpendicular to the surface; the strip here is a swept fence on the lower
surface, well forward of the trailing edge, and the mechanism is not identical. And his wing is
unswept and rectangular where this one is swept and tapered. What the measurement establishes
is that a device of this class, at this height fraction, over this spanwise extent, produces
lift increments of the magnitude required — not that this strip produces one.

**The comparison also exposes a design fault the paper had not noticed.** Traub's flap is two
percent of chord everywhere. The strip specified in Section 4.4 grows linearly from 2 cm to
6 cm while the chord it stands on shrinks:

| Station along the strip | Local chord | Strip height | h/c |
|---|---:|---:|---:|
| root | 0.969 m | 0.020 m | 2.1 % |
| mid | 0.682 m | 0.040 m | 5.9 % |
| outboard end | 0.436 m | 0.060 m | 13.7 % |

There is a measured threshold for this. A NASA study of lift-enhancing tabs — devices placed on
the **pressure side** of a wing and **near rather than at** the trailing edge, which is the
closest published geometry to the strip described here — reports that "for flap heights less
than about 1.5 % c, the maximum L/D can also increase" while "flap heights greater than 1.5 % c
cause a decrease in the maximum L/D" [32]. Every station on this strip is above that threshold
and the outboard end is nine times it.

**A law that held h/c constant would be a different trade, and the paper had not seen that
there was one to make.** Holding h/c at two percent everywhere gives a strip of 0.0165 m²
instead of 0.0466 m² — sixty-four percent less frontal area, and the same reduction in deployed
drag, from 16.7 N to 5.9 N at cruise. Because such a strip's area distribution follows the
chord, its centroid sits at 0.507 m, exactly where the half-wing's own area centroid sits, so
the rolling moment under the circulation mechanism is unchanged. What it costs is hover: the
part of the strip lying inside the slipstream shrinks from 0.0182 m² to 0.0101 m², a
forty-five percent reduction in whatever authority comes from the strip's *own* force at zero
airspeed. Which way that trade should be settled depends on which mechanism dominates in
hover, and this paper has not settled that. One thing that does *not* settle it is the L/D
threshold above, because that threshold is about a device left deployed: this one is commanded
on only while a roll is being flown, so its cruise-drag penalty is intermittent by construction
and paying it is not obviously wrong. What can be said is that **the present height law was
not derived from anything, and the alternatives are now visible.**

**Deploying it on one side yaws the aircraft, and the paper had not said so.** The strip raises
lift on the half-wing that carries it and also raises drag there; the aircraft therefore rolls
away from the strip and yaws towards it, which is adverse yaw in the classical sense. The
magnitude follows from the same drag estimate: 16.7 N at the present height law, acting at
0.679 m, is **11.3 N·m** of yawing moment, falling to 2.9 N·m for a strip held at two percent of
local chord. Against the 42.8 to 55.9 N·m of yaw authority computed above, the coupling costs
between five and twenty-six percent of the yaw axis while a roll is being commanded. **It is
covered, and it is covered by the axis that happens to be the strongest** — but it is a
coupling, it had not been stated, and a control design would have to allocate for it.

**It loads the pitch axis too, and that one is not comfortable.** A wind-tunnel study of
tapered-height Gurney flaps on a 60° delta wing — tested at heights of two and five percent of
root chord, which is the same height law and the same range as the strip specified here —
reports that "the flap significantly increases nose down pitching moment" [33]. The mechanism
is the same on this aircraft: the lift the strip adds acts aft of the centre of gravity, so it
pitches the nose down. How far aft depends on where along the chord the increment appears, and
that is the part this paper cannot compute, since the strip is neither at the trailing edge nor
straight. Bracketing it by placing the increment at mid-chord, three-quarter chord and the
trailing edge of the affected region:

| Increment acts at | Moment about CG | ΔC_m |
|---|---:|---:|
| mid-chord | 3.7 N·m | 0.005 |
| ¾ chord | 13.2 N·m | 0.019 |
| trailing edge (upper bound) | 22.7 N·m | 0.032 |

The tightest pitching-moment budget in the whole of Section 7.6 is **0.050**, at the end of the
rotation. At the upper end of this bracket, commanding a roll during that phase would consume
two thirds of it. **The conclusion is a scheduling requirement rather than a redesign: the roll
strip should not be commanded during the end of the rotation**, which is the one phase where
the pitch axis has least to spare. The paper had not previously identified any reason to
restrict when the strip may be used.

The coupling is not a novelty of this configuration, and the older literature states it more
bluntly than the estimate above does. The same NACA survey reports that where spoilers were
used for lateral control on tailless aircraft, "if only upgoing spoiler projections are used,
the pitching moments developed are **prohibitive**", and that "a spoiler arrangement employing
equal up and down projections would improve this condition" though the data then available were
insufficient to settle it [19]. The strip specified here projects from one surface only, which
is the arrangement that warning is about. Two things follow. The bracket computed above is a
lower bound in kind as well as in magnitude, since it counts the lift increment and not the
attendant pressure redistribution ahead of the device. And the remedy the survey names —
projection from both surfaces, so that the pitching contributions oppose while the rolling
contributions add — is available to this configuration in principle and has not been examined
here. **The scheduling restriction above is the conservative resolution; a two-sided strip
would be the structural one, and choosing between them needs the wind-tunnel measurement this
section has already asked for.**

**The same device has a third use, and it is the one that costs nothing.** Deployed on both
halves at once the strip is not a roll control but a speed brake, and in that mode the
pitching-moment objection does not arise: a wind-tunnel investigation of spoiler-type ailerons
used as speed brakes and glide-path controls found that they "had only a small effect on the
wing pitching moments", and — the part that matters for a configuration with one moving surface
— that "the rolling effectiveness of the ailerons will not be impaired by such use" [49]. A
tail-sitter lands vertically and does not need a glide-path control for that, but it descends
to the transition point like any other aircraft, and the strip gives it a descent-rate control
that no other part of this configuration provides. The transfer is directional only: those
tests are on conventional wings with slotted flaps at higher Mach number, and the device
projects from the upper surface rather than, as here, the lower.

**Roll authority is therefore sized, supported by a measurement on a comparable device, and
still not closed.** The quantity a future measurement must return is ΔC_L for this strip on
this planform, not a moment.

**Hover is the harder case, and for a reason that is structural rather than numerical.** At
zero airspeed only the inboard part of the strip is loaded, by the slipstream, and the same
circulation model over the slipstream-washed area gives 6.0 to 12.0 N·m for ΔC_L between
0.10 and 0.20 — enough for a thirty-degree bank in 1.5 to 2.1 s. But at zero airspeed there
is no aerodynamic damping at all: the roll axis is a double integrator, so the rate does not
settle and the strip must be commanded off rather than left on. Roll control in hover is
consequently a tighter problem than roll control in cruise, which is the reverse of the
usual situation and is a consequence of this configuration rather than of its numbers.

**The worst case, in which the extension is not modulated at all, is worth computing because
it bounds the actuator requirement.** Simulating the first-order roll dynamics above as though
the strip snapped between fully out and fully retracted, with a deadband and a finite actuator
delay, gives a bounded limit cycle: with a two-degree deadband and a fifty-millisecond
deployment the bank angle oscillates by ±0.2°, and at a hundred and fifty milliseconds by
±9.4°. **A proportional extension does not produce that limit cycle at all**, so these figures
are an upper bound on what the actuator must achieve rather than a description of how the
aircraft is flown — and they say that even a device reduced to two positions would be usable
provided it were fast. None of this is a closed-loop stability analysis, and none of it
substitutes for one.

**Two consequences of variable extension are worth stating, because both relieve constraints
identified above.** The couplings scale with the extension: adverse yaw and the nose-down
pitching moment are proportional to the lift and drag increments the strip produces, so a roll
commanded at a fraction of full extension carries that fraction of both. The scheduling
restriction derived above — that the strip should not be commanded at the end of the rotation —
is therefore a restriction on *full* extension, and small corrections remain available
throughout. And the height law is limited by those couplings rather than by mass: the strip's
own structure is a small item, so how far it may extend is set by how much yaw and pitch
disturbance the tip propellers can absorb, which is the calculation given above rather than
anything in Section 6.7.

**Yaw was examined last, and it separates cleanly into an easy half and an open half.** The
easy half is authority. The yaw inertia computed from the same mass distribution is
33.7 kg·m² — close, as it must be for a nearly planar aircraft, to the sum of the roll and
pitch inertias — so the available yaw moment turns the aircraft's own inertia at 73 to 95
degrees per second squared, reaching fifteen degrees of heading in about six tenths of a
second. Nothing in this axis is short of moment.

The open half is stability. A vortex-lattice solution of the planform at sideslip returns
**C_n_β = 0**: the wing supplies no directional stability whatever, which is not a defect of
the solution but the expected result for a planar surface with nothing to generate side
force. Two measurement campaigns say the same thing about real aircraft rather than about a
panel model. A NASA series of four 60°-swept flying wings tested from −8° to 48° of incidence
found that, without vertical tails, "each of these wings possessed unstable or essentially
neutral values of directional stability for most of the angles of attack tested" [20]; and the
NACA survey of tailless practice records that "the directional stability at low angles of
attack for the wing alone has generally been found to be inadequate" [19]. **The present
configuration is not unusual in lacking weathercock stability; it is normal, and every tailless
aircraft that flies has had to buy it somewhere.** Sweep gives this configuration its roll-due-to-sideslip — C_l_β = −0.045 per radian,
a healthy value — and gives it no weathercock stability at all. The profile-drag
contribution to yaw damping is likewise negligible, C_n_r = −0.0023, a time constant of over
a minute. That last number is less alarming than it looks, and the reason is conditional. Low
rotational damping is inherent to the tailless class, and free-flight experience is that the
small values "will not be excessively detrimental to the flying qualities **provided the
directional stability of the airplane is adequate**" [19] — so the two open items in this axis
are not independent, and the yaw-damping deficit is forgiven only if the weathercock
requirement below is actually met. The same source adds that lateral-oscillation damping is
most critical at high speed, because both C_n_r and the coupling between yawing and rolling
diminish at low incidence. **For this aircraft that names cruise, not transition, as the
critical case for Dutch roll.**

**And zero is an optimistic starting point, not a neutral one.** A vortex-lattice model has no
volume, so the calculation above contains the planform and nothing else. The centre body of a
blended wing is a body, it develops side force in sideslip, and that side force acts forward of
the centre of gravity. The survey states the magnitude in the only terms that matter here: on
tailless aircraft the destabilising effect of the fuselage and nacelles "is usually at least as
great as the stabilising effects contributed by the wing alone" [19]. The wing alone here
contributes zero, so the comparison gives no number — but the sign is unambiguous, and the true
figure the fairing has to make up is **below** zero rather than at it. Nothing in this section
quantifies that deficit, and the margin reported below should be read with it outstanding.

Directional stability must therefore come from the tip frames, which in cruise stand
perpendicular to the wing plane above and below each tip and are the only vertical surfaces
the aircraft has. Their mid-chord sits 0.879 m aft of the centre of gravity, which is a
long arm for a surface that already exists. Taking a lift-curve slope of 4 per radian for a
slender faired strut — an assumed value, not a measured one — the side area needed is 0.058 m²
to reach C_n_β = 0.03 and 0.097 m² to reach 0.05, which spread over the 2.84 m of combined
frame length is a fairing chord of 21 mm and 34 mm.

Those two targets were chosen by this study rather than taken from anywhere, and there is a
published criterion that should have been used instead. The NACA survey of tailless practice
states that tailless aircraft are **not exempt** from the conventional standard — directional
stability "should be as great as required on conventional airplanes if the same requirements
regarding satisfactory flying qualities are to be adhered to" — and puts that standard at
C_n_β "usually greater than **0.001 per degree**", noting that free-flight tunnel models were
flown successfully at one third of it but that "the best flying qualities of these models were
obtained with values of C_n_β in excess of 0.001" [19]. In radian measure the recommendation is
**0.0573** and the demonstrated floor is 0.0191. Both values this study picked lie below the
recommendation.

Sized against the criterion rather than against a guess, the fairing chord required is
**39 mm**, and the floor demonstrated in free flight is met at 13 mm. A faired strut of the
20 mm thickness assumed in Section 5.2 carries a chord of several times its thickness —
typically 50 to 70 mm — so the established criterion is met by a fairing **smaller than the
one the structure needs anyway**, with between a quarter and three quarters of that chord left
over. The conclusion the paper drew from its own two numbers survives being held to a real
standard, which is the only reason it is worth restating: directional stability on this
configuration does not ask for a surface, it asks for a fairing on a frame that is already
there.

**Where to buy it is a question the tailless literature has already answered, and the answer
is the arrangement this aircraft already has.** The NACA survey states that "if the tailless
airplane has a swept-back wing, the usual practice is to place the vertical tail surfaces at
the tips rather than at the center section in order to take advantage of the longer moment
arm" [19]. That is the tip-frame arrangement of Section 4.3, adopted here for the moment arm it
gives the control propellers and for the landing structure it provides, and it turns out to be
the placement a directional-stability surface wants for an independent reason.

The same source adds two things the estimate above does not contain, and they pull in opposite
directions. The first is favourable: because a tip fin's drag acts at a moment arm of half the
span, "the drag characteristics as well as the lift characteristics of the tip fins exert an
influence on the directional stability", and fins working on the profile-drag principle were
found more effective than those working on lift. The area estimated above was sized on lift
alone, so it is an **over**-estimate of what is needed. The second is a requirement: the toe
angle is not free. Fins of aspect ratio below about two must be toed *in*, and fins of moderate
or high aspect ratio toed *out* — and the frames here, at 1.42 m long against a fairing chord
of tens of millimetres, are firmly in the second class. Toe-out carries a hazard the paper had
no way of knowing about: yawing far enough to stall the rear fin produces a large
*destabilising* moment, where a toed-in fin stalling produces a stabilising one.

The magnitude, at least, is small. Wind-tunnel tests of a tail-less swept cargo configuration
with vertical tails carried on tip pods found the optimum toe angle for maximum lift-to-drag
ratio to be **about 1.5 degrees** for symmetric-section tails, with a cambered tail
"relatively insensitive to toe-in" [34]. The same tests found the lift-to-drag ratio "about the
same with all three vertical-tail designs, notwithstanding the 75 % larger area" of the largest
— which is the same conclusion reached above from the required-area side, arrived at by
measurement rather than by estimate. **The frame fairing therefore needs a toe angle of order a
degree or two, and that angle needs a sign.**

An earlier version of this paper left the sign open on the ground that these frames lie beyond
the aspect-ratio range of either source. That reasoning was wrong, because the rule is not a
correlation but a statement about which force does the work. Low-aspect-ratio fins are toed
*in* so that the stabilising moment is generated by the large induced drag such surfaces carry;
high-aspect-ratio fins are toed *out* so that it is generated by "the outwardly directed lift"
[19]. Raising the aspect ratio shifts the balance further from drag and towards lift, so it
strengthens the case for toe-out rather than carrying the rule outside its range. **The sign is
toe-out.**

What is genuinely open is narrower and more awkward. A fairing of 39 mm chord at cruise speed
sits at a Reynolds number near **80,000**, and the assumed lift-curve slope of 4 per radian is
an assumption at any Reynolds number and an optimistic one at that. Symmetric sections at low
Reynolds number are measured to behave badly in exactly the band a toe angle of one or two
degrees occupies: of four symmetric sections tested at Princeton, all showed lift-curve
nonlinearity about zero incidence, and in a more severe case the slope of the lift curve
"actually changed sign over a 3 deg range" [36].

**That is not one section behaving oddly; the same compilation states it as a property of the
class.** Introducing a section designed for horizontal tails, it gives the reason such a section
is cambered at all: "past work on symmetrical airfoils has shown that a deadband often appears
in the lift curve near zero degrees. This nonlinearity can lead to undesirable longitudinal
handling characteristics. Interestingly, cambered airfoils do not appear to have a similar,
intrinsic deadband region" [36]. Elsewhere it records a deadband at Reynolds numbers of 60 000
and 100 000 on a section where one was not expected, noting that "this type of behavior is
usually only seen on symmetrical airfoils at low Re's" and that "at higher Re's the dead band is
not present" [36]. The fairing sized here is a symmetric section at 80 000, which is inside that
range, and it is asked to work at one to two degrees, which is inside that band.

**The question is therefore not which way to toe the fairing but whether a surface of that
chord, at that Reynolds number, develops the side force this section has credited it with at
all.** Two things follow. The assumed 4 per radian is an upper bound and not a conservative
choice, because what the measurements remove is the linearity of the curve rather than only the
magnitude of its slope; a directional-stability margin computed on a linear derivative through
zero is computed on the one part of the curve the data say is not there. And the remedy the
source itself names is available at no structural cost: camber the fairing outboard and keep the
toe-out, so that the operating point sits on the linear part of a curve that has one. This
paper does not size that fairing. Doing so would mean choosing a slope from a curve it has not
measured, which is the error the preceding paragraph exists to record.

**This is the measurement this configuration would buy first**: side force and yawing moment on
a faired tip frame of the geometry of Section 4.5, symmetric and cambered, through small
sideslip, at a chord Reynolds number of 80 000. It is a small model in a small tunnel, and it
would either confirm the only directional-stability surface this aircraft has or remove it.

That same study is the third independent report of the finding this subsection began with: a
podded tailless wing was directionally *unstable*, and "the further addition of vertical tails
restores directional stability to the configuration" [34].

**That reframes the fairing, and the reframing is the substantive result of this
subsection.** Section 5.2 introduced the fairing as a drag measure and computed the frame
drag penalty on that basis. It is also, and not incidentally, the aircraft's directional
stability surface and its principal source of yaw damping. The two roles are served by the
same hardware — which is the same pattern the whole paper is about — but the paper had not
noticed the second role, and the fairing's chord is consequently constrained from two
directions rather than one. Neither the fin contribution nor the yaw damping it brings is
computed here. **Yaw authority is sized; directional stability is a requirement placed on a
component the design already carries.**

**Two measured effects work against the strip in exactly the conditions this configuration
needs it, and both were found by reading rather than by calculating.** Wind-tunnel tests of a
Gurney flap under controlled inflow turbulence report that the device "became less effective
after stall angle", and that at a turbulence intensity of 19 percent "the benefit to the
aerodynamic performance was negligible", against gains of 2.7 to 14.4 percent in lift-to-drag
ratio at 10.5 percent [35]. Both findings point at this aircraft. The transition passes through
incidences at which the outboard wing is post-stall, which is where roll disturbances are
largest and where the device is reported to weaken; and the strip's inboard portion is
deliberately placed inside the nose propeller's slipstream, which is not a low-turbulence
environment. **The slipstream placement that gives the strip authority at zero airspeed may
also be the place its mechanism works least well.** Neither effect is quantified for this
geometry — the cited tests are on a wind-turbine aerofoil with grid-generated freestream
turbulence, not a propeller wake — but the direction is measured rather than supposed, and it
is recorded in Section 8 as a risk to hover roll authority specifically.

**On the post-stall half of that risk the literature is not unanimous, and reporting only the
unfavourable half would misrepresent it.** A delayed-detached-eddy simulation of a 21 %-thick
section at twenty degrees of incidence — deep stall — with a Gurney flap of two percent chord,
which is the height fraction at this strip's root station, returns a lift coefficient higher by
ninety-four percent with the drag coefficient unchanged to within half a percent [37]. That is
the opposite of a device weakening past the stall. The two results are not directly comparable:
one is a measurement and the other a simulation whose plain-aerofoil baseline falls
twenty-five percent below the experimental lift at the same condition, and they vary different
things — one inflow turbulence, the other incidence. What can be said is that **the post-stall
behaviour of this class of device is contested, while the turbulence sensitivity is measured
and stands unopposed.** The risk carried into Section 8 is therefore the turbulence one
primarily, with post-stall behaviour an open question rather than a known deficit.

A third result bears on the part of the claim that looked weakest. The same device was
visualised in a water tunnel at a Reynolds number of 8 588 — four orders of magnitude below
the wind-tunnel work — and behaved in qualitative agreement with it, the authors attributing
this to the mechanism being an effective camber increase and therefore "an inviscid effect to
the first order" [38]. **That is the most direct support available for the claim that the strip
still works at zero airspeed**, where the only flow it sees is the slipstream and the Reynolds
number is at its lowest. It supports the direction and not the magnitude: the study is flow
visualisation and reports no forces. The same source also records the cost, measured rather
than estimated: a strip of 1.25 percent chord leaves drag unchanged from the clean wing, while
one of five percent brings a significant drag increase [38]. This strip runs from 2.1 to
13.7 percent.

The strip does one further thing that an ordinary aerodynamic surface cannot. Its
inboard portion lies inside the slipstream of the nose propeller, where the dynamic
pressure is set by the disc loading rather than by the airspeed:

    q_slipstream = T / A

For the light reference design this is 433 N m⁻² in hover — the dynamic pressure of a
26 m s⁻¹ freestream — available at zero airspeed. The strip therefore produces a usable
moment while the aircraft is standing still, which an aerodynamic surface outside the
slipstream cannot. Its outboard portion lies beyond the slipstream, where it works
against the freestream in cruise. The slipstream covers only twenty-seven to
thirty-nine percent of the semi-span, so lengthening the strip to serve cruise does not
compromise its hover function; one device serves two regimes. Figure 8 shows the strip
against the slipstream boundary: the inboard 46 % of its length lies inside, the
outboard 54 % outside.

---

# Supplementary S4 — Rotational authority, trim, and the transition envelope

*Supplementary material to "The Architectural Cost of Hybrid VTOL: meryemAircraft, a
Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System".*

This was Section 7.6 of an earlier, longer version of the paper. It is reproduced in full so
that every figure in the trim chain and the rotational-authority budget can be traced to the
calculation that produced it — including the inertia derivation, the rotation profiles, the
centre-of-gravity window, the twist sweep, and the measured reflex-section evidence. The
scripts are in the repository the paper cites.

---

## S4.1 Whether there is enough authority to rotate

Section 7.4 drives the body angle kinematically. The aircraft does not rotate in that
simulation; it is *assumed* to rotate, and the moment producing the rotation does not
appear. Section 8.6 records this. What follows does not remove that limitation — a full
six-degree-of-freedom treatment would need pitching-moment coefficients through ninety
degrees of incidence, and no such data exists for this planform — but it closes the part
of the question that can be closed without them.

**The test is a lower bound.** If the tip propellers cannot rotate the aircraft's inertia,
they certainly cannot rotate it against aerodynamic moment as well. If they can, the
aerodynamic margin remains unknown and is reported as unknown.

**Inertia, and where the mass may sit.** The component build-up of Section 6.7 supplies the
masses; the planform of Section 4.2 supplies where they can go. The shell and internal
structure are distributed over the planform, the tip frames along their own length, the tip
motors and propellers at the ends of those frames. The coaxial pair, its hub and the
electric machine that drives it are fixed at the nose. Everything else — engine, generator,
power electronics, fuel, battery, avionics, payload — is distributed **in proportion to the
internal volume available to hold it**, which is the constraint a real internal arrangement
faces and is not a free choice.

That distinction matters more than it appears. An earlier version of this calculation placed
those items along the root chord by hand and obtained a centre of gravity at 57 percent of
root chord. That was wrong, and the reason is the sweep: the outboard sections lie well aft
of the root trailing edge, so the internal volume's own centroid sits at 78.3 percent of root
chord and the structural centroid at 99 percent. Placed where the volume actually is, the
centre of gravity falls at **80 percent of root chord** for the light design and 82 percent
for the heavy one, and the moment of inertia about the spanwise axis — the axis the
transition rotates about — is **9.81 kg·m²** and **2 503 kg·m²**. The hand-placed figures
were 40 and 30 percent lower, and the margins below are correspondingly tighter than that
earlier version reported.

**The rotation profile matters, and Section 7.4's cannot be produced.** That simulation
ramps the body angle linearly, which requires zero torque throughout and infinite torque at
each end. Two profiles a finite moment can produce bracket the choice: a bang-bang profile,
accelerating for the first half and decelerating for the second, needs a peak angular
acceleration of 4Δθ/t_r², and is the cheapest rest-to-rest profile there is; a smooth
profile bringing angular velocity and acceleration to zero at both ends needs 6Δθ/t_r². A
feasibility test — whether the manoeuvre is possible at all — must use the cheaper of the
two, so the bang-bang value is taken as the requirement and the smooth value is reported
alongside it as what a gentler command would cost.

**Authority.** The frames place the upper and lower pairs 0.71 m from the planform in the
light design, and differential thrust between them acts about the spanwise axis, as
Section 4.3 sets out. Propeller thrust on this aircraft cannot reverse, so the largest
differential available is the upper pairs at full thrust against the lower pairs at zero,
which is the M = 2TL of Section 4.3 and not four times the single-pair moment. The
available moments are therefore 23.0 N·m for the light design at its quoted 16.2 N per
pair, and 952 N·m for the heavy design, whose transition thrust is not quoted in Section
6.3 and is computed here from its twelve percent power share as 200 N per pair.

| | Required, bang-bang | Required, smooth | Available | Margin, bang-bang | Margin, smooth |
|---|---:|---:|---:|---:|---:|
| Light, t_r = 2 s | 15.4 N·m | 23.1 N·m | 23.0 N·m | **1.49 ×** | 0.99 × |
| Heavy, t_r = 5.1 s | 605 N·m | 907 N·m | 952 N·m | **1.57 ×** | 1.05 × |

**The reference rotation times are actuator-limited lower bounds, not comfortable choices.**
Both designs close on the cheapest rest-to-rest profile with a margin near 1.5, and both sit
essentially at unity on a smooth one: 2.01 s and 4.98 s are the shortest smoothly-commanded
rotations the tip propellers can force, against reference times of 2 and 5.1 s. Read
correctly, that is not a margin of five percent — it is the statement that the reference
rotation *is* the minimum smooth rotation the moment authority allows, to within the
precision of the thrust estimate, and that anything faster is available only by commanding a
profile with discontinuous angular acceleration. The two designs are at the same point on the
same constraint, which is the tip-propeller moment; the transition times follow from it
rather than being chosen. A design iteration wanting genuine comfort on a smooth command
would lengthen both rotations by about a quarter, which Section 7.4 shows costs nothing in
altitude — and that, rather than the quoted times, is what a design study should carry
forward.

**The field has a name for what this section computes, and a settled opinion about where in it
to fly.** The feasible set of transition states is called a *transition corridor*, and it is
used to turn trajectory generation over a complex aircraft model into a constrained motion
planning problem [31]. The envelope of Section 7.4 and the moment limits here are a corridor of
that kind, computed rather than borrowed. On where to fly inside it, the same source is
explicit that existing corridor-based studies "only try to plan the flight trajectory in the
middle of the corridor, considering that the corridor bounds might be sensitive to aerodynamic
uncertainties and disturbance". **The reference rotation times of this paper are on the bound,
not in the middle** — which is exactly the practice that source warns against, and an
independent reason to read the recommendation of the preceding paragraph as the design
statement and the quoted 2 s and 5.1 s as the limit they approach.

**This calculation set the heavy design's rotation time.** An earlier version of this study
used four seconds. Against the inertia of this section that gives margins of 0.97 on the
cheapest profile and 0.65 on a smooth one — that is, infeasible on both, since the shortest
rotations the moment authority allows are 4.06 s and 4.98 s. Four seconds was not a margin
and, with the corrected inertia, not even a boundary. Lengthening the rotation to 5.1 s
brings the heavy margins to 1.57 and 1.05, matching the light design's 1.49 and 0.99 at its
quoted two seconds, and costs nothing: Table 4 shows the tip-propeller power falling from
thirteen percent of hover power to six, and the altitude-loss result of Section 7.4 is
unchanged, remaining zero at every profile tested when the rotation is entered in a climb.
The light design's own two seconds is on the same boundary — its smooth minimum is 2.01 s —
so neither reference design has margin to spare on a smooth command, and both should be read
as sized by this constraint.

This is also, in moment terms, what Table 4 of Section 6.4 already said in units of power:
that four seconds consumed nearly the whole tip-propeller allocation. The two statements
agree, and the present calculation adds the rotation profile, which Table 4 did not
distinguish.

The light figure depends on a thrust the paper quotes without a basis. At 335 W and 0.20 m
diameter, 16.2 N implies a figure of merit of 0.702 with no coaxial interference loss,
where the hover figure of merit used elsewhere is 0.599. The disc area used is that of one
rotor rather than two, which is the ordinary treatment of a coaxial pair — the lower rotor
works in the upper's wake, so the pair is charged a single disc and an interference penalty
rather than twice the area.

**Recomputing at 0.599 with a fifteen percent coaxial loss gives 12.4 N and an available moment
of 17.6 N·m, which against the bang-bang requirement of 15.4 N·m is a margin of 1.14 and against
the smooth requirement of 23.1 N·m is 0.76.** An earlier version of this section reported 1.59
here and called it comfortable; that figure does not follow from 17.6 against 15.4, and the
correct one is not comfortable. On the conservative thrust basis the light design closes only on
the cheapest rotation profile and only just, and the smooth profile does not close at all at two
seconds. The heavy figure was computed on that conservative basis to begin with, which is why
the two designs are not directly comparable on this row. Section 8 carries the consequence: the
reference rotation times are actuator-limited lower bounds under either thrust basis, and under
the conservative one the light design has no margin to give.

**The margin narrows with size, and the narrowing is measured rather than derived.** An
earlier version of this section derived a scaling law by assuming geometric similarity.
The two reference designs are not geometrically similar: span grows by a factor 3.345 while
mass grows by twenty, and 3.345³ is 37.4, not 20 — the wing loading rises from 25.3 to
45.0 kg m⁻² precisely because they are not. The ratios are therefore read from the two
computed designs instead. Inertia grows by 255.1 while available moment grows by only 41.4,
so the margin is preserved when required moment grows by the same 41.4 — which fixes the
rotation time at 4.96 s, and is where the 5.1 s of Section 6.3 comes from. Section 7.4 already concluded that the
larger aircraft must rotate more slowly; the quantitative form of that statement is that
the rotation time must grow as the square root of the ratio of inertia growth to moment
growth, and that setting it any faster spends control margin to buy nothing, since a slower
rotation loses no more altitude.
**What this does not establish.** The centre of pressure moves as the aircraft rotates, and
the pitching moment that produces is not computed here. The margins above are inertial: they
say the propellers can turn the aircraft's own inertia and say nothing about turning it
against aerodynamic moment. This is a necessary condition, not a sufficient one.

**How much is left over can be resolved along the trajectory, and doing so corrects the
question.** The moment remaining after the inertia is turned — 11.9 N·m for the light design
and 489 N·m for the heavy one — divided by q S c̄ gives the pitching-moment coefficient that
would consume it. Evaluating that along the trajectory of Section 7.4 rather than at a single
representative speed shows something the single-speed form obscured: **the aircraft does not
reach ninety degrees of incidence.** The body rotates through ninety degrees, but the relative
wind rotates with it, because the aircraft is accelerating and climbing at the same time. Peak
incidence is 17.5° for the light design entered in a 5 m s⁻¹ climb, and 21.6° entered from
rest.

| | Entry | Peak incidence | Airspeed there | C_m budget there | Tightest budget, and where |
|---|---|---:|---:|---:|---|
| Light | 5 m s⁻¹ climb | 17.5° | 7.3 m s⁻¹ | 0.205 | 0.050, at rotation end, α = 4.9°, 14.7 m s⁻¹ |
| Light | from rest | 21.6° | 2.8 m s⁻¹ | 1.381 | 0.051, at rotation end, α = 17.7°, 14.7 m s⁻¹ |
| Heavy | 5 m s⁻¹ climb | 5.4° | 35.6 m s⁻¹ | 0.010 | 0.010, at rotation end |
| Heavy | from rest | 20.5° | 6.8 m s⁻¹ | 0.287 | 0.011, at rotation end, α = 6.5°, 35.4 m s⁻¹ |

These budgets are what remains of the tip-propeller moment after the inertia is turned, so
they follow the corrected inertia of this section. An earlier version of this table used an
inertia thirty-nine percent lower and reported budgets correspondingly larger — 0.322 at the
light design's peak incidence rather than 0.205. The values above supersede it.

**The constraint splits into two, and they are different problems.** In the middle of the
rotation the incidence is high — seventeen to twenty-two degrees — but the dynamic pressure is
low, and the coefficient that would consume the margin is 0.205 entering in a climb and 1.38
entering from rest. An earlier version of this paper compared these against a generic
post-stall range quoted for swept planforms; that comparison is dropped, because the
trajectory-resolved budget above supersedes it and the generic range was not attributable to
a source we had read. What the budgets say without it is enough: entering the rotation from a
climb buys altitude at the cost of arriving at the high-incidence phase faster, and therefore
with less moment to spare, and 0.205 is not a comfortable coefficient to have left. At the end of the rotation the incidence is small, five to
six degrees, but the aircraft is fast, and the budget falls to 0.050 for the light design and
0.010 for the heavy one. That second condition is **not** a post-stall problem: it is the
trim question of a tailless aircraft at its cruise incidence, and it is examined below rather
than asserted — though examining it separates a part that is shown from a part that is not.

**The centre of gravity is an assumption, and it is stated as one.** No detailed internal
layout exists for this aircraft, so none can be measured. In its place a first-order
packaging rule is adopted: the non-structural masses — fuel, payload, engine, generator,
buffer — are distributed in proportion to the internal volume available at each station,
and the structural mass in proportion to the shell area. Applied to the planform of
Section 4.2 this rule puts the centre of gravity at **0.778 m aft of the root leading edge**,
which is 80.2 percent of root chord, or 21.9 percent of mean aerodynamic chord aft of the
mean-chord leading edge. Every stability figure below follows from that rule and not from a
layout; a different arrangement of the same masses gives a different centre of gravity, which
is why the sensitivity to it is tabulated rather than assumed away. Burning the full fuel
load moves the centre of gravity aft by 0.3 points of root chord, which is inside the
tabulated window and is therefore not a separate constraint.

**Static stability is shown.** A vortex-lattice solution over the planform of Section 4.2
places the neutral point at 0.859 m from the root leading edge — 34.4 percent of mean
aerodynamic chord, an entirely conventional value — and the result is converged, moving by
0.26 percent over a threefold refinement. With the centre of gravity where the packaging rule
puts it, the static margin is **+12.5 percent of mean aerodynamic chord**, in the middle of
the usual tailless band of five to fifteen percent. The configuration is statically stable in
pitch, and it owes that to the sweep, which carries the neutral point aft faster than it
carries the volume. All chord-referenced quantities here use the true mean aerodynamic chord,
0.651 m; an earlier version of this section quoted the margin on the mean aerodynamic chord
but the trim requirement on the mean geometric chord, 0.573 m, and the two are now on the
same datum. Because that error was a mismatch of conventions rather than of arithmetic, the
absence of a second one was checked rather than assumed: the two chains — centre of gravity
to neutral point to static margin, and centre of gravity to aerodynamic moment to required
trim coefficient — were tested for a common origin, a common sign convention, independence
of dynamic pressure, and agreement between the coefficient route and a dimensional route
that never forms a coefficient at all. All four hold; in particular W(x_np − x_cg) and
C_L × (static margin) × q S c̄ give the same 39.82 N·m. Re-deriving the margin directly from
the solver's moment about the centre of gravity, rather than from the neutral point, gives
12.8 percent against the 12.5 quoted above; the 0.3-point spread is the curvature of the
fitted lift-moment slope and is smaller than the spread across the centre-of-gravity window.

**Trim was an open item, and it is now closed — by twist rather than by camber, and at a
price.** At the cruise lift coefficient of 0.45 the moment to be balanced about the centre of
gravity has coefficient C_L × (static margin): 0.056 at the centre of gravity the packaging
rule gives, and less further aft.

| CG, % root chord | x_cg, m | Static margin, % MAC | Moment to be balanced |
|---:|---:|---:|---:|
| 78 | 0.757 | +15.7 | 0.071 |
| 80.2 (packaging rule) | 0.778 | +12.5 | 0.056 |
| 83 | 0.805 | +8.3 | 0.037 |
| 85 | 0.825 | +5.3 | 0.024 |

**Two published benchmarks place that window, and both place it favourably.** A blended-wing
UAV of this class reports its own static margin of 0.081 of the mean aerodynamic chord as
"marginally outside the typical range for static longitudinal stability", which it gives as
0.1 to 0.3, and its C_m_α of −0.086 per radian against a typical range of −0.3 to −1.5,
concluding that stability augmentation "through either forward movement of the centre of
gravity or additional reflex of the airfoils is advisable" [41]. The configuration here sits
inside both ranges at the packaging centre of gravity: 0.125 of the mean aerodynamic chord, and
C_m_α = −0.48 per radian on the lift-curve slope of 3.86 per radian the same solution returns.
The second of those inherits the magnitude caveat of Section 6.6 — but that caveat runs the
safe way here, since a lift-curve slope under-stated makes C_m_α under-stated too, and the true
value would lie further inside the range rather than outside it. **The aft limit of the window,
at 5.3 percent, is the one that falls outside the published range**, which is a second reason
beyond static margin alone to prefer the packaging value to the aft end of the window.

An earlier version of this paper supposed that reflexed sections would supply this, on the
strength of a range its authors had not read. Reading the source settles it in the other
direction. In the variable-density tunnel measurements of Jacobs, Ward and Pinkerton [17], the
reflexed section NACA 2R212 — two percent camber, mean line shaped specifically to give a
small positive moment — returns **C_m0 = +0.004**, against −0.002 for the symmetric 0012 and
−0.044 for the conventionally cambered 2412. That is one fourteenth of what the centre of
gravity above demands, and one sixth of what even the aftmost entry in the table demands. The
same report concludes that reflexed mean lines "may be of questionable value because of the
adverse effect of this mean-line shape on the maximum lift coefficient." **Reflex of the
magnitude that has actually been measured does not trim this aircraft.**

**2R212 is not an isolated case, and the wider measured record is worse for reflex than that
single number suggests.** Three further families were tested in the same variable-density
tunnel, with pitching moment measured rather than computed, and none of them returns a positive
value:

| Section | c_m at zero lift | Test |
|---|---:|---|
| NACA 2R212 | **+0.004** | Variable-density tunnel [17] |
| Boeing 106R | −0.001 | Variable-density tunnel, Re ≈ 3.1 × 10⁶ [45] |
| Navy 60R | ≈ −0.001 | as above [45] |
| Göttingen 398R | −0.007 | as above [45] |
| NACA M6 | −0.001 | as above [45] |
| NACA 4409R | −0.025 | Variable-density tunnel [46] |
| NACA 4412R | −0.030 | as above [46] |
| NACA 4415R | −0.031 | as above [46] |
| NACA 4418R | −0.030 | as above [46] |

The three 1930s reflexed sections of the second group were built by replacing the mean line aft
of thirty percent chord with a curve chosen, from thin-aerofoil theory, to give **zero** moment
about the quarter chord — and the measurements report their moments as "practically zero" over
the useful incidence range [45]. The 4400R family was designed to a target of −0.03 and the
report states that "the design pitching-moment coefficient was realized" [46]. **Reflex, as
actually built and measured, is a device for removing negative pitching moment, not for
producing positive pitching moment.** Across nine measured sections the single positive value
is +0.004, and the requirement here is +0.056.

An earlier version of this paper wrote that no plausible amount of reflex would trim this
aircraft, then withdrew that as too wide on the strength of a published optimisation which
trims a blended-wing-body of this class by treating reflex as a design variable and closing the
chain with only **2.44 degrees** of twist [41]. The withdrawal went too far in the other
direction. That study publishes no moment coefficient for the sections it generates, so the
inference that they supply much more than 0.004 was an inference and not a reading; the measured
record above runs against it. What the comparison does establish is narrower and still worth
saying: that study's trim requirement is the lighter one — a static margin of 0.081 of the mean
aerodynamic chord against 0.125 here — and reflex was not asked to act alone.

**A flying tail-sitter shows where the positive moment actually comes from.** The aerodynamic
model identification of a VTOL tail-sitter describes its own trim state explicitly: the aircraft
uses a **symmetric** section, and "the upward trim of elevons makes the symmetric airfoil to
have reflexed camber line. It makes the positive pitching moment at the aerodynamic center"
[51]. The reflex that trims that aircraft is not a property of its section but a deflected
control surface held permanently out of line — and its authors note that the elevons are sized
larger than a conventional flying wing's in order to produce enough moment for the transition.
That is the same trade this configuration faces, resolved with a control surface where this one
resolves it with twist, and it carries the same kind of continuous cost.

**The position this paper takes is therefore the conservative one, and it is a statement about
evidence rather than about physics.** The trim moment this configuration needs is C_m = +0.056.
No measured section approaches it. Whether a physically realisable reflexed section or planform
could supply it is unresolved, and this paper does not assume either way; it closes the chain
with twist, which is the route for which a computed requirement and a costed penalty both
exist.

Two costs of the reflex route are measured, and both bear on a tail-sitter specifically.
Reflex reduced maximum lift by about twelve percent in the first family [45] and by about ten
percent in the second [46] — and maximum lift is what a tail-sitter needs at the high-incidence
end of its transition. The same measurements also found that although minimum profile drag fell
slightly, "if the profile drag coefficients are compared at equal values of the lift
coefficient, the normal airfoil will be seen to have the lower profile drag except at small
values of the lift coefficient" [45].

**The reflex route is not free either, and the same literature prices it.** A separate
blended-wing UAV that trims by reflex rather than by twist records that carrying reflex over a
wide span "is not conducive to the improvement of overall lift-to-drag performance" [44]. Both
roads to trim on a tailless configuration therefore cost cruise efficiency, which is the
reading Section 5.4 places on the 4.3 percent charged there: it is the price of having no tail,
not the price of having chosen the wrong way to do without one.

The requirement 2R212 was built to meet is the one this configuration has. A survey of sections
assembled for flying-wing use states it in the same terms — "for trim flight, pitching moment
coefficient at zero angle of attack, C_m0, must be positive" — and identifies the practical
family as the Eppler 184, 186 and 387, FX 69-H-083, NACA M5 and M6, Selig 5010 and 5020, MH 60
and HS-522 [27]. **No numerical value is taken from that survey here.** Its tabulated
coefficients are negative for all ten sections, which contradicts the positive-C_m0 requirement
the same paper states two pages earlier, and a quantity this study cannot reconcile is not a
quantity it will cite. The only measured number in hand remains the +0.004 of 2R212.

The most heavily cited experimental compilation of low-Reynolds section data cannot settle the
question either, and says so itself: the UIUC low-speed tunnel "does not provide pitching
moment data," so every moment coefficient in that compilation was "determined computationally
using either the Eppler, ISES or XFOIL code" [36]. What those computed values show, however,
points the same way as the measurement. The only flying-wing section in the compilation — the
slightly reflexed MH45, designed for that application — carries C_m,c/4 = **−0.006**, and the
single positive entry among forty-one sections is not a reflexed section at all but a
five-percent-camber high-lift section designed under an explicit low-pitching-moment
constraint, at **+0.004**. That computed result points the same way as the measurements
tabulated above: across four independent sources — one computational compilation and three
tunnel campaigns — the reflexed and flying-wing sections return quarter-chord moments at or
below zero, and the single positive value this configuration could lean on rests on one
measurement from 1933. **The conclusion above is strengthened rather than weakened: the reflex
route is closed, and the twist is what trims this aircraft.**

**How much a section could contribute, if one existed that contributed more, is worth stating
as a sensitivity — provided it is read as what it is.** The rows below are not candidate
sections. They are the answer to "how much would have to come from somewhere else", and the
measured evidence sits in the second row, with the whole measured record of the preceding table
at or below it:

| If a section supplied C_m0 = | Washout still needed | Inviscid e | Cruise L/D | Measured precedent |
|---:|---:|---:|---:|---|
| 0 | 9.2° | 0.865 | 11.68 | four sections, at −0.001 to −0.007 |
| 0.004 | 8.6° | 0.875 | 11.73 | one section, NACA 2R212 |
| 0.020 | 6.0° | 0.937 | 12.01 | **none** |
| 0.050 | 1.3° | 0.986 | 12.21 | **none** |

At the one measured positive value, reflex buys half a degree of the nine and the trim problem
stays a twist problem. The two lower rows of the table describe a section nobody has published
a measurement of, and the four sections of the 4400R family fall *below* the top row rather
than between the rows. **This paper therefore takes the branch the evidence supports** — nine
degrees of washout and the penalty that goes with it — and does not offer the third row as an
alternative design point. What would change this is a measurement, not an assumption: a
reflexed section, tested in a tunnel that measures moment, returning a positive C_m0 an order
of magnitude above 0.004. Section 8 records that no such measurement was found.

What trims it is washout, which is how tailless aircraft have always been trimmed: on a swept
wing the tips lie well aft, so negative tip incidence produces a nose-up moment about the
centre of gravity. Because this mechanism is geometric rather than sectional, the
vortex-lattice model of Section 6.6 — whose sections are symmetric — can compute it directly.
Applying a linear twist from zero at the root to θ_tip at the tip and re-trimming to
C_L = 0.45 at each value:

| Tip washout | Trim α | C_m about CG | Induced C_D | Span efficiency e | Cruise L/D |
|---:|---:|---:|---:|---:|---:|
| 0° | 6.68° | −0.058 | 0.01077 | 0.993 | 12.65 |
| −4° | 8.20° | −0.034 | 0.01102 | 0.971 | 12.56 |
| −6° | 8.98° | −0.021 | 0.01141 | 0.938 | 12.43 |
| **−9°** | **10.16°** | **−0.001** | **0.01237** | **0.865** | **12.11** |

**Nine degrees of tip washout trims the aircraft at cruise with no camber at all.** That is a
large twist by transport-aircraft standards and an ordinary one for a swept tailless design,
and it is not free: the span efficiency falls from 0.993 to 0.865 and the cruise lift-to-drag
ratio from 12.65 to 12.11, a **4.3 percent penalty paid to be tailless**. It is the same kind
of payment the rest of this paper is about — a capability bought in one currency and charged
in another — and it had not previously been counted.

**One assumption is put at risk by this, and the risk runs the wrong way.** Section 6.2 assumed
an Oswald span efficiency of 0.85, and the range figures of Section 6.3 rest on it. Section 6.6
supported that assumption by computing an inviscid span efficiency of 0.99 for the planform and
noting that an Oswald-type value runs at roughly 85 to 90 percent of the inviscid one, which
places 0.85 at the bottom of the implied band of 0.84 to 0.89 — conservative, if only just.

That argument was made for a wing without twist. The wing without twist cannot be trimmed. For
the trimmed wing the inviscid figure is not 0.99 but **0.865**, and the same reasoning then
implies an Oswald value between **0.735 and 0.78** — a band the assumed 0.85 sits *above*
rather than inside. If that reasoning holds, the cruise lift-to-drag ratio is 11.4 to 11.7
rather than 12.0, and the range figures of Section 6.3 fall by three to five percent.

**That ratio has since been computed rather than assumed, and it is worth setting out what it
replaced.** An earlier version of this section could only bound the viscous-to-inviscid ratio
from the literature. Traub reports both an inviscid Oswald factor from a vortex-lattice solution
and a measured one from the tunnel for three wings [18]; the planar case gives a
measured-to-inviscid ratio of 0.95, but his two non-planar cases give 1.01 and 1.07, which
cannot be right for a real wing and are presumably an artefact of comparing an uncorrected
tunnel measurement with an inviscid calculation. That data bounds the ratio loosely rather than
fixing it, and the section carried a band of 0.85 to 0.95 with an implied penalty of one to five
percent.

Section 6.6 now computes it on this planform, by calling the section solver at each strip's own
local lift coefficient and integrating the profile drag across the span. The result:

| | Inviscid e | Oswald e | Ratio | Cruise L/D |
|---|---:|---:|---:|---:|
| Untwisted | 0.990 | 0.931 | 0.940 | 12.40 |
| **Trimmed, −9°** | **0.859** | **0.817** | **0.951** | **11.87** |

**The direction the section predicted is confirmed and the magnitude is at the mild end of the
band it allowed.** The ratio is 0.951 rather than the 0.85 the borrowed rule would have given,
so the viscous penalty is smaller than feared; but the trimmed wing starts at 0.859, and the
product lands at 0.817 — **below the assumed 0.85 by 3.9 percent**, costing 1.4 percent of cruise
lift-to-drag ratio rather than the three to five percent this section had allowed. The range
figures of Section 6.3 fall by the same 1.4 percent, and are not restated at the lower value
because they are computed on the stated assumption; the correction is reported here instead.

Two things the computed number does not settle. Its sections are symmetric, so it is a lower
bound: a cambered section reaching the same local lift coefficient at lower incidence would
carry less profile drag. And the strip integration ignores sweep, which at 45° at the root is
not a small omission — though the alternative, simple-sweep theory, halves the profile drag,
which is a sign that the transformation does not apply to skin friction rather than a measure
of the uncertainty. It is worth adding that 0.85 at this aspect ratio was a conventional choice
rather than a careless one — an independent eVTOL sizing study adopts the same value at aspect
ratio 7.0 [26] — which is precisely why it survived so long without being examined.

**What is still not established.** The twist here is linear, chosen for simplicity rather than
optimised; a distribution shaped for span loading would trim at the same moment for a smaller
efficiency penalty, so 4.3 percent should be read as an upper bound on the cost rather than as
the cost. The vortex-lattice solution is inviscid, so it says nothing about how washout of this
magnitude changes the stall behaviour of the outboard sections — washout normally improves it,
which is a reason to expect no unpleasant surprise, not a demonstration that there is none.
Two places where this result could have propagated were checked and do not. The root bending
moment of Section 6.7, 934 N·m, was computed on an untwisted loading; washout moves lift inboard
and can therefore only reduce it, so the spar sizing and the mass budget that follows are
conservative rather than threatened — the recomputation has not been done because its direction
is not in doubt. And washout makes the root stall before the tip on a swept wing, which is the
favourable direction for the transition of Section 7.4 rather than the unfavourable one — a
point that matters more than it first appears, because the tailless literature reports the
unfavourable direction as a real hazard. The NASA series of 60°-swept flying wings found a
pitch-up at high incidence that "became more severe as aspect ratio was increased", severe
enough on some configurations to produce a *hung stall* — a trim condition with insufficient
nose-down control to recover [20]. Those wings are of aspect ratio 1.15 to 2.15 and their
pitch-up is driven by leading-edge vortex breakdown, which a wing of aspect ratio 6.03 swept at
45° at the root and 35° at the tip is unlikely to reproduce in the same form. But the trend
they report runs the wrong way for a higher-aspect-ratio wing, and the incidences at which it
appears overlap the 17° to 22° this aircraft passes through in transition. **This is a reason
to keep transition controllability open rather than a new closure**, and it is the second
independent reason to want the washout that Section 7.6 already requires for trim.

A second pitch-up mechanism was found afterwards, and it does not care about aspect ratio at
all. In a blended-wing-body UAV analysed by both a low-fidelity method and RANS, the moment
prediction departs from the computation above eight degrees of incidence because "the main wing
stalls before the main body, causing the BWB to pitch-up" [39]. That is a statement about which
part of the planform separates first, not about leading-edge vortex breakdown, so the
aspect-ratio argument that limits the previous hazard offers no protection against this one.
**Washout does.** On a swept wing washout makes the root stall before the tip, and on a blended
wing the root is the body — so the twist Section 7.6 requires for trim also reverses the stall
order that produces this pitch-up. The twist therefore earns its cost three times: it closes
the trim chain, it delays tip stall on a swept planform, and it inverts the stall sequence
behind the blended-wing pitch-break. **None of this makes the 4.3 percent penalty of Section
5.4 disappear. It means the penalty is not being paid for one thing.** And the
aft limit of the centre-of-gravity window, roughly 85 percent of root chord, is still set by
static margin alone and is still firm. What has changed is that the forward limit is no
longer set by a section property nobody had measured; it is set by how much twist the design is
willing to pay for.

**The requirement is therefore smaller and more recognisable than first stated.** An earlier
version of this section asked for pitching-moment coefficients through ninety degrees of
incidence, which would have needed a wind tunnel or an unsteady computational campaign. What
is actually required is (a) the pitching moment up to roughly twenty-two degrees at low
dynamic pressure, a mildly post-stall regime much closer to available data, and (b) trim at
cruise incidence, which the configuration needs in any case. Neither is supplied here, and
transition controllability remains the study's principal open item — but it is now an open
item of ordinary size, and the reduced computational campaigns rejected earlier were rejected
for substituting a less-validated model for a dominant term, not because the term is beyond
reach.

**One mechanism was omitted, and including it makes the case better rather than worse.**
The incidences above are geometric: the angle between the body axis and the velocity vector.
But the nose propeller's slipstream passes over the inboard part of the wing — half its area
on the light design and 63 percent on the heavy one — and inside that slipstream the air is not
moving at freestream speed or in the freestream direction. Because the wake is aligned with the
body axis, the resultant flow over the washed portion is pulled towards the body axis, and the
local incidence there is smaller than the geometric one. Folk [23] writes this as

    |V_a| = √( |V_w|² + |V_i|² + 2 |V_i| |V_w| cos α ),   α_e = arcsin( |V_i| sin α / |V_a| )

with V_w the wake speed and V_i the freestream. Taking V_w from momentum theory at the
transition thrust, and reporting both the fully developed wake (V_w = 2v) and the
not-yet-developed case (V_w = v) because this study does not determine which applies at the
wing station:

| | Geometric α | α_e, V_w = v | α_e, V_w = 2v |
|---|---:|---:|---:|
| Light, from a 5 m s⁻¹ climb | 17.5° | 6.8° | 4.2° |
| Light, from rest | 21.6° | 3.7° | 2.0° |
| Heavy, from rest | 20.5° | 7.6° | 4.6° |
| Heavy, from a climb | 5.4° | 4.7° | 4.2° |

**Half the wing is therefore not post-stall at the moment of peak incidence, on either
bracket.** It is at four to eight degrees, which is ordinary attached flow. The pitching-moment
budgets of this section were computed as though the whole wing saw the geometric incidence,
so they are conservative — and the outstanding measurement, which Section 8 keeps open, is
smaller than it appeared: it concerns the *outboard* half of the wing, the part that is not
washed. Two cautions belong with this. Folk records that the reduced-order wake model
overpredicts wake velocity above roughly 8 m s⁻¹, which places three of the four cases inside
its stated range and the fourth — the heavy design entering from a climb — outside it, where
the geometric incidence is only 5.4° in any case. And the verification of that model is
attributed there to work the present authors have not read.

**What the flight-test literature does about the same term, and what it found.** The
aerodynamic pitching moment through transition is not an item this study is alone in leaving
open. A transition-optimisation study with outdoor flight trials builds its aerodynamic model
by fitting published two-dimensional NACA 0012 lift and drag data through the incidence range,
notes that its own aerofoil "is not exactly the same" and judges the error acceptable for a
model-based controller, and carries **no pitching-moment term at all** in its equations of
motion [28]. A second study does carry one, but as a linear form
C_m = C_m0 + C_mα α + C_mδ δ used throughout the manoeuvre [29]. The practice of the field, in
other words, is a borrowed section polar and a closed loop — which is what Section 7.4 does for
lift and drag, and rather less than this section does for the moment. **The open item here is
the field's open item.**

A third study carries the term in its fullest published form, and the form is instructive. Its
equations of motion carry a nonlinear C_m(α) rather than a linear one, take the curve from a
separate published study of the same vehicle rather than generating it, and evaluate the
control-surface moment at "the sum of airspeed and slipstream speed near the quarter chord",
closing the remaining discrepancy with an adaptive neural term rather than with better
aerodynamics [42]. So the nonlinear moment does appear in this literature — borrowed, not
derived, and backed by an adaptive law. Independently, a guidance architecture for the same
manoeuvre computes an effective angle of attack from rotor wake velocity using hovering
momentum theory [43], which is the same construction Section 7.4 applies above and a more
recent statement of it than the source used there.

**The pattern across all four is the same and it is worth naming.** Every one of them obtains
the transition aerodynamics by borrowing, fitting or adapting, and none by measuring the vehicle
it flies. The measurement this paper leaves open is not one the field has made and this study
skipped.

**There is a reason nobody computes it, and it has been measured.** A small blended-wing-body
UAV was analysed by Reynolds-averaged computation and then tested in a wind tunnel at a
Reynolds number of 2.0 × 10⁶. From −6° to 10° of incidence "both the aerodynamic force values
and the variation trends are in quite good agreement"; from 10° to 26° they "show remarkable
differences between the numerical and experimental results", which the authors attribute to the
demands separated flow places on the computation [44]. The same boundary appears in the two
other sources used here: a vortex-lattice solution of this class of configuration departs from
computation above eight degrees [39], and the low-aspect-ratio flying-wing series records that
its pitch-up is a separated-flow phenomenon [20]. **Three methods of three different fidelities
fail at the same place, and the highest of them fails against measurement.** The incidences
this aircraft passes through in transition — 17.5° to 21.6° geometric — lie inside that band.

This changes what the open item is. It is not that this study declined to compute the
transition pitching moment; it is that the computation is not currently reliable for anyone at
those incidences, on this class of configuration, and the literature says so with a wind tunnel
behind it. **The item belongs to measurement, and Section 8 asks for it as measurement.** One
encouraging observation travels with it: the same tests found the blended-wing configuration to
have "soft-stall performance", which is the benign end of the range of behaviours the pitch-up
literature describes.

That second study is worth more attention, because it flight-tested the question this
configuration asks. Its authors compared their tail-sitter with and without elevons. Without
them — that is, with attitude control by propeller differential thrust alone, as here — they
report "a well-controlled attitude response during hovering and transition", but find that
manoeuvres in level flight "cause an oscillatory attitude response" with "motor saturations
observed", and conclude that the cause is "the increased aerodynamic moment but decreased motor
thrust at high-speed level flight" [29].

**That is the same structural tension this section derived from the moment budget, observed in
flight.** The tight case is not the high-incidence middle of the rotation but its end and
beyond, where speed is high: the aerodynamic moment grows as V² while propeller thrust falls.
The correspondence should not be pushed too far — their pitch propellers are the vehicle's lift
rotors, mounted on the wing with a short arm, where these are dedicated control propellers on
0.71 m frames, and their vehicle is smaller — but the mechanism is identical and it saturated a
real aircraft. **And it is not an isolated observation.** A survey of tail-sitter development records the
same outcome for a separate vehicle, the CRC-20 developed at the University of Maryland with
wind-tunnel-derived aerodynamics: its builders "were able to achieve transition to forward
flight, but they had poor control over the vehicle once in forward flight" [30]. Two
independent programmes, different vehicles, the same division — transition passed, forward
flight difficult.

That is the strongest external reason to treat the end-of-rotation budgets of
0.050 and 0.010 as the binding numbers in this section, and the strongest external argument
that a propeller-only tail-sitter needs its pitch authority checked at speed rather than at
incidence. It also says something about where a future experiment should be pointed: the
regime that has caused trouble in practice is not the one this paper spent the most effort
on.

**Two limits of this reading are worth stating.** The incidence history comes from the
point-mass trajectory of Section 7.4: it is the geometric angle between the body axis and the
velocity vector, so it is only as good as that trajectory. And the rotation rate itself varies
the local incidence along the body by ω c̄ / 2V, which is ±3.1° for the light design entered in
a climb and ±8.6° entered from rest — so at the peak-incidence instant of that second case
parts of the airframe see close to thirty degrees. Nothing here should be read as a
demonstration of transition authority.

---

# Supplementary S5 — The limitations in full

*Supplementary material to "The Architectural Cost of Hybrid VTOL: meryemAircraft, a
Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System".*

This was Section 8 of an earlier, longer version of the paper, reproduced here without
abridgement. Section 8 of the paper states the limitations that bear on the conclusions; this
material states all of them, item by item, with the break-even value of every assumption that
has one and the reasoning behind each. It ends with the list of places where these results
could most efficiently be attacked.

---

## 8.1 No experimental validation

There is no wind-tunnel testing in this work and no flight testing. Nothing in Sections 4
to 7 has been measured against an experiment.

One coefficient has been computed rather than assumed or taken from the literature: the
zero-lift drag of the wing and centre body, by a three-dimensional Reynolds-averaged
solution reported in Section 6.6. That is a calculation, not a validation — it is subject
to the turbulence-model uncertainty quantified there, which is its largest term, and it
has not been checked against measurement. Every other aerodynamic coefficient is either
taken from the literature or assumed.

## 8.2 The mass budget is bounded from below, and the bound is thinner than it looks

The reference designs are sized from an assumed mass breakdown — 30 % structure, 16 %
propulsion chain, 4 % battery, 8 % avionics, 16 % fuel, 26 % payload — and that breakdown
was, in the first version of this study, a target rather than a finding. A component
build-up has since been carried out and is reported in Section 6.7. It closes at 50 kg —
the components sum to a payload residual of 30.4 percent against the 26 percent assumed, a
margin of 2.2 kg — but it closes *conditionally*, and the conditions are worth stating as
the result rather than as a footnote to it: **the light design closes if the average
structural areal density stays at or below 1.78 kg m⁻², and if everything still outside the
model together stays below 2.2 kg.** That converts the assumption from an assertion into a
bounded claim. It does not make the claim comfortable, for three reasons.

**The margin lives in one number.** Breaking each assumption in turn to find the value at
which 13 kg of payload no longer closes gives margins of 38 to 197 percent on the
propulsion and assembly terms, and 19 percent on the shell areal density. At
1.78 kg m⁻² of skin rather than the 1.5 assumed, the payload is gone.

The 1.5 is no longer without an anchor, though the anchor is not a direct one. A doctoral
study of unmanned-aircraft sizing reports an areal density of **1.05 kg m⁻²** for the fuselage
of a small UAV built as a monolithic composite shell supported by an internal structure [50].
That is below the figure assumed here, so the assumption is conservative against it — but the
comparison is not like for like: that shell is carried by an internal structure, while the
shell here is the wing and carries flight loads directly. What the figure establishes is that
the assumed value is not outside the range small composite airframes are built to. It does not
establish that this airframe can be built to it. Every other line
could be substantially worse than assumed and the design would still close; that one line
could not.

**The build-up came in lighter than the target, which is a warning and not a
reassurance.** Its structure is 23.8 percent against the 30 assumed. The first pass of the
same build-up returned a payload fraction of 42.8 percent, and the difference between
that and the 30.4 reported is seven categories of hardware that the first pass had simply
omitted. A build-up that has already been found to be missing 3.4 kg of items may still be
missing more. What that risk costs is quantifiable, and it is exactly the margin already
stated and not an additional allowance: the contingency line can rise from the 12 percent
of dry mass used to 22 percent before the payload claim fails, which is 2.68 kg growing to
4.89 kg — a further 2.2 kg of unaccounted mass, and no more. An earlier version of this
section quoted 4.5 kg by reading the break-even contingency as if it were additional to
the budget rather than inclusive of what is already in it. The two figures were never
independent: the survivable unaccounted mass and the payload margin are the same 2.2 kg,
counted once.

The four categories most often missing from a build-up of this kind were checked
explicitly and are present: propeller blades and coaxial hubs, power electronics sized on
hover peak rather than on engine rating, fuel containment as distinct from fuel, and
control actuation — the last being small here only because the configuration has no control
surfaces to actuate. What is *not* separately modelled is local load introduction: the
tip-frame roots, the nose motor mount, and the payload, fuel and battery supports are
carried inside the shell and internal-structure allowances rather than sized. If those load
paths cost more than the allowances contain, they come out of the same 2.2 kg.

**Paper aircraft are habitually lighter than the aircraft that eventually get built**, and
the payload fraction remains the number most exposed to that, because payload is the
residual and absorbs the entire error of every other line. This is still the single most
likely place for the results of this paper to be wrong, and it remains the reason
Section 6.5 declines to compare the calculated payload fractions against the published
figures of aircraft that exist.

One structural question is narrowed by the build-up rather than settled. At 50 kg the root
bending moment is 934 N·m, which a carbon spar cap of 10.7 mm² carries at the design
allowable; the caps weigh 41 grams, eight parts in ten thousand of take-off mass, and under
one percent even at 1000 kg. **Global span bending is therefore not the sizing driver in
this model** — which is why the twenty-five percent thick centre body costs nothing in
bending. That is the whole of the claim. Buckling, core shear, torsion, local load
introduction at the tip-frame roots and the nose mount, minimum manufacturing gauge,
damage tolerance and aeroelastic margin are outside the model, and an earlier version of
this section over-read the 41 grams as showing that strength in general is not the driver.
It does not. Those modes are carried, if at all, inside the shell areal density and the
internal-structure allowance — which is a further reason the shell figure is the number
this budget stands or falls on.

## 8.3 Geometry chosen rather than derived

The sweep distribution — 45° at the root falling to 38.3° at the tip on the leading edge,
with the trailing edge constant at 25° — was selected from a 20°–40° band reported
favourable in the transonic-transport literature. The present aircraft is subsonic. The
band has not been re-derived for this flight regime, and the values are therefore design
choices supported by precedent rather than results. The realised sweep variation is
under seven degrees, which is smaller than the crescent-wing precedent of Section 2.3
would suggest; the planform inherits the *principle* of a coupled sweep–chord–thickness
distribution, not the magnitude of the original.

The taper distribution has likewise not been optimised, and the aerofoil sections are
described by thickness, camber and reflex distributions rather than by specific
sections.

## 8.4 Coefficients taken from the literature

Several results depend on coefficients that were not computed for this geometry:

- The **roll authority** of the lower-surface strip. Section 4.4 now computes the two
  halves of this that can be computed for this geometry — the roll inertia, 25.0 kg·m²,
  and the roll damping, |C_l_p| = 0.358 from a vortex-lattice solution rather than from
  the literature — and inverts the question: twenty degrees per second at cruise requires
  27.1 N·m. What remains from the literature is the strip's own effectiveness, and it is
  the load-bearing part. The strip's own force as a swept fence supplies about a third of
  the required moment; the moment must therefore come from the change in the half-wing's
  circulation, which asks for ΔC_L ≈ 0.12 over the strip's span. Published wind-tunnel data
  for a two-percent-chord device over the same inboard two-thirds of span report increments
  of 0.14 to 0.17 [18], so the requirement is below what a comparable device delivers — but
  that device is a trailing-edge flap on an unswept wing, and **roll authority remains sized
  and not closed.** The same comparison shows the strip's height law to be wrong outboard,
  reaching 13.7 percent of local chord where the mechanism saturates near two; Section 4.4
  records this as a change the configuration needs. An earlier version of this
  paper quoted 46 N·m without stating the mechanism it came from; that number implies
  ΔC_L ≈ 0.20 and is not reproduced here as an authority.
- The **directional stability** of the configuration. Section 4.4 computes C_n_β = 0 for
  the planform — the wing supplies none, which measured data on tailless aircraft confirm is
  normal rather than unusual [19,20] — and shows that the tip-frame fairing must supply it, at
  a chord well inside what the fairing needs for drag reasons. Two items are added by that
  literature and closed by neither it nor this paper: the fairing needs a **toe angle**, whose
  sign follows from its aspect ratio and which brings a stall-related failure mode with it;
  and the fin's **drag** contributes to directional stability at an arm of half the span, a
  mechanism the estimate here omits and which makes it conservative. The fin contribution
  itself is **not computed**, and neither is the yaw damping it would bring; the
  profile-drag damping of the bare planform, C_n_r = −0.0023, is negligible. Yaw authority
  is not in question — the yaw arm is the semi-span, so the available moment is 2.4 times
  the pitch moment — but directional stability and yaw damping are a single open item
  resting on a component whose section has not been selected.
- The **battery buffer's specific power**, which Section 6.7 now identifies as the most
  exposed number in the mass budget. Taken at the electrical bus, where the buffer is, it asks
  for **5.63 kW kg⁻¹** to hover and 6.48 to leave the ground, where the only figures this study
  has read give 0.7 to 1.3 kW kg⁻¹ at pack level for power-application Li-ion [21]. At the top
  of that range the buffer would mass 7.8 kg instead of 1.8 and **the light design's budget
  would not close**. The assumption is that a purpose-built short-duration buffer beats an
  automotive traction pack by four to nine times; that is plausible in kind and
  unverified in magnitude, and Bill 3 rests on it. The energy side does *not* compound it: the buffer
  discharges through a take-off of ten to twenty seconds rather than continuously, and even a
  low-energy high-power cell would use only a third of its capacity doing so. Power is the
  binding currency, and a shortfall in it is a floor rather than a transient — thrust goes as
  power to the two-thirds, so a buffer at 1.3 kW kg⁻¹ gives a thrust-to-weight ratio of 0.71
  and the aircraft does not leave the ground.
- The **cruise state of the tip rotors.** Section 5.2 shows that they must turn freely at
  zero shaft load rather than stop, on pain of adding 61 to 74 percent to the zero-lift drag,
  and that fixed pitch removes feathering as a third option. The estimate behind that is an
  area-and-coefficient calculation with assumed solidity and section drag coefficients, not a
  propeller calculation; what is robust is the ratio between the states, not the values. It
  also converts a seized tip-rotor bearing from a control failure into a drag failure, and no
  reliability analysis of that is offered here.
- The **three-axis coupling of the roll strip**, none of which was previously stated.
  Deploying it on one side produces adverse yaw of 2.9 to 11.3 N·m depending on the height
  law, against 42.8 to 55.9 N·m of yaw authority — covered. It also produces a nose-down
  pitching moment, measured for this class of device [33] and bracketed here at ΔC_m of 0.005
  to 0.032 against a tightest budget of 0.050 — **not comfortably covered at the upper end**,
  which yields a scheduling restriction rather than a redesign. Both estimates carry the same
  unselected-cross-section caveat as the frames, and the chordwise position of the lift
  increment, which sets the pitch coupling, is not computed anywhere in this paper.
- **Turbulence and post-stall degradation of the strip.** The mechanism the roll requirement
  depends on is reported to weaken past the stall angle and to become negligible at 19 percent
  inflow turbulence [35]. The strip's inboard portion sits in a propeller slipstream and the
  transition passes through post-stall incidence, so both conditions are met somewhere in the
  flight envelope. The cited measurements are on a different aerofoil in grid turbulence and
  transfer only in direction; no measurement of this strip in a slipstream exists. **This is
  the principal risk to hover roll authority**, and it sits on the same claim — slipstream
  placement — that Section 4.4 offers as an advantage. The post-stall half of this item is
  contested rather than established: a simulation at twenty degrees of incidence returns a
  ninety-four percent lift increase from a flap of the same height fraction at essentially
  unchanged drag [37]. The turbulence half is unopposed. Against both, a water-tunnel study at
  a Reynolds number of 8 588 found the mechanism qualitatively unchanged four orders of
  magnitude below the usual test range [38], which is evidence that low speed as such is not
  the threat — turbulence is.
- The **roll actuator.** The strip extends by a commanded amount, so the limit cycle computed
  in Section 4.4 — ±0.2° in bank at a fifty-millisecond deployment, ±9.4° at a hundred and
  fifty — bounds the two-position worst case rather than describing normal operation. What is
  not stated anywhere is the actuator's mass, its power draw or its bandwidth, and no
  closed-loop stability analysis has been carried out.
- The **frame drag** of Section 5.2 uses C_D values representative of circular and faired
  sections at the relevant Reynolds number. **The frame cross-section has not been
  selected.** The conclusion that the frames must be faired is robust — the difference
  between C_D = 1.15 and C_D = 0.15 is not a matter of coefficient precision — but the
  twelve-percent figure is an estimate.
- The **zero-lift drag coefficient** of 0.0248 is assumed rather than adopted from a
  build-up. Section 6.6 reports a component build-up that brackets it at 0.0131 to
  0.0210, so the assumed value is conservative. That build-up had a weak link in its
  largest term — its strip method treated the root section as a two-dimensional aerofoil
  of twenty-five percent thickness, and the flow over the centre body of a blended-wing
  body is not two-dimensional. **That link has since been replaced** by a
  three-dimensional solution, also reported in Section 6.6, which brackets the
  wing-and-body term between 0.0120 and 0.0148 depending on the turbulence closure and on
  the starting field, and the total between 0.0201 and 0.0231 — still below the assumed
  value in every case. What remains uncertain is no longer the dimensionality but, first,
  the transition state — the solution is fully turbulent, and the clean-surface case is
  still the strip estimate — and, second, the uniqueness of the solution itself, since the
  wall-resolved SST case settles four percent apart from two different starting fields.
  The build-up is reported as a bound on the assumption rather than as a replacement for
  it.
- **Span efficiency** is assumed at 0.85, and the assumption is now bounded by a calculation
  rather than by a borrowed rule. A vortex-lattice solution gives an inviscid span efficiency
  of 0.99 for the untwisted planform and 0.859 for the wing twisted to trim. Section 6.6
  computes the corresponding Oswald-type values by calling a section solver at each spanwise
  station's own local lift coefficient: **0.931 untwisted and 0.817 trimmed**, a viscous ratio
  of 0.94 to 0.95. The assumed 0.85 is therefore **optimistic by 3.9 percent**, worth 1.4
  percent of cruise lift-to-drag ratio and of the range figures of Section 6.3. What the
  calculation does not settle: its sections are symmetric, so it is a lower bound rather than an
  estimate; it ignores sweep, and the root sweep is 45°; and it inherits whatever magnitude
  error the vortex-lattice solution carries on a configuration of this class, which Section 6.6
  reports as untested and bounded above by a published comparison.

## 8.5 Torque balance holds at one point only

The propeller pairs are of fixed geometry, so exact torque cancellation occurs at one
operating condition. That condition was chosen to be cruise, on the grounds that cruise
is long and strategic while hover is short and tactical. A small residual torque
therefore remains in hover. It is trimmed by the same lower-surface strip that provides
roll in cruise, but the trim authority required has not been computed.

## 8.6 The transition simulation is a point mass

The results of Section 7.4 come from a two-degree-of-freedom point-mass simulation in
which the body angle is driven kinematically. It therefore does **not** model rotational
dynamics, and the tip-propeller thrust required to produce the rotation does not follow
from it. Section 7.6 supplies part of what is missing — the inertia about the rotation
axis, the peak angular acceleration a finite moment can actually produce, and the resulting
margin — but only part: the aerodynamic pitching moment through ninety degrees of incidence
is still absent, so what that section establishes is a necessary condition and not a
sufficient one. It also records that the linear angle ramp used in Section 7.4 cannot be
produced by any finite moment, and reports the measured sensitivity of the altitude-loss
tables to that choice.

**One published number changed as a result.** The heavy reference design's rotation time
was four seconds, at which — against the corrected inertia of Section 7.6 — the margins are
0.97 on the cheapest profile and 0.65 on a smooth one, that is, infeasible on both. It is
now 5.1 s, the time at which the heavy design holds the light design's margins, and the
change costs nothing: the tip-propeller power falls from thirteen percent of hover power to
six, and the altitude-loss result is unchanged. The light design is on the same boundary
rather than clear of it: two seconds against a smooth minimum of 2.01 s. Both reference
rotation times should be read as actuator-limited lower bounds. The aerodynamic model is a linear lift curve to stall with a flat-plate relation
beyond it; dynamic stall, separation hysteresis and propeller-wake effects on the wing
are absent.

The qualitative conclusion — that a slower rotation loses less altitude, and that
entering the rotation while climbing removes the loss entirely — depends on the sign of
the vertical support term rather than on the details of the aerodynamic model, and is
robust. The specific altitude figures are not.

That robustness has since been tested rather than asserted. The simulation takes its
lift-curve slope from the thin-aerofoil expression, 4.72 rad⁻¹; the vortex-lattice
solution of Section 6.6 gives 3.87 rad⁻¹ for this planform — eighteen percent lower, and
in the direction that would make the aircraft fall further. Repeating both tables with
the lower value moves no published entry by more than 1.2 m, and the two reference
profiles — two seconds for the light design, 5.1 for the heavy, entered at 5 m s⁻¹ of
climb — still lose no altitude at either slope. The conclusion of Section 7.4 survives an
eighteen-percent error in the coefficient it rests on.

## 8.7 The tip-surface benefit is not quantified

The tip frames extend perpendicular to the planform by 0.41 of the semi-span, which is
four to eight times the relative height of a conventional winglet. Giving their fairings
a lifting section rather than a symmetric one costs no additional part, mass or
mechanism, and induced drag is 33.7 % of cruise drag at the reference condition, so the
mechanism has something to act on.

No number is claimed for it. The surface is far outside the geometric range for which
textbook winglet relations were established, and estimating the benefit properly
requires a panel method or CFD. The associated costs — increased root bending moment,
and increased directional stability that the tip propellers must overcome to command yaw
— have likewise not been quantified.

## 8.8 Disturbance rejection in hover

With the transition no longer sizing the tip propellers, hover disturbance rejection
becomes the sizing case. Only an order-of-magnitude check has been made against a
single gust condition. The disturbance spectrum, the closed-loop bandwidth required, and
the actuator response needed to achieve it have not been analysed.

## 8.9 Ground handling and crosswind

No claim is made that the aircraft resists tipping in arbitrary ground wind, and the
historical record gives a specific reason not to make one: the contemporary assessment of
the XFY-1 quoted in Section 2.2 records "tip-over tendencies noted when on ground in
gusty air" [1]. This is a property of standing an aircraft on its tail and it is
inherited here. The stance
base is a design parameter that can be widened without altering the configuration, and
the reference geometry represents one point on that trade rather than a limit. Operating
limits in ground wind are an operational matter, and published data for this class shows
that such limits are ordinary rather than exceptional: a fielded fixed-wing VTOL
uncrewed aircraft in the same mass range quotes a wind limit of 15 knots for take-off
and landing against 25 knots in cruise [8]. A lower ground-wind limit than cruise limit is
the normal condition for VTOL aircraft, not a defect peculiar to tail-sitters. The
specific limits for this configuration have not been computed here.

## 8.10 Vertical descent

The vertical descent has not been analysed. A rotor descending into its own wake can
enter the vortex ring state, in which thrust becomes erratic and additional power is
counterproductive. Whether and at what descent rate this configuration encounters that
region is an open question and one of the more important items of future work, because
it bears directly on the landing phase.

## 8.11 Prior art

The novelty claimed in this paper is a combination, and the elements of that combination
individually have antecedents. Blended-wing bodies, tail-sitters, coaxial
counter-rotating pairs, series-hybrid powertrains and attitude control by differential
thrust have all appeared before, separately and in various partial groupings. In
particular, full attitude control of a tail-sitter with no control surfaces at all has
been demonstrated and published; that aircraft differs from the present configuration in
its planform, in distributing thrust across the span, and — decisively — in taking its
rolling moment from the differential reaction torque that the coaxial arrangement here
removes by design.

The literature underpinning Sections 2 and 3 was read at first hand where the sources
could be obtained. Seven were: the two NASA reviews of United States V/STOL development
on which Section 2.2 rests [1,2], the doctoral study from which the drag measurements of
Section 3.3 are taken [3], the QuadPlane wind-tunnel characterisation [4], the
stationary-lift-propeller drag study [5], the concept-vehicle sizing study quoted in
Section 3.2 [6], and the tail-sitter flight-test paper cited in Sections 3.4 and 4.4 [7].
Three further sources were sought and not obtained — the journal version of [3], an
earlier conference paper by the authors of [7], and a 2025 forum paper on stopped-rotor
drag — and none of them is relied upon for any claim here; where a claim had rested on
the last of these, it was removed rather than retained on a summary. No patent claim text
was read in the original; the prior-art position stated here is that of an author survey,
not of a professional search.

## 8.12 The architecture comparison is conditional, and on two things rather than one

The comparative sizing of Section 5.5 settles the case against a separate lift system
using measurements, and does not settle the case against a tilting mechanism at all. Two
separate conditions carry that second result and both should be read as limitations.

The first is an unmeasured number. The tilting layout is credited with paying no cruise
drag for its nacelles, pivots and hover-pitched blades, because no measurement of that
penalty was available to charge it with; on that credit it cruises twelve percent further
than the configuration proposed here under the fixed-fuel-fraction rule. The sign of that
comparison reverses if the penalty exceeds roughly eleven percent of cruise drag, which is
what the tip frames of this configuration cost it. The reader should treat the tilting
column as an upper bound on that architecture rather than as an estimate of it.

The second is the sizing rule itself, and it applies symmetrically to every architecture
including the one proposed here. Range as computed from a fixed fuel fraction does not
depend on take-off mass, so an architecture that closes heavier is permitted to carry
proportionally more fuel and its mass penalty never reaches the range column. This is a
correct property of the Breguet form and not an error, but it is a poor contract for
comparing architectures, and a comparison reported under it alone would be misleading.
Section 5.5 therefore reports three contracts — fixed fuel fraction, fixed fuel mass, and
fixed take-off mass with fixed payload — and the tilting layout's advantage survives only
the first. Which of the three is the right question depends on what is being procured: a
fixed mission, a fixed fuel load, or a fixed vehicle class. This paper does not choose
among them, and no result here should be quoted without the contract it was computed
under.

Three further caveats sit under the same model. Wing loading and disc loading are held
common across the three architectures, which is a controlled comparison and not a
statement that each is at its own optimum. The structural fraction is likewise common,
which is generous to the distributed-lift layout, since carrying power to the extremities
is generally held to carry a structural penalty of its own; charging it makes that layout
heavier without changing its range, so the direction of the result is unaffected. And the
second table in that section, which gives each architecture its own unbuffered power
system, is a bounding case rather than a fair comparison, for the reason given there.

## 8.13 The engine rating margin is not consistent between the two reference designs

The sizing model of Section 5.5, calibrated entirely on the light reference design,
predicts the heavy one to within four percent in take-off mass and one tenth of a percent
in range without a single coefficient being changed. One term does not carry across. The
engine is rated at 2.6 kW against 1.7 kW of cruise electrical power in the light design,
a margin of 1.53, and at 54.3 kW against 39.2 kW in the heavy one, a margin of 1.385 —
ten percent apart, and nowhere justified in this paper. Carrying the light margin through
to the heavy design overstates its engine by seventeen percent while leaving range and
lift-to-drag ratio untouched. A larger generator and power electronics being relatively
more efficient is a defensible reason for the difference, but it is a reason supplied
after the fact; as the two designs stand, the margin is an undeclared choice rather than
a scaling law, and the scale-invariance claimed in Section 6.4 should be read as holding
for the mass and range fractions and not for this one.

## 8.14 The strip's authority does not start at zero

Extension is the control variable, but a device of this kind produces no lift change until it
projects about one percent of the local chord [19]. The strip is tapered, so the threshold is
crossed progressively from the outboard end inward: it is wholly inert below seven percent of
commanded travel, and above a quarter of travel the response is linear to within five percent.
The intervening band is genuinely nonlinear and is not modelled anywhere in this paper. The
consequence is confined to small corrections rather than to large ones, but a closed-loop
design would have to carry it, and no closed-loop design is attempted here.

A second, larger omission sits beside it. The strip projects from one surface only, and the
pitching moment that arrangement produces was described in the older literature as
"prohibitive" for spoilers used as ailerons, with projection from both surfaces named as the
remedy [19]. Section 4.4 resolves the coupling by restricting when the strip may be commanded.
The alternative resolution — a strip that projects from both surfaces, so that the pitching
contributions oppose and the rolling contributions add — has not been examined, costed or
ruled out.

## 8.15 The directional-stability estimate omits the body, and the sign of the omission is known

The vortex-lattice model used for C_n_β has no volume. The centre body of a blended wing
develops side force in sideslip ahead of the centre of gravity and is therefore destabilising,
and on tailless aircraft that contribution is reported to be "at least as great as the
stabilising effects contributed by the wing alone" [19]. The planform contributes zero here, so
that statement yields no magnitude — only a direction. The fairing sized in Section 4.4 is
sized to bring a zero up to criterion; the real starting point is below zero, and the shortfall
is unquantified.

The same section's fairing rests on an assumed lift-curve slope of 4 per radian at a chord
Reynolds number near 80,000. Symmetric sections at low Reynolds number are measured to be
nonlinear about zero incidence, in one case reversing the sign of the lift-curve slope over a
three-degree band [36] — the same band a toe angle of one to two degrees occupies. Whether a
fairing of that chord develops the side force credited to it is not established.

## 8.16 The toe-out arrangement has a failure mode at large sideslip

The frames' aspect ratio requires toe-out (Section 4.4). Toe-out carries a known hazard: yawing
far enough to stall the rear fin produces a large *destabilising* yawing moment, where the same
stall on a toed-in fin produces a stabilising one [19]. The sideslip angle at which that occurs
sets an upper bound on the usable sideslip envelope, and it has not been computed. It depends
on the fairing's section and Reynolds number, neither of which is fixed here.

## 8.17 What would change these conclusions

The results of this paper would be most efficiently attacked in six places, and they
are listed so that they can be:

1. ~~**A three-dimensional solution for the centre body.**~~ **Done.** This was the
   first place to attack, because the strip method of Section 6.6 could not model the flow
   over a twenty-five percent thick blended centre body. The solution has since been
   carried out and is reported in Section 6.6: it gives a wing-and-body C_D0 of 0.01475
   with the Spalart–Allmaras closure and 0.01201 – 0.01253 with k-ω SST — a spread of
   eighteen percent between the closures that nothing in the solutions resolves — and it
   leaves the assumed 0.0248 conservative in every case. The dominant term is the
   turbulence model, and it is larger than first reported because the two models were
   subsequently paired at the same wall resolution rather than at two different ones.
   **What it does not settle** is, first, the transition state — the solution is fully
   turbulent, so the clean-surface figure of 0.0073 is untested and the gap between it and
   0.0120–0.0148 is now the largest single uncertainty in the zero-lift drag, larger than
   the spread between the closures. A transition-sensitive model requires a wall-resolved
   grid and a two-equation formulation at once; that combination now converges, but the
   model could not be validated in the low-turbulence regime the cruise condition sits in.
   **Second, and newly opened, is the uniqueness of the wall-resolved solution itself.**
   That case cannot be started from a uniform field, and the two starts that do converge —
   one warmed from the Spalart–Allmaras solution, one mapped from the coarser SST solution
   — settle 4.3 percent apart, entirely in the pressure component. Steady RANS is
   admitting more than one stationary solution here. **This item is therefore narrowed
   rather than closed**, and what replaces it is stated above.
2. ~~**A structural mass estimate** for the airframe and the tip frames.~~ **Attempted;
   conditional at 50 kg, open at 1000 kg.** The build-up of Section 6.7 meets the 50 kg
   payload fraction with 2.2 kg in hand, on the condition that the shell areal density does
   not exceed 1.78 kg m⁻² and that everything still outside the model together stays under
   that same 2.2 kg. **What it does not settle** is either of those conditions, or how the
   areal density scales: the 1000 kg design is at break-even when it grows as the 0.467
   power of linear scale, and that exponent was not measured. The build-up also does not
   contain buckling, torsion, local load introduction or aeroelastic sizing, and its tip
   frames were sized for a vertical landing only. **This item is therefore narrowed rather
   than closed**, and what a fuller version of it would have to bound is now specific.
3. **A six-degree-of-freedom transition simulation** with rotational dynamics. **Partly
   done, and the remainder is blocked on data rather than on effort.** Section 7.6 derives
   the inertia from the component build-up and shows the tip propellers carry it with a
   margin of 1.49 at the light design point and 1.57 at the heavy one on the cheapest
   rotation profile, and of 0.99 and 1.05 on a smooth one — that is, at the actuator limit
   rather than clear of it — together with a measured account of how that margin
   narrows with size, and a threshold for the aerodynamic moment resolved along the
   trajectory. That resolution corrected the requirement rather than merely quantifying it:
   the aircraft does not reach ninety degrees of incidence, because the relative wind
   rotates with the body, and peak incidence is 17.5° to 21.6°. **Transition controllability
   remains the largest unresolved item in this study**, but it now asks for the pitching
   moment up to some twenty-two degrees at low dynamic pressure and for trim at cruise
   incidence, rather than for a moment sweep through ninety degrees — and Section 7.6 narrows
   it once more, since the inboard half of the wing lies in the nose propeller's slipstream and
   sees an effective incidence of four to eight degrees rather than the geometric seventeen to
   twenty-two [23]. The measurement that is still owed concerns the *outboard* half. Two further
   things are now known about this item. It is **the field's open item, not this study's
   alone**: published transition analyses with flight trials carry either no pitching-moment
   term or a linear one, and close the loop with a controller instead [28,29]. And a
   flight-tested tail-sitter controlled by differential propeller thrust alone, with no elevons,
   was well behaved through hover and transition but saturated its motors during manoeuvres in
   **level flight**, its authors attributing this to aerodynamic moment growing with speed while
   thrust falls [29]. **The binding condition for a propeller-only tail-sitter is therefore
   pitch authority at speed, not at incidence** — which is where the tightest budgets of
   Section 7.6, 0.050 and 0.010, already sit. What is still not done
   is answering it: a reduced computation would replace a dominant term with a
   less-validated model. What it cannot do is charge the
   aerodynamic pitching moment, which requires moment coefficients through ninety degrees
   of incidence; those are not available for this planform and cannot be produced without
   a wind tunnel or a dedicated computational campaign. **This item is therefore reduced
   to a specific missing measurement rather than a missing analysis.**
4. **A panel-method analysis of the tip surfaces**, which would either convert Section
   8.7 into a quantified benefit or remove it. The vortex-lattice solution of Section 6.6
   covers the planform but not the tip surfaces, which remain unquantified.
5. ~~**A viscous solution of the twisted planform, section by station.**~~ **Done.** The
   Oswald-type efficiency the drag build-up needs was obtained from the inviscid figure by a
   borrowed ratio. It is now computed on this planform by the method the non-linear
   vortex-lattice literature uses — two-dimensional viscous analyses at each spanwise station
   coupled to the three-dimensional circulation [40] — and reported in Section 6.6. The
   borrowed ratio of 0.85 to 0.90 was too pessimistic; the computed ratio is 0.94 to 0.95. The
   conclusion nevertheless stands in the unfavourable direction, because the trimmed wing
   starts from a lower inviscid figure: the Oswald efficiency is **0.817 against the assumed
   0.85**, worth 1.4 percent of cruise lift-to-drag ratio. **What it does not settle** is,
   first, that the sections used are symmetric, so the figure is a lower bound rather than an
   estimate; second, that strip integration ignores sweep, and the root sweep is 45°; and
   third, that it does nothing about the magnitude question of item 6 below, since it is built
   on the same vortex-lattice loading. **This item is therefore closed as to the ratio and
   open as to the absolute level.**
6. **A Reynolds-averaged or panel solution of this planform's loading**, to bound the
   magnitude error the vortex-lattice results carry. A published comparison on a
   blended-wing-body of this class found the vortex-lattice lift coefficient low by thirty to
   thirty-eight percent against RANS [39]. Section 6.6 argues that a near-constant
   multiplicative error of that kind cancels in the ratios this paper takes from the solution,
   but the check that would confirm it — whether the moment scales with the lift by the same
   factor — is withheld in that source. This is the one exposure in the aerodynamic chain with
   no bound at all.

**Not all of these are within reach of a calculation, and an earlier version of this list said
they were.** The first has been carried out and its result is folded into Section 6.6, and so is
the fifth. Of the remainder, the transition pitching moment is blocked on data rather than on
effort, for the reason item 3 gives — three methods of three fidelities fail above roughly ten
degrees of incidence — and the fin derivative of Section 8.15 is blocked the same way, because
what the low-Reynolds-number measurements remove is the linearity of the curve a calculation
would have to assume. Those two need a tunnel. The rest are within reach of a follow-on study,
and the configuration is described in enough detail in Section 4 and Section 6 for another
group to attempt any of them independently. The computational setup, the grid-convergence
study and the record of what failed along the way are in the repository, so the first
item can be re-run and checked rather than taken on trust.

---

# Supplementary S6 — The three bills stated formally, and a comparative sizing

*Supplementary material to "The Architectural Cost of Hybrid VTOL: meryemAircraft, a
Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System".*

This material was Sections 3.7 and 5.5 of an earlier, longer version of the paper. The first
states the three bills as equations with the transfer table showing that they are one quantity
in three currencies; the second sizes three architectures against the same mission under three
different sizing contracts, all twelve cells, with the sensitivity sweeps.

---

## S6.1 The three bills stated formally, and a test of the statement

The argument so far has been verbal. It is worth stating compactly, because the compact form
makes clear what the framework claims and what it does not.

For an architecture *a* flying a given mission, write the three charges as fractions of the
quantity each degrades:

$$f_1(a) = \frac{m_\text{hover-only}(a)}{\mathrm{MTOW}}, \qquad
f_2(a) = 1 - \frac{(L/D)_a}{(L/D)_\text{clean}}, \qquad
f_3(a) = \frac{P_\text{cont}(a) - P_\text{cruise}}{\sigma_P\,\mathrm{MTOW}}$$

where *m*<sub>hover-only</sub> is the mass that exists solely to hover, (L/D)<sub>clean</sub>
is the lift-to-drag ratio the airframe would have with no hover hardware exposed,
*P*<sub>cont</sub> is the continuously installed power, and σ<sub>P</sub> is the specific
power of the power system. Each is dimensionless, each is zero for an aircraft that does not
hover, and each is measurable for one that does.

**The claim of Section 3.6 is that the same architectural choice need not minimise all
three simultaneously.** The architectural moves available typically move cost between them
rather than removing it: retracting
the lift rotors reduces *f*₂ and raises *f*₁ by the retraction mechanism; tilting the
propulsors reduces *f*₁ and *f*₂ together and introduces a mechanism whose mass and failure
modes are the price; buffering the hover peak reduces *f*₃ and raises *f*₁ by the buffer.
Section 3.4 tabulates these transfers. The escape condition is the statement that all three
vanish simultaneously only when the hover and cruise hardware are the same hardware, in the
same orientation, doing the same job, with the peak supplied from a buffer.

**A consequence that can be checked against published work.** If the three are genuinely
separate currencies rather than three names for one quantity, then an architecture may be
*best* in one and *worst* in another — in particular, the architecture with the highest
cruise lift-to-drag ratio need not be the lightest. A single-metric comparison would not
anticipate that. The NASA sizing study quoted in Section 3.2 reports exactly this pattern:
the lift-plus-cruise concepts are the heaviest of the four examined *while having the highest
cruise efficiency of that group*, and the authors attribute the weight to hardware carried for
hover rather than to cruise power. That is *f*₁ dominating while *f*₂ is favourable, which is
the framework's prediction and not a restatement of it. The later and larger version of the
same programme states the transfer in a single sentence: "the high cruise efficiency of the
lift+cruise type reduces the battery weight compared to the quadrotor, but not enough to
counter the increase in structure and propulsion weight, so the all-electric lift+cruise
aircraft is the heaviest design" [22]. A gain in one currency, insufficient against a loss in
another, named as such by authors with no framework to defend.

**That later study also contains the case that would embarrass the framework if it behaved
differently, and it does not.** Sizing five architectures rather than four to the same mission
adds a tiltwing, and the tiltwing has the highest cruise efficiency of all of them:

| Concept | L/D_e | Design gross weight, lb |
|---|---:|---:|
| Quadrotor, turboshaft | 4.9 | 3 678 |
| Quiet single main rotor, turboshaft | 5.4 | 3 951 |
| Side-by-side, electric | 7.2 | 5 547 |
| Lift + cruise, electric | 7.9 | 9 482 |
| Lift + cruise, turbo-electric | 8.5 | 7 271 |
| **Tiltwing, turbo-electric** | **8.6** | **6 584** |

The tiltwing is best in cruise efficiency *and* lighter than either lift-plus-cruise concept.
A framework that predicted "best in cruise implies heaviest" would be refuted by this row. The
framework here predicts no such thing: it says the tiltwing satisfies most of the escape
condition, because the same propulsors serve hover and cruise and nothing is left exposed, and
that it pays instead for the mechanism that rotates them. That is precisely the trade
Section 5.5 finds when it sizes a tilting layout itself, and it is why no claim of superiority
over the tilting family is made anywhere in this paper.

The comparison of Section 5.5 shows the same pattern on a different set of architectures:
of the three sized there, the tilting layout has the best cruise lift-to-drag ratio — 13.44
against 12.00 — and is nonetheless twenty percent heavier than the tail-sitter, because it
carries a tilt mechanism that the tail-sitter does not. Best in *f*₂, worse in *f*₁. **That
comparison is an illustration and not evidence, and the distinction matters here.** Its
tilting layout is given a cruise-drag multiplier of 1.00 — that is, its mechanism is
credited as aerodynamically free — precisely to make the *f*₂ advantage as large as the
architecture could possibly claim. A comparison whose inputs were chosen by the present
authors cannot corroborate the present authors' framework. **The evidential weight rests on
work done by others**, whose numbers were produced for other purposes and are not ours to
choose; Section 5.5 shows what the framework looks like when applied, not that it is right.

**A second independent check exists, and it is on aircraft that were built rather than sized.**
Bacchini and Cestino compare three flying eVTOLs — one per architecture — on five parameters
[21]:

| | E-Hang 184 (multirotor) | Cora (lift + cruise) | Lilium (vectored thrust) |
|---|---:|---:|---:|
| Disc loading, N m⁻² | **440** | 880 | 7500 |
| Total hover time, min | **20.5** | 16.5 | 12.1 |
| Cruise speed, km h⁻¹ | 100 | 180 | **252** |
| Practical range, km | 42 | 107 | **203** |

The ranking reverses completely between the hover rows and the cruise rows. The architecture
best in hover is worst in cruise and the architecture best in cruise is worst in hover, with
the lift-plus-cruise layout between them on every line — which is what it means for the
currencies to be separate rather than three names for one quantity. Those authors also state
two of the three transfers in their own words, without any framework to state them in. Of the
lift-plus-cruise aircraft: its "parasitic drag caused by the pylons and vertical thrust
propellers increases the power required in cruise" — that is *f*₂. And of the vectored-thrust
aircraft, whose cruise efficiency is the best of the three: its hover "is so power demanding
that it requires batteries with higher specific power" than those assumed, so that "the
aerodynamic advantages of this configuration are balanced by higher demands on the batteries
and on the power electronics" — that is *f*₂ bought and *f*₃ paid, named as an exchange by an
author who was not looking for one.

None of these comparisons validates the framework. All are external consistency checks: the NASA
study was carried out for other purposes and its numbers were not chosen to suit the
argument here, and a framework that predicted the opposite ordering would be in difficulty
against them. The Bacchini and Cestino comparison is weaker as evidence in one specific way
and stronger in another: weaker because its three aircraft differ in mass, mission and
technical maturity as well as in architecture, so it does not isolate the mechanism the way a
controlled sizing study does; stronger because they exist, and their numbers are not the
output of anyone's sizing loop. Corroboration of this kind raises confidence that the three charges are
separable in practice; it does not establish that they are the only three, and nothing
short of a broad survey of sized architectures could.

**What the framework does not claim.** It does not predict the magnitude of any bill for an
architecture that has not been sized; the fractions above must be computed or measured case
by case. Nor does it claim that these are the only architectural costs a VTOL aircraft carries:
control authority, thermal management, transition hardware, reliability and certification are
all real and none of them is one of these three. What it provides is narrower and, because it is
narrower, defensible — that these three recurring charges follow from the duty-cycle mismatch of
Section 3.1, that they are the currencies in which the architectural remedies surveyed in
Section 3.5 trade against one another, and that there is a stateable condition under which none
of the three is charged.



---

## S6.2 A comparative sizing of three architectures

Sections 5.1 to 5.4 argue that a particular configuration declines a particular trade.
That argument is made against the general statement of the tax in Section 3, not against
any competing aircraft, and an argument of that shape has a known weakness: it can be
right about the mechanism and still be wrong about the outcome, because a rival
architecture may pay the bills and recover more than it pays. The claim is therefore
tested here by sizing the same mission three ways.

**Method.** One set of equations is used for all three, and they are the equations of
Section 6.1 — closed-loop mass, hover power from momentum theory, and a Breguet-type
range:

$$\mathrm{MTOW} = \frac{m_\text{payload}}{1 - f_\text{empty} - f_\text{fuel}}, \qquad
P_\text{hover} = \frac{W^{3/2}}{\eta_h \sqrt{2\rho A}}, \qquad
R = \frac{f_\text{fuel}\, E^{*} \eta_\text{chain}}{g}\,\frac{L}{D}$$

The propulsion-chain mass is not a fixed fraction. It is split into a part proportional
to take-off mass and a part proportional to installed power, because a fixed fraction
would make the third bill invisible by construction. Installed power depends on take-off
mass and take-off mass depends on installed power, so the system is closed by fixed-point
iteration.

**Calibration.** Every coefficient is back-solved from the light reference design of
Section 6.2 rather than assumed: a hover figure of merit of 0.599 from 10.9 kW at 50 kg,
a cruise propulsive efficiency of 0.721 from 1.7 kW at L/D 12, an engine rating margin of
1.53, and a power-independent propulsion fraction of 0.108 given an assumed 1.0 kW kg⁻¹
for a small engine and generator. The model must then reproduce the design it was
calibrated from, and it does — take-off mass, propulsion fraction, engine rating,
lift-to-drag ratio, range and hover power all within 0.1 percent. Run at the heavy design
point without retuning, it predicts 1 037 kg against 1 000 kg and 1 813 km against
1 814 km; the one term that does not carry across is the engine rating margin, discussed
in Section 8.13.

**What differs between the architectures.** Mission, wing loading, disc loading, fuel
fraction, structural fraction, avionics fraction and energy chain are held identical.
Only three things change, and each is either a measurement quoted elsewhere in this paper
or an openly swept parameter:

| | Cruise L/D multiplier | Architecture-specific mass | Source |
|---|---|---|---|
| A — tail-sitter | 1 / 1.12 | — | Section 5.2, tip-frame drag |
| B — lift + cruise | 13 / 17 | second propulsion group, swept | Section 3.3, wind tunnel |
| C — tilt | 1.00 | tilt mechanism, swept | **assumed, not measured** |

**Result.** With the same buffered series-hybrid power system given to all three — which
neutralises the third bill, and does so against the proposed configuration:

| | Empty fraction | MTOW | L/D | Hover power | Range |
|---|---:|---:|---:|---:|---:|
| A — tail-sitter | 0.580 | 50.0 kg | 12.00 | 10.9 kW | 1 600 km |
| B — lift + cruise | 0.689 | 86.0 kg | 10.28 | 18.7 kW | 1 370 km |
| C — tilt | 0.624 | 60.3 kg | 13.44 | 13.1 kW | 1 792 km |

Against lift-plus-cruise the result is unambiguous and it is driven by measurement: the
same mission closes at seventy-two percent higher take-off mass and fourteen percent
lower range, and the drag term behind it is a wind-tunnel result, not an assumption.
Giving the lift-plus-cruise layout the additional structural fraction that distributed
lift is generally held to require makes its mass worse still — 117 kg at four additional
points of structure — without changing its range at all, so the comparison as tabulated
is generous to it rather than the reverse.

**Against tilt the table above goes the other way, and both reasons must be stated
plainly.** The tilting layout closes lighter than lift-plus-cruise and cruises twelve
percent further than the proposed configuration. Neither part of that outcome is a
finding. The first reason is the multiplier of 1.00, which credits the tilting layout
with paying no cruise drag at all for its nacelles, pivots, actuators and hover-pitched
blades. The second is subtler and belongs to the sizing rule rather than to any
architecture.

Range in the equation above contains the fuel fraction and not the fuel mass. Holding the
fraction fixed across architectures — the natural choice, and the one the table uses —
lets the heavier aircraft carry proportionally more fuel, which removes the mass bill
from the range column entirely. The general form is

$$R = \frac{E^{*}\eta_\text{chain}}{g}\,\frac{L}{D}\,\frac{m_\text{fuel}}{\mathrm{MTOW}}$$

so that a fixed fraction makes range independent of take-off mass, a fixed fuel *mass*
makes it inversely proportional to take-off mass, and a fixed take-off mass with a fixed
payload leaves fuel as the residual.

These are three different questions, and which one is the right question depends on what is
being procured: a mission, a fuel load, or a vehicle class. The mission stated in Section
6.2 — 13 kg of payload over roughly 1600 km, with take-off mass free to close where it will
— is closest to the first, which is also the only rule under which the tilting layout
leads, and leads only because its mechanism was credited as aerodynamically free. Reporting
that column on its own would restate the credit as a conclusion. **All three are therefore
given equal standing, and no result from this section should be quoted without the rule it
was computed under.** The tilting layout keeps its zero cruise-drag credit throughout:

| Range relative to the tail-sitter | Fixed fuel fraction | Fixed fuel mass | Fixed MTOW and payload |
|---|---:|---:|---:|
| B — lift + cruise | −14.4 % | −36.5 % | −72.6 % |
| C — tilt | +12.0 % | +0.2 % | −19.1 % |

Against lift-plus-cruise the conclusion is the same under every rule and grows more
emphatic as the rule tightens. Against tilt it is not: the twelve percent advantage
becomes a tie when the two aircraft carry the same fuel, and a nineteen percent deficit
when they are the same take-off mass carrying the same payload — because at 50 kg the
tilting layout's empty fraction leaves 0.116 for fuel where the proposed configuration
leaves 0.160. Sweeping the cruise-drag multiplier across all three rules gives the full
picture:

| Tilt cruise-drag multiplier | Fixed fuel fraction | Fixed fuel mass | Fixed MTOW and payload |
|---|---:|---:|---:|
| 1.00 | +12.0 % | +0.2 % | −19.1 % |
| 0.96 | +7.5 % | −4.3 % | −23.6 % |
| 0.92 | +3.0 % | −8.9 % | −28.2 % |
| 0.88 | −1.4 % | −13.4 % | −32.7 % |

Of the twelve cells, the tilting layout leads in three, all of them in the first column
and all of them requiring its mechanism to be aerodynamically free. Under the fixed
fraction the sign changes at a multiplier of approximately 0.89, which is to two decimal
places the penalty the proposed configuration charges itself for its own tip frames,
1/1.12 = 0.893. **The comparison therefore supports a conditional and not a ranking:
under a fixed fuel-fraction rule, and with the tilt mechanism assumed aerodynamically
free, the tilting layout cruises further; under equal fuel mass or equal take-off mass
that advantage disappears.** No claim of superiority over the tilting family is made here
in either direction.

Two smaller points belong with that disclosure. The cruise propulsive efficiency is also
shared with the tilting layout, which is generous, since a blade pitched for hover is not
the blade one would choose for cruise. **An earlier version of this section claimed that range
does not contain propulsive efficiency, and that is wrong**: the propeller is the last link of
the η_chain that appears in the range equation above, at 0.80 of the overall 0.176. The
generosity therefore falls on both columns. On mass, 60.3 kg becomes 62.7 kg at a fifteen percent
efficiency penalty; on range, the tilting layout's fixed-fraction advantage of twelve percent
falls to roughly **minus five percent**, since range is linear in η_chain. The correction moves
the comparison against the tilting layout rather than for it, which is why it is recorded here
rather than left as a rounding matter: the one column in which that architecture led is the
column the correction removes it from. The sizing tables above are not recomputed on it, because
the fifteen percent is an illustration and not a measurement; what the tables report is the
comparison with the credit left in place, which is the generous case. And a second table, in which
each architecture is given its own power system with no buffer, is not reported as a fair
comparison and should not be read as one: a real lift-plus-cruise aircraft hovers on
batteries rather than on an engine sized for hover, so that table is a bounding case for
an unbuffered series hybrid and not a description of the architecture it is labelled
with.

**What this comparison does and does not support.** It supports the claim that the
proposed configuration avoids the mass and drag bills that a separate lift system pays,
and it supports it with the paper's own measurements rather than by assertion. It does
not support a claim of superiority over the tilting family under every sizing rule, and
the paper does not make one; what it shows is that the tilting family's apparent
advantage survives only one of the three rules, and only on an assumption that was not
measured. The tilting family answers the same escape condition by a different route — the same
hardware, reused, but reoriented by a mechanism — and the case for the configuration
proposed here rests on reaching that reuse without the mechanism, together with its
control and transition consequences, and not on out-cruising it.
