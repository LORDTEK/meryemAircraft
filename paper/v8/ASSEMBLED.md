# v8 — assembled view (generated; the fifteen steps are the source)


## 1. The gap

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

### The problem has been attacked for seventy years

Tail-sitting prototypes and the first tilt-rotor flew in the 1950s, vectored-thrust and tilt-wing
aircraft in the 1960s, and a broad family of hybrid vertical take-off and landing uncrewed
aircraft since roughly 2010. Different nations, services and propulsion philosophies have
attacked the same problem for seventy years.

### What the contemporary answers do, and how each changes regime

Hybrid VTOL aircraft occupy that corner today. **This paper does
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

### The third route is established, and some of its difficulties are inherited

There is a third way to put one set of propulsors into both regimes without reorienting them: **point the
thrust line at the ground and let the whole aircraft rotate.** It is neither new nor untried nor abandoned.
The Convair XFY-1 flew it in 1954 and completed six transitions to conventional flight *"before testing was
curtailed because of engine and gear-box reliability problems"*, and uncrewed tail-sitters have revisited the
route continuously since. The pilot's spatial orientation and workload, recorded for that programme, were real
and severe, **but they are not what curtailed the testing**, and they are the only one of those documented
obstacles an uncrewed aircraft removes.

**Some of the difficulties were real, internal, and are inherited here.** A tail-sitting vertical descent is
harder than a runway landing; a tail-sitter on the ground is more exposed to crosswind; and propellers whose
thrust vectors are all parallel to the body axis produce no rolling moment **by any combination of thrust
settings**. The reaction-torque channel that other coaxial tail-sitters use about that axis is a choice this
configuration declines rather than a limit it inherits (Sections 5.1 and 5.2).

Three things are available now that were not: electric drive on each individual rotor, sensor-based attitude
reference, and enough onboard computation that stability need not come from the airframe alone. **The uncrewed
tail-sitter literature has been exploiting exactly those three for over a decade**, which is why the gap below is
not a historical one.

### What is already occupied, stated before the gap

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
long-range tail-sitter reported in 2018 that uses a cyclic- and collective-pitch rotor still describes it
as *"a compromise between efficient hover and efficient forward flight"* and selects its diameter on
that basis; the same paper names variable pitch as the remedy for fixed-pitch propellers, at the cost of
extra actuators and the weight of the mechanism.

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

Each of those choices costs something, and **the giving-up is the part that is not free**. A
quadrotor tail-sitter produces a rolling moment from the reaction torque of four independently
driven rotors; a coaxial pair can produce one the same way, by running its two rotors at different
speeds. **Operating every pair torque-balanced spends that channel to buy the torque balance and
the near-zero net angular momentum**, and leaves the axis to a single aerodynamic device. What
that costs, and what the rest of the combination costs, is what the paper is for.

**None of the elements is new**, and Section 5.1 says so. Tail-sitting aircraft are seventy years
old and uncrewed ones are ordinary; blended wing bodies have been a standing subject of transport
research for three decades; series-hybrid propulsion has been flown in a crewed motor glider and designed for small uncrewed aircraft. The route is not claimed to have been waiting to be found. **The contribution is the
architecture: a configuration arranged to change regime by rotating the airframe rather than its
propulsors, and so carrying no mechanism that reorients a propulsor.** The combination, the
consequences of the choices inside it, and an accounting of what they cost are how that contribution
is presented and priced.

Section 2.1 states the cost that any architecture in this corner pays, in terms that do not
presume an escape.

## 2. The charges, the condition, an independent check

### 2.1 The tax

A claim that one architecture escapes a cost shared by the others is only meaningful if the
cost is stated first, in terms that do not presume the escape. This section states it. It is
not a claim about any particular aircraft, and nothing in it is new physics; what it provides
is the accounting that the rest of the paper is checked against.

#### The root: a duty cycle that does not match the hardware

The vertical phase is short. For a mission of one hour, a take-off, a transition, a return
transition and a landing occupy on the order of a minute — **roughly two percent of the flight.**
Any hardware installed for that phase alone is carried through the remaining ninety-eight
percent.

**An architecture that provides the vertical phase with a dedicated lift subsystem therefore
carries it for fifty times as long as it uses it.** This is not an implementation defect and it
cannot be removed by making the subsystem better, because it is a statement about duty cycle
rather than about quality: a lighter or cleaner lift rotor is still carried for the whole flight. **The mismatch between how long a
component is needed and how long it is present is the origin of all three charges below.**

The statement is deliberately confined to architectures with a dedicated lift subsystem, because
that is the family the charges describe. Whether any architecture avoids the mismatch — and what
it pays instead — is the subject of the next section, and it is not settled here.

#### Bill 1 — mass

The most direct payment is dead mass. A lift-plus-cruise aircraft carries two propulsion
groups: rotors, motors, mounts, wiring and structural reinforcement for the vertical phase, and
a separate propulsor for cruise. The vertical group provides no required lift or thrust during cruise and is
lifted anyway.

Its cost is not linear. Mass growth feeds itself — MTOW = m_payload / (1 − f_empty − f_energy)
puts additional empty mass through a multiplier that grows as the denominator shrinks — and in
the vertical phase the same increment is counted a second time, because at a fixed disc area
hover power scales with W^1.5. *(The exponent is a property of the scaling rule chosen: holding
disc loading constant instead makes hover power grow linearly with weight, and Section 7.3 uses
that.)* A modest dead-mass fraction becomes a large payload penalty.

**This charge has been identified independently, and by a source with no interest in the present
argument.** A NASA study sizing five VTOL architecture families against a common mission with common
tools found the lift-plus-cruise concepts the heaviest of the vehicles examined, and named the
cause: not the cruise power draw, since the lift-plus-cruise effective lift-to-drag ratio is the
higher of the set, but *"the extra empty weight items on board in hover."*

**That finding separates the two things this paper is at pains to keep separate.** The
lift-plus-cruise vehicle is *aerodynamically better* than the alternatives and it is nevertheless the heaviest, because of
hardware carried in order to hover. That is Bill 1 stated by an independent source in its own
terms: not a failure of engineering, but the cost of an architecture.

A second NASA review gives the structural half as a general principle, drawn from a tilt-prop
aircraft whose propeller separated in flight after a gearbox mounting fatigued: to transmit
power safely to the extremities of the planform, *"very strong (and fatigue-resistant)
structures must be incorporated with an obvious weight penalty."* Distributing lift or thrust
across the span therefore obliges the structure that reaches it to keep transmitting power
there — charged to mass, whether or not the distributed propulsors are running.

#### Bill 2 — drag

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
regime exceeding either pure mode through adverse flow interaction; and that a simulation assuming negligible rotor–structure
interaction *"always predicts higher lift and lower drag than were experimentally observed."*
Separately, a study of twenty-six stationary lift propellers held edge-on found their drag
scaling with frontal area and the square of airspeed, with hover powertrain components adding
*"a significant amount of aerodynamic drag during forward flight"* in the absence of a stowing
mechanism.

**The important property of this charge is not its size but where it falls.** It is charged per
unit time in cruise — so it grows with exactly the quantity the aircraft exists to maximise.

#### Bill 3 — power system sizing

The third payment is the least visible. A VTOL aircraft must install
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
and on the condition it is run at, and Section 7.2 computes what happens when one fixed-pitch
blade has to supply both.

A vehicle with a disc loading of 100 N m⁻², a cruise lift-to-drag ratio of 15 and a cruise speed
of 30 m s⁻¹ needs **between three and four times** as much power to hover as to cruise: the
geometric terms alone give 3.2, and the efficiency ratio η_p/η_h carries it to about four when
the cruise propeller is roughly a quarter more efficient than the hover rotor. Raising the disc
loading raises the ratio as its square root.

The power system is therefore sized by a condition that holds for a minute and is then carried,
unused, for an hour. And the consequence propagates: sizing by hover means an oversized engine,
or a battery that must deliver a peak it will rarely be asked for, or both — and whichever is
chosen, the extra installed capacity is mass: a cost in kilograms, though not Bill 1.

#### The charges are coupled: remedies move cost, among the three charges or outside them

The three charges are not independent problems with independent fixes. **Each known partial
remedy reduces one charge and pays for it, in another charge or in a cost outside the three.** They are three distinct accounting quantities, paid in kilograms,
drag counts and installed kilowatts, and they are not assumed to be independent physical causes: a
remedy can move a requirement from one currency into another. Whether a change of size moves them
together, which would make them one quantity under three names, is tested in Section 7.3.

**A charge and its currency are not the same thing.** The mismatch of the root is the origin of all three charges; each
charge is one specific payment, not the name of the currency it is paid in. Bill 1, as this accounting uses it, is the mass
of a dedicated lift subsystem; Bill 2, the cruise drag of hover hardware left exposed; Bill 3, continuous power installed
to a hover peak. A remedy's own cost can fall in kilograms, drag counts or installed kilowatts without being one of the
three charges, and the table names such a cost in words rather than by a bill's number.

| Move | Bill it attacks | What it creates — a bill by its number, any other cost in words |
|---|---|---|
| Distributed electric lift rotors | 3 — the cruise engine no longer sizes to hover | 1 and 2 — many rotors and mounts, permanently carried and exposed |
| Folding or retracting lift rotors | 2 — the exposed rotor is removed from cruise | 1 — mechanism, actuation, locking; and a new failure mode, not among the three |
| Tilt-rotor, tilt-wing, tilt-nacelle | 1 — one propulsion group serves both regimes | kilograms, not Bill 1 — the pivot and its actuators; **Bill 3**, imposed or left standing according to how the architecture the move modifies supplies its hover peak — with no store, the power plant is sized by the hover peak; and gyroscopic coupling and a transition control problem, which are **not among the three** |
| Variable-pitch or feathering propulsors | 1 and 3 — one propulsor is retrimmed across two widely separated operating points instead of duplicated | kilograms, not Bill 1 — pitch hub and actuation; and a new failure mode, not among the three |
| Higher disc loading, smaller rotors | 1 and 2 — smaller, lighter, cleaner rotors | 3 — hover power rises with √(DL) |
| Lower disc loading, larger rotors | 3 — hover power falls | 1 and 2 — larger structure and exposed area |

