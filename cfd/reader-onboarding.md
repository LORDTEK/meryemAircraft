# Reader onboarding — for a reader starting a new conversation

> **Version check.** Rewritten in Round 169 for four new conversations. Older copies (Round 61, Round 91–101) describe a paper of
> 26 000 words in nine sections with a recomposition method; **that is no longer the state of the work.** In the repository,
> `grep -c "Rewritten in Round 169" cfd/reader-onboarding.md` prints **more than 0** for this version.

> **Why you are reading this.** You are one of four independent readers (Grok, ChatGPT, DeepSeek, Qwen) of a paper in
> development. Claude, the fifth voice, runs the rounds, checks every claim against the text and the sources, applies what
> is agreed, and gives its own view **in the same table as yours, as one column among five**. The author reads everyone's
> positions and decides. **Claude is not the author.** The work has run for about 170 rounds; this file tells you what the
> paper is and claims, which rules govern changes to it, what the author has decided, which errors recur, and where the work
> stands.
>
> **It makes no claim of its own.** Every number in it is quoted from the section it names. If this file and the paper
> disagree, the paper wins. Please tell us if they do.
>
> **You receive this file together with the current round text.** Read this file first, then answer the round text. The round
> text quotes in full every text you are asked to judge. The repository is only for verification: the assembled paper is
> `paper/v8/ASSEMBLED.md`, and its source is the step files `paper/v8/NN-*.md`.

---

## 1. What the paper is

**A design study of an uncrewed aircraft**, written for the *Journal of Aircraft* (AIAA). The aircraft is a **tail-sitting
blended-wing-body (BWB) series-hybrid vertical-take-off-and-landing** configuration. It stands on its tail, takes off and lands
vertically, and then rotates the whole airframe through about ninety degrees to fly on its wing. It is aimed at **wildfire
observation and response** and **cargo delivery to places without a runway**.

**What it is made of** (Section 5.2):

- **A blended wing body.** One lifting surface; no separate fuselage or tail.
- **One coaxial contra-rotating nose pair** of fixed-pitch propellers, 1.20 m in diameter on the 50 kg reference design. It
  produces **all propulsive thrust in both regimes**, in one orientation relative to the body.
- **Four small coaxial pairs, 0.20 m, at the ends of rigid frames projecting from the wing tips.** They give pitch and yaw by
  differential thrust, and they supply the take-off margin. **In cruise they free-wheel at zero shaft torque** (the author's
  decision) and give no cruise thrust; they are not drag-free.
- **A strip on the lower surface**, deployable in two halves: one half alone for roll, both together as a speed brake. It is the
  only moving aerodynamic surface. **Roll does not come from the propellers.** The reaction-torque channel of the coaxial pairs
  could give it; this configuration **declines** that channel by design, and what declining it costs is **not computed**.
- **A series-hybrid power path:** fuel → engine → generator → electric machines. The engine is sized by cruise; a **battery
  buffer** supplies the hover peak.

**Axis names.** The paper fixes body-axis naming. The propeller axis is the roll axis in both regimes; it stands vertical in hover
(a moment about it is a change of heading) and horizontal in cruise (a bank). The two conventions are never mixed.

**Three aircraft appear in the paper; keep them apart:**

| Name in the text | What it is | Where |
|---|---|---|
| **The 50 kg reference design** | The design the inventory describes. The transition figures are its own: 2 s rotation; in the finite-moment dynamic model with zero aerodynamic moment, 5.4 to 6.6 m altitude loss | 5.2, 6.1 |
| **The four closures, A–D** | The same configuration re-closed at four combinations of drag bracket and blade family: 52.3 to 57.5 kg, 13 kg payload | 6.1 |
| **The 1 000 kg reference design** | Used only to test how the charges behave with scale. No closure was run at 1 000 kg | 6.3 |

---

## 2. What the paper claims: four axes, four opponents

