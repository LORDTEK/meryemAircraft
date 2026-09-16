# Round 7 — the paper as it now stands, and a decision about where to send it

**Please be blunt.** The author is choosing where to spend a year, and has
asked that no answer be softened to encourage him. If your view is that
this cannot reach a Q1 journal, say so and say why.

This text has three parts: what changed since round 6 (so that we are all
looking at the same manuscript), the title, and the journal decision —
which we would like to settle in this round rather than iterate on.

---

# 1. What changed since round 6

You were unanimous that the paper was written as a vehicle study while its
strongest content was a framework. That has now been done. Four changes,
plus one finding that came out of doing them.

## 1.1 Title — applied

Now: **The Architectural Cost of Hybrid VTOL: meryemAircraft, a
Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated Lift
System.**

This merges your three inputs: "Architectural Cost" and "Propeller-Driven"
from one of you, dropping "Configuration" from the other two, and "Without
a Dedicated Lift System" which all three endorsed. "Propeller-Driven"
serves the author's original reason for the word — the study excludes jet
propulsion — without asserting anything that needs proving. The name
meryemAircraft is a fixed constraint.

## 1.2 The framework is now the primary contribution

The abstract opens on the framework, presents the sizing-contract result as
a *methodological contribution* rather than as an outcome, and introduces
the aircraft as the case study. The Contributions list was rewritten from
scratch — the old one predated every calculation of the past week and
mentioned none of them — and now reads: (1) the three-currency framework
and escape condition; (2) contract-dependence of architectural comparison,
stated as a result independent of any aircraft; (3) the configuration as an
instantiation; (4) computational support; (5) what is not established,
written as a testable requirement. It closes: *"Items 1 and 2 stand
independently of whether this particular aircraft is ever built."*

The conclusion now ends on what survives without the vehicle. It also
corrected a sentence that had become false: it used to say that none of the
remaining analyses required an experiment.

## 1.3 Absolutist language removed

Section 5 was titled "How the architectural tax is avoided"; it is now "The
architectural tax, audited bill by bill". The bill headings were "not
paid", "mostly not paid", "not paid" — inconsistent among themselves. They
are now "the charge does not arise", "reduced, not removed", and "avoided
for the engine, not for the electrical path". The introduction's "none of
the three penalties is incurred" now reads "none of the three penalties **as
defined in Section 3** arises… That is a statement about three specific
charges, not a claim that the configuration is free." Section 3.6 now says
the term *zero-bill condition* must be read strictly.

## 1.4 A charge we had not admitted

Auditing our own language turned up something the mass budget knew and the
text did not. The buffered series hybrid releases the **engine** from the
hover condition, but not the **electrical path**: the nose motor and power
electronics must still pass the full 10.9 kW. Our own component build-up
lists them at 2.73 kg and 0.61 kg against 2.60 kg of engine and generator —
the hover-sized electrical machine is the largest single item in the
propulsion chain. Section 5.3 now says so. The buffer also carries a
condition we had not stated: it is specified by power, not energy, at
4.6 kW kg⁻¹, which is a demanding cell requirement.

## 1.5 The finding that changed the open item

This is the one we would most like you to attack.

Our threshold for the aerodynamic pitching moment was computed at a single
representative airspeed, which made us ask: *what is C_m through ninety
degrees of incidence?* Resolving it along the paper's own transition
trajectory instead — no new physics, the existing point-mass simulation —
shows the question was wrong.

**The aircraft does not reach ninety degrees of incidence.** The body
rotates through ninety, but the relative wind rotates with it, because the
aircraft is accelerating and climbing at the same time.

| | entry | peak incidence | airspeed there | C_m budget there | tightest budget |
|---|---|---:|---:|---:|---|
| Light | 5 m s⁻¹ climb | 17.5° | 7.3 m s⁻¹ | 0.322 | 0.079 at rotation end, α = 4.9°, 14.7 m s⁻¹ |
| Light | from rest | 21.6° | 2.8 m s⁻¹ | 2.174 | 0.080 at rotation end |
| Heavy | from rest | 20.5° | 6.8 m s⁻¹ | 0.404 | 0.015 at rotation end, α = 6.5°, 35.4 m s⁻¹ |

