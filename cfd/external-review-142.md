# Round 138 — The Vegh line is applied. The *"not …"* classification of the whole body: three defects and three smaller findings. Three evidence-record proposals.

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`c9b1968`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**

---

## 1. Applied — Proposal V (Step 1), for your confirmation

All four of you and I voted yes. The last clause stays (Q1, unanimous). *"reported in 2025"* stays as a placeholder, and the cited version
is fixed before submission (Q2, unanimous). It stands after the Rohith item and before *"And the propeller compromise …"*:

> **A coaxial tail-sitter with a series-hybrid store has been sized.** A long-endurance *"coaxial tailsitter concept"* with a fuselage
> and horizontal and vertical tails, reported in 2025, places its fuel cells *"in a series hybrid arrangement, providing electrical power
> to a battery that in turn provides electrical power to an electric motor"*, and the fuel cell alone is *"unable to completely power the
> aircraft in hover out of ground effect at takeoff"*; how its attitude is controlled, and whether its rotors vary pitch, the paper does
> not state.

**Checks after applying:**
- **Quotations.** Each was re-read in the manuscript: p. 4, p. 7, p. 13.
  - The p. 13 sentence reads in full: *"The fuel cell (and diesel engine for the diesel-electric case) was unable to completely power the
    aircraft in hover out of ground effect at takeoff for the baseline aircraft (and all aircraft sized for this study)"*.
  - *"the fuel cell alone"* is the fuel-cell branch of that sentence.
- **Counts.** No sentence in Step 1 counts the items of the occupied list (searched).
- **All checks clean:**
  - `v8_stale`: 156 retired phrases;
  - `v8_caveats`: 187 protected sentences;
  - `v8_nothing_lost`;
  - `v8_assemble`: no unresolved references;
  - `v8_refs`.

**DeepSeek's search-term check — done, and my omission.** The Round 137 absence list did not show a search for *"pitch"*. I had run it
but did not report it. The whole manuscript now reads as follows:
- **Absent:** *"variable pitch", "propeller pitch", "blade pitch", "fixed pitch", "fixed-pitch", "swashplate", "governor", "rpm", "yaw",
  "moment"*.
- ***"pitch"*** occurs once, on p. 19: *"increases the required pitch angle for forward flight"*. That is the aircraft's attitude, not
  rotor pitch.
