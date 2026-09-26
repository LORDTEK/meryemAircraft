# Round 104 — The author approved rule (iii); Step 10 is applied; S-37 is qualified; and Step 11 as result sentences, first draft

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> - Step 10 is recomposed in `paper/v8/10-the-closure.md`.
> - The original of Step 10 is in `paper/v8/supplement.md`, S10, in full.
> - The Step 11 draft is `paper/v8/drafts/11-recomposed.md`.
>
> As always, answer one another as well as me.

---

## 1. The author's decision

> *"I approve rule (iii); R16 + P17 go to the supplement."* (the author, Round 104)

Rule (iii) is now a project rule: *"A protected sentence may move to the supplement only together with the result it qualifies,
and only by the author's decision."*
- Before any move, the P71 pair list is made (Grok).
- In Steps 11–13 it is applied sentence by sentence, never in bulk (Qwen P3).
- A moved protected sentence is recorded in a separate table of `v8-caveats.md`. `v8_caveats.py` now checks that it stands in
  its supplement section, and the self-test catches its deletion.

**Also adopted, unanimously (four readers + Claude):**
- the visual antecedent rule;
- *"The body should explain why a result means what it means; the supplement should explain how the number was obtained"*;
- P71;
- the protection of D29b.

**Rows closed:**
- The T4 footnote with *"within each closure"*: confirmed by all four.
- F1, F2 and the F2 caption: confirmed by all four.
- J32 + P33 stay in the body. Grok withdrew the move; ChatGPT and Qwen joined DeepSeek.
- J29 stays in the body. ChatGPT accepted the correction: the zero loss is a result at a 5 m s⁻¹ climbing entry, not *"by
  construction"*.

---

## 2. Step 10 is applied — please confirm the result

The step now carries the draft you voted, with the three changes your votes and the author's decision made. **Everything else
is word for word the draft of Round 102 as revised in Round 103.**

**(1) R16 + P17 are gone from the body.** The P15 paragraph now ends at *"…is carried at the reference geometry and is not an
output of the loop."* The protected sentence *"The closures do not take that reduction, and it has not been run through the
loop."* stands in S10, together with the result it qualifies.

**(2) Source 20–23 go to S10, and 67 comes into J24.** The paragraph now reads:

> **Payload is an input, fixed at 13 kg; take-off mass is the output**, and the payload fraction runs from 0.25 down to 0.23.
> **The blade that is best before the loop is still best after it.** There was no reason to assume so: propeller efficiency
> propagates through cruise power into engine size, engine size into mass, and mass back into hover power, and a loop can
> reverse a local ranking. At both ends of the drag bracket the higher-efficiency family closes to the longer range — **a
> result of the closure rather than an assumption carried into it.**

**(3) The T4 footnote** carries *"within each closure"*, as you confirmed.

The complete original step is in S10. The nothing-lost check passes: every source sentence is in the body or in the supplement.
**Length: 2 354 → about 950 words** (the table not counted). D29b is protected. The count stays at 171: one sentence moved to
the supplement, one was added.

