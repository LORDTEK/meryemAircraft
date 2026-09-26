# Step 2 — The tax

**v8 taslağı, birinci yazım.** İskeletin 2. adımı. Dört dış okuyucunun dördü de sıradaki
adımın bu olduğunu söyledi: 7 ve 8 yazılmış durumda ve ikisi de var olmayan bir kaçış
koşuluna atıf yapıyor.

**Kural denetimi:** çerçeve **araç** olarak sunuluyor, ikinci katkı olarak değil (§0.6) ·
"önceki sürümde" anlatısı yok · menzil iddiası geçmiyor · Qwen'in testi: okuyucu
*"bana bir çerçeve gösterildi"* değil *"sıradakini değerlendirmek için gereken aleti aldım"*
demeli.


**Tur 56 düzeltmesi.** Başlık *"The charges behave as one quantity in three currencies"* idi; Adım 12
tam tersini sınayıp *"not one quantity under two names"* sonucuna varıyor. İskeletin niyeti *"üç
bağlaşık fatura; her çare aktarır"*. Başlık *"The charges are coupled: remedies move cost between
them"* oldu ve ChatGPT'nin cümlesi eklendi (*"distinct accounting quantities, not assumed to be
independent physical causes"*). Öngörü cümlesi ChatGPT/Qwen'in koşullu biçimine getirildi (*"will
reverse where that reweighting carries it past the point at which the two break even"*). Dört okuyucu
da daraltmayı *"düzeltme, kale taşıma değil"* buldu.

---

## The tax

A claim that one architecture escapes a cost shared by the others is only meaningful if the
cost is stated first, in terms that do not presume the escape. This section states it. It is
not a claim about any particular aircraft, and nothing in it is new physics; what it provides
is the accounting that the rest of the paper is checked against.

### The root: a duty cycle that does not match the hardware

The vertical phase is short. For a mission of one hour, a take-off, a transition, a return
transition and a landing occupy on the order of a minute — **roughly two percent of the flight.**
Any hardware installed for that phase alone is carried through the remaining ninety-eight
percent.

**An architecture that provides the vertical phase with a dedicated lift subsystem therefore
carries it for fifty times as long as it uses it.** This is not an implementation defect and it
cannot be removed by making the subsystem better, because it is a statement about duty cycle
rather than about quality: a lighter or cleaner lift rotor is still carried for the whole flight. **The mismatch between how long a
component is needed and how long it is present is the origin of all three charges below.**

The statement is deliberately confined to architectures with a dedicated lift subsystem, because
that is the family the charges describe. Whether any architecture avoids the mismatch — and what
it pays instead — is the subject of the next section, and it is not settled here.

### Bill 1 — mass

The most direct payment is dead mass. A lift-plus-cruise aircraft carries two propulsion
groups: rotors, motors, mounts, wiring and structural reinforcement for the vertical phase, and
a separate propulsor for cruise. The vertical group provides no required lift or thrust during cruise and is
lifted anyway.

Its cost is not linear. Mass growth feeds itself — MTOW = m_payload / (1 − f_empty − f_energy)
puts additional empty mass through a multiplier that grows as the denominator shrinks — and in
the vertical phase the same increment is counted a second time, because at a fixed disc area
hover power scales with W^1.5. *(The exponent is a property of the scaling rule chosen: holding
disc loading constant instead makes hover power grow linearly with weight, and Section 12 uses
that.)* A modest dead-mass fraction becomes a large payload penalty.

**This charge has been identified independently, and by a source with no interest in the present
argument.** A NASA study sizing five VTOL architecture families against a common mission with common
tools found the lift-plus-cruise concepts the heaviest of the vehicles examined, and named the
cause: not the cruise power draw, since the lift-plus-cruise effective lift-to-drag ratio is the
higher of the set, but *"the extra empty weight items on board in hover."*

**That finding separates the two things this paper is at pains to keep separate.** The
lift-plus-cruise vehicle is *aerodynamically better* than the alternatives and it is nevertheless the heaviest, because of
hardware carried in order to hover. That is Bill 1 stated by an independent source in its own
terms: not a failure of engineering, but the cost of an architecture.

A second NASA review gives the structural half as a general principle, drawn from a tilt-prop
aircraft whose propeller separated in flight after a gearbox mounting fatigued: to transmit
power safely to the extremities of the planform, *"very strong (and fatigue-resistant)
structures must be incorporated with an obvious weight penalty."* Distributing lift or thrust
across the span therefore obliges the structure that reaches it to keep transmitting power
there — charged to mass, whether or not the distributed propulsors are running.

