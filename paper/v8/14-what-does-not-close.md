# Step 14 — What does not close

**v8 taslağı, ikinci yazım (Tur 57).** Tur 56 yanıtları işlendi: *"the aircraft exists"* → *"the loop
closes"* (ChatGPT, Qwen, DeepSeek, Grok); yeniden kapanış **paketin duyarlılığı, ikinci bir uçak değil**
ve %30 gövde kesri iki kat kütlede kanıtlanmamış (Grok, DeepSeek); anma türleri farklı — tepe talep /
tezgâh ortalaması / sürekli / tasarım varsayımı (Grok, ChatGPT); *"obstacle reaches"* paragrafı:
kapalı kütleler, 927–1233 km, Adım 5'in boyutlanan dikey evresi, Adım 13 (Grok, DeepSeek; DeepSeek'in
*"pist iddiası depoya bağlı değil"* görüşü **düzeltildi**: dikey evre bu depoyla boyutlandı); defterin
ucuz dönüşümü (DeepSeek); bilinmeyenler tablosuna beş satır: tampon **enerjisi** (Grok), elektrik yolu
tepe/ısıl (ChatGPT), şerit ve fairing (Qwen — ama Qwen'in iki alıntısı **v7'den**, v8'de yok), durdurulmuş
uç çifti durumu (Grok), yer işletimi ve iniş yükleri (DeepSeek); *"measurement"* → *"validated data"*
(ChatGPT).

**Birinci yazım (Tur 56).** İskeletin 14. adımı: *"Kapanmayanlar — önce batarya, bilinen
engel olarak; sonra bilinmeyenler."* Adım 9 bu bölümü *"bir borç"* diye tanımladı: makalenin
cevaplamadığı ve daha iyi kanıtın cevaplayacağı sorular.

**Bu sayfa yeni bir hesaba dayanıyor:** `aero/buffer.py` → `aero/buffer-result.txt`. Tampon **bara
tabanında** (v7'nin `thrust.py`'de kurduğu istasyon kuralı), Adım 10'un dört kapanışında, ve tampon
özgül güçten **döngünün içinde** türetilerek. Döngü, özgül güç Adım 10'un ima ettiği değere
konunca Adım 10'u birebir üretiyor (üretmezse durur).

**Bu hesap iki yan bulgu çıkardı:**

- **3,8× artık 3,7–4,1×.** Adım 10'un kapanışları yayımlanmış tasarım değil: η_p daha düşük, motor daha
  büyük, kütle daha fazla. Kalkış talebi kapanışlarda 5,5–6,1 kW/kg; 1,49'a oranı 3,7–4,1.
- **Adım 11 ve 12'nin açık sayıları mil−mil çıkarmasıydı** — v7'nin kendi düzelttiği istasyon
  karışıklığı v8'e geri gelmişti. Bara tabanında: Adım 11 0,168–0,188 kW/kg (%12; önce 0,128–0,150,
  %17); Adım 12 0,202 → 0,199 (önce 0,166 → 0,162). **Sonuçlar değişmedi**: en çok tampon isteyen köşe
  yine en az tamponu alıyor; ölçekle değişim yine ~%2.

**Kaynak kuralı (§2.1):** ölçülmüş paket sayıları bu tur PDF'ten okundu. **v7'nin *"the highest rate
yet measured on a flown pack"* ifadesi kaynağa uymuyor:** 1,5 kW/kg **tezgâhtaki 24S1P test paketinde**
ölçüldü, uçan sistem 24S4P; ve *"yet"* aranmamış bir genelleme (§2.2). Gövdede yok.

**Kural denetimi:** 3,8×'in tek evi burası, tek paragraf (Grok, Tur 34) · Adım 10 onu anlatmıyor ·
mekanizma iddiası bu sayfadaki hiçbir kaleme bağlı değil — bu **denetlendi**, aşağıda.

---

## What does not close

Section 10 closed the sizing loop on a declared package and said that whether an aircraft can be
built to it is a different question. **This section is where that question is answered, and for the
first item the answer is no.** Section 9 called this section a debt: questions the paper does not
answer and that better evidence would. It is stated in that order — first the obstacle that is known,
then what is not known.