**One row pays part of its cost in none of the three currencies, and that is not an oversight.** What a
tilting architecture buys its unified propulsion group with is a mechanism — a pivot, an
actuator, the gyroscopic coupling of a reorienting mass, and a control problem through the turn.
The pivot and the actuator are paid in kilograms, although they are not lift-subsystem mass; the
coupling and the control problem are paid in none of the three. That part is a cost, but it is not
one of the three charges this accounting tracks, and the next section says why it is treated
separately. **The table is not a census of the field**; it lists
the moves whose transfers are documented, and a remedy absent from it is not thereby claimed to
cancel a charge.

**One of these transfers has direct experimental support.**
In the doctoral study whose wind-tunnel campaign is quoted above — and in that document rather
than in the journal article by the same author, which reports a different comparison — a
retraction system removed thirty percent of the airframe's drag; the same work then costed it. Applied to a passenger eVTOL, with the mechanism assessed
at five percent of vehicle mass, maximum range rose from 119 km to 121 km — **a two-kilometre
gain for a five-percent mass penalty.** The same work finds the retraction's advantage elsewhere — the speed that
maximises range rose by 5 m/s — which is a performance this accounting does not price. Bill 2 was converted almost exactly into Bill 1, and
**the transfer is the point rather than the small residue.**

#### What this accounting is for

**The accounting is refuted by a counter-example, and the table above is where one would appear:**
every entry in it moves cost rather than removing it.

**Stated positively, so that the test can actually be run: a counter-example is a remedy that
reduces one of the three charges, leaves the other two no worse, and whose own cost is either
absent or demonstrably smaller than the reduction — measured in the same currency.** That last
clause is what makes the test usable rather than rhetorical: mass against mass, cruise drag against
cruise drag, installed continuous power against installed continuous power. **The accounting claims
transfer. It does not claim that every architecture is equally good**, and a remedy that is simply
a better bargain in one currency refutes it.

**Two clarifications keep the test from being either too easy or unfalsifiable.** **"No worse" is
judged against the architecture the move modifies.** A charge that architecture already paid, left no
larger, is no worse. A charge it did not pay, imposed by the move, is worse; so is one it paid, enlarged
by it. A move that reduces one charge and makes another worse is a transfer between charges. And a remedy whose cost
falls **outside** the three charges does not refute the accounting, because the accounting is about
those three; **but it is not thereby exempt from being counted.** The tilting family's mechanism is
named in the table for exactly that reason, and it is the reader's to weigh against what the
remedy buys. **A framework that could absorb any cost by declaring it out-of-scope would be
unfalsifiable**, so the costs outside the three are listed, not waved away.

**The tilting row needs both clarifications.** If the architecture it modifies supplies its hover peak
from a store, tilting without one imposes Bill 3 and the row is a transfer between charges. If that architecture
already sizes its continuous plant by the hover peak, tilting leaves Bill 3 no worse; then, where the
mechanism's kilograms are fewer than those of the lift group it removes, what keeps the row from
refuting the accounting is the part of its cost that falls outside the three — which is why that part
is listed.

It also makes a prediction that can be checked without settling the architectural question at
all: **where an arrangement pays one charge heavily in order to escape another, its ranking
against a differently-balanced arrangement will move when the sizing rule changes — toward the
lighter arrangement as the rule weights mass more — and will reverse where that reweighting carries
it past the point at which the two break even, where the mass difference as the contract counts it and
the cruise-efficiency difference cancel in the range.** Section 7.4 tests both the
movement and the reversal on this configuration, and Section 2.3 tests a different consequence
against a sizing study this work did not produce.

**The moves in the table are partial remedies: each accepts the duty-cycle mismatch and then
redistributes what it costs.** Whether an architecture can decline the mismatch itself, rather
than redistribute its consequences, is a different question, and the next section states the
condition it would have to meet — a definition, derived from the table above rather than from
any aircraft.

### 2.2 The escape condition

This section asks what an architecture would have to do in order not to incur the three charges at
all. The answer is a **definition**, derived by inverting the table, and it is stated here before any
configuration is offered so that the standard is not taken from the thing it will be used to measure.

#### Inverting the table

**A charge appears wherever the two regimes are served by hardware that departs from one of four
things: the same hardware, serving both duties, held in one orientation, with the hover peak supplied
other than by its continuously installed power.** **Different hardware** costs Bills 1 and 2. **The
same hardware serving only one duty** costs them again: a propulsor that lifts and is then carried is
a dedicated lift group under another name, whatever it shares with the cruise system. **The same
hardware serving both duties in a different orientation** is the tilting family: Bill 3 is incurred
unless a store supplies the hover peak, and the mechanism that changes the orientation adds mass and
introduces a control problem through the turn. **The same hardware, both duties, one orientation, but
a different sizing point** incurs Bill 3 — unless the hover peak is supplied from somewhere other than
the continuously installed power.

Read one at a time, these are ways to pay. Read as a conjunction, they are a condition.

*(The second departure is stated separately because it does real work later: a propulsor that
produces a little thrust in cruise is not thereby serving both duties, and the distinction decides
which parts of a configuration meet the condition and which do not. "Serving both duties" is the
accurate form; hover thrust and cruise thrust are not the same **job** in any ordinary engineering
sense — one supports weight, the other balances drag.)*

#### The condition

> **An architecture does not incur the three charges if the propulsors that carry the weight,
> held in one orientation relative to the airframe, produce both the hover thrust and the cruise
> thrust, and if the difference between the hover peak and the cruise demand is supplied from
> a store rather than from permanently installed continuous power.**

Four parts: **same hardware, both duties, one orientation, hover peak from a store.** The first
three come from the first three departures; the fourth comes from the fourth.

Two things in that sentence are choices rather than derivations. The
inversion requires only *one orientation relative to the airframe*; **how** an architecture keeps
that while changing flight regime — by rotating the whole body, or otherwise — is not in the
inversion, and is treated as exposition rather than as part of the definition. And the fourth
departure's exception lets the peak come from **any** source other than the continuously installed power; a
store is the narrower reading used here, because it is what the configuration examined later
uses and because a narrower condition is easier to fail.

#### What the condition does not say, and this matters more than what it says

The condition has to be read exactly.
**It means zero of the three charges as Section 2.1 defines them.** **It does not mean an architecture that costs nothing, and it does not mean an
architecture that carries nothing for the vertical phase.** A definition that placed every
conceivable cost inside the thing to be escaped would be unfalsifiable, and an architecture
built to satisfy it would win by construction rather than by performance.

The costs the condition permits are named here, before any candidate is examined. Six of them:

- **A store is permitted, and it has the same duty-cycle character as Bill 1.** The fourth part
  moves the hover peak off the continuous power plant and onto a store; that store delivers its
  peak for two percent of the flight and is carried for the rest. It is not Bill 1 as Section 2.1
  defines it — it is not lift-subsystem mass — **but it is mass carried for a duty that is
  briefly needed, which is the same complaint Bill 1 makes.** The condition converts a power-system
  charge into a cost in kilograms and claims only that the three charges as named are not incurred.
  **It does not claim the trade is favourable.** Whether the store is lighter than the continuous
  power it displaces is a sizing result and is computed, not asserted.
- **Releasing the engine is not releasing the electrical path.** The fourth part frees the
  continuous *power plant* from the hover peak. Everything between the store and the rotors —
  machines, power electronics, wiring — still passes the full hover power and is still sized by
  it. **That is Bill 3 on the electrical path, and the condition does not remove it**; it is carried
  in the ledger rather than in this definition.
- **Rotating the airframe is permitted and is not priced here.** The condition refuses
  architectures that reorient a propulsor, and sets that refusal against the mechanism a tilt
  requires. **An architecture that instead rotates its whole body faces the same physical
  problem** — a ninety-degree change of the thrust axis relative to the flight path, with the
  moments, the authority and the control through the turn that implies. It is not one of the
  three charges and the condition does not eliminate it; it is priced where the transition is
  analysed. Saying otherwise would let a candidate win that line by wording.
- **Hardware installed for the vertical phase is permitted if it serves both duties**, and the
  second departure is what carries the weight.
- **Hardware used in both regimes for something other than propulsive thrust is permitted, and its
  cruise drag is not eliminated.** *Cruise thrust in this paper means the thrust that balances
  cruise drag.* Attitude devices produce thrust in cruise, but they produce no cruise thrust in
  that sense; they are used throughout the flight, so their duty cycle matches their presence and
  they fall outside Bill 1. **They remain in the airstream, so the second charge reaches them.**
  **Attitude hardware does not
  stop the propulsor that carries the aircraft from meeting the condition, but it is carried through
  cruise without producing cruise thrust, which is the first failure mode below — and the charges
  are about everything the aircraft carries, so Bill 2 reaches it.** An architecture in that
  position is a partial instantiation, the fourth failure mode: it meets the condition where it
  carries the aircraft and still pays one of the three elsewhere. The condition permits such
  hardware outside the first charge and does not make it free.
- **Serving two regimes with one set of hardware has a price of its own.** Hardware that is not
  duplicated cannot be optimised twice: a propeller sized for hover thrust at zero forward speed
  is not the propeller a cruise design would choose, and if its geometry is fixed the compromise
  is paid in efficiency. **The condition permits that cost and does not measure it.** Section 7.2
  does.

**One exclusion, stated narrowly.** Structure, surfaces and actuation present for reasons other
than the vertical phase are not charged **as duty-cycle mismatch under this accounting** — a
wing, a control device, a fairing that earns its place on a part already carried. That is a
statement about which ledger they belong in, not a claim that they are free, and it does not
apply to a part that would not exist but for the vertical phase. The tip frames are the case
that tests it: they are landing gear because the aircraft stands on its tail, and they also
carry the attitude propulsors and the directional fairing. **Their mass is charged in the
build-up and their drag in the ledger; the exclusion does not reach them.**

