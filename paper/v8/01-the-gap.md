# Step 1 — The gap

**v8 taslağı, birinci yazım.** İskeletin 1. adımı. **Kararı ben verdim** — gerekçe aşağıda,
`cfd/external-review-49.md` §1'de de açık.

**Kural denetimi:** sabit kanatlıyla menzil yarışı **yok** (§0) · boşluk bir **mekanizma**
boşluğu olarak konuyor, bir başarım boşluğu olarak değil · *"inşa gereği"* geçmiyor (§0.3) ·
Adım 7 ve Adım 9'un *"what is new"* cümlelerinin **dayanağı burası** · çağdaş manzara
NASA belgesinden **birinci elden**, hatırlanarak değil.

---

## The gap

### Two families, two different limits

Uncrewed powered flight is dominated by two configuration families, and neither is bounded by
the thing the other is bounded by.

**Fixed-wing aircraft** carry payload over distance efficiently, because a wing sustains the
vehicle without continuously spending power on lift. Their limit is not aerodynamic but
infrastructural: a runway, a catapult, or an equivalent installation. That requirement is
expensive, fixed in place, and scales badly — a larger aircraft wants a longer runway, stronger
pavement and wider taxiways, so its growth is gated by the ground rather than by the air.

**Rotorcraft and multirotors** remove that requirement completely. They take off and land
vertically, hover, and work from confined sites. Their limit is the converse: with no wing,
every second of flight is bought with installed power, so range and endurance stay modest and
worsen as the vehicle grows.

**Neither family is deficient.** Each is excellent at what it does and is limited by the price
of doing it that way. What is unoccupied is the corner where both capabilities are wanted at
once, and the two applications this work is aimed at sit in that corner: **wildfire observation
and response, and cargo delivery to places without a runway.** Both want to leave from an
unprepared site and then cover distance.

### The demand has been continuous for seventy years

Tail-sitting prototypes flew in the 1950s, vectored-thrust and tilt-wing aircraft in the 1960s,
tilt-rotors from the 1980s, and a broad family of hybrid vertical take-off and landing uncrewed
aircraft since roughly 2010. Different nations, services and propulsion philosophies have
attacked the same problem for seventy years. **No field sustains that level of effort against a
need that is not real.**

### What the contemporary answers do, and how each changes regime

Hybrid VTOL aircraft occupy that corner today, and several are in service. **This paper does
not dispute that they work.** What matters for the argument is *how* each changes between the
two regimes, because that is where the families differ from one another.

A NASA study that sizes five VTOL architecture families to one mission describes the two
relevant routes in its own terms.

**The lift-plus-cruise route keeps two sets of hardware and switches between them.** In that
study the configuration is a stopping-rotor compound with three flight modes — helicopter mode
with the lifting rotors turning, compound mode with both sets operating, and aeroplane mode in
which *"the lifting rotors are stopped with the blade axis pointed along the vehicle
longitudinal axis, and therefore nominally aligned with the free stream to minimise drag,"*
with forward thrust from a pusher propeller. The lifting rotors are carried through cruise and
are stopped in the airstream.

**The tilting route keeps one set of hardware and reorients it.** The tilt-wing in the same
study carries six proprotors on a tilting main wing and two more on a tilting tail, each
directly connected to its own electric motor. Nothing is carried unused; the same discs that
lift the aircraft propel it, after being turned.

**Both work, and the second is the more elegant on paper** — one propulsion group, no dead
hardware in cruise. It is also the more demanding to build, because rotating a propulsor in
flight brings a pivot and its actuators, a gyroscopic moment during the rotation, and a control
problem through a regime in which the aircraft is neither a rotorcraft nor an aeroplane.
**Those are mechanical and control requirements rather than aerodynamic ones**, and that
distinction is what this paper is built on.

### The third route was flown, and the record of why it stopped is not what it is usually taken to be

There is a third way to put one set of propulsors into both regimes without reorienting them:
**point the thrust line at the ground and let the whole aircraft rotate.** It is not a new idea
and it was not untried. Two American prototypes flew it in 1954. The Lockheed XFV-1 never
completed the cycle. The Convair XFY-1 did: it flew vertically in August 1954, and six
transitions to conventional flight were completed.

**Why that programme stopped matters, because the usual account is wrong.** Two NASA reviews of
United States V/STOL development — one written largely from the reviewer's own flight-test
experience — judge the configuration itself favourably, calling it a *"good configuration
arrangement for low- and high-speed compatibility."* What they judge poorly is the machinery and
the cockpit around it: *"poor mechanical control system features including low actuator response
rate"*, difficulty hovering precisely over a spot, tip-over tendencies on the ground in gusty
air. The landing difficulty is attributed to *"the unusual spatial orientation where the pilot
looked over his shoulder and down"*, to turbulence sensitivity, and to reduced control power
near touchdown.

And the reason testing ended is recorded identically in both reviews:

> *"Six transitions to conventional flight were successfully completed **before testing was
> curtailed because of engine and gear-box reliability problems**."*

The pilot workload was real, separately documented and severe. **But it is not what curtailed
the testing, and three of the four recorded objections are objections to 1954 machinery and to
a human pilot rather than to the configuration**: actuator response rate, gearbox reliability,
and a spatial-orientation problem that exists only because someone is sitting in the aircraft.

