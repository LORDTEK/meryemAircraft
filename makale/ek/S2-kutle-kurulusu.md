# Supplementary S2 — A component build-up of the mass budget

*Supplementary material to "The Architectural Cost of Hybrid VTOL:
meryemAircraft, a Propeller-Driven Tail-Sitting Blended-Wing-Body Without a
Dedicated Lift System".*

This material is Section 3.11 of the paper, reproduced here in full.
It is reproduced here in full so that every number quoted in the main text can
be traced to the calculation that produced it. The computational setup, the
scripts, and the record of what failed along the way are in the repository the
paper cites.

---

## S2.1 A component build-up of the mass budget

The fractions used in Sections 3.7 and 3.8 are asserted, and Section 4.4 says so. This
section replaces the assertion for the light design with a build-up from components. The
rule followed throughout is that no item may be derived from the fraction it is meant to
test: every line comes either from the geometry and a stress calculation, or from a
specific quantity — an areal density, a specific power — stated openly and then varied.

**Structure.** The wetted area follows from the planform of Section 2.8 and the NACA 00xx
thickness distribution: 4.14 m² against 1.98 m² of planform. A carbon–epoxy sandwich shell
at 1.5 kg m⁻² gives 6.20 kg, with ribs, bulkheads and bonded joints taken at 45 percent of
the shell. The tip frames are sized by a vertical landing case, since this aircraft lands on them: a
3 g arrival, half the weight through one frame, the post treated as a cantilever of the
stated length, giving 0.95 kg for both frames including fittings. That case is not shown to
be the worst one — an off-axis touchdown, a ground gust against the planform standing on
its tail, or the thrust moment of the nose pair may govern the frame root or the joint into
the wing instead — and no combined case was run.
Fasteners, adhesive, filler and paint are charged at 10 percent of primary structure and
access panels at 6 percent. The total is 11.88 kg, 23.8 percent of take-off mass.

Span bending is not what sizes the spar, and this is worth recording, because a thick
blended centre body invites the assumption that it must be. At an ultimate load factor of
5.25 the root bending moment is 934 N·m; carried at 400 MPa over a structural depth of 0.9
times the root thickness, the caps require 10.7 mm² of carbon and weigh 41 grams. The claim
that figure supports is narrow and is stated narrowly: **global span bending is not the
sizing driver in this static model.** It says nothing about the failure modes the model
does not contain — sandwich and face-sheet buckling, core shear, torsion, load introduction
at the frame roots and the nose mount, minimum manufacturing gauge, damage tolerance,
aeroelastic margin — and none of those is a reason to reduce the shell and internal-structure
allowances above. Those allowances are where such mass would have to live, and the 41 grams
does not license trimming them.

**Propulsion.** The nose motor is sized by hover peak power and the engine by cruise,
which is the configuration's central claim and is visible in the budget as such: 2.73 kg
of electric machine against 2.60 kg of engine and generator, at 4 kW kg⁻¹ and 1 kW kg⁻¹
respectively. Adding the tip motors at twelve percent of nose power, the propellers, the
coaxial hubs, the power electronics at 20 kW kg⁻¹, the engine mounting with its cooling
and exhaust, and the power cabling gives 7.60 kg, 15.2 percent.

**Systems, energy and contingency.** Avionics, fuel system, strip actuation, signal harness
and payload interface total 2.84 kg. There are no elevon or rudder actuators to add, since
the aircraft has neither; the strip is its only moving aerodynamic device and its actuation
is carried here. Fuel and battery are as sized, 9.80 kg. A contingency of 12 percent of dry
mass — ordinary preliminary-design practice — adds 2.68 kg.

**The battery buffer is specified by power, not by energy, and this has not been stated
before.** It must supply the difference between what the propellers demand and what the engine
delivers — but that difference has to be taken at one station, and an earlier version of this
section did not take it at one. It subtracted the engine's 2.6 kW of *shaft* power from the
rotor's 10.9 kW of *shaft* power and divided the remainder by the buffer mass, giving
4.61 kW kg⁻¹. The buffer sits on the electrical bus, which is neither of those stations. Running
the chain of Section 2.12 link by link instead:

