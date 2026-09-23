# Step 13 — Rankings belong to contracts

**v8 taslağı, ikinci yazım (Tur 56).** Dört okuyucunun Tur 55 yanıtları işlendi: Fatura 3'ü ortak
tutmanın bir soru seçimi olduğu ve yönü (Grok, ChatGPT, DeepSeek — yön **hesaplandı**, (d) durumu:
aleyhimize); rakiplerin *"bu planform artı iki ek"* olduğu (Grok); 93–141'in her geçtiği cümlede
*"bound"* (Grok); *"carry the audit"* rakip sütunları için karşılanmıyor (Grok) ve temel/asimetri
beyanı ona katlandı (DeepSeek'in dördüncü yükümlülüğü); tüm sözleşmelerde kararlı sıralama
bildirilebilir (DeepSeek); işaret bir parametre sonucudur, en çok ölçülmeye değer olan odur (Qwen).
**DeepSeek'in "kayma asimetriye dayanıklı" iddiası denetlendi: pervane ve sürükleme tabanına dayanıklı
(65–77 puan), kaldırma grubuna değil (14–134 puan).** "Some seventy points" sonuç cümlesinden çıktı.
DeepSeek'in *"L/D'ler farklı tabanda"* itirazı reddedildi: ikisi de aynı temiz gövde üzerinde
aerodinamik oran; yalnız uçlar adlandırıldı.

**Birinci yazım (Tur 55).** İskeletin 13. adımı: *"Sıralamalar sözleşmeye aittir — ve
çerçevenin kullanıcısından ne istediği: denetimi taşı, sözleşmeni adlandır, çıplak sıralama verme."*
(Qwen'in Tur 34'te bulduğu ve buraya katlanan madde.)

**Bu sayfa yeni bir hesaba dayanıyor:** `aero/contracts.py` → `aero/contracts-result.txt`. Adım 10'un
dört kapanışının her birinde üç mimari üç sözleşme altında boyutlandırıldı. A'nın sütunu Adım 10'u
**birebir** yeniden üretiyor (betik üretmezse durur).

**Hesap v7'nin tablosundan belirgin biçimde farklı çıktı, ve fark tek yönlü değil:**

- Hesaplanmış η_p tabanında (A 0,632/0,683; B ve C 0,80 varsayım) **lift+cruise sözleşme 1 ve 2'de
  her kapanışta önde.** Sözleşme 3'te işaret **zarfın içinde değişiyor**: üst palet ailesinde A önde
  (−13,0 / −6,5), alt palet ailesinde B önde (+1,1 / +7,3).
- **Tersine dönme dört kapanışın ikisinde oluyor**, dördünde değil. Adım 2'nin öngörüsü (*"will
  reverse"*) bu yüzden **yön olarak her yerde tutuyor, güçlü biçimiyle kısmen.** Adım 2'nin cümlesi
  *"will move … and can reverse"* biçimine getirildi — **bu, öngörünün sınanmadan sonra
  daraltılmasıdır ve öyle bildiriliyor**; okuyuculara özellikle soruluyor.
- **İşaret, rakibin ölçülmemiş bir parametresine bağlı:** B'nin kaldırma grubu %5 ise A hiçbir yerde
  önde değil; %15 ise sözleşme 3'te her kapanışta önde.
- **İdealleştirilmiş tilt her sözleşmede, her kapanışta önde** (+93 … +141 %). Sınır, sıralama değil.
- **Kütle üstünlüğü artık %27–30** (v7: %32–36). Neden: A'nın hesaplanmış η_p'si A'nın motorunu
  büyütüyor, B ise 0,80'de kalıyor.

**Kural denetimi:** öteki hibritlere karşı menzil iddiası YOK (§0) · tilt'e karşı iddia mekanizmadır,
bu sayfa ona dokunmuyor · yalnız hafif ölçek, ağır menzil yok (Grok) · *"kütle faturası devrilen
şeydir"* denmiyor (Grok): sözleşme kütle farkını seyir verimi farkına karşı tartıyor, bu kadar ·
baskın mimari ağırlıksız sıralanır (ChatGPT) — tilt satırı buna yakın ama tam o değil: takas var
(tilt %0,5–5,4 ağır), yalnız çok dengesiz. İlk yazımda *"hiçbir sayımda geride değil"* yazmıştım;
§0.2 denetiminde yanlış çıktı, düzeltildi.

---

## Rankings belong to contracts

Section 12 showed that at least two of the three charges are not locked together, and drew the
consequence: where one architecture pays less of one charge and more of another, a ranking depends
on how the charges are weighed. **A sizing contract is one such weighing.** It fixes what is held
equal between the architectures being compared, and what is held equal decides how a difference in
mass is set against a difference in cruise efficiency. This section applies three contracts to three
architectures at each of the four closures of Section 10.

### Three contracts, and what each holds equal

Range in the sizing loop is

> R = (E* η / g) · (L/D) · (m_fuel / m_TO),

where E* is the fuel's specific energy and η the energy chain, propeller included. The three
contracts differ only in the last factor.

- **Fixed fuel fraction.** Every architecture carries sixteen percent of its own take-off mass as
  fuel. **Take-off mass cancels from range**, which is then set by L/D and the chain alone. A
  heavier architecture shows its mass in the take-off-mass column and nowhere in the range column.
- **Fixed fuel mass.** Every architecture carries the fuel this configuration carries at the same
  closure — 8.4 to 9.2 kg. **Range is divided by take-off mass**, so a heavier aircraft flies the
  same fuel less far.
- **Fixed take-off mass and payload.** Every architecture is held to this configuration's closed
  mass and its 13 kg payload. **Fuel is what remains after the empty mass**, so every kilogram of
  architecture-specific hardware is a kilogram of fuel not carried.

**These are three different questions, not three estimates of one answer.** The first asks which
aircraft converts a fuel fraction into distance more efficiently; the second, which flies further on
a given tank; the third, which flies further at a given gross weight. A mission decides which of
them it is asking. This paper has no mission that would decide, and does not choose.

### What is compared, and on what basis

**Three architectures fly the same mission**: 13 kg of payload at 30 m s⁻¹, with the same wing
loading, disc loading and aspect ratio, the same airframe and avionics fractions, and the same fuel
and energy chain apart from the propeller. **The competitors are therefore this planform with two
add-ons**, not independently designed aircraft of their families. **All three carry the same buffered
series-hybrid power system** — a buffer of 3.6 percent of take-off mass and an engine sized by cruise —
so Bill 3 is held common, and what the comparison measures is mass and cruise drag. This configuration
is the first architecture; the others are a lift-plus-cruise layout and a tilting one.

**Holding Bill 3 common is a choice of question, and it has a direction.** It is made so that the
contract can be seen acting on a mass difference against a cruise-efficiency difference; it is not a
claim that those families would use this power system, and the tilting family as Section 2 describes
it has no store at all. **The choice runs against this configuration.** Given no buffer and an engine
sized by hover instead, the lift-plus-cruise layout closes at 381 kg, falls 11 to 23 percent behind
under a fixed fuel mass, and does not close at all under a fixed take-off mass; the tilt bound falls
75 to 98 percent behind under a fixed take-off mass, or does not close. **Under a fixed fuel fraction
the lift-plus-cruise lead is unchanged, at 55 to 84 percent, although the aircraft is now seven times
heavier** — the first contract's blindness to mass, made visible. **That comparison is not
used**, because it would set competitors without a store against this configuration with one — a
buffer of 3.6 percent whose feasibility is the item Section 14 examines. Until that item is settled,
the common store is the neutral choice.

**The basis is not symmetric, and each asymmetry is stated with its direction.**

- **Drag.** All three share the clean airframe at each end of the drag bracket. This configuration
  carries its exposed frames and free-wheeling rotors, as in Sections 10 and 11. The lift-plus-cruise
  layout carries the ratio measured in the wind-tunnel campaign quoted in Section 2 — maximum
  lift-to-drag ratio about 17 clean and about 13 with the lift hardware installed and its propellers
  locked parallel to the flow — **transferred from a different airframe**, and assuming lift rotors
  stopped and aligned in cruise, which takes an indexing mechanism (Section 7) whose mass is not
  separately charged. **The tilting layout carries no cruise drag penalty at all.** That is an
  idealisation in its favour, and it is deliberate: it makes the tilt row a bound.
- **Propeller efficiency.** This configuration uses the computed 0.632 and 0.683 of Section 10. The
  other two use 0.80 — the lift-plus-cruise layout because its cruise propeller does nothing else,
  the tilting layout because it has a variable-pitch hub. **Both are assumed, not computed**, and the
  asymmetry runs against this configuration; it is tested below.
- **Mass.** The lift-plus-cruise layout carries a lift group of 10 percent of take-off mass and the
  tilting layout a tilt mechanism of 5 percent. **Neither figure is measured.** The first turns out to
  decide the sign of one result, and it is varied below.

### Against lift-plus-cruise: a trade, and the contract sets the exchange rate

**The two architectures trade one charge against another.** Closed under a fixed fuel fraction, the
lift-plus-cruise layout is **38 to 43 percent heavier** — its lift group, amplified by the mass loop,
partly offset by this configuration's larger engine — so this configuration is **27 to 30 percent
lighter**. In return the lift-plus-cruise layout cruises at a lift-to-drag ratio of 11.66 at the
adverse end of the drag bracket and 15.72 at the favourable end, against 8.79 and 10.82 — both
aerodynamic ratios on the same clean airframe — with a propeller at 0.80 against 0.632 to 0.683.

Range of the lift-plus-cruise layout relative to this configuration:

| Closure (Section 10) | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass |
|---|---:|---:|---:|
| Adverse drag, lower blade family | +67.8 % | +40.2 % | +1.1 % |
| Adverse drag, upper blade family | +55.3 % | +27.5 % | **−13.0 %** |
| Favourable drag, lower blade family | +83.9 % | +53.5 % | +7.3 % |
| Favourable drag, upper blade family | +70.2 % | +40.1 % | **−6.5 %** |

**Under a fixed fuel fraction the mass difference does not reach the range column**, and the
lift-plus-cruise layout flies 55 to 84 percent further. Under a fixed fuel mass the difference enters
as a divisor, and its lead falls to 28 to 54 percent. Under a fixed take-off mass it enters as fuel not
carried, and **the lift-plus-cruise layout lands between 13 percent short of this configuration's
range and 7 percent beyond it.** Moving from the
first contract to the third shifts the comparison by **67 to 77 percentage points at every closure**
at the declared lift-group fraction, and always toward the lighter aircraft.

**The sign itself changes inside the envelope under the third contract.** This configuration is
ahead at the two closures with the higher-efficiency blade family and behind at the two with the lower.
**A statement of which architecture has the longer range, made without its contract, would therefore
be a statement about the contract.**

### Against the tilting layout: a bound, not a ranking

**The tilting layout, modelled as a bound, leads under every contract at every closure — by 93 to 141
percent.** Moving from the first contract to the third shifts the comparison by 1 to 18 points toward
this configuration, and nowhere near a reversal.

**There is a trade, but it is lopsided.** The tilting layout closes 0.5 to 5.4 percent heavier than
this configuration, and it cruises at the clean airframe's lift-to-drag ratio with a propeller at 0.80:
it is credited with no nacelle drag, no pivot fairing, and no penalty for flying hover-sized rotors as
cruise propellers. **Even the contract that weights mass most** — a fixed take-off mass, in which every
kilogram of tilt mechanism is a kilogram of fuel not carried — **leaves the bound 93 to 130 percent
ahead.**
The contract moves the comparison, as Section 12 says it must where there is a trade; none of the
three moves it far enough to matter. A ranking against a competitor modelled as a bound is not a
ranking, and **no range claim is made against the tilting family in either direction.**
The claim this paper makes against that family is about mechanism (Sections 7 and 8), and nothing in
this section bears on it.

### Section 2's prediction, tested

**Section 2 predicted that where an arrangement pays one charge heavily in order to escape another,
its ranking against a differently-balanced arrangement will move when the sizing rule changes, and
can reverse.** Both parts can now be checked.

- **The movement holds everywhere**, against both competitors, in the predicted direction: toward the
  lighter arrangement as the contract weights mass more.
- **The reversal holds at two of the four closures against lift-plus-cruise, and at none against the
  tilt bound.**

**Where the reversal falls is decided by quantities this study has not measured or not fixed.** In
the case above it is the blade family, which Section 10 leaves open. Across the sensitivity cases below
it is the competitor's lift-group mass and the propeller basis:

| Case | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass | Shift, first to third |
|---|---:|---:|---:|---:|
| As above | +55 to +84 % | +28 to +54 % | −13 to +7 % | 67 to 77 points |
| Lift group 5 % of take-off mass | +55 to +84 % | +47 to +76 % | +36 to +65 % | 14 to 24 points |
| Lift group 15 % of take-off mass | +55 to +84 % | +8 to +31 % | −62 to −50 % | 117 to 134 points |
| All three at this configuration's propeller efficiency | +33 to +45 % | +6 to +17 % | −33 to −25 % | 65 to 72 points |
| Lift-plus-cruise drag as a fixed increment, not a ratio | +59 to +75 % | +31 to +45 % | −13 to +5 % | 67 to 75 points |

*(Range of the lift-plus-cruise layout relative to this configuration, across the four closures.)*

**With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every
closure; with a heavier one this configuration leads under a fixed take-off mass at every closure.**
Giving all three the same propeller efficiency also produces a reversal at every closure. **Which
architecture ranks first under a fixed take-off mass is therefore decided, in this model, by a mass
fraction of the competitor that this study has not measured** — and the fixed-fuel-fraction column,
where mass does not enter, does not move with it at all. **Put plainly, the sign under a fixed take-off
mass is not a result about the architectures; it is a result about that parameter**, and it is the
one most worth measuring.

**The size of the shift behaves the same way.** It barely moves when the propeller or drag basis is
changed — 65 to 77 points across those cases — because those asymmetries enter all three contracts
alike. It moves a great deal with the lift group, from 14 to 134 points, because the shift *is* the
mass difference being counted. **What is robust is that the shift exists and runs toward the lighter
aircraft; its size is the size of the mass difference.**

### What the framework asks of whoever uses it

A framework that says every remedy transfers a charge rather than removing it takes something from
its user in return. **It asks for three things, and this paper holds itself to them.**

**Carry the audit, for every column.** State each charge in its own currency — kilograms, drag
counts, installed kilowatts — before any aggregate, and state the basis of the comparison with its
asymmetries and their directions. An aggregate that arrives without its parts cannot be checked, and
the parts are where the comparison is decided. **This paper meets that for its own column** (Section
11) **and not for the competitors'**, whose kilograms and drag counts here are parameters and transferred
ratios rather than an audit — which is one more reason no ranking against them is offered.

**Name the contract.** A comparison of architectures is a comparison under a contract. The contract is
chosen by the mission rather than by the analyst, and a comparison that does not state one has chosen
one silently.

**Refuse the bare ranking.** Report an ordering only with the contract it was computed under, and,
where its sign depends on an unmeasured quantity, with that quantity named. An ordering that holds
under every contract examined may be reported as such — that is a stronger statement than any one
contract gives, and it still names the contracts. Applied to this paper's
own numbers, the rule is the fourth row of Section 9: **no range claim is made against lift-plus-cruise
or tilting layouts**, because the ordering against the first depends on the contract and on the
competitor's lift-group mass, and the ordering against the second is against a bound.

### What this section does not establish

**The competitors are modelled at a coarser level than this configuration.** Their drag is a ratio
transferred from another airframe or an idealisation; their propeller efficiency is assumed; their
architecture-specific mass is a parameter. This configuration's drag and propeller efficiency are
computed. **Comparing computed figures against assumed ones favours whichever is assumed more
optimistically**. In propeller efficiency that is both competitors, and the table above shows the
size of it; in drag it is the tilting layout, by construction.

**The comparison is at one size.** Section 12's heavy design has no closure, and none of its figures
is used here.

**And nothing here ranks architectures for a mission.** Which contract a mission implies, and which
architecture it then favours, is the user's question. What this section establishes is narrower: **the
same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by
tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property
of the architectures alone.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| Menzil R = (E* η/g)(L/D)(m_yakıt/MTOW); üç sözleşmenin tanımı | `aero/baseline.py` satır 216–230 (yorum bloğu), `menzil_ver`, `sabit_yakit`, `sabit_MTOW` |
| A'nın sütunu Adım 10'u birebir üretiyor (57,51 / 55,85 / 53,51 / 52,34 kg) | `aero/contracts-result.txt`, SINAMA bloğu |
| Sabit yakıt kütlesi 8,4–9,2 kg (A'nın kapanışlarındaki %16) | aynı, AYRINTI: 9,20 / 8,94 / 8,56 / 8,37 kg |
| Görev 13 kg, 30 m/s; kanat/disk yüklemesi, gövde 0,300, aviyonik 0,080 ortak | `baseline.py` GOREV, ORTAK |
| Tampon %3,6 hepsinde, motor seyre boyutlu hepsinde (Fatura 3 ortak) | `contracts.py` `kos()`: `mimariler(f_tampon=0.036)`, `tamponlu_hepsi=True` varsayılanı |
| B'nin 13/17'si: Bacchini tezi, azami L/D ≈17 temiz, ≈13 pervaneler akışa paralel kilitli | `paper/bacchini-reading-record.md` §3.3; Adım 2 satır 79–81 alıntı |
| B'nin hizalı rotorları indeksleme mekanizması ister; kütlesi ayrı faturalanmıyor | Adım 7 tablosu (*"Rotor stowing, indexing or stopping mechanism"*); `bacchini-reading-record.md` §4 |
| C'nin L/D çarpanı 1,00 — idealleştirilmiş | `baseline.py` satır 146–147 ve `mimariler` docstring |
| A η_p 0,632/0,683 hesaplanmış; B ve C 0,80 varsayım; gerekçeleri | `aero/chain_resolve.py` docstring; `closure.py` |
| B ek grup %10, C eğme %5 — ölçülmedi | `baseline.py` `mimariler` docstring |
| B, sözleşme 1'de %38–43 ağır; A %27–30 hafif | `contracts-result.txt`: mB/mA 1,378–1,433; SALINIM bloğu 27,4–30,2 |
| Boş kütle kesri: B 0,664–0,678, A 0,592–0,614; A'nın itki kesri daha yüksek (0,176–0,198 vs 0,148–0,162) | aynı, KÜTLE BİLEŞENLERİ |
| L/D: B 11,66 / 15,72; A 8,79 / 10,82; C 15,24 / 20,55 | aynı, AYRINTI |
| Taban tablo (+67,8 … −6,5) | aynı, TABAN |
| Salınım 67–77 puan (66,8 / 68,3 / 76,6 / 76,7) | aynı, SALINIM |
| Tilt +93,3 … +140,5 %; sözleşme 3'te +93,3 … +129,5 %; salınım 1,4–17,8 puan; tilt %0,5–5,4 ağır (mC/mA 1,005–1,054) | aynı, TABAN ve SALINIM |
| Duyarlılık tablosu (beş satır) | aynı, (a), (b) %5, (b) %15, (c) |
| Adım 2'nin öngörüsü | Adım 2 satır 186–189 (**bu turda daraltıldı**, aşağıda) |
| Adım 9'un dördüncü satırı | Adım 9 satır 28–43 (**bu turda güncellendi**) |
| Rakipler tamponsuz: B 380,9 kg; s2 −23,2…−11,4; s3 kapanmıyor; tilt s3 −98,2…−75,2 ya da kapanmıyor; s1 değişmez; B/A kütle 6,6–7,3 | `contracts-result.txt`, (d) bloğu |
| Kayma: taban 66,8–76,7; %5 → 14,3–23,5; %15 → 116,8–134,1; aynı η 64,6–71,7; artış 67,0–75,2 | aynı, `kayma` sütunu |
| Adım 2'nin tilt'i depolamasız (*"Bill 3 is left standing … with no store"*) | Adım 2 tablosu |

**Bu sayfada BİLEREK olmayanlar:**

- **Ağır tasarım.** Kapanışı yok (Adım 12). Grok: *"13 on one scale is a result."*
- **Hiçbir menzil iddiası öteki hibritlere karşı**, hiçbir yönde (§0).
- **"Kütle faturası devrilen şeydir."** Grok'un uyarısı: sözleşmeler kütle farkını verim farkına karşı
  tartıyor; A'nın kütle tarafında tampon ve daha büyük motor da var, B'ninkinde kaldırma grubu. Tek
  faturaya indirilmiyor.
- **Misyon → sözleşme eşlemesi.** Hangi misyonun hangi sözleşmeyi ima ettiği söylenmiyor; yazar değil
  kullanıcı karar verir.
- **v7'nin sayıları** (+24…+45 %, %32–36). Gövdede yok (§4). Neden değiştiği yalnız burada ve bulgu
  kaydında: A'nın hesaplanmış η_p'si A'nın motorunu ve kütlesini büyütüyor, B ve C 0,80'de kalıyor;
  olumsuz uçta ×1,1 pay.
