## The gap

### Two families, two different limits

Uncrewed powered flight is dominated by two configuration families, and neither is bounded by
the thing the other is bounded by.

**Fixed-wing aircraft** carry payload over distance efficiently, because a wing sustains the
vehicle without continuously spending power on lift. Their limit is not aerodynamic but
infrastructural: a runway, a catapult, or an equivalent installation. That requirement is
expensive, fixed in place, and scales badly — a larger aircraft wants a longer runway, stronger
pavement and wider taxiways, so its growth is gated by the ground rather than by the air.

**Rotorcraft and multirotors** remove that requirement completely. They take off and land
vertically, hover, and work from confined sites. Their limit is the converse: with no wing,
every second of flight is bought with installed power, so range and endurance stay modest and
worsen as the vehicle grows.

**Neither family is deficient.** Each is excellent at what it does and is limited by the price of
doing it that way. **The corner where both capabilities are wanted at once is where the two
applications this work is aimed at sit** — wildfire observation and response, and cargo delivery to
places without a runway — and both want to leave from an unprepared site and then cover distance.
**That corner is not empty**, as the rest of this section sets out; what is unsettled is which
price an architecture in it must pay, and whether one arrangement pays less than it appears to.

### The demand has been continuous for seventy years

Tail-sitting prototypes flew in the 1950s, vectored-thrust and tilt-wing aircraft in the 1960s,
tilt-rotors from the 1980s, and a broad family of hybrid vertical take-off and landing uncrewed
aircraft since roughly 2010. Different nations, services and propulsion philosophies have
attacked the same problem for seventy years. **No field sustains that level of effort against a
need that is not real.**

### What the contemporary answers do, and how each changes regime

Hybrid VTOL aircraft occupy that corner today, and several are in service. **This paper does
not dispute that they work.** What matters for the argument is *how* each changes between the
two regimes, because that is where the families differ from one another.

A NASA study that sizes five VTOL architecture families to one mission describes the two
relevant routes in its own terms.

**The lift-plus-cruise route keeps two sets of hardware and switches between them.** In that
study the configuration is a stopping-rotor compound with three flight modes — helicopter mode
with the lifting rotors turning, compound mode with both sets operating, and aeroplane mode in
which *"the lifting rotors are stopped with the blade axis pointed along the vehicle
longitudinal axis, and therefore nominally aligned with the free stream to minimise drag,"*
with forward thrust from a pusher propeller. The lifting rotors are carried through cruise and
are stopped in the airstream.

**The tilting route keeps one set of hardware and reorients it.** The tilt-wing in the same
study carries six proprotors on a tilting main wing and two more on a tilting tail, each
directly connected to its own electric motor. Nothing is carried unused; the same discs that
lift the aircraft propel it, after being turned.

**Both work, and the second is the more elegant on paper** — one propulsion group, no dead
hardware in cruise. It is also the more demanding to build, because rotating a propulsor in
flight brings a pivot and its actuators, a gyroscopic moment during the rotation, and a control
problem through a regime in which the aircraft is neither a rotorcraft nor an aeroplane.
**Those are mechanical and control requirements rather than aerodynamic ones**, and that
distinction is what this paper is built on.

### The third route is established, and its history is not what it is usually taken to be

There is a third way to put one set of propulsors into both regimes without reorienting them:
**point the thrust line at the ground and let the whole aircraft rotate.** It is neither new nor
untried nor abandoned. Two American prototypes flew it in 1954, **and uncrewed tail-sitters have
revisited it continuously since.** The Lockheed XFV-1 never
completed the cycle. The Convair XFY-1 did: it flew vertically in August 1954, and six
transitions to conventional flight were completed.

**Why that programme stopped matters, because the usual account is wrong.** Two NASA reviews of
United States V/STOL development — one written largely from the reviewer's own flight-test
experience — judge the configuration itself favourably, calling it a *"good configuration
arrangement for low- and high-speed compatibility."* What they judge poorly is the machinery and
the cockpit around it: *"poor mechanical control system features including low actuator response
rate"*, difficulty hovering precisely over a spot, tip-over tendencies on the ground in gusty
air. The landing difficulty is attributed to *"the unusual spatial orientation where the pilot
looked over his shoulder and down"*, to turbulence sensitivity, and to reduced control power
near touchdown.

And the reason testing ended is recorded identically in both reviews:

> *"Six transitions to conventional flight were successfully completed **before testing was
> curtailed because of engine and gear-box reliability problems**."*

The pilot workload was real, separately documented and severe. **But it is not what curtailed the
testing.** The reviews record a longer list of handling and control difficulties than this section
reproduces, and no attempt is made here to sort them into those that would and would not recur —
what the record settles is the cause of the curtailment, and that cause was mechanical.

### What the history does not excuse

It would be too convenient to conclude that every one of those programmes ended for reasons
outside its configuration, and this paper does not conclude it. **Some of the difficulties were
real, internal, and are inherited here.** A tail-sitting vertical descent is genuinely harder
than a runway landing. A tail-sitting aircraft on the ground is more exposed to crosswind than a
conventional one. And a set of propellers whose thrust vectors are all parallel to the body axis
produces no rolling moment **by any combination of thrust settings** — which applies to the
configuration described later exactly as it applied to its predecessors. **The reaction-torque
channel that other coaxial tail-sitters use about that same axis is a separate matter, and it is a
choice this configuration declines rather than a limit it inherits; Section 7 says so and Section 9
says what declining it leaves uncounted.**

What the record does show is that **the obstacle that ended the flying was mechanical**, and
that one of the documented handling obstacles — the pilot's spatial orientation and workload —
is removed by an uncrewed aircraft. **The others are not removed by anything.** Precise hovering,
ground gusts and the absence of a thrust-borne rolling moment are configuration facts, and they
are inherited.

Three things are available now that were not: electric drive on each individual rotor,
sensor-based attitude reference, and enough onboard computation that stability need not come
from the airframe alone. **The uncrewed tail-sitter literature has been exploiting exactly those
three for over a decade**, which is why the gap below is not a historical one.

### What is already occupied, stated before the gap

It would be easy, and wrong, to present the third route as an empty field. **It is not**, and
the paper is better for saying so first.

**The route itself is established.** Uncrewed tail-sitters combining fixed-pitch rotors with a
flying wing have been built and flown for more than a decade, beginning with quadrotor-plus-wing
arrangements carrying a few aerodynamic actuators for forward flight.

**Attitude without aerodynamic control surfaces is established.** A quadrotor tail-sitter
operated without control surfaces, with experimental verification, was reported in 2013.

**Coaxial contra-rotating propulsion on a tail-sitter is established**, proposed specifically to
remove the reaction torque a single propeller imposes, at the cost of an extra motor and the
coaxial arrangement. A coaxial contra-rotating tail-sitting micro air vehicle reported in 2014
states the same purpose in the same terms: *"a pair of 10 inches coaxial contra rotating
propellers is mounted to compensate each other's torque."*

**The established answer to hover control on such a configuration is a surface in the
slipstream**, and it is worth naming because this paper refuses it. That 2014 vehicle places
*"elevon and rudder … immersed in the propeller slip stream to provide three axis control moments
in hover."* The answer works, costs little, and is the one a reader will reasonably expect.

**And the reaction-torque channel this paper declines is established as a control channel.** A
coaxial contra-rotating tail-sitter reported in 2012 balances rotor torque *"by the inverse
rotating of the two rotors"* and then unbalances it on purpose to steer: its published control
scheme assigns *"differential velocity of the two motors"* to yaw in the vertical mode and to
roll in the horizontal one. **Those are the same physical channel under two names** — a moment
about the propeller axis, which stands vertical in hover and horizontal in cruise — and
independently driven rotors make it available to any coaxial pair. **Using it is a choice, and
so is declining it**, which is what separates this configuration's control problem from a
physical impossibility.

**A blended-wing-body tail-sitter with contra-rotating propulsion, aimed at disaster response,
is established**, reported in 2025 with vortex-lattice and RANS analysis of its planform,
winglets and transition.

**And the propeller compromise at the centre of this paper's own ledger is a known result, not a
discovery.** The uncrewed tail-sitter literature states it directly: fixed-pitch propellers make
it *"theoretically impossible to be very efficient in both hovering and forward flight."* A
long-range tail-sitter reported in 2018 describes its own rotor as *"a compromise between
efficient hover and efficient forward flight"* and selects its diameter on exactly that basis.

### The gap, stated precisely

**Each half of the required capability is well served, and both halves together are served by
the contemporary hybrids.** This paper does not claim otherwise. **And the third route is
occupied.** What follows is therefore not a claim to an empty field.

**What is not established is the combination taken together with its price.** Specifically:
a blended-wing-body tail-sitter in which *every* propulsor is a coaxial, torque-balanced pair —
so that reaction torque and net angular momentum are given up along with the reorientation
mechanism — carrying no aerodynamic control surfaces beyond a single moving device, powered
through a buffered series hybrid, and **audited explicitly against carried hover mass, exposed
cruise drag and hover-sized continuous power**, at two scales and under three sizing contracts.

Each of those choices costs something, and **the giving-up is the part that is not free**. A
quadrotor tail-sitter produces a rolling moment from the reaction torque of four independently
driven rotors; a coaxial pair can produce one the same way, by running its two rotors at different
speeds. **Operating every pair torque-balanced spends that channel to buy the torque balance and
the near-zero net angular momentum**, and leaves the axis to a single aerodynamic device. What
that costs, and what the rest of the combination costs, is what the paper is for.

**None of the elements is new**, and Section 7 says so. Tail-sitting aircraft are seventy years
old and uncrewed ones are ordinary; blended wing bodies have been a standing subject of transport
research for three decades; series-hybrid propulsion has established precedent in small uncrewed
aircraft. **What this paper offers is the combination, the consequences of the choices inside it,
and an accounting of what they cost** — not a claim that the route was waiting to be found.

Section 2 states the cost that any architecture in this corner pays, in terms that do not
presume an escape.

---

## The tax

A claim that one architecture escapes a cost shared by the others is only meaningful if the
cost is stated first, in terms that do not presume the escape. This section states it. It is
not a claim about any particular aircraft, and nothing in it is new physics; what it provides
is the accounting that the rest of the paper is checked against.

### The root: a duty cycle that does not match the hardware

The vertical phase is short. For a mission of one hour, a take-off, a transition, a return
transition and a landing occupy on the order of a minute — **roughly two percent of the flight.**
Any hardware installed for that phase alone is carried through the remaining ninety-eight
percent.

**An architecture that provides the vertical phase with a dedicated lift subsystem therefore
carries it for fifty times as long as it uses it.** This is not an implementation defect and it
cannot be removed by making the subsystem better, because it is a statement about duty cycle
rather than about quality: a lighter lift rotor is still carried for the whole flight, and a
cleaner lift rotor is still carried for the whole flight. **The mismatch between how long a
component is needed and how long it is present is the origin of all three charges below.**

The statement is deliberately confined to architectures with a dedicated lift subsystem, because
that is the family the charges describe. Whether any architecture avoids the mismatch — and what
it pays instead — is the subject of the next section, and it is not settled here.

### Bill 1 — mass

The most direct payment is dead mass. A lift-plus-cruise aircraft carries two propulsion
groups: rotors, motors, mounts, wiring and structural reinforcement for the vertical phase, and
a separate propulsor for cruise. The vertical group provides no required lift or thrust during cruise and is
lifted anyway.

Its cost is not linear. Mass growth feeds itself — MTOW = m_payload / (1 − f_empty − f_energy)
puts additional empty mass through a multiplier that grows as the denominator shrinks — and in
the vertical phase the same increment is charged a second time, because at a fixed disc area
hover power scales with W^1.5. *(The exponent is a property of the scaling rule chosen: holding
disc loading constant instead makes hover power grow linearly with weight, and Section 12 uses
that.)* A modest dead-mass fraction becomes a large payload penalty.

**This charge has been identified independently, and by a source with no interest in the present
argument.** A NASA study sizing five VTOL architecture families against a common mission with common
tools found the lift-plus-cruise concepts the heaviest of the vehicles examined, and named the
cause: not the cruise power draw, since the lift-plus-cruise effective lift-to-drag ratio is the
higher of the set, but *"the extra empty weight items on board in hover."*

**That finding separates the two things this paper is at pains to keep separate.** The
lift-plus-cruise vehicle is *aerodynamically better* than the alternatives — its cruise
efficiency is higher, and the study says so — and it is nevertheless the heaviest, because of
hardware carried in order to hover. That is Bill 1 stated by an independent source in its own
terms: not a failure of engineering, but the cost of an architecture.

A second NASA review gives the structural half as a general principle, drawn from a tilt-prop
aircraft whose propeller separated in flight after a gearbox mounting fatigued: to transmit
power safely to the extremities of the planform, *"very strong (and fatigue-resistant)
structures must be incorporated with an obvious weight penalty."* Distributing lift or thrust
across the span therefore obliges the structure that reaches it to keep transmitting power
there — charged to mass, whether or not the distributed propulsors are running.

### Bill 2 — drag

The second payment falls on architectures that leave hover hardware exposed in forward flight:
rotors stopped in the airstream, the booms that carry them, and the interference between their
wakes and the wing. Cruise drag has other sources on any aircraft; what is charged here is the
part attributable to hardware retained for a phase that is over.

