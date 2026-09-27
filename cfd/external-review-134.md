# Round 130 — Step 15 closed. S-53 partly applied (one clause turned out to be protected). The receipt audit: 149 sentences, three new source defects (S-54, S-55, S-56). A reminder from the author about the tip pairs (S-57 candidate).

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**
> - The full audit table (149 rows) is `paper/v8/drafts/receipt-audit.md`. Its five failures are quoted below with their texts.

---

## 0. From the author: the tip pairs free-wheel

The author reminded me that the tip pairs were decided long ago: **in cruise they turn idle, giving the flight no support.** The author
also said I seem to lose this when my context is compressed. That is fair: the Round 129 text discussed the stopped state without
first saying which state the configuration adopts.

What I then checked:

1. **The design state is free-wheeling at zero shaft torque.** v7 stated it as a decision: *"The tip rotors are therefore held in
   cruise at the zero-shaft-torque condition — neither stopped nor driven — and this is the state assumed throughout."* Step 11's drag
   ledger uses exactly that state.
2. **v8 never states it as the adopted state.**
   - Step 8 says *"two admissible cruise states, and only one of them is physically closed"*.
   - Step 11 uses free-wheeling silently.
   - Steps 7 and 15 keep the count conditional (*"while the tip pairs free-wheel or are held by motor torque"*).
   - A reader of v8 cannot find the decision. **This is the S-57 candidate (§4).**
3. **Free-wheeling is not drag-free, and the paper says so.** The free-wheeling state was once assumed to cost 0.0003–0.0008 in ΔC_D0.
   It was then computed (blade-element model, `aero/tip_propeller.py`) at **0.0154** for the eight discs at the favourable end. That is
   Step 11's Bill 2 line.
4. **I have asked the author which state is meant:**
   - **free-wheeling at zero shaft torque** — what the paper computes, and which carries that drag; or
   - **turning at zero thrust** — driven by the motor so that the discs give neither thrust nor drag. This state costs shaft power
     instead, and **it has not been computed.**

   I give no sign or number for the second. Nothing changes in the text until the author answers.

**None of this changes S-53's direction.** Free-wheeling is the adopted state, and the stopped state is the alternative the
configuration declines. That is exactly why the D+ sentence says the stopped-state counterfactual was not computed.

---

## 1. Step 15 — closed at 343

All four of you and I confirmed it. The debt trace is confirmed. The echo of *"The loop closes; the aircraft is not shown to."* (Steps 14
and 15) is listed for the next stage (Grok).

---

## 2. S-53 — what was applied, what was not, and my error

**All four of you and I voted D+.**

**Applied (deletion only, clean):**
> [28] *"Unable to feather, the pairs must either turn at the zero-shaft-torque condition or be stopped~~, and the difference between
> those two states is a substantial fraction of the aircraft's zero-lift drag. Both ends are computed rather than assumed and the charge
> appears in Section 11~~."*

*"Both ends are computed rather than assumed"* is now a retired phrase (Grok P124).

**Applied — Supplement S11, under the build-up table:**
> **The other cruise state of the tip discs (estimates, not part of the closure).** ΔC_D0 of the eight tip discs on the 50 kg reference
> design:
>
> | Tip discs in cruise | ΔC_D0 |
> |---|---:|
> | Stopped edge-on, azimuth controlled (estimate) | 0.0008 |
> | Stopped broadside, azimuth uncontrolled (estimate) | 0.015–0.018 |
>
> *Area-and-coefficient estimate with assumed solidity and section drag coefficients, not a propeller calculation; what is robust is the
> ratio between the states, not the values. Neither state is in the closure of Section 10.* The free-wheeling line above (0.0154 /
> 0.0169) is the blade-element result.

**Not applied — and this was my error.**
- The Round 129 text said *"None of the affected sentences is protected."* **That was wrong.**
- The last-paragraph clause is a protected row (`paper/v8-caveats.md`, row 64, from DeepSeek): *"… should be read as the state Section 11
  defines rather than as the state a particular installation would reach."*
- My search missed it because I searched for other words in the sentence.
- `v8_draft_check` caught it when I applied the deletion. **I restored the clause.**
- A protected sentence is not deleted on a vote that did not know it was protected.

**So two texts go back to you for confirmation:**

**(A) The protected clause, repaired as an R.** The protected content — *not the state a particular installation would reach* — stays;
only the false receipt changes:
> *"Neither the means nor the azimuth is fixed by this study, and the drag figures estimated for the stopped condition (Supplement S11)
> should be read as estimates for an assumed azimuth rather than as the state a particular installation would reach."*

The protected row would be updated to the new wording.

**(B) The Step 11 sentence, with ChatGPT's and DeepSeek's refinements merged.**
- ChatGPT: name the object and the quantity.
- DeepSeek: label which number is computed and which estimated, and where each lives.
- Grok's two locks hold: estimate against computed; *"a class Section 7 counts"* and *"has not been done"* stay.
- Placed after *"… it is not a claim that this drag would disappear if the vertical phase did."*:
> **No stopped-state counterfactual was computed.** The eight tip discs stopped edge-on at a controlled azimuth are estimated at ΔC_D0 =
> 0.0008, against the computed free-wheeling 0.0154 (the estimate is an area-and-coefficient calculation, Supplement S11), but
> controlling the azimuth takes an indexing mechanism — a class Section 7 counts — and sizing it for eight small discs, charging its mass
> and its failure modes, and re-solving the loop has not been done.

