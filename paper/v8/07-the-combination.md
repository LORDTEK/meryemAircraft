# Step 7 — The combination

**v8 taslağı, birinci yazım.** İskeletin 7. adımı. Yaklaşık 700 kelime.
Grok'un tavsiyesi: *"O sayfayı önce yaz. O sayfa netse v8 tutar."*

**Kural denetimi:** "önceki sürümde" anlatısı yok · menzil iddiası yalnız çok
rotorluya karşı · üçüncü iddia dar, şerit aynı nefeste · "mekanik olarak daha basit"
geçmiyor · *"inşa gereği"* geçmiyor.

---

## The combination

None of the three elements is new.

Tail-sitting aircraft were flown in the 1950s and abandoned for reasons the record
states plainly. Blended wing bodies have been a standing subject of transport research
for three decades. Series-hybrid propulsion is ordinary in small uncrewed aircraft.
Each can be found on its own, in the literature and in hardware.

What is new is that the three of them, taken together, satisfy the escape condition of
Section 3 — and that they satisfy it with no mechanism that reorients a propulsor.

The condition asks for one set of hardware to serve both regimes in one orientation,
with the hover peak drawn from a buffer. Each element supplies one part of it, and none
of them supplies it alone:

- The **blended wing body** carries the cruise lift on a surface, so that cruise is
  wing-borne rather than thrust-borne. That is the second half of the union.
- The **tail-sitting stance** aligns the thrust axis with the body axis, so the single
  propulsor that lifts the aircraft vertically is the same one that drives it in cruise,
  running at its design condition throughout. There is no dedicated lift system to
  carry and no prepared surface to need. That is the first half.
- The **series-hybrid buffer** releases the continuous power plant from the hover peak,
  so that it is sized by cruise rather than by a condition holding for about two percent
  of the flight.

The change of regime is then made by **rotating the airframe**. The propulsors hold
their orientation relative to the body from take-off to cruise; what changes is the
orientation of the body relative to the flight path. A tilting architecture meets the
same condition by turning its propulsors and pays for the turning with a pivot, an
actuator, and a control problem during the turn. Here the same end is reached by turning
the thing the propulsors are already attached to.

That single move is what removes the mechanism. The configuration therefore carries:

| Present in tilting architectures | Present here |
|---|---|
| Pivot or tilting joint | — |
| Nacelle or rotor-group actuator | — |
| Variable-pitch hub | — |
| Gyroscopic moment from a reorienting mass | — |
| Dedicated lift rotors, and the mechanism to stop, index or retract them | — |
| Elevons, rudder, or any trailing-edge control surface | — |

Attitude is produced instead by differential thrust between fixed-pitch propellers: a
single coaxial contra-rotating pair at the nose, and four small coaxial pairs at the
ends of the tip frames, whose moment arms give pitch and yaw directly.

**The claim is narrower than it may appear, and the boundary matters.**

This is not a configuration in which nothing moves. Roll cannot be produced by the
propellers at all: every pair is coaxial and torque-balanced by construction, so every
thrust vector is parallel to the body axis and no combination of settings produces a
rolling moment. Roll is the one axis that requires an aerodynamic device, and that
device is the only moving aerodynamic surface on the aircraft — a variable-extension
strip on the lower surface, modulated rather than switched, which also pitches the nose
down by a small increment when it is deployed. The strip is part of the configuration
and is named here rather than later, because a claim about eliminated mechanisms that
omitted it would be false.

Nor is this a claim of mechanical simplicity. Part count, mass, failure modes and
maintenance burden were not measured, and nothing in this work supports a statement
about reliability. What is offered is a **count**: the classes of mechanism that a
tilting architecture requires to change regime, and which this arrangement does not
require. The actuator inventory that replaces them is the propulsion motors together
with the strip.

What the combination costs is the subject of the sections that follow. It is not free:
the attitude rotors that make the union controllable are themselves exposed in cruise,
and Section 11 charges them.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| Kaçış koşulu: tek donanım, tek yönelim, tampondan tepe | v7 özeti, satır 55 |
| Yatış eşeksenli çiftlerle üretilemez; her itki vektörü gövde eksenine paralel | §2.10, satır 811–813 |
| Şerit "uçaktaki tek hareketli aerodinamik yüzey" | §2.10, satır 815–816 |
| Şerit **modüle ediliyor**, açılıp kapanmıyor | §2.10, satır 818 |
| Şerit burnu aşağı yunuslatıyor | §2.10, ΔC_m 0,005–0,032 |
| Burunda tek eşeksenli karşıt dönüşlü çift, uçlarda dört küçük çift | §2, Şekil 6 ve 8 |
| Askı koşulu uçuşun ~%2'si | v7 özeti |
| Tiltler koşulu pivot ve kontrol problemi bedeliyle karşılıyor | v7 özeti, satır 56–57 |

**Sayı vermediğim yerler bilerek boş:** şeridin boyutları, ΔC_m aralığı ve moment
kolları bu sayfaya girmiyor — 8. adımın (neyden yapıldığı) işi. Bu sayfa **hamleyi**
anlatıyor, envanteri değil.
