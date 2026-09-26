# Round 99 — Step 8 is applied, and the count in Step 7 now carries its one condition at the table. Every block has been through its inventory. What comes next is the author's decision, and your proposals for it are asked for

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> As before, answer one another as well as me. Where one of you proposes different wording, the others are asked whether
> it should replace the applied one.

---

## 1. Confirmed and closed

All four of you confirmed Round 98's applied text: the rotorcraft axis (P-a to P-h), 1G, 7G, protection 167, and the P56
variant check.

Two points closed with all five of us agreeing to leave the text as it is:
- **P-i:** no change. Grok and Qwen withdrew.
- **4.3:** the S-27 sentence stays as it is. Grok does not insist.

---

## 2. Applied — all four of you and I agreed. Please confirm the text

**Step 8**
- **8B (S-31, S-30):**
  > *"…so **the splitting gearbox and the mechanical governors that synchronise it are not required**. This work makes no
  > claim about the shafting…"*
  > *"…**the net angular momentum of the propulsion system is nominally zero**: rotating the airframe through ninety
  > degrees precesses **nominally** nothing, and no gyroscopic moment appears for the control system to cancel **unless the
  > pairs are speed-trimmed (below)**. In a tilting architecture that term is present and must be designed for."*
- **8C (S-32):** *"…the difference is supplied from a battery buffer for the vertical phase alone.** No wattage is quoted
  here; the closed powers are Section 10's."* The previous-version narrative is gone.
- **8E:** now reads *"The aircraft rests on five points: the four lower ends of the tip frames, and the aft end of a keel
  running along the centreline."* It goes straight on to the fairing and the flight control system.
  - Removed: *"It stands on its tail in its own storage attitude, with no launch equipment present."*
  - Removed: the whole *"The tip frames therefore do four jobs at once …"* paragraph.
- **8G (S-33):** the stopped-state paragraph now ends: *"…rather than as the state a particular installation would reach.
  **The free-wheeling state needs no stopping means; the stopped state does, and if it were a brake or a lock rather than
  motor holding torque, the count of Section 7 would gain a class.**"*

**Step 7**
- **The table (S-33).** The stopping row reads *"Rotor stowing, indexing or stopping mechanism | Architectures that remove
  dedicated lift rotors from the cruise flow by such means | — (see note)"*. Directly under the table:
  > ***Note.*** *The stopping class is absent if the tip pairs free-wheel in cruise or are held stopped by motor torque; a
  > brake or a mechanical lock would add it. The means of stopping is not fixed by this study (Section 8).*

  All four of you required the qualification at the table. The wording joins Qwen's footnote to Grok's motor-torque clause.
  ChatGPT asked for the row itself to read "absent in the free-wheeling state; conditional in the stopped state". I kept the
  cell short and put the condition in the note directly under it. **ChatGPT, does the note meet your requirement, or must
  the cell itself carry the condition?** The others: which do you prefer?
- **7D (4.2):** the series-hybrid bullet now ends *"…sized by cruise rather than by a condition holding for about two
  percent of the flight. **The series arrangement is used here for the electrical path it gives the buffered hover peak, not
  because this study assumes it is the more efficient hybrid architecture.**"*

**Protected (168):** the Step 9 axis row, *"Claimed against multirotors, and bounded; against helicopters the published
comparison is mixed and no advantage is claimed."*

**New project rule:** the opponent-family vocabulary lock (ChatGPT). Every "multirotor" is one of three kinds:
- a family-level statement, which becomes *rotorcraft*;
- a specific reference, which is kept;
- a source quotation, which is untouched.

**Onboarding.** The line *"It carries none of five mechanism classes"* now adds the S-33 condition.

The originals are frozen in Supplements S7 and S8 (new). Four more retired phrases, 115 in all. Step 8 is in the nothing-lost
check. All checks pass; 168 protected. The body is 25 797 words.

---

## 3. One wording point from ChatGPT — please answer one another

**S-30.** Grok, DeepSeek and Qwen accepted the wording now applied (*"precesses nominally nothing … unless the pairs are
speed-trimmed"*). ChatGPT accepted the substance but prefers:
> *"**At equal counter-rotating speeds**, the net angular momentum of the propulsion system is nominally zero: rotating the
> airframe through ninety degrees therefore produces no gyroscopic moment for the control system to cancel. **If the pairs
> are speed-trimmed, that cancellation is no longer exact (below).**"*

ChatGPT's reason is physical: *"precession is the motion of the angular-momentum vector"*. What the paper needs is whether a
**gyroscopic moment** appears when the airframe is rotated.

**My view: ChatGPT is right, and I vote to replace the applied wording with it.** "Precesses nothing" describes the wrong
thing. The sentence is about the moment the control system would have to cancel. Grok, DeepSeek, Qwen: will you accept the
replacement?

---

## 4. New proposals, to vote

| # | Proposal | Who | My vote |
|---|---|---|---|
| a | **Conditional-inventory rule.** If an item's presence in a hardware-class inventory depends on an unresolved operating state or implementation choice, it is not classed as categorically absent; the condition appears at the inventory's home and in every count that depends on it. | ChatGPT | yes — S-33 is its case |
| b | Grok P65: add the unqualified "no stopping mechanism" to the retired-phrase list, so a later pass cannot restore it | Grok | yes |
| c | Grok P66: 8D's *"the same system assigned to the rotation (not demonstrated)"* stays beside the assignment | Grok | yes — should that sentence be protected? |
| d | DeepSeek: a stopped-state flag in the Step 7 trace; a count/scope check on every list that names aircraft families | DeepSeek | yes |
| e | **Qwen P2: a global vocabulary audit** — one script across all steps for the pairs we fixed: *charge / currency*, *transfer* (narrow / broad), *rotorcraft / multirotor*, *mechanism / transition* | Qwen | yes, with a limit. A script can find the words but not always their sense. I propose it lists every occurrence with its step and the rule it falls under, for a human (and you) to read, rather than pass or fail on its own |

---

## 5. Where the work stands, and a question for you

**Every block has now been through its inventory.**

| | |
|---|---|
| Body at Round 69 | 26 852 words |
| Body now | 25 797 words |
| The target on record | about 7 500 words for the body (Round 67); the journal's full-paper range is 10 000 to 12 000 words |

Recomposition has not shortened the paper much. What it produced was repairs: source defects S-1 to S-33, and six defects of
its own (R-1 to R-6), each caught and fixed. The paper is more accurate than it was. It is not much shorter.

In Round 77 the author decided to finish the blocks first and then look at the target again. That point has come, and the
decision is the author's. **The author asked from the start for your ideas too.** Please give your view:
1. **Is 7 500 still the right target**, or is the journal's own range the target now?
2. **How would you get there** without cutting the account of the architecture? The author's standing direction is that if
   cuts are needed, they come first from the calculation parts outside the architecture's own account (Round 67).
3. **What would you cut first, and why?** Name steps or blocks.

I will put your answers side by side for the author, with my own view.

---

## 6. What I am asking

1. Confirm §2. ChatGPT: the Step 7 note.
2. §3: the S-30 replacement.
3. §4 (a) to (e).
4. §5: your view on the target and the path.
5. Your own proposals.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
