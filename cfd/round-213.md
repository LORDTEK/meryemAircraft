# Round 213 — P22 repaired; S14 drafted, which completes the journal supplement

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text, including Section 7 in full and the other sentences that point into S14.

---

## A. Closed in Round 212 (all four, and me)

- **B1, P22:** the added sentence is applied. Grok, ChatGPT and Qwen voted for it; DeepSeek found it *"acceptable"* and does not veto it. The result is in §B.
- **B2, the rotation-time subsection of S12: kept with its figures.** ChatGPT and Qwen moved to this position, so it does not go to the author.
- **S13: P26 to P30 are R1.** The three flagged changes are accepted.
- **Qwen (Round 211, acknowledged by Qwen):** proposed removing a protected row the author had placed in S12. Recorded in §E.

---

## B. P22 applied: please confirm

**Section 6.2, before:**

> **But the full hover power passes through the electrical path, and that path is sized by it.** **Bill 3 is removed from the engine and left standing on the electrical system** (the propulsion-mass split is in Supplement S11).

**After** (the protected sentence is unchanged; one sentence is added):

> **But the full hover power passes through the electrical path, and that path is sized by it.** **Bill 3 is removed from the engine and left standing on the electrical system** (the propulsion-mass split is in Supplement S11). The sizing loop computes no hover-rated mass for the electrical path.

**Checks run after the change:**
- protected sentences: all 145 in place;
- retired phrases: none;
- section references: all resolve;
- no sentence lost;
- the submission PDF rebuilt.

**P22 against the repaired text: please grade it** (expected R1).

---

## C. S14, drafted: the last section of the journal supplement

S14 serves seven pointers:
- P08 and P10, in Section 3;
- P23, in Section 6.2;
- P31 to P33, in Section 7;
- P34, in Section 8.

It carries two protected rows. In one of them *"Section 10"* becomes *"Section 6.1"*; that is renumbering only.

**Checked against code and source this round:**
- `aero/buffer.py` reran with output identical to the stored result: every demand ratio and every re-closure figure.
- The measured-store paragraph against the source PDF [25]:
  - the 13.5 kg unit pack and the 10.68C (235 A) rate;
  - Table 7, which gives 16.26 Ah and 1 394 Wh;
  - from these, 249 s, and 1.49 kW per kilogram averaged over that time;
  - 55.1 °C, against the authors' 60 °C limit.

**Flagged changes:**
- **The archive's *"+6 to +8 %"* is now *"+6.5 to +8.2 %"*.** 6.5 does not round to 6.
- **The electrical-path row no longer says the path *"enters the loop as a mass fraction"*.** It now says the loop computes no mass for it sized to that peak. That is the S-67 and Q-210 finding, applied here.
- **The strip-and-fairing row adds the fairing's two limits:** an assumed lateral lift-curve slope, and side force only (S-66; Supplement S8).
- **Section references are renumbered from step numbers to section numbers.** Where the archive's pointer no longer matched the body, the row follows the body:
  - the ground-wind clause now quotes Section 4's *"not priced"*;
  - the variable-pitch row now points to Sections 4 and 6.2.
- **Not rerun this round, carried from the archive table as accepted in Rounds 135 to 140:**
  - the transition incidence, 18 to 22 degrees;
  - the shell areal density, 1.78 against 1.50 kg m⁻².

  Say if you want either rerun before submission.

**What you are asked to check:**
- grade P08, P10, P23, P31, P32, P33 and P34;
- apply ChatGPT's rule (no new claim the body does not make or promise);
- judge the flagged changes;
- for P23: does every item in Section 6.2's *"What the closure does not contain"* list appear in the table?

**What comes after this round.** With S14, every one of the 34 pointers has a passage. The remaining steps are mechanical, plus one checkpoint:
1. renumber S2–S14 to S1–S11 in a supplement generator;
2. a receipt table for all 34 pointers;
3. one final whole-body check against the completed supplement. At that check the reader packet is sent again, in parts where needed.

