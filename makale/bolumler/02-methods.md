# 2. Materials and Methods

This section states the analytical framework the paper is built on, defines the
configuration it is applied to, and gives the methods by which every number in Section 3 was
produced. Sections 2.1 to 2.6 develop the framework; Sections 2.7 to 2.11 define the aircraft;
Sections 2.12 and 2.13 give the sizing and computational methods; Section 2.14 records the use
of artificial-intelligence tools.

Hybrid VTOL aircraft work. The argument of this section is not that they do not, but
that they pay for the capability in a way that can be located precisely, that the
payment appears in three different currencies, and that an improvement in one currency
is usually a transfer into another rather than a reduction. The section closes by
stating the condition under which the payment would be zero — a condition none of the
current architectures satisfies, and which Section 2 is built to satisfy.

## 2.1 The root: a duty cycle that does not match the hardware

Every hybrid VTOL aircraft contains hardware whose only purpose is the vertical phase.
That phase is short. For a mission of one hour, a take-off, a transition, a return
transition and a landing occupy on the order of a minute — roughly two percent of the
flight. The remaining ninety-eight percent is spent carrying that hardware through the
air.

This is not an implementation defect and it cannot be engineered away by making the
hardware better, because it is a statement about duty cycle rather than about quality.
A lighter lift rotor is still carried for the whole flight. A cleaner lift rotor is
still carried for the whole flight. The mismatch between how long a component is
needed and how long it is present is the origin of all three bills below.

## 2.2 Bill 1 — mass

The most direct payment is dead mass. A lift-plus-cruise aircraft carries two propulsion groups:
rotors, motors, mounts, wiring and structural reinforcement for the vertical phase, and a
separate propulsor for cruise. The vertical group is inert for the whole cruise but is still
lifted. Its cost is not linear, because mass growth feeds itself: MTOW = m_payload /
(1 − f_empty − f_energy) shows that additional empty mass enters through a multiplier that grows
as the denominator shrinks, and in the vertical phase the same increment is charged again
because hover power scales with W^1.5. A modest dead-mass fraction becomes a large payload
penalty.

**This bill has been identified independently.** A NASA study sizing four VTOL architectures
against a common mission with common tools found the lift-plus-cruise concepts the heaviest of
the vehicles examined, and is explicit about the cause [22]:

> *"The weight of the Lift+Cruise concepts is heavier in general than for the other vehicles.
> This is not driven by the cruise power draw, as the L/D_e of the Lift+Cruise is indeed higher
> than the other vehicles... the most likely targets for reducing vehicle weight are the extra
> empty weight items on board in hover (wing and propeller)."*

**The finding separates the two things this paper is at pains to separate**: the lift-plus-cruise
vehicle is *aerodynamically better* than the alternatives — its cruise efficiency is higher, and
the study says so — and it is nevertheless the heaviest, because of hardware carried in order to
hover. That is Bill 1 stated by an independent source in its own terms: not a failure of
engineering, but the cost of an architecture.

A second NASA review states the structural half as a general principle, drawn from a tilt-prop
aircraft whose propeller separated in flight after a gearbox mounting fatigued: "to safely
transmit power to the extremities of the planform, very strong (and fatigue-resistant)
structures must be incorporated with an obvious weight penalty" [2]. **Distributing lift or
thrust across the span therefore obliges the structure that reaches it to be strong enough and
fatigue-resistant enough to keep transmitting power there — charged to mass, whether or not the
distributed propulsors are running.**

## 2.3 Bill 2 — drag

The second payment is charged only to architectures that leave hover hardware exposed in forward
flight: rotors stopped in the airstream, the booms that carry them, and the interference between
their wakes and the wing.

The cleanest measurement is a controlled comparison within a single aircraft. In a doctoral
study, one uncrewed airframe was tested in a wind tunnel in three configurations (Table 1):

**Table 1.** Maximum lift-to-drag ratio of one uncrewed airframe tested in three configurations in a single wind-tunnel campaign [3].