#### The condition can fail, and how

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

#### What follows from the condition, and what does not

The condition is a statement about what an architecture would have to be. **It is not a claim
that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim
that satisfying it is desirable.** Three questions follow from it, and they are answered
separately: whether the accounting behind the condition survives contact with an independent
sizing study is tested in the next section, against data this work did not produce; whether any
configuration satisfies the condition is the subject of Sections 3 to 5.1; and what such a
configuration pays instead is the subject of Section 7.2, the answer most likely to be wrong.

One consequence is worth stating now, because it shapes everything after it. The third departure is refused by a means other than the
one the field has adopted. A tilting architecture accepts that departure and buys its way out of the first departure with a mechanism. **An architecture that reorients a propulsor does not satisfy the condition as written**, because
the condition requires one orientation relative to the airframe. **Whether such an architecture
might avoid the three charges by some other route is a separate question this paper does not
settle** — the condition is a definition, not a law, and it can be too narrow without being
wrong.

### 2.3 An independent quantitative check

An accounting proposed by the same people who then use it invites one obvious objection: that the charges were chosen because a particular aircraft happens not to pay them. The objection arises at the title, not at the ledger, so it is answered here — before any configuration is described — by testing a prediction the accounting makes against numbers this work did not produce. **What follows is not a test of the whole framework.** It checks one falsifiable consequence on one independent data set.

**The prediction has two halves, and only the first is a derivation.**

> **First half, derived from Section 2.1.** A configuration carrying a dedicated lift system pays for it in gross weight, and the payment is amplified: additional empty mass enters through a multiplier that grows as the empty-mass fraction rises, and the same increment is counted again in hover.

> **Second half, not derived.** That the cruise efficiency the arrangement buys does not cover that payment. Section 2.1 predicts the charge and the amplification; **it does not prove that the credit must lose.** A dedicated lift system raises the empty-mass fraction and may lower the energy fraction at the same time, and which wins is a closure result rather than a consequence of the accounting.

The check tests the second half on independent data, with the first half supplying the reason to expect the outcome: the weight charge is amplified by a multiplier, while the efficiency credit enters linearly through the cruise lift-to-drag ratio. **If some data set showed the credit covering the charge, Bill 1 would not be refuted** — the mass would still have been paid. What would be refuted is the expectation that the amplified charge outweighs the linear credit. **The prediction is also mission-dependent**, and the page would be weaker for hiding it. The mass charge of carried lift hardware is roughly fixed; the efficiency credit accumulates with distance. A long enough mission is where the credit is most likely to cover the charge, and the mission used below is short. **The counter-set is therefore a common-mission sizing study at longer range in which a dedicated-lift configuration is both more efficient and no heavier than one without.** None is known to the authors.

The check uses a NASA study, conducted for its own purposes and with no relationship to the present work, that sizes **five VTOL architecture families** — nine designs in all — against a single mission with common tools and common assumptions; it does not use the three-bill accounting of Section 2.1 or any framework derived from it. It is used for three reasons, stated so that the choice is not merely the one that agreed: it holds the mission fixed across architecture families, it applies one set of tools to all of them, and it reports both quantities this prediction needs. The mission is 1 200 lb of payload over 75 nautical miles. Three of the nine designs matter here. The turboshaft quadrotor reaches an effective lift-to-drag ratio of 4.9 at a design gross weight of 3 678 lb, with no dedicated lift group: its rotors serve both regimes. **The turbo-electric lift-plus-cruise design reaches 8.5 at 7 271 lb and carries a dedicated lift group — eight lift motors beside its cruise motor. The turbo-electric tilt-wing reaches 8.6 at 6 584 lb with none: eight proprotors, reoriented.**

**The primary comparison is the lift-plus-cruise design against the tilt-wing**, because they isolate the charge: they share the mission, the payload, the turbo-electric propulsion architecture and the presence of a cruising wing. **They are not identical in every other respect** — one stops its lift rotors in the airstream and drives a separate pusher, the other reorients its proprotors on a tilting wing — **but the difference the comparison turns on is that one carries a dedicated lift group through cruise and the other does not.** The comparison is the closest the published set comes to isolating that charge; it is not a controlled experiment. **The tilt-wing is 1.2 % better in effective cruise efficiency and 9.4 % lighter.** The dedicated lift group buys no cruise-efficiency advantage at all here — it is marginally behind — and the design gross weights differ by 687 lb in the tilt-wing's favour. **That figure is the net difference between two architectures, not the measured mass of a lift group**, and the published weight breakdown is what makes it informative rather than merely large. **The published weight breakdown is consistent with the transfer property of Section 2.1 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce**: its three reported categories account for 580 lb of the 679 lb empty-weight difference, and the remaining 99 lb lies in categories it does not break out (Supplement S4). **And the source states the second half of the prediction in its own words.** Discussing why the all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery weight compared with the quadrotor, *"but not enough to counter the increase in structure and propulsion weight."* That is the efficiency credit conceded and found insufficient, by the authors of the data rather than by the authors of the prediction. **The quadrotor is reported for scale, and the isolation test above is what carries the prediction**: against it the lift-plus-cruise design changes three things at once, and the contrast is in Supplement S4. **The framework does not predict any of these numbers**; without the input fractions it predicts no magnitudes. What it predicts is that the amplified weight charge survives the efficiency credit, and on the isolated pair it does so with the credit reduced to nothing.

**The architecture proposed later in this paper is not the only way to avoid the first charge.** The tilting family avoids it too — it carries no dedicated lift group, it is the lighter of the two matched designs, and an independent set says so. The margin in cruise efficiency is one tenth and nothing is claimed from its direction. **The tilt-wing is consistent with the transfer property of Section 2.1, in someone else's data.** It does not escape the accounting by avoiding the mass charge; it *moves* the cost — to the mechanism that reorients its propulsors, with the actuation, the gyroscopic coupling and the transition control problem that Section 2.1 assigns to that family. What separates the tilting family from the configuration described later is not this axis; it is what each pays, and a sizing study does not settle that.

It establishes that one prediction of the accounting holds on data produced elsewhere, for purposes unrelated to this argument. That is the whole of it. **It does not establish that the accounting is complete**, that the three charges are the only costs an architecture pays, or that avoiding them makes an aircraft better. The accounting says an architecture that avoids the three is cheaper in those three currencies and nothing more; a configuration may avoid all three and still be unbuildable, uncontrollable, or unsuited to its mission. Sections 7.1 and 8 are about exactly that possibility for the configuration proposed here. **It does not establish anything about the configuration this paper proposes**, which has not yet been described, and which is not in the study used here. A reader who wants to know whether the accounting flatters that configuration will have to wait for Section 7.2, where it is applied to it and where the answer is not uniformly favourable. **An instrument whose first use is to measure the thing its authors are advocating should be shown working on something else first**, and that is why this section comes before the aircraft. **The instrument is now fixed, and it is not modified again.** **Everything that follows is measured with it rather than added to it.** The next two sections describe the two capabilities the mission asks for, one at a time and each against the family that structurally lacks it, before Section 5.1 asks whether one aircraft can hold both.

## 3. The first half: operation without a runway

### The opponent, and the axis

On this axis the alternative is the fixed-wing aircraft, and the comparison runs one way only.
**Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency**, where a
runway-launched aeroplane that never bought vertical capability pays none of the charges of
Section 2.1 and is the better machine. The claim is confined to the one thing that family cannot
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
both benefits arrive from one change. The 50 kg reference geometry is one point on that trade; an
operator with a stronger ground-wind requirement can take another.

### What is sized, and what is not demonstrated

**Sized.** The vertical phase is sized: hover power from momentum theory at thrust equal to
weight, the buffer that supplies what the engine cannot deliver of that peak — at a specific power
Section 8 examines — the
tip-frame lengths that set both the stance base and the control arms, and the structure that
carries the landing loads. Those numbers exist and Section 7.1 reports **whether** they close, and
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
is an open question in Section 8 rather than an answered one here.

**Neither has the landing transition.** The forward rotation and the reverse are not symmetric
and must not be assumed to be. Going out, the rotation builds dynamic pressure while it turns,
so lift arrives to replace the vertical component of thrust as that component falls. Coming
back, the race runs backwards: dynamic pressure is falling while the aircraft is being turned,
so lift is leaving at the moment the thrust vector has not yet returned to vertical. **A model
built for the first case cannot be read for the second by changing a sign, and no figure in this
paper describes the landing transition.**

**Hover attitude control is sized but not demonstrated as a closed loop.** The moments available
about each axis are computed, but no control allocation has been closed around them and nothing
has been simulated or flown. That gap is wider than it looks, because this configuration declines the reaction-torque channel that comparable
aircraft use about the body's longitudinal axis (Section 5.2), leaving that axis to the strip.
**What that refusal costs in authority and in response time is not computed**, and Section 8
carries it.

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
airstream, and Section 7.2 charges their drag. The attitude propellers they carry are exposed
for the whole cruise and cannot be feathered, and Section 7.2 charges that too. The buffer that
releases the engine from the hover peak is mass carried for the whole flight.

**The second half — cruise carried on a wing rather than on rotors — is the subject of the next
section**, and the two are combined in Section 5.1.

## 4. The second half: cruise carried on a wing

### The opponent, and the axis

On this axis the alternative is the rotorcraft, multirotor and helicopter alike, and as in the previous section the comparison
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

**Cruise lift is carried by the airframe itself.** There is no separate fuselage: the whole
planform is the wing, so every part of the body that is carried is also a part that lifts. At
the cruise condition the lift coefficient follows from `C_L = W/(qS)`, the drag from
`C_D = C_D0 + C_L²/(πARe)`, and the nose pair is left with one job — producing the thrust that
balances that drag. It supports none of the weight.

That is the whole of the difference, and it is worth stating in those plain terms because the
consequence is structural. **A rotorcraft's rotors must produce the lift and the propulsive force
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

