# Round 212 — Two splits to settle (P22's added sentence; the rotation-time subsection); S13 (contracts) drafted

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text, including Section 6.4 in full.

---

## A. Closed in Round 211 (all four, and me)

- **S12: P24 and P25 are R1.** Closed.
- **The S12 changes are accepted:** the 5 to 14 percent shown as arithmetic, the excluded candidates named, and the unreproduced 220 kW and 13 kW left out.
- **DeepSeek and Qwen withdrew the forms that changed the protected Bill 3 sentence.** Both noted their own Round 210 errors.

---

## B. Two splits: please answer each other

### B1. P22: add one sentence after the protected Bill 3 sentence, or change nothing?

**The body now** (Section 6.2; the second sentence is protected and stays as it is):

> **But the full hover power passes through the electrical path, and that path is sized by it.** **Bill 3 is removed from the engine and left standing on the electrical system** (the propulsion-mass split is in Supplement S11).

**The proposal:** add, immediately after it, *"The sizing loop computes no hover-rated mass for the electrical path."*

| Reader | Position | Reason given |
|---|---|---|
| **Grok** | Add the sentence (the pointer change is a fallback) | A reader of the body alone meets the protected sentence; the limit should stand next to it. It names no fraction. |
| **ChatGPT** | Add the sentence (moved from *"no change"*) | The pointer says where the split is; the sentence says what the loop does not do. It makes no identification of the 0.108. |
| **DeepSeek** | **No change** (P22 R1); if forced, Grok's pointer change | The sentence before the protected one is the physical attribution. The pointer promises the split and the split is there, with its qualification. The body does not claim that the loop computes a hover-rated mass. |
| **Qwen** | Add the sentence | A reader sent to S11 looks for the hover-sized electrical mass, does not find it, and is confused. Better to say it in the body. |
| **Claude** | Add the sentence | The body's interpretability rule: *"A calculation result may remain in the body only if the body itself retains the minimum definition, model qualification and comparison needed to interpret that result."* *"Left standing on the electrical system"* is read as a cost the loop carries unless the body says it does not compute one. DeepSeek is right that the body never claims it does; the question is what a reader infers. |

**DeepSeek:** you said the added sentence is unnecessary. Is it **acceptable** to you? If yes, it is applied. **Grok, ChatGPT, Qwen:** please answer DeepSeek's reason directly.

### B2. The rotation-time subsection of S12

**The subsection as drafted:**

> The transition is where the square–cube relation is paid. The heavy design's pitch inertia is 255 times the light design's and its available control moment 41 times, so to keep the light design's moment margin it must rotate in about 5 s rather than 2 s (4.96 s computed; the heavy design uses 5.1 s). A larger aircraft of this type turns more slowly, and must.

| Reader | Position | Reason given |
|---|---|---|
| **Grok** | Keep, with the figures | The author moved the protected row here; the figures are the working under it, from the code, and none enters the body. |
| **ChatGPT** | Keep the protected sentence; **remove** the figures | Reproducibility is not permission: without a body pointer, the figures would add an unpointed analysis to the evidentiary record. |
| **DeepSeek** | Keep, with the figures | The missing pointer follows from the author's move, not from a defect in S12; the figures support the protected claim. |
| **Qwen** | **Remove the subsection** | No body pointer, so it adds a claim the body does not make. The protected sentence is orphaned. |
| **Claude** | Keep, with the figures | The protected sentence alone, with nothing under it, is an assertion. ChatGPT's rule bars a supplement from adding a claim the body does not make; here the claim was placed by the author's decision (E15), and the figures are only the working under it. Removing the figures leaves a protected claim with no support. Removing the subsection removes a protected sentence, and only the author can do that. |

**Qwen:** removing the subsection removes a protected sentence the author moved here (E15), so that option can only go to the author. Do you want it to? **ChatGPT:** does a protected sentence standing without its working meet your rule better than one standing with it?

If we do not converge, this goes to the author with three options: (a) keep with figures; (b) keep the sentence alone; (c) the author withdraws the row from the supplement.

---

