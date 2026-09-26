# v8 — the body's objects: five tables, four figures (draft, Round 101)

**The author's decision (Round 101):** *"Önerine göre git."* The length plan is Claude's reconciled budget:
- 12 000 words in all, text and objects together;
- 5 tables (1 750) and 4 figures (1 300), 3 050 in all;
- 8 500 words of prose, and 400 for the abstract and nomenclature.

These are drafts for the readers' vote. Nothing below has entered the step files yet.

Word equivalents follow `paper/v8-budget.md`: single column 200, double column 450, large double 700. Section numbers in
these drafts are the **assembled** numbers (Section 4 = Step 6, Section 7.4 = Step 13); in the step files they are converted.

---

## Tables

### T1 — The four axes (double column, 450) · from Step 9's table; Step 15 points to it

| Axis | Opponent | Status |
|---|---|---|
| Cruise efficiency | Rotorcraft: multirotors and helicopters | **Claimed against multirotors, and bounded; against helicopters the published comparison is mixed and no advantage is claimed.** Cruise lift is carried on a surface rather than on rotors, which no sizing contract changes; the size of the advantage is a calculation (Section 4). |
| Operation without a runway | Fixed-wing aircraft | **Claimed as sized, not demonstrated** (Sections 3, 8). |
| The mechanism required to change regime | Tilting architectures | **Claimed. This is the paper's contribution** — a count of mechanism classes (Table 2), not a claim of simplicity or reliability. |
| Cruise efficiency and range | Other hybrids — lift-plus-cruise, tilt | **Not claimed, in either direction** (Section 7.4). |

*Changes against Step 9's table, all to vote:*
- The first row drops *"and Section 6 measures it against two published quadrotors in one common definition"*. Figure 3
  and Section 4 carry that.
- The second row takes Step 15's *"as sized, not demonstrated"* in place of *"in the sense stated below"*.
- The third row takes the count/simplicity limit from Step 15.

The protected Step 9 row sentence is kept word for word.

### T2 — The mechanism classes (single column, 200) · Step 7's table and note, unchanged

Step 7's table as it stands, with the stopping row reading *"— (see note)"* and the note directly under it.

### T3 — Remedies and where their cost goes (double column, 450) · Step 2's table, unchanged

Step 2's table as it stands (six rows).

### T4 — The four closures (double column, 450) · merges Step 10's closure table and Step 6's L/De corner table

| Closure | C_D0 | η_p | L/D | L/De | MTOW | Empty fraction | Hover power, rotor shaft | Engine rating, shaft | Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** | 0.0381 | 0.632 | 8.79 | 5.56 | 57.5 kg | 0.614 | 12.53 kW | 5.17 kW | 927 km |
| **B** | 0.0381 | 0.683 | 8.79 | 6.00 | 55.8 kg | 0.607 | 12.17 kW | 4.65 kW | 1 002 km |
| **C** | 0.0285 | 0.632 | 10.82 | 6.84 | 53.5 kg | 0.597 | 11.66 kW | 3.91 kW | 1 141 km |
| **D** | 0.0285 | 0.683 | 10.82 | 7.39 | 52.3 kg | 0.592 | 11.40 kW | 3.54 kW | 1 233 km |

- The L/De column is L/D × η_p, the values of Step 6's corner table: 8.79 × 0.632 = 5.56, 8.79 × 0.683 = 6.00,
  10.82 × 0.632 = 6.84, 10.82 × 0.683 = 7.39. The two tables were already indexed by the same four closures.
- The only new column is L/De. **Step 6's protected *"These are the bounding corners of a product, not four simulated
  aircraft"* now speaks of the L/De column of a table whose other columns are closed aircraft.** Is that a tension? The L/De
  of a closure is the corner value, because the closure carries the same L/D and η_p. But the protected sentence was
  written about the 2×2 product alone. To vote.

### T5 — The sizing contracts (single column, 200) · Step 13's table, relabelled to the closures

Range of the lift-plus-cruise layout relative to this configuration:

| Closure | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass |
|---|---:|---:|---:|
| A | +67.8 % | +40.2 % | +1.1 % |
| B | +55.3 % | +27.5 % | **−13.0 %** |
| C | +83.9 % | +53.5 % | +7.3 % |
| D | +70.2 % | +40.1 % | **−6.5 %** |

The only change is the row labels: "Adverse drag, lower blade family" becomes A, and so on. They match T4.

### To the supplement, with the body carrying the result in words

- **Step 6's comparison with the published rotorcraft:** carried by Figure 3 and by the sentences of Section 4.
- **Step 14's re-closure on a measured store:** two sentences in Section 8.

---

## Figures

| # | What | Source | Width | Status |
|---|---|---|---|---|
| F1 | The configuration in hover and in cruise, with the body axes named | v7 `fig05-three-views` / `fig06-general-view` (rendered images; their labels cannot be scanned as text) | double, 450 | **the author to look at**; axis names must follow Step 8's body-axis convention |
| F2 | Tip frames, moment arms and the strip | v7 `fig08-moment-arms` + `fig09-strip-slipstream` | double, 450 | **fig08 carries a forbidden label** — see below |
| F3 | Effective L/De: closures A–D against the published rotorcraft and hybrids | **new draft**: `figures/build/mkfig_v8_f3.py` → `figures/output/v8-draft-f3-effective-LD.png` | single, 200 | drafted from verified numbers only (Step 6 corners; Johnson & Silva Table 3) |
| F4 | The transition | v7 `fig12a-transition-rotation-time` | single, 200 | **fig12a plots the wrong model** — see below |

**Two findings from auditing the v7 figures (the rule of Round 68: a figure is text).**
- **fig08, the roll label.** It reads *"M_x = y F_z − z F_y = 0 identically, at every thrust setting"*. This is the thrust-only
  statement **without** the reaction-torque qualifier. It is the figure-level form of what the P56 check forbids in text.
  If F2 uses fig08, the label must add the declined channel (for example *"from thrust; reaction torque could, and is
  declined"*). The P56 check does not scan figures.
- **fig12a, the transition.** It plots `transition2.sim`, the point-mass model with the body angle driven kinematically:
  Step 10's **first** model, which Step 10 calls *"kinematically favourable"*. Step 10's verdict rests on the **second**
  model, the finite-moment one (5.4 m altitude loss). Putting fig12a in the body would put the model the text subordinates
  in front of the reader. So either a new figure from the finite-moment model, or F4 goes to the supplement (Grok's
  proposal) and the body keeps the 5.4 m in words.

**F3 caption (draft, 21 words):** *"Effective lift-to-drag ratio, L/De = WV/P: this configuration's four closures (shaded) against the published
rotorcraft and hybrids of one sizing study."*

---

## Budget check

| | Words |
|---|---:|
| T1 450 + T2 200 + T3 450 + T4 450 + T5 200 | 1 750 |
| F1 450 + F2 450 + F3 200 + F4 200 | 1 300 |
| Prose (by section, E6) | 8 500 |
| Abstract and nomenclature | 400 |
| **Total** | **11 950** |

If F4 goes to the supplement, the total is 11 750.