The sizing set of Section 2.3 reports an **effective lift-to-drag ratio**, defined in its own
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

- **Examined envelope, 5.56 to 7.39.** **The four corners are not demonstrated aircraft
  states**, and nothing here
  shows that a built aircraft would land simultaneously on both bounds.
- **Best examined blade family, 6.00 to 7.39.** The highest efficiency among the families
  examined is 0.683; holding it and sweeping only the drag bracket gives this range.

**Whether 0.683 is the blade a designer would actually choose is not settled here**, and saying
so is the point. It is the best of the four *on cruise efficiency under the hover figure-of-merit
constraint*. Blade count and section loading also govern structural loads, acoustics, the motor
operating point, rotor inertia and manufacture, and **none of those is modelled in this work**.
Section 7.1 is where one blade is carried into a closed sizing loop; until then this section stays
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
consistent with the mass charge Section 2.1 describes**, and Section 2.3 is where the independent
sizing evidence for it is set out — the comparison in this table does not establish the causal
link by itself. On cruise efficiency taken alone, the entry is ahead of this configuration's low
corner, and whether it is ahead of the best examined blade family depends on the drag bracket.

The same sizing set gives its two helicopter types at 5.4 to 7.2, and against them the result is
mixed: this configuration is ahead of the turboshaft single-main-rotor helicopter at every corner,
the two middle entries fall inside its envelope, and only its top corner is ahead of the
all-electric side-by-side helicopter, which has no wing either. The qualifications below apply to
these entries as they do to the quadrotors.

**So the second claim is narrower than the structural statement invites.** Carrying cruise lift on
a wing is worth **roughly a quarter to a half against the turboshaft reference, and against the
all-electric one it ranges from slightly behind to comfortably ahead depending on the drag outcome
and the blade** — a measurable advantage, not a change of category. And what
compresses it is not the wing. **It is the cruise efficiency this aircraft's fixed-pitch blade
delivers:** at a propeller efficiency of 0.85 the same airframe reaches 7.47 to 9.20. Whether a
variable-pitch hub would recover that difference is not computed; Section 7.2 reports the gap and
declines to attribute all of it to the hub.

### Five qualifications: three run against this configuration, one has no computed direction, and one bounds what the comparison can be called

They are given together because omitting any one of them would make the comparison look better
than it is.

**Scale.** The compared vehicles are 1 660 to 3 275 kg; the designs here are of order 50 kg and
1 000 kg — Section 7.1 closes the light one between 52.3 and 57.5 kg across the same bracket.
Reynolds number favours the larger aircraft, so the smaller design is at a disadvantage in this
comparison rather than an advantage.

**The quadrotor is a good quadrotor.** Its disc loading is 3.5 lb ft⁻², and the all-electric one's
is 3; both are unusually low. Nothing here is compared against a poor example.

**The speeds are not matched, and the direction of that mismatch is calculable.** The published
figure is quoted at the best-range speed; this configuration's is at its chosen cruise condition,
1.49 times stall, which Section 7.1 states explicitly is **not** its best lift-to-drag point. The
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
performance metric at a prescribed cruise condition, taken before the sizing closure Section 7.1
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
rather than higher. Section 7.2 charges all three.

**The two halves are now on the table separately. Section 5.1 is where they are combined**, and
the combination is what this paper is for.

## 5. Combining the solutions

### 5.1 The combination

None of the three elements is new. **Each can be found on its own, and in
combination, in the literature and in hardware** — Section 1 says where.

**What this paper contributes is that combination, the condition its primary propulsor is designed
to satisfy, and the price the configuration pays for pursuing it.** The three elements, taken together, meet the escape condition
of Section 2.2 **in the propulsor that carries the aircraft**, and they meet it with no mechanism
that reorients a propulsor. The assembly is not offered as novel because it is an assembly. It is
offered for what it satisfies, and for what it does not need in order to satisfy it — and Section 1
has already set out how much of the ground is occupied.

**The qualification in that sentence is not decoration, and it is made here rather than
conceded later.** Section 2.2 lists partial instantiation among the ways an architecture can fail
the condition: meeting it where the aircraft is carried and failing it elsewhere. That is this
configuration's own case. The single nose pair meets all four parts — same hardware, both duties
served, one orientation, hover peak from a buffer. The four attitude pairs do not: they are exposed
in the cruise flow and they cannot be feathered, so they re-open the second charge. **The
instantiation is therefore partial**, and reporting what the failing part costs is a substantial
share of what Section 7.2 does.

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
  of the flight. The series arrangement is used here for the electrical path it gives the buffered
  hover peak, not because this study assumes it is the more efficient hybrid architecture.

The configuration is arranged to change regime by **rotating the airframe**. The propulsors hold
their orientation relative to the body from take-off to cruise; what changes is the
orientation of the body relative to the flight path. A tilting architecture reaches the
same end by turning its propulsors instead, which requires a pivot and an actuator and
introduces gyroscopic coupling from the reorienting mass and a control problem through the
turn. It does not satisfy the condition as stated: the condition requires one orientation
relative to the airframe, and turning the propulsors is the case the condition excludes.
Here the end is reached by turning the thing the propulsors are already attached to, which
leaves the orientation requirement intact.

That single move is what removes the need for the mechanism. **The table below counts mechanism classes that
exist in order to change regime, or to take a rotor out of one regime's flow.** The strip of Section 5.2 is a
control surface, of a different class, and is named below and in Section 5.2 rather than in the table. The configuration therefore carries:

| Mechanism | Where it is required | Present here |
|---|---|---|
| Pivot or tilting joint | Tilting architectures | — |
| Nacelle or rotor-group actuator | Tilting architectures | — |
| Variable-pitch hub | Architectures that trim a rotor across two widely separated operating points, or feather a rotor unused in one regime | — |
| Dedicated lift rotors | Lift-plus-cruise architectures | — |
| Rotor stowing, indexing or stopping mechanism | Architectures that remove dedicated lift rotors from the cruise flow by such means | — (see note) |

*Note.* The stopping class is absent if the tip pairs free-wheel in cruise or are held stopped by motor torque; a
brake or a mechanical lock would add it. The means of stopping is not fixed by this study (Section 5.2).

Attitude is produced instead by differential thrust between fixed-pitch propellers: a
single coaxial contra-rotating pair at the nose, and four small coaxial pairs at the
ends of the tip frames, whose moment arms give pitch and yaw directly. The tip pairs are
sized from the moment requirement rather than from weight support, but the thrust that sizing
gives them also supplies the aircraft's entire take-off margin, because the nose pair is sized
at thrust equal to weight and no more. This dual role is a dependency, reported as one where the sizing is audited, and it does not make the tip pairs a dedicated lift system.

**The claim is narrower than it may appear, and the boundary matters.**

This is not a configuration in which nothing moves. Roll cannot be produced by the
propellers' **thrust**: every thrust vector is parallel to the body axis, so no combination
of thrust settings produces a moment about that axis. It **could** be produced by their **reaction
torque**, and this configuration declines that channel by design (Section 5.2), assigning the axis to an aerodynamic
device instead. The device is the only moving aerodynamic
surface on the aircraft — a variable-extension strip on the lower surface, modulated rather
than switched, which also pitches the nose down by a small increment when it is deployed. The
strip is part of the configuration and is named here rather than later, because a claim about
eliminated mechanisms that omitted it would be false.

A fixed-pitch propeller that serves two regimes pays in efficiency in at least one of them. The nose pair holds one
orientation, which is the architectural claim, but it also holds one blade geometry across a
hovering condition and a cruising one, and no single fixed-pitch blade is at its best in both.
That is a price of refusing the variable-pitch hub rather than an argument against refusing it,
and it is charged in Section 7.2 with the other costs of the union, not settled here.

Nor is this a claim of mechanical simplicity. Part count, mass, failure modes and
maintenance burden were not measured, and nothing in this work supports a statement
about reliability. What is offered is a **count**: the classes of mechanism that a
tilting architecture requires to change regime, and which this arrangement does not
require. The actuator inventory that replaces them is the propulsion motors together
with the strip.

**One thing this section does not establish, and Section 6 holds it to that.** The arrangement
described here requires no mechanism to change regime. **Whether this aircraft can actually perform
the change is a separate question and is not settled anywhere in this paper**: whether the moment
available is sufficient, and whether the aircraft trims through the rotation, depend on
aerodynamics that — for the methods used here and the published comparisons against which they were
checked — are not reliable above roughly ten degrees of incidence, which is inside the band the
rotation passes through. **The mechanism claim is about hardware and survives that limit. The
transition claim is not made.**

The combination carries costs: the attitude rotors that make the union controllable are themselves
exposed in cruise, and Section 7.2 charges them.

### 5.2 What it is made of, and what still moves

Section 5.1 claimed that a class of mechanism is absent. A claim of that kind is only as good as
the inventory behind it, so the inventory is given here in full, including the parts that move.

#### The airframe

The entire airframe is the wing. There is no cylindrical fuselage: every part of the planform
carries payload and produces lift. Leading-edge sweep varies continuously along the span while
the trailing edge is held at 25°, so the realised sweep runs from 45° at the root to 38.3° at the
tip — a variation of under seven degrees, with the crescent character coming from the curvature of
the leading edge rather than from a large change in sweep. Thickness runs from 25 % of chord at
the root to 12 % at the tip, and chord from 0.970 m to 0.236 m. For the 50 kg reference design — the design this inventory describes; Section 7.1 re-closes it at
four masses, and Section 7.3 sets it beside a 1 000 kg reference design — the span is 3.453 m, the wing area 1.979 m², and the aspect ratio 6.03.

Sweep is not a free parameter here, and the reason is structural to the configuration rather than
aerodynamic preference. The aircraft is tailless. With no horizontal stabiliser on a boom, the
pitching moment must come from the distribution of lift along the body itself, and sweep is what
places the outboard sections behind the centre of gravity so they can produce it. **The sweep
angle and the longitudinal stability are one design variable seen from two directions.**

#### The propulsion

