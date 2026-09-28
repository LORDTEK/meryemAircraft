# Bulgu haritası (A evresi, Tur 153; yazar onayı Tur 153) — `paper/build/v8_finding_map.py` adayları + Claude okuması

### K-1 — The four axes and their opponents

**Home:** 6.2 (the table) · **First met:** Section 3 · **Home complete if the others shrink:** yes

| Section | Sentence (verbatim) | Protected | Function | Treatment | Note |
|---|---|---|---|---|---|
| 3 | On this axis the alternative is the fixed-wing aircraft, and the comparison runs one way only. |  | argument | **K** | sets the first half's opponent where the half is argued |
| 3 | Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency, where a runway-launched aeroplane that never bought vertical capability pays none of the charges of Section 2.1 and is the better machine. | yes | boundary | **K** |  |
| 4 | On this axis the alternative is the rotorcraft, multirotor and helicopter alike, and as in the previous section the comparison runs one way only. |  | argument | **K** | sets the second half's opponent |
| 4 | Nothing here is claimed against fixed-wing aircraft. The claim is confined to the one thing the rotorcraft family structurally lacks: a surface that carries the cruise lift. | yes | boundary | **K** |  |
| 6.2 | *(The four-axes table of 6.2. Protected; it does not move. Quoted in full in Round 147, §8.)* | yes | boundary | **H** | the four-axes table; does not move |
| 6.2 | It does not claim range against fixed-wing aircraft. |  | boundary | **K** | item in a counted list ("Eight things") |
| 6.2 | It does not claim vertical capability against rotorcraft. That comparison runs the other way. |  | boundary | **K** | item in a counted list |
| 9 | The paper makes its claims on four axes, against four opponents (Section 6), and on each it stops where its evidence stops. |  | boundary | **C** | Section 9 restates the table; Phase D candidate (6.2 + 9) |
| 9 | Cruise efficiency, against rotorcraft — claimed against multirotors, and bounded; mixed against helicopters. Cruise lift is carried on a surface rather than on rotors. |  | boundary | **C** | restates the table's first row |
| 9 | Nothing is claimed against rotorcraft on vertical capability. |  | boundary | **–** | same as 6.2 item 2 |
| 9 | Nothing is claimed against fixed-wing aircraft on range or cruise efficiency. |  | boundary | **–** | same as 6.2 item 1 and Section 3 |

### K-2 — The declined reaction-torque channel, and that its cost is not computed

**Home:** 5.2 (physics); 6.2 (the cost named); 8 (the debt) · **First met:** Section 1 · **Home complete if the others shrink:** yes

| Section | Sentence (verbatim) | Protected | Function | Treatment | Note |
|---|---|---|---|---|---|
| 1 | The reaction-torque channel that other coaxial tail-sitters use about that axis is a choice this configuration declines rather than a limit it inherits (Sections 5.1 and 5.2). | yes | argument | **K** | inherited-difficulty paragraph; pointer to 5.1, 5.2 |
| 1 | And the reaction-torque channel this paper declines is established as a control channel. A coaxial contra-rotating tail-sitter reported in 2012 balances rotor torque *"by the inverse rotating of the two rotors"* and then unbalances it on purpose to steer: its published control scheme assigns *"differential velocity of the two motors"* to yaw in the vertical mode and to roll in the horizontal one. |  | argument | **K** | occupied-ground list: makes 'declining it' a choice |
| 1 | A quadrotor tail-sitter produces a rolling moment from the reaction torque of four independently driven rotors; a coaxial pair can produce one the same way, by running its two rotors at different speeds. |  | argument | **K** | the price of the gap |
| 3 | That gap is wider than it looks, because this configuration declines the reaction-torque channel that comparable aircraft use about the body's longitudinal axis (Section 5.2), leaving that axis to a strip on the lower surface, the only moving aerodynamic surface. |  | consequence | **K** | hover-control consequence |
| 3 | What that refusal costs in authority and in response time is not computed, and Section 8 carries it. | yes | debt | **K** | already a pointer to Section 8 |
| 5.1 | It could be produced by their reaction torque, and this configuration declines that channel by design (Section 5.2), assigning the axis to an aerodynamic device instead. |  | argument | **K** | the narrow claim at the combining step |
| 5.2 | Reaction torque could produce one: each rotor has its own machine, so running the two rotors of a pair at different speeds leaves a net torque about that axis, and the tail-sitter literature uses exactly that channel. |  | definition | **H** |  |
| 5.2 | This configuration declines it — every pair is operated torque-balanced, so no reaction torque is spent on control — and assigns the axis to an aerodynamic device instead. |  | definition | **H** |  |
| 5.2 | What declining it costs is not counted in this work. | yes | debt | **–** | said in 6.2 with the three cost components, and in 8 |
| 6.2 | This configuration declines the reaction-torque channel that comparable aircraft use for roll (Section 5.2). What that refusal costs — in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia — is not computed anywhere in this paper. The claim is that the mechanism class is eliminated. | yes | boundary | **H** | the only place the cost's three components are named |
| 9 | Roll comes from the strip; the reaction-torque channel the coaxial pairs could provide is declined, and what declining it costs is not computed. |  | boundary | **C** | Section 9; Phase D |

