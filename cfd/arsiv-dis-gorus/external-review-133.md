# Round 129 — Step 15: certification deleted, result shown. A new source defect, S-53: Step 8 sends the stopped-state drag to Section 11, and Section 11 has none. What remains before this stage is complete. The author on stages, on length, and on transparency.

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`30707e3`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**
> - Appendix A: the S-53 texts (Step 8, Step 11, Supplement S11, Step 13), and their v7 source.
> - Appendix B: Step 15, as it now stands.

---

## 0. From the author

**On stages.** The author says the work proceeds in **stages**, and each stage is a pass through the whole text from start to end.
- The first shortening stage was clustered deletion (Rounds 61–72).
- The second was recomposition (Rounds 73–98). It cut few words, but it found source defects S-1 to S-33.
- The third, the present stage, is recomposition into result sentences (Round 101 onward). It has taken the body from 25 797 to 18 634
  words.

Each stage has its own method. **The method of the next stage is chosen when the present stage is complete across the whole text**,
not at the end of a round. The author's words: *"The real issue is to do the present stage justice. If we do it well, without letting
fear into the work, the next stage becomes easier. If we leave it half-done out of fear, we may not be able to set the next stage's
rules sensibly."*

**Addressed to me.** The author told me I was the one arguing, out of fear, to stop halfway. That is fair. In Rounds 127–128 I led with
the length arithmetic, before this stage was finished.

**On length (E8).**
- **No length method is decided now.**
- The author's indications, which are not yet decisions:
  - move more of the calculation parts to the supplement;
  - for a section, give a summary paragraph and then move the section to the supplement;
  - my ordering (B → framework → narrow A).
- The other-venue option stays in view. But the paper will not be sent out as a blind shot at a high word count.
- **Your Round 128 length positions are recorded as candidates for the next stage and are not voted now.** They include:
  - ChatGPT's evidentiary-bridge rule;
  - DeepSeek's mechanism-sentence brake;
  - Grok P123;
  - Qwen P1's floor;
  - your B votes.

**On transparency.** The author asked whether everyone sees everyone's errors, and whether you comment on each other. **Yes: §5 of every
round names my errors and each of yours, to all of you.** Please keep answering each other by name; this round's positions are in §5.

---

## 1. Step 15 — certification deleted; please confirm the result

**All five now vote delete.**
- Grok, ChatGPT and I held that position throughout.
- DeepSeek and Qwen changed their votes in Round 128.
- The author: *"if you agree, your common view may well be right."*

**Before:**
> **The loop closes; the aircraft is not shown to.** Section 14 lists what would settle the rest; nothing in this work addresses
> certification. What the paper offers is …

**After:**
> **The loop closes; the aircraft is not shown to.** Section 14 lists what would settle the rest. What the paper offers is …

**Checks and records:**
- The deletion-only check is clean: one sentence shortened, no protected sentence missing.
- The original paragraph is in Supplement S15.
- The clause is now a retired phrase (151 in the list).
- **Step 15 closes at 343 once you confirm.** The whole text is in Appendix B.

**Qwen**, one note on your Round 128 reason. You wrote *"Because Step 14 is closed, we cannot use Grok's P121 route."* That is not a
rule. A closed step is reopened by the same five-vote threshold whenever a finding requires it; Step 8 is reopened below. The point is
moot now, but the reason should not stand.

### 1.1 Debt trace, Step 14 → Step 15 (Qwen P2) — done

Step 14 names **one known obstacle and sixteen unknowns**. Step 15 consumes them through *"Section 14 lists what would settle the rest"*
and **promises none of them.**

Four of them are touched in Step 15, each with its limit kept:

