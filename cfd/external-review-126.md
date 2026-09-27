# Round 122 — Voice in Steps 5 and 6: discussion round 1 of 3, and please answer one another. Two opened documents: do they stand in the way of the author's claim? S-48, S-49. Step 6: your lists side by side.

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full:**
> - Appendix A is the voice-flag table.
> - Appendix B is the relevant parts of Yang et al. 2018.
> - Appendix C is the text of Rheaume & Lents 2016, with its tables.
> - Appendix D is Step 6's body.

---

## 0. The author's decisions

1. **Voice (Steps 5 and 6).** The author has looked at the list and does not decide it yet: *"You and the other readers discuss voice
   for a few rounds. Everyone gives views and comments to everyone. If progress can be made, fine; if not, after three rounds present
   me the current state again."* This is **round 1 of 3** (Rounds 122–124). §1.
2. **Two documents the author uploaded.** They are not the two requested (Vegh 2025; Rohith et al.); they are two others, read in full.
   The author asks you to judge **whether the approach in them stands in the way of the author's claim.** §2.
3. **Closed since Round 121**, confirmed by all four of you and me:
   - Step 1, at 1 462 words, with V5 its one voice sentence;
   - Step 5, at 1 148 words.

   Also applied: *"Uncrewed tail-sitters combining fixed-pitch rotors with a flying wing have been built and flown for more than a
   decade"* is now protected (P-V4; unanimous). P103 and the Step 1 denial-map rows are accepted.

---

## 1. Voice — round 1 of 3: classify, and answer each other

Appendix A lists every sentence any of you flagged as voice in Steps 5 and 6: 11 in Step 5, 18 in Step 6. **I checked each for a
factual predicate**, because of the lesson of S-46: a sentence listed as voice turned out to assert something four other sections
denied.

**What I find:**
- **Few are pure voice.** A pure voice sentence is one whose removal changes no claim, limit or distinction:
  - Step 5: 5.1, the second half of 5.6, and the opening words of 5.11 (the figure of speech in 5.8 is discussed below);
  - Step 6: the second half of 6.1, the last clauses of 6.3 and 6.8, *"invites"* in 6.4 and 6.9, and perhaps 6.11.
- **Nine of the eighteen Step 6 flags are protected sentences:** 6.3 (in part), 6.7, 6.8 (in part), 6.12–6.16 and 6.18. The Round 116
  rule works both ways: a voice flag does not protect a sentence, and a protection is not lifted because a sentence has voice.
- **Two carry predicates that need checking, not voice decisions:**
  - **6.1**, *"That is the whole of the difference"* — a universal claim;
  - **6.2** (§3, S-49).

**Where you already disagree** — please answer each other by name:
- **5.3**, *"One structure serves four purposes and is charged to the mass budget once"*:
  - DeepSeek flags it as voice;
  - ChatGPT says it is *"a factual accounting proposition and is needed"*;
  - I agree with ChatGPT.
- **5.6**, *"Not demonstrated, and the list is not short."*:
  - ChatGPT and DeepSeek call the second half voice;
  - Grok calls it *"scope, not tone"*;
  - Round 121 made the heading word protected and the second half a voice flag. Grok, does the second half carry scope that the five
    listed items do not already carry?
- **5.8**, *"the race runs backwards"*: DeepSeek flags it; it sits inside E3, which all five of us kept as a mechanism sentence. Is a
  metaphor inside a mechanism sentence a voice item at all?
- **6.1**:
  - ChatGPT, DeepSeek and Qwen flag it;
  - Grok would not.
- **6.11**, *"They are given together because omitting any one of them would make the comparison look better than it is."*: DeepSeek
  flags it; it is also the sentence that tells the reader the five qualifications are one unit (Qwen R121-P1).

**Please give, for each flag in Appendix A:**
- your class: pure voice / carries a predicate / protected;
- where you disagree with another reader or with me, the reason, **addressed to that reader by name**.

**And one method question:** once the pure-voice set is agreed, should Step 1's method be used? That was Grok choosing one sentence to
stay while the rest go. Or is another method better for sections this dense? The author decides the method after round 3.

---

## 2. The two documents — does either stand in the way of the author's claim?

**The claim, as it now stands in Step 1** (protected):
> *"The contribution is the architecture: a configuration arranged to change regime by rotating the airframe rather than its
> propulsors, and so carrying no mechanism that reorients a propulsor."*
>
> *"What is not established is the combination taken together with its price."*

### 2.1 Yang, Zhu, Zhang & Wang 2018, IROS — a flying-wing tail-sitter (Appendix B)

**What it is:**
- mass 2.23 kg;
- **two CW/CCW propellers side by side**, torque-balanced but **not coaxial**, on fixed mounts;
- **two elevons**;
- two 6S LiPo batteries;
- **only hover and vertical flight were flown**; *"The on-going transition and horizontal flight … are the main future works."*

**How it is controlled:**
- Rotation about the belly axis comes from differential thrust.
- Rotation about the other two axes, **including the thrust axis**, comes from the elevons in the slipstream.
- The propellers' counter-moment about the thrust axis is not a control channel. It is estimated as a disturbance and cancelled.

**My reading.** It does **not** stand in the way of the claim as the paper now states it:
- **Against the six elements** of the gap (Round 120 §3), it has (a) a flying wing and (c) no reorienting mechanism. It does not have:
  - (b) every propulsor a coaxial pair;
  - (d) at most one moving device;
  - (e) buffered series hybrid;
  - (f) the three-bill accounting.
- **But it sharpens Grok's K argument.** Read on its own, the contribution sentence also describes this vehicle: it changes regime by
  rotating the airframe and carries no mechanism that reorients a propulsor, and the authors say it *"can achieve VTOL abilities
  without adding other mechanical complexity."* What separates the two is the second sentence, the combination with its price. That
  is why K and *"not a claim to an empty field"* matter.
- **It is a second witness for two Step 1 sentences:**
  - *"The established answer to hover control on such a configuration is a surface in the slipstream"*;
  - *"Using it is a choice, and so is declining it."* This vehicle also declines the reaction-torque channel. So declining it is not
    unique to this paper, and Step 1 already does not claim that it is.
- **Witness scope:** side-by-side, not coaxial; hover only.

**Please judge:**
- Does Yang et al.'s approach stand in the way of the contribution or the gap sentence?
- Should Yang et al. join Step 1's occupied list? If so, as what?

### 2.2 Rheaume & Lents 2016, SAE — energy storage for a hybrid airliner (Appendix C)

**What it is:**
- a single-aisle airliner of 62 000 kg MTOW;
- a parallel hybrid: a 2 500 HP electric motor on each fan's low spool for take-off and climb;
- **the turbines are sized for cruise**;
- a survey of storage metrics.

**Where it bears:**
- **Step 7 / Step 3.** Sizing the continuous plant for cruise and taking the peak from a store appears here, for an airliner. That
  supports Step 7's *"None of the three elements is new"*. It does not touch the architecture claim. The witness scope is a crewed
  airliner with a parallel hybrid.
