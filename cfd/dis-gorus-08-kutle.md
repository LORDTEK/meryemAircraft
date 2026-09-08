# Round 3 — auditing the mass budget

**Before anything else, a request about the shape of your answer.**

I am not looking for refinements. If your reply would change a number
without changing a conclusion, please leave it out. Specifically:
please do not propose better correlations, tighter coefficients, or
extra sweeps unless the current value is wrong enough to flip a
verdict. I have deliberately dropped two of my own questions from this
text for failing that test.

What I am looking for is one thing: **is there a mistake here that
makes a conclusion false?** A missing load path, a missing mass
category, an invalid inference. Say "no error found" if that is the
honest answer — that is a useful reply and I will not read it as a
failure to engage.

All three of you said the same thing last round: freeze the CFD, fix
the comparison model, take the mass budget down to components. All
three are done. **The weight of this text is in Part 3.** Parts 1 and 2
close out the last round and are short.

---

# 1. CFD — I withdrew my own reading

You asked me to compare the pressure fields of the two SST solutions.
Done, with no new run. It refuted me.

**Withdrawn:** *"steady RANS is settling into two distinct stationary
solutions."*

- **Separation topology is identical**: 0.02 % reverse-flow area in
  both, over the same streamwise interval (1.003–1.740 m).
- **The pressure-drag difference is spread evenly across the inner
  span** — each of eight bands carries about an eighth of it. A genuine
  second solution branch would localise.

**What replaces it.** Sections are symmetric NACA 00xx, no twist,
α = 0, so **C_L must vanish**:

| | C_L | upper/lower Cp asymmetry |
|---|---|---|
| bl_C (warm-started from SA) | +1.45e−03 | 0.0249 |
| bl_E (mapped from y⁺≈20) | **+1.35e−04** | **0.0011** |

bl_E is ~10× better on both. The induced drag of that residual lift is
negligible (9 ppm of C_D) — so the asymmetry is a **symptom, not the
cause**; but it is the criterion that says which solution is better
conditioned.

This also settled the disagreement between you: a symmetry test decided
it, instead of a third run. The range 0.01201–0.01253 is still
published; where one value is needed, bl_E is chosen on physics rather
than on residuals.

**Question 1.** Is that criterion legitimate? The obvious objection is
mesh asymmetry — but a non-symmetric mesh would bias both cases
equally, so the difference must come from the solution. Is that defence
sufficient, or is there a way it fails?

---

# 2. Three sizing contracts — the third reviewer was right

Two of you said "range being independent of MTOW at fixed fuel fraction
is a correct Breguet property, not an error." True. The third saw that
it is nonetheless the wrong **comparison contract**, because the heavier
architecture is then allowed to carry proportionally more fuel and the
mass bill never reaches the range column. All three contracts are now
computed, with the tilt architecture still credited with paying zero
cruise drag for its mechanism:

| Range vs. the proposed tail-sitter | fixed fuel **fraction** | fixed fuel **mass** | fixed **MTOW** + payload |
|---|---|---|---|
| B — lift + cruise | −14.4 % | −36.5 % | −72.6 % |
| **C — tilt** | **+12.0 %** | **+0.2 %** | **−19.1 %** |

Crossed with the tilt drag multiplier, tilt leads in 3 of 12 cells, all
three in the first column.

One correction: the hand calculation for fixed fuel mass gave −7 %
using 60.3 kg, which is the *fixed-fraction* MTOW. Fixing fuel mass
re-closes tilt at 55.9 kg, giving **+0.2 %**. The fixed-MTOW figure was
exact (−19 % by hand, −19.1 % from the model).

**Question 2.** Should one of the three be the paper's headline table,
or should all three carry equal weight? This is an editorial call, not
a numerical one.

---

# 3. MASS BUDGET — the part to audit

The paper's §6.2 fractions (30 % structure / 16 % propulsion / 4 %
battery / 8 % avionics / 16 % fuel → **26 % payload**) have been rebuilt
from components. Rule: no item is back-solved from the fraction it is
meant to test.

## 3.1 The first run was a warning

It returned **42.8 %** payload. A bottom-up budget that beats its own
target by 60 % is not good news; it means items are missing. Seven
categories were, totalling 3.4 kg: fasteners/adhesive/paint, access
panels, engine mount + cooling + exhaust, coaxial hub/shaft/bearings,
signal harness, payload interface, landing contact pads. A
**contingency allowance** (12 % of dry mass) was also absent.

