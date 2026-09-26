# v8 — Supplement (ek belge)

Gövdeden taşınan malzeme, **aynen**. Taşıma kararı: Tur 61, dört okuyucu ve Claude hemfikir (`paper/v8-shortening-consensus.md`).
Dergi kuralı: ek yalnız destekler; gövde tek başına yetmek zorunda — bu yüzden her taşınan nesnenin bulgusu ve sınırı gövdede kaldı.

---

## S1. The 1954 programmes and the reviews of them (from Section 1)

#### The third route is established, and its history is not what it is usually taken to be

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

#### What the history does not excuse

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

### Five paragraphs of Section 1 as they stood before recomposition (frozen snapshot)

Tail-sitting prototypes flew in the 1950s, vectored-thrust and tilt-wing aircraft in the 1960s,
tilt-rotors from the 1980s, and a broad family of hybrid vertical take-off and landing uncrewed
aircraft since roughly 2010. Different nations, services and propulsion philosophies have
attacked the same problem for seventy years. **No field sustains that level of effort against a
need that is not real.**

**Some of the difficulties were real, internal, and are inherited here.** A tail-sitting vertical descent is
harder than a runway landing; a tail-sitter on the ground is more exposed to crosswind; and propellers whose
thrust vectors are all parallel to the body axis produce no rolling moment **by any combination of thrust
settings**. The reaction-torque channel that other coaxial tail-sitters use about that axis is a choice this
configuration declines rather than a limit it inherits (Sections 7 and 8). Precise hovering, ground gusts and
the absence of a thrust-borne rolling moment are configuration facts, and they are inherited.

It would be easy, and wrong, to present the third route as an empty field. **It is not**, and
the paper is better for saying so first.

**And the propeller compromise at the centre of this paper's own ledger is a known result, not a
discovery.** The uncrewed tail-sitter literature states it directly: fixed-pitch propellers make
it *"theoretically impossible to be very efficient in both hovering and forward flight."* A
long-range tail-sitter reported in 2018 describes its own rotor as *"a compromise between
efficient hover and efficient forward flight"* and selects its diameter on exactly that basis.

**What is not established is the combination taken together with its price.** Specifically:
a blended-wing-body tail-sitter in which *every* propulsor is a coaxial, torque-balanced pair —
so that reaction torque and net angular momentum are given up along with the reorientation
mechanism — carrying no aerodynamic control surfaces beyond a single moving device, powered
through a buffered series hybrid, and **audited explicitly against carried hover mass, exposed
cruise drag and hover-sized continuous power**, at two scales and under three sizing contracts.

### One more paragraph of Section 1 as it stood before recomposition (frozen snapshot)

Hybrid VTOL aircraft occupy that corner today, and several are in service. **This paper does
not dispute that they work.** What matters for the argument is *how* each changes between the
two regimes, because that is where the families differ from one another.

---

## S2. Section 2 (from Section 2)

### The opening of Section 2 and the three bills as they stood before recomposition (frozen snapshot)

*Note, outside the frozen text: the body has changed since this copy was frozen. "Often the largest" was unsourced and is gone; "which returns to Bill 1" now reads "a cost in kilograms, though not Bill 1"; and the tail-sitter sentence no longer says the prediction is "borne out" or that the measurement matches the expression, because no source for it has been found.*

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
rather than about quality: a lighter lift rotor is still carried for the whole flight, and a
cleaner lift rotor is still carried for the whole flight. **The mismatch between how long a
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
regime exceeding either pure mode through adverse flow interaction; and — a point that bears on
how such aircraft are designed — that a simulation assuming negligible rotor–structure
interaction *"always predicts higher lift and lower drag than were experimentally observed."*
Separately, a study of twenty-six stationary lift propellers held edge-on found their drag
scaling with frontal area and the square of airspeed, with hover powertrain components adding
*"a significant amount of aerodynamic drag during forward flight"* in the absence of a stowing
mechanism.

**The important property of this charge is not its size but where it falls.** It is charged per
unit time in cruise — so it grows with exactly the quantity the aircraft exists to maximise.

#### Bill 3 — power system sizing

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

---

### The coupling, the transfer table and what the accounting is for, as they stood before recomposition (frozen snapshot)

*Note, outside the frozen text: the body has changed since this copy was frozen. "And it is worth more than the table" is gone; the retraction paragraph now also reports the source's own conclusion, that the advantage lies in a 5 m/s higher range-maximising speed, which this accounting does not price; and the tilting row's first branch is named "a transfer between charges".*

#### The charges are coupled: remedies move cost, among the three charges or outside them

The three charges are not independent problems with independent fixes. **Each known partial
remedy reduces one charge and pays for it, in another charge or in a cost outside the three.** They are three distinct accounting quantities — kilograms,
drag counts, installed kilowatts — and they are not assumed to be independent physical causes: a
remedy can move a requirement from one currency into another. Whether a change of size moves them
together, which would make them one quantity under three names, is tested in Section 12.

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

**One of these transfers has direct experimental support, and it is worth more than the table.**
In the doctoral study whose wind-tunnel campaign is quoted above — and in that document rather
than in the journal article by the same author, which reports a different comparison — a
retraction system removed thirty percent of the airframe's drag; the same work then costed it. Applied to a passenger eVTOL, with the mechanism assessed
at five percent of vehicle mass, maximum range rose from 119 km to 121 km — **a two-kilometre
gain for a five-percent mass penalty.** Bill 2 was converted almost exactly into Bill 1, and
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
from a store, tilting without one imposes Bill 3 and the row is a transfer. If that architecture
already sizes its continuous plant by the hover peak, tilting leaves Bill 3 no worse; then, where the
mechanism's kilograms are fewer than those of the lift group it removes, what keeps the row from
refuting the accounting is the part of its cost that falls outside the three — which is why that part
is listed.

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

