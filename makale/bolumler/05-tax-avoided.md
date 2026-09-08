# 5. The architectural tax, audited bill by bill

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

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

In cruise there is no stopped rotor in the airstream, because there is no rotor that
stops. The nose pair is the cruise propulsor and runs at its design condition
throughout. The quarter of lift-to-drag ratio that Section 3.3 reports as the measured cost of
installing hover hardware is not incurred here — not reduced, not mitigated, but absent,
because the hardware that causes it does not exist in this configuration. Nor is there a retraction mechanism,
so the transfer of Bill 2 into Bill 1 identified in Section 3.3 does not occur either.

It is worth noting what this avoidance also spares. Where lift rotors are retained,
keeping their drag small depends on stopping them at a favourable azimuth, which needs
an indexing mechanism; where they are stowed, it needs a retraction mechanism. Both are
mass, and both are failure modes. A configuration with no rotor to stop needs neither.

The word "mostly" in this heading is deliberate. The configuration does place hardware
in the cruise airstream: the four tip frames and the four control propellers they
carry. That is a real payment against Bill 2, and quantifying it produced the single
most consequential sizing result in this study.

The frames present 2.84 m of exposed length to the flow, oriented perpendicular to it,
for the light reference design. At the cruise dynamic pressure of 551 Pa, against a
total cruise drag of 38.6 N, their contribution depends almost entirely on their
cross-section:

| Frame cross-section | C_D | Share of total cruise drag |
|---|---:|---:|
| Circular tube, 20 mm | 1.15 | **93 %** |
| Faired strut, 20 mm | 0.15 | 12 % |
| Well-faired strut, 20 mm | 0.08 | 6.5 % |

Left as circular tubing, the frames alone would produce very nearly as much drag as the
entire rest of the aircraft, and the configuration's central claim would collapse. The
result is therefore not an observation but a requirement: **the tip frames must be
faired.** With a faired section the payment is real and affordable — of the order of
twelve percent of cruise drag — and it is reported here as a cost rather than absorbed
silently.

One property of this cost is worth noting. The frame frontal area scales with the
square of length, and so does the wing area, so under geometric scaling at equal cruise
dynamic pressure the fraction is preserved. This bill does not grow with the aircraft.

The drag coefficients used here are representative values for circular and faired sections at the relevant Reynolds number, and the frame cross-section has not yet been selected. The requirement to fair the frames is robust to that choice — the difference between a circular tube and a faired strut is not a matter of coefficient precision — but the twelve-percent figure is an estimate.

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
mass. The heavy reference design sits on the same line: 39.2 kW electrical in cruise,
54.3 kW engine, 216.2 kW hover, 40 kg of battery at 4.0 percent of MTOW.

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
energy, at 4.6 kW kg⁻¹, which is a demanding cell requirement and not a free parameter.

## 5.4 What is paid

The honest ledger has four entries.

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

Sections 5.1 to 5.4 argue that a particular configuration declines a particular trade.
That argument is made against the general statement of the tax in Section 3, not against
any competing aircraft, and an argument of that shape has a known weakness: it can be
right about the mechanism and still be wrong about the outcome, because a rival
architecture may pay the bills and recover more than it pays. The claim is therefore
tested here by sizing the same mission three ways.

**Method.** One set of equations is used for all three, and they are the equations of
Section 6.1 — closed-loop mass, hover power from momentum theory, and a Breguet-type
range:

$$\mathrm{MTOW} = \frac{m_\text{payload}}{1 - f_\text{empty} - f_\text{fuel}}, \qquad
P_\text{hover} = \frac{W^{3/2}}{\eta_h \sqrt{2\rho A}}, \qquad
R = \frac{f_\text{fuel}\, E^{*} \eta_\text{chain}}{g}\,\frac{L}{D}$$

The propulsion-chain mass is not a fixed fraction. It is split into a part proportional
to take-off mass and a part proportional to installed power, because a fixed fraction
would make the third bill invisible by construction. Installed power depends on take-off
mass and take-off mass depends on installed power, so the system is closed by fixed-point
iteration.

**Calibration.** Every coefficient is back-solved from the light reference design of
Section 6.2 rather than assumed: a hover figure of merit of 0.599 from 10.9 kW at 50 kg,
a cruise propulsive efficiency of 0.721 from 1.7 kW at L/D 12, an engine rating margin of
1.53, and a power-independent propulsion fraction of 0.108 given an assumed 1.0 kW kg⁻¹
for a small engine and generator. The model must then reproduce the design it was
calibrated from, and it does — take-off mass, propulsion fraction, engine rating,
lift-to-drag ratio, range and hover power all within 0.1 percent. Run at the heavy design
point without retuning, it predicts 1 037 kg against 1 000 kg and 1 813 km against
1 814 km; the one term that does not carry across is the engine rating margin, discussed
in Section 8.13.

**What differs between the architectures.** Mission, wing loading, disc loading, fuel
fraction, structural fraction, avionics fraction and energy chain are held identical.
Only three things change, and each is either a measurement quoted elsewhere in this paper
or an openly swept parameter:

| | Cruise L/D multiplier | Architecture-specific mass | Source |
|---|---|---|---|
| A — tail-sitter | 1 / 1.12 | — | Section 5.2, tip-frame drag |
| B — lift + cruise | 13 / 17 | second propulsion group, swept | Section 3.3, wind tunnel |
| C — tilt | 1.00 | tilt mechanism, swept | **assumed, not measured** |

**Result.** With the same buffered series-hybrid power system given to all three — which
neutralises the third bill, and does so against the proposed configuration:

