# The Architectural Cost of Hybrid VTOL: meryemAircraft, a Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System

Meryem Gülmen, Berke Gülmen, Ömer Gülmen

**Abstract.** Hybrid vertical take-off and landing (VTOL) aircraft combine runway independence with wing-borne cruise and pay for it in cruise efficiency. This paper treats that cost as architectural rather than as a defect of implementation, and develops it as an accounting framework. The penalty is charged in three coupled currencies — the mass of hover hardware carried through cruise, its drag when exposed in cruise, and a power system sized by a condition holding for some two percent of the flight — and every remedy surveyed here reduces one by raising another. The escape condition is then explicit: the penalty is charged whenever hover and cruise are served by hardware that is not the same hardware, in the same orientation, doing the same job. A second result is methodological: architectural comparisons depend on the sizing contract chosen, and a fixed fuel fraction removes the mass bill from the range column altogether, so three contracts are reported rather than one. meryemAircraft, an uncrewed tail-sitting blended-wing body, satisfies the escape condition and serves as the case study: one coaxial pair at the nose gives all thrust in both regimes, four small pairs at the tips give attitude moments only, and a deployable strip is assigned the roll that body-parallel thrust cannot produce. Against a lift-plus-cruise layout, on wind-tunnel drag, it closes the same mission at forty-two percent lower take-off mass and seventeen percent greater range; against a tilting layout the comparison reverses between contracts and no superiority is claimed. A three-dimensional solution bounds the zero-lift drag with a measured uncertainty budget, and a component mass build-up closes the 50 kg design conditionally and not the 1000 kg one. The study is analytical, with no experimental validation of the configuration. The tip propellers can turn the aircraft's rotational inertia through the transition but not, on present evidence, its aerodynamic moment. Resolving that margin along the trajectory shows the aircraft never reaches ninety degrees of incidence — the relative wind rotates with the body — so the outstanding measurement is the pitching moment to some twenty-two degrees at low dynamic pressure, together with trim at cruise. A vortex-lattice solution establishes static pitch stability under a stated packaging rule and sizes the camber moment that trim requires without closing it. Roll is treated the same way: the inertia and the damping are computed for this planform, the moment needed for a twenty-degree-per-second roll follows from them, and the strip's effectiveness in supplying it is stated as a requirement rather than demonstrated. Yaw has the strongest authority of the three axes, because differential tip thrust acts through the semi-span, but the planform supplies no directional stability at all, so the tip-frame fairings must serve as the vertical surfaces as well as the drag measure they were introduced as. Attitude control is therefore sized in every axis and closed in none. Transition controllability remains the principal open requirement and is stated as a threshold a future measurement must meet.

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
cannot be generated by thrust vectors parallel to the body axis, is assigned to a
level-controlled deployable strip on the lower surface positioned within the main
propeller slipstream, so that it is loaded at zero airspeed. Section 4.4 computes the roll
inertia and the roll damping of this planform and states the moment the strip must supply;
it does not show that the strip supplies it.

Because the same primary propulsor serves hover and cruise without changing its
orientation relative to the airframe, none of the three penalties **as defined in
Section 3** arises: there is no second thrust system to carry, no lift hardware left
exposed in the cruise airstream, and no continuous power system sized by the hover peak.
That is a statement about three specific charges, not a claim that the configuration is
free. What it pays instead — the mass and drag of the control propellers and their
supporting frames, the rolling-moment device, and the transition manoeuvre itself — is
reported and quantified in Section 5.4 rather than omitted.

**Contributions.** The primary contribution of this paper is a framework, and the aircraft
is the case that instantiates it. Specifically, the paper

1. **states the cruise-efficiency penalty of hybrid VTOL as an architectural property**
   rather than a defect of implementation, expresses it as three dimensionless charges —
   carried hover mass, exposed cruise drag, and continuous power sized by the hover peak —
   shows with published figures that the known remedies transfer the penalty between them
   rather than removing it, derives from that structure an explicit escape condition, and
   tests a consequence of the framework against an independent published sizing study: that
   the architecture with the best cruise efficiency need not be the lightest, which is what
   that study reports and what a single-metric comparison would not anticipate;
2. **shows that architectural comparisons are contract-dependent**, which is a
   methodological result independent of any particular aircraft: range computed at a fixed
   fuel fraction is independent of take-off mass, so the mass bill never reaches the range
   column, and an architecture that closes heavier is silently permitted to carry
   proportionally more fuel. Three sizing contracts are therefore reported side by side,
   and the ranking of architectures is shown to change between them;
