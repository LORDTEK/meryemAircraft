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
aircraft. **The contribution is the architecture: a configuration arranged to change regime by
rotating the airframe rather than its propulsors, and so carrying no mechanism that reorients a
propulsor.** The combination, the consequences of the choices inside it, and an accounting of what
they cost are how that contribution is presented and priced — not a claim that the route was
waiting to be found.

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

### The charges are coupled: remedies move cost between them

The three charges are not independent problems with independent fixes. **Each known partial
remedy reduces one and raises another.** They are three distinct accounting quantities — kilograms,
drag counts, installed kilowatts — and they are not assumed to be independent physical causes: a
remedy can move a requirement from one currency into another. Whether a change of size moves them
together, which would make them one quantity under three names, is tested in Section 12.

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
In the doctoral study whose wind-tunnel campaign is quoted above — and in that document rather
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
all: **where an arrangement pays one charge heavily in order to escape another, its ranking
against a differently-balanced arrangement will move when the sizing rule changes — toward the
lighter arrangement as the rule weights mass more — and will reverse where that reweighting carries
it past the point at which the two break even, where the mass difference as the contract counts it and
the cruise-efficiency difference cancel in the range.** Section 13 tests both the
movement and the reversal on this configuration, and Section 4 tests a different consequence
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
weight, the buffer that supplies what the engine cannot deliver of that peak — at a specific power
Section 14 examines — the
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
compresses it is not the wing. **It is the cruise efficiency this aircraft's fixed-pitch blade
delivers:** at a propeller efficiency of 0.85 the same airframe reaches 7.47 to 9.20. Whether a
variable-pitch hub would recover that difference is not computed; Section 11 reports the gap and
declines to attribute all of it to the hub.

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
rather than higher — at a propeller efficiency η_p = 0.85 the same airframe would reach 7.47 to 9.20. Section 11 charges all three.

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

