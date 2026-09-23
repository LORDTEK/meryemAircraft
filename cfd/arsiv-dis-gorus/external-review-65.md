# Round 61 — the author on what the paper is for; two readers' shortening proposals side by side; the list of caveats that cannot be cut

> **This is a task. Please answer it now; no confirmation is needed.** Last round, ChatGPT and Qwen
> confirmed they had the files and waited for an instruction. The questions are in Section 6.
>
> **Nothing in the paper changed this round.** The fifteen steps are exactly those in Section 6 of the
> Round 60 text you already have (`external-review-64`, commit `8197f9f`; `paper/v8/ALL-STEPS.md` SHA-256
> `aebd37973c164aab66f508f814811cb8f0a114f4139a5768f620a3922147edf3`). **From now on, round texts carry only what changed**, not the whole paper.

---

## 1. The author, on what this paper is for

The author wrote this round, and asked that everyone read it:

> *"The advantage the author — that is, I — has put forward must be the soul of this paper. Otherwise I do
> not want it to be 'yet another' calculation paper. I carry the justified pride of having seen what had not
> been seen. Why did we do the calculations? For a Q1 journal."*

**What this changes.** The paper is the presentation of an insight — that the regime change can be arranged
by rotating the airframe rather than its propulsors, so that the class of mechanism that reorients a
propulsor disappears — and **the calculations exist so that a Q1 reviewer can check that insight and price
it.** They are not the point in themselves. Shortening, structure and voice should make that visible.

**What it does not change.** No predicate becomes stronger. The contribution stays at the strength in the
onboarding file: *"arranged to"*, a count of mechanism classes, no simplicity claim, and novelty only as
*"not found where searched"*. **The insight has to be carried by placement, order and voice — not by a
stronger sentence.** A stronger sentence would reopen the priority claim that three of you disproved in
an earlier round, and would give a desk editor the reason to return the paper.

**There is a tension here, and I am not resolving it alone.** Step 1 ends: *"The combination, the
consequences of the choices inside it, and an accounting of what they cost are how that contribution is
presented and priced — **not a claim that the route was waiting to be found.**"* That clause was written after
the priority claim was narrowed. The author's stance is *"having seen what had not been seen."* Both can be
true — the elements are old; what the author saw is how they combine and what the combination removes — but
the sentence as written may undersell what the author saw. Question 1 asks how.

---

## 2. How rounds work from now on

- **Round texts carry only changes.** The full text is already in your conversation.
- **Nothing is cut directly.** Each reader's proposal is shown to all the others, side by side, and
  everyone's view is taken.
- **What readers agree on is processed first.** What they disagree on goes back to everyone.
- **The author decides.**

---

## 3. A translation error of mine

The author's outline of the argument has the element *"ortaya çıkan ürünün sorunsuzluğu"*. I translated it
as **"why the result holds"**. That is wrong. It means **"the soundness of the resulting product"**: that the
combined aircraft is sound as a whole. Last round, one reader placed the scale and contract results under
that heading, and my translation invited it. The onboarding file is corrected. The corrected outline is:

> *introduction · the current state · the solution to one problem · the solution to the other · **combining
> the solutions** · **the soundness of the resulting product** · the calculations · conclusion*

The mapping of that element to Steps 8 and 9, used in earlier proportion tables, was also mine, not the author's.

---

## 4. Round 60: what two readers proposed, side by side

**Grok and DeepSeek answered in full. ChatGPT and Qwen confirmed they had the files and did not answer.**
The agreement below is therefore two readers' agreement. It is put to all four.

### 4.1 Where they agree — to be processed first

