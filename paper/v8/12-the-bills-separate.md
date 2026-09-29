# Step 12 — Scale does not lock two of the charges together; the third is not tested

**v8 taslağı, üçüncü yazım (Tur 56).** Tur 55 yanıtları: Reynolds bulgusu **modelin içinde bir
ayrıştırma**, nedensel iddia değil (DeepSeek) ve *"in this polar"* bulgu cümlesinin içinde (Grok,
ChatGPT); *"the whole of the fall"* → *"18 percent above"* (DeepSeek); düşük Re belirsizliği **iki
yönlü** ve hafif terim 0,0154 **daha belirsiz olanı** — Adım 10–11 onu taşıyor (DeepSeek; Adım 11'e
çekince eklendi); aralığın uçları fiziksel sınır değil (DeepSeek); Fatura 1–3 **bağlaşık, özdeş değil**
(dördü de; DeepSeek'in "bağlaşım bir sonuçtur" önerisi ChatGPT/Grok'un "özdeşlik değil" sınırıyla
birlikte alındı); *"requires only two non-locked charges"* (ChatGPT). **Kendi bulgum:** Adım 2'nin
başlığı *"The charges behave as one quantity in three currencies"* idi — Adım 12'nin sonucuyla
doğrudan çelişiyordu; iskeletin *"üç bağlaşık fatura"* niyetine göre düzeltildi.

**İkinci yazım (Tur 55).** İskeletin 12. adımı: *"Üç para biriminin gerçekten üç
olduğunun, tek niceliğin üç adı olmadığının kanıtı."*

**Birinci yazım bu vaadi daraltmıştı** (tampon her iki ölçekte de girdi; üç faturadan yalnız
ikisi sınanabiliyor). **İkinci yazım daha büyük bir şeyi düzeltiyor: Fatura 2'nin ölçekle
düşüşünün MEKANİZMASI yanlıştı, ve yanlışlık bir hesap hatasından geliyordu.**

**Tur 55'te ne oldu, kim buldu:**

