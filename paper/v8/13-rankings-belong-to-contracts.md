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

Section 12 showed that at least two of the charges are not locked together; where one architecture pays less of one charge and more of another, the ranking depends on how the charges are weighed, and **a sizing contract is one such weighing**: it fixes what is held equal between the architectures being compared. This section applies three contracts to three architectures at each of the four closures of Section 10. **The mechanism claim is not a ranking and is not at stake here.**

### Three contracts, and what each holds equal

Range in the sizing loop is proportional to L/D, to the energy chain, propeller included, and to the fuel fraction, and the three contracts differ only in the last (Supplement S13): a **fixed fuel fraction**, sixteen percent of each architecture's own take-off mass, under which take-off mass cancels from range; a **fixed fuel mass**, the 8.4 to 9.2 kg this configuration carries, under which range is divided by take-off mass; and a **fixed take-off mass and payload**, under which every kilogram of architecture-specific hardware is a kilogram of fuel not carried. **These are three different questions, not three estimates of one answer.** A mission decides which of them it is asking; this paper has no mission that would decide, and does not choose.

### What is compared, and on what basis

Three architectures fly the same mission, 13 kg of payload at 30 m s⁻¹, with the same wing loading, disc loading and aspect ratio, the same airframe and avionics fractions, and the same fuel and energy chain apart from the propeller. **The competitors are therefore this planform with two add-ons, not independently designed aircraft of their families.** All three carry the same buffered series-hybrid power system, so Bill 3 is held common and the comparison measures mass and cruise drag. **Holding Bill 3 common is a choice of question, and it has a direction.** **The choice runs against this configuration.** Without the buffer, and with engines rated to deliver the hover demand, the lift-plus-cruise layout does not close under a fixed fuel fraction or a fixed take-off mass and falls 38 to 47 percent behind under a fixed fuel mass, and the tilt bound does not close under a fixed take-off mass; under a fixed fuel fraction it closes at 520 kg, about ten times this configuration's mass — the first contract's blindness to mass, made visible. That comparison is not used, because it would set competitors without a store against this configuration with one.

The basis is not symmetric: the lift-plus-cruise layout carries a lift-to-drag ratio transferred from a different airframe's wind-tunnel campaign (Section 2) and assumes lift rotors stopped and aligned in cruise, which takes an indexing mechanism (Section 7) whose mass is not separately charged. **The tilting layout carries no cruise drag penalty at all. That is an idealisation in its favour**, and it is deliberate: it makes the tilting layout a bound. Both competitors use a propeller efficiency of 0.80, assumed, not computed, against this configuration's computed 0.632 and 0.683; the lift-plus-cruise layout carries a lift group of 10 percent of take-off mass and the tilting layout a tilt mechanism of 5 percent. **Neither figure is measured.**

### Against lift-plus-cruise: a trade, and the contract sets the exchange rate

**The two architectures trade one charge against another**: closed under a fixed fuel fraction, this configuration is 27 to 30 percent lighter, and the lift-plus-cruise layout cruises at a lift-to-drag ratio of 11.66 and 15.72 against 8.79 and 10.82, with a propeller at 0.80.

Range of the lift-plus-cruise layout relative to this configuration:

| Closure (Section 10) | Fixed fuel fraction | Fixed fuel mass | Fixed take-off mass |
|---|---:|---:|---:|
| A | +67.8 % | +40.2 % | +1.1 % |
| B | +55.3 % | +27.5 % | **−13.0 %** |
| C | +83.9 % | +53.5 % | +7.3 % |
| D | +70.2 % | +40.1 % | **−6.5 %** |

**The lift-plus-cruise layout is 55 to 84 percent ahead under the first contract, 28 to 54 percent under the second, and between 13 percent short and 7 percent ahead under the third; the shift from first to third is 67 to 77 percentage points at every closure**, at the declared lift-group fraction, and always toward the lighter aircraft. **The sign itself changes inside the envelope under the third contract**: this configuration is ahead at the two closures with the higher-efficiency blade family and behind at the two with the lower. **A statement of which architecture has the longer range, made without its contract, would therefore be a statement about the contract.**

### Against the tilting layout: a bound, not a ranking

**What the bound gives is a size, not an order.** Credited with no cruise penalty, the tilting layout is 93 to 141 percent ahead of this configuration under every contract at every closure; that margin is the room a real tilting aircraft's cruise penalties — nacelle drag, pivot fairing, hover-sized rotors flown as cruise propellers — would have to fill, and how much of it they fill is not computed. **A ranking against a competitor modelled as a bound is not a ranking, and no range claim is made against the tilting family in either direction.**

### Section 2's prediction, tested

Section 2 predicted that such a ranking will move when the sizing rule changes, and can reverse. **The movement holds everywhere**, against both competitors, toward the lighter arrangement as the contract weights mass more; **the reversal holds at two of the four closures against lift-plus-cruise, and at none against the tilt bound.**

