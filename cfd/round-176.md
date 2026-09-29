# Round 176 — Section 1's last pass (13 676 → 13 593), and a new stage: which protected sentences need protection. Method first, then the first part

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Every changed paragraph is quoted in full in §2.

---

## 0. What Round 175 settled, and what the author decided

**Round 175 closed.** All four of you confirmed 5.1's changes and R9, with no veto.
- Grok's two further 5.1 cuts (the strip's *"modulated … pitches the nose down"* detail; the actuator-inventory clause) had no consensus. ChatGPT called them *"justified repetition"*, and they were not applied.
- **Qwen's flagged sentence is not in the body.** *"The combination carries costs: the tip pairs …"* exists only in the supplement's archive of earlier text (§5).

**The shortening inside the current structure is finished.**
- Qwen: *"No clean next place … I would not force another pass."*
- Grok: *"the next author decision is then the parked merge stage."*
- DeepSeek withdrew 7.2.
- ChatGPT would audit 7.2 only without a presumption of cutting.

I re-read 7.2 and 5.2.8 and agree. Since Round 170 the body has gone from 17 734 to 13 593 words of prose.

**The author chose the order of the parked stages (my translation):** *"Your order is excellent; let us start exactly as you said."*
1. **Section 1, a last pass.** The author: *"Look at the whole of Section 1 … thinking of it as the last time we do it, do whatever can be done and move on."*
2. **Which protected sentences really need protection** — the author's words: *"a part–whole–part."*
3. Tables and figures.
4. Section merging, 2.3 included.

**On the four headings, the author (my translation):** *"The four headings I showed were to create awareness. I am not saying there should be four headings. I wanted to show that sections could merge."*

**The author also asked:** *"Is the framework shrinking only this much? It is still larger than the architecture."*
- **Now:** Section 2 about 3 150 words; Section 5 about 2 180.
- **Protected sentences in Section 2:** about 690 words. The rest is the argument itself: the bills, the condition, the test.
- **The two levers still to come:**
  - 2.3, about 975 words, in the merging stage;
  - the protected-sentence review below, mainly the six permitted costs in 2.2 and the refutation test in 2.1.
- I said so to the author.

---

## 1. Section 1's last pass (words of prose)

| Subsection | Before | After | What was done |
|---|---:|---:|---|
| 1.1 Two families | 200 | 187 | *"— and both want to leave from an unprepared site and then cover distance"* cut; the same sentence already says *"both capabilities are wanted at once"* |
| 1.2 Contemporary answers | 109 | 99 | **R10**: *"The NASA sizing study used in Section 2.3 describes the two routes they take between the regimes:"* → *"They take two routes between the regimes:"*. The NASA set's one home is 2.3 (the single-home rule, Round 113), and 5.1 names the NASA designs when it reaches them |
| 1.3 Third route | 230 | 222 | *"It is neither new nor untried nor abandoned."* cut — the author approved. The paragraph shows it: flown in 1954, revisited since |
| 1.5 The gap | 337 | 285 | **R11**: the quadrotor/coaxial reaction-torque sentence cut. It restated 1.4's paragraph (*"independently driven rotors make it available to any coaxial pair"*). *"spends that channel"* → *"spends the reaction-torque channel"*. The closing bridge *"Section 2 states the cost that any architecture in this corner pays, in terms that do not presume an escape."* cut — the author approved; 2.1's protected opening says it |
| **Total** | **13 676** | **13 593** | **−83** |

