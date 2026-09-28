# Step 15 — Four axes, and where the paper stops

**v8 taslağı, birinci yazım (Tur 57).** İskeletin son satırı: *"Dört eksende dur — yeni hesap yok, atıf
yok."* Grok, Tur 57: *"The last section … should repeat Section 9's four axes and stop. No new number."*
Yazar, Tur 57: *"Adım 9 için dört ekseni tekrarla."*

**Kural denetimi:** hiç sayı yok (3,8×'in tek evi Adım 14 — burada tekrarlanmıyor) · hiç atıf yok · sabit
kanatla menzil yarışı yok (§0) · çok rotorluyla dikey yarış yok (§0) · tilt'e karşı iddia **mekanizma**,
dar hâliyle: yeniden yönlendiren mekanizma sınıfı yok, hareketli parça yok değil; yatış şeritten (§0.1)
· *"mekanik olarak daha basit"* yok · *"inşa gereği"* yok · öteki hibritlere karşı menzil iddiası yok ·
*"the range of a fixed-wing aircraft"* yok (§0.3) · katkı merkezde (oran incelemesi P2).

**Bu sayfa yazılırken bulunan:** Adım 9'un bağımlılık tablosu pist iddiasının *"the battery gap"*e bağlı
olmadığını söylüyordu; Adım 14 dikey evrenin bu depoyla boyutlandığını gösterdi. **Adım 9 düzeltildi.**
Ve **Adım 6 hâlâ *"It is this aircraft's own refusal of the variable-pitch hub"* diyordu** — ChatGPT'nin Tur
53'te Adım 11'de yakaladığı aşırı atıf Adım 6'ya hiç yayılmamıştı; bu sayfanın ilk yazımı onu tekrarladı.
İkisi de düzeltildi, emekli listesine girdi.

---

## Four axes, and where the paper stops

This section states the boundary of the paper's claims.

**It is not a list of the study's open questions.** Those are in Section 14, and the difference matters: the boundary below is about claims the paper **declines to make**, most of which it could not make on any evidence; Section 14 is about questions the paper **does not answer**, and which better evidence would answer. One is a scope; the other is a debt.

### The claims are made on four axes, against four different opponents

Comparison is only meaningful against a named alternative, and this paper's alternatives differ from axis to axis.

| Axis | Opponent | Status |
|---|---|---|
| Cruise efficiency | Rotorcraft: multirotors and helicopters | **Claimed against multirotors, and bounded; against helicopters the comparison with published figures is mixed and no advantage is claimed.** Cruise lift is carried on a surface rather than on rotors, which no sizing contract changes. The *size* of the resulting advantage is a calculation, not a consequence of that fact: positive throughout against one published quadrotor, and from slightly behind to comfortably ahead against the other (Section 6). |
| Operation without a runway | Fixed-wing aircraft | **Claimed as sized, not demonstrated** (Sections 5, 14). The vertical phase was sized with an energy store whose required performance the sources consulted here do not report as built. |
| The mechanism required to change regime | Tilting architectures | **Claimed.** This is the paper's contribution — a count of mechanism classes (Section 7), not a claim of mechanical simplicity or reliability. |
| Cruise efficiency and range | Other hybrids — lift-plus-cruise, tilt | **Not claimed, in either direction.** |

**The fourth row is the important one**, and the reason it is a refusal rather than a result is the paper's own finding in Section 13. Against lift-plus-cruise the ordering depends on the sizing contract: across the three contracts it moves substantially, and under one of them its sign changes inside the envelope and turns on quantities of the competitor that are assumed rather than measured. A paper that quoted one of those orderings as a result would be reporting its own choice of contract. Against the tilting family the competitor can be modelled here only as a bound that pays no cruise penalty, and an ordering against a bound is not a result. **No range claim is made against the tilting or lift-plus-cruise families in either direction**, and a reader who finds one implied anywhere in this paper should treat it as an error rather than as a claim.

### What each claim does not depend on

**Operation without a runway** does not depend on the drag bracket, the propeller efficiency or the transition aerodynamics — **but it does depend on the energy store**: the vertical phase is sized with one, and Section 14 examines whether it exists. **Cruise lift carried on a surface** does not depend on the sizing contract or the transition aerodynamics. The **size** of the cruise-efficiency margin depends on both the drag bracket and the blade family, and Section 6 reports it as a range rather than a number. **Elimination of the propulsor-reorientation mechanism class** does not depend on the drag bracket, the propeller efficiency, the sizing contract, the range result or the energy store — **nor on the transition aerodynamics**.

The mechanism claim is a statement about what hardware is present, and it is settled by the inventory of Sections 7 and 8. **The separate claim that this aircraft can actually perform the regime change is not settled** (Section 7).

### One cost of the contribution that is named and not priced

The mechanism claim has a price this work does not compute. **This configuration declines the reaction-torque channel that comparable aircraft use for roll (Section 8). What that refusal costs — in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia — is not computed anywhere in this paper.** The claim is that the mechanism class is eliminated. **Whether eliminating it is favourable on balance is a question this work does not settle**, and quantifying it would require a control-allocation study rather than a single torque figure.

### Eight things this paper does not claim

**1. It does not claim range against fixed-wing aircraft.**

**2. It does not claim vertical capability against rotorcraft.** That comparison runs the other way.

**3. It does not claim that the aircraft has no moving parts.** What is eliminated is a *class of mechanism* — the one that reorients a propulsor. The aircraft has a moving aerodynamic surface, it is named where the elimination is claimed rather than later, and it also pitches the nose down when deployed.

**4. It does not claim mechanical simplicity.** Part count, assembly mass, failure modes and maintenance burden were not measured, and nothing here supports a statement about reliability. The count of mechanism classes in Section 7 is not a reliability argument.

**5. It does not claim that the escape condition is fully instantiated.** The condition is met in the propulsor that carries the aircraft and is not met in the attitude system, which is carried through cruise producing moments rather than cruise thrust. Section 3 names that case as partial instantiation, and the charge it re-opens is reported rather than absorbed.

**6. It does not claim that satisfying the condition makes an aircraft better.** The condition concerns three specific charges. A configuration may avoid all three and still be unbuildable, uncontrollable, or unsuited to its mission, and the accounting says nothing against that possibility.

**7. It does not claim that the trades inside the escape are favourable.** Moving the hover peak onto a store converts a power-system charge into a cost in kilograms; serving two regimes with one set of fixed-geometry propellers costs efficiency in at least one of them. Both are computed, neither is asserted to be worth paying, and the ledger reports them whichever way they fall.

**8. It does not claim that the aircraft flies.** The design *sizes* vertical operation and the transition; it does not demonstrate either. No aircraft has been built, no wind tunnel has been run on this geometry, and the transition analysis is a calculation whose assumptions are stated where it appears.

### What the claims that remain amount to

Section 14 and Supplement S14 list what the paper leaves open. What the paper offers is **a configuration sized to combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism that reorients a propulsor, and an account of what the combination costs.**

Each half of that has a named opponent and neither half is a record. **Nor is the configuration claimed to be without precedent**: Section 1 sets out what is already established, including uncrewed tail-sitters, tail-sitters without control surfaces, coaxial contra-rotating tail-sitter propulsion, and blended-wing-body tail-sitters. **The contribution is the architecture, and the paper presents it as the combination, the consequences of the choices inside it, and the accounting** — which is what Sections 7 and 8 describe and what Section 11 prices.

The configuration is arranged to change regime by rotating the airframe rather than the propulsors, and so carries none of the mechanism classes Section 7 counts: no pivot, no nacelle or rotor-group actuator, no variable-pitch hub, no dedicated lift rotors, and — while the tip pairs free-wheel or are held by motor torque — no rotor stowing, indexing or stopping mechanism (Section 7's note). **This is a count of mechanism classes, not a claim that nothing moves, and not a claim of mechanical simplicity or reliability.** Whether this aircraft completes the rotation is a separate question, and it is not settled here.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 160 — D evresi: Adım 9 (6.2) bu adıma birleşti** (yazarın önerisi; dört okuyucu + Claude; E11 yazar onayı): 6.2 + 9 → tek Bölüm 9; yalnız taşıma + silme; iki bulgu yan cümlesi tabloya; *"Removing those eight"* silindi; sözleşme cümlesi Adım 10'un başına; "By construction" tanımı Ek S9'a (E11). Eski iki gövde Ek S9'da tam | Tur 159 §2–3 |
| **Tur 150 — R-11 uygulandı** (dört okuyucu + Claude): *"Section 14 lists what would settle the rest."* → *"Section 14 lists what the paper leaves open."* — X-6 silinince *"the rest"* öncülsüz kalmıştı. X-6 kapandı | Tur 149 §3.3 |
| **Tur 149 — X-6 uygulandı** (dört okuyucu + Claude; **yazar onayladı**): *"The loop closes; the aircraft is not shown to."* Adım 15'ten silindi, Adım 14'te kalıyor (`v8_stale.py` YALNIZ). **R-11:** silme sonrası *"Section 14 lists what would settle the rest"*ta *"the rest"* öncülsüz kaldı — uygularken yakaladım; onarım oyda | Tur 148 §3; Tur 149 §3 |
| **Tur 130 — Adım 15 KAPANDI: 343** (dört okuyucu + Claude teyit etti; borç izi teyit edildi) | Tur 130 |
| **Tur 129 — E9 kapandı: sertifikasyon yan cümlesi SİLİNDİ** (beş oy: Grok, ChatGPT, Claude; DeepSeek ve Qwen Tur 128'de oy değiştirdi; yazar: *"hemfikir olursanız ortak fikriniz de isabetli olabilir"*). *"Section 14 lists what would settle the rest; nothing in this work addresses certification."* → *"Section 14 lists what would settle the rest."* `v8_draft_check` temiz (kısalan 1). Özgün paragraf Ek S15'te; ifade emekli. Borç izi (Qwen P2): `drafts/15-maps.md` | E9; Tur 129 |
| **Tur 128 — listeler (dört okuyucu + Claude):** çekirdek dört eksen + kapanış; kalanlar: hepsi (yer taban); saf ses yok. Tüketim haritası metne karşı denetlendi: `paper/v8/drafts/15-maps.md`. Borç/kapsam denetimi (Qwen R108-P2): Adım 15 Adım 14'ün açık bıraktığı hiçbir şeyi kapatmıyor (dördü). (ii) quadrotor ifadesi Adım 6 tablosuyla tutuyor (turboşaft +13…+51 % / +22…+51 %; tam elektrik −4…+27 % zarf, +3…+27 % en iyi aile — Qwen: ifade zarf okumasına ait). **(i) *"nothing in this work addresses certification"* AYRIŞTI** → yazara (E9) | Tur 128 |
| **Tur 102 (Tur 101 oybirliği; R-7):** "and — while the tip pairs free-wheel or are held by motor torque — no rotor stowing, indexing or stopping mechanism (Section 7's note)"; koşulsuz biçim emekli. Özgün paragraf Ek S15'te | Adım 7 notu; S-33 |
| **Tur 98 (dört okuyucu + Claude; E5):** "Cruise efficiency, against rotorcraft — claimed against multirotors, and bounded; mixed against helicopters."; "Nothing is claimed against rotorcraft on vertical capability." | Adım 6D, 9 |
| **Tur 61 — kısa kapanış** (dört okuyucu + Claude hemfikir, A3): 1 023 → ~330 kelime. Kalan her yüklem aşağıdaki satırlarda kaynağıyla; çıkarılanlar kendi evlerinde: çerçeve özeti Adım 2–3, kısmi gerçekleşme Adım 3/7/8, *"by construction"* Adım 9, bağımsız üretilmiş rakamlar Adım 6 | `paper/v8-shortening-consensus.md` A3, A4 |
| **Tur 60:** *"rather than cruise thrust"* | Grok |
| **Tur 59:** *"The configuration is arranged to change regime by rotating the airframe"* — Grok Adım 14'ü yakaladı; aynı fiil burada da vardı | Adım 1 (P1) |
| Dört eksen, dört rakip, sıralama | Adım 9 tablosu |
| Seyir kaldırması yüzeyde | Adım 6 (*"a surface that carries the cruise lift"*), Adım 7 (*"carries the cruise lift on a surface"*). **Tur 128 düzeltmesi:** bu satır hâlâ S-49'la (Tur 123) emekliye ayrılan *"no sizing contract … moves a vehicle between those two states"* cümlesini ev gösteriyordu — kayıt yayılmamıştı (§3.1), gövde etkilenmedi |
| Üstünlük hesap; iki yayımlanmış quadrotor; turboşafta karşı pozitif, tam elektriğe karşı *"slightly behind to comfortably ahead"* | Adım 6, *"What the margin actually is"* |
| Sıkıştıran şey sabit hatveli paletin seyir verimi | Adım 6 (**Tur 57'de düzeltildi**: *"own refusal of the variable-pitch hub"* ChatGPT'nin Tur 53'te Adım 11'de yakaladığı aşırı atıftı ve Adım 6'ya yayılmamıştı) |
| Karşılaştırma kontrollü yeniden üretim değil | Adım 6, beşinci nitelendirme |
| Kuyruğunun üstünde duruyor; saha yalnız zemin veriyor; duruş yapısı = kontrol pervanelerinin yapısı | Adım 5 |
| Dikey evre bu depoyla boyutlandı; ölçülmüş depoda yalnız daha ağır, sürekli anmada kapanmıyor | Adım 14 (ikinci yazım) |
| *"By construction … by the sizing, never by demonstration"* | Adım 9, madde 8 |
| Gövde döner, propulsor dönmez; beş mekanizma sınıfı | Adım 7 tablosu ve metni |
| Yunuslama/sapma diferansiyel itkiden; yatış şeritten; tepki torku kanalı reddedildi, bedeli hesaplanmadı | Adım 7, Adım 8, Adım 9; CLAUDE.md §0.1 |
| Eyleyici envanteri: motorlar ve şerit | Adım 7 (*"the propulsion motors together with the strip"*) |
| Sayım, basitlik/güvenilirlik değil | Adım 7, Adım 9 madde 3–4 |
| Mekanizma iddiası sürükleme, η_p, sözleşme, depo, geçiş aerodinamiğine bağlı değil | Adım 9 bağımlılık tablosu; Adım 14 *"It does not reach the mechanism claim"* |
| Geçişin tamamlanması iddia edilmiyor | Adım 7 son paragrafı; Adım 10 |
| Kısmi gerçekleşme: burun çifti sağlıyor, uç çiftleri değil | Adım 7, Adım 8, Adım 9 madde 5 |
| Lift+cruise sıralaması sözleşmeye bağlı; bir sözleşmede işaret değişiyor ve ölçülmemiş bir kesre bağlı; tilt bir sınır | Adım 13 |
| Üç para birimi, bağlaşık; her çare aktarır | Adım 2 (Tur 56 başlığı) |
| En az ikisi kilitli değil → sıralama bir ağırlıklandırma | Adım 12, Adım 13 |
| Döngü kapanıyor, uçak gösterilmedi; ilk engel depo; ötekiler | Adım 10, Adım 14 |
| Son cümle | Adım 9 *"What the claims that remain amount to"*; CLAUDE.md §0.3 |

**Bu sayfada BİLEREK olmayanlar:** hiçbir sayı; hiçbir atıf; ağır tasarım; öteki hibritlere karşı menzil
sıralaması; *"validation"*; *"no moving parts"*; *"simpler"*.
