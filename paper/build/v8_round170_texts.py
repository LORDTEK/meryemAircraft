# -*- coding: utf-8 -*-
"""Tur 170 taslak metinleri (adim numarali isaretcilerle). {TABLE} kaynak alt bolumdeki tablo(lar)la doldurulur."""

S1_ANSWERS = """Hybrid VTOL aircraft occupy that corner today. **This paper does not dispute that they work.** The NASA sizing study used in
Section 4 describes the two routes they take between the regimes: lift-plus-cruise aircraft keep two sets of hardware and switch
between them, and tilting aircraft keep one set and reorient it (Section 7). Rotating a propulsor in flight brings a pivot and its
actuators, a gyroscopic moment during the rotation, and a control problem through a regime in which the aircraft is neither a
rotorcraft nor an aeroplane. **Those are mechanical and control requirements rather than aerodynamic ones**, and that distinction is
what this paper is built on."""

S1_THIRD_P1 = """There is a third way to put one set of propulsors into both regimes without reorienting them: **point the
thrust line at the ground and let the whole aircraft rotate.** It is neither new nor untried nor abandoned.
The Convair XFY-1 flew it in 1954 and completed six transitions to conventional flight *"before testing was
curtailed because of engine and gear-box reliability problems"*, and uncrewed tail-sitters have revisited the
route since. The pilot's spatial orientation and workload were real, **but they are not what curtailed the testing**, and they are
the only one of those documented obstacles an uncrewed aircraft removes."""

S1_THIRD_P3 = """What has changed is electric drive on each rotor, sensor-based attitude reference and onboard computation, and **the
uncrewed tail-sitter literature has been exploiting exactly those three for over a decade**; the gap below is not a historical one."""

S1_OCCUPIED = """**The route itself is established.** Uncrewed tail-sitters combining fixed-pitch rotors with a
flying wing have been built and flown for more than a decade. A tail-sitter study reported in 2007 already states the
comparison: tilting configurations reach the same goal *"at the expense of significantly increased mechanical complexity compared to a
tail-sitter that uses propeller wash over normal aircraft control surfaces to effect vertical flight control."*

**Attitude without aerodynamic control surfaces is established**: a quadrotor tail-sitter operated without control surfaces, with
experimental verification, was reported in 2013.

**Coaxial contra-rotating propulsion on a tail-sitter is established**, proposed to cancel a single propeller's reaction torque without
complementary controls, at a cost its proposers name as added mechanical complexity; a tail-sitting micro air vehicle reported in 2014
uses a coaxial pair for the same purpose.

**The established answer to hover control on such a configuration is a surface in the slipstream**, and this paper refuses it. The 2014
vehicle places an elevon and a rudder in the propeller slipstream for three-axis control in hover; a flying-wing tail-sitter reported in 2018 uses elevons for two of its three axes and treats the propellers'
counter-moment about the thrust axis as a disturbance rather than a control channel, and reports hover and vertical flight only.

**And the reaction-torque channel this paper declines is established as a control channel.** A coaxial contra-rotating tail-sitter
reported in 2012 balances rotor torque by counter-rotation and unbalances it on purpose to steer: its published control scheme assigns
*"differential velocity of the two motors"* to yaw in the vertical mode and to roll in the horizontal one. **Those are the same physical
channel under two names**, a moment about the propeller axis, and independently driven rotors make it available to any coaxial pair.
**Using it is a choice, and so is declining it**, which is what separates this configuration's control problem from a physical
impossibility.

**A blended-wing-body tail-sitter with contra-rotating propulsion, aimed at disaster response, is established**, reported in 2025 with vortex-lattice and RANS analysis.

**A buffered series hybrid on a winged tail-sitter has been sized**: a 2026 study of 100 kg winged biplane tail-sitters sizes the engine
for cruise and a boost battery for vertical take-off and landing, and gives its rotors collective pitch change mechanisms.

**A coaxial tail-sitter with a series-hybrid store has been sized**: a long-endurance concept reported in 2025, with a fuselage and
tails, whose fuel cells charge a battery that drives the motor, because the fuel cell alone cannot fully power hover out of ground
effect at take-off; how its attitude is controlled, and whether its rotors vary pitch, the paper does not state.

**And the propeller compromise at the centre of this paper's own ledger is a known result, not a discovery.** The uncrewed tail-sitter
literature states that fixed-pitch propellers make it *"theoretically impossible to be very efficient in both hovering and forward
flight."* A long-range tail-sitter reported in 2018 names variable pitch as the remedy, at the cost of extra actuators and mechanism weight, and even with cyclic and collective pitch still sizes its rotor as a compromise between hover and forward flight."""

