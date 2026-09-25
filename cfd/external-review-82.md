# Round 78 — Step 4 is closed. ChatGPT's test found that Section 2 describes its costs in two vocabularies, and a candidate fix is up for your vote. Drafting waits until that is settled

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`be64559`**. The inventory is
> `paper/v8/drafts/02-03-inventory.md`, and its new section is *"Round 78 — decisions, and what the Bill 1 test found"*.
> Steps 2 and 3 are unchanged since `f425af4`. **Everything this round depends on is quoted in full below**, so you can
> answer without opening the file.

---

## 1. Closed and applied

Four readers and I agreed on each of the following:

| Item | Result |
|---|---|
| Step 4: 3.1, 3.2, and the 687 / 679 object check | **Confirmed by all four. Step 4 is closed** (1 586 → 1 356 words) |
| Restatement rule | Adopted. Two homes means the second is cut; a second home survives only if it names its job |
| *"stated before any configuration / not retrofitted"* | Home is **3A**; the 3F occurrence is removable |
| Qwen P3 lock | Extended to **the four parts of 3C**, as well as the four failure modes |
| S-2 | *"the first"* means **the first departure**. It will be named by an R sentence when 3F is drafted |
| S-3 | Step 12 will read *"the distinctness Section 2 asserts"* when it is next opened. Logged as a deferred decision |
| Protection | *"Whether an architecture can decline the mismatch itself, rather than redistribute its consequences, is a different question"*. **The protected list now has 155 entries**; all 155 are present in the steps and in the assembled view |
| Outbound row added (Grok) | Step 11: *"not lift-subsystem mass, so it is not Bill 1 as Section 2 defines it"* |

**No drafting until S-1 is settled.** ChatGPT voted HOLD, and Grok's P25 says not to draft 2E until then. I agree with
both.

**Corrections to the replies.** None of these changes the vote, but each one bears on S-1:

- **Grok:** *"'One row does not pay in any of the three currencies' stays true"* under (c). It does not, as §2 shows. Separately, Step 11 does not apply
  a Bill 1 rule to the hub. It says only that no variable-pitch counterfactual was computed.
- **Qwen:** the split you propose for the pitch hub (Bill 1 on lift rotors, outside the three on a cruise propeller) does
  not fit the row as written. That row describes *"one propulsor … retrimmed across two widely separated operating points"*.
  Also, in S-3 you wrote that Step 12 *"finds they do not have"* separability. That reverses the finding: Step 12 finds
  that two of the charges are **not locked together**.

---

## 2. S-1: what ChatGPT's test found

ChatGPT asked a specific question: *does Section 2 define Bill 1 as lift-subsystem mass? If not, (c) is a rule chosen
because it suits us.* I read 2A, 2B, 2E and 3D together.

**Section 2 does not define Bill 1 explicitly.**

- 2B defines Bill 1 by example: the lift-plus-cruise *"vertical group"*, which *"provides no required lift or thrust during
  cruise and is lifted anyway"*.
- 2A limits the charges to *"architectures with a dedicated lift subsystem"*.
- The words *"lift-subsystem mass"* appear only in 3D and in Step 11. Both say that this is how **Section 2** defines Bill 1.
- 2B's structural paragraph charges to mass the structure that carries *"lift or thrust"* across the span. That is broader
  than a lift subsystem.

**The deeper finding: the text uses two vocabularies.** 2E says:

> *"three distinct accounting quantities — kilograms, drag counts, installed kilowatts … a remedy can move a requirement from
> one currency into another."*

A **charge** is a specific payment. A **currency** is a unit. The right-hand column of the table ("Bill it creates") mixes
the two:

| Row | Right-hand column as written | Currency | That charge, by the lift-subsystem rule? |
|---|---|---|---|
| Folding or retracting | 1 — mechanism, actuation, locking, … | kg | yes (it is on the lift group) |
| **Variable pitch / feathering** | **1** — pitch hub, actuation, … | kg | **no** |
| **Tilt** | Bill 3 standing; coupling and control *"not among the three"* | **kg for the pivot and actuators, missing from the row** | no |

- **The pitch-hub row writes a currency** (*1* here means kilograms).
- **The tilt row writes a charge** and leaves out the kilograms. The text itself shows those kilograms exist:
  - 3B says the mechanism *"adds mass"*.
  - The published breakdown in S4 says *"propulsion returns 146 lb of it because the tilt-wing's mechanism is heavier"*.
  - Step 4 says the tilt-wing *"moves the charge — to the mechanism"*.

**So *"One row does not pay in any of the three currencies"* is false under 2E's own definition of the currencies.** It is
false under (a), (b) and (c) alike. None of the three options repairs it.

**My error in Round 77.** I wrote that option (a) would reopen Step 4 in three places. That was wrong. Step 4's sentences
say the mass charge *moves to the mechanism*, which means the mechanism pays in kilograms. So Step 4 contradicts the
current tilt row, not option (a). The 146 lb figure is in S4, a file I built myself.

---

## 3. Candidate (d): keep the charge and the currency apart. Not applied; please vote

All three changes are in 2E. Nothing outside 2E changes.

**Change A — a new passage after *"…is tested in Section 12."*:**

> **A charge and its currency are not the same thing.** Bill 1 is the mass of a dedicated lift subsystem, Bill 2 the cruise
> drag of hover hardware left exposed, Bill 3 continuous power installed to a hover peak; each is paid in one currency, and a
> remedy's own cost can fall in that currency without being that charge. In the right-hand column of the table, a number
> names the currency.

**Change B — the tilt row, right-hand column.**

Before:
> **Bill 3 is left standing** — with no store, the power plant is still sized by the hover peak — together with gyroscopic
> coupling and a transition control problem, which are **not among the three**

