# Round 114 — the framework is done; S-43's wording, to converge; errors named; the architecture begins with Step 9 (its full text is Appendix A)

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`COMMIT`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**

---

## 1. Applied — please confirm the results

All of the following were voted by all four of you and me.

**Step 3, C-short.** *"Inverting the table"* now reads:

> **A charge appears wherever the two regimes are served by hardware that departs from one of four things: the same hardware,
> serving both duties, held in one orientation, with the hover peak supplied other than by its continuously installed power.**
> **Different hardware** costs Bills 1 and 2. **The same hardware serving only one duty** costs them again. **The same hardware
> serving both duties in a different orientation** is the tilting family. **The same hardware, both duties, one orientation, but a
> different sizing point** incurs Bill 3. What each departure costs is in Supplement S3. Read one at a time, these are ways to pay.
> Read as a conjunction, they are a condition.

**Step 4, M1 and M2.** Both moved to Supplement S4. O-a stays in the body. Step 4's last paragraph now reads:

> It establishes that one prediction of the accounting holds on data produced elsewhere, for purposes unrelated to this argument.
> That is the whole of it. **It does not establish that the accounting is complete**, that the three charges are the only costs an
> architecture pays, or that avoiding them makes an aircraft better. **It does not establish anything about the configuration this
> paper proposes**, which has not yet been described, and which is not in the study used here. A reader who wants to know whether
> the accounting flatters that configuration will have to wait for Section 11, where it is applied to it and where the answer is
> not uniformly favourable. **An instrument whose first use is to measure the thing its authors are advocating should be shown
> working on something else first**, and that is why this section comes before the aircraft. **The instrument is now fixed, and it
> is not modified again.** **Everything that follows is measured with it rather than added to it.**

Step 4 is 1 268 words (from 1 351). That is recorded as its floor under the current rules; the budget is the author's.

**The NASA study's single home is Section 4.**
- Section 1: *"A NASA study that sizes five VTOL architecture families to one mission describes the two relevant routes in its own
  terms."* → **"The NASA sizing study used in Section 4 describes the two relevant routes in its own terms."** The two route
  paragraphs are unchanged.
- Section 2: *"A NASA study sizing five VTOL architecture families against a common mission with common tools found…"* → **"The NASA
  sizing study of Section 4 found…"**. The finding and the quotation are unchanged.
- The two old openings are retired, so the check fails if either comes back (Qwen R113-P2, applied this way).
- Both forward pointers resolve to Section 4 in the assembly check.

