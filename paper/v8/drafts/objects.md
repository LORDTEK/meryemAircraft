# v8 — the body's objects: five tables, three figures (Round 101 drafts; Round 101 votes applied in Round 102)

**Round 101 votes, all eight unanimous (four readers + Claude):** T1, T4 with a footnote, T5, fig08's roll label and the
figure scan, F4 to the supplement, R-7, the Step 7 note protected, the governing sentence. **Applied in the step files:**
T1 → Step 9's table; T4 → Step 10's table (L/De column + footnote); T5 → Step 13's row labels. **Budget: 5 tables (1 750) +
3 figures (1 100) + prose 8 500 + abstract/nomenclature 400 = 11 750.**

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
| F1 | The configuration | v7 `fig05-three-views` (`figures/build/mkfig.py`) | double, 450 | **the author's information (Round 102):** (a) top view, planform; (b) front view; (c) side view, section; 2 m scale bar. fig06 (general view, 1 m bar) is the other candidate. **Proposal: F1 = fig05; fig06 to the supplement.** See below |
| F2 | Tip frames, moment arms and the strip | v8 drafts `mkfig_v8_f2a.py` (from fig08) + `mkfig_v8_f2b.py` (from fig09) → `figures/output/v8-draft-f2a-moment-arms.png`, `v8-draft-f2b-strip-slipstream.png` | double, 450 | roll label repaired (voted); **fig09 contradicts Step 8** — see below |
| F3 | Effective L/De: closures A–D against the published rotorcraft and hybrids | **new draft**: `figures/build/mkfig_v8_f3.py` → `figures/output/v8-draft-f3-effective-LD.png` | single, 200 | drafted from verified numbers only (Step 6 corners; Johnson & Silva Table 3) |
| ~~F4~~ | The transition | v7 `fig12a-transition-rotation-time` | — | **to the supplement (Round 101, unanimous)**; the body keeps 5.4 m in words |

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
| F1 450 + F2 450 + F3 200 (F4 to the supplement) | 1 100 |
| Prose (by section, E6) | 8 500 |
| Abstract and nomenclature | 400 |
| **Total** | **11 750** |

---

## Round 102 — the figure audit continued (a figure is text)

**F2a (from fig08).** The roll line now reads *"M_x = 0 from thrust at every setting; reaction torque could produce it, and is
declined"* (voted). v7's fig08 is untouched: it is the published record. The v8 figure is a copy with that one change.

**F2b (from fig09) — a contradiction with the body, found this round.** fig09's note reads *"The strip is on the lower surface,
inclined at 45°, and **deploys on–off**."* Step 8 says: *"**Extension is the control variable** — the strip is modulated, not
switched."* The v8 copy reads *"…inclined at 45°, and its extension is modulated, not switched."* — Step 8's words. To confirm.
"deploys on–off" is added to the retired phrases, so the figure scan now catches it.

**Other figure findings, to vote:**
- **Numbers on F2 that the body does not carry.** fig08: *2TL_p = 23.0 N m* and *2TL_y = 55.9 N m* (tip-pair thrust 16.2 N ×
  the arms; 16.2 N sits only in Step 8's audit table). fig09: *q = T/A = 433 Pa* and *slipstream boundary 0.67 m → 0.47 m*.
  Under the number-match check, each must be in the body or in the supplement working. Proposal: remove the two moments
  from F2a (the body gives the arms and their ratio, 2.43, which is what the figure is for); put 433 Pa and the slipstream
  contraction in S8's working.
- **Names.** fig08 says *"thrust pair (all propulsion)"* and *"control pairs"*; fig09 says *"main propeller"*. Step 8 says *nose
  pair* and *tip pairs*. Proposal: the figures take Step 8's names.
- **Titles.** fig08 and fig09 carry titles; F3 has none. A journal figure carries a caption. Proposal: titles go, captions carry
  the words.
- **Not checked:** fig09 draws the planform from its own sweep parameters (35° at the tip); Step 8 gives the realised sweep as
  45° at the root to 38.3° at the tip. It is a schematic, but I have not verified that it is a faithful one.

**F1 (from fig05).** The author's information: three panels — (a) top view, planform; (b) front view; (c) side view, section — and
a 2 m scale bar; fig06 is a general view with a 1 m bar. I looked at both. fig05 carries only the panel names and the bar.
- It is the **50 kg reference design** (span 3.453 m). The closures run 3.53 to 3.70 m. The caption must say "reference design".
- It shows the cruise attitude only. The paper's idea is that the same airframe stands nose-up in hover.
- It names no body axes. The original F1 plan asked for them (Step 8's convention).

Proposal: **F1 = fig05; fig06 to the supplement.** Draft caption (24 words): *"The 50 kg reference design: (a) top view,
planform; (b) front view; (c) side view, section. In hover the same airframe stands nose-up."* The body axes are either
named in the caption or drawn on panel (c) — to vote. Adding arrows means re-rendering fig05.

**New proposals from Round 101, to vote:**
- Qwen P1: T4's caption names L/De's status (*"L/De is the product L/D × η_p at the cruise condition, an input, not a closure
  output"*).
- Qwen P2: `v8_outbound.py` is run for every calculation step before it is drafted. **Done for Steps 11–14 this round**
  (`drafts/11-…14-outbound-map.md`); the proposal is to make it a rule.
- Qwen P3: Figure 3's data table (the nine Table 3 entries and the four closures) in the supplement.
- Grok P70: F3's points are Table 3 only; a point from any other source is a new source-opening, not a caption edit.
- ChatGPT: *"A number may move to the supplement; its meaning may not."* And a number's identity is value + unit + object +
  **model or geometry where it applies**.
