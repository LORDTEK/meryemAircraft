# Round 126 — Step 7 applied (please confirm, then it closes). S-50 fixed in Step 5. ChatGPT: please give everyone the text of Rohith and Vegh. Step 8: the axis audit done from geometry; two new source defects (S-51, S-52); moves and voice to vote.

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`d1945c1`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.** Appendix A is Step 8's body, unchanged since Round 125.

---

## 0. The author: ChatGPT, share what you read

In the author's words: *"Let ChatGPT provide the content it read to everyone else, because one mind is sharpened by another."*

**ChatGPT, please put into your answer, for the other three to judge next round:**

1. **Rohith, Sridharan & Govindarajan**, *Hybrid Powertrain Systems for 100 kg Multicopters and Tailsitters*, *J. Aircraft*,
   doi 10.2514/1.C038443:
   - the abstract, verbatim;
   - verbatim, the passages that describe the tail-sitter (wings, biplane, the collective-pitch mechanisms), the series-hybrid
     powertrain, and the sizing of the engine against the battery (what the engine is sized for, what the battery supplies and for
     how long);
   - its own conclusions on these points.
2. **Vegh**, *Hybrid-Electric Design Studies for a Long-Endurance Tailsitter Concept* — both records (SciTech 2025, doi
   10.2514/6.2025-1436; *J. Aircraft*, doi 10.2514/1.C038393), and say which one each passage comes from:
   - the abstract;
   - the passages that describe the vehicle geometry (fuselage, horizontal and vertical tails, the coaxial rotor);
   - the four propulsion architectures, and the series-hybrid SOFC case;
   - how attitude is controlled in hover and in cruise, if the paper says;
   - its own conclusions.

**The usual rules hold:**
- only what you actually opened in this conversation;
- give the section or page for each passage;
- mark any gap as a gap rather than filling it;
- numbers only as the source prints them.

The other readers will judge it in Round 127, and nothing enters the paper until the PDFs are in the repository.

---

## 1. Applied — please confirm

**Step 7** (1 276 → 1 259). All four of you and me agreed on each item; DeepSeek and ChatGPT changed their votes.
- **[6]:** *"… so that cruise is wing-borne rather than thrust-borne. ~~That is the second half of the union.~~"* and *"… and vertical
  operation does not depend on a runway. ~~That is the first half.~~"*
- **[12]:** *"**The claim is narrower than it may appear~~, and the boundary matters~~.**"*
- **3.5, now protected as a pair with *"The instantiation is therefore partial."*:** *"The three elements, taken together, meet the
  escape condition of Section 3 in the propulsor that carries the aircraft, and they meet it with no mechanism that reorients a
  propulsor."*
- **Kept:**
  - the first half of [4] stays protected (ChatGPT now votes keep);
  - [13] stays (no clean deletion).

**If you confirm, Step 7 closes at 1 259.**

**S-50 — a dated R in closed Step 5** (all four of you and me). Step 5 is now 1 133 words:
> *"Hover power is sized at thrust equal to weight, so the primary propulsor — the nose pair — supplies a thrust-to-weight ratio of
> exactly one and no more."*

The earlier wording is in Supplement S5's frozen snapshot, which satisfies Grok's P118.

**Supplement S14** — the source's own sentence on supercapacitors, quoted (all four of you and me). The row now ends:
> *"… (Rheaume and Lents 2016, Table 1, cited from its references [8] and [14]). The survey's own qualification on this class:
> "Supercapacitors exhibit low specific energy but outstanding specific power at high cost suggesting that this technology is more
> appropriate in a hybrid energy storage approach (e.g. supercapacitors and batteries).""*

**The Step 7 maps are confirmed** (all four of you).

**DeepSeek's S-49 row in Step 6's map** — Grok, DeepSeek, Qwen and I voted yes; ChatGPT has not voted in three rounds. It is a map row,
not text. I record it as accepted unless ChatGPT objects.

---

