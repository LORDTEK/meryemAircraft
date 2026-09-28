# Round 154 — The author's two instructions: no round-by-round copy cuts, and E8 (the length) is decided by our common decision. The AIAA guideline, the arithmetic, and a first measured supplement move

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**

---

## 0. The author's two instructions

1. **On the map** (my translation from Turkish, so not a verbatim quotation): *Let us not spend 30 rounds on 280 words.*

   So there will be **no cluster-by-cluster rounds for the copy cuts.** Your corrections to the map (§6) are recorded. The copy cuts are
   applied **once, in a single batch**, at the end of Phase B.
2. **On E8, the length** (also my translation): *Let us act on the common decision of all of you.*

   So E8 is decided by **the four of you and me, with the usual threshold.** That is §4. The author has also uploaded the AIAA guideline
   that we lacked. It is now in the repository (`references/AIAA-2024-09_journal-page-limits-and-word-count-guidelines.pdf`) and is
   quoted in full in §1.

---

## 1. The AIAA guideline, in full

This is the text extracted from the uploaded PDF (one page, "Rev. August 2024"). Line breaks and the layout of the tables are kept.

```
Journal Page Limits and Word Count Guidelines
The manuscript text should be as brief and concise as proper presentation of the ideas will allow. AIAA
provides word-count and manuscript length guidelines to streamline the submission and review process.
A journal editor at his or her own discretion may request that a manuscript be shortened or expanded
before or after peer review, to meet individual journal standards and to best convey the concepts being
discussed.
Recommended Published Page Counts (1400 words* per published page)
Regular/Full Articles                          7 – 10 pages; 10,000 – 12,000 words
Technical Notes                                1 – 3 pages;   2,500 – 3,500 words
Survey Papers                                  13 – 15 pages; 18,000 – 20,000 words

*Or equivalent space for figures/tables

Calculating Manuscript Word Counts
     -      MS Word: Take the software-generated word count for the text; add in word counts for the
            equivalent space taken up by tables and figures, roughly calculating the equivalent space as
            follows:
                 o Standard, single-column figure or table is equivalent to 200 words
                 o Standard, two-column figure or table is equivalent to 450 words
                 o Large, two-column table is equivalent to 700 words
     -      LaTeX/PDF: Count the number of words on 2 to 3 lines of the manuscript text and take the
            average per line; multiply the words/line by the number of lines on a full page of text to
            determine the words/page. Multiply the words/page by the total number of manuscript pages
            regardless of whether they contain text, figures, tables, displayed equations, or a combination
            thereof.

                                          Equivalencies for Author Manuscripts
                                                         Double-Spaced Manuscript Pages (one-inch margins)
                                                  Serif font (e.g., Times)               Sans serif font (e.g., Arial)
 Regular Articles
     10-point type                                       20 – 26                                     22 – 28
     12-point type                                       29 – 37                                     33 – 43


Technical Notes
         10-point type                                   5–7                                         6–8
         12-point type                                   7 – 10                                      8 – 12

 Survey Papers
     10-point type                                      30 – 33 ½                                    33 – 37
     12-point type                                       43 – 47 ½                                  48 ½ – 54




Rev. August 2024
```

**What it settles, in my reading. Please check it against the text:**
- The figures are **"Recommended Published Page Counts"**, not a hard limit. For Regular/Full Articles they are **10,000–12,000 words**,
  with figures and tables counted by equivalence: 200, 450 or 700 words each.
- *"A journal editor at his or her own discretion may request that a manuscript be shortened or expanded before or after peer review."*
  The document says **nothing about rejection or charges** for length.
- The Survey category (18,000–20,000) is not ours.

**What it does not settle:** how far past 12,000 an editor tolerates. Our own record has one warning. On 2026-09-15 the manuscript was
turned away twice without review:
- *Drones* found it out of scope;
- *Aerospace* rejected it at the desk on the day it arrived, with its *"discipline, novelty and general significance"* template, when the
  manuscript had 35 827 words.

The stated reasons were not length. But a long manuscript does not help at the desk.

---

## 2. The arithmetic, corrected

- **Sections 2.1–2.3, 4 and 7.1–7.4 hold 11 261 words.** The remaining sections (1, 3, 5.1, 5.2, 6.1, 6.2, 8, 9) hold **9 070**.
  DeepSeek's figures are right.
  - Grok gave 10 070 and 10 230.
  - ChatGPT summed only the subsections I had listed (8 096) and drew a conclusion from that sum.
- **Even if every word of 2.x, 4 and 7.x left the body, the prose would stay above the 8 500 that the Round 101 plan allows.** All four
  of you said so.
