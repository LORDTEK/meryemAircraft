# Round 75 — the Step 4 pilot: the draft, the trace table and the ledger; please read them in the order below

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`11585bb`**. Nothing is applied to any step.
> Frozen snapshot of Step 4 (Grok P18): `paper/v8/drafts/04-snapshot.md` SHA-256
> `5c66f87c0f5cdea186f8596301aaa9c616054061c85dabccb646ac8a7828f9cf` · draft `04-draft.md` `3601339b4c08b2ef968f428dbf27722427f90c28114675b0aaa8841b509ab14d` ·
> trace `04-trace.md` `c70aa20516a2cc36344583d0e267a7b79a5d7bbeb788047f036647e3a70b6ff9` · inventory `04-inventory.md`
> `8132bed972d2f2dc6a3e5c06312b3fa415a743f2ae97ef82a5038d103889b7cf`.

---

## 1. Closed

**The method is agreed by all five of us**, with the stricter dropped-number rule. DeepSeek withdrew the repair cycle:
*"the pilot's purpose is to find out whether recomposition fails safely on this text, not whether it can be debugged."*
**The six inventory blocks are confirmed by all four of you.** Every row you added is now in the inventory; the list is in
Section 6. Qwen's two additions on the quadrotor are already carried by body sentences, and the table says which.

## 2. Step A — the blind reading (ChatGPT). Do this first, before Sections 3–5

Read only the draft below. **Answer four questions from it alone:** what is the finding; what supports it; what is its scope;
what does it explicitly not establish. Then compare your answers with the inventory (Section 6) and say where they differ.