3. **instantiates the escape condition in a configuration** — meryemAircraft — audits the
   three bills against it one at a time, and states what the configuration pays instead;
4. **supports the case study with computation rather than assertion** where it could: a
   three-dimensional Reynolds-averaged solution for the zero-lift drag, reported with a
   measured uncertainty budget that includes turbulence-model and initialisation spread; a
   component mass build-up that replaces the assumed mass fractions and closes the 50 kg
   design conditionally while not closing the 1000 kg one; and a rotational check that
   establishes inertial feasibility of the transition; and
5. **states what is not established, as a testable requirement rather than an omission.**
   The aerodynamic pitching moment through the rotation is not known, and the paper reports
   the coefficient that would consume the available control margin instead of estimating
   the coefficient itself.

Items 1 and 2 stand independently of whether this particular aircraft is ever built. Item 5
is the reason the paper does not claim that it can be.

**Scope.** This is a configuration study. It contains no wind-tunnel measurement and no
flight test. Its numerical results are analytical estimates from stated assumptions, with
one exception: the zero-lift drag of the wing and centre body has been computed
three-dimensionally, and Section 6.6 reports it with a measured uncertainty budget. The
mass budget began as a target rather than a finding; Section 6.7 replaces it for the light
design with a build-up from components, which closes conditionally and names the condition,
and which does not close the heavy design at all. Section 8 states these limitations
explicitly.

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

## 3.7 The three bills stated formally, and a test of the statement

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
cruise efficiency of the group*, and the authors attribute the weight to hardware carried for
hover rather than to cruise power. That is *f*₁ dominating while *f*₂ is favourable, which is
the framework's prediction and not a restatement of it.

The comparison of Section 5.5 shows the same pattern on a different set of architectures:
of the three sized there, the tilting layout has the best cruise lift-to-drag ratio — 13.44
against 12.00 — and is nonetheless twenty percent heavier than the tail-sitter, because it
carries a tilt mechanism that the tail-sitter does not. Best in *f*₂, worse in *f*₁. **That
comparison is an illustration and not evidence, and the distinction matters here.** Its
tilting layout is given a cruise-drag multiplier of 1.00 — that is, its mechanism is
credited as aerodynamically free — precisely to make the *f*₂ advantage as large as the
architecture could possibly claim. A comparison whose inputs were chosen by the present
authors cannot corroborate the present authors' framework. **The evidential weight rests on
the NASA study alone**, whose numbers were produced for another purpose and are not ours to
choose; Section 5.5 shows what the framework looks like when applied, not that it is right.

Neither comparison validates the framework. Both are external consistency checks: the NASA
study was carried out for other purposes and its numbers were not chosen to suit the
argument here, and a framework that predicted the opposite ordering would be in difficulty
against them. Corroboration of this kind raises confidence that the three charges are
separable in practice; it does not establish that they are the only three, and nothing
short of a broad survey of sized architectures could.

**What the framework does not claim.** It does not predict the magnitude of any bill for an
architecture that has not been sized; the fractions above must be computed or measured case
by case. What it provides is the statement that there are exactly three of them, that they
are the currencies in which architectural remedies trade, and the condition under which none
is charged.

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
because it is the mechanism that releases the engine from the hover condition — Bill 3 as
Section 3 defines it. The electrical path is not released, and Section 5.3 says so.

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
inclined at forty-five degrees, deploys on or off — it is not a proportional control
surface. For the light reference design it runs one hundred and twenty percent of the
root chord in length, reaching outboard to sixty-seven percent of the semi-span, and
stands 2 cm high at its inboard end and 6 cm at its outboard end.

Its authority comes from its length, not its height. The moment scales with the moment
arm, whereas the benefit of additional height saturates: at constant length, doubling
the height from 5 cm to 10 cm roughly doubles the roll rate, while extending the length
from sixty to one hundred and twenty percent of root chord raises it almost fourfold.
This comparison is robust to how the strip's force is modelled, because the length enters
both the affected area and the moment arm while the height enters only the first.

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
Chordwise fences and Gurney strips of one to two percent chord are reported to deliver 0.1
to 0.3, so the requirement is a plausible one — but it is a requirement, taken from the
literature on a different device, and this paper does not compute it for this geometry.
**Roll authority is therefore sized here and not closed.**