- **The 187 protected sentences total about 3 025 words.** They are a floor, but not the binding one.
- **A measured supplement move (§5): Section 7.3 goes from 1 083 to 761 words, about 30 %,** with every protected sentence but one staying
  in the body. At that rate, the whole of 2.x, 4 and 7.x yields roughly 3 500–4 500 words. The prose would still be around 16 000.

---

## 3. A fact all five of us missed in Round 153

We all treated the author's Round 67 rule (*"calculations first"*) as if it forbade cutting the architecture sections. It does not. **In
Round 72 the author decided** (my translation): *If we are going to shorten, we shorten from everywhere.*

- Steps 5–8 were brought into the shortening then.
- The spirit rule stands: the insight is carried by placement, order and voice, and the ten spirit sentences stay protected.
- The order is calculations first, then the framework, then the rest.

**So "calculations first" is an order, not an exemption.** This is my error first, because I framed the Round 153 question that way.

---

## 4. E8 — the length. Please decide; the common decision is the decision

**The options, with what each costs:**

| | Option | What it takes | Risk |
|---|---|---|---|
| **1** | **12 000 all-in** (the recommended ceiling) | cuts from everywhere (Round 72): the calculations first, then the framework, then the architecture sections compressed to about half, with the spirit sentences and the protected set kept | the architecture's account becomes dense; the protected set and the argument steps (W-2's lesson) set a floor we have not measured |
| **2** | **A moderate overrun**, relying on the editor's discretion | the same order, stopping at a measured floor (perhaps 13 000–14 000 all-in) | the editor *"may request that a manuscript be shortened"*; a long paper at the desk |
| **3** | **A companion paper**: the architecture in this one, the framework and calculations in a second | a split | §0.6 of our own record: *"two contributions read as two papers"* was the reason for the Round 35 decision; a split changes the paper the author chose |
| **4** | **Aim at 1, accept 2 if measured** | start with the calculations and the framework under supplement moves, measure, then decide how far the architecture goes | none of its own; it defers the hard choice by two or three phases, with numbers in hand |

**My vote: 4**, with a written trigger. If, after the calculations and the framework, the honest floor with the architecture compressed is
above about 13 200 all-in (10 % over), we put option 3 to the author with the measured numbers. Below it, we finish at option 1 or 2. **My
reason:** the guideline makes 12 000 a recommendation with editor discretion, not a wall. The only work that is certain under every option
except 3 is the calculations' supplement moves, and they are needed first under every one of them.

**Please give:**
- your option;
- the number you would aim for;
- the risk you accept;
- your answer to each other.

**If there is no common decision this round, the disagreement goes side by side to everyone, and then to the author.**

---

## 5. A first supplement move, measured: Section 7.3 (for your check; applied only if E8 is not option 3)

**The rule applied:** Round 104. *"A calculation may not move if the surviving body sentence would cease to tell the reader what was
actually found."* Sentences are kept verbatim or cut by deletion only. Nothing is added except *"The working is in Supplement S12."*

**What moves to Supplement S12, in full and under its original headings:**
- the disc-loading and specific-power numbers;
- the 4.19 / 3.98 paragraph;
- the 0.35 → 0.47 geometry;
- the rotor-term values 0.0154 / 0.0068 / 0.0045–0.0100 and the Reynolds numbers;
- *"three other candidates are excluded"*;
- the buffer-derivation sentence;
- the opening sentence *"Either answer leaves the mechanism claim where it was; …"*, which 7.1, 7.2 and 8 each state.

**One protected sentence moves with its result, and that needs the author's decision (Round 104, rule (iii)).** It is *"This paragraph
compares the reference pair only."* It qualifies the 4.19 / 3.98 paragraph that moves. The other ten protected sentences of the section
stay in the body.

**Please check:** is any finding, qualification, model identity or number meaning lost? Does any kept sentence lose its antecedent? And
does a reader of the new 7.3 still learn what was found?

### 5.1 Section 7.3 now (1091 words)

#### 7.3 Scale does not lock two of the charges together; the third is not tested

Section 7.2 decomposed the three charges on one aircraft, at one size; **this section asks whether they are three quantities or one quantity under three names**, by changing the size of the aircraft and seeing whether they move together. Either answer leaves the mechanism claim where it was; that claim rests on the inventory of Sections 5.1 and 5.2. **The test is deliberately weak**, and it is stated at its own strength. It can show that two charges are not locked together within this model. **It cannot show that they are independent in general**, and it is not offered as doing so.

**The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 7.1's closures**: no closure was run at 1 000 kg, the heavy design has no drag bracket and no structural closure, and no heavy-design range is quoted.

##### Bill 3 — held nearly flat by a sizing rule, which is not a finding about Bill 3

Disc loading is held at approximately the same value, 44.2 kg m⁻² at 50 kg and 43.7 at 1 000 kg, so specific hover power is held with it: 0.218 kW kg⁻¹ at the light design and 0.216 at the heavy. **That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3.**

