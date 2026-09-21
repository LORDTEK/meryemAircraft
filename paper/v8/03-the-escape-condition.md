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

The charges exist because the two regimes are served by hardware that is **not the same hardware,
not serving both duties, and not held in one orientation.** Depart from any one of those and a
charge appears:

| Departure | What it costs |
|---|---|
| **Different hardware** | Bills 1 and 2. The unused set is carried for the whole flight and, if exposed, drags. |
| **Same hardware, but it serves only one duty** | Bills 1 and 2 again. A propulsor that lifts and is then carried is a dedicated lift group under another name, whatever it shares with the cruise system. |
| **Same hardware, both duties, different orientation** | The tilting family. **Bill 3 is left standing unless a store supplies the hover peak**, and the mechanism that changes the orientation is itself mass, complexity and a control problem through the turn. |
| **Same hardware, both duties, one orientation, different sizing point** | Bill 3 — unless the hover peak is supplied from somewhere other than the continuously installed power. |

Read downwards, the table is a list of ways to pay. Read as a conjunction, it is a condition.

*(The second row is stated separately rather than folded into the first because it does real
work later: a propulsor that produces a little thrust in cruise is not thereby serving both
duties, and the distinction decides which parts of a configuration meet the condition and which
do not. "Serving both duties" is the accurate form; hover thrust and cruise thrust are not the
same **job** in any ordinary engineering sense — one supports weight, the other balances drag —
and calling them one would be loose.)*

### The condition

> **An architecture does not incur the three charges if the propulsors that carry the weight,
> held in one orientation relative to the airframe, produce both the hover thrust and the cruise
> thrust, and if the difference between the hover peak and the cruise demand is supplied from
> a store rather than from permanently installed continuous power.**

Four parts: **same hardware, both duties, one orientation, hover peak from a store.** The first
three come from the first three rows of the table; the fourth comes from the fourth.

Two things in that sentence are choices rather than derivations, and are marked as such. The
table requires only *one orientation relative to the airframe*; **how** an architecture keeps
that while changing flight regime — by rotating the whole body, or otherwise — is not in the
table, and is treated as exposition rather than as part of the definition. And the table's last
row permits the peak to come from **any** source other than the continuously installed power; a
store is the narrower reading used here, because it is what the configuration examined later
uses and because a narrower condition is easier to fail.

### What the condition does not say, and this matters more than what it says

The condition is named below the **zero-bill condition**, and the name has to be read exactly.
**It means zero of the three charges as Section 2 defines them** — the mass of a dedicated lift
subsystem, the cruise drag of hover hardware left exposed, and continuous power installed to a
hover peak. **It does not mean an architecture that costs nothing, and it does not mean an
architecture that carries nothing for the vertical phase.** A definition that placed every
conceivable cost inside the thing to be escaped would be unfalsifiable, and an architecture
built to satisfy it would win by construction rather than by performance.

So the costs the condition permits are named here, before any candidate is examined. Six of them,
and the first is the one that most nearly contradicts the name:

- **A store is permitted, and it has the same duty-cycle character as Bill 1.** The fourth part
  moves the hover peak off the continuous power plant and onto a store; that store delivers its
  peak for two percent of the flight and is carried for the rest. It is not Bill 1 as Section 2
  defines it — it is not lift-subsystem mass — **but it is mass carried for a duty that is
  briefly needed, which is the same complaint Bill 1 makes.** The condition converts a power-
  system charge into a mass one and claims only that the three charges as named are not incurred.
  **It does not claim the trade is favourable.** Whether the store is lighter than the continuous
  power it displaces is a sizing result and is computed, not asserted.
- **Releasing the engine is not releasing the electrical path.** The fourth part frees the
  continuous *power plant* from the hover peak. Everything between the store and the rotors —
  machines, power electronics, wiring — still passes the full hover power and is still sized by
  it. **That is a charge the condition does not remove**, and it is carried in the ledger rather
  than in this definition.
- **Rotating the airframe is permitted and is not priced here.** The condition refuses
  architectures that reorient a propulsor, and charges that refusal against the mechanism a tilt
  requires. **An architecture that instead rotates its whole body faces the same physical
  problem** — a ninety-degree change of the thrust axis relative to the flight path, with the
  moments, the authority and the control through the turn that implies. It is not one of the
  three charges and the condition does not eliminate it; it is priced where the transition is
  analysed. Saying otherwise would let a candidate win that line by wording.
- **Hardware installed for the vertical phase is permitted if it serves both duties**, and the
  second row of the table is what carries the weight. A propulsor that lifts and then propels
  satisfies the condition. A propulsor that lifts and is then carried does not, whatever else it
  shares with the cruise system.
- **Hardware used in both regimes for something other than propulsive thrust is permitted, and its
  cruise drag is not eliminated.** *Cruise thrust in this paper means the thrust that balances
  cruise drag.* Attitude devices produce thrust in cruise, but they produce no cruise thrust in
  that sense; they are used throughout the flight, so their duty cycle matches their presence and
  they fall outside Bill 1. **They remain in the airstream, so the second charge reaches them.**
  Those are two different statements and the distinction matters: **the condition is about the
  propulsor that carries the aircraft, so attitude hardware does not violate it — but the charges
  are about everything the aircraft carries, so Bill 2 reaches that hardware anyway.** An
  architecture in that position is a partial instantiation: it satisfies the condition where the
  condition applies and still pays one of the three elsewhere. The condition permits such hardware
  and does not make it free.