S2_RETRACTION_NEW = "One of these transfers has direct experimental support (Supplement S2)."

S3_DOESNOT = """**It means zero of the three charges as Section 2 defines them.** **It does not mean an architecture that costs nothing, and it does not mean an architecture that carries nothing for the vertical phase.** A definition that placed every conceivable cost inside the thing to be escaped would be unfalsifiable. Six costs are permitted, named here before any candidate is examined (the working is in Supplement S3):

- **A store is permitted**, though it is mass carried for a duty that is briefly needed, which is the complaint Bill 1 makes. **It does not claim the trade is favourable**: whether the store is lighter than the continuous power it displaces is computed, not asserted.
- **Releasing the engine is not releasing the electrical path.** Machines, power electronics and wiring still pass the full hover power, and that Bill 3 is carried in the ledger.
- **Rotating the airframe is permitted and is not priced here.** An architecture that rotates its whole body still turns its thrust axis through ninety degrees relative to the flight path, with the moments and the control through the turn that implies; that is not one of the three charges, and it is priced where the transition is analysed.
- **Hardware installed for the vertical phase is permitted if it serves both duties.**
- **Hardware used in both regimes for something other than propulsive thrust is permitted, and its cruise drag is not eliminated.** *Cruise thrust in this paper means the thrust that balances cruise drag.* Attitude devices produce none; used throughout the flight, they fall outside Bill 1, and they do not stop the propulsor that carries the aircraft from meeting the condition. But carried through cruise without producing cruise thrust, they are the first failure mode below, and Bill 2 reaches them.
- **Serving two regimes with one set of hardware has a price of its own**: a fixed geometry cannot be optimised for both, and the compromise is paid in efficiency. **The condition permits that cost and does not measure it.** Section 11 does.

**One exclusion, stated narrowly.** Structure, surfaces and actuation present for reasons other than the vertical phase are not charged **as duty-cycle mismatch under this accounting**, which says which ledger they belong in, not that they are free; it does not reach a part that would not exist but for the vertical phase. The tip frames of Section 5 are landing gear because the aircraft stands on its tail: **their mass is charged in the build-up and their drag in the ledger.**"""

S5_SIZED = """**Sized.** The vertical phase is sized: hover power from momentum theory at thrust equal to weight, the buffer that supplies what
the engine cannot deliver of that peak (at a specific power Section 14 examines), the tip-frame lengths that set both the stance base
and the control arms, and the structure that carries the landing loads. Section 10 reports **whether** they close. This section does
not assert the outcome of a calculation it does not contain.

**Not demonstrated.**

**The aircraft leaves the ground on its tip pairs.** The nose pair is sized at thrust equal to weight, so the take-off margin comes
from the four tip pairs, which were sized from the moment requirement. That is the one place the configuration asks a component to do
a second job it was not sized for, and it means the take-off margin and the attitude authority are drawn from the same propellers and
compete for it.

**The vertical descent and the landing transition have not been analysed.** Whether the descent enters the vortex ring state is an
open question in Supplement S14; the landing transition is not the take-off transition run backwards, and no figure in this paper
describes it (Supplement S5).

**Hover attitude control is sized but not demonstrated as a closed loop**: the moments about each axis are computed, and no control
allocation has been closed around them. This configuration also declines the reaction-torque channel that comparable aircraft use
about the body's longitudinal axis (Section 8). **What that refusal costs in authority and in response time is not computed**, and
Supplement S14 carries it.

**And one historical difficulty is inherited rather than removed.** A tail-sitting aircraft on
the ground is more prone than a conventional one to tip over, in crosswind and on uneven ground. The stance base is the answer
this configuration offers, and it is a parameter rather than a proof."""

S6_MARGIN = """The sizing set of Section 4 reports an **effective lift-to-drag ratio**, `L/De = WV/P`: a system figure of merit that already
contains the propulsive efficiency of whatever produces the thrust, so **a force ratio cannot be placed beside it.** In level cruise,
with shaft power `P = DV/η_p`,

> **L/De = WV/P = (L/D) · η_p**

**Which power `P` denotes is not assumed here**, because reading it as electrical rather than shaft power would make this
configuration's figure incomparable with the published one. The source writes hover power with the figure of merit applied, which is
shaft power, and applies the propulsion-system efficiency separately, for the all-electric entries as for the shaft-driven ones.

The aerodynamic ratio is **8.79 to 10.82**, with the tip frames and the free-wheeling tip-pair rotors (Section 8) already charged; that
spread is **uncertainty**, the zero-lift drag bracket. The cruise propeller efficiency is **0.632 to 0.683** across the nose-blade
families that meet the hover figure of merit; that spread is **not uncertainty** but a design variable this study has not fixed.

{TABLE}

**These are the bounding corners of a product, not four simulated aircraft.** Across the examined envelope they give **5.56 to
7.39**; for the best examined blade family, at 0.683, **6.00 to 7.39**. Which blade a designer would choose also turns on structural
loads, acoustics, the motor operating point, rotor inertia and manufacture, **none of which is modelled in this work** (Supplement S6).
Section 10 carries one blade into a closed sizing loop; until then no corner is presented as the aircraft's performance."""

