# Step 1 — The gap

**v8 taslağı, birinci yazım.** İskeletin 1. adımı. **Kararı ben verdim** — gerekçe aşağıda,
`cfd/external-review-49.md` §1'de de açık.

**Kural denetimi:** sabit kanatlıyla menzil yarışı **yok** (§0) · boşluk bir **mekanizma**
boşluğu olarak konuyor, bir başarım boşluğu olarak değil · *"inşa gereği"* geçmiyor (§0.3) ·
Adım 7 ve Adım 9'un *"what is new"* cümlelerinin **dayanağı burası** · çağdaş manzara
NASA belgesinden **birinci elden**, hatırlanarak değil.

**Tur 47 eklemesi.** Yazarın yüklediği iki belge birinci elden okundu ve *"zaten dolu olan"*
bölümüne girdi: **Novlit ve ark. 2014** (eşeksenli karşıt dönüşlü kuyruk üstü MAV — tork
dengeleme gerekçesi, slipstream içinde elevon ve rudder, ve **eksen adlarının askıda yer
değiştirmesi**) ve **Zhang ve ark. 2012** (aynı mimaride **diferansiyel devirle yatış**).
İkincisi, boşluk paragrafındaki *"a torque-balanced coaxial pair cannot produce a rolling moment
by any setting"* cümlesini **çürüttü**; cümle bir seçim ifadesine çevrildi.

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

### The third route is established, and its history is not what it is usually taken to be

There is a third way to put one set of propulsors into both regimes without reorienting them:
**point the thrust line at the ground and let the whole aircraft rotate.** It is neither new nor
untried nor abandoned. Two American prototypes flew it in 1954, **and uncrewed tail-sitters have
revisited it continuously since.** The Lockheed XFV-1 never
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
produces no rolling moment by any combination of thrust settings — which applies to the
configuration described later exactly as it applied to its predecessors, and which this paper
addresses rather than avoids.

What the record does show is that **the obstacle that ended the flying was mechanical**, and
that one of the documented handling obstacles — the pilot's spatial orientation and workload —
is removed by an uncrewed aircraft. **The others are not removed by anything.** Precise hovering,
ground gusts and the absence of a thrust-borne rolling moment are configuration facts, and they
are inherited.

Three things are available now that were not: electric drive on each individual rotor,
sensor-based attitude reference, and enough onboard computation that stability need not come
from the airframe alone. **The uncrewed tail-sitter literature has been exploiting exactly those
three for over a decade**, which is why the gap below is not a historical one.

### What is already occupied, stated before the gap

It would be easy, and wrong, to present the third route as an empty field. **It is not**, and
the paper is better for saying so first.

**The route itself is established.** Uncrewed tail-sitters combining fixed-pitch rotors with a
flying wing have been built and flown for more than a decade, beginning with quadrotor-plus-wing
arrangements carrying a few aerodynamic actuators for forward flight.

**Attitude without aerodynamic control surfaces is established.** A quadrotor tail-sitter
operated without control surfaces, with experimental verification, was reported in 2013.

**Coaxial contra-rotating propulsion on a tail-sitter is established**, proposed specifically to
remove the reaction torque a single propeller imposes, at the cost of an extra motor and the
coaxial arrangement. A coaxial contra-rotating tail-sitting micro air vehicle reported in 2014
states the same purpose in the same terms: *"a pair of 10 inches coaxial contra rotating
propellers is mounted to compensate each other's torque."*

**The established answer to hover control on such a configuration is a surface in the
slipstream**, and it is worth naming because this paper refuses it. That 2014 vehicle places
*"elevon and rudder … immersed in the propeller slip stream to provide three axis control moments
in hover."* The answer works, costs little, and is the one a reader will reasonably expect.

**And the reaction-torque channel this paper declines is established as a control channel.** A
coaxial contra-rotating tail-sitter reported in 2012 balances rotor torque *"by the inverse
rotating of the two rotors"* and then unbalances it on purpose to steer: its published control
scheme assigns *"differential velocity of the two motors"* to yaw in the vertical mode and to
roll in the horizontal one. **Those are the same physical channel under two names** — a moment
about the propeller axis, which stands vertical in hover and horizontal in cruise — and
independently driven rotors make it available to any coaxial pair. **Using it is a choice, and
so is declining it**, which is what separates this configuration's control problem from a
physical impossibility.

