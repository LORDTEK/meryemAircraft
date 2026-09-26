# Round 96 — The three divided points in Steps 1 and 5 are resolved and applied. Step 6 applied in part: two agreed changes caught before they broke a pointer. An error of my own in S-20. Step 7 inventory — the heart

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`64c4590`**.
>
> New in the repository: `paper/v8/drafts/07-inventory.md`. Everything you are asked to vote on is quoted below.

---

## 1. Confirmed and closed

All four of you confirmed Round 95's applied text:
- 1B's new order;
- the S-20 narrowing (163);
- S-24 and S-25;
- the 5D "not computed" protection (164);
- the count rule;
- the P56 check.

**Qwen confirmed the current 1D wording**, so that item is closed.

**The wider count rule is adopted** (all five): adding, removing, splitting or combining an item in a counted list means
re-reading every nearby count and every sentence that enumerates the list.

---

## 2. Applied — all four of you and I agreed. Please confirm the text

**Step 1**
- **1B** now ends: *"…Different nations, services and propulsion philosophies have attacked the same problem for seventy
  years."* Removed: *"No field sustains that level of effort against a need that is not real."*
- **1C** now opens: *"Hybrid VTOL aircraft occupy that corner today. **This paper does not dispute that they work.**"*
  Removed: *"…, and several are in service."*

**Step 5**
- **5C:** *"…The present arrangement takes **the weight benefit** and extends it…"*
- **5D:** the signpost is removed; DeepSeek withdrew its objection. The section's sized/not-demonstrated part now opens with
  *"**Sized.** The vertical phase is sized: …"*.
- **5D, the inherited item, now protected (165):**
  > ***And one historical difficulty is inherited rather than removed.*** *A tail-sitting aircraft on the ground is more
  > prone than a conventional one to tip over, in crosswind and on uneven ground. The stance base is the answer this
  > configuration offers, and it is a parameter rather than a proof.*

  DeepSeek's vote to protect quoted the earlier wording ("more exposed to crosswind and to uneven ground"). DeepSeek also
  accepted 3.1, so I have protected the sentence as it now stands. DeepSeek, please confirm.

**Step 6**
- **6A** now reads: *"…the comparison runs one way only. **Nothing here is claimed against fixed-wing aircraft.** The claim
  is confined to the one thing the multirotor family structurally lacks: **a surface that carries the cruise lift.**"*
- **6B** now reads: *"…a site that supplies nothing. **A multirotor meets that requirement completely.**"* The next
  paragraph opens *"What it does not meet…"*.
- **6G** now ends: *"…is the reason the margin above sits where it does rather than higher. Section 11 charges all
  three."* The 7.47–9.20 stays in 6D only.
- **6E heading (S-26):** *"Five qualifications: three run against this configuration, one has no computed direction, and
  one bounds what the comparison can be called"*.

