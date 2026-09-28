# Number identity, date identity, figure scripts and the "biplane" heading (Round 139)

Identity = value + unit + object + model/geometry + state + date (Round 102, 133, 137). Method (Claude): every number that occurs in
two or more step bodies was listed with its context (`ALL-STEPS.md`, 46 groups) and read; the dated witnesses were checked against the
files in `references/`; the four v8 figure scripts' label strings were checked against the body and the supplement.

## Numbers in two or more sections — result

Consistent in value, unit and object, except:

| # | Where | Finding |
|---|---|---|
| S-61 | Step 10 (five uses), Step 11 (one) | *"the published zero-lift value of 0.0248"*, *"the published drag coefficient"*, *"the published propeller efficiency"*, *"reproduces the published aircraft"*, *"at its published mass"*, *"the 0.80 the published chain assumed"*. The object is the 50 kg reference design as first sized (`aero/closure.py`: 50.1 kg, L/D 11.88, 1 583 km; C_D0 0.0248, η_p 0.80). The body never identifies it; it reads as a previous release (CLAUDE §4) |
| N5 | Step 9 T1 (protected) | *"against helicopters the published comparison is mixed"*: the comparison is this paper's (Section 6) against published figures; "published comparison" can be read as someone else's |
| N6 | S14, low-Reynolds row | *"The 0.0154 rotor term in every closure"*: the base value is 0.0154 in every closure; the adverse-end closures carry it as 0.0169 (the ten-percent margin on the whole build-up, S11) |

Recorded, no change:
- **0.80** is two objects with one assumed value: the reference design's first sizing (Step 11) and both competitors (Step 13). Same
  origin, same status (assumed). Entered in `v8-coincidences-reviewed.md`.
- **5.4**: helicopter L/De low end (Step 6) and altitude loss in metres (Step 10). Different units; no collision.
- **0.0154 at 50 kg (Step 12)** is the free-wheeling state at the design's own cruise speed (S12: *"the free-wheeling state solved at
  each design's own cruise speed"*), the same state as Sections 10 and 11 (DeepSeek R138-P3). The 1 000 kg values 0.0068 and 0.0045–0.0100
  are the same state.
- **Transition figures (Step 10).** `aero/transition_dynamics.py` runs on the reference design's assumed drag (C_D0 0.0248, e 0.85).
  5.4 m is the linear rotation profile (the kinematic model's own); the other two profiles give 6.6 and 6.3 m (as `aero/README.md`
  records). Re-run this round at the bracket ends with the computed span efficiency (C_D0 0.0285 and 0.0381, e 0.817): 5.44 and 5.45 m.
  The drag input does not move the figure; no body change.

## Dated witnesses

| Body | Date identity | File | Status |
|---|---|---|---|
| XFY-1, 1954 | flight programme | NASA 19810010574 | verified |
| coaxial tail-sitter, 2012 | *ICA* 3(4), published online November 2012 | `ica20120400001_12673514.pdf` | verified |
| quadrotor tail-sitter without control surfaces, 2013 | ICRA 2013, pp. 317–322 | **not in the repository** — title only, De Wagter 2018 p. 24 (bibliography), mentioned p. 2 | **attributed** — the body sentence restates the title |
| coaxial micro air vehicle, 2014 | ICAS 2014 (copyright statement) | `2014_0529_paper.pdf` | verified |
| flying-wing tail-sitter, 2018 | IROS 2018 | `Yang-Zhu-2018_IROS_…pdf` | verified |
| long-range tail-sitter, 2018 | *J. Field Robotics* 2018 | `Wagter_et_al_2018_…pdf` | verified |
| BWB tail-sitter, 2025 | *J. Informatics Education and Research* 5(2), 2025 | SkySwift PDF | verified |
| Rohith, 2026 | *J. Aircraft* 63(2) | Rohith PDF | verified |
| coaxial tail-sitter with series-hybrid store, 2025 | placeholder; version fixed before submission | Vegh manuscript R3 | manuscript |
| single-aisle airliner, 2016 | SAE 2016-01-2014 | Rheaume–Lents PDF | verified |

## Figure scripts

| Script | Finding |
|---|---|
| f1, f3 | no numbers in labels; f3's categories match Section 6 |
| f2a | every number in the body (3.453, 1.726, 0.71, 1.20, 0.20, 2.43); roll label matches Section 8 (*"reaction torque could produce it, and is declined"*) |
| **f2b (F1)** | **"slipstream boundary 0.67 m → 0.47 m"** is on the figure and nowhere in the body or supplement; it is the estimate Section 8 says is *"not derived"* (S-37). **"b/2 = 1.73 m"** where f2a and the body say 1.726. The "0.47" matched only by coincidence (Step 12's diameter ratio) |

## The "biplane" heading (ChatGPT, Round 135)

Step 1: **"A buffered series hybrid on a winged tail-sitter has been sized."** Rohith et al. call the architecture *"series-hybrid"*
(p. 584–585, Table 5; conclusions p. 589) and the vehicles *"winged biplane tail-sitters"*; the sentence under the heading says
*"biplane"*. The heading is faithful; no change.