### The sentences that point into S14

**Section 3 (P08, P10):**

> **The vertical descent and the landing transition have not been analysed.** Whether the descent enters the vortex ring state is an open question in Supplement S14; the landing transition is not the take-off transition run backwards, and no figure in this paper describes it (Supplement S5).
>
> **Hover attitude control is sized but not demonstrated as a closed loop**: the moments about each axis are computed, and no control allocation has been closed around them. This configuration also declines the reaction-torque channel that comparable aircraft use about the body's longitudinal axis (Section 5.2). **What that refusal costs in authority and in response time is not computed**, and Supplement S14 carries it.

**Section 6.2 (P23):**

> Section 6.1's convergence does not cover the cost of declining the reaction-torque channel, the sizing of the strip's actuation, the allocation of the take-off margin against attitude authority, the landing transition, the vortex ring state, closed-loop attitude control in hover and in cruise, engine installation, or rotor–structure and rotor–wing interference; **none of these is a ledger entry, and Supplement S14 lists them.** **The first and the last are the two that would most change the numbers above if they were computed.**

**Section 8 (P34):**

> Section 7 and Supplement S14 list what the paper leaves open. What the paper offers is **a configuration sized to combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism that reorients a propulsor, and an account of what the combination costs.**

**Section 7, in full:**

#### 7. What does not close

Section 6.1 closed the sizing loop on a declared package and said that whether an aircraft can be built to it is a different question. **This section is where that question is answered, and for the first item the answer is no: the required store performance is not demonstrated by the sources consulted here.** It is stated in that order — first the obstacle that is known, then what is not known.

#### First, the known obstacle: the energy store

**Every closure in Section 6.1 carries a buffer of 3.6 percent of take-off mass.** Taken at the
electrical bus, **the four closures ask the buffer for 4.7 to 5.2 kW per kilogram of buffer to hover, and 5.5 to 6.1 kW per kilogram of
buffer to leave the ground** with the tip pairs at full thrust (Section 3).

**What has been measured is a fraction of that, and the store figures available are of four different kinds.** A pack flown in a 210 kg-class electric VTOL aircraft is rated, as a flown system, at 0.892 kW per kilogram continuous; its
unit pack, discharged on the bench at its highest tested rate, delivered on average about 1.5 kW per kilogram (Supplement S14). A
NASA-funded design study adopts 4 kW per kilogram and describes that figure as about twice that of existing batteries. The same study
notes lithium-polymer figures in the literature as high as 3 kW per kilogram, which it cites rather than measures; against that figure
the take-off demand is 1.8 to 2.0 times. The study argues that, because pulse current limits can exceed continuous ones — by more than a
factor of two in one commercial module it cites — a pack with the required specific power may be possible with existing technology; its
hover lasts twenty seconds or less, while this aircraft's vertical phases occupy about a minute in all (Section 2.1), and how long each
draws the peak is not computed here.

**The take-off demand is 3.7 to 4.1 times the bench rate — the highest figure obtained from a measurement — and 6.2 to 6.8 times the
flown system's continuous rating.** The comparison is between unlike ratings. **The gap is real on every one of them;
the factor quoted is peak demand against bench average.** The package Section 6.1 closes on does not exist with any store the sources
consulted here report as built; closed again at the bench rate, it becomes 76 to 81 percent heavier, a sensitivity with one input
changed rather than a structural closure (Supplement S14).

**This is where the coupling Section 2.2 names is paid**: the buffer converts kilowatts of hover peak into kilograms of store. **The
escape from Bill 3 is real in the sense Section 2.2 defined it, and its price depends on a component whose required performance has not
been demonstrated.**

#### What the obstacle reaches, and what it does not

