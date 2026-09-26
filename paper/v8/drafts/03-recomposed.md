# Step 3 as result sentences — first recomposed draft (Round 110, to vote)

**Nothing here has entered `03-the-escape-condition.md`.** Source: the step's English body, 1 654 words of prose, 13 protected
sentences. Tags as in Step 2. The deletion check (`v8_draft_check.py 3 --taslak paper/v8/drafts/03-draft2.md`) passes: no new
predicate, no deleted negative, all 13 protected sentences present. The one pointer added is in ⟦ ⟧.

## 1. The lists (Round 109), in short

| Finding | Grok | ChatGPT | DeepSeek | Qwen | Claude | Draft |
|---|---|---|---|---|---|---|
| Opening: a definition, by inversion, before any configuration (P) | body (core) | body | body | body (core) | body | D1, P2 |
| The four things departed from; *"ways to pay … a condition"* (P) | body | — | body | body | body | D3, P4 |
| The four departures, one sentence each | S3 | movable | → S3 | → S3 | → S3 — Supplement S3's table already carries them | out, with a pointer |
| The parenthesis on the second departure | — | movable | → S3 | → S3 | → S3; *"cruise thrust"* is defined again in D27 | out |
| The condition (P); four parts; where they come from | body | body | body | body | body | P5, D6, D7 |
| *"Two things in that sentence are choices"* | — | — | — | — | body — it says the store reading is a choice | D8–D10 |
| Zero of the three charges (P); unfalsifiable otherwise | body | body | body | body | body | P11, D12 |
| Six permitted costs, each with its protected clause | body | body (neg.) | summary body, detail S3 | one clause each, reasoning → S3 | each keeps its protected clause and its reason; restatements → S3 | D13–D35 |
| One exclusion; tip frames; *"does not reach them"* | — | one sentence body | body, narrowly | compress | body; *"landing gear because the aircraft stands on its tail"* stays, because it is why the exclusion does not reach them | D36–D40 |
| Four failure modes; *"not a technicality"*; partial instantiation (P) | body | body | body | body | body | D41–P43 |
| Triple denial (P); three questions | body | body | body | body | body | D44–D46 |
| Tilting: refused by another means; *"as written"* (P); separate question (P) | — | keep the two P, setup movable | body | body | body — D47 is where the paper's route is first named | D47–P50 |

**Check on quotations.**
- **ChatGPT, DeepSeek:** every quotation from Step 3 is in the body, with one exception. ChatGPT's bold *"core finding"* is not
  the source's words, though it is set as a quotation: *"an architecture avoids those three charges **only if** its propulsion
  arrangement uses the same propulsors across regimes without reorientation, and its continuously installed power is sized to
  cruise rather than hover"*. The source states a sufficient condition (*"does not incur the three charges **if**"*), and P50
  says it *"can be too narrow without being wrong"*. *"Only if"* makes it necessary, which is the reading P50 exists to refuse.
  ChatGPT's paraphrase also drops the store. ChatGPT itself adds that *"the source's own wording for the condition is the
  authority here"*. The draft keeps the source's wording.
- **Qwen:** the opening quotation *"what would an architecture have to do in order not to incur them at all? The answer is a
  definition, derived by inverting the table **rather than by describing any aircraft**…"* is the pre-recomposition opening,
  frozen in Supplement S3. The body reads *"This section asks what an architecture would have to do in order not to incur the
  three charges at all. The answer is a definition, derived by inverting the table, and it is stated here before any
  configuration is offered…"*.
- **Grok:** *"Calling them one would be loose (if still present)"* — it is not present; it is in S3's frozen snapshot. *"No
  worse three-sentence form, if it still lives in 2F/3"* — it lives in Step 2 only.
- **DeepSeek** proposes moving *"the detailed four departures table"*. Step 3 has no table; the departures are a paragraph,
  and the table is already in Supplement S3.

## 2. The draft

## The escape condition

[D1] This section asks what an architecture would have to do in order not to incur the three charges at all. [P2] The answer is a **definition**, derived by inverting the table, and it is stated here before any configuration is offered so that the standard is not taken from the thing it will be used to measure.

### Inverting the table

[D3] **A charge appears wherever the two regimes are served by hardware that departs from one of four things: the same hardware, serving both duties, held in one orientation, with the hover peak supplied other than by its continuously installed power.**⟦ What each departure costs is in Supplement S3.⟧ [P4] Read one at a time, these are ways to pay. Read as a conjunction, they are a condition.

### The condition