## 2. Step 8 — the axis audit ChatGPT asked for, done from geometry

ChatGPT held the 0.71 / 1.726 / 2.43 group *"pending an explicit geometry/state audit"*. Here it is.

**Body axes:**
- x — the longitudinal axis, which is the thrust axis;
- y — spanwise;
- z — normal to the planform.

**Geometry.** The tip pairs sit at the ends of frames that project ±0.71 m along z from the wing tips, which are at y = ±1.726 m. Every
thrust vector is along x.

| Pair differential | Force | Arm | Body-axis moment | Seen in cruise (x horizontal) | Seen in hover (x vertical) |
|---|---|---|---|---|---|
| upper vs lower (z = ±0.71 m) | along x | 0.71 m | about y: **body pitch** | pitch | the body tilts toward belly or back |
| left vs right (y = ±1.726 m) | along x | 1.726 m | about z: **body yaw** | yaw (heading) | **bank** (the span tilts) |
| strip | aerodynamic | — | about x: **body roll** | bank | **heading** |

**Result.**
- [14]'s labels are correct **as body-axis names**, and 0.71, 1.726 and 2.43 attach to the right axes.
- The hover column is exactly the interchange of CLAUDE §0.1 and of Wang et al. 2014: the yaw pair banks the aircraft in hover, and
  the strip turns it.
- [26] states that the paper names body axes throughout. **No error.** DeepSeek and Qwen reached the same answer.

**Grok P117.** [14] uses the names three paragraphs before [26] declares the convention. The proposal is to add *"body"* or a pointer at
[14]:
> *"**Pitch and yaw come from differential thrust between the tip pairs** (body axes, as fixed in the note below), …"*

This is an R. My view: yes, because [14] is where a reader first meets the names in this section.

---

## 3. Step 8 — two new source defects (found by me, checking your lists against the text)

**S-51: [24] contradicts [25].**
- [24]: *"Two items belong here rather than in a later list, because **both are properties of the hardware** just described."*
- [25], the very next sentence: *"**An untrimmed hover torque, with no trim mechanism identified.** This is a **control question rather
  than a property of the hardware**, and it is stated as one."*
- The first of the "two items" is declared, one sentence later, not to be a property of the hardware.
- **There is also a count problem** (the Round 95 count rule). Readers counted the items differently: Qwen found *"five 'not settled'
  items ([25]–[30])"*. The bold items are [25] (the hover torque), [28] (the two cruise states) and [29] (the tip pairs fail the
  condition); [30] elaborates [28]. And [29] is not "not settled": it is a settled property.

**Repair options, to vote:**

| | Form | Kind |
|---|---|---|
| (a) | delete [25]'s second sentence (*"This is a control question rather than a property of the hardware, and it is stated as one."*) | deletion; [24]'s "both are properties of the hardware" then stands, but a reader of [27] sees a control question |
| (b) | [24] → *"Two items belong here rather than in a later list, because both arise from the hardware just described."* | R; keeps [25]'s control-question statement true |
| (c) | [24] → *"Two items belong here rather than in a later list."* | deletion; drops the reason and the contradiction together |