**Five propeller stations, ten rotors:** every station is a coaxial counter-rotating pair. The
reason is narrow
and worth stating as such: **reaction torque.** A single propeller applies to the airframe a
torque equal and opposite to the one it applies to the air. It acts about the propeller axis,
which on this aircraft is the body's longitudinal axis — the roll axis in body terms — in both
regimes, and it must be opposed continuously, either by a control surface, which costs drag, or by
differential thrust, which costs a control channel. A counter-rotating pair does not produce it.

One pair sits at the nose, 1.20 m in diameter on the 50 kg reference design, and produces all propulsive
thrust in both regimes. Four smaller pairs, 0.20 m in diameter, sit at the ends of rigid frames
projecting from the wing tips. Every pair is of **fixed geometry**: no cyclic pitch, no
collective, no variable-pitch hub and no mechanism that changes a rotor's orientation relative to
the airframe. Shaft speed is commanded; blade geometry and orientation are not. Each rotor of each
pair is driven by its own
electric machine on a common axis, so **the splitting gearbox and the mechanical governors that
synchronise it are not required**. This work
makes no claim about the shafting: whether the two machines are stacked on the axis or arranged
some other way is an implementation question it does not settle.

The counter-rotating arrangement carries a second consequence that the transition analysis
depends on. **At equal counter-rotating speeds, the net angular momentum of the propulsion system is nominally
zero**: rotating the airframe through ninety degrees therefore produces no gyroscopic moment for the
control system to cancel. If the pairs are speed-trimmed, that cancellation is no longer exact (below). In a tilting architecture that term is present and must be designed for.

#### The energy path

A series hybrid: fuel to engine, engine to generator, generator to electric machines at the
rotors. The engine is not mechanically connected to any rotor. It is an energy source, and that
decoupling is what allows it to be sized by cruise rather than by hover.

**The separation the architecture depends on is that the continuous cruise requirement is several
times smaller than the hover peak, and that the difference is supplied from a battery buffer for
the vertical phase alone.** No wattage is quoted here; the closed powers are Section 7.1's.

#### What produces each moment

**Pitch and yaw come from differential thrust between the tip pairs**, and the two axes do not
have the same moment arm. The frames project ±0.71 m perpendicular to the planform, so a
differential between the upper and lower pairs acts at 0.71 m in pitch, while a differential
between the left and right pairs acts at the semi-span, **1.726 m — 2.43 times the pitch arm.**
The yaw arm is therefore the larger by that factor, which is the reverse of the usual situation
and is a consequence of the layout rather than a design choice. What authority each axis
actually has depends on the available thrust differential and on allocation as well as on the
arm, and is not settled by the ratio alone.

**The same differential-thrust system is what is assigned to rotate the airframe through
transition.** That is a design
assignment, not a demonstrated result (Section 5.1): the moment it produces is a sizing input to Section 7.1,
and whether it suffices and whether the aircraft trims through the rotation are **not settled in this paper**.

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
is why one device serves both regimes. The split is an estimate: the slipstream boundary it rests on
is not derived in this work.

#### What meets the ground

The aircraft rests on five points: the four lower ends of the tip frames, and the aft end of a
keel running along the centreline.

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

#### What moves

The propellers rotate, as propellers do, and their shaft speed is commanded; but none of them
changes its orientation relative to the airframe, or its blade pitch, at any point in the flight.
**Beyond the propellers' rotation, one thing on this aircraft changes its configuration: the
strip.**
It is described as deployable in two halves — one side alone for roll, both together as a speed
brake. The actuator inventory is therefore the propulsion motors plus the strip's actuation.
**How many actuators that is, this study does not fix.** The systems budget carries the
actuation without sizing the mechanism, and naming a number here would be inventing one.

**The tip pairs are the parts that fail the escape condition**, and naming them here is the point of
listing them. The nose pair meets all four parts of Section 2.2. The tip pairs do not: they hold
one orientation, but they are carried through cruise producing moments rather than cruise thrust,
which is the first of Section 2.2's failure modes, and they are exposed while doing it. This is the partial
instantiation Section 2.2 lists as its **fourth** failure mode — meeting the condition where the
aircraft is carried and failing it elsewhere — and the charge it re-opens is the second, carried in
Section 7.2. *(They are sized for moments and used for them in both regimes; they add the take-off
margin (Section 3) but were not sized for weight support. Section 2.2's permitted-cost clause
therefore places them outside the first charge while leaving them in the airstream.)*

## 6. The soundness of the resulting product

### 6.1 What this inventory does not settle

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
in Section 7.2.

The free-wheeling state is physically determinate: the rotor settles where net shaft torque is
zero. **The stopped state is not.** Stopping a rotor requires the stop to be produced by
something — motor holding torque, an electrical brake, a mechanical lock — and a stopped
fixed-pitch blade also has an azimuth, so "stopped" is a family of aerodynamic states rather than
one. Neither the means nor the azimuth is fixed by this study, and the drag figure quoted for the
stopped condition should be read as the state Section 7.2 defines rather than as the state a
particular installation would reach. The free-wheeling state needs no stopping means; the stopped state does, and if it were a
brake or a lock rather than motor holding torque, the count of Section 5.1 would gain a class.

### 6.2 What is not claimed

This section states the boundary of the paper's claims. It is placed before the configuration's
own numbers because a boundary drawn after the results would be a retreat, and one drawn before
them is a commitment.

**It is not a list of the study's open questions.** Those are in Section 8, and the difference
matters: the boundary below is about claims the paper **declines to make**, most of which it
could not make on any evidence; Section 8 is about questions the paper **does not answer**, and
which better evidence would answer. One is a scope; the other is a debt.

#### The claims are made on four axes, against four different opponents

The boundary is easiest to state as a consequence of the claim structure rather than as a list
of denials, so the structure comes first. Comparison is only meaningful against a named
alternative, and this paper's alternatives differ from axis to axis.

| Axis | Opponent | Status |
|---|---|---|
| Cruise efficiency | Rotorcraft: multirotors and helicopters | **Claimed against multirotors, and bounded; against helicopters the published comparison is mixed and no advantage is claimed.** Cruise lift is carried on a surface rather than on rotors, which no sizing contract changes. The *size* of the resulting advantage is a calculation, not a consequence of that fact (Section 4). |
| Operation without a runway | Fixed-wing aircraft | **Claimed as sized, not demonstrated** (Sections 3, 8). |
| The mechanism required to change regime | Tilting architectures | **Claimed.** This is the paper's contribution — a count of mechanism classes (Section 5.1), not a claim of mechanical simplicity or reliability. |
| Cruise efficiency and range | Other hybrids — lift-plus-cruise, tilt | **Not claimed, in either direction.** |

**The fourth row is the important one**, and the reason it is a refusal rather than a result is
the paper's own finding in Section 7.4. Against lift-plus-cruise the ordering depends on the sizing
contract: across the three contracts it moves substantially, and under one of them its sign changes
inside the envelope and turns on quantities of the competitor that are assumed rather than measured. A paper that quoted one of those orderings as a result would be reporting its own choice of
contract. Against the tilting family the competitor can be modelled here only as a bound that pays no
cruise penalty, and an ordering against a bound is not a result. **No
range claim is made against the tilting or lift-plus-cruise families in either direction**, and
a reader who finds one implied anywhere in this paper should treat it as an error rather than
as a claim.

#### What each claim does not depend on

A reader who rejects one of these claims should be able to see immediately which of the others
survive, and the dependencies are short enough to state.

**Operation without a runway** does not depend on the drag bracket, the propeller efficiency or the
transition aerodynamics — **but it does depend on the energy store**: the vertical phase is sized with one,
and Section 8 examines whether it exists. **Cruise lift carried on a surface** does not depend on the sizing
contract or the transition aerodynamics. The **size** of the cruise-efficiency margin depends on both the
drag bracket and the blade family, and Section 4 reports it as a range rather than a number. **Elimination
of the propulsor-reorientation mechanism class** does not depend on the drag bracket, the propeller
efficiency, the sizing contract, the range result or the energy store — **nor on the transition aerodynamics**.

**The last of these carries a distinction that matters more than the others.** The mechanism claim is
a statement about what hardware is present, and it is settled by the inventory of Sections 5.1 and 5.2. **The
separate claim that this aircraft can actually perform the regime change is not settled** (Section 5.1).

#### One cost of the contribution that is named and not priced

The mechanism claim has a price this work does not compute. **This configuration declines the reaction-torque
channel that comparable aircraft use for roll (Section 5.2). What that refusal costs — in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia —
is not computed anywhere in this paper.** The claim is that the mechanism class is eliminated.
**Whether eliminating it is favourable on balance is a question this work does not settle**, and
quantifying it would require a control-allocation study rather than a single torque figure.

#### Eight things this paper does not claim

**1. It does not claim range against fixed-wing aircraft.** A runway-launched aircraft that never
claimed vertical capability pays none of the charges of Section 2.1, and nothing here competes
with it on distance.

**2. It does not claim vertical capability against rotorcraft.** That comparison runs the other
way and would be absurd.

**3. It does not claim that the aircraft has no moving parts.** What is eliminated is a *class
of mechanism* — the one that reorients a propulsor. The aircraft has a moving aerodynamic
surface, it is named where the elimination is claimed rather than later, and it also pitches the
nose down when deployed.

**4. It does not claim mechanical simplicity.** Part count, assembly mass, failure modes and
maintenance burden were not measured, and nothing here supports a statement about reliability.
The count of mechanism classes in Section 5.1 is not a reliability argument, and
readers who convert one into the other are not quoting this paper.

**5. It does not claim that the escape condition is fully instantiated.** The condition is met
in the propulsor that carries the aircraft and is not met in the attitude system, which is
carried through cruise producing moments rather than cruise thrust. Section 2.2 names that case as
partial instantiation, and the charge it re-opens is reported rather than absorbed.

**6. It does not claim that satisfying the condition makes an aircraft better.** The condition
concerns three specific charges. A configuration may avoid all three and still be unbuildable,
uncontrollable, or unsuited to its mission, and the accounting says nothing against that
possibility.

