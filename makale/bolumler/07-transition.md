# 7. Flight profile and transition

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

The transition between vertical and horizontal flight is the manoeuvre on which
tail-sitters have historically been judged, and it is the part of this configuration
that most deserves scrutiny. This section describes the flight profile, states the
equations that govern the transition, and reports a simulation of it. One result
contradicts a widely-assumed relationship and is presented as such.

## 7.1 The five phases

**Stance.** The aircraft rests on five points — the four lower ends of the tip frames
and the aft end of the centre keel — with its longitudinal axis vertical. No launch
equipment is present, and the aircraft is in its own storage attitude.

**Vertical take-off.** The nose pair spools to a thrust exceeding weight and the
aircraft rises vertically. Attitude is held by the four tip pairs. This is the
highest-power phase of the flight and the shortest.

**Transition.** The aircraft rotates from vertical to horizontal while accelerating,
until the wing carries the weight. Treated in detail below.

**Cruise.** The aircraft flies as a tailless blended-wing body. The nose pair is now
the cruise propulsor at its design point. The tip pairs provide pitch and yaw, and the
lower-surface strip provides roll.

**Landing.** The reverse of transition, followed by a vertical descent onto the five
contact points. Section 7.5 notes what is and is not analysed here.

*[Şekil 9: beş aşama.]*

## 7.2 Why the transition begins in the easiest condition

A common objection to tail-sitter transition is that the aircraft must fight the
airflow while rotating. For a transition that begins in hover, it does not. At the
start of the manoeuvre the airspeed is zero, so the free-stream dynamic pressure

    q = ½ρV²

is zero, and with it every aerodynamic moment that would resist the rotation. The
aircraft is not turning against the air; it is turning in still air and then meeting
the air as it accelerates.

The consequence is that the difficult part of the transition is not its beginning but
its middle, where the airspeed has grown enough for aerodynamic moments to matter but
the wing is not yet carrying the weight. The control authority requirement is set
there, not at the start.

*[⚠️ Bu, önceki bir yanlışın düzeltilmiş hâlidir: geçişin başında rüzgâr gülü
etkisiyle direnç oluştuğu düşünülmüştü. $q\\to0$ olduğu için oluşmuyor.]*

## 7.3 The thrust singularity that is never reached

Consider the aircraft at an angle θ from the vertical, and suppose for a moment that it
must hold altitude with thrust alone. Vertical equilibrium then requires

    T cos θ = W        →        T = W / cos θ

which diverges as θ approaches ninety degrees. Read literally, this says a tail-sitter
cannot complete a transition, and the expression is sometimes quoted to that effect.

The expression is correct and the conclusion drawn from it is not, because the premise
is false. The aircraft does not hold altitude with thrust alone. Vertical support is

    T cos θ + L = W,        L = ½ρV²S C_L

and V is not zero during the rotation — it is growing, because the horizontal component
T sin θ is accelerating the aircraft. The horizontal acceleration, in the same
idealisation, is

    a = g tan θ

so the very rotation that reduces the vertical component of thrust is what generates
the airspeed that replaces it. The singularity is never approached because the wing
arrives first.

This is the central mechanism of the manoeuvre, and it also explains the result of the
next subsection.

## 7.4 Transition time: slower is better

The transition was simulated as a two-degree-of-freedom point mass. The body angle θ is
driven from zero to ninety degrees over a rotation time t_r; thrust acts along the body
axis, lift perpendicular to the velocity vector and drag opposite to it; the lift curve
is linear to stall and a flat-plate relation beyond it; and thrust is reduced to the
drag value once cruise speed is reached. Altitude loss is reported as the lowest point
of the trajectory relative to the entry altitude.

**Light reference design, 50 kg. Altitude loss, metres:**

