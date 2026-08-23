# 3. The architectural tax of hybrid VTOL

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

Hybrid VTOL aircraft work. The argument of this section is not that they do not, but
that they pay for the capability in a way that can be located precisely, that the
payment appears in three different currencies, and that an improvement in one currency
is usually a transfer into another rather than a reduction. The section closes by
stating the condition under which the payment would be zero — a condition none of the
current architectures satisfies, and which Section 4 is built to satisfy.

## 3.1 The root: a duty cycle that does not match the hardware

Every hybrid VTOL aircraft contains hardware whose only purpose is the vertical phase.
That phase is short. For a mission of one hour, a take-off, a transition, a return
transition and a landing occupy on the order of a minute — roughly two percent of the
flight. The remaining ninety-eight percent is spent carrying that hardware through the
air.

This is not an implementation defect and it cannot be engineered away by making the
hardware better, because it is a statement about duty cycle rather than about quality.
A lighter lift rotor is still carried for the whole flight. A cleaner lift rotor is
still carried for the whole flight. The mismatch between how long a component is
needed and how long it is present is the origin of all three bills below.

## 3.2 Bill 1 — mass

The most direct payment is dead mass. A lift-plus-cruise aircraft carries two
propulsion groups: rotors, motors, mounts, wiring and structural reinforcement for the
vertical phase, and a separate propulsor with its own installation for cruise. The
vertical group is inert for the whole cruise, but it is still lifted, and lifting it
consumes energy in proportion to its weight and inversely to the lift-to-drag ratio.

Its cost is also not linear, because mass growth feeds itself. Writing the maximum
take-off mass in terms of the payload and the empty and energy fractions,

    MTOW = m_payload / (1 − f_empty − f_energy)

shows that additional empty mass does not add to MTOW once, but through a multiplier
that grows as the denominator shrinks. In the vertical phase the same increment is
charged again, because hover power scales with weight to the three-halves power:

    P_hover = W^1.5 / (η √(2ρA))

so a mass increment raises the hover power requirement faster than proportionally,
which raises installed power, which raises mass. This is the mechanism by which a
modest dead-mass fraction becomes a large payload penalty.

## 3.3 Bill 2 — drag

The second payment is aerodynamic and is charged only to those architectures that
leave hover hardware exposed in forward flight. Rotors stopped in the airstream, their
booms, and the wake interference between them and the wing all add drag in the regime
where the aircraft spends nearly all of its time.

Published measurements on hybrid VTOL configurations put this cost in a range worth
quoting: rotor-wake interference has been reported to increase drag by twenty to forty
percent in the hybrid regime; retracting or shrouding the lift propellers has been
reported to recover on the order of thirty-eight percent of parasite drag; and at the
upper end of cruise speed the rotor-attributable drag can exceed the form drag of the
wing itself.

*[⚠️ Bu üç sayı ikincil kaynaklardan geldi. Makale son hâline gelmeden birinci elden
okunacak ve tam atıfla verilecek. Okunamazsa sayılar çıkarılıp niteliksel ifadeye
dönülecek — doğrulanmamış sayı vermektense az söylemek yeğdir.]*

The important property of this bill is not its size but where it is charged. It is
charged per unit time in cruise, so it grows with exactly the quantity the aircraft
exists to maximise — range.

## 3.4 Bill 3 — power system sizing

The third payment is the least visible and often the largest. A VTOL aircraft must
install enough power to hover, but it only uses that much power for the two percent of
the flight in which it hovers. The ratio between the two demands follows from the
governing equations rather than from any design choice. Taking hover power from
momentum theory and cruise power from the drag polar,

    P_hover / W  = √(DL / 2ρ) / η_h                 (DL = W/A, disc loading)
    P_cruise / W = V / ( (L/D) η_p )

so that

    P_hover / P_cruise = √(DL / 2ρ) · (L/D) / V · (η_p / η_h)

