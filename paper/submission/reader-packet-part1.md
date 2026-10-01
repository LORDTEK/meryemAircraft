> **Reader packet, part 1 of 4** (commit `0076354`). Read all parts before answering; the round text says what to judge.

# meryemAircraft — reader packet: the current body and the journal supplement draft

> Generated from the repository at commit `0076354` (branch `claude/ecstatic-cori-6w30at`). It is a reference for reading the round texts, not a task in itself.
>
> **Part 1** is the current body (14775 words) in the assembled numbering the round texts use (*"Section 5.2"*). The submission generator converts this to the journal's form (Roman-numeral sections, *Sec.*, numbered citations, American spelling, one figure); the wording is the same.
>
> **Part 2** is the journal supplement as drafted so far (5638 words), with each passage's provenance note.

---

# Part 1. The body

## 1. The gap

### Two families, two different limits

Uncrewed powered flight is dominated by two configuration families, and neither is bounded by
the thing the other is bounded by.

**Fixed-wing aircraft** carry payload over distance efficiently, because a wing sustains the
vehicle without continuously spending power on lift. Their limit is not aerodynamic but
infrastructural: a runway, a catapult, or an equivalent installation.

**Rotorcraft** remove that requirement completely. They take off and land
vertically, hover, and work from confined sites. Their limit is the converse: with no wing,
every second of flight is bought with installed power, so range and endurance stay modest and
worsen as the vehicle grows.

**Neither family is deficient.** Each is limited by the price of
doing it that way. **The corner where both capabilities are wanted at once is where the two
applications this work is aimed at sit** — wildfire observation and response, and cargo delivery to
places without a runway.
**That corner is not empty**, as the rest of this section sets out; what is unsettled is which
price an architecture in it must pay.

### What the contemporary answers do, and how each changes regime

Hybrid VTOL aircraft occupy that corner today. **This paper does not dispute that they work.** They take two routes between the regimes: lift-plus-cruise aircraft keep two sets of hardware and switch
between them, and tilting aircraft keep one set and reorient it (Section 5.1). Rotating a propulsor in flight brings a pivot and its
actuators, a gyroscopic moment during the rotation, and a control problem through a regime in which the aircraft is neither a
rotorcraft nor an aeroplane. **Those are mechanical and control requirements rather than aerodynamic ones**, and that distinction is
what this paper is built on.

### The third route is established, and some of its difficulties are inherited

There is a third way to put one set of propulsors into both regimes without reorienting them: **point the
thrust line at the ground and let the whole aircraft rotate.**
The Convair XFY-1 flew it in 1954 and completed six transitions to conventional flight *"before testing was
curtailed because of engine and gear-box reliability problems"*, and uncrewed tail-sitters have revisited the
route since. The pilot's spatial orientation and workload were real, **but they are not what curtailed the testing**, and they are the only ones of those documented obstacles an uncrewed aircraft removes.

**Some of the difficulties were real, internal, and are inherited here.** A tail-sitting vertical descent is
harder than a runway landing; a tail-sitter on the ground is more exposed to crosswind; and propellers whose
thrust vectors are all parallel to the body axis produce no rolling moment **by any combination of thrust
settings**. The reaction-torque channel that other coaxial tail-sitters use about that axis is a choice this
configuration declines rather than a limit it inherits (Sections 5.1 and 5.2).

What has changed is electric drive on each individual rotor, sensor-based attitude reference, and enough onboard computation that stability need not come from the airframe alone. **The uncrewed tail-sitter literature has been exploiting exactly those three for over a decade**; the gap below is not a historical one.

### What is already occupied, stated before the gap

**The route itself is established.** Uncrewed tail-sitters combining fixed-pitch rotors with a
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
flight."* A long-range tail-sitter reported in 2018 names variable pitch as the remedy, at the cost of extra actuators and mechanism weight, and even with cyclic and collective pitch still sizes its rotor as a compromise between hover and forward flight.

### The gap, stated precisely

**Each half of the required capability is well served, and both halves together are served by
the contemporary hybrids.** This paper does not claim otherwise. **And the third route is
occupied.** What follows is therefore not a claim to an empty field.

