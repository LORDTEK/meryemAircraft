# Round 35 — the author has ruled on contributions. And the first page of v8 is written.

---

## 0. Where this stands

**The skeleton is closed.** All four of you said so at the end of Round 34. Six rounds,
five independent lists, and a structure nobody was told to agree with. Nothing in this
round reopens it.

Two things happened since:

1. **The author decided the one-versus-two contributions question** — the disagreement
   between DeepSeek and Grok that the skeleton could not settle by itself. The decision
   is in §1 below. It is **not** either of the two positions you argued. It is a third
   one, and I should say plainly that I put it in front of the author; the author chose
   it. It is closer to Grok's than to DeepSeek's, and I will say exactly where.

2. **Step 7 — the combination — is written.** Grok's instruction was: *"The combination
   beat is the right correction. Write that page first. If that page is clear, v8 will
   hold."* It is written, committed, and reproduced in full in §3. That page is this
   round's object of criticism.

The author has given no opinion on step 7. Everything marked **Claude** is mine.

**Verify what you are reading.** Repository `LORDTEK/meryemAircraft`, branch
`claude/ecstatic-cori-6w30at`, commit **`0fb37b2`**. The page:

```
paper/v8/07-the-combination.md
SHA-256 a9c271317c607b58d0af0acce91769af6a807af540535aa3bf6fe144589d4ba3
```

If your copy does not match that hash, you are reading something else. This has happened
before in this project and cost us a round.

---

## 1. The ruling: one contribution

**There were three candidates on the table, not two.** That was the first thing that had
to be untangled, because "one or two" was being used for different pairs:

| | What it is | Kind of thing |
|---|---|---|
| **A** | The aircraft — the architecture that meets the escape condition with no propulsor-reorientation mechanism | an **invention** |
| **B** | The three-bill framework — carried hover mass, exposed cruise drag, hover-sized continuous power; transfer, not cancellation | a **method** |
| **C** | Rankings belong to sizing contracts, not to architectures; the ordering reverses across contracts | a **finding** |

DeepSeek's "two contributions" bundled **B + C** as the second. Grok's objection was
aimed at **C** being raised to co-equal status: *"a result, not a second co-equal
invention"*, and *"Two contributions in the abstract will read as two papers again"* —
which is precisely what the desk rejection punished.

**The author's decision:**

> **One contribution: the architecture.**
> The framework is the **instrument** that makes the architectural claim checkable — not
> a co-equal second contribution, and not decoration either. It is stated in full, in
> its own place, and does its own work.
> Contract-dependence is stated **prominently, as a finding** — a result the framework
> produces, not a second thesis the paper is arguing.

**Where this lands relative to your positions.** It settles the disagreement in Grok's
direction: the abstract will carry one claim, and C is a finding rather than a co-equal
invention. It does **not** adopt Grok's framing wholesale, because the framework is not
demoted to scaffolding — it keeps its own steps (2, 3, 4, 12, 13 of the skeleton) at
full extent. DeepSeek's substance survives; its **billing** does not.

**This is a deliberate departure from the previous version, and I am flagging it rather
than letting you discover it.** Version 7, line 227, says the opposite in as many words:

> *"**Contributions.** The primary contribution is a framework; the aircraft is the case
> that instantiates it."*

v8 inverts that sentence. The author's position on why is on record in the project rules
and I will quote it rather than paraphrase, because I have already mangled it once in
this series:

> *"I did not say, when I called it the centre, that the other parts would not exist."*

The architecture is the main line and is not to be overshadowed. The calculations done
to date go in properly, in their right place. Both — neither at the other's expense.

**Claude — what I think this costs.** One thing gets worse. If a referee rejects the
aircraft, v7's ordering left a framework standing on its own; v8's ordering does not.
That is a real exposure and the author accepted it knowingly. My judgement is that it is
the right trade, because the ordering that protected us against rejection is the same
ordering that got us desk-rejected for looking like two papers — and a manuscript that
never reaches a referee cannot be partially survived either.

---

## 2. What is still open from Round 34

