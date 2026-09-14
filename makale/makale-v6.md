# The Architectural Cost of Hybrid VTOL

---

## Title

**The Architectural Cost of Hybrid VTOL: meryemAircraft, a Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System**

## Authors

Meryem Gülmen <sup>1,\*</sup>, Berke Gülmen <sup>1</sup>, Ömer Gülmen <sup>1</sup>

<sup>1</sup> Independent Researcher, Türkiye; meryemgulmen@outlook.com (M.G.);
berkegulmen@outlook.com (B.G.); lordtek@me.com (Ö.G.)

<sup>\*</sup> Correspondence: meryemgulmen@outlook.com

## Highlights

> **What are the main findings?**
>
> - Hybrid VTOL aircraft pay for vertical flight in three coupled currencies — hover
>   hardware carried through cruise, its drag when exposed, and continuous power sized by a
>   condition holding for some two percent of the flight — and each architectural remedy
>   surveyed here reduces one by raising another.
> - A tail-sitting blended-wing body reaches the escape condition by a route the tilting
>   architectures do not take — the airframe rotates and the propulsors stay fixed — so it
>   carries no pivot, no nacelle actuator and no variable-pitch hub: the propellers hold one
>   orientation from take-off to cruise. Pitch and yaw come from differential thrust between
>   fixed-pitch propellers; roll, which coaxial pairs cannot produce, comes from a single moving
>   strip. What is eliminated is the propulsor-reorientation mechanism, not every moving part.
> - Carrying that case far enough to audit shows what it costs: the free-wheeling drag of its
>   own attitude rotors is a bill the configuration was assumed to avoid, and charging it
>   reverses one of the three range comparisons and leaves a mass advantage of 32 to 36 percent.
>
> **What are the implications of the main findings?**
>
> - Architectural rankings are properties of the sizing contract, not of the architecture.
>   Across the computed drag bracket the lift-plus-cruise layout leads on range under equal
>   fuel fractions by 24 to 45 percent, the tail-sitter leads under equal take-off mass by 29
>   to 43, and under equal fuel mass the sign changes inside the bracket. **A ranking quoted
>   without its contract is not a result.** The architectural claim made here is on a different
>   axis from all of these: it is the absence of a rotating mechanism, which no contract moves.
> - The configuration is not shown to be flyable: its 50 kg reference budget needs a battery
>   specific power 3.8 times the highest rate yet measured on a flown pack, and re-closes 38
>   percent heavier at that measured rate; transition controllability rests on a pitching
>   moment no current method predicts reliably.

## Abstract

Hybrid vertical take-off and landing (VTOL) aircraft pay for runway independence in cruise
efficiency. That cost is architectural, charged in three coupled currencies — hover hardware carried
through cruise, its drag when exposed, and continuous power sized by a two-percent-of-flight
condition — each remedy reducing one by raising another. Escape requires one set of hardware serving both regimes in one orientation, with the hover peak
from a buffer. Tilting architectures meet it by rotating their propulsors, at the cost of a pivot
and a control problem. **An uncrewed tail-sitting blended-wing body is
proposed as an alternative route: the airframe rotates and the propulsors do not**, so there is no
pivot, nacelle actuator or variable-pitch hub. Pitch and yaw come from differential
thrust; roll, which coaxial pairs cannot produce, comes from one moving strip. **What is
eliminated is the propulsor-reorientation mechanism, not every moving part.** **Architectural rankings belong to sizing
contracts, not to architectures**; three are reported, and the configuration holds a 32 to 36 percent mass advantage over a
lift-plus-cruise layout under all three but loses range under equal fuel fractions, driven by
the free-wheeling drag of its own attitude rotors. **No range superiority is claimed.** It is not shown to be flyable: the budget needs 3.8 times
the highest measured battery specific power.

## Keywords

vertical take-off and landing; tail-sitter; blended wing body; uncrewed aerial vehicle;
series hybrid propulsion; cruise efficiency; aircraft configuration design

## Declarations

### Supplementary Materials

> The following supplementary material is available: **S1** — independent checks on the two
> assumed aerodynamic coefficients (the full version of Section 3.10); **S2** — a component
> build-up of the mass budget (Section 3.11); **S3** — the control axes in full (Section 2.10);
> **S4** — rotational authority, trim and the transition envelope (Section 3.17); **S5** — the
> limitations in full (Section 4); **S6** — the three bills stated formally and the comparative
> sizing under three contracts (Sections 3.1 and 3.6).

### Patents

> A patent application covering the aircraft configuration described in this paper has been
> filed with the Turkish Patent and Trademark Office (application 2026/014570).

### Author Contributions

> Conceptualization, Ö.G. and M.G.; Methodology, Ö.G. and M.G.; Software, B.G.;
> Formal Analysis, M.G. and B.G.; Investigation, M.G., B.G. and Ö.G.; Data Curation,
> B.G.; Writing — Original Draft Preparation, M.G.; Writing — Review & Editing, M.G.,
> B.G. and Ö.G.; Visualization, B.G.; Supervision, Ö.G.; Project Administration, M.G.
> All authors have read and agreed to the published version of the manuscript.

### Acknowledgements

> During the preparation of this study, the authors used large-language-model assistants for
> the purposes of literature searching and triage, numerical checking of the authors' own
> calculations, and language editing. Section 2.14 states the scope of that use and the rules
> under which it was admitted. No source was cited on a model's description of it, and no
> correction was adopted until it had been reproduced independently from the underlying model.
> All design decisions, engineering judgements and claims presented in this paper are the
> authors' own. The authors have reviewed and edited the output and take full responsibility
> for the content of this publication.

### Conflicts of Interest

> The authors have filed a patent application covering the aircraft configuration
> described in this paper (Türkpatent application 2026/014570).

### Data Availability

> All data supporting the reported results are contained within the article. The
> parametric geometry model, the figure-generation scripts and the transition
> simulation, together with the aerodynamic calculations of Section 3.10 — including the
> mesh generator, the case setup, the grid-convergence study and the wall-resolution and
> turbulence-model sensitivity runs behind the computed zero-lift drag — are openly
> available at https://github.com/LORDTEK/meryemAircraft, and an archived version of this
> manuscript with its supplementary material is deposited at
> https://doi.org/10.5281/zenodo.22144194 (concept DOI, resolving to the latest version).

### Dual-Use Research of Concern

> This paper is a civil aircraft configuration study. The applications the configuration was
> conceived for are civil ones — wildfire observation and response, and cargo carriage to places
> without a runway — and no military organization, mission, weapon or payload is named or
> analysed anywhere in this work. It reports no experimental hardware and no controlled
> technical data.
>
> **The authors acknowledge the dual-use potential inherent in the subject matter.** A
> long-endurance unmanned aircraft is dual-use in principle, as most aircraft configurations
> are, and the authors note for completeness that the heavier of the two analytical scale cases
> — a 1000 kg vehicle with a computed range of 1 571 km — falls within the range band by which
> unmanned aerial vehicles are listed under international export-control arrangements. What is
> published here is an open configuration study and its equations, offered so that others may
> check or refute it; the authors neither direct it at, nor undertake to police, any particular
> downstream use, and they remain available to provide whatever further declaration the editors
> require.

### Funding

> This research received no external funding.

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
propeller slipstream, so that it is loaded at zero airspeed. Section 2.10 computes the roll
inertia and the roll damping of this planform and states the moment the strip must supply;
it does not show that the strip supplies it.

Because the same primary propulsor serves hover and cruise without changing its
orientation relative to the airframe, none of the three penalties **as defined in
Section 2** arises in full — but they do not fail to arise equally, and the differences are what
Section 3 spends its length on.

**The mass bill does not arise**: there is no second thrust system to carry. **The power bill is
halved rather than removed**, and Section 3.4 states the qualification rather than deferring it:
the buffered series hybrid releases the engine and its fuel consumption from the hover condition,
but the electric machines and the power electronics still pass the full hover power, and the
hover-sized machine is the largest single item in the propulsion chain. **The drag bill is reduced
and not removed.** There is no *lift* system left exposed in the cruise airstream — but the four
attitude pairs are exposed, they cannot be feathered, and Section 3.3 computes what they cost
rather than assuming it away. An earlier version of this paper counted that charge as absent; it
is not, and it turns out to be the largest single entry in the ledger of Section 3.5.

That is a statement about three specific charges, **one of which does not arise, one of which is
halved and one of which is reduced**, not a claim that the configuration is free. What it pays instead — the mass and drag of the control propellers and their
supporting frames, the rolling-moment device, and the transition manoeuvre itself — is
reported and quantified in Section 3.5 rather than omitted.

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
   three-dimensional Reynolds-averaged solution for the zero-lift drag with a quantified
   sensitivity budget across grids, wall resolutions, turbulence closures and starting fields;
   a component mass build-up that closes the 50 kg design conditionally and
   leaves the 1000 kg one's closure undetermined; a rotational check establishing inertial feasibility of the
   transition; a viscous, station-by-station solution of the trimmed wing that corrects the
   assumed span efficiency downward; a blade-element solution of the attitude rotors in their
   free-wheeling cruise state, which overturns this study's own earlier assumption that they cost
   nothing; and a Reynolds-averaged comparison of the spanwise loading against the vortex-lattice
   solution, which supplies the first direct evidence that the method's magnitude error is
   largely multiplicative; and
5. **states what is not established, as a testable requirement rather than an omission.** The
   aerodynamic pitching moment through the rotation is not known, and the paper reports the
   coefficient that would consume the available control margin instead of estimating the
   coefficient itself.

Items 1 and 2 stand independently of whether this aircraft is ever built, and they are the
contribution. Items 3 and 4 are what a case study is for: they show the framework applied to a
real geometry in enough detail that the bills can be audited one at a time, including the two
occasions on which the audit found against the configuration. Item 5 is the reason the paper does
not claim the aircraft can be built. **Three architectural claims are made and a fourth is
not, and each is made against a different competitor on a different axis.** Keeping them apart
is what makes them defensible, and running them together is what would make them indefensible.

**First, against runway-dependent fixed-wing aircraft: this configuration needs no prepared
surface.** It takes off and lands vertically from its own five contact points. The qualifier is
deliberate — catapult, water and short-field launch exist and are not the comparison — and
within it no assumption in this paper can take the claim away.

**Second, against the multirotor family: it cruises on a wing.** Lift in cruise is carried by a
surface rather than by rotors, which is a structural difference and not a margin. For scale —
and the two numbers are not the same kind of number — the sizing set discussed in Section 3.1
puts a turboshaft quadrotor at an *effective* lift-to-drag ratio of 4.9, a system-level figure of
merit, against this configuration's *aerodynamic* 8.8 to 10.8 across its computed drag bracket.

**Third, against the tilting architectures: it reaches the same regime transition with no
mechanism that reorients the propulsors.** Tilt-rotor, tilt-wing and tilt-nacelle layouts solve
the duty-cycle problem by rotating their propulsors, and Table 2 records what that costs them —
mechanical complexity, gyroscopic coupling during the rotation, and a transition control
problem. Those costs are the reason the tilting solution is the less widely fielded of the two
contemporary families. **This paper offers an alternative route to the same end.** The aircraft
rotates itself rather than its propulsors: there is no pivot, no nacelle actuator, no
variable-pitch hub, no retraction mechanism and no gyroscopic moment from tilting mass, and the
propellers hold one orientation relative to the airframe from take-off to cruise.

**The claim is bounded, and the boundary has to be stated in the same breath or it is false.**
It is a claim about the *propulsion* system, not about the aircraft having no moving parts.
Pitch and yaw are produced by differential thrust between fixed-pitch propellers that are
already turning; **roll cannot be, because coaxial torque-balanced pairs produce no rolling
moment at any setting, and it is produced instead by a variable-extension strip on the lower
surface — the one moving aerodynamic device on the aircraft**, derived in Section 2.10. The
actuator inventory is therefore the motors plus one strip actuator, against a tilting layout's
pivots, nacelle actuators and, usually, variable-pitch hubs and control surfaces as well.
**What is eliminated is a class of mechanism — the one that reorients a propulsor between hover
and cruise — not every mechanism.** That is countable, no sizing contract changes it, and it is
narrower than "mechanically simpler", which this paper does not measure and does not claim.

**Those three claims together are why the configuration exists, and none of them is weakened by
anything in this paper.** They are claims against three different families on three different
axes: runway independence against fixed wings, wing-borne cruise against multirotors, absence of
mechanism against tilts.

**What is *not* claimed is a range ranking against the other hybrid VTOL architectures** —
lift-plus-cruise and tilting — because Section 3.6 shows that ranking reverses with the sizing
contract, and because it is not the axis on which this configuration is offered. Section 3.6
reports that ranking in full, including a range deficit against the lift-plus-cruise layout
under one of the three contracts. That result is a property of a sizing case; it is not the
thesis, and it neither supports nor damages the three claims above.

**The line between the three claims and the disclaimed fourth is not arbitrary, and it is worth
stating as a criterion: each claim names the thing the competitor structurally lacks.** A
fixed-wing aircraft lacks vertical take-off; a multirotor lacks a cruising wing; a tilting
layout lacks freedom from a rotating mechanism. None of those is a quantity a sizing contract
can move. Range against a competitor that also cruises on a wing *is* such a quantity, which is
exactly why it is reported as a case result rather than claimed as a property of the
architecture.

