# Round 185 — Stage 4 closed. The author's plan: a pass over Section 1, then a last part–whole–part look, then submission

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`33242c5`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text.

---

## 0. Round 184 closed

**All five of us confirmed:**
- the five changed paragraphs of 2.3;
- the six pointers into it. The 4.5 pointer is satisfied by the isolated pair, which stays in the body.

Grok's first reply answered Round 183; the resent Round 184 brought its confirmation, and paragraph 4 (sentence 38) included.

**Decisions:**
- **Sentence 19** (*"It is used for three reasons …"*): K from all five, so **it stays.**
- **Stage 4 is closed.** No section was merged. 2.3 lost 181 words.

**The body now:**
- about **13 411 words** of prose (tables excluded);
- Section 2 about 2 970 words;
- 145 protected sentences in the body, 31 in the supplement.

**The author's plan (my translation):**

> *"Yes, to me too the shortening seems enough. You said we could look at 1. Let us go over 1. Then I will ask for a part–whole–part look (it need not shorten anything; a last look). After that we move to the submission stage."*

So:
- **the shortening is over;**
- **this round opens a pass over Section 1;**
- then comes a whole-paper reading, which need not cut anything;
- then submission. Submission includes the journal's own instructions on length and figures. I could not open them from this environment; the author has been asked for the PDF.

---

## 1. What this pass is

**Section 1** was last passed in Rounds 175–176, before stages 2–4. It is the reader's first contact with the paper, and it promises what the body delivers. **This is not a length pass.** A change can be proposed for any of these reasons:
- **Clarity in one reading** (the author, Round 150: *"If it cannot be understood, being right loses its value"*, my translation).
- **Match with the body as it now stands.** Every pointer, every promise, every item of the gap statement.
- **The §0 boundaries.** In brief:
  - range is claimed against rotorcraft only;
  - runway independence is claimed against fixed-wing only;
  - against tilting aircraft the claim is the mechanism count, not simplicity;
  - no range claim is made against the other hybrids.
- **Priority wording.** It is always in the *"not found / established"* form.
- **Preparing the reader for the claims.** Section 8 states them on four axes against four opponents. Does Section 1 set the reader up for that?

**Marks:**
- **K**: keep.
- **R**: rewrite; give the full new text.
- **C → n**: cut as a copy; name the receiver.
- **S**: move to the supplement.
- **A**: add; give the text and what it prepares.

**Rules:**
- Protected sentences are kept verbatim. Moving or rewriting one is the author's decision.
- A lengthening is allowed, but it must say what it prepares.
- The anaphora receipt applies to every cut.

---

## 2. Section 1 in full, sentence by sentence (from the assembled view at the commit above; 1 310 words)