| Configuration | Maximum L/D |
|---|---:|
| Clean airframe, no hover hardware | ≈ 17 |
| Hover hardware installed, propellers aligned with the flow | ≈ 13 |
| Hover hardware installed, propellers perpendicular to the flow | ≈ 9 |

**Two measured numbers follow.** Installing the hover hardware costs about a quarter of the
lift-to-drag ratio; failing to let the propellers align with the flow costs about a third of what
remains. A second model on a different airframe reproduced the pattern, at L/D ≈ 11 retracted
against ≈ 8 exposed. Expressed as drag, retracting the propellers reduced it by 34 % and 30 %
relative to a standard quadplane. That study's author is careful about which comparison is
legitimate — measuring the retracted aircraft against *itself* with propellers deployed gives
63 %, which he explicitly rejects — and the caution is worth adopting. Because range is linear in
lift-to-drag ratio for a fixed energy system, this ladder translates directly into range
(Figure 3).

**A third finding constrains what can be done about the penalty**, and matters more than either
number:

> *"The difference between propellers parallel to the airflow and without propellers is modest.
> The drag produced by the motors is significant."*

The bill is charged mainly by the motors and the beams that carry them — hardware that cannot be
feathered, folded or aligned away, **because its cost is its presence.**

Two further measurements support the direction. Wind-tunnel characterisation of a QuadPlane
found the highest lift and least drag in fixed-wing mode at both cruise airspeeds, drag in the
hybrid regime exceeding either pure mode through adverse flow interaction, and — a point that
matters for how such aircraft are designed — that a simulation assuming negligible
rotor–structure interaction "always predicts higher lift and lower drag than were experimentally
observed." Separately, a study of twenty-six stationary lift propellers held edge-on found their
drag scaling with frontal area and the square of airspeed, with hover powertrain components
adding "a significant amount of aerodynamic drag during forward flight" absent a stowing
mechanism.

**The important property of this bill is not its size but where it is charged.** It is charged
per unit time in cruise, so it grows with exactly the quantity the aircraft exists to maximise.

## 2.4 Bill 3 — power system sizing

The third payment is the least visible and often the largest. A VTOL aircraft must
install enough power to hover, but it only uses that much power for the two percent of
the flight in which it hovers. The ratio between the two demands follows from the
governing equations rather than from any design choice. Taking hover power from
momentum theory and cruise power from the drag polar,

    P_hover / W  = √(DL / 2ρ) / η_h                 (DL = W/A, disc loading)
    P_cruise / W = V / ( (L/D) η_p )

so that

    P_hover / P_cruise = √(DL / 2ρ) · (L/D) / V · (η_p / η_h)

Every term on the right is a property of the configuration, not of the workmanship. A
vehicle with a disc loading of 100 N m⁻², a cruise lift-to-drag ratio of 15 and a
cruise speed of 30 m s⁻¹ needs roughly four times as much power to hover as to cruise;
raising the disc loading raises the ratio as its square root. The prediction is
borne out in flight: a carbon-fibre tail-sitter reported in the literature measures its
level-flight power consumption at one fifth of its hover power, which is the same ratio
this expression gives for an aircraft of that class. The power system is
therefore sized by a condition that holds for a minute and is then carried, unused, for
an hour.

The consequence propagates. Sizing by hover means an oversized engine, or a battery
that must deliver a peak it will rarely be asked for, or both — and whichever of the
two is chosen, the extra installed capacity is mass, which returns to Bill 1.

## 2.5 The bills are one quantity in three currencies

The three bills are not independent problems with independent fixes. **Each known architectural
move reduces one and increases another.** Figure 4 shows the transfers; Table 2 lists them.

**Table 2.** Architectural moves and the bills they transfer.

| Move | Bill it attacks | Bill it creates |
|---|---|---|
| Distributed electric lift rotors | 3 — the cruise engine no longer sizes to hover | 1 and 2 — many rotors and mounts, permanently carried and exposed |
| Folding or retracting lift rotors | 2 — the exposed rotor is removed from cruise | 1 — mechanism, actuation, locking, a new failure mode |
| Tilt-rotor, tilt-wing, tilt-nacelle | 1 — one propulsion group serves both regimes | mechanical complexity, gyroscopic coupling, a transition control problem |
| Higher disc loading, smaller rotors | 1 and 2 — smaller, lighter, cleaner rotors | 3 — hover power rises with √(DL) |
| Lower disc loading, larger rotors | 3 — hover power falls | 1 and 2 — larger structure and exposed area |

