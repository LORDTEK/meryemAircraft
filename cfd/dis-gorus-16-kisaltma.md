# Round 11 — the paper is 31,000 words. Two questions.

Freeze conditions from Round 10 are met: yaw was examined (it found something —
see below), the tilt framing is fixed, Zenodo v4 is out, and the repository
landing page now carries the shown/not-shown table.

Then I measured the manuscript. **30,891 words. 16 references.** Drones research
articles run 8,000–12,000 words with 40–70 references. We are 3× long and
one-third cited. Neither number is a formatting problem.

---

## What yaw found, briefly

Authority is fine and better than expected: the yaw arm is the **semi-span**, not
the frame length, so yaw gets 55.9 N·m against pitch's 23.0 — **2.4×**, a
geometric property nobody had noticed. I_zz = 33.7 kg·m².

Stability is not fine. The vortex-lattice solution gives **C_n_β = 0** for the
planform — a planar wing has no side-force surface. Sweep gives roll-due-to-
sideslip (C_l_β = −0.045) and no weathercock at all. Directional stability must
come from the **tip-frame fairings**, which the paper had introduced purely as a
drag measure. Required fairing chord: 21 mm for C_n_β = 0.03, 34 mm for 0.05 —
inside the 50–70 mm a 20 mm faired strut needs anyway. So: comfortable, but a
**new requirement on a component whose section is unselected.**

---

## Question 1 — the shortening plan

Current and proposed, in words:

| Section | now | proposed | what leaves |
|---|---:|---:|---|
| 1 Introduction | 1358 | 1100 | — |
| 2 Background | 1851 | 900 | the historical survey → S0 |
| 3 Architectural tax | 3312 | 2200 | worked examples of the transfers → S5 |
| 4 Configuration | 3646 | 1800 | roll/yaw derivations → S4 |
| 5 Tax audited | 3111 | 1600 | the three-contract tables → S5 |
| 6 Reference designs | 5941 | 1800 | CFD verification + component build-up → S1, S2 |
| 7 Transition | 4884 | 1400 | full envelope, rotation profiles → S3 |
| 8 Limitations | 4444 | 900 | the long enumeration → S6, keeping the honest core |
| 9 Conclusion | 1405 | 700 | — |
| **total** | **29,952** | **~12,400** | |

Supplementary Material (MDPI hosts it free, and the full 71-page version stays on
Zenodo with a DOI the paper cites):

- **S1** CFD verification: three grids, four wall resolutions, two turbulence
  models, initialisation spread, symmetry selection
- **S2** Component mass build-up, item by item, with break-even values
- **S3** Transition design envelope and rotation profiles
- **S4** Control axes in full — neutral point, CG window, roll damping
  computation and limit cycle, yaw fin sizing
- **S5** The three sizing contracts, all twelve cells, sensitivity sweeps
- **S6** The full limitations enumeration

**What I am asking.** Is this the right split? Specifically: (a) is 12,400 still
too long — should the target be 9,000? (b) does moving the CFD out of the main
text weaken the paper's strongest computed result, or does it help by removing
the part reviewers will not read? (c) §8 is where the paper's honesty lives —
cutting it to 900 words worries me more than any other cut. Is that the wrong
place to save?

---

## Question 2 — citations. This is the one I want you on.

**16 references, 11 of them cited exactly once.** That pattern reads as thin
engagement regardless of whether the work is sound.

The cause is a rule we imposed on ourselves: **no number is attached to a source
we have not read first-hand.** Search-engine summaries gave us three wrong
numbers early on and we caught them by reading the originals, so the rule earns
its keep. But it is also why we are at 16.

**And there is a worse problem, which the last two rounds created.** Two claims
that are now load-bearing rest on literature we do not cite at all:

1. *"Chordwise fences and Gurney strips of one to two percent chord are reported
   to deliver ΔC_L of 0.1 to 0.3"* — this is what makes the roll requirement
   plausible. **Uncited.**
2. *"Reflexed sections typically deliver C_m0 of 0.02 to 0.05"* — this is what
   makes the trim requirement reachable. **Uncited.**

A third, older one: *"post-stall C_m of 0.1–0.3 for swept planforms."* Also
uncited.

So the reference work is not cosmetic. Three requirement statements currently
lean on remembered ranges.

**What I want your advice on:**

- Which literature areas would a Drones reviewer expect and find missing? My own
  list: recent tail-sitter UAV work (2015–2025), eVTOL sizing methodology, BWB
  UAV aerodynamics, hybrid-electric UAV propulsion, tail-sitter transition
  control, Gurney/fence effectiveness, flying-wing directional stability with
  tip fins, VLM accuracy for swept low-AR wings.
- Of those, which are **necessary** (a claim depends on them) versus merely
  **expected** (a reviewer would like to see them)?
- Is it defensible to submit with ~25 references and a stated first-hand-reading
  policy, or does that read as an excuse?
- Is there a way to cite honestly for a *range* we have not verified —
  e.g. "values in this range are reported [x,y]" with the range attributed
  rather than adopted — or is that still a claim we must verify?

Note our constraint: the environment I work in cannot reach journal sites. Every
paper has to be obtained by the authors and read before it can be cited. So your
answer to "which are necessary" directly sets what they spend their time on.
Please rank, do not list.
