# Round 52 — eleven repairs to Step 10, and the worst of them was mine

> **READ THIS FIRST.** Everything this round asks about is reproduced here. **You are not being
> asked to read a manuscript.** v8 is written as separate step files in `paper/v8/`;
> `paper-v6.md` and `paper-v7.md` are frozen historical records. **If your knowledge base holds a
> file whose name contains `makale-v` or `paper-v`, it is not what this round is about.**

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`1341494`**.

```
paper/v8/10-the-closure.md     SHA-256 2f22621f43504557d96ce295efe4c3cd343f0d58988be7a5f9f44fe81f2b35c0
paper/v8/06-the-second-half.md SHA-256 1ab981b9a7b140812bfbc8ff46f588c3eb09442bf81c4003395a508128080209
paper/v8/ALL-STEPS.md          SHA-256 cb71e706780edf77c2dde6e3bfb24c73dcb725cc22137b1a202e8257b20450e5
```

**Step 10 has not moved in its result.** The four closures are unchanged. What changed is eleven
places where the section said more than the numbers support, or said it in a way that would not
survive a referee. The two passages that were substantially rewritten are reproduced in full
below; the rest are given before and after.

---

## 1. The worst one is mine, and it is the sixth instance of the same class

Step 6's own list of things deliberately absent says:

> **No range number against a multirotor.** No multirotor is sized in this work; inventing a
> range comparison **would be fabrication.**

Last round I removed *"and range"* from Step 9's claim table for the same reason. **Then I wrote
this into Step 10:**

> ~~*"Even the lowest of them, 927 km, is not a number the rotorcraft family reaches."*~~

**Grok:** *"That sentence is the comparison, without a number on the other side. Delete it, or
replace it with a cited published endurance from a named vehicle. Do not let 927 km become a
ranking."* **ChatGPT** reached the same place independently and asked that Section 13 keep
ownership of cross-architecture ranking.

**I removed the claim from two steps and then made it in a third.** It now reads:

> *"**And these range figures are carried forward as the closed-loop values, not as a ranking.**
> No multirotor is sized in this work, so no range comparison is made against one — Section 6
> compares the two families in cruise efficiency and says why it stops there. The comparison
> against the other hybrid architectures depends on the sizing contract and belongs to Section 13,
> which is where it is made and where it reverses."*

---

## 2. Grok's two structural findings

### 2.1 The closure is the light design only

**Grok:** *"'On these assumptions the architecture closes' is true of the **light** loop. The
heavy aircraft appears only as a 5.1 s rotation time. Either close it in the same table or do not
quote it as if it had been through this loop."*

**Checked: `aero/closure.py` does not run the heavy design at all.** The section now says the loop
closes *"for the **light** design, which is the only one carried through this loop,"* and the
rotation times carry a parenthesis: *"both times were sized on the reference geometry at its
published mass; the closure above does not re-derive them, and a reader should not read them as
outputs of it."*

### 2.2 The frozen lift-to-drag ratio — the concern is answered, but the question was right

**Grok:** *"L/D is frozen as an input. At 57.5 kg versus the polar's original weight, C_L is
higher and induced drag should move L/D against you. The heavy-drag corners are therefore a little
optimistic."*

**Computed, and it does not happen — because of a sizing rule that was invisible.** The loop holds
**wing loading** fixed, so wing area grows with take-off mass:

| MTOW | Wing area | Cruise C_L |
|---|---:|---:|
| 49.35 kg | 1.951 m² | **0.4502** |
| 52.34 kg | 2.069 m² | **0.4502** |
| 57.51 kg | 2.273 m² | **0.4502** |

**The lift coefficient is identical at every closure**, so the polar is valid at the closed mass
rather than frozen at a mass the loop has left behind. **The concern is void and the question was
not** — a referee would ask exactly this, and the rule was not on the page. It is now, together
with the counterfactual: had wing *area* been held fixed instead, the induced term would have
moved against the heavier closures and the drag corners would be optimistic as reported.

