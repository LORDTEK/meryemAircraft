# 7. Flight profile and transition

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

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

The transition was simulated as a two-degree-of-freedom point mass. The body angle θ is
driven from zero to ninety degrees over a rotation time t_r; thrust acts along the body
axis, lift perpendicular to the velocity vector and drag opposite to it; the lift curve
is linear to stall and a flat-plate relation beyond it; and thrust is reduced to the
drag value once cruise speed is reached. Altitude loss is reported as the lowest point
of the trajectory relative to the entry altitude.

The result is plotted in Figure 10a for both reference designs and four thrust-to-weight
ratios; the tables below give the same values.

**Light reference design, 50 kg. Altitude loss, metres:**

| t_r | T/W = 1.1 | **T/W = 1.2** | T/W = 1.3 | T/W = 1.5 |
|---:|---:|---:|---:|---:|
| 0.5 s | −19.1 | −16.6 | −14.5 | −11.0 |
| 1 s | −17.1 | −14.2 | −11.6 | −3.5 |
| 2 s | −13.2 | **−9.1** | −2.1 | 0 |
| 3 s | −9.9 | **−0.8** | 0 | 0 |
| 4 s | −2.2 | **0** | 0 | 0 |

**Heavy reference design, 1000 kg. Altitude loss, metres:**

| t_r | T/W = 1.1 | **T/W = 1.2** | T/W = 1.3 | T/W = 1.5 |
|---:|---:|---:|---:|---:|
| 1 s | −32.2 | −27.4 | −23.3 | −16.0 |
| 2 s | −27.0 | −20.9 | −7.7 | −1.0 |
| 3 s | −21.8 | **−7.2** | −1.4 | 0 |
| 4 s | −17.7 | **−1.4** | 0 | 0 |
| 5 s | −5.8 | **0** | 0 | 0 |

The relationship is monotonic in the direction opposite to the one usually assumed. It
is frequently supposed that a tail-sitter should rotate as quickly as possible, on the
reasoning that the aircraft is unsupported during the rotation and therefore falls for a
time t_r, giving an altitude loss proportional to t_r². **That reasoning is wrong, and
the error is in its premise.** The aircraft is not unsupported during the rotation.
Vertical support is T cos θ + L, and a slow rotation keeps cos θ large during exactly
the interval in which V, and therefore L, is being built. A fast rotation collapses
cos θ before there is any L to replace it, and the aircraft falls precisely because it
hurried.

The practical consequence is a simplification rather than a trade. The control power
required to rotate the aircraft in time t_r scales as 1/t_r², so a slow rotation is
cheap in control authority; and the altitude loss also falls with t_r. **Both
constraints point the same way.** There is no optimum transition time to be found
between two competing penalties, because there are not two competing penalties. The
transition time is bounded from below, not from above, and its upper bound is set by
fuel, horizontal displacement and operational exposure rather than by flight mechanics.

Thrust-to-weight ratio is the dominant parameter. At T/W = 1.1 the loss stays in double
figures until the rotation is stretched beyond three seconds; at T/W = 1.3 the light
design reaches zero within three seconds and the heavy design within four. The reference
designs assume T/W = 1.2, at which the light design completes the manoeuvre in three
seconds for a loss under one metre and the heavy design in five seconds for no loss.

### Entering the rotation while climbing

The tables above assume the aircraft rotates from a stationary hover. It does not have
to, and it should not. The aircraft reaches transition altitude by climbing, which means
it arrives there with an upward velocity that has already been paid for. Stopping to
hover before rotating discards that velocity deliberately.

Carrying it into the manoeuvre instead converts it into a reserve. Repeating the
simulation with an entry climb rate w₀:

**Light reference design, T/W = 1.2. Altitude loss, metres:** (plotted in Figure 10b)

| t_r | w₀ = 0 | w₀ = 2 m/s | w₀ = 5 m/s | w₀ = 8 m/s |
|---:|---:|---:|---:|---:|
| 1 s | −14.2 | −10.3 | −0.4 | **0** |
| 2 s | −9.1 | −0.4 | **0** | **0** |
| 3 s | −0.8 | **0** | **0** | **0** |
| 4 s | **0** | **0** | **0** | **0** |

A five-metre-per-second entry climb removes the altitude loss at every rotation time
that is otherwise sensible, and the heavy design behaves the same way. The cost of
acquiring that climb rate is negligible: at T/W = 1.2 the vertical acceleration is
(T/W − 1)g = 1.96 m s⁻², so five metres per second is reached in 2.6 s over 6.4 m of
climb, and the kinetic energy involved is 625 J against a fuel energy of 103 kWh.

**The reference profile is therefore to enter the rotation at 5 m s⁻¹ of climb and
rotate over the times given in Section 6 — two seconds for the light design, four for
the heavy — for no altitude loss at all.** The manoeuvre that the
literature treats as the tail-sitter's characteristic hazard becomes, in this
configuration, a manoeuvre with no altitude penalty — not because of any device, but
because the aircraft is not asked to stop first.

