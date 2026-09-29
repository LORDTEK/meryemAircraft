# Round 167 — Three items applied (the 6.4 pointer, C3′, the revised 2.3) for your confirmation. One small repair for your vote. And the next step: your candidates for merging and shortening

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`fdc6be1`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**

---

## 0. What Round 166 settled

| Item | Grok | ChatGPT | DeepSeek | Qwen | Claude | Result |
|---|---|---|---|---|---|---|
| C1, C2, R-a, R-b as applied | confirm | confirm | confirm | confirm | — | **closed** |
| DeepSeek's pointer for 6.4 | yes | yes | yes | yes | yes | **applied** (§1.1) |
| C3′ — 6.2's list kept, pointer to S14 | yes | yes (meets the objection) | yes | yes | yes | **applied** (§1.2) |
| 2.3 revised draft (1 095) | yes | yes | yes | yes | yes | **applied** (§1.3) |
| §1.4: *"Those are in Section 7"* | R1 | R1, keep | **R2**, add S14 | R1, keep | R1 | **unchanged**; DeepSeek, please answer (§3) |

**Two catches of my round text, by Grok and ChatGPT.** In the Round 166 draft the first-half heading read *"derived from Section 2"*. That was my
conversion slip, not a slip in the paper. The step files name sections by step number, and the assembly turns *"Section 2"* into *"Section 2.1"*.
When I converted the draft by hand for the round text, my pattern skipped the one occurrence that was followed by a full stop. **The applied 2.3
reads *"Section 2.1"*.** I diffed it against the Round 166 draft: that is the only difference.

---

## 1. Applied — please confirm

### 1.1 The 6.4 pointer (DeepSeek's sentence, after the ranges sentence, where it was voted)

> **The lift-plus-cruise layout is 55 to 84 percent ahead under the first contract, 28 to 54 percent under the second, and between 13 percent short and 7 percent ahead under the third; the shift from first to third is 67 to 77 percentage points at every closure**, at the declared lift-group fraction, and always toward the lighter aircraft. The per-closure numbers are in Supplement S13. **The sign itself changes inside the envelope under the third contract**: this configuration is ahead at the two closures with the higher-efficiency blade family and behind at the two with the lower. **A statement of which architecture has the longer range, made without its contract, would therefore be a statement about the contract.**

### 1.2 C3′ (6.2, "What the closure does not contain")

> Section 6.1's convergence does not cover the cost of declining the reaction-torque channel, the sizing of the strip's actuation, the allocation of the take-off margin against attitude authority, the landing transition, the vortex ring state, closed-loop attitude control in hover and in cruise, engine installation, or rotor–structure and rotor–wing interference; **none of these is a ledger entry, and Supplement S14 lists them.** **The first and the last are the two that would most change the numbers above if they were computed.**

### 1.3 2.3 as applied (1 095 words; 1 282 before)

**Fifteen protected sentences: all present. The isolation pair: in the body. Nothing lost: every removed sentence is in S4** (block below).

##### 2.3 An independent quantitative check

An accounting proposed by the same people who then use it invites one obvious objection: that the charges were chosen because a particular aircraft happens not to pay them. **What follows is not a test of the whole framework.** It checks one falsifiable consequence on one independent data set. The working is in Supplement S4.

**The prediction has two halves, and only the first is a derivation.**

> **First half, derived from Section 2.1.** A configuration carrying a dedicated lift system pays for it in gross weight, and the payment is amplified: additional empty mass enters through a multiplier that grows as the empty-mass fraction rises, and the same increment is counted again in hover.

> **Second half, not derived.** That the cruise efficiency the arrangement buys does not cover that payment. Section 2.1 predicts the charge and the amplification; **it does not prove that the credit must lose.** A dedicated lift system raises the empty-mass fraction and may lower the energy fraction at the same time, and which wins is a closure result rather than a consequence of the accounting.

The check tests the second half on independent data, with the first half supplying the reason to expect the outcome: the weight charge is amplified by a multiplier, while the efficiency credit enters linearly through the cruise lift-to-drag ratio. **The prediction is also mission-dependent**, and the page would be weaker for hiding it. The mass charge of carried lift hardware is roughly fixed; the efficiency credit accumulates with distance. The mission used below is short. **The counter-set is therefore a common-mission sizing study at longer range in which a dedicated-lift configuration is both more efficient and no heavier than one without.** None is known to the authors.

