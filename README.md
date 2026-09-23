# meryemAircraft

**An uncrewed tail-sitting blended-wing-body configuration with no control surfaces —
and the cost framework built on it.** This repository holds the design record, the
paper produced from it, and the scripts that reproduce every number in that paper.

All propulsive thrust comes from **a single coaxial contra-rotating pair at the nose**;
four small pairs at the wing tips produce attitude moments only; a deployable **strip**
on the lower surface is assigned the roll moment that thrust vectors parallel to the
body axis cannot produce. There are no elevons, no rudder, no tilting mechanism, no
retraction mechanism, and no dedicated lift system.

---

## The paper

**The Architectural Cost of Hybrid VTOL: meryemAircraft, a Propeller-Driven
Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System**
Meryem Gülmen, Berke Gülmen, Ömer Gülmen · 2026

Hybrid VTOL aircraft combine runway independence with wing-borne cruise and pay for it
in cruise efficiency. The paper treats that cost not as an implementation defect but as
**architectural**, and builds it as an accounting framework: the cost falls due in three
coupled currencies — the **mass** of hover hardware carried through cruise, the **drag**
of that hardware when exposed, and a **power system** sized by a condition that holds for
about two percent of the flight. Every remedy surveyed reduces one by raising another.
Expressing the cost this way exposes the condition for escaping it. A second result is
methodological: architectural comparisons depend on the **sizing contract** chosen, and a
fixed fuel fraction erases the mass bill from the range column entirely — which is why
three contracts are reported rather than one. meryemAircraft is the **case study** that
meets the escape condition.

### What is claimed, and against whom

The contribution is architectural. The four axes have four different opponents and are
not interchangeable.

| Axis | Opponent | Claim |
|---|---|---|
| Range and cruise efficiency | Multirotors | **Claimed.** |
| Runway independence, vertical take-off and landing | Fixed-wing | **Claimed**, by construction. |
| **Absence of a propulsor-reorientation mechanism** | Tilting architectures | **The actual contribution.** |
| Range against the other hybrids | Lift-plus-cruise, tilt | **Not claimed** — it reverses with the sizing contract. |

The third claim is narrow and stated narrowly. What is eliminated against tilting
architectures is the *class of mechanism that reorients a propulsor* — no pivot, no
nacelle actuator, no variable-pitch hub, no gyroscopic moment from a rotating mass. It is
**not** a claim that nothing on the aircraft moves: roll cannot be produced by coaxial
torque-balanced pairs at all, and comes from the strip, which the paper calls the only
moving aerodynamic surface on the aircraft. Nor is it a claim of mechanical simplicity —
part count, mass, failure modes and maintenance were never measured. The claim is a
**count of eliminated mechanism classes**, not a reliability result.

