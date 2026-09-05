# Eliminating the Cruise-Efficiency Penalty of Hybrid VTOL: The meryemAircraft Tail-Sitting Blended-Wing-Body Configuration with Propeller-Only Control

Meryem Gülmen, Berke Gülmen, Ömer Gülmen

**Abstract.** Hybrid vertical take-off and landing (VTOL) aircraft combine runway independence with wing-borne cruise, but purchase that combination at a cost to cruise efficiency. This paper argues the cost is architectural rather than a defect of implementation. It is charged in three currencies — the mass of hover hardware carried through cruise, its drag when exposed in cruise, and a power system sized by a condition holding for roughly two percent of the flight — and every known remedy reduces one currency by increasing another. Stating the cost this way makes its escape condition explicit: it is charged whenever hover and cruise are served by hardware that is not the same hardware, in the same orientation, doing the same job. A configuration satisfying that condition is proposed — an uncrewed tail-sitting blended-wing body in which one coaxial counter-rotating pair at the nose produces all thrust in both regimes, four small coaxial pairs at the wing tips produce attitude moments only, and a deployable strip in the nose-propeller slipstream supplies the rolling moment that body-axis-parallel thrust vectors cannot generate. The aircraft has no control surfaces, no tilting or retraction mechanism and no dedicated lift system. Two reference designs are sized twenty times apart in mass, at 50 kg and 1000 kg, from identical equations, with the governing fractions preserved across that range. Two findings changed the study: the tip frames must be faired, and transition altitude loss falls with rotation time rather than rising with it. The study is analytical, with no wind-tunnel or flight validation, and the mass budget is a target. The two aerodynamic coefficients that carry the most weight are not replaced by computation but bounded by it.

**Keywords:** vertical take-off and landing; tail-sitter; blended wing body; uncrewed aerial vehicle; series hybrid propulsion; cruise efficiency; aircraft configuration design

# 1. Introduction

Powered flight for uncrewed aircraft is dominated by two configuration families, and
each is bounded by a different limit.

Fixed-wing aircraft carry payload efficiently over long distances because the wing
sustains the vehicle without continuously expending power on lift. Their limit is not
aerodynamic but infrastructural: they require a runway, a catapult, or an equivalent
launch and recovery installation. That requirement is expensive, fixed in place, and
scales poorly — a larger fixed-wing aircraft demands a longer runway, stronger
pavement, and wider taxiways, so its growth is gated by the ground rather than by the
air.

Rotary-wing and multirotor aircraft remove that requirement entirely. They take off
and land vertically, hover, and operate from confined sites. Their limit is the
converse: without a wing, every second of flight is paid for with installed power, so
range and endurance remain modest and degrade further as the vehicle grows. Figure 1
places the two families against the two capabilities and marks the corner that neither
occupies.

[Figure 1 about here]

The demand to combine the two has been continuous and expensive. Tail-sitting
prototypes were flown in the 1950s, vectored-thrust and tilt-wing aircraft in the
1960s, tilt-rotors from the 1980s, and a broad family of hybrid vertical take-off and
landing (VTOL) uncrewed aircraft since the 2010s. Different nations, services and
propulsion philosophies have attacked the same problem for seventy years. No field
sustains that level of effort against a need that is not real.

Contemporary hybrid VTOL aircraft do combine the two capabilities, and several are in
service. This paper does not dispute that. It argues, instead, that they purchase the
capability at a specific and quantifiable price, and that the price is charged to
cruise efficiency.

The most common hybrid architecture — separate lifting rotors for the vertical phase
and a separate propulsor for cruise — carries its hover hardware for the whole flight
while using it for a few percent of it. The consequences are measurable. Lift
propellers left exposed in forward flight impose a parasitic drag penalty large enough
that retracting them recovers a substantial fraction of it; rotor-wake interference
raises drag further in the hybrid regime; and the second propulsion system remains as
dead mass for the entire cruise. Tilting architectures avoid the dead mass but
substitute mechanical complexity, gyroscopic coupling during transition, and a
non-trivial transition control problem.

The central observation of this paper is that these penalties are not defects of
implementation. They arise from the architecture itself: from the decision to provide
hover and cruise with different hardware. Better engineering can move the penalty
between mass, drag and powertrain sizing, and can reduce any one of them, but it
cannot remove the trade, because the trade is structural.

This paper presents a configuration that does not make that trade. In the proposed
arrangement the aircraft sits on its tail, its entire body is a lifting blended-wing
body, thrust for every flight phase is produced by a single coaxial counter-rotating
propeller pair at the nose, and attitude control is produced by four small coaxial
pairs mounted on rigid frames at the wing tips. The aircraft has no elevons, no
rudder, no tilting mechanism and no dedicated lift system. Roll authority, which
cannot be generated by thrust vectors parallel to the body axis, is provided by a
level-controlled deployable strip on the lower surface positioned within the main
propeller slipstream, so that it remains effective at zero airspeed.

Because hover and cruise are served by the same hardware, none of the three penalties
is incurred. The cost that is incurred — the mass and drag of the control propellers
and their supporting frames — is reported and quantified rather than omitted.

**Contributions.** This paper (i) states the cruise-efficiency penalty of hybrid VTOL
as an architectural rather than an implementation property, and supports that statement
with published figures; (ii) describes a configuration in which the penalty does not
arise; (iii) sizes two reference designs, at 50 kg and 1000 kg maximum take-off weight,
from first principles; and (iv) shows which properties of the configuration are
preserved across that twenty-fold mass range — disc loading, energy-buffer mass fraction
and tip-frame drag fraction — and identifies the two that are not: transition duration,
and the ratio of propeller diameter to span.