S6_COMPARISON = """The sizing set contains two quadrotors for the same mission, and **neither is treated here as the primary one.**

{TABLE}

**Against the turboshaft quadrotor the sign holds at every corner of both readings**; closing it would need a propeller efficiency
of 0.557, against 0.632 for the least efficient blade family examined.

**Against the all-electric quadrotor it does not hold at the low corner**, and that result is reported as a result rather than as a
caveat. That vehicle reaches 5.8 with 1 742 lb of battery and nearly twice the gross weight for the same mission, 7 221 lb against
3 678 lb. **That higher gross weight is consistent with the mass charge Section 2 describes**; this table alone does not establish the
causal link, and Section 4 sets out the independent evidence for it.

The same sizing set gives four entries for its two helicopter types, at 5.4 to 7.2, and against them the result is
mixed: this configuration is ahead of the turboshaft single-main-rotor helicopter at every corner,
the two middle entries fall inside its envelope, and only its top corner is ahead of the
all-electric side-by-side helicopter, which has no wing either. The qualifications below apply to them too.

**So the second claim is narrower than the structural statement invites**: carrying cruise lift on a wing is worth roughly an eighth
to a half against the turboshaft reference, and against the all-electric one it ranges from slightly behind to comfortably ahead
depending on the drag outcome and the blade — a measurable advantage, not a change of category. What compresses it is the cruise
efficiency of the fixed-pitch blade: at a propeller efficiency of 0.85 the same airframe reaches 7.47 to 9.20. Whether a
variable-pitch hub would recover that difference is not computed; Section 11 reports the gap and declines to attribute all of it to the hub."""

S6_FIVE = """

**Scale.** The compared vehicles are larger than both designs here, of order 50 kg and 1 000 kg (Supplement S6), and **Reynolds number
favours the larger aircraft**, so the smaller design is at a disadvantage in this comparison rather than an advantage.

**The quadrotor is a good quadrotor**: both quadrotors have unusually low disc loadings. **Nothing here is compared against a poor
example.**

**The speeds are not matched, and the direction of that mismatch is calculable.** The reference is quoted at its best-range speed, this configuration at its cruise condition, 1.49 times stall, rather than at its best point, 1.26. **The reference is therefore given its best speed and this configuration is not given its best speed, and the margin is
positive anyway.** **The best point is not an available option** — cruising there leaves too little margin above the stall — **so this
fixes a direction, not a magnitude.**

**The atmospheres are not matched.** The published sizing mission is flown at *"5,000-ft altitude and ISA + 20°C"*; every number in
this work is at sea level. **The direction of that mismatch is not claimed here**, because it has not been computed.

**The analysis chains are not matched, and this is the qualification that bounds what the comparison can be called.** The published value comes from a fully sized vehicle in an integrated design system; the value here is a converted metric at a prescribed cruise condition, taken before the sizing closure of Section 10. So this is a comparison of two
independently produced figures in a common definition, not a controlled numerical reproduction, and nothing in it should be read as
validation of either, or as a completed aircraft-level comparison."""

S6_SIZED = """**Sized.** The drag build-up and its bracket, the lift-to-drag ratio from the drag polar, the propeller efficiency from
blade-element momentum theory at two operating points, and the range that follows from the chain.

**Not demonstrated.** **No part of this has been measured**: there is no wind-tunnel or flight test in this work, and the drag
coefficient is a build-up with a declared bracket. The planform was chosen rather than optimised. **The span efficiency used
throughout this section is the computed value, 0.817, not the assumed 0.85**, from a vortex-lattice solution of the trimmed planform.
And for the methods used here, and for the published comparisons against which they were checked, **the aerodynamic predictions
diverge above roughly ten degrees of incidence**: three methods of three fidelities depart at the same place, the highest of them
against wind-tunnel measurement. That is a statement about these methods on this class of configuration, not about what any method
could achieve; it does not touch the cruise numbers above, which sit at a few degrees, but it bounds what this section may be read to
support, and the transition of Sections 7 and 10 passes through that band."""

