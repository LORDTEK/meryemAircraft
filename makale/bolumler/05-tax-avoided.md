# 5. The architectural tax, audited bill by bill

Section 3 identified three bills and argued that they are one quantity paid in three
currencies. Section 4 described a configuration built to satisfy the zero-bill
condition. This section audits that claim bill by bill, and then states, in the same
detail, what the configuration does pay. The second half is not a concession appended
for balance. An architecture that claimed to pay nothing would be describing a
different aircraft from the one in Section 4.

## 5.1 Bill 1 — mass: the charge does not arise

There is no second propulsion group. The nose pair that lifts the aircraft off the
ground is the same pair, in the same orientation, at the same station, that propels it
in cruise. Nothing is carried unused.

This is the whole of the argument, and its brevity is the point. The bill was never a
consequence of poor design in lift-plus-cruise aircraft; it was a consequence of
counting two propulsion systems where the mission needs one. A configuration that
counts one does not reduce the bill — it does not generate it.

The tip pairs are a genuine addition and are accounted for in Section 5.4. They are not
a second propulsion group: they are sized for moments rather than for weight, and in
the vertical phase they draw 1.34 kW against the nose pair's 10.9 kW, which is twelve
percent.

## 5.2 Bill 2 — drag: reduced, not removed

In cruise there is no stopped rotor in the airstream, because there is no rotor that stops. The
nose pair is the cruise propulsor and runs at its design condition throughout. The quarter of
lift-to-drag ratio that Section 3.3 reports as the measured cost of installing hover hardware is
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
| turning at zero shaft load, blades at low incidence | 0.0003 – 0.0008 | 1 – 3 % |
| stopped edge-on, at a chosen azimuth | 0.0008 | 3 % |
| **stopped broadside, azimuth uncontrolled** | **0.015 – 0.018** | **61 – 74 %** |

**The difference between the first and third rows is the difference between a configuration that
works and one that does not**, and it is robust to the coefficients assumed, because the two
states differ by a factor of thirty. The second row shows why stopping them is survivable only
if azimuth is controlled — which is the indexing mechanism this section has just claimed the
configuration does not need.

**The resolution costs nothing, and it is a control state rather than hardware.** A fixed-pitch
propeller left free settles at the advance ratio where net shaft torque is zero: inner sections
drive, outer sections retard, and they balance. The shaft then does no work, so the motor
neither drives nor brakes and the electrical cost is controller standby draw and bearing losses.
The blades sit at low incidence with attached flow, which is the first row. **The tip rotors are
therefore held in cruise at the zero-shaft-torque condition — neither stopped nor driven** — and
this is the state assumed throughout Section 6. It is worth naming because both neighbouring
states are wrong: driven, they cost propulsive power; stopped without azimuth control, they cost
most of the aircraft's zero-lift drag.

What Bill 2 *is* paid, and this is why the heading says reduced rather than removed, is the tip
frames. They are structure in the airstream that a conventional aircraft does not carry, and at
the light design point they contribute ΔC_D0 = 0.0043 — **about twelve percent of total cruise
drag**, and seventeen percent of the zero-lift drag the sizing assumes. Both denominators appear
in this paper and each is named where it is used. That is the honest figure and it is carried in
the ledger of Section 5.4.

**The fairing on those frames is not only a drag measure.** The frames are the only surfaces
standing perpendicular to the wing plane, and the planform supplies no directional stability at
all, so the fairing is also the vertical surface that provides it. Sized against the criterion
the tailless literature recommends — C_n_β greater than 0.001 per degree [19] — the chord
required over the combined frame length is 39 mm, against the 50 to 70 mm a 20 mm faired strut
carries in any case. The two requirements do not conflict, and the directional one is the looser;
but the frame cross-section is now constrained from two directions, and a selection made on drag
alone would be made on half the evidence.

## 5.3 Bill 3 — power system sizing: avoided for the engine, not for the electrical path

The series-hybrid arrangement of Section 4.3 breaks the link that forces the power
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

**What is not avoided, and the section heading says so.** The bill is defined in Section 3
as a *continuous* power system sized by the hover peak, and it is the engine and its fuel
consumption that the buffer releases from that condition. The electrical path is not
released: the nose motor and the power electronics must still pass the full 10.9 kW, and
the component build-up of Section 6.7 shows them as 2.73 kg and 0.61 kg against 2.60 kg of
engine and generator — that is, the hover-sized electrical machine is the single largest
item in the propulsion chain. The saving is real and it is the engine's, but a reader
should not take it as an aircraft on which nothing is sized by hover. The buffer itself
carries a further condition, given in Section 6.7: it is specified by power rather than
energy, at **5.63 kW kg⁻¹** to hover and 6.48 to leave the ground, which is a demanding cell
requirement and not a free parameter. Section 8.2 measures it against what has been flown.

## 5.4 What is paid

The honest ledger has five entries.

**The control propellers.** Four pairs, their motors, mounts and wiring exist only to
produce moments. In the vertical phase they draw twelve percent of the power the nose
pair draws. This is the configuration's substitute for elevons and a rudder, and it is
not free — it is merely cheaper than a second lift system, and it does not sit in the
cruise airstream in the way a lift rotor does.

**The tip frames.** As established in Section 5.2, of the order of twelve percent of
cruise drag, conditional on being faired. This is the largest single payment the
configuration makes, and it is the price of the moment arm, the propeller mounting and
the landing structure combined into one member.

**The roll strip.** The one moving aerodynamic device on the aircraft. Its cost when
retracted is a surface discontinuity; when deployed it is a drag device by construction,
but it is deployed only while a roll is being commanded.

**The twist needed to trim.** Section 7.6 finds that the configuration trims at cruise with
nine degrees of tip washout, reflex being an order of magnitude short of the moment required.
Washout is not free: it costs span efficiency, and the cruise lift-to-drag ratio falls from
12.65 to 12.11 — **4.3 percent**. This entry was missing from earlier versions of this ledger,
and it is worth being precise about what it is a payment for. It is not one of the three bills
of Section 3, which are charged for having a hover capability; it is charged for being
tailless, and a tailed aircraft of the same architecture would not pay it. It belongs here
because this configuration is tailless, and because a ledger that omitted it would be
flattering rather than honest.

**The transition manoeuvre.** The aircraft must rotate through ninety degrees, and the
rotation costs time, horizontal displacement and control power. Section 7 treats it in
full and shows that the altitude cost, which is the one usually assumed to dominate, can
be brought to zero: rotating slowly and entering the rotation while still climbing
removes it entirely at both design points. What remains is not free — the manoeuvre
occupies seconds during which the aircraft is neither hovering nor cruising — but it is
smaller than the literature on tail-sitters would suggest, and it is the one payment on
this list that gets *cheaper* the less it is hurried.

Set against the bills of Section 3, the ledger is favourable but not empty. The
configuration does not escape physics; it declines a particular trade. What it pays
instead is smaller, and — this is the part that matters for scaling — it does not grow
faster than the aircraft.


## 5.5 A comparative sizing of three architectures

Supplementary S6 sizes three architectures against the same mission — this tail-sitter, a
lift-plus-cruise aircraft, and a tilt-rotor — under three different sizing contracts: fixed fuel
fraction, fixed fuel mass, and fixed maximum take-off mass with fixed payload. One set of
equations serves all three, and every coefficient in it is back-solved from the light reference
design of Section 6.2 rather than assumed. Mission, wing loading, disc loading, structural
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
but is a comparison of other people's aircraft, not of this sizing. Section 8 states the
comparison as conditional on both asymmetries.
