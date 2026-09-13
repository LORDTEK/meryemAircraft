# Round 19 — version 6 is built. What changed, and is it ready?

**Read this document alone. You do not need the manuscript.** Everything needed
to answer is below. Two of you could not fetch files reliably and one described
a version that did not exist; that failure mode is removed by giving you the
substance directly, and it worked last round — all four of you answered from the
document and all four answers were usable.

---

## 1. The paper, in three hundred words

**Thesis.** Hybrid VTOL aircraft pay for runway independence in cruise
efficiency. The paper treats that cost as *architectural* and develops it as an
accounting framework. The penalty is charged in three coupled currencies:

- **Bill 1** — hover hardware carried through cruise as dead mass.
- **Bill 2** — the drag of that hardware when exposed to the cruise flow.
- **Bill 3** — continuous installed power sized by a condition holding for
  roughly two percent of the flight.

Every architectural remedy surveyed reduces one bill by raising another. Escape
requires four things at once: the *same hardware*, in the *same orientation*,
doing the *same job*, with the hover peak from a *buffer*.

**The framework's central prediction**, and now the paper's headline: *architectural
rankings belong to sizing contracts, not to architectures.* Three contracts are
reported — fixed fuel fraction, fixed fuel mass, fixed take-off mass with fixed
payload — and the ranking changes between them.

**The case.** An uncrewed tail-sitting blended-wing body. One coaxial nose pair
serves hover and cruise. Four small counter-rotating pairs at the tips produce
attitude moments. No elevons, no rudder, no tilt mechanism, no dedicated lift
system. Engine → generator → bus → buffer. Sized at 50 kg and 1000 kg from one
set of equations, and carried far enough to show what instantiating the escape
condition costs.

**Not claimed.** That the aircraft is flyable, or that any architecture is
generally superior. No wind-tunnel data, no flight test. Transition
controllability rests on a pitching moment three methods of three fidelities fail
to predict above ten degrees of incidence.

**Target.** *Drones* (MDPI). IMRaD, five sections, abstract ~200 words.

---

## 2. Current numbers

| Quantity | Value |
|---|---|
| Light design, take-off mass | 50.1 kg at the assumption, 51.1–53.9 across the bracket |
| Light design, cruise L/D | 11.88 → **10.82 – 8.80** |
| Light design, **range** | 1 583 km → **1 173 – 1 442 km** |
| Heavy design, cruise L/D | 13.60 → **12.37** (rotors charged) |
| Heavy design, **range** | 1 813 → **1 649 km** |
| Free-wheeling rotor drag, light | **0.0154** |
| Free-wheeling rotor drag, heavy | **0.0033** |
| Zero-lift drag bracket | **0.0285 – 0.0381** |
| Assumed C_D0 | 0.0248 — **below both ends** |
| Mass advantage over lift-plus-cruise | 37 % |
| Range vs B, fixed fuel fraction | **B leads**, +21 to +45 % across the bracket |
| Range vs B, fixed MTOW | A leads, −29 to −45 % across the bracket |
| Range vs B, fixed fuel mass | **sign changes inside the bracket** |
| RANS/VLM ratio *K_L* | 0.796 (converged) |
| Loading redistribution, converged | **2.75°** against a 2.6° threshold |
| Consequence of exceeding it | **0.8 %** on L/D and range |

---

## 3. Your positions last round, and what was done with them

**All four of you voted B — lead with the framework, report the aircraft as the
case.** Qwen reversed from the previous round's "do not soften the claim, submit
as is." That was a 4–0 result and it has been implemented.

**One thing about implementing it is worth reporting, because it is mildly
embarrassing and it cuts against the size of your recommendation.** The body was
*already* framework-led. Section 1's contributions paragraph has said since
version 4: *"The primary contribution is a framework; the aircraft is the case
that instantiates it."* The Introduction opens on the configuration families and
the tax; the Conclusions open on the three currencies. **Only the abstract and the
highlights led with the aircraft.** So the reframing you all argued for was two
paragraphs of front matter, not a restructuring. Both are now rewritten to open on
the three currencies and to state the contract-dependence prediction. An explicit
sentence was added: *no claim of general architectural superiority is made anywhere
in this paper.*

**On the individual points:**

- **ChatGPT's "framework-led, aircraft-rich"** is the formulation that was
  followed. The case study lost nothing; it gained two calculations.
- **DeepSeek's arithmetic on the bracket** — "a 53 % increase in C_D0 is roughly a
  25–30 % increase in total drag, and range falls by roughly a quarter" — was
  checked. The drag increase is 35 %, not 25–30 %. The conclusion was right:
  range falls 26 %.
- **Qwen's "the η = 0.936 station is almost certainly a discretisation artefact"**
  was not adopted. It was an assertion without evidence, and the grid study below
  shows it was also wrong in the direction that mattered.
