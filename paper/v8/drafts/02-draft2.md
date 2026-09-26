## The tax

**A claim that one architecture escapes a cost shared by the others is only meaningful if the cost is stated first, in terms that do not presume the escape.** This section states it. It is not a claim about any particular aircraft, and nothing in it is new physics; what it provides is the accounting that the rest of the paper is checked against.

### The root: a duty cycle that does not match the hardware

For a mission of one hour, a take-off, a transition, a return transition and a landing occupy on the order of a minute — **roughly two percent of the flight.** **An architecture that provides the vertical phase with a dedicated lift subsystem therefore carries it for fifty times as long as it uses it.** This is not an implementation defect and it cannot be removed by making the subsystem better, because it is a statement about duty cycle rather than about quality. **The mismatch between how long a component is needed and how long it is present is the origin of all three charges below.**

The statement is deliberately confined to architectures with a dedicated lift subsystem, because that is the family the charges describe. Whether any architecture avoids the mismatch — and what it pays instead — is the subject of the next section, and it is not settled here.

### Bill 1 — mass

A lift-plus-cruise aircraft carries two propulsion groups: rotors, motors, mounts, wiring and structural reinforcement for the vertical phase, and a separate propulsor for cruise. The vertical group provides no required lift or thrust during cruise and is lifted anyway.

Its cost is not linear. Mass growth feeds itself — MTOW = m_payload / (1 − f_empty − f_energy) puts additional empty mass through a multiplier that grows as the denominator shrinks — and in the vertical phase the same increment is counted a second time, because at a fixed disc area hover power scales with W^1.5. *(The exponent is a property of the scaling rule chosen: holding disc loading constant instead makes hover power grow linearly with weight, and Section 12 uses that.)* A modest dead-mass fraction becomes a large payload penalty.

**This charge has been identified independently, and by a source with no interest in the present argument.** A NASA study sizing five VTOL architecture families against a common mission with common tools found the lift-plus-cruise concepts the heaviest of the vehicles examined, and named the cause: not the cruise power draw, since the lift-plus-cruise effective lift-to-drag ratio is the higher of the set, but *"the extra empty weight items on board in hover."* That is Bill 1 stated by an independent source in its own terms: not a failure of engineering, but the cost of an architecture.

A second NASA review gives the structural half as a general principle: to transmit power safely to the extremities of the planform, *"very strong (and fatigue-resistant) structures must be incorporated with an obvious weight penalty."* Distributing lift or thrust across the span therefore obliges the structure that reaches it to keep transmitting power there — charged to mass, whether or not the distributed propulsors are running.

### Bill 2 — drag

The second payment falls on architectures that leave hover hardware exposed in forward flight: rotors stopped in the airstream, the booms that carry them, and the interference between their wakes and the wing. Cruise drag has other sources on any aircraft; what is charged here is the part attributable to hardware retained for a phase that is over.

Wind-tunnel work on a hybrid airframe found that the difference between propellers parallel to the airflow and no propellers at all is modest, while *"the drag produced by the motors is significant."* The bill is charged mainly by the motors and the beams that carry them — hardware that cannot be feathered, folded or aligned away, **because its cost is its presence.** ⟦Wind-tunnel⟧ characterisation of a quadplane found drag in the hybrid regime exceeding either pure mode through adverse flow interaction, and that a simulation assuming negligible rotor–structure interaction *"always predicts higher lift and lower drag than were experimentally observed."*

**The important property of this charge is not its size but where it falls.** It is charged per unit time in cruise — so it grows with exactly the quantity the aircraft exists to maximise.

### Bill 3 — power system sizing

A VTOL aircraft must install enough power to hover, but it draws that power only during the two percent of the flight in which it hovers. The ratio between the two demands follows from the governing equations rather than from any design choice⟦ (Supplement S2)⟧:

    P_hover / P_cruise = √(DL / 2ρ) · (L/D) / V · (η_p / η_h)

**The quantities on the right come from the configuration and from the propulsion operating points, not from the duration of the hover phase.** η_h and η_p are not configuration constants, they depend on the propeller and on the condition it is run at, and Section 11 computes what happens when one fixed-pitch blade has to supply both. Raising the disc loading raises the ratio as its square root.

The power system is therefore sized by a condition that holds for a minute and is then carried, unused, for an hour. Sizing by hover means an oversized engine, or a battery that must deliver a peak it will rarely be asked for, or both — and whichever is chosen, the extra installed capacity is mass: a cost in kilograms, though not Bill 1.

### The charges are coupled: remedies move cost, among the three charges or outside them

The three charges are not independent problems with independent fixes. **Each known partial remedy reduces one charge and pays for it, in another charge or in a cost outside the three.** They are three distinct accounting quantities, paid in kilograms, drag counts and installed kilowatts, and they are not assumed to be independent physical causes: a remedy can move a requirement from one currency into another. Whether a change of size moves them together, which would make them one quantity under three names, is tested in Section 12.