### Bill 2 — drag

The second payment falls on architectures that leave hover hardware exposed in forward flight:
rotors stopped in the airstream, the booms that carry them, and the interference between their
wakes and the wing. Cruise drag has other sources on any aircraft; what is charged here is the
part attributable to hardware retained for a phase that is over.

Wind-tunnel work on a hybrid airframe found that the difference between propellers parallel to
the airflow and no propellers at all is modest, while *"the drag produced by the motors is
significant."* The bill is charged mainly by the motors and the beams that carry them —
hardware that cannot be feathered, folded or aligned away, **because its cost is its presence.**

Two further measurements support the direction. Characterisation of a quadplane found the
highest lift and least drag in fixed-wing mode at both cruise airspeeds, with drag in the hybrid
regime exceeding either pure mode through adverse flow interaction; and that a simulation assuming negligible rotor–structure
interaction *"always predicts higher lift and lower drag than were experimentally observed."*
Separately, a study of twenty-six stationary lift propellers held edge-on found their drag
scaling with frontal area and the square of airspeed, with hover powertrain components adding
*"a significant amount of aerodynamic drag during forward flight"* in the absence of a stowing
mechanism.

**The important property of this charge is not its size but where it falls.** It is charged per
unit time in cruise — so it grows with exactly the quantity the aircraft exists to maximise.

### Bill 3 — power system sizing

The third payment is the least visible. A VTOL aircraft must install
enough power to hover, but it draws that power only during the two percent of the flight in
which it hovers. The ratio between the two demands follows from the governing equations rather
than from any design choice. Taking hover power from momentum theory and cruise power from the
drag polar,

    P_hover / W  = √(DL / 2ρ) / η_h                 (DL = W/A, disc loading)
    P_cruise / W = V / ( (L/D) η_p )

so that

    P_hover / P_cruise = √(DL / 2ρ) · (L/D) / V · (η_p / η_h)

**The quantities on the right come from the configuration and from the propulsion operating
points, not from the duration of the hover phase.** That distinction matters and the efficiencies
are the reason for it: η_h and η_p are not configuration constants, they depend on the propeller
and on the condition it is run at, and Section 11 computes what happens when one fixed-pitch
blade has to supply both.

A vehicle with a disc loading of 100 N m⁻², a cruise lift-to-drag ratio of 15 and a cruise speed
of 30 m s⁻¹ needs **between three and four times** as much power to hover as to cruise: the
geometric terms alone give 3.2, and the efficiency ratio η_p/η_h carries it to about four when
the cruise propeller is roughly a quarter more efficient than the hover rotor. Raising the disc
loading raises the ratio as its square root.

The power system is therefore sized by a condition that holds for a minute and is then carried,
unused, for an hour. And the consequence propagates: sizing by hover means an oversized engine,
or a battery that must deliver a peak it will rarely be asked for, or both — and whichever is
chosen, the extra installed capacity is mass: a cost in kilograms, though not Bill 1.

### The charges are coupled: remedies move cost, among the three charges or outside them

The three charges are not independent problems with independent fixes. **Each known partial
remedy reduces one charge and pays for it, in another charge or in a cost outside the three.** They are three distinct accounting quantities — kilograms,
drag counts, installed kilowatts — and they are not assumed to be independent physical causes: a
remedy can move a requirement from one currency into another. Whether a change of size moves them
together, which would make them one quantity under three names, is tested in Section 12.

**A charge and its currency are not the same thing.** The mismatch of the root is the origin of all three charges; each
charge is one specific payment, not the name of the currency it is paid in. Bill 1, as this accounting uses it, is the mass
of a dedicated lift subsystem; Bill 2, the cruise drag of hover hardware left exposed; Bill 3, continuous power installed
to a hover peak. A remedy's own cost can fall in kilograms, drag counts or installed kilowatts without being one of the
three charges, and the table names such a cost in words rather than by a bill's number.

