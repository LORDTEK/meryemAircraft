# Number provenance: abstract, cover letter, conclusions (Section VIII)

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
