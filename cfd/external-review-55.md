# Round 51 — you caught a double-count in the Step 10 plan before it was written, and Step 10 is now written

> **READ THIS FIRST.** Everything this round asks about is reproduced here. **You are not being
> asked to read a manuscript.** v8 is written as separate step files in `paper/v8/`;
> `paper-v6.md` and `paper-v7.md` are frozen historical records. **If your knowledge base holds a
> file whose name contains `makale-v` or `paper-v`, it is not what this round is about.**

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`d749533`**.
`paper/v8/10-the-closure.md` SHA-256 `9fca2a27b1dc9c67ff8858870efe720437b53dfe87e1c3407e4e0880608ca429`.

---

## 0. The repair round, named

**The author asked that this be stated with the names attached, so that the record is
transparent.** Here it is.

### 0.1 The Step 10 plan was wrong, and ChatGPT and Grok found it independently

Round 50's briefing described the closure as:

> ~~*"carrying the four corners of the L/De matrix as four inputs to `baseline.py`, which takes
> lift-to-drag as an input"*~~

**ChatGPT:** *"Do not feed L/De into a function whose input is L/D… otherwise there is a serious
risk of doing this: L/D ← L/De = (L/D)η_p, and then multiplying by η_p again inside the chain."*

**Grok:** *"If the script still multiplies by a propeller efficiency inside the chain, feeding
L/De double-counts η_p."*

**The code was opened. They are right.**

```
baseline.py:43    eta_zincir = 0.176 = 0.2202 × 0.80    ← already contains the propeller
baseline.py:126   R = f_fuel × E* × eta_zincir × (L/D) / g
```

**And there is a second trap neither of you named, which the code check turned up.** The loop
contains **two** efficiency terms, not one:

```
baseline.py:111   P_cruise = W·V / LD / eta_seyir    ← SIZES THE ENGINE
baseline.py:126   R        = … eta_zincir × (LD) …   ← GIVES THE RANGE
```

`eta_seyir = 0.721` also contains the propeller efficiency — it was back-solved from the paper's
own cruise power. **Scaling only `eta_zincir` would size the engine on the old propeller and
compute the range on the new one**, and the loop would be internally inconsistent while appearing
to close.

**The correct mechanism already existed in the repository.** `chain_resolve.gorev_ile(eta_p)`
scales both terms together. So the mechanism was right and **my description of it was wrong.**
`aero/closure_inputs.py` now pins the input slot with a construction test that halts the script
if `gorev_ile(0.80)` fails to reproduce the published values; it reproduces them to 0.11 %.

**DeepSeek asked two questions about the loop and both are answered from the code:** η_p is an
**input**, not a loop variable — `baseline.py` does not size the propeller — and **the engine
rating does vary across the four closures**, so the spread in engine size is reported below, as
DeepSeek asked.

### 0.2 The fifth propagation failure — DeepSeek

Step 8 was corrected from *"three jobs"* to **four** for the tip frames. **Step 5 still said
"three purposes."** The correction did not propagate, inside the same round. That is the fifth
instance of the class, and the sweep rule now covers it.

### 0.3 The other six repairs

| Repair | Found by |
|---|---|
| Step 7's *"the condition it is **built to satisfy**"* revived the full-escape implication; the aircraft is a **partial** instantiation → *"the condition **its primary propulsor is designed** to satisfy… the price the configuration pays for **pursuing** it"* | ChatGPT |
| Step 6's *"every corner is **reachable**"* → *"bounding combinations permitted by two independent model inputs… **not four demonstrated aircraft states**"* | ChatGPT, Grok |
| Step 3's **inverted table** still omitted Bill 3 for tilting — step 2 had been fixed, step 3 had not | DeepSeek |
| Falsifiability stated **positively**: *"a counter-example is a remedy that reduces one of the three charges, leaves the other two no worse, and whose own cost is either absent or demonstrably smaller than the reduction — **measured in the same currency**"* | Grok asked for it; DeepSeek's objection that the test was too weak is answered by the same clause |
| Mechanism-table heading widened: *"…to change regime, **or to take a rotor out of one regime's flow**"* | DeepSeek |
| Partial instantiation is about the **charges**, not the condition — the condition governs the propulsor that carries the aircraft | Qwen |

**Two findings were based on text that had already changed:** DeepSeek quoted a permitted-costs
clause (*"the condition says nothing about them"*) that was removed the round before, and Grok's
*"if step 6's closing sentence still says 14 to 51 percent"* was conditional and it does not.

### 0.4 And one I caught in my own audit of Step 10

Writing the new section I put in it: *"the quantity Section 14 reports that **no current method**
supplies reliably."* **That is the universal claim ChatGPT had me narrow in step 6 two rounds
ago**, reappearing in a section written after the narrowing. It now reads *"for the methods used
here, and for the published comparisons against which they were checked."* The repository-wide
sweep found no other instance.

---

## 1. Step 10, in full

**This is the first numerical section in the paper.** Nothing in steps 1–9 gives a closure for
this aircraft.

**Three constraints shaped it, and all three came from you:**

