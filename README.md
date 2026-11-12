# meryemAircraft

**A tail-sitting blended-wing body that changes between hover and cruise by rotating the
whole airframe, with fixed-pitch coaxial propulsors that keep one orientation relative to
the body.** This repository holds the analysis code of the paper, the design record and
the earlier versions. The current paper, its supplement and every computation behind it
are deposited on Zenodo.

Five stations carry ten rotors, each station a coaxial contra-rotating pair. **One pair at
the nose** produces all propulsive thrust in both regimes and carries the whole takeoff
margin; **four small pairs at the wing tips** are for control, not lift. Every rotor has
fixed pitch and its own electric machine. Pitch and yaw come from differential thrust of
the tip pairs; roll is assigned to **a single modulated strip** on the lower surface. The
power plant is a series hybrid: the engine is sized by cruise, and a battery buffer
supplies the difference in the vertical phases. There is no pivot or tilting joint, no
nacelle actuator, no variable-pitch hub, no dedicated lift rotor and no rotor stowing or
stopping mechanism.

---

## The paper

**meryemAircraft: A Blended-Wing-Body Tail-Sitter with Body-Fixed Coaxial Propulsors**
Meryem Gülmen, Berke Gülmen, Ömer Gülmen · version 10, 12 November 2026

Hybrid vertical-takeoff aircraft change between hover and cruise by carrying two
propulsor sets or by reorienting one. meryemAircraft does neither, so it carries none of
the mechanism classes a tilting architecture uses to change regime. Doing without them is
paid for in exposed drag and in installed power, and the paper prices that payment. It
divides the price of hover into three accounts (carried hover mass, exposed cruise drag,
and continuous power sized to the hover peak), closes the design on a buffered series
hybrid, and compares it with a lift-plus-cruise layout under three sizing contracts, the
rules that fix what a comparison holds equal.

