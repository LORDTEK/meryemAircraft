# meryemAircraft — reader packet: the current body and the journal supplement draft

> Generated from the repository at commit `84fb24e` (branch `claude/ecstatic-cori-6w30at`). It is a reference for reading the round texts, not a task in itself.
>
> **Part 1** is the current body (14786 words) in the assembled numbering the round texts use (*"Section 5.2"*). The submission generator converts this to the journal's form (Roman-numeral sections, *Sec.*, numbered citations, American spelling, one figure); the wording is the same.
>
> **Part 2** is the journal supplement (7464 words), complete, without the provenance notes: the text as it will be submitted. The notes are in the repository, `paper/submission/supplement-src.md`. It keeps the archive labels (S2–S14) that the body's pointers use; the submission renumbers both to S1–S11.

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

**Cruise lift is carried by the airframe itself.** At
the cruise condition the lift coefficient follows from `C_L = W/(qS)`, the drag from
`C_D = C_D0 + C_L²/(πARe)`, and the nose pair is left with one job — producing the thrust that
balances that drag. It supports none of the weight.

**A rotorcraft's rotors must produce the lift and the propulsive force
together, throughout cruise.** This aircraft separates them: a surface holds the aircraft up and a
propeller pushes it along, and **the wing produces its lift without a separate continuous power
supply of its own** — the power the aircraft spends in cruise goes to overcoming drag, of which
the lift's share is the induced part.

**But the size of the resulting advantage is a calculation, not a consequence of that
statement**. The rest of this section is the calculation,
and it gives a smaller number than the structural statement invites.

### What the margin actually is, in one currency

The sizing set of Section 2.3 reports an **effective lift-to-drag ratio**, `L/De = WV/P`: a system figure of merit that already
contains the propulsive efficiency of whatever produces the thrust, so **a force ratio cannot be placed beside it.** In level cruise,
with shaft power `P = DV/η_p`,

> **L/De = WV/P = (L/D) · η_p**

**Which power `P` denotes is not assumed here**, because reading it as electrical rather than shaft power would make this
configuration's figure incomparable with the published one. The source writes hover power with the figure of merit applied, which is
shaft power, and applies the propulsion-system efficiency separately, for the all-electric entries as for the shaft-driven ones.

The aerodynamic ratio is **8.79 to 10.82**, with the tip frames and the free-wheeling tip-pair rotors (Section 5.2) already charged; that
spread is **uncertainty**, the zero-lift drag bracket. The cruise propeller efficiency is **0.632 to 0.683** across the nose-blade
families that meet the hover figure of merit; that spread is **not uncertainty** but a design variable this study has not fixed.

| L/De | η_p 0.632 | η_p 0.683 |
|---|---:|---:|
| **L/D 8.79** (adverse drag) | 5.56 | 6.00 |
| **L/D 10.82** (favourable drag) | 6.84 | 7.39 |

**These are the bounding corners of a product, not four simulated aircraft.** Across the examined envelope they give **5.56 to
7.39**; for the best examined blade family, at 0.683, **6.00 to 7.39**. Which blade a designer would choose also turns on structural
loads, acoustics, the motor operating point, rotor inertia and manufacture, **none of which is modelled in this work** (Supplement S6).
Section 6.1 carries one blade into a closed sizing loop; until then no corner is presented as the aircraft's performance.

### What the comparison gives, against both published quadrotors

The sizing set contains two quadrotors for the same mission, and **neither is treated here as the primary one.**

| | L/De | vs examined envelope 5.56 – 7.39 | vs best examined family 6.00 – 7.39 |
|---|---:|---|---|
| Quadrotor, turboshaft | 4.9 | +13 % … +51 % | **+22 % … +51 %** |
| Quadrotor, all-electric | 5.8 | −4 % … +27 % | **+3 % … +27 %** |

**Against the turboshaft quadrotor the sign holds at every corner of both readings**; closing it would need a propeller efficiency
of 0.557, against 0.632 for the least efficient blade family examined.

**Against the all-electric quadrotor it does not hold at the low corner**, and that result is reported as a result rather than as a
caveat. That vehicle reaches 5.8 with 1 742 lb of battery and nearly twice the gross weight for the same mission, 7 221 lb against
3 678 lb. **That higher gross weight is consistent with the mass charge Section 2.1 describes**; this table alone does not establish the
causal link, and Section 2.3 sets out the independent evidence for it.

The same sizing set gives four entries for its two helicopter types, at 5.4 to 7.2, and against them the result is
mixed: this configuration is ahead of the turboshaft single-main-rotor helicopter at every corner,
the two middle entries fall inside its envelope, and only its top corner is ahead of the
all-electric side-by-side helicopter, which has no wing either. The qualifications below apply to them too.

**So the second claim is narrower than the structural statement invites**: carrying cruise lift on a wing is worth roughly an eighth
to a half against the turboshaft reference, and against the all-electric one it ranges from slightly behind to comfortably ahead
depending on the drag outcome and the blade — a measurable advantage, not a change of category. What compresses it is the cruise
efficiency of the fixed-pitch blade: at a propeller efficiency of 0.85 the same airframe reaches 7.47 to 9.20. Whether a
variable-pitch hub would recover that difference is not computed; Section 6.2 reports the gap and declines to attribute all of it to the hub.

### Five qualifications: three run against this configuration, one has no computed direction, and one bounds what the comparison can be called

**Scale.** The compared vehicles are larger than both designs studied here, which are of order 50 kg and 1 000 kg (Supplement S6), and **Reynolds number
favours the larger aircraft**, so the smaller design is at a disadvantage in this comparison rather than an advantage.

**The quadrotor is a good quadrotor**: both quadrotors have unusually low disc loadings. **Nothing here is compared against a poor
example.**

**The speeds are not matched, and the direction of that mismatch is calculable.** The reference is quoted at its best-range speed, this configuration at its cruise condition, 1.49 times stall, rather than at its best point, 1.26. **The reference is therefore given its best speed and this configuration is not given its best speed, and the margin is
positive anyway.** **The best point is not an available option** — cruising there leaves too little margin above the stall — **so this
fixes a direction, not a magnitude.**

**The atmospheres are not matched.** The published sizing mission is flown at *"5,000-ft altitude and ISA + 20°C"*; every number in
this work is at sea level. **The direction of that mismatch is not claimed here**, because it has not been computed.

**The analysis chains are not matched, and this is the qualification that bounds what the comparison can be called.** The published value comes from a fully sized vehicle in an integrated design system; the value here is a converted metric at a prescribed cruise condition, taken before the sizing closure of Section 6.1. So this is a comparison of two
independently produced figures in a common definition, not a controlled numerical reproduction, and nothing in it should be read as
validation of either, or as a completed aircraft-level comparison.

### What is sized, and what is not demonstrated

**Sized.** The drag build-up and its bracket, the lift-to-drag ratio from the drag polar, the propeller efficiency from
blade-element momentum theory at two operating points, and the range that follows from the chain.

**Not demonstrated.** **No part of this has been measured**: there is no wind-tunnel or flight test in this work, and the drag
coefficient is a build-up with a declared bracket. The planform was chosen rather than optimised. **The span efficiency used
throughout this section is the computed value, 0.817, not the assumed 0.85**, from a vortex-lattice solution of the trimmed planform.
And for the methods used here, and for the published comparisons against which they were checked, **the aerodynamic predictions
diverge above roughly ten degrees of incidence**: three methods of three fidelities depart at the same place, the highest of them
against wind-tunnel measurement. That is a statement about these methods on this class of configuration, not about what any method
could achieve; it does not touch the cruise numbers above, which sit at a few degrees, but it bounds what this section may be read to
support, and the transition of Sections 5.1 and 6.1 passes through that band.

### What this half costs

The wing that makes cruise efficient is carried through the vertical phase, where it produces nothing and presents the aircraft's
largest surface to ground wind; the tailless planform constrains the sweep; and the fixed-pitch propeller is why the margin above
sits where it does. Section 6.2 charges the third. The first two are inside Section 6.1's closed numbers but are not separated out as
charges, and the wing's exposure to ground wind is not priced in this work.

**The two halves are now on the table separately. Section 5.1 is where they are combined**, and
the combination is what this paper is for.

## 5. Combining the solutions

### 5.1 The combination

None of the three elements is new. **Each can be found on its own, and some of them
together, in the literature and in hardware** — Section 1 says where. The principle behind the third element — a continuous plant sized for cruise, with the vertical or take-off peak drawn from a store — has been applied in studies of a winged tail-sitter (Section 1) and of a single-aisle airliner reported in 2016 whose turbines are *"sized for efficient operation during"* cruise and assisted by electric motors *"during takeoff and climb."*

**What this paper contributes is the architecture that brings the three elements together; the
condition shows what it satisfies, and the price shows what it costs.** The three elements, taken together, meet the escape condition
of Section 2.2 **in the propulsor that carries the aircraft**, and they meet it with no mechanism
that reorients a propulsor. The assembly is not offered as novel because it is an assembly. It is
offered for what it satisfies, and for what it does not need in order to satisfy it.

**The qualification "in the propulsor that carries the aircraft" is not decoration.** The single nose pair meets all four parts of
the condition. The four tip pairs do not: they are exposed in the cruise flow and cannot be feathered, so they re-open the second
charge. **The instantiation is therefore partial**, the case Section 2.2 lists among the ways to fail, and reporting what the failing
part costs is a substantial share of what Section 6.2 does.

Each element supplies one part of the condition, and none supplies it alone:

- The **blended wing body** carries the cruise lift on a surface.
- The **tail-sitting stance** aligns the thrust axis with the body axis, so one propulsor produces the thrust for vertical operation
  and for cruise, in one orientation relative to the airframe; there is no dedicated lift system, and vertical operation needs no runway.
- The **series-hybrid buffer** releases the continuous plant from the hover peak, so that it is sized by cruise; the series
  arrangement is chosen for the electrical path it gives the buffered peak, not because it is assumed to be the more efficient hybrid.

