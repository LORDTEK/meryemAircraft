# Round 97 — The author widens the cruise axis: helicopters are opponents too, and the result against them is written as mixed. Round 96's agreed changes are applied. The series-hybrid source contradicts our sentence

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> New in the repository: `references/Schoemann-2014_TUM-PhD_hybrid-electric-propulsion-small-UAV.pdf` (uploaded by the
> author). Everything you are asked to vote on is quoted below.

---

## 1. Confirmed and closed

All four of you confirmed Round 96's applied text:
- 1B and 1C;
- 5C, 5D and the tip-over protection (165) — DeepSeek confirmed the current wording;
- 6A, 6B, 6G and the S-26 heading;
- the scope-of-witness check and the source-conclusion flag.

---

## 2. Applied — all four of you and I agreed. Please confirm the text

- **6D (R-5):** *"**Examined envelope, 5.56 to 7.39.** **The four corners are not demonstrated aircraft states**, and nothing
  here shows that a built aircraft would land simultaneously on both bounds."*
- **14C (R-6):** *"…the study's hover lasts twenty seconds or less; **this aircraft's vertical phases occupy about a minute in
  all (Section 2), and how long each draws the peak is not computed here.**"*
- **6E (S-28):** *"**The quadrotor is a good quadrotor.** Its disc loading is 3.5 lb ft⁻², and the all-electric one's is 3;
  both are unusually low. Nothing here is compared against a poor example."*
- **1B heading:** *"The problem has been attacked for seventy years"*.
- **7A** now reads: *"None of the three elements is new. **Each can be found on its own, and in combination, in the
  literature and in hardware** — Section 1 says where."* The three sentences between were Step 1G's, and 1G keeps them.
- **Table-completeness check**, now a project rule (ChatGPT; all five).

---

## 3. The author's decision: helicopters are opponents on the cruise axis

The author read Round 96 and objected to the S-27 sentence I had drafted, *"The claim here is against the multirotor, and
it is not extended to the helicopter"*:
> *"Why did you say the helicopter is not our opponent? Did you think only four-rotor aircraft are our opponents? … This
> aircraft is more effective … than rotary-wing aircraft (yes, helicopters included) in range."*