- **Step 14.** Its Table 1 lists Li-ion at 1 800 W/kg and Li-Po at 3 000 W/kg, both cited to the same review, and supercapacitors at
  500–10k and 10k–100k W/kg. Its own qualifications:
  - *"The best metrics in each category for each battery type were selected. Such batteries are not commercially available since they
    are usually optimized either for specific energy or specific power."*;
  - *"the battery discharge rate metrics are not considered here"*;
  - *"specific power is a significant driver of battery weight but was not considered in this analysis"*.

  So it **qualifies** Step 14's *"lithium-polymer figures in the literature as high as 3 kW per kilogram"*. It does not support it:
  this is another cited best-in-category figure, not a pack.
- **Supercapacitors** reach the specific power Step 14 asks for, at 1–10 Wh/kg. Whether any store, or a battery–supercapacitor
  combination, closes this aircraft's buffer **is not computed**. I give no sign.

**My reading.** It does **not** stand in the way of the claim.
- It bears on Step 14's first unknown, the store, and on Step 7's "not new".
- Step 14's sentence *"The package Section 10 closes on does not exist with any store the sources consulted here report as built"*
  still holds: this source reports survey metrics, not a built store.

**Please judge:**
- Does its approach stand in the way of the claim?
- Should it be cited in Step 7, in Step 14, or not at all? If cited in Step 14, its qualification must travel with it (Round 94 rule).
- Should Step 14 name a supercapacitor or hybrid store as an unexamined option?

---

## 3. Two source defects to vote

**S-48 (Step 6, found by ChatGPT).**
- The text: *"On cruise efficiency taken alone, the entry is ahead of this configuration's low corner, **and whether it is ahead of the
  best examined blade family depends on the drag bracket**."*
- The same section's table: against the best examined family (6.00–7.39), this configuration leads the all-electric quadrotor (5.8) by
  **+3 % … +27 %**, at both ends of the bracket. It does not depend on the drag bracket.
- The clause would be true of the *least* efficient family (5.56 and 6.84).
- **Repair, deletion only:** *"On cruise efficiency taken alone, the entry is ahead of this configuration's low corner."*
- ChatGPT proposed *"but below the best examined blade family's range"*. That is an R, and the table already says it.

**S-49 (Step 6, found checking flag 6.2).**
- The text: *"Lift is carried on a surface or it is carried on rotors, and no sizing contract, no assumption in this paper and no choice
  available to a designer moves a vehicle between those two states."*
- A **winged compound helicopter** shares lift between a wing and a rotor. For it, the either/or does not hold, and a designer's choice
  (adding the wing) is exactly what moves a vehicle.
- The paper's rotorcraft opponent (Step 9, T1 row 1) is multirotors and helicopters, and the NASA entries it uses have no wing
  (Section 6: *"which has no wing either"*).
- **Question:** repair or keep? My proposal, deletion only:
  > *"Lift is carried on a surface or it is carried on rotors, and no sizing contract and no assumption in this paper moves a vehicle
  > between those two states."*

  The remaining claim is about the paper's own sizing contracts and assumptions, which is true. The either/or remains, and it is true of
  every vehicle the paper compares.

  Or delete the sentence: the paragraph's protected sentence *"A rotorcraft's rotors must produce the lift and the propulsive force
  together, throughout cruise"* already carries the structural point.

---

## 4. Step 6 — your lists side by side, and what can move

**The core** is agreed by all four of you and me:
- *"a surface that carries the cruise lift"*;
- the envelope 5.56–7.39, with the all-electric low-corner exception reported as a result;
- the helicopter comparison as mixed;
- *"the size of the resulting advantage is a calculation"*.

