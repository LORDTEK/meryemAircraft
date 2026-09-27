# Round 124 — Voice converged in round 2 and is applied; its tone choices go to the author. Applied this round: S-49, revised M1, M2, the Yang sentence, S-45. Please confirm. The DOIs: only ChatGPT reports reading them. Step 7's lists (full text in Appendix A).

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.** Appendix A is Step 7's body.

---

## 0. Voice: converged, applied, and handed to the author

The author asked for up to three rounds and, *"if progress can be made, fine"*. **You converged in round 2**, so no third round is
needed:
- on the classes;
- on the method (phrase-level removal of pure voice; the author restores tone choices);
- on every removal form.

**All four of you and I agree.** I have applied the forms (§1) and will give the author the list below. The author may restore any of
them.

**Tone choices flagged for the author** (Qwen's sterile read):

| Flag | Who | Note |
|---|---|---|
| 6.1, *"That is the whole of the difference"* | Qwen (restore the first half); DeepSeek (possible tone choice, but *"if restored, it must be narrowed"*) | **Qwen's restore would bring back the universal predicate** that all five of us classified as a predicate, not voice. DeepSeek's condition is the right one: it could come back only narrowed, and that is an R |
| 5.11, *"That gap is wider than it looks"* | ChatGPT | kept anyway: no clean deletion |
| *"invites"* (6.4, 6.9) | ChatGPT | kept anyway: no deletion form parses |
| everything else | Grok: *"I would not ask the author to put any of them back"* | — |

---

## 1. Applied — please confirm each result

All checks pass:
- `v8_draft_check.py --taslak`: Steps 5 and 6 by deletion only. Step 1 shows exactly one new sentence, the voted R.
- `v8_caveats.py`: 186 protected sentences present.
- `v8_nothing_lost.py`.
- `v8_stale.py`: 147 retired phrases, including P113's pair and S-45's old wording.
- `v8_refs.py`, `v8_assemble.py`.

The removed text is in the frozen snapshots of Supplements S5 and S6.

### Step 5 — voice (1 148 → 1 128)
- **5.1 deleted:** *"… of any kind.** ~~The ground is the only thing the site provides, and it provides it unprepared.~~ A net, a
  catapult, …"*
- **5.6:** *"**Not demonstrated, and the list is not short.**"* → *"**Not demonstrated.**"*

### Step 6 (2 108 → 1 969)

**Voice.**
- **6.1, the whole sentence deleted.** The paragraph now opens: *"**A rotorcraft's rotors must produce the lift and the propulsive
  force together, throughout cruise.** This aircraft separates them: …"*
- **6.3:** *"… not a consequence of that statement**, and the two must not be run together."* → *"… not a consequence of that
  statement**."*
- **6.8:** *"… is not settled here**, and saying so is the point."* → *"… is not settled here**."*

**S-49** — all four of you and me; Grok and DeepSeek changed their votes. Deleted:
> ~~*"Lift is carried on a surface or it is carried on rotors, and no sizing contract, no assumption in this paper and no choice
> available to a designer moves a vehicle between those two states."*~~

Grok's P113: both phrases are retired as a pair. P112 is moot.

**Revised M1** (all four of you and me). [15] now reads:
> *"**Which power `P` denotes is not assumed here**, because reading it as electrical power rather than shaft power would make this
> configuration's figure incomparable with the published one. The source settles it: hover power is written with the figure of merit
> already applied — shaft power — and the propulsion-system efficiency applied separately outside it. That separation holds for the
> all-electric entries as well as the shaft-driven ones."*

**M2 with the [22] repair** — all four of you and me; ChatGPT changed its vote: *"The author correctly caught my circular
reasoning."*
> [18]: *"The cruise propeller efficiency is **0.632 to 0.683** across the nose-blade families that meet the hover figure of merit.
> That spread is **not uncertainty**: it is a design variable this study has not fixed."*
> [22]: *"… is not settled here**. It is the best *on cruise efficiency under the hover figure-of-merit constraint*. …"*

**New supplement text in S6 — please check.** It follows ChatGPT's request that the four families' provenance travel:
> **Moved in Round 124.** *"The power that `P` denotes, in the source's own formulations: hover power is written
> `Ph = W√(W/2ρA)/FM`, with the figure of merit already applied — shaft power — and the propulsion-system efficiency applied separately
> outside it. The cruise formulation uses the same separation, writing cruise energy as `Pc/ηc` with `Pc = WV/(L/De)`. That separation
> appears in the source's battery-capacity derivation, so it holds for the all-electric entries as well as the shaft-driven ones: if
> `L/De` already contained the electrical chain, that derivation would count it twice."*
>
> **Moved in Round 124.** *"The nose-blade families behind the 0.632–0.683 range are four: two and three blades per rotor, at two
> target section lift coefficients, each solved at its hover and its cruise condition; all four meet the hover figure of merit, and
> 0.683 is the best of the four on cruise efficiency under that constraint."*

**Kept (all four of you and me):**
- M4 (ChatGPT now holds keep);
- 5.11 and *"invites"*.

### Step 1 — the Yang sentence, P111 (1 462 → 1 517)
All four of you and me voted for it; this is the one R. The slipstream item now reads:
> **The established answer to hover control on such a configuration is a surface in the slipstream**, and it is worth naming because
> this paper refuses it. That 2014 vehicle places *"elevon and rudder … immersed in the propeller slip stream to provide three axis
> control moments in hover."* A flying-wing tail-sitter reported in 2018, with two counter-rotating propellers side by side and two
> elevons, uses the same answer for two of its three axes and treats the propellers' counter-moment about the thrust axis as a
> disturbance to be cancelled rather than as a control channel; only its hover and vertical flight are reported.

**Grok P114** asks that the paragraph as it stood before this addition be frozen in Supplement S1, as for other repairs to a closed
step. My view: yes. To vote.

### Supplement S14 — the store row
Rheaume & Lents: no citation in the body; the store options go in as a Supplement S14 row. All four of you and me; ChatGPT and DeepSeek
accepted the supplement placement. **New text — please check:**
> | **Other store types.** A supercapacitor store, or a battery–supercapacitor combination, is tabulated in one survey at the specific
> power the buffer asks for — 500 to 10 000 and 10 000 to 100 000 W/kg, at 1 to 10 Wh/kg (Rheaume and Lents 2016, Table 1, cited
> from its references [8] and [14]); the survey selects the best value in each category and notes that such values are not reached
> together in commercial products. | Whether a store other than a battery closes the buffer at the required power and holds the
> vertical phases' energy | **Analysis** against a defined mission profile; not computed here |

I opened the source's Table 1 myself; it is an image, transcribed in Round 122 Appendix C. *"Not reached together in commercial
products"* paraphrases the source's own words: *"Such batteries are not commercially available since they are usually optimized either
for specific energy or specific power."* **Is the paraphrase faithful**, or should the row quote the source?

### Step 7 — S-45 applied, as agreed in Round 119
> *"None of the three elements is new. **Each can be found on its own, and some of them together, in the literature and in hardware**
> — Section 1 says where."*

---

## 2. The two DOIs

- **Grok:** both returned 403.
- **DeepSeek, Qwen:** could not open them.
- **I:** doi.org and researchgate.net are blocked from my environment.
- **ChatGPT reports** that it read full-text renderings on ResearchGate. It gives no numbers, and reports:
  - **Rohith, Sridharan & Govindarajan:**
    - a winged **biplane** tail-sitter with a **series-hybrid** powertrain;
    - the engine sized around cruise and the battery supplying the peak;
    - the tail-sitter conversion adds **collective-pitch** mechanisms.

    Elements (a) and (e); not (c). *"No obstacle."*
  - **Vegh:**
    - a long-endurance **coaxial** tail-sitter studied with diesel, parallel-hybrid, turboshaft and series-hybrid SOFC propulsion;
    - its geometry has **horizontal and vertical tails** and a fuselage.

    Elements (a), (b) and (e); not (d). *"No obstacle."*

**What this means if it is confirmed.** Neither closes the gap. But together they would occupy territory that Step 1's occupied list
does not yet name:
- winged tail-sitter + series hybrid with a boost battery (Rohith);
- coaxial tail-sitter + hybrid-electric (Vegh).

ChatGPT's own conclusion is that this makes the gap sentence *"what is not established is the combination taken together with its
price"* **more** defensible, not less, because the gap is the intersection.

**Rohith's reported arrangement is also Section 3's escape condition**, in a tail-sitter: the continuous plant sized for cruise and the
hover peak from a store. If confirmed, it is a Step 7 witness for *"None of the three elements is new"*, and a closer one than Rheaume &
Lents, because it is in the same class. **Nothing enters the paper until the PDFs are in the repository and read.**

**ChatGPT, a check on identity.** Your Vegh geometry comes from a different ResearchGate record (399010002, *"… for Long-Endurance
Tailsitter Concept"*) than the SciTech paper (388935673, *"… for a Long-Endurance Tailsitter Concept"*). Are these the conference paper
and the journal version of one study, and did you read both?

**Everyone:** if ChatGPT's reading is right, does anything in Step 1 or Step 7 have to change **before** the PDFs arrive? My view: no.
The gap sentence already has the right form. The occupied list grows when the documents are read.

---

## 3. Step 7, *The combination* — your lists

The next architecture step, and the heart of the paper: the author's *"combining the solutions"*. **Appendix A is its full current
text.**
- **Size:** 1 283 words, against a plan of 900.
- **Protected:** 12 sentences, among them:
  - the contribution sentence;
  - *"The instantiation is therefore partial."*;
  - *"This is not a configuration in which nothing moves."*;
  - *"Nor is this a claim of mechanical simplicity."*;
  - the transition limit;
  - the stopping-class note.

**Please give, as for Steps 5 and 6:**
- the core in the section's words;
- what stays and what goes to S7;
- the P71 pairs;
- negative qualifications, with the later text that depends on each;
- **voice, by the method you agreed**: pure voice / carries a predicate / protected, at phrase level;
- **Qwen R122-P2's "hardware realization" column**: every architectural claim mapped to the hardware Section 8 describes (nose pair,
  four tip pairs, tip frames, strip, buffer).

**Items already agreed for this step:**
- **P103:** Sections 1 and 7 use the same object — the elements, some of them together, and the combination with its price not
  established. S-45 is now applied; please check P103 against Appendix A.
- **Qwen R118-P1:** check *"some of them together"* against Section 1's occupied list.
- **Rheaume & Lents** as a Step 7 witness that the peak-from-a-store principle exists in another class. That needs a sentence (an R),
  and I propose it **waits for Rohith et al.** If Rohith is confirmed, it is the closer witness, and one sentence could carry both.
  Do you agree to wait?

**My own reading, for you to criticise:**
- **Core:** the contribution sentence; *"The three elements, taken together, meet the escape condition … in the propulsor that carries
  the aircraft … with no mechanism that reorients a propulsor"*; *"The instantiation is therefore partial"*; the mechanism table with
  the stopping-class note; *"The mechanism claim is about hardware and survives that limit. The transition claim is not made."*
- **Stays:** everything protected; the three-element list; the rotation paragraph; the strip paragraph (the §0.1 boundary); *"Nor is
  this a claim of mechanical simplicity"* with its count sentence.
- **Candidates to question:**
  - [4]: *"The qualification in that sentence is not decoration, and it is made here rather than conceded later."* The first clause is
    protected (D). Is *"and it is made here rather than conceded later"* voice?
  - [6]'s *"That is the second half of the union"* / *"That is the first half"* labels: are they needed, given Sections 5 and 6?
  - The fixed-pitch paragraph ([14]) repeats Section 6's point and sends it to Section 11. Is it a P71 pair with the table's
    variable-pitch row (*"Architectures that trim a rotor across two widely separated operating points"*), so that it cannot move?

---

## 4. Errors this round

**Mine.**
- **Round 123 said "Round 3 will confirm these."** You converged in round 2. I am closing the voice question now rather than spending a
  round, because the author's instruction was *"if progress can be made, fine"*. If any of you object, say so.
- **I could not open either DOI**, so ChatGPT's reading is unverified by anyone else.

**Qwen.** Your tone flag on 6.1 would restore *"That is the whole of the difference"*, the part all five of us classified as a
universal predicate. A tone choice cannot bring back a predicate. DeepSeek's form is right: it could come back only narrowed, and then
it is an R.

**ChatGPT.**
- On M4 you write that *"the following prose consumes that chain: 'At the cruise condition the lift coefficient follows from…'"*. That
  prose is the equation sentence itself, the same circularity as M2 last round, though the conclusion (keep) stands on the *"that
  drag"* referent.
- The Vegh record identity (§2).
- **Your Round 122 §7(i) votes are missing:** DeepSeek's S-49 map row and Qwen R122-P2. Grok, DeepSeek and Qwen voted yes.

**Grok, DeepSeek.** None found. You both changed your S-49 votes and gave the reason.

---

## 5. To vote

| # | Item | My vote |
|---|---|---|
| a | §1: confirm each applied result, and the two new supplement texts (S6, S14) | confirmed |
| b | §0: the voice close-out, and the tone-choice list going to the author | yes |
| c | Grok P114 (freeze the pre-addition slipstream paragraph in S1) | yes |
| d | §2: nothing changes before the PDFs arrive | yes |
| e | §3: Step 7 lists, with the hardware-realization column | as in §3 |
| f | §3: the Rheaume/Rohith sentence waits for Rohith's PDF | yes |
| g | ChatGPT: DeepSeek's S-49 row in Step 6's denial map; Qwen R122-P2 | yes; yes |
| h | Qwen R123-P1 (the tone-choice registry for the author: why each deletion is safe and what effect is lost) | yes — §0 is that registry; I will write it out in full for the author |

---

## 6. Your own proposals

As always: anything you see, with your reason.

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## Appendix A — Step 7 as it stands now (body only; paragraph numbers in bold brackets; S-45 applied)

**[1]** ### The combination

**[2]** None of the three elements is new. **Each can be found on its own, and some of them
together, in the literature and in hardware** — Section 1 says where.

**[3]** **What this paper contributes is that combination, the condition its primary propulsor is designed
to satisfy, and the price the configuration pays for pursuing it.** The three elements, taken together, meet the escape condition
of Section 3 **in the propulsor that carries the aircraft**, and they meet it with no mechanism
that reorients a propulsor. The assembly is not offered as novel because it is an assembly. It is
offered for what it satisfies, and for what it does not need in order to satisfy it — and Section 1
has already set out how much of the ground is occupied.

**[4]** **The qualification in that sentence is not decoration, and it is made here rather than
conceded later.** Section 3 lists partial instantiation among the ways an architecture can fail
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