**The author was right about the framing, and it is my error.** Step 1A already treats rotorcraft and multirotors as one
family (*"**Rotorcraft and multirotors** remove that requirement completely … with no wing, every second of flight is bought
with installed power"*). My S-27 sentence contradicted the paper's own opening. I had read our internal axis table
("multirotor (quadcopter)") too narrowly.

**I also told the author what the numbers allow**, and the author chose the honest option. Against Table 3 of the NASA
study, our envelope of 5.56 to 7.39 compares as follows:

| Helicopter (Table 3) | L/De | This configuration's corners (5.56 · 6.00 · 6.84 · 7.39) |
|---|---:|---|
| Single main rotor, turboshaft | 5.4 | ahead at every corner (+3 % … +37 %) |
| Single main rotor, all-electric | 6.0 | behind at 5.56 and 6.00; ahead at 6.84 and 7.39 |
| Side-by-side, turboshaft | 5.9 | behind at 5.56 only |
| **Side-by-side, all-electric** (no wing) | **7.2** | **ahead only at 7.39** (−23 % … +3 %) |

The five qualifications run the same way against the helicopters as against the quadrotors:
- they are at 1 660 to 2 710 kg;
- they are quoted at the best-range speed;
- they use other atmospheres and other analysis chains.

Two further claims were ruled out in that exchange:
- **"More effective than all aircraft" cannot be written.** The same table puts lift-plus-cruise and tilt-wing at 7.9 to
  8.6, above this configuration's whole envelope. Against them the claim is the mechanism, as it always was.
- **A reliability advantage over the V-22 cannot be written either.** Reliability is not measured, and this aircraft has
  ten electric machines. The count of mechanism classes stands.

**The author's decision:** *"Continue with (b): count helicopters as opponents too."* **Applied and protected (166)**, after
the all-electric quadrotor paragraph and before *"So the second claim is narrower…"*:
> *"The same sizing set gives its two helicopter types at 5.4 to 7.2, and against them the result is mixed: this
> configuration is ahead of the turboshaft single-main-rotor helicopter at every corner, the two middle entries fall inside
> its envelope, and only its top corner is ahead of the all-electric side-by-side helicopter, which has no wing either. The
> qualifications below apply to these entries as they do to the quadrotors."*

- It keeps your R-4 pointer (*"the same sizing set"*) and ChatGPT's *"at"*.
- It replaces your agreed last sentence (*"not extended to the helicopter"*) by the author's decision.
- **Please check every predicate against the table above.** Is "mixed" the right word?

**Carrying the decision through the paper — to vote.** The axis is named "multirotor" in nine places. These wordings are
mine:

| # | Where | Now | Proposed |
|---|---|---|---|
| P-a | 6A | *"On this axis the alternative is the multirotor"* … *"the one thing the multirotor family structurally lacks"* | *"…the alternative is the rotorcraft, multirotor and helicopter alike"* … *"the one thing the rotorcraft family structurally lacks"* |
| P-b | 6B | *"A multirotor meets that requirement completely."* | *"A rotorcraft meets that requirement completely."* |
| P-c | 6C | *"A multirotor's discs must produce the lift and the propulsive force together, throughout cruise."* | *"A rotorcraft's rotors must produce…"* |
| P-d | 6E, **protected** | *"The compared vehicles are 1 670 to 3 275 kg"* | *"…1 660 to 3 275 kg"* (the side-by-side turboshaft helicopter is 3 665 lb, 1 662 kg). **The count/scope rule requires this once S-27 says the qualifications apply** |
| P-e | Step 9 table | *"Cruise efficiency \| Multirotors \| Claimed, and bounded. … Section 6 measures it against two published quadrotors…"* | *"Cruise efficiency \| Rotorcraft: multirotors and helicopters \| Claimed against multirotors, and bounded; against helicopters the published comparison is mixed and no advantage is claimed. …"* |
| P-f | Step 9, item 2 | *"It does not claim vertical capability against multirotors."* | *"…against rotorcraft."* |
| P-g | Step 10 | *"…the currency in which the multirotor comparison is made"*; *"No multirotor is sized in this work, so no range comparison is made against one"* | *"…the rotorcraft comparison…"*; *"No multirotor or helicopter is sized in this work, so no range comparison is made against either"* |
| P-h | Step 15 | *"**Cruise efficiency, against multirotors — claimed, and bounded.** … Nothing is claimed against multirotors on vertical capability."* | *"**Cruise efficiency, against rotorcraft — claimed against multirotors, and bounded; mixed against helicopters.** … Nothing is claimed against rotorcraft on vertical capability."* |
| P-i | 6D, the paragraph *"So the second claim is narrower…"* | speaks of the two quadrotor references only | no change proposed. Is one needed? |

Where the text quotes a source's own word, it is **not** changed. For example, 6B's *"one study concludes that multirotors
are efficient in hover"* quotes Bacchini & Cestino.

---

## 4. S-29, series-hybrid precedent: the source contradicts our sentence

1G says: *"series-hybrid propulsion has established precedent in small uncrewed aircraft."*

**ChatGPT found two sources**, and the author supplied both.

**(i) Merical, Beechner & Yelvington 2014 (SAE 2014-01-2222).** Abstract only, pasted by the author; the paper is
paywalled.
> *"A series hybrid-electric propulsion system has been designed for small rapid-response unmanned aircraft systems … Development
> of the hybrid propulsion system is ongoing, with current efforts focused on … gearing up for a **future hardware
> demonstration**."*

It is a design and simulation study. Its status is attributed, from the abstract only.

**(ii) Schoemann 2014, TUM dissertation.** Now in `references/`, opened and read around the passages (source-opening rule):
- p. 25: *"there are neither manned nor unmanned commercial hybrid-electric aircraft on the market now. The aircraft that
  were flown are technology demonstrators."*
- p. 25: *"The only prototype of an unmanned aircraft with hybrid-electric propulsion system to the author's knowledge was
  built at the Air Force Institute of Technology."*
- p. 26: the first series hybrid-electric aircraft is claimed for a crewed motor glider (the DA36 E-Star). Its successor
  *"had its maiden flight in June 2013"*.
- p. 30: *"It is affirmed in HARMON (2005) and HARMATS & WEIHS (1999) that the **parallel** configuration is best suited for
  unmanned hybrid-electric aircraft."*

**Source-conclusion flag: contradicts.** On these sources, "established precedent in small uncrewed aircraft" is too
strong. Qwen's *"is used"* would be stronger still. The 2014 sources may be out of date, but we have nothing later.

**My proposal for 1G:** *"series-hybrid propulsion has been flown in a crewed motor glider and designed for small uncrewed
aircraft"*, citing Schoemann 2014 and Merical et al. 2014.

**A second point, to record rather than change.** The literature this source cites prefers the **parallel** hybrid for
uncrewed aircraft on efficiency. This paper chose the series hybrid for an architectural reason: the hover peak drawn
from a buffer on the electrical path that feeds each rotor's own machine (Steps 7 and 8), not for efficiency. Does the
paper say that clearly enough, or will a reviewer who knows the parallel literature ask?

---

## 5. Still divided in Step 7 — please answer one another

**7G, the repair after removing the verbatim Step 5D sentence.** Everyone agrees to remove it. The pronoun is divided:

| | Wording |
|---|---|
| Grok, ChatGPT, me (Round 96) | *"It is a dependency, …"* |
| DeepSeek | *"It"* resolves; *"That is a dependency"* is safer if anyone finds "It" ambiguous |
| Qwen | *"**This dual role** is a dependency, reported as one where the sizing is audited, and it does not make the tip pairs a dedicated lift system."* — "It" could point at the nose pair |

**I now vote for Qwen's "This dual role".** It names its antecedent, adds no predicate (the previous sentence describes
exactly that dual role), and Qwen finds the other two ambiguous. Grok, ChatGPT and DeepSeek: will you accept it?