**The configuration is arranged to change regime by rotating the airframe. The propulsors hold their orientation relative to the body
from take-off to cruise; what changes is the orientation of the body relative to the flight path.** The contemporary hybrids reach the
same end otherwise. The lift-plus-cruise design of the NASA study used in Section 2.3 carries its lifting rotors through cruise, stopped
and aligned with the stream, and flies on a separate pusher; its tilt-wing turns eight proprotors, each on its own motor, on a tilting
wing and tail. Turning the
propulsors is the case the condition excludes; turning the thing they are attached to leaves the orientation requirement intact.
**That single move is what removes the need for the mechanism.** The table counts the mechanism classes that exist in order to change
regime, or to take a rotor out of one regime's flow; the strip of Section 5.2 is a control surface, of a different class, and is named
below. The configuration therefore carries:

| Mechanism | Where it is required | Present here |
|---|---|---|
| Pivot or tilting joint | Tilting architectures | — |
| Nacelle or rotor-group actuator | Tilting architectures | — |
| Variable-pitch hub | Architectures that trim a rotor across two widely separated operating points, or feather a rotor unused in one regime | — |
| Dedicated lift rotors | Lift-plus-cruise architectures | — |
| Rotor stowing, indexing or stopping mechanism | Architectures that remove dedicated lift rotors from the cruise flow by such means | — (see note) |

*Note.* The stopping class is absent if the tip pairs free-wheel in cruise or are held stopped by motor torque; a
brake or a mechanical lock would add it. The means of stopping is not fixed by this study (Section 5.2).

The tip
pairs are sized from the moment requirement, but because the nose pair is sized at thrust equal to weight and no more, they also supply
the whole take-off margin; that dependency is reported in Section 3, and it does not make them a dedicated lift system.

**The claim is narrower than it may appear.** **This is not a configuration in which nothing moves.** Roll cannot come from the
propellers' thrust, since every thrust vector is parallel to the body axis; it could come from their reaction torque, and this
configuration declines that channel by design (Section 5.2), assigning the axis to the only moving aerodynamic surface on the aircraft: a
variable-extension strip on the lower surface, modulated rather than switched, which also pitches the nose down slightly when deployed.
It is named here because a claim about eliminated mechanisms that omitted it would be false. **Nor is this a claim of
mechanical simplicity**: what is offered is a count of the mechanism classes a tilting architecture needs to change regime and this
arrangement does not, and the actuator inventory that replaces them is the propulsion motors together with the strip.

**Whether this aircraft can actually perform the change is a separate question and is not settled anywhere in this paper**: the aerodynamics of the rotation are not predicted reliably here (Sections 4 and 6.1). **The mechanism claim is about hardware and survives that
limit. The transition claim is not made.** Section 8 holds the paper to that.

### 5.2 What it is made of, and what still moves

Section 5.1 claimed that a class of mechanism is absent. A claim of that kind is only as good as the inventory behind it, so the inventory is given here in full, including the parts that move.

#### The airframe

The entire airframe is the wing: there is no cylindrical fuselage, and every part carried also lifts. Leading-edge sweep varies
along the span while the trailing edge is held at 25°, from 45° at the root to 38.3° at the tip. For the 50 kg reference design, which
this inventory describes, the span is 3.453 m, the wing area 1.979 m² and the aspect ratio 6.03. The aircraft is tailless, so the
pitching moment must come from the distribution of lift along the body itself, and sweep is what places the outboard sections behind
the centre of gravity so they can produce it: **the sweep angle and the longitudinal stability are one design variable seen from two
directions.**

#### The propulsion

**Five propeller stations, ten rotors:** every station is a coaxial counter-rotating pair, because of **reaction torque.** A single
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
cancellation is no longer exact (below). In a tilting architecture that term is present and must be designed for.

#### The energy path

A series hybrid: fuel to engine, engine to generator, generator to electric machines at the rotors. The engine is not mechanically connected to any rotor. It is an energy source, and that decoupling is what allows it to be sized by cruise rather than by hover.

**The separation the architecture depends on is that the continuous cruise requirement is several times smaller than the hover peak, and that the difference is supplied from a battery buffer for the vertical phase alone.** No wattage is quoted here; the closed powers are Section 6.1's.

#### What produces each moment

**Pitch and yaw come from differential thrust between the tip pairs** (body axes, as fixed above). The frames project ±0.71 m
from the planform, so an upper–lower differential acts at 0.71 m in pitch and a left–right differential at the semi-span, **1.726 m —
2.43 times the pitch arm**, a consequence of the layout rather than a design choice. The authority each axis has depends also on the
available thrust differential and its allocation. **The same differential-thrust system is what is assigned to rotate the airframe
through transition.** That is a design assignment, not a demonstrated result (Section 5.1): the moment it produces is a sizing input to
Section 6.1, and whether it suffices is **not settled in this paper**.

**Roll comes from neither, and the reason is a choice rather than an impossibility.** No combination of thrust settings produces a
moment about the body axis, and the reaction-torque channel that could (Section 1) is declined: every pair is operated
torque-balanced. Roll comes instead from a strip on the lower surface (its
geometry is in Supplement S8). **Extension is the control variable** — the strip is modulated, not switched — and deploying it also
pitches the nose down by a small increment. Its inboard 46 % lies inside the nose propeller's slipstream, where dynamic pressure is set
by disc loading and is available at zero airspeed, and its outboard 54 % works against the freestream in cruise, which is why one
device serves both regimes. The split is an estimate: the slipstream boundary it rests on is not derived in this work.

#### What meets the ground

The aircraft rests on the five points of Section 3. **The frames carry a fairing, and it is not only a drag measure**: a planar
planform supplies no directional stability, so the fairing is the aircraft's only vertical surface, and sized against the criterion
the tailless literature recommends it needs a chord of **39 mm** at an assumed lateral lift-curve slope of 4.0 per radian (Supplement S8).
Across slopes of 5.0 to 3.0 per radian the chord is 31 to 52 mm, within or below the 50 to 70 mm assumed for a 20 mm faired strut.
Directional stability on this configuration therefore does not ask for a surface; it asks for a fairing on a frame that is already
there. An attitude reference and a flight computer are part of that mechanism rather than optional equipment, because stability is not
airframe-borne alone; they are carried in the systems budget.

#### What moves

The propellers rotate at commanded speed, but none changes its orientation relative to the airframe, or its blade pitch, at any
point in the flight. **Beyond the propellers' rotation, one thing on this aircraft changes its configuration: the strip**, deployable in
two halves — one side alone for roll, both together as a speed brake. The actuator inventory is therefore the propulsion motors plus the
strip's actuation. **How many actuators that is, this study does not fix**; the systems budget carries the actuation without sizing it.

**The tip pairs are the parts that fail the escape condition** (Section 5.1): sized for moments and used for them in both regimes, they
add the take-off margin but were not sized for weight support, and Section 2.2's permitted-cost clause places them outside the first
charge while leaving them in the airstream.

#### What this inventory does not settle

**An untrimmed hover torque, with no trim mechanism identified.** Each pair's torque balance is set exact at the cruise condition,
so a small residual about the propeller axis remains in hover. That is the axis the configuration chose not to command with the
propellers: the tip pairs cannot absorb it by thrust differential, and the strip has slipstream over only part of its length at zero
airspeed. What is left is the speed trim of the pairs, a reaction-torque command. Either the residual is small enough to be absorbed
that way, which this study has not shown and which would mean the architecture spends a little of the channel it declined, or another
duty falls on the strip.

**The fixed geometry of the tip pairs leaves two admissible cruise states**: turning at zero shaft torque, or stopped. This
configuration uses the first: free-wheeling at zero shaft torque is the tip pairs' uncommanded cruise state and the drag state Section 6.2 charges; the shaft power of commanded departures from it, for attitude moments in cruise, is not computed. **The free-wheeling
state is physically determinate: the rotor settles where net shaft torque is zero. The stopped state is not**: the stop must be
produced by something — motor holding torque, an electrical brake, a mechanical lock — and a stopped fixed-pitch blade also has an
azimuth, so the stopped-state drag estimates (Supplement S11) should be read as estimates for an assumed azimuth rather than as the
state a particular installation would reach. If the stop were a brake or a lock rather than motor holding torque, the count of Section 5.1
would gain a class.

## 6. The calculations

### 6.1 Analytical closure of the sizing loop

This section prices the arrangement of Sections 5.1 and 5.2 on a declared package; it does not bear on the count of mechanism classes, which rests on the inventory of those sections alone. **Closing a sizing loop mathematically is not the same thing as closing an aircraft physically.** This section does the first: what it produces is a set of consistent numbers on a declared set of assumptions.

Take-off mass sets the cruise power, cruise power the engine rating, engine rating the propulsion mass, and propulsion mass the take-off mass; the take-off mass is found by iteration as the fixed point of that loop (Supplement S10).

#### The inputs, and why there are four closures rather than one

**The zero-lift drag coefficient is uncertainty:** the build-up of Section 6.2 places it between 0.0285 and 0.0381, and a designer
does not choose where the real aircraft falls. **The blade family is a design variable this study has not fixed:** four nose-blade
families that meet the hover figure of merit span cruise propeller efficiencies of 0.632 to 0.683.

**These are the same configuration at four closed masses
rather than four configurations**, with anything that depends on the control moment arms carried at the reference geometry of Section 5.2. Run on the reference
design's own assumed inputs, the same construction reproduces that design within 1.5 percent (Supplement S10), so the closures report
a change of inputs, not of method.

#### The four closures

**On these assumptions all four converge**, for the 50 kg design — the only one carried through this loop.

| | C_D0 | η_p | L/D | L/De | MTOW | Empty fraction | Hover power, rotor shaft | Engine rating, shaft | Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** | 0.0381 | 0.632 | 8.79 | 5.56 | 57.5 kg | 0.614 | 12.53 kW | 5.17 kW | 927 km |
| **B** | 0.0381 | 0.683 | 8.79 | 6.00 | 55.8 kg | 0.607 | 12.17 kW | 4.65 kW | 1 002 km |
| **C** | 0.0285 | 0.632 | 10.82 | 6.84 | 53.5 kg | 0.597 | 11.66 kW | 3.91 kW | 1 141 km |
| **D** | 0.0285 | 0.683 | 10.82 | 7.39 | 52.3 kg | 0.592 | 11.40 kW | 3.54 kW | 1 233 km |