**One of these rows has been measured.** In the study of Section 2.3, the retraction system that
removed thirty percent of the drag was then costed: applied to a passenger eVTOL with the
mechanism assessed at five percent of vehicle mass, maximum range rose from 119 km to 121 km —
**a two-kilometre gain for a five-percent mass penalty.** Bill 2 was converted almost exactly
into Bill 1, and the transfer is the point rather than the small residue.

## 2.6 The condition under which the three bills are not charged

Stating the tax this way makes its escape condition explicit. The bill exists because
hover and cruise are served by hardware that is not the same hardware, doing the same
job, in the same orientation. Relax any part of that and a bill appears:

- **Different hardware** → Bills 1 and 2. The unused set is carried and, if exposed, drags.
- **Same hardware, different orientation** → the tilting family. The mechanism that changes the orientation is itself mass, complexity and a control problem.
- **Same hardware, same orientation, different sizing point** → Bill 3, unless the hover peak is supplied from somewhere other than the continuous power source.

The condition for not incurring these three bills is therefore that the same propulsors,
fixed in the same orientation relative to the airframe, produce both the hover thrust and
the cruise thrust — with the aircraft itself changing orientation rather than any part of
it — and that the difference between the hover peak and the cruise demand is supplied by a
buffer rather than by permanently installed continuous power. This is referred to below as
the *zero-bill condition*, and the name should be read strictly: it means zero of these
three bills, not an architecture that costs nothing. What an architecture satisfying it
pays instead is a separate question, and Section 3.5 answers it for the configuration
proposed here.

That is a description of a tail-sitter with a buffered series-hybrid powertrain. It is
also, precisely, the configuration described in Section 2.

## 2.7 Overview

**The configuration satisfies the zero-bill condition of Section 2.6 in its primary propulsor,
and re-opens one of the three bills in its attitude system.** The distinction matters enough to
state here rather than to leave to Section 3: the single coaxial nose pair meets all four
conditions — same hardware, same orientation, same job, hover peak from a buffer — and it is that
pair which carries the aircraft. The four attitude pairs do not. They are exposed in the cruise
flow, they cannot be feathered, and Section 3.3 computes the drag they cost. **The instantiation
is therefore partial, and reporting what the partial part costs is a substantial share of what
Section 3 does.** What follows is the configuration that makes the primary pair possible. The aircraft stands on its tail. Its entire airframe is a blended-wing
body: there is no cylindrical fuselage, and every part of the planform carries payload
and produces lift. A single coaxial counter-rotating propeller pair at the nose
produces all propulsive thrust, in hover and in cruise alike, without changing its
orientation relative to the airframe. Four small coaxial pairs, mounted on rigid frames
at the wing tips, produce attitude control and, at take-off, the thrust margin the nose pair
does not have — Section 3.15 works out why, and it is the one place this configuration asks a
component to do a second job it was not sized for. The energy system is a
series hybrid: fuel drives an internal-combustion engine, the engine drives a
generator, and the generator supplies electric machines at the rotors.

The aircraft has no elevons, no rudder, no tilting mechanism, no retraction mechanism
and no dedicated lift system. **That last phrase needs one qualification, made here so that it is
not mistaken for a stronger claim later.** The four tip pairs exist to produce moments, and their
thrust is sized by that duty; but the primary propulsor is sized at thrust equal to weight
exactly, so the margin that actually lifts the aircraft off the ground comes from those four
pairs. They are not a lift system — they are not sized for lift, they do not carry the aircraft
in hover, and they are absent from the hover power budget as a lift term — but the configuration
does depend on their surplus for take-off, and Section 4.4 treats that dependence as a
limitation rather than a feature. The only moving aerodynamic device is a variable-extension strip on
the lower surface, described in Section 2.10, which exists solely because roll cannot be
produced by propellers alone. Figure 5 gives three orthogonal views of the light
reference design and Figure 6 a general view of the same geometry.

