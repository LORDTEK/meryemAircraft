# Round 54 — two of you broke the same cell in Step 11, and Step 12 narrows its own promise

> **READ THIS FIRST.** Everything this round asks about is reproduced here. **You are not being
> asked to read a manuscript.** v8 is written as separate step files in `paper/v8/`;
> `paper-v6.md` and `paper-v7.md` are frozen historical records. **If your knowledge base holds a
> file whose name contains `makale-v` or `paper-v`, it is not what this round is about.**

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`4215575`**.

```
paper/v8/12-the-bills-separate.md  SHA-256 55694a6b4e7e1ca55196d732f66d1ed0905b7a003cc7b2bde7e26e536519eb73
paper/v8/11-the-ledger.md          SHA-256 6edb7065cb155ea6d3a9377a3bb87e3b9afb07d67d99de25c2e6a9029cb4991b
aero/drag_sweep.py                 SHA-256 f76d90f40ca45600c7f70c3994a326471f8e34d4aa8d60bb54185bafad3d96f9
```

**The author asked that this round state plainly who said what and what was done about it.**
Sections 1 to 4 do that. Section 5 is Step 12, in full.

**Who answered last round:** Grok, ChatGPT and DeepSeek. **Qwen returned nothing this round.**
In the two rounds before, its answers entered repetition loops partway through and were not used
past that point.

---

## 1. The finding two of you made independently — and it was an arithmetic error of mine

**Step 11 gave the clean-body lift-to-drag ratio at the adverse drag end as 14.29.**

**DeepSeek** rebuilt it from the table's own inputs — C_L 0.4502, πARe 15.48, induced term 0.0131,
clean zero-lift 0.0142 + 0.0022 = 0.0164 — and got **15.26**: *"The favourable value checks; the
adverse one does not."*

**Grok** did the same independently and got **15.3**: *"I cannot reconstruct 14.29 from the table
plus the polar. Until that cell is shown, the 'retains 53 % / 62 %' line and the '38 to 47
percent' sentence are unsupported at one end."*

**Both were right. The code was opened and the cause found:**

```
drag_sweep.zincir() subtracted the frame and rotor terms at their UNMARGINED values (0.0197)
from a total that already carries the ×1.1 adverse margin — where those terms are 0.0047 and
0.0169. Subtracting too little made the clean body look dirtier than it is.
```

**Corrected: 15.24.** The function now takes the margin; the correction is recorded in its
docstring.

**The closure was not affected, and this was checked rather than assumed.** The function returns a
clean-body ratio *and* a multiplier defined as their ratio, and the sizing loop multiplies them
back together — so the product is the aircraft's own lift-to-drag ratio whatever the split. All four
closures reproduce exactly: 57.5 / 55.8 / 53.5 / 52.3 kg, 927 / 1 002 / 1 141 / 1 233 km. **What was
wrong was only the reported clean-body ratio and the percentages derived from it** — both in
Step 11.

| | before | after |
|---|---|---|
| Clean-body L/D, adverse end | 14.29 | **15.24** |
| Retained | 53 % / 62 % | **52.6 % / 57.7 %** |
| Removed by non-clean-body terms | 38–47 % | **42.3–47.4 %** |

**The counter-intuitive ordering survives, narrower:** Bill 2's share is larger at the cleaner end,
47 against 42 rather than 47 against 38.

---

## 2. Grok's buffer question — and what checking it found, twice

**Grok:** *"Buffer 3.6 % / 1.9–2.1 kg: Step 10's printed table does not contain it. If the loop
still holds 3.6 % of MTOW, say so. If 3.6 % is the old 1.8/50.1 ratio pasted onto new masses,
hover energy moved and the fraction is stale."*

**Checked. The buffer is applied as a fraction of take-off mass, and it is never derived from
hover energy anywhere in the code.** A fixed fraction is the right dimensional form — at constant
disc loading hover power is linear in weight — **but what the buffer supplies is hover power minus
what the engine can deliver**, and that deficit runs from 0.128 to 0.150 kW per kilogram across the
four closures. **A 17 percent spread, and the corner needing the most buffer gets the least.**
Step 11 now states the buffer is a declared input and reports that spread.

**The same check, run again while writing Step 12, found that the heavy design's 4.0 percent is
also an input.** That changes what Step 12 can claim — Section 5 below.

---

## 3. Everything else, by reader

### Grok

