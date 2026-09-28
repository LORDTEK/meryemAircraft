# "not …" classification of the step bodies (Round 138)

Rule (CLAUDE §3.0 (3), Round 135; ChatGPT): every negative sentence is one of
**Q** open quantitative question · **C** uncomputed comparative analysis · **B** broader unresolved question ·
**E** evidence limitation · **S** scope boundary. Step 14 holds only Q, C and B, each with a settlement method (Supplement S14).
Debt trace (DeepSeek, (4)): every Q, C or B outside Step 14 is checked against Step 14's list.

**Method.** `paper/v8/ALL-STEPS.md` split into sentences (Claude, Round 138). 340 sentences carry a negative (*not, no, none, nothing,
never, neither, nor, cannot, without, un-…ed*). About sixty of them state that something was not computed, shown, settled, established,
measured and the like; each was classified by hand below. The other 280 were read: most are claim limits, definitions, physical
statements or false positives (*"a site that has not been prepared"*); those that bear on open work are in the table too (the shafting,
the strip's split and actuators, the balance question, the indexing mechanism), and one physical statement raised a finding (marked †).

## Sections 1–13

| § | Sentence (key clause) | Class | Home in Step 14 | Note |
|---|---|---|---|---|
| 1 | *"What is not established is the combination taken together with its price."* | E (search-bounded absence) | — | Section 1's occupied list; `v8-gap-search.md` |
| 1 | *"The route is not claimed to have been waiting to be found."* | S | — | |
| 2 | *"Whether any architecture avoids the mismatch … is not settled here."* | S (pointer to Section 3) | — | |
| 3 | *"Rotating the airframe is permitted and is not priced here."* | S (definition scope) | pricing: the pitching moment through the transition | |
| 3 | *"… are not charged as duty-cycle mismatch under this accounting."* | S | — | |
| 3 | *"Whether such an architecture might avoid the three charges by some other route is a separate question this paper does not settle"* | S (reach of a definition) | — | the condition is *"a definition, not a law"* |
| 4 | *"It does not establish that the accounting is complete …"*; *"None is known to the authors."* | E | — | |
| 5 | *"Not demonstrated. The aircraft leaves the ground on its control propellers."* | B | closed-loop hover control (allocation) | |
| 5 | *"The vertical descent has not been analysed."* / *"an open question in Section 14"* | B | vertical descent and the landing transition | |
| 5 | *"no figure in this paper describes the landing transition"* | B | same | |
| 5 | *"Hover attitude control is sized but not demonstrated as a closed loop."* | B | closed-loop hover control | |
| 5 | *"What that refusal costs in authority and in response time is not computed, and Section 14 carries it."* | C | closed-loop hover control | hover context: state matches |
| 6 | blade family *"a design variable this study has not fixed"*; *"none of those is modelled"*; *"Whether 0.683 is the blade … is not settled here"* | Q | blade-family selection | |
| 6 | *"Whether a variable-pitch hub would recover that difference is not computed"* | C | the variable-pitch counterfactual | |
| 6 | *"The direction of that mismatch is not claimed here, because it has not been computed"* (atmosphere) | C | atmosphere | |
| 6 | *"not a controlled numerical reproduction … validation"*; *"No part of this has been measured."* | E | — | |
| 6 | *"the wing's exposure to ground wind is not priced in this work"* | Q | ground handling and landing loads | **N4** — covered by topic; the S14 row names the stance base, not the price |
| 7 | *"The means of stopping is not fixed by this study"* | Q | the tip pairs' stopped cruise state | |
| 7 | variable-pitch price *"not settled here"* | C | the variable-pitch counterfactual | |
| 7 | *"Part count, mass, failure modes and maintenance burden were not measured"* | S (no reliability claim) | — | |
| 7 | *"Whether this aircraft can actually perform the change … is not settled anywhere in this paper"* | B | the pitching moment through the transition | |
| 8 | *"What authority each axis actually has … is not settled by the ratio alone."* | B | closed-loop **hover** control | **S-60** — the sentence has no regime |
| 8 | transition assignment *"not settled in this paper"* | B | the pitching moment through the transition | |
| 8 | shafting *"an implementation question it does not settle"* | S | — | |
| 8 | *"What declining it costs is not counted in this work."* | C | closed-loop **hover** control | **S-60** — no regime; the channel is a roll channel in cruise |
| 8 | *"The split is an estimate: the slipstream boundary it rests on is not derived in this work."* | Q | the strip and the fairing | **N2** — S14 row does not name it; S-37 derivation is scheduled |
| 8 | *"How many actuators that is, this study does not fix."* | Q | the strip and the fairing (actuation) | |
| 8 | torque residual absorption *"which this study has not shown"* | Q | closed-loop hover control (residual) | |
| 8 | shaft power of commanded departures *"is not computed"* | Q | shaft power off the free-wheeling state | |
| 8 | *"Neither the means nor the azimuth is fixed by this study"* | Q | the tip pairs' stopped cruise state | |
| 8 † | *"The stability of this configuration is not airframe-borne — it is produced by differential thrust and by the strip"* | (physical statement) | — | **S-59** — the preceding paragraph sizes the fairing for directional stability |
| 9 | *"It is not a list of the study's open questions."* and the eight non-claims | S | — | |
| 9 | refusal cost *"is not computed anywhere in this paper"* | C | closed-loop **hover** control | **S-60** |
| 9 | *"Whether eliminating it is favourable on balance is a question this work does not settle"* | B | closed-loop **hover** control | **S-60** |
| 9 | *"The separate claim that this aircraft can actually perform the regime change is not settled"* | B | the pitching moment through the transition | |
| 9 | *"No aircraft has been built, no wind tunnel has been run on this geometry"* | E | — | |
| 10 | *"The blade family is a design variable this study has not fixed"* | Q | blade-family selection | |
| 10 | *"Whether a real aircraft loses 5.4 m, more, or less is not settled by anything here."* | B | the pitching moment through the transition | |
| 10 | *"It does not establish that the package exists."* | E | the known obstacle (store) | |
| 10 | *"no rotorcraft is sized in this work, so no range comparison is made against one"* | S | — | |
| 11 | *"No stopped-state counterfactual was computed."* | C | the tip pairs' stopped cruise state | |
| 11 | *"No variable-pitch counterfactual was computed"* | C | the variable-pitch counterfactual | |
| 11 | *"Rotor–structure and rotor–wing interference is not modelled"* | Q | interference | |
| 11 | *"What the closure does not contain"* list | Q/B/C | each item in Step 14 (receipt audit) | "closed-loop hover control": **S-60** |
| 11 | *"The buffer fraction is an input to the loop, not a result of it."* | E | the known obstacle | |
| 12 | *"the third is not tested"*; *"Bill 1 is not tested"*; *"Whether the two are separable here is not established"* | E (the buffer is an input; the one derivation would not test it) | — | **question to readers**: E, or a Step 14 item? |
| 12 | *"It cannot show that they are independent in general"*; *"not a verification of separability as a general …"* | S / E | — | |
| 12 | *"no closure was run at 1 000 kg"* | S | — | |
| 13 | competitor propeller efficiency *"assumed, not computed"*; lift group and tilt mechanism *"Neither figure is measured."* | Q | the competitor's cruise propeller efficiency; lift-group mass | |
| 13 | indexing mechanism *"whose mass is not separately charged"* | Q | the competitor's lift-group mass | inside the assumed fraction |
| 13 | *"Where the reversal falls is decided by quantities this study has not measured or not fixed"* | Q | blade family; lift-group mass; propeller basis | |
| 13 | *"this paper has no mission that would decide, and does not choose"*; *"an ordering against a bound is not a result"* | S | — | |

## Section 14 (the home) and Section 15 (consumes it)

| § | Sentence | Class | Note |
|---|---|---|---|
| 14 | *"how long each draws the peak is not computed here"* | Q | the buffer's energy |
| 14 | *"whether the airframe fraction holds at twice the mass it was set at is not established"* | Q | the airframe's mass (S14 row names the re-closure masses) |
| 14 | *"how they would move with a measured store is not computed"* (Section 13's orderings) | C | sits in the known-obstacle part, without its own settlement line; my view: the settlement is the re-closure already described |
| 14 | *"The package Section 10 closes on does not exist with any store the sources consulted here report as built."* | E | the S14 *"Other store types"* row bears on it: **R-9**, **N3** |
| 15 | five negatives | — | consumed; `15-maps.md` |

## Findings

- **S-59** (Step 8, frozen source). *"The stability of this configuration is not airframe-borne"* ↔ the fairing paragraph just before it,
  which sizes the fairing to C_n_β > 0.001 per degree for directional stability. Absolute and regime-free.
- **S-60** (Steps 8, 9 ↔ Step 14 and S14; frozen source). The cost of declining the reaction-torque channel and the authority of each
  axis are stated without a regime; Step 14 and S14 carry them only inside *"closed-loop hover control"* (*"Bears on: whether hover is
  controllable"*). The channel acts about the body roll axis — a change of heading in hover, bank in cruise (Section 8; S14 strip row).
  Closed-loop control in cruise — where Step 8 says stability is *"actively commanded"* — is in no list (searched: body and supplement).
- **R-9** (Claude, Round 124; confirmed by all in Round 128). The S14 *"Other store types"* row says *"A supercapacitor store, or a
  battery–supercapacitor combination, is tabulated"*. Rheaume and Lents' Table 1 has one Super-Capacitor row, with two ranges from two
  cited sources; there is no combination row. The combination appears only in the survey's qualification sentence.
- **N2** (minor). The strip's slipstream split is an estimate not derived; the S14 strip row does not name it. S-37's derivation is
  scheduled before submission; if it fails, the item enters S14.
- **N3** (list completeness, reverse). S14's table has nineteen rows; Step 14's body list has eighteen. The extra row, *"Other store
  types"*, was placed in the supplement only by the Round 127 vote.
- **N4** (minor). The ground-wind price (Step 6) is under *"ground handling"* by topic; the S14 row names the stance base but not the price.
