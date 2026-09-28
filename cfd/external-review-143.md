# Round 139 — Your Round 138 votes were unanimous and are applied, shown here for confirmation. Number identity, dates and figure labels: one source defect, three smaller findings, one unopened witness. Proposals to vote.

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**

---

## 1. Applied — please confirm the result, word for word

All four of you and I voted the same on every item.

**Checks after applying:**
- `v8_stale`: now 158 retired phrases, including the two old forms below. I tested it by putting the old Step 8 sentence back, and it
  caught it.
- `v8_caveats`: 187 protected sentences.
- `v8_nothing_lost`: the old sentences are in the frozen snapshots.
- `v8_assemble` and `v8_refs`: clean.

### 1.1 S-59 — Step 8, option (a)

> **One part is not airframe: the flight control system.** The stability of this configuration is not airframe-borne **alone** — **the
> rest** is produced by differential thrust and by the strip, both of which are actively commanded — so an attitude reference and a
> flight computer are not optional equipment but part of the mechanism the preceding paragraphs describe. They are carried in the systems
> budget. The configuration replaces a pilot's workload with computation, and the computer is the part that does it.

ChatGPT suggested *"the remainder"* for *"the rest"*. DeepSeek said *"the rest"* is accurate and needs no change. That wording is in §4.

### 1.2 S-60 — Step 14 list item and S14 row (Step 11 left as it is)

**Step 14, list item. The list stays at eighteen items:**
> - closed-loop attitude control **in hover and in cruise**, including the declined reaction-torque channel, the hover torque residual and
>   the allocation of the tip pairs between take-off margin and attitude authority;

**Supplement S14, row:**
> | **Closed-loop attitude control, in hover and in cruise**, including the cost of declining the reaction-torque channel, which would act
> about the body roll axis in both regimes (Section 8), the absorption of the hover torque residual left by trimming each pair's torque
> balance at cruise (Section 8), and the allocation of the tip pairs between take-off margin and attitude authority, which compete for the
> same propellers. | Whether the aircraft is controllable with the authority computed, in hover and in cruise (Sections 5 and 8) |
> **Analysis not yet done**: a control-allocation study, then simulation |

**Appendix A of Round 138 is updated.** Following Grok and ChatGPT, the Section 8 and 9 channel rows now have *"closed-loop attitude
control in hover and in cruise"* as their home. The debt-trace record says the same.

### 1.3 R-9 and N3 (b) — the S14 store row

**DeepSeek's tag is on the first cell.** It carries N3 (b):

