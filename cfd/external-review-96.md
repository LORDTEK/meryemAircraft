# Round 92 — Step 9's item 4 is repaired. 14E and 14G are applied, with a new protection. Two more removals were caught before they could break a reference. A second selective quotation (S-19). The onboarding text is attached for you to check

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> The onboarding's §2–§3 are **quoted in full at the end of this text (Appendix)**, so that you can check them without the
> file.

---

## 1. Applied — please confirm

All four of you and I agreed to each change below.

- **Step 9, item 4 (the repair for R-1)**
  > ***4. It does not claim mechanical simplicity.** Part count, assembly mass, failure modes and maintenance burden were not
  > measured, and nothing here supports a statement about reliability. **The count of mechanism classes in Section 7 is not a
  > reliability argument**, and readers who convert one into the other are not quoting this paper.*
- **14E.** *"…Section 11's ledger records that conversion at the assumed store. **The escape from Bill 3 is real…**"*
  - Removed: *"at a measured specific power it costs thirteen to fifteen percent of take-off mass instead of 3.6"*.
- **14G.** The paragraph now ends after *"…because the one method used here is least reliable exactly there."*
  - Removed: *"Several — hover control, the descent, the buffer's energy, the electrical path — are analyses this study has
    not posed. One — the engine installation — is not in the work at all."*
- **Protected:** *"The escape from Bill 3 is real in the sense Section 3 defined it, and its price depends on a component
  whose required performance has not been demonstrated."* The protected list now has **160** entries.
- **9F precedent list: closed, kept.** Grok: *"I yield."*

The original paragraphs are frozen in Supplements S9 and S14. The nothing-lost check now covers Step 14. All checks pass.

---

## 2. Two removals we agreed, caught before applying (Grok P51)

**Grok P51 is now the procedure.** After any agreed deletion, the next sentence's demonstratives are read before the
deletion is applied.

**14D (R-2).** We agreed to remove the prose restatement of the table's third row. The paragraph as it stands now:

> ***At the bench rate the loop closes about three-quarters heavier**, with a buffer of about fourteen percent of take-off mass
> rather than 3.6. If Section 10's take-off masses are retained **instead**, the payload falls to about 7 kg rather than 13. …*

If the first sentence is deleted, *"instead"* has nothing to be instead of. This is **R-2**, caught before applying.
**Proposed (R):**

> *If Section 10's take-off masses are retained **instead of re-closing at the bench rate**, the payload falls to about 7 kg
> rather than 13.*

**My position: yes.**

**Item 2 of Step 9: not a defect.** ChatGPT, you asked for an R repair because you read the sentence to be removed as coming
*before* *"That comparison…"*. It comes **after** it:

> ***2. It does not claim vertical capability against multirotors.** That comparison runs the other way and would be absurd.
> ~~The multirotor family is the opponent on cruise efficiency only.~~*

*"That comparison"* points to the bold heading, which is the comparison of vertical capability against multirotors. The
sentence being removed is the last one. DeepSeek and Qwen read it this way. **ChatGPT, does this settle it?** If it does, the
removal is applied next round, which is the same way E1 was handled.

---

## 3. S-19: a second selective quotation, found by opening the source for 14C (Grok P52)

Grok asked that the 4 kW/kg figure stay *attributed* until its document was opened. **I opened it:**
`references/Barrett-2023_NIAC_solid-state-EAD-propulsion_MIT.pdf`, a NASA NIAC study.

- **PDF p. 16:** *"the specific power (4 kW/kg) is about twice that of existing batteries."* **Verified.**
- **PDF p. 34, the same study:** *"The default value of battery specific power in this study is 4 kW/kg (Table 5), about twice
  that of existing lithium-ion battery prototypes [39]. **However, the specific power of lithium-polymer batteries in the
  literature can be as high as 3 kW/kg [60].**"*

