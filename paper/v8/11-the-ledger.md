# Step 11 — The ledger

**v8 taslağı, birinci yazım.** İskeletin 11. adımı.

**Kapsam Grok ve DeepSeek tarafından, Tur 52'de birlikte konuldu ve kabul edildi:**
defter **atıf yapar, eklemez.** Adım 10'un sayıları uç çerçeve sürüklemesini, sabit hatve
uzlaşmasını, burulma bedelini ve hepsinin kütle sonuçlarını **zaten içeriyor**; defter
bunları tekrar eklerse `closure_inputs.py`'de yakalanan çift sayımın düzyazı hâli olur.

**Kural denetimi:** hiçbir kalem eklenmiyor, **ayrılıyor** · DeepSeek'in ayrımı korunuyor
(ayrıştırılabilir / ayrıştırılamaz) · **tek bir "mimarinin bedeli" sayısı verilmiyor** ve
neden verilmediği yazılıyor · **3,8× burada GEÇMİYOR** (Grok: *"o paket 14'te tek paragraf
kalır"*) · sıralama yok, Adım 13'ün işi.

---

## The ledger

Section 2 named three charges that any architecture in this corner pays; **this section says where each charge appears inside the closed numbers of Section 10, and how large it is there.** Like the closure, the ledger prices the arrangement; the count of mechanism classes is not an entry in it.

**It attributes. It does not add.** Every cost named below is already inside the closure of Section 10. **No new physical cost term is introduced here.** **And there is no single figure for what the architecture costs.** The three charges are in three different currencies — kilograms, drag counts, installed kilowatts — and **no scalar aggregate is defined, because this study has no defensible weighting between them.** **The total is the contract, not a property of the aircraft** (Section 13).

### Bill 2 — the drag of hover hardware, inside the bracket

In the zero-lift drag build-up behind Section 10's bracket (line items in Supplement S11), **the hardware exposed by the vertical-phase layout — the tip frames and the free-wheeling attitude rotors — is 69 percent of the zero-lift drag at the favourable end and 57 percent at the adverse one**; the rotor term alone is 0.0154 at the favourable end. **The rotor line rests on section drag at low Reynolds number.** It is a blade-element result for sections near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section polars that are computed rather than measured; Section 12 shows how strongly the term depends on it. **The tip-frame term is an attribution, not a marginal removal cost**: it is not a claim that this drag would disappear if the vertical phase did.

Removing the hub and small items, the tip frames and the free-wheeling rotors gives a clean-body lift-to-drag ratio of 20.55 at the favourable end and 15.24 at the adverse one, against the aircraft's 10.82 and 8.79: **the configuration retains 52.6 and 57.7 percent.** Bill 2 therefore occupies a larger share where the clean-body drag is lower, because a near-constant charge is set against a smaller total — a statement about position within the drag bracket at one scale, not about size (Section 12).

**Rotor–structure and rotor–wing interference is not modelled and is not carried as a line.** Section 2's wind-tunnel source found that a simulation assuming negligible rotor–structure interaction predicts lower drag than was experimentally observed; this build-up is such a calculation, and the bracket's upper margin is the only provision made for it.

### The cruise-efficiency gap under fixed pitch

Section 10's closures run at a cruise propeller efficiency of 0.632 to 0.683: **relative to the 0.80 the published chain assumed, 14.6 percent lower at the better blade and 21.0 percent lower at the worse.** **The ledger does not attribute the whole of that gap to the absence of variable pitch.** **No variable-pitch counterfactual was computed.** Nor is the gap decomposed.

### Bill 1 — carried mass, and what it is on this configuration

**There is no dedicated lift group to charge.** What Bill 1 becomes here is the energy buffer: **3.6 percent of take-off mass, 1.9 to 2.1 kg across the four closures.** The buffer is not lift-subsystem mass, so it is not Bill 1 as Section 2 defines it, but it is carried for the whole flight to serve a demand that lasts about two percent of it: **the architecture converts a power-system charge into a cost in kilograms**, as Section 3 said in advance it would.

**The buffer fraction is an input to the loop, not a result of it.** The deficit per kilogram of take-off mass that the buffer covers, taken at the electrical bus, spreads by 12 percent across the four closures while the fraction is held at 3.6 percent (Supplement S11). **The corner that needs the most buffer per kilogram is given the smallest buffer**, and that is a declared assumption of the closure rather than an outcome of it.

### Bill 3 — released from the engine, and not from the electrical path

The engine is sized by cruise, **3.54 to 5.17 kW** of shaft rating, against a hover requirement of **11.4 to 12.5 kW** at the rotor shaft: a ratio of installed hardware of **2.4 to 3.2**, which is not the buffer's burden (Section 14 computes that). **But the full hover power passes through the electrical path, and that path is sized by it.** **Bill 3 is removed from the engine and left standing on the electrical system** (the propulsion-mass split is in Supplement S11).

### What the closure does not contain

Section 10's convergence does not cover the cost of declining the reaction-torque channel, the sizing of the strip's actuation, the allocation of the take-off margin against attitude authority, the landing transition, the vortex ring state, closed-loop hover control, engine installation, or rotor–structure and rotor–wing interference; **none of these is a ledger entry, and Section 14 lists them.** **The first and the last are the two that would most change the numbers above if they were computed.**

**Every one of the charges above belongs to one scale**: the four closures do not establish how the three charges behave as the aircraft changes size, which Section 12 asks, or what happens to the comparison when the sizing contract changes, which Section 13 asks.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 106 — Adım 11 yeniden kuruldu** (Tur 103–105; dört okuyucu + Claude, R cümlelerine veto yok; R15 "occupies" ve J18 teyitli): `drafts/11-recomposed.md` uygulandı. Kalem kalem sürükleme dökümü ve korunan "No line item at the adverse end…" **birlikte Ek S11'de — kural (iii), yazar kararı (E9, Tur 106)**. R15 korunur. Özgün gövde Ek S11'de tam | `drafts/11-recomposed.md` §3 iz |
| **Tur 86 (S-8, dört okuyucu + Claude):** "converts a power-system charge into a mass one" → "into a cost in kilograms" — A′'ye göre depo fatura değil; aynı ifade Adım 3, 9, 11'de birlikte düzeltildi | Tur 85 metni §5 |
| **Tur 73:** 5,4 m cümlesine model ve geometri geri kondu (ChatGPT'nin model kilidi; dört okuyucu + Claude). Kaynak: S11 tablosunun özgün satırı | Tur 72 metni §3 |
| **Tur 72:** ikinci geçiş (a) *"The refusal has an address…"* silindi, (b) dört görev cümlesi silindi (ilk geçiş Adım 8'de), (c) *"and section drag is hardest to predict in that range"* silindi (Adım 12'de duruyor), (d) L/D paragrafı tek cümle (R). Dört okuyucu + Claude. 2 044 → 1 957 | Tur 71 metni §3 |
| **Tur 71:** birinci geçiş 11.1, 11.3, 11.4 uygulandı (dört okuyucu + Claude); **11.2'ye veto** (DeepSeek, ChatGPT; Grok geri koyma istedi) → Reynolds cümlesi aynen kaldı. Kaybı olan paragraflar Ek S11'de | Tur 70 metni §4 |
| **Tur 66 — dokuzuncu tablo (melez):** tablo Ek S11'e; gövdede sınır cümlesi — *"None of these is a ledger entry"* (Grok: her kalemi *"debt"* diye adlandırmak Qwen'in ayrımını bulanıklaştırırdı); *"the allocation of the take-off margin against attitude authority"* (Qwen, ChatGPT: marjın kendisi boyutlanmış, kapanmayan paylaşım); *"The first and the last…"* kaldı | Ek S11; Adım 14 listesi |
| **Tur 64 — B7** (beşimiz hemfikir; Grok ve Qwen'in şartıyla): C_D0 döküm tablosu düzyazıya — **her rakam** (temiz yüzey, göbek, çerçeve, rotor, toplam, iki uç) ve iki sütun notu aynen kaldı; tablo Ek S11'e | `aero/drag_sweep.py`; Ek S11 |
| **Tur 61:** kapanış açılışı tekrar etmiyor — *"Three charges, three currencies, no total"* ve *"No charge on this page is a new one"* çıktı; açılıştaki *"It attributes. It does not add."* ve *"no scalar aggregate"* duruyor (A4) | bu bölümün açılışı |
| **Tur 60:** *"50 kg reference geometry"* | terim birliği |
| **Tur 59:** 0,168–0,188 kW/kg **kalkış kütlesi başına** (Adım 14'ün 4,7–5,2'si tampon kütlesi başına; 0,168/0,036 = 4,67) | Qwen; `aero/buffer-result.txt` |
| **Tur 58, P3:** defter düzeni fiyatlıyor; sayım bir kalem değil | Adım 9 bağımlılık tablosu; bu bölümün *"It attributes. It does not add."* |
| C_D0 dökümü: temiz yüzey, göbek, çerçeveler, rotorlar | `aero/drag_sweep.py` satır 41–48; `aero/ledger.py` |
| Askı donanımı C_D0'in %69'u (elverişli) / %57'si (olumsuz) | `aero/ledger-result.txt` |
| Temiz gövde L/D **20,55 / 15,24**; uçak 10,82 / 8,79; korunan %52,6 / %57,7 | `drag_sweep.zincir(cd0, pay=...)`; `ledger-result.txt` |
| **DÜZELTME, Tur 53 — Grok ve DeepSeek bağımsız olarak buldu.** `zincir()` olumsuz uçta marjsız çerçeve+rotor çıkarıyordu; az çıkarınca temiz gövde 14,29 görünüyordu, doğrusu 15,24. **Kapanışa etkisi YOK** — `carpan` bir orandır ve `LD_temiz × carpan = ld(toplam)` olarak sadeleşir; dört kapanış birebir aynı | `aero/drag_sweep.py:zincir` docstring; doğrulandı |
| Tampon bir **GİRDİ**; açık **bara tabanında** 0,168–0,188 kW/kg, yayılım %12; sabit %3,6 bunu izlemiyor (**Tur 56'da düzeltildi:** önceki 0,128–0,150 / %17 rotor milinden motor milini çıkarıyordu — v7'nin `thrust.py`'de düzelttiği istasyon karışıklığı) | `aero/ledger-result.txt` tampon denetimi (Grok sordu); `aero/buffer-result.txt` §1 |
| Gövde 0,300 ve aviyonik 0,080 **kuruluş sabiti**, defter sonucu değil | `baseline.py` `ORTAK`; üç mimaride de ortak |
| **Fatura 2 elverişli uçta DAHA AĞIR** — sabit rotor terimi küçülen toplamın daha büyük kesri | aynı çıktı; gerekçe dökümden doğrudan |
| Olumsuz uca **bütün döküme** %10 pay uygulanıyor | `drag_sweep.py` satır 48: `UST = (...) * 1.1` |
| Girişim modellenmedi; rüzgâr tüneli bulgusu | Adım 2, §2.3'ten: *"always predict higher lift and lower drag"* |
| η_p açığı %14,6 (0,683) ve %21,0 (0,632) | `aero/ledger-result.txt` |
| Açık kaynak başına **bölünmedi** | `nose_propeller_crossing.py` tek η veriyor, ayrışım yok |
| Tampon %3,6; 1,9–2,1 kg | `baseline.py` `f_tampon=0.036`; `ledger-result.txt` |
| Tamponun Fatura 1 karakteri taşıdığı **önceden** söylenmişti | Adım 3, izin verilen maliyetler, birinci madde |
| Gövde 0,300 · aviyonik 0,080 · tahrik 0,176–0,198 | `baseline.py` `ORTAK`; `ledger-result.txt` |
| Motor 3,54–5,17 kW; askı 11,4–12,5 kW; oran 2,4–3,2 | `aero/closure-result.txt` ve `ledger-result.txt` |
| Tahrik kesri: sabit 0,108 + güce bağlı 0,068–0,090 | `baseline.py` `F_TAHRIK_SABIT`; `ledger-result.txt` |
| Elektrik yolu askı gücüyle boyutlanıyor, motor değil | Adım 3, izin verilen maliyetler, ikinci madde |
| Kapanışta olmayanlar listesi | `paper/deferred-decisions.md` açık teknik kalemler |
| 5,4 m bir **sonuç**, bir kalem değil; referans geometride | Adım 10, geçiş bölümü |

**Bu sayfada BİLEREK olmayanlar:**

- **Hiçbir YENİ kalem.** Sayfanın tamamı Adım 10'un sayılarının içini söküyor. Grok ve
  DeepSeek'in şartı: *"Adım 10'un kapattığı bir kilogramı bile ekleme."*
- **Tek bir "mimarinin bedeli" sayısı.** Üç para birimi var; ağırlıklandırma dayanağı yok.
- **3,8× ve batarya paketi.** Adım 14'ün tek paragrafı (Grok'un şartı).
- **Hiçbir sıralama.** B ve C ile karşılaştırma Adım 13'ün işi.