| Move | Bill it attacks | What it creates — a bill by its number, any other cost in words |
|---|---|---|
| Distributed electric lift rotors | 3 — the cruise engine no longer sizes to hover | 1 and 2 — many rotors and mounts, permanently carried and exposed |
| Folding or retracting lift rotors | 2 — the exposed rotor is removed from cruise | 1 — mechanism, actuation, locking; and a new failure mode, not among the three |
| Tilt-rotor, tilt-wing, tilt-nacelle | 1 — one propulsion group serves both regimes | kilograms, not Bill 1 — the pivot and its actuators; **Bill 3**, imposed or left standing according to how the architecture the move modifies supplies its hover peak — with no store, the power plant is sized by the hover peak; and gyroscopic coupling and a transition control problem, which are **not among the three** |
| Variable-pitch or feathering propulsors | 1 and 3 — one propulsor is retrimmed across two widely separated operating points instead of duplicated | kilograms, not Bill 1 — pitch hub and actuation; and a new failure mode, not among the three |
| Higher disc loading, smaller rotors | 1 and 2 — smaller, lighter, cleaner rotors | 3 — hover power rises with √(DL) |
| Lower disc loading, larger rotors | 3 — hover power falls | 1 and 2 — larger structure and exposed area |

**One row pays part of its cost in none of the three currencies, and that is not an oversight.** What a
tilting architecture buys its unified propulsion group with is a mechanism — a pivot, an
actuator, the gyroscopic coupling of a reorienting mass, and a control problem through the turn.
The pivot and the actuator are paid in kilograms, although they are not lift-subsystem mass; the
coupling and the control problem are paid in none of the three. That part is a cost, but it is not
one of the three charges this accounting tracks, and the next section says why it is treated
separately. **The table is not a census of the field**; it lists
the moves whose transfers are documented, and a remedy absent from it is not thereby claimed to
cancel a charge.

**One of these transfers has direct experimental support, and it is worth more than the table.**
In the doctoral study whose wind-tunnel campaign is quoted above — and in that document rather
than in the journal article by the same author, which reports a different comparison — a
retraction system removed thirty percent of the airframe's drag; the same work then costed it. Applied to a passenger eVTOL, with the mechanism assessed
at five percent of vehicle mass, maximum range rose from 119 km to 121 km — **a two-kilometre
gain for a five-percent mass penalty.** Bill 2 was converted almost exactly into Bill 1, and
**the transfer is the point rather than the small residue.**

### What this accounting is for

**The accounting is refuted by a counter-example, and the table above is where one would appear:**
every entry in it moves cost rather than removing it.

**Stated positively, so that the test can actually be run: a counter-example is a remedy that
reduces one of the three charges, leaves the other two no worse, and whose own cost is either
absent or demonstrably smaller than the reduction — measured in the same currency.** That last
clause is what makes the test usable rather than rhetorical: mass against mass, cruise drag against
cruise drag, installed continuous power against installed continuous power. **The accounting claims
transfer. It does not claim that every architecture is equally good**, and a remedy that is simply
a better bargain in one currency refutes it.

**Two clarifications keep the test from being either too easy or unfalsifiable.** **"No worse" is
judged against the architecture the move modifies.** A charge that architecture already paid, left no
larger, is no worse. A charge it did not pay, imposed by the move, is worse; so is one it paid, enlarged
by it. A move that reduces one charge and makes another worse is a transfer between charges. And a remedy whose cost
falls **outside** the three charges does not refute the accounting, because the accounting is about
those three; **but it is not thereby exempt from being counted.** The tilting family's mechanism is
named in the table for exactly that reason, and it is the reader's to weigh against what the
remedy buys. **A framework that could absorb any cost by declaring it out-of-scope would be
unfalsifiable**, so the costs outside the three are listed, not waved away.

**The tilting row needs both clarifications.** If the architecture it modifies supplies its hover peak
from a store, tilting without one imposes Bill 3 and the row is a transfer. If that architecture
already sizes its continuous plant by the hover peak, tilting leaves Bill 3 no worse; then, where the
mechanism's kilograms are fewer than those of the lift group it removes, what keeps the row from
refuting the accounting is the part of its cost that falls outside the three — which is why that part
is listed.

It also makes a prediction that can be checked without settling the architectural question at
all: **where an arrangement pays one charge heavily in order to escape another, its ranking
against a differently-balanced arrangement will move when the sizing rule changes — toward the
lighter arrangement as the rule weights mass more — and will reverse where that reweighting carries
it past the point at which the two break even, where the mass difference as the contract counts it and
the cruise-efficiency difference cancel in the range.** Section 13 tests both the
movement and the reversal on this configuration, and Section 4 tests a different consequence
against a sizing study this work did not produce.