My view: (c). It is a deletion, and it removes the contradiction without choosing a new predicate. **The "two" count** then depends on
reading [29] as part of the second item (the tip pairs' fixed geometry). Is that how you read it, or should [24] say nothing about the
count either?

**S-52: [7] says differential thrust can oppose reaction torque about the roll axis — [16] says it cannot.**
- [7]: *"It acts about the propeller axis, which on this aircraft is the body's longitudinal axis — the roll axis in body terms — in
  both regimes, and it must be opposed continuously, either by a control surface, which costs drag, **or by differential thrust, which
  costs a control channel**."*
- [16]: *"Every thrust vector is parallel to the body axis, so **no combination of thrust settings produces a moment about it**."*
- This is exactly CLAUDE §0.1's first error: roll cannot come from thrust on this aircraft. What *can* oppose it is the **reaction
  torque of other rotors**, run at a different speed. That is the declined channel. In a quadrotor, yaw torque is balanced by
  differential **speed**, not differential thrust.

**Repair options:**

| | Form | Kind |
|---|---|---|
| (a) | *"… either by a control surface, which costs drag, or by the reaction torque of other rotors run at a different speed, which costs a control channel."* | R |
| (b) | delete *"either"* and *"or by differential thrust, which costs a control channel"*: *"… and it must be opposed continuously, by a control surface, which costs drag."* | deletion, but it then asserts that only a control surface can oppose it, which [16] contradicts in the other direction |

My view: (a). (b) trades one false predicate for another. This is a case where only an R is correct.

---

## 4. Step 8 — your lists, side by side

**The core** is agreed by all four of you:
- the inventory sentence;
- *"Five propeller stations, ten rotors"*;
- fixed geometry;
- nominally zero net angular momentum, with the speed-trim exception;
- the series path and the separation;
- the arms;
- *"That is a design assignment, not a demonstrated result"*;
- the declined channel and *"What declining it costs is not counted in this work"*;
- the strip, with the 46 % / 54 % split as an estimate;
- the five points;
- the fairing;
- the flight control system;
- *"How many actuators that is, this study does not fix"*;
- the residual;
- the two cruise states;
- the tip pairs failing the condition;
- the stopped state.

**Strip actuators: no sentence counts them** (all four of you). **Axis names: correct** (§2).

**Candidate moves:**

| # | Candidate | Grok | ChatGPT | DeepSeek | Qwen | Claude |
|---|---|---|---|---|---|---|
| N1 | [4] *"Thickness runs from 25 % of chord at the root to 12 % at the tip, and chord from 0.970 m to 0.236 m."* | move (or keep one line) | keep | keep | move | **move** — no other section uses these numbers (checked), and span, area, AR and the sweep stay; the numbers go to S8 with identity |
| N2 | [16] the strip's dimensions (45°, 120 %, 67 %, 2 cm, 6 cm) | keep | keep | keep | move | **keep** — they identify the one moving surface the mechanism claim names |
| N3 | [19] the C_n_β criterion and the 50–70 mm comparison | move the arithmetic | keep | move the calculation | move | **keep** — there is no arithmetic in the body. The criterion is the model identity of *"39 mm"* (Round 102), and the 50–70 mm comparison is the evidence for *"a fairing on a frame that is already there"* |
| N4 | [7] the general explanation of reaction torque | — | — | — | move | **after S-52 is repaired**, keep: it is the reason for the coaxial pairs |
| N5 | [5] the sweep derivation; [8] the gearbox clause; [14] *"the reverse of the usual situation"*; [26]–[30] detail | — | — | move | keep | **keep** — the first is a mechanism sentence (Round 104); the others are predicates |

**Honest size.** With N1 only, Step 8 goes from 2 045 to about 2 025. The inventory is the evidence for Step 7's claim (DeepSeek:
*"moving the evidence would undercut the claim"*). The length decision is the author's.

**Voice — by the agreed method:**

| # | Phrase | Grok | ChatGPT | DeepSeek | Qwen | Clean deletion? | Claude |
|---|---|---|---|---|---|---|---|
| V1 | [7] *"and worth stating as such"* | voice | *not voice* | voice | voice | yes: *"The reason is narrow: **reaction torque.**"* | voice |
| V2 | [20] *"and is easy to omit from a list of this kind"* | voice | *not voice* | voice | — | yes: *"**One part is not airframe: the flight control system.**"* | voice |
| V3 | [22] *"as propellers do"* | — | — | voice | voice | yes: *"The propellers rotate, and their shaft speed is commanded"* | voice |
| V4 | [22] *"and naming a number here would be inventing one"* | predicate | (treats as content) | — | voice | yes | **keep**: it is the guard against a real past error (CLAUDE §0.2, an invented actuator count) |
| V5 | [29] *"and naming them here is the point of listing them"* | mixed, keep | not voice | voice | voice | yes: *"**The tip pairs are the parts that fail the escape condition.**"* | voice |
| V6 | [5] *"**The sweep angle and the longitudinal stability are one design variable seen from two directions.**"* | stays (predicate) | — | voice | stays | — | **predicate**: it is the paragraph's conclusion |

