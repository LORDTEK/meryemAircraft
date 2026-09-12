# 3. Results

Results are given in four groups: the framework tested against published sizing
studies (Section 3.1), the three charges audited against the proposed configuration
(Sections 3.2 to 3.6), two reference designs with the bounds on their assumed coefficients and a
component build-up of their mass (Sections 3.7 to 3.11), and the flight profile with the
transition analysis (Sections 3.12 to 3.17). Every number is calculated rather than measured;
Section 4 states what that means.

## 3.1 The three bills stated formally

Supplementary S6 states the three bills as equations and gives the transfer table that shows
them to be one quantity in three currencies: a design that refuses to pay one of them pays it
in another. The short form is that each bill is a fraction of take-off mass, exposed cruise
drag, or installed continuous power, and that the three are linked by the sizing loop — mass
drives thrust, thrust drives power, power drives mass — so that relieving one without relieving
its cause simply moves the charge.

**A consequence that can be checked against published work.** If the framework is right, then
for the same mission a configuration carrying a dedicated lift system should pay for it in gross
weight, and that payment should *not* be recovered by the cruise efficiency the arrangement buys.
This is a sharper prediction than it first appears, because it forbids the obvious defence: it
says the efficiency gain is real and still insufficient. The NASA sizing set is a direct test of
it. Against a common mission of 1 200 lb of payload over 75 nautical miles, the turboshaft
quadrotor — which has no cruise wing, and therefore no dedicated lift hardware to carry — sizes
at an effective lift-to-drag ratio of 4.9 and a design gross weight of 3 678 lb, while the
turbo-electric lift-plus-cruise reaches 8.5 and weighs 7 271 lb [22]. **Its cruise efficiency is
seventy percent better and it is nearly twice as heavy**, which is the prediction and not a
counter-example to it. The tilt-wing in the same set reaches 8.6 — higher than every
lift-plus-cruise entry — while carrying no dedicated lift system at all, and it is the one
configuration in the table that uses the same hardware in both regimes. The framework does not
predict the numbers; it predicts that the weight charge survives the efficiency credit, and in
this set it does.

**What the framework does not claim.** It does not claim that avoiding the three bills makes an
aircraft better, only cheaper in those three specific currencies. A configuration may avoid all
three and still be unbuildable, uncontrollable, or unsuited to its mission — and Sections 3 and
4 are about exactly that possibility for the configuration proposed here. Nor does it claim the
bills are the only costs; they are the ones that follow from the duty-cycle mismatch of Section
2.1, and a design pays many others.

Sections 2.1 to 2.6 identified three bills and argued that they are one quantity paid in three
currencies. Sections 2.7 to 2.11 described a configuration built to satisfy the zero-bill
condition. This section audits that claim bill by bill, and then states, in the same
detail, what the configuration does pay. The second half is not a concession appended
for balance. An architecture that claimed to pay nothing would be describing a
different aircraft from the one in Section 2.

## 3.2 Bill 1 — mass: the charge does not arise

There is no second propulsion group. The nose pair that lifts the aircraft off the
ground is the same pair, in the same orientation, at the same station, that propels it
in cruise. Nothing is carried unused.

This is the whole of the argument, and its brevity is the point. The bill was never a
consequence of poor design in lift-plus-cruise aircraft; it was a consequence of
counting two propulsion systems where the mission needs one. A configuration that
counts one does not reduce the bill — it does not generate it.

The tip pairs are a genuine addition and are accounted for in Section 3.5. They are not
a second propulsion group: they are sized from the moment requirement rather than from hover
weight support, though Section 3.15 shows that the thrust that sizing gives them also supplies
the aircraft's entire take-off margin. In
the vertical phase they draw 1.34 kW against the nose pair's 10.9 kW, which is twelve
percent.

## 3.3 Bill 2 — drag: reduced, not removed

In cruise there is no stopped rotor in the airstream, because there is no rotor that stops. The
nose pair is the cruise propulsor and runs at its design condition throughout. The quarter of
lift-to-drag ratio that Section 2.3 reports as the measured cost of installing hover hardware is
not incurred — not reduced, not mitigated, but **absent**, because the hardware that causes it
does not exist here. Nor is there a retraction mechanism, so the transfer of Bill 2 into Bill 1
does not occur either. Where lift rotors are retained, keeping their drag small needs an
indexing mechanism to stop them at a favourable azimuth, or a retraction mechanism to stow them;
both are mass and both are failure modes, and a configuration with no rotor to stop needs
neither.

**That carries a condition the paper had not stated, and it is a sharp one.** The four tip pairs
*are* rotors, and the claim holds only if they do not stop in cruise. Their eight discs sweep
0.251 m², **12.7 percent of the wing area** — not a small object to leave in the airstream in
the wrong state:

| Tip rotors in cruise | ΔC_D0 | of the 0.0248 assumed |
|---|---:|---:|
| turning at zero shaft load, blades at low incidence | 0.0003 – 0.0008 *(assumed)* | 1 – 3 % |
| turning at zero shaft load, **computed below** | **0.0085 – 0.0423** | **34 – 171 %** |
| stopped edge-on, at a chosen azimuth | 0.0008 | 3 % |
| **stopped broadside, azimuth uncontrolled** | **0.015 – 0.018** | **61 – 74 %** |

**The first and third rows were taken to differ by a factor of thirty, and that gap was the whole
of the argument**: whatever the coefficients, a configuration that holds its tip rotors turning
was held to be safely far from one that stops them broadside. The computed second row removes the
gap. It is derived later in this section, and it is reported here rather than buried because it
changes what this subsection concludes. The *stopped edge-on* row shows, separately, why stopping
the rotors is survivable only if azimuth is controlled — which is the indexing mechanism this
section has just claimed the configuration does not need.