S6_COSTS = """The wing that makes cruise efficient is carried through the vertical phase, where it produces nothing and presents the aircraft's
largest surface to ground wind; the tailless planform constrains the sweep; and the fixed-pitch propeller is why the margin above
sits where it does. Section 11 charges the third. The first two are inside Section 10's closed numbers but are not separated out as
charges, and the wing's exposure to ground wind is not priced in this work.

**The two halves are now on the table separately. Section 7 is where they are combined**, and
the combination is what this paper is for."""

S7_BODY = """None of the three elements is new. **Each can be found on its own, and some of them
together, in the literature and in hardware** — Section 1 says where. The principle behind the third element — a continuous plant sized for cruise, with the vertical or take-off peak drawn from a store — has been applied in studies of a winged tail-sitter (Section 1) and of a single-aisle airliner reported in 2016 whose turbines are *"sized for efficient operation during"* cruise and assisted by electric motors *"during takeoff and climb."*

**What this paper contributes is the architecture that brings the three elements together; the
condition shows what it satisfies, and the price shows what it costs.** The three elements, taken together, meet the escape condition
of Section 3 **in the propulsor that carries the aircraft**, and they meet it with no mechanism
that reorients a propulsor. The assembly is not offered as novel because it is an assembly. It is
offered for what it satisfies, and for what it does not need in order to satisfy it.

**The qualification "in the propulsor that carries the aircraft" is not decoration.** The single nose pair meets all four parts of
the condition. The four tip pairs do not: they are exposed in the cruise flow and cannot be feathered, so they re-open the second
charge. **The instantiation is therefore partial**, the case Section 3 lists among the ways to fail, and reporting what the failing
part costs is a substantial share of what Section 11 does.

Each element supplies one part of the condition, and none supplies it alone:

- The **blended wing body** carries the cruise lift on a surface.
- The **tail-sitting stance** aligns the thrust axis with the body axis, so one propulsor produces the thrust for vertical operation
  and for cruise, in one orientation relative to the airframe; there is no dedicated lift system, and vertical operation needs no runway.
- The **series-hybrid buffer** releases the continuous plant from the hover peak, so that it is sized by cruise; the series
  arrangement is chosen for the electrical path it gives the buffered peak, not because it is assumed to be the more efficient hybrid.

**The configuration is arranged to change regime by rotating the airframe. The propulsors hold their orientation relative to the body
from take-off to cruise; what changes is the orientation of the body relative to the flight path.** The contemporary hybrids reach the
same end otherwise. The lift-plus-cruise design of the NASA study used in Section 4 carries its lifting rotors through cruise, stopped
and aligned with the stream, and flies on a separate pusher; its tilt-wing turns eight proprotors, each on its own motor, on a tilting
wing and tail, which takes a pivot and actuators and brings a gyroscopic moment and a control problem through the turn. Turning the
propulsors is the case the condition excludes; turning the thing they are attached to leaves the orientation requirement intact.
**That single move is what removes the need for the mechanism.** The table counts the mechanism classes that exist in order to change
regime, or to take a rotor out of one regime's flow; the strip of Section 8 is a control surface, of a different class, and is named
below. The configuration therefore carries:

{TABLE}

Attitude comes from differential thrust between the fixed-pitch pairs: the moment arms of the four tip pairs give pitch and yaw. The tip
pairs are sized from the moment requirement, but because the nose pair is sized at thrust equal to weight and no more, they also supply
the whole take-off margin; that dependency is reported in Section 5, and it does not make them a dedicated lift system.

**The claim is narrower than it may appear.** **This is not a configuration in which nothing moves.** Roll cannot come from the
propellers' thrust, since every thrust vector is parallel to the body axis; it could come from their reaction torque, and this
configuration declines that channel by design (Section 8), assigning the axis to the only moving aerodynamic surface on the aircraft: a
variable-extension strip on the lower surface, modulated rather than switched, which also pitches the nose down slightly when deployed.
It is named here because a claim about eliminated mechanisms that omitted it would be false. A fixed-pitch blade that serves both
regimes is at its best in neither; that is a price of refusing the variable-pitch hub, charged in Section 11. **Nor is this a claim of
mechanical simplicity**: what is offered is a count of the mechanism classes a tilting architecture needs to change regime and this
arrangement does not, and the actuator inventory that replaces them is the propulsion motors together with the strip.

**Whether this aircraft can actually perform the change is a separate question and is not settled anywhere in this paper**: whether
the moment available suffices, and whether the aircraft trims through the rotation, depend on aerodynamics that the methods used here do
not predict reliably in the band the rotation passes through (Section 6). **The mechanism claim is about hardware and survives that
limit. The transition claim is not made.** Section 15 holds the paper to that."""

