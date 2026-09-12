# 7. Flight profile and transition

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

The transition between vertical and horizontal flight is the manoeuvre on which
tail-sitters have historically been judged, and it is the part of this configuration
that most deserves scrutiny. This section describes the flight profile, states the
equations that govern the transition, and reports a simulation of it. One result
contradicts a widely-assumed relationship and is presented as such.

## 7.1 The five phases

**Stance.** The aircraft rests on five points — the four lower ends of the tip frames
and the aft end of the centre keel — with its longitudinal axis vertical. No launch
equipment is present, and the aircraft is in its own storage attitude.

**Vertical take-off.** The nose pair spools to a thrust exceeding weight and the
aircraft rises vertically. Attitude is held by the four tip pairs. This is the
highest-power phase of the flight and the shortest.

**Transition.** The aircraft rotates from vertical to horizontal while accelerating,
until the wing carries the weight. Treated in detail below.

**Cruise.** The aircraft flies as a tailless blended-wing body. The nose pair is now
the cruise propulsor at its design point. The tip pairs provide pitch and yaw, and the
lower-surface strip provides roll.

**Landing.** The reverse of transition, followed by a vertical descent onto the five
contact points. Section 7.5 notes what is and is not analysed here.

Figure 9 shows the five phases in sequence. Nothing on the aircraft rotates relative to
the aircraft at any point in it.

## 7.2 Why the transition begins in the easiest condition

A common objection to tail-sitter transition is that the aircraft must fight the
airflow while rotating. For a transition that begins in hover, it does not. At the
start of the manoeuvre the airspeed is zero, so the free-stream dynamic pressure

    q = ½ρV²

is zero, and with it every aerodynamic moment that would resist the rotation. The
aircraft is not turning against the air; it is turning in still air and then meeting
the air as it accelerates.

The consequence is that the difficult part of the transition is not its beginning but
its middle, where the airspeed has grown enough for aerodynamic moments to matter but
the wing is not yet carrying the weight. The control authority requirement is set
there, not at the start.

## 7.3 The thrust singularity that is never reached

Consider the aircraft at an angle θ from the vertical, and suppose for a moment that it
must hold altitude with thrust alone. Vertical equilibrium then requires

    T cos θ = W        →        T = W / cos θ

which diverges as θ approaches ninety degrees. Read literally, this says a tail-sitter
cannot complete a transition, and the expression is sometimes quoted to that effect.

The expression is correct and the conclusion drawn from it is not, because the premise
is false. The aircraft does not hold altitude with thrust alone. Vertical support is

    T cos θ + L = W,        L = ½ρV²S C_L

and V is not zero during the rotation — it is growing, because the horizontal component
T sin θ is accelerating the aircraft. The horizontal acceleration, in the same
idealisation, is

    a = g tan θ

so the very rotation that reduces the vertical component of thrust is what generates
the airspeed that replaces it. The singularity is never approached because the wing
arrives first.

This is the central mechanism of the manoeuvre, and it also explains the result of the
next subsection.

## 7.4 Transition time: slower is better

The transition was simulated as a two-degree-of-freedom point mass. The body angle θ is
driven from zero to ninety degrees over a rotation time t_r; thrust acts along the body
axis, lift perpendicular to the velocity vector and drag opposite to it; the lift curve
is linear to stall and a flat-plate relation beyond it; and thrust is reduced to the
drag value once cruise speed is reached. Altitude loss is reported as the lowest point
of the trajectory relative to the entry altitude.

The result is plotted in Figure 10a for both reference designs and four thrust-to-weight
ratios; the tables below give the same values.

**Light reference design, 50 kg. Altitude loss, metres:**

| t_r | T/W = 1.1 | **T/W = 1.2** | T/W = 1.3 | T/W = 1.5 |
|---:|---:|---:|---:|---:|
| 0.5 s | −19.1 | −16.6 | −14.5 | −11.0 |
| 1 s | −17.1 | −14.2 | −11.6 | −3.5 |
| 2 s | −13.2 | **−9.1** | −2.1 | 0 |
| 3 s | −9.9 | **−0.8** | 0 | 0 |
| 4 s | −2.2 | **0** | 0 | 0 |

**Heavy reference design, 1000 kg. Altitude loss, metres:**