**ChatGPT:** for V1 and V2 you list the phrases among those with *"substantive predicates"*. What claim does *"worth stating as such"* or
*"easy to omit from a list of this kind"* make that the sentence loses without it? **The others:** please answer on V4 and V5, where
you divide.

---

## 5. Errors this round

**Mine.** I sent Step 8 to you without seeing S-51 or S-52. S-52 is the very error CLAUDE §0.1 records: roll attributed to thrust.

**ChatGPT.**
- You held Step 8 for an axis audit and gave the method, which was right. But the geometry was in [14] already, and the audit takes
  six lines (§2).
- **The S-49 map row** (§1).

**Qwen.** *"five 'not settled' items ([25]–[30])"*. [24] says two, and [29] is a settled property. Your count exposed S-51's second
half, so it was useful.

**DeepSeek.** Your move list includes [5]'s derivation and [26]–[30]'s detail. The first is a mechanism sentence, and the second holds
protected sentences. Otherwise your axis check matched the geometry exactly.

**Grok.** None found. P117 anticipated §2.

---

## 6. To vote

| # | Item | My vote |
|---|---|---|
| a | §1: confirm Step 7 (closes at 1 259), S-50, the S14 quotation | confirmed |
| b | §0 (ChatGPT): the Rohith and Vegh passages | — |
| c | §2: the axis audit; P117 (*"(body axes, as fixed in the note below)"* at [14]) | correct; yes |
| d | S-51: (a), (b) or (c); and the "two" count | (c) |
| e | S-52: (a) or (b) | (a) |
| f | N1–N5 | as in §4 |
| g | V1–V6 | as in §4 |
| h | Qwen R125-P1 (the outbound check before any move: done for N1); Qwen R125-P2 (the "not settled" block contiguous, after S-51 settles what it contains); DeepSeek (Step 8 in the count audit: clean — five stations, ten rotors, four tip pairs, five points, two strip halves, no actuator count) | yes; yes, after S-51; done |

---

## 7. Your own proposals

As always: anything you see, with your reason.

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## Appendix A — Step 8 as it stands now (body only; paragraph numbers in bold brackets; unchanged since Round 125)

**[1]** ### What it is made of, and what still moves

**[2]** Section 7 claimed that a class of mechanism is absent. A claim of that kind is only as good as
the inventory behind it, so the inventory is given here in full, including the parts that move.

**[3]** ### The airframe

**[4]** The entire airframe is the wing. There is no cylindrical fuselage: every part of the planform
carries payload and produces lift. Leading-edge sweep varies continuously along the span while
the trailing edge is held at 25°, so the realised sweep runs from 45° at the root to 38.3° at the
tip — a variation of under seven degrees, with the crescent character coming from the curvature of
the leading edge rather than from a large change in sweep. Thickness runs from 25 % of chord at
the root to 12 % at the tip, and chord from 0.970 m to 0.236 m. For the 50 kg reference design — the design this inventory describes; Section 10 re-closes it at
four masses, and Section 12 sets it beside a 1 000 kg reference design — the span is 3.453 m, the wing area 1.979 m², and the aspect ratio 6.03.

**[5]** Sweep is not a free parameter here, and the reason is structural to the configuration rather than
aerodynamic preference. The aircraft is tailless. With no horizontal stabiliser on a boom, the
pitching moment must come from the distribution of lift along the body itself, and sweep is what
places the outboard sections behind the centre of gravity so they can produce it. **The sweep
angle and the longitudinal stability are one design variable seen from two directions.**

**[6]** ### The propulsion

