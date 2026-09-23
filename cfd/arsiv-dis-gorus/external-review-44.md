# Round 40 — Step 8 is written. And the author is asking where to go next, not telling you.

---

## 0. Where this stands

Step 8 exists. It is in §3 below in full, and it is this round's object of criticism.

Round 39 closed almost everything. Qwen withdrew a conclusion and explained why the objection
was still worth making; that explanation is in §1 and it is the most useful thing said about how
these rounds work. Two of DeepSeek's findings were wrong, one was right and is fixed, and the
wrong ones taught us something anyway. All of that is §1.

**The author has a request about §4.** The skeleton says step 9 comes next. The author would
like your opinion on what should actually be written next, and asked me to say plainly:

> **We are not obliged to do what you say. But the opinion may be valuable.**

So §4 is a genuine question, not a ratification.

**Verify what you are reading.** `LORDTEK/meryemAircraft`, branch
`claude/ecstatic-cori-6w30at`, commit **`f94f252`**.

```
paper/v8/08-what-it-is-made-of.md  SHA-256 69cd2426c44784cf5b6609534051a97f1e9887ad0b6e917f8247fe9ae139fd3f
paper/v8/07-the-combination.md     SHA-256 ff75d432b7ccf2659ffebd2709940733cdfb9a9d1537789a8e40271f20e1e40e
```

---

## 1. Round 39, closed

### 1.1 Altitude — all four converged, and the answer is two statements, not one

Every one of you said the same thing in different words: **one clause for the cruise-efficiency
channel, a separate line for hover power, because they are different sizes and touch different
parts of the paper.** Adopted exactly.

- **§2.12 gets a clause**: η_p also moves with altitude, because the two-duty gap widens as
  V ~ 1/√ρ at fixed C_L; the computed effect is 2.9 % relative to 3000 m, and it is against the
  aircraft. This repairs the existing sentence *"altitude would move these figures only by moving
  L/D"*, which ChatGPT flagged as now simply wrong and which is the whole reason the author's
  question mattered.
- **The hover-power rise gets its own line where the buffer is sized**: 10.94 → 12.87 kW over
  0–3000 m, 17.6 %. Grok: *"It is Bill 3 and the buffer."* Not a range footnote.
- **DeepSeek's addition is adopted**: the paper must state that the propeller numbers are
  sea-level values. Otherwise a referee asks.
- **Nobody wanted altitude promoted to a skeleton step.** It stays an assumption with a
  quantified sensitivity.

**Qwen decomposed the 17.6 % and I checked it.** Density contributes √(1.2250/0.9093) = 1.1607
and the figure-of-merit drop 0.598 → 0.590 contributes 1.0136; the product is 1.1764 against an
observed 12.87/10.94 = 1.1764. **Agreement to 0.0006 %.** The decomposition is exact, and it
also answers DeepSeek's catch below.

### 1.2 DeepSeek was right once, and the right one was the small one

> *"The FM values are 0.598, 0.601, 0.602, 0.590. The bisection lands within 0.591–0.603. At
> 3000 m the FM is 0.590, which is outside the stated tolerance."*

**Correct.** 0.590 falls just outside the tolerance I stated. It is not a physical altitude
effect on hover quality — it is the seven-iteration bisection, as Grok said it should be labelled
— but the stated tolerance was wrong by 0.001 and a referee reading the table would catch it.
Fixed: the tolerance is restated from the actual runs rather than from the earlier light-design
run. **And per Qwen's decomposition, that 0.008 of figure of merit is carrying 1.36 % of the
17.6 % hover-power rise**, so it is not cosmetic either; it is a small artefact sitting inside a
reported number, and it is now labelled as one.

### 1.3 DeepSeek's two other findings were wrong — and the fact that they were is itself a finding

**Finding 2**, that *"the sign does not turn over on equal fuel fraction"* and *"the reversal is
between the second and third contracts."* The symmetric column reads +21.1 / −5.7 / −42.3 across
**contracts 1, 2 and 3**. The sign turns over between contract 1 and contract 2. Contracts 2 and
3 are both negative, so there is no reversal between them. The comparison was read down the
columns — published against symmetric, which is the same contract under two scenarios — rather
than along the rows.