## S3. The departures as a table (from Section 3)

| Departure | What it costs |
|---|---|
| **Different hardware** | Bills 1 and 2. The unused set is carried for the whole flight and, if exposed, drags. |
| **Same hardware, but it serves only one duty** | Bills 1 and 2 again. A propulsor that lifts and is then carried is a dedicated lift group under another name, whatever it shares with the cruise system. |
| **Same hardware, both duties, different orientation** | The tilting family. **Bill 3 is incurred unless a store supplies the hover peak**, and the mechanism that changes the orientation adds mass and introduces a control problem through the turn. |
| **Same hardware, both duties, one orientation, different sizing point** | Bill 3 — unless the hover peak is supplied from somewhere other than the continuously installed power. |

---

### "Inverting the table" as it stood before recomposition (frozen snapshot)

The subsection verbatim, before it was recomposed.

The charges exist because the two regimes are served by hardware that is **not the same hardware,
not serving both duties, and not held in one orientation.** Depart from any one of those and a
charge appears. **Different hardware** costs Bills 1 and 2: the unused set is carried for the whole
flight and, if exposed, drags. **The same hardware serving only one duty** costs them again: a
propulsor that lifts and is then carried is a dedicated lift group under another name, whatever it
shares with the cruise system. **The same hardware serving both duties in a different orientation**
is the tilting family: Bill 3 is incurred unless a store supplies the hover peak, and the
mechanism that changes the orientation adds mass and introduces a control problem through the turn.
**The same hardware, both duties, one orientation, but a different sizing point** leaves Bill 3 —
unless the hover peak is supplied from somewhere other than the continuously installed power.

Read one at a time, these are ways to pay. Read as a conjunction, they are a condition.

*(The second departure is stated separately rather than folded into the first because it does real
work later: a propulsor that produces a little thrust in cruise is not thereby serving both
duties, and the distinction decides which parts of a configuration meet the condition and which
do not. "Serving both duties" is the accurate form; hover thrust and cruise thrust are not the
same **job** in any ordinary engineering sense — one supports weight, the other balances drag —
and calling them one would be loose.)*

---

### The opening of Section 3 as it stood before recomposition (frozen snapshot)

The previous section listed moves that redistribute the three charges. This one asks a different
question: what would an architecture have to do in order not to incur them at all? The answer is
a **definition**, derived by inverting the table rather than by describing any aircraft, and it
is stated here before any configuration is offered so that the standard is not taken from the
thing it will be used to measure.

### "The condition" as it stood before recomposition (frozen snapshot)

> **An architecture does not incur the three charges if the propulsors that carry the weight,
> held in one orientation relative to the airframe, produce both the hover thrust and the cruise
> thrust, and if the difference between the hover peak and the cruise demand is supplied from
> a store rather than from permanently installed continuous power.**

Four parts: **same hardware, both duties, one orientation, hover peak from a store.** The first
three come from the first three departures; the fourth comes from the fourth.

Two things in that sentence are choices rather than derivations, and are marked as such. The
table requires only *one orientation relative to the airframe*; **how** an architecture keeps
that while changing flight regime — by rotating the whole body, or otherwise — is not in the
table, and is treated as exposition rather than as part of the definition. And the table's last
row permits the peak to come from **any** source other than the continuously installed power; a
store is the narrower reading used here, because it is what the configuration examined later
uses and because a narrower condition is easier to fail.

---

### "What the condition does not say" as it stood before recomposition (frozen snapshot)

*Note, outside the frozen text: the body has changed since this copy was frozen. The name "zero-bill condition" is no longer used; "a mass one" now reads "a cost in kilograms"; "charges that refusal against" now reads "sets that refusal against".*

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
  second departure is what carries the weight. A propulsor that lifts and then propels
  satisfies the condition. A propulsor that lifts and is then carried does not, whatever else it
  shares with the cruise system.
- **Hardware used in both regimes for something other than propulsive thrust is permitted, and its
  cruise drag is not eliminated.** *Cruise thrust in this paper means the thrust that balances
  cruise drag.* Attitude devices produce thrust in cruise, but they produce no cruise thrust in
  that sense; they are used throughout the flight, so their duty cycle matches their presence and
  they fall outside Bill 1. **They remain in the airstream, so the second charge reaches them.**
  Those are two different statements and the distinction matters: **attitude hardware does not
  stop the propulsor that carries the aircraft from meeting the condition, but it is carried through
  cruise without producing cruise thrust, which is the first failure mode below — and the charges
  are about everything the aircraft carries, so Bill 2 reaches it.** An architecture in that
  position is a partial instantiation, the fourth failure mode: it meets the condition where it
  carries the aircraft and still pays one of the three elsewhere. The condition permits such
  hardware outside the first charge and does not make it free.
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

---

### "What follows from the condition" as it stood before recomposition (frozen snapshot)

*Note, outside the frozen text: two statements in this copy were found to be wrong and are corrected in the body. "Those are three separate questions" pointed at three denials, only one of which is among the three questions then answered; and Section 11 is not the longest of the three answers.*

The condition is a statement about what an architecture would have to be. **It is not a claim
that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim
that satisfying it is desirable.** Those are three separate questions and they are answered
separately: whether the accounting behind the condition survives contact with an independent
sizing study is tested in the next section, against data this work did not produce; whether any
configuration satisfies the condition is the subject of Sections 5 to 7; and what such a
configuration pays instead is the subject of Section 11, which is the longest of the three
answers because it is the one most likely to be wrong.