| Station | Light design, hover |
|---|---:|
| Nose propeller shaft | 10.90 kW |
| ÷ electric machine, 0.92 | 11.85 kW |
| ÷ power electronics, 0.95 | **12.47 kW demanded at the bus** |
| Engine shaft 2.60 kW × generator 0.90 | **2.34 kW supplied at the bus** |
| **Buffer** | **10.13 kW** |

which is **5.63 kW kg⁻¹** from 1.8 kg, or about 31 C at 180 Wh kg⁻¹ — twenty-two percent above
the figure previously carried, and in the unfavourable direction. Taking the tip pairs as well,
which Section 3.15 shows the aircraft needs in order to leave the ground at all, the bus demand
rises to 14.00 kW and the buffer to 11.66 kW, or **6.48 kW kg⁻¹** at 36 C. The heavy design sits
on the same line: 198.5 kW of buffer on 40 kg, **4.96 kW kg⁻¹**, rising to 5.54 kW kg⁻¹ if the
tip pairs are counted. Energy is not the binding constraint until roughly 140 seconds of hover,
well beyond the profile of Section 3; below that the buffer is power-limited. That places the
buffer well past the high-power lithium-ion or lithium-polymer class — cells rated for twenty to
thirty times their capacity in continuous discharge — and the paragraphs below measure how far
past.

**How demanding, measured against the only figures this study has read, is the most exposed
number in the whole mass budget.** Bacchini and Cestino, sizing electric VTOL aircraft, take
735 W kg⁻¹ at pack level from an automotive traction pack and report that "Li-ion batteries for
power applications have… specific power from 700 to 1300 W kg⁻¹" [21]. The buffer here asks for
**5.63 kW kg⁻¹** to hover and 6.48 to take off, four and a third to nearly nine times the top of
that range. Sized at figures from that range instead, on the hover requirement alone:

| Buffer specific power | Buffer mass | Fraction of MTOW |
|---|---:|---:|
| 0.735 kW kg⁻¹ (the pack they assume) | 13.8 kg | 27.6 % |
| 1.30 kW kg⁻¹ (top of their quoted range) | 7.8 kg | 15.6 % |
| **5.63 kW kg⁻¹ (this study, implicitly)** | **1.8 kg** | **3.6 %** |

At the top of their range the buffer would be 6.0 kg heavier than budgeted, against the 2.2 kg
of unallocated mass this section leaves. **The light design's mass budget would not close.**

The defence available at that point was that those figures are for an energy-optimised
automotive pack, while a buffer discharged for a fraction of a minute is a different product
optimised for the opposite thing. **That defence has since been tested against a measurement of
the right product, and it does not survive.** A 24S nickel–cobalt–manganese pack was designed,
built, bench-tested across discharge rates from 0.2 C to 10.68 C and then flown in an electric
VTOL aircraft through six take-off, hover and landing cycles [47]. Its measured pack-level
specific power is **724 W kg⁻¹** continuous for the unit pack and **892 W kg⁻¹** for the
four-parallel flight system — inside the range quoted above, not above it. Its maximum tested
rate, 10.68 C, corresponds to roughly **1.5 kW kg⁻¹**, and at that rate the pack reached
55.1 °C against a 60 °C limit: a thermal margin of 4.9 °C. That is the ceiling of a pack built
for exactly this duty, instrumented, and flown.

A third source points the same way from the other direction. A NASA-funded design study of
electrically propelled aircraft adopts a battery specific power of 4 kW kg⁻¹ and states plainly
that this is "about **twice that of existing batteries**" [48] — that is, it treats a figure
below the one assumed here as a future technology level rather than a present one.

| Source | Specific power | Kind |
|---|---:|---|
| Measured eVTOL pack, continuous [47] | 0.72–0.89 kW kg⁻¹ | flight-tested measurement |
| Same pack at its maximum tested rate [47] | ≈ 1.5 kW kg⁻¹ | measurement, 4.9 °C thermal margin |
| Li-ion for power applications [21] | 0.7–1.3 kW kg⁻¹ | literature range |
| Assumed future level in a design study [48] | 4 kW kg⁻¹ | stated as ≈ 2× what exists |
| **This study, implicitly — hover** | **5.63 kW kg⁻¹** | **assumption** |
| **This study, implicitly — take-off** | **6.48 kW kg⁻¹** | **assumption** |