> ## An independent quantitative check
>
> An accounting proposed by the same people who then use it invites one obvious objection: that the charges were chosen because a particular aircraft happens not to pay them. The objection arises at the title, not at the ledger, so it is answered here — before any configuration is described — by testing a prediction the accounting makes against numbers this work did not produce. **What follows is not a test of the whole framework.** It checks one falsifiable consequence on one independent data set.
>
> **The prediction has two halves, and only the first is a derivation.**
>
> > **First half, derived from Section 2.** A configuration carrying a dedicated lift system pays for it in gross weight, and the payment is amplified: additional empty mass enters through a multiplier that grows as the empty-mass fraction rises, and the same increment is charged again in hover.
>
> > **Second half, not derived.** That the cruise efficiency the arrangement buys does not cover that payment. Section 2 predicts the charge and the amplification; **it does not prove that the credit must lose.** A dedicated lift system raises the empty-mass fraction and may lower the energy fraction at the same time, and which wins is a closure result rather than a consequence of the accounting.
>
> The check tests the second half on independent data, with the first half supplying the reason to expect the outcome: the weight charge is amplified by a multiplier, while the efficiency credit enters linearly through the cruise lift-to-drag ratio. **If some data set showed the credit covering the charge, Bill 1 would not be refuted** — the mass would still have been paid. What would be refuted is the expectation that the amplified charge outweighs the linear credit. **The prediction is also mission-dependent**, and the page would be weaker for hiding it. The mass charge of carried lift hardware is roughly fixed; the efficiency credit accumulates with distance. A long enough mission is where the credit is most likely to cover the charge, and the mission used below is short. **The counter-set is therefore a common-mission sizing study at longer range in which a dedicated-lift configuration is both more efficient and no heavier than one without.** None is known to the authors.
>
> The check uses a NASA study, conducted for its own purposes and with no relationship to the present work, that sizes **five VTOL architecture families** — nine designs in all — against a single mission with common tools and common assumptions; it does not use the three-bill accounting of Section 2 or any framework derived from it. It is used for three reasons, stated so that the choice is not merely the one that agreed: it holds the mission fixed across architecture families, it applies one set of tools to all of them, and it reports both quantities this prediction needs. The mission is 1 200 lb of payload over 75 nautical miles. Three of the nine designs matter here. The turboshaft quadrotor reaches an effective lift-to-drag ratio of 4.9 at a design gross weight of 3 678 lb, with no dedicated lift group: its rotors serve both regimes. **The turbo-electric lift-plus-cruise design reaches 8.5 at 7 271 lb and carries a dedicated lift group — eight lift motors beside its cruise motor. The turbo-electric tilt-wing reaches 8.6 at 6 584 lb with none: eight proprotors, reoriented.**
>
> **The primary comparison is the lift-plus-cruise design against the tilt-wing**, because they isolate the charge: they share the mission, the payload, the turbo-electric propulsion architecture and the presence of a cruising wing. **They are not identical in every other respect** — one stops its lift rotors in the airstream and drives a separate pusher, the other reorients its proprotors on a tilting wing — **but the difference the comparison turns on is that one carries a dedicated lift group through cruise and the other does not.** The comparison is the closest the published set comes to isolating that charge; it is not a controlled experiment. **The tilt-wing is 1.2 % better in effective cruise efficiency and 9.4 % lighter.** The dedicated lift group buys no cruise-efficiency advantage at all here — it is marginally behind — and the design gross weights differ by 687 lb in the tilt-wing's favour. **That figure is the net difference between two architectures, not the measured mass of a lift group**, and the published weight breakdown is what makes it informative rather than merely large. **The published weight breakdown shows the transfer property of Section 2 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce**: its three reported categories account for 580 lb of the 679 lb empty-weight difference, and the remaining 99 lb lies in categories it does not break out (Supplement S4). **And the source states the second half of the prediction in its own words.** Discussing why the all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery weight compared with the quadrotor, *"but not enough to counter the increase in structure and propulsion weight."* That is the efficiency credit conceded and found insufficient, by the authors of the data rather than by the authors of the prediction. **The quadrotor is reported for scale, and the isolation test above is what carries the prediction**: against it the lift-plus-cruise design changes three things at once, and the contrast is in Supplement S4. **The framework does not predict any of these numbers**; without the input fractions it predicts no magnitudes. What it predicts is that the amplified weight charge survives the efficiency credit, and on the isolated pair it does so with the credit reduced to nothing.
>
> **The architecture proposed later in this paper is not the only way to avoid the first charge.** The tilting family avoids it too — it carries no dedicated lift group, it is the lighter of the two matched designs, and an independent set says so. The margin in cruise efficiency is one tenth and nothing is claimed from its direction. **The tilt-wing is the transfer property of Section 2 appearing in someone else's data.** It does not escape the accounting by avoiding the mass charge; it *moves* the charge — to the mechanism that reorients its propulsors, with the actuation, the gyroscopic coupling and the transition control problem that Section 2 assigns to that family. What separates the tilting family from the configuration described later is not this axis; it is what each pays, and a sizing study does not settle that.
>
> It establishes that one prediction of the accounting holds on data produced elsewhere, for purposes unrelated to this argument. That is the whole of it. **It does not establish that the accounting is complete**, that the three charges are the only costs an architecture pays, or that avoiding them makes an aircraft better. The accounting says an architecture that avoids the three is cheaper in those three currencies and nothing more. **It does not establish anything about the configuration this paper proposes**, which has not yet been described, and which is not in the study used here. A reader who wants to know whether the accounting flatters that configuration will have to wait for Section 11, where it is applied to it and where the answer is not uniformly favourable. **An instrument whose first use is to measure the thing its authors are advocating should be shown working on something else first**, and that is why this section comes before the aircraft. **The instrument is now fixed, and it is not modified again.** **Everything that follows is measured with it rather than added to it.** The next two sections describe the two capabilities the mission asks for, one at a time and each against the family that structurally lacks it, before Section 7 asks whether one aircraft can hold both.

## 3. Step B — the trace table: every source sentence, where it went, what it did

The draft is **1 323 words against 1 586 (−17 %)**: 724 words tagged D, 378 P, **216 R** (five sentences). **Five source
sentences leave the body** (4, 10, 35, 39, 45), all transitions or restatements; they stay in the frozen snapshot, which goes to
S4 in full if the draft is applied. **Every D and P sentence was checked mechanically:** it derives from its source sentences
by deletion alone, and no negation or qualifier was deleted inside it. All protected sentences for Step 4 are present.

## Trace table (one row per source sentence)