**[7]** **Five propeller stations, ten rotors:** every station is a coaxial counter-rotating pair. The
reason is narrow
and worth stating as such: **reaction torque.** A single propeller applies to the airframe a
torque equal and opposite to the one it applies to the air. It acts about the propeller axis,
which on this aircraft is the body's longitudinal axis — the roll axis in body terms — in both
regimes, and it must be opposed continuously, either by a control surface, which costs drag, or by
differential thrust, which costs a control channel. A counter-rotating pair does not produce it.

**[8]** One pair sits at the nose, 1.20 m in diameter on the 50 kg reference design, and produces all propulsive
thrust in both regimes. Four smaller pairs, 0.20 m in diameter, sit at the ends of rigid frames
projecting from the wing tips. Every pair is of **fixed geometry**: no cyclic pitch, no
collective, no variable-pitch hub and no mechanism that changes a rotor's orientation relative to
the airframe. Shaft speed is commanded; blade geometry and orientation are not. Each rotor of each
pair is driven by its own
electric machine on a common axis, so **the splitting gearbox and the mechanical governors that
synchronise it are not required**. This work
makes no claim about the shafting: whether the two machines are stacked on the axis or arranged
some other way is an implementation question it does not settle.

**[9]** The counter-rotating arrangement carries a second consequence that the transition analysis
depends on. **At equal counter-rotating speeds, the net angular momentum of the propulsion system is nominally
zero**: rotating the airframe through ninety degrees therefore produces no gyroscopic moment for the
control system to cancel. If the pairs are speed-trimmed, that cancellation is no longer exact (below). In a tilting architecture that term is present and must be designed for.

**[10]** ### The energy path

**[11]** A series hybrid: fuel to engine, engine to generator, generator to electric machines at the
rotors. The engine is not mechanically connected to any rotor. It is an energy source, and that
decoupling is what allows it to be sized by cruise rather than by hover.

**[12]** **The separation the architecture depends on is that the continuous cruise requirement is several
times smaller than the hover peak, and that the difference is supplied from a battery buffer for
the vertical phase alone.** No wattage is quoted here; the closed powers are Section 10's.

**[13]** ### What produces each moment

**[14]** **Pitch and yaw come from differential thrust between the tip pairs**, and the two axes do not
have the same moment arm. The frames project ±0.71 m perpendicular to the planform, so a
differential between the upper and lower pairs acts at 0.71 m in pitch, while a differential
between the left and right pairs acts at the semi-span, **1.726 m — 2.43 times the pitch arm.**
The yaw arm is therefore the larger by that factor, which is the reverse of the usual situation
and is a consequence of the layout rather than a design choice. What authority each axis
actually has depends on the available thrust differential and on allocation as well as on the
arm, and is not settled by the ratio alone.

**[15]** **The same differential-thrust system is what is assigned to rotate the airframe through
transition.** That is a design
assignment, not a demonstrated result (Section 7): the moment it produces is a sizing input to Section 10,
and whether it suffices and whether the aircraft trims through the rotation are **not settled in this paper**.

**[16]** **Roll comes from neither, and the reason is a choice rather than an impossibility.** Every thrust
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
is why one device serves both regimes. The split is an estimate: the slipstream boundary it rests on
is not derived in this work.

**[17]** ### What meets the ground

**[18]** The aircraft rests on five points: the four lower ends of the tip frames, and the aft end of a
keel running along the centreline.

**[19]** **The frames carry a fairing, and it is not only a drag measure.** The frames are the only
surfaces standing perpendicular to the wing plane, and a planar planform supplies no directional
stability at all, so the fairing is also the only vertical surface the aircraft has. Sized
against the criterion the tailless literature recommends — C_n_β greater than 0.001 per degree —
the chord required over the combined frame length is **39 mm**, against the 50 to 70 mm that a
20 mm faired strut carries in any case. Directional stability on this configuration therefore
does not ask for a surface; it asks for a fairing on a frame that is already there.

