# 2. Background: seventy years of attempts

The configuration proposed in this paper is new, but the problem it addresses is not,
and neither are several of its ingredients. This section reviews the attempts that
preceded it. The purpose is not to establish priority but to establish two things: that
the need has been pursued continuously for seventy years, and that the pursuit was
rarely abandoned because the aerodynamics failed. Figure 2 places the programmes
discussed below on a single timeline, with the recorded reason each one stopped.

## 2.1 Removing the fuselage

The idea that a transport aircraft should carry its payload inside a lifting surface
rather than inside a cylinder is as old as the transport aircraft itself. Burnelli's
lifting-fuselage designs, flown in a succession of prototypes from the 1920s to the
1940s, placed cabin and cargo inside a thick aerofoil-shaped centre body that
contributed lift instead of only drag. The aircraft flew, repeatedly and over two
decades. They never entered series production. The reasons for that are outside the
scope of this paper and are disputed; what matters here is only that the layout was
flown rather than merely proposed, and was not abandoned at the drawing board.

The Northrop XB-35 carried the same idea to its limit: a bomber with no fuselage and
no tail at all. Its programme is often cited as evidence that the flying wing was
premature. Whatever weight that reading deserves, the aircraft's best-documented
difficulties lay in its power transmission rather than in its aerodynamics: the
contra-rotating propellers were driven through remote gearboxes and long extension
shafts, and were eventually changed to single-rotation units. The distinction between an
airframe and the machinery installed in it matters for the present work, and Section 4.3
returns to it — the configuration proposed here uses counter-rotating propellers but
never builds a contra-rotating gearbox, because each rotor of a pair is driven by its own
electric machine on a common axis.

Vought's V-173 and XF5U pursued the opposite extreme of the same intuition — a wing of
very low aspect ratio with large propellers at the tips, intended to work against the
tip vortices. The V-173 flew roughly two hundred times and supported the low-speed
claims made for it. The XF5U was completed and never flown; the programme ended as the
services moved to jet propulsion.

The recurring pattern is worth stating plainly: in each case the aircraft flew, the
configuration was not disqualified in flight, and the programme ended for a reason
that came from outside the configuration.

## 2.2 Standing the aircraft on its tail

The tail-sitter is the most direct answer to the runway: if the aircraft points its thrust line
at the ground it needs no separate lift system, no tilting mechanism and no second propulsion
group. Two American prototypes flew this idea in 1954. The Lockheed XFV-1 never completed the
cycle — its "highly tapered, straight-wing design made the transition to vertical flight only at
altitude, using a jury-rigged, landing-gear cradle for conventional takeoff and landings" [1,2].
The Convair XFY-1 did: it flew vertically in August 1954 and "six transitions to conventional
flight were successfully completed" [2].

**Why the programme stopped matters, because the usual account is wrong.** Two NASA reviews of
United States V/STOL development — one written largely from the author's own flight-test
experience [1] — judge the configuration itself favourably: "good configuration arrangement for
low- and high-speed compatibility", with a high-speed potential near 500 mph. What they judge
poorly is the machinery and the cockpit around it: "poor mechanical control system features
including low actuator response rate"; "difficult to hover precisely over a spot"; "tip-over
tendencies noted when on ground in gusty air" [1]. The landing difficulty is attributed to "the
unusual spatial orientation where the pilot looked over his shoulder and down", to "the
sensitivity to atmospheric turbulence", and to "reduced control power near touchdown" [2].

And then the reason testing ended, stated the same way in both:

> "Six transitions to conventional flight were successfully completed **before testing was
> curtailed because of engine and gear-box reliability problems**." [2]

The XFY-1 was not stopped by pilot workload. The workload was real, separately documented and
severe — but what curtailed the testing was mechanical. **Three of the four objections recorded
against these aircraft are objections to 1954 machinery and to a human pilot, not to the
configuration**: actuator response rate, gearbox reliability, and an orientation problem that
exists only because someone is sitting in it. Section 2.5 returns to what that leaves.

## 2.3 Distributing sweep along the span

The proposed planform varies its leading-edge sweep continuously from root to tip while
holding the trailing edge at a constant angle. The principle of treating sweep, chord and
thickness as one coupled distribution rather than three independent choices is not new;
the crescent wing of the Handley Page Victor is its best-known expression, its sweep
decreasing outboard so that the wing was not governed by its most vulnerable station.

The present aircraft is subsonic and does not inherit the transonic motivation that
produced that planform. What it takes is the structural idea alone, and it takes it in a
much reduced form: as Section 4.2 records, the sweep variation actually realised here is
under seven degrees. No claim of descent from the crescent wing is made, and none is
needed. Section 4.2 states the values used, and Section 8 states plainly that they were
chosen rather than derived.
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
jet-era procurement priorities, and — in the case where two contemporary NASA reviews
record the reason directly and identically — by engine and gearbox reliability [1,2]. Not
one of them was closed because the configuration failed to fly; one of the reviews rates
the configuration itself favourably while condemning the machinery around it [1]. The
human pilot, whose difficulties are the best-documented part of the record, is the single
constraint that an uncrewed aircraft removes entirely. What is available now that was not available then —
electric drive on each rotor, sensor-based attitude reference, and enough onboard
computation that stability need not come from the airframe alone — removes exactly the
obstacles that stopped it.

What the history does not settle is why the contemporary aircraft that did succeed still
pay for their vertical capability, and what exactly they pay. That is the subject of the
next section.