Wind-tunnel work on a hybrid airframe found that the difference between propellers parallel to
the airflow and no propellers at all is modest, while *"the drag produced by the motors is
significant."* The bill is charged mainly by the motors and the beams that carry them —
hardware that cannot be feathered, folded or aligned away, **because its cost is its presence.**

Two further measurements support the direction. Characterisation of a quadplane found the
highest lift and least drag in fixed-wing mode at both cruise airspeeds, with drag in the hybrid
regime exceeding either pure mode through adverse flow interaction; and — a point that bears on
how such aircraft are designed — that a simulation assuming negligible rotor–structure
interaction *"always predicts higher lift and lower drag than were experimentally observed."*
Separately, a study of twenty-six stationary lift propellers held edge-on found their drag
scaling with frontal area and the square of airspeed, with hover powertrain components adding
*"a significant amount of aerodynamic drag during forward flight"* in the absence of a stowing
mechanism.

**The important property of this charge is not its size but where it falls.** It is charged per
unit time in cruise — so it grows with exactly the quantity the aircraft exists to maximise.

### Bill 3 — power system sizing

The third payment is the least visible and often the largest. A VTOL aircraft must install
enough power to hover, but it draws that power only during the two percent of the flight in
which it hovers. The ratio between the two demands follows from the governing equations rather
than from any design choice. Taking hover power from momentum theory and cruise power from the
drag polar,

    P_hover / W  = √(DL / 2ρ) / η_h                 (DL = W/A, disc loading)
    P_cruise / W = V / ( (L/D) η_p )

so that

    P_hover / P_cruise = √(DL / 2ρ) · (L/D) / V · (η_p / η_h)

**The quantities on the right come from the configuration and from the propulsion operating
points, not from the duration of the hover phase.** That distinction matters and the efficiencies
are the reason for it: η_h and η_p are not configuration constants, they depend on the propeller
and on the condition it is run at, and Section 11 computes what happens when one fixed-pitch
blade has to supply both.

A vehicle with a disc loading of 100 N m⁻², a cruise lift-to-drag ratio of 15 and a cruise speed
of 30 m s⁻¹ needs **between three and four times** as much power to hover as to cruise: the
geometric terms alone give 3.2, and the efficiency ratio η_p/η_h carries it to about four when
the cruise propeller is roughly a quarter more efficient than the hover rotor. Raising the disc
loading raises the ratio as its square root. The prediction is borne out in flight: a
carbon-fibre tail-sitter reported in the literature measures its level-flight power consumption
at one fifth of its hover power, which is the ratio this expression gives for an aircraft of
that class.

The power system is therefore sized by a condition that holds for a minute and is then carried,
unused, for an hour. And the consequence propagates: sizing by hover means an oversized engine,
or a battery that must deliver a peak it will rarely be asked for, or both — and whichever is
chosen, the extra installed capacity is mass, which returns to Bill 1.

### The charges behave as one quantity in three currencies

The three charges are not independent problems with independent fixes. **Each known partial
remedy reduces one and raises another.**

| Move | Bill it attacks | Bill it creates |
|---|---|---|
| Distributed electric lift rotors | 3 — the cruise engine no longer sizes to hover | 1 and 2 — many rotors and mounts, permanently carried and exposed |
| Folding or retracting lift rotors | 2 — the exposed rotor is removed from cruise | 1 — mechanism, actuation, locking, a new failure mode |
| Tilt-rotor, tilt-wing, tilt-nacelle | 1 — one propulsion group serves both regimes | **Bill 3 is left standing** — with no store, the power plant is still sized by the hover peak — together with mechanical complexity, gyroscopic coupling and a transition control problem, which are **not among the three** |
| Variable-pitch or feathering propulsors | 1 and 3 — one propulsor is retrimmed across two widely separated operating points instead of duplicated | 1 — pitch hub, actuation, and a new failure mode |
| Higher disc loading, smaller rotors | 1 and 2 — smaller, lighter, cleaner rotors | 3 — hover power rises with √(DL) |
| Lower disc loading, larger rotors | 3 — hover power falls | 1 and 2 — larger structure and exposed area |

**One row does not pay in any of the three currencies, and that is not an oversight.** What a
tilting architecture buys its unified propulsion group with is a mechanism — a pivot, an
actuator, the gyroscopic coupling of a reorienting mass, and a control problem through the turn.
That is a cost, but it is not one of the three charges this accounting tracks, and the next
section says why it is treated separately. **The table is not a census of the field**; it lists
the moves whose transfers are documented, and a remedy absent from it is not thereby claimed to
cancel a charge.

**One of these transfers has direct experimental support, and it is worth more than the table.**
In the doctoral study whose wind-tunnel campaign supplies Table 1 — and in that document rather
than in the journal article by the same author, which reports a different comparison — a
retraction system removed thirty percent of the airframe's drag; the same work then costed it. Applied to a passenger eVTOL, with the mechanism assessed
at five percent of vehicle mass, maximum range rose from 119 km to 121 km — **a two-kilometre
gain for a five-percent mass penalty.** Bill 2 was converted almost exactly into Bill 1, and
**the transfer is the point rather than the small residue.**

### What this accounting is for

**The accounting is refuted by any remedy that reduces one charge while leaving the others no
worse and adding no cost of its own.** That is the test it has to survive, and the table above is
where it would fail: every entry in it is a documented transfer, and a counter-example would be a
move whose right-hand column is genuinely empty.

**Stated positively, so that the test can actually be run: a counter-example is a remedy that
reduces one of the three charges, leaves the other two no worse, and whose own cost is either
absent or demonstrably smaller than the reduction — measured in the same currency.** That last
clause is what makes the test usable rather than rhetorical: mass against mass, cruise drag against
cruise drag, installed continuous power against installed continuous power. **The accounting claims
transfer. It does not claim that every architecture is equally good**, and a remedy that is simply
a better bargain in one currency refutes it.

**Two clarifications keep the test from being either too easy or unfalsifiable.** A remedy that
attacks one charge and simply leaves another standing is not a counter-example — the tilting row is
the case, and it is written out there rather than left to be inferred. And a remedy whose cost
falls **outside** the three charges does not refute the accounting, because the accounting is about
those three; **but it is not thereby exempt from being counted.** The tilting family's mechanism is
named in the table for exactly that reason, and it is the reader's to weigh against what the
remedy buys. **A framework that could absorb any cost by declaring it out-of-scope would be
unfalsifiable**, so the costs outside the three are listed, not waved away.

It also makes a prediction that can be checked without settling the architectural question at
all: **where an arrangement pays one charge heavily in order to escape another, the ranking
against a differently-balanced arrangement will reverse when the sizing rule changes.** Section
13 tests that prediction on this configuration, and Section 4 tests a different consequence
against a sizing study this work did not produce.

**The moves in the table are partial remedies: each accepts the duty-cycle mismatch and then
redistributes what it costs.** Whether an architecture can decline the mismatch itself, rather
than redistribute its consequences, is a different question, and the next section states the
condition it would have to meet — a definition, derived from the table above rather than from
any aircraft.

---

## The escape condition

The previous section listed moves that redistribute the three charges. This one asks a different
question: what would an architecture have to do in order not to incur them at all? The answer is
a **definition**, derived by inverting the table rather than by describing any aircraft, and it
is stated here before any configuration is offered so that the standard is not taken from the
thing it will be used to measure.

### Inverting the table

The charges exist because the two regimes are served by hardware that is **not the same hardware,
not serving both duties, and not held in one orientation.** Depart from any one of those and a
charge appears:

| Departure | What it costs |
|---|---|
| **Different hardware** | Bills 1 and 2. The unused set is carried for the whole flight and, if exposed, drags. |
| **Same hardware, but it serves only one duty** | Bills 1 and 2 again. A propulsor that lifts and is then carried is a dedicated lift group under another name, whatever it shares with the cruise system. |
| **Same hardware, both duties, different orientation** | The tilting family. **Bill 3 is left standing unless a store supplies the hover peak**, and the mechanism that changes the orientation is itself mass, complexity and a control problem through the turn. |
| **Same hardware, both duties, one orientation, different sizing point** | Bill 3 — unless the hover peak is supplied from somewhere other than the continuously installed power. |

Read downwards, the table is a list of ways to pay. Read as a conjunction, it is a condition.

*(The second row is stated separately rather than folded into the first because it does real
work later: a propulsor that produces a little thrust in cruise is not thereby serving both
duties, and the distinction decides which parts of a configuration meet the condition and which
do not. "Serving both duties" is the accurate form; hover thrust and cruise thrust are not the
same **job** in any ordinary engineering sense — one supports weight, the other balances drag —
and calling them one would be loose.)*

### The condition

> **An architecture does not incur the three charges if the propulsors that carry the weight,
> held in one orientation relative to the airframe, produce both the hover thrust and the cruise
> thrust, and if the difference between the hover peak and the cruise demand is supplied from
> a store rather than from permanently installed continuous power.**

Four parts: **same hardware, both duties, one orientation, hover peak from a store.** The first
three come from the first three rows of the table; the fourth comes from the fourth.

Two things in that sentence are choices rather than derivations, and are marked as such. The
table requires only *one orientation relative to the airframe*; **how** an architecture keeps
that while changing flight regime — by rotating the whole body, or otherwise — is not in the
table, and is treated as exposition rather than as part of the definition. And the table's last
row permits the peak to come from **any** source other than the continuously installed power; a
store is the narrower reading used here, because it is what the configuration examined later
uses and because a narrower condition is easier to fail.

### What the condition does not say, and this matters more than what it says

The condition is named below the **zero-bill condition**, and the name has to be read exactly.
**It means zero of the three charges as Section 2 defines them** — the mass of a dedicated lift
subsystem, the cruise drag of hover hardware left exposed, and continuous power installed to a
hover peak. **It does not mean an architecture that costs nothing, and it does not mean an
architecture that carries nothing for the vertical phase.** A definition that placed every
conceivable cost inside the thing to be escaped would be unfalsifiable, and an architecture
built to satisfy it would win by construction rather than by performance.

So the costs the condition permits are named here, before any candidate is examined. Six of them,
and the first is the one that most nearly contradicts the name:

- **A store is permitted, and it has the same duty-cycle character as Bill 1.** The fourth part
  moves the hover peak off the continuous power plant and onto a store; that store delivers its
  peak for two percent of the flight and is carried for the rest. It is not Bill 1 as Section 2
  defines it — it is not lift-subsystem mass — **but it is mass carried for a duty that is
  briefly needed, which is the same complaint Bill 1 makes.** The condition converts a power-
  system charge into a mass one and claims only that the three charges as named are not incurred.
  **It does not claim the trade is favourable.** Whether the store is lighter than the continuous
  power it displaces is a sizing result and is computed, not asserted.
- **Releasing the engine is not releasing the electrical path.** The fourth part frees the
  continuous *power plant* from the hover peak. Everything between the store and the rotors —
  machines, power electronics, wiring — still passes the full hover power and is still sized by
  it. **That is a charge the condition does not remove**, and it is carried in the ledger rather
  than in this definition.
- **Rotating the airframe is permitted and is not priced here.** The condition refuses
  architectures that reorient a propulsor, and charges that refusal against the mechanism a tilt
  requires. **An architecture that instead rotates its whole body faces the same physical
  problem** — a ninety-degree change of the thrust axis relative to the flight path, with the
  moments, the authority and the control through the turn that implies. It is not one of the
  three charges and the condition does not eliminate it; it is priced where the transition is
  analysed. Saying otherwise would let a candidate win that line by wording.
- **Hardware installed for the vertical phase is permitted if it serves both duties**, and the
  second row of the table is what carries the weight. A propulsor that lifts and then propels
  satisfies the condition. A propulsor that lifts and is then carried does not, whatever else it
  shares with the cruise system.
- **Hardware used in both regimes for something other than propulsive thrust is permitted, and its
  cruise drag is not eliminated.** *Cruise thrust in this paper means the thrust that balances
  cruise drag.* Attitude devices produce thrust in cruise, but they produce no cruise thrust in
  that sense; they are used throughout the flight, so their duty cycle matches their presence and
  they fall outside Bill 1. **They remain in the airstream, so the second charge reaches them.**
  Those are two different statements and the distinction matters: **the condition is about the
  propulsor that carries the aircraft, so attitude hardware does not violate it — but the charges
  are about everything the aircraft carries, so Bill 2 reaches that hardware anyway.** An
  architecture in that position is a partial instantiation: it satisfies the condition where the
  condition applies and still pays one of the three elsewhere. The condition permits such hardware
  and does not make it free.
- **Serving two regimes with one set of hardware has a price of its own.** Hardware that is not
  duplicated cannot be optimised twice: a propeller sized for hover thrust at zero forward speed
  is not the propeller a cruise design would choose, and if its geometry is fixed the compromise
  is paid in efficiency. **The condition permits that cost and does not measure it.** Section 11
  does.

**One exclusion, stated narrowly.** Structure, surfaces and actuation present for reasons other
than the vertical phase are not charged **as duty-cycle mismatch under this accounting** — a
wing, a control device, a fairing that earns its place on a part already carried. That is a
statement about which ledger they belong in, not a claim that they are free, and it does not
apply to a part that would not exist but for the vertical phase. The tip frames are the case
that tests it: they are landing gear because the aircraft stands on its tail, and they also
carry the attitude propulsors and the directional fairing. **Their mass is charged in the
build-up and their drag in the ledger; the exclusion does not reach them.**

### The condition can fail, and how

