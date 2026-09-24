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
  fuel. **Take-off mass cancels from range**, which is then set by L/D and the chain alone.
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
fixed take-off mass. **That comparison is not used**, because it would set
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
  other two use 0.80. **Both are assumed, not computed**, and the
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

**What the bound gives is a size, not an order.** A tilting layout credited with no cruise penalty
at all is 93 to 141 percent ahead of this configuration under every contract at every closure, and
moving from the first contract to the third shifts that by 1 to 18 points toward this configuration. **That margin is the room
a real tilting aircraft's cruise penalties would have to fill** — nacelle drag, pivot fairing,
hover-sized rotors flown as cruise propellers — none of which is modelled here, and how much of it
they fill is not computed.

**There is a trade, but it is lopsided.** The tilting layout closes 0.5 to 5.4 percent heavier than
this configuration, and it cruises at the clean airframe's lift-to-drag ratio with a propeller at 0.80. **Even the contract that weights mass most** — a fixed take-off mass, in which every
kilogram of tilt mechanism is a kilogram of fuel not carried — **leaves the bound's margin at 93 to 130 percent.**
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
the case above it is the blade family, which Section 10 leaves open. Across the sensitivity cases
(the full table is Supplement S13) it is the competitor's lift-group mass and the propeller basis.

**With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every
closure; with a heavier one this configuration leads under a fixed take-off mass at every closure.**
Giving all three the same propeller efficiency also produces a reversal at every closure. **Which
architecture ranks first under a fixed take-off mass is therefore decided, in this model, by a mass
fraction of the competitor that this study has not measured** — and the fixed-fuel-fraction column,
where mass does not enter, does not move with it at all. **Put plainly, the sign under a fixed take-off
mass is not a result about the architectures; it is a result about that parameter**, and it is the
one most worth measuring.

**The size of the shift behaves the same way.** **What is robust is that the shift exists and runs toward the lighter
aircraft; its size is the size of the mass difference.**

### What the framework asks of whoever uses it

A framework that says every remedy transfers a charge rather than removing it takes something from
its user in return. **It asks for three things, and this paper holds itself to them.**

**Carry the audit, for every column.** State each charge in its own currency — kilograms, drag
counts, installed kilowatts — before any aggregate, and state the basis of the comparison with its
asymmetries and their directions. **This paper meets that for its own column** (Section
11) **and not for the competitors'**, whose kilograms and drag counts here are parameters and transferred
ratios rather than an audit.

**Name the contract.** A comparison of architectures is a comparison under a contract.

**Refuse the bare ranking.** Report an ordering only with the contract it was computed under, and,
where its sign depends on an unmeasured quantity, with that quantity named.

### What this section does not establish

**The competitors are modelled at a coarser level than this configuration.** Their drag is a ratio
transferred from another airframe or an idealisation; their propeller efficiency is assumed; their
architecture-specific mass is a parameter. This configuration's drag and propeller efficiency are
computed. **Comparing computed figures against assumed ones favours whichever is assumed more
optimistically**. In propeller efficiency that is both competitors, and the sensitivity case that gives all
three this configuration's propeller efficiency shows the size of it: under the first contract the
lift-plus-cruise layout falls from +55 to +84 percent to +33 to +45 percent (Supplement S13); in drag it is the tilting layout, by construction.

**The comparison is at one size.** Section 12's 1 000 kg reference design has no closure, and none of its figures
is used here.

**And nothing here ranks architectures for a mission.** Which contract a mission implies, and which
architecture it then favours, is the user's question. What this section establishes is narrower: **the
same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by
tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property
of the architectures alone.