| | Empty fraction | MTOW | L/D | Hover power | Range |
|---|---:|---:|---:|---:|---:|
| A — tail-sitter | 0.580 | 50.0 kg | 12.00 | 10.9 kW | 1 600 km |
| B — lift + cruise | 0.689 | 86.0 kg | 10.28 | 18.7 kW | 1 370 km |
| C — tilt | 0.624 | 60.3 kg | 13.44 | 13.1 kW | 1 792 km |

Against lift-plus-cruise the result is unambiguous and it is driven by measurement: the
same mission closes at seventy-two percent higher take-off mass and fourteen percent
lower range, and the drag term behind it is a wind-tunnel result, not an assumption.
Giving the lift-plus-cruise layout the additional structural fraction that distributed
lift is generally held to require makes its mass worse still — 117 kg at four additional
points of structure — without changing its range at all, so the comparison as tabulated
is generous to it rather than the reverse.

**Against tilt the table above goes the other way, and both reasons must be stated
plainly.** The tilting layout closes lighter than lift-plus-cruise and cruises twelve
percent further than the proposed configuration. Neither part of that outcome is a
finding. The first reason is the multiplier of 1.00, which credits the tilting layout
with paying no cruise drag at all for its nacelles, pivots, actuators and hover-pitched
blades. The second is subtler and belongs to the sizing rule rather than to any
architecture.

Range in the equation above contains the fuel fraction and not the fuel mass. Holding the
fraction fixed across architectures — the natural choice, and the one the table uses —
lets the heavier aircraft carry proportionally more fuel, which removes the mass bill
from the range column entirely. The general form is

$$R = \frac{E^{*}\eta_\text{chain}}{g}\,\frac{L}{D}\,\frac{m_\text{fuel}}{\mathrm{MTOW}}$$

so that a fixed fraction makes range independent of take-off mass, a fixed fuel *mass*
makes it inversely proportional to take-off mass, and a fixed take-off mass with a fixed
payload leaves fuel as the residual.

These are three different questions, and which one is the right question depends on what is
being procured: a mission, a fuel load, or a vehicle class. The mission stated in Section
6.2 — 13 kg of payload over roughly 1600 km, with take-off mass free to close where it will
— is closest to the first, which is also the only rule under which the tilting layout
leads, and leads only because its mechanism was credited as aerodynamically free. Reporting
that column on its own would restate the credit as a conclusion. **All three are therefore
given equal standing, and no result from this section should be quoted without the rule it
was computed under.** The tilting layout keeps its zero cruise-drag credit throughout:

| Range relative to the tail-sitter | Fixed fuel fraction | Fixed fuel mass | Fixed MTOW and payload |
|---|---:|---:|---:|
| B — lift + cruise | −14.4 % | −36.5 % | −72.6 % |
| C — tilt | +12.0 % | +0.2 % | −19.1 % |

Against lift-plus-cruise the conclusion is the same under every rule and grows more
emphatic as the rule tightens. Against tilt it is not: the twelve percent advantage
becomes a tie when the two aircraft carry the same fuel, and a nineteen percent deficit
when they are the same take-off mass carrying the same payload — because at 50 kg the
tilting layout's empty fraction leaves 0.116 for fuel where the proposed configuration
leaves 0.160. Sweeping the cruise-drag multiplier across all three rules gives the full
picture:

| Tilt cruise-drag multiplier | Fixed fuel fraction | Fixed fuel mass | Fixed MTOW and payload |
|---|---:|---:|---:|
| 1.00 | +12.0 % | +0.2 % | −19.1 % |
| 0.96 | +7.5 % | −4.3 % | −23.6 % |
| 0.92 | +3.0 % | −8.9 % | −28.2 % |
| 0.88 | −1.4 % | −13.4 % | −32.7 % |

Of the twelve cells, the tilting layout leads in three, all of them in the first column
and all of them requiring its mechanism to be aerodynamically free. Under the fixed
fraction the sign changes at a multiplier of approximately 0.89, which is to two decimal
places the penalty the proposed configuration charges itself for its own tip frames,
1/1.12 = 0.893. **The comparison therefore supports a conditional and not a ranking:
under a fixed fuel-fraction rule, and with the tilt mechanism assumed aerodynamically
free, the tilting layout cruises further; under equal fuel mass or equal take-off mass
that advantage disappears.** No claim of superiority over the tilting family is made here
in either direction.

Two smaller points belong with that disclosure. The cruise propulsive efficiency is also
shared with the tilting layout, which is generous, since a blade pitched for hover is not
the blade one would choose for cruise; but range does not contain propulsive efficiency,
so the generosity falls entirely on mass — 60.3 kg becomes 62.7 kg at a fifteen percent
efficiency penalty — and none of it on the range comparison. And a second table, in which
each architecture is given its own power system with no buffer, is not reported as a fair
comparison and should not be read as one: a real lift-plus-cruise aircraft hovers on
batteries rather than on an engine sized for hover, so that table is a bounding case for
an unbuffered series hybrid and not a description of the architecture it is labelled
with.

**What this comparison does and does not support.** It supports the claim that the
proposed configuration avoids the mass and drag bills that a separate lift system pays,
and it supports it with the paper's own measurements rather than by assertion. It does
not support a claim of superiority over the tilting family under every sizing rule, and
the paper does not make one; what it shows is that the tilting family's apparent
advantage survives only one of the three rules, and only on an assumption that was not
measured. The tilting family answers the same escape condition by a different route — the same
hardware, reused, but reoriented by a mechanism — and the case for the configuration
proposed here rests on reaching that reuse without the mechanism, together with its
control and transition consequences, and not on out-cruising it.
