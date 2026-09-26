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

**Tur 47 düzeltmesi — yatış ekseni.** ChatGPT *"yatış pervanelerle ÜRETİLEMEZ"* cümlesinin
tepki torkunu atladığını gösterdi; §2.9 her rotorun **kendi elektrik makinesinde** olduğunu
söylüyor, dolayısıyla diferansiyel devir gövde ekseni etrafında net tork verir. Zhang ve ark.
2012 (`references/ica20120400001_12673514.pdf`) bunu **birincil kontrol kanalı** olarak kullanıyor.
Qwen ayrıca §2.10'un askı paragrafındaki *"thirty-degree bank"* ifadesinin aslında bir **yön
değişimi** olduğunu gösterdi. İddia daraltıldı: **fiziksel imkânsızlık değil, tasarım seçimi.**
Ayrıntı ve alıntılar: `paper/roll-axis-finding.md`.

---

## The combination

None of the three elements is new. **Each can be found on its own, and in
combination, in the literature and in hardware** — Section 1 says where.

**What this paper contributes is that combination, the condition its primary propulsor is designed
to satisfy, and the price the configuration pays for pursuing it.** The three elements, taken together, meet the escape condition
of Section 3 **in the propulsor that carries the aircraft**, and they meet it with no mechanism
that reorients a propulsor. The assembly is not offered as novel because it is an assembly. It is
offered for what it satisfies, and for what it does not need in order to satisfy it — and Section 1
has already set out how much of the ground is occupied.

**The qualification in that sentence is not decoration, and it is made here rather than
conceded later.** Section 3 lists partial instantiation among the ways an architecture can fail
the condition: meeting it where the aircraft is carried and failing it elsewhere. That is this
configuration's own case. The single nose pair meets all four parts — same hardware, both duties
served, one orientation, hover peak from a buffer. The four attitude pairs do not: they are exposed
in the cruise flow and they cannot be feathered, so they re-open the second charge. **The
instantiation is therefore partial**, and reporting what the failing part costs is a substantial
share of what Section 11 does.

The condition asks for one set of hardware to serve both regimes in one orientation,
with the hover peak drawn from a buffer. Each element supplies one part of it, and none
of them supplies it alone:

- The **blended wing body** carries the cruise lift on a surface, so that cruise is
  wing-borne rather than thrust-borne. That is the second half of the union.
- The **tail-sitting stance** aligns the thrust axis with the body axis, so the propulsor
  that produces the thrust for vertical operation is the same one that produces the cruise
  thrust, holding
  one orientation relative to the airframe throughout. There is no dedicated lift system to
  carry, and vertical operation does not depend on a runway. That is the first half.
- The **series-hybrid buffer** releases the continuous power plant from the hover peak,
  so that it is sized by cruise rather than by a condition holding for about two percent
  of the flight.

The configuration is arranged to change regime by **rotating the airframe**. The propulsors hold
their orientation relative to the body from take-off to cruise; what changes is the
orientation of the body relative to the flight path. A tilting architecture reaches the
same end by turning its propulsors instead, which requires a pivot and an actuator and
introduces gyroscopic coupling from the reorienting mass and a control problem through the
turn. It does not satisfy the condition as stated: the condition requires one orientation
relative to the airframe, and turning the propulsors is the case the condition excludes.
Here the end is reached by turning the thing the propulsors are already attached to, which
leaves the orientation requirement intact.

That single move is what removes the need for the mechanism. **The table below counts mechanism classes that
exist in order to change regime, or to take a rotor out of one regime's flow.** The strip of Section 8 is a
control surface, of a different class, and is named below and in Section 8 rather than in the table. The configuration therefore carries:

| Mechanism | Where it is required | Present here |
|---|---|---|
| Pivot or tilting joint | Tilting architectures | — |
| Nacelle or rotor-group actuator | Tilting architectures | — |
| Variable-pitch hub | Architectures that trim a rotor across two widely separated operating points, or feather a rotor unused in one regime | — |
| Dedicated lift rotors | Lift-plus-cruise architectures | — |
| Rotor stowing, indexing or stopping mechanism | Architectures that remove dedicated lift rotors from the cruise flow by such means | — |

Attitude is produced instead by differential thrust between fixed-pitch propellers: a
single coaxial contra-rotating pair at the nose, and four small coaxial pairs at the
ends of the tip frames, whose moment arms give pitch and yaw directly. The tip pairs are
sized from the moment requirement rather than from weight support, but the thrust that sizing
gives them also supplies the aircraft's entire take-off margin, because the nose pair is sized
at thrust equal to weight and no more. This dual role is a dependency, reported as one where the sizing is audited, and it does not make the tip pairs a dedicated lift system.

**The claim is narrower than it may appear, and the boundary matters.**