S8_AIRFRAME = """The entire airframe is the wing: there is no cylindrical fuselage, and every part carried also lifts. Leading-edge sweep varies
along the span while the trailing edge is held at 25°, from 45° at the root to 38.3° at the tip. For the 50 kg reference design, which
this inventory describes, the span is 3.453 m, the wing area 1.979 m² and the aspect ratio 6.03. The aircraft is tailless, so the
pitching moment must come from the distribution of lift along the body itself, and sweep is what places the outboard sections behind
the centre of gravity so they can produce it: **the sweep angle and the longitudinal stability are one design variable seen from two
directions.**"""

S8_PROPULSION = """**Five propeller stations, ten rotors:** every station is a coaxial counter-rotating pair, because of **reaction torque.** A single
propeller applies to the airframe a torque about its own axis, which on this aircraft is the body's longitudinal axis — the roll axis
in body terms — in both regimes. It must be opposed continuously, either by a control surface, which costs drag, or by the reaction
torque of other rotors run at a different speed, which costs a control channel. A torque-balanced counter-rotating pair does not
produce it. *(This paper fixes body-axis naming throughout. That axis is the roll axis in both regimes; what changes is its orientation relative to the earth — it stands vertical in the hover attitude, where a moment about it appears as a change of heading, and horizontal in cruise, where it appears as a bank. The two conventions are not mixed here.)*

One pair sits at the nose, 1.20 m in diameter on the 50 kg reference design, and produces all propulsive thrust in both regimes; four
pairs of 0.20 m sit at the ends of rigid frames projecting from the wing tips. Every pair is of **fixed geometry**: no cyclic or
collective pitch, no variable-pitch hub and no mechanism that changes a rotor's orientation relative to the airframe. Shaft speed is
commanded; blade geometry and orientation are not. Each rotor has its own electric machine on a common axis, so no splitting gearbox
or mechanical governor is required. This work makes no claim about the shafting.

**At equal counter-rotating speeds, the net angular momentum of the propulsion system is nominally zero**, so rotating the airframe
through ninety degrees produces no gyroscopic moment for the control system to cancel; if the pairs are speed-trimmed, that
cancellation is no longer exact (below). In a tilting architecture that term is present and must be designed for."""

S8_MOMENTS = """**Pitch and yaw come from differential thrust between the tip pairs** (body axes, as fixed above). The frames project ±0.71 m
from the planform, so an upper–lower differential acts at 0.71 m in pitch and a left–right differential at the semi-span, **1.726 m —
2.43 times the pitch arm**, a consequence of the layout rather than a design choice. The authority each axis has depends also on the
available thrust differential and its allocation. **The same differential-thrust system is what is assigned to rotate the airframe
through transition.** That is a design assignment, not a demonstrated result (Section 7): the moment it produces is a sizing input to
Section 10, and whether it suffices is **not settled in this paper**.

**Roll comes from neither, and the reason is a choice rather than an impossibility.** No combination of thrust settings produces a
moment about the body axis, and the reaction-torque channel that could (Section 1) is declined: every pair is operated
torque-balanced. What declining it costs is not counted in this work. Roll comes instead from a strip on the lower surface (its
geometry is in Supplement S8). **Extension is the control variable** — the strip is modulated, not switched — and deploying it also
pitches the nose down by a small increment. Its inboard 46 % lies inside the nose propeller's slipstream, where dynamic pressure is set
by disc loading and is available at zero airspeed, and its outboard 54 % works against the freestream in cruise, which is why one
device serves both regimes. The split is an estimate: the slipstream boundary it rests on is not derived in this work."""

S8_GROUND = """The aircraft rests on the five points of Section 5. **The frames carry a fairing, and it is not only a drag measure**: a planar
planform supplies no directional stability, so the fairing is the aircraft's only vertical surface, and sized against the criterion
the tailless literature recommends it needs a chord of **39 mm**, less than a 20 mm faired strut carries in any case (Supplement S8).
Directional stability on this configuration therefore does not ask for a surface; it asks for a fairing on a frame that is already
there. An attitude reference and a flight computer are part of that mechanism rather than optional equipment, because stability is not
airframe-borne alone; they are carried in the systems budget."""

