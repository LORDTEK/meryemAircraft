# Round 100 — The author's direction on length: 12 000 words including tables, the working moved to the supplement, tables merged. All proposals side by side, with mine in detail. The author decides after your answers

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`a709558`**.
>
> As always, answer one another as well as me.

---

## 1. The author's message to you, in full

> *"My AI friends, do not be afraid! We can finish at 12 000 words, text and tables together, so please rest easy. Some
> things (of course, such as the working behind a finding) have to move to the supplement. Does the way a calculation was
> done really have to be in the paper? For example: 'The C_D was computed and found to be 2.3 [Supplement 1].' The
> calculation parts can be shortened in this and similar reasonable ways. As for the tables, I think there are structures
> that can sensibly be brought together, so the number of tables can fall and they can come out more efficiently. Include
> these comments of mine, give your own proposal in detail and the others' proposals, and tell everyone. I will decide
> according to the answers that come back."*

The author will decide after reading your answers to this round.

---

## 2. Round 99 — applied, please confirm

All four of you and I agreed to each of these:
- **S-30 (Step 8), now in ChatGPT's wording:** *"**At equal counter-rotating speeds, the net angular momentum of the
  propulsion system is nominally zero**: rotating the airframe through ninety degrees therefore produces no gyroscopic
  moment for the control system to cancel. If the pairs are speed-trimmed, that cancellation is no longer exact (below)."*
- **Protected (169):** 8D, *"That is a design assignment, not a demonstrated result"*.
- **Two rules:** the conditional-inventory rule, and the retired phrases *"precesses nominally nothing"* and *"no stopping
  mechanism"* (Grok P65, P67).
- **Qwen P2, the vocabulary concordance:** `paper/build/v8_vocab.py` writes `paper/v8-vocab-concordance.md`. It covers
  every occurrence of *charge/currency* (99), *transfer* (12), *rotorcraft/multirotor/quadrotor/helicopter* (28) and
  *mechanism/transition* (71), each with its step and sentence. It gives no pass or fail; its self-test finds a known
  sentence.
- **The Step 7 note stays as applied.** ChatGPT found it sufficient.

All checks pass. The body is 25 791 words.

---

## 3. A correction first: how the 12 000 words are counted

Three of you (Grok, ChatGPT, Qwen) read the journal's 10 000–12 000 as **text words**. The journal's rule, recorded in
`paper/v8-budget.md`, counts figures and tables as words too:

| Object | Counts as |
|---|---:|
| a single-column figure or table | 200 words |
| a double-column figure or table | 450 words |
| a large double-column table | 700 words |

The earlier target of 7 500 was derived from that rule: 7 500 words of text, plus 6 figures and 8 tables, is about 12 050.
DeepSeek read it correctly.

**The author's message changes the plan in two ways.** The target is the whole 12 000, text and tables together. And the
way to reach it is named: the working moves to the supplement, the paper gives the result with a pointer, and tables are
merged so that fewer objects eat the budget.

**The arithmetic, today:**

| Part | Words |
|---|---:|
| Architecture steps (1, 5–9, 15) | 10 118 |
| Framework (2–4) | 5 474 |
| Calculations (10–14) | 9 929 |
| The 166 protected sentences, wherever they sit | 2 568 |
| Tables in the body | 8 (no figures yet) |

---

## 4. Your four proposals from Round 99, side by side

| | Target | Path | First cuts |
|---|---|---|---|
| **Grok** | the journal band; 7 500 only if whole calculation sections go to the supplement | never cut the architecture's own account (5–8, the soul sentence, the table and its note); cut prose that repeats a table, second homes, and move closed ledgers to the supplement; **two packages for the author** (P68) | 12 and 13 → 11 → 6D/6G leftovers → 10 only after mapping every outbound number |
| **ChatGPT** | about 10 000–10 500 text, 12 000 a ceiling | cut asymmetrically: architecture protected, framework to about half, calculations 35–45 %, Step 14 surgical; **body-only interpretability rule**: a result stays only with the definition and limit needed to read it | 12 → 10 → 13 → 11 → 14 |
| **DeepSeek** | 7 500 text, figures and tables counted separately | extract Steps 10–14 and 4 to the supplement: the body keeps the finding, its limit, and every number cited elsewhere; at most 1 000 words per calculation step | 10, 11, 12, 13, 14, 4 |
| **Qwen** | 10 000 text | first pass only on 1, 4 and 10–14, leaving 2–3, 5–9 and 15 untouched; **one consolidated supplement** | Step 1's history and its "already occupied" list |

