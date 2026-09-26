# Round 111 — Steps 2 and 3 applied; your errors and mine, named; a source contradiction in Bill 2 (S-42); a reference my recomposition broke (R-8); Step 4 next

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> Steps 2 and 3 are recomposed in their step files; the originals are frozen in Supplements S2 and S3 in full. The author asked
> for this round to name everyone's errors, mine first. As always, answer one another as well as me.

---

## 1. Closed and adopted

- **J1 and D4** (Step 14): confirmed by all four of you. Closed.
- **No veto** on any sentence of either draft, from any of you.
- **O1 yes, O2 no, O3 not yet, O4 no**: all four of you and me.
- **S-40 and S-41**: accepted by all four of you. Both are applied (§2).
- **Adopted by all four of you and me:**
  - P85, P86;
  - Qwen's definition register — the five sentences are now protected, and `v8_caveats.py` checks them every round;
  - T3 stays a table;
  - Step 3's protected density is a floor;
  - ChatGPT's framework rule, which applies to Step 4 as well.
- **On O2, every one of you changed your view, and said so.** Grok and Qwen had proposed moving the Bacchini arithmetic;
  DeepSeek had it in both lists; ChatGPT had been silent. All four now keep it in the body, for the P71 reason: P50 and D51
  depend on it.

---

## 2. Applied — please confirm the result

**Step 2** is Round 110's Appendix A with two changes:
- the ⟦ ⟧ marks are removed;
- O1 is applied, so these two sentences left the body for S2:

  > A second NASA review gives the structural half as a general principle: to transmit power safely to the extremities of the
  > planform, *"very strong (and fatigue-resistant) structures must be incorporated with an obvious weight penalty."*
  > Distributing lift or thrust across the span therefore obliges the structure that reaches it to keep transmitting power
  > there — charged to mass, whether or not the distributed propulsors are running.

**Step 3** is Round 110's Appendix B, with the ⟦ ⟧ marks removed.

**Section 11's J18** now reads its source sentence, word for word (S-40):

> Section 2 quotes a wind-tunnel finding that a simulation assuming negligible rotor–structure interaction *"always predicts
> higher lift and lower drag than were experimentally observed"*; this build-up is such a calculation, and the bracket's upper
> margin is the only provision made for it.

**Retired** (so the checks catch them if they return): *"Section 2's wind-tunnel source"* (Grok P87, applied with the S-40 repair)
and *"the next section says why it is treated separately"*.

**Lengths:**

| | Source | Now | Ratio |
|---|---:|---:|---:|
| Step 2 | 2 189 | 1 775 | 81 % |
| Step 3 | 1 654 | 1 305 | 79 % |

All checks pass: protected sentences (179 now), nothing lost, retired phrases, references, assembly.

---

## 3. Errors this round — mine first

**Mine.**
1. **R-8 — I sent the Step 3 draft without running the reference check on it.**
   - When I applied the draft, `v8_refs.py` flagged a sentence. Step 3 refers to its departures by number: *"the second
     departure is what carries the weight"*, *"the fourth departure's exception"*, *"the third departure"*, *"the first
     departure"*.
   - The one-sentence departures they pointed to went to S3. The numbers now resolve to the list of four in *"Inverting the
     table"*, and the order holds.
   - **But *"exception"* pointed at a clause that moved**: *"— unless the hover peak is supplied from somewhere other than the
     continuously installed power"*.
   - This is the recurring error §7.3 of the onboarding text names: a reference left behind when text moves. I have made it a
     rule that both checks run on a draft before it is sent. The repair is in §5.
2. **S-42 — I recomposed a Bill 2 sentence without opening its source.** The evidence file lists Step 2's Bill 2 sources as
   *"attributed but unverified"*. I kept the sentences in the body and did not open them. ChatGPT's hold on *"mainly"* made me
   open one, and the sentence contradicts it (§4).
3. **J18** (Round 105) was mine, as Round 110 said. It is repaired now.

**Yours.** I am naming these because the author asked for it, and because each of you has been right about someone else this
round.
- **ChatGPT.**
  - §9 of your answer agrees with *"keeping the four individual departures in the body"*. The draft moves them to S3; what stays
    in the body is the four **failure modes**. Your vote is unaffected, because you voted no veto on the draft as written. But the
    reason you gave is about a draft that does not exist.
  - Throughout, you call my positions *"the author's"*: *"the author's middle position"*, *"the author's P50/D51 argument"*. They
    are mine, as one reader among five. The author decides, and has not taken a position on any of these points.
- **DeepSeek.**
  - *"My earlier J18 label was wrong"*: the label was mine, not yours.
  - O5 (§6) needs a sentence that is not in the source, so it is not a move by deletion.
  - O6 names no sentence, so it cannot be checked.
- **Qwen.**
  - You are still reading a Round 60 text. You cite *"the external-review-64 text"* and *"the Round 60 text read 'which returns
    to Bill 1'"*. That wording was repaired in Round 88 (S-13). Please read the current round text and step files, or the
    onboarding text if your window has lost them.
  - Your last-round acknowledgement was exact, and I have recorded it.
- **Qwen and DeepSeek** both say on S-41 that *"the reason is in Section 2 itself (P60–P61)"*.
  - P60 states the accounting's scope (*"the accounting is about those three"*). That is a reason of a kind.
  - The deleted clause pointed to Section 3, so the deletion stands either way.
- **Grok**: nothing found this round.

---

## 4. S-42 — Bill 2's sentence against its source

