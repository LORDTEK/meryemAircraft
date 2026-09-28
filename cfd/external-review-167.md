# Round 163 — The author's decisions on 5.2 and Section 7, drafted in full. Two versions of 5.2 so the author can see what distributing buys. To be applied unless there is a serious objection

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**

---

## 0. What the author decided (my translation, not verbatim)

**On 5.2 (Question A):**

> *In truth, Qwen and ChatGPT are right that the proper form is above and below: the inventory above, its limits below. But then we may not
> knead it enough to make it smaller. There is a devil hidden right here. If we distribute the limits and it shortens by the same amount anyway,
> I prefer above and below. So write both, distributed and above/below, and write both well. Whether the difference matters or not, we decide
> accordingly.*

**On Section 7, "What does not close" (Question B):**

> *The list goes to the supplement, with one sentence. The re-closure, with one sentence.*

**And:** *Present these to the readers too. If there is no serious objection, we apply them.*

So this round the threshold is the author's: **apply unless there is a serious objection.** If you object, say it is serious and why.

---

## 1. 5.2: the two versions, and what distributing buys

**Both versions share five cuts** (C1–C5). None removes a finding, and none touches a protected sentence:

| | Cut | Why |
|---|---|---|
| C1 | *"This is a control question rather than a property of the hardware, and it is stated as one."* | voice (Grok) |
| C2 | *" — the aircraft's longitudinal axis, which is the roll axis in body terms (Section 5.2)"* in the hover-residual paragraph | **my Round 162 defect**: after the move it pointed at its own section. It also repeats the axis note in *The propulsion* |
| C3 | *", and only one of them is physically closed"* in the cruise-state lead | the protected *"The free-wheeling state is physically determinate … The stopped state is not."* says it two paragraphs later |
| C4 | *"; Section 6.1 re-closes it at four masses, and Section 6.3 sets it beside a 1 000 kg reference design"* | two pointers inside a parenthesis; *"the design this inventory describes"* stays |
| C5 | *"The configuration replaces a pilot's workload with computation, and the computer is the part that does it."*, and *", and naming a number here would be inventing one"* | voice |

**What only the distributed version can do:**
- It drops the heading *"What this inventory does not settle"*.
- The hover-residual paragraph now sits directly after the roll paragraph, which has just said that every thrust vector is parallel to that
  axis and that the channel is declined. So its opening can lose the repetition (deletion only, one capital letter changed):

  > *"~~That axis is the one the configuration has chosen not to command with the propellers, which is why~~ The residual is awkward: the tip pairs
  > cannot absorb it by thrust differential~~, because their thrust vectors are parallel to that axis too~~, and the strip works against …"*

**Where each limit goes in the distributed version:**
- the two cruise states go into *The propulsion*, after the angular-momentum paragraph;
- the hover residual goes into *What produces each moment*, after the roll paragraph;
- *"The tip pairs are the parts that fail the escape condition"* closes the section in both versions.

**Measured, with the protected check run on a temporary copy of the step files:**

| | 5.2 words |
|---|---:|
| Today | 1 930 |
| **Above / below** (inventory, then *"What this inventory does not settle"*) | **1 844** |
| **Distributed** | **1 816** |
| **Difference** | **28** |

**Distributing buys 28 words.** By the author's rule (*"if it shortens by the same amount anyway, I prefer above and below"*), the choice is the
author's to make with this number. **My view:** 28 words is not a difference that should decide the structure. Both versions read well. The
above/below version keeps the limits findable in one place, which is what Qwen and ChatGPT argued.

**Please:** say whether either version loses anything, and whether you see a cut that would make the difference larger. That is the author's
*"devil"*.

---

## 2. Section 7: the two one-sentence replacements

Both are **new sentences** (label R). Please check each word against what it replaces.

**The re-closure. Before** (175 words):

> **Closing the loop on a measured store is a sensitivity of that package, not a second aircraft**: the buffer is derived inside the loop from the take-off demand at a given specific power, and everything else is Section 6.1's. At the bench rate of about 1.5 kW per kilogram the loop closes at 94.6 to 101.2 kg, 76 to 81 percent heavier, with a buffer of 13.4 to 14.7 percent; at the design study's 4 kW per kilogram it closes 6 to 8 percent heavier (the table is Supplement S14). **These masses are the Section 6.1 package with one input changed. They are not a structural closure at 100 kg**, and whether the airframe fraction holds at twice the mass it was set at is not established. If Section 6.1's take-off masses are retained instead of re-closing at the bench rate, the payload falls to about 7 kg rather than 13; at the flown system's continuous rating the loop only just closes, and at the unit pack's continuous rating it does not close at all.

