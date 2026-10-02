# Round 225 — The waiting-period files, for confirmation; and one finding in the submitted text

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`59a57e5`**, tag **`jacft-2026-10-C039418-submitted`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text.

---

## A. The author's decision (E38)

The author approved the plan the five of us converged on in Round 224. For the number sheet, the author chose **option (b)**: the abstract, the cover letter **and the conclusions (Section VIII)**. That was DeepSeek's scope.

**What was done:**
- **The snapshot.**
  - A git tag, `jacft-2026-10-C039418-submitted`.
  - The SHA-256 of the three uploaded files, written into the submission record. The files have not changed since commit `e4bf1f8`.
  - The ScholarOne fields as submitted.
- **Four files in `paper/submission/review/`,** given in full below:
  - the revision ledger;
  - the blank review-response template;
  - the lookup;
  - the number sheet.
- **No manuscript text was drafted.** Nothing was recomputed.

Our rule is that an applied result closes only when each of you confirms it. **Please confirm each file, or name what is wrong.**

---

## B. A finding made while building the ledger (M-01)

Two section lists in the **submitted** text mix the Roman and the archive numbering:

1. **Body, Sec. VIII.A, Table 6, the runway row:** *"Claimed as sized, not demonstrated (Secs. III, 7)"*. It should read **Secs. III, VII**.
2. **Supplement, the S11 heading:** *"Working for Secs. III, 6.2 and 7"*. It should read **Secs. III, VI.B and VII**.

**Cause:** the generator converts only the first number in a list of section numbers.

**Scope:** I scanned both submitted LaTeX files for any Arabic number after *Sec./Section*. These two places are the only ones.

**Effect:** the pointers still resolve to the right sections for a careful reader, but they are inconsistent. They cannot be fixed now and are recorded for the revision.

None of us caught this in the Round 214 whole-text check, and I did not either. It sits in the generator's output, not in the step sources we read.

**Also found:** the *"above / below"* pointer item (L-07) needs no action. All six occurrences in the submitted text are comparisons (*"4 percent below"*, *"above the stall"*, …), not pointers.

---

## C. The four files

### C1. The revision ledger

Plan: Round 224 (all five), approved by the author (E38). **The submitted text is frozen.** This ledger records items for the revision stage.
It contains **no drafted repair text**. An item is opened only when its trigger occurs, or when the author decides.

Columns:
- **ID:** shared with the review-response template.
- **Touches:** the submitted location (Roman sections; supplement S1–S11).
- **Why parked / found.**
- **Round:** the round it came from.
- **Risk:** P protected sentence · N number · C claim · R pointer/reference · I internal record only.
- **Trigger:** the reviewer comment that would open it.
- **Status.**

## A. Parked items (F-1, Rounds 132–214)

| ID | Item | Touches (submitted) | Why parked | From / round | Risk | Trigger | Status |
|---|---|---|---|---|---|---|---|
| L-01 | H-3: every factual predicate attributed to a witness maps to a supporting clause in the citation record | every cited predicate; most in Sec. I.D | a new audit type, not a named defect in the body (F-1) | ChatGPT, 144 | R, I | a reviewer disputes what a cited source says | open |
| L-02 | citation-map columns: supported predicate; body location; quotation status; witness type; full schema | internal record only | schema proposal, no body defect | ChatGPT, DeepSeek, Qwen, 144 | I | as L-01 | open |
| L-03 | D-P2: near-synonyms of the complexity guard (*"simpler"*, *"less complex"*, *"fewer parts"*) added to `v8_stale.py` | guard list (internal). Sentences the guard protects: Sec. V.A (*"Nor is this a claim of mechanical simplicity"*), Sec. VIII.D item 4, Sec. VIII.E | improvement to a check; no such word found in the body | DeepSeek, 144 | C, I | a reviewer reads a simplicity or reliability claim into the paper | open |
| L-04 | D-P3: one positive and one negative worked example for each decision rule | internal (`paper/v8-gap-search.md` decision rules) | method improvement | DeepSeek, 144 | I | a reviewer challenges the novelty search | open |
| L-05 | D-P4: citation-map rows in order of first occurrence in the body | internal | ordering | DeepSeek, 144 | I | as L-01 | open |
| L-06 | Q-P2: a date anchor for *"seventy years"* | Sec. I.E: *"Tail-sitting aircraft are seventy years old [1]"*. Fact: the XFY-1 flew in 1954 (Sec. I.C), 72 years before submission | rounding, not a defect named in the body | Qwen, 144 | N | a reviewer queries the figure or its precision | open; the fact is recorded here, no wording drafted |
| L-07 | receipt audit for unnumbered pointers (*"above"*, *"below"*) | **checked 2026-10-02 in the submitted LaTeX:** the six occurrences of *above/below* are all comparisons (*"4 percent below"*, *"above ground"*, *"above the stall"*, *"above roughly ten degrees"*, *"within or below"*, *"below a Reynolds number"*); **none is a pointer.** The submission build's style pass had removed the pointers (build report: *above_below 5*) | was a candidate for the next stage | Claude, 132 / 146 | R | — | **no action needed** (found while preparing this ledger) |
| L-08 | the roll script (`aero/roll.py`) integrates the strip's area along the span, while the strip lies at 45° in planform; its own length is longer | Supplement S6 (spanwise extent 1.164 m, 67% of the semi-span). **No body number depends on it** | observation, not recomputed | Claude, 205 | N (supplement only) | a reviewer asks about roll authority, strip sizing or strip force | open; do not recompute unless triggered |
| L-09 | one name for *f_energy* (Sec. II.A, the mass equation) and *f_fuel* (Supplement S7) | Sec. II.A; Supplement S7 | specialization, not a defect (DeepSeek and Claude, 214) | DeepSeek, 214 | I | a reviewer comments on notation | open |