**Step 14 quotes the first sentence and leaves out the second.** This is the same pattern as S-18. The second sentence
matters because Step 14's gap is stated against the highest figure *"measured"* in the sources consulted, a bench rate of
about 1.5 kW/kg. Against 3 kW/kg, the take-off demand of 5.5 to 6.1 kW/kg is **1.8 to 2.0 times**, not 3.7 to 4.1.

**Proposed addition to 14C (R, added)**, placed after the design-study sentence:

> *The same study notes lithium-polymer figures in the literature as high as 3 kW per kilogram, which it cites rather than
> measures; against that figure the take-off demand is 1.8 to 2.0 times.*

**What this changes, and what it does not:**

- **It narrows the size of the gap. It does not close it.** Even 3 kW/kg is below the demand.
- **The protected sentences stand as they are.** *"…does not exist with any store the sources consulted here report as
  built"* and *"the factor quoted is peak demand against bench average"* are both still true.
- **The status of 3 kW/kg is *attributed*.** Barrett cites it as ref. [60], and we have not opened that reference. So the
  sentence says *"which it cites rather than measures"*.
- **My position: yes.** Leaving it out would be selective quotation, exactly as in S-18. I also ask: **should we open
  Barrett's ref. [60]?** If anyone can give a downloadable PDF for it, please do.

---

## 4. Your proposals, and what I did

| Proposal | Action |
|---|---|
| **Qwen P1: version-stamp the onboarding** | **Done.** It now opens with a version check, and `grep -c "this configuration's range is"` must print 0. **Qwen, the copy you quoted is the Round 61 file sent in Round 64.** The repository file (commit b8dc24d onward) says at §3: *"Against this configuration, the lift-plus-cruise layout is 55 to 84 percent ahead…"*. You were right to check it, and the stamp now makes the check mechanical |
| **DeepSeek: make every onboarding number traceable** | Adopted. Every number in §1–§3 names its step, and the Appendix below is there so that you can check them |
| **DeepSeek: evidence status in the journal supplement** | **My view: no.** The supplement goes to the journal. Evidence statuses are our internal record, kept in `paper/v8-evidence.md`. **Tell me if you disagree** |
| **Qwen P2: a *debt vs scope* flag in the Step 14 trace** | Adopted |
| **ChatGPT: "removable in content, but the deletion needs an R repair"** | This is now the standing rule (R-1, R-2) |

---

## 5. What I am asking

1. **Confirm §1.**
2. **Vote on 14D's R (R-2).** **ChatGPT:** item 2 (§2).
3. **S-19:** vote on the added sentence. Can you supply Barrett's ref. [60]?
4. **Check the onboarding Appendix** against the steps.
5. **New proposals.**

**Sources.** Barrett 2023 was opened this round: PDF pp. 16 and 34.

---

## Appendix — `cfd/reader-onboarding.md` §2–§3, as they stand now (please check against the steps)

## 2. What the paper claims: four axes, four opponents

| Axis | Opponent | Standing |
|---|---|---|
| **Cruise efficiency** | Multirotors | **Claimed, and bounded.** The size of the margin is a calculation. In one measure it is 5.56 to 7.39 here, against 4.9 for a published turboshaft quadrotor and 5.8 for an all-electric one (Step 6). |
| **Operation without a runway** | Fixed-wing aircraft | **Claimed as sized, not demonstrated.** It depends on an energy store whose required performance the sources consulted do not report as built (Step 14). |
| **The mechanism required to change regime** | Tilting architectures | **The contribution.** |
| **Range** | The other hybrids (lift-plus-cruise, tilting) | **Not claimed, in either direction.** The ordering belongs to the sizing contract (Step 13). |

**There is one contribution: the architecture.** It is *"arranged to change regime by rotating the airframe rather than
its propulsors"*. It carries none of five mechanism classes (Step 7):

- a pivot or tilting joint;
- a nacelle or rotor-group actuator;
- a variable-pitch hub;
- dedicated lift rotors;
- a rotor stowing, indexing or stopping mechanism.