**The resolution costs nothing, and it is a control state rather than hardware.** A fixed-pitch
propeller left free settles at the advance ratio where net shaft torque is zero: inner sections
drive, outer sections retard, and they balance. The shaft then does no work, so the motor
neither drives nor brakes and the electrical cost is controller standby draw and bearing losses.
The blades sit at low incidence, which was taken to put them in the first row. **The tip rotors
are therefore held in cruise at the zero-shaft-torque condition — neither stopped nor driven** —
and this is the state assumed throughout Section 3. It is worth naming because both neighbouring
states are wrong: driven, they cost propulsive power; stopped without azimuth control, they cost
most of the aircraft's zero-lift drag. What the state costs *itself*, the paragraphs below now
compute, and the answer is not the first row.

**That first row has since been computed rather than assumed, and it is the worst result in this
paper.** A blade-element calculation was set up the only way that makes the comparison mean
anything: the blade is first *designed* for the hover duty — each station twisted to a target
section lift coefficient and chorded to carry its share of 8.1 N, with section data taken at each
station's own Reynolds number — so that what is run at cruise is this aircraft's propeller rather
than a generic one. Four designs were built, spanning target section lift coefficients from 0.40
to 0.85 and hover figures of merit from 0.62 down to 0.27. Each was then run at 30 m s⁻¹ and the
shaft speed found at which net torque is zero.

| Design section c_l | Hover figure of merit | Free-wheeling speed | Tip Mach | ΔC_D0, eight discs |
|---:|---:|---:|---:|---:|
| 0.40 | 0.62 | 36 400 rpm | 1.12 | 0.0423 |
| 0.55 | 0.65 | 29 200 rpm | 0.90 | 0.0238 |
| 0.70 | 0.35 | 19 800 rpm | 0.61 | 0.0126 |
| **0.85** | **0.27** | **14 500 rpm** | **0.45** | **0.0085** |

**Every design exceeds the assumed 0.0003–0.0008, and the lowest exceeds it by a factor of ten.**
The two fastest rows must be discarded on their own terms — the section data are incompressible
and those tip speeds are not — but the last row is at Mach 0.45, inside the model's range, and it
alone gives **0.0085: twice the 0.0043 charged for the tip frames, and thirty-four percent of the
total zero-lift drag the sizing assumes.**

The mechanism does not depend on the solver. A propeller designed for hover has low pitch; left
free at 30 m s⁻¹ it must spin fast before its sections reach zero incidence, and at that speed
the blades' own profile drag is large. The trend across the four designs is the trade stated
plainly: the blade that hovers well free-wheels fastest and drags most. Section 2.9 rules out the
escape, because these pairs are of fixed geometry and cannot feather.

**The consequence is stated rather than absorbed.** Bill 2 is not absent. On the most favourable
design computed here the tip rotors cost at least as much as the frames already charged, the
cruise lift-to-drag ratio falls, and the margin over the lift-plus-cruise layout narrows by an
amount this paper has not re-sized. What would settle it is a propeller design study that
optimises the blade across both duties rather than for hover alone, or a variable-pitch tip pair
— which is a mechanism, and mechanisms are what this configuration was built to avoid.

What Bill 2 *is* paid, and this is why the heading says reduced rather than removed, is the tip
frames. They are structure in the airstream that a conventional aircraft does not carry, and at
the light design point they contribute ΔC_D0 = 0.0043 — **about twelve percent of total cruise
drag**, and seventeen percent of the zero-lift drag the sizing assumes. Both denominators appear
in this paper and each is named where it is used. That is the honest figure and it is carried in
the ledger of Section 3.5.

**The fairing on those frames is not only a drag measure.** The frames are the only surfaces
standing perpendicular to the wing plane, and the planform supplies no directional stability at
all, so the fairing is also the vertical surface that provides it. Sized against the criterion
the tailless literature recommends — C_n_β greater than 0.001 per degree [19] — the chord
required over the combined frame length is 39 mm, against the 50 to 70 mm a 20 mm faired strut
carries in any case. The two requirements do not conflict, and the directional one is the looser;
but the frame cross-section is now constrained from two directions, and a selection made on drag
alone would be made on half the evidence.

## 3.4 Bill 3 — power system sizing: avoided for the engine, not for the electrical path

The series-hybrid arrangement of Section 2.9 breaks the link that forces the power
system to be sized by the hover condition. Because the engine drives a generator rather
than a rotor, it supplies average power, not peak power, and the peak is supplied from
a buffer.

For the light reference design the numbers are as follows. Cruise draws 1.7 kW at the
electric machines, which is 1.9 kW at the engine shaft once the generator and power
electronics are accounted for, and the engine is sized at 2.6 kW. Hover requires 10.9 kW
at the rotor — 4.2 times the engine's rating. The difference is drawn for the duration of
the vertical phase from a 1.8 kg battery, which is 3.6 percent of the maximum take-off
mass. **That difference must be taken at one station, and it is the electrical bus**: the
rotor's 10.9 kW of shaft power is 12.47 kW at the bus once the machine and the power
electronics are passed, the engine delivers 2.34 kW there through the generator, and the
buffer supplies the remaining 10.13 kW. Supplementary S2 gives the chain and records that an
earlier version of this paper differenced two shaft stations instead, understating the demand
on the buffer by twenty-two percent. The heavy reference design sits on the same line:
39.2 kW electrical in cruise, 54.3 kW engine, 216.2 kW hover, 40 kg of battery at 4.0 percent
of MTOW.

An aircraft of this class whose powerplant had to be sized for hover would carry an
engine rated above 10.9 kW instead of 2.6 kW. The mass difference is not recovered
elsewhere; it is simply not incurred. That the buffer costs under four percent of MTOW
at both design points, twenty times apart in mass, is the numerical statement that this
avoidance is architectural rather than a fortunate coincidence of one size.

**What is not avoided, and the section heading says so.** The bill is defined in Section 2
as a *continuous* power system sized by the hover peak, and it is the engine and its fuel
consumption that the buffer releases from that condition. The electrical path is not
released: the nose motor and the power electronics must still pass the full 10.9 kW, and
the component build-up of Section 3.11 shows them as 2.73 kg and 0.61 kg against 2.60 kg of
engine and generator — that is, the hover-sized electrical machine is the single largest
item in the propulsion chain. The saving is real and it is the engine's, but a reader
should not take it as an aircraft on which nothing is sized by hover. The buffer itself
carries a further condition, given in Section 3.11: it is specified by power rather than
energy, at **5.63 kW kg⁻¹** to hover and 6.48 to leave the ground, which is a demanding cell
requirement and not a free parameter. Section 4.4 measures it against what has been flown.