*L/De = L/D × η_p at the cruise condition; the loop holds both factors fixed within each closure. The four L/De values are the bounding corners of that product, carried into the closures as inputs, not four
simulated aircraft.*

Payload is fixed at 13 kg and take-off mass is the output. **The blade that is best before the loop is still best after it** — **a result of the closure rather than an assumption carried into it.**

#### The transition

The sizing above says nothing about whether the aircraft can change regime. **The question is asked in two models, only the
second of which carries rotational dynamics, and that one does not support a zero altitude loss.** Both use the reference designs at
their reference masses and assumed drag, not the closures. A point-mass model with the body angle driven kinematically loses no
altitude in a rotation entered in a 5 m s⁻¹ climb. Solved with rotational dynamics and a finite control moment, **and with the aerodynamic pitching moment set to exactly
zero, so that nothing favourable is borrowed**, the 50 kg design **loses 5.4 to 6.6 m at the same reference condition**; the loss is
not an artefact of the controller (Supplement S10). **What the kinematic model leaves out is not the difficulty of turning the aircraft
but the trajectory the aircraft flies while it is being turned.** **So the zero-altitude-loss result is a property of the model that
produced it.**

A prediction would need the aerodynamic pitching moment, and the methods used here diverge in the band the rotation passes through
(Section 4); with a borrowed moment some models complete the rotation, some saturate the tip pairs, and some tumble. **That spread is
itself the finding.**
Whether a real aircraft loses 5.4 to 6.6 m, more, or less is not settled by anything here.

#### What closing does and does not establish

It establishes that the architecture is arithmetically self-consistent on a declared package, at four corners of that package. **It does not establish that the package exists.** The energy store this closure assumes is the item Section 7 examines, and the examination does not end well. These ranges are carried forward as closed-loop values, not as a ranking: no rotorcraft is sized in this work, so no range comparison is made against one (Section 4 compares cruise efficiency), and the comparison with the other hybrids depends on the sizing contract (Section 6.4).

### 6.2 The ledger

This section says where each charge of Section 2.1 appears inside the closed numbers of Section 6.1, and how large it is there.
**It attributes. It does not add.** **And there is no single figure for what the architecture costs**: the charges are in three currencies, and **no
scalar aggregate is defined, because this study has no defensible weighting between them** (Section 6.4).

#### Bill 2 — the drag of hover hardware, inside the bracket

In the drag build-up behind the bracket (line items in Supplement S11), **the hardware exposed by the vertical-phase layout — the
tip frames and the free-wheeling tip-pair rotors — is 69 percent of the zero-lift drag at the favourable end and 57 percent at the
adverse one**; the rotor term alone is 0.0154 at the favourable end. **The rotor line rests on section drag at low Reynolds number**,
on section polars computed rather than measured (Section 6.3). **The tip-frame term is an attribution, not a marginal removal cost**: it
is not a claim that this drag would disappear if the vertical phase did. **No stopped-state counterfactual was computed**: the eight
tip discs stopped edge-on are estimated at ΔC_D0 = 0.0008 (Supplement S11), but that takes an indexing mechanism, a class Section 5.1
counts, which has not been sized, charged or closed.

**Rotor–structure and rotor–wing interference is not modelled and is not carried as a line.** Section 2.1 quotes a wind-tunnel finding
that a simulation neglecting it predicted higher lift and lower drag than were measured; this build-up is such a calculation, and the bracket's
upper margin is the only provision made for it.

#### The cruise-efficiency gap under fixed pitch

Section 6.1's closures run at a cruise propeller efficiency of 0.632 to 0.683: **relative to the 0.80 the reference design's sizing assumed, 14.6 percent lower at the better blade and 21.0 percent lower at the worse.** **The ledger does not attribute the whole of that gap to the absence of variable pitch.** **No variable-pitch counterfactual was computed.** Nor is the gap decomposed.

#### Bill 1 — carried mass, and what it is on this configuration

**There is no dedicated lift group to charge.** What Bill 1 becomes here is the energy buffer: **3.6 percent of take-off mass, 1.9 to 2.1 kg across the four closures.** The buffer is not lift-subsystem mass, so it is not Bill 1 as Section 2.1 defines it, but it is carried for the whole flight to serve a demand that lasts about two percent of it: **the architecture converts a power-system charge into a cost in kilograms**, as Section 2.2 said in advance it would.

**The buffer fraction is an input to the loop, not a result of it.** The deficit per kilogram of take-off mass that the buffer covers, taken at the electrical bus, spreads by 12 percent across the four closures while the fraction is held at 3.6 percent (Supplement S11). **The corner that needs the most buffer per kilogram is given the smallest buffer**, and that is a declared assumption of the closure rather than an outcome of it.

#### Bill 3 — released from the engine, and not from the electrical path

The engine is sized by cruise, **3.54 to 5.17 kW** of shaft rating, against a hover requirement of **11.4 to 12.5 kW** at the rotor shaft: a ratio of installed hardware of **2.4 to 3.2**, which is not the buffer's burden (Section 7 computes that). **But the full hover power passes through the electrical path, and that path is sized by it.** **Bill 3 is removed from the engine and left standing on the electrical system** (the propulsion-mass split is in Supplement S11). The sizing loop computes no hover-rated mass for the electrical path.

#### What the closure does not contain

Section 6.1's convergence does not cover the cost of declining the reaction-torque channel, the sizing of the strip's actuation, the allocation of the take-off margin against attitude authority, the landing transition, the vortex ring state, closed-loop attitude control in hover and in cruise, engine installation, or rotor–structure and rotor–wing interference; **none of these is a ledger entry, and Supplement S14 lists them.** **The first and the last are the two that would most change the numbers above if they were computed.**

### 6.3 Scale does not lock two of the charges together; the third is not tested

Section 6.2 decomposed the three charges on one aircraft, at one size; **this section asks whether they are three quantities or
one quantity under three names**, by changing the size of the aircraft and seeing whether they move together. **The test is deliberately weak**: it can show that two charges are not locked together within this
model; **it cannot show that they are independent in general.**

**The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 6.1's closures** (Supplement S12).

**Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its light-design value in the section
polars used here, while the Bill 3 ratio changes by 5 to 14 percent.** **Within this model, the two are therefore
not one quantity under two names.**

Within the
blade-element and section-polar model the section Reynolds number accounts for the fall, a decomposition inside the model rather than
a causal claim beyond it, and the light end lies below a Reynolds number of 10⁵, where section drag is hardest to predict. **Of the two
rotor terms, the light one is therefore the less certain — and it is the one Sections 6.1 and 6.2 carry.**

**Bill 1 is not tested.** It appears here as the energy buffer, 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and both figures are inputs (Supplement S12). Whether it is separable from Bill 3 here is not established;
that the two are coupled here is Section 2.2's claim, and coupling is not identity.

**The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low
Reynolds number.** **It is consistent with the separability Section 2.1 asserts; it is not a verification of separability as a general
property.**

**Because at least two of the charges are not locked together, a comparison of architectures cannot in general be reduced to a number
that does not depend on how the charges are weighed.** Section 6.4 examines what the choice of sizing contract does to a ranking, on the
light closures of Section 6.1 only.

### 6.4 Rankings belong to contracts

Where one architecture pays less of one charge and more of another, the ranking depends on how the charges are weighed
(Section 6.3), and **a sizing contract is one such weighing**: it fixes what is held equal between the architectures being compared.
This section applies three contracts to three architectures at each of the four closures of Section 6.1. **The mechanism claim is not a
ranking and is not at stake here.**

#### Three contracts, and what each holds equal

Range in the sizing loop is proportional to L/D, to the energy chain and to the fuel fraction, and the three contracts differ
only in the last (Supplement S13): a **fixed fuel fraction**, sixteen percent of each architecture's own take-off mass; a **fixed fuel
mass**, the 8.4 to 9.2 kg this configuration carries; and a **fixed take-off mass and payload**, under which every kilogram of
architecture-specific hardware is a kilogram of fuel not carried. **These are three different questions, not three estimates of one
answer**, and this paper has no mission that would decide among them.

#### What is compared, and on what basis

Three architectures fly the same mission, 13 kg of payload at 30 m s⁻¹, with the same wing loading, disc loading and aspect ratio,
the same airframe and avionics fractions, and the same energy chain apart from the propeller. **The competitors are therefore this
planform with two add-ons, not independently designed aircraft of their families.** All three carry the same buffered series-hybrid
power system, so Bill 3 is held common and the comparison measures mass and cruise drag. **Holding Bill 3 common is a choice of
question, and it has a direction.** **The choice runs against this configuration**: without the buffer, and with engines rated to the
hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off mass (Supplement S13).

The basis is not symmetric. The lift-plus-cruise layout carries a lift-to-drag ratio transferred from a different airframe's
wind-tunnel campaign (Section 2.1), and its stopped lift rotors take an indexing mechanism (Section 5.1) whose mass is not charged. **The
tilting layout carries no cruise drag penalty at all. That is an idealisation in its favour**, and it makes the tilting layout a bound.
Both competitors are given a propeller efficiency of 0.80, assumed, against this configuration's computed 0.632 and 0.683, and a lift
group of 10 percent or a tilt mechanism of 5 percent of take-off mass. **Neither figure is measured.**

#### Against lift-plus-cruise: a trade, and the contract sets the exchange rate

**The two architectures trade one charge against another**: closed under a fixed fuel fraction, this configuration is 27 to 30 percent lighter, and the lift-plus-cruise layout cruises at a lift-to-drag ratio of 11.66 and 15.72 against 8.79 and 10.82, with a propeller at 0.80.