**Scope.** This is a configuration study. It contains no computational fluid dynamics,
no wind-tunnel measurement and no flight test. Its numerical results are analytical
estimates from stated assumptions, and its mass budget is a target rather than a
finding. Section 8 states these limitations explicitly.

The remainder of the paper is organised as follows. Section 2 reviews seventy years of
attempts to merge the two configuration families and argues, on the evidence of two
contemporary NASA reviews, that they ended for reasons external to the configuration —
principally engine and transmission reliability — while the one difficulty those reviews
document most fully, the workload of a pilot flying a vertical descent, is also the one
that an uncrewed aircraft removes outright. Section 3 sets out the
architectural tax in its three currencies, shows that architectural remedies transfer it
rather than remove it, and derives the condition under which it would not be charged.
Section 4 describes the proposed configuration, which is built to satisfy that condition.
Section 5 audits the claim bill by bill and states what the configuration does pay.
Section 6 sizes two reference designs twenty times apart in mass and examines how the
proportions scale. Section 7 treats the flight profile and the transition manoeuvre,
including a result that contradicts a common assumption about how quickly a tail-sitter
should rotate. Section 8 states the limitations, and Section 9 concludes.

# 2. Background: seventy years of attempts

The configuration proposed in this paper is new, but the problem it addresses is not,
and neither are several of its ingredients. This section reviews the attempts that
preceded it. The purpose is not to establish priority but to establish two things: that
the need has been pursued continuously for seventy years, and that the pursuit was
rarely abandoned because the aerodynamics failed. Figure 2 places the programmes
discussed below on a single timeline, with the recorded reason each one stopped.

[Figure 2 about here]

## 2.1 Removing the fuselage

The idea that a transport aircraft should carry its payload inside a lifting surface
rather than inside a cylinder is as old as the transport aircraft itself. Burnelli's
lifting-fuselage designs, flown in a succession of prototypes from the 1920s to the
1940s, placed cabin and cargo inside a thick aerofoil-shaped centre body that
contributed lift instead of only drag. The aircraft flew, repeatedly and over two
decades. They never entered series production. The reasons for that are outside the
scope of this paper and are disputed; what matters here is only that the layout was
flown rather than merely proposed, and was not abandoned at the drawing board.

The Northrop XB-35 carried the same idea to its limit: a bomber with no fuselage and
no tail at all. Its programme is often cited as evidence that the flying wing was
premature. Whatever weight that reading deserves, the aircraft's best-documented
difficulties lay in its power transmission rather than in its aerodynamics: the
contra-rotating propellers were driven through remote gearboxes and long extension
shafts, and were eventually changed to single-rotation units. The distinction between an
airframe and the machinery installed in it matters for the present work, and Section 4.3
returns to it — the configuration proposed here uses counter-rotating propellers but
never builds a contra-rotating gearbox, because each rotor of a pair is driven by its own
electric machine on a common axis.

Vought's V-173 and XF5U pursued the opposite extreme of the same intuition — a wing of
very low aspect ratio with large propellers at the tips, intended to work against the
tip vortices. The V-173 flew roughly two hundred times and supported the low-speed
claims made for it. The XF5U was completed and never flown; the programme ended as the
services moved to jet propulsion.

The recurring pattern is worth stating plainly: in each case the aircraft flew, the
configuration was not disqualified in flight, and the programme ended for a reason
that came from outside the configuration.

## 2.2 Standing the aircraft on its tail

The tail-sitter is the most direct answer to the runway. If the aircraft can point its
thrust line at the ground, it needs no separate lift system, no tilting mechanism and
no second propulsion group — the same propeller that cruises also hovers. Two American
prototypes flew this idea in 1954.

The Lockheed XFV-1 never completed the cycle it was built for. Two contemporary NASA
reviews of United States V/STOL development record what it did instead: its "highly
tapered, straight-wing design made the transition to vertical flight only at altitude,
using a jury-rigged, landing-gear cradle for conventional takeoff and landings" [1,2].
It was cancelled with the question it was built to answer still unanswered.

The Convair XFY-1 did answer it. It flew vertically in August 1954, and "six transitions
to conventional flight were successfully completed" [2]. The concept was demonstrated.

What the aircraft was like to fly, and why the programme stopped, are recorded in the
same two reviews — one of which states that most of its content came from the author's
first-hand flight-test experience [1]. Their assessment is more interesting than the
account usually given.

The configuration itself is judged favourably: "good configuration arrangement for low-
and high-speed compatibility", with a high-speed potential of about 500 mph [1]. What is
judged poorly is the machinery and the cockpit around it — "poor mechanical control
system features including low actuator response rate"; "difficult to hover precisely over
a spot"; "tip-over tendencies noted when on ground in gusty air"; "gust sensitivity
bothersome to pilot during takeoff and landing phases" [1]. Of the landing itself, the
second review is explicit about the cause: the pilot skill required was driven by "the
unusual spatial orientation where the pilot looked over his shoulder and down", by "the
sensitivity to atmospheric turbulence", and by "reduced control power near touchdown"
[2]. The precision of flightpath control these concepts offered "was, needless to say,
less than desired" [2].

And then the reason the programme ended, stated the same way in both documents:

> "Six transitions to conventional flight were successfully completed **before testing
> was curtailed because of engine and gear-box reliability problems**." [2]

That sentence corrects the account usually given — including an earlier draft of this
paper. The XFY-1 was not stopped by the pilot workload. The workload was real,
separately documented and severe, but what curtailed the testing was mechanical
reliability in the engine and the gearbox. The tail-sitter of 1954 therefore shares its
cause of death with the XB-35 and with the XFV-1's undelivered engine: **the powerplant
and its transmission, not the configuration.**