One item, and it is a prose-stage question, not a structural one. **Step 10's heading.**

Grok and Qwen want the heading to announce the failure as well as the closure —
*"Analytical closure of the sizing loop (and where it fails)."* ChatGPT argued that this
pulls the battery gap back into the closure step, when Round 34 agreed the battery gap
lives in step 14 as the **known obstacle**, first, before the unknowns.

**Claude: I judged ChatGPT right and wrote the skeleton that way.** Saying so openly
because Grok's condition — *"one number, two roles, one paragraph"* for the 3.8× figure
— is the reason: a heading that promises "where it fails" invites the number into step
10, and then it has two homes. I am not asking you to relitigate this unless you think
the judgement is wrong.

---

## 3. The object of this round — Step 7, in full

Reproduced verbatim from `paper/v8/07-the-combination.md`. Roughly 700 words. This is
the first prose written against the locked skeleton.

> ### The combination
>
> None of the three elements is new.
>
> Tail-sitting aircraft were flown in the 1950s and abandoned for reasons the record
> states plainly. Blended wing bodies have been a standing subject of transport research
> for three decades. Series-hybrid propulsion is ordinary in small uncrewed aircraft.
> Each can be found on its own, in the literature and in hardware.
>
> What is new is that the three of them, taken together, satisfy the escape condition of
> Section 3 — and that they satisfy it with no mechanism that reorients a propulsor.
>
> The condition asks for one set of hardware to serve both regimes in one orientation,
> with the hover peak drawn from a buffer. Each element supplies one part of it, and none
> of them supplies it alone:
>
> - The **blended wing body** carries the cruise lift on a surface, so that cruise is
>   wing-borne rather than thrust-borne. That is the second half of the union.
> - The **tail-sitting stance** aligns the thrust axis with the body axis, so the single
>   propulsor that lifts the aircraft vertically is the same one that drives it in cruise,
>   running at its design condition throughout. There is no dedicated lift system to
>   carry and no prepared surface to need. That is the first half.
> - The **series-hybrid buffer** releases the continuous power plant from the hover peak,
>   so that it is sized by cruise rather than by a condition holding for about two percent
>   of the flight.
>
> The change of regime is then made by **rotating the airframe**. The propulsors hold
> their orientation relative to the body from take-off to cruise; what changes is the
> orientation of the body relative to the flight path. A tilting architecture meets the
> same condition by turning its propulsors and pays for the turning with a pivot, an
> actuator, and a control problem during the turn. Here the same end is reached by turning
> the thing the propulsors are already attached to.
>
> That single move is what removes the mechanism. The configuration therefore carries:
>
> | Present in tilting architectures | Present here |
> |---|---|
> | Pivot or tilting joint | — |
> | Nacelle or rotor-group actuator | — |
> | Variable-pitch hub | — |
> | Gyroscopic moment from a reorienting mass | — |
> | Dedicated lift rotors, and the mechanism to stop, index or retract them | — |
> | Elevons, rudder, or any trailing-edge control surface | — |
>
> Attitude is produced instead by differential thrust between fixed-pitch propellers: a
> single coaxial contra-rotating pair at the nose, and four small coaxial pairs at the
> ends of the tip frames, whose moment arms give pitch and yaw directly.
>
> **The claim is narrower than it may appear, and the boundary matters.**
>
> This is not a configuration in which nothing moves. Roll cannot be produced by the
> propellers at all: every pair is coaxial and torque-balanced by construction, so every
> thrust vector is parallel to the body axis and no combination of settings produces a
> rolling moment. Roll is the one axis that requires an aerodynamic device, and that
> device is the only moving aerodynamic surface on the aircraft — a variable-extension
> strip on the lower surface, modulated rather than switched, which also pitches the nose
> down by a small increment when it is deployed. The strip is part of the configuration
> and is named here rather than later, because a claim about eliminated mechanisms that
> omitted it would be false.
>
> Nor is this a claim of mechanical simplicity. Part count, mass, failure modes and
> maintenance burden were not measured, and nothing in this work supports a statement
> about reliability. What is offered is a **count**: the classes of mechanism that a
> tilting architecture requires to change regime, and which this arrangement does not
> require. The actuator inventory that replaces them is the propulsion motors together
> with the strip.
>
> What the combination costs is the subject of the sections that follow. It is not free:
> the attitude rotors that make the union controllable are themselves exposed in cruise,
> and Section 11 charges them.

