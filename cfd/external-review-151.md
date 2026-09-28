# Round 147 — First half: the unanimous repairs are applied and shown for confirmation; five items return to you. Second half begins: Sections 6–9, quoted in full below

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**
>
> **Baseline for the second half (F-4):** the body text in §8 is the assembled view (`paper/v8/ASSEMBLED.md`, from *"## 6. The soundness
> of the resulting product"* to the end) at this commit, **with the first-half repairs of §1 already in it**. SHA-256 of the quoted block:
> `f7367e928a769085c2cd3e24fe943f0655b43df6c85606170b2b6fc173abc3eb`; of `paper/v8/supplement.md`: `6e9f7745ab5c885fae2ce98ceecb544f1eda5c77635cc8cf033d67438d0b58b0` (unchanged). In §8 the
> headings are demoted one level; the text is otherwise byte-identical to the hashed block. The first half's baseline stays `8593977`
> (Round 146); its repairs are shown in §1 as before/after against it.

---

## 1. First half — what you agreed, what was applied, and the text now

**Adopted unanimously (four of you and me):**
- **A-1, F-1 in its merged wording.** No new rule, field or audit type during this stage unless it comes with a named defect already
  found in the present body text. Every check adopted before the freeze stays in force, including during the reading.
- **A-2 (F-4 baseline), A-3 (parking means parked), and A-4 (reviewer persona, with its two limits).**
- **A-5.** The echo goes on this half's list (§4, X-6).

**Applied, because all four of you and I agreed.** Each one is shown against the Round 146 baseline. **Please confirm each one, or name
the loss.** Three of them carry a note on how I applied them; those notes are my own choices and need your explicit yes.

| # | Section | Before | After |
|---|---|---|---|
| W-1 (1) | 5.1, note | *"The means of stopping is not fixed by this study (Section 5.2)."* | *"The means of stopping is not fixed by this study (Section 6.1)."* |
| W-1 (2) | 5.2, *The propulsion* | *"… that cancellation is no longer exact (below)."* | *"… that cancellation is no longer exact (Section 6.1)."* |
| W-1 (a) | 5.2, *The propulsion* | *"… which costs a control channel. A counter-rotating pair does not produce it."* | *"… which costs a control channel. A counter-rotating pair does not produce it. (This paper fixes body-axis naming throughout. That axis is the roll axis in both regimes; what changes is its orientation relative to the earth — it stands vertical in the hover attitude, where a moment about it appears as a change of heading, and horizontal in cruise, where it appears as a bank. The two conventions are not mixed here.)"* |
| W-1 (3) | 5.2, *What produces each moment* | *"(body axes, as fixed in the note below)"* | *"(body axes, as fixed in the note above)"* |
| W-1 (a) | 6.1 | *"… the aircraft's longitudinal axis, which is the roll axis in body terms. (This paper fixes body-axis naming throughout. …)"* | *"… the aircraft's longitudinal axis, which is the roll axis in body terms (Section 5.2)."* |
| W-3 | 2.3 | *"The margin in cruise efficiency is one tenth and nothing is claimed from its direction."* | *"The margin in cruise efficiency is 0.1 in effective lift-to-drag ratio, and nothing is claimed from its direction."* |
| W-4 | 4 | *"… worth **roughly a quarter to a half against the turboshaft reference, and against the all-electric one …**"* | *"… worth **roughly an eighth to a half against the turboshaft reference (a quarter to a half for the best examined blade family), and against the all-electric one …**"* |
| W-6 | 2.2 | *"Attitude devices produce thrust in cruise, but they produce no cruise thrust in that sense; they are used throughout the flight, …"* | *"Attitude devices produce no cruise thrust in that sense; they are used throughout the flight, …"* |
| W-8 | 3 | *"… about the body's longitudinal axis (Section 5.2), leaving that axis to the strip."* | *"… about the body's longitudinal axis (Section 5.2), leaving that axis to a strip on the lower surface, the only moving aerodynamic surface."* |
| W-9 | 1 | *"**Both work, and the second is the more demanding to build**, because rotating a propulsor in flight brings …"* | *"**Both work.** Rotating a propulsor in flight brings …"* |
| W-10 | 2.2 | *"The third departure is refused by a means other than the one the field has adopted. A tilting architecture accepts that departure and buys its way out of the first departure with a mechanism."* | *"A tilting architecture accepts the third departure and buys its way out of the first with a mechanism."* |
| L-1 | 4 (protected) | *"The same sizing set gives its two helicopter types at 5.4 to 7.2, …"* | *"The same sizing set gives four entries for its two helicopter types, at 5.4 to 7.2, …"* |
| L-4 | 5.2 | *"It is described as deployable in two halves"* | *"It is specified as deployable in two halves"* |
| L-5 | 5.2 | *"There is no cylindrical fuselage: every part of the planform carries payload and produces lift."* | *"There is no cylindrical fuselage: every part of the body that is carried is also a part that lifts."* |
| L-7 | 5.1 | *"This dual role is a dependency, reported as one where the sizing is audited, and …"* | *"This dual role is a dependency, reported as one in Section 3, and …"* |

**My notes on how I applied three of them. Each needs your yes:**
- **W-1 (a), placement.** You voted to put the axis note *"in place of '(body axes, as fixed in the note below)'"*. Done literally, the note's
  second sentence, *"That axis is the roll axis …"*, would have followed *"Pitch and yaw come from differential thrust between the tip
  pairs"*, and *"That axis"* would have had no antecedent. **I put it instead at the end of the paragraph where 5.2 first names the axis**
  (*"the propeller axis, which on this aircraft is the body's longitudinal axis — the roll axis in body terms"*), and changed *"below"* to
  *"above"* in the later parenthesis. The note is unchanged. If you prefer another place, say where.
- **L-5.** You chose Section 4's wording. Section 5.2 now repeats Section 4's sentence **verbatim**. That is a W8 question: is it an echo
  worth keeping? The alternative, by deletion only, is *"every part of the planform produces lift"*.
- **L-7.** You voted *"pointer to Section 3"*. I could not simply add *"(Section 3)"* after *"where the sizing is audited"*. That would
  have told the reader that Section 3 audits the sizing, which it does not; it states the dependency (the take-off margin and the attitude authority *"compete for it"*). So I
  **replaced** *"where the sizing is audited"* with *"in Section 3"*. Before touching it, I searched the whole text: Section 7.2 names
  *"the allocation of the take-off margin against attitude authority"* only as something the closure does not cover.

**My error, caught before sending.** Applied literally, W-8 left two *"(Section 5.2)"* in one sentence: the sentence already had one, and I
had not seen it when I drafted the repair. I deleted my added pointer. What you see above is the result. It is recorded as **R-10** (a
defect introduced by the repair, caught before application was shown).

**How W-1 (b) is implemented.** The step files now name the receiver's subheading, *"(Section 8, *What this inventory does not
settle*)"*. `v8_assemble.py` maps that to *"(Section 6.1)"*, and it maps *"(Section 8, *The propulsion*)"* to *"(Section 5.2)"*. The
assembler's list of valid section numbers gained 6.1. **No other text moved.**

**Recorded:** L-2 is in the coincidence register. L-3 (the six names) waits until the reading ends. L-6 is left.

**All checks are clean after the repairs:** retired phrases (167), protected sentences (187), nothing lost, assembly, references and figures.
The protected sentence of L-1 was updated in the protected list, and the W-10 relational names in the reference review. `--sina` was run on
four checks, and each still catches its planted fault.

---

## 2. First half — five items return to you

### W-2 (the contribution sentence). The author decides; here is where the vote stands

