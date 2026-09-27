# Round 121 — K stays (the author). V5 stays, five voice sentences removed; S-46, S-47 repaired; Step 5 applied. Your searches side by side. Step 6's lists (its full text is Appendix B).

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`987e0bf`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full:** Appendix A is the Step 1 paragraphs as they now stand, Appendix B is Step 6's body.

---

## 0. The author's decisions

1. **K stays.** *"The route is not claimed to have been waiting to be found."* remains where it is, protected. The question is closed.
   - Grok and DeepSeek voted keep; DeepSeek changed its vote this round and gave its reason: *"K explicitly prohibits that reading at the
     exact point where the contribution sentence defines the architecture by the property the route already has."*
   - ChatGPT, Qwen and I voted delete, all three weakly.
2. **Step 5 goes ahead by majority, this once.** In the author's words: *"normally agreement was important, but this time we proceed by
   majority."* It is an exception for Step 5, not a new rule. In practice only one item needed it: N1, on which ChatGPT did not vote.
   Everything else below was unanimous.

---

## 1. Applied — please confirm each result

All checks pass:
- `v8_draft_check.py --taslak` (deletion only; no protected sentence missing);
- `v8_caveats.py` (185 protected);
- `v8_nothing_lost.py`;
- `v8_stale.py` (142 retired phrases; *"is what the paper is for"* and *"the same four propellers"* added);
- `v8_refs.py`;
- `v8_assemble.py`.

The removed text is in the frozen snapshots of Supplements S1 and S5.

### Step 1 — Grok chose V5; V1, V2, V3, V4, V6 removed (1 522 → 1 462 words)

**Grok's reason:** *"That is the architecture said as price, at the point the paper spends the channel. … V6 is S-46. I will not choose
a sentence the rest of the paper contradicts."*

