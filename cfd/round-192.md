# Round 192 — Submission stage: the title and the abstract

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you need is in this text.

---

## A. Where we are

**The last reading closed in Round 191.** All five of us confirmed the three repairs. C1 and C2 were K. No defect remains.

**The submission stage has opened.** The target is *Journal of Aircraft*. The author's decisions (my translation):
- **Full-Length Paper** (peer-reviewed), not Design Forum.
- **LaTeX.**
- **Submit at the present length.** The guideline recommends 10,000–12,000 words including table equivalents; we are at about 16,000. The editor may ask for shortening.
- The authors are three independent researchers in Ankara, Türkiye. There is no funding.

**What the paper does not have yet:**
- a title and an abstract (this round);
- a numbered reference list;
- the style conversion: Roman-numeral sections, *"Sec."*, numbered tables and equations, lists as 1) 2), American spelling, no bold emphasis, no dashes;
- an acknowledgments section, which carries the AI-use statement.

The requirement-by-requirement record is in `paper/joa-requirements.md` and `paper/joa-compliance.md`.

**One style finding touches our own D1 repair.** AIAA style says *"Avoid using dashes in scholarly writing. Pairs of dashes can be replaced with commas or parentheses."* The submission version of 4.1 will therefore read *"the rotorcraft (multirotor and helicopter alike)"*. The dashes go in the style conversion, with the other dashes; each change that could alter meaning comes to you for confirmation.

---

## B. The journal's rules, verbatim

**Title** (AIAA author pages):
- *"no more than 12 words"*;
- *"avoid technical jargon and acronyms and abbreviations"*;
- *"Don't begin a title with an article (The, A, An)"*;
- *"avoid expressions such as preliminary or exploratory"*;
- *"long titles with multiple prepositional phrases are distracting"*;
- *"How would I search for this piece of information?"*;
- *"A colon also is preferable to a dash in the paper title"*.

