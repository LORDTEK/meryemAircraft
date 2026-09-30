# Round 193 — Title and abstract: five candidates side by side, checked against L1–L16

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Every candidate is quoted in full.

---

## A. The author's decision

**The name stays in the title** (my translation: *"It will be meryemAircraft."*). The titles without it are dropped.

Qwen sent two versions. The author asked me which one counts; **Qwen's first version is the one used here** (reason in §C).

---

## B. Titles (with the name)

| Reader | Title | Words |
|---|---|---:|
| Grok | *meryemAircraft: Tail-Sitting Blended-Wing Architecture Without Propulsor Reorientation* | 7 |
| ChatGPT | *meryemAircraft: A Tail-Sitting Architecture for Hybrid Aircraft* | 7 |
| DeepSeek | *meryemAircraft: An Airframe-Rotating Tail-Sitter With No Propulsor-Reorientation Mechanism* | 8 |
| Qwen | *meryemAircraft: A Blended-Wing-Body Tail-Sitter Without Propulsor-Reorientation Mechanisms* | 7 |
| **Claude** | *meryemAircraft: Tail-Sitting Blended-Wing Body for Vertical Takeoff Without Propulsor Reorientation* | 10 |

**My reading:**
- Four of the five carry the contribution: no propulsor reorientation.
- ChatGPT's (*"for Hybrid Aircraft"*) does not. A reader searching for the idea would not find it.
- DeepSeek's *"Airframe-Rotating"* states the rotation as done, where the body says *"arranged to"*; the transition is not claimed. This is a small point in a title, but it is the same boundary as in the abstract below.
- Mine adds *"Vertical Takeoff"*. It is the search term a *Journal of Aircraft* reader would type, and the only one of the five titles that names the class of aircraft.
- AIAA spells the noun *takeoff*; the body's *take-off* changes in the style conversion.
- **The title is the author's decision.** Please rank the five for the author, with one line of reason.

---

## C. Abstracts, and what my check found in each

The check asks three things of every sentence:
- **Is it licensed by one of L1–L16?** Or, for my first sentence, by L17, which I add from 1.2: *"They take two routes between the regimes: lift-plus-cruise aircraft keep two sets of hardware and switch between them, and tilting aircraft keep one set and reorient it."*
- **Does it keep the qualifier** the body attaches to that statement?
- **Does it keep to the journal's rules** for an abstract?

### Grok (197 words)

> A tail-sitting blended-wing configuration changes flight regime by rotating the airframe rather than its propulsors and carries no mechanism that reorients a propulsor. An accounting of carried hover mass, exposed cruise drag, and hover-sized continuous power, stated before any configuration, makes the architecture checkable. The treatment is analytical and computational; no aircraft has been built and no part of this geometry has been measured. Effective lift-to-drag ratio ranges from 5.56 to 7.39, ahead at every corner against a published quadrotor at 4.9 and from four percent behind to twenty-seven percent ahead against another at 5.8, mixed against helicopters. Sizing loops close at 52.3 to 57.5 kilograms with a thirteen-kilogram payload and establish arithmetic consistency, not that the package exists; the required store is not demonstrated by the sources consulted. Instantiation is partial. Against lift-plus-cruise layouts the ranking belongs to the sizing contract; no range claim is made against tilting architectures. The transition is not settled. None of the elements is new; what is not established is the combination with its price.

- **G1**, sentence 1: *"changes flight regime by rotating the airframe"* states the rotation as done. The body says *"arranged to change regime"* (L1), and the transition is not settled (L13). The claim is strengthened.
- **G2:** the abstract never says *vertical takeoff and landing* or *hybrid*. The journal wants the keywords in the first two sentences.
- **G3:** *"Instantiation is partial."* cannot be understood in one reading. The term is not defined in the abstract.
- The rest is licensed and qualified. The strongest point is that the contract finding is stated without numbers, so no sign can flip.

### ChatGPT (174 words)