**A charge and its currency are not the same thing.** The mismatch of the root is the origin of all three charges; each charge is one specific payment, not the name of the currency it is paid in. Bill 1, as this accounting uses it, is the mass of a dedicated lift subsystem; Bill 2, the cruise drag of hover hardware left exposed; Bill 3, continuous power installed to a hover peak. A remedy's own cost can fall in kilograms, drag counts or installed kilowatts without being one of the three charges, and the table names such a cost in words rather than by a bill's number.

| Move | Bill it attacks | What it creates — a bill by its number, any other cost in words |
|---|---|---|
| Distributed electric lift rotors | 3 — the cruise engine no longer sizes to hover | 1 and 2 — many rotors and mounts, permanently carried and exposed |
| Folding or retracting lift rotors | 2 — the exposed rotor is removed from cruise | 1 — mechanism, actuation, locking; and a new failure mode, not among the three |
| Tilt-rotor, tilt-wing, tilt-nacelle | 1 — one propulsion group serves both regimes | kilograms, not Bill 1 — the pivot and its actuators; **Bill 3**, imposed or left standing according to how the architecture the move modifies supplies its hover peak — with no store, the power plant is sized by the hover peak; and gyroscopic coupling and a transition control problem, which are **not among the three** |
| Variable-pitch or feathering propulsors | 1 and 3 — one propulsor is retrimmed across two widely separated operating points instead of duplicated | kilograms, not Bill 1 — pitch hub and actuation; and a new failure mode, not among the three |
| Higher disc loading, smaller rotors | 1 and 2 — smaller, lighter, cleaner rotors | 3 — hover power rises with √(DL) |
| Lower disc loading, larger rotors | 3 — hover power falls | 1 and 2 — larger structure and exposed area |

**One row pays part of its cost in none of the three currencies, and that is not an oversight.** What a tilting architecture buys its unified propulsion group with is a mechanism — a pivot, an actuator, the gyroscopic coupling of a reorienting mass, and a control problem through the turn. The pivot and the actuator are paid in kilograms, although they are not lift-subsystem mass; the coupling and the control problem are paid in none of the three. That part is a cost, but it is not one of the three charges this accounting tracks. **The table is not a census of the field**; it lists the moves whose transfers are documented, and a remedy absent from it is not thereby claimed to cancel a charge.

**One of these transfers has direct experimental support.** In the doctoral study whose wind-tunnel campaign is quoted above — and in that document rather than in the journal article by the same author, which reports a different comparison — a retraction system removed thirty percent of the airframe's drag; applied to a passenger eVTOL, with the mechanism assessed at five percent of vehicle mass, maximum range rose from 119 km to 121 km — **a two-kilometre gain for a five-percent mass penalty.** The same work finds the retraction's advantage elsewhere — the speed that maximises range rose by 5 m/s — which is a performance this accounting does not price. Bill 2 was converted almost exactly into Bill 1, and **the transfer is the point rather than the small residue.**

### What this accounting is for

**The accounting is refuted by a counter-example, and the table above is where one would appear:** every entry in it moves cost rather than removing it.

**Stated positively, so that the test can actually be run: a counter-example is a remedy that reduces one of the three charges, leaves the other two no worse, and whose own cost is either absent or demonstrably smaller than the reduction — measured in the same currency.** **The accounting claims transfer. It does not claim that every architecture is equally good**, and a remedy that is simply a better bargain in one currency refutes it.

**Two clarifications keep the test from being either too easy or unfalsifiable.** **"No worse" is judged against the architecture the move modifies.** A charge that architecture already paid, left no larger, is no worse. A charge it did not pay, imposed by the move, is worse; so is one it paid, enlarged by it. A move that reduces one charge and makes another worse is a transfer between charges. And a remedy whose cost falls **outside** the three charges does not refute the accounting, because the accounting is about those three; **but it is not thereby exempt from being counted.** **A framework that could absorb any cost by declaring it out-of-scope would be unfalsifiable**, so the costs outside the three are listed, not waved away.

**The tilting row needs both clarifications.** If the architecture it modifies supplies its hover peak from a store, tilting without one imposes Bill 3 and the row is a transfer between charges. If that architecture already sizes its continuous plant by the hover peak, tilting leaves Bill 3 no worse; then, where the mechanism's kilograms are fewer than those of the lift group it removes, what keeps the row from refuting the accounting is the part of its cost that falls outside the three — which is why that part is listed.

It also makes a prediction that can be checked without settling the architectural question at all: **where an arrangement pays one charge heavily in order to escape another, its ranking against a differently-balanced arrangement will move when the sizing rule changes — toward the lighter arrangement as the rule weights mass more — and will reverse where that reweighting carries it past the point at which the two break even, where the mass difference as the contract counts it and the cruise-efficiency difference cancel in the range.** Section 13 tests both the movement and the reversal on this configuration, and Section 4 tests a different consequence against a sizing study this work did not produce.

**The moves in the table are partial remedies: each accepts the duty-cycle mismatch and then redistributes what it costs.** Whether an architecture can decline the mismatch itself, rather than redistribute its consequences, is a different question, and the next section states the condition it would have to meet — a definition, derived from the table above rather than from any aircraft.