- **Grok's "do the propagation, it is days not months"** was correct. It took a
  day.

---

## 4. What was run since, what was expected, what came out

### 4.1 The drag bracket was itself wrong, and the error was mine

While building the sweep I found that the lower end of the published bracket
still used **0.0085** for the rotors — the drag of the blade with a hover figure
of merit of 0.27, the one the paper had already established the aircraft cannot
use. **This is the same error DeepSeek caught last round, committed again in the
other column of the same table.**

The only rotor the aircraft can carry costs 0.0154 at either end.

| | published | corrected |
|---|---|---|
| bracket | 0.0216 – 0.0380 | **0.0285 – 0.0381** |
| assumed 0.0248 | inside it | **below both ends** |

So the assumption is not merely "no longer conservative." It is optimistic at the
*favourable* end of the paper's own calculation.

A third value was also in circulation: §3.6's re-sizing had effectively used
0.0401 (assumed + rotor), which sits *above* the bracket. Three different drag
values in one paper. All three are now derived from one book-keeping, and the
construction reproduces the published clean-body L/D to within 0.33 % before
anything is changed — that check is the reason to believe the sweep and the
original sizing are the same calculation.

### 4.2 The sweep

**Expected:** the reference designs would move a little and the contract-dependence
result would either survive or not.

**Came out:** the designs move substantially and the contract result survives and
strengthens.

| Light design | assumption | favourable end | adverse end |
|---|---:|---:|---:|
| Cruise L/D | 11.88 | 10.82 | 8.80 |
| Cruise power | 1.72 kW | 1.93 kW | 2.50 kW |
| Take-off mass | 50.1 kg | 51.1 kg | 53.9 kg |
| Endurance | 14.7 h | 13.4 h | 10.9 h |
| **Range** | 1 583 km | **1 442 km** | **1 173 km** |

Nothing else in the design table moves: geometry, loadings, hover power and
transition time are set by mass and disc area, which drag does not touch.

**Against lift-plus-cruise, across the whole bracket:** A loses under equal fuel
fractions everywhere, leads under fixed take-off mass everywhere, and **the sign
changes inside the bracket** under fixed fuel mass. The contract-dependence result
is therefore not an artefact of one drag assumption.

**One direction was not intuitive.** A *cleaner* airframe makes this configuration's
position *worse* relative to lift-plus-cruise, because the frames and rotors are a
roughly fixed absolute charge and a cleaner airframe makes them a larger fraction.

### 4.3 The heavy design carried the same defect

**Expected:** the heavy line would need the same rotor charge, scaled.

**Came out:** it does, but the charge is five times *lighter*, and a second and
unrelated problem surfaced.

Rather than scale the light result, the same blade-element calculation was run at
the heavy design's own conditions — 0.67 m discs, 40 m s⁻¹, the tip-pair power
this configuration allocates (12 % of hover power ÷ 4), and the hover thrust that
follows. The published row reproduces 13.60 and 1 813 km, which is the chain check.

| | published | rotors charged |
|---|---:|---:|
| ΔC_D0, eight discs | assumed negligible | **0.0033** |
| Cruise L/D | 13.60 | **12.37** |
| **Range** | 1 813 km | **1 649 km** |

**The second result is adverse and is not about drag.** *No blade in the heavy
family reaches the hover figure of merit of 0.599 that the heavy design's own power
budget assumes.* The best is 0.547, and the designs that come closest do so at tip
Mach numbers above unity, where the section data do not apply. So the twelve
percent of hover power allocated to the heavy design's tip pairs is insufficient by
roughly a tenth. This is reported and **left uncorrected**, because correcting it
means re-sizing the tip pairs — a design change, not a coefficient.

### 4.4 A framework result fell out of the case study

Bill 2 falls from 0.0154 at 50 kg to 0.0033 at 1000 kg: the tip discs are
referenced to a wing area that grows faster than they do. The mass bill scales the
other way. The power bill is held flat by construction.

**The three currencies do not move together, which is the framework's separability
claim operating on its own case.** A consequence worth stating: the *light* design
is the harder case for this configuration and the heavy one the easier — the
opposite of the usual expectation for a tail-sitter.

### 4.5 The grid study — the coarse mesh had been wrong

**Expected:** refinement would settle whether the η ≈ 0.94 station was physics or
discretisation, and most likely show it was discretisation (which is what Qwen
asserted and what the paper would have preferred).

**Came out:** the opposite, on both counts.

| Mesh | Cells | *K_L* | inner residual | tip residual |
|---|---:|---:|---:|---:|
| Coarse | 192 000 | 0.787 | 0.029 | 0.133 |
| Medium | 444 000 | 0.793 | 0.046 | 0.130 |
| **Fine** | **682 000** | **0.796** | **0.048** | **0.122** |