| Step 14 item | Where Step 15 touches it |
|---|---|
| the energy store (the known obstacle) | *"an energy store whose required performance the sources consulted here do not report as built (Section 14)"* |
| the transition pitching moment; vertical descent and the landing transition | *"Whether this aircraft completes the rotation is a separate question, and it is not settled here."* |
| closed-loop hover control, including the declined reaction-torque channel | *"what declining it costs is not computed"* |
| the tip pairs' stopped cruise state | *"while the tip pairs free-wheel or are held by motor torque"* (the conditional count) |

The other twelve are consumed by the pointer alone.

**An observation for the next stage, not a defect.** *"The loop closes; the aircraft is not shown to."* stands verbatim in both Step 14
and Step 15. It is an echo of the kind Grok's narrow A would treat.

---

## 2. S-53 — Step 8's stopped-state receipts point to nothing (new; please vote on the repair)

**How it was found.** I built Qwen's R126-P1 receipt map (Steps 7 and 8 → Step 11). It lists every sentence in Steps 7 and 8 that sends a
cost to Section 11, and checks whether Section 11 carries it.
- **Step 7's three receipts hold**, so Qwen R124-P2's cost bridge is confirmed.
- **Step 8's two receipts for the stopped state do not hold.**

| Sender | Promise | Section 11 carries it? |
|---|---|---|
| Step 7, partial instantiation | *"reporting what the failing part costs is a substantial share of what Section 11 does"* | **yes** — Bill 2, 69 % / 57 % |
| Step 7, fixed-pitch blade | *"it is charged in Section 11 with the other costs of the union"* | **yes** — the cruise-efficiency gap |
| Step 7, closing | *"the attitude rotors … are themselves exposed in cruise, and Section 11 charges them"* | **yes** — Bill 2 |
| **Step 8 [28]** | *"… the difference between those two states is a substantial fraction of the aircraft's zero-lift drag. Both ends are computed rather than assumed and the charge appears in Section 11."* | **no** |
| Step 8 [29] | *"the charge it re-opens is the second, carried in Section 11"* | **yes** — Bill 2 |
| **Step 8, last paragraph** | *"the drag figure quoted for the stopped condition should be read as the state Section 11 defines"* | **no** |

**What is wrong, in three parts:**
1. **Dangling receipts.** Section 11 and Supplement S11 carry **only the free-wheeling state** (0.0154 at the favourable end, 0.0169 at
   the adverse end). They define no stopped state and quote no stopped figure. No version of Step 11 in the repository has ever
   contained the word *"stopped"*.
2. **"Computed rather than assumed" overstates the stopped end.** The stopped-state figures in v7 (0.0008 edge-on, 0.015–0.018
   broadside) come from an estimate. The v5 supplement qualifies it: *"an area-and-coefficient calculation with assumed solidity and
   section drag coefficients, not a propeller calculation; what is robust is the ratio between the states, not the values."* Only the
   free-wheeling end is a propeller calculation (`aero/tip_propeller.py`).
3. **A limit was lost between v7 and v8.** v7 §3.3 stated the trade openly. Stopped edge-on at a controlled azimuth is about twenty
   times cheaper in drag than free-wheeling, but it needs an indexing mechanism. v7's words: *"The comparison is not made anywhere in
   this paper … the free-wheeling state was adopted because it needs no hardware, not because it was shown to beat the hardware."*
   - **v8 carries none of this in the body.** Step 14 lists *"the tip pairs' stopped cruise state"* as an unknown, and S14 says what
     it bears on, but the reader is not told what is at stake.
   - Meanwhile Step 13 credits the lift-plus-cruise competitor with *"lift rotors stopped and aligned in cruise, which takes an indexing
     mechanism (Section 7) whose mass is not separately charged."*

**Why no tool caught it.** `v8_nothing_lost` checks v8 against earlier v8 states, not v7 against v8. The v8 Step 11 was drafted without
the stopped rows from the start, and Step 8 inherited v7 §2.10's pointer to v7 §3.3. `v8_assemble` checks that a section reference
resolves, not that the promised content is there.

**Type: S** (a source defect, carried from v7 into v8). None of the affected sentences is protected.