Two further findings from these reviews bear directly on the present work, and both cut
against the usual summary.

The first is what NASA identifies as the *foremost* deficiency of the tail-sitter
concept — not the landing, but the absence of a short take-off option: "foremost among
the deficiencies was the lack of STOL operational capability which could improve the
poor payload and range capabilities of these aircraft" [2]. That criticism is aimed at
an aircraft whose payload and range were poor for other reasons, and it does not
transfer automatically to a configuration designed for cruise efficiency; but it is the
judgement of the reviewers and it is recorded here rather than omitted.

The second is a positive finding that is rarely quoted: "dispensing with a conventional
landing gear improved the empty weight fraction for these VATOL aircraft" [2]. Standing
on the tail removed a mass item rather than adding one. Section 4.5 returns to this,
because the present configuration takes the same benefit further — its landing structure
is also its control moment arm.

Finally, the pilot workload matters for a reason that has nothing to do with blame. It
is the one item on the list that an uncrewed aircraft removes outright. "Unusual spatial
orientation where the pilot looked over his shoulder and down" is a statement about a
human being in a cockpit. A vehicle whose attitude comes from an inertial measurement
unit and whose height above ground is a sensor reading has no unusual spatial
orientation, because it has no orientation to be disoriented in.

The rest of the list does transfer, and this paper does not pretend otherwise. Tip-over
tendencies in gusty ground wind, difficulty holding a precise hover, sensitivity to
turbulence and reduced control power near touchdown are properties of standing an
aircraft on its tail, not of having a pilot. Section 8 treats them as inherited.

*One further detail from the record is worth noting because Section 7 arrives at the
same place from theory. The XFY-1's return transition was flown as "a zoom climb... to
achieve a vertical attitude for the descent and to reduce airspeed (altitude gain of
about 3,000 ft)" [2]. The 1954 aircraft climbed into its transition. So, for different
reasons and by a different argument, does the aircraft proposed here.*

## 2.3 Distributing sweep along the span

The proposed planform varies its leading-edge sweep continuously from root to tip while
holding the trailing edge at a constant angle. The principle of treating sweep, chord and
thickness as one coupled distribution rather than three independent choices is not new;
the crescent wing of the Handley Page Victor is its best-known expression, its sweep
decreasing outboard so that the wing was not governed by its most vulnerable station.

The present aircraft is subsonic and does not inherit the transonic motivation that
produced that planform. What it takes is the structural idea alone, and it takes it in a
much reduced form: as Section 4.2 records, the sweep variation actually realised here is
under seven degrees. No claim of descent from the crescent wing is made, and none is
needed. Section 4.2 states the values used, and Section 8 states plainly that they were
chosen rather than derived.
## 2.4 The contemporary hybrids

The problem did not go away when the prototypes did. Since roughly 2010 a large family
of hybrid VTOL uncrewed aircraft has reached service, in two dominant architectures.
Lift-plus-cruise aircraft carry a set of rotors for the vertical phase and a separate
propulsor for cruise, and fly as a fixed-wing aircraft in between. Tilting
architectures — tilt-rotor, tilt-wing and tilt-nacelle — reuse the same propulsors in
both regimes by rotating them.

Both work. Both are in operational use. This paper does not claim otherwise, and
Section 6.5 places the proposed reference designs alongside them without ranking them.
What Section 3 argues is that each of these architectures pays for its capability in a
way the other does not, that the payment can be moved between mass, drag and power
system sizing, and that it cannot be brought to zero as long as hover and cruise are
served by different hardware or by hardware that must move between two roles.

## 2.5 What this history does and does not show

It would be too convenient to declare that every one of these programmes ended for
reasons external to its configuration. Some of the difficulties were real and internal,
and this paper inherits them. The tail-sitter's vertical descent is genuinely harder
than a runway landing. A tail-sitting aircraft is more exposed to crosswind on the
ground than a conventional one. And a set of propellers whose thrust vectors are all
parallel to the body axis cannot, by construction, produce a rolling moment — a
limitation that applies to this configuration exactly as it applied to its
predecessors, and which Section 4.4 addresses rather than avoids.

What the history does show is that the concept was never given a fair verdict under
present-day conditions. The programmes of the 1950s were closed by engine deliveries, by
jet-era procurement priorities, and — in the case where two contemporary NASA reviews
record the reason directly and identically — by engine and gearbox reliability [1,2]. Not
one of them was closed because the configuration failed to fly; one of the reviews rates
the configuration itself favourably while condemning the machinery around it [1]. The
human pilot, whose difficulties are the best-documented part of the record, is the single
constraint that an uncrewed aircraft removes entirely. What is available now that was not available then —
electric drive on each rotor, sensor-based attitude reference, and enough onboard
computation that stability need not come from the airframe alone — removes exactly the
obstacles that stopped it.

What the history does not settle is why the contemporary aircraft that did succeed still
pay for their vertical capability, and what exactly they pay. That is the subject of the
next section.

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

[Figure 12 about here]

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

[Figure 3 about here]

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

# 4. Proposed configuration

## 4.1 Overview

The configuration satisfies the zero-bill condition of Section 3.6 directly rather than
by compensation. The aircraft stands on its tail. Its entire airframe is a blended-wing
body: there is no cylindrical fuselage, and every part of the planform carries payload
and produces lift. A single coaxial counter-rotating propeller pair at the nose
produces all propulsive thrust, in hover and in cruise alike, without changing its
orientation relative to the airframe. Four small coaxial pairs, mounted on rigid frames
at the wing tips, produce attitude control and nothing else. The energy system is a
series hybrid: fuel drives an internal-combustion engine, the engine drives a
generator, and the generator supplies electric machines at the rotors.

