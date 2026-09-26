# Round 108 — Steps 12 and 13 closed; S-38 repaired (one clause still divided); an error of mine in J29; and Step 14 as result sentences

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`d83c843`**.
>
> The Step 14 draft is `paper/v8/drafts/14-recomposed.md`. Answer one another as well as me; where you still differ, say why
> to the one you differ from.

---

## 1. Closed, and applied

**Steps 12 and 13 are confirmed by all four of you, and closed.**

**Applied, unanimously — please confirm the words:**

**S-38, Step 13:**
> **Which architecture ranks first under a fixed take-off mass is therefore decided, in this model, by quantities this study
> assumes for the competitor rather than measures: its lift-group mass fraction and its propeller efficiency.** **Put plainly,
> the sign under a fixed take-off mass is not a result about the architectures; it is a result about those quantities.**

**S-38, Step 9:**
> *"…under one of them its sign changes inside the envelope and turns on quantities of the competitor that are assumed rather
> than measured."*

**Also applied:**
- **D26b, P27 and P28 are one protected unit**, and D26b is newly protected.
- **Three retired phrases** enforce Grok's P81, so the scan catches any return of the single-parameter form:
  - *"turns on a mass fraction of the competitor"*;
  - *"by a mass fraction of the competitor that this study has not measured"*;
  - *"it is a result about that parameter"*.
- **D31 is protected** (*"A larger aircraft of this type turns more slowly, and must"*). J30 is not.
- **The comparison-construction audit list** is adopted, and *"transferred from a different airframe"* is protected.

There are now 174 protected sentences. The originals of all the changed sentences are in S9 and S13.

**J29, Step 12 — my error, repaired, to confirm.** The short form you all accepted was my proposal:

> *"The fixed-pitch gap also widens slightly with size, to 16.4 to 22.9 percent at the heavy design (Supplement S12)."*

**It dropped *"as in Section 11, no variable-pitch counterfactual was computed"*.** That is a negative qualification, and our own
audit list, adopted two rounds ago, says every *"not …"* is traced. I proposed a sentence that lost one, and none of us caught
it. The applied text is your wording with the qualifier restored:

> *"The fixed-pitch gap also widens slightly with size, to 16.4 to 22.9 percent at the heavy design (Supplement S12); as in
> Section 11, no variable-pitch counterfactual was computed."*

**Please confirm.**

---

## 2. Still divided — the last clause of P28

The clause is *"and they are the ones most worth measuring"*.

| | Position and reason |
|---|---|
| **Grok** | Keep it. Each quantity settles the sign alone, so the judgment is the same judgment twice, not a new ranking. |
| **Qwen** | Keep it. Dropping it loses the paper's guidance on which measurements are most informative; the object widens, the predicate does not. |
| **ChatGPT** | Drop it. The table establishes sensitivity, not a research-priority ranking. The repair closes the defect without it. |
| **DeepSeek** | *"and both are worth measuring"*, or drop it. |

Until you agree, **P28 ends at "those quantities."** The singular clause could not survive the repair, and every replacement has
someone against it.

**My view:** I lean toward ChatGPT. *"Most worth measuring"* is a comparison against every other measurement the paper lists as
open (Step 14 lists fifteen), and the sensitivity table does not rank those.

Qwen's point is real, though. The guidance is not lost if it lives where the measurements are listed: in Step 14's unknowns,
where *"the competitor's lift-group mass"* is already an item with what would settle it. **To Grok and Qwen:** would you accept
the clause dropped here if Step 14's list carries the competitor's propeller efficiency as an item too (§4 (b))?

---

## 3. Step 14 — the draft

Your lists are side by side in the draft file (§1).

**Two checks on the lists:**
- Every DeepSeek and Qwen quotation is in the body, except one. DeepSeek's *"The first obstacle is known and named: the energy
  store"* reworks the heading and opening sentence; it is not a sentence of the source.
- Grok did not open the step and said so. Every figure Grok recalled matches the body.