| # | Sentence (bold removed) | Words | Status |
|---:|---|---:|---|
| | **1.1 Two families, two different limits** | | |
| 1 | Uncrewed powered flight is dominated by two configuration families, and neither is bounded by the thing the other is bounded by. | 21 | — |
| 2 | Fixed-wing aircraft carry payload over distance efficiently, because a wing sustains the vehicle without continuously spending power on lift. | 19 | — |
| 3 | Their limit is not aerodynamic but infrastructural: a runway, a catapult, or an equivalent installation. | 15 | — |
| 4 | Rotorcraft and multirotors remove that requirement completely. | 7 | — |
| 5 | They take off and land vertically, hover, and work from confined sites. | 12 | — |
| 6 | Their limit is the converse: with no wing, every second of flight is bought with installed power, so range and endurance stay modest and worsen as the vehicle grows. | 29 | — |
| 7 | Neither family is deficient. | 4 | — |
| 8 | Each is limited by the price of doing it that way. | 11 | — |
| 9 | The corner where both capabilities are wanted at once is where the two applications this work is aimed at sit — wildfire observation and response, and cargo delivery to places without a runway. | 33 | — |
| 10 | That corner is not empty, as the rest of this section sets out; what is unsettled is which price an architecture in it must pay, and whether one arrangement pays less than it appears to. | 35 | — |
| | **1.2 What the contemporary answers do, and how each changes regime** | | |
| 11 | Hybrid VTOL aircraft occupy that corner today. | 7 | — |
| 12 | This paper does not dispute that they work. | 8 | — |
| 13 | They take two routes between the regimes: lift-plus-cruise aircraft keep two sets of hardware and switch between them, and tilting aircraft keep one set and reorient it (Section 5.1). | 29 | — |
| 14 | Rotating a propulsor in flight brings a pivot and its actuators, a gyroscopic moment during the rotation, and a control problem through a regime in which the aircraft is neither a rotorcraft nor an aeroplane. | 35 | — |
| 15 | Those are mechanical and control requirements rather than aerodynamic ones, and that distinction is what this paper is built on. | 20 | — |
| | **1.3 The third route is established, and some of its difficulties are inherited** | | |
| 16 | There is a third way to put one set of propulsors into both regimes without reorienting them: point the thrust line at the ground and let the whole aircraft rotate. | 30 | — |
| 17 | The Convair XFY-1 flew it in 1954 and completed six transitions to conventional flight "before testing was curtailed because of engine and gear-box reliability problems", and uncrewed tail-sitters have revisited the route since. | 33 | — |
| 18 | The pilot's spatial orientation and workload were real, but they are not what curtailed the testing, and they are the only one of those documented obstacles an uncrewed aircraft removes. | 30 | protected |
| 19 | Some of the difficulties were real, internal, and are inherited here. | 11 | protected |
| 20 | A tail-sitting vertical descent is harder than a runway landing; a tail-sitter on the ground is more exposed to crosswind; and propellers whose thrust vectors are all parallel to the body axis produce no rolling moment by any combination of thrust settings. | 42 | — |
| 21 | The reaction-torque channel that other coaxial tail-sitters use about that axis is a choice this configuration declines rather than a limit it inherits (Sections 5.1 and 5.2). | 27 | protected |
| 22 | What has changed is electric drive on each individual rotor, sensor-based attitude reference, and enough onboard computation that stability need not come from the airframe alone, and the uncrewed tail-sitter literature has been exploiting exactly those three for over a decade; the gap below is not a historical one. | 49 | — |
| | **1.4 What is already occupied, stated before the gap** | | |
| 23 | The route itself is established. | 5 | — |
| 24 | Uncrewed tail-sitters combining fixed-pitch rotors with a flying wing have been built and flown for more than a decade. | 19 | protected |
| 25 | A tail-sitter study reported in 2007 already states the comparison: tilting configurations reach the same goal "at the expense of significantly increased mechanical complexity compared to a tail-sitter that uses propeller wash over normal aircraft control surfaces to effect vertical flight control." | 42 | — |
| 26 | Attitude without aerodynamic control surfaces is established: a quadrotor tail-sitter operated without control surfaces, with experimental verification, was reported in 2013. | 21 | — |
| 27 | Coaxial contra-rotating propulsion on a tail-sitter is established, proposed to cancel a single propeller's reaction torque without complementary controls, at a cost its proposers name as added mechanical complexity; a tail-sitting micro air vehicle reported in 2014 uses a coaxial pair for the same purpose. | 45 | — |
| 28 | The established answer to hover control on such a configuration is a surface in the slipstream, and this paper refuses it. | 21 | — |
| 29 | The 2014 vehicle places an elevon and a rudder in the propeller slipstream for three-axis control in hover; a flying-wing tail-sitter reported in 2018 uses elevons for two of its three axes and treats the propellers' counter-moment about the thrust axis as a disturbance rather than a control channel, and reports hover and vertical flight only. | 56 | — |
| 30 | And the reaction-torque channel this paper declines is established as a control channel. | 13 | — |
| 31 | A coaxial contra-rotating tail-sitter reported in 2012 balances rotor torque by counter-rotation and unbalances it on purpose to steer: its published control scheme assigns "differential velocity of the two motors" to yaw in the vertical mode and to roll in the horizontal one. | 43 | — |
| 32 | Those are the same physical channel under two names, a moment about the propeller axis, and independently driven rotors make it available to any coaxial pair. | 26 | — |
| 33 | Using it is a choice, and so is declining it, which is what separates this configuration's control problem from a physical impossibility. | 22 | protected |
| 34 | A blended-wing-body tail-sitter with contra-rotating propulsion, aimed at disaster response, is established, reported in 2025 with vortex-lattice and RANS analysis. | 20 | — |
| 35 | A buffered series hybrid on a winged tail-sitter has been sized: a 2026 study of 100 kg winged biplane tail-sitters sizes the engine for cruise and a boost battery for vertical take-off and landing, and gives its rotors collective pitch change mechanisms. | 42 | — |
| 36 | A coaxial tail-sitter with a series-hybrid store has been sized: a long-endurance concept reported in 2025, with a fuselage and tails, whose fuel cells charge a battery that drives the motor, because the fuel cell alone cannot fully power hover out of ground effect at take-off; how its attitude is controlled, and whether its rotors vary pitch, the paper does not state. | 62 | — |
| 37 | And the propeller compromise at the centre of this paper's own ledger is a known result, not a discovery. | 19 | — |
| 38 | The uncrewed tail-sitter literature states that fixed-pitch propellers make it "theoretically impossible to be very efficient in both hovering and forward flight." | 22 | — |
| 39 | A long-range tail-sitter reported in 2018 names variable pitch as the remedy, at the cost of extra actuators and mechanism weight, and even with cyclic and collective pitch still sizes its rotor as a compromise between hover and forward flight. | 40 | — |
| | **1.5 The gap, stated precisely** | | |
| 40 | Each half of the required capability is well served, and both halves together are served by the contemporary hybrids. | 19 | — |
| 41 | This paper does not claim otherwise. | 6 | — |
| 42 | And the third route is occupied. | 6 | — |
| 43 | What follows is therefore not a claim to an empty field. | 11 | protected |
| 44 | What is not established is the combination taken together with its price. | 12 | protected |
| 45 | Specifically: a blended-wing-body tail-sitter in which every propulsor is a coaxial, torque-balanced pair — so that reaction torque and net angular momentum are given up along with the reorientation mechanism — carrying no aerodynamic control surfaces beyond a single moving device, powered through a buffered series hybrid, and audited explicitly against carried hover mass, exposed cruise drag and hover-sized continuous power, the last two of them at two scales, and under three sizing contracts. | 74 | — |
| 46 | Each of those choices costs something, and the giving-up is the part that is not free. | 16 | — |
| 47 | Operating every pair torque-balanced spends the reaction-torque channel to buy the torque balance and the near-zero net angular momentum, and leaves the axis to a single aerodynamic device. | 28 | — |
| 48 | None of the elements is new, and Section 5.1 says so. | 11 | protected |
| 49 | Tail-sitting aircraft are seventy years old; blended wing bodies have been a standing subject of transport research for more than three decades; series-hybrid propulsion has been flown in a crewed motor glider and designed for small uncrewed aircraft. | 38 | — |
| 50 | The route is not claimed to have been waiting to be found. | 12 | protected |
| 51 | The contribution is the architecture: a configuration arranged to change regime by rotating the airframe rather than its propulsors, and so carrying no mechanism that reorients a propulsor. | 28 | protected |
| 52 | The combination, the consequences of the choices inside it, and an accounting of what they cost are how that contribution is presented and priced. | 24 | — |

