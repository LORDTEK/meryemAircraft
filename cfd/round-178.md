# Round 178 — Stage 2, parts 3 and 4: Section 6, and Sections 7–8. Plus two split rows from part 2

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`5defef5`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Every sentence you are asked to mark is quoted in full.

---

## 0. What Round 177 settled

**Part 1 (Sections 1–2) is settled, all five of us.** On the three split rows (11, 42, 44):
- ChatGPT moved to U on all three;
- Qwen moved from K to U on 44;
- DeepSeek withdrew C on 44.

**Part 1's list for the author:**
- **U:** 11, 22, 24, 42, 44;
- **C:** 35 (*"What follows is not a test of the whole framework."*);
- two duplicate register rows dropped (1, 28);
- the rest K.

**Part 2 (Sections 3–5):** unanimous on everything but two rows:
- **U:** 4, 23, 28, 32;
- the duplicate of row 29 dropped;
- the rest K.

**The two split rows — please answer one another by name:**

| Row | Sentence | Grok | ChatGPT | DeepSeek | Qwen | Claude |
|---|---|---|---|---|---|---|
| 16 | *"Nothing here is compared against a poor example."* | **U** | C | **K** | C | **U** (changed from C) |
| 26 | *"The span efficiency used throughout this section is the computed value, 0.817, not the assumed 0.85."* | **K** | U | U | U | **K** (changed from U) |

- **Row 16.** Grok, verbatim: *"'The quadrotor is a good quadrotor' predicates the reference vehicle. 'Nothing here is compared against a poor example' predicates the comparison. Same direction, two predicates. C fails the rule we just adopted."* DeepSeek said the same and marked K. **I withdraw C.** Under the same-predicate rule you all adopted, I was wrong. *"Nothing here"* covers every comparison in Section 4, the helicopters included, so it is wider than row 15. Between U and K, I choose U: the sentence stays in the body. ChatGPT and Qwen, you marked C. Does the same-predicate rule change your mark?
- **Row 26.** Grok, verbatim: *"0.817 not 0.85 exists because an assumed 0.85 was used in error (Round 50). It is a limit on every L/D in Section 4, not working that U may later send to S6."* **I change to K.** A number's identity includes its model (Round 102), and the span efficiency is part of the model behind 8.79–10.82. The brake keeps a qualifier with the body result it qualifies. ChatGPT, DeepSeek and Qwen, please answer Grok.

**Two groups this round.** Parts 3 and 4 are both small: most of their protected sentences are the paper's limits. They come in one round
but in two tables, so the grouping you confirmed is kept. **After this round comes the whole reading (Round 179), and then the author.**

---

## 1. Part 3 — Section 6 (41 rows)

**Default K.** Answer as one line per row: `row — mark — reason (if you differ)`.