One consequence is worth stating now, because it shapes everything after it. The third departure — same hardware, both duties, different orientation — is refused by a means other than the
one the field has adopted. A tilting architecture accepts that departure and buys its way out of the first with a mechanism. **An architecture that reorients a propulsor does not satisfy the condition as written**, because
the condition requires one orientation relative to the airframe. **Whether such an architecture
might avoid the three charges by some other route is a separate question this paper does not
settle** — the condition is a definition, not a law, and it can be too narrow without being
wrong. What it is not is retrofitted: it is stated here so that when a configuration is offered
later, the reader can check the claim against a standard fixed before the configuration
appeared.

---

## S4. The independent check: the table, the weight breakdown, and the quadrotor contrast (from Section 4)

| Configuration | Effective L/D | Design gross weight | Dedicated lift group |
|---|---:|---:|---|
| Turboshaft quadrotor | 4.9 | 3 678 lb | none — the rotors serve both regimes |
| **Turbo-electric lift-plus-cruise** | **8.5** | **7 271 lb** | **yes** — eight lift motors and a cruise motor |
| **Turbo-electric tilt-wing** | **8.6** | **6 584 lb** | **none** — eight proprotors, reoriented |

**The weight breakdown shows the transfer, and it does not close on the categories the table
reports.** Of the empty-weight difference of 679 lb, structure accounts for 716 lb in the
lift-plus-cruise entry's disfavour, propulsion returns 146 lb of it because the tilt-wing's
mechanism is heavier, and battery returns a further 10 lb. **Those three categories account for
580 lb of the 679**; the remaining 99 lb lies in empty-weight categories the published table does
not break out, and this work does not know how it is distributed. **What the three reported
categories do show is the transfer property of Section 2 — the mechanism giving part of the
structural saving back — visible inside a weight breakdown this work did not produce.**

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


### Section 4 as it stood before recomposition (frozen snapshot, Round 76)

The whole of Section 4 before the recomposition pilot, verbatim.

*Note, outside the frozen text: the body of Section 4 has changed since this copy was frozen. Where this copy reads "moves the charge", the body now reads "moves the cost"; where it reads "the tilt-wing is the transfer property of Section 2", the body now reads "is consistent with the transfer property of Section 2".*

An accounting proposed by the same people who then use it to argue for a configuration invites
one obvious objection: that the charges were chosen because a particular aircraft happens not to
pay them. The objection arises at the title, not at the ledger, so it is answered here — before
any configuration is described — and it is answered in the only way that settles anything, by
testing a prediction the accounting makes against numbers this work did not produce.

**What follows is not a test of the whole framework.** It checks one falsifiable consequence on
one independent data set. That is a narrow thing, and it is stated narrowly.

#### The prediction, stated before the data

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

#### The data

The check uses a NASA study that sizes **five VTOL architecture families**, most in two
propulsion variants — nine designs in all — against a single mission with common tools and
common assumptions. It was conducted for its own purposes, has no
relationship to the present work, and does not use the three-bill accounting of Section 2 or any
framework derived from it. It is used here for three reasons, stated so that the choice is not
merely the one that agreed: it holds the mission fixed across architecture families, it applies
one set of tools to all of them, and it reports both quantities this prediction needs. The
mission is 1 200 lb of payload over 75 nautical miles.

Three of the nine designs matter here. The turboshaft quadrotor reaches an effective lift-to-drag ratio of
4.9 at a design gross weight of 3 678 lb, with no dedicated lift group: its rotors serve both regimes.
**The turbo-electric lift-plus-cruise design reaches 8.5 at 7 271 lb and carries a dedicated lift group —
eight lift motors beside its cruise motor. The turbo-electric tilt-wing reaches 8.6 at 6 584 lb with none:
eight proprotors, reoriented.**

#### The result

**The primary comparison is the last two designs**, because they isolate the charge. The
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
published weight breakdown is what makes it informative rather than merely large.

**The published weight breakdown shows the transfer property of Section 2 — the mechanism giving part
of the structural saving back — inside a breakdown this work did not produce**, although the categories
it reports do not account for the whole difference (Supplement S4).

**And the source states the second half of the prediction in its own words.** Discussing why the
all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high
cruise efficiency of the lift-plus-cruise type reduces battery weight compared with the
quadrotor, *"but not enough to counter the increase in structure and propulsion weight."* That
is the efficiency credit conceded and found insufficient, by the authors of the data rather than
by the authors of the prediction.

**The quadrotor is reported for scale, and the isolation test above is what carries the
prediction**: against it the lift-plus-cruise design changes three things at once, and the contrast is in
Supplement S4.

**The framework does not predict any of these numbers**; without the input fractions it predicts
no magnitudes. What it predicts is that the amplified weight charge survives the efficiency
credit, and on the isolated pair it does so with the credit reduced to nothing.

#### The tilt-wing is the instructive case

The tilt-wing is the entry that carries the isolation test above, and it is also the entry that
denies this paper a claim it might otherwise be read as making.

**The architecture proposed later in this paper is not the only way to avoid the first charge.**
The tilting family avoids it too — it carries no dedicated lift group, it is the lighter of the
two matched designs, and an independent set says so. The margin in cruise efficiency is one
tenth and nothing is claimed from its direction; what matters is that the dedicated lift group
does not buy an efficiency advantage to set against its mass.

