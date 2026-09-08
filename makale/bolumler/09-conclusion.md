# 9. Conclusion

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

Hybrid vertical take-off aircraft pay for their vertical capability, and this paper has
argued that the payment is architectural rather than a defect of implementation. It
appears in three currencies — the mass of hardware carried but unused, the drag of
hardware exposed but inactive, and a power system sized by a condition that holds for
about two percent of the flight — and each known architectural move reduces one of them
by increasing another. A NASA sizing study of four VTOL architectures reaches the same
conclusion from the opposite direction, finding the lift-plus-cruise concept to be the
heaviest of those examined while also having the best cruise efficiency, and naming the
cause as the empty weight carried for hover.

Stating the tax in that form makes its escape condition explicit: it is charged whenever
hover and cruise are served by hardware that is not the same hardware, doing the same
job, in the same orientation. The configuration described here satisfies that condition
rather than compensating for failing it. The aircraft rotates; nothing on the aircraft
rotates relative to it. A single coaxial pair at the nose provides all thrust in both
regimes. Four small coaxial pairs at the wing tips provide moments and nothing else, and
a strip on the lower surface is assigned the one gap that propellers cannot close — the
rolling moment, which parallel thrust vectors cannot produce at any thrust setting or
mounting position, and which Section 4.4 sizes without demonstrating. There are no elevons, no rudder, no tilting mechanism, no retraction mechanism
and no dedicated lift system.

The configuration was sized at 50 kg and at 1000 kg using the same equations and the
same architecture, twenty times apart in mass. Three properties hold across that range:
disc loading is constant by design, the energy buffer that decouples the engine from the
hover peak stays under four percent of take-off mass at both points, and the drag
fraction charged to the tip frames is preserved because frontal area and wing area scale
together. Holding the disc loading is what keeps hover power growing linearly with mass
instead of as the classical L^3.5. Two quantities do not scale, and both are reported
rather than smoothed: the larger aircraft must rotate more slowly, and its propeller
grows faster than its span, so the heavy design is not the light design seen from further
away. A third does not scale either, and it is the one that matters most: these are
properties of the sizing rules, and a component build-up of the structure that would have
to realise them meets the mass fractions at 50 kg and does not at 1000 kg.

Two results emerged during the study that changed it. The tip frames, if left as
circular tubing, would produce nearly as much drag as the entire rest of the aircraft;
fairing them is not an option but a requirement, and it is also what makes their tip
surfaces available as lifting surfaces at no additional part or mass. And the transition
does not behave as commonly assumed: a slower rotation loses *less* altitude, not more,
because the aircraft is supported during the manoeuvre rather than falling through it —
so entering the rotation while still climbing, rather than stopping to hover first,
removes the altitude penalty entirely in the point-mass model of Section 7.4.

What this paper offers is a configuration and its numbers, not a validated aircraft.
There is no wind-tunnel data here and no flight test. Two of the four analyses that
Section 8 lists as tests of these results have been carried out — a three-dimensional
solution for the centre body, which narrowed the zero-lift drag without overturning it,
a component build-up of the mass budget, which closes the light design point with 2.2 kg
in hand provided the shell areal density stays at or below 1.78 kg m⁻² and does not close
the heavy design at all, and a rotational check which shows the tip propellers can turn the aircraft's own inertia
through the transition, with a margin of 1.49 at 50 kg and 1.57 at 1000 kg on the cheapest
rotation profile — and of 0.99 and 1.05 on a smooth one, which is to say that both reference
rotation times are actuator-limited lower bounds rather than comfortable choices. That
second figure set the heavy design's rotation time: at the four seconds first used, the
margin was below unity on both profiles, so the rotation was
lengthened to 5.1 s, which costs six percent of hover power instead of thirteen and changes
no other result. The fourth has not been carried
out, and the third is a necessary condition only: charging the aerodynamic pitching moment
through ninety degrees of incidence needs measurements this study does not have. What that
check does supply is a threshold, resolved along the trajectory, and resolving it changed the
question. The aircraft does not reach ninety degrees of incidence: the body rotates through
ninety, but the relative wind rotates with it, and peak incidence is between seventeen and
twenty-two degrees. The high-incidence part of the rotation happens at low dynamic pressure,
where the margin tolerates a coefficient of about 0.21 entering in a climb; the tight part
is the end of the rotation, where incidence is small and speed is high, and that is a trim
question rather than a post-stall one. The trim question has since been sized rather than
closed: the configuration is statically stable, with a neutral point at 34 percent of mean
aerodynamic chord and a margin of 12.5 percent at the assumed centre of gravity, and the
camber moment needed to trim it at cruise is 0.056, which is at the upper edge of what
reflexed sections deliver. The roll axis was treated the same way and gave the same kind of
answer: the roll inertia and the roll damping are computed for this planform, twenty degrees
per second at cruise requires 27.1 N·m, the strip's own force supplies about a third of
that, and the remainder must come from the change it makes to the half-wing's circulation —
a requirement of ΔC_L ≈ 0.12 that published fence and Gurney data make plausible without
this paper establishing it. Attitude control on this aircraft is therefore sized in every
axis and closed in none of them, and that is the honest summary of its control case. The outstanding measurement is therefore of ordinary size. The claims
most exposed are identified in Section 8. An earlier version of this section stated that
none of the remaining analyses required an experiment; that is no longer true, and the
change is the most important thing this study learned about itself. Transition
controllability rests on a pitching moment that cannot be obtained without a wind tunnel or
an unsteady computational campaign, and the paper declines to substitute a reduced
calculation for it.

What survives independently of that is the framework. The three currencies, the
demonstration that architectural remedies transfer the penalty rather than remove it, the
escape condition, and the finding that architectural comparisons change their ranking with
the sizing contract chosen — none of these depends on whether this particular aircraft is
ever built. meryemAircraft is the case that shows the escape condition can be instantiated
in a real geometry and carried through to reference designs at two scales; it is not
offered as a validated vehicle, and the paper is careful throughout to say which of its
statements are demonstrated, which are conditional, and which are open. The configuration is
described in enough detail for another group to attempt any of the outstanding analyses
independently, and that is the outcome this paper is written to invite.