**Rules the draft follows:**
- **The obstacle leads** (Grok P82, Qwen R107-P2).
- **Each unknown stays a question** (Qwen's debt/scope guard). No sentence says *"cannot"*.
- **Each store figure keeps its rating and provenance** (ChatGPT's rating-identity audit, which is to vote). The table in the
  draft file's §3 lists each figure with its rating.

**The plain fact on length: about 1 145 words, 83 % of the source,** the highest so far. There are two reasons:
- 240 protected words, most of them in the store paragraph;
- the fifteen unknowns, named item by item, about 110 words.

**What moved:**
- the re-closure table, with each row's result kept in R13 and D15;
- the pack details: 13.5 kg, 10.68C, four minutes, 55.1 °C against 60 °C;
- the bus arithmetic;
- *"what would settle it"* for each unknown.

> ## What does not close
> 
> [J1] Section 10 closed the sizing loop on a declared package and said that whether an aircraft can be built to it is a different question. **This section is where that question is answered, and for the first item the answer is no.** [D2] Section 9 called this section a debt: questions the paper does not answer and that better evidence would. It is stated in that order — first the obstacle that is known, then what is not known.
> 
> ### First, the known obstacle: the energy store
> 
> [J3] **Every closure in Section 10 carries a buffer of 3.6 percent of take-off mass**, an input rather than a result (Sections 11 and 12). Taken at the electrical bus, where the buffer sits, **the four closures ask the buffer for 4.7 to 5.2 kW per kilogram of buffer to hover, and 5.5 to 6.1 kW per kilogram of buffer to leave the ground** with the tip pairs at full thrust (Section 5).
> 
> [D4] **What has been measured is a fraction of that, and the figures available are of four different kinds.** [D5] A 24-series nickel–cobalt–manganese pack designed, bench-tested and flown in a 210 kg-class electric VTOL aircraft is rated, as a flown system, at 0.892 kW per kilogram continuous; its unit pack, discharged on the bench at its highest tested rate, delivered on average about 1.5 kW per kilogram (Supplement S14). A NASA-funded design study adopts 4 kW per kilogram and describes that figure as about twice that of existing batteries. [P6] The same study notes lithium-polymer figures in the literature as high as 3 kW per kilogram, which it cites rather than measures; against that figure the take-off demand is 1.8 to 2.0 times. [P7] The study argues that, because pulse current limits can exceed continuous ones — by more than a factor of two in one commercial module it cites — a pack with the required specific power may be possible with existing technology; the study's hover lasts twenty seconds or less; this aircraft's vertical phases occupy about a minute in all (Section 2), and how long each draws the peak is not computed here.
> 
> [D8] **The take-off demand of Section 10's closures is 3.7 to 4.1 times the bench rate — the highest figure obtained from a measurement — and 6.2 to 6.8 times the flown system's continuous rating**; hover alone is 3.1 to 3.5 times the bench rate. [P9] The comparison is between unlike ratings: a peak demand held through the vertical phases, a bench average over minutes, a continuous rating, a design assumption, and a literature figure the study cites without its rating. [P10] **The gap is real on every one of them; the factor quoted is peak demand against bench average.** [P11] The package Section 10 closes on does not exist with any store the sources consulted here report as built.
> 
> [J12] **Closing the loop on a measured store is a sensitivity of that package, not a second aircraft**: the buffer is derived inside the loop from the take-off demand at a given specific power, and everything else is Section 10's. [R13] At the bench rate of about 1.5 kW per kilogram the loop closes at 94.6 to 101.2 kg, 76 to 81 percent heavier, with a buffer of 13.4 to 14.7 percent; at the design study's 4 kW per kilogram it closes 6 to 8 percent heavier (the table is Supplement S14). [P14] **These masses are the Section 10 package with one input changed. They are not a structural closure at 100 kg**, and whether the airframe fraction holds at twice the mass it was set at is not established. [D15] If Section 10's take-off masses are retained instead of re-closing at the bench rate, the payload falls to about 7 kg rather than 13; at the flown system's continuous rating the loop only just closes, and at the unit pack's continuous rating it does not close at all.
> 
> [D16] **This is where the coupling Section 12 found is paid**: the buffer is the conversion the escape condition permits — kilowatts of hover peak paid in kilograms of store. [P17] **The escape from Bill 3 is real in the sense Section 3 defined it, and its price depends on a component whose required performance has not been demonstrated.**
> 
> ### What the obstacle reaches, and what it does not
> 
> [D18] **It reaches every number that describes this aircraft at Section 10's masses**: the closed masses of 52.3 to 57.5 kg and the 13 kg payload assume the store. [P19] The ranges of 927 to 1 233 km survive the re-closure only because the fuel fraction is held, on an aircraft three-quarters heavier; they do not survive as 13 kg carried that far on a store that has been built. [J20] The vertical phase that Section 5 reports as sized was sized with this store in it, and Section 13's orderings were computed with the store held common at 3.6 percent; how they would move with a measured store is not computed.
> 
> [P21] **It does not reach the mechanism claim.** [D22] That is a statement about hardware, and a heavier store adds no pivot. [D23] **Nor does it reach the cruise-efficiency comparison of Section 6 as a ratio**: effective lift-to-drag ratio has no mass in it. As a comparison of aircraft, that section describes the configuration at Section 10's masses, which the store does reach.
> 
> ### Then what is not known
> 
> [D24] The remaining items are not known obstacles; they are questions this work has not answered, and each is listed with what would settle it in Supplement S14. [R25] They are:
> - the pitching moment through the transition;
> - section drag at low Reynolds number;
> - the tip pairs' stopped cruise state;
> - the buffer's energy, not only its power;
> - the electrical path at peak;
> - the airframe's mass;
> - the strip and the fairing;
> - closed-loop hover control, including the declined reaction-torque channel, the hover torque residual and the allocation of the tip pairs between take-off margin and attitude authority;
> - vertical descent and the landing transition;
> - ground handling and landing loads;
> - the competitor's lift-group mass;
> - rotor–structure and rotor–wing interference;
> - engine installation;
> - blade-family selection;
> - atmosphere.
> 
> [D26] **None of these is a small correction to a known quantity.** [D27] Two of them need validated data rather than more of the computation already done: the transition moment, because three methods have been tried against it and disagree, and the low-Reynolds section drag, because the one method used here is least reliable exactly there.
> 
> ### What this section amounts to
> 
> [P30] **The loop closes; the aircraft is not shown to.** [D31] At the energy store the paper can name the gap exactly, in specific power and in take-off mass; everywhere else it can name only what would settle the question. [D32] **The architecture claim — that the configuration is arranged to change regime with no mechanism that reorients a propulsor — is a count of hardware, and nothing in this section reaches it.** What this section reaches is the aircraft, and the paper has not claimed the aircraft. [D33] The last section returns to the four axes of Section 9 and states what is claimed on each.

---

## 4. To decide

**(a) The unknowns' names** (R25, about 110 words). Keep them in the body, or move them and keep only *"fifteen questions,
listed with what would settle each in Supplement S14"* plus the two named in D27 (about 1 030 words)?

My view: keep them. The debt/scope guard asks that each debt stay visible, and a count alone hides which debt is which.
DeepSeek and ChatGPT sent the list to the supplement last round; Qwen kept a summary; Grok kept *"the list of debts in words"*.
**Answer one another.**

**(b) S-38's reach into Step 14.** The unknowns list has *"the competitor's lift-group mass — measured inventories of
lift-plus-cruise aircraft of this class"*. After S-38, the competitor's propeller efficiency decides the same sign, and it is
assumed (0.80), not computed. **Proposal:** a sixteenth item in S14's full list, and in R25's names: *"the competitor's cruise
propeller efficiency — computation of that propeller at its operating point"*.

This adds a predicate to the paper. It is not in the source, and it is a consequence of S-38. D24's count would then read
sixteen, and D27's *"Two of them"* is unaffected.

**(c) Veto any sentence of the draft by number.** Watch R13 and R25 especially.

---

## 5. New proposals, to vote

- **ChatGPT — rating-identity audit for store figures:** value + unit + rating type + provenance + duration. My view: yes, as
  an audit list, like the other two. §3 of the draft file shows it applied.
- **Grok P82** and **Qwen R107-P1/P2** are followed in the draft. They become rules if you confirm the draft.

**For the author's later redistribution.** DeepSeek and Qwen independently named the same framework example as working that
could move: Step 2's example vehicle (100 N m⁻², L/D 15, 30 m s⁻¹, the geometric 3.2), with its result sentence staying.
Grok named the Bacchini retraction arithmetic. The definitions you all said must stay are:
- the charge/currency distinction;
- the escape condition and its four parts;
- the three bills' definitions;
- the refutation test;
- Step 2's root sentence.

All of this is recorded in `deferred-decisions.md` E8.

---

## 6. To vote

| # | Item | My vote |
|---|---|---|
| a | Confirm S-38 as applied, and J29 with the restored qualifier | confirm |
| b | P28's last clause: keep / *"both are worth measuring"* / drop | drop, if (d) is adopted |
| c | Step 14 draft: veto by number | no veto |
| d | A sixteenth unknown: the competitor's cruise propeller efficiency | yes |
| e | Unknowns' names in the body or not | keep |
| f | The rating-identity audit | yes |

---

## 7. Your own proposals

As always: anything you see, with your reason.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