- **DeepSeek** *"ΔC_D0 ∝ σR²/(qS)"* formülünü sorguladı: sabit bir rotorda kuvvet q ile
  ölçeklenir, katsayı q'dan bağımsız olmalıdır. **Haklıydı.** Denetlerken `aero/heavy_rotor.py`'de
  **üç kurulum hatası** buldum — üçü de ağır hattın hafif hattın değerlerinde kalmasıydı:
  (1) `sifir_tork(c, th, V=V_SEYIR)` varsayılanı tanım anında 30 m/s'ye bağlanmış, denge 30 m/s'de
  çözülüp 40 m/s'nin q'suna bölünmüş; (2) `hover_tasarla` hafif rotorun 2100 rad/s tasarım devrini
  ağır rotora uygulamış — 0,67 m'de **703 m/s tasarım uç hızı**, palet askıda **uç Mach ≈ 1,0**'da;
  (3) göbek 0,015 m'de kalmış (%4,5 R). v7'nin *"dolgunluk düşer, q artar"* mekanizması **bu iki
  hatanın imzasıydı.** Düzeltilmiş hesap: terim **0,0045–0,0100** (hafifin 0,29–0,65'i), dinamik
  basınç **sadeleşiyor**, dolgunluk **artıyor** (0,075 → 0,100), ve düşüşün **tamamı Reynolds
  sayısından** (aynı Re'de ağır rotor hafifin 1,18 katı öder). `aero/heavy-rotor-result.txt`.
- **`paper/build/verify.py` bu hatayı yakalamıyor, YENİDEN ÜRETİYORDU** — aynı varsayılan
  argümanlarla çağırıp 0,0035–0,0074'ü "doğruluyordu." Düzeltildi; artık eski kurulumu reddettiği de
  sınanıyor (benim bulgum).
- **Grok** %5'lik askı/motor oranının motor tarafında *"ikinci bir kural"* taşıdığını söyledi.
  **Haklıydı ve durum daha kötü:** iki yayımlanmış tasarımın motor payı **aynı değil** (1,53 ve
  1,39). Bu `aero/baseline.py`'de **zaten kayıtlıydı** ve Adım 12'ye taşımamıştım — **benim
  ihmalim.** Eşit payla oran %14 değişir.
- **ChatGPT:** *"ayrışma"* değil *"kilitlenmeme"*; başlık; *"any ranking must"* fazla evrensel.
- **DeepSeek ve Qwen:** Fatura 1'i sabit özgül güçle türetmek mümkün. **Doğru, ama türetim Fatura 1'i
  Fatura 3'ün iki niceliğinin fonksiyonu yapıyor** — sınanan şey türetim olur, ayrışma değil.
  DeepSeek'in %1,6'sı **%2,3** olmalı (askı/kg değişimini atlamış).
- **Kendi bulgum:** Adım 12'nin birinci yazımı sabit hatve açığını *"refusing the variable-pitch hub
  costs"* diye göbeğe atfediyordu — **ChatGPT'nin Tur 53'te Adım 11'de yakaladığı aşırı atfın
  aynısı**, Adım 12'ye yayılmamıştı (§3.1). Adım 11'in dili getirildi.
- **Kendi bulgum:** İngilizce yeniden adlandırma commit'i (`d2c181c`) `rotation.py`, `roll.py`,
  `yaw.py` ve `cfd/plate/` altında üç betikte eski modül adlarını bırakmış; betikler **çalışmıyordu.**
  Tablo 15'in sayıları hiçbir betik çıktısında yok; onarılan `rotation.py`'den **%2 içinde** yeniden
  üretiliyor — gövdede yuvarlatıldı.

**Kural denetimi:** hiçbir ağır tasarım MENZİLİ verilmiyor · 3,8× GEÇMİYOR · iki uç **yayımlanmış
çift** (Adım 10 kapanışları değil) · *"harder case"* yalnız rotor terimi için · Adım 13'e
*"kütle faturası devrilir"* iddiası devredilmiyor (Grok).

---

## Scale does not lock two of the charges together; the third is not tested

Section 11 decomposed the three charges on one aircraft, at one size; **this section asks whether they are three quantities or
one quantity under three names**, by changing the size of the aircraft and seeing whether they move together. **The test is deliberately weak**: it can show that two charges are not locked together within this
model; **it cannot show that they are independent in general.**

**The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 10's closures** (Supplement S12).

**Under a twentyfold change of mass, the rotor term of Bill 2 falls to between 0.29 and 0.65 of its light-design value in the section
polars used here, while the Bill 3 ratio changes by 5 to 14 percent.** **Within this model, the two are therefore
not one quantity under two names.**

Within the
blade-element and section-polar model the section Reynolds number accounts for the fall, a decomposition inside the model rather than
a causal claim beyond it, and the light end lies below a Reynolds number of 10⁵, where section drag is hardest to predict. **Of the two
rotor terms, the light one is therefore the less certain — and it is the one Sections 10 and 11 carry.**

**Bill 1 is not tested.** It appears here as the energy buffer, 3.6 percent of take-off mass at 50 kg and 4.0 percent at 1 000 kg, and both figures are inputs (Supplement S12). Whether it is separable from Bill 3 here is not established;
that the two are coupled here is Section 3's claim, and coupling is not identity.

**The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low
Reynolds number.** **It is consistent with the separability Section 2 asserts; it is not a verification of separability as a general
property.**

**Because at least two of the charges are not locked together, a comparison of architectures cannot in general be reduced to a number
that does not depend on how the charges are weighed.** Section 13 examines what the choice of sizing contract does to a ranking, on the
light closures of Section 10 only.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 170 — yazarın notları üzerine kısaltma uygulandı** (Tur 168–169: işlemlerde dört okuyucu + Claude; korunan cümle taşımaları yazar kararı E13). Değişen her paragrafın eski hâli ekin bu adıma ait bölümünde aynen (*"… before the Round 170 shortening"*). Yeni (R) cümleler Tur 170 §2'de okuyucu vetosuna açık; sonuç teyide | `paper/build/v8_round170_texts.py`, `v8_round170_apply.py` |
| **Tur 172 — hesap geçişi (yazar E14, E15; katman 1 okuyucu teyidine)** E15 h, j, k (yazar k için: "Atalet diye bir şey var sonuçta"); ağır tasarım ayrıntıları S12'ye; "Either answer leaves the mechanism claim where it was." kesildi. Eski paragraflar ekte aynen | — |
| **Tur 172 cevapları — j çiftinin tamamlanması (DeepSeek onarım, Grok "weak"):** korunan *"that near-constancy is a property of the constant-disc-loading rule"* eke gitmiş ama nitelediği sonuç (*"specific hover power changes by one percent"*) gövdede kalmıştı — P71 ihlali, benim hatam. Sonuç da S12'ye: *"while the Bill 3 ratio changes by 5 to 14 percent"*. Teyide | DeepSeek, Grok |
| **Tur 155 — birleştirme aşamasının ilk eke taşıması (S), dört okuyucu + Claude; korunan cümle için yazar kararı E10 ("Eke gitsin"):** 7.3 1 083 → ~830 kelime. Eke giden çalışma (S12, "as it stood before the supplement move"): disk yüklemesi ve özgül güç sayıları, 4.19 / 3.98 paragrafı ve korunan *"This paragraph compares the reference pair only."*, rotor terimi değerleri ve Reynolds sayıları, *"three other candidates are excluded"*, tampon türetme cümlesi. Geri konanlar: çap/açıklık 0.35 → 0.47 ve *"Coupling is not identity"* (Grok), *"Either answer leaves the mechanism claim …"* (DeepSeek). Alt başlıklar kaldırıldı | Tur 154 §5; Tur 155 |
| **Tur 149 — L-3 satır 8 uygulandı:** *"from the tip propellers"* → *"from the tip pairs"* | Tur 148 §3 |
| **Tur 108 (Tur 107: dört okuyucu + Claude):** J29 kısa biçim — "The fixed-pitch gap also widens slightly with size, to 16.4 to 22.9 percent at the heavy design (Supplement S12)"; **oylanan sözcüklere olumsuz niteleyici geri eklendi** ("as in Section 11, no variable-pitch counterfactual was computed") — benim önerim onu düşürmüştü; teyide | Tur 107 metni §3(a) |
| **Tur 107 — Adım 12 yeniden kuruldu** (Tur 105–106; dört okuyucu + Claude, hiçbir cümleye veto yok): `drafts/12-recomposed.md` uygulandı; korunan cümlelerin hepsi gövdede. Özgün gövde Ek S12'de tam | `drafts/12-recomposed.md` §3 iz |
| **Tur 70:** ikinci geçiş uygulandı — R1 (Grok; Claude: *sized by one method*, kapsam cümlesi, üstel; Grok/Qwen: *none could be run on the same footing* geri), R2, R3 (DeepSeek; Grok: *blade-section Reynolds number* adı geri), R4, R5 (Grok), D1, D2 (ChatGPT). Dört okuyucu kabul. Değişen paragrafların özgün hâli Ek S12'de — **biri (*"Two conditions travel…"*) eksikti**, çünkü ilk geçişte bütün kalmıştı; `v8_nothing_lost.py` yakaladı, eklendi | Tur 69 metni §4 |
| **Tur 69:** Tur 68 taslağı uygulandı (dört okuyucu: veto yok; Claude). 2 973 → 2 151 kelime; kaybı olan her paragraf Ek S12'de aynen. Korunan listeye eklendi: *"Of the two rotor terms, the light one is therefore the less certain — and it is the one Sections 10 and 11 carry."* | Tur 68 metni §7.2; `paper/build/v8_draft_check.py 12` |
| **Tur 59, metin hazırlanırken:** *"with one exception"* — motor derecesi Section 10'un değiştirdiği bir nicelik; benim Bill 3 parantezim bölümün kendi kuralıyla çelişiyordu (§0.2, düzeltmenin yan hasarı) | Bu bölüm satır 83–88 ve Bill 3 paragrafı |
| **Tur 59:** bu bölümde *light/heavy design* = 50 kg ve 1000 kg referans tasarımları; 4,19 referans çiftinde (10,9 kW / 2,6 kW), Adım 11'in 2,4–3,2'si kapanışlarda; rotor terimi kenar payından önce | DeepSeek (2.2, 2.4), Qwen; `aero/baseline.py` yorum bloğu (2,6/1,7 = 1,53); Adım 11 tablo notu |
| **Tur 58, P3:** her iki cevap da mekanizma iddiasını yerinde bırakır; iddia envantere dayanır | Adım 9 bağımlılık tablosu; Adım 15 |
| Adım 10 yalnız hafif tasarımı kapattı, 52,3–57,5 kg; 1000 kg'da kapanış yok | `aero/closure-result.txt`; Adım 10 satır 109–111 |
| Disk yüklemesi 44,2 / 43,7 kg/m², %1,1 fark | v7 §3.9 satır 1768; §3.8 Tablo 13 |
| Askı gücü 10,9 → 216,2 kW, ×19,8 vs kütle ×20 | v7 §3.9 satır 1769–1771 |
| Özgül askı gücü 0,218 / 0,216 kW/kg, fark %0,6 | hesaplandı: 10,9/50,1 ve 216,2/1000 |
| Askı/motor oranı 4,19 / 3,98, değişim %5 | hesaplandı: 10,9/2,6 ve 216,2/54,3 (v7 Tablo, satır 1619 ve 1683) |
| **Motor payı 1,53 / 1,39** — iki tasarımda farklı | 2,6/1,7 ve 54,3/39,2 (v7 satır 1618–1619, 1682–1683); `aero/baseline.py` satır 447–461 (zaten kayıtlıydı) |
| Eşit payla ağır motor 60,0 kW, oran 3,61, değişim %14 | hesaplandı: 39,2 × 2,6/1,7 = 59,95; 216,2/59,95 |
| Kanat yüklemesi 25,3 → 45,0; açıklık ×3,35, pervane ×4,50; pervane/açıklık 0,35 → 0,47 | v7 §3.9 satır 1824–1827; `verify.py` ölçek blokları |
| 1000 kg'ın üstünde ikinci çift gerekir | v7 §3.9 satır 1830–1831 |
| Çerçeve terimi iki referans tasarımda aynı çarpan (1/1,12) — inşa gereği | `aero/baseline.py` satır 165 ve 463–464 (`LD_temiz = 13,6 × 1,12`); v7 satır 1421–1422 (*"1/1.12 … covering the tip frames alone"*) |
| **Hafif rotor terimi 0,0154, c_l 0,68, dolgunluk 0,0754** | `aero/tip_propeller.py` (bu tur yeniden koşuldu: 0,01535; c_l 0,70'te FM 0,350 — seçimi askı şartı yapıyor) |
| **Ağır rotor terimi 0,0068 (c_l 0,68), aralık 0,0045–0,0100, oran 0,29–0,65** | `aero/heavy-rotor-result.txt` (düzeltilmiş kurulum) |
| Ağır FM 0,75–0,77, askı uç Mach 0,65–0,67 | aynı |
| Disk/kanat alanı 0,127 iki ölçekte de | v7 §3.9 satır 1783–1785 |
| **q deneyi: aynı ağır palet 30 → 40 m/s'de katsayı −%9, q ölçeklemesi −%44 verirdi** | `aero/heavy-rotor-result.txt`, MEKANİZMA bloğu: 0,00748 → 0,00681 |
| **Dolgunluk 0,075 → 0,100 (artıyor)** | aynı; ×1,33 |
| **Medyan kesit Re 8,2×10⁴ → 5,6×10⁵ (×6,8); hafif Re'de ağır palet 0,0181 = hafifin 1,18 katı** | aynı, Re deneyi |
| Kesit kutupları NeuralFoil, NACA 0012 — ölçülmedi | `aero/tip_propeller.py` `kesit_kuvvet`, satır 57 ve 80–85 |
| Düşük Re belirsizliği iki yönlü: hafif terim eşit-Re deneyinde Re ile monoton (düşük Re → büyük terim) | `heavy-rotor-result.txt`: 0,0068 (Re 5,6×10⁵) → 0,0181 (hafif Re'ye indirilmiş) |
| Ağır tasarımın sürükleme braketi yok | v7 §3.8 satır 1750–1754 |
| Ağır yapısal kapanış belirlenmemiş; kabuk üssü ölçülmedi | v7 §3.8 satır 1690–1698 |
| Tampon %3,6 ve %4,0 İKİSİ DE GİRDİ | `aero/mass.py` `m_pil` parametresi; `baseline.py` `f_tampon`; türeten kod yok |
| Açık/kg **bara tabanında** 0,202 → 0,199, düşüş %1,8 (yayımlanmış paylarla) (**Tur 56'da düzeltildi:** önceki 0,166 → 0,162 mil−mil çıkarmasıydı) | `aero/buffer-result.txt` §5 |
| Tampon "Fatura 3'ü motordan kurtaran aygıt" — Adım 3 önceden söyledi | Adım 3 satır 73–79; Adım 11 satır 129–132 |
| Sabit hatve açığı hafif %14,6–21,0, ağır %16,4–22,9 (**birinci yazımda 23,0 idi; betik 22,9 veriyor** — 1 − 0,616/0,80 yuvarlanmış η'dan) — **her ikisi yayımlanmış seyir itkisinde** (L/D 12,0 ve 13,6) | `aero/nose-propeller-crossing.txt`, `aero/nose-propeller-heavy.txt`; `nose_propeller.py` satır 156, `nose_propeller_heavy.py` satır 24 |
| **Geçiş: 2 s → ~220 kW (~%100); 5,1 s → ~13 kW (%6)** — v7 Tablo 15 (221,5 / 13,4) **hiçbir betik çıktısında yok**; onarılan `rotation.py`: 5,1 s'de üçgen profil 127,0 N/çift → 4 çift × 6486 W × (127,0/200,1)^1,5 = **13,1 kW**; ×(5,1/2)³ → **217,6 kW (%101)**. Tablo %2 içinde tutuyor; gövdede yuvarlatıldı | v7 satır 1842–1849; `aero/rotation.py` (bu tur onarıldı) |

**Bu sayfada BİLEREK olmayanlar:**

- **Hiçbir ağır tasarım menzili.** Elimizdeki her biri kısmi: 1.814 km (rotor yüklenmemiş, η_p 0,80),
  1.571 km (rotor yüklenmiş — **ama hatalı 0,0051 ile**, η_p 0,80), 1.398–1.517 km (η_p yeniden
  çözülmüş, rotor yüklenmemiş). Doğru rotor terimi ile hesaplanan η_p'yi birlikte taşıyan kapanış yok.
- **`ΔC_D0 ∝ σR²/(qS)` formülü ve üç haneli uyum.** Mekanizma yanlıştı; formül gövdeden çıktı.
  Gövde **"önceki sürüm"** anlatısı taşımıyor (CLAUDE.md §4); doğru mekanizma şimdiki zamanda yazıldı.
- **3,8× ve batarya özgül gücü.** Adım 14.
- **Kabuk kütlesi Fatura 1 olarak.** Tanımı sınava uydurmak olur.
- **"Fatura 2 fiziksel, Fatura 3 sözleşmesel" çerçevesi (DeepSeek).** Reddedildi: Fatura 2'nin terimi
  de tasarım seçimlerine bağlı (palet tasarımı, seyir hızı; şimdi Reynolds sayısı, yani veter ve hız).
- **Adım 13'e "kütle faturası devrilir" devri.** Grok: 13'ün sözleşmeleri yakıt kesri, yakıt kütlesi,
  kalkış kütlesi tartar; bunlar Fatura 2'ye karşı Fatura 3 değildir. Devir cümlesi yalnız
  *"ağırlık seçimine bağlı"* diyor.
