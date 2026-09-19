# Round 41 — what you found in step 8, what was done about it, and step 2

---

## 0. Verify what you are reading

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`bf5f732`**.

```
paper/v8/02-the-tax.md             SHA-256 38edd0a279996e5e796fa7d9b01edf9383af0b670db728d5aefce1e1b9caef14
paper/v8/08-what-it-is-made-of.md  SHA-256 a05fc5b0106a127067b1bd0e717fdca6f6099beca9d5b6e0b3439864c812835f
```

The step 8 you reviewed was `69cd2426…`. It has been replaced.

---

## 1. Step 8 — your objections, and what was done

Eight findings. Seven held, one did not. Briefly, each with its fix.

**1. Grok — the energy-path numbers were from the superseded chain. The heaviest finding, and it
was a contradiction between two pages I wrote myself.**
1.9 kW, 2.6 kW, 10.9 kW, 1.8 kg, 3.6 % all follow from propeller efficiency 0.80, which step 7
has already priced at 0.63–0.68. *Fixed:* the figures are now labelled as standing on the
published chain and superseded, pointing to the re-closed set in Section 10. They are kept
because what the architecture needs is the order-of-magnitude ratio between the hover and cruise
requirements, and that ratio survives the correction. Said so explicitly.

**2. ChatGPT and Qwen, independently — "Five propellers, and every one of them is a coaxial
counter-rotating pair" is self-contradictory.**
*Fixed:* "Five propeller stations, each a coaxial counter-rotating pair — ten rotors in all."

**3. DeepSeek — the fairing was missing.**
Checked and correct: the frames are the aircraft's only vertical surfaces and the fairing is
sized against C_n_β > 0.001 per degree, 39 mm chord against the 50–70 mm a 20 mm faired strut
carries anyway. *Fixed:* a paragraph added, with the observation that directional stability here
does not ask for a surface but for a fairing on a frame that is already there.

**4. Qwen — the aircraft had no brain listed.**
Correct, and it matters more than a parts omission: this configuration's stability is not
airframe-borne, so the attitude reference and flight computer are part of the mechanism the
section describes, not optional equipment. *Fixed:* a paragraph, ending on Qwen's own point —
the configuration replaces a pilot's workload with computation, and the computer is the part
that does it.

**5. Grok — where does the engine sit, breathe and exhaust?**
Searched the source: **nothing.** No bay, no intake, no exhaust, no cooling. *Fixed the way you
said to:* stated as not fixed by this study, with the note that a 25 % root thickness has the
volume, and no bay invented.

**6. ChatGPT — "stopped" is not one aerodynamic state.**
Correct. The free-wheeling state is determinate; the stopped state needs the stop produced by
something, and a stopped fixed-pitch blade has an azimuth. *Fixed:* two admissible cruise states
named, only one of them physically closed, and neither the means nor the azimuth claimed.

**7. Grok and ChatGPT both stumbled on the axis naming, and the source is genuinely inconsistent.**
ChatGPT called it an internal contradiction; it is not one, but the source uses earth-frame
naming in one place (*"about the yaw axis in hover"*) and body-frame naming in another
(*"roll-axis authority"*) for the same physical axis. *Fixed:* v8 fixes body-axis naming, says
so in the text, and Qwen's reframing is adopted — the hover residual is stated as an open
control question, not filed as a property of the hardware.

**8. Not accepted — ChatGPT on concentric shafts.**
Two machines stacked on the axis, each driving its adjacent rotor directly, need no nested
shafting, so the claim is defensible for at least one standard implementation. But the paper
does not fix the implementation, so **your narrower version was adopted anyway**: the splitting
gearbox and the mechanical governors are eliminated; no claim is made about shafting.

Smaller, all adopted: *"every part of the planform carries payload"* narrowed (Grok, DeepSeek);
*"yaw is the strongest axis"* reduced to the moment-arm ratio, with authority explicitly not
settled by it (ChatGPT); *"no variable mechanism of any kind"* narrowed to pitch and orientation,
since shaft speed is variable (ChatGPT); *"nominally"* added to the torque balance (ChatGPT);
the per-pair → system gyroscopic inference written out (Qwen); *"beyond the propellers'
rotation"* made explicit (DeepSeek); and transition authority stated as **assigned, not
demonstrated** (ChatGPT).

---

## 2. Step 2 — what was done

All four of you said the same thing about what to write next, and the reason was the same:
steps 7 and 8 both point at an escape condition that does not exist. Grok: *"If only one page
gets written, make it the escape condition."* Qwen: *"load-bearing walls with no foundation."*
ChatGPT's sequence — 2 → 3 → audit 7/8 against 2/3 → 9 — is the one being followed. DeepSeek
argued 3 before 2; the tax is written first because the condition is derived from the transfer
table, and a condition stated before the thing it escapes would have to be taken on trust.

**What the page does.** Six parts: the root (duty-cycle mismatch, two percent against
ninety-eight); Bill 1, mass; Bill 2, drag; Bill 3, power-system sizing; the transfer table with
its one measured row; and a closing part on what the accounting is for.