**Hover is the harder case, and for a reason that is structural rather than numerical.** At
zero airspeed only the inboard part of the strip is loaded, by the slipstream, and the same
circulation model over the slipstream-washed area gives 6.0 to 12.0 N·m for ΔC_L between
0.10 and 0.20 — enough for a thirty-degree bank in 1.5 to 2.1 s. But at zero airspeed there
is no aerodynamic damping at all: the roll axis is a double integrator, so the rate does not
settle and the strip must be commanded off rather than left on. Roll control in hover is
consequently a tighter problem than roll control in cruise, which is the reverse of the
usual situation and is a consequence of this configuration rather than of its numbers.

**Being an on-off device is not, by itself, disqualifying.** Simulating the first-order roll
dynamics above with a deadband and a finite actuator delay gives a bounded limit cycle: with
a two-degree deadband and a fifty-millisecond deployment the bank angle oscillates by ±0.2°,
and at a hundred and fifty milliseconds by ±9.4°. The device is therefore usable if it is
fast and unusable if it is slow, and the threshold sits in a range where real actuators
differ. That is a design requirement on the actuator, stated here for the first time. None
of this is a closed-loop stability analysis, and none of it substitutes for one.

**Yaw was examined last, and it separates cleanly into an easy half and an open half.** The
easy half is authority. The yaw inertia computed from the same mass distribution is
33.7 kg·m² — close, as it must be for a nearly planar aircraft, to the sum of the roll and
pitch inertias — so the available yaw moment turns the aircraft's own inertia at 73 to 95
degrees per second squared, reaching fifteen degrees of heading in about six tenths of a
second. Nothing in this axis is short of moment.

The open half is stability. A vortex-lattice solution of the planform at sideslip returns
**C_n_β = 0**: the wing supplies no directional stability whatever, which is not a defect of
the solution but the expected result for a planar surface with nothing to generate side
force. Sweep gives this configuration its roll-due-to-sideslip — C_l_β = −0.045 per radian,
a healthy value — and gives it no weathercock stability at all. The profile-drag
contribution to yaw damping is likewise negligible, C_n_r = −0.0023, a time constant of over
a minute.

Directional stability must therefore come from the tip frames, which in cruise stand
perpendicular to the wing plane above and below each tip and are the only vertical surfaces
the aircraft has. Their mid-chord sits 0.879 m aft of the centre of gravity, so with a
surface lift-curve slope of 4 per radian the side area needed is 0.058 m² for
C_n_β = 0.03 and 0.097 m² for 0.05 — which, spread over the 2.84 m of combined frame
length, is a fairing chord of 21 mm and 34 mm respectively. A faired strut of the 20 mm
thickness assumed in Section 5.2 would have a chord of roughly 50 to 70 mm, so the
requirement is comfortably inside what the fairing must be anyway.

**That reframes the fairing, and the reframing is the substantive result of this
subsection.** Section 5.2 introduced the fairing as a drag measure and computed the frame
drag penalty on that basis. It is also, and not incidentally, the aircraft's directional
stability surface and its principal source of yaw damping. The two roles are served by the
same hardware — which is the same pattern the whole paper is about — but the paper had not
noticed the second role, and the fairing's chord is consequently constrained from two
directions rather than one. Neither the fin contribution nor the yaw damping it brings is
computed here. **Yaw authority is sized; directional stability is a requirement placed on a
component the design already carries.**

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

# 5. The architectural tax, audited bill by bill

Section 3 identified three bills and argued that they are one quantity paid in three
currencies. Section 4 described a configuration built to satisfy the zero-bill
condition. This section audits that claim bill by bill, and then states, in the same
detail, what the configuration does pay. The second half is not a concession appended
for balance. An architecture that claimed to pay nothing would be describing a
different aircraft from the one in Section 4.

## 5.1 Bill 1 — mass: the charge does not arise

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

## 5.2 Bill 2 — drag: reduced, not removed

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

The drag coefficients used here are representative values for circular and faired sections at the relevant Reynolds number, and the frame cross-section has not yet been selected. The requirement to fair the frames is robust to that choice — the difference between a circular tube and a faired strut is not a matter of coefficient precision — but the twelve-percent figure is an estimate. At the small cross-section Reynolds number of the light design, achieving a faired coefficient of order 0.15 is itself a design requirement rather than a guaranteed property of any faired shape.

**The fairing is not only a drag measure, and Section 4.4 says why.** The frames are the only surfaces on this aircraft standing perpendicular to the wing plane, and the planform supplies no directional stability at all. The fairing is therefore also the vertical surface that provides it, and a chord of 21 to 34 mm over the combined frame length would deliver a weathercock derivative of 0.03 to 0.05 per radian. That is well inside the chord a 20 mm faired strut needs in any case, so the two requirements do not conflict — but the frame cross-section is now constrained from two directions, and a selection made on drag alone would be made on half the evidence.