**What is not established is the combination taken together with its price.** Specifically:
a blended-wing-body tail-sitter in which *every* propulsor is a coaxial, torque-balanced pair —
so that reaction torque and net angular momentum are given up along with the reorientation
mechanism — carrying no aerodynamic control surfaces beyond a single moving device, powered
through a buffered series hybrid, and **audited explicitly against carried hover mass, exposed
cruise drag and hover-sized continuous power**, the last two of them at two scales, and under three sizing
contracts.

Each of those choices costs something, and **the giving-up is the part that is not free**. **Operating every pair torque-balanced spends the reaction-torque channel to buy the torque balance and
the near-zero net angular momentum**, and leaves the moment about the propeller axis to a single aerodynamic device.

**None of the elements is new**, and Section 5.1 says so. Tail-sitting aircraft are seventy years old; blended wing bodies have been a standing subject of transport
research for more than three decades; series-hybrid propulsion has been designed for small uncrewed aircraft. The route is not claimed to have been waiting to be found. **The contribution is the
architecture: a configuration arranged to change regime by rotating the airframe rather than its
propulsors, and so carrying no mechanism that reorients a propulsor.** The combination, the
consequences of the choices inside it, and an accounting of what they cost are how that contribution
is presented and priced.

## 2. The charges, the condition, an independent check

### 2.1 The tax

**A claim that one architecture escapes a cost shared by the others is only meaningful if the cost is stated first, in terms that do not presume the escape.** This section states it. It is not a claim about any particular aircraft, and nothing in it is new physics; what it provides is the accounting that the rest of the paper is checked against.

#### The root: a duty cycle that does not match the hardware

For a mission of one hour, a take-off, a transition, a return transition and a landing occupy on the order of a minute — **roughly two percent of the flight.** **An architecture that provides the vertical phase with a dedicated lift subsystem therefore carries it for fifty times as long as it uses it.** This is not an implementation defect and it cannot be removed by making the subsystem better, because it is a statement about duty cycle rather than about quality. **The mismatch between how long a component is needed and how long it is present is the origin of all three charges below.**

The statement is deliberately confined to architectures with a dedicated lift subsystem, because that is the family the charges describe.

#### Bill 1 — mass

A lift-plus-cruise aircraft carries two propulsion groups: rotors, motors, mounts, wiring and structural reinforcement for the vertical phase, and a separate propulsor for cruise. The vertical group provides no required lift or thrust during cruise and is lifted anyway.

Its cost is not linear. Mass growth feeds itself — MTOW = m_payload / (1 − f_empty − f_energy) puts additional empty mass through a multiplier that grows as the denominator shrinks — and in the vertical phase the same increment is counted a second time, because at a fixed disc area hover power scales with W^1.5. A modest dead-mass fraction becomes a large payload penalty.

#### Bill 2 — drag

The second payment falls on architectures that leave hover hardware exposed in forward flight: rotors stopped in the airstream, the booms that carry them, and the interference between their wakes and the wing. Cruise drag has other sources on any aircraft; what is charged here is the part attributable to hardware retained for a phase that is over.

Wind-tunnel work on a hybrid airframe found that the difference between propellers parallel to the airflow and no propellers at all is modest, while *"the drag produced by the motors is significant."* The bill is charged mainly by the motors — hardware that cannot be feathered or aligned away, **because its cost is its presence**; the same work notes that its motors were chosen for performance rather than for low drag, and that the drag of the supporting beams is limited. Wind-tunnel characterisation of a quadplane found drag in the hybrid regime generally exceeding either pure mode through adverse flow interaction, and that a simulation assuming negligible rotor–structure interaction *"always predicts higher lift and lower drag than were experimentally observed."*

**The important property of this charge is not its size but where it falls.** It is charged per unit time in cruise — so it grows with exactly the quantity the aircraft exists to maximise.

#### Bill 3 — power system sizing

A VTOL aircraft must install enough power to hover. The ratio between the two demands follows from the governing equations rather than from any design choice (Supplement S2):

    P_hover / P_cruise = √(DL / 2ρ) · (L/D) / V · (η_p / η_h)

**The quantities on the right come from the configuration and from the propulsion operating points, not from the duration of the hover phase.** η_h and η_p are not configuration constants, they depend on the propeller and on the condition it is run at, and Section 6.2 computes what happens when one fixed-pitch blade has to supply both. Raising the disc loading raises the ratio as its square root.