Every term on the right is a property of the configuration, not of the workmanship. A
vehicle with a disc loading of 100 N m⁻², a cruise lift-to-drag ratio of 15 and a
cruise speed of 30 m s⁻¹ needs roughly four times as much power to hover as to cruise;
raising the disc loading raises the ratio as its square root. The power system is
therefore sized by a condition that holds for a minute and is then carried, unused, for
an hour.

The consequence propagates. Sizing by hover means an oversized engine, or a battery
that must deliver a peak it will rarely be asked for, or both — and whichever of the
two is chosen, the extra installed capacity is mass, which returns to Bill 1.

## 3.5 The bills are one quantity in three currencies

The three bills are not independent problems with three independent fixes. Each known
architectural move reduces one and increases another.

| Move | Bill it attacks | Bill it creates |
|---|---|---|
| Distributed electric lift rotors | 3 — the cruise engine no longer sizes to hover | 1 and 2 — many rotors and mounts, permanently carried and exposed |
| Folding or retracting lift rotors | 2 — the exposed rotor is removed from cruise | 1 — mechanism, actuation, locking, and a new failure mode |
| Tilt-rotor, tilt-wing, tilt-nacelle | 1 — one propulsion group serves both regimes | mechanical complexity, gyroscopic coupling during rotation, and a transition control problem |
| Higher disc loading, smaller rotors | 1 and 2 — smaller, lighter, cleaner rotors | 3 — hover power rises with √(DL) |
| Lower disc loading, larger rotors | 3 — hover power falls | 1 and 2 — larger structure, larger exposed area |

*[Tablo 1 buradan üretilecek.]*

Read as a whole, the table says something stronger than any of its rows. There is a
conserved quantity here: the cost of providing a vertical capability to a wing-borne
aircraft. Architectures do not remove that cost; they choose the currency in which to
pay it. This is why seventy years of engineering effort has improved hybrid VTOL
aircraft considerably without ever producing one whose cruise efficiency matches a
comparable fixed-wing aircraft.

*[⚠️ "Korunumlu nicelik" ifadesi mecazdır, fiziksel bir korunum yasası değildir.
Hakemin ilk saldıracağı cümle budur. Ya "gözlem" diye yumuşatılacak ya da tabloyla
sınırlandırılacak. Bölüm 8'de de tekrar anılmalı.]*

## 3.6 The condition for a zero bill

Stating the tax this way makes its escape condition explicit. The bill exists because
hover and cruise are served by hardware that is not the same hardware, doing the same
job, in the same orientation. Relax any part of that and a bill appears:

- **Different hardware** → Bills 1 and 2. The unused set is carried and, if exposed, drags.
- **Same hardware, different orientation** → the tilting family. The mechanism that changes the orientation is itself mass, complexity and a control problem.
- **Same hardware, same orientation, different sizing point** → Bill 3, unless the hover peak is supplied from somewhere other than the continuous power source.

The condition for paying nothing is therefore that the same propulsors, fixed in the
same orientation relative to the airframe, produce both the hover thrust and the cruise
thrust — with the aircraft itself changing orientation rather than any part of it — and
that the difference between the hover peak and the cruise demand is supplied by a
buffer rather than by permanently installed continuous power.

That is a description of a tail-sitter with a buffered series-hybrid powertrain. It is
also, precisely, the configuration described in Section 4.

## 3.7 Why the market looks the way it does

One observable consequence supports the argument. Hybrid VTOL aircraft occupy a narrow
band of the mission space. Below it, where range requirements are short, a multirotor
is cheaper and simpler and pays none of these bills because it never claimed cruise
efficiency. Above it, where range requirements are long, a runway-launched fixed-wing
aircraft is more efficient and pays none of them because it never claimed vertical
capability. The hybrid sits between the two, and the width of that band is set by how
much cruise efficiency the architecture had to surrender.

An architecture that surrenders less does not merely perform better inside the band. It
widens the band.

*[N60: faydalı yük oranı – menzil düzleminde üç aile. Şekil 12. Referans tasarım
sayıları kesinleştiğinde ayrı sayfada kurulacak.]*