## 5.3 Bill 3 — power system sizing: avoided for the engine, not for the electrical path

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

**What is not avoided, and the section heading says so.** The bill is defined in Section 3
as a *continuous* power system sized by the hover peak, and it is the engine and its fuel
consumption that the buffer releases from that condition. The electrical path is not
released: the nose motor and the power electronics must still pass the full 10.9 kW, and
the component build-up of Section 6.7 shows them as 2.73 kg and 0.61 kg against 2.60 kg of
engine and generator — that is, the hover-sized electrical machine is the single largest
item in the propulsion chain. The saving is real and it is the engine's, but a reader
should not take it as an aircraft on which nothing is sized by hover. The buffer itself
carries a further condition, given in Section 6.7: it is specified by power rather than
energy, at 4.6 kW kg⁻¹, which is a demanding cell requirement and not a free parameter.

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


## 5.5 A comparative sizing of three architectures

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
the blade one would choose for cruise; but range does not contain propulsive efficiency,
so the generosity falls entirely on mass — 60.3 kg becomes 62.7 kg at a fifteen percent
efficiency penalty — and none of it on the range comparison. And a second table, in which
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

The mass budget behind this — 30 % structure, 16 % propulsion chain, 4 % battery, 8 %
avionics and control, 16 % fuel, leaving 26 %, or 13 kg, for payload — is the allowance the
design is sized against, and it is asserted here rather than derived. Section 6.7 rebuilds
it from components and finds it can be met, with 2.2 kg in hand, on one condition that is
not demonstrated: a structural areal density no greater than 1.78 kg m⁻². Paper aircraft
are habitually lighter than the ones that get built, and no allowance for that has been
paid in this table beyond the contingency inside the build-up. Section 8.2 keeps this as
the single most likely place for these numbers to be wrong.

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
| Transition time | 5.1 s |

The heavy design has a longer range than the light one despite a shorter endurance.
Both effects come from the same source: the larger aircraft cruises faster and, at a
higher Reynolds number, achieves a lower zero-lift drag coefficient and therefore a
better lift-to-drag ratio. Nothing in the architecture was changed to obtain this.

## 6.4 Scale behaviour

One qualification applies to everything in this section. The scaling described here is the
scaling of the analytical sizing model — of powers, loadings and mass *fractions*. The
component build-up of Section 6.7 does not reproduce it for the structure: whether the
heavy design's mass closes depends on how shell areal density grows with size, which was
not measured. The fractions below are preserved by the sizing rules; they have not been
shown to be realisable at 1000 kg.

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
| 4 s | 27.7 kW | 13 % |
| 5 s | 14.2 kW | 7 % |
| **5.1 s** | **13.4 kW** | **6 %** |

**The rule is that a larger aircraft turns more slowly.** The heavy design rotates in
5.1 seconds, at six percent of its hover power. That figure is not a round number chosen
for convenience: Section 7.6 shows it is the rotation time at which the heavy design holds
the same rotational control margin the light design holds at two seconds. An earlier
version of this study used four seconds, at which the tip propellers must supply thirteen
percent of hover power — nearly the whole of their allocation — and at which a smoothly
commanded rotation does not close at all.

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
been removed. Section 8.14 lists it first among the places these results should be
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
is therefore bracketed rather than simply beaten. Substituting each in turn raises the
total to between 0.0203 and 0.0230. **The assumed 0.0248 lies above all of them**, so the
conclusion of the previous paragraph survives the more expensive calculation under either
closure and under either initialisation; the margin is twenty-two percent on the most
optimistic value and eight percent on the conservative one. The assumption is not
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
shows one would fall inside the interval; 0.01201 – 0.01253 is a measured spread and not
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