Sized at the measured thermal ceiling of 1.5 kW kg⁻¹ the buffer becomes **6.8 kg** rather than
1.8 kg — 5.0 kg heavier, against 2.2 kg of unallocated mass — and 7.8 kg if it must also lift
the aircraft off the ground. Sized at the measured continuous figure it becomes 11.4 kg, or
23 percent of take-off mass, which is most of the payload. **The light design's mass budget does
not close at any measured specific power, and this is the single most exposed number in the
paper.** It is not resolved by arguing that the buffer is a different product: the source above
*is* that product, built and flown. The gap to be closed is a factor of **3.8 on the measured
thermal ceiling and 6.3 on the measured continuous rate**. What would resolve it is a pack
demonstrating that, at acceptable temperature, or a heavier buffer carried at the cost of
payload fraction. Section 4 states which.

Both figures in this paragraph are larger than the ones an earlier version reported, and the
reason is bookkeeping rather than new evidence: the buffer power was previously taken as a
difference between two shaft stations and is now taken at the bus, where the buffer is.

**The energy side is a different matter, and it is far more comfortable than the power side.**
The buffer does not discharge continuously for the whole vertical phase. It discharges through
the take-off, which ends when the rotation begins and the wing starts carrying the aircraft;
it then recharges from the engine over hours of cruise, and discharges again for the landing.
At the achievable thrust-to-weight ratio of 1.132 the vertical acceleration is 0.132 g, so the
5 m s⁻¹ climb from which Section 3.15 enters the rotation is reached in 3.9 s and 9.6 m — and in
7.7 s and 19.3 m if full rotation authority is held in reserve. A take-off segment of ten to
twenty seconds at full draw therefore remains generous, though less so than at the 1.2 an
earlier version assumed. Against that:

| Take-off segment at full draw | Energy used | of a 180 Wh kg⁻¹ buffer | of an 80 Wh kg⁻¹ buffer |
|---:|---:|---:|---:|
| 10 s | 32 Wh | 10 % | 23 % |
| 20 s | 65 Wh | 20 % | 45 % |
| 30 s | 97 Wh | 30 % | 68 % |

These are the take-off draw of 11.66 kW at the bus. An earlier version of this table read 23, 46
and 69 Wh, which is 8.3 kW — the rotor-shaft-minus-engine-shaft difference retired at the head of
this section. The correction survived into the power figures and not into the energy ones.

Even at the low energy density that a high-power chemistry would carry, a twenty-second take-off
uses under half the buffer and a thirty-second one just over two thirds. **The binding constraint
is power, not energy, and it stays that way under any plausible take-off duration** — though the
margin on the energy side is thinner than the previous arithmetic suggested, and a buffer at
80 Wh kg⁻¹ would not tolerate a take-off much longer than the ones tabulated.

That distinction matters, because it says what would *not* rescue the specific-power figure.
A shortfall in power is not a transient to be ridden out. Hover power goes as thrust to the
three-halves, so thrust goes as power to the two-thirds, and a buffer delivering less simply
buys less thrust:

Every row below is taken through the same chain: the buffer and the generator both deliver to the
bus, and the bus is converted to propeller-shaft power by the power electronics and the electric
machine before momentum theory is applied.

| Buffer specific power | At the bus | At the nose propeller shaft | Resulting T/W | Leaves the ground |
|---|---:|---:|---:|---|
| 0.735 kW kg⁻¹ | 3.66 kW | 3.20 kW | 0.44 | no |
| 1.30 kW kg⁻¹ | 4.68 kW | 4.09 kW | 0.52 | no |
| 2.50 kW kg⁻¹ | 6.84 kW | 5.98 kW | 0.67 | no |
| **5.63 kW kg⁻¹** | **12.47 kW** | **10.90 kW** | **1.00** | only just |