**After:**

> Closed again on the measured bench rate of about 1.5 kW per kilogram, the same package becomes 76 to 81 percent heavier, a sensitivity of that package with one input changed rather than a structural closure (Supplement S14).

- **What moves to S14:** 94.6–101.2 kg, the 13.4–14.7 % buffer, the design study's 6–8 %, the 7 kg payload, and the two continuous ratings
  that do not close. S14 already holds the table; the paragraph goes there in full.
- **Two protected sentences** go with it: *"These masses are the Section 6.1 package with one input changed."* and *"They are not a structural
  closure at 100 kg"*. **The author's decision, E12.**
- **Their meaning stays in the body.** The new sentence carries *"a sensitivity of that package with one input changed rather than a
  structural closure"*.
- **The later sentence stays fed.** *"The ranges … survive the re-closure only because the fuel fraction is held, on an aircraft three-quarters
  heavier"* keeps its antecedent: *"the re-closure"* and *"76 to 81 percent heavier"*.

**The list. Before** (160 words):

> The remaining items are not known obstacles; they are questions this work has not answered, and each is listed with what would settle it in Supplement S14. They are: - the pitching moment through the transition; - section drag at low Reynolds number; - the tip pairs' stopped cruise state; - the tip pairs' shaft power when commanded off the free-wheeling state in cruise; - the buffer's energy, not only its power; - the electrical path at peak; - the airframe's mass; - the strip and the fairing; - closed-loop attitude control in hover and in cruise, including the declined reaction-torque channel, the hover torque residual and the allocation of the tip pairs between take-off margin and attitude authority; - vertical descent and the landing transition; - ground handling and landing loads; - the competitor's lift-group mass; - the competitor's cruise propeller efficiency; - rotor–structure and rotor–wing interference; - engine installation; - blade-family selection; - the variable-pitch counterfactual; - atmosphere.

**After:**

> Eighteen further questions are open, and Supplement S14 lists each with what it bears on and what would settle it.

- The eighteen are S14's table rows, one for one. (S14 also has a row on other store types, which is marked as part of the known obstacle,
  not one of the eighteen.)
- The next paragraph (*"None of these is a small correction to a known quantity. Two of them need validated data …"*) stays. Its *"these"*
  now refers to *"eighteen further questions"*.

**Section 7: 1 185 → 908 words (−277).**

---

## 3. What I ask of you