The aircraft has no elevons, no rudder, no tilting mechanism, no retraction mechanism
and no dedicated lift system. The only moving aerodynamic device is an on-off strip on
the lower surface, described in Section 4.4, which exists solely because roll cannot be
produced by propellers alone. Figure 4 gives three orthogonal views of the light
reference design and Figure 5 a general view of the same geometry.

[Figure 4 about here]

[Figure 5 about here]

## 4.2 Planform

The planform is a blended-wing body whose leading-edge sweep varies continuously along
the span while the trailing edge is held at a constant angle. The sweep law is linear in
span, running from 45° at the root towards 35° at the span station where leading and
trailing edges would converge; the wing is cropped at 67 % of that station, so the sweep
actually realised runs from **45° at the root to 38.3° at the tip**. The trailing edge is
constant at **25°**. Thickness runs from 25 % of chord at the root to 12 % at the tip, and
the chord from 0.970 m to 0.236 m — a taper ratio of 0.244. These are one distribution
rather than four independent ones, in the manner described in Section 2.3.

The realised sweep variation is therefore modest — under seven degrees — and this should
be stated plainly rather than dressed up. The crescent character of the planform comes
from the curvature of the leading edge and from the divergence between leading and
trailing edge angles, not from a large change in sweep across the span.

These values were chosen, not derived. The 20°–40° band from which they started was
reported favourable in the transonic-transport literature from which the crescent-wing
idea comes, and the present aircraft is subsonic, so that band does not transfer on its
own authority. The choice is stated here as a design decision and is listed again in
Section 8 among the limitations.

Sweep does two jobs in this aircraft, and the second is the reason it is not a free
parameter. The first is the conventional one. The second is that the aircraft is
tailless: with no horizontal stabiliser on a boom, the pitching moment must be
generated by the distribution of lift along the body itself, and sweep is what places
the outboard sections behind the centre of gravity so that they can do it. The sweep
angle and the longitudinal stability of the aircraft are therefore the same design
variable seen from two directions.

Decreasing sweep outboard also keeps the tip sections from being the first to stall.
For a tailless aircraft this matters more than usual, because a tip stall on a swept
planform moves the centre of pressure forward and pitches the aircraft further into the
stall, and there is no tail with which to argue.

The reference geometry for the light design point is a root chord of 0.970 m, a tip
chord of 0.236 m, a span of 3.453 m, a wing area of 1.979 m² and an aspect ratio of 6.03,
giving a wing loading of 25.3 kg m⁻² and a stall speed of 20.1 m s⁻¹ against a cruise
speed of 30 m s⁻¹. These follow from the sweep and crop laws above rather than being
specified independently; Figure 6 gives the distributions.

[Figure 6 about here]

## 4.3 Propulsion

Every propeller on the aircraft is a coaxial counter-rotating pair. There is exactly
one reason for this, and it is worth stating narrowly because coaxial rotors are often
adopted for other reasons that do not apply here. The reason is reaction torque. A
single propeller applies to the airframe a torque equal and opposite to the one it
applies to the air. In a tail-sitter that torque acts about the vertical axis in hover
and about the roll axis in cruise, and in both cases it must be opposed continuously by
something. Opposing it with a control surface costs drag; opposing it with differential
thrust costs a control channel. A counter-rotating pair does not produce it.

The pairs are of fixed geometry. The two rotors of a pair may carry different blade
twist, but the twist is fixed, and there is no cyclic pitch, no collective pitch and no
variable mechanism of any kind. The design point at which torque balance is exact is
cruise, not hover; a small residual torque therefore remains in hover, and Section 8
records this.

The counter-rotating arrangement has a second consequence that the transition analysis
depends on. Because the two rotors of each pair carry equal and opposite angular
momentum, the net angular momentum of the propulsion system is nominally zero. Rotating
the airframe through ninety degrees during transition therefore does not precess
anything, and no gyroscopic moment appears that the control system would have to
cancel. In a tilting architecture this term is present and must be designed for; here it
is absent by construction.

Crucially, the pair is never a contra-rotating gearbox. Each rotor is driven by its own
electric machine on a common axis. The mechanism that repeatedly defeated the XB-35 —
concentric shafts, a splitting gearbox, and the governors that synchronise them — is
never built. This is a direct benefit of electric drive and is one of the three things
listed in Section 2.5 as available now and not in 1954.

The energy path is a series hybrid: fuel → internal-combustion engine → generator →
electric machines. The engine is not mechanically connected to any rotor; it is an
energy source. This decoupling is what allows the engine to be sized for cruise rather
than for hover. For the light reference design the continuous cruise requirement is
1.9 kW at the engine shaft — 1.7 kW at the electric machines — and the engine is sized at
2.6 kW, while the hover requirement is 10.9 kW at the rotor; the
difference is supplied for the duration of the vertical phase by a battery buffer of
1.8 kg, which is 3.6 percent of the maximum take-off mass. Section 5 returns to this,
because it is the mechanism by which Bill 3 is not paid.

## 4.4 Control without control surfaces

The nose pair produces thrust. The four tip pairs produce moments. They are not lift
rotors and they are not sized to hover the aircraft; in the vertical phase they carry
under fifteen percent of the total power. For the light reference design each tip pair
is 0.20 m in diameter and produces 16.2 N during the transition manoeuvre, drawing
335 W, for a total of 1.34 kW across the four.

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

[Figure 7 about here]

