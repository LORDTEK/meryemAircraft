# 3. The architectural tax of hybrid VTOL

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

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

The most direct payment is dead mass. A lift-plus-cruise aircraft carries two
propulsion groups: rotors, motors, mounts, wiring and structural reinforcement for the
vertical phase, and a separate propulsor with its own installation for cruise. The
vertical group is inert for the whole cruise, but it is still lifted, and lifting it
consumes energy in proportion to its weight and inversely to the lift-to-drag ratio.

Its cost is also not linear, because mass growth feeds itself. Writing the maximum
take-off mass in terms of the payload and the empty and energy fractions,

    MTOW = m_payload / (1 − f_empty − f_energy)

shows that additional empty mass does not add to MTOW once, but through a multiplier
that grows as the denominator shrinks. In the vertical phase the same increment is
charged again, because hover power scales with weight to the three-halves power:

    P_hover = W^1.5 / (η √(2ρA))

so a mass increment raises the hover power requirement faster than proportionally,
which raises installed power, which raises mass. This is the mechanism by which a
modest dead-mass fraction becomes a large payload penalty.

This bill is not hypothetical, and it has been identified independently. In a NASA study
that sized four VTOL architectures against a common mission with a common set of tools,
the lift-plus-cruise concepts came out as the heaviest of the vehicles examined, and the
authors are explicit about the cause:

> *"The weight of the Lift+Cruise concepts is heavier in general than for the other
> vehicles. This is not driven by the cruise power draw, as the L/D_e of the Lift+Cruise
> is indeed higher than the other vehicles. Hover power is higher, but the most likely
> targets for reducing vehicle weight are the extra empty weight items on board in hover
> (wing and propeller)."*

A second NASA review of United States V/STOL development states the structural half of
the same bill as a general principle, drawn from the failure of a tilt-prop aircraft
whose propeller separated in flight after a gearbox mounting fatigued: "this exemplified
an inherent deficiency of this VTOL (lift) arrangement: **to safely transmit power to the
extremities of the planform, very strong (and fatigue-resistant) structures must be
incorporated with an obvious weight penalty**" [2].

Distributing lift or thrust across the span is therefore not only a matter of carrying
rotors and mounts. It obliges the structure that reaches them to be strong enough to
transmit power to the planform extremities and fatigue-resistant enough to keep doing
so. That obligation is charged to mass, and it is charged whether or not the distributed
propulsors are running.

The finding is worth reading carefully, because it separates the two things this paper
is at pains to separate. The lift-plus-cruise vehicle is *aerodynamically better* than
the alternatives it was compared against — its cruise efficiency is higher, and the
study says so. It is nevertheless the heaviest, and the reason given is the hardware it
carries in order to hover. That is Bill 1, stated by an independent source in its own
terms: not a failure of engineering, but the cost of an architecture.

## 3.3 Bill 2 — drag

The second payment is aerodynamic and is charged only to those architectures that
leave hover hardware exposed in forward flight. Rotors stopped in the airstream, the
booms that carry them, and the interference between their wakes and the wing all add
drag in the regime where the aircraft spends nearly all of its time.

The cleanest available measurement of this bill is a controlled comparison within a
single aircraft. In a doctoral study, one uncrewed airframe was tested in a wind tunnel
in four configurations: clean, with the vertical-lift motors and their supporting beams
installed and the propellers left free to align with the flow, with the same hardware but
the propellers held perpendicular to the flow, and with the propellers retracted into the
fuselage. The maximum lift-to-drag ratios measured were:

| Configuration | Maximum L/D |
|---|---:|
| Clean airframe, no hover hardware | ≈ 17 |
| Hover hardware installed, propellers aligned with the flow | ≈ 13 |
| Hover hardware installed, propellers perpendicular to the flow | ≈ 9 |

Two numbers follow, and both are measured rather than estimated. Installing the hover
hardware costs about a quarter of the aircraft's lift-to-drag ratio. Failing to let the
propellers align with the flow costs about a third of what remains. A second model
built on a different airframe reproduced the pattern, at L/D ≈ 11 with the propellers
retracted against ≈ 8 with them exposed.

Because range is linear in lift-to-drag ratio for a fixed energy system, this ladder
translates directly into range; Figure 12 carries it onto the range axis for both a
battery-electric and a fuel-burning energy system.

Expressed as drag rather than efficiency, retracting the propellers reduced drag by 34 %
relative to the standard quadplane configuration on one model and by 30 % on the other.
The author of that study is careful about which comparison is legitimate: measuring the
retracted aircraft against *itself* with the propellers deployed gives 63 %, and he
explicitly rejects that figure in favour of the comparison against a conventional
quadplane. The caution is worth adopting.

A third finding from the same tests matters more than either number, because it
constrains what can be done about the penalty. The drag is not dominated by the
propeller blades:

> *"The difference between propellers parallel to the airflow and without propellers is
> modest. The drag produced by the motors is significant."*

