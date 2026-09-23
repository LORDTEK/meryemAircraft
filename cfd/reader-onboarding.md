# Reader onboarding — for a new conversation

> **Why you are reading this.** You have been one of four independent readers of a paper in
> development — the four are ChatGPT, Grok, DeepSeek and Qwen — over some sixty rounds. The texts
> have grown so long that conversations were filling up, so **every reader is starting a fresh
> conversation now.** This file is meant to put you back where you were: what the paper is, what
> it claims and does not claim, what has already been settled, which errors have recurred, and how
> to answer. **It contains no new claim of its own. Every number in it is quoted from the paper
> text you will receive with it, and the step it comes from is named.**
>
> **You will receive two files:** this one, and the round text (`external-review-64`), which
> carries this round's corrections, this round's questions, and **all fifteen steps of the paper
> in full.** Read this file first; then answer the round text.

---

## 1. What the paper is

**A design study of an uncrewed aircraft**, written for the *Journal of Aircraft* (AIAA). The aircraft
is a **tail-sitting blended-wing-body (BWB) series-hybrid vertical-take-off-and-landing** configuration.
It stands on its tail on the ground, takes off and lands vertically, and then rotates the whole airframe
through about ninety degrees to fly on its wing. The two applications it is aimed at are **wildfire
observation and response** and **cargo delivery to places without a runway**.

**What it is made of** (Step 8):

- **A blended wing body** — one lifting surface, no separate fuselage or tail.
- **One coaxial contra-rotating nose pair** of fixed-pitch propellers, 1.20 m in diameter on the 50 kg
  reference design. It produces **all propulsive thrust in both regimes**: it lifts the aircraft in
  hover and pulls it in cruise, in one orientation relative to the body.
- **Four smaller counter-rotating pairs, 0.20 m in diameter, at the ends of rigid frames projecting from
  the wing tips.** They produce pitch
  and yaw by differential thrust, and they supply the take-off margin. In cruise they are carried,
  producing moments rather than cruise thrust.
- **A strip on the lower surface**, deployable in two halves — one side alone for roll, both together as
  a speed brake. Roll does not come from the propellers.
- **A series-hybrid power path:** fuel → engine → generator → electric machines at the rotors. The engine
  is sized by cruise; a **battery buffer** supplies the hover peak.

**Three aircraft appear in the paper, and keeping them apart matters** (Step 8 defines them):

| Name in the text | What it is | Where |
|---|---|---|
| **The 50 kg reference design** | The design the inventory describes: span 3.453 m, wing area 1.979 m², aspect ratio 6.03, nose pair 1.20 m. Transition results (2 s rotation, 5.4 m altitude loss) belong to it. | Step 8; Steps 10, 12 |
| **The four closures, A–D** | The same configuration re-closed by an analytical sizing loop at four combinations of drag and propeller efficiency. **52.3 to 57.5 kg.** | Step 10 |
| **The 1 000 kg reference design** | A heavy version sized by the same method, used only to test how the charges behave with scale. No closure was run at 1 000 kg. | Step 12 |

The four closures (Step 10), with a 13 kg payload at 30 m s⁻¹:

| Closure | C_D0 | η_p | L/D | Take-off mass | Hover power (rotor shaft) | Engine (shaft) | Range |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 0.0381 | 0.632 | 8.79 | 57.5 kg | 12.53 kW | 5.17 kW | 927 km |
| B | 0.0381 | 0.683 | 8.79 | 55.8 kg | 12.17 kW | 4.65 kW | 1 002 km |
| C | 0.0285 | 0.632 | 10.82 | 53.5 kg | 11.66 kW | 3.91 kW | 1 141 km |
| D | 0.0285 | 0.683 | 10.82 | 52.3 kg | 11.40 kW | 3.54 kW | 1 233 km |

C_D0 0.0285 and 0.0381 are the two ends of the **drag bracket**; η_p 0.632 and 0.683 are two **blade
families** of computed propeller efficiency.

---

## 2. What the paper claims — four axes, four opponents

This is the spine of the whole work, and every sentence of the paper is meant to be consistent with it
(Step 9 states it; Step 15 closes on it).