## C. S13, drafted

S13 serves five pointers (P26–P30) and carries two protected rows. Every figure comes from `aero/contracts.py`, rerun this round; the output is identical to the stored result, and every range in the archive's tables matches it.

**Flagged changes:**
- **Added to the per-closure table:** the shift and the mass ratio under the first contract, both from the same output.
- ***"Put plainly,"* is not carried.** It precedes the protected sentence in the archive but is not part of the register text. I added an antecedent sentence for *"those quantities"*; it restates Section 6.4.
- **The no-buffer case (P27)** is stated only as far as the pointer goes: the lift-plus-cruise layout does not close under two contracts, and is 38 to 47 percent behind under the third. That case is not used in the comparison.

**What you are asked to check:**
- grade P26–P30;
- apply ChatGPT's rule;
- judge the flagged changes.

### Section 6.4, in full

#### 6.4 Rankings belong to contracts

Where one architecture pays less of one charge and more of another, the ranking depends on how the charges are weighed
(Section 6.3), and **a sizing contract is one such weighing**: it fixes what is held equal between the architectures being compared.
This section applies three contracts to three architectures at each of the four closures of Section 6.1. **The mechanism claim is not a
ranking and is not at stake here.**

##### Three contracts, and what each holds equal

Range in the sizing loop is proportional to L/D, to the energy chain and to the fuel fraction, and the three contracts differ
only in the last (Supplement S13): a **fixed fuel fraction**, sixteen percent of each architecture's own take-off mass; a **fixed fuel
mass**, the 8.4 to 9.2 kg this configuration carries; and a **fixed take-off mass and payload**, under which every kilogram of
architecture-specific hardware is a kilogram of fuel not carried. **These are three different questions, not three estimates of one
answer**, and this paper has no mission that would decide among them.

##### What is compared, and on what basis

Three architectures fly the same mission, 13 kg of payload at 30 m s⁻¹, with the same wing loading, disc loading and aspect ratio,
the same airframe and avionics fractions, and the same energy chain apart from the propeller. **The competitors are therefore this
planform with two add-ons, not independently designed aircraft of their families.** All three carry the same buffered series-hybrid
power system, so Bill 3 is held common and the comparison measures mass and cruise drag. **Holding Bill 3 common is a choice of
question, and it has a direction.** **The choice runs against this configuration**: without the buffer, and with engines rated to the
hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off mass (Supplement S13).

The basis is not symmetric. The lift-plus-cruise layout carries a lift-to-drag ratio transferred from a different airframe's
wind-tunnel campaign (Section 2.1), and its stopped lift rotors take an indexing mechanism (Section 5.1) whose mass is not charged. **The
tilting layout carries no cruise drag penalty at all. That is an idealisation in its favour**, and it makes the tilting layout a bound.
Both competitors are given a propeller efficiency of 0.80, assumed, against this configuration's computed 0.632 and 0.683, and a lift
group of 10 percent or a tilt mechanism of 5 percent of take-off mass. **Neither figure is measured.**

##### Against lift-plus-cruise: a trade, and the contract sets the exchange rate

**The two architectures trade one charge against another**: closed under a fixed fuel fraction, this configuration is 27 to 30 percent lighter, and the lift-plus-cruise layout cruises at a lift-to-drag ratio of 11.66 and 15.72 against 8.79 and 10.82, with a propeller at 0.80.

**The lift-plus-cruise layout is 55 to 84 percent ahead under the first contract, 28 to 54 percent under the second, and between 13 percent short and 7 percent ahead under the third; the shift from first to third is 67 to 77 percentage points at every closure**, at the declared lift-group fraction, and always toward the lighter aircraft. The per-closure numbers are in Supplement S13. **The sign itself changes inside the envelope under the third contract**: this configuration is ahead at the two closures with the higher-efficiency blade family and behind at the two with the lower. **A statement of which architecture has the longer range, made without its contract, would therefore be a statement about the contract.**

##### Against the tilting layout: a bound, not a ranking

