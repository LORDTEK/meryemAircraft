# Supplementary S3 — Control axes in full

*Supplementary material to "The Architectural Cost of Hybrid VTOL: meryemAircraft, a
Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System".*

This was Section 4.4 of an earlier, longer version of the paper. It is reproduced in full so
that every control-axis number quoted in the main text can be traced to the calculation that
produced it. The scripts that produce these numbers, and the record of the corrections made to
them during the study, are in the repository the paper cites.

---

## S3.1 Control without control surfaces

The nose pair produces thrust. The four tip pairs produce moments. They are not lift
rotors and they are not sized to hover the aircraft; in the vertical phase they carry
under fifteen percent of the total power. For the light reference design each tip pair
is 0.20 m in diameter and produces 16.2 N during the transition manoeuvre, drawing
335 W, for a total of 1.34 kW across the four.

The principle is not new, and the paper is better for saying so. A survey of tail-sitter
development identifies it directly: "one way to generate a larger pitching moment to assist
with the transition from vertical to horizontal flight is to add propellers away from the axis
of rotation of the tail-sitter and apply a differential thrust to these propellers", and traces
the idea to work at NASA Ames around the turn of the century [30]. What is particular here is
not the mechanism but the arm and the accounting: the frames reach three tip chords rather than
a fraction of one, and they are structure the aircraft needs anyway, so the arm is charged to
the landing gear rather than to the control system.

The tip pairs sit at the ends of rigid frames that extend from each wing tip
perpendicular to the planform, above and below, by three hundred percent of the local
tip chord — 0.71 m in each direction, giving a vertical separation of 1.42 m between
the upper and lower pairs. Figure 7 gives the placement and the resulting moment
arms. The frames are long on purpose. The control moment is
M = 2 T L, so lengthening the arm buys the same moment with less thrust; and because
propeller power goes as thrust to the three-halves power, tripling the arm reduces the
power required for a given moment to roughly one fifth. The frames are structure that
is already needed for another reason, as Section 4.5 explains, so the arm is nearly
free.

Pitch and yaw are produced by the same four actuators, but not with the same arm, and the
difference has not previously been stated. Differential thrust between the upper and lower
pairs produces a moment about the spanwise axis through the frame length, 0.71 m; differential
thrust between the left and right pairs produces a moment about the remaining axis through the
**semi-span, 1.726 m**. The yaw arm is therefore 2.43 times the pitch arm, and since the
thrust available is the same, so is the moment: 55.9 N·m against 23.0 N·m at the quoted
tip thrust, or 42.8 against 17.6 on the conservative thrust of Section 7.6. Yaw is the
strongest axis this arrangement has, and it is strongest for a geometric reason rather than
a designed one. In hover these are the two axes the aircraft must control against
disturbance; in cruise, with the airframe rotated through ninety degrees, the same four
actuators address the same two axes with their roles exchanged. No actuator changes its
function, its orientation, or its mounting.

Roll is different, and this is the one place where propellers alone are not sufficient.
The result is elementary but decisive. Every propeller on this aircraft has its thrust
vector parallel to the body's longitudinal axis, so each thrust is a force
**F** = (F_x, 0, 0) applied at a station **r** = (x, y, z). The moment about the
longitudinal axis is

    M_x = y F_z − z F_y = 0

identically, for every propeller, at every thrust setting, regardless of where it is
mounted. No arrangement of parallel thrust vectors, and no number of them, can produce a
rolling moment. The only roll moment available from the propulsion system is the
residual reaction torque, which the counter-rotating arrangement of Section 4.3 has
deliberately reduced to nearly zero. The two design decisions oppose one another, and
the opposition is real rather than apparent.

This is the same limitation that constrains every tail-sitter, and it is worth being
precise about how others resolve it, because the resolution here is not a variation on
theirs but a consequence of a different decision made earlier.