## 3.5 What is paid

The honest ledger has five entries.

**The control propellers.** Four pairs, their motors, mounts and wiring exist only to
produce moments. In the vertical phase they draw twelve percent of the power the nose
pair draws. This is the configuration's substitute for elevons and a rudder, and it is
not free — it is merely cheaper than a second lift system, and it does not sit in the
cruise airstream in the way a lift rotor does.

**The tip frames.** As established in Section 3.3, of the order of twelve percent of
cruise drag, conditional on being faired. This is the largest single payment the
configuration makes, and it is the price of the moment arm, the propeller mounting and
the landing structure combined into one member.

**The roll strip.** The one moving aerodynamic device on the aircraft. Its cost when
retracted is a surface discontinuity; when deployed it is a drag device by construction,
but it is deployed only while a roll is being commanded.

**The twist needed to trim.** Section 3.17 finds that the configuration trims at cruise with
nine degrees of tip washout, reflex being an order of magnitude short of the moment required.
Washout is not free: it costs span efficiency, and the cruise lift-to-drag ratio falls from
12.65 to 12.11 — **4.3 percent**. This entry was missing from earlier versions of this ledger,
and it is worth being precise about what it is a payment for. It is not one of the three bills
of Section 2, which are charged for having a hover capability; it is charged for being
tailless, and a tailed aircraft of the same architecture would not pay it. It belongs here
because this configuration is tailless, and because a ledger that omitted it would be
flattering rather than honest.

**The transition manoeuvre.** The aircraft must rotate through ninety degrees, and the
rotation costs time, horizontal displacement and control power. Section 3 treats it in
full and shows that the altitude cost, which is the one usually assumed to dominate, can
be brought to zero: rotating slowly and entering the rotation while still climbing
removes it entirely at both design points. What remains is not free — the manoeuvre
occupies seconds during which the aircraft is neither hovering nor cruising — but it is
smaller than the literature on tail-sitters would suggest, and it is the one payment on
this list that gets *cheaper* the less it is hurried.

Set against the bills of Section 2, the ledger is favourable but not empty. The
configuration does not escape physics; it declines a particular trade. What it pays
instead is smaller, and — this is the part that matters for scaling — it does not grow
faster than the aircraft.


## 3.6 A comparative sizing of three architectures

Supplementary S6 sizes three architectures against the same mission — this tail-sitter, a
lift-plus-cruise aircraft, and a tilt-rotor — under three different sizing contracts: fixed fuel
fraction, fixed fuel mass, and fixed maximum take-off mass with fixed payload. One set of
equations serves all three, and every coefficient in it is back-solved from the light reference
design of Section 3.7 rather than assumed. Mission, wing loading, disc loading, structural
fraction and energy chain are held identical; only the cruise-drag multiplier and the
architecture-specific mass differ. Under the first contract:

| | Empty fraction | MTOW | Cruise L/D | Hover power | Range |
|---|---:|---:|---:|---:|---:|
| A — tail-sitter | **0.580** | **50.0 kg** | 12.00 | **10.9 kW** | 1 600 km |
| B — lift + cruise | 0.689 | 86.0 kg | 10.28 | 18.7 kW | 1 370 km |
| C — tilt | 0.624 | 60.3 kg | **13.44** | 13.1 kW | **1 792 km** |

**The ordering depends on which contract is used, and that dependence is the result rather than
an inconvenience.** Range in the sizing equation contains the fuel *fraction*, so holding the
fraction fixed lets the heavier aircraft carry proportionally more fuel and removes the mass
bill from the range column altogether. Fixing the fuel *mass* makes range inversely proportional
to take-off mass; fixing take-off mass and payload leaves fuel as the residual. These are three
different questions, and the answers separate:

| Range relative to the tail-sitter | Fixed fuel fraction | Fixed fuel mass | Fixed MTOW and payload |
|---|---:|---:|---:|
| B — lift + cruise | −14.4 % | −36.5 % | −72.6 % |
| C — tilt | **+12.0 %** | +0.2 % | −19.1 % |

Against lift-plus-cruise the conclusion is the same under every rule and grows more emphatic as
the rule tightens, and the drag term driving it is a wind-tunnel result rather than an
assumption. Against tilt it is not: of the twelve cells S6 reports, the tilting layout leads in
three, all of them under the fixed fraction and all of them requiring its nacelles, pivots,
actuators and hover-pitched blades to be credited as aerodynamically free. **No result from this
section should be quoted without the rule it was computed under**, and no claim of superiority
over the tilting family is made here in either direction.

**What this comparison does and does not support.** It supports the claim that the three bills
are real and separable in a sizing loop. It does **not** support a claim that this configuration
is better: the competing architectures are modelled from published mass fractions at a coarser
level of detail than the one proposed here, which is modelled from a component build-up.
**Comparing a build-up against a fraction favours whichever is modelled more optimistically**,
and this study cannot rule out that it is this one. An external check against three flying
eVTOLs, one per architecture, is reported in S6.1; it corroborates the ordering of the charges
but is a comparison of other people's aircraft, not of this sizing. Section 4 states the
comparison as conditional on both asymmetries.

A configuration argument is only as good as its willingness to become a number. This
section sizes two aircraft from the arrangement of Section 2 — one at 50 kg and one at
1000 kg, a factor of twenty apart in mass — using the same equations, the same
assumptions and the same architecture. The two points are not a light version and a
heavy version of different aircraft. They are the same aircraft at two sizes, and the
purpose of presenting both is to show that the proportions hold.

Every number below is calculated, not measured. Section 4 says what that means.

## 3.7 Light reference design — 50 kg

| Quantity | Value |
|---|---:|
| Maximum take-off mass | 50 kg |
| Root chord | 0.97 m |
| Tip chord | 0.236 m |
| Span | 3.45 m |
| Wing area | 1.98 m² |
| Aspect ratio | 6.03 |
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