**What the bound gives is a size, not an order.** Credited with no cruise penalty, the tilting layout is 93 to 141 percent ahead of this configuration under every contract at every closure; that margin is the room a real tilting aircraft's cruise penalties — nacelle drag, pivot fairing, hover-sized rotors flown as cruise propellers — would have to fill, and how much of it they fill is not computed. **A ranking against a competitor modelled as a bound is not a ranking, and no range claim is made against the tilting family in either direction.**

##### Section 2.1's prediction, tested

Section 2.1 predicted that such a ranking will move when the sizing rule changes, and can reverse. **The movement holds
everywhere**, against both competitors, toward the lighter arrangement as the contract weights mass more; **the reversal holds at two of
the four closures against lift-plus-cruise, and at none against the tilt bound.** Where it falls is decided by quantities this study
has not measured or fixed: the blade family in the base case, and across the sensitivity cases the competitor's lift-group mass and the
propeller basis (Supplement S13). **Which architecture ranks first under a fixed take-off mass is therefore decided, in this model,
by quantities this study assumes for the competitor rather than measures: its lift-group mass fraction and its propeller efficiency.**
What is robust is that the shift exists and runs toward the lighter aircraft.

##### What the framework asks of whoever uses it

**Each comparison states every charge in its own currency before any aggregate, names its contract, and states its asymmetries and their directions; an ordering is reported only with the contract it was computed under and, where its sign depends on an unmeasured quantity, with that quantity named.** This paper meets that for its own column (Section 6.2) and not for the competitors', whose kilograms and drag counts here are parameters and transferred ratios rather than an audit.

##### What this section does not establish

**The competitors are modelled at a coarser level than this configuration**: their drag is transferred or idealised, their propeller efficiency assumed and their architecture-specific mass a parameter. **Comparing computed figures against assumed ones favours whichever is assumed more optimistically** — in propeller efficiency both competitors, and with a common propeller efficiency the lift-plus-cruise lead under the first contract falls from 55–84 to 33–45 percent (Supplement S13); in drag the tilting layout, by assumption. **The comparison is at one size**: Section 6.3's 1 000 kg reference design has no closure, and none of its figures is used here. **And nothing here ranks architectures for a mission.** What this section establishes is narrower: **the same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property of the architectures alone.


### The draft

### S13. Contracts: working for Section 6.4

#### The three contracts

> *Provenance and changes:* for P26 (Section 6.4): "Range in the sizing loop is proportional to L/D, to the energy chain and to the fuel fraction, and the three contracts differ only in the last (Supplement S13) …". src: archive "Section 13's paragraphs as they stood before compression", "Three contracts, and what each holds equal". Checked against the code this round: aero/baseline.py menzil_ver() (R = f_fuel E* eta_chain L/D / g), sabit_yakit(), sabit_MTOW(); aero/contracts.py, rerun this round, output identical to aero/contracts-result.txt (fuel 9.20 / 8.94 / 8.56 / 8.37 kg at closures A-D).

Range in the sizing loop is R = f_fuel E* η_chain (L/D)/g, with E* the fuel's specific energy and η_chain the energy chain from fuel to thrust. The three architectures share E* and the chain apart from the propeller efficiency, which enters η_chain, and they differ in L/D. The three contracts differ only in the fuel fraction f_fuel:

1) fixed fuel fraction: every architecture carries 0.16 of its own take-off mass as fuel, so take-off mass cancels from range;
2) fixed fuel mass: every architecture carries the fuel this configuration carries at that closure, 9.20, 8.94, 8.56 and 8.37 kg at closures A to D, as a fraction of its own take-off mass;
3) fixed take-off mass and payload: every architecture is held at this configuration's take-off mass with the same 13 kg payload, and its fuel is what remains after its empty mass, so every kilogram of architecture-specific hardware is a kilogram of fuel not carried.

#### The per-closure numbers

> *Provenance and changes:* for P28 (Section 6.4): "The per-closure numbers are in Supplement S13." src: archive S13 first table (L4126-L4132); figures from aero/contracts.py, rerun this round. Added from the same output: the mass ratio under the first contract and the shift.

