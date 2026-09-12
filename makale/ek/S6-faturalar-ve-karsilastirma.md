# Supplementary S6 — The three bills stated formally, and a comparative sizing

*Supplementary material to "The Architectural Cost of Hybrid VTOL: meryemAircraft, a
Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System".*

This material was Sections 3.7 and 5.5 of an earlier, longer version of the paper. The first
states the three bills as equations with the transfer table showing that they are one quantity
in three currencies; the second sizes three architectures against the same mission under three
different sizing contracts, all twelve cells, with the sensitivity sweeps.

---

## S6.1 The three bills stated formally, and a test of the statement

The argument so far has been verbal. It is worth stating compactly, because the compact form
makes clear what the framework claims and what it does not.

For an architecture *a* flying a given mission, write the three charges as fractions of the
quantity each degrades:

$$f_1(a) = \frac{m_\text{hover-only}(a)}{\mathrm{MTOW}}, \qquad
f_2(a) = 1 - \frac{(L/D)_a}{(L/D)_\text{clean}}, \qquad
f_3(a) = \frac{P_\text{cont}(a) - P_\text{cruise}}{\sigma_P\,\mathrm{MTOW}}$$

where *m*<sub>hover-only</sub> is the mass that exists solely to hover, (L/D)<sub>clean</sub>
is the lift-to-drag ratio the airframe would have with no hover hardware exposed,
*P*<sub>cont</sub> is the continuously installed power, and σ<sub>P</sub> is the specific
power of the power system. Each is dimensionless, each is zero for an aircraft that does not
hover, and each is measurable for one that does.

**The claim of Section 3.6 is that the same architectural choice need not minimise all
three simultaneously.** The architectural moves available typically move cost between them
rather than removing it: retracting
the lift rotors reduces *f*₂ and raises *f*₁ by the retraction mechanism; tilting the
propulsors reduces *f*₁ and *f*₂ together and introduces a mechanism whose mass and failure
modes are the price; buffering the hover peak reduces *f*₃ and raises *f*₁ by the buffer.
Section 3.4 tabulates these transfers. The escape condition is the statement that all three
vanish simultaneously only when the hover and cruise hardware are the same hardware, in the
same orientation, doing the same job, with the peak supplied from a buffer.

**A consequence that can be checked against published work.** If the three are genuinely
separate currencies rather than three names for one quantity, then an architecture may be
*best* in one and *worst* in another — in particular, the architecture with the highest
cruise lift-to-drag ratio need not be the lightest. A single-metric comparison would not
anticipate that. The NASA sizing study quoted in Section 3.2 reports exactly this pattern:
the lift-plus-cruise concepts are the heaviest of the four examined *while having the highest
cruise efficiency of that group*, and the authors attribute the weight to hardware carried for
hover rather than to cruise power. That is *f*₁ dominating while *f*₂ is favourable, which is
the framework's prediction and not a restatement of it. The later and larger version of the
same programme states the transfer in a single sentence: "the high cruise efficiency of the
lift+cruise type reduces the battery weight compared to the quadrotor, but not enough to
counter the increase in structure and propulsion weight, so the all-electric lift+cruise
aircraft is the heaviest design" [22]. A gain in one currency, insufficient against a loss in
another, named as such by authors with no framework to defend.

**That later study also contains the case that would embarrass the framework if it behaved
differently, and it does not.** Sizing five architectures rather than four to the same mission
adds a tiltwing, and the tiltwing has the highest cruise efficiency of all of them:

| Concept | L/D_e | Design gross weight, lb |
|---|---:|---:|
| Quadrotor, turboshaft | 4.9 | 3 678 |
| Quiet single main rotor, turboshaft | 5.4 | 3 951 |
| Side-by-side, electric | 7.2 | 5 547 |
| Lift + cruise, electric | 7.9 | 9 482 |
| Lift + cruise, turbo-electric | 8.5 | 7 271 |
| **Tiltwing, turbo-electric** | **8.6** | **6 584** |

The tiltwing is best in cruise efficiency *and* lighter than either lift-plus-cruise concept.
A framework that predicted "best in cruise implies heaviest" would be refuted by this row. The
framework here predicts no such thing: it says the tiltwing satisfies most of the escape
condition, because the same propulsors serve hover and cruise and nothing is left exposed, and
that it pays instead for the mechanism that rotates them. That is precisely the trade
Section 5.5 finds when it sizes a tilting layout itself, and it is why no claim of superiority
over the tilting family is made anywhere in this paper.