### K-3 — The transition: assigned and analysed, not demonstrated

**Home:** 5.1 (the claim boundary); 7.1 (what was computed); 6.2 item 8 (not claimed) · **First met:** Section 3 · **Home complete if the others shrink:** yes

| Section | Sentence (verbatim) | Protected | Function | Treatment | Note |
|---|---|---|---|---|---|
| 3 | Neither has the landing transition. The forward rotation and the reverse are not symmetric and must not be assumed to be. |  | debt | **K** | Section 3's not-demonstrated list |
| 5.1 | Whether this aircraft can actually perform the change is a separate question and is not settled anywhere in this paper: whether the moment available is sufficient, and whether the aircraft trims through the rotation, depend on aerodynamics that — for the methods used here and the published comparisons against which they were checked — are not reliable above roughly ten degrees of incidence, which is inside the band the rotation passes through. The mechanism claim is about hardware and survives that limit. The transition claim is not made. | yes | boundary | **H** | the mechanism/transition split |
| 5.2 | The same differential-thrust system is what is assigned to rotate the airframe through transition. That is a design assignment, not a demonstrated result (Section 5.1): the moment it produces is a sizing input to Section 7.1, and whether it suffices and whether the aircraft trims through the rotation are not settled in this paper. | yes | definition | **K** | the hardware assignment |
| 6.2 | The last of these carries a distinction that matters more than the others. The mechanism claim is a statement about what hardware is present, and it is settled by the inventory of Sections 5.1 and 5.2. The separate claim that this aircraft can actually perform the regime change is not settled (Section 5.1). | yes | boundary | **C** | restates 5.1 inside 6.2, next to item 8 |
| 6.2 | It does not claim that the aircraft flies. The design *sizes* vertical operation and the transition; it does not demonstrate either. | yes | boundary | **H** |  |
| 7.1 | The sizing above says nothing about whether the aircraft can change regime. |  | definition | **H** | the computation |
| 7.3 | The transition is where the square–cube relation is paid in full: rotating the heavy design in the light design's two seconds would demand about 220 kW from the tip pairs, roughly the whole of hover power; at its own 5.1 seconds the demand is about 13 kW. |  | consequence | **K** | scale |
| 9 | This is a count of mechanism classes, not a claim that nothing moves, and not a claim of mechanical simplicity or reliability. Whether this aircraft completes the rotation is a separate question, and it is not settled here. | yes | boundary | **C** | Section 9; Phase D |

### K-4 — Partial instantiation: the tip pairs fail the condition

**Home:** 2.2 (definition); 5.1 (the case) · **First met:** Section 2.2 · **Home complete if the others shrink:** yes

| Section | Sentence (verbatim) | Protected | Function | Treatment | Note |
|---|---|---|---|---|---|
| 2.2 | It satisfies the first three only in part — for instance in its primary propulsor while a secondary set fails them — in which case the instantiation is partial, and the part that fails re-opens the charge it fails. |  | definition | **H** |  |
| 5.1 | The qualification "in the propulsor that carries the aircraft" is not decoration. Section 2.2 lists partial instantiation among the ways an architecture can fail the condition: meeting it where the aircraft is carried and failing it elsewhere. | yes | argument | **H** | the combining step names the case |
| 5.2 | The tip pairs are the parts that fail the escape condition. The nose pair meets all four parts of Section 2.2. | yes | argument | **C** | 5.2 repeats 5.1's case; keep one sentence and the parenthesis on sizing |
| 5.2 | This is the partial instantiation Section 2.2 lists as its fourth failure mode — meeting the condition where the aircraft is carried and failing it elsewhere — and the charge it re-opens is the second, carried in Section 7.2. |  | argument | **–** | same function as 5.1 |
| 6.2 | It does not claim that the escape condition is fully instantiated. The condition is met in the propulsor that carries the aircraft and is not met in the attitude system, which is carried through cruise producing moments rather than cruise thrust. |  | boundary | **K** | item in a counted list |