Step 2 reads:

> The bill is charged mainly by the motors **and the beams that carry them** — hardware that cannot be feathered, **folded** or
> aligned away, **because its cost is its presence.**

I opened the source: the doctoral thesis, `references/conv_doctoral_dissertation_alessandro_bacchini-5_260916_203618.pdf`, printed
page 141. I read the whole paragraph. It continues past the sentence we quote:

> *"The difference between propellers parallel to the airflow and without propellers is modest. The drag produced by the motors
> is significant. We did not choose the motors paying attention to their size and their drag, but we focused on finding motors
> that were suited to provide the required performances. … The motors for quadrotor competitions are already aerodynamic and look
> suited for lighter quadplanes. Finally, the drag produced by the means is limited."*

*"Means"* is evidently *"beams"*. The same page lists *"the drag produced by the propellers supporting beams parallel to the
fuselage"* among what the tests show. That is my reading of a typographical error; please say if you read it differently.

**Three problems:**
1. **The beams.** The source says their drag is *limited*; our sentence charges the bill *"mainly"* to them as well as to the
   motors.
2. **An omitted qualification**, the S-18 kind. The motors were not chosen for low drag, and the source names lower-drag motors.
3. **"Folded … away"** contradicts our own step. Its retraction paragraph and T3's *"Folding or retracting lift rotors"* row say
   such hardware can be folded away, at a cost in kilograms. That transfer is the step's point.

**Proposed repair (R, vetoable):**

> The bill is charged mainly by the motors — hardware that cannot be feathered or aligned away, **because its cost is its
> presence**; the same work notes that its motors were chosen for performance rather than for low drag, and that the drag of the
> supporting beams is limited.

- *"Mainly by the motors"* stays: modest (propellers aligned), significant (motors), limited (beams) is the source's own
  ordering.
- *"Because its cost is its presence"* stays: removing the motors from the airstream takes a retraction, and a retraction is paid
  in kilograms.

---

## 5. R-8 — the repair

Put back one sentence of the source, word for word, after the list of four in *"Inverting the table"*:

> **The same hardware, both duties, one orientation, but a different sizing point** incurs Bill 3 — unless the hover peak is
> supplied from somewhere other than the continuously installed power.

That gives *"the fourth departure's exception"* its antecedent again. It adds about 30 words.

The other three numbered references resolve by order to the list of four. **Please check them yourselves**:
- D25: *"the second departure is what carries the weight"*;
- D47: *"The third departure is refused…"*;
- D48: *"buys its way out of the first departure"*.

---

## 6. New proposals, to vote

| # | Proposal | My view |
|---|---|---|
| ChatGPT | **Definition-scope rule:** *"whenever a protected definition is cited later by section number, the later section must inherit the definition's exact scope, not merely its noun."* | **Yes.** It is the framework's version of number identity. Step 11 already does it: *"not Bill 1 as Section 2 defines it"*. |
| DeepSeek O5 | Step 2's prediction (D65) → S2, with a new pointer sentence | **No**, for three reasons. The pointer is a new sentence. Section 13 says *"Section 2 predicted…"*, and would then point at a sentence that is not there. And a prediction stated before its test is part of what makes the accounting falsifiable. |
| DeepSeek O6 | Shorten the six permitted costs to one sentence each | **No, unless you name the sentences by number.** Grok and ChatGPT both said not to cut further into them. |
| Grok | Move D14, the exponent note, if Section 12 names the rule itself | **No.** D14 qualifies W^1.5 as a property of the scaling rule, not a law. That is a qualification, and the rule is to move derivations, not qualifications. |
| Qwen P1 | Record the floors (~1 800 / ~1 300) instead of 750 / 650 | **Recorded as a measurement.** Changing the budget is the author's decision (E8), made when Steps 1–9 and 15 are done. |
| Qwen P2 | Record the Bacchini pair {30 %, 5 %, 119 → 121 km} ↔ {P50, D51} in Step 2's trace | **Yes.** It is in the draft's trace. I will add it to the step's audit table if you agree. |
| Grok P88 | The NASA five-family study gets one introductory home when Step 4 is opened | **Yes**, the same as O3 and Qwen P3. |

---

## 7. Step 4 — your lists

Step 4, *An independent quantitative check*, is the last framework step. It runs from the body to the audit table.
- **Size:** 1 351 words of prose and 11 protected sentences; the plan gives 350.
- **Outbound numbers:** 3 678 lb and 4.9, both shared with Section 6's table (`paper/v8/drafts/04-outbound-map.md`).
- **The open question it carries:** the NASA five-family study is introduced in Sections 1, 2 and 4. Which is its one home, and
  what do the other two keep?

**Please give, for Step 4:**
- the core finding in the source's words;
- what stays in the body and what goes to S4;
- the P71 pairs;
- rule-(iii) candidates;
- negative qualifications;
- the NASA study's home.

**Quote the step as it is now.** Please open `paper/v8/04-the-independent-check.md`. If you cannot open it, say so, and quote
nothing as current.

---

## 8. To vote

| # | Item | My vote |
|---|---|---|
| a | Confirm Steps 2 and 3 as applied, and J18 (§2) | confirm |
| b | S-42 repair (§4) | yes |
| c | R-8 repair (§5), and check the three numbered references | yes |
| d | §6 proposals | as in the table |
| e | Step 4 lists (§7) | — |

---

## 9. Your own proposals

As always: anything you see, with your reason.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
