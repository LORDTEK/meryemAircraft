# Round 226 — The Gate 7 road plan for the final v9: review it before work starts

**Readers: twelve channels.** Claude, Codex and Grok (council); GLM-5.3, DeepSeek and Qwen (Token Plan API); ChatGPT, Grok, DeepSeek, Qwen and Z.ai (web). This text was prepared by a Claude session working in the repository. That session is not the council's Claude channel; its checks below are offered for everyone to verify and contest.

---

## 0. Where the work stands

- ***Journal of Aircraft*, Manuscript 2026-10-C039418.** The paper (v8) was submitted on 2 October 2026 and desk-rejected on 14 October by the Associate Editor, without review: *"The paper does not provide any developments that are of archival nature."* Nothing is under review anywhere now.
- **v9 is the current manuscript.** It was prepared through the council's Gates 1–6 and is targeted at *Aerospace Science and Technology*. It is 25 pages in `elsarticle`, with a 16-page supplement.
- **The author's decision (2026-10-29):** the architecture is the centre and the accounting is the instrument. The paper stays v9: there is no v10. The administrative items (address, photographs, declarations) are not part of this plan.
- **The author's principle (2026-10-29):** *move first on the work everyone agrees on; the divergent items are decided by the results of that work.*

**Files referred to below, for verification only.** Every passage you are asked to judge is quoted in this text.

| File | SHA-256 |
|---|---|
| v9 manuscript PDF | `a6d795aa5c85fe7cb8d6fc0b0034b62b4e22afb0c03fb5d1b3a0450d39d72006` |
| v9 supplement PDF | `c024449695bc15930956fe8234035047d24b2c036e3beff5c43898d2d39e2c5b` |
| v9 LaTeX source (zip) | `32b2a0c1c9388113b40f03e0efd522b93755e7995d95ac150882c47e64a3042a` |
| Analysis code (zip; repository commit `b3c1bd4`) | `6c628000963416988fe27537340721ff1e821447520e341e19afa34ff0d9cb0c` |
| Re-implementation prompt, scripts and outputs (zip) | `42e4845421d33d02d4579211667b9129fb16b256f78ca2c8df4e70dbf008a70c` |

---

## 1. The plan, in full

The author wrote the plan in Turkish; the translation below is the Claude session's. One phrase in item 4 is interpreted, and the interpretation is marked.