Pitch and yaw follow immediately. Differential thrust between the upper and lower pairs
produces a moment about one lateral axis; differential thrust between the left and
right pairs produces a moment about the other. In hover these are the two axes the
aircraft must control against disturbance; in cruise, with the airframe rotated through
ninety degrees, the same four actuators address the same two axes with their roles
exchanged. No actuator changes its function, its orientation, or its mounting.

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
inclined at forty-five degrees, deploys on or off — it is not a proportional control
surface. For the light reference design it runs one hundred and twenty percent of the
root chord in length, reaching outboard to sixty-seven percent of the semi-span, and
stands 2 cm high at its inboard end and 6 cm at its outboard end.

Its authority comes from its length, not its height. The moment scales with the moment
arm, whereas the benefit of additional height saturates: at constant length, doubling
the height from 5 cm to 10 cm roughly doubles the roll rate, while extending the length
from sixty to one hundred and twenty percent of root chord raises it almost fourfold.
The estimated roll moment is approximately 46 N·m, giving a roll rate of the order of
twenty to twenty-five degrees per second, or 1.2 to 1.5 seconds to a thirty-degree
bank.

These figures are order-of-magnitude estimates: the damping and control-effectiveness coefficients are taken from the literature rather than computed for this geometry. The length-versus-height conclusion is robust to that choice, because the proportional difference between the two is far larger than the uncertainty in the coefficients.

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

[Figure 8 about here]

## 4.5 Structure and ground contact

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
buy the control moment arm of Section 4.4 widens the stance base at the same time. One
structure serves three purposes — mounting the control propellers, providing the moment
arm, and carrying the landing loads — and is charged to the mass budget once.

The stance base is a design parameter, not a constraint imposed by the configuration.
Moving the frame ends further outboard widens it without altering the planform, the
propulsion, or the control architecture — and because the same displacement lengthens
the control moment arm of Section 4.4, the two benefits arrive together from one
change. The reference geometry given here is one point on that trade; an operator with
a stronger ground-wind requirement can take another without redesigning the aircraft.

# 5. How the architectural tax is avoided

Section 3 identified three bills and argued that they are one quantity paid in three
currencies. Section 4 described a configuration built to satisfy the zero-bill
condition. This section audits that claim bill by bill, and then states, in the same
detail, what the configuration does pay. The second half is not a concession appended
for balance. An architecture that claimed to pay nothing would be describing a
different aircraft from the one in Section 4.

## 5.1 Bill 1 — mass: not paid

There is no second propulsion group. The nose pair that lifts the aircraft off the
ground is the same pair, in the same orientation, at the same station, that propels it
in cruise. Nothing is carried unused.

This is the whole of the argument, and its brevity is the point. The bill was never a
consequence of poor design in lift-plus-cruise aircraft; it was a consequence of
counting two propulsion systems where the mission needs one. A configuration that
counts one does not reduce the bill — it does not generate it.

The tip pairs are a genuine addition and are accounted for in Section 5.4. They are not
a second propulsion group: they are sized for moments rather than for weight, and in
the vertical phase they draw 1.34 kW against the nose pair's 10.9 kW, which is twelve
percent.

## 5.2 Bill 2 — drag: mostly not paid

In cruise there is no stopped rotor in the airstream, because there is no rotor that
stops. The nose pair is the cruise propulsor and runs at its design condition
throughout. The quarter of lift-to-drag ratio that Section 3.3 reports as the measured cost of
installing hover hardware is not incurred here — not reduced, not mitigated, but absent,
because the hardware that causes it does not exist in this configuration. Nor is there a retraction mechanism,
so the transfer of Bill 2 into Bill 1 identified in Section 3.3 does not occur either.

It is worth noting what this avoidance also spares. Where lift rotors are retained,
keeping their drag small depends on stopping them at a favourable azimuth, which needs
an indexing mechanism; where they are stowed, it needs a retraction mechanism. Both are
mass, and both are failure modes. A configuration with no rotor to stop needs neither.

The word "mostly" in this heading is deliberate. The configuration does place hardware
in the cruise airstream: the four tip frames and the four control propellers they
carry. That is a real payment against Bill 2, and quantifying it produced the single
most consequential sizing result in this study.

The frames present 2.84 m of exposed length to the flow, oriented perpendicular to it,
for the light reference design. At the cruise dynamic pressure of 551 Pa, against a
total cruise drag of 38.6 N, their contribution depends almost entirely on their
cross-section:

| Frame cross-section | C_D | Share of total cruise drag |
|---|---:|---:|
| Circular tube, 20 mm | 1.15 | **93 %** |
| Faired strut, 20 mm | 0.15 | 12 % |
| Well-faired strut, 20 mm | 0.08 | 6.5 % |

Left as circular tubing, the frames alone would produce very nearly as much drag as the
entire rest of the aircraft, and the configuration's central claim would collapse. The
result is therefore not an observation but a requirement: **the tip frames must be
faired.** With a faired section the payment is real and affordable — of the order of
twelve percent of cruise drag — and it is reported here as a cost rather than absorbed
silently.

One property of this cost is worth noting. The frame frontal area scales with the
square of length, and so does the wing area, so under geometric scaling at equal cruise
dynamic pressure the fraction is preserved. This bill does not grow with the aircraft.

The drag coefficients used here are representative values for circular and faired sections at the relevant Reynolds number, and the frame cross-section has not yet been selected. The requirement to fair the frames is robust to that choice — the difference between a circular tube and a faired strut is not a matter of coefficient precision — but the twelve-percent figure is an estimate.

## 5.3 Bill 3 — power system sizing: not paid

The series-hybrid arrangement of Section 4.3 breaks the link that forces the power
system to be sized by the hover condition. Because the engine drives a generator rather
than a rotor, it supplies average power, not peak power, and the peak is supplied from
a buffer.