**Second, and this is what the entry is actually for: the tilt-wing is the transfer property of
Section 2 appearing in someone else's data.** It does not escape the accounting by avoiding the
mass charge; it *moves* the charge — to the mechanism that reorients its propulsors, with the
actuation, the gyroscopic coupling and the transition control problem that Section 2 assigns to
that family. The entry therefore does two jobs: it denies this paper a uniqueness it has not
earned, and it confirms the property the accounting is built on. What separates the tilting
family from the configuration described later is not this axis; it is what each pays, and a
sizing study does not settle that.

#### What this check does and does not establish

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

## S5. Section 5 (from Section 5)

### Three paragraphs of Section 5 as they stood before recomposition (frozen snapshot)

**The saving has precedent and it is not this paper's observation.** Reviewing the tail-sitters
of the 1950s, NASA recorded that *"dispensing with a conventional landing gear improved the
empty weight fraction for these VATOL aircraft"*, while noting that some form of gear was still
required on the tail surfaces. The present arrangement takes that benefit and extends it by
giving the same structure the control duty as well.

**And one historical difficulty is inherited rather than removed.** A tail-sitting aircraft on
the ground is more exposed to crosswind than a conventional one. The stance base is the answer
this configuration offers, and it is a parameter rather than a proof.

One of the 1954 objections is genuinely removed and it should be named exactly. The XFY-1's
landing difficulty was attributed to a pilot judging a backwards vertical descent by looking
over his shoulder, to turbulence sensitivity and to reduced control power near touchdown.
**There is no pilot here, and height above ground is a sensor measurement rather than a human
estimate.** That disposes of the spatial-orientation objection and nothing else. **Precise
hovering, ground gusts and the descent itself are not disposed of by removing the pilot**, and
this section does not pretend otherwise.

### One more paragraph of Section 5 as it stood before recomposition (frozen snapshot)

This is the part of the section that decides whether the rest of it can be trusted.

---

## S6. Section 6 (from Section 6)

### Three paragraphs and a heading of Section 6 as they stood before recomposition (frozen snapshot)

On this axis the alternative is the multirotor, and as in the previous section the comparison
runs one way only. **Nothing here is claimed against fixed-wing aircraft.** A runway-launched
aeroplane cruises more efficiently than this configuration and pays none of the charges of
Section 2; that comparison is not made, and no result in this paper rests on it. The claim is
confined to the one thing the multirotor family structurally lacks: **a surface that carries the
cruise lift.**

Section 5 established the first half: the aircraft must leave from and return to a site that
supplies nothing. **A multirotor meets that requirement completely.** It is not a deficient
machine and this section does not treat it as one; it is excellent at what it does and is
limited by the price of doing it that way.

The wing that makes cruise efficient is carried through the vertical phase, where it produces
nothing and presents the aircraft's largest surface to ground wind. The tailless planform that
follows from having no boom constrains the sweep, because with no horizontal stabiliser the
pitching moment must come from the distribution of lift along the body itself. And the
fixed-pitch propeller that serves both regimes is the reason the margin above sits where it does
rather than higher — at a propeller efficiency η_p = 0.85 the same airframe would reach 7.47 to 9.20. Section 11 charges all three.

Heading: *Five qualifications, and every one of them runs against this configuration*


### Two more passages of Section 6 as they stood before recomposition (frozen snapshot)

- **Examined envelope, 5.56 to 7.39.** These are the bounding combinations permitted by two
  independent model inputs. **They are not four demonstrated aircraft states**, and nothing here
  shows that a built aircraft would land simultaneously on both bounds.
- **Best examined blade family, 6.00 to 7.39.** The highest efficiency among the families
  examined is 0.683; holding it and sweeping only the drag bracket gives this range.

**The quadrotor is a good quadrotor.** Its disc loading is 3.5 lb ft⁻², which is unusually low
and unusually efficient. Nothing here is compared against a poor example.

---

## S7. Section 7 (from Section 7)

### The opening of Section 7 as it stood before recomposition (frozen snapshot)

None of the three elements is new.

Tail-sitting aircraft were flown in the 1950s and are ordinary among uncrewed aircraft today,
including with blended-wing-body planforms and contra-rotating propulsion. Blended wing bodies
have been a standing subject of transport research for three decades. Series-hybrid propulsion
has established precedent in small uncrewed aircraft. **Each can be found on its own, and in
combination, in the literature and in hardware** — Section 1 says where.

---

## S9. Section 9 (from Section 9)

### "It does not claim range against fixed-wing aircraft" as it stood before recomposition (frozen snapshot)

**1. It does not claim range against fixed-wing aircraft.** The vertical axis is where the
fixed-wing family is the opponent; the range axis is not. A runway-launched aircraft that never
claimed vertical capability pays none of the charges of Section 2, and nothing here competes
with it on distance.

---

### "It does not claim vertical capability against multirotors" as it stood before recomposition (frozen snapshot)

**2. It does not claim vertical capability against multirotors.** That comparison runs the other
way and would be absurd. The multirotor family is the opponent on cruise efficiency only.

---

### "It does not claim mechanical simplicity" as it stood before recomposition (frozen snapshot)

**4. It does not claim mechanical simplicity.** Part count, assembly mass, failure modes and
maintenance burden were not measured, and nothing here supports a statement about reliability.
What is offered is a **count** of mechanism classes that a tilting architecture requires to
change regime and that this arrangement does not. A count is not a reliability argument, and
readers who convert one into the other are not quoting this paper.

---

## S10. Section 10's paragraphs as they stood before compression (from Section 10, Round 73)

Every paragraph of Section 10 that lost a sentence or a clause in compression is given here in full, verbatim.

