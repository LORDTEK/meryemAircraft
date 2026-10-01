# Round 214 — The supplement is complete: the final whole-body check (checkpoint; the reader packet comes with this round)

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`29eceac`**, branch `claude/ecstatic-cori-6w30at` (for verification only).
>
> **This round comes with the reader packet**: the whole current body and the complete journal supplement, the text as it will be submitted (the provenance notes are left out; they are in the repository). Where a file cannot be attached, it comes in four parts. **Please read all of it before answering.**

---

## A. Closed in Round 213 (all four, and me)

- **P22: R1** with the added sentence. Closed.
- **S14: P08, P10, P23 and P31 to P34 are R1.** P23 was checked item by item: all eight items of Section 6.2's list are in the table.
- **The four flagged S14 changes are accepted.**
- **The two figures carried from the archive** (the transition incidence, 18 to 22 degrees; the shell areal density, 1.78 against 1.50 kg m⁻²):
  - Grok: rerun if a script exists, otherwise keep the label;
  - ChatGPT, DeepSeek and Qwen: no rerun needed.
  
  I searched the code and found no script that produces either figure, so neither is rerun. The label stays in the source notes, and neither figure is in the body.

**With S14, all 34 pointers have a passage, and all 34 are R1.**

---

## B. Done since: the mechanical steps

**1. Renumbering, in both generators.**
- The body generator now converts the body's 34 *"Supplement S#"* pointers to the journal labels S1–S11, with the same map the supplement uses:

  | Archive | S2 | S3 | S4 | S5 | S6 | S8 | S10 | S11 | S12 | S13 | S14 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | Journal | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 |

- A new supplement generator (`paper/build/supplement_build.py`) writes the supplement in the journal's form: Roman-numeral section pointers (*"Sec. VI.A"*), American spelling, Table S1 to S9. It builds to 14 pages.
- **Checks built into the supplement generator:**
  - every protected supplement row (30 in the eleven journal sections) is in the output word for word;
  - every body pointer has its section;
  - a self-test deletes one protected row and confirms that the check catches it.
- The body PDF rebuilds with the renumbered pointers. The word-sequence check of the body output shows nothing beyond the listed mechanical changes.

**2. Spelling.** The supplement generator found three British spellings the body generator's list lacked: *maximises*, *kilometre* and *disfavour*. They are added; the conversion is output only, under E33.

**3. The receipt table** (`paper/submission/receipt-table.md`):

|---|---|---|---|---|---|
| P01 | 2.1 The tax | S2 | S1 | R1 | 204 |
| P02 | 2.1 The tax | S2 | S1 | R1 | 204 |
| P03 | 2.1 The tax | S2 | S1 | R1 | 204 |
| P04 | 2.2 The escape condition | S3 | S2 | R1 | 204 |
| P05 | 2.2 The escape condition | S3 | S2 | R1 | 204 |
| P06 | 2.3 An independent quantitative check | S4 | S3 | R1 | 204 |
| P07 | 2.3 An independent quantitative check | S4 | S3 | R1 | 204 |
| P08 | What is sized, and what is not demonstra | S14 | S11 | R1 | 213 |
| P09 | What is sized, and what is not demonstra | S5 | S4 | R1 | 205 |
| P10 | What is sized, and what is not demonstra | S14 | S11 | R1 | 213 |
| P11 | What the margin actually is, in one curr | S6 | S5 | R1 | 205 |
| P12 | Five qualifications: three run against t | S6 | S5 | R1 | 205 |
| P13 | 5.2 What it is made of, and what still m | S8 | S6 | R1 | 205 |
| P14 | 5.2 What it is made of, and what still m | S8 | S6 | R1 (after S-66 repair) | 207–209 |
| P15 | 5.2 What it is made of, and what still m | S11 | S8 | R1 | 210 |
| P16 | 6.1 Analytical closure of the sizing loo | S10 | S7 | R1 (after S-67 repair) | 210 |
| P17 | 6.1 Analytical closure of the sizing loo | S10 | S7 | R1 | 208 |
| P18 | 6.1 Analytical closure of the sizing loo | S10 | S7 | R1 | 208 |
| P19 | 6.2 The ledger | S11 | S8 | R1 | 210 |
| P20 | 6.2 The ledger | S11 | S8 | R1 | 210 |
| P21 | 6.2 The ledger | S11 | S8 | R1 | 210 |
| P22 | 6.2 The ledger | S11 | S8 | R1 (after Q-210 sentence) | 213 |
| P23 | 6.2 The ledger | S14 | S11 | R1 | 213 |
| P24 | 6.3 Scale does not lock two of the charg | S12 | S9 | R1 | 211 |
| P25 | 6.3 Scale does not lock two of the charg | S12 | S9 | R1 | 211 |
| P26 | 6.4 Rankings belong to contracts | S13 | S10 | R1 | 212 |
| P27 | 6.4 Rankings belong to contracts | S13 | S10 | R1 | 212 |
| P28 | 6.4 Rankings belong to contracts | S13 | S10 | R1 | 212 |
| P29 | 6.4 Rankings belong to contracts | S13 | S10 | R1 | 212 |
| P30 | 6.4 Rankings belong to contracts | S13 | S10 | R1 | 212 |
| P31 | First, the known obstacle: the energy st | S14 | S11 | R1 | 213 |
| P32 | First, the known obstacle: the energy st | S14 | S11 | R1 | 213 |
| P33 | Then what is not known | S14 | S11 | R1 | 213 |
| P34 | What the claims that remain amount to | S14 | S11 | R1 | 213 |

**All 34 are R1.** Three reached R1 only after a body repair the readers found while grading: P14 (S-66, the fairing sentence),
P16 (S-67, the loop sentence) and P22 (Q-210, the sentence added after the protected Bill 3 sentence).

---

## C. The final whole-body check

This is the checkpoint the author agreed to: one reading of the whole body against the complete supplement before the package goes to the author. **Please report defects only.** For each one, quote the sentence and name the section. Improvements that are not defects go in §D and do not block submission.

**Please check:**
1. **Contradiction.** Does any supplement passage contradict the body, or another supplement passage, in a number, a unit, an object, an operating state or a scope?
2. **The three repairs.** P14, P16 and P22 changed body sentences after other text was written. Does any other sentence of the body or the supplement still say what the old sentences said? The old sentences:
   - *"less than a 20 mm faired strut carries in any case"*;
   - *"take-off mass the hover power that sizes the installed power"*;
   - and the absence of the hover-rated-mass limit.
3. **The claims.** Read against the four axes (onboarding §2), does anything in the supplement claim more than the body does? Look in particular at:
   - range, which is claimed against rotorcraft only;
   - mechanism, which is a count, not simplicity or reliability;
   - the tilting layout, which is a bound, not a ranking.
4. **A referee's first reading.** Is there anything that would stop a referee in the first pass, such as a broken pointer, an undefined symbol, or a table that does not say what its rows are?

---

## D. Your own proposals

Open, as always. **Proposals that are not defects are recorded for after submission and do not block it.**

---

## E. Errors (one list)

- **Claude:** my supplement source had one comment nested inside another, and the generator's first build printed its tail (*"notunda. –>"*) on page 1. I caught it by reading the output and corrected it.
- **Claude:** a string-quoting slip in the generator dropped the closing quotation marks in the supplement's opening sentence. Caught the same way and corrected.
- **Readers:** none found in Round 213.

---

## F. What goes to the author

**After this round, the package goes to the author for the submission decision.** The package:
- the body PDF;
- the supplement PDF;
- the references (26);
- the AI-use sentence (E31);
- the receipt table.

Anything you report as a defect is repaired first.