For the light reference design the numbers are as follows. Cruise draws 1.7 kW at the
electric machines, which is 1.9 kW at the engine shaft once the generator and power
electronics are accounted for, and the engine is sized at 2.6 kW. Hover requires 10.9 kW
at the rotor — 4.2 times the engine's rating. The difference is drawn for the duration of
the vertical phase from a 1.8 kg battery, which is 3.6 percent of the maximum take-off
mass. The heavy reference design sits on the same line: 39.2 kW electrical in cruise,
54.3 kW engine, 216.2 kW hover, 40 kg of battery at 4.0 percent of MTOW.

An aircraft of this class whose powerplant had to be sized for hover would carry an
engine rated above 10.9 kW instead of 2.6 kW. The mass difference is not recovered
elsewhere; it is simply not incurred. That the buffer costs under four percent of MTOW
at both design points, twenty times apart in mass, is the numerical statement that this
avoidance is architectural rather than a fortunate coincidence of one size.

## 5.4 What is paid

The honest ledger has four entries.

**The control propellers.** Four pairs, their motors, mounts and wiring exist only to
produce moments. In the vertical phase they draw twelve percent of the power the nose
pair draws. This is the configuration's substitute for elevons and a rudder, and it is
not free — it is merely cheaper than a second lift system, and it does not sit in the
cruise airstream in the way a lift rotor does.

**The tip frames.** As established in Section 5.2, of the order of twelve percent of
cruise drag, conditional on being faired. This is the largest single payment the
configuration makes, and it is the price of the moment arm, the propeller mounting and
the landing structure combined into one member.

**The roll strip.** The one moving aerodynamic device on the aircraft. Its cost when
retracted is a surface discontinuity; when deployed it is a drag device by construction,
but it is deployed only while a roll is being commanded.

**The transition manoeuvre.** The aircraft must rotate through ninety degrees, and the
rotation costs time, horizontal displacement and control power. Section 7 treats it in
full and shows that the altitude cost, which is the one usually assumed to dominate, can
be brought to zero: rotating slowly and entering the rotation while still climbing
removes it entirely at both design points. What remains is not free — the manoeuvre
occupies seconds during which the aircraft is neither hovering nor cruising — but it is
smaller than the literature on tail-sitters would suggest, and it is the one payment on
this list that gets *cheaper* the less it is hurried.

Set against the bills of Section 3, the ledger is favourable but not empty. The
configuration does not escape physics; it declines a particular trade. What it pays
instead is smaller, and — this is the part that matters for scaling — it does not grow
faster than the aircraft.

# 6. Reference designs at two scales

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

The mass budget behind this is a target and not a finding: 30 % structure, 16 %
propulsion chain, 4 % battery, 8 % avionics and control, 16 % fuel, leaving 26 % —
13 kg — for payload. Paper aircraft are habitually lighter than the ones that get
built, and that margin has not been paid in this table. Section 8 repeats this warning,
because it is the single most likely place for these numbers to be wrong.

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
| Transition time | 4 s |

The heavy design has a longer range than the light one despite a shorter endurance.
Both effects come from the same source: the larger aircraft cruises faster and, at a
higher Reynolds number, achieves a lower zero-lift drag coefficient and therefore a
better lift-to-drag ratio. Nothing in the architecture was changed to obtain this.

## 6.4 Scale behaviour

Five properties of the scaling are worth separating, because three of them are
favourable and two are not. Figure 11 shows the two designs at a common scale, and it
shows the second of the unfavourable ones directly.

[Figure 11 about here]

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
| **4 s** | **27.7 kW** | **13 %** |
| 5 s | 14.2 kW | 7 % |

**The rule is that a larger aircraft turns more slowly.** The heavy design rotates in
four seconds, at thirteen percent of its hover power.

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

**Span efficiency.** A vortex-lattice solution of the planform of Section 4.2 [15] gives
an inviscid span efficiency of 0.99. That is not the same quantity as the 0.85 used here.
The vortex-lattice figure counts only the departure of the induced drag from the
elliptic ideal; the 0.85 is an Oswald-type efficiency that also carries the viscous
drag due to lift, which for a clean wing runs at roughly 85 to 90 percent of the
inviscid value. The two are consistent. Reporting the calculation as an improvement on
the assumption would be a category error, and it is not claimed.

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
been removed. Section 8.12 lists it first among the places these results should be
attacked, and the calculation it asks for has now been carried out: a structured
Reynolds-averaged solution over the planform of Section 4.2, at the cruise Reynolds
number and at zero lift, resolving the wing and blended body as a three-dimensional
surface rather than as stacked sections. It gives a wing-and-body zero-lift drag of

**0.0141, with a measured uncertainty of about five percent**,

against the 0.0129 of the tripped strip estimate — nine percent higher, and in the
unfavourable direction. Substituting it for the strip figure raises the total to 0.0224.
**The assumed 0.0248 still lies above it**, so the conclusion of the previous paragraph
survives the more expensive calculation; the margin narrows from seventeen percent to
eleven. The assumption is not replaced here either, for the same reason as before.

The five percent is itself measured rather than asserted:

| Source of uncertainty | Magnitude |
|---|---:|
| Iterative convergence | 0.1 % |
| Spatial discretisation, three grids of 0.27 – 2.66 M cells | < 0.1 % |
| Wall resolution, y⁺ 20 → 1 | 1.6 % |
| Wall resolution, y⁺ 43 → 20 | 10 % |
| Turbulence model, k-ω SST against Spalart–Allmaras | 2.7 – 8.1 % |