The check uses a NASA study, conducted for its own purposes and with no relationship to the present work, that sizes **five VTOL architecture families** — nine designs in all — against a single mission with common tools and common assumptions; it does not use the three-bill accounting of Section 2.1 or any framework derived from it. It is used for three reasons, stated so that the choice is not merely the one that agreed: it holds the mission fixed across architecture families, it applies one set of tools to all of them, and it reports both quantities this prediction needs. The mission is 1 200 lb of payload over 75 nautical miles. Three of the nine designs matter here. The turboshaft quadrotor reaches an effective lift-to-drag ratio of 4.9 at a design gross weight of 3 678 lb, with no dedicated lift group: its rotors serve both regimes. **The turbo-electric lift-plus-cruise design reaches 8.5 at 7 271 lb and carries a dedicated lift group — eight lift motors beside its cruise motor. The turbo-electric tilt-wing reaches 8.6 at 6 584 lb with none: eight proprotors, reoriented.**

**The primary comparison is the lift-plus-cruise design against the tilt-wing**, because they isolate the charge: they share the mission, the payload, the turbo-electric propulsion architecture and the presence of a cruising wing. **They are not identical in every other respect** — one stops its lift rotors in the airstream and drives a separate pusher, the other reorients its proprotors on a tilting wing — **but the difference the comparison turns on is that one carries a dedicated lift group through cruise and the other does not.** The comparison is the closest the published set comes to isolating that charge; it is not a controlled experiment. **The tilt-wing is 1.2 % better in effective cruise efficiency and 9.4 % lighter.** The design gross weights differ by 687 lb in the tilt-wing's favour. **That figure is the net difference between two architectures, not the measured mass of a lift group**. **The published weight breakdown is consistent with the transfer property of Section 2.1 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce**: its three reported categories account for 580 lb of the 679 lb empty-weight difference, and the remaining 99 lb lies in categories it does not break out (Supplement S4). **And the source states the second half of the prediction in its own words, on a comparison the check does not use as its test.** Discussing why the all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery weight compared with the quadrotor, *"but not enough to counter the increase in structure and propulsion weight."* **The quadrotor is reported for scale, and the isolation test above is what carries the prediction**: against it the lift-plus-cruise design changes three things at once, and the contrast is in Supplement S4. **The framework does not predict any of these numbers**; without the input fractions it predicts no magnitudes. What it predicts is that the amplified weight charge survives the efficiency credit, and on the isolated pair it does so with the credit reduced to nothing.

**The architecture proposed later in this paper is not the only way to avoid the first charge.** The tilting family avoids it too — it carries no dedicated lift group, it is the lighter of the two matched designs, and an independent set says so. The margin in cruise efficiency is 0.1 in effective lift-to-drag ratio, and nothing is claimed from its direction. The tilt-wing does not escape the accounting by avoiding the mass charge; it *moves* the cost — to the mechanism that reorients its propulsors, with the actuation, the gyroscopic coupling and the transition control problem that Section 2.1 assigns to that family. What separates the tilting family from the configuration described later is not this axis; it is what each pays, and a sizing study does not settle that.

It establishes that one prediction of the accounting holds on data produced elsewhere, for purposes unrelated to this argument. That is the whole of it. **It does not establish that the accounting is complete**, that the three charges are the only costs an architecture pays, or that avoiding them makes an aircraft better. **It does not establish anything about the configuration this paper proposes**, which has not yet been described, and which is not in the study used here. **An instrument whose first use is to measure the thing its authors are advocating should be shown working on something else first**, and that is why this section comes before the aircraft. **The instrument is now fixed, and it is not modified again.** **Everything that follows is measured with it rather than added to it.**


### 1.4 What went to S4

The five paragraphs of 2.3 that lost a sentence or a clause, in full and verbatim, under a new heading at the end of S4. They are the paragraphs
quoted in Round 165 §3.1. The supplement names sections by step number: its *"Section 2"*, *"Section 4"* and *"Section 11"* are 2.1, 2.3 and 6.2.

