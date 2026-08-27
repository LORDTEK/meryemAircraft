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

The Convair XFY-1 did answer it. It first flew vertically in August 1954 and made six
transitions to conventional flight from November of that year. The concept was
demonstrated.

What the aircraft was actually like to fly is recorded in a NASA review of V/STOL
technology whose author states that most of its content came from first-hand flight-test
experience [1]. Its assessment of the XFY-1 is worth reading in full, because it is more
interesting than the summary usually given. The configuration itself is judged
favourably — "good configuration arrangement for low- and high-speed compatibility",
with a high-speed potential of about 500 mph. What is judged poorly is everything
surrounding it: "poor mechanical control system features including low actuator response
rate"; "difficult to hover precisely over a spot"; "tip-over tendencies noted when on
ground in gusty air"; "gust sensitivity bothersome to pilot during takeoff and landing
phases"; and, on the manoeuvre this paper cares about most, "precision of flightpath
control in landing approach poor because of unusual spatial orientation situation".

The same entry records "very high pilot workload during low-speed operation", and then
states the reason the programme stopped: **"testing curtailed because of engine and
gearbox reliability problems."**

That last sentence deserves emphasis, because it corrects the account usually given —
including an earlier draft of this paper. The XFY-1 was not stopped by the pilot
workload. The workload was real, separately documented, and severe; but what curtailed
the testing was mechanical reliability in the engine and the gearbox. The tail-sitter of
1954 shares its cause of death with the XB-35 and the XFV-1: **the powerplant and its
transmission, not the configuration.**

The pilot workload matters for a different reason. It is the one item on that list that
an uncrewed aircraft removes outright. "Unusual spatial orientation" is a statement
about a human being in a cockpit; a vehicle whose attitude reference is an inertial
measurement unit and whose height above ground is a sensor reading does not have an
unusual spatial orientation, because it has no orientation to be disoriented in. Of the
difficulties the XFY-1 recorded, that one simply does not transfer.

The others do transfer, and this paper does not pretend otherwise. Tip-over tendencies
in gusty ground wind, difficulty in holding a precise hover, and gust sensitivity during
take-off and landing are properties of standing an aircraft on its tail, not properties
of having a pilot. Section 8 treats them as inherited rather than solved.

*A similar assessment of another tail-sitter in the same review — the Ryan X-13 — reaches
the same place from a different direction: "precision of flight-path control poor due in
part to pilot visibility limitations in vertical hover mode."*

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
present-day conditions. The programmes of the 1950s were closed by engine deliveries, by
jet-era procurement priorities, and — in the one case where a contemporary NASA
assessment records the reason directly — by engine and gearbox reliability. Not one of
them was closed because the configuration failed to fly. The human pilot, whose
difficulties are the best-documented part of the record, is the one constraint that an
uncrewed aircraft removes entirely. What is available now that was not available then —
electric drive on each rotor, sensor-based attitude reference, and enough onboard
computation that stability need not come from the airframe alone — removes exactly the
obstacles that stopped it.

What the history does not settle is why the contemporary aircraft that did succeed still
pay for their vertical capability, and what exactly they pay. That is the subject of the
next section.