| # | Item |
|---|---|
| a | 5.2, above/below: any loss? Any objection you would call serious? |
| b | 5.2, distributed: the same |
| c | **Can either version shrink further without losing a finding?** (The author's *"devil"*: does distributing buy more than 28 words?) |
| d | Section 7: the two new sentences — does either say more, or less, than what it replaces? |
| e | Your own proposals; answer each other |

---

## 4. Full texts (assembled view, as they would stand)

### 4.1 5.2, above / below — 1844 words

##### 5.2 What it is made of, and what still moves

Section 5.1 claimed that a class of mechanism is absent. A claim of that kind is only as good as the inventory behind it, so the inventory is given here in full, including the parts that move.

###### The airframe

The entire airframe is the wing. There is no cylindrical fuselage: every part of the body that is carried is also a part that lifts. Leading-edge sweep varies continuously along the span while the trailing edge is held at 25°, so the realised sweep runs from 45° at the root to 38.3° at the tip — a variation of under seven degrees, with the crescent character coming from the curvature of the leading edge rather than from a large change in sweep. For the 50 kg reference design — the design this inventory describes — the span is 3.453 m, the wing area 1.979 m², and the aspect ratio 6.03.

Sweep is not a free parameter here, and the reason is structural to the configuration rather than aerodynamic preference. The aircraft is tailless. With no horizontal stabiliser on a boom, the pitching moment must come from the distribution of lift along the body itself, and sweep is what places the outboard sections behind the centre of gravity so they can produce it. **The sweep angle and the longitudinal stability are one design variable seen from two directions.**

###### The propulsion

**Five propeller stations, ten rotors:** every station is a coaxial counter-rotating pair. The reason is narrow: **reaction torque.** A single propeller applies to the airframe a torque equal and opposite to the one it applies to the air. It acts about the propeller axis, which on this aircraft is the body's longitudinal axis — the roll axis in body terms — in both regimes, and it must be opposed continuously, either by a control surface, which costs drag, or by the reaction torque of other rotors run at a different speed, which costs a control channel. A torque-balanced counter-rotating pair does not produce it. *(This paper fixes body-axis naming throughout. That axis is the roll axis in both regimes; what changes is its orientation relative to the earth — it stands vertical in the hover attitude, where a moment about it appears as a change of heading, and horizontal in cruise, where it appears as a bank. The two conventions are not mixed here.)*

One pair sits at the nose, 1.20 m in diameter on the 50 kg reference design, and produces all propulsive thrust in both regimes. Four smaller pairs, 0.20 m in diameter, sit at the ends of rigid frames projecting from the wing tips. Every pair is of **fixed geometry**: no cyclic pitch, no collective, no variable-pitch hub and no mechanism that changes a rotor's orientation relative to the airframe. Shaft speed is commanded; blade geometry and orientation are not. Each rotor of each pair is driven by its own electric machine on a common axis, so **the splitting gearbox and the mechanical governors that synchronise it are not required**. This work makes no claim about the shafting: whether the two machines are stacked on the axis or arranged some other way is an implementation question it does not settle.

The counter-rotating arrangement carries a second consequence that the transition analysis depends on. **At equal counter-rotating speeds, the net angular momentum of the propulsion system is nominally zero**: rotating the airframe through ninety degrees therefore produces no gyroscopic moment for the control system to cancel. If the pairs are speed-trimmed, that cancellation is no longer exact (below). In a tilting architecture that term is present and must be designed for.

###### The energy path

A series hybrid: fuel to engine, engine to generator, generator to electric machines at the rotors. The engine is not mechanically connected to any rotor. It is an energy source, and that decoupling is what allows it to be sized by cruise rather than by hover.

**The separation the architecture depends on is that the continuous cruise requirement is several times smaller than the hover peak, and that the difference is supplied from a battery buffer for the vertical phase alone.** No wattage is quoted here; the closed powers are Section 6.1's.

###### What produces each moment

**Pitch and yaw come from differential thrust between the tip pairs** (body axes, as fixed in the note above), and the two axes do not have the same moment arm. The frames project ±0.71 m perpendicular to the planform, so a differential between the upper and lower pairs acts at 0.71 m in pitch, while a differential between the left and right pairs acts at the semi-span, **1.726 m — 2.43 times the pitch arm.** The yaw arm is therefore the larger by that factor, which is the reverse of the usual situation and is a consequence of the layout rather than a design choice. What authority each axis actually has depends on the available thrust differential and on allocation as well as on the arm, and is not settled by the ratio alone.

**The same differential-thrust system is what is assigned to rotate the airframe through transition.** That is a design assignment, not a demonstrated result (Section 5.1): the moment it produces is a sizing input to Section 6.1, and whether it suffices and whether the aircraft trims through the rotation are **not settled in this paper**.

**Roll comes from neither, and the reason is a choice rather than an impossibility.** Every thrust vector is parallel to the body axis, so no combination of thrust settings produces a moment about it. Reaction torque could produce one: each rotor has its own machine, so running the two rotors of a pair at different speeds leaves a net torque about that axis, and the tail-sitter literature uses exactly that channel. **This configuration declines it** — every pair is operated torque-balanced, so no reaction torque is spent on control — and assigns the axis to an aerodynamic device instead. What declining it costs is not counted in this work. Roll is produced instead by a strip on the lower surface: inclined at 45° in planform, running 120 % of root chord, reaching 67 % of semi-span, and standing 2 cm proud at its inboard end and 6 cm at its outboard end. **Extension is the control variable** — the strip is modulated, not switched — and deploying it also pitches the nose down by a small increment. Its inboard 46 % lies inside the nose propeller's slipstream, where dynamic pressure is set by disc loading and is therefore available at zero airspeed; its outboard 54 % works against the freestream in cruise. That split is why one device serves both regimes. The split is an estimate: the slipstream boundary it rests on is not derived in this work.

###### What meets the ground

The aircraft rests on five points: the four lower ends of the tip frames, and the aft end of a keel running along the centreline.

**The frames carry a fairing, and it is not only a drag measure.** The frames are the only surfaces standing perpendicular to the wing plane, and a planar planform supplies no directional stability at all, so the fairing is also the only vertical surface the aircraft has. Sized against the criterion the tailless literature recommends — C_n_β greater than 0.001 per degree — the chord required over the combined frame length is **39 mm**, against the 50 to 70 mm that a 20 mm faired strut carries in any case. Directional stability on this configuration therefore does not ask for a surface; it asks for a fairing on a frame that is already there.

**One part is not airframe: the flight control system.** The stability of this configuration is not airframe-borne alone — the rest is produced by differential thrust and by the strip, both of which are actively commanded — so an attitude reference and a flight computer are not optional equipment but part of the mechanism the preceding paragraphs describe. They are carried in the systems budget. 

###### What moves

The propellers rotate, and their shaft speed is commanded; but none of them changes its orientation relative to the airframe, or its blade pitch, at any point in the flight. **Beyond the propellers' rotation, one thing on this aircraft changes its configuration: the strip.** It is specified as deployable in two halves — one side alone for roll, both together as a speed brake. The actuator inventory is therefore the propulsion motors plus the strip's actuation. **How many actuators that is, this study does not fix.** The systems budget carries the actuation without sizing the mechanism.

**The tip pairs are the parts that fail the escape condition** (Section 5.1). They are sized for moments and used for them in both regimes; they add the take-off margin (Section 3) but were not sized for weight support. Section 2.2's permitted-cost clause therefore places them outside the first charge while leaving them in the airstream.

###### What this inventory does not settle

**An untrimmed hover torque, with no trim mechanism identified.** 

The torque balance within each pair is set exact at the cruise condition rather than at hover, so a small residual remains in hover. It acts about the propeller axis .

That axis is the one the configuration has chosen not to command with the propellers, which is why the residual is awkward: the tip pairs cannot absorb it by thrust differential, because their thrust vectors are parallel to that axis too, and the strip works against dynamic pressure that the slipstream supplies over only part of its length at zero airspeed. What is left is the channel the configuration set aside — the speed trim of the pairs, which is a reaction-torque command and not a thrust one. Either the residual is small enough to be absorbed that way, which this study has not shown and which would mean the architecture spends a little of the channel it declined, or another duty falls on the strip.

**The fixed geometry of the tip pairs leaves two admissible cruise states.** Unable to feather, the pairs must either turn at the zero-shaft-torque condition or be stopped. This configuration uses the first: free-wheeling at zero shaft torque is the tip pairs' uncommanded cruise state, and it is the drag state Section 6.2 charges. The shaft power of commanded departures from that state, for attitude moments in cruise, is not computed.

The free-wheeling state is physically determinate: the rotor settles where net shaft torque is zero. **The stopped state is not.** Stopping a rotor requires the stop to be produced by something — motor holding torque, an electrical brake, a mechanical lock — and a stopped fixed-pitch blade also has an azimuth, so "stopped" is a family of aerodynamic states rather than one. Neither the means nor the azimuth is fixed by this study, and the drag figures estimated for the stopped condition (Supplement S11) should be read as estimates for an assumed azimuth rather than as the state a particular installation would reach. The free-wheeling state needs no stopping means; the stopped state does, and if it were a brake or a lock rather than motor holding torque, the count of Section 5.1 would gain a class.

### 4.2 5.2, distributed — 1816 words

##### 5.2 What it is made of, and what still moves

Section 5.1 claimed that a class of mechanism is absent. A claim of that kind is only as good as the inventory behind it, so the inventory is given here in full, including the parts that move.

###### The airframe

The entire airframe is the wing. There is no cylindrical fuselage: every part of the body that is carried is also a part that lifts. Leading-edge sweep varies continuously along the span while the trailing edge is held at 25°, so the realised sweep runs from 45° at the root to 38.3° at the tip — a variation of under seven degrees, with the crescent character coming from the curvature of the leading edge rather than from a large change in sweep. For the 50 kg reference design — the design this inventory describes — the span is 3.453 m, the wing area 1.979 m², and the aspect ratio 6.03.

Sweep is not a free parameter here, and the reason is structural to the configuration rather than aerodynamic preference. The aircraft is tailless. With no horizontal stabiliser on a boom, the pitching moment must come from the distribution of lift along the body itself, and sweep is what places the outboard sections behind the centre of gravity so they can produce it. **The sweep angle and the longitudinal stability are one design variable seen from two directions.**

###### The propulsion

**Five propeller stations, ten rotors:** every station is a coaxial counter-rotating pair. The reason is narrow: **reaction torque.** A single propeller applies to the airframe a torque equal and opposite to the one it applies to the air. It acts about the propeller axis, which on this aircraft is the body's longitudinal axis — the roll axis in body terms — in both regimes, and it must be opposed continuously, either by a control surface, which costs drag, or by the reaction torque of other rotors run at a different speed, which costs a control channel. A torque-balanced counter-rotating pair does not produce it. *(This paper fixes body-axis naming throughout. That axis is the roll axis in both regimes; what changes is its orientation relative to the earth — it stands vertical in the hover attitude, where a moment about it appears as a change of heading, and horizontal in cruise, where it appears as a bank. The two conventions are not mixed here.)*

One pair sits at the nose, 1.20 m in diameter on the 50 kg reference design, and produces all propulsive thrust in both regimes. Four smaller pairs, 0.20 m in diameter, sit at the ends of rigid frames projecting from the wing tips. Every pair is of **fixed geometry**: no cyclic pitch, no collective, no variable-pitch hub and no mechanism that changes a rotor's orientation relative to the airframe. Shaft speed is commanded; blade geometry and orientation are not. Each rotor of each pair is driven by its own electric machine on a common axis, so **the splitting gearbox and the mechanical governors that synchronise it are not required**. This work makes no claim about the shafting: whether the two machines are stacked on the axis or arranged some other way is an implementation question it does not settle.

The counter-rotating arrangement carries a second consequence that the transition analysis depends on. **At equal counter-rotating speeds, the net angular momentum of the propulsion system is nominally zero**: rotating the airframe through ninety degrees therefore produces no gyroscopic moment for the control system to cancel. If the pairs are speed-trimmed, that cancellation is no longer exact (below). In a tilting architecture that term is present and must be designed for.

**The fixed geometry of the tip pairs leaves two admissible cruise states.** Unable to feather, the pairs must either turn at the zero-shaft-torque condition or be stopped. This configuration uses the first: free-wheeling at zero shaft torque is the tip pairs' uncommanded cruise state, and it is the drag state Section 6.2 charges. The shaft power of commanded departures from that state, for attitude moments in cruise, is not computed.

The free-wheeling state is physically determinate: the rotor settles where net shaft torque is zero. **The stopped state is not.** Stopping a rotor requires the stop to be produced by something — motor holding torque, an electrical brake, a mechanical lock — and a stopped fixed-pitch blade also has an azimuth, so "stopped" is a family of aerodynamic states rather than one. Neither the means nor the azimuth is fixed by this study, and the drag figures estimated for the stopped condition (Supplement S11) should be read as estimates for an assumed azimuth rather than as the state a particular installation would reach. The free-wheeling state needs no stopping means; the stopped state does, and if it were a brake or a lock rather than motor holding torque, the count of Section 5.1 would gain a class.

###### The energy path

A series hybrid: fuel to engine, engine to generator, generator to electric machines at the rotors. The engine is not mechanically connected to any rotor. It is an energy source, and that decoupling is what allows it to be sized by cruise rather than by hover.

**The separation the architecture depends on is that the continuous cruise requirement is several times smaller than the hover peak, and that the difference is supplied from a battery buffer for the vertical phase alone.** No wattage is quoted here; the closed powers are Section 6.1's.

###### What produces each moment

**Pitch and yaw come from differential thrust between the tip pairs** (body axes, as fixed in the note above), and the two axes do not have the same moment arm. The frames project ±0.71 m perpendicular to the planform, so a differential between the upper and lower pairs acts at 0.71 m in pitch, while a differential between the left and right pairs acts at the semi-span, **1.726 m — 2.43 times the pitch arm.** The yaw arm is therefore the larger by that factor, which is the reverse of the usual situation and is a consequence of the layout rather than a design choice. What authority each axis actually has depends on the available thrust differential and on allocation as well as on the arm, and is not settled by the ratio alone.

**The same differential-thrust system is what is assigned to rotate the airframe through transition.** That is a design assignment, not a demonstrated result (Section 5.1): the moment it produces is a sizing input to Section 6.1, and whether it suffices and whether the aircraft trims through the rotation are **not settled in this paper**.

**Roll comes from neither, and the reason is a choice rather than an impossibility.** Every thrust vector is parallel to the body axis, so no combination of thrust settings produces a moment about it. Reaction torque could produce one: each rotor has its own machine, so running the two rotors of a pair at different speeds leaves a net torque about that axis, and the tail-sitter literature uses exactly that channel. **This configuration declines it** — every pair is operated torque-balanced, so no reaction torque is spent on control — and assigns the axis to an aerodynamic device instead. What declining it costs is not counted in this work. Roll is produced instead by a strip on the lower surface: inclined at 45° in planform, running 120 % of root chord, reaching 67 % of semi-span, and standing 2 cm proud at its inboard end and 6 cm at its outboard end. **Extension is the control variable** — the strip is modulated, not switched — and deploying it also pitches the nose down by a small increment. Its inboard 46 % lies inside the nose propeller's slipstream, where dynamic pressure is set by disc loading and is therefore available at zero airspeed; its outboard 54 % works against the freestream in cruise. That split is why one device serves both regimes. The split is an estimate: the slipstream boundary it rests on is not derived in this work.

**An untrimmed hover torque, with no trim mechanism identified.** 

The torque balance within each pair is set exact at the cruise condition rather than at hover, so a small residual remains in hover. It acts about the propeller axis .

The residual is awkward: the tip pairs cannot absorb it by thrust differential, and the strip works against dynamic pressure that the slipstream supplies over only part of its length at zero airspeed. What is left is the channel the configuration set aside — the speed trim of the pairs, which is a reaction-torque command and not a thrust one. Either the residual is small enough to be absorbed that way, which this study has not shown and which would mean the architecture spends a little of the channel it declined, or another duty falls on the strip.

###### What meets the ground

The aircraft rests on five points: the four lower ends of the tip frames, and the aft end of a keel running along the centreline.

**The frames carry a fairing, and it is not only a drag measure.** The frames are the only surfaces standing perpendicular to the wing plane, and a planar planform supplies no directional stability at all, so the fairing is also the only vertical surface the aircraft has. Sized against the criterion the tailless literature recommends — C_n_β greater than 0.001 per degree — the chord required over the combined frame length is **39 mm**, against the 50 to 70 mm that a 20 mm faired strut carries in any case. Directional stability on this configuration therefore does not ask for a surface; it asks for a fairing on a frame that is already there.

**One part is not airframe: the flight control system.** The stability of this configuration is not airframe-borne alone — the rest is produced by differential thrust and by the strip, both of which are actively commanded — so an attitude reference and a flight computer are not optional equipment but part of the mechanism the preceding paragraphs describe. They are carried in the systems budget. 

###### What moves

The propellers rotate, and their shaft speed is commanded; but none of them changes its orientation relative to the airframe, or its blade pitch, at any point in the flight. **Beyond the propellers' rotation, one thing on this aircraft changes its configuration: the strip.** It is specified as deployable in two halves — one side alone for roll, both together as a speed brake. The actuator inventory is therefore the propulsion motors plus the strip's actuation. **How many actuators that is, this study does not fix.** The systems budget carries the actuation without sizing the mechanism.

**The tip pairs are the parts that fail the escape condition** (Section 5.1). They are sized for moments and used for them in both regimes; they add the take-off margin (Section 3) but were not sized for weight support. Section 2.2's permitted-cost clause therefore places them outside the first charge while leaving them in the airstream.

### 4.3 Section 7, "What does not close" — 908 words

#### 7. What does not close

Section 6.1 closed the sizing loop on a declared package and said that whether an aircraft can be built to it is a different question. **This section is where that question is answered, and for the first item the answer is no: the required store performance is not demonstrated by the sources consulted here.** Section 8 calls this section a debt: questions the paper does not answer and that better evidence would. It is stated in that order — first the obstacle that is known, then what is not known.

##### First, the known obstacle: the energy store

**Every closure in Section 6.1 carries a buffer of 3.6 percent of take-off mass**, an input rather than a result (Sections 6.2 and 6.3). Taken at the electrical bus, where the buffer sits, **the four closures ask the buffer for 4.7 to 5.2 kW per kilogram of buffer to hover, and 5.5 to 6.1 kW per kilogram of buffer to leave the ground** with the tip pairs at full thrust (Section 3).

**What has been measured is a fraction of that, and the store figures available are of four different kinds.** A 24-series nickel–cobalt–manganese pack designed, bench-tested and flown in a 210 kg-class electric VTOL aircraft is rated, as a flown system, at 0.892 kW per kilogram continuous; its unit pack, discharged on the bench at its highest tested rate, delivered on average about 1.5 kW per kilogram (Supplement S14). A NASA-funded design study adopts 4 kW per kilogram and describes that figure as about twice that of existing batteries. The same study notes lithium-polymer figures in the literature as high as 3 kW per kilogram, which it cites rather than measures; against that figure the take-off demand is 1.8 to 2.0 times. The study argues that, because pulse current limits can exceed continuous ones — by more than a factor of two in one commercial module it cites — a pack with the required specific power may be possible with existing technology; the study's hover lasts twenty seconds or less; this aircraft's vertical phases occupy about a minute in all (Section 2.1), and how long each draws the peak is not computed here.

**The take-off demand of Section 6.1's closures is 3.7 to 4.1 times the bench rate — the highest figure obtained from a measurement — and 6.2 to 6.8 times the flown system's continuous rating**; hover alone is 3.1 to 3.5 times the bench rate. The comparison is between unlike ratings: a peak demand held through the vertical phases, a bench average over minutes, a continuous rating, a design assumption, and a literature figure the study cites without its rating. **The gap is real on every one of them; the factor quoted is peak demand against bench average.** The package Section 6.1 closes on does not exist with any store the sources consulted here report as built.

Closed again on the measured bench rate of about 1.5 kW per kilogram, the same package becomes 76 to 81 percent heavier, a sensitivity of that package with one input changed rather than a structural closure (Supplement S14).

**This is where the coupling Section 6.3 found is paid**: the buffer is the conversion the escape condition permits — kilowatts of hover peak paid in kilograms of store. **The escape from Bill 3 is real in the sense Section 2.2 defined it, and its price depends on a component whose required performance has not been demonstrated.**

##### What the obstacle reaches, and what it does not

**It reaches every number that describes this aircraft at Section 6.1's masses**: the closed masses of 52.3 to 57.5 kg and the 13 kg payload assume the store. The ranges of 927 to 1 233 km survive the re-closure only because the fuel fraction is held, on an aircraft three-quarters heavier; they do not survive as 13 kg carried that far on a store that has been built. The vertical phase that Section 3 reports as sized was sized with this store in it, and Section 6.4's orderings were computed with the store held common at 3.6 percent; how they would move with a measured store is not computed.

**It does not reach the mechanism claim.** That is a statement about hardware, and a heavier store adds no pivot. **Nor does it reach the cruise-efficiency comparison of Section 4 as a ratio**: effective lift-to-drag ratio has no mass in it. As a comparison of aircraft, that section describes the configuration at Section 6.1's masses, which the store does reach.

##### Then what is not known

Eighteen further questions are open, and Supplement S14 lists each with what it bears on and what would settle it.

**None of these is a small correction to a known quantity.** Two of them need validated data rather than more of the computation already done: the transition moment, because three methods have been tried against it and disagree, and the low-Reynolds section drag, because the one method used here is least reliable exactly there.

##### What this section amounts to

**The loop closes; the aircraft is not shown to.** At the energy store the paper can name the gap exactly, in specific power and in take-off mass; everywhere else it can name only what would settle the question. **The architecture claim — that the configuration is arranged to change regime with no mechanism that reorients a propulsor — is a count of hardware, and nothing in this section reaches it.** What this section reaches is the aircraft, and the paper has not claimed the aircraft. The last section returns to the four axes and states what is claimed on each.