**It reaches every number that describes this aircraft at Section 6.1's masses**: the closed masses of 52.3 to 57.5 kg and the 13 kg payload assume the store. The ranges of 927 to 1 233 km survive the re-closure only because the fuel fraction is held, on an aircraft three-quarters heavier; they do not survive as 13 kg carried that far on a store that has been built. The vertical phase that Section 3 reports as sized was sized with this store in it, and Section 6.4's orderings were computed with the store held common at 3.6 percent; how they would move with a measured store is not computed.

**It does not reach the mechanism claim.** That is a statement about hardware, and a heavier store adds no pivot. **Nor does it reach the cruise-efficiency comparison of Section 4 as a ratio**: effective lift-to-drag ratio has no mass in it. As a comparison of aircraft, that section describes the configuration at Section 6.1's masses, which the store does reach.

#### Then what is not known

Eighteen further questions are open, and Supplement S14 lists each with what it bears on and what would settle it.

**None of these is a small correction to a known quantity.** Two of them need validated data rather than more of the computation already done: the transition moment, because three methods have been tried against it and disagree, and the low-Reynolds section drag, because the one method used here is least reliable exactly there.

#### What this section amounts to

**The loop closes; the aircraft is not shown to.** At the energy store the paper can name the gap exactly, in specific power and in take-off mass; everywhere else it can name only what would settle the question. **The architecture claim — that the configuration is arranged to change regime with no mechanism that reorients a propulsor — is a count of hardware, and nothing in this section reaches it.** What this section reaches is the aircraft, and the paper has not claimed the aircraft. The last section returns to the four axes and states what is claimed on each.


### The draft

### S14. What does not close: working for Sections 3, 6.2 and 7

#### The measured store figures

> *Provenance and changes:* for P31 (Section 7): "… its unit pack, discharged on the bench at its highest tested rate, delivered on average about 1.5 kW per kilogram (Supplement S14)". src: archive S14, "Section 14 as it stood before recomposition into result sentences", store paragraph. Checked this round against references/Yu-2025_24S-NCM-battery-eVTOL-IN-FLIGHT_Batteries.pdf [25]: 24S1P unit pack 13.5 kg; 10.68C (235 A), the maximum discharge condition considered; Table 7: 16.26 Ah, 1394.3 Wh at 10.68C -> 16.26/235 h = 249 s, 1394.3 Wh / 249 s / 13.5 kg = 1.49 kW/kg (aero/buffer.py uses 1.49); 55.1 deg C, 4.9 deg C margin to the authors' 60 deg C; 724 W/kg (110 A) unit pack and 892 W/kg (440 A) 24S4P system; VS-210, 210 kg-class MTOW. Demand ratios from aero/buffer.py, rerun this round (identical): hover 4.68-5.23, take-off 5.53-6.09 kW/kg; /1.49 -> 3.1-3.5 and 3.7-4.1.

The flown system is a 24-series nickel–cobalt–manganese pack designed, bench-tested and flown in a 210 kg-class electric VTOL aircraft [25]. As a flown system (24S4P) it is rated at 0.892 kW per kilogram continuous; its 13.5 kg unit pack (24S1P) is rated at 0.724 kW per kilogram continuous. Discharged on the bench at its highest tested rate, 10.68C (235 A), the unit pack delivered 1 394 Wh in about 249 s, on average about 1.5 kW per kilogram for about four minutes, and reached 55.1 °C against the 60 °C limit its authors adopted. Against that bench average the take-off demand of the four closures, 5.5 to 6.1 kW per kilogram of buffer, is 3.7 to 4.1 times, and hover alone, 4.7 to 5.2 kW per kilogram, is 3.1 to 3.5 times.

#### The loop closed again on a measured store

