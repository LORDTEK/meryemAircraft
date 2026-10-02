# Reader onboarding — for a reader starting a new conversation

> **Version check.** Rewritten in Round 169 for four new conversations, and brought up to date in Round 209, when all four readers started
> new conversations again; §6 is rewritten every round (Round 223: the paper is submitted). Older copies (Round 61, Round 91–101) describe a paper of 26 000 words in nine sections with a recomposition
> method; **that is no longer the state of the work.** In the repository, `grep -c "brought up to date in Round 209" cfd/reader-onboarding.md`
> prints **more than 0** for this version.

> **Why you are reading this.** You are one of four independent readers (Grok, ChatGPT, DeepSeek, Qwen) of a paper in
> development. Claude, the fifth voice, runs the rounds, checks every claim against the text and the sources, applies what
> is agreed, and gives its own view **in the same table as yours, as one column among five**. The author reads everyone's
> positions and decides. **Claude is not the author.** The work has run for about 210 rounds; this file tells you what the
> paper is and claims, which rules govern changes to it, what the author has decided, which errors recur, and where the work
> stands.
>
> **It makes no claim of its own.** Every number in it is quoted from the section it names. If this file and the paper
> disagree, the paper wins. Please tell us if they do.
>
> **You receive this file together with the reader packet and the current round text.** The reader packet
> (`paper/submission/reader-packet.md`, in parts where a file cannot be attached) is the whole current body and the journal supplement
> drafted so far. Read this file first, then the packet, then answer the round text. The round
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

**The audit archive (`paper/v8/supplement.md`) names sections by step number.** Its *"Section 10"* is 6.1, and so on. **The journal
supplement** (`paper/submission/supplement-src.md`, in the packet) uses the assembled section numbers and keeps the archive's S labels
(S2, S3, … S14) while it is drafted; the submission renumbers them S1–S11.

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
shorter*, and *perhaps 6.1 and 6.2 merge*. **That pass closed in Round 171; a calculation pass followed in Round 172, a framework pass in Rounds 173–174, 5.1 in Round 175 and Section 1 in Round 176.** The last whole reading closed in Round 191. **The work is now in the submission stage** (§6): the body is about 14 800 words in the assembled view, tables included, and is not being shortened (the author, E25 and E32); the journal supplement is being composed.

**Length.** The author has set word targets aside (Round 161). **Do not argue from 12 000, 8 500 or 7 500;** those were earlier
targets.

**Who decides.** A change is applied when **all four readers and Claude agree**, or when **the author decides**. One objection means
it is not applied; it goes back with its reasons. **The applied result is shown word for word and confirmed by everyone before it
closes.** Readers answer one another, not only Claude.

**The rules that govern every proposal:**

1. **Protected sentences.** *"A sentence is protected when removing it silently would change a claim, a limit or a derivation that
   later text depends on …"* There are **145 in the body and 31 in the supplement** (and 14 unprotected by the author's decision E18, still in the body), in the register `paper/v8-caveats.md`. A protected
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

**Round 224. The paper is submitted:** *Journal of Aircraft*, Manuscript ID **2026-10-C039418**, 2 October 2026, Full Paper. The submitted text
cannot change; anything found from here on is recorded for the revision stage. DeepSeek's window filled during Round 222; DeepSeek starts a new
conversation with this file, the reader packet (regenerated in Round 223) and the Round 223 text. Files are not re-sent each round; each round
text carries what it asks you to judge and ends by naming what goes to the author.