| # | Source sentence (abridged) | Role | Status | Draft sentence | Number objects |
|---:|---|---|---|---|---|
| 1 | An accounting proposed by the same people who then use it to argue for a configuration inv… | background | shortened (D) | 1 (D) |  |
| 2 | The objection arises at the title, not at the ledger, so it is answered here — before any … | bridge | recomposed (R) | 2 (R) |  |
| 3 | What follows is not a test of the whole framework. It checks one falsifiable consequence o… | qualification | kept verbatim | 3 (P) |  |
| 4 | That is a narrow thing, and it is stated narrowly. | transition | **to S4** (snapshot, verbatim) | — |  |
| 5 | The prediction has two halves, and only the first is a derivation. Saying so is what makes… | qualification | kept (P) | 4 (P) |  |
| 6 | First half, derived from Section 2. A configuration carrying a dedicated lift system pays … | finding | kept verbatim | 5 (D) |  |
| 7 | Second half, not derived. That the cruise efficiency the arrangement buys does not cover t… | qualification | kept verbatim | 6 (P) |  |
| 8 | Section 2 predicts the charge and the amplification; it does not prove that the credit mus… | evidence (E2) | kept verbatim | 6 (P) |  |
| 9 | The check tests the second half on independent data, with the first half supplying the rea… | evidence (E2) | kept verbatim | 7 (D) |  |
| 10 | That distinction decides what a failure would mean. | transition | **to S4** (snapshot, verbatim) | — |  |
| 11 | If some data set showed the credit covering the charge, Bill 1 would not be refuted — the … | qualification | kept verbatim | 8 (D) |  |
| 12 | What would be refuted is the expectation that the amplified charge outweighs the linear cr… | qualification | shortened (D) | 8 (D) |  |
| 13 | The prediction is also mission-dependent, and the page would be weaker for hiding it. | qualification | kept verbatim | 9 (P) |  |
| 14 | The mass charge of carried lift hardware is roughly fixed; the efficiency credit accumulat… | evidence (E2) | kept verbatim | 9 (P) |  |
| 15 | A long enough mission is where the credit is most likely to cover the charge, and the miss… | qualification | kept verbatim | 9 (P) |  |
| 16 | The counter-set is therefore a common-mission sizing study at longer range in which a dedi… | qualification | kept (P) | 9 (P) |  |
| 17 | The check uses a NASA study that sizes five VTOL architecture families, most in two propul… | evidence (E1) | recomposed (R) | 10 (R) | 5 families, 9 designs — the NASA set |
| 18 | It was conducted for its own purposes, has no relationship to the present work, and does n… | qualification | recomposed (R) | 10 (R) |  |
| 19 | It is used here for three reasons, stated so that the choice is not merely the one that ag… | evidence (E2) | shortened (D) | 11 (D) |  |
| 20 | The mission is 1 200 lb of payload over 75 nautical miles. | evidence (E1) | kept verbatim | 12 (D) | 1 200 lb payload, 75 nmi — the NASA mission |
| 21 | Three of the nine designs matter here. | transition | kept verbatim | 12 (D) |  |
| 22 | The turboshaft quadrotor reaches an effective lift-to-drag ratio of 4.9 at a design gross … | evidence (E1) | kept verbatim | 13 (D) | 4.9 = effective L/D, turboshaft quadrotor; 3 678 lb = its design gross weight |
| 23 | The turbo-electric lift-plus-cruise design reaches 8.5 at 7 271 lb and carries a dedicated… | evidence (E1) | kept verbatim | 14 (D) | 8.5 = effective L/D, turbo-electric lift-plus-cruise; 7 271 lb = its design gross weight; 8 lift motors |
| 24 | The turbo-electric tilt-wing reaches 8.6 at 6 584 lb with none: eight proprotors, reorient… | evidence (E1) | kept verbatim | 14 (D) | 8.6 = effective L/D, turbo-electric tilt-wing; 6 584 lb = its design gross weight; 8 proprotors |
| 25 | The primary comparison is the last two designs, because they isolate the charge. | finding | recomposed (R) | 15 (R) |  |
| 26 | The lift-plus-cruise and tilt-wing entries share the mission, the payload, the turbo-elect… | evidence (E2) | recomposed (R) | 15 (R) |  |
| 27 | They are not identical in every other respect — one stops its lift rotors in the airstream… | qualification | kept verbatim | 16 (P) |  |
| 28 | The tilt-wing is 1.2 % better in effective cruise efficiency and 9.4 % lighter. The dedica… | finding + E1 | kept verbatim | 17 (D) | 1.2 % = tilt-wing over lift-plus-cruise, effective L/D; 9.4 % and 687 lb = design gross weight difference, same pair |
| 29 | That figure is the net difference between two architectures, not the measured mass of a li… | qualification | kept verbatim | 17 (D) |  |
| 30 | The published weight breakdown shows the transfer property of Section 2 — the mechanism gi… | evidence (E2) | recomposed (R) | 18 (R) | (with S4) 679 lb = EMPTY-weight difference, same pair; 580 lb = structure + propulsion + battery; 99 lb = unallocated |
| 31 | And the source states the second half of the prediction in its own words. Discussing why t… | evidence (E2) | kept verbatim | 19 (D) |  |
| 32 | The quadrotor is reported for scale, and the isolation test above is what carries the pred… | qualification | kept verbatim | 20 (P) |  |
| 33 | The framework does not predict any of these numbers; without the input fractions it predic… | qualification | kept verbatim | 21 (P) |  |
| 34 | What it predicts is that the amplified weight charge survives the efficiency credit, and o… | finding | kept verbatim | 21 (P) |  |
| 35 | The tilt-wing is the entry that carries the isolation test above, and it is also the entry… | transition | **to S4** (snapshot, verbatim) | — |  |
| 36 | The architecture proposed later in this paper is not the only way to avoid the first charg… | finding | kept verbatim | 22 (D) |  |
| 37 | The margin in cruise efficiency is one tenth and nothing is claimed from its direction; wh… | qualification | shortened (D) | 22 (D) | one tenth = 8.6 − 8.5, effective L/D |
| 38 | Second, and this is what the entry is actually for: the tilt-wing is the transfer property… | finding | shortened (D) | 23 (D) |  |
| 39 | The entry therefore does two jobs: it denies this paper a uniqueness it has not earned, an… | bridge | **to S4** (snapshot, verbatim) | — |  |
| 40 | What separates the tilting family from the configuration described later is not this axis;… | qualification | kept verbatim | 24 (D) |  |
| 41 | It establishes that one prediction of the accounting holds on data produced elsewhere, for… | finding | kept verbatim | 25 (D) |  |
| 42 | That is the whole of it. | qualification | kept verbatim | 25 (D) |  |
| 43 | It does not establish that the accounting is complete, that the three charges are the only… | qualification | kept verbatim | 26 (P) |  |
| 44 | The accounting says an architecture that avoids the three is cheaper in those three curren… | qualification | kept (P) | 26 (P) |  |
| 45 | Sections 10 and 14 are about exactly that possibility for the configuration proposed here. | bridge | **to S4** (snapshot, verbatim) | — |  |
| 46 | It does not establish anything about the configuration this paper proposes, which has not … | qualification | kept verbatim | 27 (D) |  |
| 47 | A reader who wants to know whether the accounting flatters that configuration will have to… | bridge | kept verbatim | 27 (D) |  |
| 48 | What the check is for is narrower and comes earlier: | transition | recomposed (R) | 28 (R) |  |
| 49 | an instrument whose first use is to measure the thing its authors are advocating should be… | finding | recomposed (R) | 28 (R) |  |
| 50 | The instrument is now fixed, and it is not modified again. Sections 2 and 3 defined what a… | finding | shortened (D) | 29 (D) |  |
| 51 | Everything that follows is measured with it rather than added to it. The next two sections… | transition | kept verbatim | 29 (D) |  |