**Finding 5**, that the step-7 adoption was presented as unanimous. The briefing named the split
first — ChatGPT and DeepSeek for acknowledgment only, Grok and Qwen for the number — and then
adopted. The attribution was there.

**But being misread twice by a careful reader is a finding about the table, not about the
reader.** Both corrections are adopted in substance even though the objections were wrong: the
columns are relabelled *"published configuration, A at 0.80"* and *"same configuration, all at
0.632"*, the reversal is stated as **across contracts** rather than left for the reader to
locate, and the adoption is marked *"on Qwen's argument"*. If one of you misread it, a referee
will.

**Qwen's two flags are adopted as written**, and both are about preventing the same kind of
misreading: the symmetric scenario is a **counterfactual** for testing robustness, not a claim
that B and C actually have η_p = 0.632; and the altitude table is a **sensitivity study of the
sea-level design**, not a redesign for altitude.

### 1.4 Qwen withdrew a conclusion, and said something about method worth keeping

> *"My conclusion was wrong; my objection was valuable. I'd rather have made a wrong objection
> that surfaced a real defect than a correct objection that confirmed what you already believed."*

That is the correct account of what happened and it is worth stating because it is the opposite
of how these rounds usually get summarised. The objection was wrong about the physics and right
about where to look. **An agreement would have left the mis-configured comparison in place.**

### 1.5 Where you split on Qwen's proposed sentence, and what was decided

Qwen's Round 38 sentence — three asserted quantities later computed, all worse, predictions
survived — drew four answers that agree on placement and disagree on wording.

**All four: not in the conclusion.** Grok: *"In the last page of a Journal of Aircraft paper it
reads as a making-of. Referees punish that."* All four: it belongs in the step on what the
framework demands of its user.

**All four: drop "the strongest evidence we have."** Qwen included, about Qwen's own sentence.

**DeepSeek found the clause that is false**, and this is the substantive correction:

> *"'The framework's predictions survived all three' is not accurate. What survived was the
> framework's **structural** predictions… What did not survive was the framework's **numerical**
> assumptions."*

That distinction is right and it is the paper's actual finding about itself. **Adopted in
DeepSeek's form**, with ChatGPT's framing of the point: the claim is not *our numbers got worse
and we survived*, it is *the framework forced the recomputation and made visible which results
moved and which did not.*

### 1.6 Two wording rules from ChatGPT, adopted for everything from here

- **"Computed", never "measured."** Several of these briefings said "measured" for calculation
  results. Nothing here was measured. This is exactly the class of error this project keeps
  making, in miniature.
- **Drop "second-order"** as a term covering both altitude channels, since one is 2.9 % and the
  other 17.6 %. The honest form is ChatGPT's: *the cruise-efficiency effect is modest over
  0–3000 m, whereas the increase in hover power is not negligible for power-system sizing.*

---

## 2. What step 8 is for, and what is deliberately not in it

Step 7 claims that a class of mechanism is absent. **A claim of that kind is only as good as the
inventory behind it.** Step 8 is that inventory, including the parts that move.

Three things are kept out on your own advice, and the page says so at its foot:

- **The propeller-efficiency number.** Grok and Qwen won that argument: it appears once in step 7,
  where the elimination is claimed, and is itemised in the ledger as *the fixed-pitch compromise*.
  Not here. Step 8 is inventory; a refused class's price is not an inventory item.
- **The size of the drag charges.** Step 11.
- **The mass build-up.** Steps 10 and 11.

And one thing is deliberately left unresolved rather than invented: **the number of actuators.**
The paper does not fix it — it describes the strip as deployable in two halves and carries the
actuation in the systems budget without sizing the mechanism. An earlier summary in this project
invented "one strip actuator" and it was wrong. The page now says the study does not fix it.

---

## 3. Step 8, first writing

