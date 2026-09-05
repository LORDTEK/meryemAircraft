# 6. Reference designs at two scales

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

A configuration argument is only as good as its willingness to become a number. This
section sizes two aircraft from the arrangement of Section 4 — one at 50 kg and one at
1000 kg, a factor of twenty apart in mass — using the same equations, the same
assumptions and the same architecture. The two points are not a light version and a
heavy version of different aircraft. They are the same aircraft at two sizes, and the
purpose of presenting both is to show that the proportions hold.

Every number below is calculated, not measured. Section 8 says what that means.

## 6.1 Sizing method

The method is deliberately elementary, and the equations are given so that any result
in this section can be checked by hand.

**Hover.** Thrust equals weight, and induced power follows from momentum theory:

    v_i = √(T / 2ρA)          P_i = T^1.5 / √(2ρA)

with the disc loading DL = T/A as the governing parameter. Figure of merit is applied
to obtain shaft power.

**Cruise.** Lift equals weight, which fixes the lift coefficient at the chosen cruise
speed; drag then follows from the polar, and the lift-to-drag ratio is the ratio of the
two at that point:

    C_L = W / (q S),   q = ½ ρ V²

    C_D = C_D0 + C_L² / (π · AR · e)

    L/D = C_L / C_D

This is evaluated **at the cruise condition**, not at the aircraft's best point. The
familiar expression L/D_max = 0.5 √(π·AR·e/C_D0) gives the *maximum* lift-to-drag ratio,
which occurs at one particular lift coefficient and therefore at one particular speed —
25.3 m s⁻¹ for the light design, only 1.26 times its stall speed. Cruising there would
leave too little margin, so both reference designs cruise at 1.49 times stall instead
and accept the lift-to-drag ratio that this condition gives. Using the maximum value
while specifying a different cruise speed would overstate the range, and an earlier
version of this paper did exactly that; the figures below are computed at the cruise
point.

**Range.** The series-hybrid chain is stated explicitly rather than folded into a
single efficiency, because the result is sensitive to it and a reader should be able to
disagree with any single link:

| Link | Value |
|---|---:|
| Internal-combustion engine | 0.28 |
| Generator | 0.90 |
| Power electronics | 0.95 |
| Electric machine | 0.92 |
| Propeller | 0.80 |
| **Overall** | **0.176** |

Fuel energy is taken as 12.9 kWh kg⁻¹. The engine figure is the one that matters most:
0.28 is representative of a small four-stroke engine at its best operating point, and
it is the reason the range figures below are lower than an optimistic estimate would
give.

**Control.** Tip-pair thrust follows from the required angular acceleration,
M = 2 T L = I α, with the transition manoeuvre as the sizing case.

**Assumptions carried throughout:** sea-level density; no compressibility; span
efficiency e assumed at 0.85; C_D0 assumed at 0.0248 for the light design, which is
generous for a clean blended-wing body and is intended to absorb the tip-frame
contribution of Section 5.2 — that contribution is 0.0043, or seventeen percent of the
assumed C_D0, so the assumption is self-consistent rather than optimistic. Both
coefficients remain assumptions in what follows. Section 6.6 does not replace them; it
bounds them by independent calculation, which is a weaker but more honest claim.

## 6.2 Light reference design — 50 kg

| Quantity | Value |
|---|---:|
| Maximum take-off mass | 50 kg |
| Root chord | 0.97 m |
| Tip chord | 0.236 m |
| Span | 3.45 m |
| Wing area | 1.98 m² |
| Aspect ratio | 6.00 |
| Wing loading | 25.3 kg m⁻² |
| Main propeller diameter | 1.20 m |
| Disc loading | 44.2 kg m⁻² |
| Tip propeller diameter | 0.20 m |
| Frame post length | 0.71 m each direction |
| Stall speed | 20.1 m s⁻¹ |
| Cruise speed | 30 m s⁻¹ (108 km h⁻¹) |
| Cruise L/D | 12.0 |
| Hover power | 10.9 kW |
| Cruise power, electrical | 1.7 kW |
| Engine rating | 2.6 kW |
| Battery buffer | 1.8 kg (3.6 % MTOW) |
| Fuel | 8 kg |
| **Endurance** | **14.8 h** |
| **Range** | **1 598 km** |
| Transition time | 2 s |

The mass budget behind this is a target and not a finding: 30 % structure, 16 %
propulsion chain, 4 % battery, 8 % avionics and control, 16 % fuel, leaving 26 % —
13 kg — for payload. Paper aircraft are habitually lighter than the ones that get
built, and that margin has not been paid in this table. Section 8 repeats this warning,
because it is the single most likely place for these numbers to be wrong.

