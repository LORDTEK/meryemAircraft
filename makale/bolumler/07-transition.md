# 7. Flight profile and transition

The transition between vertical and horizontal flight is the manoeuvre on which
tail-sitters have historically been judged, and it is the part of this configuration
that most deserves scrutiny. This section describes the flight profile, states the
equations that govern the transition, and reports a simulation of it. One result
contradicts a widely-assumed relationship and is presented as such.

## 7.1 The five phases

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
contact points. Section 7.5 notes what is and is not analysed here.

Figure 9 shows the five phases in sequence. Nothing on the aircraft rotates relative to
the aircraft at any point in it.

## 7.2 Why the transition begins in the easiest condition

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

## 7.3 The thrust singularity that is never reached

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

## 7.4 Transition time: slower is better

The transition was simulated as a two-degree-of-freedom point mass. The body angle is driven
from zero to ninety degrees over a rotation time t_r; thrust acts along the body axis, lift
perpendicular to the velocity vector and drag opposite to it; the lift curve is linear to stall
and a flat-plate relation beyond it. Altitude loss is the lowest point of the trajectory
relative to the entry altitude. Figure 10a plots both reference designs at four
thrust-to-weight ratios.

**The ratio the aircraft actually has must be established first, and it is not a free choice.**
Section 6.1 sizes hover power at thrust equal to weight, so the 10.9 kW of Section 6.2 buys
T/W = 1.00 and nothing more; the same is true of the 216.2 kW of Section 6.3. The only other
source of vertical thrust on this aircraft is the tip pairs, and during the rotation they are
occupied producing the rotation itself. On the bang-bang profile the upper pairs run at full
thrust and the lower pairs at zero, which is the M = 2TL of Section 4.3 — and the two upper
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
to rotate in time t_r scales as 1/t_r² and the control *power* as 1/t_r³ — Table 4 of Section 6.4
is the second of these, and its entries are constant to within a third of a percent when
multiplied by t_r³ — so a slow rotation is cheap in authority and cheaper still in power; and
altitude loss also falls with t_r. **All of these point the same way**, so there is no optimum
transition time to be found between competing penalties — the rotation time is set by what the
actuator can do, not by a balance, and Section 7.6 shows that is where both reference times come
from.

**Entering the rotation while still climbing removes the penalty entirely**, and it survives the
correction to thrust-to-weight above. At an entry climb of 5 m s⁻¹ the altitude loss is zero at
both reference rotation times — 2 s light and 5.1 s heavy — and remains zero at every ratio from
1.066 down to 1.00, which is to say the result does not depend on the tip pairs contributing any
lift at all once the climb has been acquired.

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
requirement. And the tip pairs, introduced in Section 4.3 as moment producers and charged in
Section 5.4 for their mass and drag, turn out to carry the take-off thrust margin as well: an
aircraft whose primary propulsor is sized at thrust equal to weight leaves the ground on them.
That is a second duty for hardware bought for the first, which is the kind of economy this
configuration is built on — but it is also a dependency, and it is a harder one than it looks,
because the margin and the attitude authority are drawn from the same four propellers and cannot
both be had in full. Section 8 records it as an open item.

**The test is a lower bound.** A point mass carries no rotational dynamics, no aerodynamic
pitching moment and no control-power limit; Section 7.6 supplies the rotational budget that this
model omits, and Section 8 states what neither supplies.

## 7.5 Landing

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
question. It is listed in Section 8 rather than answered here.

## 7.6 Whether there is enough authority to rotate, and whether it trims

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
to be tailless**, and entered in the ledger of Section 5.4 as its fifth item. The reflex route
is not free either: a blended-wing UAV trimming by reflex rather than twist records that
carrying reflex over a wide span "is not conducive to the improvement of overall lift-to-drag
performance" [44]. **Both roads to trim on a tailless configuration cost cruise efficiency**,
which is the reading Section 5.4 places on the 4.3 percent: it is the price of having no tail,
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
than to computation, and Section 8 asks for it as measurement. The same tests found the
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
