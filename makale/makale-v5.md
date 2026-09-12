# The Architectural Cost of Hybrid VTOL

---

## Title

**The Architectural Cost of Hybrid VTOL: meryemAircraft, a
Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated
Lift System**

## Authors

Meryem Gülmen <sup>1,\*</sup>, Berke Gülmen <sup>1</sup>, Ömer Gülmen <sup>1</sup>

<sup>1</sup> Independent Researcher, Türkiye

<sup>\*</sup> Correspondence: meryemgulmen@outlook.com

---

## Abstract

Hybrid vertical take-off and landing (VTOL) aircraft combine runway independence with
wing-borne cruise and pay for it in cruise efficiency. This paper treats that cost as
architectural rather than as a defect of implementation, and develops it as an accounting
framework. The penalty is charged in three coupled currencies — the mass of hover hardware
carried through cruise, its drag when exposed in cruise, and a power system sized by a
condition holding for some two percent of the flight — and every remedy surveyed here
reduces one by raising another. The escape condition is then explicit: the penalty is charged whenever
hover and cruise are served by hardware that is not the same hardware, in the same
orientation, doing the same job. A second result is methodological: architectural
comparisons depend on the sizing contract chosen, and a fixed fuel fraction removes the
mass bill from the range column altogether, so three contracts are reported rather than
one.

meryemAircraft, an uncrewed tail-sitting blended-wing body, satisfies the escape condition
and serves as the case study: one coaxial pair at the nose gives all thrust in both
regimes, four small pairs at the tips give attitude moments only, and a deployable strip is
assigned the roll that body-parallel thrust cannot produce. Against a lift-plus-cruise layout, on
wind-tunnel drag, it closes the same mission at forty-two percent lower take-off mass and
seventeen percent greater range; against a tilting layout the comparison reverses between
contracts and no superiority is claimed. A three-dimensional solution bounds the zero-lift
drag with a measured uncertainty budget, and a component mass build-up closes the 50 kg
design conditionally and not the 1000 kg one.

The study is analytical, with no experimental validation of the configuration. The tip
propellers can turn the aircraft's rotational inertia through the transition but not, on
present evidence, its aerodynamic moment. Resolving that margin along the trajectory shows
the aircraft never reaches ninety degrees of incidence — the relative wind rotates with the
body — so the outstanding measurement is the pitching moment to some twenty-two degrees at low
dynamic pressure, together with trim at cruise. A vortex-lattice solution establishes static
pitch stability under a stated packaging rule and closes cruise trim, though not in the way
first supposed: measured data for reflexed sections fall an order of magnitude short of the
moment required, while nine degrees of tip washout supplies it, at a cost of 4.3 percent of
cruise lift-to-drag ratio. Roll is treated the same way: the inertia and the damping are computed
for this planform, the moment needed for a twenty-degree-per-second roll follows from them,
and the strip's effectiveness in supplying it is stated as a requirement rather than
demonstrated. Yaw has the strongest authority of the three axes, because differential tip
thrust acts through the semi-span, but the planform supplies no directional stability at
all, so the tip-frame fairings must serve as the vertical surfaces as well as the drag
measure they were introduced as. Attitude control is therefore sized in every axis and
closed in none. Transition controllability remains the
principal open requirement and is stated as a threshold a future measurement must meet.

*[≈270 kelime. 200 isteyen dergide kesilecek ilk yer: ikinci paragrafın
konfigürasyon tarifi, sonra üçüncü paragrafın ilk cümlesi.]*

*[⚠️ Özette **hiçbir ödünç sayı yok.** %38/%13 (Bacchini & Cestino) bilerek
dışarıda — kaynak henüz birinci elden okunmadı. Menzil sayıları da yok, çünkü
hesaplanmış değerler özette bağlamsız durur.]*

---

## Keywords

vertical take-off and landing; tail-sitter; blended wing body; uncrewed aerial vehicle;
series hybrid propulsion; cruise efficiency; aircraft configuration design

---

## Declarations

### Acknowledgements

> Artificial-intelligence tools were used during the preparation of this work, for
> literature searching, numerical checking and language editing. All design decisions,
> engineering judgements and claims presented in this paper are the authors' own, and
> the authors accept full responsibility for the content.

