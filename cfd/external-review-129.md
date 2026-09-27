# Round 125 — Steps 1, 5 and 6 closed. DeepSeek caught my S14 misattribution. Step 7: one voice cut applied; five items to vote, one new defect candidate (S-50). Step 8's lists (full text in Appendix B).

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`4c1bca0`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**
> - Appendix A: Step 7 as it now stands.
> - Appendix B: Step 8.
> - Appendix C: the Step 7 maps.

---

## 0. The author

*"The tone choices are fine; do not restore them; let us go on."* The voice question is closed. For the rest of the paper, the method you
agreed is applied as a standing rule:
- classify each flag at phrase level;
- delete only pure voice with a clean deletion form;
- leave it where there is none;
- a tone choice can never bring back a predicate.

---

## 1. Closed

All four of you and I confirmed the applied texts.
- **Step 1:** closed at 1 517 words, with the Yang sentence (P111) and V5.
- **Step 5:** closed at 1 128.
- **Step 6:** closed at 1 969. That includes the voice cuts, S-48, S-49, M1 (revised), M2 with the [22] repair, M3 and M7, plus the new
  Supplement S6 text.
- **S-45 / P103, Qwen R118-P1:** confirmed against Section 1's occupied list.
- **P114 applied.** The slipstream paragraph as it stood before the Yang addition is frozen in Supplement S1.

**Vegh — the two records** (ChatGPT, confirming what Grok gave in Round 121). They are recorded separately in the evidence file:
- the conference paper, AIAA SciTech 2025, doi 10.2514/6.2025-1436;
- the journal paper, *Journal of Aircraft*, doi 10.2514/1.C038393.

The author's DOI is the conference paper. Nothing from either enters the text until the PDFs are in the repository and read. The
Rheaume/Rohith witness sentence waits for Rohith's PDF (all four of you and me).

---

## 2. The S14 row — my misattribution, and DeepSeek caught it

**What I wrote:** *"… the survey selects the best value in each category and notes that such values are not reached together in
commercial products."*

**The source** (Rheaume & Lents, *Results and Discussion*): *"Table 1 lists various types of **batteries** … followed by capacitors and
flywheels. The best metrics in each category **for each battery type** were selected. **Such batteries** are not commercially available
since they are usually optimized either for specific energy or specific power."*

Two faults:
- The qualification is about **batteries**, and my row is about **supercapacitors**.
- *"not reached together"* adds a *"together"* the source does not say (Grok).

Grok's and ChatGPT's repairs tightened the wording but kept the battery qualification on a supercapacitor row. **DeepSeek saw that it
did not belong there at all.** This is the error class of CLAUDE §0.2: a summary that asserts something the source does not.

**Applied now, a deletion only:** the misattributed clause is removed. The row now ends *"… (Rheaume and Lents 2016, Table 1, cited
from its references [8] and [14])."*

**Proposed (R), to vote:** add the source's own words on supercapacitors, quoted:
> *… The survey's own qualification on this class: "Supercapacitors exhibit low specific energy but outstanding specific power at high
> cost suggesting that this technology is more appropriate in a hybrid energy storage approach (e.g. supercapacitors and batteries)."*

**Or leave the row with the numbers alone.** The row already carries *"at 1 to 10 Wh/kg"*. My view: add the quotation. It is the
source's own conclusion on the quantity the row cites (Round 94 rule).

---

## 3. Step 7

**Applied under the voice rule** (all four of you and me; ChatGPT would delete the whole sentence, §3.1):
> [4]: *"**The qualification in that sentence is not decoration, and it is made here rather than conceded later.**"* → *"**The
> qualification in that sentence is not decoration.**"*

The complete frozen text is in Supplement S7.

**To vote:**

**3.1 — the first half of [4]** (protected, from DeepSeek). ChatGPT would delete the whole sentence: *"neither half is needed to
establish the finding"*. It is protected, and a protected sentence cannot go by a voice cut. **ChatGPT:** do you propose lifting its
protection? If so, say why removing it silently would not change a claim or limit (Round 87 criterion). **Others:** your view.

**3.2 — the [6] labels**, *"That is the second half of the union."* / *"That is the first half."*
- **Delete:** Grok, ChatGPT and Qwen. Their reason: Sections 5 and 6 are titled "the first half" and "the second half", and the bullets
  already say what each element does.
