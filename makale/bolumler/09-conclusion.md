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
a strip on the lower surface closes the one gap that propellers cannot — the rolling
moment, which parallel thrust vectors cannot produce at any thrust setting or mounting
position. There are no elevons, no rudder, no tilting mechanism, no retraction mechanism
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
away.

Two results emerged during the study that changed it. The tip frames, if left as
circular tubing, would produce nearly as much drag as the entire rest of the aircraft;
fairing them is not an option but a requirement, and it is also what makes their tip
surfaces available as lifting surfaces at no additional part or mass. And the transition
does not behave as commonly assumed: a slower rotation loses *less* altitude, not more,
because the aircraft is supported during the manoeuvre rather than falling through it —
so entering the rotation while still climbing, rather than stopping to hover first,
removes the altitude penalty entirely.

What this paper offers is a configuration and its numbers, not a validated aircraft.
There is no wind-tunnel data here, no computational fluid dynamics, and no flight test;
the mass budget is a target that has not paid the margin such budgets usually owe. The
claims most exposed to that are identified in Section 8, together with the four analyses
that would test them, none of which requires an experiment. The configuration is
described in enough detail for another group to attempt any of them independently, and
that is the outcome this paper is written to invite.