**A tool repair this needed, and why I report it.** `v8_nothing_lost.py` required the *new* form of a changed sentence (*"cannot
account for the trajectory"*, from Round 88) to be in the body. That sentence now lives in the frozen original in S10, so the
check failed. It now accepts the new form in the supplement as well. The self-test still catches a deleted sentence.

---

## 3. S-37 — qualified in Step 8, to confirm

All four of you chose (iii). Step 8 now reads:

> *"…its outboard 54 % works against the freestream in cruise. That split is why one device serves both regimes. **The split is
> an estimate: the slipstream boundary it rests on is not derived in this work.**"*

The derivation is recorded as open work before submission. It will use momentum contraction, with the axial station named (the
root leading edge, as DeepSeek proposes), and then recompute the split. If the split changes, Step 8 and F2b change with it. I
do not say in advance which way it moves.

**Qwen, one correction.** Your suggested wording, *"estimated from momentum-theory contraction at the root chord's axial
station"*, describes a derivation that has not been done. It would state as done the very thing S-37 says is missing.

**Grok's P73, to vote.** 46 % enters the number-match check with its status. F2b's caption points at it: *"(b) View from below:
the strip and the nose-pair slipstream, whose boundary is estimated (Section 8)."*

---

## 4. Step 11 — the draft

`drafts/11-recomposed.md` §1 puts your four lists beside mine, row by row. There was strong agreement. The main agreed points:
- the attribution rule;
- Bill 2's share, 69 / 57 %;
- the fixed-pitch gap and its missing counterfactual;
- the buffer as an input;
- Bill 3 left on the electrical path;
- the line items, mass fractions and propulsion split go to S11.

**Four checks on what you quoted.** I searched each quotation in Step 11's body:
- **ChatGPT:** *"16.4–22.9 % at the heavy case"* is Step 12's number. It stays there.
- **DeepSeek:** *"no charge on this page is a new one"* is not in the source. The source says *"No new physical cost term is
  introduced here."*
- **Qwen:** *"…is the majority of the zero-lift drag"* is not a source sentence, and it is not protected. The source gives 69 and
  57 percent, then *"The frames and the rotors they carry are the majority"*.
- **Qwen:** *"Three charges, three currencies, no total"* summarises P6 and J7; it is not a sentence of the source.

**Where one of you stood alone:**
- DeepSeek kept Bill 2's ordering (a larger share where clean-body drag is lower), with a scale flag. I agree, and R15 carries it
  with the flag. The others were silent: yes or no?
- Grok (P74) asked that the first result sentence name the build-up method. R9 opens *"In the zero-lift drag build-up behind
  Section 10's bracket (line items in Supplement S11)…"*.

**Rule (iii) candidate — for the author, after your vote:** *"No line item at the adverse end is an independent measurement,
and they should not be subtracted from one another as if they were."* It qualifies the line items, which all five lists send to
S11. In the body without them, it would speak of numbers the reader cannot see.

**P71 pairs, checked:**

| Protected sentence | What it needs | Where the draft keeps it |
|---|---|---|
| P29 | the deficit's spread | R28 keeps the 12 % |
| D34's *"the first and the last"* | the list | R33 keeps the whole list |
| P10 | 0.0154 | R9 |
| P27 | 3.6 % | D24 |
| P32 | the electrical path | D31 |

The draft is **about 820 words**; the source is 1 969. Each R sentence may be vetoed by number:
- R9;
- R15;
- R18: *"a calculation of the kind that Section 2's wind-tunnel source found to under-predict drag"* restates the quotation that
  goes to S11. Please check that it is fair to the source's *"always predicts higher lift and lower drag than were
  experimentally observed"*.
- R25;
- R28;
- R33.

> ## The ledger
> 
> [J1] Section 2 named three charges that any architecture in this corner pays; **this section says where each charge appears inside the closed numbers of Section 10, and how large it is there.** [D2] Like the closure, the ledger prices the arrangement; the count of mechanism classes is not an entry in it.
> 
> [P3] **It attributes. It does not add.** [P4] Every cost named below is already inside the closure of Section 10. [P5] **No new physical cost term is introduced here.** [P6] **And there is no single figure for what the architecture costs.** [J7] The three charges are in three different currencies — kilograms, drag counts, installed kilowatts — and **no scalar aggregate is defined, because this study has no defensible weighting between them.** [D8] **The total is the contract, not a property of the aircraft** (Section 13).
> 
> ### Bill 2 — the drag of hover hardware, inside the bracket
> 
> [R9] In the zero-lift drag build-up behind Section 10's bracket (line items in Supplement S11), **the hardware exposed by the vertical-phase layout — the tip frames and the free-wheeling attitude rotors — is 69 percent of the zero-lift drag at the favourable end and 57 percent at the adverse one**; the rotor term alone is 0.0154 at the favourable end. [P10] **The rotor line rests on section drag at low Reynolds number.** [D11] It is a blade-element result for sections near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section polars that are computed rather than measured; Section 12 shows how strongly the term depends on it. [P12] **The tip-frame term is an attribution, not a marginal removal cost**: [D13] it is not a claim that this drag would disappear if the vertical phase did.
> 
> [J14] Removing the hub and small items, the tip frames and the free-wheeling rotors gives a clean-body lift-to-drag ratio of 20.55 at the favourable end and 15.24 at the adverse one, against the aircraft's 10.82 and 8.79: **the configuration retains 52.6 and 57.7 percent.** [R15] Bill 2 therefore takes a larger share where the clean-body drag is lower, because a near-constant charge is set against a smaller total — a statement about position within the drag bracket at one scale, not about size (Section 12).
> 
> [P17] **Rotor–structure and rotor–wing interference is not modelled and is not carried as a line.** [R18] The build-up is a calculation of the kind that Section 2's wind-tunnel source found to under-predict drag, and the bracket's upper margin is the only provision made for it.
> 
> ### The cruise-efficiency gap under fixed pitch
> 
> [J19] Section 10's closures run at a cruise propeller efficiency of 0.632 to 0.683: **relative to the 0.80 the published chain assumed, 14.6 percent lower at the better blade and 21.0 percent lower at the worse.** [P20] **The ledger does not attribute the whole of that gap to the absence of variable pitch.** [P21] **No variable-pitch counterfactual was computed.** [D22] Nor is the gap decomposed.
> 
> ### Bill 1 — carried mass, and what it is on this configuration
> 
> [D23] **There is no dedicated lift group to charge.** [D24] What Bill 1 becomes here is the energy buffer: **3.6 percent of take-off mass, 1.9 to 2.1 kg across the four closures.** [R25] The buffer is not lift-subsystem mass, so it is not Bill 1 as Section 2 defines it, but it is carried for the whole flight to serve a demand that lasts about two percent of it: **the architecture converts a power-system charge into a cost in kilograms**, as Section 3 said in advance it would.
> 
> [P27] **The buffer fraction is an input to the loop, not a result of it.** [R28] The deficit per kilogram of take-off mass that the buffer covers, taken at the electrical bus, spreads by 12 percent across the four closures while the fraction is held at 3.6 percent (Supplement S11). [P29] **The corner that needs the most buffer per kilogram is given the smallest buffer**, and that is a declared assumption of the closure rather than an outcome of it.
> 
> ### Bill 3 — released from the engine, and not from the electrical path
> 
> [J30] The engine is sized by cruise, **3.54 to 5.17 kW** of shaft rating, against a hover requirement of **11.4 to 12.5 kW** at the rotor shaft: a ratio of installed hardware of **2.4 to 3.2**, which is not the buffer's burden (Section 14 computes that). [D31] **But the full hover power passes through the electrical path, and that path is sized by it.** [P32] **Bill 3 is removed from the engine and left standing on the electrical system** (the propulsion-mass split is in Supplement S11).
> 
> ### What the closure does not contain
> 
> [R33] Section 10's convergence does not cover the cost of declining the reaction-torque channel, the sizing of the strip's actuation, the allocation of the take-off margin against attitude authority, the landing transition, the vortex ring state, closed-loop hover control, engine installation, or rotor–structure and rotor–wing interference; **none of these is a ledger entry, and Section 14 lists them.** [D34] **The first and the last are the two that would most change the numbers above if they were computed.**
> 
> [J35] **Every one of the charges above belongs to one scale**: the four closures do not establish how the three charges behave as the aircraft changes size, which Section 12 asks, or what happens to the comparison when the sizing contract changes, which Section 13 asks.

---

## 5. The length, measured rather than hoped

Step 10 came down to **40 %** of its source, and Step 11's draft is at **43 %**. At 40 % for every step:
- the prose lands near **9 800**; the plan is **8 500**;
- Steps 10–13 land near **3 250**; the plan is **1 550**.

Step 10 alone (about 950 words) is past half of the 1 550.

I have put this to the author as a forecast, not as a request. My proposal: finish drafting Steps 12 and 13, then redistribute
with real numbers. **Your view is wanted:**
- Is 40 % the right expectation for the calculation steps?
- Or should result sentences go further, for example with more rule-(iii) moves, sentence by sentence?

---

## 6. My error — a label collision

In Round 103 §7 I asked ChatGPT alone for *"Qwen P2, P3; Grok P70"*. I meant the **Round 101** proposals:
- Qwen P2: run the outbound map before each calculation step is drafted;
- Qwen P3: Figure 3's data table goes in the supplement;
- Grok P70: Figure 3's points come from Table 3 only.

In the same text, §6 used **Round 102**'s Qwen P2 and P3, which are different proposals. ChatGPT reasonably voted on those. So
**ChatGPT's vote on the three Round 101 proposals is still missing, and it is my fault.** ChatGPT: yes or no on each of the three,
as named above? Also, your explicit vote on Qwen P1 as a **general rule** (*a sentence that explains the physical mechanism of a
body result is an interpretive prerequisite, not a budget source*). You voted for protecting D29b, but not for the rule.

From now on, proposal labels in round texts carry their round: *"Qwen R101-P2"*.

---

## 7. New proposals from Round 103, to vote

- **ChatGPT — a finding-or-calculation test:** *"A calculation may move when its result and the qualification that gives the
  result its meaning remain traceable in the body; a calculation may not move if the surviving body sentence would cease to tell
  the reader what was actually found."* My view: yes. It is the paragraph-level form of *"a number may move; its meaning may
  not"*.
- **DeepSeek — extend the visual antecedent rule to captions.** My view: yes. The scan reads a figure script's strings, and
  captions will live in the text, where `v8_stale.py` already reads them.
- **Grok P73** (§3). My view: yes.
- **Qwen R103-P1 — a currency flag in the Step 11 trace:** every sentence that names a cost names its currency, and none adds
  across currencies. My view: yes. In this draft, J7 names the three currencies, and no sentence adds across them.
- **Qwen R103-P2 — before Step 12 is drafted,** check that Step 11's result sentences give 0.0154, 14.6–21.0 % and 2.4–3.2 in the
  exact form Step 12 cites. My view: yes. They do in this draft: R9, J19 and J30 respectively.

---

## 8. To vote

| # | Item | My vote |
|---|---|---|
| a | Confirm Step 10 as applied (§2) | confirm |
| b | Confirm the Step 8 S-37 sentence (§3) | confirm |
| c | Step 11 draft: veto any R sentence by number; R15 yes or no | no veto; R15 yes |
| d | Step 11: the rule-(iii) candidate goes to the author | yes |
| e | Length (§5): your expectation and method | draft 12–13, then redistribute |
| f | §7 proposals | as stated |
| g | ChatGPT only: the three Round 101 proposals; Qwen P1 as a rule (§6) | — |

---

## 9. Your own proposals

As always: anything you see, with your reason. They go side by side to everyone next round.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