**Abstract** (AIAA author pages and the journal's own text, `joa-compliance.md` §4):
- *"100 to 200 (maximum) words in one paragraph, without numerical references, acronyms, or abbreviations"*;
- *"intelligible and complete in itself … it should not cite figures, tables, or sections of the paper"*;
- *"written using third person"*;
- *"Keywords and significant findings should be incorporated into the first two sentences"*;
- *"The title … should not be repeated or paraphrased in the first sentence of the abstract"*;
- *"state the objectives of the investigation"*;
- *"describe the treatment by one or more such terms as brief, exhaustive, theoretical, experimental"*;
- *"indicate newly observed facts and the conclusions"*;
- *"contain new numerical data presented in the paper if space permits"*.

**Consequences for us:**
- No *"VTOL"*, *"BWB"*, *"L/De"* or *"RANS"* in either. Spell them out, or describe them.
- Unit abbreviations are safest avoided in the abstract too. Say *"kilograms"*, or give ratios and percentages.
- **The aircraft's name.** `joa-compliance.md` records that *meryemAircraft* stays in the title as the author's decision. The body never uses the name. I am asking the author to confirm. **Please give one title candidate with the name and one without.**

---

## C. What the paper licenses: every statement you may use, with the body sentence that carries it

Use only these. A title or abstract sentence that cannot be traced to one of them is a new predicate and fails.

| # | Statement | Body (section, sentence) |
|---|---|---|
| L1 | The contribution is the architecture: regime change by rotating the airframe, not the propulsors, so no mechanism reorients a propulsor | 1.5 (protected): *"The contribution is the architecture: a configuration arranged to change regime by rotating the airframe rather than its propulsors, and so carrying no mechanism that reorients a propulsor."* |
| L2 | The configuration: a tail-sitting blended-wing body; every propulsor a coaxial, torque-balanced pair; a buffered series hybrid; one moving aerodynamic device | 1.5: *"a blended-wing-body tail-sitter in which every propulsor is a coaxial, torque-balanced pair … carrying no aerodynamic control surfaces beyond a single moving device, powered through a buffered series hybrid"* |
| L3 | Pitch and yaw from differential thrust of the tip pairs; roll from a strip; the reaction-torque channel is declined by choice | 5.2: *"Pitch and yaw come from differential thrust between the tip pairs"*; *"Roll comes from neither, and the reason is a choice rather than an impossibility."* |
| L4 | None of the elements is new; what is not established is the combination with its price | 1.5 (protected, both) |
| L5 | An accounting of three charges (carried hover mass, exposed cruise drag, hover-sized continuous power) and an escape condition stated before any configuration | 2.1, 2.2 (*"stated here before any configuration is offered"*) |
| L6 | The accounting's prediction holds on an independent NASA sizing study, on the pair closest to isolating the charge, which is not a controlled experiment | 2.3 (protected: *"it is not a controlled experiment"*) |
| L7 | The instantiation is partial: the nose pair meets the condition, the four tip pairs do not; tip hardware is 57 to 69 percent of zero-lift drag | 5.1 (protected: *"The instantiation is therefore partial"*); 6.2 |
| L8 | Effective lift-to-drag ratio 5.56 to 7.39 against two published quadrotors at 4.9 (ahead at every corner) and 5.8 (from 4 percent behind to 27 percent ahead); mixed against helicopters | 4.4, 4.5; 8.2 (protected: *"Claimed against multirotors, and bounded; against helicopters … mixed and no advantage is claimed"*) |
| L9 | The sizing loop closes analytically at four corners, 52.3 to 57.5 kg with 13 kg payload; this establishes arithmetic self-consistency, not that the package exists | 6.1: *"It does not establish that the package exists."* |
| L10 | Against lift-plus-cruise, the ranking belongs to the sizing contract: 55 to 84 percent behind under a fixed fuel fraction, and from 13 percent ahead to 7 percent behind under a fixed take-off mass. The shift is always toward the lighter aircraft, and this configuration is 27 to 30 percent lighter | 6.4 |
| L11 | No range claim against the tilting family; the tilting layout is a bound | 6.4 (protected in 8: *"No range claim is made against the tilting or lift-plus-cruise families in either direction."*) |
| L12 | The required energy-store performance is not demonstrated by the sources consulted: the buffer must deliver 4.7 to 5.2 kilowatts per kilogram to hover | 7 (protected: *"for the first item the answer is no"*) |
| L13 | The transition is not settled; a finite-moment model with zero aerodynamic moment loses 5.4 to 6.6 m | 6.1; 5.1 (protected: *"The transition claim is not made."*) |
| L14 | The claim is a count of mechanism classes, not mechanical simplicity, not that nothing moves | 5.1, 8.6 (protected) |
| L15 | The treatment is analytical and computational: no wind tunnel, no aircraft built | 4.7 (*"No part of this has been measured"*); 8.5 item 8 (protected) |
| L16 | The applications: wildfire observation and response; cargo to places without a runway | 1.1 |

**Check L10 against the text before using it.** The body reports the lift-plus-cruise layout's lead: *"55 to 84 percent ahead under the first contract … between 13 percent short and 7 percent ahead under the third"*. In L10 I restated it from this configuration's side ("behind" and "ahead"). **If you use it, restate it from the body's side**, as the lift-plus-cruise layout's lead, so the sign cannot flip.

---

## D. What neither may say (§0; each of these has been written once and retracted)

- **Range against fixed-wing aircraft.** The runway claim is against fixed-wing only; the range claim is against rotorcraft only.
- **Vertical capability against rotorcraft.**
- **Superiority, or range, against the other hybrids.** Tilting and lift-plus-cruise are opponents only on the mechanism axis.
- *"mechanically simpler"*, *"no moving parts"*, *"nothing moves"*, *"no control surfaces"* (there is one moving device).
- *"flies"*, *"demonstrated"*, *"validated"*, or *"feasible"* for the aircraft.
- *"first"*, *"novel"*, *"new"* or *"unique"* for the configuration. Priority is only *"not established"*, and the elements are not new.
- *"roll cannot be produced by coaxial pairs"*. It can, by reaction torque; the configuration declines it.
- **Any number not in C**, or a number without its model or state (L9, L12, L13).
- **The old *Drones* title**, for comparison only: *"The Architectural Cost of Hybrid VTOL: meryemAircraft, a Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System"*. It has 16 words and an acronym. **The old abstract is not reused.** Its numbers and two of its claims were retired in v8.

**The single-contribution rule** (Round 35): the abstract leads with the architecture. The accounting is the instrument that makes it checkable. The contract dependence is stated as a finding, not as a second thesis.

---

## E. What I ask of you

| # | Item |
|---|---|
| a | **Two title candidates**, one with *meryemAircraft* and one without. Each at most 12 words, no acronym, not starting with an article. Give the word count |
| b | **One abstract**, 100–200 words, one paragraph. After it, give for **each sentence** the L-numbers from §C that license it. Give the word count |
| c | **Your reasons**, briefly: what you put in the first two sentences and why, and what you left out for space |
| d | **Your own proposals** (open) |

As always with a new question, my candidates come next round, beside yours. The title is the author's final decision.

---

## F. Errors (one list)

- **Claude, twice on the same day, outside the rounds:**
  - I told the author the journal's length guideline had never been read, and asked for it. It had been in the repository since Round 154.
  - I then called the journal's supplementary-material and preprint policies "open questions". They had been recorded verbatim on 16 September.
  - Both are now in the record, and there is a new rule for me: read the two journal files and search `references/` before saying anything about the journal.
- **None found in the readers' Round 191 answers.**