| Block | State |
|---|---|
| Closed | the shortening (E21); the pass over Section 1 (Rounds 185–187, E22); **the last part–whole–part reading (Rounds 188–191, E23): repairs D1, D2 (E24), row 0; no defect remains** |
| **Now: submission to *Journal of Aircraft*** | the author (E25, E26): **Full-Length Paper**, LaTeX, submitted at the present length (~16 000 with table equivalents; 10 000–12 000 recommended). Requirements, verbatim and item by item: `paper/joa-compliance.md` (16 September) and `paper/joa-requirements.md` (30 September) |
| Decided (E27) | title *meryemAircraft: Tail-Sitting Blended-Wing Body for Vertical Takeoff Without Propulsor Reorientation*; abstract as in `paper/submission/title-abstract.md` (199 words) |
| Decided (E28) | Section 1.5: the crewed-motor-glider clause is dropped (no original source); the reference list is renumbered (26 entries) |
| Closed (Round 195) | E28 confirmed; [13] Merical (abstract), [6] (no DOI); E1: the generator names NeuralFoil 0.3.3 and AeroSandbox 4.2.10 at 4.7; [9] pages 6268–6278 printed in the PDF |
| Closed (Round 196) | [11] Vegh: cite SciTech 2025-1436 with its correction notice (the journal item exists; its text is unread); [9] pages 6268–6278 |
| Closed (Round 197) | [15] Mathur: cite arXiv v1 under its own title, the quotation unchanged (all five, position d) |
| Closed (Round 198) | the reference list (26 entries, all fields cross-checked; [15] is arXiv v1, the only version); 2.1 *"generally"* applied (awaiting confirmation); the v7 AI statement read against the v8 facts (all five agree) |
| Decided (E30) | submit directly with full disclosure (no inquiry to the office); the authors used AI tools as a tool for the calculations; the disclosure is **one sentence**. 2.1 *"generally"* confirmed by all four |
| Decided (E31) | the AI-use sentence, in the Acknowledgments only, with *"and solution approach"* |
| Decided (E32) | stay with the *Journal of Aircraft* (SJR 2025 Q2, recorded); no shortening (E25 stands); at least one figure (Fig. 1: the aircraft standing on its tail); AIAA's official `new-aiaa.cls` now used (33 pages) |
| Decided (E33) | format-only changes (punctuation, American spelling, italics) allowed in protected sentences in the submission output, provided no attachment moves; A02 approved. Closed (Round 202): Fig. 1, Table 6 caption, [2, 3], [6] kept, most of the style pass |
| Closed (Round 203) | A11, A12, D50 applied; the supplement method agreed; no pointer removed |
| Closed (Round 204) | D33 comma form and D55 *"all of which"* (both Grok's) applied; the journal supplement renumbered S1–S11; ChatGPT's rule adopted (*"A supplement passage may clarify or expose working already underlying the body pointer, but may not introduce a new substantive claim that the body itself does not make or promise."*); P01–P07 R1; S-64, S-65 accepted |
| Decided (E34) | the protected S4 sentence reads *"the isolation test of Section 2.3"* |
| Closed (Round 205) | S5, S6, S8 receipts P09, P11, P12, P13 R1; S-66 is a defect (the body's fairing *"less than … in any case"* fails at a slope of 3.0 per radian); C1 (a): the NACA qualification goes into S8 |
| Closed (Round 206) | S-66 repaired in the body (Section 5.2: *"39 mm at an assumed lateral lift-curve slope of 4.0 per radian … 31 to 52 mm, within or below the 50 to 70 mm assumed for a 20 mm faired strut"*); P14 on the old sentence R4; the S8 NACA qualification text accepted |
| **Reader packet** | `paper/submission/reader-packet.md` (generated by `paper/build/reader_packet.py`): the current body and the journal supplement draft in one file. **A reader opening a new conversation gets this file together with this onboarding text and the current round text** |
| Closed (Round 207) | S-66 repair confirmed; *"within or below"* kept; S8 qualification text kept as drafted (*"side force only"*; Qwen to confirm); Qwen answered the author's question (nothing missing now; window fine) |
| Closed (Round 208) | all four answered the author's question (nothing missing; Grok and DeepSeek: a fresh conversation would help before S11–S14); S2–S8 whole-body check passed by all four; S10: P17, P18 R1, archive corrections accepted, gain sweep kept as a new sensitivity run; S-67 is a defect (P16 R4 until repaired); S8 ending kept |
| **Reader packet, how it is used** | not attached every round (the author cannot attach it to every reader); used at checkpoints (S2–S10 done; next: the completed supplement) and for a fresh conversation, in ~6 000-word parts (`paper/submission/reader-packet-partN.md`) where a file cannot be attached. Between checkpoints each round text carries the body section it asks about in full |
| Closed (Round 209) | S-67 repaired with ChatGPT's wording (all five): *"Take-off mass sets the cruise power, cruise power the engine rating, engine rating the propulsion mass, and propulsion mass the take-off mass; the take-off mass is found by iteration as the fixed point of that loop (Supplement S10)."*; P14 R1; the gain-sweep number stays in S10 |
| Closed (Round 210) | S-67 result confirmed (P16 R1); S11 P15, P19, P20, P21 R1; S11's reordering, archive correction and omitted counts accepted |
| Closed (Round 211) | S12: P24, P25 R1; its arithmetic, named candidates and omitted transition powers accepted |
| Closed (Round 212) | P22: the body adds *"The sizing loop computes no hover-rated mass for the electrical path."* after the protected Bill 3 sentence (all five); S12's rotation-time subsection kept with its figures (all five); S13 P26–P30 R1 |
| Closed (Round 213) | P22 R1; S14 P08, P10, P23, P31–P34 R1; **all 34 pointers R1** (receipt table `paper/submission/receipt-table.md`) |
| Done (Round 214) | renumbering S2–S14 → S1–S11 in both generators; `paper/build/supplement_build.py` (supplement PDF, 14 pages; checks: 30 protected supplement rows, every pointer's section, self-test) |
| Closed (Round 214) | final whole-body check: the three repairs carried everywhere, the claims hold on the four axes, nothing stops a first reading (all four) |
| Closed (Round 215) | B1: S13's tilting sentence carries the bound's frame (all five, b); B2: the fifth sensitivity row stays (Qwen preferred a label clause); f_energy / f_fuel parked |
| Closed (Round 216) | B1's result confirmed by all four; Qwen withdrew (c) on B2; no pre-submission defect remains. **The package is with the author for the submission decision** |
| Round 217 | the author is submitting on ScholarOne; Steps 1–4 complete (type, title, abstract; the two PDFs and the LaTeX source; subject index; the three authors). **Step 5 needs at least three suggested reviewers; the author asked for consensus of all five** |
| Round 218 | the five answers on suggested reviewers side by side (the author: Claude does not comment this round; everyone comments on everyone's); B2 (not the authors of [10], [11]) and B3 (no non-preferred reviewer, no editor preference) were the same in all five answers |
| Round 219 | the second exchange on suggested reviewers, side by side, without comment from Claude (the author); German on all four readers' lists; open: whether authors cited elsewhere in the paper (De Wagter [2], Panagiotou [21]) stay on the list |
| Closed (Round 220) | suggested reviewers, all five: German (Georgia Tech), Zingg (UTIAS), Laskaridis (Cranfield), Li (PolyU); no author cited in Sec. I.D ([2], [3], [10], [11]); no non-preferred reviewer, no editor preference |
| Round 221 | the cover letter for ScholarOne Step 6 (`paper/submission/cover-letter.md`): one draft, every predicate sourced |
| Round 222 | cover letter second pass (differences: 2b wording, MDPI mention, Qwen's closing sentence); the two AI-use explanations and the figure gap in the Acknowledgments |
| **SUBMITTED** | *Journal of Aircraft*, Manuscript ID **2026-10-C039418**, 2 October 2026 (Full Paper). The cover letter and the two AI-use texts were used as agreed (E37); the Acknowledgments name the code that renders Figure 1 (E36). Open after submission: confirm E36; the Figure 1 fact for ChatGPT (the script was written by Claude); DeepSeek in a new window |
| Closed (Round 223) | all five confirmed what was sent: the Acknowledgments sentence (E36), the cover letter (E37), the two AI-use texts; ChatGPT withdrew its Round 222 objection once the "I" was identified as Claude |
| **Now (Round 224)** | what to prepare while the paper is under review: five positions side by side (snapshot, a ledger of parked items, a review-comment classification, no answers before reviews exist) |
| **How the journal supplement is composed** (Rounds 203–208) | only what the 34 body pointers (P01–P34) promise; each passage taken from the latest archive snapshot, brought up to the current body and checked against the code and sources, with a provenance note; protected supplement rows carried verbatim; ChatGPT's rule (Round 204); each pointer's receipt graded R1 faithful / R2 differently qualified / R3 no content / R4 the body says more than the supplement establishes. Done: S2–S6, S8, S10, S11 (P22 open); S12, S13; S14 drafted (Round 213). All 34 pointers have a passage |
| Done in the submission stage | numbered references (26); the generator `paper/build/submission_build.py` (LaTeX, AIAA class, Roman-numeral sections, *Sec.*, American spelling, no dashes); Fig. 1; the Acknowledgments AI-use sentence |
| Still to do | the supplement generator (LaTeX, S1–S11); the receipt table for all 34 pointers; the final whole-body check with the completed supplement |
| Protected sentences | 145 in the body, 31 in the supplement; U table 14 |

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
- **Word targets set aside** (Round 161); **the shortening is closed and the paper is submitted at its present length** (E21, E25, E32).
- **Target: *Journal of Aircraft*, Full-Length Paper, LaTeX with the AIAA class** (E25, E26, E32), with at least one figure (Fig. 1).
- **2.1.6's "Where is our foundation?"** is about the inside of that subsection, not the order of the paper (Round 168).
- **Rule (iii)**, and S moves decided **as one list**.
- **The journal body carries no "in a previous version…" narrative.**
- **AI use is declared without brand, model or company names**, in one sentence in the Acknowledgments (E30, E31). The concept, architecture,
  design and solution approach are the authors'; AI tools were a tool (E29).
- **Source research is the readers' work** (Round 195): bibliographic fields, DOIs, pages and versions are cross-checked among the four of
  you; when all four agree, it is accepted. A request to the author for a file always carries a link the four have agreed on (Round 201).

---

## 9. How to answer

- **Begin with your name alone on the first line. Reply in English.**
- **Be blunt; encouragement is not wanted.** Quote the sentence and name the section for every point.
- **Vote item by item.** If you object, name the **current** sentence you object to and why.
- **Answer the other readers' positions and Claude's**, favourable or not. Claude's view is one column among five; criticise it as you would any other.
- **Keep it professional** (the author, Round 205): disagree with the reading, name the sentence and the reason; do not characterise the reader.
- **Sources:** give a downloadable PDF link only for novelty claims, numbers from tables, or verbatim quotations. **Say which
  document you opened in this conversation.** If you could not open it, give no number from it.
- **Do not guess the sign of a calculation. Do not propose new claims.**
- **Every round text ends with an open call for your own proposals.**

---

## 10. Verifying the text you have

Each round text names the repository (`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`) and the commit. You do not need the
repository to answer; that line is there so that a stale copy can be recognised.