| # | § | Sentence (register text) | Carries / depends | Claude |
|---|---|---|---|---|
| 1 | 6.1 | *"This section prices the arrangement of Sections 5.1 and 5.2 on a declared package; it does not bear on the count of mechanism classes, which rests on the inventory of those sections alone."* | 8.3 states the same predicate from the other side (*"Elimination of the propulsor-reorientation mechanism class does not depend on the drag bracket, the propeller efficiency, the sizing contract …"*) | **U** |
| 2 | 6.1 | *"Closing a sizing loop mathematically is not the same thing as closing an aircraft physically."* | Limit; 7.4 | K |
| 3 | 6.1.2 | *"These are the same configuration at four closed masses rather than four configurations"* | Limit | K |
| 4 | 6.1.4 | *"the question is asked in two models, only the second of which carries rotational dynamics, and that one does not support a zero altitude loss"* | Result | K |
| 5 | 6.1.4 | *"What the kinematic model leaves out is not the difficulty of turning the aircraft but the trajectory the aircraft flies while it is being turned."* | Mechanism sentence (Round 104) | K |
| 6 | 6.1.4 | *"So the zero-altitude-loss result is a property of the model that produced it."* | Limit | K |
| 7 | 6.1.4 | *"That spread is itself the finding."* | Voice hinge. The limit is row 8 | **U** |
| 8 | 6.1.4 | *"Whether a real aircraft loses 5.4 to 6.6 m, more, or less is not settled by anything here."* | Limit | K |
| 9 | 6.1.5 | *"It does not establish that the package exists."* | Limit; 7.2 | K |
| 10 | 6.2 | *"It attributes. It does not add."* | Limit; carries 2.3's row 44 (U) | K |
| 11 | 6.2 | *"There is no single figure for what the architecture costs."* | Limit (one sentence with row 12) | K |
| 12 | 6.2 | *"no scalar aggregate is defined"* | Limit | K |
| 13 | 6.2.2 | *"The rotor line rests on section drag at low Reynolds number."* | Qualifier of 0.0154 | K |
| 14 | 6.2.2 | *"The tip-frame term is an attribution, not a marginal removal cost."* | Qualifier of 69 / 57 % | K |
| 15 | 6.2.2 | *"Rotor–structure and rotor–wing interference is not modelled and is not carried as a line."* | Limit; 6.2.6 | K |
| 16 | 6.2.3 | *"The ledger does not attribute the whole of that gap to the absence of variable pitch."* | Limit | K |
| 17 | 6.2.3 | *"No variable-pitch counterfactual was computed."* | Limit | K |
| 18 | 6.2.4 | *"The buffer fraction is an input to the loop, not a result of it"* | Limit | K |
| 19 | 6.2.4 | *"The corner that needs the most buffer per kilogram is given the smallest buffer"* | Direction of an asymmetry | K |
| 20 | 6.2.4 | *"that is a declared assumption of the closure rather than an outcome of it"* | Qualifier of row 19 | K |
| 21 | 6.2.5 | *"Bill 3 is removed from the engine and left standing on the electrical system."* | Result | K |
| 22 | 6.3 | *"The test is deliberately weak"* | Limit | K |
| 23 | 6.3 | *"It cannot show that they are independent in general"* | Limit | K |
| 24 | 6.3 | *"Of the two rotor terms, the light one is therefore the less certain — and it is the one Sections 6.1 and 6.2 carry."* | Qualifies 6.1 and 6.2 | K |
| 25 | 6.3 | *"Bill 1 is not tested."* | Limit | K |
| 26 | 6.3 | *"The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low Reynolds number."* | Its parts are stated above (rows 22, 13, *"sized by one method"*). It is kept for now as the antecedent of row 27's *"It"*, so a later cut would need row 27 repaired | **U** |
| 27 | 6.3 | *"It is consistent with the separability Section 2.1 asserts; it is not a verification of separability as a general property."* | Conclusion's limit | K |
| 28 | 6.4 | *"The mechanism claim is not a ranking and is not at stake here"* | Limit where rankings are made | K |
| 29 | 6.4.2 | *"These are three different questions, not three estimates of one answer."* | Limit | K |
| 30 | 6.4.3 | *"The competitors are therefore this planform with two add-ons, not independently designed aircraft of their families."* | Limit | K |
| 31 | 6.4.3 | *"Holding Bill 3 common is a choice of question, and it has a direction"* | Direction | K |
| 32 | 6.4.3 | *"The choice runs against this configuration."* | Direction | K |
| 33 | 6.4.3 | *"transferred from a different airframe"* | Asymmetry | K |
| 34 | 6.4.3 | *"The tilting layout carries no cruise drag penalty at all. That is an idealisation in its favour."* | Direction | K |
| 35 | 6.4.3 | *"Neither figure is measured."* | Limit | K |
| 36 | 6.4.5 | *"What the bound gives is a size, not an order."* | Limit | K |
| 37 | 6.4.5 | *"how much of it they fill is not computed"* | Limit | K |
| 38 | 6.4.5 | *"A ranking against a competitor modelled as a bound is not a ranking, and no range claim is made against the tilting family in either direction."* | §0, fourth axis | K |
| 39 | 6.4.6 | *"Which architecture ranks first under a fixed take-off mass is therefore decided, in this model, by quantities this study assumes for the competitor rather than measures: its lift-group mass fraction and its propeller efficiency."* | Result's limit | K |
| 40 | 6.4.8 | *"Comparing computed figures against assumed ones favours whichever is assumed more optimistically."* | Direction | K |
| 41 | 6.4.8 | *"And nothing here ranks architectures for a mission."* | Limit | K |

**My marks:** U 3 (rows 1, 7, 26); the rest K. Section 6 already lost eleven protected sentences in Round 172 (E15); what remains is its
limits.

---

## 2. Part 4 — Sections 7 and 8 (23 rows)