| | |
|---|---|
| DOI, always the latest version | [10.5281/zenodo.22144194](https://doi.org/10.5281/zenodo.22144194) |
| Version 10 (current) | [10.5281/zenodo.24169404](https://doi.org/10.5281/zenodo.24169404) |
| Paper and supplement | `meryemAircraft-v10.pdf` (30 pages), `meryemAircraft-v10-supplement.pdf` (34 pages), in the deposit |
| Sources | `meryemAircraft-v10-source.zip`: the LaTeX sources and `numbers.tex`, which holds every number of the paper as a macro labelled with the file it is read from |
| Analysis code | `meryemAircraft-v10-code.zip`: [`aero/`](aero/) of this repository at commit `628b027` |
| Computations | `meryemAircraft-v10-computations.zip`: scripts, inputs and outputs of the closures, the takeoff, hover and landing model, the sizing contracts and the sensitivities, with the RANS cases, their configurations, logs and convergence histories |
| RANS surface solutions | `meryemAircraft-v10-rans-surfaces.zip` |

**Status: not peer reviewed.** Version 10 is a preprint; the manuscript was submitted to
*The Aeronautical Journal* (Royal Aeronautical Society) on 12 November 2026 and is under
consideration there. Earlier versions were declined by editors without peer review (Drones
and Aerospace, September 2026; Journal of Aircraft, October 2026).

### Headline results

All of these are computed; none is measured or flown.

- **Sizing.** For a 13 kg payload, sized from a 50 kg reference design (span 3.453 m, wing
  area 1.979 m², aspect ratio 6.03) at a cruise speed of 24 m/s with a nose-only static
  thrust-to-weight ratio of 1.25, the loop closes at a takeoff mass of **58.3 to 59.8 kg**
  at the model's hover figure of merit, and at 66.3 to 68.4 kg at a figure of merit of
  0.70. Across the rotor-section and frame-drag data sources examined the closures span
  57.7 to 61.8 kg.
- **Range.** The closures carry the payload 1,096 to 1,378 km, 12.7 to 16.0 h, on a fuel
  fraction of 0.16 with no reserve; 879 to 1,519 km across the drag-data sources, at a
  thermal efficiency the paper calls optimistic.
- **Cruise efficiency.** The aerodynamic lift-to-drag ratio is 10.40 to 12.10 with the
  tip frames and the driven tip rotors charged; with the computed propeller efficiency of
  0.632 to 0.683 the effective lift-to-drag ratio is **6.57 to 8.26**.
- **Where it pays.** The attitude-control tip pairs and the frames that carry them stay
  in the cruise flow and take **47 to 79 percent of the zero-lift drag** across the
  drag-data sources. That is where the configuration should be improved.
- **Rankings depend on the contract.** The range margin of a lift-plus-cruise layout over
  this aircraft shifts by **75 to 82 percentage points** across three sizing contracts
  and changes sign between them at every closure, for the competitor assumed.
- **Takeoff, hover and landing.** On a moment law from steady RANS at high incidence, a
  three-degree-of-freedom model settles the takeoff up to a 10 m/s steady headwind at a
  tip rating of 23.0 N·m and lands by a climbing flare that rises 32 to 53 m.

### What is claimed, and against whom

The contribution is the architecture. The comparisons have different opponents and are
not interchangeable.

| Axis | Opponent | Claim |
|---|---|---|
| Regime change without a propulsor-reorienting mechanism | Tilting architectures | **The contribution.** None of the five mechanism classes counted in the paper is present. In that sense the aircraft is mechanically simpler, though not one in which nothing moves; part count, mass and reliability are not compared. |
| Cruise efficiency | Rotorcraft | **Claimed where the evidence carries it.** Against a published NASA sizing set, the effective lift-to-drag ratio is 34 to 69 percent above a turboshaft quadrotor's (4.9) and 13 to 42 percent above an all-electric quadrotor's (5.8); against the helicopters of that set (5.4 to 7.2) it is higher except against the electric side-by-side. Independent analyses in a common definition, not a controlled comparison. |
| Cruise efficiency | Winged hybrid concepts | **Not claimed.** It is 3 to 24 percent below the winged pair of the same set (8.5 and 8.6). |
| Range | Lift-plus-cruise | **Not claimed.** The sign of the range margin changes with the sizing contract. |

What is eliminated against tilting architectures is the *class of mechanism that
reorients a propulsor or removes a rotor from one regime's flow*. It is not a claim that
nothing on the aircraft moves: beyond the rotation of the rotors, the strip changes
configuration, deployable in two halves, and the actuator inventory is the propulsion
machines plus the strip.

---

## What is shown and what is not

No aircraft has been built or flown, and no wind-tunnel test has been made on this
geometry. The paper sets each headline claim against its evidence and against what would
refute it (Supplement Table S0); the list below follows that table and the paper's
limitations.

| | Status |
|---|---|
| Regime change with none of the counted mechanism classes | **Inventory of the design.** A brake or lock for the tip rotors, if found necessary, would add one class. |
| Closure at 58.3 to 59.8 kg | **Computed.** It establishes that the configuration is arithmetically self-consistent on the declared package; it does not establish that the package exists. |
| Hover figure of merit | **Model value, not measured.** At 0.70 the closures are 66.3 to 68.4 kg; at 0.65, 72.0 to 74.5 kg. |
| Tip hardware as the largest drag item | **Computed** from two section-data sources in one solver, against a threshold stated before the second run; not measured. |
| Engine sized by cruise, not by the hover peak | **Computed.** |
| Ranking against lift-plus-cruise depends on the contract | **Computed**, in closed form and in the loop, under stated competitor assumptions. |
| Takeoff, hover in wind, landing | **Computed, not flown.** Three degrees of freedom; the pitching-moment law is steady RANS that is not validated, with no data beyond 40.9 degrees; no dynamic stall, slipstream, ground effect, gusts or lateral axes. |
| Energy store | **Rated on cell data, not measured on a whole pack.** At the cited bench average the closures are 55 to 56 percent heavier. |
| Hover heading authority of the strip | **Not established.** The strip's own force is below both of the paper's screens; more rests on a circulation increment that is assumed. |
| Attitude control | **Sized, not designed as a control loop.** The hover torque residual and gust rejection are not analysed. |
| Airframe mass | **A construction constant** (fraction 0.30), not a structural sizing; heat rejection and engine installation are not sized. |
| Altitude and cold | **Limitations.** Ranges are modelled at sea level and the store is rated on cell data at 25 °C; at 2,000 m a 60 s hover lasts 33 to 36 s at the takeoff mass and holds at the landing mass; at −10 °C the pack needs pre-heating. |

The missions considered are observation and small cargo, water by hose included; the
design is not sized for fire suppression.

---

## What is here

```
aero/           Analysis code of the paper (the part archived with version 10): sizing loop,
                contracts, drag build-up, propellers, buffer, stability, transition checks
paper/          Earlier versions of the paper (to version 8), their working record and build scripts
figures/        Figures and the parametric geometry model of the earlier versions
cfd/            Earlier CFD setups and their validation record
patent/         Texts and drawings of the Turkish patent application (in Turkish)
references/     Record of the literature read
presentation/   Presentation material
video/          Visualisation
```

The text of version 10, the scripts that produce its tables and the RANS work are **not
in this repository**; they are in the Zenodo deposit listed above.

## Reproducing the numbers of version 10

Every number of the paper and the supplement is a macro of `numbers.tex` (in the source
archive). The comment after each macro names where the value is read from: a file of the
computations archive, a cited reference, a stated arithmetic, or a design decision of the
authors. `README.txt` in the computations archive describes each folder and says which
script produces which result; `MANIFEST.txt` lists every file with its SHA-256. The
analysis code those scripts import is [`aero/`](aero/) at commit `628b027`.

The deposit also carries the record of two re-implementations of the sizing closures of
version 9 from its frozen text, made without access to the code. That is a
reproducibility check of version 9, not a validation.

## Earlier versions in this repository

[`paper/`](paper/) and [`figures/`](figures/) hold the paper as it stood in versions 5 to
7 (*The Architectural Cost of Hybrid VTOL*; single-file sources `paper/paper-v7.md` and
its supplement), the working record of version 8, and their build and verification
scripts; [`paper/VERSIONS.md`](paper/VERSIONS.md) records the file-name translation of
16 September 2026. Those texts describe an earlier design basis (a 50 kg closure,
free-wheeling tip rotors, another transition model). **Where they differ from
version 10, version 10 holds.**

## Version history

Published versions are immutable; each remains reachable at its own DOI.

| Version | Date | Substance |
|---|---|---|
| **v10** | 2026-11-12 | Transition model corrected (the aerodynamic pitching moment had entered the pitch equation with the wrong sign) and the design revised on it: the nose pair alone carries the takeoff margin at a thrust-to-weight ratio of 1.25, the tip pairs serve control only, cruise is at 24 m/s self-trimmed by washout, the buffer is sized on power-cell data, and takeoff, hover and landing are computed in one three-degree-of-freedom model on a RANS moment law. 58.3 to 59.8 kg. [10.5281/zenodo.24169404](https://doi.org/10.5281/zenodo.24169404) |
| v9 | 2026-10-29 | First version under the present title, written as a journal article; closures at 52.3 to 57.5 kg. Its transition results are withdrawn by version 10. [10.5281/zenodo.23754355](https://doi.org/10.5281/zenodo.23754355) |
| v8 | 2026-10-17 | Rewritten around the architecture, under the title *meryemAircraft: Tail-Sitting Blended-Wing Body for Vertical Takeoff Without Propulsor Reorientation*. [10.5281/zenodo.23437041](https://doi.org/10.5281/zenodo.23437041) |
| v7 | 2026-09-13 | Claim structure rebuilt onto four axes with four different opponents; the mechanism claim narrowed to the propulsor-reorientation class. [10.5281/zenodo.22745666](https://doi.org/10.5281/zenodo.22745666) |
| v6 | 2026-09-11 | Figure and table production defects closed; all 22 tables numbered, captioned and cited. |
| v5 | 2026-09-10 | Supplementary material separated; sizing contracts consolidated. |
| v4 | 2026-09-08 | Framework-centred restructuring; capability sentences rewritten as requirements. Three control axes audited. |
| v3 | 2026-09-05 | Three-dimensional solution for the centre body. |
| v2 | 2026-08-29 | Range method corrected (cruise-point polar instead of maximum L/D). |
| v1 | 2026-08 | First release. [10.5281/zenodo.22144195](https://doi.org/10.5281/zenodo.22144195) |

## Patent

A patent application for the configuration was filed in Türkiye (2026-08). The texts and
drawings under `patent/` are the drafts the application was based on, and are **in
Turkish**, as filed. They were not prepared by a patent attorney.

## Licence

Text, figures and scripts of this repository: **AGPL-3.0**, see [LICENSE](LICENSE).
The Zenodo versions of the paper are published under **CC BY 4.0**.

---

*The concept, architecture, design and solution approach of this work are the authors'
own. Generative AI tools were used in its preparation: to draft and revise text, to search
and check the literature, to review the manuscript, and to write and check analysis code.
The authors reviewed and edited that content and take full responsibility for it.*