**It is a count of mechanism classes.** It is not a claim that nothing moves, since the strip moves, and not a claim of
simplicity or reliability, which were not measured. **"Arranged to", not "changes": the transition is not shown.**

**The paper's own statement of what it offers** (Steps 9 and 15): *"a configuration sized to combine runway-independent
vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism that reorients a propulsor, and
an account of what the combination costs."*

**Sentences that are never written:**

- "the range of a fixed-wing aircraft", or any range comparison with fixed-wing aircraft;
- any comparison with multirotors on vertical capability;
- a range claim against lift-plus-cruise or tilting aircraft;
- "no moving parts", "no control surfaces", "simpler";
- "the aircraft changes regime";
- "there is no general architectural superiority claim";
- "first", "only", "not done before". These appear only as "not found", with the place searched named. Uncrewed
  tail-sitters, tail-sitters without control surfaces, coaxial tail-sitters and BWB tail-sitters are all in the
  literature (Step 1).

---

## 3. The framework, which is the instrument that makes the claim checkable

**The framework is not a second contribution.**

**The three charges ("bills")** (Step 2). The root of all three is a **duty-cycle mismatch**: hardware needed for about two
percent of a flight is carried for the rest.

| Charge | What it is |
|---|---|
| **Bill 1** | the mass of a dedicated lift subsystem |
| **Bill 2** | the cruise drag of hover hardware left exposed |
| **Bill 3** | continuous power installed to a hover peak |

**Charge and currency are not the same thing** (settled over Rounds 77–80). The currencies are kilograms, drag counts and
installed kilowatts. A remedy's own cost can fall in a currency without being a charge. For example, a tilt pivot's mass is
*"kilograms, not Bill 1"*. The table in Step 2 names bills by number and every other cost in words.

**Remedies move cost; they do not remove it.** The Step 2E heading reads *"remedies move cost, among the three charges or
outside them"*. The word *transfer* has two senses:

- **"A transfer between charges"** is narrow: one charge is reduced and another made worse.
- **"The accounting claims transfer"** is broad: cost is moved, possibly out of the three charges.

**The refutation test** (Step 2F). A counter-example reduces one charge, leaves the other two no worse, and has an own cost
that is either absent or demonstrably smaller than the reduction, in the same currency.

- *"No worse"* is judged against **the architecture the move modifies**.
- A cost outside the three does not refute the accounting, **but it is listed, not waved away**.
- **The tilting row** falls on one of two branches, depending on how the modified architecture supplies its hover peak:
  - either it is a transfer between charges;
  - or what keeps it from refuting the accounting is the part of its cost that falls outside the three.

**The escape condition** (Step 3) is **a definition, stated before any configuration**. It is derived by inverting the
table. It has four parts: **same hardware, both duties, one orientation, hover peak from a store**. It names six permitted
costs and four failure modes, the fourth being **partial instantiation**. **This configuration is a partial
instantiation**: the nose pair meets all four parts, and the tip pairs are carried through cruise producing moments, so they
re-open Bill 2.

**The rest of the framework:**

- **Independent check** (Step 4): a NASA sizing set of five VTOL families.
- **Ledger** (Step 11): the price of the closures attributed to the three charges, with no scalar total.
- **Scale** (Step 12): the rotor term of Bill 2 falls to 0.29–0.65 of its light value while Bill 3 is held nearly flat by
  the sizing rule, so **at least two charges are not locked together.**
- **Contracts** (Step 13). **Against this configuration, the lift-plus-cruise layout is 55 to 84 percent ahead under a fixed
  fuel fraction, 28 to 54 percent under a fixed fuel mass, and between 13 percent short and 7 percent ahead under a fixed
  take-off mass.** The sign changes inside the envelope, and the tilting competitor is only a bound.
  *(The earlier onboarding text of Round 61 stated these figures with the direction reversed. The figures above are
  quoted from Step 13.)*
- **What does not close** (Step 14): the energy store. The take-off demand is 3.7 to 4.1 times the highest measured figure.

---