## 6.3 Heavy reference design — 1000 kg

| Quantity | Value |
|---|---:|
| Maximum take-off mass | 1000 kg |
| Root chord | 3.25 m |
| Span | 11.55 m |
| Wing area | 22.24 m² |
| Wing loading | 45.0 kg m⁻² |
| Main propeller diameter | 5.40 m |
| Disc loading | 43.7 kg m⁻² |
| Tip propeller diameter | 0.67 m |
| Frame post length | 2.38 m each direction |
| Cruise speed | 40 m s⁻¹ (144 km h⁻¹) |
| Cruise L/D | 13.6 |
| Hover power | 216.2 kW |
| Cruise power, electrical | 39.2 kW |
| Engine rating | 54.3 kW |
| Battery buffer | 40 kg (4.0 % MTOW) |
| Fuel | 160 kg |
| **Endurance** | **12.6 h** |
| **Range** | **1 814 km** |
| Transition time | 4 s |

The heavy design has a longer range than the light one despite a shorter endurance.
Both effects come from the same source: the larger aircraft cruises faster and, at a
higher Reynolds number, achieves a lower zero-lift drag coefficient and therefore a
better lift-to-drag ratio. Nothing in the architecture was changed to obtain this.

## 6.4 Scale behaviour

Five properties of the scaling are worth separating, because three of them are
favourable and two are not. Figure 11 shows the two designs at a common scale, and it
shows the second of the unfavourable ones directly.

**Disc loading is held constant.** The two designs sit at 44.2 and 43.7 kg m⁻². This is
not a coincidence of sizing but the rule that governs it. Hover power per unit weight
is √(DL/2ρ), so holding disc loading constant holds the specific hover power constant,
and the aircraft can grow without the hover condition running away. The effect is direct:
hover power rises from 10.9 kW to 216.2 kW, a factor of 19.8 against a mass factor of 20.
Hover power grows *linearly* with mass rather than as the L^3.5 of the classical result,
and that is the whole benefit of fixing the disc loading.

Constant disc loading means disc area must grow in proportion to weight. For a
geometrically similar aircraft, whose mass grows as L³, that is a demand for disc area to
grow as L³ rather than as L² — which for a fixed number of propellers is impossible. This
architecture has two ways out of that, and it uses both. It may add coaxial pairs, and
adding a pair is architecturally free because every pair is already torque-balanced on
its own; and, as the next paragraph records, it does not hold geometric similarity.

**The propeller grows faster than the airframe.** This is the second exception, and it
is visible in Figure 11 rather than hidden in it. Wing loading is not held constant: it
rises from 25.3 to 45.0 kg m⁻², so wing area grows by a factor of 11.2 and span by 3.35
— more than the 2.71 that geometric similarity at constant density would give, but well
short of the 4.50 by which the main propeller must grow to hold the disc loading. The ratio of
propeller diameter to span therefore rises from 0.35 to 0.47. The heavy design is not the
light design photographed from further away; its propeller occupies almost half its span.

Nothing in the argument of this paper fails because of that, since the propeller is the
nose of the aircraft rather than an appendage on it, and disc loading — the quantity the
hover power depends on — is what is being held. But the claim that the configuration
keeps its proportions across the range should be read as applying to the four quantities
named here and not to every dimension, and a design much heavier than 1000 kg would reach
the point where a single nose pair can no longer hold the disc loading and a second pair
must be added.

**The buffer fraction is preserved.** 3.6 % of MTOW at 50 kg and 4.0 % at 1000 kg. The
mechanism by which Bill 3 is avoided therefore does not degrade with size.

**The frame drag fraction is preserved.** Frontal area and wing area both scale as L²,
so the twelve percent of Section 5.2 holds at both ends.

**Transition time does not scale.** This is the exception, and it is stated plainly.
The control moment required to rotate the aircraft follows M = Iα with I ∝ mL², so the
moment needed to turn it in a fixed time grows much faster than the aircraft itself.
Scaling the light design's two-second rotation geometrically to 1000 kg would demand
221.5 kW from the tip propellers — 102 % of the hover power, which is to say it is not
available at all:

**Table 4.** Tip-propeller power required to rotate the heavy reference design.

| Rotation time | Tip-propeller power, 4 total | Fraction of hover power |
|---:|---:|---:|
| 2 s | 221.5 kW | 102 % |
| 3 s | 65.6 kW | 30 % |
| **4 s** | **27.7 kW** | **13 %** |
| 5 s | 14.2 kW | 7 % |