**Also adopted:**
- the isolation-pair rule (ChatGPT);
- P92 (Grok) — 1.2 % and 9.4 % carry the identity *"tilt-wing against lift-plus-cruise, same study"* in the number-match check;
- the two instrument sentences as one P71 unit (DeepSeek);
- *"None is known to the authors."* and the selection-basis sentence (*"It is used for three reasons, stated so that the choice is not
  merely the one that agreed…"*) are now protected (Qwen);
- *"credit reduced to nothing"* stays.

**With Step 4, the framework is done:**

| Step | 2 | 3 | 4 | Together | Plan |
|---|---:|---:|---:|---:|---:|
| Words now | 1 786 | 1 351 | 1 268 | 4 405 | 1 750 |

---

## 2. S-43 — you all chose (b); the wording differs

The paragraph as it stands:

> **And the source states the second half of the prediction in its own words.** Discussing why the all-electric lift-plus-cruise
> design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery
> weight compared with the quadrotor, *"but not enough to counter the increase in structure and propulsion weight."* That is the
> efficiency credit conceded and found insufficient, by the authors of the data rather than by the authors of the prediction.

**The four wordings you proposed:**

| | Where | Text |
|---|---|---|
| Grok | first sentence | *"…in its own words, **on a comparison** the check does not use as its test."* |
| ChatGPT | first sentence | *"…in its own words, **though on a comparison** the check does not use as its test."* |
| DeepSeek | end of the last sentence | *"…by the authors of the data rather than by the authors of the prediction, **on the comparison** the check does not use as its test."* |
| Qwen, and I last round | first sentence | *"…in its own words, **on the comparison** the check does not use as its test."* |

**My view now: Grok's.**
- **Place.** The scope should come before the quotation, so the reader meets the limit before the evidence. This is DeepSeek's
  point to answer.
- **"A", not "the"** (ChatGPT's reason). The check sets aside more than one comparison: the quadrotor contrast as well as this
  one. *"The"* makes the reader look for a single one.
- **No "though".** *"On a comparison the check does not use"* already carries the contrast.

**Proposed:**

> **And the source states the second half of the prediction in its own words, on a comparison the check does not use as its
> test.**

**DeepSeek's proposal:** protect this sentence once it is revised. My view: yes, together with the quotation it qualifies.

---

## 3. Errors this round

**Mine.** I found none this round. The list below is what I found in yours; please look for mine too.

**ChatGPT — two things.**
- **O-a.** You vote to reject the move, but then quote the tilt-wing sentence **without** the clause as *"the current sentence"*. You
  also write *"leave its material omitted from body/S4"* and *"the current shorter sentence is actually safer"*.
  - The clause is in the body now. O-a proposed moving it out, and all five of us said no, so it stays.
  - If you in fact prefer it out, please say so; otherwise your vote stands as *"stays"*.
- **"The author".** This is the third round in which you attribute my positions to the author: *"the author's rejection"*, *"the
  author correctly identifies"*. The author has taken no position on these points. They are mine, as one of five readers.
  Please attribute them to *"Claude"* or *"K"*.

**DeepSeek.** You name S-19, S-20 and S-22 as *"the pattern"* for the witness-scope check. Those three were **selective quotation**:
a source's own qualification left out.
- S-19: Barrett's 3 kW per kilogram, a cited figure.
- S-20: Barrett's *"may be possible"*.
- S-22: DelftaCopter's variable pitch.

S-43 is a different class: the right sentence, from the wrong comparison. Both classes matter; they need different checks.

**Grok, Qwen:** none found.

---

## 4. Proposals, to vote

| # | Proposal | My view |
|---|---|---|
| Grok P93 + DeepSeek | **Witness-scope check for quotations from a dataset:** a quotation whose compared objects are not the test's is flagged unless the sentence says so; the comparison population is named and matched to the body's use | **yes**, as an audit-list item (a person reads it; no script can) |
| ChatGPT | Record in the evidence file: **a dataset's home is not every claim's witness.** The NASA study's identity lives in Section 4; the 1.2 % and 9.4 % come from the test pair; the quoted sentence comes from the all-electric/quadrotor comparison; Section 1 uses its route descriptions; Section 2 uses one finding. | **yes** |
| Grok P94 | Section 1's two route paragraphs must not grow a third design, a mission number or the three reasons. | **yes** — recorded in Section 1's audit table already; adopt it as a rule |
| Qwen R113-P1 | In Step 4's trace, flag the study's identity, comparison population and provenance sentences, as the selection basis is now protected | **yes, as flags** — the isolation-pair rule already halts on moving them |

---

## 5. The architecture begins: Step 9, *What is not claimed*

The plan's order is 9 → 1 → 5–6 → 7–8 → 15. **The full current text of Step 9 is Appendix A.**
- **Size:** 1 166 words of prose, plus its axis table (T1, a planned body table).
- **Protected:** 9 sentences.
- **Plan:** 400 words.

**What changes now.** The architecture is where the paper's point is made (the author's instructions: the architecture is carried
by placement, order and voice, never by a stronger sentence). The same rules apply, with two more questions:
- **Placement:** does a sentence carry the architecture where it stands?
- **Duplication with Step 15:** Step 15 (*"Four axes"*, 349 words) returns to the same four axes at the end. Is Step 9's table the
  axes' one home, with Step 15 consuming it?

**Please give, for Step 9:**
- the core finding in the section's words;
- what stays in the body and what goes to S9;
- the P71 pairs;
- rule-(iii) candidates;
- negative qualifications (in this section, almost everything is one; say which carry a limit that later text depends on);
- the Step 9 / Step 15 question.

**My own list, for you to criticise:**
- **Core:** the table, and *"No range claim is made against the tilting or lift-plus-cruise families in either direction"*. The
  narrower statement at the end (*"a configuration sized to combine … and an account of what the combination costs"*) is the
  positive form.
- **Stays:**
  - the scope/debt distinction (protected);
  - the table;
  - the fourth-row paragraph;
  - the dependencies paragraph and its distinction (the mechanism claim settled by inventory; the regime change not settled);
  - the named, unpriced cost;
  - the eight headings;
  - the narrower statement;
  - the contract consequence.
- **Could move or shorten:**
  - The opening's reason for placement (*"It is placed before the configuration's own numbers because…"*). It is working, not a
    claim.
  - The second sentences under items 2 and 4:
    - *"That comparison runs the other way and would be absurd."* — the word *"absurd"* is tone, not content;
    - *"readers who convert one into the other are not quoting this paper"*.
- **Must stay: item 6's second sentence.** Step 4's M1 moved *because* Section 9's item 6 carries it (*"A configuration may avoid all
  three and still be unbuildable…"*). This is a P71 pair across sections.

---

## 6. To vote

| # | Item | My vote |
|---|---|---|
| a | Confirm §1 (C-short, Step 4, the NASA pointers) | confirm |
| b | S-43: Grok's wording (§2), or yours; and protect it | Grok's; protect |
| c | §4 proposals | yes |
| d | Step 9 lists and the Step 9 / Step 15 question (§5) | as above |

---

## 7. Your own proposals

As always: anything you see, with your reason.

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## Appendix A — Step 9 as it stands now (body only)

## What is not claimed

This section states the boundary of the paper's claims. It is placed before the configuration's
own numbers because a boundary drawn after the results would be a retreat, and one drawn before
them is a commitment.

**It is not a list of the study's open questions.** Those are in Section 14, and the difference
matters: the boundary below is about claims the paper **declines to make**, most of which it
could not make on any evidence; Section 14 is about questions the paper **does not answer**, and
which better evidence would answer. One is a scope; the other is a debt.

### The claims are made on four axes, against four different opponents

The boundary is easiest to state as a consequence of the claim structure rather than as a list
of denials, so the structure comes first. Comparison is only meaningful against a named
alternative, and this paper's alternatives differ from axis to axis.

| Axis | Opponent | Status |
|---|---|---|
| Cruise efficiency | Rotorcraft: multirotors and helicopters | **Claimed against multirotors, and bounded; against helicopters the published comparison is mixed and no advantage is claimed.** Cruise lift is carried on a surface rather than on rotors, which no sizing contract changes. The *size* of the resulting advantage is a calculation, not a consequence of that fact (Section 6). |
| Operation without a runway | Fixed-wing aircraft | **Claimed as sized, not demonstrated** (Sections 5, 14). |
| The mechanism required to change regime | Tilting architectures | **Claimed.** This is the paper's contribution — a count of mechanism classes (Section 7), not a claim of mechanical simplicity or reliability. |
| Cruise efficiency and range | Other hybrids — lift-plus-cruise, tilt | **Not claimed, in either direction.** |

**The fourth row is the important one**, and the reason it is a refusal rather than a result is
the paper's own finding in Section 13. Against lift-plus-cruise the ordering depends on the sizing
contract: across the three contracts it moves substantially, and under one of them its sign changes
inside the envelope and turns on quantities of the competitor that are assumed rather than measured. A paper that quoted one of those orderings as a result would be reporting its own choice of
contract. Against the tilting family the competitor can be modelled here only as a bound that pays no
cruise penalty, and an ordering against a bound is not a result. **No
range claim is made against the tilting or lift-plus-cruise families in either direction**, and
a reader who finds one implied anywhere in this paper should treat it as an error rather than
as a claim.

### What each claim does not depend on

A reader who rejects one of these claims should be able to see immediately which of the others
survive, and the dependencies are short enough to state.

**Operation without a runway** does not depend on the drag bracket, the propeller efficiency or the
transition aerodynamics — **but it does depend on the energy store**: the vertical phase is sized with one,
and Section 14 examines whether it exists. **Cruise lift carried on a surface** does not depend on the sizing
contract or the transition aerodynamics. The **size** of the cruise-efficiency margin depends on both the
drag bracket and the blade family, and Section 6 reports it as a range rather than a number. **Elimination
of the propulsor-reorientation mechanism class** does not depend on the drag bracket, the propeller
efficiency, the sizing contract, the range result or the energy store — **nor on the transition aerodynamics**.

**The last of these carries a distinction that matters more than the others.** The mechanism claim is
a statement about what hardware is present, and it is settled by the inventory of Sections 7 and 8. **The
separate claim that this aircraft can actually perform the regime change is not settled** (Section 7).

### One cost of the contribution that is named and not priced

The mechanism claim has a price this work does not compute. **This configuration declines the reaction-torque
channel that comparable aircraft use for roll (Section 8). What that refusal costs — in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia —
is not computed anywhere in this paper.** The claim is that the mechanism class is eliminated.
**Whether eliminating it is favourable on balance is a question this work does not settle**, and
quantifying it would require a control-allocation study rather than a single torque figure.

### Eight things this paper does not claim

**1. It does not claim range against fixed-wing aircraft.** A runway-launched aircraft that never
claimed vertical capability pays none of the charges of Section 2, and nothing here competes
with it on distance.

**2. It does not claim vertical capability against rotorcraft.** That comparison runs the other
way and would be absurd.

**3. It does not claim that the aircraft has no moving parts.** What is eliminated is a *class
of mechanism* — the one that reorients a propulsor. The aircraft has a moving aerodynamic
surface, it is named where the elimination is claimed rather than later, and it also pitches the
nose down when deployed.

**4. It does not claim mechanical simplicity.** Part count, assembly mass, failure modes and
maintenance burden were not measured, and nothing here supports a statement about reliability.
The count of mechanism classes in Section 7 is not a reliability argument, and
readers who convert one into the other are not quoting this paper.

**5. It does not claim that the escape condition is fully instantiated.** The condition is met
in the propulsor that carries the aircraft and is not met in the attitude system, which is
carried through cruise producing moments rather than cruise thrust. Section 3 names that case as
partial instantiation, and the charge it re-opens is reported rather than absorbed.

**6. It does not claim that satisfying the condition makes an aircraft better.** The condition
concerns three specific charges. A configuration may avoid all three and still be unbuildable,
uncontrollable, or unsuited to its mission, and the accounting says nothing against that
possibility.

**7. It does not claim that the trades inside the escape are favourable.** Moving the hover
peak onto a store converts a power-system charge into a cost in kilograms; serving two regimes with one
set of fixed-geometry propellers costs efficiency in at least one of them. Both are computed,
neither is asserted to be worth paying, and the ledger reports them whichever way they fall.

**8. It does not claim that the aircraft flies.** The design *sizes* vertical operation and the
transition; it does not demonstrate either. No aircraft has been built, no wind tunnel has been
run on this geometry, and the transition analysis is a calculation whose assumptions are stated
where it appears. **"By construction" throughout this paper means "by the sizing", never "by
demonstration."**

### What the claims that remain amount to

Removing those eight leaves something narrower than a first reading of the abstract might
suggest, and the narrower statement is the one the paper defends: **a configuration sized to
combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so
with no mechanism that reorients a propulsor, and an account of what the combination costs.**

Each half of that has a named opponent and neither half is a record. **Nor is the configuration
claimed to be without precedent**: Section 1 sets out what is already established, including
uncrewed tail-sitters, tail-sitters without control surfaces, coaxial contra-rotating
tail-sitter propulsion, and blended-wing-body tail-sitters. **The contribution is the
architecture, and the paper presents it as the combination, the consequences of the choices inside
it, and the accounting** — which is what Sections 7 and 8 describe and what Section 11 prices.

### One consequence for how the numbers that follow should be read

Because the comparative result depends on the sizing contract, **no comparison in this paper
should be quoted without the contract it was computed under.** That is not a caveat attached for
safety; it is the paper's own finding applied to the paper's own numbers, and Section 13 states
what it demands of anyone who uses the framework afterwards.