## 2.8 Planform

The planform is a blended-wing body whose leading-edge sweep varies continuously along the span
while the trailing edge is held constant. The sweep law is linear in span from 45° at the root
towards 35° at the station where leading and trailing edges would converge; the wing is cropped
at 67 % of that station, so the realised sweep runs from **45° at the root to 38.3° at the tip**,
with the trailing edge constant at **25°**. Thickness runs from 25 % of chord at the root to
12 % at the tip and the chord from 0.970 m to 0.236 m, a taper ratio of 0.244 — one distribution
rather than four independent ones. **The realised sweep variation is therefore modest, under
seven degrees**, and the crescent character comes from the curvature of the leading edge and the
divergence between the two edge angles rather than from a large change in sweep. These values
were chosen, not derived: the 20°–40° band they started from was reported favourable in the
transonic-transport literature the crescent-wing idea comes from, and this aircraft is subsonic,
so that band does not transfer on its own authority. Section 4 lists it among the limitations.

**Sweep does two jobs here, and the second is why it is not a free parameter.** The aircraft is
tailless: with no horizontal stabiliser on a boom, the pitching moment must be generated by the
distribution of lift along the body itself, and sweep is what places the outboard sections behind
the centre of gravity so that they can do it. **The sweep angle and the longitudinal stability
are the same design variable seen from two directions.** Decreasing sweep outboard also keeps
the tips from stalling first, which matters more than usual on a tailless aircraft because a tip
stall on a swept planform moves the centre of pressure forward and pitches the aircraft further
in, with no tail to argue with.

The reference geometry for the light design is a root chord of 0.970 m, a tip chord of 0.236 m,
a span of 3.453 m, a wing area of 1.979 m² and an aspect ratio of 6.03, giving a wing loading of
25.3 kg m⁻² and a stall speed of 20.1 m s⁻¹ against a cruise speed of 30 m s⁻¹. Figure 7 gives
the distributions.

## 2.9 Propulsion

Every propeller is a coaxial counter-rotating pair, for one reason worth stating narrowly:
**reaction torque.** A single propeller applies to the airframe a torque equal and opposite to
the one it applies to the air, acting about the yaw axis in hover and the roll axis in cruise,
and it must be opposed continuously — by a control surface, which costs drag, or by differential
thrust, which costs a control channel. A counter-rotating pair does not produce it.

The pairs are of fixed geometry: no cyclic pitch, no collective, no variable mechanism. **This
has a consequence for the tip pairs in cruise that Section 3.3 works out** — unable to feather,
they must either turn at the zero-shaft-torque condition or be stopped, and the difference
between those two states is a substantial fraction of the aircraft's zero-lift drag;
Section 3.3 computes both ends of it rather than assuming the lower one. The torque balance is exact
at cruise rather than hover, so a small residual remains in hover.

The arrangement has a second consequence the transition analysis depends on. Because the two
rotors of each pair carry equal and opposite angular momentum, **the net angular momentum of the
propulsion system is nominally zero**: rotating the airframe through ninety degrees precesses
nothing, and no gyroscopic moment appears for the control system to cancel. In a tilting
architecture that term is present and must be designed for; here it is absent by construction.

Crucially, the pair is never a contra-rotating gearbox. Each rotor is driven by its own electric
machine on a common axis, so the mechanism that repeatedly defeated the XB-35 — concentric
shafts, a splitting gearbox, and the governors that synchronise them — is never built.

The energy path is a series hybrid: fuel → engine → generator → electric machines. The engine is
not mechanically connected to any rotor; it is an energy source, and that decoupling is what
allows it to be sized for cruise rather than hover. For the light design the continuous cruise
requirement is 1.9 kW at the engine shaft and the engine is sized at 2.6 kW, while the hover
requirement is 10.9 kW at the rotor; the difference is supplied for the vertical phase by a
**1.8 kg battery buffer, 3.6 percent of take-off mass**. That is the mechanism that releases the
engine from the hover condition — Bill 3 as Section 2 defines it. The electrical path is not
released, and Section 3.4 says so.

