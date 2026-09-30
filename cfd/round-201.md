# Round 201 — The submission package: the mechanical build, and what it adds that you must check

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`5b7828d`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text.

---

## A. What the author decided, and what was built

**The author (E31):** *"(b) approved; move to the submission package"* (my translation). The AI-use sentence is final, with *"and solution approach"*.

**Built this round:** `paper/build/submission_build.py`.
- It reads the assembled view of the fifteen step sources and writes one LaTeX manuscript, `paper/submission/latex/meryemaircraft.tex`, which compiles to a 34-page PDF.
- **It changes no step source.** Every change it makes is listed in `paper/submission/build-report.md`.

**The class.** AIAA's journal class `new-aiaa.cls` is distributed through Overleaf. It is not in the TeX Live archive this environment can reach. The build uses it if the file is present. Otherwise it falls back to an equivalent layout: Times, 10 pt, single column, double spaced, centred bold Roman-numeral section heads, lettered subheads, italic numbered sub-subheads, and table captions above.

**What the build does, mechanically:**

1. **Sections.** Sections become Roman numerals, numbered subsections become letters, and every pointer changes form: *"Section 6.1"* → *"Sec. VI.A"*, *"Sections 5.1 and 5.2"* → *"Secs. V.A and V.B"*. At a sentence start the word stays *"Section"*. The map: 1 → I; 2 → II, with 2.1–2.3 → II.A–II.C; 3 → III; 4 → IV; 5 → V, with 5.1–5.2 → V.A–V.B; 6 → VI, with 6.1–6.4 → VI.A–VI.D; 7 → VII; 8 → VIII. That is 121 pointers. The build stops if any pointer does not resolve.
2. **Headings** are converted to title case (79 of them).
3. **Bold emphasis is removed.** Quotations lose their italics and keep their quotation marks.
4. **Lists** become *1) 2) 3)*.
5. **Spelling is converted to American**: take-off → takeoff (27); favourable → favorable (7); modelled → modeled (5); aeroplane → airplane (2); centre → center (2); optimised → optimized (2); favour → favor (2); favours → favors (2); characterisation → characterization (1); maximise → maximize (1); analyses (verb) → analyzes (1); centreline → centerline (1); analysed → analyzed (1); idealisation → idealization (1); idealised → idealized (1).
6. **Numbers.** Thin-space thousands become *1200* and *12,000*: · 1 200 → 1200 · 7 271 → 7271 · 6 584 → 6584 · 1 742 → 1742 · 7 221 → 7221 · 3 678 → 3678 · 1 000 → 1000 · 1 002 → 1002 · 1 141 → 1141 · 1 233 → 1233 · 1 000 → 1000 · 1 000 → 1000 · 1 000 → 1000 · 1 233 → 1233. In addition, *"13 %"* becomes *"13%"* (12 places).
7. **Equations.** Two display equations are numbered: the power ratio in II.A, and *(L/D)e = WV/P = (L/D) ηp* in IV. The mass relation and four short relations stay inline.
8. **Citations and E1.** Citation markers are placed from the placement table of Round 194. E1 is applied as agreed in Round 195.
9. **Acknowledgments** carries the E31 sentence. The **reference list** has 26 entries, from `references-draft.md`.

**The output check.** The generator compares the output's word sequence with the source's, after undoing the listed changes. **17 residual differences remain, and all are notation:**
- list numbers moved into the list environment (4);
- *L/De* written as *(L/D)e* (7);
- the drag polar's *C_L²* written in math (1);
- exponents written as superscripts (4);
- *5,000* inside the quoted NASA mission, which the check normalises (1).

No word is lost or added outside the listed changes.

**Length, measured on the output:**
- **prose 14,057 words**;
- six tables, 741 words of cells, which count by AIAA's rule as about 2,000 to 2,700 equivalent words (200, 450 or 700 per table, depending on the width each needs in the journal's layout);
- the abstract, 199 words.

The total is about **16,300 to 17,000**, against the recommended 10,000–12,000. The author decided in E25 to submit at this length.