- The **overall ratio converges** (0.8 %, then 0.4 %).
- The **inner residual does not shrink — it grows and settles.** The coarse mesh
  was smoothing the loading and flattering the agreement.
- The **tip residual barely moves across a threefold change in cell count.** That
  is the signature of a real disagreement, not a numerical one. The near-tip
  anomaly is physics, and Qwen's confident attribution to mesh resolution was
  wrong.

### 4.6 A measurement fight, and why it had to be settled first

On the converged solution the equivalent redistribution came out **on both sides
of the threshold depending on how it was measured**: 2.80° using extremes on the
solution's own bins, 1.87° on a coarser common sampling, against a 2.6° threshold.

Letting the measurement decide the result is not acceptable. The cause is that an
extreme-value measure is sensitive to sample count, and the two sides carry
different numbers of spanwise stations — the RANS side 20, 29 or 37 bins depending
on mesh, the vortex-lattice side about 52 strips. More samples, more chance of an
extreme.

Both sides were recomputed as **standard deviations**, which are sample-count
insensitive, and the sensitivity coefficient was re-derived in the same units.

### 4.7 The answer: the threshold is exceeded, and the exceedance is small

**2.75° against a 2.6° threshold — exceeded by six percent.** The coarse mesh's
1.66° was under-resolution.

The threshold was defined externally as *the redistribution that would move the
trim twist by one degree*. Carrying 2.75° through the measured chain:

| | |
|---|---|
| trim twist moves | **1.04°** |
| span efficiency moves | 0.817 → **0.799**, 2.1 % |
| cruise L/D and every range | **0.8 %** |

**0.8 % is an order of magnitude inside the drag bracket the same section already
applies**, which moves range by 9 to 26 %. The vortex-lattice trim chain is not
overturned by the comparison; it is displaced by less than the uncertainty already
carried around it. The exceedance is reported rather than rounded away.

---

## 5. Errors made this round, all caught before anything was reported

Recorded because the same discipline will be needed again, and because a reader
should know how many of these there are.

1. **Bin edges hard-coded to the coarse mesh's 20 stations.** On the 28-station
   medium mesh the wall faces fell into bins alternately, producing a regular
   alternating pattern (0.56 / 1.15 / 0.56 / 1.11 …) that looked like physics and
   was a partitioning defect.
2. **The measure was sample-count dependent**, §4.6 above. Caught because the two
   measures disagreed across the threshold.
3. **The bracket's lower end used the unusable propeller**, §4.1 above — the same
   error class caught by DeepSeek one round earlier.

Each was caught by the same rule: *every spanwise sum must reproduce the solver's
own integrated coefficient before any ratio is taken from it.*

---

## 6. Where version 6 stands

Built and deposited: `makale-v6.md`, `makale-v6-ek.md`, two PDFs. Abstract 214
words. Forty internal consistency checks, zero deviations. Framework-led. Both
reference designs on the bracket. The grid study folded in.

**Open items, as the paper states them:**

1. The **trimmed geometry has not been solved.** The mesh generator accepts
   stations as span, leading edge, chord and thickness — four fields, no twist.
   All RANS runs are on the untwisted planform.
2. The **near-tip loading disagreement is real** and survives refinement. Nothing
   in the paper is taken from that region alone.
3. The **heavy design's tip pairs do not meet their own assumed efficiency** and
   have not been re-sized.
4. The **transition pitching moment** is blocked on measurement, not effort.
5. The overall lift ratio **runs opposite** to the published comparison the paper
   cites. Reported, not reconciled.

---

## 7. What we want from you

The intention is to deposit version 6 and then submit to *Drones*. Before that:

**Q1 — Is anything on the open list above a submission blocker rather than a
stated limitation?** Be specific about which one and why. "It would be better with
X" is not the question; the question is whether a referee can reject on it.

**Q2 — The threshold is exceeded by 6 % and the consequence is 0.8 %.** Is
reporting it that way defensible, or does exceeding a threshold the paper itself
set require something more — re-deriving the trim, or re-stating the threshold?
A referee could read "we exceeded our own criterion and then argued it did not
matter" unkindly.

**Q3 — The heavy design's tip pairs fail their own efficiency assumption by about
a tenth, and this is reported without correction.** Is that acceptable as a stated
limitation, or does it undermine the heavy design enough that it should be
re-sized or withdrawn? The heavy design carries the scale-behaviour argument, so
withdrawing it costs a section.

**Q4 — Bill 2 shrinking with scale while Bill 1 grows** is presented as the
framework's separability claim verified on its own case. Is that a real result or
a restatement of the definitions? We think it is real, because nothing in the
framework forced the bills to move in opposite directions and they were computed
independently — but that is exactly the kind of claim an author overrates.

**Q5 — Anything else you would fix before submission.** This is the last round
before the paper goes out, so say it now rather than agreeing politely.

Answer from this document. If you want a number that is not here, say which one
rather than inferring it.