### What the history does not excuse

It would be too convenient to conclude that every one of those programmes ended for reasons
outside its configuration, and this paper does not conclude it. **Some of the difficulties were
real, internal, and are inherited here.** A tail-sitting vertical descent is genuinely harder
than a runway landing. A tail-sitting aircraft on the ground is more exposed to crosswind than a
conventional one. And a set of propellers whose thrust vectors are all parallel to the body axis
cannot produce a rolling moment — a limitation that applies to the configuration described later
exactly as it applied to its predecessors, and one this paper addresses rather than avoids.

What the record does show is that **the configuration was never given a verdict under
present-day conditions.** The single best-documented obstacle — the human pilot — is the one an
uncrewed aircraft removes entirely. And three things are now available that were not: electric
drive on each individual rotor, sensor-based attitude reference, and enough onboard computation
that stability need not come from the airframe alone.

### The gap, stated precisely

Putting those together gives a gap that is narrower and more specific than "nobody has built a
good VTOL aircraft."

**Each half of the required capability is well served, and by different families.** Wing-borne
cruise is what fixed-wing aircraft do. Runway-independent vertical operation is what rotorcraft
do. **Both halves together are served by the contemporary hybrids, and this paper does not
claim that they fail to serve them.**

**What is unoccupied is the means.** Every architecture that puts one set of hardware into both
regimes does so by reorienting the propulsors, and pays a mechanism for it. Every architecture
that refuses the mechanism does so by carrying a second set of hardware, and pays mass and drag
for that. **The route that refuses both — one set of hardware, never reoriented, with the
airframe turning instead — was flown once, in 1954, with the machinery and the pilot of 1954,
and has not been revisited as a design proposition since the constraints that stopped it were
removed.**

That is the gap this paper addresses. **None of the elements it uses is new**, and Section 7
says so explicitly: tail-sitting aircraft are seventy years old, blended wing bodies have been a
standing subject of transport research for three decades, and series-hybrid propulsion is
ordinary in small uncrewed aircraft. **What is offered is the combination and the means**, and
the paper's job is to say what that combination costs rather than to assert that it is free.

Section 2 states the cost that any architecture in this corner pays, in terms that do not
presume an escape.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| Sabit kanatlının sınırı altyapısal; pist, mancınık, eşdeğeri | §1, satır 152–157 |
| Rotorlunun sınırı: kanat yok, her saniye kurulu güçle ödeniyor | §1, satır 159–163 |
| Yetmiş yıl: 1950'ler kuyruk üstü, 1960'lar tilt-wing, 1980'ler tilt-rotor, 2010'lar hibrit | §1, satır 167–172 |
| **Lift+cruise: durdurulan rotor, üç uçuş kipi, palalar gövde eksenine hizalı** | **Johnson & Silva 2022, §5.4, s. 71 — birinci elden okundu** |
| **Tiltwing: eğilen ana kanatta altı, eğilen kuyrukta iki proprotor, her biri kendi motorunda** | **Johnson & Silva 2022, §5.5, s. 72 — birinci elden** |
| Beş VTOL mimari ailesi, çoğu iki tahrik türünde | Johnson & Silva 2022, s. 70 |
| Tilt bedeli: pivot ve aktüatörler, dönüşte gyroskopik moment, geçiş kontrol problemi | §1.4, satır 460–464 |
| XFV-1 çevrimi tamamlamadı; XFY-1 Ağustos 1954, **altı geçiş** | §1.2, satır 402–407, kaynaklar [1,2] |
| *"Good configuration arrangement for low- and high-speed compatibility"* | §1.2, satır 411–412, kaynak [1] |
| *"Poor mechanical control system features including low actuator response rate"* | §1.2, satır 413 |
| *"The unusual spatial orientation where the pilot looked over his shoulder and down"* | §1.2, satır 415–416, kaynak [2] |
| *"…curtailed because of engine and gear-box reliability problems"* — iki incelemede de aynı | §1.2, satır 421–422 |
| Dördünden üçü 1954 makinesine ve insan pilota itiraz | §1.2, satır 424–427 |
| Miras alınan üç gerçek güçlük: dikey iniş, yanal rüzgâr, yatış momenti | §1.5, satır 481–488 |
| Şimdi var olan üç şey: her rotorda elektrik tahrik, sensör tabanlı tutum, gövdeden gelmeyen kararlılık | §1.5, satır 497–501 |
| Üç öğenin hiçbiri yeni değil | `paper/v8/07-the-combination.md` açılışı |

**Bu sayfada BİLEREK olmayanlar:** tek bir başarım sayısı, bu uçağa dair hiçbir tarif, ve
çağdaş hibritlerin **işe yaramadığı** iması. Boşluk bir **başarım** boşluğu olarak değil,
bir **araç** boşluğu olarak konuyor — çünkü makalenin iddiası da o.

**Adım 7 ve Adım 9'un dayanağı artık burada.** Her ikisi de *"yeni olan şey birleşme ve
araçtır"* diyor; bu sayfa o cümlenin karşılığını veriyor ve neyin yeni **olmadığını** açıkça
sayıyor.