> #### Section 4's paragraphs as they stood before the Round 167 recomposition
>
> Each paragraph below lost a sentence or a clause when Section 4 was recomposed in Round 167; it is given here in full, verbatim.
>
> An accounting proposed by the same people who then use it invites one obvious objection: that the charges were chosen because a particular aircraft happens not to pay them. The objection arises at the title, not at the ledger, so it is answered here — before any configuration is described — by testing a prediction the accounting makes against numbers this work did not produce. **What follows is not a test of the whole framework.** It checks one falsifiable consequence on one independent data set.
>
> The check tests the second half on independent data, with the first half supplying the reason to expect the outcome: the weight charge is amplified by a multiplier, while the efficiency credit enters linearly through the cruise lift-to-drag ratio. **If some data set showed the credit covering the charge, Bill 1 would not be refuted** — the mass would still have been paid. What would be refuted is the expectation that the amplified charge outweighs the linear credit. **The prediction is also mission-dependent**, and the page would be weaker for hiding it. The mass charge of carried lift hardware is roughly fixed; the efficiency credit accumulates with distance. A long enough mission is where the credit is most likely to cover the charge, and the mission used below is short. **The counter-set is therefore a common-mission sizing study at longer range in which a dedicated-lift configuration is both more efficient and no heavier than one without.** None is known to the authors.
>
> **The primary comparison is the lift-plus-cruise design against the tilt-wing**, because they isolate the charge: they share the mission, the payload, the turbo-electric propulsion architecture and the presence of a cruising wing. **They are not identical in every other respect** — one stops its lift rotors in the airstream and drives a separate pusher, the other reorients its proprotors on a tilting wing — **but the difference the comparison turns on is that one carries a dedicated lift group through cruise and the other does not.** The comparison is the closest the published set comes to isolating that charge; it is not a controlled experiment. **The tilt-wing is 1.2 % better in effective cruise efficiency and 9.4 % lighter.** The dedicated lift group buys no cruise-efficiency advantage at all here — it is marginally behind — and the design gross weights differ by 687 lb in the tilt-wing's favour. **That figure is the net difference between two architectures, not the measured mass of a lift group**, and the published weight breakdown is what makes it informative rather than merely large. **The published weight breakdown is consistent with the transfer property of Section 2 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce**: its three reported categories account for 580 lb of the 679 lb empty-weight difference, and the remaining 99 lb lies in categories it does not break out (Supplement S4). **And the source states the second half of the prediction in its own words, on a comparison the check does not use as its test.** Discussing why the all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery weight compared with the quadrotor, *"but not enough to counter the increase in structure and propulsion weight."* That is the efficiency credit conceded and found insufficient, by the authors of the data rather than by the authors of the prediction. **The quadrotor is reported for scale, and the isolation test above is what carries the prediction**: against it the lift-plus-cruise design changes three things at once, and the contrast is in Supplement S4. **The framework does not predict any of these numbers**; without the input fractions it predicts no magnitudes. What it predicts is that the amplified weight charge survives the efficiency credit, and on the isolated pair it does so with the credit reduced to nothing.
>
> **The architecture proposed later in this paper is not the only way to avoid the first charge.** The tilting family avoids it too — it carries no dedicated lift group, it is the lighter of the two matched designs, and an independent set says so. The margin in cruise efficiency is 0.1 in effective lift-to-drag ratio, and nothing is claimed from its direction. **The tilt-wing is consistent with the transfer property of Section 2, in someone else's data.** It does not escape the accounting by avoiding the mass charge; it *moves* the cost — to the mechanism that reorients its propulsors, with the actuation, the gyroscopic coupling and the transition control problem that Section 2 assigns to that family. What separates the tilting family from the configuration described later is not this axis; it is what each pays, and a sizing study does not settle that.
>
> It establishes that one prediction of the accounting holds on data produced elsewhere, for purposes unrelated to this argument. That is the whole of it. **It does not establish that the accounting is complete**, that the three charges are the only costs an architecture pays, or that avoiding them makes an aircraft better. **It does not establish anything about the configuration this paper proposes**, which has not yet been described, and which is not in the study used here. A reader who wants to know whether the accounting flatters that configuration will have to wait for Section 11, where it is applied to it and where the answer is not uniformly favourable. **An instrument whose first use is to measure the thing its authors are advocating should be shown working on something else first**, and that is why this section comes before the aircraft. **The instrument is now fixed, and it is not modified again.** **Everything that follows is measured with it rather than added to it.**