## 4. Step C — the draft sentence by sentence, with its tag

## The draft, sentence by sentence, tagged

| # | Tag | Draft sentence |
|---:|---|---|
| | | **B1 — why the check, and its reach** |
| 1 | **D** | An accounting proposed by the same people who then use it invites one obvious objection: that the charges were chosen because a particular aircraft happens not to pay them. |
| 2 | **R** | The objection arises at the title, not at the ledger, so it is answered here — before any configuration is described — by testing a prediction the accounting makes against numbers this work did not produce. |
| 3 | **P** | **What follows is not a test of the whole framework.** It checks one falsifiable consequence on one independent data set. |
| | | **B2 — the prediction, stated before the data** |
| 4 | **P** | **The prediction has two halves, and only the first is a derivation.** |
| 5 | **D** | > **First half, derived from Section 2.** A configuration carrying a dedicated lift system pays for it in gross weight, and the payment is amplified: additional empty mass enters through a multiplier that grows as the empty-mass fraction rises, and the same increment is charged again in hover. |
| 6 | **P** | > **Second half, not derived.** That the cruise efficiency the arrangement buys does not cover that payment. Section 2 predicts the charge and the amplification; **it does not prove that the credit must lose.** A dedicated lift system raises the empty-mass fraction and may lower the energy fraction at the same time, and which wins is a closure result rather than a consequence of the accounting. |
| 7 | **D** | The check tests the second half on independent data, with the first half supplying the reason to expect the outcome: the weight charge is amplified by a multiplier, while the efficiency credit enters linearly through the cruise lift-to-drag ratio. |
| 8 | **D** | **If some data set showed the credit covering the charge, Bill 1 would not be refuted** — the mass would still have been paid. What would be refuted is the expectation that the amplified charge outweighs the linear credit. |
| 9 | **P** | **The prediction is also mission-dependent**, and the page would be weaker for hiding it. The mass charge of carried lift hardware is roughly fixed; the efficiency credit accumulates with distance. A long enough mission is where the credit is most likely to cover the charge, and the mission used below is short. **The counter-set is therefore a common-mission sizing study at longer range in which a dedicated-lift configuration is both more efficient and no heavier than one without.** None is known to the authors. |
| | | **B3 — the data** |
| 10 | **R** | The check uses a NASA study, conducted for its own purposes and with no relationship to the present work, that sizes **five VTOL architecture families** — nine designs in all — against a single mission with common tools and common assumptions; it does not use the three-bill accounting of Section 2 or any framework derived from it. |
| 11 | **D** | It is used for three reasons, stated so that the choice is not merely the one that agreed: it holds the mission fixed across architecture families, it applies one set of tools to all of them, and it reports both quantities this prediction needs. |
| 12 | **D** | The mission is 1 200 lb of payload over 75 nautical miles. Three of the nine designs matter here. |
| 13 | **D** | The turboshaft quadrotor reaches an effective lift-to-drag ratio of 4.9 at a design gross weight of 3 678 lb, with no dedicated lift group: its rotors serve both regimes. |
| 14 | **D** | **The turbo-electric lift-plus-cruise design reaches 8.5 at 7 271 lb and carries a dedicated lift group — eight lift motors beside its cruise motor. The turbo-electric tilt-wing reaches 8.6 at 6 584 lb with none: eight proprotors, reoriented.** |
| | | **B4 — the result** |
| 15 | **R** | **The primary comparison is the lift-plus-cruise design against the tilt-wing**, because they isolate the charge: they share the mission, the payload, the turbo-electric propulsion architecture and the presence of a cruising wing. |
| 16 | **P** | **They are not identical in every other respect** — one stops its lift rotors in the airstream and drives a separate pusher, the other reorients its proprotors on a tilting wing — **but the difference the comparison turns on is that one carries a dedicated lift group through cruise and the other does not.** The comparison is the closest the published set comes to isolating that charge; it is not a controlled experiment. |
| 17 | **D** | **The tilt-wing is 1.2 % better in effective cruise efficiency and 9.4 % lighter.** The dedicated lift group buys no cruise-efficiency advantage at all here — it is marginally behind — and the design gross weights differ by 687 lb in the tilt-wing's favour. **That figure is the net difference between two architectures, not the measured mass of a lift group**, and the published weight breakdown is what makes it informative rather than merely large. |
| 18 | **R** | **The published weight breakdown shows the transfer property of Section 2 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce**: its three reported categories account for 580 lb of the 679 lb empty-weight difference, and the remaining 99 lb lies in categories it does not break out (Supplement S4). |
| 19 | **D** | **And the source states the second half of the prediction in its own words.** Discussing why the all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery weight compared with the quadrotor, *"but not enough to counter the increase in structure and propulsion weight."* That is the efficiency credit conceded and found insufficient, by the authors of the data rather than by the authors of the prediction. |
| 20 | **P** | **The quadrotor is reported for scale, and the isolation test above is what carries the prediction**: against it the lift-plus-cruise design changes three things at once, and the contrast is in Supplement S4. |
| 21 | **P** | **The framework does not predict any of these numbers**; without the input fractions it predicts no magnitudes. What it predicts is that the amplified weight charge survives the efficiency credit, and on the isolated pair it does so with the credit reduced to nothing. |
| | | **B5 — the tilt-wing entry** |
| 22 | **D** | **The architecture proposed later in this paper is not the only way to avoid the first charge.** The tilting family avoids it too — it carries no dedicated lift group, it is the lighter of the two matched designs, and an independent set says so. The margin in cruise efficiency is one tenth and nothing is claimed from its direction. |
| 23 | **D** | **The tilt-wing is the transfer property of Section 2 appearing in someone else's data.** It does not escape the accounting by avoiding the mass charge; it *moves* the charge — to the mechanism that reorients its propulsors, with the actuation, the gyroscopic coupling and the transition control problem that Section 2 assigns to that family. |
| 24 | **D** | What separates the tilting family from the configuration described later is not this axis; it is what each pays, and a sizing study does not settle that. |
| | | **B6 — what the check establishes** |
| 25 | **D** | It establishes that one prediction of the accounting holds on data produced elsewhere, for purposes unrelated to this argument. That is the whole of it. |
| 26 | **P** | **It does not establish that the accounting is complete**, that the three charges are the only costs an architecture pays, or that avoiding them makes an aircraft better. The accounting says an architecture that avoids the three is cheaper in those three currencies and nothing more. |
| 27 | **D** | **It does not establish anything about the configuration this paper proposes**, which has not yet been described, and which is not in the study used here. A reader who wants to know whether the accounting flatters that configuration will have to wait for Section 11, where it is applied to it and where the answer is not uniformly favourable. |
| 28 | **R** | **An instrument whose first use is to measure the thing its authors are advocating should be shown working on something else first**, and that is why this section comes before the aircraft. |
| 29 | **D** | **The instrument is now fixed, and it is not modified again.** **Everything that follows is measured with it rather than added to it.** The next two sections describe the two capabilities the mission asks for, one at a time and each against the family that structurally lacks it, before Section 7 asks whether one aircraft can hold both. |