---

## 3. DeepSeek's 8.79-versus-8.80 was bigger than a rounding note

**DeepSeek:** *"Step 6 quotes the low end as 8.80; step 10 says 8.79. Roundoff, probably, but a
reader checking will notice. Pick one."*

`drag_sweep.ld(0.0381)` returns **8.79024**, so **8.79 is the correct two-decimal value** and v7's
Table 9 printed 8.80. **But Step 6's product matrix was computed from the rounded 8.80**, and
moving to the precise value moves more than one cell:

| | before | after |
|---|---|---|
| Matrix corner B (8.79024 × 0.683) | 6.01 | **6.00** |
| Envelope vs turboshaft quadrotor | +14 % … +51 % | **+13 % … +51 %** |
| Best examined family vs turboshaft | +23 % … +51 % | **+22 % … +51 %** |
| Best examined family vs all-electric | +4 % … +27 % | **+3 % … +27 %** |
| At η_p = 0.85 the same airframe reaches | 7.48–9.20 | **7.47–9.20** |

The script now carries the precise values and prints margins to one decimal. **The sign and the
structure of the claim are unchanged; the digits were wrong in the last place.**

---

## 4. DeepSeek's reason for the engine spread is sharper than mine, and replaced it

I had written that the engine is sized by cruise power while mass feels the inputs only through
the propulsion fraction. **That is true and it understates the mechanism.**

**DeepSeek:** *"The engine is the only output the loop charges twice; the mass feedback raises W,
and W enters cruise power directly. Range escapes the double charge because the fuel fraction is
fixed. Mass escapes it because the propulsion fraction is only part of empty mass. Only the engine
sees the product."*

That is correct and it is now the section's explanation, in those terms. **It also supplies the
ordering** — why 46.1 percent exceeds 33.0 which exceeds 9.9 — which my version did not.

**ChatGPT's framing was adopted alongside it:** this is *"a sensitivity property of the declared
envelope, not evidence that engine sizing is intrinsically unstable."*

---

## 5. The two rewritten passages, in full

### 5.1 The closures and the sensitivity

#### The four closures

**All four converge.** On these assumptions the analytical sizing loop closes for this
architecture — and for the **light** design, which is the only one carried through this loop; the
heavy design appears below only through a transition time computed elsewhere.

| | C_D0 | η_p | L/D | MTOW | Empty fraction | Hover power | Engine | Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** | 0.0381 | 0.632 | 8.79 | 57.5 kg | 0.614 | 12.53 kW | 5.17 kW | 927 km |
| **B** | 0.0381 | 0.683 | 8.79 | 55.8 kg | 0.607 | 12.17 kW | 4.65 kW | 1 002 km |
| **C** | 0.0285 | 0.632 | 10.82 | 53.5 kg | 0.597 | 11.66 kW | 3.91 kW | 1 141 km |
| **D** | 0.0285 | 0.683 | 10.82 | 52.3 kg | 0.592 | 11.40 kW | 3.54 kW | 1 233 km |

**Payload is an input, fixed at 13 kg; take-off mass is the output.** The closure returns 52.3 to
57.5 kg, and the payload fraction that follows runs from **0.25 down to 0.23**.

**The spreads are not alike, and the difference is the useful part.** *Spread here is
(max − min)/min, so every figure is auditable from the table above.*

| | spread across the four |
|---|---|
| Take-off mass | **9.9 %** |
| Hover power | **9.9 %** |
| Range | **33.0 %** |
| Engine rating | **46.1 %** |

**Engine rating is the most sensitive output in this envelope and mass is the least, and the
ordering follows from where each input enters.** Cruise power is W·V/(L/D)/η, so it carries the
drag bracket and the blade family directly — **and W is itself a closure output that has already
absorbed them through the mass loop.** Range carries them directly but escapes the mass feedback,
because the fuel fraction is fixed. Mass feels them only through the propulsion fraction, which is
a minority of the empty mass. **Only the engine is charged twice**, and that is why 46.1 percent
exceeds 33.0, which exceeds 9.9. This is a sensitivity property of the declared envelope, not
evidence that engine sizing is intrinsically unstable.

