# Round 113 — R-8 applied as C, and can it be shorter; Step 4's first draft; a question on the scope of one quoted sentence (S-43); what Sections 1 and 2 keep of the NASA study

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`9fc1587`**, branch `claude/ecstatic-cori-6w30at`. The repository is for verification only. **Every text you are asked to
> judge is in this file, in full.**

**A change in how these round texts are written, at the author's request.** Twice (Rounds 109 and 111) I asked you to open a
file in the repository, although some of you cannot, and gave you hashes instead of text. You then worked from older versions,
and a round was lost. From now on, whatever you are asked to judge is quoted here: the current text, the draft, the neighbouring
sentences it depends on, and the source paragraph behind any quotation.

---

## 1. Closed and applied

- **S-42** is confirmed by all four of you. Closed.
- **The external-evidence identity rule** (ChatGPT) is adopted by all four of you and me.
- **R-8: all four of you chose C, Qwen included.** It is applied. *"Inverting the table"* now reads, in full:

> **A charge appears wherever the two regimes are served by hardware that departs from one of four things: the same hardware,
> serving both duties, held in one orientation, with the hover peak supplied other than by its continuously installed power.**
> **Different hardware** costs Bills 1 and 2. **The same hardware serving only one duty** costs them again. **The same hardware
> serving both duties in a different orientation** is the tilting family. **The same hardware, both duties, one orientation, but a
> different sizing point** incurs Bill 3 — unless the hover peak is supplied from somewhere other than the continuously installed
> power. What each departure costs is in Supplement S3. Read one at a time, these are ways to pay. Read as a conjunction, they are
> a condition.

- **The reference check now fails** if *"first / second / third / fourth departure"* appears in Section 3 while the sentence
  naming that departure is missing (Grok P91). It was tested by deleting the second one; the check caught it.

---

## 2. Can C be shorter? The author asks

The author accepts C but asks whether the four departures need this many words.

**My count was wrong:** C is **60** words, not the ~55 I gave you.

**Where the words go:**
- The four names are the antecedents, and cannot shrink: *"Different hardware"*, *"The same hardware serving only one duty"*,
  *"The same hardware serving both duties in a different orientation"*, *"The same hardware, both duties, one orientation, but a
  different sizing point"*. That is about 31 words.
- The verbs and costs take about 15 words.
- The *"unless"* clause takes 14.

**Three shorter forms:**

| | Text | Words | Kind |
|---|---|---:|---|
| **C** (applied) | as above | 60 | deletion |
| **C-short** | C without its last 14 words: *"…but a different sizing point** incurs Bill 3."* | 46 | deletion |
| **C-list** | *"The four departures, in order, are different hardware; the same hardware serving only one duty; the same hardware serving both duties in a different orientation; and the same hardware, both duties and one orientation, at a different sizing point."* | 39 | **R** — a new sentence; the costs stay only in S3 |

**What C-short costs.** The *"unless"* clause was put back to give *"the fourth departure's exception"* an antecedent. That phrase is
in the paragraph after the condition, which reads in full:

> Two things in that sentence are choices rather than derivations. The inversion requires only *one orientation relative to the
> airframe*; **how** an architecture keeps that while changing flight regime — by rotating the whole body, or otherwise — is not
> in the inversion, and is treated as exposition rather than as part of the definition. And the fourth departure's exception lets
> the peak come from **any** source other than the continuously installed power; a store is the narrower reading used here,
> because it is what the configuration examined later uses and because a narrower condition is easier to fail.

That sentence says what the exception allows. D3's fourth item (*"with the hover peak supplied other than by its continuously
installed power"*) says it too. With C-short, *"exception"* is defined where it is used rather than beforehand.

**My view: C-short.** It saves 14 words, it is still deletion only, and the one reference it touches carries its own definition.
C-list saves 21, but it is a new sentence, and it drops what each departure costs from the body. **Please judge both. Qwen,
since R-8 was your objection, your answer weighs here.**

---

## 3. Errors, mine first

- **Mine:**
  - the word count of C (above);
  - asking you twice to open files instead of quoting them. The author named it, and the rule has changed (top of this file).
