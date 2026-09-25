# Round 74 — the method is accepted, with your changes; the pilot begins with Step 4's inventory only; please confirm or add to it

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`bc5f64a`**. Step 4 is unchanged
> (`paper/v8/04-the-independent-check.md`, body 1 586 words). New: `paper/v8/drafts/04-inventory.md` SHA-256 `13d9dbc8273991aa1110f26f3165647b60a3e47e027aea75d6680dcdf3af2d97`.

---

## 1. Closed

**1.1–1.3 confirmed by all four of you:** the 5.4 m qualification in Step 11, the protected Step 10 verdict (152), and
Step 10 at 2 498 words with the vetoed passages standing.

## 2. The method, as you amended it

All four of you accepted, each with changes. **Where your changes pull in different directions, I took the stricter one**
and say so below. The author's condition, *"if they accept, let us begin"*, is met, so the pilot begins, and it begins with
**the inventory only** (Grok P16).

**The unit (ChatGPT, Grok).** One **finding-block**: a finding together with the minimum local evidence and qualification a
reader needs to see why it follows. Steps 2–4 may later live under one heading, but they are drafted block by block, never
in one pass (Grok's change 1; Qwen's single section survives as the heading).

**The inventory (ChatGPT, Grok, DeepSeek, Qwen)** is a table: finding; numbers (E1); the inferential evidence that makes the
numbers support the finding (E2); qualifications; forbidden predicates; and **outbound dependencies** (Qwen). **Any of you
can add a row before the draft; a rejected addition is recorded with its reason** (DeepSeek).

**Tags (ChatGPT, Qwen).** **P** protected, verbatim. **D** deletion only, checked mechanically. **J** a join that introduces no
factual predicate, causal relation, scope or evaluation, and uses only verbs of location, sequence or attribution (*tests,
follows, is examined in, is carried to*); a J with a causal or evaluative verb is R. **R** new wording, vetoed sentence by
sentence. **Untagged counts as R.**

**Predicate ledger for every R (ChatGPT):** source predicate → new predicate, and the new one may not be broader. *"The
finite-moment model gives 5.4 m"* → *"the transition loses 5.4 m"* would fail it.

**Trace table (DeepSeek, ChatGPT, Grok):** one row per source sentence, with its status, its destination, its **evidence role**
(finding, evidence, qualification, bridge, background, transition) and, for every number, **its object**: which aircraft,
which model, which contract (Grok P17).

**Supplement snapshot (ChatGPT):** the whole of Step 4 goes to S4 first, and the snapshot is frozen for the pilot.

**Review order (Qwen, DeepSeek):** inventory, then trace table, then draft, so that the fluency of new prose does not decide
the reading.

### Stop criteria — the stricter of your proposals