Every row is the same calculation: all of the shaft power goes to the 1.20 m nose disc and
T/W follows from momentum theory as (P/10.9 kW)^(2/3). **The take-off case cannot be added as a
fifth row of this table, and an earlier version did add it.** Taking the aircraft off the ground
needs 6.48 kW kg⁻¹, which is 14.00 kW at the bus and 12.24 kW of shaft power — but that 12.24 kW
is 10.90 kW at the nose *plus* 1.34 kW at the tips, and the tip power drives four pairs of 0.20 m
discs rather than the nose disc. Putting the whole 12.24 kW through the nose-disc formula gives
T/W = 1.08, and that number is an artefact: it spends the tip power twice, once as nose thrust
and once as the 64.8 N the tip pairs actually produce. The take-off ratio of **1.132** is a force
sum across two different propulsors, 490.5 N from the nose and 64.8 N from the tips, and it is
computed that way in `aero/itki.py`. The two calculations do not belong in one column.

Two earlier versions of this table were wrong in two different ways, and both are worth naming
because the second was introduced by the correction of the first. The original read 0.61, 0.71,
0.90 and 1.20 in the T/W column — a fifth too high at every row, because the column was scaled
from an assumed T/W of 1.2 at its foot while 10.9 kW is, by the sizing statement of Section 2.12,
the power for thrust equal to weight exactly. Correcting that left a second fault in place: the
first three rows added the buffer's power to the engine's *shaft* rating and then read the sum as
shaft power, which is the same mixing of stations this section has just spent two paragraphs
removing from the headline figure. The rows above are on one formula throughout. The consequence
of the pair of corrections is that the bottom of the table is worse than it looked: the specific
power demanded rises, and what it buys is a hover rather than a take-off. Leaving the ground
needs the tip pairs and 6.48 kW kg⁻¹.

**At the specific powers this study has a citation for, the aircraft does not lift off**, so
there is no brief overshoot to tolerate and no manoeuvre that shortens the exposure. The only
remedy is a heavier buffer, which is why this appears as a mass-budget exposure rather than a
flight-dynamics one. The buffer masses used here are a cell-selection requirement rather than a
free parameter, and it is the specific power, not the energy, that has to be found.

| Group | Build-up | Assumed in 6.2 |
|---|---:|---:|
| Structure | 23.8 % | 30 % |
| Propulsion chain | 15.2 % | 16 % |
| Battery buffer | 3.6 % | 4 % |
| Systems and contingency | 11.0 % | 8 % |
| Fuel | 16.0 % | 16 % |
| **Payload, as residual** | **30.4 %** | **26 %** |

**Where the mass may sit is also constrained, and the constraint was not previously
stated.** The budget above says how much each item weighs and not where it sits. Section 3.17
adopts a first-order packaging rule in the absence of an internal layout — masses distributed
in proportion to internal volume — and shows that the resulting centre of gravity has to lie
in a band whose aft limit is firm and whose forward limit is not: aft of roughly 85 percent of
root chord the static margin falls below the usual tailless band, while the forward limit
depends on how much camber moment the sections can supply, which this paper does not fix. The sweep carries the neutral point to 0.859 m
from the root leading edge, well aft of the root chord's midpoint, which is what makes such
an aft centre of gravity admissible at all. The internal volume's own centroid is at 78.3
percent, so an arrangement that simply follows the available volume lands just forward of the
window; fuel, payload and engine therefore cannot be placed for convenience, and the budget
above should be read as constrained in position as well as in magnitude.

The build-up closes with 2.2 kg in hand — **conditionally, and the conditions are the
result.** It closes if the average structural areal density is no more than 1.78 kg m⁻²,
and if everything still outside the model together stays under that same 2.2 kg. Neither is
demonstrated here; the 1.5 kg m⁻² used is an aggressive target for a composite airframe of
this class rather than a measured property of one that has flown. Why a build-up coming in
lighter than its own target should be read as a warning rather than a confirmation is set
out in Section 4.4.

