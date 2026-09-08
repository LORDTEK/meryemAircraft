# Round 4 — rotational authority, and the road ahead

Thank you for the last round. It was the most useful one so far, and this
text opens by saying what it changed rather than by asking anything.

**The same request about the shape of your answer as last time.** Please
flag only what would change a conclusion. "No error found" is a complete
and welcome reply. We are deliberately trying not to polish numbers.

---

# 1. What your last round changed in the paper

Every item below was a comment from one of you, and every one is now in
the text. This is reported first so that you are reviewing the paper as
it now stands, not as it stood when you last saw it.

| Your comment | What changed |
|---|---|
| "Strength is not the driver" over-reads a single load case *(all three of you)* | **Withdrawn.** Replaced by "global span bending is not the sizing driver in this static model," followed by an explicit list of what the 41 g does not cover — buckling, core shear, torsion, load introduction, minimum gauge, damage tolerance, aeroelastic margin — and a statement that none of it licenses trimming the shell or internal-structure allowances. |
| "A second steady state need not localise" | **Withdrawn.** That inference is gone from §6.6. |
| Symmetry test is a selection criterion, not a proof | **Reworded.** bl_E is now "taken as the reference state"; the mesh-asymmetry defence is labelled a supporting argument, explicitly because the equations are non-linear. |
| "The light design closes" must be conditional | **Rewritten** as a conditional in §6.7, §8.2, the abstract, the introduction and the conclusion: it closes *if* shell areal density ≤ 1.78 kg m⁻² *and* everything still outside the model together stays under 2.2 kg. |
| Do not claim heavy-line closure; leave the exponent unmeasured | **Done,** and no side of 0.467 is argued for. The stated reason is that a structural model would be standing in for a measurement. §6.4's scale-invariance is now qualified: the fractions are a property of the sizing rules and have not been shown to be realisable at 1000 kg. |
| Tip frames: "the landing case" is unproven | **Narrowed** to "a vertical landing case," with off-axis touchdown, ground gust and nose thrust moment named as unexamined. |
| The three contracts | **Given equal standing,** with one sentence of mission language: §6.2's mission is closest to the fixed-fraction column, which is the only column where tilt leads and leads only on a credit it was given — so quoting it alone would restate the credit as a conclusion. |
| "Check the four categories that usually go missing" | **Checked and reported.** Propeller blades and coaxial hubs, power electronics sized on hover peak, fuel containment, and control actuation are all present; the last is small only because there are no control surfaces. The one category *not* separately modelled is local load introduction, and §8.2 now says so. |
| "Is the buffer power- or energy-limited?" | **A real omission, now fixed.** See below. |
| The 4.5 kg contingency figure looks inconsistent with a 2.2 kg margin | **A real arithmetic error of ours.** See below. |

## Two things you caught that were genuinely wrong

**The contingency was double-counted.** We had written that a further
4.5 kg of unaccounted mass was survivable. The break-even contingency of
4.89 kg is the *whole* of that line, of which 2.68 kg is already in the
budget; the additional survivable mass is 2.21 kg — which is the same
2.2 kg margin, counted once. The paper now says so and records the
correction. The budget is tighter than we had written.

**The battery buffer is specified by power, not energy, and that was
never stated.** It must supply 8.3 kW from 1.8 kg — 4.6 kW kg⁻¹, about
26 C at 180 Wh kg⁻¹. Energy does not become the binding constraint until
roughly 140 s of hover, well beyond the flight profile. The heavy design
is in the same regime at 4.1 kW kg⁻¹. Cells that discharge that hard
generally carry less energy per kilogram, which lowers the crossover
further. So the buffer masses are a cell-selection requirement, not a
free parameter, and a demanding one. Now in §6.7.

---

# 2. This round: rotational authority

## The choice we made, and why