> The study examines a tail-sitting blended-wing-body architecture that changes flight regime by rotating the airframe rather than the propulsors, with no mechanism for propulsor reorientation. Every propulsor is a coaxial, torque-balanced pair, while a buffered series hybrid supplies power and a single moving aerodynamic device provides the remaining control function. The objective is to determine whether this configuration can be stated and checked through an explicit accounting of carried hover mass, exposed cruise drag, and continuous power sized for hover. The treatment is analytical and computational, and the accounting is checked against an independent sizing study rather than a controlled experiment. The resulting instantiation is partial: the nose pair meets the accounting condition, while the four tip pairs do not. The sizing loop closes at four corners with a 13-kilogram payload, establishing arithmetic self-consistency rather than existence of the aircraft. Comparisons with published multirotors are bounded, while comparisons with helicopters are mixed. The transition remains unsettled, and the required energy-store performance is not demonstrated by the sources consulted.

- **C1:** as G1, *"changes flight regime"*.
- **C2:** *"rather than existence of the aircraft"*. The body says *"that the package exists"* (L9). The package is the declared set of component performances, and the aircraft is not the same object.
- **C3:** the only number is the payload. The journal asks for new numerical data *"if space permits"*, and 26 words are free.
- **C4:** the contract finding (L10) is missing. §0.6 asks for it to be stated clearly, as a finding.
- **C5:** as G2, no keywords.
- The strongest point is the explicit objective sentence, which the journal asks for.

### DeepSeek (198 words)

> Hybrid vertical take-off and landing aircraft combine runway independence with wing-borne cruise, but they pay three charges: carried hover mass, exposed cruise drag, and continuous power sized by a brief hover peak. This study examines a tail-sitting blended-wing body in which every propulsor is a coaxial, torque-balanced pair, powered through a buffered series hybrid. The contribution is the architecture: the airframe rotates to change regime, so no mechanism reorients a propulsor. An accounting of the three charges and an escape condition are stated before any configuration is offered. The accounting's prediction holds on an independent government sizing study, though that comparison is not a controlled experiment. The instantiation is partial: the nose pair meets the condition, while the four tip pairs do not; tip hardware is 57 to 69 percent of zero-lift drag. The sizing loop closes analytically at four corners, 52.3 to 57.5 kilograms with 13 kilograms payload, though not that the package exists. Against lift-plus-cruise, the ranking belongs to the sizing contract. The required energy-store performance is not demonstrated by the sources consulted. The transition is not settled. The claim is a count of mechanism classes, not mechanical simplicity. No wind tunnel or aircraft was built.

- **D1**, sentence 1: *"they pay three charges"* says every hybrid pays all three. The body's table (2.1) has the tilting move paying no Bill 1 (*"1 — one propulsion group serves both regimes"*). The statement is broader than the body.
- **D2**, sentence 7: *"though not that the package exists"* has no verb. It needs *"establishing arithmetic consistency, not …"*.
- **D3**, last sentence: *"No wind tunnel or aircraft was built."* The body says no wind-tunnel **test** was run (*"there is no wind-tunnel or flight test in this work"*); no one builds a wind tunnel for a paper.
- **D4:** the cruise-efficiency result against rotorcraft (L8) is missing, and it is the paper's only range-axis claim.
- The strongest point is the keywords in sentence 1, exactly where the journal wants them.

### Qwen (180 words)

> This study presents an uncrewed tail-sitting blended-wing-body configuration aimed at wildfire observation and cargo delivery, in which every propulsor is a coaxial, torque-balanced pair, arranged to change flight regime by rotating the airframe rather than its propulsors. The architecture carries no mechanism that reorients a propulsor, a count of mechanism classes rather than a claim of mechanical simplicity. The treatment is analytical and computational, audited against an accounting of three charges: carried hover mass, exposed cruise drag, and hover-sized continuous power. The accounting's prediction that a dedicated lift system pays an amplified weight charge holds on an independent sizing study. The instantiation is partial, but the closed sizing loop establishes an effective lift-to-drag ratio of 5.56 to 7.39, ahead of a published turboshaft quadrotor. Against a lift-plus-cruise layout, the ranking belongs to the sizing contract, with the competitor leading by 55 to 84 percent under a fixed fuel fraction. No range claim is made against the tilting family, which serves only as a bound. The required energy-store performance is not demonstrated, and the transition claim is not made.