This is not a configuration in which nothing moves. Roll cannot be produced by the
propellers' **thrust**: every thrust vector is parallel to the body axis, so no combination
of thrust settings produces a moment about that axis. It **could** be produced by their **reaction
torque**, and this configuration declines that channel by design (Section 8), assigning the axis to an aerodynamic
device instead. The device is the only moving aerodynamic
surface on the aircraft — a variable-extension strip on the lower surface, modulated rather
than switched, which also pitches the nose down by a small increment when it is deployed. The
strip is part of the configuration and is named here rather than later, because a claim about
eliminated mechanisms that omitted it would be false.

A fixed-pitch propeller that serves two regimes pays in efficiency in at least one of them. The nose pair holds one
orientation, which is the architectural claim, but it also holds one blade geometry across a
hovering condition and a cruising one, and no single fixed-pitch blade is at its best in both.
That is a price of refusing the variable-pitch hub rather than an argument against refusing it,
and it is charged in Section 11 with the other costs of the union, not settled here.

Nor is this a claim of mechanical simplicity. Part count, mass, failure modes and
maintenance burden were not measured, and nothing in this work supports a statement
about reliability. What is offered is a **count**: the classes of mechanism that a
tilting architecture requires to change regime, and which this arrangement does not
require. The actuator inventory that replaces them is the propulsion motors together
with the strip.

**One thing this section does not establish, and Section 9 holds it to that.** The arrangement
described here requires no mechanism to change regime. **Whether this aircraft can actually perform
the change is a separate question and is not settled anywhere in this paper**: whether the moment
available is sufficient, and whether the aircraft trims through the rotation, depend on
aerodynamics that — for the methods used here and the published comparisons against which they were
checked — are not reliable above roughly ten degrees of incidence, which is inside the band the
rotation passes through. **The mechanism claim is about hardware and survives that limit. The
transition claim is not made.**

The combination carries costs: the attitude rotors that make the union controllable are themselves
exposed in cruise, and Section 11 charges them.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 98 (dört okuyucu + Claude):** 7G — Adım 5D'nin birebir cümlesi çıktı; "This dual role is a dependency, reported as one where the sizing is audited, and it does not make the tip pairs a dedicated lift system." (Qwen'in göndergesi). 7L kalıyor (dört okuyucu + Claude; iz: köprü/kapanış, yineleme değil). Özgün Ek S7'de | Tur 97 metni §5 |
| **Tur 97 (yeniden kurma; dört okuyucu + Claude):** envanter teyit edildi; 7A ortadaki üç cümle çıktı (Adım 1G'nin yinelemesi; ev 1G). **Uygulanmadı:** 7G (onarım biçimi ayrışık: "It" / "That" / "This dual role"); 7L (Grok ve Qwen çıkar, ChatGPT ve DeepSeek tut — köprü/kapanış). Özgün paragraflar Ek S7'de | Tur 96 metni §7 |
| **Tur 67 — V2, Grok'un ifadesi** (dört okuyucu + Claude): *"pays in efficiency in at least one of them"* — bedelin birimini adlandırıyor, sayı eklemiyor; Adım 3'ün *"the compromise is paid in efficiency"* cümlesiyle aynı güçte (Qwen) | Adım 3 |
| **Tur 66 — B4 (3.2) ve ses geçişi V1, V2, V6** (dört okuyucu + Claude): tepki torku tek cümle (*"could"* + *"by design"* = tasarım kısıtı, fiziksel imkânsızlık değil); şerit dışlaması kural olarak; *"pays for it"*; *"carries costs"*. **V3 ve V5 kaldı** (herkes korudu), **V4 kaldı** (Grok: olumlu hâli koşulun karşılandığını ima ediyordu — uç çiftleri karşılamıyor) | Adım 8; ChatGPT'nin A–D kuralı |
| **Tur 64:** *"removes the mechanism"* → *"removes the need for the mechanism"* (ChatGPT önerdi; beşimiz hemfikir) — bir şey sökülmüş gibi okunmasın; korunan liste aynı commit'te güncellendi | `v8-caveats.md` ruh listesi |
| **Tur 59:** *"The configuration is arranged to change regime by rotating the airframe"* — P1 fiili | Adım 1 (P1); Grok'un Adım 14 işaretinin yayılması |
| Kaçış koşulu: tek donanım, tek yönelim, tampondan tepe | v7 özeti, satır 55 |
| Her itki vektörü gövde eksenine paralel; itkiden yatış momenti yok | §2.10, satır 810–812 |
| Tepki torku bir yatış kanalıdır; her rotor kendi elektrik makinesinde | §2.9, satır 784–785 |
| Kuyruk üstü literatürü bu kanalı kullanıyor | Zhang ve ark. 2012, `references/ica20120400001_12673514.pdf`: *"Roll motion is controlled by the differential velocity of the two motors"* |
| Kaynağın *"roll cannot be produced by propellers at all"* cümlesi **daraltıldı** | §2.10, satır 813–814 aşırı iddia; `paper/roll-axis-finding.md` |
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