S8_MOVES = """The propellers rotate at commanded speed, but none changes its orientation relative to the airframe, or its blade pitch, at any
point in the flight. **Beyond the propellers' rotation, one thing on this aircraft changes its configuration: the strip**, deployable in
two halves — one side alone for roll, both together as a speed brake. The actuator inventory is therefore the propulsion motors plus the
strip's actuation. **How many actuators that is, this study does not fix**; the systems budget carries the actuation without sizing it.

**The tip pairs are the parts that fail the escape condition** (Section 7): sized for moments and used for them in both regimes, they
add the take-off margin but were not sized for weight support, and Section 3's permitted-cost clause places them outside the first
charge while leaving them in the airstream."""

S8_NOTSETTLE = """**An untrimmed hover torque, with no trim mechanism identified.** Each pair's torque balance is set exact at the cruise condition,
so a small residual about the propeller axis remains in hover. That is the axis the configuration chose not to command with the
propellers: the tip pairs cannot absorb it by thrust differential, and the strip has slipstream over only part of its length at zero
airspeed. What is left is the speed trim of the pairs, a reaction-torque command. Either the residual is small enough to be absorbed
that way, which this study has not shown and which would mean the architecture spends a little of the channel it declined, or another
duty falls on the strip.

**The fixed geometry of the tip pairs leaves two admissible cruise states**: turning at zero shaft torque, or stopped. This
configuration uses the first: free-wheeling at zero shaft torque is the tip pairs' uncommanded cruise state and the drag state Section 11 charges; the shaft power of commanded departures from it, for attitude moments in cruise, is not computed. **The free-wheeling
state is physically determinate: the rotor settles where net shaft torque is zero. The stopped state is not**: the stop must be
produced by something — motor holding torque, an electrical brake, a mechanical lock — and a stopped fixed-pitch blade also has an
azimuth, so the stopped-state drag estimates (Supplement S11) should be read as estimates for an assumed azimuth rather than as the
state a particular installation would reach. If the stop were a brake or a lock rather than motor holding torque, the count of Section 7
would gain a class."""

S10_INPUTS = """**The zero-lift drag coefficient is uncertainty:** the build-up of Section 11 places it between 0.0285 and 0.0381, and a designer
does not choose where the real aircraft falls. **The blade family is a design variable this study has not fixed:** four nose-blade
families that meet the hover figure of merit span cruise propeller efficiencies of 0.632 to 0.683. **The reference design's assumed
zero-lift value of 0.0248 is not used**: it lies below both ends of the bracket.

Wing loading, disc loading and aspect ratio are held fixed, so **the cruise lift coefficient is 0.450 in every closure** (Supplement S10). The tip frames, tip discs and strip were set on the 50 kg reference design of Section 8, and **the control moment arms of Section 8 are therefore reference values that this closure does not re-derive.** **These are the same configuration at four closed masses
rather than four configurations**, with anything that depends on the arms carried at the reference geometry. Run on the reference
design's own assumed inputs, the same construction reproduces that design within 1.5 percent (Supplement S10), so the closures report
a change of inputs, not of method."""

S10_CLOSURES = """**On these assumptions all four converge**, for the 50 kg design — the only one carried through this loop.

{TABLE}

Payload is fixed at 13 kg and take-off mass is the output. **The blade that is best before the loop is still best after it**, though a
loop can reverse a local ranking: at both ends of the drag bracket the higher-efficiency family closes to the longer range — **a result
of the closure rather than an assumption carried into it.**"""

S10_TRANSITION = """The sizing above says nothing about whether the aircraft can change regime. **The question is asked in two models, only the
second of which carries rotational dynamics, and that one does not support a zero altitude loss.** Both use the reference designs at
their reference masses and assumed drag, not the closures. A point-mass model with the body angle driven kinematically loses no
altitude in a rotation entered in a 5 m s⁻¹ climb, at the reference rotation times of 2 s for the 50 kg design and 5.1 s for the
1 000 kg one. Solved with rotational dynamics and a finite control moment, **and with the aerodynamic pitching moment set to exactly
zero, so that nothing favourable is borrowed**, the 50 kg design **loses 5.4 to 6.6 m at the same reference condition**; the loss is
not an artefact of the controller (Supplement S10). **What the kinematic model leaves out is not the difficulty of turning the aircraft
but the trajectory the aircraft flies while it is being turned.** **So the zero-altitude-loss result is a property of the model that
produced it.**

A prediction would need the aerodynamic pitching moment, and the methods used here diverge in the band the rotation passes through
(Section 6); with a borrowed moment some models complete the rotation, some saturate the tip pairs, and some tumble. **That spread is
itself the finding.** **Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude.**
Whether a real aircraft loses 5.4 to 6.6 m, more, or less is not settled by anything here."""

