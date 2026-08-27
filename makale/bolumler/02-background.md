# 2. Background: seventy years of attempts

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

The configuration proposed in this paper is new, but the problem it addresses is not,
and neither are several of its ingredients. This section reviews the attempts that
preceded it. The purpose is not to establish priority but to establish two things: that
the need has been pursued continuously for seventy years, and that the pursuit was
rarely abandoned because the aerodynamics failed.

## 2.1 Removing the fuselage

The idea that a transport aircraft should carry its payload inside a lifting surface
rather than inside a cylinder is as old as the transport aircraft itself. Burnelli's
lifting-fuselage designs, flown in a succession of prototypes from the 1920s to the
1940s, placed cabin and cargo inside a thick aerofoil-shaped centre body that
contributed lift instead of only drag. The aircraft flew, and flight testing did not
report an aerodynamic deficiency that would have disqualified the layout. They never
entered series production, and the reasons usually offered are procurement and
commercial, not aerodynamic.

The Northrop XB-35 carried the same idea to its limit: a bomber with no fuselage and
no tail at all. Its programme is often cited as evidence that the flying wing was
premature. The record is more specific than that. The XB-35's persistent failures were
in its power transmission — the contra-rotating propeller gearboxes, drive shafts and
governors — and the aircraft was eventually flown with single-rotation propellers at a
measurable performance cost. The wing was not the part that failed. This distinction
is directly relevant to the present work, and Section 4.3 returns to it: the
configuration proposed here uses counter-rotating propellers but never builds a
contra-rotating gearbox, because each rotor of a pair is driven by its own electric
machine.

Vought's V-173 and XF5U pursued the opposite extreme of the same intuition — a wing of
very low aspect ratio with large propellers at the tips, intended to work against the
tip vortices. The V-173 flew roughly two hundred times and supported the low-speed
claims made for it. The XF5U was completed and never flown; the programme ended as the
services moved to jet propulsion.

The recurring pattern is worth stating plainly: in each case the aircraft flew, the
configuration was not disqualified in flight, and the programme ended for a reason
that came from outside the configuration.

## 2.2 Standing the aircraft on its tail

The tail-sitter is the most direct answer to the runway. If the aircraft can point its
thrust line at the ground, it needs no separate lift system, no tilting mechanism and
no second propulsion group — the same propeller that cruises also hovers. Two American
prototypes flew this idea in 1954.

The Lockheed XFV-1 never completed the cycle it was built for. Its intended engine was
not delivered, and the aircraft flew with a lower-powered substitute and a temporary
conventional undercarriage; it made transitions in flight but never a full vertical
take-off. It was cancelled with the question it was built to answer still unanswered.

The Convair XFY-1 did answer it. In November 1954 it took off vertically, transitioned
to horizontal flight, transitioned back, and landed vertically. The concept was
demonstrated. What ended the programme was the landing: the pilot had to descend
backwards, judging his height above the ground by looking over his shoulder, with no
useful cue when he needed one most. The workload was judged to be beyond what an
average operational pilot could sustain, and the aircraft was cancelled.

This is the single most important fact in this section. The XFY-1 was not defeated by
its aerodynamics, its propulsion or its structure. It was defeated by a constraint
located entirely in the cockpit — and an uncrewed aircraft does not have one. A
vertical descent judged by sensors rather than by a pilot's neck is a different
problem, and the argument that closed the tail-sitter in 1956 does not close it now.

## 2.3 Distributing sweep along the span

The proposed planform varies its sweep angle continuously from root to tip. The
principle is not new. The crescent wing of the Handley Page Victor distributed sweep,
chord and thickness together across the span, in panels of decreasing sweep outboard,
so that the critical Mach number stayed approximately constant along the wing instead
of being set by its most vulnerable station.

The present aircraft is subsonic by design and does not inherit the Victor's transonic
motivation. What it inherits is the structural idea: sweep, chord and thickness are one
distribution, not three independent choices. Section 4.2 states the sweep values used
here, and Section 8 states plainly that they were chosen rather than derived.

## 2.4 The contemporary hybrids

The problem did not go away when the prototypes did. Since roughly 2010 a large family
of hybrid VTOL uncrewed aircraft has reached service, in two dominant architectures.
Lift-plus-cruise aircraft carry a set of rotors for the vertical phase and a separate
propulsor for cruise, and fly as a fixed-wing aircraft in between. Tilting
architectures — tilt-rotor, tilt-wing and tilt-nacelle — reuse the same propulsors in
both regimes by rotating them.

Both work. Both are in operational use. This paper does not claim otherwise, and
Section 6.5 places the proposed reference designs alongside them without ranking them.
What Section 3 argues is that each of these architectures pays for its capability in a
way the other does not, that the payment can be moved between mass, drag and power
system sizing, and that it cannot be brought to zero as long as hover and cruise are
served by different hardware or by hardware that must move between two roles.

## 2.5 What this history does and does not show

It would be too convenient to declare that every one of these programmes ended for
reasons external to its configuration. Some of the difficulties were real and internal,
and this paper inherits them. The tail-sitter's vertical descent is genuinely harder
than a runway landing. A tail-sitting aircraft is more exposed to crosswind on the
ground than a conventional one. And a set of propellers whose thrust vectors are all
parallel to the body axis cannot, by construction, produce a rolling moment — a
limitation that applies to this configuration exactly as it applied to its
predecessors, and which Section 4.4 addresses rather than avoids.

What the history does show is that the concept was never given a fair verdict under
present-day conditions. The programmes of the 1950s were closed by engine deliveries,
by jet-era procurement priorities, by gearboxes, and by the limits of a human pilot in
a vertical descent. Of those four, three are historical accidents and the fourth is
absent in an uncrewed aircraft. What is available now that was not available then —
electric drive on each rotor, sensor-based attitude reference, and enough onboard
computation that stability need not come from the airframe alone — removes exactly the
obstacles that stopped it.

What the history does not settle is why the contemporary aircraft that did succeed still
pay for their vertical capability, and what exactly they pay. That is the subject of the
next section.