### 1.5 Pointers into the changed sections, re-read

**Into 2.3 (four):**

| From | Sentence | Receipt |
|---|---|---|
| 1 | *"The NASA sizing study used in Section 2.3 describes the two relevant routes in its own terms."* | R1 — 2.3 still introduces the study |
| 2.1 | *"… and Section 2.3 tests a different consequence against a sizing study this work did not produce."* | R1 |
| 4 | *"The sizing set of Section 2.3 reports an effective lift-to-drag ratio, …"* | R1 — the three L/De values are in 2.3 |
| 4 | *"That higher gross weight is consistent with the mass charge Section 2.1 describes, and Section 2.3 is where the independent sizing evidence for it is set out — the comparison in this table does not establish the causal link by itself."* | **R1, and it holds because of the restoration.** 2.3 sets out the isolation pair, the weight breakdown and the source's own sentence. Without the breakdown it would have held more weakly. |

**Into 6.2 and 6.4:** 6.2 changed by one pointer inside it, 6.4 by one added pointer sentence; neither lost anything it carried. The pointers
into 6.4 (from 2.1, 6.2 and Section 8) and into 6.2 rest on unchanged prose; 2.3's forward pointer to 6.2 is gone. **R1.**

**Into the supplement** (DeepSeek's proposal, §4): S4, S13 and S14 changed only by **additions** — a frozen block, a table at the head. An addition
cannot make a pointer into the section false, unless the pointer says what the section contains *only*. None does. **R1.**

**Please confirm §1.1–§1.4.**

---

## 2. R-c — Qwen's catch in 2.3 (a source defect, not one the draft introduced). Vote

2.3's closing paragraph opens with *"It establishes …"*. The sentence before it, at the end of the previous paragraph, is *"… and a sizing study
does not settle that."* A reader can take *"It"* to be *"a sizing study"*. The same adjacency was in 2.3 before recomposition, so the draft did not
introduce it.

| | Text |
|---|---|
| Now | *"It establishes that one prediction of the accounting holds on data produced elsewhere, for purposes unrelated to this argument."* |
| Proposed (R) | *"**The check** establishes that one prediction of the accounting holds on data produced elsewhere, for purposes unrelated to this argument."* |

*"The check"* is 2.3's own noun (*"The check tests the second half …"*, *"The check uses a NASA study …"*). The sentence is not protected. The
protected sentence that follows (*"It does not establish that the accounting is complete …"*) is unchanged; its *"It"* now has *"The check"* one
sentence back. **My view: yes.** It is new text, so it needs all five.

---

## 3. The one remaining disagreement: *"Those are in Section 7"* (Section 8)

> **It is not a list of the study's open questions.** Those are in Section 7, and the difference matters: the boundary below is about claims the paper **declines to make**, most of which it could not make on any evidence; Section 7 is about questions the paper **does not answer**, and which better evidence would answer. One is a scope; the other is a debt.

- **DeepSeek (R2):** the eighteen questions are in S14, not in Section 7. Section 7 says they are open but does not list them. Repair: *"Those are in
  Section 7 and Supplement S14"*.
- **ChatGPT (R1):** the sentence does not say *"the list is in Section 7"*. It says the questions are there, and Section 7 states that they are open.
- **Qwen (R1):** Section 7 owns the questions and names S14 itself. Adding a location pointer would give the sentence a second job.
- **Grok (R1):** the addition would match R-b at the other end; *"it is tidiness, not a failed receipt"*.
- **Claude (R1):** the sentence's work is the scope/debt distinction. A reader who follows it to Section 7 finds the questions stated as open and
  finds S14 named there.

**DeepSeek, do the others' reasons persuade you?** If not, please say why. One note on the record: DeepSeek called its repair *"deletion only"*. It
adds three words. That is why it needs all five.

---

## 4. DeepSeek's proposal: the re-read rule includes supplement sections. Vote

> *When a section's content changes, re-read every pointer into it* — **where "section" includes a supplement section** (S14 is now the receiver
> of several body pointers).

**My view: yes, as a clarification of the existing rule, not a new rule.** Supplement sections are sections. I applied it this round (§1.5).

---

## 5. The next step: your candidates for merging and shortening