Contemporary tail-sitters resolve it in one of two ways. Some place elevons in the
propeller wash, which is a control surface by any definition. Others — including a
carbon-fibre quadrotor tail-sitter that achieves full attitude control in every flight
mode with no control surfaces at all — carry four separate single-rotation propellers
and take their rolling moment from the *differential reaction torque* between them.
That is the same mechanism a multirotor uses for yaw, appearing as roll once the
airframe is rotated into wing-borne flight.

The second solution is unavailable here, and unavailable by construction. The coaxial
counter-rotating arrangement of Section 4.3 exists precisely to cancel reaction torque,
and it cancels the roll actuator along with it. The two decisions are not merely in
tension, as noted above; they are mutually exclusive. A tail-sitter cannot both null its
reaction torque and use that torque to roll.

This is the fork at which the present configuration departs from its nearest relatives,
and it is why the strip is not an accessory. It is the element that makes the
combination possible. The
resolution adopted here is different in kind. A single strip on the lower surface,
inclined at forty-five degrees, extends by a commanded amount rather than snapping between
two positions. The extension is the control variable, so the rolling moment is modulated by
how far the strip stands proud of the surface rather than by how long it is held out. For the light reference design it runs one hundred and twenty percent of the
root chord in length, reaching outboard to sixty-seven percent of the semi-span, and
stands 2 cm high at its inboard end and 6 cm at its outboard end.

Its authority comes from its length, not its height. The moment scales with the moment
arm, whereas the benefit of additional height saturates: at constant length, doubling
the height from 5 cm to 10 cm roughly doubles the roll rate, while extending the length
from sixty to one hundred and twenty percent of root chord raises it almost fourfold.
This comparison is robust to how the strip's force is modelled, because the length enters
both the affected area and the moment arm while the height enters only the first.

**Because extension is the control variable, the strip has a threshold, and the threshold has
been measured.** Tests of rearwardly located spoilers on two models established that
"projections of less than 0.01c produce negligible changes in lift", and warned that a device
with that property is poor as a control because "a small stick movement produces no change in
trim, whereas a larger movement of the stick may produce large changes" [19]. The strip here is
tapered, so the threshold is not crossed everywhere at once: height grows outboard while chord
shrinks, and the outboard end reaches one percent of local chord at seven percent of full
extension while the root does not reach it until forty-eight percent. Evaluated on the actual
chord distribution, the strip is wholly inert below seven percent of commanded travel and
wholly active above fifty.

| Commanded extension | First active station | Active length | Effective arm | Rolling moment, fraction of full |
|---:|---:|---:|---:|---:|
| 0.05 | none | 0 % | — | **0.000** |
| 0.10 | 0.945 m | 19 % | 1.057 m | 0.041 |
| 0.15 | 0.668 m | 43 % | 0.930 m | 0.113 |
| 0.20 | 0.481 m | 59 % | 0.850 m | 0.177 |
| 0.30 | 0.239 m | 80 % | 0.757 m | 0.293 |
| 0.40 | 0.090 m | 92 % | 0.707 m | 0.399 |
| 0.50 | root | 100 % | 0.679 m | 0.500 |

The last column is the one that matters, and it is more benign than the threshold suggests. The
part of the strip that survives the threshold is the part with the longest arm — the effective
arm rises from 0.679 m at full extension to 1.057 m at one tenth of it — so most of the lost
area is bought back by the lengthened arm. Above a quarter of travel the response is linear to
within five percent; below fifteen percent more than a quarter of the commanded moment is
missing; below seven percent there is none. **Continuous extension therefore does not give
continuous authority from zero**, and a control design would have to carry that dead band
explicitly. It bounds small corrections rather than large ones, which is the opposite of the
usual complaint about a threshold device, and it is a consequence of the taper rather than of
the concept: a strip of constant height fraction would cross the threshold everywhere at once.