**The three axes are not chosen because they are the ones this configuration wins; they are the
three that decide whether an aircraft can fly the mission class this paper is about.** Wildfire
observation and cargo delivery to sites without a runway require, in order: getting airborne
where there is no strip, staying up long enough to be useful once there, and being maintainable
and controllable by an operator who is not an airline. Those are the runway axis, the cruise
axis and the mechanism axis. A range ranking among winged VTOL layouts decides none of them by
itself, which is a second reason it is reported rather than claimed.

**Scope.** This is a configuration study containing no wind-tunnel measurement and no flight
test. Its results are analytical estimates from stated assumptions, with two exceptions computed
here: the zero-lift drag of the wing and centre body, solved three-dimensionally, and the span
efficiency of the trimmed wing, solved station by station with a viscous section method. The
mass budget began as a target rather than a finding; a component build-up replaces it for the
light design, closes conditionally, names the condition, and leaves the heavy design's closure undetermined at
all. Section 4 states these limitations, and Supplementary S5 enumerates all of them.

**The paper is arranged as follows.** Sections 2.1 to 2.6 set out the architectural tax in its
three currencies, show that architectural remedies transfer it rather than remove it, and derive
the condition under which it would not be charged. Sections 2.7 to 2.11 describe the proposed
configuration, which is built to satisfy that condition, and Sections 2.12 to 2.14 give the
sizing and computational methods and record the use of artificial-intelligence tools.
Section 3.1 tests the framework against published sizing studies; Sections 3.2 to 3.6 audit the
claim bill by bill, state what the configuration does pay, and size three architectures against
one mission under three sizing contracts. Sections 3.7 to 3.11 size two reference designs twenty
times apart in mass, bound the two assumed aerodynamic coefficients by calculation, and rebuild
the mass budget from components. Sections 3.12 to 3.17 treat the flight profile and the
transition manoeuvre, including a result that contradicts a common assumption about how quickly a
tail-sitter should rotate. Section 4 places the results in context and states the limitations,
ordered by whether they could change a conclusion. Section 5 concludes.

The configuration proposed in this paper is new, but the problem it addresses is not,
and neither are several of its ingredients. This section reviews the attempts that
preceded it. The purpose is not to establish priority but to establish two things: that
the need has been pursued continuously for seventy years, and that the pursuit was
rarely abandoned because the aerodynamics failed. Figure 2 places the programmes
discussed below on a single timeline, with the recorded reason each one stopped.

## 1.1 Removing the fuselage

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
airframe and the machinery installed in it matters for the present work, and Section 2.9
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

## 1.2 Standing the aircraft on its tail

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
exists only because someone is sitting in it. Section 1.5 returns to what that leaves.

## 1.3 Distributing sweep along the span

The proposed planform varies its leading-edge sweep continuously from root to tip while
holding the trailing edge at a constant angle. The principle of treating sweep, chord and
thickness as one coupled distribution rather than three independent choices is not new;
the crescent wing of the Handley Page Victor is its best-known expression, its sweep
decreasing outboard so that the wing was not governed by its most vulnerable station.

The present aircraft is subsonic and does not inherit the transonic motivation that
produced that planform. What it takes is the structural idea alone, and it takes it in a
much reduced form: as Section 2.8 records, the sweep variation actually realised here is
under seven degrees. No claim of descent from the crescent wing is made, and none is
needed. Section 2.8 states the values used, and Section 4 states plainly that they were
chosen rather than derived.
## 1.4 The contemporary hybrids

The problem did not go away when the prototypes did. Since roughly 2010 a large family
of hybrid VTOL uncrewed aircraft has reached service, in two dominant architectures.
Lift-plus-cruise aircraft carry a set of rotors for the vertical phase and a separate
propulsor for cruise, and fly as a fixed-wing aircraft in between. Tilting
architectures — tilt-rotor, tilt-wing and tilt-nacelle — reuse the same propulsors in
both regimes by rotating them.

Both work. Both are in operational use. This paper does not claim otherwise, and
Section 4.1 places the proposed reference designs alongside them without ranking them.
What Section 2 argues is that each of these architectures pays for its capability in a
way the other does not, that the payment can be moved between mass, drag and power
system sizing, and that it cannot be brought to zero as long as hover and cruise are
served by different hardware or by hardware that must move between two roles.

**The two families are not equally represented, and the reason matters to this paper.**
Lift-plus-cruise dominates the fielded population. The tilting architectures are the more
elegant answer on paper — one propulsion group, no dead hardware in cruise — and the less
common one in service, because rotating a propulsor in flight brings a pivot and its
actuators, a gyroscopic moment during the rotation, and a control problem through a regime
in which the aircraft is neither a rotorcraft nor an aeroplane. **The tilting idea is not
rejected by the market; its implementation is.**

**That is the gap this paper addresses.** The configuration studied here reaches the same
end as a tilting layout — one propulsion group serving both regimes — by a different route:
the propulsors are fixed to the airframe and the *airframe* rotates. Nothing pivots, nothing
retracts and nothing changes pitch. **One moving aerodynamic device remains** — a strip on the
lower surface that supplies the rolling moment coaxial propellers cannot, described in
Section 2.10 — and it is named here rather than left for a reader to find, because what is
eliminated is the propulsor-reorientation mechanism and not every moving part. Whether that trade is worth making is what the rest of the paper audits, bill by
bill, including where the audit finds against it.

## 1.5 What this history does and does not show

It would be too convenient to declare that every one of these programmes ended for
reasons external to its configuration. Some of the difficulties were real and internal,
and this paper inherits them. The tail-sitter's vertical descent is genuinely harder
than a runway landing. A tail-sitting aircraft is more exposed to crosswind on the
ground than a conventional one. And a set of propellers whose thrust vectors are all
parallel to the body axis cannot, by construction, produce a rolling moment — a
limitation that applies to this configuration exactly as it applied to its
predecessors, and which Section 2.10 addresses rather than avoids.

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

**Sea-level density is a deliberate choice and not an oversight.** An earlier version of this
paragraph called it the conservative one, on the grounds that cruising at altitude would reduce
drag with the density ratio and lengthen every range figure; **that reasoning is wrong and the
paper's own range equation shows why.** Range here is f_fuel · E* · η_chain · (L/D) / g, in
which density does not appear: at a fixed lift coefficient a thinner atmosphere is flown faster
for the same lift-to-drag ratio, and the range is unchanged. Altitude would move these figures
only by moving L/D — which it can do in either direction, depending on where the trimmed cruise
sits on the polar — so sea level is neither conservative nor generous, it is simply the one
atmosphere everything here is computed on. The choice matches the intended missions — wildfire observation and cargo delivery to
sites without a runway — which are flown low, and it keeps the hover and cruise calculations on
one atmosphere so that the ratio between them, which is what the three bills are about, is not
carrying a density change as well. A design intended to cruise high would need the whole chain
re-run; nothing in the framework prevents that, and nothing in this paper does it.

Section 3.10 computes **the drag coefficient and the span efficiency** and reports what the
computation does to them: it bounds them rather than replacing them, which is a weaker but more
honest claim.

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

---

# 3. Results

Results are given in four groups: the framework tested against published sizing
studies (Section 3.1), the three charges audited against the proposed configuration
(Sections 3.2 to 3.6), two reference designs with the bounds on their assumed coefficients and a
component build-up of their mass (Sections 3.7 to 3.11), and the flight profile with the
transition analysis (Sections 3.12 to 3.17). Every number is calculated rather than measured;
Section 4 states what that means.

## 3.1 The three bills stated formally

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
three and still be unbuildable, uncontrollable, or unsuited to its mission — and Sections 3 and
4 are about exactly that possibility for the configuration proposed here. Nor does it claim the
bills are the only costs; they are the ones that follow from the duty-cycle mismatch of Section
2.1, and a design pays many others.

Sections 2.1 to 2.6 identified three bills and argued that they are one quantity paid in three
currencies. Sections 2.7 to 2.11 described a configuration built to satisfy the zero-bill
condition. This section audits that claim bill by bill, and then states, in the same
detail, what the configuration does pay. The second half is not a concession appended
for balance. An architecture that claimed to pay nothing would be describing a
different aircraft from the one in Section 2.

## 3.2 Bill 1 — mass: the charge does not arise

There is no second propulsion group. The nose pair that lifts the aircraft off the
ground is the same pair, in the same orientation, at the same station, that propels it
in cruise. Nothing is carried unused.

This is the whole of the argument, and its brevity is the point. The bill was never a
consequence of poor design in lift-plus-cruise aircraft; it was a consequence of
counting two propulsion systems where the mission needs one. A configuration that
counts one does not reduce the bill — it does not generate it.

The tip pairs are a genuine addition and are accounted for in Section 3.5. They are not
a second propulsion group: they are sized from the moment requirement rather than from hover
weight support, though Section 3.15 shows that the thrust that sizing gives them also supplies
the aircraft's entire take-off margin. In
the vertical phase they draw 1.34 kW against the nose pair's 10.9 kW, which is twelve
percent.

## 3.3 Bill 2 — drag: reduced, and larger than assumed

In cruise there is no stopped rotor in the airstream, because there is no rotor that stops. The
nose pair is the cruise propulsor and runs at its design condition throughout. The quarter of
lift-to-drag ratio that Section 2.3 reports as the measured cost of installing hover hardware is
not incurred — not reduced, not mitigated, but **absent**, because the hardware that causes it
does not exist here. Nor is there a retraction mechanism, so the transfer of Bill 2 into Bill 1
does not occur either. Where lift rotors are retained, keeping their drag small needs an
indexing mechanism to stop them at a favourable azimuth, or a retraction mechanism to stow them;
both are mass and both are failure modes, and a configuration with no rotor to stop needs
neither.

**That carries a condition the paper had not stated, and it is a sharp one.** The four tip pairs
*are* rotors, and the claim holds only if they do not stop in cruise. Their eight discs sweep
0.251 m², **12.7 percent of the wing area** — not a small object to leave in the airstream in
the wrong state (Table 3):

**Table 3.** Cruise zero-lift drag increment of the eight tip discs in four cruise states, against the 0.0248 assumed for the clean airframe.

| Tip rotors in cruise | ΔC_D0 | of the 0.0248 assumed |
|---|---:|---:|
| turning at zero shaft load, blades at low incidence | 0.0003 – 0.0008 *(assumed)* | 1 – 3 % |
| turning at zero shaft load, **computed below** | **0.0154 – 0.0423** | **62 – 171 %** |
| stopped edge-on, at a chosen azimuth | 0.0008 | 3 % |
| **stopped broadside, azimuth uncontrolled** | **0.015 – 0.018** | **61 – 74 %** |

**The first and third rows were taken to differ by a factor of thirty, and that gap was the whole
of the argument**: whatever the coefficients, a configuration that holds its tip rotors turning
was held to be safely far from one that stops them broadside. The computed second row removes the
gap. It is derived later in this section, and it is reported here rather than buried because it
changes what this subsection concludes. The *stopped edge-on* row shows, separately, why stopping
the rotors is survivable only if azimuth is controlled — which is the indexing mechanism this
section has just claimed the configuration does not need.

**Charging the free-wheeling state also reopens a trade this paper has not priced, and that
absence should be stated before the calculation rather than after it.** The computed
free-wheeling charge below is 0.0154; the *stopped edge-on* row is 0.0008 — **a factor of twenty
cheaper in drag**. The configuration cannot be made to stop its rotors for free, because
azimuth control is exactly the indexing mechanism Section 2.10 gives as a reason not to stop
them; but "this configuration has no rotor to stop" is a design choice, not a consequence, and
a reader is entitled to ask what the mechanism would cost against the twenty-fold drag saving.
**The comparison is not made anywhere in this paper.** Sizing an indexing mechanism for eight
small discs, charging its mass and its failure modes, and re-solving the loop against a
zero-lift drag reduced by 0.0146 is a bounded calculation and it has not been done. It is the
single most likely question a reader of Section 3.3 will ask, and the honest answer is that the
free-wheeling state was adopted because it needs no hardware, not because it was shown to beat
the hardware.

**With that said, the resolution needs no hardware and can be imposed as a control state, but
its aerodynamic cost has to be computed rather than assumed away — and this section computes
it.** A fixed-pitch
propeller left free settles at the advance ratio where net shaft torque is zero: inner sections
drive, outer sections retard, and they balance. The shaft then does no work, so the motor
neither drives nor brakes and the electrical cost is controller standby draw and bearing losses.
The blades sit at low incidence, which was taken to put them in the first row —
**an inference the calculation below overturns**, since low section incidence at high rotational
speed is not the same thing as low drag. **The tip rotors
are therefore held in cruise at the zero-shaft-torque condition — neither stopped nor driven** —
and this is the state assumed throughout Section 3. It is worth naming because both neighbouring
states are wrong: driven, they cost propulsive power; stopped without azimuth control, they cost
a substantial fraction of the aircraft's zero-lift drag. What the state costs *itself*, the paragraphs below now
compute, and the answer is not the first row.

**That first row has since been computed rather than assumed, and it is the worst result in this
paper.** A blade-element calculation was set up the only way that makes the comparison mean
anything: the blade is first *designed* for the hover duty — each station twisted to a target
section lift coefficient and chorded to carry its share of 8.1 N, with section data taken at each
station's own Reynolds number — so that what is run at cruise is this aircraft's propeller rather
than a generic one. Seven designs were built, spanning target section lift coefficients from 0.40
to 0.85 and hover figures of merit from 0.65 down to 0.27. Each was then run at 30 m s⁻¹ and the
shaft speed found at which net torque is zero. Table 4 collects them.

**Table 4.** Seven tip-propeller designs run to their zero-torque free-wheeling state at 30 m s⁻¹. Shaft speed and tip Mach number were not recorded for the two designs added by the later solver-stability sweep.

