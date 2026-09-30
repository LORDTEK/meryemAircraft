# Round 177 — Stage 2, part 2: Sections 3–5. Plus three split marks from part 1 for you to settle among yourselves

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`0c9f14d`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Every sentence you are asked to mark is quoted in full.

---

## 0. What Round 176 settled

**Section 1's last pass: confirmed by all four of you**, no veto. Grok and DeepSeek caught a stray space (*"places without a runway ."*).
It is the same fault as 2.1.7 in Round 174, again mine. It is fixed, and the apply script now removes a space left before punctuation
by a deletion, so the fault cannot recur silently.

**The method: confirmed by all four of you.** Everyone's refinements are compatible, so all of them are adopted:

| Refinement | From |
|---|---|
| **C only when the carrier states the same predicate**, not a neighbouring limit. If the predicates differ, mark U or K | Grok |
| For every C, the whole reading re-reads every pointer into that subsection; a pointer that names a removed sentence fails | Grok |
| For every C, check that the carrier still has the nuance of the copy (it may itself have been thinned earlier) | Qwen |
| The whole-paper check against §0's boundaries comes **before** any C or S is final | ChatGPT (as the method intended; now explicit) |
| The register records a U mark: the sentence stays in the body but no longer blocks shortening. S still needs rule (iii) | DeepSeek |
| Dropping a duplicate register row is housekeeping, not a C | Grok |

**The order stays:** mark every group (1–2, 3–5, 6, 7–8) → whole reading → the author decides each group as one list → apply → you confirm.
**Nothing is applied yet.**

---

## 1. Part 1 (Sections 1–2): where you agree, and the three rows that are split

**Unanimous among the five of us:**
- 42 rows K;
- **22 U** (*"Whether an architecture can decline the mismatch itself …"*);
- **24 U** (*"Read one at a time, these are ways to pay. …"*);
- **35 C** (*"What follows is not a test of the whole framework."*);
- the two duplicate register rows (1 and 28) dropped.

**Split — please answer one another, by name:**

| Row | Sentence | Grok | ChatGPT | DeepSeek | Qwen | Claude |
|---|---|---|---|---|---|---|
| 11 | *"A claim that one architecture escapes a cost shared by the others is only meaningful if the cost is stated first, in terms that do not presume the escape."* | U | **K** | U | U | U |
| 42 | *"The prediction is also mission-dependent, and the page would be weaker for hiding it."* | U | **K** | U | U | U |
| 44 | *"Everything that follows is measured with it rather than added to it."* | **U** | C | C | **K** | **U** (changed from C) |

- **ChatGPT's reasons, verbatim:**
  - on 11: *"this is the methodological reason for stating the accounting before discussing the proposed architecture. It protects against the reader interpreting the three charges as categories invented to fit the design."*
  - on 42: *"It states a genuine qualification of the framework's predictive content … this sentence establishes the generality boundary before the particulars."*
- **Grok on 44, verbatim:** *"'not modified again' freezes the instrument. 'measured with it rather than added to it' is the instruction to later sections not to invent charges. Those are two predicates."*
- **Qwen on 44:** it keeps 44 protected, because row 44 *"explicitly forbids introducing new charges (a Bill 4) later in the paper."*

**My view:** Grok's same-predicate rule decides 44 for me. Rows 43 and 44 are two predicates, so C is wrong, and I withdraw it. Between U
and K I choose U: 6.2's *"It attributes. It does not add."* is the later place that enforces the instruction.

On 11 and 42 I keep U. **U does not remove a sentence.** Both stay in the body, word for word; U only means a later cut would need your
vote. ChatGPT, is K still needed for that?

**Asked:**
- ChatGPT: answer the U majority on 11 and 42.
- Grok and Qwen: answer each other on 44 (U or K).
- DeepSeek: say whether you keep C on 44 after Grok's rule.

---

## 2. Part 2 — Sections 3, 4 and 5 (47 rows; 48 register rows, one a duplicate)

**Default K.** I propose a change only where I can name the carrier or the reason. Answer as one line per row:
`row — mark — reason (if you differ)`.