*[✅ Tasarımcının değişmez kuralı: **genel ifade, marka/model/firma adı yok**,
yazar satırında yapay zekâ yer almaz. Bu metin o kuralı karşılar ve aynı zamanda
MDPI'ın yapay zekâ beyan zorunluluğunu da karşılar.]*

### Conflicts of Interest

> The authors have filed a patent application covering the aircraft configuration
> described in this paper (Türkpatent application 2026/014570).

*Durum: başvuru **yapıldı**. Metin buna göre yazıldı — "yapılacaktır" değil,
"yapılmıştır". Dergi başvuru numarası isterse eklenir.*

### Data Availability

> All data supporting the reported results are contained within the article. The
> parametric geometry model, the figure-generation scripts and the transition
> simulation, together with the aerodynamic calculations of Section 6.6 — including the
> mesh generator, the case setup, the grid-convergence study and the wall-resolution and
> turbulence-model sensitivity runs behind the computed zero-lift drag — are openly
> available at https://github.com/LORDTEK/meryemAircraft

*Bölüm 8.12'deki "başka bir grup bunu bağımsız deneyebilir" davetinin somut
karşılığı. Depo bağlantısı yayın öncesi eklenecek.*

### Funding

*[Öneri: "This research received no external funding."]*

---

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

**Contributions.** The primary contribution is a framework; the aircraft is the case that
instantiates it. The paper

1. **states the cruise-efficiency penalty of hybrid VTOL as an architectural property** rather
   than a defect of implementation, expresses it as three dimensionless charges — carried hover
   mass, exposed cruise drag, and continuous power sized by the hover peak — shows with
   published figures that the known remedies transfer the penalty between them rather than
   removing it, derives an explicit escape condition, and tests a consequence against an
   independent published sizing study: that the architecture with the best cruise efficiency
   need not be the lightest, which is what that study reports and what a single-metric
   comparison would not anticipate;
2. **shows that architectural comparisons are contract-dependent**, a methodological result
   independent of any particular aircraft: range computed at a fixed fuel fraction is
   independent of take-off mass, so the mass bill never reaches the range column. Three sizing
   contracts are reported side by side and the ranking changes between them;
3. **instantiates the escape condition in a configuration**, audits the three bills against it
   one at a time, and states what the configuration pays instead;
4. **supports the case study with computation rather than assertion** where it could — a
   three-dimensional Reynolds-averaged solution for the zero-lift drag with a measured
   uncertainty budget; a component mass build-up that closes the 50 kg design conditionally and
   does not close the 1000 kg one; a rotational check establishing inertial feasibility of the
   transition; and a viscous, station-by-station solution of the trimmed wing that corrects the
   assumed span efficiency downward; and
5. **states what is not established, as a testable requirement rather than an omission.** The
   aerodynamic pitching moment through the rotation is not known, and the paper reports the
   coefficient that would consume the available control margin instead of estimating the
   coefficient itself.

Items 1 and 2 stand independently of whether this aircraft is ever built. Item 5 is the reason
the paper does not claim that it can be.

**Scope.** This is a configuration study containing no wind-tunnel measurement and no flight
test. Its results are analytical estimates from stated assumptions, with two exceptions computed
here: the zero-lift drag of the wing and centre body, solved three-dimensionally, and the span
efficiency of the trimmed wing, solved station by station with a viscous section method. The
mass budget began as a target rather than a finding; a component build-up replaces it for the
light design, closes conditionally, names the condition, and does not close the heavy design at
all. Section 8 states these limitations, and Supplementary S5 enumerates all of them.

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

---

# 2. Background: seventy years of attempts

The configuration proposed in this paper is new, but the problem it addresses is not,
and neither are several of its ingredients. This section reviews the attempts that
preceded it. The purpose is not to establish priority but to establish two things: that
the need has been pursued continuously for seventy years, and that the pursuit was
rarely abandoned because the aerodynamics failed. Figure 2 places the programmes
discussed below on a single timeline, with the recorded reason each one stopped.

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

The tail-sitter is the most direct answer to the runway: if the aircraft points its thrust line
at the ground it needs no separate lift system, no tilting mechanism and no second propulsion
group. Two American prototypes flew this idea in 1954. The Lockheed XFV-1 never completed the
cycle — its "highly tapered, straight-wing design made the transition to vertical flight only at
altitude, using a jury-rigged, landing-gear cradle for conventional takeoff and landings" [1,2].
The Convair XFY-1 did: it flew vertically in August 1954 and "six transitions to conventional
flight were successfully completed" [2].

**Why the programme stopped matters, because the usual account is wrong.** Two NASA reviews of
United States V/STOL development — one written largely from the author's own flight-test
experience [1] — judge the configuration itself favourably: "good configuration arrangement for
low- and high-speed compatibility", with a high-speed potential near 500 mph. What they judge
poorly is the machinery and the cockpit around it: "poor mechanical control system features
including low actuator response rate"; "difficult to hover precisely over a spot"; "tip-over
tendencies noted when on ground in gusty air" [1]. The landing difficulty is attributed to "the
unusual spatial orientation where the pilot looked over his shoulder and down", to "the
sensitivity to atmospheric turbulence", and to "reduced control power near touchdown" [2].

And then the reason testing ended, stated the same way in both:

> "Six transitions to conventional flight were successfully completed **before testing was
> curtailed because of engine and gear-box reliability problems**." [2]

The XFY-1 was not stopped by pilot workload. The workload was real, separately documented and
severe — but what curtailed the testing was mechanical. **Three of the four objections recorded
against these aircraft are objections to 1954 machinery and to a human pilot, not to the
configuration**: actuator response rate, gearbox reliability, and an orientation problem that
exists only because someone is sitting in it. Section 2.5 returns to what that leaves.

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

---

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
the vehicles examined, and is explicit about the cause:

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

**A consequence that can be checked against published work.** If the framework is right, a
configuration carrying a dedicated lift system should show lower cruise efficiency *and* higher
design gross weight than one that does not, for the same mission. A NASA study sizing five
concept vehicles against a common mission reports exactly that ordering, from a quadrotor at an
effective lift-to-drag ratio of 4.9 and 3 678 lb to a lift-plus-cruise turbo-electric at 8.5 and
7 271 lb [7]. The tilt-wing in that set reaches 8.6 — **higher than every lift-plus-cruise
entry** — which is the point: it carries no dedicated lift system, and it is the one
configuration in the table that uses the same hardware in both regimes. The framework does not
predict the numbers; it predicts the ordering, and the ordering holds.

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

---

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
and no dedicated lift system. The only moving aerodynamic device is a variable-extension strip on
the lower surface, described in Section 4.4, which exists solely because roll cannot be
produced by propellers alone. Figure 4 gives three orthogonal views of the light
reference design and Figure 5 a general view of the same geometry.

## 4.2 Planform

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
so that band does not transfer on its own authority. Section 8 lists it among the limitations.

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
25.3 kg m⁻² and a stall speed of 20.1 m s⁻¹ against a cruise speed of 30 m s⁻¹. Figure 6 gives
the distributions.

## 4.3 Propulsion

Every propeller is a coaxial counter-rotating pair, for one reason worth stating narrowly:
**reaction torque.** A single propeller applies to the airframe a torque equal and opposite to
the one it applies to the air, acting about the yaw axis in hover and the roll axis in cruise,
and it must be opposed continuously — by a control surface, which costs drag, or by differential
thrust, which costs a control channel. A counter-rotating pair does not produce it.

The pairs are of fixed geometry: no cyclic pitch, no collective, no variable mechanism. **This
has a consequence for the tip pairs in cruise that Section 5.2 works out** — unable to feather,
they must either turn at the zero-shaft-torque condition or be stopped, and the difference
between those two states is most of the aircraft's zero-lift drag. The torque balance is exact
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
engine from the hover condition — Bill 3 as Section 3 defines it. The electrical path is not
released, and Section 5.3 says so.

## 4.4 Control without control surfaces

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
tip-propeller layout rather than a design choice.

**Roll cannot be produced by propellers at all**, because every pair is coaxial and
torque-balanced by construction. It is the one axis that needs an aerodynamic device, and that
device is the only moving aerodynamic surface on the aircraft: a strip on the lower surface,
inclined at 45° in planform, running 120 % of root chord and reaching 67 % of semi-span,
standing 2 cm proud at its inboard end and 6 cm at its outboard end. **Extension is the control
variable** — the strip is modulated, not switched.

Roll inertia computed from the component mass distribution is 25.0 kg·m², two and a half times
the pitch inertia, and the roll damping derivative from a helix-angle vortex-lattice solution is
|C_l_p| = 0.358, giving a damping slope of 77.6 N·m per rad s⁻¹ and a roll time constant of
0.32 s. **Twenty degrees per second at cruise therefore requires 27.1 N·m.** The strip's own
force as a swept fence, at an upper-bound normal-force coefficient of 1.3, supplies 11.3 N·m —
about a third. The remainder must come from the second mechanism, the change the strip makes to
the circulation of the half-wing it sits on, which asks for **ΔC_L ≈ 0.12** over the strip's
span. Measured data on non-planar wings carrying Gurney flaps of two percent chord over the
inboard two-thirds gives lift increments of that magnitude [31], and a lift-enhancing tab study
gives a measured height threshold of 1.5 % chord above which maximum lift-to-drag falls [32].
**Roll authority is therefore sized and supported by measurement on a comparable device, and it
is not closed**: the quantity a future measurement must return is ΔC_L for this strip on this
planform.

**The strip loads the other two axes, and Supplementary S3 quantifies all three couplings.**
Deployed on one side it raises drag there and yaws the aircraft towards the strip — adverse yaw
in the classical sense, 11.3 N·m at the present height law, against 42.8 to 55.9 N·m of yaw
authority, so it costs five to twenty-six percent of the strongest axis. It also pitches the
nose down, by ΔC_m between 0.005 and 0.032 depending on where along the chord the lift increment
acts; the tightest pitching-moment budget in Section 7.6 is 0.050, so at the upper end a
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
sideslip that this paper does not compute. And a 39 mm chord at cruise sits at a Reynolds number
near 80 000, where symmetric sections are measured to be nonlinear about zero incidence — in one
case reversing the slope of the lift curve over a three-degree band [36], which is the band a
toe angle of one or two degrees occupies. **Whether a fairing of that chord develops the side
force credited to it is the open question, not which way to toe it.**

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

---

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

In cruise there is no stopped rotor in the airstream, because there is no rotor that stops. The
nose pair is the cruise propulsor and runs at its design condition throughout. The quarter of
lift-to-drag ratio that Section 3.3 reports as the measured cost of installing hover hardware is
not incurred — not reduced, not mitigated, but **absent**, because the hardware that causes it
does not exist here. Nor is there a retraction mechanism, so the transfer of Bill 2 into Bill 1
does not occur either. Where lift rotors are retained, keeping their drag small needs an
indexing mechanism to stop them at a favourable azimuth, or a retraction mechanism to stow them;
both are mass and both are failure modes, and a configuration with no rotor to stop needs
neither.

**That carries a condition the paper had not stated, and it is a sharp one.** The four tip pairs
*are* rotors, and the claim holds only if they do not stop in cruise. Their eight discs sweep
0.251 m², **12.7 percent of the wing area** — not a small object to leave in the airstream in
the wrong state:

| Tip rotors in cruise | ΔC_D0 | of the 0.0248 assumed |
|---|---:|---:|
| turning at zero shaft load, blades at low incidence | 0.0003 – 0.0008 | 1 – 3 % |
| stopped edge-on, at a chosen azimuth | 0.0008 | 3 % |
| **stopped broadside, azimuth uncontrolled** | **0.015 – 0.018** | **61 – 74 %** |

**The difference between the first and third rows is the difference between a configuration that
works and one that does not**, and it is robust to the coefficients assumed, because the two
states differ by a factor of thirty. The second row shows why stopping them is survivable only
if azimuth is controlled — which is the indexing mechanism this section has just claimed the
configuration does not need.

**The resolution costs nothing, and it is a control state rather than hardware.** A fixed-pitch
propeller left free settles at the advance ratio where net shaft torque is zero: inner sections
drive, outer sections retard, and they balance. The shaft then does no work, so the motor
neither drives nor brakes and the electrical cost is controller standby draw and bearing losses.
The blades sit at low incidence with attached flow, which is the first row. **The tip rotors are
therefore held in cruise at the zero-shaft-torque condition — neither stopped nor driven** — and
this is the state assumed throughout Section 6. It is worth naming because both neighbouring
states are wrong: driven, they cost propulsive power; stopped without azimuth control, they cost
most of the aircraft's zero-lift drag.

What Bill 2 *is* paid, and this is why the heading says reduced rather than removed, is the tip
frames. They are structure in the airstream that a conventional aircraft does not carry, and at
the light design point they contribute ΔC_D0 = 0.0043 — **about twelve percent of cruise drag**.
That is the honest figure and it is carried in the ledger of Section 5.4.

**The fairing on those frames is not only a drag measure.** The frames are the only surfaces
standing perpendicular to the wing plane, and the planform supplies no directional stability at
all, so the fairing is also the vertical surface that provides it. Sized against the criterion
the tailless literature recommends — C_n_β greater than 0.001 per degree [19] — the chord
required over the combined frame length is 39 mm, against the 50 to 70 mm a 20 mm faired strut
carries in any case. The two requirements do not conflict, and the directional one is the looser;
but the frame cross-section is now constrained from two directions, and a selection made on drag
alone would be made on half the evidence.

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

The honest ledger has five entries.

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

**The twist needed to trim.** Section 7.6 finds that the configuration trims at cruise with
nine degrees of tip washout, reflex being an order of magnitude short of the moment required.
Washout is not free: it costs span efficiency, and the cruise lift-to-drag ratio falls from
12.65 to 12.11 — **4.3 percent**. This entry was missing from earlier versions of this ledger,
and it is worth being precise about what it is a payment for. It is not one of the three bills
of Section 3, which are charged for having a hover capability; it is charged for being
tailless, and a tailed aircraft of the same architecture would not pay it. It belongs here
because this configuration is tailless, and because a ledger that omitted it would be
flattering rather than honest.

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

Supplementary S6 sizes three architectures against the same mission — this tail-sitter, a
lift-plus-cruise aircraft, and a tilt-rotor — under three different sizing contracts: fixed fuel
fraction, fixed fuel mass, and fixed maximum take-off mass with fixed payload. All twelve cells
are given there with their sensitivity sweeps. The headline is that the ordering does not depend
on which contract is used:

| | Tail-sitter | Lift + cruise | Tilt-rotor |
|---|---:|---:|---:|
| Disc loading, N m⁻² | **440** | 880 | 7 500 |
| Total hover time, min | **20.5** | 16.5 | 12.1 |
| Cruise speed, km h⁻¹ | 100 | 180 | **252** |
| Practical range, km | 42 | 107 | **203** |

**What this comparison does and does not support.** It supports the claim that the three bills
are real and that a configuration avoiding them buys hover endurance and disc loading. It does
**not** support a claim that this configuration is better: the competing architectures are
modelled from published mass fractions at a coarser level of detail than the one proposed here,
which is modelled from a component build-up. **Comparing a build-up against a fraction favours
whichever is modelled more optimistically**, and this study cannot rule out that it is this one.
Section 8 states the comparison as conditional on that asymmetry.

---

# 6. Reference designs at two scales

A configuration argument is only as good as its willingness to become a number. This
section sizes two aircraft from the arrangement of Section 4 — one at 50 kg and one at
1000 kg, a factor of twenty apart in mass — using the same equations, the same
assumptions and the same architecture. The two points are not a light version and a
heavy version of different aircraft. They are the same aircraft at two sizes, and the
purpose of presenting both is to show that the proportions hold.

Every number below is calculated, not measured. Section 8 says what that means.

## 6.1 Sizing method

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
e = 0.85; C_D0 = 0.0248 for the light design, which is generous for a clean blended-wing body
and absorbs the tip-frame contribution of Section 5.2 — that contribution is 0.0043, or
seventeen percent of the assumed value, so the assumption is self-consistent rather than
optimistic. Both are carried as assumptions throughout, so that every downstream figure rests
on one stated basis. Section 6.6 computes both and reports what the computation does to them:
it bounds them rather than replacing them, which is a weaker but more honest claim.

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

One qualification applies throughout: this is the scaling of the analytical sizing model — of
powers, loadings and mass *fractions*. Whether the heavy design's structure closes depends on
how shell areal density grows with size, which was not measured. Figure 11 shows the two
designs at a common scale. Four properties are preserved and one is not.

**Disc loading is held constant** — 44.2 and 43.7 kg m⁻². This is the rule that governs the
sizing rather than a coincidence of it. Hover power per unit weight is √(DL/2ρ), so fixing disc
loading fixes specific hover power: hover power rises from 10.9 kW to 216.2 kW, a factor of 19.8
against a mass factor of 20. **Hover power grows linearly with mass rather than as the L^3.5 of
the classical result**, and that is the whole benefit of fixing it. The cost is that disc area
must then grow as L³ rather than L², which for a fixed number of propellers is impossible. The
architecture has two ways out and uses both: a coaxial pair may be added at no architectural
cost, since every pair is torque-balanced on its own; and geometric similarity is not held.

**The propeller therefore grows faster than the airframe.** Wing loading rises from 25.3 to
45.0 kg m⁻², so span grows by 3.35 against the 4.50 by which the main propeller must grow. The
ratio of propeller diameter to span rises from 0.35 to 0.47: the heavy design is not the light
design photographed from further away, and its propeller occupies almost half its span. Nothing
in the argument fails because of this — the propeller is the nose of the aircraft rather than an
appendage, and disc loading is what is being held — but the claim that the configuration keeps
its proportions applies to the quantities named here and not to every dimension. Much above
1000 kg, a single nose pair can no longer hold the disc loading and a second must be added.

**The buffer fraction is preserved** (3.6 % of MTOW at 50 kg, 4.0 % at 1000 kg), so the
mechanism by which Bill 3 is avoided does not degrade with size, and **the frame drag fraction is
preserved** because frontal and wing area both scale as L².

**Transition time does not scale, and this is the exception.** The rotating moment follows
M = Iα with I ∝ mL², so the moment needed to turn the aircraft in a fixed time grows much
faster than the aircraft. Scaling the light design's two-second rotation to 1000 kg would demand
221.5 kW from the tip propellers — 102 % of hover power, which is to say it is not available:

**Table 4.** Tip-propeller power required to rotate the heavy reference design.

| Rotation time | Tip-propeller power, 4 total | Fraction of hover power |
|---:|---:|---:|
| 2 s | 221.5 kW | 102 % |
| 3 s | 65.6 kW | 30 % |
| 4 s | 27.7 kW | 13 % |
| **5.1 s** | **13.4 kW** | **6 %** |

**The rule is that a larger aircraft turns more slowly.** The heavy design rotates in 5.1 s at
six percent of hover power — not a round number but the rotation time at which it holds the same
control margin the light design holds at two seconds (Section 7.6). The constraint is less costly
than it looks, because Section 7.4 shows a slower rotation loses *less* altitude: the scaling
penalty on transition time works with the penalty on control power rather than against it. The
classical objection to scaling a VTOL aircraft — hover power growing as L^3.5 against power
available as L³ — is removed on the hover side by fixing disc loading. It is not removed on the
transition side, and Table 4 is where it reappears: **the rotation is the one place in this
aircraft where the square–cube relation is still paid in full.**

## 6.5 Context

The following aircraft occupy the same mass range. They are listed to locate the reference
designs in a real field, not to rank them.

| Aircraft | MTOW | Payload | Payload fraction |
|---|---:|---:|---:|
| HAVELSAN BAHA [8] | 28 kg | 2 kg | 7.1 % |
| Textron Aerosonde Mk 4.7 VTOL [9] | 45.4 kg | 9.1 kg | 20.0 % |
| Baykar KALKAN [10] | 75 kg | ~3 kg internal | 4.0 % |
| HAVELSAN BULUT [11] | not published | 5 kg | — |
| Elroy Air Chaparral [12] | 865 kg | 136 / 227 kg | 15.7 / 26.2 % |
| Sabrewing Rhaegal-A [13] | 1400 kg | 360–450 kg | 25.7–32.1 % |
| Pipistrel Nuuva V300 [14] | 1700 kg | 408 kg | 24.0 % |

All entries are from manufacturers' published material; payload definitions are not consistent
between them and empty weights are generally not published.

Three statements can be made and a fourth cannot. The field is real and populated at both ends
of the range. Payload fraction rises with size across it, from a few percent to roughly a
quarter, which is the ordinary consequence of fixed costs not scaling down. And **none of these
aircraft connects an internal-combustion engine directly to a lifting rotor** — every one uses
either a generator or separate electric lift, which is independent confirmation that the series
arrangement of Section 4.3 is the practical choice at this scale rather than an unusual one.

**The fourth statement — that the reference designs outperform these aircraft — is not made.**
Sections 6.2 and 6.3 are calculated from a mass budget with an unpaid structural margin; this
table describes aircraft that exist and fly. Placing a calculation beside a measurement and
declaring a winner would be a category error. Several entries are also fully electric, for
which endurance is set by battery specific energy rather than by configuration, so comparing
them with a fuel-burning design would compare energy sources rather than architectures. What
could properly be compared, once such aircraft are built, is **range at similar payload** — a
configuration carrying a comparable load further is making an architectural claim, while one
carrying a heavier load is making a claim about mass budgeting, which is the least validated
part of this study.

## 6.6 Independent checks on the two assumed coefficients

Both coefficients carried through Sections 6.2 and 6.3 were assumed. Both have since been
computed, and the computations are reported in full in Supplementary S1. Neither replaces its
assumption in the figures above — those are quoted on one stated basis throughout — but each
bounds it, and the direction of each is stated here.

**Zero-lift drag.** A Reynolds-averaged solution of the wing and body gives C_D0 between
0.0120 and 0.0148, against the 0.0248 assumed. The spread is the turbulence closure:
0.01475 with Spalart–Allmaras and 0.01201 to 0.01253 with k-ω SST, eighteen percent apart
at matched wall resolution. **The assumption lies above the whole of that range**, so it is
conservative rather than optimistic. Two things S1 does not settle: the solutions are fully
turbulent, so the clean-surface figure of 0.0073 from the strip method is untested and the gap
between it and 0.0120–0.0148 is now the largest single uncertainty in the zero-lift drag; and
the wall-resolved SST case admits more than one stationary solution, two converged starts
settling 4.3 percent apart in the pressure component.

**Span efficiency.** A vortex-lattice solution gives an inviscid span efficiency of 0.990 for
the untwisted planform and 0.859 for the wing twisted to trim. Those are not the quantity the
drag build-up needs: an Oswald-type efficiency also carries the viscous drag due to lift. An
earlier version of this paper converted between them with a borrowed rule of 85 to 90 percent
and reported an implied value of 0.735 to 0.78. S1 computes the conversion instead, on this
planform, by calling the section solver at **each spanwise station's own local lift
coefficient** rather than at zero lift and integrating the profile drag across the span — the
two-dimensional-viscous-coupled-to-three-dimensional-circulation construction of the non-linear
vortex-lattice literature [40]. Before any number is taken from it, the strip decomposition is
checked against the solver it comes from: the strip loads reproduce the solver's own lift
coefficient to six decimal places.

| | Inviscid e | **Oswald e** | Ratio |
|---|---:|---:|---:|
| Untwisted planform | 0.990 | 0.931 | 0.940 |
| **Trimmed, −9° washout** | **0.859** | **0.817** | **0.951** |

**The borrowed rule was wrong in the favourable direction and the conclusion is unchanged in
the unfavourable one.** The viscous penalty is 5 to 6 percent rather than 10 to 15, but the
trimmed wing starts from 0.859, so the Oswald efficiency lands at **0.817 — below the assumed
0.85 by 3.9 percent**. At that value the cruise lift-to-drag ratio is **11.87 against 12.04**,
and the range figures of Section 6.3 are optimistic by the same 1.4 percent. Two limits belong
with the number: the vortex-lattice sections are symmetric, so a cambered section reaching the
same local lift coefficient at lower incidence would carry less drag and the figure is a
**lower bound**; and strip integration ignores sweep, which at 45° at the root is not a small
omission, though the alternative — simple-sweep theory — halves the profile drag, which is a
sign that the transformation does not apply to skin friction rather than a measure of the
uncertainty.

**What the vortex-lattice method is being asked for, and a bound on it that has no bound.**
Four results here come from a vortex-lattice solution: the span efficiency, the neutral point,
the twist required to trim, and the roll damping. Falkner separates the quantities the method
settles quickly — spanwise circulation, local aerodynamic centre — from those it does not, and
every quantity taken here is of the first kind [24]. But a published comparison on a
blended-wing-body of this class found the vortex-lattice lift coefficient low by **thirty to
thirty-eight percent** against RANS, and excluded the method from its trim analysis on that
basis [39]. The deviation there is nearly constant with incidence, which is the signature of a
multiplicative error in the magnitude of the loading rather than an error in its distribution —
and a factor common to lift and moment cancels in a ratio of derivatives. That argument depends
on the moment scaling with the lift, and the pitching-moment comparison in that source is
published with its values withheld. **The vortex-lattice results here therefore carry an
untested magnitude error of unknown size, bounded above by a published comparison on a similar
configuration, and every use made of them is of a kind a magnitude error does not disturb.**
Section 8 lists settling this as the one exposure in the aerodynamic chain with no bound at all.

## 6.7 A component build-up of the mass budget

The sizing above assumes an empty-mass fraction rather than deriving one. Supplementary S2
builds the 50 kg design's mass item by item — structure from wetted area and an assumed shell
areal density, tip frames sized by a vertical landing case, propulsion, energy, avionics and
systems — and reports the break-even value of every assumption in it.

**The build-up closes, and it closes on one number.** The total is 11.88 kg against a 14.08 kg
allowance, leaving 2.2 kg unallocated. It closes on the condition that the average structural
areal density does not exceed **1.78 kg m⁻²**, against the 1.5 assumed; at 1.78 the payload is
gone. A doctoral study of unmanned-aircraft sizing reports 1.05 kg m⁻² for a small UAV's
monolithic composite fuselage shell supported by an internal structure [50], which places the
assumption inside the range small composite airframes are built to without establishing that
this airframe reaches it — that shell is carried by an internal structure, while this one is
the wing and carries flight loads directly.

**The build-up came in lighter than the target, and that is a warning rather than a result.**
Paper aircraft are habitually lighter than the aircraft that get built. What S2 does not
contain is buckling, torsion, local load introduction, aeroelastic sizing, fasteners, adhesive,
paint, or the mass of anything the design has not yet specified — and the 2.2 kg of margin is
what all of those must fit into. Section 8.2 states the item as bounded from below rather than
demonstrated.

---

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

The transition was simulated as a two-degree-of-freedom point mass. The body angle is driven
from zero to ninety degrees over a rotation time t_r; thrust acts along the body axis, lift
perpendicular to the velocity vector and drag opposite to it; the lift curve is linear to stall
and a flat-plate relation beyond it. Altitude loss is the lowest point of the trajectory
relative to the entry altitude. Figure 10a plots both reference designs at four
thrust-to-weight ratios; the tables at T/W = 1.2 are:

| t_r | Light, 50 kg | | t_r | Heavy, 1000 kg |
|---:|---:|---|---:|---:|
| 1 s | −14.2 m | | 2 s | −20.9 m |
| 2 s | −9.1 m | | 3 s | −7.2 m |
| 3 s | −0.8 m | | 4 s | −1.4 m |
| 4 s | 0 m | | 5 s | 0 m |

**The relationship is monotonic in the direction opposite to the one usually assumed.** It is
frequently supposed that a tail-sitter should rotate as fast as possible, on the reasoning that
it is unsupported during the rotation and therefore falls for a time t_r, giving a loss
proportional to t_r². **That reasoning is wrong, and the error is in its premise:** the aircraft
is not unsupported. Vertical support is T cos θ + L, and a slow rotation keeps cos θ large during
exactly the interval in which speed, and therefore lift, is being built. A fast rotation
collapses cos θ before there is any lift to replace it, and the aircraft falls precisely because
it hurried.

The practical consequence is a simplification rather than a trade. Control power required to
rotate in time t_r scales as 1/t_r², so a slow rotation is cheap in authority; and altitude loss
also falls with t_r. **Both constraints point the same way**, so there is no optimum transition
time to be found between competing penalties — the rotation time is set by what the actuator can
do, not by a balance, and Section 7.6 shows that is where both reference times come from.

**Entering the rotation while still climbing removes the penalty entirely.** The aircraft
reaches transition altitude by climbing, so it need not stop and hover first. At an entry climb
of 5 m s⁻¹ the altitude loss is zero for every profile at both design points, and acquiring that
climb rate is nearly free: at T/W = 1.2 the vertical acceleration is 0.2 g, so 5 m s⁻¹ is reached
in 2.6 s over 6.4 m, and the kinetic energy involved is 625 J against a fuel energy of 103 kWh.
**The reference profile is therefore to enter the rotation at 5 m s⁻¹ of climb**, and the
altitude-loss column is zero throughout.

**The test is a lower bound.** A point mass carries no rotational dynamics, no aerodynamic
pitching moment and no control-power limit; Section 7.6 supplies the rotational budget that this
model omits, and Section 8 states what neither supplies.

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

## 7.6 Whether there is enough authority to rotate, and whether it trims

Rotating the airframe through ninety degrees is the manoeuvre this configuration must perform
with four small propellers and no control surfaces. Supplementary S4 carries the full budget —
inertia derivation, rotation profiles, centre-of-gravity window, twist sweep and the measured
section evidence. This section states what it returns.

**The rotation closes at the actuator limit rather than clear of it.** The pitch inertia
derived from the component build-up is 9.81 kg·m² for the light design and 2 503 kg·m² for the
heavy one. On the cheapest rotation profile the tip propellers carry the manoeuvre with a margin
of **1.49** at the light design point and **1.57** at the heavy one; on a smoothly commanded
profile the margins fall to 0.99 and 1.05. The reference rotation times — two seconds light,
5.1 seconds heavy — are therefore lower bounds set by the actuator, not comfortable choices,
and the margin narrows with size.

**Resolving the requirement along the trajectory changed the question rather than merely
quantifying it.** The aircraft does not reach ninety degrees of incidence: the body rotates
through ninety, but the relative wind rotates with it, and **peak incidence is 17.5° for the
light design entering in a 5 m s⁻¹ climb and 21.6° entering from level hover**. The
high-incidence part happens at low dynamic pressure, where the margin tolerates a pitching-moment
coefficient of 0.205; the tight part is the *end* of the rotation, where incidence is small and
speed is high, and the budget there is 0.050. **The demanding case is not the post-stall middle
but the attached-flow end**, which makes it a trim question rather than a stall question.

One mechanism was omitted and including it improves the case. The inboard half of the wing lies
in the nose propeller's slipstream, where the local flow is faster and more axial, so the
effective incidence there is lower than the geometric one. Applying the slipstream relation used
in the tail-sitter literature [23] gives **four to eight degrees effective against seventeen to
twenty-two geometric**: half the wing is not post-stall at the moment of peak incidence. The
measurement still owed concerns the outboard half.

**Static stability is shown, and the trim chain closes by twist.** A vortex-lattice solution
places the neutral point at 0.859 m from the root leading edge — 34.4 percent of mean
aerodynamic chord — and the packaging centre of gravity at 80.2 percent of root chord gives a
**static margin of +12.5 percent of mean aerodynamic chord**, with a pitching moment of 0.056 to
be balanced at the cruise lift coefficient. Two published benchmarks place that window
favourably: a blended-wing UAV of this class reports its own margin of 0.081 as "marginally
outside the typical range for static longitudinal stability", given as 0.1 to 0.3, and its
C_m_α of −0.086 per radian against a typical −0.3 to −1.5 [41]. This configuration sits inside
both at 0.125 and −0.48 per radian.

**Reflex does not supply the 0.056, and this is now a measured statement rather than an
inference.** Nine reflexed and low-moment sections have been tested in tunnels that measure
pitching moment. Exactly one returns a positive value — NACA 2R212 at **+0.004** [17], one
fourteenth of what is needed. The three 1930s reflexed sections whose mean lines were shaped
from thin-aerofoil theory to give *zero* quarter-chord moment measure "practically zero", from
−0.001 to −0.007 [45]; the four sections of the NACA 4400R family were designed to a target of
**−0.03** and the report states that "the design pitching-moment coefficient was realized" [46].
**Reflex, as actually built and measured, is a device for removing negative pitching moment
rather than for producing positive pitching moment.** Two costs are measured with it, and both
bear on a tail-sitter: maximum lift falls by about twelve percent in the first family and ten
percent in the second — and maximum lift is what a tail-sitter needs at the high-incidence end
of transition. A flying tail-sitter shows where the positive moment actually comes from: it uses
a symmetric section, and "the upward trim of elevons makes the symmetric airfoil to have
reflexed camber line", producing the positive moment at the aerodynamic centre [51]. The reflex
that trims that aircraft is a deflected control surface held permanently out of line, not a
property of its section.

**Nine degrees of tip washout trims this aircraft at cruise with no camber at all**, and the
vortex-lattice model computes it directly because the mechanism is geometric rather than
sectional: on a swept wing the tips lie well aft, so negative tip incidence produces a nose-up
moment about the centre of gravity. The price is a span efficiency of 0.865 instead of 0.993 and
a cruise lift-to-drag ratio of 12.11 instead of 12.65 — **4.3 percent of cruise efficiency, paid
to be tailless**, and entered in the ledger of Section 5.4 as its fifth item. The reflex route
is not free either: a blended-wing UAV trimming by reflex rather than twist records that
carrying reflex over a wide span "is not conducive to the improvement of overall lift-to-drag
performance" [44]. **Both roads to trim on a tailless configuration cost cruise efficiency**,
which is the reading Section 5.4 places on the 4.3 percent: it is the price of having no tail,
not the price of choosing the wrong way to do without one.

The twist earns its cost three times over. It closes the trim chain; on a swept planform it
delays tip stall, which on a tailless aircraft matters more than usual because a tip stall moves
the centre of pressure forward and there is no tail with which to argue; and it inverts the
stall sequence behind a blended-wing pitch-break. That third mechanism was found late and does
not depend on aspect ratio: in a blended-wing-body analysed by both a low-fidelity method and
RANS, the moment prediction departs above eight degrees because "the main wing stalls before the
main body, causing the BWB to pitch-up" [39]. Washout makes the root stall first, and on a
blended wing the root is the body.

**The pitching moment through transition remains this study's largest open item, and the reason
nobody computes it has been measured.** A small blended-wing-body UAV was analysed by RANS and
then tested in a wind tunnel at a Reynolds number of 2.0 × 10⁶: from −6° to 10° of incidence
"both the aerodynamic force values and the variation trends are in quite good agreement"; from
10° to 26° they "show remarkable differences between the numerical and experimental results"
[44]. The same boundary appears at lower fidelity — a vortex-lattice solution of this class of
configuration departs above eight degrees [39] — and the incidences this aircraft passes through
lie inside that band. **Three methods of three fidelities fail at the same place, and the
highest of them fails against measurement.** The item therefore belongs to measurement rather
than to computation, and Section 8 asks for it as measurement. The same tests found the
blended-wing configuration to have "soft-stall performance", which is the benign end of the
range the pitch-up literature describes.

The field does not have this term either. A transition-optimisation study with outdoor flight
trials carries **no pitching-moment term at all** [28]; a second carries a linear one and
flight-tested the question this configuration asks, reporting that without elevons its
tail-sitter had "a well-controlled attitude response during hovering and transition" but that
manoeuvres in level flight caused "an oscillatory attitude response" with "motor saturations
observed", attributed to "the increased aerodynamic moment but decreased motor thrust at
high-speed level flight" [29]. A survey records the same outcome for a separate vehicle: "able
to achieve transition to forward flight, but they had poor control over the vehicle once in
forward flight" [30]. A third carries a nonlinear C_m(α) but borrows the curve and closes the
remaining discrepancy with an adaptive law [42]. **Every one of them obtains the transition
aerodynamics by borrowing, fitting or adapting, and none by measuring the vehicle it flies.**
Two independent programmes, different vehicles, the same division — transition passed, forward
flight difficult — and that is the same structural tension this section derives from the moment
budget: the tight case is the end of the rotation and beyond, where aerodynamic moment grows as
V² while propeller thrust falls.

---

# 8. Limitations

This is a configuration study. It contains no experimental validation of any kind, and
the numbers in it are the output of elementary methods applied to a set of assumptions.
This section states what those limits are, in enough detail that a reader can judge how
much weight each result will bear. Several of the items below were discovered during the
study and changed its results; they are recorded here rather than smoothed away.

## 8.1 What is not shown

**No part of this study has been validated experimentally.** No wind-tunnel test, no flight
test, no hardware. Everything here is calculation, and the calculations rest on assumptions
stated in the sections that use them. Supplementary S5 enumerates every limitation item by item
with the break-even value of each assumption that has one. This section states the ones that
bear on the conclusions.

## 8.2 The three that could change a conclusion

**The buffer's specific power is the most exposed number in the paper.** Bill 3 is avoided by
sizing the engine for cruise and supplying the hover excess from a battery buffer, and the light
design's buffer implies **4.61 kW kg⁻¹**. A 24S nickel–cobalt–manganese pack designed, built,
bench-tested from 0.2 C to 10.68 C and flown in an electric VTOL aircraft measures **724 W kg⁻¹**
continuous for the unit pack and **892 W kg⁻¹** for the flight system, reaching roughly
1.5 kW kg⁻¹ at its maximum tested rate with a thermal margin of 4.9 °C [47]. A NASA-funded design
study adopts 4 kW kg⁻¹ and states that this is "about twice that of existing batteries" [48].
Sized at the measured thermal ceiling the buffer is **5.5 kg rather than 1.8 kg**, against 2.2 kg
of unallocated mass; sized at the measured continuous figure, 9.3 kg. **The light design's mass
budget does not close at any measured specific power.** The defence available earlier — that a
short-duration buffer is a different product from an energy-optimised automotive pack — does not
survive, because the source above *is* that product. What would resolve it is a pack
demonstrating three times the measured specific power at acceptable temperature, or a heavier
buffer carried at the cost of payload fraction.

**The mass budget is bounded from below and the bound is thin.** The component build-up of
Supplementary S2 totals 11.88 kg against a 14.08 kg allowance, on the condition that average
structural areal density does not exceed **1.78 kg m⁻²** against the 1.5 assumed; at 1.78 the
payload is gone. A doctoral study of UAV sizing reports 1.05 kg m⁻² for a small UAV's monolithic
composite fuselage shell supported by internal structure [50], which places the assumption inside
the range small composite airframes are built to without establishing that this airframe reaches
it — that shell is carried by internal structure, while this one is the wing and carries flight
loads directly. The build-up contains no buckling, torsion, local load introduction, aeroelastic
sizing, fasteners, adhesive or paint, and 2.2 kg is what all of those must fit into. **Paper
aircraft are habitually lighter than the aircraft that get built.**

**The transition pitching moment is not computed, and Section 7.6 shows the computation is not
currently reliable for anyone on this class of configuration.** Three methods of three fidelities
fail above roughly ten degrees of incidence, the highest of them against wind-tunnel measurement
[39,44], and the incidences this aircraft passes through lie inside that band. **This item
belongs to measurement.** It asks for the pitching moment to about twenty-two degrees at low
dynamic pressure, on the outboard half of the wing — the inboard half lies in the slipstream and
sees four to eight degrees — and for trim at cruise incidence.

## 8.3 What is assumed rather than derived

The planform's sweep, taper and thickness distributions were **chosen, not optimised**. The
centre of gravity is a packaging assumption. The zero-lift drag coefficient of 0.0248 and the
span efficiency of 0.85 are assumptions; Section 6.6 bounds both by calculation and neither
replaces its assumption — the span efficiency computes to **0.817, optimistic by 3.9 percent**,
worth 1.4 percent of cruise lift-to-drag ratio and of the ranges quoted. Torque balance is exact
at cruise only, leaving a small residual in hover. The comparative sizing of Section 5.5 is
conditional on the two competing architectures being modelled at the same level of detail as
this one, which they are not: they are modelled from published fractions.

**The vortex-lattice results carry an untested magnitude error.** A published comparison on a
blended-wing-body of this class found the vortex-lattice lift coefficient low by thirty to
thirty-eight percent against RANS [39]. Section 6.6 argues that a near-constant multiplicative
error of that kind cancels in the ratios this paper takes from the solution — neutral point,
static margin, twist effectiveness — but the check that would confirm it is withheld in that
source. **This is the one exposure in the aerodynamic chain with no bound at all.**

## 8.4 What is sized but not closed

Attitude control is sized in every axis and closed in none. Roll asks for **ΔC_L ≈ 0.12** from
the strip, which published fence and Gurney data make plausible without establishing it for this
geometry, and the strip's measured weaknesses — degradation in turbulence, contested post-stall
behaviour, a dead band below seven percent of travel — all fall in conditions this configuration
uses it in. Directional stability asks for a **39 mm** fairing chord on a frame that already
exists, at a Reynolds number near 80 000 where thin symmetric sections are measured to be
nonlinear about zero incidence; whether such a fairing develops the side force credited to it is
not established, and the toe-out its aspect ratio requires carries a stall-related failure mode
at large sideslip that has not been computed. Hover disturbance rejection, ground handling,
crosswind and vertical descent have been checked only to order of magnitude or not at all.

## 8.5 Where this could most efficiently be attacked

Supplementary S5 lists six places. Two have been carried out and are folded into Section 6.6: a
three-dimensional solution for the centre body, and a viscous solution of the twisted planform
station by station. Of the remaining four, the one with no bound at all is a Reynolds-averaged or
panel solution of this planform's loading, to bound the magnitude question above. **None of the
four requires an experiment**, and the configuration is described in enough detail in Sections 4
and 6 for another group to attempt any of them independently. The computational setup, the
grid-convergence study and the record of what failed along the way are in the repository, so
every result here can be re-run and checked rather than taken on trust.

---

# 9. Conclusion

Hybrid vertical take-off aircraft pay for their vertical capability, and the payment is
architectural rather than a defect of implementation. It appears in three currencies — the mass
of hardware carried but unused, the drag of hardware exposed but inactive, and a power system
sized by a condition that holds for about two percent of the flight — and **each known
architectural move reduces one of them by increasing another**. A NASA sizing study of four VTOL
architectures reaches the same conclusion from the opposite direction, finding the
lift-plus-cruise concept the heaviest of those examined while also the most efficient in cruise,
and naming the cause as the empty weight carried for hover.

Stating the tax that way makes its escape condition explicit: **it is charged whenever hover and
cruise are served by hardware that is not the same hardware, doing the same job, in the same
orientation.** The configuration described here satisfies that condition rather than
compensating for failing it. The aircraft rotates; nothing on the aircraft rotates relative to
it. A single coaxial pair at the nose provides all thrust in both regimes; four small coaxial
pairs at the tips provide moments and nothing else; and a strip on the lower surface is assigned
the one gap propellers cannot close — the rolling moment, which parallel thrust vectors cannot
produce at any setting or mounting position. There are no elevons, no rudder, no tilting
mechanism, no retraction mechanism and no dedicated lift system.

The configuration was sized at 50 kg and at 1000 kg with the same equations, twenty times apart
in mass. Disc loading is constant by design, which is what keeps hover power growing linearly
with mass instead of as the classical L^3.5; the buffer that decouples the engine from the hover
peak stays under four percent of take-off mass at both points; and the drag fraction charged to
the tip frames is preserved. Three things do not scale, and all three are reported rather than
smoothed: the larger aircraft must rotate more slowly; its propeller grows faster than its span,
so the heavy design is not the light design seen from further away; and these are properties of
the sizing rules, while a component build-up of the structure meets the mass fractions at 50 kg
and does not at 1000 kg.

Two results emerged during the study that changed it. The tip frames, left as circular tubing,
would produce nearly as much drag as the rest of the aircraft — fairing them is a requirement
rather than an option, and the same fairing turns out to be the aircraft's directional stability
surface. And **a slower rotation loses *less* altitude, not more**, because the aircraft is
supported during the manoeuvre rather than falling through it, so entering the rotation while
still climbing removes the altitude penalty entirely in the point-mass model.

**What this paper offers is a configuration and its numbers, not a validated aircraft.** There
is no wind-tunnel data here and no flight test. Of the analyses Section 8 lists as tests of
these results, three have been carried out. A three-dimensional solution for the centre body
narrowed the zero-lift drag without overturning the assumption. A component build-up closes the
light design with 2.2 kg in hand, conditional on a shell areal density at or below 1.78 kg m⁻²,
and does not close the heavy design. And a rotational check shows the tip propellers can turn
the aircraft's own inertia through the transition with a margin of 1.49 at 50 kg and 1.57 at
1000 kg on the cheapest profile — **0.99 and 1.05 on a smooth one**, which is to say both
reference rotation times are actuator-limited lower bounds rather than comfortable choices.

Resolving that check along the trajectory changed the question. The aircraft does not reach
ninety degrees of incidence: the body rotates through ninety but the relative wind rotates with
it, and peak incidence is seventeen to twenty-two degrees — four to eight over the half of the
wing lying in the nose propeller's slipstream. **The tight case is not the high-incidence middle
but the end of the rotation**, where incidence is small and speed is high, which makes it a trim
question rather than a stall one. The configuration is statically stable, with a neutral point
at 34 percent of mean aerodynamic chord and a margin of 12.5 percent, and the moment to be
balanced at cruise is 0.056. Reflex does not supply it: nine reflexed and low-moment sections
have been measured in tunnels that measure moment, exactly one returns a positive value — one
fourteenth of what is needed [17] — and the rest lie between zero and −0.03, because reflex as
actually built is a device for removing negative pitching moment rather than producing positive
moment [45,46]. **Nine degrees of tip washout does supply it**, at a cost of 4.3 percent of
cruise efficiency: the price of having no tail.

That twist also settled an assumption, and not in the paper's favour. Computing the profile drag
of the trimmed wing station by station at each station's own local lift coefficient gives an
Oswald span efficiency of **0.817** against the 0.85 assumed — optimistic by 3.9 percent, worth
1.4 percent of the ranges quoted.

**Attitude control is sized in every axis and closed in none, and that is the honest summary of
its control case.** Roll asks for ΔC_L ≈ 0.12 from the strip, which published fence and Gurney
data make plausible without establishing it here. Yaw is the strongest axis the arrangement has,
at 2.4 times the pitch moment, because differential thrust between the left and right tip pairs
acts through the semi-span; what yaw lacks is not authority but stability, and the surfaces that
must supply it are the same tip-frame fairings. That one member serves as landing structure,
moment arm, propeller mount and directional stability surface is the configuration's own
argument made once more; that none of the four roles has been verified together is its principal
limitation.

An earlier version of this section stated that none of the remaining analyses required an
experiment. **That is no longer true, and the change is the most important thing this study
learned about itself.** Transition controllability rests on a pitching moment that three methods
of three different fidelities fail to predict above roughly ten degrees of incidence — the
highest of them against wind-tunnel measurement — and the paper declines to substitute a reduced
calculation for a measurement.

**What survives independently of that is the framework.** The three currencies, the
demonstration that architectural remedies transfer the penalty rather than remove it, the escape
condition, and the finding that architectural comparisons change their ranking with the sizing
contract chosen — none of these depends on whether this particular aircraft is ever built.
meryemAircraft is the case that shows the escape condition can be instantiated in a real
geometry and carried through to reference designs at two scales. It is not offered as a
validated vehicle, and the paper is careful throughout to say which of its statements are
demonstrated, which are conditional, and which are open. The configuration is described in
enough detail for another group to attempt any of the outstanding analyses independently, and
that is the outcome this paper is written to invite.

---

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
17. Jacobs, E. N.; Ward, K. E.; Pinkerton, R. M. *The Characteristics of 78
    Related Airfoil Sections from Tests in the Variable-Density Wind Tunnel.*
    NACA Report No. 460, National Advisory Committee for Aeronautics, 1933.
    (Reflexed mean-line sections NACA 2R112 and 2R212, pp. 52–53.)
18. Traub, L. W. *Effect of Gurney Flaps on Non-Planar Wings at Low Reynolds
    Number.* Aerospace, 2024, 11 (9), 728. https://doi.org/10.3390/aerospace11090728
19. *An Interim Report on the Stability and Control of Tailless Airplanes.*
    NACA Report No. 796, Langley Research Division, National Advisory Committee
    for Aeronautics, 1944. (Tip fins on swept tailless aircraft, pp. 428–429.)
20. Moul, T. M.; Fears, S. P.; Ross, H. M.; Foster, J. V. *Low-Speed Wind-Tunnel
    Investigation of the Stability and Control Characteristics of a Series of
    Flying Wings With Sweep Angles of 60°.* NASA Technical Memorandum 4649,
    Langley Research Center, August 1995.
21. Bacchini, A.; Cestino, E. Electric VTOL Configurations Comparison.
    *Aerospace* **2019**, 6 (3), 26. https://doi.org/10.3390/aerospace6030026
22. Johnson, W.; Silva, C. NASA concept vehicles and the engineering of advanced
    air mobility aircraft. *The Aeronautical Journal* **2022**, 126 (1295),
    59–91. doi:10.1017/aer.2021.92
23. Folk, S. *Modeling, Planning, and Control for Hybrid UAV Transition
    Maneuvers.* Qualifying examination report, Department of Mechanical
    Engineering and Applied Mechanics, University of Pennsylvania, 2020;
    arXiv:2412.06197, 2024.
24. Falkner, V. M. *The Scope and Accuracy of Vortex Lattice Theory.*
    Aeronautical Research Council Reports and Memoranda No. 2749, Ministry of
    Supply, London, 1952.
25. Smith, C. W.; Bhateley, I. C. *Application of the Vortex-Lattice Technique to
    the Analysis of Thin Wings with Vortex Separation and Thick Multi-Element
    Wings.* NASA report, Fort Worth Division of General Dynamics, 1976.
26. Ugwueze, O.; Statheros, T.; Bromfield, M. A.; Horri, N. An Efficient and
    Robust Sizing Method for eVTOL Aircraft Configurations in Conceptual Design.
    *Aerospace* **2023**, 10 (3), 311. https://doi.org/10.3390/aerospace10030311
27. Shinde, S. D.; Patel, A. A.; Mehta, M. A.; Mehta, A. B.; Kotecha, K.
    Airfoil Selection Procedure, Wind Tunnel Experimentation and Implementation
    of 6DOF Modeling on a Flying Wing Micro Aerial Vehicle. *Micromachines*
    **2020**, 11 (6), 553. https://doi.org/10.3390/mi11060553
28. Li, B.; Sun, J.; Zhou, W.; Wen, C.-Y.; Low, K. H.; Chen, C.-K. Transition
    Optimization for a VTOL Tail-sitter UAV. *IEEE/ASME Transactions on
    Mechatronics* **2020**. doi:10.1109/TMECH.2020.2983255
29. Lyu, X.; Gu, H.; Zhou, J.; Li, Z.; Shen, S.; Zhang, F. *A Hierarchical
    Control Approach for a Quadrotor Tail-Sitter VTOL UAV and Experimental
    Verification.* IEEE/RSJ International Conference on Intelligent Robots and
    Systems (IROS), 2017.
30. Carter, G. I. *Adaptive Control of the Transition from Vertical to
    Horizontal Flight Regime of a Quad-Tailsitter UAV.* M.S. thesis, Virginia
    Polytechnic Institute and State University, 2021.
31. Cheng, Z.; Pei, H. Time Optimal Altitude-Hold Flight Mode Transition
    Strategy for a Class of Ducted Fan Tail Sitter UAV. *Aerospace* **2024**,
    11 (8), 654. https://doi.org/10.3390/aerospace11080654
32. Ross, J. C.; Storms, B. L.; Carrannanto, P. G. *Lift-Enhancing Tabs on
    Multielement Airfoils.* NASA Technical Memorandum 112990, Ames Research
    Center, 1997.
33. Buchholz, M. D. *Lift Augmentation on a Delta Wing via Leading Edge Fences
    and the Gurney Flap.* M.S. thesis; NASA Contractor Report 194793, 1993.
34. *Wind Tunnel Tests on a Tail-less Swept Wing Span-Distributed Cargo Aircraft
    Configuration.* NASA Technical Memorandum 78767, 1978.
35. Yang, J.; Yang, H.; Zhu, W.; Li, N.; Yuan, Y. Experimental Study on
    Aerodynamic Characteristics of a Gurney Flap on a Wind Turbine Airfoil under
    High Turbulent Flow Condition. *Applied Sciences* **2020**, 10 (20), 7258.
    https://doi.org/10.3390/app10207258
36. Selig, M. S.; Lyon, C. A.; Giguère, P.; Ninham, C. N.; Guglielmo, J. J.
    *Summary of Low-Speed Airfoil Data, Volume 2.* SoarTech Publications:
    Virginia Beach, VA, 1996. (Volume 1: Selig, M. S.; Guglielmo, J. J.;
    Broeren, A. P.; Giguère, P., 1995.)
37. Liu, Z.; Li, K.; Sun, X. Influence of Gurney Flap and Leading-Edge/Trailing-Edge
    Flaps on the Stall Characteristics and Aeroacoustic Performance of Airfoils.
    *Fluids* **2025**, 10 (6), 152. https://doi.org/10.3390/fluids10060152
38. Neuhart, D. H.; Pendergraft, O. C., Jr. *A Water Tunnel Study of Gurney Flaps.*
    NASA Technical Memorandum 4071, Langley Research Center, 1988.
39. Panagiotou, P.; Dimopoulos, T.; Dimitriou, S.; Yakinthos, K. Quasi-3D Aerodynamic
    Analysis Method for Blended-Wing-Body UAV Configurations. *Aerospace* **2021**,
    8 (1), 13. https://doi.org/10.3390/aerospace8010013
40. Şugar Gabor, O.; Koreanschi, A.; Botez, R. M. A New Non-Linear Vortex Lattice Method:
    Applications to Wing Aerodynamic Optimizations. *Chinese Journal of Aeronautics*
    **2016**, 29 (5), 1178–1195. https://doi.org/10.1016/j.cja.2016.08.001
41. Lampropoulos, N.; Vouros, A.; Templalexis, I.; Lekas, T. On the Aerodynamic
    Performance of a Blended-Wing-Body, Low-Mach Number Unmanned Aerial Vehicle.
    *Fluids* **2025**, 10 (3), 54. https://doi.org/10.3390/fluids10030054
42. Zhong, J.; Wang, C.; Zhang, H. Transition Control of a Tail-Sitter Unmanned Aerial
    Vehicle with L1 Neural Network Adaptive Control. *Chinese Journal of Aeronautics*
    **2023**, 36 (7), 460–475. https://doi.org/10.1016/j.cja.2023.04.002
43. McIntosh, K. F.; Mishra, S.; Reddinger, J.-P. *An Aerodynamic Feedforward-Feedback
    Architecture for Tailsitter Control in Hybrid Flight Regimes.* arXiv:2312.10761, 2023.
44. Wang, K.; Zhou, Z. Aerodynamic Design, Analysis and Validation of a Small
    Blended-Wing-Body Unmanned Aerial Vehicle. *Aerospace* **2022**, 9 (1), 36.
    https://doi.org/10.3390/aerospace9010036
45. Defoe, G. L. *A Comparison of the Aerodynamic Characteristics of Three Simple
    Reflexed Airfoils in the Normal and Variable Density Wind Tunnel.* NACA Technical
    Note No. 388, Langley Memorial Aeronautical Laboratory, 1931.
46. *Preliminary Report on the Characteristics of the NACA 4400R Series Airfoils.*
    NACA Wartime Report, Langley Memorial Aeronautical Laboratory, 1939.
47. Yu, S.; Jung, Y.-J.; Cho, B.-D.; Lee, G.-S. Design, Fabrication, and In-Flight
    Demonstration of a 24S NCM Battery System for an eVTOL Aircraft. *Batteries*
    **2025**, 12 (9), 317. https://doi.org/10.3390/batteries12090317
48. Barrett, S. R. H.; Brown, A.; Gomez-Vega, N. *Silent, Solid-State Propulsion for
    Advanced Air Mobility Vehicles.* NASA Innovative Advanced Concepts Phase I Final
    Report, Massachusetts Institute of Technology, 2023.
49. Fischel, J.; Watson, J. M. *Investigation of Spoiler Ailerons for Use as Speed
    Brakes or Glide-Path Controls on Two NACA 65-Series Wings Equipped with
    Full-Span Slotted Flaps.* NACA Report 1034, Langley Aeronautical Laboratory, 1951.
50. Pollet, F. *Design Optimization of Unmanned Aerial Vehicles: A Multidisciplinary
    Approach with Uncertainty, Fault-Tolerance, and Environmental Impact Assessments.*
    Doctoral thesis, ISAE-SUPAERO, Université de Toulouse, 2024. (The 1.05 kg m⁻²
    figure is attributed there to Stahl, P.; Roessler, C.; Hornung, M., 2020,
    doi:10.25967/490207.)
51. Lee, H.; Lee, J. D.; Bang, H. *Aerodynamic Model Identification of a VTOL Tailsitter
    UAV Using Sparse Identification of Nonlinear Dynamics.* 34th Congress of the
    International Council of the Aeronautical Sciences (ICAS), 2024, paper 0653.

---

# Supplementary Material

Six supplementary files accompany this paper and are cited from it by number.
They carry the derivations behind the results stated here; each was a section of an earlier,
longer version and is reproduced without abridgement.

- **Supplementary S1** — Independent checks on the two assumed aerodynamic coefficients (3339 words)
- **Supplementary S2** — A component build-up of the mass budget (2404 words)
- **Supplementary S3** — Control axes in full (6336 words)
- **Supplementary S4** — Rotational authority, trim, and the transition envelope (7544 words)
- **Supplementary S5** — The limitations in full (6426 words)
- **Supplementary S6** — The three bills stated formally, and a comparative sizing (2935 words)

The computational setup, the scripts that produce every number here, and a running record
of the corrections made during the study are in the repository this paper cites.
