# Round 101 — The author decided: the length plan goes ahead. Drafts of the five tables and four figures, the map of Step 10's outbound numbers, two figure findings, and an error of mine in Step 15

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> New in the repository:
> - `paper/v8/drafts/objects.md` — the five tables and four figures;
> - `paper/v8/drafts/10-outbound-map.md` — Step 10's outbound numbers;
> - `figures/output/v8-draft-f3-effective-LD.png` — the Figure 3 draft, described in §3;
> - `paper/build/v8_outbound.py`.
>
> As always, answer one another as well as me.

---

## 1. The author's decision

Your Round 100 answers were put to the author side by side. The author replied: *"Go with your proposal."* That is my
reconciled plan, built from your answers, and it is now a project rule:

| | Decided |
|---|---|
| Target | **12 000 words in all**, text, tables and figures together |
| Objects | **5 tables** (1 750) and **4 figures** (1 300) |
| Prose | **8 500 words**, plus 400 for the abstract and nomenclature. Total 11 950 |
| Section budgets | 1: 850 · 2.1: 750 · 2.2: 650 · 2.3: 350 · 3: 600 · 4: 850 · **5.1: 900** · 5.2/6.1: 900 · 6.2: 400 · 7.1–7.4: **1 550** · 8: 450 · 9: 250 |
| Result sentences | the method is always named; a limit is written only where one really applies; a supplement pointer; no rigid template |
| Interpretability | ChatGPT's body-only interpretability rule is adopted |
| Supplement | split in two: a clean journal supplement, and the frozen audit snapshots kept in the repository only |
| Order | objects → map of Step 10's outbound numbers → calculations (10–14) → framework (2–4) → architecture (1, 5–9, 15) last, frozen meanwhile |
| New check | every body number is matched to the supplement working by value, unit and object; a script flags, a person reads |
| If room runs short | F4 goes to the supplement first (Grok) |

Where you differed, this took the majority:
- **Calculations** get 1 550, not my 1 250. You were right that 729 protected words left too little.
- **Step 8** gets 900.
- **Contracts** get their own small table (ChatGPT, Qwen), not DeepSeek's divided single table.
- **Four axes** stay a table (Grok, ChatGPT, Qwen).
- **Four figures** stay (ChatGPT, DeepSeek, Qwen).

Round 100's applied text is confirmed by all four of you and is closed.

---

## 2. The five tables — drafts, to vote

- **T1, the four axes (double column).** Step 9's table; Step 15 points to it. Three changes, all to vote:
  - Row 1 drops *"Section 6 measures it against two published quadrotors"*, which Figure 3 now carries.
  - Row 2 takes Step 15's *"as sized, not demonstrated"*.
  - Row 3 takes Step 15's count/simplicity limit.

  The protected Step 9 row sentence is unchanged.
- **T2, the mechanism classes (single column).** Step 7's table and note, unchanged.
- **T3, remedies and where their cost goes (double column).** Step 2's table, unchanged.
- **T4, the four closures (double column).** Step 10's closure table with one new column, **L/De**. That column holds the
  values of Step 6's corner table, which drops out of the body.

  | Closure | C_D0 | η_p | L/D | **L/De** | MTOW | Empty fraction | Hover power, rotor shaft | Engine rating, shaft | Range |
  |---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
  | **A** | 0.0381 | 0.632 | 8.79 | **5.56** | 57.5 kg | 0.614 | 12.53 kW | 5.17 kW | 927 km |
  | **B** | 0.0381 | 0.683 | 8.79 | **6.00** | 55.8 kg | 0.607 | 12.17 kW | 4.65 kW | 1 002 km |
  | **C** | 0.0285 | 0.632 | 10.82 | **6.84** | 53.5 kg | 0.597 | 11.66 kW | 3.91 kW | 1 141 km |
  | **D** | 0.0285 | 0.683 | 10.82 | **7.39** | 52.3 kg | 0.592 | 11.40 kW | 3.54 kW | 1 233 km |

  **A question I cannot settle alone.** Step 6's protected sentence reads *"These are the bounding corners of a product, not
  four simulated aircraft."* In T4 the same four values sit beside four closed aircraft. Each closure carries its own L/D and
  η_p, so its L/De is that corner value. But the protected sentence was written about the bare 2×2 product. Does T4 need a
  footnote that keeps the sentence true: *"L/De = L/D × η_p at the cruise condition; the closure changes neither"*? Or does
  the move break the sentence, so that the corner table must stay in Section 4?
- **T5, the contracts (single column).** Step 13's table. The only change is the row labels, which become A–D to match T4.
  The caption line stays: *"Range of the lift-plus-cruise layout relative to this configuration"*.

**To the supplement, with the result kept in words:**
- Step 6's comparison with the published rotorcraft. Figure 3 and Section 4's sentences carry it.
- Step 14's re-closure on a measured store. Two sentences in Section 8.

---

## 3. The four figures — and two findings from auditing v7's

Our rule since Round 68 is that a figure is text: its labels are checked against the retired phrases and the protected
limits before it enters. I checked the v7 figure scripts.

| # | What | Source | Finding |
|---|---|---|---|
| F1 | The configuration in hover and in cruise, body axes named | v7 three-view / general view (rendered images) | the author will look; the axis names must follow Step 8's body-axis convention |
| F2 | Tip frames, moment arms, the strip | v7 `fig08` + `fig09` | **fig08 carries a forbidden label** |
| F3 | Effective L/De: closures A–D against the published designs | **new draft**, from verified numbers only | see below |
| F4 | The transition | v7 `fig12a` | **fig12a plots the wrong model** |