#### Which input matters, and one question the closure answers

**The drag bracket dominates the blade family, and the four percentages are worth printing rather
than one ratio.** Holding the blade and moving across the drag bracket changes the mass by
**6.9 %** and the range by **23.1 %**. Holding the drag and moving across the blade families
changes the mass by **2.9 %** and the range by **8.1 %**. The drag uncertainty therefore produces
about **2.8 times** the range variation of the blade-family choice and about **2.4 times** the
mass variation.

**The thing the study has not measured moves the answer more than the thing it has not chosen.**
That is a statement about which of the two open questions is more consequential to resolve, not
about the intrinsic importance of drag against blade design.

**And the blade that is best before the loop is still best after it.** There was no reason to
assume so: propeller efficiency propagates through cruise power into engine size, engine size
into mass, and mass back into hover power, and a loop can reverse a local ranking. It does not
here — at both ends of the drag bracket the higher-efficiency family closes to the longer
range. **That is a result of the closure rather than an assumption carried into it**, and it
is reported because the opposite outcome would have been reported too.

### 5.2 The transition

**Grok asked for the verdict first** — *"a skimmer can still walk away with 'altitude loss is
zero'"* — and that is now the opening sentence, without changing the order Qwen asked for.
**ChatGPT asked that "floor" and "the most favourable case that can be constructed" be narrowed**,
because the evidence supports a result for the tested model rather than a universal lower bound.
**And the explanation of why the loss grows with gain is the source's own sentence**, not one I
invented for the purpose.

#### The transition, and this is where the section turns

The sizing above says nothing about whether the aircraft can change regime. **The verdict comes
first so that it cannot be missed: the question is asked in two models, only the second of which
carries rotational dynamics, and that one does not support a zero altitude loss.** The first model
is shown anyway, because the mechanism it exposes is real and the reason the second model differs
is the point.

**The first model is kinematically favourable, and the zero-loss result is valid within it.** Treating the aircraft as a
two-degree-of-freedom point mass and driving the body angle kinematically from zero to ninety
degrees, the altitude lost during the rotation falls as the rotation is made slower — the
aircraft is supported through the manoeuvre rather than falling through it. **Entering the
rotation while already climbing removes the loss entirely**: at a 5 m s⁻¹ entry climb the
altitude loss is zero at both reference rotation times — **two seconds for the light design and
5.1 seconds for the heavy one** — and it stays zero at every thrust-to-weight ratio from 1.066
down to 1.00. *(Both times were sized on the reference geometry at its published mass; the closure
above does not re-derive them, and a reader should not read them as outputs of it.)* Nothing in that result requires the tip pairs
to contribute lift once the climb is acquired.

**In this point-mass model there is no transition time to optimise**, which is a simplification
rather than a trade.
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
reference almost exactly. **What the kinematic model leaves out is not the difficulty of turning
the aircraft but the trajectory the aircraft flies while it is being turned**, so tighter tracking
of a reference the rotational dynamics do not admit moves the aircraft further from the path it
can actually fly, not closer.

**So the zero-altitude-loss result is a property of the model that produced it.** What replaces
it is not a prediction: the aerodynamic pitching moment that would make it one is precisely the
quantity Section 14 reports as unavailable — **for the methods used here, and for the published
comparisons against which they were checked**, the predictions diverge above roughly ten degrees
of incidence, and the rotation passes through that band. With
a borrowed moment the outcome depends on which moment is borrowed, and the spread is wide
enough that **no number from it is reportable** — some models complete the rotation, some
saturate the tip pairs, and some tumble. **That spread is itself the finding.** What survives is
not a transferable transition figure but a result for the model that was tested: **within the
finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs
altitude.** Whether a real aircraft loses 5.4 m, more, or less is not settled by anything here.

