# Round 63 — nothing closes until you have seen the result: last round's changes checked, one loss found and repaired, two more changes applied, two drafts for you to approve

> **This is a task. Please answer it now.** Every change is shown before and after, verbatim. Everything
> else is identical to Section 6 of the Round 60 text (`external-review-64`) as amended by the Round 62
> text (`external-review-66`).
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`3fe0e5d`** ·
> `paper/v8/ALL-STEPS.md` SHA-256 `42543502b358bbeabdb6c7bbb06738b0c821c991ced3569cd454e1f8e4562ec9` ·
> `paper/v8/supplement.md` SHA-256 `ae5b0ae7fb830b8183a45b890696a99995651c252bcd3d0ca25db1946163a50f`

---

## 1. A rule from the author: an agreed change is not finished when it is applied

The author wrote this round:

> *"'Everyone agreed, and we ruled that Step 15 is long. I cut it from 2 000 words to 30. I am closing this
> topic now.' That is no way to work. All the effort would be wasted. You have to show the result of the
> agreed action too — and by the result I do not mean how many words it came down to. There may have been
> a misunderstanding."*

**So from now on, an applied change goes through four stages:** agreed → applied → **shown to you
verbatim** → **confirmed by each of you** → closed. If one of you finds a loss or a change of strength, it is
repaired, and the repaired text comes back for confirmation.

**Last round showed why.** Grok found a real loss in a change we had all agreed to (Section 2).

---

## 2. Last round's changes: your confirmations

| Change | G | C | D | Q | Status |
|---|---|---|---|---|---|
| Step 1 — the denial before the contribution | ✓ | ✓ | ✓ | ✓ | **Closed** |
| Step 9 — the dependency table as prose | ✓ | ✓ | ✓ | ✓ | **Closed** |
| Step 10 — the spread table as one sentence | ✓ | ✓ | ✓ | ✓ | **Closed** |
| Step 11 — the closing no longer restates the opening | ✓ | ✓ | ✓ | conditional | **Back to Qwen** (2.2) |
| Step 13 — the sensitivity table to S13, and the dangling reference | ✓ | ✓ | ✓ | ✓ | **Closed** |
| Step 14 — the table of unknowns to S14, a list in the body | **✗ — a clause was lost** | ✓ | ✓ | ✓ | **Repaired, back to all** (2.1) |
| Step 15 — the short close | ✓ | ✓ | ✓ | ✓ | **Closed** |

### 2.1 Step 14: a clause I dropped, found by Grok

When I turned the table row into a list item, I kept two of the row's three parts and dropped the third:
*the allocation of the tip pairs between take-off margin and attitude authority, which compete for the same
propellers.* That is the "second job they were not sized for" that Steps 5 and 7 discuss. It is restored.
**This was my error in applying an agreed change, which is exactly what the new rule exists to catch.**

**As applied last round:**

> - **closed-loop hover control**, including the declined reaction-torque channel and the hover torque
>   residual — a control-allocation study, then simulation;

**Now:**

> - **closed-loop hover control**, including the declined reaction-torque channel, the hover torque
>   residual, and the allocation of the tip pairs between take-off margin and attitude authority, which
>   compete for the same propellers — a control-allocation study, then simulation;

### 2.2 Step 11: Qwen's condition

Qwen noted that the removed sentence *"No charge on this page is a new one…"* was not protected by the
caveat list. Its substance is in Step 11's opening, which is unchanged: *"**No new physical cost term is
introduced here.**"* **That sentence is now on the caveat list**, so a later cut cannot remove it silently.
The removed closing sentence is not restored, because it would repeat the opening. *Qwen: does that meet
your condition?*

---

## 3. Applied this round — all five of us agreed (N2 and N4); please confirm the result

### 3.1 N2 — Step 4's table becomes prose

**Before:**

> | Configuration | Effective L/D | Design gross weight | Dedicated lift group |
> |---|---:|---:|---|
> | Turboshaft quadrotor | 4.9 | 3 678 lb | none — the rotors serve both regimes |
> | **Turbo-electric lift-plus-cruise** | **8.5** | **7 271 lb** | **yes** — eight lift motors and a cruise motor |
> | **Turbo-electric tilt-wing** | **8.6** | **6 584 lb** | **none** — eight proprotors, reoriented |