#### The inputs, and why there are four closures rather than one

**The sizing rules that keep that ratio valid as the mass moves are worth stating, because they
also say what the four closures are geometrically.** The loop holds **wing loading, disc loading
and aspect ratio** fixed, so area, span and disc diameter follow the mass: across the four
closures the wing area runs 2.07 to 2.27 m², the span 3.53 to 3.70 m, and the nose disc diameter
1.23 to 1.29 m. **The cruise lift coefficient is unchanged at 0.450 in every one of them**, so the
lift-to-drag ratio is an input that stays valid at the closed mass rather than one frozen at a mass
the loop has left behind. Had wing **area** been held fixed instead, the lift coefficient would
have risen with the closed mass, the induced term would have moved against the heavier closures,
and the drag corners would be optimistic as reported.

#### The transition, and this is where the section turns

**In this point-mass model there is no transition time to optimise**, which is a simplification
rather than a trade.
The control moment required scales as 1/t_r² and the control power as 1/t_r³, and the altitude
loss falls with t_r as well: all three point the same way, so the rotation time is set by what
the actuator can do rather than by a balance between competing penalties.

---

## S11. The zero-lift drag build-up as a table (from Section 11)

| | favourable end | adverse end |
|---|---:|---:|
| Clean wetted surface | 0.0073 | 0.0142 |
| Hub and small items | 0.0015 | 0.0022 |
| **Tip frames** | **0.0043** | **0.0047** |
| **Attitude rotors, free-wheeling** | **0.0154** | **0.0169** |
| Total | 0.0285 | 0.0381 |

### What the closure does not contain (from Section 11)

| Item | Status |
|---|---|
| **The cost of declining the reaction-torque channel** | Not computed. Thrust asymmetry, propulsive efficiency and the lag set by rotor inertia; quantifying it requires a control-allocation study rather than a torque figure. |
| **The transition altitude result** | 5.4 m in the finite-moment model at the 50 kg reference geometry — **a result, not a charge**, and not a term in any sizing loop here. |
| **The strip's actuation** | Carried in the systems budget without sizing the mechanism. The number of actuators is not fixed by this study. |
| **The take-off margin** | Drawn from the tip pairs, because the nose pair is sized at thrust equal to weight. It competes with attitude authority and neither is closed against the other. |
| **Landing transition, vortex ring state, closed-loop hover control** | Not analysed. |
| **Engine installation — bay, intake, exhaust, cooling** | Absent from this work entirely. |
| **Rotor–structure and rotor–wing interference** | Inside Bill 2 in principle, absent from the build-up in practice. |

### Section 11's paragraphs as they stood before compression

Every paragraph of Section 11 that lost a sentence or a clause in compression is given here in full, verbatim (Round 71).

#### What this section does, and the one thing it must not do

**The refusal has an address, and saying where it points is what keeps it from reading as an
unfinished cost section.** These three quantities become one number only under a sizing contract,
and that is Section 13: **the total is the contract, not a property of the aircraft.** For a
specific mission a designer weights them against that mission's own constraints. **Reporting them
is this paper's job; the weighting belongs to whoever has the mission.**

#### The cruise-efficiency gap under fixed pitch

**Nor is the gap decomposed.** How much of it is blade twist, how much is section drag at the
cruise inflow angle, and how much is the operating point itself, this work does not say. Anything
finer would be a decomposition that was never performed.

#### What the ledger amounts to

The non-clean-body drag terms remove 42.3 to 47.4
percent of the clean-body lift-to-drag ratio, and the hardware exposed by the vertical-phase
layout is the majority of the zero-lift drag. Bill 1 appears as a 3.6 percent buffer rather than a
lift group. Bill 3 is divided by 2.4 to 3.2 at the engine and is not divided at all on the
electrical path. **The cruise propeller efficiency sits 14.6 to 21.0 percent below the published
assumption under fixed pitch.**

**And every one of them belongs to one scale.** The four closures vary the drag uncertainty and
the blade-family choice at the reference size; **they do not establish how the three charges
behave as the aircraft changes size.** Section 12 asks whether they move together when the size
changes, and Section 13 asks what happens to the comparison when the sizing contract changes.

*(Round 72, second pass)*

#### Bill 2 — the drag of hover hardware, inside the bracket

**The rotor line rests on section drag at low Reynolds number.** It is a blade-element result for
blades whose sections run near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section
polars that are computed rather than measured, and section drag is hardest to predict in that range.
Section 12 shows how strongly the term depends on it.

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

*(Round 73)*

#### What the closure does not contain at all

The closure does not contain the cost of declining the reaction-torque channel, the sizing of the strip's
actuation, the allocation of the take-off margin against attitude authority, the landing transition, the vortex
ring state, closed-loop hover control, engine installation, or rotor–structure and rotor–wing interference. **None
of these is a ledger entry; Section 14 lists them.** The transition altitude result (5.4 m) is a result, not a
charge, and is not a term in any sizing loop (the table is Supplement S11).

---

## S12. Section 12's paragraphs as they stood before compression (from Section 12)

Every paragraph of Section 12 that lost a sentence or a clause in compression is given here in full, verbatim.

Section 11 decomposed the three charges on one aircraft, at one size. **This section asks a
different question: are they three quantities, or one quantity under three names?** The test is
to change the size of the aircraft and see whether they move together. If they did, the framework
of Section 2 would be a single cost described three ways, and a ledger in three currencies would be
a ledger in one. Either answer leaves the mechanism claim where it was; that claim rests on the
inventory of Sections 7 and 8.

