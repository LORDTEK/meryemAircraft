# Steps 2–3 — one semantic inventory (Round 77; before any draft)

Source: `02-the-tax.md` (2 263 words) and `03-the-escape-condition.md` (1 874 words) at commit 6f93b0d; neither step has changed since f425af4. SHA-256: 02 `ce0503fb…4665591`, 03 `9b16a4d8…6016330`.
**P** = protected (verbatim). E1 numbers, E2 inferential evidence. **Home** = where a definition or finding is stated first
(Grok P22). **Restatement** (ChatGPT, DeepSeek): *first* / *necessary repetition* / *removable repetition* — and of what.

## Blocks

| Block | Home | Must say | E1 | E2 | Must qualify | Must not say | Restatement |
|---|---|---|---|---|---|---|---|
| **2A. The root** | 2 | The vertical phase is about two percent of the flight; hardware installed for it alone is carried fifty times as long as it is used. **P** *"is the origin of all three charges below"*. | ~2 % of a one-hour mission; ×50 | It is a statement about duty cycle, not quality: a lighter or cleaner lift rotor is still carried. | **P** *"A claim that one architecture escapes a cost shared by the others is only meaningful if the cost is stated first, in terms that do not presume the escape."* **P** *"The statement is deliberately confined to architectures with a dedicated lift subsystem."* *"It is not a claim about any particular aircraft, and nothing in it is new physics"* (not P; must survive in substance). | That the mismatch is an implementation defect; that any architecture is shown here to avoid it. | first |
| **2B. Bill 1 — mass** | 2 | A dedicated vertical group is dead mass in cruise, and its cost is not linear. | MTOW = m_payload / (1 − f_empty − f_energy); hover power ∝ W^1.5 at fixed disc area | The multiplier grows as the denominator shrinks, and the increment is charged again in hover (**Step 4's first half is derived from this**). NASA sizing study: lift-plus-cruise the heaviest because of *"the extra empty weight items on board in hover"*, although its effective L/D is the highest — aerodynamically better and still the heaviest. NASA review: power to the extremities needs *"very strong (and fatigue-resistant) structures … with an obvious weight penalty."* | The exponent is a property of the scaling rule (constant disc loading makes hover power linear in weight — **Section 12 uses that**). | That the NASA study uses this accounting. | first |
| **2C. Bill 2 — drag** | 2 | Hover hardware left exposed in cruise is charged in drag; its property is where it falls — per unit time in cruise. | — | Wind tunnel: *"the drag produced by the motors is significant."* Quadplane: drag in the hybrid regime above either pure mode; a simulation assuming negligible rotor–structure interaction *"always predicts higher lift and lower drag than were experimentally observed"* (**Step 11 relies on this quote**). Twenty-six edge-on lift propellers: drag with frontal area and airspeed squared; *"a significant amount of aerodynamic drag"* without stowing. **The wind-tunnel campaign itself is the one Step 13 takes its 17 / 13 ratio from.** | What is charged is the part attributable to hardware retained for a finished phase, not all cruise drag. | That the size of this charge is established here. | first |
| **2D. Bill 3 — power sizing** | 2 | Power installed for a hover peak held for a minute is carried unused for an hour; the ratio follows from the governing equations. | P_hover/W = √(DL/2ρ)/η_h; P_cruise/W = V/((L/D)η_p); the ratio; example DL 100 N m⁻², L/D 15, 30 m s⁻¹ → 3.2 geometric, about 4 with η_p/η_h; tail-sitter measures one fifth | The right-hand side depends on configuration and operating points, not on hover duration; η_h and η_p are not constants (**Section 11 computes** the fixed-pitch case). Sizing by hover returns to Bill 1 as installed mass. | "Between three and four times" belongs to that example. *"often the largest"* is an unsourced comparative: keep it as the source has it, or drop it; never strengthen it. The tail-sitter's one fifth is *"the ratio this expression gives for an aircraft of that class"*, not a fit. | That the ratio is a design choice; that Bill 3 is shown to be the largest. | *"two percent"* = **necessary repetition** of 2A (it is the premise of the sizing argument) |
| **2E. Coupled; the transfer table** | 2 | Each known partial remedy reduces one charge and raises another; three distinct currencies. **Table stays in the body (B7).** | Retraction experiment: 30 % of airframe drag removed; 5 % mass; range 119 → 121 km | **The transfer is the point rather than the small residue** (Bill 2 converted almost exactly into Bill 1). | **P** *"they are not assumed to be independent physical causes"*; whether size moves them together is **tested in Section 12**. The tilting row: Bill 3 left standing; mechanism **not among the three**. **P** *"The table is not a census of the field…"*. The doctoral study, not the journal article, reports the comparison. | That the table lists every move; that the tilting mechanism is free. | *"One row does not pay in any of the three currencies…"* **restates** the tilting row → candidate **removable repetition** (the table row and 2F's clarification both carry it) |
| **2F. What the accounting is for** | 2 | *"The moves in the table are partial remedies: each accepts the duty-cycle mismatch and then redistributes what it costs."* Whether an architecture can **decline** the mismatch rather than redistribute it is a different question (**the pivot to the contribution; home of *decline vs redistribute***). The accounting is refuted by a remedy that reduces one charge, leaves the others no worse and adds no cost of its own — measured in the same currency. It predicts that a ranking moves toward the lighter arrangement when the sizing rule weights mass more, and reverses past break-even (**Section 13 tests it; Section 4 tests a different consequence**). | — | The same-currency clause is what makes the test usable. | **P** *"The accounting claims transfer. It does not claim that every architecture is equally good."* **P** *"A remedy whose cost falls outside the three charges does not refute the accounting…but it is not thereby exempt from being counted."* **P** *"A framework that could absorb any cost by declaring it out-of-scope would be unfalsifiable."* | That the accounting ranks architectures. | The first refutation sentence and its *"Stated positively…"* restatement → candidate **removable repetition** (keep the usable form). Last paragraph = bridge to Step 3; its *"derived from the table above rather than from any aircraft"* is restated in 3A |
| **3A. Opening** | 3 | The condition is a **definition**, derived by inverting the table, stated before any configuration so the standard is not taken from what it measures. | — | — | — | That it is derived from the aircraft. | **Restates** 2F's last paragraph: *"The previous section listed moves that redistribute the three charges. This one asks a different question"* ≈ 2F's *decline vs redistribute*; *"derived by inverting the table rather than by describing any aircraft"* ≈ 2F's *"derived from the table above rather than from any aircraft"*; *"stated here before any configuration"* ≈ 3F's *"not retrofitted"*. → **removable in part**: 3A keeps *definition* and *by inverting the table* (new job: names the method of 3B) |
| **3B. Inverting the table** | 3 | Four departures, each a way to pay: different hardware (Bills 1, 2); same hardware, one duty (again 1, 2); same hardware, both duties, different orientation (the tilting family: Bill 3 unless a store, plus the mechanism); one orientation but a different sizing point (Bill 3). Read as a conjunction, they are a condition. | — | The second departure is separate because *"serving both duties"* decides which parts of a configuration meet the condition (thrust that supports weight and thrust that balances drag are not one job). | — | — | **Restates** the table rows of 2E in departure form (**Qwen P1**) → the primary compression target: state the four departures once, derive the condition |
| **3C. The condition** | 3 | **P** *"An architecture does not incur the three charges if the propulsors that carry the weight … produce both the hover thrust and the cruise … is supplied from a store rather than from permanently installed continuous power."* Four parts: **same hardware, both duties, one orientation, hover peak from a store** (**Step 8: "The nose pair meets all four parts of Section 3"**). | — | — | Two choices are not derivations: *how* one orientation is kept (by rotating the body, or otherwise) is exposition; a store is the narrower reading of "any source other than continuous power". | That rotating the body is part of the definition. | first |
| **3D. What it does not say; permitted costs; one exclusion** | 3 | The name means zero of the three charges as Section 2 defines them, not zero cost. Six permitted costs, named before any candidate: the store (same duty-cycle character as Bill 1); the electrical path; rotating the airframe; hardware serving both duties; attitude hardware (in both regimes, not cruise thrust; Bill 2 reaches it — partial instantiation); the one-blade compromise (Section 11 measures it). One exclusion: parts present for other reasons, not the tip frames. | — | A definition that placed every cost inside the thing escaped would be unfalsifiable; one that won by construction would not win by performance. | **P** *"It means zero of the three charges as Section 2 defines them…It does not mean an architecture that costs nothing"*; **P** store … *"It does not claim the trade is favourable."*; **P** *"Releasing the engine is not releasing the electrical path."*; **P** *"Rotating the airframe is permitted and is not priced here."*; **P** *"Serving two regimes with one set of hardware has a price of its own…The condition permits that cost and does not measure it."* Tip frames: mass in the build-up, drag in the ledger. **Steps 11 and 14 rely on the store clause; Steps 8 and 9 on the attitude-hardware clause.** | That the condition makes anything free; that rotating the airframe costs nothing. | The dash-gloss after *"as Section 2 defines them"* (*"the mass of a dedicated lift subsystem, the cruise drag … and continuous power installed to a hover peak"*) repeats 2B–2D → by Grok P22 **removable** (the pointer does the job; the gloss sits inside the ellipsis of the protected row, so dropping it is D, not a change to P). 3B's *"the unused set is carried for the whole flight and, if exposed, drags"* likewise. *"two percent of the flight"* → necessary (store duty cycle). The attitude-hardware bullet anticipates 3E's modes 1 and 4 → check at drafting |
| **3E. How the condition can fail** | 3 | Four failure modes: (1) a propulsor carried through cruise producing no cruise thrust; (2) a propulsor reoriented to change regime; (3) continuous power sized by hover; (4) **partial** instantiation — the first three met only in part, and the failing part re-opens its charge. | — | Mode 4 is why the list exists: a paper reporting only where the condition is met would report the condition, not the aircraft. | **P** *"An architecture may meet the condition where it carries the aircraft and fail it elsewhere"*. **Outbound lock (Qwen P3): the wording and numbering of the four modes are cited by Steps 7, 8 and 9 (*"the first of Section 3's failure modes"*, *"its fourth failure mode"*) and may not change.** | — | first |
| **3F. What follows, and what does not** | 3 | The condition is a definition; three questions answered elsewhere (Step 4 the accounting; Steps 5–7 whether anything satisfies it; Step 11 what it pays). A tilting architecture accepts the third departure and buys its way out with a mechanism, so it does not satisfy the condition as written; whether it avoids the charges another way is not settled. Stated before the configuration: not retrofitted. | — | — | **P** *"It is not a claim that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim that satisfying it is desirable."* **P** *"An architecture that reorients a propulsor does not satisfy the condition as written…the condition is a definition, not a law…"* **P** *"Whether such an architecture might avoid the three charges by some other route is a separate question this paper does not settle."* | That tilting architectures incur the charges; that the condition is a law. | The tilting consequence **restates** 2E's row and 3B's third departure → one home suffices for the *mechanism* statement; the *does-not-satisfy-as-written* statement is first here |

## Outbound dependencies — what the rest of the paper takes from Steps 2–3

| Taken by | What | From |
|---|---|---|
| Step 1 | *"Section 2 states the cost … in terms that do not presume an escape"* | 2A (P) |
| Step 4 | The first half of the prediction: amplification through the MTOW multiplier and the hover charge; the transfer property; *"the actuation, the gyroscopic coupling and the transition control problem that Section 2 assigns to that family"* | 2B, 2E (tilting row) |
| Steps 5, 6, 9 | A runway aeroplane *"pays none of the charges of Section 2"* | 2A–2D |
| Step 6 | *"the mass charge Section 2 describes"* | 2B |
| Step 7 | *"the escape condition of Section 3"*; *"Section 3 lists partial instantiation among the ways an architecture can fail"*; the four parts in its own words (*"same hardware, both duties served, one orientation, hover peak from a buffer"*) → **the four parts of 3C are locked with the four modes** | 3C, 3E |
| Step 8 | *"The nose pair meets all four parts of Section 3"*; *"the first of Section 3's failure modes"*; *"its fourth failure mode"*; *"Section 3's permitted-cost clause"* | 3C, 3E, 3D |
| Step 9 | Partial instantiation; the declined condition in the attitude system | 3D, 3E |
| Step 11 | *"Section 2 named three charges"*; Bill 2 *"in the terms Section 2 defined it"*; the simulation quote; *"Section 3 said in advance that this would happen"* (the store) | 2B–2D, 2C, 3D |
| Step 12 | *"the framework of Section 2"*; the constant-disc-loading exponent; *"the separability Section 2 asserts"* (see S-3); *"as Section 3 anticipated"*, *"Section 3's claim"* (the store coupled to Bill 3) | 2B, 2E, 3D |
| Step 13 | The wind-tunnel campaign *"quoted in Section 2"*; Section 2's prediction, tested; *"the tilting family as Section 2 describes it has no store at all"* | 2C, 2F, 2E (tilting row) |
| Step 15 | **Nothing.** Qwen P3 lists Step 15 among the citers of the failure modes; it does not cite Section 3 (searched). | — |
| Step 14 | *"the escape from Bill 3 … in the sense Section 3 defined it"*; the conversion the condition permits | 3C, 3D |

## The restatement map, in one place (P22)

| Content | Home | Also stated in | Status |
|---|---|---|---|
| Two-percent duty cycle | 2A | 2D, 3D | necessary (premise of 2D; store duty cycle in 3D) |
| The tilting row: Bill 3 standing; mechanism outside the three | 2E table | 2E *"One row does not pay…"*; 2F clarification; 3B third departure; 3F | **removable** in part — keep the table row, one clarification and 3F's *"does not satisfy as written"* |
| The table as source of the condition | 2E | 2F last paragraph; 3A; 3B | **removable** in part — one bridge suffices |
| The three charge definitions | 2B–2D | 3D (the name) | necessary |
| Refutation test | 2F | 2F *"Stated positively…"* | **removable** in part — keep the same-currency form |
| *Decline* vs *redistribute* | 2F last paragraph | 3A first two sentences | **removable** in 3A |
| Derived from the table, not from an aircraft | 2F last paragraph | 3A | **removable** in one place; 3A's *"by inverting the table"* names 3B's method and stays |
| Stated before any configuration / not retrofitted | 3A | 3F | **removable** in one place (open: which) |
| The three charges glossed | 2B–2D | 3D dash-gloss; 3B *"carried … and, if exposed, drags"* | **removable** (Grok P22) |

**Rule for this column (Grok P22 with ChatGPT's exception).** A statement kept in two homes is restatement and is the cut —
**unless** the second occurrence does a job the inventory names (the two-percent in 2D is the premise of the sizing argument; in
3D it is the store's duty cycle). A repetition that cannot name its job is removable. A draft that keeps **neither** home is a
first-occurrence halt.

## Source-level issues the inventory surfaced (not drafting changes; for your view)

**S-1. The table's mechanism rows do not follow one rule.** Folding mechanism → Bill 1 (*"1 — mechanism, actuation,
locking, …"*); pitch hub → Bill 1 (*"1 — pitch hub, actuation, …"*); tilting mechanism → *"not among the three"*, though 3B
says it *"adds mass"*. Two rules are available in the text, and the table follows neither:
- **Duty cycle (2A's root):** hardware needed briefly and carried for the rest. Folding mechanism and tilt pivot are used at
  the transitions only → both Bill-1-like; the pitch hub retrims in both regimes → not. The **tilt row** is the odd one.
- **Lift-subsystem mass (2B; 3D's gloss; Step 11: *"not lift-subsystem mass, so it is not Bill 1 as Section 2 defines
  it"*):** the folding mechanism belongs to a dedicated lift group → Bill 1; neither the pitch hub nor the tilt pivot does.
  The **pitch-hub row** is the odd one.

The paper applies the second rule twice already (the store in 3D, the buffer in Step 11), each time adding that the excluded
mass carries Bill 1's complaint (3D: *"the same duty-cycle character as Bill 1"*; Step 11: *"which is the complaint Bill 1
makes"*). Options, none applied: (a) duty-cycle rule — tilt mechanism mass to
Bill 1; reopens 2E *"One row does not pay…"*, 3B, and closed Step 4 (*"The tilting family avoids it too"*, *"it moves the
charge — to the mechanism"*, #18); (b) state a principle for the current assignment; (c) lift-subsystem rule, applied as the
paper applies it elsewhere — the pitch-hub row's mass leaves Bill 1, and the tilt row says, as 3D says of the store, that
its mechanism mass has Bill 1's duty-cycle character without being Bill 1. (c) touches 2E only (the pitch-hub row, *"One
row…"*, the tilt row); Step 4 is untouched.

**S-2. An unclear antecedent in 3F.** *"A tilting architecture accepts that departure and buys its way out of the first with a
mechanism."* *"The first"* is most naturally *the first departure*; the table says the tilting row attacks **Bill 1**. One
of the two is meant; the draft must name it (R, vetoable).

**S-3. Step 12 says *"the separability Section 2 asserts"*.** Section 2 asserts three distinct **accounting** quantities and
says explicitly that they are *"not assumed to be independent physical causes"*; whether size moves them together is left to
Section 12. *"Asserts separability"* may be stronger than Section 2. Step 12 is not being drafted now; noted so it is not lost.

## Round 77 additions — who asked for what, and where it is

| Proposal | Where |
|---|---|
| Grok P22 — mark every charge definition with its home; both homes kept = cut; neither = halt | **Home** column; rule above; the gloss rows |
| Grok P23 — object check on 687 / 679 in the assembled view | done: one paragraph (Section 2.3), 687 lb = design gross-weight difference (*"the net difference between two architectures"*), 679 lb = empty-weight difference; not mixed |
| ChatGPT — first / necessary / removable repetition | **Restatement** column |
| DeepSeek — *"restatement of"* named; a cross-step flag in the trace | **Restatement** column names what is restated; the trace will carry a cross-step flag column |
| Qwen P1 — the inversion as the primary target | 3B row |
| Qwen P2 — the qualification-lost column made permanent; a lost qualification must point to where it is covered | trace column, for this and every later section |
| Qwen P3 — the four failure modes locked | 3E row; extended to the four parts of 3C (Step 7 names them) |


## Round 78 — decisions, and what the Bill 1 test found

**Agreed by all four and Claude (applied to this inventory):** the restatement rule (default: two homes = cut; a second home
stays only with a named job); *"stated before any configuration / not retrofitted"* — **home 3A**, 3F removable; the P3 lock
covers the four parts of 3C; S-2 — *"the first"* is **the first departure**, named by an R sentence when 3F is drafted; S-3 —
*"the distinctness Section 2 asserts"* when Step 12 is next opened (`paper/deferred-decisions.md`). **Protected (155):**
*"Whether an architecture can decline the mismatch itself, rather than redistribute its consequences, is a different question"*.

**Outbound row added (Grok):** Step 11, *"not lift-subsystem mass, so it is not Bill 1 as Section 2 defines it"*; with 3D's
*"It is not Bill 1 as Section 2 defines it — it is not lift-subsystem mass"*, two sentences that say Section 2 defines Bill 1
as lift-subsystem mass.

**No drafting of Steps 2–3 until S-1 is settled** (ChatGPT HOLD; Grok P25).

### ChatGPT's test: does Section 2 define Bill 1 as lift-subsystem mass?

**Not explicitly.** 2B defines Bill 1 by its example — the lift-plus-cruise *"vertical group"*, which *"provides no required lift
or thrust during cruise and is lifted anyway"* — and 2A confines the charges to *"architectures with a dedicated lift
subsystem"*. The explicit phrase *"lift-subsystem mass"* appears only in 3D and Step 11, each saying that is how **Section 2**
defines it. And 2B's structural paragraph charges to mass the structure that distributes *"lift or thrust"* — broader than a
lift subsystem.

**And the text uses two vocabularies.** 2E: *"three distinct accounting quantities — kilograms, drag counts, installed kilowatts
… a remedy can move a requirement from one **currency** into another."* The **charges** are specific payments; the
**currencies** are units. The table's right-hand column mixes them:

| Row | Attacks | Creates, as written | Currency the created cost is paid in | That charge, by the lift-subsystem rule? | Who depends on it |
|---|---|---|---|---|---|
| Distributed electric lift rotors | 3 | 1 and 2 | kg; drag | yes; yes | — |
| Folding or retracting | 2 | 1 — mechanism, actuation, locking, … | kg | yes (on the lift group) | the retraction experiment (2E) |
| **Tilt** | 1 | Bill 3 standing; gyroscopic coupling, transition control *"not among the three"* | **kg for the pivot and actuators — absent from the row**; 3B: *"adds mass"*; S4: *"propulsion returns 146 lb of it because the tilt-wing's mechanism is heavier"* | no | Step 4 (*"moves the charge — to the mechanism"*; #18), Step 13, 3B, 3F |
| **Variable pitch / feathering** | 1 and 3 | **1** — pitch hub, actuation, … | kg | **no** | Step 11 (no variable-pitch counterfactual) |
| Higher disc loading | 1 and 2 | 3 | kW | yes | Step 12 |
| Lower disc loading | 3 | 1 and 2 | kg; drag | yes where the rotors are a lift group | — |

**The pitch-hub row writes the currency (*1* = kilograms); the tilt row writes the charge and omits the kilograms.** Hence
*"One row does not pay in any of the three currencies"* is false under 2E's own definition of the currencies: the tilt
row pays the pivot in kilograms (3B; S4). **This holds under (a), (b) and (c) alike.**

**Claude's error, Round 77:** option (a) was said to reopen Step 4 in three places. Wrong: Step 4's sentences say the mass
charge *moves to the mechanism* — the mechanism pays in kilograms. Step 4 contradicts the current tilt row, not (a). S4's
146 lb was in a file Claude built.

### Candidate (d): name the charge and the currency apart (not applied; Round 78 vote)

Three changes, all in 2E. Before → after in the Round 78 text §3. Predicate ledger:

| New predicate | Narrower / broader than the source? | Already in the text? |
|---|---|---|
| A charge and its currency are not the same thing | new distinction; narrows *"One row does not pay in any…"* | 2E names currencies; 3D and Step 11 use the charge |
| Bill 1 is lift-subsystem mass, in Section 2 | makes 3D's and Step 11's *"as Section 2 defines it"* true | 3D, Step 11 |
| The tilt pivot and actuators are paid in kilograms and are not lift-subsystem mass | admits a cost; against the configuration's side of the comparison, not for it | 3B *"adds mass"*; S4 146 lb; Step 4 *"moves the charge"* |
| In the right-hand column a number names the currency | describes the table | pitch-hub row already does it |

### S-5 (a question, not a finding): does 2F's own test hold up against Step 4's tilt-wing?

Under (d) — and already today, since S4's kilograms are data — the tilt-wing's mechanism mass and the lift group it replaces
are in one currency, so 2F's positive test is runnable on it: in the published breakdown the mechanism returns 146 lb of a
716 lb structural difference. 2F's positive form asks that the other two charges be *"no worse"*; its clarification says a
remedy that *"simply leaves another standing is not a counter-example — the tilting row is the case"*. **Those two sentences
turn on whether *left standing* is *no worse*, and the text does not say against which baseline.** Claude has not checked how
the NASA categories map onto the charges. Open.

## Round 79 — (d) content agreed by all four; final wording package to vote

Content of A, B, C: all four accept. Grok's two conditions (definition must not read as 2A's; *"1 in kilograms"* repeats the
mix) → nothing applied; package **A′, B′, C, C4 (pitch-hub cell), C5 (folding cell), H (header)** in the Round 79 text §2.
ChatGPT's pre-draft invariant run on the table as the package would leave it: six rows pass except the tilt row's Bill 3
(S-5). Step 4 *"moves the charge"* → *"moves the cost"* (Qwen) to vote (Grok: loose; ChatGPT, DeepSeek: fine).

**S-5 sharpened:** Step 4's isolated pair shares *"the turbo-electric propulsion architecture"*. If both size continuous
plant by hover (unchecked), *left standing* = *no worse*, and Step 4's *"giving part of the structural saving back"* has the
form of 2F's counter-example in kilograms. The row then stands only on *"a remedy whose cost falls outside the three charges
does not refute the accounting"*. Unchecked: NASA category mapping; plant sizing. **No 3B draft until S-5 is settled.**

## Round 80 — (d) applied; S-5 wording to vote

Applied (four readers + Claude): A′, H, C5, B′, C4, C in `02-the-tax.md`; Step 4 *"moves the cost"*. Retired: *"does not pay
in any of the three currencies"*, *"moves* the charge"*. P29 six-row check on the assembled view: passes. Step 2 2 263 → 2 433
words (content change). S-5 wording S5-1..S5-4 in the Round 80 text §2; baseline = the architecture the move modifies (all
four); diagnosis conditional only (Grok, ChatGPT). 3B draft after S-5.

## Round 81 — S-5 applied; pre-draft invariant extended

Applied (four + Claude): S5-1..S5-4; S3 row propagated (and the Round 65 "complexity" removed there); S5-2's last clause
protected (156); S4 frozen copy carries a note outside the frozen text. **Pre-draft invariant (every table):** row → modified
architecture → cost → currency → bill or outside → where defined. **3B trace columns:** charge / currency / outside flag;
relative-word flag (*left standing*, *still*); qualification lost; cross-step flag. To vote: S5-1′ (*left no larger* /
*enlarged*), protection of S5-2's condition, Step 4 *"The tilt-wing is consistent with the transfer property"*.

## Round 83 — 3.1 applied; 3B snapshot, draft, trace

3.1 three-sentence form applied (four + Claude). 3B snapshot `03B-snapshot.md` (271 words, sha256 `4ca6fe342462244c…`),
draft in `03-draft.md` (3B only; 247 words, −9 %). R1 (four properties; *wherever* for *because*), R6 (*leaves* → *incurs*),
D3 (gloss), D8, D9. **S-6:** the source names three properties and lists four departures; R1 repairs it inside 3B. The
expected restatement saving in 3B was over-estimated: Qwen P2 (Round 78) keeps 2E and 3B as two views.