---

## B. What the build ADDS: please check each one

These are the only places where the output carries words the step sources do not.

### B1. Table captions (new text; tables had none)

| Table | Where | Proposed caption |
|---|---|---|
| 1 | II.A, the remedies table | Known partial remedies and the charges they move |
| 2 | IV, the L/De corners | Effective lift-to-drag ratio at the corners of the drag and propeller-efficiency brackets |
| 3 | IV, against the quadrotors | Effective lift-to-drag ratio against the two published quadrotors |
| 4 | V.A, mechanism classes | Mechanism classes that change regime or remove a rotor from one regime's flow |
| 5 | VI.A, the closures | The four closures of the sizing loop, 50 kg design |
| 6 | VIII, the axes | The four claim axes and their opponents |

**B1:** does any caption say more than its table, or name it wrongly? Table 6 is the axis table, and two of its four rows are *"not claimed"*, so check that *"claim axes"* does not overstate.

### B2. Table references (AIAA: every table numbered and cited in the text)

| Source | Output |
|---|---|
| The table is not a census of the field | Table 1 is not a census of the field |
| and the table above is where one would appear | and Table 1 is where one would appear |
| derived by inverting the table, | derived by inverting Table 1, |
| a design variable this study has not fixed. | a design variable this study has not fixed (Table 2). |
| The sizing set contains two quadrotors for the same mission, | The sizing set contains two quadrotors for the same mission (Table 3), |
| this table alone does not establish | Table 3 alone does not establish |
| The table counts the mechanism classes | Table 4 counts the mechanism classes |
| On these assumptions all four converge | On these assumptions all four converge (Table 5) |
| this paper's alternatives differ from axis to axis. | this paper's alternatives differ from axis to axis (Table 6). |

The heading *"Inverting the table"* is left as it is (a heading does not cite a table). **B2:** is each reference placed where its table is first used?

### B3. Citation markers (36): the words immediately before each marker

- `ng was curtailed because of engine and gear-box reliability problems"*` + [1]
- `has been exploiting exactly those three for over a decade` + [2]
- `have been built and flown for more than a decade` + [2,3]
- `A tail-sitter study reported in 2007` + [4]
- `Attitude without aerodynamic control surfaces is established` + [3]
- `at a cost its proposers name as added mechanical complexity` + [5]
- `a tail-sitting micro air vehicle reported in 2014` + [6]
- `for three-axis control in hover` + [6]
- `a flying-wing tail-sitter reported in 2018` + [7]
- `A coaxial contra-rotating tail-sitter reported in 2012` + [8]
- `aimed at disaster response, is established, reported in 2025` + [9]
- `a 2026 study of 100 kg winged biplane tail-sitters` + [10]
- `a long-endurance concept reported in 2025` + [11]
- `impossible to be very efficient in both hovering and forward flight."*` + [2]
- `A long-range tail-sitter reported in 2018` + [2]
- `Tail-sitting aircraft are seventy years old` + [1]
- `a standing subject of transport research for more than three decades` + [12]
- `series-hybrid propulsion has been designed for small uncrewed aircraft` + [13]
- `the drag produced by the motors is significant."*` + [14]
- `edicts higher lift and lower drag than were experimentally observed."*` + [15]
- `One of these transfers has direct experimental support` + [14]
- `The check uses a NASA study` + [16]
- `Reviewing the tail-sitters of the 1950s, NASA recorded` + [17]
- `The landing difficulty of the 1950s tail-sitters was attributed` + [17]
- `surveying the field, one study concludes` + [18]
- `The sizing set of Section 2.3 reports` + [16]
- `The source writes hover power` + [16]
- `5,000-ft altitude and ISA + 20°C"*` + [16]
- `at the same place, the highest of them against wind-tunnel measurement` + [21,22]
- `studies of a winged tail-sitter (Section 1)` + [10]
- `a single-aisle airliner reported in 2016` + [23]
- `sized against the criterion the tailless literature recommends` + [24]
- `on section polars computed rather than measured` + [19]
- `transferred from a different airframe's wind-tunnel campaign` + [14]
- `A pack flown in a 210 kg-class electric VTOL aircraft` + [25]
- `A NASA-funded design study adopts 4 kW per kilogram` + [26]