The power system is therefore sized by a condition that holds for a minute and is then carried, unused, for an hour. Sizing by hover means an oversized engine, or a battery that must deliver a peak it will rarely be asked for, or both — and whichever is chosen, the extra installed capacity is mass: a cost in kilograms, though not Bill 1.

#### The charges are coupled: remedies move cost, among the three charges or outside them

The three charges are not independent problems with independent fixes. **Each known partial remedy reduces one charge and pays for it, in another charge or in a cost outside the three.** They are three distinct accounting quantities, paid in kilograms, drag counts and installed kilowatts, and they are not assumed to be independent physical causes: a remedy can move a requirement from one currency into another. Whether a change of size moves them together, which would make them one quantity under three names, is tested in Section 6.3.

**A charge and its currency are not the same thing.** Each charge is one specific payment, not the name of the currency it is paid in. Bill 1, as this accounting uses it, is the mass of a dedicated lift subsystem; Bill 2, the cruise drag of hover hardware left exposed; Bill 3, continuous power installed to a hover peak.

| Move | Bill it attacks | What it creates — a bill by its number, any other cost in words |
|---|---|---|
| Distributed electric lift rotors | 3 — the cruise engine no longer sizes to hover | 1 and 2 — many rotors and mounts, permanently carried and exposed |
| Folding or retracting lift rotors | 2 — the exposed rotor is removed from cruise | 1 — mechanism, actuation, locking; and a new failure mode, not among the three |
| Tilt-rotor, tilt-wing, tilt-nacelle | 1 — one propulsion group serves both regimes | kilograms, not Bill 1 — the pivot and its actuators; **Bill 3**, imposed or left standing according to how the architecture the move modifies supplies its hover peak — with no store, the power plant is sized by the hover peak; and gyroscopic coupling and a transition control problem, which are **not among the three** |
| Variable-pitch or feathering propulsors | 1 and 3 — one propulsor is retrimmed across two widely separated operating points instead of duplicated | kilograms, not Bill 1 — pitch hub and actuation; and a new failure mode, not among the three |
| Higher disc loading, smaller rotors | 1 and 2 — smaller, lighter, cleaner rotors | 3 — hover power rises with √(DL) |
| Lower disc loading, larger rotors | 3 — hover power falls | 1 and 2 — larger structure and exposed area |

**One row pays part of its cost in none of the three currencies, and that is not an oversight**: the tilting row's gyroscopic coupling and transition control problem are costs, but not charges this accounting tracks. **The table is not a census of the field**; it lists the moves whose transfers are documented, and a remedy absent from it is not thereby claimed to cancel a charge.

One of these transfers has direct experimental support (Supplement S2).

#### What this accounting is for

**The accounting is refuted by a counter-example, and the table above is where one would appear:** every entry in it moves cost rather than removing it.

**Stated positively, so that the test can actually be run: a counter-example is a remedy that reduces one of the three charges, leaves the other two no worse, and whose own cost is either absent or demonstrably smaller than the reduction — measured in the same currency.** **The accounting claims transfer. It does not claim that every architecture is equally good**, and a remedy that is simply a better bargain in one currency refutes it.

**Two clarifications keep the test from being either too easy or unfalsifiable.** **"No worse" is judged against the architecture the move modifies.** A move that reduces one charge and makes another worse is a transfer between charges. And a remedy whose cost falls **outside** the three charges does not refute the accounting, because the accounting is about those three; **but it is not thereby exempt from being counted.** The tilting row, which needs both clarifications, is worked through in Supplement S2.

The accounting also makes a prediction that can be checked without settling the architectural question at all: **where an arrangement pays one charge heavily in order to escape another, its ranking against a differently-balanced arrangement will move when the sizing rule changes — toward the lighter arrangement as the rule weights mass more — and will reverse where that reweighting carries it past the point at which the two break even.** Section 6.4 tests both the movement and the reversal on this configuration, and Section 2.3 tests a different consequence against a sizing study this work did not produce.

Whether an architecture can decline the mismatch itself, rather than redistribute its consequences, is a different question, and the next section states the condition it would have to meet.

### 2.2 The escape condition

This section asks what an architecture would have to do in order not to incur the three charges at all. The answer is a **definition**, derived by inverting the table, and it is stated here before any configuration is offered so that the standard is not taken from the thing it will be used to measure.

#### Inverting the table

