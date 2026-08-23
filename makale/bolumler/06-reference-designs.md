# 6. Reference designs at two scales

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

A configuration argument is only as good as its willingness to become a number. This
section sizes two aircraft from the arrangement of Section 4 — one at 50 kg and one at
1000 kg, a factor of twenty apart in mass — using the same equations, the same
assumptions and the same architecture. The two points are not a light version and a
heavy version of different aircraft. They are the same aircraft at two sizes, and the
purpose of presenting both is to show that the proportions hold.

Every number below is calculated, not measured. Section 8 says what that means.

## 6.1 Sizing method

The method is deliberately elementary, and the equations are given so that any result
in this section can be checked by hand.

**Hover.** Thrust equals weight, and induced power follows from momentum theory:

    v_i = √(T / 2ρA)          P_i = T^1.5 / √(2ρA)

with the disc loading DL = T/A as the governing parameter. Figure of merit is applied
to obtain shaft power.

**Cruise.** Lift equals weight, drag follows from the polar, and the lift-to-drag ratio
is estimated from aspect ratio and zero-lift drag:

    L/D ≈ 0.5 √(π · AR · e / C_D0)

**Range.** The series-hybrid chain is stated explicitly rather than folded into a
single efficiency, because the result is sensitive to it and a reader should be able to
disagree with any single link:

| Link | Value |
|---|---:|
| Internal-combustion engine | 0.28 |
| Generator | 0.90 |
| Power electronics | 0.95 |
| Electric machine | 0.92 |
| Propeller | 0.80 |
| **Overall** | **0.176** |

Fuel energy is taken as 12.9 kWh kg⁻¹. The engine figure is the one that matters most:
0.28 is representative of a small four-stroke engine at its best operating point, and
it is the reason the range figures below are lower than an optimistic estimate would
give.

**Control.** Tip-pair thrust follows from the required angular acceleration,
M = 2 T L = I α, with the transition manoeuvre as the sizing case.

**Assumptions carried throughout:** sea-level density; no compressibility; span
efficiency e assumed rather than computed; C_D0 assumed at 0.0248 for the light
design, which is generous for a clean blended-wing body and is intended to absorb the
tip-frame contribution of Section 5.2 — that contribution is 0.0043, or seventeen
percent of the assumed C_D0, so the assumption is self-consistent rather than
optimistic.

## 6.2 Light reference design — 50 kg

| Quantity | Value |
|---|---:|
| Maximum take-off mass | 50 kg |
| Root chord | 0.97 m |
| Tip chord | 0.238 m |
| Span | 3.45 m |
| Wing area | 1.98 m² |
| Aspect ratio | 6.00 |
| Wing loading | 25.3 kg m⁻² |
| Main propeller diameter | 1.20 m |
| Disc loading | 44.2 kg m⁻² |
| Tip propeller diameter | 0.20 m |
| Frame post length | 0.71 m each direction |
| Stall speed | 20.1 m s⁻¹ |
| Cruise speed | 30 m s⁻¹ (108 km h⁻¹) |
| Cruise L/D | 12.7 |
| Hover power | 10.9 kW |
| Cruise power, electrical | 1.6 kW |
| Engine rating | 2.6 kW |
| Battery buffer | 1.8 kg (3.6 % MTOW) |
| Fuel | 8 kg |
| **Endurance** | **15.7 h** |
| **Range** | **1 695 km** |
| Transition time | 2 s |

The mass budget behind this is a target and not a finding: 30 % structure, 16 %
propulsion chain, 4 % battery, 8 % avionics and control, 16 % fuel, leaving 26 % —
13 kg — for payload. Paper aircraft are habitually twenty to forty percent lighter than
the ones that get built, and that margin has not been paid in this table. Section 8
repeats this warning, because it is the single most likely place for these numbers to
be wrong.

## 6.3 Heavy reference design — 1000 kg

| Quantity | Value |
|---|---:|
| Maximum take-off mass | 1000 kg |
| Root chord | 3.25 m |
| Span | 11.55 m |
| Wing area | 22.24 m² |
| Wing loading | 45.0 kg m⁻² |
| Main propeller diameter | 5.40 m |
| Disc loading | 43.7 kg m⁻² |
| Tip propeller diameter | 0.67 m |
| Frame post length | 2.38 m each direction |
| Cruise speed | 40 m s⁻¹ (144 km h⁻¹) |
| Cruise L/D | 14.0 |
| Hover power | 216.2 kW |
| Cruise power, electrical | 38.1 kW |
| Engine rating | 54.3 kW |
| Battery buffer | 40 kg (4.0 % MTOW) |
| Fuel | 160 kg |
| **Endurance** | **13.0 h** |
| **Range** | **1 868 km** |
| Transition time | 4 s |

The heavy design has a slightly longer range than the light one despite a shorter
endurance. Both effects come from the same source: the larger aircraft cruises faster
and, at a higher Reynolds number, achieves a better lift-to-drag ratio. Nothing in the
architecture was changed to obtain this.