| t_r | T/W = 1.1 | **T/W = 1.2** | T/W = 1.3 | T/W = 1.5 |
|---:|---:|---:|---:|---:|
| 1 s | −32.2 | −27.4 | −23.3 | −16.0 |
| 2 s | −27.0 | −20.9 | −7.7 | −1.0 |
| 3 s | −21.8 | **−7.2** | −1.4 | 0 |
| 4 s | −17.7 | **−1.4** | 0 | 0 |
| 5 s | −5.8 | **0** | 0 | 0 |

The relationship is monotonic in the direction opposite to the one usually assumed. It
is frequently supposed that a tail-sitter should rotate as quickly as possible, on the
reasoning that the aircraft is unsupported during the rotation and therefore falls for a
time t_r, giving an altitude loss proportional to t_r². **That reasoning is wrong, and
the error is in its premise.** The aircraft is not unsupported during the rotation.
Vertical support is T cos θ + L, and a slow rotation keeps cos θ large during exactly
the interval in which V, and therefore L, is being built. A fast rotation collapses
cos θ before there is any L to replace it, and the aircraft falls precisely because it
hurried.

The practical consequence is a simplification rather than a trade. The control power
required to rotate the aircraft in time t_r scales as 1/t_r², so a slow rotation is
cheap in control authority; and the altitude loss also falls with t_r. **Both
constraints point the same way.** There is no optimum transition time to be found
between two competing penalties, because there are not two competing penalties. The
transition time is bounded from below, not from above, and its upper bound is set by
fuel, horizontal displacement and operational exposure rather than by flight mechanics.

Thrust-to-weight ratio is the dominant parameter. At T/W = 1.1 the loss stays in double
figures until the rotation is stretched beyond three seconds; at T/W = 1.3 the light
design reaches zero within three seconds and the heavy design within four. The reference
designs assume T/W = 1.2, at which the light design completes the manoeuvre in three
seconds for a loss under one metre and the heavy design in five seconds for no loss.

### Entering the rotation while climbing

The tables above assume the aircraft rotates from a stationary hover. It does not have
to, and it should not. The aircraft reaches transition altitude by climbing, which means
it arrives there with an upward velocity that has already been paid for. Stopping to
hover before rotating discards that velocity deliberately.

Carrying it into the manoeuvre instead converts it into a reserve. Repeating the
simulation with an entry climb rate w₀:

**Light reference design, T/W = 1.2. Altitude loss, metres:** (plotted in Figure 10b)

| t_r | w₀ = 0 | w₀ = 2 m s⁻¹ | w₀ = 5 m s⁻¹ | w₀ = 8 m s⁻¹ |
|---:|---:|---:|---:|---:|
| 1 s | −14.2 | −10.3 | −0.4 | **0** |
| 2 s | −9.1 | −0.4 | **0** | **0** |
| 3 s | −0.8 | **0** | **0** | **0** |
| 4 s | **0** | **0** | **0** | **0** |

A five-metre-per-second entry climb removes the altitude loss at every rotation time
that is otherwise sensible, and the heavy design behaves the same way. The cost of
**These tables use a kinematically driven angle profile, and its sensitivity has been
measured.** The body angle is ramped linearly, which Section 7.6 shows no finite moment can
produce. Repeating the calculation with the two realisable profiles of that section moves
the entries by one to two metres in most cells and leaves the conclusion of this section
untouched: at an entry climb of 5 m s⁻¹ the loss is zero for all three profiles, at both
design points and at every thrust-to-weight ratio tabulated, and it remains zero for the
heavy design at the 4.06 and 4.98 seconds that Section 7.6 identifies as the shortest
rotations its moment authority allows. One cell moves materially and is flagged rather than
smoothed: the heavy design at T/W = 1.2 and t_r = 4 s with no entry climb reads −1.4 m on
the linear profile and −11.6 to −13.4 m on the realisable ones. That cell is a reference
condition in neither respect — the reference profiles enter with climb, and the heavy
rotation time has since been set at 5.1 s — but the tables should be read as a kinematic
parametric map rather than as achievable trajectories.