**A charge appears wherever the two regimes are served by hardware that departs from one of four things: the same hardware, serving both duties, held in one orientation, with the hover peak supplied other than by its continuously installed power.** **Different hardware** costs Bills 1 and 2. **The same hardware serving only one duty** costs them again. **The same hardware serving both duties in a different orientation** is the tilting family. **The same hardware, both duties, one orientation, but a different sizing point** incurs Bill 3. What each departure costs is in Supplement S3. Read one at a time, these are ways to pay. Read as a conjunction, they are a condition.

#### The condition

> **An architecture does not incur the three charges if the propulsors that carry the weight,
> held in one orientation relative to the airframe, produce both the hover thrust and the cruise
> thrust, and if the difference between the hover peak and the cruise demand is supplied from
> a store rather than from permanently installed continuous power.**

Four parts: **same hardware, both duties, one orientation, hover peak from a store.**

Two things in that sentence are choices rather than derivations. The inversion requires only *one orientation relative to the airframe*; **how** an architecture keeps that while changing flight regime — by rotating the whole body, or otherwise — is not in the inversion, and is treated as exposition rather than as part of the definition. And the fourth departure's exception lets the peak come from **any** source other than the continuously installed power; a store is the narrower reading used here, because it is what the configuration examined later uses and because a narrower condition is easier to fail.

#### What the condition does not say, and this matters more than what it says

**It means zero of the three charges as Section 2.1 defines them.** **It does not mean an architecture that costs nothing, and it does not mean an architecture that carries nothing for the vertical phase.** A definition that placed every conceivable cost inside the thing to be escaped would be unfalsifiable. Six costs are permitted, named here before any candidate is examined (the working is in Supplement S3):

- **A store is permitted**, though it is mass carried for a duty that is briefly needed, which is the complaint Bill 1 makes. **It does not claim the trade is favourable**: whether the store is lighter than the continuous power it displaces is computed, not asserted.
- **Releasing the engine is not releasing the electrical path.** Machines, power electronics and wiring still pass the full hover power, and that Bill 3 is carried in the ledger.
- **Rotating the airframe is permitted and is not priced here.** An architecture that rotates its whole body still turns its thrust axis through ninety degrees relative to the flight path, with the moments and the control through the turn that implies; that is not one of the three charges, and Section 6.1 analyses the transition without pricing it.
- **Hardware installed for the vertical phase is permitted if it serves both duties.**
- **Hardware used in both regimes for something other than propulsive thrust is permitted, and its cruise drag is not eliminated.** *Cruise thrust in this paper means the thrust that balances cruise drag.* Attitude devices produce none; used throughout the flight, they fall outside Bill 1, and they do not stop the propulsor that carries the aircraft from meeting the condition. But carried through cruise without producing cruise thrust, they are the first failure mode below, and Bill 2 reaches them.
- **Serving two regimes with one set of hardware has a price of its own**: a fixed geometry cannot be optimised for both, and the compromise is paid in efficiency. **The condition permits that cost and does not measure it.** Section 6.2 does.

**One exclusion, stated narrowly.** Structure, surfaces and actuation present for reasons other than the vertical phase are not charged **as duty-cycle mismatch under this accounting**, which says which ledger they belong in, not that they are free; it does not reach a part that would not exist but for the vertical phase. The tip frames of Section 3 are landing gear because the aircraft stands on its tail: **their mass is charged in the build-up and their drag in the ledger.**

#### The condition can fail, and how

An architecture fails the condition if **any** of the following holds:

1. It carries a propulsor through cruise that produces no cruise thrust.
2. It changes the orientation of a propulsor relative to the airframe in order to change regime.
3. Its continuously installed power is sized by the hover requirement rather than by cruise.
4. It satisfies the first three only in part — for instance in its primary propulsor while a secondary set fails them — in which case the instantiation is **partial**, and the part that fails re-opens the charge it fails.

#### What follows from the condition, and what does not

The condition is a statement about what an architecture would have to be. **It is not a claim that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim that satisfying it is desirable.**

**An architecture that reorients a propulsor does not satisfy the condition as written**, because the condition requires one orientation relative to the airframe. **Whether such an architecture might avoid the three charges by some other route is a separate question this paper does not settle** — the condition is a definition, not a law, and it can be too narrow without being wrong.

### 2.3 An independent quantitative check