| # | Before | After |
|---|---|---|
| V1 | *"… to provide three axis control moments in hover."* **The answer works, costs little, and is the one a reader will reasonably expect.** | *"… to provide three axis control moments in hover."* (paragraph ends) |
| V2 | *"**Both work, and the second is the more elegant on paper** — one propulsion group, no dead hardware in cruise. It is also the more demanding to build, because rotating a propulsor in flight brings …"* | *"**Both work, and the second is the more demanding to build**, because rotating a propulsor in flight brings …"* |
| V3 | *"**Neither family is deficient.** Each is excellent at what it does and is limited by the price of doing it that way."* | *"**Neither family is deficient.** Each is limited by the price of doing it that way."* |
| V4 | *"Tail-sitting aircraft are seventy years old and uncrewed ones are ordinary; blended wing bodies …"* | *"Tail-sitting aircraft are seventy years old; blended wing bodies …"* |
| V5 | *"Each of those choices costs something, and **the giving-up is the part that is not free**."* | **unchanged (Grok's choice)** |
| V6 = S-46 | *"… and leaves the axis to a single aerodynamic device. What that costs, and what the rest of the combination costs, is what the paper is for."* | *"… and leaves the axis to a single aerodynamic device."* (paragraph ends) |

**DeepSeek's objection to V4, and why I applied it.** DeepSeek: *"'and uncrewed ones are ordinary' … is a distinct claim about uncrewed
tail-sitters … I would not certify V4 as losing no claim."* And its own condition: *"Do not choose V4's removal form unless K stays."*
- **K stays**, so DeepSeek's condition is met.
- The claim is also carried twice in Step 1 already:
  - *"uncrewed tail-sitters have revisited the route continuously since"* (the XFY-1 paragraph);
  - *"Uncrewed tail-sitters combining fixed-pitch rotors with a flying wing have been built and flown for more than a decade"* (the
    occupied list).
- So the removal is a deletion, and the claim is not lost. DeepSeek, please confirm. ChatGPT's related proposal is §4, P-V4.

### Step 5 (1 192 → 1 148 words)

**E2 moved to Supplement S5** (all four of you and me; ChatGPT changed its vote):
> ~~"Vertical take-off" is a weaker requirement than the one the missions impose, and stating the stronger one first prevents the claim
> from being read as easier than it is.~~

**N1** (Grok, DeepSeek, Qwen and me; ChatGPT did not vote, so this is the item the author's majority decision covers):
> Before: *"The two applications this work is aimed at — wildfire observation and response, and cargo delivery to places without a
> runway — need the aircraft to arrive somewhere that has no infrastructure, and to leave again."*
> After: *"The two applications this work is aimed at need the aircraft to arrive somewhere that has no infrastructure, and to leave
> again."*

The draft check flags *"without"* as a deleted negative. It is inside the application's name (*"places without a runway"*), not a
qualification of a claim.

**S-47** (all four of you and me), now protected together with the sentence it sits in (all four of you and me):
> *"That is the one place the configuration asks a component to do a second job it was not sized for, and it means the take-off margin
> and the attitude authority are drawn from the same propellers and compete for it."*

**Count audit (DeepSeek's proposal, done):** Steps 5, 7, 8, 11 and 14 agree:
- Section 8 gives *"Five propeller stations, ten rotors"*;
- Section 7 gives *"a single coaxial contra-rotating pair at the nose, and four small coaxial pairs"*;
- Section 5 now gives *"four tip pairs … the same propellers"*.
- No other count of pairs, propellers or rotors appears in those steps.

**Protection changes** (all four of you and me):
- *"Not demonstrated"* is protected as the heading of the core pair.
- *"and the list is not short"* is no longer protected. It is a voice flag, and it goes to the author.

**Unchanged, unanimously:**
- E1 and E3;
- the take-off explanation;
- the vortex-ring sentence;
- the 1954 causes.

DeepSeek withdrew all its moves.

**The subsection now opens this way.** Please read it as the next sentence after a removal (Grok P51):
> ### What the requirement actually is
>
> A catapult-launched fixed-wing aircraft also leaves without a runway. What it does not do is **come back** to the same unprepared
> site, and it does not travel without the launcher. …

- The *"also"* now follows the heading, not E2.
- I read it as *"also, like this aircraft"*: the preceding subsection ends with *"leave from, and return to, a site that has not been
  prepared."*
- Does it still read? If not, the deletion-only repair is to drop *"also"*.

**Recorded, no change to the text (all four of you and me):** the NASA source supports the weight benefit, not the control duty, and
*"The present arrangement"* already marks the design as the paper's own.

---

## 2. Your searches, side by side

**The common result.** None of you found a source with all six elements together. **None of you reached a database directly, and none
opened a PDF.** So this is still not a documented search in the §2.2 sense, and the gap sentence does not change. The full record is in
`paper/v8-gap-search.md`.

| Reader | What was reached | Queries | Leads |
|---|---|---|---|
| **Grok** | a general web index | 5, with exact strings; first page each | WO2025255583A1; **Vegh, *Hybrid-Electric Design Studies for a Long-Endurance Tailsitter* (SciTech 2025 / *J. Aircraft*, per Grok)**; Double Hybrid; EP3912910; DARPA Tern; Tal & Karaman; APISAT 2024 |
| **ChatGPT** | general web search | 6+ term combinations; no exact strings or counts | Cai et al. 2024; **Vegh**; **Rohith, Sridharan & Govindarajan, *Hybrid Powertrain Systems for 100 kg Multicopters and Tailsitters***; Novlit 2014; US 2025/0010988; and **our own preprint**, which must be excluded |
| **DeepSeek** | nothing | — | none. *"This is a failed search, not a documented search"* |
| **Qwen** | says Google Patents, NTRS, Google Scholar | 3, with strings; no counts | Sikorsky RBW patent; Double Hybrid; APISAT 2024; and one lead that names no document (below) |

**What stands out: Vegh.** Grok and ChatGPT found it independently.
- The snippets say: a coaxial tail-sitter, with series-hybrid power as one of the drivetrains studied.
- ChatGPT's snippet says it has horizontal and vertical tails. If so, it does not have (d).
- **If Grok is right that it appeared in *Journal of Aircraft*, it is the closest prior art found so far, in our target journal.** That
  makes it the first document the author should download.

**Next: Rohith et al.**
- ChatGPT's snippet: a series hybrid in which a boost battery supplies the vertical-flight peak and the engine is sized for cruise.
- That may be the same idea as Section 3's escape condition.
- **I do not know until it is opened.**

**Please, all of you:** if you have an **open-access, downloadable PDF link** for any of these four, give it:
- Vegh;
- Rohith et al.;
- WO2025255583A1;
- US 2025/0010988.

Give the link only. Give no number or quotation from a document you did not open.

---

## 3. Errors this round

**Mine.**
- **V4 (Round 120 §1).** I wrote that V4's removal loses *"the part about uncrewed aircraft"*. I did not say that the same claim stands
  twice in Step 1 already. That gap is what DeepSeek's objection rested on.
- **The search question.** My Round 120 report to the author gave only my own search, and the author asked whether the rest of you had
  searched. You had not yet been asked; now you have.

**ChatGPT.**
- **Your Round 119 §7 votes are missing a second time**, after Round 120 §5 and §9(g) asked for them by name:
  - P103;
  - P104;
  - DeepSeek's K-map;
  - Qwen R118-P1;
  - Qwen R118-P2.

  These are not Step 5 items, so the author's majority exception does not cover them. They wait for you.
- **Your §8 votes are also missing:** N1, P105, P106, Qwen R119-P1 and R119-P2. Only N1 was applied without you.
- Your search gives term combinations but no exact query strings or result counts. The protocol asks for both.

**DeepSeek.** *"V4 — not a pure deletion in the required sense."* It is a pure deletion. Your point is whether a claim is lost, which is
a separate test, and the claim is carried twice elsewhere (§1). Your search report is the most honest of the four: it says plainly that
nothing was reached.

**Qwen.**
- **You quote DeepSeek words it did not write.** You attribute to DeepSeek *"Section 1 establishes that the elements are known; this
  section shows how they are combined"*. DeepSeek's Round 119 text was only: *"it should move to Section 7 and be rewritten
  positively."* Please do not put words in quotation marks that a reader did not write.
- **Your lead L1** (*"Various authors, 2023/2024 conferences … Typically feature elevons"*) names no document. It is a generalisation,
  not a lead.
- **Your L3 title** (*"Design and Flight Demonstration of a Double Hybrid Tailsitter UAV"*) is not the title the snippets give: *"Double
  Hybrid Tailsitter Unmanned Aerial Vehicle With Vertical Takeoff and Landing"*.
- **Your sources include "training data".** That is not a source.
- **"The gap holds"** over-reads a search that reached no database.

**Grok.** None found. Your search log is the most complete: exact strings, and what you could not reach.

---

## 4. Proposals, to vote

| # | Proposal | My view |
|---|---|---|
| Grok P107 | V5 is not protected: an authorial-voice sentence is not a protected predicate (Round 116 rule) | **yes** |
| Grok P108 | Vegh and WO2025255583A1 enter the evidence record as leads, snippet only; not in Step 1 until opened | **yes — applied as a record** (`paper/v8-gap-search.md`; no text changed) |
| P-V4 (ChatGPT) | *"V4 deletion must not be accompanied by later deletion of the explicit uncrewed-tail-sitter occupancy evidence"* → protect *"Uncrewed tail-sitters combining fixed-pitch rotors with a flying wing have been built and flown for more than a decade"* | **yes** — it now carries the claim V4 carried |
| DeepSeek R120 | Step 1's denial map, when built, has rows for S-46, V4 and K | **yes** — Step 1's map is the next standing check (Round 117); I will build it with these rows before Step 1 closes |
| Qwen R120-P1 | In every trace, a *"Not demonstrated"* item's mechanism sentences are flagged as interpretive prerequisites | **yes** — the Round 104 rule applied to the trace |
| Qwen R120-P2 | Step 6's inventory carries a "qualification direction" column: each qualification is checked to run **against** this configuration | **yes** — and I ask for it in §5 now; if you vote no, drop the column |

---

## 5. Step 6, *The second half: cruise carried on a wing* — your lists

The next architecture step. **Appendix B is its full current text.**
- **Size:** 2 145 words of prose, against a plan of 850.
- **Protected:** 23 sentences.
- **What makes it different from Step 5:** it holds numbers — the L/De envelope, the NASA comparison and the propeller. So the
  calculation rules apply as well as the architecture rules: the body-only interpretability rule; *"move the working, not the
  evidence"*; the isolation-pair rule for the external comparison.

**Please give, as for Step 5:**
- the core in the section's words;
- what stays and what goes to S6;
- the P71 pairs;
- negative qualifications, the later text that depends on each, and (Qwen P2) **the direction of each qualification**: against this
  configuration, for it, or neutral;
- voice flags, for the author;
- **every number in the body**, and whether its identity (value + unit + object + model) survives your proposed moves.

**My own reading, for you to criticise:**
- **Core:** *"a surface that carries the cruise lift"*; the envelope against rotorcraft, with the quadrotor low-corner exception
  reported as a result; the helicopter comparison as mixed.
- **Protected and structural:** the isolation pair for the NASA comparison — objects, common basis, *"not a controlled numerical
  reproduction"*. The three *"not matched"* sentences (speeds, atmospheres, analysis chains) are one unit.
- **Where the words are:** the propeller selection and the speed-mismatch argument look like working that can go to S6, with their
  results and qualifications left in the body. I have not tested that sentence by sentence; that is what your lists are for.

---

## 6. To vote

| # | Item | Who | My vote |
|---|---|---|---|
| a | §1: confirm each applied result, including *"also"* | all | confirmed |
| b | §1: V4 — the claim is carried twice elsewhere | DeepSeek | yes |
| c | §2: open-access PDF links for the four leads | all | — |
| d | Round 119 §7 votes; Round 120 §8 votes | **ChatGPT** | yes |
| e | §4 proposals | all | as in §4 |
| f | §5: Step 6 lists | all | as in §5 |

---

## 7. Your own proposals

As always: anything you see, with your reason.

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## Appendix A — Step 1, the paragraphs changed this round, as they now stand

**Neither family is deficient.** Each is limited by the price of
doing it that way. **The corner where both capabilities are wanted at once is where the two
applications this work is aimed at sit** — wildfire observation and response, and cargo delivery to
places without a runway — and both want to leave from an unprepared site and then cover distance.
**That corner is not empty**, as the rest of this section sets out; what is unsettled is which
price an architecture in it must pay, and whether one arrangement pays less than it appears to.

**Both work, and the second is the more demanding to build**, because rotating a propulsor in
flight brings a pivot and its actuators, a gyroscopic moment during the rotation, and a control
problem through a regime in which the aircraft is neither a rotorcraft nor an aeroplane.
**Those are mechanical and control requirements rather than aerodynamic ones**, and that
distinction is what this paper is built on.

**The established answer to hover control on such a configuration is a surface in the
slipstream**, and it is worth naming because this paper refuses it. That 2014 vehicle places
*"elevon and rudder … immersed in the propeller slip stream to provide three axis control moments
in hover."*

Each of those choices costs something, and **the giving-up is the part that is not free**. A
quadrotor tail-sitter produces a rolling moment from the reaction torque of four independently
driven rotors; a coaxial pair can produce one the same way, by running its two rotors at different
speeds. **Operating every pair torque-balanced spends that channel to buy the torque balance and
the near-zero net angular momentum**, and leaves the axis to a single aerodynamic device.

**None of the elements is new**, and Section 7 says so. Tail-sitting aircraft are seventy years old; blended wing bodies have been a standing subject of transport
research for three decades; series-hybrid propulsion has been flown in a crewed motor glider and designed for small uncrewed aircraft. The route is not claimed to have been waiting to be found. **The contribution is the
architecture: a configuration arranged to change regime by rotating the airframe rather than its
propulsors, and so carrying no mechanism that reorients a propulsor.** The combination, the
consequences of the choices inside it, and an accounting of what they cost are how that contribution
is presented and priced.

---

## Appendix B — Step 6 as it stands now (body only)

### The second half: cruise carried on a wing

### The opponent, and the axis

On this axis the alternative is the rotorcraft, multirotor and helicopter alike, and as in the previous section the comparison
runs one way only. **Nothing here is claimed against fixed-wing aircraft.** The claim is
confined to the one thing the rotorcraft family structurally lacks: **a surface that carries the
cruise lift.**

### What the requirement is

Section 5 established the first half: the aircraft must leave from and return to a site that
supplies nothing. **A rotorcraft meets that requirement completely.**

What it does not meet is the second half of both missions. Wildfire observation and response,
and cargo delivery to places without a runway, each require the aircraft to **cover distance
after it has left the unprepared site**, and a vehicle with no wing buys every second of that
distance with installed power. The consequence has been stated independently: surveying the
field, one study concludes that multirotors are efficient in hover and suited to short-range
missions, while vectored-thrust aircraft are efficient in cruise and suited to long-range ones.

### What the configuration does instead

**Cruise lift is carried by the airframe itself.** There is no separate fuselage: the whole
planform is the wing, so every part of the body that is carried is also a part that lifts. At
the cruise condition the lift coefficient follows from `C_L = W/(qS)`, the drag from
`C_D = C_D0 + C_L²/(πARe)`, and the nose pair is left with one job — producing the thrust that
balances that drag. It supports none of the weight.

That is the whole of the difference, and it is worth stating in those plain terms because the
consequence is structural. **A rotorcraft's rotors must produce the lift and the propulsive force
together, throughout cruise.** This aircraft separates them: a surface holds the aircraft up and a
propeller pushes it along, and **the wing produces its lift without a separate continuous power
supply of its own** — the power the aircraft spends in cruise goes to overcoming drag, of which
the lift's share is the induced part.
Lift is carried on a surface or it is carried on rotors, and no sizing contract, no assumption
in this paper and no choice available to a designer moves a vehicle between those two states.

**But the size of the resulting advantage is a calculation, not a consequence of that
statement**, and the two must not be run together. The rest of this section is the calculation,
and it gives a smaller number than the structural statement invites.

### What the margin actually is, in one currency

The sizing set of Section 4 reports an **effective lift-to-drag ratio**, defined in its own
nomenclature as `L/De = WV/P`: weight times speed over power. That is a system figure of merit,
not a force ratio, and it already contains the propulsive efficiency of whatever produces the
thrust. **A force ratio cannot be placed beside it.**

Converting this configuration's aerodynamic ratio into the same quantity is one line: in level
cruise thrust equals drag and lift equals weight, so with shaft power `P = DV/η_p`,

> **L/De = WV/P = (L/D) · η_p**

**Which power `P` denotes is not assumed here**, because reading it as electrical power rather
than shaft power would make this configuration's figure incomparable with the published one. The
source settles it in its hover formulation: hover power is written `Ph = W√(W/2ρA)/FM`, with the
figure of merit already applied — shaft power — and the propulsion-system efficiency applied
separately outside it. The cruise formulation uses the same separation, writing cruise energy as
`Pc/ηc` with `Pc = WV/(L/De)`. That separation appears in the source's **battery-capacity**
derivation, so it holds for the all-electric entries as well as the shaft-driven ones: if `L/De`
already contained the electrical chain, that derivation would count it twice.

**Neither factor is a single number, and they are two different kinds of spread.**

The aerodynamic ratio is **8.79 to 10.82**, with the tip frames and the free-wheeling attitude
rotors already charged. That spread is **uncertainty**: it is the zero-lift drag bracket, and a
designer does not get to choose where in it the real aircraft lands.

The cruise propeller efficiency is **0.632 to 0.683** across the nose-blade families that meet
the hover figure of merit — two and three blades per rotor, at two target section lift
coefficients, each solved at its hover and its cruise condition. That spread is **not
uncertainty**: it is a design variable this study has not fixed.

| L/De | η_p 0.632 | η_p 0.683 |
|---|---:|---:|
| **L/D 8.79** (adverse drag) | 5.56 | 6.00 |
| **L/D 10.82** (favourable drag) | 6.84 | 7.39 |

**These are the bounding corners of a product, not four simulated aircraft.** Two readings follow
and both are given, because choosing between them requires something this section does not have:

- **Examined envelope, 5.56 to 7.39.** **The four corners are not demonstrated aircraft
  states**, and nothing here
  shows that a built aircraft would land simultaneously on both bounds.
- **Best examined blade family, 6.00 to 7.39.** The highest efficiency among the families
  examined is 0.683; holding it and sweeping only the drag bracket gives this range.

**Whether 0.683 is the blade a designer would actually choose is not settled here**, and saying
so is the point. It is the best of the four *on cruise efficiency under the hover figure-of-merit
constraint*. Blade count and section loading also govern structural loads, acoustics, the motor
operating point, rotor inertia and manufacture, and **none of those is modelled in this work**.
Section 10 is where one blade is carried into a closed sizing loop; until then this section stays
at envelope level and does not present any corner as the aircraft's performance.

### What the comparison gives, against both published quadrotors

The sizing set contains two quadrotors for the same mission, and **neither is treated here as the
primary one.**

| | L/De | vs examined envelope 5.56 – 7.39 | vs best examined family 6.00 – 7.39 |
|---|---:|---|---|
| Quadrotor, turboshaft | 4.9 | +13 % … +51 % | **+22 % … +51 %** |
| Quadrotor, all-electric | 5.8 | −4 % … +27 % | **+3 % … +27 %** |

**Against the turboshaft quadrotor the sign holds at every corner of both readings.** Closing it
would need the propeller efficiency to fall to 0.557, against 0.632 for the least efficient blade
family examined.

**Against the all-electric quadrotor it does not hold at the low corner**, and that result is
reported as a result rather than as a caveat. That vehicle reaches 5.8 — above this
configuration's 5.56 — and it buys the difference with 1 742 lb of battery and nearly twice the
gross weight for the same mission, 7 221 lb against 3 678 lb. **That higher gross weight is
consistent with the mass charge Section 2 describes**, and Section 4 is where the independent
sizing evidence for it is set out — the comparison in this table does not establish the causal
link by itself. On cruise efficiency taken alone, the entry is ahead of this configuration's low
corner, and whether it is ahead of the best examined blade family depends on the drag bracket.

The same sizing set gives its two helicopter types at 5.4 to 7.2, and against them the result is
mixed: this configuration is ahead of the turboshaft single-main-rotor helicopter at every corner,
the two middle entries fall inside its envelope, and only its top corner is ahead of the
all-electric side-by-side helicopter, which has no wing either. The qualifications below apply to
these entries as they do to the quadrotors.

**So the second claim is narrower than the structural statement invites.** Carrying cruise lift on
a wing is worth **roughly a quarter to a half against the turboshaft reference, and against the
all-electric one it ranges from slightly behind to comfortably ahead depending on the drag outcome
and the blade** — a measurable advantage, not a change of category. And what
compresses it is not the wing. **It is the cruise efficiency this aircraft's fixed-pitch blade
delivers:** at a propeller efficiency of 0.85 the same airframe reaches 7.47 to 9.20. Whether a
variable-pitch hub would recover that difference is not computed; Section 11 reports the gap and
declines to attribute all of it to the hub.

### Five qualifications: three run against this configuration, one has no computed direction, and one bounds what the comparison can be called

They are given together because omitting any one of them would make the comparison look better
than it is.

**Scale.** The compared vehicles are 1 660 to 3 275 kg; the designs here are of order 50 kg and
1 000 kg — Section 10 closes the light one between 52.3 and 57.5 kg across the same bracket.
Reynolds number favours the larger aircraft, so the smaller design is at a disadvantage in this
comparison rather than an advantage.

**The quadrotor is a good quadrotor.** Its disc loading is 3.5 lb ft⁻², and the all-electric one's
is 3; both are unusually low. Nothing here is compared against a poor example.

**The speeds are not matched, and the direction of that mismatch is calculable.** The published
figure is quoted at the best-range speed; this configuration's is at its chosen cruise condition,
1.49 times stall, which Section 10 states explicitly is **not** its best lift-to-drag point. The
best point lies at 1.26 times stall, and `L/D_max = 0.5√(πARe/C_D0)` exceeds the cruise ratio at
both ends of the drag bracket — 11.65 against 10.82, and 10.08 against 8.79, both at e = 0.817.
**The reference is
therefore given its best speed and this configuration is not given its best speed, and the margin
is positive anyway.** The best point is not an available option — cruising there leaves too little
margin above the stall — so this fixes a direction, not a magnitude.

**The atmospheres are not matched.** The published sizing mission is flown at *"5,000-ft altitude
and ISA + 20°C"*; every number in this work is at sea level, with a sea-level drag polar and a
sea-level blade solution. **The direction of that mismatch is not claimed here**, because it has
not been computed: the altitude sweep in this work measured the effect on hover power and on
propeller efficiency, not on a cruise comparison at a re-trimmed best-range speed.

**The analysis chains are not matched, and this is the qualification that bounds what the
comparison can be called.** The published value is the output of an integrated conceptual-design
system with a comprehensive rotor analysis behind its rotor performance. The value here is
assembled from a drag build-up, a drag polar at a prescribed cruise condition, and a separate
blade-element propeller solution. There is a second difference inside that one: **the published
value is the effective ratio of a fully sized vehicle, while the value here is a converted
performance metric at a prescribed cruise condition, taken before the sizing closure Section 10
reports.** So this is a comparison of two independently produced figures in a common definition,
not a controlled numerical reproduction, and nothing in it should be read as validation of either,
or as a completed aircraft-level comparison.

### What is sized, and what is not demonstrated

**Sized.** The drag build-up and its bracket; the lift-to-drag ratio at the cruise condition
from the drag polar; the propeller efficiency from blade-element momentum theory at two
operating points; and the range that follows from the chain, link by link.

**Not demonstrated.** **No part of this has been measured.** There is no wind-tunnel test and no
flight test in this work, and the drag coefficient is a build-up with a declared bracket rather
than a measurement. The planform's sweep, taper and thickness distributions were chosen rather
than optimised. **The span efficiency used throughout this section is the computed value, 0.817,
not the assumed 0.85** — a vortex-lattice solution of the trimmed planform, and 3.9 percent below
the assumption, so the lift-to-drag figures above carry the calculated penalty rather than the
optimistic estimate. And **for the methods used here, and for the published
comparisons against which they were checked, the aerodynamic predictions diverge above roughly ten
degrees of incidence**: three methods of three fidelities depart at the same place, the highest of
them against wind-tunnel measurement. That is a statement about these methods on this class of
configuration, not about what any method could achieve. It does not touch the cruise numbers
above, which sit at a few degrees, but it bounds what this section may be read to support.

### What this half costs

The wing that makes cruise efficient is carried through the vertical phase, where it produces
nothing and presents the aircraft's largest surface to ground wind. The tailless planform that
follows from having no boom constrains the sweep, because with no horizontal stabiliser the
pitching moment must come from the distribution of lift along the body itself. And the
fixed-pitch propeller that serves both regimes is the reason the margin above sits where it does
rather than higher. Section 11 charges all three.

**The two halves are now on the table separately. Section 7 is where they are combined**, and
the combination is what this paper is for.