After:
> 1 in kilograms, not as a charge — the pivot and its actuators; **Bill 3 is left standing** — with no store, the power plant
> is still sized by the hover peak; and gyroscopic coupling and a transition control problem, which are **not among the
> three**

**Change C — the paragraph under the table.**

Before:
> **One row does not pay in any of the three currencies, and that is not an oversight.** What a tilting architecture buys its
> unified propulsion group with is a mechanism — a pivot, an actuator, the gyroscopic coupling of a reorienting mass, and a
> control problem through the turn. That is a cost, but it is not one of the three charges this accounting tracks, and the
> next section says why it is treated separately.

After:
> **One row pays part of its cost in none of the three currencies, and that is not an oversight.** What a tilting
> architecture buys its unified propulsion group with is a mechanism — a pivot, an actuator, the gyroscopic coupling of a
> reorienting mass, and a control problem through the turn. The pivot and the actuator are paid in kilograms, although they
> are not lift-subsystem mass; the coupling and the control problem are paid in none of the three. That part is a cost, but
> it is not one of the three charges this accounting tracks, and the next section says why it is treated separately.

**Predicate ledger:**

| New predicate | Effect | Already in the text? |
|---|---|---|
| A charge and its currency are not the same thing | Narrows *"One row does not pay in any…"* | 2E names the currencies; 3D and Step 11 use the charges |
| Bill 1 is lift-subsystem mass, stated in Section 2 | Makes true the claim in 3D and Step 11 that this is how *"Section 2 defines it"* | 3D, Step 11 |
| The tilt pivot and actuators are paid in kilograms and are not lift-subsystem mass | **Admits a cost of tilt designs.** It favours neither this configuration nor tilt | 3B *"adds mass"*; S4 146 lb; Step 4 *"moves the charge"* |
| A number in the right-hand column names the currency | Describes the table | The pitch-hub row already reads this way |

**Downstream effects, checked against the text:**

- Step 4, *"The tilting family avoids it too"*: stays true, because it avoids the lift-group charge.
- Step 4, *"moves the charge — to the mechanism"*: now agrees with the table.
- 3B, *"adds mass"*: now agrees with the table.
- 3D and Step 11, *"as Section 2 defines it"*: now true.
- 3D's gloss of the three charges: becomes a restatement of Change A and can be cut (§2.1 rule).
- 2B's structural paragraph (*"lift or thrust"*): now reads as a cost in kilograms. That is consistent with (d), and the
  paragraph needs no change.

**How (d) relates to the earlier options.** It uses (c)'s **definition** and (a)'s **accounting**: the pivot is not Bill 1,
but it is paid in Bill 1's currency. Grok wrote *"(c) is chosen because it fits the later paper, not because 2A forces it. Say
that."* Under (d), the choice is no longer a choice we would have to defend. The definition is the one 3D and Step 11
already attribute to Section 2, and the kilograms appear in the row because the data put them there.

**My position:** (d). Please answer three questions:

1. Does any sentence in (d) claim more than its source supports?
2. Does Change A's definition sentence conflict with 2A's duty-cycle root?
3. Is there a predicate outside 2E that changes, which I have missed?

---

## 4. S-5 — a question, not a finding

The mechanism's mass and the lift group it replaces are paid in the same currency. That is already true today, because
S4's kilograms are data; (d) only makes it visible. So 2F's positive test can be run on Step 4's tilt-wing. In the
published breakdown, the mechanism returns 146 lb of a 716 lb structural difference.

Two sentences in 2F bear on this:

- The positive form asks that the other two charges be *"no worse"*.
- The clarification says that a remedy which *"simply leaves another standing is not a counter-example — the tilting row is
  the case"*.

**Whether the tilt-wing counts as a counter-example depends on whether "left standing" means "no worse". The text does not
say against which baseline.** I have not checked how the NASA categories map onto the charges, so I am not claiming that the
tilt-wing is a counter-example. I am asking whether 2F needs to name its baseline.

**My position:** 2F should name its baseline. Every row of the table implicitly compares a move with the architecture it
modifies. I would not propose wording until you have read this.

---

## 5. Proposals from Round 77, side by side, with my view

| Proposal | My view |
|---|---|
| **Grok P24**: in the trace, flag every sentence that names a Bill with the definition it uses | **Yes.** Under (d), the flag becomes *charge* or *currency*, which is sharper than *duty-cycle* versus *lift-subsystem* |
| **Grok P25**: do not draft 2E until S-1 is applied or explicitly deferred | **Yes.** Already adopted (§1) |
| **ChatGPT**: an allocation-rule test, meaning row → governing definition → classification → consequences | **Yes.** It is the table in §2; it becomes a column of the trace |
| **DeepSeek**: a duty-cycle note in 2E | **Covered by (d)**, Changes A and C. If you want the words *"duty-cycle character"* themselves, propose them |
| **Qwen P1**: the prose after the table separates *Bill 1* from *mass carrying Bill 1's complaint* | **Covered by (d)**, in the vocabulary of currency |
| **Qwen P2**: 2E is the accounting view and 3B the architectural view, joined by one J sentence | **Yes**, for the 3B draft. The join must state no fact (J rule) |

---

## 6. What I am asking

1. **Vote on (d): Changes A, B and C, separately.** Answer the three questions at the end of §3.
2. **S-5:** is this a real gap in 2F? Should 2F name its baseline?
3. **Check the corrections** in §1 and my own error in §2.
4. **New proposals**, as always.

**Next round:** if (d) is agreed, it is applied as a content change with before and after shown, and it goes back to you
for confirmation. After that comes the snapshot, the trace, and the draft beginning with 3B. **If (d) is not agreed, there
is no drafting.**

**Sources.** No new source is needed. S4's 146 lb comes from the published breakdown that Step 4 already cites.
