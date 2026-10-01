# Round 203 — Splits from the style pass, and the journal supplement: what the archive holds and how to build it

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text.

---

## A. The author's decisions (E33)

The author answered Round 202 §H: *"1 and 2 yes, go on"* (my translation).
1. **Format-only changes are allowed in protected sentences** in the submission output: punctuation, American spelling, and the removal of italics.
   - The step sources do not change.
   - **ChatGPT's condition is adopted as the rule:** *"format normalization may not be used to alter wording, clause boundaries, or qualifier scope."* A punctuation change that moves an attachment is not format-only.
2. **A02 is approved.** *"the origin of all three charges below"* becomes *"… that follow"*.

---

## B. Closed in Round 202 (all four, and me)

| Item | Result |
|---|---|
| Figure 1 | Caption, placement and two-blade rendering accepted by all four. First citation stays in Sec. III. Grok's optional addition (*"nose disks shown as circles"*) was not taken up by the others. I would leave the caption as it is; say so if you want it |
| Table 6 caption | **"The four axes and their opponents"**: all five (DeepSeek and Qwen moved). Applied |
| [2] for *"over a decade"* | **[2, 3]**: all five (Grok accepted). Applied |
| [6] on the elevon sentence | **Kept**: all five (Qwen yielded) |
| Style pass | Every row accepted by all four except the five in §C |
| Qwen: A04, A05, A14 are protected | **Checked: they are not.** None of *"first failure mode below"*, *"mission used below"*, *"as fixed above"* is in the protected register. No author decision is needed |

---

## C. Five style rows still split: please answer each other

| Row | Proposal | Positions | My view |
|---|---|---|---|
| **D33** | *"… at the semi-span, 1.726 m: 2.43 times the pitch arm, a consequence of the layout rather than a design choice."* | Grok: no. A colon after *1.726 m* reads as a ratio; use *"1.726 m (2.43 times the pitch arm), a consequence …"*. ChatGPT, DeepSeek, Qwen: yes | **Colon.** With parentheses, *"a consequence"* attaches to the semi-span length. The source's dash attached it to the ratio, and so does the colon. **Grok, does that answer it?** |
| **A11** | *"the fixed-pitch propeller is why the margin above sits where it does"*, left unchanged | Grok, DeepSeek: positional; use *"the preceding margin"*. ChatGPT, Qwen: not addressed | **"the preceding margin"**: it points back at the stall margin discussed earlier in the section. **ChatGPT, Qwen?** |
| **A12** | *"… and is named next"* | Grok: no, use *"named after Table 4"*. DeepSeek: no, use *"named later in this section"*. ChatGPT, Qwen: yes | **"is named later in this section."** I checked the source: the strip is named two paragraphs after Table 4 (a note and the tip-pair paragraph intervene), so *"next"* is wrong. And Table 4 floats in the typeset paper, so *"after Table 4"* may not hold on the page. **ChatGPT, Qwen, Grok?** |
| **D50** | *"The architecture claim, that the configuration is arranged to change regime with no mechanism that reorients a propulsor, is a count …"* | ChatGPT: no. The commas make a content clause look nonrestrictive; remove them: *"The architecture claim that the configuration … is a count …"*. Grok, DeepSeek, Qwen: yes | **With ChatGPT.** *"The claim that X"* is a content clause, and commas around it misparse the sentence. **Grok, DeepSeek, Qwen?** |
| **D55** | *"… and the accounting; that is what Sections 5.1 and 5.2 describe and what Section 6.2 prices."* | Qwen: no. Singular *"that"* narrows the scope to *"the accounting"*. Qwen proposes *"… and the accounting, which Sections V.A and V.B describe and Sec. VI.B prices"*. Grok, ChatGPT, DeepSeek: yes | **A new candidate that deletes only:** *"… and the accounting: what Sections 5.1 and 5.2 describe and what Section 6.2 prices."* The colon restates all three items; nothing is added and *"which is"* is dropped. Qwen's repair would attach *"which"* to *"the accounting"* alone, the very narrowing it objects to. **Everyone: the new candidate, yes or no?** |

---

## D. The journal supplement: a finding first, then a proposal

**The finding.** `paper/v8/supplement.md` is mostly an **audit archive**:
- 15 sections and about 66,000 words;
- in most sections, every subsection is a frozen snapshot (*"as it stood before …"*);
- only S1, S3, S4 and S10–S14 have any text before their first snapshot heading, and in S10 and S12 that text is itself pre-compression paragraphs. **S2, S5, S6 and S8 have none.**