| Axis | Opponent | Standing |
|---|---|---|
| **Cruise efficiency** | Rotorcraft: multirotors **and helicopters** (the author's decision) | **Claimed against multirotors, and bounded:** effective L/D 5.56 to 7.39 here, against 4.9 for a published turboshaft quadrotor and 5.8 for an all-electric one (Section 4). **Against helicopters the result is mixed** (5.4 to 7.2 in the same NASA table); no advantage is claimed there. |
| **Operation without a runway** | Fixed-wing aircraft | **Claimed as sized, not demonstrated.** It depends on an energy store whose required performance the sources consulted do not report as built (Section 7). |
| **The mechanism required to change regime** | Tilting architectures | **The contribution.** |
| **Range** | The other hybrids (lift-plus-cruise, tilting) | **Not claimed, in either direction.** The ordering belongs to the sizing contract (6.4). |

**There is one contribution: the architecture.** It is *"arranged to change regime by rotating the airframe rather than its
propulsors"*. It carries none of five mechanism classes (5.1): a pivot or tilting joint; a nacelle or rotor-group actuator; a
variable-pitch hub; dedicated lift rotors; a rotor stowing, indexing or stopping mechanism. **The fifth is absent only while the tip
pairs free-wheel or are held by motor torque; a brake or lock would add it.**

**It is a count of mechanism classes.** It is not a claim that nothing moves (the strip moves), and not a claim of simplicity or
reliability (neither was measured). **"Arranged to", not "changes": the transition is not shown.**

**The paper's own statement of what it offers** (Section 8): *"a configuration sized to combine runway-independent vertical operation
with wing-borne cruise efficiency, arranged to do so with no mechanism that reorients a propulsor, and an account of what the
combination costs."*

**Sentences that are never written:**

- "the range of a fixed-wing aircraft", or any range comparison with fixed-wing aircraft;
- any comparison with rotorcraft on vertical capability;
- a range claim against lift-plus-cruise or tilting aircraft;
- "no moving parts", "no control surfaces", "simpler", "more reliable";
- "the aircraft changes regime";
- "first", "only", "not done before". These appear only as "not found", with the place searched named. Uncrewed tail-sitters,
  tail-sitters without control surfaces, coaxial tail-sitters and BWB tail-sitters are all in the literature (Section 1).

---

## 3. The framework: the instrument that makes the claim checkable

**The framework is not a second contribution.** It is how the architecture claim is made checkable.

**The three charges ("bills")** (2.1). The root is a **duty-cycle mismatch**: hardware needed for about two percent of a flight
is carried for the rest.

| Charge | What it is |
|---|---|
| **Bill 1** | the mass of a dedicated lift subsystem |
| **Bill 2** | the cruise drag of hover hardware left exposed |
| **Bill 3** | continuous power installed to a hover peak |

**A charge and its currency are not the same thing.** The currencies are kilograms, drag counts and installed kilowatts. A remedy's
own cost can fall in a currency without being a charge (a tilt pivot's mass is *"kilograms, not Bill 1"*). **Remedies move cost; they
do not remove it.** The refutation test (2.1): a counter-example reduces one charge, leaves the other two no worse (judged against the
architecture the move modifies), and has an own cost that is absent or demonstrably smaller, in the same currency. Costs outside the
three are listed, not waved away.

**The escape condition** (2.2) is **a definition, stated before any configuration**: same hardware, both duties, one orientation,
hover peak from a store. It permits six costs and has four failure modes; the fourth is **partial instantiation**. **This
configuration is a partial instantiation:** the nose pair meets all four parts; the tip pairs are carried through cruise producing
moments, so they re-open Bill 2.

**The rest:**

- **Independent check** (2.3): a NASA sizing set of five VTOL families, nine designs, one mission. Its test is the **isolation pair**
  (turbo-electric lift-plus-cruise against turbo-electric tilt-wing). **2.3 is the home of this data set.**
- **Closure** (6.1) and **ledger** (6.2): the loop closes on a declared package at four corners; the ledger attributes the three
  charges inside it, with no scalar total.
- **Scale** (6.3): the rotor term of Bill 2 falls to 0.29–0.65 of its light value while Bill 3 is held nearly flat by the sizing rule,
  so **at least two charges are not locked together**, within this model.
- **Contracts** (6.4): **against this configuration, the lift-plus-cruise layout is 55 to 84 percent ahead under a fixed fuel
  fraction, 28 to 54 percent under a fixed fuel mass, and between 13 percent short and 7 percent ahead under a fixed take-off mass.**
  The sign changes inside the envelope; the tilting competitor is only a bound.
- **What does not close** (7): the energy store. The take-off demand is 3.7 to 4.1 times the highest measured figure (a bench
  average of about 1.5 kW per kilogram). A NASA-funded design study argues that a pack with the required specific power *may be
  possible*; that is its conclusion, not a built pack. Eighteen further questions are listed in Supplement S14.

---

## 4. The paper's structure, and the two numberings

The source is **fifteen step files**; Step 9 has been merged into Step 15 and retired. The **assembled view**
(`paper/v8/ASSEMBLED.md`, produced by a script) arranges them into **eight sections**. **Readers must use the section numbers.**
Using step numbers as section numbers is a recurring error (§7).

| Step | Section | Title |
|---:|---|---|
| 1 | 1 | The gap |
| 2 | 2.1 | The tax |
| 3 | 2.2 | The escape condition |
| 4 | 2.3 | An independent quantitative check |
| 5 | 3 | The first half: operation without a runway |
| 6 | 4 | The second half: cruise carried on a wing |
| 7 | 5.1 | The combination |
| 8 | 5.2 | What it is made of, and what still moves |
| 10 | 6.1 | Analytical closure of the sizing loop |
| 11 | 6.2 | The ledger |
| 12 | 6.3 | Scale |
| 13 | 6.4 | Rankings belong to contracts |
| 14 | 7 | What does not close |
| 15 | 8 | Four axes, and where the paper stops (the conclusion) |

**The supplement names sections by step number.** Its *"Section 10"* is 6.1, and so on.

**The author's subsection numbering (Round 168).** Subsections are numbered in order. Where a section opens with text before its
first subheading, that text is .1. So 2.1.6 is *"The charges are coupled"*, 5.2.6 is *"What meets the ground"*, and 7.2 is *"First,
the known obstacle: the energy store"*.

**The author's outline of the argument:** *introduction · the current state · one problem's solution · the other's · **combining the
solutions** · the soundness of the product · the calculations · conclusion.* (Claude's translation) The author has also floated, as a thought and not a
decision, a four-heading telling: *Current state · Proposed solution · Calculations · Conclusion* (Round 169; Claude's translation).

---

## 5. How changes are made now

**The stage.** The paper went through deletion (Rounds 61–72), recomposition (73–98), recomposition into result sentences (101–151,
25 797 → 18 634 words) and compression by finding (from Round 153). **Sentence-level cutting is exhausted** (Round 167). The author
then read the whole paper and wrote notes on about thirty subsections (Round 168): *narrow this*, *merge this*, *2.3 at least 100 words
shorter*, and *perhaps 6.1 and 6.2 merge*. **That pass closed in Round 171; a calculation pass followed in Round 172 and a framework pass in Rounds 173–174** (§6). The body is **13 762 words of prose** (tables excluded).

**Length.** The author has set word targets aside (Round 161). **Do not argue from 12 000, 8 500 or 7 500;** those were earlier
targets.

**Who decides.** A change is applied when **all four readers and Claude agree**, or when **the author decides**. One objection means
it is not applied; it goes back with its reasons. **The applied result is shown word for word and confirmed by everyone before it
closes.** Readers answer one another, not only Claude.

**The rules that govern every proposal:**

1. **Protected sentences.** *"A sentence is protected when removing it silently would change a claim, a limit or a derivation that
   later text depends on …"* There are **161 in the body and 28 in the supplement**, in the register `paper/v8-caveats.md`. A protected
   sentence is kept **verbatim**. **It cannot be reworded.** If you think one should be, ask the author.
2. **Rule (iii) (the author, Round 104).** *"A protected sentence may move to the supplement only together with the result it
   qualifies, and only by the author's decision."* The author decides these **as one list** (Round 168).
3. **The four operations on a protected sentence:** **K** keep verbatim · **S** supplement, with its result (rule (iii)) · **C** cut as a
   copy, **naming the other body sentence that already says it** · **M** move to another body section.
4. **The brake.** *"Move the working, not the evidence; move the derivation, not the qualification; move the audit trail, not the
   result."* A qualifier travels with the result it qualifies, or neither moves.
5. **The Round 104 test.** *"… a calculation may not move if the surviving body sentence would cease to tell the reader what was
   actually found."* A sentence that explains the physical mechanism behind a body result is an interpretive prerequisite, not a
   source of words.
6. **The isolation pair (Round 113).** When an external comparison tests a prediction, the body keeps the compared objects, their
   common basis, and *"it is not a controlled experiment"*.
7. **One home per external data set.** The NASA set's identity, selection and population live in 2.3; other sections use its
   findings.
8. **Occupied before the gap.** What the literature already holds is stated in the body, before the gap (Section 1).
9. **The receipt check.** Every pointer must deliver what it promises. **When a section changes, every sentence pointing into it is
   re-read**, including pointers into supplement sections.
10. **Counting words.** When a list gains or loses an item, every nearby count (*"three reasons"*, *"the third route"*) is re-read.
11. **Quotation lock.** Quotation marks only on verbatim text.
12. **Readability (the author, Round 150).** *"This is not a legal text. Once it cannot be understood, being right loses its
    importance."* (Claude's translation) Ask of every candidate: would a person understand this in one reading?
13. **Nothing new.** A shortening adds no new claim and **no new number**.

**Frozen snapshots in the supplement are an audit archive, not the journal supplement.** Do not quote them as the current text.

---

## 6. Where the work stands — *updated every round*

**Round 174.** All four readers work in new conversations since Round 169; this was done **for equality** (Grok's conversation did not need
renewing). **The author (Round 171):** *"You readers, work together. Whenever it comes to my turn, don't forget to tell me."* Each round
text ends by naming what goes to the author.

| Block | State |
|---|---|
| Closed | the author's subsection notes (Rounds 168–171); Section 6 calculation pass (Round 172); Section 2 pass (Round 173); the 2.3 pound figures stay in the body (all five) |
| Author's decisions | E13–E16 as above; **"Finish Section 2"**; **E17** a, 2.2.5 *"An architecture may meet the condition where it carries the aircraft …"* cut as a copy of item 4 |
| **Parked by the author, not now** | protected-sentence status (a part–whole–part later); tables and figures; 2.3 with the section merging; Section 1 later |
| **Open (Round 174)** | confirm or veto the Section 2 completion; R7, R8; receipt of E17; the next place (proposals: Grok 5.1, DeepSeek 1.4 or 7.2) |
| Protected sentences | 161 in the body, 28 in the supplement |
| Body | 13 762 words of prose (tables excluded) |

**Tools the round texts mention:**

| Tool | What it checks |
|---|---|
| `v8_caveats.py` | the protected sentences are where the register says |
| `v8_nothing_lost.py` | every sentence of a shortened step is in a body or the supplement, or is a voted replacement |
| `v8_draft_check.py` | a draft derives from its source by deletion only; no negative or qualifier deleted |
| `v8_assemble.py` | the assembled view; section references resolve |
| `v8_refs.py`, `v8_stale.py`, `v8_count_flag.py`, `v8_figures.py` | table references; retired phrases; counting words; figure numbers |

---

## 7. Errors that recur — look for these first

1. **Step numbers used as section numbers** (*"Section 4"* meaning 2.3). Use §4's table.
2. **Old targets and old instructions from memory**: 12 000, 8 500, 7 500 words; the author's early position of no shortening until confident (Round 61,
   reversed in Round 72).
3. **Getting protection wrong.** Marking an unprotected sentence as protected, or missing that a sentence is protected. Check the
   register; the round text lists the protected sentences you are asked to mark.
4. **Rewording a protected sentence** while calling it compression.
5. **A shortening that adds a number or a claim** the section did not carry.
6. **A correction that creates a new contradiction** in another section, or **does not travel** to every place the phrase appears.
7. **A pointer left behind when text moves.**
8. **Selective quotation of a source.** The source's own qualification or contrary conclusion is quoted or recorded as omitted (S-18:
   the retraction's speed gain; S-20: the store study's *"may be possible"*).
9. **Charge/currency conflation:** calling kilograms "Bill 1".
10. **A number from one aircraft attributed to another** (§1), and mixed power stations (rotor shaft, engine shaft, electrical bus).
11. **Treating Claude as the author.** The drafts, checks and objections are Claude's; the decisions are the author's.
12. **Over-claiming while summarising**, including in this file.

---

## 8. Decisions already made — please do not reopen them

These are the author's decisions. You may point out a consequence the author may not have seen, but please do not argue the decision
itself.

- **One contribution: the architecture** (Round 35). The framework is the instrument; contract dependence is a finding, not a second thesis.
- **Helicopters are rivals on the cruise axis** (Round 97); the result against them is written as mixed.
- **Tip pairs free-wheel at zero shaft torque in cruise** (Rounds 130–131).
- **"Arranged to change regime."** Roll comes from the strip; the reaction-torque channel is declined.
- **Word targets set aside** (Round 161); shortening continues by merges and cuts.
- **2.3 is to be at least 100 words shorter** (Round 168). The open question is which 100.
- **2.1.6's "Where is our foundation?"** is about the inside of that subsection, not the order of the paper (Round 168).
- **Rule (iii)**, and S moves decided **as one list**.
- **The journal body carries no "in a previous version…" narrative.**
- **AI use is declared without brand, model or company names.**

---

## 9. How to answer

- **Begin with your name alone on the first line. Reply in English.**
- **Be blunt; encouragement is not wanted.** Quote the sentence and name the section for every point.
- **Vote item by item.** If you object, name the **current** sentence you object to and why.
- **Answer the other readers' positions and Claude's**, favourable or not. Claude's view is one column among five; criticise it as you would any other.
- **Sources:** give a downloadable PDF link only for novelty claims, numbers from tables, or verbatim quotations. **Say which
  document you opened in this conversation.** If you could not open it, give no number from it.
- **Do not guess the sign of a calculation. Do not propose new claims.**
- **Every round text ends with an open call for your own proposals.**

---

## 10. Verifying the text you have

Each round text names the repository (`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`) and the commit. You do not need the
repository to answer; that line is there so that a stale copy can be recognised.
