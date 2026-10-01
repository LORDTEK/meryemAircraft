> **Reader packet, part 2 of 4** (commit `0076354`). Read all parts before answering; the round text says what to judge.

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

Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Supplement S10).

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

The engine is sized by cruise, **3.54 to 5.17 kW** of shaft rating, against a hover requirement of **11.4 to 12.5 kW** at the rotor shaft: a ratio of installed hardware of **2.4 to 3.2**, which is not the buffer's burden (Section 7 computes that). **But the full hover power passes through the electrical path, and that path is sized by it.** **Bill 3 is removed from the engine and left standing on the electrical system** (the propulsion-mass split is in Supplement S11).

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
