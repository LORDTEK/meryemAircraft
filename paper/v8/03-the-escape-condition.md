# Step 3 — The escape condition

**v8 taslağı, birinci yazım.** İskeletin 3. adımı. **Bu bir tanımdır**, bir sonuç değil
(Grok, Tur 34: *"Kaçış bir tanımdır. NASA bir sınamadır."*).

**Kural denetimi:** koşul **tablodan** türetiliyor, uçaktan değil · *"inşa gereği"* dikkatli
(§0.3) · koşulun neye izin verdiği **adlandırılıyor**, yoksa uçak tanım gereği kazanır
(ChatGPT'nin Tur 41 uyarısı) · sabit hatve bedeli burada adı konuyor.

---

## The escape condition

The previous section listed moves that redistribute the three charges. This one asks a different
question: what would an architecture have to do in order not to incur them at all? The answer is
a **definition**, derived by inverting the table rather than by describing any aircraft, and it
is stated here before any configuration is offered so that the standard is not taken from the
thing it will be used to measure.

### Inverting the table

The charges exist because hover and cruise are served by hardware that is **not the same
hardware, doing the same job, in the same orientation.** Relax any one part of that and a charge
appears:

| Relaxation | What it costs |
|---|---|
| **Different hardware** | Bills 1 and 2. The unused set is carried for the whole flight and, if exposed, drags. |
| **Same hardware, different orientation** | The tilting family. The mechanism that changes the orientation is itself mass, complexity and a control problem through the turn. |
| **Same hardware, same orientation, different sizing point** | Bill 3 — unless the hover peak is supplied from somewhere other than the continuously installed power. |

Read downwards, the table is a list of ways to pay. Read as a conjunction, it is a condition.

### The condition

> **An architecture does not incur the three charges if the same propulsors, held in one
> orientation relative to the airframe, produce both the hover thrust and the cruise thrust —
> the aircraft changing its orientation rather than any part of it — and if the difference
> between the hover peak and the cruise demand is supplied from a buffer rather than from
> permanently installed continuous power.**

Four parts: **same hardware, same job, same orientation, hover peak from a buffer.** The first
three come from the first two rows of the table; the fourth comes from the third.

### What the condition does not say, and this matters more than what it says

The name used below is the **zero-bill condition**, and it must be read strictly. **It means
zero of these three charges. It does not mean an architecture that costs nothing.** A definition
that placed every conceivable cost inside the thing to be escaped would be unfalsifiable, and an
architecture built to satisfy it would win by construction rather than by performance. So the
costs the condition explicitly permits are named here, before any candidate is examined:

- **Buffer mass is permitted, and it is a real payment.** The fourth part of the condition moves
  the hover peak off the continuous power plant and onto a store, and that store is mass carried
  for the whole flight — a Bill 1 payment made to avoid a Bill 3 payment. **The condition does
  not claim the trade is favourable.** Whether the buffer is smaller than the engine it displaces
  is a sizing result, not a definitional one, and it is computed rather than asserted.
- **Hardware installed for the vertical phase is permitted if it is also used in cruise**, and
  the "same job" clause is what carries the weight. A propulsor that lifts and then propels
  satisfies it. A propulsor that lifts and is then carried does not.
- **Serving two regimes with one set of hardware has a price of its own.** Hardware that is not
  duplicated is hardware that cannot be optimised twice: a propeller sized for hover thrust at
  zero forward speed is not the propeller that a cruise design would choose, and if its geometry
  is fixed the compromise is paid in efficiency. **The condition permits that cost and does not
  measure it.** Section 11 does.
- **Any structure, surface or actuation present for reasons other than the vertical phase is
  outside the accounting entirely** — a wing, a control device, a fairing that earns its place on
  a part already carried. The three charges are about hardware whose duty cycle does not match
  its presence, not about everything an aircraft contains.

### The condition can fail, and how

A definition worth stating is one an architecture can be shown not to meet, so the failure modes
are explicit. An architecture fails the condition if **any** of the following holds:

1. It carries a propulsor through cruise that produces no cruise thrust.
2. It changes the orientation of a propulsor relative to the airframe in order to change regime.
3. Its continuously installed power is sized by the hover requirement rather than by cruise.
4. It satisfies the first three only in part — for instance in its primary propulsor while a
   secondary set fails them — in which case the instantiation is **partial**, and the part that
   fails re-opens the charge it fails.

The fourth is not a technicality, and it is the reason this list exists. **An architecture may
meet the condition where it carries the aircraft and fail it elsewhere**, and a paper that
reported only the first half would be reporting the condition rather than the aircraft.

### What follows from the condition, and what does not

The condition is a statement about what an architecture would have to be. **It is not a claim
that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim
that satisfying it is desirable.** Those are three separate questions and they are answered
separately: whether the accounting behind the condition survives contact with an independent
sizing study is tested in the next section, against data this work did not produce; whether any
configuration satisfies the condition is the subject of Sections 5 to 7; and what such a
configuration pays instead is the subject of Section 11, which is the longest of the three
answers because it is the one most likely to be wrong.

One consequence is worth stating now, because it shapes everything after it. The second row of
the inverted table — same hardware, different orientation — is refused by a means other than the
one the field has adopted. A tilting architecture accepts that row and buys its way out of the
first with a mechanism. **The condition as written closes that route by construction: it requires
one orientation relative to the airframe, so an architecture that reorients a propulsor does not
satisfy it, whatever else it achieves.** That is a property of the definition and not yet a claim
about any hardware, and it is stated here so that when a configuration is offered later, the
reader can check the claim against a standard that was fixed before the configuration appeared.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| Üç gevşetme ve her birinin doğurduğu fatura | §2.6, satır 671–677 |
| Koşulun dört parçası: aynı donanım, aynı iş, aynı yönelim, tampondan tepe | §2.6, satır 679–684; §2.12, satır 2785–2788 |
| *"Sıfır fatura"* adı katı okunur: bu üç faturadan sıfır, bedelsiz mimari değil | §2.6, satır 684–686 |
| Koşulu sağlayanın ne ödediği ayrı bir sorudur | §2.6, satır 686–688 |
| Kısmî örnekleme: birincil propulsor sağlar, tutum sistemi sağlamaz | §2.7, satır 692–700 |
| Tilt, ikinci satırı kabul edip birinciden mekanizmayla çıkar | §2.6, satır 674–675 |
| Sabit geometrili pervane iki görevde birden en iyi olamaz | `paper/nose-pair-finding.md`; §3.4'ün uç çiftleri için aynı savı |

**Tur 41'in uyarısı bu sayfanın merkezinde.** ChatGPT şunu yazdı: *"Vergiden kaçmak, üç
faturanın herhangi bir yerinde görünen şeylerin hiçbirini ödememek anlamına gelemez. Yoksa
makale sorunu öyle dar tanımlar ki uçak inşa gereği kazanır."* Bu yüzden sayfanın en uzun
bölümü koşulun **neye izin verdiğidir**, ve dördü de adlandırılmıştır: tampon kütlesi, seyirde
de kullanılan dikey donanım, **sabit hatve uzlaşması**, ve dikey fazdan başka gerekçesi olan
her yapı. Ayrıca koşulun **nasıl başarısız olabileceği** dört madde hâlinde yazılmıştır;
dördüncüsü kısmî örneklemeyi adlandırır, ki bu uçağın kendi durumudur.

**Bu sayfada BİLEREK olmayanlar:** hiçbir uçak, hiçbir sayı, ve koşulu sağlayan bir şey
olduğu iddiası. Sayfa bir tanım kurar ve orada durur.