The mass budget behind this — 30 % structure, 16 % propulsion chain, 4 % battery, 8 %
avionics and control, 16 % fuel, leaving 26 %, or 13 kg, for payload — is the allowance the
design is sized against, and it is asserted here rather than derived. Section 3.11 rebuilds
it from components and finds it can be met, with 2.2 kg in hand, on one condition that is
not demonstrated: a structural areal density no greater than 1.78 kg m⁻². Paper aircraft
are habitually lighter than the ones that get built, and no allowance for that has been
paid in this table beyond the contingency inside the build-up. Section 4.4 keeps the areal
density as the most likely place for the *structural* numbers to be wrong, and identifies the
battery buffer's specific power — not the structure — as the most exposed number in the paper.

## 3.8 Heavy reference design — 1000 kg

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
| Transition time | 5.1 s |

The heavy design has a longer range than the light one despite a shorter endurance.
Both effects come from the same source: the larger aircraft cruises faster and, at a
higher Reynolds number, achieves a lower zero-lift drag coefficient and therefore a
better lift-to-drag ratio. Nothing in the architecture was changed to obtain this.

## 3.9 Scale behaviour

One qualification applies throughout: this is the scaling of the analytical sizing model — of
powers, loadings and mass *fractions*. Whether the heavy design's structure closes depends on
how shell areal density grows with size, which was not measured. Figure 11 shows the two
designs at a common scale. Four properties are preserved and one is not.

**Disc loading is held constant** — 44.2 and 43.7 kg m⁻². This is the rule that governs the
sizing rather than a coincidence of it. Hover power per unit weight is √(DL/2ρ), so fixing disc
loading fixes specific hover power: hover power rises from 10.9 kW to 216.2 kW, a factor of 19.8
against a mass factor of 20. **Hover power grows linearly with mass rather than as the L^3.5 of
the classical result**, and that is the whole benefit of fixing it. The cost is that disc area
must then grow as L³ rather than L², which for a fixed number of propellers is impossible. The
architecture has two ways out and uses both: a coaxial pair may be added at no architectural
cost, since every pair is torque-balanced on its own; and geometric similarity is not held.

**The propeller therefore grows faster than the airframe.** Wing loading rises from 25.3 to
45.0 kg m⁻², so span grows by 3.35 against the 4.50 by which the main propeller must grow. The
ratio of propeller diameter to span rises from 0.35 to 0.47: the heavy design is not the light
design photographed from further away, and its propeller occupies almost half its span. Nothing
in the argument fails because of this — the propeller is the nose of the aircraft rather than an
appendage, and disc loading is what is being held — but the claim that the configuration keeps
its proportions applies to the quantities named here and not to every dimension. Much above
1000 kg, a single nose pair can no longer hold the disc loading and a second must be added.

**The buffer fraction is preserved** (3.6 % of MTOW at 50 kg, 4.0 % at 1000 kg), so the
mechanism by which Bill 3 is avoided does not degrade with size, and **the frame drag fraction is
preserved** because frontal and wing area both scale as L².

**Transition time does not scale, and this is the exception.** The rotating moment follows
M = Iα with I ∝ mL², so the moment needed to turn the aircraft in a fixed time grows much
faster than the aircraft. Scaling the light design's two-second rotation to 1000 kg would demand
221.5 kW from the tip propellers — 102 % of hover power, which is to say it is not available:

**Table 4.** Tip-propeller power required to rotate the heavy reference design.

| Rotation time | Tip-propeller power, 4 total | Fraction of hover power |
|---:|---:|---:|
| 2 s | 221.5 kW | 102 % |
| 3 s | 65.6 kW | 30 % |
| 4 s | 27.7 kW | 13 % |
| **5.1 s** | **13.4 kW** | **6 %** |

**The rule is that a larger aircraft turns more slowly.** The heavy design rotates in 5.1 s at
six percent of hover power — not a round number but the rotation time at which it holds the same
control margin the light design holds at two seconds (Section 3.17). The constraint is less costly
than it looks, because Section 3.15 shows a slower rotation loses *less* altitude: the scaling
penalty on transition time works with the penalty on control power rather than against it. The
classical objection to scaling a VTOL aircraft — hover power growing as L^3.5 against power
available as L³ — is removed on the hover side by fixing disc loading. It is not removed on the
transition side, and Table 4 is where it reappears: **the rotation is the one place in this
aircraft where the square–cube relation is still paid in full.**

## 3.10 Independent checks on the two assumed coefficients

Both coefficients carried through Sections 3.7 and 3.8 were assumed. Both have since been
computed, and the computations are reported in full in Supplementary S1. Neither replaces its
assumption in the figures above — those are quoted on one stated basis throughout — but each
bounds it, and the direction of each is stated here.

**Zero-lift drag.** A Reynolds-averaged solution of the wing and body gives C_D0 between
0.0120 and 0.0148, against the 0.0248 assumed. The spread is the turbulence closure:
0.01475 with Spalart–Allmaras and 0.01201 to 0.01253 with k-ω SST, eighteen percent apart
at matched wall resolution. **The assumption lies above the whole of that range**, so it is
conservative rather than optimistic. Two things S1 does not settle: the solutions are fully
turbulent, so the clean-surface figure of 0.0073 from the strip method is untested and the gap
between it and 0.0120–0.0148 is now the largest single uncertainty in the zero-lift drag; and
the wall-resolved SST case admits more than one stationary solution, two converged starts
settling 4.3 percent apart in the pressure component.

**Span efficiency.** A vortex-lattice solution gives an inviscid span efficiency of 0.990 for
the untwisted planform and 0.859 for the wing twisted to trim. Those are not the quantity the
drag build-up needs: an Oswald-type efficiency also carries the viscous drag due to lift. An
earlier version of this paper converted between them with a borrowed rule of 85 to 90 percent
and reported an implied value of 0.735 to 0.78. S1 computes the conversion instead, on this
planform, by calling the section solver at **each spanwise station's own local lift
coefficient** rather than at zero lift and integrating the profile drag across the span — the
two-dimensional-viscous-coupled-to-three-dimensional-circulation construction of the non-linear
vortex-lattice literature [40]. Before any number is taken from it, the strip decomposition is
checked against the solver it comes from: the strip loads reproduce the solver's own lift
coefficient to six decimal places.