**Rules and records**
- **Scope-of-witness check** (ChatGPT) and **source-conclusion flag** (DeepSeek) are adopted.
  - The evidence file now has a table: for each source opened, what the body takes, what the source's own conclusion
    says, and the relation (supports / qualifies / softens / contradicts / not stated, ChatGPT's values).
  - Barrett is marked *softens*; De Wagter, the NASA 1984 review and Table 3 are marked *qualifies*; the V-22 is marked
    *out of scope*.
- Grok P57 and P58 and Qwen P1 are recorded.
- Qwen P2: all nine Table 3 values are in the evidence file.

The originals are frozen in Supplements S1, S5 and S6 (new). Five more retired phrases, 101 in all, including *"every one
of them runs against this configuration"* (Grok P59). Steps 6 and 1 are in the nothing-lost check.
- All checks pass; 165 protected.
- Word counts: Step 1 is now 1 648 (from 1 679), Step 5 is 1 235 (from 1 213; S-24 added words), Step 6 is 2 138 (from
  2 206), and the body is 25 810.

---

## 3. Two agreed changes I did not apply — each would have broken a pointer

**R-4 — S-27, the helicopters.** All five of us accepted the disclosure. I inserted it where I had proposed, after the
quadrotor table and its two paragraphs. The pointer check (`v8_refs.py`) then failed on *"**The same table** gives the
study's two helicopter types…"*: the nearest table is **this paper's comparison table**, not the NASA study's Table 3. I
removed the insertion. The fault is mine; I wrote the wording and chose the place.

Repair, to vote, using the paper's own name for the NASA study (*"The sizing set contains two quadrotors…"*), with ChatGPT's
*"at"*:
> *"**The same sizing set** gives its two helicopter types at 5.4 to 7.2; the all-electric side-by-side helicopter, which
> has no wing either, reaches the upper part of this configuration's envelope. The claim here is against the multirotor,
> and it is not extended to the helicopter."*

Placement: after the paragraph on the all-electric quadrotor, before *"So the second claim is narrower…"*.

**R-5 — the weak 6D removal.** All five of us agreed to remove *"These are the bounding combinations permitted by two
independent model inputs."* I read the next sentence first (P51). After the removal, the bullet would read:
> *"**Examined envelope, 5.56 to 7.39.** **They are not four demonstrated aircraft states**, and nothing here shows…"*

"They" would then point at a bold label.

Repair, to vote: remove the sentence **and** change *"They are not…"* to *"**The four corners are not** demonstrated aircraft
states"*.

---

## 4. My error — R-6, in the S-20 sentence you confirmed

The S-20 sentence says:
> *"…the study's hover lasts twenty seconds or less, and **how long this aircraft's vertical phases draw the peak is not
> computed here.**"*

Step 2 (assembled Section 2.1) says:
> *"For a mission of one hour, a take-off, a transition, a return transition and a landing occupy **on the order of a
> minute**."*

I wrote a "not computed" statement without searching for a section that says otherwise. That is exactly the error CLAUDE's
rule §0.2 is written against. Section 2 gives an order of magnitude, not a computation of this aircraft's peak duration, so
the sentence is not false word for word. But a reader who has seen "about a minute" in Section 2 and then reads "not
computed" in Section 8 sees a contradiction. The comparison the sentence is there to enable, Barrett's 20 s against ours,
is also left unmade.

Repair, to vote (the protected part of the sentence is unchanged):
> *"…the study's hover lasts twenty seconds or less; **this aircraft's vertical phases occupy about a minute in all
> (Section 2), and how long each draws the peak is not computed here.**"*

---

## 5. Still divided — please answer one another

**S-28, the quadrotor disc loadings.**

| | Position |
|---|---|
| Grok | give both loadings; keep the protected *"The quadrotor is a good quadrotor."* singular, as the class |
| DeepSeek | accept the plural sentence, and make the protected sentence plural too |
| Qwen | same as DeepSeek |
| ChatGPT | do not apply; use *"The study calls the turboshaft quadrotor 'a good quadrotor' and gives it a disc loading of 3.5 lb ft⁻²; the all-electric quadrotor is at 3 lb ft⁻²."* |

**A factual point on ChatGPT's wording.** The NASA study does not call anything "a good quadrotor". I searched the PDF: the
phrase is **this paper's**, not the source's. So that wording would attribute to the source a judgment the source does not
make — the kind of error §2.1 of our rules is written against.

ChatGPT's other point stands: *"unusually efficient"* is a stronger inference than a disc loading alone supports. The
current text already says it of the 3.5.

**My proposal**, which tries to meet all four positions:
> *"**The quadrotor is a good quadrotor.** Its disc loading is 3.5 lb ft⁻², and the all-electric one's is 3; both are
> unusually low. Nothing here is compared against a poor example."*

This keeps the protected sentence singular, as the class (Grok). It gives both loadings (DeepSeek, Qwen). It attributes
nothing to the source and drops *"unusually efficient"* (ChatGPT).

**The 1B heading — my own check after the removal.** The heading still reads *"The demand has been continuous for seventy
years"*. ChatGPT's argument, that effort is evidence of pursuit rather than of need, applies to the heading as much as to
the removed sentence. Proposal: *"### The problem has been attacked for seventy years"*. Does anyone think the heading is
fine as it stands?

---

## 6. New proposals, to vote

| # | Proposal | Who | My vote |
|---|---|---|---|
| a | Protect the S-27 sentence once applied | DeepSeek | yes — like S-19 and S-20, it stops the section from looking more certain than its table |
| b | **Table-completeness check.** When a source table is opened in full and used to bound a comparison, every entry that could bear on the claim is accounted for, if only to record why it is omitted. | ChatGPT | yes — S-27 is its case |
| c | Grok P60 and Qwen P1: in the Step 6 trace, 6C's *"Lift is carried on a surface or it is carried on rotors"* is linked to S-27, so it cannot be read as "rotors cannot reach this envelope" | Grok, Qwen | yes |

---

## 7. Step 7 inventory — the combination — please confirm or correct

Step 7 (assembled Section 5.1) is the step the author named as a step in its own right: *the combining of the solutions*.
It is 1 269 words, with 10 protected sentences. **The soul rule applies at full force here.** Every candidate below is a
restatement of text that has a first home earlier. None touches a protected sentence, the move (7E) or the count (7F).

| Block | Must say | Candidate |
|---|---|---|
| **7A** None is new | *"None of the three elements is new."* … *"Each can be found on its own, and in combination, in the literature and in hardware — Section 1 says where."* | The three sentences between them restate Step 1G almost word for word. **Step 1's inventory deferred this cut to Step 7.** → **remove the three middle sentences** |
| **7B** Contribution | P *"What this paper contributes is that combination, …"*; P *"The assembly is not offered as novel because it is an assembly."* | — |
| **7C** Partial | P *"The qualification in that sentence is not decoration"*; P *"The instantiation is therefore partial."* | — (Step 3 names partial instantiation in general; this is its first application to this aircraft, and *"made here rather than conceded later"* is the placement job) |
| **7D** What each element supplies | BWB → wing-borne cruise; stance → one propulsor, one orientation; buffer → engine sized by cruise | — |
| **7E** The move | P *"The configuration is arranged to change regime by rotating the airframe. …"* — the soul sentence | — |
| **7F** The count | P *"That single move is what removes the need for the mechanism."*; the five-class table; the strip named | — |
| **7G** Attitude | Differential thrust; tip pairs sized by moment, supplying the take-off margin; a dependency, not a lift system | *"That is the one place the configuration asks a component to do a second job it was not sized for"* is Step 5D's sentence **verbatim** → **remove**. P51 reading: the next clause becomes *"It is a dependency, it is reported as one where the sizing is audited, and it does not make the tip pairs a dedicated lift system"*, and *"It"* takes the previous sentence (the tip-pair thrust also supplying the take-off margin) as antecedent. It resolves, but only with a capital *"It"*, and that is a change you are voting on |
| **7H** Boundary | P *"This is not a configuration in which nothing moves."*; roll not from thrust, possible from reaction torque, declined; the strip, modulated, pitches nose-down | — (the home Step 1D points to). Note: *"no combination of thrust settings produces a moment about that axis"* is a variant of the P56 phrase; it is qualified in the next sentence, but the P56 check does not see variants |
| **7I** Fixed-pitch price | A price of refusing the variable-pitch hub, charged in Section 11 | — (it ties the price to the table's hub row) |
| **7J** Not simplicity | P *"Nor is this a claim of mechanical simplicity."*; the actuator inventory is the motors plus the strip | — |
| **7K** Transition | P ×2: not settled; the mechanism claim survives, the transition claim is not made | — |
| **7L** Costs | *"The combination carries costs: the attitude rotors that make the union controllable are themselves exposed in cruise, and Section 11 charges them."* | The **third** statement of that cost (7C, Step 5F, Step 3's first failure mode) → **remove**. The section would then end on *"The transition claim is not made."* Is that the right last line for the heart of the paper? |

**One source finding (S), to vote.**
- **S-29 (7A and Step 1G).** *"Series-hybrid propulsion has established precedent in small uncrewed aircraft"* has no source,
  in the body or in the repository. Step 1's audit points to Step 7 and Step 7 points to Section 1.
  - If 7A's middle sentences go, the claim survives only in 1G, still unsourced.
  - The BWB claim ("three decades") is attributed: the BWB paper in the repository cites Liebeck 1998 and 2004.
  - **Can any of you give a downloadable source for series-hybrid propulsion in small uncrewed aircraft?** If none turns
    up, 1G's clause is softened or removed.

---

## 8. What I am asking

1. Confirm §2's text. DeepSeek: confirm the 5D protection in its current wording.
2. §3: vote on the R-4 and R-5 repairs.
3. §4: vote on the R-6 repair.
4. §5: answer one another on S-28 and my proposal, and on the 1B heading.
5. §6 (a) to (c).
6. §7: confirm or correct the Step 7 inventory.
   - Vote on removing the 7A middle sentences, 7G's verbatim sentence (with the capital "It"), and 7L.
   - Answer the last-line question.
   - Give a source for S-29 if you have one.
7. Your own proposals, of any kind, with reasons.

Step 8 is the last block.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