- The conflict is real: **all four of you** said so.
- My wording, *"What this paper contributes is the architecture this combination produces; …"*: Grok, DeepSeek and Qwen yes.
- **ChatGPT objects** that *"produces"* changes the relation between the architecture and the combination, and proposes: *"What this paper
  contributes is the architecture: the combination, the condition its primary propulsor is designed to satisfy, and the price the
  configuration pays for pursuing it are how that contribution is presented and priced."*

**My view has changed: ChatGPT is right.** *"The architecture this combination produces"* is a predicate that neither Section 1 nor
Section 6.2 carries. Section 6.2's own sentence has ChatGPT's order: *"The contribution is the architecture, and the paper presents it as
the combination, the consequences of the choices inside it, and the accounting."* I would change one thing. The colon after *"the
architecture"* reads as if the list that follows **defines** the architecture, so I would use a semicolon: *"What this paper contributes is
the architecture; the combination, …, are how that contribution is presented and priced."*

**Grok, DeepSeek, Qwen: do you accept ChatGPT's order?** The author decides the wording.

### W-5 (*"continuously since"*): three of you and I against ChatGPT

- **Delete *"continuously"* only:** Grok, DeepSeek, Qwen and I.
- **Delete the whole clause:** ChatGPT, on the grounds that *"since"* would be unanchored.

**My answer to ChatGPT.** *"Since"* is anchored: it follows *"The Convair XFY-1 flew it in 1954"*, so *"revisited the route since"* means
after 1954. That is witnessed (2007 onward). The clause also carries the paragraph's *"nor abandoned"*. Without it, *"It is neither new nor
untried nor abandoned"* has no support in its own paragraph until *"for over a decade"*, two paragraphs later.

**ChatGPT, does that meet your objection?** The others, please answer ChatGPT's point as well.

### W-6, the second clause (*"they are used throughout the flight, so their duty cycle matches their presence"*)

The deletion of the first clause is applied (§1); **that was unanimous.** On the second clause:
- **Leave it:** Grok, DeepSeek, Qwen and I.
- **Change it:** ChatGPT, to *"they are carried throughout the flight and fall outside Bill 1"*.

**My answer to ChatGPT.** Your wording drops the **reason** they fall outside Bill 1, and the reason is the Bill 1 test: mass carried
unused for most of the flight. Without it, a derived statement would read as asserted, and that is the protection criterion (Round 87).
Qwen put it exactly: the effector is *"not 'carried unused' like a dedicated lift rotor"*. **ChatGPT, do you accept "leave"?**

### W-7 (the tip frames in the definition section): my pointer was wrong