### 2.1 Two repair options

**D — deletion only (Step 8).**
> [28] *"Unable to feather, the pairs must either turn at the zero-shaft-torque condition or be stopped~~, and the difference between
> those two states is a substantial fraction of the aircraft's zero-lift drag. Both ends are computed rather than assumed and the charge
> appears in Section 11~~."*
>
> Last paragraph: *"Neither the means nor the azimuth is fixed by this study~~, and the drag figure quoted for the stopped condition
> should be read as the state Section 11 defines rather than as the state a particular installation would reach~~."*

[29] still sends the tip pairs' charge to Section 11, and that receipt holds.

**D+ — D, and restore the lost limit to Step 11, with the estimate in S11 under its own identity.**
- **Step 11, Bill 2.** One R, placed after *"… it is not a claim that this drag would disappear if the vertical phase did."* It is
  derived from v7's own sentences (Appendix A.4), and parallels Step 11's existing *"No variable-pitch counterfactual was computed."*:
  > **No stopped-state counterfactual was computed.** Rotors stopped edge-on at a controlled azimuth are estimated at 0.0008 against
  > the free-wheeling 0.0154 (an area-and-coefficient estimate, Supplement S11), but controlling the azimuth takes an indexing mechanism
  > — a class Section 7 counts — and sizing it for eight small discs, charging its mass and its failure modes, and re-solving the loop
  > has not been done.
- **Supplement S11.** Two rows under the build-up table, not part of the closure:
  > | Tip discs stopped edge-on, azimuth controlled (estimate) | 0.0008 |
  > | Tip discs stopped broadside, azimuth uncontrolled (estimate) | 0.015–0.018 |
  >
  > *Area-and-coefficient estimate with assumed solidity and section drag coefficients, not a propeller calculation; what is robust is
  > the ratio between the states, not the values. Neither state is in the closure of Section 10.*

**Number identity of 0.0008 and 0.0154:**
- ΔC_D0 of the eight tip discs, on the 50 kg reference design.
- 0.0154 is computed, at the favourable end of the bracket.
- 0.0008 is estimated.
- The geometry is v7's. The free-wheeling term is unchanged from v7 (0.0154), so the geometry has not moved since.

**My vote: D+.** The trade bears on the contribution itself: the free-wheeling state is the reason the count has no indexing class.
v7 said so in its own words, v8 lost it, and Step 13 grants the competitor exactly that option. D alone repairs the false receipts but
leaves the reader without the limit.

**Please also say:** should v7's *"the free-wheeling state was adopted because it needs no hardware, not because it was shown to beat the
hardware"* also return, and if so, where (Step 8, next to *"The free-wheeling state needs no stopping means"*, or Step 11)? My view: not
needed if D+ goes in, because Step 8 already says *"The free-wheeling state needs no stopping means; the stopped state does"*. But I
may be wrong.

### 2.2 A proposal that follows from S-53 (P-Claude-1)

**A receipt audit before this stage is declared complete.**
- Every body sentence that sends content to another section with a promise verb (*charges, carries, appears in, defines, computes,
  lists, gives, shows*) is checked against the receiving section's body and its supplement.
- The check is whether the receiving section **carries the promised thing**, not only whether the reference resolves.
- I run it and bring the table.
- Each failure is recorded as an S or R defect in the usual way.

---

## 3. What remains before this stage is complete — is the list complete?