| Design section c_l | Hover figure of merit | Free-wheeling speed | Tip Mach | ΔC_D0, eight discs |
|---:|---:|---:|---:|---:|
| 0.40 | 0.62 | 36 400 rpm | 1.12 | 0.0423 |
| 0.55 | 0.65 | 29 200 rpm | 0.90 | 0.0238 |
| 0.60 | 0.65 | — | — | 0.0199 |
| 0.64 | 0.64 | — | — | 0.0174 |
| **0.68** | **0.63** | **25 000 rpm** | **0.77** | **0.0154** |
| 0.70 | 0.35 | 19 800 rpm | 0.61 | 0.0126 |
| 0.85 | 0.27 | 14 500 rpm | 0.45 | 0.0085 |

**Every design exceeds the assumed 0.0003–0.0008, and the lowest exceeds it by a factor of ten.**

**Which row the aircraft is entitled to quote is decided by its own hover budget, and an earlier
version of this section quoted the wrong one.** That version took 0.0085 as the figure because it
was the smallest computed and the only one at a tip Mach number the incompressible section data
can carry. But the design producing it has a hover figure of merit of 0.27, and the hover power of
Section 3.7 — 10.9 kW at 50 kg, from which every mass and energy result in this paper descends —
is built on **0.599**. A propeller at 0.27 would not hover this aircraft on the power it is
allotted; quoting its cruise drag charges the configuration for a component it has already ruled
out. The figure of merit is flat at 0.63 to 0.65 from c_l 0.55 to 0.68 and then collapses to 0.35
by 0.70, so 0.599 falls in the collapse and no design in this family sits exactly on it. Every
design that *meets* the hover requirement lies at c_l ≤ 0.68, and **the least draggy of them gives
0.0154** — three and a half times the 0.0043 charged for the tip frames, and sixty-two percent of
the total zero-lift drag the sizing assumes. The two fastest rows are still discarded on their own
terms, the section data being incompressible where their tips are not.

**The 0.68 row runs at tip Mach 0.76, which is marginal for the same reason, so the correction
was applied rather than assumed.** The section polar was recomputed with a Prandtl–Glauert lift
correction, a Korn drag-divergence Mach number and a fourth-power wave-drag increment, and the
zero-torque shaft speed was searched again rather than held fixed. The solver used for this was
first run with the correction disabled and reproduced the uncorrected result exactly, so the two
figures differ only in the polar (Table 5):

**Table 5.** The same free-wheeling state recomputed with a compressibility correction in the blade polar.

| | Shaft speed | Tip Mach | ΔC_D0, eight discs |
|---|---:|---:|---:|
| Incompressible section data | 25 046 rpm | 0.76 | 0.01545 |
| Compressibility-corrected | 24 958 rpm | 0.76 | **0.01541** |

**The figure moves by four tenths of one percent**, and two mechanisms explain why. The lift
correction steepens the section lift-curve slope, so the blade reaches the same zero-torque state
at a *lower* shaft speed — 24 958 against 25 046 — and the profile drag falls with the square of
the local velocity, offsetting part of the wave term. More importantly, a free-wheeling blade
sits at almost zero section lift by construction, which raises the drag-divergence Mach number to
about 0.74 through the lift term in the Korn relation; at Mach 0.76 the wave increment is then of
order 10⁻⁶. **The compressibility penalty that would fall on a loaded blade does not fall on this
one.** The value is therefore reported as a figure rather than as a lower bound, and the
comparisons built on it in Sections 3.6 and 4.4 do not need re-deriving for this reason.

The mechanism does not depend on the solver. A propeller designed for hover has low pitch; left
free at 30 m s⁻¹ it must spin fast before its sections reach zero incidence, and at that speed
the blades' own profile drag is large. The trend across the seven designs is the trade stated
plainly: the blade that hovers well free-wheels fastest and drags most. Section 2.9 rules out the
escape, because these pairs are of fixed geometry and cannot feather.

**The consequence is stated rather than absorbed.** Bill 2 is not absent. On the most favourable
design computed here the tip rotors cost at least as much as the frames already charged, the
cruise lift-to-drag ratio falls, and the margin over the lift-plus-cruise layout narrows by an
amount Section 3.6 re-sizes. What would settle it is a propeller design study that
optimises the blade across both duties rather than for hover alone, or a variable-pitch tip pair
— which is a mechanism, and mechanisms are what this configuration was built to avoid.

What Bill 2 *is* paid, and this is why the heading says reduced rather than removed, is the tip
frames. They are structure in the airstream that a conventional aircraft does not carry, and at
the light design point they contribute ΔC_D0 = 0.0043 — **about twelve percent of total cruise
drag**, and seventeen percent of the zero-lift drag the sizing assumes. Both denominators appear
in this paper and each is named where it is used. That is the honest figure and it is carried in
the ledger of Section 3.5.

**The fairing on those frames is not only a drag measure.** The frames are the only surfaces
standing perpendicular to the wing plane, and the planform supplies no directional stability at
all, so the fairing is also the vertical surface that provides it. Sized against the criterion
the tailless literature recommends — C_n_β greater than 0.001 per degree [19] — the chord
required over the combined frame length is 39 mm, against the 50 to 70 mm a 20 mm faired strut
carries in any case. The two requirements do not conflict, and the directional one is the looser;
but the frame cross-section is now constrained from two directions, and a selection made on drag
alone would be made on half the evidence.

## 3.4 Bill 3 — power system sizing: avoided for the engine, not for the electrical path

The series-hybrid arrangement of Section 2.9 breaks the link that forces the power
system to be sized by the hover condition. Because the engine drives a generator rather
than a rotor, it supplies average power, not peak power, and the peak is supplied from
a buffer.

For the light reference design the numbers are as follows. Cruise draws 1.7 kW at the
electric machines, which is 1.9 kW at the engine shaft once the generator and power
electronics are accounted for, and the engine is sized at 2.6 kW. Hover requires 10.9 kW
at the rotor — 4.2 times the engine's rating. The difference is drawn for the duration of
the vertical phase from a 1.8 kg battery, which is 3.6 percent of the maximum take-off
mass. **That difference must be taken at one station, and it is the electrical bus**: the
rotor's 10.9 kW of shaft power is 12.47 kW at the bus once the machine and the power
electronics are passed, the engine delivers 2.34 kW there through the generator, and the
buffer supplies the remaining 10.13 kW. Supplementary S2 gives the chain and records that an
earlier version of this paper differenced two shaft stations instead, understating the demand
on the buffer by twenty-two percent. The heavy reference design sits on the same line:
39.2 kW electrical in cruise, 54.3 kW engine, 216.2 kW hover, 40 kg of battery at 4.0 percent
of MTOW.

An aircraft of this class whose powerplant had to be sized for hover would carry an
engine rated above 10.9 kW instead of 2.6 kW. The mass difference is not recovered
elsewhere; it is simply not incurred. That the buffer costs under four percent of MTOW
at both design points, twenty times apart in mass, is the numerical statement that this
avoidance is architectural rather than a fortunate coincidence of one size.

**What is not avoided, and the section heading says so.** The bill is defined in Section 2
as a *continuous* power system sized by the hover peak, and it is the engine and its fuel
consumption that the buffer releases from that condition. The electrical path is not
released: the nose motor and the power electronics must still pass the full 10.9 kW, and
the component build-up of Supplementary S2, summarised in Section 3.11, shows them as 2.73 kg
and 0.61 kg against 2.60 kg of
engine and generator — that is, the hover-sized electrical machine is the single largest
item in the propulsion chain. The saving is real and it is the engine's, but a reader
should not take it as an aircraft on which nothing is sized by hover. The buffer itself
carries a further condition, given in Supplementary S2: it is specified by power rather than
energy, at **5.63 kW kg⁻¹** to hover and 6.48 to leave the ground, which is a demanding cell
requirement and not a free parameter. Section 4.4 measures it against what has been flown.

## 3.5 What is paid

The honest ledger has five entries.

**The control propellers.** Four pairs, their motors, mounts and wiring exist only to
produce moments. In the vertical phase they draw twelve percent of the power the nose
pair draws. This is the configuration's substitute for elevons and a rudder, and it is
not free — it is merely cheaper than a second lift system. **An earlier version of this
ledger added that it does not sit in the cruise airstream in the way a lift rotor does.
Section 3.3 has since computed that it does.** Free-wheeling, the eight discs add more to
zero-lift drag than the frames that carry them, which makes this the largest entry in the
ledger and not the third.

**The tip frames.** As established in Section 3.3, of the order of twelve percent of
cruise drag, conditional on being faired. **An earlier version of this entry called it the
largest single payment the configuration makes; since Section 3.3 computed the free-wheeling
rotors at 0.0154 against the frames' 0.0043, it is the second largest** — the price of the
moment arm, the propeller mounting and the landing structure combined into one member.

**The roll strip.** The one moving aerodynamic device on the aircraft. Its cost when
retracted is a surface discontinuity; when deployed it is a drag device by construction,
but it is deployed only while a roll is being commanded.

**The twist needed to trim.** Section 3.17 finds that the configuration trims at cruise with
nine degrees of tip washout, reflex being an order of magnitude short of the moment required.
Washout is not free: it costs span efficiency, and the cruise lift-to-drag ratio falls from
12.65 to 12.11 — **4.3 percent**. This entry was missing from earlier versions of this ledger,
and it is worth being precise about what it is a payment for. It is not one of the three bills
of Section 2, which are charged for having a hover capability; it is charged for being
tailless, and a tailed aircraft of the same architecture would not pay it. It belongs here
because this configuration is tailless, and because a ledger that omitted it would be
flattering rather than honest.

**The transition manoeuvre.** The aircraft must rotate through ninety degrees, and the
rotation costs time, horizontal displacement and control power. Section 3 treats it in
full and shows that the altitude cost, which is the one usually assumed to dominate, can
be brought to zero: rotating slowly and entering the rotation while still climbing
removes it entirely at both design points. What remains is not free — the manoeuvre
occupies seconds during which the aircraft is neither hovering nor cruising — but it is
smaller than the literature on tail-sitters would suggest, and it is the one payment on
this list that gets *cheaper* the less it is hurried.

Set against the bills of Section 2, the ledger is favourable but not empty. The
configuration does not escape physics; it declines a particular trade. What it pays
instead is smaller, and — this is the part that matters for scaling — it does not grow
faster than the aircraft.


## 3.6 A comparative sizing of three architectures

Supplementary S6 sizes three architectures against the same mission — this tail-sitter, a
lift-plus-cruise aircraft, and a tilt-rotor — under three different sizing contracts: fixed fuel
fraction, fixed fuel mass, and fixed maximum take-off mass with fixed payload. One set of
equations serves all three, and every coefficient in it is back-solved from the light reference
design of Section 3.7 rather than assumed. Mission, wing loading, disc loading, structural
fraction and energy chain are held identical; only the cruise-drag multiplier and the
architecture-specific mass differ. Under the first contract (Table 6):

**Table 6.** Three architectures sized for the same mission under the first contract, a fixed fuel fraction, **at the published zero-lift drag assumption**. The rows for A are superseded twice below — first by charging its free-wheeling rotors, then by the bracket sweep of Table 9 — and are kept so the size of each correction can be read.

| | Empty fraction | MTOW | Cruise L/D | Hover power | Range |
|---|---:|---:|---:|---:|---:|
| A — tail-sitter | **0.580** | **50.0 kg** | 12.00 | **10.9 kW** | 1 600 km † |
| B — lift + cruise | 0.689 | 86.0 kg | 10.28 | 18.7 kW | 1 370 km |
| C — tilt | 0.624 | 60.3 kg | **13.44** | 13.1 kW | **1 792 km** |

† *Every figure in this table is at the published drag assumption. The sweep at the end of this
section gives the range as 1 173 to 1 442 km across the computed bracket, and the table is kept in
this form because the corrections below are stated relative to it.*

**That table is built on a cruise-drag multiplier this paper has since shown to be incomplete,
and re-deriving it reverses one of the three results.** Architecture A was charged 1/1.12 for its
exposed hardware, a figure covering the tip frames alone. Architecture B was charged 13/17, which
comes from a measured configuration and therefore already contains the drag of its lift rotors.
The comparison was asymmetric, and Section 3.3 has now computed the term that was missing: the
free-wheeling tip rotors add at least 0.0154 to zero-lift drag. Rebuilt from the same drag
book-keeping that reproduces the original 1.12 to three digits, A's multiplier becomes **1/1.58**,
its cruise lift-to-drag ratio falls from 12.00 to **8.49**, and its take-off mass rises to
**54.5 kg**. B cannot escape this charge by stopping its rotors and A cannot: B's lift discs are
horizontal in cruise and can be stopped with the blades aligned fore-and-aft, while A's are
fixed-pitch tractors whose blades cannot be turned out of the flow at all. **The asymmetry is
real and it runs against this configuration.** Table 7 states the effect on each contract.

**Table 7.** Architecture B against A under each of the three contracts, before and after A's free-wheeling rotor drag is charged. **A mixed basis:** the charge is applied to A and not to the clean-airframe drag coefficient the other two are sized on. Table 9 re-solves all three on a common basis and is the reportable form.

| Contract | B against A, as published | B against A, rotors charged |
|---|---:|---:|
| Fixed fuel fraction | −14.4 % | **+21.1 %** |
| Fixed fuel mass | −36.5 % | −5.4 % |
| Fixed MTOW and payload | −72.6 % | −44.9 % |

