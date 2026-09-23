# Round 57 — the last section is written, writing it exposed two old contradictions, and this text carries everything the questions touch

> **READ THIS FIRST.** Everything this round asks about is reproduced here, **in full**. **You are not
> being asked to read a manuscript, and you do not need the repository.** v8 is written as separate
> step files; `paper-v6.md` and `paper-v7.md` are frozen historical records. **If your knowledge base
> holds a file whose name contains `makale-v` or `paper-v`, it is not what this round is about.**

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`d39db1c`** — metadata only.

```
paper/v8/15-four-axes.md                     SHA-256 981fa0a7db19c380f968794bce8f0d8a710a54ca03a2890225b664688f2d3cf7
paper/v8/14-what-does-not-close.md           SHA-256 8e7ef193ac501c1d069c4b15375ec84a91bdb551ca1392d5f3ab87e9475b756f
paper/v8/09-what-is-not-claimed.md           SHA-256 a7b355e25792ff6162be4b24d58e4bf8b5a2c30c98ddb819c635632f6899ea18
paper/v8/08-what-it-is-made-of.md            SHA-256 262b8086f39a7b605df2721868399c784be860e7833c65d65501f308e9a3e441
paper/v8/07-the-combination.md               SHA-256 c2203eef22a8308837016b3d0e29f042913957ff5fbecb8afe44b0b1b8b7c77d
paper/v8/06-the-second-half.md               SHA-256 2f78ff0eee7a67748fb9d31db0d329a1d69f0fca77b6052f0a39aadc9bb82459
paper/v8/05-the-first-half.md                SHA-256 e062df8dbde8a336230e8cc722122e43ab991d287ee2fd8eaac42420653ca349
aero/contracts.py                            SHA-256 2b43a66e9476f78d0e8d1ad03a9cc591601fc5ccc0a8addc9d8d6016e01dbb38
aero/baseline.py                             SHA-256 577f9620f39046cbe99c19811260cdf192b7bea1e9933ee389b4d9bde8f86fc2
```

### A note to Qwen, and the reason this text is long