**7. It does not claim that the trades inside the escape are favourable.** Moving the hover
peak onto a store converts a power-system charge into a cost in kilograms; serving two regimes with one
set of fixed-geometry propellers costs efficiency in at least one of them. Both are computed,
neither is asserted to be worth paying, and the ledger reports them whichever way they fall.

**8. It does not claim that the aircraft flies.** The design *sizes* vertical operation and the
transition; it does not demonstrate either. No aircraft has been built, no wind tunnel has been
run on this geometry, and the transition analysis is a calculation whose assumptions are stated
where it appears. **"By construction" throughout this paper means "by the sizing", never "by
demonstration."**

#### What the claims that remain amount to

Removing those eight leaves something narrower than a first reading of the abstract might
suggest, and the narrower statement is the one the paper defends: **a configuration sized to
combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so
with no mechanism that reorients a propulsor, and an account of what the combination costs.**

Each half of that has a named opponent and neither half is a record. **Nor is the configuration
claimed to be without precedent**: Section 1 sets out what is already established, including
uncrewed tail-sitters, tail-sitters without control surfaces, coaxial contra-rotating
tail-sitter propulsion, and blended-wing-body tail-sitters. **The contribution is the
architecture, and the paper presents it as the combination, the consequences of the choices inside
it, and the accounting** — which is what Sections 5.1 and 5.2 describe and what Section 7.2 prices.

#### One consequence for how the numbers that follow should be read

Because the comparative result depends on the sizing contract, **no comparison in this paper
should be quoted without the contract it was computed under.** That is not a caveat attached for
safety; it is the paper's own finding applied to the paper's own numbers, and Section 7.4 states
what it demands of anyone who uses the framework afterwards.

## 7. The calculations

### 7.1 Analytical closure of the sizing loop

This section prices the arrangement of Sections 5.1 and 5.2 on a declared package; it does not bear on the count of mechanism classes, which rests on the inventory of those sections alone. **Closing a sizing loop mathematically is not the same thing as closing an aircraft physically.** This section does the first: what it produces is a set of consistent numbers on a declared set of assumptions.

Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Supplement S10). **If no fixed point exists, the declared sizing package does not close.**

#### The inputs, and why there are four closures rather than one

**The zero-lift drag coefficient is uncertainty:** a consistent build-up places it between 0.0285 and 0.0381 (Section 7.2), and a designer does not choose where the real aircraft falls in that range. **The blade family is a design variable this study has not fixed:** four nose-blade families that meet the hover figure of merit span cruise propeller efficiencies of 0.632 to 0.683, and the study carries all four rather than pretending to have chosen. **The published zero-lift value of 0.0248 is not used**; the consistent build-up places it below both ends of the bracket, outside the supported range.

The loop holds wing loading, disc loading and aspect ratio fixed, so **the cruise lift coefficient is unchanged at 0.450 in every closure** (geometry in Supplement S10); the claim is that C_L is unchanged, not that C_D0 is exactly so. The tip frames, the tip discs and the strip are not sizing variables; they were set on the 50 kg reference design of Section 5.2, and **the control moment arms of Section 5.2 are therefore reference values that this closure does not re-derive.** **These are the same configuration at four closed masses rather than four configurations** — but anything that depends on the arms is carried at the reference geometry and is not an output of the loop.

Run on the published drag coefficient without the rotor term and the published propeller efficiency, the same construction reproduces the published aircraft within 1.5 percent (Supplement S10). That check is the only place in this section where the published value appears, so the closures report a change of inputs, not of method.

#### The four closures

**On these assumptions all four converge**, for the 50 kg design — the only one carried through this loop.

| | C_D0 | η_p | L/D | L/De | MTOW | Empty fraction | Hover power, rotor shaft | Engine rating, shaft | Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** | 0.0381 | 0.632 | 8.79 | 5.56 | 57.5 kg | 0.614 | 12.53 kW | 5.17 kW | 927 km |
| **B** | 0.0381 | 0.683 | 8.79 | 6.00 | 55.8 kg | 0.607 | 12.17 kW | 4.65 kW | 1 002 km |
| **C** | 0.0285 | 0.632 | 10.82 | 6.84 | 53.5 kg | 0.597 | 11.66 kW | 3.91 kW | 1 141 km |
| **D** | 0.0285 | 0.683 | 10.82 | 7.39 | 52.3 kg | 0.592 | 11.40 kW | 3.54 kW | 1 233 km |

*L/De = L/D × η_p at the cruise condition; the loop holds both factors fixed within each closure, so the closure changes
neither. The four L/De values are the bounding corners of that product, carried into the closures as inputs, not four
simulated aircraft.*

**Payload is an input, fixed at 13 kg; take-off mass is the output**, and the payload fraction runs from 0.25 down to 0.23. **The blade that is best before the loop is still best after it.** There was no reason to assume so: propeller efficiency propagates through cruise power into engine size, engine size into mass, and mass back into hover power, and a loop can reverse a local ranking. At both ends of the drag bracket the higher-efficiency family closes to the longer range — **a result of the closure rather than an assumption carried into it.**

#### The transition

The sizing above says nothing about whether the aircraft can change regime. **The question is asked in two models, only the second of which carries rotational dynamics, and that one does not support a zero altitude loss.** Every transition figure here belongs to a reference design at its published mass and is not an output of the closure. In the first, a point-mass model with the body angle driven kinematically, a rotation entered in a 5 m s⁻¹ climb loses no altitude at either reference rotation time: 2 s for the 50 kg design and 5.1 s for the 1 000 kg one. Solved instead with rotational dynamics and a finite control moment, **and with the aerodynamic pitching moment set to exactly zero, so that nothing favourable is borrowed**, the 50 kg design **loses 5.4 m at the same reference condition.** The loss is not an artefact of the controller: it is unchanged across three reference profiles, appears without the control moment saturating, and grows as the gains are raised (Supplement S10). **What the kinematic model leaves out is not the difficulty of turning the aircraft but the trajectory the aircraft flies while it is being turned.** **So the zero-altitude-loss result is a property of the model that produced it.**

What replaces it is not a prediction: the pitching moment that would make it one exists, but for the methods used here the predictions diverge above roughly ten degrees of incidence, the band the rotation passes through (Section 8). With a borrowed moment the spread is wide enough that no number from it is reportable: some models complete the rotation, some saturate the tip pairs, and some tumble. **That spread is itself the finding.** **Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude.** Whether a real aircraft loses 5.4 m, more, or less is not settled by anything here.

#### What closing does and does not establish

It establishes that the architecture is arithmetically self-consistent on a declared package, at four corners of that package. **It does not establish that the package exists.** The energy store this closure assumes is the item Section 8 examines, and the examination does not end well. These ranges are carried forward as closed-loop values, not as a ranking: no rotorcraft is sized in this work, so no range comparison is made against one (Section 4 compares cruise efficiency), and the comparison with the other hybrids depends on the sizing contract (Section 7.4).

### 7.2 The ledger

Section 2.1 named three charges that any architecture in this corner pays; **this section says where each charge appears inside the closed numbers of Section 7.1, and how large it is there.** Like the closure, the ledger prices the arrangement; the count of mechanism classes is not an entry in it.

**It attributes. It does not add.** Every cost named below is already inside the closure of Section 7.1. **No new physical cost term is introduced here.** **And there is no single figure for what the architecture costs.** The three charges are in three different currencies — kilograms, drag counts, installed kilowatts — and **no scalar aggregate is defined, because this study has no defensible weighting between them.** **The total is the contract, not a property of the aircraft** (Section 7.4).

#### Bill 2 — the drag of hover hardware, inside the bracket

In the zero-lift drag build-up behind Section 7.1's bracket (line items in Supplement S11), **the hardware exposed by the vertical-phase layout — the tip frames and the free-wheeling attitude rotors — is 69 percent of the zero-lift drag at the favourable end and 57 percent at the adverse one**; the rotor term alone is 0.0154 at the favourable end. **The rotor line rests on section drag at low Reynolds number.** It is a blade-element result for sections near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section polars that are computed rather than measured; Section 7.3 shows how strongly the term depends on it. **The tip-frame term is an attribution, not a marginal removal cost**: it is not a claim that this drag would disappear if the vertical phase did.

Removing the hub and small items, the tip frames and the free-wheeling rotors gives a clean-body lift-to-drag ratio of 20.55 at the favourable end and 15.24 at the adverse one, against the aircraft's 10.82 and 8.79: **the configuration retains 52.6 and 57.7 percent.** Bill 2 therefore occupies a larger share where the clean-body drag is lower, because a near-constant charge is set against a smaller total — a statement about position within the drag bracket at one scale, not about size (Section 7.3).

**Rotor–structure and rotor–wing interference is not modelled and is not carried as a line.** Section 2.1's wind-tunnel source found that a simulation assuming negligible rotor–structure interaction predicts lower drag than was experimentally observed; this build-up is such a calculation, and the bracket's upper margin is the only provision made for it.

#### The cruise-efficiency gap under fixed pitch

Section 7.1's closures run at a cruise propeller efficiency of 0.632 to 0.683: **relative to the 0.80 the published chain assumed, 14.6 percent lower at the better blade and 21.0 percent lower at the worse.** **The ledger does not attribute the whole of that gap to the absence of variable pitch.** **No variable-pitch counterfactual was computed.** Nor is the gap decomposed.

#### Bill 1 — carried mass, and what it is on this configuration

**There is no dedicated lift group to charge.** What Bill 1 becomes here is the energy buffer: **3.6 percent of take-off mass, 1.9 to 2.1 kg across the four closures.** The buffer is not lift-subsystem mass, so it is not Bill 1 as Section 2.1 defines it, but it is carried for the whole flight to serve a demand that lasts about two percent of it: **the architecture converts a power-system charge into a cost in kilograms**, as Section 2.2 said in advance it would.