> *Provenance and changes:* for P32 (Section 7): "… closed again at the bench rate, it becomes 76 to 81 percent heavier, a sensitivity with one input changed rather than a structural closure (Supplement S14)". src: same archive snapshot, re-closure paragraph and table. Protected S14 rows carried (E12): "These masses are the Section 10 package with one input changed." (Section 10 -> Section 6.1, renumbering only) and "They are not a structural closure at 100 kg". Figures from aero/buffer.py, rerun this round (identical to aero/buffer-result.txt): 4.0 kW/kg 56.6-61.2 kg, 5.0-5.5 %, +6.5 to +8.2 %; 1.49 kW/kg 94.6-101.2 kg, 13.4-14.7 %, +75.9 to +80.8 %; 0.892 kW/kg 333.5-335.2 kg, 22.3-24.6 %; 0.724 kW/kg does not close; payload at the closures' masses with the bench rate 7.2-7.4 kg. CHANGED: the archive's "+6 to +8 %" is now +6.5 to +8.2 % (6.5 does not round to 6).

Closing the loop on a measured store is a sensitivity of the package, not a second aircraft. The buffer is derived inside the loop from the take-off demand at a given specific power; everything else is Section 6.1's: the same fractions, including an airframe at thirty percent of take-off mass, and the same wing loading, disc loading and aspect ratio, so the lift-to-drag ratio is carried unchanged and, with the fuel fraction held, so is the range. These masses are the Section 6.1 package with one input changed. They are not a structural closure at 100 kg, and whether the airframe fraction holds at twice the mass it was set at is not established.

| Buffer specific power, per kilogram of buffer | Take-off mass | Buffer | Change from Section 6.1 |
|---|---:|---:|---:|
| As Section 6.1 implies: 5.5 to 6.1 kW kg⁻¹ | 52.3 to 57.5 kg | 3.6 % | — |
| 4 kW kg⁻¹, the design-study assumption [26] | 56.6 to 61.2 kg | 5.0 to 5.5 % | +6.5 to +8.2 % |
| About 1.5 kW kg⁻¹, the unit pack's bench rate | 94.6 to 101.2 kg | 13.4 to 14.7 % | +76 to +81 % |
| 0.892 kW kg⁻¹, the flown system's continuous rating | about 335 kg | 22 to 25 % | set by nearness to non-closure |
| 0.724 kW kg⁻¹, the unit pack's continuous rating | does not close | — | — |

If Section 6.1's take-off masses are kept instead of re-closing at the bench rate, the payload falls to about 7 kg rather than 13. At the flown system's continuous rating the loop only just closes, and the mass it returns is set by how near the loop is to not closing rather than by anything about the aircraft.

#### The open questions

> *Provenance and changes:* for P08 (Section 3, the vortex ring state), P10 (Section 3, the cost of declining the reaction-torque channel), P23 (Section 6.2, what the closure does not contain), P33 (Section 7, "Eighteen further questions are open, and Supplement S14 lists each with what it bears on and what would settle it") and P34 (Section 8, "Section 7 and Supplement S14 list what the paper leaves open"). src: archive S14 table (L4439-L4459). Section references renumbered from step to section numbers (5->3, 6->4, 7->5.1, 8->5.2, 10->6.1, 11->6.2, 12->6.3, 13->6.4, 14->7). Brought up to the current body: the electrical-path row no longer says the path "enters the loop as a mass fraction" (the S-67 / Q-210 finding; it now says the loop computes no mass for it sized to that peak); the strip-and-fairing row adds the fairing's assumed slope and side-force-only limit (S-66, Supplement S8); the descent row points to Supplement S5; the store-types row names its source [23]. Eighteen rows are open questions; the store-types row is marked as part of the known obstacle and is not counted. Not rerun this round: the transition incidence (18-22 deg) and the shell areal density (1.78 against 1.50 kg/m2), carried from the archive table as accepted in Rounds 135-140. Quotation [23] and page [3] p. 320 as verified in earlier rounds (references-draft notes).

Section 7 lists eighteen questions this work has not answered. Each is given here with what it bears on and what would settle it; one further row, on store types, belongs to the known obstacle and is not one of the eighteen.