The comparison of Section 5.5 shows the same pattern on a different set of architectures:
of the three sized there, the tilting layout has the best cruise lift-to-drag ratio — 13.44
against 12.00 — and is nonetheless twenty percent heavier than the tail-sitter, because it
carries a tilt mechanism that the tail-sitter does not. Best in *f*₂, worse in *f*₁. **That
comparison is an illustration and not evidence, and the distinction matters here.** Its
tilting layout is given a cruise-drag multiplier of 1.00 — that is, its mechanism is
credited as aerodynamically free — precisely to make the *f*₂ advantage as large as the
architecture could possibly claim. A comparison whose inputs were chosen by the present
authors cannot corroborate the present authors' framework. **The evidential weight rests on
work done by others**, whose numbers were produced for other purposes and are not ours to
choose; Section 5.5 shows what the framework looks like when applied, not that it is right.

**A second independent check exists, and it is on aircraft that were built rather than sized.**
Bacchini and Cestino compare three flying eVTOLs — one per architecture — on five parameters
[21]:

| | E-Hang 184 (multirotor) | Cora (lift + cruise) | Lilium (vectored thrust) |
|---|---:|---:|---:|
| Disc loading, N m⁻² | **440** | 880 | 7500 |
| Total hover time, min | **20.5** | 16.5 | 12.1 |
| Cruise speed, km h⁻¹ | 100 | 180 | **252** |
| Practical range, km | 42 | 107 | **203** |

The ranking reverses completely between the hover rows and the cruise rows. The architecture
best in hover is worst in cruise and the architecture best in cruise is worst in hover, with
the lift-plus-cruise layout between them on every line — which is what it means for the
currencies to be separate rather than three names for one quantity. Those authors also state
two of the three transfers in their own words, without any framework to state them in. Of the
lift-plus-cruise aircraft: its "parasitic drag caused by the pylons and vertical thrust
propellers increases the power required in cruise" — that is *f*₂. And of the vectored-thrust
aircraft, whose cruise efficiency is the best of the three: its hover "is so power demanding
that it requires batteries with higher specific power" than those assumed, so that "the
aerodynamic advantages of this configuration are balanced by higher demands on the batteries
and on the power electronics" — that is *f*₂ bought and *f*₃ paid, named as an exchange by an
author who was not looking for one.

None of these comparisons validates the framework. All are external consistency checks: the NASA
study was carried out for other purposes and its numbers were not chosen to suit the
argument here, and a framework that predicted the opposite ordering would be in difficulty
against them. The Bacchini and Cestino comparison is weaker as evidence in one specific way
and stronger in another: weaker because its three aircraft differ in mass, mission and
technical maturity as well as in architecture, so it does not isolate the mechanism the way a
controlled sizing study does; stronger because they exist, and their numbers are not the
output of anyone's sizing loop. Corroboration of this kind raises confidence that the three charges are
separable in practice; it does not establish that they are the only three, and nothing
short of a broad survey of sized architectures could.

**What the framework does not claim.** It does not predict the magnitude of any bill for an
architecture that has not been sized; the fractions above must be computed or measured case
by case. Nor does it claim that these are the only architectural costs a VTOL aircraft carries:
control authority, thermal management, transition hardware, reliability and certification are
all real and none of them is one of these three. What it provides is narrower and, because it is
narrower, defensible — that these three recurring charges follow from the duty-cycle mismatch of
Section 3.1, that they are the currencies in which the architectural remedies surveyed in
Section 3.5 trade against one another, and that there is a stateable condition under which none
of the three is charged.



---

## S6.2 A comparative sizing of three architectures

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
in Supplementary S5.13.

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
the blade one would choose for cruise. **An earlier version of this section claimed that range
does not contain propulsive efficiency, and that is wrong**: the propeller is the last link of
the η_chain that appears in the range equation above, at 0.80 of the overall 0.176. The
generosity therefore falls on both columns. On mass, 60.3 kg becomes 62.7 kg at a fifteen percent
efficiency penalty; on range, the tilting layout's fixed-fraction advantage of twelve percent
falls to roughly **minus five percent**, since range is linear in η_chain. The correction moves
the comparison against the tilting layout rather than for it, which is why it is recorded here
rather than left as a rounding matter: the one column in which that architecture led is the
column the correction removes it from. The sizing tables above are not recomputed on it, because
the fifteen percent is an illustration and not a measurement; what the tables report is the
comparison with the credit left in place, which is the generous case. And a second table, in which
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