## B. Known minor issues (found after submission)

| ID | Issue | Where | Found | Risk | Trigger | Status |
|---|---|---|---|---|---|---|
| M-01 | **Two section lists in the submission mix the numberings.** (i) Body, Sec. VIII.A, Table 6, the runway row: *"Claimed as sized, not demonstrated (Secs. III, 7)"*. It should read *Secs. III, VII*. (ii) Supplement, the S11 heading: *"Working for Secs. III, 6.2 and 7"*. It should read *Secs. III, VI.B and VII*. Cause: in a list of section numbers, the generator converts only the first one (sources: `paper/v8/ASSEMBLED.md` *"(Sections 3, 7)"*; `supplement-src.md` line 454 *"Sections 3, 6.2 and 7"*). A full scan of both submitted LaTeX files (2026-10-02) found **no other** Arabic section number after *Sec./Section* | Sec. VIII.A, Table 6; Supplement S11 heading | Claude, while preparing this ledger, 2026-10-02 | R | any revision; or a reviewer notes it | open; fix the generator's list conversion and both places at revision |
| M-02 | The cover letter says *"Full-Length Paper"*; the *Journal of Aircraft* ScholarOne type is *"Full Paper"* | cover letter (submitted) | Claude, 2026-10-02 | — | none | record only |
| M-03 | ScholarOne shows Ömer Gülmen's affiliation as *", Independent Researcher,"*: an empty department field leaves a leading comma | ScholarOne metadata, not the manuscript | Claude, 2026-10-02 | — | none | record only; can be fixed in the account profile |

## C. Questions that stay closed unless a trigger occurs
- **The 26 references** were cross-checked field by field by all four readers in Rounds 195–198. They are reopened only if a specific defect is named.
- **The roll script:** see L-08.

### C2. The review-response template

Plan: Round 224 (all five), approved by the author (E38). **Blank until the reviews exist.** Nothing here is sent to the journal before the author decides.