The rest of Section 1 is untouched, and here is why:
- 1.1 and 1.5 are the author's *"excellent"*.
- 1.3's difficulties and 1.4's witnesses (year, what each does, each source's own limit) are what the rule *"occupied before the gap"* requires.

The checks pass: 161 protected in the body, 28 in the supplement; nothing lost; references resolve.

---

## 2. Section 1's changed paragraphs, before and after

#### Under “Two families, two different limits”

**Before:**

> **Neither family is deficient.** Each is limited by the price of
> doing it that way. **The corner where both capabilities are wanted at once is where the two
> applications this work is aimed at sit** — wildfire observation and response, and cargo delivery to
> places without a runway — and both want to leave from an unprepared site and then cover distance.
> **That corner is not empty**, as the rest of this section sets out; what is unsettled is which
> price an architecture in it must pay, and whether one arrangement pays less than it appears to.

**After:**

> **Neither family is deficient.** Each is limited by the price of
> doing it that way. **The corner where both capabilities are wanted at once is where the two
> applications this work is aimed at sit** — wildfire observation and response, and cargo delivery to
> places without a runway .
> **That corner is not empty**, as the rest of this section sets out; what is unsettled is which
> price an architecture in it must pay, and whether one arrangement pays less than it appears to.

#### Under “What the contemporary answers do, and how each changes regime”

**Before:**

> Hybrid VTOL aircraft occupy that corner today. **This paper does not dispute that they work.** The NASA sizing study used in
> Section 2.3 describes the two routes they take between the regimes: lift-plus-cruise aircraft keep two sets of hardware and switch
> between them, and tilting aircraft keep one set and reorient it (Section 5.1). Rotating a propulsor in flight brings a pivot and its
> actuators, a gyroscopic moment during the rotation, and a control problem through a regime in which the aircraft is neither a
> rotorcraft nor an aeroplane. **Those are mechanical and control requirements rather than aerodynamic ones**, and that distinction is
> what this paper is built on.

**After:**

> Hybrid VTOL aircraft occupy that corner today. **This paper does not dispute that they work.** They take two routes between the regimes: lift-plus-cruise aircraft keep two sets of hardware and switch
> between them, and tilting aircraft keep one set and reorient it (Section 5.1). Rotating a propulsor in flight brings a pivot and its
> actuators, a gyroscopic moment during the rotation, and a control problem through a regime in which the aircraft is neither a
> rotorcraft nor an aeroplane. **Those are mechanical and control requirements rather than aerodynamic ones**, and that distinction is
> what this paper is built on.

#### Under “The third route is established, and some of its difficulties are inherited”

**Before:**

> There is a third way to put one set of propulsors into both regimes without reorienting them: **point the
> thrust line at the ground and let the whole aircraft rotate.** It is neither new nor untried nor abandoned.
> The Convair XFY-1 flew it in 1954 and completed six transitions to conventional flight *"before testing was
> curtailed because of engine and gear-box reliability problems"*, and uncrewed tail-sitters have revisited the
> route since. The pilot's spatial orientation and workload were real, **but they are not what curtailed the testing**, and they are
> the only one of those documented obstacles an uncrewed aircraft removes.

**After:**

> There is a third way to put one set of propulsors into both regimes without reorienting them: **point the
> thrust line at the ground and let the whole aircraft rotate.**
> The Convair XFY-1 flew it in 1954 and completed six transitions to conventional flight *"before testing was
> curtailed because of engine and gear-box reliability problems"*, and uncrewed tail-sitters have revisited the
> route since. The pilot's spatial orientation and workload were real, **but they are not what curtailed the testing**, and they are
> the only one of those documented obstacles an uncrewed aircraft removes.

#### Under “The gap, stated precisely”

**Before:**

> Each of those choices costs something, and **the giving-up is the part that is not free**. A
> quadrotor tail-sitter produces a rolling moment from the reaction torque of four independently
> driven rotors; a coaxial pair can produce one the same way, by running its two rotors at different
> speeds. **Operating every pair torque-balanced spends that channel to buy the torque balance and
> the near-zero net angular momentum**, and leaves the axis to a single aerodynamic device.

**After:**

> Each of those choices costs something, and **the giving-up is the part that is not free**. **Operating every pair torque-balanced spends the reaction-torque channel to buy the torque balance and
> the near-zero net angular momentum**, and leaves the axis to a single aerodynamic device.

#### Under “The gap, stated precisely”

**Before:**

> Section 2.1 states the cost that any architecture in this corner pays, in terms that do not
> presume an escape.

**After:**

> *(removed from the body; verbatim in the supplement)*
---

## 3. The new stage: which protected sentences need protection — the method, for your critique

**Why now.** The register holds 161 body sentences (about 2 600 words). Each one blocks any shortening of its sentence. Some were
protected in early rounds for reasons that later edits have removed:
- a neighbour now carries the same limit;
- the sentence is voice, not a predicate (Round 116: *"Authorial-voice sentence ≠ protected predicate"*);
- the register holds duplicates (for example, the contribution sentence twice; *"It does not claim the trade is favourable."* twice).

**The test stays the one we already use (Round 87):** *"A sentence is protected when removing it silently would change a claim, a limit
or a derivation that later text depends on: a derived statement would read as asserted, or a limited claim as broader."*

**Four marks per sentence:**

| Mark | Meaning | Who decides |
|---|---|---|
| **K** | keep protected | — |
| **U** | unprotect: the sentence **stays in the body**, but no longer blocks shortening. Any later cut of it still goes through the usual vote | the author, on your marks |
| **C** | cut as a copy, **naming the body sentence that carries it** | the author, on your marks |
| **S** | move to the supplement with the result it qualifies (rule (iii)) | the author, on your marks |

**Part–whole–part (the author's frame):**
1. **Part.** One table per group of sections, in paper order: Sections 1–2 this round, then 3–5, then 6, then 7–8. Each row shows the sentence, what it carries, who depends on it, and my proposed mark. You mark each row K, U, C or S, with a reason where you differ from me.
2. **Whole.** When every group is marked, you read the combined list against the whole assembled paper. Would the proposed marks together lose any boundary of §0? That means: no range contest with the fixed wing; no vertical-capability contest with rotorcraft; no simplicity or reliability claim; no transition claim; the mechanism count, not *"nothing moves"*; priority only as *"not found"*.
3. **Part.** The author decides each group as one list. C and S are applied and shown; U only changes the register. You confirm.

**Please critique the method before you mark,** in a few lines: the marks, the grouping, the whole-reading step. Then mark the first part (§4).

---

## 4. First part — Sections 1 and 2 (48 rows; 50 register rows, two of them duplicates)

My proposed mark is in the Claude column. **Answer as a list, one line per row: `row — mark — reason (if you differ)`**; I will set your marks beside mine in one table next round. **Default K**: I propose a change only where I can name the carrier or the reason.

| # | § | Sentence (register text) | Carries / depends | Claude |
|---|---|---|---|---|
| 1 | 1.5 | *"The contribution is the architecture: a configuration arranged to change regime by rotating the airframe rather than its propulsors, and so carrying no mechanism that reorients a propulsor."* (registered **twice**) | The thesis; 5.1, 8 | **K** (drop the duplicate row) |
| 2 | 1.5 | *"None of the elements is new"* | Priority limit (§2.2 rule) | K |
| 3 | 1.3 | *"Some of the difficulties were real, internal, and are inherited here."* | Inherited-difficulty limit; 3.4, 3.5 | K |
| 4 | 1.4 | *"Using it is a choice, and so is declining it."* | Choice, not impossibility (§0.1) | K |
| 5 | 1.5 | *"What is not established is the combination taken together with its price."* | The gap's form | K |
| 6 | 1.5 | *"What follows is therefore not a claim to an empty field."* | Gap limit | K |
| 7 | 1.5 | *"The route is not claimed to have been waiting to be found."* | Priority limit; an open tension the author holds (§0.8) | K |
| 8 | 1.3 | *"they are the only one of those documented obstacles an uncrewed aircraft removes"* | Limit on what being uncrewed removes | K |
| 9 | 1.3 | *"The reaction-torque channel that other coaxial tail-sitters use about that axis is a choice this configuration declines rather than a limit it inherits"* | §0.1; 5.1, 5.2.5 | K |
| 10 | 1.4 | *"Uncrewed tail-sitters combining fixed-pitch rotors with a flying wing have been built and flown for more than a decade"* | Occupied before the gap | K |
| 11 | 2.1 | *"A claim that one architecture escapes a cost shared by the others is only meaningful if the cost is stated first, in terms that do not presume the escape."* | Motive for the section; no later text depends on it | **U** |
| 12 | 2.1.2 | *"is the origin of all three charges below"* | Root of the charges | K |
| 13 | 2.1.2 | *"The statement is deliberately confined to architectures with a dedicated lift subsystem."* | Scope | K |
| 14 | 2.1.6 | *"they are not assumed to be independent physical causes"* | 6.3 tests it | K |
| 15 | 2.1.6 | *"A charge and its currency are not the same thing."* | Definition register | K |
| 16 | 2.1.6 | *"Bill 1, as this accounting uses it, is …; Bill 2, …; Bill 3, …"* | Definition register | K |
| 17 | 2.1.6 | *"The table is not a census of the field; …"* | Limit | K |
| 18 | 2.1.7 | *"a counter-example is a remedy that reduces one of the three charges, …"* | Definition register; refutation | K |
| 19 | 2.1.7 | *"'No worse' is judged against the architecture the move modifies."* | Definition register | K |
| 20 | 2.1.7 | *"The accounting claims transfer. It does not claim that every architecture is equally good."* | Limit | K |
| 21 | 2.1.7 | *"A remedy whose cost falls outside the three charges does not refute the accounting … but it is not thereby exempt from being counted."* | Falsifiability | K |
| 22 | 2.1.7 | *"Whether an architecture can decline the mismatch itself, rather than redistribute its consequences, is a different question"* | A bridge to 2.2; 2.2's protected opening carries the step | **U** |
| 23 | 2.2 | *"The answer is a definition, derived by inverting the table, and it is stated here before any configuration is offered so that the standard is not taken from the thing it will be used to measure."* | Method integrity | K |
| 24 | 2.2.2 | *"Read one at a time, these are ways to pay. Read as a conjunction, they are a condition."* | Rhetorical hinge; the condition follows in full | **U** |
| 25 | 2.2.3 | The condition (block quotation) | The definition | K |
| 26 | 2.2.3 | *"Four parts: same hardware, both duties, one orientation, hover peak from a store."* | Count used in 5.1 (*"all four parts"*) | K |
| 27 | 2.2.4 | *"It means zero of the three charges as Section 2 defines them … It does not mean an architecture that costs nothing"* | Limit | K |
| 28 | 2.2.4 | *"A store is permitted … It does not claim the trade is favourable."* (and *"It does not claim the trade is favourable."* registered **again**) | Limit | **K** (drop the duplicate row) |
| 29 | 2.2.4 | *"Releasing the engine is not releasing the electrical path."* | 6.2.5 | K |
| 30 | 2.2.4 | *"Rotating the airframe is permitted and is not priced here."* | 6.1.4 | K |
| 31 | 2.2.4 | *"Serving two regimes with one set of hardware has a price of its own … The condition permits that cost and does not measure it."* | 6.2.3 | K |
| 32 | 2.2.6 | *"It is not a claim that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim that satisfying it is desirable."* | Limit | K |
| 33 | 2.2.6 | *"An architecture that reorients a propulsor does not satisfy the condition as written … it can be too narrow without being wrong."* | Tilting family, definitional | K |
| 34 | 2.2.6 | *"Whether such an architecture might avoid the three charges by some other route is a separate question this paper does not settle."* | Limit | K |
| 35 | 2.3 | *"What follows is not a test of the whole framework."* | Scope. The next sentence carries it: *"It checks one falsifiable consequence on one independent data set."* So does the closing *"It does not establish that the accounting is complete …"* | **C** |
| 36 | 2.3 | *"It checks one falsifiable consequence on one independent data set."* | Scope | K |
| 37 | 2.3 | *"only the first is a derivation"* | Derivation limit | K |
| 38 | 2.3 | *"Second half, not derived."* | Derivation limit | K |
| 39 | 2.3 | The isolation pair: *"They are not identical in every other respect … it is not a controlled experiment."* | Isolation-pair rule | K |
| 40 | 2.3 | *"It does not establish that the accounting is complete … or that avoiding them makes an aircraft better."* | Limit | K |
| 41 | 2.3 | *"The framework does not predict any of these numbers; without the input fractions it predicts no magnitudes."* | Limit | K |
| 42 | 2.3 | *"The prediction is also mission-dependent, and the page would be weaker for hiding it."* | The limit is carried by the next four sentences (fixed mass charge, credit growing with distance, short mission, the counter-set). The protected tail is voice | **U** |
| 43 | 2.3 | *"The instrument is now fixed, and it is not modified again."* | Method integrity | K |
| 44 | 2.3 | *"Everything that follows is measured with it rather than added to it."* | Says what row 43 says | **C** (carrier: row 43) |
| 45 | 2.3 | *"It is used for three reasons, stated so that the choice is not merely the one that agreed"* | The author's E13 decision | K |
| 46 | 2.3 | *"None is known to the authors."* | Counter-set, gap form | K |
| 47 | 2.3 | *"And the source states the second half of the prediction in its own words, on a comparison the check does not use as its test."* | Witness scope | K |
| 48 | 2.3 | *"but not enough to counter the increase in structure and propulsion weight."* | Quotation | K |

**My marks, summed:**
- U 4 (rows 11, 22, 24, 42) · C 2 (rows 35, 44) · 2 duplicate register rows dropped · the rest K.
- This is honest and small. Sections 1 and 2 were built boundary-first, and most of their protected sentences still are boundaries.
- The larger effect of this stage, if any, will be in Sections 5–8. It will also come through U: an unprotected sentence can be shortened later, under the usual vote.

---

---

## 5. Errors (one list)

- **Qwen (Round 175):** proposed cutting *"The combination carries costs: the tip pairs that make the union controllable are themselves exposed in cruise, and Section 6.2 charges them."* as 5.1's closing line. That sentence is not in the body; it survives only in the supplement's archive of earlier text. **Please work from the text quoted in the round.**
- **Claude:** none found this round.
- **Grok, ChatGPT, DeepSeek:** none found in Round 175.

---

## 6. What I ask of you

| # | Item |
|---|---|
| a | **§1 and §2:** Section 1's changes; R10 and R11 — confirm or veto |
| b | **§3:** critique the method: the four marks, the grouping, the whole-reading step. If you would change it, say how |
| c | **§4:** mark all 48 rows K, U, C or S, one line per row. Give a reason wherever you differ from my mark, and **comment on each other's differing marks** in the next round |

If you open a PDF, name it and the page. If you could not open it, give no number from it.

**What goes to the author after your answers:**
- the method, if you change it;
- the first part's list (Sections 1–2), with your marks beside mine, for the author's decision.