**The lift-plus-cruise layout is 55 to 84 percent ahead under the first contract, 28 to 54 percent under the second, and between 13 percent short and 7 percent ahead under the third; the shift from first to third is 67 to 77 percentage points at every closure**, at the declared lift-group fraction, and always toward the lighter aircraft. The per-closure numbers are in Supplement S13. **The sign itself changes inside the envelope under the third contract**: this configuration is ahead at the two closures with the higher-efficiency blade family and behind at the two with the lower. **A statement of which architecture has the longer range, made without its contract, would therefore be a statement about the contract.**

#### Against the tilting layout: a bound, not a ranking

**What the bound gives is a size, not an order.** Credited with no cruise penalty, the tilting layout is 93 to 141 percent ahead of this configuration under every contract at every closure; that margin is the room a real tilting aircraft's cruise penalties — nacelle drag, pivot fairing, hover-sized rotors flown as cruise propellers — would have to fill, and how much of it they fill is not computed. **A ranking against a competitor modelled as a bound is not a ranking, and no range claim is made against the tilting family in either direction.**

#### Section 2.1's prediction, tested

Section 2.1 predicted that such a ranking will move when the sizing rule changes, and can reverse. **The movement holds
everywhere**, against both competitors, toward the lighter arrangement as the contract weights mass more; **the reversal holds at two of
the four closures against lift-plus-cruise, and at none against the tilt bound.** Where it falls is decided by quantities this study
has not measured or fixed: the blade family in the base case, and across the sensitivity cases the competitor's lift-group mass and the
propeller basis (Supplement S13). **Which architecture ranks first under a fixed take-off mass is therefore decided, in this model,
by quantities this study assumes for the competitor rather than measures: its lift-group mass fraction and its propeller efficiency.**
What is robust is that the shift exists and runs toward the lighter aircraft.

#### What the framework asks of whoever uses it

**Each comparison states every charge in its own currency before any aggregate, names its contract, and states its asymmetries and their directions; an ordering is reported only with the contract it was computed under and, where its sign depends on an unmeasured quantity, with that quantity named.** This paper meets that for its own column (Section 6.2) and not for the competitors', whose kilograms and drag counts here are parameters and transferred ratios rather than an audit.

#### What this section does not establish

**The competitors are modelled at a coarser level than this configuration**: their drag is transferred or idealised, their propeller efficiency assumed and their architecture-specific mass a parameter. **Comparing computed figures against assumed ones favours whichever is assumed more optimistically** — in propeller efficiency both competitors, and with a common propeller efficiency the lift-plus-cruise lead under the first contract falls from 55–84 to 33–45 percent (Supplement S13); in drag the tilting layout, by assumption. **The comparison is at one size**: Section 6.3's 1 000 kg reference design has no closure, and none of its figures is used here. **And nothing here ranks architectures for a mission.** What this section establishes is narrower: **the same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property of the architectures alone.

## 7. What does not close

Section 6.1 closed the sizing loop on a declared package and said that whether an aircraft can be built to it is a different question. **This section is where that question is answered, and for the first item the answer is no: the required store performance is not demonstrated by the sources consulted here.** It is stated in that order — first the obstacle that is known, then what is not known.

### First, the known obstacle: the energy store

**Every closure in Section 6.1 carries a buffer of 3.6 percent of take-off mass.** Taken at the
electrical bus, **the four closures ask the buffer for 4.7 to 5.2 kW per kilogram of buffer to hover, and 5.5 to 6.1 kW per kilogram of
buffer to leave the ground** with the tip pairs at full thrust (Section 3).

**What has been measured is a fraction of that, and the store figures available are of four different kinds.** A pack flown in a 210 kg-class electric VTOL aircraft is rated, as a flown system, at 0.892 kW per kilogram continuous; its
unit pack, discharged on the bench at its highest tested rate, delivered on average about 1.5 kW per kilogram (Supplement S14). A
NASA-funded design study adopts 4 kW per kilogram and describes that figure as about twice that of existing batteries. The same study
notes lithium-polymer figures in the literature as high as 3 kW per kilogram, which it cites rather than measures; against that figure
the take-off demand is 1.8 to 2.0 times. The study argues that, because pulse current limits can exceed continuous ones — by more than a
factor of two in one commercial module it cites — a pack with the required specific power may be possible with existing technology; its
hover lasts twenty seconds or less, while this aircraft's vertical phases occupy about a minute in all (Section 2.1), and how long each
draws the peak is not computed here.

**The take-off demand is 3.7 to 4.1 times the bench rate — the highest figure obtained from a measurement — and 6.2 to 6.8 times the
flown system's continuous rating.** The comparison is between unlike ratings. **The gap is real on every one of them;
the factor quoted is peak demand against bench average.** The package Section 6.1 closes on does not exist with any store the sources
consulted here report as built; closed again at the bench rate, it becomes 76 to 81 percent heavier, a sensitivity with one input
changed rather than a structural closure (Supplement S14).

**This is where the coupling Section 2.2 names is paid**: the buffer converts kilowatts of hover peak into kilograms of store. **The
escape from Bill 3 is real in the sense Section 2.2 defined it, and its price depends on a component whose required performance has not
been demonstrated.**

### What the obstacle reaches, and what it does not

**It reaches every number that describes this aircraft at Section 6.1's masses**: the closed masses of 52.3 to 57.5 kg and the 13 kg payload assume the store. The ranges of 927 to 1 233 km survive the re-closure only because the fuel fraction is held, on an aircraft three-quarters heavier; they do not survive as 13 kg carried that far on a store that has been built. The vertical phase that Section 3 reports as sized was sized with this store in it, and Section 6.4's orderings were computed with the store held common at 3.6 percent; how they would move with a measured store is not computed.

**It does not reach the mechanism claim.** That is a statement about hardware, and a heavier store adds no pivot. **Nor does it reach the cruise-efficiency comparison of Section 4 as a ratio**: effective lift-to-drag ratio has no mass in it. As a comparison of aircraft, that section describes the configuration at Section 6.1's masses, which the store does reach.

### Then what is not known

Eighteen further questions are open, and Supplement S14 lists each with what it bears on and what would settle it.

**None of these is a small correction to a known quantity.** Two of them need validated data rather than more of the computation already done: the transition moment, because three methods have been tried against it and disagree, and the low-Reynolds section drag, because the one method used here is least reliable exactly there.

### What this section amounts to

**The loop closes; the aircraft is not shown to.** At the energy store the paper can name the gap exactly, in specific power and in take-off mass; everywhere else it can name only what would settle the question. **The architecture claim — that the configuration is arranged to change regime with no mechanism that reorients a propulsor — is a count of hardware, and nothing in this section reaches it.** What this section reaches is the aircraft, and the paper has not claimed the aircraft. The last section returns to the four axes and states what is claimed on each.

## 8. Four axes, and where the paper stops

This section states the boundary of the paper's claims.

**It is not a list of the study's open questions.** Those are in Section 7, and the difference matters: the boundary below is about claims the paper **declines to make**, most of which it could not make on any evidence; Section 7 is about questions the paper **does not answer**, and which better evidence would answer. One is a scope; the other is a debt.

### The claims are made on four axes, against four different opponents

Comparison is only meaningful against a named alternative, and this paper's alternatives differ from axis to axis.

| Axis | Opponent | Status |
|---|---|---|
| Cruise efficiency | Rotorcraft: multirotors and helicopters | **Claimed against multirotors, and bounded; against helicopters the comparison with published figures is mixed and no advantage is claimed.** Cruise lift is carried on a surface rather than on rotors, which no sizing contract changes. The *size* of the resulting advantage is a calculation, not a consequence of that fact: positive throughout against one published quadrotor, and from slightly behind to comfortably ahead against the other (Section 4). |
| Operation without a runway | Fixed-wing aircraft | **Claimed as sized, not demonstrated** (Sections 3, 7). The vertical phase was sized with an energy store whose required performance the sources consulted here do not report as built. |
| The mechanism required to change regime | Tilting architectures | **Claimed.** This is the paper's contribution — a count of mechanism classes (Section 5.1), not a claim of mechanical simplicity or reliability. |
| Cruise efficiency and range | Other hybrids — lift-plus-cruise, tilt | **Not claimed, in either direction.** |

**The fourth row is the important one**, and the reason it is a refusal rather than a result is the paper's own finding in Section 6.4. Against lift-plus-cruise the ordering depends on the sizing contract: across the three contracts it moves substantially, and under one of them its sign changes inside the envelope and turns on quantities of the competitor that are assumed rather than measured. A paper that quoted one of those orderings as a result would be reporting its own choice of contract. Against the tilting family the competitor can be modelled here only as a bound that pays no cruise penalty, and an ordering against a bound is not a result. **No range claim is made against the tilting or lift-plus-cruise families in either direction**, and a reader who finds one implied anywhere in this paper should treat it as an error rather than as a claim.

### What each claim does not depend on

**Operation without a runway** does not depend on the drag bracket, the propeller efficiency or the transition aerodynamics — **but it does depend on the energy store**: the vertical phase is sized with one, and Section 7 examines whether it exists. **Cruise lift carried on a surface** does not depend on the sizing contract or the transition aerodynamics. The **size** of the cruise-efficiency margin depends on both the drag bracket and the blade family, and Section 4 reports it as a range rather than a number. **Elimination of the propulsor-reorientation mechanism class** does not depend on the drag bracket, the propeller efficiency, the sizing contract, the range result or the energy store — **nor on the transition aerodynamics**.

The mechanism claim is a statement about what hardware is present, and it is settled by the inventory of Sections 5.1 and 5.2. **The separate claim that this aircraft can actually perform the regime change is not settled** (Section 5.1).

### One cost of the contribution that is named and not priced

The mechanism claim has a price this work does not compute. **This configuration declines the reaction-torque channel that comparable aircraft use for roll (Section 5.2). What that refusal costs — in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia — is not computed anywhere in this paper.** The claim is that the mechanism class is eliminated. **Whether eliminating it is favourable on balance is a question this work does not settle**, and quantifying it would require a control-allocation study rather than a single torque figure.

### Eight things this paper does not claim