## 2.10 Control without control surfaces

The nose pair produces thrust; the four tip pairs produce moments. They are not lift rotors and
are not sized to hover the aircraft — in the vertical phase they carry under fifteen percent of
total power. Each tip pair on the light design is 0.20 m in diameter and produces 16.2 N during
the transition manoeuvre, drawing 335 W, 1.34 kW across the four. The principle is not new: a
survey of tail-sitter development identifies adding propellers away from the axis as a way to
generate transition pitching moment, and a flight-tested quad tail-sitter uses exactly this
arrangement [30]. The full derivations for all three axes are in Supplementary S3; what follows
is the result in each.

**Pitch and yaw are produced by differential thrust, and the yaw arm is the larger.** The tip
frames extend ±0.71 m perpendicular to the planform, so a differential between the upper and
lower pairs acts at 0.71 m in pitch, while a differential between the left and right pairs acts
at the **semi-span, 1.726 m — 2.43 times the pitch arm**. Yaw is therefore the strongest axis
on this aircraft, which is the reverse of the usual situation and is a free consequence of the
tip-propeller layout rather than a design choice. Figure 8 shows the placement and the two arms,
and shows why the third axis has neither: every thrust vector is parallel to the body axis, so
no combination of settings produces a rolling moment.

**Roll cannot be produced by propellers at all**, because every pair is coaxial and
torque-balanced by construction. It is the one axis that needs an aerodynamic device, and that
device is the only moving aerodynamic surface on the aircraft: a strip on the lower surface,
inclined at 45° in planform, running 120 % of root chord and reaching 67 % of semi-span,
standing 2 cm proud at its inboard end and 6 cm at its outboard end. **Extension is the control
variable** — the strip is modulated, not switched. Figure 9 shows it against the nose
propeller's slipstream: the inboard 46 percent of its length lies inside the slipstream, where
dynamic pressure is set by disc loading and is therefore available at zero airspeed, and the
outboard 54 percent works against the freestream in cruise. That split is why one device serves
both regimes.

Roll inertia computed from the component mass distribution is 25.0 kg·m², two and a half times
the pitch inertia, and the roll damping derivative from a helix-angle vortex-lattice solution is
|C_l_p| = 0.358, giving a damping slope of 77.6 N·m per rad s⁻¹ and a roll time constant of
0.32 s. **Twenty degrees per second at cruise therefore requires 27.1 N·m.** The strip's own
force as a swept fence, at an upper-bound normal-force coefficient of 1.3, supplies 11.3 N·m —
about a third. The remainder must come from the second mechanism, the change the strip makes to
the circulation of the half-wing it sits on, which asks for **ΔC_L ≈ 0.12** over the strip's
span. Measured data on non-planar wings carrying Gurney flaps of two percent chord over the
inboard two-thirds gives lift increments of that magnitude [18], and a lift-enhancing tab study
gives a measured height threshold of 1.5 % chord above which maximum lift-to-drag falls [32].
**Roll authority is therefore sized and supported by measurement on a comparable device, and it
is not closed**: the quantity a future measurement must return is ΔC_L for this strip on this
planform.

**The strip loads the other two axes, and Supplementary S3 quantifies all three couplings.**
Deployed on one side it raises drag there and yaws the aircraft towards the strip — adverse yaw
in the classical sense, 11.3 N·m at the present height law, against 42.8 to 55.9 N·m of yaw
authority, so it costs five to twenty-six percent of the strongest axis. It also pitches the
nose down, by ΔC_m between 0.005 and 0.032 depending on where along the chord the lift increment
acts; the tightest pitching-moment budget in Section 3.17 is 0.050, so at the upper end a
commanded roll would consume two thirds of it. **The conclusion is a scheduling requirement
rather than a redesign: the strip should not be commanded at full extension during the end of
the rotation.** The older literature states the same coupling more bluntly — for spoilers used
as ailerons on tailless aircraft, "if only upgoing spoiler projections are used, the pitching
moments developed are prohibitive", with projection from both surfaces named as the remedy [19].
The strip here projects from one surface only, which is the arrangement that warning is about.