The configuration is arranged to change regime by **rotating the airframe**. The propulsors hold
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
on the transition aerodynamics, and Section 14 says why those are not reliable — for the methods used
here and the published comparisons against which they were checked — at the incidences the rotation
passes through.

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
listing them. The nose pair meets all four parts of Section 3. The tip pairs do not: they hold
one orientation, but they are carried through cruise producing moments rather than cruise thrust,
which is the first of Section 3's failure modes, and they are exposed while doing it. This is the partial
instantiation Section 3 lists as its **fourth** failure mode — meeting the condition where the
aircraft is carried and failing it elsewhere — and the charge it re-opens is the second, carried in
Section 11. *(They are not the second row of Section 3's table: that row concerns a propulsor whose
duty is to lift and which is then carried. The tip pairs are sized for moments; they add the
take-off margin (Section 5), but they were not sized for weight support, and Section 3's permitted-cost clause places attitude devices outside the first charge while leaving them in the
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
the paper's own finding in Section 13. Against lift-plus-cruise the ordering depends on the sizing
contract: across the three contracts it moves substantially, and under one of them its sign changes
inside the envelope and turns on a mass fraction of the competitor that is not measured. A paper that quoted one of those orderings as a result would be reporting its own choice of
contract. Against the tilting family the competitor can be modelled here only as a bound that pays no
cruise penalty, and an ordering against a bound is not a result. **No
range claim is made against the tilting or lift-plus-cruise families in either direction**, and
a reader who finds one implied anywhere in this paper should treat it as an error rather than
as a claim.

### What each claim does not depend on

A reader who rejects one of these claims should be able to see immediately which of the others
survive, and the dependencies are short enough to list.

| Claim | Does not depend on |
|---|---|
| Operation without a runway | the drag bracket, the propeller efficiency, the transition aerodynamics — **but it does depend on the energy store**: the vertical phase is sized with one, and Section 14 examines whether it exists |
| Cruise lift carried on a surface | the sizing contract, the transition aerodynamics |
| The **size** of the cruise-efficiency margin | — it depends on both the drag bracket and the blade family, and Section 6 reports it as a range rather than a number |
| Elimination of the propulsor-reorientation mechanism class | the drag bracket, the propeller efficiency, the sizing contract, the range result, the energy store, **and the transition aerodynamics** |

**The last row carries a distinction that matters more than the others.** The mechanism claim is
a statement about what hardware is present, and it is settled by the inventory of Sections 7 and 8. **The
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
suggest, and the narrower statement is the one the paper defends: **a configuration sized to
combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so
with no mechanism that reorients a propulsor, and an account of what the combination costs.**

Each half of that has a named opponent and neither half is a record. **Nor is the configuration
claimed to be without precedent**: Section 1 sets out what is already established, including
uncrewed tail-sitters, tail-sitters without control surfaces, coaxial contra-rotating
tail-sitter propulsion, and blended-wing-body tail-sitters. **The contribution is the
architecture, and the paper presents it as the combination, the consequences of the choices inside
it, and the accounting** — which is what Sections 7 and 8 describe and what Section 11 prices.

### One consequence for how the numbers that follow should be read

Because the comparative result depends on the sizing contract, **no comparison in this paper
should be quoted without the contract it was computed under.** That is not a caveat attached for
safety; it is the paper's own finding applied to the paper's own numbers, and Section 13 states
what it demands of anyone who uses the framework afterwards.

---

## Analytical closure of the sizing loop

This section prices the arrangement of Sections 7 and 8 on a declared package; it does not bear on
the count of mechanism classes, which rests on the inventory of those sections alone.

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
closures the wing area runs 2.07 to 2.27 m², the span 3.53 to 3.70 m, and the nose disc diameter
1.23 to 1.29 m. **The cruise lift coefficient is unchanged at 0.450 in every one of them**, so the
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

| | C_D0 | η_p | L/D | MTOW | Empty fraction | Hover power, rotor shaft | Engine rating, shaft | Range |
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
where it is made.

---

## The ledger

Section 2 named three charges that any architecture in this corner pays. Section 10 closed a
sizing loop. **This section puts the two together: it says where each charge appears inside
the closed numbers, and how large it is there.** Like the closure, the ledger prices the
arrangement; the count of mechanism classes is not an entry in it.

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

**The rotor line rests on section drag at low Reynolds number.** It is a blade-element result for
blades whose sections run near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section
polars that are computed rather than measured, and section drag is hardest to predict in that range.
Section 12 shows how strongly the term depends on it.

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
linear in weight and hover energy with it. **But what the buffer supplies is the hover demand less
what the engine can deliver, and that deficit is not linear.** Taken at the electrical bus, where
the buffer sits — rotor shaft power divided by the machine and power-electronics efficiencies, less
the engine's shaft power times the generator's — it runs from 0.168 to 0.188 kW per kilogram of take-off mass across
the four closures, a spread of 12 percent, while the buffer fraction is held at 3.6 percent
throughout. **The corner that needs the most buffer per kilogram is given the
smallest buffer**, and that is a declared assumption of the closure rather than an outcome of it.

The rest of the empty-mass fraction, for completeness: airframe 0.300 and avionics 0.080 are
**construction constants held common across the three architectures** so that Section 13 compares
like with like — they are not results of this ledger — and propulsion runs 0.176 to 0.198.

### Bill 3 — released from the engine, and not from the electrical path

**This is the charge the architecture attacks most directly, and it is also the one where the
release is partial.**

The engine is sized by cruise: **3.54 to 5.17 kW** of shaft rating. The hover requirement is
**11.4 to 12.5 kW** at the rotor shaft. The ratio between the two is **2.4 to 3.2** — a ratio of
installed hardware, the factor by which the continuously installed power plant is smaller than the
peak the rotors must absorb. **It is not the buffer's burden**, which is taken at the electrical bus
rather than as the difference of these two shaft figures, and which Section 14 computes.

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
behave as the aircraft changes size.** Section 12 asks whether they move together when the size
changes, and Section 13 asks what happens to the comparison when the sizing contract changes.

---

## Scale does not lock two of the charges together; the third is not tested

Section 11 decomposed the three charges on one aircraft, at one size. **This section asks a
different question: are they three quantities, or one quantity under three names?** The test is
to change the size of the aircraft and see whether they move together. If they did, the framework
of Section 2 would be a single cost described three ways, and a ledger in three currencies would be
a ledger in one. Either answer leaves the mechanism claim where it was; that claim rests on the
inventory of Sections 7 and 8.

**The test is deliberately weak, and it is stated at its own strength.** It can show that two
charges are not locked together within this model. It cannot show that they are independent in
general, and it is not offered as doing so.

**This is a different axis from the one Section 11 examined.** There, Bill 2's share of the
zero-lift drag was compared at the two ends of the drag bracket, at a fixed size. Here the size
changes. The two answers are about different variables and do not bear on each other.

### What is compared, and why it is these two points

**Section 10 closed only the light configuration, at 52.3 to 57.5 kg. No closure was run at 1 000 kg**, and
none could be run on the same footing: the heavy design has neither a drag bracket nor a structural
closure (both below). A scale comparison therefore cannot be made from Section 10's closures. **It
is made between the two reference designs, 50 kg and 1 000 kg, sized by one method, and both ends are taken from that pair.** In this section *the light design* and *the heavy design* mean
those two reference designs. Taking one end from Section 10 and the other from the reference pair would manufacture a scale
change that is really a propeller-efficiency update applied to one end only.

**The quantities used are ones Section 10 did not replace.** Disc loading is a sizing rule
Section 10 holds. The buffer fraction is an input to its loop. The free-wheeling rotor term is the value Section 10 carries at both ends of its bracket at 50 kg,
before the ten percent margin of the adverse end (Section 11), and it is computed here at 1 000 kg by
the same method. **The total zero-lift drag, the propeller efficiency, the range and the closed mass
are not used.** No heavy-design range is quoted: the figures available for it either omit the
free-wheeling rotor charge or carry an assumed rather than a computed propeller efficiency, and none
carries both.

**Two conditions travel with the heavy design.** It has no drag bracket; it stands on a single
zero-lift coefficient with no equivalent bound. And **its structural closure is undetermined**: shell
mass scales with wetted area while take-off mass scales with volume, so the structural fraction
depends on how areal density grows with size, and that exponent has not been measured. **The
comparison below uses powers, loadings and drag terms; it does not use the structure**, which is why
it can be made at all.

### Bill 3 — held nearly flat by a sizing rule, which is not a finding about Bill 3

**Disc loading is held at approximately the same value**: 44.2 kg m⁻² at 50 kg and 43.7 at
1 000 kg, one percent apart. At a given figure of merit, specific hover power depends only on disc
loading, so holding it holds hover power per unit weight — **0.218 kW kg⁻¹ at the light design and
0.216 at the heavy**, within one percent. Hover power rises from 10.9 kW to 216.2 kW, a factor of 19.8
against a mass factor of 20. **Hover power grows linearly with mass rather than as the L^3.5 of the
classical result.**

**That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3.**
What it establishes is narrower and still useful: the hover side of Bill 3 *can* be held flat across
a factor of twenty in mass by a single sizing choice.

**The measure Section 11 uses for Bill 3 — rotor-shaft hover power divided by engine shaft rating, a
ratio of installed hardware rather than a deficit — carries a second quantity, and it does not travel
as cleanly.** The ratio is 4.19 at the light design and 3.98 at the
heavy, a change of 5 percent. *(Section 11's 2.4 to 3.2 is the same ratio at the four closures; their
cruise engines, 3.54 to 5.17 kW, are larger than the light reference design's 2.6 kW, and the engine
rating is a quantity Section 10 did replace. This paragraph compares the reference pair only.)* But the engine is sized by cruise, not by disc loading, and **the two
reference designs do not use the same engine margin**: the engine is rated at 1.53 times cruise
electrical power at 50 kg and 1.39 times at 1 000 kg. With the light design's margin at both sizes the
heavy engine would be 60.0 kW and the ratio 3.61, a change of 14 percent. **The Bill 3 ratio therefore
moves by between 5 and 14 percent across the factor of twenty, depending on an engine margin the
sizing rule does not set.**

**The rule has a price, and it is paid in geometry.** Holding disc loading constant makes disc area
grow as L³ rather than L², so the nose propeller grows faster than the airframe. Wing loading rises
from 25.3 to 45.0 kg m⁻², span grows by a factor of 3.35 and the main propeller by 4.50, and **the
ratio of propeller diameter to span rises from 0.35 to 0.47.** The heavy design is not the light
design photographed from further away. **Much above 1 000 kg a single nose pair can no longer hold
the disc loading**, and a second would have to be added — which the architecture permits, since
every pair is torque-balanced on its own.

### Bill 2 — the rotor term falls, and in this model Reynolds number accounts for it

**Only the rotor term of Bill 2 is computed at both sizes.** The frame term enters both reference
designs as the same multiplier on clean lift-to-drag ratio, by construction, so it cannot show a scale
effect in either direction.

**The rotor term is computed by one method at both sizes**: the blade designed for its own hover
thrust at the same design tip speed, the hub at the same fraction of the radius, and the free-wheeling
state solved at each design's own cruise speed. At 50 kg it is **0.0154**. At 1 000 kg the blade
designed to the same section lift coefficient gives **0.0068 — 0.44 of the light value.** Across the
blade designs swept, design section lift coefficient 0.55 to 0.85, the heavy term runs from **0.0045
to 0.0100**, and every design in that range meets the heavy design's hover requirement with margin — a
figure of merit of 0.75 to 0.77 against the 0.599 required. At 50 kg the hover requirement selects the
blade; at 1 000 kg nothing selects within the interval, and its ends are the ends of the swept blade
family, not a physical bound. **At every point in it, and in the section polars used here, the heavy
charge is between 0.29 and 0.65 of the light one** — a direction that is the ordinary one and a factor
that is not a measurement, for the reason given below.

**The mechanism is not the obvious one, and it is not the one a dimensional argument suggests.**
Three candidates can be excluded directly:

- **Geometry.** The eight tip discs total 0.251 m² against 1.98 m² of wing at 50 kg, and 2.82 m²
  against 22.24 m² at 1 000 kg — **a disc-to-wing area ratio of 0.127 at both sizes.** The wing does
  not outgrow the discs.
- **Dynamic pressure.** A rotor turning freely at zero shaft torque settles at a rotational speed
  proportional to the flight speed, so its axial force scales with dynamic pressure and a coefficient
  referenced to that pressure does not. Solving the heavy blade's free-wheeling state at 30 and at
  40 m s⁻¹ confirms it: the coefficient changes by **9 percent** — itself a Reynolds-number effect —
  not by the 44 percent a dynamic-pressure scaling would give.
- **Solidity.** The heavy blade is not thinner; it is fuller — **0.100 against 0.075** for blades
  designed to the same section lift coefficient.

**Within the blade-element and section-polar model, the section Reynolds number accounts for the
fall.** In the free-wheeling state the median blade-section Reynolds number rises from about 8 × 10⁴
at 50 kg to 5.6 × 10⁵ at 1 000 kg, a factor of 6.8, because the chords are longer and the flight speed
higher. **Evaluating the heavy blade with its section Reynolds number scaled down to the light rotor's
returns 0.0181 — 18 percent above the light charge.** At equal Reynolds number the fuller heavy blade
would pay more, not less. Reynolds number is not an independent variable — it follows from the chord
and the speed each rotor has — so this is a decomposition inside the model rather than a causal claim
beyond it: for the chords and speeds these two designs have, the fall is what lower section drag at a
higher Reynolds number gives.

**That places a condition on the result, and it runs both ways.** The fall rests on how section drag
changes between 8 × 10⁴ and 5.6 × 10⁵, which is taken from the section polars used for every rotor in
this work rather than measured, and the light end lies below a Reynolds number of 10⁵, where section
drag is hardest to predict. **The direction — lower section drag at higher Reynolds number — is the
ordinary one; the size of the fall is as good as the section model at the low end.** If the light
blade's real section drag is higher than the polars give, the light charge is larger and the fall is
larger; if it is lower, the fall is smaller — the heavy end, at the higher Reynolds number, being the
better predicted of the two. **Of the two rotor terms, the light one is therefore the
less certain — and it is the one Sections 10 and 11 carry.**

**The result does not touch the structural question.** It comes from blade-element solutions on two
sized rotors at their own conditions; it would remain a result even if the heavy airframe were shown
not to close. **For the rotor term, the light design is the harder case.** That statement is not
extended to Bill 2 as a whole, because the frame term is not computed at the heavy design and the
heavy design has no drag bracket.

### Bill 1 — not tested, and the one available derivation would not test it

**On this configuration Bill 1 appears as the energy buffer**, as Section 11 set out, since there is
no dedicated lift group to charge. The buffer is 3.6 percent of take-off mass at 50 kg and 4.0
percent at 1 000 kg.

**Both of those figures are inputs.** Neither is derived from the hover energy the aircraft needs;
each was chosen for its design point and carried into the sizing. **A change from 3.6 to 4.0 percent
is a change between two choices, not a scaling result**, and it cannot be offered as evidence that
Bill 1 moves with size in either direction.

**A derivation is available without settling what specific power a store can deliver, and it is
stated here because it shows why it is not used.** If the buffer is sized to supply the hover deficit
— the hover demand at the electrical bus less what the engine delivers there — at a specific power
that is the same at both sizes, its mass fraction follows the deficit per kilogram: 0.202 kW kg⁻¹ at
50 kg and 0.199 at 1 000 kg, a fall of about 2 percent. **But that derivation makes the buffer a function of the hover power and the engine
rating, which are the two quantities that measure Bill 3.** A buffer derived that way is locked to
Bill 3 by the derivation itself, and comparing the two across scale would test the derivation, not
whether they are separate. Sizing the buffer by energy instead adds a hover duration, which is a
mission choice, and changes nothing in that argument.

**No quantity computed in this work gives a buffer requirement at scale that is independent of the
hover and engine powers and of an assumed specific power or energy.** On this aircraft Bill 1 takes
the form of the device that releases Bill 3 from the engine, as Section 3 anticipated, and **whether
the two are separable here is not established.**

**What is established is that they are coupled here, and that is Section 3's claim rather than a
defect found in it.** The buffer is the conversion the fourth part of the escape condition permits:
kilowatts of hover peak paid in kilograms of store. **Coupling is not identity.** The buffer is
measured in kilograms and the engine in kilowatts, linked by a specific power that is itself an
assumption; and the coupling belongs to an aircraft that meets the escape condition, not to the
framework — a lift-plus-cruise aircraft pays a lift group whose mass is not a function of its cruise
engine.

**Nor is the structural mass a substitute.** The shell-mass exponent governs how the airframe
fraction scales, and it is unmeasured; but the airframe is not Bill 1 as Section 2 defines it — it
is the structure every architecture carries — and treating it as the mass bill would change the
definition to fit the test. What specific power a store of the required mass must deliver is the
item Section 14 examines and does not resolve.

### What the comparison establishes

**Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its
light-design value in the section polars used here, while specific hover power changes by one percent
and the Bill 3 ratio by 5 to 14 percent.** The flatness of Bill 3 is imposed by a sizing rule; the finding is that Bill 2 moved anyway,
by more than the Bill 3 ratio at every point in the heavy interval and under either engine margin.
**Within this model, the two are therefore not one quantity under two names.**

**Bill 1 is not tested**, for the reason given above, and nothing here should be read as showing
that it separates from the other two — or as showing that it does not.

**And the evidence is one pair of design points, computed by one method, with the Bill 2 result
resting on a section-drag model at low Reynolds number.** It is consistent with the separability
Section 2 asserts; it is not a verification of separability as a general property, which a single
instantiation cannot supply.

### Two costs that scale does not relieve

Neither is one of the three charges, and both are reported because a section about what scale does
to this aircraft would be incomplete without them.

**The cruise-efficiency gap under fixed pitch does not close with size; it widens slightly.**
Computed at each reference design's cruise thrust, a nose-pair blade that meets the hover requirement
delivers a cruise efficiency 14.6 to 21.0 percent below the 0.80 assumed at the light design and
**16.4 to 22.9 percent below it at the heavy one.** As in Section 11, no variable-pitch counterfactual
was computed, so this is not a measure of what refusing the hub costs; it is a measure of what a fixed
blade that hovers delivers in cruise, and that does not improve with size.

**The transition is where the square–cube relation is paid in full.** The moment needed to rotate
the aircraft follows M = Iα with I ∝ mL², so the moment required for a fixed rotation time grows
much faster than the aircraft. **Rotating the heavy design in the light design's two seconds would
demand about 220 kW from the tip propellers — roughly the whole of hover power**, which is not
available. At 5.1 seconds, the heavy design's rotation time, the demand falls to about 13 kW, 6
percent of hover power. **A larger aircraft of this type turns more slowly, and must.** Hover power
escapes the classical scaling objection by fixing disc loading; the rotation does not escape it.

### Why this section sits between the ledger and the contracts

**The next section needs only what this one shows.** If the three charges were one quantity, a single
number could rank architectures whatever weight each charge was given. **Because at least two of them
are not locked together, a comparison of architectures cannot in general be reduced to a number that
does not depend on how the charges are weighed: where one architecture pays less of one charge and
more of another, the ranking depends on the weighting.** The argument requires only two charges that
are not locked together; the third need not be shown separate for the conclusion to hold. A third
shown to be separate would strengthen it; a third shown to be locked to one of the others would
leave it standing.

Section 13 examines what the choice of sizing contract does to a ranking, on the light closures of
Section 10 only.

---

## Rankings belong to contracts

Section 12 showed that at least two of the three charges are not locked together, and drew the
consequence: where one architecture pays less of one charge and more of another, a ranking depends
on how the charges are weighed. **A sizing contract is one such weighing.** It fixes what is held
equal between the architectures being compared, and what is held equal decides how a difference in
mass is set against a difference in cruise efficiency. This section applies three contracts to three
architectures at each of the four closures of Section 10. **The mechanism claim is not a ranking
and is not at stake here**; what is at stake is how the price computed in Sections 10 and 11 enters
a comparison with other architectures.

### Three contracts, and what each holds equal

Range in the sizing loop is

> R = (E* η / g) · (L/D) · (m_fuel / m_TO),

where E* is the fuel's specific energy and η the energy chain, propeller included. The three
contracts differ only in the last factor.

- **Fixed fuel fraction.** Every architecture carries sixteen percent of its own take-off mass as
  fuel. **Take-off mass cancels from range**, which is then set by L/D and the chain alone. A
  heavier architecture shows its mass in the take-off-mass column and nowhere in the range column.
- **Fixed fuel mass.** Every architecture carries the fuel this configuration carries at the same
  closure — 8.4 to 9.2 kg. **Range is divided by take-off mass**, so a heavier aircraft flies the
  same fuel less far.
- **Fixed take-off mass and payload.** Every architecture is held to this configuration's closed
  mass and its 13 kg payload. **Fuel is what remains after the empty mass**, so every kilogram of
  architecture-specific hardware is a kilogram of fuel not carried.

**These are three different questions, not three estimates of one answer.** The first asks which
aircraft converts a fuel fraction into distance more efficiently; the second, which flies further on
a given tank; the third, which flies further at a given gross weight. A mission decides which of
them it is asking. This paper has no mission that would decide, and does not choose.

### What is compared, and on what basis

**Three architectures fly the same mission**: 13 kg of payload at 30 m s⁻¹, with the same wing
loading, disc loading and aspect ratio, the same airframe and avionics fractions, and the same fuel
and energy chain apart from the propeller. **The competitors are therefore this planform with two
add-ons**, not independently designed aircraft of their families. **All three carry the same buffered
series-hybrid power system** — a buffer of 3.6 percent of take-off mass and an engine sized by cruise —
so Bill 3 is held common, and what the comparison measures is mass and cruise drag. This configuration
is the first architecture; the others are a lift-plus-cruise layout and a tilting one.

**Holding Bill 3 common is a choice of question, and it has a direction.** It is made so that the
contract can be seen acting on a mass difference against a cruise-efficiency difference; it is not a
claim that those families would use this power system, and the tilting family as Section 2 describes
it has no store at all. **The choice runs against this configuration.** Given no buffer and an engine
rated to deliver the hover demand through the generator, the power electronics and the machines
instead, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off
mass, and under a fixed fuel mass falls 38 to 47 percent behind; the tilt bound does not close under a
fixed take-off mass. **Under a fixed fuel fraction the tilt bound closes at 520 kg — about ten times
this configuration's mass — with its range lead unchanged at 103 to 141 percent**: the first
contract's blindness to mass, made visible. **That comparison is not used**, because it would set
competitors without a store against this configuration with one — a buffer of 3.6 percent whose
feasibility is the item Section 14 examines. Whatever that store turns out to cost, holding it common
charges all three the same assumption.

**The basis is not symmetric, and each asymmetry is stated with its direction.**

- **Drag.** All three share the clean airframe at each end of the drag bracket. This configuration
  carries its exposed frames and free-wheeling rotors, as in Sections 10 and 11. The lift-plus-cruise
  layout carries the ratio measured in the wind-tunnel campaign quoted in Section 2 — maximum
  lift-to-drag ratio about 17 clean and about 13 with the lift hardware installed and its propellers
  locked parallel to the flow — **transferred from a different airframe**, and assuming lift rotors
  stopped and aligned in cruise, which takes an indexing mechanism (Section 7) whose mass is not
  separately charged. **The tilting layout carries no cruise drag penalty at all.** That is an
  idealisation in its favour, and it is deliberate: it makes the tilt row a bound.
- **Propeller efficiency.** This configuration uses the computed 0.632 and 0.683 of Section 10. The
  other two use 0.80 — the lift-plus-cruise layout because its cruise propeller does nothing else,
  the tilting layout because it has a variable-pitch hub. **Both are assumed, not computed**, and the
  asymmetry runs against this configuration; it is tested below.
- **Mass.** The lift-plus-cruise layout carries a lift group of 10 percent of take-off mass and the
  tilting layout a tilt mechanism of 5 percent. **Neither figure is measured.** The first turns out to
  decide the sign of one result, and it is varied below.

### Against lift-plus-cruise: a trade, and the contract sets the exchange rate

**The two architectures trade one charge against another.** Closed under a fixed fuel fraction, the
lift-plus-cruise layout is **38 to 43 percent heavier** — its lift group, amplified by the mass loop,
partly offset by this configuration's larger engine — so this configuration is **27 to 30 percent
lighter**. In return the lift-plus-cruise layout cruises at a lift-to-drag ratio of 11.66 at the
adverse end of the drag bracket and 15.72 at the favourable end, against 8.79 and 10.82 — both
aerodynamic ratios on the same clean airframe — with a propeller at 0.80 against 0.632 to 0.683.

Range of the lift-plus-cruise layout relative to this configuration:

| Closure (Section 10) | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass |
|---|---:|---:|---:|
| Adverse drag, lower blade family | +67.8 % | +40.2 % | +1.1 % |
| Adverse drag, upper blade family | +55.3 % | +27.5 % | **−13.0 %** |
| Favourable drag, lower blade family | +83.9 % | +53.5 % | +7.3 % |
| Favourable drag, upper blade family | +70.2 % | +40.1 % | **−6.5 %** |

**Under a fixed fuel fraction the mass difference does not reach the range column**, and the
lift-plus-cruise layout flies 55 to 84 percent further. Under a fixed fuel mass the difference enters
as a divisor, and its lead falls to 28 to 54 percent. Under a fixed take-off mass it enters as fuel not
carried, and **the lift-plus-cruise layout lands between 13 percent short of this configuration's
range and 7 percent beyond it.** Moving from the
first contract to the third shifts the comparison by **67 to 77 percentage points at every closure**
at the declared lift-group fraction, and always toward the lighter aircraft.

**The sign itself changes inside the envelope under the third contract.** This configuration is
ahead at the two closures with the higher-efficiency blade family and behind at the two with the lower.
**A statement of which architecture has the longer range, made without its contract, would therefore
be a statement about the contract.**

### Against the tilting layout: a bound, not a ranking

**The tilting layout, modelled as a bound, leads under every contract at every closure — by 93 to 141
percent.** Moving from the first contract to the third shifts the comparison by 1 to 18 points toward
this configuration, and nowhere near a reversal.

**There is a trade, but it is lopsided.** The tilting layout closes 0.5 to 5.4 percent heavier than
this configuration, and it cruises at the clean airframe's lift-to-drag ratio with a propeller at 0.80:
it is credited with no nacelle drag, no pivot fairing, and no penalty for flying hover-sized rotors as
cruise propellers. **Even the contract that weights mass most** — a fixed take-off mass, in which every
kilogram of tilt mechanism is a kilogram of fuel not carried — **leaves the bound 93 to 130 percent
ahead.**
The contract moves the comparison, as Section 12 says it must where there is a trade; none of the
three moves it far enough to matter. A ranking against a competitor modelled as a bound is not a
ranking, and **no range claim is made against the tilting family in either direction.**
The claim this paper makes against that family is about mechanism (Sections 7 and 8), and nothing in
this section bears on it.

### Section 2's prediction, tested

**Section 2 predicted that where an arrangement pays one charge heavily in order to escape another,
its ranking against a differently-balanced arrangement will move when the sizing rule changes, and
can reverse.** Both parts can now be checked.

- **The movement holds everywhere**, against both competitors, in the predicted direction: toward the
  lighter arrangement as the contract weights mass more.
- **The reversal holds at two of the four closures against lift-plus-cruise, and at none against the
  tilt bound.**

**Where the reversal falls is decided by quantities this study has not measured or not fixed.** In
the case above it is the blade family, which Section 10 leaves open. Across the sensitivity cases below
it is the competitor's lift-group mass and the propeller basis:

| Case | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass | Shift, first to third |
|---|---:|---:|---:|---:|
| As above | +55 to +84 % | +28 to +54 % | −13 to +7 % | 67 to 77 points |
| Lift group 5 % of take-off mass | +55 to +84 % | +47 to +76 % | +36 to +65 % | 14 to 24 points |
| Lift group 15 % of take-off mass | +55 to +84 % | +8 to +31 % | −62 to −50 % | 117 to 134 points |
| All three at this configuration's propeller efficiency | +33 to +45 % | +6 to +17 % | −33 to −25 % | 65 to 72 points |
| Lift-plus-cruise drag as a fixed increment, not a ratio | +59 to +75 % | +31 to +45 % | −13 to +5 % | 67 to 75 points |

*(Range of the lift-plus-cruise layout relative to this configuration, across the four closures.)*

**With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every
closure; with a heavier one this configuration leads under a fixed take-off mass at every closure.**
Giving all three the same propeller efficiency also produces a reversal at every closure. **Which
architecture ranks first under a fixed take-off mass is therefore decided, in this model, by a mass
fraction of the competitor that this study has not measured** — and the fixed-fuel-fraction column,
where mass does not enter, does not move with it at all. **Put plainly, the sign under a fixed take-off
mass is not a result about the architectures; it is a result about that parameter**, and it is the
one most worth measuring.

**The size of the shift behaves the same way.** It barely moves when the propeller or drag basis is
changed — 65 to 77 points across those cases — because those asymmetries enter all three contracts
alike. It moves a great deal with the lift group, from 14 to 134 points, because the shift *is* the
mass difference being counted. **What is robust is that the shift exists and runs toward the lighter
aircraft; its size is the size of the mass difference.**

### What the framework asks of whoever uses it

A framework that says every remedy transfers a charge rather than removing it takes something from
its user in return. **It asks for three things, and this paper holds itself to them.**

**Carry the audit, for every column.** State each charge in its own currency — kilograms, drag
counts, installed kilowatts — before any aggregate, and state the basis of the comparison with its
asymmetries and their directions. An aggregate that arrives without its parts cannot be checked, and
the parts are where the comparison is decided. **This paper meets that for its own column** (Section
11) **and not for the competitors'**, whose kilograms and drag counts here are parameters and transferred
ratios rather than an audit — which is one more reason no ranking against them is offered.

**Name the contract.** A comparison of architectures is a comparison under a contract. The contract is
chosen by the mission rather than by the analyst, and a comparison that does not state one has chosen
one silently.

**Refuse the bare ranking.** Report an ordering only with the contract it was computed under, and,
where its sign depends on an unmeasured quantity, with that quantity named. An ordering that holds
under every contract examined may be reported as such — that is a stronger statement than any one
contract gives, and it still names the contracts. Applied to this paper's
own numbers, the rule is the fourth row of Section 9: **no range claim is made against lift-plus-cruise
or tilting layouts**, because the ordering against the first depends on the contract and on the
competitor's lift-group mass, and the ordering against the second is against a bound.

### What this section does not establish

**The competitors are modelled at a coarser level than this configuration.** Their drag is a ratio
transferred from another airframe or an idealisation; their propeller efficiency is assumed; their
architecture-specific mass is a parameter. This configuration's drag and propeller efficiency are
computed. **Comparing computed figures against assumed ones favours whichever is assumed more
optimistically**. In propeller efficiency that is both competitors, and the table above shows the
size of it; in drag it is the tilting layout, by construction.

**The comparison is at one size.** Section 12's heavy design has no closure, and none of its figures
is used here.

**And nothing here ranks architectures for a mission.** Which contract a mission implies, and which
architecture it then favours, is the user's question. What this section establishes is narrower: **the
same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by
tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property
of the architectures alone.

---

## What does not close

Section 10 closed the sizing loop on a declared package and said that whether an aircraft can be
built to it is a different question. **This section is where that question is answered, and for the
first item the answer is no.** Section 9 called this section a debt: questions the paper does not
answer and that better evidence would. It is stated in that order — first the obstacle that is known,
then what is not known.

### First, the known obstacle: the energy store

**Every closure in Section 10 carries a buffer of 3.6 percent of take-off mass.** That figure is an
input, not a result (Sections 11 and 12). What it implies can be computed. Taken at the electrical bus,
where the buffer sits — the rotor demand divided by the machine and power-electronics efficiencies, less
what the engine delivers through its generator — **the four closures ask the buffer for 4.7 to 5.2 kW per kilogram of buffer to hover, and 5.5 to 6.1
kW per kilogram of buffer to leave the ground** with the tip pairs at full
thrust, which is where the take-off margin comes from (Section 5).

**What has been measured is a fraction of that, and the figures available are of three different
kinds.** A 24-series nickel–cobalt–manganese pack designed, bench-tested and flown in a 210 kg-class
electric VTOL aircraft is rated, as a flown system, at 0.892 kW per kilogram continuous; its 13.5 kg
unit pack, discharged on the bench at its highest tested rate of 10.68C, delivered on average about
1.5 kW per kilogram for about four minutes and reached 55.1 °C against the 60 °C limit its authors
adopted. A NASA-funded design study adopts 4 kW per kilogram and describes that figure as about twice
that of existing batteries. **The take-off demand of Section 10's closures is 3.7 to 4.1 times the
bench rate — the highest of the measured figures — and 6.2 to 6.8 times the flown system's continuous
rating**; hover alone is 3.1 to 3.5 times the bench rate. The comparison is between unlike ratings: a
peak demand held through the vertical phases, a bench average over minutes, a continuous rating, and a
design assumption. **The gap is real on every one of them; the factor quoted is peak demand against
bench average.** The package Section 10 closes on does not exist with any store the sources consulted
here report as built.

**Closing the loop on a measured store is a sensitivity of that package, not a second aircraft.** The
buffer is derived inside the loop from the take-off demand at a given specific power; everything else is
Section 10's — the same fractions, including an airframe at thirty percent of take-off mass, and the same
wing loading, disc loading and aspect ratio, so the lift-to-drag ratio is carried unchanged and, with the
fuel fraction held, so is the range. **These masses are the Section 10 package with one input changed.
They are not a structural closure at 100 kg**, and whether the airframe fraction holds at twice the mass
it was set at is not established.

| Buffer specific power | Take-off mass | Buffer | Change from Section 10 |
|---|---:|---:|---:|
| As Section 10 implies — 5.5 to 6.1 kW kg⁻¹ | 52.3 to 57.5 kg | 3.6 % | — |
| 4 kW kg⁻¹, the design-study assumption | 56.6 to 61.2 kg | 5.0 to 5.5 % | +6 to +8 % |
| About 1.5 kW kg⁻¹, the unit pack's bench rate | 94.6 to 101.2 kg | 13.4 to 14.7 % | **+76 to +81 %** |
| 0.892 kW kg⁻¹, the flown system's continuous rating | about 335 kg | 22 to 25 % | set by nearness to non-closure |
| 0.724 kW kg⁻¹, the unit pack's continuous rating | **does not close** | — | — |

**At the bench rate the loop closes about three-quarters heavier**, with a buffer of about fourteen
percent of take-off mass rather than 3.6. If Section 10's take-off masses are retained instead, the
payload falls to about 7 kg rather than 13. At the flown system's continuous rating the loop only just
closes, and the mass it returns is set by how near the loop is to not closing rather than by anything
about the aircraft. At the unit pack's continuous rating it does not close at all.

**This is where the coupling Section 12 found is paid.** The buffer is the conversion the escape
condition permits — kilowatts of hover peak paid in kilograms of store. Section 11's ledger records that
conversion at the assumed store; at a measured specific power it costs thirteen to fifteen percent of
take-off mass instead of 3.6. **The escape from Bill 3 is real in the sense Section 3 defined it, and
its price depends on a component whose required performance has not been demonstrated.**

### What the obstacle reaches, and what it does not

**It reaches every number that describes this aircraft at Section 10's masses.** The closed masses of
52.3 to 57.5 kg and the 13 kg payload assume the store. The ranges of 927 to 1 233 km survive the
re-closure only because the fuel fraction is held, on an aircraft three-quarters heavier; they do not
survive as 13 kg carried that far on a store that has been built. The vertical phase that Section 5
reports as sized was sized with this store in it. And Section 13's orderings were computed with the
store held common at 3.6 percent; how they would move with a measured store is not computed.

**It does not reach the mechanism claim.** Sections 7 and 8 count the classes of mechanism that a
tilting architecture needs to change regime and this one does not; that is a statement about hardware,
and a heavier store adds no pivot. **Nor does it reach the cruise-efficiency comparison of Section 6
as a ratio**: effective lift-to-drag ratio combines aerodynamic and propulsive efficiencies and has no
mass in it. As a comparison of aircraft, that section describes the configuration at Section 10's
masses, which the store does reach.

### Then what is not known

The remaining items are not known obstacles; they are questions this work has not answered. They are
grouped by what would settle them.

| Item | Bears on | What would settle it |
|---|---|---|
| **The pitching moment through the transition.** Three methods of three fidelities diverge above about ten degrees of incidence; the rotation passes through that band, peaking near 18 to 22 degrees on the reference geometry, with the inboard half of the wing in the slipstream at a much lower effective incidence. | Whether the aircraft trims through the rotation (Sections 7 and 10) | **Validated aerodynamic data**: a measurement of the outboard wing's pitching moment to about 22 degrees at low dynamic pressure and of trim at the attached-flow end of the rotation, or a higher-fidelity method validated against one |
| **Section drag at low Reynolds number.** The attitude rotors' free-wheeling charge rests on section polars below a Reynolds number of 10⁵, and the uncertainty runs both ways. | The 0.0154 rotor term in every closure (Sections 10 and 11) and the size of Bill 2's fall with scale (Section 12) | **Validated data**: the drag of a free-wheeling attitude rotor, or of its sections, at about 8 × 10⁴, or a method validated there |
| **The tip pairs' other cruise state.** Free-wheeling is determinate and computed; stopped is a family of states whose means and azimuth are not fixed (Section 8). | Whether a lower-drag cruise state is available, and at what mechanism cost | **Analysis**, or a measurement of one stopped state |
| **The buffer's energy, not only its power.** The store is sized here by power. Whether it also holds the energy for the vertical phases and their reserves, and how it is recharged in cruise, depends on a hover duration this work does not fix; at the bench rate the unit pack emptied in about four minutes. | Whether the store sized by power is also large enough | **Analysis** against a defined mission profile |
| **The electrical path at peak.** Machines, power electronics, wiring and their cooling carry the full take-off demand; they enter the loop as a mass fraction, not as components sized for that peak and its heat. | Whether the path that delivers the buffer's power exists at the mass assumed | **Component sizing and thermal analysis** |
| **The airframe's mass.** It enters the loop as a construction constant, thirty percent of take-off mass (Section 11). A component build-up at the reference mass leaves room for the 13 kg payload only if the average shell areal density stays at or below 1.78 kg m⁻², against 1.50 assumed; the build-up carries a contingency rather than a structural sizing, and it has not been re-run at Section 10's closed masses, still less at the masses the store re-closure returns. At the heavy design the shell-mass exponent is not measured at all. | Every closed mass | **Structural sizing** (analysis), then a **built article** (measurement) |
| **The strip and the fairing.** The strip's effect on this planform is computed, not measured, and its actuation is carried in the systems budget without being sized (Section 11); the fairing is sized against a published stability criterion, and the side force it develops is not measured. | The strip: the body roll axis, which appears as bank in cruise and as a change of heading in hover (Section 8). The fairing: directional stability in cruise | **Measurement** of both surfaces; **sizing** of the actuation |
| **Closed-loop hover control**, including the cost of declining the reaction-torque channel, the absorption of the hover torque residual left by trimming each pair's torque balance at cruise (Section 8), and the allocation of the tip pairs between take-off margin and attitude authority, which compete for the same propellers. | Whether hover is controllable with the authority computed (Sections 5 and 8) | **Analysis not yet done**: a control-allocation study, then simulation |
| **Vertical descent and the landing transition.** Neither is analysed; the vortex ring state is not assessed, and the landing transition is not the take-off transition run backwards. | Whether the aircraft can come down as it went up (Section 5) | **Analysis not yet done** |
| **Ground handling and landing loads.** The stance base is a parameter against static crosswind (Section 5); the response to a landing with lateral velocity or on uneven ground, and handling between flights, are not assessed. | Operation from unprepared sites | **Analysis not yet done** |
| **The competitor's lift-group mass.** It decides the sign of the fixed-take-off-mass ordering in Section 13. | Section 13's sensitivity, not a claim | **Measured inventories** of lift-plus-cruise aircraft of this class |
| **Engine installation** — bay, intake, exhaust, cooling. | Mass, drag and packaging | **Absent from this work entirely** |
| **Blade-family selection.** The criteria that would choose among the blade families — structural loads, acoustics, the motor operating point, rotor inertia, manufacture — are not modelled (Section 10). | Which point of the envelope the aircraft occupies | **Analysis not yet done** |
| **Atmosphere.** Every number here is at sea level; the configuration's own altitude sensitivity has been computed for hover power and propeller efficiency, its effect on the Section 6 comparison has not. | The comparison in Section 6, made against a mission flown at altitude | **Analysis**: the direction of the effect has not been computed |

**None of these is a small correction to a known quantity.** Two of them need validated data rather
than more of the computation already done: the transition moment, because three methods have been
tried against it and disagree, and the low-Reynolds section drag, because the one method used here is
least reliable exactly there. Several — hover control, the descent, the buffer's energy, the electrical
path — are analyses this study has not posed. One — the engine installation — is not in the work at
all.

### What this section amounts to

**The loop closes; the aircraft is not shown to.** At the energy store the paper can name the gap
exactly, in specific power and in take-off mass. Everywhere else it can name only what would settle the
question. **The architecture claim — that the configuration is arranged to change regime with no mechanism that
reorients a propulsor — is a count of hardware, and nothing in this section reaches it.** What this section reaches
is the aircraft, and the paper has not claimed the aircraft.

The last section returns to the four axes of Section 9 and states what is claimed on each.

---

## Four axes, and where the paper stops

The paper makes claims on four axes, against four different opponents, and on each it stops where its
evidence stops. They are restated here in the order Section 9 gave them, with what each now rests on.

### Cruise efficiency, against multirotors — claimed, and bounded

**Cruise lift is carried on a surface rather than on rotors**, and no sizing contract or assumption in
this paper moves the configuration out of that state. That is the structural claim, and it stands.
**The size of the advantage is a calculation, not a consequence of it.** Made in one common definition
against two published quadrotors, it is positive throughout against one of them; against the other it
runs from slightly behind to comfortably ahead, depending on the drag outcome and the blade. **What
compresses it is the cruise efficiency of the fixed-pitch blade**, not the wing. The comparison
is between independently produced figures, not a controlled reproduction, and it is not claimed as
more. Nothing is claimed against multirotors on vertical capability, where they are the better machines.

### Operation without a runway, against fixed-wing aircraft — claimed as sized, not demonstrated

**The aircraft stands on its own tail, carries everything it needs to leave and to return, and asks
the site for nothing but ground.** The structure it stands on is the structure that carries its control
propellers. That is a property of the arrangement. **What is sized rather than shown is that it can do
so at the masses reported**: the vertical phase was sized with an energy store whose required
performance the sources consulted here do not report as built, and with a store that has been built the
sizing loop closes only for a heavier aircraft — and at the unit pack's continuous rating not at all. **By construction,
in this paper, means by the sizing, never by demonstration.** Nothing is claimed against fixed-wing
aircraft on range or cruise efficiency, where they are the better machines.

### The mechanism required to change regime, against tilting architectures — the contribution

**The configuration is arranged to change regime by rotating the airframe rather than the
propulsors.** The propulsors hold
their orientation relative to the body from take-off to cruise, and so the configuration carries **no
mechanism that reorients a propulsor** — nor any of the other mechanism classes that architectures use
to change regime or to take a rotor out of one regime's flow: no pivot, no nacelle or rotor-group
actuator, no variable-pitch hub, no dedicated lift rotors, and no rotor stowing, indexing or stopping
mechanism. Pitch and yaw come
from differential thrust between fixed-pitch propellers. **Roll does not come from the propellers**: the
configuration declines the reaction-torque channel its coaxial pairs could provide and assigns that
axis to a single moving aerodynamic surface, the strip; what declining the channel costs is not
computed. The actuator inventory is the propulsion motors together with the strip.

**This is a count of mechanism classes, not a claim that nothing moves, and not a claim of mechanical
simplicity or reliability**, none of which was measured. It rests on the inventory of Sections 7 and 8.
It does not rest on the drag bracket, the propeller efficiency, the sizing contract, the range result,
the energy store, or the transition aerodynamics (Section 9). **Whether this aircraft completes the
rotation is a separate question, and it is not settled here**; the arrangement requires no mechanism to
change regime, and the paper does not claim that it has been shown to change regime.

**The escape condition is met where the aircraft is carried and not everywhere.** The nose pair serves
both regimes in one orientation with the hover peak drawn from a store; the attitude pairs are carried
through cruise producing moments rather than thrust, and the drag they add is reported rather than
absorbed.

### Range, against the other hybrids — not claimed, in either direction

**Against lift-plus-cruise the ordering belongs to the sizing contract.** It moves substantially across
the three contracts examined, and under one of them its sign changes inside the envelope and turns on a
mass fraction of the competitor that has not been measured. **Against the tilting family the competitor
could be modelled here only as a bound that pays no cruise penalty**, and an ordering against a bound is
not a result. A reader who finds a range claim against either family anywhere in this paper should read
it as an error.

### What holds the four together

**The claims are made through an accounting, and the accounting is what makes them checkable.** Hybrid
vertical-take-off aircraft pay for runway independence in three currencies — hover hardware carried
through cruise, its drag when exposed, and continuous power sized by the hover peak. The currencies are
coupled, and every known partial remedy moves cost between them. An escape condition states what an
architecture would have to do to incur none of the three as named; this configuration meets it in the
propulsor that carries the aircraft and pays the rest, and the ledger reports each charge in its own
currency rather than as one number. **At least two of the charges are not locked together, and so,
where architectures trade one charge against another, a ranking is a weighting and belongs to the
contract that makes it.**

### Where the paper stops

**The sizing loop closes on a declared package; the aircraft is not shown to close.** The first obstacle
is known and named: the energy store. The rest are listed with what would settle them — the pitching
moment through the transition, section drag at low Reynolds number, the airframe's mass, hover control,
the descent, and the items this work does not contain at all; Section 14 gives the full list. Nothing
in this work addresses certification.

What the paper offers, and defends, is narrower than a first reading might take it to be: **a
configuration sized to combine runway-independent vertical operation with wing-borne cruise efficiency,
arranged to do so with no mechanism that reorients a propulsor, and an account of what the combination
costs.**