### K-5 — A count of mechanism classes, not mechanical simplicity or reliability

**Home:** 6.2 item 4 · **First met:** Section 5.1 · **Home complete if the others shrink:** yes

| Section | Sentence (verbatim) | Protected | Function | Treatment | Note |
|---|---|---|---|---|---|
| 5.1 | Nor is this a claim of mechanical simplicity. | yes | boundary | **K** | at the table, where a reader would draw the inference |
| 5.1 | Part count, mass, failure modes and maintenance burden were not measured, and nothing in this work supports a statement about reliability. |  | boundary | **C** | same sentence as 6.2 item 4; keep one |
| 6.2 | It does not claim mechanical simplicity. Part count, assembly mass, failure modes and maintenance burden were not measured, and nothing here supports a statement about reliability. |  | boundary | **H** |  |

### K-6 — The methods diverge above about ten degrees of incidence

**Home:** 4 (where the methods are introduced) · **First met:** Section 4 · **Home complete if the others shrink:** yes

| Section | Sentence (verbatim) | Protected | Function | Treatment | Note |
|---|---|---|---|---|---|
| 4 | And for the methods used here, and for the published comparisons against which they were checked, the aerodynamic predictions diverge above roughly ten degrees of incidence: three methods of three fidelities depart at the same place, the highest of them against wind-tunnel measurement. | yes | definition | **H** |  |
| 5.1 | Whether this aircraft can actually perform the change is a separate question and is not settled anywhere in this paper: whether the moment available is sufficient, and whether the aircraft trims through the rotation, depend on aerodynamics that — for the methods used here and the published comparisons against which they were checked — are not reliable above roughly ten degrees of incidence, which is inside the band the rotation passes through. | yes | consequence | **K** | the reason the transition claim is not made (K-3 home) |
| 7.1 | What replaces it is not a prediction: the pitching moment that would make it one exists, but for the methods used here the predictions diverge above roughly ten degrees of incidence, the band the rotation passes through (Section 8). |  | consequence | **K** | the reason the moment is not borrowed |

### K-7 — The buffer: kilograms for kilowatts, and its fraction an input

**Home:** 7.2 (Bill 1); 8 (the obstacle) · **First met:** Section 3 · **Home complete if the others shrink:** yes

| Section | Sentence (verbatim) | Protected | Function | Treatment | Note |
|---|---|---|---|---|---|
| 3 | The buffer that releases the engine from the hover peak is mass carried for the whole flight. |  | consequence | **K** | Section 3's cost list |
| 7.2 | There is no dedicated lift group to charge. What Bill 1 becomes here is the energy buffer: 3.6 percent of take-off mass, 1.9 to 2.1 kg across the four closures. The buffer is not lift-subsystem mass, so it is not Bill 1 as Section 2.1 defines it, but it is carried for the whole flight to serve a demand that lasts about two percent of it: the architecture converts a power-system charge into a cost in kilograms, as Section 2.2 said in advance it would. |  | definition | **H** |  |
| 7.2 | The buffer fraction is an input to the loop, not a result of it. The deficit per kilogram of take-off mass that the buffer covers, taken at the electrical bus, spreads by 12 percent across the four closures while the fraction is held at 3.6 percent (Supplement S11). | yes | definition | **H** |  |
| 7.3 | On this configuration Bill 1 appears as the energy buffer: 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and both of those figures are inputs. A change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction. A buffer sized to the hover deficit at the same specific power would track hover power and engine rating, which are the Bill 3 measures, so that derivation cannot test whether Bill 1 separates. | yes | consequence | **K** | the scale test's own input statement |
| 8 | Every closure in Section 7.1 carries a buffer of 3.6 percent of take-off mass, an input rather than a result (Sections 7.2 and 7.3). |  | debt | **C** | restates 7.2 with a pointer |
| 8 | This is where the coupling Section 7.3 found is paid: the buffer is the conversion the escape condition permits — kilowatts of hover peak paid in kilograms of store. |  | debt | **H** | the obstacle |