### First, the known obstacle: the energy store

**Every closure in Section 10 carries a buffer of 3.6 percent of take-off mass.** That figure is an
input, not a result (Sections 11 and 12). What it implies can be computed. Taken at the electrical bus,
where the buffer sits — the rotor demand divided by the machine and power-electronics efficiencies, less
what the engine delivers through its generator — **the four closures ask the buffer for 4.7 to 5.2 kW per kilogram of buffer to hover, and 5.5 to 6.1
kW per kilogram of buffer to leave the ground** with the tip pairs at full
thrust, which is where the take-off margin comes from (Section 5).

**What has been measured is a fraction of that, and the figures available are of four different
kinds.** A 24-series nickel–cobalt–manganese pack designed, bench-tested and flown in a 210 kg-class
electric VTOL aircraft is rated, as a flown system, at 0.892 kW per kilogram continuous; its 13.5 kg
unit pack, discharged on the bench at its highest tested rate of 10.68C, delivered on average about
1.5 kW per kilogram for about four minutes and reached 55.1 °C against the 60 °C limit its authors
adopted. A NASA-funded design study adopts 4 kW per kilogram and describes that figure as about twice
that of existing batteries. The same study notes lithium-polymer figures in the literature as high as
3 kW per kilogram, which it cites rather than measures; against that figure the take-off demand is 1.8
to 2.0 times. The study argues that, because pulse current limits can exceed continuous ones — by more
than a factor of two in one commercial module it cites — a pack with the required specific power may be possible with
existing technology; the study's hover lasts twenty seconds or less, and how long this aircraft's
vertical phases draw the peak is not computed here. **The take-off demand of Section 10's closures is 3.7 to 4.1 times the
bench rate — the highest figure obtained from a measurement — and 6.2 to 6.8 times the flown system's continuous
rating**; hover alone is 3.1 to 3.5 times the bench rate. The comparison is between unlike ratings: a
peak demand held through the vertical phases, a bench average over minutes, a continuous rating, a
design assumption, and a literature figure the study cites without its rating. **The gap is real on every one of them; the factor quoted is peak demand against
bench average.** The package Section 10 closes on does not exist with any store the sources consulted
here report as built.

**Closing the loop on a measured store is a sensitivity of that package, not a second aircraft.** The
buffer is derived inside the loop from the take-off demand at a given specific power; everything else is
Section 10's — the same fractions, including an airframe at thirty percent of take-off mass, and the same
wing loading, disc loading and aspect ratio, so the lift-to-drag ratio is carried unchanged and, with the
fuel fraction held, so is the range. **These masses are the Section 10 package with one input changed.
They are not a structural closure at 100 kg**, and whether the airframe fraction holds at twice the mass
it was set at is not established.

| Buffer specific power, per kilogram of buffer | Take-off mass | Buffer | Change from Section 10 |
|---|---:|---:|---:|
| As Section 10 implies — 5.5 to 6.1 kW kg⁻¹ | 52.3 to 57.5 kg | 3.6 % | — |
| 4 kW kg⁻¹, the design-study assumption | 56.6 to 61.2 kg | 5.0 to 5.5 % | +6 to +8 % |
| About 1.5 kW kg⁻¹, the unit pack's bench rate | 94.6 to 101.2 kg | 13.4 to 14.7 % | **+76 to +81 %** |
| 0.892 kW kg⁻¹, the flown system's continuous rating | about 335 kg | 22 to 25 % | set by nearness to non-closure |
| 0.724 kW kg⁻¹, the unit pack's continuous rating | **does not close** | — | — |

If Section 10's take-off masses are retained instead of re-closing at the bench rate, the
payload falls to about 7 kg rather than 13. At the flown system's continuous rating the loop only just
closes, and the mass it returns is set by how near the loop is to not closing rather than by anything
about the aircraft. At the unit pack's continuous rating it does not close at all.

**This is where the coupling Section 12 found is paid.** The buffer is the conversion the escape
condition permits — kilowatts of hover peak paid in kilograms of store. Section 11's ledger records that
conversion at the assumed store. **The escape from Bill 3 is real in the sense Section 3 defined it, and
its price depends on a component whose required performance has not been demonstrated.**