> ### Gate 7 — Road plan (for the final v9)
>
> Date: 2026-10-29. Two rounds, twelve channels. Architecture is the centre, accounting the instrument. The paper stays v9; the administrative items (address, photo, declarations) are not in this plan.
>
> Principle (author, 2026-10-29): move first on the work everyone agrees on; the divergent items are decided by the results of that work.
>
> **Phase 1 — Work everyone agrees on (start now)**
>
> *Writing:*
> 1. **A2:** a comparison table against [9]–[11] on the same criteria. Criteria: regime-change method, reorientation mechanism, attitude control, power architecture, level of evidence.
> 2. **A5 consistency pass:**
>    - W^3/2 versus W;
>    - "six times" versus 5.8–6.4;
>    - the Table 4 caption tied to the store condition;
>    - the warning on the 927–1,233 km range comes back.
> 3. **Claim–evidence chart:** columns claim → quantity → evidence → falsifier. Thresholds are written BEFORE the runs; the word "preregistered" is not used.
> 4. **Bill 2 in range terms:** one sentence. Against the airframe in its hub-only state *[translator's note: read as v9 Sec. 4.3's "without the tip frames and rotors"; correct me if that is wrong]*, the range loss is about 42–47 percent (from the ratio 0.526–0.577). The number takes the B1 band; it is not given as a single point.
> 5. **Provenance column:** Table S2a gets a column assumed / computed / quoted.
> 6. **Standing decisions:** Eq. 3 is not a contribution. The title carries no accounting word; "meryemAircraft:" stays.
>
> *Calculation (all with the existing code):*
>
> 7. **B4 closure gates:**
>    - store power (bench average and continuous value) and energy;
>    - one bound for the omitted electrical and installation mass;
>    - landing: not analysed;
>    - competitor assumptions.
> 8. **Roll authority = diameter limit check:** one calculation, two uses (Z.ai's merge). The required roll moment is compared with the moment the strip provides; the uncertainty in the slipstream share is stated explicitly. The same calculation shows the hover and takeoff margin of the 0.20 m diameter.
> 9. **B1 drag band:**
>    - Run A: NeuralFoil, as it is.
>    - Run B: the same `sifir_tork` solver with Sheldahl–Klimas at Re 8e4. Label: "Eppler synthesis, not measurement".
>    - Floor: the flat-plate value 0.0094.
>    - Frame: the present Cd 0.15 against Hoerner's faired value. The rotor/frame split is 0.0154 / 0.0043.
>    - Molaa and Ohtake: only as a finite-wing envelope (AR 2, figure); not an input to the strip code.
>    - XFOIL: code check only.
>    - If A and B diverge, a windmill-momentum calculation is used as arbiter.
> 10. **B5:** the band is carried into the closure; the break-even thresholds are updated.
> 11. **Value (B3):** one capability paragraph from our own closures (radius, time on station). Also a single altitude run with `nose_propeller_altitude.py` (1,500–3,000 m for fire observation). No new mission model and no competitor sizing.
>
> Order of work: 1–6 and 8 start now, in parallel → 7 (B4) → 9 (B1) → 10 → 11. Seven channels support this order; Qwen web says B1 first, GLM says one combined pass. In the paper B1 and B4 are written as one section: bounds first, then propagation.
>
> **Phase 2 — Depends on the Phase 1 results (no decision now)**
>
> | Item | Depends on | Views |
> |---|---|---|
> | B2 fairing-chord sensitivity (supplement only) | whether item 8 shows margin in the diameter | If there is no margin, one sentence: "tip drag is the price of hover control". Never a diameter sweep. Grok still says "no". |
> | Feasibility map | when the gate table exists, and only if it can be drawn from the same numbers | Table as the spine: Qwen TP, Codex, Grok, DeepSeek web, Z.ai. Map: GLM, DeepSeek TP, ChatGPT, Qwen web. |
> | 2-D RANS for the frame | only if B1 cannot pass its threshold | No RANS on the rotor (unanimous). |
> | Transition envelope | if the existing 3-DOF model runs without rework | Yes: Z.ai, Qwen TP/web, Codex (limited). No: Grok ("5.4–6.6 m is already written"). |
> | Gyroscopic number | if the item 8 calculation gives it as a by-product | Two sentences: Z.ai, Qwen. Not needed: Grok, Codex. |
> | "How to audit" box | — | In the supplement: Z.ai, Qwen TP. No: Grok, Codex, Qwen web. |
>
> **Phase 3 — When the text freezes**
> - The abstract and highlights are written LAST; they do not freeze before the B1 and B4 numbers are known.
> - B6, the blind re-implementation, is run once, on the frozen text. Only Qwen web opposes B6; the others want it because it tests whether the text is sufficient.
>
> **Definitely out (unanimous, or the author's decision)**
> - Diameter sweep and redesign; reaction torque for roll (another paper).
> - Rotor RANS; Monte Carlo or Sobol.
> - A new mission model; an invented competitor for 13 kg; a NASA ranking test; a second "law".
> - A first-person paragraph by the authors: the author's decision (2026-10-29). That text was already written in earlier versions and will not be rewritten.
> - v10.
>
> **Word budget**
> 12K is a hard limit, and the paper must get shorter. Every addition is paired with a cut. New tables (A2, gates) go in the body; detail goes to the supplement.
>
> **Not yet verified (does not enter the plan as a number)**
> - "The store is power-limited, about 0.2 kWh" (GLM): B4 computes it.
> - 42–47 percent: Grok derived it from the paper's numbers; it is recomputed after B1.

---

## 2. Checks of the plan against v9 and the code

These are facts with locations, checked by the Claude session, plus three questions about method (C7–C9). They are offered for verification, not as votes. Where a check is wrong, say so with the location.

**C1. W^3/2 and W are both correct, under different conditions (item 2).**
- v9 Sec. 2.1, Bill 1: *"at fixed disc area the hover power it requires grows as W^{3/2}."*
- Supplement S7: *"Because the disc loading is fixed, hover power is itself proportional to takeoff mass."*
- The sizing loop holds disc loading fixed (44.2 kg m⁻²).

The repair is therefore to name the held quantity in each place, not to make one sentence match the other.

**C2. "About six times heavier" is 5.8–6.4 (item 2).** The closures are 52.3–57.5 kg; v9 gives the re-closure at 0.892 kW/kg as *"about 335 kg"* (v8's supplement gave 333.5–335.2 kg). The ratio is 5.8 (closure A) to 6.4 (closure D). The arithmetic holds.

**C3. The basis of item 4.** v9 Sec. 4.3: *"Without the tip frames and rotors, the lift-to-drag ratio would be 20.55 and 15.24; the configuration retains 52.6 and 57.7 percent of it."* With range proportional to L/D, the loss is 42.3–47.4 percent, but only at fixed fuel fraction, propeller efficiency and fuel-to-shaft chain. Removing the tip pairs also removes the hover attitude control and changes the mass. The sentence therefore prices the drag; it does not describe an alternative aircraft.

**C4. The 0.0094 flat-plate floor (item 9) was not found.** It does not appear in the v9 manuscript, the supplement or the code archive (text search). Which channel produced it, and how? Until it is located it has the same status as the two numbers in the "not yet verified" list.

**C5. The rotor/frame split has two ends (item 9).** Supplement Table S4:

| | favourable end | adverse end |
|---|---|---|
| Tip frames | 0.0043 | 0.0047 |
| Tip-pair rotors, free-wheeling | 0.0154 | 0.0169 |
| Total zero-lift drag | 0.0285 | 0.0381 |

The plan quotes the favourable end only. Frames plus rotors are 69 percent of zero-lift drag at the favourable end and 57 percent at the adverse end. That is the abstract's 57–69 percent.

**C6. None of the B1 sources is in the repository** (Sheldahl–Klimas, Hoerner, Ohtake, "Molaa"). Under the standing source rule, a number taken from a source table needs the document opened in the round that uses it. Requests:
- The channel that proposed each source gives its exact citation and a working download link.
- "Molaa" in particular needs a full reference.
- For Sheldahl–Klimas (Sandia report SAND80-2114, 1981, as the Claude session recalls it; please verify), confirm from the report itself that its low-Reynolds entries were generated by the Eppler code rather than measured. The plan's label assumes this.

**C7. Can windmill momentum arbitrate between Run A and Run B? (method question, item 9).** At zero shaft torque, the power the rotor takes from the stream equals the blades' profile power. The axial force at equilibrium therefore depends on the section drag that Runs A and B dispute. Momentum theory turns a given section drag into rotor drag; it does not choose between two section-drag sets.

What it can supply is an upper bound: the actuator-disc maximum for a windmilling disc. Question to the proposer and to everyone: what exactly is the arbiter's output, and how does it avoid depending on the disputed quantity?

**C8. Item 8 needs a stated "required" moment, and its axis named for hover (method question).**
- v9 Sec. 3.1: *"the longitudinal axis is the roll axis in both regimes, so a moment about it appears as a heading change in hover and as bank in cruise."* The strip's moment in hover is therefore a heading moment.
- v9 Sec. 5 names two candidate requirements, neither yet computed: *"each pair is torque-balanced in cruise, leaving a small hover residual whose absorption is not shown"*; and gust rejection in hover, *"not analysed."*

Under item 3, the required moment and its source are written before the run. A further question to Z.ai, as the proposer of the merge: which quantity links the strip moment to the 0.20 m tip-rotor diameter? Per v9 Sec. 3.1, the tip pairs give pitch and yaw at arms of 0.71 m and 1.726 m, and the strip gives the body-roll axis.

**C9. Item 11 mixes two states unless it is scoped (method question).** The docstring of `nose_propeller_altitude.py` says that altitude changes the cruise advance ratio while hover (J = 0) is independent of it. The script covers the nose propeller only; it does not re-close the sizing.

At 1,500–3,000 m, hover power, store sizing and engine sizing all change. A capability paragraph built from sea-level closures, placed beside a propeller result at altitude, would combine two operating states. Question: is the altitude run reported as a propeller result only, and does the capability paragraph name sea level?

**C10. The word budget, measured on v9.**
- pdftotext gives 7,850 words from the abstract through the references, and about 6,800 from the Introduction to the start of the references.
- The source has 6 tables and 2 figures.
- The plan says *"the paper must get shorter,"* while adding the A2 table, a gate table, the claim–evidence chart (location not stated), the Bill 2 sentence and the capability paragraph.

*Aerospace Science and Technology*'s counting rule for tables and figures is not in the plan. Which count does the 12K apply to, and where does the claim–evidence chart go?

**C11. Items open from the v9 review that the plan does not list.** Each was verified against v9 or the record:
- **(a) Vegh [11].** Round 197 decided *"Cite the SciTech paper, AIAA 2025-1436, with its correction notice."* The notice is missing from v9, and was already missing from the v8 text sent to the *Journal of Aircraft*.
- **(b) The reproducibility sentence** (v9 Sec. 3.2): *"both then reproduced all 39 tabulated values … within 0.25 percent."*
  - Rerunning both scripts reproduces their recorded outputs exactly.
  - DeepSeek's largest deviation is 0.253 percent (closure D, buffer mass).
  - Some of the 39 values are calibration targets rather than reproductions. Qwen back-solved the figure of merit from closure A's hover power and the fuel–engine product from closure A's range. DeepSeek back-solved the figure of merit from Table 5's hover powers and the range constant from closure D's range.
  - No run was made after Table S2a was added, yet the text says the inputs are *"now stated."*
  - B6 (Phase 3) is the natural place to repair this. Should the sentence be corrected now, under A5?
- **(c) The simplicity claim against tilting architectures.** This is the author's decision of 2026-10-16/17, and the v8 text carries it (*"The arrangement is therefore mechanically simpler than a tilting architecture: a moving mechanism is more complex than a fixed structure …"*). v9 says instead: *"No comparison of part count, mass or reliability is made."* The plan does not mention it. This is not put to a vote. The question is only where in the plan it is restored, which is for the author.
- **(d) Section 1.3 and the highlights.** v9 says *"This paper makes three contributions"*, with the accounting first. Four of the five highlights concern the accounting, the contracts or the inputs, and none names the regime change without propulsor reorientation. The author's centre decision implies a rewrite of Sec. 1.3. The plan covers the title (item 6) and the highlights (Phase 3), but not Sec. 1.3.

---

## 3. Questions

Answer each by number. Agree, amend or object, with one reason. "Agree" with no reason is fine where you have nothing to add.

**Q1. Phase 1, items 1–6.** Agree / amend / object, for each item. For item 1, say also whether A2 should replace or extend v9's Table 1, which already compares the closest work on airframe, propulsors, control about the thrust axis, power, and evidence. The word budget is the reason to ask.

**Q2. Phase 1, items 7–11,** with C3–C9 in view. In particular:
- **C4:** the source of 0.0094;
- **C6:** citations and links for every B1 source;
- **C7:** what the windmill arbiter outputs;
- **C8:** the required moment, its source, and the strip–diameter link;
- **C9:** the scope of the altitude run.

**Q3. Order of work.** Seven channels support 1–6 and 8 → 7 → 9 → 10 → 11. Qwen web proposed B1 first; GLM proposed one combined pass. Qwen web and GLM: has anything changed your view? Everyone else: answer their reasons, not only the count.

**Q4. Phase 2.** For each row, give your position in one line. The existing positions are in the plan's table, and each channel is asked to answer the opposing argument by name. Specifically:
- **B2.** Grok: what would change your "no" if item 8 shows a margin?
- **Transition envelope.** Grok says 5.4–6.6 m is already written. Those in favour: what would the envelope add that the written figure does not?
- **Feasibility map against table.** Can the map be drawn from exactly the gate-table numbers, or does it need new ones?

**Q5. Phase 3.** Qwen web: your reason against B6, so the others can answer it. Everyone: should B6 declare in advance which values are calibration targets and which are tests (C11b)?

**Q6. "Definitely out."** Any objection, with a reason? Silence means none.

**Q7. Word budget (C10).** Which count does the 12K apply to under the target journal's rule, and which cuts pair with the planned additions?

**Q8. C11 (a), (b), (d).** Add them to Phase 1, or leave them out? Item (c) goes to the author; you may give a view on where it fits.

**Q9. Open proposals.** Anything else: a cut, a move, a restructuring or an idea, with its reason. Proposals are put side by side to everyone next round.

---

## 4. Errors found in the last exchange (one list, all sources)

These come from the readers' reviews of the v9 PDF. Each was checked against v9 or the record. The list is for the record and is not a judgement of anyone.

| # | Source | Statement | Finding |
|---|---|---|---|
| 1 | DeepSeek | The AI-declaration paragraph appears twice on p. 22 | It appears once. |
| 2 | DeepSeek | Sec. 4.1 is truncated | Page break only; the sentence completes on the next page. |
| 3 | DeepSeek | Table 1 reads "Eleven", "ac- and"; the name is misspelled "myermyAircraft" | The source has "Elevon" and "accounting and contracts"; "myermy" occurs nowhere. These are text-extraction artefacts. |
| 4 | DeepSeek | The stopped-rotor sentence in Sec. 4.3 is wrong | v9 is right. With the rotor axis parallel to the cruise flow, the projected area is independent of azimuth; an edge-on blade needs feathering. **The error was v8's** (*"stopped edge-on … 0.0008"*). |
| 5 | DeepSeek | v8 and v9 disagree on 0.892 kW/kg; one must be wrong | v9 is right. The source table (Yu et al.) says *"440 A (Calculated from 4 × 110 A)"*. **v8's "flown system … rated at 0.892" was loose.** |
| 6 | Qwen | v8 is under review at the *Journal of Aircraft*; v9 cannot be submitted | v8 was desk-rejected on 14 October; v9 targets *Aerospace Science and Technology*. |
| 7 | Qwen | The simplicity claim remains forbidden | The author withdrew that rule on 16 October (see C11c). |
| 8 | Qwen | The PDF has spacing artefacts ("takeoffmass", "f amilies") | Not found in the PDF text. |
| 9 | Grok | v9 has sections 1–5 | v9 has six (6, Conclusions). |
| 10 | Claude | v8's stopped edge-on estimate (0.0008) and the "flown" wording for 0.892 | Both were in the text and records the Claude session kept; v9 corrected both. |
| 11 | Claude | Vegh correction notice | Voted in Round 197, omitted from the text sent to the *Journal of Aircraft*. |
| 12 | Claude | Cover letter to the *Journal of Aircraft*: *"we have no conflicts of interest to disclose"* | The patent application TR 2026/014570 was filed on 26 August, before the submission. The Claude session wrote the letter without asking about patents. v9 declares the application. |

---

## 5. Answer format

Give your channel name first. Then Q1–Q9 by number; then any correction to Sections 2 or 4 with its location. Where you disagree with another channel, name it and answer its reason.

## 6. What goes to the author after this round

- **C11(c):** where the simplicity claim is restored. The author decides.
- **Phase 2:** any row on which the channels still diverge once the Phase 1 results exist. The author decides by those results, as the principle says.
- **C11 (a), (b), (d)**, if the channels do not agree on whether to add them to Phase 1.
- **The answers to C4 and C6.** If a source or number cannot be located, it does not enter the work, and the author is told which one.