| Halt the pilot | Continue |
|---|---|
| Any stronger predicate (all four) | Joins that state no fact |
| Any dropped number that another section or the finding's own evidence needs (Grok, ChatGPT, Qwen) | One broken antecedent, repaired in the same round and counted (Grok, ChatGPT) |
| A number that survives but has shed its model, geometry or object (Grok, ChatGPT) | |
| An invented causal relation or evaluation (ChatGPT) | |
| A first occurrence that moved: a later sentence becomes the first unexplained use of a concept (Grok) | |
| **"Compressed but unbelievable"**: a finding stays but its minimum local evidence has gone entirely to the supplement (ChatGPT; Grok's change 3) | |
| A second broken antecedent, even if both are repaired (Grok, ChatGPT) | |

**DeepSeek, one of your proposals is not taken, and here is why:** you would allow one repair cycle after a dropped number.
Grok, ChatGPT and Qwen would halt on it, and I side with them for the pilot, whose purpose is to find out whether the method
fails safely. **If you disagree, say so; the author decides.**

**Not a criterion:** the percentage (ChatGPT, Grok). *"38 percent with no semantic failure is a useful result; 71 percent with
lost bridges is a worse one."*

**After the draft (ChatGPT):** a **blind reconstruction**. Before you open the trace table, answer from the new body alone:
what is the finding, what supports it, what is its scope, and what does it not establish. Then a **pilot report**: words
removed by D, J and R; the number of R sentences and vetoes; and a count for each halt condition (ChatGPT, DeepSeek).

## 3. Step 4 — the inventory (the first object of the pilot)

Source: `paper/v8/04-the-independent-check.md` at commit 94b9482, body 1 586 words. **P** = protected sentence (verbatim).
E1 = numerical evidence, E2 = inferential evidence (why the numbers support the finding). Every number carries its object.

| Block | Must say (finding) | Must show — E1 | Must show — E2 | Must qualify | Must not say |
|---|---|---|---|---|---|
| **B1. Why the check, and its reach** | An accounting proposed by its users invites the objection that the charges were chosen to suit an aircraft; the answer is to test one prediction against numbers this work did not produce, before any configuration is described. | — | *"The objection arises at the title, not at the ledger, so it is answered here — before any configuration is described."* | **P** *"What follows is not a test of the whole framework."* **P** *"It checks one falsifiable consequence on one independent data set."* | That the framework is validated or proven. |
| **B2. The prediction, before the data** | Two halves: (1) a dedicated lift system pays in gross weight, amplified (multiplier on empty-mass fraction; charged again in hover); (2) the efficiency credit does not cover the payment. The check tests (2). | — | The weight charge is amplified by a multiplier while the efficiency credit enters linearly through cruise L/D — the reason to expect the outcome. A failure would not refute Bill 1 (the mass is still paid); it would refute the expectation that the amplified charge outweighs the linear credit. | **P** *"only the first is a derivation"*; **P** *"Second half, not derived."*; *"it does not prove that the credit must lose"*; **P** *"The prediction is also mission-dependent, and the page would be weaker for hiding it."* — the mission used is short; the counter-set is a longer-range common-mission study with a dedicated-lift design both more efficient and no heavier; none is known to the authors. | That the credit must always lose; that the result holds at any mission length. |
| **B3. The data** | A NASA study sizing **five VTOL architecture families, nine designs**, against one mission with common tools and assumptions; independent of this work; does not use the three-bill accounting. Chosen because it fixes the mission, applies one tool set, and reports both quantities the prediction needs. | Mission: **1 200 lb payload over 75 nautical miles**. Three designs: **turboshaft quadrotor** — effective L/D **4.9**, design gross weight **3 678 lb**, no dedicated lift group; **turbo-electric lift-plus-cruise** — **8.5**, **7 271 lb**, dedicated lift group (eight lift motors beside a cruise motor); **turbo-electric tilt-wing** — **8.6**, **6 584 lb**, none (eight proprotors, reoriented). | The reasons for choosing this study are stated *so that the choice is not merely the one that agreed*. | Effective L/D is the study's own quantity (Section 6 defines it and uses this set). | That the study endorses or uses the accounting. |
| **B4. The result** | **The isolated pair (lift-plus-cruise against tilt-wing) carries the test:** same mission, payload, turbo-electric architecture and cruising wing; the difference the comparison turns on is the dedicated lift group carried through cruise. The tilt-wing is **1.2 % better** in effective cruise efficiency and **9.4 % lighter**; the lift group buys no efficiency advantage here. The source states the second half in its own words. | Design gross weights differ by **687 lb** in the tilt-wing's favour. Weight breakdown (S4): of the **679 lb** empty-weight difference, structure **716 lb** against the lift-plus-cruise entry, propulsion returns **146 lb**, battery **10 lb**; these account for **580 lb**; **99 lb** lies in categories the table does not break out. Source quote: *"but not enough to counter the increase in structure and propulsion weight."* | The breakdown shows the transfer property of Section 2 (the mechanism giving part of the structural saving back) inside a breakdown this work did not produce — this is what makes 687 lb informative rather than merely large. | **P** *"They are not identical in every other respect … it is not a controlled experiment."* *"That figure is the net difference between two architectures, not the measured mass of a lift group."* The categories do not account for the whole difference. **P** *"The quadrotor is reported for scale, and the isolation test above is what carries the prediction"* (contrast in S4). **P** *"The framework does not predict any of these numbers; without the input fractions it predicts no magnitudes."* | That 687 lb is the mass of a lift group; that the quadrotor contrast is the test; that the comparison is controlled. |
| **B5. The tilt-wing entry** | It denies this paper a uniqueness: **the proposed architecture is not the only way to avoid the first charge** — the tilting family avoids it too, and is the lighter of the matched pair. And it shows the transfer property in someone else's data: it *moves* the charge to the mechanism that reorients its propulsors (actuation, gyroscopic coupling, transition control problem). | The efficiency margin is one tenth (8.6 against 8.5). | What separates the tilting family from the configuration described later is not this axis but what each pays, and a sizing study does not settle that. | Nothing is claimed from the direction of the one-tenth margin. | That the tilting family fails the accounting; that this paper's configuration is shown better than it. |
| **B6. What the check establishes** | One prediction of the accounting holds on data produced elsewhere; that is the whole of it. The instrument is shown working on something else before it measures the thing its authors advocate — which is why the section comes here. The instrument is then fixed. | — | — | **P** *"It does not establish that the accounting is complete … or that avoiding them makes an aircraft better."* It establishes nothing about the proposed configuration (Section 11 applies it; the answer is not uniformly favourable). | That the configuration benefits from this check. |

**Outbound dependencies (Qwen) — what other sections take from Step 4**

| Section | What it takes |
|---|---|
| Step 6 | *"The sizing set of Section 4 reports an effective lift-to-drag ratio"* — the identity of the NASA set as **the sizing set**; and *"Section 4 is where the independent sizing evidence for [the mass charge] is set out"* |
| Steps 1, 2 | Name the same NASA study on their own; they do not depend on Step 4's wording |
| Step 11 | Pointed to by Step 4 (*"where it is applied … not uniformly favourable"*); does not cite back |

**Grok P16's items are all in it:** the isolation pair (8.5 at 7 271 lb with a lift group; 8.6 at 6 584 lb with none); the
quadrotor as scale, not the test; the transfer inside a breakdown this work did not produce; the categories that do not account
for the whole difference (the 99 lb); and *"the isolation test above is what carries the prediction."*

**One thing I caught in my own first version:** for B1's inferential evidence I had written *"so the aircraft cannot have shaped
it."* That is my inference, not the source's, and it is stronger. It now quotes the source: *"The objection arises at the title,
not at the ledger, so it is answered here — before any configuration is described."* It is the kind of error the pilot exists to
catch, and it happened in the inventory.

## 4. What I am asking

1. **The method (Section 2):** is my reconciliation of your changes right? **DeepSeek** especially, on the dropped-number rule.
2. **The inventory (Section 3):** confirm, or **add rows** — a finding, a number, a piece of local evidence, a qualification or a
   forbidden predicate that is missing. Quote the source sentence for anything you add.
3. **New proposals**, as always.

**Next round**, if the inventory is confirmed: the S4 snapshot, the trace table, and the draft, block by block, in that order.

**Sources.** None of this needs a source.
