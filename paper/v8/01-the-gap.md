# Step 1 — The gap

**v8 taslağı, birinci yazım.** İskeletin 1. adımı. **Kararı ben verdim** — gerekçe aşağıda,
`cfd/arsiv-dis-gorus/external-review-49.md` §1'de de açık.

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
infrastructural: a runway, a catapult, or an equivalent installation.

**Rotorcraft** remove that requirement completely. They take off and land
vertically, hover, and work from confined sites. Their limit is the converse: with no wing,
every second of flight is bought with installed power, so range and endurance stay modest and
worsen as the vehicle grows.

**Neither family is deficient.** Each is limited by the price of
doing it that way. **The corner where both capabilities are wanted at once is where the two
applications this work is aimed at sit** — wildfire observation and response, and cargo delivery to
places without a runway.
**That corner is not empty**, as the rest of this section sets out; what is unsettled is which
price an architecture in it must pay.

### What the contemporary answers do, and how each changes regime

Hybrid VTOL aircraft occupy that corner today. **This paper does not dispute that they work.** They take two routes between the regimes: lift-plus-cruise aircraft keep two sets of hardware and switch
between them, and tilting aircraft keep one set and reorient it (Section 7). Rotating a propulsor in flight brings a pivot and its
actuators, a gyroscopic moment during the rotation, and a control problem through a regime in which the aircraft is neither a
rotorcraft nor an aeroplane. **Those are mechanical and control requirements rather than aerodynamic ones**, and that distinction is
what this paper is built on.

### The third route is established, and some of its difficulties are inherited

There is a third way to put one set of propulsors into both regimes without reorienting them: **point the
thrust line at the ground and let the whole aircraft rotate.**
The Convair XFY-1 flew it in 1954 and completed six transitions to conventional flight *"before testing was
curtailed because of engine and gear-box reliability problems"*, and uncrewed tail-sitters have revisited the
route since. The pilot's spatial orientation and workload were real, **but they are not what curtailed the testing**, and they are the only ones of those documented obstacles an uncrewed aircraft removes.

**Some of the difficulties were real, internal, and are inherited here.** A tail-sitting vertical descent is
harder than a runway landing; a tail-sitter on the ground is more exposed to crosswind; and propellers whose
thrust vectors are all parallel to the body axis produce no rolling moment **by any combination of thrust
settings**. The reaction-torque channel that other coaxial tail-sitters use about that axis is a choice this
configuration declines rather than a limit it inherits (Sections 7 and 8).

What has changed is electric drive on each individual rotor, sensor-based attitude reference, and enough onboard computation that stability need not come from the airframe alone. **The uncrewed tail-sitter literature has been exploiting exactly those three for over a decade**; the gap below is not a historical one.

### What is already occupied, stated before the gap

**The route itself is established.** Uncrewed tail-sitters combining fixed-pitch rotors with a
flying wing have been built and flown for more than a decade. A tail-sitter study reported in 2007 already states the
comparison: tilting configurations reach the same goal *"at the expense of significantly increased mechanical complexity compared to a
tail-sitter that uses propeller wash over normal aircraft control surfaces to effect vertical flight control."*

**Attitude without aerodynamic control surfaces is established**: a quadrotor tail-sitter operated without control surfaces, with
experimental verification, was reported in 2013.

**Coaxial contra-rotating propulsion on a tail-sitter is established**, proposed to cancel a single propeller's reaction torque without
complementary controls, at a cost its proposers name as added mechanical complexity; a tail-sitting micro air vehicle reported in 2014
uses a coaxial pair for the same purpose.

**The established answer to hover control on such a configuration is a surface in the slipstream**, and this paper refuses it. The 2014
vehicle places an elevon and a rudder in the propeller slipstream for three-axis control in hover; a flying-wing tail-sitter reported in 2018 uses elevons for two of its three axes and treats the propellers'
counter-moment about the thrust axis as a disturbance rather than a control channel, and reports hover and vertical flight only.