| Point | Done |
|---|---|
| *"Write 'share' in every sentence… 'Heavier' alone will be read as counts"* — absolute frame+rotor drag is 0.0197 favourable, 0.0216 adverse | **Taken.** *"larger fractional burden where the clean-body drag is lower"*, and the reverse direction of the counts is stated |
| *"The 10 % adverse margin is applied to the whole build-up, so line items at that end are not independent measurements"* | **Taken**, in the table caption |
| *"The total is the contract… Without that pointer it reads as leaving the cost section unfinished"* | **Taken.** *"the total is the contract, not a property of the aircraft"* → Section 13 |
| Airframe 0.300 and avionics 0.080 — *"construction constants or inventory?"* | **Taken.** Stated as construction constants held common across architectures |
| *"Keep 'hover hardware' tied to 'exposed for the vertical-phase layout,' not 'dedicated lift group'"* | **Taken**, with the reason: Section 7 claims there is no dedicated lift group |
| *"Do not preview 'Bill 2 shrinks with scale.' 12 needs that unspent"* | **Kept unspent.** It is said for the first time in Step 12 |

### DeepSeek

| Point | Done |
|---|---|
| The 10 % margin caption mis-describes the table — clean surface varies 94 %, hub 47 %, frames and rotors 10 % | **Taken.** The two separate causes — bracket base values, then margin — are now distinguished |
| Step 11's Bill 2 ordering is *position within the bracket at fixed scale*; Step 12 is *scale* — *"a reader will see two statements that appear to go in opposite directions"* | **Taken** in both steps: each says it is a different axis from the other |
| *"The weighting belongs to whoever has the mission"* | **Taken**, beside Grok's pointer to Section 13 |
| *"Section 12 should use the buffer as the currency-conversion test"* | **Tried, and it cannot be run** — the buffer is an input at both scales. Section 5 says why |

### ChatGPT

| Point | Done |
|---|---|
| *"'None of those numbers is new here' is literally false"* | **Taken.** *"No new physical cost term is introduced here"*; the percentages are new calculations, not new charges |
| Tip-frame drag is not purely a hover cost — the frames have four duties | **Taken.** *"an attribution, not a marginal removal cost"* |
| *"'Removing the frames and the rotors' — your table also removes the hub"* | **Taken.** *"removing all three non-clean-body terms"* |
| **The fixed-pitch gap is over-attributed** — *"You have not demonstrated that a variable-pitch hub would recover the entire difference to 0.80"* | **Taken, and it was the most important of the three.** Section retitled *"The cruise-efficiency gap under fixed pitch"*; states that **no variable-pitch counterfactual was computed** |
| *"No scalar aggregate is defined because the study does not specify a defensible weighting"* | **Taken**, in that form |
| *"These four closures vary drag and blade at the reference scale; they do not establish how the bills scale"* | **Taken**, as the handoff to Step 12 |

---

## 4. What Step 12 found before it was finished — and it narrows the step's own promise

The skeleton promised Step 12 would show **"that the three currencies really are three, not one
quantity under three names."** Writing it against the source changed what it can say.

**Bill 1 cannot be tested at scale with what this work contains.** On this configuration Bill 1
*is* the buffer — Step 11 established that there is no dedicated lift group to charge. The published
comparison has the buffer rising from 3.6 to 4.0 percent between 50 kg and 1 000 kg and calls that
the mass bill rising. **Both figures are inputs**, chosen for each design point. A change between two
choices is not a scaling result. And the structural mass does not stand in for it: the airframe is
carried by every architecture and is not Bill 1 as Step 2 defines it.

**So separability is shown between two of the three charges.** Bill 2 falls to between a quarter and
a half of its light-design value; Bill 3 is held within 5 percent by one sizing rule. Two quantities
that respond so differently to the same change are not one quantity under two names. **Bill 1 is
untested**, and the section says so rather than borrowing the structure to fill the gap.

**Deriving the buffer from hover energy is possible and was not attempted.** It leads directly to the
battery specific-power question — **the one Grok said stays a single paragraph in Section 14.** Step
12 stops there deliberately.

**One more thing checking the source turned up.** The published scale comparison states the blade
solidity falls from 0.075 to 0.044 and gives the predicted ratio as *"1.73 × 1.78 = 3.08"* against a
computed 3.04. **0.075 / 0.044 is 1.70, not 1.73, and the product is 3.03** — and neither solidity
value appears in any script output in the repository. Step 12 does not claim the three-digit
agreement. It gives the mechanism, the direction, and a ratio of *about three*, and notes that the
computed ratio moves from 2.1 to 4.4 across the heavy design's interval anyway.

**No heavy-design range is given.** Every figure available — 1 814, 1 571, 1 398–1 517 km — is partial
in one respect or another, and none carries both the rotor charge and the computed propeller.

---

## 5. Step 12, in full

### The charges separate with scale, and one of them cannot be tested