## 6.4 Scale behaviour

Three properties of the scaling are worth separating, because two of them are
favourable and one is not.

**Disc loading is held constant.** The two designs sit at 44.2 and 43.7 kg m⁻². This is
not a coincidence of sizing but the rule that governs it. Hover power per unit weight
is √(DL/2ρ), so holding disc loading constant holds the specific hover power constant,
and the aircraft can grow without the hover condition running away. Holding it constant
requires disc area to grow as L³ rather than L², which for a fixed number of propellers
is impossible — but this architecture may add coaxial pairs, and adding a pair is
architecturally free because every pair is already torque-balanced on its own.

**The buffer fraction is preserved.** 3.6 % of MTOW at 50 kg and 4.0 % at 1000 kg. The
mechanism by which Bill 3 is avoided therefore does not degrade with size.

**The frame drag fraction is preserved.** Frontal area and wing area both scale as L²,
so the twelve percent of Section 5.2 holds at both ends.

**Transition time does not scale.** This is the exception and it is stated plainly.
Required control moment goes as M = Iα with I ∝ mL², so the moment needed to rotate the
aircraft in a fixed time grows much faster than the aircraft. Scaling the light
design's two-second transition geometrically to 1000 kg would demand 221.5 kW from the
tip propellers — 102 % of the hover power, which is to say it is not available:

| Transition time | Tip-propeller power, 4 total | Fraction of hover power | Altitude lost |
|---:|---:|---:|---:|
| 2 s | 221.5 kW | 102 % | 8 m |
| 3 s | 65.6 kW | 30 % | 18 m |
| **4 s** | **27.7 kW** | **13 %** | **31 m** |
| 5 s | 14.2 kW | 7 % | 49 m |

The heavy design therefore rotates in four seconds and loses 31 m. **The rule is that a
larger aircraft turns more slowly**, and 31 m is an acceptable altitude allowance for a
1000 kg vehicle. This is the transition-side counterpart of the general result that
hover power required grows as L^3.5 while power available grows as L³.

*[Şekil 11: iki hat yan yana, aynı ölçekte. Tablo 4: geçiş süresi ve kumanda gücü.]*

## 6.5 Context

The following aircraft occupy the same mass range. They are listed to locate the
reference designs in a real field, not to rank them.

| Aircraft | MTOW | Payload | Payload fraction |
|---|---:|---:|---:|
| HAVELSAN BAHA | 28 kg | — | — |
| Textron Aerosonde Mk 4.7 VTOL | 45.4 kg | 9.1 kg | 20.0 % |
| Baykar KALKAN | 75 kg | ~3 kg internal | 4.0 % |
| HAVELSAN BULUT | not published | 5 kg | — |
| Elroy Air Chaparral | 865 kg | 136 / 227 kg | 15.7 / 26.2 % |
| Sabrewing Rhaegal-A | 1400 kg | 360–450 kg | 25.7–32.1 % |
| Pipistrel Nuuva V300 | 1700 kg | 408 kg | 24.0 % |

*[⚠️ Hepsi üretici tanıtımlarından. Faydalı yük tanımları tutarsız — kimi dahilî,
kimi harici, kimi ikisi. Boş ağırlıklar yayımlanmıyor. Yayına gitmeden her satıra
kaynak ve tanım eklenecek. HAVELSAN BAHA'nın VTOL olup olmadığı **doğrulanmadı**.]*

Three statements can be made about this table and a fourth cannot.

First, the field is real and populated, at both ends of the mass range considered here.
Second, payload fraction rises with size across the field, from a few percent at the
light end to roughly a quarter at the heavy end, which is the ordinary consequence of
fixed costs not scaling down. Third, none of these aircraft connects an
internal-combustion engine directly to a lifting rotor; every one of them uses either a
generator or separate electric lift, which is independent confirmation that the series
arrangement of Section 4.3 is the practical choice at this scale rather than an
unusual one.

The fourth statement — that the reference designs outperform these aircraft — is not
made, and the numbers in Sections 6.2 and 6.3 should not be read as making it. Those
numbers are calculated from a mass budget with an unpaid structural margin; the numbers
in this table describe aircraft that exist and fly. Placing a calculation beside a
measurement and declaring a winner would be a category error, and the comparison is
offered only to show that the reference designs fall inside the field rather than
outside it.

What can properly be compared, once these aircraft have been built and flown, is range
at similar payload — not payload at similar range. A configuration that carries a
comparable load further is making an architectural claim; a configuration that carries
a heavier load is making a claim about mass budgeting, which is exactly the part of
this study that is least validated.

*[Şekil 12 / N60: faydalı yük oranı – menzil düzlemi, üç aile. Ayrı sayfada
kurulacak. Bu bölümün argümanı o grafikte görselleşiyor.]*