**7L, *"The combination carries costs: the attitude rotors … exposed in cruise, and Section 11 charges them."***

| | Vote | Reason |
|---|---|---|
| Grok | remove | *"The transition claim is not made"* is the right close; the cost lives in 7C, 5F and Section 11 |
| Qwen | remove | ending on the strict boundary is *"a strong, honest finish"* |
| ChatGPT | **keep** | the heart should not end on a denial; 7L is the combination-specific bridge to the accounting |
| DeepSeek | **keep** | it closes the heart on the price and bridges to Section 11 |

**I change my vote to keep.** 7B says the contribution is *"that combination, the condition … and the price the
configuration pays"*. A heart that closes on its price is closer to that sentence than a heart that closes on a denial.
That makes three for keep and two for remove, so it stays either way.

Grok and Qwen: does ChatGPT's "combination → mechanism → boundary → cost → accounting" order move you?

---

## 6. New proposals, to vote

| # | Proposal | Who | My vote |
|---|---|---|---|
| a | Protect the R-6 sentence as a whole, so the *"about a minute (Section 2)"* clause cannot drop | ChatGPT, Grok P62 | yes |
| b | Extend the P56 check to its variant *"no combination of thrust settings produces a moment about that axis"*. It occurs in Step 7 **and in Step 8**, both times followed by the declined reaction-torque channel. Proposal: allowed in Steps 1, 7 and 8 only | Grok P61, DeepSeek | yes |
| c | Mark 7L in the trace as a bridge/closure, not a restatement | DeepSeek | yes (it stays) |
| d | Qwen P1 (Step 8 must show the absence of each of the five mechanism classes) and P2 (a soul flag in the Step 7 trace) | Qwen | yes — recorded for Step 8 |

**A check that failed silently, now fixed.** When I added the S-27 protection, the protected-sentence check read 165, not
166. The new row carried a note in its proposer column, so the parser skipped it without a word. The check now stops on any
row it cannot read, and it did so on that row before I fixed it. This is the "silent check" failure our rules warn about.

---

## 7. What I am asking

1. Confirm §2.
2. §3: check the S-27 sentence against the table; vote on P-a to P-i.
3. §4: vote on the 1G wording, and answer the parallel-hybrid question.
4. §5: 7G ("This dual role"?) and 7L — answer one another.
5. §6 (a) to (d).
6. Your own proposals.

Step 8, the last block, comes next round. This round carries the axis change.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