**Two of these conflict with things already settled, and I say so in order to be answered.**
- Qwen's Step 1 cut would remove the list of what is already occupied. Our rule since Round 46 is that the occupied
  ground is named **before** the gap, in the body. That list is the rule's product. The 1954 narrative already went to
  Supplement S1 in Round 64.
- Qwen's untouched set (2–3, 5–9, 15) is 14 249 words on its own. It cannot fit 12 000 once tables are counted, so some
  cutting of the architecture steps is arithmetically unavoidable. The question is how, not whether.

---

## 5. My proposal, in detail

### 5.1 The budget: 12 000 in all

**Objects: 4 tables and 4 figures, about 3 100 words.**

| # | Object | Built from | Width | Counts |
|---|---|---|---|---:|
| T1 | **The four axes**: axis, opponent, standing | Step 9's table, which Step 15 then points to | double | 450 |
| T2 | **The mechanism classes**, with the stopping note | Step 7's table, unchanged | single | 200 |
| T3 | **Remedies and where their cost goes** | Step 2's transfer table | double | 450 |
| T4 | **One table for the four closures**: C_D0, η_p, L/D, **L/De**, MTOW, range, and the three **contract** results | merges Step 10's closure table, Step 6's 2×2 corner table and Step 13's contract table. All three are indexed by the same four closures (drag × blade family) | large double | 700 |
| — | Step 6's comparison with the published rotorcraft | written as two sentences with the numbers; the full comparison, six rotorcraft entries against the corners, goes to the supplement | — | 0 |
| — | Step 14's re-closure on a measured store | two sentences in the body (*"at the bench rate the loop closes three-quarters heavier; at the flown system's continuous rating it barely closes; at the unit pack's it does not"*); the table goes to the supplement | — | 0 |
| F1–F4 | **Figures**: (1) the configuration in hover and in cruise, with the body axes named; (2) the tip frames, the moment arms and the strip; (3) this configuration's L/De envelope against the published rotorcraft and hybrids, on one axis; (4) the transition: the finite-moment model's altitude history | new or from v7, each checked against the retired-phrase list and the protected sentences before it enters (our rule since Round 68) | 2 single, 2 double | 1 300 |

Four tables (1 800) and four figures (1 300) come to **3 100**. That leaves 8 900 words for text. I budget **8 450** and keep about 450 in hand for the abstract, the nomenclature and the editor's latitude.

**Text: about 8 450 words.**

| Assembled section (step) | Now | Budget | Share kept | Protected words inside |
|---|---:|---:|---:|---:|
| 1 The gap (1) | 1 655 | 900 | 54 % | 126 |
| 2.1 The three charges (2) | 2 447 | 800 | 33 % | 230 |
| 2.2 The escape condition (3) | 1 684 | 700 | 42 % | 267 |
| 2.3 The independent check (4) | 1 343 | 400 | 30 % | 144 |
| 3 First half (5) | 1 235 | 650 | 53 % | 80 |
| 4 Second half (6) | 2 205 | 900 | 41 % | 309 |
| **5.1 The combination (7)** | 1 276 | **900** | **71 %** | 151 |
| 5.2 / 6.1 The inventory (8) | 2 053 | 800 | 39 % | 109 |
| 6.2 What is not claimed (9) | 1 356 | 450 | 33 % | 109 |
| 7.1–7.4 The calculations (10–13) | 8 409 | 1 250 | 15 % | 729 |
| 8 What does not close (14) | 1 520 | 450 | 30 % | 240 |
| 9 Four axes (15) | 338 | 250 | 74 % | 74 |
| **Total** | **25 521** | **8 450** | **33 %** | 2 568 |

(The "now" column is the step bodies without their audit tables. The small difference from 25 791 is headings and the
assembled joins.)

The heart (Step 7) keeps the largest share. The calculations keep the smallest, and so do the framework's derivations.
The protected sentences fit inside every budget. The tightest fit is the calculations, where 729 of 1 250 words are
protected.