| | |
|---|---|
| DOI (always the latest version) | [10.5281/zenodo.22144194](https://doi.org/10.5281/zenodo.22144194) — currently **v7** |
| v7 version DOI | [10.5281/zenodo.22745666](https://doi.org/10.5281/zenodo.22745666) |
| First release (v1, immutable) | [10.5281/zenodo.22144195](https://doi.org/10.5281/zenodo.22144195) |
| PDF | [`paper/pdf/meryemAircraft-paper.pdf`](paper/pdf/meryemAircraft-paper.pdf) — 79 pages, 12 figures, 22 tables |
| Single-file source | [`paper/paper-v7.md`](paper/paper-v7.md) |
| Supplementary | [`paper/paper-v7-supp.md`](paper/paper-v7-supp.md) |
| Section by section | [`paper/sections/`](paper/sections/) |
| Bibliography | [`paper/bibliography-en.md`](paper/bibliography-en.md) |

### Submission status — not peer reviewed

Submitted to **Drones** (MDPI) on 14 September 2026. Returned from the editorial desk the
next day as out of scope and transferred to **Aerospace** (MDPI), which rejected it the
same day. **Neither rejection reached a referee**, and neither carries any technical
comment, so neither says anything about the content — for it or against it. The record,
including the two errors in the submission that were ours, is in
[`paper/drones-submission.md`](paper/drones-submission.md) §10; what is being corrected for
the next version is in [`paper/revision-list.md`](paper/revision-list.md).

---

## What is shown and what is not

This is the most important section of the repository. The paper is a **configuration
study**. There is **no wind-tunnel and no flight data**. The distinction below is held
everywhere in the paper and is held here.

| | status |
|---|---|
| The three-bill framework and the escape condition | **established**; its falsifiable prediction is tested against an independent published sizing set |
| Three sizing contracts | **computed**; shows why rankings drawn from a single contract mislead |
| Static pitch stability | **shown** — vortex-lattice, neutral point at 34.4 % MAC, margin +12.5 % |
| Cruise trim | **not shown** — the camber moment required is *quantified* at 0.056; the camber/reflex distribution is undefined |
| Roll authority | **not shown** — inertia (25.0 kg·m²) and damping (\|C_l_p\| = 0.358) computed for this planform; 27.1 N·m needed for 20°/s, of which the strip's own force gives about a third, the rest being a *requirement* of ΔC_L ≈ 0.12 borrowed from published fence and Gurney data |
| Yaw authority | **comfortable** — 2.43 times the pitch case, the arm being the semi-span (55.9 N·m against 23.0) |
| Directional stability | **not shown** — the planform gives C_n_β = 0; it must come from a tip-frame fairing, chord required 39 mm at a chord Reynolds number near 80 000 where thin symmetric sections are measured to be nonlinear |
| Transition controllability | **open** — the tip propellers rotate the inertia; that they rotate the aerodynamic moment is not shown. The largest open item in the study |
| Free-wheeling rotor drag | **computed, not measured** — C_D0 = 0.0154 at 50 kg, 62 % of the assumed zero-lift drag, against 0.0008 for the same propeller stopped edge-on |
| Mass budget, 50 kg | **closes conditionally** — 2.2 kg of margin if shell areal density stays ≤ 1.78 kg/m²; 1.5 kg/m² is a target, not a measurement |
| Mass budget, 1000 kg | **does not close** — the heavy point is a scale extension, not a second design point |
| Power budget | **does not close on measured cells** — it needs 3.8 times the highest specific power yet measured on a flown pack, and re-closes 38 % heavier at that measured rate |
| Loading shape | **bounded, not replaced** — the RANS study converges to *K_L* = 0.796 across a three-level grid refinement |

In short: **attitude control is sized in every axis and closed in none.** The paper says
so in those words.

---

## What is here

```
paper/          The paper: sections, single-file source, PDF, bibliography, roadmap
  build/          Compiler and verification scripts
  sections/       Section-by-section source
  supplement/     Supplementary material
aero/           Independent calculations — each states its own reasoning and its limit
figures/        The twelve figures
  source/         Parametric geometry model
  build/          Scripts that produce the figures and the transition simulation
  output/         Publication-ready png / svg
cfd/            OpenFOAM setups, the validation record, the current external-review round and the reader onboarding text
  arsiv-dis-gorus/  Every earlier external-review round
patent/         Texts and drawings of the Turkish patent application (in Turkish)
design/         Design record — every decision with the reasoning held at the time
references/     Record of the literature read
presentation/   Presentation material
video/          Visualisation
```

## Reproducibility

Every number and every figure in the paper can be regenerated from the scripts here.

| Script | What it does |
|---|---|
| `paper/build/mkpaper.py` | Compiles sections, figures and bibliography into one PDF |
| `paper/build/verify.py` | **Recomputes every headline number in the paper from the paper's own equations and compares it with the text** |
| `paper/build/links.py` | Connective-tissue guard: checks that every cross-reference resolves, and to the right place |
| `aero/planform.py` | Rebuilds the planform from the sweep laws; checks it against the design record |
| `aero/baseline.py` | Closed-loop sizing of three architectures under three contracts |
| `aero/mass.py` | Component-level mass budget, shell-density break-even, buffer check |
| `aero/vlm.py` · `aero/cd0.py` | Vortex-lattice solution and the `C_D0` build-up |
| `aero/stability.py` | Neutral point, static margin, trim requirement, **convention audit** |
| `aero/rotation.py` · `aero/envelope.py` | Transition rotation dynamics and the design envelope |
| `aero/roll.py` · `aero/yaw.py` | Roll and yaw inertia, damping, authority requirement |
| `aero/tip_propeller.py` | Free-wheeling drag of the tip propellers at zero shaft torque |
| `figures/build/transition2.py` | Transition simulation — two-degree-of-freedom point mass |
| `figures/build/mkfig*.py` · `mkconcept.py` | Generators for the twelve figures |
| `figures/build/figlib.py` | Opens the 3-D model in headless Chromium, drives the camera, captures |

`verify.py` currently runs **43 checks** plus **68 cells** of the transition tables, with
no deviation, and screens twelve files against a list of forbidden stale values. It has
caught, among other things, two tables left stale during a build and one place where a
moment had been confused with a thrust.

**Dependencies:** `python3`, `matplotlib`, `pillow`, `markdown`, `playwright` (headless
Chromium, for the three-dimensional figures and the PDF); `aero/` additionally needs
`aerosandbox` and `neuralfoil`.

Scripts run from where they sit and need no path outside the repository. The
three-dimensional figures are produced from `figures/source/body-study.html`: `figlib.py`
injects a render hook into a **copy** of the model and never modifies the source file. If
Chromium lives elsewhere, point to it with `CHROME_PATH`.

## External review record

Before submission the paper was read round by round by **four mutually independent
language models**, and the text of every round is kept under
[`cfd/arsiv-dis-gorus/`](cfd/arsiv-dis-gorus/) (the current round is in [`cfd/`](cfd/)). This is not a validation; it is a **bug hunt**, and the
hunt is on the record — what was found was not only corrected but written down, with what
was wrong and why, in `aero/README.md`. Claims that collapsed during the process include:
that the pitching moment was 2TL rather than 4TL; that placing the centre of gravity by
hand gave an absurd static margin; that the static margin and the trim requirement had
been written with **two different reference chords**; and that §4.4's 46 N·m rolling
moment **could not** come from the strip's own force.

Errors made while *summarising* the paper are recorded with equal weight, because that
turned out to be the highest-error activity in the project: a claim that no general
architectural superiority was asserted, which denied the paper's own earned claims; a
claim that nothing on the aircraft moves, contradicted by the strip; and a claim that the
strip produces no pitching moment, contradicted by the same section.

## Use of sources

Every numerical and historical claim rests on a source **read first-hand**; no number is
attached to a source that was not read. The distinction is written out in §8 of the paper.
`paper/references.md` records how far each source was verified, and how **three wrong
numbers** taken from search-engine summaries were caught by first-hand reading.

## Version history

Published versions are **immutable**; each remains reachable at its own DOI. File *names*
in this repository were translated to English on 16 September 2026, but the contents of
published versions were not touched — see [`paper/VERSIONS.md`](paper/VERSIONS.md) for the
path translation table.

| Version | Date | Substance |
|---|---|---|
| **v7** | 2026-09-13 | Submitted version. Claim structure rebuilt onto four axes with four different opponents; the mechanism claim narrowed to the propulsor-reorientation class; figure order and numbering corrected to first mention; heavy-rotor charge reported as an interval. |
| v6 | 2026-09-11 | Figure and table production defects closed; all 22 tables numbered, captioned and cited. |
| v5 | 2026-09-10 | Supplementary material separated; sizing contracts consolidated. |
| v4 | 2026-09-08 | Framework-centred restructuring; capability sentences rewritten as requirements. Three control axes audited. |
| v3 | 2026-09-05 | Three-dimensional solution for the centre body. §8.1 became "No experimental validation". |
| v2 | 2026-08-29 | Range method corrected (cruise-point polar instead of maximum L/D): 1 695 → **1 598 km**. |
| v1 | 2026-08 | First release. |

## Patent

A patent application for the configuration was filed in Türkiye (2026-08). The texts and
drawings under `patent/` are the drafts the application was based on, and are **in
Turkish**, as filed. They were not prepared by a patent attorney.

## Licence

Text, figures and scripts: **AGPL-3.0** — see [LICENSE](LICENSE).
The Zenodo version of the paper is published under **CC BY 4.0**.

---

*Artificial-intelligence tools were used in preparing this work for literature search,
numerical checking and language correction. All design decisions, engineering judgements
and claims belong to the authors.*