**Under the first contract the ranking reverses.** On equal fuel fractions the lift-plus-cruise
layout now flies twenty-one percent further, because A's cruise efficiency has fallen below B's:
0.632 of the clean value against B's 0.765. A retains the advantage under the other two contracts
and retains a mass advantage under all three, though **not the advantage an earlier version
quoted**. That version compared this configuration with its rotors charged, at 54.5 kg, against a
lift-plus-cruise layout at 86.0 kg sized on the *uncharged* drag — 37 percent, on two different
aerodynamic bases. Re-solving both layouts on the same drag at each end of the bracket gives 51.1
against 75.5 kg at the favourable end and 53.9 against 83.9 at the adverse one: **a mass advantage
of 32 to 36 percent, not 37 and not the 42 of the original assumption.** The two ends run the
opposite way to the intuition: the advantage is *larger* at the adverse end, because the
lift-plus-cruise layout's mass grows faster with drag than this one's does. **The conservative
single figure is therefore 32 percent, at the favourable end** — which is why the range is quoted
rather than either end alone. The claim that this
architecture leads on range under every rule does not survive either. Against the tilting layout, which was already ahead in three of
twelve cells, A now trails under all three contracts.

**A second correction pushes the other way, and it is larger.** The comparison above holds the
battery buffer at four percent of take-off mass for all three architectures. Section 4.4 sizes
that buffer on a measured pack instead, where it becomes roughly sixteen percent. Applying the
same fraction to all three — B and C included, since charging only A would invert the very
objection that motivated it — does not narrow A's margin. It widens it, because B's hover power
per unit mass is the highest of the three and the buffer feeds back on itself through hover
power (Table 8):

**Table 8.** Take-off mass of the three architectures as the energy-buffer mass fraction is raised, applied equally to all three. **On the same mixed basis as Table 7:** every row pairs A with its rotors charged against B and C at the published drag assumption — the pairing this section retires three paragraphs above. The rows are kept for the buffer trend, which is what they are used for; no mass difference should be read off them.

| Buffer fraction | A | B | C |
|---|---:|---:|---:|
| 4 % | 54.5 kg | 86.0 kg | 60.3 kg |
| 12 % | 82.1 kg | 182.5 kg | 95.9 kg |
| 16 % | 106.2 kg | 369 kg | 130.6 kg |
| 18 % | 132.1 kg | 1 157 kg | 172.1 kg |
| 20 % | 165.8 kg | **does not close** | 234.1 kg |

**The entries for B beyond twelve percent are not masses and should not be read as masses.** They
lie on a curve going vertical: B stops closing between eighteen and twenty percent, so its value
at sixteen is set by how near that limit it sits rather than by anything structural. The
reportable statement is the qualitative one — **on the highest specific power yet measured on a
flown pack, the lift-plus-cruise layout is close to not closing at all, while this one closes at
106 kg and goes on closing past twenty percent.** **That statement inherits the mixed basis of the
caption and should be read as a direction, not a margin.** What carries it is B's hover power per
unit mass, the highest of the three, and that ordering does not depend on the drag assumption;
what would move with the basis is how far apart the two curves are, which is why no number from
this table is quoted anywhere else in the paper. Section 4.4 estimates that margin at twenty
percent by holding B fixed at 86 kg while A grows; that estimate is now superseded, and it was
conservative rather than generous.

**Neither correction cancels the other, and the paper does not claim they do.** They act on
different contracts. The rotor drag costs A the range comparison under equal fuel fractions; the
measured buffer costs B its ability to close at all. A reader taking one and not the other will
reach a different conclusion from a reader taking both, which is why all four combinations are
reported in the repository rather than a single replacement table.

### The whole comparison, swept across the drag bracket

Every figure above is computed at a single assumed zero-lift drag coefficient. Supplementary S1
brackets that coefficient by calculation at **0.0285 to 0.0381**, and the assumed 0.0248 lies
below both ends rather than inside them. The sweep below therefore replaces the single-point
comparison. The drag book-keeping is the one used throughout: clean airframe from wing, body and
hubs; the tip frames and the free-wheeling rotors charged to this configuration alone; the two
competing layouts carrying their own published penalties against the same airframe. At the
published assumption the construction returns a clean-body lift-to-drag ratio of 13.40 against
the 13.44 used in the sizing, which is the check that the sweep and the original chain are the
same calculation. Table 9 gives the sweep.

**Table 9.** The whole comparison swept across the zero-lift drag bracket of Supplementary S1.

| | Published assumption | Bracket, favourable end | Bracket, adverse end |
|---|---:|---:|---:|
| Zero-lift drag coefficient | 0.0248 | 0.0285 | 0.0381 |
| Cruise lift-to-drag ratio, A | 11.88 | 10.82 | **8.80** |
| Take-off mass, A | 50.1 kg | 51.1 kg | 53.9 kg |
| **Range, A** | 1 583 km | **1 442 km** | **1 173 km** |
| Range of B relative to A, fixed fuel fraction | −13.7 % | **+45.3 %** | **+24.4 %** |
| Range of B relative to A, fixed fuel mass | −36.0 % | **+16.5 %** | −2.3 % |
| Range of B relative to A, fixed mass and payload | −72.2 % | −29.2 % | −42.6 % |
| Range of C relative to A, fixed fuel fraction | +12.8 % | +90.0 % | +62.6 % |

**Three things survive the sweep and one does not.** What survives is the result this paper leads
on: **the ranking still depends on the contract at every drag coefficient in the bracket**, and it
depends on it more strongly, not less. A holds its advantage under fixed take-off mass across the
whole bracket and loses it under equal fuel fractions across the whole bracket. What does not
survive is any reading in which the choice of contract is a detail: under fixed fuel *mass* the
sign itself changes inside the bracket, from B ahead by sixteen percent at the favourable end to A
ahead by two at the adverse one.

**The direction of the drag sensitivity is not the intuitive one and it is worth stating.** A
*cleaner* airframe makes this configuration's position *worse* relative to lift-plus-cruise, not
better. The tip frames and the free-wheeling rotors are a roughly fixed absolute charge; the
cleaner the rest of the aircraft, the larger a fraction of the total that charge becomes. At the
favourable end it is a nineteen-percent penalty on cruise efficiency and at the adverse end
sixteen. **This is Bill 2 behaving exactly as Section 2.3 says a bill behaves** — it does not
scale away, and improving the airframe does not pay it.

**What the sweep does not do.** It holds the competing layouts' penalties at their published
ratios against the swept airframe, so at the favourable end layout B is credited with a cruise
efficiency no aircraft of its kind has demonstrated. It holds the span efficiency, the buffer
fraction and the mass model fixed. And the range figures quoted elsewhere in this paper are at
the published assumption; **the honest range of the light reference design is 1 173 to 1 442 km,
not the single figure the earlier sections carry.**

**The ordering depends on which contract is used, and that dependence is the result rather than
an inconvenience.** Range in the sizing equation contains the fuel *fraction*, so holding the
fraction fixed lets the heavier aircraft carry proportionally more fuel and removes the mass
bill from the range column altogether. Fixing the fuel *mass* makes range inversely proportional
to take-off mass; fixing take-off mass and payload leaves fuel as the residual. These are three
different questions, and the answers separate (Table 10):

**Table 10.** Range of the two competing architectures relative to the tail-sitter under each of the three sizing contracts, with the rotor drag charged, **at the single published drag assumption**. Table 9 sweeps the same comparison across the computed bracket and is the reportable form; the first column here reads +21.1 % where the bracket gives +24 to +45 %.

| Range relative to the tail-sitter, **rotors charged** | Fixed fuel fraction | Fixed fuel mass | Fixed MTOW and payload |
|---|---:|---:|---:|
| B — lift + cruise | **+21.1 %** | −5.4 % | −44.9 % |
| C — tilt | **+58.3 %** | +49.2 % | +35.7 % |

*(Before the rotor term was charged these rows read −14.4 / −36.5 / −72.6 and +12.0 / +0.2 /
−19.1. The earlier figures are kept in Supplementary S6 so the size and direction of the
correction can be read off; they are not the result.)*

Against lift-plus-cruise the conclusion now depends on the rule: the tail-sitter leads under two
of the three and loses the third, where equal fuel fractions expose its lower cruise efficiency.
Against tilt it no longer leads at all: with the rotor term charged **the tilting layout** leads
under all three rules, where before **the tail-sitter** led in three of the twelve cells S6
reports and tied a fourth. Every one
of those leads still requires its nacelles, pivots,
actuators and hover-pitched blades to be credited as aerodynamically free. **No result from this
section should be quoted without the rule it was computed under**, and **no claim of *range*
superiority over the tilting family is made here in either direction.** The claim this paper does
make against that family is made in Section 1 and restated in Section 4.2, and it is not on this
axis: it is that the same regime transition is reached with no pivot, no nacelle actuator and no
variable-pitch hub — the propulsors never change orientation. Nothing in this section supports
or damages it,
because this section measures range and that claim is about parts.

**What this comparison does and does not support.** It supports the claim that the three bills
are real and separable in a sizing loop. It does **not** support a claim that this configuration
is better: the competing architectures are modelled from published mass fractions at a coarser
level of detail than the one proposed here, which is modelled from a component build-up.
**Comparing a build-up against a fraction favours whichever is modelled more optimistically**,
and this study cannot rule out that it is this one. An external check against three flying
eVTOLs, one per architecture, is reported in S6.1; it corroborates the ordering of the charges
but is a comparison of other people's aircraft, not of this sizing. Section 4 states the
comparison as conditional on both asymmetries.

A configuration argument is only as good as its willingness to become a number. This
section sizes two aircraft from the arrangement of Section 2 — one at 50 kg and one at
1000 kg, a factor of twenty apart in mass — using the same equations, the same
assumptions and the same architecture. The two points are not a light version and a
heavy version of different aircraft. They are the same aircraft at two sizes, and the
purpose of presenting both is to show that the proportions hold.

Every number below is calculated, not measured. Section 4 says what that means.

## 3.7 Light reference design — 50 kg

Table 11 gives the design.

**Table 11.** The light reference design, 50 kg, **at the published zero-lift drag assumption**. Table 12 re-solves it across the computed bracket; the cruise and range rows here are optimistic rather than central.

| Quantity | Value |
|---|---:|
| Maximum take-off mass | 50 kg |
| Root chord | 0.97 m |
| Tip chord | 0.236 m |
| Span | 3.45 m |
| Wing area | 1.98 m² |
| Aspect ratio | 6.03 |
| Wing loading | 25.3 kg m⁻² |
| Main propeller diameter | 1.20 m |
| Disc loading | 44.2 kg m⁻² |
| Tip propeller diameter | 0.20 m |
| Tip-pair disc loading | 26.3 kg m⁻² |
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

**The four cruise quantities in that table are computed at a single assumed zero-lift drag
coefficient, and Supplementary S1 brackets that coefficient by calculation.** The bracket is
0.0285 to 0.0381 and the assumed 0.0248 lies below both ends, so the table is optimistic rather
than central. Re-solving the same sizing loop across the bracket — same wing and disc loading,
same fuel fraction, same mass model, only the drag changed (Table 12):

**Table 12.** The light reference design re-solved across the zero-lift drag bracket.

| | Assumption | Favourable end | Adverse end |
|---|---:|---:|---:|
| Zero-lift drag coefficient | 0.0248 | 0.0285 | 0.0381 |
| Cruise L/D | 11.88 | 10.82 | **8.80** |
| Cruise power, electrical | 1.72 kW | 1.93 kW | **2.50 kW** |
| Take-off mass | 50.1 kg | 51.1 kg | 53.9 kg |
| Endurance | 14.7 h | 13.4 h | **10.9 h** |
| **Range** | **1 583 km** | **1 442 km** | **1 173 km** |

At the published assumption the loop returns 50.1 kg and 1 583 km against the 50 kg and 1 598 km
in the table above, which is the check that the sweep and the original sizing are the same
calculation rather than two.

**The honest figure for this design is a range of 1 173 to 1 442 km, not 1 598.** Nothing else in
the table moves: the geometry, the loadings, the hover power and the transition time are all set
by mass and disc area, none of which the drag coefficient touches. What moves is every quantity
that passes through cruise efficiency, and those are the four in bold.

The mass budget behind this — 30 % structure, 16 % propulsion chain, 4 % battery, 8 %
avionics and control, 16 % fuel, leaving 26 %, or 13 kg, for payload — is the allowance the
design is sized against, and it is asserted here rather than derived. Section 3.11 rebuilds
it from components and finds it can be met, with 2.2 kg in hand, on one condition that is
not demonstrated: a structural areal density no greater than 1.78 kg m⁻². Paper aircraft
are habitually lighter than the ones that get built, and no allowance for that has been
paid in this table beyond the contingency inside the build-up. Section 4.4 keeps the areal
density as the most likely place for the *structural* numbers to be wrong, and identifies the
battery buffer's specific power — not the structure — as the most exposed number in the paper.

## 3.8 Heavy reference design — 1000 kg

Table 13 gives the design.

**Table 13.** The heavy reference design, 1000 kg.

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

**Before any of these numbers is read, one condition belongs beside them rather than in the
supplement.** The light design of Section 3.7 closes its component build-up with 2.2 kg in hand,
conditional on a structural areal density no greater than 1.78 kg m⁻² — an assumed value with a
margin and a published anchor. **The heavy design has no such margin and no assumed value.** Its
shell mass scales with wetted area while take-off mass scales with volume, so the shell fraction
depends on how areal density grows with size, and that exponent has not been measured. At an
exponent of 0.467 the 260 kg payload is exactly break-even, closing below and failing above, and
Supplementary S2 declines to argue for either side because any such argument would be a structural
model standing in for a measurement. **The aerodynamic, propulsive, energy and mission numbers in
this section close; the structure is not shown to.** The two designs therefore differ in kind and
not only in degree: the light one closes conditionally, the heavy one's closure is undetermined.