A definition worth stating is one an architecture can be shown not to meet, so the failure modes
are explicit. An architecture fails the condition if **any** of the following holds:

1. It carries a propulsor through cruise that produces no cruise thrust.
2. It changes the orientation of a propulsor relative to the airframe in order to change regime.
3. Its continuously installed power is sized by the hover requirement rather than by cruise.
4. It satisfies the first three only in part — for instance in its primary propulsor while a
   secondary set fails them — in which case the instantiation is **partial**, and the part that
   fails re-opens the charge it fails.

The fourth is not a technicality, and it is the reason this list exists. **An architecture may
meet the condition where it carries the aircraft and fail it elsewhere**, and a paper that
reported only the first half would be reporting the condition rather than the aircraft.

### What follows from the condition, and what does not

The condition is a statement about what an architecture would have to be. **It is not a claim
that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim
that satisfying it is desirable.** Those are three separate questions and they are answered
separately: whether the accounting behind the condition survives contact with an independent
sizing study is tested in the next section, against data this work did not produce; whether any
configuration satisfies the condition is the subject of Sections 5 to 7; and what such a
configuration pays instead is the subject of Section 11, which is the longest of the three
answers because it is the one most likely to be wrong.

One consequence is worth stating now, because it shapes everything after it. The second row of
the inverted table — same hardware, different orientation — is refused by a means other than the
one the field has adopted. A tilting architecture accepts that row and buys its way out of the
first with a mechanism. **An architecture that reorients a propulsor does not satisfy the condition as written**, because
the condition requires one orientation relative to the airframe. **Whether such an architecture
might avoid the three charges by some other route is a separate question this paper does not
settle** — the condition is a definition, not a law, and it can be too narrow without being
wrong. What it is not is retrofitted: it is stated here so that when a configuration is offered
later, the reader can check the claim against a standard fixed before the configuration
appeared.

---

## An independent quantitative check

An accounting proposed by the same people who then use it to argue for a configuration invites
one obvious objection: that the charges were chosen because a particular aircraft happens not to
pay them. The objection arises at the title, not at the ledger, so it is answered here — before
any configuration is described — and it is answered in the only way that settles anything, by
testing a prediction the accounting makes against numbers this work did not produce.

**What follows is not a test of the whole framework.** It checks one falsifiable consequence on
one independent data set. That is a narrow thing, and it is stated narrowly.

### The prediction, stated before the data

**The prediction has two halves, and only the first is a derivation.** Saying so is what makes
the check worth running.

> **First half, derived from Section 2.** A configuration carrying a dedicated lift system pays
> for it in gross weight, and the payment is amplified: additional empty mass enters through a
> multiplier that grows as the empty-mass fraction rises, and the same increment is charged
> again in hover.
>
> **Second half, not derived.** That the cruise efficiency the arrangement buys does not cover
> that payment. Section 2 predicts the charge and the amplification; **it does not prove that
> the credit must lose.** A dedicated lift system raises the empty-mass fraction and may lower
> the energy fraction at the same time, and which wins is a closure result rather than a
> consequence of the accounting.

The check tests the second half on independent data, with the first half supplying the reason to
expect the outcome: the weight charge is amplified by a multiplier, while the efficiency credit
enters linearly through the cruise lift-to-drag ratio.

That distinction decides what a failure would mean. **If some data set showed the credit covering
the charge, Bill 1 would not be refuted** — the mass would still have been paid. What would be
refuted is the expectation that the amplified charge outweighs the linear credit, and that is
worth testing precisely because it could go either way.

**The prediction is also mission-dependent**, and the page would be weaker for hiding it. The
mass charge of carried lift hardware is roughly fixed; the efficiency credit accumulates with
distance. A long enough mission is where the credit is most likely to cover the charge, and the
mission used below is short. **The counter-set is therefore a common-mission sizing study at
longer range in which a dedicated-lift configuration is both more efficient and no heavier than
one without.** None is known to the authors, and the invitation is meant literally.

### The data

The check uses a NASA study that sizes **five VTOL architecture families**, most in two
propulsion variants — nine designs in all — against a single mission with common tools and
common assumptions. It was conducted for its own purposes, has no
relationship to the present work, and does not use the three-bill accounting of Section 2 or any
framework derived from it. It is used here for three reasons, stated so that the choice is not
merely the one that agreed: it holds the mission fixed across architecture families, it applies
one set of tools to all of them, and it reports both quantities this prediction needs. The
mission is 1 200 lb of payload over 75 nautical miles.

| Configuration | Effective L/D | Design gross weight | Dedicated lift group |
|---|---:|---:|---|
| Turboshaft quadrotor | 4.9 | 3 678 lb | none — the rotors serve both regimes |
| **Turbo-electric lift-plus-cruise** | **8.5** | **7 271 lb** | **yes** — eight lift motors and a cruise motor |
| **Turbo-electric tilt-wing** | **8.6** | **6 584 lb** | **none** — eight proprotors, reoriented |

### The result

**The primary comparison is the last two rows**, because they isolate the charge. The
lift-plus-cruise and tilt-wing entries share the mission, the payload, the turbo-electric
propulsion architecture and the presence of a cruising wing. **They are not identical in every
other respect** — one stops its lift rotors in the airstream and drives a separate pusher, the
other reorients its proprotors on a tilting wing — **but the difference the comparison turns on is
that one carries a dedicated lift group through cruise and the other does not.** The comparison is
the closest the published set comes to isolating that charge; it is not a controlled experiment.

**The tilt-wing is 1.2 % better in effective cruise efficiency and 9.4 % lighter.** The dedicated
lift group buys no cruise-efficiency advantage at all here — it is marginally behind — and the
design gross weights differ by 687 lb in the tilt-wing's favour. **That figure is the net
difference between two architectures, not the measured mass of a lift group**, and the
decomposition below is what makes it informative rather than merely large.

**The weight breakdown shows the transfer, and it does not close on the categories the table
reports.** Of the empty-weight difference of 679 lb, structure accounts for 716 lb in the
lift-plus-cruise entry's disfavour, propulsion returns 146 lb of it because the tilt-wing's
mechanism is heavier, and battery returns a further 10 lb. **Those three categories account for
580 lb of the 679**; the remaining 99 lb lies in empty-weight categories the published table does
not break out, and this work does not know how it is distributed. **What the three reported
categories do show is the transfer property of Section 2 — the mechanism giving part of the
structural saving back — visible inside a weight breakdown this work did not produce.**

**And the source states the second half of the prediction in its own words.** Discussing why the
all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high
cruise efficiency of the lift-plus-cruise type reduces battery weight compared with the
quadrotor, *"but not enough to counter the increase in structure and propulsion weight."* That
is the efficiency credit conceded and found insufficient, by the authors of the data rather than
by the authors of the prediction.

**The quadrotor row is retained as a contrast rather than as the test.** Against it the
lift-plus-cruise configuration is about three-quarters better in cruise efficiency — a factor of
1.74 — and nearly twice as heavy, a factor of 1.98. That is the prediction, and it is worth
being explicit about why it is not a counter-example to it: the efficiency credit is exactly
what the accounting says a dedicated lift system buys, and the weight charge is exactly what it
says the buyer pays. The charge survives the credit.

**But that contrast changes three things at once** — dedicated lift group, powertrain, and
whether a cruise wing exists at all — so it supports a weaker proposition than the prediction as
stated: that adding a wing and a lift group together still costs mass. Section 2 had already
called that much obvious. **It is reported for scale, and the isolation test above is what
carries the prediction.**

**The framework does not predict any of these numbers**; without the input fractions it predicts
no magnitudes. What it predicts is that the amplified weight charge survives the efficiency
credit, and on the isolated pair it does so with the credit reduced to nothing.

### The tilt-wing is the instructive case

The tilt-wing is the entry that carries the isolation test above, and it is also the entry that
denies this paper a claim it might otherwise be read as making.

**The architecture proposed later in this paper is not the only way to avoid the first charge.**
The tilting family avoids it too — it carries no dedicated lift group, it is the lighter of the
two matched designs, and an independent set says so. The margin in cruise efficiency is one
tenth and nothing is claimed from its direction; what matters is that the dedicated lift group
does not buy an efficiency advantage to set against its mass.

**Second, and this is what the row is actually for: the tilt-wing is the transfer property of
Section 2 appearing in someone else's data.** It does not escape the accounting by avoiding the
mass charge; it *moves* the charge — to the mechanism that reorients its propulsors, with the
actuation, the gyroscopic coupling and the transition control problem that Section 2 assigns to
that family. The row therefore does two jobs: it denies this paper a uniqueness it has not
earned, and it confirms the property the accounting is built on. What separates the tilting
family from the configuration described later is not this axis; it is what each pays, and a
sizing study does not settle that.

### What this check does and does not establish

It establishes that one prediction of the accounting holds on data produced elsewhere, for
purposes unrelated to this argument. That is the whole of it.

**It does not establish that the accounting is complete**, that the three charges are the only
costs an architecture pays, or that avoiding them makes an aircraft better. The accounting says
an architecture that avoids the three is cheaper in those three currencies and nothing more; a
configuration may avoid all three and still be unbuildable, uncontrollable, or unsuited to its
mission. Sections 10 and 14 are about exactly that possibility for the configuration proposed
here.

**It does not establish anything about the configuration this paper proposes**, which has not
yet been described, and which is not in the study used here. A reader who wants to know whether
the accounting flatters that configuration will have to wait for Section 11, where it is applied
to it and where the answer is not uniformly favourable.

What the check is for is narrower and comes earlier: **an instrument whose first use is to
measure the thing its authors are advocating should be shown working on something else first.**
That is what this section does, and it is the reason it appears here rather than after the
aircraft.

**The instrument is now fixed, and it is not modified again.** Sections 2 and 3 defined what any
architecture in this corner pays and what escaping it would require; this section tested one
falsifiable consequence of that definition on data produced by other people for other aircraft.
**Everything that follows is measured with it rather than added to it.** The next two sections
describe the two capabilities the mission asks for, one at a time and each against the family
that structurally lacks it, before Section 7 asks whether one aircraft can hold both.

---

## The first half: operation without a runway

### The opponent, and the axis

On this axis the alternative is the fixed-wing aircraft, and the comparison runs one way only.
**Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency**, where a
runway-launched aeroplane that never bought vertical capability pays none of the charges of
Section 2 and is the better machine. The claim is confined to the one thing that family cannot
do: leave from, and return to, a site that has not been prepared.

### What the requirement actually is

"Vertical take-off" is a weaker requirement than the one the missions impose, and stating the
stronger one first prevents the claim from being read as easier than it is.

A catapult-launched fixed-wing aircraft also leaves without a runway. What it does not do is
**come back** to the same unprepared site, and it does not travel without the launcher. The two
applications this work is aimed at — wildfire observation and response, and cargo delivery to
places without a runway — need the aircraft to arrive somewhere that has no infrastructure, and
to leave again.

So the requirement is: **the aircraft carries everything it needs to depart and recover, and the
site supplies no prepared launch or recovery infrastructure of any kind.** The ground is the only
thing the site provides, and it provides it unprepared. A net, a catapult, a cradle, a prepared
strip or a recovery vehicle each fail that test — including the ones that fail it only on the
recovery half.

### How the configuration meets it

The aircraft stands on its tail, with its longitudinal axis vertical, in its own storage
attitude. **No launch equipment is present.** It rests on five points: the four lower ends of
the tip frames and the aft end of a keel running along the centreline.

**Those five points are not added hardware.** The tip frames are the landing structure, they are
also the structure that carries the attitude propellers and sets their moment arm, and their
fairing is the aircraft's only vertical surface. **One structure serves four purposes and is
charged to the mass budget once** — Section 8 gives the fairing's sizing.

**The saving has precedent and it is not this paper's observation.** Reviewing the tail-sitters
of the 1950s, NASA recorded that *"dispensing with a conventional landing gear improved the
empty weight fraction for these VATOL aircraft"*, while noting that some form of gear was still
required on the tail surfaces. The present arrangement takes that benefit and extends it by
giving the same structure the control duty as well.

**And the stance base is a parameter rather than a constraint.** Moving the frame ends further
outboard widens the base against ground wind without altering the planform, the propulsion or
the control architecture — and because the same displacement lengthens the control moment arm,
both benefits arrive from one change. The reference geometry is one point on that trade; an
operator with a stronger ground-wind requirement can take another.

### What is sized, and what is not demonstrated

This is the part of the section that decides whether the rest of it can be trusted.

**Sized.** The vertical phase is sized: hover power from momentum theory at thrust equal to
weight, the buffer that supplies the difference between that peak and the cruise demand, the
tip-frame lengths that set both the stance base and the control arms, and the structure that
carries the landing loads. Those numbers exist and Section 10 reports **whether** they close, and
with what margin. This section does not assert the outcome of a calculation it does not contain.

**Not demonstrated, and the list is not short.**

**The aircraft leaves the ground on its control propellers.** Hover power is sized at thrust
equal to weight, so the primary propulsor supplies a thrust-to-weight ratio of exactly one and
no more. The take-off margin comes from the four tip pairs, which were sized from the moment
requirement rather than from weight support. That is the one place the configuration asks a
component to do a second job it was not sized for, and it means the take-off margin and the
attitude authority are drawn from the same four propellers and compete for it.

**The vertical descent has not been analysed.** A rotor descending into its own wake can enter
the vortex ring state, in which thrust becomes erratic and adding power makes matters worse.
Whether this configuration's descent profile enters that region, and at what rate of descent,
is an open question in Section 14 rather than an answered one here.

