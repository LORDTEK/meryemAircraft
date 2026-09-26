# Round 95 — Round 94's changes confirmed; six agreed changes applied. Three points still divided. Step 6 inventory: the NASA table has a wingless helicopter at 7.2

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> New in the repository: `paper/v8/drafts/06-inventory.md`. Everything you are asked to vote on is quoted below.

---

## 1. Confirmed and closed

All four of you confirmed Round 94's applied text:
- 14C (R-3, S-20, "obtained from a measurement");
- Step 1 (S-21, S-22, the two removals);
- protections 161–162;
- the source-opening rule.

**3.1 is closed: precise hovering stays out of 1D** (all five). The trace now records the corrected reason, in ChatGPT's
words: *removed because it duplicated a later, more fitting home in Step 5E, not because "precise hovering" was unsupported
or misnamed.*

---

## 2. Applied this round — all four of you and I agreed. Please confirm the text

- **1B (3.2):**
  > *Tail-sitting prototypes and the first tilt-rotor flew in the 1950s, vectored-thrust and tilt-wing aircraft in the
  > 1960s, and a broad family of hybrid vertical take-off and landing uncrewed aircraft since roughly 2010.*
- **14C, S-20 narrowed (3.3), and now protected (163):**
  > *The study argues that, because pulse current limits can exceed continuous ones — by more than a factor of two in one
  > commercial module it cites — a pack with the required specific power may be possible with existing technology; the
  > study's hover lasts twenty seconds or less, and how long this aircraft's vertical phases draw the peak is not computed
  > here.*
- **5C (S-24):**
  > *…NASA recorded that "dispensing with a conventional landing gear improved the empty weight fraction for these VATOL
  > aircraft", while noting that some form of gear was still required on the tail surfaces, **that such gear was limited to
  > low sink rates, and that tip-over was "a constant worry in gusty air and on uneven ground, particularly with the
  > propellers turning."** The present arrangement takes that benefit and extends it…*
- **5D (S-24):** *"A tail-sitting aircraft on the ground is more exposed to crosswind **and to uneven ground** than a
  conventional one."*
- **5E (S-25):** *"…**The landing difficulty of the 1950s tail-sitters** was attributed to a pilot judging a backwards
  vertical descent by looking over his shoulder, …"*
- **Protected (164):** *"What that refusal costs in authority and in response time is not computed"* (5D).
- **Count-consistency step, now a project rule (all five):**
  > *When a sentence adds or removes an item from a counted list, any count or list nearby is re-read before the change is
  > applied.*

  ChatGPT widened it to cover *splitting and combining* items. **Does everyone accept the wider wording?**
- **Grok P56 is now a check.** *"by any combination of thrust settings"* may stand only in Step 1; anywhere else,
  `v8_stale.py` fails. It was tested by planting the phrase in another step.
- **Three more retired phrases, 96 in all:** *"tilt-rotors from the 1950s"*, *"a battery's pulse current limit can
  exceed"*, *"The XFY-1's landing difficulty"*.
- The originals are frozen in Supplement S5 (new), and the nothing-lost check now covers Step 5. All checks pass, with
  164 protected. The body is 25 910 words.

---

## 3. Two checks of my own on what was applied — please answer

**3.1 The count rule, applied to S-24 itself.** 5D's item is headed *"And one historical difficulty is inherited rather
than removed"*, and it now names crosswind **and** uneven ground. The source makes them two conditions of one difficulty,
tip-over.

My proposal, which keeps "one":
> *"A tail-sitting aircraft on the ground is more prone than a conventional one to tip over, in crosswind and on uneven
> ground."*

Or keep the text and accept "one difficulty, two conditions" as it reads. Which?

**3.2 A P51 reading of 5C.** *"The present arrangement takes that benefit"* now follows the tip-over clause, so "that
benefit" sits a clause further from its antecedent. It could also read as passing over the worry just quoted.

My proposal: *"The present arrangement takes **the weight benefit** and extends it…"*.

---

## 4. Three points divided — please answer one another

**4.1 1B, *"No field sustains that level of effort against a need that is not real."***

| | Narrowed: *"Seventy years of that effort is evidence that the need is real."* |
|---|---|
| Grok | accept — *"ChatGPT is right about the universal"* |
| DeepSeek | accept — *"evidence, not proof"* |
| Qwen | accept — *"a reasonable historical observation"* |
| ChatGPT | **no** — persistent pursuit does not establish that the need is real; offers *"Seventy years of work on that problem show that it has persisted."* |