### K-8 — Rankings belong to the sizing contract; no range claim against the other hybrids

**Home:** 7.4 (the result); 6.2 (the refusal) · **First met:** Section 2.1 · **Home complete if the others shrink:** yes

| Section | Sentence (verbatim) | Protected | Function | Treatment | Note |
|---|---|---|---|---|---|
| 2.1 | It also makes a prediction that can be checked without settling the architectural question at all: where an arrangement pays one charge heavily in order to escape another, its ranking against a differently-balanced arrangement will move when the sizing rule changes — toward the lighter arrangement as the rule weights mass more — and will reverse where that reweighting carries it past the point at which the two break even, where the mass difference as the contract counts it and the cruise-efficiency difference cancel in the range. Section 7.4 tests both the movement and the reversal on this configuration, and Section 2.3 tests a different consequence against a sizing study this work did not produce. |  | definition | **H** | the prediction; the framework |
| 6.2 | Against lift-plus-cruise the ordering depends on the sizing contract: across the three contracts it moves substantially, and under one of them its sign changes inside the envelope and turns on quantities of the competitor that are assumed rather than measured. |  | boundary | **H** | the refusal |
| 6.2 | Because the comparative result depends on the sizing contract, no comparison in this paper should be quoted without the contract it was computed under. | yes | boundary | **K** |  |
| 7.4 | A statement of which architecture has the longer range, made without its contract, would therefore be a statement about the contract. |  | consequence | **H** |  |
| 9 | Range, against the other hybrids — not claimed, in either direction. The ordering belongs to the sizing contract (Section 7.4). |  | boundary | **C** | Section 9; Phase D |

### K-9 — The fixed-pitch compromise; no variable-pitch counterfactual

**Home:** 7.2 · **First met:** Section 1 · **Home complete if the others shrink:** yes

| Section | Sentence (verbatim) | Protected | Function | Treatment | Note |
|---|---|---|---|---|---|
| 1 | And the propeller compromise at the centre of this paper's own ledger is a known result, not a discovery. The uncrewed tail-sitter literature states it directly: fixed-pitch propellers make it *"theoretically impossible to be very efficient in both hovering and forward flight."* A long-range tail-sitter reported in 2018 that uses a cyclic- and collective-pitch rotor still describes it as *"a compromise between efficient hover and efficient forward flight"* and selects its diameter on that basis; the same paper names variable pitch as the remedy for fixed-pitch propellers, at the cost of extra actuators and the weight of the mechanism. |  | argument | **K** | occupied ground |
| 2.2 | Serving two regimes with one set of hardware has a price of its own. Hardware that is not duplicated cannot be optimised twice: a propeller sized for hover thrust at zero forward speed is not the propeller a cruise design would choose, and if its geometry is fixed the compromise is paid in efficiency. |  | definition | **K** | a permitted cost, defined before the aircraft |
| 4 | It is the cruise efficiency this aircraft's fixed-pitch blade delivers: at a propeller efficiency of 0.85 the same airframe reaches 7.47 to 9.20. |  | consequence | **K** | why the second half's margin sits where it does |
| 4 | Whether a variable-pitch hub would recover that difference is not computed; Section 7.2 reports the gap and declines to attribute all of it to the hub. |  | debt | **C** | 7.2 says it |
| 4 | And the fixed-pitch propeller that serves both regimes is the reason the margin above sits where it does rather than higher. |  | consequence | **–** | same as the sentence two rows up |
| 5.1 | A fixed-pitch propeller that serves two regimes pays in efficiency in at least one of them. |  | argument | **C** | 5.1: keep one sentence and the pointer to 7.2 |
| 7.2 | Section 7.1's closures run at a cruise propeller efficiency of 0.632 to 0.683: relative to the 0.80 the reference design's sizing assumed, 14.6 percent lower at the better blade and 21.0 percent lower at the worse. The ledger does not attribute the whole of that gap to the absence of variable pitch. No variable-pitch counterfactual was computed. Nor is the gap decomposed. | yes | definition | **H** |  |
| 7.3 | The fixed-pitch gap also widens slightly with size, to 16.4 to 22.9 percent at the heavy design (Supplement S12); as in Section 7.2, no variable-pitch counterfactual was computed. | yes | consequence | **K** | scale |