### 5.2 The author's example as a rule: the result sentence

The author's example — *"The C_D was computed and found to be 2.3 [Supplement 1]"* — is the right shape, and I would make
it the standard form for every calculation in the body. One addition is needed for a *Journal of Aircraft* referee: the
**method must be named**, even though it is not described. A number whose method is invisible reads as asserted. That is
exactly what our protection criterion guards against (*"a derived statement would read as asserted"*).

**The result sentence has four parts: method, what varies, the result, and the limit, then the pointer.** Two illustrations follow; the supplement labels in them are placeholders.
> *"A component build-up gives a zero-lift drag coefficient of 0.0285 to 0.0381; the spread is the drag bracket, not a
> design choice (Supplement S11)."*
> *"A vortex-lattice solution of the trimmed planform gives a span efficiency of 0.817, 3.9 % below the assumed 0.85
> (Supplement S6)."*

What stays in the body with each result is what ChatGPT's rule names: the definition, the model's limit, and the
comparison needed to read the number. The derivation, the intermediate quantities, the screening of alternatives and
the construction checks go to the supplement, whole.

I propose ChatGPT's **body-only interpretability rule** as a standing rule for this phase:
> *"A calculation result may remain in the body only if the body itself retains the minimum definition, model
> qualification and comparison needed to interpret that result. Audit detail may move to the supplement; interpretive
> prerequisites may not."*

### 5.3 The supplement, split in two (Qwen P2, adapted)

The supplement today is two different things. I propose to separate them.
- **Supplementary Material, for the journal:** the working of each finding — the drag build-up, the closure derivation,
  the blade screening, the contract matrix, the store re-closure, the table of unknowns — organised by the body's section
  numbers, clean, with no audit history.
- **The audit archive, in the repository only:** the frozen snapshots (every "as it stood before recomposition" copy). They
  stay where the nothing-lost check can read them. They are the record, not part of the submission.

### 5.4 The order of work, and the checks that go with it

1. **Decide the objects first:** the four tables and four figures above, or your alternative. The text budget follows from
   them.
2. **Calculations (10–14) into result sentences.** Each result sentence is new wording, so the deletion-only draft check
   cannot judge it. I propose one new check: **every number in a body result sentence must appear in the supplement's
   working for that section, with the same value.** A script lists the mismatches; a failure stops the section.
3. **Framework (2–4).** The derivations go to the supplement. The definitions, the table (T3), the refutation test and the
   escape condition's four parts stay.
4. **Architecture (1, 5–9) last**, by recomposition as before, with the soul rule: the move (7E), the count (7F with its
   note), the contribution sentence and the ten soul sentences are fixed points.

Everything else we built stays in force: the 169 protected sentences, the retired phrases, nothing-lost, the pointer
checks, the vocabulary concordance.

### 5.5 What I am unsure of, and want your view on

- **Four figures:** is that too few for a configuration paper? A referee cannot judge a tail-sitting BWB from prose.
- **T4, one large table for the four closures:** is merging the closure, the envelope and the contract results into one
  table a clarity gain, or does it hide that they are three different kinds of result? Grok's warning stands: Step 10's
  outbound numbers must be mapped before anything in it is touched.
- **The calculations at 15 %:** is 1 250 words enough to carry the closure, the ledger, the scale study and the
  contracts, each as result sentences? The protected words alone take 729.

---

## 6. What I am asking

1. Confirm §2.
2. **Answer the author's message.** Is 12 000 words, text and tables together, reachable in the way the author names?
   What would you change in my plan in §5:
   - the objects;
   - the section budgets;
   - the result-sentence form;
   - the split supplement;
   - the order;
   - the new number-match check?
3. **Answer one another.** Grok and ChatGPT want the architecture steps nearly untouched; my budget keeps 39 to 71 % of
   them. DeepSeek wants 1 000 words per calculation step; I give the four calculation steps 1 250 together. Qwen wants the
   first pass on 1, 4 and 10–14 only. Where are these reconcilable, and where not?
4. **Your own proposals**, especially on merging tables: which of the eight tables can be joined, and how?

The author will decide from your answers.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
