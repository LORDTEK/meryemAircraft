# Reader onboarding — for a reader starting a new conversation

> **Version check (Qwen P1, Round 92; corrected in Round 93).** This version was rewritten in Round 91 and last updated in
> Round 96. An older copy (Round 61, sent in Round 64) stated Step 13's contract results **in the reverse direction**: it
> gave this configuration's range as 55 to 84 percent ahead of the lift-plus-cruise layout. **The older copy has no
> version box at all; if yours does not begin with this box, it is the old one: do not use it.** In the repository:
> `grep -c "Version check (Qwen P1" cfd/reader-onboarding.md` prints **more than 0** for this version and **0** for the old one.
> (The Round 92 check searched for the old phrase itself and so found it in its own quotation: it printed 2 on this file,
> not 0. My error; the positive check above replaces it.)

> **Why you are reading this.** You are one of four independent readers (ChatGPT, Grok, DeepSeek, Qwen) of a paper in
> development. The work has run for about ninety rounds. If your previous conversation filled up, this file puts you back
> where the others are: what the paper is and claims, how the text is now being worked, what has been settled, which
> errors recur, and how to answer. **It makes no claim of its own. Every number in it is quoted from the step it names,
> and if this file and a step disagree, the step wins. Please tell us if they do.**
>
> **You will receive this file together with the current round text.** Read this file first, then answer the round text.
> If you can open the repository, the whole current paper is `paper/v8/ASSEMBLED.md` (about 26 000 words), and each of the
> fifteen source steps is `paper/v8/NN-*.md`.
>
> *This file is kept current: the **"Where the work stands"** section (§6) is rewritten every round.*

---

## 1. What the paper is

**A design study of an uncrewed aircraft**, written for the *Journal of Aircraft* (AIAA). The aircraft is a
**tail-sitting blended-wing-body (BWB) series-hybrid vertical-take-off-and-landing** configuration. It stands on its tail,
takes off and lands vertically, and then rotates the whole airframe through about ninety degrees to fly on its wing. It is
aimed at **wildfire observation and response** and **cargo delivery to places without a runway**.

**What it is made of** (Step 8):

- **A blended wing body.** It has one lifting surface and no separate fuselage or tail.
- **One coaxial contra-rotating nose pair** of fixed-pitch propellers, 1.20 m in diameter on the 50 kg reference design.
  It produces **all propulsive thrust in both regimes**, in one orientation relative to the body.
- **Four small counter-rotating pairs, 0.20 m, at the ends of rigid frames projecting from the wing tips.**
  - In hover they give pitch and yaw by differential thrust, and they supply the take-off margin.
  - In cruise they are carried, producing moments rather than cruise thrust.
- **A strip on the lower surface**, deployable in two halves. One half alone gives roll; both together act as a speed
  brake. **Roll does not come from the propellers**: the reaction-torque channel of the coaxial pairs is **declined** as a
  design choice, and its cost is **not computed**.
- **A series-hybrid power path:** fuel → engine → generator → electric machines. The engine is sized by cruise, and a
  **battery buffer** supplies the hover peak.

**Three aircraft appear in the paper; keep them apart:**

| Name in the text | What it is | Where |
|---|---|---|
| **The 50 kg reference design** | The design the inventory describes. The transition results (2 s rotation, 5.4 m altitude loss) are its own. | Steps 8, 10, 12 |
| **The four closures, A–D** | The same configuration, re-closed at four combinations of drag bracket and blade family. They weigh 52.3 to 57.5 kg. | Step 10 |
| **The 1 000 kg reference design** | Used only to test how the charges behave with scale. No closure was run at 1 000 kg. | Step 12 |

---

## 2. What the paper claims: four axes, four opponents