### What the obstacle reaches, and what it does not

**It reaches every number that describes this aircraft at Section 10's masses.** The closed masses of
52.3 to 57.5 kg and the 13 kg payload assume the store. The ranges of 927 to 1 233 km survive the
re-closure only because the fuel fraction is held, on an aircraft three-quarters heavier; they do not
survive as 13 kg carried that far on a store that has been built. The vertical phase that Section 5
reports as sized was sized with this store in it. And Section 13's orderings were computed with the
store held common at 3.6 percent; how they would move with a measured store is not computed.

**It does not reach the mechanism claim.** Sections 7 and 8 count the classes of mechanism that a
tilting architecture needs to change regime and this one does not; that is a statement about hardware,
and a heavier store adds no pivot. **Nor does it reach the cruise-efficiency comparison of Section 6
as a ratio**: effective lift-to-drag ratio combines aerodynamic and propulsive efficiencies and has no
mass in it. As a comparison of aircraft, that section describes the configuration at Section 10's
masses, which the store does reach.

### Then what is not known

The remaining items are not known obstacles; they are questions this work has not answered. Each is
listed with what would settle it.

- **the pitching moment through the transition** — validated aerodynamic data;
- **section drag at low Reynolds number** — validated data, or a method validated there;
- **the tip pairs' stopped cruise state** — analysis, or a measurement of one stopped state;
- **the buffer's energy, not only its power** — analysis against a defined mission profile;
- **the electrical path at peak** — component sizing and thermal analysis;
- **the airframe's mass** — structural sizing, then a built article;
- **the strip and the fairing** — measurement of both surfaces, and sizing of the actuation;
- **closed-loop hover control**, including the declined reaction-torque channel, the hover torque
  residual, and the allocation of the tip pairs between take-off margin and attitude authority, which
  compete for the same propellers — a control-allocation study, then simulation;
- **vertical descent and the landing transition** — analysis not yet done;
- **ground handling and landing loads** — analysis not yet done;
- **the competitor's lift-group mass** — measured inventories of lift-plus-cruise aircraft of this class;
- **rotor–structure and rotor–wing interference** — inside Bill 2 in principle, absent from the build-up and not
  modelled; analysis not yet done;
- **engine installation** — absent from this work entirely;
- **blade-family selection** — analysis not yet done;
- **atmosphere** — analysis; the direction of its effect on the Section 6 comparison has not been computed.

*(What each item bears on is in the full table, Supplement S14.)*

**None of these is a small correction to a known quantity.** Two of them need validated data rather
than more of the computation already done: the transition moment, because three methods have been
tried against it and disagree, and the low-Reynolds section drag, because the one method used here is
least reliable exactly there.

### What this section amounts to

**The loop closes; the aircraft is not shown to.** At the energy store the paper can name the gap
exactly, in specific power and in take-off mass. Everywhere else it can name only what would settle the
question. **The architecture claim — that the configuration is arranged to change regime with no mechanism that
reorients a propulsor — is a count of hardware, and nothing in this section reaches it.** What this section reaches
is the aircraft, and the paper has not claimed the aircraft.