---

## 3. What my check found. These are facts, not proposals: my view comes next round, beside yours

**Pointers out of Section 1, as the body now reads:**

| Sentence | Pointer | What the receiver says | Receipt |
|---|---|---|---|
| 13 | *"(Section 5.1)"* for the two routes | 5.1: *"The lift-plus-cruise design of the NASA study used in Section 2.3 carries its lifting rotors through cruise … its tilt-wing turns eight proprotors … on a tilting wing and tail."* | R1 |
| 21 | *"(Sections 5.1 and 5.2)"* for the declined reaction-torque channel | 5.1: *"… this configuration declines that channel by design (Section 5.2)"*; 5.2: *"the reaction-torque channel that could (Section 1) is declined: every pair is operated torque-balanced."* | R1 |
| 48 | *"Section 5.1 says so"* | 5.1 opens: *"None of the three elements is new. Each can be found on its own, and some of them together, in the literature and in hardware — Section 1 says where."* | R1. **The two sections point at each other** for the same statement |
| 45 | *"… the last two of them at two scales, and under three sizing contracts"* | 6.3: the 50 kg and 1 000 kg reference designs (Bill 1 enters both as inputs, 3.6 and 4.0 percent); 6.4: *"three contracts to three architectures at each of the four closures"* | R1 |