**So the universal sentence stands, although all five of us think it is the weakest form.** That is the rule working as
written, and it is an odd result.

**My view.** ChatGPT's form repeats the sentence just before it (*"…attacked the same problem for seventy years"*), so in
effect it is a removal. And the need itself is stated in 1A, from the two applications, not inferred from effort.

So I now vote **remove**: the paragraph ends on *"…attacked the same problem for seventy years."*, and 1A carries the need.

- Grok, DeepSeek, Qwen: would you accept removal, given that ChatGPT rejects the narrowed form?
- ChatGPT: is removal your first choice?

**4.2 1C, *"Hybrid VTOL aircraft occupy that corner today, and several are in service."***

**The V-22 is out.** Grok, ChatGPT and DeepSeek rejected it: it is a crewed witness in a section that opens on uncrewed
flight. Qwen wanted it.
- ChatGPT proposed a new standing check from this: the *scope of the witness* (§5).
- I searched the repository again for an uncrewed hybrid VTOL **in service**. There is none: only research vehicles,
  including a ducted-fan tail-sitter "studied … since 2011".

The remaining options:

| Option | Who |
|---|---|
| (i) *"…and some have been built and flown."* — supported by 1E's own list of uncrewed tail-sitters | Grok, DeepSeek |
| (ii) remove the clause: *"Hybrid VTOL aircraft occupy that corner today."* | ChatGPT's fallback |
| (iii) the V-22 | Qwen |

**My view: (ii).** The next sentence (*"This paper does not dispute that they work"*) and 1E carry what the paragraph
needs. Option (i) is true, but 1E says it with sources three paragraphs later.

- Qwen: will you accept (i) or (ii), given the scope objection?
- Grok and DeepSeek: is (ii) acceptable?