Section 7.2's measure of Bill 3, rotor-shaft hover power over engine shaft rating, is 4.19 at the light design and 3.98 at the heavy, and with the engine margins the two designs use it **moves by between 5 and 14 percent across the factor of twenty, depending on an engine margin the sizing rule does not set** (Supplement S12). *(Section 7.2's 2.4 to 3.2 is the same ratio at the four closures. This paragraph compares the reference pair only.)*

The rule has a price, paid in geometry: the ratio of propeller diameter to span rises from 0.35 to 0.47, and **much above 1 000 kg a single nose pair can no longer hold the disc loading**, so a second would have to be added.

##### Bill 2 — the rotor term falls, and in this model Reynolds number accounts for it

**Only the rotor term of Bill 2 is computed at both sizes**; the frame term enters both designs as the same multiplier, so it cannot show a scale effect in either direction. At 50 kg the rotor term is **0.0154**; at 1 000 kg the blade designed to the same section lift coefficient gives **0.0068**, and the blades swept give 0.0045 to 0.0100 — a direction that is the ordinary one and a factor that is not a measurement. **Within the blade-element and section-polar model, the section Reynolds number accounts for the fall**, rising from about 8 × 10⁴ to 5.6 × 10⁵; three other candidates are excluded (Supplement S12), and this is a decomposition inside the model rather than a causal claim beyond it.

The fall rests on section drag taken from polars rather than measured, and the light end lies below a Reynolds number of 10⁵, where section drag is hardest to predict. **Of the two rotor terms, the light one is therefore the less certain — and it is the one Sections 7.1 and 7.2 carry.**

##### Bill 1 — not tested, and the one available derivation would not test it

On this configuration Bill 1 appears as the energy buffer: 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and **both of those figures are inputs.** **A change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction.** A buffer sized to the hover deficit at the same specific power would track hover power and engine rating, which are the Bill 3 measures, so that derivation cannot test whether Bill 1 separates. **Whether the two are separable here is not established**; what is established is that they are coupled here, which is Section 2.2's claim rather than a defect found in it. **Coupling is not identity**: the buffer is measured in kilograms and the engine in kilowatts, linked by a specific power that is itself an assumption.

##### What the comparison establishes

**Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its light-design value in the section polars used here, while specific hover power changes by one percent and the Bill 3 ratio by 5 to 14 percent.** The flatness of Bill 3 is imposed by a sizing rule; the finding is that Bill 2 moved anyway, by more than the Bill 3 ratio at every point in the heavy interval and under either engine margin. **Within this model, the two are therefore not one quantity under two names.**

**Bill 1 is not tested**, and nothing here should be read as showing that it separates from the other two — or as showing that it does not. **The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low Reynolds number.** It is consistent with the separability Section 2.1 asserts; it is not a verification of separability as a general property, which a single instantiation cannot supply.

##### Two costs that scale does not relieve

The fixed-pitch gap also widens slightly with size, to 16.4 to 22.9 percent at the heavy design (Supplement S12); as in Section 7.2, no variable-pitch counterfactual was computed. **The transition is where the square–cube relation is paid in full**: rotating the heavy design in the light design's two seconds would demand about 220 kW from the tip pairs, roughly the whole of hover power; at its own 5.1 seconds the demand is about 13 kW. **A larger aircraft of this type turns more slowly, and must.**

##### Why this section sits between the ledger and the contracts

**Because at least two of the charges are not locked together, a comparison of architectures cannot in general be reduced to a number that does not depend on how the charges are weighed.** The argument requires only two charges that are not locked together; the third need not be shown separate for the conclusion to hold. Section 7.4 examines what the choice of sizing contract does to a ranking, on the light closures of Section 7.1 only.

### 5.2 Section 7.3 proposed (763 words)

#### 7.3 Scale does not lock two of the charges together; the third is not tested

Section 7.2 decomposed the three charges on one aircraft, at one size; **this section asks whether they are three quantities or one quantity under three names**, by changing the size of the aircraft and seeing whether they move together. **The test is deliberately weak**, and it is stated at its own strength. It can show that two charges are not locked together within this model. **It cannot show that they are independent in general**, and it is not offered as doing so.

**The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 7.1's closures**: no closure was run at 1 000 kg, the heavy design has no drag bracket and no structural closure, and no heavy-design range is quoted. The working is in Supplement S12.

**Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its light-design value in the section polars used here, while specific hover power changes by one percent and the Bill 3 ratio by 5 to 14 percent.** The flatness of Bill 3 is imposed by a sizing rule; the finding is that Bill 2 moved anyway, by more than the Bill 3 ratio at every point in the heavy interval and under either engine margin. **Within this model, the two are therefore not one quantity under two names.**