| Axis | Opponent | Standing |
|---|---|---|
| **Cruise efficiency** | Multirotors | **Claimed, and bounded.** Cruise lift is carried on a wing rather than on rotors. The size of the advantage is a calculation: in one common measure (effective lift-to-drag ratio) it is positive throughout against a published turboshaft quadrotor (4.9), and from slightly behind to comfortably ahead against an all-electric one (5.8), against this configuration's 5.56 to 7.39 (Step 6). |
| **Operation without a runway** | Fixed-wing aircraft | **Claimed as sized, not demonstrated.** The vertical phase was sized with an energy store whose required performance the sources consulted do not report as built (Steps 14, 15). |
| **The mechanism required to change regime** | Tilting architectures | **The contribution.** |
| **Range** | The other hybrids (lift-plus-cruise, tilting) | **Not claimed, in either direction.** The ordering belongs to the sizing contract (Step 13). |

**The single contribution is the architecture.** In the paper's words (Step 1): *"a configuration arranged
to change regime by rotating the airframe rather than its propulsors, and so carrying no mechanism that
reorients a propulsor."* The configuration carries none of five mechanism classes (Step 7): pivot or
tilting joint; nacelle or rotor-group actuator; variable-pitch hub; dedicated lift rotors; rotor stowing,
indexing or stopping mechanism. Pitch and yaw come from differential thrust; **roll comes from the strip.**
The coaxial pairs could produce roll from reaction torque (running the two rotors of a pair at different
speeds); **the configuration declines that channel as a design choice, and what declining it costs is not
computed.**

**The narrow strength of that claim is deliberate, and each limit below was reached after an error:**

- It is **a count of mechanism classes** — not a claim that nothing moves (the strip moves), not a claim of
  mechanical simplicity, reliability, part count or maintenance, none of which was measured.
- It is **"arranged to change regime"**, not "changes regime": **the transition has not been shown.**
  Whether this aircraft completes the rotation is a separate, open question.
- It does not depend on the drag bracket, the propeller efficiency, the sizing contract, the range result,
  the energy store, or the transition aerodynamics.

**The paper's own one-line statement of what it offers** (Steps 9 and 15): *"a configuration sized to
combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with
no mechanism that reorients a propulsor, and an account of what the combination costs."*

### Sentences that are never written, and why

| Never | Why |
|---|---|
| "the range of a fixed-wing aircraft", or any range comparison with fixed-wing aircraft | Fixed-wing aircraft are the better machines on range. The range claim is against multirotors only. |
| Any comparison with multirotors on vertical capability | Multirotors are the better machines there. The vertical-axis opponent is fixed-wing aircraft. |
| A range claim against lift-plus-cruise or tilting aircraft | Step 13 shows the ordering belongs to the contract. |
| "no moving parts", "no control surfaces", "simpler" | The strip moves; simplicity was not measured. |
| "the aircraft changes regime" / "the regime change is made" | The transition is not shown. |
| "there is no general architectural superiority claim" | It denies the paper's own contribution. |
| "first", "only", "never revisited", "not done before" | Only as "not found", naming where the search was made. Tail-sitters are seventy years old; uncrewed ones, tail-sitters without control surfaces, coaxial tail-sitters and BWB tail-sitters are all in the literature (Step 1). |

---

## 3. The framework — the tool that makes the claim checkable

**The framework is not a second contribution.** It is how the architecture is priced so that the claim can
be checked (Steps 2–4, 11–13).

- **Three charges ("bills")** that any hybrid vertical-take-off aircraft pays for runway independence
  (Step 2): **Bill 1**, hover hardware carried through cruise (mass); **Bill 2**, its drag when exposed in
  cruise; **Bill 3**, continuous power sized by the hover peak rather than by cruise. The three are
  **coupled**, and every known partial remedy moves cost between them.
- **The escape condition** (Step 3): what an architecture would have to do to incur none of the three as
  defined — the same hardware, serving both duties, held in one orientation, and a continuous power plant
  not sized by the hover peak. **It is a definition, stated before any configuration is offered.** It lists
  the costs it permits, and four failure modes; the fourth is **partial instantiation** — meeting the
  condition where the aircraft is carried and failing it elsewhere.