**Neither has the landing transition.** The forward rotation and the reverse are not symmetric
and must not be assumed to be. Going out, the rotation builds dynamic pressure while it turns,
so lift arrives to replace the vertical component of thrust as that component falls. Coming
back, the race runs backwards: dynamic pressure is falling while the aircraft is being turned,
so lift is leaving at the moment the thrust vector has not yet returned to vertical. **A model
built for the first case cannot be read for the second by changing a sign, and no figure in this
paper describes the landing transition.**

**Hover attitude control is sized but not demonstrated as a closed loop.** The moments available
about each axis are computed, but no control allocation has been closed around them and nothing
has been simulated or flown. That gap is wider than it looks, because this configuration
deliberately declines a control channel that comparable aircraft use: the two rotors of a coaxial
pair could be run at different speeds to produce a reaction torque about the body's longitudinal
axis, and here every pair is operated torque-balanced instead, leaving that axis to the strip.
**What that refusal costs in authority and in response time is not computed**, and Section 14
carries it.

**And one historical difficulty is inherited rather than removed.** A tail-sitting aircraft on
the ground is more exposed to crosswind than a conventional one. The stance base is the answer
this configuration offers, and it is a parameter rather than a proof.

### What the historical record does and does not give back

One of the 1954 objections is genuinely removed and it should be named exactly. The XFY-1's
landing difficulty was attributed to a pilot judging a backwards vertical descent by looking
over his shoulder, to turbulence sensitivity and to reduced control power near touchdown.
**There is no pilot here, and height above ground is a sensor measurement rather than a human
estimate.** That disposes of the spatial-orientation objection and nothing else. **Precise
hovering, ground gusts and the descent itself are not disposed of by removing the pilot**, and
this section does not pretend otherwise.

### What this half costs

Runway independence is not obtained free, and the charges appear later rather than here. The
tip frames that make the aircraft self-supporting are structure standing in the cruise
airstream, and Section 11 charges their drag. The attitude propellers they carry are exposed
for the whole cruise and cannot be feathered, and Section 11 charges that too. The buffer that
releases the engine from the hover peak is mass carried for the whole flight.

**The second half — cruise carried on a wing rather than on rotors — is the subject of the next
section**, and the two are combined in Section 7.

---

## The second half: cruise carried on a wing

### The opponent, and the axis

On this axis the alternative is the multirotor, and as in the previous section the comparison
runs one way only. **Nothing here is claimed against fixed-wing aircraft.** A runway-launched
aeroplane cruises more efficiently than this configuration and pays none of the charges of
Section 2; that comparison is not made, and no result in this paper rests on it. The claim is
confined to the one thing the multirotor family structurally lacks: **a surface that carries the
cruise lift.**

### What the requirement is

Section 5 established the first half: the aircraft must leave from and return to a site that
supplies nothing. **A multirotor meets that requirement completely.** It is not a deficient
machine and this section does not treat it as one; it is excellent at what it does and is
limited by the price of doing it that way.

What it does not meet is the second half of both missions. Wildfire observation and response,
and cargo delivery to places without a runway, each require the aircraft to **cover distance
after it has left the unprepared site**, and a vehicle with no wing buys every second of that
distance with installed power. The consequence has been stated independently: surveying the
field, one study concludes that multirotors are efficient in hover and suited to short-range
missions, while vectored-thrust aircraft are efficient in cruise and suited to long-range ones.

### What the configuration does instead

**Cruise lift is carried by the airframe itself.** There is no separate fuselage: the whole
planform is the wing, so every part of the body that is carried is also a part that lifts. At
the cruise condition the lift coefficient follows from `C_L = W/(qS)`, the drag from
`C_D = C_D0 + C_L²/(πARe)`, and the nose pair is left with one job — producing the thrust that
balances that drag. It supports none of the weight.

That is the whole of the difference, and it is worth stating in those plain terms because the
consequence is structural. **A multirotor's discs must produce the lift and the propulsive force
together, throughout cruise.** This aircraft separates them: a surface holds the aircraft up and a
propeller pushes it along, and **the wing produces its lift without a separate continuous power
supply of its own** — the power the aircraft spends in cruise goes to overcoming drag, of which
the lift's share is the induced part.
Lift is carried on a surface or it is carried on rotors, and no sizing contract, no assumption
in this paper and no choice available to a designer moves a vehicle between those two states.

**But the size of the resulting advantage is a calculation, not a consequence of that
statement**, and the two must not be run together. The rest of this section is the calculation,
and it gives a smaller number than the structural statement invites.

### What the margin actually is, in one currency

The sizing set of Section 4 reports an **effective lift-to-drag ratio**, defined in its own
nomenclature as `L/De = WV/P`: weight times speed over power. That is a system figure of merit,
not a force ratio, and it already contains the propulsive efficiency of whatever produces the
thrust. **A force ratio cannot be placed beside it.**

Converting this configuration's aerodynamic ratio into the same quantity is one line: in level
cruise thrust equals drag and lift equals weight, so with shaft power `P = DV/η_p`,

> **L/De = WV/P = (L/D) · η_p**

**Which power `P` denotes is not assumed here**, because reading it as electrical power rather
than shaft power would make this configuration's figure incomparable with the published one. The
source settles it in its hover formulation: hover power is written `Ph = W√(W/2ρA)/FM`, with the
figure of merit already applied — shaft power — and the propulsion-system efficiency applied
separately outside it. The cruise formulation uses the same separation, writing cruise energy as
`Pc/ηc` with `Pc = WV/(L/De)`. That separation appears in the source's **battery-capacity**
derivation, so it holds for the all-electric entries as well as the shaft-driven ones: if `L/De`
already contained the electrical chain, that derivation would count it twice.

**Neither factor is a single number, and they are two different kinds of spread.**

The aerodynamic ratio is **8.79 to 10.82**, with the tip frames and the free-wheeling attitude
rotors already charged. That spread is **uncertainty**: it is the zero-lift drag bracket, and a
designer does not get to choose where in it the real aircraft lands.

The cruise propeller efficiency is **0.632 to 0.683** across the nose-blade families that meet
the hover figure of merit — two and three blades per rotor, at two target section lift
coefficients, each solved at its hover and its cruise condition. That spread is **not
uncertainty**: it is a design variable this study has not fixed.

| L/De | η_p 0.632 | η_p 0.683 |
|---|---:|---:|
| **L/D 8.79** (adverse drag) | 5.56 | 6.00 |
| **L/D 10.82** (favourable drag) | 6.84 | 7.39 |

**These are the bounding corners of a product, not four simulated aircraft.** Two readings follow
and both are given, because choosing between them requires something this section does not have:

- **Examined envelope, 5.56 to 7.39.** These are the bounding combinations permitted by two
  independent model inputs. **They are not four demonstrated aircraft states**, and nothing here
  shows that a built aircraft would land simultaneously on both bounds.
- **Best examined blade family, 6.00 to 7.39.** The highest efficiency among the families
  examined is 0.683; holding it and sweeping only the drag bracket gives this range.

**Whether 0.683 is the blade a designer would actually choose is not settled here**, and saying
so is the point. It is the best of the four *on cruise efficiency under the hover figure-of-merit
constraint*. Blade count and section loading also govern structural loads, acoustics, the motor
operating point, rotor inertia and manufacture, and **none of those is modelled in this work**.
Section 10 is where one blade is carried into a closed sizing loop; until then this section stays
at envelope level and does not present any corner as the aircraft's performance.

### What the comparison gives, against both published quadrotors

The sizing set contains two quadrotors for the same mission, and **neither is treated here as the
primary one.**

| | L/De | vs examined envelope 5.56 – 7.39 | vs best examined family 6.00 – 7.39 |
|---|---:|---|---|
| Quadrotor, turboshaft | 4.9 | +13 % … +51 % | **+22 % … +51 %** |
| Quadrotor, all-electric | 5.8 | −4 % … +27 % | **+3 % … +27 %** |

**Against the turboshaft quadrotor the sign holds at every corner of both readings.** Closing it
would need the propeller efficiency to fall to 0.557, against 0.632 for the least efficient blade
family examined.

**Against the all-electric quadrotor it does not hold at the low corner**, and that result is
reported as a result rather than as a caveat. That vehicle reaches 5.8 — above this
configuration's 5.56 — and it buys the difference with 1 742 lb of battery and nearly twice the
gross weight for the same mission, 7 221 lb against 3 678 lb. **That higher gross weight is
consistent with the mass charge Section 2 describes**, and Section 4 is where the independent
sizing evidence for it is set out — the comparison in this table does not establish the causal
link by itself. On cruise efficiency taken alone, the entry is ahead of this configuration's low
corner, and whether it is ahead of the best examined blade family depends on the drag bracket.

**So the second claim is narrower than the structural statement invites.** Carrying cruise lift on
a wing is worth **roughly a quarter to a half against the turboshaft reference, and against the
all-electric one it ranges from slightly behind to comfortably ahead depending on the drag outcome
and the blade** — a measurable advantage, not a change of category. And what
compresses it is not the wing. **It is this aircraft's own refusal of the variable-pitch hub:**
at a propeller efficiency of 0.85 the same airframe reaches 7.47 to 9.20. Section 11 charges it
there.

### Five qualifications, and every one of them runs against this configuration

They are given together because omitting any one of them would make the comparison look better
than it is.

**Scale.** The compared vehicles are 1 670 to 3 275 kg; the designs here are of order 50 kg and
1 000 kg — Section 10 closes the light one between 52 and 58 kg across the same bracket.
Reynolds number favours the larger aircraft, so the smaller design is at a disadvantage in this
comparison rather than an advantage.

**The quadrotor is a good quadrotor.** Its disc loading is 3.5 lb ft⁻², which is unusually low
and unusually efficient. Nothing here is compared against a poor example.

**The speeds are not matched, and the direction of that mismatch is calculable.** The published
figure is quoted at the best-range speed; this configuration's is at its chosen cruise condition,
1.49 times stall, which Section 10 states explicitly is **not** its best lift-to-drag point. The
best point lies at 1.26 times stall, and `L/D_max = 0.5√(πARe/C_D0)` exceeds the cruise ratio at
both ends of the drag bracket — 11.65 against 10.82, and 10.08 against 8.79, both at e = 0.817.
**The reference is
therefore given its best speed and this configuration is not given its best speed, and the margin
is positive anyway.** The best point is not an available option — cruising there leaves too little
margin above the stall — so this fixes a direction, not a magnitude.

**The atmospheres are not matched.** The published sizing mission is flown at *"5,000-ft altitude
and ISA + 20°C"*; every number in this work is at sea level, with a sea-level drag polar and a
sea-level blade solution. **The direction of that mismatch is not claimed here**, because it has
not been computed: the altitude sweep in this work measured the effect on hover power and on
propeller efficiency, not on a cruise comparison at a re-trimmed best-range speed.

**The analysis chains are not matched, and this is the qualification that bounds what the
comparison can be called.** The published value is the output of an integrated conceptual-design
system with a comprehensive rotor analysis behind its rotor performance. The value here is
assembled from a drag build-up, a drag polar at a prescribed cruise condition, and a separate
blade-element propeller solution. There is a second difference inside that one: **the published
value is the effective ratio of a fully sized vehicle, while the value here is a converted
performance metric at a prescribed cruise condition, taken before the sizing closure Section 10
reports.** So this is a comparison of two independently produced figures in a common definition,
not a controlled numerical reproduction, and nothing in it should be read as validation of either,
or as a completed aircraft-level comparison.

### What is sized, and what is not demonstrated

**Sized.** The drag build-up and its bracket; the lift-to-drag ratio at the cruise condition
from the drag polar; the propeller efficiency from blade-element momentum theory at two
operating points; and the range that follows from the chain, link by link.

**Not demonstrated.** **No part of this has been measured.** There is no wind-tunnel test and no
flight test in this work, and the drag coefficient is a build-up with a declared bracket rather
than a measurement. The planform's sweep, taper and thickness distributions were chosen rather
than optimised. **The span efficiency used throughout this section is the computed value, 0.817,
not the assumed 0.85** — a vortex-lattice solution of the trimmed planform, and 3.9 percent below
the assumption, so the lift-to-drag figures above carry the calculated penalty rather than the
optimistic estimate. And **for the methods used here, and for the published
comparisons against which they were checked, the aerodynamic predictions diverge above roughly ten
degrees of incidence**: three methods of three fidelities depart at the same place, the highest of
them against wind-tunnel measurement. That is a statement about these methods on this class of
configuration, not about what any method could achieve. It does not touch the cruise numbers
above, which sit at a few degrees, but it bounds what this section may be read to support.

### What this half costs

The wing that makes cruise efficient is carried through the vertical phase, where it produces
nothing and presents the aircraft's largest surface to ground wind. The tailless planform that
follows from having no boom constrains the sweep, because with no horizontal stabiliser the
pitching moment must come from the distribution of lift along the body itself. And the
fixed-pitch propeller that serves both regimes is the reason the margin above sits where it does
rather than higher — at e = 0.85 the same airframe would reach 7.48 to 9.20. Section 11 charges all three.

**The two halves are now on the table separately. Section 7 is where they are combined**, and
the combination is what this paper is for.

---

## The combination

None of the three elements is new.