An accounting proposed by the same people who then use it invites one obvious objection: that the charges were chosen because a particular aircraft happens not to pay them. **What follows is not a test of the whole framework.** It checks one falsifiable consequence on one independent data set. The working is in Supplement S4.

**The prediction has two halves, and only the first is a derivation.**

> **First half, derived from Section 2.1.** A configuration carrying a dedicated lift system pays for it in gross weight, and the payment is amplified.

> **Second half, not derived.** That the cruise efficiency the arrangement buys does not cover that payment.

The check tests the second half on independent data, with the first half supplying the reason to expect the outcome: the weight charge is amplified by a multiplier, while the efficiency credit enters linearly through the cruise lift-to-drag ratio. **The prediction is also mission-dependent**, and the page would be weaker for hiding it. The mass charge of carried lift hardware is roughly fixed; the efficiency credit accumulates with distance. The mission used below is short.

The check uses a NASA study, conducted for its own purposes and with no relationship to the present work, that sizes **five VTOL architecture families** — nine designs in all — against a single mission with common tools and common assumptions; it does not use the three-bill accounting of Section 2.1 or any framework derived from it. It is used for three reasons, stated so that the choice is not merely the one that agreed: it holds the mission fixed across architecture families, it applies one set of tools to all of them, and it reports both quantities this prediction needs. The mission is 1 200 lb of payload over 75 nautical miles. Two of the nine designs matter here. **The turbo-electric lift-plus-cruise design reaches 8.5 at 7 271 lb and carries a dedicated lift group — eight lift motors beside its cruise motor. The turbo-electric tilt-wing reaches 8.6 at 6 584 lb with none: eight proprotors, reoriented.**

**The primary comparison is the lift-plus-cruise design against the tilt-wing**, because they isolate the charge: they share the mission, the payload, the turbo-electric propulsion architecture and the presence of a cruising wing. **They are not identical in every other respect** — one stops its lift rotors in the airstream and drives a separate pusher, the other reorients its proprotors on a tilting wing — **but the difference the comparison turns on is that one carries a dedicated lift group through cruise and the other does not.** The comparison is the closest the published set comes to isolating that charge; it is not a controlled experiment. **The tilt-wing is 1.2 % better in effective cruise efficiency and 9.4 % lighter.** The design gross weights differ by 687 lb in the tilt-wing's favour. **That figure is the net difference between two architectures, not the measured mass of a lift group**. **The published weight breakdown is consistent with the transfer property of Section 2.1 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce**: its three reported categories account for 580 lb of the 679 lb empty-weight difference, and the remaining 99 lb lies in categories it does not break out (Supplement S4). **The framework does not predict any of these numbers**; without the input fractions it predicts no magnitudes. What it predicts is that the amplified weight charge survives the efficiency credit, and on the isolated pair it does so with the credit reduced to nothing.

**The architecture proposed later in this paper is not the only way to avoid the first charge.** The tilting family avoids it too. The margin in cruise efficiency is 0.1 in effective lift-to-drag ratio, and nothing is claimed from its direction. What separates the tilting family from the configuration described later is not this axis; it is what each pays, and a sizing study does not settle that.

The check establishes that one prediction of the accounting holds on data produced elsewhere, for purposes unrelated to this argument. **It does not establish that the accounting is complete**, that the three charges are the only costs an architecture pays, or that avoiding them makes an aircraft better. **It does not establish anything about the configuration this paper proposes**, which has not yet been described, and which is not in the study used here. **An instrument whose first use is to measure the thing its authors are advocating should be shown working on something else first**, and that is why this section comes before the aircraft. **The instrument is now fixed, and it is not modified again.** **Everything that follows is measured with it rather than added to it.**

## 3. The first half: operation without a runway

### The opponent, and the axis

On this axis the alternative is the fixed-wing aircraft, and the comparison runs one way only.
**Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency**, where a
runway-launched aeroplane that never bought vertical capability pays none of the charges of
Section 2.1 and is the better machine. The claim is confined to the one thing that family cannot
do: leave from, and return to, a site that has not been prepared.

### What the requirement actually is

A catapult-launched fixed-wing aircraft also leaves without a runway. What it does not do is
**come back** to the same unprepared site, and it does not travel without the launcher. The two
applications this work is aimed at need the aircraft to arrive somewhere that has no infrastructure, and
to leave again.