- **This configuration is a partial instantiation.** The nose pair meets all four parts. The tip pairs do
  not: they hold one orientation, but they are carried through cruise producing moments rather than cruise
  thrust, and they are exposed — so Bill 2 is re-opened (Steps 3, 7, 8).
- **An independent check** (Step 4): the charges are checked against a published NASA study that sizes five
  VTOL architecture families, among them quadrotors, lift-plus-cruise and tilt-wing designs.
- **The ledger** (Step 11) attributes the price of the closures to the three charges without adding any;
  there is no single scalar total, because three currencies (kilograms, drag counts, installed kilowatts)
  have no defensible weighting.
- **Scale** (Step 12): between the 50 kg and 1 000 kg reference designs, the rotor term of Bill 2 falls to
  0.29–0.65 of its light value while Bill 3 is held nearly flat by the sizing rule — so **at least two of the
  charges are not locked together within this model.** Bill 1 is not tested.
- **Contracts** (Step 13): because the charges are not locked together, a ranking is a weighting, and a
  **sizing contract** is one such weighting. Three are applied — fixed fuel fraction, fixed fuel mass,
  fixed take-off mass. Against lift-plus-cruise with a 10 percent lift group, this configuration's range is
  +55 to +84 %, +28 to +54 % and −13 to +7 % under the three; the shift from the first to the third is 67 to
  77 points, and 14 to 134 points across lift groups of 5 to 15 percent. **The tilting competitor can be
  modelled only as a bound that pays no cruise penalty**, and a comparison against a bound is not a ranking.
- **What does not close** (Step 14): **the sizing loop closes; the aircraft is not shown to.** The first,
  named obstacle is the energy store: the closures ask the buffer for 4.7 to 5.2 kW per kilogram of buffer to
  hover and 5.5 to 6.1 to take off. **The take-off demand is 3.7 to 4.1 times the highest of the measured
  figures** — a bench rate of about 1.5 kW per kilogram, held for about four minutes. At that measured rate the loop closes only for a heavier
  aircraft (94.6 to 101.2 kg); at the unit pack's continuous rating it does not close at all.

---

## 4. The paper, step by step

The paper is being built as **fifteen step files**; **Step N is Section N**, and cross-references
(*"Section 10"*) point to the step of that number.

| Step | Title | What it does |
|---:|---|---|
| 1 | The gap | Two families, two limits; what the contemporary answers do; what is already occupied; **names the contribution** |
| 2 | The tax | The three charges, coupled; how known remedies move cost between them |
| 3 | The escape condition | The definition, its permitted costs, its failure modes |
| 4 | An independent quantitative check | The charges against a published sizing set |
| 5 | The first half: operation without a runway | Against fixed-wing aircraft; what is sized and what is not demonstrated |
| 6 | The second half: cruise carried on a wing | Against multirotors; the margin in one currency, and five qualifications against it |
| 7 | **The combination** | One aircraft supplies both halves by rotating the airframe; the mechanism-class count |
| 8 | What it is made of, and what still moves | The inventory; which parts fail the condition; the strip |
| 9 | What is not claimed | The four axes; what each claim does not depend on; eight things not claimed |
| 10 | Analytical closure of the sizing loop | The four closures; the transition results of the reference design |
| 11 | The ledger | The price attributed to the three charges |
| 12 | Scale does not lock two of the charges together | 50 kg against 1 000 kg |
| 13 | Rankings belong to contracts | Three contracts, lift-plus-cruise, and the tilt bound |
| 14 | What does not close | The energy store; the list of unknowns |
| 15 | Four axes, and where the paper stops | Restates the four axes; no new number |

The author's own outline of the argument, which the steps follow: *introduction · the current state · the
solution to one problem · the solution to the other · **combining the solutions** (a move of its own, not a
by-product) · the soundness of the resulting product · the calculations · conclusion.*

---

## 5. Where the work stands

- **Target journal: *Journal of Aircraft*** (AIAA), full article. The paper was first sent to *Drones*,
  found out of scope there (the journal requires experimental validation from at least a laboratory-scale
  platform for general theoretical aircraft-design papers), transferred to *Aerospace* and returned the same
  day. **It never reached a reviewer.** *Journal of Aircraft* lists UAV and V/STOL in its scope and has no such
  requirement.