**This table charges the tip frames and not the free-wheeling rotors, which is the defect
Section 3.3 found in the light line, and the heavy line carries it too.** Running the same
blade-element calculation at this design's own conditions — 0.67 m discs, 40 m s⁻¹, the tip-pair
power this configuration allocates, and the hover thrust that follows from it — gives a much
smaller charge than the light design pays (Table 14):

**Table 14.** The heavy reference design before and after its own free-wheeling rotor drag is charged.

| | Published | Rotors charged |
|---|---:|---:|
| Free-wheeling ΔC_D0, eight discs | assumed negligible | **0.0051** |
| Zero-lift drag coefficient | 0.0200 | 0.0251 |
| Cruise L/D | 13.60 | **11.78** |
| Take-off mass | 1 037 kg | 1 077 kg |
| **Range** | **1 814 km** | **1 571 km** |

The published row is what the sizing loop returns with no rotor charge, and it reproduces the
13.6 and 1 814 km of the table above, which is the check that this is the same calculation. The
carried value is **a third of the light design's 0.0154** — the interval around it spans a
quarter to a half — and Section 3.9 works out why.

**The heavy family's blades meet the hover requirement, and that is exactly why the charge above
is a range rather than a single number.** Across every design tried the figure of merit is 0.65 to
0.66, against the 0.599 the power budget assumes, so the twelve percent of hover power allocated to
the tip pairs buys the thrust it is credited with. **But this is where the heavy line differs from
the light one in a way that has to be stated, because it weakens the number rather than
strengthening it.** In the light line the design is pinned: the figure of merit collapses from
0.633 to 0.350 above a target section lift coefficient of 0.68, so the least-draggy blade that
still hovers is the one the cliff leaves standing, and the 0.0154 of Section 3.3 is selected by
physics. In the heavy line there is no cliff — the figure of merit is still 0.657 at a target of
0.85 — so the same rule selects whichever design sits at the end of whatever range is swept.
Across designs meeting the hover requirement the charge runs from **0.0074 down to 0.0035**, and
applying the light line's rule literally would return the lowest of these, which is the end
favourable to this configuration. **The 0.0051 carried above is the interior value the sizing was
run at, not a minimum, and it is reported as such:** the honest statement is that the heavy
charge is bounded by 0.0035 and 0.0074 and is not pinned within that interval by any criterion
this study applies. It remains between **a quarter and a half** of the light design's charge at every point in the
interval — 0.0035/0.0154 is 0.23 and 0.0074/0.0154 is 0.48 — so the qualitative statement that
the heavy line pays a fraction of the light line's charge holds wherever in the interval the
value falls. **One thing in Section 3.9 does not hold that way, and it is named there rather
than buried here:** the numerical agreement between the predicted and computed scaling ratios is
computed at 0.0051 and moves with the choice. The chord limits in the
blade-element routine are expressed relative to rotor radius; an earlier draft of this study used
absolute limits taken from the light design's 0.20 m rotor, which on a 0.67 m rotor produce a
12 mm chord on a 335 mm radius and a correspondingly slender blade. The repository records that
correction and its effect.

The heavy design still has a longer range than the light one despite a shorter endurance, and the
margin survives charging both lines: 1 571 km against 1 173 to 1 442 km. **That comparison is
asymmetric and the asymmetry is worth naming rather than leaving to be noticed: the light range
is a bracket and the heavy range is a single number, because no drag bracket has been computed
for the heavy line.** Supplementary S1 brackets the light airframe's zero-lift drag; the heavy
line stands on its own 0.0200 with no equivalent bound. The margin survives because 1 571
exceeds the adverse end of the light bracket, which is the weakest form of the statement and the
only one the evidence supports. Both effects come from the
same source: the larger aircraft cruises faster and, at a higher Reynolds number, achieves a lower
zero-lift drag coefficient and therefore a better lift-to-drag ratio. Nothing in the architecture
was changed to obtain this.

## 3.9 Scale behaviour

One qualification applies throughout: this is the scaling of the analytical sizing model — of
powers, loadings and mass *fractions*. Whether the heavy design's structure closes depends on
how shell areal density grows with size, which was not measured. Figure 10 shows the two
designs at a common scale. Four properties are preserved and one is not.

**Disc loading is held constant** — 44.2 and 43.7 kg m⁻². This is the rule that governs the
sizing rather than a coincidence of it. Hover power per unit weight is √(DL/2ρ), so fixing disc
loading fixes specific hover power: hover power rises from 10.9 kW to 216.2 kW, a factor of 19.8
against a mass factor of 20. **Hover power grows linearly with mass rather than as the L^3.5 of
the classical result**, and that is the whole benefit of fixing it. The cost is that disc area
must then grow as L³ rather than L², which for a fixed number of propellers is impossible. The
architecture has two ways out and uses both: a coaxial pair may be added at no architectural
cost, since every pair is torque-balanced on its own; and geometric similarity is not held.

**The three bills do not scale together, and Bill 2 scales in the configuration's favour.** The
free-wheeling charge computed in Sections 3.3 and 3.8 falls from 0.0154 at 50 kg to 0.0051 at
1000 kg while the mass bill rises and the power bill is held flat by construction.

**The mechanism is not the obvious one, and an earlier version of this paragraph gave the obvious
one and was wrong.** That version said the tip discs are referenced to a wing area that grows
faster than they do. They are not: the eight discs total 0.251 m² against 1.98 m² of wing at
50 kg and 2.82 m² against 22.24 m² at 1000 kg, which is 0.127 in both cases. **The disc-to-wing
area ratio is constant to three digits, and contributes nothing.** What the charge actually
follows is

    ΔC_D0  ∝  σ R² / (q S),

in which the geometric ratio *R²/S* is the constant just quoted, so only two terms move: the blade
solidity falls from 0.075 to 0.044 as the larger rotor meets its thrust with proportionally less
blade, and the cruise dynamic pressure rises by a factor 1.78 between 30 and 40 m s⁻¹. Their
product, 1.73 × 1.78 = 3.08, is the predicted ratio; the computed ratio is 3.04. **The bill falls
because the reference dynamic pressure rises and the blade thins, not because the wing outgrows
the disc.**

**How close that agreement is depends on a number Section 3.8 has just declared unpinned, and
saying so costs the agreement some of its force.** The computed 3.04 is 0.0154/0.0051, and 0.0051
is the interior value the heavy sizing was run at rather than a value any criterion selects; at
the ends of the interval Section 3.8 bounds — 0.0035 and 0.0074 — the ratio computes to 2.08 and
4.40, either side of the predicted 3.08. **The mechanism — that solidity and dynamic pressure are the only two terms that
move — does not depend on the choice, and neither does the direction or the order of magnitude.
The three-digit agreement does.** It is reported as a consistency check at the sizing point, not
as a validation of the scaling law.

**The two halves of this comparison do not have the same standing, and putting them under one
heading would suggest they do.** Bill 2's scaling is computed: it comes from two blade-element
solutions on two sized rotors, it uses solidity and cruise dynamic pressure, and **it does not
touch the shell-mass exponent at all.** It would remain a result even if the heavy airframe were
shown not to close. Bill 1's scaling is the opposite case: it *is* the unmeasured exponent of
Supplementary S2, and it is a projection of the sizing model rather than a computed outcome. The
first is reported here as a result; the second as a property of the model, conditional on an
exponent nobody has measured.

**What the pair does and does not establish.** The currencies were computed independently at two
design points and moved in opposite directions; nothing in the definitions of Section 2 required
them to. That is evidence *consistent with* the separability the framework asserts, demonstrated
on one case — not a verification of separability as a general property, which a single
instantiation cannot supply. What it does establish for this configuration, and what does not
depend on the structural question at all, is a consequence worth stating on its own: **the light
design is the harder case for Bill 2 and the heavy design the easier**, which is the opposite of
the usual expectation for a tail-sitter.

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
221.5 kW from the tip propellers — 102 % of hover power, which is to say it is not available (Table 15):

**Table 15.** Tip-propeller power required to rotate the heavy reference design.

| Rotation time | Tip-propeller power, 4 total | Fraction of hover power |
|---:|---:|---:|
| 2 s | 221.5 kW | 102 % |
| 3 s | 65.6 kW | 30 % |
| 4 s | 27.7 kW | 13 % |
| **5.1 s** | **13.4 kW** | **6 %** |

**The rule is that a larger aircraft turns more slowly.** The heavy design rotates in 5.1 s at
six percent of hover power — not a round number but the rotation time at which it holds the same
control margin the light design holds at two seconds (Section 3.17). The constraint is less costly
than it looks, because Section 3.15 shows a slower rotation loses *less* altitude: the scaling
penalty on transition time works with the penalty on control power rather than against it. The
classical objection to scaling a VTOL aircraft — hover power growing as L^3.5 against power
available as L³ — is removed on the hover side by fixing disc loading. It is not removed on the
transition side, and Table 15 is where it reappears: **the rotation is the one place in this
aircraft where the square–cube relation is still paid in full.**

## 3.10 Independent checks on the two assumed coefficients

Both coefficients carried through Sections 3.7 and 3.8 were assumed. Both have since been
computed, and the computations are reported in full in Supplementary S1. Neither replaces its
assumption in the figures above — those are quoted on one stated basis throughout — but each
bounds it, and the direction of each is stated here.

**Zero-lift drag.** A Reynolds-averaged solution of the wing and body gives C_D0 between
0.0120 and 0.0148, against the 0.0248 assumed. The spread is the turbulence closure:
0.01475 with Spalart–Allmaras and 0.01201 to 0.01253 with k-ω SST, eighteen percent apart
at matched wall resolution. **The assumption lies above the whole of that range**, so
against the airframe alone it is conservative rather than optimistic. **It is not conservative
against the aircraft.** That solution resolves the wing and the body and no rotors, and the
free-wheeling discs computed in Section 3.3 add at least 0.0154 to whatever it returns. Carried
into the build-up of Supplementary S1 the bracket becomes 0.0285 to 0.0381 and the assumed 0.0248
lies below both ends rather than above them — optimistic by as much as fifty-three percent at the upper
end. **The cruise lift-to-drag ratio, the ranges of Section 3.7 and the comparative sizing of
Section 3.6 are all computed on 0.0248 and none of them is re-derived here** — the heavy line of
Section 3.8 stands on its own coefficient, 0.0200, which this bracket does not address. Two things S1 does not settle: the solutions are fully
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
coefficient to six decimal places. Table 16 gives the two efficiencies.

**Table 16.** Inviscid and Oswald span efficiency of the planform, and the ratio between them.

| | Inviscid e | **Oswald e** | Ratio |
|---|---:|---:|---:|
| Untwisted planform | 0.990 | 0.931 | 0.940 |
| **Trimmed, −9° washout** | **0.859** | **0.817** | **0.951** |

**The borrowed rule was wrong in the favourable direction and the conclusion is unchanged in
the unfavourable one.** The viscous penalty is 5 to 6 percent rather than 10 to 15, but the
trimmed wing starts from 0.859, so the Oswald efficiency lands at **0.817 — below the assumed
0.85 by 3.9 percent**. At that value the cruise lift-to-drag ratio is **11.87 against 12.04**,
and the range figures of Section 3.8 are optimistic by the same 1.4 percent. Two limits belong
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
configuration, and every use made of them is of a kind a magnitude error *would not* disturb —
provided the moment scales with the lift by the same factor, which is exactly what cannot be
checked.**
**The magnitude question cannot be settled here, but its complement can be, and doing so moves
the exposure rather than removing it.** Whether the moment scales with the lift is untestable
without the withheld data. What is testable is the opposite question: *if the true loading
differs from the vortex-lattice loading by a redistribution across the span, how far do the
quantities taken from the solution move?* The twist distribution is perturbed by a half-sine in
the span fraction, which vanishes at root and tip, so root and tip incidence — and therefore tip
loading — are untouched and only the distribution between them shifts. The neutral point and the
trim twist are then re-solved at each shape. The perturbation is a redistribution and not a
rescaling, which is what makes it the complement of the error the source reports: across ±2° the
inviscid span efficiency moves by at most 1.6 percent from its 0.859. Table 17 gives the sweep.

**Table 17.** Neutral point and trim twist under a spanwise redistribution of the loading shape.

| Shape perturbation | Neutral point | Δ from baseline | Trim twist | Δ from baseline |
|---|---:|---:|---:|---:|
| −2° (loading inboard) | 0.8646 m | −0.34 %MAC | −8.42° | +0.77° |
| −1° | 0.8658 m | −0.16 %MAC | −8.81° | +0.38° |
| **0, baseline** | **0.8668 m** | — | **−9.19°** | — |
| +1° | 0.8677 m | +0.14 %MAC | −9.57° | −0.37° |
| +2° (loading outboard) | 0.8685 m | +0.26 %MAC | −9.93° | −0.74° |

The baseline reproduces the chain it is testing: the trim twist of **−9.19°** at **10.24°** of
incidence is the nine degrees of washout reported above, and an independent solver in the
repository — bisecting incidence rather than solving the linearised system — returns the same
incidence to 0.01° with a residual pitching moment of 3 × 10⁻⁵.

