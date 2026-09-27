# Round 131 — The author decides: the tip pairs free-wheel at zero shaft torque. S-53 (A, B), S-54 and S-55 applied; please confirm. S-56 not applied: the voted wording was also wrong, and Qwen's reasoning shows why. The S-57 sentence, from your four drafts.

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`cedf3c8`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**

---

## 0. The author's decision

> *"Let it stay at zero shaft torque."*

The tip pairs' uncommanded cruise state is **free-wheeling at zero shaft torque**. That is the state Section 11 computes and charges
(ΔC_D0 0.0154 for the eight discs at the favourable end). **The zero-thrust, motor-driven state is not adopted and not computed.** It is
recorded in the project's working rules, so that it is not lost again.

---

## 1. Applied — please confirm the results

All four of you and I voted for each item.

**S-53 (A), Step 8. The protected clause, R-repaired.** The protected row is updated to the new words.
> Before: *"Neither the means nor the azimuth is fixed by this study, and the drag figure quoted for the stopped condition should be read
> as the state Section 11 defines rather than as the state a particular installation would reach."*
>
> After: *"Neither the means nor the azimuth is fixed by this study, and the drag figures estimated for the stopped condition (Supplement
> S11) should be read as estimates for an assumed azimuth rather than as the state a particular installation would reach."*

**S-53 (B), Step 11, Bill 2. New sentence** after *"… it is not a claim that this drag would disappear if the vertical phase did."*:
> **No stopped-state counterfactual was computed.** The eight tip discs stopped edge-on at a controlled azimuth are estimated at ΔC_D0 =
> 0.0008, against the computed free-wheeling 0.0154 (the estimate is an area-and-coefficient calculation, Supplement S11), but
> controlling the azimuth takes an indexing mechanism — a class Section 7 counts — and sizing it for eight small discs, charging its
> mass and its failure modes, and re-solving the loop has not been done.

DeepSeek's optional *"at the favourable end"* was not added. The sentence before it in the same paragraph already says *"the rotor
term alone is 0.0154 at the favourable end"*.

**S-54 (a), Step 2. The paragraph is deleted:**
> ~~**This charge has been identified independently, and by a source with no interest in the present argument.** The NASA sizing study
> of Section 4 found the lift-plus-cruise concepts the heaviest of the vehicles examined, and named the cause: not the cruise power
> draw, since the lift-plus-cruise effective lift-to-drag ratio is the higher of the set, but *"the extra empty weight items on board in
> hover."* That is Bill 1 stated by an independent source in its own terms: not a failure of engineering, but the cost of an
> architecture.~~

- Step 2 now runs from the non-linearity paragraph (*"… A modest dead-mass fraction becomes a large payload penalty."*) straight to
  *"### Bill 2 — drag"*.
- Bill 1's independent support is Step 4's, on Johnson & Silva 2022.
- The 2018 source is recorded in the evidence file as **contradicts** (for the Bill 1 reading), not used in the body.
- **Check, please:** does anything later in the paper depend on Step 2 having said *"identified independently"*? My search found
  nothing.

**S-55, Step 6. Deletion:**
> *"… 1.49 times stall, which ~~Section 10 states explicitly~~ is **not** its best lift-to-drag point."*

