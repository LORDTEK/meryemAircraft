# Supplementary S2 — A component build-up of the mass budget

*Supplementary material to "The Architectural Cost of Hybrid VTOL:
meryemAircraft, a Propeller-Driven Tail-Sitting Blended-Wing-Body Without a
Dedicated Lift System".*

This material was Section 6.7 of an earlier, longer version of the paper.
It is reproduced here in full so that every number quoted in the main text can
be traced to the calculation that produced it. The computational setup, the
scripts, and the record of what failed along the way are in the repository the
paper cites.

---

## S2.1 A component build-up of the mass budget

The fractions used in Sections 6.2 and 6.3 are asserted, and Section 8.2 says so. This
section replaces the assertion for the light design with a build-up from components. The
rule followed throughout is that no item may be derived from the fraction it is meant to
test: every line comes either from the geometry and a stress calculation, or from a
specific quantity — an areal density, a specific power — stated openly and then varied.

**Structure.** The wetted area follows from the planform of Section 4.2 and the NACA 00xx
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
before.** It must supply the difference between hover power and engine rating, 8.3 kW at
the light design point, from 1.8 kg — a specific power of 4.6 kW kg⁻¹, or about 26 C at
180 Wh kg⁻¹. Energy is not the binding constraint until roughly 140 seconds of hover, well
beyond the profile of Section 7; below that the buffer is power-limited. The heavy design
is in the same regime, 4.1 kW kg⁻¹ at 22 C. That places the buffer in the high-power
lithium-ion or lithium-polymer class — cells rated for twenty to thirty times their
capacity in continuous discharge — rather than in the high-energy class a range-driven
selection would reach for.

**How demanding, measured against the only figures this study has read, is the most exposed
number in the whole mass budget.** Bacchini and Cestino, sizing electric VTOL aircraft, take
735 W kg⁻¹ at pack level from an automotive traction pack and report that "Li-ion batteries for
power applications have… specific power from 700 to 1300 W kg⁻¹" [21]. The buffer here asks for
**4.6 kW kg⁻¹**, three and a half to six and a half times the top of that range. Sized at
figures from that range instead:

| Buffer specific power | Buffer mass | Fraction of MTOW |
|---|---:|---:|
| 0.735 kW kg⁻¹ (the pack they assume) | 11.3 kg | 22.6 % |
| 1.30 kW kg⁻¹ (top of their quoted range) | 6.4 kg | 12.8 % |
| **4.61 kW kg⁻¹ (this study, implicitly)** | **1.8 kg** | **3.6 %** |

At the top of their range the buffer would be 4.6 kg heavier than budgeted, against the 2.2 kg
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
| **This study, implicitly** | **4.61 kW kg⁻¹** | **assumption** |

Sized at the measured thermal ceiling of 1.5 kW kg⁻¹ the buffer becomes **5.5 kg** rather than
1.8 kg — 3.7 kg heavier, against 2.2 kg of unallocated mass. Sized at the measured continuous
figure it becomes 9.3 kg. **The light design's mass budget does not close at any measured
specific power, and this is the single most exposed number in the paper.** It is not resolved
by arguing that the buffer is a different product: the source above *is* that product, built
and flown. What would resolve it is a pack demonstrating three times the measured specific
power at acceptable temperature, or a heavier buffer carried at the cost of payload fraction.
Section 8 states which.

**The energy side is a different matter, and it is far more comfortable than the power side.**
The buffer does not discharge continuously for the whole vertical phase. It discharges through
the take-off, which ends when the rotation begins and the wing starts carrying the aircraft;
it then recharges from the engine over hours of cruise, and discharges again for the landing.
At a thrust-to-weight ratio of 1.2 the vertical acceleration is 0.2 g, so the 5 m s⁻¹ climb
from which Section 7.4 enters the rotation is reached in 2.6 s and 6.4 m. A take-off segment of
ten to twenty seconds at full draw is generous. Against that:

| Take-off segment at full draw | Energy used | of a 180 Wh kg⁻¹ buffer | of an 80 Wh kg⁻¹ buffer |
|---:|---:|---:|---:|
| 10 s | 23 Wh | 7 % | 16 % |
| 20 s | 46 Wh | 14 % | 32 % |
| 30 s | 69 Wh | 21 % | 48 % |

Even at the low energy density that a high-power chemistry would carry, a twenty-second take-off
uses a third of the buffer. **The binding constraint is power, not energy, and it stays that way
under any plausible take-off duration.**

That distinction matters, because it says what would *not* rescue the specific-power figure.
A shortfall in power is not a transient to be ridden out. Hover power goes as thrust to the
three-halves, so thrust goes as power to the two-thirds, and a buffer delivering less simply
buys less thrust:

| Buffer specific power | Total power available | Resulting T/W | Leaves the ground |
|---|---:|---:|---|
| 0.735 kW kg⁻¹ | 3.9 kW | 0.61 | no |
| 1.30 kW kg⁻¹ | 4.9 kW | 0.71 | no |
| 2.50 kW kg⁻¹ | 7.1 kW | 0.90 | no |
| 4.61 kW kg⁻¹ | 10.9 kW | 1.20 | yes |

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
stated.** The budget above says how much each item weighs and not where it sits. Section 7.6
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
out in Section 8.2.

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
in the mass budget of this study, and it qualifies the scale-invariance of Section 6.4 —
which holds for the analytical sizing fractions and has not been shown to hold for the
structure that must realise them.