**Where the reversal falls is decided by quantities this study has not measured or not fixed**: the blade family in the base case, and across the sensitivity cases the competitor's lift-group mass and the propeller basis (Supplement S13). With a lighter lift group the lift-plus-cruise layout leads under all three contracts at every closure; with a heavier one this configuration leads under a fixed take-off mass at every closure; with a common propeller efficiency a reversal appears at every closure. **Which architecture ranks first under a fixed take-off mass is therefore decided, in this model, by a mass fraction of the competitor that this study has not measured.** **Put plainly, the sign under a fixed take-off mass is not a result about the architectures; it is a result about that parameter**, and it is the one most worth measuring. What is robust is that the shift exists and runs toward the lighter aircraft; its size is the size of the mass difference.

### What the framework asks of whoever uses it

**Each comparison states every charge in its own currency before any aggregate, names its contract, and states its asymmetries and their directions; an ordering is reported only with the contract it was computed under and, where its sign depends on an unmeasured quantity, with that quantity named.** This paper meets that for its own column (Section 11) and not for the competitors', whose kilograms and drag counts here are parameters and transferred ratios rather than an audit.

### What this section does not establish

**The competitors are modelled at a coarser level than this configuration**: their drag is transferred or idealised, their propeller efficiency assumed and their architecture-specific mass a parameter. **Comparing computed figures against assumed ones favours whichever is assumed more optimistically** — in propeller efficiency both competitors, and with a common propeller efficiency the lift-plus-cruise lead under the first contract falls from 55–84 to 33–45 percent (Supplement S13); in drag the tilting layout, by construction. **The comparison is at one size**: Section 12's 1 000 kg reference design has no closure, and none of its figures is used here. **And nothing here ranks architectures for a mission.** What this section establishes is narrower: **the same aircraft, under three reasonable contracts, give orderings against lift-plus-cruise that move by tens of percentage points and, inside the envelope, change sign** — so the ordering is not a property of the architectures alone.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 107 — Adım 13 yeniden kuruldu** (Tur 105–106; dört okuyucu + Claude, hiçbir cümleye veto yok): `drafts/13-recomposed.md` uygulandı; korunan cümlelerin hepsi gövdede. Özgün gövde Ek S13'de tam | `drafts/13-recomposed.md` §3 iz |
| **Tur 102 (Tur 101 oybirliği; T5):** satır adları A–D (Adım 10 tablosuyla eşleşir): adverse/lower = A, adverse/upper = B, favourable/lower = C, favourable/upper = D. Özgün tablo Ek S13'te | Adım 10 tablosu |
| **Tur 90 (dört okuyucu + Claude):** "every remedy transfers a charge rather than removing it" → "every remedy moves cost rather than removing it" — S-16'nın kopyası; 2F ile birebir | Tur 89 metni §2 |
| **Tur 87 (dört okuyucu + Claude):** "it makes the tilt row a bound" → "the tilting layout" (gövde tablosunda tilt satırı yok; karşılaştırma S13'te — `v8_refs.py` ilk koşuda yakaladı); "charges all three the same assumption" → "puts the same assumption on all three" (fatura sözcüğü genel fiil olarak, A′) | Tur 86 metni §5 |
| **Tur 71:** ikinci geçiş S1–S5 uygulandı (Qwen RW-13A–D, ChatGPT'nin tek cümlesi); **S1'de DeepSeek'in vetosu:** sözleşme tanımı (*"It fixes what is held equal…"*) aynen geri | Tur 70 metni §3 |
| **Tur 70:** Tur 69 taslağı uygulandı, iki istisnayla: 520 kg cümlesi **kaldı** (Grok'un vetosu: bu adımın kendi bulgusu, ve *"That comparison is not used"* öncülü); 0,80 gerekçeleri ve *"The contract is chosen by the mission…"* **kaldı** (Grok, Qwen). Kaybı olan her paragraf Ek S13'te aynen | Tur 69 metni §5 |
| **Tur 61:** duyarlılık tablosu Ek S13'e taşındı (dört okuyucu + Claude hemfikir, A6); gövdede 14–134 puan ve işaret cümleleri kaldı. Taşıma sırasında *"the table above shows the size of it"* sarkık kaldı — taşınan tablonun satırıydı; rakam (+55…+84 → +33…+45 %) gövdeye yazıldı | `aero/contracts-result.txt`; `paper/v8/supplement.md` S13 |
| **Tur 60:** tilt paragrafı *"a size, not an order"* — sınırın payı, gerçek tilt'in seyir cezalarının doldurması gereken alan; doldurma hesaplanmadı | ChatGPT; `aero/contracts-result.txt` |
| **Tur 58, P3:** mekanizma iddiası bir sıralama değil, burada söz konusu değil | Adım 9 bağımlılık tablosu (*"sizing contract"*); Adım 15 |
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
| Rakipler tamponsuz, motor askıyı bara üzerinden besleyecek şekilde (÷0,92×0,95×0,90): B s1 ve s3'te kapanmıyor, s2 −46,6…−38,4; tilt s1 519,6 kg (×9,0–9,9), menzil +103…+141 değişmez; s2 −4,3…+10,4; s3 kapanmıyor. **Tur 57 düzeltmesi:** önceki 380,9 kg / −23…−11 motoru rotor milindeki askı gücüne EŞİT alıyordu (`baseline.py` `motor_hover` yolu, istasyon karışıklığı — DeepSeek'in *"baseline.py'yi denetle"* önerisiyle bulundu) | `contracts-result.txt`, (d) bloğu; `baseline.py` `motor_hover_carpan` |
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