| | Inviscid e | **Oswald e** | Ratio |
|---|---:|---:|---:|
| Untwisted planform | 0.990 | 0.931 | 0.940 |
| **Trimmed, −9° washout** | **0.859** | **0.817** | **0.951** |

**The borrowed rule was wrong in the favourable direction and the conclusion is unchanged in
the unfavourable one.** The viscous penalty is 5 to 6 percent rather than 10 to 15, but the
trimmed wing starts from 0.859, so the Oswald efficiency lands at **0.817 — below the assumed
0.85 by 3.9 percent**. At that value the cruise lift-to-drag ratio is **11.87 against 12.04**,
and the range figures of Section 3.8 are optimistic by the same 1.4 percent. Two limits belong
with the number: the vortex-lattice sections are symmetric, so a cambered section reaching the
same local lift coefficient at lower incidence would carry less drag and the figure is a
**lower bound**; and strip integration ignores sweep, which at 45° at the root is not a small
omission, though the alternative — simple-sweep theory — halves the profile drag, which is a
sign that the transformation does not apply to skin friction rather than a measure of the
uncertainty.

**What the vortex-lattice method is being asked for, and a bound on it that has no bound.**
Four results here come from a vortex-lattice solution: the span efficiency, the neutral point,
the twist required to trim, and the roll damping. Falkner separates the quantities the method
settles quickly — spanwise circulation, local aerodynamic centre — from those it does not, and
every quantity taken here is of the first kind [24]. But a published comparison on a
blended-wing-body of this class found the vortex-lattice lift coefficient low by **thirty to
thirty-eight percent** against RANS, and excluded the method from its trim analysis on that
basis [39]. The deviation there is nearly constant with incidence, which is the signature of a
multiplicative error in the magnitude of the loading rather than an error in its distribution —
and a factor common to lift and moment cancels in a ratio of derivatives. That argument depends
on the moment scaling with the lift, and the pitching-moment comparison in that source is
published with its values withheld. **The vortex-lattice results here therefore carry an
untested magnitude error of unknown size, bounded above by a published comparison on a similar
configuration, and every use made of them is of a kind a magnitude error *would not* disturb —
provided the moment scales with the lift by the same factor, which is exactly what cannot be
checked.**
**The magnitude question cannot be settled here, but its complement can be, and doing so moves
the exposure rather than removing it.** Whether the moment scales with the lift is untestable
without the withheld data. What is testable is the opposite question: *if the true loading
differs from the vortex-lattice loading by a redistribution across the span, how far do the
quantities taken from the solution move?* The twist distribution is perturbed by a half-sine in
the span fraction, which vanishes at root and tip, so root and tip incidence — and therefore tip
loading — are untouched and only the distribution between them shifts. The neutral point and the
trim twist are then re-solved at each shape. The perturbation is a redistribution and not a
rescaling, which is what makes it the complement of the error the source reports: across ±2° the
inviscid span efficiency moves by at most 1.6 percent from its 0.859.

| Shape perturbation | Neutral point | Δ from baseline | Trim twist | Δ from baseline |
|---|---:|---:|---:|---:|
| −2° (loading inboard) | 0.8646 m | −0.34 %MAC | −8.42° | +0.77° |
| −1° | 0.8658 m | −0.16 %MAC | −8.81° | +0.38° |
| **0, baseline** | **0.8668 m** | — | **−9.19°** | — |
| +1° | 0.8677 m | +0.14 %MAC | −9.57° | −0.37° |
| +2° (loading outboard) | 0.8685 m | +0.26 %MAC | −9.93° | −0.74° |

The baseline reproduces the chain it is testing: the trim twist of **−9.19°** at **10.24°** of
incidence is the nine degrees of washout reported above, and an independent solver in the
repository — bisecting incidence rather than solving the linearised system — returns the same
incidence to 0.01° with a residual pitching moment of 3 × 10⁻⁵.

**Two things follow, and the second was not expected.** Per degree of mid-span redistribution the
neutral point moves **0.15 %MAC** and the trim twist moves **0.38°**. Against the thresholds that
would force the trim chain to be recomputed — 5 %MAC and one degree — the neutral point would need
a redistribution of **33 degrees** and the trim twist one of **2.6 degrees**. **The binding
constraint is the trim twist and not the neutral point, by a factor of thirteen.** The static
margin, which is the quantity the cancellation argument above was constructed to defend, is the
robust half of the chain; the trim twist, which that argument never addressed, is what a
redistribution disturbs first.

This does not measure the redistribution a RANS solution would find, and it is not offered as
one. It converts an exposure that had no bound into a transfer coefficient: a reader holding an
estimate of the redistribution can multiply. Section 4 keeps this among the open items for that
reason, with its location changed.

## 3.11 A component build-up of the mass budget

The sizing above assumes an empty-mass fraction rather than deriving one. Supplementary S2
builds the 50 kg design's mass item by item — structure from wetted area and an assumed shell
areal density, tip frames sized by a vertical landing case, propulsion, energy, avionics and
systems — and reports the break-even value of every assumption in it.

**The build-up closes, and it closes on one number.** The total is 11.88 kg against a 14.08 kg
allowance, leaving 2.2 kg unallocated. It closes on the condition that the average structural
areal density does not exceed **1.78 kg m⁻²**, against the 1.5 assumed; at 1.78 the payload is
gone. A doctoral study of unmanned-aircraft sizing reports 1.05 kg m⁻² for a small UAV's
monolithic composite fuselage shell supported by an internal structure [50], which places the
assumption inside the range small composite airframes are built to without establishing that
this airframe reaches it — that shell is carried by an internal structure, while this one is
the wing and carries flight loads directly.

**The build-up came in lighter than the target, and that is a warning rather than a result.**
Paper aircraft are habitually lighter than the aircraft that get built. What S2 does not
contain is buckling, torsion, local load introduction, aeroelastic sizing, fasteners, adhesive,
paint, or the mass of anything the design has not yet specified — and the 2.2 kg of margin is
what all of those must fit into. Section 4.4 states the item as bounded from below rather than
demonstrated.