[P5]
> **An architecture does not incur the three charges if the propulsors that carry the weight,
> held in one orientation relative to the airframe, produce both the hover thrust and the cruise
> thrust, and if the difference between the hover peak and the cruise demand is supplied from
> a store rather than from permanently installed continuous power.**

[D6] Four parts: **same hardware, both duties, one orientation, hover peak from a store.** [D7] The first three come from the first three departures; the fourth comes from the fourth.

[D8] Two things in that sentence are choices rather than derivations. [D9] The inversion requires only *one orientation relative to the airframe*; **how** an architecture keeps that while changing flight regime — by rotating the whole body, or otherwise — is not in the inversion, and is treated as exposition rather than as part of the definition. [D10] And the fourth departure's exception lets the peak come from **any** source other than the continuously installed power; a store is the narrower reading used here, because it is what the configuration examined later uses and because a narrower condition is easier to fail.

### What the condition does not say, and this matters more than what it says

[P11] **It means zero of the three charges as Section 2 defines them.** **It does not mean an architecture that costs nothing, and it does not mean an architecture that carries nothing for the vertical phase.** [D12] A definition that placed every conceivable cost inside the thing to be escaped would be unfalsifiable, and an architecture built to satisfy it would win by construction rather than by performance.

[D13] The costs the condition permits are named here, before any candidate is examined. Six of them:

- [P14] **A store is permitted, and it has the same duty-cycle character as Bill 1.** [D15] It is not Bill 1 as Section 2 defines it — it is not lift-subsystem mass — **but it is mass carried for a duty that is briefly needed, which is the same complaint Bill 1 makes.** [D16] The condition converts a power-system charge into a cost in kilograms and claims only that the three charges as named are not incurred. [P17] **It does not claim the trade is favourable.** [D18] Whether the store is lighter than the continuous power it displaces is a sizing result and is computed, not asserted.
- [P19] **Releasing the engine is not releasing the electrical path.** [D20] Everything between the store and the rotors — machines, power electronics, wiring — still passes the full hover power and is still sized by it. [D21] **That is Bill 3 on the electrical path, and the condition does not remove it**; it is carried in the ledger rather than in this definition.
- [P22] **Rotating the airframe is permitted and is not priced here.** [D23] **An architecture that rotates its whole body faces the same physical problem** — a ninety-degree change of the thrust axis relative to the flight path, with the moments, the authority and the control through the turn that implies. [D24] It is not one of the three charges and the condition does not eliminate it; it is priced where the transition is analysed.
- [D25] **Hardware installed for the vertical phase is permitted if it serves both duties**, and the second departure is what carries the weight.
- [D26] **Hardware used in both regimes for something other than propulsive thrust is permitted, and its cruise drag is not eliminated.** [D27] *Cruise thrust in this paper means the thrust that balances cruise drag.* [D28] Attitude devices produce thrust in cruise, but they produce no cruise thrust in that sense; they are used throughout the flight, so their duty cycle matches their presence and they fall outside Bill 1. [D29] **They remain in the airstream, so the second charge reaches them.** [D30] **Attitude hardware does not stop the propulsor that carries the aircraft from meeting the condition, but it is carried through cruise without producing cruise thrust, which is the first failure mode below — and the charges are about everything the aircraft carries, so Bill 2 reaches it.** [D31] The condition permits such hardware outside the first charge and does not make it free.
- [P32] **Serving two regimes with one set of hardware has a price of its own.** [D33] Hardware that is not duplicated cannot be optimised twice: a propeller sized for hover thrust at zero forward speed is not the propeller a cruise design would choose, and if its geometry is fixed the compromise is paid in efficiency. [P34] **The condition permits that cost and does not measure it.** [D35] Section 11 does.

[D36] **One exclusion, stated narrowly.** [D37] Structure, surfaces and actuation present for reasons other than the vertical phase are not charged **as duty-cycle mismatch under this accounting**. [D38] That is a statement about which ledger they belong in, not a claim that they are free, and it does not apply to a part that would not exist but for the vertical phase. [D39] The tip frames are the case that tests it: they are landing gear because the aircraft stands on its tail. [D40] **Their mass is charged in the build-up and their drag in the ledger; the exclusion does not reach them.**

### The condition can fail, and how

[D41] An architecture fails the condition if **any** of the following holds:

1. It carries a propulsor through cruise that produces no cruise thrust.
2. It changes the orientation of a propulsor relative to the airframe in order to change regime.
3. Its continuously installed power is sized by the hover requirement rather than by cruise.
4. It satisfies the first three only in part — for instance in its primary propulsor while a secondary set fails them — in which case the instantiation is **partial**, and the part that fails re-opens the charge it fails.

