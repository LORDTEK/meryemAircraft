# Round 190 — The last reading, the whole: pointers across sections, transitions, the §0 map, headline numbers

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Sections 1–4 were given in full in Round 188, and 5–8 in Round 189. **Everything you are asked to judge here is quoted in full below.**

---

## A. Part 2: what came back, and what is decided

- **D1 (4.1): R-2, all five.**
  - Grok moved from K: *"I was wrong to mark K."*
  - DeepSeek withdrew R-1.
  - Applied in Round 191: *"On this axis the alternative is the rotorcraft — multirotor and helicopter alike — and as in the previous section the comparison runs one way only."*
- **D2 (1.3, protected): the author decided (b)** (E24, my translation: *"(b) approved for D2"*). All four of you had also recommended (b). Applied in Round 191: *"… and they are the only ones of those documented obstacles an uncrewed aircraft removes."*
- **Sections 5–8:** Grok, ChatGPT and Qwen found no defect. **DeepSeek found one (D3), and my check does not support it:**

> 5.2: *"The frames project ±0.71 m from the planform, so an upper–lower differential acts at 0.71 m in pitch and a left–right differential at the semi-span, 1.726 m — 2.43 times the pitch arm."*

**DeepSeek:** the pitch arm is the separation, 1.42 m, so the ratio is 1.22.

**My check:**
- Both arms in the sentence are measured the same way: **from the centre to each pair.** That is 0.71 m for an upper or lower pair and 1.726 m for a left or right pair.
- A differential ±ΔT on two opposing pairs gives M = 2ΔT × 0.71 in pitch and M = 2ΔT × 1.726 in yaw. The computation is written exactly that way: `aero/yaw.py` computes the yaw moment as 2·T times the semi-span and prints the pitch moment beside it as `2 * T * 0.71`; `aero/thrust.py` sets `KOL = 0.71`, the frame post length.
- Measured either way, the ratio is 2.43: half-distances 1.726 / 0.71, or full separations 3.453 / 1.42.
- DeepSeek's 1.22 takes the full separation for pitch but the half-span for yaw.
- **I read the sentence as correct.** DeepSeek, please answer. The others, please confirm or not.

---

## B. The whole: what I ask you to read

**Defects only, as before.** A change needs one of these:
1. false given the rest;
2. pointer not delivering;
3. §0 boundary unheld or claim strengthened;
4. stale number;
5. contradiction;
6. not understandable in one reading.

**No shortening.** At most three defects per reader.

**Lenses:**
- Grok: B3.
- ChatGPT: B1 and B2.
- DeepSeek: B4.
- Qwen: B2.

**Everyone reads everything.**

### B1. Every sentence that points to another section, with my reading of what the receiver delivers

- There are 82 of them, plus one pointer without a section number (row 0).
- R1 means the receiver delivers what the sentence promises. R2 means it delivers, but in different words or a different form. R4 means the sender says more than the receiver holds.
- **My readings are check output for you to test, not votes.** The one I read as a candidate defect is **row 0**. It was noted in Round 189.