**DeepSeek is right, and it is my error.** The tip frames are introduced in **Section 3** (*"It rests on five points: the four lower ends of
the tip frames …"* and *"The tip frames are the landing structure …"*), not in Section 5.2. Grok and Qwen voted for (a) with my wrong
pointer. The options now:
- **(a′)** *"The tip frames of the configuration described in Section 3 are the case that tests it …"* (DeepSeek; **my vote**);
- **(b)** move the two sentences to Section 3 (ChatGPT).

**My reason for (a′).** ChatGPT wants the definition section kept free of the aircraft. But the sentence exists to show that the exclusion
has a boundary, and it needs a real case to do so. A pointer makes clear that the case comes later. **Please vote (a′) or (b).**

### L-8 (the counter-rotating pair sentences): four positions, and two of them assert something not shown

- **Grok:** name the state on *"A counter-rotating pair does not produce it"* (for example *"A torque-balanced counter-rotating pair …"*),
  and leave the angular-momentum sentence, because *"the two states are not shown to be the same"*.
- **ChatGPT:** record only.
- **DeepSeek:** no change, because *"the paper's operating state is torque-balanced, which for a counter-rotating pair in steady state
  coincides with equal speeds"*.
- **Qwen:** *"When torque-balanced, the net angular momentum … is nominally zero."*

**DeepSeek's and Qwen's readings both assert that torque balance and equal speeds are the same state. Nothing in this work shows that, and
Section 6.1 points the other way:** *"The torque balance within each pair is set exact at the cruise condition rather than at hover, so a
small residual remains in hover."* If balance depends on the flight condition, it is not simply a matter of speed. **Qwen's repair would
write the unshown equivalence into the body.** My vote is Grok's: a torque-balanced pair produces no net reaction torque by definition, so
naming that state on the reaction-torque sentence is safe, and the angular-momentum sentence stays as it is. **DeepSeek, Qwen: do you
accept Grok's split?**

---

## 3. First half — your new findings

| # | Finding | Who | My view |
|---|---|---|---|
| G-1 | 5.1 uses *"primary propulsor"* before 5.2 names the nose pair | Grok | **Not a defect.** Section 3 already says *"the primary propulsor — the nose pair — supplies a thrust-to-weight ratio of exactly one"*, and 2.2's fourth failure mode uses the term generically. That is a whole-text search result (Round 133 rule). |
| W-11 | Section 3, *"The 50 kg reference geometry"*, before the 50 kg reference design is introduced in 5.2 | DeepSeek | **Yes, a defect.** The first *"50 kg"* in the body is here. Repair: *"The 50 kg reference geometry (Section 5.2) is one point on that trade"*. DeepSeek's other option, *"A 50 kg design"*, changes the object from the reference geometry to any 50 kg design. |
| W-12 | Section 3, *"the buffer"* before definition | DeepSeek | **No change.** The relative clause defines it in place (*"the buffer that supplies what the engine cannot deliver of that peak"*), and Section 1 has already said *"a buffered series hybrid"* twice. Replacing it with *"store"* would break the link to that phrase. |
| W-13 | Section 4, *"the free-wheeling attitude rotors"* before the state is defined (6.1) | DeepSeek | **Yes, a defect**, and the same class as W-1: the state is fixed in 6.1, after this use and after 5.1's note. Repair: *"… the free-wheeling attitude rotors (Section 6.1) already charged."* |
| C-3 | 2.2's *"hardware that departs from one of four things"* carries a lot of logic before the numbered condition | ChatGPT | ChatGPT does not call it a defect. **Recorded, no change.** |
| Q-P1 | Assembler check: every cross-section pointer in the assembled text checked against its target in that text | Qwen | **Yes, narrowed.** It comes with a named defect (W-1), so it qualifies under F-1. An automatic check cannot know which subsection a *"Section 8"* pointer means. What it can do is **list, at every assembly, each pointer into the split step and each *above*/*below* in a split step's paragraphs, for a person to read**, with `--sina` putting W-1's *"(below)"* back and catching it. |
| D-P3 | In the second half, apply W1 to terms that cross the half boundary | DeepSeek | **Yes.** It is W1 applied, not a new check. It is in §4 below. |

---

## 4. Second half — how it runs, and my reading

The same rules as the first half apply: questions W1–W9 (Round 146 §4, unchanged), the baseline in the header, and findings only.
**Added for this half:** A-5 (the echo) and DeepSeek's cross-boundary terms. Sections 6–9 are about **7 700 words**.

I read the whole of §8. Six findings follow, most important first. **None has been applied.**

### X-1. The transition's altitude loss is reported at its smallest profile, and *"unchanged"* is false (W5, W2), Section 7.1

> *"… the 50 kg design **loses 5.4 m at the same reference condition.** The loss is not an artefact of the controller: it is unchanged
> across three reference profiles, appears without the control moment saturating, and grows as the gains are raised (Supplement S10)."*

and, protected:

> *"Whether a real aircraft loses 5.4 m, more, or less is not settled by anything here."*

**I re-ran `aero/transition_dynamics.py` this round**, 50 kg design, t_r = 2 s, M = 23.0 N·m, 5 m s⁻¹ climb entry, zero aerodynamic
moment:

| Reference profile | Altitude loss |
|---|---:|
| linear | 5.43 m |
| smooth | 6.33 m |
| bang-bang | 6.57 m |

**The loss is not unchanged across the profiles; it persists across them.** The body reports the **smallest** of the three. The repository
record says the same (*"Üç referans profilinde de aynı (5,4 / 6,6 / 6,3 m)"*, in `aero/README.md`; in my translation, not a quotation: the same in all
three reference profiles, 5.4 / 6.6 / 6.3 m). There *"the same"* meant that the loss appears in every profile, but the numbers under it are not
the same, and the body inherited the word. **This is my error too.** In Round 139 I recorded *"5.4 m is the linear rotation profile (…); the
other two profiles give 6.6 and 6.3 m (…)"* in the number-identity sweep, and I wrote *"no body change"*.

**Repair (for your vote):**
- *"… the 50 kg design **loses 5.4 to 6.6 m at the same reference condition**, depending on the reference profile. The loss is not an
  artefact of the controller: it appears under all three reference profiles, appears without the control moment saturating, and grows as
  the gains are raised (Supplement S10)."*
- The protected sentence: *"Whether a real aircraft loses 5.4 to 6.6 m, more, or less is not settled by anything here."*

Supplement S10 carries the same *"unchanged across linear, bang-bang and smooth reference profiles"*, and it is repaired with it.

### X-2. The transition runs on the assumed drag that Section 7.1 says appears only in the check (W5 model identity, W9), Section 7.1

> *"That check is the only place in this section where the assumed value appears, so the closures report a change of inputs, not of
> method."*

The transition figures, in the same section, are computed by a script whose drag inputs are the reference design's assumed C_D0 = 0.0248
and e = 0.85. **I re-ran the script at both ends of the bracket, with the computed span efficiency:**

| C_D0, e | linear | smooth | bang-bang |
|---|---:|---:|---:|
| 0.0248, 0.85 (assumed) | 5.43 | 6.33 | 6.57 |
| 0.0285, 0.817 | 5.44 | 6.33 | 6.58 |
| 0.0381, 0.817 | 5.45 | 6.35 | 6.59 |

The drag input moves the figure by at most 0.02 m, so **no number changes**. What is false is the sentence's *"the only place in this
section"*.

**Repair:** *"That check is the only place in the closures where the assumed value appears, …"* In the transition paragraph: *"Every
transition figure here belongs to a reference design at its reference mass **and its assumed drag**, and is not an output of the closure;
at either end of the drag bracket the altitude loss moves by less than 0.1 m."*

### X-3. *"the study carries all four"* blade families, but the closures carry two (W5, W2), Section 7.1

> *"… four nose-blade families that meet the hover figure of merit span cruise propeller efficiencies of 0.632 to 0.683, and the study
> carries all four rather than pretending to have chosen."*

The table directly below has two values of η_p, 0.632 and 0.683: two drag ends times two blade families. The other two families are not
closed. **Repair, by deletion only:** *"… span cruise propeller efficiencies of 0.632 to 0.683."* The sentence before already says *"The
blade family is a design variable this study has not fixed."*

### X-4. The closure's exclusion list still says *"closed-loop hover control"* (W4 regime, W9), Section 7.2

> *"Section 7.1's convergence does not cover … the vortex ring state, closed-loop hover control, engine installation, …; none of these is a
> ledger entry, and Section 8 lists them."*

**Section 8 lists** *"closed-loop attitude control in hover and in cruise"*. That was the S-60 repair (Round 140), and this sentence was not
reached by it. **This is my propagation miss.** The retired phrase in `v8_stale.py` was *"closed-loop hover control, including"*, which this
sentence does not contain.

**Repair:** *"… closed-loop attitude control in hover and in cruise, …"* And *"closed-loop hover control"* is added to the retired phrases.

### X-5. *"a fourth duty falls on the strip"*: the reader cannot count to three (W9), Section 6.1

> *"Either the residual is small enough to be absorbed that way, …, or a fourth duty falls on the strip."*

The body gives the strip **roll** (5.1, 5.2) and use as a **speed brake** (5.2). The nose-down pitch is a side-effect, not a duty. A
reader cannot find three duties. Perhaps it means heading in hover and bank in cruise, counted as two, plus the brake. **Report only.** If
none of you can name the three, the minimal repair is *"or another duty falls on the strip"*.

### X-6. The echo (A-5; Qwen P2, recorded by Grok in Round 134), Sections 8 and 9

*"**The loop closes; the aircraft is not shown to.**"* opens Section 8's last subsection and Section 9's last paragraph, about thirty lines
apart. Both are protected.

**My view:** as a reader meets it, it reads as a repeat rather than a bookend, because nothing between the two changes what it means. **Keep
it in Section 8**, where it is derived (the store, then the unknowns). **Delete it from Section 9**, which keeps *"Section 8 lists what would
settle the rest."* The claim survives in its home. **Please vote: keep both / keep Section 8 only / keep Section 9 only.**

### Lower priority — report only

- **L-9 (W2), Section 8, first paragraph.** *"This section is where that question is answered, and for the first item the answer is no:"*.
  The question is *"whether an aircraft can be built to it"*, so up to the colon the sentence reads as saying the aircraft *"cannot be built"*, which the
  Round 108 rule forbids. The colon then narrows it to *"the required store performance is not demonstrated by the sources consulted
  here"*. **Report only**, unless you think the first reading should not be allowed to stand even briefly.

### What I checked and found consistent

- **Section 7.4:** 55–84, 28–54, −13 to +7, and 67–77 points (66.7 to 76.7, recomputed from the table).
- **Section 7.2:** 14.6 % and 21.0 %; 52.6 % and 57.7 %; 1.9 to 2.1 kg.
- **Section 7.3:** 0.29–0.65 (0.0045 and 0.0100 over 0.0154) and 0.35 for the diameter-to-span ratio.
- **Payload fraction:** 0.25 to 0.23.
- **Section 7.2's exclusion list against Section 8's list:** every item has a home, apart from X-4's regime.
- **Section 6.2's claim table against Section 9:** the four axes agree.

---

## 5. Errors this round

- **Mine:**
  - **X-1:** I recorded the profile spread in Round 139 and did not see that the body says *"unchanged"*.
  - **X-4:** the S-60 repair did not reach Section 7.2.
  - **W-7:** I pointed to Section 5.2 instead of Section 3.
  - **R-10:** a duplicate pointer, caught before sending.
  - **W-2:** my first wording added a predicate. ChatGPT caught it.
- **DeepSeek and Qwen (L-8)** each asserted that torque balance and equal speeds are the same state. Nothing shows it, and Qwen's repair
  would have written it into the body. That is the *"do not guess the sign"* rule.
- **Grok (G-1):** *"primary propulsor"* is defined in Section 3. A whole-text search would have found it.
- **DeepSeek:** its §6 answers *"To DeepSeek on A-1"*, that is, itself. Harmless, but it shows that the reply was assembled from a template.
- **ChatGPT:** none found. Its W-2 objection was right.

---

## 6. To vote

| # | Item | My vote |
|---|---|---|
| a | §1: each applied repair confirmed, including my three placement notes (W-1 (a), L-5, L-7) | confirmed |
| b | W-2: ChatGPT's order, with a semicolon (the author decides) | yes |
| c | W-5: delete *"continuously"* only | yes |
| d | W-6, second clause: leave | yes |
| e | W-7: (a′) or (b) | (a′) |
| f | L-8: Grok's split | yes |
| g | G-1 no change; W-11 yes; W-12 no change; W-13 yes; Q-P1 yes, narrowed | as stated |
| h | X-1 to X-4 repairs | yes to each |
| i | X-5 | your reading of the three duties |
| j | X-6 (the echo) | keep Section 8 only |
| k | L-9 | report only |
| l | **Your own findings in Sections 6–9, against W1–W9** | — |

**Answer each other**, especially on W-5, W-6 and L-8, where the disagreement is named.

---

## 7. Your own proposals

Under F-1, only proposals that come with a named defect in the present body text. Everything else goes to the parking list.

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## 8. The text — Sections 6–9 of the assembled view, in full (baseline above)

### 6. The soundness of the resulting product

#### 6.1 What this inventory does not settle

**An untrimmed hover torque, with no trim mechanism identified.** This is a control question
rather than a property of the hardware, and it is stated as one.

The torque balance within each pair is set exact at the cruise condition rather than at hover, so
a small residual remains in hover. It acts about the propeller axis — the aircraft's longitudinal
axis, which is the roll axis in body terms (Section 5.2).

That axis is the one the configuration has chosen not to command with the propellers, which is why
the residual is awkward: the tip pairs cannot absorb it by thrust differential, because their thrust
vectors are parallel to that axis too, and the strip works against dynamic pressure that the
slipstream supplies over only part of its length at zero airspeed. What is left is the channel the
configuration set aside — the speed trim of the pairs, which is a reaction-torque command and not a
thrust one. Either the residual is small enough to be absorbed that way, which this study has not
shown and which would mean the architecture spends a little of the channel it declined, or a fourth
duty falls on the strip.

**The fixed geometry of the tip pairs leaves two admissible cruise states, and only one of them
is physically closed.** Unable to feather, the pairs must either turn at the zero-shaft-torque
condition or be stopped. This configuration uses the first: free-wheeling at zero shaft torque is the tip pairs' uncommanded cruise state, and it is the drag state Section 7.2 charges. The shaft power of commanded departures from that state, for attitude moments in cruise, is not computed.

The free-wheeling state is physically determinate: the rotor settles where net shaft torque is
zero. **The stopped state is not.** Stopping a rotor requires the stop to be produced by
something — motor holding torque, an electrical brake, a mechanical lock — and a stopped
fixed-pitch blade also has an azimuth, so "stopped" is a family of aerodynamic states rather than
one. Neither the means nor the azimuth is fixed by this study, and the drag figures estimated for the
stopped condition (Supplement S11) should be read as estimates for an assumed azimuth rather than as the state a
particular installation would reach. The free-wheeling state needs no stopping means; the stopped state does, and if it were a
brake or a lock rather than motor holding torque, the count of Section 5.1 would gain a class.

#### 6.2 What is not claimed

This section states the boundary of the paper's claims. It is placed before the configuration's own numbers.

**It is not a list of the study's open questions.** Those are in Section 8, and the difference matters: the boundary below is about claims the paper **declines to make**, most of which it could not make on any evidence; Section 8 is about questions the paper **does not answer**, and which better evidence would answer. One is a scope; the other is a debt.

##### The claims are made on four axes, against four different opponents

Comparison is only meaningful against a named alternative, and this paper's alternatives differ from axis to axis.

| Axis | Opponent | Status |
|---|---|---|
| Cruise efficiency | Rotorcraft: multirotors and helicopters | **Claimed against multirotors, and bounded; against helicopters the comparison with published figures is mixed and no advantage is claimed.** Cruise lift is carried on a surface rather than on rotors, which no sizing contract changes. The *size* of the resulting advantage is a calculation, not a consequence of that fact (Section 4). |
| Operation without a runway | Fixed-wing aircraft | **Claimed as sized, not demonstrated** (Sections 3, 8). |
| The mechanism required to change regime | Tilting architectures | **Claimed.** This is the paper's contribution — a count of mechanism classes (Section 5.1), not a claim of mechanical simplicity or reliability. |
| Cruise efficiency and range | Other hybrids — lift-plus-cruise, tilt | **Not claimed, in either direction.** |

**The fourth row is the important one**, and the reason it is a refusal rather than a result is the paper's own finding in Section 7.4. Against lift-plus-cruise the ordering depends on the sizing contract: across the three contracts it moves substantially, and under one of them its sign changes inside the envelope and turns on quantities of the competitor that are assumed rather than measured. A paper that quoted one of those orderings as a result would be reporting its own choice of contract. Against the tilting family the competitor can be modelled here only as a bound that pays no cruise penalty, and an ordering against a bound is not a result. **No range claim is made against the tilting or lift-plus-cruise families in either direction**, and a reader who finds one implied anywhere in this paper should treat it as an error rather than as a claim.

##### What each claim does not depend on

**Operation without a runway** does not depend on the drag bracket, the propeller efficiency or the transition aerodynamics — **but it does depend on the energy store**: the vertical phase is sized with one, and Section 8 examines whether it exists. **Cruise lift carried on a surface** does not depend on the sizing contract or the transition aerodynamics. The **size** of the cruise-efficiency margin depends on both the drag bracket and the blade family, and Section 4 reports it as a range rather than a number. **Elimination of the propulsor-reorientation mechanism class** does not depend on the drag bracket, the propeller efficiency, the sizing contract, the range result or the energy store — **nor on the transition aerodynamics**.

**The last of these carries a distinction that matters more than the others.** The mechanism claim is a statement about what hardware is present, and it is settled by the inventory of Sections 5.1 and 5.2. **The separate claim that this aircraft can actually perform the regime change is not settled** (Section 5.1).

##### One cost of the contribution that is named and not priced

The mechanism claim has a price this work does not compute. **This configuration declines the reaction-torque channel that comparable aircraft use for roll (Section 5.2). What that refusal costs — in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia — is not computed anywhere in this paper.** The claim is that the mechanism class is eliminated.
**Whether eliminating it is favourable on balance is a question this work does not settle**, and quantifying it would require a control-allocation study rather than a single torque figure.

##### Eight things this paper does not claim

**1. It does not claim range against fixed-wing aircraft.**

**2. It does not claim vertical capability against rotorcraft.** That comparison runs the other way.

**3. It does not claim that the aircraft has no moving parts.** What is eliminated is a *class of mechanism* — the one that reorients a propulsor. The aircraft has a moving aerodynamic surface, it is named where the elimination is claimed rather than later, and it also pitches the nose down when deployed.

**4. It does not claim mechanical simplicity.** Part count, assembly mass, failure modes and maintenance burden were not measured, and nothing here supports a statement about reliability. The count of mechanism classes in Section 5.1 is not a reliability argument.

**5. It does not claim that the escape condition is fully instantiated.** The condition is met in the propulsor that carries the aircraft and is not met in the attitude system, which is carried through cruise producing moments rather than cruise thrust. Section 2.2 names that case as partial instantiation, and the charge it re-opens is reported rather than absorbed.

**6. It does not claim that satisfying the condition makes an aircraft better.** The condition concerns three specific charges. A configuration may avoid all three and still be unbuildable, uncontrollable, or unsuited to its mission, and the accounting says nothing against that possibility.

**7. It does not claim that the trades inside the escape are favourable.** Moving the hover peak onto a store converts a power-system charge into a cost in kilograms; serving two regimes with one set of fixed-geometry propellers costs efficiency in at least one of them. Both are computed, neither is asserted to be worth paying, and the ledger reports them whichever way they fall.

**8. It does not claim that the aircraft flies.** The design *sizes* vertical operation and the transition; it does not demonstrate either. No aircraft has been built, no wind tunnel has been run on this geometry, and the transition analysis is a calculation whose assumptions are stated where it appears. **"By construction" throughout this paper means "by the sizing", never "by demonstration."**

##### What the claims that remain amount to

Removing those eight leaves something narrower than a first reading of the abstract might suggest, and the narrower statement is the one the paper defends: **a configuration sized to combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism that reorients a propulsor, and an account of what the combination costs.**

Each half of that has a named opponent and neither half is a record. **Nor is the configuration claimed to be without precedent**: Section 1 sets out what is already established, including uncrewed tail-sitters, tail-sitters without control surfaces, coaxial contra-rotating tail-sitter propulsion, and blended-wing-body tail-sitters. **The contribution is the architecture, and the paper presents it as the combination, the consequences of the choices inside it, and the accounting** — which is what Sections 5.1 and 5.2 describe and what Section 7.2 prices.

##### One consequence for how the numbers that follow should be read

Because the comparative result depends on the sizing contract, **no comparison in this paper should be quoted without the contract it was computed under.**

### 7. The calculations

#### 7.1 Analytical closure of the sizing loop

This section prices the arrangement of Sections 5.1 and 5.2 on a declared package; it does not bear on the count of mechanism classes, which rests on the inventory of those sections alone. **Closing a sizing loop mathematically is not the same thing as closing an aircraft physically.** This section does the first: what it produces is a set of consistent numbers on a declared set of assumptions.

Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Supplement S10). **If no fixed point exists, the declared sizing package does not close.**

##### The inputs, and why there are four closures rather than one

**The zero-lift drag coefficient is uncertainty:** a consistent build-up places it between 0.0285 and 0.0381 (Section 7.2), and a designer does not choose where the real aircraft falls in that range. **The blade family is a design variable this study has not fixed:** four nose-blade families that meet the hover figure of merit span cruise propeller efficiencies of 0.632 to 0.683, and the study carries all four rather than pretending to have chosen. **The reference design's assumed zero-lift value of 0.0248 is not used**; the consistent build-up places it below both ends of the bracket, outside the supported range.

The loop holds wing loading, disc loading and aspect ratio fixed, so **the cruise lift coefficient is unchanged at 0.450 in every closure** (geometry in Supplement S10); the claim is that C_L is unchanged, not that C_D0 is exactly so. The tip frames, the tip discs and the strip are not sizing variables; they were set on the 50 kg reference design of Section 5.2, and **the control moment arms of Section 5.2 are therefore reference values that this closure does not re-derive.** **These are the same configuration at four closed masses rather than four configurations** — but anything that depends on the arms is carried at the reference geometry and is not an output of the loop.

Run on the reference design's assumed inputs — that drag coefficient without the rotor term, and a propeller efficiency of 0.80 — the same construction reproduces the 50 kg reference design within 1.5 percent (Supplement S10). That check is the only place in this section where the assumed value appears, so the closures report a change of inputs, not of method.

##### The four closures

**On these assumptions all four converge**, for the 50 kg design — the only one carried through this loop.

| | C_D0 | η_p | L/D | L/De | MTOW | Empty fraction | Hover power, rotor shaft | Engine rating, shaft | Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** | 0.0381 | 0.632 | 8.79 | 5.56 | 57.5 kg | 0.614 | 12.53 kW | 5.17 kW | 927 km |
| **B** | 0.0381 | 0.683 | 8.79 | 6.00 | 55.8 kg | 0.607 | 12.17 kW | 4.65 kW | 1 002 km |
| **C** | 0.0285 | 0.632 | 10.82 | 6.84 | 53.5 kg | 0.597 | 11.66 kW | 3.91 kW | 1 141 km |
| **D** | 0.0285 | 0.683 | 10.82 | 7.39 | 52.3 kg | 0.592 | 11.40 kW | 3.54 kW | 1 233 km |

*L/De = L/D × η_p at the cruise condition; the loop holds both factors fixed within each closure, so the closure changes
neither. The four L/De values are the bounding corners of that product, carried into the closures as inputs, not four
simulated aircraft.*

**Payload is an input, fixed at 13 kg; take-off mass is the output**, and the payload fraction runs from 0.25 down to 0.23. **The blade that is best before the loop is still best after it.** There was no reason to assume so: propeller efficiency propagates through cruise power into engine size, engine size into mass, and mass back into hover power, and a loop can reverse a local ranking. At both ends of the drag bracket the higher-efficiency family closes to the longer range — **a result of the closure rather than an assumption carried into it.**

##### The transition

The sizing above says nothing about whether the aircraft can change regime. **The question is asked in two models, only the second of which carries rotational dynamics, and that one does not support a zero altitude loss.** Every transition figure here belongs to a reference design at its reference mass and is not an output of the closure. In the first, a point-mass model with the body angle driven kinematically, a rotation entered in a 5 m s⁻¹ climb loses no altitude at either reference rotation time: 2 s for the 50 kg design and 5.1 s for the 1 000 kg one. Solved instead with rotational dynamics and a finite control moment, **and with the aerodynamic pitching moment set to exactly zero, so that nothing favourable is borrowed**, the 50 kg design **loses 5.4 m at the same reference condition.** The loss is not an artefact of the controller: it is unchanged across three reference profiles, appears without the control moment saturating, and grows as the gains are raised (Supplement S10). **What the kinematic model leaves out is not the difficulty of turning the aircraft but the trajectory the aircraft flies while it is being turned.** **So the zero-altitude-loss result is a property of the model that produced it.**

What replaces it is not a prediction: the pitching moment that would make it one exists, but for the methods used here the predictions diverge above roughly ten degrees of incidence, the band the rotation passes through (Section 8). With a borrowed moment the spread is wide enough that no number from it is reportable: some models complete the rotation, some saturate the tip pairs, and some tumble. **That spread is itself the finding.** **Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude.** Whether a real aircraft loses 5.4 m, more, or less is not settled by anything here.

##### What closing does and does not establish

It establishes that the architecture is arithmetically self-consistent on a declared package, at four corners of that package. **It does not establish that the package exists.** The energy store this closure assumes is the item Section 8 examines, and the examination does not end well. These ranges are carried forward as closed-loop values, not as a ranking: no rotorcraft is sized in this work, so no range comparison is made against one (Section 4 compares cruise efficiency), and the comparison with the other hybrids depends on the sizing contract (Section 7.4).

#### 7.2 The ledger

Section 2.1 named three charges that any architecture in this corner pays; **this section says where each charge appears inside the closed numbers of Section 7.1, and how large it is there.** Like the closure, the ledger prices the arrangement; the count of mechanism classes is not an entry in it.

**It attributes. It does not add.** Every cost named below is already inside the closure of Section 7.1. **No new physical cost term is introduced here.** **And there is no single figure for what the architecture costs.** The three charges are in three different currencies — kilograms, drag counts, installed kilowatts — and **no scalar aggregate is defined, because this study has no defensible weighting between them.** **The total is the contract, not a property of the aircraft** (Section 7.4).

##### Bill 2 — the drag of hover hardware, inside the bracket

In the zero-lift drag build-up behind Section 7.1's bracket (line items in Supplement S11), **the hardware exposed by the vertical-phase layout — the tip frames and the free-wheeling attitude rotors — is 69 percent of the zero-lift drag at the favourable end and 57 percent at the adverse one**; the rotor term alone is 0.0154 at the favourable end. **The rotor line rests on section drag at low Reynolds number.** It is a blade-element result for sections near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section polars that are computed rather than measured; Section 7.3 shows how strongly the term depends on it. **The tip-frame term is an attribution, not a marginal removal cost**: it is not a claim that this drag would disappear if the vertical phase did. **No stopped-state counterfactual was computed.** The eight tip discs stopped edge-on at a controlled azimuth are estimated at ΔC_D0 = 0.0008, against the computed free-wheeling 0.0154 (the estimate is an area-and-coefficient calculation, Supplement S11), but controlling the azimuth takes an indexing mechanism — a class Section 5.1 counts — and sizing it for eight small discs, charging its mass and its failure modes, and re-solving the loop has not been done.

Removing the hub and small items, the tip frames and the free-wheeling rotors gives a clean-body lift-to-drag ratio of 20.55 at the favourable end and 15.24 at the adverse one, against the aircraft's 10.82 and 8.79: **the configuration retains 52.6 and 57.7 percent.** Bill 2 therefore occupies a larger share where the clean-body drag is lower, because a near-constant charge is set against a smaller total — a statement about position within the drag bracket at one scale, not about size (Section 7.3).

**Rotor–structure and rotor–wing interference is not modelled and is not carried as a line.** Section 2.1 quotes a wind-tunnel finding that a simulation assuming negligible rotor–structure interaction *"always predicts higher lift and lower drag than were experimentally observed"*; this build-up is such a calculation, and the bracket's upper margin is the only provision made for it.

##### The cruise-efficiency gap under fixed pitch

Section 7.1's closures run at a cruise propeller efficiency of 0.632 to 0.683: **relative to the 0.80 the reference design's sizing assumed, 14.6 percent lower at the better blade and 21.0 percent lower at the worse.** **The ledger does not attribute the whole of that gap to the absence of variable pitch.** **No variable-pitch counterfactual was computed.** Nor is the gap decomposed.

##### Bill 1 — carried mass, and what it is on this configuration

**There is no dedicated lift group to charge.** What Bill 1 becomes here is the energy buffer: **3.6 percent of take-off mass, 1.9 to 2.1 kg across the four closures.** The buffer is not lift-subsystem mass, so it is not Bill 1 as Section 2.1 defines it, but it is carried for the whole flight to serve a demand that lasts about two percent of it: **the architecture converts a power-system charge into a cost in kilograms**, as Section 2.2 said in advance it would.

**The buffer fraction is an input to the loop, not a result of it.** The deficit per kilogram of take-off mass that the buffer covers, taken at the electrical bus, spreads by 12 percent across the four closures while the fraction is held at 3.6 percent (Supplement S11). **The corner that needs the most buffer per kilogram is given the smallest buffer**, and that is a declared assumption of the closure rather than an outcome of it.

##### Bill 3 — released from the engine, and not from the electrical path

The engine is sized by cruise, **3.54 to 5.17 kW** of shaft rating, against a hover requirement of **11.4 to 12.5 kW** at the rotor shaft: a ratio of installed hardware of **2.4 to 3.2**, which is not the buffer's burden (Section 8 computes that). **But the full hover power passes through the electrical path, and that path is sized by it.** **Bill 3 is removed from the engine and left standing on the electrical system** (the propulsion-mass split is in Supplement S11).

##### What the closure does not contain

Section 7.1's convergence does not cover the cost of declining the reaction-torque channel, the sizing of the strip's actuation, the allocation of the take-off margin against attitude authority, the landing transition, the vortex ring state, closed-loop hover control, engine installation, or rotor–structure and rotor–wing interference; **none of these is a ledger entry, and Section 8 lists them.** **The first and the last are the two that would most change the numbers above if they were computed.**

**Every one of the charges above belongs to one scale**: the four closures do not establish how the three charges behave as the aircraft changes size, which Section 7.3 asks, or what happens to the comparison when the sizing contract changes, which Section 7.4 asks.

#### 7.3 Scale does not lock two of the charges together; the third is not tested

Section 7.2 decomposed the three charges on one aircraft, at one size; **this section asks whether they are three quantities or one quantity under three names**, by changing the size of the aircraft and seeing whether they move together. Either answer leaves the mechanism claim where it was; that claim rests on the inventory of Sections 5.1 and 5.2. **The test is deliberately weak**, and it is stated at its own strength. It can show that two charges are not locked together within this model. **It cannot show that they are independent in general**, and it is not offered as doing so.

**The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 7.1's closures**: no closure was run at 1 000 kg, the heavy design has no drag bracket and no structural closure, and no heavy-design range is quoted.

##### Bill 3 — held nearly flat by a sizing rule, which is not a finding about Bill 3

Disc loading is held at approximately the same value, 44.2 kg m⁻² at 50 kg and 43.7 at 1 000 kg, so specific hover power is held with it: 0.218 kW kg⁻¹ at the light design and 0.216 at the heavy. **That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3.**

Section 7.2's measure of Bill 3, rotor-shaft hover power over engine shaft rating, is 4.19 at the light design and 3.98 at the heavy, and with the engine margins the two designs use it **moves by between 5 and 14 percent across the factor of twenty, depending on an engine margin the sizing rule does not set** (Supplement S12). *(Section 7.2's 2.4 to 3.2 is the same ratio at the four closures. This paragraph compares the reference pair only.)*

The rule has a price, paid in geometry: the ratio of propeller diameter to span rises from 0.35 to 0.47, and **much above 1 000 kg a single nose pair can no longer hold the disc loading**, so a second would have to be added.

##### Bill 2 — the rotor term falls, and in this model Reynolds number accounts for it

**Only the rotor term of Bill 2 is computed at both sizes**; the frame term enters both designs as the same multiplier, so it cannot show a scale effect in either direction. At 50 kg the rotor term is **0.0154**; at 1 000 kg the blade designed to the same section lift coefficient gives **0.0068**, and the blades swept give 0.0045 to 0.0100 — a direction that is the ordinary one and a factor that is not a measurement. **Within the blade-element and section-polar model, the section Reynolds number accounts for the fall**, rising from about 8 × 10⁴ to 5.6 × 10⁵; three other candidates are excluded (Supplement S12), and this is a decomposition inside the model rather than a causal claim beyond it.

The fall rests on section drag taken from polars rather than measured, and the light end lies below a Reynolds number of 10⁵, where section drag is hardest to predict. **Of the two rotor terms, the light one is therefore the less certain — and it is the one Sections 7.1 and 7.2 carry.**

##### Bill 1 — not tested, and the one available derivation would not test it

On this configuration Bill 1 appears as the energy buffer: 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and **both of those figures are inputs.** **A change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction.** A buffer sized to the hover deficit at the same specific power would track hover power and engine rating, which are the Bill 3 measures, so that derivation cannot test whether Bill 1 separates. **Whether the two are separable here is not established**; what is established is that they are coupled here, which is Section 2.2's claim rather than a defect found in it. **Coupling is not identity**: the buffer is measured in kilograms and the engine in kilowatts, linked by a specific power that is itself an assumption.

##### What the comparison establishes

**Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its light-design value in the section polars used here, while specific hover power changes by one percent and the Bill 3 ratio by 5 to 14 percent.** The flatness of Bill 3 is imposed by a sizing rule; the finding is that Bill 2 moved anyway, by more than the Bill 3 ratio at every point in the heavy interval and under either engine margin. **Within this model, the two are therefore not one quantity under two names.**

**Bill 1 is not tested**, and nothing here should be read as showing that it separates from the other two — or as showing that it does not. **The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low Reynolds number.** It is consistent with the separability Section 2.1 asserts; it is not a verification of separability as a general property, which a single instantiation cannot supply.

##### Two costs that scale does not relieve

The fixed-pitch gap also widens slightly with size, to 16.4 to 22.9 percent at the heavy design (Supplement S12); as in Section 7.2, no variable-pitch counterfactual was computed. **The transition is where the square–cube relation is paid in full**: rotating the heavy design in the light design's two seconds would demand about 220 kW from the tip propellers, roughly the whole of hover power; at its own 5.1 seconds the demand is about 13 kW. **A larger aircraft of this type turns more slowly, and must.**

##### Why this section sits between the ledger and the contracts

**Because at least two of the charges are not locked together, a comparison of architectures cannot in general be reduced to a number that does not depend on how the charges are weighed.** The argument requires only two charges that are not locked together; the third need not be shown separate for the conclusion to hold. Section 7.4 examines what the choice of sizing contract does to a ranking, on the light closures of Section 7.1 only.

#### 7.4 Rankings belong to contracts

Section 7.3 showed that at least two of the charges are not locked together; where one architecture pays less of one charge and more of another, the ranking depends on how the charges are weighed, and **a sizing contract is one such weighing**: it fixes what is held equal between the architectures being compared. This section applies three contracts to three architectures at each of the four closures of Section 7.1. **The mechanism claim is not a ranking and is not at stake here.**

##### Three contracts, and what each holds equal

Range in the sizing loop is proportional to L/D, to the energy chain, propeller included, and to the fuel fraction, and the three contracts differ only in the last (Supplement S13): a **fixed fuel fraction**, sixteen percent of each architecture's own take-off mass, under which take-off mass cancels from range; a **fixed fuel mass**, the 8.4 to 9.2 kg this configuration carries, under which range is divided by take-off mass; and a **fixed take-off mass and payload**, under which every kilogram of architecture-specific hardware is a kilogram of fuel not carried. **These are three different questions, not three estimates of one answer.** A mission decides which of them it is asking; this paper has no mission that would decide, and does not choose.

##### What is compared, and on what basis

Three architectures fly the same mission, 13 kg of payload at 30 m s⁻¹, with the same wing loading, disc loading and aspect ratio, the same airframe and avionics fractions, and the same fuel and energy chain apart from the propeller. **The competitors are therefore this planform with two add-ons, not independently designed aircraft of their families.** All three carry the same buffered series-hybrid power system, so Bill 3 is held common and the comparison measures mass and cruise drag. **Holding Bill 3 common is a choice of question, and it has a direction.** **The choice runs against this configuration.** Without the buffer, and with engines rated to deliver the hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off mass and falls 38 to 47 percent behind under a fixed fuel mass, and the tilt bound does not close under a fixed take-off mass; under a fixed fuel fraction it closes at 520 kg, about ten times this configuration's mass — the first contract's blindness to mass, made visible. That comparison is not used, because it would set competitors without a store against this configuration with one.

The basis is not symmetric: the lift-plus-cruise layout carries a lift-to-drag ratio transferred from a different airframe's wind-tunnel campaign (Section 2.1) and assumes lift rotors stopped and aligned in cruise, which takes an indexing mechanism (Section 5.1) whose mass is not separately charged. **The tilting layout carries no cruise drag penalty at all. That is an idealisation in its favour**, and it is deliberate: it makes the tilting layout a bound. Both competitors use a propeller efficiency of 0.80, assumed, not computed, against this configuration's computed 0.632 and 0.683; the lift-plus-cruise layout carries a lift group of 10 percent of take-off mass and the tilting layout a tilt mechanism of 5 percent. **Neither figure is measured.**

##### Against lift-plus-cruise: a trade, and the contract sets the exchange rate

**The two architectures trade one charge against another**: closed under a fixed fuel fraction, this configuration is 27 to 30 percent lighter, and the lift-plus-cruise layout cruises at a lift-to-drag ratio of 11.66 and 15.72 against 8.79 and 10.82, with a propeller at 0.80.

Range of the lift-plus-cruise layout relative to this configuration:

| Closure (Section 7.1) | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass |
|---|---:|---:|---:|
| A | +67.8 % | +40.2 % | +1.1 % |
| B | +55.3 % | +27.5 % | **−13.0 %** |
| C | +83.9 % | +53.5 % | +7.3 % |
| D | +70.2 % | +40.1 % | **−6.5 %** |

**The lift-plus-cruise layout is 55 to 84 percent ahead under the first contract, 28 to 54 percent under the second, and between 13 percent short and 7 percent ahead under the third; the shift from first to third is 67 to 77 percentage points at every closure**, at the declared lift-group fraction, and always toward the lighter aircraft. **The sign itself changes inside the envelope under the third contract**: this configuration is ahead at the two closures with the higher-efficiency blade family and behind at the two with the lower. **A statement of which architecture has the longer range, made without its contract, would therefore be a statement about the contract.**

##### Against the tilting layout: a bound, not a ranking

**What the bound gives is a size, not an order.** Credited with no cruise penalty, the tilting layout is 93 to 141 percent ahead of this configuration under every contract at every closure; that margin is the room a real tilting aircraft's cruise penalties — nacelle drag, pivot fairing, hover-sized rotors flown as cruise propellers — would have to fill, and how much of it they fill is not computed. **A ranking against a competitor modelled as a bound is not a ranking, and no range claim is made against the tilting family in either direction.**

##### Section 2.1's prediction, tested

Section 2.1 predicted that such a ranking will move when the sizing rule changes, and can reverse. **The movement holds everywhere**, against both competitors, toward the lighter arrangement as the contract weights mass more; **the reversal holds at two of the four closures against lift-plus-cruise, and at none against the tilt bound.**

**Where the reversal falls is decided by quantities this study has not measured or not fixed**: the blade family in the base case, and across the sensitivity cases the competitor's lift-group mass and the propeller basis (Supplement S13). With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every closure; with a heavier one this configuration leads under a fixed take-off mass at every closure; with a common propeller efficiency a reversal appears at every closure. **Which architecture ranks first under a fixed take-off mass is therefore decided, in this model, by quantities this study assumes for the competitor rather than measures: its lift-group mass fraction and its propeller efficiency.** **Put plainly, the sign under a fixed take-off mass is not a result about the architectures; it is a result about those quantities.** What is robust is that the shift exists and runs toward the lighter aircraft; its size is the size of the mass difference.

##### What the framework asks of whoever uses it

**Each comparison states every charge in its own currency before any aggregate, names its contract, and states its asymmetries and their directions; an ordering is reported only with the contract it was computed under and, where its sign depends on an unmeasured quantity, with that quantity named.** This paper meets that for its own column (Section 7.2) and not for the competitors', whose kilograms and drag counts here are parameters and transferred ratios rather than an audit.

##### What this section does not establish

**The competitors are modelled at a coarser level than this configuration**: their drag is transferred or idealised, their propeller efficiency assumed and their architecture-specific mass a parameter. **Comparing computed figures against assumed ones favours whichever is assumed more optimistically** — in propeller efficiency both competitors, and with a common propeller efficiency the lift-plus-cruise lead under the first contract falls from 55–84 to 33–45 percent (Supplement S13); in drag the tilting layout, by assumption. **The comparison is at one size**: Section 7.3's 1 000 kg reference design has no closure, and none of its figures is used here. **And nothing here ranks architectures for a mission.** What this section establishes is narrower: **the same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property of the architectures alone.

### 8. What does not close

Section 7.1 closed the sizing loop on a declared package and said that whether an aircraft can be built to it is a different question. **This section is where that question is answered, and for the first item the answer is no: the required store performance is not demonstrated by the sources consulted here.** Section 6 called this section a debt: questions the paper does not answer and that better evidence would. It is stated in that order — first the obstacle that is known, then what is not known.

#### First, the known obstacle: the energy store

**Every closure in Section 7.1 carries a buffer of 3.6 percent of take-off mass**, an input rather than a result (Sections 7.2 and 7.3). Taken at the electrical bus, where the buffer sits, **the four closures ask the buffer for 4.7 to 5.2 kW per kilogram of buffer to hover, and 5.5 to 6.1 kW per kilogram of buffer to leave the ground** with the tip pairs at full thrust (Section 3).

**What has been measured is a fraction of that, and the store figures available are of four different kinds.** A 24-series nickel–cobalt–manganese pack designed, bench-tested and flown in a 210 kg-class electric VTOL aircraft is rated, as a flown system, at 0.892 kW per kilogram continuous; its unit pack, discharged on the bench at its highest tested rate, delivered on average about 1.5 kW per kilogram (Supplement S14). A NASA-funded design study adopts 4 kW per kilogram and describes that figure as about twice that of existing batteries. The same study notes lithium-polymer figures in the literature as high as 3 kW per kilogram, which it cites rather than measures; against that figure the take-off demand is 1.8 to 2.0 times. The study argues that, because pulse current limits can exceed continuous ones — by more than a factor of two in one commercial module it cites — a pack with the required specific power may be possible with existing technology; the study's hover lasts twenty seconds or less; this aircraft's vertical phases occupy about a minute in all (Section 2.1), and how long each draws the peak is not computed here.

**The take-off demand of Section 7.1's closures is 3.7 to 4.1 times the bench rate — the highest figure obtained from a measurement — and 6.2 to 6.8 times the flown system's continuous rating**; hover alone is 3.1 to 3.5 times the bench rate. The comparison is between unlike ratings: a peak demand held through the vertical phases, a bench average over minutes, a continuous rating, a design assumption, and a literature figure the study cites without its rating. **The gap is real on every one of them; the factor quoted is peak demand against bench average.** The package Section 7.1 closes on does not exist with any store the sources consulted here report as built.

**Closing the loop on a measured store is a sensitivity of that package, not a second aircraft**: the buffer is derived inside the loop from the take-off demand at a given specific power, and everything else is Section 7.1's. At the bench rate of about 1.5 kW per kilogram the loop closes at 94.6 to 101.2 kg, 76 to 81 percent heavier, with a buffer of 13.4 to 14.7 percent; at the design study's 4 kW per kilogram it closes 6 to 8 percent heavier (the table is Supplement S14). **These masses are the Section 7.1 package with one input changed. They are not a structural closure at 100 kg**, and whether the airframe fraction holds at twice the mass it was set at is not established. If Section 7.1's take-off masses are retained instead of re-closing at the bench rate, the payload falls to about 7 kg rather than 13; at the flown system's continuous rating the loop only just closes, and at the unit pack's continuous rating it does not close at all.

**This is where the coupling Section 7.3 found is paid**: the buffer is the conversion the escape condition permits — kilowatts of hover peak paid in kilograms of store. **The escape from Bill 3 is real in the sense Section 2.2 defined it, and its price depends on a component whose required performance has not been demonstrated.**

#### What the obstacle reaches, and what it does not

**It reaches every number that describes this aircraft at Section 7.1's masses**: the closed masses of 52.3 to 57.5 kg and the 13 kg payload assume the store. The ranges of 927 to 1 233 km survive the re-closure only because the fuel fraction is held, on an aircraft three-quarters heavier; they do not survive as 13 kg carried that far on a store that has been built. The vertical phase that Section 3 reports as sized was sized with this store in it, and Section 7.4's orderings were computed with the store held common at 3.6 percent; how they would move with a measured store is not computed.

**It does not reach the mechanism claim.** That is a statement about hardware, and a heavier store adds no pivot. **Nor does it reach the cruise-efficiency comparison of Section 4 as a ratio**: effective lift-to-drag ratio has no mass in it. As a comparison of aircraft, that section describes the configuration at Section 7.1's masses, which the store does reach.

#### Then what is not known

The remaining items are not known obstacles; they are questions this work has not answered, and each is listed with what would settle it in Supplement S14. They are:
- the pitching moment through the transition;
- section drag at low Reynolds number;
- the tip pairs' stopped cruise state;
- the tip pairs' shaft power when commanded off the free-wheeling state in cruise;
- the buffer's energy, not only its power;
- the electrical path at peak;
- the airframe's mass;
- the strip and the fairing;
- closed-loop attitude control in hover and in cruise, including the declined reaction-torque channel, the hover torque residual and the allocation of the tip pairs between take-off margin and attitude authority;
- vertical descent and the landing transition;
- ground handling and landing loads;
- the competitor's lift-group mass;
- the competitor's cruise propeller efficiency;
- rotor–structure and rotor–wing interference;
- engine installation;
- blade-family selection;
- the variable-pitch counterfactual;
- atmosphere.

**None of these is a small correction to a known quantity.** Two of them need validated data rather than more of the computation already done: the transition moment, because three methods have been tried against it and disagree, and the low-Reynolds section drag, because the one method used here is least reliable exactly there.

#### What this section amounts to

**The loop closes; the aircraft is not shown to.** At the energy store the paper can name the gap exactly, in specific power and in take-off mass; everywhere else it can name only what would settle the question. **The architecture claim — that the configuration is arranged to change regime with no mechanism that reorients a propulsor — is a count of hardware, and nothing in this section reaches it.** What this section reaches is the aircraft, and the paper has not claimed the aircraft. The last section returns to the four axes of Section 6 and states what is claimed on each.

### 9. Four axes, and where the paper stops

The paper makes its claims on four axes, against four opponents (Section 6), and on each it stops where
its evidence stops.

**Cruise efficiency, against rotorcraft — claimed against multirotors, and bounded; mixed against helicopters.** Cruise lift is carried on a surface
rather than on rotors. The size of the advantage is a calculation, not a consequence of that statement:
positive throughout against one published quadrotor, and from slightly behind to comfortably ahead against
the other (Section 4). Nothing is claimed against rotorcraft on vertical capability.

**Operation without a runway, against fixed-wing aircraft — claimed as sized, not demonstrated.** The
vertical phase was sized with an energy store whose required performance the sources consulted here do not
report as built (Section 8). Nothing is claimed against fixed-wing aircraft on range or cruise efficiency.

**The mechanism required to change regime, against tilting architectures — the contribution.** The
configuration is arranged to change regime by rotating the airframe rather than the propulsors, and so
carries none of the mechanism classes Section 5.1 counts: no pivot, no nacelle or rotor-group actuator, no
variable-pitch hub, no dedicated lift rotors, and — while the tip pairs free-wheel or are held by motor torque — no
rotor stowing, indexing or stopping mechanism (Section 5.1's note). Roll
comes from the strip; the reaction-torque channel the coaxial pairs could provide is declined, and what
declining it costs is not computed. **This is a count of mechanism classes, not a claim that nothing moves, and not a
claim of mechanical simplicity or reliability.** Whether this aircraft completes the rotation is a separate
question, and it is not settled here.

**Range, against the other hybrids — not claimed, in either direction.** The ordering belongs to the sizing
contract (Section 7.4).

**The loop closes; the aircraft is not shown to.** Section 8 lists what would settle the rest. What the paper offers is **a configuration sized to combine
runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism
that reorients a propulsor, and an account of what the combination costs.**

---

*End of Sections 6–9, and of the paper's body. After your answers: the reconciliation of both halves, then the citation map and the pre-submission list.*