S11_INTRO = """This section says where each charge of Section 2 appears inside the closed numbers of Section 10, and how large it is there.
**It attributes. It does not add.** Every cost named below is already inside the closure of Section 10. **No new physical cost term is
introduced here.** **And there is no single figure for what the architecture costs**: the charges are in three currencies, and **no
scalar aggregate is defined, because this study has no defensible weighting between them** (Section 13)."""

S11_BILL2 = """In the drag build-up behind the bracket (line items in Supplement S11), **the hardware exposed by the vertical-phase layout — the
tip frames and the free-wheeling tip-pair rotors — is 69 percent of the zero-lift drag at the favourable end and 57 percent at the
adverse one**; the rotor term alone is 0.0154 at the favourable end. **The rotor line rests on section drag at low Reynolds number**,
on section polars computed rather than measured (Section 12). **The tip-frame term is an attribution, not a marginal removal cost**: it
is not a claim that this drag would disappear if the vertical phase did. **No stopped-state counterfactual was computed**: the eight
tip discs stopped edge-on are estimated at ΔC_D0 = 0.0008 (Supplement S11), but that takes an indexing mechanism, a class Section 7
counts, which has not been sized, charged or closed.

Without the hub and small items, the tip frames and the rotors, the clean body reaches a lift-to-drag ratio of 20.55 at the favourable
end and 15.24 at the adverse one, against the aircraft's 10.82 and 8.79: **the configuration retains 52.6 and 57.7 percent.** Bill 2
therefore occupies a larger share where the clean-body drag is lower — a statement about position within the drag bracket at one
scale, not about size (Section 12).

**Rotor–structure and rotor–wing interference is not modelled and is not carried as a line.** Section 2 quotes a wind-tunnel finding
that a simulation neglecting it predicted higher lift and lower drag than were measured; this build-up is such a calculation, and the bracket's
upper margin is the only provision made for it."""

S12_BODY = """Section 11 decomposed the three charges on one aircraft, at one size; **this section asks whether they are three quantities or
one quantity under three names**, by changing the size of the aircraft and seeing whether they move together. Either answer leaves the
mechanism claim where it was. **The test is deliberately weak**: it can show that two charges are not locked together within this
model; **it cannot show that they are independent in general.**

**The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 10's closures**: no closure was run at
1 000 kg, the heavy design has no drag bracket and no structural closure, and no heavy-design range is quoted (Supplement S12).

**Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its light-design value in the section
polars used here, while specific hover power changes by one percent and the Bill 3 ratio by 5 to 14 percent.** Bill 2 moved by more
than the Bill 3 ratio at every point in the heavy interval and under either engine margin. **Within this model, the two are therefore
not one quantity under two names.** Disc loading is held nearly constant, so specific hover power is held with it: **that
near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3.** The rule is paid in geometry, and **much
above 1 000 kg a single nose pair can no longer hold the disc loading.**

Only the rotor term of Bill 2 is computed at both sizes; the frame term enters both designs as the same multiplier. Within the
blade-element and section-polar model the section Reynolds number accounts for the fall, a decomposition inside the model rather than
a causal claim beyond it, and the light end lies below a Reynolds number of 10⁵, where section drag is hardest to predict. **Of the two
rotor terms, the light one is therefore the less certain — and it is the one Sections 10 and 11 carry.**

**Bill 1 is not tested.** It appears here as the energy buffer, 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and
both figures are inputs: **a change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be
offered as evidence that Bill 1 moves with size in either direction.** Whether it is separable from Bill 3 here is not established;
that the two are coupled here is Section 3's claim, and coupling is not identity.

**The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low
Reynolds number.** **It is consistent with the separability Section 2 asserts; it is not a verification of separability as a general
property.** **The transition is where the square–cube relation is paid in full**, and **a larger aircraft of this type turns more
slowly, and must** (Supplement S12).

**Because at least two of the charges are not locked together, a comparison of architectures cannot in general be reduced to a number
that does not depend on how the charges are weighed.** Section 13 examines what the choice of sizing contract does to a ranking, on the
light closures of Section 10 only."""

S13_INTRO = """Where one architecture pays less of one charge and more of another, the ranking depends on how the charges are weighed
(Section 12), and **a sizing contract is one such weighing**: it fixes what is held equal between the architectures being compared.
This section applies three contracts to three architectures at each of the four closures of Section 10. **The mechanism claim is not a
ranking and is not at stake here.**"""