The transition between vertical and horizontal flight is the manoeuvre on which
tail-sitters have historically been judged, and it is the part of this configuration
that most deserves scrutiny. This section describes the flight profile, states the
equations that govern the transition, and reports a simulation of it. One result
contradicts a widely-assumed relationship and is presented as such.

## 3.12 The five phases

**Stance.** The aircraft rests on five points — the four lower ends of the tip frames
and the aft end of the centre keel — with its longitudinal axis vertical. No launch
equipment is present, and the aircraft is in its own storage attitude.

**Vertical take-off.** The nose pair spools to a thrust exceeding weight and the
aircraft rises vertically. Attitude is held by the four tip pairs. This is the
highest-power phase of the flight and the shortest.

**Transition.** The aircraft rotates from vertical to horizontal while accelerating,
until the wing carries the weight. Treated in detail below.

**Cruise.** The aircraft flies as a tailless blended-wing body. The nose pair is now
the cruise propulsor at its design point. The tip pairs provide pitch and yaw, and the
lower-surface strip provides roll.

**Landing.** The reverse of transition, followed by a vertical descent onto the five
contact points. Section 3.16 notes what is and is not analysed here.

Figure 9 shows the five phases in sequence. Nothing on the aircraft rotates relative to
the aircraft at any point in it.

## 3.13 Why the transition begins in the easiest condition

A common objection to tail-sitter transition is that the aircraft must fight the
airflow while rotating. For a transition that begins in hover, it does not. At the
start of the manoeuvre the airspeed is zero, so the free-stream dynamic pressure

    q = ½ρV²

is zero, and with it every aerodynamic moment that would resist the rotation. The
aircraft is not turning against the air; it is turning in still air and then meeting
the air as it accelerates.

The consequence is that the difficult part of the transition is not its beginning but
its middle, where the airspeed has grown enough for aerodynamic moments to matter but
the wing is not yet carrying the weight. The control authority requirement is set
there, not at the start.

## 3.14 The thrust singularity that is never reached

Consider the aircraft at an angle θ from the vertical, and suppose for a moment that it
must hold altitude with thrust alone. Vertical equilibrium then requires

    T cos θ = W        →        T = W / cos θ

which diverges as θ approaches ninety degrees. Read literally, this says a tail-sitter
cannot complete a transition, and the expression is sometimes quoted to that effect.

The expression is correct and the conclusion drawn from it is not, because the premise
is false. The aircraft does not hold altitude with thrust alone. Vertical support is

    T cos θ + L = W,        L = ½ρV²S C_L

and V is not zero during the rotation — it is growing, because the horizontal component
T sin θ is accelerating the aircraft. The horizontal acceleration, in the same
idealisation, is

    a = g tan θ

so the very rotation that reduces the vertical component of thrust is what generates
the airspeed that replaces it. The singularity is never approached because the wing
arrives first.

This is the central mechanism of the manoeuvre, and it also explains the result of the
next subsection.

## 3.15 Transition time: slower is better

The transition was simulated as a two-degree-of-freedom point mass. The body angle is driven
from zero to ninety degrees over a rotation time t_r; thrust acts along the body axis, lift
perpendicular to the velocity vector and drag opposite to it; the lift curve is linear to stall
and a flat-plate relation beyond it. Altitude loss is the lowest point of the trajectory
relative to the entry altitude. Figure 10a plots both reference designs at four
thrust-to-weight ratios.

**The ratio the aircraft actually has must be established first, and it is not a free choice.**
Section 2.12 sizes hover power at thrust equal to weight, so the 10.9 kW of Section 3.7 buys
T/W = 1.00 and nothing more; the same is true of the 216.2 kW of Section 3.8. The only other
source of vertical thrust on this aircraft is the tip pairs, and during the rotation they are
occupied producing the rotation itself. On the bang-bang profile the upper pairs run at full
thrust and the lower pairs at zero, which is the M = 2TL of Section 2.9 — and the two upper
pairs still push upward. That fixes the ratio available *during* a full-authority rotation at
**1.066 for the light design and 1.041 for the heavy one**, and it is the ratio the tables below
use. Giving up rotation authority buys a little more, to 1.132 and 1.082 with none retained;
Supplementary S2 gives the trade. An earlier version of this section assumed T/W = 1.2, which
the installed power does not supply at any setting, and the tables have been recomputed.

| t_r | Light, 50 kg | | t_r | Heavy, 1000 kg |
|---:|---:|---|---:|---:|
| 1 s | −18.2 m | | 2 s | −31.0 m |
| 2 s | −14.7 m | | 3 s | −26.9 m |
| 3 s | −11.2 m | | 4 s | −22.7 m |
| 4 s | −4.9 m | | 5.1 s | −13.1 m |

**The relationship is monotonic in the direction opposite to the one usually assumed.** It is
frequently supposed that a tail-sitter should rotate as fast as possible, on the reasoning that
it is unsupported during the rotation and therefore falls for a time t_r, giving a loss
proportional to t_r². **That reasoning is wrong, and the error is in its premise:** the aircraft
is not unsupported. Vertical support is T cos θ + L, and a slow rotation keeps cos θ large during
exactly the interval in which speed, and therefore lift, is being built. A fast rotation
collapses cos θ before there is any lift to replace it, and the aircraft falls precisely because
it hurried.

The practical consequence is a simplification rather than a trade. The control *moment* required
to rotate in time t_r scales as 1/t_r² and the control *power* as 1/t_r³ — Table 4 of Section 3.9
is the second of these, and its entries are constant to within a third of a percent when
multiplied by t_r³ — so a slow rotation is cheap in authority and cheaper still in power; and
altitude loss also falls with t_r. **All of these point the same way**, so there is no optimum
transition time to be found between competing penalties — the rotation time is set by what the
actuator can do, not by a balance, and Section 3.17 shows that is where both reference times come
from.