The bill is charged mainly by the motors and the beams that carry them — hardware that
cannot be feathered, folded or aligned away, because its cost is its presence.

Two further measurements support the direction of this result without being combined
with it. Wind-tunnel characterisation of a QuadPlane uncrewed aircraft found that the
highest lift and the least drag occurred in fixed-wing mode at both cruise airspeeds,
that drag in the hybrid regime exceeded drag in either pure mode because of adverse flow
interactions, and — a point that matters for how such aircraft are designed — that a
simulation model assuming negligible interaction between the rotors and the structure
"always predicts higher lift and lower drag than were experimentally observed."

Separately, a wind-tunnel study of twenty-six stationary lift propellers held edge-on to
the flow found that their drag scales with frontal area and with the square of airspeed,
that blade pitch adds to it, and that the hover powertrain components "added a
significant amount of aerodynamic drag during forward flight" in the absence of a
mechanism to stow them.

The important property of this bill is not its size but where it is charged. It is
charged per unit time in cruise, so it grows with exactly the quantity the aircraft
exists to maximise.

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

The three bills are not independent problems with three independent fixes. Each known
architectural move reduces one and increases another. Figure 3 shows the three bills and
the moves that convert one into another; Table 1 lists the same moves in full.

**Table 1.** Architectural moves and the bills they transfer.

| Move | Bill it attacks | Bill it creates |
|---|---|---|
| Distributed electric lift rotors | 3 — the cruise engine no longer sizes to hover | 1 and 2 — many rotors and mounts, permanently carried and exposed |
| Folding or retracting lift rotors | 2 — the exposed rotor is removed from cruise | 1 — mechanism, actuation, locking, and a new failure mode |
| Tilt-rotor, tilt-wing, tilt-nacelle | 1 — one propulsion group serves both regimes | mechanical complexity, gyroscopic coupling during rotation, and a transition control problem |
| Higher disc loading, smaller rotors | 1 and 2 — smaller, lighter, cleaner rotors | 3 — hover power rises with √(DL) |
| Lower disc loading, larger rotors | 3 — hover power falls | 1 and 2 — larger structure, larger exposed area |

The table is not only an argument. One of its rows has been measured. In the study
cited in Section 3.3, the retraction system that removed thirty percent of the drag was
then costed: applied to a passenger eVTOL of known characteristics, with the retraction
mechanism assessed at five percent of vehicle mass, the maximum range rose from 119 km
to 121 km — an improvement of under two percent. The drag was genuinely removed and the
range barely moved, because the mechanism that removed it was itself carried.

That is the transfer in Table 1, observed rather than asserted: Bill 2 was paid off by
borrowing from Bill 1, and the balance was very nearly unchanged. What did improve was
speed — the airspeed for maximum range rose by 5 m s⁻¹, and an 80 km mission could be
flown 10 m s⁻¹ faster — which is a real operational gain, and one worth having, but it
is not a reduction of the tax. It is a change in the currency in which the tax is
returned.

The same study notes that for a surveillance aircraft, whose endurance is maximised at
low airspeed where the drag reduction is least effective, even that gain largely
disappears.

Read as a whole, the table describes a pattern rather than a law. Across every move
listed, the cost of giving a wing-borne aircraft a vertical capability behaves as though
it were conserved: architectures do not remove that cost, they choose the currency in
which to pay it.

It should be said plainly that nothing in physics requires this. No conservation
principle is being invoked, and an architecture that reduced all three bills at once
would be a genuine contribution rather than a contradiction. The claim here is
empirical and bounded: among the architectures surveyed, none does, and Section 3.3
supplies a measured instance of the transfer rather than an assumed one. This is why
seventy years of engineering effort has improved hybrid VTOL aircraft considerably
without producing one whose cruise efficiency matches a comparable fixed-wing
aircraft.

## 3.6 The condition for a zero bill

Stating the tax this way makes its escape condition explicit. The bill exists because
hover and cruise are served by hardware that is not the same hardware, doing the same
job, in the same orientation. Relax any part of that and a bill appears:

- **Different hardware** → Bills 1 and 2. The unused set is carried and, if exposed, drags.
- **Same hardware, different orientation** → the tilting family. The mechanism that changes the orientation is itself mass, complexity and a control problem.
- **Same hardware, same orientation, different sizing point** → Bill 3, unless the hover peak is supplied from somewhere other than the continuous power source.

The condition for paying nothing is therefore that the same propulsors, fixed in the
same orientation relative to the airframe, produce both the hover thrust and the cruise
thrust — with the aircraft itself changing orientation rather than any part of it — and
that the difference between the hover peak and the cruise demand is supplied by a
buffer rather than by permanently installed continuous power.

That is a description of a tail-sitter with a buffered series-hybrid powertrain. It is
also, precisely, the configuration described in Section 4.

## 3.7 Why the market looks the way it does

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