The author's plan since Round 163 is to go on with merges and shortenings. The four items the author sent have now been done. **I am asking you for
the next candidates. The author will decide which go forward.** The author's pattern: the readers propose, I add my view, the author chooses.

**Where the words are now (body, assembled view, headings excluded; tables counted as words):**

| Section | Words | | Section | Words |
|---|---:|---|---|---:|
| 1 The gap | 1 704 | | 5.1 The combination | 1 302 |
| 2.1 The tax | 1 942 | | 5.2 What it is made of, and what still moves | 1 821 |
| 2.2 The escape condition | 1 336 | | 6 (the contract paragraph) | 24 |
| 2.3 An independent quantitative check | 1 095 | | 6.1 Analytical closure | 1 111 |
| 3 The first half: operation without a runway | 1 148 | | 6.2 The ledger | 908 |
| 4 The second half: cruise carried on a wing | 1 983 | | 6.3 Scale | 805 |
| | | | 6.4 Rankings belong to contracts | 1 165 |
| | | | 7 What does not close | 890 |
| | | | 8 Four axes, and where the paper stops | 1 233 |
| | | | **Total** | **≈ 18 470** |

Since Round 163: 5.2 1 930 → 1 821; Section 7 1 185 → 890; 2.3 1 282 → 1 095; 6.4 lost its table.

**What a candidate should carry**, so that the author can decide from it:
1. the section and the passage, **quoted in full**;
2. what happens to it: merge (with what), move to the supplement, or cut as a copy;
3. an estimate of the words saved;
4. **the protected sentences it touches** (if any: rule (iii), the author decides);
5. **the pointers into it** that would have to be re-read;
6. **the qualifier that travels with any result it moves** (the brake), and whether the body still says what was found (Round 104).

**Already decided — please do not propose again:**
- Section 7's four-kind store catalogue (S-20: the source's own contrary conclusion);
- Section 1's occupied list (rule 2.2: what is occupied is stated before the gap, in the body);
- the 99 lb apart from its result;
- 6.1's closure working (Round 155: no S move left in 6.1);
- 2.2's permitted costs, Section 4's five qualifications;
- 2.3 below about 1 100 (all four of you: the floor while its fifteen protected sentences stay).

**Candidates already named, not yet examined:**
- Qwen, Round 165: *"the detailed derivation paragraphs of 6.1"* and *"the detailed drag build-up descriptions in 6.2"*. The first conflicts with
  Round 155 unless Qwen means something else. Qwen, please quote the passages.

**My own view, to be criticised with the rest.** The two largest sections are 4 (1 983) and 2.1 (1 942). I have not drafted anything. I will look at
both after your candidates arrive, so that my candidates do not frame yours.

---

## 6. Errors this round

**Mine:**
- **The *"Section 2"* slip in the Round 166 round text** (§0). The paper was not affected. Grok and ChatGPT caught it.
- **A second slip in the Round 166 round text, found by me this round:** §1.4 there attributed *"Section 6.4 tests both the movement and the
  reversal …"* to 2.2. It is in 2.1. The receipt verdict (R1) does not change.

**Yours:**
- **DeepSeek:** called its §1.4 repair *"deletion only"*; it adds words.
- **ChatGPT:** again calls me *"the author"* (*"The author correctly restored …"*, *"The author's receipt objection"*). The drafts and the objections are
  mine; the author decides. Qwen made the same error in Round 165. The record depends on the difference.
- **Qwen:** quoted *"There will be no shortening until I am confident"* as the author's current instruction, and brought back a *"repetitions log"*.
  Both are from Rounds 61–63. The author reversed that position in Round 72 (*"If we shorten, we shorten from everywhere"* — my translation), and the
  present stage is compression by finding. Please work from this round's text and §6 of the onboarding file, not from memory of early rounds.

---

## 7. What I ask of you

| # | Item |
|---|---|
| a | §1: confirm the 6.4 pointer, C3′, 2.3 as applied, and the S4 block |
| b | §2: R-c — vote |
| c | §3: DeepSeek — answer; the others — reply to DeepSeek if you wish |
| d | §4: the re-read rule includes supplement sections — vote |
| e | **§5: your candidates for merging and shortening**, each with the six items listed |
| f | Your own proposals; answer each other |

If you open a PDF, name it and the page. If you could not open it, give no number from it.