**Entering the rotation while still climbing removes the penalty entirely in this model**, and
that survives the correction to thrust-to-weight above. At an entry climb of 5 m s⁻¹ the altitude
loss is zero at both reference rotation times — 2 s light and 5.1 s heavy — and remains zero at
every ratio from 1.066 down to 1.00, which is to say the result does not depend on the tip pairs
contributing any lift at all once the climb has been acquired.

**It does not survive the addition of rotational dynamics, and that is the sharpest limitation of
this result.** The simulation above drives the body angle kinematically: the aircraft is assumed
to rotate, and the moment producing the rotation does not appear. Section 3.17 asks separately
whether the moment is available. The two have now been solved together — three degrees of freedom,
a finite control moment, and the same trajectory model otherwise — and with **zero aerodynamic
pitching moment**, which isolates the rotational dynamics alone, the light design loses **5.4 m**
at its reference condition where the kinematic model reports zero. The loss is not a tracking
artefact: it is unchanged across the linear, bang-bang and smooth reference profiles, it appears
without the control moment ever saturating, and it grows rather than vanishes as the controller
gains are raised, reaching 17 m at gains high enough to track the reference almost exactly. What
the kinematic model omits is not the difficulty of turning the aircraft but the trajectory the
aircraft flies while it is being turned.

With a borrowed pitching moment the outcome depends on which moment is borrowed, and the spread is
wide enough that no number from it is reportable: some models complete the rotation, others
saturate the tip pairs, and others tumble. That spread is itself the finding, and it is the same
finding Section 4 states from the other direction — the transition rests on a coefficient no
current method predicts reliably. Supplementary S4 gives the sweep. **Two cautions belong with it:
the model carries no aerodynamic pitch damping, and its controller is a fixed-gain regulator
rather than a designed one, so the borrowed-moment rows bound nothing.** The zero-moment row does
not depend on either and is the result carried forward.

**Acquiring the climb is where the correction is paid.** The aircraft reaches transition altitude
by climbing, so it need not stop and hover first, but the excess thrust available to build that
climb is now 0.132 g rather than the 0.2 g an earlier version claimed, and only if no rotation
authority is held in reserve; with full authority retained it is 0.066 g. Five metres per second
is therefore reached in 3.9 s over 9.6 m at best, and 7.7 s over 19.3 m at worst, against the
2.6 s and 6.4 m previously stated. The energy involved is unchanged and remains negligible —
625 J against a fuel energy of 103 kWh — so what the correction costs is time and height, not
range. **The reference profile is therefore still to enter the rotation at 5 m s⁻¹ of climb**,
with the acquisition charged at the achievable rate.

Two consequences follow that the earlier tables hid. Starting the rotation from rest is worse
than reported — the light design loses 14.7 m at its own two seconds rather than 9.1 m, and the
heavy design 13.1 m at 5.1 s rather than none — so the climb entry is not a convenience but a
requirement. And the tip pairs, introduced in Section 2.9 as moment producers and charged in
Section 3.5 for their mass and drag, turn out to carry the take-off thrust margin as well: an
aircraft whose primary propulsor is sized at thrust equal to weight leaves the ground on them.
That is a second duty for hardware bought for the first, which is the kind of economy this
configuration is built on — but it is also a dependency, and it is a harder one than it looks,
because the margin and the attitude authority are drawn from the same four propellers and cannot
both be had in full. Section 4 records it as an open item.

**The test is a lower bound.** A point mass carries no rotational dynamics, no aerodynamic
pitching moment and no control-power limit; Section 3.17 supplies the rotational budget that this
model omits, and Section 4 states what neither supplies.

## 3.16 Landing

Landing reverses the sequence: the aircraft decelerates, rotates nose-up, and descends
vertically onto its five contact points. Two things should be said about it plainly.

The first is that the historical objection to this manoeuvre does not apply. The XFY-1
was cancelled because its pilot had to judge a backwards vertical descent by looking
over his shoulder. There is no pilot here, and height above ground is a sensor
measurement rather than a human estimate.

The second is that the vertical descent itself has not been analysed in this study. A
rotor descending into its own wake can enter the vortex ring state, in which thrust
becomes erratic and increasing power makes matters worse. Whether the descent profile
of this configuration enters that region, and at what rate of descent, is an open
question. It is listed in Section 4 rather than answered here.

## 3.17 Whether there is enough authority to rotate, and whether it trims

Rotating the airframe through ninety degrees is the manoeuvre this configuration must perform
with four small propellers and no control surfaces. Supplementary S4 carries the full budget —
inertia derivation, rotation profiles, centre-of-gravity window, twist sweep and the measured
section evidence. This section states what it returns.

**The rotation closes at the actuator limit rather than clear of it.** The pitch inertia
derived from the component build-up is 9.81 kg·m² for the light design and 2 503 kg·m² for the
heavy one. On the cheapest rotation profile the tip propellers carry the manoeuvre with a margin
of **1.49** at the light design point and **1.57** at the heavy one; on a smoothly commanded
profile the margins fall to 0.99 and 1.05. The reference rotation times — two seconds light,
5.1 seconds heavy — are therefore lower bounds set by the actuator, not comfortable choices,
and the margin narrows with size.

**The light figure rests on a tip thrust the design tables assert rather than derive, and on the
conservative basis it is thinner still.** The 16.2 N quoted per pair implies a figure of merit of
0.702, against the 0.599 used for hover everywhere else. Recomputing at 0.599 with a fifteen
percent coaxial interference loss gives 12.4 N, an available moment of 17.6 N·m, and margins of
**1.14 bang-bang and 0.76 smooth** — which is to say the light design closes on the cheapest
profile and does not close on a smooth one at two seconds. The heavy design was computed on the
conservative basis from the outset. Supplementary S4 gives both, and the honest reading is that
the rotation is sized by the actuator under either basis and has no margin to give under the
stricter one.

**Resolving the requirement along the trajectory changed the question rather than merely
quantifying it.** The aircraft does not reach ninety degrees of incidence: the body rotates
through ninety, but the relative wind rotates with it, and **peak incidence is 17.5° for the
light design entering in a 5 m s⁻¹ climb and 21.6° entering from level hover**. The
high-incidence part happens at low dynamic pressure, where the margin tolerates a pitching-moment
coefficient of 0.205; the tight part is the *end* of the rotation, where incidence is small and
speed is high, and the budget there is 0.050. **The demanding case is not the post-stall middle
but the attached-flow end**, which makes it a trim question rather than a stall question.