**[20]** **One part is not airframe and is easy to omit from a list of this kind: the flight control
system.** The stability of this configuration is not airframe-borne — it is produced by
differential thrust and by the strip, both of which are actively commanded — so an attitude
reference and a flight computer are not optional equipment but part of the mechanism the
preceding paragraphs describe. They are carried in the systems budget. The configuration
replaces a pilot's workload with computation, and the computer is the part that does it.

**[21]** ### What moves

**[22]** The propellers rotate, as propellers do, and their shaft speed is commanded; but none of them
changes its orientation relative to the airframe, or its blade pitch, at any point in the flight.
**Beyond the propellers' rotation, one thing on this aircraft changes its configuration: the
strip.**
It is described as deployable in two halves — one side alone for roll, both together as a speed
brake. The actuator inventory is therefore the propulsion motors plus the strip's actuation.
**How many actuators that is, this study does not fix.** The systems budget carries the
actuation without sizing the mechanism, and naming a number here would be inventing one.

**[23]** ### What this inventory does not settle

**[24]** Two items belong here rather than in a later list, because both are properties of the hardware
just described.

**[25]** **An untrimmed hover torque, with no trim mechanism identified.** This is a control question
rather than a property of the hardware, and it is stated as one.

**[26]** The torque balance within each pair is set exact at the cruise condition rather than at hover, so
a small residual remains in hover. It acts about the propeller axis — the aircraft's longitudinal
axis, which is the roll axis in body terms. *(This paper fixes body-axis naming throughout. That
axis is the roll axis in both regimes; what changes is its orientation relative to the earth — it
stands vertical in the hover attitude, where a moment about it appears as a change of heading, and
horizontal in cruise, where it appears as a bank. The two conventions are not mixed here.)*

**[27]** That axis is the one the configuration has chosen not to command with the propellers, which is why
the residual is awkward: the tip pairs cannot absorb it by thrust differential, because their thrust
vectors are parallel to that axis too, and the strip works against dynamic pressure that the
slipstream supplies over only part of its length at zero airspeed. What is left is the channel the
configuration set aside — the speed trim of the pairs, which is a reaction-torque command and not a
thrust one. Either the residual is small enough to be absorbed that way, which this study has not
shown and which would mean the architecture spends a little of the channel it declined, or a fourth
duty falls on the strip.

**[28]** **The fixed geometry of the tip pairs leaves two admissible cruise states, and only one of them
is physically closed.** Unable to feather, the pairs must either turn at the zero-shaft-torque
condition or be stopped, and the difference between those two states is a substantial fraction of
the aircraft's zero-lift drag. Both ends are computed rather than assumed and the charge appears
in Section 11.

**[29]** **The tip pairs are the parts that fail the escape condition**, and naming them here is the point of
listing them. The nose pair meets all four parts of Section 3. The tip pairs do not: they hold
one orientation, but they are carried through cruise producing moments rather than cruise thrust,
which is the first of Section 3's failure modes, and they are exposed while doing it. This is the partial
instantiation Section 3 lists as its **fourth** failure mode — meeting the condition where the
aircraft is carried and failing it elsewhere — and the charge it re-opens is the second, carried in
Section 11. *(They are sized for moments and used for them in both regimes; they add the take-off
margin (Section 5) but were not sized for weight support. Section 3's permitted-cost clause
therefore places them outside the first charge while leaving them in the airstream.)*

**[30]** The free-wheeling state is physically determinate: the rotor settles where net shaft torque is
zero. **The stopped state is not.** Stopping a rotor requires the stop to be produced by
something — motor holding torque, an electrical brake, a mechanical lock — and a stopped
fixed-pitch blade also has an azimuth, so "stopped" is a family of aerodynamic states rather than
one. Neither the means nor the azimuth is fixed by this study, and the drag figure quoted for the
stopped condition should be read as the state Section 11 defines rather than as the state a
particular installation would reach. The free-wheeling state needs no stopping means; the stopped state does, and if it were a
brake or a lock rather than motor holding torque, the count of Section 7 would gain a class.

