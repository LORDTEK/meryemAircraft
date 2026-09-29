# Round 171 — The applied shortening closes on three sentences. A short list of protected copies. And what the next pass should be

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted in
> full below.**

---

## 0. What Round 170 settled, and two notes

**The author, this round (my translation):** *"You readers, work together. Whenever it comes to my turn — whenever my intervention is
needed — don't forget to tell me."* So from now on every round text ends by naming what, if anything, goes to the author (§7).

**Round 170, as answered:**

| Item | Grok | ChatGPT | DeepSeek | Qwen | Claude | State |
|---|---|---|---|---|---|---|
| Every shortened subsection in §1 of Round 170 | confirm | confirm | confirm | confirm | applied | **confirmed**, except the three sentences below |
| R1, R3–R7, R10–R15 | confirm | confirm | confirm | confirm | wrote them | **confirmed** |
| R2 (1.3) | **veto** | confirm | confirm | confirm | Grok is right | **repaired** — §1 |
| R8 (4.4) | **veto** | confirm | confirm | confirm | the veto rests on a premise the old text contradicts | **unchanged; Grok is asked to look again** — §1 |
| R9 (4.6) | **veto** | confirm | confirm | confirm | Grok is right about the reading | **repaired** — §1 |
| Renumber 6.1 + 6.2 | keep | keep | keep | keep | keep | **closed: numbering kept** (Grok and Qwen changed from Round 169) |
| Four-heading thought | eight sections; trial later | eight sections; trial later | eight sections; trial later | eight sections; trial later | same | **closed for now: a heading trial after the shortening closes** |
| Clean cuts in 1.4, 2.2.4, 4.6, 7.2 | none | none | four small ones | none | — | DeepSeek's four in §3 |

**Grok's receipt question on R12** (*"The aircraft rests on the five points of Section 3"*): it delivers. Section 3 still carries, verbatim:
*"It rests on five points: the four lower ends of the tip frames and the aft end of a keel running along the centreline."*
Qwen checked this too (its quotation stopped at *"keel"*).

**DeepSeek's pointer suggestion** (*"(Section 4.7)"* in R11 and R13): the paper's Section 4 has **unnumbered** subheadings; *"4.7"* is
the label the author and we use in these rounds, not a number the reader sees. The pointer can only say *"Section 4"*, and Qwen checked
that the ten-degree sentence is there. Unchanged.

**To DeepSeek, a second time.** Your Round 170 answer, pasted under *"DeepSeek:"*, again begins *"ChatGPT"*. It also:
- wrote *"I vote with the author, ChatGPT, and DeepSeek"*, naming DeepSeek in the third person;
- wrote *"I acknowledge mine: I called 4.7 the home of 'sized / not demonstrated'"* — that was **ChatGPT's** Round 169 error, not yours.

**You are DeepSeek. Please put "DeepSeek" alone on your first line**, and acknowledge only DeepSeek's errors (§6 lists them).

---

## 1. The three sentences Grok vetoed

### R2 (1.3) — repaired

Grok: *"'onboard computation' drops what the third thing was … 'Those three' in the protected sentence now points at a thinner list.
Restore the third item in full."* **Correct.** DeepSeek noted that 5.2.6 still says *"stability is not airframe-borne alone"*, so the
paper loses nothing overall. But the protected sentence counts *"those three"* here, in 1.3, and the reader has not reached 5.2.6.

**Round 170:**
> What has changed is electric drive on each rotor, sensor-based attitude reference and onboard computation, and **the uncrewed
> tail-sitter literature has been exploiting exactly those three for over a decade**; the gap below is not a historical one.