| Axis | Opponent | Standing |
|---|---|---|
| **Cruise efficiency** | Rotorcraft: multirotors **and helicopters** (the author's decision, Round 97) | **Claimed against multirotors, and bounded:** 5.56 to 7.39 here, against 4.9 for a published turboshaft quadrotor and 5.8 for an all-electric one (Step 6). **Against helicopters the result is mixed:** the same NASA table gives 5.4 to 7.2; ahead of the turboshaft single-main-rotor helicopter at every corner, and only the top corner ahead of the all-electric side-by-side helicopter (7.2). No superiority is claimed there. |
| **Operation without a runway** | Fixed-wing aircraft | **Claimed as sized, not demonstrated.** It depends on an energy store whose required performance the sources consulted do not report as built (Step 14). |
| **The mechanism required to change regime** | Tilting architectures | **The contribution.** |
| **Range** | The other hybrids (lift-plus-cruise, tilting) | **Not claimed, in either direction.** The ordering belongs to the sizing contract (Step 13). |

**There is one contribution: the architecture.** It is *"arranged to change regime by rotating the airframe rather than
its propulsors"*. It carries none of five mechanism classes (Step 7):

- a pivot or tilting joint;
- a nacelle or rotor-group actuator;
- a variable-pitch hub;
- dedicated lift rotors;
- a rotor stowing, indexing or stopping mechanism.

**It is a count of mechanism classes.** It is not a claim that nothing moves, since the strip moves, and not a claim of
simplicity or reliability, which were not measured. **"Arranged to", not "changes": the transition is not shown.**

**The paper's own statement of what it offers** (Steps 9 and 15): *"a configuration sized to combine runway-independent
vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism that reorients a propulsor, and
an account of what the combination costs."*

**Sentences that are never written:**

- "the range of a fixed-wing aircraft", or any range comparison with fixed-wing aircraft;
- any comparison with multirotors on vertical capability;
- a range claim against lift-plus-cruise or tilting aircraft;
- "no moving parts", "no control surfaces", "simpler";
- "the aircraft changes regime";
- "there is no general architectural superiority claim";
- "first", "only", "not done before". These appear only as "not found", with the place searched named. Uncrewed
  tail-sitters, tail-sitters without control surfaces, coaxial tail-sitters and BWB tail-sitters are all in the
  literature (Step 1).

---

## 3. The framework, which is the instrument that makes the claim checkable

**The framework is not a second contribution.**

**The three charges ("bills")** (Step 2). The root of all three is a **duty-cycle mismatch**: hardware needed for about two
percent of a flight is carried for the rest.

| Charge | What it is |
|---|---|
| **Bill 1** | the mass of a dedicated lift subsystem |
| **Bill 2** | the cruise drag of hover hardware left exposed |
| **Bill 3** | continuous power installed to a hover peak |

**Charge and currency are not the same thing** (settled over Rounds 77–80). The currencies are kilograms, drag counts and
installed kilowatts. A remedy's own cost can fall in a currency without being a charge. For example, a tilt pivot's mass is
*"kilograms, not Bill 1"*. The table in Step 2 names bills by number and every other cost in words.

**Remedies move cost; they do not remove it.** The Step 2E heading reads *"remedies move cost, among the three charges or
outside them"*. The word *transfer* has two senses:

- **"A transfer between charges"** is narrow: one charge is reduced and another made worse.
- **"The accounting claims transfer"** is broad: cost is moved, possibly out of the three charges.

**The refutation test** (Step 2F). A counter-example reduces one charge, leaves the other two no worse, and has an own cost
that is either absent or demonstrably smaller than the reduction, in the same currency.

- *"No worse"* is judged against **the architecture the move modifies**.
- A cost outside the three does not refute the accounting, **but it is listed, not waved away**.
- **The tilting row** falls on one of two branches, depending on how the modified architecture supplies its hover peak:
  - either it is a transfer between charges;
  - or what keeps it from refuting the accounting is the part of its cost that falls outside the three.

**The escape condition** (Step 3) is **a definition, stated before any configuration**. It is derived by inverting the
table. It has four parts: **same hardware, both duties, one orientation, hover peak from a store**. It names six permitted
costs and four failure modes, the fourth being **partial instantiation**. **This configuration is a partial
instantiation**: the nose pair meets all four parts, and the tip pairs are carried through cruise producing moments, so they
re-open Bill 2.

**The rest of the framework:**

- **Independent check** (Step 4): a NASA sizing set of five VTOL families.
- **Ledger** (Step 11): the price of the closures attributed to the three charges, with no scalar total.
- **Scale** (Step 12): the rotor term of Bill 2 falls to 0.29–0.65 of its light value while Bill 3 is held nearly flat by
  the sizing rule, so **at least two charges are not locked together.**
- **Contracts** (Step 13). **Against this configuration, the lift-plus-cruise layout is 55 to 84 percent ahead under a fixed
  fuel fraction, 28 to 54 percent under a fixed fuel mass, and between 13 percent short and 7 percent ahead under a fixed
  take-off mass.** The sign changes inside the envelope, and the tilting competitor is only a bound.
  *(The earlier onboarding text of Round 61 stated these figures with the direction reversed. The figures above are
  quoted from Step 13.)*
- **What does not close** (Step 14): the energy store. The take-off demand is 3.7 to 4.1 times the bench rate derived from a measured 10.68C bench discharge of the unit pack of a battery flown in a 210 kg-class eVTOL aircraft (about 1.5 kW/kg, model-derived from the source's current, voltage and pack mass), and 1.8 to 2.0 times the 3 kW/kg a NASA-funded design study cites from the literature (attributed, not measured by that study). The same study argues that, with pulse current limits, a pack with the required specific power *may be possible* with existing technology; its hover lasts 20 s or less, and this aircraft's peak duration is not computed. That is an attributed conclusion, not a built pack.

---

## 4. The paper, step by step, and the assembled numbering

The source is **fifteen step files**. The **assembled view** (`paper/v8/ASSEMBLED.md`, produced by a script) arranges them
into nine sections:

| Step | Title | Section in the assembled view |
|---:|---|---|
| 1 | The gap | 1 |
| 2 | The tax | 2.1 |
| 3 | The escape condition | 2.2 |
| 4 | An independent quantitative check | 2.3 |
| 5 | The first half: operation without a runway | 3 |
| 6 | The second half: cruise carried on a wing | 4 |
| 7 | **The combination** | 5.1 |
| 8 | What it is made of, and what still moves | 5.2 (and 6.1) |
| 9 | What is not claimed | 6.2 |
| 10–13 | Closure, ledger, scale, contracts | 7.1–7.4 |
| 14 | What does not close | 8 |
| 15 | Four axes, and where the paper stops | 9 |

The author's outline: *introduction · the current state · one problem's solution · the other's · **combining the solutions**
· the soundness of the product · the calculations · conclusion.*

---

## 5. How the text is being worked now: recomposition

The body is about **26 000 words**, and the journal's working target is **about 7 500**. The author's rules are these:

- **Shortening is not pruning, and no word budget drives it.**
- **The insight is carried by placement, order and voice**, never by a stronger sentence.
- **Cuts come from everywhere**, but the calculations are cut first.

**The method (agreed in Rounds 73–76), applied one block at a time:**

1. **A semantic inventory**, confirmed by the readers first. It records what must be said, the evidence, the
   qualifications, what must *not* be said, where each item is stated first, and its outbound dependencies.
2. **A frozen snapshot** of the source block. When the block changes, the original goes to the supplement, whole, with a
   note that sits outside the frozen text.
3. **A blind reading.** The readers reconstruct the block from the draft alone, *before* they see the trace.
4. **A trace table.** Every sentence is tagged **P** (protected, verbatim), **D** (deletion only), **J** (joining sentence;
   states no fact) or **R** (rewrite; each R sentence can be vetoed on its own). The table also records any qualification
   or epistemic status that was lost, and the **origin** of every defect found: **S** (it was already in the source) or
   **R** (the recomposition introduced it).
5. **Votes.** A change is applied only if **all four readers and Claude** agree. **One objection means it is not applied**;
   it goes back with the reasons. **The applied result is shown word for word and confirmed by everyone before it
   closes.**

**Rules that are now standing:**

- **Restatement.** A statement kept in two places is cut in the second, unless the second occurrence has a job the
  inventory names. A draft that keeps neither is a halt.
- **Protection.** *"A sentence is protected when removing it silently would change a claim, a limit or a derivation that
  later text depends on … Being load-bearing for the structure alone is not enough."* There are currently 160 protected
  sentences.
- **The stop rule** counts only defects that the *draft* introduces or fails to repair. Defects found in the *source* are
  repaired under their own trace and recorded in `paper/v8-source-defects.md`. So far there are seventeen of origin S (one,
  S-19, still being voted) and two of origin R (R-1, R-2), both caught before they were applied.
- **Content before drafting.** When the inventory finds a content problem, the problem is settled first and the draft
  waits (S-1, S-5, S-15/S-16).
- **Every empirical claim carries an evidence status:** verified / attributed but unverified / model-derived / unsupported
  (`paper/v8-evidence.md`, with PDF page locators).
- **Readers answer one another**, not only Claude. When one reader is not persuaded, the others are asked to respond.
- **A veto must cite the "now" text, not the "proposed" text.** Tables in the round text show both.

---

## 6. Where the work stands — *updated every round*

**Round 96.**

| Block | State |
|---|---|
| Step 4 | recomposed and closed (1 586 → 1 356) |
| Step 3 | recomposed and closed (1 874 → 1 698) |
| Step 2 | recomposed, with its last pieces awaiting confirmation. It went **2 263 → 2 487**, because content repairs added more than recomposition removed. |
| Step 9 | recomposed and closed (1 388 → 1 339) |
| Step 14 | recomposed and confirmed. One repair of my own to vote (R-6: the S-20 sentence says the vertical-phase duration is not computed, but Section 2 gives about a minute) |
| Step 1 | recomposed; *"No field sustains…"* and *"several are in service"* removed, awaiting confirmation. Open: the 1B heading ("The demand has been continuous…") |
| Step 5 | recomposed; signpost removed, tip-over sentence reworded and protected, awaiting confirmation |
| Step 6 | recomposed (6A, 6B, 6G removed; S-26 heading), awaiting confirmation. To vote: S-27 with a pointer repair (R-4), the 6D removal with a pointer repair (R-5); divided: S-28 |
| Step 7 | inventory sent (Round 96) — the combination, the heart of the paper |
| Next | Step 8, last |

**The body is about 25 770 words.** Recomposition gains a few percent per block. In Steps 2 and 3 its main product was
defects found in the source and repaired. The author will review the target when the steps are done.

**Tools the round texts mention:**

| Tool | What it checks |
|---|---|
| `v8_caveats.py` | the protected sentences |
| `v8_stale.py` | retired phrases; nearly 90 of them |
| `v8_nothing_lost.py` | every sentence of a recomposed step is in the body or the supplement, or is a voted replacement |
| `v8_refs.py` | table, row and relational-noun references, and supplement references |
| `v8_assemble.py` | the assembled view and section references |

**`links.py` checks the old v7 file**, not v8.

---

## 7. Errors that recur — look for these first

1. **A correction that creates a new contradiction** in another section.
2. **A correction that does not travel.** A phrase is retired in one step and survives in another (S-8, S-16 in Step 13).
3. **A reference left behind when text moves.** A table moves to the supplement and *"the table"* keeps pointing at it
   (S-7, S-11).
4. **Charge/currency conflation:** calling kilograms "Bill 1" (S-1, S-8, S-13).
5. **Selective quotation of a source.** S-18: the source's own conclusion, a speed advantage, was left out.
6. **An uncited number that survives by repetition.** S-14 went uncited from v5 to v8, and is deleted.
7. **Quoting the proposed text as the current text, or an old version as the current one.**
8. **A number from one aircraft attributed to another** (see §1), and mixed power stations (rotor shaft, engine shaft,
   electrical bus).
9. **Over-claiming while summarising**, including in this file.

---

## 8. Decisions already made — please do not reopen them

These are the author's decisions. You may point out a consequence the author may not have seen, but please do not argue
the decision itself.

- **One contribution: the architecture.** No range claim against the other hybrids.
- **"Arranged to change regime."** Roll comes from the strip; the reaction-torque channel is declined.
- **The frozen v7 and its public archive are not touched.**
- **The journal body carries no "in a previous version…" narrative.**
- **AI use is declared without brand, model or company names.**
- **The name "zero-bill condition" is dropped** (Round 86).

---

## 9. How to answer

- **Begin with your name alone on the first line. Reply in English.**
- **Be blunt; encouragement is not wanted.** Quote the sentence and name the step for every point.
- **Sources:** give a downloadable PDF link only for novelty claims, numbers from tables, or verbatim quotations. **Say which
  document you opened in this conversation.** If you could not open it, give no number.
- **Do not guess the sign of a calculation. Do not propose new claims.**
- **Vote item by item.** If you veto, say which **current** sentence you object to and why.
- **You may answer the other readers' positions**, favourable or not.
- **Every round text ends with an open call for your own proposals.**

---

## 10. Verifying the text you have

Each round text names the repository (`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`), the commit, and
usually a SHA-256 or a short `grep` check. You do not need the repository to answer; those are there so that a stale copy
can be recognised.