> ### What it is made of, and what still moves
>
> Section 7 claimed that a class of mechanism is absent. A claim of that kind is only as good as
> the inventory behind it, so the inventory is given here in full, including the parts that move.
>
> ### The airframe
>
> The entire airframe is the wing. There is no cylindrical fuselage: every part of the planform
> carries payload and produces lift. Leading-edge sweep varies continuously along the span while
> the trailing edge is held at 25°, so the realised sweep runs from 45° at the root to 38.3° at the
> tip — a variation of under seven degrees, with the crescent character coming from the curvature of
> the leading edge rather than from a large change in sweep. Thickness runs from 25 % of chord at
> the root to 12 % at the tip, and chord from 0.970 m to 0.236 m. For the light design the span is
> 3.453 m, the wing area 1.979 m², and the aspect ratio 6.03.
>
> Sweep is not a free parameter here, and the reason is structural to the configuration rather than
> aerodynamic preference. The aircraft is tailless. With no horizontal stabiliser on a boom, the
> pitching moment must come from the distribution of lift along the body itself, and sweep is what
> places the outboard sections behind the centre of gravity so they can produce it. **The sweep
> angle and the longitudinal stability are one design variable seen from two directions.**
>
> ### The propulsion
>
> Five propellers, and every one of them is a coaxial counter-rotating pair. The reason is narrow
> and worth stating as such: **reaction torque.** A single propeller applies to the airframe a
> torque equal and opposite to the one it applies to the air — about the yaw axis in hover and the
> roll axis in cruise — and that torque must be opposed continuously, either by a control surface,
> which costs drag, or by differential thrust, which costs a control channel. A counter-rotating
> pair does not produce it.
>
> One pair sits at the nose, 1.20 m in diameter on the light design, and produces all propulsive
> thrust in both regimes. Four smaller pairs, 0.20 m in diameter, sit at the ends of rigid frames
> projecting from the wing tips. Every pair is of **fixed geometry**: no cyclic pitch, no
> collective, no variable mechanism of any kind. Each rotor of each pair is driven by its own
> electric machine on a common axis, so the arrangement that repeatedly defeated the XB-35 —
> concentric shafts, a splitting gearbox, and the governors that synchronise them — is never built.
>
> The counter-rotating arrangement carries a second consequence that the transition analysis
> depends on. Because the two rotors of each pair carry equal and opposite angular momentum, **the
> net angular momentum of the propulsion system is nominally zero**: rotating the airframe through
> ninety degrees precesses nothing, and no gyroscopic moment appears for the control system to
> cancel. In a tilting architecture that term is present and must be designed for.
>
> ### The energy path
>
> A series hybrid: fuel to engine, engine to generator, generator to electric machines at the
> rotors. The engine is not mechanically connected to any rotor. It is an energy source, and that
> decoupling is what allows it to be sized by cruise rather than by hover. For the light design the
> continuous cruise requirement is 1.9 kW at the engine shaft and the engine is rated at 2.6 kW,
> while the hover requirement is 10.9 kW at the rotor. The difference is supplied for the vertical
> phase from a **1.8 kg battery buffer, 3.6 % of take-off mass.**
>
> ### What produces each moment
>
> **Pitch and yaw come from differential thrust between the tip pairs**, and the two axes do not
> have the same authority. The frames project ±0.71 m perpendicular to the planform, so a
> differential between the upper and lower pairs acts at 0.71 m in pitch, while a differential
> between the left and right pairs acts at the semi-span, **1.726 m — 2.43 times the pitch arm.**
> Yaw is therefore the strongest axis on this aircraft, which is the reverse of the usual situation
> and is a consequence of the layout rather than a design choice.
>
> **Roll comes from neither.** Every pair is coaxial and torque-balanced, so every thrust vector is
> parallel to the body axis and no combination of settings produces a rolling moment. Roll is
> produced instead by a strip on the lower surface: inclined at 45° in planform, running 120 % of
> root chord, reaching 67 % of semi-span, and standing 2 cm proud at its inboard end and 6 cm at
> its outboard end. **Extension is the control variable** — the strip is modulated, not switched —
> and deploying it also pitches the nose down by a small increment. Its inboard 46 % lies inside
> the nose propeller's slipstream, where dynamic pressure is set by disc loading and is therefore
> available at zero airspeed; its outboard 54 % works against the freestream in cruise. That split
> is why one device serves both regimes.
>
> ### What meets the ground
>
> The aircraft rests on five points: the four lower ends of the tip frames, and the aft end of a
> keel running along the centreline. It stands on its tail in its own storage attitude, with no
> launch equipment present.
>
> **The tip frames therefore do three jobs at once**, and this is the clearest instance in the
> configuration of one structure carrying several duties: they are the landing gear, they set the
> control moment arms, and they carry the attitude rotors. Lengthening them to buy control
> authority widens the stance base against tipping in wind at the same time. They are also the
> structure that is exposed in cruise, and Section 11 charges them for it.
>
> ### What moves
>
> The propellers rotate, as propellers do, but none of them changes its orientation relative to the
> airframe at any point in the flight. Beyond that, **one thing on this aircraft moves: the strip.**
> It is described as deployable in two halves — one side alone for roll, both together as a speed
> brake. The actuator inventory is therefore the propulsion motors plus the strip's actuation.
> **How many actuators that is, this study does not fix.** The systems budget carries the
> actuation without sizing the mechanism, and naming a number here would be inventing one.
>
> ### What this inventory does not settle
>
> Two items belong here rather than in a later list, because both are properties of the hardware
> just described.
>
> **The torque balance is exact at cruise rather than at hover, so a small residual remains in
> hover.** What trims that residual is not established. It is too small to be carried by the tip
> pairs without spending roll-axis authority the aircraft does not have in hover, and the strip
> works against dynamic pressure that the slipstream supplies over only part of its length. Either
> the residual is absorbed by the speed trim of the pairs — which this study has not shown — or a
> fourth duty falls on the strip.
>
> **The fixed geometry of the tip pairs has a cruise consequence.** Unable to feather, they must
> either turn at the zero-shaft-torque condition or be stopped, and the difference between those two
> states is a substantial fraction of the aircraft's zero-lift drag. Both ends are computed rather
> than assumed, and the charge appears in Section 11.
>
> ---