**And the reaction-torque channel this paper declines is established as a control channel.** A coaxial contra-rotating tail-sitter
reported in 2012 balances rotor torque by counter-rotation and unbalances it on purpose to steer: its published control scheme assigns
*"differential velocity of the two motors"* to yaw in the vertical mode and to roll in the horizontal one. **Those are the same physical
channel under two names**, a moment about the propeller axis, and independently driven rotors make it available to any coaxial pair.
**Using it is a choice, and so is declining it**, which is what separates this configuration's control problem from a physical
impossibility.

**A blended-wing-body tail-sitter with contra-rotating propulsion, aimed at disaster response, is established**, reported in 2025 with vortex-lattice and RANS analysis.

**A buffered series hybrid on a winged tail-sitter has been sized**: a 2026 study of 100 kg winged biplane tail-sitters sizes the engine
for cruise and a boost battery for vertical take-off and landing, and gives its rotors collective pitch change mechanisms.

**A coaxial tail-sitter with a series-hybrid store has been sized**: a long-endurance concept reported in 2025, with a fuselage and
tails, whose fuel cells charge a battery that drives the motor, because the fuel cell alone cannot fully power hover out of ground
effect at take-off; how its attitude is controlled, and whether its rotors vary pitch, the paper does not state.

**And the propeller compromise at the centre of this paper's own ledger is a known result, not a discovery.** The uncrewed tail-sitter
literature states that fixed-pitch propellers make it *"theoretically impossible to be very efficient in both hovering and forward
flight."* A long-range tail-sitter reported in 2018 names variable pitch as the remedy, at the cost of extra actuators and mechanism weight, and even with cyclic and collective pitch still sizes its rotor as a compromise between hover and forward flight.

### The gap, stated precisely

**Each half of the required capability is well served, and both halves together are served by
the contemporary hybrids.** This paper does not claim otherwise. **And the third route is
occupied.** What follows is therefore not a claim to an empty field.

**What is not established is the combination taken together with its price.** Specifically:
a blended-wing-body tail-sitter in which *every* propulsor is a coaxial, torque-balanced pair —
so that reaction torque and net angular momentum are given up along with the reorientation
mechanism — carrying no aerodynamic control surfaces beyond a single moving device, powered
through a buffered series hybrid, and **audited explicitly against carried hover mass, exposed
cruise drag and hover-sized continuous power**, the last two of them at two scales, and under three sizing
contracts.

Each of those choices costs something, and **the giving-up is the part that is not free**. **Operating every pair torque-balanced spends the reaction-torque channel to buy the torque balance and
the near-zero net angular momentum**, and leaves the moment about the propeller axis to a single aerodynamic device.

**None of the elements is new**, and Section 7 says so. Tail-sitting aircraft are seventy years old; blended wing bodies have been a standing subject of transport
research for more than three decades; series-hybrid propulsion has been designed for small uncrewed aircraft. The route is not claimed to have been waiting to be found. **The contribution is the
architecture: a configuration arranged to change regime by rotating the airframe rather than its
propulsors, and so carrying no mechanism that reorients a propulsor.** The combination, the
consequences of the choices inside it, and an accounting of what they cost are how that contribution
is presented and priced.