**Qwen**, in the last three rounds several passages you quoted as v8 steps were from the frozen v7 in
your knowledge base: *"the quantity a future measurement must return is ΔC_L for this strip on this
planform"* and *"whether such a fairing develops the side force credited to it is not established"*
(you attributed both to Step 8; neither is in v8 — the first is v7's line 836), and the *"Step 2.9 /
Step 3.4"* power passages (v7's §2.9 and §3.4). **That is not a fault of yours: you did not have the v8
text, and asking you to look it up elsewhere was not a fair instruction.** The author has asked that you
be given the content instead. **So this round reproduces in full every v8 step the questions touch —
Steps 5, 6, 7, 8, 9, 14 and 15 — and the changed passages of the others. Please work only from what is
here.** Next round the author will share all fifteen steps.

**The substance of your two v7 quotes was right**, by the way: the strip and the fairing are computed,
not measured. That went into Step 14's table.

---

## 1. What was done with last round's answers

**All four of you agreed** that the energy-store paragraph was at the right strength and that one
sentence was not: *"At the highest measured rate the aircraft exists."* **Grok** put it most exactly —
*"a loop sensitivity, not a second aircraft."* **Taken**: *"the loop closes"*; *"These masses are the
Section 10 package with one input changed. They are not a structural closure at 100 kg."*

| Point | Who | Done |
|---|---|---|
| The ratings are of different kinds — peak demand, bench average over minutes, continuous, design assumption; the factor is peak-to-bench | Grok, ChatGPT | **Taken**, in the paragraph that carries the factor |
| Say which rule the re-closure holds | DeepSeek | **Taken**: wing loading, disc loading and aspect ratio held, so L/D and range are carried |
| What the store **reaches**: Section 10's masses and payload; the 927–1 233 km ranges survive only because fuel fraction is held; the vertical phase Section 5 reports as sized; Section 13 | Grok, DeepSeek | **Taken** — a new paragraph, *"What the obstacle reaches, and what it does not"* |
| Section 6 is untouched **as a ratio**, not as a comparison of aircraft | Grok | **Taken** |
| Section 11's ledger records the conversion at the assumed store; this is its price at a measured one | DeepSeek | **Taken** |
| Unknowns table: buffer **energy**, not only power | Grok | **Added** — the bench pack emptied in about four minutes at 10.68C |
| Unknowns table: electrical path at peak, and its cooling | ChatGPT | **Added** |
| Unknowns table: the strip and the fairing, measured and actuated | Grok, DeepSeek, Qwen | **Added** |
| Unknowns table: the tip pairs' stopped state (means and azimuth not fixed) | Grok | **Added** |
| Unknowns table: ground handling and landing with lateral velocity | DeepSeek | **Added** |
| Airframe row: analysis, then a built article; and not established at the re-closure masses | DeepSeek | **Taken** |
| *"Measurement"* is too exclusive — *"validated aerodynamic data"* | ChatGPT | **Taken** |
| Station labels on every power in Steps 10–12; the Bill 3 ratio is shaft-to-shaft | Grok, ChatGPT, DeepSeek | **Taken**: *"a ratio of installed hardware rather than a deficit"*; Step 11's *"the buffer supplies the difference"* removed |
| Define *"break even"* in Step 2 | DeepSeek | **Taken** |
| Step 13's *"the common store is the neutral choice"* is only neutral before Step 14; do not reopen 13 | Grok | **One sentence**: *"holding it common charges all three the same assumption"* |

**Declined, with reasons:**

- **DeepSeek: the runway claim does not depend on the store** (*"sized, not demonstrated"*). Partly not:
  the vertical phase *was sized with this store in it*. Step 14 now says so — and writing Step 15 then
  found that Step 9 had said the opposite (Section 4).
- **DeepSeek: 4.19 and 3.98 are "understated"; at a common station they would be about 5.33.** The ratio
  was not wrong but undefined: rotor-shaft hover power over engine shaft rating is a legitimate hardware
  ratio. It is now labelled so, which is ChatGPT's first option.

---

## 2. An error your answers led to — and a figure I sent you last round was wrong

**DeepSeek:** *"If the loop combines rotor-shaft and engine-shaft powers anywhere, it would be inside
`baseline.py`, not in the prose. Worth a one-line audit of the script."*

**Audited; it did.** When a competitor has no buffer, the sizing script rated its engine **equal to the
hover power at the rotor shaft**. But in a series hybrid the engine's output reaches the rotor through
the generator (0.90), the power electronics (0.95) and the machine (0.92), so the engine must be rated
**1.27 times** that. The path is used only by Step 13's case in which the competitors carry no buffer.

**Corrected, that case is sharper than I reported:**

| Competitors without a buffer | Round 56 (wrong station) | Corrected |
|---|---|---|
| Lift-plus-cruise, fixed fuel fraction | closes at 381 kg | **does not close** |
| Lift-plus-cruise, fixed fuel mass | 11–23 % behind | **38–47 % behind** |
| Lift-plus-cruise, fixed take-off mass | does not close | does not close |
| Tilt bound, fixed fuel fraction | — | **closes at 520 kg, about ten times this configuration, range lead unchanged at 103–141 %** |
| Tilt bound, fixed take-off mass | 75–98 % behind or does not close | **does not close** |

**The direction is the same; the magnitude is larger. The "381 kg" in last round's text was wrong.** The
default of the new factor reproduces the published tables unchanged; the numerical audit still passes all
45 checks.

---

## 3. What writing the last section found — two contradictions that had survived several rounds

**Step 15 repeats Step 9's four axes.** Checking each against the step it summarizes found:

1. **Step 9's dependency table said the runway claim *"does not depend on … the battery gap."*** Step 14
   shows the vertical phase was sized with that store, and that with a store that has been built the
   loop closes only for a heavier aircraft, or at one continuous rating not at all. **Step 9 now says the
   runway claim does depend on the energy store.**
2. **Step 6 still said the multirotor margin is compressed by *"this aircraft's own refusal of the
   variable-pitch hub."*** That is the over-attribution **ChatGPT** caught in Step 11 in Round 53 — no
   variable-pitch counterfactual was computed. The repair reached Step 11 and Step 12 and **never reached
   Step 6**; my first draft of Step 15 copied it. Both now say *"the cruise efficiency of the fixed-pitch
   blade"*, and Step 6 adds that whether a hub would recover the difference is not computed.

**Both are mine**, and both are the same failure the project keeps recording: a correction made in one
place that does not reach every place the corrected claim lives. The automatic check for retired phrases
now holds 37 of them.

---

## 4. The proportion pass — no cuts

**The author's instruction this round:** *"Shortening will not be done for now. There will be no
shortening until I am confident. Do the proportion work."*

The question is the one asked in Round 49 and never answered: **for a paper whose single contribution is
the architecture, is the weight in the right places?** Two of the author's decisions constrain the
answer: the innovation is the main flow and is not to be overshadowed, but the calculations stay, in
their right place; and the framework is the tool that makes the claim checkable, **keeping its own steps
(2, 3, 4, 12, 13) at full size.**

| Flow element (the author's outline) | Steps | Words | Share |
|---|---|---:|---:|
| Introduction | 1 | 1 958 | 6.9 % |
| Current state — the framework | 2–4 | 5 924 | 20.8 % |
| One problem solved — runway | 5 | 1 237 | 4.4 % |
| The other problem solved — cruise | 6 | 2 206 | 7.8 % |
| **Combining the solutions** | **7** | **1 355** | **4.8 %** |
| Why the result holds — inventory and boundary | 8–9 | 3 662 | 12.9 % |
| Existing calculations | 10–14 | 12 094 | **42.5 %** |

*(Before Step 14's second writing and Step 15.)*

**What the measurement shows:**

- **The contribution's name arrives late.** The phrase *"no mechanism that reorients a propulsor"* first
  appears **57 % of the way through**, in Step 7. Step 1 states what the paper offers as three things —
  *"the combination, the consequences of the choices inside it, and an accounting"* — not as one.
- **The step the outline marks as the central move is the second shortest.** Length is not importance,
  and Step 7 may be strong because it is short.
- **The calculations are 42.5 % and barely mention the contribution** — the mechanism vocabulary appears
  twice in Steps 10–13 together, against eighteen times in Steps 7 and 9.
- **Step 12 is the longest step (10 %)**, and its findings have narrowed most in these rounds.

**Proposals, none applied except the last section:** **P1** — one sentence at the end of Step 1 naming the
contribution as the architecture, before the existing three-item statement. **P3** — one sentence at the
opening of each of Steps 10–13 saying where that calculation stands relative to the contribution (it
measures the price, not the claim). **P2** — the last section puts the mechanism axis at its centre:
**done.** Growing Step 7 to fix its share is **not** proposed.

---

## 5. The changed passages of Steps 2, 10, 11, 12 and 13, verbatim

**Step 2 — the prediction, with *break even* defined:**

> It also makes a prediction that can be checked without settling the architectural question at
> all: **where an arrangement pays one charge heavily in order to escape another, its ranking
> against a differently-balanced arrangement will move when the sizing rule changes — toward the
> lighter arrangement as the rule weights mass more — and will reverse where that reweighting carries
> it past the point at which the two break even, where the mass difference as the contract counts it and
> the cruise-efficiency difference cancel in the range.** Section 13 tests both the
> movement and the reversal on this configuration, and Section 4 tests a different consequence
> against a sizing study this work did not produce.

**Step 10 — the closure table's power columns, now labelled by station:**

> | | C_D0 | η_p | L/D | MTOW | Empty fraction | Hover power, rotor shaft | Engine rating, shaft | Range |

**Step 11 — Bill 3, with stations:**

> The engine is sized by cruise: **3.54 to 5.17 kW** of shaft rating. The hover requirement is
> **11.4 to 12.5 kW** at the rotor shaft. The ratio between the two is **2.4 to 3.2** — a ratio of
> installed hardware, the factor by which the continuously installed power plant is smaller than the
> peak the rotors must absorb. **It is not the buffer's burden**, which is taken at the electrical bus
> rather than as the difference of these two shaft figures, and which Section 14 computes.

**Step 12 — the Bill 3 ratio, labelled:**

> **The measure Section 11 uses for Bill 3 — rotor-shaft hover power divided by engine shaft rating, a
> ratio of installed hardware rather than a deficit — carries a second quantity, and it does not travel
> as cleanly.**

**Step 13 — the no-buffer case, corrected (Section 2 above):**

> **Holding Bill 3 common is a choice of question, and it has a direction.** It is made so that the
> contract can be seen acting on a mass difference against a cruise-efficiency difference; it is not a
> claim that those families would use this power system, and the tilting family as Section 2 describes
> it has no store at all. **The choice runs against this configuration.** Given no buffer and an engine
> rated to deliver the hover demand through the generator, the power electronics and the machines
> instead, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off
> mass, and under a fixed fuel mass falls 38 to 47 percent behind; the tilt bound does not close under a
> fixed take-off mass. **Under a fixed fuel fraction the tilt bound closes at 520 kg — about ten times
> this configuration's mass — with its range lead unchanged at 103 to 141 percent**: the first
> contract's blindness to mass, made visible. **That comparison is not used**, because it would set
> competitors without a store against this configuration with one — a buffer of 3.6 percent whose
> feasibility is the item Section 14 examines. Whatever that store turns out to cost, holding it common
> charges all three the same assumption.

---

## 6. Step 15, in full (new — the last section)

### Four axes, and where the paper stops

The paper makes claims on four axes, against four different opponents, and on each it stops where its
evidence stops. They are restated here in the order Section 9 gave them, with what each now rests on.

#### Cruise efficiency, against multirotors — claimed, and bounded

**Cruise lift is carried on a surface rather than on rotors**, and no sizing contract or assumption in
this paper moves the configuration out of that state. That is the structural claim, and it stands.
**The size of the advantage is a calculation, not a consequence of it.** Made in one common definition
against two published quadrotors, it is positive throughout against one of them; against the other it
runs from slightly behind to comfortably ahead, depending on the drag outcome and the blade. **What
compresses it is the cruise efficiency of the fixed-pitch blade**, not the wing. The comparison
is between independently produced figures, not a controlled reproduction, and it is not claimed as
more. Nothing is claimed against multirotors on vertical capability, where they are the better machines.

#### Operation without a runway, against fixed-wing aircraft — claimed as sized, not demonstrated

**The aircraft stands on its own tail, carries everything it needs to leave and to return, and asks
the site for nothing but ground.** The structure it stands on is the structure that carries its control
propellers. That is a property of the arrangement. **What is sized rather than shown is that it can do
so at the masses reported**: the vertical phase was sized with an energy store whose required
performance the sources consulted here do not report as built, and with a store that has been built the
sizing loop closes only for a heavier aircraft — and at one of the measured continuous ratings not at
all. **By construction,
in this paper, means by the sizing, never by demonstration.** Nothing is claimed against fixed-wing
aircraft on range or cruise efficiency, where they are the better machines.

#### The mechanism required to change regime, against tilting architectures — the contribution

**The regime change is made by rotating the airframe rather than the propulsors.** The propulsors hold
their orientation relative to the body from take-off to cruise, and so the configuration carries **no
mechanism that reorients a propulsor**: no pivot, no nacelle or rotor-group actuator, no variable-pitch
hub, no dedicated lift rotors, and no rotor stowing, indexing or stopping mechanism. Pitch and yaw come
from differential thrust between fixed-pitch propellers. **Roll does not come from the propellers**: the
configuration declines the reaction-torque channel its coaxial pairs could provide and assigns that
axis to a single moving aerodynamic surface, the strip; what declining the channel costs is not
computed. The actuator inventory is the propulsion motors together with the strip.

**This is a count of mechanism classes, not a claim that nothing moves, and not a claim of mechanical
simplicity or reliability**, none of which was measured. It rests on the inventory of Sections 7 and 8.
It does not rest on the drag bracket, the propeller efficiency, the sizing contract, the energy store,
or the transition aerodynamics. **Whether this aircraft completes the
rotation is a separate question, and it is not settled here**; the arrangement requires no mechanism to
change regime, and the paper does not claim that it has been shown to change regime.

**The escape condition is met where the aircraft is carried and not everywhere.** The nose pair serves
both regimes in one orientation with the hover peak drawn from a store; the attitude pairs are carried
through cruise producing moments rather than thrust, and the drag they add is reported rather than
absorbed.

#### Range, against the other hybrids — not claimed, in either direction

**Against lift-plus-cruise the ordering belongs to the sizing contract.** It moves substantially across
the three contracts examined, and under one of them its sign changes inside the envelope and turns on a
mass fraction of the competitor that has not been measured. **Against the tilting family the competitor
could be modelled here only as a bound that pays no cruise penalty**, and an ordering against a bound is
not a result. A reader who finds a range claim against either family anywhere in this paper should read
it as an error.

#### What holds the four together

**The claims are made through an accounting, and the accounting is what makes them checkable.** Hybrid
vertical-take-off aircraft pay for runway independence in three currencies — hover hardware carried
through cruise, its drag when exposed, and continuous power sized by the hover peak. The currencies are
coupled, and every known partial remedy moves cost between them. An escape condition states what an
architecture would have to do to incur none of the three as named; this configuration meets it in the
propulsor that carries the aircraft and pays the rest, and the ledger reports each charge in its own
currency rather than as one number. **At least two of the charges are not locked together, and so,
where architectures trade one charge against another, a ranking is a weighting and belongs to the
contract that makes it.**

#### Where the paper stops

**The sizing loop closes on a declared package; the aircraft is not shown to close.** The first obstacle
is known and named: the energy store. The rest are listed with what would settle them — the pitching
moment through the transition, section drag at low Reynolds number, the airframe's mass, hover control,
the descent, and the items this work does not contain at all.

What the paper offers, and defends, is narrower than a first reading might take it to be: **a
configuration that combines runway-independent vertical operation with wing-borne cruise efficiency,
reaches that combination with no mechanism that reorients a propulsor, and reports what the combination
costs.**

---

## 7. Step 14, in full (second writing)

### What does not close

Section 10 closed the sizing loop on a declared package and said that whether an aircraft can be
built to it is a different question. **This section is where that question is answered, and for the
first item the answer is no.** Section 9 called this section a debt: questions the paper does not
answer and that better evidence would. It is stated in that order — first the obstacle that is known,
then what is not known.

#### First, the known obstacle: the energy store

**Every closure in Section 10 carries a buffer of 3.6 percent of take-off mass.** That figure is an
input, not a result (Sections 11 and 12). What it implies can be computed. Taken at the electrical bus,
where the buffer sits — the rotor demand divided by the machine and power-electronics efficiencies, less
what the engine delivers through its generator — **the four closures ask the buffer for 4.7 to 5.2 kW
per kilogram to hover, and 5.5 to 6.1 kW per kilogram to leave the ground** with the tip pairs at full
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

#### What the obstacle reaches, and what it does not

**It reaches every number that describes this aircraft at Section 10's masses.** The closed masses of
52 to 58 kg and the 13 kg payload assume the store. The ranges of 927 to 1 233 km survive the
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

#### Then what is not known

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
| **Closed-loop hover control**, including the cost of declining the reaction-torque channel, and the allocation of the tip pairs between take-off margin and attitude authority, which compete for the same propellers. | Whether hover is controllable with the authority computed (Sections 5 and 8) | **Analysis not yet done**: a control-allocation study, then simulation |
| **Vertical descent and the landing transition.** Neither is analysed; the vortex ring state is not assessed, and the landing transition is not the take-off transition run backwards. | Whether the aircraft can come down as it went up (Section 5) | **Analysis not yet done** |
| **Ground handling and landing loads.** The stance base is a parameter against static crosswind (Section 5); the response to a landing with lateral velocity or on uneven ground, and handling between flights, are not assessed. | Operation from unprepared sites | **Analysis not yet done** |
| **The competitor's lift-group mass.** It decides the sign of the fixed-take-off-mass ordering in Section 13. | Section 13's sensitivity, not a claim | **Measured inventories** of lift-plus-cruise aircraft of this class |
| **Engine installation** — bay, intake, exhaust, cooling. | Mass, drag and packaging | **Absent from this work entirely** |
| **Atmosphere.** Every number here is at sea level. | The comparison in Section 6, made against a mission flown at altitude | **Analysis**: the direction of the effect has not been computed |

**None of these is a small correction to a known quantity.** Two of them need validated data rather
than more of the computation already done: the transition moment, because three methods have been
tried against it and disagree, and the low-Reynolds section drag, because the one method used here is
least reliable exactly there. Several — hover control, the descent, the buffer's energy, the electrical
path — are analyses this study has not posed. One — the engine installation — is not in the work at
all.

#### What this section amounts to

**The loop closes; the aircraft is not shown to.** At the energy store the paper can name the gap
exactly, in specific power and in take-off mass. Everywhere else it can name only what would settle the
question. **The architecture claim — that the regime change is made with no mechanism that reorients a
propulsor — is a count of hardware, and nothing in this section reaches it.** What this section reaches
is the aircraft, and the paper has not claimed the aircraft.

The last section returns to the four axes of Section 9 and states what is claimed on each.

---

## 8. Step 9, in full (the four axes Step 15 repeats; one row corrected)

### What is not claimed

This section states the boundary of the paper's claims. It is placed before the configuration's
own numbers because a boundary drawn after the results would be a retreat, and one drawn before
them is a commitment.

**It is not a list of the study's open questions.** Those are in Section 14, and the difference
matters: the boundary below is about claims the paper **declines to make**, most of which it
could not make on any evidence; Section 14 is about questions the paper **does not answer**, and
which better evidence would answer. One is a scope; the other is a debt.

#### The claims are made on four axes, against four different opponents

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

#### What each claim does not depend on

A reader who rejects one of these claims should be able to see immediately which of the others
survive, and the dependencies are short enough to list.

| Claim | Does not depend on |
|---|---|
| Operation without a runway | the drag bracket, the propeller efficiency, the transition aerodynamics — **but it does depend on the energy store**: the vertical phase is sized with one, and Section 14 examines whether it exists |
| Cruise lift carried on a surface | the sizing contract, the transition aerodynamics |
| The **size** of the cruise-efficiency margin | — it depends on both the drag bracket and the blade family, and Section 6 reports it as a range rather than a number |
| Elimination of the propulsor-reorientation mechanism class | the drag bracket, the sizing contract, the range result, **and the transition aerodynamics** |

**The last row carries a distinction that matters more than the others.** The mechanism claim is
a statement about what hardware is present, and it is settled by the inventory in Section 8. **The
separate claim that this aircraft can actually perform the regime change is not settled**, and it
depends on exactly the aerodynamics that Sections 6 and 14 describe as unreliable above roughly
ten degrees of incidence — the band the rotation passes through. **Section 7 should be read under
that limit**: it describes an arrangement that requires no reorienting mechanism, not a
demonstration that the arrangement transitions.

#### One cost of the contribution that is named and not priced

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

#### Eight things this paper does not claim

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

#### What the claims that remain amount to

Removing those eight leaves something narrower than a first reading of the abstract might
suggest, and the narrower statement is the one the paper defends: **a configuration that
combines runway-independent vertical operation with wing-borne cruise efficiency, reaches that
combination with no mechanism that reorients a propulsor, and reports what the combination
costs.**

Each half of that has a named opponent and neither half is a record. **Nor is the configuration
claimed to be without precedent**: Section 1 sets out what is already established, including
uncrewed tail-sitters, tail-sitters without control surfaces, coaxial contra-rotating
tail-sitter propulsion, and blended-wing-body tail-sitters. **What this paper offers is the
combination, the consequences of the choices inside it, and the accounting** — which is what
Sections 7 and 8 describe and what Section 11 prices.

#### One consequence for how the numbers that follow should be read

Because the comparative result depends on the sizing contract, **no comparison in this paper
should be quoted without the contract it was computed under.** That is not a caveat attached for
safety; it is the paper's own finding applied to the paper's own numbers, and Section 13 states
what it demands of anyone who uses the framework afterwards.

---

## 9. Step 5, in full (the runway axis)

### The first half: operation without a runway

#### The opponent, and the axis

On this axis the alternative is the fixed-wing aircraft, and the comparison runs one way only.
**Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency**, where a
runway-launched aeroplane that never bought vertical capability pays none of the charges of
Section 2 and is the better machine. The claim is confined to the one thing that family cannot
do: leave from, and return to, a site that has not been prepared.

#### What the requirement actually is

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

#### How the configuration meets it

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

#### What is sized, and what is not demonstrated

This is the part of the section that decides whether the rest of it can be trusted.

**Sized.** The vertical phase is sized: hover power from momentum theory at thrust equal to
weight, the buffer that supplies the difference between that peak and the cruise demand, the
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

#### What the historical record does and does not give back

One of the 1954 objections is genuinely removed and it should be named exactly. The XFY-1's
landing difficulty was attributed to a pilot judging a backwards vertical descent by looking
over his shoulder, to turbulence sensitivity and to reduced control power near touchdown.
**There is no pilot here, and height above ground is a sensor measurement rather than a human
estimate.** That disposes of the spatial-orientation objection and nothing else. **Precise
hovering, ground gusts and the descent itself are not disposed of by removing the pilot**, and
this section does not pretend otherwise.

#### What this half costs

Runway independence is not obtained free, and the charges appear later rather than here. The
tip frames that make the aircraft self-supporting are structure standing in the cruise
airstream, and Section 11 charges their drag. The attitude propellers they carry are exposed
for the whole cruise and cannot be feathered, and Section 11 charges that too. The buffer that
releases the engine from the hover peak is mass carried for the whole flight.

**The second half — cruise carried on a wing rather than on rotors — is the subject of the next
section**, and the two are combined in Section 7.

---

## 10. Step 6, in full (the cruise axis; one sentence corrected)

### The second half: cruise carried on a wing

#### The opponent, and the axis

On this axis the alternative is the multirotor, and as in the previous section the comparison
runs one way only. **Nothing here is claimed against fixed-wing aircraft.** A runway-launched
aeroplane cruises more efficiently than this configuration and pays none of the charges of
Section 2; that comparison is not made, and no result in this paper rests on it. The claim is
confined to the one thing the multirotor family structurally lacks: **a surface that carries the
cruise lift.**

#### What the requirement is

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

#### What the configuration does instead

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

#### What the margin actually is, in one currency

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

#### What the comparison gives, against both published quadrotors

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

#### Five qualifications, and every one of them runs against this configuration

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

#### What is sized, and what is not demonstrated

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

#### What this half costs

The wing that makes cruise efficient is carried through the vertical phase, where it produces
nothing and presents the aircraft's largest surface to ground wind. The tailless planform that
follows from having no boom constrains the sweep, because with no horizontal stabiliser the
pitching moment must come from the distribution of lift along the body itself. And the
fixed-pitch propeller that serves both regimes is the reason the margin above sits where it does
rather than higher — at e = 0.85 the same airframe would reach 7.48 to 9.20. Section 11 charges all three.

**The two halves are now on the table separately. Section 7 is where they are combined**, and
the combination is what this paper is for.

---

## 11. Step 7, in full (the combination — the contribution)

### The combination

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

The change of regime is then made by **rotating the airframe**. The propulsors hold
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

## 12. Step 8, in full (the inventory)

### What it is made of, and what still moves

Section 7 claimed that a class of mechanism is absent. A claim of that kind is only as good as
the inventory behind it, so the inventory is given here in full, including the parts that move.

#### The airframe

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

#### The propulsion

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

#### The energy path

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
transition.** That is a design assignment, not a demonstrated result: whether the moment it
produces is sufficient, and whether the aircraft trims through the rotation, are **not settled in
this paper**: the moment is a sizing input to Section 10, but the trim through the rotation depends
on the transition aerodynamics, and Section 14 says why those are not currently reliable for anyone
on this class of configuration at the incidences the rotation passes through.

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

#### What meets the ground

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

#### What moves

The propellers rotate, as propellers do, and their shaft speed is commanded; but none of them
changes its orientation relative to the airframe, or its blade pitch, at any point in the flight.
**Beyond the propellers' rotation, one thing on this aircraft changes its configuration: the
strip.**
It is described as deployable in two halves — one side alone for roll, both together as a speed
brake. The actuator inventory is therefore the propulsion motors plus the strip's actuation.
**How many actuators that is, this study does not fix.** The systems budget carries the
actuation without sizing the mechanism, and naming a number here would be inventing one.

#### What this inventory does not settle

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
listing them. The nose pair meets all four parts of Section 3. The tip pairs meet none of the
first three: they are carried through cruise producing moments rather than thrust, so they fail
the second row of Section 3's table, and they are exposed while doing it. This is the partial
instantiation Section 3 lists as its **fourth** failure mode — meeting the condition where the
aircraft is carried and failing it elsewhere — and the charge it re-opens is the second, carried in
Section 11. *(They are not the second row of Section 3's table: that row concerns a propulsor that
lifts and is then carried, and the tip pairs do not lift. They produce moments, and Section 3's
permitted-cost clause places attitude devices outside the first charge while leaving them in the
airstream.)*

The free-wheeling state is physically determinate: the rotor settles where net shaft torque is
zero. **The stopped state is not.** Stopping a rotor requires the stop to be produced by
something — motor holding torque, an electrical brake, a mechanical lock — and a stopped
fixed-pitch blade also has an azimuth, so "stopped" is a family of aerodynamic states rather than
one. Neither the means nor the azimuth is fixed by this study, and the drag figure quoted for the
stopped condition should be read as the state Section 11 defines rather than as the state a
particular installation would reach.

---

## 13. What I am asking

1. **Step 15 against its sources.** Every sentence in Step 15 summarizes a step reproduced above. **Is
   any predicate stronger or weaker than the step it comes from?** Two axes changed standing this round
   and deserve a direct look: the cruise axis (positive throughout against one quadrotor, from slightly
   behind to comfortably ahead against the other) and the runway axis (now dependent on the energy
   store).
2. **Does Step 15 add anything the paper has not earned before it** — a claim, a number, a citation, an
   adjective? It is meant to contain none.
3. **The contribution on the mechanism axis.** Is it stated at the narrow strength the paper has agreed —
   no mechanism class that reorients a propulsor; not "nothing moves", not "simpler"; roll from the
   strip, with the reaction-torque channel declined? Is anything in Steps 7 and 8 inconsistent with how
   Step 15 states it?
4. **Proportion.** No cuts are being made. **Is the weight in the right places for a single-contribution
   paper, and are P1 and P3 right?** In particular: should the contribution be named in Step 1, given that
   Steps 1 and 9 currently state what the paper offers as three things?
5. **Step 14, second writing.** Does *"the loop closes"* now hold everywhere, and is the unknowns table
   complete?

**No source is needed for any of this.** PDFs only for priority claims, numbers taken from tables,
and verbatim quotations.