**What the roll axis costs, and what it is opposed by, are computed here.** The roll axis
had not been examined with the care given to pitch, and doing so separates a part that can
be computed for this geometry from a part that cannot. Distributing the component masses of
Section 6.7 by the same volume-weighted rule used for pitch gives a roll inertia of
**25.0 kg·m²** — two and a half times the pitch inertia of 9.81 kg·m², because the mass is
spread along the span rather than along the chord. Roll damping was then computed for this
planform rather than taken from the literature: imposing the helix-angle twist
θ(y) = −arctan(p y / V) on a vortex-lattice solution of the actual geometry gives a damping
coefficient of magnitude **|C_l_p| = 0.358**, linear in roll rate to 0.4 rad s⁻¹ and
converged to within 1.3 percent over a threefold resolution refinement. At the cruise
condition this is a damping slope of 77.6 N·m per rad s⁻¹ and a roll time constant of
**0.32 s**, so the roll response is damping-dominated within a third of a second and the
steady rate, not the initial acceleration, is what a control moment buys.

**The requirement follows, and it is a requirement rather than a demonstration.** A steady
roll rate of twenty degrees per second at cruise needs **27.1 N·m**, and twenty-five degrees
per second needs 33.9 N·m; time to a thirty-degree bank is then about 1.2 s. Whether the
strip supplies that depends on which mechanism it works by, and the two candidates do not
agree:

| Mechanism | Rolling moment | Steady roll rate |
|---|---:|---:|
| The strip's own force, as a swept fence (C_N = 1.3, an upper bound) | 11.3 N·m | 8.4 ° s⁻¹ |
| A change in the half-wing's circulation, ΔC_L = 0.10 | 22.4 N·m | 16.6 ° s⁻¹ |
| the same, ΔC_L = 0.15 | 33.7 N·m | 24.8 ° s⁻¹ |
| the same, ΔC_L = 0.20 | 44.9 N·m | 33.1 ° s⁻¹ |

The strip's own force cannot produce the twenty to twenty-five degrees per second this
configuration needs — it falls short by a factor of about three, and an earlier version of
this paper quoted 46 N·m without saying where it came from. The moment must therefore come
from the second mechanism: the strip changes the circulation of the half-wing it sits on,
which is how a Gurney flap or a low fence works, and the affected area is the wing's, not
the strip's. Twenty degrees per second then asks for **ΔC_L ≈ 0.12** over the strip's span.

**That figure can be compared against a measurement, and the comparison is favourable.** Traub
[18] tested an aspect-ratio-three wing in a low-speed tunnel with a Gurney flap two percent of
chord in height, in two spanwise arrangements: full span, and **the inboard two-thirds only**.
The second is the same spanwise fraction the strip occupies here. From the measured lift-curve
slopes and zero-lift angles of that inboard case, the increment at lift coefficients spanning
the present cruise condition is:

| Clean C_L | With inboard flap | ΔC_L |
|---:|---:|---:|
| 0.30 | 0.442 | 0.142 |
| 0.45 | 0.608 | 0.158 |
| 0.60 | 0.773 | 0.173 |

The requirement of 0.12 sits below the measured range rather than above it. **Two differences
keep this short of a demonstration, and both cut the same way.** Traub's flap is at the
trailing edge and perpendicular to the surface; the strip here is a swept fence on the lower
surface, well forward of the trailing edge, and the mechanism is not identical. And his wing is
unswept and rectangular where this one is swept and tapered. What the measurement establishes
is that a device of this class, at this height fraction, over this spanwise extent, produces
lift increments of the magnitude required — not that this strip produces one.

**The comparison also exposes a design fault the paper had not noticed.** Traub's flap is two
percent of chord everywhere. The strip specified in Section 4.4 grows linearly from 2 cm to
6 cm while the chord it stands on shrinks:

| Station along the strip | Local chord | Strip height | h/c |
|---|---:|---:|---:|
| root | 0.969 m | 0.020 m | 2.1 % |
| mid | 0.682 m | 0.040 m | 5.9 % |
| outboard end | 0.436 m | 0.060 m | 13.7 % |