**Checks.**
- The deletion-only check is clean on Steps 2, 6 and 8 (Step 8's clause is the voted R).
- No protected sentence is missing.
- Four phrases are retired (155 in the list).
- Body prose: Step 2 1 697, Step 6 1 879, Step 8 1 962, Step 11 902; total 18 578.

---

## 2. S-56 — not applied, because the voted wording was also wrong (credit: Qwen)

**What we voted.** All four of you and I voted (b), my wording: *"Section 11 charges the third; the first two are not priced in this
work."*

**Why it was not applied.** Qwen's answer on the mirror-cost question said the wing's mass is *"baseline airframe mass, priced in the
sizing loop"*. I checked, and Qwen is right:
- **The wing's mass is inside Section 10's closure.** The loop holds wing loading fixed, so the wing grows with take-off mass. Structure
  sits in the empty fraction: the airframe, wing included, is a fixed 0.30 of take-off mass (`aero/baseline.py`, `f_govde`), and
  MTOW = m_payload / (1 − f_empty − f_energy). Carrying the wing through hover is therefore paid for in
  the closure, through take-off mass and hover power. It is simply not separated out.
- **The constrained planform is inside the computed aerodynamics.** The span efficiency, e = 0.817, is the vortex-lattice result for the
  trimmed planform (Supplement S6). Whatever the sweep constraint costs is inside that number. No unconstrained counterfactual was run.
- **What is not priced anywhere** is the wing's exposure to ground wind. Step 14 lists *"ground handling and landing loads"* as an
  unknown.

So *"not priced in this work"* would have been a new overstatement, in the other direction from S-56 itself. **This is my error.** I
checked Section 11 for the receipt but not Section 10's closure for the cost.

**Corrected R, to vote:**
> *"Section 11 charges the third. The first two are inside Section 10's closed numbers — the wing's mass in the empty fraction, the
> constrained planform in the computed span efficiency — but neither is separated out as a charge, and the wing's exposure to ground wind
> is not priced in this work."*

**The mirror-cost question**, where your answers diverge:
- **Grok and DeepSeek:** a scope sentence saying the cost is outside the three bills.
- **ChatGPT:** leave it open; do not classify.
- **Qwen:** no framework change; the wing is airframe, priced through MTOW.

**My view:** the corrected S-56 sentence is the scope statement this configuration needs. It says where the cost is (inside the closure,
not attributed) and what is unpriced (ground wind), without defining a mirror bill that Section 2 lacks. **Grok, DeepSeek:** does it
meet your reason? **ChatGPT:** does it classify more than you would?

**Grok P125** (S-56's costs as Step 14 candidates): with the correction, only the ground-wind part is unpriced, and Step 14 already lists
ground handling. My view: nothing to add.

---

## 3. S-57 — the adopted state, now decided; the sentence from your drafts

**Step 8 [28], as it stands:**
> **The fixed geometry of the tip pairs leaves two admissible cruise states, and only one of them is physically closed.** Unable to
> feather, the pairs must either turn at the zero-shaft-torque condition or be stopped.

**All four of you rejected my *"that is the state assumed throughout"*:** the tip pairs make moments in cruise, so they are driven when
commanded. Your drafts:

| | Draft |
|---|---|
| Grok | *"The drag state assumed in the ledger is free-wheeling at zero shaft torque."* |
| ChatGPT | *"This configuration uses the zero-shaft-torque, free-wheeling state as its uncommanded cruise state, and that is the drag state assumed throughout."* |
| DeepSeek | *"This configuration **trims** them at the zero-shaft-torque condition in cruise, and that is the state assumed throughout."* |
| Qwen | hold until the author decides, and reconcile with attitude control |

**Merged proposal (R), to follow *"… or be stopped."*:**
> ***"This configuration uses the first: free-wheeling at zero shaft torque is the tip pairs' uncommanded cruise state, and it is the
> drag state Section 11 charges."***

**Why this wording:**
- ***"uncommanded"*** (ChatGPT) leaves commanded moments as departures from the baseline. That answers Qwen's tension, and Grok's and
  DeepSeek's objection to *"throughout"*.
- ***"the drag state Section 11 charges"*** (Grok's ledger point) names what the state is used for, and its receipt holds: Section 11
  charges the free-wheeling rotors.
- ***"trims"*** (DeepSeek) is not used. In this paper *trim* also means the aircraft's pitch trim, which comes from the planform's lift
  distribution (Step 6). Using it for the rotors would mix two senses.

**Qwen P1 (the cost basis).** The uncommanded state's cost is the drag above, and it is charged. The shaft power of commanded departures
in cruise — moments for attitude — is **not computed** anywhere, and no step says so. **Should it be named?** My view: yes, but as a
clause in Step 14's existing *"closed-loop hover control"* item would change a closed list. I would rather ask you first than propose
wording.

**Steps 7 and 15 stay conditional** (all four of you and I agree).

---

## 4. The completion list and the order of work

**Accepted (all four of you and I):**
- i–vi of Round 130;
- two halves (Steps 1–8, then 9–15) and a short reconciliation.

**The order**, following ChatGPT's sequence, adjusted:

| | Item | State |
|---|---|---|
| A–D | S-53, S-54, S-55 | applied; confirm (§1) |
| C′ | S-56 | corrected R, to vote (§2) |
| E | S-57 | author decided; sentence to vote (§3) |
| F | **re-run the receipt audit** on the repaired text (the repairs add new pointers: S11, *"Section 11 charges"*) | after C′ and E |
| G | surface and identity sweep: numbers, counts, axis names **against the state each describes** (DeepSeek), figure labels | next |
| H | record-propagation sweep, **including the receipt-audit table itself** (DeepSeek) | next |
| I | denial maps: Step 1 and Step 8 | next |
| — | Rohith and Vegh PDFs | waiting for the files |
| J | the whole reading: 1–8, 9–15, reconciliation | last |

**New proposals, to vote:**
- **Qwen P2 and ChatGPT:** the receipt audit becomes a **standing end-of-stage check** for every future stage. My vote: yes.
- **ChatGPT:** receipt categories R1–R4 in the audit table (R1 carried; R2 carried but qualified differently; R3 resolves, content
  absent; R4 sender overstates). Already added to `receipt-audit.md`. Confirm?
- **DeepSeek:** unnumbered pointers (*above*, *below*) as a next-stage candidate. My vote: yes, next stage.

---

## 5. Errors this round, and your positions on each other

**Mine.**
- **S-56 (b)** was my wording, and all four of you voted for it. It would have introduced a new overstatement: *"not priced"* when the
  mass and the planform are inside the closure. I checked the receiver for the promise but not the closure for the cost. Qwen's reasoning
  on another question exposed it.
- **S-57:** my *"that is the state assumed throughout"* would have reintroduced what v7's *"neither driven"* got wrong. All four of you
  caught it.

**Qwen.** You wrote *"I must refer to the facilitator as Claude"*, and then used *"K"* for me four more times in the same reply. Please
use *Claude*. **Credit:** your S-56 reasoning is the reason a wrong repair was not applied.

**ChatGPT, DeepSeek, Grok.** None found.

**Positions to answer each other (§2):** the mirror-cost scope sentence. Grok and DeepSeek want one; ChatGPT says leave it open; Qwen says
no framework change. The corrected S-56 sentence is offered as the common ground. Say whether it is.

---

## 6. To vote

| # | Item | My vote |
|---|---|---|
| a | §1: confirm S-53 (A, B), S-54, S-55 as applied | confirmed |
| b | §2: the corrected S-56 R | yes |
| c | §2: the mirror-cost question — is the S-56 sentence enough? | yes |
| d | §3: the S-57 sentence | yes |
| e | §3: Qwen P1 — should the uncomputed shaft power of commanded departures be named, and where? | yes; where is open |
| f | §4: the receipt audit as a standing end-of-stage check; R1–R4; unnumbered pointers next stage | yes; yes; yes |

---

## 7. Your own proposals

As always, give anything you see, with your reason.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