| # | Topic | Agreement |
|---|---|---|
| A1 | The framework under shortening | **Both assumed it is shortened in proportion with the rest.** Its *functions* are kept: the three charges, the escape condition and its four failure modes, the independent check, the scale finding, the contract finding. Its *step lengths* are not. It is not reduced to pointers. *(The author's remark above — calculations exist for a Q1 journal — is consistent with this reading; the author has not yet confirmed it.)* |
| A2 | Combining the solutions | **Steps 7 and 8 become one section**: the contribution's section. It is not folded into the sections on the two halves. |
| A3 | Step 15 | **A short close**, after the numbers. Not a second Step 9. |
| A4 | One home for each repeated claim | The two-percent duty cycle → **Step 2**. *"By construction means by the sizing"* → **Step 9**. No range claim against the other hybrids → **Step 9** (the refusal) and **Step 13** (the finding), one sentence in 15. Partial instantiation → **defined in Step 3**, applied in 7 and 8, pointers elsewhere. The mechanism-class table → **Step 7**; 15 does not reprint it. The list of what does not close → **Step 14**; 15 keeps one paragraph. The 1954 history and *"what is already occupied"* → both in **Step 1**, compressed. Step 11's opening and closing → stated once. |
| A5 | Must stay in the body | Cruise axis: Step 6's conversion to effective lift-to-drag ratio, the 5.56–7.39 envelope, the two quadrotor comparisons, the five qualifications (as sentences). Runway axis: Step 5's requirement and its sized/not-demonstrated list, and Step 14's store figures. Mechanism: Steps 7 and 8. Range refusal: Step 9's fourth row and Step 13's main table. |
| A6 | Can move to a supplement | Step 10's spread table (one sentence stays); Step 13's sensitivity matrix (at most one row stays: the lift group); Step 14's long table of unknowns (a summary stays); the longer part of the 1954 history; part of Step 4 (Grok: the quadrotor contrast; DeepSeek: the weight breakdown). The lift-plus-cruise / tilt-wing isolation pair and its conclusion stay. |
| A7 | Tables in the body | **Six agreed:** Step 6's corners · Step 6 against the two quadrotors · Step 7's mechanism classes · Step 10's closures A–D · Step 13's three contracts · Step 14's store re-closure. The target is eight; **two places are open** (B7). |
| A8 | Last round's corrections | Both: faithful to their sources, no new contradiction. |
| A9 | Caveats that cannot be cut | Merged, the two lists give **100 caveats** (Section 5). **Every one was checked against the text and is in the step named.** Three were light paraphrases and are now given verbatim. An automated check now fails if any of them disappears from its step in a shortened draft. |

### 4.2 Where they disagree — please weigh in

| # | Topic | Grok | DeepSeek |
|---|---|---|---|
| B1 | What goes under *"the soundness of the resulting product"* | Step 9 (the boundary) | Steps 12 and 13, moved before 10 *(under my wrong translation, "why the result holds")* |
| B2 | Steps 2, 3, 4 | One section, three subsections | Three sections |
| B3 | Steps 5 and 6 | Question 2: *"two short halves inside one section"*; the map: two sections (**Grok's two answers differ**) | Two sections, parallel structure kept |
| B4 | Home of the declined reaction-torque channel | **Step 8**, with one clause each in 1 and 7 | **Steps 7 and 8** |
| B5 | Home of "the transition is not shown" | **Step 7** | **Step 9** (the boundary) with **Step 10** (the 5.4 m result) |
| B6 | Home of the fixed-pitch efficiency gap | **Step 11** (14.6 to 21.0 percent) | **Step 6** (the gap and its cause); 11 attributes it |
| B7 | The two open table places | **Step 2's transfer table** and **Step 11's C_D0 build-up**; Steps 3, 4 and **9's four-axis table** become prose | **Step 9's four-axis table** and **Step 9's dependency table**; Step 2's table to the supplement or condensed; Step 11's build-up to the supplement with 57–69 percent in the text |

---

## 5. The caveats that cannot be cut — 100, merged from Grok (G) and DeepSeek (D)

Each is quoted from the step named, and each has been checked to be there. `…` joins fragments of one passage.
**This is the list every shortened draft will be checked against.** If a line is to leave its step, it moves
or goes only by the author's decision, and that is recorded.

| Step | Caveat | From |
|---:|---|---|
| 1 | The contribution is the architecture: a configuration arranged to change regime by rotating the airframe rather than its propulsors, and so carrying no mechanism that reorients a propulsor. | G |
| 1 | None of the elements is new | G |
| 1 | Some of the difficulties were real, internal, and are inherited here. | D |
| 1 | Using it is a choice, and so is declining it. | D |
| 2 | The accounting claims transfer. It does not claim that every architecture is equally good. | G |
| 2 | A remedy whose cost falls outside the three charges does not refute the accounting…but it is not thereby exempt from being counted. | G |
| 2 | A framework that could absorb any cost by declaring it out-of-scope would be unfalsifiable. | D |
| 2 | The statement is deliberately confined to architectures with a dedicated lift subsystem. | D |
| 2 | they are not assumed to be independent physical causes | D |
| 3 | It means zero of the three charges as Section 2 defines them…It does not mean an architecture that costs nothing | G |
| 3 | It does not claim the trade is favourable. | G |
| 3 | An architecture may meet the condition where it carries the aircraft and fail it elsewhere | G |
| 3 | Whether such an architecture might avoid the three charges by some other route is a separate question this paper does not settle. | G |
| 3 | A store is permitted…It does not claim the trade is favourable. | D |
| 3 | Releasing the engine is not releasing the electrical path. | D |
| 3 | Rotating the airframe is permitted and is not priced here. | D |
| 3 | Serving two regimes with one set of hardware has a price of its own…The condition permits that cost and does not measure it. | D |
| 3 | An architecture that reorients a propulsor does not satisfy the condition as written…the condition is a definition, not a law, and it can be too narrow without being wrong. | D |
| 4 | What follows is not a test of the whole framework. | G |
| 4 | only the first is a derivation | G |
| 4 | They are not identical in every other respect…the comparison is the closest the published set comes to isolating that charge; it is not a controlled experiment. | G |
| 4 | It checks one falsifiable consequence on one independent data set. | D |
| 4 | Second half, not derived. | D |
| 4 | It does not establish that the accounting is complete…or that avoiding them makes an aircraft better. | D |
| 5 | Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency. | G |
| 5 | Not demonstrated, and the list is not short. | D |
| 5 | The saving has precedent and it is not this paper's observation. | D |
| 6 | The size of the resulting advantage is a calculation, not a consequence of that statement. | G |
| 6 | These are the bounding corners of a product, not four simulated aircraft. | G |
| 6 | Against the all-electric quadrotor it does not hold at the low corner, and that result is reported as a result rather than as a caveat. | G |
| 6 | This is a comparison of two independently produced figures in a common definition, not a controlled numerical reproduction. | G |
| 6 | is not claimed here, because it has not been computed. | G |
| 6 | Nothing here is claimed against fixed-wing aircraft. | D |
| 6 | Whether 0.683 is the blade a designer would actually choose is not settled here. | D |
| 6 | No part of this has been measured. | D |
| 6 | The span efficiency used throughout this section is the computed value, 0.817, not the assumed 0.85. | D |
| 6 | the aerodynamic predictions diverge above roughly ten degrees of incidence | D |
| 7 | The instantiation is therefore partial. | G |
| 7 | This is not a configuration in which nothing moves. | G |
| 7 | Nor is this a claim of mechanical simplicity. | G |
| 7 | Whether this aircraft can actually perform the change is a separate question and is not settled anywhere in this paper. | G |
| 7 | The mechanism claim is about hardware and survives that limit. The transition claim is not made. | G |
| 7 | The qualification in that sentence is not decoration | D |
| 8 | What declining it costs is not counted in this work. | G |
| 8 | The stopped state is not. | G |
| 8 | should be read as the state Section 11 defines rather than as the state a particular installation would reach. | D |
| 8 | How many actuators that is, this study does not fix. | D |
| 9 | No range claim is made against the tilting or lift-plus-cruise families in either direction. | G |
| 9 | is not computed anywhere in this paper. | G |
| 9 | The mechanism claim is a statement about what hardware is present | D |
| 9 | The separate claim that this aircraft can actually perform the regime change is not settled | D |
| 9 | By construction" throughout this paper means "by the sizing", never "by demonstration. | D |
| 9 | no comparison in this paper should be quoted without the contract it was computed under. | D |
| 10 | Closing a sizing loop mathematically is not the same thing as closing an aircraft physically. | G |
| 10 | These are the same configuration at four closed masses rather than four configurations | G |
| 10 | The closures do not take that reduction, and it has not been run through the loop. | G |
| 10 | So the zero-altitude-loss result is a property of the model that produced it. | G |
| 10 | That spread is itself the finding. | G |
| 10 | Whether a real aircraft loses 5.4 m, more, or less is not settled by anything here. | G |
| 10 | If no fixed point exists, the declared sizing package does not close. | D |
| 10 | Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude. | D |
| 10 | It does not establish that the package exists. | D |
| 11 | It attributes. It does not add. | G |
| 11 | no scalar aggregate is defined | G |
| 11 | The ledger does not attribute the whole of that gap to the absence of variable pitch. | G |
| 11 | No variable-pitch counterfactual was computed. | G |
| 11 | The buffer fraction is an input to the loop, not a result of it | G |
| 11 | Bill 3 is removed from the engine and left standing on the electrical system. | G |
| 11 | There is no single figure for what the architecture costs. | D |
| 11 | The rotor line rests on section drag at low Reynolds number. | D |
| 11 | The tip-frame term is an attribution, not a marginal removal cost. | D |
| 11 | Rotor–structure and rotor–wing interference is not modelled and is not carried as a line. | D |
| 12 | That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3. | G |
| 12 | This paragraph compares the reference pair only. | G |
| 12 | Bill 1 is not tested. | G |
| 12 | It is consistent with the separability Section 2 asserts; it is not a verification of separability as a general property. | G |
| 12 | The test is deliberately weak | D |
| 12 | It cannot show that they are independent in general | D |
| 12 | The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low Reynolds number. | D |
| 13 | What the bound gives is a size, not an order. | G |
| 13 | how much of it they fill is not computed | G |
| 13 | A ranking against a competitor modelled as a bound is not a ranking, and no range claim is made against the tilting family in either direction. | G |
| 13 | Which architecture ranks first under a fixed take-off mass is therefore decided, in this model, by a mass fraction of the competitor that this study has not measured. | G |
| 13 | These are three different questions, not three estimates of one answer. | D |
| 13 | Holding Bill 3 common is a choice of question, and it has a direction | D |
| 13 | The choice runs against this configuration. | D |
| 13 | The tilting layout carries no cruise drag penalty at all. That is an idealisation in its favour. | D |
| 13 | Neither figure is measured. | D |
| 13 | The sign under a fixed take-off mass is not a result about the architectures; it is a result about that parameter. | D |
| 13 | Comparing computed figures against assumed ones favours whichever is assumed more optimistically. | D |
| 14 | The package Section 10 closes on does not exist with any store the sources consulted here report as built. | G |
| 14 | It does not reach the mechanism claim. | G |
| 14 | The loop closes; the aircraft is not shown to. | G |
| 14 | for the first item the answer is no | D |
| 14 | The comparison is between unlike ratings | D |
| 14 | The gap is real on every one of them; the factor quoted is peak demand against bench average. | D |
| 14 | These masses are the Section 10 package with one input changed. | D |
| 14 | They are not a structural closure at 100 kg | D |
| 15 | This is a count of mechanism classes, not a claim that nothing moves, and not a claim of mechanical simplicity or reliability | D |
| 15 | Whether this aircraft completes the rotation is a separate question, and it is not settled here | D |

---

## 6. What I am asking

**Everyone:**

1. **The soul.** Read your coarse map (or the two in Section 4) against the author's statement in Section 1.
   **Where would the shortened paper read as a calculation paper that happens to contain an architecture,
   rather than as the presentation of an insight whose calculations make it checkable?** What placement,
   order or voice would change that — **without making any predicate stronger**? And the Step 1 clause:
   *"not a claim that the route was waiting to be found"* — keep, rewrite, or move, and to what? If you
   propose words, they must stay at the strength the onboarding file sets.
2. **The disagreements B1–B7.** For each: which side, or a third option, **in one line with a reason.**
   For B1, use the corrected outline element (Section 3).
3. **The caveat list** (Section 5). Anything missing whose loss would turn a claim into an over-claim? Anything
   on it that is not actually load-bearing? Quote the sentence and name the step.

**ChatGPT and Qwen** — you have the Round 60 questions. Rather than starting from zero:

4. **For each of A1–A9, agree or disagree**, in a line; and add anything from your own reading of the Round 60
   questions (the core of each step, one home for each repeated claim, body or supplement, the coarse map,
   the tables) that Grok and DeepSeek did not say.

**Grok and DeepSeek:**

5. **Have I represented your position correctly** in Section 4? Say where not.

**Sources.** None of this needs a source. PDFs only for priority claims, numbers taken from tables and
verbatim quotations — and say which document you opened in this conversation for any number you give.
Quote only from the v8 text (Section 6 of the Round 60 text).