There is a measured threshold for this. A NASA study of lift-enhancing tabs — devices placed on
the **pressure side** of a wing and **near rather than at** the trailing edge, which is the
closest published geometry to the strip described here — reports that "for flap heights less
than about 1.5 % c, the maximum L/D can also increase" while "flap heights greater than 1.5 % c
cause a decrease in the maximum L/D" [32]. Every station on this strip is above that threshold
and the outboard end is nine times it.

**A law that held h/c constant would be a different trade, and the paper had not seen that
there was one to make.** Holding h/c at two percent everywhere gives a strip of 0.0165 m²
instead of 0.0466 m² — sixty-four percent less frontal area, and the same reduction in deployed
drag, from 16.7 N to 5.9 N at cruise. Because such a strip's area distribution follows the
chord, its centroid sits at 0.507 m, exactly where the half-wing's own area centroid sits, so
the rolling moment under the circulation mechanism is unchanged. What it costs is hover: the
part of the strip lying inside the slipstream shrinks from 0.0182 m² to 0.0101 m², a
forty-five percent reduction in whatever authority comes from the strip's *own* force at zero
airspeed. Which way that trade should be settled depends on which mechanism dominates in
hover, and this paper has not settled that. One thing that does *not* settle it is the L/D
threshold above, because that threshold is about a device left deployed: this one is commanded
on only while a roll is being flown, so its cruise-drag penalty is intermittent by construction
and paying it is not obviously wrong. What can be said is that **the present height law was
not derived from anything, and the alternatives are now visible.**

**Deploying it on one side yaws the aircraft, and the paper had not said so.** The strip raises
lift on the half-wing that carries it and also raises drag there; the aircraft therefore rolls
away from the strip and yaws towards it, which is adverse yaw in the classical sense. The
magnitude follows from the same drag estimate: 16.7 N at the present height law, acting at
0.679 m, is **11.3 N·m** of yawing moment, falling to 2.9 N·m for a strip held at two percent of
local chord. Against the 42.8 to 55.9 N·m of yaw authority computed above, the coupling costs
between five and twenty-six percent of the yaw axis while a roll is being commanded. **It is
covered, and it is covered by the axis that happens to be the strongest** — but it is a
coupling, it had not been stated, and a control design would have to allocate for it.

**It loads the pitch axis too, and that one is not comfortable.** A wind-tunnel study of
tapered-height Gurney flaps on a 60° delta wing — tested at heights of two and five percent of
root chord, which is the same height law and the same range as the strip specified here —
reports that "the flap significantly increases nose down pitching moment" [33]. The mechanism
is the same on this aircraft: the lift the strip adds acts aft of the centre of gravity, so it
pitches the nose down. How far aft depends on where along the chord the increment appears, and
that is the part this paper cannot compute, since the strip is neither at the trailing edge nor
straight. Bracketing it by placing the increment at mid-chord, three-quarter chord and the
trailing edge of the affected region:

| Increment acts at | Moment about CG | ΔC_m |
|---|---:|---:|
| mid-chord | 3.7 N·m | 0.005 |
| ¾ chord | 13.2 N·m | 0.019 |
| trailing edge (upper bound) | 22.7 N·m | 0.032 |

The tightest pitching-moment budget in the whole of Section 7.6 is **0.050**, at the end of the
rotation. At the upper end of this bracket, commanding a roll during that phase would consume
two thirds of it. **The conclusion is a scheduling requirement rather than a redesign: the roll
strip should not be commanded during the end of the rotation**, which is the one phase where
the pitch axis has least to spare. The paper had not previously identified any reason to
restrict when the strip may be used.

