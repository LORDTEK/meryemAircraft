# 5. How the architectural tax is avoided

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

Section 3 identified three bills and argued that they are one quantity paid in three
currencies. Section 4 described a configuration built to satisfy the zero-bill
condition. This section audits that claim bill by bill, and then states, in the same
detail, what the configuration does pay. The second half is not a concession appended
for balance. An architecture that claimed to pay nothing would be describing a
different aircraft from the one in Section 4.

## 5.1 Bill 1 — mass: not paid

There is no second propulsion group. The nose pair that lifts the aircraft off the
ground is the same pair, in the same orientation, at the same station, that propels it
in cruise. Nothing is carried unused.

This is the whole of the argument, and its brevity is the point. The bill was never a
consequence of poor design in lift-plus-cruise aircraft; it was a consequence of
counting two propulsion systems where the mission needs one. A configuration that
counts one does not reduce the bill — it does not generate it.

The tip pairs are a genuine addition and are accounted for in Section 5.4. They are not
a second propulsion group: they are sized for moments rather than for weight, and in
the vertical phase they draw 1.34 kW against the nose pair's 10.9 kW, which is twelve
percent.

## 5.2 Bill 2 — drag: mostly not paid

In cruise there is no stopped rotor in the airstream, because there is no rotor that
stops. The nose pair is the cruise propulsor and runs at its design condition
throughout. The quarter of lift-to-drag ratio that Section 3.3 reports as the measured cost of
installing hover hardware is not incurred here — not reduced, not mitigated, but absent,
because the hardware that causes it does not exist in this configuration. Nor is there a retraction mechanism,
so the transfer of Bill 2 into Bill 1 identified in Section 3.3 does not occur either.

It is worth noting what this avoidance also spares. Where lift rotors are retained,
keeping their drag small depends on stopping them at a favourable azimuth, which needs
an indexing mechanism; where they are stowed, it needs a retraction mechanism. Both are
mass, and both are failure modes. A configuration with no rotor to stop needs neither.

The word "mostly" in this heading is deliberate. The configuration does place hardware
in the cruise airstream: the four tip frames and the four control propellers they
carry. That is a real payment against Bill 2, and quantifying it produced the single
most consequential sizing result in this study.

The frames present 2.84 m of exposed length to the flow, oriented perpendicular to it,
for the light reference design. At the cruise dynamic pressure of 551 Pa, against a
total cruise drag of 38.6 N, their contribution depends almost entirely on their
cross-section:

| Frame cross-section | C_D | Share of total cruise drag |
|---|---:|---:|
| Circular tube, 20 mm | 1.15 | **93 %** |
| Faired strut, 20 mm | 0.15 | 12 % |
| Well-faired strut, 20 mm | 0.08 | 6.5 % |

Left as circular tubing, the frames alone would produce very nearly as much drag as the
entire rest of the aircraft, and the configuration's central claim would collapse. The
result is therefore not an observation but a requirement: **the tip frames must be
faired.** With a faired section the payment is real and affordable — of the order of
twelve percent of cruise drag — and it is reported here as a cost rather than absorbed
silently.

One property of this cost is worth noting. The frame frontal area scales with the
square of length, and so does the wing area, so under geometric scaling at equal cruise
dynamic pressure the fraction is preserved. This bill does not grow with the aircraft.

*[⚠️ C_D değerleri literatür mertebeleridir; bu kesit için hesaplanmadı ve kesit
henüz seçilmedi. Bölüm 8'e girecek. Künye §11.5b, N83.]*

## 5.3 Bill 3 — power system sizing: not paid

The series-hybrid arrangement of Section 4.3 breaks the link that forces the power
system to be sized by the hover condition. Because the engine drives a generator rather
than a rotor, it supplies average power, not peak power, and the peak is supplied from
a buffer.

For the light reference design the numbers are as follows. Cruise requires 1.8 kW
continuously, and the engine is sized at 2.6 kW. Hover requires 10.9 kW — 4.2 times the
engine's rating. The difference is drawn for the duration of the vertical phase from a
1.8 kg battery, which is 3.6 percent of the maximum take-off mass. The heavy reference
design sits on the same line: 38.8 kW cruise, 54.3 kW engine, 216.2 kW hover, 40 kg of
battery at 4.0 percent of MTOW.

An aircraft of this class whose powerplant had to be sized for hover would carry an
engine rated above 10.9 kW instead of 2.6 kW. The mass difference is not recovered
elsewhere; it is simply not incurred. That the buffer costs under four percent of MTOW
at both design points, twenty times apart in mass, is the numerical statement that this
avoidance is architectural rather than a fortunate coincidence of one size.

## 5.4 What is paid

The honest ledger has four entries.

**The control propellers.** Four pairs, their motors, mounts and wiring exist only to
produce moments. In the vertical phase they draw twelve percent of the power the nose
pair draws. This is the configuration's substitute for elevons and a rudder, and it is
not free — it is merely cheaper than a second lift system, and it does not sit in the
cruise airstream in the way a lift rotor does.

**The tip frames.** As established in Section 5.2, of the order of twelve percent of
cruise drag, conditional on being faired. This is the largest single payment the
configuration makes, and it is the price of the moment arm, the propeller mounting and
the landing structure combined into one member.

**The roll strip.** The one moving aerodynamic device on the aircraft. Its cost when
retracted is a surface discontinuity; when deployed it is a drag device by construction,
but it is deployed only while a roll is being commanded.

**The transition manoeuvre.** The aircraft must rotate through ninety degrees, and the
rotation costs altitude and control power. Section 7 treats this in full. It is a real
operational cost and it is not scale-invariant: the light design rotates in 2 s losing
8 m, while the heavy design requires 4 s and loses 31 m.

Set against the bills of Section 3, the ledger is favourable but not empty. The
configuration does not escape physics; it declines a particular trade. What it pays
instead is smaller, and — this is the part that matters for scaling — it does not grow
faster than the aircraft.

*[Tablo 1 buradan üretilecek: üç fatura, dört mimari (lift+cruise, tilt, katlanır
rotor, bu çalışma), her hücrede ödenme biçimi.]*