## 3.2 How it is computed

**Structure.** Wetted area integrated from the planform and the NACA
00xx thickness distribution: **4.14 m²** (planform 1.98 m²). Carbon
sandwich shell at 1.5 kg m⁻² → 6.20 kg. Ribs, bulkheads and bonded
joints at 45 % of shell. **Tip frames sized by the landing case** —
this aircraft lands on them: 3 g vertical arrival, half the weight
through one frame, post as a cantilever → 0.95 kg for both.

**Spar.** At n_ult = 5.25 the root bending moment is **934 N·m**; at
400 MPa over a depth of 0.9 × root thickness the caps need **10.7 mm²**
and weigh **41 g** — 8 parts in 10 000 of MTOW.

**Propulsion.** Nose motor sized by **hover peak**, engine by **cruise**
— the configuration's central claim, visible in the budget as 2.73 kg of
electric machine against 2.60 kg of engine + generator (4 kW/kg and
1 kW/kg).

    m_spar  = 2·2·ρ·[M_root/(σ·h)]·(b/2)·0.35
    m_shell = σ_areal · S_wet
    m_motor = P_hover / (kW/kg)
    m_ICE   = P_cruise_rating / (kW/kg)

## 3.3 The light design closes

| group | build-up | assumed |
|---|---|---|
| structure | 23.8 % | 30 % |
| propulsion | 15.2 % | 16 % |
| battery | 3.6 % | 4 % |
| systems + contingency | 11.0 % | 8 % |
| fuel | 16.0 % | 16 % |
| **payload (residual)** | **30.4 %** | **26 %** |

**2.2 kg in hand.**

## 3.4 But the whole margin sits on one number

Value at which 13 kg of payload stops closing:

| assumption | base | break-even | margin |
|---|---|---|---|
| **shell kg m⁻²** | 1.50 | **1.783** | **19 %** |
| internal structure / shell | 0.45 | 0.723 | 61 % |
| contingency | 0.12 | 0.219 | 82 % |
| motor kW/kg | 4.00 | 2.433 | 39 % |
| ICE + generator kW/kg | 1.00 | 0.623 | 38 % |

Everything else can be substantially worse and the design still closes.
**Above 1.78 kg m⁻² of skin it does not.** The contingency row reads:
about **4.5 kg more unaccounted mass** is survivable, and no more.

## 3.5 The heavy design does NOT close — the real open question

Shell mass ~ scale², MTOW ~ scale³. Constant areal density would make
the shell *fraction* fall as 1/scale, which is plainly wrong — skins on
larger aircraft are not thinner. A constant fraction needs areal density
~ scale¹. The truth is between, and the exponent **was not measured**:

| exponent | shell kg m⁻² | payload kg (target 260) |
|---|---|---|
| 0.00 | 1.50 | 359 ✓ |
| 0.25 | 2.03 | 313 ✓ |
| **0.467** | **2.64** | **260 — break-even** |
| 0.50 | 2.74 | 251 ✗ |
| 1.00 | 5.02 | 52 ✗ |

## 3.6 Where I think the errors would be

1. **Structure came out at 23.8 % against a 30 % target.** The budget is
   lighter than the thing it was meant to test. Having already missed
   seven categories on the first pass, what category am I still not
   seeing?

2. **Is 1.5 kg m⁻² defensible** for a 50 kg-class, 25 %-thick BWB that
   houses all systems internally and takes landing loads through its tip
   frames? The entire result hangs on this one value.

3. **Is "strength is not the driver" a valid inference?** The spar
   weighs 41 g. Is that the known result at this scale, or am I missing
   a load path — torsion box, local introduction at the frame joints,
   flutter, ground handling?

4. **Tip frames were sized by vertical landing.** Is that actually the
   worst case, against propeller thrust moment, a gust on the ground, or
   an off-axis touchdown?

5. **The heavy-line exponent.** Should it be expected above or below
   0.467? Is there a defensible way to bound it, or should it stay
   labelled "not measured"?

---

# QUESTIONS

1. Is the symmetry criterion legitimate? (Part 1)
2. Which contract should be the headline table — or all three equally?
   (Part 2)
3. **Which of the five doubts in 3.6 is a real error, and what do you
   see that is not on my list?** This is the one I actually need.
4. What should the next piece of work be: the 6-DoF transition
   simulation, bounding the heavy-line shell exponent, or a full re-read
   of the paper? One answer, with a reason.