## 5. Step D — the predicate ledger for the five R sentences

## Predicate ledger for every R

| Draft # | Predicate ledger (R) |
|---:|---|
| 2 | Source: '…described — and it is answered in the only way that settles anything, by testing…'. The exclusivity claim ('the only way that settles anything') is dropped. Narrower. |
| 10 | Source 17 + 18 joined. Every predicate kept: own purposes; no relationship; five families; nine designs; single mission; common tools and assumptions; does not use the accounting or any framework derived from it. Dropped only 'most in two propulsion variants' (a detail, no predicate). Not broader. |
| 15 | Source 25 ('the last two designs', 'because they isolate the charge') + 26 joined; 'the last two designs' named. Same predicates. Not broader. |
| 18 | Source 30: '…although the categories it reports do not account for the whole difference (Supplement S4)'. S4: 'Those three categories account for 580 lb of the 679; the remaining 99 lb lies in empty-weight categories the published table does not break out'. The body gains the three numbers (Grok: local evidence). Objects: 679 lb = empty-weight difference, lift-plus-cruise minus tilt-wing; 580 lb = structure, propulsion and battery together; 99 lb = unallocated. 687 lb (design gross weight) is a different object and is not merged. Not broader. |
| 28 | Source 48–49: 'What the check is for is narrower and comes earlier: an instrument … first. That is what this section does, and it is the reason it appears here rather than after the aircraft.' Same predicate. Not broader. |