**fig08.** The roll line reads *"M_x = y F_z − z F_y = 0 identically, at every thrust setting"*. That is the thrust-only
statement **without** the declined reaction-torque channel. In text, the P56 check forbids exactly this. The check does not
scan figures.
- Proposal: if F2 uses fig08, the line becomes *"M_x = 0 from thrust at every setting; reaction torque could produce it,
  and is declined"*.
- Should the P56 check be extended to the figure scripts?

**fig12a.** It plots the point-mass model with the body angle imposed kinematically, which Step 10 calls **the first model,
*"kinematically favourable"***. Step 10's verdict rests on the **second**, finite-moment model: 5.4 m of altitude loss. Put
in the body, fig12a would show the model the text puts second.

The options are:
- (a) a new figure from the finite-moment model;
- (b) F4 goes to the supplement and the body keeps the 5.4 m in words (Grok's proposal). This also frees 200 words.

**My view: (b).** The transition is the claim the paper does not make. Its figure belongs with its working.

**F3, the new draft**, since you cannot see the image:
- A horizontal scale of L/De from 4.5 to 9.
- A shaded band for this configuration, with the four closures marked A–D at 5.56, 6.00, 6.84 and 7.39.
- Nine points from the NASA study's Table 3, coloured by family:
  - quadrotors: 4.9 and 5.8;
  - helicopters: single main rotor 5.4 and 6.0, side-by-side 5.9 and 7.2;
  - hybrids: lift-plus-cruise 8.5 and 7.9, tilt-wing 8.6.

Draft caption (21 words): *"Effective lift-to-drag ratio, L/De = WV/P: this configuration's four closures (shaded) against the published
rotorcraft and hybrids of one sizing study."*

It shows at a glance the multirotor claim, the mixed helicopter result, and the hybrids above the whole envelope. It has no
title and no claim of its own.

---

## 4. Step 10's outbound numbers (Grok's warning, now a map)

`v8_outbound.py 10` finds **21 numbers** of Step 10 that also appear in another step. Each is listed with its context in
Step 10 and in each other step. Its self-test finds 52.3 → Step 14.

**Five are coincidences, and they show why a person must read the map:**
- **11.66** is a hover power in kW in Step 10, and lift-plus-cruise's L/D in Step 13.
- **5.4** is an altitude loss in metres in Step 10, but in Step 6 it is a helicopter's L/De, and in Step 13 a percentage.
- **17** is 17 m of altitude in Step 10, and an L/D of about 17 in Step 13.
- **1.5** is an exponent (MTOW^1.5) in Step 10, and 1.5 kW per kilogram in Step 14.
- **2.4** is a mass-variation ratio in Step 10, and a power ratio in Steps 11 and 12.

The real dependencies:
- the drag bracket (0.0285, 0.0381) → Step 11;
- η_p (0.632, 0.683) → Steps 6, 11 and 13;
- the L/D pair (8.79, 10.82) → Steps 6, 11 and 13;
- the masses (52.3–57.5) → Steps 6 and 14;
- the ranges (927, 1 233) → Step 14;
- 1.979 m² → Step 8;
- 5.1 s → Step 12.

**Rule for the calculation work that follows:** any of these that leaves Step 10's body for the supplement stays in T4, or
the dependent step carries its own reason for the number, or it points to T4.

---

## 5. My error — R-7, found while drafting T1

Step 15 still reads: *"…carries none of the mechanism classes Section 7 counts: no pivot, no nacelle or rotor-group actuator,
no variable-pitch hub, no dedicated lift rotors, **and no rotor stowing, indexing or stopping mechanism.**"*

The S-33 condition went into Steps 7 and 8 and into the onboarding text, but **not into Step 15**. That breaks the
conditional-inventory rule we adopted in Round 99. Grok's retired phrase *"no stopping mechanism"* did not catch it, because
the sentence words it differently.

Repair, to vote:
> *"…no dedicated lift rotors, and — while the tip pairs free-wheel or are held by motor torque — no rotor stowing, indexing
> or stopping mechanism (Section 7's note)."*

The unconditional form is added to the retired phrases. The protected Step 15 sentence (*"This is a count of mechanism
classes, …"*) is not touched.

---

## 6. To vote

| # | Item | Who | My vote |
|---|---|---|---|
| a | T1 as drafted (three changes) | me | yes |
| b | T4, and whether it needs the footnote under Step 6's protected corner sentence | me | yes, with the footnote |
| c | T5 with A–D labels | me | yes |
| d | fig08's roll label reworded; extend the P56 check to the figure scripts | me | yes |
| e | F4: (a) a new finite-moment figure, or (b) to the supplement | Grok (b) | (b) |
| f | R-7 repair in Step 15 | me | yes |
| g | Protect the Step 7 note | DeepSeek | yes — the count is the contribution, and the condition must not drop |
| h | ChatGPT's governing sentence as the rule of this phase: *"Move the working, not the evidence; move the derivation, not the qualification; move the audit trail, not the result."* | ChatGPT | yes |

---

## 7. The next step, and a question for each of you

The next work is **Step 10 as result sentences**, within 1 550 words for Steps 10–13 together. Before I draft, please give
your own list:
- **which findings of Step 10 must stay in the body**, as findings, not wording;
- **which may go to the supplement.**

I will put your lists side by side with mine and draft from the common part.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
