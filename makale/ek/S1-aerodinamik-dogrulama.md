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