- **ChatGPT's, from Round 34:** the title does not contain *"and where it fails"*, because that
  phrasing pulls the battery shortfall into the closure section. The shortfalls live in Section 14.
- **Grok's, from the same round:** **the 3.8× figure has exactly one home, and this is not it.**
  *"One number, two roles, one paragraph."* The closure section says the loop closes on a declared
  package; Section 14 says that package does not exist. **This section does not tell that story.**
- **Qwen's:** the *favourable result, then the break* structure stays in **one place**, unbroken,
  so the reader sees the result given and taken back without turning a page.

---

### Analytical closure of the sizing loop

**Closing a sizing loop mathematically is not the same thing as closing an aircraft
physically.** This section does the first. What it produces is a set of consistent numbers
on a declared set of assumptions: if the assumptions hold, these masses, powers and ranges
follow from one another without contradiction. Whether an aircraft can be built to them is a
different question, and Section 14 is where the answer is not yet yes.

#### Why the loop has to be iterative

The pieces depend on each other in a circle. Installed power sets the mass of the propulsion
system; propulsion mass raises the take-off mass; take-off mass raises the power needed to
hover; and the hover power is what sizes the installed power. The closure statement is

> MTOW = m_payload / (1 − f_empty − f_energy)

and f_empty contains a term proportional to installed power, which contains a term
proportional to MTOW^1.5. **A fixed point is sought by iteration. If none exists, the
architecture does not close**, and the calculation says so rather than returning a number.

#### The inputs, and why there are four closures rather than one

Two quantities entering the loop are not single values, and **they are not the same kind of
quantity**, which is why they are carried separately rather than merged.

**The zero-lift drag coefficient is uncertainty.** A consistent build-up places it between
**0.0285 and 0.0381**, with the same rotor term at both ends. A designer does not choose where
the real aircraft falls in that range.

**The blade family is a design variable this study has not fixed.** Four nose-blade families
meet the hover figure of merit, and their cruise propeller efficiencies span **0.632 to
0.683**. A designer would choose one; the criteria that would decide the choice — structural
loads, acoustics, the motor operating point, rotor inertia, manufacture — are not modelled
here, so the study carries all four rather than pretending to have chosen.

**The published zero-lift value of 0.0248 is not used.** The consistent build-up places it
below both ends of the bracket, so it is not a conservative choice or an optimistic one; it is
outside the supported range, and closing the loop on it would mean closing on a number this
work has shown it cannot support.

**Propeller efficiency enters the loop twice, and both entries move together.** It appears in
the range expression, and it appears in the cruise power that sizes the engine. Scaling one
without the other would size the engine on one propeller and compute the range on another, and
the loop would be internally inconsistent while appearing to close. Both terms are scaled
with the blade family in every closure reported here.

**The reference point is the aerodynamic lift-to-drag ratio, not the effective one.** The
effective ratio of Section 6 already contains the propeller efficiency; it is the currency in
which the multirotor comparison is made, and it is not an input to a loop whose own chain
supplies that efficiency separately.

#### The construction is checked before it is used

At the published assumption — the published drag coefficient with the rotor term omitted, and
the published propeller efficiency — the construction returns a take-off mass of **49.4 kg**
against the published 50.1, a cruise lift-to-drag ratio of **11.88** against 11.88, and a range
of **1 585 km** against 1 583. **The largest deviation is 1.5 percent**, in mass. The
construction reproduces the published aircraft, so the same construction run on the bracket is
reporting a change of inputs rather than a change of method.

#### The four closures

**All four converge.** On these assumptions the architecture closes.

| | C_D0 | η_p | L/D | MTOW | Empty fraction | Hover power | Engine | Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** | 0.0381 | 0.632 | 8.79 | 57.5 kg | 0.614 | 12.53 kW | 5.17 kW | 927 km |
| **B** | 0.0381 | 0.683 | 8.79 | 55.8 kg | 0.607 | 12.17 kW | 4.65 kW | 1 002 km |
| **C** | 0.0285 | 0.632 | 10.82 | 53.5 kg | 0.597 | 11.66 kW | 3.91 kW | 1 141 km |
| **D** | 0.0285 | 0.683 | 10.82 | 52.3 kg | 0.592 | 11.40 kW | 3.54 kW | 1 233 km |

The payload is 13 kg throughout, so the payload fraction runs from **0.23 to 0.25**.

**The spreads are not alike, and the difference is the useful part:**

| | spread across the four |
|---|---|
| Take-off mass | **9.9 %** |
| Hover power | **9.9 %** |
| Range | **33.0 %** |
| Engine rating | **46.1 %** |

**Mass is the stable quantity and the engine is the volatile one.** Mass moves by a tenth
across the whole envelope; the engine rating moves by nearly half. That is a property of where
each input enters: the engine is sized by cruise power, which carries the drag and the
propeller efficiency directly, while mass feels them only through the propulsion fraction,
which is a minority of the empty mass.

#### Which input matters, and one question the closure answers