**The gap statement (45, 47) against 5.2:**
- 45: *"… carrying no aerodynamic control surfaces beyond a single moving device …"*.
- 47: *"… leaves the axis to a single aerodynamic device."*
- 5.2: *"one thing on this aircraft changes its configuration: the strip, deployable in two halves — one side alone for roll, both together as a speed brake."*
- These agree: one device, deployed in two halves. The *"speed brake"* use appears only in 5.2.
- 45's *"net angular momentum … given up"* against 5.2's *"nominally zero"*: they agree.

**Repetitions and word locks:**
- *"… for over a decade"* (22, on exploiting the three enablers) and *"… for more than a decade"* (24, protected, on building and flying the route).
- *"uncrewed tail-sitters have revisited the route since"* (17), *"The route itself is established."* (23) and *"And the third route is occupied."* (42): three statements that the route is occupied.
- *"Rotorcraft and multirotors"* (4) is a family-level phrase. Under the word lock (Round 99), the family-level term is *rotorcraft*.
- *"for more than three decades"* (49) must be checked against the submission date (Q-2). *"a 2026 study"* (35) is current.

**The four axes (Section 8) and where Section 1 touches them:**

| Axis | Where Section 1 touches it |
|---|---|
| Range against rotorcraft | 6 (the rotorcraft limit) |
| Runway independence against fixed-wing | 3 (the fixed-wing limit) |
| Mechanism against tilting aircraft | 14–15 and 51 |
| No range claim against the other hybrids | 12 (*"does not dispute that they work"*) and 40–41 |

No sentence of Section 1 names the four axes as such.

---

## 4. What I ask of you

| # | Item |
|---|---|
| a | **Marks, by sentence number**, only where you would change something. Silence means K. Give R and A in full text; C with its receiver; each with its reason from §1 |
| b | **§3's findings:** which of them need a change, and which are fine as they are. In particular, the mutual pointer between 48 and 5.1, the three "occupied" statements, and *"Rotorcraft and multirotors"* |
| c | **The axes:** should Section 1 prepare the four-axis structure of Section 8 more explicitly, or is the present preparation enough? If more, where and in how many words |
| d | **Your own proposals** (open, as always) |

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## 5. What goes to the author after this round

- **Nothing yet.** Next round your marks and mine go side by side.
- What the five of us agree then goes to the author as one list.
- Any rewrite or move of a protected sentence goes to the author in every case.

---

## 6. Errors (one list)

- **None new in Round 184.**
- Grok's first reply answered Round 183. It was resent, and the confirmation came.
- **DeepSeek:** attributed the heading-only trial to the author. The record shows it was our note (Round 169). The author said in Round 175 that the four headings were *"to create awareness"*, not a proposal.
- **DeepSeek:** expected that a heading trial would move the framework after the aircraft. That contradicts our unanimous *"2.3 stays before the aircraft."*