The last section returns to the four axes of Section 9 and states what is claimed on each.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 95 (14C; dört okuyucu + Claude):** S-20 daraltıldı — "because pulse current limits can exceed continuous ones — by more than a factor of two in one commercial module it cites —" (Barrett'in genel cümlesi yalnız "can have … higher"; iki kat tek modül örneği). S-20 cümlesi korunan (163) | Barrett PDF s. 34; Tur 94 metni §3.3 |
| **Tur 94 (14C; dört okuyucu + Claude):** R-3 — "three different kinds" → "four", ve "unlike ratings" listesine "and a literature figure the study cites without its rating"; S-20 — Barrett'in kendi sonucu eklendi ("The study argues that … may be possible with existing technology; the study's hover lasts twenty seconds or less, and how long this aircraft's vertical phases draw the peak is not computed here"; "The study"/"the study's" ChatGPT'nin göndergesi); "the highest of the measured figures" → "the highest figure obtained from a measurement" (ChatGPT tercih etti, üçü itirazsız). S-19 cümlesi korunan (161). Özgün paragraf Ek S14'te | Barrett PDF s. 32, 34–35; Tur 93 metni §3–§4 |
| **Tur 93 (yeniden kurma, 14C ve 14D; dört okuyucu + Claude):** 14D — "At the bench rate the loop closes about three-quarters heavier, with a buffer of about fourteen percent…" çıktı (tablonun üçüncü satırını yineliyordu); ardından gelen cümle "retained instead," → "retained instead of re-closing at the bench rate," (R-2 onarımı: "instead" silinen cümleye bağlıydı, Grok P51 okuması uygulamadan önce yakaladı). 14C — S-19: Barrett çalışmasının 3 kW/kg alıntısı gövdeye girdi, **alıntı olarak** (çalışma ölçmüyor, kendi kaynağı [60]'ı gösteriyor); 5,5–6,1 / 3 = 1,8–2,0 kat. Özgün 14D paragrafı Ek S14'te | Tur 92 metni §2–§3 |
| **Tur 92 (yeniden kurma, 14E ve 14G; dört okuyucu + Claude):** 14E "at a measured specific power it costs thirteen to fifteen percent of take-off mass instead of 3.6" çıktı (tablonun üçüncü satırının üçüncü söylenişi); 14G son iki cümle çıktı (listede zaten etiketli). "The escape from Bill 3 is real…" korunan (160). Özgün paragraflar Ek S14'te | Tur 91 metni §3 |
| **Tur 66:** listeye rotor–yapı ve rotor–kanat girişimi eklendi (Adım 11'in tablosundan; Adım 14'te eksikti) | Adım 11 sınır cümlesi; Ek S11 |
| **Tur 63:** Tur 62 listesinde *"allocation of the tip pairs between take-off margin and attitude authority"* düşmüştü — Grok yakaladı; geri kondu (Adım 5 ve 7'nin *"ikinci iş"*i) | Ek S14'ün ilgili satırı |
| **Tur 61:** bilinmeyenler tablosu Ek S14'e taşındı; gövdede her kalem ve onu neyin çözeceği (dört okuyucu + Claude hemfikir, A6) | `paper/v8/supplement.md` S14 |
| **Tur 60:** tablo başlığı *"per kilogram of buffer"*; *"50 kg reference geometry"*, *"1 000 kg reference design"* | Grok, terim birliği |
| **Tur 59:** *"arranged to change regime"*; 52,3–57,5 kg; kW/kg **tampon kütlesi başına** | Grok (A, D), Qwen |
| Kapanışlar %3,6 tampon taşıyor; tampon girdi | `closure.py` (`f_tampon=0.036`); Adım 11–12 |
| Bara kuralı: P_mil/(0,92×0,95) − P_motor×0,90 | `aero/thrust.py` satır 21–30 ve 168–170; `aero/buffer.py` |
| Aşkı 4,68–5,23, kalkış 5,53–6,09 kW/kg | `buffer-result.txt` §1 |
| Kalkış talebi = aşkı × (1 + 4×335/10 900) = ×1,123, uç çiftleri tam (T/W 1,132) | `buffer.py` `UC_PAYI`; `thrust.py` |
| **Yu ve ark. 2026:** VS-210, 210 kg sınıfı; 24S4P uçan sistem 892 W/kg sürekli (4×110 A'dan hesaplanmış); 24S1P 13,5 kg | `references/Yu-2025_24S-NCM-battery-eVTOL-IN-FLIGHT_Batteries.pdf`, Tablo 3 (bu tur açıldı) |
| **~1,5 kW/kg türetildi:** 10,68C'de 1394,3 Wh, 4 dk 09 s, 13,5 kg → 1,49 kW/kg ortalama | aynı, deşarj tabloları (satır 707, 759 metin çıktısında) |
| 55,1 °C, sınır 60 °C, ısıl pay 4,9 °C; yerel sıcak noktalar ölçülmemiş | aynı, §3 ve Özet |
| **Barrett ve ark. 2023 (NIAC):** *"the specific power (4 kW/kg) is about twice that of existing batteries"* | `references/Barrett-2023_NIAC_solid-state-EAD-propulsion_MIT.pdf` (bu tur açıldı) |
| Oranlar: kalkış/1,49 = 3,7–4,1; kalkış/0,892 = 6,2–6,8; aşkı/1,49 = 3,1–3,5 | `buffer-result.txt` §1 (aşkı oranı: 4,68/1,49 = 3,14; 5,23/1,49 = 3,51) |
| Döngü tablosu (5 satır); 4 kW/kg satırı +6,5…+8,2 % | `buffer-result.txt` §3; sınama §2 |
| Sabit MTOW'da faydalı yük ~7 kg (7,2–7,4) | `buffer-result.txt` §4 |
| Menzil değişmez (yakıt kesri sabit, L/D sabit) | `buffer.py` döngüsü; Adım 13'ün sözleşme 1 mantığı |
| Etkin L/D = (L/D)·η_p, kütleden bağımsız | Adım 6 |
| Adım 13 tamponu ortak tutuyor | Adım 13 |
| Geçiş: ~10° üstü üç yöntem sapıyor | Adım 10 satır 207–211 |
| **Tepe hücum 17,5° (5 m/s tırmanışla), 21,6° (düz askıdan); iç yarı 4–8° etkin; ölçüm dış yarı için ~22°'ye kadar; zor kısım bağlı akış ucu** | v7 §3.17 satır 2329–2341, §4.4 satır 2651–2654 — **v7 hesabı, bu tur yeniden koşulmadı**; referans geometride |
| Düşük Re, iki yönlü | Adım 12 |
| Kabuk yoğunluğu kırılma 1,783 kg/m², taban 1,50; kurulum yayımlanmış kütlede; %12 belirsizlik payı | `aero/mass.py` çıktısı (bu tur koşuldu): *"kabuk kg/m2 taban 1.50 -> kirilma 1.783"*, *"belirsizlik payi (kurunun %12'i)"* |
| Kabuk üssü ölçülmedi (ağır) | Adım 12 |
| Kaldırma grubu kesri işareti belirliyor | Adım 13 |
| Kontrol, girdap halkası, iniş geçişi, motor yerleşimi | Adım 5; Adım 11 *"What the closure does not contain"* |
| Tampon enerjisi: 10,68C'de birim paket 4 dk 09 s'de boşaldı | Yu ve ark., deşarj tablosu (`buffer.py` docstring) |
| Durdurulmuş hâl: yöntem ve azimut sabitlenmemiş | Adım 8 satır 195–201 |
| Şerit: gövde yatış ekseni, seyirde yatış, askıda yön değişimi | Adım 8 satır 163–167 (§0.1) |
| Fairing: C_n_β > 0,001/° ölçütüne göre 39 mm; yan kuvvet ölçülmedi | Adım 8 satır 121–127 |
| Şerit eyleyicisi boyutlandırılmadı | Adım 11 tablosu |
| Yan rüzgâr: duruş tabanı bir parametre | Adım 5 satır 104–106 |
| Yeniden kapanış: kanat/disk yüklemesi ve AR sabit → L/D sabit; yakıt kesri sabit → menzil sabit; rotor terimi büyük kütlede yeniden hesaplanmadı | `buffer.py` `kapat_ozgul` |
| Deniz seviyesi; NASA görevi 5000 ft ISA+20 | Adım 6 satır 182–185 |

**Bu sayfada BİLEREK olmayanlar:**

- **Ağır tasarımın tamponu.** Ağır tasarımın kapanışı yok (Adım 12).
- **Tampon ölçüldüğünde lift+cruise'a ne olduğu.** v7 lift+cruise'un daha çok acı çektiğini söylüyordu
  (askı gücü/kütle en yüksek); aynı disk yüklemesinde bu **denetlenmedi** ve iddia edilmedi.
- **"Bataryalar gelişiyor" iyimserliği.** Gelecek özgül güç tahmini yok.
- **Motor pay farkı (1,53 / 1,39).** Yalnız Adım 12'yi etkiliyor, orada söylendi.