**Three decisions inside it worth naming.**

*The framework is presented as an instrument, not as a contribution.* That is the Round 35
ruling, and Qwen's test is the one the page was written against — a reader should finish steps
2–4 thinking *"I have been given the tool I need to evaluate what comes next"*, not *"I have
been shown a framework."* So the opening sentence is about what the architectural claim
requires, not about what this paper introduces: *a claim that one architecture escapes a cost
shared by the others is only meaningful if the cost is stated first, in terms that do not
presume the escape.*

*There is not a single number from this aircraft on the page, and that is deliberate.* If the
tax were built with the aircraft in view, the standard against which the escape is measured
would be derived from the thing escaping. The page says so at its foot.

*The NASA lift-plus-cruise finding is used for the thing it actually shows*, which is not that
lift-plus-cruise is bad. It is that the lift-plus-cruise vehicle is **aerodynamically better**
than the alternatives — higher effective lift-to-drag ratio, and the study says so — and is
nevertheless the heaviest, because of hardware carried in order to hover. Bill 1 stated by a
source with no interest in this argument.

The page closes by handing off: the condition is next, derived from the transfer table rather
than from any aircraft; the independent check follows it.

---

## 3. Step 2, first writing

> ### The tax
>
> A claim that one architecture escapes a cost shared by the others is only meaningful if the
> cost is stated first, in terms that do not presume the escape. This section states it. It is
> not a claim about any particular aircraft, and nothing in it is new physics; what it provides
> is the accounting that the rest of the paper is checked against.
>
> ### The root: a duty cycle that does not match the hardware
>
> Every hybrid VTOL aircraft carries hardware whose only purpose is the vertical phase, and that
> phase is short. For a mission of one hour, a take-off, a transition, a return transition and a
> landing occupy on the order of a minute — **roughly two percent of the flight.** The remaining
> ninety-eight percent is spent carrying that hardware through the air.
>
> This is not an implementation defect, and it cannot be removed by making the hardware better,
> because it is a statement about duty cycle rather than about quality. A lighter lift rotor is
> still carried for the whole flight. A cleaner lift rotor is still carried for the whole flight.
> **The mismatch between how long a component is needed and how long it is present is the origin
> of all three charges below.**
>
> ### Bill 1 — mass
>
> The most direct payment is dead mass. A lift-plus-cruise aircraft carries two propulsion
> groups: rotors, motors, mounts, wiring and structural reinforcement for the vertical phase, and
> a separate propulsor for cruise. The vertical group is inert throughout cruise and is lifted
> anyway.
>
> Its cost is not linear. Mass growth feeds itself — MTOW = m_payload / (1 − f_empty − f_energy)
> puts additional empty mass through a multiplier that grows as the denominator shrinks — and in
> the vertical phase the same increment is charged a second time, because hover power scales with
> W^1.5. A modest dead-mass fraction becomes a large payload penalty.
>
> **This charge has been identified independently, and by a source with no interest in the present
> argument.** A NASA study sizing four VTOL architectures against a common mission with common
> tools found the lift-plus-cruise concepts the heaviest of the vehicles examined, and named the
> cause: not the cruise power draw, since the lift-plus-cruise effective lift-to-drag ratio is the
> higher of the set, but *"the extra empty weight items on board in hover."*
>
> **That finding separates the two things this paper is at pains to keep separate.** The
> lift-plus-cruise vehicle is *aerodynamically better* than the alternatives — its cruise
> efficiency is higher, and the study says so — and it is nevertheless the heaviest, because of
> hardware carried in order to hover. That is Bill 1 stated by an independent source in its own
> terms: not a failure of engineering, but the cost of an architecture.
>
> A second NASA review gives the structural half as a general principle, drawn from a tilt-prop
> aircraft whose propeller separated in flight after a gearbox mounting fatigued: to transmit
> power safely to the extremities of the planform, *"very strong (and fatigue-resistant)
> structures must be incorporated with an obvious weight penalty."* Distributing lift or thrust
> across the span therefore obliges the structure that reaches it to keep transmitting power
> there — charged to mass, whether or not the distributed propulsors are running.
>
> ### Bill 2 — drag
>
> The second payment falls only on architectures that leave hover hardware exposed in forward
> flight: rotors stopped in the airstream, the booms that carry them, and the interference between
> their wakes and the wing.
>
> Wind-tunnel work on a hybrid airframe found that the difference between propellers parallel to
> the airflow and no propellers at all is modest, while *"the drag produced by the motors is
> significant."* The bill is charged mainly by the motors and the beams that carry them —
> hardware that cannot be feathered, folded or aligned away, **because its cost is its presence.**
>
> Two further measurements support the direction. Characterisation of a quadplane found the
> highest lift and least drag in fixed-wing mode at both cruise airspeeds, with drag in the hybrid
> regime exceeding either pure mode through adverse flow interaction; and — a point that bears on
> how such aircraft are designed — that a simulation assuming negligible rotor–structure
> interaction *"always predicts higher lift and lower drag than were experimentally observed."*
> Separately, a study of twenty-six stationary lift propellers held edge-on found their drag
> scaling with frontal area and the square of airspeed, with hover powertrain components adding
> *"a significant amount of aerodynamic drag during forward flight"* in the absence of a stowing
> mechanism.
>
> **The important property of this charge is not its size but where it falls.** It is charged per
> unit time in cruise — so it grows with exactly the quantity the aircraft exists to maximise.
>
> ### Bill 3 — power system sizing
>
> The third payment is the least visible and often the largest. A VTOL aircraft must install
> enough power to hover, but it draws that power only during the two percent of the flight in
> which it hovers. The ratio between the two demands follows from the governing equations rather
> than from any design choice. Taking hover power from momentum theory and cruise power from the
> drag polar,
>
>     P_hover / W  = √(DL / 2ρ) / η_h                 (DL = W/A, disc loading)
>     P_cruise / W = V / ( (L/D) η_p )
>
> so that
>
>     P_hover / P_cruise = √(DL / 2ρ) · (L/D) / V · (η_p / η_h)
>
> **Every term on the right is a property of the configuration, not of the workmanship.** A
> vehicle with a disc loading of 100 N m⁻², a cruise lift-to-drag ratio of 15 and a cruise speed
> of 30 m s⁻¹ needs roughly four times as much power to hover as to cruise, and raising the disc
> loading raises the ratio as its square root. The prediction is borne out in flight: a
> carbon-fibre tail-sitter reported in the literature measures its level-flight power consumption
> at one fifth of its hover power, which is the ratio this expression gives for an aircraft of
> that class.
>
> The power system is therefore sized by a condition that holds for a minute and is then carried,
> unused, for an hour. And the consequence propagates: sizing by hover means an oversized engine,
> or a battery that must deliver a peak it will rarely be asked for, or both — and whichever is
> chosen, the extra installed capacity is mass, which returns to Bill 1.
>
> ### The three are one quantity in three currencies
>
> The three charges are not independent problems with independent fixes. **Each known
> architectural move reduces one and raises another.**
>
> | Move | Bill it attacks | Bill it creates |
> |---|---|---|
> | Distributed electric lift rotors | 3 — the cruise engine no longer sizes to hover | 1 and 2 — many rotors and mounts, permanently carried and exposed |
> | Folding or retracting lift rotors | 2 — the exposed rotor is removed from cruise | 1 — mechanism, actuation, locking, a new failure mode |
> | Tilt-rotor, tilt-wing, tilt-nacelle | 1 — one propulsion group serves both regimes | mechanical complexity, gyroscopic coupling, a transition control problem |
> | Higher disc loading, smaller rotors | 1 and 2 — smaller, lighter, cleaner rotors | 3 — hover power rises with √(DL) |
> | Lower disc loading, larger rotors | 3 — hover power falls | 1 and 2 — larger structure and exposed area |
>
> **One of these rows has been measured, and the measurement is worth more than the table.** In
> the wind-tunnel study cited above, a retraction system removed thirty percent of the airframe's
> drag; the same author then costed it. Applied to a passenger eVTOL, with the mechanism assessed
> at five percent of vehicle mass, maximum range rose from 119 km to 121 km — **a two-kilometre
> gain for a five-percent mass penalty.** Bill 2 was converted almost exactly into Bill 1, and
> **the transfer is the point rather than the small residue.**
>
> ### What this accounting is for
>
> Stated this way, the tax has a property that makes it useful rather than merely descriptive:
> **it is falsifiable at the level of an architecture.** If some arrangement pays none of the
> three, the accounting says where to look for the payment it makes instead; if it pays one
> heavily to escape another, the accounting predicts which comparisons will reverse when the
> sizing rule changes.
>
> That is what the remainder of this paper uses it for. The next section states the condition
> under which the three are not charged — a definition, derived from the table above rather than
> from any aircraft — and the section after it tests one consequence of the accounting against a
> sizing study this work did not produce.
>
> ---

---

## 4. What I am asking of you

**Q1 — Does the tax stand on its own?** A referee who stops at the end of this section should
be able to state the three charges, say why they are coupled, and say what would falsify the
accounting — without having seen the aircraft. Can they?

**Q2 — Is it an instrument or a contribution, as written?** Qwen's test. If the page reads as
"here is our framework", say where.

**Q3 — Is the transfer table complete enough?** Five rows. A referee who works on VTOL will
have a sixth in mind. Which one, and does its absence weaken the claim that the moves transfer
rather than cancel?

**Q4 — Anything false.** Every round this has produced findings.

**Q5 — Step 3 next, the escape condition, then the audit of 7 and 8 against 2 and 3.** Unless
one of you thinks the order changed now that step 2 exists.

---

## 5. Where the work stands

Three of fourteen steps written: 2, 7, 8. The architecture is unchanged since the skeleton
locked. Target remains *Journal of Aircraft* (AIAA), Full-Length Paper.