## 6.7 A component build-up of the mass budget

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
5.25 the root bending moment is 934 N m; carried at 400 MPa over a structural depth of 0.9
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
before.** It must supply the difference between hover power and engine rating, 8.3 kW at
the light design point, from 1.8 kg — a specific power of 4.6 kW kg⁻¹, or about 26 C at
180 Wh kg⁻¹. Energy is not the binding constraint until roughly 140 seconds of hover, well
beyond the profile of Section 7; below that the buffer is power-limited. The heavy design
is in the same regime, 4.1 kW kg⁻¹ at 22 C. That places the buffer in the high-power
lithium-ion or lithium-polymer class — cells rated for twenty to thirty times their
capacity in continuous discharge — rather than in the high-energy class a range-driven
selection would reach for. Cells capable of those discharge rates generally carry less
energy per kilogram than 180 Wh kg⁻¹, which lowers the crossover further. The buffer masses used are therefore a cell-selection requirement rather than a
free parameter, and the requirement is a demanding one.

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
between roughly 80 and 85 percent of root chord: forward of 80 percent the camber moment
needed to trim exceeds what reflexed sections deliver, and aft of 85 percent the static
margin falls below the usual tailless band. The sweep carries the neutral point to 0.859 m
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

# 8. Limitations

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

- The **roll authority** of the lower-surface strip. Section 4.4 now computes the two
  halves of this that can be computed for this geometry — the roll inertia, 25.0 kg·m²,
  and the roll damping, |C_l_p| = 0.358 from a vortex-lattice solution rather than from
  the literature — and inverts the question: twenty degrees per second at cruise requires
  27.1 N·m. What remains from the literature is the strip's own effectiveness, and it is
  the load-bearing part. The strip's own force as a swept fence supplies about a third of
  the required moment; the moment must therefore come from the change in the half-wing's
  circulation, which asks for ΔC_L ≈ 0.12 over the strip's span. That figure is consistent
  with published Gurney-flap and fence data but is not computed here, so **roll authority
  is sized and not closed, in the same sense as cruise trim.** An earlier version of this
  paper quoted 46 N·m without stating the mechanism it came from; that number implies
  ΔC_L ≈ 0.20 and is not reproduced here as an authority.
- The **directional stability** of the configuration. Section 4.4 computes C_n_β = 0 for
  the planform — the wing supplies none — and shows that the tip-frame fairing must supply
  it, at a chord well inside what the fairing needs for drag reasons. The fin contribution
  itself is **not computed**, and neither is the yaw damping it would bring; the
  profile-drag damping of the bare planform, C_n_r = −0.0023, is negligible. Yaw authority
  is not in question — the yaw arm is the semi-span, so the available moment is 2.4 times
  the pitch moment — but directional stability and yaw damping are a single open item
  resting on a component whose section has not been selected.
- The **roll actuator's speed** is a requirement this paper did not previously state. The
  on-off strip gives a bounded limit cycle of ±0.2° in bank at a fifty-millisecond
  deployment and ±9.4° at a hundred and fifty, so the device is usable if it is fast. No
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
   margin of 1.49 at the light design point and 1.57 at the heavy one on the cheapest
   rotation profile, and of 0.99 and 1.05 on a smooth one — that is, at the actuator limit
   rather than clear of it — together with a measured account of how that margin
   narrows with size, and a threshold for the aerodynamic moment resolved along the
   trajectory. That resolution corrected the requirement rather than merely quantifying it:
   the aircraft does not reach ninety degrees of incidence, because the relative wind
   rotates with the body, and peak incidence is 17.5° to 21.6°. **Transition controllability
   remains the largest unresolved item in this study**, but it now asks for the pitching
   moment up to some twenty-two degrees at low dynamic pressure and for trim at cruise
   incidence, rather than for a moment sweep through ninety degrees. What is still not done
   is answering it: a reduced computation would replace a dominant term with a
   less-validated model. What it cannot do is charge the
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
a strip on the lower surface is assigned the one gap that propellers cannot close — the
rolling moment, which parallel thrust vectors cannot produce at any thrust setting or
mounting position, and which Section 4.4 sizes without demonstrating. There are no elevons, no rudder, no tilting mechanism, no retraction mechanism
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
away. A third does not scale either, and it is the one that matters most: these are
properties of the sizing rules, and a component build-up of the structure that would have
to realise them meets the mass fractions at 50 kg and does not at 1000 kg.

Two results emerged during the study that changed it. The tip frames, if left as
circular tubing, would produce nearly as much drag as the entire rest of the aircraft;
fairing them is not an option but a requirement, and it is also what makes their tip
surfaces available as lifting surfaces at no additional part or mass. And the transition
does not behave as commonly assumed: a slower rotation loses *less* altitude, not more,
because the aircraft is supported during the manoeuvre rather than falling through it —
so entering the rotation while still climbing, rather than stopping to hover first,
removes the altitude penalty entirely in the point-mass model of Section 7.4.