Section 11 decomposed the three charges on one aircraft, at one size. **This section asks a
different question: are they three quantities, or one quantity under three names?** The test is
to change the size of the aircraft and see whether they move together. If they did, the framework
of Section 2 would be a single cost described three ways, and a ledger in three currencies would be
a ledger in one.

**This is a different axis from the one Section 11 examined.** There, Bill 2's share of the
zero-lift drag was compared at the two ends of the drag bracket, at a fixed size. Here the size
changes. The two answers are about different variables and do not bear on each other.

#### What is compared, and why it is these two points

**The comparison is between the two published reference designs, 50 kg and 1 000 kg, sized by
one method.** It is not between the four closures of Section 10, which vary the drag uncertainty
and the blade family at a single size and are not a scale study.

**The pair can be used even though Section 10 superseded some of what was published, because the
quantities this section needs are not among the superseded ones.** The free-wheeling rotor term
is the same value Section 10 carries at both ends of its bracket. Disc loading is a sizing rule
Section 10 holds. The buffer fraction is an input to Section 10's loop. **The quantities Section 10
replaced — the total zero-lift drag, the propeller efficiency, the range and the closed mass — are
not used here**, and no heavy-design range is quoted for that reason: every figure available for
it is partial in one respect or another.

**Two conditions travel with the heavy design and are stated here rather than later.** It has no
drag bracket; it stands on a single zero-lift coefficient with no equivalent bound. And **its
structural closure is undetermined**: shell mass scales with wetted area while take-off mass scales
with volume, so the structural fraction depends on how areal density grows with size, and that
exponent has not been measured. **The comparison below uses powers, loadings and drag terms; it
does not use the structure**, which is why it can be made at all.

#### Bill 3 — held nearly flat, and held there by a sizing rule

**Disc loading is held constant**: 44.2 kg m⁻² at 50 kg and 43.7 at 1 000 kg. Specific hover power
depends only on disc loading, so fixing it fixes hover power per unit weight — **0.218 kW kg⁻¹ at
the light design and 0.216 at the heavy**, a ratio of 0.99. Hover power rises from 10.9 kW to
216.2 kW, a factor of 19.8 against a mass factor of 20. **Hover power grows linearly with mass
rather than as the L^3.5 of the classical result.**

The engine, sized by cruise, moves slightly more, because the heavy design cruises faster at a
better lift-to-drag ratio. **The ratio of hover power to engine rating is 4.19 at the light design
and 3.98 at the heavy — a change of 5 percent.**

**That near-constancy is a consequence of a design rule, not a finding about Bill 3**, and it has
to be read that way. What it does establish is narrower and still useful: Bill 3 *can* be held
nearly flat across a factor of twenty in mass by a single sizing choice.

**The rule has a price, and it is paid in geometry.** Holding disc loading constant makes disc area
grow as L³ rather than L², so the nose propeller grows faster than the airframe. Wing loading rises
from 25.3 to 45.0 kg m⁻², span grows by a factor of 3.35 and the main propeller by 4.50, and **the
ratio of propeller diameter to span rises from 0.35 to 0.47.** The heavy design is not the light
design photographed from further away. **Much above 1 000 kg a single nose pair can no longer hold
the disc loading**, and a second would have to be added — which the architecture permits, since
every pair is torque-balanced on its own.

#### Bill 2 — falls to between a quarter and a half, and this is the computed result

**The free-wheeling rotor term falls from 0.0154 at 50 kg to 0.0051 at 1 000 kg.** The heavy value
is not pinned: across the blade designs that meet the heavy design's hover requirement it runs from
0.0035 to 0.0074, and 0.0051 is the interior value the sizing was run at. **At every point in that
interval the heavy charge is between a quarter and a half of the light one** — 0.23 at one end,
0.48 at the other.

**The mechanism is not the obvious one.** The obvious explanation is that the wing outgrows the
discs. It does not: the eight tip discs total 0.251 m² against 1.98 m² of wing at 50 kg, and
2.82 m² against 22.24 m² at 1 000 kg — **a disc-to-wing area ratio of 0.127 at both sizes.** What
the charge follows is

> ΔC_D0 ∝ σ R² / (q S)

in which R²/S is the constant just quoted, so **only two terms move**: the blade solidity σ falls,
because the larger rotor meets its thrust with proportionally less blade, and the cruise dynamic
pressure q rises, because the heavy design cruises at 40 m s⁻¹ rather than 30. **The charge falls
because the blade thins and the reference dynamic pressure rises, not because the wing outgrows
the disc.**

**How closely the two terms predict the computed ratio is not claimed here.** The two terms give a
ratio of about three; the computed ratio at the interior value is also about three; but the
computed ratio moves from 2.1 to 4.4 across the heavy interval, so any closer agreement would be an
agreement at a point that no criterion selects. **What holds everywhere in the interval is the
mechanism, the direction, and the order of magnitude.**