So the requirement is: **the aircraft carries everything it needs to depart and recover, and the
site supplies no prepared launch or recovery infrastructure of any kind.** A net, a catapult, a cradle, a prepared
strip or a recovery vehicle each fail that test — including the ones that fail it only on the
recovery half.

### How the configuration meets it

The aircraft stands on its tail, with its longitudinal axis vertical, in its own storage
attitude. **No launch equipment is present.** It rests on five points: the four lower ends of
the tip frames and the aft end of a keel running along the centreline.

**Those five points are not added hardware.** The tip frames are the landing structure, they are
also the structure that carries the four tip pairs (the attitude propellers) and sets their moment arm, and their
fairing is the aircraft's only vertical surface. **One structure serves four purposes and is
charged to the mass budget once** — Section 5.2 gives the fairing's sizing.

**The saving has precedent and it is not this paper's observation.** Reviewing the tail-sitters
of the 1950s, NASA recorded that *"dispensing with a conventional landing gear improved the
empty weight fraction for these VATOL aircraft"*, while noting that some form of gear was still
required on the tail surfaces, that such gear was limited to low sink rates, and that tip-over was
*"a constant worry in gusty air and on uneven ground, particularly with the propellers turning."* The present arrangement takes the weight benefit and extends it by
giving the same structure the control duty as well.

**And the stance base is a parameter rather than a constraint.** Moving the frame ends further
outboard widens the base against ground wind without altering the planform, the propulsion or
the control architecture — and because the same displacement lengthens the control moment arm,
both benefits arrive from one change. The 50 kg reference geometry (Section 5.2) is one point on that trade; an
operator with a stronger ground-wind requirement can take another.

### What is sized, and what is not demonstrated

**Sized.** The vertical phase is sized: hover power from momentum theory at thrust equal to weight, the buffer that supplies what
the engine cannot deliver of that peak (at a specific power Section 7 examines), the tip-frame lengths that set both the stance base
and the control arms, and the structure that carries the landing loads. Section 6.1 reports **whether** they close. This section does
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
about the body's longitudinal axis (Section 5.2). **What that refusal costs in authority and in response time is not computed**, and
Supplement S14 carries it.

**And one historical difficulty is inherited rather than removed.** A tail-sitting aircraft on
the ground is more prone than a conventional one to tip over, in crosswind and on uneven ground. The stance base is the answer
this configuration offers, and it is a parameter rather than a proof.

### What the historical record does and does not give back

One of the 1954 objections is genuinely removed and it should be named exactly. The landing
difficulty of the 1950s tail-sitters was attributed to a pilot judging a backwards vertical descent by looking
over his shoulder, to turbulence sensitivity and to reduced control power near touchdown.
**There is no pilot here, and height above ground is a sensor measurement rather than a human
estimate.** That disposes of the spatial-orientation objection and nothing else. **Precise
hovering, ground gusts and the descent itself are not disposed of by removing the pilot**, and
this section does not pretend otherwise.

### What this half costs

Runway independence is not obtained free, and the charges appear later rather than here. The
tip frames that make the aircraft self-supporting are structure standing in the cruise
airstream, and Section 6.2 charges their drag. The tip pairs they carry are exposed
for the whole cruise and cannot be feathered, and Section 6.2 charges that too. The buffer that
releases the engine from the hover peak is mass carried for the whole flight.

**The second half — cruise carried on a wing rather than on rotors — is the subject of the next
section**, and the two are combined in Section 5.1.

## 4. The second half: cruise carried on a wing

### The opponent, and the axis

On this axis the alternative is the rotorcraft — multirotor and helicopter alike — and as in the previous section the comparison
runs one way only. **Nothing here is claimed against fixed-wing aircraft.** The claim is
confined to the one thing the rotorcraft family structurally lacks: **a surface that carries the
cruise lift.**

### What the requirement is

Section 3 established the first half: the aircraft must leave from and return to a site that
supplies nothing. **A rotorcraft meets that requirement completely.**

What it does not meet is the second half of both missions. Wildfire observation and response,
and cargo delivery to places without a runway, each require the aircraft to **cover distance
after it has left the unprepared site**, and a vehicle with no wing buys every second of that
distance with installed power. The consequence has been stated independently: surveying the
field, one study concludes that multirotors are efficient in hover and suited to short-range
missions, while vectored-thrust aircraft are efficient in cruise and suited to long-range ones.

### What the configuration does instead