- **Serving two regimes with one set of hardware has a price of its own.** Hardware that is not
  duplicated cannot be optimised twice: a propeller sized for hover thrust at zero forward speed
  is not the propeller a cruise design would choose, and if its geometry is fixed the compromise
  is paid in efficiency. **The condition permits that cost and does not measure it.** Section 11
  does.

**One exclusion, stated narrowly.** Structure, surfaces and actuation present for reasons other
than the vertical phase are not charged **as duty-cycle mismatch under this accounting** — a
wing, a control device, a fairing that earns its place on a part already carried. That is a
statement about which ledger they belong in, not a claim that they are free, and it does not
apply to a part that would not exist but for the vertical phase. The tip frames are the case
that tests it: they are landing gear because the aircraft stands on its tail, and they also
carry the attitude propulsors and the directional fairing. **Their mass is charged in the
build-up and their drag in the ledger; the exclusion does not reach them.**

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
first with a mechanism. **An architecture that reorients a propulsor does not satisfy the condition as written**, because
the condition requires one orientation relative to the airframe. **Whether such an architecture
might avoid the three charges by some other route is a separate question this paper does not
settle** — the condition is a definition, not a law, and it can be too narrow without being
wrong. What it is not is retrofitted: it is stated here so that when a configuration is offered
later, the reader can check the claim against a standard fixed before the configuration
appeared.

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

**Tur 42'de düzeltilenler — merkezde bir mantık kusuru vardı.**

ChatGPT *"Tur 42'nin en önemli meselesi"* dedi ve Grok aynı yere geldi: sayfa bir yandan
**"sıfır fatura"** diyor, öte yandan tamponu **"bir Fatura 1 ödemesi"** diye adlandırıyordu.
Aynı sayfada. Grok'un ifadesiyle: *"Hakem ikisini birden alıntılar. Ya adı bırakın, ya Fatura
1'i kullanılmayan kaldırma alt sistemi kütlesi olarak tanımlayın. İki ifadeyi birden
tutmayın."*

**Çözüm tanımı daraltmak değil, itiraf etmek oldu.** Tampon §2'nin tanımladığı Fatura 1 değil —
kaldırma alt sistemi kütlesi değil — **ama kısa süre gereken bir görev için taşınan kütledir, ki
Fatura 1'in şikâyeti tam olarak budur.** Sayfa artık bunu söylüyor: koşul bir güç sistemi
faturasını bir kütle faturasına **çeviriyor** ve yalnız adı konmuş üç faturanın doğmadığını
iddia ediyor.

**DeepSeek: elektrik yolu serbest kalmıyor.** Doğrulandı, §2.9'da yazılı: *"The electrical path
is not released."* Tampon motoru serbest bırakıyor; makineler, güç elektroniği ve kablolama
hâlâ tam askı gücünü geçiriyor ve hâlâ ona göre boyutlanıyor. İzin verilen bedeller listesine
girdi.

**Grok: gövdeyi döndürmek de ücretsiz sayılıyordu.** En keskin bulgu. Propulsor döndürmek
bedelli (mekanizma, gyroskopik bağlaşım, geçişte kontrol); gövdeyi döndürmek **aynı fiziksel
problem** ve sayfada hiç geçmiyordu. *"Bu beşinci izin verilen kalem olmadan, gövdeyi çeviren
bir aday 'geçişte kontrol' satırını kelime oyunuyla kazanır."* Eklendi.

**Üçü birden: "same job" tabloda yoktu.** Grok dördüncü bir satır olarak konmasını istedi;
kondu. ChatGPT ayrıca adlandırmanın yanlış olduğunu gösterdi — askı itkisi ağırlığı taşır, seyir
itkisi sürüklemeyi dengeler, bunlar aynı **iş** değil. *"Her iki görevi de görmek"* oldu.

**DeepSeek: tampon, "sürekli güçten başka bir kaynak"ın daraltılmasıdır** — bir kavrama, bir
süperkapasitör de sağlardı. Türetme değil, **seçim** olarak işaretlendi. Aynı şekilde gövdenin
dönmesi de tabloda yok; açıklama olarak ayrıldı.

**DeepSeek + Grok: uç çerçeveleri.** *"Dikey fazdan başka gerekçesi olan yapı muhasebenin
tamamen dışındadır"* fazla genişti ve tam da çerçeveleri park etmeye yarardı. Daraltıldı ve
çerçevelerin **muafiyetin dışında** olduğu açıkça yazıldı: kuyruğu üstünde durduğu için iniş
takımılar.

**Qwen: tutum çiftlerinin sürüklemesi.** Koşulun görmediği tek bedel. İzin verilen bedel olarak
adlandırıldı — görev çevrimleri varlıklarıyla uyuştuğu için Fatura 1'in dışındalar, ama yine de
akış içindeler.

**DeepSeek: *"whatever else it achieves"* fazla genişti.** Koşul bir yasa değil, bir tanım;
fazla dar olabilir ve bu yanlış olmasını gerektirmez. Düzeltildi.

**Adım 8'e de bir cümle girdi** (DeepSeek): uç çiftleri artık envanterde **kısmî örneklemenin
başarısız olan parçası** olarak adlandırılıyor.

**Bu sayfada BİLEREK olmayanlar:** hiçbir uçak, hiçbir sayı, ve koşulu sağlayan bir şey
olduğu iddiası. Sayfa bir tanım kurar ve orada durur.