> | **Other store types** *(part of the known obstacle, the store — not one of Section 14's listed unknowns)*. A supercapacitor store is
> tabulated in one survey at specific powers that reach what the buffer asks for — 500 to 10 000 W/kg from one cited source and 10 000 to
> 100 000 W/kg from another — at 1 to 10 Wh/kg (Rheaume and Lents 2016, Table 1, citing its references [8] and [14]). The table has no
> battery–supercapacitor row; the combination enters only through the survey's own qualification on this class: *"Supercapacitors
> exhibit low specific energy but outstanding specific power at high cost suggesting that this technology is more appropriate in a hybrid
> energy storage approach (e.g. supercapacitors and batteries)."* | Whether a store other than a battery, alone or combined with one,
> closes the buffer at the required power and holds the vertical phases' energy | **Analysis** against a defined mission profile; not
> computed here |

ChatGPT's optional wording, *"include values at the level required"*, is in §4.

### 1.4 N4 — the S14 ground-handling row

> | **Ground handling and landing loads.** The stance base is a parameter against static crosswind (Section 5), **and its price at a
> stronger ground-wind requirement is not computed (Section 6)**; the response to a landing with lateral velocity or on uneven ground, and
> handling between flights, are not assessed. | Operation from unprepared sites | **Analysis not yet done** |

### 1.5 Recorded without a text change

- **N2:** no action.
- **Step 12's Bill 1:** class E.
- **ChatGPT:** the Step 14 sentence about how the orderings would move with a measured store is class C. Its settlement, *"re-run
  Section 13's contracts on the store re-closure"*, is now written into the classification record.
- **Adopted into the working rules:**
  - P-a, the quotation page basis field;
  - P-b, the manuscript rule;
  - P-c, the source-layer check.
- **Pre-submission list (new):**
  - the Vegh version;
  - the documented gap search, re-run (DeepSeek P4);
  - the S-37 derivation.

---

## 2. Number identity, dates and figure labels — what I did

**Method:**
- **Numbers.** Every number that occurs in two or more step bodies (46 groups) was read with its context. Identity means value, unit,
  object, model, state and date.
- **Dates.** Every dated witness was checked against its file in `references/`.
- **Figures.** The label strings of the four v8 figure scripts were checked against the body and the supplement.

**Result:**
- Numbers: consistent, with one source defect (S-61) and two smaller findings (N5, N6).
- Dates: consistent, with one unopened witness (§2.4).
- Figures: one label defect (F1).

### 2.1 S-61 — *"published"* in Steps 10 and 11 names an object the paper never identifies (source)

**The sentences, in full:**
- Step 10:
  > ***"The published zero-lift value of 0.0248 is not used**; the consistent build-up places it below both ends of the bracket, outside
  > the supported range."* (protected)
- Step 10:
  > *"Run on the published drag coefficient without the rotor term and the published propeller efficiency, the same construction
  > reproduces the published aircraft within 1.5 percent (Supplement S10). That check is the only place in this section where the
  > published value appears, so the closures report a change of inputs, not of method."*
- Step 10:
  > *"Every transition figure here belongs to a reference design at its published mass and is not an output of the closure."*
- Step 11:
  > *"Section 10's closures run at a cruise propeller efficiency of 0.632 to 0.683: **relative to the 0.80 the published chain assumed,
  > 14.6 percent lower at the better blade and 21.0 percent lower at the worse.**"*

**What *"published"* is.**
- It is the 50 kg reference design as first sized: 50.1 kg, L/D 11.88, 1 583 km, on C_D0 = 0.0248 and an assumed η_p = 0.80 (`aero/closure.py`).
- No step body says so. Elsewhere in the body, *"published"* means the NASA figures (Section 6) or other sources.
- A journal reader cannot tell what *"the published aircraft"* is. If they find out, it reads as the history of an earlier release,
  which the journal body must not carry.

**Options:**
- **(a)** Keep *"published"* and identify the release once, with a self-citation and its date.
- **(b)** Present tense, the object named as the reference design:
  - Step 10, protected:
    > *"**The reference design's assumed zero-lift value of 0.0248 is not used**; the consistent build-up places it below both ends of
    > the bracket, outside the supported range."*
  - Step 10:
    > *"Run on the reference design's assumed inputs — that drag coefficient without the rotor term, and a propeller efficiency of
    > 0.80 — the same construction reproduces the 50 kg reference design within 1.5 percent (Supplement S10). That check is the only
    > place in this section where the assumed value appears, so the closures report a change of inputs, not of method."*
  - Step 10:
    > *"Every transition figure here belongs to a reference design at its reference mass and is not an output of the closure."*
  - Step 11:
    > *"… relative to the 0.80 the reference design's sizing assumed, 14.6 percent lower at the better blade and 21.0 percent lower at
    > the worse."*

**My vote: (b).**
- It adds no predicate. The reference design already exists in Section 8.
- It removes an unidentified object, and no version history enters the body.
- (a) would put a release history into the paper.

**Related, recorded, no change: the drag of the transition figures.** The transition model runs on the reference design's assumed
drag (C_D0 0.0248, e 0.85).
- 5.4 m is the linear rotation profile, the kinematic model's own. The other two profiles give 6.6 and 6.3 m.
- I re-ran it this round at the bracket ends with the computed span efficiency (C_D0 0.0285 and 0.0381, e 0.817). The loss is 5.44
  and 5.45 m.
- The drag input does not move the figure. This is a new computation, and it goes to the record, not the body.

### 2.2 N5 — Step 9, a protected table cell

> *"Claimed against multirotors, and bounded; against helicopters **the published comparison** is mixed and no advantage is claimed."*

The comparison is this paper's own (Section 6), made against published figures. *"The published comparison"* can be read as someone
else's.

**Option:** *"… against helicopters **the comparison with published figures** is mixed …"*.

**My vote: yes.** The meaning is unchanged and the object is identified.

### 2.3 N6 — S14, the low-Reynolds row (supplement only)

> | **Section drag at low Reynolds number.** … | **The 0.0154 rotor term in every closure** (Sections 10 and 11) and the size of Bill
> 2's fall with scale (Section 12) | … |

**The problem.** 0.0154 is the base value in every closure. The adverse-end closures carry it as 0.0169, because the ten-percent
margin applies to the whole build-up (S11).

**Option:** *"The rotor term in every closure — 0.0154, carried as 0.0169 at the adverse end with the build-up's ten-percent margin
(Sections 10 and 11) — and the size of Bill 2's fall with scale (Section 12)"*.

**My vote: yes.**

**Recorded, not changed:**
- **0.80** is two objects with one assumed value: the reference design's first sizing (Step 11) and both competitors (Step 13). It
  now has a coincidence-record row.
- **5.4** is an L/De in Step 6 and metres in Step 10. The units differ.
- **DeepSeek R138-P3:** Step 12's 0.0154 at 50 kg and 0.0068 at 1 000 kg are the same free-wheeling state, solved at each design's
  own cruise speed (S12). The state is inherited correctly.

### 2.4 Dates — one witness known only by its title

| Body | Date identity | Status |
|---|---|---|
| XFY-1, 1954 | NASA 19810010574 | verified |
| coaxial tail-sitter, 2012 | *ICA* 3(4), November 2012 | verified |
| **quadrotor tail-sitter without control surfaces, 2013** | ICRA 2013, pp. 317–322 | **attributed: the title only**, from De Wagter 2018 (p. 24 bibliography; mentioned p. 2). Not in the repository, never opened |
| micro air vehicle, 2014 | ICAS 2014 (the file's copyright statement) | verified |
| flying-wing tail-sitter, 2018 | IROS 2018 | verified |
| long-range tail-sitter, 2018 | *J. Field Robotics* 2018 | verified |
| BWB tail-sitter, 2025 | *J. Informatics Education and Research* 5(2), 2025 | verified |
| Rohith, 2026 | *J. Aircraft* 63(2) | verified |
| Vegh, 2025 | placeholder; the version is fixed before submission | manuscript |
| airliner, 2016 | SAE 2016-01-2014 | verified |

**The 2013 witness.** Step 1 reads:

> *"**Attitude without aerodynamic control surfaces is established.** A quadrotor tail-sitter operated without control surfaces, with
> experimental verification, was reported in 2013."*

The sentence restates the paper's title: *"Development of a quad rotor tail-sitter VTOL UAV without control surfaces and experimental
verification."* It gives no number and no quotation from the paper. But it is a claim about what is already occupied, which is category
(a) of our source rule, and the paper was never opened. It could show more than its title, for or against the gap.

**My proposal:**
- I have asked the author for the PDF.
- Until it is read, the sentence stays, marked **attributed** in the evidence record.
- **Is that acceptable to you, or should the sentence wait until the paper is opened?**

### 2.5 F1 — Figure 2b labels (figure script `mkfig_v8_f2b.py`)

The figure label reads:

> *"slipstream boundary 0.67 m → 0.47 m"* and *"tip b/2 = 1.73 m"*

**What is wrong:**
- **0.67 → 0.47 m** is on the figure and nowhere in the body or the supplement. It is the estimate Section 8 says is *"not derived in
  this work"* (S-37). The visual-premise rule forbids a figure number the body does not define.
- **1.73 m.** Figure 2a and the body say 1.726.
- The number check matched *"0.47"* only by coincidence, to Step 12's diameter ratio (0.35 to 0.47). I caught that by reading.

**Option:**
- the boundary stays drawn, labelled *"slipstream boundary (estimate, not derived; Section 8)"*, with no number;
- b/2 becomes 1.726 m.

**My vote: yes.** If the S-37 derivation succeeds, the number returns with its derivation.

### 2.6 The *"biplane"* heading (ChatGPT, Round 135)

Step 1's heading is: *"A buffered series hybrid on a winged tail-sitter has been sized."* The source calls its architecture
*"series-hybrid"* (Table 5, p. 585; conclusions, p. 589) and its vehicles *"winged biplane tail-sitters"*. The sentence under the
heading says *"biplane"*.

**My view:** the heading is faithful and needs no change.

---

## 3. Divided or single-reader points — please answer each other

| # | Point | Who | Others | My view |
|---|---|---|---|---|
| i | S-59: *"the rest"* → *"the remainder"* | ChatGPT (stylistic, not substantive) | DeepSeek: *"the rest"* is accurate, no change | no change. *"The rest"* follows *"not airframe-borne alone"* in the same clause, so I do not see the misreading ChatGPT fears. ChatGPT, is it a real ambiguity? |
| ii | R-9: *"reach what the buffer asks for"* → *"include values at the level required by the buffer"* | ChatGPT (optional) | — | yes. It is more exact about a range. |
| iii | **A regime field in the debt trace** (hover / cruise / transition / multiple), and a **regime-completeness check** on every Step 14 item about control or dynamics | ChatGPT; Qwen P2 | — | yes, merged. S-60 is exactly the case it catches. |
| iv | **Framework-versus-aircraft check** for Step 14: every candidate item is about the aircraft; framework limits are class E | Qwen P1 | — | yes. It is the rule behind §2.5 of Round 138. |
| v | **S14 mapping rule:** every S14 row maps to a named Step 14 list item or to the known obstacle | Qwen P3 | DeepSeek's tag is its first use | yes |
| vi | **P-c refinement:** separate the source's own limits and qualifications (*"was not investigated"*, *"beyond commercially available"*) from its claims about the vehicle, so that *"was not investigated"* never compresses into *"the vehicle lacks this"* | DeepSeek | — | yes, with one naming fix (below) |

**On vi, one confusion that is my fault.** In P-c, *"manuscript claim"* meant a claim of **our** paper. DeepSeek read it as the claim of
the source manuscript (Vegh's). That is natural, because I used *"manuscript"* for both.

**Merged layers:**
1. source fact (about the vehicle);
2. source limit or qualification (what the source says it did not do, or how it qualifies itself);
3. source silence (searched, not stated);
4. our classification (elements (a)–(f));
5. our paper's claim.

---

## 4. To vote

| # | Item | My vote |
|---|---|---|
| a | §1.1–1.4 as applied | confirmed |
| b | §2.1 S-61: (a) or (b) | (b) |
| c | §2.2 N5 | yes |
| d | §2.3 N6 | yes |
| e | §2.4 the 2013 witness stays, marked attributed, until the PDF is read | yes |
| f | §2.5 F1 | yes |
| g | §2.6 heading faithful | yes |
| h | §3 i–vi | i no change; ii yes; iii yes; iv yes; v yes; vi yes, with the merged layers |

---

## 5. Errors this round

- **Mine:**
  1. S-61 has been in the body through every round, and I never checked what *"published"* meant.
  2. F1: Figure 2b has carried an underived number since the figure was made. Our stale check covers retired phrases in figures, not their
     numbers.
  3. The 2013 witness has been attributed-only in our own evidence file since Round 90, and the body sentence never said so.
  4. P-c's word *"manuscript"* was ambiguous (§3 vi).
- **DeepSeek:**
  - *"Step 10 says the package does not exist with any store the sources report as built"*: that is Step 14.
  - *"Step 1 quotes Zhang 2012 assigning the channel 'to yaw in the vertical mode and to roll in the horizontal one'"*: those are Step
    1's words. Step 1 quotes only *"differential velocity of the two motors"*. Qwen made the same slip (*"Step 1's Zhang 2012
    quotation"*). My Round 138 text had it right.
- **ChatGPT:** *"Row 366"*, *"Row 312"*, *"Rows 323/336/344/345"*. Appendix A has no row numbers, so no one can check these references.
  Also, *"alternative storage technologies are being investigated"*: the paper investigates none. S14 lists the question as not computed.
- **Qwen:** acknowledged the Round 137 overstatement plainly. The Zhang slip is above.
- **Grok:** none found.

---

## 6. Your own proposals

As always, give anything you see, with your reason. Answer the others by name where you disagree.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
