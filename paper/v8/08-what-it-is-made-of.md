# Step 8 — What it is made of, and what still moves

**v8 taslağı, birinci yazım.** İskeletin 8. adımı. Adım 7'nin işaret ettiği yer.

**Kural denetimi:** "önceki sürümde" anlatısı yok · "mekanik olarak daha basit" geçmiyor ·
şerit yunuslama momentiyle birlikte geçiyor · eyleyici sayısı **uydurulmuyor** ·
pervane verimi sayısı burada **yok** (Adım 7'de bir kez, defterde kalem olarak) ·
askı tork artığı açık kalem olarak adlandırılıyor.

---

## What it is made of, and what still moves

Section 7 claimed that a class of mechanism is absent. A claim of that kind is only as good as
the inventory behind it, so the inventory is given here in full, including the parts that move.

### The airframe

The entire airframe is the wing. There is no cylindrical fuselage: every part of the planform
carries payload and produces lift. Leading-edge sweep varies continuously along the span while
the trailing edge is held at 25°, so the realised sweep runs from 45° at the root to 38.3° at the
tip — a variation of under seven degrees, with the crescent character coming from the curvature of
the leading edge rather than from a large change in sweep. Thickness runs from 25 % of chord at
the root to 12 % at the tip, and chord from 0.970 m to 0.236 m. For the light design the span is
3.453 m, the wing area 1.979 m², and the aspect ratio 6.03.

Sweep is not a free parameter here, and the reason is structural to the configuration rather than
aerodynamic preference. The aircraft is tailless. With no horizontal stabiliser on a boom, the
pitching moment must come from the distribution of lift along the body itself, and sweep is what
places the outboard sections behind the centre of gravity so they can produce it. **The sweep
angle and the longitudinal stability are one design variable seen from two directions.**

### The propulsion

Five propellers, and every one of them is a coaxial counter-rotating pair. The reason is narrow
and worth stating as such: **reaction torque.** A single propeller applies to the airframe a
torque equal and opposite to the one it applies to the air — about the yaw axis in hover and the
roll axis in cruise — and that torque must be opposed continuously, either by a control surface,
which costs drag, or by differential thrust, which costs a control channel. A counter-rotating
pair does not produce it.

One pair sits at the nose, 1.20 m in diameter on the light design, and produces all propulsive
thrust in both regimes. Four smaller pairs, 0.20 m in diameter, sit at the ends of rigid frames
projecting from the wing tips. Every pair is of **fixed geometry**: no cyclic pitch, no
collective, no variable mechanism of any kind. Each rotor of each pair is driven by its own
electric machine on a common axis, so the arrangement that repeatedly defeated the XB-35 —
concentric shafts, a splitting gearbox, and the governors that synchronise them — is never built.

The counter-rotating arrangement carries a second consequence that the transition analysis
depends on. Because the two rotors of each pair carry equal and opposite angular momentum, **the
net angular momentum of the propulsion system is nominally zero**: rotating the airframe through
ninety degrees precesses nothing, and no gyroscopic moment appears for the control system to
cancel. In a tilting architecture that term is present and must be designed for.

### The energy path

A series hybrid: fuel to engine, engine to generator, generator to electric machines at the
rotors. The engine is not mechanically connected to any rotor. It is an energy source, and that
decoupling is what allows it to be sized by cruise rather than by hover. For the light design the
continuous cruise requirement is 1.9 kW at the engine shaft and the engine is rated at 2.6 kW,
while the hover requirement is 10.9 kW at the rotor. The difference is supplied for the vertical
phase from a **1.8 kg battery buffer, 3.6 % of take-off mass.**

### What produces each moment

**Pitch and yaw come from differential thrust between the tip pairs**, and the two axes do not
have the same moment arm. The frames project ±0.71 m perpendicular to the planform, so a
differential between the upper and lower pairs acts at 0.71 m in pitch, while a differential
between the left and right pairs acts at the semi-span, **1.726 m — 2.43 times the pitch arm.**
The yaw arm is therefore the larger by that factor, which is the reverse of the usual situation
and is a consequence of the layout rather than a design choice. What authority each axis
actually has depends on the available thrust differential and on allocation as well as on the
arm, and is not settled by the ratio alone.

**The same differential-thrust system is what is assigned to rotate the airframe through
transition.** That is a design assignment, not a demonstrated result: whether the moment it
produces is sufficient, and whether the aircraft trims through the rotation, are questions for
Section 10.

**Roll comes from neither.** Every pair is coaxial and nominally torque-balanced, so every thrust
vector is parallel to the body axis and no combination of settings produces a rolling moment. Roll is
produced instead by a strip on the lower surface: inclined at 45° in planform, running 120 % of
root chord, reaching 67 % of semi-span, and standing 2 cm proud at its inboard end and 6 cm at
its outboard end. **Extension is the control variable** — the strip is modulated, not switched —
and deploying it also pitches the nose down by a small increment. Its inboard 46 % lies inside
the nose propeller's slipstream, where dynamic pressure is set by disc loading and is therefore
available at zero airspeed; its outboard 54 % works against the freestream in cruise. That split
is why one device serves both regimes.

### What meets the ground

The aircraft rests on five points: the four lower ends of the tip frames, and the aft end of a
keel running along the centreline. It stands on its tail in its own storage attitude, with no
launch equipment present.

**The frames carry a fairing, and it is not only a drag measure.** The frames are the only
surfaces standing perpendicular to the wing plane, and a planar planform supplies no directional
stability at all, so the fairing is also the only vertical surface the aircraft has. Sized
against the criterion the tailless literature recommends — C_n_β greater than 0.001 per degree —
the chord required over the combined frame length is **39 mm**, against the 50 to 70 mm that a
20 mm faired strut carries in any case. Directional stability on this configuration therefore
does not ask for a surface; it asks for a fairing on a frame that is already there.

**One part is not airframe and is easy to omit from a list of this kind: the flight control
system.** The stability of this configuration is not airframe-borne — it is produced by
differential thrust and by the strip, both of which are actively commanded — so an attitude
reference and a flight computer are not optional equipment but part of the mechanism the
preceding paragraphs describe. They are carried in the systems budget. The configuration
replaces a pilot's workload with computation, and the computer is the part that does it.

**The tip frames therefore do three jobs at once**, and this is the clearest instance in the
configuration of one structure carrying several duties: they are the landing gear, they set the
control moment arms, and they carry the attitude rotors. Lengthening them to buy control
authority widens the stance base against tipping in wind at the same time. They are also the
structure that is exposed in cruise, and Section 11 charges them for it.

### What moves

The propellers rotate, as propellers do, and their shaft speed is commanded; but none of them
changes its orientation relative to the airframe, or its blade pitch, at any point in the flight.
**Beyond the propellers' rotation, one thing on this aircraft changes its configuration: the
strip.**
It is described as deployable in two halves — one side alone for roll, both together as a speed
brake. The actuator inventory is therefore the propulsion motors plus the strip's actuation.
**How many actuators that is, this study does not fix.** The systems budget carries the
actuation without sizing the mechanism, and naming a number here would be inventing one.

### What this inventory does not settle

Two items belong here rather than in a later list, because both are properties of the hardware
just described.

**An untrimmed hover torque, with no trim mechanism identified.** This is a control question
rather than a property of the hardware, and it is stated as one.

The torque balance within each pair is set exact at the cruise condition rather than at hover, so
a small residual remains in hover. It acts about the propeller axis — the aircraft's longitudinal
axis, which is the roll axis in body terms and stands vertical in the hover attitude, so it
appears there as a change of heading. *(This paper fixes body-axis naming throughout; the earlier
description of reaction torque as acting "about the yaw axis in hover" named the same axis by its
earth-frame effect, and the two conventions are not mixed here.)*

That axis is the one the propellers cannot command at all, which is why the residual is a
problem: the tip pairs cannot absorb it without roll authority the aircraft does not have in
hover, and the strip works against dynamic pressure that the slipstream supplies over only part
of its length at zero airspeed. Either the residual is small enough to be absorbed by the speed
trim of the pairs — which this study has not shown — or a fourth duty falls on the strip.

**The fixed geometry of the tip pairs leaves two admissible cruise states, and only one of them
is physically closed.** Unable to feather, the pairs must either turn at the zero-shaft-torque
condition or be stopped, and the difference between those two states is a substantial fraction of
the aircraft's zero-lift drag. Both ends are computed rather than assumed and the charge appears
in Section 11.

The free-wheeling state is physically determinate: the rotor settles where net shaft torque is
zero. **The stopped state is not.** Stopping a rotor requires the stop to be produced by
something — motor holding torque, an electrical brake, a mechanical lock — and a stopped
fixed-pitch blade also has an azimuth, so "stopped" is a family of aerodynamic states rather than
one. Neither the means nor the azimuth is fixed by this study, and the drag figure quoted for the
stopped condition should be read as the state Section 11 defines rather than as the state a
particular installation would reach.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| Süpürme 45° kökten 38,3° uca, firar kenarı 25°, değişim <7° | §2.8, satır 729–733 |
| Kalınlık %25→%12, veter 0,970→0,236 m | §2.8, satır 731–732 |
| Açıklık 3,453 m, alan 1,979 m², AR 6,03 | §2.8, satır 750–752 |
| Süpürme ile boyuna kararlılık tek değişken | §2.8, satır 741–743 |
| Her pervane eşeksenli karşıt dönüşlü; gerekçe tepki torku | §2.9, satır 757–760 |
| Sabit geometri: cyclic yok, collective yok | §2.9, satır 762 |
| Her rotor kendi elektrik makinesinde; XB-35 dişli kutusu hiç kurulmuyor | §2.9, satır 784–786 |
| Net açısal momentum nominal sıfır; gyroskopik moment yok | §2.9, satır 776–780 |
| Seri hibrit; motor 1,9 kW gerek, 2,6 kW derece; askı 10,9 kW | §2.9, satır 788–792 |
| Tampon 1,8 kg, MTOW'un %3,6'sı | §2.9, satır 792–793 |
| Burun çifti 1,20 m, uç çiftleri 0,20 m, 16,2 N, 335 W, dörtte 1,34 kW | §2.10, satır 796–799 |
| Yunuslama kolu 0,71 m, sapma kolu 1,726 m, oran 2,43 | §2.10, satır 805–808 |
| Yatış eşeksenli çiftlerle üretilemez | §2.10, satır 811–813 |
| Şerit: alt yüzey, 45°, kök veterinin %120'si, açıklığın %67'si, 2→6 cm | §2.10, satır 816–818 |
| Şerit modüle ediliyor; burnu aşağı yunuslatıyor | §2.10, satır 818; ΔC_m §3.17 |
| Slipstream içinde %46, serbest akışta %54 | §2.10, satır 821–823 |
| Beş temas noktası: dört uç çerçevesi ucu + orta omurga | §2.11, satır 946–947; §3.12, satır 2103–2104 |
| Uç çerçeveleri: iniş takımı + moment kolu + kumanda pervanesi | §2.11, satır 942–944 |
| Şerit iki yarım: bir yan yatış, ikisi birden hava freni | §1, satır 296–297 |
| **Eyleyici sayısı bu çalışmada belirlenmiyor** | §1, satır 295–298 |
| Tork dengesi seyirde tam, askıda artık kalıyor; trim edilişi belirlenmemiş | §2.9, satır 766–773; §4.6 |
| Uç çiftleri pala açısı değiştiremez; durmak ya da sıfır tork | §2.9, satır 762–766 |
| Fairing: uçaktaki tek dikey yüzey, C_n_β > 0,001/derece, 39 mm veter | §2.11, satır 899–903; §3.5, satır 1301–1306 |
| 20 mm kaplanmış dikme zaten 50–70 mm taşıyor | §2.11, satır 902–903 |
| Aviyonik kütle bütçesinde (%8) | §3.7 kütle dökümü, satır 1653 |
| **Motor yerleşimi, hava alışı, soğutması: makalede YOK** | arama: intake/exhaust/cooling/engine bay — sonuç yok |
| Enerji yolu sayıları yayımlanmış 0,80 zincirinden | §2.9, satır 788–793; aşıldı: `paper/chain-resolve-finding.md` |

**Tur 40'ta düzeltilenler.** ChatGPT ve Qwen bağımsız olarak *"beş pervane, her biri bir çift"*
çelişkisini buldu. **Grok'un bulgusu en ağırıydı:** enerji yolu sayıları yayımlanmış 0,80
zincirinden geliyordu ve Adım 7 o varsayımı zaten 0,63–0,68'e indirmişti — iki sayfa birbiriyle
çelişiyordu. DeepSeek fairing'in eksik olduğunu, Qwen uçuş kontrol sisteminin eksik olduğunu,
Grok motorun nerede durduğunun hiç söylenmediğini buldu. ChatGPT *"durdurulmuş"* durumunun tek
bir aerodinamik durum olmadığını gösterdi. Eksen adlandırması iki okuyucuyu birden tökezletti;
kaynakta gerçekten iki ayrı anlaşma karışık kullanılıyor ve burada sabitlendi.

**Kabul edilmeyen tek bulgu:** ChatGPT eşeksenli çiftin iç içe mil gerektirdiğini, dolayısıyla
*"concentric shafts... is never built"* cümlesinin yanlış olduğunu söyledi. İki makine eksende
istiflenip her biri kendi bitişik rotorunu doğrudan sürerse iç içe mil gerekmez; yani iddia en
az bir standart uygulama için savunulabilir. Ama makale uygulamayı belirlemiyor, bu yüzden
**ChatGPT'nin dar hali alındı**: dişli kutusu ve regülatörler elenir, mil düzeni hakkında iddia
yok.

**Bu sayfada BİLEREK olmayanlar:** pervane verimi sayısı (Adım 7'de bir kez, defterde kalem),
sürükleme kalemlerinin büyüklüğü (Adım 11), kütle dökümü (Adım 10 ve 11).