You were split on what to do next — 6-DoF, bound the shell exponent, or
re-read the paper. We did the re-read first because it needed no new
model, and then took up 6-DoF. On looking at it properly, we concluded
that a full 6-DoF **cannot honestly be built**: it needs pitching-moment
coefficients through ninety degrees of incidence, and no such data exists
for this planform. Producing it would mean a wind tunnel or a fresh CFD
campaign, and you had all asked us not to reopen CFD.

So we narrowed it to the part that can be closed, and said so in the
paper. **The test is an inertial lower bound:** if the tip propellers
cannot turn the aircraft's own inertia, they certainly cannot turn it
against aerodynamic moment as well. If they can, the aerodynamic margin
stays unknown and is reported as unknown.

This was possible only because of the mass build-up from last round: the
inertia comes from those component masses distributed over the planform.
Before that work, it could not have been computed at all.

## Findings

**The rotation profile in §7.4 cannot be produced by any finite moment.**
That simulation ramps body angle linearly — zero torque throughout,
infinite torque at each end. The nearest profile a finite moment can
produce needs a peak angular acceleration of 6Δθ/t_r². This was a silent
assumption in the existing model; it now has a number, and the check uses
the stricter value.

**Inertia, from the component build-up:** I_yy = 7.04 kg m² (light) and
1918 kg m² (heavy) about the spanwise axis, which is the axis the
transition turns about; CG at 57 % and 58 % of root chord.

**Both designs have authority, with different margins:**

| | Required | Available | Margin | Shortest rotation |
|---|---:|---:|---:|---:|
| Light, t_r = 2 s | 16.6 N m | 46.0 N m | **2.8 ×** | 1.20 s |
| Heavy, t_r = 4 s | 1130 N m | 1905 N m | **1.69 ×** | 3.08 s |

The light design needs 5.84 N per pair to turn its own inertia — 36 % of
the 16.2 N quoted in §4.3.

**A check on our own published number.** That 16.2 N at 335 W and 0.20 m
implies a figure of merit of 0.702 with no coaxial interference loss,
where the hover figure of merit used elsewhere in the paper is 0.599.
Recomputing at 0.599 with a 15 % coaxial loss gives 12.4 N and a margin of
2.1 ×. The conclusion survives either way, but the basis of 16.2 N was not
stated anywhere and now is.

**A scaling law we did not have.** Available moment goes as scale³,
inertia as scale⁵, required acceleration as 1/t_r². So margin goes as
t_r²/scale², and holding it constant requires rotation time to grow
*linearly* with scale. From 50 kg to 1000 kg is a factor 3.345 in linear
scale, so preserving the light margin would need 6.7 s rather than the 4 s
used — which is exactly why the heavy margin is 1.69 and not 2.8. §7.4
already said the larger aircraft must rotate more slowly; this adds that
what tightens is the *control* margin, not only the altitude loss.

**What it does not establish,** stated in the section itself: the centre
of pressure travels through the rotation and the moment that produces is
not computed. These are inertial margins, not total control margins.

---

# 3. The road ahead

Our plan, in order:

1. **Nothing further on the mass budget or the CFD.** Both are labelled
   with their conditions. Polishing either would produce numbers without
   measurements.
2. **§8.14 item 3 is reduced from a missing analysis to a missing
   measurement** — moment coefficients through 90°. We propose to leave it
   there and say plainly that it needs an experiment.
3. **Journal preparation:** figure quality, reference completeness,
   formatting to a target journal, and a final consistency pass.

We are not planning further modelling. The reasoning is that every
remaining item is either blocked on measurement or would be a model
substituting for one.

---

# QUESTIONS

1. **Is there something obvious to you that we are not seeing?** The paper
   has changed a good deal; a fresh look at the whole rather than at our
   list is what we would value most.
2. **Do you have a serious objection to the road map in Part 3** — in
   particular to stopping the modelling here?
3. **On the narrowing of 6-DoF:** was reducing it to an inertial lower
   bound the right call, or does it claim less than it should, or more?
4. Anything in Part 1 that we implemented in a way you did not intend.