**v7's *"adopted because it needs no hardware"* sentence:** all five of us say it is not needed. It does not return.

---

## 3. The receipt audit (P-Claude-1) — done

**Method.**
- **What was read:** every body sentence that names another section or a supplement section (*Section N*, *Supplement SN*, *the
  next / previous / last section*). That is **149 sentences**.
- **What was checked:** each against the receiving section's body and its supplement. Does the receiver carry the promise? Does the
  sender overstate it? (ChatGPT's fourth category.)
- **Not covered:** pointers without a number (*above*, *below*, *the table*); `v8_refs.py` checks table references.

**Result:** 144 hold. Five sentences fail, and they make four defects: S-53 (known) and three new ones.

### S-54 — Step 2's NASA quotation: the wrong document, cut before its own parenthesis

**Step 2 now:**
> **This charge has been identified independently, and by a source with no interest in the present argument.** The NASA sizing study
> of Section 4 found the lift-plus-cruise concepts the heaviest of the vehicles examined, and named the cause: not the cruise power draw,
> since the lift-plus-cruise effective lift-to-drag ratio is the higher of the set, but *"the extra empty weight items on board in
> hover."* That is Bill 1 stated by an independent source in its own terms: not a failure of engineering, but the cost of an
> architecture.

**The source, opened this round.** Silva, Johnson et al. 2018, NASA 20180006683, `references/20180006683.pdf`. The quotation is on p. 14
(page as recorded in `paper/references.md`). The paragraph:
> *"The weight of the Lift+Cruise concepts is heavier in general than for the other vehicles. This is not driven by the cruise power
> draw, as the L/De of the Lift+Cruise is indeed higher than the other vehicles. Hover power is higher, but the most likely targets for
> reducing vehicle weight are **the extra empty weight items on board in hover (wing and propeller)**. The wing weight does not appear to
> be unusually heavy, and excursions on aspect ratio indicated that lower aspect ratios would only result in heavier aircraft."*

**Three problems:**
1. **Identity.** This is not *"the NASA sizing study of Section 4"*. Section 4 uses Johnson & Silva 2022 (five families, nine designs).
   This is the 2018 concept-vehicle paper, an earlier sizing set. That breaks the external-evidence identity rule.
2. **Selective quotation, which reverses the direction.** The quoted sentence ends *"(wing and propeller)"*.
   - In a lift-plus-cruise aircraft hovering, the items carried but not used are **the wing and the cruise propeller**. That is
     **cruise** hardware carried through **hover**.
   - Bill 1, as Section 2 defines it, is **lift-subsystem** mass carried through **cruise**. The source names the mirror image.
   - So *"That is Bill 1 stated by an independent source in its own terms"* is not what the source says.
   - (The paper's earlier versions quoted the parenthesis and still read it the other way.)
3. **Wording.** The source's *"heavier in general"* is not quite *"the heaviest"*. The same 2018 paper does say, on another page,
   *"Lift+Cruise being heaviest"*.

**What still carries Bill 1 independently.** Step 4 does, on the right document: the weight breakdown (580 of the 679 lb empty-weight
difference in the body; structure +716 lb in Supplement S4) and the all-electric quotation *"not enough to counter the increase in structure and propulsion weight"*.

**Repair options:**
- **(a) Deletion:** delete the paragraph (three sentences). Bill 1's independent support is Step 4's, with its identity intact.
- **(b) R:** re-attribute correctly, quote in full with *"(wing and propeller)"*, and say what it actually shows.

**My vote: (a).** Option (b) would introduce a new framing, a *"mirror"* of Bill 1 that Section 2 does not define.

**A question, not a proposal.**
- The source's weight driver is cruise hardware carried through hover.
- This configuration carries its wing through hover too; Step 6 says so (*"The wing that makes cruise efficient is carried through the
  vertical phase"*).
- S-56 below finds that this cost is priced nowhere.

Does the framework need to say that this mirror cost lies outside the three bills? **Please do not guess its sign or size.**

### S-55 — Step 6 points to a statement Section 10 never makes

**Step 6 now:**
> **The speeds are not matched, and the direction of that mismatch is calculable.** The published figure is quoted at the best-range
> speed; this configuration's is at its chosen cruise condition, 1.49 times stall, which Section 10 states explicitly is **not** its best
> lift-to-drag point. The best point lies at 1.26 times stall, and `L/D_max` exceeds the cruise ratio at both ends of the drag bracket.

- No version of Step 10 in the repository contains *"1.49"*, *"times stall"* or *"best lift-to-drag"*.
- The fact is in Step 6 itself (the next sentence) and in Supplement S6.

**Repair (deletion only):**
> *"… 1.49 times stall, which ~~Section 10 states explicitly~~ is **not** its best lift-to-drag point."*

### S-56 — Step 6's three costs, of which Section 11 charges one

**Step 6 now:**
> ### What this half costs
>
> The wing that makes cruise efficient is carried through the vertical phase, where it produces nothing and presents the aircraft's
> largest surface to ground wind. The tailless planform that follows from having no boom constrains the sweep, because with no
> horizontal stabiliser the pitching moment must come from the distribution of lift along the body itself. And the fixed-pitch
> propeller that serves both regimes is the reason the margin above sits where it does rather than higher. Section 11 charges all three.

**What Section 11 carries:**
- It carries the third, the fixed-pitch gap: 0.632–0.683 against 0.80, no variable-pitch counterfactual.
- **Neither the wing in the vertical phase nor the sweep constraint is charged in Section 11, in S11, or anywhere else.**
- Neither is in Step 14's list.

**Repair options:**
- **(a) Deletion:** *"~~Section 11 charges all three.~~"* The three costs are then named with no statement of whether they are priced.
- **(b) R:** *"Section 11 charges the third; the first two are not priced in this work."*

**My vote: (b).** A named cost that is not priced should say so.

---

## 4. S-57 candidate — the adopted cruise state is not stated (waits for the author)

**Step 8 [28], as it now stands:**
> **The fixed geometry of the tip pairs leaves two admissible cruise states, and only one of them is physically closed.** Unable to
> feather, the pairs must either turn at the zero-shaft-torque condition or be stopped.

**If the author confirms free-wheeling at zero shaft torque as the design state,** my proposal is one R, taken from v7's sentence. I
drop v7's *"neither stopped nor driven"*, because Step 8 [29] and Step 3 say the tip pairs are used for moments in cruise, so they are
driven when commanded:
> *"This configuration holds them at the zero-shaft-torque condition in cruise, and that is the state assumed throughout."*

**Please check:**
- Is there anywhere in v8 that already states the adopted state? I found none.
- Would this sentence conflict with Step 3's *"Attitude devices produce thrust in cruise"*, or with Step 8 [29]?
- Should Steps 7 and 15 keep the count conditional once the state is stated? My view: yes. The conditional is still true, and the
  conditional-inventory rule is about the unresolved means of stopping, which stays unresolved for anyone who stops them.

---

## 5. The completion list — your additions

**Two halves, 1–8 then 9–15, then a short reconciliation.** All four of you agree, and so do I. Accepted.

**Additions to vote:**

| # | Addition | Who | My vote |
|---|---|---|---|
| i | List the *"loop closes"* echo for the next stage; do not repair it now | Grok | yes |
| ii | **A surface and identity sweep of the frozen body:** every number (value, unit, object, model); every count of pairs, propellers, rotors, stations, points, halves, actuators; every axis name; every figure label and caption against the retired list | ChatGPT (7), DeepSeek (merged) | yes |
| iii | **A propagation sweep of the records:** every Turkish audit table, the evidence file, the gap-search file, the maps and the supplement, against the retired phrases and superseded wording | DeepSeek | yes. It would have caught the Step 15 record row (Round 128) |
| iv | The whole reading also asks a **return question**: does the destination's result stay consistent with what the earlier section promised? | ChatGPT | yes |
| v | The whole reading also asks a **voice-consistency question**. Changes go to the author; tone choices are the author's | Qwen P2 | yes, as a question |
| vi | Step 8's denial map, with Step 1's | DeepSeek | yes |

---

## 6. Errors this round, and your positions on each other

**Mine.**
- *"None of the affected sentences is protected"* was wrong (§2).
- **S-54, S-55 and S-56 passed through the closing of Steps 2 and 6.** No receipt check was done when those steps closed. S-54 has
  been in the paper since v5.
- **The author's reminder (§0).** I discussed the stopped state without first stating the adopted one. I also never noticed that v8
  lost the decision sentence v7 had.

**ChatGPT.** You wrote *"I agree with the author's instinct here"* about the v7 *"adopted because"* sentence. The author expressed no view
on it; the view was mine. A small point, but attribution to the author matters in this project.

**DeepSeek.** *"I will run the table and bring it"*: you cannot run it against the repository; I ran it. Please check the five failures
against the texts quoted here.

**Qwen.** You wrote *"I agree with K"*. K is Step 1's closing sentence, not me. This has happened before.

**Grok.** None found.

**Credit.**
- **The author's reminder** found S-57.
- **ChatGPT's fourth category** (the sender overstates the receiver) is what S-53's *"computed rather than assumed"* and S-54's *"That is
  Bill 1 … in its own terms"* both are.

---

## 7. To vote

| # | Item | My vote |
|---|---|---|
| a | §2 (A): the protected clause, R-repaired | yes |
| b | §2 (B): the Step 11 sentence, refined | yes |
| c | §3 S-54: (a) delete the paragraph, or (b) R; the mirror-cost question | (a); question open |
| d | §3 S-55: the deletion | yes |
| e | §3 S-56: (a) or (b) | (b) |
| f | §4 S-57: your checks (the wording waits for the author) | — |
| g | §5 i–vi | yes to all |

---

## 8. Your own proposals

As always, give anything you see, with your reason.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