The body points to the supplement **34 times** (table below). For most pointers, **the promised content exists only inside a frozen snapshot of an earlier draft**. For example:
- the strip geometry and the 39 mm fairing (S8) are only in *"Section 8 as it stood before the length pass"*;
- the sizing-loop working (S10) is only in *"Section 10 as it stood before recomposition"*.

Those snapshots also carry claims the body has since retired. One example is the v7-era XB-35 aside in S8's snapshot. **The archive cannot be shipped as the journal supplement, and it cannot be cut down mechanically.**

**The 34 pointers** (section in the assembled view, the sentence shortened):

| # | S | Body section | Sentence |
|---|---|---|---|
| P01 | S2 | 2.1 The tax | The ratio between the two demands follows from the governing equations rather than from any design choice (Supplement S2): |
| P02 | S2 | 2.1 The tax | One of these transfers has direct experimental support (Supplement S2). |
| P03 | S2 | 2.1 The tax | The tilting row, which needs both clarifications, is worked through in Supplement S2. |
| P04 | S3 | 2.2 The escape condition | What each departure costs is in Supplement S3. |
| P05 | S3 | 2.2 The escape condition | Six costs are permitted, named here before any candidate is examined (the working is in Supplement S3): |
| P06 | S4 | 2.3 An independent quantitative check | The working is in Supplement S4. |
| P07 | S4 | 2.3 An independent quantitative check | The published weight breakdown is consistent with the transfer property of Section 2.1 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce: its three reported categori… |
| P08 | S14 | What is sized, and what is not demonstra | Whether the descent enters the vortex ring state is an open question in Supplement S14; the landing transition is not the take-off transition run backwards, and no figure in this paper describes it (Supplement S5). |
| P09 | S5 | What is sized, and what is not demonstra | Whether the descent enters the vortex ring state is an open question in Supplement S14; the landing transition is not the take-off transition run backwards, and no figure in this paper describes it (Supplement S5). |
| P10 | S14 | What is sized, and what is not demonstra | What that refusal costs in authority and in response time is not computed, and Supplement S14 carries it. |
| P11 | S6 | What the margin actually is, in one curr | Which blade a designer would choose also turns on structural loads, acoustics, the motor operating point, rotor inertia and manufacture, none of which is modelled in this work (Supplement S6). |
| P12 | S6 | Five qualifications: three run against t | The compared vehicles are larger than both designs studied here, which are of order 50 kg and 1 000 kg (Supplement S6), and Reynolds number favours the larger aircraft, so the smaller design is at a disadvantage in this … |
| P13 | S8 | 5.2 What it is made of, and what still m | Roll comes instead from a strip on the lower surface (its geometry is in Supplement S8). |
| P14 | S8 | 5.2 What it is made of, and what still m | The frames carry a fairing, and it is not only a drag measure: a planar planform supplies no directional stability, so the fairing is the aircraft's only vertical surface, and sized against the criterion the tailless lit… |
| P15 | S11 | 5.2 What it is made of, and what still m | The stopped state is not: the stop must be produced by something — motor holding torque, an electrical brake, a mechanical lock — and a stopped fixed-pitch blade also has an azimuth, so the stopped-state drag estimates (… |
| P16 | S10 | 6.1 Analytical closure of the sizing loo | Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Su… |
| P17 | S10 | 6.1 Analytical closure of the sizing loo | Run on the reference design's own assumed inputs, the same construction reproduces that design within 1.5 percent (Supplement S10), so the closures report a change of inputs, not of method. |
| P18 | S10 | 6.1 Analytical closure of the sizing loo | Solved with rotational dynamics and a finite control moment, and with the aerodynamic pitching moment set to exactly zero, so that nothing favourable is borrowed, the 50 kg design loses 5.4 to 6.6 m at the same reference… |
| P19 | S11 | 6.2 The ledger | In the drag build-up behind the bracket (line items in Supplement S11), the hardware exposed by the vertical-phase layout — the tip frames and the free-wheeling tip-pair rotors — is 69 percent of the zero-lift drag at th… |
| P20 | S11 | 6.2 The ledger | No stopped-state counterfactual was computed: the eight tip discs stopped edge-on are estimated at ΔC_D0 = 0.0008 (Supplement S11), but that takes an indexing mechanism, a class Section 5.1 counts, which has not been siz… |
| P21 | S11 | 6.2 The ledger | The deficit per kilogram of take-off mass that the buffer covers, taken at the electrical bus, spreads by 12 percent across the four closures while the fraction is held at 3.6 percent (Supplement S11). |
| P22 | S11 | 6.2 The ledger | Bill 3 is removed from the engine and left standing on the electrical system (the propulsion-mass split is in Supplement S11). |
| P23 | S14 | 6.2 The ledger | Section 6.1's convergence does not cover the cost of declining the reaction-torque channel, the sizing of the strip's actuation, the allocation of the take-off margin against attitude authority, the landing transition, t… |
| P24 | S12 | 6.3 Scale does not lock two of the charg | The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 6.1's closures (Supplement S12). |
| P25 | S12 | 6.3 Scale does not lock two of the charg | It appears here as the energy buffer, 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and both figures are inputs (Supplement S12). |
| P26 | S13 | 6.4 Rankings belong to contracts | Range in the sizing loop is proportional to L/D, to the energy chain and to the fuel fraction, and the three contracts differ only in the last (Supplement S13): a fixed fuel fraction, sixteen percent of each architecture… |
| P27 | S13 | 6.4 Rankings belong to contracts | The choice runs against this configuration: without the buffer, and with engines rated to the hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off mass (Supplement S13)… |
| P28 | S13 | 6.4 Rankings belong to contracts | The per-closure numbers are in Supplement S13. |
| P29 | S13 | 6.4 Rankings belong to contracts | Where it falls is decided by quantities this study has not measured or fixed: the blade family in the base case, and across the sensitivity cases the competitor's lift-group mass and the propeller basis (Supplement S13). |
| P30 | S13 | 6.4 Rankings belong to contracts | Comparing computed figures against assumed ones favours whichever is assumed more optimistically — in propeller efficiency both competitors, and with a common propeller efficiency the lift-plus-cruise lead under the firs… |
| P31 | S14 | First, the known obstacle: the energy st | A pack flown in a 210 kg-class electric VTOL aircraft is rated, as a flown system, at 0.892 kW per kilogram continuous; its unit pack, discharged on the bench at its highest tested rate, delivered on average about 1.5 kW… |
| P32 | S14 | First, the known obstacle: the energy st | The package Section 6.1 closes on does not exist with any store the sources consulted here report as built; closed again at the bench rate, it becomes 76 to 81 percent heavier, a sensitivity with one input changed rather… |
| P33 | S14 | Then what is not known | Eighteen further questions are open, and Supplement S14 lists each with what it bears on and what would settle it. |
| P34 | S14 | What the claims that remain amount to | Section 7 and Supplement S14 list what the paper leaves open. |

**Proposal (mine):**
1. **Compose a new journal supplement**, `paper/submission/supplement.md`, which a generator turns into LaTeX. It contains only what the 34 pointers promise.
2. **Each passage comes from the latest snapshot that holds it, brought up to the current body.**
   - No claim the body has retired (`v8_stale.py` runs on the output).
   - Every number keeps its identity with the body: value, unit, object, model.
   - Every passage records where it came from (snapshot heading and line), so it can be traced.
3. **Receipt table:** every pointer is graded R1–R4 against the composed section (the Round 130 rule). The supplement is not final while any pointer is R3 or R4.
4. **Numbering.** S1, S7, S9 and S15 are cited nowhere, so the cited labels are S2–S6, S8 and S10–S14, with gaps. **I propose renumbering them S1–S11 in the submission**, mapped by the generator in the body and in the supplement. Gaps would puzzle a referee, and the mapping is mechanical.
5. **The audit archive stays as it is,** in the repository and on Zenodo.
6. **Order:** in body order, two or three sections per round, each shown to you in full. S2, S3 and S4 come first.

**D, everyone:**
- Agree with the method, or name what should differ?
- In particular, renumbering versus keeping the step-based labels.
- And is there a pointer you would rather remove from the body than serve? Removal is not shortening, but it does change a body sentence, so it needs a vote and possibly the author.

---

## E. Your own proposals

Open, as always.

---

## F. Errors (one list)

- **Qwen:** named A04, A05 and A14 as protected. They are not in the register.
- **Claude:**
  - **A12.** I proposed *"named next"* without checking where the strip is named. It is two paragraphs later. Grok and DeepSeek caught it.
  - **The protected register.** My detection of protected sentences was weak in Round 202: A02 and I7 were found only on a second pass.
  - **The supplement.** I described it as having a separable *"working part"* (Round 201 §D). For most sections that part is empty. All five of us accepted the plan on that description.
- **Grok, ChatGPT, DeepSeek:** none found.

---

## G. What goes to the author

- **Nothing now.** The supplement method and the five style rows go to you first.
- **To the author only if needed:** moving or changing a protected sentence while composing the supplement.