Disc loading is held at approximately the same value, so specific hover power is held with it. **That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3.** The rule has a price, paid in geometry: **much above 1 000 kg a single nose pair can no longer hold the disc loading**, so a second would have to be added.

**Only the rotor term of Bill 2 is computed at both sizes**; the frame term enters both designs as the same multiplier, so it cannot show a scale effect in either direction. **Within the blade-element and section-polar model, the section Reynolds number accounts for the fall**, and this is a decomposition inside the model rather than a causal claim beyond it. The fall rests on section drag taken from polars rather than measured, and the light end lies below a Reynolds number of 10⁵, where section drag is hardest to predict. **Of the two rotor terms, the light one is therefore the less certain — and it is the one Sections 7.1 and 7.2 carry.**

**Bill 1 is not tested**, and nothing here should be read as showing that it separates from the other two — or as showing that it does not. On this configuration Bill 1 appears as the energy buffer: 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and **both of those figures are inputs.** **A change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction.** **Whether the two are separable here is not established**; what is established is that they are coupled here, which is Section 2.2's claim rather than a defect found in it.

**The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low Reynolds number.** It is consistent with the separability Section 2.1 asserts; it is not a verification of separability as a general property, which a single instantiation cannot supply.

The fixed-pitch gap also widens slightly with size, to 16.4 to 22.9 percent at the heavy design (Supplement S12); as in Section 7.2, no variable-pitch counterfactual was computed. **The transition is where the square–cube relation is paid in full**: rotating the heavy design in the light design's two seconds would demand about 220 kW from the tip pairs, roughly the whole of hover power; at its own 5.1 seconds the demand is about 13 kW. **A larger aircraft of this type turns more slowly, and must.**

**Because at least two of the charges are not locked together, a comparison of architectures cannot in general be reduced to a number that does not depend on how the charges are weighed.** The argument requires only two charges that are not locked together; the third need not be shown separate for the conclusion to hold. Section 7.4 examines what the choice of sizing contract does to a ranking, on the light closures of Section 7.1 only.

---

## 6. The map: your corrections, recorded, to be applied once

**The corrections:**
- **K-2, 5.2, "What declining it costs is not counted in this work."** It is protected, so it cannot be "–".
  - It becomes **C** (Grok, ChatGPT) or **K** (DeepSeek). I agree it cannot be deleted. I prefer C: it keeps the local boundary in a clause.
  - **My error:** the map's own rule forbade what I marked.
- **K-4:** the map missed 5.1's *"The four tip pairs do not: they are exposed in the cruise flow and they cannot be feathered, so they
  re-open the second charge."* (ChatGPT). Added.
- **K-3, 7.1:** the function is **boundary**, not definition (ChatGPT). Agreed.
- **K-3, 6.2** (restating 5.1): **K** (DeepSeek) or **C** (the others). To be settled in the batch.
- **K-1, Section 9, the two denials:** **C (Phase D)**, not "–" (DeepSeek). They go with the 6.2 + 9 decision. Agreed.
- **K-9, 4, "And the fixed-pitch propeller …":** **–** (Grok, ChatGPT, Qwen) or **K** (DeepSeek, who argues that it states a different
  consequence). To be settled in the batch.
- **C-13, 5.1, the actuator sentence:** **K** (Grok, DeepSeek). Agreed: the replacement is named at the combining step.

**New clusters you proposed:**
- Grok: F-1 (the tip pairs' adopted cruise state) and F-2 (the transition numbers).
- ChatGPT: K-10 to K-13 (airframe rotation; sized, not demonstrated; wing-borne cruise lift; the transition as a model result).
- DeepSeek: C-14 (the stopping note) and C-15 (the tip frames' four jobs).
- Qwen: the drag bracket and the closures.

They join the batch list. Most of their occurrences, like the map's, will be K.

---

## 7. Errors this round

- **Mine:**
  - the protected sentence marked "–";
  - the K-4 occurrence I missed;
  - the Round 153 question framed as if Round 67 exempted the architecture (§3).
- **Grok:** its section totals were 10 070 and 10 230; they are 9 070 and 11 261.
- **ChatGPT:**
  - it drew a total from a partial table (8 096);
  - it placed the independent check in §4; it is 2.3.
- **DeepSeek, Qwen:** none found. DeepSeek's arithmetic is the one this round uses.

---

## 8. What I ask of you

| # | Item |
|---|---|
| a | §1: is my reading of the guideline right? |
| b | **§4: E8 — your option, your number, your accepted risk; answer each other** |
| c | §5: the 7.3 move — any loss? Confirm or name it |
| d | §6: the two unsettled map rows (K-3 6.2; K-9 4) |

If you open a PDF, name it and the page. If you could not open it, give no number from it.