**Two things follow, and the second was not expected.** Per degree of mid-span redistribution the
neutral point moves **0.15 %MAC** and the trim twist moves **0.38°**. The first of those two
numbers has to be read against the method's own scatter: the neutral point is not determined to
better than about 1.3 %MAC across equally defensible solver choices, which is the equivalent of
nine degrees of redistribution. **The neutral-point column of the table above therefore sits
inside the noise floor of the method that produced it**, and its entries should be read as
showing an absence of movement rather than measuring one. The trim twist carries no such
problem: it is solved to a residual of 10⁻⁶ at every shape, and its movement is an order of
magnitude larger than anything the solver choices introduce. Against the thresholds that
would force the trim chain to be recomputed — 5 %MAC and one degree — the neutral point would need
a redistribution of **33 degrees** and the trim twist one of **2.6 degrees**. **The binding
constraint is the trim twist and not the neutral point, by a factor of thirteen.** The static
margin, which is the quantity the cancellation argument above was constructed to defend, is the
robust half of the chain; the trim twist, which that argument never addressed, is what a
redistribution disturbs first.

This does not measure the redistribution a RANS solution would find. It converts an exposure that
had no bound into a transfer coefficient: a reader holding an estimate of the redistribution can
multiply.

**A Reynolds-averaged solution of this planform now supplies that estimate, and the answer falls
across the threshold rather than cleanly on one side of it.** The untwisted planform was solved
at the incidence where the vortex-lattice method returns the cruise lift coefficient, 6.69°, on a
192 000-cell wall-function mesh, and the spanwise loading was extracted from the wall pressures.
The face sum reproduces the case's own integrated lift coefficient exactly, which is the check
that the extraction is not itself the result. Table 18 gives the result.

**Table 18.** Reynolds-averaged solution of the untwisted planform at the vortex-lattice cruise incidence, on the **initial 192 000-cell mesh**. Table 19 refines it twice; the converged ratio is 0.796, not the 0.787 below.

| | Value |
|---|---|
| RANS lift coefficient | 0.354 |
| Vortex-lattice lift coefficient | 0.450 |
| Ratio *K_L* | **0.787** |
| Local ratio *K(y)*, η = 0.05 to 0.91 | 0.740 – 0.816 |
| *K(y)/K_L* over the same range | **0.940 – 1.037** |

**Two things follow and they point in different directions.** The first is that the error is
very nearly multiplicative: once the overall ratio is divided out, the local ratio holds to within
five percent of unity across nine tenths of the span. That is the condition the cancellation
argument of this section requires, and it is the first direct evidence for it rather than an
assumption about it. The second is that **the overall ratio runs the other way from the published
comparison this paper cites**: that source reports the vortex-lattice lift coefficient low by
thirty to thirty-eight percent against RANS, whereas here it is high by twenty-seven percent. The
two are different geometries solved at different fidelities and neither refutes the other, but
the direction assumed in the earlier argument is not the direction found here.

**The solution was refined twice and the refinement changed the answer**, so what follows is the
converged reading rather than the first one. Three meshes were run at identical settings (Table 19):

**Table 19.** Grid refinement of the Reynolds-averaged solution: three meshes at identical settings.

| Mesh | Cells | *K_L* | Inner-region residual | Tip-region residual |
|---|---:|---:|---:|---:|
| Coarse | 192 000 | 0.787 | 0.029 | 0.133 |
| Medium | 444 000 | 0.793 | 0.046 | 0.130 |
| Fine | 682 000 | **0.796** | **0.048** | **0.122** |

The overall ratio converges — 0.787, 0.793, 0.796, the last step being four tenths of a percent.
The **inner-region residual does not shrink with refinement; it grows and then settles**, which
means the coarse mesh was smoothing the loading and making the agreement look better than it is.
The tip-region residual barely moves across a threefold change in cell count, which is the
signature of a real disagreement rather than a discretisation error.

**Converted into the units of the sensitivity above, the converged residual is 2.75 degrees of
equivalent redistribution over the inner nine tenths of the span.**
The conversion is measured rather than asserted — the same half-sine perturbation was applied to
the vortex-lattice solution and its effect on the normalised loading ratio recorded — and both
sides are measured as standard deviations rather than as extremes, because the two solutions carry
different numbers of spanwise stations and an extreme-value measure would reward whichever had
more. That choice is not cosmetic: on the same converged solution the extreme-value measure gives
2.80 degrees and a coarser common sampling gives 1.87, and the two sit on opposite sides of the
one-degree trim-twist mark, so the measurement rather than the physics would have decided what the
paper reported.

**What that number is, and what it is not.** The 2.6 degrees is not an acceptance criterion the
solution has failed; it is a unit conversion — the redistribution that corresponds to one degree
of trim twist through the measured sensitivity of 0.38 degrees per degree. Read as a criterion it
invites the reply that the paper exceeded its own gate and then argued the gate did not matter.
Read as what it is, the calculation is a calibration: **a measured redistribution of 2.75 degrees
converts to 1.04 degrees of trim twist, a 2.1 percent change in span efficiency from 0.817 to
0.799, and 0.8 percent on the cruise lift-to-drag ratio and on every range computed from it.** That is an order of
magnitude inside the drag bracket the same section already applies, which moves range by nine to
twenty-six percent. **The vortex-lattice trim chain is therefore not overturned by this
comparison; it is displaced by less than the uncertainty already carried around it**, and the
paper reports the exceedance rather than rounding it away.

What the comparison does establish against the configuration is the tip. The disagreement outboard
of η = 0.90 survives refinement undiminished, and the vortex-lattice method is where it would be
expected to fail — at the tip vortex, on a section of finite thickness modelled as a sheet.

**No quantity here is taken from the outboard tenth alone, but three are integrals over the span
that include it, and saying "nothing depends on the tip" would be too quick.** The span
efficiency, the roll damping and the neutral point all integrate the loading, so the tip enters
them weighted by its share of the load. That share is about a tenth, and the local disagreement
there is about a quarter, so the integrated quantities carry roughly 2.5 percent from this source
— inside the drag bracket applied to the same numbers and of the same order as the trim
displacement above. A strip-based estimate drawn from the tip region by itself would not be
safe; none is made.

**Three limits belong with all of this.** No viscous drag is taken from these runs, which use wall
functions. The twisted geometry is not solved at all, because the mesh generator accepts stations
as span, leading edge, chord and thickness and has no field for twist. And the overall ratio runs
opposite to the published comparison cited above, which the paper reports rather than reconciles.

## 3.11 A component build-up of the mass budget

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
what all of those must fit into. Section 4.4 states the item as bounded from below rather than
demonstrated.

The transition between vertical and horizontal flight is the manoeuvre on which
tail-sitters have historically been judged, and it is the part of this configuration
that most deserves scrutiny. This section describes the flight profile, states the
equations that govern the transition, and reports a simulation of it. One result
contradicts a widely-assumed relationship and is presented as such.

## 3.12 The five phases

**Why the next six subsections are here.** Everything so far has audited the three bills and the
sizing that follows from them, which is what the framework of Section 2 asks of a case. None of it
establishes that the configuration can perform the manoeuvre that makes it a tail-sitter rather
than a fixed-wing aircraft that cannot take off. **The bills are only owed by an aircraft that
rotates**, and whether this one can is a separate question from what its architecture costs. The
subsections below ask it, and the answer decides whether the case study is of an aircraft or of a
configuration that has never left the ground. It is also where this paper's largest unresolved
item lives.

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
contact points. Section 3.16 notes what is and is not analysed here.

Figure 11 shows the five phases in sequence. Nothing on the aircraft rotates relative to
the aircraft at any point in it.

## 3.13 Why the transition begins in the easiest condition

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

## 3.14 The thrust singularity that is never reached

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

## 3.15 Transition time: slower is better

The transition was simulated as a two-degree-of-freedom point mass. The body angle is driven
from zero to ninety degrees over a rotation time t_r; thrust acts along the body axis, lift
perpendicular to the velocity vector and drag opposite to it; the lift curve is linear to stall
and a flat-plate relation beyond it. Altitude loss is the lowest point of the trajectory
relative to the entry altitude. Figure 12a plots both reference designs against rotation
time, each at the two thrust-to-weight ratios its own installed power supplies.

**The ratio the aircraft actually has must be established first, and it is not a free choice.**
Section 2.12 sizes hover power at thrust equal to weight, so the 10.9 kW of Section 3.7 buys
T/W = 1.00 and nothing more; the same is true of the 216.2 kW of Section 3.8. The only other
source of vertical thrust on this aircraft is the tip pairs, and during the rotation they are
occupied producing the rotation itself. On the bang-bang profile the upper pairs run at full
thrust and the lower pairs at zero, which is the M = 2TL of Section 2.9 — and the two upper
pairs still push upward. That fixes the ratio available *during* a full-authority rotation at
**1.066 for the light design and 1.041 for the heavy one**, and it is the ratio the tables below
use. Giving up rotation authority buys a little more, to 1.132 and 1.082 with none retained;
Supplementary S2 gives the trade. An earlier version of this section assumed T/W = 1.2, which
the installed power does not supply at any setting, and the tables have been recomputed. Table 20 gives the recomputed losses.

**Table 20.** Transition altitude loss against rotation time, at the thrust-to-weight ratio each design's installed power supplies with full rotation authority retained.

| t_r, light | Altitude loss, 50 kg | t_r, heavy | Altitude loss, 1000 kg |
|---:|---:|---:|---:|
| 1 s | −18.2 m | 2 s | −31.0 m |
| 2 s | −14.7 m | 3 s | −26.9 m |
| 3 s | −11.2 m | 4 s | −22.7 m |
| 4 s | −4.9 m | 5.1 s | −13.1 m |

**The relationship is monotonic in the direction opposite to the one usually assumed.** It is
frequently supposed that a tail-sitter should rotate as fast as possible, on the reasoning that
it is unsupported during the rotation and therefore falls for a time t_r, giving a loss
proportional to t_r². **That reasoning is wrong, and the error is in its premise:** the aircraft
is not unsupported. Vertical support is T cos θ + L, and a slow rotation keeps cos θ large during
exactly the interval in which speed, and therefore lift, is being built. A fast rotation
collapses cos θ before there is any lift to replace it, and the aircraft falls precisely because
it hurried.

The practical consequence is a simplification rather than a trade. The control *moment* required
to rotate in time t_r scales as 1/t_r² and the control *power* as 1/t_r³ — Table 15 of Section 3.9
is the second of these, and its entries are constant to within a third of a percent when
multiplied by t_r³ — so a slow rotation is cheap in authority and cheaper still in power; and
altitude loss also falls with t_r. **All of these point the same way**, so there is no optimum
transition time to be found between competing penalties — the rotation time is set by what the
actuator can do, not by a balance, and Section 3.17 shows that is where both reference times come
from.

**Entering the rotation while still climbing removes the penalty entirely in this model**, and
that survives the correction to thrust-to-weight above. At an entry climb of 5 m s⁻¹ the altitude
loss is zero at both reference rotation times — 2 s light and 5.1 s heavy — and remains zero at
every ratio from 1.066 down to 1.00, which is to say the result does not depend on the tip pairs
contributing any lift at all once the climb has been acquired.

**It does not survive the addition of rotational dynamics, and that is the sharpest limitation of
this result.** The simulation above drives the body angle kinematically: the aircraft is assumed
to rotate, and the moment producing the rotation does not appear. Section 3.17 asks separately
whether the moment is available. The two have now been solved together — three degrees of freedom,
a finite control moment, and the same trajectory model otherwise — and with **zero aerodynamic
pitching moment**, which isolates the rotational dynamics alone, the light design loses **5.4 m**
at its reference condition where the kinematic model reports zero. The loss is not a tracking
artefact: it is unchanged across the linear, bang-bang and smooth reference profiles, it appears
without the control moment ever saturating, and it grows rather than vanishes as the controller
gains are raised, reaching 17 m at gains high enough to track the reference almost exactly. What
the kinematic model omits is not the difficulty of turning the aircraft but the trajectory the
aircraft flies while it is being turned.

With a borrowed pitching moment the outcome depends on which moment is borrowed, and the spread is
wide enough that no number from it is reportable: some models complete the rotation, others
saturate the tip pairs, and others tumble. That spread is itself the finding, and it is the same
finding Section 4 states from the other direction — the transition rests on a coefficient no
current method predicts reliably. Supplementary S4 gives the sweep. **Two cautions belong with it:
the model carries no aerodynamic pitch damping, and its controller is a fixed-gain regulator
rather than a designed one, so the borrowed-moment rows bound nothing.** The zero-moment row does
not depend on either and is the result carried forward.

**Acquiring the climb is where the correction is paid.** The aircraft reaches transition altitude
by climbing, so it need not stop and hover first, but the excess thrust available to build that
climb is now 0.132 g rather than the 0.2 g an earlier version claimed, and only if no rotation
authority is held in reserve; with full authority retained it is 0.066 g. Five metres per second
is therefore reached in 3.9 s over 9.6 m at best, and 7.7 s over 19.3 m at worst, against the
2.6 s and 6.4 m previously stated. The energy involved is unchanged and remains negligible —
625 J against a fuel energy of 103 kWh — so what the correction costs is time and height, not
range. **The reference profile is therefore still to enter the rotation at 5 m s⁻¹ of climb**,
with the acquisition charged at the achievable rate.

