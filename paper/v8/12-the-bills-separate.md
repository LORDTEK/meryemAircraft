# Step 12 — The charges separate with scale, and one of them cannot be tested

**v8 taslağı, birinci yazım.** İskeletin 12. adımı: *"Üç para biriminin gerçekten üç
olduğunun, tek niceliğin üç adı olmadığının kanıtı."*

**Bu sayfa iskeletin vaadini DARALTIYOR, ve nedeni denetimde çıktı.** Tampon (Fatura 1'in
bu yapılandırmadaki biçimi) **her iki ölçekte de girdi** — %3,6 ve %4,0, ikisi de seçilmiş,
hiçbiri askı enerjisinden türetilmemiş (`aero/mass.py` `m_pil` parametresi; `baseline.py`
`f_tampon`). v7'nin *"kütle faturası yükselir"* cümlesi iki girdi seçimini bir sonuç gibi
okuyordu. **Yani üç faturadan yalnız ikisi ölçekte sınanabiliyor.**

**Kural denetimi:** Adım 11'in eksenden farklı olduğu söyleniyor (DeepSeek) · *"Fatura 2
ölçekle küçülür"* **burada** söyleniyor, 11'de önizlenmemişti (Grok) · hiçbir ağır tasarım
MENZİLİ verilmiyor (elimizdeki her ağır menzil kısmi) · **3,8× GEÇMİYOR** — tamponu askı
enerjisinden türetmek tam o sorunun içine giriyor, ve bu sayfa oraya gitmiyor · üç haneli
öngörü–hesap uyumu **iddia edilmiyor** (aşağıda neden).

---

## The charges separate with scale, and one of them cannot be tested

Section 11 decomposed the three charges on one aircraft, at one size. **This section asks a
different question: are they three quantities, or one quantity under three names?** The test is
to change the size of the aircraft and see whether they move together. If they did, the framework
of Section 2 would be a single cost described three ways, and a ledger in three currencies would be
a ledger in one.

**This is a different axis from the one Section 11 examined.** There, Bill 2's share of the
zero-lift drag was compared at the two ends of the drag bracket, at a fixed size. Here the size
changes. The two answers are about different variables and do not bear on each other.

### What is compared, and why it is these two points

**The comparison is between the two published reference designs, 50 kg and 1 000 kg, sized by
one method.** It is not between the four closures of Section 10, which vary the drag uncertainty
and the blade family at a single size and are not a scale study.

**The pair can be used even though Section 10 superseded some of what was published, because the
quantities this section needs are not among the superseded ones.** The free-wheeling rotor term
is the same value Section 10 carries at both ends of its bracket. Disc loading is a sizing rule
Section 10 holds. The buffer fraction is an input to Section 10's loop. **The quantities Section 10
replaced — the total zero-lift drag, the propeller efficiency, the range and the closed mass — are
not used here**, and no heavy-design range is quoted for that reason: every figure available for
it is partial in one respect or another.

**Two conditions travel with the heavy design and are stated here rather than later.** It has no
drag bracket; it stands on a single zero-lift coefficient with no equivalent bound. And **its
structural closure is undetermined**: shell mass scales with wetted area while take-off mass scales
with volume, so the structural fraction depends on how areal density grows with size, and that
exponent has not been measured. **The comparison below uses powers, loadings and drag terms; it
does not use the structure**, which is why it can be made at all.

### Bill 3 — held nearly flat, and held there by a sizing rule

**Disc loading is held constant**: 44.2 kg m⁻² at 50 kg and 43.7 at 1 000 kg. Specific hover power
depends only on disc loading, so fixing it fixes hover power per unit weight — **0.218 kW kg⁻¹ at
the light design and 0.216 at the heavy**, a ratio of 0.99. Hover power rises from 10.9 kW to
216.2 kW, a factor of 19.8 against a mass factor of 20. **Hover power grows linearly with mass
rather than as the L^3.5 of the classical result.**

The engine, sized by cruise, moves slightly more, because the heavy design cruises faster at a
better lift-to-drag ratio. **The ratio of hover power to engine rating is 4.19 at the light design
and 3.98 at the heavy — a change of 5 percent.**

**That near-constancy is a consequence of a design rule, not a finding about Bill 3**, and it has
to be read that way. What it does establish is narrower and still useful: Bill 3 *can* be held
nearly flat across a factor of twenty in mass by a single sizing choice.