**1. It does not claim range against fixed-wing aircraft.**

**2. It does not claim vertical capability against rotorcraft.** That comparison runs the other way.

**3. It does not claim that the aircraft has no moving parts.** What is eliminated is a *class of mechanism* — the one that reorients a propulsor. The aircraft has a moving aerodynamic surface, it is named where the elimination is claimed rather than later, and it also pitches the nose down when deployed.

**4. It does not claim mechanical simplicity.** Part count, assembly mass, failure modes and maintenance burden were not measured, and nothing here supports a statement about reliability. The count of mechanism classes in Section 5.1 is not a reliability argument.

**5. It does not claim that the escape condition is fully instantiated.** The condition is met in the propulsor that carries the aircraft and is not met in the attitude system, which is carried through cruise producing moments rather than cruise thrust. Section 2.2 names that case as partial instantiation, and the charge it re-opens is reported rather than absorbed.

**6. It does not claim that satisfying the condition makes an aircraft better.** The condition concerns three specific charges. A configuration may avoid all three and still be unbuildable, uncontrollable, or unsuited to its mission, and the accounting says nothing against that possibility.

**7. It does not claim that the trades inside the escape are favourable.** Moving the hover peak onto a store converts a power-system charge into a cost in kilograms; serving two regimes with one set of fixed-geometry propellers costs efficiency in at least one of them. Both are computed, neither is asserted to be worth paying, and the ledger reports them whichever way they fall.

**8. It does not claim that the aircraft flies.** The design *sizes* vertical operation and the transition; it does not demonstrate either. No aircraft has been built, no wind tunnel has been run on this geometry, and the transition analysis is a calculation whose assumptions are stated where it appears.

### What the claims that remain amount to

Section 7 and Supplement S14 list what the paper leaves open. What the paper offers is **a configuration sized to combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism that reorients a propulsor, and an account of what the combination costs.**

Each half of that has a named opponent and neither half is a record. **Nor is the configuration claimed to be without precedent**: Section 1 sets out what is already established, including uncrewed tail-sitters, tail-sitters without control surfaces, coaxial contra-rotating tail-sitter propulsion, and blended-wing-body tail-sitters. **The contribution is the architecture, and the paper presents it as the combination, the consequences of the choices inside it, and the accounting** — which is what Sections 5.1 and 5.2 describe and what Section 6.2 prices.

The configuration is arranged to change regime by rotating the airframe rather than the propulsors, and so carries none of the mechanism classes Section 5.1 counts: no pivot, no nacelle or rotor-group actuator, no variable-pitch hub, no dedicated lift rotors, and — while the tip pairs free-wheel or are held by motor torque — no rotor stowing, indexing or stopping mechanism (Section 5.1's note). **This is a count of mechanism classes, not a claim that nothing moves, and not a claim of mechanical simplicity or reliability.** Whether this aircraft completes the rotation is a separate question, and it is not settled here.

---

# Part 2. The journal supplement (draft so far)

### S2. The charges: working for Section 2.1

#### The power ratio


Taking hover power from momentum theory and cruise power from the drag polar,

    P_hover / W  = √(DL / 2ρ) / η_h                 (DL = W/A, disc loading)
    P_cruise / W = V / ((L/D) η_p)

so that

    P_hover / P_cruise = √(DL / 2ρ) · (L/D) / V · (η_p / η_h)

A vehicle with a disc loading of 100 N m⁻², a cruise lift-to-drag ratio of 15 and a cruise speed of 30 m s⁻¹ needs between three and four times as much power to hover as to cruise: the geometric terms alone give 3.2, and the efficiency ratio η_p/η_h carries it to about four when the cruise propeller is roughly a quarter more efficient than the hover rotor.

#### The transfer with direct experimental support


In the doctoral study whose wind-tunnel campaign Section 2.1 quotes [14], and in that document rather than in the journal article by the same author, which reports a different comparison, a retraction system removed thirty percent of the airframe's drag; the same work then costed it. Applied to a passenger eVTOL, with the mechanism assessed at five percent of vehicle mass and deducted from the battery mass, maximum range rose from 119 km to 121 km: a two-kilometre gain for a five-percent mass penalty. The same work finds the retraction's advantage elsewhere (the speed that maximises range rose by 5 m/s), which is a performance this accounting does not price. Bill 2 was converted almost exactly into Bill 1, and the transfer is the point rather than the small residue.

#### The tilting row


What a tilting architecture buys its unified propulsion group with is a mechanism: a pivot, an actuator, the gyroscopic coupling of a reorienting mass, and a control problem through the turn. The pivot and the actuator are paid in kilograms, although they are not lift-subsystem mass; the coupling and the control problem are paid in none of the three.

The two clarifications of Section 2.1 apply to it as follows. "No worse" is judged against the architecture the move modifies. A charge that architecture already paid, left no larger, is no worse. A charge it did not pay, imposed by the move, is worse; so is one it paid, enlarged by it. A remedy whose cost falls outside the three charges does not refute the accounting, but it is not thereby exempt from being counted. A framework that could absorb any cost by declaring it out-of-scope would be unfalsifiable, so the costs outside the three are listed, not waved away.

The tilting row needs both clarifications. If the architecture it modifies supplies its hover peak from a store, tilting without one imposes Bill 3 and the row is a transfer between charges. If that architecture already sizes its continuous plant by the hover peak, tilting leaves Bill 3 no worse; then, where the mechanism's kilograms are fewer than those of the lift group it removes, what keeps the row from refuting the accounting is the part of its cost that falls outside the three, which is why that part is listed.

### S3. The condition: working for Section 2.2

#### What each departure costs


| Departure | What it costs |
|---|---|
| Different hardware | Bills 1 and 2. The unused set is carried for the whole flight and, if exposed, drags. |
| Same hardware, but it serves only one duty | Bills 1 and 2 again. A propulsor that lifts and is then carried is a dedicated lift group under another name, whatever it shares with the cruise system. |
| Same hardware, both duties, different orientation | The tilting family. Bill 3 is incurred unless a store supplies the hover peak, and the mechanism that changes the orientation adds mass and introduces a control problem through the turn. |
| Same hardware, both duties, one orientation, different sizing point | Bill 3, unless the hover peak is supplied from somewhere other than the continuously installed power. |

The second departure is stated separately because it does real work later: a propulsor that produces a little thrust in cruise is not thereby serving both duties, and the distinction decides which parts of a configuration meet the condition and which do not.

#### The six permitted costs


1) **A store.** It has the same duty-cycle character as Bill 1. The fourth part moves the hover peak off the continuous power plant and onto a store; that store delivers its peak for two percent of the flight and is carried for the rest. It is not Bill 1 as Section 2.1 defines it (it is not lift-subsystem mass), but it is mass carried for a duty that is briefly needed, which is the same complaint Bill 1 makes. The condition converts a power-system charge into a cost in kilograms and claims only that the three charges as named are not incurred. It does not claim the trade is favourable. Whether the store is lighter than the continuous power it displaces is a sizing result and is computed, not asserted.

2) **The electrical path.** The fourth part frees the continuous power plant from the hover peak. Everything between the store and the rotors (machines, power electronics, wiring) still passes the full hover power and is still sized by it. That is Bill 3 on the electrical path, and the condition does not remove it; it is carried in the ledger rather than in this definition.

3) **Rotating the airframe.** The condition refuses architectures that reorient a propulsor, and sets that refusal against the mechanism a tilt requires. An architecture that instead rotates its whole body faces the same physical problem: a ninety-degree change of the thrust axis relative to the flight path, with the moments, the authority and the control through the turn that implies. It is not one of the three charges and the condition does not eliminate it; Section 6.1 analyses the transition without pricing it. Saying otherwise would let a candidate win that line by wording.

4) **Hardware installed for the vertical phase that serves both duties.** The second departure is what carries the weight of this permission.

5) **Hardware used in both regimes for something other than propulsive thrust.** Cruise thrust in this paper means the thrust that balances cruise drag. Attitude devices produce no cruise thrust in that sense; they are used throughout the flight, so their duty cycle matches their presence and they fall outside Bill 1. They remain in the airstream, so the second charge reaches them. Attitude hardware does not stop the propulsor that carries the aircraft from meeting the condition, but it is carried through cruise without producing cruise thrust, which is the first failure mode of Section 2.2, and the charges are about everything the aircraft carries, so Bill 2 reaches it. An architecture in that position is a partial instantiation, the fourth failure mode: it meets the condition where it carries the aircraft and still pays one of the three elsewhere. The fourth failure mode is not a technicality. An architecture may meet the condition where it carries the aircraft and fail it elsewhere, and a paper that reported only the first half would be reporting the condition rather than the aircraft.

6) **The price of serving two regimes with one set of hardware.** Hardware that is not duplicated cannot be optimised twice: a propeller sized for hover thrust at zero forward speed is not the propeller a cruise design would choose, and if its geometry is fixed the compromise is paid in efficiency. The condition permits that cost and does not measure it. Section 6.2 does.

### S4. The independent check: working for Section 2.3

#### The published designs used


| Configuration (NASA sizing set [16]) | Effective L/D | Design gross weight | Dedicated lift group |
|---|---:|---:|---|
| Turboshaft quadrotor | 4.9 | 3 678 lb | none; the rotors serve both regimes |
| Turbo-electric lift-plus-cruise | 8.5 | 7 271 lb | yes: eight lift motors and a cruise motor |
| Turbo-electric tilt-wing | 8.6 | 6 584 lb | none: eight proprotors, reoriented |

#### Why the second half of the prediction is not derived


Section 2.1 predicts the charge and the amplification; it does not prove that the credit must lose. A dedicated lift system raises the empty-mass fraction and may lower the energy fraction at the same time, and which wins is a closure result rather than a consequence of the accounting. If some data set showed the credit covering the charge, Bill 1 would not be refuted: the mass would still have been paid. What would be refuted is the expectation that the amplified charge outweighs the linear credit. A long enough mission is where the credit is most likely to cover the charge, and the mission of Section 2.3 is short. The counter-set is therefore a common-mission sizing study at longer range in which a dedicated-lift configuration is both more efficient and no heavier than one without. None is known to the authors.