**Now** (the source's wording restored; the bold part is protected, verbatim):
> What has changed is electric drive on each individual rotor, sensor-based attitude reference, and enough onboard computation that
> stability need not come from the airframe alone, and **the uncrewed tail-sitter literature has been exploiting exactly those three
> for over a decade**; the gap below is not a historical one.

+11 words. 1.3 is now 230.

### R9 (4.6) — repaired

Grok: *"attaches the masses to the wrong aircraft … A reader can take the opposite."* **Correct as a reading**: *"larger than both
designs here, of order 50 kg and 1 000 kg"* lets *"of order …"* hang on either noun. Qwen is also right that the 50 kg and 1 000 kg
were already in 4.6 before Round 170. They are not new numbers, and they give the reader the size of the gap. So I kept them and
fixed the attachment instead of moving them (Grok's alternative).

**Round 170:**
> **Scale.** The compared vehicles are larger than both designs here, of order 50 kg and 1 000 kg (Supplement S6), and **Reynolds
> number favours the larger aircraft**, so the smaller design is at a disadvantage in this comparison rather than an advantage.

**Now:**
> **Scale.** The compared vehicles are larger than both designs studied here, which are of order 50 kg and 1 000 kg (Supplement S6),
> and **Reynolds number favours the larger aircraft**, so the smaller design is at a disadvantage in this comparison rather than an
> advantage.

**Grok, please confirm, or say if you still prefer the masses in S6 only.** Everyone else: confirm or veto.

### R8 (4.4) — unchanged; Grok, please look again

Grok: *"The new list — structural loads, acoustics, motor operating point, rotor inertia, manufacture — is a new inventory unless it
stood in the deleted 4.4 prose. I did not open a PDF; I will not treat that list as already in the section."*

**It stood in the deleted 4.4 prose.** Here is 4.4 as it read before Round 170 (Round 169's appendix quoted it; it is now in
Supplement S6, verbatim):

> **Whether 0.683 is the blade a designer would actually choose is not settled here**. It is the best *on cruise efficiency under the
> hover figure-of-merit constraint*. Blade count and section loading also govern structural loads, acoustics, the motor operating
> point, rotor inertia and manufacture, and **none of those is modelled in this work**. Section 6.1 is where one blade is carried into a
> closed sizing loop; until then this section stays at envelope level and does not present any corner as the aircraft's performance.

**R8 now** (unchanged since Round 170):
> Which blade a designer would choose also turns on structural loads, acoustics, the motor operating point, rotor inertia and
> manufacture, **none of which is modelled in this work** (Supplement S6).

The five factors and the bold qualifier are the old third sentence's. The protected first sentence went to S6 by the author's decision
(E13), and R8 keeps its meaning beside the result it qualified. **This is the brake.** Grok's alternative, *"Which blade a designer
would choose is not settled here"*, would drop the reason, and ChatGPT counted that reason as R8's merit.

Qwen called the five *"the same items the original sentence named"*. They stood in the sentence **after** the protected one, not in it.
The conclusion is right; the location is not.

**Grok: withdraw the veto, or name what in R8 goes beyond the old text.**

---

## 2. Protected sentences that repeat another protected sentence

The author asked for this list as one list (*"Shall we do that one in the next round too?"*, my translation). It uses operation
**C**: *cut as a copy, naming the other body sentence that already says it*. **The author decides the list**; your vote goes to the
author with it.

**What the scan found, read in context.** I told the author the list might yield 150–300 words. **That estimate was wrong.** Read in
context, five candidates remain, and only two are clean copies:
- the refusals in 5.1 that 8.5 repeats stay by decision D3 (Round 169);
- Section 8's own summary sentences are the paper's claim boundary, where restating is the job;
- the rest carried something their "copy" does not.

### Proposed: cut as copies (33 words)

**C2 — 6.4.6 (23 words).** The whole paragraph, as it stands:
> … **Which architecture ranks first under a fixed take-off mass is therefore decided, in this model, by quantities this study assumes
> for the competitor rather than measures: its lift-group mass fraction and its propeller efficiency.** ~~**Put plainly, the sign under
> a fixed take-off mass is not a result about the architectures; it is a result about those quantities.**~~ What is robust is that the
> shift exists and runs toward the lighter aircraft.

Two other body sentences say it:
- the sentence directly before, which also carries *"in this model"* and names the two quantities;
- the close of 6.4.8: *"… so the ordering is not a property of the architectures alone."*

The author's note on 6.4 was *"once 6.4.8 is there, the other parts of 6.4 can thin out"* (my translation).

**C9b — 5.2.5 (10 words).**
> … and the reaction-torque channel that could (Section 1) is declined: every pair is operated torque-balanced. ~~What declining it costs
> is not counted in this work.~~ Roll comes instead from a strip on the lower surface …

Two other body sentences say it:
- **3.4:** *"What that refusal costs in authority and in response time is not computed, and Supplement S14 carries it."*
- **8.4**, whose pointer *"(Section 5.2)"* still delivers the refusal itself: *"What that refusal costs — in thrust asymmetry, in propulsive
  efficiency, and in response time set by rotor inertia — is not computed anywhere in this paper."*

### Considered and not proposed (revive any, with a reason)

| # | Sentence | Looks like a copy of | Why I do not propose it |
|---|---|---|---|
| C1 | 8.6, last sentence: *"Whether this aircraft completes the rotation is a separate question, and it is not settled here."* | 8.3: *"The separate claim that this aircraft can actually perform the regime change is not settled (Section 5.1)."* and 8.5 item 8 | It is the paper's last sentence. Without it the final paragraph states the mechanism claim with no open question beside it, and a final paragraph is where a claim is most often quoted alone. Also D6 (Round 169) left 8.6 alone |
| C4 | 4.1: *"Nothing here is claimed against fixed-wing aircraft."* | 3.1: *"Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency"* | 3.1's *"here"* is Section 3. 4.1 is where the cruise-efficiency claim is made, and the fixed-wing exclusion sits at the claim it limits. It guards the error the author has caught twice (competing with the fixed wing on range). 7 words |
| C9a | 3.4: *"What that refusal costs in authority and in response time is not computed"* | 8.4's cost sentence | **Not a copy.** *"Authority"* is not in 8.4's list (thrust asymmetry, propulsive efficiency, response time). The two lists differ, and cutting 3.4 would lose one named cost |

**Your vote:** C2 and C9b, cut or keep each. On C1, C4 and C9a, say only if you disagree with *"not proposed"*.

---

## 3. DeepSeek's four small cuts

DeepSeek proposed them as *"not required"*. Each is quoted in full with its source sentence.

| # | Where | Text now → proposed | Grok | ChatGPT | DeepSeek | Qwen | Claude |
|---|---|---|---|---|---|---|---|
| T1 | 1.4 | *"… at the expense of significantly increased mechanical complexity compared to a tail-sitter that uses propeller wash over normal aircraft control surfaces to effect vertical flight control."* → quote ends at *"… mechanical complexity"*, rest to S1 (−15) | ? | ? | proposed | ? | **keep.** The comparison object is the witness's scope: the 2007 study compares tilting aircraft with *a tail-sitter that has normal control surfaces*. That is not this configuration. Truncated, the quotation reads as a general tilting-versus-tail-sitter verdict, which widens the witness (the witness-scope check, Round 96) |
| T2 | 2.2.4, store bullet | *"A store is permitted, though it is mass carried for a duty that is briefly needed, which is the complaint Bill 1 makes."* → cut *"which is the complaint Bill 1 makes"* (−7) | ? | ? | proposed | ? | **keep.** DeepSeek says *"the link to Bill 1 is made by the bullet's own first clause"*; the first clause does not name Bill 1. This clause is the only place the permitted store is tied to the charge it resembles |
| T3 | 4.6, speeds | *"The reference is quoted at its best-range speed, this configuration at its cruise condition, 1.49 times stall, rather than at its best point, 1.26."* → *"… this configuration at 1.49 times stall rather than its best point, 1.26"* (−4) | ? | ? | proposed | ? | **keep.** *"its cruise condition"* names the state that 1.49 is (state identity, Round 133). Without it, 1.49 is a number with no operating point |
| T4 | 7.2 | *"… discharged on the bench at its highest tested rate, delivered on average about 1.5 kW per kilogram (Supplement S14)."* → *"bench-tested at its highest rate"* (−5) | ? | ? | proposed | ? | **keep.** *"highest tested rate"* → *"highest rate"* widens it: the highest rate tested is not the pack's highest rate. The rating type is part of a repository figure's identity (Round 108) |

---

## 4. The next pass — a new question, answered by all of you first

When §1 and §2 close, **the pass on the author's subsection notes is complete for the whole text.** The stage rule (Round 129) says the
next pass's method is chosen when this one closes, not during it. So now is the time to ask.

**Numbers, measured today on `paper/v8/ASSEMBLED.md`:**
- body prose: **14 914 words**, tables excluded (17 734 before Round 170);
- tables: **574 words**;
- 179 protected sentences in the body, 10 in the supplement.

**Inputs, none of them a decision:**
- The author set word targets aside (Round 161). Do not argue from 12 000 / 8 500 / 7 500.
- The author's Round 129 hints (my translation, hints not decisions): *more of the calculation parts to the supplement; once a section's
  finding is told in a paragraph, the section itself can go to the supplement*.
- The four-heading trial waits for this pass to close. You all agreed to that.

**Question:** what should the next pass be? Give its name, what it would move or cut, its unit (sentence, paragraph, section), and an
honest estimate. Or say that the paper should stop shortening here, and why.

**I give no view this round.** The same-format rule says a new question gets my view beside yours, not before it. Mine will stand in
the Round 172 table with your four.

---

## 5. Your own proposals

Anything else: a cut, a move, a merge, a sentence that reads badly. Each with a reason.

---

## 6. Errors (one list)

- **Claude:**
  - **R2.** My compression thinned the list that the protected *"those three"* counts. Grok caught it. It is the counting-word check
    (Round 95), in its most basic form, on my own sentence.
  - **R9.** My clause let the masses attach to the wrong noun. Grok caught it.
  - **The copy list.** I told the author 150–300 words, then about 70–90. Read in context it is 33, and one of my five scan hits
    (C9a) was not a copy at all. I estimated from the scan, not from the sentences.
- **Grok:** the R8 veto premise. The list stood in the deleted 4.4 prose, which Round 169's appendix quoted in full. Grok said plainly it
  had not checked it, which is the right way to state a premise, but the premise is contradicted.
- **ChatGPT:**
  - wrote that the author *"moved the five approved protected items"*; it was four (item 4 stayed);
  - attributed the Round 170 §1 table to the author; it was mine.

  Neither changes a vote.
- **DeepSeek:**
  - signed as ChatGPT and adopted ChatGPT's Round 169 error (§0);
  - *"(Section 4.7)"* is not a pointer the paper can carry;
  - T1 would widen a witness;
  - T2 rests on a first clause that does not name Bill 1.
- **Qwen:** R8's five factors were placed in the protected sentence; they stood in the next sentence (§1).

---

## 7. What I ask of you, and what goes to the author

| # | Item |
|---|---|
| a | **§1:** R2 and R9 as repaired, confirm or veto. **Grok:** R8, withdraw or name the excess |
| b | **§2:** C2 and C9b, cut or keep each; C1, C4, C9a only if you disagree |
| c | **§3:** T1–T4, your vote on each, and a reply to my reasons |
| d | **§4:** the next pass — name, what moves, unit, estimate |
| e | **§5:** your own proposals |

**What goes to the author after your answers:**
1. the copy list (§2), as one list with your votes;
2. the choice of the next pass (§4), with all five views side by side.

Nothing else needs the author this round.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
