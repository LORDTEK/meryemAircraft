# Step 5 — The first half: operation without a runway

**v8 taslağı, birinci yazım.** İskeletin 5. adımı. Rakip **sabit kanatlı**, ve **yalnız bu
eksende.**

**Kural denetimi:** sabit kanatlıya karşı **menzil iddiası yok** (§0) · *"inşa gereği"*
geçmiyor · **boyutlandırıldı / gösterilmedi** ayrımı sayfanın merkezinde (§0.3) ·
ChatGPT'nin Tur 45 şartı: bu sayfa uçağın dikey yeteneğini **kanıtlamaya çalışmıyor**,
gereksinimi kuruyor ve neyin boyutlandırıldığını söylüyor.

---

## The first half: operation without a runway

### The opponent, and the axis

On this axis the alternative is the fixed-wing aircraft, and the comparison runs one way only.
**Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency**, where a
runway-launched aeroplane that never bought vertical capability pays none of the charges of
Section 2 and is the better machine. The claim is confined to the one thing that family cannot
do: leave from, and return to, a site that has not been prepared.

### What the requirement actually is

"Vertical take-off" is a weaker requirement than the one the missions impose, and stating the
stronger one first prevents the claim from being read as easier than it is.

A catapult-launched fixed-wing aircraft also leaves without a runway. What it does not do is
**come back** to the same unprepared site, and it does not travel without the launcher. The two
applications this work is aimed at — wildfire observation and response, and cargo delivery to
places without a runway — need the aircraft to arrive somewhere that has no infrastructure, and
to leave again.

So the requirement is: **the aircraft carries everything it needs to depart and recover, and the
site supplies no prepared launch or recovery infrastructure of any kind.** The ground is the only
thing the site provides, and it provides it unprepared. A net, a catapult, a cradle, a prepared
strip or a recovery vehicle each fail that test — including the ones that fail it only on the
recovery half.

### How the configuration meets it

The aircraft stands on its tail, with its longitudinal axis vertical, in its own storage
attitude. **No launch equipment is present.** It rests on five points: the four lower ends of
the tip frames and the aft end of a keel running along the centreline.

**Those five points are not added hardware.** The tip frames are the landing structure, they are
also the structure that carries the attitude propellers and sets their moment arm, and their
fairing is the aircraft's only vertical surface. **One structure serves four purposes and is
charged to the mass budget once** — Section 8 gives the fairing's sizing.

**The saving has precedent and it is not this paper's observation.** Reviewing the tail-sitters
of the 1950s, NASA recorded that *"dispensing with a conventional landing gear improved the
empty weight fraction for these VATOL aircraft"*, while noting that some form of gear was still
required on the tail surfaces, that such gear was limited to low sink rates, and that tip-over was
*"a constant worry in gusty air and on uneven ground, particularly with the propellers turning."* The present arrangement takes that benefit and extends it by
giving the same structure the control duty as well.

**And the stance base is a parameter rather than a constraint.** Moving the frame ends further
outboard widens the base against ground wind without altering the planform, the propulsion or
the control architecture — and because the same displacement lengthens the control moment arm,
both benefits arrive from one change. The 50 kg reference geometry is one point on that trade; an
operator with a stronger ground-wind requirement can take another.

### What is sized, and what is not demonstrated

This is the part of the section that decides whether the rest of it can be trusted.

**Sized.** The vertical phase is sized: hover power from momentum theory at thrust equal to
weight, the buffer that supplies what the engine cannot deliver of that peak — at a specific power
Section 14 examines — the
tip-frame lengths that set both the stance base and the control arms, and the structure that
carries the landing loads. Those numbers exist and Section 10 reports **whether** they close, and
with what margin. This section does not assert the outcome of a calculation it does not contain.

**Not demonstrated, and the list is not short.**

**The aircraft leaves the ground on its control propellers.** Hover power is sized at thrust
equal to weight, so the primary propulsor supplies a thrust-to-weight ratio of exactly one and
no more. The take-off margin comes from the four tip pairs, which were sized from the moment
requirement rather than from weight support. That is the one place the configuration asks a
component to do a second job it was not sized for, and it means the take-off margin and the
attitude authority are drawn from the same four propellers and compete for it.

**The vertical descent has not been analysed.** A rotor descending into its own wake can enter
the vortex ring state, in which thrust becomes erratic and adding power makes matters worse.
Whether this configuration's descent profile enters that region, and at what rate of descent,
is an open question in Section 14 rather than an answered one here.

**Neither has the landing transition.** The forward rotation and the reverse are not symmetric
and must not be assumed to be. Going out, the rotation builds dynamic pressure while it turns,
so lift arrives to replace the vertical component of thrust as that component falls. Coming
back, the race runs backwards: dynamic pressure is falling while the aircraft is being turned,
so lift is leaving at the moment the thrust vector has not yet returned to vertical. **A model
built for the first case cannot be read for the second by changing a sign, and no figure in this
paper describes the landing transition.**