Two consequences follow that the earlier tables hid. Starting the rotation from rest is worse
than reported — the light design loses 14.7 m at its own two seconds rather than 9.1 m, and the
heavy design 13.1 m at 5.1 s rather than none — so the climb entry is not a convenience but a
requirement. And the tip pairs, introduced in Section 2.9 as moment producers and charged in
Section 3.5 for their mass and drag, turn out to carry the take-off thrust margin as well: an
aircraft whose primary propulsor is sized at thrust equal to weight leaves the ground on them.
That is a second duty for hardware bought for the first, which is the kind of economy this
configuration is built on — but it is also a dependency, and it is a harder one than it looks,
because the margin and the attitude authority are drawn from the same four propellers and cannot
both be had in full. Section 4 records it as an open item.

**The test is a lower bound.** A point mass carries no rotational dynamics, no aerodynamic
pitching moment and no control-power limit; Section 3.17 supplies the rotational budget that this
model omits, and Section 4 states what neither supplies.

## 3.16 Landing

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
question. It is listed in Section 4 rather than answered here.

**The third belongs with them and has not been said at all until now: the deceleration
and nose-up rotation are not analysed either.** Sections 3.12 to 3.15 treat the forward
transition in six subsections and the reverse in this clause. The two are not symmetric
and should not be assumed to be: the forward rotation builds dynamic pressure while it
turns, so lift arrives to replace the vertical component of thrust as that component
falls, and Section 3.15 shows the result turns on exactly that race. The reverse runs the
race backwards — dynamic pressure falls while the aircraft is being turned, so lift is
leaving at the moment the thrust vector has not yet returned to vertical — and a model
built for the first case cannot be read for the second by changing a sign. **No figure in
this paper describes the landing transition, and none should be inferred from the
take-off one.** Section 4 records it.

## 3.17 Whether there is enough authority to rotate, and whether it trims

Rotating the airframe through ninety degrees is the manoeuvre this configuration must perform
with four small propellers and no pitch control surface — the one aerodynamic device the aircraft carries, the roll strip of Section 2.10, produces no pitching moment and takes no part in this manoeuvre. Supplementary S4 carries the full budget —
inertia derivation, rotation profiles, centre-of-gravity window, twist sweep and the measured
section evidence. This section states what it returns.

**The rotation closes at the actuator limit rather than clear of it.** The pitch inertia
derived from the component build-up is 9.81 kg·m² for the light design and 2 503 kg·m² for the
heavy one. On the cheapest rotation profile the tip propellers carry the manoeuvre with a margin
of **1.49** at the light design point and **1.57** at the heavy one; on a smoothly commanded
profile the margins fall to 0.99 and 1.05. The reference rotation times — two seconds light,
5.1 seconds heavy — are therefore lower bounds set by the actuator, not comfortable choices,
and the margin narrows with size.

**The light figure rests on a tip thrust the design tables assert rather than derive, and on the
conservative basis it is thinner still.** The 16.2 N quoted per pair implies a figure of merit of
0.702, against the 0.599 used for hover everywhere else. Recomputing at 0.599 with a fifteen
percent coaxial interference loss gives 12.4 N, an available moment of 17.6 N·m, and margins of
**1.14 bang-bang and 0.76 smooth** — which is to say the light design closes on the cheapest
profile and does not close on a smooth one at two seconds. The heavy design was computed on the
conservative basis from the outset. Supplementary S4 gives both, and the honest reading is that
the rotation is sized by the actuator under either basis and has no margin to give under the
stricter one.

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
**static margin of +12.5 percent of mean aerodynamic chord**, on the untwisted planform. On the
wing twisted to trim, which is the geometry the aircraft flies, the same solver places it at
0.867 m and the margin at +13.6 percent. **Neither figure is determined to better than about a
percent of mean chord**: across eight combinations of geometry, moment reference and incidence
range that are all equally defensible, the neutral point spans 0.858 to 0.867 m and the margin
12.3 to 13.6 percent. In exact linear theory none of those choices should move it; they move it
because the solution is not exactly linear in incidence. The scatter is stated rather than
averaged away, it is small against the packaging window, and it is the reason the static margin
is quoted to one decimal and not two, with a pitching moment of 0.056 to
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
to be tailless**, and entered in the ledger of Section 3.5 as its fifth item. The reflex route
is not free either: a blended-wing UAV trimming by reflex rather than twist records that
carrying reflex over a wide span "is not conducive to the improvement of overall lift-to-drag
performance" [44]. **Both roads to trim on a tailless configuration cost cruise efficiency**,
which is the reading Section 3.5 places on the 4.3 percent: it is the price of having no tail,
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
than to computation, and Section 4 asks for it as measurement. The same tests found the
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

# 4. Discussion

This section places the results against existing aircraft and existing
literature, then states what is not shown. Sections 4.1 and 4.2 are interpretation;
Sections 4.3 to 4.7 are limitations, ordered by whether they could change a conclusion.

## 4.1 Context

The following aircraft occupy the same mass range. They are listed to locate the reference
designs in a real field, not to rank them. Table 21 lists them.

**Table 21.** Aircraft occupying the same mass range as the two reference designs.

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
arrangement of Section 2.9 is the practical choice at this scale rather than an unusual one.

**The fourth statement — that the reference designs outperform these aircraft — is not made.**
Sections 3.7 and 3.8 are calculated from a mass budget with an unpaid structural margin; this
table describes aircraft that exist and fly. Placing a calculation beside a measurement and
declaring a winner would be a category error. Several entries are also fully electric, for
which endurance is set by battery specific energy rather than by configuration, so comparing
them with a fuel-burning design would compare energy sources rather than architectures. What
could properly be compared, once such aircraft are built, is **range at similar payload** — a
configuration carrying a comparable load further is making an architectural claim, while one
carrying a heavier load is making a claim about mass budgeting, which is the least validated
part of this study.

## 4.2 Why the market looks the way it does

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

**Where this configuration sits in that statement has to be said precisely, because the obvious
reading is too generous to it.** Against the two families that bound the band, the case is
straightforward and is why the configuration exists: it needs no runway, which the fixed-wing
family cannot say, and it carries a cruising wing, which the multirotor family does not — the
sizing set of Section 3.1 puts a turboshaft quadrotor at an *effective* lift-to-drag ratio of
4.9 against this configuration's *aerodynamic* 8.8 to 10.8. Those are different kinds of number
— the first a system-level figure of merit, the second a force ratio — and the comparison is
offered for scale rather than as a measured margin. **The claim that survives it is structural:
a vehicle that carries its cruise lift on a wing is in a different efficiency class from one that
carries it on rotors, and no sizing contract moves a vehicle between those classes.** On both
edges the band is genuinely wider.

**Inside the band, against the other hybrids, the claim splits and one half of it fails.** Once
the free-wheeling drag of the attitude rotors is charged, this configuration retains 0.632 of its
clean cruise efficiency against the lift-plus-cruise layout's 0.765. **It surrenders more cruise
efficiency, not less**, so on the range axis it does not widen the band against that layout — and
Section 3.6 measures the consequence, a range deficit of 24 to 45 percent under equal fuel
fractions. What it does hold is the mass axis, by 32 to 36 percent across the same bracket.
**The band is widened on one axis and not the other, and which one matters is the sizing
contract's question rather than the architecture's** — which is this paper's central result
arriving at its own case.

**None of that touches the third claim, because the third claim is not on this axis at all.**
Against the tilting family the offer of this configuration was never a longer range; Section 3.6
reports that the tilting layout leads on range under all three contracts, and that result stands.
The offer is that the same regime transition is reached **without reorienting a propulsor** — no
pivot, no nacelle actuator, no gyroscopic moment from tilting mass, no variable-pitch hub. **Not
that the aircraft has no moving parts:** roll is supplied by the variable-extension strip of
Section 2.10, which is a moving aerodynamic device and is charged as one in Section 3.5. The
claim is the elimination of a mechanism *class* — the one that turns a propulsor between hover
and cruise — and it is stated that narrowly on purpose. Every one of the tilting layout's range advantages
in Section 3.6 is computed with its nacelles, pivots, actuators and hover-pitched blades credited
as aerodynamically free and mechanically reliable; the present configuration has nothing
corresponding to charge, because it has nothing corresponding. **That is a hardware claim rather
than a performance claim, it is countable rather than contract-dependent, and it is the reason
this configuration is proposed at all.** Whether the hardware saved is worth the range given up
is a question for a designer with a mission in hand, and this paper does not answer it for them.

**Stated together, then, the three claims sit on three different axes against three different
families, and each is safe from the others.** Runway independence against fixed wings is not
weakened by a range deficit against lift-plus-cruise. Wing-borne cruise against multirotors is
not weakened by a tilting layout flying further. Freedom from mechanism against tilts is not
weakened by anything in Section 3.6, because Section 3.6 measures range and the claim is about
parts. The one thing that would damage all three at once is the aircraft not flying, and
Section 4.4 is the honest account of how close that possibility still is.


This is a configuration study. It contains no experimental validation of any kind, and
the numbers in it are the output of elementary methods applied to a set of assumptions.
This section states what those limits are, in enough detail that a reader can judge how
much weight each result will bear. Several of the items below were discovered during the
study and changed its results; they are recorded here rather than smoothed away.

## 4.3 What is not shown

**No part of this study has been validated experimentally.** No wind-tunnel test, no flight
test, no hardware. Everything here is calculation, and the calculations rest on assumptions
stated in the sections that use them. Supplementary S5 enumerates every limitation item by item
with the break-even value of each assumption that has one. This section states the ones that
bear on the conclusions.

## 4.4 The three that could change a conclusion

**The buffer's specific power is the most exposed number in the paper.** Bill 3 is avoided by
sizing the engine for cruise and supplying the hover excess from a battery buffer, and the light
design's buffer implies **5.63 kW kg⁻¹** to hover and **6.48 kW kg⁻¹** to leave the ground. Both
figures are taken at the electrical bus, where the buffer is; an earlier version of this paper
differenced the rotor shaft against the engine shaft and reported 4.61, which understated the
demand by a fifth. A 24S nickel–cobalt–manganese pack designed, built, bench-tested from 0.2 C
to 10.68 C and flown in an electric VTOL aircraft measures **724 W kg⁻¹** continuous for the unit
pack and **892 W kg⁻¹** for the flight system, reaching roughly 1.5 kW kg⁻¹ at its maximum tested
rate with a thermal margin of 4.9 °C [47]. A NASA-funded design study adopts 4 kW kg⁻¹ and states
that this is "about twice that of existing batteries" [48]. The defence available earlier — that a
short-duration buffer is a different product from an energy-optimised automotive pack — does not
survive, because the source above *is* that product.

**An earlier version of this section then compared a 6.8 kg buffer against 2.2 kg of unallocated
mass and concluded that the budget does not close at any measured specific power. That comparison
was a subtraction inside a box that had been sized on the number being replaced, and the
conclusion drawn from it was too strong.** A heavier buffer raises take-off mass, which raises
hover power, which raises the buffer again; at constant disc loading that feedback is linear
rather than divergent, so it accumulates to a finite answer and the answer is not where the
subtraction pointed. Closing the loop — holding wing and disc loading, holding the fuel fraction
so that range is preserved, and rebuilding the component budget at each step — gives (Table 22):

**Table 22.** Take-off mass, buffer mass, range and payload as the buffer specific power is varied, with the sizing loop closed at each step.

| Buffer specific power | Take-off mass at 13 kg payload | Buffer | Range | Payload if held at 50 kg |
|---|---:|---:|---:|---:|
| 0.724 kW kg⁻¹, measured continuous | **no solution** | — | — | 0.9 kg |
| 0.892 kW kg⁻¹, measured continuous | 162.0 kg | 42.4 kg | 1 600 km | 3.9 kg |
| **1.5 kW kg⁻¹, measured thermal ceiling** | **68.9 kg** | **10.7 kg** | **1 600 km** | **9.2 kg** |
| 5.63 kW kg⁻¹, assumed here | 50.0 kg | 1.8 kg | 1 600 km | 13.0 kg |

*The range column is constant by construction: the loop holds the fuel fraction so that range is
preserved while mass is solved for. Its value is the published one; on the drag bracket of
Section 3.6 the same column would read 1 173 to 1 442 km throughout, without changing any mass in
the table.*

The right-hand column is the same loop run the other way and it needs its arithmetic stated,
because the figure is not a subtraction from the payload. Take-off demand at 50 kg is 11.66 kW at
the bus, so a 1.5 kW kg⁻¹ buffer masses 7.78 kg against the 1.8 kg already budgeted. The extra
5.98 kg does not come off the 13 kg payload directly: the component build-up leaves **2.2 kg
unallocated above the payload**, and the buffer takes that first. Payload falls by the remaining
3.8 kg, to 9.2. **That figure therefore spends the whole of the structural margin** — the 2.2 kg
into which Section 4.4 below says buckling, torsion, local load introduction, fasteners, adhesive
and paint must all fit. Read without that condition the column is too kind by 2.2 kg.

**At the highest rate yet measured on a flown pack the aircraft exists.** It is 38 percent
heavier than the reference design, it carries a buffer of 15.6 percent of take-off mass rather
than 3.6, and its range is unchanged because the fuel fraction is what sets range. Held instead
at 50 kg, it carries 9.2 kg rather than 13. At the pack's *continuous* rating the loop does not
converge at all for the take-off demand, so the sharper statement survives there.