The page carries, in the repository, a twenty-three-row table mapping every factual predicate to
the source line that supports it. That table is not part of the manuscript; it exists so the
author can audit the page without trusting me.

---

## 4. **The author's question: what gets written next?**

The skeleton's reading order is 1 gap · 2 tax · 3 escape condition · 4 independent NASA check ·
5 first half · 6 second half · **7 combination (written)** · **8 what it is made of (written)** ·
9 what is not claimed · 10 sizing closure · 11 the ledger · 12 bills separate with scale ·
13 rankings belong to contracts, and what the framework demands of its user · 14 what is not
closed · stop on the four axes.

**Writing order need not follow reading order, and two rounds ago you were split on this.**
DeepSeek wanted steps 2 and 3 written early, because step 7 refers to an escape condition that
does not yet exist in v8. The other three wanted step 8, which is now done.

Arguments visible from here, given without a recommendation:

- **Step 9** is next in reading order, and the skeleton puts it deliberately *before any numbers*.
  Writing it now would fix the refusals while the architecture pages are fresh.
- **Steps 2–3** are what steps 7 and 8 both point back to. Step 7's opening sentence refers to
  "the escape condition of Section 3" and that section is unwritten. DeepSeek's argument was that
  writing 7 against an unwritten 3 risks the two not matching.
- **Step 11** now has a ledger entry waiting that did not exist a week ago — the fixed-pitch
  compromise — and three of you said the ledger is where the new number does its work.
- **Step 13** now has the framework-demands paragraph decided in §1.5 and nowhere to live.

The author's words, verbatim: **"We are not obliged to do what you say. But the opinion may be
valuable."** Say what you would write next and why. If you think the question is premature, say
that instead.

---

## 5. What I am asking of you

**Q1 — Does step 8 support the claim step 7 makes?** The test is narrow: after reading this
inventory, can a referee still believe the elimination claim, or does something in the parts list
undercut it?

**Q2 — Is anything missing from the inventory that a referee would expect?** Not the numbers
that were deliberately withheld — a *part*, or a duty with no part assigned to it.

**Q3 — The two unresolved items are inside the section rather than in a later list.** The hover
torque residual, and the tip pairs' inability to feather. Both are properties of the hardware
just described, which is why they are here. Is that the right place, or does putting unresolved
items inside a parts list weaken it?

**Q4 — Anything false.** Every round this question has produced findings. Assume it will again.

**Q5 — §4 above: what would you write next?**

---

## 6. Where the work stands

Two of fourteen steps written. The architecture is unchanged since the skeleton locked. The
propeller calculation cost the paper a number and one published sentence, and gave the third
claim its price. Altitude cost one clause and one line. Nothing has cost the thesis anything.

Target remains *Journal of Aircraft* (AIAA), Full-Length Paper.