The coupling is not a novelty of this configuration, and the older literature states it more
bluntly than the estimate above does. The same NACA survey reports that where spoilers were
used for lateral control on tailless aircraft, "if only upgoing spoiler projections are used,
the pitching moments developed are **prohibitive**", and that "a spoiler arrangement employing
equal up and down projections would improve this condition" though the data then available were
insufficient to settle it [19]. The strip specified here projects from one surface only, which
is the arrangement that warning is about. Two things follow. The bracket computed above is a
lower bound in kind as well as in magnitude, since it counts the lift increment and not the
attendant pressure redistribution ahead of the device. And the remedy the survey names —
projection from both surfaces, so that the pitching contributions oppose while the rolling
contributions add — is available to this configuration in principle and has not been examined
here. **The scheduling restriction above is the conservative resolution; a two-sided strip
would be the structural one, and choosing between them needs the wind-tunnel measurement this
section has already asked for.**

**The same device has a third use, and it is the one that costs nothing.** Deployed on both
halves at once the strip is not a roll control but a speed brake, and in that mode the
pitching-moment objection does not arise: a wind-tunnel investigation of spoiler-type ailerons
used as speed brakes and glide-path controls found that they "had only a small effect on the
wing pitching moments", and — the part that matters for a configuration with one moving surface
— that "the rolling effectiveness of the ailerons will not be impaired by such use" [49]. A
tail-sitter lands vertically and does not need a glide-path control for that, but it descends
to the transition point like any other aircraft, and the strip gives it a descent-rate control
that no other part of this configuration provides. The transfer is directional only: those
tests are on conventional wings with slotted flaps at higher Mach number, and the device
projects from the upper surface rather than, as here, the lower.

**Roll authority is therefore sized, supported by a measurement on a comparable device, and
still not closed.** The quantity a future measurement must return is ΔC_L for this strip on
this planform, not a moment.

**Hover is the harder case, and for a reason that is structural rather than numerical.** At
zero airspeed only the inboard part of the strip is loaded, by the slipstream, and the same
circulation model over the slipstream-washed area gives 6.0 to 12.0 N·m for ΔC_L between
0.10 and 0.20 — enough for a thirty-degree bank in 1.5 to 2.1 s. But at zero airspeed there
is no aerodynamic damping at all: the roll axis is a double integrator, so the rate does not
settle and the strip must be commanded off rather than left on. Roll control in hover is
consequently a tighter problem than roll control in cruise, which is the reverse of the
usual situation and is a consequence of this configuration rather than of its numbers.

**The worst case, in which the extension is not modulated at all, is worth computing because
it bounds the actuator requirement.** Simulating the first-order roll dynamics above as though
the strip snapped between fully out and fully retracted, with a deadband and a finite actuator
delay, gives a bounded limit cycle: with a two-degree deadband and a fifty-millisecond
deployment the bank angle oscillates by ±0.2°, and at a hundred and fifty milliseconds by
±9.4°. **A proportional extension does not produce that limit cycle at all**, so these figures
are an upper bound on what the actuator must achieve rather than a description of how the
aircraft is flown — and they say that even a device reduced to two positions would be usable
provided it were fast. None of this is a closed-loop stability analysis, and none of it
substitutes for one.

**Two consequences of variable extension are worth stating, because both relieve constraints
identified above.** The couplings scale with the extension: adverse yaw and the nose-down
pitching moment are proportional to the lift and drag increments the strip produces, so a roll
commanded at a fraction of full extension carries that fraction of both. The scheduling
restriction derived above — that the strip should not be commanded at the end of the rotation —
is therefore a restriction on *full* extension, and small corrections remain available
throughout. And the height law is limited by those couplings rather than by mass: the strip's
own structure is a small item, so how far it may extend is set by how much yaw and pitch
disturbance the tip propellers can absorb, which is the calculation given above rather than
anything in Section 6.7.

**Yaw was examined last, and it separates cleanly into an easy half and an open half.** The
easy half is authority. The yaw inertia computed from the same mass distribution is
33.7 kg·m² — close, as it must be for a nearly planar aircraft, to the sum of the roll and
pitch inertias — so the available yaw moment turns the aircraft's own inertia at 73 to 95
degrees per second squared, reaching fifteen degrees of heading in about six tenths of a
second. Nothing in this axis is short of moment.