The dominant term is the turbulence model, not the grid — which is worth stating plainly,
because grid convergence is the check a reader expects and it turns out to bound the
smallest of the five terms. Two further results are recorded because they are easy to get
wrong in either direction. The forces converge far more slowly than the residuals: at a
velocity residual of 1.6 × 10⁻⁵ the computed drag was still fifty-five percent above its
converged value, so a solution stopped on residuals alone would have been badly wrong.
And the wall-resolution sensitivity saturates rather than continuing: between y⁺ 20 and
y⁺ 1 the drag moves by 1.6 percent, so the wall-function results are not systematically
far from the wall-resolved one, and an extrapolation of the coarser trend overstated the
wall-resolved value by nine percent.

**What this does not settle.** The solution is fully turbulent throughout. It therefore
speaks to the tripped row of the table above and not to the clean-surface row, and the
gap between those two rows — 0.0073 against 0.0141 — is now the largest single
uncertainty in the zero-lift drag. Closing it requires a transition-sensitive model,
which needs a wall-resolved grid and a two-equation formulation at the same time; that
combination was attempted and did not converge. The clean-surface bound therefore remains
where the strip calculation left it.

**Internal volume.** One closure that the mass budget does not address is whether the
payload fits. The body's gross internal volume follows from the thickness distribution:
185 litres for the light design. Taking rather more than half of that as usable and
subtracting fuel, buffer, powerplant and avionics leaves about 80 litres for 13 kg of
payload, which requires a mean density of only 0.16 kg per litre. The configuration is
mass-limited rather than volume-limited, and the choice of mission therefore constrains
the structure and the load paths rather than the internal arrangement.

# 7. Flight profile and transition

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

[Figure 9 about here]

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

[Figure 10 about here]

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
acquiring that climb rate is negligible: at T/W = 1.2 the vertical acceleration is
(T/W − 1)g = 1.96 m s⁻², so five metres per second is reached in 2.6 s over 6.4 m of
climb, and the kinetic energy involved is 625 J against a fuel energy of 103 kWh.

**The reference profile is therefore to enter the rotation at 5 m s⁻¹ of climb and
rotate over the times given in Section 6 — two seconds for the light design, four for
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

# 8. Limitations

This is a configuration study. It contains no experimental validation of any kind, and
the numbers in it are the output of elementary methods applied to a set of assumptions.
This section states what those limits are, in enough detail that a reader can judge how
much weight each result will bear. Several of the items below were discovered during the
study and changed its results; they are recorded here rather than smoothed away.

## 8.1 No validation

There is no computational fluid dynamics in this work, no wind-tunnel testing, and no
flight testing. Every aerodynamic coefficient is either taken from the literature or
assumed. Nothing in Sections 4 to 7 has been measured.

## 8.2 The mass budget is a target, not a finding

The reference designs are sized from an assumed mass breakdown — 30 % structure, 16 %
propulsion chain, 4 % battery, 8 % avionics, 16 % fuel, 26 % payload. Paper aircraft are
habitually lighter than the aircraft that eventually get built, and no allowance for that
margin has been made anywhere in this study. The payload fraction is the
number most exposed to it, because payload is the residual: it absorbs the entire error
of every other line.

This is the single most likely place for the results of this paper to be wrong, and it
is the reason Section 6.5 declines to compare the calculated payload fractions against
the published figures of aircraft that exist.

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
  0.0210, so the assumed value is conservative; but the build-up has a weak link, and it
  is the largest term in it. Its strip method treats the root section as a
  two-dimensional aerofoil of twenty-five percent thickness, and the flow over the centre
  body of a blended-wing body is not two-dimensional. The build-up is therefore reported
  as a bound on the assumption rather than as a replacement for it.
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
from it. The aerodynamic model is a linear lift curve to stall with a flat-plate relation
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

## 8.12 What would change these conclusions

The results of this paper would be most efficiently attacked in four places, and they
are listed so that they can be:

1. **A three-dimensional solution for the centre body.** Section 6.6 reports a component
   build-up that bounds the assumed C_D0, but its strip method cannot model the flow over
   a twenty-five percent thick blended centre body, and that is where most of the
   remaining uncertainty sits.
2. **A structural mass estimate** for the airframe and the tip frames, which would test
   the payload fraction — the weakest number in the study.
3. **A six-degree-of-freedom transition simulation** with rotational dynamics, which
   would size the tip propellers properly rather than by order of magnitude.
4. **A panel-method analysis of the tip surfaces**, which would either convert Section
   8.7 into a quantified benefit or remove it. The vortex-lattice solution of Section 6.6
   covers the planform but not the tip surfaces, which remain unquantified.

None of these requires an experiment. All four are within reach of a follow-on study,
and the configuration is described in enough detail in Section 4 and Section 6 for
another group to attempt any of them independently.

# 9. Conclusion

Hybrid vertical take-off aircraft pay for their vertical capability, and this paper has
argued that the payment is architectural rather than a defect of implementation. It
appears in three currencies — the mass of hardware carried but unused, the drag of
hardware exposed but inactive, and a power system sized by a condition that holds for
about two percent of the flight — and each known architectural move reduces one of them
by increasing another. A NASA sizing study of four VTOL architectures reaches the same
conclusion from the opposite direction, finding the lift-plus-cruise concept to be the
heaviest of those examined while also having the best cruise efficiency, and naming the
cause as the empty weight carried for hover.

Stating the tax in that form makes its escape condition explicit: it is charged whenever
hover and cruise are served by hardware that is not the same hardware, doing the same
job, in the same orientation. The configuration described here satisfies that condition
rather than compensating for failing it. The aircraft rotates; nothing on the aircraft
rotates relative to it. A single coaxial pair at the nose provides all thrust in both
regimes. Four small coaxial pairs at the wing tips provide moments and nothing else, and
a strip on the lower surface closes the one gap that propellers cannot — the rolling
moment, which parallel thrust vectors cannot produce at any thrust setting or mounting
position. There are no elevons, no rudder, no tilting mechanism, no retraction mechanism
and no dedicated lift system.

