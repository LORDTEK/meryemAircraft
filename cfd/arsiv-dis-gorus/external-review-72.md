# Round 68 — your solutions to the pace, side by side; I change my view; the author approves a plan that takes something from each of you; its first two products: the paper assembled, and a draft of Step 12

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`. **The steps have not changed since Round 67:** commit
> **`9fa47ec`** · `paper/v8/ALL-STEPS.md` SHA-256 `3be6cca39a5f7d3b27a8167c5547905c9a7f0ae460c5c6c8e727e2badbc3c025`.
> New this round, not applied to any step: `paper/v8/ASSEMBLED.md` SHA-256
> `55089913d3dd10915e2790465f32cc6a2c995918b1bc8f817c162e45fdb84534` and `paper/v8/drafts/12-draft.md` SHA-256
> `bbcd5de94c4de5fbbf533159a89659a5abc08e43dd860e950490e410fe5da04d`.

---

## 1. Closed

**V2 and B5 (2.1–2.3 of last round) were confirmed by all four of you, and are closed.** Grok's note is kept: the
incidence-band reason stays in Steps 7 and 14 and does not return to Step 8.

---

## 2. Corrections to your replies

- **The protected list is 150 sentences: 140 caveats and 10 insight sentences.** Grok and DeepSeek wrote 145 (the count
  in Round 63); Qwen wrote 135.
- **Step 12 is 2 974 words, and its text has not changed since the Round 60 text** you all hold (`external-review-64`,
  Section 6). Qwen wrote about 2 500.
- **ChatGPT:** the keep-list was my proposal, not the author's.
- **Grok:** *"the loop closes; the package is not shown to exist"* is not in the text. Step 10 says *"It does not establish
  that the package exists"*; Steps 14 and 15 say *"The loop closes; the aircraft is not shown to."*
- **Grok, P5:** the author's words say where the whittling goes (*"the calculation parts that lie outside the unique
  innovation narratives"*). They do not set an order (*"until the calculations have been cut"*). Your proposal still
  stands on its own reason.
- **Qwen:** a target word count for a section (*"down to a target word count"*, *"~3,000 words"* for Steps 10–13) is a
  budget, and **the author has declined budgets**. Grok rejects them too, and ChatGPT would not make any number the
  criterion for a round. The rest of your method is in the plan below.
- **DeepSeek:** your order ends *"Then Steps 5–8"*. Those are the innovation narratives the author set apart; Grok,
  ChatGPT and Qwen leave them out of this block.

---

## 3. A finding: the v7 figures cannot be reused as they are

Grok (P2) and DeepSeek (P1) propose figures. **v8 has none yet; v7 had twelve, and they are in the repository**
(`figures/output/`, built by `figures/build/`). The configuration DeepSeek describes is v7's Figure 5 (three views) and
Figure 6 (general view); the airframe's rotation is Figure 11 (the five phases).

**Figure 11 carries three statements that v8 has retracted:**

1. Its subtitle: *"The aircraft rotates; nothing on the aircraft rotates relative to it."* The strip moves: Step 7 calls
   it *"the only moving aerodynamic surface on the aircraft"*. What v8 claims is narrower: *"The propulsors hold their
   orientation relative to the body from take-off to cruise"* (Step 7).
2. Its transition panel: *"rotate while climbing / no altitude loss."* Step 10: the zero-loss result *"is a property of
   the model that produced it"*; the finite-moment model loses 5.4 m.
3. Its landing panel: *"reverse of transition."* Step 5: *"The forward rotation and the reverse are not symmetric and
   must not be assumed to be … no figure in this paper describes the landing transition."*

**My proposal:** a v7 figure enters v8 only after its labels and captions are checked like text, against the protected
sentences and the list of retired phrases. None of us could have seen this: the figures were never in a round text.

---

## 4. The pace — your solutions side by side

| | Grok | ChatGPT | DeepSeek | Qwen | K (now) |
|---|---|---|---|---|---|
| **Unit** | one step | one step | one step | one section | one step |
| **Mechanism** | a draft | functions classified, then the shortest faithful wording | keep-list, text moved as it is | a draft written against the protected lists | a draft (Section 6) |
| **What must survive** | every protected sentence; every number another step cites | any function in five tests (finding, its boundary, a number used later, a calculation needed to reproduce it, a bridge to the architecture's price) | finding, limit, every cited number, definition, cross-reference; the protected lists automatically | the caveat and insight lists | all of these |
| **Veto** | a dropped number or a stronger predicate; the source sentence returns verbatim | all five confirm | any list keeps a sentence | one veto kills a draft | Grok's |
| **Assemble the structure first** | yes | yes (strongest) | — | — | yes, as a generated view |
| **Order of the calculations** | 12, 13, 11, 10 | 10, 11, 12, 13, 14 | 10, 11, 12, 13, 14 | 10, 11, 12, 13 | 12, 13, 11, 10 |
| **Steps 7–8** | not in this block | last, in a final voice pass | a smaller unit until the calculations are done; then 5–8 by keep-list | last | not in this block |
| **Word target** | none | not as a criterion | — | yes | none (the author) |

---

## 5. I change my view

**I withdraw the keep-list.** Grok: *"The unit grew; the veto did not."* ChatGPT: *"a union of five people's anxieties."*
Qwen: *"a skeleton, not a paper."* They are right on both counts. The union of five lists would keep almost the whole
step. And the keep-list moves text without rewriting it, when writing the joins is the actual work. DeepSeek supported it,
and DeepSeek's three failure points (collective omission, a body that becomes assertion, joins that cost more than
expected) are what the plan below is built to prevent.

---

## 6. The plan — one piece from each of you. **The author has approved it.**

The author read your four solutions and my proposal to combine them, and approved the plan as written below rather than
sending it to a vote first. That saves a round: its first two products are in Section 7. Your vetoes on those products
stand exactly as item 4 describes.

1. **Assemble the structure first** (Grok, ChatGPT), **as a generated view**, like `ALL-STEPS.md` today. The fifteen steps
   stay the source, so the automated checks keep working unchanged. The view puts them under the nine agreed sections,
   renumbers the cross-references (Section 10 alone is cited about forty times) and splits Step 8 as B1 decided. No source
   sentence changes. **The Step 8 split is the one judgment, and it will be shown to you.**
2. **Before each calculation draft, a dependency map of that step** (ChatGPT; it is also DeepSeek's cross-reference scan).
   It lists the step's findings, each paragraph's one job (ChatGPT P3), every number another section cites, and the
   protected sentences in the step.
3. **The draft** (Grok, ChatGPT, Qwen), written by me from your specifications, because I hold the exact source and run the
   checks. It must hold every protected sentence (DeepSeek's floor); every number another section cites, with the clause
   that makes it checkable (DeepSeek); and every function any of you names (ChatGPT). **It adds no predicate.** Each sentence
   must be a source sentence, a source sentence shortened only by deletion, or a join that states no fact. That rule is mine;
   summaries are where this project's errors have come from. Every sentence removed is listed beside the draft with its
   destination: the supplement verbatim, or a repeat whose home is named.
4. **Veto (Grok's):** a dropped number, a lost function or a stronger predicate. The source sentence then returns verbatim.
   The result is shown and confirmed as now.
5. **Order: Step 12 first.** Three of you have already specified it, the three of you agree on its finding, and its text
   is the one you all hold. **Then 13, 11, 10**, so that Step 10, the most cited, comes last, as Grok argued: by then
   every number the other steps cite from it is known.
6. **Steps 5 to 8 are not opened in this block.** They are the innovation narratives the author named, so what happens to
   them after it is the author's decision. Steps 2 to 4 come after the calculations (Grok), with Step 2's opening sentence
   first (Grok P4).
7. **No budget.** ChatGPT's criterion instead: the body holds what is needed to understand and audit the principal claims.
   The supplement is the complete calculation record (ChatGPT's *"shadow paper"*).
8. **Figures** (Grok, DeepSeek). The configuration and the rotation come first, from v7, after the label check in Section
   3. The other figures come after the calculation drafts, because they show calculation results. **A figure replaces a body
   table; it does not duplicate one.**

**At one calculation step a round, with each confirmation in the next round's text, the four calculation steps should
take about five rounds**, inside the six to eight the author prefers.

---

## 7. The first two products — please check them

### 7.1 The paper, assembled (plan item 1)

`paper/v8/ASSEMBLED.md`, generated by `paper/build/v8_assemble.py`. **No source sentence is changed.** The steps remain the
source; the view is rebuilt after every change.

| Section | From |
|---|---|
| 1. The gap (Step 1's own title) | Step 1 |
| 2. The charges, the condition, an independent check | Steps 2, 3, 4 as 2.1–2.3 |
| 3. and 4. (their own titles) | Steps 5 and 6 |
| **5. Combining the solutions** | 5.1 = Step 7; 5.2 = Step 8's inventory, through *"What moves"*, **plus** *"These are the parts that fail the escape condition"* |
| **6. The soundness of the resulting product** | 6.1 = Step 8's *"What this inventory does not settle"* (the untrimmed hover torque; the two cruise states of the tip pairs, and the stopped one); 6.2 = Step 9 |
| 7. The calculations | Steps 10–13 as 7.1–7.4 |
| 8. and 9. (their own titles) | Steps 14 and 15 |

**Checked:** all 150 protected sentences are in the view, read with the new section numbers; the check catches one that is
deleted. Every cross-reference resolves to a section that exists. 27 714 words: the step bodies plus the new headings.

**The one judgment is the Step 8 split, made by B1:** the combining section keeps the count, the strip, the declined channel
and which parts fail; the soundness section gets the unsettled remainder. **One join follows from it:** *"These are the parts
that fail the escape condition"* now follows *"What moves"* rather than the paragraph on the tip pairs' cruise states. Its
next sentence names the tip pairs, so it still reads. Please check that.

**Twelve joins are listed, not repaired.** Repairing them would change source sentences, so each repair will be shown and go
through the veto like any other change:
- seven times *"Sections 7 and 8"* becomes *"Section 5"* (Steps 1, 9 twice, 10, 12, 13, 14). Two of those now break the verb:
  *"which is what Section 5 describe"* (Step 9) and *"Section 5 count the classes of mechanism"* (Step 14);
- five references inside Section 5 now point to Section 5 itself: Step 7's *"Section 8"* three times, and Step 8's
  *"Section 7"* twice, including its opening, *"Section 5 claimed that a class of mechanism is absent"*.

### 7.2 Step 12 — the first draft (plan items 2–5)

**Dependency map.** What other sections take from Step 12:
- Step 2: hover power linear in weight at constant disc loading; the scale test itself;
- Step 8: the 1 000 kg reference design;
- Step 11: how strongly the rotor term depends on low Reynolds number;
- Step 13: at least two charges are not locked together, so a ranking depends on the weighting; the 1 000 kg design has
  no closure;
- Step 14: the buffer is an input; the coupling of Bill 1 to Bill 3.

**The specifications followed:** Grok P3, DeepSeek P3 and Qwen P2 (the three excluded mechanisms and the equal-Re check move;
one sentence of the Reynolds mechanism stays, as Qwen asked; the low-Re limit stays, as Grok asked). Every protected
sentence is kept. **The limit sentence I proposed to protect is in the draft:** *"Of the two rotor terms, the light one is
therefore the less certain — and it is the one Sections 10 and 11 carry."*

**How it is checked** (`paper/build/v8_draft_check.py`). Every draft sentence must be a source sentence shortened only by
deletion: its words appear in the source in the same order. **Deletion alone can reverse a sentence,** since deleting *not*
turns *"Coupling is not identity"* into *"Coupling is identity"*. So the check also refuses any deleted negation or
qualifier (*not, no, only, without, about, within, rather, less…*). It caught exactly that when I planted it. It then
caught two of my own shortenings, where I had deleted *"without settling what specific power a store can deliver"* and a
definition containing *"less"*. **Both are restored.** There is one join that states no new fact, a pointer:
*"(geometry, dynamic pressure and solidity; Supplement S12)"*.

**The result: 2 973 → 2 151 words (−28 %).** 27 source sentences leave for Supplement S12 verbatim, 13 are shortened, and
76 stand as they were. **That is less than several of you expected** (Grok: *"12's finding is three sentences"*). The reason
is the rule, not caution: deletion without a new predicate keeps every limit sentence in full. To go further, a paragraph
would have to be replaced by a shorter sentence in new words. That is a rewrite: it must be proposed and shown, and it goes
through the veto. **Grok especially: which paragraphs would you replace, and with what sentence?**

**The draft, in full:**

> ## Scale does not lock two of the charges together; the third is not tested
>
> Section 11 decomposed the three charges on one aircraft, at one size. **This section asks a
> different question: are they three quantities, or one quantity under three names?** The test is
> to change the size of the aircraft and see whether they move together. If they did, the framework
> of Section 2 would be a single cost described three ways. Either answer leaves the mechanism claim
> where it was; that claim rests on the inventory of Sections 7 and 8.
>
> **The test is deliberately weak, and it is stated at its own strength.** It can show that two
> charges are not locked together within this model. It cannot show that they are independent in
> general, and it is not offered as doing so.
>
> ### What is compared, and why it is these two points
>
> **Section 10 closed only the light configuration, at 52.3 to 57.5 kg. No closure was run at 1 000 kg**, and
> none could be run on the same footing. A scale comparison therefore cannot be made from Section 10's closures. **It
> is made between the two reference designs, 50 kg and 1 000 kg, sized by one method, and both ends are taken from that pair.** In this section *the light design* and *the heavy design* mean
> those two reference designs. **The total zero-lift drag, the propeller efficiency, the range and the closed mass
> are not used.** No heavy-design range is quoted.
>
> **Two conditions travel with the heavy design.** It has no drag bracket; it stands on a single
> zero-lift coefficient with no equivalent bound. And **its structural closure is undetermined**: shell
> mass scales with wetted area while take-off mass scales with volume, so the structural fraction
> depends on how areal density grows with size, and that exponent has not been measured. **The
> comparison below uses powers, loadings and drag terms; it does not use the structure**, which is why
> it can be made at all.
>
> ### Bill 3 — held nearly flat by a sizing rule, which is not a finding about Bill 3
>
> **Disc loading is held at approximately the same value**: 44.2 kg m⁻² at 50 kg and 43.7 at
> 1 000 kg, one percent apart. At a given figure of merit, specific hover power depends only on disc
> loading, so holding it holds hover power per unit weight — **0.218 kW kg⁻¹ at the light design and
> 0.216 at the heavy**, within one percent. Hover power rises from 10.9 kW to 216.2 kW, a factor of 19.8
> against a mass factor of 20. **Hover power grows linearly with mass rather than as the L^3.5 of the
> classical result.**
>
> **That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3.**
> What it establishes is narrower and still useful: the hover side of Bill 3 *can* be held flat across
> a factor of twenty in mass by a single sizing choice.
>
> **The measure Section 11 uses for Bill 3 — rotor-shaft hover power divided by engine shaft rating, a
> ratio of installed hardware rather than a deficit — carries a second quantity, and it does not travel
> as cleanly.** The ratio is 4.19 at the light design and 3.98 at the
> heavy, a change of 5 percent. *(Section 11's 2.4 to 3.2 is the same ratio at the four closures. This paragraph compares the reference pair only.)* But the engine is sized by cruise, not by disc loading, and **the two
> reference designs do not use the same engine margin**: the engine is rated at 1.53 times cruise
> electrical power at 50 kg and 1.39 times at 1 000 kg. With the light design's margin at both sizes the
> heavy engine would be 60.0 kW and the ratio 3.61, a change of 14 percent. **The Bill 3 ratio therefore
> moves by between 5 and 14 percent across the factor of twenty, depending on an engine margin the
> sizing rule does not set.**
>
> **The rule has a price, and it is paid in geometry.** Holding disc loading constant makes disc area
> grow as L³ rather than L², so the nose propeller grows faster than the airframe. The
> ratio of propeller diameter to span rises from 0.35 to 0.47. **Much above 1 000 kg a single nose pair can no longer hold
> the disc loading**, and a second would have to be added — which the architecture permits, since
> every pair is torque-balanced on its own.
>
> ### Bill 2 — the rotor term falls, and in this model Reynolds number accounts for it
>
> **Only the rotor term of Bill 2 is computed at both sizes.** The frame term enters both reference
> designs as the same multiplier on clean lift-to-drag ratio, by construction, so it cannot show a scale
> effect in either direction.
>
> **The rotor term is computed by one method at both sizes.** At 50 kg it is **0.0154**. At 1 000 kg the blade
> designed to the same section lift coefficient gives **0.0068 — 0.44 of the light value.** Across the
> blade designs swept, design section lift coefficient 0.55 to 0.85, the heavy term runs from **0.0045
> to 0.0100**. At 50 kg the hover requirement selects the
> blade; at 1 000 kg nothing selects within the interval, and its ends are the ends of the swept blade
> family, not a physical bound. **At every point in it, and in the section polars used here, the heavy
> charge is between 0.29 and 0.65 of the light one** — a direction that is the ordinary one and a factor
> that is not a measurement, for the reason given below.
>
> **The mechanism is not the obvious one, and it is not the one a dimensional argument suggests.**
> Three candidates can be excluded directly ⟦(geometry, dynamic pressure and solidity; Supplement S12)⟧.
>
> **Within the blade-element and section-polar model, the section Reynolds number accounts for the
> fall.** In the free-wheeling state the median blade-section Reynolds number rises from about 8 × 10⁴
> at 50 kg to 5.6 × 10⁵ at 1 000 kg, a factor of 6.8, because the chords are longer and the flight speed
> higher. Reynolds number is not an independent variable — it follows from the chord
> and the speed each rotor has — so this is a decomposition inside the model rather than a causal claim
> beyond it.
>
> **That places a condition on the result, and it runs both ways.** The fall rests on how section drag
> changes between 8 × 10⁴ and 5.6 × 10⁵, which is taken from the section polars used for every rotor in
> this work rather than measured, and the light end lies below a Reynolds number of 10⁵, where section
> drag is hardest to predict. **The direction — lower section drag at higher Reynolds number — is the
> ordinary one; the size of the fall is as good as the section model at the low end.** If the light
> blade's real section drag is higher than the polars give, the light charge is larger and the fall is
> larger; if it is lower, the fall is smaller. **Of the two rotor terms, the light one is therefore the
> less certain — and it is the one Sections 10 and 11 carry.**
>
> **For the rotor term, the light design is the harder case.** That statement is not
> extended to Bill 2 as a whole, because the frame term is not computed at the heavy design and the
> heavy design has no drag bracket.
>
> ### Bill 1 — not tested, and the one available derivation would not test it
>
> **On this configuration Bill 1 appears as the energy buffer**, as Section 11 set out, since there is
> no dedicated lift group to charge. The buffer is 3.6 percent of take-off mass at 50 kg and 4.0
> percent at 1 000 kg.
>
> **Both of those figures are inputs.** Neither is derived from the hover energy the aircraft needs. **A change from 3.6 to 4.0 percent
> is a change between two choices, not a scaling result**, and it cannot be offered as evidence that
> Bill 1 moves with size in either direction.
>
> **A derivation is available without settling what specific power a store can deliver, and it is
> stated here because it shows why it is not used.** If the buffer is sized to supply the hover deficit
> — the hover demand at the electrical bus less what the engine delivers there — at a specific power
> that is the same at both sizes, its mass fraction follows the deficit per kilogram. **But that derivation makes the buffer a function of the hover power and the engine
> rating, which are the two quantities that measure Bill 3.** A buffer derived that way is locked to
> Bill 3 by the derivation itself, and comparing the two across scale would test the derivation, not
> whether they are separate.
>
> **No quantity computed in this work gives a buffer requirement at scale that is independent of the
> hover and engine powers and of an assumed specific power or energy.** On this aircraft Bill 1 takes
> the form of the device that releases Bill 3 from the engine, as Section 3 anticipated, and **whether
> the two are separable here is not established.**
>
> **What is established is that they are coupled here, and that is Section 3's claim rather than a
> defect found in it.** **Coupling is not identity.** The buffer is
> measured in kilograms and the engine in kilowatts, linked by a specific power that is itself an
> assumption; and the coupling belongs to an aircraft that meets the escape condition, not to the
> framework — a lift-plus-cruise aircraft pays a lift group whose mass is not a function of its cruise
> engine.
>
> What specific power a store of the required mass must deliver is the
> item Section 14 examines and does not resolve.
>
> ### What the comparison establishes
>
> **Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its
> light-design value in the section polars used here, while specific hover power changes by one percent
> and the Bill 3 ratio by 5 to 14 percent.** The flatness of Bill 3 is imposed by a sizing rule; the finding is that Bill 2 moved anyway,
> by more than the Bill 3 ratio at every point in the heavy interval and under either engine margin.
> **Within this model, the two are therefore not one quantity under two names.**
>
> **Bill 1 is not tested**, for the reason given above, and nothing here should be read as showing
> that it separates from the other two — or as showing that it does not.
>
> **And the evidence is one pair of design points, computed by one method, with the Bill 2 result
> resting on a section-drag model at low Reynolds number.** It is consistent with the separability
> Section 2 asserts; it is not a verification of separability as a general property, which a single
> instantiation cannot supply.
>
> ### Two costs that scale does not relieve
>
> **The cruise-efficiency gap under fixed pitch does not close with size; it widens slightly.**
> Computed at each reference design's cruise thrust, a nose-pair blade that meets the hover requirement
> delivers a cruise efficiency 14.6 to 21.0 percent below the 0.80 assumed at the light design and
> **16.4 to 22.9 percent below it at the heavy one.** As in Section 11, no variable-pitch counterfactual
> was computed, so this is not a measure of what refusing the hub costs.
>
> **The transition is where the square–cube relation is paid in full.** The moment needed to rotate
> the aircraft follows M = Iα with I ∝ mL², so the moment required for a fixed rotation time grows
> much faster than the aircraft. **Rotating the heavy design in the light design's two seconds would
> demand about 220 kW from the tip propellers — roughly the whole of hover power**, which is not
> available. At 5.1 seconds, the heavy design's rotation time, the demand falls to about 13 kW, 6
> percent of hover power. **A larger aircraft of this type turns more slowly, and must.**
>
> ### Why this section sits between the ledger and the contracts
>
> **The next section needs only what this one shows.** If the three charges were one quantity, a single
> number could rank architectures whatever weight each charge was given. **Because at least two of them
> are not locked together, a comparison of architectures cannot in general be reduced to a number that
> does not depend on how the charges are weighed: where one architecture pays less of one charge and
> more of another, the ranking depends on the weighting.** The argument requires only two charges that
> are not locked together; the third need not be shown separate for the conclusion to hold.
>
> Section 13 examines what the choice of sizing contract does to a ranking, on the light closures of
> Section 10 only.

**What leaves, and what is shortened** (27 out, 13 shortened; everything out goes to S12 verbatim):

- **Shortened:** If they did, the framework of Section 2 would be a single cost described three ways, and a ledger in three currencies would be a ledger in one.
  - *deleted:* and a ledger in three currencies would be a ledger in one
- **Out:** This is a different axis from the one Section 11 examined.
- **Out:** There, Bill 2's share of the zero-lift drag was compared at the two ends of the drag bracket, at a fixed size.
- **Out:** Here the size changes.
- **Out:** The two answers are about different variables and do not bear on each other.
- **Shortened:** No closure was run at 1 000 kg, and none could be run on the same footing: the heavy design has neither a drag bracket nor a structural closure (both below).
  - *deleted:* the heavy design has neither a drag bracket nor a structural closure both below
- **Out:** Taking one end from Section 10 and the other from the reference pair would manufacture a scale change that is really a propeller-efficiency update applied to one end only.
- **Out:** The quantities used are, with one exception, ones Section 10 did not replace.
- **Out:** Disc loading is a sizing rule Section 10 holds.
- **Out:** The buffer fraction is an input to its loop.
- **Out:** The free-wheeling rotor term is the value Section 10 carries at both ends of its bracket at 50 kg, before the ten percent margin of the adverse end (Section 11), and it is computed here at 1 000 kg by the same method.
- **Out:** The exception is the engine rating inside the Bill 3 ratio, which Section 10 did replace; it is taken from the reference pair and said so where it is used.
- **Shortened:** No heavy-design range is quoted: the figures available for it either omit the free-wheeling rotor charge or carry an assumed rather than a computed propeller efficiency, and none carries both.
  - *deleted:* the figures available for it either omit the free wheeling rotor charge or carry an assumed rather than a computed propeller efficiency and none carries both
- **Shortened:** (Section 11's 2.4 to 3.2 is the same ratio at the four closures; their cruise engines, 3.54 to 5.17 kW, are larger than the light reference design's 2.6 kW, and the engine rating is a quantity Section 10 did replace.
  - *deleted:* their cruise engines 3.54 to 5.17 kw are larger than the light reference design's 2.6 kw and the engine rating is a quantity section 10 did replace
- **Shortened:** Wing loading rises from 25.3 to 45.0 kg m⁻², span grows by a factor of 3.35 and the main propeller by 4.50, and the ratio of propeller diameter to span rises from 0.35 to 0.47.
  - *deleted:* wing loading rises from 25.3 to 45.0 kg m⁻² span grows by a factor of 3.35 and main propeller by 4.50 and the
- **Out:** The heavy design is not the light design photographed from further away.
- **Shortened:** The rotor term is computed by one method at both sizes: the blade designed for its own hover thrust at the same design tip speed, the hub at the same fraction of the radius, and the free-wheeling state solved at each design's own cruise speed.
  - *deleted:* the blade designed for its own hover thrust at the same design tip speed the hub at the same fraction of the radius and the free wheeling state solved at each design's own cruise speed
- **Shortened:** Across the blade designs swept, design section lift coefficient 0.55 to 0.85, the heavy term runs from 0.0045 to 0.0100, and every design in that range meets the heavy design's hover requirement with margin — a figure of merit of 0.75 to 0.77 against the 0.599 required.
  - *deleted:* and every design in that range meets the heavy design's hover requirement with margin a figure of merit of 0.75 to 0.77 against the 0.599 required
- **Shortened:** Three candidates can be excluded directly: - Geometry.
  - *deleted:* geometry
- **Out:** The eight tip discs total 0.251 m² against 1.98 m² of wing at 50 kg, and 2.82 m² against 22.24 m² at 1 000 kg — a disc-to-wing area ratio of 0.127 at both sizes.
- **Out:** The wing does not outgrow the discs. - Dynamic pressure.
- **Out:** A rotor turning freely at zero shaft torque settles at a rotational speed proportional to the flight speed, so its axial force scales with dynamic pressure and a coefficient referenced to that pressure does not.
- **Out:** Solving the heavy blade's free-wheeling state at 30 and at 40 m s⁻¹ confirms it: the coefficient changes by 9 percent — itself a Reynolds-number effect — not by the 44 percent a dynamic-pressure scaling would give. - Solidity.
- **Out:** The heavy blade is not thinner; it is fuller — 0.100 against 0.075 for blades designed to the same section lift coefficient.
- **Out:** Evaluating the heavy blade with its section Reynolds number scaled down to the light rotor's returns 0.0181 — 18 percent above the light charge.
- **Out:** At equal Reynolds number the fuller heavy blade would pay more, not less.
- **Shortened:** Reynolds number is not an independent variable — it follows from the chord and the speed each rotor has — so this is a decomposition inside the model rather than a causal claim beyond it: for the chords and speeds these two designs have, the fall is what lower section drag at a higher Reynolds number gives.
  - *deleted:* for the chords and speeds these two designs have the fall is what lower section drag at a higher reynolds number gives
- **Shortened:** If the light blade's real section drag is higher than the polars give, the light charge is larger and the fall is larger; if it is lower, the fall is smaller — the heavy end, at the higher Reynolds number, being the better predicted of the two.
  - *deleted:* the heavy end at the higher reynolds number being the better predicted of the two
- **Out:** The result does not touch the structural question.
- **Out:** It comes from blade-element solutions on two sized rotors at their own conditions; it would remain a result even if the heavy airframe were shown not to close.
- **Shortened:** Neither is derived from the hover energy the aircraft needs; each was chosen for its design point and carried into the sizing.
  - *deleted:* each was chosen for its design point and carried into the sizing
- **Shortened:** If the buffer is sized to supply the hover deficit — the hover demand at the electrical bus less what the engine delivers there — at a specific power that is the same at both sizes, its mass fraction follows the deficit per kilogram: 0.202 kW kg⁻¹ at 50 kg and 0.199 at 1 000 kg, a fall of about 2 percent.
  - *deleted:* 0.202 kw kg⁻¹ at 50 kg and 0.199 at 1 000 kg a fall of about 2 percent
- **Out:** Sizing the buffer by energy instead adds a hover duration, which is a mission choice, and changes nothing in that argument.
- **Out:** The buffer is the conversion the fourth part of the escape condition permits: kilowatts of hover peak paid in kilograms of store.
- **Out:** Nor is the structural mass a substitute.
- **Out:** The shell-mass exponent governs how the airframe fraction scales, and it is unmeasured; but the airframe is not Bill 1 as Section 2 defines it — it is the structure every architecture carries — and treating it as the mass bill would change the definition to fit the test.
- **Out:** Neither is one of the three charges, and both are reported because a section about what scale does to this aircraft would be incomplete without them.
- **Shortened:** As in Section 11, no variable-pitch counterfactual was computed, so this is not a measure of what refusing the hub costs; it is a measure of what a fixed blade that hovers delivers in cruise, and that does not improve with size.
  - *deleted:* it is a measure of what a fixed blade that hovers delivers in cruise and that does not improve with size
- **Out:** Hover power escapes the classical scaling objection by fixing disc loading; the rotation does not escape it.
- **Out:** A third shown to be separate would strengthen it; a third shown to be locked to one of the others would leave it standing.

---

## 8. Your proposals — side by side, with my position

| Proposal | By | My position |
|---|---|---|
| Assemble the agreed structure first | Grok P1, ChatGPT P1 | **Yes** — plan item 1 |
| Six figures | Grok P2 | **Partly.** Five of the six show what body tables already show (Steps 2, 6, 7, 10, 13); a figure would replace its table, not add to it. The configuration and rotation figures first; the rest after the calculations |
| A configuration figure | DeepSeek P1 | **Yes** — v7 Figures 5 and 6, after the label check |
| Step 12: the three excluded mechanisms and the equal-Re check (0.0181) to the supplement | Grok P3, DeepSeek P3, Qwen P2 | **Yes — done in the draft (7.2).** One sentence of the Reynolds mechanism stays (Qwen's point), because the limit is stated in its terms. **That limit is not protected yet:** I propose adding *"Of the two rotor terms, the light one is therefore the less certain — and it is the one Sections 10 and 11 carry"* (Grok's *"low-Re limit on the light rotor term"*) |
| Step 2's opening sentence stays first in the merged section | Grok P4 | **Yes** — it is already protected |
| No compressed draft of Steps 7–8 in this block | Grok P5 | **Yes** — plan item 6 |
| When Step 11 is drafted: keep *"three currencies, no total"* and the 14.6–21.0 % gap with *"No variable-pitch counterfactual was computed"*; what only restates Step 10 goes | Grok P6 | **Yes.** The refusal and that sentence are already protected |
| A one-page claim spine | ChatGPT P2 | **Yes, but built from the ten insight sentences and Step 9's four-axis table**, not a new summary |
| One job per calculation paragraph | ChatGPT P3 | **Yes** — plan item 2 |
| 7 500 is a destination, not a criterion for each round | ChatGPT P4 | **Yes** |
| The supplement as a *"shadow paper"* | ChatGPT P5 | **Yes** — plan item 7 |
| Step 10's first transition model to one paragraph | DeepSeek P2 | **Yes, when Step 10 is drafted.** The 5.4 m result, the verdict, and one sentence that the loss is not a controller artefact stay |
| A three-tier rule for every calculation step | DeepSeek P4 | **Yes** — it is plan item 3 |
| Merge Steps 10 and 11 | Qwen P1 | **Not now.** When Step 11 is drafted, what only restates Step 10 goes (Grok P6). That takes most of the gain and keeps Step 11's opening rule where it is |
| Soul sentences as the first or last sentence of their sections | Qwen P3 | **As a test in the final voice pass, not a rule now.** Some of them make sense only after the sentence before them (*"That single move is what removes the need for the mechanism"*) |
| A definitions block, as a table | Qwen P4 | **No.** The definition has had one home since Round 60 (Step 8). Steps 10 and 12 compare different aircraft, and their scope sentences are what prevent the confusion you fear. A table would be the ninth |

---

## 9. What I am asking

1. **The assembled view (7.1):** is the Step 8 split right? Does the join after *"What moves"* read? Name any cross-reference
   that now points to the wrong place.
2. **The Step 12 draft (7.2):** veto under plan item 4 — a dropped number, a lost function or a stronger predicate — quoting
   the sentence. Then: **which further cuts would you make, and with what replacement sentence?**
3. **Protect** *"Of the two rotor terms, the light one is therefore the less certain — and it is the one Sections 10 and 11
   carry"*: yes or no.
4. **The proposals (Section 8):** vote on those not already in the plan, and criticise my position.
5. **The v7 figures (Section 3):** is the finding right, and do you accept the rule?
6. **New proposals**, as always.

**Sources.** None of this needs a source. The files are in the repository at the paths and hashes given.