| Item | Bears on | What would settle it |
|---|---|---|
| **The pitching moment through the transition.** Three methods of three fidelities diverge above about ten degrees of incidence; the rotation passes through that band, peaking near 18 to 22 degrees on the 50 kg reference geometry, with the inboard half of the wing in the slipstream at a much lower effective incidence. | Whether the aircraft trims through the rotation (Sections 5.1 and 6.1) | Validated aerodynamic data: a measurement of the outboard wing's pitching moment to about 22 degrees at low dynamic pressure and of trim at the attached-flow end of the rotation, or a higher-fidelity method validated against one |
| **Section drag at low Reynolds number.** The tip-pair rotors' free-wheeling charge rests on section polars below a Reynolds number of 10⁵, and the uncertainty runs both ways. | The rotor term in every closure, 0.0154, carried as 0.0169 at the adverse end with the build-up's ten percent margin (Sections 6.1 and 6.2); the size of Bill 2's fall with scale (Section 6.3); and the tip-rotor blade itself, which the hover requirement selects on the same polars (Supplement S12) | Validated data: the drag of a free-wheeling tip rotor, or of its sections, at about 8 × 10⁴, or a method validated there |
| **The tip pairs' other cruise state.** Free-wheeling is determinate and computed; stopped is a family of states whose means and azimuth are not fixed (Section 5.2; Supplement S11). | Whether a lower-drag cruise state is available, and at what mechanism cost | Analysis, or a measurement of one stopped state |
| **The tip pairs' shaft power off the free-wheeling state in cruise.** Attitude moments in cruise are commanded departures from the zero-shaft-torque state, and the shaft power they take is not computed (Section 5.2). | Cruise energy | Analysis of cruise attitude demand and of the tip pairs' shaft power off the zero-torque state |
| **The buffer's energy, not only its power.** The store is sized here by power. Whether it also holds the energy for the vertical phases and their reserves, and how it is recharged in cruise, depends on a hover duration this work does not fix; at the bench rate the unit pack emptied in about four minutes. | Whether the store sized by power is also large enough | Analysis against a defined mission profile |
| *Other store types (part of the known obstacle; not one of the eighteen).* A supercapacitor store is tabulated in one survey at specific-power ranges that include values at the level the buffer requires, 500 to 10 000 W/kg from one cited source and 10 000 to 100 000 W/kg from another, at 1 to 10 Wh/kg [23]. The table has no battery–supercapacitor row; the combination enters only through the survey's own qualification on this class: *"Supercapacitors exhibit low specific energy but outstanding specific power at high cost suggesting that this technology is more appropriate in a hybrid energy storage approach (e.g. supercapacitors and batteries)."* | Whether a store other than a battery, alone or combined with one, closes the buffer at the required power and holds the vertical phases' energy | Analysis against a defined mission profile; not computed here |
| **The electrical path at peak.** Machines, power electronics, wiring and their cooling carry the full take-off demand; the loop computes no mass for them sized to that peak and its heat (Section 6.2; Supplement S11). | Whether the path that delivers the buffer's power exists at the mass assumed | Component sizing and thermal analysis |
| **The airframe's mass.** It enters the loop as a construction constant, thirty percent of take-off mass (Supplement S11). A component build-up at the reference mass leaves room for the 13 kg payload only if the average shell areal density stays at or below 1.78 kg m⁻², against 1.50 assumed; the build-up carries a contingency rather than a structural sizing, and it has not been re-run at Section 6.1's closed masses, still less at the masses the store re-closure returns. At the 1 000 kg reference design the shell-mass exponent is not measured at all. | Every closed mass | Structural sizing (analysis), then a built article (measurement) |
| **The strip and the fairing.** The strip's effect on this planform is computed, not measured, and its actuation is carried in the systems budget without being sized (Section 5.2). The fairing is sized against a published stability criterion at an assumed lateral lift-curve slope, counts the frames' side force only, and the side force it develops is not measured (Supplement S8). | The strip: the body roll axis, which appears as bank in cruise and as a change of heading in hover (Section 5.2). The fairing: directional stability in cruise | Measurement of both surfaces; sizing of the actuation |
| **Closed-loop attitude control, in hover and in cruise**, including the cost of declining the reaction-torque channel, which would act about the body roll axis in both regimes (Section 5.2), the absorption of the hover torque residual left by trimming each pair's torque balance at cruise (Section 5.2), and the allocation of the tip pairs between take-off margin and attitude authority, which compete for the same propellers. | Whether the aircraft is controllable with the authority computed, in hover and in cruise (Sections 3 and 5.2) | Analysis not yet done: a control-allocation study, then simulation |
| **Vertical descent and the landing transition.** Neither is analysed; the vortex ring state is not assessed, and the landing transition is not the take-off transition run backwards (Supplement S5). | Whether the aircraft can come down as it went up (Section 3) | Analysis not yet done |
| **Ground handling and landing loads.** The stance base is a parameter against static crosswind (Section 3), and the wing's exposure to ground wind is not priced (Section 4); the response to a landing with lateral velocity or on uneven ground, and handling between flights, are not assessed. | Operation from unprepared sites | Analysis not yet done |
| **The competitor's lift-group mass.** It is one of the two assumed quantities that decide the sign of the fixed-take-off-mass ordering in Section 6.4; the other is the competitor's cruise propeller efficiency. | Section 6.4's sensitivity, not a claim | Measured inventories of lift-plus-cruise aircraft of this class |
| **The competitor's cruise propeller efficiency.** Assumed at 0.80, not computed; with all three architectures at this configuration's propeller efficiency, this configuration leads under a fixed take-off mass at every closure (Supplement S13). | Section 6.4's sensitivity, not a claim | Computation of that propeller at its operating point |
| **Rotor–structure and rotor–wing interference, in cruise and in hover.** In cruise it is inside Bill 2 in principle, absent from the build-up and not modelled (Section 6.2); the drag bracket's upper margin is the only provision made for it. In hover the nose pair's slipstream runs over the inboard wing and the strip (Section 5.2), and any force or moment it produces there beyond the strip's commanded action is not computed. On a quadrotor tail-sitter reported in 2013 the slipstream acting on a wing under the propellers made control about the thrust axis difficult, and the wing was moved out of it ([3], p. 320); that aircraft used single rotors, and whether a contra-rotating pair changes the effect is not computed. | Bill 2, and so every closure; in hover, the control about the body roll axis and the hover torque balance (Sections 3 and 5.2) | Analysis not yet done |
| **Engine installation**: bay, intake, exhaust, cooling. | Mass, drag and packaging | Absent from this work entirely |
| **Blade-family selection.** The criteria that would choose among the blade families (structural loads, acoustics, the motor operating point, rotor inertia, manufacture) are not modelled (Section 4; Supplement S6). | Which point of the envelope the aircraft occupies | Analysis not yet done |
| **The variable-pitch counterfactual.** Whether a variable-pitch hub would recover the fixed-pitch cruise-efficiency gap is not computed (Sections 4 and 6.2). | The cruise-efficiency gap (Section 6.2) | A variable-pitch counterfactual closed through the same loop |
| **Atmosphere.** Every number here is at sea level; the configuration's own altitude sensitivity has been computed for hover power and propeller efficiency, but its effect on the Section 4 comparison has not. | The comparison in Section 4, made against a mission flown at altitude | Analysis; the direction of the effect has not been computed |


---

## D. Your own proposals

Open, as always.

---

## E. Errors (one list)

- **Qwen (Round 211, acknowledged by Qwen):** proposed removing the rotation-time subsection, which holds a protected row the author placed there (E15).
- **Claude:** none found this round.
- **Grok, ChatGPT, DeepSeek:** none found.

---

## F. What goes to the author

**Nothing for decision.** When the supplement generator and the receipt table are done, the completed package (body, supplement, references, AI statement) goes to the author for the submission decision.
