# Round 5 — one measurement changed the question, so we are asking again

We are not asking you to repeat yourselves. We are asking because a
number we did not have when you last advised has since been measured,
and it points the other way. **No computation has been started.** This
text is a road plan with time estimates, put to you before any of it
runs.

---

# 1. What we measured after your last round

You all advised, reasonably, not to reopen CFD, and to leave the missing
90° pitching-moment coefficients as a missing *measurement*. We accepted
that and implemented everything you asked. Then, while answering a
question about whether the road map was right, we quantified how large
the missing term is.

The inertial check leaves a residual moment — the difference between what
the tip propellers can produce and what turning the aircraft's own
inertia consumes. Setting that against q·S·c̄ gives the pitching-moment
coefficient that would consume it entirely:

| Airspeed during rotation | 10 m s⁻¹ | 15 m s⁻¹ | 20 m s⁻¹ | 30 m s⁻¹ |
|---|---:|---:|---:|---:|
| Light design | 0.172 | **0.076** | 0.043 | 0.019 |
| Heavy design | 0.186 | **0.083** | 0.047 | 0.021 |

Post-stall pitching-moment coefficients on swept planforms at high
incidence are routinely of order 0.1 to 0.3.

**So the inertial margin we reported is the small term.** The unmeasured
term is probably the larger one and possibly several times larger. The
paper now says this, and has demoted the inertial result accordingly:
transition controllability, not the mass budget, is named as the largest
unresolved item in the study.

**That is why we are asking again.** Your advice not to reopen CFD was
given before this threshold existed. With it, the missing measurement is
no longer one open item among fourteen; it is the one the central
architectural claim — transition without control surfaces — rests on.

---

# 2. What a campaign would cost, measured rather than guessed

## The machine

Four cores, 15 GB RAM, and — this is the binding constraint — an
**ephemeral container**. It has already restarted once mid-session and
has silently killed a background run. The longest computation we have
completed in one piece is 9.4 hours.

## Measured cost of what we have already run

| Case | Cells | Iterations | Wall clock |
|---|---:|---:|---:|
| bl_C, steady, cold-ish start | 2 263 560 | 5 000 | **9.4 h** |
| bl_E, steady, mapped start | 2 263 560 | 5 081 | **4.8 h** |

## Estimated cost of a URANS campaign

This is the weakest number in this text and we would like it challenged.
The reasoning: convective time c/V ≈ 0.032 s at the light design point;
roughly 20 convective times to clear the transient and 20 more to
average; at ~300 time steps per convective time that is ~12 000 steps;
with 2–3 PIMPLE outer iterations each, ~30 000 steady-equivalent
iterations. Against the measured 5 000 iterations in 9.4 h, that is
**~56 h ≈ 2.3 days per incidence.**

| Option | What it is | Estimated cost | What it delivers |
|---|---|---:|---|
| **B4** | Full 3-D URANS, fine mesh, 8 incidences 0–90° | **~19 days** | The measurement the paper needs |
| **B3** | 3-D URANS on the coarse y⁺≈20 mesh, 5 incidences | ~4 days | Wall-modelled, in massively separated flow |
| **B2** | 2-D URANS, 3 spanwise sections × 8 incidences | ~2 days | Loses the three-dimensionality that Section 6.6 existed to capture |
| **B1** | Steady RANS α-sweep to 20–25° only | ~2 days | C_m in the attached regime only — about a quarter of the rotation |

**B4 cannot be run here.** Nineteen days of continuous computation is not
available in an environment whose longest completed run is 9.4 hours. It
would need a machine we do not have.

We should also say plainly what we already know about this solver on this
problem: at α = 0 and y⁺ ≈ 1, steady RANS did **not** return a unique
solution — two well-converged starts settled 4.3 % apart in drag, and we
selected between them on a symmetry argument. In massively separated flow
at 45° or 60° incidence, steady RANS is not merely less accurate; it is
the wrong tool. That is why the options above are URANS and not a steady
sweep, and it is also why B1 stops at 25°.

---

# 3. The questions

1. **Does the threshold in Part 1 change your advice?** You said do not
   reopen CFD. That was before we knew the aerodynamic term probably
   dominates the inertial one. Knowing it, would you still say the same?

2. **If it does change your advice, which option?** And more sharply:
   **is any reduced option (B1, B2, B3) worth running at all, or is a
   reduced campaign just another model standing in for the measurement?**
   We are genuinely unsure. B2 would give numbers, but they would be
   two-dimensional numbers for a configuration whose whole aerodynamic
   argument is that two-dimensional treatment is inadequate — the paper
   makes that criticism of its own earlier strip method. We would rather
   run nothing than repeat the mistake we already corrected.

3. **If none of them is worth it, is there a third road we are not
   seeing?** Specifically: is it better to narrow the paper — remove the
   transition claim entirely, publish the architecture, the cruise
   efficiency comparison and the mass budget, and leave transition to a
   separate study with an experiment — than to publish with the item open
   but named?

4. **Challenge the 2.3 days per incidence** if you think it is wrong. If
   the real figure is a quarter of that, B4 becomes possible and the
   answer to question 1 changes.

---

# 4. What we are not asking

We are not asking whether the paper is publishable as it stands; you have
already answered that and we have implemented the corrections. We are
asking whether the newly quantified size of the missing term should
change the decision to stop. If your answer is "no, stop anyway and name
the gap," that is a complete answer and we will take it.