- ***"torque"*** occurs on p. 6, 16, 21 and 22. Every use is motor specific torque, a sizing quantity, not control.
- **One more thing, recorded but not put in the body.** On p. 14, *"rotor tip speed was lowered to 80% of the hover value"* for loiter,
  cruise and descent.
  - That is a change of **speed**, not of pitch.
  - The sizing tool is NDARC, with rotors described by blade loading. No pitch mechanism is inferred from that (Qwen P1's guard).

The term list, the version flag and the four evidence fields are now in `paper/v8-evidence.md`, with a first table:

| Document | Type/version | In repository | Read by (version) | Verification | Quotation page basis (proposal P-a) |
|---|---|---|---|---|---|
| Vegh manuscript R3 | author's manuscript, revision 3, clean; publication not stated | yes | Claude (R3) | repository PDF | manuscript |
| Vegh SciTech 2025 (10.2514/6.2025-1436) | conference full text | no | ChatGPT (ResearchGate rendering) | single-reader rendering | ResearchGate (1–2 pages off) |
| Vegh correction notice (…1436.c1) | correction only | yes | Claude | repository PDF | — (never cited as the paper) |
| Vegh *J. Aircraft* (10.2514/1.C038393) | journal article | no | nobody (abstract only) | abstract only | — |
| Rohith et al. 2026 | *J. Aircraft* 63(2):575–591, typeset | yes | Claude (typeset) | repository PDF | typeset |

**Also closed:** *"reported in 2016"* (Step 7), which all four of you confirmed.

---

## 2. The *"not …"* classification of the whole body

**Method.**
- I split all fifteen step bodies into sentences. **340** carry a negative.
- **About sixty** of them state that something was not computed, shown, settled, established or measured. I classified each by hand as:
  - **Q**: open quantitative question;
  - **C**: uncomputed comparative analysis;
  - **B**: broader unresolved question;
  - **E**: evidence limitation;
  - **S**: scope boundary.
- For each Q, C or B outside Step 14, I found its home in Step 14's list.
- I read the other 280. Most are claim limits, definitions or physical statements. The few that bear on open work were added.

**The table is Appendix A.**

**Result:**
- Every Q, C and B outside Step 14 has a home in Step 14's list, with one exception: the regime of the control items (S-60 below).
- Three defects and three smaller findings came out.

### 2.1 S-59 — Step 8: *"not airframe-borne"* against the paragraph before it (source)

The two paragraphs as they stand, in full:

> **The frames carry a fairing, and it is not only a drag measure.** The frames are the only surfaces standing perpendicular to the wing
> plane, and a planar planform supplies no directional stability at all, so the fairing is also the only vertical surface the aircraft
> has. Sized against the criterion the tailless literature recommends — C_n_β greater than 0.001 per degree — the chord required over
> the combined frame length is **39 mm**, against the 50 to 70 mm that a 20 mm faired strut carries in any case. Directional stability on
> this configuration therefore does not ask for a surface; it asks for a fairing on a frame that is already there.
>
> **One part is not airframe: the flight control system.** The stability of this configuration is not airframe-borne — it is produced
> by differential thrust and by the strip, both of which are actively commanded — so an attitude reference and a flight computer are
> not optional equipment but part of the mechanism the preceding paragraphs describe. They are carried in the systems budget. The
> configuration replaces a pilot's workload with computation, and the computer is the part that does it.

**The defect.**
- The first paragraph sizes an airframe part for directional stability.
- The second then says the stability *"is not airframe-borne"*. It says so absolutely and for no stated regime.
- Step 1 says it more carefully: *"stability need not come from the airframe **alone**"*.
- The sentence is not protected.

**Repair options:**
- **(a) the minimal repair:**
  > *"The stability of this configuration is not airframe-borne **alone** — **the rest** is produced by differential thrust and by the
  > strip, both of which are actively commanded — so …"*
- **(b) name the regimes:**
  > *"… is not airframe-borne in hover, and in cruise not alone …"*

  This asserts something about hover. At zero airspeed that is plausible, but the inboard wing sits in the nose slipstream, and I have
  not computed whether that gives any damping. So (b) adds a predicate.

**My vote: (a).** It adds no predicate. It matches Step 1, and it no longer contradicts the fairing.

### 2.2 S-60 — the control items carry a regime that Steps 8 and 9 do not (source; state identity applied to the debt trace)

**Outside Step 14, with no regime stated:**
- Step 8: *"What authority each axis actually has depends on the available thrust differential and on allocation as well as on the arm,
  and is not settled by the ratio alone."*
- Step 8: *"What declining it costs is not counted in this work."*
- Step 9: *"This configuration declines the reaction-torque channel that comparable aircraft use for roll (Section 8). What that refusal
  costs — in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia — is not computed anywhere in this
  paper."*
- Step 9: *"Whether eliminating it is favourable on balance is a question this work does not settle, and quantifying it would require a
  control-allocation study rather than a single torque figure."*
- Step 8, in the paragraph of §2.1: the stability is produced by commands that are *"actively commanded"*. That holds in cruise as well.

**In Step 14 and Supplement S14, hover only:**
- **Step 14 list item:**
  > *"- closed-loop hover control, including the declined reaction-torque channel, the hover torque residual and the allocation of the
  > tip pairs between take-off margin and attitude authority;"*
- **S14 row:**
  > | **Closed-loop hover control**, including the cost of declining the reaction-torque channel, the absorption of the hover torque
  > residual left by trimming each pair's torque balance at cruise (Section 8), and the allocation of the tip pairs between take-off margin
  > and attitude authority, which compete for the same propellers. | Whether hover is controllable with the authority computed (Sections 5
  > and 8) | **Analysis not yet done**: a control-allocation study, then simulation |

**Why this is a gap:**
- The declined channel acts about the body roll axis. In hover that is a change of heading; in cruise it is bank. S14's own strip row says
  so.
- Its cost is therefore not a hover question alone. Step 1 says the 2012 source assigns the channel *"to yaw in the vertical mode and to
  roll in the horizontal one"*.
- Closed-loop attitude control in cruise appears in no list. I searched the body and the supplement for *"closed-loop"*, *"closed loop"*,
  *"control allocation"* and *"hover control"*. Only the hover item exists.

**Proposed repair (R), keeping the list at eighteen items:**
- **Step 14 item:**
  > *"- closed-loop attitude control **in hover and in cruise**, including the declined reaction-torque channel, the hover torque residual
  > and the allocation of the tip pairs between take-off margin and attitude authority;"*
- **S14 row:**
  > | **Closed-loop attitude control, in hover and in cruise**, including the cost of declining the reaction-torque channel, which would act
  > about the body roll axis in both regimes (Section 8), the absorption of the hover torque residual left by trimming each pair's torque
  > balance at cruise (Section 8), and the allocation of the tip pairs between take-off margin and attitude authority, which compete for
  > the same propellers. | Whether the aircraft is controllable with the authority computed, in hover and in cruise (Sections 5 and 8) |
  > **Analysis not yet done**: a control-allocation study, then simulation |

**What else I checked:**
- *"None of these is a small correction to a known quantity"* and *"Two of them need validated data"* still hold.
- No sentence states the number eighteen.
- **Step 11's list** says *"closed-loop hover control"*. It is true as written, and it does not claim to be complete. **My vote: leave it.**
- **Step 5's** hover sentence (*"… and Section 14 carries it"*) is still carried.
- **Step 15's** *"what declining it costs is not computed"* has no regime and is consistent with the widened item.

**My vote: yes to both.**

### 2.3 R-9 — my second misreading in the S14 *"Other store types"* row (written in Round 124; the first misreading, found by DeepSeek, was repaired in Round 125; all of us confirmed the row in Round 126)

**The row as it stands:**

> | **Other store types.** A supercapacitor store, or a battery–supercapacitor combination, is tabulated in one survey at the specific power
> the buffer asks for — 500 to 10 000 and 10 000 to 100 000 W/kg, at 1 to 10 Wh/kg (Rheaume and Lents 2016, Table 1, cited from its
> references [8] and [14]). The survey's own qualification on this class: *"Supercapacitors exhibit low specific energy but outstanding
> specific power at high cost suggesting that this technology is more appropriate in a hybrid energy storage approach (e.g.
> supercapacitors and batteries)."* | Whether a store other than a battery closes the buffer at the required power and holds the vertical
> phases' energy | **Analysis** against a defined mission profile; not computed here |

**The source** (Table 1, transcribed in Round 122 Appendix C; I re-read the qualification sentence in the PDF this round, p. 2):

| Technology | Specific Energy (Wh/kg) | Specific Power (W/kg) |
|---|---|---|
| Super-Capacitor | 1-10 [14] | 500-10k [8], 10k-100k [14] |

**What is wrong:**
- There is **one** Super-Capacitor row. Its two ranges come from two different cited sources.
- There is **no battery–supercapacitor row**. The combination appears only in the qualification sentence.
- So *"or a battery–supercapacitor combination, is tabulated"* is false. The two ranges also read as if there were one per store type.

**Proposed repair (R):**

> | **Other store types.** A supercapacitor store is tabulated in one survey at specific powers that reach what the buffer asks for — 500 to
> 10 000 W/kg from one cited source and 10 000 to 100 000 W/kg from another — at 1 to 10 Wh/kg (Rheaume and Lents 2016, Table 1, citing
> its references [8] and [14]). The table has no battery–supercapacitor row; the combination enters only through the survey's own
> qualification on this class: *"Supercapacitors exhibit low specific energy but outstanding specific power at high cost suggesting that
> this technology is more appropriate in a hybrid energy storage approach (e.g. supercapacitors and batteries)."* | Whether a store other
> than a battery, alone or combined with one, closes the buffer at the required power and holds the vertical phases' energy |
> **Analysis** against a defined mission profile; not computed here |

**My vote: yes.**

### 2.4 Three smaller findings

**N2. The strip's slipstream split.** Step 8 says: *"The split is an estimate: the slipstream boundary it rests on is not derived in this
work."*
- The S14 strip row does not name it.
- The derivation is already scheduled before submission (S-37). If it succeeds, the sentence changes. If it fails, the item enters S14.
- **My vote:** no action now, and recorded.

**N3. S14 has nineteen rows; Step 14's list has eighteen.**
- The extra row is *"Other store types"*. It went to the supplement only, by the Round 127 vote.
- Step 14 introduces its list as: *"The remaining items are not known obstacles; they are questions this work has not answered, and each
  is listed with what would settle it in Supplement S14. They are:"*
- Under the scope that sentence states, *"other store types"* is such a question. Qwen's list-completeness check therefore flags it.
- **Options:**
  - **(a)** Add *"other store types"* to the body list (nineteen items; no body sentence states the count).
  - **(b)** Mark the S14 row as belonging to the **known obstacle** (the store), not to the unknowns. The body is unchanged: the store
    section's *"does not exist with any store the sources consulted here report as built"* is where the question sits. Rheaume and Lents
    give survey metrics, not a built store, as you all judged in Round 127.
  - **(c)** Leave it.
- **My vote: (b).** Whether another store type closes the buffer is the known obstacle's own open end.

**N4. The ground-wind price.** Step 6 says *"the wing's exposure to ground wind is not priced in this work"*.
- By topic it sits under Step 14's *"ground handling and landing loads"*.
- The S14 row names the stance base (*"a parameter against static crosswind"*) but not the price.
- **My vote:** add one clause to the S14 row's first cell: *"… (Section 5), and its price at a stronger ground-wind requirement is not
  computed (Section 6);"*.

### 2.5 One classification question — Step 12's Bill 1

The sentences:
- *"Scale does not lock two of the charges together; the third is not tested"* (heading);
- *"Bill 1 is not tested, and nothing here should be read as showing that it separates from the other two — or as showing that it does
  not."*;
- *"Whether the two are separable here is not established"*.

**I classify them E** (evidence limitation), not as a Step 14 item:
- On this configuration Bill 1 appears as the buffer, which is an **input**.
- Step 12 says the one available derivation would not test it.
- The question is the framework's, not the aircraft's.
- What would settle it is a store derived rather than assumed, and that is the known obstacle.

Step 14 says *"What this section reaches is the aircraft"*. **Do you agree it is E, or should it be a Step 14 item?**

---

## 3. Your proposals from Round 137, merged for the vote

| # | Proposal | From | My vote |
|---|---|---|---|
| P-a | **Fifth evidence field: quotation page basis** — which version's page numbers a quotation uses (manuscript / typeset / rendering) | DeepSeek | yes |
| P-b | **Manuscript rule.** When a document is read as a manuscript, its quotations and pages are recorded as manuscript-version. The citation is flagged, and before submission it is reconciled against the typeset version if one is obtained. | DeepSeek P2 + Qwen P2 | yes |
| P-c | **Source-layer check, in the record-propagation sweep (H).** Every sentence drawn from a witness is one of four layers: source fact / source absence / classification (elements (a)–(f)) / manuscript claim. Source-absence clauses (*"the paper does not state"*) carry their search-term list in the evidence record, and no compression may turn one into a claim about the vehicle. | ChatGPT + Qwen P1 + DeepSeek P4 | yes |

**Accepted in Round 137 (unanimous):** date identity in the provenance sweep; the *"not …"* classification before the figure scripts;
p. 4's *"reduced mechanical complexity"* as record only.

---

## 4. What comes next in this stage

1. Your votes on §2.
2. **Number identity** (value, unit, object, model, state, date).
3. The figure scripts and the *"biplane"* heading check.
4. **H:** the record-propagation sweep, with P-c if adopted.
5. **I:** the Step 1 and Step 8 denial maps.
6. The whole reading in two halves (1–8, 9–15), then a short reconciliation.

---

## 5. Errors this round

- **Mine:**
  1. **R-9.** I wrote a combination into the supplement that the source does not tabulate. It is the second misreading in the same row:
     DeepSeek caught the first in Round 125, and all of us then confirmed the row in Round 126 without seeing this one. The
     whole-supplement search of this round found it.
  2. **I did not report the *"pitch"* search** in Round 137. DeepSeek asked for it. It was run, and it is now reported.
- **S-59 and S-60** are source defects. Both are in text all of us have read several times.
- **Qwen:** *"The manuscript corresponds to the SciTech 2025 conference paper"* and *"'2025' is accurate for the work's date"*.
  - The file states neither.
  - The match is by title, which is why the version is fixed before submission.
  - This is a small overstatement, and the kind P-b is meant to prevent.
- **Others:** none found. Please look at mine.

---

## 6. To vote

| # | Item | My vote |
|---|---|---|
| a | §1: Proposal V as applied | confirmed |
| b | §2.1 S-59: (a) or (b) | (a) |
| c | §2.2 S-60: Step 14 item and S14 row; Step 11 left as is | yes; yes; leave |
| d | §2.3 R-9: the corrected S14 row | yes |
| e | §2.4: N2 no action; N3 (a)/(b)/(c); N4 the S14 clause | yes; (b); yes |
| f | §2.5: Step 12's Bill 1 is E | yes |
| g | §3: P-a, P-b, P-c | yes; yes; yes |
| h | Appendix A: any classification you would change | — |

---

## 7. Your own proposals

As always, give anything you see, with your reason. If another reader's view is divided from yours, answer it by name.

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## Appendix A — the classification (Sections 1–13, then Step 14's own negatives)

Classes: **Q** open quantitative question · **C** uncomputed comparative analysis · **B** broader unresolved question · **E** evidence
limitation · **S** scope boundary. *"Home"* is the Step 14 list item.

| § | Sentence (key clause) | Class | Home in Step 14 | Note |
|---|---|---|---|---|
| 1 | *"What is not established is the combination taken together with its price."* | E (search-bounded absence) | — | Section 1's occupied list |
| 1 | *"The route is not claimed to have been waiting to be found."* | S | — | |
| 2 | *"Whether any architecture avoids the mismatch … is not settled here."* | S (pointer to Section 3) | — | |
| 3 | *"Rotating the airframe is permitted and is not priced here."* | S (definition scope) | pricing: the pitching moment through the transition | |
| 3 | *"… are not charged as duty-cycle mismatch under this accounting."* | S | — | |
| 3 | *"Whether such an architecture might avoid the three charges by some other route is a separate question this paper does not settle"* | S (reach of a definition) | — | *"a definition, not a law"* |
| 4 | *"It does not establish that the accounting is complete …"*; *"None is known to the authors."* | E | — | |
| 5 | *"Not demonstrated. The aircraft leaves the ground on its control propellers."* | B | closed-loop hover control (allocation) | |
| 5 | *"The vertical descent has not been analysed."*; *"an open question in Section 14"* | B | vertical descent and the landing transition | |
| 5 | *"no figure in this paper describes the landing transition"* | B | same | |
| 5 | *"Hover attitude control is sized but not demonstrated as a closed loop."* | B | closed-loop hover control | |
| 5 | *"What that refusal costs in authority and in response time is not computed, and Section 14 carries it."* | C | closed-loop hover control | hover context: state matches |
| 6 | blade family *"a design variable this study has not fixed"*; *"none of those is modelled"*; *"Whether 0.683 is the blade … is not settled here"* | Q | blade-family selection | |
| 6 | *"Whether a variable-pitch hub would recover that difference is not computed"* | C | the variable-pitch counterfactual | |
| 6 | *"The direction of that mismatch is not claimed here, because it has not been computed"* (atmosphere) | C | atmosphere | |
| 6 | *"not a controlled numerical reproduction … validation"*; *"No part of this has been measured."* | E | — | |
| 6 | *"the wing's exposure to ground wind is not priced in this work"* | Q | ground handling and landing loads | N4 |
| 7 | *"The means of stopping is not fixed by this study"* | Q | the tip pairs' stopped cruise state | |
| 7 | variable-pitch price *"not settled here"* | C | the variable-pitch counterfactual | |
| 7 | *"Part count, mass, failure modes and maintenance burden were not measured"* | S (no reliability claim) | — | |
| 7 | *"Whether this aircraft can actually perform the change … is not settled anywhere in this paper"* | B | the pitching moment through the transition | |
| 8 | *"What authority each axis actually has … is not settled by the ratio alone."* | B | closed-loop **hover** control | S-60 |
| 8 | transition assignment *"not settled in this paper"* | B | the pitching moment through the transition | |
| 8 | shafting: *"an implementation question it does not settle"* | S | — | |
| 8 | *"What declining it costs is not counted in this work."* | C | closed-loop **hover** control | S-60 |
| 8 | *"The split is an estimate: the slipstream boundary it rests on is not derived in this work."* | Q | the strip and the fairing | N2 |
| 8 | *"How many actuators that is, this study does not fix."* | Q | the strip and the fairing (actuation) | |
| 8 | torque residual absorbed *"which this study has not shown"* | Q | closed-loop hover control (residual) | |
| 8 | shaft power of commanded departures *"is not computed"* | Q | shaft power off the free-wheeling state | |
| 8 | *"Neither the means nor the azimuth is fixed by this study"* | Q | the tip pairs' stopped cruise state | |
| 8 | *"The stability of this configuration is not airframe-borne …"* | (physical statement) | — | S-59 |
| 9 | *"It is not a list of the study's open questions."* and the eight non-claims | S | — | |
| 9 | refusal cost *"is not computed anywhere in this paper"* | C | closed-loop **hover** control | S-60 |
| 9 | *"Whether eliminating it is favourable on balance is a question this work does not settle"* | B | closed-loop **hover** control | S-60 |
| 9 | *"The separate claim that this aircraft can actually perform the regime change is not settled"* | B | the pitching moment through the transition | |
| 9 | *"No aircraft has been built, no wind tunnel has been run on this geometry"* | E | — | |
| 10 | *"The blade family is a design variable this study has not fixed"* | Q | blade-family selection | |
| 10 | *"Whether a real aircraft loses 5.4 m, more, or less is not settled by anything here."* | B | the pitching moment through the transition | |
| 10 | *"It does not establish that the package exists."* | E | the known obstacle (store) | |
| 10 | *"no rotorcraft is sized in this work, so no range comparison is made against one"* | S | — | |
| 11 | *"No stopped-state counterfactual was computed."* | C | the tip pairs' stopped cruise state | |
| 11 | *"No variable-pitch counterfactual was computed"* | C | the variable-pitch counterfactual | |
| 11 | *"Rotor–structure and rotor–wing interference is not modelled"* | Q | interference | |
| 11 | the *"What the closure does not contain"* list | Q/B/C | each item in Step 14 (receipt audit) | "closed-loop hover control": S-60 |
| 11 | *"The buffer fraction is an input to the loop, not a result of it."* | E | the known obstacle | |
| 12 | *"the third is not tested"*; *"Bill 1 is not tested"*; *"Whether the two are separable here is not established"* | E | — | §2.5 |
| 12 | *"It cannot show that they are independent in general"*; *"not a verification of separability as a general …"* | S / E | — | |
| 12 | *"no closure was run at 1 000 kg"* | S | — | |
| 13 | competitor propeller efficiency *"assumed, not computed"*; lift group and tilt mechanism: *"Neither figure is measured."* | Q | the competitor's cruise propeller efficiency; lift-group mass | |
| 13 | indexing mechanism *"whose mass is not separately charged"* | Q | the competitor's lift-group mass | inside the assumed fraction |
| 13 | *"Where the reversal falls is decided by quantities this study has not measured or not fixed"* | Q | blade family; lift-group mass; propeller basis | |
| 13 | *"this paper has no mission that would decide, and does not choose"*; *"an ordering against a bound is not a result"* | S | — | |
| 14 | *"how long each draws the peak is not computed here"* | Q | the buffer's energy | |
| 14 | *"whether the airframe fraction holds at twice the mass it was set at is not established"* | Q | the airframe's mass | |
| 14 | *"how they would move with a measured store is not computed"* (Section 13's orderings) | C | in the known-obstacle part, with no settlement line of its own | my view: the settlement is the re-closure already described |
| 14 | *"The package Section 10 closes on does not exist with any store the sources consulted here report as built."* | E | — | R-9, N3 |
| 15 | five negatives | — | consumed | `paper/v8/drafts/15-maps.md` |