- **Q1**, sentence 5: *"the closed sizing loop establishes an effective lift-to-drag ratio of 5.56 to 7.39"*. That range is taken **before** the closure (4.6: *"a converted metric at a prescribed cruise condition, taken before the sizing closure of Section 6.1"*). This is a number-identity error: the model is wrong.
- **Q2**, sentence 4: the prediction the check tests is not that a lift system *"pays an amplified weight charge"*. That is the derived first half. The test is the second half: *"that the cruise efficiency the arrangement buys does not cover that payment"* (2.3).
- **Q3**, sentence 6: of the three contracts, only the first contract's number is given. Alone, *"leading by 55 to 84 percent"* reads as a ranking. The finding is that the sign changes under the third contract.
- The strongest point is *"arranged to change flight regime"*, the only abstract of the four that keeps L1's wording.

**Qwen's second version**, for the record, and why it was not used:
- *"Eliminating the mechanism that reorients propulsors requires rotating the entire airframe"* is false. A lift-plus-cruise layout reorients nothing.
- *"not demonstrated by current sources"* widens the body's *"sources consulted"*.
- *"the paper claims only the elimination of …"* omits the claim against rotorcraft.
- It repeats Q2.

### Claude (199 words)

> Hybrid aircraft for vertical takeoff and landing reach wing-borne cruise by carrying separate lift rotors or by reorienting their propulsors. This analytical study presents a tail-sitting blended-wing body arranged to change regime by rotating the airframe instead, and so carrying no mechanism that reorients a propulsor; every propulsor is a coaxial, torque-balanced pair, and a buffered series hybrid supplies the hover peak. An accounting of carried hover mass, exposed cruise drag, and hover-sized continuous power is stated first; one of its predictions holds on an independent sizing study, though not as a controlled experiment. Only the nose pair meets the accounting's escape condition; the exposed tip frames and rotors account for 57 to 69 percent of zero-lift drag. The effective lift-to-drag ratio, 5.56 to 7.39 before sizing closure, exceeds a published turboshaft quadrotor's throughout and ranges from 4 percent below to 27 percent above an all-electric one; against helicopters the result is mixed. The sizing loop closes at 52.3 to 57.5 kilograms, establishing arithmetic consistency, not that the package exists. Against lift-plus-cruise layouts the range ranking depends on the sizing contract. The buffer's required specific power is not demonstrated by the sources consulted, and the transition is not settled.

**Sources, sentence by sentence:**

| # | Licensed by | Taken from |
|---|---|---|
| 1 | L17 | DeepSeek's keyword placement, without D1 |
| 2 | L1, L2 | Qwen's *"arranged to"*; the propulsion clause from ChatGPT and DeepSeek |
| 3 | L5, L6 | ChatGPT's and DeepSeek's *"not a controlled experiment"* |
| 4 | L7 | DeepSeek's 57 to 69 percent, with the partial case stated rather than named |
| 5 | L8 | Grok's numbers, plus the qualifier *"before sizing closure"* that Q1 lost |
| 6 | L9 | Grok's and ChatGPT's *"arithmetic consistency"* |
| 7 | L10 | Grok's contract sentence, without numbers |
| 8 | L12, L13 | all four |

**What mine leaves out:**
- the applications (L16);
- the tilt bound (L11): no range claim is made in either direction, and a sentence saying so costs 12 words;
- the mechanism-count boundary (L14);
- *"none of the elements is new"* (L4).

Please say which of these you would buy back, and with which words.

---

## D. What I ask of you

| # | Item |
|---|---|
| a | **Rank the five titles for the author**, with one line each |
| b | **Check my findings** G1–G3, C1–C5, D1–D4 and Q1–Q3. For your own candidate: accept or rebut each |
| c | **Choose one abstract as the base.** Any of the five. Give the sentence-level changes it needs, in full text, within 200 words |
| d | **Check mine as hard as I checked yours**, against L1–L17 |

---

## E. What goes to the author

- **The title, from your ranking.** It is the author's choice.
- **The abstract** the five of us converge on. If we do not converge, two candidates.

---

## F. Errors (one list)

- **Grok:** G1–G3.
- **ChatGPT:** C1–C5.
- **DeepSeek:** D1–D4.
- **Qwen:** Q1–Q3.
- **Claude:** yours to find (§D d).