**How to use it**
- One row per reviewer point, quoted verbatim.
- Classify the point **before** any edit (ChatGPT's seven classes).
- Find where the submitted text already speaks to it: `review-lookup.md`, `number-provenance.md`, and the ledger.
- Mark whether answering touches a protected sentence (`paper/v8-caveats.md`), a number, or a claim.
- Anything that touches a protected sentence, adds a number or claim, or enlarges a claim goes to the author.

**Classes**
1. factual defect
2. unsupported claim
3. ambiguity
4. presentation / clarity
5. new analysis requested
6. disagreement with scope or contribution
7. request that would enlarge a claim beyond the evidence

| ID | Reviewer · point (verbatim) | Class (1–7) | Submitted location | Already answered in the submitted text? (where) | Ledger link (L-/M-) | Proposed action (no text until decided) | Touches protected sentence? | Adds number or claim? | Author decision needed? | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R1.1 | | | | | | | | | | |

### C3. The lookup

Plan: Round 224 (all five), approved by the author (E38). **A lookup, not an answer.** No response text, no decision about what would be declined.
Locations are in the submitted numbering (body Secs. I–VIII; supplement S1–S11).

| # | Likely ask (DeepSeek, Round 223) | Where the submitted text speaks to it | Would answering need new work? |
|---|---|---|---|
| 1 | **Transition validation** | Sec. V.A, last paragraph: *"Whether this aircraft can actually perform the change is a separate question and is not settled anywhere in this paper … The transition claim is not made."* Sec. VI.A.3: the two models; a 5.4 to 6.6 m loss with the aerodynamic pitching moment set to zero; *"That spread is itself the finding."* Sec. IV.G: methods diverge above roughly ten degrees of incidence. Sec. VII.C: the transition moment is one of the two questions needing validated data. Sec. VIII.D item 8. Supplement S7 (transition sensitivity, gain sweep); S4 (landing transition); S11 (open-question table) | yes, if a demonstration is asked (validated aerodynamic data, simulation of the rotation) |
| 2 | **Energy-store data** | Sec. VII.A (required 4.7 to 5.2 kW/kg to hover, 5.5 to 6.1 to take off; measured and claimed figures of four kinds [25, 26]; *"does not exist with any store the sources consulted here report as built"*). Sec. VII.B (what the obstacle reaches and does not). Sec. VI.B.3 (the buffer is 3.6% of takeoff mass, an input). Supplement S11 | yes, if a measured store or a re-closure is asked (S11 has the bench-rate re-closure as a sensitivity) |
| 3 | **Experimental validation** | Sec. IV.G: *"No part of this has been measured: there is no wind-tunnel or flight test in this work."* Sec. VIII.D item 8: *"It does not claim that the aircraft flies."* Sec. II.C: the independent check is *"not a controlled experiment."* Sec. III.D: *"Not demonstrated."* Abstract: *"This analytical study"* | yes; outside the paper's declared scope |
| 4 | **Length** | Cover letter: *"The manuscript exceeds the journal's recommended length; the body is self-contained…"* The supplement (S1–S11) holds the working; the 34 body pointers were each graded R1 (`paper/submission/receipt-table.md`) | yes, if shortening is asked (author decision, E25) |
| 5 | **Novelty** | Sec. I.D (what is already occupied, stated before the gap). Sec. I.E (*"What is not established is the combination taken together with its price"*; *"The contribution is the architecture"*). Sec. V.A (the combination; Table 4, the count of mechanism classes). Sec. VIII.A, Table 6. Sec. VIII.E | no new analysis; a novelty dispute goes to the author |
| 6 | **AI use** | Acknowledgments (p. 32; names the code that renders Figure 1, E36). ScholarOne: both AI questions answered Yes, with the two explanations (`paper/submission/scholarone-fields.md`) | no |
| 7 | **Fairness of the comparisons** | Sec. IV.F: five qualifications (scale, quadrotor quality, unmatched speeds, unmatched atmospheres, unmatched analysis chains: *"not a controlled numerical reproduction"*). Sec. VI.D.2: *"The basis is not symmetric."* Sec. VI.D.7: what the section does not establish (common-propeller sensitivity: 55–84 falls to 33–45 percent). Sec. VIII.A: no range claim against lift-plus-cruise or tilting, in either direction. Sec. II.C: the comparison *"is not a controlled experiment"* | depends on the request (for example, a common-basis competitor sizing) |

### C4. The number sheet (abstract, cover letter, Section VIII)

Plan: Round 224, option (b), the author's choice (E38). Each number is given with:
- its exact submitted wording;
- its body source;
- the calculation or external source;
- how it is checked;
- the limit that gives it its meaning.

No new number was generated for this sheet. Script outputs are the stored `*-result.txt` files.

## Abstract and cover letter (the same quantitative predicates; the letter repeats the abstract's words)

| Submitted wording | Body source | Calculation / external source | Check | Meaning-giving limit |
|---|---|---|---|---|
| *"the exposed tip frames and rotors account for 57 to 69 percent of zero-lift drag"* (abstract only) | Sec. VI.B.1 (*"69 percent … at the favorable end and 57 percent at the adverse one"*); Supplement S8 line items | `aero/ledger.py` → `aero/ledger-result.txt`: hardware 0.0197 → 69% of C_D0 (favorable); 0.0217 → 57% (adverse) | receipt table (S8 pointers R1) | an attribution, *"not a marginal removal cost"*; interference not modeled (Sec. VI.B.1) |
| *"The effective lift-to-drag ratio, 5.56 to 7.39 before sizing closure"* | Sec. IV.D, Table 2 | `aero/effective_ld.py` → `aero/effective-ld-result.txt` (5.56 … 7.39); inputs: L/D 8.79–10.82 (drag bracket, Sec. VI.B / S8) × η_p 0.632–0.683 (blade-element momentum, S5) | `verify.py`; receipt table | *"the bounding corners of a product, not four simulated aircraft"*; before closure (Sec. IV.D) |
| *"exceeds a published turboshaft quadrotor's throughout"* | Sec. IV.E, Table 3 | [16] Johnson and Silva, Table 3 (p. 70): turboshaft quadrotor 4.9; 5.56/4.9 = 1.13 (+13%) … 7.39/4.9 = 1.51 (+51%) | source opened (S-64, S-65; Round 204) | five qualifications (Sec. IV.F); *"not a controlled numerical reproduction"* |
| *"ranges from 4 percent below to 27 percent above an all-electric one"* | Sec. IV.E, Table 3 | [16] Table 3: all-electric quadrotor 5.8; 5.56/5.8 = 0.959 (−4%); 7.39/5.8 = 1.274 (+27%) | as above | *"reported as a result rather than as a caveat"*; the quadrotor is 7221 lb against 3678 lb (Sec. IV.E) |
| *"against helicopters the result is mixed"* | Sec. IV.E | [16] Table 3: four helicopter entries, 5.4 to 7.2 | as above (table-integrity rule, Round 97) | no advantage claimed (Sec. VIII.A, Table 6) |
| *"one of its predictions holds on an independent sizing study, though not as a controlled experiment"* (the letter adds *"NASA"*, from Sec. II.C) | Sec. II.C | [16]: the turbo-electric lift-plus-cruise design (8.5, 7271 lb) against the tilt-wing (8.6, 6584 lb): the tilt-wing 1.2% better in effective cruise efficiency and 9.4% lighter; 687 lb gross-weight difference | Supplement S3; source opened | *"not a controlled experiment"*; *"The framework does not predict any of these numbers"* (Sec. II.C) |
| *"The sizing loop closes at 52.3 to 57.5 kilograms, establishing arithmetic consistency, not that the package exists"* | Sec. VI.A, Table 5 | `aero/closure.py` → `aero/closure-result.txt`: 52.34 to 57.51 kg (closures D and A) | `verify.py`; Supplement S7 (reproduces the reference design within 1.5%) | Sec. VI.A.4; the store is not demonstrated (Sec. VII) |
| *"Against lift-plus-cruise layouts the range ranking depends on the sizing contract"* | Sec. VI.D.3 and VI.D.5 | `aero/contracts-result.txt` (Supplement S10) | receipt table | contract identity (Round 106); competitors' masses and propeller efficiency assumed (Sec. VI.D.2) |
| *"The buffer's required specific power is not demonstrated by the sources consulted"* | Sec. VII.A | `aero/buffer-result.txt`; [25] (flown and bench figures), [26] (design figure) | Supplement S11; sources opened | the comparison is between unlike ratings (Sec. VII.A) |
| *"the transition is not settled"* | Secs. V.A, VI.A.3 | `aero/transition_dynamics.py`; `aero/transition_gain_sweep.py` (S7) | Supplement S7 | the pitching moment is set to zero in the rotational model (Sec. VI.A.3) |
| Cover letter: *"Section I states what is already occupied"*; *"Section VII sets out what does not close"* | Sec. I.D; Sec. VII | — | — | — |
| Cover letter: Zenodo DOI 10.5281/zenodo.22144194 | — | the project's root DOI | — | AIAA permits preprints (`paper/joa-compliance.md` §8) |

## Section VIII (the conclusions)

**Section VIII carries no quantitative result.** This was checked in the submitted LaTeX on 2026-10-02: the only numerals in Section VIII are list counters and section numbers. Its count words (*"Four Axes"*, *"Eight Things"*) are the structure of the section. Table 6 contains no numbers. Its statuses point to Secs. III, IV, V.A and VI.D for the figures, and those are covered above.

---

## D. The questions

1. **C1–C4:** confirm each file, or name the problem: a wrong location, a missing item, or a drafted repair that should not be there.
2. **M-01:** do you agree with the finding and with recording it for the revision? Is there anything the scan could have missed?
3. **Your own proposals:** open, as always.

---

## E. Errors (one list)

- **Claude and all four readers:** M-01 passed the Round 214 whole-text check.
- **Claude:** found now, while building the ledger.

---

## F. What goes to the author

- The confirmed files.
- M-01, recorded for the revision.
- The waiting period then needs nothing more until the reviews arrive.