#### The weight breakdown


Of the empty-weight difference of 679 lb, structure accounts for 716 lb in the lift-plus-cruise entry's disfavour, propulsion returns 146 lb of it because the tilt-wing's mechanism is heavier, and battery adds a further 10 lb. Those three categories account for 580 lb of the 679; the remaining 99 lb lies in empty-weight categories the published table does not break out, and this work does not know how it is distributed. What the three reported categories do show is the transfer property of Section 2.1 (the mechanism giving part of the structural saving back), visible inside a weight breakdown this work did not produce.

#### The source's own statement


And the source states the second half of the prediction in its own words, on a comparison the check does not use as its test. Discussing why the all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery weight compared with a quadrotor, *"but not enough to counter the increase in structure and propulsion weight."*

#### The quadrotor contrast


The quadrotor is reported for scale, and the isolation test of Section 2.3 is what carries the prediction. Against it the lift-plus-cruise configuration is about three-quarters better in cruise efficiency (a factor of 1.73) and nearly twice as heavy, a factor of 1.98. The efficiency credit is exactly what the accounting says a dedicated lift system buys, and the weight charge is exactly what it says the buyer pays: the charge survives the credit. But that contrast changes three things at once (dedicated lift group, powertrain, and whether a cruise wing exists at all), so it supports a weaker proposition than the prediction as stated: that adding a wing and a lift group together still costs mass.

### S5. The landing transition: working for Section 3


The forward rotation and the reverse are not symmetric and must not be assumed to be. Going out, the rotation builds dynamic pressure while it turns, so lift arrives to replace the vertical component of thrust as that component falls. Coming back, the race runs backwards: dynamic pressure is falling while the aircraft is being turned, so lift is leaving at the moment the thrust vector has not yet returned to vertical. A model built for the first case cannot be read for the second by changing a sign, and no figure in this paper describes the second.

### S6. The cruise-efficiency comparison: working for Section 4

#### The blade families


The four nose-blade families are two and three blades per rotor, each designed at two target section lift coefficients, 0.55 and 0.70, and each solved at its hover and its cruise condition by blade-element momentum theory. Their cruise propeller efficiencies are 0.648 and 0.683 with two blades and 0.632 and 0.643 with three, at the lower and the higher section lift coefficient respectively. Whether 0.683 is the blade a designer would actually choose is not settled here. It is the best of the four on cruise efficiency under the hover figure-of-merit constraint. Blade count and section loading also govern structural loads, acoustics, the motor operating point, rotor inertia and manufacture, and none of those is modelled in this work. Section 6.1 is where one blade is carried into a closed sizing loop.

#### The compared vehicles


The compared vehicles are 1 660 to 3 275 kg: the six rotorcraft entries of the NASA sizing set [16] have design gross weights from 3 665 lb (the turboshaft side-by-side helicopter) to 7 221 lb (the all-electric quadrotor). The designs here are of order 50 kg and 1 000 kg, and Section 6.1 closes the 50 kg design between 52.3 and 57.5 kg across its four closures.

### S8. The strip and the fairing: working for Section 5.2

#### The strip's geometry


The reaction-torque channel is declined: every pair is operated torque-balanced, so no reaction torque is spent on control. What declining it costs is not counted in this work. The strip lies on the lower surface, inclined at 45° in planform, and runs outboard from the centreline over a spanwise extent of 120 percent of the root chord (1.164 m against a root chord of 0.97 m), so that it reaches 67 percent of the 1.726 m semi-span. Fully extended it stands 2 cm proud of the surface at its inboard end and 6 cm at its outboard end; extension scales that height.

#### The fairing chord


The planform alone supplies no directional stability: a vortex-lattice solution of the planform without the frames returns a directional-stability derivative of zero, as a planar surface with nothing standing out of its plane should. The fairing on the tip frames therefore supplies all of it. The criterion is the value recommended for conventional airplanes, which the tailless literature applies to tailless ones: a directional-stability parameter *"usually greater than 0.001 per degree"* [24], 0.0573 per radian. With the frames' mid-chord 0.879 m aft of the centre of gravity, the side area required is C_nβ S b/(a_f l_f), where S and b are the reference area and span, l_f the arm and a_f the lateral lift-curve slope of the faired frame. Taken over the combined frame length of 2.84 m (two frames, each projecting 0.71 m on both sides of the planform), that area is a chord of 39 mm at an assumed a_f of 4.0 per radian, and 52 mm and 31 mm at 3.0 and 5.0. A 20 mm thick faired strut is taken to have a chord of 50 to 70 mm, a fineness ratio of 2.5 to 3.5 assumed here rather than sourced. The same report qualifies the criterion in two ways. Models were flown in the Langley free-flight tunnel with one-third of that value, though the best flying qualities came above it; and when fins stand at the wing tips, the moment arm of their drag is half the span, so that *"the drag characteristics as well as the lift characteristics of the tip fins exert an influence on the directional stability"* [24]. The chord derived here counts the frames' side force only.

### S10. The sizing loop and the transition: working for Section 6.1

#### The loop


The closure statement is

    MTOW = m_payload / (1 − f_empty − f_fuel)

with the fuel fraction fixed at 0.16. The empty fraction contains a propulsion term, f_prop = 0.108 + P_engine / (p_s · MTOW), in which the engine rating P_engine is 1.53 times the cruise electrical power at the take-off mass and p_s, 1.0 kW per kilogram, is the specific power assumed for the engine and generator. The take-off mass is found by iteration as the fixed point of that loop: mass sets the cruise power, cruise power the engine rating, the engine rating the propulsion mass, and the propulsion mass the take-off mass. The rest of the propulsion mass, the fixed 0.108, is a fraction back-solved from the reference design's own budget. Hover power, W^1.5/(FM √(2ρA)) with the disc area A set by the fixed disc loading, is computed at the closed mass and reported, and it does not size the engine. Because the disc loading is fixed, hover power is itself proportional to take-off mass, so any mass that scales with hover power scales as a fixed fraction does; the loop computes no hover-rated mass of its own. The buffer that supplies the hover deficit is a fixed 3.6 percent of take-off mass. If no fixed point exists, the declared sizing package does not close. That is a statement about that package rather than about whether some other package could, and the calculation then returns no number.

#### What the loop holds fixed


The reference design's assumed zero-lift value of 0.0248 is not used: the build-up of Section 6.2 places it below both ends of the bracket, outside the supported range. Propeller efficiency enters the loop twice, in the range expression and in the cruise power that sizes the engine, and both entries move together with the blade family in every closure; scaling one without the other would size the engine on one propeller and compute the range on another.

The loop holds wing loading (25.3 kg/m²), disc loading (44.2 kg/m²) and aspect ratio (6.03) fixed, so area, span and nose disc diameter follow the mass: across the four closures the wing area runs from 2.07 to 2.27 m², the span from 3.53 to 3.70 m and the nose disc diameter from 1.23 to 1.29 m, and the cruise lift coefficient is 0.450 in every one of them. The tip-frame length, the tip-disc diameter and the strip are not sizing variables. They were set on the 50 kg reference design of Section 5.2, and the control moment arms of Section 5.2 are therefore reference values that this closure does not re-derive.

The frame and rotor drag terms are coefficients on the reference wing area of 1.979 m², so holding them unchanged across the closures lets that hardware grow with the wing. Held at its reference size instead, the hardware would give terms 4 to 13 percent smaller across the four closures, 0.0009 to 0.0028 of zero-lift drag. The closures do not take that reduction, and it has not been run through the loop.

The drag polar is likewise a fixed input. Chord grows with the square root of area, so the chord Reynolds number is up to about 7 percent higher than on the reference design (about 5 percent across the four closures). On a turbulent flat-plate scaling, C_D0 ∝ Re^−0.2, 7 percent is a 1.4 percent change in the zero-lift coefficient, against a bracket whose two ends differ by 34 percent. The claim is that C_L is unchanged, not that C_D0 is exactly so.

#### The check against the reference design


Run on the reference design's own assumed inputs (a zero-lift coefficient of 0.0248 without the rotor term, and a propeller efficiency of 0.80), the construction returns a take-off mass of 49.4 kg against 50.1 kg, a cruise lift-to-drag ratio of 11.88 against 11.88, and a range of 1 585 km against 1 583 km. The largest deviation is 1.5 percent, in mass. This check is the only place in the closures where the assumed zero-lift value appears; every closure uses the bracket.

#### The transition loss and the controller


The 50 kg design is rotated in a three-degree-of-freedom model: the body angle follows a reference profile through a proportional-derivative controller whose moment is limited to the available control moment of 23.0 N·m, with a rotation time of 2 s, an entry climb of 5 m s⁻¹, and the aerodynamic pitching moment set to zero. The loss persists across three reference profiles: 5.43 m with a linear profile, 6.33 m with a smooth (cubic) one and 6.57 m with a bang-bang one, which is the body's 5.4 to 6.6 m. In none of the three does the control moment saturate. Raising the gains increases the loss rather than removing it: with the proportional gain raised sixteen-fold and the derivative gain four-fold, the loss is 16.9 m, again without saturation. With the zero-lift coefficient at either end of the bracket and an Oswald factor of 0.817 instead of the assumed 0.0248 and 0.85, each figure moves by at most 0.02 m. Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude.

#### The range figures


The ranges of the four closures are closed-loop values at a fuel fraction fixed at 0.16, not a ranking. Because the comparative result depends on the sizing contract, no comparison in this paper should be quoted without the contract it was computed under.

### S11. The ledger: working for Sections 5.2 and 6.2

#### The tip discs stopped: an estimate outside the closure


In the closure the tip pairs cruise free-wheeling at zero shaft torque. For the other admissible state, stopped, the eight tip discs of the 50 kg reference design are estimated as follows; neither stopped figure is part of the closure of Section 6.1.