acquiring that climb rate is negligible: at T/W = 1.2 the vertical acceleration is
(T/W − 1)g = 1.96 m s⁻², so five metres per second is reached in 2.6 s over 6.4 m of
climb, and the kinetic energy involved is 625 J against a fuel energy of 103 kWh.

**The reference profile is therefore to enter the rotation at 5 m s⁻¹ of climb and
rotate over the times given in Section 6 — two seconds for the light design, 5.1 for
the heavy — for no altitude loss at all.** The manoeuvre that the
literature treats as the tail-sitter's characteristic hazard becomes, in this
configuration, a manoeuvre with no altitude penalty — not because of any device, but
because the aircraft is not asked to stop first.

The limits of this simulation should be stated where its results are used. It is a point-mass model in which the body angle is driven kinematically, so it does not represent rotational dynamics and the tip-propeller thrust required to produce the rotation does not follow from it. The aerodynamic model is a linear lift curve to stall with a flat-plate relation beyond it; dynamic stall, separation hysteresis and propeller-wake effects on the wing are absent.

With the transition no longer demanding a rapid rotation, it is no longer the case that
sizes the tip propellers. The sizing case becomes disturbance rejection in hover, which
an order-of-magnitude estimate places well inside the existing capability: a five-metre-
per-second gust normal to the planform produces a moment of the order of 5 N·m, against
a capability of M = 2 T L = 23 N·m from the tip pairs at the reference geometry — a
margin of roughly four. The tip propellers are
therefore kept small — 0.20 m — deliberately, so that they contribute as little as
possible to cruise drag while retaining margin on the case that actually sizes them.

This is an order-of-magnitude check against a single gust condition. The disturbance spectrum and the closed-loop bandwidth required to reject it have not been analysed.

## 7.5 Landing

Landing reverses the sequence: the aircraft decelerates, rotates nose-up, and descends
vertically onto its five contact points. Two things should be said about it plainly.

The first is that the historical objection to this manoeuvre does not apply. The XFY-1
was cancelled because its pilot had to judge a backwards vertical descent by looking
over his shoulder. There is no pilot here, and height above ground is a sensor
measurement rather than a human estimate.

The second is that the vertical descent itself has not been analysed in this study. A
rotor descending into its own wake can enter the vortex ring state, in which thrust
becomes erratic and increasing power makes matters worse. Whether the descent profile
of this configuration enters that region, and at what rate of descent, is an open
question. It is listed in Section 8 rather than answered here.

## 7.6 Whether there is enough authority to rotate

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
where the hover figure of merit used elsewhere is 0.599. Recomputing at 0.599 with a
fifteen percent coaxial loss gives 12.4 N, an available moment of 17.6 N·m, and a bang-bang
margin of 1.59 — still comfortable. The heavy figure was computed on that conservative
basis to begin with.

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

**The conclusion does not depend on that ratio, which is fortunate, because the ratio is not
settled.** Traub reports both an inviscid Oswald factor from a vortex-lattice solution and a
measured one from the tunnel for three wings [18]; the planar case gives a measured-to-inviscid
ratio of 0.95, but his two non-planar cases give 1.01 and 1.07, which cannot be right for a real
wing and are presumably an artefact of comparing an uncorrected tunnel measurement with an
inviscid calculation. That data therefore bounds the ratio loosely rather than fixing it. But
the sign of the conclusion survives the whole plausible band:

| Viscous / inviscid ratio | Implied Oswald e | Cruise L/D | Against the assumed 12.04 |
|---:|---:|---:|---:|
| 0.85 | 0.735 | 11.44 | −5.0 % |
| 0.90 | 0.778 | 11.68 | −3.0 % |
| 0.95 | 0.822 | 11.90 | −1.2 % |

**For any ratio below unity — that is, for any wing with viscosity — the trimmed span
efficiency is below the assumed 0.85 and the cruise lift-to-drag ratio is below 12.04.** Only
the magnitude is open, and it lies between one and five percent. The assumption is not revised
here because revising it would mean choosing a ratio this study has not measured; what has
changed is that it is no longer bounded from above by a calculation, and Section 8 records it
as exposed. It is worth adding that 0.85 at this aspect ratio is a conventional choice rather
than a careless one — an independent eVTOL sizing study adopts the same value at aspect ratio
7.0 [26] — which is precisely why it survived so long without being examined.

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
