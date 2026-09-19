# Step 7 — The combination

**v8 taslağı, birinci yazım.** İskeletin 7. adımı. Yaklaşık 700 kelime.
Grok'un tavsiyesi: *"O sayfayı önce yaz. O sayfa netse v8 tutar."*

**Kural denetimi:** "önceki sürümde" anlatısı yok · menzil iddiası yalnız çok
rotorluya karşı · üçüncü iddia dar, şerit aynı nefeste · "mekanik olarak daha basit"
geçmiyor · *"inşa gereği"* geçmiyor.

**İkinci yazım, Tur 35 sonrası.** Dört dış okuyucunun bulduğu beş kusur düzeltildi:
tiltin koşulu *sağladığı* iddiası (DeepSeek — §2.6 tam tersini söylüyor), *"single
propulsor ... design condition throughout"* (Grok ve ChatGPT — §3.15 burun çiftinin tek
başına kalkamadığını söylüyor), tablo başlığının bütün tiltlere genellenmesi (ChatGPT ve
Qwen bağımsız olarak), gyroskopik momentin mekanizma sayılması (ChatGPT — bir etki,
mekanizma değil; düzyazıya taşındı), ve kalkış marjı bağımlılığının sayfada hiç
geçmemesi (Grok).

---

## The combination

None of the three elements is new.

Tail-sitting aircraft were flown in the 1950s and abandoned for reasons the record
states plainly. Blended wing bodies have been a standing subject of transport research
for three decades. Series-hybrid propulsion is ordinary in small uncrewed aircraft.
Each can be found on its own, in the literature and in hardware.

What is new is that the three of them, taken together, satisfy the escape condition of
Section 3 — and that they satisfy it with no mechanism that reorients a propulsor. The
assembly is not new because it is an assembly. It is new because of what it satisfies, and
because of what it does not need in order to satisfy it.

The condition asks for one set of hardware to serve both regimes in one orientation,
with the hover peak drawn from a buffer. Each element supplies one part of it, and none
of them supplies it alone:

- The **blended wing body** carries the cruise lift on a surface, so that cruise is
  wing-borne rather than thrust-borne. That is the second half of the union.
- The **tail-sitting stance** aligns the thrust axis with the body axis, so the propulsor
  that produces the vertical thrust is the same one that produces the cruise thrust, holding
  one orientation relative to the airframe throughout. There is no dedicated lift system to
  carry and no prepared surface to need. That is the first half.
- The **series-hybrid buffer** releases the continuous power plant from the hover peak,
  so that it is sized by cruise rather than by a condition holding for about two percent
  of the flight.

The change of regime is then made by **rotating the airframe**. The propulsors hold
their orientation relative to the body from take-off to cruise; what changes is the
orientation of the body relative to the flight path. A tilting architecture reaches the
same end by turning its propulsors instead, and pays for the turning with a pivot, an
actuator, a gyroscopic moment from the reorienting mass, and a control problem through the
turn. It does not satisfy the condition as stated: the condition requires one orientation
relative to the airframe, and turning the propulsors is the case the condition excludes.
Here the end is reached by turning the thing the propulsors are already attached to, which
leaves the orientation requirement intact.

That single move is what removes the mechanism. The configuration therefore carries:

| Mechanism | Where it is required | Present here |
|---|---|---|
| Pivot or tilting joint | Tilting architectures | — |
| Nacelle or rotor-group actuator | Tilting architectures | — |
| Variable-pitch hub | Where one propulsor must be trimmed across two widely separated operating points | — |
| Dedicated lift rotors, and the mechanism to stop, index or retract them | Lift-plus-cruise architectures | — |
| Elevons, rudder, or any trailing-edge control surface | Conventional and blended-wing-body practice | — |

Attitude is produced instead by differential thrust between fixed-pitch propellers: a
single coaxial contra-rotating pair at the nose, and four small coaxial pairs at the
ends of the tip frames, whose moment arms give pitch and yaw directly. The tip pairs are
sized from the moment requirement rather than from weight support, but the thrust that sizing
gives them also supplies the aircraft's entire take-off margin, because the nose pair is sized
at thrust equal to weight and no more. That is the one place the configuration asks a component
to do a second job it was not sized for; it is a dependency, it is reported as one where the
sizing is audited, and it does not make the tip pairs a lift system.

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
| Tiltler koşulu **sağlamaz**; "aynı donanım, farklı yönelim" bir fatura doğurur | §2.6, satır 672–674 |
| Tilt bedeli: pivot, aktüatör, gyroskopik moment, geçiş kontrol problemi | §2.6 tablosu satır 659; ayrıca satır 463 |
| Burun çifti T/W = 1,00 tam, fazlası yok; kalkış marjı uçlardan | §3.15, satır 2624–2626 |
| Uç çiftleri moment gereğinden boyutlandırıldı, ağırlık taşımaktan değil | §3.2, satır 1150–1151 |
| "Sızdırılmadığı için sorulmayan bir ikinci iş" — tek yer | §2.7, satır 706–708 |
| Şerit alt yüzeyde, planformda 45°, kök veterinin %120'si — firar kenarı aygıtı DEĞİL | §2.10, satır 816–818 |

**Sayı vermediğim yerler bilerek boş:** şeridin boyutları, ΔC_m aralığı ve moment
kolları bu sayfaya girmiyor — 8. adımın (neyden yapıldığı) işi. Bu sayfa **hamleyi**
anlatıyor, envanteri değil.