**Agreed to stay (all four of you and me):**
- the opponent and the one-way comparison;
- the requirement;
- the structural difference;
- the L/De definition;
- the two kinds of spread;
- the four-corner table and both readings;
- both quadrotors and the helicopters;
- the five qualifications as one unit, including the isolation pair (objects, common basis, *"not a controlled numerical
  reproduction"*);
- Sized / Not demonstrated;
- the cost bridge.

**Candidate moves.** Paragraph numbers refer to Appendix D.

| # | Candidate | Grok | ChatGPT | DeepSeek | Qwen | Claude |
|---|---|---|---|---|---|---|
| M1 | [15], the source's hover and cruise formulation and battery-capacity argument (sentences 2–4), keeping *"Which power P denotes is not assumed here, because reading it as electrical power rather than shaft power would make this configuration's figure incomparable with the published one."* | not addressed (keeps *"shaft-not-electrical power"*) | move | move | move | **move** |
| M2 | [18], *"— two and three blades per rotor, at two target section lift coefficients, each solved at its hover and its cruise condition"* | move | not addressed | move | move | **not unless [22] is repaired**: [22] says *"It is the best of the four"*, and without M2 the reader is never told there are four (Grok P51). Deletion-only repair of [22]: *"It is the best ~~of the four~~ on cruise efficiency under the hover figure-of-merit constraint"* |
| M3 | [34], delete *"= 0.5√(πARe/C_D0)"* and *"— 11.65 against 10.82, and 10.08 against 8.79, both at e = 0.817"*, leaving *"The best point lies at 1.26 times stall, and `L/D_max` exceeds the cruise ratio at both ends of the drag bracket."* | move (keep 1.26 / 1.49 and *"margin is positive anyway"*) | move (keep direction) | **keep** the numbers | move | **move** — the direction is the finding; the numbers are working |
| M4 | [8], the two coefficient equations | — | move | **keep** | — | **keep**: 20 words, and removing them breaks *"that drag"* |
| M5 | [6], the survey sentence (*"The consequence has been stated independently: … long-range ones."*) | move | — (keeps the requirement) | — (keeps the requirement) | — | **keep**: it is external evidence for the requirement. *"Move the working, not the evidence."* |
| M6 | [26], the 0.557 *"derivation"* | — | move the derivation | move the arithmetic | — | **nothing to move**: the body has one sentence and no arithmetic |
| M7 | [39], *"— a vortex-lattice solution of the trimmed planform, and 3.9 percent below the assumption,"* | keep 0.817 vs 0.85 | keep 0.817 | keep 3.9 % | move the detail | **keep *"a vortex-lattice solution"*** (the model is part of the number's identity); *"3.9 percent below the assumption"* could go |

**Honest size.** With M1, M2 (and the [22] repair), M3 and part of M7, Step 6 goes from 2 145 to about 2 000 words.
- It does not approach 850, and deleting working will not get it there.
- ChatGPT's *"2,145 → 1,350–1,500 words"* would need recomposition of the qualification paragraphs, and those are protected or
  isolation-pair material.
- I report this. The length decision is the author's (E8).

**The qualification-direction column (Qwen R120-P2) needs one definition.** You used the word in different senses:
- Grok marks scale *"against"* this configuration;
- DeepSeek marks it *"for this configuration, conservatively"*;
- ChatGPT uses *"against overinterpretation"*.

The section's own heading counts *"three run against this configuration, one has no computed direction, and one bounds what the
comparison can be called"*. I propose that definition:
> **Direction = the way the mismatch biases the comparison.** *Against this configuration*: correcting it would widen the margin.
> *For*: correcting it would narrow the margin. *Not computed.* *Bounds*: it limits what the comparison can be called, not its sign.

Under it, the heading's count is: scale, the good quadrotor and the speeds against; the atmospheres not computed; the analysis chains
bounds. That is what Grok's table shows. Please check it against yours.

**Checked this round:**
- **Grok P110.** 3 678 lb, 7 221 lb, 1 742 lb, 4.9 and 5.8 match Johnson & Silva 2022 Table 3 exactly; the helicopters are 5.4, 6.0,
  5.9 and 7.2, so *"5.4 to 7.2"* holds. I opened `references/1521_Johnson & Silva_122721.pdf`, the table on its printed page 71.
- **DeepSeek's count audit, extended to Step 6.** It is clean:
  - *"nose pair"*;
  - four blade families (two blade counts × two lift coefficients) for *"the best of the four"*;
  - *"tip frames and the free-wheeling attitude rotors"*.

---

## 5. ChatGPT — three votes, with the proposals' own texts

Your Round 121 votes on these carried descriptions of other proposals. Please vote on the texts:
- **P104 (Grok):** *"The author's 'having seen what had not been seen' is not used as a draft sentence, heading or abstract line; the
  permitted form is the documented gap."* (You described it as keeping Step 1's *"what is unsettled is which price …"*.)
- **Qwen R118-P1:** *"Step 7's trace checks 'some of them together' against Section 1's occupied list."* (You described Qwen R120-P1,
  the mechanism-prerequisite flag.)
- **Qwen R118-P2:** *"The search protocol is recorded in the evidence record."* Applied: it is in `paper/v8-gap-search.md`, and the
  evidence file points to it. (You described R120-P2, the direction column.)

---

## 6. Errors this round

**Mine.**
- In Round 121 I sent you Step 6 without seeing S-48, which contradicts its own table two paragraphs up; ChatGPT saw it.
- I did not see S-49 until I checked the voice flags for predicates.

**ChatGPT.**
- The mislabelled votes (§5).
- *"There is one sentence I would not yet approve unchanged … A deletion-only repair is possible"*: the repair you then gave is not a
  deletion.
- The find itself (S-48) is the most useful catch of the round.

**DeepSeek.**
- Your Step 6 lists keep the coefficient equations and the *"Ph"* hover formula *"as source anchor"* in the body, while your move list
  sends *"the full derivation of L/De and the source's hover/cruise formulation"* to S6. Which is it?

**Qwen.**
- *"All numbers … survive the proposed moves"*: your own move list sends 11.65 and 10.08 to S6, so they would not stay in the body. If
  they move, their identity must move with them (Round 102).
- You fully and plainly acknowledged the Round 120 errors. Thank you.

**Grok.** None found.
- The DOI links you gave are recorded as unverified.
- Neither uploaded document came from them. The author found other papers, and the ones you linked are still wanted.

---

## 7. To vote

| # | Item | My vote |
|---|---|---|
| a | §1 voice, round 1: your class for each flag, and your answers to each other by name | as in Appendix A |
| b | §2.1 Yang et al.: an obstacle to the claim? occupied list? | no obstacle; yes, as a second witness for the slipstream surface and for declining the channel |
| c | §2.2 Rheaume & Lents: an obstacle? cite where? | no obstacle; Step 14 and Step 7 only with its qualification and scope, or not at all |
| d | S-48 deletion | yes |
| e | S-49: deletion form, or delete the sentence | deletion form |
| f | §4 M1–M7 | as in the table |
| g | §4 direction definition | yes |
| h | §5 (ChatGPT) | yes |
| i | New: Grok P109 (the decade-occupancy sentence is the uncrewed tail-sitter home; cutting it reopens V4); Qwen R121-P1 (the isolation-pair numbers 7 221 / 3 678 / 1 742 lb are one unit with the low-corner exception); Qwen R121-P2 (Step 6 → Step 11 delegations mapped when Step 11 is re-read) | yes, yes, yes |

---

## 8. Your own proposals

As always: anything you see, with your reason.

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## Appendix A — the voice flags (G Grok, C ChatGPT, D DeepSeek, Q Qwen); "protected" = in the protected register

### Step 5 (11 flags)

| # | Sentence | Flagged by | Protected | My class |
|---|---|---|---|---|
| 5.1 | *"The ground is the only thing the site provides, and it provides it unprepared."* | D, Q | no | **pure voice** — restates the requirement sentence before it |
| 5.2 | *"Those five points are not added hardware."* | D | no | **predicate** — the tip frames are the landing structure; Section 8 rests on it |
| 5.3 | *"One structure serves four purposes and is charged to the mass budget once — Section 8 gives the fairing's sizing."* | D (C: not voice) | no | **predicate** — mass accounting (with ChatGPT) |
| 5.4 | *"The saving has precedent and it is not this paper's observation."* | D | **yes** | predicate (priority limit) |
| 5.5 | *"And the stance base is a parameter rather than a constraint."* | D | no | **predicate** — opens E1; P71 pair with item 5 |
| 5.6 | *"Not demonstrated, and the list is not short."* | D, C (G: scope) | *"Not demonstrated"* **yes** | **only *"and the list is not short"* is pure voice** |
| 5.7 | *"That is the one place the configuration asks a component to do a second job it was not sized for, and it means … compete for it."* | D | **yes** | predicate |
| 5.8 | *"Coming back, the race runs backwards: dynamic pressure is falling …"* | D (*"the race runs backwards"* only) | no | mechanism sentence (E3, kept); the metaphor's content follows the colon |
| 5.9 | *"That disposes of the spatial-orientation objection and nothing else."* | D | no | **predicate** — *"and nothing else"* is a limit, tied to Section 1 |
| 5.10 | *"Runway independence is not obtained free, and the charges appear later rather than here."* | D | no | **predicate** — cost pointer |
| 5.11 | *"That gap is wider than it looks, because this configuration declines the reaction-torque channel … leaving that axis to the strip."* | C | no | *"wider than it looks"* **pure voice**; *"because …"* content |

### Step 6 (18 flags)

| # | Sentence | Flagged by | Protected | My class |
|---|---|---|---|---|
| 6.1 | *"That is the whole of the difference, and it is worth stating in those plain terms because the consequence is structural."* | C, D, Q (G: would not flag) | no | *"worth stating in those plain terms"* **pure voice**; *"the whole of the difference"* **a universal predicate** — to check |
| 6.2 | *"Lift is carried on a surface or it is carried on rotors, and no sizing contract, no assumption in this paper and no choice available to a designer moves a vehicle between those two states."* | D | no | **predicate — S-49 (§3)** |
| 6.3 | *"But the size of the resulting advantage is a calculation, not a consequence of that statement, and the two must not be run together."* | D | first half **yes** | *"and the two must not be run together"* **pure voice** |
| 6.4 | *"The rest of this section is the calculation, and it gives a smaller number than the structural statement invites."* | C, D | no | *"invites"* voice; *"a smaller number"* a predicate (the direction of the result) |
| 6.5 | *"A force ratio cannot be placed beside it."* | D | no | **predicate** — the comparability limit |
| 6.6 | *"Neither factor is a single number, and they are two different kinds of spread."* | D | no | **predicate** — the uncertainty / design-variable distinction (ChatGPT: keep) |
| 6.7 | *"These are the bounding corners of a product, not four simulated aircraft."* | D | **yes** | predicate |
| 6.8 | *"Whether 0.683 is the blade a designer would actually choose is not settled here, and saying so is the point."* | D, Q | first half **yes** | *"and saying so is the point"* **pure voice** |
| 6.9 | *"So the second claim is narrower than the structural statement invites."* | C, D | no | **predicate** (the claim is narrow); *"invites"* voice |
| 6.10 | *"And what compresses it is not the wing. It is the cruise efficiency this aircraft's fixed-pitch blade delivers."* | C, D | no | **predicate** — attributes the gap to the blade; Section 11 depends on it |
| 6.11 | *"They are given together because omitting any one of them would make the comparison look better than it is."* | D | no | half voice; it also says the five are one unit |
| 6.12 | *"The quadrotor is a good quadrotor."* | C | **yes** | predicate |
| 6.13 | *"Nothing here is compared against a poor example."* | C | **yes** | predicate |
| 6.14 | *"The reference is therefore given its best speed and this configuration is not given its best speed, and the margin is positive anyway."* | C, D | **yes** | predicate |
| 6.15 | *"So this is a comparison of two independently produced figures in a common definition, not a controlled numerical reproduction, …"* | D | **yes** | predicate (isolation pair) |
| 6.16 | *"No part of this has been measured."* | D | **yes** | predicate |
| 6.17 | *"The wing that makes cruise efficient is carried through the vertical phase, where it produces nothing and presents the aircraft's largest surface to ground wind."* | C | no | **predicate** — a cost sentence; *"produces nothing"* is true of lift in hover |
| 6.18 | *"The two halves are now on the table separately. Section 7 is where they are combined, and the combination is what this paper is for."* | D | **yes** | predicate |

---

## Appendix B — Yang, Zhu, Zhang & Wang 2018: the relevant parts

**Source:** Y. Yang, J. Zhu, X. Zhang and X. Wang, *Active Disturbance Rejection Control of a Flying-Wing Tailsitter in Hover
Flight*, 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Madrid, pp. 6390–6396. File:
`references/Yang-Zhu-2018_IROS_ADRC-flying-wing-tailsitter-hover.pdf` (7 pages).

**What is quoted and why.** The paper is mainly a control-law paper (ADRC: extended state observer, tracking differentiator,
nonlinear state-error feedback). That part does not bear on our paper and is not quoted. Quoted verbatim below are the parts that do:
- the vehicle;
- how each attitude axis is actuated;
- how the propellers' counter-moment is treated;
- what was flown;
- what is left to future work.

The equations are garbled in the text extraction. Where one matters, it is described in words in square brackets, and **the brackets
are mine, not the paper's**.

**Abstract (in full).** *"This paper presents the development and hovering control of a tailsitter unmanned aerial vehicle (UAV) that
merges long endurance and vertical takeoff and landing (VTOL) abilities. The designed tailsitter contains one flying-wing with two
motors and two elevons. Vehicle aerodynamics and a six-degrees-of-freedom (6-DOF) model are especially developed for the tailsitter. To
achieve a good performance in outdoor stationary hovering and accurate vertical flying, the active disturbance rejection control
(ADRC) for attitude controller is proposed. … Experimental results are presented to corroborate the effectiveness of the controller in
disturbance rejection."*

**Introduction.** *"As shown in Fig. 1, we designed and manufactured a dual-rotor tailsitter UAV based on a kind of fixed-wing
aircraft. The UAV can achieve VTOL abilities without adding other mechanical complexity."* It also cites, among the tail-sitter
literature, *"A. Oosedo, … 'Development of a quad rotor tailsitter VTOL UAV without control surfaces and experimental verification,'
… ICRA, pp. 317-322, 2013"* (its reference [3]); that is the 2013 vehicle in Step 1's occupied list.

**II-A, Aircraft Design.** *"Two CW/CCW carbon propellers with the diameter of 16" driven by 600W brushless electrical motors are
chosen as the system propulsion. Two 6s LIPO batteries are used to supply power. The airframe consists of one flying-wing with two
elevons. The profile of the wing is the MH91 whose wing area is 0.478m², span is 1.2m and chord length is 0.438m. … The all-up-weight
of the tailsitter is 2.23kg."*

**II-B, Coordinate systems.** *"… vertical body frame is adopted to avoid singularity in the controller design: the original point
coincides with the center of gravity (C.G.), xb points to the belly of the vehicle, zb points to the tail of the vehicle and yb is
determined by the right-hand principle."* [So zb is the fuselage axis, which is the thrust axis; it is vertical in hover.]

**II-C, Actuation Principle.** *"The tailsitter uses a minimum combination of motors and elevons to control its attitude during the
whole flight envelope. As shown in Fig. 4(a), differential thrust of two propellers is used to control the axis xb of the vehicle. The
vehicle axis yb is controlled by equal elevons deflections (Fig. 4(b)) and the axis zb is similarly steered by differential elevons
deflections (Fig. 4(c)). The elevons have a range of ±30°, and the down deflection is defined as positive. The moments of pitch and yaw
are determined by both propeller slipstream and air flow diverted by the elevons."*

**III-B, the moment equations.** *"… the resultant thrust of left propeller and right propeller coincides with the negative zb axis
but it does not pass through the center of gravity."* [In the equation for the axis zb, the propellers enter only as a moment
M_l + M_r, and not as a control.] *"Ml and Mr are the moments generated due to the rotation of motors and propellers."*

**IV-B, how that moment is handled.** *"For the pitch and yaw channels, ESOs reflect their unknown dynamics and external disturbances
respectively, including the counter-moment due to rotation of propellers, undesired pitch moment due to the displacement between
resultant thrust axis and center of gravity and so on."* [The propellers' counter-moment about the thrust axis is estimated as a
disturbance and cancelled; it is not used as a control channel.]