The configuration was sized at 50 kg and at 1000 kg using the same equations and the
same architecture, twenty times apart in mass. Three properties hold across that range:
disc loading is constant by design, the energy buffer that decouples the engine from the
hover peak stays under four percent of take-off mass at both points, and the drag
fraction charged to the tip frames is preserved because frontal area and wing area scale
together. Holding the disc loading is what keeps hover power growing linearly with mass
instead of as the classical L^3.5. Two quantities do not scale, and both are reported
rather than smoothed: the larger aircraft must rotate more slowly, and its propeller
grows faster than its span, so the heavy design is not the light design seen from further
away.

Two results emerged during the study that changed it. The tip frames, if left as
circular tubing, would produce nearly as much drag as the entire rest of the aircraft;
fairing them is not an option but a requirement, and it is also what makes their tip
surfaces available as lifting surfaces at no additional part or mass. And the transition
does not behave as commonly assumed: a slower rotation loses *less* altitude, not more,
because the aircraft is supported during the manoeuvre rather than falling through it —
so entering the rotation while still climbing, rather than stopping to hover first,
removes the altitude penalty entirely.

What this paper offers is a configuration and its numbers, not a validated aircraft.
There is no wind-tunnel data here, no computational fluid dynamics, and no flight test;
the mass budget is a target that has not paid the margin such budgets usually owe. The
claims most exposed to that are identified in Section 8, together with the four analyses
that would test them, none of which requires an experiment. The configuration is
described in enough detail for another group to attempt any of them independently, and
that is the outcome this paper is written to invite.

# Declarations

**Funding.** This research received no external funding.

**Conflicts of interest.** The authors have filed a patent application covering the aircraft configuration
described in this paper (Türkpatent application 2026/014570).

**Data availability.** All data supporting the reported results are contained within the article. The
parametric geometry model, the figure-generation scripts and the transition
simulation, together with the aerodynamic calculations of Section 6.6, are openly
available at https://github.com/LORDTEK/meryemAircraft

**Acknowledgements.** Artificial-intelligence tools were used during the preparation of this work, for
literature searching, numerical checking and language editing. All design decisions,
engineering judgements and claims presented in this paper are the authors' own, and
the authors accept full responsibility for the content.

# References

1. Anderson, S. B. *Historical Overview of V/STOL Aircraft Technology.* NASA
   Technical Memorandum 81280, NASA Ames Research Center, Moffett Field, CA,
   March 1981.
2. Nelms, W. P.; Anderson, S. B. *V/STOL Concepts in the United States — Past,
   Present, and Future.* NASA Technical Memorandum 85938 (Report A-9695), NASA
   Ames Research Center, Moffett Field, CA, April 1984.
3. Bacchini, A. *Electric VTOL Preliminary Design and Wind Tunnel Tests.*
   Doctoral thesis, Politecnico di Torino, Department of Mechanical and
   Aerospace Engineering, XXXII cycle, March 2020.
4. Mathur, A.; Atkins, E. *Wind Tunnel Testing and Aerodynamic Characterization
   of a QuadPlane Uncrewed Aircraft System.* arXiv:2301.12316, 2023.
5. Sahwee, Z.; Mohd Kamal, N. L.; Abdul Hamid, S.; Norhashim, N.; Lotta, N.;
   Mohd Asri, M. H. Drag Assessment of Vertical Lift Propeller in Forward Flight
   for Electric Fixed-Wing VTOL Unmanned Aerial Vehicle. *IOP Conference Series:
   Materials Science and Engineering* **705**, 012007, 2019.
   doi:10.1088/1757-899X/705/1/012007
6. Silva, C.; Johnson, W.; Antcliff, K. R.; Patterson, M. D. *VTOL Urban Air
   Mobility Concept Vehicles for Technology Development.* AIAA Paper 2018-3847,
   2018 Aviation Technology, Integration, and Operations Conference, Atlanta,
   GA, June 2018. doi:10.2514/6.2018-3847
7. Xu, W.; Gu, H.; Qing, Y.; Lin, J.; Zhang, F. *Full Attitude Control of an
   Efficient Quadrotor Tail-sitter VTOL UAV with Flexible Modes.*
   arXiv:1903.06393, 2019.
8. HAVELSAN. *BAHA — Sub-Cloud Autonomous UAV.* Manufacturer product sheet.
   Accessed 27 August 2026.
9. Textron Systems. *Aerosonde Mk 4.7 HQ (VTOL).* Manufacturer product sheet.
   Accessed 27 August 2026.
10. Baykar. *KALKAN.* Manufacturer product sheet. Accessed 27 August 2026.
11. HAVELSAN. *BULUT.* Manufacturer product sheet. Accessed 27 August 2026.
12. Elroy Air. *Chaparral.* Manufacturer product sheet. Accessed 27 August 2026.
13. Sabrewing Aircraft Company. *Rhaegal-A.* Manufacturer product sheet.
    Accessed 27 August 2026.
14. Pipistrel. *Nuuva V300.* Manufacturer product sheet. Accessed 27 August 2026.
15. Sharpe, P. D. *AeroSandbox: A Differentiable Framework for Aircraft Design
    Optimization.* S.M. thesis, Massachusetts Institute of Technology, 2021.
    Software: https://github.com/peterdsharpe/AeroSandbox
16. Sharpe, P. D. *NeuralFoil: An airfoil aerodynamics analysis tool using
    physics-informed machine learning.* 2023.
    Software: https://github.com/peterdsharpe/NeuralFoil