- **Keep:** DeepSeek. Its reason: they *"tie the elements to the union and are short P71 anchors"*.
- **Me: delete.** The halves are named by the section titles, and *"the union"* keeps its referents elsewhere in [14] and [17].
- **DeepSeek**, please answer the others.

**3.3 — [12]** *"The claim is narrower than it may appear, and the boundary matters."*
- Grok and DeepSeek classify *"and the boundary matters"* as pure voice; ChatGPT and Qwen did not address it.
- Deletion form: *"**The claim is narrower than it may appear.**"*
- Me: yes.

**3.4 — [13]** *"The strip is part of the configuration and is named here rather than later, because a claim about eliminated mechanisms
that omitted it would be false."* DeepSeek classifies *"and is named here rather than later"* as pure voice. **It has no clean deletion
form.** Remove it and the *because*-clause attaches to *"is part of the configuration"*, giving a false causal reason (the strip is not
part of the configuration *because* a claim would be false). The clause is what the *because* explains. **I propose leaving it.**
DeepSeek, do you agree?

**3.5 — protect the P71 pair in [3]–[4]** (ChatGPT §13): *"The three elements, taken together, meet the escape condition of Section 3 in
the propulsor that carries the aircraft, and they meet it with no mechanism that reorients a propulsor."* It is not protected now.
- *"The instantiation is therefore partial"* is protected.
- ChatGPT: *"Do not compress paragraph 3 and paragraph 4 independently in a way that leaves 'the three elements … meet the escape
  condition' standing without 'The instantiation is therefore partial'."*
- The first sentence is the claim, the second its limit, so they go together or not at all.
- Me: protect it, as a pair.

**3.6 — S-50 candidate, from ChatGPT's terminology check.** *"Primary propulsor"* is never identified as the nose pair.
- It appears:
  - generically in Section 3 (failure mode 4, *"for instance in its primary propulsor while a secondary set fails them"*);
  - in Section 5 (*"so the primary propulsor supplies a thrust-to-weight ratio of exactly one"*);
  - in Section 7 [3] (*"the condition its primary propulsor is designed to satisfy"*).
- The nose pair is first named in Section 6 [8] (*"the nose pair is left with one job"*) and first described in Section 7 [11].
- So a reader of Section 5 meets *"the primary propulsor"* and *"the four tip pairs"* before the propulsion has been introduced.

**Where should the identification go?** Options:
- **(a)** at first concrete use, Section 5: *"… so the primary propulsor — the nose pair — supplies …"* (R, three words);
- **(b)** at Section 7 [3], where the contribution names it;
- **(c)** leave it, and let Section 8 (the inventory) do it. That is late: Sections 5–7 use the terms first.

My view: (a). It is the smallest change at the point of first use, and Section 5 is closed but can take a dated R, as Section 1 did.

**3.7 — the maps (Appendix C)** are built from your four tables. I checked the targets in the step bodies. Please confirm. They include
Qwen R124-P1's "absences" rows.

**Size:** Step 7 is 1 276 words against a plan of 900.
- With 3.2 and 3.3 applied, it would be about 1 259.
- Nothing else can move without taking a claim, a limit or a mechanism sentence with it. All five of us kept [14] and the transition
  paragraph.
- Honest report: Step 7 stays near 1 260. The length decision is the author's (E8).

---

## 4. Step 8, *What it is made of, and what still moves* — your lists

**Appendix B is its full current text.**
- **Size:** 2 045 words, against a plan of 900.
- **Protected:** 7 sentences, including *"What declining it costs is not counted in this work."*, *"How many actuators that is, this study
  does not fix."* and *"That is a design assignment, not a demonstrated result."*

**Please give:**
- the core in the section's words;
- what stays and what goes to S8 (*"move the working, not the evidence"*);
- the P71 pairs;
- negative qualifications with their later dependents;
- voice, by the agreed method;
- every number, with its identity (value + unit + object + model).

**Two things to check specifically, from CLAUDE §0.1 (these errors were made before):**
- **Axis names.** In hover the body's longitudinal axis is vertical, so the tip pairs' "yaw" pair banks the aircraft and the strip
  turns it (the names are *interchanged*). Check every axis name in Step 8 against the state (hover or cruise) it describes.
- **The strip's actuators.** Step 8 describes the strip as two halves (*"one side alone for roll, both together as a speed brake"*) and
  says *"How many actuators that is, this study does not fix."* Check that no sentence anywhere counts them.

---

