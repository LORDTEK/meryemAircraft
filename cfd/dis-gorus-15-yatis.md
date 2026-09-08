# Round 10 — you were right about roll, and the number did not survive

YZ3 said the weakest load-bearing claim was not trim but roll. I went and
checked it with the same effort I had spent on trim. The claim did not hold.

## What I computed (not taken from the literature)

- **Roll inertia I_xx = 25.0 kg·m²** — 2.5× the pitch inertia of 9.81, because
  the mass is spread along the span, not the chord. The roll axis had never
  been examined.
- **Roll damping |C_l_p| = 0.358**, computed for this planform by imposing the
  helix-angle twist θ(y) = −arctan(p·y/V) on a vortex-lattice solution.
  Linear in p to 0.4 rad/s (0.3% spread), converged to 1.3% over a threefold
  refinement. Previously this coefficient came from the literature.
- Cruise damping slope **77.6 N·m per rad/s**, roll time constant **0.32 s**.

## The requirement, inverted

| target | moment required |
|---|---|
| 20 °/s | **27.1 N·m** |
| 25 °/s | 33.9 N·m |
| the paper's 46 N·m | → 34.0 °/s |

Time to a 30° bank comes out at 1.21 s. Section 4.4 said "1.2 to 1.5 s". That
part held.

## The finding: 46 N·m cannot come from the strip's own force

The strip is a 45° diagonal fence, 1.164 m long, 2→6 cm high, area 0.0466 m².
For a swept fence the normal force scales with cos²(sweep).

| mechanism | moment |
|---|---|
| the strip's own force, C_N = 1.3 (an upper bound) | **11.3 N·m** |
| change in the half-wing's circulation, ΔC_L = 0.10 | 22.4 N·m |
| ΔC_L = 0.15 | 33.7 N·m |
| ΔC_L = 0.20 | **44.9 N·m** ← where 46 came from |

46 N·m would need C_N = 5.3. A flat plate normal to the flow gives 1.1–1.3.
So the strip's own drag falls short by a factor of about four.

The moment can only come from the second mechanism — the strip changes the
circulation of the half-wing it sits on, Gurney-flap style, so the acting area
is the **wing's** (0.802 m²), not the strip's. The paper never said which
mechanism it meant.

**20 °/s then requires ΔC_L ≈ 0.12.** Published Gurney and fence data give
0.1–0.3, so this is plausible — and it is now written as a requirement, not an
authority. Same treatment as trim.

## Two things this turned up that were not in the paper at all

**Hover is the harder case, structurally.** At V = 0 there is no aerodynamic
damping — the roll axis is a double integrator. The rate never settles; the
strip must be commanded off. Roll control in hover is therefore a tighter
problem than in cruise, which is the reverse of the usual situation.

**The actuator has a speed requirement.** First-order roll dynamics with a
deadband and a finite deployment time:

| deadband | delay | limit cycle |
|---|---|---|
| 2° | 50 ms | ±0.2° |
| 2° | 150 ms | **±9.4°** |

So being on-off is not disqualifying — but only if the device is fast, and the
threshold sits where real actuators differ. This is a new stated requirement.

## Also done this round

- **Convention audit** (YZ1's request). Six tests on whether the two chains
  share an origin, a sign convention, and a reference chord. All six pass; in
  particular W(x_np − x_cg) and C_L × margin × q S c̄ both give 39.82 N·m. One
  honest residual: the margin is 12.5% derived via the neutral point and 12.8%
  taken directly from the solver's moment about the CG. Both are now in the text.
- **Capability sentences converted to requirement language** throughout. The
  strip is now "assigned" the roll rather than "giving" it. The altitude-loss
  result is tied to the point-mass model. Buffer cell class named (high-power
  Li-ion/LiPo, 20–30 C, explicitly not the high-energy class).

## The question

I was about to freeze a public version (Zenodo v4) and submit to Drones. Then
this happened — a load-bearing number in Section 4.4 that did not survive being
checked, found only because YZ3 pointed at the right place.

So: **is there a reason to keep looking before freezing, or is the marginal
return now low enough to stop?**

Concretely, what I have *not* audited to this depth:
- the yaw axis (differential tip thrust; never examined separately)
- the tip-frame drag coefficients (disclosed as literature values)
- the tilt architecture's L/D multiplier of 1.0 in Section 5.5, which YZ5
  flagged as still on credit and which the comparison result rests on
- Section 6.6's CFD drag bound and its uncertainty budget

Tell me which of those you would check before submission and which you would
leave in the limitations section. If your answer is "none, submit", say that
plainly — I would rather stop at the right point than keep polishing.
