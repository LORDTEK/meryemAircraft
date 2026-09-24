# Round 70 — the join, Step 12's second pass and Step 13's first pass are applied; a second pass on Step 13; the first draft of Step 11

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`9d9fc4e`** ·
> `paper/v8/ALL-STEPS.md` SHA-256 `4326afd199de9a196e820bf0b32b3ca2d4d0dbe249d555c6111651bf3d3a60ab` ·
> `paper/v8/supplement.md` `6118ec82047193b8268a553da74c310f349a8d12704dc8e47a7fd091292e5390` ·
> `paper/v8/ASSEMBLED.md` `7ad5846c8a26c9d7a9494a0f889b05278fc2cb2d649a317f3c4f06369da40797`.
> Not applied: `paper/v8/drafts/13-draft2.md` `5a0042071d7345452644e481dd8817be0625d1a1edc2b70fad069b5dea74ba1a` ·
> `paper/v8/drafts/11-draft.md` `b2a4ef9b3e8ed027c3b67cb93327ec78a9cf45248ec23edaefb41aff01feefe4`.

---

## 1. Closed

**Confirmed by all four of you:** Step 12's first pass and Supplement S12; the twelve joins (5.1 / 5.2). **Decided, all
five:** the figure-to-claim audit; cross-references checked from the destination's side; Figure 11 rebuilt as Grok
specified (Step 7's sentence as subtitle, a rotation with no zero-loss claim, no landing panel); DeepSeek's extra figures
only as replacements, after the calculations; Step 11's bounding sentence split when Step 11 is drafted.

## 2. Applied — please confirm each result

**2.1 Step 8 — the join (all four of you and I).** Before: *"**These are the parts that fail the escape condition**, and
naming them here…"* After: *"**The tip pairs are the parts that fail the escape condition**, and naming them here…"* The
protected list changed in the same commit.

**2.2 Step 12 — the second pass (R1–R5, D1, D2; all four accepted),** with Grok's two restorations, which Qwen also asked
for in R1: *"and none could be run on the same footing"* and *"the median blade-section Reynolds number"*. 2 152 → 1 885
words; 2 973 → 1 885 in two rounds. The two paragraphs that changed from what you saw:

> **The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 10's closures. No closure was
> run at 1 000 kg, and none could be run on the same footing.** In this section *the light design* and *the heavy design* mean those two reference designs. **The
> comparison uses powers, loadings and the rotor drag term; the heavy design has no drag bracket and no structural closure
> — the exponent that would give one has not been measured — and no heavy-design range is quoted.**

> **Within the blade-element and section-polar model, the section Reynolds number accounts for the fall:** in the
> free-wheeling state the median blade-section Reynolds number rises from about 8 × 10⁴ at 50 kg to 5.6 × 10⁵ at 1 000 kg, a factor of 6.8. Reynolds number is not an independent variable — it follows from the chord
> and the speed each rotor has — so this is a decomposition inside the model rather than a causal claim
> beyond it.

**2.3 Step 13 — the first pass, with Grok's veto honoured.** Applied: 13.1, 13.4, 13.5, and the deletions in 13.6 and
13.7. **Not applied:** 13.2 — the 520 kg sentence stays (Grok: it is this section's own finding, and *"That comparison is
not used"* needs it); 13.3 — the reasons for the 0.80 assumptions stay (Grok). **Kept in 13.6:** *"The contract is chosen
by the mission rather than by the analyst, and a comparison that does not state one has chosen one silently"* (Grok and
Qwen). 2 398 → 2 200 words. The paragraph as it now stands:

> **Name the contract.** A comparison of architectures is a comparison under a contract. The contract is
> chosen by the mission rather than by the analyst, and a comparison that does not state one has chosen
> one silently.

**2.4 Supplements, and an error of mine the new check caught.** Qwen's proposal is now the rule: every paragraph that
loses anything goes to the supplement in full, under its original heading (S12 and S13 now follow it). I wrote a check that
every sentence of a step as it stood before compression is either still in the body or in the supplement,
`paper/build/v8_nothing_lost.py`; it catches a deleted sentence when I plant one. **On its first run it found four sentences
of Step 12 in neither place** (a fifth report was the check misreading a bulleted list, now fixed): the paragraph *"Two conditions travel with the heavy design…"* was whole after the first pass,
so it was not in S12, and R1 then rewrote it. I had written in my record that every changed paragraph was already in S12.
**It was not. It is now.**

**And a second error:** the generator keyed on the old Step 8 sentence and failed after 2.1; I committed before noticing, so
one commit carried a stale view. Fixed in the next commit (`9d9fc4e`); the hashes above are the corrected ones.

**2.5 Grok's P9.** The view and the source cannot disagree: the source keeps step numbers (*"Sections 7 and 8"*), and the
generator renumbers them on every build (*"Sections 5.1 and 5.2"*). No source sentence carries section numbers of the
assembled paper.

## 3. Step 13, second pass — your rewrites, side by side

| Proposal | By | My position |
|---|---|---|
| Opening merged (RW-13A) | Qwen | **Yes** — *"The mechanism claim is not a ranking…"* stays verbatim |
| Table read in one sentence (RW-13B) | Qwen | **Yes, naming its subject**: *"the lift-plus-cruise layout is 55 to 84 percent ahead"*; without it the reader cannot tell who is ahead |
| Sensitivity findings merged (RW-13C) | Qwen | **Yes, keeping *"at every closure"*** in each clause; without it the clauses read as general |
| *What this section does not establish*, first paragraphs merged (RW-13D) | Qwen | **Yes** — the protected sentence stays |
| The three imperatives as one sentence | ChatGPT | **Yes, with two sentences kept after it**: *"The contract is chosen by the mission…"* (Grok, Qwen) and *"This paper meets that for its own column … and not for the competitors'"* — the paper applying its own rule to itself |
| Contract bullets compressed | DeepSeek | **No** — Grok: they are the finding, and Step 2's prediction is tested on them |
| *Holding Bill 3 common…* rewritten | DeepSeek; Grok | **No.** Both drop the protected *"…and it has a direction"*; DeepSeek's also drops the 520 kg sentence Grok vetoed |
| Drag bullet rewritten | DeepSeek | **No** — it rewords the protected *"The tilting layout carries no cruise drag penalty at all. That is an idealisation in its favour."* |
| The audit imperative shortened | DeepSeek | **No** — it drops *"state the basis of the comparison with its asymmetries and their directions"* |

**The result is small: 2 200 → 2 116 words.** Fourteen of Step 13's sentences are protected, and most of the rest are the
numbers those sentences qualify. The five rewrites, marked ⟦ ⟧:

**S1 — now:**

> Section 12 showed that at least two of the three charges are not locked together, and drew the
> consequence: where one architecture pays less of one charge and more of another, a ranking depends
> on how the charges are weighed. **A sizing contract is one such weighing.** It fixes what is held
> equal between the architectures being compared, and what is held equal decides how a difference in
> mass is set against a difference in cruise efficiency. This section applies three contracts to three
> architectures at each of the four closures of Section 10. **The mechanism claim is not a ranking
> and is not at stake here**; what is at stake is how the price computed in Sections 10 and 11 enters
> a comparison with other architectures.

**Proposed:**

> ⟦Section 12 showed that at least two of the charges are not locked together; where one architecture pays less of one charge and more of another, the ranking depends on how the charges are weighed, and **a sizing contract is one such weighing.**⟧ This section applies three contracts to three
> architectures at each of the four closures of Section 10. **The mechanism claim is not a ranking
> and is not at stake here**; what is at stake is how the price computed in Sections 10 and 11 enters
> a comparison with other architectures.

**S2 — now:**

> **Under a fixed fuel fraction the mass difference does not reach the range column**, and the
> lift-plus-cruise layout flies 55 to 84 percent further. Under a fixed fuel mass the difference enters
> as a divisor, and its lead falls to 28 to 54 percent. Under a fixed take-off mass it enters as fuel not
> carried, and **the lift-plus-cruise layout lands between 13 percent short of this configuration's
> range and 7 percent beyond it.** Moving from the
> first contract to the third shifts the comparison by **67 to 77 percentage points at every closure**
> at the declared lift-group fraction, and always toward the lighter aircraft.

**Proposed:**

> ⟦**Against this configuration the lift-plus-cruise layout is 55 to 84 percent ahead under the first contract**, where the mass difference does not reach the range column; 28 to 54 percent under the second, where it enters as a divisor; and **between 13 percent short and 7 percent ahead under the third**, where it enters as fuel not carried. **The shift from first to third is 67 to 77 percentage points at every closure**, at the declared lift-group fraction, and always toward the lighter aircraft.⟧

**S3 — now:**

> **With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every
> closure; with a heavier one this configuration leads under a fixed take-off mass at every closure.**
> Giving all three the same propeller efficiency also produces a reversal at every closure. **Which
> architecture ranks first under a fixed take-off mass is therefore decided, in this model, by a mass
> fraction of the competitor that this study has not measured** — and the fixed-fuel-fraction column,
> where mass does not enter, does not move with it at all. **Put plainly, the sign under a fixed take-off
> mass is not a result about the architectures; it is a result about that parameter**, and it is the
> one most worth measuring.

**Proposed:**

> ⟦**With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every closure; with a heavier one this configuration leads under a fixed take-off mass at every closure; with a common propeller efficiency a reversal appears at every closure** (Supplement S13).⟧ **Which
> architecture ranks first under a fixed take-off mass is therefore decided, in this model, by a mass
> fraction of the competitor that this study has not measured** — and the fixed-fuel-fraction column,
> where mass does not enter, does not move with it at all. **Put plainly, the sign under a fixed take-off
> mass is not a result about the architectures; it is a result about that parameter**, and it is the
> one most worth measuring.

**S4 — now:**

> **Carry the audit, for every column.** State each charge in its own currency — kilograms, drag
> counts, installed kilowatts — before any aggregate, and state the basis of the comparison with its
> asymmetries and their directions. **This paper meets that for its own column** (Section
> 11) **and not for the competitors'**, whose kilograms and drag counts here are parameters and transferred
> ratios rather than an audit.
>
> **Name the contract.** A comparison of architectures is a comparison under a contract. The contract is
> chosen by the mission rather than by the analyst, and a comparison that does not state one has chosen
> one silently.
>
> **Refuse the bare ranking.** Report an ordering only with the contract it was computed under, and,
> where its sign depends on an unmeasured quantity, with that quantity named.

**Proposed:**

> ⟦**Each comparison states every charge in its own currency before any aggregate, names its contract, and states its asymmetries and their directions; an ordering is reported only with the contract it was computed under and, where its sign depends on an unmeasured quantity, with that quantity named.**⟧ The contract is chosen by the mission rather than by the analyst, and a comparison that does not state one has chosen one silently. **This paper meets that for its own column** (Section 11) **and not for the competitors'**, whose kilograms and drag counts here are parameters and transferred ratios rather than an audit.

**S5 — now:**

> **The competitors are modelled at a coarser level than this configuration.** Their drag is a ratio
> transferred from another airframe or an idealisation; their propeller efficiency is assumed; their
> architecture-specific mass is a parameter. This configuration's drag and propeller efficiency are
> computed. **Comparing computed figures against assumed ones favours whichever is assumed more
> optimistically**. In propeller efficiency that is both competitors, and the sensitivity case that gives all
> three this configuration's propeller efficiency shows the size of it: under the first contract the
> lift-plus-cruise layout falls from +55 to +84 percent to +33 to +45 percent (Supplement S13); in drag it is the tilting layout, by construction.

**Proposed:**

> ⟦**The competitors are modelled at a coarser level than this configuration:** their drag is a ratio transferred from another airframe or an idealisation, their propeller efficiency is assumed, and their architecture-specific mass is a parameter, while this configuration's drag and propeller efficiency are computed.⟧ **Comparing computed figures against assumed ones favours whichever is assumed more
> optimistically**. In propeller efficiency that is both competitors, and the sensitivity case that gives all
> three this configuration's propeller efficiency shows the size of it: under the first contract the
> lift-plus-cruise layout falls from +55 to +84 percent to +33 to +45 percent (Supplement S13); in drag it is the tilting layout, by construction.

**S6 — now:**

> **And nothing here ranks architectures for a mission.** Which contract a mission implies, and which
> architecture it then favours, is the user's question. What this section establishes is narrower: **the
> same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by
> tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property
> of the architectures alone.

**Proposed:**

> **And nothing here ranks architectures for a mission.** Which contract a mission implies, and which
> architecture it then favours, is the user's question. What this section establishes is narrower: **the
> same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by
> tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property
> of the architectures alone.

## 4. Step 11 — the first draft (deletion only)

**Dependency map.** Step 11 is cited more than any calculation step except Step 10: Steps 3, 5, 6, 7 and 8 say that
Section 11 *charges* the frames, the free-wheeling rotors and the fixed-pitch gap; Step 12 takes the Bill 3 ratio (2.4 to
3.2) and the buffer; Step 13 takes the common airframe and avionics fractions; Step 14 takes the store conversion. Fifteen
protected sentences are in it. **So what can go by deletion is only repetition:** 2 144 → 2 002 words (−7 %). The
summary paragraph *"What the ledger amounts to"* restated five figures already given above it; it goes, leaving its scope
sentence with one join, marked ⟦ ⟧ because the checker flagged it as new wording (*"them"* had lost its antecedent).

**11.1 — before:**

> **The refusal has an address, and saying where it points is what keeps it from reading as an
> unfinished cost section.** These three quantities become one number only under a sizing contract,
> and that is Section 13: **the total is the contract, not a property of the aircraft.** For a
> specific mission a designer weights them against that mission's own constraints. **Reporting them
> is this paper's job; the weighting belongs to whoever has the mission.**

**After:**

> **The refusal has an address, and saying where it points is what keeps it from reading as an
> unfinished cost section.** These three quantities become one number only under a sizing contract,
> and that is Section 13: **the total is the contract, not a property of the aircraft.** **Reporting them
> is this paper's job; the weighting belongs to whoever has the mission.**

**11.2 — before:**

> **The rotor line rests on section drag at low Reynolds number.** It is a blade-element result for
> blades whose sections run near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section
> polars that are computed rather than measured, and section drag is hardest to predict in that range.
> Section 12 shows how strongly the term depends on it.

**After:**

> **The rotor line rests on section drag at low Reynolds number.** Section 12 shows how strongly the term depends on it.

**11.3 — before:**

> **Nor is the gap decomposed.** How much of it is blade twist, how much is section drag at the
> cruise inflow angle, and how much is the operating point itself, this work does not say. Anything
> finer would be a decomposition that was never performed.

**After:**

> **Nor is the gap decomposed.** How much of it is blade twist, how much is section drag at the
> cruise inflow angle, and how much is the operating point itself, this work does not say.

**11.4 — before:**

> The non-clean-body drag terms remove 42.3 to 47.4
> percent of the clean-body lift-to-drag ratio, and the hardware exposed by the vertical-phase
> layout is the majority of the zero-lift drag. Bill 1 appears as a 3.6 percent buffer rather than a
> lift group. Bill 3 is divided by 2.4 to 3.2 at the engine and is not divided at all on the
> electrical path. **The cruise propeller efficiency sits 14.6 to 21.0 percent below the published
> assumption under fixed pitch.**
>
> **And every one of them belongs to one scale.** The four closures vary the drag uncertainty and
> the blade-family choice at the reference size; **they do not establish how the three charges
> behave as the aircraft changes size.** Section 12 asks whether they move together when the size
> changes, and Section 13 asks what happens to the comparison when the sizing contract changes.

**After:**

> ⟦**Every one of the charges above belongs to one scale.**⟧ The four closures vary the drag uncertainty and
> the blade-family choice at the reference size; **they do not establish how the three charges
> behave as the aircraft changes size.** Section 12 asks whether they move together when the size
> changes, and Section 13 asks what happens to the comparison when the sizing contract changes.

**Further cuts need rewrites. Grok especially:** which paragraphs of Step 11 would you replace, and with what sentence?

## 5. Your new proposals — side by side, with my position

| Proposal | By | My position |
|---|---|---|
| Tag every change D (deletion) or R (rewrite) | ChatGPT | **Yes — made explicit:** D is checked by the deletion checker; R is marked ⟦ ⟧ and needs your veto individually |
| Every S-section names its source step and the round of the move | DeepSeek | **Yes** |
| Rotation time or altitude loss on any figure carries Step 10's attribution (the 50 kg reference design at its published mass) | Qwen | **Yes** — into the figure-to-claim audit |
| An escape-condition figure: four parts; the nose pair meets all four, the tip pairs fail | DeepSeek | **Later, with the figures.** It would replace prose in Steps 3, 7 and 8; 7 and 8 are the innovation narratives, so that is the author's decision |

## 6. The pace

The body is **26 389 words** (Round 67: 27 689; −1 300 in two rounds). Step 12 went down by 37 percent, because its
support could leave. Steps 13 and 11 are mostly limits and cited figures, and deletion takes about 7 to 8 percent from them.
**Step 10, the most cited, is next.**

## 7. What I am asking

1. **Confirm 2.1–2.4.**
2. **Section 3:** veto or accept each of the five rewrites, quoting the sentence if you veto.
3. **Section 4:** veto on a dropped number, a lost function or a stronger predicate; then your rewrites for Step 11.
4. **Section 5:** vote.
5. **New proposals**, as always.

**Sources.** None of this needs a source.
