# 3. The architectural tax of hybrid VTOL

Hybrid VTOL aircraft work. The argument of this section is not that they do not, but
that they pay for the capability in a way that can be located precisely, that the
payment appears in three different currencies, and that an improvement in one currency
is usually a transfer into another rather than a reduction. The section closes by
stating the condition under which the payment would be zero — a condition none of the
current architectures satisfies, and which Section 4 is built to satisfy.

## 3.1 The root: a duty cycle that does not match the hardware

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

## 3.2 Bill 1 — mass

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

## 3.3 Bill 2 — drag

The second payment is charged only to architectures that leave hover hardware exposed in forward
flight: rotors stopped in the airstream, the booms that carry them, and the interference between
their wakes and the wing.

The cleanest measurement is a controlled comparison within a single aircraft. In a doctoral
study, one uncrewed airframe was tested in a wind tunnel in four configurations:

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
(Figure 12).

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

## 3.4 Bill 3 — power system sizing

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

## 3.5 The bills are one quantity in three currencies

The three bills are not independent problems with independent fixes. **Each known architectural
move reduces one and increases another.** Figure 3 shows the transfers; Table 1 lists them.

**Table 1.** Architectural moves and the bills they transfer.

| Move | Bill it attacks | Bill it creates |
|---|---|---|
| Distributed electric lift rotors | 3 — the cruise engine no longer sizes to hover | 1 and 2 — many rotors and mounts, permanently carried and exposed |
| Folding or retracting lift rotors | 2 — the exposed rotor is removed from cruise | 1 — mechanism, actuation, locking, a new failure mode |
| Tilt-rotor, tilt-wing, tilt-nacelle | 1 — one propulsion group serves both regimes | mechanical complexity, gyroscopic coupling, a transition control problem |
| Higher disc loading, smaller rotors | 1 and 2 — smaller, lighter, cleaner rotors | 3 — hover power rises with √(DL) |
| Lower disc loading, larger rotors | 3 — hover power falls | 1 and 2 — larger structure and exposed area |

**One of these rows has been measured.** In the study of Section 3.3, the retraction system that
removed thirty percent of the drag was then costed: applied to a passenger eVTOL with the
mechanism assessed at five percent of vehicle mass, maximum range rose from 119 km to 121 km —
**a two-kilometre gain for a five-percent mass penalty.** Bill 2 was converted almost exactly
into Bill 1, and the transfer is the point rather than the small residue.

## 3.6 The condition under which the three bills are not charged

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
pays instead is a separate question, and Section 5.4 answers it for the configuration
proposed here.

That is a description of a tail-sitter with a buffered series-hybrid powertrain. It is
also, precisely, the configuration described in Section 4.

## 3.7 The three bills stated formally

Supplementary S6 states the three bills as equations and gives the transfer table that shows
them to be one quantity in three currencies: a design that refuses to pay one of them pays it
in another. The short form is that each bill is a fraction of take-off mass, exposed cruise
drag, or installed continuous power, and that the three are linked by the sizing loop — mass
drives thrust, thrust drives power, power drives mass — so that relieving one without relieving
its cause simply moves the charge.

**A consequence that can be checked against published work.** If the framework is right, then
for the same mission a configuration carrying a dedicated lift system should pay for it in gross
weight, and that payment should *not* be recovered by the cruise efficiency the arrangement buys.
This is a sharper prediction than it first appears, because it forbids the obvious defence: it
says the efficiency gain is real and still insufficient. The NASA sizing set is a direct test of
it. Against a common mission of 1 200 lb of payload over 75 nautical miles, the turboshaft
quadrotor — which has no cruise wing, and therefore no dedicated lift hardware to carry — sizes
at an effective lift-to-drag ratio of 4.9 and a design gross weight of 3 678 lb, while the
turbo-electric lift-plus-cruise reaches 8.5 and weighs 7 271 lb [22]. **Its cruise efficiency is
seventy percent better and it is nearly twice as heavy**, which is the prediction and not a
counter-example to it. The tilt-wing in the same set reaches 8.6 — higher than every
lift-plus-cruise entry — while carrying no dedicated lift system at all, and it is the one
configuration in the table that uses the same hardware in both regimes. The framework does not
predict the numbers; it predicts that the weight charge survives the efficiency credit, and in
this set it does.

**What the framework does not claim.** It does not claim that avoiding the three bills makes an
aircraft better, only cheaper in those three specific currencies. A configuration may avoid all
three and still be unbuildable, uncontrollable, or unsuited to its mission — and Sections 7 and
8 are about exactly that possibility for the configuration proposed here. Nor does it claim the
bills are the only costs; they are the ones that follow from the duty-cycle mismatch of Section
3.1, and a design pays many others.

## 3.8 Why the market looks the way it does

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