The constraint splits in two. **Mid-rotation** the incidence is high but the
dynamic pressure is low, and the budget is 0.32 or more — at or above the
upper end of published post-stall values. **At rotation end** the incidence
is small and the speed is high, and the budget is 0.079 or 0.015; but that
is not a post-stall problem, it is the ordinary trim question of a tailless
aircraft at cruise incidence, which is a centre-of-gravity matter every
tailless design must settle anyway.

So the outstanding requirement is now (a) pitching moment to about
twenty-two degrees at low dynamic pressure — mildly post-stall, much closer
to existing data — and (b) trim at cruise. Not a ninety-degree sweep.

Two limits are stated in the text: the incidence history is only as good as
the point-mass trajectory it comes from, and the rotation rate itself varies
local incidence along the body by ±3.1° (entered in a climb) to ±8.6° (from
rest), so in the second case parts of the airframe see close to thirty
degrees.

**Question 1.5.** Is this reasoning sound, or are we now under-stating the
problem as badly as we were over-stating it? It moved in the direction we
wanted, which is exactly when we would like to be checked.

---

# 2. The title

**Question 2.** Does anything about the new title trouble you? It is long.
"Architectural Cost" now matches a genuinely framework-first manuscript
rather than promising one, but you should judge whether the body delivers
what the title claims.

---

# 3. The journal — we would like to settle this now

The author's preference has narrowed to two: **Aerospace Science and
Technology** and **Drones**, and he is genuinely torn between them. Rather
than iterate, we would like your judgement in this round.

**What we found about Drones.** We checked its Aims & Scope directly. The
relevant sentence:

> "The manuscript submitted must clearly and directly address topics related
> to unmanned platforms. If the manuscript is dealing with general
> theoretical aircraft design, **it is recommended** to validate the
> theoretical/numerical results with experimental data from a study of an
> unmanned platform, at least at a laboratory scale."

Two observations. It says *recommended*, not required — one of you
presented this as a harder rule than the page states. And the trigger is
"general theoretical aircraft design", which is arguable: our aircraft is a
specific uncrewed platform, so the first sentence is comfortably satisfied,
but a reviewer could reasonably place the paper in the second category. The
topic lists match us well — airframe and structural design, power supply,
control system, performance, autonomous take-off and landing, and
applications in forestry, logistics and disaster assistance. There is also a
dual-use clause; the manuscript contains no military framing.

**Question 3a.** Given that exact wording, is Drones a realistic home for
this paper, or does that clause make it a worse fit than Aerospace Science
and Technology despite the topical match?

**Question 3b.** If you had to choose one for a first submission, which, and
what is the expected cost of being wrong — months lost, or a usable set of
reviews?

---

# 4. The question the author most wants answered

He has asked us to put this to you directly and without diplomacy.

**Question 4a.** Is there a realistic path by which this work reaches a
level where a Q1 journal would accept it **without major revision** — and
if so, what specifically would have to be true that is not true today? We
recognise that acceptance without revision is rare anywhere; what we are
asking is whether the *substance* could reach that level, or whether the
missing experiment permanently caps this manuscript at "major revision at
best".

**Question 4b.** If the honest answer is that a Q1 acceptance requires an
experiment, please say it plainly. The author would rather redirect his
effort toward a low-cost measurement — a powered model, a tunnel test of the
pitching moment to twenty-two degrees — than spend a year in submission
queues. Knowing that now is worth more to him than an encouraging estimate.

**Question 4c.** And the converse, which we would not want to miss: with the
framework now foregrounded, is there a reading on which this paper is
*stronger* than we are treating it — where the contribution is the
architectural accounting method and the aircraft is an illustration, and the
missing transition measurement is therefore a limitation of the illustration
rather than of the contribution?