| t_r | T/W = 1.1 | **T/W = 1.2** | T/W = 1.3 | T/W = 1.5 |
|---:|---:|---:|---:|---:|
| 0.5 s | −15.9 | −13.5 | −11.5 | −8.3 |
| 1 s | −14.0 | −11.3 | −8.8 | −3.0 |
| 2 s | −10.5 | **−6.6** | −1.6 | 0 |
| 3 s | −9.9 | **−0.3** | 0 | 0 |
| 4 s | −1.8 | **0** | 0 | 0 |

**Heavy reference design, 1000 kg. Altitude loss, metres:**

| t_r | T/W = 1.1 | **T/W = 1.2** | T/W = 1.3 | T/W = 1.5 |
|---:|---:|---:|---:|---:|
| 1 s | −26.6 | −22.1 | −18.2 | −11.5 |
| 2 s | −21.8 | −16.0 | −6.8 | −0.2 |
| 3 s | −17.0 | −6.3 | −0.6 | 0 |
| 4 s | −17.7 | **−0.6** | 0 | 0 |
| 5 s | −5.0 | **0** | 0 | 0 |

The relationship is monotonic in the direction opposite to the one usually assumed. It
is frequently supposed that a tail-sitter should rotate as quickly as possible, on the
reasoning that the aircraft is unsupported during the rotation and therefore falls for a
time t_r, giving an altitude loss proportional to t_r². **That reasoning is wrong, and
the error is in its premise.** The aircraft is not unsupported during the rotation.
Vertical support is T cos θ + L, and a slow rotation keeps cos θ large during exactly
the interval in which V, and therefore L, is being built. A fast rotation collapses
cos θ before there is any L to replace it, and the aircraft falls precisely because it
hurried.

The practical consequence is a simplification rather than a trade. The control power
required to rotate the aircraft in time t_r scales as 1/t_r², so a slow rotation is
cheap in control authority; and the altitude loss also falls with t_r. **Both
constraints point the same way.** There is no optimum transition time to be found
between two competing penalties, because there are not two competing penalties. The
transition time is bounded from below, not from above, and its upper bound is set by
fuel, horizontal displacement and operational exposure rather than by flight mechanics.

Thrust-to-weight ratio is the dominant parameter. At T/W = 1.1 the aircraft loses
roughly ten metres regardless of how it is flown; at T/W = 1.3 the loss reaches zero
within three seconds. The reference designs assume T/W = 1.2, at which the light design
completes the manoeuvre in three seconds for a loss under one metre and the heavy design
in five seconds for no loss.

*[⚠️ Sınırlar açıkça: benzetim nokta-kütledir ve **dönme dinamiğini modellemez** —
$\\theta$ kinematik olarak sürülür. Dolayısıyla gereken uç pervanesi itkisi bu
benzetimden ÇIKMAZ. Kanat aerodinamiği basit bir modeldir; girdaplı ayrılma,
gecikmeli tutukluk ve iz etkileri yoktur. Bölüm 8'e girecek. Künye N86–N89.]*

*[⚠️ N88: uç pervanelerinin 16,2 N'luk boyutu **2 saniyelik geçişten** türetilmişti.
Geçiş artık yavaş yapılıyorsa boyutlandıran durum geçiş değil, **hover'da bozucu
bastırmadır.** Yeniden boyutlandırma yapılmadı — Bölüm 8'de açık iş olarak yazılacak.]*

*[Şekil 10: irtifa kaybı, $t_r$ ve T/W'ye göre.]*

## 7.5 Landing

Landing reverses the sequence: the aircraft decelerates, rotates nose-up, and descends
vertically onto its five contact points. Two things should be said about it plainly.

The first is that the historical objection to this manoeuvre does not apply. The XFY-1
was cancelled because its pilot had to judge a backwards vertical descent by looking
over his shoulder. There is no pilot here, and height above ground is a sensor
measurement rather than a human estimate.

The second is that the vertical descent itself has not been analysed in this study. A
rotor descending into its own wake can enter the vortex ring state, in which thrust
becomes erratic and increasing power makes matters worse. Whether the descent profile
of this configuration enters that region, and at what rate of descent, is an open
question. It is listed in Section 8 rather than answered here.