**IV-C, Control Allocation.** *"… uM̄ is the pitch control moment, which is produced by equal elevons deflections. And uN̄ is the yaw
control moment, which is produced by differential elevons deflections."* [The roll moment is (T_r − T_l)·l_y, from differential
thrust.]

**V, Experiments.** *"The experiments are conducted at a windy day … The wind blows from north to south at the speed of 3 ∼ 4m/s,
which is measured by a handheld anemometer in ground."* Two tests: a hover of about 30 s, and *"fly 15 meters forward and then back
with its belly facing the wind"* in the vertical attitude.

**VI, Conclusions (in full).** *"The design and hovering control laws of the flying-wing tailsitter with two motors and two elevons
are discussed in this paper. … Experiments are presented to corroborate effectiveness of the controller in disturbance rejection.
The on-going transition and horizontal flight of the tailsitter, as well as the ability to resist stronger winds, are the main future
works."*

---

## Appendix C — Rheaume & Lents 2016: the body text and tables

**Source:** J. M. Rheaume and C. Lents, *Energy Storage for Commercial Hybrid Electric Aircraft*, SAE Technical Paper 2016-01-2014,
2016, doi:10.4271/2016-01-2014. File: `references/Rheaume-Lents-2016_SAE-2016-01-2014_energy-storage-hybrid-electric-aircraft.pdf`
(5 pages). **Extracted with `pdftotext`; paragraph breaks restored by hand from the page layout; the three tables are images in the PDF
and were transcribed by hand.** Reference list, contact details and disclaimer omitted.

