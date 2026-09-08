# Round 9 — what changed, and the one thing I want you to attack

All three of you agreed on a list last round. It is applied. Here is what
actually changed, with numbers, so you can check rather than take my word.

## 1. A reference-chord error I found while applying your notes

The static margin was quoted on the mean **aerodynamic** chord (0.651 m) but
the trim requirement on the mean **geometric** chord (0.573 m) — a 13.7%
mismatch between two numbers presented side by side. Both are now on MAC.

Neutral point unchanged: 0.859 m from root LE = 34.4% MAC (converged, 0.26%
over 3x refinement). Margin 12.4% -> **12.5% MAC**. Trim requirement
0.063 -> **0.056**.

## 2. CG is now written as an assumption, not a measurement

"In the absence of a detailed internal layout, a first-order packaging rule is
adopted: non-structural masses distributed in proportion to internal volume,
structure in proportion to shell area." One datum: **0.778 m aft of root LE =
80.2% root chord = 21.9% MAC**. Fuel burn shifts it +0.3 points of root chord.

Sensitivity window now tabulated (C_L cruise = 0.45):

| CG, % root | margin, % MAC | camber C_m needed |
|---|---|---|
| 78 | +15.7 | 0.071 |
| 80.2 (rule) | +12.5 | 0.056 |
| 83 | +8.3 | 0.037 |
| 85 | +5.3 | 0.024 |

Reflex sections give 0.02-0.05. So the upper half of the window is reachable
and the lower half is not — which is what turns the rule into a constraint.

## 3. Stability and trim separated

Section 7.6 now has two headings: "**Static stability is shown**" and "**Trim
is not shown. It is a requirement, and the requirement is quantified.**" The
sentence "the aircraft is trimmed" does not appear anywhere in the paper.

## 4. Rotation times reframed as actuator-limited lower bounds

Not margins. Smooth-profile minima are 2.01 s (light, reference 2.0 s) and
4.98 s (heavy, reference 5.1 s). Both reference designs sit **at** the
constraint, not clear of it.

## 5. Stale numbers from the old inertia, now corrected

Tightest C_m budgets 0.079/0.015 -> **0.050/0.010**. Heavy design at 4 s:
margins 1.26/0.84 -> **0.97/0.65** (infeasible on both profiles, not just the
smooth one). Rotation margins in Sections 8 and 9: 2.08/2.05 -> **1.49/1.57**
(bang-bang) and 0.99/1.05 (smooth). Mid-rotation C_m in Section 9:
0.32 -> **0.21**. The altitude-loss check was re-run at 4.06 and 4.98 s:
still zero at a 5 m/s entry climb.

## 6. Framework language

"cannot be minimised independently" -> "the same architectural choice need not
minimise all three simultaneously". The NASA comparison is now called an
**external consistency check**, explicitly not a validation, with a sentence
saying corroboration does not establish that there are only three charges.

## 7. Journal decision recorded

Drones, first submission. All three of you converged on it. The Aims & Scope
line recommending experimental validation is written into the record as a
known risk rather than argued away.

---

## The one thing I want you to attack

I have been applying your corrections for several rounds now, and each round
found real errors. That is a good sign about the process and a bad sign about
the manuscript. So:

**Is there a load-bearing claim left in this paper that is still asserted
rather than shown?** I am not asking for more polish. I am asking whether
something in Sections 3-7 would collapse under a referee who checked it the
way you have been checking the ones I brought you.

Specifically I am uneasy about three:

- **The heavy (1000 kg) design's mass budget does not close.** The paper says
  so. Is saying so enough, or does carrying a design point that does not close
  weaken the case study?
- **The shell areal density of 1.5 kg/m2** (break-even 1.78) is a target, not
  a measured property. Everything in the light design's 2.2 kg margin rests
  on it.
- **The trim closure.** Stability is shown; trim is sized but open. Is an open
  trim closure survivable in a configuration paper, or is it the thing a
  referee rejects on?

Short answers. If you think the honest answer is "this is not a Q1 paper
without X", say X.