**This is a different axis from the one Section 11 examined.** There, Bill 2's share of the
zero-lift drag was compared at the two ends of the drag bracket, at a fixed size. Here the size
changes. The two answers are about different variables and do not bear on each other.

#### What is compared, and why it is these two points

**Section 10 closed only the light configuration, at 52.3 to 57.5 kg. No closure was run at 1 000 kg**, and
none could be run on the same footing: the heavy design has neither a drag bracket nor a structural
closure (both below). A scale comparison therefore cannot be made from Section 10's closures. **It
is made between the two reference designs, 50 kg and 1 000 kg, sized by one method, and both ends are taken from that pair.** In this section *the light design* and *the heavy design* mean
those two reference designs. Taking one end from Section 10 and the other from the reference pair would manufacture a scale
change that is really a propeller-efficiency update applied to one end only.

**The quantities used are, with one exception, ones Section 10 did not replace.** Disc loading is a sizing rule
Section 10 holds. The buffer fraction is an input to its loop. The free-wheeling rotor term is the value Section 10 carries at both ends of its bracket at 50 kg,
before the ten percent margin of the adverse end (Section 11), and it is computed here at 1 000 kg by
the same method. **The total zero-lift drag, the propeller efficiency, the range and the closed mass
are not used.** The exception is the engine rating inside the Bill 3 ratio, which Section 10 did replace; it is
taken from the reference pair and said so where it is used. No heavy-design range is quoted: the figures available for it either omit the
free-wheeling rotor charge or carry an assumed rather than a computed propeller efficiency, and none
carries both.


**Two conditions travel with the heavy design.** It has no drag bracket; it stands on a single
zero-lift coefficient with no equivalent bound. And **its structural closure is undetermined**: shell
mass scales with wetted area while take-off mass scales with volume, so the structural fraction
depends on how areal density grows with size, and that exponent has not been measured. **The
comparison below uses powers, loadings and drag terms; it does not use the structure**, which is why
it can be made at all.

#### Bill 3 — held nearly flat by a sizing rule, which is not a finding about Bill 3

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

#### Bill 2 — the rotor term falls, and in this model Reynolds number accounts for it

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

#### Bill 1 — not tested, and the one available derivation would not test it

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

#### Two costs that scale does not relieve

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

#### Why this section sits between the ledger and the contracts

**The next section needs only what this one shows.** If the three charges were one quantity, a single
number could rank architectures whatever weight each charge was given. **Because at least two of them
are not locked together, a comparison of architectures cannot in general be reduced to a number that
does not depend on how the charges are weighed: where one architecture pays less of one charge and
more of another, the ranking depends on the weighting.** The argument requires only two charges that
are not locked together; the third need not be shown separate for the conclusion to hold. A third
shown to be separate would strengthen it; a third shown to be locked to one of the others would
leave it standing.

---

## S13. Sensitivity of the lift-plus-cruise comparison (from Section 13)

| Case | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass | Shift, first to third |
|---|---:|---:|---:|---:|
| As above | +55 to +84 % | +28 to +54 % | −13 to +7 % | 67 to 77 points |
| Lift group 5 % of take-off mass | +55 to +84 % | +47 to +76 % | +36 to +65 % | 14 to 24 points |
| Lift group 15 % of take-off mass | +55 to +84 % | +8 to +31 % | −62 to −50 % | 117 to 134 points |
| All three at this configuration's propeller efficiency | +33 to +45 % | +6 to +17 % | −33 to −25 % | 65 to 72 points |
| Lift-plus-cruise drag as a fixed increment, not a ratio | +59 to +75 % | +31 to +45 % | −13 to +5 % | 67 to 75 points |

*(Range of the lift-plus-cruise layout relative to this configuration, across the four closures.)*


### Section 13's paragraphs as they stood before compression

Every paragraph of Section 13 that lost a sentence or a clause in compression is given here in full, verbatim.

#### Three contracts, and what each holds equal

- **Fixed fuel fraction.** Every architecture carries sixteen percent of its own take-off mass as
  fuel. **Take-off mass cancels from range**, which is then set by L/D and the chain alone. A
  heavier architecture shows its mass in the take-off-mass column and nowhere in the range column.
- **Fixed fuel mass.** Every architecture carries the fuel this configuration carries at the same
  closure — 8.4 to 9.2 kg. **Range is divided by take-off mass**, so a heavier aircraft flies the
  same fuel less far.
- **Fixed take-off mass and payload.** Every architecture is held to this configuration's closed
  mass and its 13 kg payload. **Fuel is what remains after the empty mass**, so every kilogram of
  architecture-specific hardware is a kilogram of fuel not carried.

#### Against the tilting layout: a bound, not a ranking

**There is a trade, but it is lopsided.** The tilting layout closes 0.5 to 5.4 percent heavier than
this configuration, and it cruises at the clean airframe's lift-to-drag ratio with a propeller at 0.80:
it is credited with no nacelle drag, no pivot fairing, and no penalty for flying hover-sized rotors as
cruise propellers. **Even the contract that weights mass most** — a fixed take-off mass, in which every
kilogram of tilt mechanism is a kilogram of fuel not carried — **leaves the bound's margin at 93 to 130 percent.**
The contract moves the comparison, as Section 12 says it must where there is a trade; none of the
three moves it far enough to matter. A ranking against a competitor modelled as a bound is not a
ranking, and **no range claim is made against the tilting family in either direction.**
The claim this paper makes against that family is about mechanism (Sections 7 and 8), and nothing in
this section bears on it.

#### Section 2's prediction, tested