- **Qwen:**
  - your correction last round was exact;
  - one point this round: P2 says *"None is known to the authors"* *"acknowledges … that the longer-range counter-set does not
    exist"*. It does not say that. It says none is **known**, which is the §2.2 form of the claim (*"not found"*, not *"does not
    exist"*). That is the reason to protect it, and also the reason not to paraphrase it.
- **ChatGPT:**
  - On NASA in Section 2 you say Section 2 should keep *"only a pointer"*. Section 2's use is not a pointer: it quotes the study's
    **finding** for Bill 1 (text in §6). That is a consumed finding, which your own rule allows. Grok reads it that way too.
  - Your hold on *"credit reduced to nothing"* is in §7.
- **Grok, DeepSeek:** nothing found this round.

---

## 4. Step 4 — the first draft

**All four of your lists (from last round's Appendix A) and mine agree on what stays.** They move only:

- **M1** → S4:
  > The accounting says an architecture that avoids the three is cheaper in those three currencies and nothing more; a
  > configuration may avoid all three and still be unbuildable, uncontrollable, or unsuited to its mission. Sections 10 and 14 are
  > about exactly that possibility for the configuration proposed here.

  The second sentence's *"that possibility"* needs the first, so the two go together. The point is carried in the body twice:
  Section 3's triple denial, and Section 9's item 6:
  > **6. It does not claim that satisfying the condition makes an aircraft better.** The condition concerns three specific charges.
  > A configuration may avoid all three and still be unbuildable, uncontrollable, or unsuited to its mission, and the accounting says
  > nothing against that possibility.

- **M2** → S4, the closing transition:
  > The next two sections describe the two capabilities the mission asks for, one at a time and each against the family that
  > structurally lacks it, before Section 7 asks whether one aircraft can hold both.

- **O-a, optional** (ChatGPT: *"detailed tilt-wing mechanism explanation, S4 candidate"*): the clause *", with the actuation, the
  gyroscopic coupling and the transition control problem that Section 2 assigns to that family"*.
  - My view: **no**. It is where Section 4's transfer finding is tied to Section 2's assignment of the tilting row. Without it,
    *"moves the cost — to the mechanism"* is a reading the check makes rather than one the accounting predicted.

**Kept, against a proposal to move it:**
- the Section 11 pointer, whole (*"…where it is applied to it and where the answer is not uniformly favourable"*). All four of you
  keep the qualifier. Keeping only the qualifier would need a new sentence.
- *"If some data set showed the credit covering the charge, Bill 1 would not be refuted"* (Grok: the prediction's limit).

**Length: 1 351 → 1 268 (94 %); 1 250 with O-a.** The deletion check passes: no new predicate, no deleted negative, all 11
protected sentences present.
- This is the smallest cut of any step, and I will not dress it up. The step is a chain of result, basis and limit, and your five
  lists found almost nothing in it that is working.
- ChatGPT and Qwen both said the 350-word plan should not be a stop rule for this step. Qwen proposes recording the floor.
- **If you see a sentence that is working and not evidence, name it by its first words.**

The full draft is **Appendix A**, with moved text struck through.

---

## 5. S-43 — a question on the scope of one quotation (not yet a defect)

Step 4 says:

> **And the source states the second half of the prediction in its own words.** Discussing why the all-electric lift-plus-cruise
> design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery
> weight compared with the quadrotor, *"but not enough to counter the increase in structure and propulsion weight."* That is the
> efficiency credit conceded and found insufficient, by the authors of the data rather than by the authors of the prediction.

I opened the source while drafting (`references/1521_Johnson & Silva_122721.pdf`, page 11 of the PDF) and read the whole paragraph:

> *"Figure 6 shows the breakdown of the weight empty. For each design, the payload is 1,200 lb and the fuel for turboshaft
> propulsion is 150–180 lb. Generally, structural and propulsion weights increase with the number of rotors. There is only one
> design mission, so the battery capacity equals the energy (including reserve) needed for that mission. Even high
> specific-energy batteries are heavy, so all-electric propulsion produces a heavier aircraft than turboshaft or hybrid or
> turbo-electric propulsion. The high cruise efficiency of the lift+cruise type reduces the battery weight compared to the
> quadrotor, but not enough to counter the increase in structure and propulsion weight, so the all-electric lift+cruise aircraft is
> the heaviest design."*

**The quoted comparison is the all-electric lift-plus-cruise design against the quadrotor.** Step 4's test is the turbo-electric
pair (lift-plus-cruise against tilt-wing). The same step says the quadrotor contrast *"changes three things at once"* and is
reported *"for scale"*.

**What the body does right:** it names the all-electric design and the quadrotor, so nothing is hidden.

**The question** (the witness-scope rule, Round 96): do *"the source states the second half of the prediction in its own words"*
and *"That is the efficiency credit conceded and found insufficient"* read as support from the test pair, when they come from
the pair the step set aside?

**Options:**
- **(a)** Leave it: the pair is named, and the source's sentence is the general mechanism, which the same paragraph states
  (*"Generally, structural and propulsion weights increase with the number of rotors"*).
- **(b)** Qualify it (R): e.g. *"…in its own words, on the comparison the check does not use as its test."*
- **(c)** Move the paragraph to S4 with the quadrotor contrast.

**My view: (b).** The sentence is the one place the data's authors speak, and it should stay. But it sits between the isolated
pair and the quadrotor sentence, and a reader can take it as part of the test.

---

## 6. What Sections 1 and 2 keep of the NASA study — the texts, so you can settle it now

The author would rather settle this now than wait for Step 1. Your positions were:

| Grok | ChatGPT | DeepSeek | Qwen |
|---|---|---|---|
| Section 1: a pointer at most. Section 2: its quotation can stay if it does not re-introduce the study. | Section 1: a contextual introduction, if needed. Section 2: only a pointer. | decide when Step 1 is recomposed | Section 1: one short contextual sentence, without the five-family list |

**Section 1 now reads** (the NASA sentences and the two paragraphs that use the study):

> A NASA study that sizes five VTOL architecture families to one mission describes the two relevant routes in its own terms.
>
> **The lift-plus-cruise route keeps two sets of hardware and switches between them.** In that study the configuration is a
> stopping-rotor compound with three flight modes — helicopter mode with the lifting rotors turning, compound mode with both sets
> operating, and aeroplane mode in which *"the lifting rotors are stopped with the blade axis pointed along the vehicle
> longitudinal axis, and therefore nominally aligned with the free stream to minimise drag,"* with forward thrust from a pusher
> propeller. The lifting rotors are carried through cruise and are stopped in the airstream.
>
> **The tilting route keeps one set of hardware and reorients it.** The tilt-wing in the same study carries six proprotors on a
> tilting main wing and two more on a tilting tail, each directly connected to its own electric motor. Nothing is carried unused;
> the same discs that lift the aircraft propel it, after being turned.

**Section 2 now reads** (Bill 1):

> **This charge has been identified independently, and by a source with no interest in the present argument.** A NASA study sizing
> five VTOL architecture families against a common mission with common tools found the lift-plus-cruise concepts the heaviest of
> the vehicles examined, and named the cause: not the cruise power draw, since the lift-plus-cruise effective lift-to-drag ratio is
> the higher of the set, but *"the extra empty weight items on board in hover."* That is Bill 1 stated by an independent source in
> its own terms: not a failure of engineering, but the cost of an architecture.

**What each uses.**
- **Section 1** consumes the study's **descriptions** of two routes; Section 4 does not repeat them.
- **Section 2** consumes one **finding**.
- **Section 4** is the home: its identity, the three reasons, the mission, the three designs and the test.

**My proposal (R, both vetoable):**
- **Section 1:** *"A NASA study that sizes five VTOL architecture families to one mission describes…"* → *"The NASA sizing study used
  in Section 4 describes the two relevant routes in its own terms."* The two route paragraphs stay: they are Section 1's own use,
  and nothing else in the paper describes the routes.
- **Section 2:** *"A NASA study sizing five VTOL architecture families against a common mission with common tools found…"* → *"The
  NASA sizing study of Section 4 found…"*. The rest of the sentence and the finding stay.

**A problem with the order.** Section 1 and Section 2 come **before** Section 4, so both would point forward to the study's home. The
alternative is that Section 1 is the home of the study's identity, and Section 4 carries the selection basis and the test. That
splits the home, which the rule you just adopted forbids. **My view: forward pointers are acceptable.** A reader meets the study's
name early and its identity where it is used as evidence. Please say if you disagree.

---

## 7. Proposals, to vote

| # | Proposal | My view |
|---|---|---|
| Grok P92 | Step 4's 1.2 % and 9.4 % enter the number-match check as *"tilt-wing against lift-plus-cruise, same study, effective L/D and design gross weight"* — not Section 6's rotorcraft L/De points | **yes** |
| ChatGPT | **Isolation-pair rule:** *"When an external comparison is used as the evidentiary test of a prediction, the body must retain the identities of the compared objects, the common basis on which they are comparable, and the qualification that the comparison is not controlled. Moving any one of these to the supplement while leaving the numerical result in the body is a halt condition."* | **yes** |
| DeepSeek | Mark *"The instrument is now fixed, and it is not modified again."* + *"Everything that follows is measured with it rather than added to it."* as one P71 unit (both are already protected) | **yes** |
| Qwen P1 | Protect the selection-basis sentence: *"It is used for three reasons, stated so that the choice is not merely the one that agreed: it holds the mission fixed across architecture families, it applies one set of tools to all of them, and it reports both quantities this prediction needs."* | **yes** — it is what the external-evidence rule requires the home to carry |
| Qwen P2 | Protect *"None is known to the authors."* | **yes**, word for word (see §3) |
| Qwen P3 | Record Step 4's floor rather than 350 | **recorded as a measurement**; the budget is the author's |
| ChatGPT (hold, not veto) | *"What it predicts is that the amplified weight charge survives the efficiency credit, and on the isolated pair it does so with the credit reduced to nothing."* The lift-plus-cruise design has **no** credit here (8.5 against 8.6), so *"reduced to nothing"* is slightly generous to it. | **Keep.** The sentence before says the lift group *"buys no cruise-efficiency advantage at all here — it is marginally behind"*, which is the exact form. Any other wording would be a new sentence. |

---

## 8. To vote

| # | Item | My vote |
|---|---|---|
| a | C, C-short or C-list (§2) | C-short |
| b | Step 4 draft: veto any sentence; M1, M2; O-a (§4, Appendix A) | M1 yes, M2 yes, O-a no |
| c | S-43: (a), (b) or (c); and your wording for (b) | (b) |
| d | NASA in Sections 1 and 2 (§6), and the forward pointer | yes |
| e | §7 proposals | as in the table |

---

## 9. Your own proposals

As always: anything you see, with your reason.

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## Appendix A — Step 4, the draft (moved text struck through; everything else is the current text, unchanged)

## An independent quantitative check

An accounting proposed by the same people who then use it invites one obvious objection: that the charges were chosen because a particular aircraft happens not to pay them. The objection arises at the title, not at the ledger, so it is answered here — before any configuration is described — by testing a prediction the accounting makes against numbers this work did not produce. **What follows is not a test of the whole framework.** It checks one falsifiable consequence on one independent data set.

**The prediction has two halves, and only the first is a derivation.**

> **First half, derived from Section 2.** A configuration carrying a dedicated lift system pays for it in gross weight, and the payment is amplified: additional empty mass enters through a multiplier that grows as the empty-mass fraction rises, and the same increment is counted again in hover.

> **Second half, not derived.** That the cruise efficiency the arrangement buys does not cover that payment. Section 2 predicts the charge and the amplification; **it does not prove that the credit must lose.** A dedicated lift system raises the empty-mass fraction and may lower the energy fraction at the same time, and which wins is a closure result rather than a consequence of the accounting.

The check tests the second half on independent data, with the first half supplying the reason to expect the outcome: the weight charge is amplified by a multiplier, while the efficiency credit enters linearly through the cruise lift-to-drag ratio. **If some data set showed the credit covering the charge, Bill 1 would not be refuted** — the mass would still have been paid. What would be refuted is the expectation that the amplified charge outweighs the linear credit. **The prediction is also mission-dependent**, and the page would be weaker for hiding it. The mass charge of carried lift hardware is roughly fixed; the efficiency credit accumulates with distance. A long enough mission is where the credit is most likely to cover the charge, and the mission used below is short. **The counter-set is therefore a common-mission sizing study at longer range in which a dedicated-lift configuration is both more efficient and no heavier than one without.** None is known to the authors.

The check uses a NASA study, conducted for its own purposes and with no relationship to the present work, that sizes **five VTOL architecture families** — nine designs in all — against a single mission with common tools and common assumptions; it does not use the three-bill accounting of Section 2 or any framework derived from it. It is used for three reasons, stated so that the choice is not merely the one that agreed: it holds the mission fixed across architecture families, it applies one set of tools to all of them, and it reports both quantities this prediction needs. The mission is 1 200 lb of payload over 75 nautical miles. Three of the nine designs matter here. The turboshaft quadrotor reaches an effective lift-to-drag ratio of 4.9 at a design gross weight of 3 678 lb, with no dedicated lift group: its rotors serve both regimes. **The turbo-electric lift-plus-cruise design reaches 8.5 at 7 271 lb and carries a dedicated lift group — eight lift motors beside its cruise motor. The turbo-electric tilt-wing reaches 8.6 at 6 584 lb with none: eight proprotors, reoriented.**

**The primary comparison is the lift-plus-cruise design against the tilt-wing**, because they isolate the charge: they share the mission, the payload, the turbo-electric propulsion architecture and the presence of a cruising wing. **They are not identical in every other respect** — one stops its lift rotors in the airstream and drives a separate pusher, the other reorients its proprotors on a tilting wing — **but the difference the comparison turns on is that one carries a dedicated lift group through cruise and the other does not.** The comparison is the closest the published set comes to isolating that charge; it is not a controlled experiment. **The tilt-wing is 1.2 % better in effective cruise efficiency and 9.4 % lighter.** The dedicated lift group buys no cruise-efficiency advantage at all here — it is marginally behind — and the design gross weights differ by 687 lb in the tilt-wing's favour. **That figure is the net difference between two architectures, not the measured mass of a lift group**, and the published weight breakdown is what makes it informative rather than merely large. **The published weight breakdown is consistent with the transfer property of Section 2 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce**: its three reported categories account for 580 lb of the 679 lb empty-weight difference, and the remaining 99 lb lies in categories it does not break out (Supplement S4). **And the source states the second half of the prediction in its own words.** Discussing why the all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery weight compared with the quadrotor, *"but not enough to counter the increase in structure and propulsion weight."* That is the efficiency credit conceded and found insufficient, by the authors of the data rather than by the authors of the prediction. **The quadrotor is reported for scale, and the isolation test above is what carries the prediction**: against it the lift-plus-cruise design changes three things at once, and the contrast is in Supplement S4. **The framework does not predict any of these numbers**; without the input fractions it predicts no magnitudes. What it predicts is that the amplified weight charge survives the efficiency credit, and on the isolated pair it does so with the credit reduced to nothing.

**The architecture proposed later in this paper is not the only way to avoid the first charge.** The tilting family avoids it too — it carries no dedicated lift group, it is the lighter of the two matched designs, and an independent set says so. The margin in cruise efficiency is one tenth and nothing is claimed from its direction. **The tilt-wing is consistent with the transfer property of Section 2, in someone else's data.** It does not escape the accounting by avoiding the mass charge; it *moves* the cost — to the mechanism that reorients its propulsors~~, with the actuation, the gyroscopic coupling and the transition control problem that Section 2 assigns to that family~~ **[O-a, optional → S4]**. What separates the tilting family from the configuration described later is not this axis; it is what each pays, and a sizing study does not settle that.

It establishes that one prediction of the accounting holds on data produced elsewhere, for purposes unrelated to this argument. That is the whole of it. **It does not establish that the accounting is complete**, that the three charges are the only costs an architecture pays, or that avoiding them makes an aircraft better. ~~The accounting says an architecture that avoids the three is cheaper in those three currencies and nothing more; a configuration may avoid all three and still be unbuildable, uncontrollable, or unsuited to its mission. Sections 10 and 14 are about exactly that possibility for the configuration proposed here.~~ **[M1 → S4]** **It does not establish anything about the configuration this paper proposes**, which has not yet been described, and which is not in the study used here. A reader who wants to know whether the accounting flatters that configuration will have to wait for Section 11, where it is applied to it and where the answer is not uniformly favourable. **An instrument whose first use is to measure the thing its authors are advocating should be shown working on something else first**, and that is why this section comes before the aircraft. **The instrument is now fixed, and it is not modified again.** **Everything that follows is measured with it rather than added to it.** ~~The next two sections describe the two capabilities the mission asks for, one at a time and each against the family that structurally lacks it, before Section 7 asks whether one aircraft can hold both.~~ **[M2 → S4]**