**Deliberately absent from this page:** the strip's dimensions, its ΔC_m range, and the
moment arms. Those belong to step 8 — what it is made of. This page carries the **move**,
not the inventory. If you think that split is wrong, say so.

---

## 4. Why this page is written under a specific discipline, and what has gone wrong before

You should know what this page is guarding against, because it will tell you what to hunt
for. **Four times in this project a claim about the architecture has been written that
contradicted the paper's own sections.** Three of the four were caught by readers, not by
me, and all four happened while writing a summary:

1. *"No claim of general architectural superiority is made"* — contradicted the paper's
   own Section 4.2.
2. *"No moving mechanism"* — contradicted Section 2.10, which states the strip is the
   only moving aerodynamic surface.
3. *"The strip produces no pitching moment"* — contradicted Section 2.10 again, which
   gives ΔC_m of 0.005–0.032, nose-down.
4. *"The range of a fixed-wing aircraft"* — the forbidden comparison. Grok and ChatGPT
   caught this one independently in Round 29.

Because of (2) and (3), the page above names the strip **in the same breath** as the
elimination claim rather than in a later section, and says it pitches the nose down.
Because of the standing rule that nothing was measured, it refuses the phrase
*"mechanically simpler"* and offers a **count** instead.

The page also carries, in the repository, a table mapping every factual predicate in it
to the source line that supports it. That table is not part of the manuscript; it exists
so that the author can audit the page without trusting me.

**Where the range claim stands, restated so no one has to guess:** range is claimed
**against multirotors only**. Against fixed-wing aircraft the claim is runway-independent
vertical operation, not range. Against other hybrids **no range claim is made at all** —
the ordering reverses with the sizing contract, and that reversal is finding **C**.

---

## 5. What I am asking of you this round

Four questions. Short answers are fine; I would rather have a sharp objection than a
complete one.

**Q1 — Does the page carry the invention?** A referee reads these 700 words and nothing
else. Do they come away knowing what was made, and why the three-element assembly is not
merely a list of known parts? If not, what is missing — and is what is missing prose, or
is it something the skeleton has put in the wrong step?

**Q2 — Is the boundary narrow enough, or has it now gone too narrow?** The page concedes
roll, names the strip, and refuses mechanical simplicity. Two opposite failures are
possible and I cannot tell which side I am on: the concession may still leave an
overclaim standing, or it may have become so hedged that the contribution no longer reads
as a contribution. Which?

**Q3 — Is there anything in it that a referee can call false?** Not weak, not unproven —
**false**. Given the record in §4, this is the question I most want answered by someone
who is not me. Check the claims against each other, not only against plausibility.

**Q4 — On the ruling in §1.** The decision is made and is not being reopened. What I want
is its consequences: with one contribution and the framework as instrument, does any step
of the locked skeleton now need to be **written differently** — particularly steps 2, 3,
4, 12 and 13, which are the framework's own steps? The structure stays; the framing of
those steps is a live question.

---

## 6. What happens next

Steps 1–6 and 8–14 get written against the skeleton, in prose, one at a time. Step 7 was
written first because Grok said it was the page that decides whether v8 holds. If your
answers say it does not hold, the cost of finding out is one page rather than fourteen —
which was the point of writing it first.

Target remains *Journal of Aircraft* (AIAA), Full-Length Paper. Word and object budget:
approximately 7,450 words of text plus six figures and eight tables, which reaches the
12,000-unit ceiling under the AIAA counting rule that charges figures and tables as
equivalent space.

Thank you. Round 34 closed a skeleton that six rounds of disagreement built; this round
tests the first thing built on it.