Tail-sitting aircraft were flown in the 1950s and are ordinary among uncrewed aircraft today,
including with blended-wing-body planforms and contra-rotating propulsion. Blended wing bodies
have been a standing subject of transport research for three decades. Series-hybrid propulsion
has established precedent in small uncrewed aircraft. **Each can be found on its own, and in
combination, in the literature and in hardware** — Section 1 says where.

**What this paper contributes is that combination, the condition its primary propulsor is designed
to satisfy, and the price the configuration pays for pursuing it.** The three elements, taken together, meet the escape condition
of Section 3 **in the propulsor that carries the aircraft**, and they meet it with no mechanism
that reorients a propulsor. The assembly is not offered as novel because it is an assembly. It is
offered for what it satisfies, and for what it does not need in order to satisfy it — and Section 1
has already set out how much of the ground is occupied.

**The qualification in that sentence is not decoration, and it is made here rather than
conceded later.** Section 3 lists partial instantiation among the ways an architecture can fail
the condition: meeting it where the aircraft is carried and failing it elsewhere. That is this
configuration's own case. The single nose pair meets all four parts — same hardware, both duties
served, one orientation, hover peak from a buffer. The four attitude pairs do not: they are exposed
in the cruise flow and they cannot be feathered, so they re-open the second charge. **The
instantiation is therefore partial**, and reporting what the failing part costs is a substantial
share of what Section 11 does.

The condition asks for one set of hardware to serve both regimes in one orientation,
with the hover peak drawn from a buffer. Each element supplies one part of it, and none
of them supplies it alone:

- The **blended wing body** carries the cruise lift on a surface, so that cruise is
  wing-borne rather than thrust-borne. That is the second half of the union.
- The **tail-sitting stance** aligns the thrust axis with the body axis, so the propulsor
  that produces the thrust for vertical operation is the same one that produces the cruise
  thrust, holding
  one orientation relative to the airframe throughout. There is no dedicated lift system to
  carry, and vertical operation does not depend on a runway. That is the first half.
- The **series-hybrid buffer** releases the continuous power plant from the hover peak,
  so that it is sized by cruise rather than by a condition holding for about two percent
  of the flight.

The change of regime is then made by **rotating the airframe**. The propulsors hold
their orientation relative to the body from take-off to cruise; what changes is the
orientation of the body relative to the flight path. A tilting architecture reaches the
same end by turning its propulsors instead, which requires a pivot and an actuator and
introduces gyroscopic coupling from the reorienting mass and a control problem through the
turn. It does not satisfy the condition as stated: the condition requires one orientation
relative to the airframe, and turning the propulsors is the case the condition excludes.
Here the end is reached by turning the thing the propulsors are already attached to, which
leaves the orientation requirement intact.

That single move is what removes the mechanism. **The table below counts mechanism classes that
exist in order to change regime, or to take a rotor out of one regime's flow**, which is why no
aerodynamic control device appears in it: the strip of Section 8 is a control surface, not a means
of changing regime, and counting its absence would be counting the wrong thing. The configuration therefore carries:

| Mechanism | Where it is required | Present here |
|---|---|---|
| Pivot or tilting joint | Tilting architectures | — |
| Nacelle or rotor-group actuator | Tilting architectures | — |
| Variable-pitch hub | Architectures that trim a rotor across two widely separated operating points, or feather a rotor unused in one regime | — |
| Dedicated lift rotors | Lift-plus-cruise architectures | — |
| Rotor stowing, indexing or stopping mechanism | Architectures that remove dedicated lift rotors from the cruise flow by such means | — |

Attitude is produced instead by differential thrust between fixed-pitch propellers: a
single coaxial contra-rotating pair at the nose, and four small coaxial pairs at the
ends of the tip frames, whose moment arms give pitch and yaw directly. The tip pairs are
sized from the moment requirement rather than from weight support, but the thrust that sizing
gives them also supplies the aircraft's entire take-off margin, because the nose pair is sized
at thrust equal to weight and no more. That is the one place the configuration asks a component
to do a second job it was not sized for; it is a dependency, it is reported as one where the
sizing is audited, and it does not make the tip pairs a dedicated lift system.

**The claim is narrower than it may appear, and the boundary matters.**

This is not a configuration in which nothing moves. Roll cannot be produced by the
propellers' **thrust**: every thrust vector is parallel to the body axis, so no combination
of thrust settings produces a moment about that axis. It **could** be produced by their
**reaction torque** — each rotor carries its own electrical machine, and running the two
rotors of a coaxial pair at different speeds leaves a net torque about the body axis, which
is a channel the tail-sitter literature uses. This configuration declines it: every pair is
operated torque-balanced, so no reaction torque is spent on control, and the axis is assigned
to an aerodynamic device instead. That is a design constraint, not a physical impossibility,
and what declining it costs is not counted here. The device is the only moving aerodynamic
surface on the aircraft — a variable-extension strip on the lower surface, modulated rather
than switched, which also pitches the nose down by a small increment when it is deployed. The
strip is part of the configuration and is named here rather than later, because a claim about
eliminated mechanisms that omitted it would be false.

Nor does a fixed-pitch propeller serve two regimes for nothing. The nose pair holds one
orientation, which is the architectural claim, but it also holds one blade geometry across a
hovering condition and a cruising one, and no single fixed-pitch blade is at its best in both.
That is a price of refusing the variable-pitch hub rather than an argument against refusing it,
and it is charged in Section 11 with the other costs of the union, not settled here.

Nor is this a claim of mechanical simplicity. Part count, mass, failure modes and
maintenance burden were not measured, and nothing in this work supports a statement
about reliability. What is offered is a **count**: the classes of mechanism that a
tilting architecture requires to change regime, and which this arrangement does not
require. The actuator inventory that replaces them is the propulsion motors together
with the strip.

**One thing this section does not establish, and Section 9 holds it to that.** The arrangement
described here requires no mechanism to change regime. **Whether this aircraft can actually perform
the change is a separate question and is not settled anywhere in this paper**: whether the moment
available is sufficient, and whether the aircraft trims through the rotation, depend on
aerodynamics that — for the methods used here and the published comparisons against which they were
checked — are not reliable above roughly ten degrees of incidence, which is inside the band the
rotation passes through. **The mechanism claim is about hardware and survives that limit. The
transition claim is not made.**

What the combination costs is the subject of the sections that follow. It is not free:
the attitude rotors that make the union controllable are themselves exposed in cruise,
and Section 11 charges them.

---

## What it is made of, and what still moves

Section 7 claimed that a class of mechanism is absent. A claim of that kind is only as good as
the inventory behind it, so the inventory is given here in full, including the parts that move.

### The airframe

The entire airframe is the wing. There is no cylindrical fuselage: every part of the planform
carries payload and produces lift. Leading-edge sweep varies continuously along the span while
the trailing edge is held at 25°, so the realised sweep runs from 45° at the root to 38.3° at the
tip — a variation of under seven degrees, with the crescent character coming from the curvature of
the leading edge rather than from a large change in sweep. Thickness runs from 25 % of chord at
the root to 12 % at the tip, and chord from 0.970 m to 0.236 m. For the light design the span is
3.453 m, the wing area 1.979 m², and the aspect ratio 6.03.

Sweep is not a free parameter here, and the reason is structural to the configuration rather than
aerodynamic preference. The aircraft is tailless. With no horizontal stabiliser on a boom, the
pitching moment must come from the distribution of lift along the body itself, and sweep is what
places the outboard sections behind the centre of gravity so they can produce it. **The sweep
angle and the longitudinal stability are one design variable seen from two directions.**

### The propulsion

**Five propeller stations, ten rotors:** every station is a coaxial counter-rotating pair. The
reason is narrow
and worth stating as such: **reaction torque.** A single propeller applies to the airframe a
torque equal and opposite to the one it applies to the air. It acts about the propeller axis,
which on this aircraft is the body's longitudinal axis — the roll axis in body terms — in both
regimes, and it must be opposed continuously, either by a control surface, which costs drag, or by
differential thrust, which costs a control channel. A counter-rotating pair does not produce it.

One pair sits at the nose, 1.20 m in diameter on the light design, and produces all propulsive
thrust in both regimes. Four smaller pairs, 0.20 m in diameter, sit at the ends of rigid frames
projecting from the wing tips. Every pair is of **fixed geometry**: no cyclic pitch, no
collective, no variable-pitch hub and no mechanism that changes a rotor's orientation relative to
the airframe. Shaft speed is commanded; blade geometry and orientation are not. Each rotor of each
pair is driven by its own
electric machine on a common axis, so **the splitting gearbox and the mechanical governors that
synchronise it are not required** — the arrangement that repeatedly defeated the XB-35. This work
makes no claim about the shafting: whether the two machines are stacked on the axis or arranged
some other way is an implementation question it does not settle.

The counter-rotating arrangement carries a second consequence that the transition analysis
depends on. Because the two rotors of each pair carry equal and opposite angular momentum, **the
net angular momentum of the propulsion system is nominally zero**: rotating the airframe through
ninety degrees precesses nothing, and no gyroscopic moment appears for the control system to
cancel. In a tilting architecture that term is present and must be designed for.

### The energy path

A series hybrid: fuel to engine, engine to generator, generator to electric machines at the
rotors. The engine is not mechanically connected to any rotor. It is an energy source, and that
decoupling is what allows it to be sized by cruise rather than by hover.

**The separation the architecture depends on is that the continuous cruise requirement is several
times smaller than the hover peak, and that the difference is supplied from a battery buffer for
the vertical phase alone.** No wattage is quoted here. The figures published for this configuration
were closed on a propeller efficiency this work has since replaced with a computed one, and the
re-closed set belongs to Section 10 rather than to an inventory. **Quoting the superseded numbers
beside a propulsion section that no longer assumes them is precisely the inconsistency this paper
is trying not to commit.**

### What produces each moment

**Pitch and yaw come from differential thrust between the tip pairs**, and the two axes do not
have the same moment arm. The frames project ±0.71 m perpendicular to the planform, so a
differential between the upper and lower pairs acts at 0.71 m in pitch, while a differential
between the left and right pairs acts at the semi-span, **1.726 m — 2.43 times the pitch arm.**
The yaw arm is therefore the larger by that factor, which is the reverse of the usual situation
and is a consequence of the layout rather than a design choice. What authority each axis
actually has depends on the available thrust differential and on allocation as well as on the
arm, and is not settled by the ratio alone.

**The same differential-thrust system is what is assigned to rotate the airframe through
transition.** That is a design assignment, not a demonstrated result: whether the moment it
produces is sufficient, and whether the aircraft trims through the rotation, are **not settled in
this paper**: the moment is a sizing input to Section 10, but the trim through the rotation depends
on the transition aerodynamics, and Section 14 says why those are not currently reliable for anyone
on this class of configuration at the incidences the rotation passes through.

**Roll comes from neither, and the reason is a choice rather than an impossibility.** Every thrust
vector is parallel to the body axis, so no combination of thrust settings produces a moment about
it. Reaction torque could produce one: each rotor has its own machine, so running the two rotors of
a pair at different speeds leaves a net torque about that axis, and the tail-sitter literature uses
exactly that channel. **This configuration declines it** — every pair is operated torque-balanced,
so no reaction torque is spent on control — and assigns the axis to an aerodynamic device instead.
What declining it costs is not counted in this work. Roll is produced instead by a strip on the
lower surface: inclined at 45° in planform, running 120 % of
root chord, reaching 67 % of semi-span, and standing 2 cm proud at its inboard end and 6 cm at
its outboard end. **Extension is the control variable** — the strip is modulated, not switched —
and deploying it also pitches the nose down by a small increment. Its inboard 46 % lies inside
the nose propeller's slipstream, where dynamic pressure is set by disc loading and is therefore
available at zero airspeed; its outboard 54 % works against the freestream in cruise. That split
is why one device serves both regimes.

### What meets the ground

The aircraft rests on five points: the four lower ends of the tip frames, and the aft end of a
keel running along the centreline. It stands on its tail in its own storage attitude, with no
launch equipment present.

**The frames carry a fairing, and it is not only a drag measure.** The frames are the only
surfaces standing perpendicular to the wing plane, and a planar planform supplies no directional
stability at all, so the fairing is also the only vertical surface the aircraft has. Sized
against the criterion the tailless literature recommends — C_n_β greater than 0.001 per degree —
the chord required over the combined frame length is **39 mm**, against the 50 to 70 mm that a
20 mm faired strut carries in any case. Directional stability on this configuration therefore
does not ask for a surface; it asks for a fairing on a frame that is already there.

**One part is not airframe and is easy to omit from a list of this kind: the flight control
system.** The stability of this configuration is not airframe-borne — it is produced by
differential thrust and by the strip, both of which are actively commanded — so an attitude
reference and a flight computer are not optional equipment but part of the mechanism the
preceding paragraphs describe. They are carried in the systems budget. The configuration
replaces a pilot's workload with computation, and the computer is the part that does it.

**The tip frames therefore do four jobs at once**, and this is the clearest instance in the
configuration of one structure carrying several duties: they are the landing gear, they set the
control moment arms, they carry the attitude rotors, and — through the fairing described above —
they are the aircraft's only vertical surface. Lengthening them to buy control
authority widens the stance base against tipping in wind at the same time. They are also the
structure that is exposed in cruise, and Section 11 charges them for it.

### What moves