**The size of the shift behaves the same way.** It barely moves when the propeller or drag basis is
changed — 65 to 77 points across those cases — because those asymmetries enter all three contracts
alike. It moves a great deal with the lift group, from 14 to 134 points, because the shift *is* the
mass difference being counted. **What is robust is that the shift exists and runs toward the lighter
aircraft; its size is the size of the mass difference.**

#### What the framework asks of whoever uses it

**Carry the audit, for every column.** State each charge in its own currency — kilograms, drag
counts, installed kilowatts — before any aggregate, and state the basis of the comparison with its
asymmetries and their directions. An aggregate that arrives without its parts cannot be checked, and
the parts are where the comparison is decided. **This paper meets that for its own column** (Section
11) **and not for the competitors'**, whose kilograms and drag counts here are parameters and transferred
ratios rather than an audit — which is one more reason no ranking against them is offered.

**Refuse the bare ranking.** Report an ordering only with the contract it was computed under, and,
where its sign depends on an unmeasured quantity, with that quantity named. An ordering that holds
under every contract examined may be reported as such — that is a stronger statement than any one
contract gives, and it still names the contracts. Applied to this paper's
own numbers, the rule is the fourth row of Section 9: **no range claim is made against lift-plus-cruise
or tilting layouts**, because the ordering against the first depends on the contract and on the
competitor's lift-group mass, and the ordering against the second is against a bound.

*(Round 71, second pass)*

Section 12 showed that at least two of the three charges are not locked together, and drew the
consequence: where one architecture pays less of one charge and more of another, a ranking depends
on how the charges are weighed. **A sizing contract is one such weighing.** It fixes what is held
equal between the architectures being compared, and what is held equal decides how a difference in
mass is set against a difference in cruise efficiency. This section applies three contracts to three
architectures at each of the four closures of Section 10. **The mechanism claim is not a ranking
and is not at stake here**; what is at stake is how the price computed in Sections 10 and 11 enters
a comparison with other architectures.

#### Against lift-plus-cruise: a trade, and the contract sets the exchange rate

**Under a fixed fuel fraction the mass difference does not reach the range column**, and the
lift-plus-cruise layout flies 55 to 84 percent further. Under a fixed fuel mass the difference enters
as a divisor, and its lead falls to 28 to 54 percent. Under a fixed take-off mass it enters as fuel not
carried, and **the lift-plus-cruise layout lands between 13 percent short of this configuration's
range and 7 percent beyond it.** Moving from the
first contract to the third shifts the comparison by **67 to 77 percentage points at every closure**
at the declared lift-group fraction, and always toward the lighter aircraft.

#### Section 2's prediction, tested

**With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every
closure; with a heavier one this configuration leads under a fixed take-off mass at every closure.**
Giving all three the same propeller efficiency also produces a reversal at every closure. **Which
architecture ranks first under a fixed take-off mass is therefore decided, in this model, by a mass
fraction of the competitor that this study has not measured** — and the fixed-fuel-fraction column,
where mass does not enter, does not move with it at all. **Put plainly, the sign under a fixed take-off
mass is not a result about the architectures; it is a result about that parameter**, and it is the
one most worth measuring.

#### What the framework asks of whoever uses it

**Name the contract.** A comparison of architectures is a comparison under a contract. The contract is
chosen by the mission rather than by the analyst, and a comparison that does not state one has chosen
one silently.

#### What this section does not establish

**The competitors are modelled at a coarser level than this configuration.** Their drag is a ratio
transferred from another airframe or an idealisation; their propeller efficiency is assumed; their
architecture-specific mass is a parameter. This configuration's drag and propeller efficiency are
computed. **Comparing computed figures against assumed ones favours whichever is assumed more
optimistically**. In propeller efficiency that is both competitors, and the sensitivity case that gives all
three this configuration's propeller efficiency shows the size of it: under the first contract the
lift-plus-cruise layout falls from +55 to +84 percent to +33 to +45 percent (Supplement S13); in drag it is the tilting layout, by construction.

---

## S14. What is not known, what each item bears on, and what would settle it (from Section 14)