The open half is stability. A vortex-lattice solution of the planform at sideslip returns
**C_n_β = 0**: the wing supplies no directional stability whatever, which is not a defect of
the solution but the expected result for a planar surface with nothing to generate side
force. Two measurement campaigns say the same thing about real aircraft rather than about a
panel model. A NASA series of four 60°-swept flying wings tested from −8° to 48° of incidence
found that, without vertical tails, "each of these wings possessed unstable or essentially
neutral values of directional stability for most of the angles of attack tested" [20]; and the
NACA survey of tailless practice records that "the directional stability at low angles of
attack for the wing alone has generally been found to be inadequate" [19]. **The present
configuration is not unusual in lacking weathercock stability; it is normal, and every tailless
aircraft that flies has had to buy it somewhere.** Sweep gives this configuration its roll-due-to-sideslip — C_l_β = −0.045 per radian,
a healthy value — and gives it no weathercock stability at all. The profile-drag
contribution to yaw damping is likewise negligible, C_n_r = −0.0023, a time constant of over
a minute. That last number is less alarming than it looks, and the reason is conditional. Low
rotational damping is inherent to the tailless class, and free-flight experience is that the
small values "will not be excessively detrimental to the flying qualities **provided the
directional stability of the airplane is adequate**" [19] — so the two open items in this axis
are not independent, and the yaw-damping deficit is forgiven only if the weathercock
requirement below is actually met. The same source adds that lateral-oscillation damping is
most critical at high speed, because both C_n_r and the coupling between yawing and rolling
diminish at low incidence. **For this aircraft that names cruise, not transition, as the
critical case for Dutch roll.**

**And zero is an optimistic starting point, not a neutral one.** A vortex-lattice model has no
volume, so the calculation above contains the planform and nothing else. The centre body of a
blended wing is a body, it develops side force in sideslip, and that side force acts forward of
the centre of gravity. The survey states the magnitude in the only terms that matter here: on
tailless aircraft the destabilising effect of the fuselage and nacelles "is usually at least as
great as the stabilising effects contributed by the wing alone" [19]. The wing alone here
contributes zero, so the comparison gives no number — but the sign is unambiguous, and the true
figure the fairing has to make up is **below** zero rather than at it. Nothing in this section
quantifies that deficit, and the margin reported below should be read with it outstanding.

Directional stability must therefore come from the tip frames, which in cruise stand
perpendicular to the wing plane above and below each tip and are the only vertical surfaces
the aircraft has. Their mid-chord sits 0.879 m aft of the centre of gravity, which is a
long arm for a surface that already exists. Taking a lift-curve slope of 4 per radian for a
slender faired strut — an assumed value, not a measured one — the side area needed is 0.058 m²
to reach C_n_β = 0.03 and 0.097 m² to reach 0.05, which spread over the 2.84 m of combined
frame length is a fairing chord of 21 mm and 34 mm.

Those two targets were chosen by this study rather than taken from anywhere, and there is a
published criterion that should have been used instead. The NACA survey of tailless practice
states that tailless aircraft are **not exempt** from the conventional standard — directional
stability "should be as great as required on conventional airplanes if the same requirements
regarding satisfactory flying qualities are to be adhered to" — and puts that standard at
C_n_β "usually greater than **0.001 per degree**", noting that free-flight tunnel models were
flown successfully at one third of it but that "the best flying qualities of these models were
obtained with values of C_n_β in excess of 0.001" [19]. In radian measure the recommendation is
**0.0573** and the demonstrated floor is 0.0191. Both values this study picked lie below the
recommendation.

Sized against the criterion rather than against a guess, the fairing chord required is
**39 mm**, and the floor demonstrated in free flight is met at 13 mm. A faired strut of the
20 mm thickness assumed in Section 5.2 carries a chord of several times its thickness —
typically 50 to 70 mm — so the established criterion is met by a fairing **smaller than the
one the structure needs anyway**, with between a quarter and three quarters of that chord left
over. The conclusion the paper drew from its own two numbers survives being held to a real
standard, which is the only reason it is worth restating: directional stability on this
configuration does not ask for a surface, it asks for a fairing on a frame that is already
there.