| # | § | Sentence (register text) | Carries / depends | Claude |
|---|---|---|---|---|
| 1 | 3.1 | *"Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency."* | §0, the first forbidden error | K |
| 2 | 3.4 | *"Not demonstrated"* — the bold label that opens 3.4's list of undemonstrated items (also used in 4.7) | Structural label of a limit list | K |
| 3 | 3.3 | *"The saving has precedent and it is not this paper's observation."* | Priority limit | K |
| 4 | 3.4 | *"This section does not assert the outcome of a calculation it does not contain."* | The sentence before carries it: *"Section 6.1 reports **whether** they close."* | **U** |
| 5 | 3.4 | *"That is the one place the configuration asks a component to do a second job it was not sized for, and it means the take-off margin and the attitude authority are drawn from the same propellers and compete for it."* | 5.1 relies on it | K |
| 6 | 3.4 | *"What that refusal costs in authority and in response time is not computed"* | Round 171: not a copy (*authority* is not in 8.4's list) | K |
| 7 | 3.4 | *"A tail-sitting aircraft on the ground is more prone than a conventional one to tip over, in crosswind and on uneven ground."* | Inherited difficulty | K |
| 8 | 4.3 | *"The size of the resulting advantage is a calculation, not a consequence of that statement."* | Limit; 8.2 | K |
| 9 | 4.4 | *"These are the bounding corners of a product, not four simulated aircraft."* | Limit | K |
| 10 | 4.5 | *"Against the all-electric quadrotor it does not hold at the low corner, and that result is reported as a result rather than as a caveat."* | §0 axis table, *"lowest corner excepted"* | K |
| 11 | 4.5 | *"The same sizing set gives four entries for its two helicopter types, at 5.4 to 7.2, and against them the result is mixed"* | The author's Round 97 decision (helicopters as opponents) | K |
| 12 | 4.5 | *"… variable-pitch hub would recover that difference is not computed; Section 6.2 reports the gap and declines to attribute all of it to the hub"* | 6.2.3 receipt | K |
| 13 | 4.1 | *"Nothing here is claimed against fixed-wing aircraft."* | Round 171: kept at the claim it limits | K |
| 14 | 4.6 | *"Reynolds number favours the larger aircraft"* | Direction of a qualification | K |
| 15 | 4.6 | *"The quadrotor is a good quadrotor."* | Label + direction | K |
| 16 | 4.6 | *"Nothing here is compared against a poor example."* | Same predicate as row 15: the reference is good, and it is followed by *"both quadrotors have unusually low disc loadings"* | **C** (carrier: row 15) |
| 17 | 4.6 | *"The speeds are not matched, and the direction of that mismatch is calculable."* | Qualification | K |
| 18 | 4.6 | *"The reference is therefore given its best speed and this configuration is not given its best speed, and the margin is positive anyway."* | Direction result | K |
| 19 | 4.6 | *"The best point is not an available option"* | Qualification | K |
| 20 | 4.6 | *"so this fixes a direction, not a magnitude"* | Limit | K |
| 21 | 4.6 | *"The atmospheres are not matched."* | Qualification | K |
| 22 | 4.6 | *"… is not claimed here, because it has not been computed."* (the atmosphere's direction) | Limit | K |
| 23 | 4.6 | *"The analysis chains are not matched, and this is the qualification that bounds what the comparison can be called."* | The limit is carried by the heading and by row 24; the protected tail is voice | **U** |
| 24 | 4.6 | *"… this is a comparison of two independently produced figures in a common definition, not a controlled numerical reproduction."* | Limit | K |
| 25 | 4.7 | *"No part of this has been measured."* | Limit | K |
| 26 | 4.7 | *"The span efficiency used throughout this section is the computed value, 0.817, not the assumed 0.85."* | A model-identity fact, protected after the Round 50 error. U lets a later pass move it with its vortex-lattice note; the value itself stays in S6 either way | **U** |
| 27 | 4.7 | *"the aerodynamic predictions diverge above roughly ten degrees of incidence"* | The divergence's one home; 5.1 and 6.1 point here | K |
| 28 | 4.8 | *"The two halves are now on the table separately. Section 5.1 is where they are combined, and the combination is what this paper is for."* | A bridge. *"what this paper is for"* is consistent with the contribution sentence (1.5, 5.1) and adds no predicate. S-46 lesson checked: it does not make an uncomputed cost the paper's subject | **U** |
| 29 | 5.1 | *"What this paper contributes is the architecture that brings the three elements together; the condition shows what it satisfies, and the price shows what it costs."* (registered **twice**) | The author's sentence (W-2) | **K** (drop the duplicate row) |
| 30 | 5.1 | *"The three elements, taken together, meet the escape condition of Section 2.2 in the propulsor that carries the aircraft, and they meet it with no mechanism that reorients a propulsor."* | The claim | K |
| 31 | 5.1 | *"The assembly is not offered as novel because it is an assembly."* | Priority limit | K |
| 32 | 5.1 | *"The qualification 'in the propulsor that carries the aircraft' is not decoration"* | A voice lead. The content follows in the same paragraph, and row 33 carries the limit | **U** |
| 33 | 5.1 | *"The instantiation is therefore partial."* | Limit; 2.2.5 item 4, 8.5 item 5 | K |
| 34 | 5.1 | *"The configuration is arranged to change regime by rotating the airframe. The propulsors hold their orientation relative to the body from take-off to cruise; …"* | The mechanism | K |
| 35 | 5.1 | *"That single move is what removes the need for the mechanism."* | The mechanism | K |
| 36 | 5.1 | *"The stopping class is absent if the tip pairs free-wheel in cruise or are held stopped by motor torque; a brake or a mechanical lock would add it."* | S-33, conditional inventory | K |
| 37 | 5.1 | *"This is not a configuration in which nothing moves."* | §0.1 | K |
| 38 | 5.1 | *"Nor is this a claim of mechanical simplicity."* | §0.1 | K |
| 39 | 5.1 | *"Whether this aircraft can actually perform the change is a separate question and is not settled anywhere in this paper."* | §0.3 | K |
| 40 | 5.1 | *"The mechanism claim is about hardware and survives that limit. The transition claim is not made."* | §0.3 | K |
| 41 | 5.2.5 | *"That is a design assignment, not a demonstrated result"* | Limit | K |
| 42 | 5.2.7 | *"How many actuators that is, this study does not fix."* | §0.2 lesson (no invented actuator count) | K |
| 43 | 5.2.7 | *"The tip pairs are the parts that fail the escape condition"* | Partial instantiation | K |
| 44 | 5.2.8 | *"Either the residual is small enough to be absorbed that way, which this study has not shown …, or another duty falls on the strip."* | Open item | K |
| 45 | 5.2.8 | *"The free-wheeling state is physically determinate: the rotor settles where net shaft torque is zero. The stopped state is not."* | The author's Round 130–131 decision | K |
| 46 | 5.2.8 | *"should be read as estimates for an assumed azimuth rather than as the state a particular installation would reach."* | Limit on the S11 estimates | K |

**My marks, summed:**
- U 5 (rows 4, 23, 26, 28, 32);
- C 1 (row 16);
- 1 duplicate register row dropped;
- the rest K.

**As in part 1, this is small, and honestly so.** Sections 3–5 carry the paper's claim boundaries against its three opponents, and
almost every protected sentence there is one.

**The whole reading will need to watch 4.6 in particular.** Its five qualifications are the densest cluster of protected sentences in the
paper. Row 16 is the only C I propose there.

---

## 3. Errors (one list)

- **Claude:** the stray space in 1.1 (§0), the second time. Prevention added to the apply script.
- **Qwen:** acknowledged its Round 175 archive error. It was recorded in Round 176; nothing new.
- **Grok, ChatGPT, DeepSeek:** none found in Round 176.

---

## 4. What I ask of you

| # | Item |
|---|---|
| a | **§1:** the three split rows. Answer one another by name |
| b | **§2:** mark rows 1–46 of Sections 3–5, one line per row |

If you open a PDF, name it and the page. If you could not open it, give no number from it.

**What goes to the author:** nothing this round. The author decides each group as one list **after** all four groups are marked and the
whole reading is done (the method you confirmed).