The propellers rotate, as propellers do, and their shaft speed is commanded; but none of them
changes its orientation relative to the airframe, or its blade pitch, at any point in the flight.
**Beyond the propellers' rotation, one thing on this aircraft changes its configuration: the
strip.**
It is described as deployable in two halves — one side alone for roll, both together as a speed
brake. The actuator inventory is therefore the propulsion motors plus the strip's actuation.
**How many actuators that is, this study does not fix.** The systems budget carries the
actuation without sizing the mechanism, and naming a number here would be inventing one.

### What this inventory does not settle

Two items belong here rather than in a later list, because both are properties of the hardware
just described.

**An untrimmed hover torque, with no trim mechanism identified.** This is a control question
rather than a property of the hardware, and it is stated as one.

The torque balance within each pair is set exact at the cruise condition rather than at hover, so
a small residual remains in hover. It acts about the propeller axis — the aircraft's longitudinal
axis, which is the roll axis in body terms. *(This paper fixes body-axis naming throughout. That
axis is the roll axis in both regimes; what changes is its orientation relative to the earth — it
stands vertical in the hover attitude, where a moment about it appears as a change of heading, and
horizontal in cruise, where it appears as a bank. The two conventions are not mixed here.)*

That axis is the one the configuration has chosen not to command with the propellers, which is why
the residual is awkward: the tip pairs cannot absorb it by thrust differential, because their thrust
vectors are parallel to that axis too, and the strip works against dynamic pressure that the
slipstream supplies over only part of its length at zero airspeed. What is left is the channel the
configuration set aside — the speed trim of the pairs, which is a reaction-torque command and not a
thrust one. Either the residual is small enough to be absorbed that way, which this study has not
shown and which would mean the architecture spends a little of the channel it declined, or a fourth
duty falls on the strip.

**The fixed geometry of the tip pairs leaves two admissible cruise states, and only one of them
is physically closed.** Unable to feather, the pairs must either turn at the zero-shaft-torque
condition or be stopped, and the difference between those two states is a substantial fraction of
the aircraft's zero-lift drag. Both ends are computed rather than assumed and the charge appears
in Section 11.

**These are the parts that fail the escape condition**, and naming them here is the point of
listing them. The nose pair meets all four parts of Section 3. The tip pairs meet none of the
first three: they are carried through cruise producing moments rather than thrust, so they fail
the second row of Section 3's table, and they are exposed while doing it. This is the partial
instantiation Section 3 lists as its **fourth** failure mode — meeting the condition where the
aircraft is carried and failing it elsewhere — and the charge it re-opens is the second, carried in
Section 11. *(They are not the second row of Section 3's table: that row concerns a propulsor that
lifts and is then carried, and the tip pairs do not lift. They produce moments, and Section 3's
permitted-cost clause places attitude devices outside the first charge while leaving them in the
airstream.)*

The free-wheeling state is physically determinate: the rotor settles where net shaft torque is
zero. **The stopped state is not.** Stopping a rotor requires the stop to be produced by
something — motor holding torque, an electrical brake, a mechanical lock — and a stopped
fixed-pitch blade also has an azimuth, so "stopped" is a family of aerodynamic states rather than
one. Neither the means nor the azimuth is fixed by this study, and the drag figure quoted for the
stopped condition should be read as the state Section 11 defines rather than as the state a
particular installation would reach.

---

## What is not claimed

This section states the boundary of the paper's claims. It is placed before the configuration's
own numbers because a boundary drawn after the results would be a retreat, and one drawn before
them is a commitment.

**It is not a list of the study's open questions.** Those are in Section 14, and the difference
matters: the boundary below is about claims the paper **declines to make**, most of which it
could not make on any evidence; Section 14 is about questions the paper **does not answer**, and
which better evidence would answer. One is a scope; the other is a debt.

### The claims are made on four axes, against four different opponents

The boundary is easiest to state as a consequence of the claim structure rather than as a list
of denials, so the structure comes first. Comparison is only meaningful against a named
alternative, and this paper's alternatives differ from axis to axis.

| Axis | Opponent | Status |
|---|---|---|
| Cruise efficiency | Multirotors | **Claimed, and bounded.** Cruise lift is carried on a surface rather than on rotors, which no sizing contract changes. The *size* of the resulting advantage is a calculation, not a consequence of that fact, and Section 6 measures it against two published quadrotors in one common definition. |
| Operation without a runway | Fixed-wing aircraft | **Claimed**, in the sense stated below. |
| The mechanism required to change regime | Tilting architectures | **Claimed.** This is the paper's contribution. |
| Cruise efficiency and range | Other hybrids — lift-plus-cruise, tilt | **Not claimed, in either direction.** |

**The fourth row is the important one**, and the reason it is a refusal rather than a result is
the paper's own central finding: against the other hybrids the ranking depends on the sizing
contract, and it reverses across the three contracts reported in Section 13. A paper that
quoted one of those orderings as a result would be reporting its own choice of contract. **No
range claim is made against the tilting or lift-plus-cruise families in either direction**, and
a reader who finds one implied anywhere in this paper should treat it as an error rather than
as a claim.

### What each claim does not depend on

A reader who rejects one of these claims should be able to see immediately which of the others
survive, and the dependencies are short enough to list.

| Claim | Does not depend on |
|---|---|
| Operation without a runway | the drag bracket, the propeller efficiency, the battery gap, the transition aerodynamics |
| Cruise lift carried on a surface | the sizing contract, the transition aerodynamics |
| The **size** of the cruise-efficiency margin | — it depends on both the drag bracket and the blade family, and Section 6 reports it as a range rather than a number |
| Elimination of the propulsor-reorientation mechanism class | the drag bracket, the sizing contract, the range result, **and the transition aerodynamics** |

**The last row carries a distinction that matters more than the others.** The mechanism claim is
a statement about what hardware is present, and it is settled by the inventory in Section 8. **The
separate claim that this aircraft can actually perform the regime change is not settled**, and it
depends on exactly the aerodynamics that Sections 6 and 14 describe as unreliable above roughly
ten degrees of incidence — the band the rotation passes through. **Section 7 should be read under
that limit**: it describes an arrangement that requires no reorienting mechanism, not a
demonstration that the arrangement transitions.

### One cost of the contribution that is named and not priced

The mechanism claim has a price this work does not compute, and it belongs here rather than only
in Section 1.

**This configuration declines a control channel that comparable aircraft use.** The two rotors of
a coaxial pair have independent machines and could be run at different speeds, producing a moment
about the body's longitudinal axis; the tail-sitter literature uses exactly that. Here every pair
is operated torque-balanced instead, and the axis is assigned to the strip. **What that refusal
costs — in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia —
is not computed anywhere in this paper.** The claim is that the mechanism class is eliminated.
**Whether eliminating it is favourable on balance is a question this work does not settle**, and
quantifying it would require a control-allocation study rather than a single torque figure.

### Eight things this paper does not claim

**1. It does not claim range against fixed-wing aircraft.** The vertical axis is where the
fixed-wing family is the opponent; the range axis is not. A runway-launched aircraft that never
claimed vertical capability pays none of the charges of Section 2, and nothing here competes
with it on distance.

**2. It does not claim vertical capability against multirotors.** That comparison runs the other
way and would be absurd. The multirotor family is the opponent on cruise efficiency only.

**3. It does not claim that the aircraft has no moving parts.** What is eliminated is a *class
of mechanism* — the one that reorients a propulsor. The aircraft has a moving aerodynamic
surface, it is named where the elimination is claimed rather than later, and it also pitches the
nose down when deployed.

**4. It does not claim mechanical simplicity.** Part count, assembly mass, failure modes and
maintenance burden were not measured, and nothing here supports a statement about reliability.
What is offered is a **count** of mechanism classes that a tilting architecture requires to
change regime and that this arrangement does not. A count is not a reliability argument, and
readers who convert one into the other are not quoting this paper.

**5. It does not claim that the escape condition is fully instantiated.** The condition is met
in the propulsor that carries the aircraft and is not met in the attitude system, which is
carried through cruise producing moments rather than thrust. Section 3 names that case as
partial instantiation, and the charge it re-opens is reported rather than absorbed.

**6. It does not claim that satisfying the condition makes an aircraft better.** The condition
concerns three specific charges. A configuration may avoid all three and still be unbuildable,
uncontrollable, or unsuited to its mission, and the accounting says nothing against that
possibility.

**7. It does not claim that the trades inside the escape are favourable.** Moving the hover
peak onto a store converts a power-system charge into a mass one; serving two regimes with one
set of fixed-geometry propellers costs efficiency in at least one of them. Both are computed,
neither is asserted to be worth paying, and the ledger reports them whichever way they fall.

**8. It does not claim that the aircraft flies.** The design *sizes* vertical operation and the
transition; it does not demonstrate either. No aircraft has been built, no wind tunnel has been
run on this geometry, and the transition analysis is a calculation whose assumptions are stated
where it appears. **"By construction" throughout this paper means "by the sizing", never "by
demonstration."**

### What the claims that remain amount to

Removing those eight leaves something narrower than a first reading of the abstract might
suggest, and the narrower statement is the one the paper defends: **a configuration that
combines runway-independent vertical operation with wing-borne cruise efficiency, reaches that
combination with no mechanism that reorients a propulsor, and reports what the combination
costs.**

Each half of that has a named opponent and neither half is a record. **Nor is the configuration
claimed to be without precedent**: Section 1 sets out what is already established, including
uncrewed tail-sitters, tail-sitters without control surfaces, coaxial contra-rotating
tail-sitter propulsion, and blended-wing-body tail-sitters. **What this paper offers is the
combination, the consequences of the choices inside it, and the accounting** — which is what
Sections 7 and 8 describe and what Section 11 prices.

### One consequence for how the numbers that follow should be read

Because the comparative result depends on the sizing contract, **no comparison in this paper
should be quoted without the contract it was computed under.** That is not a caveat attached for
safety; it is the paper's own finding applied to the paper's own numbers, and Section 13 states
what it demands of anyone who uses the framework afterwards.

---

## Analytical closure of the sizing loop

**Closing a sizing loop mathematically is not the same thing as closing an aircraft
physically.** This section does the first. What it produces is a set of consistent numbers
on a declared set of assumptions: if the assumptions hold, these masses, powers and ranges
follow from one another without contradiction. Whether an aircraft can be built to them is a
different question, and Section 14 is where the answer is not yet yes.

### Why the loop has to be iterative

The pieces depend on each other in a circle. Installed power sets the mass of the propulsion
system; propulsion mass raises the take-off mass; take-off mass raises the power needed to
hover; and the hover power is what sizes the installed power. The closure statement is

> MTOW = m_payload / (1 − f_empty − f_energy)

and f_empty contains a term proportional to installed power, which contains a term
proportional to MTOW^1.5. **A fixed point is sought by iteration. If no fixed point exists, the
declared sizing package does not close** — which is a statement about that package rather than
about whether some other package could — and the calculation says so rather than returning a
number.

### The inputs, and why there are four closures rather than one

Two quantities entering the loop are not single values, and **they are not the same kind of
quantity**, which is why they are carried separately rather than merged.

**The zero-lift drag coefficient is uncertainty.** A consistent build-up places it between
**0.0285 and 0.0381**, with the same rotor term at both ends. A designer does not choose where
the real aircraft falls in that range.

**The blade family is a design variable this study has not fixed.** Four nose-blade families
meet the hover figure of merit, and their cruise propeller efficiencies span **0.632 to
0.683**. A designer would choose one; the criteria that would decide the choice — structural
loads, acoustics, the motor operating point, rotor inertia, manufacture — are not modelled
here, so the study carries all four rather than pretending to have chosen.

**The published zero-lift value of 0.0248 is not used.** The consistent build-up places it
below both ends of the bracket, so it is not a conservative choice or an optimistic one; it is
outside the supported range, and closing the loop on it would mean closing on a number this
work has shown it cannot support.

**Propeller efficiency enters the loop twice, and both entries move together.** It appears in
the range expression, and it appears in the cruise power that sizes the engine. Scaling one
without the other would size the engine on one propeller and compute the range on another, and
the loop would be internally inconsistent while appearing to close. Both terms are scaled
with the blade family in every closure reported here.

**The reference point is the aerodynamic lift-to-drag ratio, not the effective one.** The
effective ratio of Section 6 already contains the propeller efficiency; it is the currency in
which the multirotor comparison is made, and it is not an input to a loop whose own chain supplies
that efficiency separately.

**The sizing rules that keep that ratio valid as the mass moves are worth stating, because they
also say what the four closures are geometrically.** The loop holds **wing loading, disc loading
and aspect ratio** fixed, so area, span and disc diameter follow the mass: across the four
closures the wing area runs 1.98 to 2.27 m², the span 3.45 to 3.70 m, and the nose disc diameter
1.20 to 1.29 m. **The cruise lift coefficient is unchanged at 0.450 in every one of them**, so the
lift-to-drag ratio is an input that stays valid at the closed mass rather than one frozen at a mass
the loop has left behind. Had wing **area** been held fixed instead, the lift coefficient would
have risen with the closed mass, the induced term would have moved against the heavier closures,
and the drag corners would be optimistic as reported.

**Two things the loop does not scale, and a reader comparing this section with Section 8 should
know which is which.** The tip-frame length and the strip are not sizing variables here. They were
set on the reference geometry, and **the control moment arms of Section 8 are therefore reference
values that this closure does not re-derive.** Section 8 describes one aeroplane; this section
describes what its sizing rules give at four sets of inputs. **These are the same configuration at
four closed masses rather than four configurations** — but anything that depends on the arms is
carried at the reference geometry and is not an output of the loop.