**A blended-wing-body tail-sitter with contra-rotating propulsion, aimed at disaster response,
is established**, reported in 2025 with vortex-lattice and RANS analysis of its planform,
winglets and transition.

**And the propeller compromise at the centre of this paper's own ledger is a known result, not a
discovery.** The uncrewed tail-sitter literature states it directly: fixed-pitch propellers make
it *"theoretically impossible to be very efficient in both hovering and forward flight."* A
long-range tail-sitter reported in 2018 describes its own rotor as *"a compromise between
efficient hover and efficient forward flight"* and selects its diameter on exactly that basis.

### The gap, stated precisely

**Each half of the required capability is well served, and both halves together are served by
the contemporary hybrids.** This paper does not claim otherwise. **And the third route is
occupied.** What follows is therefore not a claim to an empty field.

**What is not established is the combination taken together with its price.** Specifically:
a blended-wing-body tail-sitter in which *every* propulsor is a coaxial, torque-balanced pair —
so that reaction torque and net angular momentum are given up along with the reorientation
mechanism — carrying no aerodynamic control surfaces beyond a single moving device, powered
through a buffered series hybrid, and **audited explicitly against carried hover mass, exposed
cruise drag and hover-sized continuous power**, at two scales and under three sizing contracts.

Each of those choices costs something, and **the giving-up is the part that is not free**. A
quadrotor tail-sitter produces a rolling moment from the reaction torque of four independently
driven rotors; a coaxial pair can produce one the same way, by running its two rotors at different
speeds. **Operating every pair torque-balanced spends that channel to buy the torque balance and
the near-zero net angular momentum**, and leaves the axis to a single aerodynamic device. What
that costs, and what the rest of the combination costs, is what the paper is for.

**None of the elements is new**, and Section 7 says so. Tail-sitting aircraft are seventy years
old and uncrewed ones are ordinary; blended wing bodies have been a standing subject of transport
research for three decades; series-hybrid propulsion has established precedent in small uncrewed
aircraft. **What this paper offers is the combination, the consequences of the choices inside it,
and an accounting of what they cost** — not a claim that the route was waiting to be found.

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
| Eşeksenli karşıt dönüşlü kuyruk üstü, gerekçe tork dengeleme | Novlit ve ark. 2014, `cfd/2014_0529_paper.pdf`: *"A pair of 10 inches coaxial contra rotating propellers is mounted to compensate each other's torque"* — **birinci elden** |
| Askı kontrolünün yerleşik cevabı: slipstream içinde elevon ve rudder | Novlit ve ark. 2014, aynı belge: *"Elevon and rudder are immersed in the propeller slip stream to provide three axis control moments in hover"* — **birinci elden** |
| Tepki torku yerleşik bir yatış kanalı; diferansiyel devirle | Zhang ve ark. 2012, `cfd/ica20120400001_12673514.pdf`, satır 128–130: *"It balances the anti-torque of the rotors by the inverse rotating of the two rotors"* — **birinci elden** |
| Aynı kanal dikey kipte *yaw*, yatay kipte *roll* adını alıyor | Zhang 2012 **Tablo 2**, satır 159–165: Yaw/Vertical = *"Differential velocity of the two motors"*; Roll/Horizontal = aynı — **birinci elden** |
| Eksen adlarının askıda yer değiştirmesi literatürde adlandırılmış | Novlit ve ark. 2014, satır 118–123: *"the definition of the roll and yaw angles are interchanged"* — **birinci elden** |
| Kuadrotor kuyruk üstü yatışı bağımsız rotorların tepki torkundan üretir | Oosedo ve ark. 2013 (De Wagter 2018 içinden); Zhang 2012 aynı ilkeyi eşeksenli çiftte gösteriyor |
| Üç öğenin hiçbiri yeni değil | `paper/v8/07-the-combination.md` açılışı |

**Bu sayfada BİLEREK olmayanlar:** tek bir başarım sayısı, bu uçağa dair hiçbir tarif, ve
çağdaş hibritlerin **işe yaramadığı** iması. Boşluk bir **başarım** boşluğu olarak değil,
bir **araç** boşluğu olarak konuyor — çünkü makalenin iddiası da o.

**Adım 7 ve Adım 9'un dayanağı artık burada.** Her ikisi de *"yeni olan şey birleşme ve
araçtır"* diyor; bu sayfa o cümlenin karşılığını veriyor ve neyin yeni **olmadığını** açıkça
sayıyor.