**The E1 tool names are inserted at IV:**
- *"… from blade-element momentum theory, with section polars from NeuralFoil 0.3.3 [19], at two operating points …"*
- *"… from a vortex-lattice solution (AeroSandbox 4.2.10 [20]) of the trimmed planform."*

**B3, please check:**
- Does each marker sit on the claim its source supports?
- Two markers deserve a look:
  - **[2] after *"for over a decade"*.** DelftaCopter is 2018. Is it the right witness for a decade of literature, or should it be [2, 3]?
  - **[6] repeated on the 2014 vehicle's elevon sentence.** Should it be kept, or dropped because the vehicle was cited in the previous sentence?

### B4. Title case

Examples:
- *"What the Condition Does Not Say, and This Matters More than What It Says"*;
- *"Bill 1 — Mass"*;
- *"Against Lift-Plus-Cruise: A Trade, and the Contract Sets the Exchange Rate"*.

Small words (articles, short prepositions, conjunctions) stay lower case, except first, last and after a colon. **B4:** any objection to the rule?

---

## C. The style pass: now, or leave it to copy-editing? (a proposal, please vote)

AIAA asks authors to avoid dashes and *"above"* and *"below"*, and discourages italics for emphasis. The build leaves these untouched and lists them:
- **dashes in 74 sentences**;
- ***above* or *below* in 17 sentences**;
- **8 italic spans**: every; one orientation relative to the airframe; Cruise thrust in this paper means the thrust that balances cruise drag.; Note.; (This paper fixes body-axis naming throughout. That axis is the roll axis in bot; size; class of mechanism; sizes.

**My proposal:**
- **Do it before submission, as a rule-based pass that the generator applies**, with every sentence shown before and after in the next round:
  - a pair of dashes becomes parentheses, or commas where the inserted clause is short;
  - a single dash becomes a colon or a semicolon;
  - *above* and *below* become *preceding*, *following*, or a table or section reference;
  - emphasis italics are removed, except the two definitions (*"Cruise thrust in this paper means …"*, and the body-axis note), which become plain sentences.
- **Reason:** the change is mechanical in form, but a dash sometimes carries a qualifier. Seeing each sentence is the only way to know that no qualifier's scope moved.
- **The alternative is to leave it to AIAA's copy-editors.** That is cheaper now, but costs a referee's first impression.

**C, everyone:** now or later? If now, any rule you would change?

---

## D. The journal supplement: the next build (a proposal)

The body points to *Supplement S2*–*S14* 34 times. `paper/v8/supplement.md` holds two things:
1. **the journal supplement** (the working of each section);
2. **the repository audit archive** (every frozen snapshot, *"as it stood before …"*).

**Proposal:**
- A second generator writes the journal supplement from the first part only, keeping the S-numbers the body uses.
- A receipt check confirms that every body pointer's promised content is in it (the Round 130 receipt rule).
- The audit archive stays in the repository and on Zenodo.

**D:** agree, or name what should differ.

---

## E. Nomenclature (optional in AIAA)

A nomenclature list is optional. If used, it must hold every symbol, and definitions are not repeated in the text. The body defines its symbols where they appear.

**My view: no nomenclature.** It would add words, and the definitions in the text would then have to go. **E:** your view.

---

## F. Your own proposals

Open, as always.

---

## G. Errors (one list)

- **None found in the Round 200 answers.**
- **Claude:** none found by the readers.

---

## H. What goes to the author

- **Optional:** AIAA's `new-aiaa.cls`. If the author downloads the AIAA template from Overleaf (*"Download as zip"*) and uploads that one file, the build switches to the official class automatically.
- **Nothing else now.** The style pass (C) and the supplement (D) follow your votes.