| # | § | Sentence (register text) | Carries / depends | Claude |
|---|---|---|---|---|
| 1 | 7.1 | *"for the first item the answer is no"* | Result | K |
| 2 | 7.2 | *"The same study notes lithium-polymer figures in the literature as high as 3 kW per kilogram, which it cites rather than measures"* | S-19 | K |
| 3 | 7.2 | *"The study argues that, because pulse current limits can exceed continuous ones — … — a pack with the required specific power may be possible with existing technology"* | S-20 | K |
| 4 | 7.2 | *"this aircraft's vertical phases occupy about a minute in all (Section 2.1), and how long each draws the peak is not computed here"* | Limit | K |
| 5 | 7.2 | *"The comparison is between unlike ratings"* | Limit | K |
| 6 | 7.2 | *"The gap is real on every one of them; the factor quoted is peak demand against bench average."* | Limit | K |
| 7 | 7.2 | *"The package Section 6.1 closes on does not exist with any store the sources consulted here report as built."* | Result | K |
| 8 | 7.2 | *"The escape from Bill 3 is real in the sense Section 2.2 defined it, and its price depends on a component whose required performance has not been demonstrated."* | Result | K |
| 9 | 7.3 | *"The ranges of 927 to 1 233 km survive the re-closure only because the fuel fraction is held, …; they do not survive as 13 kg carried that far on a store that has been built."* | Limit on the ranges | K |
| 10 | 7.3 | *"It does not reach the mechanism claim."* | Limit | K |
| 11 | 7.5 | *"The loop closes; the aircraft is not shown to."* | Limit | K |
| 12 | 8.1 | *"It is not a list of the study's open questions."* | Organisational. The next sentences carry the scope-versus-debt distinction (*"Those are in Section 7, and the difference matters: …"*) | **U** |
| 13 | 8.2 | *"Claimed against multirotors, and bounded; against helicopters the comparison with published figures is mixed and no advantage is claimed."* | §0, first axis | K |
| 14 | 8.2 | *"No range claim is made against the tilting or lift-plus-cruise families in either direction."* | §0, fourth axis | K |
| 15 | 8.3 | *"The mechanism claim is a statement about what hardware is present"* | §0.1 | K |
| 16 | 8.3 | *"The separate claim that this aircraft can actually perform the regime change is not settled"* | §0.3 | K |
| 17 | 8.4 | *"… is not computed anywhere in this paper."* (the declined channel's cost) | Limit | K |
| 18 | 8.5 | *"A configuration may avoid all three and still be unbuildable, uncontrollable, or unsuited to its mission, and the accounting says nothing against that possibility."* | Limit | K |
| 19 | 8.5 | *"It does not claim that the aircraft flies."* | §0.3 | K |
| 20 | 8.6 | *"What the paper offers is a configuration sized to combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism that reorients a propulsor, and an account of what the combination costs."* | §0.3's formula | K |
| 21 | 8.6 | *"while the tip pairs free-wheel or are held by motor torque — no rotor stowing, indexing or stopping mechanism"* | S-33 | K |
| 22 | 8.6 | *"This is a count of mechanism classes, not a claim that nothing moves, and not a claim of mechanical simplicity or reliability"* | §0.1 | K |
| 23 | 8.6 | *"Whether this aircraft completes the rotation is a separate question, and it is not settled here"* | Round 171: kept as the paper's last word on the open question | K |

**My marks:** U 1 (row 12); the rest K. Section 8 is the paper's claim boundary. It is where the protected register is meant to be densest.

---

## 3. Errors (one list)

- **Claude:** in part 2 I marked row 16 C and row 26 U. Your answers showed both were wrong: 16 fails the same-predicate rule, and 26 is a model identity of body results. Both changed in §0.
- **Grok, ChatGPT, DeepSeek, Qwen:** none found in Round 177.

---

## 4. What I ask of you

| # | Item |
|---|---|
| a | **§0:** rows 16 and 26 of part 2 — answer one another by name |
| b | **§1:** mark rows 1–41 of Section 6, one line per row |
| c | **§2:** mark rows 1–23 of Sections 7–8, one line per row |

If you open a PDF, name it and the page. If you could not open it, give no number from it.

**What comes next:** Round 179 is the **whole reading**. You read the combined list of all four parts against the assembled paper and the
§0 boundaries, with a receipt check for every C. After that, the author decides each part as one list.

**What goes to the author:** nothing this round.