| Tip discs in cruise | ΔC_D0 |
|---|---:|
| Free-wheeling at zero shaft torque (blade-element result, in the closure; favourable end) | 0.0154 |
| Stopped edge-on, azimuth controlled (estimate) | 0.0008 |
| Stopped broadside, azimuth uncontrolled (estimate) | 0.015 to 0.018 |

The stopped figures are an area-and-coefficient estimate with assumed solidity and section drag coefficients, not a propeller calculation; what is robust is the ratio between the states, not the values. The edge-on figure assumes an azimuth that something holds.

#### The line items of the drag bracket


Every cost named below is already inside the closure of Section 6.1. No new physical cost term is introduced here.

| Zero-lift drag build-up | favourable end | adverse end |
|---|---:|---:|
| Clean wetted surface | 0.0073 | 0.0142 |
| Hub and small items | 0.0015 | 0.0022 |
| Tip frames | 0.0043 | 0.0047 |
| Tip-pair rotors, free-wheeling | 0.0154 | 0.0169 |
| Total | 0.0285 | 0.0381 |

The two ends differ for two separate reasons. The clean surface and the hub are where the drag bracket itself lives, so their base values differ between the ends; on top of that, the adverse end carries a ten percent margin applied to the whole build-up, so the frames and rotors, which have the same base value at both ends, differ only by that margin. No line item at the adverse end is an independent measurement, and they should not be subtracted from one another as if they were.

The tip frames and the free-wheeling rotors together are 69 percent of the zero-lift drag at the favourable end and 57 percent at the adverse one. Removing the hub and small items, the tip frames and the free-wheeling rotors gives a clean-body lift-to-drag ratio of 20.55 at the favourable end and 15.24 at the adverse one, against the aircraft's 10.82 and 8.79: the configuration retains 52.6 and 57.7 percent. Bill 2 therefore occupies a larger share where the clean-body drag is lower, because a near-constant charge is set against a smaller total. That is a statement about position within the drag bracket at one scale, not about size (Section 6.3).

#### The buffer against the deficit it covers


The buffer fraction is an input to the loop and is not re-derived from the hover energy the four closures need. What the buffer supplies is the hover demand less what the engine can deliver, taken at the electrical bus where the buffer sits: the rotor shaft power divided by the machine and power-electronics efficiencies (0.92 and 0.95), less the engine's shaft power times the generator efficiency (0.90).

| Closure | Deficit at the bus | Per kilogram of take-off mass | Buffer at 3.6 percent |
|---|---:|---:|---:|
| A | 9.68 kW | 0.1683 kW/kg | 2.07 kg |
| B | 9.74 kW | 0.1744 kW/kg | 2.01 kg |
| C | 9.82 kW | 0.1835 kW/kg | 1.93 kg |
| D | 9.86 kW | 0.1884 kW/kg | 1.88 kg |

The deficit per kilogram spreads by 12 percent across the four closures, and the closure that needs the most per kilogram, D, carries the smallest buffer.

#### The propulsion-mass split


The propulsion fraction of the empty mass is 0.176 to 0.198 across the four closures, in two parts. A fixed 0.108 is back-solved from the reference design's own budget (the code's comment lists propeller, shaft, mount and wiring). The engine term is the engine rating divided by an assumed specific power of 1.0 kW per kilogram: 0.068 at closure D to 0.090 at closure A, following the cruise-sized rating of 3.54 to 5.17 kW. The hover power, 11.4 to 12.5 kW at the rotor shaft, passes through the electrical path whatever the engine is rated at, but the loop computes no hover-rated mass for that path; whatever of it lies in the fixed 0.108 scales with take-off mass, which at fixed disc loading is how hover power scales. The airframe (0.300) and avionics (0.080) fractions are construction constants held common across the three architectures of Section 6.4; they are not results of the ledger.

### S12. Scale: working for Section 6.3

#### The reference pair


The test uses the 50 kg and 1 000 kg reference designs, sized by one method. No closure of Section 6.1 was run at 1 000 kg: the heavy design has no drag bracket and no structural closure, and no heavy-design range is quoted.

Disc loading is held at approximately the same value, 44.2 kg m⁻² at 50 kg and 43.7 at 1 000 kg, so specific hover power is held with it: 0.218 kW kg⁻¹ at the light design and 0.216 at the heavy. That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3. Section 6.2's measure of Bill 3, rotor-shaft hover power over engine shaft rating, is 4.19 at the light design (10.9 kW over 2.6 kW) and 3.98 at the heavy (216.2 kW over 54.3 kW). The two designs rate their engines at different margins over cruise power, 1.53 and 1.39; with the light design's margin, the heavy ratio would be 3.61. The ratio therefore moves by 5 to 14 percent across the factor of twenty, depending on an engine margin the sizing rule does not set. Section 6.2's 2.4 to 3.2 is the same ratio at the four closures. This paragraph compares the reference pair only.

The rule has a price, paid in geometry: the ratio of nose-propeller diameter to span rises from 0.35 to 0.47, and much above 1 000 kg a single nose pair can no longer hold the disc loading, so a second would have to be added.

#### The rotor term of Bill 2


Only the rotor term of Bill 2 is computed at both sizes; the frame term enters both designs as the same multiplier, so it cannot show a scale effect in either direction. At 50 kg the rotor term is 0.0154. At 1 000 kg, eight tip-rotor designs at section lift coefficients from 0.55 to 0.85, all meeting the hover figure of merit, give 0.0045 to 0.0100, that is 0.29 to 0.65 of the light value; the design at the light design's section lift coefficient, 0.68, gives 0.0068. Within the blade-element and section-polar model the section Reynolds number accounts for the fall: the median section Reynolds number rises from about 8.2 × 10⁴ to 5.6 × 10⁵, and the heavy blade brought down to the light design's Reynolds number gives 0.0181, 1.18 times the light value. The other candidates are excluded. The heavy blade is the more solid (1.33 times), which would raise its drag rather than lower it; dynamic pressure cancels (between 30 and 40 m s⁻¹ the heavy term changes by a factor of 0.911, against the 0.562 a dynamic-pressure effect would give); and the design tip speed (210 m s⁻¹) and the hub fraction (15 percent of radius) are the same at both sizes. This is a decomposition inside the model rather than a causal claim beyond it.

#### Bill 1


Both buffer figures are inputs: 0.036 of take-off mass in the light closures and 0.040 in the heavy design's sizing. A change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction. A buffer sized to the hover deficit at the same specific power would track hover power and engine rating, which are the Bill 3 measures, so that derivation cannot test whether Bill 1 separates.

#### The rotation time


The transition is where the square–cube relation is paid. The heavy design's pitch inertia is 255 times the light design's and its available control moment 41 times, so to keep the light design's moment margin it must rotate in about 5 s rather than 2 s (4.96 s computed; the heavy design uses 5.1 s). A larger aircraft of this type turns more slowly, and must.

### S13. Contracts: working for Section 6.4

#### The three contracts


Range in the sizing loop is R = f_fuel E* η_chain (L/D)/g, with E* the fuel's specific energy and η_chain the energy chain from fuel to thrust. The three architectures share E* and the chain apart from the propeller efficiency, which enters η_chain, and they differ in L/D. The three contracts differ only in the fuel fraction f_fuel:

1) fixed fuel fraction: every architecture carries 0.16 of its own take-off mass as fuel, so take-off mass cancels from range;
2) fixed fuel mass: every architecture carries the fuel this configuration carries at that closure, 9.20, 8.94, 8.56 and 8.37 kg at closures A to D, as a fraction of its own take-off mass;
3) fixed take-off mass and payload: every architecture is held at this configuration's take-off mass with the same 13 kg payload, and its fuel is what remains after its empty mass, so every kilogram of architecture-specific hardware is a kilogram of fuel not carried.

#### The per-closure numbers


Range of the lift-plus-cruise layout relative to this configuration (positive: lift-plus-cruise ahead), and the mass ratio under the first contract:

| Closure | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass | Shift, first to third | Lift-plus-cruise mass / this configuration's, first contract |
|---|---:|---:|---:|---:|---:|
| A | +67.8 % | +40.2 % | +1.1 % | 66.8 points | 1.392 |
| B | +55.3 % | +27.5 % | −13.0 % | 68.3 points | 1.433 |
| C | +83.9 % | +53.5 % | +7.3 % | 76.6 points | 1.378 |
| D | +70.2 % | +40.1 % | −6.5 % | 76.7 points | 1.409 |

The tilting layout, credited with no cruise penalty, is 93 to 141 percent ahead under every contract at every closure: the size of the bound of Section 6.4, not a ranking.

#### Without the common buffer


If the competitors carry no buffer and rate their engines to the hover demand, the lift-plus-cruise layout does not close at any of the four closures under a fixed fuel fraction or a fixed take-off mass; under a fixed fuel mass it is 38 to 47 percent behind this configuration. This case is not used in Section 6.4's comparison; it shows only the direction of the choice to hold Bill 3 common.

#### Sensitivity