The correction cuts both ways and both should be stated. The reference design is not unreachable,
which is what the earlier sentence implied; and the comparison that opens this paper is made at
50 kg against a lift-plus-cruise layout at 86 kg, so an obvious reading is that at a measured pack
the margin falls to 69 against 86 — twenty percent rather than forty-two. **That reading is wrong,
and it is wrong in this configuration's favour, which is why it is corrected here rather than
left standing.** It grows A on the measured pack while holding B at a mass sized on the assumed
one. Section 3.6 now re-sizes all three architectures on the same buffer fraction, and the
lift-plus-cruise layout is the one that suffers: its hover power per unit mass is the highest of
the three, the buffer feeds back through hover power, and somewhere between eighteen and twenty
percent of take-off mass its budget stops closing altogether. **What the measured pack costs is
not this architecture's margin but the competing architecture's existence.** The figure that does
move against this paper is the rotor drag of Section 3.3, which takes the mass margin from
forty-two percent to between thirty-two and thirty-six, once both layouts are
re-solved on the same drag at each end of the computed bracket, and reverses the range comparison
under one of the three contracts.

**The aircraft leaves the ground on its control propellers, and that is a dependency rather than
a design feature.** Section 2.12 sizes hover power at thrust equal to weight, so the primary
propulsor supplies T/W = 1.00 exactly and no more. The margin to take off comes from the four
tip pairs, which raises the achievable ratio to 1.066 for the light design and 1.041 for the
heavy one with full rotation authority retained, and to 1.132 and 1.082 with none — never to the
1.2 an earlier version of Section 3.15 assumed. Three things follow
and none of them is closed here: the take-off margin and the attitude authority are drawn from
the same four propellers and compete; the buffer must carry the tip pairs as well, which is the
6.48 kW kg⁻¹ above; and a rotation entered from rest, rather than from a climb, now loses 14.7 m
at the light design's own two seconds. The entry climb of Section 3.15 is therefore a requirement
of the configuration and not a refinement of it.

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

**The transition pitching moment is not computed, and Section 3.17 shows the computation is not
currently reliable for anyone on this class of configuration.** Three methods of three fidelities
fail above roughly ten degrees of incidence, the highest of them against wind-tunnel measurement
[39,44], and the incidences this aircraft passes through lie inside that band. **This item
belongs to measurement.** It asks for the pitching moment to about twenty-two degrees at low
dynamic pressure, on the outboard half of the wing — the inboard half lies in the slipstream and
sees four to eight degrees — and for trim at cruise incidence.

## 4.5 What is assumed rather than derived

The planform's sweep, taper and thickness distributions were **chosen, not optimised**. The
centre of gravity is a packaging assumption. The zero-lift drag coefficient of 0.0248 and the
span efficiency of 0.85 are assumptions; Section 3.10 bounds both by calculation and neither
replaces its assumption — the span efficiency computes to **0.817, optimistic by 3.9 percent**,
worth 1.4 percent of cruise lift-to-drag ratio and of the ranges quoted. **The drag assumption is
the more serious of the two and it moved this round.** Counting the free-wheeling rotors of
Section 3.3, which no earlier version of the build-up contained, puts the computed bracket at
0.0285 to 0.0381 with 0.0248 below both ends rather than above them. Every lift-to-drag ratio, range and
architectural comparison in this paper is computed on 0.0248; **re-deriving them on a bracket that
now sits entirely above it is the largest single piece of unfinished work here**, and it is more likely to
move the comparative results of Section 3.6 than anything else left open. Torque balance is exact
at cruise only, leaving a small residual in hover. The comparative sizing of Section 3.6 is
conditional on the two competing architectures being modelled at the same level of detail as
this one, which they are not: they are modelled from published fractions.

**The vortex-lattice results carry an untested magnitude error, and the part of the chain it
threatens is not the part that was defended.** A published comparison on a blended-wing-body of
this class found the vortex-lattice lift coefficient low by thirty to thirty-eight percent
against RANS [39]. Section 3.10 argues that a near-constant multiplicative error of that kind
cancels in the ratios this paper takes from the solution — neutral point, static margin, twist
effectiveness — but the check that would confirm it is withheld in that source, so the argument
stands unverified. An earlier version of this section called this the one exposure in the
aerodynamic chain with no bound at all. **It now has one, and the bound points somewhere else.**
Perturbing the spanwise loading shape and re-solving shows that a one-degree mid-span
redistribution moves the neutral point by 0.15 percent of mean chord and the trim twist by 0.38
degrees; the neutral point would need a redistribution of 33 degrees to matter and the trim twist
one of 2.6. **The static margin — the quantity the cancellation argument exists to protect — is
the robust half. The trim twist is thirteen times more sensitive and the argument never covered
it.**

**A Reynolds-averaged solution has since supplied the missing redistribution, on three meshes
rather than one, and the answer is that the threshold is exceeded and the exceedance does not
matter much.** The local loading ratio holds to within five percent of a constant across nine
tenths of the span, which is direct support for the cancellation argument and the first evidence
for it of any kind. Refinement matters: the coarse mesh put the residual at 1.7 degrees of
equivalent redistribution and the converged solution puts it at **2.75 against a 2.6-degree
threshold**, so the first reading was under-resolution rather than agreement. **Carrying the
exceedance through the measured chain moves the trim twist by one degree, the span efficiency
from 0.817 to 0.799, and every cruise efficiency and range in this paper by 0.8 percent** — an
order of magnitude inside the drag bracket already applied to the same numbers. The exposure that
had no bound is therefore bounded, exceeded and quantified, in that order, and the trim chain
stands.

What does not resolve with refinement is the outboard tenth of the span, where the disagreement
is undiminished across a threefold change in cell count. That is where a vortex-lattice method
would be expected to fail and nothing in this paper is taken from that region alone, but a
strip-based estimate that depended on it would not be safe. Two limits belong with all of it: the
runs are untwisted, because the mesh generator has no field for twist; and the overall lift ratio
runs opposite to the published comparison cited above, which the paper reports rather than
reconciles.

## 4.6 What is sized but not closed

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

**The free-wheeling-versus-indexing trade is unpriced, and it is the first thing a reader of
Section 3.3 will ask.** Stopping the tip rotors edge-on at a controlled azimuth costs 0.0008 in
zero-lift drag against the free-wheeling state's 0.0154 — a factor of twenty — at the price of an
indexing mechanism this configuration was designed to avoid. The free-wheeling state was adopted
because it needs no hardware; it was not shown to beat the hardware, and this paper does not
compare them. The calculation is bounded and belongs in the next version of this work rather
than in a later one.

**The landing transition belongs on this list and had been left off it.** The forward
transition is treated in six subsections of Section 3 and the reverse — decelerate, rotate
nose-up, descend — in a clause. The two are not symmetric: the forward rotation gains dynamic
pressure while it turns, so lift arrives as the vertical component of thrust departs, and
Section 3.15 shows the altitude loss turns on that race; the reverse loses dynamic pressure
while turning, so lift departs before the thrust vector has returned to vertical. Nothing in
this paper models that case, no number here describes it, and the take-off transition must not
be read backwards to supply one. Together with the vertical descent above it, the landing is
the least examined phase of the flight profile.

## 4.7 Where this could most efficiently be attacked

Supplementary S5 lists six places. Two have been carried out and are folded into Section 3.10: a
three-dimensional solution for the centre body, and a viscous solution of the twisted planform
station by station. Of the remaining four, the most valuable is a Reynolds-averaged or
panel solution of this planform's loading — no longer because that exposure is unbounded, but
because it is now the one input a single number would close: Section 3.10 supplies the
sensitivity to a redistribution, and such a solution would supply the redistribution. **Three of the
four can be carried out computationally; the fourth cannot, and saying otherwise was the most
consequential thing this study got wrong about itself.** Transition controllability rests on a
pitching moment that three methods of three different fidelities fail to predict above roughly
ten degrees of incidence, the highest of them against wind-tunnel measurement, so it is blocked
on data rather than on effort — as is the fin derivative of Section 2.10, for the reason
Supplementary S3 gives. An earlier version of this section stated that none of the four required
an experiment. The configuration is described in enough detail in Sections 2 and 3 for another
group to attempt any of them independently, by whichever of the two routes each one needs. The computational setup, the
grid-convergence study and the record of what failed along the way are in the repository, so
every result here can be re-run and checked rather than taken on trust.

---

# 5. Conclusions

Hybrid vertical take-off aircraft pay for their vertical capability, and the payment is
architectural rather than a defect of implementation. It appears in three currencies — the mass
of hardware carried but unused, the drag of hardware exposed but inactive, and a power system
sized by a condition that holds for about two percent of the flight — and **each of the
architectural moves surveyed here reduces one of them by increasing another**. They are not
offered as the only costs a VTOL aircraft carries; they are the three that follow from the
duty-cycle mismatch, and the claim is about them. A NASA sizing study of four VTOL
architectures reaches the same conclusion from the opposite direction, finding the
lift-plus-cruise concept the heaviest of those examined while also the most efficient in cruise,
and naming the cause as the empty weight carried for hover.

Stating the tax that way makes its escape condition explicit, and it has four parts: **it is
charged unless hover and cruise are served by the same hardware, doing the same job, in the same
orientation, with the hover peak drawn from a buffer rather than from permanently installed
continuous power.** The configuration described here satisfies that condition **in the
propulsor that carries it**, rather than compensating for failing it — and re-opens the drag bill
in the attitude system that controls it, which is a result of this study rather than a caveat on
it. The aircraft rotates; nothing on the aircraft rotates relative to
it. A single coaxial pair at the nose provides all thrust in both regimes; four small coaxial
pairs at the tips provide attitude moments and the take-off thrust margin; and a strip on the
lower surface is assigned the one gap propellers cannot close — the rolling moment, which parallel thrust vectors cannot
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
still climbing removes the altitude penalty entirely in the point-mass model. That second result
survived a correction that might have removed it. The primary propulsor is sized at thrust equal
to weight and therefore supplies no climb at all; the margin comes from the four tip propellers,
which raises the achievable ratio to 1.066 for the light design and 1.041 for the heavy
one with full rotation authority retained, and to 1.132 and 1.082 with none retained, rather
than the 1.2 an earlier version assumed. Recomputed there, the altitude loss at both reference rotation times is still
zero — but acquiring the entry climb now takes twice as long, a rotation begun from rest is
worse than reported, and the take-off margin and the attitude authority are drawn from the same
four propellers and compete for them.

**A second correction did remove it, and that is the sharper limitation of the two.** The
point-mass model prescribes the attitude and so cannot charge for the time the aircraft spends
rotating into it. Solved instead with rotational dynamics and a finite control moment, and with
the aerodynamic pitching moment set to exactly zero so that nothing is borrowed, the light
design loses **5.4 m** at the same reference condition where the point-mass model reports none,
and the loss grows rather than shrinks as the controller is tightened. The zero-altitude-loss
result is therefore a property of the model that produced it. What replaces it is not a
prediction — the aerodynamic moment that would make it one is the quantity Section 4 says no
current method supplies — but a floor: the manoeuvre costs altitude even in the most favourable
case that can be constructed.

**What this paper offers is a configuration and its numbers, not a validated aircraft.** There
is no wind-tunnel data here and no flight test. Three of the analyses Section 4 lists as tests
of these results have been carried out, and they are named so that the count can be checked
against that section. A three-dimensional solution for the centre body narrowed the zero-lift drag without overturning the assumption. A component build-up closes the
light design with 2.2 kg in hand, conditional on a shell areal density at or below 1.78 kg m⁻²
*and* on a battery buffer no measured cell can yet supply, and leaves the heavy design's closure undetermined.
And a rotational check shows the tip propellers can turn the aircraft's own inertia through the
transition with a margin of 1.49 at 50 kg and 1.57 at 1000 kg on the cheapest profile — **0.99
and 1.05 on a smooth one**, and 1.14 and 0.76 at 50 kg if the tip thrust is recomputed on the
figure of merit used elsewhere in the paper rather than the one its design table implies. Under
every basis, both reference rotation times are actuator-limited lower bounds rather than
comfortable choices.

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

**Two things survive independently of that, and they should be stated separately because they
are claims of different kinds.**

**The first is the framework.** The three currencies, the demonstration that architectural
remedies transfer the penalty rather than remove it, the escape condition, and the finding that
architectural comparisons change their ranking with the sizing contract chosen — none of these
depends on whether this particular aircraft is ever built.

**The second is the configuration's architectural claim, and it is not a performance claim.**
Against the fixed-wing family this aircraft needs no runway; against the multirotor family it
cruises on a wing; against the tilting family it reaches the same regime transition **without reorienting a
propulsor** — no pivot, no nacelle actuator, no gyroscopic moment from tilting mass, no
variable-pitch hub. It is not a claim that nothing on the aircraft moves: the roll strip is a
moving aerodynamic device and the paper charges it as one. The tilting solution is the less widely
fielded of the two contemporary hybrid families, and the reasons given for that in the literature
are mechanical and control reasons rather than aerodynamic ones; **this configuration is offered
as an alternative route to the same end, and that is what it is for.** Each of those three claims
is made against a different family on a different axis, and none of them is a range ranking
against the other hybrids — a ranking this paper reports in full, finds to reverse with the
sizing contract, and does not claim. **The absence of a mechanism is countable and no contract
moves it; the range comparison is neither.**
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
    **2026**, 12 (9), 317. https://doi.org/10.3390/batteries12090317
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

- **Supplementary S1** — Independent checks on the two assumed aerodynamic coefficients (3811 words)
- **Supplementary S2** — A component build-up of the mass budget (3689 words)
- **Supplementary S3** — Control axes in full (6553 words)
- **Supplementary S4** — Rotational authority, trim, and the transition envelope (8310 words)
- **Supplementary S5** — The limitations in full (6724 words)
- **Supplementary S6** — The three bills stated formally, and a comparative sizing (3158 words)

The computational setup, the scripts that produce every number here, and a running record
of the corrections made during the study are in the repository this paper cites.