S13_CONTRACTS = """Range in the sizing loop is proportional to L/D, to the energy chain and to the fuel fraction, and the three contracts differ
only in the last (Supplement S13): a **fixed fuel fraction**, sixteen percent of each architecture's own take-off mass; a **fixed fuel
mass**, the 8.4 to 9.2 kg this configuration carries; and a **fixed take-off mass and payload**, under which every kilogram of
architecture-specific hardware is a kilogram of fuel not carried. **These are three different questions, not three estimates of one
answer**, and this paper has no mission that would decide among them."""

S13_BASIS = """Three architectures fly the same mission, 13 kg of payload at 30 m s⁻¹, with the same wing loading, disc loading and aspect ratio,
the same airframe and avionics fractions, and the same energy chain apart from the propeller. **The competitors are therefore this
planform with two add-ons, not independently designed aircraft of their families.** All three carry the same buffered series-hybrid
power system, so Bill 3 is held common and the comparison measures mass and cruise drag. **Holding Bill 3 common is a choice of
question, and it has a direction.** **The choice runs against this configuration**: without the buffer, and with engines rated to the
hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off mass (Supplement S13).

The basis is not symmetric. The lift-plus-cruise layout carries a lift-to-drag ratio transferred from a different airframe's
wind-tunnel campaign (Section 2), and its stopped lift rotors take an indexing mechanism (Section 7) whose mass is not charged. **The
tilting layout carries no cruise drag penalty at all. That is an idealisation in its favour**, and it makes the tilting layout a bound.
Both competitors are given a propeller efficiency of 0.80, assumed, against this configuration's computed 0.632 and 0.683, and a lift
group of 10 percent or a tilt mechanism of 5 percent of take-off mass. **Neither figure is measured.**"""

S13_PREDICTION = """Section 2 predicted that such a ranking will move when the sizing rule changes, and can reverse. **The movement holds
everywhere**, against both competitors, toward the lighter arrangement as the contract weights mass more; **the reversal holds at two of
the four closures against lift-plus-cruise, and at none against the tilt bound.** Where it falls is decided by quantities this study
has not measured or fixed: the blade family in the base case, and across the sensitivity cases the competitor's lift-group mass and the
propeller basis (Supplement S13). With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every
closure; with a heavier one this configuration leads under a fixed take-off mass at every closure; with a common propeller efficiency
a reversal appears at every closure. **Which architecture ranks first under a fixed take-off mass is therefore decided, in this model,
by quantities this study assumes for the competitor rather than measures: its lift-group mass fraction and its propeller efficiency.**
**Put plainly, the sign under a fixed take-off mass is not a result about the architectures; it is a result about those quantities.**
What is robust is that the shift exists and runs toward the lighter aircraft."""

S14_STORE = """**Every closure in Section 10 carries a buffer of 3.6 percent of take-off mass.** Taken at the
electrical bus, **the four closures ask the buffer for 4.7 to 5.2 kW per kilogram of buffer to hover, and 5.5 to 6.1 kW per kilogram of
buffer to leave the ground** with the tip pairs at full thrust (Section 5).

**What has been measured is a fraction of that, and the store figures available are of four different kinds.** A pack flown in a 210 kg-class electric VTOL aircraft is rated, as a flown system, at 0.892 kW per kilogram continuous; its
unit pack, discharged on the bench at its highest tested rate, delivered on average about 1.5 kW per kilogram (Supplement S14). A
NASA-funded design study adopts 4 kW per kilogram and describes that figure as about twice that of existing batteries. The same study
notes lithium-polymer figures in the literature as high as 3 kW per kilogram, which it cites rather than measures; against that figure
the take-off demand is 1.8 to 2.0 times. The study argues that, because pulse current limits can exceed continuous ones — by more than a
factor of two in one commercial module it cites — a pack with the required specific power may be possible with existing technology; its
hover lasts twenty seconds or less, while this aircraft's vertical phases occupy about a minute in all (Section 2), and how long each
draws the peak is not computed here.

**The take-off demand is 3.7 to 4.1 times the bench rate — the highest figure obtained from a measurement — and 6.2 to 6.8 times the
flown system's continuous rating.** The comparison is between unlike ratings. **The gap is real on every one of them;
the factor quoted is peak demand against bench average.** The package Section 10 closes on does not exist with any store the sources
consulted here report as built; closed again at the bench rate, it becomes 76 to 81 percent heavier, a sensitivity with one input
changed rather than a structural closure (Supplement S14).

**This is where the coupling Section 12 found is paid**: the buffer converts kilowatts of hover peak into kilograms of store. **The
escape from Bill 3 is real in the sense Section 3 defined it, and its price depends on a component whose required performance has not
been demonstrated.**"""