**The rule is that a larger aircraft turns more slowly.** The heavy design rotates in
four seconds, at thirteen percent of its hover power.

This constraint is less costly than it first appears, and Section 7 explains why: a
slower rotation does not lose more altitude but less, so the scaling penalty on
transition time works in the same direction as the scaling penalty on control power
rather than against it. The larger aircraft is obliged to turn slowly, and turning
slowly is what it should do anyway.

The classical objection to scaling a VTOL aircraft up is that hover power required grows
as L^3.5 while power available grows as L³. Fixing the disc loading is what removes that
objection on the hover side, as the first item above shows. It does not remove it on the
transition side, and Table 4 is where it reappears: the rotation is the one place in this
aircraft where the square–cube relation is still paid in full.

## 6.5 Context

The following aircraft occupy the same mass range. They are listed to locate the
reference designs in a real field, not to rank them.

| Aircraft | MTOW | Payload | Payload fraction |
|---|---:|---:|---:|
| HAVELSAN BAHA [8] | 28 kg | 2 kg | 7.1 % |
| Textron Aerosonde Mk 4.7 VTOL [9] | 45.4 kg | 9.1 kg | 20.0 % |
| Baykar KALKAN [10] | 75 kg | ~3 kg internal | 4.0 % |
| HAVELSAN BULUT [11] | not published | 5 kg | — |
| Elroy Air Chaparral [12] | 865 kg | 136 / 227 kg | 15.7 / 26.2 % |
| Sabrewing Rhaegal-A [13] | 1400 kg | 360–450 kg | 25.7–32.1 % |
| Pipistrel Nuuva V300 [14] | 1700 kg | 408 kg | 24.0 % |

All entries are taken from manufacturers' published material. Payload definitions are not consistent between them — some quote internal payload, some external, some both — and empty weights are generally not published. The lightest entry has been confirmed from its manufacturer's data sheet as a vertical take-off aircraft [8].

Three statements can be made about this table and a fourth cannot.

First, the field is real and populated, at both ends of the mass range considered here.
Second, payload fraction rises with size across the field, from a few percent at the
light end to roughly a quarter at the heavy end, which is the ordinary consequence of
fixed costs not scaling down. Third, none of these aircraft connects an
internal-combustion engine directly to a lifting rotor; every one of them uses either a
generator or separate electric lift, which is independent confirmation that the series
arrangement of Section 4.3 is the practical choice at this scale rather than an
unusual one.

The fourth statement — that the reference designs outperform these aircraft — is not
made, and the numbers in Sections 6.2 and 6.3 should not be read as making it. Those
numbers are calculated from a mass budget with an unpaid structural margin; the numbers
in this table describe aircraft that exist and fly. Placing a calculation beside a
measurement and declaring a winner would be a category error, and the comparison is
offered only to show that the reference designs fall inside the field rather than
outside it.

A further caution applies to any comparison of endurance or range across this table.
Several of these aircraft are fully electric, and for those the endurance figure is set
by battery specific energy rather than by configuration. The lightest entry, for
instance, is an all-electric fixed-wing VTOL quoting up to two hours of endurance;
setting the fuel-burning reference design of Section 6.2 against that number would
compare energy sources, not architectures, and would say nothing about the argument of
this paper.

What can properly be compared, once these aircraft have been built and flown, is range
at similar payload — not payload at similar range. A configuration that carries a
comparable load further is making an architectural claim; a configuration that carries
a heavier load is making a claim about mass budgeting, which is exactly the part of
this study that is least validated.

## 6.6 Independent checks on the two assumed coefficients

The two coefficients that carry the most weight in Section 6 — span efficiency and
zero-lift drag — were assumed rather than derived. They remain assumed. What follows
does not replace them with computed values; it asks a narrower question that can be
answered honestly: **are the assumed values inside the range that a calculation gives,
and on which side?**

**Span efficiency.** A vortex-lattice solution of the planform of Section 4.2 [15] gives
an inviscid span efficiency of 0.99. That is not the same quantity as the 0.85 used here.
The vortex-lattice figure counts only the departure of the induced drag from the
elliptic ideal; the 0.85 is an Oswald-type efficiency that also carries the viscous
drag due to lift, which for a clean wing runs at roughly 85 to 90 percent of the
inviscid value. The two are consistent. Reporting the calculation as an improvement on
the assumption would be a category error, and it is not claimed.