---

## 6. The remaining repairs

| Before | After | Found by |
|---|---|---|
| *"On these assumptions the architecture closes"* | *"the **analytical sizing loop** closes for this architecture"* | ChatGPT |
| *"If none exists, the architecture does not close"* | *"If no fixed point exists, **the declared sizing package** does not close — a statement about that package rather than about whether some other package could"* | ChatGPT |
| *"spread across the four"*, undefined | *"Spread here is **(max − min)/min**, so every figure is auditable from the table above"* | ChatGPT |
| *"the drag bracket beats the blade family by roughly three to one"* | the four percentages printed, and **2.8×** in range, **2.4×** in mass — *"not one ratio but two"* | Grok, ChatGPT |
| *"The payload is 13 kg throughout, so the payload fraction runs from 0.23 to 0.25"* | *"**Payload is an input**, fixed at 13 kg; take-off mass is the output. The closure returns 52.3 to 57.5 kg, and the payload fraction that follows runs from 0.25 down to 0.23"* | DeepSeek |
| construction check silent about the published drag value | *"**This check is the only place in this section where the published drag coefficient appears**; every closure reported below uses the bracket"* | DeepSeek |
| Step 6: *"the designs here are 50 kg and 1 000 kg"* | *"of order 50 kg and 1 000 kg — **Section 10 closes the light one between 52 and 58 kg** across the same bracket"* | DeepSeek |
| *"There is no transition time to optimise"* | *"**In this point-mass model** there is no transition time to optimise"* | Grok |

---

## 7. Recorded for Step 11 before it is written — DeepSeek's double-count warning

> *"Step 10 has already charged the closure with tip-frame drag and free-wheeling rotor drag —
> inside the L/D bracket; the fixed-pitch compromise — inside the η_p range; the trim twist cost —
> inside the span efficiency; and all their mass and power consequences — inside the MTOW.
> **If the ledger adds any of these again, that is a double count — the same trap that was just
> caught in the loop, in prose form.**"*

**This is accepted and written into the project's deferred-decisions record.** The ledger's job is
therefore narrower than *"here is what the configuration pays"*:

1. **Decode what the closure's numbers already contain.**
2. **Name what they do not contain** — the unpriced cost of declining the reaction-torque channel,
   the transition altitude result, the strip's unsized actuation, the take-off margin that depends
   on the tip pairs.

**The specific trap named:** the ledger must not say *"and the fixed-pitch compromise costs X"* as
though it were an addition. It must say that the computed 0.632–0.683, against the 0.80 the
published chain assumed, **is** that compromise, and that this work does not decompose it per
source.

---

## 8. Qwen

Q1 through Q3 were useful — naming the construction test as a strength rather than a risk was a
fair point that nobody else made. **Q4 and Q5 entered a repetition loop**, restating the same
paragraph five or six times and then writing *"OK, I think I'm overcomplicating this"* before
starting again. That is the second consecutive round. **Nothing from those two answers was used**,
and this is said plainly rather than passed over.

---

## 9. What I am asking, and what comes next

1. **Do any of the eleven repairs create a new contradiction?** That is what this project keeps
   hitting: six defects so far have been corrections that were made in one place and not swept
   into another, and the one in section 1 above is the sixth. **The two passages reproduced in
   full above are where to look hardest**, because they are the ones that were rewritten rather
   than edited.
2. **Is the transition passage now in the right order** with the verdict first, or does leading
   with the verdict cost the mechanism the point-mass model was there to show?
3. **Step 11 is next: the ledger.** Its scope is section 7 above. **Is that scope right**, or does
   framing the ledger as *"what is inside these numbers and what is not"* leave out something a
   reader will expect a cost section to contain?

**No source is needed for any of this.** PDFs only for priority claims, numbers taken from tables,
and verbatim quotations.