**Hover attitude control is sized but not demonstrated as a closed loop.** The moments available
about each axis are computed, but no control allocation has been closed around them and nothing
has been simulated or flown. That gap is wider than it looks, because this configuration declines the reaction-torque channel that comparable
aircraft use about the body's longitudinal axis (Section 8), leaving that axis to the strip.
**What that refusal costs in authority and in response time is not computed**, and Section 14
carries it.

**And one historical difficulty is inherited rather than removed.** A tail-sitting aircraft on
the ground is more exposed to crosswind and to uneven ground than a conventional one. The stance base is the answer
this configuration offers, and it is a parameter rather than a proof.

### What the historical record does and does not give back

One of the 1954 objections is genuinely removed and it should be named exactly. The landing
difficulty of the 1950s tail-sitters was attributed to a pilot judging a backwards vertical descent by looking
over his shoulder, to turbulence sensitivity and to reduced control power near touchdown.
**There is no pilot here, and height above ground is a sensor measurement rather than a human
estimate.** That disposes of the spatial-orientation objection and nothing else. **Precise
hovering, ground gusts and the descent itself are not disposed of by removing the pilot**, and
this section does not pretend otherwise.

### What this half costs

Runway independence is not obtained free, and the charges appear later rather than here. The
tip frames that make the aircraft self-supporting are structure standing in the cruise
airstream, and Section 11 charges their drag. The attitude propellers they carry are exposed
for the whole cruise and cannot be feathered, and Section 11 charges that too. The buffer that
releases the engine from the hover peak is mass carried for the whole flight.

**The second half — cruise carried on a wing rather than on rotors — is the subject of the next
section**, and the two are combined in Section 7.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 95 (yeniden kurma; dört okuyucu + Claude):** envanter teyit edildi. S-24 — 5C alıntısı sürdürüldü ("that such gear was limited to low sink rates, and that tip-over was 'a constant worry in gusty air and on uneven ground, particularly with the propellers turning.'"), 5D'ye "and to uneven ground"; S-25 — "The landing difficulty of the 1950s tail-sitters was attributed…"; "What that refusal costs … is not computed" korunan (164). **Açık:** 5D işaret cümlesi (üçü çıkar, DeepSeek tut). Özgün paragraflar Ek S5'te | NASA 19840014464 "In retrospect" paragrafı; 19810010574 XFY-1 satırı |
| **Tur 66 — B4 (3.1):** tepki torku kanalının açıklaması Adım 8'e; burada işaretçi ve *"not computed"* sınırı (dört okuyucu + Claude) | Adım 8 |
| **Tur 60:** *"50 kg reference geometry"* — terim birliği | Adım 8 tanımı |
| Beş temas noktası: dört uç çerçevesi ucu + orta omurga | §2.11, satır 946–948 |
| Uç çerçeveleri pervaneler için eklenmedi; **iniş yapısıdır** | §2.11, satır 937 |
| *"Dispensing with a conventional landing gear improved the empty weight fraction"* | §2.11, satır 940–942, kaynak [2] |
| Tek yapı üç amaca hizmet ediyor, kütle bütçesine **bir kez** yazılıyor | §2.11, satır 950–952 |
| Duruş tabanı **parametre**, kısıt değil; uçları dışa almak tabanı ve kolu birlikte büyütüyor | §2.11, satır 954–960 |
| Gövde ekseni dikey, kendi depolama durumunda, **fırlatma teçhizatı yok** | §3.12, satır 2103–2105 |
| Burun çifti T/W = 1,00 tam; kalkış marjı uç çiftlerinden | §3.15, satır 2624–2627 |
| Kalkış marjı ile tutum otoritesi **aynı dört pervaneden** ve yarışıyorlar | §3.15, satır 2630–2631 |
| Dikey iniş **analiz edilmedi**; girdap halkası durumu açık soru | §3.16, satır 2279–2285 |
| İniş geçişi de analiz edilmedi; ileri ve geri **simetrik değil** | §3.16, satır 2287–2297 |
| *"No figure in this paper describes the landing transition"* | §3.16, satır 2296–2297 |
| XFY-1'in iniş güçlüğü: omzunun üstünden bakan pilot; **burada pilot yok** | §3.16, satır 2275–2278 |
| Yanal rüzgâr maruziyeti **miras alınıyor** | §1.5, satır 483–485 |

**Bu sayfada BİLEREK olmayanlar:** sabit kanatlıya karşı **hiçbir menzil ya da verim
karşılaştırması**, ve uçağın dikey işletimi **gösterdiği** iması. ChatGPT'nin Tur 45 şartı:
*"Adım 5, uçağın dikey yeteneğe sahip olduğunu KANITLAMAYA çalışmasın; rakibi ve görev
düzeyindeki gereksinimi kursun, sonra neyin boyutlandırıldığını neyin gösterilmediğini
söylesin."* Sayfa bunu yapıyor ve gösterilmeyenler listesi **dört maddelik**, kısaltılmadı.