**This result does not touch the structural question at all.** It comes from blade-element
solutions on two sized rotors and from the two cruise speeds; it would remain a result even if
the heavy airframe were shown not to close. **And it means the light design is the harder case for
Bill 2**, which is the opposite of the usual expectation for a tail-sitter.

#### Bill 1 — cannot be tested with what this work contains

**On this configuration Bill 1 appears as the energy buffer**, as Section 11 set out, since there is
no dedicated lift group to charge. The buffer is 3.6 percent of take-off mass at 50 kg and 4.0
percent at 1 000 kg.

**Both of those figures are inputs.** Neither is derived from the hover energy the aircraft needs;
each was chosen for its design point and carried into the sizing. **A change from 3.6 to 4.0 percent
is therefore a change between two choices, not a scaling result**, and it cannot be offered as
evidence that Bill 1 moves with size in either direction.

**Nor is the structural mass a substitute.** The shell-mass exponent governs how the airframe
fraction scales, and it is unmeasured; but the airframe is not Bill 1 as Section 2 defines it — it
is the structure every architecture carries — and treating it as the mass bill would change the
definition to fit the test.

**Deriving the buffer from the hover energy is possible in principle and is not attempted here.**
Doing it properly means asking what specific power a store of that mass must deliver, and that is
the item Section 14 examines and does not resolve. This section stops short of it deliberately.

#### What the comparison establishes

**Separability is shown between two of the three charges, and not the third.** Bill 2 falls to
between a quarter and a half of its light-design value while Bill 3 is held within 5 percent by a
single sizing rule. **Two quantities that respond that differently to the same change of size are
not one quantity under two names.** That is the finding, and it holds wherever in the heavy
interval the rotor term falls.

**Bill 1 is untested at scale**, for the reason given above, and nothing here should be read as
showing it separates from the other two — or as showing that it does not.

**And the evidence is one pair of design points, computed by one method.** It is consistent with
the separability Section 2 asserts; it is not a verification of separability as a general property,
which a single instantiation cannot supply.

#### Two costs that scale does not relieve

Neither is one of the three charges, and both are reported because a section about what scale does
to this aircraft would be incomplete without them.

**The fixed-pitch gap does not close with size; it widens slightly.** Against the 0.80 the
published chain assumed, the computed cruise propeller efficiency is 14.6 to 21.0 percent lower at
the light design and **16.4 to 23.0 percent lower at the heavy one.** Refusing the variable-pitch
hub costs as much or more at the larger size.

**The transition is where the square–cube relation is paid in full.** The moment needed to rotate
the aircraft follows M = Iα with I ∝ mL², so the moment required for a fixed rotation time grows
much faster than the aircraft. **Rotating the heavy design in the light design's two seconds would
demand 221.5 kW from the tip propellers — 102 percent of hover power**, which is not available. At
5.1 seconds the demand falls to 13.4 kW, 6 percent of hover power, and that is the heavy design's
rotation time. **A larger aircraft of this type turns more slowly, and must.** Hover power escapes
the classical scaling objection by fixing disc loading; the rotation does not escape it.

#### Why this section sits between the ledger and the contracts

**The argument of the next section depends on this one.** If the three charges were one quantity,
a single number could rank architectures regardless of how the charges were weighed. **Because at
least two of them move independently, any ranking must say how they were weighed** — and a sizing
contract is exactly such a weighing. Section 13 shows what happens to the ranking when the contract
changes, and it can do so only because this section has shown that there is more than one thing
being weighed.

---

## 6. What I am asking

1. **Is the narrowing right?** The skeleton promised three; the section delivers two and says the
   third is untested. **Is that the honest form, or is there a way to test Bill 1 at scale that I
   have missed** — one that does not run through the battery specific-power question Section 14 owns?
2. **Is "held within 5 percent by a design rule" evidence of anything?** The section argues it is:
   that Bill 3 *can* be held flat while Bill 2 falls threefold shows they are distinct. **Is that
   argument sound, or does fixing one quantity by construction make the comparison trivial?**
3. **Is refusing the three-digit agreement too cautious?** The published figure may be right with
   unrounded solidities that are simply not in the repository. The section declines to use it
   because it cannot be traced. **Is that the correct call?**
4. **Does Step 12 hand off to Step 13?** The closing argument is that a ranking must name the
   contract *because* at least two charges move independently. **Does that carry, given that only
   two were shown to?**

**No source is needed for any of this.** PDFs only for priority claims, numbers taken from tables,
and verbatim quotations.