**The moves in the table are partial remedies: each accepts the duty-cycle mismatch and then
redistributes what it costs.** Whether an architecture can decline the mismatch itself, rather
than redistribute its consequences, is a different question, and the next section states the
condition it would have to meet — a definition, derived from the table above rather than from
any aircraft.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 89 (içerik, S-15/S-16; dört okuyucu + Claude):** 2E "Each known partial remedy reduces one and raises another" → "reduces one charge and pays for it, in another charge or in a cost outside the three"; 2F ilk paragraf (iki farklı sınama) → "The accounting is refuted by a counter-example, and the table above is where one would appear: every entry in it moves cost rather than removing it."; 3.1 "…is a transfer between charges"; başlık "remedies move cost between them" → "…among the three charges or outside them" (dördü değişsin dedi; sözcük DeepSeek'inki, teyide); 2B "charged a second time" → "counted" | Tur 88 metni §2 |
| **Tur 88 — S-14 silindi:** kuyruk üstü "beşte bir" cümlesi — dört okuyucunun koşulu ("gelecek tura kadar kaynak gelmezse sil") gerçekleşti; hiçbir okuyucu kaynak bulamadı (Grok aradı), depoda yok, yazara soruldu. Örnek oran (3,2; ~4) ona dayanmıyor. Yazar kaynağı bulursa geri gelir | Tur 87 metni §5 |
| **Tur 88 (yeniden kurma, 2A–2D):** 1 281 → 1 233. A1 R ("lighter or cleaner"), B1 D, C1 D, D1 D ("often the largest" — kaynaksız), **S-13** D2 ("returns to Bill 1" → "a cost in kilograms, though not Bill 1"), **S-14** D3 ("borne out" → "points the same way"; ifadeyle eşleşme düştü; kaynak yok — gelmezse silinecek). Dört okuyucu + Claude. Özgün Ek S2'de donmuş | Tur 87 metni |
| **Tur 83 (içerik):** S5-1'in tanımı üç cümle — "left no larger" (azalan dahil), "imposed … so is one it paid, enlarged by it", aktarım yalnız "reduces one charge and makes another worse" birleşimi. Dört okuyucu + Claude (Grok ilk ayrımını yüksek disk yükü satırıyla geri çekti) | Tur 82 metni §3 |
| **Tur 81 (içerik):** S-5 — 2F'de taban adlandırıldı (S5-1: "No worse" değiştirilen mimariye göre), eğme satırı iki kollu koşullu (S5-2, son cümleciği korunan), eğme hücresi "imposed or left standing" (S5-3). Dört okuyucu + Claude. Emekli: "is not a counter-example — the tilting row", "Bill 3 is left standing" | Tur 80 metni §2 |
| **Tur 80 (içerik değişikliği, kısaltma değil):** fatura ile para birimi ayrıldı — 2E'ye A′ paragrafı; tablo başlığı H; katlama (C5), eğme (B′), hatve göbeği (C4) hücreleri; "One row" paragrafı (C). Dört okuyucu + Claude, Tur 79 paketi. Gerekçe: pivot kilogramı 3B, S4 (146 lb) ve Adım 4'te vardı, tablo satırı "üç birimin hiçbirinde ödemez" diyordu. Emekli: *"does not pay in any of the three currencies"* | Tur 79 metni §2 |
| **Tur 65:** tilt satırından *"mechanical complexity,"* çıktı — ölçülmedi; Adım 3'ten aynı gerekçeyle çıkmıştı (dört okuyucu + Claude hemfikir). Mekanizmanın bedeli düzyazıda duruyor: *"a pivot, an actuator, the gyroscopic coupling of a reorienting mass, and a control problem through the turn"* | bu bölümün tabloyu izleyen paragrafı |
| Dikey faz uçuşun ~%2'si; bir saatlik görevde ~bir dakika | §2.1, satır 524–527 |
| Uyumsuzluk üç faturanın da kökeni; kalite sorunu değil | §2.1, satır 531–534 |
| MTOW = m_faydalı/(1−f_boş−f_enerji); askı gücü W^1.5 | §2.2, satır 538–543 |
| NASA: lift+cruise en ağırı, sebep "askıdaki fazla boş ağırlık kalemleri" | §2.2, satır 546–552, kaynak [22] |
| Lift+cruise'un L/D_e seti içinde **daha yüksek** | §2.2, satır 549–550 |
| NASA: dişli yatağı yorulan tilt-prop; "çok güçlü yapılar... belirgin ağırlık cezası" | §2.2, satır 563–566, kaynak [2] |
| "Pervaneler akışa paralel olduğunda fark küçük; motorların ürettiği sürükleme önemli" | §2.3, satır 600–601 |
| Quadplane: hibrit rejimde sürükleme her iki saf kipten fazla | §2.3, satır 606–610 |
| Simülasyon "her zaman daha yüksek taşıma, daha düşük sürükleme öngörüyor" | §2.3, satır 610–612 |
| Yirmi altı durdurulmuş kaldırma pervanesi; alan ve hız karesiyle ölçekleniyor | §2.3, satır 612–615 |
| Fatura 2 seyirde **birim zaman başına** tahsil ediliyor | §2.3, satır 617–618 |
| Fatura 3 denklemleri ve P_askı/P_seyir bağıntısı | §2.4, satır 627–635 |
| DL 100 N/m², L/D 15, V 30 m/s → ~dört kat | §2.4, satır 635–637 |
| Karbon fiber kuyruk üstü: seyir gücü askının beşte biri | §2.4, satır 638–641 |
| Aktarım tablosu, beş satır | §2.5, Tablo 2, satır 655–661 |
| Geri çekme %30 sürükleme aldı; %5 kütle cezasıyla 119 → 121 km | §2.5, satır 663–666 |

| Değişken hatve satırı | Tur 41'de dördü de istedi; §2.9'un "no variable-pitch hub" elemesinin karşılığı |
| P_askı/P_seyir = 3,2 (geometrik terimler), η oranıyla ~4 | §2.4 denklemi, doğrudan hesaplandı |
| Sabit disk yüklemesinde askı gücü **doğrusal** | §3.9; `aero/closure.py` satır 50–54 |
| 119 → 121 km **tezde**, dergi makalesinde değil | `paper/bacchini-reading-record.md`; makale atfı [3] |

**Tur 41'de düzeltilenler.** ChatGPT ve Grok *"her hibrit VTOL dikey faz için donanım taşır"*
cümlesini yakaladı: evrensel olarak yanlış (tilt ve kuyruk üstü taşımaz) **ve kendi uçağımızı da
çürütüyor** — bizim de 1,8 kg tamponumuz dikey faz için. ChatGPT'nin teşhisi tam yerinde:
*"artık en büyük tehlike çerçevenin fazla belirsiz olması değil; sınayacağı mimari için fazla
evrensel ifade edilmiş olması."* Cümle **adanmış kaldırma alt sistemi olan** ailelere daraltıldı.

Dördü de **değişken hatve satırını** istedi. Eklendi — makalenin kendi katkısı o satıra karşı
tanımlanıyor.

Üçü bağımsız olarak *"kabaca dört kat"* aritmetiğini denetledi ve η oranı 1 iken 3,2 çıkıyor.
Düzeltildi: geometrik terimler 3,2, η oranı dörde taşıyor, ve bu **söyleniyor.**

Qwen çürütülebilirlik cümlesinin **tersine çalıştığını** gösterdi — *"hiçbirini ödemeyen bir
düzenleme varsa muhasebe ödemenin nereye gittiğini söyler"* bir sağlamlık iddiasıdır, çürütme
ölçütü değil. Çürütme ölçütü artık başta ve doğru: **bir faturayı bir başkasını yükseltmeden
kaldıran herhangi bir çare.**

ChatGPT *"sağdaki her terim yapılandırmanın özelliğidir"* cümlesini yakaladı — η_h ve η_p
yapılandırma sabiti değil, ve bunu **kendi pervane hesabımız kanıtlıyor.**

**Qwen'in bir sayısı yanlıştı ve düzeltildi.** Sabit disk yüklemesinde askı gücünün W^0,5 ile
ölçeklendiğini söyledi; doğrusu **W^1,0**, yani doğrusal: P = W^1,5/(η√(2ρA)) ve A = W/DL ise
P ∝ W. Bulgu geçerli (bağlam belirtilmeliydi), sayı değil.

**Eklenmeyen tek satır: seri hibrit tamponu.** DeepSeek istedi, ChatGPT "3. adım karar versin"
dedi, Grok'un kuralı belirleyici oldu: *"Kuyruk üstünü ekleme. Bu, onu yasaklayan sayfada kaçışı
uçaktan türetmek olur."* Tampon bizim mimarimizin parçası; vergi tablosuna girerse ölçüt
ölçülenden türemiş olur.

**Bu sayfada BİLEREK olmayanlar:** kaçış koşulunun kendisi (Adım 3), NASA sınaması (Adım 4),
ve bu uçağa ait hiçbir sayı. Vergi, uçaktan **önce** ve uçaktan **bağımsız** kurulur; yoksa
kaçışın ölçüleceği ölçüt kaçanın kendisinden türetilmiş olur.