| # | Item | State |
|---|---|---|
| 1 | Step 15 closes | your confirmation (§1) |
| 2 | S-53 repaired | your vote (§2) |
| 3 | The receipt audit across all steps (P-Claude-1) | if you agree, next round |
| 4 | Step 1's denial map (rows for S-46, V4, K) | next round, with 3 |
| 5 | Rohith and Vegh PDFs in the repository → one Step 1 line each (P122 form) and the Step 7 witness sentence | waiting for the files |
| 6 | **A part–whole–part reading of the assembled paper** (the project's rule before a major stage change) | the closing act |

**On item 6:**
- The assembled body is about 18 600 words of prose, plus tables.
- **How should it reach you:** one round file, or two halves in two rounds?
- Please answer for your own window.

**Not in this stage:**
- S-37's derivation, which is due before submission;
- the supplement split (the journal supplement versus the audit archive);
- every length method.

**What is missing from this list?**

---

## 4. The Round 128 confirmations, recorded

**All four of you and I:**
- **Step 8 closed at 1 990** (it is reopened now only for S-53).
- **The Rohith/Vegh record** is accepted as worded.
- **P122** is accepted as the form of the Rohith line.
- **The Step 15 map** is confirmed.

**Everyone voted yes to B as a first move, when that stage comes.**

**Author's decision:** length waits until this stage is complete.

---

## 5. Errors this round, and your positions on each other

**Mine.**
- **S-53 went through the closing of Step 8 unseen.** Qwen's R126-P1 asked for this map in Round 126. I parked it *"until Step 11 is
  re-read"* and closed Step 8 without it. Had I built the map when closing Step 8, the defect would have been caught before the close,
  not after.
- **Rounds 127–128:** I led with the length arithmetic before this stage was complete. The author has corrected that (§0).

**Qwen.**
- The *"Step 14 is closed"* reason (§1). That is not a rule.
- In Round 128 you gave venues with *"a 15,000+ word limit"* and an *"irreducible floor of ~14,000 words"*.
  - No one has opened those journals' requirements. The floor has not been measured.
  - Under the source rule, neither enters the records as a fact. Both are recorded as unverified.

**DeepSeek.** You wrote that your Round 127 judgment *"already treated (d) for Vegh as not established"*. Your Round 127 text said
*"**Not (d)** as far as the geometry shows"*. That is close, but it is not the same. A small point, noted only because the record now
turns on that difference.

**ChatGPT.** None found. You corrected your arithmetic plainly and early.

**Grok.** None found.

**Credit.**
- **Qwen's R126-P1** is what found S-53.
- **DeepSeek and Qwen** accepted their Round 128 map errors by name.
- **DeepSeek and Qwen** changed their votes on certification, with reasons.

**Positions still divided, for the next stage (answer each other if you wish; not voted now):**
- **DeepSeek** now says Step 8's residual-torque block and the strip split could move with a one-sentence body summary, and the
  stopped-state block could not.
- **Grok, ChatGPT and Qwen** say none of the three moves: the residual-torque chain is the evidence that the declined channel is not
  free.
- **S-53 bears on this.** The stopped-state block is the one whose receipt was broken.

---

## 6. To vote

| # | Item | My vote |
|---|---|---|
| a | §1: confirm the certification deletion; Step 15 closes at 343 | confirmed |
| b | §1.1: the debt trace | confirmed |
| c | §2: S-53 — D or D+ (vote on the D+ sentence and the S11 rows separately); v7's "adopted because" sentence | D+; not needed |
| d | §2.2: P-Claude-1, the receipt audit before the stage closes | yes |
| e | §3: is the completion list complete; how should the whole paper reach you | — |

---

## 7. Your own proposals

As always, give anything you see, with your reason.

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## Appendix A — the S-53 texts

### A.1 Step 8, as it now stands

> **The fixed geometry of the tip pairs leaves two admissible cruise states, and only one of them
> is physically closed.** Unable to feather, the pairs must either turn at the zero-shaft-torque
> condition or be stopped, and the difference between those two states is a substantial fraction of
> the aircraft's zero-lift drag. Both ends are computed rather than assumed and the charge appears
> in Section 11.
>
> **The tip pairs are the parts that fail the escape condition.** The nose pair meets all four parts of Section 3. The tip pairs do not: they hold
> one orientation, but they are carried through cruise producing moments rather than cruise thrust,
> which is the first of Section 3's failure modes, and they are exposed while doing it. This is the partial
> instantiation Section 3 lists as its **fourth** failure mode — meeting the condition where the
> aircraft is carried and failing it elsewhere — and the charge it re-opens is the second, carried in
> Section 11. *(They are sized for moments and used for them in both regimes; they add the take-off
> margin (Section 5) but were not sized for weight support. Section 3's permitted-cost clause
> therefore places them outside the first charge while leaving them in the airstream.)*
>
> The free-wheeling state is physically determinate: the rotor settles where net shaft torque is
> zero. **The stopped state is not.** Stopping a rotor requires the stop to be produced by
> something — motor holding torque, an electrical brake, a mechanical lock — and a stopped
> fixed-pitch blade also has an azimuth, so "stopped" is a family of aerodynamic states rather than
> one. Neither the means nor the azimuth is fixed by this study, and the drag figure quoted for the
> stopped condition should be read as the state Section 11 defines rather than as the state a
> particular installation would reach. The free-wheeling state needs no stopping means; the stopped state does, and if it were a
> brake or a lock rather than motor holding torque, the count of Section 7 would gain a class.

### A.2 Step 11, as it now stands (Bill 2 and the fixed-pitch gap)

> ### Bill 2 — the drag of hover hardware, inside the bracket
>
> In the zero-lift drag build-up behind Section 10's bracket (line items in Supplement S11), **the hardware exposed by the vertical-phase
> layout — the tip frames and the free-wheeling attitude rotors — is 69 percent of the zero-lift drag at the favourable end and 57
> percent at the adverse one**; the rotor term alone is 0.0154 at the favourable end. **The rotor line rests on section drag at low
> Reynolds number.** It is a blade-element result for sections near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section
> polars that are computed rather than measured; Section 12 shows how strongly the term depends on it. **The tip-frame term is an
> attribution, not a marginal removal cost**: it is not a claim that this drag would disappear if the vertical phase did.
>
> Removing the hub and small items, the tip frames and the free-wheeling rotors gives a clean-body lift-to-drag ratio of 20.55 at the
> favourable end and 15.24 at the adverse one, against the aircraft's 10.82 and 8.79: **the configuration retains 52.6 and 57.7
> percent.** Bill 2 therefore occupies a larger share where the clean-body drag is lower, because a near-constant charge is set against
> a smaller total — a statement about position within the drag bracket at one scale, not about size (Section 12).
>
> **Rotor–structure and rotor–wing interference is not modelled and is not carried as a line.** Section 2 quotes a wind-tunnel finding
> that a simulation assuming negligible rotor–structure interaction *"always predicts higher lift and lower drag than were
> experimentally observed"*; this build-up is such a calculation, and the bracket's upper margin is the only provision made for it.
>
> ### The cruise-efficiency gap under fixed pitch
>
> Section 10's closures run at a cruise propeller efficiency of 0.632 to 0.683: **relative to the 0.80 the published chain assumed,
> 14.6 percent lower at the better blade and 21.0 percent lower at the worse.** **The ledger does not attribute the whole of that gap to
> the absence of variable pitch.** **No variable-pitch counterfactual was computed.** Nor is the gap decomposed.

### A.3 Supplement S11's table, as it now stands

> | | favourable end | adverse end |
> |---|---:|---:|
> | Clean wetted surface | 0.0073 | 0.0142 |
> | Hub and small items | 0.0015 | 0.0022 |
> | **Tip frames** | **0.0043** | **0.0047** |
> | **Attitude rotors, free-wheeling** | **0.0154** | **0.0169** |
> | Total | 0.0285 | 0.0381 |

And Step 13, for comparison: *"… the lift-plus-cruise layout … assumes lift rotors stopped and aligned in cruise, which takes an
indexing mechanism (Section 7) whose mass is not separately charged."*

### A.4 The v7 source (`paper/paper-v7.md`, §3.3), from which the D+ sentence is derived

> **Table 3.** Cruise zero-lift drag increment of the eight tip discs in four cruise states, against the 0.0248 assumed for the clean airframe.
>
> | Tip rotors in cruise | ΔC_D0 | of the 0.0248 assumed |
> |---|---:|---:|
> | turning at zero shaft load, blades at low incidence | 0.0003 – 0.0008 *(assumed)* | 1 – 3 % |
> | turning at zero shaft load, **computed below** | **0.0154 – 0.0423** | **62 – 171 %** |
> | stopped edge-on, at a chosen azimuth | 0.0008 | 3 % |
> | **stopped broadside, azimuth uncontrolled** | **0.015 – 0.018** | **61 – 74 %** |
>
> **Charging the free-wheeling state also reopens a trade this paper has not priced, and that absence should be stated before the
> calculation rather than after it.** The computed free-wheeling charge below is 0.0154; the *stopped edge-on* row is 0.0008 — **a
> factor of twenty cheaper in drag**. The configuration cannot be made to stop its rotors for free, because azimuth control is exactly
> the indexing mechanism Section 2.10 gives as a reason not to stop them; but "this configuration has no rotor to stop" is a design
> choice, not a consequence, and a reader is entitled to ask what the mechanism would cost against the twenty-fold drag saving. **The
> comparison is not made anywhere in this paper.** Sizing an indexing mechanism for eight small discs, charging its mass and its failure
> modes, and re-solving the loop against a zero-lift drag reduced by 0.0146 is a bounded calculation and it has not been done. It is the
> single most likely question a reader of Section 3.3 will ask, and the honest answer is that the free-wheeling state was adopted
> because it needs no hardware, not because it was shown to beat the hardware.

**The estimate's own qualification** (`paper/paper-v5-supp.md`): *"The estimate behind that is an area-and-coefficient calculation with
assumed solidity and section drag coefficients, not a propeller calculation; what is robust is the ratio between the states, not the
values."*

(v7's *"0.0248 assumed for the clean airframe"* and its percentages belong to v7's drag basis. They are not proposed for v8.)

---

## Appendix B — Step 15 as it now stands (body only)

### Four axes, and where the paper stops

The paper makes its claims on four axes, against four opponents (Section 9), and on each it stops where
its evidence stops.

**Cruise efficiency, against rotorcraft — claimed against multirotors, and bounded; mixed against helicopters.** Cruise lift is carried on a surface
rather than on rotors. The size of the advantage is a calculation, not a consequence of that statement:
positive throughout against one published quadrotor, and from slightly behind to comfortably ahead against
the other (Section 6). Nothing is claimed against rotorcraft on vertical capability.

**Operation without a runway, against fixed-wing aircraft — claimed as sized, not demonstrated.** The
vertical phase was sized with an energy store whose required performance the sources consulted here do not
report as built (Section 14). Nothing is claimed against fixed-wing aircraft on range or cruise efficiency.

**The mechanism required to change regime, against tilting architectures — the contribution.** The
configuration is arranged to change regime by rotating the airframe rather than the propulsors, and so
carries none of the mechanism classes Section 7 counts: no pivot, no nacelle or rotor-group actuator, no
variable-pitch hub, no dedicated lift rotors, and — while the tip pairs free-wheel or are held by motor torque — no
rotor stowing, indexing or stopping mechanism (Section 7's note). Roll
comes from the strip; the reaction-torque channel the coaxial pairs could provide is declined, and what
declining it costs is not computed. **This is a count of mechanism classes, not a claim that nothing moves, and not a
claim of mechanical simplicity or reliability.** Whether this aircraft completes the rotation is a separate
question, and it is not settled here.

**Range, against the other hybrids — not claimed, in either direction.** The ordering belongs to the sizing
contract (Section 13).

**The loop closes; the aircraft is not shown to.** Section 14 lists what would settle the rest. What the paper offers is **a configuration sized to combine
runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism
that reorients a propulsor, and an account of what the combination costs.**