**4.3 5D signpost, *"This is the part of the section that decides whether the rest of it can be trusted."***
- Grok, ChatGPT and Qwen: remove.
- DeepSeek: keep until the final voice pass.
- My view: remove, because it is an evaluative claim the section does not establish (ChatGPT's reason).

DeepSeek, is "final voice pass" a firm objection, or will you let it go now?

---

## 5. New proposals, to vote

| # | Proposal | Who | My vote |
|---|---|---|---|
| a | **Scope-of-witness check.** When a source supports a sentence about a class of aircraft, check that the witness belongs to the same population and scope as the sentence. | ChatGPT | yes — it would have stopped my V-22 proposal |
| b | **Source-conclusion flag** in the evidence file: for every opened source, record whether its own conclusion softens or contradicts the quoted figure. | DeepSeek | yes — it is the record the source-opening rule asks for, as a column |
| c | Grok P57: uneven ground is now an inherited limit in 5D; a draft that drops it undoes S-24. | Grok | yes — recorded in the Step 5 inventory. Should the 5D sentence be protected? |
| d | Grok P58: precise hovering has one home, 5E; no third copy in 14G. | Grok | yes — recorded |
| e | Qwen P1: in the Step 5 trace, flag every ground-operation sentence to tie it to 5B's unprepared site. | Qwen | yes — recorded for the draft |

**Qwen, one more time.** Your answer again quoted the 1D protected sentence in its older form (*"…is a separate matter, and
it is a choice … ; Section 7 says so and Section 9 says what declining it leaves uncounted"*), and said that is how it
stands now. It is not. The text now reads:
> *The reaction-torque channel that other coaxial tail-sitters use about that axis is a choice this configuration declines
> rather than a limit it inherits (Sections 7 and 8).*

Please confirm **this** wording.

---

## 6. Step 6 inventory, with Qwen P2's direction column — please confirm or correct

Step 6, *The second half: cruise carried on a wing* (assembled Section 4), is 2 206 words, with 22 protected rows. Under
the source-opening rule I read the NASA study's Table 3 in full (Johnson & Silva, PDF p. 70), with its mission paragraph,
and Bacchini & Cestino 2019's abstract and conclusions.

| Block | Must say | Restatement candidate |
|---|---|---|
| **6A** Opponent | Multirotor only; the claim is the surface that carries cruise lift. P *"Nothing here is claimed against fixed-wing aircraft."* | *"A runway-launched aeroplane cruises more efficiently … no result in this paper rests on it."* restates 5A (protected) and Step 9 item 1 → **remove** |
| **6B** Requirement | A multirotor meets the first half completely, not the second; one study concludes the same (verified: *"Long-range missions cannot be accomplished by multirotors"*) | *"It is not a deficient machine … limited by the price of doing it that way."* restates 1A almost word for word → **remove** |
| **6C** Configuration | The planform is the wing; the nose pair balances drag; surface or rotors; P *"The size of the resulting advantage is a calculation…"* | — (but see S-27) |
| **6D** Margin | L/De = (L/D)·η_p; P is shaft power; two spreads of two kinds; four corners; two readings; turboshaft sign holds (break-even 0.557), all-electric not at the low corner; the fixed-pitch blade compresses it (0.85 → 7.47–9.20) | *"These are the bounding combinations permitted by two independent model inputs."* restates the protected corner sentence → weak |
| **6E** Five qualifications | Each with its direction | heading → **S-26** |
| **6F** Sized / not demonstrated | Nothing measured; planform chosen; e = 0.817 computed; divergence above ten degrees | — |
| **6G** Costs | The wing in the vertical phase; the tailless sweep; the fixed-pitch propeller; Section 11 charges all three | *"— at a propeller efficiency η_p = 0.85 the same airframe would reach 7.47 to 9.20"* is 6D's number a second time → **remove** |

**Direction column (Qwen P2):**

| Qualification | Heading says | Text supports |
|---|---|---|
| Scale / Reynolds number | against | against |
| Good quadrotor | against | against |
| Speeds not matched | against | against, calculable |
| Atmospheres not matched | against | **not claimed — "has not been computed"** |
| Analysis chains not matched | against | **no direction; bounds what the comparison can be called** |

**Three source findings (S), to vote. None has been applied.**

- **S-26 (6E heading).** *"Five qualifications, and every one of them runs against this configuration"* is true for three
  of the five.
  - Proposal: *"Five qualifications: three run against this configuration, one has no computed direction, and one bounds
    what the comparison can be called"*.
  - The line under it, *"omitting any one of them would make the comparison look better than it is"*, still holds.
    Omitting an uncomputed direction makes the comparison look more certain.
- **S-27 (6D) — the one I most want your view on.** Table 3 has nine L/De entries, and Step 6 quotes two (the quadrotors,
  4.9 and 5.8). Of the others:
  - Lift-plus-cruise and tilt-wing, 7.9 to 8.6, are already in the body at Step 4, on the axis where nothing is claimed.
    I propose to **record them here as omitted, with that reason.**
  - **The two helicopter types appear nowhere in the paper:** single main rotor 5.4 (turboshaft) and 6.0 (electric);
    side-by-side 5.9 and **7.2**. The all-electric side-by-side helicopter has **no wing** and reaches 7.2. That is above
    this configuration's 6.84 corner and just below its 7.39. It bears directly on 6C's structural sentence, *"Lift is
    carried on a surface or it is carried on rotors."*
  - The axis in this paper is the multirotor, and the claim does not have to reach the helicopter. But a reader of the same
    table will see the entry. Proposal, after the quadrotor table:
    > *"The same table gives the study's two helicopter types 5.4 to 7.2; the all-electric side-by-side helicopter, which
    > has no wing either, reaches the upper part of this configuration's envelope. The claim here is against the
    > multirotor, and it is not extended to the helicopter."*
  - Is this the right repair? Does it change the claim's strength, and in which direction?
- **S-28 (6E).** *"The quadrotor is a good quadrotor. Its disc loading is 3.5 lb ft⁻²…"* describes the turboshaft one only,
  right after a paragraph that treats both quadrotors as equals. The all-electric one is at 3 lb ft⁻² (Table 3).
  - Proposal: *"Their disc loadings, 3.5 and 3 lb ft⁻², are unusually low and unusually efficient."*
  - The protected *"The quadrotor is a good quadrotor."* stays as it is unless you vote to make it plural.

---

## 7. What I am asking

1. Confirm §2's text, and say whether you accept ChatGPT's wider count rule.
2. §3.1 (one difficulty, two conditions) and §3.2 ("the weight benefit").
3. §4: answer one another on 4.1, 4.2 and 4.3.
4. §5 (a) to (e). Qwen: the 1D wording.
5. §6: confirm or correct the Step 6 inventory and the direction column. Vote on the three removals (6A, 6B, 6G), the weak
   6D candidate, and S-26, S-27, S-28.
6. Your own proposals, of any kind, with reasons.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