#### Abstract

Energy storage options for a hybrid electric commercial single aisle aircraft were investigated. The propulsion system features twin Geared Turbofan™ engines in which each low speed spool is assisted by a 2,500 HP electric motor during takeoff and climb. During cruise, the aircraft is powered solely by the turbine engines which are sized for efficient operation during this mission phase. A survey of state of the art energy storage options was conducted. Battery, supercapacitor, and flywheel metrics were collected from the literature including Specific Energy (Wh/kg), Volumetric Energy Density (Wh/L), Specific Power (W/kg), Cost ($/kWh), and Number of Cycles. Energy storage in fuels was also considered along with various converters sized to produce a targeted quantity of electric power. The fuel and converters include fuel cells (both proton exchange membrane and solid oxide operating on hydrogen or on jet fuel) and a turbogenerator (jet fuel or LNG). The various energy storage options were compared across a range of stored energy on the basis of weight. The selection of a lightweight energy storage technology depends on power and quantity of energy storage. A turbogenerator auxiliary power unit has the best energy and power density for the application. The fuel cells tend to be heavy options due to low specific power. PEM fuel cells operating on compressed or liquid hydrogen are lighter weight than SOFCs, however, PEMFCs are comparable to batteries at the energy storage design point of 1500 kWh. Applications requiring low detectability and long duration favor PEM fuel cells.

#### Introduction

A hybrid electric aircraft propulsion system for a commercial single aisle aircraft motivates this investigation of energy storage. The hybrid architecture consists of twin Geared Turbofan™ engines assisted by 2,500 HP electric motors during takeoff and climb. The motors provide power to the low speed spools of each engine allowing the core to be downsized. (See Figure 1.) During cruise, the aircraft is powered solely by the turbine engines which are sized for efficient operation during this mission phase. As fuel mass decreases during cruise, excess power can be allocated to recharging energy storage by taking power off the low spool motor-generator. Earlier efforts indicated that 1500 kWh of energy is necessary to boost the fan during takeoff and climb [1].

The automotive industry has pioneered hybrid electric vehicle development. Several vehicles are available for sale from numerous manufacturers. The aerospace industry has not followed the automotive trend largely due to integration challenges, a long and costly product development cycle that includes airworthiness certification, and the weight of the additional motor, drive and energy storage systems.

Numerous prior studies exist on vehicular energy storage [2, 3, 4, 5, 6, 7]. This paper builds on previous work by reviewing and comparing state of the art energy storage methods as they relate to a commercial single aisle hybrid electric aircraft. Conventional technologies such as batteries, capacitors, and flywheels were considered. In addition, energy conversion devices such as fuel cells (both proton exchange membrane and solid oxide) and a turbogenerator (turbine directly coupled with an electric generator) were explored.

Metrics of state of the art energy storage technologies are tabulated for comparison. These metrics include: Specific Energy (Wh/kg), Volumetric Energy Density (Wh/L), Specific Power (W/kg), Cost ($/kWh), and Number of Cycles. On account of the importance of weight for aircraft applications, various energy storage technologies are compared for energy storage on a mass basis.

In the following, energy storage is examined from the point of view of hybrid propulsion of a commercial single aisle aircraft with focus on performance metrics that enable a hybrid electric aircraft architecture.

#### Methods

A literature survey was conducted in order to harvest metrics for comparison. These metrics were tabulated and used to estimate the weight of energy storage systems over a range of stored energy. Projections of future energy storage parameters were made for batteries and similarly compared. The design point is a 1,500 kWh energy storage system that delivers 5,000 HP for a commercial aircraft with a maximum takeoff gross weight of 62,000 kg.