**After:**

> Three of the nine designs matter here. The turboshaft quadrotor reaches an effective lift-to-drag ratio of
> 4.9 at a design gross weight of 3 678 lb, with no dedicated lift group: its rotors serve both regimes.
> **The turbo-electric lift-plus-cruise design reaches 8.5 at 7 271 lb and carries a dedicated lift group —
> eight lift motors beside its cruise motor. The turbo-electric tilt-wing reaches 8.6 at 6 584 lb with none:
> eight proprotors, reoriented.**

### 3.2 N4 — Step 4's weight breakdown moves to Supplement S4; the conclusion stays in the body

Qwen asked that the conclusion stay in the body. It does, together with the caveat that the reported
categories do not account for the whole difference.

**Before:**

> **The weight breakdown shows the transfer, and it does not close on the categories the table
> reports.** Of the empty-weight difference of 679 lb, structure accounts for 716 lb in the
> lift-plus-cruise entry's disfavour, propulsion returns 146 lb of it because the tilt-wing's
> mechanism is heavier, and battery returns a further 10 lb. **Those three categories account for
> 580 lb of the 679**; the remaining 99 lb lies in empty-weight categories the published table does
> not break out, and this work does not know how it is distributed. **What the three reported
> categories do show is the transfer property of Section 2 — the mechanism giving part of the
> structural saving back — visible inside a weight breakdown this work did not produce.**

**After:**

> **The published weight breakdown shows the transfer property of Section 2 — the mechanism giving part
> of the structural saving back — inside a breakdown this work did not produce**, although the categories
> it reports do not account for the whole difference (Supplement S4).

### 3.3 N4 — Step 4's quadrotor contrast moves to Supplement S4

**Before:**

> **The quadrotor row is retained as a contrast rather than as the test.** Against it the
> lift-plus-cruise configuration is about three-quarters better in cruise efficiency — a factor of
> 1.74 — and nearly twice as heavy, a factor of 1.98. That is the prediction, and it is worth
> being explicit about why it is not a counter-example to it: the efficiency credit is exactly
> what the accounting says a dedicated lift system buys, and the weight charge is exactly what it
> says the buyer pays. The charge survives the credit.
>
> **But that contrast changes three things at once** — dedicated lift group, powertrain, and
> whether a cruise wing exists at all — so it supports a weaker proposition than the prediction as
> stated: that adding a wing and a lift group together still costs mass. Section 2 had already
> called that much obvious. **It is reported for scale, and the isolation test above is what
> carries the prediction.**

**After:**

> **The quadrotor is reported for scale, not as the test**: against it the lift-plus-cruise design
> changes three things at once, and the contrast is in Supplement S4.

### 3.4 What the table's removal changed elsewhere in Step 4

*"The primary comparison is the last two rows"* → *"the last two designs"*. *"This is what the row is actually
for"* → *"what the entry is actually for"*. *"The row therefore does two jobs"* → *"The entry therefore does two
jobs"*. *"The decomposition below is what makes it informative"* → *"the published weight breakdown is what
makes it informative"*. Step 4's quadrotor figure (4.9) stays in the body, because Step 6 compares against it.

**Size now:** 28 329 words, 11 tables in the body. (Round 60: 30 096 and 16.)

---

## 4. Decided — all five of us agree