**Where to buy it is a question the tailless literature has already answered, and the answer
is the arrangement this aircraft already has.** The NACA survey states that "if the tailless
airplane has a swept-back wing, the usual practice is to place the vertical tail surfaces at
the tips rather than at the center section in order to take advantage of the longer moment
arm" [19]. That is the tip-frame arrangement of Section 4.3, adopted here for the moment arm it
gives the control propellers and for the landing structure it provides, and it turns out to be
the placement a directional-stability surface wants for an independent reason.

The same source adds two things the estimate above does not contain, and they pull in opposite
directions. The first is favourable: because a tip fin's drag acts at a moment arm of half the
span, "the drag characteristics as well as the lift characteristics of the tip fins exert an
influence on the directional stability", and fins working on the profile-drag principle were
found more effective than those working on lift. The area estimated above was sized on lift
alone, so it is an **over**-estimate of what is needed. The second is a requirement: the toe
angle is not free. Fins of aspect ratio below about two must be toed *in*, and fins of moderate
or high aspect ratio toed *out* — and the frames here, at 1.42 m long against a fairing chord
of tens of millimetres, are firmly in the second class. Toe-out carries a hazard the paper had
no way of knowing about: yawing far enough to stall the rear fin produces a large
*destabilising* moment, where a toed-in fin stalling produces a stabilising one.

The magnitude, at least, is small. Wind-tunnel tests of a tail-less swept cargo configuration
with vertical tails carried on tip pods found the optimum toe angle for maximum lift-to-drag
ratio to be **about 1.5 degrees** for symmetric-section tails, with a cambered tail
"relatively insensitive to toe-in" [34]. The same tests found the lift-to-drag ratio "about the
same with all three vertical-tail designs, notwithstanding the 75 % larger area" of the largest
— which is the same conclusion reached above from the required-area side, arrived at by
measurement rather than by estimate. **The frame fairing therefore needs a toe angle of order a
degree or two, and that angle needs a sign.**

An earlier version of this paper left the sign open on the ground that these frames lie beyond
the aspect-ratio range of either source. That reasoning was wrong, because the rule is not a
correlation but a statement about which force does the work. Low-aspect-ratio fins are toed
*in* so that the stabilising moment is generated by the large induced drag such surfaces carry;
high-aspect-ratio fins are toed *out* so that it is generated by "the outwardly directed lift"
[19]. Raising the aspect ratio shifts the balance further from drag and towards lift, so it
strengthens the case for toe-out rather than carrying the rule outside its range. **The sign is
toe-out.**

What is genuinely open is narrower and more awkward. A fairing of 39 mm chord at cruise speed
sits at a Reynolds number near **80,000**, and the assumed lift-curve slope of 4 per radian is
an assumption at any Reynolds number and an optimistic one at that. Symmetric sections at low
Reynolds number are measured to behave badly in exactly the band a toe angle of one or two
degrees occupies: of four symmetric sections tested at Princeton, all showed lift-curve
nonlinearity about zero incidence, and in a more severe case the slope of the lift curve
"actually changed sign over a 3 deg range" [36]. **The question is therefore not which way to
toe the fairing but whether a surface of that chord, at that Reynolds number, develops the side
force this section has credited it with at all.** That is a wind-tunnel question, and it is the
one this paper would put first if it had a tunnel.

That same study is the third independent report of the finding this subsection began with: a
podded tailless wing was directionally *unstable*, and "the further addition of vertical tails
restores directional stability to the configuration" [34].

