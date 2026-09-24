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

---

## S3. The departures as a table (from Section 3)

| Departure | What it costs |
|---|---|
| **Different hardware** | Bills 1 and 2. The unused set is carried for the whole flight and, if exposed, drags. |
| **Same hardware, but it serves only one duty** | Bills 1 and 2 again. A propulsor that lifts and is then carried is a dedicated lift group under another name, whatever it shares with the cruise system. |
| **Same hardware, both duties, different orientation** | The tilting family. **Bill 3 is left standing unless a store supplies the hover peak**, and the mechanism that changes the orientation is itself mass, complexity and a control problem through the turn. |
| **Same hardware, both duties, one orientation, different sizing point** | Bill 3 — unless the hover peak is supplied from somewhere other than the continuously installed power. |

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