- **The caveat format.** Each caveat is checked verbatim. If one is compressed, its list entry changes in the
  same commit and the next round shows old and new side by side. **Whether the new wording keeps the old
  strength is checked by you, not by the script** (DeepSeek's addition, taken).
- **B2** — Steps 2, 3 and 4 become one section with three subsections: the charges, the condition, an
  independent check. *(DeepSeek changed its vote.)*
- **B4** — The declined reaction-torque channel: its home is Step 8; Step 7 states the choice in one sentence;
  Steps 1 and 15 keep a clause.
- **B5** — *"The transition is not shown"*: its home is Step 7; Step 10 keeps the 5.4 m result; Step 9 points.
  *(Qwen changed its vote.)*
- **Step 14 becomes its own section, immediately before the conclusion.**

**B4 and B5 need text changes in several steps. Following the new rule, I will bring those as drafts first,
not apply them directly.**

---

## 5. Still open — with my positions, which have moved; please criticise them

**B1 — the soundness of the resulting product. I have moved to Grok's slice.** Grok: *"If they migrate into
soundness, Section 7 can keep the five-class table and lose the failing parts, which is exactly the over-claim
you are trying to prevent."* He is right. So: **the combining section (7 + 8) keeps the count, the strip, the
declined channel, and which parts fail the condition**; **the soundness section keeps Step 9 plus the unsettled
remainder of Step 8** — the hover torque residual, the stopped-state family, what the inventory does not
settle. ChatGPT, DeepSeek and Qwen agreed with my earlier slice; *does Grok's refinement change your vote?*

**B6 — the fixed-pitch efficiency gap. I have moved to Grok's split.** Grok: putting the figure of 14.6 to 21.0
percent into Step 6 without Step 11's refusal (*"No variable-pitch counterfactual was computed"*) *"lets 6 be
read as 'refusing the hub costs twenty percent.' That is a stronger predicate."* So: **the phenomenon lives in
Step 6** (the fixed-pitch blade is what compresses the multirotor margin), and **the number lives in Step 11
with its refusal.** That is ChatGPT's own formula — *"Step 6 = phenomenon, Step 11 = accounting"* — with the
number placed on the page that carries its limit. *ChatGPT, DeepSeek, Qwen: does this meet your vote for 6?*

**B7 — the two open table places. Still open, and my position has not moved:** Step 2's transfer table and Step
9's four-axis table.

| | G | C | D | Q | K |
|---|---|---|---|---|---|
| Step 2 transfer | ✓ | ✓ | ✓ | | ✓ |
| Step 9 four-axis | ✓ | | ✓ | ✓ | ✓ |
| Step 11 build-up | | ✓ | | ✓ | |

The arguments, side by side. **For the build-up** (ChatGPT, Qwen): it is the table that connects the calculations
to the insight — *"where the price of this architecture comes from"* — and without it Bill 2 becomes *"an asserted
percentage rather than a checkable decomposition."* **For the four-axis table** (Grok, DeepSeek, me): it is the one
object against which a desk reader can check every claim at once. **My counter to the build-up case:** its finding
can be audited from four numbers in one sentence — frames 0.0043 and 0.0047, rotors 0.0154 and 0.0169, out of
0.0285 and 0.0381 — and that sentence can replace the table without losing a figure the finding rests on. *Please answer the counter, not just the
vote.*

**ChatGPT's wording for the fourth sentence I protected** — *"That single move is what removes the mechanism"* →
*"That single move is what removes **the need for** the mechanism."* **I agree:** the configuration carries no
reorienting mechanism because it does not need one, and the new wording says that without implying anything was
taken away. *Everyone: agree or not?*

**N1 — Step 3's table as four sentences, revised.** ChatGPT pointed out that *"complexity"* is not measured anywhere
in the paper; saying the tilt mechanism *"is itself … complexity"* is the mirror image of the "simpler" claim the
paper refuses. Revised:

> Depart from any one of those and a charge appears. **Different hardware** costs Bills 1 and 2: the unused set is
> carried for the whole flight and, if exposed, drags. **The same hardware serving only one duty** costs them again:
> a propulsor that lifts and is then carried is a dedicated lift group under another name, whatever it shares with
> the cruise system. **The same hardware serving both duties in a different orientation** is the tilting family:
> Bill 3 is left standing unless a store supplies the hover peak, and the mechanism that changes the orientation
> adds mass and introduces a control problem through the turn. **The same hardware, both duties, one orientation,
> but a different sizing point** leaves Bill 3 — unless the hover peak is supplied from somewhere other than the
> continuously installed power.
>
> Read one at a time, these are ways to pay. Read as a conjunction, they are a condition.

**Two points on it.** *Grok:* the parenthesis that justifies the second departure (*"The second row is stated
separately rather than folded into the first because it does real work later…"*) **was never to be removed.**
Only its word *"row"* becomes *"departure"*. *ChatGPT:* you preferred *"case"* to *"departure"*. **I would keep
"departure"**, because the sentence before the four reads *"Depart from any one of those and a charge appears"*.
The other three accepted it.

**N3 — Step 1's history, compressed. A draft, not applied.** The two subsections (about 570 words) become one
(about 250). The rest moves verbatim to Supplement S1. Everything each of you named as must-stay is in it, except
the two NASA reviews' judgements of the configuration and the cockpit, which move to S1.

> ### The third route is established, and some of its difficulties are inherited
>
> There is a third way to put one set of propulsors into both regimes without reorienting them: **point the thrust
> line at the ground and let the whole aircraft rotate.** It is neither new nor untried nor abandoned. The Convair
> XFY-1 flew it in 1954 and completed six transitions to conventional flight *"before testing was curtailed because
> of engine and gear-box reliability problems"*, and uncrewed tail-sitters have revisited the route continuously
> since. The pilot's spatial orientation and workload, recorded for that programme, were real and severe, **but
> they are not what curtailed the testing**, and they are the one documented obstacle an uncrewed aircraft removes.
>
> **Some of the difficulties were real, internal, and are inherited here.** A tail-sitting vertical descent is
> harder than a runway landing; a tail-sitter on the ground is more exposed to crosswind; and propellers whose
> thrust vectors are all parallel to the body axis produce no rolling moment **by any combination of thrust
> settings**. The reaction-torque channel that other coaxial tail-sitters use about that axis is a choice this
> configuration declines rather than a limit it inherits (Sections 7 and 8). Precise hovering, ground gusts and
> the absence of a thrust-borne rolling moment are configuration facts, and they are inherited.
>
> Three things are available now that were not: electric drive on each individual rotor, sensor-based attitude
> reference, and enough onboard computation that stability need not come from the airframe alone. **The uncrewed
> tail-sitter literature has been exploiting exactly those three for over a decade**, which is why the gap below is
> not a historical one.

**What leaves the body:** the Lockheed XFV-1, which never completed the cycle; the NASA reviews' judgement that the
configuration was a *"good configuration arrangement for low- and high-speed compatibility"*; their list of mechanical
and cockpit difficulties; and the sentence *"the usual account is wrong"*. **The last one is a claim about other
people's accounts that this paper does not need.** *"What follows is therefore not a claim to an empty field"* and
*"Using it is a choice, and so is declining it"* are in the next subsection, which is not touched.

**The protected sentences.** Added at your request: Grok (Step 7's rotation pair), DeepSeek (Step 3's condition;
Step 8's *"These are the parts that fail the escape condition"*), Qwen (Step 2's *"is the origin of all three charges
below"*; Step 11's *"No new physical cost term is introduced here"* as a caveat). Some sentences you proposed were
already protected as caveats: *"The instantiation is therefore partial"*, *"The assembly is not offered as novel because
it is an assembly"*, *"The loop closes; the aircraft is not shown to"* and Step 9's mechanism/transition distinction.
**Grok proposed removing** Step 6's *"Section 7 is where they are combined, and the combination is what this paper is
for"* (*"a corridor … protect the room"*). ChatGPT wants it kept, so it stays. **Total: 145.** *Grok, can you name the
sentence in Step 2 that does the "cost stated first" job you want protected?*

---

## 6. What I am asking

1. **Confirm or reject each result**, one line each: 2.1 (Step 14 repaired), 2.2 (Qwen only), 3.1, 3.2, 3.3, 3.4.
   If a result loses or strengthens anything, quote it.
2. **B1 and B6:** my positions moved to Grok's. Agree, or say what the move gets wrong.
3. **B7:** answer my counter-argument.
4. **The fourth protected sentence:** *"removes the need for the mechanism"* — agree or not.
5. **N1 revised:** confirm the wording, or quote what it changes.
6. **N3 draft:** does it lose, soften or strengthen anything you consider load-bearing? Quote it. If you agree, it
   will be applied and shown back to you next round.

**DeepSeek:** your last reply said *"Q4 (For DeepSeek — I am not DeepSeek, so I skip this)"* and referred to
DeepSeek's earlier positions in the third person. Question 4 was addressed to you. Your answers to Questions 1–3
and 5 were recorded as yours, including your changed vote on B2.

**Sources.** None of this needs a source. PDFs only for priority claims, numbers taken from tables and verbatim
quotations — and say which document you opened in this conversation for any number you give.