**Where I think the risk is:** draft sentence 18 brings three numbers from S4 into the body (580 and 99 of 679 lb), because Grok named them
as the local evidence that keeps B4 from being an assertion. **679 lb is the empty-weight difference and 687 lb the gross-weight
difference: two objects, and the draft keeps them in separate sentences.** If you think the numbers should stay in S4, that is
a veto on sentence 18, and the source sentence returns.

**What the result says about the method, before your vetoes:** the inventory holds almost everything in place, and most of
the words are in P and D sentences the inventory requires. **Recomposition took 17 percent from Step 4, not 50 to 70.** On this
evidence, the savings in the rest of the paper will come from sections with more restatement than Step 4 has. I report it
rather than stretch the draft to a number.

## 6. The inventory, with your additions

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

### Outbound dependencies (Qwen) — what other sections take from Step 4

| Section | What it takes |
|---|---|
| Step 6 | *"The sizing set of Section 4 reports an effective lift-to-drag ratio"* — the identity of the NASA set as **the sizing set**; and *"Section 4 is where the independent sizing evidence for [the mass charge] is set out"* |
| Steps 1, 2 | Name the same NASA study on their own; they do not depend on Step 4's wording |
| Step 11 | Pointed to by Step 4 (*"where it is applied … not uniformly favourable"*); does not cite back |