Because extension is continuous, the strip also has a threshold. Projections below one percent
of local chord produce negligible lift change [19], and the strip is tapered, so this cuts a
graded dead band out of the bottom of its travel: **nothing below seven percent of commanded
extension, and linear to within five percent only above twenty-five**. The part that survives
the threshold is the part with the longest arm, so most of the lost area is bought back by the
lengthened arm — the deficit is confined to small corrections rather than large ones.

**The same device has a third use that costs nothing.** Deployed on both halves at once it is a
speed brake, and in that mode the pitching-moment objection does not arise: spoiler-type
ailerons used as speed brakes "had only a small effect on the wing pitching moments", and "the
rolling effectiveness of the ailerons will not be impaired by such use" [49]. That gives this
configuration a descent-rate control no other part of it provides.

**Hover is the harder case, for a structural reason rather than a numerical one.** At zero
airspeed only the inboard part of the strip is loaded, by the nose propeller's slipstream, and
the same circulation model over the slipstream-washed area gives 6.0 to 12.0 N·m — enough for a
thirty-degree bank in 1.5 to 2.1 s. But there is no aerodynamic damping at all at zero airspeed:
the roll axis is a double integrator, so the rate does not settle and the strip must be
commanded off rather than left out. **Roll control in hover is a tighter problem than roll
control in cruise**, which is the reverse of the usual situation.

Two measured effects work against the strip in the conditions this configuration needs it, and
one works for it. A Gurney flap under controlled inflow turbulence became "less effective after
stall angle", and at nineteen percent turbulence intensity "the benefit to the aerodynamic
performance was negligible" [35] — and the strip's inboard portion is deliberately placed inside
a propeller slipstream, which is not a low-turbulence environment. The post-stall half of that
is contested: a delayed-detached-eddy simulation at twenty degrees of incidence with a flap of
the same height fraction returns lift higher by ninety-four percent at unchanged drag [37],
though on a baseline twenty-five percent below the experimental value. **The turbulence
sensitivity is measured and unopposed; the post-stall behaviour is contested.** Against both, a
water-tunnel study found the mechanism qualitatively unchanged at a Reynolds number of 8 588 —
four orders of magnitude below the usual test range — because an effective camber increase is
"an inviscid effect to the first order" [38]. That is the most direct support available for the
claim that the strip still works at zero airspeed, and it supports the direction rather than the
magnitude.

**Directional stability is the one open half of the yaw axis.** A vortex-lattice solution of the
planform at sideslip returns **C_n_β = 0**: the wing supplies none, which is not a defect of the
solution but the expected result for a planar surface, and which two measurement campaigns
confirm is normal for tailless aircraft rather than unusual [19,20]. Sweep gives this
configuration its roll-due-to-sideslip — C_l_β = −0.045 per radian, a healthy value — and gives
it no weathercock stability at all. **Zero is also an optimistic starting point rather than a
neutral one**, because a vortex-lattice model has no volume: the centre body develops side force
ahead of the centre of gravity, and on tailless aircraft that destabilising contribution is
reported to be "at least as great as the stabilising effects contributed by the wing alone"
[19].

Directional stability must therefore come from the tip frames, which in cruise are the only
vertical surfaces the aircraft has. Sized against the criterion the tailless literature
recommends — C_n_β greater than 0.001 per degree, or 0.0573 per radian [19] — the fairing chord
required over the combined frame length is **39 mm**, against the 50 to 70 mm a 20 mm faired
strut carries in any case. **Directional stability on this configuration does not ask for a
surface; it asks for a fairing on a frame that is already there.** Two requirements come with
it. The fairing needs a toe angle, and its sign follows from the aspect ratio: low-aspect-ratio
fins are toed *in* so the stabilising moment comes from induced drag, high-aspect-ratio fins
toed *out* so it comes from "the outwardly directed lift" [19] — and these frames are firmly in
the second class, so **the sign is toe-out**. Toe-out carries a hazard: yawing far enough to
stall the rear fin produces a large *destabilising* moment, which sets an upper bound on usable
sideslip that this paper does not compute.