Table 1. Energy Storage Performance Parameters *(an image in the PDF; transcribed by hand, bracketed numbers are the paper's reference numbers)*

| Technology | Specific Energy (Wh/kg) | Volumetric Energy Density (Wh/L) | Specific Power (W/kg) | Cost ($/kWh) | Cycles |
|---|---|---|---|---|---|
| Lead-Acid Battery | 20-50 [8] | 50-100 [8] | 150-300 [8] | 50-310 [9] | 1200-1800 [10] |
| Ni-Cd Battery | 40-60 [8] | 75-150 [8] | 150-200 [8] | 300 [8], 400-2400 [9] | 2000 [14] 3000 [10] |
| Ni-MH Battery | 60-100 [8] | 100-250 [8] | 250-1000 [14] | 300-500 [8] | 300 [10], 1000 [14] |
| Lithium-Ion Battery | 150-200 [11] | 200-300 [8] | 1800 [12] | 200-700 [8], 600-2500 [13] | 3000 [10] |
| Lithium-Polymer Battery | 130-200 [14] | 250 [15] | 3000 [12] | 333-500 [12] | >1000 [14] |
| Lithium-Air Battery | 400-800 [16] | 180-250 [15,16] | "Poor" [16] | n/a | 10 [16] |
| Lithium-Sulfur Battery | 200-700 [11] | 180-250 [15,16] | 750 [16] | n/a | 100 [14,16] |
| Sodium Sulfur Battery | 90–250 [14] | 167 [17] | 50 [14] | 180-500 [9] | >2500 [14] |
| Zinc-Air Battery | 200-300 [18] | 500 [13] | 70 [18] | 10-60 [13] | 100-300 [13] |
| Super-Capacitor | 1-10 [14] | 10 [8] | 500-10k [8], 10k-100k [14] | 20k [8] | >500k [14] |
| Fly-wheel | 10, 50-400 | 200 | 200-400 | 200-500, 400-800 | No limits |

*References cited in the table, from the paper's list: [8] Srinivasan 2006 (book); [12] Shukla & Kumar 2013, J. Phys. Chem. Lett.; [14] Chin 2011, NPS Masters thesis.*

The weight of energy converters was calculated from their specific power, and fuel was added to meet energy storage requirements. In contrast, battery weight was estimated solely on the basis of specific energy. Specific power is also likely to be a significant driver of weight but has not been considered in this analysis.

*[Figure 1, Parallel Hybrid Electric Geared Turbofan™ Architecture, and Figure 2, Energy Storage Weight, are figures and are not reproduced.]*

#### Results and Discussion

Values of energy storage parameters appear in Table 1 for conventional energy storage systems and in Table 2 for energy conversion systems (fuel cells, turbogenerator). An effort was made to select recent values in the appropriate size range.

Table 1 lists various types of batteries (loosely organized by technological maturity) followed by capacitors and flywheels. The best metrics in each category for each battery type were selected. Such batteries are not commercially available since they are usually optimized either for specific energy or specific power. The best metrics were selected in order to provide the best possible comparison with energy conversion devices. Multiple ranges of values and their sources were cited in the cases in which ranges differed. Cost information labelled as “n/a” applies to technologies in development (e.g. Li-S).

Table 2. Energy Converter Performance Parameters. All values exclude fuel and storage tank weights. *(image; transcribed)*

| Technology | Specific Power (W/kg) |
|---|---|
| PEMFC System with Fuel Processor | 140 [8] |
| PEMFC Stack plus BOP and excluding Fuel Processor | 500 |
| PEMFC Stack | >1000 [19,20] |
| SOFC System plus BOP including Fuel Processor (without Desulfurizer) | 100 |
| SOFC Stack | 500 |
| Gas Turbine-Driven Generator | 3,300 |

Lithium-air and lithium-sulfur batteries are attractive for high specific energy, however, these batteries are not widely available in the marketplace. Lithium polymer batteries exhibit attractive volumetric energy density as well as high specific power. The lithium chemistries tend to be more expensive than other options while offering high energy density. Supercapacitors exhibit low specific energy but outstanding specific power at high cost suggesting that this technology is more appropriate in a hybrid energy storage approach (e.g. supercapacitors and batteries). Flywheels exhibit attractive metrics, however, packaging remains challenging.

Energy converters (Table 2) rely on chemical energy storage, and their value proposition lies in the weight and efficiency of conversion. Fuel cells and a turbogenerator were considered.

Fuel cells were examined due to their high efficiency. The performance metrics of a fuel cell power system are dependent on the system size since efficiency varies with load. Generally no fuel cell power systems are available in the 5,000 HP class, so conservative values representative of automotive applications were chosen or estimated.

The specific power of fuel cell stacks and balance of plant (BOP) excluding fuel and tank weight were broken out separately in order to better understand the contribution of the stacks to the system weight.

Fuel processors that convert hydrocarbon fuels to a hydrogen-rich stream were included in the fuel cell system weight in order to make a direct comparison of the conversion of chemical energy to electricity. A likely fuel processor technology for aviation applications is partial oxidation due to low weight, however, autothermal reforming is more efficient than partial oxidation, and it is lighter weight than steam reforming.

For the fuel cell systems, the fuel is assumed to be desulfurized on account of the large weight penalty that a desulfurizer imposes; it has the potential to cut the specific power in half depending on the technology selected. Even with the advantage of desulfurized fuel, fuel cells exhibit lower specific power than a gas turbine-driven generator by a wide margin. The specific power of the turbogenerator in Table 2 was selected by identifying the specific powers of the turbine and generator (non-cryo-cooled) and combining them into one metric by taking the inverse of the sum of their reciprocals.

Competing engine technologies such as reciprocating engines and Wankel engines were not considered due to low specific power and consequently a dearth of commercial products available for aviation in the 5,000 HP class.

Turbogenerators are the lowest weight solution at the present time for the specified mission. The choice of liquid natural gas as fuel does not carry a significant weight penalty, however, it does increase system and logistical complexity.

For batteries, several energy storage densities are shown (200, 300, 500, and 1000 W-hr/kg). The current state of the art in commercially available lithium ion batteries is approximately 200 W-hr/kg. The higher battery energy densities allow one to set future targets for battery energy storage. The battery chemistry is not specified. No penalties for battery self-discharge and inefficiency of charging and discharging are applied in Fig. 2. In addition, the battery discharge rate metrics are not considered here.

The efficiency of conversion is also of interest. Fuel cells running on hydrogen exhibit over 50% efficiency, however, the fuel processing dramatically reduces the system efficiency. Partial oxidation is the lightest fuel conversion technology albeit the least efficient. The efficiency of a fuel cell power system with partial oxidation is on par with that of the lighter weight turbogenerator. When considering the fuel required to transport the energy converter, the turbogenerator exhibits favorable fuel consumption characteristics.

Figure 2 shows the weights of PEM fuel cells, turbogenerators, and batteries to deliver 5000 HP power over a range of stored energy including the design point of 1500 kWh. The PEM fuel cells operate on hydrogen in either compressed or liquid form. Not shown is the SOFC; the weight of a system that processes logistics fuel is several tens of thousands of kg excluding the desulfurizer. The weight of the ceramic stacks, their housing, the reformer, and nickel superalloy ducting combine for a massive and expensive system.

In Figure 2, power converters that operate on fuels other than Jet-A include the weight of the tank. For example, the turbogenerator that operates on Jet-A includes fuel weight but not tank weight because fuel tanks are already onboard, however, the turbogenerator operating on LNG includes fuel and tank weights. Similarly, the PEM fuel cell systems include the weight of the hydrogen fuel and tank because this fuel is not otherwise on the aircraft. The base PEM weight is the same for both cases, but compressed hydrogen storage is heavier than liquid.

Table 3. Energy to Transport Energy Storage System Mass throughout Mission. *(image; transcribed)*

| Energy Storage Technology | Transport Energy (kWh) | Fuel (lbm) |
|---|---|---|
| SOFC + Jet-A (S-free) | 6,067 | 1,121 |
| PEMFC + Comp H2 | 1,409 | 260 |
| PEMFC + LH2 | 1,232 | 228 |
| Battery 200 | 1,437 | 266 |
| Battery 300 | 958 | 177 |
| Battery 500 | 575 | 106 |
| Battery 1000 | 287 | 53 |
| GT-APU + LNG | 242 | 45 |
| GT-APU + Jet-A | 189 | 35 |

Despite consideration under ideal conditions, batteries are heavier than turbogenerators at the design point. For batteries to compete favorably for the intended application to assist takeoff and climb, a specific energy in excess of 1000 W-hr/kg is required. This value may further increase due to discharge losses, performance degradation, etc.

State-of-the-art batteries may find niche applications with small quantities of stored energy. The all electric Airbus E-Fan 2.0 training aircraft has 60 kW total propulsive power and can fly for an hour on a charge of lithium polymer batteries [21]. Reduced maintenance costs may result from the electric drivetrain.

Batteries have an inherent drawback: the weight of batteries remains unchanged throughout the flight envelope whereas jet fuel decreases in weight. Fuel must be expended to transport battery weight. Similarly, the weight of fuel cell and turbogenerator systems must be transported throughout the mission requiring additional energy, however, the fuel weight is significant. Table 3 quantifies the energy required to transport the various energy storage devices (and fuel other than -Jet-A when applicable) throughout a mission of 900 nm length (approx. 1.8 hr long) in which they provide 1525 kWh stored energy. The lower heating value of Jet-A fuel (42.9 MJ/kg) was used to calculate an equivalent fuel quantity. The fuel weight penalty that was used was derived from Pratt & Whitney aircraft and engine models.

Fuel for the turbogenerator and fuel cells was assumed to be completely consumed during takeoff and climb (no reserves). In reality, some reserves would be required in the event of an aborted landing to come around and to climb. In addition, fuel was assumed to be consumed at a constant rate during these mission phases. In reality, fuel consumption varies with power from a high during takeoff and tapering off during climb. The first assumption understates the energy required to transport fuel whereas the second one overstates it. Nevertheless, the conclusions are unlikely to change: batteries and fuel cells require large increases in specific energy in order to be competitive with the turbogenerators for this application. A factor 5 increase over the present state of the art specific energy will begin to make batteries competitive with present heat engines at the design point noting that specific power is a significant driver of battery weight but was not considered in this analysis. Until then, the transport of battery weight is prohibitively energy-intensive.

The turbogenerators (labelled as GT-APU) require the least weight to transport. They have high specific power and in contrast to batteries; the turbogenerators lose their fuel weight early in the flight. In the case of Jet-A fuel, no additional tank weight is required whereas LNG requires an additional tank. The SOFC utilizes Jet-A so no additional tank is required, however, at least an order of magnitude improvement in specific power (mass reduction) is necessary in order to be viable. The PEM fuel cell systems require almost as much energy to transport during the mission as they provide.

Factors other than fuel burn and specific energy may lead to the selection of different energy storage methods For example, if low noise and low IR signature are desired criteria, then a PEM fuel cell competes favorably against the turbogenerator. The PEM fuel cell is preferred over present batteries for stored energy greater than 1300 kWh for the given power rate provided that liquid hydrogen is available. The infrastructure to generate and distribute the hydrogen must also be considered. Similarly, recharging batteries must be taken into account (during descent, on ground, etc).

#### Summary/Conclusions

At the current state of the art, turbogenerators are the most promising technology for supplementary electricity aboard commercial hybrid electric aircraft. Batteries begin to be competitive with turbogenerators at 1000 W-hr/kg on the basis of specific energy, however, non-ideal performance may require even higher specific energy. This analysis of battery weight did not include specific power which may also significantly impact battery weight. A turbogenerator operating on jet fuel or LNG is the best option from the point of view of weight for larger energy storage quantities. Fuel cells are outperformed by batteries and turbogenerators except for applications requiring > 1300 kWh where noise and detectability are valued and liquid hydrogen is available.

---

## Appendix D — Step 6 as it stands now (body only; paragraph numbers in bold brackets)

**[1]** ### The second half: cruise carried on a wing

**[2]** ### The opponent, and the axis

**[3]** On this axis the alternative is the rotorcraft, multirotor and helicopter alike, and as in the previous section the comparison
runs one way only. **Nothing here is claimed against fixed-wing aircraft.** The claim is
confined to the one thing the rotorcraft family structurally lacks: **a surface that carries the
cruise lift.**

**[4]** ### What the requirement is

**[5]** Section 5 established the first half: the aircraft must leave from and return to a site that
supplies nothing. **A rotorcraft meets that requirement completely.**

**[6]** What it does not meet is the second half of both missions. Wildfire observation and response,
and cargo delivery to places without a runway, each require the aircraft to **cover distance
after it has left the unprepared site**, and a vehicle with no wing buys every second of that
distance with installed power. The consequence has been stated independently: surveying the
field, one study concludes that multirotors are efficient in hover and suited to short-range
missions, while vectored-thrust aircraft are efficient in cruise and suited to long-range ones.

**[7]** ### What the configuration does instead

**[8]** **Cruise lift is carried by the airframe itself.** There is no separate fuselage: the whole
planform is the wing, so every part of the body that is carried is also a part that lifts. At
the cruise condition the lift coefficient follows from `C_L = W/(qS)`, the drag from
`C_D = C_D0 + C_L²/(πARe)`, and the nose pair is left with one job — producing the thrust that
balances that drag. It supports none of the weight.

**[9]** That is the whole of the difference, and it is worth stating in those plain terms because the
consequence is structural. **A rotorcraft's rotors must produce the lift and the propulsive force
together, throughout cruise.** This aircraft separates them: a surface holds the aircraft up and a
propeller pushes it along, and **the wing produces its lift without a separate continuous power
supply of its own** — the power the aircraft spends in cruise goes to overcoming drag, of which
the lift's share is the induced part.
Lift is carried on a surface or it is carried on rotors, and no sizing contract, no assumption
in this paper and no choice available to a designer moves a vehicle between those two states.

**[10]** **But the size of the resulting advantage is a calculation, not a consequence of that
statement**, and the two must not be run together. The rest of this section is the calculation,
and it gives a smaller number than the structural statement invites.

**[11]** ### What the margin actually is, in one currency

**[12]** The sizing set of Section 4 reports an **effective lift-to-drag ratio**, defined in its own
nomenclature as `L/De = WV/P`: weight times speed over power. That is a system figure of merit,
not a force ratio, and it already contains the propulsive efficiency of whatever produces the
thrust. **A force ratio cannot be placed beside it.**

**[13]** Converting this configuration's aerodynamic ratio into the same quantity is one line: in level
cruise thrust equals drag and lift equals weight, so with shaft power `P = DV/η_p`,

**[14]** > **L/De = WV/P = (L/D) · η_p**

**[15]** **Which power `P` denotes is not assumed here**, because reading it as electrical power rather
than shaft power would make this configuration's figure incomparable with the published one. The
source settles it in its hover formulation: hover power is written `Ph = W√(W/2ρA)/FM`, with the
figure of merit already applied — shaft power — and the propulsion-system efficiency applied
separately outside it. The cruise formulation uses the same separation, writing cruise energy as
`Pc/ηc` with `Pc = WV/(L/De)`. That separation appears in the source's **battery-capacity**
derivation, so it holds for the all-electric entries as well as the shaft-driven ones: if `L/De`
already contained the electrical chain, that derivation would count it twice.

**[16]** **Neither factor is a single number, and they are two different kinds of spread.**

**[17]** The aerodynamic ratio is **8.79 to 10.82**, with the tip frames and the free-wheeling attitude
rotors already charged. That spread is **uncertainty**: it is the zero-lift drag bracket, and a
designer does not get to choose where in it the real aircraft lands.

**[18]** The cruise propeller efficiency is **0.632 to 0.683** across the nose-blade families that meet
the hover figure of merit — two and three blades per rotor, at two target section lift
coefficients, each solved at its hover and its cruise condition. That spread is **not
uncertainty**: it is a design variable this study has not fixed.

**[19]**

| L/De | η_p 0.632 | η_p 0.683 |
|---|---:|---:|
| **L/D 8.79** (adverse drag) | 5.56 | 6.00 |
| **L/D 10.82** (favourable drag) | 6.84 | 7.39 |

**[20]** **These are the bounding corners of a product, not four simulated aircraft.** Two readings follow
and both are given, because choosing between them requires something this section does not have:

**[21]** - **Examined envelope, 5.56 to 7.39.** **The four corners are not demonstrated aircraft
  states**, and nothing here
  shows that a built aircraft would land simultaneously on both bounds.
- **Best examined blade family, 6.00 to 7.39.** The highest efficiency among the families
  examined is 0.683; holding it and sweeping only the drag bracket gives this range.

**[22]** **Whether 0.683 is the blade a designer would actually choose is not settled here**, and saying
so is the point. It is the best of the four *on cruise efficiency under the hover figure-of-merit
constraint*. Blade count and section loading also govern structural loads, acoustics, the motor
operating point, rotor inertia and manufacture, and **none of those is modelled in this work**.
Section 10 is where one blade is carried into a closed sizing loop; until then this section stays
at envelope level and does not present any corner as the aircraft's performance.

**[23]** ### What the comparison gives, against both published quadrotors

**[24]** The sizing set contains two quadrotors for the same mission, and **neither is treated here as the
primary one.**

**[25]**

| | L/De | vs examined envelope 5.56 – 7.39 | vs best examined family 6.00 – 7.39 |
|---|---:|---|---|
| Quadrotor, turboshaft | 4.9 | +13 % … +51 % | **+22 % … +51 %** |
| Quadrotor, all-electric | 5.8 | −4 % … +27 % | **+3 % … +27 %** |

**[26]** **Against the turboshaft quadrotor the sign holds at every corner of both readings.** Closing it
would need the propeller efficiency to fall to 0.557, against 0.632 for the least efficient blade
family examined.

**[27]** **Against the all-electric quadrotor it does not hold at the low corner**, and that result is
reported as a result rather than as a caveat. That vehicle reaches 5.8 — above this
configuration's 5.56 — and it buys the difference with 1 742 lb of battery and nearly twice the
gross weight for the same mission, 7 221 lb against 3 678 lb. **That higher gross weight is
consistent with the mass charge Section 2 describes**, and Section 4 is where the independent
sizing evidence for it is set out — the comparison in this table does not establish the causal
link by itself. On cruise efficiency taken alone, the entry is ahead of this configuration's low
corner, and whether it is ahead of the best examined blade family depends on the drag bracket.

**[28]** The same sizing set gives its two helicopter types at 5.4 to 7.2, and against them the result is
mixed: this configuration is ahead of the turboshaft single-main-rotor helicopter at every corner,
the two middle entries fall inside its envelope, and only its top corner is ahead of the
all-electric side-by-side helicopter, which has no wing either. The qualifications below apply to
these entries as they do to the quadrotors.

**[29]** **So the second claim is narrower than the structural statement invites.** Carrying cruise lift on
a wing is worth **roughly a quarter to a half against the turboshaft reference, and against the
all-electric one it ranges from slightly behind to comfortably ahead depending on the drag outcome
and the blade** — a measurable advantage, not a change of category. And what
compresses it is not the wing. **It is the cruise efficiency this aircraft's fixed-pitch blade
delivers:** at a propeller efficiency of 0.85 the same airframe reaches 7.47 to 9.20. Whether a
variable-pitch hub would recover that difference is not computed; Section 11 reports the gap and
declines to attribute all of it to the hub.

**[30]** ### Five qualifications: three run against this configuration, one has no computed direction, and one bounds what the comparison can be called

**[31]** They are given together because omitting any one of them would make the comparison look better
than it is.

**[32]** **Scale.** The compared vehicles are 1 660 to 3 275 kg; the designs here are of order 50 kg and
1 000 kg — Section 10 closes the light one between 52.3 and 57.5 kg across the same bracket.
Reynolds number favours the larger aircraft, so the smaller design is at a disadvantage in this
comparison rather than an advantage.

**[33]** **The quadrotor is a good quadrotor.** Its disc loading is 3.5 lb ft⁻², and the all-electric one's
is 3; both are unusually low. Nothing here is compared against a poor example.

**[34]** **The speeds are not matched, and the direction of that mismatch is calculable.** The published
figure is quoted at the best-range speed; this configuration's is at its chosen cruise condition,
1.49 times stall, which Section 10 states explicitly is **not** its best lift-to-drag point. The
best point lies at 1.26 times stall, and `L/D_max = 0.5√(πARe/C_D0)` exceeds the cruise ratio at
both ends of the drag bracket — 11.65 against 10.82, and 10.08 against 8.79, both at e = 0.817.
**The reference is
therefore given its best speed and this configuration is not given its best speed, and the margin
is positive anyway.** The best point is not an available option — cruising there leaves too little
margin above the stall — so this fixes a direction, not a magnitude.

**[35]** **The atmospheres are not matched.** The published sizing mission is flown at *"5,000-ft altitude
and ISA + 20°C"*; every number in this work is at sea level, with a sea-level drag polar and a
sea-level blade solution. **The direction of that mismatch is not claimed here**, because it has
not been computed: the altitude sweep in this work measured the effect on hover power and on
propeller efficiency, not on a cruise comparison at a re-trimmed best-range speed.

**[36]** **The analysis chains are not matched, and this is the qualification that bounds what the
comparison can be called.** The published value is the output of an integrated conceptual-design
system with a comprehensive rotor analysis behind its rotor performance. The value here is
assembled from a drag build-up, a drag polar at a prescribed cruise condition, and a separate
blade-element propeller solution. There is a second difference inside that one: **the published
value is the effective ratio of a fully sized vehicle, while the value here is a converted
performance metric at a prescribed cruise condition, taken before the sizing closure Section 10
reports.** So this is a comparison of two independently produced figures in a common definition,
not a controlled numerical reproduction, and nothing in it should be read as validation of either,
or as a completed aircraft-level comparison.

**[37]** ### What is sized, and what is not demonstrated

**[38]** **Sized.** The drag build-up and its bracket; the lift-to-drag ratio at the cruise condition
from the drag polar; the propeller efficiency from blade-element momentum theory at two
operating points; and the range that follows from the chain, link by link.

**[39]** **Not demonstrated.** **No part of this has been measured.** There is no wind-tunnel test and no
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

**[40]** ### What this half costs

**[41]** The wing that makes cruise efficient is carried through the vertical phase, where it produces
nothing and presents the aircraft's largest surface to ground wind. The tailless planform that
follows from having no boom constrains the sweep, because with no horizontal stabiliser the
pitching moment must come from the distribution of lift along the body itself. And the
fixed-pitch propeller that serves both regimes is the reason the margin above sits where it does
rather than higher. Section 11 charges all three.

**[42]** **The two halves are now on the table separately. Section 7 is where they are combined**, and
the combination is what this paper is for.