The same solution gives a lift-curve slope of 3.87 rad⁻¹ against the 4.72 rad⁻¹ that
the transition simulation of Section 7.4 assumes — eighteen percent lower, and in the
unfavourable direction. Section 8.6 reports what that does to the transition results.

**Zero-lift drag.** A strip calculation over the span, taking section drag coefficients
at zero lift from a physics-informed aerofoil model [16] and adding the tip frames and the propeller hubs, gives:

| Contribution | Light design |
|---|---:|
| Wing and body, clean surface | 0.0073 |
| Wing and body, transition tripped near the leading edge | 0.0129 |
| Tip frames, faired | 0.0043 |
| Tip-propeller hubs | 0.0015 – 0.0020 |
| **Total** | **0.0131 – 0.0210** |

The frame term reproduces the 0.0043 of Section 5.2, which was reached by a different
route, and it comes out the same for the heavy design — an independent confirmation of
the scale invariance claimed in Section 6.4. The hub term is bounded by hardware rather
than guessed: each tip rotor must deliver about 0.83 kgf on a 0.20 m propeller, which
places it in the standard 22 mm stator class whose outer cans measure roughly 28 mm.

**The assumed 0.0248 lies above the whole of that range.** The assumption is therefore
conservative in every scenario considered, not merely in the pessimistic one. Because
range is linear in lift-to-drag ratio, the reference designs of Sections 6.2 and 6.3
would gain rather than lose if the calculation were adopted — which is the reason it is
not adopted. An assumption that is declared and shown to be conservative is a smaller
target than a calculation whose weakest link, discussed in Section 8.4, is the
treatment of a twenty-five percent thick centre body as a two-dimensional section.

**A three-dimensional solution for the centre body.** The weakness just named has since
been removed. Section 8.12 lists it first among the places these results should be
attacked, and the calculation it asks for has now been carried out: a structured
Reynolds-averaged solution over the planform of Section 4.2, at the cruise Reynolds
number and at zero lift, resolving the wing and blended body as a three-dimensional
surface rather than as stacked sections. It gives a wing-and-body zero-lift drag of

**0.0141, with a measured uncertainty of about five percent**,

against the 0.0129 of the tripped strip estimate — nine percent higher, and in the
unfavourable direction. Substituting it for the strip figure raises the total to 0.0224.
**The assumed 0.0248 still lies above it**, so the conclusion of the previous paragraph
survives the more expensive calculation; the margin narrows from seventeen percent to
eleven. The assumption is not replaced here either, for the same reason as before.

The five percent is itself measured rather than asserted:

| Source of uncertainty | Magnitude |
|---|---:|
| Iterative convergence | 0.1 % |
| Spatial discretisation, three grids of 0.27 – 2.66 M cells | < 0.1 % |
| Wall resolution, y⁺ 20 → 1 | 1.6 % |
| Wall resolution, y⁺ 43 → 20 | 10 % |
| Turbulence model, k-ω SST against Spalart–Allmaras | 2.7 – 8.1 % |

The dominant term is the turbulence model, not the grid — which is worth stating plainly,
because grid convergence is the check a reader expects and it turns out to bound the
smallest of the five terms. Two further results are recorded because they are easy to get
wrong in either direction. The forces converge far more slowly than the residuals: at a
velocity residual of 1.6 × 10⁻⁵ the computed drag was still fifty-five percent above its
converged value, so a solution stopped on residuals alone would have been badly wrong.
And the wall-resolution sensitivity saturates rather than continuing: between y⁺ 20 and
y⁺ 1 the drag moves by 1.6 percent, so the wall-function results are not systematically
far from the wall-resolved one, and an extrapolation of the coarser trend overstated the
wall-resolved value by nine percent.

**What this does not settle.** The solution is fully turbulent throughout. It therefore
speaks to the tripped row of the table above and not to the clean-surface row, and the
gap between those two rows — 0.0073 against 0.0141 — is now the largest single
uncertainty in the zero-lift drag. Closing it requires a transition-sensitive model,
which needs a wall-resolved grid and a two-equation formulation at the same time; that
combination was attempted and did not converge. The clean-surface bound therefore remains
where the strip calculation left it.

**Internal volume.** One closure that the mass budget does not address is whether the
payload fits. The body's gross internal volume follows from the thickness distribution:
185 litres for the light design. Taking rather more than half of that as usable and
subtracting fuel, buffer, powerplant and avionics leaves about 80 litres for 13 kg of
payload, which requires a mean density of only 0.16 kg per litre. The configuration is
mass-limited rather than volume-limited, and the choice of mission therefore constrains
the structure and the load paths rather than the internal arrangement.
