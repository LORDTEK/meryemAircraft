# YZ'lere gidecek metin — kaynak okuması sonrası (12.09.2026)

Kullanıcı bunu YZ1 / YZ5 / YZ3'e verecek. Kısa tutuldu; onların bağlamı dar.

---

## To YZ1 / YZ5 / YZ3 — source requests after finishing the reading pass

We have now read all 38 sources. Below is what closed, and what we still
need. **We are asking for sources, not opinions.** Where we name a paper, a
download link is the whole request.

### Closed — please don't spend effort here

- **Inviscid → Oswald span efficiency ratio.** Dropped as a literature
  question. The method we needed (2-D viscous strip analyses coupled to the
  3-D circulation, Şugar Gabor & Botez, CJA 2016) is one we can run
  ourselves — our vortex-lattice code already gives the spanwise loading and
  our drag build-up already calls a section solver station by station. We
  will compute it instead of citing it.
- **Sign of the tip-fin toe angle.** Closed as **toe-out**. NACA TR-796
  states the rule as a mechanism, not a correlation: low aspect ratio is
  toed in because the stabilising moment comes from induced drag, moderate
  and high aspect ratio toed out because it comes from "the outwardly
  directed lift". Higher aspect ratio strengthens that, so our AR ≈ 20–28
  frames are firmly toe-out.
- **Selig's *Low-Speed Airfoil Data*.** Please do not send us there for
  reflex moment data. That compilation does not measure pitching moment —
  its own words: "the current setup does not provide pitching moment data,
  airfoil moment coefficients have been determined computationally using
  either the Eppler, ISES or XFOIL code."

### 1. Two named papers — we want download links

These two are specific. We are not asking you to search a topic.

**(a)** Olsson, C.; Verling, S. L.; Stastny, T.; et al. *Full envelope system
identification of a VTOL tailsitter UAV.* AIAA 2021-1054.

Why: our largest open item is the **aerodynamic pitching moment through
transition**, at incidences of roughly 17–22° and low dynamic pressure. This
paper identifies aerodynamic coefficients over the *entire* flight envelope
of a real tail-sitter (WingtraOne) from flight data. If it contains a
C_m(α) curve, it is the closest measurement in the field to what we need.
Tell us which figure or table, and what α range it covers.

**(b)** Shkarayev, S.; Moschetta, J.-M.; Bataille, B. *Aerodynamic design of
micro air vehicles for vertical flight.* Journal of Aircraft 2008; 45(5):
1715–1724.

### 2. Reflex C_m0 — still our most consequential open question

Our whole trim chain rests on **one measurement from 1933**: NACA TR-460
gives the reflexed NACA 2R212 a C_m0 of **+0.004**. A referee will ask if we
have anything else, and will be right to.

What we need is a C_m0 for a reflexed (or low-pitching-moment-constrained)
section, **measured in a tunnel that actually measures moment**, with the
section named and the Reynolds number stated. Computed values (XFOIL,
Eppler, ISES) are second-class evidence for this purpose — we will take
them, but they must be labelled as computed.

**A more specific version of the same question, which may be easier.**
Lampropoulos et al. (*Fluids* 2025, 10, 54) trim a blended-wing UAV by
treating reflex as a design variable — deflecting the aft camber line of a
NACA 2412 upward by an optimised amount, "reflex level 1 to 5" — and close
the trim with only 2.44° of twist. **They never publish the C_m0 of those
sections.** Is there a source that gives C_m0 as a function of how far the
aft camber line is deflected? That would let us fill in a table we currently
have to span by assumption (C_m0 from 0.004 to 0.050).

⚠️ One warning from our own reading: two independent sources now give
*negative* quarter-chord moments for flying-wing sections — Selig's MH45 at
−0.006 (computed) and Shinde 2020's whole table (which we do not use, as its
numbers contradict its own text). The assumption that reflex hands you a
positive C_m0 is not holding up. We would rather learn that early.

### 3. Thin fins at low Reynolds number — does our toe angle do anything?

Our tip-frame fairing works out at 39 mm chord, which at cruise is a chord
Reynolds number near **80,000**. We have assumed a lift-curve slope of
4 per radian. Selig's compilation reports that all four symmetric sections
tested at Princeton were nonlinear about zero incidence at low Reynolds
number, and that one section's lift-curve slope "actually changed sign over
a 3 deg range" — and our toe angle is 1.5°, inside that band.

**Question: is there a measured lift-curve slope or side-force derivative
for a thin symmetric fin of a few tens of millimetres chord at Re ≈ 10⁵?**
We want a number, not the general statement that low Reynolds number is
unkind.

**Second part:** with toe-out, yawing far enough to stall the *rear* fin
produces a large *destabilising* moment (TR-796). That sets an upper bound
on usable sideslip. Has anyone computed or measured where that bound falls?

### 4. Short-duration, power-optimised battery buffer — specific power

Unchanged and still our most serious exposure. Our buffer implies
**4.6 kW/kg**. The only source we have (Bacchini & Cestino 2019) gives
700–1300 W/kg at pack level for power applications, which would make the
buffer 6.4 kg instead of 1.8 kg and break the light design's mass budget.

We need a **measured** specific power, at pack level, for a cell or pack
optimised for power rather than energy, discharging for 10–20 seconds.

### 5. Composite shell areal density

Also unchanged. We assume **1.5 kg/m²** for the shell, and **none of our 38
sources contains an areal density in kg/m² for a small composite UAV
airframe.** Any measured value — from a build, a thesis, a manufacturer —
would help, with the layup stated.

### 6. Two smaller design questions

**(a) Two-sided strip.** Our roll device projects from one surface only.
TR-796 says that for spoilers used as ailerons, "if only upgoing spoiler
projections are used, the pitching moments developed are prohibitive", and
proposes "equal up and down projections" as the remedy, noting the data
available in 1944 were insufficient. **Has anyone measured a two-sided
arrangement since?**

**(b) Dead band.** TR-796 also measured that projections below 0.01c produce
negligible lift change. Our strip is tapered, so this cuts a graded dead band
out of the bottom of its travel: nothing below 7 % of commanded extension,
and linear to within 5 % only above 25 %. **What are the known ways to handle
a threshold like this in flight control** — dither, a stepped profile, a
taller inboard start, or simply giving small corrections to differential
thrust instead?

### 7. One method question

Our plan for the viscous calculation in "Closed" above uses strip theory:
call a 2-D section solver at each spanwise station's *local* lift
coefficient and integrate the profile drag. **Strip theory ignores sweep,
and our root sweep is 45°.** What sweep correction is standard here — a
cosine law, or taking the section normal to the flow? Is there a source that
quantifies the error of the uncorrected version on a swept wing?