What this paper offers is a configuration and its numbers, not a validated aircraft.
There is no wind-tunnel data here and no flight test. Two of the four analyses that
Section 8 lists as tests of these results have been carried out — a three-dimensional
solution for the centre body, which narrowed the zero-lift drag without overturning it,
a component build-up of the mass budget, which closes the light design point with 2.2 kg
in hand provided the shell areal density stays at or below 1.78 kg m⁻² and does not close
the heavy design at all, and a rotational check which shows the tip propellers can turn the aircraft's own inertia
through the transition, with a margin of 1.49 at 50 kg and 1.57 at 1000 kg on the cheapest
rotation profile — and of 0.99 and 1.05 on a smooth one, which is to say that both reference
rotation times are actuator-limited lower bounds rather than comfortable choices. That
second figure set the heavy design's rotation time: at the four seconds first used, the
margin was below unity on both profiles, so the rotation was
lengthened to 5.1 s, which costs six percent of hover power instead of thirteen and changes
no other result. The fourth has not been carried
out, and the third is a necessary condition only: charging the aerodynamic pitching moment
through ninety degrees of incidence needs measurements this study does not have. What that
check does supply is a threshold, resolved along the trajectory, and resolving it changed the
question. The aircraft does not reach ninety degrees of incidence: the body rotates through
ninety, but the relative wind rotates with it, and peak incidence is between seventeen and
twenty-two degrees. The high-incidence part of the rotation happens at low dynamic pressure,
where the margin tolerates a coefficient of about 0.21 entering in a climb; the tight part
is the end of the rotation, where incidence is small and speed is high, and that is a trim
question rather than a post-stall one. The trim question has since been sized rather than
closed: the configuration is statically stable, with a neutral point at 34 percent of mean
aerodynamic chord and a margin of 12.5 percent at the assumed centre of gravity, and the
camber moment needed to trim it at cruise is 0.056, which is at the upper edge of what
reflexed sections deliver. The roll axis was treated the same way and gave the same kind of
answer: the roll inertia and the roll damping are computed for this planform, twenty degrees
per second at cruise requires 27.1 N·m, the strip's own force supplies about a third of
that, and the remainder must come from the change it makes to the half-wing's circulation —
a requirement of ΔC_L ≈ 0.12 that published fence and Gurney data make plausible without
this paper establishing it. Attitude control on this aircraft is therefore sized in every
axis and closed in none of them, and that is the honest summary of its control case. Yaw
completes the picture and does so more favourably: because differential thrust between the
left and right tip pairs acts through the semi-span rather than the frame length, yaw is the
strongest axis the arrangement has, at 2.4 times the pitch moment. What yaw lacks is not
authority but stability — the planform's weathercock derivative is zero — and the surfaces
that must supply it are the tip-frame fairings, which the paper had until now treated purely
as a drag measure. That the same member serves as landing structure, moment arm, propeller
mount and directional stability surface is the configuration's own argument made once more;
that none of the four roles has been verified together is its principal limitation. The outstanding measurement is therefore of ordinary size. The claims
most exposed are identified in Section 8. An earlier version of this section stated that
none of the remaining analyses required an experiment; that is no longer true, and the
change is the most important thing this study learned about itself. Transition
controllability rests on a pitching moment that cannot be obtained without a wind tunnel or
an unsteady computational campaign, and the paper declines to substitute a reduced
calculation for it.

What survives independently of that is the framework. The three currencies, the
demonstration that architectural remedies transfer the penalty rather than remove it, the
escape condition, and the finding that architectural comparisons change their ranking with
the sizing contract chosen — none of these depends on whether this particular aircraft is
ever built. meryemAircraft is the case that shows the escape condition can be instantiated
in a real geometry and carried through to reference designs at two scales; it is not
offered as a validated vehicle, and the paper is careful throughout to say which of its
statements are demonstrated, which are conditional, and which are open. The configuration is
described in enough detail for another group to attempt any of the outstanding analyses
independently, and that is the outcome this paper is written to invite.

# Declarations

**Funding.** This research received no external funding.

**Conflicts of interest.** The authors have filed a patent application covering the aircraft configuration
described in this paper (Türkpatent application 2026/014570).

**Data availability.** All data supporting the reported results are contained within the article. The
parametric geometry model, the figure-generation scripts and the transition
simulation, together with the aerodynamic calculations of Section 6.6 — including the
mesh generator, the case setup, the grid-convergence study and the wall-resolution and
turbulence-model sensitivity runs behind the computed zero-lift drag — are openly
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