**The drag polar is likewise a fixed input, and it is worth saying what that costs.** Chord grows
with area, so the chord Reynolds number rises about **7 %** across the closure range. On a
turbulent-flat-plate scaling, C_D0 ∝ Re^−0.2, that is a **1.4 %** change in the zero-lift
coefficient — against a bracket whose two ends differ by **34 %**. The polar is therefore not
re-solved per closure. **The claim made above is that C_L is unchanged, not that C_D0 is exactly
so.**

### The construction is checked before it is used

At the published assumption — the published drag coefficient with the rotor term omitted, and
the published propeller efficiency — the construction returns a take-off mass of **49.4 kg**
against the published 50.1, a cruise lift-to-drag ratio of **11.88** against 11.88, and a range
of **1 585 km** against 1 583. **The largest deviation is 1.5 percent**, in mass. The
construction reproduces the published aircraft, so the same construction run on the bracket is
reporting a change of inputs rather than a change of method. **This check is the only place in
this section where the published drag coefficient appears**; every closure reported below uses the
bracket.

### The four closures

**All four converge.** On these assumptions the analytical sizing loop closes for this
architecture — and for the **light** design, which is the only one carried through this loop; the
heavy design appears below only through a transition time computed elsewhere.

| | C_D0 | η_p | L/D | MTOW | Empty fraction | Hover power | Engine | Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** | 0.0381 | 0.632 | 8.79 | 57.5 kg | 0.614 | 12.53 kW | 5.17 kW | 927 km |
| **B** | 0.0381 | 0.683 | 8.79 | 55.8 kg | 0.607 | 12.17 kW | 4.65 kW | 1 002 km |
| **C** | 0.0285 | 0.632 | 10.82 | 53.5 kg | 0.597 | 11.66 kW | 3.91 kW | 1 141 km |
| **D** | 0.0285 | 0.683 | 10.82 | 52.3 kg | 0.592 | 11.40 kW | 3.54 kW | 1 233 km |

**Payload is an input, fixed at 13 kg; take-off mass is the output.** The closure returns 52.3 to
57.5 kg, and the payload fraction that follows runs from **0.25 down to 0.23**.

**The spreads are not alike, and the difference is the useful part.** *Spread here is
(max − min)/min, so every figure is auditable from the table above.*

| | spread across the four |
|---|---|
| Take-off mass | **9.9 %** |
| Hover power | **9.9 %** |
| Range | **33.0 %** |
| Engine rating | **46.1 %** |

**Engine rating is the most sensitive output in this envelope and mass is the least, and the
ordering follows from where each input enters.** Cruise power is W·V/(L/D)/η, so it carries the
drag bracket and the blade family directly — **and W is itself a closure output that has already
absorbed them through the mass loop.** Range carries them directly but escapes the mass feedback,
because the fuel fraction is fixed. Mass feels them only through the propulsion fraction, which is
a minority of the empty mass. **Only the engine is charged twice**, and that is why 46.1 percent
exceeds 33.0, which exceeds 9.9. This is a sensitivity property of the declared envelope, not
evidence that engine sizing is intrinsically unstable.

### Which input matters, and one question the closure answers

**The drag bracket dominates the blade family, and the four percentages are worth printing rather
than one ratio.** Holding the blade and moving across the drag bracket changes the mass by
**6.9 %** and the range by **23.1 %**. Holding the drag and moving across the blade families
changes the mass by **2.9 %** and the range by **8.1 %**. The drag uncertainty therefore produces
about **2.8 times** the range variation of the blade-family choice and about **2.4 times** the
mass variation.

**The thing the study has not measured moves the answer more than the thing it has not chosen.**
That is a statement about which of the two open questions is more consequential to resolve, not
about the intrinsic importance of drag against blade design.

**And the blade that is best before the loop is still best after it.** There was no reason to
assume so: propeller efficiency propagates through cruise power into engine size, engine size
into mass, and mass back into hover power, and a loop can reverse a local ranking. It does not
here — at both ends of the drag bracket the higher-efficiency family closes to the longer
range. **That is a result of the closure rather than an assumption carried into it**, and it
is reported because the opposite outcome would have been reported too.

### The transition, and this is where the section turns

The sizing above says nothing about whether the aircraft can change regime. **The verdict comes
first so that it cannot be missed: the question is asked in two models, only the second of which
carries rotational dynamics, and that one does not support a zero altitude loss.** The first model
is shown anyway, because the mechanism it exposes is real and the reason the second model differs
is the point.

**The first model is kinematically favourable, and the zero-loss result is valid within it.** Treating the aircraft as a
two-degree-of-freedom point mass and driving the body angle kinematically from zero to ninety
degrees, the altitude lost during the rotation falls as the rotation is made slower — the
aircraft is supported through the manoeuvre rather than falling through it. **Entering the
rotation while already climbing removes the loss entirely**: at a 5 m s⁻¹ entry climb the
altitude loss is zero at both reference rotation times — **two seconds for the light design and
5.1 seconds for the heavy one** — and it stays zero at every thrust-to-weight ratio from 1.066
down to 1.00. *(Both times, and the thrust-to-weight figures with them, were established on the
reference geometry at its published mass. The closure above does not re-derive any of them, and
none of them is an output of it.)* Nothing in that result requires the tip pairs
to contribute lift once the climb is acquired.

**In this point-mass model there is no transition time to optimise**, which is a simplification
rather than a trade.
The control moment required scales as 1/t_r² and the control power as 1/t_r³, and the altitude
loss falls with t_r as well: all three point the same way, so the rotation time is set by what
the actuator can do rather than by a balance between competing penalties.

**The second model removes the result, and this is the sharper of the two limitations.** The
point-mass model prescribes the attitude and therefore cannot charge for the trajectory the
aircraft flies while it is being rotated into that attitude. Solved instead with rotational
dynamics and a finite control moment — **and with the aerodynamic pitching moment set to
exactly zero, so that nothing favourable is borrowed** — the light design **loses 5.4 m at the
same reference condition where the point-mass model reports none.** *(That figure, like the
rotation times, belongs to the reference geometry at its published mass; the closure above does
not re-derive it either.)*

**The loss is not an artefact of the controller.** It is unchanged across linear, bang-bang and
smooth reference profiles; it appears without the control moment ever saturating; and it grows
rather than vanishes as the gains are raised, reaching 17 m at gains high enough to track the
reference almost exactly. **What the kinematic model leaves out is not the difficulty of turning
the aircraft but the trajectory the aircraft flies while it is being turned**, so tighter tracking
of a reference the rotational dynamics do not admit moves the aircraft further from the path it
can actually fly, not closer.

**So the zero-altitude-loss result is a property of the model that produced it.** What replaces
it is not a prediction: the aerodynamic pitching moment that would make it one is precisely the
quantity Section 14 reports as **not predicted reliably** — the moment exists; what is missing is
a method that predicts it. **For the methods used here, and for the published comparisons against
which they were checked**, the predictions diverge above roughly ten degrees of incidence, which
is the band the rotation passes through. With
a borrowed moment the outcome depends on which moment is borrowed, and the spread is wide
enough that **no number from it is reportable** — some models complete the rotation, some
saturate the tip pairs, and some tumble. **That spread is itself the finding.** What survives is
not a transferable transition figure but a result for the model that was tested: **within the
finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs
altitude.** Whether a real aircraft loses 5.4 m, more, or less is not settled by anything here.

### What closing does and does not establish

**It establishes that the architecture is arithmetically self-consistent on a declared
package**, at four corners of that package, with mass, power and range agreeing with one
another and with the construction that reproduces the published aircraft.

**It does not establish that the package exists.** The energy store this closure assumes is
the item Section 14 examines, and the examination does not end well. Nothing in this section
should be read as a claim that the aircraft is buildable; the claim is narrower and is the one
the section's title makes — the loop closes analytically, on assumptions that are stated and
that Section 14 tests.

**And these range figures are carried forward as the closed-loop values, not as a ranking.** No
multirotor is sized in this work, so no range comparison is made against one — Section 6 compares
the two families in cruise efficiency and says why it stops there. The comparison against the
other hybrid architectures depends on the sizing contract and belongs to Section 13, which is
where it is made and where it reverses.

---

## The ledger

Section 2 named three charges that any architecture in this corner pays. Section 10 closed a
sizing loop. **This section puts the two together: it says where each charge appears inside
the closed numbers, and how large it is there.**

### What this section does, and the one thing it must not do

**It attributes. It does not add.** Every cost named below is already inside the closure of
Section 10 — in the drag bracket, in the propeller efficiency, in the empty-mass fraction, in the
engine rating. **No new physical cost term is introduced here.** The shares, ratios and
percentages below are new calculations, but each is a decomposition or a derived measure of a
quantity the closure already reported, and adding any of them again as a separate charge would be
double counting.

**Two kinds of item appear, and the difference is stated rather than smoothed over.** Some
costs were computed per source and can be split: the drag build-up has named terms, and the
mass fractions were solved separately. Others are inside a single computed quantity and **the
study did not separate them**; saying otherwise would invent a decomposition that was never
performed. Each is marked.

**And there is no single figure for what the architecture costs.** The three charges are in three
different currencies — kilograms, drag counts, installed kilowatts — and **no scalar aggregate is
defined, because this study has no defensible weighting between them.**

**The refusal has an address, and saying where it points is what keeps it from reading as an
unfinished cost section.** These three quantities become one number only under a sizing contract,
and that is Section 13: **the total is the contract, not a property of the aircraft.** For a
specific mission a designer weights them against that mission's own constraints. **Reporting them
is this paper's job; the weighting belongs to whoever has the mission.**

### Bill 2 — the drag of hover hardware, inside the bracket

The zero-lift drag coefficient of Section 10 is a build-up with named terms. Splitting it:

| | favourable end | adverse end |
|---|---:|---:|
| Clean wetted surface | 0.0073 | 0.0142 |
| Hub and small items | 0.0015 | 0.0022 |
| **Tip frames** | **0.0043** | **0.0047** |
| **Attitude rotors, free-wheeling** | **0.0154** | **0.0169** |
| Total | 0.0285 | 0.0381 |

*(The two columns differ for two separate reasons, and a reader dividing cells should know which
is which. The clean surface and the hub are where the drag bracket itself lives, so their base
values differ between the ends. On top of that, the adverse end carries a ten percent margin
applied to the whole build-up. The frames and rotors have the same base value at both ends and
differ only by that margin. **No line item at the adverse end is an independent measurement**, and
they should not be subtracted from one another as if they were.)*

**The hardware exposed by the vertical-phase layout is 69 percent of the zero-lift drag at the
favourable end and 57 percent at the adverse one.** The frames and the rotors they carry are the
majority of the aircraft's zero-lift drag in both cases, and the rotors alone are more than half
of it at the favourable end. **That is Bill 2 on this aircraft, in the terms Section 2 defined
it** — and the phrase is "exposed by the vertical-phase layout" rather than "dedicated lift group",
because Section 7 is precisely the claim that there is no dedicated lift group here.

**The tip-frame term is an attribution, not a marginal removal cost.** Section 8 gives the frames
four duties: landing gear, control moment arms, rotor support, and the fairing that is the
aircraft's only vertical surface. Their drag is charged to the hover-related hardware set because
that is the set the ledger is decomposing; **it is not a claim that this drag would disappear if
the vertical phase did**, since the landing and directional duties would still have to be met
somehow.

The same statement as a lift-to-drag ratio. **Removing all three non-clean-body terms — the hub
and small items, the tip frames and the free-wheeling rotors** — gives a clean-body ratio of
**20.55** at the favourable end and **15.24** at the adverse one, against the aircraft's **10.82**
and **8.79**. **The configuration retains 52.6 percent of its clean-body lift-to-drag ratio at the
favourable end and 57.7 percent at the adverse one**, so the non-clean-body terms remove 47.4 and
42.3 percent respectively, with the frames and rotors the large majority of what is removed.

**That ordering is the opposite of the one intuition offers, and the word that carries it has to
be exact.** Bill 2 has a **larger fractional burden where the clean-body drag is lower.** In
absolute counts it runs the other way — the frames and rotors are 0.0197 at the favourable end and
0.0216 at the adverse one — but the clean surface nearly doubles between the ends while that
charge moves by a tenth, so a near-constant charge is levied against a smaller total and takes a
larger share of it. **An architecture that improved its clean-body drag without touching its
exposed rotors would find this charge growing as a fraction, not shrinking.**

**This is a statement about position within the drag bracket at one scale.** Section 12 asks a
different question — how the same charge behaves as the aircraft changes size — and the two
answers are about different axes rather than in tension.

**One term inside Bill 2 is not separated, and it is not small in principle.** The build-up
computes each item on its own. **Rotor–structure and rotor–wing interference is not modelled
and is not carried as a line.** Section 2 quotes a wind-tunnel finding that a simulation
assuming negligible rotor–structure interaction *"always predicts higher lift and lower drag than
were experimentally observed"*; this build-up is such a calculation, and the bracket's upper margin
is the only provision made for it.

### The cruise-efficiency gap under fixed pitch

Section 10's closures run at a cruise propeller efficiency of 0.632 to 0.683, against the 0.80 the
published chain assumed. **Relative to that assumption the four fixed-blade closures are 14.6
percent lower at the better blade and 21.0 percent lower at the worse.**