One mechanism was omitted and including it improves the case. The inboard half of the wing lies
in the nose propeller's slipstream, where the local flow is faster and more axial, so the
effective incidence there is lower than the geometric one. Applying the slipstream relation used
in the tail-sitter literature [23] gives **four to eight degrees effective against seventeen to
twenty-two geometric**: half the wing is not post-stall at the moment of peak incidence. The
measurement still owed concerns the outboard half.

**Static stability is shown, and the trim chain closes by twist.** A vortex-lattice solution
places the neutral point at 0.859 m from the root leading edge — 34.4 percent of mean
aerodynamic chord — and the packaging centre of gravity at 80.2 percent of root chord gives a
**static margin of +12.5 percent of mean aerodynamic chord**, with a pitching moment of 0.056 to
be balanced at the cruise lift coefficient. Two published benchmarks place that window
favourably: a blended-wing UAV of this class reports its own margin of 0.081 as "marginally
outside the typical range for static longitudinal stability", given as 0.1 to 0.3, and its
C_m_α of −0.086 per radian against a typical −0.3 to −1.5 [41]. This configuration sits inside
both at 0.125 and −0.48 per radian.

**Reflex does not supply the 0.056, and this is now a measured statement rather than an
inference.** Nine reflexed and low-moment sections have been tested in tunnels that measure
pitching moment. Exactly one returns a positive value — NACA 2R212 at **+0.004** [17], one
fourteenth of what is needed. The three 1930s reflexed sections whose mean lines were shaped
from thin-aerofoil theory to give *zero* quarter-chord moment measure "practically zero", from
−0.001 to −0.007 [45]; the four sections of the NACA 4400R family were designed to a target of
**−0.03** and the report states that "the design pitching-moment coefficient was realized" [46].
**Reflex, as actually built and measured, is a device for removing negative pitching moment
rather than for producing positive pitching moment.** Two costs are measured with it, and both
bear on a tail-sitter: maximum lift falls by about twelve percent in the first family and ten
percent in the second — and maximum lift is what a tail-sitter needs at the high-incidence end
of transition. A flying tail-sitter shows where the positive moment actually comes from: it uses
a symmetric section, and "the upward trim of elevons makes the symmetric airfoil to have
reflexed camber line", producing the positive moment at the aerodynamic centre [51]. The reflex
that trims that aircraft is a deflected control surface held permanently out of line, not a
property of its section.

**Nine degrees of tip washout trims this aircraft at cruise with no camber at all**, and the
vortex-lattice model computes it directly because the mechanism is geometric rather than
sectional: on a swept wing the tips lie well aft, so negative tip incidence produces a nose-up
moment about the centre of gravity. The price is a span efficiency of 0.865 instead of 0.993 and
a cruise lift-to-drag ratio of 12.11 instead of 12.65 — **4.3 percent of cruise efficiency, paid
to be tailless**, and entered in the ledger of Section 3.5 as its fifth item. The reflex route
is not free either: a blended-wing UAV trimming by reflex rather than twist records that
carrying reflex over a wide span "is not conducive to the improvement of overall lift-to-drag
performance" [44]. **Both roads to trim on a tailless configuration cost cruise efficiency**,
which is the reading Section 3.5 places on the 4.3 percent: it is the price of having no tail,
not the price of choosing the wrong way to do without one.

The twist earns its cost three times over. It closes the trim chain; on a swept planform it
delays tip stall, which on a tailless aircraft matters more than usual because a tip stall moves
the centre of pressure forward and there is no tail with which to argue; and it inverts the
stall sequence behind a blended-wing pitch-break. That third mechanism was found late and does
not depend on aspect ratio: in a blended-wing-body analysed by both a low-fidelity method and
RANS, the moment prediction departs above eight degrees because "the main wing stalls before the
main body, causing the BWB to pitch-up" [39]. Washout makes the root stall first, and on a
blended wing the root is the body.

**The pitching moment through transition remains this study's largest open item, and the reason
nobody computes it has been measured.** A small blended-wing-body UAV was analysed by RANS and
then tested in a wind tunnel at a Reynolds number of 2.0 × 10⁶: from −6° to 10° of incidence
"both the aerodynamic force values and the variation trends are in quite good agreement"; from
10° to 26° they "show remarkable differences between the numerical and experimental results"
[44]. The same boundary appears at lower fidelity — a vortex-lattice solution of this class of
configuration departs above eight degrees [39] — and the incidences this aircraft passes through
lie inside that band. **Three methods of three fidelities fail at the same place, and the
highest of them fails against measurement.** The item therefore belongs to measurement rather
than to computation, and Section 4 asks for it as measurement. The same tests found the
blended-wing configuration to have "soft-stall performance", which is the benign end of the
range the pitch-up literature describes.

The field does not have this term either. A transition-optimisation study with outdoor flight
trials carries **no pitching-moment term at all** [28]; a second carries a linear one and
flight-tested the question this configuration asks, reporting that without elevons its
tail-sitter had "a well-controlled attitude response during hovering and transition" but that
manoeuvres in level flight caused "an oscillatory attitude response" with "motor saturations
observed", attributed to "the increased aerodynamic moment but decreased motor thrust at
high-speed level flight" [29]. A survey records the same outcome for a separate vehicle: "able
to achieve transition to forward flight, but they had poor control over the vehicle once in
forward flight" [30]. A third carries a nonlinear C_m(α) but borrows the curve and closes the
remaining discrepancy with an adaptive law [42]. **Every one of them obtains the transition
aerodynamics by borrowing, fitting or adapting, and none by measuring the vehicle it flies.**
Two independent programmes, different vehicles, the same division — transition passed, forward
flight difficult — and that is the same structural tension this section derives from the moment
budget: the tight case is the end of the rotation and beyond, where aerodynamic moment grows as
V² while propeller thrust falls.
