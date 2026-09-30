# Step 3 — The escape condition

**v8 taslağı, birinci yazım.** İskeletin 3. adımı. **Bu bir tanımdır**, bir sonuç değil
(Grok, Tur 34: *"Kaçış bir tanımdır. NASA bir sınamadır."*).

**Kural denetimi:** koşul **tablodan** türetiliyor, uçaktan değil · *"inşa gereği"* dikkatli
(§0.3) · koşulun neye izin verdiği **adlandırılıyor**, yoksa uçak tanım gereği kazanır
(ChatGPT'nin Tur 41 uyarısı) · sabit hatve bedeli burada adı konuyor.

---

## The escape condition

This section asks what an architecture would have to do in order not to incur the three charges at all. The answer is a **definition**, derived by inverting the table, and it is stated here before any configuration is offered so that the standard is not taken from the thing it will be used to measure.

### Inverting the table

**A charge appears wherever the two regimes are served by hardware that departs from one of four things: the same hardware, serving both duties, held in one orientation, with the hover peak supplied other than by its continuously installed power.** **Different hardware** costs Bills 1 and 2. **The same hardware serving only one duty** costs them again. **The same hardware serving both duties in a different orientation** is the tilting family. **The same hardware, both duties, one orientation, but a different sizing point** incurs Bill 3. What each departure costs is in Supplement S3. Read one at a time, these are ways to pay. Read as a conjunction, they are a condition.

### The condition

> **An architecture does not incur the three charges if the propulsors that carry the weight,
> held in one orientation relative to the airframe, produce both the hover thrust and the cruise
> thrust, and if the difference between the hover peak and the cruise demand is supplied from
> a store rather than from permanently installed continuous power.**

Four parts: **same hardware, both duties, one orientation, hover peak from a store.**

Two things in that sentence are choices rather than derivations. The inversion requires only *one orientation relative to the airframe*; **how** an architecture keeps that while changing flight regime — by rotating the whole body, or otherwise — is not in the inversion, and is treated as exposition rather than as part of the definition. And the fourth departure's exception lets the peak come from **any** source other than the continuously installed power; a store is the narrower reading used here, because it is what the configuration examined later uses and because a narrower condition is easier to fail.

### What the condition does not say, and this matters more than what it says

**It means zero of the three charges as Section 2 defines them.** **It does not mean an architecture that costs nothing, and it does not mean an architecture that carries nothing for the vertical phase.** A definition that placed every conceivable cost inside the thing to be escaped would be unfalsifiable. Six costs are permitted, named here before any candidate is examined (the working is in Supplement S3):

- **A store is permitted**, though it is mass carried for a duty that is briefly needed, which is the complaint Bill 1 makes. **It does not claim the trade is favourable**: whether the store is lighter than the continuous power it displaces is computed, not asserted.
- **Releasing the engine is not releasing the electrical path.** Machines, power electronics and wiring still pass the full hover power, and that Bill 3 is carried in the ledger.
- **Rotating the airframe is permitted and is not priced here.** An architecture that rotates its whole body still turns its thrust axis through ninety degrees relative to the flight path, with the moments and the control through the turn that implies; that is not one of the three charges, and Section 10 analyses the transition without pricing it.
- **Hardware installed for the vertical phase is permitted if it serves both duties.**
- **Hardware used in both regimes for something other than propulsive thrust is permitted, and its cruise drag is not eliminated.** *Cruise thrust in this paper means the thrust that balances cruise drag.* Attitude devices produce none; used throughout the flight, they fall outside Bill 1, and they do not stop the propulsor that carries the aircraft from meeting the condition. But carried through cruise without producing cruise thrust, they are the first failure mode below, and Bill 2 reaches them.
- **Serving two regimes with one set of hardware has a price of its own**: a fixed geometry cannot be optimised for both, and the compromise is paid in efficiency. **The condition permits that cost and does not measure it.** Section 11 does.

**One exclusion, stated narrowly.** Structure, surfaces and actuation present for reasons other than the vertical phase are not charged **as duty-cycle mismatch under this accounting**, which says which ledger they belong in, not that they are free; it does not reach a part that would not exist but for the vertical phase. The tip frames of Section 5 are landing gear because the aircraft stands on its tail: **their mass is charged in the build-up and their drag in the ledger.**

### The condition can fail, and how

An architecture fails the condition if **any** of the following holds:

1. It carries a propulsor through cruise that produces no cruise thrust.
2. It changes the orientation of a propulsor relative to the airframe in order to change regime.
3. Its continuously installed power is sized by the hover requirement rather than by cruise.
4. It satisfies the first three only in part — for instance in its primary propulsor while a secondary set fails them — in which case the instantiation is **partial**, and the part that fails re-opens the charge it fails.

### What follows from the condition, and what does not

The condition is a statement about what an architecture would have to be. **It is not a claim that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim that satisfying it is desirable.**

**An architecture that reorients a propulsor does not satisfy the condition as written**, because the condition requires one orientation relative to the airframe. **Whether such an architecture might avoid the three charges by some other route is a separate question this paper does not settle** — the condition is a definition, not a law, and it can be too narrow without being wrong.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 191 — son okuma onarımı, satır 0** (beşimiz): *"it is priced where the transition is analysed"* → *"Section 10 analyses the transition without pricing it"* (6.1 analiz eder ve sınırlar, fiyatlamaz; alındı R4). Önceki korunan cümleye dokunulmadı. Eski paragraf S3'te | Tur 190 cevapları |
| **Tur 170 — yazarın notları üzerine kısaltma uygulandı** (Tur 168–169: işlemlerde dört okuyucu + Claude; korunan cümle taşımaları yazar kararı E13). Değişen her paragrafın eski hâli ekin bu adıma ait bölümünde aynen (*"… before the Round 170 shortening"*). Yeni (R) cümleler Tur 170 §2'de okuyucu vetosuna açık; sonuç teyide | `paper/build/v8_round170_texts.py`, `v8_round170_apply.py` |
| **Tur 172 — hesap geçişi (yazar E14, E15; katman 1 okuyucu teyidine)** 2.2.5 kısaldı (yazarın notu): yol haritası cümlesi ve 2.1 tekrarı çıktı; korunan üç cümle yerinde. Eski paragraflar ekte aynen | — |
| **Tur 173 — 2.2.3 sayım tekrarı ("The first three come from…") kesildi.** Eski paragraflar ekte aynen; okuyucu teyidine | — |
| **Tur 174 — 2.2.5 ses cümlesi kesildi; E17 a (C) "An architecture may meet the condition where it carries the aircraft …".** Eski paragraflar ekte aynen; okuyucu teyidine | — |
| **Tur 148 — W-7 (a′) uygulandı** (dört okuyucu + Claude): *"The tip frames are the case"* → *"The tip frames of the configuration described in Section 5 are the case"* (benim ilk işaretçim 5.2'ydi, DeepSeek düzeltti). W-6 ikinci yan cümle değişmedi (oybirliği); W-6, W-10 kapandı | Tur 147 §2 |
| **Tur 147 — W-6 ve W-10 uygulandı** (bütün okuma; dört okuyucu + Claude): W-6 *"Attitude devices produce thrust in cruise, but they produce…"* → *"Attitude devices produce…"* (kumandasız seyir durumu serbest dönme; ikinci yan cümle ayrışık); W-10 ilk cümle silindi, *"that departure"* → *"the third departure"*, *"the first departure"* → *"the first"*. W-7 (uç çerçeveleri, işaretçi Bölüm 3'e mi, taşıma mı) geri soruldu | Tur 146 §5; Tur 147 §1 |
| **Tur 117 — S-44 onarıldı** (Tur 116; dört okuyucu + Claude): "would win by construction rather than by performance" → "by definition"; "by construction" yalnız Adım 9 madde 8'in anlamında (boyutlandırma gereği) | Tur 116 metni §3 |
| **Tur 114 — C-kısa** (Tur 113; dört okuyucu + Claude; yazarın sorusu): dördüncü sapma cümlesinin "— unless the hover peak is supplied from somewhere other than the continuously installed power" kısmı çıktı (C 60 → 46 kelime); "the fourth departure's exception" kendi cümlesinde tanımlı | Tur 113 metni §2 |
| **Tur 113 — R-8 onarıldı, seçenek C** (Tur 112; dört okuyucu + Claude; Qwen'in itirazı üzerine): dört sapma cümlesi, sapmayı adlandıran sözcüklere kadar silinmiş hâlleriyle (dördüncüsü tam, "exception"ın öncülü) D3'ün ardına. Sıra göndergeleri (D7, D10, D25, D47, D48) artık adlandırılmış öncüllere bağlı; `v8_refs.py` bunu sınıyor (Grok P91) | Tur 112 metni §4 |
| **Tur 111 — Adım 3 sonuç cümleleriyle yeniden kuruldu** (Tur 110; dört okuyucu + Claude, veto yok): 1 654 → 1 305. Dört sapma cümlesi (Ek S3 tablosu taşıyor) ve ikinci sapma parantezi Ek S3'e; "Two things … are choices" (O4 reddedildi), eğme kurulumu D47–D48, uç çerçevelerin "landing gear" gerekçesi gövdede. Özgün Ek S3'te tam | Tur 110 metni §4, `drafts/03-recomposed.md` |
| **Tur 87 (yeniden kurma, 3F; P39):** 3F 279 → 229 — F1 (S-9: "Those" yanlış üçlüye işaret ediyordu → "Three questions follow from it"), F2 (S-10: "the longest of the three answers" yanlış → "the answer most likely to be wrong"), F3 (3B evi), F4 (S-2 "the first departure"), F5 (3A evi, korunan). Elektrik yolu: "a charge" → "Bill 3 on the electrical path" (Adım 11'in korunan cümlesiyle). Dört okuyucu + Claude. 3E kilitli, değişmedi. Özgün 3F Ek S3'te donmuş | Tur 86 metni |
| **Tur 86 (yeniden kurma, 3D; E2):** 880 → 797. D2 (A′ evi), D3, D4, D7 (3B evi), D8; **S-8** D5 "a mass one" → "a cost in kilograms" (Adım 9 ve 11 de), D6 "charges that refusal" → "sets". **E2 yazarın kararı:** "zero-bill condition" adı düştü → "The condition has to be read exactly."; "the first most nearly contradicts the name" gönderge kaybetti → silindi ("Six of them:"; bilgi ilk maddede). Dört okuyucu + Claude. Özgün 3D Ek S3'te donmuş | Tur 85 metni |
| **Tur 85 (yeniden kurma, 3A ve 3C):** 3A 77 → 60 (A1 çıktı — evi 2F; A2 R — gönderge; A3 D — evi 2F); 3C 196 → 190 (C3 D; C4, C5 R — **S-7**: Tur 64'te 3B tablosu S3'e taşınınca 3C'deki "the table" 2E tablosuna işaret eder olmuştu). Kör okuma dördünde geçti. Dört okuyucu + Claude. Özgünler Ek S3'te donmuş | Tur 84 metni |
| **Tur 84 (yeniden kurma, 3B):** 271 → 247 kelime. R1 (dört özellik; "because" → "wherever" — kaynağın S-6 sayım hatasının **esaslı onarımı**, üslup değil), R6 ("leaves" → "incurs"), D3 (Fatura 1–2 açıklaması, iki ev kuralı), D8, D9. Kör okuma dördünde de geçti. Dört okuyucu + Claude. Özgün 3B Ek S3'te donmuş | Tur 83 metni |
| **Tur 81:** 3B üçüncü sapma "left standing" → "incurred" (S5-4; dört okuyucu + Claude): 3B tabana göre karşılaştırmıyor, ne ödendiğini söylüyor. Ek S3 aynı değişiklik + Tur 65'te emekli "complexity" (kaçırılmıştı) | Tur 80 metni §2 |
| **Tur 64 — N1 uygulanırken bulunan eski hata:** *"The second row of the inverted table — same hardware, different orientation"* — farklı yönelim **üçüncü** satırdı; *"tek görev"* satırı sonradan araya girince atıf bayat kalmış. *"The third departure — same hardware, both duties, different orientation"* | bu bölümün dört ayrılışı |
| **Tur 64 — N1** (beşimiz hemfikir): tablo dört cümleye; *"complexity"* çıktı (ölçülmedi — ChatGPT); *"row"* → *"departure"* (dört yerde); ikinci ayrılışın gerekçe parantezi kaldı | Ek S3 |
| **Tur 60:** tutum donanımı taşıyan propulsor'ün koşulu karşılamasını engellemez, ama seyirde seyir itkisi üretmeden taşınır → birinci başarısızlık kipi; mimari kısmi gerçekleşme (dördüncü kip). Eski *"does not violate it"* Adım 7/8 ile çelişiyordu | DeepSeek; bu bölümün başarısızlık kipleri 1 ve 4 |
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