| Case | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass | Shift, first to third |
|---|---:|---:|---:|---:|
| As declared (lift group 10 % of take-off mass, competitors' propeller efficiency 0.80) | +55 to +84 % | +28 to +54 % | −13 to +7 % | 67 to 77 points |
| Lift group 5 % of take-off mass | +55 to +84 % | +47 to +76 % | +36 to +65 % | 14 to 24 points |
| Lift group 15 % of take-off mass | +55 to +84 % | +8 to +31 % | −62 to −50 % | 117 to 134 points |
| All three at this configuration's propeller efficiency | +33 to +45 % | +6 to +17 % | −33 to −25 % | 65 to 72 points |
| Lift-plus-cruise drag as a fixed increment, not a ratio | +59 to +75 % | +31 to +45 % | −13 to +5 % | 67 to 75 points |

With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every closure; with a heavier one this configuration leads under a fixed take-off mass at every closure; with a common propeller efficiency a reversal appears at every closure. The quantities that decide the sign are assumed for the competitor rather than measured: its lift-group mass fraction and its propeller efficiency. The sign under a fixed take-off mass is not a result about the architectures; it is a result about those quantities.

### S14. What does not close: working for Sections 3, 6.2 and 7

#### The measured store figures


The flown system is a 24-series nickel–cobalt–manganese pack designed, bench-tested and flown in a 210 kg-class electric VTOL aircraft [25]. As a flown system (24S4P) it is rated at 0.892 kW per kilogram continuous; its 13.5 kg unit pack (24S1P) is rated at 0.724 kW per kilogram continuous. Discharged on the bench at its highest tested rate, 10.68C (235 A), the unit pack delivered 1 394 Wh in about 249 s, on average about 1.5 kW per kilogram for about four minutes, and reached 55.1 °C against the 60 °C limit its authors adopted. Against that bench average the take-off demand of the four closures, 5.5 to 6.1 kW per kilogram of buffer, is 3.7 to 4.1 times, and hover alone, 4.7 to 5.2 kW per kilogram, is 3.1 to 3.5 times.

#### The loop closed again on a measured store


Closing the loop on a measured store is a sensitivity of the package, not a second aircraft. The buffer is derived inside the loop from the take-off demand at a given specific power; everything else is Section 6.1's: the same fractions, including an airframe at thirty percent of take-off mass, and the same wing loading, disc loading and aspect ratio, so the lift-to-drag ratio is carried unchanged and, with the fuel fraction held, so is the range. These masses are the Section 6.1 package with one input changed. They are not a structural closure at 100 kg, and whether the airframe fraction holds at twice the mass it was set at is not established.

| Buffer specific power, per kilogram of buffer | Take-off mass | Buffer | Change from Section 6.1 |
|---|---:|---:|---:|
| As Section 6.1 implies: 5.5 to 6.1 kW kg⁻¹ | 52.3 to 57.5 kg | 3.6 % | — |
| 4 kW kg⁻¹, the design-study assumption [26] | 56.6 to 61.2 kg | 5.0 to 5.5 % | +6.5 to +8.2 % |
| About 1.5 kW kg⁻¹, the unit pack's bench rate | 94.6 to 101.2 kg | 13.4 to 14.7 % | +76 to +81 % |
| 0.892 kW kg⁻¹, the flown system's continuous rating | about 335 kg | 22 to 25 % | set by nearness to non-closure |
| 0.724 kW kg⁻¹, the unit pack's continuous rating | does not close | — | — |

If Section 6.1's take-off masses are kept instead of re-closing at the bench rate, the payload falls to about 7 kg rather than 13. At the flown system's continuous rating the loop only just closes, and the mass it returns is set by how near the loop is to not closing rather than by anything about the aircraft.

#### The open questions


Section 7 lists eighteen questions this work has not answered. Each is given here with what it bears on and what would settle it; one further row, on store types, belongs to the known obstacle and is not one of the eighteen.

| Item | Bears on | What would settle it |
|---|---|---|
| **The pitching moment through the transition.** Three methods of three fidelities diverge above about ten degrees of incidence; the rotation passes through that band, peaking near 18 to 22 degrees on the 50 kg reference geometry, with the inboard half of the wing in the slipstream at a much lower effective incidence. | Whether the aircraft trims through the rotation (Sections 5.1 and 6.1) | Validated aerodynamic data: a measurement of the outboard wing's pitching moment to about 22 degrees at low dynamic pressure and of trim at the attached-flow end of the rotation, or a higher-fidelity method validated against one |
| **Section drag at low Reynolds number.** The tip-pair rotors' free-wheeling charge rests on section polars below a Reynolds number of 10⁵, and the uncertainty runs both ways. | The rotor term in every closure, 0.0154, carried as 0.0169 at the adverse end with the build-up's ten percent margin (Sections 6.1 and 6.2); the size of Bill 2's fall with scale (Section 6.3); and the tip-rotor blade itself, which the hover requirement selects on the same polars (Supplement S12) | Validated data: the drag of a free-wheeling tip rotor, or of its sections, at about 8 × 10⁴, or a method validated there |
| **The tip pairs' other cruise state.** Free-wheeling is determinate and computed; stopped is a family of states whose means and azimuth are not fixed (Section 5.2; Supplement S11). | Whether a lower-drag cruise state is available, and at what mechanism cost | Analysis, or a measurement of one stopped state |
| **The tip pairs' shaft power off the free-wheeling state in cruise.** Attitude moments in cruise are commanded departures from the zero-shaft-torque state, and the shaft power they take is not computed (Section 5.2). | Cruise energy | Analysis of cruise attitude demand and of the tip pairs' shaft power off the zero-torque state |
| **The buffer's energy, not only its power.** The store is sized here by power. Whether it also holds the energy for the vertical phases and their reserves, and how it is recharged in cruise, depends on a hover duration this work does not fix; at the bench rate the unit pack emptied in about four minutes. | Whether the store sized by power is also large enough | Analysis against a defined mission profile |
| *Other store types (part of the known obstacle; not one of the eighteen).* A supercapacitor store is tabulated in one survey at specific-power ranges that include values at the level the buffer requires, 500 to 10 000 W/kg from one cited source and 10 000 to 100 000 W/kg from another, at 1 to 10 Wh/kg [23]. The table has no battery–supercapacitor row; the combination enters only through the survey's own qualification on this class: *"Supercapacitors exhibit low specific energy but outstanding specific power at high cost suggesting that this technology is more appropriate in a hybrid energy storage approach (e.g. supercapacitors and batteries)."* | Whether a store other than a battery, alone or combined with one, closes the buffer at the required power and holds the vertical phases' energy | Analysis against a defined mission profile; not computed here |
| **The electrical path at peak.** Machines, power electronics, wiring and their cooling carry the full take-off demand; the loop computes no mass for them sized to that peak and its heat (Section 6.2; Supplement S11). | Whether the path that delivers the buffer's power exists at the mass assumed | Component sizing and thermal analysis |
| **The airframe's mass.** It enters the loop as a construction constant, thirty percent of take-off mass (Supplement S11). A component build-up at the reference mass leaves room for the 13 kg payload only if the average shell areal density stays at or below 1.78 kg m⁻², against 1.50 assumed; the build-up carries a contingency rather than a structural sizing, and it has not been re-run at Section 6.1's closed masses, still less at the masses the store re-closure returns. At the 1 000 kg reference design the shell-mass exponent is not measured at all. | Every closed mass | Structural sizing (analysis), then a built article (measurement) |
| **The strip and the fairing.** The strip's effect on this planform is computed, not measured, and its actuation is carried in the systems budget without being sized (Section 5.2). The fairing is sized against a published stability criterion at an assumed lateral lift-curve slope, counts the frames' side force only, and the side force it develops is not measured (Supplement S8). | The strip: the body roll axis, which appears as bank in cruise and as a change of heading in hover (Section 5.2). The fairing: directional stability in cruise | Measurement of both surfaces; sizing of the actuation |
| **Closed-loop attitude control, in hover and in cruise**, including the cost of declining the reaction-torque channel, which would act about the body roll axis in both regimes (Section 5.2), the absorption of the hover torque residual left by trimming each pair's torque balance at cruise (Section 5.2), and the allocation of the tip pairs between take-off margin and attitude authority, which compete for the same propellers. | Whether the aircraft is controllable with the authority computed, in hover and in cruise (Sections 3 and 5.2) | Analysis not yet done: a control-allocation study, then simulation |
| **Vertical descent and the landing transition.** Neither is analysed; the vortex ring state is not assessed, and the landing transition is not the take-off transition run backwards (Supplement S5). | Whether the aircraft can come down as it went up (Section 3) | Analysis not yet done |
| **Ground handling and landing loads.** The stance base is a parameter against static crosswind (Section 3), and the wing's exposure to ground wind is not priced (Section 4); the response to a landing with lateral velocity or on uneven ground, and handling between flights, are not assessed. | Operation from unprepared sites | Analysis not yet done |
| **The competitor's lift-group mass.** It is one of the two assumed quantities that decide the sign of the fixed-take-off-mass ordering in Section 6.4; the other is the competitor's cruise propeller efficiency. | Section 6.4's sensitivity, not a claim | Measured inventories of lift-plus-cruise aircraft of this class |
| **The competitor's cruise propeller efficiency.** Assumed at 0.80, not computed; with all three architectures at this configuration's propeller efficiency, this configuration leads under a fixed take-off mass at every closure (Supplement S13). | Section 6.4's sensitivity, not a claim | Computation of that propeller at its operating point |
| **Rotor–structure and rotor–wing interference, in cruise and in hover.** In cruise it is inside Bill 2 in principle, absent from the build-up and not modelled (Section 6.2); the drag bracket's upper margin is the only provision made for it. In hover the nose pair's slipstream runs over the inboard wing and the strip (Section 5.2), and any force or moment it produces there beyond the strip's commanded action is not computed. On a quadrotor tail-sitter reported in 2013 the slipstream acting on a wing under the propellers made control about the thrust axis difficult, and the wing was moved out of it ([3], p. 320); that aircraft used single rotors, and whether a contra-rotating pair changes the effect is not computed. | Bill 2, and so every closure; in hover, the control about the body roll axis and the hover torque balance (Sections 3 and 5.2) | Analysis not yet done |
| **Engine installation**: bay, intake, exhaust, cooling. | Mass, drag and packaging | Absent from this work entirely |
| **Blade-family selection.** The criteria that would choose among the blade families (structural loads, acoustics, the motor operating point, rotor inertia, manufacture) are not modelled (Section 4; Supplement S6). | Which point of the envelope the aircraft occupies | Analysis not yet done |
| **The variable-pitch counterfactual.** Whether a variable-pitch hub would recover the fixed-pitch cruise-efficiency gap is not computed (Sections 4 and 6.2). | The cruise-efficiency gap (Section 6.2) | A variable-pitch counterfactual closed through the same loop |
| **Atmosphere.** Every number here is at sea level; the configuration's own altitude sensitivity has been computed for hover power and propeller efficiency, but its effect on the Section 4 comparison has not. | The comparison in Section 4, made against a mission flown at altitude | Analysis; the direction of the effect has not been computed |