**The buffer fraction is an input to the loop, not a result of it.** The deficit per kilogram of take-off mass that the buffer covers, taken at the electrical bus, spreads by 12 percent across the four closures while the fraction is held at 3.6 percent (Supplement S11). **The corner that needs the most buffer per kilogram is given the smallest buffer**, and that is a declared assumption of the closure rather than an outcome of it.

#### Bill 3 — released from the engine, and not from the electrical path

The engine is sized by cruise, **3.54 to 5.17 kW** of shaft rating, against a hover requirement of **11.4 to 12.5 kW** at the rotor shaft: a ratio of installed hardware of **2.4 to 3.2**, which is not the buffer's burden (Section 8 computes that). **But the full hover power passes through the electrical path, and that path is sized by it.** **Bill 3 is removed from the engine and left standing on the electrical system** (the propulsion-mass split is in Supplement S11).

#### What the closure does not contain

Section 7.1's convergence does not cover the cost of declining the reaction-torque channel, the sizing of the strip's actuation, the allocation of the take-off margin against attitude authority, the landing transition, the vortex ring state, closed-loop hover control, engine installation, or rotor–structure and rotor–wing interference; **none of these is a ledger entry, and Section 8 lists them.** **The first and the last are the two that would most change the numbers above if they were computed.**

**Every one of the charges above belongs to one scale**: the four closures do not establish how the three charges behave as the aircraft changes size, which Section 7.3 asks, or what happens to the comparison when the sizing contract changes, which Section 7.4 asks.

### 7.3 Scale does not lock two of the charges together; the third is not tested

Section 7.2 decomposed the three charges on one aircraft, at one size; **this section asks whether they are three quantities or one quantity under three names**, by changing the size of the aircraft and seeing whether they move together. Either answer leaves the mechanism claim where it was; that claim rests on the inventory of Sections 5.1 and 5.2. **The test is deliberately weak**, and it is stated at its own strength. It can show that two charges are not locked together within this model. **It cannot show that they are independent in general**, and it is not offered as doing so.

**The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 7.1's closures**: no closure was run at 1 000 kg, the heavy design has no drag bracket and no structural closure, and no heavy-design range is quoted.

#### Bill 3 — held nearly flat by a sizing rule, which is not a finding about Bill 3

Disc loading is held at approximately the same value, 44.2 kg m⁻² at 50 kg and 43.7 at 1 000 kg, so specific hover power is held with it: 0.218 kW kg⁻¹ at the light design and 0.216 at the heavy. **That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3.**

Section 7.2's measure of Bill 3, rotor-shaft hover power over engine shaft rating, is 4.19 at the light design and 3.98 at the heavy, and with the engine margins the two designs use it **moves by between 5 and 14 percent across the factor of twenty, depending on an engine margin the sizing rule does not set** (Supplement S12). *(Section 7.2's 2.4 to 3.2 is the same ratio at the four closures. This paragraph compares the reference pair only.)*

The rule has a price, paid in geometry: the ratio of propeller diameter to span rises from 0.35 to 0.47, and **much above 1 000 kg a single nose pair can no longer hold the disc loading**, so a second would have to be added.

#### Bill 2 — the rotor term falls, and in this model Reynolds number accounts for it

**Only the rotor term of Bill 2 is computed at both sizes**; the frame term enters both designs as the same multiplier, so it cannot show a scale effect in either direction. At 50 kg the rotor term is **0.0154**; at 1 000 kg the blade designed to the same section lift coefficient gives **0.0068**, and the blades swept give 0.0045 to 0.0100 — a direction that is the ordinary one and a factor that is not a measurement. **Within the blade-element and section-polar model, the section Reynolds number accounts for the fall**, rising from about 8 × 10⁴ to 5.6 × 10⁵; three other candidates are excluded (Supplement S12), and this is a decomposition inside the model rather than a causal claim beyond it.

The fall rests on section drag taken from polars rather than measured, and the light end lies below a Reynolds number of 10⁵, where section drag is hardest to predict. **Of the two rotor terms, the light one is therefore the less certain — and it is the one Sections 7.1 and 7.2 carry.**

#### Bill 1 — not tested, and the one available derivation would not test it

On this configuration Bill 1 appears as the energy buffer: 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and **both of those figures are inputs.** **A change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction.** A buffer sized to the hover deficit at the same specific power would track hover power and engine rating, which are the Bill 3 measures, so that derivation cannot test whether Bill 1 separates. **Whether the two are separable here is not established**; what is established is that they are coupled here, which is Section 2.2's claim rather than a defect found in it. **Coupling is not identity**: the buffer is measured in kilograms and the engine in kilowatts, linked by a specific power that is itself an assumption.

#### What the comparison establishes

**Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its light-design value in the section polars used here, while specific hover power changes by one percent and the Bill 3 ratio by 5 to 14 percent.** The flatness of Bill 3 is imposed by a sizing rule; the finding is that Bill 2 moved anyway, by more than the Bill 3 ratio at every point in the heavy interval and under either engine margin. **Within this model, the two are therefore not one quantity under two names.**

**Bill 1 is not tested**, and nothing here should be read as showing that it separates from the other two — or as showing that it does not. **The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low Reynolds number.** It is consistent with the separability Section 2.1 asserts; it is not a verification of separability as a general property, which a single instantiation cannot supply.

#### Two costs that scale does not relieve

The fixed-pitch gap also widens slightly with size, to 16.4 to 22.9 percent at the heavy design (Supplement S12); as in Section 7.2, no variable-pitch counterfactual was computed. **The transition is where the square–cube relation is paid in full**: rotating the heavy design in the light design's two seconds would demand about 220 kW from the tip propellers, roughly the whole of hover power; at its own 5.1 seconds the demand is about 13 kW. **A larger aircraft of this type turns more slowly, and must.**

#### Why this section sits between the ledger and the contracts

**Because at least two of the charges are not locked together, a comparison of architectures cannot in general be reduced to a number that does not depend on how the charges are weighed.** The argument requires only two charges that are not locked together; the third need not be shown separate for the conclusion to hold. Section 7.4 examines what the choice of sizing contract does to a ranking, on the light closures of Section 7.1 only.

### 7.4 Rankings belong to contracts

Section 7.3 showed that at least two of the charges are not locked together; where one architecture pays less of one charge and more of another, the ranking depends on how the charges are weighed, and **a sizing contract is one such weighing**: it fixes what is held equal between the architectures being compared. This section applies three contracts to three architectures at each of the four closures of Section 7.1. **The mechanism claim is not a ranking and is not at stake here.**

#### Three contracts, and what each holds equal

Range in the sizing loop is proportional to L/D, to the energy chain, propeller included, and to the fuel fraction, and the three contracts differ only in the last (Supplement S13): a **fixed fuel fraction**, sixteen percent of each architecture's own take-off mass, under which take-off mass cancels from range; a **fixed fuel mass**, the 8.4 to 9.2 kg this configuration carries, under which range is divided by take-off mass; and a **fixed take-off mass and payload**, under which every kilogram of architecture-specific hardware is a kilogram of fuel not carried. **These are three different questions, not three estimates of one answer.** A mission decides which of them it is asking; this paper has no mission that would decide, and does not choose.

#### What is compared, and on what basis

Three architectures fly the same mission, 13 kg of payload at 30 m s⁻¹, with the same wing loading, disc loading and aspect ratio, the same airframe and avionics fractions, and the same fuel and energy chain apart from the propeller. **The competitors are therefore this planform with two add-ons, not independently designed aircraft of their families.** All three carry the same buffered series-hybrid power system, so Bill 3 is held common and the comparison measures mass and cruise drag. **Holding Bill 3 common is a choice of question, and it has a direction.** **The choice runs against this configuration.** Without the buffer, and with engines rated to deliver the hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off mass and falls 38 to 47 percent behind under a fixed fuel mass, and the tilt bound does not close under a fixed take-off mass; under a fixed fuel fraction it closes at 520 kg, about ten times this configuration's mass — the first contract's blindness to mass, made visible. That comparison is not used, because it would set competitors without a store against this configuration with one.

The basis is not symmetric: the lift-plus-cruise layout carries a lift-to-drag ratio transferred from a different airframe's wind-tunnel campaign (Section 2.1) and assumes lift rotors stopped and aligned in cruise, which takes an indexing mechanism (Section 5.1) whose mass is not separately charged. **The tilting layout carries no cruise drag penalty at all. That is an idealisation in its favour**, and it is deliberate: it makes the tilting layout a bound. Both competitors use a propeller efficiency of 0.80, assumed, not computed, against this configuration's computed 0.632 and 0.683; the lift-plus-cruise layout carries a lift group of 10 percent of take-off mass and the tilting layout a tilt mechanism of 5 percent. **Neither figure is measured.**

#### Against lift-plus-cruise: a trade, and the contract sets the exchange rate

**The two architectures trade one charge against another**: closed under a fixed fuel fraction, this configuration is 27 to 30 percent lighter, and the lift-plus-cruise layout cruises at a lift-to-drag ratio of 11.66 and 15.72 against 8.79 and 10.82, with a propeller at 0.80.

Range of the lift-plus-cruise layout relative to this configuration:

| Closure (Section 7.1) | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass |
|---|---:|---:|---:|
| A | +67.8 % | +40.2 % | +1.1 % |
| B | +55.3 % | +27.5 % | **−13.0 %** |
| C | +83.9 % | +53.5 % | +7.3 % |
| D | +70.2 % | +40.1 % | **−6.5 %** |

**The lift-plus-cruise layout is 55 to 84 percent ahead under the first contract, 28 to 54 percent under the second, and between 13 percent short and 7 percent ahead under the third; the shift from first to third is 67 to 77 percentage points at every closure**, at the declared lift-group fraction, and always toward the lighter aircraft. **The sign itself changes inside the envelope under the third contract**: this configuration is ahead at the two closures with the higher-efficiency blade family and behind at the two with the lower. **A statement of which architecture has the longer range, made without its contract, would therefore be a statement about the contract.**

#### Against the tilting layout: a bound, not a ranking

