# Revision ledger — Journal of Aircraft 2026-10-C039418

> **Confirmed by all four readers and Claude, Round 225.**

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
| M-01 | **Two section lists in the submission mix the numberings.** (i) Body, Sec. VIII.A, Table 6, the runway row: *"Claimed as sized, not demonstrated (Secs. III, 7)"*. It should read *Secs. III, VII*. (ii) Supplement, the S11 heading: *"Working for Secs. III, 6.2 and 7"*. It should read *Secs. III, VI.B and VII*. Cause: in a list of section numbers, the generator converts only the first one (sources: `paper/v8/ASSEMBLED.md` *"(Sections 3, 7)"*; `supplement-src.md` line 454 *"Sections 3, 6.2 and 7"*). A full scan of both submitted LaTeX files (2026-10-02) found **no other** Arabic section number after *Sec./Section* | Sec. VIII.A, Table 6; Supplement S11 heading | Claude, while preparing this ledger, 2026-10-02 | R | any revision; or a reviewer notes it | open; fix the generator's list conversion and both places at revision. **Round 225 additions:** fix at the generator first, rebuild, rerun the scan, check the rendered PDF (ChatGPT); add a build-time check that flags any Arabic number after *Sec./Section* in the output (DeepSeek proposal, to be voted at revision); the scan would not catch a bare section number outside *Sec./Section* (Grok), so the revision rescan also reads section lists by eye. **Finding confirmed by all four and Claude (Round 225)** |
| M-02 | The cover letter says *"Full-Length Paper"*; the *Journal of Aircraft* ScholarOne type is *"Full Paper"* | cover letter (submitted) | Claude, 2026-10-02 | — | none | record only |
| M-03 | ScholarOne shows Ömer Gülmen's affiliation as *", Independent Researcher,"*: an empty department field leaves a leading comma | ScholarOne metadata, not the manuscript | Claude, 2026-10-02 | — | none | record only; can be fixed in the account profile |

## C. Questions that stay closed unless a trigger occurs
- **The 26 references** were cross-checked field by field by all four readers in Rounds 195–198. They are reopened only if a specific defect is named.
- **The roll script:** see L-08.
