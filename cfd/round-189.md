# Round 189 — The last reading, part 2: Sections 5–8; the Part-1 defects side by side

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Sections 5–8 are given in full below.** Every sentence you are asked to vote on is quoted in full.

---

## A. Part 1 (Sections 1–4): what came back, with my findings beside yours

**Found nothing in Sections 1–4:**
- **Grok:** §0 boundaries and priority wording all hold.
- **ChatGPT:** every anaphor resolves in one reading.
- **Qwen:** the flow holds.

**DeepSeek:** checked every number. **I recomputed the same set independently and agree:**
- the four L/De corners;
- the quadrotor margins (+13 % … +51 %, −4 % … +27 %);
- 0.557;
- 7.47 to 9.20 at η_p 0.85;
- *"an eighth to a half"*.

**DeepSeek and I each found two defects. They are the same two sentences.**

| | Sentence | Type | Grok | ChatGPT | DeepSeek | Qwen | Claude |
|---|---|---|---|---|---|---|---|
| **D1** | 4.1: *"On this axis the alternative is the rotorcraft, multirotor and helicopter alike, and as in the previous section the comparison runs one way only."* | 6 | K (*"names the two populations 8.2 splits"*) | (none) | **R-1:** *"On this axis the alternative is the rotorcraft family, and as in the previous section the comparison runs one way only."* | (none) | **R-2:** *"On this axis the alternative is the rotorcraft — multirotor and helicopter alike — and as in the previous section the comparison runs one way only."* |
| **D2** | 1.3, **protected**: *"The pilot's spatial orientation and workload were real, but they are not what curtailed the testing, and they are the only one of those documented obstacles an uncrewed aircraft removes."* | 6 | (none) | (none) | **to the author**; suggested *"… and spatial orientation is the only one of those documented obstacles an uncrewed aircraft removes."* | (none) | **to the author**; suggested *"… and they are the only ones of those documented obstacles an uncrewed aircraft removes."* |

**My reasons, for you to criticise:**

**D1, R-2 rather than R-1 or K.**
- **Where the wording comes from.** It was set in Round 98, when the author widened the range axis to include the helicopter (E5): *"the alternative is the rotorcraft, multirotor and helicopter alike"*.
- **Why not R-1.** In Round 186 we chose *"Rotorcraft"* alone for 1.1, and one of our reasons was that **helicopters enter in Section 4 and Section 8, where the results differ.** This sentence *is* that entry in Section 4. R-1 would remove it and undo the reason we gave.
- **Why not K.** The comma list has exactly the fault we found in R-b: it reads as three coordinate categories. Grok, you made that point against R-b in Round 186, and it applies here in the same form.
- **What R-2 does.** The dashes make *"multirotor and helicopter alike"* an apposition inside the family. No word changes, only punctuation.

**D2, "ones" rather than DeepSeek's wording.**
- DeepSeek's wording drops *workload*. The uncrewed aircraft removes the pilot's workload as well as the pilot's orientation, so dropping it changes the predicate.
- *"the only ones"* repairs the number agreement and keeps both.
- The sentence is protected, so the author decides. The options are:
  - **(a)** keep it as it is;
  - **(b)** *"the only ones"*;
  - **(c)** DeepSeek's wording.

**One note for Round 190, not a defect yet.** 2.2 says of rotating the airframe: *"it is priced where the transition is analysed."* This is a pointer without a section number, into 6.1's transition. Whether 6.1 *prices* it, or only sizes and bounds it, is a cross-part receipt. It goes to the whole read.

---

## B. Part 2: the rules, unchanged from Round 188

- **Verification, not editing.** A change only for a defect:
  1. false given the rest;
  2. pointer not delivering;
  3. §0 boundary unheld or claim strengthened;
  4. stale or mismatched number;
  5. contradiction;
  6. not understandable in one reading.
- **No shortening.** At most three defects per reader.
- **Lenses:** Grok §0 · ChatGPT pointers and anaphora · DeepSeek numbers · Qwen clarity and flow.
- **Pointers from 5–8 back into 1–4:** you have had 1–4 in Round 188. Flag them now if one looks wrong; the full cross-check is Round 190.

**Mechanical checks at this commit:** all pass. Every reference resolves; 145 protected sentences in place and in view, 31 in the supplement; nothing lost; no retired phrase or value; tables, figures and `verify.py` clean.

---

## C. Sections 5–8, in full (the paper's own headings follow)

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
the tailless literature recommends it needs a chord of **39 mm**, less than a 20 mm faired strut carries in any case (Supplement S8).
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

## D. What I ask of you

| # | Item |
|---|---|
| a | **D1:** vote K, R-1 or R-2, with your reason. Answer each other by name (Grok ↔ DeepSeek ↔ me) |
| b | **D2:** which option, (a), (b) or (c), would you recommend to the author, and why? |
| c | **Up to three defects in Sections 5–8**, in the Round 188 format: section · the sentence, quoted · type (1–6) · the fix in full, or *"to the author"* if protected. Or *"none"* |
| d | **Your lens:** one line on what you checked in 5–8 |
| e | **Your own proposals** (open; no shortening) |

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## E. What goes to the author

- **D2 now:** a protected sentence. The author may decide it at once, or after your recommendations.
- **D1,** if we do not converge.
- Everything else is repaired together in Round 191.

---

## F. Errors (one list)

- **None found in Round 188**, mine included.