**The rule has a price, and it is paid in geometry.** Holding disc loading constant makes disc area
grow as L³ rather than L², so the nose propeller grows faster than the airframe. Wing loading rises
from 25.3 to 45.0 kg m⁻², span grows by a factor of 3.35 and the main propeller by 4.50, and **the
ratio of propeller diameter to span rises from 0.35 to 0.47.** The heavy design is not the light
design photographed from further away. **Much above 1 000 kg a single nose pair can no longer hold
the disc loading**, and a second would have to be added — which the architecture permits, since
every pair is torque-balanced on its own.

### Bill 2 — falls to between a quarter and a half, and this is the computed result

**The free-wheeling rotor term falls from 0.0154 at 50 kg to 0.0051 at 1 000 kg.** The heavy value
is not pinned: across the blade designs that meet the heavy design's hover requirement it runs from
0.0035 to 0.0074, and 0.0051 is the interior value the sizing was run at. **At every point in that
interval the heavy charge is between a quarter and a half of the light one** — 0.23 at one end,
0.48 at the other.

**The mechanism is not the obvious one.** The obvious explanation is that the wing outgrows the
discs. It does not: the eight tip discs total 0.251 m² against 1.98 m² of wing at 50 kg, and
2.82 m² against 22.24 m² at 1 000 kg — **a disc-to-wing area ratio of 0.127 at both sizes.** What
the charge follows is

> ΔC_D0 ∝ σ R² / (q S)

in which R²/S is the constant just quoted, so **only two terms move**: the blade solidity σ falls,
because the larger rotor meets its thrust with proportionally less blade, and the cruise dynamic
pressure q rises, because the heavy design cruises at 40 m s⁻¹ rather than 30. **The charge falls
because the blade thins and the reference dynamic pressure rises, not because the wing outgrows
the disc.**

**How closely the two terms predict the computed ratio is not claimed here.** The two terms give a
ratio of about three; the computed ratio at the interior value is also about three; but the
computed ratio moves from 2.1 to 4.4 across the heavy interval, so any closer agreement would be an
agreement at a point that no criterion selects. **What holds everywhere in the interval is the
mechanism, the direction, and the order of magnitude.**

**This result does not touch the structural question at all.** It comes from blade-element
solutions on two sized rotors and from the two cruise speeds; it would remain a result even if
the heavy airframe were shown not to close. **And it means the light design is the harder case for
Bill 2**, which is the opposite of the usual expectation for a tail-sitter.

### Bill 1 — cannot be tested with what this work contains

**On this configuration Bill 1 appears as the energy buffer**, as Section 11 set out, since there is
no dedicated lift group to charge. The buffer is 3.6 percent of take-off mass at 50 kg and 4.0
percent at 1 000 kg.

**Both of those figures are inputs.** Neither is derived from the hover energy the aircraft needs;
each was chosen for its design point and carried into the sizing. **A change from 3.6 to 4.0 percent
is therefore a change between two choices, not a scaling result**, and it cannot be offered as
evidence that Bill 1 moves with size in either direction.

**Nor is the structural mass a substitute.** The shell-mass exponent governs how the airframe
fraction scales, and it is unmeasured; but the airframe is not Bill 1 as Section 2 defines it — it
is the structure every architecture carries — and treating it as the mass bill would change the
definition to fit the test.

**Deriving the buffer from the hover energy is possible in principle and is not attempted here.**
Doing it properly means asking what specific power a store of that mass must deliver, and that is
the item Section 14 examines and does not resolve. This section stops short of it deliberately.

### What the comparison establishes

**Separability is shown between two of the three charges, and not the third.** Bill 2 falls to
between a quarter and a half of its light-design value while Bill 3 is held within 5 percent by a
single sizing rule. **Two quantities that respond that differently to the same change of size are
not one quantity under two names.** That is the finding, and it holds wherever in the heavy
interval the rotor term falls.

**Bill 1 is untested at scale**, for the reason given above, and nothing here should be read as
showing it separates from the other two — or as showing that it does not.

**And the evidence is one pair of design points, computed by one method.** It is consistent with
the separability Section 2 asserts; it is not a verification of separability as a general property,
which a single instantiation cannot supply.

### Two costs that scale does not relieve

Neither is one of the three charges, and both are reported because a section about what scale does
to this aircraft would be incomplete without them.

**The fixed-pitch gap does not close with size; it widens slightly.** Against the 0.80 the
published chain assumed, the computed cruise propeller efficiency is 14.6 to 21.0 percent lower at
the light design and **16.4 to 23.0 percent lower at the heavy one.** Refusing the variable-pitch
hub costs as much or more at the larger size.

