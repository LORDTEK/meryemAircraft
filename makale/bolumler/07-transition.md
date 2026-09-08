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

| t_r | w₀ = 0 | w₀ = 2 m/s | w₀ = 5 m/s | w₀ = 8 m/s |
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
transition rotates about — is **9.81 kg m²** and **2 503 kg m²**. The hand-placed figures
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
available moments are therefore 23.0 N m for the light design at its quoted 16.2 N per
pair, and 952 N m for the heavy design, whose transition thrust is not quoted in Section
6.3 and is computed here from its twelve percent power share as 200 N per pair.

| | Required, bang-bang | Required, smooth | Available | Margin, bang-bang | Margin, smooth |
|---|---:|---:|---:|---:|---:|
| Light, t_r = 2 s | 15.4 N m | 23.1 N m | 23.0 N m | **1.49 ×** | 0.99 × |
| Heavy, t_r = 5.1 s | 605 N m | 907 N m | 952 N m | **1.57 ×** | 1.05 × |

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
fifteen percent coaxial loss gives 12.4 N, an available moment of 17.6 N m, and a bang-bang
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
question.** The moment remaining after the inertia is turned — 11.9 N m for the light design
and 489 N m for the heavy one — divided by q S c̄ gives the pitching-moment coefficient that
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
entering from rest. The first of those sits *inside* the range of published post-stall values
rather than above it, so the mid-rotation condition is not comfortable either: entering the
rotation from a climb buys altitude at the cost of arriving at the high-incidence phase
faster, and therefore with less moment to spare. At the end of the rotation the incidence is small, five to
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

**Trim is not shown. It is a requirement, and the requirement is quantified.** At the cruise
lift coefficient of 0.45 the moment to be balanced about the centre of gravity has coefficient
C_L × (static margin), and the section camber must supply it. Across the plausible range of
centre-of-gravity positions:

| CG, % root chord | x_cg, m | Static margin, % MAC | Camber C_m required |
|---:|---:|---:|---:|
| 78 | 0.757 | +15.7 | 0.071 |
| 80.2 (packaging rule) | 0.778 | +12.5 | 0.056 |
| 83 | 0.805 | +8.3 | 0.037 |
| 85 | 0.825 | +5.3 | 0.024 |

Reflexed sections typically deliver 0.02 to 0.05. The upper half of that window is therefore
reachable with conventional reflex and the lower half is not, which turns the packaging rule
from a result into a design constraint: **the centre of gravity must lie between roughly 80
and 85 percent of root chord**, and closer to the aft end of that range than the volume
centroid alone would place it. It is not a demanding constraint — the internal volume's own
centroid is at 78.3 percent — but it is a constraint, and the placement of fuel, payload and
engine is not free. What is *not* established is that any particular camber and twist
distribution delivers the required moment at the required lift coefficient without an
unacceptable cruise drag penalty: the vortex-lattice model carries symmetric sections, so it
can size the requirement but cannot meet it. The aircraft of this paper is statically stable
and has an open trim closure, and those two statements should not be run together.

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

**Two limits of this reading are worth stating.** The incidence history comes from the
point-mass trajectory of Section 7.4: it is the geometric angle between the body axis and the
velocity vector, so it is only as good as that trajectory. And the rotation rate itself varies
the local incidence along the body by ω c̄ / 2V, which is ±3.1° for the light design entered in
a climb and ±8.6° entered from rest — so at the peak-incidence instant of that second case
parts of the airframe see close to thirty degrees. Nothing here should be read as a
demonstration of transition authority.