**The drag bracket dominates the blade family, and not marginally.** Holding the blade and
moving across the drag bracket changes the mass by 6.9 percent and the range by 23.1 percent.
Holding the drag and moving across the blade families changes the mass by 2.9 percent and the
range by 8.1 percent. **The thing the study has not measured moves the answer more than the
thing it has not chosen.**

**And the blade that is best before the loop is still best after it.** There was no reason to
assume so: propeller efficiency propagates through cruise power into engine size, engine size
into mass, and mass back into hover power, and a loop can reverse a local ranking. It does not
here — at both ends of the drag bracket the higher-efficiency family closes to the longer
range. **That is a result of the closure rather than an assumption carried into it**, and it
is reported because the opposite outcome would have been reported too.

#### The transition, and this is where the section turns

The sizing above says nothing about whether the aircraft can change regime. That question is
asked here rather than later, and it is asked in two models, because the second one takes back
what the first one gives.

**The first model is favourable and the result is real within it.** Treating the aircraft as a
two-degree-of-freedom point mass and driving the body angle kinematically from zero to ninety
degrees, the altitude lost during the rotation falls as the rotation is made slower — the
aircraft is supported through the manoeuvre rather than falling through it. **Entering the
rotation while already climbing removes the loss entirely**: at a 5 m s⁻¹ entry climb the
altitude loss is zero at both reference rotation times — **two seconds for the light design and
5.1 seconds for the heavy one** — and it stays zero at every thrust-to-weight ratio from 1.066
down to 1.00. Nothing in that result requires the tip pairs
to contribute lift once the climb is acquired.

**There is no transition time to optimise**, which is a simplification rather than a trade.
The control moment required scales as 1/t_r² and the control power as 1/t_r³, and the altitude
loss falls with t_r as well: all three point the same way, so the rotation time is set by what
the actuator can do rather than by a balance between competing penalties.

**The second model removes the result, and this is the sharper of the two limitations.** The
point-mass model prescribes the attitude and therefore cannot charge for the trajectory the
aircraft flies while it is being rotated into that attitude. Solved instead with rotational
dynamics and a finite control moment — **and with the aerodynamic pitching moment set to
exactly zero, so that nothing favourable is borrowed** — the light design **loses 5.4 m at the
same reference condition where the point-mass model reports none.**

**The loss is not an artefact of the controller.** It is unchanged across linear, bang-bang and
smooth reference profiles; it appears without the control moment ever saturating; and it grows
rather than vanishes as the gains are raised, reaching 17 m at gains high enough to track the
reference almost exactly.

**So the zero-altitude-loss result is a property of the model that produced it.** What replaces
it is not a prediction: the aerodynamic pitching moment that would make it one is precisely the
quantity Section 14 reports as unavailable — **for the methods used here, and for the published
comparisons against which they were checked**, the predictions diverge above roughly ten degrees
of incidence, and the rotation passes through that band. With
a borrowed moment the outcome depends on which moment is borrowed, and the spread is wide
enough that **no number from it is reportable** — some models complete the rotation, some
saturate the tip pairs, and some tumble. **That spread is itself the finding.** What survives
is a floor rather than a figure: **the manoeuvre costs altitude even in the most favourable
case that can be constructed.**

#### What closing does and does not establish

**It establishes that the architecture is arithmetically self-consistent on a declared
package**, at four corners of that package, with mass, power and range agreeing with one
another and with the construction that reproduces the published aircraft.

**It does not establish that the package exists.** The energy store this closure assumes is
the item Section 14 examines, and the examination does not end well. Nothing in this section
should be read as a claim that the aircraft is buildable; the claim is narrower and is the one
the section's title makes — the loop closes analytically, on assumptions that are stated and
that Section 14 tests.

**And the range figures above belong to this configuration against the multirotor family, and
to no other comparison.** Even the lowest of them, 927 km, is not a number the rotorcraft
family reaches; the ranking against the other hybrid architectures is the subject of Section 13
and it is not claimed in either direction here.

---

## 2. What I am asking of you

1. **Does the closure section claim more than the numbers support?** It reports that the loop
   closes and that the architecture is arithmetically self-consistent. It should not read as a
   claim that the aircraft is buildable.
2. **Is the transition passage honest in its order?** The favourable model comes first and the
   result is real within it; the second model takes it back and the section says the first result
   is a property of its model. Does that read as honest, or as a result being defended before it
   is withdrawn?
3. **The engine-rating spread of 46.1 percent is the largest number on the page.** Is that a
   finding worth the weight it gets, or an artefact of where the inputs enter? I have said it is
   the former and given the reason; say so if the reason is wrong.
4. **The drag bracket beats the blade family by roughly three to one.** That says the unmeasured
   quantity moves the answer more than the unchosen one. Is there anything wrong with reporting it
   that way?
5. **Steps 11 to 14 remain.** 11 is the ledger, 12 the bills separating with scale, 13 the
   contract-dependence of rankings, 14 what does not close. **Does Step 10 hand off cleanly to
   the ledger**, or does it already spend something the ledger needs?

**No source is needed for any of this.** PDFs only for priority claims, numbers taken from tables,
and verbatim quotations.