**The transition is where the square–cube relation is paid in full.** The moment needed to rotate
the aircraft follows M = Iα with I ∝ mL², so the moment required for a fixed rotation time grows
much faster than the aircraft. **Rotating the heavy design in the light design's two seconds would
demand 221.5 kW from the tip propellers — 102 percent of hover power**, which is not available. At
5.1 seconds the demand falls to 13.4 kW, 6 percent of hover power, and that is the heavy design's
rotation time. **A larger aircraft of this type turns more slowly, and must.** Hover power escapes
the classical scaling objection by fixing disc loading; the rotation does not escape it.

### Why this section sits between the ledger and the contracts

**The argument of the next section depends on this one.** If the three charges were one quantity,
a single number could rank architectures regardless of how the charges were weighed. **Because at
least two of them move independently, any ranking must say how they were weighed** — and a sizing
contract is exactly such a weighing. Section 13 shows what happens to the ranking when the contract
changes, and it can do so only because this section has shown that there is more than one thing
being weighed.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| Disk yüklemesi 44,2 / 43,7 kg/m² | v7 §3.9 satır 1768; §3.8 Tablo 13 |
| Askı gücü 10,9 → 216,2 kW, ×19,8 vs kütle ×20 | v7 §3.9 satır 1769–1771 |
| Özgül askı gücü 0,218 / 0,216 kW/kg, oran 0,99 | hesaplandı: 10,9/50,1 ve 216,2/1000 |
| Askı/motor oranı 4,19 / 3,98, değişim %5 | hesaplandı: 10,9/2,6 ve 216,2/54,3 (motor: §2.9 ve §3.8 Tablo 13) |
| Kanat yüklemesi 25,3 → 45,0; açıklık ×3,35, pervane ×4,50; pervane/açıklık 0,35 → 0,47 | v7 §3.9 satır 1824–1827 |
| 1000 kg'ın üstünde ikinci çift gerekir | v7 §3.9 satır 1830–1831 (doğrulandı: 1831) |
| Rotor terimi 0,0154 → 0,0051; aralık 0,0035–0,0074; 0,23–0,48 | v7 §3.8 Tablo 14 ve satır 1728–1734 |
| Disk/kanat alanı 0,127 iki ölçekte de; 0,251 m² / 1,98 m² ve 2,82 m² / 22,24 m² | v7 §3.9 satır 1783–1785 |
| ΔC_D0 ∝ σR²/(qS) | v7 §3.9 satır 1785 |
| **Üç haneli öngörü–hesap uyumu İDDİA EDİLMİYOR** — v7 *"1,73 × 1,78 = 3,08"* diyor ama alıntılanan çözücüler 0,075/0,044 = **1,70** veriyor, çarpım **3,03**; ve 0,075 / 0,044 **hiçbir betik çıktısında yok**, yalnız v7 düzyazısında. Hesaplanan oran aralık boyunca 2,08–4,40 | v7 §3.9 satır 1791–1795; `grep` ile arandı |
| Ağır tasarımın sürükleme braketi yok | v7 §3.8 satır 1750–1754 |
| Ağır yapısal kapanış belirlenmemiş; kabuk üssü ölçülmedi | v7 §3.8 satır 1690–1698 |
| **Tampon %3,6 ve %4,0 İKİSİ DE GİRDİ** | `aero/mass.py` `m_pil` parametresi (varsayılan 1,8); `baseline.py` `f_tampon`; askı enerjisinden türeten kod yok (arandı) |
| Sabit hatve açığı hafif %14,6–21,0, ağır %16,4–23,0 | `aero/nose-propeller-crossing.txt` ve `aero/nose-propeller-heavy.txt` |
| 2 s → 221,5 kW (%102); 5,1 s → 13,4 kW (%6) | v7 §3.9 Tablo 15 |

**Bu sayfada BİLEREK olmayanlar:**

- **Hiçbir ağır tasarım menzili.** Elimizdeki her biri kısmi: 1.814 km (rotor yüklenmemiş,
  η_p 0,80), 1.571 km (rotor yüklenmiş, η_p 0,80), 1.398–1.517 km (η_p yeniden çözülmüş, rotor
  yüklenmemiş). İkisini birden taşıyan bir kapanış yok.
- **3,8× ve batarya özgül gücü.** Tamponu askı enerjisinden türetmek tam oraya girer; Adım 14.
- **Kabuk kütlesi Fatura 1 olarak.** Gövde her mimarinin taşıdığı yapıdır; onu Fatura 1 saymak
  tanımı sınava uydurmak olur.
- **Üç faturanın ayrıştığı iddiası.** İkisi ayrışıyor; üçüncüsü sınanamıyor.