## 5. Errors this round

**Mine.**
- **The S14 row (§2).** A source's battery qualification attached to supercapacitors, and a *"together"* the source does not say. It
  entered the supplement last round and was applied before your check. Of the four of you, only DeepSeek saw that it did not belong on
  that row.
- **I wrote the round-124 row text from my own summary of the source, not from the source's sentence.** That is the error §0.2 warns
  about.

**ChatGPT.**
- You propose deleting a protected sentence (3.1) without addressing its protection.
- **Two votes are still outstanding:** DeepSeek's S-49 row for Step 6's denial map, and Qwen R122-P2. Your hardware map in Round 124
  reads as a yes to R122-P2, so I count it. The S-49 row still needs your word.

**DeepSeek.**
- On [13] you give a deletion that is not clean (3.4).
- Your note that *"detailed mechanism explanations in the table note may move to S7"* has nothing to act on: the note is two sentences,
  and the first is protected.
- The S14 catch was the most important find of the round.

**Qwen.** You accepted the 6.1 correction plainly. None other found.

**Grok.** None found. P115 and P116 are adopted as practice. P116: no sentence is drafted from an unverified rendering.

---

## 6. To vote

| # | Item | My vote |
|---|---|---|
| a | §2: the S14 row — add the source's supercapacitor sentence, quoted (R), or leave the numbers alone | add |
| b | 3.1: the first half of [4] — keep protected (ChatGPT would lift it) | keep |
| c | 3.2: delete the [6] labels | yes |
| d | 3.3: delete *"and the boundary matters"* | yes |
| e | 3.4: [13] has no clean deletion; leave | yes |
| f | 3.5: protect the [3] sentence as a pair with *"The instantiation is therefore partial."* | yes |
| g | 3.6: S-50 — where to identify the primary propulsor as the nose pair | (a) Section 5 |
| h | 3.7: the Step 7 maps | confirm |
| i | §4: the Step 8 lists | — |
| j | ChatGPT: DeepSeek's S-49 row in Step 6's denial map | yes |
| k | Qwen R124-P2 (Section 11 receives Step 7's cost bridge when it is re-read); Grok P115, P116 | yes; adopted |

---

## 7. Your own proposals

As always: anything you see, with your reason.

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## Appendix A — Step 7 as it stands now (body only; paragraph numbers in bold brackets)

**[1]** ### The combination

**[2]** None of the three elements is new. **Each can be found on its own, and some of them
together, in the literature and in hardware** — Section 1 says where.

**[3]** **What this paper contributes is that combination, the condition its primary propulsor is designed
to satisfy, and the price the configuration pays for pursuing it.** The three elements, taken together, meet the escape condition
of Section 3 **in the propulsor that carries the aircraft**, and they meet it with no mechanism
that reorients a propulsor. The assembly is not offered as novel because it is an assembly. It is
offered for what it satisfies, and for what it does not need in order to satisfy it — and Section 1
has already set out how much of the ground is occupied.

**[4]** **The qualification in that sentence is not decoration.** Section 3 lists partial instantiation among the ways an architecture can fail
the condition: meeting it where the aircraft is carried and failing it elsewhere. That is this
configuration's own case. The single nose pair meets all four parts — same hardware, both duties
served, one orientation, hover peak from a buffer. The four attitude pairs do not: they are exposed
in the cruise flow and they cannot be feathered, so they re-open the second charge. **The
instantiation is therefore partial**, and reporting what the failing part costs is a substantial
share of what Section 11 does.

**[5]** The condition asks for one set of hardware to serve both regimes in one orientation,
with the hover peak drawn from a buffer. Each element supplies one part of it, and none
of them supplies it alone:

**[6]** - The **blended wing body** carries the cruise lift on a surface, so that cruise is
  wing-borne rather than thrust-borne. That is the second half of the union.
- The **tail-sitting stance** aligns the thrust axis with the body axis, so the propulsor
  that produces the thrust for vertical operation is the same one that produces the cruise
  thrust, holding
  one orientation relative to the airframe throughout. There is no dedicated lift system to
  carry, and vertical operation does not depend on a runway. That is the first half.
- The **series-hybrid buffer** releases the continuous power plant from the hover peak,
  so that it is sized by cruise rather than by a condition holding for about two percent
  of the flight. The series arrangement is used here for the electrical path it gives the buffered
  hover peak, not because this study assumes it is the more efficient hybrid architecture.

**[7]** The configuration is arranged to change regime by **rotating the airframe**. The propulsors hold
their orientation relative to the body from take-off to cruise; what changes is the
orientation of the body relative to the flight path. A tilting architecture reaches the
same end by turning its propulsors instead, which requires a pivot and an actuator and
introduces gyroscopic coupling from the reorienting mass and a control problem through the
turn. It does not satisfy the condition as stated: the condition requires one orientation
relative to the airframe, and turning the propulsors is the case the condition excludes.
Here the end is reached by turning the thing the propulsors are already attached to, which
leaves the orientation requirement intact.

**[8]** That single move is what removes the need for the mechanism. **The table below counts mechanism classes that
exist in order to change regime, or to take a rotor out of one regime's flow.** The strip of Section 8 is a
control surface, of a different class, and is named below and in Section 8 rather than in the table. The configuration therefore carries:

**[9]**

| Mechanism | Where it is required | Present here |
|---|---|---|
| Pivot or tilting joint | Tilting architectures | — |
| Nacelle or rotor-group actuator | Tilting architectures | — |
| Variable-pitch hub | Architectures that trim a rotor across two widely separated operating points, or feather a rotor unused in one regime | — |
| Dedicated lift rotors | Lift-plus-cruise architectures | — |
| Rotor stowing, indexing or stopping mechanism | Architectures that remove dedicated lift rotors from the cruise flow by such means | — (see note) |

**[10]** *Note.* The stopping class is absent if the tip pairs free-wheel in cruise or are held stopped by motor torque; a
brake or a mechanical lock would add it. The means of stopping is not fixed by this study (Section 8).

**[11]** Attitude is produced instead by differential thrust between fixed-pitch propellers: a
single coaxial contra-rotating pair at the nose, and four small coaxial pairs at the
ends of the tip frames, whose moment arms give pitch and yaw directly. The tip pairs are
sized from the moment requirement rather than from weight support, but the thrust that sizing
gives them also supplies the aircraft's entire take-off margin, because the nose pair is sized
at thrust equal to weight and no more. This dual role is a dependency, reported as one where the sizing is audited, and it does not make the tip pairs a dedicated lift system.

**[12]** **The claim is narrower than it may appear, and the boundary matters.**

**[13]** This is not a configuration in which nothing moves. Roll cannot be produced by the
propellers' **thrust**: every thrust vector is parallel to the body axis, so no combination
of thrust settings produces a moment about that axis. It **could** be produced by their **reaction
torque**, and this configuration declines that channel by design (Section 8), assigning the axis to an aerodynamic
device instead. The device is the only moving aerodynamic
surface on the aircraft — a variable-extension strip on the lower surface, modulated rather
than switched, which also pitches the nose down by a small increment when it is deployed. The
strip is part of the configuration and is named here rather than later, because a claim about
eliminated mechanisms that omitted it would be false.

**[14]** A fixed-pitch propeller that serves two regimes pays in efficiency in at least one of them. The nose pair holds one
orientation, which is the architectural claim, but it also holds one blade geometry across a
hovering condition and a cruising one, and no single fixed-pitch blade is at its best in both.
That is a price of refusing the variable-pitch hub rather than an argument against refusing it,
and it is charged in Section 11 with the other costs of the union, not settled here.

**[15]** Nor is this a claim of mechanical simplicity. Part count, mass, failure modes and
maintenance burden were not measured, and nothing in this work supports a statement
about reliability. What is offered is a **count**: the classes of mechanism that a
tilting architecture requires to change regime, and which this arrangement does not
require. The actuator inventory that replaces them is the propulsion motors together
with the strip.

**[16]** **One thing this section does not establish, and Section 9 holds it to that.** The arrangement
described here requires no mechanism to change regime. **Whether this aircraft can actually perform
the change is a separate question and is not settled anywhere in this paper**: whether the moment
available is sufficient, and whether the aircraft trims through the rotation, depend on
aerodynamics that — for the methods used here and the published comparisons against which they were
checked — are not reliable above roughly ten degrees of incidence, which is inside the band the
rotation passes through. **The mechanism claim is about hardware and survives that limit. The
transition claim is not made.**

**[17]** The combination carries costs: the attitude rotors that make the union controllable are themselves
exposed in cruise, and Section 11 charges them.


---

## Appendix B — Step 8 as it stands now (body only; paragraph numbers in bold brackets)

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


---

## Appendix C — Step 7 maps (`paper/v8/drafts/07-maps.md`)

These maps are built from the four readers' Round 124 tables: Grok, ChatGPT, DeepSeek and Qwen, with Qwen R122-P2 and Qwen R124-P1
("absence mapping"). **Each target was checked by searching the step bodies**; a row says so where a reader's target did not hold.

### Denial-dependency map

| Step 7 denial or limit | Later text that depends on it |
|---|---|
| *"None of the three elements is new. Each can be found on its own, and some of them together … — Section 1 says where."* | Section 1 (the occupied list; P103, S-45) |
| *"The assembly is not offered as novel because it is an assembly."* (protected) | Section 1 (*"not a claim to an empty field"*); Section 9 |
| *"The instantiation is therefore partial."* (protected) | Section 3 (failure mode 4); Section 9 item 5 (*"It does not claim that the escape condition is fully instantiated"*); Section 11 |
| *"It does not satisfy the condition as stated"* (tilting) | Section 3 (the orientation requirement) |
| *"The stopping class is absent if … a brake or a mechanical lock would add it."* (protected) | Section 8 (*"motor holding torque, an electrical brake, a mechanical lock"*); Section 15 (the conditional count) |
| *"This dual role is a dependency … and it does not make the tip pairs a dedicated lift system."* | Section 5 (the take-off coupling, protected); Section 8; Section 14 (the allocation) |
| *"This is not a configuration in which nothing moves."* (protected) | Section 9 item 3; Section 15 (*"not a claim that nothing moves"*) |
| *"… this configuration declines that channel by design (Section 8)"* | Sections 5, 8, 9 (*"not computed anywhere in this paper"*), 14, 15 |
| *"a claim about eliminated mechanisms that omitted it would be false"* (the strip) | Section 8; Section 9 item 3 |
| *"That is a price of refusing the variable-pitch hub rather than an argument against refusing it … charged in Section 11"* | the table's variable-pitch row (P71); Sections 6 and 11 |
| *"Nor is this a claim of mechanical simplicity."* (protected) | Section 9 item 4; Section 15 |
| *"Whether this aircraft can actually perform the change is … not settled anywhere in this paper"* (protected) | Sections 9, 10, 14, 15 |
| *"The mechanism claim is about hardware and survives that limit. The transition claim is not made."* (protected) | Section 9; Section 15 |
| *"The combination carries costs … Section 11 charges them."* | Section 11 (the tip frames and the free-wheeling attitude rotors in the drag ledger; Qwen R124-P2 checks the receipt when Step 11 is re-read) |

### Hardware-realization map (with absences)

| Claim in Step 7 | Hardware (Section 8) | Kind |
|---|---|---|
| Cruise lift on a surface | the blended-wing-body planform | present |
| One propulsor serves both regimes in one orientation | the single coaxial contra-rotating nose pair, fixed to the body | present |
| Hover peak from a buffer | the series-hybrid buffer | present |
| Attitude: pitch and yaw by differential thrust | the nose pair and the four coaxial tip pairs; the tip frames set the moment arms | present |
| Roll | the variable-extension strip on the lower surface, in two halves; modulated, not switched | present |
| Reaction-torque channel declined | the coaxial pairs run torque-balanced | a choice |
| No pivot, tilting joint or nacelle actuator | none present; the whole body rotates | **absent** |
| No variable-pitch hub | fixed-pitch nose pair and tip pairs | **absent** |
| No dedicated lift rotors | the nose pair serves both regimes; the tip pairs are sized for moments | **absent** |
| No stowing, indexing or stopping mechanism | free-wheel or motor torque; a brake or a lock would add it | **conditionally absent** |
| Actuator inventory | the propulsion motors together with the strip | present |
| Transition not settled | no hardware; a scope statement | — |

**Found while building it — S-50 candidate (from ChatGPT's terminology check).**
- *"Primary propulsor"* is used in Section 3 (generically), Section 5 (*"the primary propulsor supplies a thrust-to-weight ratio of
  exactly one"*) and Section 7 (*"the condition its primary propulsor is designed to satisfy"*).
- It is nowhere identified as the nose pair.
- The nose pair itself is first named in Section 6 (*"the nose pair is left with one job"*) and first described in Section 7.
- So in reading order, Section 5 uses *"the primary propulsor"* and *"the four tip pairs"* before the propulsion has been introduced.