The limits of this simulation should be stated where its results are used. It is a point-mass model in which the body angle is driven kinematically, so it does not represent rotational dynamics and the tip-propeller thrust required to produce the rotation does not follow from it. The aerodynamic model is a linear lift curve to stall with a flat-plate relation beyond it; dynamic stall, separation hysteresis and propeller-wake effects on the wing are absent.

With the transition no longer demanding a rapid rotation, it is no longer the case that
sizes the tip propellers. The sizing case becomes disturbance rejection in hover, which
an order-of-magnitude estimate places well inside the existing capability: a five-metre-
per-second gust normal to the planform produces a moment of the order of 5 N·m, against
a capability of M = 2 T L = 23 N·m from the tip pairs at the reference geometry — a
margin of roughly four. The tip propellers are
therefore kept small — 0.20 m — deliberately, so that they contribute as little as
possible to cruise drag while retaining margin on the case that actually sizes them.

This is an order-of-magnitude check against a single gust condition. The disturbance spectrum and the closed-loop bandwidth required to reject it have not been analysed.

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

## 7.6 Whether there is enough authority to rotate

Section 7.4 drives the body angle kinematically. The aircraft does not rotate in that
simulation; it is *assumed* to rotate, and the moment producing the rotation does not
appear. Section 8.6 records this. What follows does not remove that limitation — a full
six-degree-of-freedom treatment would need pitching-moment coefficients through ninety
degrees of incidence, and no such data exists for this planform — but it closes the part
of the question that can be closed without them.

**The test is a lower bound.** If the tip propellers cannot rotate the aircraft's inertia,
they certainly cannot rotate it against aerodynamic moment as well. If they can, the
aerodynamic margin remains unknown and is reported as unknown.

**Inertia.** The component build-up of Section 6.7 supplies the masses; the planform of
Section 4.2 supplies where they sit. Distributing the shell and internal structure over the
planform, the tip frames along their own length, the tip motors and propellers at the ends
of those frames, and the centre-body items along the root chord gives a moment of inertia
about the spanwise axis — the axis the transition rotates about — of 7.04 kg m² for the
light design and 1 918 kg m² for the heavy one, with the centre of gravity at 57 and 58
percent of root chord respectively.

**The rotation profile matters, and Section 7.4's cannot be produced.** That simulation
ramps the body angle linearly, which requires zero torque throughout and infinite torque at
each end. The nearest profile a finite moment can produce brings angular velocity and
acceleration to zero at both ends, and its peak angular acceleration is 6Δθ/t_r²; a
bang-bang profile needs 4Δθ/t_r². The stricter of the two is used here.

**Authority.** The frames place the upper and lower pairs 0.71 m from the planform in the
light design, and differential thrust between them acts about the spanwise axis, as
Section 4.3 sets out. Taking the transition thrust of Section 4.3:

| | Required | Available | Margin | Shortest rotation |
|---|---:|---:|---:|---:|
| Light, t_r = 2 s | 16.6 N m | 46.0 N m | **2.8 ×** | 1.20 s |
| Heavy, t_r = 4 s | 1 130 N m | 1 905 N m | **1.69 ×** | 3.08 s |

The light design needs 5.84 N per pair to turn its own inertia, thirty-six percent of the
16.2 N quoted in Section 4.3. That quoted figure is itself worth checking: at 335 W and
0.20 m diameter it implies a figure of merit of 0.702 with no coaxial interference loss,
where the hover figure of merit used elsewhere in this paper is 0.599. Recomputing at 0.599
with a fifteen percent coaxial loss gives 12.4 N and a margin of 2.1 ×. The conclusion does
not depend on which is right.

**The margin narrows with size, and now has a scaling law.** Available moment grows as
thrust times arm, so as the cube of linear scale; inertia grows as mass times length
squared, so as the fifth power; and required acceleration falls as the square of rotation
time. The margin therefore goes as t_r²/scale², and holding it constant requires rotation
time to grow *linearly* with scale. Going from 50 kg to 1000 kg is a linear scale factor of
3.345, so preserving the light design's margin would need 6.7 s rather than the 4 s used —
which is why the heavy margin is 1.69 rather than 2.8. Section 7.4 already concluded that
the larger aircraft must rotate more slowly; this is the quantitative form of that
statement, and it adds to it that the control margin, not only the altitude loss, is what
tightens.

**What this does not establish.** The centre of pressure travels as the aircraft rotates
through ninety degrees, and the pitching moment that travel produces is not computed here.
The margins above are inertial margins and not total control margins. Whether the
aerodynamic moment consumes them is the question a six-degree-of-freedom simulation would
answer, and it cannot be answered without moment data this study does not have.