### C-10 — The wing carried through hover, and ground wind (DeepSeek)

**Home:** 4 (What this half costs) · **First met:** Section 3 · **Home complete if the others shrink:** yes

| Section | Sentence (verbatim) | Protected | Function | Treatment | Note |
|---|---|---|---|---|---|
| 4 | The wing that makes cruise efficient is carried through the vertical phase, where it produces nothing and presents the aircraft's largest surface to ground wind. |  | consequence | **H** |  |
| 4 | The first two are inside Section 7.1's closed numbers — the wing's mass in the empty fraction, the constrained planform in the computed span efficiency — but neither is separated out as a charge, and the wing's exposure to ground wind is not priced in this work. |  | debt | **K** | same paragraph; says where the cost sits |

### C-11 — The tailless planform and the sweep (DeepSeek)

**Home:** 5.2 · **First met:** Section 4 · **Home complete if the others shrink:** yes

| Section | Sentence (verbatim) | Protected | Function | Treatment | Note |
|---|---|---|---|---|---|
| 4 | The tailless planform that follows from having no boom constrains the sweep, because with no horizontal stabiliser the pitching moment must come from the distribution of lift along the body itself. |  | consequence | **C** | 4 keeps the cost; the reason is 5.2's |
| 5.2 | Sweep is not a free parameter here, and the reason is structural to the configuration rather than aerodynamic preference. |  | definition | **H** |  |

### C-12 — The energy store (DeepSeek)

**Home:** 8 (the obstacle); 7.2 (the conversion); 2.2 (permitted) · **First met:** Section 2.2 · **Home complete if the others shrink:** yes

| Section | Sentence (verbatim) | Protected | Function | Treatment | Note |
|---|---|---|---|---|---|
| 2.2 | A store is permitted, and it has the same duty-cycle character as Bill 1. It is not Bill 1 as Section 2.1 defines it — it is not lift-subsystem mass — but it is mass carried for a duty that is briefly needed, which is the same complaint Bill 1 makes. The condition converts a power-system charge into a cost in kilograms and claims only that the three charges as named are not incurred. |  | definition | **H** |  |
| 6.2 | Operation without a runway does not depend on the drag bracket, the propeller efficiency or the transition aerodynamics — but it does depend on the energy store: the vertical phase is sized with one, and Section 8 examines whether it exists. |  | boundary | **K** | claim dependence |
| 7.1 | It does not establish that the package exists. The energy store this closure assumes is the item Section 8 examines, and the examination does not end well. | yes | debt | **K** | 7.1's own limit, points to 8 |
| 8 | This section is where that question is answered, and for the first item the answer is no: the required store performance is not demonstrated by the sources consulted here. Section 6 called this section a debt: questions the paper does not answer and that better evidence would. | yes | debt | **H** |  |
| 9 | Operation without a runway, against fixed-wing aircraft — claimed as sized, not demonstrated. The vertical phase was sized with an energy store whose required performance the sources consulted here do not report as built (Section 8). | yes | boundary | **C** | Section 9; Phase D |

### C-13 — The strip (DeepSeek)

**Home:** 5.2 (hardware); 5.1 (named at the claim) · **First met:** Section 3 · **Home complete if the others shrink:** yes

| Section | Sentence (verbatim) | Protected | Function | Treatment | Note |
|---|---|---|---|---|---|
| 5.1 | The device is the only moving aerodynamic surface on the aircraft — a variable-extension strip on the lower surface, modulated rather than switched, which also pitches the nose down by a small increment when it is deployed. |  | argument | **H** | named where the elimination is claimed |
| 5.2 | Roll is produced instead by a strip on the lower surface: inclined at 45° in planform, running 120 % of root chord, reaching 67 % of semi-span, and standing 2 cm proud at its inboard end and 6 cm at its outboard end. |  | definition | **H** |  |
| 5.2 | Beyond the propellers' rotation, one thing on this aircraft changes its configuration: the strip. It is specified as deployable in two halves — one side alone for roll, both together as a speed brake. |  | definition | **K** | 5.2's 'What moves' |
| 5.1 | The actuator inventory that replaces them is the propulsion motors together with the strip. |  | argument | **–** | 5.2 says it with the actuator count |