**That reframes the fairing, and the reframing is the substantive result of this
subsection.** Section 5.2 introduced the fairing as a drag measure and computed the frame
drag penalty on that basis. It is also, and not incidentally, the aircraft's directional
stability surface and its principal source of yaw damping. The two roles are served by the
same hardware — which is the same pattern the whole paper is about — but the paper had not
noticed the second role, and the fairing's chord is consequently constrained from two
directions rather than one. Neither the fin contribution nor the yaw damping it brings is
computed here. **Yaw authority is sized; directional stability is a requirement placed on a
component the design already carries.**

**Two measured effects work against the strip in exactly the conditions this configuration
needs it, and both were found by reading rather than by calculating.** Wind-tunnel tests of a
Gurney flap under controlled inflow turbulence report that the device "became less effective
after stall angle", and that at a turbulence intensity of 19 percent "the benefit to the
aerodynamic performance was negligible", against gains of 2.7 to 14.4 percent in lift-to-drag
ratio at 10.5 percent [35]. Both findings point at this aircraft. The transition passes through
incidences at which the outboard wing is post-stall, which is where roll disturbances are
largest and where the device is reported to weaken; and the strip's inboard portion is
deliberately placed inside the nose propeller's slipstream, which is not a low-turbulence
environment. **The slipstream placement that gives the strip authority at zero airspeed may
also be the place its mechanism works least well.** Neither effect is quantified for this
geometry — the cited tests are on a wind-turbine aerofoil with grid-generated freestream
turbulence, not a propeller wake — but the direction is measured rather than supposed, and it
is recorded in Section 8 as a risk to hover roll authority specifically.

**On the post-stall half of that risk the literature is not unanimous, and reporting only the
unfavourable half would misrepresent it.** A delayed-detached-eddy simulation of a 21 %-thick
section at twenty degrees of incidence — deep stall — with a Gurney flap of two percent chord,
which is the height fraction at this strip's root station, returns a lift coefficient higher by
ninety-four percent with the drag coefficient unchanged to within half a percent [37]. That is
the opposite of a device weakening past the stall. The two results are not directly comparable:
one is a measurement and the other a simulation whose plain-aerofoil baseline falls
twenty-five percent below the experimental lift at the same condition, and they vary different
things — one inflow turbulence, the other incidence. What can be said is that **the post-stall
behaviour of this class of device is contested, while the turbulence sensitivity is measured
and stands unopposed.** The risk carried into Section 8 is therefore the turbulence one
primarily, with post-stall behaviour an open question rather than a known deficit.

A third result bears on the part of the claim that looked weakest. The same device was
visualised in a water tunnel at a Reynolds number of 8 588 — four orders of magnitude below
the wind-tunnel work — and behaved in qualitative agreement with it, the authors attributing
this to the mechanism being an effective camber increase and therefore "an inviscid effect to
the first order" [38]. **That is the most direct support available for the claim that the strip
still works at zero airspeed**, where the only flow it sees is the slipstream and the Reynolds
number is at its lowest. It supports the direction and not the magnitude: the study is flow
visualisation and reports no forces. The same source also records the cost, measured rather
than estimated: a strip of 1.25 percent chord leaves drag unchanged from the clean wing, while
one of five percent brings a significant drag increase [38]. This strip runs from 2.1 to
13.7 percent.

The strip does one further thing that an ordinary aerodynamic surface cannot. Its
inboard portion lies inside the slipstream of the nose propeller, where the dynamic
pressure is set by the disc loading rather than by the airspeed:

    q_slipstream = T / A

For the light reference design this is 433 N m⁻² in hover — the dynamic pressure of a
26 m s⁻¹ freestream — available at zero airspeed. The strip therefore produces a usable
moment while the aircraft is standing still, which an aerodynamic surface outside the
slipstream cannot. Its outboard portion lies beyond the slipstream, where it works
against the freestream in cruise. The slipstream covers only twenty-seven to
thirty-nine percent of the semi-span, so lengthening the strip to serve cruise does not
compromise its hover function; one device serves two regimes. Figure 8 shows the strip
against the slipstream boundary: the inboard 46 % of its length lies inside, the
outboard 54 % outside.