| # | From → to | Sentence (bold removed) | Claude's reading |
|---:|---|---|---|
| 0 | 2.2 → (6.1, no number) | An architecture that rotates its whole body still turns its thrust axis through ninety degrees relative to the flight path, with the moments and the control through the turn that implies; that is not one of the three charges, and it is priced where the transition is analysed. | **R4?** 6.1's transition analyses and bounds: a model altitude loss of 5.4 to 6.6 m with the aerodynamic moment set to zero, and *"Whether a real aircraft loses 5.4 to 6.6 m, more, or less is not settled by anything here."* Nothing prices *"the moments and the control through the turn"*; Section 3 says no control allocation has been closed. The preceding sentence (*"Rotating the airframe is permitted and is not priced here."*) is protected; this one is not. Candidate fix: *"…that is not one of the three charges, and Section 6.1 analyses the transition without pricing it."* |
| 1 | 1 → 5.1 | This paper does not dispute that they work. They take two routes between the regimes: lift-plus-cruise aircraft keep two sets of hardware and switch between them, and tilting aircraft keep one set and reorient it (Section 5.1). | R1 |
| 2 | 1 → 5.1,5.2 | The reaction-torque channel that other coaxial tail-sitters use about that axis is a choice this configuration declines rather than a limit it inherits (Sections 5.1 and 5.2). | R1 |
| 3 | 1 → 5.1 | None of the elements is new, and Section 5.1 says so. | R1 |
| 4 | 2.1 → 6.2 | The quantities on the right come from the configuration and from the propulsion operating points, not from the duration of the hover phase. η_h and η_p are not configuration constants, they depend on the propeller and on the condition it is run at, and Section 6.2 computes what happens when one fixed-pitch blade has to supply both. | R1 |
| 5 | 2.1 → 6.3 | Whether a change of size moves them together, which would make them one quantity under three names, is tested in Section 6.3. | R1 |
| 6 | 2.1 → 6.4 | The accounting also makes a prediction that can be checked without settling the architectural question at all: where an arrangement pays one charge heavily in order to escape another, its ranking against a differently-balanced arrangement will move when the sizing rule changes — toward the lighter arrangement as the rule weights mass more — and will reverse where that reweighting carries it past the point at which the two break even. Section 6.4 tests both the movement and the reversal on this configuration, and Section 2.3 tests a different consequence against a sizing study this work did not produce. | R1 |
| 7 | 2.2 → 6.2 | The condition permits that cost and does not measure it. Section 6.2 does. | R1 |
| 8 | 2.2 → 3 | The tip frames of Section 3 are landing gear because the aircraft stands on its tail: their mass is charged in the build-up and their drag in the ledger. | R1 |
| 9 | 3 → 2.1 | Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency, where a runway-launched aeroplane that never bought vertical capability pays none of the charges of Section 2.1 and is the better machine. | R1 |
| 10 | 3 → 5.2 | One structure serves four purposes and is charged to the mass budget once — Section 5.2 gives the fairing's sizing. | R1 |
| 11 | 3 → 5.2 | The 50 kg reference geometry (Section 5.2) is one point on that trade; an operator with a stronger ground-wind requirement can take another. | R1 |
| 12 | 3 → 7 | Sized. The vertical phase is sized: hover power from momentum theory at thrust equal to weight, the buffer that supplies what the engine cannot deliver of that peak (at a specific power Section 7 examines), the tip-frame lengths that set both the stance base and the control arms, and the structure that carries the landing loads. | R1 |
| 13 | 3 → 6.1 | Section 6.1 reports whether they close. | R1 |
| 14 | 3 → 5.2 | This configuration also declines the reaction-torque channel that comparable aircraft use about the body's longitudinal axis (Section 5.2). | R1 |
| 15 | 3 → 6.2 | The tip frames that make the aircraft self-supporting are structure standing in the cruise airstream, and Section 6.2 charges their drag. | R1 |
| 16 | 3 → 6.2 | The tip pairs they carry are exposed for the whole cruise and cannot be feathered, and Section 6.2 charges that too. | R1 |
| 17 | 3 → 5.1 | The second half — cruise carried on a wing rather than on rotors — is the subject of the next section, and the two are combined in Section 5.1. | R1 |
| 18 | 4 → 3 | Section 3 established the first half: the aircraft must leave from and return to a site that supplies nothing. | R1 |
| 19 | 4 → 2.3 | The sizing set of Section 2.3 reports an effective lift-to-drag ratio, `L/De = WV/P`: a system figure of merit that already contains the propulsive efficiency of whatever produces the thrust, so a force ratio cannot be placed beside it. In level cruise, with shaft power `P = DV/η_p`, | R1 |
| 20 | 4 → 5.2 | The aerodynamic ratio is 8.79 to 10.82, with the tip frames and the free-wheeling tip-pair rotors (Section 5.2) already charged; that spread is uncertainty, the zero-lift drag bracket. | R1 |
| 21 | 4 → 6.1 | Section 6.1 carries one blade into a closed sizing loop; until then no corner is presented as the aircraft's performance. | R1 |
| 22 | 4 → 2.1,2.3 | That higher gross weight is consistent with the mass charge Section 2.1 describes; this table alone does not establish the causal link, and Section 2.3 sets out the independent evidence for it. | R1 |
| 23 | 4 → 6.2 | Whether a variable-pitch hub would recover that difference is not computed; Section 6.2 reports the gap and declines to attribute all of it to the hub. | R1 |
| 24 | 4 → 6.1 | The analysis chains are not matched, and this is the qualification that bounds what the comparison can be called. The published value comes from a fully sized vehicle in an integrated design system; the value here is a converted metric at a prescribed cruise condition, taken before the sizing closure of Section 6.1. | R1 |
| 25 | 4 → 5.1,6.1 | That is a statement about these methods on this class of configuration, not about what any method could achieve; it does not touch the cruise numbers above, which sit at a few degrees, but it bounds what this section may be read to support, and the transition of Sections 5.1 and 6.1 passes through that band. | R1 |
| 26 | 4 → 6.2 | Section 6.2 charges the third. | R1 |
| 27 | 4 → 6.1 | The first two are inside Section 6.1's closed numbers but are not separated out as charges, and the wing's exposure to ground wind is not priced in this work. | R1 |
| 28 | 4 → 5.1 | Section 5.1 is where they are combined, and the combination is what this paper is for. | R1 |
| 29 | 5.1 → 1 | Each can be found on its own, and some of them together, in the literature and in hardware — Section 1 says where. | R1 |
| 30 | 5.1 → 1 | The principle behind the third element — a continuous plant sized for cruise, with the vertical or take-off peak drawn from a store — has been applied in studies of a winged tail-sitter (Section 1) and of a single-aisle airliner reported in 2016 whose turbines are *"sized for efficient operation during"* cruise and assisted by electric motors *"during takeoff and climb."* | R1 |
| 31 | 5.1 → 2.2 | What this paper contributes is the architecture that brings the three elements together; the condition shows what it satisfies, and the price shows what it costs. The three elements, taken together, meet the escape condition of Section 2.2 in the propulsor that carries the aircraft, and they meet it with no mechanism that reorients a propulsor. | R1 |
| 32 | 5.1 → 2.2,6.2 | The instantiation is therefore partial, the case Section 2.2 lists among the ways to fail, and reporting what the failing part costs is a substantial share of what Section 6.2 does. | R1 |
| 33 | 5.1 → 2.3 | The lift-plus-cruise design of the NASA study used in Section 2.3 carries its lifting rotors through cruise, stopped and aligned with the stream, and flies on a separate pusher; its tilt-wing turns eight proprotors, each on its own motor, on a tilting wing and tail. | R1 |
| 34 | 5.1 → 3 | The tip pairs are sized from the moment requirement, but because the nose pair is sized at thrust equal to weight and no more, they also supply the whole take-off margin; that dependency is reported in Section 3, and it does not make them a dedicated lift system. | R1 |
| 35 | 5.1 → 4,6.1 | Whether this aircraft can actually perform the change is a separate question and is not settled anywhere in this paper: the aerodynamics of the rotation are not predicted reliably here (Sections 4 and 6.1). | R1 |
| 36 | 5.1 → 8 | The transition claim is not made. Section 8 holds the paper to that. | R1 |
| 37 | 5.2 → 6.1 | The separation the architecture depends on is that the continuous cruise requirement is several times smaller than the hover peak, and that the difference is supplied from a battery buffer for the vertical phase alone. No wattage is quoted here; the closed powers are Section 6.1's. | R1 |
| 38 | 5.2 → 6.1 | The same differential-thrust system is what is assigned to rotate the airframe through transition. That is a design assignment, not a demonstrated result (Section 5.1): the moment it produces is a sizing input to Section 6.1, and whether it suffices is not settled in this paper. | R1 |
| 39 | 5.2 → 1 | Roll comes from neither, and the reason is a choice rather than an impossibility. No combination of thrust settings produces a moment about the body axis, and the reaction-torque channel that could (Section 1) is declined: every pair is operated torque-balanced. | R1 |
| 40 | 5.2 → 3 | The aircraft rests on the five points of Section 3. | R1 |
| 41 | 5.2 → 2.2 | The tip pairs are the parts that fail the escape condition (Section 5.1): sized for moments and used for them in both regimes, they add the take-off margin but were not sized for weight support, and Section 2.2's permitted-cost clause places them outside the first charge while leaving them in the airstream. | R1 |
| 42 | 5.2 → 6.2 | This configuration uses the first: free-wheeling at zero shaft torque is the tip pairs' uncommanded cruise state and the drag state Section 6.2 charges; the shaft power of commanded departures from it, for attitude moments in cruise, is not computed. | R1 |
| 43 | 6.1 → 5.1,5.2 | This section prices the arrangement of Sections 5.1 and 5.2 on a declared package; it does not bear on the count of mechanism classes, which rests on the inventory of those sections alone. | R1 |
| 44 | 6.1 → 5.2 | These are the same configuration at four closed masses rather than four configurations, with anything that depends on the control moment arms carried at the reference geometry of Section 5.2. | R1 |
| 45 | 6.1 → 4 | A prediction would need the aerodynamic pitching moment, and the methods used here diverge in the band the rotation passes through (Section 4); with a borrowed moment some models complete the rotation, some saturate the tip pairs, and some tumble. | R1 |
| 46 | 6.1 → 7 | It does not establish that the package exists. The energy store this closure assumes is the item Section 7 examines, and the examination does not end well. | R1 |
| 47 | 6.1 → 4 | These ranges are carried forward as closed-loop values, not as a ranking: no rotorcraft is sized in this work, so no range comparison is made against one (Section 4 compares cruise efficiency), and the comparison with the other hybrids depends on the sizing contract (Section 6.4). | R1 |
| 48 | 6.2 → 2.1 | This section says where each charge of Section 2.1 appears inside the closed numbers of Section 6.1, and how large it is there. | R1 |
| 49 | 6.2 → 5.1 | No stopped-state counterfactual was computed: the eight tip discs stopped edge-on are estimated at ΔC_D0 = 0.0008 (Supplement S11), but that takes an indexing mechanism, a class Section 5.1 counts, which has not been sized, charged or closed. | R1 |
| 50 | 6.2 → 2.1 | Rotor–structure and rotor–wing interference is not modelled and is not carried as a line. Section 2.1 quotes a wind-tunnel finding that a simulation neglecting it predicted higher lift and lower drag than were measured; this build-up is such a calculation, and the bracket's upper margin is the only provision made for it. | R1 |
| 51 | 6.2 → 2.1,2.2 | There is no dedicated lift group to charge. What Bill 1 becomes here is the energy buffer: 3.6 percent of take-off mass, 1.9 to 2.1 kg across the four closures. The buffer is not lift-subsystem mass, so it is not Bill 1 as Section 2.1 defines it, but it is carried for the whole flight to serve a demand that lasts about two percent of it: the architecture converts a power-system charge into a cost in kilograms, as Section 2.2 said in advance it would. | R1 |
| 52 | 6.2 → 7 | The engine is sized by cruise, 3.54 to 5.17 kW of shaft rating, against a hover requirement of 11.4 to 12.5 kW at the rotor shaft: a ratio of installed hardware of 2.4 to 3.2, which is not the buffer's burden (Section 7 computes that). | R1 |
| 53 | 6.3 → 2.2 | Whether it is separable from Bill 3 here is not established; that the two are coupled here is Section 2.2's claim, and coupling is not identity. | R2 — the store-for-power trade is named in 2.2's first permitted cost (*"A store is permitted … whether the store is lighter than the continuous power it displaces is computed"*); the word *coupling* is 2.1's subsection title |
| 54 | 6.3 → 2.1 | The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low Reynolds number. It is consistent with the separability Section 2.1 asserts; it is not a verification of separability as a general property. | R2 — 2.1 says the charges are *"three distinct accounting quantities … not assumed to be independent physical causes"*; *"asserts separability"* reads that as separability of accounts, which is what 6.3 tests |
| 55 | 6.4 → 2.1,5.1 | The lift-plus-cruise layout carries a lift-to-drag ratio transferred from a different airframe's wind-tunnel campaign (Section 2.1), and its stopped lift rotors take an indexing mechanism (Section 5.1) whose mass is not charged. | R2 — 2.1 introduces the wind-tunnel characterisation of a quadplane but gives no L/D; the transfer is described in S13 |
| 56 | 6.4 → 2.1 | #### Section 2.1's prediction, tested | R1 |
| 57 | 6.4 → 2.1 | Section 2.1 predicted that such a ranking will move when the sizing rule changes, and can reverse. | R2 — 2.1 says the ranking *"will reverse where that reweighting carries it past the point at which the two break even"*; *"can reverse"* is that condition compressed |
| 58 | 7 → 6.1 | Section 6.1 closed the sizing loop on a declared package and said that whether an aircraft can be built to it is a different question. | R1 |
| 59 | 7 → 6.1,3 | Every closure in Section 6.1 carries a buffer of 3.6 percent of take-off mass. Taken at the electrical bus, the four closures ask the buffer for 4.7 to 5.2 kW per kilogram of buffer to hover, and 5.5 to 6.1 kW per kilogram of buffer to leave the ground with the tip pairs at full thrust (Section 3). | R1 |
| 60 | 7 → 2.1 | The study argues that, because pulse current limits can exceed continuous ones — by more than a factor of two in one commercial module it cites — a pack with the required specific power may be possible with existing technology; its hover lasts twenty seconds or less, while this aircraft's vertical phases occupy about a minute in all (Section 2.1), and how long each draws the peak is not computed here. | R1 |
| 61 | 7 → 6.1 | The gap is real on every one of them; the factor quoted is peak demand against bench average. The package Section 6.1 closes on does not exist with any store the sources consulted here report as built; closed again at the bench rate, it becomes 76 to 81 percent heavier, a sensitivity with one input changed rather than a structural closure (Supplement S14). | R1 |
| 62 | 7 → 2.2 | This is where the coupling Section 2.2 names is paid: the buffer converts kilowatts of hover peak into kilograms of store. | R2 — as 53 |
| 63 | 7 → 2.2 | The escape from Bill 3 is real in the sense Section 2.2 defined it, and its price depends on a component whose required performance has not been demonstrated. | R1 |
| 64 | 7 → 6.1 | It reaches every number that describes this aircraft at Section 6.1's masses: the closed masses of 52.3 to 57.5 kg and the 13 kg payload assume the store. | R1 |
| 65 | 7 → 3,6.4 | The vertical phase that Section 3 reports as sized was sized with this store in it, and Section 6.4's orderings were computed with the store held common at 3.6 percent; how they would move with a measured store is not computed. | R1 |
| 66 | 7 → 4 | Nor does it reach the cruise-efficiency comparison of Section 4 as a ratio: effective lift-to-drag ratio has no mass in it. | R1 |
| 67 | 7 → 6.1 | As a comparison of aircraft, that section describes the configuration at Section 6.1's masses, which the store does reach. | R1 |
| 68 | 8 → 7,7 | It is not a list of the study's open questions. Those are in Section 7, and the difference matters: the boundary below is about claims the paper declines to make, most of which it could not make on any evidence; Section 7 is about questions the paper does not answer, and which better evidence would answer. | R1 |
| 69 | 8 → 4,3,7 | The *size* of the resulting advantage is a calculation, not a consequence of that fact: positive throughout against one published quadrotor, and from slightly behind to comfortably ahead against the other (Section 4). \| \| Operation without a runway \| Fixed-wing aircraft \| Claimed as sized, not demonstrated (Sections 3, 7). | R1 |
| 70 | 8 → 5.1 | The vertical phase was sized with an energy store whose required performance the sources consulted here do not report as built. \| \| The mechanism required to change regime \| Tilting architectures \| Claimed. This is the paper's contribution — a count of mechanism classes (Section 5.1), not a claim of mechanical simplicity or reliability. \| \| Cruise efficiency and range \| Other hybrids — lift-plus-cruise, tilt \| Not claimed, in either direction. \| | R1 |
| 71 | 8 → 6.4 | The fourth row is the important one, and the reason it is a refusal rather than a result is the paper's own finding in Section 6.4. | R1 |
| 72 | 8 → 7 | Operation without a runway does not depend on the drag bracket, the propeller efficiency or the transition aerodynamics — but it does depend on the energy store: the vertical phase is sized with one, and Section 7 examines whether it exists. | R1 |
| 73 | 8 → 4 | The size of the cruise-efficiency margin depends on both the drag bracket and the blade family, and Section 4 reports it as a range rather than a number. | R1 |
| 74 | 8 → 5.1,5.2 | The mechanism claim is a statement about what hardware is present, and it is settled by the inventory of Sections 5.1 and 5.2. | R1 |
| 75 | 8 → 5.1 | The separate claim that this aircraft can actually perform the regime change is not settled (Section 5.1). | R1 |
| 76 | 8 → 5.2 | This configuration declines the reaction-torque channel that comparable aircraft use for roll (Section 5.2). | R1 |
| 77 | 8 → 5.1 | The count of mechanism classes in Section 5.1 is not a reliability argument. | R1 |
| 78 | 8 → 2.2 | Section 2.2 names that case as partial instantiation, and the charge it re-opens is reported rather than absorbed. | R1 |
| 79 | 8 → 7 | Section 7 and Supplement S14 list what the paper leaves open. | R1 |
| 80 | 8 → 1 | Nor is the configuration claimed to be without precedent: Section 1 sets out what is already established, including uncrewed tail-sitters, tail-sitters without control surfaces, coaxial contra-rotating tail-sitter propulsion, and blended-wing-body tail-sitters. | R1 |
| 81 | 8 → 5.1,5.2,6.2 | The contribution is the architecture, and the paper presents it as the combination, the consequences of the choices inside it, and the accounting — which is what Sections 5.1 and 5.2 describe and what Section 6.2 prices. | R1 |
| 82 | 8 → 5.1,5.1 | The configuration is arranged to change regime by rotating the airframe rather than the propulsors, and so carries none of the mechanism classes Section 5.1 counts: no pivot, no nacelle or rotor-group actuator, no variable-pitch hub, no dedicated lift rotors, and — while the tip pairs free-wheel or are held by motor torque — no rotor stowing, indexing or stopping mechanism (Section 5.1's note). | R1 |

### B2. Transitions: the last paragraph of each section or subsection, and the first of the next

**T1 — end of 1. The gap → start of 2. The charges, the condition, an independent check / 2.1 The tax**

> **None of the elements is new**, and Section 5.1 says so. Tail-sitting aircraft are seventy years old; blended wing bodies have been a standing subject of transport
> research for more than three decades; series-hybrid propulsion has been flown in a crewed motor glider and designed for small uncrewed aircraft. The route is not claimed to have been waiting to be found. **The contribution is the
> architecture: a configuration arranged to change regime by rotating the airframe rather than its
> propulsors, and so carrying no mechanism that reorients a propulsor.** The combination, the
> consequences of the choices inside it, and an accounting of what they cost are how that contribution
> is presented and priced.

*then:*

> **A claim that one architecture escapes a cost shared by the others is only meaningful if the cost is stated first, in terms that do not presume the escape.** This section states it. It is not a claim about any particular aircraft, and nothing in it is new physics; what it provides is the accounting that the rest of the paper is checked against.

**T2 — end of 2.1 The tax → start of 2.2 The escape condition**

> Whether an architecture can decline the mismatch itself, rather than redistribute its consequences, is a different question, and the next section states the condition it would have to meet.

*then:*

> This section asks what an architecture would have to do in order not to incur the three charges at all. The answer is a **definition**, derived by inverting the table, and it is stated here before any configuration is offered so that the standard is not taken from the thing it will be used to measure.

**T3 — end of 2.2 The escape condition → start of 2.3 An independent quantitative check**

> **An architecture that reorients a propulsor does not satisfy the condition as written**, because the condition requires one orientation relative to the airframe. **Whether such an architecture might avoid the three charges by some other route is a separate question this paper does not settle** — the condition is a definition, not a law, and it can be too narrow without being wrong.

*then:*

> An accounting proposed by the same people who then use it invites one obvious objection: that the charges were chosen because a particular aircraft happens not to pay them. **What follows is not a test of the whole framework.** It checks one falsifiable consequence on one independent data set. The working is in Supplement S4.

**T4 — end of 2.3 An independent quantitative check → start of 3. The first half: operation without a runway**

> The check establishes that one prediction of the accounting holds on data produced elsewhere, for purposes unrelated to this argument. **It does not establish that the accounting is complete**, that the three charges are the only costs an architecture pays, or that avoiding them makes an aircraft better. **It does not establish anything about the configuration this paper proposes**, which has not yet been described, and which is not in the study used here. **An instrument whose first use is to measure the thing its authors are advocating should be shown working on something else first**, and that is why this section comes before the aircraft. **The instrument is now fixed, and it is not modified again.** **Everything that follows is measured with it rather than added to it.**

*then:*

> On this axis the alternative is the fixed-wing aircraft, and the comparison runs one way only.
> **Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency**, where a
> runway-launched aeroplane that never bought vertical capability pays none of the charges of
> Section 2.1 and is the better machine. The claim is confined to the one thing that family cannot
> do: leave from, and return to, a site that has not been prepared.

**T5 — end of 3. The first half: operation without a runway → start of 4. The second half: cruise carried on a wing**

> **The second half — cruise carried on a wing rather than on rotors — is the subject of the next
> section**, and the two are combined in Section 5.1.

*then:*

> On this axis the alternative is the rotorcraft, multirotor and helicopter alike, and as in the previous section the comparison
> runs one way only. **Nothing here is claimed against fixed-wing aircraft.** The claim is
> confined to the one thing the rotorcraft family structurally lacks: **a surface that carries the
> cruise lift.**

**T6 — end of 4. The second half: cruise carried on a wing → start of 5. Combining the solutions / 5.1 The combination**

> **The two halves are now on the table separately. Section 5.1 is where they are combined**, and
> the combination is what this paper is for.

*then:*

> None of the three elements is new. **Each can be found on its own, and some of them
> together, in the literature and in hardware** — Section 1 says where. The principle behind the third element — a continuous plant sized for cruise, with the vertical or take-off peak drawn from a store — has been applied in studies of a winged tail-sitter (Section 1) and of a single-aisle airliner reported in 2016 whose turbines are *"sized for efficient operation during"* cruise and assisted by electric motors *"during takeoff and climb."*

**T7 — end of 5.1 The combination → start of 5.2 What it is made of, and what still moves**

> **Whether this aircraft can actually perform the change is a separate question and is not settled anywhere in this paper**: the aerodynamics of the rotation are not predicted reliably here (Sections 4 and 6.1). **The mechanism claim is about hardware and survives that
> limit. The transition claim is not made.** Section 8 holds the paper to that.

*then:*

> Section 5.1 claimed that a class of mechanism is absent. A claim of that kind is only as good as the inventory behind it, so the inventory is given here in full, including the parts that move.

**T8 — end of 5.2 What it is made of, and what still moves → start of 6. The calculations / 6.1 Analytical closure of the sizing loop**

> **The fixed geometry of the tip pairs leaves two admissible cruise states**: turning at zero shaft torque, or stopped. This
> configuration uses the first: free-wheeling at zero shaft torque is the tip pairs' uncommanded cruise state and the drag state Section 6.2 charges; the shaft power of commanded departures from it, for attitude moments in cruise, is not computed. **The free-wheeling
> state is physically determinate: the rotor settles where net shaft torque is zero. The stopped state is not**: the stop must be
> produced by something — motor holding torque, an electrical brake, a mechanical lock — and a stopped fixed-pitch blade also has an
> azimuth, so the stopped-state drag estimates (Supplement S11) should be read as estimates for an assumed azimuth rather than as the
> state a particular installation would reach. If the stop were a brake or a lock rather than motor holding torque, the count of Section 5.1
> would gain a class.

*then:*

> This section prices the arrangement of Sections 5.1 and 5.2 on a declared package; it does not bear on the count of mechanism classes, which rests on the inventory of those sections alone. **Closing a sizing loop mathematically is not the same thing as closing an aircraft physically.** This section does the first: what it produces is a set of consistent numbers on a declared set of assumptions.

**T9 — end of 6.1 Analytical closure of the sizing loop → start of 6.2 The ledger**

> It establishes that the architecture is arithmetically self-consistent on a declared package, at four corners of that package. **It does not establish that the package exists.** The energy store this closure assumes is the item Section 7 examines, and the examination does not end well. These ranges are carried forward as closed-loop values, not as a ranking: no rotorcraft is sized in this work, so no range comparison is made against one (Section 4 compares cruise efficiency), and the comparison with the other hybrids depends on the sizing contract (Section 6.4).

*then:*

> This section says where each charge of Section 2.1 appears inside the closed numbers of Section 6.1, and how large it is there.
> **It attributes. It does not add.** **And there is no single figure for what the architecture costs**: the charges are in three currencies, and **no
> scalar aggregate is defined, because this study has no defensible weighting between them** (Section 6.4).

**T10 — end of 6.2 The ledger → start of 6.3 Scale does not lock two of the charges together; the third is not tested**

> Section 6.1's convergence does not cover the cost of declining the reaction-torque channel, the sizing of the strip's actuation, the allocation of the take-off margin against attitude authority, the landing transition, the vortex ring state, closed-loop attitude control in hover and in cruise, engine installation, or rotor–structure and rotor–wing interference; **none of these is a ledger entry, and Supplement S14 lists them.** **The first and the last are the two that would most change the numbers above if they were computed.**

*then:*

> Section 6.2 decomposed the three charges on one aircraft, at one size; **this section asks whether they are three quantities or
> one quantity under three names**, by changing the size of the aircraft and seeing whether they move together. **The test is deliberately weak**: it can show that two charges are not locked together within this
> model; **it cannot show that they are independent in general.**

**T11 — end of 6.3 Scale does not lock two of the charges together; the third is not tested → start of 6.4 Rankings belong to contracts**

> **Because at least two of the charges are not locked together, a comparison of architectures cannot in general be reduced to a number
> that does not depend on how the charges are weighed.** Section 6.4 examines what the choice of sizing contract does to a ranking, on the
> light closures of Section 6.1 only.

*then:*

> Where one architecture pays less of one charge and more of another, the ranking depends on how the charges are weighed
> (Section 6.3), and **a sizing contract is one such weighing**: it fixes what is held equal between the architectures being compared.
> This section applies three contracts to three architectures at each of the four closures of Section 6.1. **The mechanism claim is not a
> ranking and is not at stake here.**

**T12 — end of 6.4 Rankings belong to contracts → start of 7. What does not close**

> **The competitors are modelled at a coarser level than this configuration**: their drag is transferred or idealised, their propeller efficiency assumed and their architecture-specific mass a parameter. **Comparing computed figures against assumed ones favours whichever is assumed more optimistically** — in propeller efficiency both competitors, and with a common propeller efficiency the lift-plus-cruise lead under the first contract falls from 55–84 to 33–45 percent (Supplement S13); in drag the tilting layout, by assumption. **The comparison is at one size**: Section 6.3's 1 000 kg reference design has no closure, and none of its figures is used here. **And nothing here ranks architectures for a mission.** What this section establishes is narrower: **the same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property of the architectures alone.

*then:*

> Section 6.1 closed the sizing loop on a declared package and said that whether an aircraft can be built to it is a different question. **This section is where that question is answered, and for the first item the answer is no: the required store performance is not demonstrated by the sources consulted here.** It is stated in that order — first the obstacle that is known, then what is not known.

**T13 — end of 7. What does not close → start of 8. Four axes, and where the paper stops**

> **The loop closes; the aircraft is not shown to.** At the energy store the paper can name the gap exactly, in specific power and in take-off mass; everywhere else it can name only what would settle the question. **The architecture claim — that the configuration is arranged to change regime with no mechanism that reorients a propulsor — is a count of hardware, and nothing in this section reaches it.** What this section reaches is the aircraft, and the paper has not claimed the aircraft. The last section returns to the four axes and states what is claimed on each.

*then:*

> This section states the boundary of the paper's claims.

### B3. The §0 map: which sentences hold each boundary

| Boundary | Held in | Held by a U sentence alone? |
|---|---|---|
| No range or cruise-efficiency claim against fixed-wing aircraft | 3.1 (*"Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency …"*), 4.1 (*"Nothing here is claimed against fixed-wing aircraft."*), 8.5 item 1 (*"It does not claim range against fixed-wing aircraft."*, protected) | no |
| No vertical-capability claim against rotorcraft | 4.2 (*"A rotorcraft meets that requirement completely."*), 8.5 item 2 (*"… vertical capability against rotorcraft."*, protected) | no |
| Range / cruise efficiency: against multirotors bounded, against helicopters mixed | 4.5 (the two quadrotor rows; *"against them the result is mixed"*), 8.2 table (*"Claimed against multirotors, and bounded; against helicopters … mixed and no advantage is claimed."*, protected) | no |
| No range claim against the other hybrids | 1.2 (*"This paper does not dispute that they work."*), 6.1 (*"… the comparison with the other hybrids depends on the sizing contract (Section 6.4)"*), 6.4 (the contract results and the tilt bound *"a size, not an order"*), 8.2 fourth row and *"No range claim is made against the tilting or lift-plus-cruise families in either direction."* (protected) | no |
| Mechanism count, not *"nothing moves"*, not simplicity or reliability | 5.1 (*"This is not a configuration in which nothing moves."*, *"Nor is this a claim of mechanical simplicity."*, both protected), 5.2 *"What moves"*, 8.5 items 3–4 (protected), 8.6 (*"This is a count of mechanism classes, not a claim that nothing moves, and not a claim of mechanical simplicity or reliability"*, protected) | no |
| No transition or flight claim | 2.2 (*"… not a claim that anything satisfying it would fly …"*), 5.1 (*"The transition claim is not made."*, protected), 6.1 transition (*"Whether a real aircraft loses 5.4 to 6.6 m, more, or less is not settled by anything here."*), 8.5 item 8 (*"It does not claim that the aircraft flies."*, protected) | no |
| Priority in the *"established / not found"* form | 1.4 (every item *"… is established"*), 1.5 (*"What is not established is the combination taken together with its price."*, protected; *"The route is not claimed to have been waiting to be found."*, protected), 5.1 (*"The assembly is not offered as novel because it is an assembly."*, protected), 8.6 (*"Nor is the configuration claimed to be without precedent"*) | no |
| Range is not the thesis; the store is not demonstrated | 7 (*"for the first item the answer is no"*, protected), 7 *"What the obstacle reaches"* (the 927 to 1 233 km *"survive the re-closure only because the fuel fraction is held"*, protected), 8.3 (*"… but it does depend on the energy store"*) | no |

**None of the §0 boundaries rests on a U sentence alone.** The fourteen U sentences qualify local results. Please test this claim: name any boundary you think is held more thinly than the table shows.

### B4. Headline numbers and the qualification beside each

| Number | Where | Its qualification, in the same paragraph |
|---|---|---|
| L/De 5.56–7.39 (best family 6.00–7.39) | 4.4 | *"These are the bounding corners of a product, not four simulated aircraft."* · *"until then no corner is presented as the aircraft's performance"* |
| +13 % … +51 % and −4 % … +27 % against the two quadrotors | 4.5 | *"that result is reported as a result rather than as a caveat"* · the five qualifications of 4.6, the last: *"not a controlled numerical reproduction"* |
| helicopters 5.4–7.2, mixed | 4.5 | *"The qualifications below apply to them too."* |
| 1.2 % better, 9.4 % lighter | 2.3 | *"it is not a controlled experiment"* · *"The framework does not predict any of these numbers"* |
| ranges 927–1 233 km | 6.1 table | 6.1: *"carried forward as closed-loop values, not as a ranking"*; 7: *"survive the re-closure only because the fuel fraction is held"* |
| tip hardware 69 % / 57 % of zero-lift drag; rotor term 0.0154 | 6.2 | *"The rotor line rests on section drag at low Reynolds number"* |
| η_p 14.6 % / 21.0 % below 0.80 | 6.2 | *"The ledger does not attribute the whole of that gap to the absence of variable pitch"* |
| installed-hardware ratio 2.4–3.2 | 6.2 | *"which is not the buffer's burden (Section 7 computes that)"* · *"But the full hover power passes through the electrical path"* |
| Bill 2 rotor term falls to 0.29–0.65 | 6.3 | *"The evidence is one pair of design points, computed by one method …"* (U) · *"it is not a verification of separability as a general property"* |
| 55–84 % / 28–54 % / −13 … +7 % | 6.4 | contract identity; *"with a common propeller efficiency the lift-plus-cruise lead under the first contract falls from 55–84 to 33–45 percent"* · *"The comparison is at one size"* |
| tilt bound 93–141 % | 6.4 | *"What the bound gives is a size, not an order."* · *"how much of it they fill is not computed"* |
| 4.7–5.2 kW per kg of buffer | 7 | not demonstrated by the sources consulted · *"the factor quoted is peak demand against bench average"* |
| 76–81 % heavier | 7 | *"a sensitivity with one input changed rather than a structural closure"* |
| 5.4–6.6 m altitude loss | 6.1 | *"with the aerodynamic pitching moment set to exactly zero"* · *"Whether a real aircraft loses 5.4 to 6.6 m, more, or less is not settled by anything here."* |

---

## C. What I ask of you

| # | Item |
|---|---|
| a | **D3:** DeepSeek, answer my check. Everyone else: confirm the sentence is correct, or show why not |
| b | **Up to three defects in the whole** (B1–B4), in the usual format: where · the sentence, quoted · type (1–6) · the fix in full, or *"to the author"* if protected. Or *"none"*. **Row 0 of B1 in particular:** is it a defect, and is the candidate fix right? |
| c | **Your lens:** one line |
| d | **Your own proposals** (open; no shortening) |

---

## D. What comes next

- **Round 191:** D1 and D2, plus every whole-read defect all five of us agree, applied and shown before and after. Then your confirmation, and **the last reading closes.**
- **Then submission.** The journal's length and figure instructions are needed; the author has been asked for the PDF.

---

## E. Errors (one list)

- **None settled this round.** D3 is under check; if my reading holds, it goes here next round as DeepSeek's.
- **Grok's Round 188 K on D1**, withdrawn in Round 189 by Grok itself.