**The ledger does not attribute the whole of that gap to the absence of variable pitch**, and the
distinction matters. What has been shown is that a blade meeting the hover figure of merit
delivers 0.632 to 0.683 in cruise, and that the published assumption was optimistic by that
margin. **No variable-pitch counterfactual was computed**, so nothing here establishes that a
variable-pitch hub would recover the whole difference to 0.80.

**Nor is the gap decomposed.** How much of it is blade twist, how much is section drag at the
cruise inflow angle, and how much is the operating point itself, this work does not say. Anything
finer would be a decomposition that was never performed.

### Bill 1 — carried mass, and what it is on this configuration

**There is no dedicated lift group to charge**, which is the architectural claim of Section 7
appearing as an absence in a ledger. What Bill 1 becomes here is the energy buffer: **3.6
percent of take-off mass, 1.9 to 2.1 kg across the four closures.**

**Section 3 said in advance that this would happen and refused to call it free.** The buffer is
not lift-subsystem mass, so it is not Bill 1 as Section 2 defines it — but it is mass carried
for the whole flight to serve a demand that lasts about two percent of it, which is the
complaint Bill 1 makes. **The architecture converts a power-system charge into a mass one.**
Whether that trade is favourable is what the closure tests, and the closure is where the answer
is: the engine it buys is 3.54 to 5.17 kW rather than one sized by a hover peak of 11.4 to
12.5 kW.

**The buffer fraction is an input to the loop, not a result of it**, and the closure does not
re-derive it from the hover energy the four corners actually need. Dimensionally a fixed fraction
is the right form: at constant disc loading the disc area grows with weight, so hover power is
linear in weight and hover energy with it. **But what the buffer supplies is the hover power minus
what the engine can deliver, and that deficit is not linear.** Across the four closures it runs
from 0.128 to 0.150 kW per kilogram — a spread of 17 percent — while the buffer fraction is held
at 3.6 percent throughout. **The corner that needs the most buffer per kilogram is given the
smallest buffer**, and that is a declared assumption of the closure rather than an outcome of it.

The rest of the empty-mass fraction, for completeness: airframe 0.300 and avionics 0.080 are
**construction constants held common across the three architectures** so that Section 13 compares
like with like — they are not results of this ledger — and propulsion runs 0.176 to 0.198.

### Bill 3 — released from the engine, and not from the electrical path

**This is the charge the architecture attacks most directly, and it is also the one where the
release is partial.**

The engine is sized by cruise: **3.54 to 5.17 kW**. The hover requirement is **11.4 to
12.5 kW**. The buffer supplies the difference for the vertical phase, and the ratio between the
two is **2.4 to 3.2** — that is the factor by which the continuously installed power plant is
smaller than the peak the aircraft must produce.

**But the full hover power passes through the electrical path, and that path is sized by it.**
Machines, power electronics and wiring between the buffer and the rotors carry 11.4 to 12.5 kW
whatever the engine is rated at. **Bill 3 is removed from the engine and left standing on the
electrical system**, and the propulsion mass fraction reflects it: of the 0.176 to 0.198 that
propulsion occupies, **0.108 is fixed and 0.068 to 0.090 scales with installed power.**

### What the closure does not contain at all

The items above are inside Section 10's numbers. **These are not**, and a reader should not
take the closure's convergence as covering them.

| Item | Status |
|---|---|
| **The cost of declining the reaction-torque channel** | Not computed. Thrust asymmetry, propulsive efficiency and the lag set by rotor inertia; quantifying it requires a control-allocation study rather than a torque figure. |
| **The transition altitude result** | 5.4 m in the finite-moment model at the reference geometry — **a result, not a charge**, and not a term in any sizing loop here. |
| **The strip's actuation** | Carried in the systems budget without sizing the mechanism. The number of actuators is not fixed by this study. |
| **The take-off margin** | Drawn from the tip pairs, because the nose pair is sized at thrust equal to weight. It competes with attitude authority and neither is closed against the other. |
| **Landing transition, vortex ring state, closed-loop hover control** | Not analysed. |
| **Engine installation — bay, intake, exhaust, cooling** | Absent from this work entirely. |
| **Rotor–structure and rotor–wing interference** | Inside Bill 2 in principle, absent from the build-up in practice. |

**The first and the last are the two that would most change the numbers above if they were
computed**, and neither is a small correction to a known quantity: one is a control problem the
study has not posed, and the other is a term the study's method is known to under-predict.

### What the ledger amounts to

**Three charges, three currencies, no total.** The non-clean-body drag terms remove 42.3 to 47.4
percent of the clean-body lift-to-drag ratio, and the hardware exposed by the vertical-phase
layout is the majority of the zero-lift drag. Bill 1 appears as a 3.6 percent buffer rather than a
lift group. Bill 3 is divided by 2.4 to 3.2 at the engine and is not divided at all on the
electrical path. **The cruise propeller efficiency sits 14.6 to 21.0 percent below the published
assumption under fixed pitch.**

**No charge on this page is a new one.** Every figure was already inside a quantity Section 10
reported, and this section's only work has been to say which part of which quantity it was.

**And every one of them belongs to one scale.** The four closures vary the drag uncertainty and
the blade-family choice at the reference size; **they do not establish how the three charges
behave as the aircraft changes size.** Section 12 tests that separation directly, and Section 13
asks what happens to the comparison when the sizing contract changes.

---

## The charges separate with scale, and one of them cannot be tested

Section 11 decomposed the three charges on one aircraft, at one size. **This section asks a
different question: are they three quantities, or one quantity under three names?** The test is
to change the size of the aircraft and see whether they move together. If they did, the framework
of Section 2 would be a single cost described three ways, and a ledger in three currencies would be
a ledger in one.

**This is a different axis from the one Section 11 examined.** There, Bill 2's share of the
zero-lift drag was compared at the two ends of the drag bracket, at a fixed size. Here the size
changes. The two answers are about different variables and do not bear on each other.

### What is compared, and why it is these two points

**The comparison is between the two published reference designs, 50 kg and 1 000 kg, sized by
one method.** It is not between the four closures of Section 10, which vary the drag uncertainty
and the blade family at a single size and are not a scale study.

**The pair can be used even though Section 10 superseded some of what was published, because the
quantities this section needs are not among the superseded ones.** The free-wheeling rotor term
is the same value Section 10 carries at both ends of its bracket. Disc loading is a sizing rule
Section 10 holds. The buffer fraction is an input to Section 10's loop. **The quantities Section 10
replaced — the total zero-lift drag, the propeller efficiency, the range and the closed mass — are
not used here**, and no heavy-design range is quoted for that reason: every figure available for
it is partial in one respect or another.

**Two conditions travel with the heavy design and are stated here rather than later.** It has no
drag bracket; it stands on a single zero-lift coefficient with no equivalent bound. And **its
structural closure is undetermined**: shell mass scales with wetted area while take-off mass scales
with volume, so the structural fraction depends on how areal density grows with size, and that
exponent has not been measured. **The comparison below uses powers, loadings and drag terms; it
does not use the structure**, which is why it can be made at all.

### Bill 3 — held nearly flat, and held there by a sizing rule

**Disc loading is held constant**: 44.2 kg m⁻² at 50 kg and 43.7 at 1 000 kg. Specific hover power
depends only on disc loading, so fixing it fixes hover power per unit weight — **0.218 kW kg⁻¹ at
the light design and 0.216 at the heavy**, a ratio of 0.99. Hover power rises from 10.9 kW to
216.2 kW, a factor of 19.8 against a mass factor of 20. **Hover power grows linearly with mass
rather than as the L^3.5 of the classical result.**

The engine, sized by cruise, moves slightly more, because the heavy design cruises faster at a
better lift-to-drag ratio. **The ratio of hover power to engine rating is 4.19 at the light design
and 3.98 at the heavy — a change of 5 percent.**

**That near-constancy is a consequence of a design rule, not a finding about Bill 3**, and it has
to be read that way. What it does establish is narrower and still useful: Bill 3 *can* be held
nearly flat across a factor of twenty in mass by a single sizing choice.

**The rule has a price, and it is paid in geometry.** Holding disc loading constant makes disc area
grow as L³ rather than L², so the nose propeller grows faster than the airframe. Wing loading rises
from 25.3 to 45.0 kg m⁻², span grows by a factor of 3.35 and the main propeller by 4.50, and **the
ratio of propeller diameter to span rises from 0.35 to 0.47.** The heavy design is not the light
design photographed from further away. **Much above 1 000 kg a single nose pair can no longer hold
the disc loading**, and a second would have to be added — which the architecture permits, since
every pair is torque-balanced on its own.

### Bill 2 — falls to between a quarter and a half, and this is the computed result

**The free-wheeling rotor term falls from 0.0154 at 50 kg to 0.0051 at 1 000 kg.** The heavy value
is not pinned: across the blade designs that meet the heavy design's hover requirement it runs from
0.0035 to 0.0074, and 0.0051 is the interior value the sizing was run at. **At every point in that
interval the heavy charge is between a quarter and a half of the light one** — 0.23 at one end,
0.48 at the other.

**The mechanism is not the obvious one.** The obvious explanation is that the wing outgrows the
discs. It does not: the eight tip discs total 0.251 m² against 1.98 m² of wing at 50 kg, and
2.82 m² against 22.24 m² at 1 000 kg — **a disc-to-wing area ratio of 0.127 at both sizes.** What
the charge follows is

> ΔC_D0 ∝ σ R² / (q S)

in which R²/S is the constant just quoted, so **only two terms move**: the blade solidity σ falls,
because the larger rotor meets its thrust with proportionally less blade, and the cruise dynamic
pressure q rises, because the heavy design cruises at 40 m s⁻¹ rather than 30. **The charge falls
because the blade thins and the reference dynamic pressure rises, not because the wing outgrows
the disc.**

**How closely the two terms predict the computed ratio is not claimed here.** The two terms give a
ratio of about three; the computed ratio at the interior value is also about three; but the
computed ratio moves from 2.1 to 4.4 across the heavy interval, so any closer agreement would be an
agreement at a point that no criterion selects. **What holds everywhere in the interval is the
mechanism, the direction, and the order of magnitude.**

**This result does not touch the structural question at all.** It comes from blade-element
solutions on two sized rotors and from the two cruise speeds; it would remain a result even if
the heavy airframe were shown not to close. **And it means the light design is the harder case for
Bill 2**, which is the opposite of the usual expectation for a tail-sitter.

### Bill 1 — cannot be tested with what this work contains

**On this configuration Bill 1 appears as the energy buffer**, as Section 11 set out, since there is
no dedicated lift group to charge. The buffer is 3.6 percent of take-off mass at 50 kg and 4.0
percent at 1 000 kg.

**Both of those figures are inputs.** Neither is derived from the hover energy the aircraft needs;
each was chosen for its design point and carried into the sizing. **A change from 3.6 to 4.0 percent
is therefore a change between two choices, not a scaling result**, and it cannot be offered as
evidence that Bill 1 moves with size in either direction.

**Nor is the structural mass a substitute.** The shell-mass exponent governs how the airframe
fraction scales, and it is unmeasured; but the airframe is not Bill 1 as Section 2 defines it — it
is the structure every architecture carries — and treating it as the mass bill would change the
definition to fit the test.

**Deriving the buffer from the hover energy is possible in principle and is not attempted here.**
Doing it properly means asking what specific power a store of that mass must deliver, and that is
the item Section 14 examines and does not resolve. This section stops short of it deliberately.

### What the comparison establishes

**Separability is shown between two of the three charges, and not the third.** Bill 2 falls to
between a quarter and a half of its light-design value while Bill 3 is held within 5 percent by a
single sizing rule. **Two quantities that respond that differently to the same change of size are
not one quantity under two names.** That is the finding, and it holds wherever in the heavy
interval the rotor term falls.

**Bill 1 is untested at scale**, for the reason given above, and nothing here should be read as
showing it separates from the other two — or as showing that it does not.

**And the evidence is one pair of design points, computed by one method.** It is consistent with
the separability Section 2 asserts; it is not a verification of separability as a general property,
which a single instantiation cannot supply.

### Two costs that scale does not relieve

Neither is one of the three charges, and both are reported because a section about what scale does
to this aircraft would be incomplete without them.

**The fixed-pitch gap does not close with size; it widens slightly.** Against the 0.80 the
published chain assumed, the computed cruise propeller efficiency is 14.6 to 21.0 percent lower at
the light design and **16.4 to 23.0 percent lower at the heavy one.** Refusing the variable-pitch
hub costs as much or more at the larger size.

**The transition is where the square–cube relation is paid in full.** The moment needed to rotate
the aircraft follows M = Iα with I ∝ mL², so the moment required for a fixed rotation time grows
much faster than the aircraft. **Rotating the heavy design in the light design's two seconds would
demand 221.5 kW from the tip propellers — 102 percent of hover power**, which is not available. At
5.1 seconds the demand falls to 13.4 kW, 6 percent of hover power, and that is the heavy design's
rotation time. **A larger aircraft of this type turns more slowly, and must.** Hover power escapes
the classical scaling objection by fixing disc loading; the rotation does not escape it.

### Why this section sits between the ledger and the contracts

**The argument of the next section depends on this one.** If the three charges were one quantity,
a single number could rank architectures regardless of how the charges were weighed. **Because at
least two of them move independently, any ranking must say how they were weighed** — and a sizing
contract is exactly such a weighing. Section 13 shows what happens to the ranking when the contract
changes, and it can do so only because this section has shown that there is more than one thing
being weighed.