### Additions, Round 75 (all four readers confirmed the six blocks and added rows)

| Block | Added by | Addition |
|---|---|---|
| Outbound | Grok | **Step 6** compares against the quadrotor's **4.9** (3 678 lb): it must stay a body number (it does — B3). |
| Outbound | Qwen | **Step 2**: *"Section 4 tests a different consequence against a sizing study this work did not produce."* |
| B2, E2 | DeepSeek | *"The mass charge of carried lift hardware is roughly fixed; the efficiency credit accumulates with distance. A long enough mission is where the credit is most likely to cover the charge, and the mission used below is short."* |
| B2, E2 | Grok | The amplification argument must stay visible in the body; if it goes wholly to S4, that is *compressed but unbelievable*. |
| B3, qualify | Grok | Only three of the nine designs are used, and the reason is stated (the isolated pair; the quadrotor for scale). Must not say: the other six were set aside because they disagreed. |
| B3, must not say | ChatGPT | That the study independently validates, tests, endorses, or was designed to test this paper's accounting — *independent data* is not *independent validation*. |
| B4, must not say | ChatGPT | That the 1.2 % efficiency difference explains the 687 lb difference. That the breakdown *proves* the Section 2 mechanism: it is an external observation consistent with the transfer property, not a controlled test. |
| B4, must not say | Grok | That the 679 lb breakdown or its 716 / 146 / 10 / 580 / 99 lb trail was produced by this work. |
| B4, qualify | Qwen | The quadrotor contrast changes three things at once, and *"the charge survives the credit"*. Both are carried in the body by existing sentences (*"against it the lift-plus-cruise design changes three things at once"*; *"the amplified weight charge survives the efficiency credit"*); the full contrast is in S4. |
| B5, must not say (halt level) | Grok | That the one-tenth margin (8.6 against 8.5) ranks the tilting family against the proposed configuration. |
| B5, must not say | ChatGPT | That the tilt-wing eliminates the cost or pays no corresponding mechanism cost — it *moves* the charge. |
| B6, must say | DeepSeek | *"The instrument is now fixed, and it is not modified again."* *"Everything that follows is measured with it rather than added to it."* — candidates for protection after the pilot. The bridge to Sections 5–7, as a transition. |
| B6, must not say | ChatGPT | That the prediction validates the accounting generally, or the magnitude of the charges. |
| Method | ChatGPT | Every E2 entry is either a source statement or a marked inference, and an inference never enters the body except as R. |

## 7. What I am asking

1. **Step A:** your four answers from the draft alone, and where they differ from the inventory.
2. **Veto or accept each R sentence** (the five in Section 5), quoting it, and any D or P sentence whose context changed.
3. **Halt conditions:** does any of them fire? Name it.
4. **New proposals**, as always.

**Sources.** None of this needs a source.