- **The fifteen steps are written** — about **30 000 words**, with sixteen tables.
- **The journal's budget:** a full article is 10 000 to 12 000 words, with each figure or table counted as
  200 to 700 words. The working target is **about 7 500 words of text with 6 figures and 8 tables — roughly a
  quarter of the present text.** Supplemental files are allowed, but the journal states that the article
  *"must be self-contained and stand on its own. Acceptance for publication will be based solely on the
  content of the article."*
- **Shortening is about to begin, gradually.** Until now the author has refused to shorten (*"There will be
  no shortening until I am confident"*). **This round is the preparation round**; no cut is made in it.

---

## 6. Errors that have recurred — look for these first

Readers have caught most of these; the author and I have made all of them. They are listed so that you
know where the text is most likely to be wrong.

1. **A correction that creates a new contradiction.** Rewriting one sentence to fix a claim, and the new
   sentence contradicting another section. This has happened more than any other error, including in the
   last two rounds (Step 12's rule and its own exception; Step 3 against Step 8).
2. **A correction that does not travel.** A phrase or number is retired in one step and survives in
   another. A retired-phrase list now scans every step automatically.
3. **A number of one aircraft quoted under another's name.** The latest: the lower ends of the closures'
   geometry were the 50 kg reference design's figures. Also: the Bill 3 ratio of the reference design (4.19)
   beside that of the closures (2.4–3.2) under one label.
4. **Mixing power stations.** Rotor-shaft, engine-shaft and electrical-bus powers are not interchangeable;
   subtracting one from another without the conversion efficiencies was made twice and corrected.
5. **A hand-copied number from a script.** Fixing a script does not fix the prose that quoted its old output.
6. **An old version quoted as the current one.** `paper-v6` and `paper-v7` are frozen historical records and
   differ from v8 in many places. **Quote only the v8 text supplied in the round file.**
7. **Over-claiming while summarising.** Every summary — including this file — is the highest-error place in
   the project. If a sentence here disagrees with the step it names, the step wins, and please say so.

---

## 7. Decisions already made — please do not reopen these

These are the author's decisions. You may say a decision has a consequence the author may not have seen;
please do not argue the decision itself.

- **One contribution: the architecture.** The framework is the instrument, not a second contribution. The
  contract-dependence of rankings is reported as a finding, not as a second thesis.
- **No range claim against the other hybrids**, in either direction.
- **"Arranged to change regime"** is the strength of the contribution sentence.
- **Roll from the strip; the reaction-torque channel is declined**, its cost stated as not computed.
- **The frozen v7 and its public archive are not being touched.** v8 is being built.
- **The journal body carries no "in the previous version this was …" narrative.** The history lives in the
  repository.
- **AI use is declared without brand, model or company names**, and no AI appears as an author.
- **Open by the author's choice, not to be settled by readers:** the name *"zero-bill condition"* for the
  escape condition.

---

## 8. How to answer

- **Reply in English.**
- **Blunt is wanted; encouragement is not.** Say what is wrong, where, and why.
- **Quote the sentence and name the step** for every point you make about the text. If two steps
  contradict each other, quote both.
- **Sources.** No source is needed for judgement, structure, style or logic. **A downloadable PDF link is
  needed only for** (a) priority and novelty claims ("this has been done before"), (b) numbers taken from a
  table, and (c) verbatim quotations. For any number you give, **say which document you opened in this
  conversation**; if you could not open it, give no number. A hedged number is worse than none, because it
  enters the record as data.
- **Do not guess the sign of a calculation.** If the direction of an effect is not computed, say so.
- **Do not propose new claims.** The paper's work at this stage is making the existing claims exact.
- **Every answer is audited** against the text before anything is applied, and the next round says who
  found what, what was taken, and what was declined and why. Your earlier findings are in the record of
  every round; several of the corrections in the text you are about to read are yours.

---

## 9. Verifying the text you have

The round file names the repository (`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`), the
commit, and the SHA-256 of every step file. You do not need the repository to answer; the hashes are there
so that a stale copy can be recognised.