**The second requirement is harder, and the measured record is against the assumption the
fairing was sized on.** A 39 mm chord at cruise sits at a chord Reynolds number near 80 000, and
the side force credited to it above was computed from a lift-curve slope of 4 per radian.
Symmetric sections at that Reynolds number are not measured to behave that way. The compilation
that reports four such sections tested at Princeton finds lift-curve nonlinearity about zero
incidence in all of them, in the severest case the slope "actually changed sign over a 3 deg
range" [36] — and it states the effect as a property of the class rather than an accident of one
section: "past work on **symmetrical** airfoils has shown that a **deadband often appears in the
lift curve near zero degrees**", present at Reynolds numbers of 60 000 and 100 000 and absent at
higher ones [36]. A toe angle of one or two degrees puts the fairing inside that band. **The open
question is therefore not which way to toe the fairing but whether a surface of that chord, at
that Reynolds number, develops the side force at all** — and 4 per radian should be read as an
upper bound rather than as a conservative choice, since what fails there is the linearity of the
curve and not merely the size of its slope.

The same source names the remedy, and it is cheap here. Camber removes the deadband: cambered
sections "do not appear to have a similar, intrinsic deadband region" [36], and the observation
is drawn from designing tail surfaces, which is what these fairings are. A fairing that is
cambered outboard and toed out would take its side force from the linear part of a curve that
has one, at no cost the frame does not already pay. This paper does not size that fairing,
because doing so on a curve it has not measured would repeat the error it has just described.
Supplementary S3 states it as the measurement this configuration would buy first.

## 2.11 Structure and ground contact

The tip frames are not added for the propellers. They are the landing structure.

This inverts a cost into a saving, and the inversion has precedent. Reviewing the
tail-sitters of the 1950s, NASA noted that "dispensing with a conventional landing gear
improved the empty weight fraction for these VATOL aircraft", while adding that some form
of gear was still required on the tail surfaces [2]. The present configuration takes the
same benefit and extends it: the structure that meets the ground is also the structure
that carries the control propellers and sets their moment arm.

The aircraft rests on five points: the four lower ends of the tip frames and a single
keel that runs aft along the centreline from the nose propeller to the trailing edge.
Because the aircraft stands on its tail, these five points are what it stands on, and
their spread is the stance base that resists tipping in wind. Lengthening the frames to
buy the control moment arm of Section 2.10 widens the stance base at the same time. One
structure serves three purposes — mounting the control propellers, providing the moment
arm, and carrying the landing loads — and is charged to the mass budget once.

The stance base is a design parameter, not a constraint imposed by the configuration.
Moving the frame ends further outboard widens it without altering the planform, the
propulsion, or the control architecture — and because the same displacement lengthens
the control moment arm of Section 2.10, the two benefits arrive together from one
change. The reference geometry given here is one point on that trade; an operator with
a stronger ground-wind requirement can take another without redesigning the aircraft.


## 2.12 Sizing method

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
e = 0.85; C_D0 = 0.0248 for the light design, which was taken as generous for a clean
blended-wing body on the grounds that it absorbs the tip-frame contribution of Section 3.3 —
0.0043, or seventeen percent of the assumed value. **Section 3.10 computes the coefficient and
that reasoning does not survive:** the computed bracket is 0.0285 to 0.0381 and the assumption
lies below both ends, so it is an assumption and an optimistic one, not a self-consistent
choice. It is carried unchanged so that every downstream figure rests on one stated basis, and
every result that depends on it is also reported across the computed bracket.

**Sea-level density is a deliberate choice and not an oversight, and it is the conservative
one.** A cruise at altitude would reduce drag with the density ratio and lengthen every range
figure quoted here; holding sea level therefore understates the aircraft rather than flattering
it. The choice also matches the intended missions — wildfire observation and cargo delivery to
sites without a runway — which are flown low, and it keeps the hover and cruise calculations on
one atmosphere so that the ratio between them, which is what the three bills are about, is not
carrying a density change as well. A design intended to cruise high would need the whole chain
re-run; nothing in the framework prevents that, and nothing in this paper does it. Section 3.10 computes both and reports what the computation does to them:
it bounds them rather than replacing them, which is a weaker but more honest claim.

