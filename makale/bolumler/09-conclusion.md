# 9. Conclusion

Hybrid vertical take-off aircraft pay for their vertical capability, and the payment is
architectural rather than a defect of implementation. It appears in three currencies — the mass
of hardware carried but unused, the drag of hardware exposed but inactive, and a power system
sized by a condition that holds for about two percent of the flight — and **each of the
architectural moves surveyed here reduces one of them by increasing another**. They are not
offered as the only costs a VTOL aircraft carries; they are the three that follow from the
duty-cycle mismatch, and the claim is about them. A NASA sizing study of four VTOL
architectures reaches the same conclusion from the opposite direction, finding the
lift-plus-cruise concept the heaviest of those examined while also the most efficient in cruise,
and naming the cause as the empty weight carried for hover.

Stating the tax that way makes its escape condition explicit, and it has four parts: **it is
charged unless hover and cruise are served by the same hardware, doing the same job, in the same
orientation, with the hover peak drawn from a buffer rather than from permanently installed
continuous power.** The configuration described here satisfies that condition rather than
compensating for failing it. The aircraft rotates; nothing on the aircraft rotates relative to
it. A single coaxial pair at the nose provides all thrust in both regimes; four small coaxial
pairs at the tips provide moments and nothing else; and a strip on the lower surface is assigned
the one gap propellers cannot close — the rolling moment, which parallel thrust vectors cannot
produce at any setting or mounting position. There are no elevons, no rudder, no tilting
mechanism, no retraction mechanism and no dedicated lift system.

The configuration was sized at 50 kg and at 1000 kg with the same equations, twenty times apart
in mass. Disc loading is constant by design, which is what keeps hover power growing linearly
with mass instead of as the classical L^3.5; the buffer that decouples the engine from the hover
peak stays under four percent of take-off mass at both points; and the drag fraction charged to
the tip frames is preserved. Three things do not scale, and all three are reported rather than
smoothed: the larger aircraft must rotate more slowly; its propeller grows faster than its span,
so the heavy design is not the light design seen from further away; and these are properties of
the sizing rules, while a component build-up of the structure meets the mass fractions at 50 kg
and does not at 1000 kg.

Two results emerged during the study that changed it. The tip frames, left as circular tubing,
would produce nearly as much drag as the rest of the aircraft — fairing them is a requirement
rather than an option, and the same fairing turns out to be the aircraft's directional stability
surface. And **a slower rotation loses *less* altitude, not more**, because the aircraft is
supported during the manoeuvre rather than falling through it, so entering the rotation while
still climbing removes the altitude penalty entirely in the point-mass model. That second result
survived a correction that might have removed it. The primary propulsor is sized at thrust equal
to weight and therefore supplies no climb at all; the margin comes from the four tip propellers,
which raises the achievable ratio to between 1.066 and 1.132 rather than the 1.2 an earlier
version assumed. Recomputed there, the altitude loss at both reference rotation times is still
zero — but acquiring the entry climb now takes twice as long, a rotation begun from rest is
worse than reported, and the take-off margin and the attitude authority are drawn from the same
four propellers and compete for them.

**What this paper offers is a configuration and its numbers, not a validated aircraft.** There
is no wind-tunnel data here and no flight test. Of the analyses Section 8 lists as tests of
these results, three have been carried out. A three-dimensional solution for the centre body
narrowed the zero-lift drag without overturning the assumption. A component build-up closes the
light design with 2.2 kg in hand, conditional on a shell areal density at or below 1.78 kg m⁻²
*and* on a battery buffer no measured cell can yet supply, and does not close the heavy design.
And a rotational check shows the tip propellers can turn the aircraft's own inertia through the
transition with a margin of 1.49 at 50 kg and 1.57 at 1000 kg on the cheapest profile — **0.99
and 1.05 on a smooth one**, and 1.14 and 0.76 at 50 kg if the tip thrust is recomputed on the
figure of merit used elsewhere in the paper rather than the one its design table implies. Under
every basis, both reference rotation times are actuator-limited lower bounds rather than
comfortable choices.

Resolving that check along the trajectory changed the question. The aircraft does not reach
ninety degrees of incidence: the body rotates through ninety but the relative wind rotates with
it, and peak incidence is seventeen to twenty-two degrees — four to eight over the half of the
wing lying in the nose propeller's slipstream. **The tight case is not the high-incidence middle
but the end of the rotation**, where incidence is small and speed is high, which makes it a trim
question rather than a stall one. The configuration is statically stable, with a neutral point
at 34 percent of mean aerodynamic chord and a margin of 12.5 percent, and the moment to be
balanced at cruise is 0.056. Reflex does not supply it: nine reflexed and low-moment sections
have been measured in tunnels that measure moment, exactly one returns a positive value — one
fourteenth of what is needed [17] — and the rest lie between zero and −0.03, because reflex as
actually built is a device for removing negative pitching moment rather than producing positive
moment [45,46]. **Nine degrees of tip washout does supply it**, at a cost of 4.3 percent of
cruise efficiency: the price of having no tail.

That twist also settled an assumption, and not in the paper's favour. Computing the profile drag
of the trimmed wing station by station at each station's own local lift coefficient gives an
Oswald span efficiency of **0.817** against the 0.85 assumed — optimistic by 3.9 percent, worth
1.4 percent of the ranges quoted.

**Attitude control is sized in every axis and closed in none, and that is the honest summary of
its control case.** Roll asks for ΔC_L ≈ 0.12 from the strip, which published fence and Gurney
data make plausible without establishing it here. Yaw is the strongest axis the arrangement has,
at 2.4 times the pitch moment, because differential thrust between the left and right tip pairs
acts through the semi-span; what yaw lacks is not authority but stability, and the surfaces that
must supply it are the same tip-frame fairings. That one member serves as landing structure,
moment arm, propeller mount and directional stability surface is the configuration's own
argument made once more; that none of the four roles has been verified together is its principal
limitation.

An earlier version of this section stated that none of the remaining analyses required an
experiment. **That is no longer true, and the change is the most important thing this study
learned about itself.** Transition controllability rests on a pitching moment that three methods
of three different fidelities fail to predict above roughly ten degrees of incidence — the
highest of them against wind-tunnel measurement — and the paper declines to substitute a reduced
calculation for a measurement.

**What survives independently of that is the framework.** The three currencies, the
demonstration that architectural remedies transfer the penalty rather than remove it, the escape
condition, and the finding that architectural comparisons change their ranking with the sizing
contract chosen — none of these depends on whether this particular aircraft is ever built.
meryemAircraft is the case that shows the escape condition can be instantiated in a real
geometry and carried through to reference designs at two scales. It is not offered as a
validated vehicle, and the paper is careful throughout to say which of its statements are
demonstrated, which are conditional, and which are open. The configuration is described in
enough detail for another group to attempt any of the outstanding analyses independently, and
that is the outcome this paper is written to invite.