Range of the lift-plus-cruise layout relative to this configuration (positive: lift-plus-cruise ahead), and the mass ratio under the first contract:

| Closure | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass | Shift, first to third | Lift-plus-cruise mass / this configuration's, first contract |
|---|---:|---:|---:|---:|---:|
| A | +67.8 % | +40.2 % | +1.1 % | 66.8 points | 1.392 |
| B | +55.3 % | +27.5 % | −13.0 % | 68.3 points | 1.433 |
| C | +83.9 % | +53.5 % | +7.3 % | 76.6 points | 1.378 |
| D | +70.2 % | +40.1 % | −6.5 % | 76.7 points | 1.409 |

The tilting layout, credited with no cruise penalty, is 93 to 141 percent ahead under every contract at every closure.

#### Without the common buffer

> *Provenance and changes:* for P27 (Section 6.4): "… without the buffer, and with engines rated to the hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off mass (Supplement S13)". src: aero/contracts.py case (d), rerun this round: lift-plus-cruise "KAPANMADI" (does not close) under contracts 1 and 3 at every closure; under contract 2, -46.6 to -38.4 percent. Not used in Section 6.4's comparison.

If the competitors carry no buffer and rate their engines to the hover demand, the lift-plus-cruise layout does not close at any of the four closures under a fixed fuel fraction or a fixed take-off mass; under a fixed fuel mass it is 38 to 47 percent behind this configuration. This case is not used in Section 6.4's comparison; it shows only the direction of the choice to hold Bill 3 common.

#### Sensitivity

> *Provenance and changes:* for P29 (Section 6.4): "… across the sensitivity cases the competitor's lift-group mass and the propeller basis (Supplement S13)" and P30: "… with a common propeller efficiency the lift-plus-cruise lead under the first contract falls from 55–84 to 33–45 percent (Supplement S13)". src: archive S13 second table (L4136-L4144) and "Section 13's paragraphs as they stood before the Round 172 shortening" (L4417 version). Protected S13 rows carried: "With a lighter lift group … a reversal appears at every closure." (E15) and "The sign under a fixed take-off mass is not a result about the architectures; it is a result about those quantities." (E14; the archive's lead-in "Put plainly," is not part of the register text and is not carried). Figures from aero/contracts.py cases (a), (b) 5 % and 15 %, (c), rerun this round: every range and shift matches the archive table. The antecedent sentence for "those quantities" restates the body's Section 6.4.

| Case | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass | Shift, first to third |
|---|---:|---:|---:|---:|
| As declared (lift group 10 % of take-off mass, competitors' propeller efficiency 0.80) | +55 to +84 % | +28 to +54 % | −13 to +7 % | 67 to 77 points |
| Lift group 5 % of take-off mass | +55 to +84 % | +47 to +76 % | +36 to +65 % | 14 to 24 points |
| Lift group 15 % of take-off mass | +55 to +84 % | +8 to +31 % | −62 to −50 % | 117 to 134 points |
| All three at this configuration's propeller efficiency | +33 to +45 % | +6 to +17 % | −33 to −25 % | 65 to 72 points |
| Lift-plus-cruise drag as a fixed increment, not a ratio | +59 to +75 % | +31 to +45 % | −13 to +5 % | 67 to 75 points |

With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every closure; with a heavier one this configuration leads under a fixed take-off mass at every closure; with a common propeller efficiency a reversal appears at every closure. The quantities that decide the sign are assumed for the competitor rather than measured: its lift-group mass fraction and its propeller efficiency. The sign under a fixed take-off mass is not a result about the architectures; it is a result about those quantities.


---

## D. Your own proposals

Open, as always.

---

## E. Errors (one list)

- **DeepSeek and Qwen (Round 210, acknowledged by both):** forms that changed the protected Bill 3 sentence. Withdrawn.
- **Claude:** none found this round.
- **Grok, ChatGPT:** none found.

---

## F. What goes to the author

**Possibly B2.** If the five of us do not converge on the rotation-time subsection, it goes to the author with the three options in §B2. Otherwise, nothing.
