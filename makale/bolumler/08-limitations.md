# 8. Limitations

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

This is a configuration study. It contains no experimental validation of any kind, and
the numbers in it are the output of elementary methods applied to a set of assumptions.
This section states what those limits are, in enough detail that a reader can judge how
much weight each result will bear. Several of the items below were discovered during the
study and changed its results; they are recorded here rather than smoothed away.

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
1.78 kg m⁻² of skin rather than the 1.5 assumed, the payload is gone. Every other line
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
bending moment is 934 N m, which a carbon spar cap of 10.7 mm² carries at the design
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

- The **roll authority** of the lower-surface strip — approximately 46 N·m, or twenty to
  twenty-five degrees per second — uses damping and control-effectiveness coefficients
  taken from the literature. The order of magnitude is defensible; the value is not. The
  length-versus-height conclusion is robust to the coefficient choice, because the
  proportional difference between the two is far larger than the uncertainty.
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
  the starting field, and the total between 0.0203 and 0.0230 — still below the assumed
  value in every case. What remains uncertain is no longer the dimensionality but, first,
  the transition state — the solution is fully turbulent, and the clean-surface case is
  still the strip estimate — and, second, the uniqueness of the solution itself, since the
  wall-resolved SST case settles four percent apart from two different starting fields.
  The build-up is reported as a bound on the assumption rather than as a replacement for
  it.
- **Span efficiency** is assumed at 0.85. A vortex-lattice solution gives an inviscid
  span efficiency of 0.99 for this planform, which is consistent with the assumed
  Oswald-type value once the viscous drag due to lift is allowed for, but does not
  measure the same quantity and is not offered as a correction to it.

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
is still absent, and the margins reported there are inertial rather than total. It also
records that the linear angle ramp used in Section 7.4 cannot be produced by any finite
moment. The aerodynamic model is a linear lift curve to stall with a flat-plate relation
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
profiles — two seconds for the light design, four for the heavy, entered at 5 m s⁻¹ of
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

## 8.14 What would change these conclusions

The results of this paper would be most efficiently attacked in four places, and they
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
   margin of 2.8 at the light design point and 1.69 at the heavy one, together with a
   scaling law for how that margin narrows with size. What it cannot do is charge the
   aerodynamic pitching moment, which requires moment coefficients through ninety degrees
   of incidence; those are not available for this planform and cannot be produced without
   a wind tunnel or a dedicated computational campaign. **This item is therefore reduced
   to a specific missing measurement rather than a missing analysis.**
4. **A panel-method analysis of the tip surfaces**, which would either convert Section
   8.7 into a quantified benefit or remove it. The vortex-lattice solution of Section 6.6
   covers the planform but not the tip surfaces, which remain unquantified.

None of these requires an experiment. The first has been carried out and its result is
folded into Section 6.6; the remaining three are within reach of a follow-on study, and
the configuration is described in enough detail in Section 4 and Section 6 for another
group to attempt any of them independently. The computational setup, the grid-convergence
study and the record of what failed along the way are in the repository, so the first
item can be re-run and checked rather than taken on trust.