| Item | Bears on | What would settle it |
|---|---|---|
| **The pitching moment through the transition.** Three methods of three fidelities diverge above about ten degrees of incidence; the rotation passes through that band, peaking near 18 to 22 degrees on the 50 kg reference geometry, with the inboard half of the wing in the slipstream at a much lower effective incidence. | Whether the aircraft trims through the rotation (Sections 7 and 10) | **Validated aerodynamic data**: a measurement of the outboard wing's pitching moment to about 22 degrees at low dynamic pressure and of trim at the attached-flow end of the rotation, or a higher-fidelity method validated against one |
| **Section drag at low Reynolds number.** The attitude rotors' free-wheeling charge rests on section polars below a Reynolds number of 10⁵, and the uncertainty runs both ways. | The 0.0154 rotor term in every closure (Sections 10 and 11) and the size of Bill 2's fall with scale (Section 12) | **Validated data**: the drag of a free-wheeling attitude rotor, or of its sections, at about 8 × 10⁴, or a method validated there |
| **The tip pairs' other cruise state.** Free-wheeling is determinate and computed; stopped is a family of states whose means and azimuth are not fixed (Section 8). | Whether a lower-drag cruise state is available, and at what mechanism cost | **Analysis**, or a measurement of one stopped state |
| **The buffer's energy, not only its power.** The store is sized here by power. Whether it also holds the energy for the vertical phases and their reserves, and how it is recharged in cruise, depends on a hover duration this work does not fix; at the bench rate the unit pack emptied in about four minutes. | Whether the store sized by power is also large enough | **Analysis** against a defined mission profile |
| **The electrical path at peak.** Machines, power electronics, wiring and their cooling carry the full take-off demand; they enter the loop as a mass fraction, not as components sized for that peak and its heat. | Whether the path that delivers the buffer's power exists at the mass assumed | **Component sizing and thermal analysis** |
| **The airframe's mass.** It enters the loop as a construction constant, thirty percent of take-off mass (Section 11). A component build-up at the reference mass leaves room for the 13 kg payload only if the average shell areal density stays at or below 1.78 kg m⁻², against 1.50 assumed; the build-up carries a contingency rather than a structural sizing, and it has not been re-run at Section 10's closed masses, still less at the masses the store re-closure returns. At the 1 000 kg reference design the shell-mass exponent is not measured at all. | Every closed mass | **Structural sizing** (analysis), then a **built article** (measurement) |
| **The strip and the fairing.** The strip's effect on this planform is computed, not measured, and its actuation is carried in the systems budget without being sized (Section 11); the fairing is sized against a published stability criterion, and the side force it develops is not measured. | The strip: the body roll axis, which appears as bank in cruise and as a change of heading in hover (Section 8). The fairing: directional stability in cruise | **Measurement** of both surfaces; **sizing** of the actuation |
| **Closed-loop hover control**, including the cost of declining the reaction-torque channel, the absorption of the hover torque residual left by trimming each pair's torque balance at cruise (Section 8), and the allocation of the tip pairs between take-off margin and attitude authority, which compete for the same propellers. | Whether hover is controllable with the authority computed (Sections 5 and 8) | **Analysis not yet done**: a control-allocation study, then simulation |
| **Vertical descent and the landing transition.** Neither is analysed; the vortex ring state is not assessed, and the landing transition is not the take-off transition run backwards. | Whether the aircraft can come down as it went up (Section 5) | **Analysis not yet done** |
| **Ground handling and landing loads.** The stance base is a parameter against static crosswind (Section 5); the response to a landing with lateral velocity or on uneven ground, and handling between flights, are not assessed. | Operation from unprepared sites | **Analysis not yet done** |
| **The competitor's lift-group mass.** It decides the sign of the fixed-take-off-mass ordering in Section 13. | Section 13's sensitivity, not a claim | **Measured inventories** of lift-plus-cruise aircraft of this class |
| **Engine installation** — bay, intake, exhaust, cooling. | Mass, drag and packaging | **Absent from this work entirely** |
| **Blade-family selection.** The criteria that would choose among the blade families — structural loads, acoustics, the motor operating point, rotor inertia, manufacture — are not modelled (Section 10). | Which point of the envelope the aircraft occupies | **Analysis not yet done** |
| **Atmosphere.** Every number here is at sea level; the configuration's own altitude sensitivity has been computed for hover power and propeller efficiency, its effect on the Section 6 comparison has not. | The comparison in Section 6, made against a mission flown at altitude | **Analysis**: the direction of the effect has not been computed |

### Two paragraphs of Section 14 as they stood before recomposition (frozen snapshot)

**This is where the coupling Section 12 found is paid.** The buffer is the conversion the escape
condition permits — kilowatts of hover peak paid in kilograms of store. Section 11's ledger records that
conversion at the assumed store; at a measured specific power it costs thirteen to fifteen percent of
take-off mass instead of 3.6. **The escape from Bill 3 is real in the sense Section 3 defined it, and
its price depends on a component whose required performance has not been demonstrated.**

**None of these is a small correction to a known quantity.** Two of them need validated data rather
than more of the computation already done: the transition moment, because three methods have been
tried against it and disagree, and the low-Reynolds section drag, because the one method used here is
least reliable exactly there. Several — hover control, the descent, the buffer's energy, the electrical
path — are analyses this study has not posed. One — the engine installation — is not in the work at
all.

### The paragraph after the re-closure table as it stood before recomposition (frozen snapshot)

**At the bench rate the loop closes about three-quarters heavier**, with a buffer of about fourteen
percent of take-off mass rather than 3.6. If Section 10's take-off masses are retained instead, the
payload falls to about 7 kg rather than 13. At the flown system's continuous rating the loop only just
closes, and the mass it returns is set by how near the loop is to not closing rather than by anything
about the aircraft. At the unit pack's continuous rating it does not close at all.

### The paragraph on measured store figures as it stood before recomposition (frozen snapshot)

**What has been measured is a fraction of that, and the figures available are of three different
kinds.** A 24-series nickel–cobalt–manganese pack designed, bench-tested and flown in a 210 kg-class
electric VTOL aircraft is rated, as a flown system, at 0.892 kW per kilogram continuous; its 13.5 kg
unit pack, discharged on the bench at its highest tested rate of 10.68C, delivered on average about
1.5 kW per kilogram for about four minutes and reached 55.1 °C against the 60 °C limit its authors
adopted. A NASA-funded design study adopts 4 kW per kilogram and describes that figure as about twice
that of existing batteries. The same study notes lithium-polymer figures in the literature as high as
3 kW per kilogram, which it cites rather than measures; against that figure the take-off demand is 1.8
to 2.0 times. **The take-off demand of Section 10's closures is 3.7 to 4.1 times the
bench rate — the highest of the measured figures — and 6.2 to 6.8 times the flown system's continuous
rating**; hover alone is 3.1 to 3.5 times the bench rate. The comparison is between unlike ratings: a
peak demand held through the vertical phases, a bench average over minutes, a continuous rating, and a
design assumption. **The gap is real on every one of them; the factor quoted is peak demand against
bench average.** The package Section 10 closes on does not exist with any store the sources consulted
here report as built.