---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 195 — E28 (a), yazarın kararı:** 1.5'te *"has been flown in a crewed motor glider and"* düştü; cümle *"series-hybrid propulsion has been designed for small uncrewed aircraft."* Gerekçe: AIAA birincil kaynak ister; motorlu planörün (DA36 E-Star, 2011) tek birinci elden kaydı üretici haber sayfası, Schömann ikincil. Kalan yüklemi Merical ve ark. 2014 taşır (özet: tasarım ve benzetim). Eski paragraf S1'de; `paper/build/v8_round195_apply.py` | Tur 194; E28 |
| **Tur 191 — son okuma onarımı D2** (yazar E24): 1.3 korunan cümlede *"the only one"* → *"the only ones"* (sayı uyumu; iş yükü korunur); kayıt satırı da güncellendi. Eski paragraf S1'de | Tur 189; E24 |
| **Tur 187 — Bölüm 1 geçişi uygulandı** (`paper/build/v8_round187_apply.py`; Tur 186 oylaması): 10 R (*"and whether one arrangement pays less than it appears to"* düştü — sıralama vaadi gibi okunuyordu; beşimiz), 22 R (ikiye bölündü; beşimiz), 47 R (*"the axis"* → *"the moment about the propeller axis"*; beşimiz), 4 R-a (*"Rotorcraft remove …"*; yazar E22, 4'e 1). 23 ve 45 K. Eski dört paragraf ekte (S1) aynen; okuyucu teyidine | Tur 186 cevapları; E22 |
| **Tur 170 — yazarın notları üzerine kısaltma uygulandı** (Tur 168–169: işlemlerde dört okuyucu + Claude; korunan cümle taşımaları yazar kararı E13). Değişen her paragrafın eski hâli ekin bu adıma ait bölümünde aynen (*"… before the Round 170 shortening"*). Yeni (R) cümleler Tur 170 §2'de okuyucu vetosuna açık; sonuç teyide | `paper/build/v8_round170_texts.py`, `v8_round170_apply.py` |
| **Tur 171 — R2 onarıldı** (Grok vetosu, Tur 170): 1.3'te "onboard computation" kaynak ifadeye geri döndü — "electric drive on each individual rotor, sensor-based attitude reference, and enough onboard computation that stability need not come from the airframe alone"; korunan "those three" yine üç tam öğeyi sayıyor (sayma sözcüğü denetimi, benim hatam). +11 kelime. Teyide (Tur 171 §1) | Grok |
| **Tur 176 — Bölüm 1 son geçiş (yazar: "son kez yapıyoruz gibi düşünerek ne oluyorsa yap geç"):** 1.1 yan cümle, 1.2 R10 (NASA tek ev 2.3), 1.3 "It is neither new…" (yazar onayı), 1.5 R11 (tepki torku tekrarı) ve kapanış köprüsü (yazar onayı). Eski paragraflar ekte; okuyucu teyidine | — |
| **Tur 148 — W-5 uygulandı** (dört okuyucu + Claude; ChatGPT itirazını geri çekti): *"revisited the route continuously since"* → *"…the route since"* (1954'e bağlı; 2007'den tanıklı; *"nor abandoned"*ın paragraf içi dayanağı). W-9 kapandı | Tur 147 §2; Tur 148 §1 |
| **Tur 147 — W-9 uygulandı** (bütün okuma; dört okuyucu + Claude; silme + noktalama): *"Both work, and the second is the more demanding to build, because rotating…"* → *"Both work. Rotating…"* — ölçülmemiş karşılaştırma; 2007 alıntısı eğimliyi kuyruk üstüyle karşılaştırıyor. W-5 (*"continuously"*) ayrışık, geri soruldu | Tur 146 metni §5; Tur 147 §1 |
| **Tur 144 — W, E-1, N9 KAPANDI (dört okuyucu teyit etti); E-1′ uygulandı** (dört okuyucu + Claude; yalnız silme): *"states the same purpose in the same terms:"* → *"states the same purpose:"*; ifade emekli. Karmaşıklık izi (Q-P1b): *"mechanical complexity"* yalnız bu adımda (kaynak alıntıları), `v8_stale.py` YALNIZ; *"mechanically simpler"*, *"more reliable"* emekli (Adım 7 sayımı, Adım 9 madde 4) | Escareno 2007, 2008 |
| **Tur 143 — W, E-1 (b), N9 uygulandı (dört okuyucu + Claude).** W: rota maddesine *"A tail-sitter study reported in 2007 already states the comparison: tilting configurations reach the same goal 'at the expense of significantly increased mechanical complexity compared to a tail-sitter that uses propeller wash over normal aircraft control surfaces to effect vertical flight control.'"* (Escareno 2007 s. 3385; *"gives the reason"* dört okuyucuca fazla bulundu). E-1: *"… proposed specifically to face the reaction torque a single propeller imposes 'without using complementary controls', at a cost its proposers name directly: it 'increases the mechanical complexity.'"* (Escareno 2008 s. 262); eski bedel ifadesi emekli. N9: *"for more than three decades"* (Liebeck 2004 s. 10: 1988). Sonraki cümlenin *"in the same terms"*i açık (E-1′) | Escareno 2007, 2008; Liebeck 2004 |
| **Tur 142 — Escareno 2007 (tam), 2008 (s. 261–262) ve Liebeck 2004 birinci elden okundu** (yazar yükledi). Eşeksenli maddenin gerekçe yan cümlesi 2008 s. 262 ile birincil; bedel yan cümlesi De Wagter'den (ikincil) ve birincil onu *"it increases the mechanical complexity"* diye adlandırıyor (öneri E-1). *"three decades"*: Liebeck s. 10, 1988 (öneri N9). Rota maddesine Escareno 2007 s. 3385 önerisi (W) | Escareno 2007, 2008; Liebeck 2004 |
| **Tur 140 — 2013 tanığı birinci elden okundu** (Oosedo ve ark. 2013, ICRA, s. 317–322; yazar yükledi): *"A quadrotor tail-sitter operated without control surfaces, with experimental verification, was reported in 2013"* — s. 317 (*"does not use any control surfaces even in the level flight"*), s. 318 (kanatçık sabit), s. 321–322 (askı, geçiş, seyir uçuşu). Cümle değişmeden doğru | Oosedo 2013 |
| **Tur 139 — Vegh satırı KAPANDI** (dört okuyucu teyit etti) | Vegh müsveddesi R3 |
| **Tur 138 — Vegh dolu liste satırı (Öneri V; dört okuyucu + Claude; son yan cümle kalır — Q1 oybirliği; *"reported in 2025"* yer tutucu, sürüm gönderimden önce sabitlenir — Q2 oybirliği):** Rohith maddesinden sonra *"A coaxial tail-sitter with a series-hybrid store has been sized. … how its attitude is controlled, and whether its rotors vary pitch, the paper does not state."* Alıntılar s. 4, 7, 13; yokluk arama listesi ve sürüm bayrağı `v8-evidence.md` Tur 138. Liste öğelerini sayan cümle yok (arandı). Sınıflama: (a) hayır, (b) evet, (c)(d) söylemiyor, (e) evet, (f) hayır | Vegh müsveddesi R3 |
| **Tur 136 — Rohith satırı KAPANDI** (dört okuyucu teyit etti) | Rohith 2026 |
| **Tur 135 — Rohith dolu liste satırı (A; dört okuyucu + Claude; Grok P122 biçimi):** BWB maddesinden sonra *"A buffered series hybrid on a winged tail-sitter has been sized. A 2026 sizing study of 100 kg winged biplane tail-sitters sizes the engine 'to provide cruise power, while a 'boost' battery was sized …'; converting its quadcopter baseline to the tail-sitter adds 'fixed wings and collective pitch change mechanisms for the rotor blades.'"* Kaynak: Rohith ve ark. 2026 *J. Aircraft* s. 575, 586 (`references/Rohith-…pdf`). ChatGPT: başlıkta "biplane" isteğe bağlı, yüzey taramasında denetlenecek | Rohith 2026 |
| **Tur 121 — ses işaretleri (yazar kararı, Tur 119: Grok birini seçer, gerisi çıkar).** Grok V5'i seçti (*"the giving-up is the part that is not free"* kalır). Çıktı: V1 (*"The answer works, costs little…"*), V2 (*"elegant on paper — one propulsion group, no dead hardware in cruise. It is also the more"*; içerik rota paragrafında), V3 (*"excellent at what it does and is"*), V4 (*"and uncrewed ones are ordinary"*; içerik dolu listede ve XFY-1 paragrafında), V6 = **S-46** (*"What that costs … is what the paper is for"* — Adım 5, 8, 9, 15 ile çelişiyordu). Hepsi silme (`v8_draft_check.py --taslak`). **K kalır — yazar kararı (Tur 120).** Özgün Ek S1'in dondurulmuş kopyasında | Tur 120 metni §1, §4; yazar |
| **Tur 118 — Adım 1 uzunluk geçişi, ilk kısım** (Tur 117; dört okuyucu + Claude): C1 (sabit kanatlının pist gereğini açan cümle) ve C2 ("The problem has been attacked for seventy years" alt bölümü, tarihleriyle — Grok P101) Ek S1'e; "Tail-sitting aircraft are seventy years old" son paragrafta kalıyor. Özgün Ek S1'de tam | Tur 117 metni §3 |
| **Tur 114 — NASA çalışmasının tek evi Adım 4** (P88, dış kanıt kimliği kuralı; Tur 113, dört okuyucu + Claude): "A NASA study that sizes five VTOL architecture families to one mission describes …" → "The NASA sizing study used in Section 4 describes …" (ileri işaretçi); iki rota paragrafı Adım 1'in kendi kullanımı olarak kalır (Grok P94: üçüncü tasarım, görev sayısı ya da üç neden buraya girmez) | Tur 113 metni §6 |
| **Tur 98 (dört okuyucu + Claude):** S-29 — 1G "series-hybrid propulsion has been flown in a crewed motor glider and designed for small uncrewed aircraft" (Schoemann 2014 s. 25–26; Merical ve ark. 2014 özeti). Özgün Ek S1'de | `references/Schoemann-2014_…pdf` |
| **Tur 97 (dört okuyucu + Claude):** 1B başlığı "The problem has been attacked for seventy years" (çaba ihtiyacın kanıtı değil) | Tur 96 metni §5 |
| **Tur 96 (dört okuyucu + Claude):** "No field sustains that level of effort against a need that is not real." çıktı (evrensel çıkarım; ihtiyacı 1A söylüyor); "and several are in service" çıktı (insansız hibrit için hizmette kaynağı yok; V-22 insanlı tanık — reddedildi). Özgün 1C paragrafı Ek S1'de | Tur 95 metni §4 |
| **Tur 95 (dört okuyucu + Claude):** 1B sırası — "Tail-sitting prototypes and the first tilt-rotor flew in the 1950s, vectored-thrust and tilt-wing aircraft in the 1960s, and a broad family…" (S-23'ün uygulanmış hâli sırayı bozuyor ve süreklilik ima ediyordu). **1D gerekçesi düzeltildi:** "Precise hovering…" cümlesi yanlış maddeyi saydığı için değil (kaynakta var: XFY-1 "Difficult to hover precisely over a spot"), yineleme olduğu ve daha uygun evi Adım 5E olduğu için çıktı; 1D'ye geri konmadı (dört okuyucu + Claude). **Açık:** "No field sustains…" ve "several are in service" | NASA 19810010574 XFY-1 satırı; 19840014464 "In retrospect" paragrafı |
| **Tur 94 (yeniden kurma; dört okuyucu + Claude):** 1D "Precise hovering … inherited" çıktı (üçüncü "inherited", listeyle uyuşmuyordu); 1E açılışı ("It would be easy, and wrong …") çıktı; S-21 "the last two of them at two scales"; S-22 DelftaCopter'in cyclic+collective hatveli rotoru ve değişken hatvenin bedeli; S-23 "tilt-rotors from the 1950s". 1D reddetme cümlesi korunan (162). Özgün paragraflar Ek S1'de. **Açık:** "No field sustains…" (üçü tut, ChatGPT çıkar); "several are in service" (kaynak ya da yumuşatma — dört farklı öneri) | De Wagter 2018 (değişken hatve: "two extra actuators … added weight from the mechanisms"; "A diameter of 1 m was finally selected as a compromise"); NASA 19810010574 (XV-3 Ağustos 1955, XV-15 Mayıs 1977); Adım 12 "Bill 1 is not tested" |
| **Tur 64 — N3** (beşimiz hemfikir; Qwen'in *"the only one of those documented obstacles"* düzeltmesiyle): iki alt bölüm bire; XFV-1, NASA incelemelerinin değerlendirmeleri ve güçlük listesi, *"the usual account is wrong"* Ek S1'e aynen | Ek S1; Adım 5 *"That disposes of the spatial-orientation objection and nothing else"* |
| **Tur 61:** ret cümlesi katkıdan önceye alındı; paragraf katkıyla bitiyor (dört okuyucu + Claude aynı yönde; Grok ve Qwen neredeyse aynı metni önerdi). Yüklem değişmedi | CLAUDE.md §0.8; `v8-shortening-consensus.md` C2 |
| **Tur 58, P1:** katkı mimaridir — gövde döner, propulsor dönmez; yeniden yönlendiren mekanizma yok; üçlü katkının sunuluş/fiyatlanış biçimi | Adım 7 satır 69 (*"rotating the airframe"*); Adım 7 tablosu; Adım 15; CLAUDE.md §0.6. *"arranged to"*: geçişin tamamlanması iddia edilmiyor (Adım 7, 15) |
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
| Eşeksenli karşıt dönüşlü kuyruk üstü, gerekçe tork dengeleme | Novlit ve ark. 2014, `references/2014_0529_paper.pdf`: *"A pair of 10 inches coaxial contra rotating propellers is mounted to compensate each other's torque"* — **birinci elden** |
| Askı kontrolünün yerleşik cevabı: slipstream içinde elevon ve rudder | Novlit ve ark. 2014, aynı belge: *"Elevon and rudder are immersed in the propeller slip stream to provide three axis control moments in hover"* — **birinci elden** |
| Tepki torku yerleşik bir yatış kanalı; diferansiyel devirle | Zhang ve ark. 2012, `references/ica20120400001_12673514.pdf`, satır 128–130: *"It balances the anti-torque of the rotors by the inverse rotating of the two rotors"* — **birinci elden** |
| Aynı kanal dikey kipte *yaw*, yatay kipte *roll* adını alıyor | Zhang 2012 **Tablo 2**, satır 159–165: Yaw/Vertical = *"Differential velocity of the two motors"*; Roll/Horizontal = aynı — **birinci elden** |
| Eksen adlarının askıda yer değiştirmesi literatürde adlandırılmış | Novlit ve ark. 2014, satır 118–123: *"the definition of the roll and yaw angles are interchanged"* — **birinci elden** |
| Kuadrotor kuyruk üstü yatışı bağımsız rotorların tepki torkundan üretir | **Oosedo ve ark. 2013 s. 319, birinci elden (Tur 140)**: *"the desired torque for Zb axis control"*, Zb itki ekseni, kaynak adı *yaw* (eksen adları yer değiştirir); Zhang 2012 aynı ilkeyi eşeksenli çiftte gösteriyor |
| Üç öğenin hiçbiri yeni değil | `paper/v8/07-the-combination.md` açılışı |

**Bu sayfada BİLEREK olmayanlar:** tek bir başarım sayısı, bu uçağa dair hiçbir tarif, ve
çağdaş hibritlerin **işe yaramadığı** iması. Boşluk bir **başarım** boşluğu olarak değil,
bir **araç** boşluğu olarak konuyor — çünkü makalenin iddiası da o.

**Adım 7 ve Adım 9'un dayanağı artık burada.** Her ikisi de *"yeni olan şey birleşme ve
araçtır"* diyor; bu sayfa o cümlenin karşılığını veriyor ve neyin yeni **olmadığını** açıkça
sayıyor.