[D42] The fourth is not a technicality, and it is the reason this list exists. [P43] **An architecture may meet the condition where it carries the aircraft and fail it elsewhere**, and a paper that reported only the first half would be reporting the condition rather than the aircraft.

### What follows from the condition, and what does not

[D44] The condition is a statement about what an architecture would have to be. [P45] **It is not a claim that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim that satisfying it is desirable.** [D46] Three questions follow from it, and they are answered separately: whether the accounting behind the condition survives contact with an independent sizing study is tested in the next section, against data this work did not produce; whether any configuration satisfies the condition is the subject of Sections 5 to 7; and what such a configuration pays instead is the subject of Section 11, the answer most likely to be wrong.

[D47] The third departure is refused by a means other than the one the field has adopted. [D48] A tilting architecture accepts that departure and buys its way out of the first departure with a mechanism. [P49] **An architecture that reorients a propulsor does not satisfy the condition as written**, because the condition requires one orientation relative to the airframe. [P50] **Whether such an architecture might avoid the three charges by some other route is a separate question this paper does not settle** — the condition is a definition, not a law, and it can be too narrow without being wrong.

## 3. Trace, pairs and audits

| Source paragraph | Fate |
|---|---|
| Opening (2) | D1, P2 |
| Inverting the table (5 + 2) | D3 + pointer; the four one-sentence departures → S3 (its table already carries them); P4 |
| The parenthesis (3) | → S3 |
| The condition, four parts (2) | P5, D6, D7 |
| Two choices (3) | D8, D9, D10 |
| Does not say (4) | P11, D12 (*"The condition has to be read exactly."* → S3) |
| Six costs, intro (2) | D13 |
| Store (6) | P14, D15, D16, P17, D18 (*"The fourth part moves the hover peak off the continuous power plant and onto a store; that store delivers its peak for two percent of the flight and is carried for the rest."* → S3) |
| Electrical path (4) | P19, D20, D21 (*"The fourth part frees the continuous power plant from the hover peak."* → S3) |
| Rotating the airframe (5) | P22, D23 (*"instead"* deleted), D24 (*"The condition refuses architectures that reorient a propulsor…"* and *"Saying otherwise would let a candidate win that line by wording."* → S3) |
| Both duties (1) | D25 |
| Attitude hardware (7) | D26–D31 (*"An architecture in that position is a partial instantiation, the fourth failure mode…"* → S3; failure mode 4 and P43 carry it) |
| Fixed pitch (4) | P32, D33, P34, D35 |
| One exclusion (5) | D36–D40 (*"— a wing, a control device, a fairing that earns its place on a part already carried"* and *"and they also carry the attitude propulsors and the directional fairing"* → S3) |
| Can fail (2 + list) | D41 (*"A definition worth stating is one an architecture can be shown not to meet, so the failure modes are explicit."* → S3), the list unchanged |
| Not a technicality (2) | D42, P43 |
| What follows (3) | D44, P45, D46 |
| Tilting (5) | D47, D48, P49, P50 (*"One consequence is worth stating now, because it shapes everything after it."* → S3) |

**Words:** 1 305 of prose, **79 %** of the source (1 654). The plan gives 650. Qwen's P3 names the reason: 13 protected sentences,
and most of the rest are the six costs' reasons.

**P71 pairs checked:**
- P4 needs D3 (the four things).
- P5 and D6–D7 need D3.
- P17 needs P14–D16 (the store and the conversion).
- D21 needs D20 (what the electrical path is).
- P34 needs D33 (why one set of hardware pays).
- P43 needs failure mode 4.
- D40 needs D39's reason, which is why *"landing gear because the aircraft stands on its tail"* stays.
- P49 and P50 need D47–D48.
- Section 11's *"as Section 3 said in advance it would"* needs D16; Section 8's attitude-hardware sentences need D26–D31.

**Rule (iii):** no candidate. No protected sentence moves.

**Negative-qualification audit** — every *"not"* the draft removes:
- The parenthesis: *"a propulsor that produces a little thrust in cruise is not thereby serving both duties"* and *"hover
  thrust and cruise thrust are not the same job"*. D27 (*"Cruise thrust in this paper means the thrust that balances cruise
  drag"*), D28 and failure mode 1 carry the distinction. The explanation of the wording *"serving both duties"* moves.
- *"A definition worth stating is one an architecture can be shown not to meet"* — D12 carries the falsifiability point.
- *"Saying otherwise would let a candidate win that line by wording"* — P22's *"is not priced here"* stays.
- Every other *"not"* in the source is in the draft.