## 2.13 Computational methods

Five computational tools produce the results of Section 3. Each is named here with what it was
asked for and what it was not; the results themselves, and the convergence and sensitivity
evidence behind them, are in Sections 3.10 and 3.17 and in Supplementary S1 and S4.

**Vortex-lattice.** A vortex-lattice solution of the planform of Section 2.8 supplies the
inviscid span efficiency, the neutral point from dC_m/dC_L, the twist required to trim, and the
roll damping from a helix-angle solution. It is used only for quantities that depend on the
spanwise circulation and the aerodynamic centre, which converge quickly; it is not used for
pressure distributions near the plan discontinuity, and no vortex-lattice result is quoted at
the transition incidences of Sections 3.12 to 3.17, where leading-edge vortex separation puts
the planform outside the linear method's range. A published comparison against RANS on a
blended-wing body of this class found the vortex-lattice lift coefficient low by thirty to
thirty-eight percent; Section 3.10 states what that does and does not disturb.

**Strip method with a section solver.** Zero-lift drag is built up strip by strip along the span,
with section drag coefficients from a physics-informed aerofoil model evaluated at each strip's
own chord Reynolds number and thickness. The same construction, called instead at each strip's
*local lift coefficient* taken from the vortex-lattice loading, gives the profile drag of the
trimmed wing and hence the Oswald efficiency. The section angle of attack that delivers a
required local lift coefficient is found by bisection rather than by linear interpolation.

**Reynolds-averaged Navier–Stokes.** A structured three-dimensional solution over the wing and
blended centre body, at the cruise Reynolds number and at zero lift, replaces the strip method's
weakest term — its treatment of a twenty-five percent thick centre body as a two-dimensional
section. The solution is fully turbulent. Its spread is quantified across three grids, four wall
resolutions, two turbulence closures and two initialisation fields, and the turbulence closure
dominates that spread.

**Point-mass transition simulation.** The transition is simulated as a two-degree-of-freedom
point mass. The body angle is driven kinematically from zero to ninety degrees over a rotation
time; thrust acts along the body axis, lift perpendicular to the velocity vector and drag
opposite to it; the lift curve is linear to stall and a flat-plate relation beyond it. **The
aircraft does not rotate in this simulation — it is assumed to rotate, and the moment producing
the rotation does not appear.** Whether the moment exists is a separate calculation, below.

**Rotational-authority and mass models.** A component build-up distributes mass over the planform
in proportion to the internal volume available to hold it, which fixes the centre of gravity and
the moment of inertia about the axis the transition rotates about. Two rotation profiles a finite
moment can produce — bang-bang and smooth — bracket the required moment, and the available moment
follows from the tip-pair thrust and the frame length.

Every script that produces a number in this paper is in the repository named in the Data
Availability statement, together with the convergence studies and a record of the calculations
that failed.

## 2.14 Use of artificial-intelligence tools

Large-language-model assistants were used during this study for three purposes, and the
distinction between them matters for what the reader should check.

They were used to **search and triage literature** — proposing candidate sources against a stated
question. No number or claim in this paper rests on a model's description of a source. Every
source cited was obtained as the original document and read by the authors before citation, a
rule adopted after search-derived summaries produced three incorrect values early in the study,
and one that has since caught two further cases in which a proposed source stated the opposite of
what it was offered for.

They were used to **check numerical work** — recomputing published arithmetic, auditing units and
cross-references, and questioning derivations. Several corrections recorded in Sections 3 and 4
originated this way, including the thrust-to-weight inconsistency of Section 3.15, the
station-mixing error in the buffer power of Section 3.4, and the misattributed comparative table
of Section 3.6. In each case the correction was reproduced independently from the underlying
model before it was adopted, and the reproduction rather than the suggestion is what is reported.

They were used for **language editing**.

No text was accepted without review, no result was generated by a model, and the authors take
full responsibility for the content of this publication. The prompts, the responses and the
resulting corrections are in the repository, so a reader who wishes to audit this use can do so
rather than take the statement on trust.