**The heavy design is not closed by this exercise, and no claim is made that it closes.**
Shell mass scales as areal density times wetted area, so as the square of linear scale,
while take-off mass scales as the cube; holding areal density constant would make the shell
fraction fall as the inverse of scale, which is plainly wrong, since skins on larger
aircraft are not thinner. Holding the fraction constant instead requires areal density to
grow linearly with scale. The truth lies between, and the exponent has not been measured.
Sweeping it puts the 1000 kg design's 260 kg payload at break-even at an exponent of 0.467,
an areal density of 2.64 kg m⁻², closing below and failing above. No attempt is made here
to argue for a value on either side of that threshold, because any such argument would be a
structural model standing in for a measurement. What the sweep establishes is the
statement itself: **the component build-up does not demonstrate closure of the heavy
design.** That, and not any of the light-design assumptions, is the largest open question
in the mass budget of this study, and it qualifies the scale-invariance of Section 3.9 —
which holds for the analytical sizing fractions and has not been shown to hold for the
structure that must realise them.

---

## S2.2 Closing the loop at a measured pack

Section S2.1 compares the buffer mass a measured cell would require against the unallocated mass
the build-up leaves. That comparison is a subtraction, and it is made inside a take-off mass that
was itself sized on the specific power being replaced. The feedback it omits is the ordinary
sizing loop: a heavier buffer raises take-off mass, which raises hover power, which raises the
buffer again.

**The feedback does not diverge, and that matters.** Section 3.9 holds disc loading constant,
which makes hover power grow linearly with weight rather than as the classical three-halves
power. A linear feedback accumulates to a finite answer, so the question "does it close" has a
number rather than a verdict, and the number is not where the subtraction pointed.

**Method.** Wing loading and disc loading are held at their Section 3.7 values, so the linear
scale is the square root of the mass ratio. The fuel *fraction* is held at 0.16, which preserves
range by the equation of Section 2.12. Hover shaft power, tip-pair power and engine rating all
scale linearly with take-off mass. At each candidate mass the component build-up of Section S2.1
is rebuilt at the new scale with the new buffer, and the payload residual is read. The mass at
which the residual equals 13 kg is found by bisection rather than by relaxation, so that a
non-converging case is distinguished from a solver that oscillates.

**Result, on the take-off demand** — the aircraft must leave the ground, so the tip pairs are
counted:

| Buffer specific power | Take-off mass | Buffer | Buffer, % MTOW | Range | Payload if held at 50 kg |
|---|---:|---:|---:|---:|---:|
| 0.724 kW kg⁻¹ | **no solution to 5 000 kg** | — | — | — | 0.9 kg |
| 0.892 kW kg⁻¹ | 162.0 kg | 42.4 kg | 26.2 % | 1 600 km | 3.9 kg |
| **1.50 kW kg⁻¹** | **68.9 kg** | **10.7 kg** | **15.6 %** | **1 600 km** | **9.2 kg** |
| 2.50 kW kg⁻¹ | 52.5 kg | 4.9 kg | 9.3 % | 1 600 km | 12.3 kg |
| 5.63 kW kg⁻¹ | 50.0 kg | 2.1 kg | 4.1 % | 1 600 km | 14.9 kg |

On the hover demand alone the same rows give 231.7, 110.4, 62.5, 50.2 and 50.0 kg.

**The earlier conclusion was too strong.** At 1.5 kW kg⁻¹ — the highest rate measured on the flown
pack of [47], at a thermal margin of 4.9 °C — the aircraft exists. It is 38 percent heavier, its
buffer is 15.6 percent of take-off mass rather than 3.6, and its range is unchanged because range
follows the fuel fraction. Held instead at 50 kg it carries 9.2 kg of payload rather than 13. Only
at the pack's *continuous* rating does the loop fail to converge, and only on the take-off demand.

**What this costs the comparison.** The mass advantage over the lift-plus-cruise layout — 42
percent at the assumed drag, 32 to 36 percent across the computed bracket of Section 3.6 —
layout is computed at 50 kg against 86 kg. At a measured pack the tail-sitter is 69 kg, and 69
against 86 is twenty percent. The competing layout has *not* been re-sized on the same pack, and
it would also grow; the honest statement is therefore that any single figure is
conditional on the buffer assumption and that nothing here replaces it. `aero/kapanma.py` carries
the loop.