**What the bound gives is a size, not an order.** Credited with no cruise penalty, the tilting layout is 93 to 141 percent ahead of this configuration under every contract at every closure; that margin is the room a real tilting aircraft's cruise penalties — nacelle drag, pivot fairing, hover-sized rotors flown as cruise propellers — would have to fill, and how much of it they fill is not computed. **A ranking against a competitor modelled as a bound is not a ranking, and no range claim is made against the tilting family in either direction.**

#### Section 2.1's prediction, tested

Section 2.1 predicted that such a ranking will move when the sizing rule changes, and can reverse. **The movement holds everywhere**, against both competitors, toward the lighter arrangement as the contract weights mass more; **the reversal holds at two of the four closures against lift-plus-cruise, and at none against the tilt bound.**

**Where the reversal falls is decided by quantities this study has not measured or not fixed**: the blade family in the base case, and across the sensitivity cases the competitor's lift-group mass and the propeller basis (Supplement S13). With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every closure; with a heavier one this configuration leads under a fixed take-off mass at every closure; with a common propeller efficiency a reversal appears at every closure. **Which architecture ranks first under a fixed take-off mass is therefore decided, in this model, by quantities this study assumes for the competitor rather than measures: its lift-group mass fraction and its propeller efficiency.** **Put plainly, the sign under a fixed take-off mass is not a result about the architectures; it is a result about those quantities.** What is robust is that the shift exists and runs toward the lighter aircraft; its size is the size of the mass difference.

#### What the framework asks of whoever uses it

**Each comparison states every charge in its own currency before any aggregate, names its contract, and states its asymmetries and their directions; an ordering is reported only with the contract it was computed under and, where its sign depends on an unmeasured quantity, with that quantity named.** This paper meets that for its own column (Section 7.2) and not for the competitors', whose kilograms and drag counts here are parameters and transferred ratios rather than an audit.

#### What this section does not establish

**The competitors are modelled at a coarser level than this configuration**: their drag is transferred or idealised, their propeller efficiency assumed and their architecture-specific mass a parameter. **Comparing computed figures against assumed ones favours whichever is assumed more optimistically** — in propeller efficiency both competitors, and with a common propeller efficiency the lift-plus-cruise lead under the first contract falls from 55–84 to 33–45 percent (Supplement S13); in drag the tilting layout, by construction. **The comparison is at one size**: Section 7.3's 1 000 kg reference design has no closure, and none of its figures is used here. **And nothing here ranks architectures for a mission.** What this section establishes is narrower: **the same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property of the architectures alone.

## 8. What does not close

Section 7.1 closed the sizing loop on a declared package and said that whether an aircraft can be built to it is a different question. **This section is where that question is answered, and for the first item the answer is no.** Section 6 called this section a debt: questions the paper does not answer and that better evidence would. It is stated in that order — first the obstacle that is known, then what is not known.

### First, the known obstacle: the energy store

**Every closure in Section 7.1 carries a buffer of 3.6 percent of take-off mass**, an input rather than a result (Sections 7.2 and 7.3). Taken at the electrical bus, where the buffer sits, **the four closures ask the buffer for 4.7 to 5.2 kW per kilogram of buffer to hover, and 5.5 to 6.1 kW per kilogram of buffer to leave the ground** with the tip pairs at full thrust (Section 3).

**What has been measured is a fraction of that, and the figures available are of four different kinds.** A 24-series nickel–cobalt–manganese pack designed, bench-tested and flown in a 210 kg-class electric VTOL aircraft is rated, as a flown system, at 0.892 kW per kilogram continuous; its unit pack, discharged on the bench at its highest tested rate, delivered on average about 1.5 kW per kilogram (Supplement S14). A NASA-funded design study adopts 4 kW per kilogram and describes that figure as about twice that of existing batteries. The same study notes lithium-polymer figures in the literature as high as 3 kW per kilogram, which it cites rather than measures; against that figure the take-off demand is 1.8 to 2.0 times. The study argues that, because pulse current limits can exceed continuous ones — by more than a factor of two in one commercial module it cites — a pack with the required specific power may be possible with existing technology; the study's hover lasts twenty seconds or less; this aircraft's vertical phases occupy about a minute in all (Section 2.1), and how long each draws the peak is not computed here.

**The take-off demand of Section 7.1's closures is 3.7 to 4.1 times the bench rate — the highest figure obtained from a measurement — and 6.2 to 6.8 times the flown system's continuous rating**; hover alone is 3.1 to 3.5 times the bench rate. The comparison is between unlike ratings: a peak demand held through the vertical phases, a bench average over minutes, a continuous rating, a design assumption, and a literature figure the study cites without its rating. **The gap is real on every one of them; the factor quoted is peak demand against bench average.** The package Section 7.1 closes on does not exist with any store the sources consulted here report as built.

**Closing the loop on a measured store is a sensitivity of that package, not a second aircraft**: the buffer is derived inside the loop from the take-off demand at a given specific power, and everything else is Section 7.1's. At the bench rate of about 1.5 kW per kilogram the loop closes at 94.6 to 101.2 kg, 76 to 81 percent heavier, with a buffer of 13.4 to 14.7 percent; at the design study's 4 kW per kilogram it closes 6 to 8 percent heavier (the table is Supplement S14). **These masses are the Section 7.1 package with one input changed. They are not a structural closure at 100 kg**, and whether the airframe fraction holds at twice the mass it was set at is not established. If Section 7.1's take-off masses are retained instead of re-closing at the bench rate, the payload falls to about 7 kg rather than 13; at the flown system's continuous rating the loop only just closes, and at the unit pack's continuous rating it does not close at all.

**This is where the coupling Section 7.3 found is paid**: the buffer is the conversion the escape condition permits — kilowatts of hover peak paid in kilograms of store. **The escape from Bill 3 is real in the sense Section 2.2 defined it, and its price depends on a component whose required performance has not been demonstrated.**

### What the obstacle reaches, and what it does not

**It reaches every number that describes this aircraft at Section 7.1's masses**: the closed masses of 52.3 to 57.5 kg and the 13 kg payload assume the store. The ranges of 927 to 1 233 km survive the re-closure only because the fuel fraction is held, on an aircraft three-quarters heavier; they do not survive as 13 kg carried that far on a store that has been built. The vertical phase that Section 3 reports as sized was sized with this store in it, and Section 7.4's orderings were computed with the store held common at 3.6 percent; how they would move with a measured store is not computed.

**It does not reach the mechanism claim.** That is a statement about hardware, and a heavier store adds no pivot. **Nor does it reach the cruise-efficiency comparison of Section 4 as a ratio**: effective lift-to-drag ratio has no mass in it. As a comparison of aircraft, that section describes the configuration at Section 7.1's masses, which the store does reach.

### Then what is not known

The remaining items are not known obstacles; they are questions this work has not answered, and each is listed with what would settle it in Supplement S14. They are:
- the pitching moment through the transition;
- section drag at low Reynolds number;
- the tip pairs' stopped cruise state;
- the buffer's energy, not only its power;
- the electrical path at peak;
- the airframe's mass;
- the strip and the fairing;
- closed-loop hover control, including the declined reaction-torque channel, the hover torque residual and the allocation of the tip pairs between take-off margin and attitude authority;
- vertical descent and the landing transition;
- ground handling and landing loads;
- the competitor's lift-group mass;
- the competitor's cruise propeller efficiency;
- rotor–structure and rotor–wing interference;
- engine installation;
- blade-family selection;
- atmosphere.

**None of these is a small correction to a known quantity.** Two of them need validated data rather than more of the computation already done: the transition moment, because three methods have been tried against it and disagree, and the low-Reynolds section drag, because the one method used here is least reliable exactly there.

### What this section amounts to

**The loop closes; the aircraft is not shown to.** At the energy store the paper can name the gap exactly, in specific power and in take-off mass; everywhere else it can name only what would settle the question. **The architecture claim — that the configuration is arranged to change regime with no mechanism that reorients a propulsor — is a count of hardware, and nothing in this section reaches it.** What this section reaches is the aircraft, and the paper has not claimed the aircraft. The last section returns to the four axes of Section 6 and states what is claimed on each.

## 9. Four axes, and where the paper stops

The paper makes its claims on four axes, against four opponents (Section 6), and on each it stops where
its evidence stops.

**Cruise efficiency, against rotorcraft — claimed against multirotors, and bounded; mixed against helicopters.** Cruise lift is carried on a surface
rather than on rotors. The size of the advantage is a calculation, not a consequence of that statement:
positive throughout against one published quadrotor, and from slightly behind to comfortably ahead against
the other (Section 4). Nothing is claimed against rotorcraft on vertical capability.

**Operation without a runway, against fixed-wing aircraft — claimed as sized, not demonstrated.** The
vertical phase was sized with an energy store whose required performance the sources consulted here do not
report as built (Section 8). Nothing is claimed against fixed-wing aircraft on range or cruise efficiency.

**The mechanism required to change regime, against tilting architectures — the contribution.** The
configuration is arranged to change regime by rotating the airframe rather than the propulsors, and so
carries none of the mechanism classes Section 5.1 counts: no pivot, no nacelle or rotor-group actuator, no
variable-pitch hub, no dedicated lift rotors, and — while the tip pairs free-wheel or are held by motor torque — no
rotor stowing, indexing or stopping mechanism (Section 5.1's note). Roll
comes from the strip; the reaction-torque channel the coaxial pairs could provide is declined, and what
declining it costs is not computed. **This is a count of mechanism classes, not a claim that nothing moves, and not a
claim of mechanical simplicity or reliability.** Whether this aircraft completes the rotation is a separate
question, and it is not settled here.

**Range, against the other hybrids — not claimed, in either direction.** The ordering belongs to the sizing
contract (Section 7.4).

**The loop closes; the aircraft is not shown to.** Section 8 lists what would settle the rest; nothing in
this work addresses certification. What the paper offers is **a configuration sized to combine
runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism
that reorients a propulsor, and an account of what the combination costs.**
